"""
PEAD portfolio-level backtest: a real daily equity curve vs SPY and 60/40, and
do the live-bar filters earn their keep?

Research only. Does not modify memory/strategy.md, places no orders, touches no
live routine. Definitions, arms, questions and the engine are pre-registered in
pead_portfolio_prereg.py (committed before the first full run).

Usage (from anywhere):
    python3 backtesting/scripts/backtest_pead_portfolio_sim.py
    python3 backtesting/scripts/check_pead_portfolio_report.py \
        backtesting/pead_portfolio_sim_<date>.md \
        backtesting/reports/pead_portfolio_claims_<date>.json

Data: the committed candidate sets (reports/backtest_trades_PEAD_2022_2025_
ENHANCED_base.csv and reports/backtest_trades_PEAD_2026_YTD.csv) and daily
adjusted OHLC from the repo's requests + Yahoo chart transport
(backtest_risk_sweep_entry_stop._fetch_chart / cached_history).
Matched-random pools follow backtest_pead_vs_random_control.py (branch
claude/project-thread-bpcb4z): same day, same sector, same 20d $-volume
quintile, no committed earnings report in [D-10, D+5], widening to +/-1
quintile then sector-only when fewer than 5 names match.
"""

import json
import os
import subprocess
import sys
from datetime import datetime

import numpy as np
import pandas as pd

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)

import backtest_risk_sweep_entry_stop as rs  # noqa: E402
import pead_portfolio_prereg as P  # noqa: E402

RUN_DATE = "2026-10-15"
BT_DIR = os.path.dirname(_SCRIPT_DIR)
REPO = os.path.dirname(BT_DIR)
REPORTS = os.path.join(BT_DIR, "reports")
REPORT_MD = os.path.join(BT_DIR, f"pead_portfolio_sim_{RUN_DATE}.md")
CLAIMS = os.path.join(REPORTS, f"pead_portfolio_claims_{RUN_DATE}.json")
REJECTS_CSV = os.path.join(REPORTS, f"pead_portfolio_rejects_{RUN_DATE}.csv")
TRADES_CSV = os.path.join(REPORTS, f"pead_portfolio_trades_{RUN_DATE}.csv")
GRID_CSV = os.path.join(REPORTS, f"pead_portfolio_grid_{RUN_DATE}.csv")
POSTURE_CSV = os.path.join(REPORTS, f"pead_portfolio_posture_{RUN_DATE}.csv")
RANDOM_CSV = os.path.join(REPORTS, f"pead_portfolio_random_{RUN_DATE}.csv")

ANCHOR_DATA_END = "2026-07-08"     # the risk sweep's fetch end (2026 trades truncate here)
DVOL_WINDOW = 20
N_BUCKETS = 5
MIN_POOL = 5
EXCL_BEFORE, EXCL_AFTER = 10, 5
REASONS = ["slots_full", "weekly_cap", "sector_cap", "cash_floor", "already_held"]

rs._P2 = int(pd.Timestamp(RUN_DATE).timestamp())   # bars through the prior session
rs.MIN_PRICE = 0.0   # the $10 gate is applied explicitly on the UNADJUSTED open


def raw_open(ticker):
    """Unadjusted (no dividend or split adjustment) daily open, same chart endpoint (cached)."""
    path = os.path.join(rs.CACHE_DIR, "rawopen_" + ticker.replace("/", "_") + ".pkl")
    if os.path.exists(path):
        return pd.read_pickle(path)
    sym = ticker.replace(".", "-")
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        url = (f"https://{host}/v8/finance/chart/{sym}?period1={rs._P1}&period2={rs._P2}"
               f"&interval=1d&events=div%2Csplits")
        for attempt in range(4):
            try:
                r = rs._rq.get(url, timeout=30, headers={"User-Agent": rs._UA})
                if r.status_code == 429:
                    rs.time.sleep(3 * (attempt + 1)); continue
                if r.status_code != 200:
                    break
                res = r.json()["chart"]["result"][0]
                idx = (pd.to_datetime(res["timestamp"], unit="s", utc=True)
                       .tz_convert("America/New_York").normalize().tz_localize(None))
                ser = pd.Series(res["indicators"]["quote"][0]["open"], index=idx, dtype=float)
                ser = ser[~ser.index.duplicated()]
                # Yahoo's quote series is split-adjusted; undo splits to get the price
                # actually traded on each day.
                for sp in (res.get("events") or {}).get("splits", {}).values():
                    d = (pd.to_datetime(sp["date"], unit="s", utc=True)
                         .tz_convert("America/New_York").normalize().tz_localize(None))
                    ser[ser.index < d] *= sp["numerator"] / sp["denominator"]
                ser.to_pickle(path)
                return ser
            except Exception:
                rs.time.sleep(2 * (attempt + 1))
    return None


# ─── report builder: every prose number is cited from a table ────────────────
class Report:
    def __init__(self):
        self.lines, self.claims, self.tables, self._refs = [], [], {}, []

    def w(self, s=""):
        assert not self._refs, "cited values must go through p()"
        self.lines.append(s)

    def table(self, tid, hdr, rows):
        rows = [[str(x).replace("|", "/") for x in r] for r in rows]
        hdr = [str(h).replace("|", "/") for h in hdr]
        keys = [r[0] for r in rows]
        assert len(keys) == len(set(keys)), f"duplicate row keys in {tid}"
        self.tables[tid] = (hdr, rows)
        self.lines.append(f"<!-- table:{tid} -->")
        self.lines.append("| " + " | ".join(hdr) + " |")
        self.lines.append("|" + "|".join("---" for _ in hdr) + "|")
        for r in rows:
            self.lines.append("| " + " | ".join(r) + " |")
        self.lines.append("")

    def c(self, tid, row, col):
        hdr, rows = self.tables[tid]
        v = [r for r in rows if r[0] == row][0][hdr.index(col)]
        self._refs.append(dict(table=tid, row=row, col=col, value=v))
        return v

    def p(self, s):
        self.lines.append(s)
        if self._refs:
            self.claims.append(dict(line=s, refs=self._refs))
        self._refs = []


def pct(x, d=1):
    return "n/a" if x is None or not np.isfinite(x) else f"{x * 100:.{d}f}%"


def f2(x):
    return "n/a" if x is None or not np.isfinite(x) else f"{x:.2f}"


def yn(b):
    return "yes" if b else "no"


# ─── data ─────────────────────────────────────────────────────────────────────
def load_candidates():
    a = pd.read_csv(rs.CAND_2022_2025)
    b = pd.read_csv(rs.CAND_2026)
    a["src"], b["src"] = "base", "live2026"
    cols = ["ticker", "sector", "earn_date", "entry_date", "surprise_pct",
            "f_vol15x", "f_rs", "f_52w", "f_nearearn", "src"]
    c = pd.concat([a[cols], b[cols]], ignore_index=True)
    for f in ["f_vol15x", "f_rs", "f_52w", "f_nearearn"]:
        c[f] = c[f].astype(bool)
    c["q"] = c.f_vol15x.astype(int) + c.f_rs.astype(int) + c.f_52w.astype(int)
    c["entry_date"] = pd.to_datetime(c.entry_date).values.astype("datetime64[D]")
    c["earn_date"] = pd.to_datetime(c.earn_date).values.astype("datetime64[D]")
    c["period"] = None
    for lab, (s, e) in P.PERIODS.items():
        m = (c.entry_date >= np.datetime64(s)) & (c.entry_date <= np.datetime64(e))
        c.loc[m, "period"] = lab
    c["cid"] = np.arange(len(c))
    # Rank: EPS surprise descending (pre-registered); ties by ticker in the engine.
    c["rank"] = (-c.surprise_pct).rank(method="first").astype(int)
    return c


def fetch_all(tickers):
    hists, missing = {}, []
    for n, t in enumerate(tickers):
        if n % 100 == 0:
            print(f"  fetch {n}/{len(tickers)}", flush=True)
        h = rs.cached_history(t)
        if h is None:
            missing.append(t)
            continue
        h = h[h.index < pd.Timestamp(RUN_DATE)].copy()
        if t != "^IRX":
            ro = raw_open(t)
            if ro is None:
                missing.append(t)
                continue
            h["RawOpen"] = ro.reindex(h.index)
        hists[t] = h
    return hists, missing


# ─── matched random pools (port of the PEAD-vs-random control helper) ─────────
def dvol20(panel):
    dv = np.nan_to_num(panel.close * panel.vol)
    cs = np.vstack([np.zeros(dv.shape[1]), np.cumsum(dv, 0)])
    out = np.full(dv.shape, np.nan)
    out[DVOL_WINDOW:] = (cs[DVOL_WINDOW:-1] - cs[:-DVOL_WINDOW - 1]) / DVOL_WINDOW
    return out


def build_matches(panel, cands, sector_of, earn_by):
    """For each candidate row: array of matched random tickers."""
    dv = dvol20(panel)
    stock_ks = [panel.col[t] for t in panel.tickers if t in sector_of]
    out, levels = {}, {}
    for d, grp in cands.groupby("entry_date"):
        d = np.datetime64(d, "D")
        i = panel.pos.get(d)
        if i is None:
            continue
        rows = []
        for k in stock_ks:
            t = panel.tickers[k]
            o = panel.open[i, k]
            if not (o >= 0) or not (panel.raw_open[i, k] >= P.MIN_PRICE) or not (dv[i, k] >= rs_min_dvol()):
                continue
            ed = earn_by.get(t)
            if ed is not None:
                lo, hi = d - np.timedelta64(EXCL_BEFORE, "D"), d + np.timedelta64(EXCL_AFTER, "D")
                j = np.searchsorted(ed, lo)
                if j < len(ed) and ed[j] <= hi:
                    continue
            rows.append((t, sector_of[t], dv[i, k]))
        if not rows:
            continue
        pool = pd.DataFrame(rows, columns=["ticker", "sector", "dvol"])
        pool["bucket"] = pd.qcut(pool.dvol.rank(method="first"), N_BUCKETS, labels=False)
        edges = np.sort(pool.dvol.to_numpy())
        for r in grp.itertuples():
            k = panel.col.get(r.ticker)
            v = dv[i, k] if k is not None else np.nan
            b = (min(int(np.searchsorted(edges, v) / len(edges) * N_BUCKETS), N_BUCKETS - 1)
                 if np.isfinite(v) else None)
            sec = pool[(pool.sector == r.sector) & (pool.ticker != r.ticker)]
            lvl, m = "sector+size", sec[sec.bucket == b] if b is not None else sec.iloc[0:0]
            if len(m) < MIN_POOL and b is not None:
                lvl, m = "sector+size+-1", sec[(sec.bucket - b).abs() <= 1]
            if len(m) < MIN_POOL:
                lvl, m = "sector only", sec
            if len(m):
                out[r.cid] = m.ticker.to_numpy()
                levels[r.cid] = lvl
    return out, levels


def rs_min_dvol():
    return 20_000_000.0


# ─── gate 0 ───────────────────────────────────────────────────────────────────
def anchor_stats(rets):
    r = np.asarray(rets, float)
    gw, gl = r[r > 0].sum(), -r[r <= 0].sum()
    return dict(n=len(r), win=(r > 0).mean() * 100, avg=r.mean(), pf=gw / gl if gl > 0 else np.inf)


def gate0(R, cands, hists, panel, bill, irx_raw):
    ok_all = True
    R.w("## Gate 0 — data and validation anchor")
    R.w("")
    # 1. live control ticker through the repo transport
    R.w("### Item 1 — live control ticker through the repo's requests + Yahoo chart transport")
    R.w("")
    try:
        a = rs._fetch_chart("AAPL")
        err = None
    except Exception as e:  # transport error, not a data finding
        a, err = None, repr(e)
    if a is None:
        R.w(f"**GATE 0 STOPPED — transport failure fetching AAPL (not a data finding):** `{err}`")
        return False, {}
    last = a.index[-1].date()
    g1 = len(a) > 1000 and (pd.Timestamp(RUN_DATE) - a.index[-1]).days <= 5
    R.table("g0_aapl", ["Check", "Value", "Pass rule", "Result"], [
        ["AAPL bars fetched", str(len(a)), "> 1000", "PASS" if len(a) > 1000 else "FAIL"],
        ["AAPL last bar", str(last), "within 5 days of run date", "PASS" if g1 else "FAIL"],
        ["Tickers with no history", str(len(cands.ticker.unique()) - sum(t in hists for t in cands.ticker.unique())),
         "reported", "INFO"],
    ])
    ok_all &= g1

    # 2. validation anchor (risk-sweep baseline, exact simulate(), sweep's data end)
    R.w("### Item 2 — validation anchor (per-trade baseline: EPS>=15%, vol>=1.5x, RS>0, 52wk-high<=45d, flat -8%)")
    R.w("")
    R.w("The $10 entry gate is applied to the unadjusted open (pre-registration amended after "
        "the first Gate 0 stop; see the record at the end). A period passes when every "
        "committed baseline trade that still has bars matches the risk sweep's per-trade "
        "return within 0.001 pp and the trade count equals the anchor minus the trades whose "
        "ticker has no bars.")
    R.w("")
    cut = pd.Timestamp(ANCHOR_DATA_END)
    sw = pd.read_csv(os.path.join(REPORTS, "backtest_risk_sweep_trades_2026-07-08.csv"))
    sw = sw[(sw.surprise_pct >= 15) & (sw.q == 3)].copy()
    sw["entry_date"] = pd.to_datetime(sw.entry_date)
    sw["period"] = sw.period.map({"IS (2022-2024)": "IS 2022-2024", "OOS (2025)": "OOS 2025",
                                  "2026 YTD": "2026 YTD"})
    rows, anc, drows = [], {}, []
    for lab in P.PERIODS:
        sub = sw[sw.period == lab]
        rets, nobars, mism = [], 0, 0
        for r in sub.itertuples():
            h = hists.get(r.ticker)
            if h is None:
                nobars += 1
                drows.append([f"{r.ticker} {r.entry_date.date()}", lab, f"{r.flat8_ret_pct:.2f}%",
                              "no bars served by Yahoo today (AAPL control live)", "dropped"])
                continue
            raw = h.loc[h.index == r.entry_date, "RawOpen"]
            res = None
            if len(raw) and raw.iloc[0] >= P.MIN_PRICE:
                res = rs.simulate(h[h.index < cut], r.entry_date, 8.0)
            if res is None or abs(res["return_pct"] - r.flat8_ret_pct) > P.ANCHOR_TRADE_TOL:
                mism += 1
                drows.append([f"{r.ticker} {r.entry_date.date()}", lab, f"{r.flat8_ret_pct:.2f}%",
                              "not reproduced", "FAIL"])
                continue
            rets.append(res["return_pct"])
        st = anchor_stats(rets)
        tgt = P.ANCHOR[lab]
        good = mism == 0 and st["n"] == tgt["n"] - nobars
        ok_all &= good
        anc[lab] = st
        rows.append([lab, f"{st['n']} / {tgt['n']}", str(nobars), f"{st['win']:.1f}% / {tgt['win']}%",
                     f"{st['avg']:.3f}% / {tgt['avg']}%", f"{st['pf']:.3f} / {tgt['pf']}",
                     "PASS" if good else "FAIL"])
    R.table("g0_anchor", ["Period", "Trades (got / anchor)", "No-bars trades", "Win (got / anchor)",
                          "Avg (got / anchor)", "PF (got / anchor)", "Result"], rows)
    if drows:
        R.w("Committed baseline trades not in the reproduction:")
        R.w("")
        R.table("g0_diag", ["Trade", "Period", "Committed return", "Reason", "Status"], drows)
    unserved = sorted(set(cands.ticker) - set(hists))
    R.w(f"Tickers with no Yahoo history today (dropped from every arm and from random pools): "
        f"`{', '.join(unserved)}`.")
    R.w("")

    # 3. ^IRX coverage
    R.w("### Item 3 — ^IRX (13-week T-bill, percent) on the trading calendar")
    R.w("")
    span = (panel.dates >= np.datetime64("2022-01-01")) & (panel.dates <= np.datetime64("2026-06-04"))
    miss = int(np.isnan(irx_raw[span]).sum())
    frac = miss / span.sum()
    m23 = np.nanmean(irx_raw[(panel.dates >= np.datetime64("2023-01-01")) & (panel.dates <= np.datetime64("2024-12-31"))])
    g3 = frac <= 0.02 and 4.5 <= m23 <= 5.6
    R.table("g0_irx", ["Check", "Value", "Pass rule", "Result"], [
        ["Missing ^IRX values on SPY dates", str(miss), "<= 2% of days (forward-filled)", "PASS" if frac <= 0.02 else "FAIL"],
        ["Mean ^IRX 2023-2024", f"{m23:.2f}", "4.5 to 5.6", "PASS" if 4.5 <= m23 <= 5.6 else "FAIL"],
    ])
    ok_all &= g3

    # 4. engine reproduces simulate() per trade when unconstrained and cost-free
    R.w("### Item 4 — portfolio engine vs simulate() (unconstrained, zero cost, full data)")
    R.w("")
    erows = []
    p1 = cands[(cands.surprise_pct >= 15) & (cands.q == 3) & cands.f_nearearn]
    for lab, (s, e) in P.PERIODS.items():
        sub = p1[p1.period == lab]
        run = P.run_portfolio(panel, sub, s, e, 0.11, 0.0, np.zeros(len(panel.dates)),
                              np.zeros(len(panel.dates), bool), constrained=False, log=True)
        cid2 = sub.set_index("cid")
        worst, n = 0.0, 0
        for t in run["trades"]:
            if t["exit"] == "open_at_period_end":
                continue
            r = cid2.loc[t["cid"]]
            ref = rs.simulate(hists[r.ticker], pd.Timestamp(r.entry_date), 8.0)
            worst = max(worst, abs(ref["return_pct"] - t["gross_ret"]))
            n += 1
        dup = sum(1 for x in run["rejects"] if x[5] == "already_held")
        g = worst < 1e-6
        ok_all &= g
        erows.append([lab, str(n), f"{worst:.1e}", str(dup), "PASS" if g else "FAIL"])
    R.table("g0_engine", ["Period", "Closed trades compared", "Max abs diff (pp)",
                          "Same-ticker overlaps skipped", "Result"], erows)
    return ok_all, anc


# ─── main ─────────────────────────────────────────────────────────────────────
def main():
    t0 = datetime.now()
    R = Report()
    cands = load_candidates()
    tickers = sorted(set(cands.ticker))
    print(f"{len(cands)} candidates, {len(tickers)} tickers")
    hists, missing = fetch_all(tickers + ["SPY", "IEF", "^IRX"])
    for t in ("SPY", "IEF", "^IRX"):
        if t not in hists:
            print(f"FATAL: {t} unavailable (transport)"); sys.exit(2)
    cal = hists["SPY"].index
    cal = cal[cal >= pd.Timestamp("2021-06-01")]
    irx_raw = hists["^IRX"]["Close"].reindex(cal).to_numpy(float)
    irx = pd.Series(irx_raw).ffill().to_numpy()
    bill = P.bill_daily(cal.values, irx)
    stock_hists = {t: h for t, h in hists.items() if t != "^IRX"}
    panel = P.Panel(stock_hists, cal.values)
    spy_k = panel.col["SPY"]
    spy_ret_all = np.r_[np.nan, panel.mark[1:, spy_k] / panel.mark[:-1, spy_k] - 1]

    R.w(f"# PEAD portfolio simulation — real daily equity curve vs SPY and 60/40 ({RUN_DATE})")
    R.w("")
    R.w("*Research only. No `memory/strategy.md` edit, no orders, no live routine touched. "
        "Generated by `backtesting/scripts/backtest_pead_portfolio_sim.py`; definitions, arms, "
        "questions and engine pre-registered in `backtesting/scripts/pead_portfolio_prereg.py`.*")
    R.w("")
    ok, anchor = gate0(R, cands, hists, panel, bill, irx_raw)
    R.w("")
    if "--gate0-only" in sys.argv:
        print("\n".join(R.lines)); sys.exit(0 if ok else 1)
    if not ok:
        R.w("**GATE 0: FAIL — stopped before any portfolio run. See the failing rows above.**")
        open(REPORT_MD, "w").write("\n".join(R.lines) + "\n")
        json.dump(R.claims, open(CLAIMS, "w"), indent=1)
        print("GATE 0 FAILED"); sys.exit(1)
    R.w("**GATE 0: PASS** — the transport returns live AAPL bars, the per-trade baseline is "
        "reproduced trade by trade in all three periods (the trades whose tickers no longer have bars are dropped and listed above), ^IRX is usable after forward-filling, and the "
        "portfolio engine reproduces `simulate()` trade by trade when caps and costs are off.")
    R.w("")

    # ── posture ───────────────────────────────────────────────────────────────
    base = cands[cands.src == "base"]
    elev_rec, weekly = P.weekly_posture(panel, base)
    weekly.to_csv(POSTURE_CSV, index=False)
    no_elev = np.zeros(len(panel.dates), bool)

    def elev_for(period, posture):
        return elev_rec if (posture == "on" and period in P.POSTURE_PERIODS) else no_elev

    # ── runs ──────────────────────────────────────────────────────────────────
    results, all_rejects, all_trades = {}, [], []
    filtered_by_posture = {}

    def arm_cands(arm, period, elev):
        sub = cands[cands.period == period]
        if period == "2026 YTD" and arm != "P1":
            return None                     # no committed 2026 base population
        if period != "2026 YTD":
            sub = sub[sub.src == "base"]
        idx = np.array([panel.pos.get(np.datetime64(d, "D"), -1) for d in sub.entry_date])
        e = np.where(idx >= 0, elev[np.clip(idx, 0, None)], False)
        m = P.arm_mask(sub, arm, e)
        m_noelev = P.arm_mask(sub, arm, np.zeros(len(sub), bool))
        return sub[m], int((m_noelev & ~m).sum())

    def period_metrics(run, period):
        s, e = P.PERIODS[period]
        d0 = np.searchsorted(panel.dates, np.datetime64(s, "D"))
        d1 = np.searchsorted(panel.dates, np.datetime64(e, "D"), side="right")
        return P.metrics(run["eq"], spy_ret_all[d0:d1], run.get("exposure"))

    configs = [(sz, cost, post) for sz in P.SIZES for cost in (P.COST_PRIMARY, P.COST_SENS)
               for post in ("on", "off")]
    for sz, cost, post in configs:
        for period, (s, e) in P.PERIODS.items():
            if post == "on" and period not in P.POSTURE_PERIODS:
                continue                    # 2026 posture-off only (not reconstructible)
            el = elev_for(period, post)
            for arm in P.ARMS:
                got = arm_cands(arm, period, el)
                if got is None:
                    continue
                sub, nfilt = got
                run = P.run_portfolio(panel, sub, s, e, sz, cost, bill, el)
                m = period_metrics(run, period)
                rej = pd.DataFrame(run["rejects"], columns=["cid", "ticker", "sector", "date",
                                                            "surprise_pct", "reason"])
                m["Trades"] = len(run["trades"])
                m["Qualified"] = len(sub)
                for rsn in REASONS:
                    m[rsn] = int((rej.reason == rsn).sum())
                m["Rejected"] = int(rej.reason.isin(REASONS).sum())
                m["PostureFiltered"] = nfilt
                key = (arm, period, sz, cost, post)
                results[key] = (m, run, rej)
                if cost == P.COST_PRIMARY:
                    rej = rej.assign(arm=arm, period=period, size=sz, posture=post)
                    all_rejects.append(rej)
                    tr = pd.DataFrame(run["trades"]).assign(arm=arm, period=period, size=sz,
                                                            posture=post)
                    all_trades.append(tr)
            for bname, w, mon in (("SPY", {"SPY": 1.0}, False),
                                  ("60/40", {"SPY": 0.6, "IEF": 0.4}, True)):
                b = P.run_benchmark(panel, w, s, e, cost, bill, mon)
                results[(bname, period, sz, cost, post)] = (period_metrics(b, period), b, None)
        print(f"  config size={sz} cost={cost} posture={post} done", flush=True)

    def primary_post(period):
        return "on" if period in P.POSTURE_PERIODS else "off"

    # ── matched random arm (primary config) ──────────────────────────────────
    print("Matched random arm...", flush=True)
    sector_of = cands.groupby("ticker")["sector"].first().to_dict()
    earn_by = {t: np.sort(g.earn_date.values.astype("datetime64[D]"))
               for t, g in cands.groupby("ticker")}
    p1_all = cands[(cands.surprise_pct >= 15) & (cands.q == 3) & cands.f_nearearn
                   & cands.period.notna()]
    p1_all = p1_all[(p1_all.src == "base") | (p1_all.period == "2026 YTD")]
    matches, levels = build_matches(panel, p1_all, sector_of, earn_by)
    rng = np.random.default_rng(P.SEED)
    rnd = {}
    for period, (s, e) in P.PERIODS.items():
        post = primary_post(period)
        el = elev_for(period, post)
        sub, _ = arm_cands("P1", period, el)
        sub = sub[sub.cid.isin(matches.keys())]
        draws = {cid: rng.integers(0, len(matches[cid]), P.N_RANDOM) for cid in sub.cid}
        for sz in P.SIZES:
            ms = []
            for k in range(P.N_RANDOM):
                rc = sub.copy()
                rc["ticker"] = [matches[c][draws[c][k]] for c in rc.cid]
                run = P.run_portfolio(panel, rc, s, e, sz, P.COST_PRIMARY, bill, el, log=False)
                mm = period_metrics(run, period)
                mm["Trades"] = len(run["trades"])
                ms.append(mm)
            rnd[(period, sz)] = pd.DataFrame(ms)
        print(f"  random {period} done", flush=True)
    rnd_out = pd.concat([d.assign(period=p, size=z) for (p, z), d in rnd.items()])
    rnd_out.to_csv(RANDOM_CSV, index=False)
    lvl_share = pd.Series(levels).value_counts(normalize=True)

    # ── CSV outputs ───────────────────────────────────────────────────────────
    pd.concat(all_rejects).to_csv(REJECTS_CSV, index=False)
    pd.concat(all_trades).to_csv(TRADES_CSV, index=False)
    grid = []
    for (arm, period, sz, cost, post), (m, _, _) in results.items():
        grid.append(dict(arm=arm, period=period, size=sz, cost_bp=cost * 1e4, posture=post,
                         **{k: v for k, v in m.items()}))
    pd.DataFrame(grid).to_csv(GRID_CSV, index=False)

    build_report(R, results, rnd, weekly, elev_rec, panel, anchor, lvl_share, cands)
    open(REPORT_MD, "w").write("\n".join(R.lines) + "\n")
    json.dump(R.claims, open(CLAIMS, "w"), indent=1)
    print(f"Wrote {REPORT_MD} ({(datetime.now() - t0).seconds}s)")


# ─── report ───────────────────────────────────────────────────────────────────
def build_report(R, results, rnd, weekly, elev, panel, anchor, lvl_share, cands):
    PER = list(P.PERIODS)
    PRIM = P.COST_PRIMARY

    def pp(period):
        return "on" if period in P.POSTURE_PERIODS else "off"

    def M(arm, period, sz, cost=PRIM, post=None):
        k = (arm, period, sz, cost, post or pp(period))
        return results[k][0] if k in results else None

    def szl(sz):
        return f"{int(round(sz * 100))}%"

    # posture summary
    R.w("## Setup")
    R.w("")
    R.w("- Arms P1/P2/P3, the matched random arm, SPY and 60/40 all run through one daily "
        "mark-to-market engine from $100k per period; IS 2022-2024, OOS 2025 and 2026 YTD "
        "are separate runs and are never pooled.")
    R.w("- Live constraints: 8 concurrent positions, 30% sector cap, 10% cash floor, 5 new "
        "positions per week, -8% hard stop, +10% trigger (sell 1/3, trail the rest 7%), "
        "42-day time stop. Sizes 11% and 20% of equity. Costs 5 bp per side, 10 bp as a "
        "sensitivity. Idle cash earns ^IRX.")
    R.w("- Ranking when candidates compete for room: EPS surprise, largest first (the live "
        "1-10 score cannot be rebuilt from price and earnings data; surprise is its only graded "
        "input available for every candidate).")
    R.w("- A candidate whose room under the sector cap or cash floor is smaller than the target "
        "size is trimmed to fit; below half the target size it is rejected and logged.")
    R.w("- Not applied, as in the anchor: the sector-specific >20% EPS bars and the SPY<200MA "
        "bear-regime gate in `strategy.md`.")
    R.w("")
    R.w("### ELEVATED_BAR posture")
    R.w("")
    prow = []
    for period in P.POSTURE_PERIODS:
        s, e = P.PERIODS[period]
        msk = (panel.dates >= np.datetime64(s)) & (panel.dates <= np.datetime64(e))
        wk = weekly[(pd.to_datetime(weekly.sunday) >= pd.Timestamp(s) - pd.Timedelta(days=6))
                    & (pd.to_datetime(weekly.sunday) <= pd.Timestamp(e))]
        thin = int((wk.n < P.HEALTH_MIN_N).sum())
        prow.append([period, f"{elev[msk].mean() * 100:.0f}%", str(len(wk)), str(thin)])
    prow.append(["2026 YTD", "not reconstructible", "n/a", "n/a"])
    R.table("posture", ["Period", "Share of trading days ELEVATED_BAR", "Weekly readings",
                        "Thin-data weeks (fail-open NORMAL)"], prow)
    R.p("The health metric is rebuilt every Sunday from committed base trades with a positive "
        "surprise that exited in the prior 60 days, the same rule `compute_pead_health.py` "
        "uses, and only bars on or before that Sunday. ELEVATED_BAR was in force on "
        f"{R.c('posture', 'IS 2022-2024', 'Share of trading days ELEVATED_BAR')} of IS days and "
        f"{R.c('posture', 'OOS 2025', 'Share of trading days ELEVATED_BAR')} of OOS days. "
        "The first IS weeks fail open because the committed set starts with 2022 entries.")
    R.w("2026 YTD runs posture-off: the committed data has no 2026 base population and the "
        "live `pead_health.md` history starts 2026-09-20, after the 2026 candidate window. "
        "Posture-off results for IS and OOS are in the sensitivity section.")
    R.w("")

    # main tables
    R.w("## Results by period")
    R.w("")
    R.w("CAGR uses years = trading days / 252, so the 2026 YTD figure annualises about five "
        "months; Total is the unannualised return. Sharpe is on daily returns. Invested is the "
        "average share of equity in stocks. Rejected counts qualified candidates turned away "
        "by a cap (slots, weekly, sector, cash floor, already held). Beta, alpha (annualised) "
        "and R2 come from regressing daily returns on SPY daily returns. RND is the median of "
        "500 matched random simulations.")
    R.w("")
    hdr = ["Arm", "CAGR", "Total", "Sharpe", "MaxDD", "Invested", "Trades", "Rejected",
           "Beta", "Alpha", "R2"]
    for sz in P.SIZES:
        for period in PER:
            rows = []
            for arm in list(P.ARMS) + ["RND", "SPY", "60/40"]:
                if arm == "RND":
                    d = rnd[(period, sz)]
                    rows.append(["RND median", pct(d.CAGR.median()), pct(d.TotRet.median()),
                                 f2(d.Sharpe.median()), pct(d.MaxDD.median()),
                                 pct(d.Invested.median(), 0), f"{d.Trades.median():.0f}", "n/a",
                                 f2(d.Beta.median()), pct(d.Alpha.median()), f2(d.R2.median())])
                    continue
                m = M(arm, period, sz)
                if m is None:
                    rows.append([arm, "no row"] + ["n/a"] * 9)
                    continue
                bench = arm in ("SPY", "60/40")
                rows.append([arm, pct(m["CAGR"]), pct(m["TotRet"]), f2(m["Sharpe"]),
                             pct(m["MaxDD"]), pct(m.get("Invested", np.nan), 0) if not bench else "100%",
                             str(m["Trades"]) if not bench else "n/a",
                             str(m["Rejected"]) if not bench else "n/a",
                             f2(m["Beta"]), pct(m["Alpha"]), f2(m["R2"])])
            R.w(f"### {period} — {szl(sz)} position size")
            R.w("")
            R.table(f"res_{period}_{szl(sz)}".replace(" ", "_"), hdr, rows)
    R.w("P2 and P3 have no 2026 YTD row: the committed 2026 data is only the 30 live-bar "
        "trades, so the wider candidate sets cannot be built for 2026.")
    R.w("")

    # rejections per year (Q5)
    R.w("## Candidates turned away (Q5)")
    R.w("")
    R.w("Qualified candidates rejected by each cap, primary configuration (5 bp, posture as "
        "above), per calendar year. Every rejected candidate is logged with its reason in "
        f"`backtesting/reports/{os.path.basename(REJECTS_CSV)}`.")
    R.w("")
    for sz in P.SIZES:
        rows = []
        for arm in P.ARMS:
            for period in PER:
                res = results.get((arm, period, sz, PRIM, pp(period)))
                if res is None:
                    continue
                m, run, rej = res
                yrs = pd.to_datetime(rej.date).dt.year if len(rej) else pd.Series(dtype=int)
                tyrs = pd.Series([pd.Timestamp(t["entry_date"]).year for t in run["trades"]])
                for y in sorted(set(tyrs) | set(yrs)):
                    ry = rej[yrs == y]
                    rows.append([f"{arm} {y}", str(int((tyrs == y).sum()))]
                                + [str(int((ry.reason == rsn).sum())) for rsn in REASONS]
                                + [str(int(ry.reason.isin(REASONS).sum()))])
        R.w(f"### {szl(sz)} position size")
        R.w("")
        R.table(f"rej_{szl(sz)}", ["Arm year", "Trades taken", "Slots full (8)", "Weekly cap",
                                   "Sector cap", "Cash floor", "Already held", "Total rejected"],
                rows)
    R.w("")

    # random arm
    R.w("## Matched random arm (500 simulations, same engine)")
    R.w("")
    R.w("Each P1 candidate's ticker is replaced by a random name from the same sector and the "
        "same 20-day dollar-volume quintile on the same entry date, keeping the P1 entry date, "
        "rank and posture treatment. Share at or above P1 is the fraction of the 500 random "
        "portfolios whose Sharpe is at least P1's (a one-sided p-value).")
    R.w("")
    rows = []
    for sz in P.SIZES:
        for period in PER:
            d = rnd[(period, sz)]
            m = M("P1", period, sz)
            rows.append([f"{period} {szl(sz)}", f2(m["Sharpe"]), f2(d.Sharpe.median()),
                         f2(d.Sharpe.quantile(0.05)), f2(d.Sharpe.quantile(0.95)),
                         f"{(d.Sharpe >= m['Sharpe']).mean():.3f}", pct(m["CAGR"]),
                         pct(d.CAGR.median()), pct(m["MaxDD"]), pct(d.MaxDD.median())])
    R.table("rnd", ["Period size", "P1 Sharpe", "RND median Sharpe", "RND 5th pct",
                    "RND 95th pct", "Share at or above P1", "P1 CAGR", "RND median CAGR",
                    "P1 MaxDD", "RND median MaxDD"], rows)
    lv = ", ".join(f"{k} {v * 100:.0f}%" for k, v in lvl_share.items())
    R.w(f"Match level across P1 candidates: `{lv}`. 2026 earnings exclusions only know the "
        "30 committed 2026 candidates' report dates, so 2026 controls may include names near "
        "their own earnings.")
    R.w("")

    # Q4 decomposition
    R.w("## Market exposure vs stock selection (Q4)")
    R.w("")
    R.w("Annualised mean daily return split into beta times the SPY mean daily return "
        "(market part) and the regression intercept (alpha). Market share is the market part "
        "divided by the arm's annualised mean return, shown only when that mean is positive.")
    R.w("")
    rows = []
    for sz in P.SIZES:
        for arm in list(P.ARMS):
            for period in PER:
                m = M(arm, period, sz)
                if m is None:
                    continue
                share = (f"{m['MktPart'] / m['AnnMean'] * 100:.0f}%" if m["AnnMean"] > 0
                         else "n/a (mean <= 0)")
                rows.append([f"{arm} {period} {szl(sz)}", pct(m["AnnMean"]), pct(m["MktPart"]),
                             pct(m["Alpha"]), f2(m["Beta"]), f2(m["R2"]), share])
    R.table("q4", ["Arm period size", "Ann. mean return", "Market part", "Alpha", "Beta", "R2",
                   "Market share"], rows)

    # sensitivities
    R.w("## Sensitivities")
    R.w("")
    R.w("Same engine. 10 bp per side instead of 5 bp, and ELEVATED_BAR switched off in IS and "
        "OOS (2026 is posture-off in every row).")
    R.w("")
    rows = []
    for sz in P.SIZES:
        for arm in list(P.ARMS) + ["SPY", "60/40"]:
            for period in PER:
                a = M(arm, period, sz)
                b = M(arm, period, sz, cost=P.COST_SENS)
                c = M(arm, period, sz, post="off")
                if a is None:
                    continue
                rows.append([f"{arm} {period} {szl(sz)}", f2(a["Sharpe"]), pct(a["CAGR"]),
                             f2(b["Sharpe"]), pct(b["CAGR"]), f2(c["Sharpe"]), pct(c["CAGR"]),
                             pct(c["MaxDD"])])
    R.table("sens", ["Arm period size", "Primary Sharpe", "Primary CAGR", "10bp Sharpe",
                     "10bp CAGR", "Posture-off Sharpe", "Posture-off CAGR", "Posture-off MaxDD"],
            rows)

    # questions
    R.w("## Pre-registered questions — verdicts")
    R.w("")
    R.w("Answered at 5 bp per side with the primary posture, for both position sizes. "
        "\"Beats\" means strictly better; for drawdown, shallower.")
    R.w("")
    rows = []
    O, I = "OOS 2025", "IS 2022-2024"
    for sz in P.SIZES:
        p1o, spo = M("P1", O, sz), M("SPY", O, sz)
        t1 = P.q1(p1o, spo)
        rows.append([f"Q1 {szl(sz)}", f"CAGR {yn(t1['cagr'])}, Sharpe {yn(t1['sharpe'])}, "
                     f"MaxDD {yn(t1['maxdd'])}"])
        q2i = P.q2(M("P1", I, sz), M("60/40", I, sz))
        q2o = P.q2(M("P1", O, sz), M("60/40", O, sz))
        rows.append([f"Q2 {szl(sz)}", f"IS {yn(q2i)}, OOS {yn(q2o)}, both {yn(q2i and q2o)}"])
        q3i = P.q3(M("P1", I, sz), M("P2", I, sz))
        q3o = P.q3(M("P1", O, sz), M("P2", O, sz))
        rows.append([f"Q3 {szl(sz)}", f"IS {yn(q3i)}, OOS {yn(q3o)}, both {yn(q3i and q3o)}"])
    R.table("verdict", ["Question size", "Answer"], rows)
    mar = []
    for sz in P.SIZES:
        for arm in ("P1", "SPY", "60/40"):
            for period in (I, O):
                m = M(arm, period, sz)
                mar.append([f"{arm} {period} {szl(sz)}", f2(m["MAR"])])
    R.table("mar", ["Arm period size", "CAGR/MaxDD"], mar)

    T = lambda period, sz: f"res_{period}_{szl(sz)}".replace(" ", "_")  # noqa: E731
    R.w("### Plain-language verdicts")
    R.w("")
    for sz in P.SIZES:
        s_ = szl(sz)
        to = T(O, sz)
        R.p(f"**Q1 ({s_} size).** In OOS 2025, P1 made {R.c(to, 'P1', 'CAGR')} a year against "
            f"SPY's {R.c(to, 'SPY', 'CAGR')}, with Sharpe {R.c(to, 'P1', 'Sharpe')} vs "
            f"{R.c(to, 'SPY', 'Sharpe')} and max drawdown {R.c(to, 'P1', 'MaxDD')} vs "
            f"{R.c(to, 'SPY', 'MaxDD')}. Answer: {R.c('verdict', f'Q1 {s_}', 'Answer')}.")
    for sz in P.SIZES:
        s_ = szl(sz)
        R.p(f"**Q2 ({s_} size).** Sharpe P1 vs 60/40: IS {R.c(T(I, sz), 'P1', 'Sharpe')} vs "
            f"{R.c(T(I, sz), '60/40', 'Sharpe')}, OOS {R.c(T(O, sz), 'P1', 'Sharpe')} vs "
            f"{R.c(T(O, sz), '60/40', 'Sharpe')}; CAGR/MaxDD IS "
            f"{R.c('mar', f'P1 {I} {s_}', 'CAGR/MaxDD')} vs {R.c('mar', f'60/40 {I} {s_}', 'CAGR/MaxDD')}, "
            f"OOS {R.c('mar', f'P1 {O} {s_}', 'CAGR/MaxDD')} vs "
            f"{R.c('mar', f'60/40 {O} {s_}', 'CAGR/MaxDD')}. Answer: "
            f"{R.c('verdict', f'Q2 {s_}', 'Answer')}.")
    q3_fail = []
    for sz in P.SIZES:
        s_ = szl(sz)
        R.p(f"**Q3 ({s_} size).** Sharpe P1 vs P2: IS {R.c(T(I, sz), 'P1', 'Sharpe')} vs "
            f"{R.c(T(I, sz), 'P2', 'Sharpe')}, OOS {R.c(T(O, sz), 'P1', 'Sharpe')} vs "
            f"{R.c(T(O, sz), 'P2', 'Sharpe')}. Answer: {R.c('verdict', f'Q3 {s_}', 'Answer')}.")
        ok3 = P.q3(M("P1", I, sz), M("P2", I, sz)) and P.q3(M("P1", O, sz), M("P2", O, sz))
        if not ok3:
            q3_fail.append(s_)
    if q3_fail:
        R.w(f"Because P1 does not beat P2 on Sharpe in both periods at {' and '.join(q3_fail)} "
            "size, the volume, relative-strength and 52-week-high filters cost more in lost "
            "trades than they add in selection at the portfolio level, on this data.")
    else:
        R.w("P1 beats P2 on Sharpe in both periods at both sizes, so at the portfolio level the "
            "extra filters add more in selection than they cost in lost trades, on this data.")
    for sz in P.SIZES:
        s_ = szl(sz)
        q = "q4"
        parts = []
        for arm in P.ARMS:
            for period in (I, O):
                row = f"{arm} {period} {s_}"
                parts.append(f"{arm} {period.split()[0]} beta {R.c(q, row, 'Beta')} "
                             f"(market share {R.c(q, row, 'Market share')})")
        R.p(f"**Q4 ({s_} size).** " + "; ".join(parts) + ".")
    for sz in P.SIZES:
        s_ = szl(sz)
        parts = []
        for arm in P.ARMS:
            for period in (I, O):
                tb = T(period, sz)
                parts.append(f"{arm} {period.split()[0]} took {R.c(tb, arm, 'Trades')} and "
                             f"turned away {R.c(tb, arm, 'Rejected')}")
        R.p(f"**Q5 ({s_} size).** " + "; ".join(parts) + ". The per-year split by cap is in "
            "the Q5 table; the 8-slot cap binds only where the Slots full column is non-zero.")
    R.w("")
    R.w("No `strategy.md` change is recommended by this report.")
    R.w("")

    # limitations
    R.w("## Limitations")
    R.w("")
    R.w("- **Survivorship.** The universe is current S&P 500 members only, for every arm "
        "including the random control, so names that left the index are missing from both sides.")
    R.w("- **2026.** The only 2026 data is the 30 committed live-bar trades, so P2 and P3 have no "
        "2026 row, the 2026 posture cannot be rebuilt, and 2026 random controls use a weaker "
        "earnings exclusion.")
    R.w("- **Costs.** No slippage beyond the 5 bp (or 10 bp) per side assumption; fills are at "
        "the open (entries) and the close (exits), with the 1/3 scale-out booked at exactly +10% "
        "as the per-trade simulator books it. Shares are fractional.")
    R.w("- **Repeated testing.** This is now at least the thirteenth backtest run on this same "
        "2022-2025 candidate set (in-sample, OOS, enhanced filters, signal health, health + 200MA, "
        "variants, ATR stop vs flat, ATR stop widened, risk sweep, ELEVATED_BAR threshold "
        "comparison, PEAD vs random, and this simulation), so OOS 2025 is no longer a clean "
        "holdout.")
    R.w("- **Live score.** The live 1-10 score and its research inputs (guidance, analysts, "
        "insiders, regulatory scans) cannot be reconstructed; P1 is the mechanical live bar "
        "and ranking uses EPS surprise as a proxy.")
    R.w("- **Rules not modelled.** Sector-specific >20% EPS bars, the SPY<200MA bear-regime "
        "gate, thesis-break exits and the 60-day rotation rule are not applied.")
    R.w("- **Health warm-up.** The committed set starts with 2022 entries, so the first IS "
        "weeks have too few realised trades and fail open to NORMAL.")
    R.w("- **Size proxy.** Random matching uses 20-day dollar volume, not market cap.")
    R.w("")
    R.w("## Pre-registration record")
    R.w("")
    log = subprocess.run(["git", "log", "--format=%h %ad %s", "--date=iso", "--",
                          "backtesting/scripts/pead_portfolio_prereg.py"],
                         cwd=REPO, capture_output=True, text=True).stdout.strip().splitlines()
    R.w("Commits touching `pead_portfolio_prereg.py` (questions, arms, constants, engine):")
    R.w("")
    R.w("```")
    for ln in log:
        R.w(ln)
    R.w("```")
    R.w("")
    R.w("Outputs: " + ", ".join(f"`backtesting/reports/{os.path.basename(x)}`" for x in
                                 (GRID_CSV, TRADES_CSV, REJECTS_CSV, POSTURE_CSV, RANDOM_CSV,
                                  CLAIMS)) + ".")


if __name__ == "__main__":
    main()
