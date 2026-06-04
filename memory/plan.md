# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

_(pre_market will fill this in)_

## Planned buys

_(none — pre_market will fill this in)_

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| CSCO | 54eb2e8d | $108.10 | **⚠️ CARRY-FORWARD FROM JUNE 4**: Convert to 7% trailing stop GTC immediately at open | Cancel 54eb2e8d; place trailing_stop 42@7% trail_percent GTC | CSCO closed $129.45 on June 4, crossing the $129.16 trail trigger (+10% vs avg_cost $117.42). The conversion was not executed during the trading session (no routine ran between midday 12:10 ET and close). market_open June 5 MUST cancel stop 54eb2e8d and place trailing stop 42@7% trail_percent GTC immediately at open. |

## Notes

_(pre_market will fill this in)_

> **Carry-forward critical action (set by market_close 2026-06-04):**
> CSCO hard stop 54eb2e8d ($108.10) MUST be converted to a 7% trailing stop at market_open June 5. CSCO closed $129.45 on June 4 (above trigger $129.16). Position is at +10.25% unrealized (+$505.36). HWM = $129.45 (use close as initial HWM). New trailing stop = $129.45 × 0.93 = ~$120.39.
