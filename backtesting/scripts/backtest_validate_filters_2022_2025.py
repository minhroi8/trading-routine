"""
Filter validation on a LARGE sample: enhanced PEAD rules over 2022-2025.

The 2026 YTD run produced only 30 enhanced trades — too few to judge whether the
filters help. This re-applies the SAME verifiable filter stack to 2022-2025 so we
can measure each filter's effect on thousands of trades, and check year-by-year
whether the raw PEAD signal is decaying.

Reuses the engine helpers from backtest_pead_2026_ytd.py (no logic duplication).
"""

import os
import pickle
import pandas as pd
import numpy as np
import time
import sys
from datetime import datetime, timedelta

import yfinance as yf

# --- Path anchoring (research artifacts consolidated under backtesting/) ------
# This script lives in backtesting/scripts/. The shared engine
# backtest_pead_2026_ytd.py stays at the repo root because production
# compute_pead_health.py imports it; add the repo root to sys.path so the bare
# `import backtest_pead_2026_ytd` below still resolves. Reports and the data
# cache resolve relative to this file, not the current working directory.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
_REPORTS_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "reports"))

import backtest_pead_2026_ytd as eng

CACHE_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "data_cache"))
os.makedirs(CACHE_DIR, exist_ok=True)


def cached_fetch(ticker):
    """Disk-cached per-ticker (hist, earnings) so reruns are deterministic + fast."""
    path = os.path.join(CACHE_DIR, ticker.replace("/", "_").replace("\\", "_") + ".pkl")
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    res = eng.fetch_ticker_data(ticker)
    if res[0] is not None:                      # only cache successful fetches
        try:
            with open(path, "wb") as f:
                pickle.dump(res, f)
        except Exception:
            pass
    return res


def robust_spy():
    """SPY download with retries; SPY is critical for regime + relative strength."""
    for attempt in range(5):
        spy = yf.download("SPY", start="2020-01-01", end=eng.DATA_END,
                          auto_adjust=True, progress=False)
        if isinstance(spy.columns, pd.MultiIndex):
            spy.columns = spy.columns.get_level_values(0)
        if not spy.empty and "Close" in spy.columns and spy["Close"].notna().sum() > 200:
            return spy
        print(f"  SPY download attempt {attempt+1} insufficient; retrying...")
        time.sleep(3)
    raise RuntimeError("SPY download failed after 5 retries — aborting (would corrupt "
                       "regime + relative-strength filters).")

# Repoint the engine's fetch window for the longer history
eng.HIST_START = "2020-06-01"     # deep lookback for 52-wk high into early 2022
eng.DATA_END   = "2026-02-15"     # let 42-day stops on Dec-2025 entries resolve

TEST_START = "2022-01-01"
TEST_END   = "2025-12-31"
P = eng.POSITION_SIZE


def run():
    print("Fetching S&P 500 universe...")
    sp500 = eng.get_sp500()
    tickers = sp500["ticker"].tolist()
    sector_map = dict(zip(sp500["ticker"], sp500["sector"]))
    name_map = dict(zip(sp500["ticker"], sp500["name"]))

    print("Fetching SPY (2020-> for 200MA + RS)...")
    spy_hist = robust_spy()
    spy_close, regime = eng.build_spy(spy_hist)
    assert spy_close.notna().sum() > 200, "SPY close series empty after build"

    rows = []
    skipped = no_earn = 0
    total = len(tickers)
    print(f"Processing {total} tickers (2022-2025)...")
    for idx, ticker in enumerate(tickers):
        if idx % 50 == 0:
            print(f"  {idx}/{total} ({len(rows)} candidates)...")
        hist, earnings = cached_fetch(ticker)
        if hist is None:
            skipped += 1; continue
        if earnings is None:
            no_earn += 1; continue

        trading_days = eng.get_trading_days(hist)
        sector = sector_map.get(ticker, "Unknown")
        is_it = (sector == eng.IT_SECTOR)

        for earn_date, erow in earnings.iterrows():
            earn_date = pd.Timestamp(earn_date).normalize()
            if earn_date < pd.Timestamp(TEST_START) - timedelta(days=30):
                continue
            if earn_date > pd.Timestamp(TEST_END):
                continue
            try:
                reported = float(erow.get("reported", np.nan))
                estimate = float(erow.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(reported) or pd.isna(estimate) or not (reported > estimate):
                continue

            entry_date = eng.nth_trading_day_after(trading_days, earn_date, eng.ENTRY_DELAY)
            if entry_date is None or entry_date < pd.Timestamp(TEST_START) or entry_date > pd.Timestamp(TEST_END):
                continue
            day_data = hist[hist.index == entry_date]
            if day_data.empty:
                continue
            open_price = day_data["Open"].iloc[0]
            if pd.isna(open_price) or open_price < eng.MIN_PRICE:
                continue
            if not eng.avg_dvol_ok(hist, earn_date):
                continue

            trail_pct = eng.TRAIL_PCT_IT if is_it else eng.TRAIL_PCT_DEFAULT
            res = eng.simulate_trade(hist, entry_date, trail_pct)
            if res is None:
                continue
            res7 = eng.simulate_trade(hist, entry_date, 0.07)
            res12 = eng.simulate_trade(hist, entry_date, 0.12)

            surprise = None
            if "surprise_pct" in erow and not pd.isna(erow["surprise_pct"]):
                surprise = float(erow["surprise_pct"])
            elif estimate != 0:
                surprise = (reported - estimate) / abs(estimate) * 100

            vratio = eng.vol_ratio_on_day(hist, earn_date)
            rs = eng.rel_strength_vs_spy(hist, spy_close, earn_date, entry_date)
            hi45 = eng.new_52w_high_recent(hist, entry_date)
            d_next = eng.days_to_next_earnings(earnings, earn_date, entry_date)

            rows.append({
                "ticker": ticker, "sector": sector, "is_it": is_it,
                "year": entry_date.year,
                "earn_date": earn_date.date(), "entry_date": entry_date.date(),
                "entry_price": round(open_price, 4),
                "exit_reason": res["exit_reason"], "holding_days": res["holding_days"],
                "return_pct": round(res["return_pct"] * 100, 2),
                "ret_trail7": round(res7["return_pct"] * 100, 2) if res7 else None,
                "ret_trail12": round(res12["return_pct"] * 100, 2) if res12 else None,
                "surprise_pct": round(surprise, 2) if surprise is not None else None,
                "f_surprise15": (surprise is not None) and (surprise >= eng.SURPRISE_MIN),
                "f_vol15x": (vratio is not None) and (vratio >= eng.VOL_MULT),
                "f_rs": (rs is not None) and (rs > 0),
                "f_52w": (hi45 is True),
                "f_nearearn": (d_next is None) or (d_next > eng.NEAR_EARN_DAYS) or (d_next < 0),
                "spy_bull_regime": eng.regime_at(regime, entry_date),
            })
        time.sleep(0.03)

    print(f"\nDone. BASE candidates: {len(rows)}, no-earn: {no_earn}, skipped: {skipped}")
    return pd.DataFrame(rows)


def line(df, ret="return_pct"):
    if df.empty:
        return (0, None, None, None)
    n = len(df)
    wr = round((df[ret] > 0).mean() * 100, 1)
    avg = round(df[ret].mean(), 2)
    gw = (df[df[ret] > 0][ret] / 100 * P).sum()
    gl = abs((df[df[ret] <= 0][ret] / 100 * P).sum())
    pf = round(gw / gl, 2) if gl > 0 else float("inf")
    return (n, wr, avg, pf)


def report(base):
    enh = base[base.f_surprise15 & base.f_vol15x & base.f_rs & base.f_52w & base.f_nearearn]
    scenA = base[base.f_surprise15]
    scenB = base[base.f_surprise15 & base.f_vol15x]
    L = []; A = L.append
    A("# Enhanced PEAD — 2022-2025 Full-Sample Filter Validation\n")
    A(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} — window {TEST_START}→{TEST_END}, "
      "S&P 500 current constituents (survivorship-biased).*\n")
    A("Re-applies the 2026 enhanced filter stack to a large multi-year sample so each filter's "
      "value can be judged on thousands of trades instead of the 30 the 2026 YTD window produced.\n")

    nB, wB, aB, pB = line(base)
    nE, wE, aE, pE = line(enh)
    A("## Headline\n")
    A("| Set | Trades | Win% | Avg% | PF |")
    A("|-----|-------:|-----:|-----:|---:|")
    for nm, d in [("BASE (EPS beat only)", base), ("Scenario A (≥15%)", scenA),
                  ("Scenario B (≥15%+vol)", scenB), ("Full enhanced stack", enh)]:
        n, w, a, p = line(d)
        A(f"| {nm} | {n} | {w}% | {a}% | {p} |")
    A("")
    if nE:
        verdict = ("filters ADD value on a large sample" if (aE > aB and wE >= wB) else
                   "filters do NOT clearly beat EPS-beat-only on a large sample")
        A(f"**Verdict: {verdict}.** Full stack {wE}%/{aE}% vs BASE {wB}%/{aB}% "
          f"over {nB:,} base candidates.\n")

    A("## Per-filter impact (independent removal from BASE)\n")
    A("Removed = BASE trades that FAIL the filter. A good filter removes trades with win rate "
      f"BELOW the BASE win rate ({wB}%).\n")
    A("| Filter | Kept | Removed | Win% kept | Win% removed | Avg% removed | Verdict |")
    A("|--------|-----:|--------:|----------:|-------------:|-------------:|---------|")
    for label, col in [("EPS surprise ≥15%", "f_surprise15"),
                       ("Volume ≥1.5×", "f_vol15x"),
                       ("Rel. strength >0", "f_rs"),
                       ("New 52-wk high ≤45d", "f_52w"),
                       ("Not ≤3d to next earn", "f_nearearn")]:
        kept = base[base[col]]; rem = base[~base[col]]
        wk = round((kept.return_pct > 0).mean()*100,1) if not kept.empty else None
        wr_rm = round((rem.return_pct > 0).mean()*100,1) if not rem.empty else None
        av_rm = round(rem.return_pct.mean(),2) if not rem.empty else None
        if rem.empty:
            v = "removed nothing"
        elif wr_rm < wB - 2:
            v = "✓ strips losers"
        elif wr_rm > wB + 2:
            v = "✗ removes winners"
        else:
            v = "~ neutral"
        A(f"| {label} | {len(kept)} | {len(rem)} | {wk}% | "
          f"{wr_rm if wr_rm is not None else '—'}% | {av_rm if av_rm is not None else '—'}% | {v} |")
    A("")

    A("## Year-by-year signal stability (is PEAD decaying?)\n")
    A("| Year | BASE n | BASE win% | BASE avg% | Enh n | Enh win% | Enh avg% |")
    A("|------|-------:|----------:|----------:|------:|---------:|---------:|")
    for y in [2022, 2023, 2024, 2025]:
        b = base[base.year == y]; e = enh[enh.year == y]
        nb, wb, ab, _ = line(b); ne, we, ae, _ = line(e)
        A(f"| {y} | {nb} | {wb if wb is not None else '—'}% | {ab if ab is not None else '—'}% "
          f"| {ne} | {we if we is not None else '—'}% | {ae if ae is not None else '—'}% |")
    A("\n*Compare against the 2026 YTD figures: BASE 37.9%/-1.24%, Enhanced 36.7%/+0.16%.*\n")

    A("## IT trailing stop: 7% vs 12% (full sample)\n")
    it = enh[enh.is_it]
    if not it.empty:
        A(f"IT enhanced trades: {len(it)}.\n")
        A("| Trail | IT avg% | IT win% |")
        A("|-------|--------:|--------:|")
        A(f"| 7% | {round(it.ret_trail7.mean(),2)}% | {round((it.ret_trail7>0).mean()*100,1)}% |")
        A(f"| 12% | {round(it.ret_trail12.mean(),2)}% | {round((it.ret_trail12>0).mean()*100,1)}% |")
        d = it.ret_trail12.mean() - it.ret_trail7.mean()
        A(f"\nWider 12% trail = {round(d,2)}% per IT trade vs 7% "
          f"({'better' if d>0 else 'worse'}) on the full sample.\n")
    else:
        A("*No IT enhanced trades.*\n")
    A("---\n*Reuses backtest_pead_2026_ytd.py engine. Survivorship bias + no costs apply.*")
    return "\n".join(L), enh


if __name__ == "__main__":
    base = run()
    if base.empty:
        print("No candidates."); sys.exit(1)
    rep, enh = report(base)
    with open(os.path.join(_REPORTS_DIR, "backtest_report_PEAD_2022_2025_ENHANCED.md"), "w", encoding="utf-8") as f:
        f.write(rep)
    base.to_csv(os.path.join(_REPORTS_DIR, "backtest_trades_PEAD_2022_2025_ENHANCED_base.csv"), index=False)
    enh.to_csv(os.path.join(_REPORTS_DIR, "backtest_trades_PEAD_2022_2025_ENHANCED.csv"), index=False)
    nB, wB, aB, pB = line(base); nE, wE, aE, pE = line(enh)
    print(f"\nBASE {nB} ({wB}%/{aB}%/PF{pB}) | Enhanced {nE} ({wE}%/{aE}%/PF{pE})")
    print("Report: backtest_report_PEAD_2022_2025_ENHANCED.md")
