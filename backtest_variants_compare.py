"""
Strategy-variant comparison — turns the improvement recommendations into numbers.

Builds the full BASE candidate set 2022-01-01 -> 2026-06-04 ONCE from the disk
cache (fast), then evaluates several rule variants over two periods:
  - 2022-2025 (large in/near-sample)
  - 2026 YTD  (hostile out-of-sample regime)

Variants tested:
  V0  Current enhanced stack          (surprise15 + vol + rs + 52w + nearearn; sector trail 12%IT/7%)
  V1  Drop the 52-wk-high filter
  V2  Revert IT trail to 7% (all sectors 7%)
  V3  Drop 52w  AND  all-7% trail
  V4  Current stack + bull-regime gate (only enter when SPY > 200MA)
"""

import os
import time
import sys
import pandas as pd
import numpy as np
from datetime import timedelta

import yfinance as yf
import backtest_pead_2026_ytd as eng
from backtest_validate_filters_2022_2025 import cached_fetch, robust_spy

eng.HIST_START = "2020-06-01"
eng.DATA_END   = "2026-06-05"          # include 2026 YTD through 2026-06-04
SCAN_START = "2022-01-01"
SCAN_END   = "2026-06-04"
P = eng.POSITION_SIZE


def build_candidates():
    sp500 = eng.get_sp500()
    tickers = sp500["ticker"].tolist()
    sector_map = dict(zip(sp500["ticker"], sp500["sector"]))
    print("SPY...")
    spy_close, regime = eng.build_spy(robust_spy())
    assert spy_close.notna().sum() > 200

    rows = []
    for idx, ticker in enumerate(tickers):
        if idx % 100 == 0:
            print(f"  {idx}/{len(tickers)} ({len(rows)} cand)...")
        hist, earnings = cached_fetch(ticker)
        if hist is None or earnings is None:
            continue
        td = eng.get_trading_days(hist)
        sector = sector_map.get(ticker, "Unknown")
        is_it = (sector == eng.IT_SECTOR)
        for ed, er in earnings.iterrows():
            ed = pd.Timestamp(ed).normalize()
            if ed < pd.Timestamp(SCAN_START) - timedelta(days=30) or ed > pd.Timestamp(SCAN_END):
                continue
            try:
                rep = float(er.get("reported", np.nan)); est = float(er.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(rep) or pd.isna(est) or not (rep > est):
                continue
            en = eng.nth_trading_day_after(td, ed, eng.ENTRY_DELAY)
            if en is None or en < pd.Timestamp(SCAN_START) or en > pd.Timestamp(SCAN_END):
                continue
            dd = hist[hist.index == en]
            if dd.empty:
                continue
            op = dd["Open"].iloc[0]
            if pd.isna(op) or op < eng.MIN_PRICE or not eng.avg_dvol_ok(hist, ed):
                continue
            r7 = eng.simulate_trade(hist, en, 0.07)
            r12 = eng.simulate_trade(hist, en, 0.12)
            if r7 is None or r12 is None:
                continue
            surprise = None
            if "surprise_pct" in er and not pd.isna(er["surprise_pct"]):
                surprise = float(er["surprise_pct"])
            elif est != 0:
                surprise = (rep - est) / abs(est) * 100
            vr = eng.vol_ratio_on_day(hist, ed)
            rs = eng.rel_strength_vs_spy(hist, spy_close, ed, en)
            hi = eng.new_52w_high_recent(hist, en)
            dn = eng.days_to_next_earnings(earnings, ed, en)
            rows.append({
                "ticker": ticker, "is_it": is_it, "year": en.year,
                "ret_sector": round((r12 if is_it else r7)["return_pct"] * 100, 2),  # 12%IT/7%other
                "ret_all7": round(r7["return_pct"] * 100, 2),
                "f_surprise15": (surprise is not None) and (surprise >= eng.SURPRISE_MIN),
                "f_vol15x": (vr is not None) and (vr >= eng.VOL_MULT),
                "f_rs": (rs is not None) and (rs > 0),
                "f_52w": (hi is True),
                "f_nearearn": (dn is None) or (dn > eng.NEAR_EARN_DAYS) or (dn < 0),
                "bull": eng.regime_at(regime, en),
            })
        time.sleep(0.0)
    return pd.DataFrame(rows)


def stat(df, retcol):
    if df.empty:
        return (0, None, None, None)
    n = len(df)
    wr = round((df[retcol] > 0).mean() * 100, 1)
    avg = round(df[retcol].mean(), 2)
    gw = (df[df[retcol] > 0][retcol] / 100 * P).sum()
    gl = abs((df[df[retcol] <= 0][retcol] / 100 * P).sum())
    pf = round(gw / gl, 2) if gl > 0 else float("inf")
    return (n, wr, avg, pf)


def variants(c):
    full = c.f_surprise15 & c.f_vol15x & c.f_rs & c.f_nearearn
    return {
        "V0 Current enhanced":        (c[full & c.f_52w], "ret_sector"),
        "V1 Drop 52-wk filter":       (c[full], "ret_sector"),
        "V2 IT trail 7% (revert)":    (c[full & c.f_52w], "ret_all7"),
        "V3 Drop 52w + 7% trail":     (c[full], "ret_all7"),
        "V4 + bull-regime gate":      (c[full & c.f_52w & (c.bull == True)], "ret_sector"),
    }


def main():
    c = build_candidates()
    print(f"\nTotal BASE candidates {SCAN_START}..{SCAN_END}: {len(c)}")
    c.to_csv("backtest_variants_candidates.csv", index=False)

    periods = {
        "2022-2025": c[c.year <= 2025],
        "2026 YTD":  c[c.year == 2026],
    }
    L = []; A = L.append
    A("# PEAD Strategy-Variant Comparison\n")
    A(f"*Window {SCAN_START}→{SCAN_END}. Each variant = a rule change applied to the same "
      "candidate set. Numbers are n / win% / avg% / profit factor.*\n")
    for pname, pdf in periods.items():
        A(f"## {pname}\n")
        A("| Variant | Trades | Win% | Avg% | PF |")
        A("|---------|-------:|-----:|-----:|---:|")
        for vname, (vdf, rc) in variants(pdf).items():
            n, w, a, p = stat(vdf, rc)
            A(f"| {vname} | {n} | {w if w is not None else '—'}% | "
              f"{a if a is not None else '—'}% | {p if p is not None else '—'} |")
        A("")
    A("**Read:** compare each Vn against V0 (current rules) within a period. A variant that "
      "raises avg% and PF without crushing trade count is an improvement.\n")
    report = "\n".join(L)
    with open("backtest_report_PEAD_VARIANTS.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n" + report)
    print("\nSaved: backtest_report_PEAD_VARIANTS.md, backtest_variants_candidates.csv")


if __name__ == "__main__":
    main()
