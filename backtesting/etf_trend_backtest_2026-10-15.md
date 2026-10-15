# ETF swing / trend backtest — 2026-10-15

Research only. No change to `memory/strategy.md`, no orders, no live routine touched. Script: `backtesting/scripts/backtest_etf_trend.py` (data + GATE 0: `backtesting/scripts/etf_data.py`).

Data through **2026-10-14** (last completed daily bar). IS = 2006-01-03 → 2017-12-29, OOS = 2018-01-02 → 2026-10-14.

## Summary (post-hoc commentary on the pre-registered results)

| Strategy | Pre-registered verdict | What actually carries it |
|---|---|---|
| A pullback | **PASS** vs random-entry control | Beats matched random entries on both Sharpe and CAGR/|DD| in both periods (98th–99th pct of 200 control runs IS, 82nd–88th pct OOS — OOS is *not* significant at 95%). In absolute terms it is a low-return sleeve: 3.1% CAGR / 0.44 Sharpe OOS at ~24% exposure, well below SPY's 0.81 Sharpe. |
| B time-series trend | **PASS** vs EW buy-and-hold | Drawdown: −14.8% vs −45.4% IS, −12.1% vs −29.6% OOS, for ~4.6 pts/yr less CAGR OOS. Sharpe ≈ benchmark OOS (0.80 vs 0.77; SPY 0.81). It is a drawdown tool, not a return enhancer. |
| C momentum | **PASS** (narrowly) vs EW buy-and-hold | Passes **only** on CAGR/|DD|; its Sharpe is *below* EW buy-and-hold in both periods (0.58 vs 0.60 IS, 0.64 vs 0.77 OOS). OOS margin is 0.42 vs 0.40 and it loses to SPY (0.43). Weakest of the three. |

None of the three beats SPY's raw CAGR in OOS (and per the brief they are not judged on that). No grid cell is flagged OVERFIT (no cell wins OOS while losing IS). Several cells pass IS only and decay OOS (A RSI<15/T=5; B 1/k-SMA100; C 6-1/top3, 9-1/top3, 9-1/top5) — evidence that the shorter-lookback / looser variants were IS-favourable, and a reason not to swap to any of them.

## GATE 0 — data / transport check

Transport: `requests` + Yahoo v8 chart API (browser User-Agent, query1→query2 fallback), same as the other research scripts in this repo. Live fetch, cache bypassed.

- Control ticker SPY fetched live: 5732 bars, 2004-01-02 -> 2026-10-14, last AdjClose 769.60.
- SPY dividends since 2004-01-01: 92 ex-dates; max |AdjClose return - (Close+Div)/prevClose return| on ex-dates = 2.52 bp (median 0.20 bp).
- SPY total-return multiple 10.48x vs price-only 6.92x (difference = reinvested dividends).

| ETF | first bar | bars | max cal-day gap | splits in data | max |1d adj ret| (date) | non-dividend AdjClose/Close factor jumps |
|---|---|---|---|---|---|---|
| SPY | 2004-01-02 | 5480 | 5d | none | +14.5% (2008-10-13) | 0 |
| QQQ | 2004-01-02 | 5480 | 5d | none | +12.2% (2008-10-13) | 0 |
| IWM | 2004-01-02 | 5480 | 5d | 2005-06-09 2:1 | -13.3% (2020-03-16) | 0 |
| EFA | 2004-01-02 | 5480 | 5d | 2005-06-09 3:1 | +15.9% (2008-10-13) | 0 |
| EEM | 2004-01-02 | 5480 | 5d | 2005-06-09 3:1, 2008-07-24 3:1 | +22.8% (2008-10-13) | 0 |
| TLT | 2004-01-02 | 5480 | 5d | none | +7.5% (2020-03-20) | 0 |
| GLD | 2004-11-18 | 5480 | 5d | none | +11.3% (2008-09-17) | 0 |
| XLK | 2004-01-02 | 5480 | 5d | 2025-12-05 2:1 | +13.9% (2008-10-28) | 0 |
| XLF | 2004-01-02 | 5480 | 5d | 2016-09-19 1.231:1 | -16.7% (2008-12-01) | 0 |
| XLE | 2004-01-02 | 5480 | 5d | 2025-12-05 2:1 | -20.1% (2020-03-09) | 0 |
| XLV | 2004-01-02 | 5480 | 5d | none | +12.1% (2008-10-13) | 0 |
| XLY | 2004-01-02 | 5480 | 5d | 2025-12-05 2:1 | -12.7% (2020-03-16) | 0 |
| XLP | 2004-01-02 | 5480 | 5d | none | -9.4% (2020-03-12) | 0 |
| XLI | 2004-01-02 | 5480 | 5d | none | +12.7% (2020-03-24) | 0 |
| XLB | 2004-01-02 | 5480 | 5d | 2025-12-05 2:1 | +14.1% (2008-10-13) | 0 |
| XLU | 2004-01-02 | 5480 | 5d | 2025-12-05 2:1 | +12.8% (2020-03-17) | 0 |

Checks: (1) on every SPY ex-dividend date the AdjClose return equals (Close + Div) / prevClose − 1 to within 10 bp (it does, max 2.5 bp) → AdjClose is a continuous total-return series; (2) the AdjClose/Close factor changes only on dividend ex-dates for all 16 ETFs (0 unexplained jumps); (3) no split date shows a >20% jump in the split-adjusted close (IWM/EFA/EEM 2005, EEM 2008, the five SPDR sector 2:1 splits on 2025-12-05 are all continuous; XLF's 2016-09-19 '1.231:1' is the XLRE special distribution, which Yahoo encodes as a split and which is also continuous); (4) all 16 ETFs have a bar on 2005-01-03, no NaN rows and no missing SPY dates since then. Largest one-day moves are the known Oct-2008 / Mar-2020 days. **GATE 0: PASS.**

## Pre-registered definitions

Fixed in code before any result was viewed (a smoke run of the pre-registered configs was used only to check mechanics; no definition, parameter, benchmark or pass rule was changed after it).

- **Prices.** Signals and returns on Yahoo AdjClose (split + dividend adjusted). Fills at the next day's open: Yahoo's open (split-adjusted, not dividend-adjusted) converted to the total-return basis with that day's AdjClose/Close factor, so fill and mark share one basis. 5 bp per side on every fill (including monthly rebalance trades). Cash earns 0% (this penalises the strategies that sit in cash, most of all in OOS where T-bills paid 2–5%).
- **Timing.** Every signal uses data through close *t*; every fill is the open of *t+1*. Monthly strategies decide on the last trading day's close and trade at the first open of the next month.
- **A — pullback in uptrend.** Entry when close > SMA200, SMA50 > SMA200, close ≤ SMA20 and RSI(2) < 10 (Wilder smoothing). Exit at the next open after: close > SMA5, or the 10th trading day held, or close ≤ entry × 0.92 (the −8% stop is evaluated on the close, consistent with the close-t/open-t+1 rule; realised losses can exceed 8% on gaps). 5 slots × 20% of prior-close equity; if more signals than free slots, most-oversold RSI(2) first; one position per ETF.
- **B — time-series trend.** Each ETF has a fixed 1/16 sleeve. At each month-end close the sleeve is long if close > SMA200, else cash; held sleeves are rebalanced back to 1/16. (Reading of "equal weight across ETFs that qualify": equal 1/16 weight per qualifying ETF, the rest in cash — the per-asset time-series definition, directly comparable to the equal-weight universe. The alternative 1/k re-normalisation is shown as a labelled sensitivity, not the pre-registered config.)
- **C — cross-sectional momentum.** Month-end ranking by 12-1 month total return (AdjClose[t−21] / AdjClose[t−252] − 1, 21 trading days per month). Top 3 get 1/3 each; a slot whose ETF closes below its SMA200 is held in cash (the 4th-ranked ETF is not promoted).
- **Benchmarks.** SPY buy-and-hold (total return) and equal-weight buy-and-hold of the 16 ETFs (1/16 each at the period's first open, never rebalanced), each bought fresh at the start of IS and of OOS with the same 5 bp entry cost. Monthly-rebalanced equal weight is shown for information. For A: a random-entry control (200 simulations, seed 20261015) — for each A trade, a random ETF and random entry date within the same period, the same holding length, the same 20% slot size, the same 5-slot cap and one-position-per-ETF rule, the same costs. This matches A's trade count, holding-period distribution and exposure.
- **Primary benchmark per strategy (for the pass rule).** A → random-entry control (median of the simulations); B → equal-weight buy-and-hold of the universe (same assets, same weights, only the trend filter differs); C → equal-weight buy-and-hold of the universe (same opportunity set). SPY is reported for every strategy as a secondary reference.
- **Pass rule.** The pre-registered config beats its primary benchmark on Sharpe **or** on CAGR/|MaxDD| in **both** IS and OOS. Grid cells are reported but cannot rescue a failing pre-registered config.
- **Periods.** All strategies run continuously from 2006-01-03 (indicators warmed up on 2004–2005 data) and are sliced at 2017-12-31; trade statistics are assigned to the period of the trade's entry. Sharpe is annualised from daily returns with rf = 0. Max drawdown is on the daily mark-to-market equity.

## Pass / fail (pre-registered configs only)

| Strategy | Primary benchmark | IS: strat Sharpe / bench | IS: strat CAGR/|DD| / bench | IS beats? | OOS: strat Sharpe / bench | OOS: strat CAGR/|DD| / bench | OOS beats? | **Verdict** |
|---|---|---|---|---|---|---|---|---|
| A | random-entry control (median) | 0.61 / 0.12 | 0.38 / 0.03 | yes | 0.45 / 0.22 | 0.27 / 0.07 | yes | **PASS** |
| B | EW buy-and-hold | 0.82 / 0.60 | 0.55 / 0.19 | yes | 0.80 / 0.77 | 0.59 / 0.40 | yes | **PASS** |
| C | EW buy-and-hold | 0.58 / 0.60 | 0.32 / 0.19 | yes | 0.64 / 0.77 | 0.42 / 0.40 | yes | **PASS** |

## IS 2006-2017

| Series | CAGR | Sharpe | MaxDD | CAGR/|MaxDD| | Avg exposure | Trades | Win % | PF |
|---|---|---|---|---|---|---|---|---|
| A pullback (RSI2<10, T=10) | 4.0% | 0.61 | -10.6% | 0.38 | 22% | 903 | 67% | 1.53 |
| B trend (SMA200, 1/16 sleeves) | 8.1% | 0.82 | -14.8% | 0.55 | 74% | 158 | 56% | 5.80 |
| C momentum (12-1, top 3) | 8.1% | 0.58 | -25.5% | 0.32 | 89% | 129 | 61% | 2.26 |
| SPY buy-and-hold | 8.7% | 0.53 | -55.2% | 0.16 | 100% | — | — | — |
| EW buy-and-hold (16 ETFs) | 8.6% | 0.60 | -45.4% | 0.19 | 100% | — | — | — |
| EW monthly-rebalanced (info) | 9.0% | 0.59 | -48.3% | 0.19 | 100% | — | — | — |
| A random-entry control (median of 200) | 0.5% | 0.12 | -19.6% | 0.03 | 22% | 903 | 53% | 1.06 |

A vs random control: A's Sharpe beats 98% of control runs (control Sharpe 5th–95th pct -0.17 – 0.44); A's CAGR/|DD| beats 98% (-0.05 – 0.21). Control avg exposure 22% vs A 22%; control avg trade 0.05% vs A 0.27%.

## OOS 2018-latest

| Series | CAGR | Sharpe | MaxDD | CAGR/|MaxDD| | Avg exposure | Trades | Win % | PF |
|---|---|---|---|---|---|---|---|---|
| A pullback (RSI2<10, T=10) | 3.2% | 0.45 | -12.0% | 0.27 | 24% | 696 | 65% | 1.30 |
| B trend (SMA200, 1/16 sleeves) | 7.1% | 0.80 | -12.1% | 0.59 | 71% | 145 | 43% | 3.88 |
| C momentum (12-1, top 3) | 9.9% | 0.64 | -23.4% | 0.42 | 91% | 79 | 53% | 2.53 |
| SPY buy-and-hold | 14.5% | 0.81 | -33.7% | 0.43 | 100% | — | — | — |
| EW buy-and-hold (16 ETFs) | 11.7% | 0.77 | -29.6% | 0.40 | 100% | — | — | — |
| EW monthly-rebalanced (info) | 11.4% | 0.76 | -30.9% | 0.37 | 100% | — | — | — |
| A random-entry control (median of 200) | 1.1% | 0.22 | -13.0% | 0.07 | 24% | 695 | 53% | 1.10 |

A vs random control: A's Sharpe beats 83% of control runs (control Sharpe 5th–95th pct -0.20 – 0.57); A's CAGR/|DD| beats 87% (-0.07 – 0.33). Control avg exposure 24% vs A 24%; control avg trade 0.08% vs A 0.21%.

## Full period 2006 → latest (information only, not part of the pass rule)

| Series | CAGR | Sharpe | MaxDD | CAGR/|MaxDD| | Avg exposure | Trades | Win % | PF |
|---|---|---|---|---|---|---|---|---|
| A pullback (RSI2<10, T=10) | 3.7% | 0.54 | -12.0% | 0.31 | 23% | 1599 | 66% | 1.41 |
| B trend (SMA200, 1/16 sleeves) | 7.7% | 0.81 | -14.8% | 0.52 | 73% | 303 | 50% | 4.79 |
| C momentum (12-1, top 3) | 8.9% | 0.60 | -25.5% | 0.35 | 90% | 208 | 58% | 2.38 |
| SPY buy-and-hold | 11.2% | 0.65 | -55.2% | 0.20 | 100% | — | — | — |
| EW buy-and-hold (16 ETFs) | 10.4% | 0.68 | -45.4% | 0.23 | 100% | — | — | — |

## Strategy A — trade-level expectancy and outlier dependence

Net per-trade return (after 5 bp × 2), trades assigned by entry date.

| Period | Trades | Win % | Avg win | Avg loss | Expectancy | Excl. best trade | Excl. best 5 | Sum of returns | Sum excl. best 5 | Avg days held | Trades ≤ −8% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IS 2006-2017 | 903 | 67% | 1.19% | -1.55% | 0.274% | 0.269% | 0.249% | 247% | 224% | 3.7 | 10 |
| OOS 2018-latest | 696 | 65% | 1.41% | -2.03% | 0.213% | 0.197% | 0.160% | 148% | 111% | 3.8 | 15 |
| Full | 1599 | 66% | 1.28% | -1.76% | 0.247% | 0.240% | 0.224% | 395% | 358% | 3.7 | 25 |

Best 5 trades (full period): XLK 2020-02-28 11.5%; QQQ 2020-02-28 9.2%; XLB 2020-10-28 6.1%; XLE 2022-08-05 5.9%; EEM 2020-02-03 5.1%.

A by ETF (full period): XLP n=121 avg 0.10%; GLD n=110 avg 0.23%; XLU n=109 avg -0.15%; XLB n=108 avg 0.09%; XLI n=105 avg 0.34%; XLE n=103 avg 0.45%; TLT n=102 avg 0.10%; XLV n=100 avg 0.10%; XLY n=99 avg 0.38%; XLF n=97 avg 0.40%; QQQ n=96 avg 0.60%; EFA n=95 avg 0.02%; EEM n=92 avg 0.43%; IWM n=90 avg 0.22%; SPY n=86 avg 0.27%; XLK n=86 avg 0.51%.

## Sensitivity grids (labelled; the pre-registered cell is marked ★)

A cell "passes" with the same rule as above against the same primary benchmark. **OVERFIT** = wins OOS but loses IS. Grid cells never override the pre-registered verdict.

### A — RSI(2) threshold × time stop (benchmark: random-entry control matched to each cell, 100 sims)

| RSI(2) < | Time stop | IS Sharpe (ctrl) | IS CAGR/|DD| (ctrl) | IS trades | OOS Sharpe (ctrl) | OOS CAGR/|DD| (ctrl) | OOS trades | Result |
|---|---|---|---|---|---|---|---|---|
| 5 | 5 | 0.32 (0.09) | 0.16 (0.02) | 547 | 0.33 (0.18) | 0.13 (0.05) | 462 | pass both |
| 5 | 10 | 0.43 (0.11) | 0.19 (0.02) | 530 | 0.41 (0.10) | 0.22 (0.03) | 447 | pass both |
| 5 | 15 | 0.45 (0.15) | 0.20 (0.04) | 526 | 0.42 (0.20) | 0.23 (0.08) | 446 | pass both |
| 10 | 5 | 0.51 (0.08) | 0.31 (0.02) | 957 | 0.24 (0.11) | 0.09 (0.03) | 735 | pass both |
| 10 ★ | 10 | 0.61 (0.15) | 0.38 (0.04) | 903 | 0.45 (0.17) | 0.27 (0.06) | 696 | pass both |
| 10 | 15 | 0.60 (0.17) | 0.37 (0.05) | 896 | 0.43 (0.26) | 0.25 (0.11) | 690 | pass both |
| 15 | 5 | 0.43 (0.14) | 0.25 (0.04) | 1239 | 0.09 (0.17) | 0.02 (0.06) | 944 | IS only (decays OOS) |
| 15 | 10 | 0.55 (0.17) | 0.32 (0.04) | 1145 | 0.28 (0.21) | 0.12 (0.08) | 873 | pass both |
| 15 | 15 | 0.54 (0.12) | 0.31 (0.03) | 1136 | 0.27 (0.25) | 0.11 (0.10) | 868 | pass both |

### B — SMA length (benchmark: EW buy-and-hold)

| SMA | Weighting | IS CAGR | IS Sharpe | IS MaxDD | IS CAGR/|DD| | OOS CAGR | OOS Sharpe | OOS MaxDD | OOS CAGR/|DD| | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 1/16 sleeves | 8.0% | 0.86 | -11.9% | 0.67 | 5.6% | 0.66 | -12.8% | 0.44 | pass both |
| 150 | 1/16 sleeves | 8.4% | 0.89 | -13.6% | 0.62 | 7.0% | 0.79 | -11.3% | 0.62 | pass both |
| 200 ★ | 1/16 sleeves | 8.1% | 0.82 | -14.8% | 0.55 | 7.1% | 0.80 | -12.1% | 0.59 | pass both |
| 100 | 1/k of qualifiers (sensitivity) | 11.4% | 0.87 | -21.5% | 0.53 | 8.5% | 0.66 | -26.5% | 0.32 | IS only (decays OOS) |
| 150 | 1/k of qualifiers (sensitivity) | 11.1% | 0.84 | -25.2% | 0.44 | 9.1% | 0.70 | -20.2% | 0.45 | pass both |
| 200 | 1/k of qualifiers (sensitivity) | 9.4% | 0.72 | -29.5% | 0.32 | 9.8% | 0.75 | -20.0% | 0.49 | pass both |

### C — lookback × N (benchmark: EW buy-and-hold)

| Lookback | N | IS CAGR | IS Sharpe | IS MaxDD | IS CAGR/|DD| | OOS CAGR | OOS Sharpe | OOS MaxDD | OOS CAGR/|DD| | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| 6-1 | 3 | 10.1% | 0.71 | -20.8% | 0.49 | 6.9% | 0.48 | -24.3% | 0.29 | IS only (decays OOS) |
| 6-1 | 5 | 9.4% | 0.72 | -18.6% | 0.51 | 7.5% | 0.58 | -18.6% | 0.40 | pass both |
| 9-1 | 3 | 7.8% | 0.57 | -23.7% | 0.33 | 5.6% | 0.40 | -27.1% | 0.20 | IS only (decays OOS) |
| 9-1 | 5 | 8.3% | 0.64 | -23.7% | 0.35 | 7.7% | 0.59 | -22.1% | 0.35 | IS only (decays OOS) |
| 12-1 ★ | 3 | 8.1% | 0.58 | -25.5% | 0.32 | 9.9% | 0.64 | -23.4% | 0.42 | pass both |
| 12-1 | 5 | 9.4% | 0.72 | -19.1% | 0.49 | 9.8% | 0.73 | -19.6% | 0.50 | pass both |

Benchmarks for B/C grid: IS EW B&H Sharpe 0.60, CAGR/|DD| 0.19; OOS EW B&H Sharpe 0.77, CAGR/|DD| 0.40.

## Calendar-year returns (pre-registered configs; benchmarks bought 2006-01-03)

| Year | A | B | C | SPY | EW B&H |
|---|---|---|---|---|---|
| 2006 | 5.6% | 12.9% | 23.1% | 15.2% | 15.9% |
| 2007 | 6.6% | 12.1% | 19.8% | 5.1% | 12.6% |
| 2008 | -5.9% | -8.9% | -4.7% | -36.8% | -30.4% |
| 2009 | 10.3% | 20.7% | 19.4% | 26.4% | 25.3% |
| 2010 | 1.7% | 3.6% | -6.4% | 15.1% | 17.4% |
| 2011 | 1.9% | 2.9% | -6.6% | 1.9% | 3.2% |
| 2012 | 7.5% | 5.9% | -0.1% | 16.0% | 12.7% |
| 2013 | 6.2% | 23.0% | 33.2% | 32.3% | 18.4% |
| 2014 | 3.2% | 9.0% | 15.3% | 13.5% | 10.8% |
| 2015 | 4.6% | -4.7% | -1.1% | 1.2% | -1.2% |
| 2016 | 2.2% | 6.7% | -4.3% | 12.0% | 10.7% |
| 2017 | 5.4% | 18.2% | 20.1% | 21.7% | 20.6% |
| 2018 | -7.3% | -1.7% | 3.5% | -4.6% | -5.4% |
| 2019 | 2.4% | 9.5% | 11.9% | 31.2% | 27.8% |
| 2020 | 8.5% | 10.1% | 8.9% | 18.3% | 20.6% |
| 2021 | 8.6% | 18.4% | 14.1% | 28.7% | 21.9% |
| 2022 | -6.1% | -8.6% | -4.6% | -18.2% | -16.7% |
| 2023 | -1.1% | 3.3% | 3.9% | 26.2% | 22.2% |
| 2024 | 6.1% | 12.9% | 16.5% | 24.9% | 17.3% |
| 2025 | 9.6% | 13.5% | 27.6% | 17.7% | 18.9% |
| 2026 (YTD) | 9.1% | 7.8% | 7.5% | 13.7% | 13.8% |

## Stress windows: 2008, 2020, 2022

| Window | A return / max DD | B return / max DD | C return / max DD | SPY return / max DD | EW B&H return / max DD |
|---|---|---|---|---|---|
| 2008 calendar year | -5.9% / -6.4% | -8.9% / -10.7% | -4.7% / -17.6% | -36.8% / -47.6% | -30.4% / -42.4% |
| GFC peak→trough (SPY 2007-10-09 → 2009-03-09) | -0.6% / -7.5% | -9.9% / -12.5% | -7.6% / -17.6% | -55.2% / -55.2% | -44.8% / -45.4% |
| 2020 calendar year | 8.5% / -8.4% | 10.1% / -11.7% | 8.9% / -23.4% | 18.3% / -33.7% | 20.6% / -29.6% |
| COVID crash (2020-02-19 → 2020-03-23) | -4.6% / -8.4% | -11.0% / -11.7% | -23.4% / -23.4% | -33.7% / -33.7% | -29.6% / -29.6% |
| 2022 calendar year | -6.1% / -7.6% | -8.6% / -9.9% | -4.6% / -14.9% | -18.2% / -24.5% | -16.7% / -23.2% |

Exposure going into each stress window (avg gross exposure in the window): 2008 calendar year: A 9%, B 29%, C 64%; GFC peak→trough: A 11%, B 36%, C 70%; 2020 calendar year: A 16%, B 65%, C 91%; COVID crash: A 30%, B 45%, C 75%; 2022 calendar year: A 13%, B 34%, C 75%.

## Interpretation (post-hoc)

- **B is the most robust result.** Every 1/16-sleeve SMA cell passes both periods, with OOS CAGR/|DD| 0.44–0.62 vs 0.40 and MaxDD −11% to −15% across both periods vs −30% / −45% for the benchmark. Its drawdown cut is visible in all three stress windows (2008 −8.9%, COVID crash −11.0%, 2022 −8.6%). The cost is persistent lag in V-shaped recoveries and strong bull years (2019, 2023: +9.5% / +3.3% vs +27.8% / +22.2% EW) and roughly 26–29% average cash earning 0% here.
- **A's edge is real but small and partly regime-driven.** Expectancy is +0.27% / +0.21% per trade (IS/OOS) net of 5 bp/side; removing the best 5 trades leaves +0.25% / +0.16%, so it is not a single-outlier artefact, but 3 of the 5 best trades are Feb-2020 crash-rebound entries and the OOS profit factor falls from 1.53 to 1.30. At 10 bp/side the OOS expectancy would roughly halve. The random control does not apply A's trend filter, so part of A's advantage over it is simply 'own uptrending ETFs' — the control measures entry-timing + filter jointly, not the pullback trigger alone. A also had two losing years in OOS (2018 −7.3%, 2022 −6.1%), i.e. the SMA200/SMA50 filter did not keep it out of choppy down-years.
- **C's pass is fragile.** It depends on one number per period (MaxDD, set in 2008 IS and the 2020 crash OOS). In the COVID crash C took the full −23.4% because the monthly check left it 75% invested; it underperformed in 2010–2012 and 2016. The 12-1/top-5 cell is better on every metric in both periods, but picking it now would be grid-mining.
- **Correlation of outcomes:** all three cut 2008 and 2022 losses to single digits, so as a portfolio overlay they mostly provide the same thing — reduced equity-beta in sustained bears — rather than independent return streams.

## Limitations

- **Hindsight universe.** The 16 ETFs were chosen today; all survived and remain liquid. Closed, merged or delisted ETFs are absent, which flatters every strategy and both universe benchmarks (and especially momentum, which can only rotate into survivors).
- **No PEAD correlation possible.** The repo's PEAD artefacts are trade-level only (candidate/trade CSVs 2022–2026), not a daily return series over 2006–latest, so the diversification value of these ETF strategies against the live PEAD book cannot be measured here.
- **2008 is the only deep bear in IS.** IS (2006–2017) contains one prolonged bear market (GFC); OOS adds the fast 2020 crash and the 2022 rate bear. Trend filters' drawdown benefit in IS rests largely on a single episode.
- Cash earns 0% (understates B/C/A — all hold substantial cash — relative to buy-and-hold, especially 2018+ and 2023+ when T-bills yielded 2–5%). Sharpe uses rf = 0 for every series.
- A's −8% stop is evaluated on the close and executed next open (no intraday stop), so stop losses can exceed 8%. Fills at the open assume no slippage beyond 5 bp; these ETFs are among the most liquid, so this is reasonable for small size.
- Yahoo's "raw" open is split-adjusted (not truly as-traded); this does not affect returns.
- Taxes, borrow, dividend withholding and intra-month rebalancing drift are not modelled.
- A's grid controls use 100 simulations per cell (200 for the pre-registered config); control medians carry sampling noise of a few hundredths of Sharpe.

## Files

- `backtesting/reports/etf_trend_trades_A_2026-10-15.csv` — every A trade (pre-registered config).
- `backtesting/reports/etf_trend_grid_2026-10-15.csv` — every grid cell × period with metrics and benchmark.
