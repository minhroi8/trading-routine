# PEAD Signal-Health × SPY>200MA Combo

*Window 2022-01-01→2026-06-04. Gate applied to enhanced set. n / win% / avg% / PF. Realized-health = trailing-60d mean return of BASE trades already exited (point-in-time).*

## Aggregate

| Gate | Trades | Win% | Avg% | PF |
|------|-------:|-----:|-----:|---:|
| Ungated | 270 | 53.3% | 1.72% | 1.6 |
| Health ≥0 | 191 | 55.5% | 1.83% | 1.66 |
| SPY>200MA | 237 | 56.1% | 2.1% | 1.81 |
| AND (health & 200MA) | 174 | 58.6% | 2.4% | 1.99 |
| OR (health | 200MA) | 254 | 53.9% | 1.69% | 1.6 |

## Per-year (⛔ = hostile regime)

| Gate | 2022⛔ | 2023 | 2024 | 2025 | 2026⛔ |
|------|------|------|------|------|------|
| Ungated | 33t -2.87% | 57t 1.45% | 99t 3.52% | 51t 1.66% | 30t 1.44% |
| Health ≥0 | 19t -4.08% | 23t -1.3% | 97t 3.64% | 42t 2.14% | 10t 1.42% |
| SPY>200MA | 4t -3.32% | 54t 1.2% | 99t 3.52% | 50t 1.1% | 30t 1.44% |
| AND (health & 200MA) | 3t -6.03% | 22t -0.97% | 97t 3.64% | 42t 2.14% | 10t 1.42% |
| OR (health | 200MA) | 20t -3.64% | 55t 1.02% | 99t 3.52% | 50t 1.1% | 30t 1.44% |

*Each cell = trades kept and their avg return. Compare against Ungated row.*

## The two failure modes — did the combo fix them?

| Gate | 2023 kept (lag victim) | 2023 avg% | 2026 blocked (detection) | 2026 avg% |
|------|----------------------:|----------:|-------------------------:|----------:|
| Ungated | 57/57 (100%) | 1.45% | 0% | 1.44% |
| Health ≥0 | 23/57 (40%) | -1.3% | 67% | 1.42% |
| SPY>200MA | 54/57 (95%) | 1.2% | 0% | 1.44% |
| AND (health & 200MA) | 22/57 (39%) | -0.97% | 67% | 1.42% |
| OR (health | 200MA) | 55/57 (96%) | 1.02% | 0% | 1.44% |

## Regime discrimination

| Gate | Blocked hostile (22,26) | Blocked good (23-25) | Discrimination |
|------|------------------------:|---------------------:|---------------:|
| Health ≥0 | 54% | 22% | +32 pts |
| SPY>200MA | 46% | 2% | +44 pts |
| AND (health & 200MA) | 79% | 22% | +57 pts |
| OR (health | 200MA) | 21% | 1% | +19 pts |
