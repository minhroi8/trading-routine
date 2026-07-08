"""
Full episodic-pivot matrix + comparisons (runs AFTER canonical validation passed).
Everything is survivorship-biased relative comparison — NOT absolute strategy evidence.

Produces (into reports/):
  grid_results.csv            54-cell parameter grid, IS & OOS, with denominators
  isolated_exits.csv          each exit rule alone vs combined (canonical filter)
  comparisons.json            SPY, PEAD(from artifacts), simple-gap, random control
  overlap.json                EP vs PEAD: shared tickers/events/concurrent/monthly-corr
"""
import os, sys, json, itertools, random
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ep_engine as E

CANON_RULES = {"struct", "time", "trail"}


def load_cache(tickers):
    return {t: E.cached_history(t) for t in list(tickers) + ["SPY", "QQQ"]
            if E.cached_history(t) is not None}


def precompute_feats(ev, cache):
    """event row + features (computed once)."""
    pool = []
    for _, e in ev.iterrows():
        h = cache.get(e["ticker"])
        if h is None:
            continue
        f = E.compute_features(h, e["earn_date"])
        if f is None or pd.isna(f["vol_ratio"]):
            continue
        pool.append((e.to_dict(), f))
    return pool


def signals_from_pool(pool, cache, kind, gap, vol, entry_mode, bw=5, max_stop=0.08):
    sigs = []
    nxt = {}
    for (e, _) in pool:
        nxt.setdefault(e["ticker"], []).append(pd.Timestamp(e["earn_date"]))
    for tk in nxt:
        nxt[tk] = sorted(nxt[tk])
    for (e, f) in pool:
        s = e["surprise_pct"]
        if kind == "ep":
            ok = (s >= 15 and f["gap"] >= gap and f["ann_open"] > f["prior20_high"]
                  and f["vol_ratio"] >= vol and f["range_pos"] >= 0.75 and f["ann_ret"] >= 0.04)
        else:  # simple gap+vol only
            ok = (f["gap"] >= gap and f["vol_ratio"] >= vol)
        if not ok:
            continue
        hist = cache[e["ticker"]]
        ed, fill = E.decide_entry(hist, f, entry_mode, bw)
        if ed is None or fill is None or fill < E.MIN_PRICE:
            continue
        stop = f["ann_low"]
        if (fill - stop) / fill > max_stop:
            continue
        fut = [d for d in nxt[e["ticker"]] if d > pd.Timestamp(e["earn_date"])]
        sigs.append({"ticker": e["ticker"], "sector": e["sector"],
                     "earn_date": pd.Timestamp(e["earn_date"]), "surprise_pct": s,
                     "entry_date": ed, "entry_fill_raw": float(fill),
                     "stop_price": float(stop), "next_earn": (min(fut) if fut else None),
                     "gap": f["gap"], "vol_ratio": f["vol_ratio"],
                     "range_pos": f["range_pos"], "ann_ret": f["ann_ret"],
                     "year": int(pd.Timestamp(ed).year)})
    return sigs


def run_cell(pool, cache, kind, gap, vol, entry_mode, maxhold, rules, y0, y1, label):
    sigs = [s for s in signals_from_pool(pool, cache, kind, gap, vol, entry_mode)
            if y0 <= pd.Timestamp(s["entry_date"]).year <= y1]
    swx = E.attach_exits(sigs, cache, rules, time_stop_sessions=maxhold, trail_pct=0.07)
    tr, eq, recon, missed = E.simulate_portfolio(swx, cache)
    m = E.metrics(tr, eq, label, missed)
    m["recon_ok"] = recon
    return m, tr, eq


def spy_benchmark(cache, start, end):
    spy = cache["SPY"]["Close"]
    s = spy[(spy.index >= pd.Timestamp(start)) & (spy.index <= pd.Timestamp(end))]
    ret = s.iloc[-1] / s.iloc[0] - 1
    days = (s.index[-1] - s.index[0]).days or 1
    cagr = (s.iloc[-1] / s.iloc[0]) ** (365 / days) - 1
    dret = s.pct_change().dropna()
    mdd = ((s - s.cummax()) / s.cummax()).min()
    return {"total_return_pct": ret * 100, "cagr_pct": cagr * 100,
            "max_drawdown_pct": mdd * 100,
            "sharpe": (dret.mean() / dret.std() * np.sqrt(252)) if dret.std() > 0 else None}


def pead_from_artifacts(y0, y1):
    """PEAD realized trade stats, re-pulled from artifacts (NOT re-simulated)."""
    t = E.load_pead_trades()
    t = t[(t["year"] >= y0) & (t["year"] <= y1)]
    r = t["return_pct"].dropna().values     # already in PERCENT units in the artifact
    wins = r[r > 0]; losses = r[r < 0]
    return {"n_trades": int(len(r)), "win_rate_pct": float((r > 0).mean() * 100),
            "expectancy_pct": float(r.mean()), "median_return_pct": float(np.median(r)),
            "profit_factor": float(wins.sum() / abs(losses.sum())) if losses.sum() != 0 else None,
            "note": "trade-level, PEAD's own sizing/exits (~42-cal-day hold); not portfolio-CAGR comparable"}


def random_control(canon_trades, pool, cache, rules, maxhold, seeds=(1, 2, 3, 4, 5), window=10):
    """For each EP trade, sample same-sector beat events within +/-`window` calendar
    days, simulate next-open entry + same exits. Mean return across picks/seeds."""
    by_sector = {}
    for (e, f) in pool:
        by_sector.setdefault(e["sector"], []).append((e, f))
    rets = []
    n_used = 0
    for _, tr in canon_trades.iterrows():
        cands = []
        for (e, f) in by_sector.get(tr["sector"], []):
            if e["ticker"] == tr["ticker"]:
                continue
            if abs((pd.Timestamp(e["earn_date"]) - pd.Timestamp(tr["earn_date"])).days) <= window:
                cands.append((e, f))
        if not cands:
            continue
        n_used += 1
        for seed in seeds:
            random.seed(seed * 1000 + hash(tr["ticker"]) % 1000)
            e, f = random.choice(cands)
            hist = cache[e["ticker"]]
            ed, fill = E.decide_entry(hist, f, "next_open")
            if ed is None or fill is None or fill < E.MIN_PRICE:
                continue
            ex = E.simulate_exit(hist, ed, fill, f["ann_low"], None, rules,
                                 time_stop_sessions=maxhold, trail_pct=0.07)
            if ex:
                rets.append(ex["raw_return"])
    rets = np.array(rets)
    return {"n_ep_trades_matched": n_used, "n_random_samples": int(len(rets)),
            "mean_return_pct": float(rets.mean() * 100) if len(rets) else None,
            "median_return_pct": float(np.median(rets) * 100) if len(rets) else None,
            "win_rate_pct": float((rets > 0).mean() * 100) if len(rets) else None}


def overlap_vs_pead(canon_trades):
    pead = E.load_pead_trades()
    ep_tk = set(canon_trades["ticker"]); pead_tk = set(pead["ticker"])
    ep_ev = set(zip(canon_trades["ticker"], canon_trades["earn_date"].astype(str)))
    pead_ev = set(zip(pead["ticker"], pead["earn_date"].astype(str)))
    # concurrent exposure: EP holding-days overlapping a PEAD position in same ticker
    pead_by_tk = {}
    for _, r in pead.iterrows():
        pead_by_tk.setdefault(r["ticker"], []).append((r["entry_date"], r["exit_date"]))
    conc_days = tot_days = 0
    for _, tr in canon_trades.iterrows():
        span = pd.bdate_range(tr["entry_date"], tr["exit_date"])
        tot_days += len(span)
        for (pe, px) in pead_by_tk.get(tr["ticker"], []):
            conc_days += int(((span >= pe) & (span <= px)).sum())
    # monthly realized-PnL correlation (best-effort; labeled)
    ep_m = canon_trades.assign(m=pd.to_datetime(canon_trades["exit_date"]).dt.to_period("M")
                               ).groupby("m")["pnl"].sum()
    pe = pead.dropna(subset=["exit_date"]).copy()
    pe["m"] = pd.to_datetime(pe["exit_date"]).dt.to_period("M")
    pe_m = pe.groupby("m")["return_dollar"].sum() if "return_dollar" in pe else None
    corr = None
    if pe_m is not None:
        j = pd.concat([ep_m.rename("ep"), pe_m.rename("pead")], axis=1).dropna()
        if len(j) >= 4:
            corr = float(j["ep"].corr(j["pead"]))
    return {
        "ep_tickers": len(ep_tk), "shared_tickers": len(ep_tk & pead_tk),
        "shared_tickers_pct_of_ep": round(100 * len(ep_tk & pead_tk) / max(1, len(ep_tk)), 1),
        "ep_events": len(ep_ev), "shared_events": len(ep_ev & pead_ev),
        "shared_events_pct_of_ep": round(100 * len(ep_ev & pead_ev) / max(1, len(ep_ev)), 1),
        "ep_holding_bdays": int(tot_days), "concurrent_bdays_same_ticker": int(conc_days),
        "concurrent_pct_of_ep_holding": round(100 * conc_days / max(1, tot_days), 1),
        "monthly_realized_pnl_corr": corr,
        "monthly_corr_note": ("realized-PnL-by-exit-month proxy only; true daily MTM "
                              "return correlation is NOT computable from PEAD trade-level artifacts"),
        "n_monthly_points": (0 if corr is None else int(len(j))),
    }


def main():
    ev = E.load_events()
    cache = load_cache(ev.ticker.unique())
    pool = precompute_feats(ev, cache)
    print("feature pool:", len(pool))
    periods = [(2022, 2024, "IS_2022_2024"), (2025, 2025, "OOS_2025")]

    # ---------- GRID ----------
    grid_rows = []
    for gap, vol, em, mh in itertools.product([0.05, 0.08, 0.10], [1.5, 2.0, 3.0],
                                              ["next_open", "breakout"], [10, 20, 30]):
        for (y0, y1, lab) in periods:
            m, _, _ = run_cell(pool, cache, "ep", gap, vol, em, mh, CANON_RULES, y0, y1, lab)
            grid_rows.append({"gap": gap, "vol": vol, "entry": em, "maxhold": mh,
                              "period": lab, **{k: m.get(k) for k in
                              ("n_trades", "total_return_pct", "cagr_pct", "max_drawdown_pct",
                               "sharpe", "win_rate_pct", "expectancy_pct", "median_return_pct",
                               "profit_factor", "largest_winner_contrib_pct",
                               "expectancy_ex_top1_pct", "avg_invested_frac_pct", "recon_ok")}})
    gdf = pd.DataFrame(grid_rows)
    gdf.to_csv(os.path.join(E.REPORTS_DIR, "grid_results.csv"), index=False)
    print("grid cells:", len(gdf), "-> grid_results.csv")

    # ---------- ISOLATED EXITS (canonical filter gap5/vol2/next_open) ----------
    iso_rows = []
    exit_sets = {"hard_only": {"hard"}, "time_only": {"time"}, "trail_only": {"trail"},
                 "earn_only": {"earn"}, "combined_canonical": CANON_RULES}
    for name, rules in exit_sets.items():
        for (y0, y1, lab) in periods:
            m, _, _ = run_cell(pool, cache, "ep", 0.05, 2.0, "next_open", 20, rules, y0, y1, lab)
            iso_rows.append({"exit": name, "period": lab, **{k: m.get(k) for k in
                             ("n_trades", "total_return_pct", "win_rate_pct", "expectancy_pct",
                              "median_return_pct", "profit_factor", "max_drawdown_pct",
                              "largest_winner_contrib_pct")}})
    pd.DataFrame(iso_rows).to_csv(os.path.join(E.REPORTS_DIR, "isolated_exits.csv"), index=False)
    print("isolated-exit rows:", len(iso_rows), "-> isolated_exits.csv")

    # ---------- COMPARISONS (canonical config) ----------
    comparisons = {}
    for (y0, y1, lab) in periods:
        m, tr, eq = run_cell(pool, cache, "ep", 0.05, 2.0, "next_open", 20, CANON_RULES, y0, y1, lab)
        sm, ts, es = run_cell(pool, cache, "simple", 0.05, 2.0, "next_open", 20, CANON_RULES, y0, y1, lab)
        start = eq.index[0] if not eq.empty else f"{y0}-01-01"
        end = eq.index[-1] if not eq.empty else f"{y1}-12-31"
        comparisons[lab] = {
            "episodic_pivot": {k: m.get(k) for k in
                ("n_trades", "total_return_pct", "cagr_pct", "max_drawdown_pct", "sharpe",
                 "win_rate_pct", "expectancy_pct", "median_return_pct", "profit_factor",
                 "avg_invested_frac_pct", "pct_days_invested", "turnover_annual_x",
                 "slippage_cost_$", "largest_winner_contrib_pct", "top5_winner_contrib_pct",
                 "expectancy_ex_top1_pct", "expectancy_ex_top5_pct")},
            "spy_buyhold": spy_benchmark(cache, start, end),
            "pead_from_artifacts": pead_from_artifacts(y0, y1),
            "simple_gap_baseline": {k: sm.get(k) for k in
                ("n_trades", "total_return_pct", "win_rate_pct", "expectancy_pct",
                 "median_return_pct", "profit_factor", "largest_winner_contrib_pct")},
            "random_matched_control": random_control(tr, pool, cache, CANON_RULES, 20)
                if not tr.empty else {"note": "no EP trades"},
        }
        if lab == "OOS_2025" and not tr.empty:
            overlap = overlap_vs_pead(tr)
    # overlap on full-period canonical trades (IS+OOS combined for a fuller picture)
    m_all, tr_all, _ = run_cell(pool, cache, "ep", 0.05, 2.0, "next_open", 20, CANON_RULES,
                                2022, 2025, "ALL")
    overlap_all = overlap_vs_pead(tr_all) if not tr_all.empty else {}
    with open(os.path.join(E.REPORTS_DIR, "comparisons.json"), "w") as f:
        json.dump(comparisons, f, indent=2, default=str)
    with open(os.path.join(E.REPORTS_DIR, "overlap.json"), "w") as f:
        json.dump(overlap_all, f, indent=2, default=str)
    print("wrote comparisons.json, overlap.json")
    print("\nOVERLAP (all canonical trades):", json.dumps(overlap_all, indent=2, default=str))


if __name__ == "__main__":
    main()
