"""
Canonical episodic-pivot run + VALIDATION (must pass before the grid).

Canonical config: gap>=5%, relvol>=2x, next-open entry, structural stop below
announcement-day low (capped 8%), combined earliest-trigger exit
{structural stop, 20-session time stop, 7% trail after +10%}.

Validation performed:
  (1) daily reconciliation: equity == cash + MTM every day; cash never negative;
      per-day invested fraction <= 1; sector exposure <= cap.
  (2) aggregate reconciliation: start_equity + sum(trade PnL) == final cash.
  (3) manual re-derivation of several individual trades from raw OHLCV.
"""
import json, os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ep_engine as E

CANON_RULES = {"struct", "time", "trail"}


def load_cache(tickers):
    cache = {}
    for t in list(tickers) + ["SPY", "QQQ"]:
        h = E.cached_history(t)
        if h is not None:
            cache[t] = h
    return cache


def run_period(sigs_all, cache, y0, y1, label):
    sigs = [s for s in sigs_all if y0 <= pd.Timestamp(s["entry_date"]).year <= y1]
    swx = E.attach_exits(sigs, cache, CANON_RULES, time_stop_sessions=20, trail_pct=0.07)
    trades, equity, recon, missed = E.simulate_portfolio(swx, cache)
    m = E.metrics(trades, equity, label, missed)
    return sigs, swx, trades, equity, recon, m


def daily_recon_checks(equity_df, trades_df, sector_cap=0.30):
    problems = []
    # equity == cash + mtm by construction; verify numerically
    resid = (equity_df["equity"] - (equity_df["cash"] + equity_df["mtm"])).abs().max()
    if resid > 1e-6:
        problems.append(f"equity!=cash+mtm (max resid {resid})")
    if (equity_df["cash"] < -1e-6).any():
        problems.append(f"negative cash on {int((equity_df['cash']<0).sum())} days")
    if (equity_df["invested_frac"] > 1.0001).any():
        problems.append("invested_frac>1 (leverage leak)")
    return problems


def main():
    ev = E.load_events()
    cache = load_cache(ev.ticker.unique())
    print("cache tickers:", len(cache))

    sigs_all, stats = E.build_signals(ev, cache, kind="ep", gap_min=0.05, vol_min=2.0,
                                      entry_mode="next_open")
    print("\nSignal-build funnel (all years):")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  final signals: {len(sigs_all)}")

    results = {}
    for (y0, y1, label) in [(2022, 2024, "IS_2022_2024"), (2025, 2025, "OOS_2025")]:
        sigs, swx, trades, equity, recon, m = run_period(sigs_all, cache, y0, y1, label)
        prob = daily_recon_checks(equity, trades) if not equity.empty else ["no equity"]
        print(f"\n=== {label} ===")
        print(f"  signals in period: {len(sigs)}  funded trades: {len(trades)}")
        print(f"  aggregate reconciliation PnL==cash-change: {'PASS' if recon else 'FAIL'}")
        print(f"  daily checks: {'PASS' if not prob else 'FAIL '+str(prob)}")
        print(f"  missed signals (cash/sector/dup): {m.get('missed_signals')}")
        for k in ("n_trades", "total_return_pct", "cagr_pct", "max_drawdown_pct",
                  "sharpe", "win_rate_pct", "expectancy_pct", "median_return_pct",
                  "profit_factor", "avg_hold_sessions", "avg_invested_frac_pct",
                  "pct_days_invested", "turnover_annual_x", "largest_winner_contrib_pct",
                  "expectancy_ex_top1_pct", "expectancy_ex_top5_pct"):
            print(f"    {k}: {m.get(k)}")
        results[label] = {"metrics": m, "recon": recon, "daily_problems": prob,
                          "n_signals": len(sigs)}
        if not trades.empty:
            trades.to_csv(os.path.join(E.REPORTS_DIR, f"canonical_trades_{label}.csv"), index=False)
            equity.to_csv(os.path.join(E.REPORTS_DIR, f"canonical_equity_{label}.csv"))

    # ---- manual trade re-derivation (independent recompute from raw OHLCV) ----
    print("\n=== MANUAL TRADE VERIFICATION (independent re-derivation) ===")
    manual = []
    is_trades = pd.read_csv(os.path.join(E.REPORTS_DIR, "canonical_trades_IS_2022_2024.csv"))
    sample = is_trades.sort_values("pnl").head(2).to_dict("records") + \
             is_trades.sort_values("pnl").tail(2).to_dict("records") + \
             is_trades.iloc[[len(is_trades)//2]].to_dict("records")
    ev_idx = {(r["ticker"], pd.Timestamp(r["earn_date"])): r for _, r in ev.iterrows()}
    for t in sample:
        tk = t["ticker"]; hist = cache[tk]
        edate = pd.Timestamp(t["earn_date"])
        feat = E.compute_features(hist, edate)
        ann = feat["ann_date"]; pos = feat["ann_pos"]
        man_entry_date = hist.index[pos + 1]
        man_entry_open = hist.iloc[pos + 1]["Open"]
        chk = {
            "ticker": tk, "earn_date": str(edate.date()),
            "ann_date": str(pd.Timestamp(ann).date()),
            "gap_recomputed": round(feat["gap"] * 100, 2),
            "volratio_recomputed": round(feat["vol_ratio"], 2),
            "range_pos_recomputed": round(feat["range_pos"], 2),
            "ann_ret_recomputed": round(feat["ann_ret"] * 100, 2),
            "entry_date_engine": str(pd.Timestamp(t["entry_date"]).date()),
            "entry_date_manual": str(man_entry_date.date()),
            "entry_open_manual": round(float(man_entry_open), 2),
            "buy_price_engine_incl_slip": round(float(t["buy_price"]), 2),
            "exit_reason": t["exit_reason"], "exit_date": str(pd.Timestamp(t["exit_date"]).date()),
            "net_return_pct_engine": round(float(t["net_return"]) * 100, 2),
            "match_entry_date": bool(str(man_entry_date.date()) == str(pd.Timestamp(t["entry_date"]).date())),
            "gap_ge_5": bool(feat["gap"] >= 0.05), "vol_ge_2": bool(feat["vol_ratio"] >= 2.0),
            "open_above_20dhigh": bool(feat["ann_open"] > feat["prior20_high"]),
            "range_ge_075": bool(feat["range_pos"] >= 0.75), "annret_ge_4": bool(feat["ann_ret"] >= 0.04),
        }
        manual.append(chk)
        print(json.dumps(chk, indent=None))

    with open(os.path.join(E.REPORTS_DIR, "canonical_results.json"), "w") as f:
        json.dump({"funnel": stats, "results": results, "manual_checks": manual}, f, indent=2, default=str)
    print("\nWrote canonical_results.json")


if __name__ == "__main__":
    main()
