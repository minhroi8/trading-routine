# PEAD Earnings-Beat vs Matched Random Control

*Generated: 2026-10-15 04:49 — 2022-01 → 2026 YTD, current S&P 500 constituents (survivorship-biased, both arms).*

**Research / diagnostic only — no `strategy.md` edit, no orders.** Script: `backtesting/scripts/backtest_pead_vs_random_control.py`.

## 0. Question and method

Does the PEAD signal pick **better stocks than random**, or does its P&L just come from being long the market on those days? Each signal trade is compared with random stocks bought at the **same open, same GICS sector, same size quintile**, run through the **same exits**.

- **Control pool per trade:** same-day eligible names (open ≥$10, 20d avg $-volume ≥$20M — the strategy's base gate) in the same sector and the same cross-sectional size quintile, excluding the signal ticker and any name with its own earnings report within D−10…D+5 days. If fewer than 5 names match, widen to quintile ±1, then sector only.
- **Size proxy:** 20d average $-volume (point-in-time market cap is not reconstructible from the data available here). Within the S&P 500 this tracks cap closely but not exactly.
- **Two return measures:** (a) *strategy exits* — flat −8% stop, 1/3 out at +10%, 7% trail, 42-day time stop (the repo's `simulate()`); (b) *plain 42-day hold* — no stops, isolates selection from exit rules.
- **Placebo p:** 10,000 placebo portfolios, each swapping every signal trade for one random member of its matched pool; p = share of placebo means ≥ the signal mean.
- **Paired excess:** signal return − mean of its matched pool. 95% CI by bootstrap over **entry dates** (same-day trades share market moves) and a date-clustered sign-flip permutation p.
- IS = 2022–2024, OOS = 2025, 2026 YTD shown separately and never averaged. Zero costs/slippage.

## 1. Headline — live entry bar (EPS ≥15% & q==3)

| Period | Measure | n | Signal avg% | Matched-random avg% | Excess (95% CI) | p (placebo) | p (clustered) |
|--------|---------|--:|-----------:|--------------------:|-----------------|-----------:|--------------:|
| IS (2022-2024) | strategy exits | 192 | 1.82 | 0.35 | +1.48 (+0.37 … +2.52) | 0.002 | 0.006 |
| IS (2022-2024) | 42d hold | 192 | 2.56 | 1.20 | +1.36 (+0.06 … +2.61) | 0.018 | 0.019 |
| OOS (2025) | strategy exits | 52 | 1.43 | 0.41 | +1.02 (-1.49 … +4.10) | 0.204 | 0.237 |
| OOS (2025) | 42d hold | 52 | 1.33 | 0.36 | +0.95 (-2.64 … +5.17) | 0.264 | 0.321 |
| 2026 YTD | strategy exits | 30 | -0.23 | -0.74 | +0.50 (-3.21 … +5.18) | 0.370 | 0.432 |
| 2026 YTD | 42d hold | 30 | 1.82 | -0.29 | +2.09 (-4.22 … +9.63) | 0.160 | 0.305 |

*p values are one-sided (H1: signal > random). “Excess” is in percentage points per trade.*

**Verdict (strategy exits, date-clustered p):**
- **The raw EPS-beat signal shows selection skill in both periods.** EPS ≥15% beats matched random by +0.77 pp (p <0.001, n=1097) in-sample and +1.08 pp (p 0.009, n=380) out-of-sample; the plain 42-day hold agrees (+0.76 pp (p 0.003, n=1097) IS, +1.83 pp (p 0.002, n=380) OOS), so it is not an artefact of the exit rules.
- **Reports without a big beat sit close to random:** +0.25 pp (p 0.031, n=3241) IS, +0.22 pp (p 0.203, n=1079) OOS, and the exit-free hold shows +0.08 pp (p 0.307, n=3241) IS. The edge comes mostly from the beat, not from simply having reported earnings.
- Only ~52–56% of signal trades beat their own matched pool, so the excess comes from a fatter right tail (see §3), not from a higher hit rate.
- **The live bar (adds q==3 quality filters)** is significant in-sample (+1.48 pp (p 0.006, n=192)) and points the same way out-of-sample (+1.02 pp (p 0.237, n=52)) and in 2026 YTD (+0.50 pp (p 0.432, n=30)), but those two samples are too small to separate it from random. Its OOS excess is not larger than the raw beat's, so these data do not show the quality filters adding selection skill on top of the beat — they mainly cut trade count.
- Absolute returns are modest: per-trade excess of roughly +1 pp over a ~6-week hold. Much of each trade's raw return is shared with same-day, same-sector, same-size random names.

## 2. All tiers — does the beat itself add anything?

| Tier | Period | Measure | n | Signal avg% | Random avg% | Excess pp (95% CI) | % trades > pool | p (placebo) | p (clustered, 2-sided) |
|------|--------|---------|--:|-----------:|-----------:|--------------------|---------------:|-----------:|------------------:|
| Live bar (EPS≥15% & q==3) | IS (2022-2024) | strat | 192 | 1.82 | 0.35 | +1.48 (+0.37 … +2.52) | 56.2 | 0.002 | 0.011 |
| Live bar (EPS≥15% & q==3) | IS (2022-2024) | hold | 192 | 2.56 | 1.20 | +1.36 (+0.06 … +2.61) | 55.7 | 0.018 | 0.040 |
| Live bar (EPS≥15% & q==3) | OOS (2025) | strat | 52 | 1.43 | 0.41 | +1.02 (-1.49 … +4.10) | 48.1 | 0.204 | 0.470 |
| Live bar (EPS≥15% & q==3) | OOS (2025) | hold | 52 | 1.33 | 0.36 | +0.95 (-2.64 … +5.17) | 53.8 | 0.264 | 0.632 |
| Live bar (EPS≥15% & q==3) | 2026 YTD | strat | 30 | -0.23 | -0.74 | +0.50 (-3.21 … +5.18) | 46.7 | 0.370 | 0.842 |
| Live bar (EPS≥15% & q==3) | 2026 YTD | hold | 30 | 1.82 | -0.29 | +2.09 (-4.22 … +9.63) | 53.3 | 0.160 | 0.606 |
| Raw beat (EPS≥15%, any q) | IS (2022-2024) | strat | 1097 | 1.28 | 0.52 | +0.77 (+0.30 … +1.23) | 52.7 | <0.001 | 0.002 |
| Raw beat (EPS≥15%, any q) | IS (2022-2024) | hold | 1097 | 1.97 | 1.20 | +0.76 (+0.23 … +1.31) | 52.6 | 0.002 | 0.006 |
| Raw beat (EPS≥15%, any q) | OOS (2025) | strat | 380 | 1.68 | 0.61 | +1.08 (+0.21 … +2.06) | 52.1 | 0.004 | 0.018 |
| Raw beat (EPS≥15%, any q) | OOS (2025) | hold | 380 | 2.64 | 0.80 | +1.83 (+0.65 … +3.15) | 54.2 | <0.001 | 0.003 |
| Non-beat reports (EPS surprise <15%) | IS (2022-2024) | strat | 3241 | 1.14 | 0.88 | +0.25 (-0.01 … +0.51) | 51.0 | 0.024 | 0.059 |
| Non-beat reports (EPS surprise <15%) | IS (2022-2024) | hold | 3241 | 1.64 | 1.55 | +0.08 (-0.23 … +0.39) | 49.8 | 0.292 | 0.597 |
| Non-beat reports (EPS surprise <15%) | OOS (2025) | strat | 1079 | 1.18 | 0.97 | +0.22 (-0.30 … +0.73) | 49.5 | 0.196 | 0.419 |
| Non-beat reports (EPS surprise <15%) | OOS (2025) | hold | 1079 | 1.82 | 1.41 | +0.42 (-0.22 … +1.09) | 51.1 | 0.098 | 0.207 |
| All base candidates (any surprise) | IS (2022-2024) | strat | 4338 | 1.17 | 0.79 | +0.38 (+0.16 … +0.60) | 51.4 | <0.001 | <0.001 |
| All base candidates (any surprise) | IS (2022-2024) | hold | 4338 | 1.72 | 1.46 | +0.26 (-0.01 … +0.51) | 50.5 | 0.026 | 0.058 |
| All base candidates (any surprise) | OOS (2025) | strat | 1459 | 1.31 | 0.87 | +0.44 (+0.01 … +0.90) | 50.2 | 0.021 | 0.048 |
| All base candidates (any surprise) | OOS (2025) | hold | 1459 | 2.04 | 1.25 | +0.79 (+0.20 … +1.41) | 51.9 | 0.002 | 0.012 |

*The 2026 YTD committed data holds only the 30 live-bar trades, so the wider tiers have no 2026 row.*

## 3. Return distributions (per-trade %, signal vs pooled matched controls)

### Live bar (EPS≥15% & q==3)

| Period | Measure | Arm | n | Mean | Std | Win% | P5 | P25 | Median | P75 | P95 |
|--------|---------|-----|--:|-----:|----:|-----:|---:|----:|-------:|----:|----:|
| IS (2022-2024) | strat | signal | 192 | 1.82 | 8.61 | 57.8 | -9.74 | -5.59 | 1.98 | 7.43 | 15.18 |
| IS (2022-2024) | strat | random | 1906 | 0.22 | 9.40 | 49.6 | -11.04 | -8.32 | -0.10 | 6.43 | 14.83 |
| IS (2022-2024) | hold | signal | 192 | 2.56 | 10.51 | 57.3 | -10.82 | -4.01 | 1.69 | 7.58 | 19.76 |
| IS (2022-2024) | hold | random | 1906 | 0.97 | 11.91 | 51.2 | -15.96 | -5.98 | 0.26 | 7.02 | 19.52 |
| OOS (2025) | strat | signal | 52 | 1.43 | 11.04 | 50.0 | -11.06 | -8.17 | -0.09 | 5.83 | 17.12 |
| OOS (2025) | strat | random | 569 | 0.72 | 10.91 | 51.8 | -11.84 | -8.46 | 0.76 | 7.15 | 15.61 |
| OOS (2025) | hold | signal | 52 | 1.33 | 14.80 | 50.0 | -15.45 | -3.29 | -0.09 | 4.68 | 20.68 |
| OOS (2025) | hold | random | 569 | 0.94 | 14.40 | 53.1 | -18.94 | -5.55 | 1.03 | 7.45 | 18.40 |
| 2026 YTD | strat | signal | 30 | -0.23 | 11.04 | 50.0 | -11.41 | -8.64 | -0.61 | 4.95 | 12.24 |
| 2026 YTD | strat | random | 524 | -0.29 | 11.16 | 46.6 | -13.13 | -9.07 | -1.36 | 6.55 | 19.55 |
| 2026 YTD | hold | signal | 30 | 1.82 | 17.88 | 40.0 | -16.74 | -6.98 | -1.70 | 3.58 | 26.65 |
| 2026 YTD | hold | random | 524 | 0.68 | 16.73 | 46.2 | -21.66 | -8.83 | -0.92 | 7.05 | 26.60 |

### Raw beat (EPS≥15%, any q)

| Period | Measure | Arm | n | Mean | Std | Win% | P5 | P25 | Median | P75 | P95 |
|--------|---------|-----|--:|-----:|----:|-----:|---:|----:|-------:|----:|----:|
| IS (2022-2024) | strat | signal | 1097 | 1.28 | 9.01 | 54.8 | -10.31 | -8.17 | 1.72 | 7.76 | 15.08 |
| IS (2022-2024) | strat | random | 10530 | 0.42 | 9.29 | 50.3 | -10.99 | -8.31 | 0.09 | 7.11 | 15.44 |
| IS (2022-2024) | hold | signal | 1097 | 1.97 | 10.99 | 55.5 | -13.93 | -5.06 | 1.56 | 8.24 | 19.36 |
| IS (2022-2024) | hold | random | 10530 | 1.05 | 11.54 | 51.8 | -15.76 | -5.89 | 0.35 | 7.21 | 19.56 |
| OOS (2025) | strat | signal | 380 | 1.68 | 9.88 | 56.8 | -10.41 | -8.16 | 2.30 | 7.67 | 15.56 |
| OOS (2025) | strat | random | 3782 | 0.77 | 9.97 | 52.9 | -11.66 | -8.32 | 0.93 | 7.43 | 16.34 |
| OOS (2025) | hold | signal | 380 | 2.64 | 13.99 | 59.2 | -15.02 | -3.25 | 2.32 | 7.99 | 20.15 |
| OOS (2025) | hold | random | 3782 | 1.29 | 13.15 | 55.0 | -19.12 | -5.39 | 1.26 | 7.80 | 20.94 |

*Random-arm n counts every matched (trade, control) pair, so it is a pooled distribution, not an independent sample size.*

## 4. Placebo spread and match quality

| Tier | Period | Measure | Signal avg% | Placebo 5th–95th pct | Median pool size | Match level mix |
|------|--------|---------|-----------:|---------------------|----------------:|-----------------|
| live | IS (2022-2024) | strat | 1.82 | -0.46 … 1.17 | 9 | sector+size 77.1%, sector+size±1 17.2%, sector only 5.7% |
| live | IS (2022-2024) | hold | 2.56 | 0.18 … 2.24 | 9 | sector+size 77.1%, sector+size±1 17.2%, sector only 5.7% |
| live | OOS (2025) | strat | 1.43 | -1.58 … 2.50 | 9 | sector+size 63.5%, sector+size±1 28.8%, sector only 7.7% |
| live | OOS (2025) | hold | 1.33 | -2.22 … 3.17 | 9 | sector+size 63.5%, sector+size±1 28.8%, sector only 7.7% |
| live | 2026 YTD | strat | -0.23 | -3.26 … 1.78 | 14 | sector+size 93.3%, sector+size±1 6.7% |
| live | 2026 YTD | hold | 1.82 | -3.65 … 3.27 | 14 | sector+size 93.3%, sector+size±1 6.7% |
| beat15 | IS (2022-2024) | strat | 1.28 | 0.17 … 0.86 | 9 | sector+size 69.6%, sector+size±1 24.3%, sector only 6.1% |
| beat15 | IS (2022-2024) | hold | 1.97 | 0.79 … 1.62 | 9 | sector+size 69.6%, sector+size±1 24.3%, sector only 6.1% |
| beat15 | OOS (2025) | strat | 1.68 | -0.03 … 1.25 | 8 | sector+size 67.1%, sector+size±1 23.4%, sector only 9.5% |
| beat15 | OOS (2025) | hold | 2.64 | -0.01 … 1.64 | 8 | sector+size 67.1%, sector+size±1 23.4%, sector only 9.5% |
| nonbeat | IS (2022-2024) | strat | 1.14 | 0.68 … 1.10 | 9 | sector+size 76.0%, sector+size±1 20.8%, sector only 3.2% |
| nonbeat | IS (2022-2024) | hold | 1.64 | 1.30 … 1.81 | 9 | sector+size 76.0%, sector+size±1 20.8%, sector only 3.2% |
| nonbeat | OOS (2025) | strat | 1.18 | 0.54 … 1.40 | 9 | sector+size 75.4%, sector+size±1 21.7%, sector only 2.9% |
| nonbeat | OOS (2025) | hold | 1.82 | 0.87 … 1.95 | 9 | sector+size 75.4%, sector+size±1 21.7%, sector only 2.9% |
| all | IS (2022-2024) | strat | 1.17 | 0.61 … 0.96 | 9 | sector+size 74.3%, sector+size±1 21.7%, sector only 3.9% |
| all | IS (2022-2024) | hold | 1.72 | 1.25 … 1.68 | 9 | sector+size 74.3%, sector+size±1 21.7%, sector only 3.9% |
| all | OOS (2025) | strat | 1.31 | 0.52 … 1.23 | 9 | sector+size 73.3%, sector+size±1 22.1%, sector only 4.6% |
| all | OOS (2025) | hold | 2.04 | 0.80 … 1.70 | 9 | sector+size 73.3%, sector+size±1 22.1%, sector only 4.6% |

SPY over the same 42-day windows (avg across live-bar trades): IS (2022-2024) 2.32%, OOS (2025) 0.75%, 2026 YTD 0.32%.

## 5. Caveats

- Survivorship bias (current S&P 500 members) applies to **both** arms, so it mostly cancels in the comparison but inflates both absolute levels.
- Size is matched on 20d $-volume, not market cap. Post-earnings names often carry elevated volume, so the signal ticker can land a quintile higher than its usual size; the effect on the comparison is second-order but real.
- The control excludes names with their own committed earnings report near D, so it measures the signal against **non-event** same-sector, same-size stocks.
- Overlapping 42-day windows and same-day clustering are handled by clustering on entry date, not by a full portfolio simulation with capital limits.
- One historical sample, zero costs. A significant result here is evidence of selection skill, not a validated trading edge.