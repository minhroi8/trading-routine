---
computed_on: 2026-06-05
expires_on: 2026-06-12
gate: RISK_OFF
spy_close: 737.55
spy_200ma: 681.56
spy_above_200ma: true
realized_health_60d_pct: -2.08
health_sample_n: 211
health_threshold_pct: 0.0
health_ok: false
window_days: 60
min_sample: 20
source: yfinance
---

# PEAD signal-health gate

Weekly snapshot of whether the post-earnings-drift edge is currently "on". **Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market` as the **AND gate** on NEW entries. It never blocks exits.

## The gate

```
RISK_ON  iff  (spy_above_200ma == true)  AND  (health_ok == true)
RISK_OFF otherwise
```

- **SPY 200-day regime** — fast bear-turn protection.
- **Realized signal health** — trailing-60d mean return of S&P 500 EPS-beat PEAD trades that have already exited (buy +2 days after beat; -8% stop / 7% trail / 42d time stop). Measures the drift edge directly, so it can read RISK_OFF even in a bull market (the 2026 case).
- `health_ok` is true when `realized_health_60d_pct >= 0.0` OR fewer than 20 realized trades exist (fail-open on thin data — only the SPY leg can flip the gate then).

## Current reading

| Field | Value |
|-------|-------|
| Gate | **RISK_OFF** |
| SPY close | 737.55 |
| SPY 200MA | 681.56 |
| SPY > 200MA | true |
| Realized health (trailing 60d) | -2.08% |
| Health sample size | 211 |
| Health OK (>= 0.0%) | false |

Validated in `backtest_report_PEAD_HEALTH_200MA_COMBO.md`: the AND combo gave the best risk-adjusted result (PF 1.60 → 1.99) and the strongest regime discrimination (+57 pts). Threshold is 0 (untuned). Known limitation: realized health lags at regime TURNS, so the gate can stay RISK_OFF a little into a fresh recovery.
