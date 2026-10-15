"""
PEAD portfolio-level simulation: PRE-REGISTRATION + ENGINE.

Committed BEFORE the first full run. Any later commit to this file is
disclosed in the report (the report lists this file's git history).

Research only. Does not modify memory/strategy.md, places no orders, touches
no live routine.

Every earlier PEAD backtest in this repo scored trades independently with no
capital constraint. This module defines one daily mark-to-market portfolio
engine (cash, positions, caps, costs, T-bill interest) and the arms that are
pushed through it.

--------------------------------------------------------------------------------
ARMS (same engine, same constraints, same costs for all)
--------------------------------------------------------------------------------
  P1  Live bar  : EPS surprise >= 15% AND vol >= 1.5x AND RS > 0 AND new
                  52-wk high <= 45d (q == 3) AND near-earnings gate.
  P2  Beat only : EPS surprise >= 15%, no other filters.
  P3  All base  : every committed base candidate (any surprise).
  RND Matched random: every P1 candidate's ticker replaced by a random name in
                  the same GICS sector and same 20d $-volume quintile on the
                  same entry date (pool and fallbacks as in the PEAD-vs-random
                  control test), keeping the P1 candidate's entry date, rank
                  and posture treatment. 500 simulations.
  Benchmarks : SPY buy-and-hold (adjusted close = total return) and 60/40
               SPY/IEF rebalanced at each month end, both through the same
               cost and T-bill conventions.

Ranking when more candidates qualify than can be taken (all arms):
  EPS surprise % descending, ticker ascending as tie-break. The live 1-10
  score is not reconstructible from price + earnings data (see the risk-sweep
  report); EPS surprise is its only graded input available for every
  candidate, and q is constant (= 3) inside P1. Spec says P3 ranks by
  surprise size; using the same key for every arm keeps the comparison clean.
  RND candidates keep the rank of the P1 candidate they replace.

--------------------------------------------------------------------------------
LIVE CONSTRAINTS (memory/strategy.md, as listed in the request)
--------------------------------------------------------------------------------
  start equity $100k; position size 11% (old rule) and 20% (current rule) of
  equity at the prior close; max 8 concurrent; 30% sector cap; 10% cash floor;
  max 5 new positions per week (ISO week; a position opened counts even if it
  closes the same week); -8% hard stop; +10% trigger -> sell 1/3, trail the
  rest 7% from the highest close; 42-calendar-day time stop.
  Exit mechanics are identical to simulate() in backtest_risk_sweep_entry_stop.py
  (close-based stop checks; the 1/3 scale-out is booked at entry x 1.10, as
  that function books it), so an unconstrained, zero-cost run reproduces the
  per-trade anchor.
  Trim rule: if the sector cap or cash floor leaves less room than the target
  size, the position is trimmed to fit; if the room is below half the target
  size the candidate is rejected and logged with that reason.
  A ticker already held is not bought again (logged as already_held).
  Not applied (not in the request's list, and not in the anchor): the
  sector-specific >20% EPS bars and the SPY<200MA bear-regime gate.

ELEVATED_BAR posture (pre_market step 1c / step 6, as the live routine applies
it): EPS surprise > 20% for all sectors and at most 2 new positions per week.
Health metric reconstructed point-in-time from the committed base candidates
(see weekly_posture()). 2026 cannot be reconstructed (no committed 2026 base
population; live pead_health.md history starts 2026-09-20), so 2026 YTD runs
posture-off, labeled as such. Posture-off is also reported for IS and OOS.

Costs: 5 bp per side (primary), 10 bp per side (sensitivity).
Cash: idle cash earns ^IRX, ETF v2 convention: day-i return =
IRX[i-1]/100 x calendar days(i-1 -> i)/360, forward-filled.

Periods (separate runs, each from $100k, never pooled):
  IS 2022-2024, OOS 2025, 2026 YTD (2026-01-01 -> 2026-06-04, the committed
  2026 candidate window; positions still open at the end are marked to market).

Metrics: CAGR (years = trading days / 252), Sharpe (mean / std of daily
returns x sqrt 252, rf not subtracted, ETF v2 convention), max drawdown on
daily equity, average % of equity invested, trades opened, qualified
candidates rejected (by reason), OLS of daily returns on SPY daily returns
(beta, alpha annualised x252, R^2).

--------------------------------------------------------------------------------
PRE-REGISTERED QUESTIONS (answered for both sizes, 5 bp, primary posture)
--------------------------------------------------------------------------------
"""

import numpy as np
import pandas as pd

QUESTIONS = {
    "Q1": "Does P1 beat SPY on CAGR in OOS? On Sharpe? On max drawdown?",
    "Q2": "Does P1 beat 60/40 on Sharpe AND on CAGR/MaxDD, in both periods (IS and OOS)?",
    "Q3": "Does P1 beat P2 on Sharpe in BOTH periods (IS and OOS)? If not, the extra "
          "filters cost more in lost trades than they add in selection.",
    "Q4": "How much of each arm's return is market beta rather than stock selection?",
    "Q5": "Does the 8-slot cap bind? How many qualified candidates were turned away?",
}

# ─── constants ────────────────────────────────────────────────────────────────
START_EQUITY = 100_000.0
SIZES = (0.11, 0.20)
MAX_POS = 8
SECTOR_CAP = 0.30
CASH_FLOOR = 0.10
WEEKLY_NEW = 5
HARD_STOP = 0.08
TRIGGER = 0.10
SCALE_FRAC = 1.0 / 3.0
TRAIL = 0.07
TIME_STOP = 42
MIN_PRICE = 10.0
MIN_TRIM_FRAC = 0.5          # trimmed size must be >= half the target size
COST_PRIMARY = 0.0005
COST_SENS = 0.0010

EPS_BAR = 15.0
ELEV_EPS_BAR = 20.0          # strict ">"
ELEV_WEEKLY_NEW = 2

# health metric (compute_pead_health.py, frozen)
HEALTH_WINDOW = 60
HEALTH_MIN_N = 20
HEALTH_THRESHOLD = 0.0

N_RANDOM = 500
SEED = 20261015

PERIODS = {
    "IS 2022-2024": ("2022-01-01", "2024-12-31"),
    "OOS 2025": ("2025-01-01", "2025-12-31"),
    "2026 YTD": ("2026-01-01", "2026-06-04"),
}
POSTURE_PERIODS = ("IS 2022-2024", "OOS 2025")   # reconstructible point-in-time

ARMS = {
    "P1": "Live bar (EPS>=15% + vol + RS + 52wk-high)",
    "P2": "Beat only (EPS>=15%)",
    "P3": "All base candidates (any surprise)",
}

# Validation anchor (memory/backtest_risk_sweep_2026-07-08.md, baseline row)
ANCHOR = {
    "IS 2022-2024": dict(n=194, win=57.7, avg=1.81, pf=1.68),
    "OOS 2025": dict(n=53, win=49.1, avg=1.228, pf=1.38),
    "2026 YTD": dict(n=30, win=50.0, avg=-0.23, pf=0.95),
}
ANCHOR_TOL = dict(n=0, win=0.1, avg=0.01, pf=0.01)


def arm_mask(c, arm, elevated):
    """Qualification of candidate rows for an arm under a posture flag array."""
    s = c["surprise_pct"].to_numpy(float)
    bar = np.where(elevated, s > ELEV_EPS_BAR, s >= EPS_BAR)
    if arm == "P1":
        return bar & (c["q"].to_numpy() == 3) & c["f_nearearn"].to_numpy(bool)
    if arm == "P2":
        return bar
    if arm == "P3":
        return np.where(elevated, s > ELEV_EPS_BAR, True)
    raise ValueError(arm)


# ─── pre-registered tests ─────────────────────────────────────────────────────
def q1(p1, spy):
    return dict(cagr=p1["CAGR"] > spy["CAGR"], sharpe=p1["Sharpe"] > spy["Sharpe"],
                maxdd=abs(p1["MaxDD"]) < abs(spy["MaxDD"]))


def q2(p1, b6040):
    return p1["Sharpe"] > b6040["Sharpe"] and p1["MAR"] > b6040["MAR"]


def q3(p1, p2):
    return p1["Sharpe"] > p2["Sharpe"]


# ─── market data containers ───────────────────────────────────────────────────
class Panel:
    """Open/close arrays for every ticker on one trading calendar."""

    def __init__(self, hists, calendar):
        self.dates = np.asarray(calendar, dtype="datetime64[D]")
        self.pos = {d: i for i, d in enumerate(self.dates)}
        self.tickers = sorted(hists)
        self.col = {t: k for k, t in enumerate(self.tickers)}
        cal = pd.DatetimeIndex(self.dates)
        n, m = len(cal), len(self.tickers)
        self.open = np.full((n, m), np.nan)
        self.close = np.full((n, m), np.nan)
        self.vol = np.full((n, m), np.nan)
        for t, h in hists.items():
            k = self.col[t]
            h = h[~h.index.duplicated()].reindex(cal)
            self.open[:, k] = h["Open"].to_numpy(float)
            self.close[:, k] = h["Close"].to_numpy(float)
            self.vol[:, k] = h["Volume"].to_numpy(float)
        # last valid close (for marking on days a ticker has no bar)
        self.mark = pd.DataFrame(self.close).ffill().to_numpy()


def bill_daily(dates, irx_pct):
    """Day-i cash return = IRX[i-1]/100 * caldays(i-1 -> i)/360. Day 0 = 0."""
    d = pd.Series(pd.DatetimeIndex(dates))
    days = d.diff().dt.days.to_numpy(float)
    r = np.r_[0.0, irx_pct[:-1] / 100.0 * days[1:] / 360.0]
    return np.nan_to_num(r)


# ─── health metric (point-in-time) ────────────────────────────────────────────
def health_trade(o, c, dates, i):
    """Port of backtest_pead_2026_ytd.simulate_trade with a 7% trail (the BASE
    trade compute_pead_health.py averages). Returns (exit_day_index, ret) or None
    while still open at the end of data."""
    e = o[i]
    hi = e
    trail = False
    for j in range(i, len(c)):
        x = c[j]
        if np.isnan(x):
            continue
        hi = max(hi, x)
        if hi >= e * (1 + TRIGGER):
            trail = True
        cal = int((dates[j] - dates[i]).astype(int))
        if cal >= TIME_STOP or x <= e * (1 - HARD_STOP) or (trail and x <= hi * (1 - TRAIL)):
            return j, (x - e) / e
    return None


def weekly_posture(panel, base):
    """ELEVATED flag per trading day. Each Sunday s, health = mean return of base
    trades with a positive surprise that EXITED in [s-60d, s]; posture for the
    following Mon-Fri = ELEVATED if n >= 20 and health < 0, else NORMAL (fail-open
    on thin data, as compute_pead_health.py). Uses only bars on or before s."""
    exits, rets = [], []
    for _, r in base[base.surprise_pct > 0].iterrows():
        k = panel.col.get(r.ticker)
        i = panel.pos.get(np.datetime64(r.entry_date, "D"))
        if k is None or i is None:
            continue
        o, c = panel.open[:, k], panel.close[:, k]
        if np.isnan(o[i]) or o[i] < MIN_PRICE:
            continue
        res = health_trade(o, c, panel.dates, i)
        if res is None:
            continue
        exits.append(panel.dates[res[0]])
        rets.append(res[1] * 100)
    exits = np.array(exits, dtype="datetime64[D]")
    rets = np.array(rets)
    order = np.argsort(exits)
    exits, rets = exits[order], rets[order]

    elevated = np.zeros(len(panel.dates), bool)
    weekly = []
    dts = pd.DatetimeIndex(panel.dates)
    sundays = pd.date_range(dts[0] - pd.Timedelta(days=7), dts[-1], freq="W-SUN")
    for s in sundays:
        s64 = np.datetime64(s.date(), "D")
        lo = s64 - np.timedelta64(HEALTH_WINDOW, "D")
        a, b = np.searchsorted(exits, lo), np.searchsorted(exits, s64, side="right")
        n = b - a
        h = rets[a:b].mean() if n >= HEALTH_MIN_N else np.nan
        elev = bool(n >= HEALTH_MIN_N and h < HEALTH_THRESHOLD)
        wk = (dts > s) & (dts <= s + pd.Timedelta(days=7))
        elevated[wk] = elev
        weekly.append(dict(sunday=s.date(), n=int(n), health=h, elevated=elev))
    return elevated, pd.DataFrame(weekly)


# ─── portfolio engine ─────────────────────────────────────────────────────────
def run_portfolio(panel, cands, start, end, size, cost, bill, elevated,
                  constrained=True, log=True):
    """Daily mark-to-market simulation.

    cands: DataFrame with columns ticker, sector, entry_date (datetime64[D]),
           surprise_pct, rank (lower = better), cid (candidate id). Already
           filtered to the arm's qualifying rows (posture included).
    Returns dict(eq, exposure, dates, trades, rejects).
    """
    d0 = np.searchsorted(panel.dates, np.datetime64(start, "D"))
    d1 = np.searchsorted(panel.dates, np.datetime64(end, "D"), side="right")
    by_day = {}
    if len(cands):
        cc = cands.sort_values(["rank", "ticker"])
        for row in cc.itertuples(index=False):
            i = panel.pos.get(np.datetime64(row.entry_date, "D"))
            if i is not None and d0 <= i < d1:
                by_day.setdefault(i, []).append(row)

    cash = START_EQUITY
    held = {}            # ticker -> dict
    week_new = {}
    eq = np.empty(d1 - d0)
    expo = np.empty(d1 - d0)
    trades, rejects = [], []
    close, mark, opn = panel.close, panel.mark, panel.open
    col = panel.col
    dates = panel.dates
    prev_eq = START_EQUITY

    for t in range(d0, d1):
        cash *= 1.0 + bill[t]
        # ── entries at the open ───────────────────────────────────────────
        todays = by_day.get(t)
        if todays:
            equity = cash + sum(p["sh"] * mark[t - 1, p["k"]] for p in held.values()) \
                if t > d0 else cash
            sect = {}
            for p in held.values():
                sect[p["sector"]] = sect.get(p["sector"], 0.0) + p["sh"] * mark[t - 1, p["k"]]
            iso = pd.Timestamp(dates[t]).isocalendar()
            wk = (iso[0], iso[1])
            wcap = ELEV_WEEKLY_NEW if elevated[t] else WEEKLY_NEW
            seen = set()
            for r in todays:
                tk = r.ticker
                if tk in seen:
                    continue
                seen.add(tk)
                k = col.get(tk)
                px = opn[t, k] if k is not None else np.nan
                reason = None
                target = size * equity
                amt = target
                if k is None or np.isnan(px) or px < MIN_PRICE:
                    reason = "no_entry_bar"
                elif tk in held:
                    reason = "already_held"
                elif constrained:
                    if len(held) >= MAX_POS:
                        reason = "slots_full"
                    elif week_new.get(wk, 0) >= wcap:
                        reason = "weekly_cap"
                    else:
                        room_s = SECTOR_CAP * equity - sect.get(r.sector, 0.0)
                        room_c = (cash - CASH_FLOOR * equity) / (1 + cost)
                        amt = min(target, room_s, room_c)
                        if amt < MIN_TRIM_FRAC * target:
                            reason = "sector_cap" if room_s <= room_c else "cash_floor"
                if reason:
                    if log:
                        rejects.append((r.cid, tk, r.sector, dates[t], r.surprise_pct, reason))
                    continue
                if not constrained:
                    amt = target
                sh = amt / px
                cash -= amt * (1 + cost)
                held[tk] = dict(k=k, sh=sh, entry=px, i=t, hi=px, scaled=False,
                                sector=r.sector, cid=r.cid, cost_in=amt * (1 + cost),
                                proceeds=0.0, booked=0.0)
                sect[r.sector] = sect.get(r.sector, 0.0) + amt
                week_new[wk] = week_new.get(wk, 0) + 1
        # ── exits at the close ────────────────────────────────────────────
        done = []
        for tk, p in held.items():
            x = close[t, p["k"]]
            if np.isnan(x):
                continue
            if x > p["hi"]:
                p["hi"] = x
            e = p["entry"]
            cal = int((dates[t] - dates[p["i"]]).astype(int))
            why = None
            if not p["scaled"] and x <= e * (1 - HARD_STOP):
                why = "hard_stop"
            else:
                if not p["scaled"] and x >= e * (1 + TRIGGER):
                    sell = p["sh"] * SCALE_FRAC
                    px_s = e * (1 + TRIGGER)
                    cash += sell * px_s * (1 - cost)
                    p["proceeds"] += sell * px_s * (1 - cost)
                    p["booked"] = SCALE_FRAC * TRIGGER
                    p["sh"] -= sell
                    p["scaled"] = True
                if p["scaled"] and x <= p["hi"] * (1 - TRAIL):
                    why = "trail_stop"
                elif cal >= TIME_STOP:
                    why = "time"
            if why:
                cash += p["sh"] * x * (1 - cost)
                p["proceeds"] += p["sh"] * x * (1 - cost)
                gross = p["booked"] + (1 - (SCALE_FRAC if p["scaled"] else 0.0)) * (x - e) / e
                trades.append(dict(cid=p["cid"], ticker=tk, sector=p["sector"],
                                   entry_date=dates[p["i"]], exit_date=dates[t], exit=why,
                                   gross_ret=gross * 100,
                                   net_ret=(p["proceeds"] / p["cost_in"] - 1) * 100,
                                   alloc=p["cost_in"]))
                done.append(tk)
        for tk in done:
            del held[tk]
        pv = sum(p["sh"] * mark[t, p["k"]] for p in held.values())
        eq[t - d0] = cash + pv
        expo[t - d0] = pv / eq[t - d0]
        prev_eq = eq[t - d0]
    for tk, p in held.items():
        x = mark[d1 - 1, p["k"]]
        e = p["entry"]
        gross = p["booked"] + (1 - (SCALE_FRAC if p["scaled"] else 0.0)) * (x - e) / e
        trades.append(dict(cid=p["cid"], ticker=tk, sector=p["sector"],
                           entry_date=dates[p["i"]], exit_date=dates[d1 - 1],
                           exit="open_at_period_end", gross_ret=gross * 100,
                           net_ret=((p["proceeds"] + p["sh"] * x) / p["cost_in"] - 1) * 100,
                           alloc=p["cost_in"]))
    return dict(eq=eq, exposure=expo, dates=dates[d0:d1], trades=trades, rejects=rejects,
                final=prev_eq)


def run_benchmark(panel, weights, start, end, cost, bill, rebalance_monthly):
    """Buy at the first open, mark at closes; optional month-end rebalance at close."""
    d0 = np.searchsorted(panel.dates, np.datetime64(start, "D"))
    d1 = np.searchsorted(panel.dates, np.datetime64(end, "D"), side="right")
    ks = {t: panel.col[t] for t in weights}
    cash = START_EQUITY
    sh = {}
    for t, w in weights.items():
        amt = w * START_EQUITY / (1 + cost)
        sh[t] = amt / panel.open[d0, ks[t]]
        cash -= amt * (1 + cost)
    eq = np.empty(d1 - d0)
    dts = pd.DatetimeIndex(panel.dates)
    for t in range(d0, d1):
        if t > d0:
            cash *= 1.0 + bill[t]
        val = {s: sh[s] * panel.mark[t, ks[s]] for s in sh}
        tot = cash + sum(val.values())
        month_end = t + 1 >= len(dts) or dts[t + 1].month != dts[t].month
        if rebalance_monthly and month_end and t < d1 - 1:
            for s, w in weights.items():
                tgt = w * tot
                diff = tgt - val[s]
                cash -= diff + abs(diff) * cost
                sh[s] = tgt / panel.mark[t, ks[s]]
            tot = cash + sum(sh[s] * panel.mark[t, ks[s]] for s in sh)
        eq[t - d0] = tot
    return dict(eq=eq, dates=panel.dates[d0:d1])


# ─── metrics ──────────────────────────────────────────────────────────────────
def metrics(eq, spy_ret, exposure=None):
    e = np.asarray(eq, float) / START_EQUITY
    r = np.diff(np.r_[1.0, e])
    yrs = len(e) / 252.0
    cagr = e[-1] ** (1 / yrs) - 1
    sd = r.std(ddof=1)
    sharpe = r.mean() / sd * np.sqrt(252) if sd > 0 else np.nan
    path = np.r_[1.0, e]
    dd = (path / np.maximum.accumulate(path) - 1).min()
    out = dict(CAGR=cagr, TotRet=e[-1] - 1, Sharpe=sharpe, MaxDD=dd,
               MAR=cagr / abs(dd) if dd else np.nan, Vol=sd * np.sqrt(252))
    if exposure is not None:
        out["Invested"] = float(np.mean(exposure))
    # OLS of daily returns on SPY daily returns (day 0 dropped: entry-day costs)
    y, x = r[1:], np.asarray(spy_ret, float)[1:]
    X = np.c_[np.ones_like(x), x]
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    ss_tot = ((y - y.mean()) ** 2).sum()
    out["Alpha"] = coef[0] * 252
    out["Beta"] = coef[1]
    out["R2"] = 1 - (resid ** 2).sum() / ss_tot if ss_tot > 0 else np.nan
    # Q4 split of the annualised mean daily return
    out["AnnMean"] = y.mean() * 252
    out["MktPart"] = coef[1] * x.mean() * 252
    return out
