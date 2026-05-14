# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-14

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| CSCO | 42 | $117.50 | $108.10 | Q3 FY2026 blowout (reported May 13 after close): EPS $1.06 vs $1.04 est, revenue $15.8B +12% YoY, networking +25%, product orders +35% YoY, hyperscaler orders triple digits YoY; Q4 guide $16.7–16.9B (raised); AI infrastructure demand structural. Pre-market +15% to $117.24. Next earnings Aug 12, 2026. |
| AMZN | 18 | $272.00 | $250.24 | Q1 2026 blowout (Apr 29): EPS $2.78 vs $1.64 est (+70%), AWS $37.6B +28% YoY (fastest growth in 15 qtrs), custom AI chips >$20B annualized run rate; Q2 guide $194–199B (+16–19% YoY); 41 analysts Strong Buy, avg PT $306; Trump-Xi summit tailwind (potential AWS China unlock). Next earnings Jul 30, 2026. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Notes

### Sanity checks — all passed
- Cash floor: $85,801.10 cash → after both fills ~$75,970 (75.5% of equity) >> 10% floor ✓
- Max concurrent positions: 3 current + 2 new = 5 ≤ 8 ✓
- Max new positions this week (May 12–16): 0 prior + 2 planned = 2 ≤ 3 ✓
- Sector caps (of $100,546.70 equity): IT (AAPL + AMD + CSCO) ≈ 14.8%; Consumer Discretionary (AMZN) ≈ 4.9%; Communication Services (GOOGL) ≈ 4.8% — all well within 30% ✓
- Both CSCO and AMZN confirmed in universe.md (large cap, avg vol >> $20M). Alpaca status: tradable=true, active ✓. No halt or SEC investigation news ✓.

### Candidates dropped
- **NVDA**: Next earnings May 20, 2026 (6 days away). Entry today would require exit by May 17 to stay outside the 3-day window — a 3-day hold is not a swing trade. Dropped; revisit post-earnings.
- **QCOM**: Stock plunged −11% May 12 after record high $247 (technical breakdown). DZ Bank downgraded to Hold; analyst consensus 9 Buy / 18 Hold / 4 Sell. Risks: losing Apple processor share, Windows PC competition from Nvidia. Dropped.

### Existing positions — no exit criteria triggered
- **GOOGL** 12 @ $395.72 avg_cost → May 13 close $402.63 (+1.74% vs cost); stop $364.07 active. Thesis intact (Mizuho PT $460; EU antitrust pre-existing, no escalation).
- **AAPL** 17 @ $283.10 avg_cost → May 13 close $298.95 (+5.60% vs cost); stop $260.45 active. Thesis intact (new CEO Ternus, AI pipeline, $100B buyback active).
- **AMD** 11 @ $421.59 avg_cost → May 13 close $445.40 (+5.63% vs cost); stop $387.86 active. Thesis intact (Data Center +57% Q1); gaming -20% H2 headwind noted but gaming is not the thesis driver. Trailing stop trigger at $463.75 (+10%) — not yet reached.

### Macro context
- Trump-Xi Beijing summit live today; Jensen Huang (NVDA) joined trip; reports of US clearing Nvidia H200 sales to China — broad semiconductor/AI tailwind
- Dow futures +0.7% (set to retake 50,000), S&P 500 futures +0.3%, Nasdaq +0.2%
- DRY_RUN: false
