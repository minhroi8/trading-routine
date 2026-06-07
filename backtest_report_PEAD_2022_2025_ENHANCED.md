# Enhanced PEAD — 2022-2025 Full-Sample Filter Validation

*Generated: 2026-06-07 00:24 — window 2022-01-01→2025-12-31, S&P 500 current constituents (survivorship-biased).*

Re-applies the 2026 enhanced filter stack to a large multi-year sample so each filter's value can be judged on thousands of trades instead of the 30 the 2026 YTD window produced.

## Headline

| Set | Trades | Win% | Avg% | PF |
|-----|-------:|-----:|-----:|---:|
| BASE (EPS beat only) | 5836 | 54.6% | 1.39% | 1.48 |
| Scenario A (≥15%) | 1505 | 54.2% | 1.63% | 1.52 |
| Scenario B (≥15%+vol) | 1033 | 54.1% | 1.56% | 1.49 |
| Full enhanced stack | 247 | 55.5% | 1.97% | 1.7 |

**Verdict: filters ADD value on a large sample.** Full stack 55.5%/1.97% vs BASE 54.6%/1.39% over 5,836 base candidates.

## Per-filter impact (independent removal from BASE)

Removed = BASE trades that FAIL the filter. A good filter removes trades with win rate BELOW the BASE win rate (54.6%).

| Filter | Kept | Removed | Win% kept | Win% removed | Avg% removed | Verdict |
|--------|-----:|--------:|----------:|-------------:|-------------:|---------|
| EPS surprise ≥15% | 1505 | 4331 | 54.2% | 54.7% | 1.31% | ~ neutral |
| Volume ≥1.5× | 4085 | 1751 | 54.9% | 54.0% | 1.31% | ~ neutral |
| Rel. strength >0 | 3050 | 2786 | 56.4% | 52.7% | 1.18% | ~ neutral |
| New 52-wk high ≤45d | 2046 | 3790 | 54.3% | 54.7% | 1.59% | ~ neutral |
| Not ≤3d to next earn | 5836 | 0 | 54.6% | —% | —% | removed nothing |

## Year-by-year signal stability (is PEAD decaying?)

| Year | BASE n | BASE win% | BASE avg% | Enh n | Enh win% | Enh avg% |
|------|-------:|----------:|----------:|------:|---------:|---------:|
| 2022 | 1415 | 45.6% | -0.56% | 33 | 30.3% | -2.87% |
| 2023 | 1467 | 52.5% | 1.85% | 59 | 50.8% | 1.64% |
| 2024 | 1486 | 64.3% | 2.56% | 102 | 69.6% | 3.88% |
| 2025 | 1468 | 55.6% | 1.62% | 53 | 49.1% | 1.68% |

*Compare against the 2026 YTD figures: BASE 37.9%/-1.24%, Enhanced 36.7%/+0.16%.*

## IT trailing stop: 7% vs 12% (full sample)

IT enhanced trades: 36.

| Trail | IT avg% | IT win% |
|-------|--------:|--------:|
| 7% | 6.65% | 63.9% |
| 12% | 6.55% | 61.1% |

Wider 12% trail = -0.1% per IT trade vs 7% (worse) on the full sample.

---
*Reuses backtest_pead_2026_ytd.py engine. Survivorship bias + no costs apply.*