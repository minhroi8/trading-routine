# Backtest: Chronic-Never-Worked Early-Exit Rule vs Current -8%-Only Baseline

*Generated: 2026-07-08 16:55 -- window 2022-01-01->2026-07-04, S&P 500 current constituents (survivorship-biased).*

Follow-up to `memory/stop_audit_2026-07-07.md` (hypothesis H4). That audit found chronic never-worked positions were the modal hard-stop-loss bucket in the live 13-trade sample (4/8, 50%), but 2 of those 4 (PWR, CASY) later recovered fully after the eventual hard stop fired -- so an early chronic-exit rule is not a free lunch. This backtest tests the rule at scale, with the same in-sample/out-of-sample discipline used for the S3 ATR-stop test (the split that correctly caught S3 failing OOS despite looking strong in-sample).

**Rule tested:** exit at close if, by trading day D since entry, MFE (peak High since entry vs. entry price) has not reached +3% AND the position has closed underwater for K consecutive sessions. Layered on top of the current rules (flat -8% hard stop always takes priority; 1/3 scale-out + 7% trail at +10%; 42-calendar-day time stop) -- it never overrides an already-fired hard stop, it only potentially exits *earlier*.

**Grid tested (no cherry-picking):** D in [5, 7, 10], K in [3, 4, 5] -- 9 combinations, all reported below.

**Position sizing is unchanged** (fixed $11,000 / 11% of $100k equity) -- this rule only changes exit *timing*, not position size, so dollar P&L differences reflect the exit-timing effect in isolation.

## 1. Baseline (V0, current -8%-only rules)

Full sample: **277 trades**, win rate 55.2%, avg return 1.48%, median 1.65%, PF 1.5, total P&L $45,039.

| Period | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | Total P&L |
|--------|-------:|-----:|-----:|-----:|--------:|---------:|---:|----------:|
| 2022-2024 | 194 | 57.7% | 1.81% | 1.98% | 7.76% | -6.31% | 1.68 | $38,624 |
| 2025 | 53 | 49.1% | 1.23% | -0.2% | 9.03% | -6.29% | 1.38 | $7,159 |
| 2026 YTD | 30 | 50.0% | -0.23% | -0.61% | 7.79% | -8.24% | 0.95 | $-744 |

## 2. Grid results -- all 9 (D, K) combinations vs baseline

Win rate / avg return / profit factor for the chronic-exit variant, full sample and split in-sample (2022-2024) vs out-of-sample (2025+2026 YTD), same split methodology as the S3 ATR-stop backtest.

| D | K | # triggered (full) | Full Win% | Full Avg% | Full PF | IS (22-24) Avg% | IS PF | OOS (25+26) Avg% | OOS PF | OOS verdict |
|--:|--:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 5 | 3 | 103 | 40.4% | 1.05% | 1.41 | 1.31% | 1.58 | 0.43% | 1.14 | DOES NOT IMPROVE |
| 5 | 4 | 100 | 41.2% | 1.02% | 1.39 | 1.28% | 1.55 | 0.4% | 1.13 | DOES NOT IMPROVE |
| 5 | 5 | 97 | 41.9% | 1.1% | 1.42 | 1.38% | 1.59 | 0.44% | 1.14 | DOES NOT IMPROVE |
| 7 | 3 | 94 | 42.2% | 0.86% | 1.31 | 1.12% | 1.44 | 0.26% | 1.08 | DOES NOT IMPROVE |
| 7 | 4 | 91 | 43.3% | 0.97% | 1.35 | 1.25% | 1.49 | 0.31% | 1.09 | DOES NOT IMPROVE |
| 7 | 5 | 89 | 43.7% | 1.0% | 1.36 | 1.27% | 1.49 | 0.38% | 1.12 | DOES NOT IMPROVE |
| 10 | 3 | 70 | 46.6% | 1.12% | 1.4 | 1.46% | 1.57 | 0.31% | 1.09 | DOES NOT IMPROVE |
| 10 | 4 | 69 | 46.9% | 1.18% | 1.42 | 1.54% | 1.61 | 0.33% | 1.1 | DOES NOT IMPROVE |
| 10 | 5 | 69 | 46.9% | 1.17% | 1.42 | 1.52% | 1.6 | 0.34% | 1.1 | DOES NOT IMPROVE |

_Baseline for comparison -- Full: win 55.2% avg 1.48% PF 1.5. IS (22-24): avg 1.81% PF 1.68. OOS (25+26): avg 0.7% PF 1.2._

## 3. Avoided losses vs. foreclosed recoveries -- all 9 combinations

For every trade where the chronic rule actually fires (`chronic_exit`), this splits the outcome by what the CURRENT (-8%-only) rules would have done with that same trade if left alone:

- **Avoided** = baseline eventually hit the hard stop anyway -- chronic exit got out earlier/smaller.
- **Foreclosed** = baseline eventually closed profitably (trail stop, time stop, or data-end) -- chronic exit would have cut a trade that later recovered, the PWR/CASY pattern.
- **Neutral** = baseline was also a loss, but not via the hard stop (time-stop/data-end loss) -- neither a clean avoided-loss nor a foreclosed-recovery case.

| D | K | # Triggered | Avoided (V0 hard-stop) | Avoided: V0 avg% -> Chronic avg% | Foreclosed (V0 profitable) | Foreclosed: V0 avg% forgone -> Chronic avg% taken | Neutral |
|--:|--:|---:|---:|---|---:|---|---:|
| 5 | 3 | 103 | 36 | -9.0% -> -3.63% | 41 | 5.65% -> -2.15% | 26 |
| 5 | 4 | 100 | 35 | -8.99% -> -4.05% | 39 | 5.65% -> -2.21% | 26 |
| 5 | 5 | 97 | 34 | -9.0% -> -4.05% | 37 | 5.31% -> -2.15% | 26 |
| 7 | 3 | 94 | 32 | -8.95% -> -4.4% | 36 | 5.89% -> -2.46% | 26 |
| 7 | 4 | 91 | 32 | -8.95% -> -4.38% | 33 | 5.78% -> -2.54% | 26 |
| 7 | 5 | 89 | 31 | -8.96% -> -4.57% | 32 | 5.54% -> -2.45% | 26 |
| 10 | 3 | 70 | 21 | -8.83% -> -4.32% | 24 | 5.52% -> -2.0% | 25 |
| 10 | 4 | 69 | 21 | -8.83% -> -4.11% | 23 | 5.32% -> -2.09% | 25 |
| 10 | 5 | 69 | 21 | -8.83% -> -4.39% | 23 | 5.32% -> -1.98% | 25 |

## 4. Net effect on hard-stop-loss trades specifically

Restricting to the subset of trades whose CURRENT (-8%-only) outcome is a hard-stop loss (the exact population the stop audit examined), how much of that loss bucket does each (D, K) combination intercept, and at what average loss reduction?

Hard-stop-loss trades in the full backtest sample: **75** (of 277 total, 27.1%), avg return -9.23%.

| D | K | Intercepted (of hard-stop pop.) | Intercept rate | Avg loss under V0 | Avg loss under chronic exit | Avg loss reduction |
|--:|--:|---:|---:|---:|---:|---:|
| 5 | 3 | 36 | 48.0% | -9.0% | -3.63% | +5.37% |
| 5 | 4 | 35 | 46.7% | -8.99% | -4.05% | +4.94% |
| 5 | 5 | 34 | 45.3% | -9.0% | -4.05% | +4.95% |
| 7 | 3 | 32 | 42.7% | -8.95% | -4.4% | +4.55% |
| 7 | 4 | 32 | 42.7% | -8.95% | -4.38% | +4.57% |
| 7 | 5 | 31 | 41.3% | -8.96% | -4.57% | +4.39% |
| 10 | 3 | 21 | 28.0% | -8.83% | -4.32% | +4.51% |
| 10 | 4 | 21 | 28.0% | -8.83% | -4.11% | +4.72% |
| 10 | 5 | 21 | 28.0% | -8.83% | -4.39% | +4.44% |

## 5. Recommendation

Of the 9 combinations, the ones passing the OOS bar (avg return AND PF at or above baseline on 2025+2026) are: none.

This is a research read, not a recommendation to change `memory/strategy.md`. Per the stop-audit's own H4 framing: even a combination that improves full-sample and OOS averages does so by foreclosing some real recoveries (see §3) -- the right lens is whether the avoided-loss dollars exceed the foreclosed-recovery dollars at that specific (D, K), not win rate alone. See Limitations for sample-size and survivorship caveats before treating any single combination as validated.

## 6. Beat-the-benchmark bar (SPY buy-and-hold, same period, for context)

| Period | SPY buy-and-hold | V0 avg/trade |
|--------|------------------:|--------------:|
| 2022-2024 | 28.2% | 1.81% |
| 2025 | 18.0% | 1.23% |
| 2026 YTD | 11.1% | -0.23% |

_SPY figures are per-period index buy-and-hold return, taken from the other PEAD backtest reports in this repo; not directly comparable to a single-trade avg% (per-trade return on ~11% position size, not a fully-invested compounded return), shown for context only.

## 7. Limitations

- **No regime gate applied to the candidate set.** This matches the S3 ATR-stop script's own V0/V2 baseline (not the separate bull-regime-gate variant reported elsewhere in this repo), chosen for entry-set consistency with the most recent comparable backtest and for statistical power (277 candidate entries vs. the much smaller 207-trade regime-gated sample). The live book currently trades under the regime gate, so this backtest's candidate population is broader than what the live strategy would actually enter today; treat the grid results as evidence about the *exit rule* in isolation, not as a like-for-like replay of the exact live entry population.
- **Survivorship bias.** Tickers are drawn from current S&P 500/400/600 constituents and current sector classifications, same caveat as every other backtest report in this repo.
- **MFE uses daily High, not intraday path.** Same simplification as the live stop audit's multi-day trades; entry/exit-day intraday sequencing is approximated by daily OHLC.
- **Chronic-exit and hard-stop are both evaluated at the daily close**, i.e. this assumes an end-of-day rule review can execute at that day's close price -- in live trading, an analogous rule would likely execute at the next session's open (via `midday` or `market_close`), which would introduce a small amount of slippage not modeled here.
- **2026 YTD sample is small** (30 candidate entries per the enhanced-filter stack) -- the OOS split's 2026 component individually carries limited weight; the OOS verdict column above is driven mostly by 2025.
- **This backtest answers a different question than the live 13-trade audit.** The audit's PWR/CASY recoveries are two specific real trades; this backtest's "foreclosed recovery" counts are the same *pattern* replayed across the full historical candidate set, not a guarantee those exact two trades appear in this sample under these tickers/dates.
- No orders were placed and `memory/strategy.md` was not modified to produce this report.
