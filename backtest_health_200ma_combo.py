"""
Signal-health + SPY>200MA combo test.

Question: does combining the realized-health gate with a SPY>200MA regime filter
fix the regime-TURN lag (over-blocking the recovering 2023) while keeping the
bull-and-weak detection (blocking 2026)?

Reuses the cached BASE population (backtest_signal_health_candidates.csv) — no
refetch. Health is recomputed point-in-time; the 200MA flag is added per entry.
"""

import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import pandas as pd
import numpy as np

import backtest_pead_2026_ytd as eng
from backtest_validate_filters_2022_2025 import robust_spy

EVAL_START = "2022-01-01"
P = eng.POSITION_SIZE
L_REAL = 60
MIN_N = 25


def stat(df, col="ret_sector"):
    if df.empty:
        return (0, None, None, None)
    wr = round((df[col] > 0).mean() * 100, 1)
    avg = round(df[col].mean(), 2)
    gw = (df[df[col] > 0][col] / 100 * P).sum()
    gl = abs((df[df[col] <= 0][col] / 100 * P).sum())
    pf = round(gw / gl, 2) if gl > 0 else float("inf")
    return (len(df), wr, avg, pf)


def health_realized(base, D, L=L_REAL):
    w = base[(base.exit_date < D) & (base.exit_date >= D - pd.Timedelta(days=L))]
    if len(w) < MIN_N:
        return None
    return float(w.ret_base.mean())


def main():
    base = pd.read_csv("backtest_signal_health_candidates.csv",
                       parse_dates=["entry_date", "exit_date", "ret5_known"])
    print("SPY 200MA...")
    spy_close, regime = eng.build_spy(robust_spy())
    assert spy_close.notna().sum() > 200

    def bull_at(d):
        try:
            return bool(regime.asof(pd.Timestamp(d).normalize()))
        except Exception:
            return None

    base["bull"] = base["entry_date"].map(bull_at)
    base["health_ok"] = base["entry_date"].map(
        lambda d: (lambda v: True if v is None else v >= 0)(health_realized(base, d)))

    enh = base[(base.enhanced) & (base.entry_date >= pd.Timestamp(EVAL_START))].copy()

    gates = {
        "Ungated":             pd.Series(True, index=enh.index),
        "Health ≥0":           enh.health_ok,
        "SPY>200MA":           enh.bull == True,
        "AND (health & 200MA)": enh.health_ok & (enh.bull == True),
        "OR (health | 200MA)":  enh.health_ok | (enh.bull == True),
    }

    L = []; A = L.append
    A("# PEAD Signal-Health × SPY>200MA Combo\n")
    A(f"*Window {EVAL_START}→2026-06-04. Gate applied to enhanced set. n / win% / avg% / PF. "
      "Realized-health = trailing-60d mean return of BASE trades already exited (point-in-time).*\n")

    A("## Aggregate\n")
    A("| Gate | Trades | Win% | Avg% | PF |")
    A("|------|-------:|-----:|-----:|---:|")
    for name, mask in gates.items():
        n, w, a, p = stat(enh[mask])
        A(f"| {name} | {n} | {w}% | {a}% | {p} |")
    A("")

    A("## Per-year (⛔ = hostile regime)\n")
    A("| Gate | 2022⛔ | 2023 | 2024 | 2025 | 2026⛔ |")
    A("|------|------|------|------|------|------|")
    def cell(sub):
        n, w, a, p = stat(sub)
        return f"{n}t {a if a is not None else '—'}%"
    for name, mask in gates.items():
        cells = []
        for y in [2022, 2023, 2024, 2025, 2026]:
            cells.append(cell(enh[mask & (enh.year == y)]))
        A(f"| {name} | " + " | ".join(cells) + " |")
    A("\n*Each cell = trades kept and their avg return. Compare against Ungated row.*\n")

    A("## The two failure modes — did the combo fix them?\n")
    A("| Gate | 2023 kept (lag victim) | 2023 avg% | 2026 blocked (detection) | 2026 avg% |")
    A("|------|----------------------:|----------:|-------------------------:|----------:|")
    full23 = len(enh[enh.year == 2023]); full26 = len(enh[enh.year == 2026])
    for name, mask in gates.items():
        s23 = enh[mask & (enh.year == 2023)]; s26 = enh[mask & (enh.year == 2026)]
        kept23 = len(s23)
        blk26 = (1 - len(s26) / full26) * 100 if full26 else 0
        a23 = stat(s23)[2]; a26 = stat(s26)[2]
        A(f"| {name} | {kept23}/{full23} ({kept23/full23*100:.0f}%) | "
          f"{a23 if a23 is not None else '—'}% | {blk26:.0f}% | {a26 if a26 is not None else '—'}% |")
    A("")

    A("## Regime discrimination\n")
    A("| Gate | Blocked hostile (22,26) | Blocked good (23-25) | Discrimination |")
    A("|------|------------------------:|---------------------:|---------------:|")
    hostile = enh[enh.year.isin([2022, 2026])]; good = enh[enh.year.isin([2023, 2024, 2025])]
    for name, mask in gates.items():
        if name == "Ungated":
            continue
        bh = (1 - mask[hostile.index].mean()) * 100
        bg = (1 - mask[good.index].mean()) * 100
        A(f"| {name} | {bh:.0f}% | {bg:.0f}% | {bh-bg:+.0f} pts |")
    A("")

    rep = "\n".join(L)
    with open("backtest_report_PEAD_HEALTH_200MA_COMBO.md", "w", encoding="utf-8") as f:
        f.write(rep)
    print("\n" + rep)
    print("\nSaved: backtest_report_PEAD_HEALTH_200MA_COMBO.md")


if __name__ == "__main__":
    main()
