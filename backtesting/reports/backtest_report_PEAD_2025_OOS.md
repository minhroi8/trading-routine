# PEAD Out-of-Sample Backtest Report — 2025

*Generated: 2026-05-28 18:29*

---

## 1. Out-of-Sample Verdict

**YES — Strategy held up in 2025.**

The strategy produced a profit factor of 1.55, win rate of 55.5%, and average return of 1.54% on completely out-of-sample data. Performance was broadly consistent with the 2022-2024 in-sample baseline, confirming the PEAD edge is real and not an artefact of curve-fitting.

## 2. 2025 vs 2022-2024 Comparison

| Metric | 2022-2024 (in-sample) | 2025 (out-of-sample) | Direction |
|--------|-----------------------|----------------------|-----------|
| Total trades | 4387 | 1454 | — |
| Win rate | 54.8% | 55.5% | ↑ better |
| Avg return / trade | 1.32% | 1.54% | ↑ better |
| Avg winner | +7.74% | +7.84% | ↑ better |
| Avg loser | -6.45% | -6.31% | ↓ better |
| Profit factor | 1.45 | 1.55 | ↑ better |
| Max consec. losses | 41 | 13 | ↓ better |
| Avg holding days | 35.6 | 35.8 | — |
| SPY buy-and-hold | 28.2% | 18.0% | — |

## 3. Full Trade Statistics

| Metric | Value |
|--------|-------|
| Total trades | 1454 |
| Win rate | 55.5% |
| Avg return per trade | 1.54% |
| Median return per trade | 1.36% |
| Avg winner | +7.84% |
| Avg loser | -6.31% |
| Profit factor | 1.55 |
| Max consecutive losses | 13 |
| Avg holding period | 35.8 days |
| Total P&L (all positions) | $246,323 |
| Best trade | SNDK +113.08% (38d) |
| Worst trade | TER -23.4% (39d) |
| SPY buy-and-hold 2025 | 18.0% |
| Approx. Sharpe ratio | 4.64 |

**Exit reason breakdown:**

- time: 1022 (70.3%)
- hard_stop: 326 (22.4%)
- trail_stop: 106 (7.3%)

## 4. Regime Analysis (SPY vs 200-Day MA)

**Bull regime (SPY > 200MA)** — 1148 trades
- Win rate: 50.0%
- Avg return: 0.33%
- Profit factor: 1.1

**Bear regime (SPY < 200MA)** — 306 trades
- Win rate: 76.1%
- Avg return: 6.07%
- Profit factor: 5.81

## 5. EPS Surprise Analysis

| Surprise Group | Trades | Win Rate | Avg Return | Profit Factor |
|----------------|--------|----------|------------|---------------|
| Small (0–5%) | 546 | 53.8% | 1.14% | 1.43 |
| Medium (5–15%) | 515 | 56.9% | 1.62% | 1.58 |
| Large (>15%) | 393 | 56.0% | 1.99% | 1.66 |

## 6. Holding Period Analysis

| Holding Group | Trades | Win Rate | Avg Return |
|---------------|--------|----------|------------|
| ≤ 14 days (≤2 weeks) | 151 | 6.6% | -8.4% |
| 15–28 days (2–4 weeks) | 145 | 24.1% | -5.38% |
| 29–42 days (time stop) | 1158 | 65.8% | 3.7% |

## 7. Sector Breakdown

| Sector | Trades | Win Rate | Avg Return | Total P&L |
|--------|--------|----------|------------|-----------|
| Financials | 231.0 | 67.1% | 3.14% | $79,702 |
| Information Technology | 231.0 | 50.2% | 2.08% | $52,763 |
| Industrials | 251.0 | 55.0% | 1.32% | $36,411 |
| Health Care | 181.0 | 58.0% | 1.35% | $26,967 |
| Communication Services | 69.0 | 65.2% | 3.14% | $23,850 |
| Consumer Staples | 98.0 | 54.1% | 1.3% | $14,056 |
| Energy | 55.0 | 63.6% | 2.06% | $12,451 |
| Consumer Discretionary | 131.0 | 53.4% | 0.66% | $9,557 |
| Materials | 57.0 | 57.9% | 1.23% | $7,728 |
| Real Estate | 74.0 | 48.6% | -0.25% | $-2,057 |
| Utilities | 76.0 | 27.6% | -1.81% | $-15,105 |

## 8. Best 10 Trades

| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |
|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|
| SNDK | Information Technology | 2025-08-18 | $44.25 | 2025-09-25 | $94.29 | +113.08% | 38 | trail_stop |
| MU | Information Technology | 2025-12-19 | $251.5427 | 2026-01-30 | $414.7058 | +64.86% | 42 | time |
| WBD | Communication Services | 2025-08-11 | $10.94 | 2025-09-17 | $17.99 | +64.44% | 37 | trail_stop |
| HOOD | Financials | 2025-05-02 | $46.775 | 2025-06-13 | $72.6 | +55.21% | 42 | time |
| CIEN | Information Technology | 2025-09-08 | $118.45 | 2025-10-20 | $173.12 | +46.15% | 42 | time |
| STX | Information Technology | 2025-05-01 | $90.8293 | 2025-06-12 | $124.4658 | +37.03% | 42 | time |
| VRT | Industrials | 2025-04-25 | $84.8651 | 2025-06-06 | $115.2176 | +35.77% | 42 | time |
| GEV | Industrials | 2025-04-25 | $359.022 | 2025-06-06 | $483.9378 | +34.79% | 42 | time |
| STX | Information Technology | 2025-07-31 | $147.1904 | 2025-09-11 | $195.3375 | +32.71% | 42 | time |
| INTC | Information Technology | 2025-02-03 | $18.97 | 2025-02-21 | $24.87 | +31.1% | 18 | trail_stop |

## 9. Worst 10 Trades

| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |
|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|
| TER | Information Technology | 2025-01-31 | $113.2065 | 2025-03-11 | $86.7157 | -23.4% | 39 | hard_stop |
| NKE | Consumer Discretionary | 2025-03-24 | $66.8815 | 2025-04-03 | $54.2193 | -18.93% | 10 | hard_stop |
| FANG | Energy | 2025-02-26 | $145.9583 | 2025-04-04 | $119.4359 | -18.17% | 37 | hard_stop |
| COIN | Financials | 2025-02-18 | $278.8 | 2025-02-21 | $235.38 | -15.57% | 3 | hard_stop |
| OKE | Energy | 2025-02-26 | $89.1154 | 2025-04-04 | $75.684 | -15.07% | 37 | hard_stop |
| BAX | Health Care | 2025-02-24 | $33.3991 | 2025-04-04 | $28.4021 | -14.96% | 39 | hard_stop |
| APH | Information Technology | 2025-01-24 | $78.242 | 2025-01-27 | $66.8424 | -14.57% | 3 | hard_stop |
| HOOD | Financials | 2025-11-07 | $123.766 | 2025-11-20 | $106.21 | -14.18% | 13 | hard_stop |
| WSM | Consumer Discretionary | 2025-03-21 | $158.053 | 2025-04-03 | $136.1998 | -13.83% | 13 | hard_stop |
| COHR | Information Technology | 2025-02-07 | $101.07 | 2025-02-11 | $87.5 | -13.43% | 4 | hard_stop |

## 10. Key Findings

- **vs 2022–2024 baseline:** Avg return shifted from +1.32% to 1.54%; win rate from 54.8% to 55.5%; profit factor from 1.45 to 1.55.
- **Exit mix:** 22.4% hard stop, 7.3% trailing stop, 70.3% time stop — similar exit profile to in-sample.
- **Reward/risk:** 7.84% avg winner vs 6.31% avg loser = 1.24:1.
- **SPY 2025:** 18.0% buy-and-hold. Strategy alpha positive.
- **Regime dependency:** Bull-regime trades averaged 0.33% vs bear-regime 6.07%. Bear regime trades outperformed — strategy may be counter-trend.
- **Surprise magnitude:** Large beats (>15% surprise) averaged 1.99% vs small beats (0-5%) at 1.14%. Filter for large beats could improve selectivity.
- **Survivorship bias** remains present (current S&P 500 constituents only).

## 11. Recommendation

*Based on combined in-sample (2022-2024) + out-of-sample (2025) evidence:*

**CONTINUE — Deploy the live bot.** Both in-sample and out-of-sample tests confirm a real edge.

The strategy passes the critical out-of-sample test with metrics that closely track the in-sample baseline. Recommend going live on the paper account with `DRY_RUN: false`, monitoring weekly. Priority enhancements: (1) add a guidance-raise filter using a premium data source to improve trade quality; (2) consider filtering for large EPS surprises (>15%) if the surprise-magnitude analysis shows meaningful separation.

---

*Backtest engine: yfinance + custom Python. Identical rules to 2022-2024 in-sample run. Not financial advice.*