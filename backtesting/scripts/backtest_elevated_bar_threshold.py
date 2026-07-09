"""
backtest_elevated_bar_threshold.py — ELEVATED_BAR health-threshold comparison (S1).

RESEARCH / DIAGNOSTIC ONLY. Does not edit strategy.md, places no orders, not part of
the live 7-routine system. Reconstructs everything from committed repo CSVs (no network).

What it tests
-------------
The live PEAD signal-health overlay flips posture NORMAL -> ELEVATED_BAR when the
trailing-60-calendar-day realized health metric < HEALTH_THRESHOLD (live = 0.0). This
script re-derives that metric from committed data and sweeps the threshold over
{0.0, -0.5, -1.0, -1.5}, reporting per-threshold posture frequency and the trade-level
retained-vs-blocked outcomes of the EPS-bar gate (surprise >=15 under NORMAL vs >=20
under ELEVATED_BAR).

Key facts read from the live code (compute_pead_health.py + backtest_pead_2026_ytd.py)
--------------------------------------------------------------------------------------
* The realized-health metric is MARKET-WIDE (mean outcome of ALL S&P 500 EPS-beat base
  trades that exited in the trailing 60 calendar days), computed independently of the
  portfolio. It is therefore ONE series shared across thresholds; a blocked trade does
  NOT change future health. Only the position caps create true path-dependence, and that
  dimension is not reconstructible (needs the unbacktestable conviction score).
* Per-trade return basis = simulate_trade(entry, 0.07): -8% hard stop / +10% trigger ->
  7% trailing stop / 42-cal-day time stop (no 1/3 scale-out — the live metric omits it).
  In signal_health_candidates.csv this is column `ret_base`; in the *_ENHANCED_base.csv
  candidate stream it is `ret_trail7`.

Availability gate (see report §2)
---------------------------------
* Health series / posture: reconstructable 2022 -> 2026-06-04.
* EPS-bar retained/blocked trade counterfactual: reconstructable 2022-2025 (base stream
  has surprise_pct + sector). NOT for 2026 (base population absent) and NOT for the
  position-cap dimension. True portfolio CAGR / daily-MTM Sharpe / maxDD are NOT
  reconstructible and are deliberately NOT produced here.

Outputs (backtesting/reports/, memory/)
---------------------------------------
* backtest_elevated_bar_health_series_2026-07-08.csv  (daily health + posture per threshold)
* backtest_elevated_bar_swing_2026-07-08.csv           (the enhanced trades ELEVATED can block)
* prints the tables that populate memory/backtest_elevated_bar_threshold_2026-07-08.md
"""
import os
import json
import numpy as np
import pandas as pd

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_BT_DIR = os.path.dirname(_SCRIPT_DIR)
_REPO = os.path.dirname(_BT_DIR)
RPTS = os.path.join(_BT_DIR, "reports")

MIN_SAMPLE = 20                        # compute_pead_health.py:46
WINDOW = 60                            # calendar days, keyed on EXIT date
THRESHOLDS = [0.0, -0.5, -1.0, -1.5]
DEPRIO = {"Utilities", "Real Estate", "Industrials", "Energy"}
RUN_DATE = "2026-07-08"

# ── health population (broad base EPS-beat pop, 2021-2026) ────────────────────
H = pd.read_csv(os.path.join(RPTS, "backtest_signal_health_candidates.csv"),
                parse_dates=["entry_date", "exit_date"])
DATA_END = H.exit_date.max()


def health_at(D):
    D = pd.Timestamp(D)
    w = H[(H.exit_date >= D - pd.Timedelta(days=WINDOW)) & (H.exit_date <= D)]
    n = len(w)
    return (float(w.ret_base.mean()) if n >= MIN_SAMPLE else None), n


def posture(hv, thr):
    if hv is None:
        return "NORMAL"                # fail-open on thin data
    return "ELEVATED_BAR" if hv < thr else "NORMAL"


def stats(x):
    x = pd.Series(x).dropna()
    n = len(x)
    if n == 0:
        return {"n": 0, "win": None, "avg": None, "med": None, "pf": None}
    gw = x[x > 0].sum(); gl = -x[x <= 0].sum()
    return {"n": int(n), "win": round((x > 0).mean() * 100, 1),
            "avg": round(x.mean(), 3), "med": round(x.median(), 3),
            "pf": (round(gw / gl, 3) if gl > 0 else float("inf"))}


def main():
    out = {"data_end": str(DATA_END.date())}

    # daily health + posture series over business days
    cal = pd.bdate_range("2022-01-03", DATA_END)
    ser = pd.DataFrame({"date": cal})
    ser["hv"], ser["n"] = zip(*[health_at(d) for d in cal])
    ser["period"] = np.where(ser.date.dt.year <= 2024, "IS (2022-2024)",
                     np.where(ser.date.dt.year == 2025, "OOS (2025)", "2026 (partial)"))
    for t in THRESHOLDS:
        ser[f"post_{t}"] = [posture(v, t) for v in ser.hv]

    # posture timeline
    tl = {}
    for per in ["IS (2022-2024)", "OOS (2025)", "2026 (partial)", "ALL"]:
        sub = ser if per == "ALL" else ser[ser.period == per]
        tl[per] = {"days": int(len(sub)),
                   **{f"@{t}": round((sub[f"post_{t}"] == "ELEVATED_BAR").mean() * 100, 1)
                      for t in THRESHOLDS}}
    out["posture_timeline"] = tl

    # tradeable candidates -> EPS-bar admit/block per threshold
    b = pd.read_csv(os.path.join(RPTS, "backtest_trades_PEAD_2022_2025_ENHANCED_base.csv"),
                    parse_dates=["entry_date"])
    b["q"] = b.f_vol15x.astype(int) + b.f_rs.astype(int) + b.f_52w.astype(int)
    b["deprio"] = b.sector.isin(DEPRIO)
    b["hv"] = [health_at(d)[0] for d in b.entry_date]
    b["period"] = np.where(b.entry_date.dt.year <= 2024, "IS (2022-2024)", "OOS (2025)")
    b["ret"] = b.ret_trail7
    b["n_ok"] = (b.q == 3) & b.f_nearearn & (
        (~b.deprio & (b.surprise_pct >= 15)) | (b.deprio & (b.surprise_pct >= 20)))
    b["e_ok"] = (b.q == 3) & b.f_nearearn & (b.surprise_pct >= 20)

    grid = {}
    for per in ["IS (2022-2024)", "OOS (2025)", "ALL"]:
        sub = b if per == "ALL" else b[b.period == per]
        adm, blk = {}, {}
        for t in THRESHOLDS:
            ed = sub.hv.notna() & (sub.hv < t)
            adm[str(t)] = stats(sub[(sub.n_ok & ~ed) | (sub.e_ok & ed)].ret)
            blk[str(t)] = stats(sub[sub.n_ok & ed & ~sub.e_ok].ret)
        grid[per] = {"admitted": adm, "blocked": blk}
    out["enhanced_grid"] = grid

    # swing universe (enhanced) + save artifacts
    sw = b[b.n_ok & ~b.e_ok & ~b.deprio][
        ["ticker", "sector", "entry_date", "surprise_pct", "q", "hv", "ret",
         "exit_reason", "period"]].sort_values("entry_date")
    sw.to_csv(os.path.join(RPTS, f"backtest_elevated_bar_swing_{RUN_DATE}.csv"), index=False)
    ser.to_csv(os.path.join(RPTS, f"backtest_elevated_bar_health_series_{RUN_DATE}.csv"), index=False)
    out["swing_enhanced_n"] = int(len(sw))

    # Step-7 reconciliation vs the 3 live logged readings
    live = [("2026-06-05", -2.08, 211), ("2026-06-14", -1.025, 282), ("2026-06-21", -0.492, 367)]
    out["reconcile"] = [{"date": d, "live": lv, "live_n": ln,
                         "recon": round(health_at(d)[0], 3), "recon_n": health_at(d)[1]}
                        for d, lv, ln in live]

    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
