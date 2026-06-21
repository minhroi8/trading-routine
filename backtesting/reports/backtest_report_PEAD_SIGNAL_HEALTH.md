# PEAD Signal-Health Gate

*Window 2022-01-01→2026-06-04. Health signals measured on the broad EPS-beat (BASE) population, strictly point-in-time (only outcomes known at entry). Gate is applied to the enhanced trade set. n / win% / avg% / PF.*

## Aggregate (all eval years)

| Gate | Trades | Win% | Avg% | PF | vs ungated avg |
|------|-------:|-----:|-----:|---:|---------------:|
| Ungated | 270 | 53.3% | 1.72% | 1.6 | — |
| Realized health ≥0 | 191 | 55.5% | 1.83% | 1.66 | +0.11 pts |
| Drift health ≥0 | 180 | 53.3% | 1.54% | 1.54 | -0.18 pts |
| Both ≥0 | 134 | 57.5% | 1.64% | 1.63 | -0.08 pts |

## Per-year — does it cut hostile years but keep favourable ones?

### Ungated

| Year | Trades | Win% | Avg% | PF | % blocked |
|------|-------:|-----:|-----:|---:|----------:|
| 2022 ⛔hostile | 33 | 30.3% | -2.87% | 0.44 | 0% |
| 2023 | 57 | 50.9% | 1.45% | 1.5 | 0% |
| 2024 | 99 | 69.7% | 3.52% | 3.03 | 0% |
| 2025 | 51 | 47.1% | 1.66% | 1.5 | 0% |
| 2026 ⛔hostile | 30 | 40.0% | 1.44% | 1.44 | 0% |

### Realized health ≥0

| Year | Trades | Win% | Avg% | PF | % blocked |
|------|-------:|-----:|-----:|---:|----------:|
| 2022 ⛔hostile | 19 | 26.3% | -4.08% | 0.33 | 42% |
| 2023 | 23 | 39.1% | -1.3% | 0.61 | 60% |
| 2024 | 97 | 70.1% | 3.64% | 3.13 | 2% |
| 2025 | 42 | 52.4% | 2.14% | 1.72 | 18% |
| 2026 ⛔hostile | 10 | 20.0% | 1.42% | 1.32 | 67% |

### Drift health ≥0

| Year | Trades | Win% | Avg% | PF | % blocked |
|------|-------:|-----:|-----:|---:|----------:|
| 2022 ⛔hostile | 24 | 41.7% | -1.23% | 0.72 | 27% |
| 2023 | 27 | 29.6% | -0.98% | 0.77 | 53% |
| 2024 | 74 | 70.3% | 3.04% | 2.92 | 25% |
| 2025 | 36 | 50.0% | 2.64% | 1.82 | 29% |
| 2026 ⛔hostile | 19 | 42.1% | 0.64% | 1.2 | 37% |

### Both ≥0

| Year | Trades | Win% | Avg% | PF | % blocked |
|------|-------:|-----:|-----:|---:|----------:|
| 2022 ⛔hostile | 12 | 41.7% | -1.82% | 0.64 | 64% |
| 2023 | 15 | 26.7% | -2.98% | 0.32 | 74% |
| 2024 | 73 | 71.2% | 3.17% | 3.09 | 26% |
| 2025 | 29 | 55.2% | 2.86% | 1.94 | 43% |
| 2026 ⛔hostile | 5 | 0.0% | -5.52% | 0.0 | 83% |

## Regime discrimination (the key property)

| Gate | Blocked in hostile yrs (2022,2026) | Blocked in good yrs (2023-25) | Discrimination |
|------|-----------------------------------:|------------------------------:|---------------:|
| Realized health ≥0 | 54% | 22% | +32 pts ✓ targets bad regimes |
| Drift health ≥0 | 32% | 34% | -2 pts ✗ backwards |
| Both ≥0 | 73% | 43% | +30 pts ✓ targets bad regimes |

*A good gate blocks a much larger share of trades in hostile years than in good years (positive discrimination), unlike SPY>200MA which fired bull-and-weak 2026 as 'risk-on'.*

## Live implementation note

The gate needs a rolling read of the broad PEAD signal, which the live agent does not get automatically (it only trades the enhanced set). To run this live, add a weekly **PEAD breadth monitor** (in `universe_refresh` or `pre_market`): sample recent S&P 500 EPS beats and record their 5-trading-day post-earnings drift; gate entries when the trailing-35d mean drift (and/or trailing-60d realized BASE return) drops below 0. This is a research/monitoring change — it does NOT alter `memory/strategy.md` rules, which are human-edit-only.
