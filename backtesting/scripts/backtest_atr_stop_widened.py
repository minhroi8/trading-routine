"""
Wider ATR-scaled stop vs flat -8% stop -- head-to-head PEAD backtest.

This is the actual S3 proposal from memory/lessons.md (as ranked STRONG in
backtesting/strategy_review_log.md, 2026-06-30 run): for high-ATR names,
widen the initial stop instead of using a flat -8%, and shrink the position
size proportionally so dollar risk per trade stays constant.

  V0 (baseline): flat -8% stop, position = 11% of equity ($11k on $100k).
  V2 (wider ATR stop): stop = max(8%, 2 x 14d ATR%) -- a FLOOR at 8%, no cap.
                        Position sized so (stop% x notional) = 0.8% of equity,
                        hard-capped at 11% of equity.

This differs from the already-rejected V1 variant in
backtest_report_ATR_STOP_VS_FLAT.md, whose stop was `min(8%, max(4%, 2xATR))`
(a CEILING at 8%, so it could only ever be tighter than flat -- never wider).
V2 removes that ceiling, which is the mechanical change the S3 proposal and
the V1 report's own recommendation both call for ("raise/remove the 8% cap").

Reuses the validated candidate CSVs already in this repo
(backtesting/reports/backtest_trades_PEAD_2022_2025_ENHANCED_base.csv and
backtesting/reports/backtest_trades_PEAD_2026_YTD.csv) so the entry set is
identical to every other report in this repo. Only the exit/sizing logic is
new. OHLC paths are re-fetched from Yahoo's chart API (same approach as the
V0/V1 script) since backtesting/data_cache/ is not committed.

Periods: 2022-2024 (in-sample), 2025 (OOS), 2026 YTD (OOS, through today).
"""

import os
import sys
import pickle
import time
import warnings
from datetime import datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import backtest_pead_2026_ytd as eng  # noqa: E402  (for MIN_PRICE only)

HERE        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backtesting/
CACHE_DIR   = os.path.join(HERE, "data_cache")
REPORTS_DIR = os.path.join(HERE, "reports")
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

TEST_START = "2022-01-01"
TEST_END   = "2026-07-04"

EQUITY         = 100_000.0
POS_CAP_PCT    = 0.11
POS_CAP_DOLLAR = EQUITY * POS_CAP_PCT      # $11,000
RISK_PCT       = 0.008                     # per S3 proposed wording: 0.8% of equity
RISK_DOLLAR    = EQUITY * RISK_PCT         # $800

TRAIL_PCT     = 0.07
TRAIL_TRIGGER = 0.10
SCALE_FRAC    = 1.0 / 3.0
TIME_STOP     = 42

ATR_PERIOD    = 14
ATR_MULT      = 2.0
FLAT_STOP_PCT = 8.0

NOISE_WINDOW     = 5
MU_ATR_THRESHOLD = 3.0

HIST_FETCH_START = "2021-10-01"
HIST_FETCH_END   = "2026-07-04"

CAND_2022_2025 = os.path.join(REPORTS_DIR, "backtest_trades_PEAD_2022_2025_ENHANCED_base.csv")
CAND_2026      = os.path.join(REPORTS_DIR, "backtest_trades_PEAD_2026_YTD.csv")

SPY_BENCHMARK = {"2022-2024": 28.2, "2025": 18.0, "2026 YTD": 11.1}  # from prior reports in this repo

import requests as _rq

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_P1 = int(pd.Timestamp(HIST_FETCH_START).timestamp())
_P2 = int(pd.Timestamp(HIST_FETCH_END).timestamp())


def _fetch_chart(ticker):
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


def effective_wider_stop_pct(atr_pct):
    """S3 proposal: max(8%, 2xATR) -- a FLOOR at the flat stop, uncapped above it."""
    return max(FLAT_STOP_PCT, ATR_MULT * atr_pct)


def simulate(hist, entry_date, hard_stop_pct, trail_pct=TRAIL_PCT):
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data = hist[hist.index == entry_date]
    if day_data.empty:
        return None
    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < eng.MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1.0 - hard_stop_pct / 100.0)
    future = hist[hist.index >= entry_date]

    booked = 0.0
    open_frac = 1.0
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

        if not scaled and close <= hard_stop_price:
            ret = (close - entry_price) / entry_price
            return _result(dt, ret, "hard_stop", cal_days,
                           stop_fired=True, stop_first5=(i < NOISE_WINDOW))

        if not scaled and close >= entry_price * (1.0 + TRAIL_TRIGGER):
            booked += SCALE_FRAC * TRAIL_TRIGGER
            open_frac = 1.0 - SCALE_FRAC
            scaled = True
            trail_active = True

        if trail_active:
            trail_stop = highest * (1.0 - trail_pct)
            if close <= trail_stop:
                ret_open = (close - entry_price) / entry_price
                total = booked + open_frac * ret_open
                return _result(dt, total, "trail_stop", cal_days,
                               stop_fired=False, stop_first5=False)

        if cal_days >= TIME_STOP:
            ret_open = (close - entry_price) / entry_price
            total = booked + open_frac * ret_open
            return _result(dt, total, "time", cal_days,
                           stop_fired=False, stop_first5=False)

    last = future.iloc[-1]
    ret_open = (last["Close"] - entry_price) / entry_price
    total = booked + open_frac * ret_open
    return _result(last.name, total, "data_end", (last.name - entry_date).days,
                   stop_fired=False, stop_first5=False)


def _result(dt, ret, reason, days, stop_fired, stop_first5):
    return {"exit_date": dt.date(), "return_pct": ret * 100.0, "exit_reason": reason,
            "holding_days": days, "stop_fired": stop_fired, "stop_first5": stop_first5}


def build_trades():
    cand = load_candidates()
    tickers = sorted(cand["ticker"].unique())
    print(f"Candidate entries: {len(cand)} over {len(tickers)} tickers")

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
        eff_stop = effective_wider_stop_pct(atrp)

        v0 = simulate(hist, entry_date, FLAT_STOP_PCT)
        v2 = simulate(hist, entry_date, eff_stop)
        if v0 is None or v2 is None:
            no_entry += 1
            continue

        pos_v0 = POS_CAP_DOLLAR
        pos_v2_uncapped = RISK_DOLLAR / (eff_stop / 100.0)
        pos_v2 = min(POS_CAP_DOLLAR, pos_v2_uncapped)
        v2_capped = pos_v2_uncapped > POS_CAP_DOLLAR

        rows.append({
            "ticker": t, "sector": c["sector"], "is_it": bool(c["is_it"]),
            "year": int(c["year"]),
            "earn_date": c["earn_date"], "entry_date": entry_date.date(),
            "entry_price": round(float(open_price), 4),
            "surprise_pct": round(float(c["surprise_pct"]), 2) if pd.notna(c["surprise_pct"]) else None,
            "atr_pct": round(atrp, 3),
            "eff_stop_pct": round(eff_stop, 3),
            "pos_v2_dollar": round(pos_v2, 2),
            "v2_capped": v2_capped,
            "v0_return_pct": round(v0["return_pct"], 3),
            "v0_exit_reason": v0["exit_reason"],
            "v0_holding_days": v0["holding_days"],
            "v0_stop_fired": v0["stop_fired"],
            "v0_stop_first5": v0["stop_first5"],
            "v0_return_dollar": round(v0["return_pct"] / 100.0 * pos_v0, 2),
            "v2_return_pct": round(v2["return_pct"], 3),
            "v2_exit_reason": v2["exit_reason"],
            "v2_holding_days": v2["holding_days"],
            "v2_stop_fired": v2["stop_fired"],
            "v2_stop_first5": v2["stop_first5"],
            "v2_return_dollar": round(v2["return_pct"] / 100.0 * pos_v2, 2),
        })

    print(f"\nSimulated trades: {len(rows)}, no-history: {no_hist}, no-entry/skip: {no_entry}")
    return pd.DataFrame(rows)


def variant_stats(df, prefix):
    rp = df[f"{prefix}_return_pct"]
    rd = df[f"{prefix}_return_dollar"]
    if df.empty:
        return None
    winners = df[rp > 0]
    losers = df[rp <= 0]
    gw = winners[f"{prefix}_return_dollar"].sum()
    gl = abs(losers[f"{prefix}_return_dollar"].sum())
    pf = gw / gl if gl > 0 else float("inf")

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
    }


def pf_str(v):
    return "inf" if v == float("inf") else f"{v}"


PERIODS = [
    ("2022-2024", lambda d: d[d.year.isin([2022, 2023, 2024])]),
    ("2025",      lambda d: d[d.year == 2025]),
    ("2026 YTD",  lambda d: d[d.year == 2026]),
]


def build_report(df):
    L = []
    A = L.append
    A("# Backtest: Wider ATR-Scaled Stop (V2, S3 proposal) vs Flat -8% Stop (V0)")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} -- "
      f"window {TEST_START}->{TEST_END}, S&P 500 current constituents (survivorship-biased).*\n")
    A("This tests the actual S3 recommendation from `backtesting/strategy_review_log.md` "
      "(2026-06-30 run): widen the stop for high-ATR names instead of using a tighter-only "
      "ATR floor. Unlike the already-rejected V1 variant in "
      "`backtest_report_ATR_STOP_VS_FLAT.md` (`min(8%, max(4%, 2xATR))`, a CEILING at 8% that "
      "can only ever be equal-or-tighter than flat), this variant (V2) removes the ceiling.\n")
    A("- **V0 (baseline):** flat -8% stop; position = 11% of equity ($11k on $100k).")
    A("- **V2 (wider ATR stop):** stop = `max(8%, 2x14-day ATR%)` -- a FLOOR at 8%, uncapped "
      "above it; position sized to risk 0.8% of equity (`$800 / stop_pct`), hard-capped at 11% "
      "of equity. Per the proposed wording, dollar risk per trade is held roughly constant by "
      "shrinking notional as the stop widens.\n")
    A("Both variants scale out 1/3 at +10% and trail the remaining 2/3 by 7% below the peak; "
      "42-calendar-day time stop. Entry set, filters and trailing/time-stop logic are identical "
      "to every other PEAD backtest in this repo.\n")

    per = {}
    for pname, sel in PERIODS:
        sub = sel(df)
        per[pname] = (variant_stats(sub, "v0"), variant_stats(sub, "v2"), sub)

    A("## 1. Verdict\n")
    v0_avg_all = round(df["v0_return_pct"].mean(), 2)
    v2_avg_all = round(df["v2_return_pct"].mean(), 2)
    v0_pf_all = variant_stats(df, "v0")["profit_factor"]
    v2_pf_all = variant_stats(df, "v2")["profit_factor"]
    A(f"Across the full sample ({len(df)} trades), **V0 avg/trade = {v0_avg_all}%** "
      f"(PF {pf_str(v0_pf_all)}) vs **V2 avg/trade = {v2_avg_all}%** (PF {pf_str(v2_pf_all)}).\n")

    A("## 2. Comparison Table -- V0 vs V2 by period (in-sample vs out-of-sample)\n")
    A("| Period | Var | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | MaxConsecL | AvgHold | Total P&L |")
    A("|--------|-----|-------:|-----:|-----:|-----:|--------:|---------:|---:|-----------:|--------:|----------:|")
    for pname, _ in PERIODS:
        s0, s2, _ = per[pname]
        for tag, s in [("V0", s0), ("V2", s2)]:
            if s is None:
                A(f"| {pname} | {tag} | 0 | - | - | - | - | - | - | - | - | - |")
                continue
            A(f"| {pname} | {tag} | {s['trades']} | {s['win_rate']}% | {s['avg_return']}% | "
              f"{s['median_return']}% | {s['avg_winner']}% | {s['avg_loser']}% | {pf_str(s['profit_factor'])} | "
              f"{s['max_consec_loss']} | {s['avg_holding_days']}d | ${s['total_pnl']:,.0f} |")
    A("")

    A("## 3. Out-of-sample discipline (2022-2024 in-sample vs 2025+2026 out-of-sample)\n")
    is_sub = df[df.year.isin([2022, 2023, 2024])]
    oos_sub = df[df.year.isin([2025, 2026])]
    is0, is2 = variant_stats(is_sub, "v0"), variant_stats(is_sub, "v2")
    oos0, oos2 = variant_stats(oos_sub, "v0"), variant_stats(oos_sub, "v2")
    A("| Segment | Var | Trades | Avg% | PF |")
    A("|---------|-----|-------:|-----:|---:|")
    A(f"| In-sample (2022-2024) | V0 | {is0['trades']} | {is0['avg_return']}% | {pf_str(is0['profit_factor'])} |")
    A(f"| In-sample (2022-2024) | V2 | {is2['trades']} | {is2['avg_return']}% | {pf_str(is2['profit_factor'])} |")
    A(f"| Out-of-sample (2025-2026) | V0 | {oos0['trades']} | {oos0['avg_return']}% | {pf_str(oos0['profit_factor'])} |")
    A(f"| Out-of-sample (2025-2026) | V2 | {oos2['trades']} | {oos2['avg_return']}% | {pf_str(oos2['profit_factor'])} |")
    A("")
    oos_verdict = "IMPROVES OR HOLDS" if (oos2['avg_return'] >= oos0['avg_return'] and pf_str(oos2['profit_factor']) != '0') else "DOES NOT IMPROVE"
    A(f"**OOS verdict: V2 {oos_verdict} vs V0 out-of-sample** "
      f"({oos2['avg_return']}% vs {oos0['avg_return']}% avg; PF {pf_str(oos2['profit_factor'])} vs {pf_str(oos0['profit_factor'])}).\n")

    A("## 4. Noise-stop analysis (stops inside first 5 trading days)\n")
    A("| Period | Var | #Stops | #Stops in first 5d | Noise-stop rate | First-5d stops as % of all trades |")
    A("|--------|-----|-------:|-------------------:|----------------:|----------------------------------:|")
    for pname, _ in PERIODS:
        s0, s2, _ = per[pname]
        for tag, s in [("V0", s0), ("V2", s2)]:
            if s is None:
                continue
            nr = f"{s['noise_stop_rate']}%" if s['noise_stop_rate'] is not None else "-"
            fa = f"{s['first5_of_all']}%" if s['first5_of_all'] is not None else "-"
            A(f"| {pname} | {tag} | {s['n_stops']} | {s['n_stops_first5']} | {nr} | {fa} |")
    A("")

    A("## 5. MU-style analysis -- high-ATR semiconductor / IT names\n")
    hi = df[(df.is_it) & (df.atr_pct > MU_ATR_THRESHOLD)]
    A(f"Filter: IT-sector names with daily ATR > {MU_ATR_THRESHOLD}% of price. Matched **{len(hi)}** trades.\n")
    if not hi.empty:
        v0_first5 = hi[hi.v0_stop_first5]
        v2_first5 = hi[hi.v2_stop_first5]
        avoided = hi[hi.v0_stop_first5 & ~hi.v2_stop_first5]
        added = hi[~hi.v0_stop_first5 & hi.v2_stop_first5]
        A(f"- Mean ATR of these names: {round(hi.atr_pct.mean(), 2)}%/day -> mean V2 stop "
          f"{round(hi.eff_stop_pct.mean(), 2)}% (vs flat 8%).")
        A(f"- V0 first-5-day noise stops: **{len(v0_first5)}**. V2 first-5-day noise stops: **{len(v2_first5)}**.")
        A(f"- V0 noise stops *avoided* under V2: **{len(avoided)}**. "
          f"*New* noise stops V2 introduced: **{len(added)}**.")
        A(f"- V0 avg return on these names: {round(hi.v0_return_pct.mean(), 2)}%; "
          f"V2 avg: {round(hi.v2_return_pct.mean(), 2)}%.")
        shrunk_share = round((~hi.v2_capped).mean() * 100, 1)
        A(f"- Position downsizing: **{shrunk_share}%** of these high-ATR trades had V2 notional "
          f"BELOW the $11k cap (mean ${round(hi.pos_v2_dollar.mean()):,}) -- the 11% cap never "
          f"bound; sizing genuinely shrank to hold dollar risk near $800.\n")
    else:
        A("_No IT names with daily ATR > 3% in the candidate set._\n")

    A("## 6. Beat-the-benchmark bar (SPY buy-and-hold, same period)\n")
    A("| Period | SPY buy-and-hold | V0 avg/trade | V2 avg/trade |")
    A("|--------|------------------:|--------------:|--------------:|")
    for pname, _ in PERIODS:
        s0, s2, _ = per[pname]
        spy = SPY_BENCHMARK.get(pname, None)
        spy_s = f"{spy}%" if spy is not None else "-"
        A(f"| {pname} | {spy_s} | {s0['avg_return'] if s0 else '-'}% | {s2['avg_return'] if s2 else '-'}% |")
    A("\n_SPY figures are per-period index buy-and-hold return, taken from the other PEAD backtest "
      "reports in this repo (`backtest_report_PEAD_2022_2024.md`, `backtest_report_PEAD_2025_OOS.md`, "
      "`backtest_report_PEAD_2026_YTD.md`); they are not directly comparable to a single-trade avg% "
      "(these are per-trade returns on ~11% position size, not a fully-invested compounded return), "
      "but are shown for context per the routine's beat-the-benchmark bar.\n")

    A("## 7. Recommendation\n")
    better_periods = sum(1 for pname, _ in PERIODS
                         if per[pname][1] and per[pname][0]
                         and per[pname][1]["avg_return"] > per[pname][0]["avg_return"])
    A(f"V2 beat V0 on average return in **{better_periods} of 3** periods "
      f"(OOS 2025+2026: {oos_verdict}).\n")
    return "\n".join(L)


def main():
    df = build_trades()
    if df.empty:
        print("No candidates generated.")
        sys.exit(1)

    v0_cols = ["ticker", "sector", "is_it", "year", "earn_date", "entry_date", "entry_price",
               "surprise_pct", "atr_pct",
               "v0_return_pct", "v0_exit_reason", "v0_holding_days", "v0_stop_fired",
               "v0_stop_first5", "v0_return_dollar"]
    v2_cols = ["ticker", "sector", "is_it", "year", "earn_date", "entry_date", "entry_price",
               "surprise_pct", "atr_pct", "eff_stop_pct", "pos_v2_dollar", "v2_capped",
               "v2_return_pct", "v2_exit_reason", "v2_holding_days", "v2_stop_fired",
               "v2_stop_first5", "v2_return_dollar"]
    df[v0_cols].to_csv(os.path.join(REPORTS_DIR, "backtest_trades_ATR_STOP_V2_widened_v0.csv"), index=False)
    df[v2_cols].to_csv(os.path.join(REPORTS_DIR, "backtest_trades_ATR_STOP_V2_widened.csv"), index=False)

    report = build_report(df)
    rpath = os.path.join(REPORTS_DIR, "backtest_report_ATR_STOP_WIDENED_V2.md")
    with open(rpath, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n=== HEADLINE ===")
    for pname, sel in PERIODS:
        sub = sel(df)
        s0 = variant_stats(sub, "v0")
        s2 = variant_stats(sub, "v2")
        if s0 is None:
            print(f"{pname}: no trades")
            continue
        print(f"{pname}: n={s0['trades']} | "
              f"V0 win {s0['win_rate']}% avg {s0['avg_return']}% PF {pf_str(s0['profit_factor'])} | "
              f"V2 win {s2['win_rate']}% avg {s2['avg_return']}% PF {pf_str(s2['profit_factor'])}")
    print(f"\nReport: {rpath}")


if __name__ == "__main__":
    main()
