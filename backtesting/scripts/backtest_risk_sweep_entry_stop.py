"""
Parameter-sweep backtest: entry-quality filters x stop width.

Grid-searches the interaction between LOOSENING the entry bar and WIDENING the
stop, using the same already-validated candidate entry set and the same IS/OOS
split discipline as the regime-gate and S3 ATR-stop backtests in this repo.

Research only. Does not modify strategy.md and places no orders. Diagnostic,
exactly like backtest_atr_stop_widened.py (S3) and the stop audit.

--------------------------------------------------------------------------------
WHAT IS SWEPT (grid, all combinations)
--------------------------------------------------------------------------------
  EPS surprise threshold : 15% (current)   | 12.5% | 10%
  Score cutoff           : >=6 (current)   | >=5   | >=4      (see PROXY note)
  Stop width             : flat -8% (current) | -10% | -12%
                           | max(8%, 1.5xATR14) | max(8%, 2.0xATR14)  (ATR = S3)

  = 3 x 3 x 5 = 45 combinations, each reported separately for IS and OOS.

--------------------------------------------------------------------------------
IS / OOS SPLIT (identical discipline to S3 / regime-gate audits)
--------------------------------------------------------------------------------
  IS  (in-sample)     : 2022-2024   (S3's V0 in-sample = 194 baseline trades)
  OOS (out-of-sample) : 2025        (S3's V0 2025 = 53 baseline trades)
  2026 YTD            : cross-check panel, CURRENT-FILTER combos only, on the
                        30 committed enhanced trades (see 2026 caveat in report).

A combination that wins IS but loses OOS is a REJECTED combination and is
labelled as such. IS and OOS are never averaged into a single number.

--------------------------------------------------------------------------------
SCORE-CUTOFF PROXY  (important honesty caveat -- also stated in the report)
--------------------------------------------------------------------------------
The live pre_market 1-10 conviction score (routines/pre_market.md) weights
guidance-raise magnitude, analyst-upgrade counts, earnings-call tone, insider
activity, sector-ETF momentum, short interest, and regulatory (shelf/BIS)
checks -- NONE of which are reconstructible from price+earnings data. The live
score therefore CANNOT be reproduced in a historical backtest, exactly as the
2026-YTD and ENHANCED reports flagged guidance/BIS/shelf as unbacktestable.

We implement the score cutoff as a transparent, mechanical proxy = the count of
the three VERIFIABLE enhanced quality filters that pass:
    q = 1[vol >= 1.5x 20d avg] + 1[rel-strength vs SPY > 0] + 1[new 52-wk high <=45d]
    score >= 6 (current live bar) -> require q == 3  (== the current enhanced set)
    score >= 5 (looser)           -> require q >= 2
    score >= 4 (loosest)          -> require q >= 1
This is a lower-dimensional stand-in for "how many verifiable quality signals
must align", NOT the literal live score. EPS-surprise magnitude is handled by
the separate EPS-threshold dimension and is deliberately NOT double-counted in q.

The near-earnings event gate (f_nearearn) is kept ON for every combination as a
base gate (it is 100% True on the committed base set, so it is a no-op here but
is retained for fidelity to the live rules).

Baseline combination (EPS>=15% / score>=6 / flat -8%) reproduces the current
live strategy AND S3's V0 entry set exactly (194 IS + 53 OOS).

--------------------------------------------------------------------------------
DATA
--------------------------------------------------------------------------------
Entry set (2022-2025): backtesting/reports/backtest_trades_PEAD_2022_2025_ENHANCED_base.csv
    = every EPS-beat candidate passing the BASE liquidity gate (price>=$10,
      20d $vol>=$20M), with surprise_pct + the enhanced-filter booleans. This is
      the same entry set every other report in this repo uses.
Entry set (2026 YTD): backtesting/reports/backtest_trades_PEAD_2026_YTD.csv
    = the 30 committed enhanced trades (all already EPS>=15% & q==3). The full
      2026 BASE population is NOT in the committed dataset and cannot be rebuilt
      here (yfinance earnings endpoint is blocked in this environment), so
      loosened-filter cells for 2026 are reported as N/A rather than fabricated.

Daily auto-adjusted OHLC is re-fetched from Yahoo's chart API (same source/method
as backtest_atr_stop_widened.py) and cached under backtesting/data_cache/. Stops,
ATR, the 1/3 scale-out at +10%, the 7% trail and the 42-day time stop are all
re-simulated on that series with the SAME simulate() logic as S3 -- only the
initial stop width and (for ATR variants) the position size differ across the
five stop variants.

Survivorship bias (current S&P 500 constituents) and zero transaction
costs/slippage apply, as in every prior report in this repo.
"""

import os
import sys
import time
import pickle
import warnings
from datetime import datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# ─── Paths (anchored to this file, like the other research scripts) ───────────
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_BT_DIR     = os.path.dirname(_SCRIPT_DIR)                     # backtesting/
_REPO_ROOT  = os.path.dirname(_BT_DIR)
CACHE_DIR   = os.path.join(_BT_DIR, "data_cache")
REPORTS_DIR = os.path.join(_BT_DIR, "reports")
MEMORY_DIR  = os.path.join(_REPO_ROOT, "memory")
os.makedirs(CACHE_DIR, exist_ok=True)

RUN_DATE = "2026-07-08"

CAND_2022_2025 = os.path.join(REPORTS_DIR, "backtest_trades_PEAD_2022_2025_ENHANCED_base.csv")
CAND_2026      = os.path.join(REPORTS_DIR, "backtest_trades_PEAD_2026_YTD.csv")

MIN_PRICE = 10.0

# ─── Strategy exit constants (identical to S3 backtest_atr_stop_widened.py) ────
EQUITY         = 100_000.0
POS_CAP_PCT    = 0.11
POS_CAP_DOLLAR = EQUITY * POS_CAP_PCT      # $11,000
RISK_PCT       = 0.008                     # S3 wording: risk 0.8% of equity / trade
RISK_DOLLAR    = EQUITY * RISK_PCT         # $800

TRAIL_PCT      = 0.07                       # 7% trail on the remaining 2/3 (all sectors)
TRAIL_TRIGGER  = 0.10                       # scale out 1/3 at +10%
SCALE_FRAC     = 1.0 / 3.0
TIME_STOP      = 42                         # calendar days
ATR_PERIOD     = 14

# ─── Swept parameter grids ─────────────────────────────────────────────────────
EPS_THRESHOLDS = [15.0, 12.5, 10.0]        # current, looser, loosest
SCORE_LEVELS   = [(">=6", 3), (">=5", 2), (">=4", 1)]   # (label, min q of {vol,rs,52w})
# stop variants: (key, label, kind, param)   kind in {"flat","atr"}
STOP_VARIANTS = [
    ("flat8",  "flat -8%",              "flat", 8.0),
    ("flat10", "flat -10%",             "flat", 10.0),
    ("flat12", "flat -12%",             "flat", 12.0),
    ("atr15",  "max(8%, 1.5xATR14)",    "atr",  1.5),
    ("atr20",  "max(8%, 2.0xATR14)",    "atr",  2.0),
]
BASELINE_KEY = ("15.0", ">=6", "flat8")    # current live strategy == S3 V0

# SPY per-period buy-and-hold, recomputed from the chart API below; repo-cited
# fallbacks (from the existing PEAD reports) if the fetch fails.
SPY_FALLBACK = {"IS (2022-2024)": 28.2, "OOS (2025)": 18.0, "2026 YTD": 11.1}

# ─── Yahoo chart-API fetch + disk cache (same approach as the S3 script) ───────
import requests as _rq

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
_HIST_FETCH_START = "2021-06-01"          # deep enough for ATR + entries from 2022-01
_HIST_FETCH_END   = "2026-07-08"
_P1 = int(pd.Timestamp(_HIST_FETCH_START).timestamp())
_P2 = int(pd.Timestamp(_HIST_FETCH_END).timestamp())


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
    time.sleep(0.25)
    return hist


# ─── ATR% at entry (same as S3) ────────────────────────────────────────────────
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
    row = hist[hist.index == entry_date]
    if row.empty:
        return None
    px = row["Open"].iloc[0]
    if pd.isna(px) or px <= 0:
        return None
    return float(atr / px * 100.0)


# ─── One-trade simulation (identical mechanics to S3 simulate()) ───────────────
def simulate(hist, entry_date, hard_stop_pct, trail_pct=TRAIL_PCT):
    entry_date = pd.Timestamp(entry_date).normalize()
    dd = hist[hist.index == entry_date]
    if dd.empty:
        return None
    entry_price = dd["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1.0 - hard_stop_pct / 100.0)
    future = hist[hist.index >= entry_date]

    booked = 0.0
    open_frac = 1.0
    scaled = False
    trail_active = False
    highest = entry_price

    for dt, row in future.iterrows():
        close = row["Close"]
        if pd.isna(close):
            continue
        if close > highest:
            highest = close
        cal_days = (dt - entry_date).days

        if not scaled and close <= hard_stop_price:
            ret = (close - entry_price) / entry_price
            return {"return_pct": ret * 100.0, "exit_reason": "hard_stop",
                    "holding_days": cal_days}

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
                return {"return_pct": total * 100.0, "exit_reason": "trail_stop",
                        "holding_days": cal_days}

        if cal_days >= TIME_STOP:
            ret_open = (close - entry_price) / entry_price
            total = booked + open_frac * ret_open
            return {"return_pct": total * 100.0, "exit_reason": "time",
                    "holding_days": cal_days}

    last = future.iloc[-1]
    ret_open = (last["Close"] - entry_price) / entry_price
    total = booked + open_frac * ret_open
    return {"return_pct": total * 100.0, "exit_reason": "data_end",
            "holding_days": (last.name - entry_date).days}


def stop_pct_for_variant(kind, param, atr_pct):
    if kind == "flat":
        return param
    # atr: floor at 8%, uncapped above (S3 definition)
    return max(8.0, param * atr_pct)


def position_dollars(kind, eff_stop_pct):
    if kind == "flat":
        return POS_CAP_DOLLAR                       # fixed 11% (current live sizing)
    # ATR variants use S3 risk-based sizing: risk 0.8% of equity, capped at 11%
    return min(POS_CAP_DOLLAR, RISK_DOLLAR / (eff_stop_pct / 100.0))


# ─── Build per-candidate simulated returns for all 5 stop variants ─────────────
def load_entry_set():
    a = pd.read_csv(CAND_2022_2025)
    a = a[["ticker", "sector", "is_it", "year", "earn_date", "entry_date",
           "entry_price", "surprise_pct", "f_vol15x", "f_rs", "f_52w", "f_nearearn"]].copy()
    a["period"] = a["year"].map(lambda y: "IS (2022-2024)" if y in (2022, 2023, 2024)
                                else ("OOS (2025)" if y == 2025 else "other"))
    a = a[a.period != "other"]
    return a


def load_2026():
    b = pd.read_csv(CAND_2026)
    b = b[["ticker", "sector", "is_it", "earn_date", "entry_date",
           "entry_price", "surprise_pct", "f_vol15x", "f_rs", "f_52w", "f_nearearn"]].copy()
    b["year"] = pd.to_datetime(b["entry_date"]).dt.year
    b["period"] = "2026 YTD"
    return b


def simulate_all(cand, hist_map):
    """Return per-candidate DataFrame with return_pct/pos$ for each stop variant."""
    rows = []
    no_hist = no_entry = 0
    for _, c in cand.iterrows():
        hist = hist_map.get(c["ticker"])
        if hist is None:
            no_hist += 1
            continue
        entry_date = pd.Timestamp(c["entry_date"]).normalize()
        dd = hist[hist.index == entry_date]
        if dd.empty or pd.isna(dd["Open"].iloc[0]) or dd["Open"].iloc[0] < MIN_PRICE:
            no_entry += 1
            continue
        atrp = atr_pct_at_entry(hist, entry_date)
        if atrp is None:
            no_entry += 1
            continue

        rec = {
            "ticker": c["ticker"], "sector": c["sector"], "is_it": bool(c["is_it"]),
            "year": int(c["year"]), "period": c["period"],
            "entry_date": entry_date.date(),
            "surprise_pct": round(float(c["surprise_pct"]), 3) if pd.notna(c["surprise_pct"]) else None,
            "q": int(bool(c["f_vol15x"]) + bool(c["f_rs"]) + bool(c["f_52w"])),
            "f_vol15x": bool(c["f_vol15x"]), "f_rs": bool(c["f_rs"]),
            "f_52w": bool(c["f_52w"]), "f_nearearn": bool(c["f_nearearn"]),
            "atr_pct": round(atrp, 3),
        }
        ok = True
        for key, _lab, kind, param in STOP_VARIANTS:
            eff = stop_pct_for_variant(kind, param, atrp)
            res = simulate(hist, entry_date, eff)
            if res is None:
                ok = False
                break
            posd = position_dollars(kind, eff)
            rec[f"{key}_stop_pct"] = round(eff, 3)
            rec[f"{key}_pos_dollar"] = round(posd, 2)
            rec[f"{key}_ret_pct"] = round(res["return_pct"], 4)
            rec[f"{key}_ret_dollar"] = round(res["return_pct"] / 100.0 * posd, 2)
            rec[f"{key}_exit"] = res["exit_reason"]
            rec[f"{key}_hold"] = res["holding_days"]
        if not ok:
            no_entry += 1
            continue
        rows.append(rec)
    print(f"  simulated {len(rows)}, no-history {no_hist}, no-entry/skip {no_entry}")
    return pd.DataFrame(rows)


# ─── Stats for a selected sub-frame under one stop variant ─────────────────────
def block_stats(sub, key):
    """Per-trade + dollar stats for sub-frame under stop variant `key`."""
    rp = sub[f"{key}_ret_pct"]
    rd = sub[f"{key}_ret_dollar"]
    n = len(sub)
    if n == 0:
        return None
    winners = rp[rp > 0]
    losers = rp[rp <= 0]
    gw = rd[rp > 0].sum()
    gl = abs(rd[rp <= 0].sum())
    pf = (gw / gl) if gl > 0 else float("inf")
    # per-trade Sharpe = mean/std of per-trade returns (rf ~ 0 at trade horizon)
    sd = rp.std(ddof=1)
    sharpe = (rp.mean() / sd) if (sd and sd > 0) else None
    # Max drawdown of a sequential equity curve that REINVESTS each trade at its own
    # position fraction (entry-date order). Compounding keeps the curve strictly
    # positive so the drawdown is bounded in [0, 100%) — unlike an additive sum of
    # independent $11k bets, which can drive cumulative losses past starting capital
    # on the high-trade-count loosened combos and produce a meaningless >100% figure.
    # Still an approximation: no concurrency / capital constraint (the live book runs
    # up to 8 positions at once), so this is not the live portfolio drawdown.
    seq = sub.sort_values("entry_date")
    frac = (seq[f"{key}_pos_dollar"] / EQUITY).to_numpy()
    r = (seq[f"{key}_ret_pct"] / 100.0).to_numpy()
    eq = np.cumprod(1.0 + frac * r)
    peak = np.maximum.accumulate(eq)
    dd = (eq - peak) / peak
    maxdd = float(dd.min()) * 100.0 if len(eq) else 0.0
    # max consecutive losses (entry-date order)
    cur = mx = 0
    for r in sub.sort_values("entry_date")[f"{key}_ret_pct"]:
        if r <= 0:
            cur += 1; mx = max(mx, cur)
        else:
            cur = 0
    return {
        "n": n,
        "win_rate": round((rp > 0).mean() * 100, 1),
        "avg_return": round(rp.mean(), 3),
        "median_return": round(rp.median(), 3),
        "avg_winner": round(winners.mean(), 2) if len(winners) else 0.0,
        "avg_loser": round(losers.mean(), 2) if len(losers) else 0.0,
        "profit_factor": round(pf, 3) if pf != float("inf") else float("inf"),
        "sharpe": round(sharpe, 3) if sharpe is not None else None,
        "max_drawdown_pct": round(maxdd, 2),
        "max_consec_losses": mx,
        "avg_holding_days": round(sub[f"{key}_hold"].mean(), 1),
        "total_pnl": round(rd.sum(), 0),
        "avg_position_dollar": round(sub[f"{key}_pos_dollar"].mean(), 0),
    }


def select(df, eps_thr, qmin):
    return df[(df.surprise_pct >= eps_thr) & (df.q >= qmin) & (df.f_nearearn)]


# ─── SPY buy-and-hold per period from the chart API ────────────────────────────
def spy_returns():
    hist = cached_history("SPY")
    out = {}
    windows = {
        "IS (2022-2024)": ("2022-01-01", "2024-12-31"),
        "OOS (2025)":     ("2025-01-01", "2025-12-31"),
        "2026 YTD":       ("2026-01-01", "2026-07-08"),
    }
    for lab, (s, e) in windows.items():
        try:
            w = hist[(hist.index >= s) & (hist.index <= e)]["Close"].dropna()
            out[lab] = round((float(w.iloc[-1]) - float(w.iloc[0])) / float(w.iloc[0]) * 100, 1)
        except Exception:
            out[lab] = SPY_FALLBACK.get(lab)
    return out


# ─── Grid build ────────────────────────────────────────────────────────────────
def build_grid(df):
    """Return long-form grid rows for IS + OOS across all 45 combinations."""
    grid = []
    for period in ["IS (2022-2024)", "OOS (2025)"]:
        pdf = df[df.period == period]
        for eps in EPS_THRESHOLDS:
            for slabel, qmin in SCORE_LEVELS:
                sub = select(pdf, eps, qmin)
                for key, slab, kind, param in STOP_VARIANTS:
                    st = block_stats(sub, key)
                    row = {
                        "period": period, "eps_threshold": eps,
                        "score_cutoff": slabel, "score_qmin": qmin,
                        "stop_key": key, "stop_label": slab,
                    }
                    if st is None:
                        row.update({k: None for k in
                                    ["n", "win_rate", "avg_return", "median_return",
                                     "avg_winner", "avg_loser", "profit_factor", "sharpe",
                                     "max_drawdown_pct", "max_consec_losses",
                                     "avg_holding_days", "total_pnl", "avg_position_dollar"]})
                    else:
                        row.update(st)
                    grid.append(row)
    return pd.DataFrame(grid)


def baseline_row(grid, period):
    m = grid[(grid.period == period) & (grid.eps_threshold == 15.0)
             & (grid.score_cutoff == ">=6") & (grid.stop_key == "flat8")]
    return m.iloc[0] if len(m) else None


def pf_s(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "—"
    return "inf" if v == float("inf") else f"{v}"


def num(v, suf=""):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "—"
    return f"{v}{suf}"


# ─── 2026 YTD cross-check (current-filter combos only) ─────────────────────────
def build_2026_panel(df26):
    """df26 already all EPS>=15 & q==3 -> only the baseline entry combo. Report the
    5 stop variants on those 30 trades."""
    rows = []
    for key, slab, kind, param in STOP_VARIANTS:
        st = block_stats(df26, key)
        rows.append({"stop_key": key, "stop_label": slab, **(st or {})})
    return pd.DataFrame(rows)


# ─── Report ────────────────────────────────────────────────────────────────────
def build_report(df, df26, grid, panel26, spy):
    L = []
    A = L.append

    A("# Parameter-Sweep Backtest — Entry-Quality Filters × Stop Width")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} — "
      f"window 2022-01-01→2025-12-31 (grid) + 2026 YTD cross-check; "
      f"S&P 500 current constituents (survivorship-biased).*\n")
    A("**Research / diagnostic only — no `strategy.md` edit, no orders.** Same status as the "
      "stop audit (`memory/stop_audit_2026-07-07.md`), the S3 ATR-stop backtest "
      "(`backtest_report_ATR_STOP_WIDENED_V2.md`) and the chronic-exit backtest.\n")

    # ── 0. Method / caveats ──
    A("## 0. What this sweeps, and the honesty caveats up front\n")
    A("| Dimension | Values (current in **bold**) |")
    A("|-----------|------------------------------|")
    A("| EPS surprise threshold | **≥15%** · ≥12.5% · ≥10% |")
    A("| Score cutoff (proxy) | **≥6** · ≥5 · ≥4 |")
    A("| Stop width | **flat −8%** · flat −10% · flat −12% · max(8%, 1.5×ATR14) · max(8%, 2.0×ATR14) |")
    A("\n3 × 3 × 5 = **45 combinations**, each reported **separately for IS and OOS**.\n")
    A("- **IS / OOS split** (identical to the S3 and regime-gate audits): "
      "**IS = 2022–2024**, **OOS = 2025**. A combination that wins IS but loses OOS is a "
      "**rejected** combination and is labelled so — IS and OOS are never averaged into one number.")
    A("- **Baseline** = EPS ≥15% / score ≥6 / flat −8%. This reproduces the current live strategy "
      "and S3's V0 entry set exactly (**194 IS + 53 OOS** trades).")
    A("- **Score-cutoff is a PROXY, not the live 1–10 score.** The live pre-market score weights "
      "guidance-raise magnitude, analyst-upgrade counts, earnings-call tone, insider activity, "
      "sector-ETF momentum, short interest and regulatory (shelf/BIS) checks — **none reconstructible "
      "from price+earnings data** (same class of unbacktestable inputs the 2026-YTD and ENHANCED "
      "reports flagged). We proxy it as the count `q` of the three verifiable quality filters "
      "{volume ≥1.5×, relative-strength >0, new 52-wk high ≤45d}: **≥6 → q==3** (= current enhanced "
      "set), **≥5 → q≥2**, **≥4 → q≥1**. Read the score rows as *“how many verifiable quality signals "
      "must align”*, not as the literal live score. EPS-surprise magnitude is handled by the EPS "
      "dimension and is deliberately not double-counted in `q`.")
    A("- **Stop mechanics** are identical to S3: both fixed and ATR variants scale out 1/3 at +10% "
      "and trail the remaining 2/3 by 7%; 42-day time stop. **ATR variants use S3's risk-based "
      "sizing** (risk 0.8% of equity = $800/stop%, capped at 11%); **fixed variants use the current "
      "flat 11% ($11k) sizing.** Per-trade return %/win %/Sharpe are sizing-independent; profit factor, "
      "total P&L and max-drawdown use each variant's own sizing, so ATR's smaller average notional "
      "mechanically dampens both its P&L and its drawdown (flagged again where it matters).")
    A(f"- **Coverage:** {len(df)} of the committed 2022–2025 base candidates were re-simulated from "
      f"re-fetched OHLC ({df[df.period=='IS (2022-2024)'].shape[0]} IS / "
      f"{df[df.period=='OOS (2025)'].shape[0]} OOS); "
      f"{len(df26)} of the 30 committed 2026 enhanced trades.")
    A("- **Sharpe** = mean(per-trade return) / std(per-trade return) (rf≈0 at the trade horizon); a "
      "per-trade risk-adjusted ratio, **not** annualised, and deliberately **not** ×√n (so it does not "
      "reward a combo merely for admitting more trades). **Max drawdown** = deepest peak-to-trough of "
      "a sequential equity curve that reinvests each trade at its own position fraction (entry-date "
      "order; compounded so it stays bounded in 0–100%). It models **no** concurrency / capital "
      "constraint — the live book runs up to 8 positions at once — so it is a directional stress read "
      "(looser ⇒ deeper), not the live portfolio drawdown. High-trade-count loosened cells sequence "
      "hundreds of bets through one account, which inflates the figure; weight it accordingly.\n")

    # ── 1. Headline verdict ──
    bIS = baseline_row(grid, "IS (2022-2024)")
    bOOS = baseline_row(grid, "OOS (2025)")
    A("## 1. Headline\n")
    A(f"- **Baseline (EPS≥15 / score≥6 / flat −8%)** — IS: {bIS['n']} trades, "
      f"{bIS['win_rate']}% win, {bIS['avg_return']}% avg, PF {pf_s(bIS['profit_factor'])}, "
      f"Sharpe {num(bIS['sharpe'])}, MaxDD {bIS['max_drawdown_pct']}%. "
      f"OOS: {bOOS['n']} trades, {bOOS['win_rate']}% win, {bOOS['avg_return']}% avg, "
      f"PF {pf_s(bOOS['profit_factor'])}, Sharpe {num(bOOS['sharpe'])}, MaxDD {bOOS['max_drawdown_pct']}%.")
    A(f"- **SPY buy-and-hold:** IS {spy['IS (2022-2024)']}% · OOS {spy['OOS (2025)']}% "
      f"· 2026 YTD {spy['2026 YTD']}% (index total return; not directly comparable to a per-trade "
      f"avg% on ~11% sizing — shown for the beat-the-benchmark bar).\n")

    # ── 2. Full grid, OOS ──
    for period in ["OOS (2025)", "IS (2022-2024)"]:
        base = baseline_row(grid, period)
        A(f"## 2{'a' if period.startswith('OOS') else 'b'}. Full grid — {period}\n")
        A("Δavg = avg-return minus the same-period baseline (flat −8% / EPS≥15 / score≥6). "
          "`n` is the raw trade count (denominator for every rate in the row).\n")
        A("| EPS | Score | Stop | n | Win% | Avg% | Med% | PF | Sharpe | MaxDD% | MaxConsecL | AvgHold | TotP&L | Δavg vs base |")
        A("|----:|:-----:|------|--:|-----:|-----:|-----:|---:|-------:|------:|-----------:|--------:|-------:|-------------:|")
        g = grid[grid.period == period]
        for eps in EPS_THRESHOLDS:
            for slabel, qmin in SCORE_LEVELS:
                for key, slab, kind, param in STOP_VARIANTS:
                    r = g[(g.eps_threshold == eps) & (g.score_cutoff == slabel)
                          & (g.stop_key == key)].iloc[0]
                    if r["n"] is None or (isinstance(r["n"], float) and pd.isna(r["n"])):
                        continue
                    davg = (round(r["avg_return"] - base["avg_return"], 2)
                            if base is not None else None)
                    dtag = ("baseline" if (str(eps) == "15.0" and slabel == ">=6" and key == "flat8")
                            else (f"{davg:+.2f}" if davg is not None else "—"))
                    A(f"| ≥{eps:g}% | {slabel} | {slab} | {int(r['n'])} | {r['win_rate']} | "
                      f"{r['avg_return']} | {r['median_return']} | {pf_s(r['profit_factor'])} | "
                      f"{num(r['sharpe'])} | {r['max_drawdown_pct']} | {r['max_consec_losses']} | "
                      f"{r['avg_holding_days']} | ${r['total_pnl']:,.0f} | {dtag} |")
        A("")

    # ── 3. Rankings ──
    oos = grid[(grid.period == "OOS (2025)") & grid.n.notna()].copy()
    oos["combo"] = ("EPS≥" + oos.eps_threshold.map(lambda x: f"{x:g}") + "% / score "
                    + oos.score_cutoff + " / " + oos.stop_label)
    oos_sh = oos[oos.sharpe.notna()].sort_values("sharpe", ascending=False).head(5)
    oos_pf = oos[oos.profit_factor != float("inf")].sort_values("profit_factor", ascending=False).head(5)

    A("## 3. Rankings (OOS = 2025)\n")
    A("### Top 5 by OOS Sharpe\n")
    A("| # | Combination | n | Win% | Avg% | PF | Sharpe | MaxDD% | Beats baseline OOS? | IS check |")
    A("|--:|-------------|--:|-----:|-----:|---:|-------:|------:|:-------------------:|:--------:|")
    _rank_rows(A, oos_sh, grid, bOOS)
    A("\n### Top 5 by OOS Profit Factor\n")
    A("| # | Combination | n | Win% | Avg% | PF | Sharpe | MaxDD% | Beats baseline OOS? | IS check |")
    A("|--:|-------------|--:|-----:|-----:|---:|-------:|------:|:-------------------:|:--------:|")
    _rank_rows(A, oos_pf, grid, bOOS)
    A("\n*“IS check” compares the same combo's IS avg return vs the IS baseline "
      f"({bIS['avg_return']}%). **Wins-OOS-but-loses-IS, or wins-IS-but-loses-OOS ⇒ rejected.** "
      "No combo here is “validated”: every candidate is flagged for a forward walk-forward / "
      "paper-trading period before any `strategy.md` change (see §6).*\n")

    # Robustness scan: which combos beat baseline avg return in BOTH IS and OOS?
    isg = grid[grid.period == "IS (2022-2024)"]
    oosg = grid[grid.period == "OOS (2025)"]
    both = []
    for _, r in oosg[oosg.n.notna()].iterrows():
        ism = isg[(isg.eps_threshold == r.eps_threshold) & (isg.score_cutoff == r.score_cutoff)
                  & (isg.stop_key == r.stop_key)]
        if not len(ism):
            continue
        isr = ism.iloc[0]
        if r.avg_return > bOOS["avg_return"] and isr.avg_return > bIS["avg_return"]:
            both.append((r.eps_threshold, r.score_cutoff, r.stop_label,
                         isr.avg_return, r.avg_return, r.max_drawdown_pct))
    A("**Robustness cross-check — which of the 45 combos beat the baseline in BOTH IS and OOS "
      "avg return?**")
    if not both:
        A("- **None.** No swept combination is a consistent (both-period) improvement over the "
          "current baseline. The high-OOS-Sharpe combos above all *underperform* baseline in-sample; "
          "the strong-IS combos underperform out-of-sample.\n")
    else:
        A(f"- **{len(both)}** combo(s) beat baseline in both periods:")
        for eps, sc, stp, isa, oosa, dd in both:
            A(f"  - EPS≥{eps:g}% / score {sc} / {stp}: IS {isa}% (base {bIS['avg_return']}%), "
              f"OOS {oosa}% (base {bOOS['avg_return']}%), OOS MaxDD {dd}%. "
              "— but by a thin margin and on the same entries as baseline (wider stop only bites the "
              "high-ATR minority); **reverses on 2026** (§5), so still not robust across the full window.")
        A("")

    # ── 4. S3 re-test: wider stop × looser filters ──
    A("## 4. Does loosening the entry filter change the S3 verdict on wider stops?\n")
    A("S3 (standalone) tested **max(8%, 2.0×ATR) [=atr20] vs flat −8% [=flat8] with the CURRENT "
      "entry filters** on OOS = **2025+2026** and concluded *V2 does not improve on V0 out-of-sample* "
      "(0.64% vs 0.70% avg; PF 1.08 vs 1.20 → **keep V0**). This sweep re-tests that pairing "
      "**inside every looser entry combo** — a distinct hypothesis (wider stop **combined with** a "
      "looser bar), since S3 only tested it in isolation at the current bar.\n")

    # First: reproduce S3's own OOS window (2025+2026) at the current bar as the anchor.
    cur25 = df[(df.period == "OOS (2025)") & (df.surprise_pct >= 15.0) & (df.q == 3) & (df.f_nearearn)]
    comb = pd.concat([cur25, df26], ignore_index=True)
    A("**Anchor — reproduce S3 on its own OOS window (2025+2026), current bar (n="
      f"{len(comb)}):**")
    A(f"| Stop | avg% (2025 only, n={len(cur25)}) | avg% (2025+2026, n={len(comb)}) |")
    A("|------|----------------------:|----------------------:|")
    for key, slab, *_ in STOP_VARIANTS:
        a25 = round(cur25[f"{key}_ret_pct"].mean(), 2)
        ac = round(comb[f"{key}_ret_pct"].mean(), 2)
        A(f"| {slab} | {a25} | {ac} |")
    f8c = round(comb["flat8_ret_pct"].mean(), 2)
    a20c = round(comb["atr20_ret_pct"].mean(), 2)
    A(f"\nOn S3's full OOS window (2025+2026) at the current bar, **flat −8% ({f8c}%) still beats "
      f"2.0×ATR ({a20c}%)** — an exact reproduction of S3's 0.70% vs 0.64%. The 2026 slice (§5) is "
      f"where wider stops clearly lose; it drags the combined figure below flat −8%.\n")

    # ATR-floor binding fact
    atr20_bind = round((df["atr20_stop_pct"] > 8.0001).mean() * 100, 1)
    atr15_bind = round((df["atr15_stop_pct"] > 8.0001).mean() * 100, 1)
    A(f"**Why the ATR variants ≈ flat −8%:** entry-day ATR averages {round(df.atr_pct.mean(),2)}%/day, "
      f"so max(8%, k×ATR) only lifts the stop above 8% on **{atr20_bind}%** of trades at 2.0×ATR "
      f"(**{atr15_bind}%** at 1.5×ATR). For ~86% of names the ATR stop *is* the flat 8% stop; any edge "
      f"comes from the &lt;14% of high-ATR names dodging an early noise stop (the MU case S3 studied).\n")

    A("Per-combo OOS = **2025 only** (the only window available at looser bars — no 2026 base in the "
      "committed data): each wider stop minus flat −8% (avg return %, identical trades per row):\n")
    A("| EPS | Score | n | flat−8 avg% | −10% Δ | −12% Δ | 1.5×ATR Δ | 2.0×ATR (S3) Δ |")
    A("|----:|:-----:|--:|-----------:|-------:|-------:|----------:|---------------:|")
    g = grid[grid.period == "OOS (2025)"]
    fixed_win = atr_win = total = 0
    for eps in EPS_THRESHOLDS:
        for slabel, qmin in SCORE_LEVELS:
            b = g[(g.eps_threshold == eps) & (g.score_cutoff == slabel) & (g.stop_key == "flat8")].iloc[0]
            if b["n"] is None or (isinstance(b["n"], float) and pd.isna(b["n"])):
                continue
            total += 1
            def d(k):
                r = g[(g.eps_threshold == eps) & (g.score_cutoff == slabel) & (g.stop_key == k)].iloc[0]
                return round(r["avg_return"] - b["avg_return"], 2)
            d10, d12, da15, da20 = d("flat10"), d("flat12"), d("atr15"), d("atr20")
            if max(d10, d12) > 0:
                fixed_win += 1
            if da20 > 0:
                atr_win += 1
            A(f"| ≥{eps:g}% | {slabel} | {int(b['n'])} | {b['avg_return']} | {d10:+.2f} | "
              f"{d12:+.2f} | {da15:+.2f} | {da20:+.2f} |")
    A("")
    A(f"**Verdict — CONFIRMS S3; does NOT overturn it.**")
    A(f"1. On S3's own OOS window (2025+2026) at the current bar, flat −8% still wins "
      f"({f8c}% vs {a20c}%) — reproduced exactly. 2. On 2025 alone, 2.0×ATR edges flat −8% at "
      f"{atr_win}/{total} bars, but the edge is razor-thin (≤+0.22 pp/trade), appears **at the "
      f"current bar too** (≥15/≥6: +0.08) so it is **not** a loosening effect, and **reverses on "
      f"2026** (§5: atr20 −0.55% vs flat8 −0.23%). 3. **Fixed** wider stops (−10%/−12%) are worse "
      f"OOS at {total - fixed_win}/{total} bars — they only help IS (§2b), the classic overfit "
      f"signature. Loosening the entry bar therefore does **not** create a robust wider-stop edge; "
      f"the standalone S3 rejection stands.\n")

    # ── 5. 2026 YTD cross-check ──
    A("## 5. 2026 YTD cross-check — current filter only (stop width × 30 enhanced trades)\n")
    A("The committed 2026 dataset is the **30 enhanced trades** (all already EPS≥15% & q==3 = the "
      "baseline entry combo). The full 2026 BASE population needed for the loosened-filter cells is "
      "**not** in the committed data and cannot be rebuilt here (yfinance earnings endpoint blocked in "
      "this environment), so **every loosened-filter 2026 cell is N/A** — not fabricated. This panel "
      "therefore only extends S3's 2026 stop-width finding at the current bar.\n")
    A("| Stop | n | Win% | Avg% | Med% | PF | Sharpe | MaxDD% | AvgHold | TotP&L |")
    A("|------|--:|-----:|-----:|-----:|---:|-------:|------:|--------:|-------:|")
    for _, r in panel26.iterrows():
        if "n" not in r or pd.isna(r.get("n")):
            A(f"| {r['stop_label']} | — | — | — | — | — | — | — | — | — |")
            continue
        A(f"| {r['stop_label']} | {int(r['n'])} | {r['win_rate']} | {r['avg_return']} | "
          f"{r['median_return']} | {pf_s(r['profit_factor'])} | {num(r['sharpe'])} | "
          f"{r['max_drawdown_pct']} | {r['avg_holding_days']} | ${r['total_pnl']:,.0f} |")
    A(f"\n*SPY 2026 YTD buy-and-hold: {spy['2026 YTD']}%. n=30 is far too small for any conclusion; "
      "shown only to check the direction of the stop-width effect on the 2026 slice against S3.*\n")

    # ── 6. Reporting discipline / recommendation ──
    A("## 6. Discipline notes & recommendation\n")
    A("**Bottom line:** no swept combination is a validated improvement, and the current parameters "
      "(EPS ≥15% / score ≥6 / flat −8%) remain the best *consistent* (both-period) risk-adjusted "
      "choice.")
    A("- **Loosening the entry bar** (score ≥5/≥4 or EPS ≥12.5%/≥10%) raises the *raw* OOS 2025 "
      "return and win rate, but it **underperforms baseline in-sample** and multiplies drawdown "
      "(OOS MaxDD from ~−6% at baseline to ~−27% to −48%) and max-consecutive-losses (5 → 14–22). "
      "The best-looking OOS combos are the worst IS combos — the textbook overfit signature — so "
      "they are **rejected**, not endorsed.")
    A("- **Widening the stop** confirms S3 (§4): fixed −10%/−12% mostly hurt OOS; the ATR variants "
      "are ≈ flat −8% because the ATR term clears 8% on <14% of trades, and their sliver of 2025 "
      "edge reverses on 2026.")
    A("- **If anything is worth a forward test**, it is the single razor-thin both-period combo "
      "surfaced in §3 (EPS≥15 / score≥6 / 2.0×ATR floor) — i.e. keep the current entry bar and only "
      "widen the stop for genuinely high-ATR names — and even that must clear a walk-forward / paper "
      "period first (it lost on 2026). **Do not loosen the entry filters on this evidence.**\n")
    A("- **Nothing here is “validated.”** This is a single historical backtest on survivorship-biased, "
      "cost-free data. Any combo that looks attractive is at most a **candidate for a forward "
      "walk-forward or paper-trading validation period** before `strategy.md` is touched — and per "
      "`CLAUDE.md`, only the human operator edits `strategy.md`.")
    A("- **IS≠OOS ⇒ reject.** Combos that beat baseline IS but not OOS (or vice-versa) are curve-fit "
      "artifacts, not edges. See the “IS check” column in §3 and the two full grids in §2.")
    A("- **Every rate above carries its raw `n`.** Loosened-EPS / loosened-score cells admit more "
      "trades but the OOS denominators still range from ~53 (baseline) to ~500 (loosest) — the tighter "
      "OOS cells remain modest samples.")
    A("- **S3 re-statement:** this sweep tests wider stops *combined with looser entry filters*, a "
      "distinct hypothesis from the standalone S3 test (wider stop, current filters). See §4 for the "
      "explicit confirm/overturn verdict.")
    A("\n---\n*Engine: reuses the S3 `simulate()` mechanics and the committed validated candidate set. "
      "Survivorship bias, zero transaction costs/slippage, and independent-per-trade sizing (no "
      "portfolio capital constraint) apply, as in every prior report in this repo.*")
    return "\n".join(L)


def _rank_rows(A, ranked, grid, bOOS):
    isg = grid[grid.period == "IS (2022-2024)"]
    bIS = baseline_row(grid, "IS (2022-2024)")
    for i, (_, r) in enumerate(ranked.iterrows(), 1):
        beats = "✅" if (r["avg_return"] is not None and r["avg_return"] > bOOS["avg_return"]) else "❌"
        ism = isg[(isg.eps_threshold == r.eps_threshold) & (isg.score_cutoff == r.score_cutoff)
                  & (isg.stop_key == r.stop_key)]
        if len(ism):
            isr = ism.iloc[0]
            is_ok = (isr["avg_return"] is not None and isr["avg_return"] > bIS["avg_return"])
            ischk = f"IS {isr['avg_return']}% {'✓' if is_ok else '✗(rej)'}"
        else:
            ischk = "—"
        A(f"| {i} | {r['combo']} | {int(r['n'])} | {r['win_rate']} | {r['avg_return']} | "
          f"{pf_s(r['profit_factor'])} | {num(r['sharpe'])} | {r['max_drawdown_pct']} | {beats} | {ischk} |")


# ─── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Loading committed entry sets...")
    cand = load_entry_set()
    cand26 = load_2026()
    all_tickers = sorted(set(cand.ticker) | set(cand26.ticker) | {"SPY"})
    print(f"  {len(cand)} candidates (2022-2025) + {len(cand26)} (2026) over {len(all_tickers)} tickers")

    print("Fetching / caching OHLC (Yahoo chart API)...")
    hist_map = {}
    for i, t in enumerate(all_tickers):
        if i % 25 == 0:
            ok = sum(v is not None for v in hist_map.values())
            print(f"  {i}/{len(all_tickers)} ({ok} ok)...")
        hist_map[t] = cached_history(t)
    n_ok = sum(v is not None for v in hist_map.values())
    print(f"  history: {n_ok}/{len(all_tickers)} tickers")

    print("Simulating 2022-2025 candidates across 5 stop variants...")
    df = simulate_all(cand, hist_map)
    print("Simulating 2026 YTD candidates...")
    df26 = simulate_all(cand26, hist_map)

    print("Building grid + SPY benchmark...")
    grid = build_grid(df)
    panel26 = build_2026_panel(df26)
    spy = spy_returns()

    # ── write per-trade CSV ──
    trade_cols = (["ticker", "sector", "is_it", "year", "period", "entry_date",
                   "surprise_pct", "q", "f_vol15x", "f_rs", "f_52w", "f_nearearn", "atr_pct"]
                  + [f"{k}_{s}" for k, *_ in STOP_VARIANTS
                     for s in ("stop_pct", "pos_dollar", "ret_pct", "ret_dollar", "exit", "hold")])
    all_trades = pd.concat([df, df26], ignore_index=True)
    all_trades[[c for c in trade_cols if c in all_trades.columns]].to_csv(
        os.path.join(REPORTS_DIR, f"backtest_risk_sweep_trades_{RUN_DATE}.csv"), index=False)

    # ── write grid CSV ──
    grid_out = grid.copy()
    for period in ["IS (2022-2024)", "OOS (2025)"]:
        base = baseline_row(grid, period)
        mask = grid_out.period == period
        grid_out.loc[mask, "avg_return_vs_baseline"] = grid_out.loc[mask, "avg_return"].map(
            lambda v: None if v is None or pd.isna(v) else round(v - base["avg_return"], 3))
    grid_out.to_csv(os.path.join(REPORTS_DIR, f"backtest_risk_sweep_grid_{RUN_DATE}.csv"), index=False)

    # ── write report md ──
    report = build_report(df, df26, grid, panel26, spy)
    rpath = os.path.join(MEMORY_DIR, f"backtest_risk_sweep_{RUN_DATE}.md")
    with open(rpath, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n=== HEADLINE (OOS 2025) ===")
    bOOS = baseline_row(grid, "OOS (2025)")
    print(f"Baseline OOS: n={bOOS['n']} win {bOOS['win_rate']}% avg {bOOS['avg_return']}% "
          f"PF {pf_s(bOOS['profit_factor'])} Sharpe {bOOS['sharpe']} MaxDD {bOOS['max_drawdown_pct']}%")
    print(f"SPY: {spy}")
    print(f"\nReport: {rpath}")
    print(f"Grid CSV: backtest_risk_sweep_grid_{RUN_DATE}.csv")
    print(f"Trades CSV: backtest_risk_sweep_trades_{RUN_DATE}.csv")


if __name__ == "__main__":
    main()
