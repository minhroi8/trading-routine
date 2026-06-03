# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-03

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Why no new buys today:**
1. **MRVL** (strongest new catalyst — Jensen Huang "next trillion-dollar company" at Computex June 2, +46% surge): NOT IN UNIVERSE. Per CLAUDE.md, cannot plan a trade. Noted for human review.
2. **META** (Communication Services, no current sector exposure): Shortlisted but dropped. EU court ruling June 3 is mixed (Messenger gatekeeper upheld, stock −0.47%). Q1 non-GAAP EPS beat +7.66% (below 15% threshold); stock declining from $613 (May 19) to $602; capex overhang persists. Not the risk/reward setup we want.
3. **AVGO, CRM, CRWD**: All report earnings tonight June 3 after close — 3-day pre-earnings block applies. First eligible entry June 6.
4. **IT sector cap**: Current IT positions (AAPL + CSCO + MSFT + NVDA) = $20,391 = 20.4% of equity. Only $9.6K room before 30% cap — cannot open a full 11% IT position even if a qualifying ticker existed.
5. **Capacity**: 1 weekly slot and 1 concurrent slot remain. Preserving weekly slot for AVGO/CRM/CRWD post-earnings reassessment on June 4 pre_market (eligible entry June 6).

**Stop proximity watch — market_open must monitor:**
- **MSFT trailing stop d1228e16**: current $439.54, stop $433.68 (HWM $466.32) — only **1.33% cushion**. Microsoft Build Day 2 sell-the-news risk. Trailing stop is Alpaca-managed; DO NOT manually intervene unless thesis breaks.
- **AMZN stop f87a7a95**: current $256.03, stop $248.14 — **3.08% cushion**. Prime Day June 23–26 catalyst intact; do not cut on intraday weakness alone.

**NVDA ex-dividend June 4**: $0.25/share × 22 shares = **$5.50 cash credit** (Alpaca-managed, no action needed).

**Upcoming catalysts to plan around:**
- AAPL WWDC June 8–12 (AI platform reveal — key catalyst for trailing stop management)
- AVGO earnings tonight June 3 → reassess June 4 pre_market for June 6 entry (1 weekly slot available)
- GEV ex-div June 16 ($0.50/share × 4 = $2.00 credit)

**Portfolio sanity check (pre-market):**
- Equity: $99,999.76 | Cash: $60,542.15 (60.5%) > 10% floor ✓
- Concurrent positions: 7/8 ✓
- New positions this week: 2/3 (HPE June 2 — stopped out same day; PWR June 2) ✓
- Sector caps: IT 20.4% ✓ | Industrials 14.5% ✓ | Consumer Disc 4.6% ✓ | all < 30% ✓
- DRY_RUN: false
