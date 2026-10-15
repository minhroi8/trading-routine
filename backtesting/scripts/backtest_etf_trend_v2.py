"""
ETF trend backtest v2 -- runner and report writer. Research only.

Definitions, tests, grids and the engine live in etf_trend_v2_prereg.py
(committed before the first full run). This file only orchestrates GATE 0,
runs the pre-registered configs, builds the tables and writes the report.

Report hygiene: every number in prose is pulled with Rep.q() from a table that
is already in the report; the (line, table, row, column, value) references are
written to reports/etf_trend_v2_claims_<date>.json and verified by
check_etf_trend_v2_report.py, which also rejects any prose number that is not
sourced from a table or a whitelisted pre-registered constant.
"""

import json
import os
import subprocess
import sys
from datetime import date

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etf_data  # noqa: E402
import backtest_etf_trend as v1  # noqa: E402
import etf_trend_v2_prereg as P  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backtesting/
ROOT = os.path.dirname(HERE)
REPORTS_DIR = os.path.join(HERE, "reports")
TODAY = date.today().isoformat()
REPORT_PATH = os.path.join(HERE, f"etf_trend_v2_{TODAY}.md")
CLAIMS_PATH = os.path.join(REPORTS_DIR, f"etf_trend_v2_claims_{TODAY}.json")
GRID_PATH = os.path.join(REPORTS_DIR, f"etf_trend_v2_grid_{TODAY}.csv")
PREREG_FILES = ["backtesting/scripts/etf_trend_v2_prereg.py", "backtesting/scripts/etf_data.py"]

PN_IS, PN_OOS = list(P.PERIODS)
PN_FULL = "Full 2006-latest"
ALLP = {PN_IS: P.PERIODS[PN_IS], PN_OOS: P.PERIODS[PN_OOS], PN_FULL: P.FULL}


# --------------------------------------------------------------------------
# formatting
# --------------------------------------------------------------------------
def pct(x, d=1):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    return f"{x*100:.{d}f}%"


def num(x, d=2):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    return f"{x:.{d}f}"


def pts(x):
    return f"{x*100:.1f}"


def yn(b):
    return "PASS" if b else "FAIL"


# --------------------------------------------------------------------------
# report builder with table registry + claim tracking
# --------------------------------------------------------------------------
class Rep:
    def __init__(self):
        self.secs, self.cur = {}, None
        self.tables, self.claims, self.buf = {}, [], []

    def sec(self, name):
        self.cur = self.secs.setdefault(name, [])

    def w(self, s=""):
        assert not self.buf, f"unattached claims before line: {s[:60]}"
        self.cur.append(s)

    def p(self, s):
        """Prose line; attaches the q() references used to build it."""
        self.cur.append(s)
        if self.buf:
            self.claims.append(dict(line=s, refs=self.buf))
        self.buf = []

    def table(self, tid, header, rows):
        for r in rows:
            assert len(r) == len(header), (tid, r)
            for c in list(r) + list(header):
                assert "|" not in str(c), f"pipe in table cell {tid}: {c}"
        labels = [r[0] for r in rows]
        assert len(labels) == len(set(labels)), f"duplicate row labels in {tid}"
        self.tables[tid] = (list(header), [list(map(str, r)) for r in rows])
        self.cur.append(f"<!-- table:{tid} -->")
        self.cur.append("| " + " | ".join(header) + " |")
        self.cur.append("|" + "---|" * len(header))
        for r in rows:
            self.cur.append("| " + " | ".join(map(str, r)) + " |")

    def q(self, tid, row, col):
        h, rows = self.tables[tid]
        r = [x for x in rows if x[0] == row]
        assert len(r) == 1, (tid, row)
        v = r[0][h.index(col)]
        self.buf.append(dict(table=tid, row=row, col=col, value=v))
        return v

    def text(self, order):
        out = []
        for s in order:
            out += self.secs.get(s, []) + [""]
        return "\n".join(out)


def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True,
                          text=True).stdout.strip()


# --------------------------------------------------------------------------
# GATE 0
# --------------------------------------------------------------------------
def gate0(R):
    R.sec("gate0")
    R.w("## GATE 0 — data, T-bill and validation anchor")
    R.w("")
    R.w("Transport: `requests` + Yahoo v8 chart API (browser User-Agent, query1→query2 fallback), "
        "live fetch with the cache bypassed — the v1 loader `etf_data.py`, unchanged except that "
        "`gate0()` now also accepts extra tickers (IEF) and its table header no longer contains pipe "
        "characters. A transport error stops the run and is reported as such, never as a data finding.")
    R.w("")
    R.w("### Items 1 and 2 — v1 Gate 0 re-run for SPY and the 16 ETFs, plus IEF")
    R.w("")
    ok, lines, data = etf_data.gate0(extra=[P.SAFE])
    bullets = [x for x in lines if not x.startswith("|") and x.strip()]
    tbl = [x for x in lines if x.startswith("|")]
    R.w("Raw output of `etf_data.gate0()` (bullet lines):")
    R.w("")
    R.w("```")
    for b in bullets:
        R.w(b)
    R.w("```")
    R.w("")
    if not data or len(tbl) < 3:
        R.w("**GATE 0 STOPPED — transport failure (not a data finding).**")
        return False, data, None, None
    hdr = [c.strip() for c in tbl[0].strip("|").split("|")]
    rows = [[c.strip() for c in t.strip("|").split("|")] for t in tbl[2:]]
    R.table("g0_etf", hdr, rows)
    R.w("")
    # dividend continuity for SPY and IEF (same rule as v1: max error <= 10 bp)
    drows, dok = [], True
    for t in ("SPY", P.SAFE):
        err, exd = etf_data.dividend_continuity(data[t])
        good = err.max() <= 0.0010
        dok &= good
        drows.append([t, len(exd), f"{err.max()*1e4:.2f}", f"{err.median()*1e4:.2f}", "10.00", yn(good)])
    R.w("Dividend continuity on every ex-date: abs(AdjClose return − ((Close + Div) / prevClose − 1)), in bp.")
    R.w("")
    R.table("g0_div", ["Ticker", "Ex-dates", "Max error (bp)", "Median error (bp)", "Limit (bp)", "Result"], drows)
    R.w("")
    ief_row = [r for r in rows if r[0] == P.SAFE][0]
    R.w(f"IEF row status (first bar, 2005-01-03 bar, NaNs, SPY-date coverage, splits, factor jumps) is in the "
        f"table above; `etf_data.gate0()` returns {'PASS' if ok else 'FAIL'} over all 17 rows.")
    R.w("")
    if not (ok and dok):
        R.w("**GATE 0 FAIL (data finding) — stopped.**")
        return False, data, None, None

    # ---- 0.3 ^IRX
    R.w("### Item 3 — ^IRX (13-week T-bill yield, percent)")
    R.w("")
    try:
        irx_df = etf_data.load("^IRX", refresh=True)
    except etf_data.TransportError as e:
        R.w(f"**GATE 0 STOPPED — transport failure fetching ^IRX (not a data finding):** `{e}`")
        return False, data, None, None
    idx = data["SPY"].index
    irx_ff, raw = P.irx_on(idx, irx_df)
    s = raw.loc["2005-01-03":]
    miss = s.isna()
    runs = (miss.groupby((~miss).cumsum()).sum()).max() if miss.any() else 0
    ff = irx_ff.loc["2005-01-03":]
    irows, iok = [], True
    frac = miss.mean()
    g = frac <= P.IRX_MAX_MISSING_FRAC
    iok &= g
    irows.append(["SPY trading days since 2005-01-03", str(len(s)), "—", "info"])
    irows.append(["Missing ^IRX values on SPY dates", str(int(miss.sum())),
                  f"<= {P.IRX_MAX_MISSING_FRAC*100:.0f}% of days", yn(g)])
    g = runs <= P.IRX_MAX_MISSING_RUN
    iok &= g
    irows.append(["Longest run of consecutive missing days", str(int(runs)),
                  f"<= {P.IRX_MAX_MISSING_RUN}", yn(g)])
    g = bool(ff.notna().all()) and ff.min() >= P.IRX_RANGE[0] and ff.max() <= P.IRX_RANGE[1]
    iok &= g
    irows.append(["Min / max after forward-fill (%)", f"{ff.min():.2f} / {ff.max():.2f}",
                  f"{P.IRX_RANGE[0]} to {P.IRX_RANGE[1]}", yn(g)])
    for lab, a, b, lo, hi in P.IRX_SANITY:
        m = ff.loc[a:b].mean()
        g = lo <= m <= hi
        iok &= g
        irows.append([f"Mean {lab} (%)", f"{m:.2f}", f"{lo} to {hi}", yn(g)])
    R.table("g0_irx", ["Check", "Value", "Threshold", "Result"], irows)
    R.w("")
    md = ", ".join(str(d.date()) for d in s.index[miss])
    bond_hol = all((d.month == 10 and d.dayofweek == 0 and 8 <= d.day <= 14) or (d.month == 11 and d.day == 11)
                   for d in s.index[miss])
    R.w(f"Missing dates (forward-filled with the prior day's value; disclosed): {md or 'none'}."
        + (" All are Columbus Day or Veterans Day, when the bond market is closed and stocks trade."
           if miss.any() and bond_hol else ""))
    R.w("")
    if not iok:
        R.w("**GATE 0 FAIL — ^IRX unusable; stopped. No substitute was used.**")
        return False, data, irx_ff, None

    # ---- 0.4 validation anchor
    R.w("### Item 4 — validation anchor: v1 pre-registered B re-run (SMA200, 1/16 sleeves, cash 0%)")
    R.w("")
    AC, AO = P.build_panels(data)
    b0 = P.run_B(AC, AO, P.zero_bill(AC.index), P.PRE_B["sma"], safe=False)
    arows, aok = [], True
    for pn, (a, b) in P.PERIODS.items():
        m = P.metrics(b0, a, b)
        got = dict(CAGR=m["CAGR"] * 100, Sharpe=m["Sharpe"], MaxDD=m["MaxDD"] * 100)
        for k, ref in P.ANCHOR[pn].items():
            d = abs(round(got[k], 6) - ref)
            g = d <= P.ANCHOR_TOL[k] + 1e-9
            aok &= g
            arows.append([f"{pn} {k}", f"{ref:.2f}", f"{got[k]:.3f}", f"{P.ANCHOR_TOL[k]:.2f}", yn(g)])
    R.table("g0_anchor", ["Period / metric", "v1 report", "v2 re-run", "Tolerance", "Result"], arows)
    R.w("")
    if not aok:
        R.w("**GATE 0 FAIL — anchor mismatch; stopped for diagnosis.**")
        return False, data, irx_ff, None
    R.w("**GATE 0: PASS** — all 16 ETFs and IEF have bars from 2005-01-03 with continuous dividend and split "
        "adjustment; ^IRX is usable after forward-filling the missing days listed above; the v1 anchor is "
        "reproduced within tolerance (the v2 engine with a zero cash rate is the v1 engine).")
    R.w("")
    return True, data, irx_ff, b0


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
NAMES = {
    "B0": "v1 B (cash 0%, anchor)",
    "B1": "B1 trend + T-bill",
    "B2": "B2 trend + IEF or T-bill",
    "VT": "VT SPY vol target",
    "BL": "BL 50% B1 + 50% VT",
    "SPY": "SPY buy-and-hold",
    "EW": "EW buy-and-hold (16 ETFs)",
    "6040": "60/40 SPY/IEF monthly",
}
MCOLS = ["Series", "CAGR", "Sharpe", "Sharpe ex T-bill", "MaxDD", "CAGR/MaxDD",
         "Avg exposure", "Avg IEF weight", "Round trips", "Fills"]


def mrow(name, m):
    return [name, pct(m["CAGR"]), num(m["Sharpe"]), num(m["ExSharpe"]), pct(m["MaxDD"]),
            num(m["MAR"]), pct(m["Exposure"], 0), pct(m["SafeExp"], 0),
            str(int(m.get("Trades", 0))), str(m["Fills"])]


def bill_run(rb, start=P.SIM_START):
    r = rb.loc[start:]
    eq = (1 + r).cumprod()
    z = pd.Series(0.0, eq.index)
    return dict(eq=eq, exp=z, safe_exp=z, spells=pd.DataFrame(), fills=pd.DatetimeIndex([]), rb=r)


def main():
    R = Rep()
    ok, data, irx_ff, b0 = gate0(R)
    if not ok:
        R.sec("head")
        R.w(f"# ETF trend backtest v2 — {TODAY}")
        R.w("")
        R.w("**STOPPED AT GATE 0.** No strategy was run. See below.")
        return R, ["head", "gate0"], None
    AC, AO = P.build_panels(data)
    idx = AC.index
    last = idx[-1].date()
    rb = P.bill_daily(idx, irx_ff)

    # ---------------- pre-registered runs
    # v1 B was simulated with a zero cash rate; its "Sharpe ex T-bill" is still
    # measured against the real T-bill like every other series.
    b0 = dict(b0, rb=rb.reindex(b0["eq"].index).fillna(0.0))
    runs = {"B0": b0,
            "B1": P.run_B(AC, AO, rb, P.PRE_B["sma"], safe=False),
            "B2": P.run_B(AC, AO, rb, P.PRE_B["sma"], safe=True),
            "VT": P.run_VT(AC, AO, rb, **P.PRE_VT),
            "BL": P.run_BL(AC, AO, rb)}
    spy_w, ew_w = {"SPY": 1.0}, P.ew_weights()
    bench = {}
    for pn, (a, b) in P.PERIODS.items():
        bench[pn] = {"SPY": P.bench_bh(AC, AO, rb, spy_w, a, b),
                     "EW": P.bench_bh(AC, AO, rb, ew_w, a, b),
                     "6040": P.bench_6040(AC, AO, rb, a, b)}
    bench[PN_FULL] = {"SPY": P.bench_bh(AC, AO, rb, spy_w, P.SIM_START, None),
                      "EW": P.bench_bh(AC, AO, rb, ew_w, P.SIM_START, None),
                      "6040": P.bench_6040(AC, AO, rb, P.SIM_START, None)}
    M = {}
    for pn, (a, b) in ALLP.items():
        for k, r in runs.items():
            M[(k, pn)] = P.metrics(r, a, b)
        for k, r in bench[pn].items():
            M[(k, pn)] = P.metrics(r, a, b)
    bill = bill_run(rb)

    # ---------------- definitions section
    R.sec("defs")
    sha = git("log", "--diff-filter=A", "--format=%h", "--", PREREG_FILES[0]).splitlines()
    sha = sha[-1] if sha else "uncommitted"
    later = git("log", "--format=%h %s", f"{sha}..HEAD", "--", *PREREG_FILES).splitlines()
    dirty = git("status", "--porcelain", "--", *PREREG_FILES)
    R.w("## Pre-registration")
    R.w("")
    R.w(f"Definitions, tests, grids, Gate 0 thresholds and the engine are in "
        f"`backtesting/scripts/etf_trend_v2_prereg.py`, committed in `{sha}` before the first full run. "
        "Every later commit touching it or `etf_data.py` (from `git log` at report time):")
    R.w("")
    for c in later or ["none"]:
        R.w(f"- `{c.split(' ', 1)[0]}` {c.split(' ', 1)[1] if ' ' in c else ''}".rstrip())
    R.w("")
    R.w("The first run attempt crashed inside the B2 run (an indexing bug) before any v2 metric was computed "
        "or printed; the one-line fix above changed no definition, parameter, test or grid."
        + (" **Uncommitted changes to the pre-registered files exist at report time.**" if dirty else ""))
    R.w("")
    R.w("Smoke tests before that commit, disclosed: (a) the new engine with a zero cash rate was run on v1 B "
        "and matched v1's `strat_B` equity curve exactly (the Gate 0 anchor, a result already published in v1); "
        "(b) a two-account run of two identical B accounts was checked against one account (identical). "
        "No B1, B2, VT, BL or benchmark-with-T-bill result was computed or viewed before the commit, and nothing "
        "in the pre-registration module was changed afterward apart from the crash fix listed above. This runner (tables, wording, the interpretation "
        "text) was written and edited after the run; it does not define any strategy, test or grid.")
    R.w("")
    R.w("## Definitions (pre-registered)")
    R.w("")
    R.w("- **Inherited from v1.** Same 16 ETFs (SPY QQQ IWM EFA EEM TLT GLD XLK XLF XLE XLV XLY XLP XLI XLB XLU); "
        f"IS 2006-01-03 to 2017-12-29, OOS 2018-01-02 to {last}; signals on Yahoo AdjClose (total return) at "
        "close t, fills at the open of t+1 (open converted to the total-return basis); 5 bp per side on every "
        "fill including rebalances; daily mark-to-market. Sharpe is annualised from daily returns with rf = 0 "
        "(v1 convention, needed for the anchor); the column \"Sharpe ex T-bill\" uses returns in excess of the "
        "same T-bill and is information plus a labeled sensitivity of the tests.")
    R.w("- **Cash.** Idle money earns the T-bill: daily return = (^IRX at the prior close / 100) × "
        "(calendar days since the prior bar) / 360, credited before the open. Synthetic bills have no trading "
        "cost and no bid/ask, which slightly flatters every strategy that holds cash. Applies to all series, "
        "benchmarks included (their idle cash is only the few bp left after entry costs).")
    R.w("- **B1 (primary).** v1 B: each ETF has a fixed 1/16 sleeve, long when its close > SMA200 at the "
        "month-end close, else the sleeve is idle; held sleeves are rebalanced to 1/16. Idle sleeves earn the T-bill.")
    R.w("- **B2.** As B1, but at each month-end the idle sleeves go into IEF if IEF's close > its own SMA200, "
        "else T-bill. IEF trades pay 5 bp per side.")
    R.w("- **VT.** SPY exposure = min(1.0, 10% / realized vol), realized vol = stdev of the last 21 daily "
        "SPY AdjClose returns × √252, measured at each week's last close (Friday, or Thursday when Friday is a "
        "holiday) and traded at the next open; the rest earns the T-bill. No leverage.")
    R.w("- **BL.** Two sub-accounts, 50% B1 and 50% VT, each following its own rule and calendar; at each "
        "month-end close both are reset to 50% of total equity at the next open (each account trades back to "
        "its current target). Costs are charged per account with no netting between them (conservative).")
    R.w("- **Benchmarks.** SPY buy-and-hold and equal-weight buy-and-hold of the 16 ETFs (bought at each "
        "period's first open, never rebalanced — v1 convention), and 60/40 SPY/IEF rebalanced at each month-end "
        "(5 bp per trade). Each is bought fresh at the start of IS, of OOS, and of the full period.")
    R.w("- **Seatbelt test.** In BOTH IS and OOS: max drawdown no deeper than 50% of the benchmark's AND Sharpe "
        "≥ the benchmark's. Benchmark: EW buy-and-hold for B1, B2, BL; SPY buy-and-hold for VT.")
    R.w("- **60/40 test.** In BOTH IS and OOS: Sharpe AND CAGR/MaxDD both strictly above the 60/40's.")
    R.w("- **Labeled sensitivities (cannot rescue a failing config).** B1 and B2 with SMA 100 / 150 / 200; "
        "VT targets 8% / 10% / 12% × lookbacks 21 / 63 days; VT with monthly rebalance; VT with a 1.5x cap "
        "(borrowing at the T-bill, no spread — flatters it); B1 with idle cash in BIL instead of the synthetic "
        "bill (OOS only, BIL starts 2007-05-30); every test re-evaluated with Sharpe ex T-bill.")
    R.w("- **Trades.** \"Round trips\" = v1's definition (a position opened from zero and closed to zero, by "
        "entry date; open positions count). \"Fills\" = every order executed, rebalances included.")
    R.w("")

    # ---------------- tests
    R.sec("tests")
    R.w("## Pre-registered tests")
    R.w("")
    srows, frows, verdict = [], [], {}
    for s in ("B1", "B2", "VT", "BL"):
        bn = P.SEATBELT_BENCH[s]
        sb, sf = [], []
        for pn in P.PERIODS:
            m, bm, f = M[(s, pn)], M[(bn, pn)], M[("6040", pn)]
            o1 = P.seatbelt_ok(m, bm)
            o2 = P.sixty_forty_ok(m, f)
            sb.append(o1)
            sf.append(o2)
            srows.append([f"{s} {pn}", NAMES[bn], pct(m["MaxDD"]), pct(bm["MaxDD"]),
                          pct(P.SEATBELT_DD_FRAC * bm["MaxDD"]),
                          num(m["Sharpe"], 3), num(bm["Sharpe"], 3), yn(o1)])
            frows.append([f"{s} {pn}", num(m["Sharpe"], 3), num(f["Sharpe"], 3), num(m["MAR"], 3),
                          num(f["MAR"], 3), yn(o2)])
        verdict[s] = (all(sb), all(sf), sb, sf)
    R.w("### Verdicts")
    R.w("")
    R.table("verdict", ["Strategy", "Seatbelt IS", "Seatbelt OOS", "Seatbelt verdict",
                        "60/40 IS", "60/40 OOS", "60/40 verdict"],
            [[s, yn(v[2][0]), yn(v[2][1]), f"**{yn(v[0])}**", yn(v[3][0]), yn(v[3][1]), f"**{yn(v[1])}**"]
             for s, v in verdict.items()])
    R.w("")
    R.w("### Seatbelt test detail")
    R.w("")
    R.table("seatbelt", ["Strategy / period", "Benchmark", "Strategy MaxDD", "Benchmark MaxDD",
                         "Limit (50% of benchmark DD)", "Strategy Sharpe", "Benchmark Sharpe", "Result"], srows)
    R.w("")
    R.w("### 60/40 test detail")
    R.w("")
    R.table("t6040", ["Strategy / period", "Strategy Sharpe", "60/40 Sharpe", "Strategy CAGR/MaxDD",
                      "60/40 CAGR/MaxDD", "Result"], frows)
    R.w("")

    # ---------------- metrics per period
    R.sec("metrics")
    keys = ["B0", "B1", "B2", "VT", "BL", "SPY", "EW", "6040"]
    for pn in ALLP:
        R.w(f"## {pn}" + (" (information only)" if pn == PN_FULL else ""))
        R.w("")
        R.table(f"m_{pn.split()[0]}", MCOLS, [mrow(NAMES[k], M[(k, pn)]) for k in keys])
        R.w("")
    R.w(f"VT row = pre-registered 10% target, 21-day lookback, weekly, cap 1.0. Avg exposure = average weight "
        "in ETFs (IEF included); the rest is in T-bills.")
    R.w("")

    # ---------------- cash effect
    R.sec("cash")
    R.w("## Cash effect: B1 vs v1 B")
    R.w("")
    R.w("Gap = EW buy-and-hold CAGR minus strategy CAGR, in percentage points. \"Closed\" = how much of v1 B's "
        "gap disappears when the same positions' idle sleeves earn the T-bill (B1 and v1 B hold identical ETF "
        "positions; only the cash rate differs).")
    R.w("")
    crows = []
    for pn, (a, b) in ALLP.items():
        ew, b0m, b1m = M[("EW", pn)]["CAGR"], M[("B0", pn)]["CAGR"], M[("B1", pn)]["CAGR"]
        g0, g1 = ew - b0m, ew - b1m
        bm = v1.metrics(bill["eq"], None, None, a, b)
        crows.append([pn, pct(ew), pct(b0m), pct(b1m), pts(g0), pts(g1), pts(g0 - g1),
                      pct((g0 - g1) / g0, 0) if g0 > 0 else "— (no gap)",
                      pct(1 - M[("B1", pn)]["Exposure"], 0), pct(bm["CAGR"])])
    R.table("cash", ["Period", "EW B&H CAGR", "v1 B CAGR", "B1 CAGR", "Gap v1 B (pts)", "Gap B1 (pts)",
                     "Closed (pts)", "Closed (share of v1 gap)", "B1 avg idle", "T-bill CAGR"], crows)
    R.w("")

    # ---------------- grids
    R.sec("grids")
    grid_rows = []

    def tests_for(m_is, m_oos, bn):
        sb = [P.seatbelt_ok(m_is, M[(bn, PN_IS)]), P.seatbelt_ok(m_oos, M[(bn, PN_OOS)])]
        sf = [P.sixty_forty_ok(m_is, M[("6040", PN_IS)]), P.sixty_forty_ok(m_oos, M[("6040", PN_OOS)])]
        return sb, sf

    def flag(r):
        return {(True, True): "pass both", (False, True): "OOS only", (True, False): "IS only",
                (False, False): "fail both"}[tuple(r)]

    GH = ["Cell", "IS CAGR", "IS Sharpe", "IS MaxDD", "IS CAGR/MaxDD", "OOS CAGR", "OOS Sharpe",
          "OOS MaxDD", "OOS CAGR/MaxDD", "Seatbelt", "60/40"]

    def grow(label, run, bn, key):
        mi, mo = P.metrics(run, *P.PERIODS[PN_IS]), P.metrics(run, *P.PERIODS[PN_OOS])
        sb, sf = tests_for(mi, mo, bn)
        for pn, m in ((PN_IS, mi), (PN_OOS, mo)):
            grid_rows.append(dict(strategy=key, cell=label, period=pn, **m))
        return [label, pct(mi["CAGR"]), num(mi["Sharpe"]), pct(mi["MaxDD"]), num(mi["MAR"]),
                pct(mo["CAGR"]), num(mo["Sharpe"]), pct(mo["MaxDD"]), num(mo["MAR"]), flag(sb), flag(sf)]

    R.w("## Sensitivity grids (labeled; ★ = pre-registered; never rescue a failing config)")
    R.w("")
    R.w("Seatbelt / 60/40 columns: \"pass both\", \"IS only\", \"OOS only\" or \"fail both\" for that cell "
        "against the same benchmarks as the pre-registered tests.")
    R.w("")
    R.w("### B1 / B2 — SMA length")
    R.w("")
    brows = []
    for safe, key in ((False, "B1"), (True, "B2")):
        for n in P.GRID_B_SMA:
            pre = n == P.PRE_B["sma"]
            run = runs[key] if pre else P.run_B(AC, AO, rb, n, safe)
            brows.append(grow(f"{key} SMA{n}{' ★' if pre else ''}", run, "EW", key))
    R.table("grid_b", GH, brows)
    R.w("")
    R.w("### VT — target × lookback, and labeled variants")
    R.w("")
    vrows = []
    for t, lk in P.GRID_VT:
        pre = (t, lk) == (P.PRE_VT["target"], P.PRE_VT["look"])
        run = runs["VT"] if pre else P.run_VT(AC, AO, rb, t, lk, 1.0, "W")
        vrows.append(grow(f"VT {t*100:.0f}% / {lk}d{' ★' if pre else ''}", run, "SPY", "VT"))
    vt_sens = {}
    for lab, cfg in P.SENS_VT:
        run = P.run_VT(AC, AO, rb, **cfg)
        vt_sens[lab] = run
        vrows.append(grow(f"VT 10% / 21d, {lab} (sensitivity)", run, "SPY", "VT"))
    R.table("grid_vt", GH, vrows)
    R.w("")
    cap = vt_sens[P.SENS_VT[1][0]]
    R.table("vt_cap", ["Series", "IS avg exposure", "OOS avg exposure", "Max exposure"],
            [["VT ★ (cap 1.0)", pct(M[("VT", PN_IS)]["Exposure"], 0), pct(M[("VT", PN_OOS)]["Exposure"], 0),
              pct(runs["VT"]["exp"].max(), 0)],
             ["VT cap 1.5 (sensitivity)", pct(cap["exp"].loc[slice(*P.PERIODS[PN_IS])].mean(), 0),
              pct(cap["exp"].loc[slice(*P.PERIODS[PN_OOS])].mean(), 0), pct(cap["exp"].max(), 0)]])
    R.w("")

    # BIL sensitivity (OOS only)
    R.w("### B1 with idle cash in BIL (OOS only, labeled sensitivity)")
    R.w("")
    try:
        bil = etf_data.load("BIL", refresh=True)
        rbil = bil["AdjClose"].reindex(idx).pct_change()
        rb_bil = rbil.where(rbil.notna() & (idx >= bil.index[0] + pd.Timedelta(days=1)), rb)
        b1b = P.run_B(AC, AO, rb_bil, P.PRE_B["sma"], safe=False)
        a, b = P.PERIODS[PN_OOS]
        mb = P.metrics(b1b, a, b)
        bm_bil = v1.metrics(bill_run(rb_bil)["eq"], None, None, a, b)
        bm_irx = v1.metrics(bill["eq"], None, None, a, b)
        R.table("bil", ["Series (OOS)", "CAGR", "Sharpe", "MaxDD", "CAGR/MaxDD", "Cash-leg CAGR"],
                [["B1 ★ (synthetic ^IRX bill)", pct(M[("B1", PN_OOS)]["CAGR"]), num(M[("B1", PN_OOS)]["Sharpe"]),
                  pct(M[("B1", PN_OOS)]["MaxDD"]), num(M[("B1", PN_OOS)]["MAR"]), pct(bm_irx["CAGR"])],
                 ["B1, idle cash in BIL (sensitivity)", pct(mb["CAGR"]), num(mb["Sharpe"]), pct(mb["MaxDD"]),
                  num(mb["MAR"]), pct(bm_bil["CAGR"])]])
        R.w("")
        R.w(f"BIL first bar {bil.index[0].date()}; BIL fills are not charged the 5 bp cost in this "
            "sensitivity (only its expense ratio, which is inside its total return).")
    except etf_data.TransportError as e:
        R.w(f"BIL sensitivity not run — transport error (not a data finding): `{e}`")
    R.w("")

    # excess-Sharpe sensitivity of the tests
    R.w("### Tests re-evaluated with Sharpe ex T-bill (labeled sensitivity)")
    R.w("")
    xrows = []
    for s in ("B1", "B2", "VT", "BL"):
        bn = P.SEATBELT_BENCH[s]
        sb = [P.seatbelt_ok(M[(s, pn)], M[(bn, pn)], "ExSharpe") for pn in P.PERIODS]
        sf = [P.sixty_forty_ok(M[(s, pn)], M[("6040", pn)], "ExSharpe") for pn in P.PERIODS]
        xrows.append([s, NAMES[bn], num(M[(s, PN_IS)]["ExSharpe"], 3), num(M[(bn, PN_IS)]["ExSharpe"], 3),
                      num(M[("6040", PN_IS)]["ExSharpe"], 3),
                      num(M[(s, PN_OOS)]["ExSharpe"], 3), num(M[(bn, PN_OOS)]["ExSharpe"], 3),
                      num(M[("6040", PN_OOS)]["ExSharpe"], 3), flag(sb), flag(sf)])
    R.table("exsharpe", ["Strategy", "Seatbelt benchmark", "IS Sharpe ex", "IS bench Sharpe ex",
                         "IS 60/40 Sharpe ex", "OOS Sharpe ex", "OOS bench Sharpe ex", "OOS 60/40 Sharpe ex",
                         "Seatbelt (ex)", "60/40 (ex)"], xrows)
    R.w("")
    R.w("Drawdown and CAGR/MaxDD sides of both tests are unchanged by the Sharpe convention; only the Sharpe "
        "comparisons are re-done here.")
    R.w("")
    pd.DataFrame(grid_rows).to_csv(GRID_PATH, index=False)

    # ---------------- calendar years
    R.sec("years")
    R.w("## Calendar-year returns (all series from 2006-01-03; benchmarks bought then)")
    R.w("")
    series = {"v1 B": runs["B0"]["eq"], "B1": runs["B1"]["eq"], "B2": runs["B2"]["eq"],
              "VT": runs["VT"]["eq"], "BL": runs["BL"]["eq"], "SPY": bench[PN_FULL]["SPY"]["eq"],
              "EW B&H": bench[PN_FULL]["EW"]["eq"], "60/40": bench[PN_FULL]["6040"]["eq"],
              "T-bill": bill["eq"]}
    yt = v1.year_table(series)
    R.table("years", ["Year"] + list(yt.columns),
            [[f"{y} (YTD)" if y == last.year else str(y)] + [pct(v) for v in r.values] for y, r in yt.iterrows()])
    R.w("")

    # ---------------- stress windows
    R.sec("stress")
    R.w("## Stress windows: 2008, 2020, 2022")
    R.w("")
    wins = [("2008 calendar year", "2008-01-01", "2008-12-31"),
            ("GFC SPY peak to trough 2007-10-09 to 2009-03-09", "2007-10-10", "2009-03-09"),
            ("2020 calendar year", "2020-01-01", "2020-12-31"),
            ("COVID crash 2020-02-19 to 2020-03-23", "2020-02-20", "2020-03-23"),
            ("2022 calendar year", "2022-01-01", "2022-12-31")]
    sser = {k: v for k, v in series.items() if k != "T-bill"}
    R.w("Each cell: window return / max drawdown inside the window.")
    R.w("")
    R.table("stress", ["Window"] + list(sser),
            [[lab] + ["{} / {}".format(*map(pct, v1.window_stats(eq, a, b))) for eq in sser.values()]
             for lab, a, b in wins])
    R.w("")
    R.w("Average exposure inside each window (ETF weight; for B2 IEF included):")
    R.w("")
    ex = {"v1 B": runs["B0"]["exp"], "B1": runs["B1"]["exp"], "B2": runs["B2"]["exp"],
          "B2 IEF part": runs["B2"]["safe_exp"], "VT": runs["VT"]["exp"], "BL": runs["BL"]["exp"]}
    R.table("stress_exp", ["Window"] + list(ex),
            [[lab] + [pct(e.loc[a:b].mean(), 0) for e in ex.values()] for lab, a, b in wins])
    R.w("")

    # ---------------- limitations / files
    R.sec("limits")
    R.w("## Limitations")
    R.w("")
    R.w("- **Hindsight ETF universe.** The 16 ETFs were picked today; all survived and stayed liquid. That "
        "flatters every strategy and the equal-weight benchmark.")
    R.w("- **Synthetic T-bill with no trading cost.** Idle cash earns ^IRX (a discount-basis yield used as a "
        "simple rate, actual/360) with no cost, bid/ask, or lag. It is a slight overstatement of what a "
        "real T-bill ETF or sweep would have paid; the BIL sensitivity shows the size of the gap in OOS.")
    R.w("- **Start dates.** IEF has data from 2004 (checked from 2005-01-03); BIL only from 2007-05-30, so "
        "BIL can only be an OOS sensitivity. ^IRX had missing days that were forward-filled (count in Gate 0).")
    R.w("- **2008 is the only deep bear in IS.** The seatbelt test's IS drawdown side rests mainly on one episode; "
        "OOS adds the fast 2020 crash and the 2022 stock-and-bond bear.")
    R.w("- **PEAD correlation is not measurable.** The repo holds trade-level PEAD results (2022 onward), not a "
        "daily return series over 2006 to now, so the diversification value against the live PEAD book is unknown.")
    R.w("- **Second round of tests on the same data.** v1 already tested B, its grid and two other strategies on "
        "exactly these prices and periods; v2 adds four configs, a grid and several sensitivities. Every additional "
        "test raises the chance that something passes by luck, and the OOS period has now been looked at twice — "
        "it is no longer a clean holdout for anything derived from v1's results.")
    R.w("- Sharpe uses rf = 0 (v1 convention). That favours cash-heavy series now that cash earns interest; the "
        "Sharpe ex T-bill columns and the re-evaluated tests show whether any verdict depends on it.")
    R.w("- BL charges costs per sub-account without netting; VT's 1.5x-cap variant borrows at the T-bill with no "
        "spread. Taxes and intra-month drift costs are not modelled. Fills at the open assume no slippage beyond 5 bp.")
    R.w("")
    R.w("## Files")
    R.w("")
    R.w("- `backtesting/scripts/etf_trend_v2_prereg.py` — pre-registered definitions, tests, grids, engine.")
    R.w("- `backtesting/scripts/backtest_etf_trend_v2.py` — this runner; `etf_data.py` — loader and Gate 0.")
    R.w("- `backtesting/scripts/check_etf_trend_v2_report.py` — prose-vs-table number checker.")
    R.w(f"- `backtesting/reports/etf_trend_v2_grid_{TODAY}.csv`, `backtesting/reports/etf_trend_v2_claims_{TODAY}.json`.")
    R.w("")

    ctx = dict(M=M, verdict=verdict, last=last)
    write_prose(R, ctx)
    order = ["head", "summary", "gate0", "defs", "tests", "metrics", "cash", "grids", "years",
             "stress", "interp", "limits"]
    return R, order, ctx


# --------------------------------------------------------------------------
# summary + interpretation: every number via R.q()
# --------------------------------------------------------------------------
def write_prose(R, ctx):
    q = R.q
    last = ctx["last"]
    R.sec("head")
    R.w(f"# ETF trend backtest v2 — {TODAY}")
    R.w("")
    R.w("Research only. No change to `memory/strategy.md`, no orders, no live routine touched. "
        "Follows `backtesting/etf_trend_backtest_2026-10-15.md` (v1).")
    R.w("")
    R.w(f"Data through **{last}** (last completed daily bar). IS = 2006-01-03 to 2017-12-29, "
        f"OOS = 2018-01-02 to {last}.")
    R.w("")
    R.sec("summary")
    R.w("## Summary")
    R.w("")
    R.w("_Pre-registered verdicts (the full table, with per-period results, is under \"Pre-registered tests\")._")
    R.w("")
    v = ctx["verdict"]
    sb = [s for s in v if v[s][0]]
    sf = [s for s in v if v[s][1]]
    R.p("- **Seatbelt test passed by:** " + (", ".join(sb) if sb else "**none**") +
        ". **60/40 test passed by:** " + (", ".join(sf) if sf else "**none**") + ".")
    write_findings(R, ctx)


def write_findings(R, ctx):
    """Post-hoc commentary, written after reading the first full run's tables.
    Numbers only via R.q(); result-dependent words are computed from ctx/tables."""
    q, M, v = R.q, ctx["M"], ctx["verdict"]
    IS_, OOS_ = PN_IS, PN_OOS
    xh, xr = R.tables["exsharpe"]
    xflag = {r[0]: (r[xh.index("Seatbelt (ex)")], r[xh.index("60/40 (ex)")]) for r in xr}
    both_ex = [k for k, (a, b) in xflag.items() if a == "pass both" and b == "pass both"]
    lose_ex = [k for k in xflag if v[k][0] and xflag[k][0] != "pass both"]

    def andj(xs):
        return ", ".join(xs[:-1]) + (" and " if len(xs) > 1 else "") + xs[-1] if xs else "none"

    # ---------------- summary bullets
    R.sec("summary")
    R.p(f"- **B1 (primary): idle sleeves earning the T-bill.** Seatbelt: max drawdown "
        f"{q('seatbelt', 'B1 ' + IS_, 'Strategy MaxDD')} vs EW buy-and-hold "
        f"{q('seatbelt', 'B1 ' + IS_, 'Benchmark MaxDD')} in IS and {q('seatbelt', 'B1 ' + OOS_, 'Strategy MaxDD')} vs "
        f"{q('seatbelt', 'B1 ' + OOS_, 'Benchmark MaxDD')} in OOS; Sharpe {q('seatbelt', 'B1 ' + IS_, 'Strategy Sharpe')} vs "
        f"{q('seatbelt', 'B1 ' + IS_, 'Benchmark Sharpe')} in IS and {q('seatbelt', 'B1 ' + OOS_, 'Strategy Sharpe')} vs "
        f"{q('seatbelt', 'B1 ' + OOS_, 'Benchmark Sharpe')} in OOS. Against 60/40 in OOS: Sharpe "
        f"{q('t6040', 'B1 ' + OOS_, 'Strategy Sharpe')} vs {q('t6040', 'B1 ' + OOS_, '60/40 Sharpe')}, CAGR/MaxDD "
        f"{q('t6040', 'B1 ' + OOS_, 'Strategy CAGR/MaxDD')} vs {q('t6040', 'B1 ' + OOS_, '60/40 CAGR/MaxDD')}. "
        f"It is still a lower-return series: OOS CAGR {q('m_OOS', NAMES['B1'], 'CAGR')} vs "
        f"{q('m_OOS', NAMES['EW'], 'CAGR')} for EW buy-and-hold and {q('m_OOS', NAMES['SPY'], 'CAGR')} for SPY.")
    R.p(f"- **The Sharpe convention matters.** The pre-registered tests use Sharpe with rf = 0, as in v1. "
        f"Now that idle cash earns interest, that convention gives cash-heavy series credit for the T-bill "
        f"itself. Measured in excess of the T-bill (a labeled sensitivity), B1's OOS Sharpe is "
        f"{q('exsharpe', 'B1', 'OOS Sharpe ex')} vs EW buy-and-hold's {q('exsharpe', 'B1', 'OOS bench Sharpe ex')}. "
        f"Seatbelt passes that do not survive the excess-return Sharpe: {andj(lose_ex)}. Configs that pass both "
        f"tests in both periods under both conventions: {andj(both_ex)}. Read the other seatbelt passes "
        f"as marginal on Sharpe and clear on drawdown.")
    R.p(f"- **Cash effect.** Paying T-bill interest on the same positions closes "
        f"{q('cash', OOS_, 'Closed (pts)')} of v1 B's {q('cash', OOS_, 'Gap v1 B (pts)')}-point OOS CAGR gap to EW "
        f"buy-and-hold ({q('cash', OOS_, 'Closed (share of v1 gap)')} of it). In IS it closes "
        f"{q('cash', IS_, 'Closed (pts)')} of {q('cash', IS_, 'Gap v1 B (pts)')} points "
        f"({q('cash', IS_, 'Closed (share of v1 gap)')}). The remaining "
        f"{q('cash', OOS_, 'Gap B1 (pts)')} points in OOS come from being out of the market while it rose, not "
        f"from idle cash earning nothing.")
    R.p(f"- **B2 (IEF rotation)** helped mostly in IS: 2008 {q('years', '2008', 'B2')} vs "
        f"{q('years', '2008', 'B1')} for B1, IS CAGR {q('m_IS', NAMES['B2'], 'CAGR')} vs "
        f"{q('m_IS', NAMES['B1'], 'CAGR')}. In OOS it adds little: CAGR {q('m_OOS', NAMES['B2'], 'CAGR')} vs "
        f"{q('m_OOS', NAMES['B1'], 'CAGR')}, MaxDD {q('m_OOS', NAMES['B2'], 'MaxDD')} vs "
        f"{q('m_OOS', NAMES['B1'], 'MaxDD')}. In 2022 its average IEF weight was "
        f"{q('stress_exp', '2022 calendar year', 'B2 IEF part')}: IEF was below its own SMA200, so the "
        f"rotation sat in bills.")
    R.p(f"- **VT** {'passes' if v['VT'][0] else 'fails'} the seatbelt test against SPY "
        f"(MaxDD {q('seatbelt', 'VT ' + IS_, 'Strategy MaxDD')} vs {q('seatbelt', 'VT ' + IS_, 'Benchmark MaxDD')} IS, "
        f"{q('seatbelt', 'VT ' + OOS_, 'Strategy MaxDD')} vs {q('seatbelt', 'VT ' + OOS_, 'Benchmark MaxDD')} OOS) and "
        f"{'passes' if v['VT'][1] else 'fails'} the 60/40 test: in IS its Sharpe is "
        f"{q('t6040', 'VT ' + IS_, 'Strategy Sharpe')} vs {q('t6040', 'VT ' + IS_, '60/40 Sharpe')}. "
        f"Its weakness is the GFC: {q('stress', 'GFC SPY peak to trough 2007-10-09 to 2009-03-09', 'VT')} "
        f"(return / max DD), consistent with a 21-day vol estimate that cuts exposure only after volatility "
        f"has already risen.")
    R.p(f"- **BL (50% B1 + 50% VT)** {'passes' if v['BL'][0] and v['BL'][1] else 'does not pass'} both "
        f"pre-registered tests: OOS Sharpe {q('t6040', 'BL ' + OOS_, 'Strategy Sharpe')} vs 60/40 "
        f"{q('t6040', 'BL ' + OOS_, '60/40 Sharpe')} and EW {q('seatbelt', 'BL ' + OOS_, 'Benchmark Sharpe')}, "
        f"OOS MaxDD {q('seatbelt', 'BL ' + OOS_, 'Strategy MaxDD')} against a limit of "
        f"{q('seatbelt', 'BL ' + OOS_, 'Limit (50% of benchmark DD)')}. With Sharpe ex T-bill its seatbelt result is "
        f"\"{xflag['BL'][0]}\" and its 60/40 result \"{xflag['BL'][1]}\".")
    R.p(f"- **Nothing here is a return enhancer.** Best pre-registered OOS CAGR is "
        f"{q('m_OOS', NAMES[max(('B1', 'B2', 'VT', 'BL'), key=lambda k: M[(k, OOS_)]['CAGR'])], 'CAGR')} "
        f"vs SPY's {q('m_OOS', NAMES['SPY'], 'CAGR')}. The tests reward lower drawdown at a similar or "
        f"slightly better Sharpe; that is what passed.")

    # ---------------- result-dependent words for the interpretation
    gh, gr = R.tables["grid_vt"]
    gcell = {r[0]: r for r in gr}
    vt63_fail = [c.replace("VT ", "") for c in gcell if "/ 63d" in c
                 and gcell[c][gh.index("Seatbelt")] in ("IS only", "fail both")]
    vt_pass = [c.replace("VT ", "") for c in gcell if gcell[c][gh.index("Seatbelt")] == "pass both"
               and gcell[c][gh.index("60/40")] == "pass both"]
    cap_worse = (float(gcell["VT 10% / 21d, 1.5x exposure cap (sensitivity)"][gh.index("OOS Sharpe")])
                 <= float(gcell["VT 10% / 21d ★"][gh.index("OOS Sharpe")]))
    bh, br = R.tables["bil"]
    bil_less = float(br[1][bh.index("Cash-leg CAGR")].rstrip("%")) < float(br[0][bh.index("Cash-leg CAGR")].rstrip("%"))
    sh_, sr_ = R.tables["stress"]
    ddv = lambda row, col: float(next(r for r in sr_ if r[0] == row)[sh_.index(col)].split(" / ")[1].rstrip("%"))
    dd_half = all(abs(ddv(w_, "B1")) < 0.5 * abs(ddv(w_, "EW B&H"))
                  for w_ in ("2008 calendar year", "2020 calendar year", "2022 calendar year"))

    # qualitative claims below are asserted so a re-run on new data fails loudly
    bgh, bgr = R.tables["grid_b"]
    bcell = {r[0]: (r[bgh.index("Seatbelt")], r[bgh.index("60/40")]) for r in bgr}
    assert all(bcell[f"{k} SMA100"] == ("IS only", "IS only") for k in ("B1", "B2")), bcell
    assert all(bcell[f"{k} SMA150"] == bcell[f"{k} SMA200 ★"] for k in ("B1", "B2")), bcell
    assert M[("EW", PN_FULL)]["CAGR"] - M[("B0", PN_FULL)]["CAGR"] - (
        M[("EW", PN_FULL)]["CAGR"] - M[("B1", PN_FULL)]["CAGR"]) < 0.01

    # ---------------- interpretation
    R.sec("interp")
    R.w("## Interpretation (post-hoc)")
    R.w("")
    R.w("Written after reading the tables. It does not change any definition, test or verdict.")
    R.w("")
    R.p(f"- **The passes rest mainly on drawdown.** The 60/40 test is passed on CAGR/MaxDD by a wide margin "
        f"(B1 OOS {q('t6040', 'B1 ' + OOS_, 'Strategy CAGR/MaxDD')} vs {q('t6040', 'B1 ' + OOS_, '60/40 CAGR/MaxDD')}) "
        f"but on Sharpe by a thin one ({q('t6040', 'B1 ' + OOS_, 'Strategy Sharpe')} vs "
        f"{q('t6040', 'B1 ' + OOS_, '60/40 Sharpe')}), and the Sharpe side flips for some configs once the "
        f"T-bill is subtracted. The robust finding is the same as v1's: the trend filter kept B1's drawdowns "
        f"{'to less than half' if dd_half else 'below'} of EW buy-and-hold's in 2008, 2020 and 2022 "
        f"(2022: B1 {q('stress', '2022 calendar year', 'B1')} vs EW {q('stress', '2022 calendar year', 'EW B&H')}).")
    R.p(f"- **T-bill interest is a modest correction, not the missing return.** Over the full period the "
        f"T-bill compounded at {q('cash', PN_FULL, 'T-bill CAGR')} a year and B1 was idle "
        f"{q('cash', PN_FULL, 'B1 avg idle')} of the time on average, so the cash effect is a fraction of a "
        f"point per year (full-period gap closed: {q('cash', PN_FULL, 'Closed (pts)')} points). The years "
        f"it mattered are the high-rate ones: 2023 B1 {q('years', '2023', 'B1')} vs v1 B "
        f"{q('years', '2023', 'v1 B')}. The BIL sensitivity shows a real T-bill ETF would have paid "
        f"{'less' if bil_less else 'at least as much as'} than the synthetic bill in OOS ({q('bil', 'B1, idle cash in BIL (sensitivity)', 'Cash-leg CAGR')} "
        f"vs {q('bil', 'B1 ★ (synthetic ^IRX bill)', 'Cash-leg CAGR')}), with B1's OOS CAGR "
        f"{q('bil', 'B1, idle cash in BIL (sensitivity)', 'CAGR')} instead of "
        f"{q('bil', 'B1 ★ (synthetic ^IRX bill)', 'CAGR')}.")
    R.p(f"- **Grids.** The SMA100 cells of B1 and B2 pass IS only and decay in OOS (B1 SMA100 OOS CAGR "
        f"{q('grid_b', 'B1 SMA100', 'OOS CAGR')}); the SMA150 cells have the same verdicts as SMA200. "
        f"VT is sensitive to its lookback: 63-day cells failing the seatbelt test in OOS: "
        f"{andj(vt63_fail) if vt63_fail else 'none'} (e.g. 10% / 63d OOS MaxDD "
        f"{q('grid_vt', 'VT 10% / 63d', 'OOS MaxDD')}). The 1.5x cap {'does not improve' if cap_worse else 'improves'} the "
        f"OOS Sharpe ({q('grid_vt', 'VT 10% / 21d, 1.5x exposure cap (sensitivity)', 'OOS Sharpe')} vs "
        f"{q('grid_vt', 'VT 10% / 21d ★', 'OOS Sharpe')}). VT cells that pass both tests in both periods: "
        f"{andj(vt_pass) if vt_pass else 'none'}; per the rules they do not rescue the pre-registered VT.")
    R.p(f"- **What this does and does not support.** A month-end SMA200 trend sleeve with cash in T-bills is "
        f"a defensible drawdown-control sleeve: about {q('m_Full', NAMES['B1'], 'CAGR')} a year over the full "
        f"period at a worst drawdown of {q('m_Full', NAMES['B1'], 'MaxDD')}. It does not beat SPY or the EW "
        f"basket on return, and its edge over 60/40 on risk-adjusted terms is small. BL is the only config that "
        f"{'passes everything under both Sharpe conventions' if 'BL' in both_ex and len(both_ex) == 1 else 'is listed above under both conventions'}, "
        f"but it is the most tested idea in the set (it combines two other tested configs), and this is the "
        f"second round of tests on the same data. None of this is a recommendation to change the live PEAD "
        f"strategy, which this repo cannot correlate against these series.")
    R.w("")


if __name__ == "__main__":
    R, order, ctx = main()
    with open(REPORT_PATH, "w") as f:
        f.write(R.text(order))
    with open(CLAIMS_PATH, "w") as f:
        json.dump(R.claims, f, indent=1, ensure_ascii=False)
    print("wrote", REPORT_PATH)
    if ctx is None:
        sys.exit(1)
