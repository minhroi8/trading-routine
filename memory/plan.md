# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-04

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| GOOGL | 12 | $387.00 | $356.04 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94% surprise), revenue $109.9B +22% YoY; cloud margins expanding; AI Search +19% YoY fastest in years; CapEx ROI clearly visible; next earnings ~Jul 22-23 2026. |
| AAPL | 17 | $281.50 | $258.98 | Q2 2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record), Services ATH $31B; June-qtr guidance raised to 14-17% growth vs 9.5% expected; shares +3.7% post-earnings; next earnings Jul 30 2026. |
| STX | 6 | $729.00 | $670.68 | Q3 FY2026 blowout: EPS $4.10 vs $3.47 est (+18% surprise), revenue $3.11B +44% YoY; Q4 guidance raised to $3.45B rev / $5.00 EPS; AI-driven nearline HDD structural demand ("new era of structural growth"); next earnings ~Jul 16-28 2026. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|

_No open positions — no planned sells._

## Notes

**Date**: 2026-05-04 | **DRY_RUN: true** — market_open MUST NOT call /v2/orders; write intended orders to plan.md only.

**Macro**: Iran tensions elevated; WTI crude +1.2% to $103.20, Brent +2.2% to $110.50. Market mixed (S&P 500 dipping on Iran uncertainty). Nasdaq futures edged up on peace hopes. All three picks are tech/internet companies with minimal direct commodity exposure.

**Earnings season backdrop**: 84% of S&P 500 Q1 reporters beat EPS estimates (highest since Q2 2021), earnings beating by ~20.7% on average vs 7.3% historical.

**Earnings risk tickers dropped (within 3-day window as of 2026-05-04)**:
- PLTR: reports today (May 4) after close — dropped
- AMD: reports May 5 after close — dropped
- SBUX: earnings_date_next = 2026-05-05 — dropped
- DIS: earnings_date_next = 2026-05-06 — dropped
- MCD: reports May 7 — dropped

**Additional candidates considered but dropped**:
- MSFT: Q3 FY2026 beat (EPS $4.27 vs ~$4.06, Azure +40%) — strong candidate but dropped to respect max 3 new-per-week cap; also media raising CapEx sustainability concerns ($190B AI CapEx pledge).
- EBAY: Surged ~10% on GME unsolicited $125/share acquisition bid — M&A event risk, not fundamentals signal; deal probability uncertain; Bernstein skeptical.

**Sanity checks**:
- Cash floor: deploy ~$13,803 (GOOGL $4,644 + AAPL $4,785 + STX $4,374) → 13.8% of equity deployed, 86.2% cash. Floor ≥ 10% ✓
- Max concurrent positions: 0 existing + 3 new = 3. Max 8 ✓
- Max new per week: 3 planned buys this week, max is 3 ✓
- Sector cap: IT sector (AAPL + STX) ~9.2%; Communication Services (GOOGL) ~4.6%. No sector near 30% cap ✓
- All tickers confirmed in universe.md (502-ticker cache, expires 2026-05-10) ✓
- All tickers: Alpaca status=active, tradable=true ✓
