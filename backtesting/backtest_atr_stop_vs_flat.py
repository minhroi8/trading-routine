"""
ATR-based stop vs flat -8% stop — head-to-head PEAD backtest.

Same candidate set, same entry rules, same trailing/time exits. The ONLY thing
that changes between the two variants is the initial stop-loss and the position
size:

  V0 (baseline):  flat -8% stop, position = 11% of equity ($11k on $100k).
  V1 (ATR stop):  stop distance = 2 x 14d ATR, floored at 4%, capped at 8% of
                  entry. Position sized so (stop$ x shares) = 0.9% of equity,
                  but never above 11% of equity (hard notional cap).

Reuses the validated engine helpers from backtest_pead_2026_ytd.py for the
universe, data fetch, and entry filters (EPS surprise >=15%, vol >=1.5x,
relative strength vs SPY > 0, new 52-wk high within 45d, price/$-vol floors,
entry 2 trading days after earnings). Only the exit simulation is rewritten
here so we can swap the stop rule and model the 1/3 scale-out.

Periods: 2022-2024 (in-sample), 2025 (OOS), 2026 YTD (through 2026-06-25).
"""

import os
import sys
import pickle
import time
import warnings
from datetime import timedelta, datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# Run from repo root so `import backtest_pead_2026_ytd` resolves.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import yfinance as yf
import backtest_pead_2026_ytd as eng

# Widen the engine's fetch window for the full 2022 -> 2026-06-25 span.
eng.HIST_START = "2020-06-01"     # deep lookback for 52-wk high + 14d ATR into early 2022
eng.DATA_END   = "2026-06-26"     # today is 2026-06-25; include latest bar

# ─── PATHS ────────────────────────────────────────────────────────────────────
HERE        = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR   = os.path.join(HERE, "data_cache")
REPORTS_DIR = os.path.join(HERE, "reports")
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# ─── CONFIG ───────────────────────────────────────────────────────────────────
TEST_START = "2022-01-01"
TEST_END   = "2026-06-25"

EQUITY        = 100_000.0     # reference portfolio equity
POS_CAP_PCT   = 0.11          # 11% notional cap (V0 size, V1 hard cap)
POS_CAP_DOLLAR = EQUITY * POS_CAP_PCT          # $11,000
RISK_PCT      = 0.009         # V1 target dollar risk = 0.9% of equity
RISK_DOLLAR   = EQUITY * RISK_PCT              # $900

TRAIL_PCT     = 0.07          # trail 7% below peak (both variants)
TRAIL_TRIGGER = 0.10          # scale 1/3 once up +10%, then trail the rest
SCALE_FRAC    = 1.0 / 3.0     # fraction sold at the +10% trigger
TIME_STOP     = 42            # calendar days

ATR_PERIOD    = 14
ATR_MULT      = 2.0
ATR_FLOOR_PCT = 4.0
ATR_CAP_PCT   = 8.0
FLAT_STOP_PCT = 8.0

NOISE_WINDOW  = 5             # trading days; a stop inside this = "noise stop"
MU_ATR_THRESHOLD = 3.0       # daily ATR > 3% of price = high-vol name


# ─── DATA SOURCING ────────────────────────────────────────────────────────────
# The earnings/EPS-surprise endpoint hard-rate-limits the plain-requests yfinance
# backend, and the curl_cffi backend cannot traverse this environment's egress
# proxy (BoringSSL CONNECT failure). But the *entry set* (which already encodes
# every entry filter: EPS surprise >=15%, vol >=1.5x, RS>0, new-52wk-high<=45d) is
# already materialised in this repo's existing candidate CSVs. So we read entries
# from disk and fetch ONLY daily OHLC paths (the chart endpoint, which works).

HIST_FETCH_START = "2021-10-01"     # >= 15 trading days before earliest 2022 entry (for 14d ATR)
HIST_FETCH_END   = "2026-06-26"

CAND_2022_2025 = os.path.join(REPO_ROOT, "backtest_trades_PEAD_2022_2025_ENHANCED_base.csv")
CAND_2026      = os.path.join(REPO_ROOT, "backtest_trades_PEAD_2026_YTD.csv")


import requests as _rq

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_P1 = int(pd.Timestamp(HIST_FETCH_START).timestamp())
_P2 = int(pd.Timestamp(HIST_FETCH_END).timestamp())


def _fetch_chart(ticker):
    """Daily auto-adjusted OHLCV via Yahoo's chart API (raw requests — bypasses
    yfinance's rate-limited crumb/session flow)."""
    sym = ticker.replace(".", "-")
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        url = (f"https://{host}/v8/finance/chart/{sym}"
               f"?period1={_P1}&period2={_P2}&interval=1d&events=div%2Csplits")
        for attempt in range(4):
            try:
                r = _rq.get(url, timeout=30, headers={"User-Agent": _UA})
                if r.status_code == 429:
                    time.sleep(3 * (attempt + 1))
                    continue
                if r.status_code != 200:
                    break
                res = r.json()["chart"]["result"][0]
                ts = res.get("timestamp")
                if not ts:
                    return None
                q = res["indicators"]["quote"][0]
                adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
                idx = (pd.to_datetime(ts, unit="s", utc=True)
                       .tz_convert("America/New_York").normalize().tz_localize(None))
                df = pd.DataFrame({
                    "Open": q["open"], "High": q["high"], "Low": q["low"],
                    "Close": q["close"], "Volume": q["volume"],
                }, index=idx)
                if adj is not None:
                    a = pd.Series(adj, index=idx)
                    factor = a / df["Close"]
                    for col in ("Open", "High", "Low"):
                        df[col] = df[col] * factor
                    df["Close"] = a
                df = df.dropna(subset=["Open", "High", "Low", "Close"])
                if len(df) > 60:
                    return df
                return None
            except Exception:
                time.sleep(2 * (attempt + 1))
    return None


def cached_history(ticker):
    """Disk-cached daily auto-adjusted OHLCV for one ticker."""
    path = os.path.join(CACHE_DIR, ticker.replace("/", "_").replace("\\", "_") + ".pkl")
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    hist = _fetch_chart(ticker)
    if hist is not None:
        try:
            with open(path, "wb") as f:
                pickle.dump(hist, f)
        except Exception:
            pass
    time.sleep(0.3)
    return hist


def load_candidates():
    """Build the entry set from existing repo CSVs, applying the full entry stack
    (EPS surprise >=15% & vol >=1.5x & RS>0 & new 52-wk high <=45d)."""
    a = pd.read_csv(CAND_2022_2025)
    a = a[a.f_surprise15 & a.f_vol15x & a.f_rs & a.f_52w].copy()
    a = a[["ticker", "sector", "is_it", "year", "earn_date", "entry_date",
           "entry_price", "surprise_pct"]]

    b = pd.read_csv(CAND_2026)
    b = b[b.f_surprise15 & b.f_vol15x & b.f_rs & b.f_52w].copy()
    b = b[["ticker", "sector", "is_it", "earn_date", "entry_date",
           "entry_price", "surprise_pct"]]
    b["entry_date_ts"] = pd.to_datetime(b["entry_date"])
    b["year"] = b["entry_date_ts"].dt.year
    b = b.drop(columns=["entry_date_ts"])

    cand = pd.concat([a, b], ignore_index=True)
    cand = cand.drop_duplicates(subset=["ticker", "entry_date"]).reset_index(drop=True)
    return cand


# ─── ATR (no lookahead: uses the 14 completed days before entry) ──────────────
def atr_pct_at_entry(hist, entry_date, period=ATR_PERIOD):
    entry_date = pd.Timestamp(entry_date).normalize()
    prior = hist[hist.index < entry_date]
    if len(prior) < period + 1:
        return None
    w = prior.tail(period + 1).copy()
    high = w["High"].values
    low = w["Low"].values
    close = w["Close"].values
    prev_close = close[:-1]
    tr = np.maximum.reduce([
        high[1:] - low[1:],
        np.abs(high[1:] - prev_close),
        np.abs(low[1:] - prev_close),
    ])
    atr = np.mean(tr)
    entry_open_row = hist[hist.index == entry_date]
    if entry_open_row.empty:
        return None
    entry_price = entry_open_row["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price <= 0:
        return None
    return float(atr / entry_price * 100.0)


def effective_atr_stop_pct(atr_pct):
    """2x ATR, floored at 4%, capped at 8%."""
    raw = ATR_MULT * atr_pct
    return min(ATR_CAP_PCT, max(ATR_FLOOR_PCT, raw))


# ─── TRADE SIMULATION (parametric stop + 1/3 scale-out) ──────────────────────
def simulate(hist, entry_date, hard_stop_pct, trail_pct=TRAIL_PCT):
    """Simulate one trade with a hard stop at -hard_stop_pct%, +10% scale of 1/3,
    7% trailing on the remaining 2/3, and a 42-cal-day time stop.

    Returns dict with blended return_pct (position-weighted across the scale-out),
    exit_reason, holding_days, stop_fired (bool), stop_first5 (bool)."""
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data = hist[hist.index == entry_date]
    if day_data.empty:
        return None
    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < eng.MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1.0 - hard_stop_pct / 100.0)
    future = hist[hist.index >= entry_date]

    booked = 0.0           # realized return contribution from the 1/3 scale-out
    open_frac = 1.0        # fraction of position still held
    scaled = False
    trail_active = False
    highest = entry_price

    for i, (dt, row) in enumerate(future.iterrows()):
        close = row["Close"]
        if pd.isna(close):
            continue
        if close > highest:
            highest = close
        cal_days = (dt - entry_date).days

        # 1) hard stop — only relevant before the +10% scale-out
        if not scaled and close <= hard_stop_price:
            ret = (close - entry_price) / entry_price
            return _result(dt, ret, "hard_stop", cal_days,
                           stop_fired=True, stop_first5=(i < NOISE_WINDOW),
                           entry_price=entry_price)

        # 2) +10% scale-out: book 1/3 at the +10% level, trail the rest
        if not scaled and close >= entry_price * (1.0 + TRAIL_TRIGGER):
            booked += SCALE_FRAC * TRAIL_TRIGGER
            open_frac = 1.0 - SCALE_FRAC
            scaled = True
            trail_active = True

        # 3) trailing stop on the remaining position
        if trail_active:
            trail_stop = highest * (1.0 - trail_pct)
            if close <= trail_stop:
                ret_open = (close - entry_price) / entry_price
                total = booked + open_frac * ret_open
                return _result(dt, total, "trail_stop", cal_days,
                               stop_fired=False, stop_first5=False,
                               entry_price=entry_price)

        # 4) time stop
        if cal_days >= TIME_STOP:
            ret_open = (close - entry_price) / entry_price
            total = booked + open_frac * ret_open
            return _result(dt, total, "time", cal_days,
                           stop_fired=False, stop_first5=False,
                           entry_price=entry_price)

    last = future.iloc[-1]
    ret_open = (last["Close"] - entry_price) / entry_price
    total = booked + open_frac * ret_open
    return _result(last.name, total, "data_end",
                   (last.name - entry_date).days,
                   stop_fired=False, stop_first5=False, entry_price=entry_price)


def _result(dt, ret, reason, days, stop_fired, stop_first5, entry_price):
    return {
        "exit_date": dt.date(),
        "return_pct": ret * 100.0,
        "exit_reason": reason,
        "holding_days": days,
        "stop_fired": stop_fired,
        "stop_first5": stop_first5,
        "entry_price": entry_price,
    }


# ─── SIMULATE BOTH VARIANTS OVER THE CANDIDATE SET ────────────────────────────
def build_trades():
    cand = load_candidates()
    tickers = sorted(cand["ticker"].unique())
    print(f"Candidate entries: {len(cand)} over {len(tickers)} tickers")

    # Fetch (and cache) daily OHLC paths for each unique ticker.
    hist_map = {}
    for i, t in enumerate(tickers):
        if i % 25 == 0:
            print(f"  fetching {i}/{len(tickers)} ({sum(v is not None for v in hist_map.values())} ok)...")
        hist_map[t] = cached_history(t)
    n_ok = sum(v is not None for v in hist_map.values())
    print(f"  history fetched: {n_ok}/{len(tickers)} tickers")

    rows = []
    no_hist = no_entry = 0
    for _, c in cand.iterrows():
        t = c["ticker"]
        hist = hist_map.get(t)
        if hist is None:
            no_hist += 1
            continue
        entry_date = pd.Timestamp(c["entry_date"]).normalize()
        dd = hist[hist.index == entry_date]
        if dd.empty:
            no_entry += 1
            continue
        open_price = dd["Open"].iloc[0]
        if pd.isna(open_price) or open_price <= 0:
            no_entry += 1
            continue

        atrp = atr_pct_at_entry(hist, entry_date)
        if atrp is None:
            no_entry += 1
            continue
        eff_stop = effective_atr_stop_pct(atrp)

        v0 = simulate(hist, entry_date, FLAT_STOP_PCT)
        v1 = simulate(hist, entry_date, eff_stop)
        if v0 is None or v1 is None:
            no_entry += 1
            continue

        pos_v0 = POS_CAP_DOLLAR
        pos_v1_uncapped = RISK_DOLLAR / (eff_stop / 100.0)
        pos_v1 = min(POS_CAP_DOLLAR, pos_v1_uncapped)
        v1_capped = pos_v1_uncapped > POS_CAP_DOLLAR

        rows.append({
            "ticker": t, "sector": c["sector"], "is_it": bool(c["is_it"]),
            "year": int(c["year"]),
            "earn_date": c["earn_date"], "entry_date": entry_date.date(),
            "entry_price": round(float(open_price), 4),
            "surprise_pct": round(float(c["surprise_pct"]), 2) if pd.notna(c["surprise_pct"]) else None,
            "atr_pct": round(atrp, 3),
            "eff_stop_pct": round(eff_stop, 3),
            "pos_v1_dollar": round(pos_v1, 2),
            "v1_capped": v1_capped,
            "v0_return_pct": round(v0["return_pct"], 3),
            "v0_exit_reason": v0["exit_reason"],
            "v0_holding_days": v0["holding_days"],
            "v0_stop_fired": v0["stop_fired"],
            "v0_stop_first5": v0["stop_first5"],
            "v0_return_dollar": round(v0["return_pct"] / 100.0 * pos_v0, 2),
            "v1_return_pct": round(v1["return_pct"], 3),
            "v1_exit_reason": v1["exit_reason"],
            "v1_holding_days": v1["holding_days"],
            "v1_stop_fired": v1["stop_fired"],
            "v1_stop_first5": v1["stop_first5"],
            "v1_return_dollar": round(v1["return_pct"] / 100.0 * pos_v1, 2),
        })

    print(f"\nSimulated trades: {len(rows)}, no-history: {no_hist}, no-entry/skip: {no_entry}")
    return pd.DataFrame(rows)


# ─── METRICS ──────────────────────────────────────────────────────────────────
def variant_stats(df, prefix):
    """prefix = 'v0' or 'v1'."""
    rp = df[f"{prefix}_return_pct"]
    rd = df[f"{prefix}_return_dollar"]
    if df.empty:
        return None
    winners = df[rp > 0]
    losers = df[rp <= 0]
    gw = winners[f"{prefix}_return_dollar"].sum()
    gl = abs(losers[f"{prefix}_return_dollar"].sum())
    pf = gw / gl if gl > 0 else float("inf")

    # max consecutive losses by entry order
    s = df.sort_values("entry_date")[f"{prefix}_return_pct"]
    cur = mx = 0
    for r in s:
        if r <= 0:
            cur += 1
            mx = max(mx, cur)
        else:
            cur = 0

    stops = df[df[f"{prefix}_stop_fired"]]
    first5 = stops[stops[f"{prefix}_stop_first5"]]
    return {
        "trades": len(df),
        "win_rate": round((rp > 0).mean() * 100, 1),
        "avg_return": round(rp.mean(), 2),
        "median_return": round(rp.median(), 2),
        "avg_winner": round(winners[f"{prefix}_return_pct"].mean(), 2) if not winners.empty else 0.0,
        "avg_loser": round(losers[f"{prefix}_return_pct"].mean(), 2) if not losers.empty else 0.0,
        "profit_factor": round(pf, 2) if pf != float("inf") else float("inf"),
        "max_consec_loss": mx,
        "avg_holding_days": round(df[f"{prefix}_holding_days"].mean(), 1),
        "total_pnl": round(rd.sum(), 0),
        "n_stops": len(stops),
        "n_stops_first5": len(first5),
        "noise_stop_rate": round(len(first5) / len(stops) * 100, 1) if len(stops) else None,
        "first5_of_all": round(len(first5) / len(df) * 100, 1) if len(df) else None,
        "exit_reasons": df[f"{prefix}_exit_reason"].value_counts().to_dict(),
    }


def pf_str(v):
    return "∞" if v == float("inf") else f"{v}"


PERIODS = [
    ("2022-2024", lambda d: d[d.year.isin([2022, 2023, 2024])]),
    ("2025",      lambda d: d[d.year == 2025]),
    ("2026 YTD",  lambda d: d[d.year == 2026]),
]


def atr_distribution(df):
    """Histogram buckets of effective stop % used by V1."""
    eff = df["eff_stop_pct"]
    buckets = {
        "4% (floor)":  ((eff <= 4.0 + 1e-9)).sum(),
        "4–5%":        ((eff > 4.0 + 1e-9) & (eff < 5.0)).sum(),
        "5–6%":        ((eff >= 5.0) & (eff < 6.0)).sum(),
        "6–7%":        ((eff >= 6.0) & (eff < 7.0)).sum(),
        "7–8%":        ((eff >= 7.0) & (eff < 8.0 - 1e-9)).sum(),
        "8% (cap)":    ((eff >= 8.0 - 1e-9)).sum(),
    }
    return buckets


# ─── REPORT ───────────────────────────────────────────────────────────────────
def build_report(df):
    L = []
    A = L.append
    A("# Backtest: ATR-Based Stop (V1) vs Flat −8% Stop (V0)")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} — "
      f"window {TEST_START}→{TEST_END}, S&P 500 current constituents (survivorship-biased).*\n")
    A("Same candidate set, same entry rules, same trailing/time exits. Only the initial "
      "stop-loss and position size differ between the two variants.\n")
    A("- **V0 (baseline):** flat −8% stop; position = 11% of equity ($11k on $100k).")
    A("- **V1 (ATR stop):** stop = 2×14-day ATR, floored at 4%, capped at 8%; position sized "
      "to risk 0.9% of equity, hard-capped at 11% of equity.\n")
    A("Both variants scale out 1/3 at +10% and trail the remaining 2/3 by 7% below the peak; "
      "42-calendar-day time stop.\n")

    # Pre-compute per-period stats
    per = {}
    for pname, sel in PERIODS:
        sub = sel(df)
        per[pname] = (variant_stats(sub, "v0"), variant_stats(sub, "v1"), sub)

    # ── 1. VERDICT ──
    A("## 1. Verdict\n")
    # Decide winner by avg return + profit factor across periods, weighted by trade count
    v0_avg_all = round(df["v0_return_pct"].mean(), 2)
    v1_avg_all = round(df["v1_return_pct"].mean(), 2)
    v0_pf_all = variant_stats(df, "v0")["profit_factor"]
    v1_pf_all = variant_stats(df, "v1")["profit_factor"]
    winner = "V1 (ATR stop)" if (v1_avg_all > v0_avg_all) else "V0 (flat −8%)"
    A(f"Across the full sample ({len(df)} trades), **V0 avg/trade = {v0_avg_all}%** "
      f"(PF {pf_str(v0_pf_all)}) vs **V1 avg/trade = {v1_avg_all}%** (PF {pf_str(v1_pf_all)}). "
      f"_Winner per-period detail below._\n")
    A("**Mechanical note that drives everything:** the V1 stop is `min(8%, max(4%, 2×ATR))`, so it "
      "is **always ≤ the flat 8% stop** — it can only ever be tighter, never wider. And the 0.9% "
      "risk-sizing target implies a notional of `$900 / stop_frac`, which is **≥ $11,250 even at the "
      "8% cap** — so the 11% ($11k) notional cap binds on **100% of V1 trades** (verified: every "
      "single one). The 0.9% risk-target never actually applies. Net effect: "
      "V1 is, in practice, *the same ~$11k position as V0 but with an equal-or-tighter stop.* "
      "Tighter stops cut the size of each loss but fire more often (more noise stops).\n")

    # ── 2. COMPARISON TABLE ──
    A("## 2. Comparison Table — V0 vs V1 by period\n")
    A("| Period | Var | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | MaxConsecL | AvgHold | Total P&L |")
    A("|--------|-----|-------:|-----:|-----:|-----:|--------:|---------:|---:|-----------:|--------:|----------:|")
    for pname, _ in PERIODS:
        s0, s1, _ = per[pname]
        for tag, s in [("V0", s0), ("V1", s1)]:
            if s is None:
                A(f"| {pname} | {tag} | 0 | — | — | — | — | — | — | — | — | — |")
                continue
            A(f"| {pname} | {tag} | {s['trades']} | {s['win_rate']}% | {s['avg_return']}% | "
              f"{s['median_return']}% | {s['avg_winner']}% | {s['avg_loser']}% | {pf_str(s['profit_factor'])} | "
              f"{s['max_consec_loss']} | {s['avg_holding_days']}d | ${s['total_pnl']:,.0f} |")
    A("")
    A("_Position size is ~$11k for both variants (the 11% cap binds for V1), so the P&L "
      "and profit-factor deltas come purely from the different stop paths._\n")

    # ── 3. NOISE STOP ANALYSIS ──
    A("## 3. Noise-Stop Analysis (stops inside first 5 trading days)\n")
    A("| Period | Var | #Stops | #Stops in first 5d | Noise-stop rate | First-5d stops as % of all trades |")
    A("|--------|-----|-------:|-------------------:|----------------:|----------------------------------:|")
    for pname, _ in PERIODS:
        s0, s1, _ = per[pname]
        for tag, s in [("V0", s0), ("V1", s1)]:
            if s is None:
                continue
            nr = f"{s['noise_stop_rate']}%" if s['noise_stop_rate'] is not None else "—"
            fa = f"{s['first5_of_all']}%" if s['first5_of_all'] is not None else "—"
            A(f"| {pname} | {tag} | {s['n_stops']} | {s['n_stops_first5']} | {nr} | {fa} |")
    A("")
    s0a = variant_stats(df, "v0")
    s1a = variant_stats(df, "v1")
    A(f"**Did V1 reduce first-5-day stop-outs?** Full sample: V0 had {s0a['n_stops_first5']} "
      f"first-5-day stops ({s0a['first5_of_all']}% of all trades); V1 had {s1a['n_stops_first5']} "
      f"({s1a['first5_of_all']}%). Because the ATR stop is never wider than the flat 8% stop, V1 "
      f"{'did NOT reduce' if s1a['n_stops_first5'] >= s0a['n_stops_first5'] else 'reduced'} early "
      f"stop-outs — {'it produced at least as many' if s1a['n_stops_first5'] >= s0a['n_stops_first5'] else 'it produced fewer'}.\n")

    # ── 4. ATR DISTRIBUTION ──
    A("## 4. ATR Stop-Width Distribution (V1) — validates the 4–8% collar\n")
    A("| Effective stop bucket | Trades | Share |")
    A("|-----------------------|-------:|------:|")
    dist = atr_distribution(df)
    n = len(df)
    for b, c in dist.items():
        A(f"| {b} | {c} | {round(c / n * 100, 1) if n else 0}% |")
    A("")
    floored = dist["4% (floor)"]
    capped = dist["8% (cap)"]
    A(f"Mean effective V1 stop: **{round(df['eff_stop_pct'].mean(), 2)}%** "
      f"(vs flat 8% for V0). {round(floored / n * 100, 1)}% of trades hit the 4% floor, "
      f"{round(capped / n * 100, 1)}% hit the 8% cap. Mean entry-day ATR: "
      f"{round(df['atr_pct'].mean(), 2)}% of price.\n")

    # ── 5. MU-STYLE HIGH-ATR ANALYSIS ──
    A("## 5. MU-Style Analysis — high-ATR semiconductor / IT names\n")
    hi = df[(df.is_it) & (df.atr_pct > MU_ATR_THRESHOLD)]
    A(f"Filter: IT-sector names with daily ATR > {MU_ATR_THRESHOLD}% of price. "
      f"Matched **{len(hi)}** trades.\n")
    if not hi.empty:
        v0_first5 = hi[hi.v0_stop_first5]
        v1_first5 = hi[hi.v1_stop_first5]
        # "avoided" = V0 noise-stopped but V1 did NOT
        avoided = hi[hi.v0_stop_first5 & ~hi.v1_stop_first5]
        added = hi[~hi.v0_stop_first5 & hi.v1_stop_first5]
        A(f"- Mean ATR of these names: {round(hi.atr_pct.mean(), 2)}%/day → mean V1 stop "
          f"{round(hi.eff_stop_pct.mean(), 2)}% (vs flat 8%).")
        A(f"- V0 first-5-day noise stops: **{len(v0_first5)}**.")
        A(f"- V1 first-5-day noise stops: **{len(v1_first5)}**.")
        A(f"- V0 noise stops *avoided* under V1: **{len(avoided)}**.")
        A(f"- *New* noise stops V1 introduced (V0 survived, V1 stopped early): **{len(added)}**.")
        A(f"- V0 avg return on these names: {round(hi.v0_return_pct.mean(), 2)}%; "
          f"V1 avg: {round(hi.v1_return_pct.mean(), 2)}%.\n")
        A("Because 2×ATR for these names is **at or above the 8% cap only when daily ATR ≥ 4%** — "
          "and is *tighter* than 8% whenever daily ATR is 2–4% — the ATR rule as specified gives "
          "high-vol names an **equal-or-tighter** stop than the flat 8%. It therefore cannot rescue "
          "the MU-style noise stop the proposal was designed to avoid: to widen the stop on a volatile "
          "name you would need to *raise or remove the 8% cap*, not add an ATR term beneath it.\n")
    else:
        A("_No IT names with daily ATR > 3% in the candidate set._\n")

    # ── 6. RECOMMENDATION ──
    A("## 6. Recommendation\n")
    better_periods = sum(1 for pname, _ in PERIODS
                         if per[pname][1] and per[pname][0]
                         and per[pname][1]["avg_return"] > per[pname][0]["avg_return"])
    A(f"V1 beat V0 on average return in **{better_periods} of 3** periods. ")
    if v1_avg_all > v0_avg_all and v1_pf_all != float("inf") and v1_pf_all >= v0_pf_all:
        rec = ("**Lean adopt V1**, but only on the strength of smaller losses per stop — not on the "
               "noise-stop thesis, which the math refutes. Recommend a **hybrid**: keep ATR sizing "
               "for the *floor* (tighten stops on quiet names) but **raise the cap above 8%** (e.g. "
               "3×ATR capped at 12%) if the real goal is to give volatile names room to breathe.")
    else:
        rec = ("**Keep V0.** V1's tighter-only stops increase early stop-outs without a compensating "
               "return edge, and the 8% cap means it never delivers the wider stop the proposal "
               "intended for volatile names. If the goal is genuinely to avoid noise stops on high-ATR "
               "names, the fix is to **raise/remove the 8% cap** (let the ATR term widen the stop), "
               "not to add an ATR floor beneath an unchanged cap.")
    A(rec + "\n")
    A("---\n**Methodology / data provenance.** The *entry set* (every trade that passed the full "
      "entry stack — EPS surprise ≥15%, announcement volume ≥1.5×, relative strength >0 vs SPY, "
      "new 52-wk high ≤45d, price ≥$10, 20-day $-vol ≥$20M, entry day+2 at open) is read from this "
      "repo's existing validated candidate files "
      "(`backtest_trades_PEAD_2022_2025_ENHANCED_base.csv` + `backtest_trades_PEAD_2026_YTD.csv`), so "
      "both variants run on an identical, already-validated candidate set. Daily auto-adjusted OHLC "
      "paths were re-fetched from Yahoo's chart API and cached under `backtesting/data_cache/`; ATR, "
      "entry fills, stops and the 1/3 scale-out are all simulated on that fresh series. Survivorship "
      "bias (current S&P 500 constituents) and zero transaction costs apply, as in all prior reports "
      "in this repo. Relative-strength was measured earnings-close→entry-eve (no lookahead at the "
      "day+2 open).*")
    return "\n".join(L)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    df = build_trades()
    if df.empty:
        print("No candidates generated.")
        sys.exit(1)

    # Save per-variant trade CSVs
    v0_cols = ["ticker", "sector", "is_it", "year", "earn_date", "entry_date", "entry_price",
               "surprise_pct", "atr_pct",
               "v0_return_pct", "v0_exit_reason", "v0_holding_days", "v0_stop_fired",
               "v0_stop_first5", "v0_return_dollar"]
    v1_cols = ["ticker", "sector", "is_it", "year", "earn_date", "entry_date", "entry_price",
               "surprise_pct", "atr_pct", "eff_stop_pct", "pos_v1_dollar", "v1_capped",
               "v1_return_pct", "v1_exit_reason", "v1_holding_days", "v1_stop_fired",
               "v1_stop_first5", "v1_return_dollar"]
    df[v0_cols].to_csv(os.path.join(REPORTS_DIR, "backtest_trades_ATR_STOP_V0.csv"), index=False)
    df[v1_cols].to_csv(os.path.join(REPORTS_DIR, "backtest_trades_ATR_STOP_V1.csv"), index=False)

    report = build_report(df)
    rpath = os.path.join(REPORTS_DIR, "backtest_report_ATR_STOP_VS_FLAT.md")
    with open(rpath, "w", encoding="utf-8") as f:
        f.write(report)

    # Console summary
    print("\n=== HEADLINE ===")
    for pname, sel in PERIODS:
        sub = sel(df)
        s0 = variant_stats(sub, "v0")
        s1 = variant_stats(sub, "v1")
        if s0 is None:
            print(f"{pname}: no trades")
            continue
        print(f"{pname}: n={s0['trades']} | "
              f"V0 win {s0['win_rate']}% avg {s0['avg_return']}% PF {pf_str(s0['profit_factor'])} "
              f"noise {s0['noise_stop_rate']}% | "
              f"V1 win {s1['win_rate']}% avg {s1['avg_return']}% PF {pf_str(s1['profit_factor'])} "
              f"noise {s1['noise_stop_rate']}%")
    print(f"\nReport: {rpath}")


if __name__ == "__main__":
    main()
