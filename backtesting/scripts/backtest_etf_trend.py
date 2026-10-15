"""
ETF swing / trend backtest -- research only.

Strategies (pre-registered configs marked *):
  A. Pullback in uptrend (per-ETF, max 5 concurrent, 20% of equity per slot)
       entry : close > SMA200 and SMA50 > SMA200 and close <= SMA20 and RSI(2) < th
       exit  : close > SMA5, or held T trading days, or close <= entry * 0.92
       grid  : th in {5, 10*, 15} x T in {5, 10*, 15}
  B. Time-series trend: 1/16 sleeve per ETF, long when close > SMA(n) at the
     month-end check, else that sleeve is cash.   grid: n in {100, 150, 200*}
     (+ labelled sensitivity: 1/k weighting across the k qualifiers)
  C. Cross-sectional momentum: monthly, rank by (L-1)-month return, hold top N
     at 1/N each, a slot is cash if its ETF is below SMA200.
       grid  : L-1 in {6-1, 9-1, 12-1*} x N in {3*, 5}

Mechanics: signals on adjusted close (total return) through close t; fills at
the open of t+1. The fill price is Yahoo's (split-adjusted, not dividend-
adjusted) open, converted to the total-return basis with the same-day
AdjClose/Close factor so fills and marks share one price basis. 5 bp per side.
Daily mark-to-market on AdjClose. Cash earns 0%.

Split (pre-registered): IS 2006-01-01..2017-12-31, OOS 2018-01-01..latest.
Every strategy runs continuously from the first trading day of 2006 and is
sliced into IS / OOS; benchmarks are bought fresh at each period's start.
"""

import os
import sys
from datetime import date

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etf_data  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backtesting/
REPORTS_DIR = os.path.join(HERE, "reports")
TODAY = date.today().isoformat()
REPORT_PATH = os.path.join(HERE, f"etf_trend_backtest_{TODAY}.md")

COST = 0.0005
SIM_START = "2006-01-01"
IS = ("2006-01-01", "2017-12-31")
OOS = ("2018-01-01", "2100-01-01")
PERIODS = {"IS 2006-2017": IS, "OOS 2018-latest": OOS}
N_RANDOM = 200
RNG_SEED = 20261015

PRE_A = dict(rsi=10, tstop=10)
PRE_B = dict(sma=200, weighting="sleeve")
PRE_C = dict(look=12, n=3)


# --------------------------------------------------------------------------
# data panels
# --------------------------------------------------------------------------
def build_panels(data):
    idx = data["SPY"].index
    AC = pd.DataFrame({t: d["AdjClose"] for t, d in data.items()}).reindex(idx)
    C = pd.DataFrame({t: d["Close"] for t, d in data.items()}).reindex(idx)
    O = pd.DataFrame({t: d["Open"] for t, d in data.items()}).reindex(idx)
    AO = O * AC / C  # open on the total-return basis
    AC = AC[etf_data.UNIVERSE]
    AO = AO[etf_data.UNIVERSE]
    return AC, AO


def rsi_wilder(s, n=2):
    d = s.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)


# --------------------------------------------------------------------------
# Strategy A + random control: slot simulator
# --------------------------------------------------------------------------
def sim_slots(AC, AO, start, entry_fn=None, exit_fn=None, planned=None,
              slots=5, ind=None):
    """Daily loop. Either (entry_fn, exit_fn) signal-driven, or `planned` =
    list of (entry_i, exit_i, ticker) with fills at those day indexes.
    Returns (equity Series, exposure Series, trades DataFrame)."""
    dates = AC.index
    i0 = dates.searchsorted(pd.Timestamp(start))
    ac = AC.values
    ao = AO.values
    tick = list(AC.columns)
    cash, eq_prev = 1.0, 1.0
    pos = {}  # j -> dict(sh, px, ei)
    pend_buy, pend_sell = [], []
    eqs, exps, trades = [], [], []
    plan_in, plan_out = {}, {}
    if planned is not None:
        for (ei, xi, t) in planned:
            j = tick.index(t)
            plan_in.setdefault(ei, []).append(j)
            plan_out.setdefault(xi, []).append(j)
    for i in range(i0, len(dates)):
        # ---- fills at the open of day i
        sells = pend_sell if planned is None else [j for j in plan_out.get(i, []) if j in pos]
        for j in sells:
            p = pos.pop(j)
            px = ao[i, j] * (1 - COST)
            cash += p["sh"] * px
            trades.append(dict(ticker=tick[j], entry=dates[p["ei"]], exit=dates[i],
                               days=i - p["ei"],
                               ret=px / (p["px"] * (1 + COST)) - 1,
                               pnl=p["sh"] * (px - p["px"] * (1 + COST))))
        buys = pend_buy if planned is None else plan_in.get(i, [])
        for j in buys:
            if j in pos or len(pos) >= slots or np.isnan(ao[i, j]):
                continue
            val = min(eq_prev / slots, cash)
            if val <= 0:
                continue
            fill = ao[i, j] * (1 + COST)
            pos[j] = dict(sh=val / fill, px=ao[i, j], ei=i)
            cash -= val
        # ---- mark at close
        inv = sum(p["sh"] * ac[i, j] for j, p in pos.items())
        eq = cash + inv
        eqs.append(eq)
        exps.append(inv / eq)
        eq_prev = eq
        # ---- signals at close i for the open of i+1
        if planned is None:
            pend_sell = [j for j, p in pos.items() if exit_fn(i, j, p)]
            free = slots - len(pos) + len(pend_sell)
            cands = entry_fn(i, set(pos) | set(pend_sell))
            pend_buy = cands[:max(free, 0)]
    # open positions at the end are closed at the last close for trade stats
    for j, p in pos.items():
        trades.append(dict(ticker=tick[j], entry=dates[p["ei"]], exit=dates[-1],
                           days=len(dates) - 1 - p["ei"],
                           ret=ac[-1, j] * (1 - COST) / (p["px"] * (1 + COST)) - 1,
                           pnl=p["sh"] * (ac[-1, j] * (1 - COST) - p["px"] * (1 + COST)),
                           open=True))
    out_idx = dates[i0:]
    return (pd.Series(eqs, out_idx), pd.Series(exps, out_idx),
            pd.DataFrame(trades))


def strat_A(AC, AO, rsi_th=10, tstop=10, stop=0.08):
    sma200 = AC.rolling(200).mean().values
    sma50 = AC.rolling(50).mean().values
    sma20 = AC.rolling(20).mean().values
    sma5 = AC.rolling(5).mean().values
    rsi = AC.apply(rsi_wilder).values
    ac = AC.values
    sig = ((ac > sma200) & (sma50 > sma200) & (ac <= sma20) & (rsi < rsi_th))

    def entry_fn(i, held):
        js = [j for j in np.flatnonzero(sig[i]) if j not in held]
        return sorted(js, key=lambda j: rsi[i, j])  # most oversold first

    def exit_fn(i, j, p):
        return (ac[i, j] > sma5[i, j]
                or (i - p["ei"] + 1) >= tstop
                or ac[i, j] <= p["px"] * (1 - stop))

    return sim_slots(AC, AO, SIM_START, entry_fn, exit_fn)


def random_control(AC, AO, trades, n_sims, seed):
    """Random-entry control matched to A: same number of trades per period,
    same holding-period draws, same 20% slot sizing and 5-slot cap; entry
    date and ETF drawn uniformly at random within the trade's period."""
    rng = np.random.default_rng(seed)
    dates = AC.index
    i0 = dates.searchsorted(pd.Timestamp(SIM_START))
    n = len(dates)
    tick = list(AC.columns)
    bounds = {}
    for name, (a, b) in PERIODS.items():
        bounds[name] = (max(i0, dates.searchsorted(pd.Timestamp(a))),
                        dates.searchsorted(pd.Timestamp(b), side="right") - 1)
    tr = trades[~trades.get("open", pd.Series(False, index=trades.index)).fillna(False).astype(bool)]
    specs = []
    for _, t in tr.iterrows():
        per = "IS 2006-2017" if t["entry"] <= pd.Timestamp(IS[1]) else "OOS 2018-latest"
        specs.append((per, int(t["days"])))
    results = []
    for s in range(n_sims):
        occ = np.zeros(n, dtype=int)
        tocc = np.zeros((n, len(tick)), dtype=bool)
        planned = []
        for per, h in specs:
            lo, hi = bounds[per]
            for _ in range(50):
                ei = int(rng.integers(lo + 1, max(lo + 2, hi - h + 1)))
                xi = min(ei + h, n - 1)
                j = int(rng.integers(len(tick)))
                if np.isnan(AO.values[ei, j]):
                    continue
                if occ[ei:xi].max(initial=0) >= 5 or tocc[ei:xi, j].any():
                    continue
                occ[ei:xi] += 1
                tocc[ei:xi, j] = True
                planned.append((ei, xi, tick[j]))
                break
        eq, ex, tr_r = sim_slots(AC, AO, SIM_START, planned=planned)
        results.append((eq, ex, tr_r))
    return results


# --------------------------------------------------------------------------
# B, C and benchmarks: monthly target-weight simulator
# --------------------------------------------------------------------------
def month_end_mask(idx):
    s = pd.Series(idx.month, idx)
    return (s != s.shift(-1)).values  # last trading day of each month


def sim_weights(AC, AO, start, weight_fn, rebalance=True, end=None):
    """weight_fn(i) -> array of target weights decided at close i (month end).
    Trades at the next open. If rebalance=False, weight_fn is used once."""
    dates = AC.index
    i0 = dates.searchsorted(pd.Timestamp(start))
    i1 = len(dates) if end is None else dates.searchsorted(pd.Timestamp(end), side="right")
    ac, ao = AC.values, AO.values
    me = month_end_mask(dates)
    k = ac.shape[1]
    sh = np.zeros(k)
    cash = 1.0
    target = weight_fn(i0 - 1)  # decided at the close before the start
    pending = True
    eqs, exps = [], []
    spells, open_sp = [], {}
    for i in range(i0, i1):
        if pending:
            px = np.nan_to_num(ao[i])
            eq_open = cash + float(np.dot(sh, px))
            tgt_sh = np.where(px > 0, target * eq_open / np.where(px > 0, px, 1), 0)
            d = tgt_sh - sh
            cash -= float(np.dot(d, px)) + COST * float(np.dot(np.abs(d), px))
            for j in range(k):
                if sh[j] <= 0 < tgt_sh[j]:
                    open_sp[j] = (i, ao[i, j])
                elif tgt_sh[j] <= 0 < sh[j] and j in open_sp:
                    ei, epx = open_sp.pop(j)
                    spells.append(dict(ticker=AC.columns[j], entry=dates[ei], exit=dates[i],
                                       days=i - ei,
                                       ret=ao[i, j] * (1 - COST) / (epx * (1 + COST)) - 1))
            sh = tgt_sh
            pending = False
        inv = float(np.dot(sh, np.nan_to_num(ac[i])))
        eq = cash + inv
        eqs.append(eq)
        exps.append(inv / eq if eq else 0)
        if rebalance and me[i] and i < i1 - 1:
            target = weight_fn(i)
            pending = True
    for j, (ei, epx) in open_sp.items():
        spells.append(dict(ticker=AC.columns[j], entry=dates[ei], exit=dates[i1 - 1],
                           days=i1 - 1 - ei,
                           ret=ac[i1 - 1, j] * (1 - COST) / (epx * (1 + COST)) - 1,
                           open=True))
    out = dates[i0:i1]
    return pd.Series(eqs, out), pd.Series(exps, out), pd.DataFrame(spells)


def strat_B(AC, AO, sma=200, weighting="sleeve"):
    m = AC.rolling(sma).mean().values
    ac = AC.values
    k = ac.shape[1]

    def wf(i):
        q = (ac[i] > m[i])  # NaN compares False -> not qualifying
        if weighting == "sleeve":
            return q / k
        return q / q.sum() if q.sum() else np.zeros(k)

    return sim_weights(AC, AO, SIM_START, wf)


def strat_C(AC, AO, look=12, n=3):
    ac = AC.values
    sma200 = AC.rolling(200).mean().values
    L = 21 * look
    k = ac.shape[1]

    def wf(i):
        w = np.zeros(k)
        if i - L < 0:
            return w
        mom = ac[i - 21] / ac[i - L] - 1
        mom = np.where(np.isnan(mom), -np.inf, mom)
        top = np.argsort(-mom)[:n]
        for j in top:
            if np.isfinite(mom[j]) and ac[i, j] > sma200[i, j]:
                w[j] = 1 / n
        return w

    return sim_weights(AC, AO, SIM_START, wf)


def bench_bh(AC, AO, weights, start, end):
    w = np.asarray(weights, float)
    return sim_weights(AC, AO, start, lambda i: w, rebalance=False, end=end)


def bench_ew_monthly(AC, AO, start, end):
    k = AC.shape[1]
    return sim_weights(AC, AO, start, lambda i: np.ones(k) / k, end=end)


# --------------------------------------------------------------------------
# metrics
# --------------------------------------------------------------------------
def slice_eq(eq, a, b):
    s = eq.loc[a:b]
    # include the prior close as the base so the first day's return counts
    prev = eq.loc[:pd.Timestamp(a) - pd.Timedelta(days=1)]
    base = prev.iloc[-1] if len(prev) else 1.0
    return s / base, base


def metrics(eq, exp=None, trades=None, a=None, b=None):
    if a is not None:
        e, _ = slice_eq(eq, a, b)
        x = exp.loc[a:b] if exp is not None else None
    else:
        e, x = eq / 1.0, exp
    r = e.pct_change().fillna(e.iloc[0] - 1)
    yrs = len(e) / 252.0
    cagr = e.iloc[-1] ** (1 / yrs) - 1
    sd = r.std()
    sharpe = r.mean() / sd * np.sqrt(252) if sd > 0 else np.nan
    path = pd.concat([pd.Series([1.0]), e.reset_index(drop=True)])
    dd = (path / path.cummax() - 1).min()
    out = dict(CAGR=cagr, Sharpe=sharpe, MaxDD=dd, MAR=cagr / abs(dd) if dd else np.nan,
               Vol=sd * np.sqrt(252))
    if x is not None:
        out["Exposure"] = x.mean()
        out["DaysInvested"] = (x > 0.001).mean()
    if trades is not None and len(trades):
        t = trades
        if a is not None:
            t = t[(t["entry"] >= pd.Timestamp(a)) & (t["entry"] <= pd.Timestamp(b))]
        out["Trades"] = len(t)
        if len(t):
            w = t.loc[t["ret"] > 0, "ret"].sum()
            l_ = -t.loc[t["ret"] <= 0, "ret"].sum()
            out["WinRate"] = (t["ret"] > 0).mean()
            out["PF"] = w / l_ if l_ > 0 else np.inf
            out["AvgTrade"] = t["ret"].mean()
            out["AvgDays"] = t["days"].mean()
    return out


def year_table(series_map, start=SIM_START):
    rows = {}
    for name, eq in series_map.items():
        e = eq.loc[start:]
        y = e.groupby(e.index.year).last()
        prev = pd.concat([pd.Series([1.0], [y.index[0] - 1]), y]).shift(1).iloc[1:]
        rows[name] = y / prev - 1
    return pd.DataFrame(rows)


def window_stats(eq, a, b):
    e = eq.loc[a:b]
    prev = eq.loc[:pd.Timestamp(a) - pd.Timedelta(days=1)]
    base = prev.iloc[-1] if len(prev) else e.iloc[0]
    path = pd.concat([pd.Series([base]), e])
    return e.iloc[-1] / base - 1, (path / path.cummax() - 1).min()


# --------------------------------------------------------------------------
# formatting helpers
# --------------------------------------------------------------------------
def pct(x, d=1):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x*100:.{d}f}%"


def num(x, d=2):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    if np.isinf(x):
        return "inf"
    return f"{x:.{d}f}"


def mrow(name, m):
    return (f"| {name} | {pct(m['CAGR'])} | {num(m['Sharpe'])} | {pct(m['MaxDD'])} | "
            f"{num(m['MAR'])} | {pct(m.get('Exposure'), 0)} | {m.get('Trades', '—')} | "
            f"{pct(m.get('WinRate'), 0)} | {num(m.get('PF'))} |")


MHEAD = ("| Series | CAGR | Sharpe | MaxDD | CAGR/|MaxDD| | Avg exposure | Trades | Win % | PF |\n"
         "|---|---|---|---|---|---|---|---|---|")


def beats(s, b):
    return (s["Sharpe"] > b["Sharpe"]) or (s["MAR"] > b["MAR"])


# --------------------------------------------------------------------------
# Post-hoc commentary. Written AFTER viewing the 2026-10-15 run (data through
# 2026-10-14); it quotes that run's numbers and does not feed back into any
# definition, parameter, benchmark or pass decision above. Re-check it if the
# script is re-run on newer data.
# --------------------------------------------------------------------------
SUMMARY = [
    "## Summary (post-hoc commentary on the pre-registered results)",
    "",
    "| Strategy | Pre-registered verdict | What actually carries it |",
    "|---|---|---|",
    "| A pullback | **PASS** vs random-entry control | Beats matched random entries on both Sharpe and CAGR/|DD| "
    "in both periods (98th–99th pct of 200 control runs IS, 82nd–88th pct OOS — OOS is *not* significant at 95%). In absolute terms it is "
    "a low-return sleeve: 3.1% CAGR / 0.44 Sharpe OOS at ~24% exposure, well below SPY's 0.81 Sharpe. |",
    "| B time-series trend | **PASS** vs EW buy-and-hold | Drawdown: −14.8% vs −45.4% IS, −12.1% vs −29.6% OOS, "
    "for ~4.6 pts/yr less CAGR OOS. Sharpe ≈ benchmark OOS (0.80 vs 0.77; SPY 0.81). It is a drawdown tool, "
    "not a return enhancer. |",
    "| C momentum | **PASS** (narrowly) vs EW buy-and-hold | Passes **only** on CAGR/|DD|; its Sharpe is *below* "
    "EW buy-and-hold in both periods (0.58 vs 0.60 IS, 0.64 vs 0.77 OOS). OOS margin is 0.42 vs 0.40 and it "
    "loses to SPY (0.43). Weakest of the three. |",
    "",
    "None of the three beats SPY's raw CAGR in OOS (and per the brief they are not judged on that). "
    "No grid cell is flagged OVERFIT (no cell wins OOS while losing IS). Several cells pass IS only and decay OOS "
    "(A RSI<15/T=5; B 1/k-SMA100; C 6-1/top3, 9-1/top3, 9-1/top5) — evidence that the shorter-lookback / "
    "looser variants were IS-favourable, and a reason not to swap to any of them.",
]

INTERPRETATION = [
    "## Interpretation (post-hoc)",
    "",
    "- **B is the most robust result.** Every 1/16-sleeve SMA cell passes both periods, with OOS CAGR/|DD| "
    "0.44–0.62 vs 0.40 and MaxDD −11% to −15% across both periods vs −30% / −45% for the benchmark. "
    "Its drawdown cut is visible in all three stress windows (2008 −8.9%, COVID crash −11.0%, 2022 −8.6%). "
    "The cost is persistent lag in V-shaped recoveries and strong bull years (2019, 2023: +9.5% / +3.3% vs "
    "+27.8% / +22.2% EW) and roughly 26–29% average cash earning 0% here.",
    "- **A's edge is real but small and partly regime-driven.** Expectancy is +0.27% / +0.21% per trade (IS/OOS) "
    "net of 5 bp/side; removing the best 5 trades leaves +0.25% / +0.16%, so it is not a single-outlier artefact, "
    "but 3 of the 5 best trades are Feb-2020 crash-rebound entries and the OOS profit factor falls from 1.53 to 1.30. "
    "At 10 bp/side the OOS expectancy would roughly halve. The random control does not apply A's trend filter, "
    "so part of A's advantage over it is simply 'own uptrending ETFs' — the control measures entry-timing + "
    "filter jointly, not the pullback trigger alone. A also had two losing years in OOS (2018 −7.3%, 2022 −6.1%), "
    "i.e. the SMA200/SMA50 filter did not keep it out of choppy down-years.",
    "- **C's pass is fragile.** It depends on one number per period (MaxDD, set in 2008 IS and the 2020 crash "
    "OOS). In the COVID crash C took the full −23.4% because the monthly check left it 75% invested; it "
    "underperformed in 2010–2012 and 2016. The 12-1/top-5 cell is better on every metric in both periods, but "
    "picking it now would be grid-mining.",
    "- **Correlation of outcomes:** all three cut 2008 and 2022 losses to single digits, so as a portfolio "
    "overlay they mostly provide the same thing — reduced equity-beta in sustained bears — rather than "
    "independent return streams.",
]


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def control_summary(ctrl, a, b):
    ms = [metrics(eq, ex, tr, a, b) for eq, ex, tr in ctrl]
    df = pd.DataFrame(ms)
    return df


def pctile(val, arr):
    arr = np.asarray(arr, float)
    return float((arr < val).mean())


def main():
    ok, g0, data = etf_data.gate0()
    if not ok:
        print("\n".join(g0))
        print("GATE 0 FAILED -- stopping.")
        sys.exit(1)
    AC, AO = build_panels(data)
    last = AC.index[-1].date()
    L = []
    w = L.append

    # ---------------- runs
    A = strat_A(AC, AO, PRE_A["rsi"], PRE_A["tstop"])
    B = strat_B(AC, AO, PRE_B["sma"], PRE_B["weighting"])
    C = strat_C(AC, AO, PRE_C["look"], PRE_C["n"])
    ctrl = random_control(AC, AO, A[2], N_RANDOM, RNG_SEED)
    k = AC.shape[1]
    spy_w = [1.0] + [0.0] * (k - 1)
    ew_w = [1.0 / k] * k
    bench = {}
    for pn, (a, b) in PERIODS.items():
        bench[pn] = dict(SPY=bench_bh(AC, AO, spy_w, a, b),
                         EW=bench_bh(AC, AO, ew_w, a, b),
                         EWm=bench_ew_monthly(AC, AO, a, b))
    full_spy = bench_bh(AC, AO, spy_w, SIM_START, None)
    full_ew = bench_bh(AC, AO, ew_w, SIM_START, None)

    A[2].to_csv(os.path.join(REPORTS_DIR, f"etf_trend_trades_A_{TODAY}.csv"), index=False)

    M = {}  # (strategy, period) -> metrics
    for pn, (a, b) in PERIODS.items():
        for name, run in (("A", A), ("B", B), ("C", C)):
            M[(name, pn)] = metrics(run[0], run[1], run[2], a, b)
        for bn in ("SPY", "EW", "EWm"):
            eq, ex, tr = bench[pn][bn]
            M[(bn, pn)] = metrics(eq, ex)
        M[("CTRL", pn)] = control_summary(ctrl, a, b)

    # ---------------- report
    w(f"# ETF swing / trend backtest — {TODAY}")
    w("")
    w("Research only. No change to `memory/strategy.md`, no orders, no live routine touched. "
      "Script: `backtesting/scripts/backtest_etf_trend.py` (data + GATE 0: `backtesting/scripts/etf_data.py`).")
    w("")
    w(f"Data through **{last}** (last completed daily bar). IS = 2006-01-03 → 2017-12-29, "
      f"OOS = 2018-01-02 → {last}.")
    w("")

    # summary verdict placeholder (filled after pass table)
    verdict_at = len(L)
    L.extend(SUMMARY)
    w("")

    w("## GATE 0 — data / transport check")
    w("")
    w("Transport: `requests` + Yahoo v8 chart API (browser User-Agent, query1→query2 fallback), "
      "same as the other research scripts in this repo. Live fetch, cache bypassed.")
    w("")
    L.extend(g0)
    w("")
    w("Checks: (1) on every SPY ex-dividend date the AdjClose return equals "
      "(Close + Div) / prevClose − 1 to within 10 bp (it does, max 2.5 bp) → AdjClose is a continuous total-return series; "
      "(2) the AdjClose/Close factor changes only on dividend ex-dates for all 16 ETFs (0 unexplained jumps); "
      "(3) no split date shows a >20% jump in the split-adjusted close (IWM/EFA/EEM 2005, EEM 2008, "
      "the five SPDR sector 2:1 splits on 2025-12-05 are all continuous; XLF's 2016-09-19 '1.231:1' is the "
      "XLRE special distribution, which Yahoo encodes as a split and which is also continuous); "
      "(4) all 16 ETFs have a bar on 2005-01-03, no NaN rows and no missing SPY dates since then. "
      "Largest one-day moves are the known Oct-2008 / Mar-2020 days. **GATE 0: PASS.**")
    w("")

    w("## Pre-registered definitions")
    w("")
    w("Fixed in code before any result was viewed (a smoke run of the pre-registered configs was used only "
      "to check mechanics; no definition, parameter, benchmark or pass rule was changed after it).")
    w("")
    w("- **Prices.** Signals and returns on Yahoo AdjClose (split + dividend adjusted). Fills at the next "
      "day's open: Yahoo's open (split-adjusted, not dividend-adjusted) converted to the total-return basis "
      "with that day's AdjClose/Close factor, so fill and mark share one basis. 5 bp per side on every fill "
      "(including monthly rebalance trades). Cash earns 0% (this penalises the strategies that sit in cash, "
      "most of all in OOS where T-bills paid 2–5%).")
    w("- **Timing.** Every signal uses data through close *t*; every fill is the open of *t+1*. "
      "Monthly strategies decide on the last trading day's close and trade at the first open of the next month.")
    w("- **A — pullback in uptrend.** Entry when close > SMA200, SMA50 > SMA200, close ≤ SMA20 and "
      "RSI(2) < 10 (Wilder smoothing). Exit at the next open after: close > SMA5, or the 10th trading day held, "
      "or close ≤ entry × 0.92 (the −8% stop is evaluated on the close, consistent with the close-t/open-t+1 rule; "
      "realised losses can exceed 8% on gaps). 5 slots × 20% of prior-close equity; if more signals than free "
      "slots, most-oversold RSI(2) first; one position per ETF.")
    w("- **B — time-series trend.** Each ETF has a fixed 1/16 sleeve. At each month-end close the sleeve is long "
      "if close > SMA200, else cash; held sleeves are rebalanced back to 1/16. (Reading of \"equal weight across "
      "ETFs that qualify\": equal 1/16 weight per qualifying ETF, the rest in cash — the per-asset time-series "
      "definition, directly comparable to the equal-weight universe. The alternative 1/k re-normalisation is "
      "shown as a labelled sensitivity, not the pre-registered config.)")
    w("- **C — cross-sectional momentum.** Month-end ranking by 12-1 month total return "
      "(AdjClose[t−21] / AdjClose[t−252] − 1, 21 trading days per month). Top 3 get 1/3 each; a slot whose ETF "
      "closes below its SMA200 is held in cash (the 4th-ranked ETF is not promoted).")
    w("- **Benchmarks.** SPY buy-and-hold (total return) and equal-weight buy-and-hold of the 16 ETFs "
      "(1/16 each at the period's first open, never rebalanced), each bought fresh at the start of IS and of OOS "
      "with the same 5 bp entry cost. Monthly-rebalanced equal weight is shown for information. "
      f"For A: a random-entry control ({N_RANDOM} simulations, seed {RNG_SEED}) — for each A trade, a random ETF "
      "and random entry date within the same period, the same holding length, the same 20% slot size, the same "
      "5-slot cap and one-position-per-ETF rule, the same costs. This matches A's trade count, holding-period "
      "distribution and exposure.")
    w("- **Primary benchmark per strategy (for the pass rule).** A → random-entry control (median of the "
      "simulations); B → equal-weight buy-and-hold of the universe (same assets, same weights, only the trend "
      "filter differs); C → equal-weight buy-and-hold of the universe (same opportunity set). SPY is reported "
      "for every strategy as a secondary reference.")
    w("- **Pass rule.** The pre-registered config beats its primary benchmark on Sharpe **or** on "
      "CAGR/|MaxDD| in **both** IS and OOS. Grid cells are reported but cannot rescue a failing pre-registered config.")
    w("- **Periods.** All strategies run continuously from 2006-01-03 (indicators warmed up on 2004–2005 data) "
      "and are sliced at 2017-12-31; trade statistics are assigned to the period of the trade's entry. "
      "Sharpe is annualised from daily returns with rf = 0. Max drawdown is on the daily mark-to-market equity.")
    w("")

    # ---------------- pass table
    w("## Pass / fail (pre-registered configs only)")
    w("")
    w("| Strategy | Primary benchmark | IS: strat Sharpe / bench | IS: strat CAGR/|DD| / bench | IS beats? | "
      "OOS: strat Sharpe / bench | OOS: strat CAGR/|DD| / bench | OOS beats? | **Verdict** |")
    w("|---|---|---|---|---|---|---|---|---|")
    verdicts = {}
    for name, bname in (("A", "CTRL"), ("B", "EW"), ("C", "EW")):
        cells, both = [], True
        for pn in PERIODS:
            s = M[(name, pn)]
            if bname == "CTRL":
                c = M[("CTRL", pn)]
                bm = dict(Sharpe=c["Sharpe"].median(), MAR=c["MAR"].median())
            else:
                bm = M[(bname, pn)]
            ok_ = beats(s, bm)
            both &= ok_
            cells += [f"{num(s['Sharpe'])} / {num(bm['Sharpe'])}",
                      f"{num(s['MAR'])} / {num(bm['MAR'])}", "yes" if ok_ else "**no**"]
        verdicts[name] = both
        label = "random-entry control (median)" if bname == "CTRL" else "EW buy-and-hold"
        w(f"| {name} | {label} | " + " | ".join(cells) + f" | **{'PASS' if both else 'FAIL'}** |")
    w("")

    # ---------------- per-period tables
    names = {"A": "A pullback (RSI2<10, T=10)", "B": "B trend (SMA200, 1/16 sleeves)",
             "C": "C momentum (12-1, top 3)", "SPY": "SPY buy-and-hold",
             "EW": "EW buy-and-hold (16 ETFs)", "EWm": "EW monthly-rebalanced (info)"}
    for pn in PERIODS:
        w(f"## {pn}")
        w("")
        w(MHEAD)
        for key in ("A", "B", "C", "SPY", "EW", "EWm"):
            w(mrow(names[key], M[(key, pn)]))
        c = M[("CTRL", pn)]
        cm = {kk: c[kk].median() for kk in c.columns}
        cm["Trades"] = int(round(cm["Trades"]))
        w(mrow(f"A random-entry control (median of {N_RANDOM})", cm))
        w("")
        s = M[("A", pn)]
        w(f"A vs random control: A's Sharpe beats {pctile(s['Sharpe'], c['Sharpe'])*100:.0f}% of control runs "
          f"(control Sharpe 5th–95th pct {c['Sharpe'].quantile(.05):.2f} – {c['Sharpe'].quantile(.95):.2f}); "
          f"A's CAGR/|DD| beats {pctile(s['MAR'], c['MAR'])*100:.0f}% "
          f"({c['MAR'].quantile(.05):.2f} – {c['MAR'].quantile(.95):.2f}). "
          f"Control avg exposure {pct(c['Exposure'].median(),0)} vs A {pct(s['Exposure'],0)}; "
          f"control avg trade {pct(c['AvgTrade'].median(),2)} vs A {pct(s['AvgTrade'],2)}.")
        w("")

    # full period info
    w("## Full period 2006 → latest (information only, not part of the pass rule)")
    w("")
    w(MHEAD)
    for key, run in (("A", A), ("B", B), ("C", C)):
        w(mrow(names[key], metrics(run[0], run[1], run[2], SIM_START, "2100-01-01")))
    w(mrow(names["SPY"], metrics(full_spy[0], full_spy[1])))
    w(mrow(names["EW"], metrics(full_ew[0], full_ew[1])))
    w("")

    # ---------------- A trade analysis
    w("## Strategy A — trade-level expectancy and outlier dependence")
    w("")
    w("Net per-trade return (after 5 bp × 2), trades assigned by entry date.")
    w("")
    w("| Period | Trades | Win % | Avg win | Avg loss | Expectancy | Excl. best trade | Excl. best 5 | "
      "Sum of returns | Sum excl. best 5 | Avg days held | Trades ≤ −8% |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    tr = A[2]
    for pn, (a, b) in list(PERIODS.items()) + [("Full", (SIM_START, "2100-01-01"))]:
        t = tr[(tr["entry"] >= pd.Timestamp(a)) & (tr["entry"] <= pd.Timestamp(b))]["ret"].sort_values()
        w(f"| {pn} | {len(t)} | {pct((t>0).mean(),0)} | {pct(t[t>0].mean(),2)} | {pct(t[t<=0].mean(),2)} | "
          f"{pct(t.mean(),3)} | {pct(t.iloc[:-1].mean(),3)} | {pct(t.iloc[:-5].mean(),3)} | "
          f"{pct(t.sum(),0)} | {pct(t.iloc[:-5].sum(),0)} | "
          f"{tr.loc[t.index,'days'].mean():.1f} | {(t <= -0.08).sum()} |")
    w("")
    bt = tr.sort_values("ret", ascending=False).head(5)
    w("Best 5 trades (full period): " + "; ".join(
        f"{r.ticker} {r.entry.date()} {pct(r.ret,1)}" for r in bt.itertuples()) + ".")
    w("")
    per_etf = tr.groupby("ticker")["ret"].agg(["count", "mean", lambda s: (s > 0).mean()])
    per_etf.columns = ["n", "mean", "win"]
    w("A by ETF (full period): " + "; ".join(
        f"{t_} n={int(r.n)} avg {pct(r['mean'],2)}" for t_, r in per_etf.sort_values("n", ascending=False).iterrows()) + ".")
    w("")

    # ---------------- grids
    w("## Sensitivity grids (labelled; the pre-registered cell is marked ★)")
    w("")
    w("A cell \"passes\" with the same rule as above against the same primary benchmark. "
      "**OVERFIT** = wins OOS but loses IS. Grid cells never override the pre-registered verdict.")
    w("")
    grid_rows = []

    def flag(is_ok, oos_ok):
        if is_ok and oos_ok:
            return "pass both"
        if oos_ok and not is_ok:
            return "**OVERFIT** (OOS win, IS loss)"
        if is_ok and not oos_ok:
            return "IS only (decays OOS)"
        return "fail both"

    w("### A — RSI(2) threshold × time stop (benchmark: random-entry control matched to each cell, 100 sims)")
    w("")
    w("| RSI(2) < | Time stop | IS Sharpe (ctrl) | IS CAGR/|DD| (ctrl) | IS trades | "
      "OOS Sharpe (ctrl) | OOS CAGR/|DD| (ctrl) | OOS trades | Result |")
    w("|---|---|---|---|---|---|---|---|---|")
    for th in (5, 10, 15):
        for ts in (5, 10, 15):
            run = A if (th, ts) == (PRE_A["rsi"], PRE_A["tstop"]) else strat_A(AC, AO, th, ts)
            cc = random_control(AC, AO, run[2], 100, RNG_SEED + th * 100 + ts)
            res, cells = [], []
            for pn, (a, b) in PERIODS.items():
                s = metrics(run[0], run[1], run[2], a, b)
                c = control_summary(cc, a, b)
                bm = dict(Sharpe=c["Sharpe"].median(), MAR=c["MAR"].median())
                res.append(beats(s, bm))
                cells += [f"{num(s['Sharpe'])} ({num(bm['Sharpe'])})",
                          f"{num(s['MAR'])} ({num(bm['MAR'])})", str(s.get("Trades", 0))]
                grid_rows.append(dict(strategy="A", cell=f"rsi{th}_t{ts}", period=pn, **s,
                                      bench_Sharpe=bm["Sharpe"], bench_MAR=bm["MAR"]))
            star = " ★" if (th, ts) == (PRE_A["rsi"], PRE_A["tstop"]) else ""
            w(f"| {th}{star} | {ts} | " + " | ".join(cells) + f" | {flag(*res)} |")
    w("")

    w("### B — SMA length (benchmark: EW buy-and-hold)")
    w("")
    w("| SMA | Weighting | IS CAGR | IS Sharpe | IS MaxDD | IS CAGR/|DD| | OOS CAGR | OOS Sharpe | OOS MaxDD | "
      "OOS CAGR/|DD| | Result |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for wt in ("sleeve", "1/k"):
        for n in (100, 150, 200):
            run = B if (n, wt) == (PRE_B["sma"], PRE_B["weighting"]) else strat_B(AC, AO, n, wt)
            res, cells = [], []
            for pn, (a, b) in PERIODS.items():
                s = metrics(run[0], run[1], run[2], a, b)
                bm = M[("EW", pn)]
                res.append(beats(s, bm))
                cells += [pct(s["CAGR"]), num(s["Sharpe"]), pct(s["MaxDD"]), num(s["MAR"])]
                grid_rows.append(dict(strategy="B", cell=f"sma{n}_{wt}", period=pn, **s,
                                      bench_Sharpe=bm["Sharpe"], bench_MAR=bm["MAR"]))
            star = " ★" if (n, wt) == (PRE_B["sma"], PRE_B["weighting"]) else ""
            wl = "1/16 sleeves" if wt == "sleeve" else "1/k of qualifiers (sensitivity)"
            w(f"| {n}{star} | {wl} | " + " | ".join(cells) + f" | {flag(*res)} |")
    w("")

    w("### C — lookback × N (benchmark: EW buy-and-hold)")
    w("")
    w("| Lookback | N | IS CAGR | IS Sharpe | IS MaxDD | IS CAGR/|DD| | OOS CAGR | OOS Sharpe | OOS MaxDD | "
      "OOS CAGR/|DD| | Result |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for lk in (6, 9, 12):
        for n in (3, 5):
            run = C if (lk, n) == (PRE_C["look"], PRE_C["n"]) else strat_C(AC, AO, lk, n)
            res, cells = [], []
            for pn, (a, b) in PERIODS.items():
                s = metrics(run[0], run[1], run[2], a, b)
                bm = M[("EW", pn)]
                res.append(beats(s, bm))
                cells += [pct(s["CAGR"]), num(s["Sharpe"]), pct(s["MaxDD"]), num(s["MAR"])]
                grid_rows.append(dict(strategy="C", cell=f"{lk}-1_top{n}", period=pn, **s,
                                      bench_Sharpe=bm["Sharpe"], bench_MAR=bm["MAR"]))
            star = " ★" if (lk, n) == (PRE_C["look"], PRE_C["n"]) else ""
            w(f"| {lk}-1{star} | {n} | " + " | ".join(cells) + f" | {flag(*res)} |")
    w("")
    w("Benchmarks for B/C grid: IS EW B&H Sharpe "
      f"{num(M[('EW','IS 2006-2017')]['Sharpe'])}, CAGR/|DD| {num(M[('EW','IS 2006-2017')]['MAR'])}; "
      f"OOS EW B&H Sharpe {num(M[('EW','OOS 2018-latest')]['Sharpe'])}, "
      f"CAGR/|DD| {num(M[('EW','OOS 2018-latest')]['MAR'])}.")
    w("")
    pd.DataFrame(grid_rows).to_csv(os.path.join(REPORTS_DIR, f"etf_trend_grid_{TODAY}.csv"), index=False)

    # ---------------- calendar years
    w("## Calendar-year returns (pre-registered configs; benchmarks bought 2006-01-03)")
    w("")
    yt = year_table({"A": A[0], "B": B[0], "C": C[0], "SPY": full_spy[0], "EW B&H": full_ew[0]})
    w("| Year | " + " | ".join(yt.columns) + " |")
    w("|---|" + "---|" * len(yt.columns))
    for y, r in yt.iterrows():
        tag = f"{y} (YTD)" if y == last.year else str(y)
        w(f"| {tag} | " + " | ".join(pct(v) for v in r.values) + " |")
    w("")

    # ---------------- stress windows
    w("## Stress windows: 2008, 2020, 2022")
    w("")
    wins = [("2008 calendar year", "2008-01-01", "2008-12-31"),
            ("GFC peak→trough (SPY 2007-10-09 → 2009-03-09)", "2007-10-10", "2009-03-09"),
            ("2020 calendar year", "2020-01-01", "2020-12-31"),
            ("COVID crash (2020-02-19 → 2020-03-23)", "2020-02-20", "2020-03-23"),
            ("2022 calendar year", "2022-01-01", "2022-12-31")]
    series = {"A": A[0], "B": B[0], "C": C[0], "SPY": full_spy[0], "EW B&H": full_ew[0]}
    w("| Window | " + " | ".join(f"{s} return / max DD" for s in series) + " |")
    w("|---|" + "---|" * len(series))
    for lab, a, b in wins:
        cells = []
        for s, eq in series.items():
            rr, dd = window_stats(eq, a, b)
            cells.append(f"{pct(rr)} / {pct(dd)}")
        w(f"| {lab} | " + " | ".join(cells) + " |")
    w("")
    w("Exposure going into each stress window (avg gross exposure in the window): " + "; ".join(
        f"{lab.split(' (')[0]}: A {pct(A[1].loc[a:b].mean(),0)}, B {pct(B[1].loc[a:b].mean(),0)}, "
        f"C {pct(C[1].loc[a:b].mean(),0)}" for lab, a, b in wins) + ".")
    w("")

    # ---------------- interpretation scaffold
    interp_at = len(L)
    L.extend(INTERPRETATION)
    w("")

    # ---------------- limitations
    w("## Limitations")
    w("")
    w("- **Hindsight universe.** The 16 ETFs were chosen today; all survived and remain liquid. "
      "Closed, merged or delisted ETFs are absent, which flatters every strategy and both universe benchmarks "
      "(and especially momentum, which can only rotate into survivors).")
    w("- **No PEAD correlation possible.** The repo's PEAD artefacts are trade-level only (candidate/trade CSVs "
      "2022–2026), not a daily return series over 2006–latest, so the diversification value of these ETF "
      "strategies against the live PEAD book cannot be measured here.")
    w("- **2008 is the only deep bear in IS.** IS (2006–2017) contains one prolonged bear market (GFC); OOS adds "
      "the fast 2020 crash and the 2022 rate bear. Trend filters' drawdown benefit in IS rests largely on a "
      "single episode.")
    w("- Cash earns 0% (understates B/C/A — all hold substantial cash — relative to buy-and-hold, especially "
      "2018+ and 2023+ when T-bills yielded 2–5%). Sharpe uses rf = 0 for every series.")
    w("- A's −8% stop is evaluated on the close and executed next open (no intraday stop), so stop losses can "
      "exceed 8%. Fills at the open assume no slippage beyond 5 bp; these ETFs are among the most liquid, "
      "so this is reasonable for small size.")
    w("- Yahoo's \"raw\" open is split-adjusted (not truly as-traded); this does not affect returns.")
    w("- Taxes, borrow, dividend withholding and intra-month rebalancing drift are not modelled.")
    w("- A's grid controls use 100 simulations per cell (200 for the pre-registered config); control medians "
      "carry sampling noise of a few hundredths of Sharpe.")
    w("")
    w("## Files")
    w("")
    w(f"- `backtesting/reports/etf_trend_trades_A_{TODAY}.csv` — every A trade (pre-registered config).")
    w(f"- `backtesting/reports/etf_trend_grid_{TODAY}.csv` — every grid cell × period with metrics and benchmark.")
    w("")
    return L, verdict_at, interp_at, M, verdicts


if __name__ == "__main__":
    L, verdict_at, interp_at, M, verdicts = main()
    import json
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(L))
    print("wrote", REPORT_PATH)
    print({k_: bool(v_) for k_, v_ in verdicts.items()})
