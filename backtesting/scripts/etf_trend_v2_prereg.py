"""
ETF trend v2 -- PRE-REGISTERED definitions, tests, grids and engine.

This module is committed BEFORE the first full run. The runner
(backtest_etf_trend_v2.py) imports it, and the report states the commit that
added this file and whether it has changed since (git diff), so any post-hoc
edit is visible.

Conventions inherited from v1 (backtest_etf_trend.py / etf_data.py):
same 16-ETF universe, IS 2006-01-03..2017-12-29, OOS 2018-01-02..latest,
5 bp per side, signals at close t, fills at open t+1 (Yahoo open converted to
the total-return basis with that day's AdjClose/Close factor), daily marks on
Yahoo AdjClose, metrics = v1 `metrics()` (Sharpe annualised, rf = 0).

What changes in v2:
  * Idle cash earns the 13-week T-bill (^IRX). Day-i cash return =
    IRX[close i-1] / 100 * (calendar days from bar i-1 to bar i) / 360, credited
    to the cash balance before the open of day i. Synthetic bills carry no
    trading cost. Negative cash (costs, or the 1.5x-cap sensitivity) pays the
    same rate.
  * IEF (7-10y Treasuries) is available as a rotation asset (B2) and for the
    60/40 benchmark.
"""

import numpy as np
import pandas as pd

import backtest_etf_trend as v1

COST = v1.COST                     # 5 bp per side
SIM_START = v1.SIM_START           # 2006-01-01 -> first bar 2006-01-03
PERIODS = v1.PERIODS               # IS 2006-2017, OOS 2018-latest
FULL = ("2006-01-01", "2100-01-01")
SAFE = "IEF"

# --------------------------------------------------------------------------
# GATE 0 thresholds (fixed before any fetch result was used)
# --------------------------------------------------------------------------
# Validation anchor: v1 pre-registered B (SMA200, 1/16 sleeves, cash 0%),
# from backtesting/etf_trend_backtest_2026-10-15.md.
ANCHOR = {"IS 2006-2017": dict(CAGR=8.1, Sharpe=0.82, MaxDD=-14.8),
          "OOS 2018-latest": dict(CAGR=7.1, Sharpe=0.80, MaxDD=-12.1)}
ANCHOR_TOL = dict(CAGR=0.1, Sharpe=0.01, MaxDD=0.2)   # pts, Sharpe units, pts

# ^IRX sanity windows: (label, start, end, lo %, hi %) on the window mean.
IRX_SANITY = [("2006-2007", "2006-01-01", "2007-12-31", 3.0, 5.5),
              ("2010-2015", "2010-01-01", "2015-12-31", 0.0, 0.5),
              ("2023-2024", "2023-01-01", "2024-12-31", 4.5, 5.6)]
IRX_MAX_MISSING_FRAC = 0.02        # of SPY trading days since 2005-01-03
IRX_MAX_MISSING_RUN = 5            # consecutive missing SPY trading days
IRX_RANGE = (-0.5, 10.0)           # plausible % bounds since 2005

# --------------------------------------------------------------------------
# PRE-REGISTERED strategy configs
# --------------------------------------------------------------------------
PRE_B = dict(sma=200)                          # B1, B2 trend filter
PRE_B2_SAFE_SMA = 200                          # IEF trend filter for B2
PRE_VT = dict(target=0.10, look=21, cap=1.0, freq="W")
PRE_BL = dict(w_b1=0.5, w_vt=0.5, freq="M")
SIXTY_FORTY = {"SPY": 0.6, "IEF": 0.4}         # monthly rebalanced, 5 bp/trade

# Labeled sensitivity grids (never rescue a failing pre-registered config)
GRID_B_SMA = (100, 150, 200)                   # for B1 and B2
GRID_VT = [(t, lk) for t in (0.08, 0.10, 0.12) for lk in (21, 63)]
SENS_VT = [("monthly rebalance", dict(target=0.10, look=21, cap=1.0, freq="M")),
           ("1.5x exposure cap", dict(target=0.10, look=21, cap=1.5, freq="W"))]
# Extra labeled sensitivities: B1 OOS with idle cash in BIL (from 2007-05);
# all tests re-evaluated with Sharpe in excess of the T-bill.

# Pre-registered test benchmarks
SEATBELT_BENCH = {"B1": "EW", "B2": "EW", "BL": "EW", "VT": "SPY"}
SEATBELT_DD_FRAC = 0.50


def seatbelt_ok(s, b, sharpe_key="Sharpe"):
    """max DD <= 50% of benchmark's (in magnitude) AND Sharpe >= benchmark's."""
    return (abs(s["MaxDD"]) <= SEATBELT_DD_FRAC * abs(b["MaxDD"])
            and s[sharpe_key] >= b[sharpe_key])


def sixty_forty_ok(s, b, sharpe_key="Sharpe"):
    """Sharpe AND CAGR/MaxDD both strictly exceed the 60/40's."""
    return s[sharpe_key] > b[sharpe_key] and s["MAR"] > b["MAR"]


# --------------------------------------------------------------------------
# data
# --------------------------------------------------------------------------
def build_panels(data):
    """AC/AO panels for the 16-ETF universe (v1 order) plus IEF as last column."""
    idx = data["SPY"].index
    cols = list(v1.etf_data.UNIVERSE) + [SAFE]
    AC = pd.DataFrame({t: data[t]["AdjClose"] for t in cols}).reindex(idx)
    C = pd.DataFrame({t: data[t]["Close"] for t in cols}).reindex(idx)
    O = pd.DataFrame({t: data[t]["Open"] for t in cols}).reindex(idx)
    AO = O * AC / C
    return AC[cols], AO[cols]


def irx_on(idx, irx_df):
    """^IRX close (percent) reindexed to the trading calendar; returns
    (forward-filled Series, raw reindexed Series with NaNs)."""
    raw = irx_df["Close"].reindex(idx)
    return raw.ffill(), raw


def bill_daily(idx, irx_pct):
    """Day-i cash return = IRX[i-1]/100 * caldays(i-1 -> i)/360. Day 0 = 0."""
    days = pd.Series(idx, idx).diff().dt.days
    r = irx_pct.shift(1) / 100.0 * days / 360.0
    return r.fillna(0.0)


def zero_bill(idx):
    return pd.Series(0.0, idx)


# --------------------------------------------------------------------------
# masks
# --------------------------------------------------------------------------
def month_end_mask(idx):
    return v1.month_end_mask(idx)


def week_end_mask(idx):
    """Last trading day of each ISO week (the Friday close, or the last
    trading day of the week when Friday is a holiday)."""
    iso = idx.isocalendar()
    wk = pd.Series(iso.year.values * 100 + iso.week.values, idx)
    return (wk != wk.shift(-1)).values


def mask_for(idx, freq):
    return month_end_mask(idx) if freq == "M" else week_end_mask(idx)


# --------------------------------------------------------------------------
# engine: one or more sub-accounts, each with its own target-weight rule and
# decision calendar; optional periodic re-allocation between sub-accounts.
# With one account and a zero bill rate this reproduces v1.sim_weights.
# --------------------------------------------------------------------------
def sim(AC, AO, rb, accounts, alloc=(1.0,), alloc_mask=None, start=SIM_START,
        end=None, rebalance=True):
    """accounts: list of (weight_fn, decision_mask). weight_fn(i) -> target
    weights over AC.columns decided at close i; the remainder is cash at the
    T-bill rate `rb` (daily return Series aligned to AC.index).
    Returns dict(eq, exp, safe_exp, spells DataFrame, fills DatetimeIndex)."""
    dates = AC.index
    i0 = dates.searchsorted(pd.Timestamp(start))
    i1 = len(dates) if end is None else dates.searchsorted(pd.Timestamp(end), side="right")
    ac, ao = AC.values, AO.values
    rbv = np.asarray(rb.reindex(dates).fillna(0.0).values, float)
    k = ac.shape[1]
    na = len(accounts)
    safe_j = list(AC.columns).index(SAFE) if SAFE in AC.columns else None
    sh = [np.zeros(k) for _ in range(na)]
    cash = [float(a) for a in alloc]
    target = [accounts[a][0](i0 - 1) for a in range(na)]
    pending = [True] * na
    pend_alloc = False
    eqs, exps, sexp = [], [], []
    spells, open_sp, fills = [], [{} for _ in range(na)], []
    for i in range(i0, i1):
        for a in range(na):
            cash[a] *= 1.0 + rbv[i]
        px = np.nan_to_num(ao[i])
        if pend_alloc:
            eqo = [cash[a] + float(np.dot(sh[a], px)) for a in range(na)]
            tot = sum(eqo)
            for a in range(na):
                cash[a] += alloc[a] * tot - eqo[a]
                pending[a] = True
            pend_alloc = False
        for a in range(na):
            if not pending[a]:
                continue
            eq_open = cash[a] + float(np.dot(sh[a], px))
            tgt_sh = np.where(px > 0, target[a] * eq_open / np.where(px > 0, px, 1), 0)
            d = tgt_sh - sh[a]
            cash[a] -= float(np.dot(d, px)) + COST * float(np.dot(np.abs(d), px))
            for j in range(k):
                if abs(d[j]) * px[j] > 1e-9:
                    fills.append(dates[i])
                if sh[a][j] <= 0 < tgt_sh[j]:
                    open_sp[a][j] = (i, ao[i, j])
                elif tgt_sh[j] <= 0 < sh[a][j] and j in open_sp[a]:
                    ei, epx = open_sp[a].pop(j)
                    spells.append(dict(ticker=AC.columns[j], entry=dates[ei], exit=dates[i],
                                       days=i - ei,
                                       ret=ao[i, j] * (1 - COST) / (epx * (1 + COST)) - 1))
            sh[a] = tgt_sh
            pending[a] = False
        mark = np.nan_to_num(ac[i])
        inv = sum(float(np.dot(sh[a], mark)) for a in range(na))
        eq = sum(cash) + inv
        eqs.append(eq)
        exps.append(inv / eq if eq else 0)
        sexp.append(sum(sh[a][safe_j] * mark[safe_j] for a in range(na)) / eq
                    if safe_j is not None and eq else 0.0)
        if rebalance and i < i1 - 1:
            for a in range(na):
                if accounts[a][1][i]:
                    target[a] = accounts[a][0](i)
                    pending[a] = True
            if alloc_mask is not None and alloc_mask[i]:
                pend_alloc = True
    last = i1 - 1
    for a in range(na):
        for j, (ei, epx) in open_sp[a].items():
            spells.append(dict(ticker=AC.columns[j], entry=dates[ei], exit=dates[last],
                               days=last - ei,
                               ret=ac[last, j] * (1 - COST) / (epx * (1 + COST)) - 1,
                               open=True))
    out = dates[i0:i1]
    sp = pd.DataFrame(spells, columns=["ticker", "entry", "exit", "days", "ret", "open"])
    return dict(eq=pd.Series(eqs, out), exp=pd.Series(exps, out),
                safe_exp=pd.Series(sexp, out), spells=sp,
                fills=pd.DatetimeIndex(fills), rb=rb.reindex(out).fillna(0.0))


# --------------------------------------------------------------------------
# strategy weight rules
# --------------------------------------------------------------------------
def n_univ(AC):
    return len(v1.etf_data.UNIVERSE)


def wf_B(AC, sma=200, safe=False, safe_sma=PRE_B2_SAFE_SMA):
    """1/16 sleeve per universe ETF when close > SMA(sma) at the decision
    close. safe=False: idle sleeves in T-bill (B1, and v1 B when rb = 0).
    safe=True (B2): idle sleeves go to IEF while IEF close > its SMA200,
    else T-bill."""
    ac = AC.values
    m = AC.rolling(sma).mean().values
    ms = AC[SAFE].rolling(safe_sma).mean().values
    k, n = ac.shape[1], n_univ(AC)
    sj = list(AC.columns).index(SAFE)

    def wf(i):
        w = np.zeros(k)
        q = ac[i, :n] > m[i, :n]   # NaN compares False
        w[:n] = q / n
        if safe and ac[i, sj] > ms[i, sj]:
            w[sj] = (n - q.sum()) / n
        return w
    return wf


def wf_VT(AC, target=0.10, look=21, cap=1.0):
    """SPY exposure = min(cap, target / realised vol), realised vol = stdev of
    the last `look` daily AdjClose returns x sqrt(252); rest in T-bill."""
    spy = AC["SPY"]
    rv = (spy.pct_change().rolling(look).std() * np.sqrt(252)).values
    k = AC.shape[1]
    j = list(AC.columns).index("SPY")

    def wf(i):
        w = np.zeros(k)
        if i >= 0 and np.isfinite(rv[i]) and rv[i] > 0:
            w[j] = min(cap, target / rv[i])
        return w
    return wf


def wf_const(AC, weights):
    w = np.zeros(AC.shape[1])
    for t, x in weights.items():
        w[list(AC.columns).index(t)] = x
    return lambda i: w


# --------------------------------------------------------------------------
# runners
# --------------------------------------------------------------------------
def run_B(AC, AO, rb, sma=200, safe=False):
    return sim(AC, AO, rb, [(wf_B(AC, sma, safe), month_end_mask(AC.index))])


def run_VT(AC, AO, rb, target=0.10, look=21, cap=1.0, freq="W"):
    return sim(AC, AO, rb, [(wf_VT(AC, target, look, cap), mask_for(AC.index, freq))])


def run_BL(AC, AO, rb):
    idx = AC.index
    return sim(AC, AO, rb,
               [(wf_B(AC, PRE_B["sma"], False), month_end_mask(idx)),
                (wf_VT(AC, PRE_VT["target"], PRE_VT["look"], PRE_VT["cap"]),
                 mask_for(idx, PRE_VT["freq"]))],
               alloc=(PRE_BL["w_b1"], PRE_BL["w_vt"]),
               alloc_mask=mask_for(idx, PRE_BL["freq"]))


def bench_bh(AC, AO, rb, weights, start, end):
    """Buy-and-hold, bought at `start`'s first open, never rebalanced."""
    return sim(AC, AO, rb, [(wf_const(AC, weights), month_end_mask(AC.index))],
               start=start, end=end, rebalance=False)


def bench_6040(AC, AO, rb, start, end):
    return sim(AC, AO, rb, [(wf_const(AC, SIXTY_FORTY), month_end_mask(AC.index))],
               start=start, end=end)


def ew_weights():
    u = v1.etf_data.UNIVERSE
    return {t: 1.0 / len(u) for t in u}


# --------------------------------------------------------------------------
# metrics: v1.metrics + fills, T-bill-excess Sharpe, IEF share
# --------------------------------------------------------------------------
def metrics(run, a, b):
    sp = run["spells"]
    m = v1.metrics(run["eq"], run["exp"], sp if len(sp) else None, a, b)
    m.setdefault("Trades", 0)
    f = run["fills"]
    m["Fills"] = int(((f >= pd.Timestamp(a)) & (f <= pd.Timestamp(b))).sum())
    e, _ = v1.slice_eq(run["eq"], a, b)
    r = e.pct_change().fillna(e.iloc[0] - 1)
    x = r - run["rb"].loc[e.index]
    m["ExSharpe"] = x.mean() / x.std() * np.sqrt(252) if x.std() > 0 else np.nan
    m["SafeExp"] = run["safe_exp"].loc[a:b].mean()
    return m
