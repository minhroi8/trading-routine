---
computed_on: 2026-07-19
expires_on: 2026-07-26
posture: NORMAL
spy_close: 743.29
spy_200ma: 693.44
spy_above_200ma: true
realized_health_60d_pct: 1.225
health_sample_n: 318
health_threshold_pct: 0.0
health_ok: true
window_days: 60
min_sample: 20
source: yfinance
---

# PEAD signal-health overlay

Weekly snapshot of whether the post-earnings-drift edge is currently paying. **Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market` as a **"raise the bar" overlay** on NEW entries — it never halts trading and never affects exits.

## Posture

```
posture = ELEVATED_BAR  if  health_ok == false   (weak realized PEAD drift)
          NORMAL        otherwise
```

When **ELEVATED_BAR**, `pre_market` raises the EPS-surprise threshold to >20% for ALL sectors and caps new positions at 2 for the session — the same treatment `strategy.md` applies in a bear regime. High-conviction setups still trade; the bar is just higher. This is the "don't stop entirely, raise the bar" philosophy.

- **Realized signal health** — trailing-60d mean return of S&P 500 EPS-beat PEAD trades that have already exited (buy +2 days after beat; -8% stop / 7% trail / 42d time stop). Measures the drift edge directly, so it can read weak even in a bull market (the 2026 case) — the gap a SPY>200MA filter alone misses.
- `health_ok` is true when `realized_health_60d_pct >= 0.0` OR fewer than 20 realized trades exist (fail-open on thin data).
- **SPY 200-day regime** is reported here for transparency but is enforced separately by the regime-gate rule in `strategy.md` — this overlay does not duplicate it.

## Current reading

| Field | Value |
|-------|-------|
| Posture | **NORMAL** |
| Realized health (trailing 60d) | 1.225% |
| Health sample size | 318 |
| Health OK (>= 0.0%) | true |
| SPY close | 743.29 |
| SPY 200MA | 693.44 |
| SPY > 200MA (info; enforced via strategy.md) | true |

Validated in `backtest_report_PEAD_HEALTH_200MA_COMBO.md`: combining realized health with the SPY-200MA regime gave the best risk-adjusted result (PF 1.60 → 1.99) and the strongest regime discrimination (+57 pts). Threshold is 0 (untuned). Known limitation: realized health lags at regime TURNS, so the posture can stay ELEVATED_BAR a little into a fresh recovery.
