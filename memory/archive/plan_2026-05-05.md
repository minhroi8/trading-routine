# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-05

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| GOOGL | 12 | $387.00 | $356.04 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63% YoY; AI ROI now clearly visible; CapEx guidance raised to $180-190B signalling conviction; next earnings ~July 22 2026. Freedom Broker downgraded Buy→Hold May 4 but Citizens raised PT to $515; majority consensus remains bullish. |
| AAPL | 17 | $281.50 | $258.98 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle driven by iPhone 17), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings July 30 2026 confirmed. No rating changes post-earnings; thesis intact. |
| PLTR | 34 | $147.00 | $135.24 | Q1 2026 blowout reported May 4 after close: EPS $0.33 vs $0.28 (+18%), revenue $1.63B +85% YoY (+6% vs est); US Commercial rev +130% YoY; FY2026 guidance raised to 71% growth ($7.65-7.66B) vs $7.27B consensus; muted +2-4% initial reaction despite massive beat creates entry opportunity; next earnings ~Aug 10 2026. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|

_No open positions — no planned sells._

## Simulated fills (DRY_RUN: true — market_open 2026-05-05 ~09:35 ET)

_No real orders placed. Hypothetical fills based on latest trade prices at routine execution time._

| ticker | side | qty | hypothetical_fill | stop_price | status | notes |
|--------|------|-----|-------------------|------------|--------|-------|
| GOOGL | buy | 12 | $387.00 | $356.04 | limit working — not immediately filled | Last trade $388.98 > limit $387.00; order would sit working and potentially fill if price dips |
| AAPL | buy | 17 | $279.44 | $257.08 | simulated fill | Last trade $279.44 < limit $281.50; fills at market; stop = $279.44 × 0.92 |
| PLTR | buy | 34 | $141.91 | $130.56 | simulated fill | Last trade $141.91 < limit $147.00; fills at market; stop = $141.91 × 0.92 |

_Sizing re-check (equity $100,000 at run time):_
- GOOGL 12 × $387.00 = $4,644.00 (4.64%) ✓
- AAPL 17 × $279.44 = $4,750.48 (4.75%) ✓
- PLTR 34 × $141.91 = $4,824.94 (4.82%) ✓
- Total deployed: $14,219.42 (14.22%); cash floor: 85.78% ≥ 10% ✓
- Concurrent positions: 3/8 ✓ | New this week: 3/3 ✓ | Sector caps: Comm. Svcs 4.64%, IT 9.57% — both < 30% ✓

## Notes

**Date**: 2026-05-05 | **DRY_RUN: true** — market_open MUST NOT call /v2/orders; write intended orders to plan.md only.

**Universe cache**: expires 2026-05-10 ✓

**Macro environment**: Iran-UAE missile exchange escalated overnight; WTI crude +4.4% to $106.42, Brent +5.8% to $114.44. S&P 500 -0.41%, Dow -1.13% on May 4. All three planned picks (GOOGL, AAPL, PLTR) are tech/software companies with minimal direct commodity exposure. NFP report due Friday May 8 — key macro catalyst to watch.

**Earnings risk tickers dropped (within 3-day window as of 2026-05-05)**:
- AMD: reports tonight (May 5) after close — dropped
- SBUX: earnings_date_next = 2026-05-05 after close — dropped
- DIS: earnings_date_next = 2026-05-06 — dropped
- MCD: reports May 7 — dropped

**PLTR vs STX decision (3rd slot)**:
- STX remains a strong candidate (Q3 FY2026 beat, AI nearline HDD demand) but is already up 147% YTD at all-time highs — initial post-earnings pop largely captured (reported Apr 28, surged ~5% on results and hit ATH ~$728 on May 1).
- PLTR is a fresher catalyst (reported last night May 4), with a far more muted initial reaction (+2-4%) despite 85% revenue growth and a massive guidance raise — better risk/reward setup. STX noted for human review as strong alternative.

**Halt / trading-status checks (Alpaca /v2/assets)**:
- GOOGL: tradable=True, status=active ✓
- AAPL: tradable=True, status=active ✓
- PLTR: tradable=True, status=active ✓

**Sanity checks**:
- Cash floor: deploy ~$14,428 (GOOGL $4,644 + AAPL $4,785.50 + PLTR $4,998) → 14.4% equity deployed, 85.6% cash. Floor ≥ 10% ✓
- Max concurrent positions: 0 existing + 3 new = 3. Max 8 ✓
- Max new per week: 0 fills in trade_log this week + 3 planned = 3. Cap is 3 ✓
- Sector cap: Communication Services (GOOGL) 4.6%; Information Technology (AAPL + PLTR) 9.8%. No sector near 30% ✓
- All tickers confirmed in universe.md (502-ticker cache, expires 2026-05-10) ✓
