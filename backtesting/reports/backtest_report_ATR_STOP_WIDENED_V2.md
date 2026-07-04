# Backtest: Wider ATR-Scaled Stop (V2, S3 proposal) vs Flat -8% Stop (V0)

*Generated: 2026-07-04 14:18 -- window 2022-01-01->2026-07-04, S&P 500 current constituents (survivorship-biased).*

This tests the actual S3 recommendation from `backtesting/strategy_review_log.md` (2026-06-30 run): widen the stop for high-ATR names instead of using a tighter-only ATR floor. Unlike the already-rejected V1 variant in `backtest_report_ATR_STOP_VS_FLAT.md` (`min(8%, max(4%, 2xATR))`, a CEILING at 8% that can only ever be equal-or-tighter than flat), this variant (V2) removes the ceiling.

- **V0 (baseline):** flat -8% stop; position = 11% of equity ($11k on $100k).
- **V2 (wider ATR stop):** stop = `max(8%, 2x14-day ATR%)` -- a FLOOR at 8%, uncapped above it; position sized to risk 0.8% of equity (`$800 / stop_pct`), hard-capped at 11% of equity. Per the proposed wording, dollar risk per trade is held roughly constant by shrinking notional as the stop widens.

Both variants scale out 1/3 at +10% and trail the remaining 2/3 by 7% below the peak; 42-calendar-day time stop. Entry set, filters and trailing/time-stop logic are identical to every other PEAD backtest in this repo.

## 1. Verdict

Across the full sample (277 trades), **V0 avg/trade = 1.48%** (PF 1.5) vs **V2 avg/trade = 1.52%** (PF 1.49).

## 2. Comparison Table -- V0 vs V2 by period (in-sample vs out-of-sample)

| Period | Var | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | MaxConsecL | AvgHold | Total P&L |
|--------|-----|-------:|-----:|-----:|-----:|--------:|---------:|---:|-----------:|--------:|----------:|
| 2022-2024 | V0 | 194 | 57.7% | 1.81% | 1.98% | 7.76% | -6.31% | 1.68 | 9 | 35.5d | $38,624 |
| 2022-2024 | V2 | 194 | 58.2% | 1.9% | 1.99% | 7.89% | -6.46% | 1.72 | 9 | 35.9d | $36,047 |
| 2025 | V0 | 53 | 49.1% | 1.23% | -0.2% | 9.03% | -6.29% | 1.38 | 5 | 34.0d | $7,159 |
| 2025 | V2 | 53 | 49.1% | 1.31% | -0.2% | 9.03% | -6.12% | 1.36 | 5 | 34.8d | $5,502 |
| 2026 YTD | V0 | 30 | 50.0% | -0.23% | -0.61% | 7.79% | -8.24% | 0.95 | 5 | 28.8d | $-744 |
| 2026 YTD | V2 | 30 | 50.0% | -0.55% | -0.61% | 7.79% | -8.88% | 0.73 | 5 | 29.0d | $-3,243 |

## 3. Out-of-sample discipline (2022-2024 in-sample vs 2025+2026 out-of-sample)

| Segment | Var | Trades | Avg% | PF |
|---------|-----|-------:|-----:|---:|
| In-sample (2022-2024) | V0 | 194 | 1.81% | 1.68 |
| In-sample (2022-2024) | V2 | 194 | 1.9% | 1.72 |
| Out-of-sample (2025-2026) | V0 | 83 | 0.7% | 1.2 |
| Out-of-sample (2025-2026) | V2 | 83 | 0.64% | 1.08 |

**OOS verdict: V2 DOES NOT IMPROVE vs V0 out-of-sample** (0.64% vs 0.7% avg; PF 1.08 vs 1.2).

## 4. Noise-stop analysis (stops inside first 5 trading days)

| Period | Var | #Stops | #Stops in first 5d | Noise-stop rate | First-5d stops as % of all trades |
|--------|-----|-------:|-------------------:|----------------:|----------------------------------:|
| 2022-2024 | V0 | 47 | 8 | 17.0% | 4.1% |
| 2022-2024 | V2 | 45 | 6 | 13.3% | 3.1% |
| 2025 | V0 | 16 | 4 | 25.0% | 7.5% |
| 2025 | V2 | 15 | 3 | 20.0% | 5.7% |
| 2026 YTD | V0 | 12 | 2 | 16.7% | 6.7% |
| 2026 YTD | V2 | 12 | 1 | 8.3% | 3.3% |

## 5. MU-style analysis -- high-ATR semiconductor / IT names

Filter: IT-sector names with daily ATR > 3.0% of price. Matched **29** trades.

- Mean ATR of these names: 4.76%/day -> mean V2 stop 9.81% (vs flat 8%).
- V0 first-5-day noise stops: **3**. V2 first-5-day noise stops: **1**.
- V0 noise stops *avoided* under V2: **2**. *New* noise stops V2 introduced: **0**.
- V0 avg return on these names: 6.1%; V2 avg: 5.49%.
- Position downsizing: **100%** of these high-ATR trades had V2 notional BELOW the $11k cap (mean $8,523, range $4,439–$10,000) — the 11%-of-equity cap never bound for a single one of these 29 trades; sizing genuinely shrank in every case to hold dollar risk near $800, exactly as the proposed wording specifies.

## 6. Beat-the-benchmark bar (SPY buy-and-hold, same period)

| Period | SPY buy-and-hold | V0 avg/trade | V2 avg/trade |
|--------|------------------:|--------------:|--------------:|
| 2022-2024 | 28.2% | 1.81% | 1.9% |
| 2025 | 18.0% | 1.23% | 1.31% |
| 2026 YTD | 11.1% | -0.23% | -0.55% |

_SPY figures are per-period index buy-and-hold return, taken from the other PEAD backtest reports in this repo (`backtest_report_PEAD_2022_2024.md`, `backtest_report_PEAD_2025_OOS.md`, `backtest_report_PEAD_2026_YTD.md`); they are not directly comparable to a single-trade avg% (these are per-trade returns on ~11% position size, not a fully-invested compounded return), but are shown for context per the routine's beat-the-benchmark bar.

## 7. Recommendation

V2 beat V0 on average return in **2 of 3** periods (OOS 2025+2026: DOES NOT IMPROVE).
