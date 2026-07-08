"""
Chronic-never-worked early-exit rule vs current -8%-only baseline -- head-to-head
PEAD backtest.

Follow-up to `memory/stop_audit_2026-07-07.md` (H4): that 13-trade live-book audit
found chronic never-worked positions (majority of holding period closing
underwater, MFE never confirmed +3%) were the modal hard-stop loss bucket
(4/8, 50%), but also found 2 of those 4 (PWR, CASY) later recovered fully after
the eventual hard stop fired. H4 called for a dedicated backtest weighing avoided
chronic-drift losses against foreclosed recoveries before touching any live rule.
This script is that backtest.

Rule under test: for a position held under the CURRENT entry/exit rules (flat -8%
hard stop; scale out 1/3 + 7% trail at +10%; 42-calendar-day time stop), add one
more exit trigger:

    exit at close if, by trading day D since entry, MFE has not reached +3%
    AND the position has closed underwater for K consecutive sessions.

Grid: D in {5, 7, 10} trading days, K in {3, 4, 5} consecutive underwater closes
-- 9 combinations, all reported (no cherry-picking).

Reuses the exact same validated candidate set as every other PEAD backtest in
this repo (backtesting/reports/backtest_trades_PEAD_2022_2025_ENHANCED_base.csv
+ backtest_trades_PEAD_2026_YTD.csv, same enhanced-filter stack), the same
Yahoo chart-API OHLC fetch + backtesting/data_cache/ pickle cache, and the same
in-sample (2022-2024) vs out-of-sample (2025+2026) split discipline used in
`backtest_atr_stop_widened.py` (the S3 ATR-stop test) -- the split that
correctly caught S3 failing OOS despite looking strong in-sample.

No regime gate is applied to the candidate set (matching the S3 script's own
V0/V2 baseline, not the separate bull-regime-gate variant) -- this tests the
exit-rule question on the full enhanced-filter entry population for statistical
power; see the report's Limitations section for what that does and doesn't
imply about the smaller regime-gated live book.

Diagnostic only. Does not modify memory/strategy.md and is not a production
change -- same status as the stop-audit report it follows up on.
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
POS_CAP_DOLLAR = EQUITY * POS_CAP_PCT      # $11,000 -- fixed; this rule doesn't touch sizing

TRAIL_PCT     = 0.07
TRAIL_TRIGGER = 0.10
SCALE_FRAC    = 1.0 / 3.0
TIME_STOP     = 42                          # calendar days
FLAT_STOP_PCT = 8.0

MFE_THRESHOLD = 3.0                         # percent
D_GRID = [5, 7, 10]                         # trading days since entry
K_GRID = [3, 4, 5]                          # consecutive underwater closes

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


def simulate(hist, entry_date, chronic=None):
    """
    Baseline (chronic=None): flat -8% hard stop; scale 1/3 + 7% trail at +10%;
    42-calendar-day time stop. Identical mechanics to every other PEAD backtest
    in this repo.

    chronic=(D, K): additionally exit at close if, by trading day D since entry
    (day 1 = entry day), MFE (max High since entry / entry - 1) has not reached
    +3% AND the position has closed underwater for K consecutive sessions.
    Checked every day, after the hard-stop check and before the trail-trigger check,
    so a resting hard stop always takes priority over the chronic-exit review,
    matching how a live stop order vs. an end-of-day rule review would actually
    interact.
    """
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data = hist[hist.index == entry_date]
    if day_data.empty:
        return None
    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < eng.MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1.0 - FLAT_STOP_PCT / 100.0)
    future = hist[hist.index >= entry_date]

    booked = 0.0
    open_frac = 1.0
    scaled = False
    trail_active = False
    highest = entry_price          # peak CLOSE since entry (drives the 7% trail)
    running_max_high = -np.inf     # peak HIGH since entry (drives MFE)
    underwater_streak = 0

    D = K = None
    if chronic is not None:
        D, K = chronic

    for i, (dt, row) in enumerate(future.iterrows()):
        close = row["Close"]
        high = row["High"]
        if pd.isna(close):
            continue
        if not pd.isna(high):
            running_max_high = max(running_max_high, high)
        if close > highest:
            highest = close
        cal_days = (dt - entry_date).days
        trading_day = i + 1

        # 1. hard stop -- a resting order, always checked first
        if not scaled and close <= hard_stop_price:
            ret = (close - entry_price) / entry_price
            return _result(dt, ret, "hard_stop", cal_days)

        # underwater streak, updated every day regardless of D
        if close < entry_price:
            underwater_streak += 1
        else:
            underwater_streak = 0

        # 2. chronic-never-worked early exit (variant only)
        if chronic is not None and not scaled and trading_day >= D:
            mfe_pct = (running_max_high / entry_price - 1.0) * 100.0
            if mfe_pct < MFE_THRESHOLD and underwater_streak >= K:
                ret = (close - entry_price) / entry_price
                return _result(dt, ret, "chronic_exit", cal_days)

        # 3. profit-lock trigger / trailing stop
        if not scaled and close >= entry_price * (1.0 + TRAIL_TRIGGER):
            booked += SCALE_FRAC * TRAIL_TRIGGER
            open_frac = 1.0 - SCALE_FRAC
            scaled = True
            trail_active = True

        if trail_active:
            trail_stop = highest * (1.0 - TRAIL_PCT)
            if close <= trail_stop:
                ret_open = (close - entry_price) / entry_price
                total = booked + open_frac * ret_open
                return _result(dt, total, "trail_stop", cal_days)

        # 4. time stop
        if cal_days >= TIME_STOP:
            ret_open = (close - entry_price) / entry_price
            total = booked + open_frac * ret_open
            return _result(dt, total, "time", cal_days)

    last = future.iloc[-1]
    ret_open = (last["Close"] - entry_price) / entry_price
    total = booked + open_frac * ret_open
    return _result(last.name, total, "data_end", (last.name - entry_date).days)


def _result(dt, ret, reason, days):
    return {"exit_date": dt.date(), "return_pct": ret * 100.0, "exit_reason": reason,
            "holding_days": days}


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

        v0 = simulate(hist, entry_date, chronic=None)
        if v0 is None:
            no_entry += 1
            continue

        row = {
            "ticker": t, "sector": c["sector"], "is_it": bool(c["is_it"]),
            "year": int(c["year"]),
            "earn_date": c["earn_date"], "entry_date": entry_date.date(),
            "surprise_pct": round(float(c["surprise_pct"]), 2) if pd.notna(c["surprise_pct"]) else None,
            "v0_return_pct": round(v0["return_pct"], 3),
            "v0_exit_reason": v0["exit_reason"],
            "v0_holding_days": v0["holding_days"],
            "v0_return_dollar": round(v0["return_pct"] / 100.0 * POS_CAP_DOLLAR, 2),
        }

        for D in D_GRID:
            for K in K_GRID:
                key = f"D{D}K{K}"
                vv = simulate(hist, entry_date, chronic=(D, K))
                if vv is None:
                    continue
                row[f"{key}_return_pct"] = round(vv["return_pct"], 3)
                row[f"{key}_exit_reason"] = vv["exit_reason"]
                row[f"{key}_holding_days"] = vv["holding_days"]
                row[f"{key}_return_dollar"] = round(vv["return_pct"] / 100.0 * POS_CAP_DOLLAR, 2)
                row[f"{key}_triggered"] = (vv["exit_reason"] == "chronic_exit")

        rows.append(row)

    print(f"\nSimulated trades: {len(rows)}, no-history: {no_hist}, no-entry/skip: {no_entry}")
    return pd.DataFrame(rows)


def variant_stats(df, prefix):
    if df.empty:
        return None
    rp = df[f"{prefix}_return_pct"]
    winners = df[rp > 0]
    losers = df[rp <= 0]
    gw = winners[f"{prefix}_return_dollar"].sum()
    gl = abs(losers[f"{prefix}_return_dollar"].sum())
    pf = gw / gl if gl > 0 else float("inf")
    return {
        "trades": len(df),
        "win_rate": round((rp > 0).mean() * 100, 1),
        "avg_return": round(rp.mean(), 2),
        "median_return": round(rp.median(), 2),
        "avg_winner": round(winners[f"{prefix}_return_pct"].mean(), 2) if not winners.empty else 0.0,
        "avg_loser": round(losers[f"{prefix}_return_pct"].mean(), 2) if not losers.empty else 0.0,
        "profit_factor": round(pf, 2) if pf != float("inf") else float("inf"),
        "total_pnl": round(df[f"{prefix}_return_dollar"].sum(), 0),
    }


def pf_str(v):
    return "inf" if v == float("inf") else f"{v}"


PERIODS = [
    ("2022-2024", lambda d: d[d.year.isin([2022, 2023, 2024])]),
    ("2025",      lambda d: d[d.year == 2025]),
    ("2026 YTD",  lambda d: d[d.year == 2026]),
]


def avoided_and_foreclosed(df, key):
    """
    Among trades where the chronic rule fires (exit_reason == chronic_exit):
      - avoided: baseline (V0) eventually hit the hard stop -> chronic exit cut
        the loss earlier/smaller than the full -8%.
      - foreclosed: baseline (V0) eventually closed profitably (any exit
        reason) -> the chronic rule would have locked in a loss instead of
        letting the position recover, exactly the PWR/CASY pattern from the
        13-trade live audit.
      - neutral: baseline was also a loss but NOT via hard_stop (e.g. time
        stop / data_end at a loss) -- neither a clean "avoided -8%" nor a
        "foreclosed recovery"; reported for completeness.
    """
    trig = df[df[f"{key}_triggered"]]
    avoided = trig[trig["v0_exit_reason"] == "hard_stop"]
    foreclosed = trig[trig["v0_return_pct"] > 0]
    neutral = trig[(trig["v0_exit_reason"] != "hard_stop") & (trig["v0_return_pct"] <= 0)]
    return {
        "n_triggered": len(trig),
        "n_avoided": len(avoided),
        "avoided_v0_avg_return": round(avoided["v0_return_pct"].mean(), 2) if not avoided.empty else None,
        "avoided_chronic_avg_return": round(avoided[f"{key}_return_pct"].mean(), 2) if not avoided.empty else None,
        "n_foreclosed": len(foreclosed),
        "foreclosed_v0_avg_return": round(foreclosed["v0_return_pct"].mean(), 2) if not foreclosed.empty else None,
        "foreclosed_chronic_avg_return": round(foreclosed[f"{key}_return_pct"].mean(), 2) if not foreclosed.empty else None,
        "n_neutral": len(neutral),
    }


def build_report(df):
    L = []
    A = L.append
    A("# Backtest: Chronic-Never-Worked Early-Exit Rule vs Current -8%-Only Baseline")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} -- "
      f"window {TEST_START}->{TEST_END}, S&P 500 current constituents (survivorship-biased).*\n")
    A("Follow-up to `memory/stop_audit_2026-07-07.md` (hypothesis H4). That audit found "
      "chronic never-worked positions were the modal hard-stop-loss bucket in the live "
      "13-trade sample (4/8, 50%), but 2 of those 4 (PWR, CASY) later recovered fully after "
      "the eventual hard stop fired -- so an early chronic-exit rule is not a free lunch. "
      "This backtest tests the rule at scale, with the same in-sample/out-of-sample "
      "discipline used for the S3 ATR-stop test (the split that correctly caught S3 failing "
      "OOS despite looking strong in-sample).\n")
    A("**Rule tested:** exit at close if, by trading day D since entry, MFE (peak High since "
      "entry vs. entry price) has not reached +3% AND the position has closed underwater for "
      "K consecutive sessions. Layered on top of the current rules (flat -8% hard stop always "
      "takes priority; 1/3 scale-out + 7% trail at +10%; 42-calendar-day time stop) -- it "
      "never overrides an already-fired hard stop, it only potentially exits *earlier*.\n")
    A(f"**Grid tested (no cherry-picking):** D in {D_GRID}, K in {K_GRID} -- "
      f"{len(D_GRID) * len(K_GRID)} combinations, all reported below.\n")
    A("**Position sizing is unchanged** (fixed $11,000 / 11% of $100k equity) -- this rule "
      "only changes exit *timing*, not position size, so dollar P&L differences reflect the "
      "exit-timing effect in isolation.\n")

    A("## 1. Baseline (V0, current -8%-only rules)\n")
    v0_all = variant_stats(df, "v0")
    A(f"Full sample: **{v0_all['trades']} trades**, win rate {v0_all['win_rate']}%, "
      f"avg return {v0_all['avg_return']}%, median {v0_all['median_return']}%, "
      f"PF {pf_str(v0_all['profit_factor'])}, total P&L ${v0_all['total_pnl']:,.0f}.\n")
    A("| Period | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | Total P&L |")
    A("|--------|-------:|-----:|-----:|-----:|--------:|---------:|---:|----------:|")
    for pname, sel in PERIODS:
        sub = sel(df)
        s = variant_stats(sub, "v0")
        if s is None:
            A(f"| {pname} | 0 | - | - | - | - | - | - | - |")
            continue
        A(f"| {pname} | {s['trades']} | {s['win_rate']}% | {s['avg_return']}% | {s['median_return']}% | "
          f"{s['avg_winner']}% | {s['avg_loser']}% | {pf_str(s['profit_factor'])} | ${s['total_pnl']:,.0f} |")
    A("")

    A("## 2. Grid results -- all 9 (D, K) combinations vs baseline\n")
    A("Win rate / avg return / profit factor for the chronic-exit variant, full sample and "
      "split in-sample (2022-2024) vs out-of-sample (2025+2026 YTD), same split methodology "
      "as the S3 ATR-stop backtest.\n")
    A("| D | K | # triggered (full) | Full Win% | Full Avg% | Full PF | IS (22-24) Avg% | IS PF | "
      "OOS (25+26) Avg% | OOS PF | OOS verdict |")
    A("|--:|--:|---:|---:|---:|---:|---:|---:|---:|---:|---|")

    is_mask = df.year.isin([2022, 2023, 2024])
    oos_mask = df.year.isin([2025, 2026])
    is_v0 = variant_stats(df[is_mask], "v0")
    oos_v0 = variant_stats(df[oos_mask], "v0")

    grid_rows = []
    for D in D_GRID:
        for K in K_GRID:
            key = f"D{D}K{K}"
            s_full = variant_stats(df, key)
            s_is = variant_stats(df[is_mask], key)
            s_oos = variant_stats(df[oos_mask], key)
            n_trig_full = int(df[f"{key}_triggered"].sum())
            oos_better = (s_oos["avg_return"] >= oos_v0["avg_return"]) and \
                         (pf_str(s_oos["profit_factor"]) == "inf" or s_oos["profit_factor"] >= oos_v0["profit_factor"])
            verdict = "IMPROVES/HOLDS" if oos_better else "DOES NOT IMPROVE"
            A(f"| {D} | {K} | {n_trig_full} | {s_full['win_rate']}% | {s_full['avg_return']}% | "
              f"{pf_str(s_full['profit_factor'])} | {s_is['avg_return']}% | {pf_str(s_is['profit_factor'])} | "
              f"{s_oos['avg_return']}% | {pf_str(s_oos['profit_factor'])} | {verdict} |")
            grid_rows.append((D, K, s_full, s_is, s_oos, verdict, n_trig_full))
    A("")
    A(f"_Baseline for comparison -- Full: win {v0_all['win_rate']}% avg {v0_all['avg_return']}% "
      f"PF {pf_str(v0_all['profit_factor'])}. IS (22-24): avg {is_v0['avg_return']}% PF {pf_str(is_v0['profit_factor'])}. "
      f"OOS (25+26): avg {oos_v0['avg_return']}% PF {pf_str(oos_v0['profit_factor'])}._\n")

    A("## 3. Avoided losses vs. foreclosed recoveries -- all 9 combinations\n")
    A("For every trade where the chronic rule actually fires (`chronic_exit`), this splits the "
      "outcome by what the CURRENT (-8%-only) rules would have done with that same trade if left "
      "alone:\n")
    A("- **Avoided** = baseline eventually hit the hard stop anyway -- chronic exit got out earlier/smaller.")
    A("- **Foreclosed** = baseline eventually closed profitably (trail stop, time stop, or data-end) -- "
      "chronic exit would have cut a trade that later recovered, the PWR/CASY pattern.")
    A("- **Neutral** = baseline was also a loss, but not via the hard stop (time-stop/data-end loss) -- "
      "neither a clean avoided-loss nor a foreclosed-recovery case.\n")
    A("| D | K | # Triggered | Avoided (V0 hard-stop) | Avoided: V0 avg% -> Chronic avg% | "
      "Foreclosed (V0 profitable) | Foreclosed: V0 avg% forgone -> Chronic avg% taken | Neutral |")
    A("|--:|--:|---:|---:|---|---:|---|---:|")
    for D in D_GRID:
        for K in K_GRID:
            key = f"D{D}K{K}"
            s = avoided_and_foreclosed(df, key)
            av = f"{s['avoided_v0_avg_return']}% -> {s['avoided_chronic_avg_return']}%" if s["n_avoided"] else "-"
            fo = f"{s['foreclosed_v0_avg_return']}% -> {s['foreclosed_chronic_avg_return']}%" if s["n_foreclosed"] else "-"
            A(f"| {D} | {K} | {s['n_triggered']} | {s['n_avoided']} | {av} | {s['n_foreclosed']} | {fo} | {s['n_neutral']} |")
    A("")

    A("## 4. Net effect on hard-stop-loss trades specifically\n")
    A("Restricting to the subset of trades whose CURRENT (-8%-only) outcome is a hard-stop loss "
      "(the exact population the stop audit examined), how much of that loss bucket does each "
      "(D, K) combination intercept, and at what average loss reduction?\n")
    hard_stop_pop = df[df.v0_exit_reason == "hard_stop"]
    A(f"Hard-stop-loss trades in the full backtest sample: **{len(hard_stop_pop)}** "
      f"(of {len(df)} total, {round(len(hard_stop_pop) / len(df) * 100, 1)}%), avg return "
      f"{round(hard_stop_pop['v0_return_pct'].mean(), 2)}%.\n")
    A("| D | K | Intercepted (of hard-stop pop.) | Intercept rate | Avg loss under V0 | Avg loss under chronic exit | Avg loss reduction |")
    A("|--:|--:|---:|---:|---:|---:|---:|")
    for D in D_GRID:
        for K in K_GRID:
            key = f"D{D}K{K}"
            sub = hard_stop_pop[hard_stop_pop[f"{key}_triggered"]]
            if hard_stop_pop.empty:
                continue
            rate = round(len(sub) / len(hard_stop_pop) * 100, 1) if len(hard_stop_pop) else 0.0
            if not sub.empty:
                v0m = round(sub["v0_return_pct"].mean(), 2)
                chm = round(sub[f"{key}_return_pct"].mean(), 2)
                red = round(chm - v0m, 2)
                v0m_s, chm_s = f"{v0m}%", f"{chm}%"
                red_s = f"+{red}%" if red > 0 else f"{red}%"
            else:
                v0m_s = chm_s = red_s = "-"
            A(f"| {D} | {K} | {len(sub)} | {rate}% | {v0m_s} | {chm_s} | {red_s} |")
    A("")

    A("## 5. Recommendation\n")
    best = max(grid_rows, key=lambda r: (r[5] == "IMPROVES/HOLDS", r[4]["avg_return"]))
    A(f"Of the 9 combinations, the ones passing the OOS bar (avg return AND PF at or above baseline "
      f"on 2025+2026) are: " +
      (", ".join(f"D={r[0]},K={r[1]}" for r in grid_rows if r[5] == "IMPROVES/HOLDS") or "none") + ".\n")
    A("This is a research read, not a recommendation to change `memory/strategy.md`. Per the "
      "stop-audit's own H4 framing: even a combination that improves full-sample and OOS averages "
      "does so by foreclosing some real recoveries (see §3) -- the right lens is whether the "
      "avoided-loss dollars exceed the foreclosed-recovery dollars at that specific (D, K), not "
      "win rate alone. See Limitations for sample-size and survivorship caveats before treating "
      "any single combination as validated.\n")

    A("## 6. Beat-the-benchmark bar (SPY buy-and-hold, same period, for context)\n")
    A("| Period | SPY buy-and-hold | V0 avg/trade |")
    A("|--------|------------------:|--------------:|")
    for pname, sel in PERIODS:
        sub = sel(df)
        s0 = variant_stats(sub, "v0")
        spy = SPY_BENCHMARK.get(pname, None)
        spy_s = f"{spy}%" if spy is not None else "-"
        A(f"| {pname} | {spy_s} | {s0['avg_return'] if s0 else '-'}% |")
    A("\n_SPY figures are per-period index buy-and-hold return, taken from the other PEAD backtest "
      "reports in this repo; not directly comparable to a single-trade avg% (per-trade return on "
      "~11% position size, not a fully-invested compounded return), shown for context only.\n")

    A("## 7. Limitations\n")
    A("- **No regime gate applied to the candidate set.** This matches the S3 ATR-stop script's "
      "own V0/V2 baseline (not the separate bull-regime-gate variant reported elsewhere in this "
      "repo), chosen for entry-set consistency with the most recent comparable backtest and for "
      "statistical power (277 candidate entries vs. the much smaller 207-trade regime-gated "
      "sample). The live book currently trades under the regime gate, so this backtest's "
      "candidate population is broader than what the live strategy would actually enter today; "
      "treat the grid results as evidence about the *exit rule* in isolation, not as a like-for-like "
      "replay of the exact live entry population.")
    A("- **Survivorship bias.** Tickers are drawn from current S&P 500/400/600 constituents and "
      "current sector classifications, same caveat as every other backtest report in this repo.")
    A("- **MFE uses daily High, not intraday path.** Same simplification as the live stop audit's "
      "multi-day trades; entry/exit-day intraday sequencing is approximated by daily OHLC.")
    A("- **Chronic-exit and hard-stop are both evaluated at the daily close**, i.e. this assumes "
      "an end-of-day rule review can execute at that day's close price -- in live trading, an "
      "analogous rule would likely execute at the next session's open (via `midday` or "
      "`market_close`), which would introduce a small amount of slippage not modeled here.")
    A("- **2026 YTD sample is small** (30 candidate entries per the enhanced-filter stack) -- "
      "the OOS split's 2026 component individually carries limited weight; the OOS verdict "
      "column above is driven mostly by 2025.")
    A("- **This backtest answers a different question than the live 13-trade audit.** The audit's "
      "PWR/CASY recoveries are two specific real trades; this backtest's \"foreclosed recovery\" "
      "counts are the same *pattern* replayed across the full historical candidate set, not a "
      "guarantee those exact two trades appear in this sample under these tickers/dates.")
    A("- No orders were placed and `memory/strategy.md` was not modified to produce this report.\n")

    return "\n".join(L)


def main():
    df = build_trades()
    if df.empty:
        print("No candidates generated.")
        sys.exit(1)

    keep_cols = ["ticker", "sector", "is_it", "year", "earn_date", "entry_date",
                 "surprise_pct", "v0_return_pct", "v0_exit_reason", "v0_holding_days",
                 "v0_return_dollar"]
    for D in D_GRID:
        for K in K_GRID:
            key = f"D{D}K{K}"
            keep_cols += [f"{key}_return_pct", f"{key}_exit_reason", f"{key}_holding_days",
                          f"{key}_return_dollar", f"{key}_triggered"]
    df[keep_cols].to_csv(os.path.join(REPORTS_DIR, "backtest_trades_CHRONIC_EXIT.csv"), index=False)

    report = build_report(df)
    rpath = os.path.join(REPORTS_DIR, "backtest_report_CHRONIC_EXIT.md")
    with open(rpath, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n=== HEADLINE (full sample) ===")
    s0 = variant_stats(df, "v0")
    print(f"V0 baseline: n={s0['trades']} win {s0['win_rate']}% avg {s0['avg_return']}% PF {pf_str(s0['profit_factor'])}")
    for D in D_GRID:
        for K in K_GRID:
            key = f"D{D}K{K}"
            s = variant_stats(df, key)
            n_trig = int(df[f'{key}_triggered'].sum())
            print(f"D={D} K={K}: n_triggered={n_trig} win {s['win_rate']}% avg {s['avg_return']}% PF {pf_str(s['profit_factor'])}")
    print(f"\nReport: {rpath}")
    print(f"Trades CSV: {os.path.join(REPORTS_DIR, 'backtest_trades_CHRONIC_EXIT.csv')}")


if __name__ == "__main__":
    main()
