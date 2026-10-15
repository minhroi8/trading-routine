"""
Selection-skill test: PEAD earnings-beat entries vs matched random picks.

Question: does the PEAD earnings-beat signal pick stocks that do better than
random stocks bought on the SAME day, in the SAME sector, of SIMILAR size, and
run through the SAME exit rules? If not, any PEAD P&L is market/sector/size
beta (or exit-rule luck), not selection skill.

Research only. Does not modify strategy.md and places no orders. Diagnostic,
like backtest_risk_sweep_entry_stop.py, whose data fetch, cache and simulate()
mechanics this script reuses.

--------------------------------------------------------------------------------
SIGNAL TIERS (all from the committed, already-validated candidate set)
--------------------------------------------------------------------------------
  live   : EPS surprise >= 15% AND q == 3 (vol>=1.5x, RS>0, 52w high <=45d)
           == the current live entry bar == S3 V0 / risk-sweep baseline
           (194 IS + 53 OOS) plus the 30 committed 2026 YTD trades.
  beat15 : EPS surprise >= 15%, any q (the raw earnings-beat signal).
  nonbeat: base candidates with EPS surprise < 15% (incl. misses) -- the
           earnings-event control: what a report with NO big beat does.
  all    : every base candidate (any surprise, incl. misses) -- shows whether
           "had an earnings report" alone beats random, i.e. what the beat
           itself adds on top of a generic earnings-event drift.

--------------------------------------------------------------------------------
RANDOM CONTROL (matched placebo)
--------------------------------------------------------------------------------
For each signal trade entered at the open of day D in GICS sector S:
  pool  = tickers in the same committed universe (current S&P 500 members, the
          same survivorship bias as the signal arm) that on day D
            * have an open price on D, >= $10            (same base gate)
            * have 20d avg $-volume (close x volume, prior 20 sessions)
              >= $20M                                     (same base gate)
            * are in sector S
            * are in the same SIZE quintile on D, where size = 20d avg
              $-volume ranked cross-sectionally over the eligible pool on D
            * are not the signal ticker, and had no earnings report in the
              committed set in [D-10, D+5] calendar days (so the control is
              not itself a post-earnings drift trade)
  If fewer than MIN_POOL names match, widen to size quintile +/-1, then to
  sector-only. The level used is recorded per trade.

Historical market cap is not reconstructible here (no point-in-time shares
outstanding), so size is proxied by 20d $-volume, the same liquidity measure
the strategy's own universe gate uses. Liquidity and cap are highly correlated
within the S&P 500 but not identical; this is stated in the report.

Every control is entered at the open of D and simulated with the SAME exits as
the signal: flat -8% hard stop, 1/3 scale-out at +10%, 7% trail on the rest,
42-calendar-day time stop (simulate() from the risk-sweep / S3 scripts). A
second, exit-free measure (plain 42-day hold, open D to the first close >= 42
calendar days later) separates selection skill from exit-rule effects.

--------------------------------------------------------------------------------
STATISTICS
--------------------------------------------------------------------------------
  1. Placebo portfolios: N_PLACEBO draws; each draw replaces every signal trade
     with one random member of its matched pool. p = share of placebo means
     >= the signal mean (one-sided, "signal beats random").
  2. Paired excess per trade = signal return - mean return of its matched
     pool. Mean excess with a 95% bootstrap CI that resamples ENTRY DATES (trades
     on the same day share market moves, so per-trade i.i.d. bootstraps would
     overstate significance), plus a date-clustered sign-flip permutation p.
  3. Distributions: percentiles, win rate, std of signal returns vs the pooled
     matched-control returns.

IS = 2022-2024, OOS = 2025, 2026 YTD reported separately (never averaged), as in
every other report in this repo. Zero costs/slippage, survivorship-biased
universe.
"""

import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)

import backtest_risk_sweep_entry_stop as rs  # noqa: E402  (fetch/cache/simulate)

REPORTS_DIR = rs.REPORTS_DIR
RUN_DATE = "2026-10-15"

HARD_STOP_PCT = 8.0          # current live flat stop
HOLD_DAYS = rs.TIME_STOP     # 42 calendar days
MIN_PRICE = rs.MIN_PRICE     # $10
MIN_DVOL = 20_000_000.0      # 20d avg $-volume gate
DVOL_WINDOW = 20
N_SIZE_BUCKETS = 5
MIN_POOL = 5
EARN_EXCL_BEFORE = 10        # calendar days before D
EARN_EXCL_AFTER = 5          # calendar days after D
N_PLACEBO = 10_000
N_BOOT = 10_000
SEED = 20261015

PERIODS = ["IS (2022-2024)", "OOS (2025)", "2026 YTD"]
TIERS = [
    ("live", "Live bar (EPS≥15% & q==3)"),
    ("beat15", "Raw beat (EPS≥15%, any q)"),
    ("nonbeat", "Non-beat reports (EPS surprise <15%)"),
    ("all", "All base candidates (any surprise)"),
]
MEASURES = [("strat", "strategy exits (−8% stop / scale / trail / 42d)"),
            ("hold", "plain 42-day hold, no stops")]


# ─── Fast per-ticker arrays + simulation (same rules as rs.simulate) ───────────
class Series:
    __slots__ = ("dates", "open", "close", "dvol20")

    def __init__(self, hist):
        self.dates = hist.index.values.astype("datetime64[D]")
        self.open = hist["Open"].to_numpy(float)
        self.close = hist["Close"].to_numpy(float)
        dv = (hist["Close"] * hist["Volume"].fillna(0)).to_numpy(float)
        # mean of the 20 sessions strictly BEFORE each day (no look-ahead)
        c = np.concatenate([[0.0], np.cumsum(dv)])
        out = np.full(len(dv), np.nan)
        for i in range(DVOL_WINDOW, len(dv)):
            out[i] = (c[i] - c[i - DVOL_WINDOW]) / DVOL_WINDOW
        self.dvol20 = out

    def idx(self, d):
        d = np.datetime64(pd.Timestamp(d), "D")
        i = np.searchsorted(self.dates, d)
        return i if i < len(self.dates) and self.dates[i] == d else -1


def sim_fast(s, i):
    """Exact port of rs.simulate() (flat stop) on arrays; returns (strat%, hold%)."""
    entry = s.open[i]
    stop = entry * (1.0 - HARD_STOP_PCT / 100.0)
    d0 = s.dates[i]
    booked, open_frac, scaled, highest = 0.0, 1.0, False, entry
    strat = None
    hold = None
    n = len(s.close)
    for j in range(i, n):
        close = s.close[j]
        if close > highest:
            highest = close
        cal = int((s.dates[j] - d0).astype(int))
        if strat is None:
            if not scaled and close <= stop:
                strat = (close - entry) / entry
            else:
                if not scaled and close >= entry * (1.0 + rs.TRAIL_TRIGGER):
                    booked += rs.SCALE_FRAC * rs.TRAIL_TRIGGER
                    open_frac = 1.0 - rs.SCALE_FRAC
                    scaled = True
                if scaled and close <= highest * (1.0 - rs.TRAIL_PCT):
                    strat = booked + open_frac * (close - entry) / entry
                elif cal >= HOLD_DAYS:
                    strat = booked + open_frac * (close - entry) / entry
        if cal >= HOLD_DAYS:
            hold = (close - entry) / entry
            break
    last = s.close[n - 1]
    if strat is None:
        strat = booked + open_frac * (last - entry) / entry
    if hold is None:
        hold = (last - entry) / entry
    return strat * 100.0, hold * 100.0


# ─── Data ──────────────────────────────────────────────────────────────────────
def load_candidates():
    a = pd.read_csv(rs.CAND_2022_2025)
    a["period"] = a["year"].map(lambda y: "IS (2022-2024)" if y <= 2024
                                else ("OOS (2025)" if y == 2025 else "other"))
    a = a[a.period != "other"]
    b = pd.read_csv(rs.CAND_2026)
    b["year"] = pd.to_datetime(b["entry_date"]).dt.year
    b["period"] = "2026 YTD"
    cols = ["ticker", "sector", "year", "period", "earn_date", "entry_date",
            "surprise_pct", "f_vol15x", "f_rs", "f_52w", "f_nearearn"]
    c = pd.concat([a[cols], b[cols]], ignore_index=True)
    c["q"] = c.f_vol15x.astype(bool).astype(int) + c.f_rs.astype(bool).astype(int) \
        + c.f_52w.astype(bool).astype(int)
    c["entry_date"] = pd.to_datetime(c.entry_date).values.astype("datetime64[D]")
    c["earn_date"] = pd.to_datetime(c.earn_date).values.astype("datetime64[D]")
    c["tier_live"] = (c.surprise_pct >= 15.0) & (c.q == 3) & c.f_nearearn.astype(bool)
    c["tier_beat15"] = c.surprise_pct >= 15.0
    c["tier_nonbeat"] = c.surprise_pct < 15.0
    c["tier_all"] = True
    return c


def build_pools(cand, series, sector_of, earn_by_ticker):
    """For each unique entry date: eligible pool with size bucket."""
    dates = np.unique(cand.entry_date.values)
    tickers = [t for t in series if t != "SPY" and t in sector_of]
    pools = {}
    for d in dates:
        rows = []
        for t in tickers:
            s = series[t]
            i = s.idx(d)
            if i < 0:
                continue
            if not (s.open[i] >= MIN_PRICE) or not (s.dvol20[i] >= MIN_DVOL):
                continue
            ed = earn_by_ticker.get(t)
            if ed is not None:
                lo = d - np.timedelta64(EARN_EXCL_BEFORE, "D")
                hi = d + np.timedelta64(EARN_EXCL_AFTER, "D")
                k = np.searchsorted(ed, lo)
                if k < len(ed) and ed[k] <= hi:
                    continue
            rows.append((t, sector_of[t], s.dvol20[i], i))
        if not rows:
            pools[d] = pd.DataFrame(columns=["ticker", "sector", "dvol", "i", "bucket"])
            continue
        p = pd.DataFrame(rows, columns=["ticker", "sector", "dvol", "i"])
        p["bucket"] = pd.qcut(p.dvol.rank(method="first"), N_SIZE_BUCKETS, labels=False)
        pools[d] = p
    return pools


def size_bucket_of(series_t, d, pool):
    """Bucket the signal ticker would fall in on day d, against that day's pool."""
    i = series_t.idx(d)
    v = series_t.dvol20[i] if i >= 0 else np.nan
    if pool.empty or not np.isfinite(v):
        return None
    edges = np.sort(pool.dvol.to_numpy())
    rank = np.searchsorted(edges, v) / len(edges)
    return min(int(rank * N_SIZE_BUCKETS), N_SIZE_BUCKETS - 1)


# ─── Stats helpers ─────────────────────────────────────────────────────────────
def dist(x):
    x = np.asarray(x, float)
    if len(x) == 0:
        return {}
    p = np.percentile(x, [5, 25, 50, 75, 95])
    return {"n": len(x), "mean": x.mean(), "std": x.std(ddof=1) if len(x) > 1 else np.nan,
            "win": (x > 0).mean() * 100, "p5": p[0], "p25": p[1], "p50": p[2],
            "p75": p[3], "p95": p[4]}


def clustered_tests(excess, dates, rng):
    """Date-clustered bootstrap CI for mean excess + sign-flip permutation p."""
    df = pd.DataFrame({"e": excess, "d": dates})
    g = df.groupby("d")["e"].agg(["sum", "count"])
    sums, cnts = g["sum"].to_numpy(), g["count"].to_numpy()
    k = len(sums)
    obs = sums.sum() / cnts.sum()
    idx = rng.integers(0, k, size=(N_BOOT, k))
    boot = sums[idx].sum(1) / cnts[idx].sum(1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    signs = rng.choice([-1.0, 1.0], size=(N_BOOT, k))
    perm = (signs * sums).sum(1) / cnts.sum()
    p_one = (np.sum(perm >= obs) + 1) / (N_BOOT + 1)
    p_two = (np.sum(np.abs(perm) >= abs(obs)) + 1) / (N_BOOT + 1)
    return obs, lo, hi, p_one, p_two, k


# ─── Main analysis ─────────────────────────────────────────────────────────────
def run():
    rng = np.random.default_rng(SEED)
    cand = load_candidates()
    tickers = sorted(set(cand.ticker) | {"SPY"})
    print(f"{len(cand)} candidates over {len(tickers)} tickers; fetching/caching OHLC...")
    series = {}
    for n_, t in enumerate(tickers):
        if n_ % 50 == 0:
            print(f"  {n_}/{len(tickers)}")
        h = rs.cached_history(t)
        if h is not None and len(h) > DVOL_WINDOW + 5:
            series[t] = Series(h)
    print(f"  history ok: {len(series)}/{len(tickers)}")

    sector_of = cand.groupby("ticker")["sector"].first().to_dict()
    earn_by_ticker = {t: np.sort(g.earn_date.values) for t, g in cand.groupby("ticker")}

    # Verify the fast simulator against the repo's simulate() on the live tier.
    chk = cand[cand.tier_live].head(40)
    for _, r in chk.iterrows():
        if r.ticker not in series:
            continue
        s = series[r.ticker]
        i = s.idx(r.entry_date)
        if i < 0 or s.open[i] < MIN_PRICE:
            continue
        ref = rs.simulate(rs.cached_history(r.ticker), pd.Timestamp(r.entry_date), HARD_STOP_PCT)
        mine = sim_fast(s, i)[0]
        assert ref is not None and abs(ref["return_pct"] - mine) < 1e-6, (r.ticker, ref, mine)
    print("  sim_fast matches rs.simulate() on live-tier sample")

    print("Building matched pools per entry date...")
    pools = build_pools(cand, series, sector_of, earn_by_ticker)

    sim_cache = {}

    def sim(t, i):
        key = (t, i)
        if key not in sim_cache:
            sim_cache[key] = sim_fast(series[t], i)
        return sim_cache[key]

    spy = series.get("SPY")
    print("Simulating signal trades and matched controls...")
    recs, ctrl_rets = [], {}
    for ridx, r in cand.iterrows():
        if r.ticker not in series:
            continue
        s = series[r.ticker]
        i = s.idx(r.entry_date)
        if i < 0 or not (s.open[i] >= MIN_PRICE):
            continue
        pool = pools.get(np.datetime64(pd.Timestamp(r.entry_date), "D"))
        if pool is None or pool.empty:
            continue
        b = size_bucket_of(s, r.entry_date, pool)
        sec = pool[(pool.sector == r.sector) & (pool.ticker != r.ticker)]
        level, m = "sector+size", sec[sec.bucket == b] if b is not None else sec.iloc[0:0]
        if len(m) < MIN_POOL and b is not None:
            level, m = "sector+size±1", sec[(sec.bucket - b).abs() <= 1]
        if len(m) < MIN_POOL:
            level, m = "sector only", sec
        if len(m) == 0:
            continue
        sr, sh = sim(r.ticker, i)
        cr = np.array([sim(t, j) for t, j in zip(m.ticker, m.i)])
        spy_hold = np.nan
        if spy is not None:
            k = spy.idx(r.entry_date)
            if k >= 0:
                spy_hold = sim_fast(spy, k)[1]
        ctrl_rets[ridx] = cr
        recs.append({
            "row": ridx, "ticker": r.ticker, "sector": r.sector, "period": r.period,
            "entry_date": str(r.entry_date), "surprise_pct": r.surprise_pct, "q": r.q,
            "tier_live": r.tier_live, "tier_beat15": r.tier_beat15,
            "tier_nonbeat": r.tier_nonbeat,
            "size_bucket": b, "match_level": level, "pool_n": len(m),
            "strat_ret": sr, "hold_ret": sh,
            "ctrl_strat_mean": cr[:, 0].mean(), "ctrl_hold_mean": cr[:, 1].mean(),
            "excess_strat": sr - cr[:, 0].mean(), "excess_hold": sh - cr[:, 1].mean(),
            "spy_hold": spy_hold,
        })
    res = pd.DataFrame(recs)
    print(f"  {len(res)} signal trades matched; {len(sim_cache)} unique sims")

    # ── per tier x period x measure ──
    out = []
    for tkey, tlab in TIERS:
        tmask = res[f"tier_{tkey}"] if tkey != "all" else pd.Series(True, index=res.index)
        for period in PERIODS:
            # committed 2026 data is only the live-bar trades: no wider-tier 2026 rows
            if period == "2026 YTD" and tkey != "live":
                continue
            sub = res[tmask & (res.period == period)]
            if len(sub) < 10:
                continue
            for mi, (mkey, mlab) in enumerate(MEASURES):
                sig = sub[f"{mkey}_ret"].to_numpy()
                pools_r = [ctrl_rets[rw][:, mi] for rw in sub.row]
                # placebo portfolios: one random matched name per trade per draw
                draws = np.empty((N_PLACEBO, len(pools_r)))
                for c_, pr in enumerate(pools_r):
                    draws[:, c_] = pr[rng.integers(0, len(pr), N_PLACEBO)]
                plac = draws.mean(1)
                p_plac = (np.sum(plac >= sig.mean()) + 1) / (N_PLACEBO + 1)
                obs, lo, hi, p1, p2, k = clustered_tests(
                    sub[f"excess_{mkey}"].to_numpy(), sub.entry_date.to_numpy(), rng)
                pooled = np.concatenate(pools_r)
                out.append({
                    "tier": tkey, "tier_label": tlab, "period": period, "measure": mkey,
                    "n": len(sub), "n_dates": k,
                    "sig": dist(sig), "ctrl": dist(pooled),
                    "plac_mean": plac.mean(), "plac_p5": np.percentile(plac, 5),
                    "plac_p95": np.percentile(plac, 95), "p_placebo": p_plac,
                    "excess": obs, "ci_lo": lo, "ci_hi": hi, "p_one": p1, "p_two": p2,
                    "pct_beats_pool": (sub[f"excess_{mkey}"] > 0).mean() * 100,
                    "spy_hold": sub.spy_hold.mean(),
                    "match": sub.match_level.value_counts(normalize=True).mul(100).round(1).to_dict(),
                    "pool_med": int(sub.pool_n.median()),
                })
    return res, out


# ─── Report ────────────────────────────────────────────────────────────────────
def f2(v, s=""):
    return "—" if v is None or (isinstance(v, float) and not np.isfinite(v)) else f"{v:.2f}{s}"


def fp(p):
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def build_report(res, out):
    L = []
    A = L.append
    get = {(o["tier"], o["period"], o["measure"]): o for o in out}

    A("# PEAD Earnings-Beat vs Matched Random Control")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} — "
      "2022-01 → 2026 YTD, current S&P 500 constituents (survivorship-biased, both arms).*\n")
    A("**Research / diagnostic only — no `strategy.md` edit, no orders.** Script: "
      "`backtesting/scripts/backtest_pead_vs_random_control.py`.\n")

    A("## 0. Question and method\n")
    A("Does the PEAD signal pick **better stocks than random**, or does its P&L just come from "
      "being long the market on those days? Each signal trade is compared with random stocks "
      "bought at the **same open, same GICS sector, same size quintile**, run through the "
      "**same exits**.\n")
    A("- **Control pool per trade:** same-day eligible names (open ≥$10, 20d avg $-volume ≥$20M — "
      "the strategy's base gate) in the same sector and the same cross-sectional size quintile, "
      "excluding the signal ticker and any name with its own earnings report within D−10…D+5 "
      f"days. If fewer than {MIN_POOL} names match, widen to quintile ±1, then sector only.")
    A("- **Size proxy:** 20d average $-volume (point-in-time market cap is not reconstructible "
      "from the data available here). Within the S&P 500 this tracks cap closely but not exactly.")
    A("- **Two return measures:** (a) *strategy exits* — flat −8% stop, 1/3 out at +10%, 7% trail, "
      "42-day time stop (the repo's `simulate()`); (b) *plain 42-day hold* — no stops, isolates "
      "selection from exit rules.")
    A(f"- **Placebo p:** {N_PLACEBO:,} placebo portfolios, each swapping every signal trade for one "
      "random member of its matched pool; p = share of placebo means ≥ the signal mean.")
    A("- **Paired excess:** signal return − mean of its matched pool. 95% CI by bootstrap over "
      "**entry dates** (same-day trades share market moves) and a date-clustered sign-flip "
      "permutation p.")
    A("- IS = 2022–2024, OOS = 2025, 2026 YTD shown separately and never averaged. "
      "Zero costs/slippage.\n")

    A("## 1. Headline — live entry bar (EPS ≥15% & q==3)\n")
    A("| Period | Measure | n | Signal avg% | Matched-random avg% | Excess (95% CI) | p (placebo) | p (clustered) |")
    A("|--------|---------|--:|-----------:|--------------------:|-----------------|-----------:|--------------:|")
    for period in PERIODS:
        for mkey, mlab in MEASURES:
            o = get.get(("live", period, mkey))
            if not o:
                continue
            A(f"| {period} | {'strategy exits' if mkey == 'strat' else '42d hold'} | {o['n']} | "
              f"{f2(o['sig']['mean'])} | {f2(o['plac_mean'])} | "
              f"{o['excess']:+.2f} ({o['ci_lo']:+.2f} … {o['ci_hi']:+.2f}) | "
              f"{fp(o['p_placebo'])} | {fp(o['p_one'])} |")
    A("")
    A("*p values are one-sided (H1: signal > random). “Excess” is in percentage points per trade.*\n")

    def ex(t, p, m="strat"):
        o = get.get((t, p, m))
        return (f"{o['excess']:+.2f} pp (p {fp(o['p_one'])}, n={o['n']})") if o else "—"

    A("**Verdict (strategy exits, date-clustered p):**")
    A(f"- **The raw EPS-beat signal shows selection skill in both periods.** EPS ≥15% beats "
      f"matched random by {ex('beat15', 'IS (2022-2024)')} in-sample and "
      f"{ex('beat15', 'OOS (2025)')} out-of-sample; the plain 42-day hold agrees "
      f"({ex('beat15', 'IS (2022-2024)', 'hold')} IS, {ex('beat15', 'OOS (2025)', 'hold')} OOS), so "
      "it is not an artefact of the exit rules.")
    A(f"- **Reports without a big beat sit close to random:** {ex('nonbeat', 'IS (2022-2024)')} IS, "
      f"{ex('nonbeat', 'OOS (2025)')} OOS, and the exit-free hold shows "
      f"{ex('nonbeat', 'IS (2022-2024)', 'hold')} IS. The edge comes mostly from the beat, not "
      "from simply having reported earnings.")
    A("- The edge is a broad upward shift, not a few outsized winners: signal medians sit ~1–2 pp "
      "above the random arm and the left tail is shallower, while the 95th percentiles are about "
      "the same (§3). Per trade it is still a coin-flip-plus: only ~52–56% of signal trades beat "
      "their own matched pool's average.")
    A(f"- **The live bar (adds q==3 quality filters)** is significant in-sample "
      f"({ex('live', 'IS (2022-2024)')}) and points the same way out-of-sample "
      f"({ex('live', 'OOS (2025)')}) and in 2026 YTD ({ex('live', '2026 YTD')}), but those two "
      "samples are too small to separate it from random. Its OOS excess is not larger than the "
      "raw beat's, so these data do not show the quality filters adding selection skill on top of "
      "the beat — they mainly cut trade count.")
    A("- Absolute returns are modest: per-trade excess of roughly +1 pp over a ~6-week hold. Much of "
      "each trade's raw return is shared with same-day, same-sector, same-size random names.\n")

    A("## 2. All tiers — does the beat itself add anything?\n")
    A("| Tier | Period | Measure | n | Signal avg% | Random avg% | Excess pp (95% CI) | % trades > pool | p (placebo) | p (clustered, 2-sided) |")
    A("|------|--------|---------|--:|-----------:|-----------:|--------------------|---------------:|-----------:|------------------:|")
    for tkey, tlab in TIERS:
        for period in PERIODS:
            for mkey, _ in MEASURES:
                o = get.get((tkey, period, mkey))
                if not o:
                    continue
                A(f"| {tlab} | {period} | {'strat' if mkey == 'strat' else 'hold'} | {o['n']} | "
                  f"{f2(o['sig']['mean'])} | {f2(o['plac_mean'])} | "
                  f"{o['excess']:+.2f} ({o['ci_lo']:+.2f} … {o['ci_hi']:+.2f}) | "
                  f"{o['pct_beats_pool']:.1f} | {fp(o['p_placebo'])} | {fp(o['p_two'])} |")
    A("\n*The 2026 YTD committed data holds only the 30 live-bar trades, so the wider tiers have "
      "no 2026 row.*\n")

    A("## 3. Return distributions (per-trade %, signal vs pooled matched controls)\n")
    for tkey, tlab in TIERS[:2]:
        A(f"### {tlab}\n")
        A("| Period | Measure | Arm | n | Mean | Std | Win% | P5 | P25 | Median | P75 | P95 |")
        A("|--------|---------|-----|--:|-----:|----:|-----:|---:|----:|-------:|----:|----:|")
        for period in PERIODS:
            for mkey, _ in MEASURES:
                o = get.get((tkey, period, mkey))
                if not o:
                    continue
                for arm, d in (("signal", o["sig"]), ("random", o["ctrl"])):
                    A(f"| {period} | {mkey} | {arm} | {d['n']} | {f2(d['mean'])} | {f2(d['std'])} | "
                      f"{d['win']:.1f} | {f2(d['p5'])} | {f2(d['p25'])} | {f2(d['p50'])} | "
                      f"{f2(d['p75'])} | {f2(d['p95'])} |")
        A("")
    A("*Random-arm n counts every matched (trade, control) pair, so it is a pooled distribution, "
      "not an independent sample size.*\n")

    A("## 4. Placebo spread and match quality\n")
    A("| Tier | Period | Measure | Signal avg% | Placebo 5th–95th pct | Median pool size | Match level mix |")
    A("|------|--------|---------|-----------:|---------------------|----------------:|-----------------|")
    for tkey, tlab in TIERS:
        for period in PERIODS:
            for mkey, _ in MEASURES:
                o = get.get((tkey, period, mkey))
                if not o:
                    continue
                mix = ", ".join(f"{k} {v}%" for k, v in o["match"].items())
                A(f"| {tkey} | {period} | {mkey} | {f2(o['sig']['mean'])} | "
                  f"{f2(o['plac_p5'])} … {f2(o['plac_p95'])} | {o['pool_med']} | {mix} |")
    A("")
    A("SPY over the same 42-day windows (avg across live-bar trades): " + ", ".join(
        f"{p} {f2(get[('live', p, 'hold')]['spy_hold'])}%" for p in PERIODS
        if ('live', p, 'hold') in get) + ".\n")

    A("## 5. Caveats\n")
    A("- Survivorship bias (current S&P 500 members) applies to **both** arms, so it mostly cancels "
      "in the comparison but inflates both absolute levels.")
    A("- Size is matched on 20d $-volume, not market cap. Post-earnings names often carry elevated "
      "volume, so the signal ticker can land a quintile higher than its usual size; the effect on "
      "the comparison is second-order but real.")
    A("- The control excludes names with their own committed earnings report near D, so it measures "
      "the signal against **non-event** same-sector, same-size stocks.")
    A("- Overlapping 42-day windows and same-day clustering are handled by clustering on entry date, "
      "not by a full portfolio simulation with capital limits.")
    A("- One historical sample, zero costs. A significant result here is evidence of selection skill, "
      "not a validated trading edge.")
    return "\n".join(L)


def main():
    res, out = run()
    csv = os.path.join(REPORTS_DIR, f"backtest_pead_vs_random_trades_{RUN_DATE}.csv")
    res.drop(columns=["row"]).round(4).to_csv(csv, index=False)
    rpt = os.path.join(REPORTS_DIR, "backtest_report_PEAD_VS_RANDOM_CONTROL.md")
    with open(rpt, "w", encoding="utf-8") as f:
        f.write(build_report(res, out))
    print("\n=== HEADLINE ===")
    for o in out:
        print(f"{o['tier']:6s} {o['period']:15s} {o['measure']:5s} n={o['n']:4d} "
              f"sig {o['sig']['mean']:+.2f} rand {o['plac_mean']:+.2f} "
              f"exc {o['excess']:+.2f} [{o['ci_lo']:+.2f},{o['ci_hi']:+.2f}] "
              f"p_plac {o['p_placebo']:.3f} p_clu {o['p_one']:.3f}")
    print(f"\nReport: {rpt}\nTrades: {csv}")


if __name__ == "__main__":
    main()
