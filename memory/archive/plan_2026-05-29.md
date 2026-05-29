# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-29 (Friday — last trading day of May 2026)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| _(none — 8/8 concurrent cap full)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| MSFT | 790e2653 | $379.62 | CONVERT if intraday high ≥ $453.89 | 7% below intraday HWM at time of conversion | +10% trigger vs avg_cost $412.63 = $453.89; not yet crossed as of 10:00 ET ($440.86); monitor intraday |

## Notes

### Capacity constraint
Portfolio is at 8/8 maximum concurrent positions. **No new buys are possible today** unless a position is closed by stop trigger or midday action. Weekly new-position cap: 0/3 consumed this week (May 26–30).

### NVDA stop watch — PRIMARY RISK
- Current price: ~$216.78. Hard stop: $205.43 (order daaecbf6). Cushion: ~$11.35 / 5.2%.
- Smuggling probe update (May 27): Taiwan prosecutors charged 3 individuals for smuggling ~50 Supermicro AI servers with NVDA chips via Japan to China. Jensen Huang responded calling NVDA compliance "rigorous" and directed Supermicro to enhance its compliance framework. This is a third-party distributor allegation — not an SEC investigation of NVDA, not a direct BIS action against NVDA. Thesis intact per strategy.md criteria.
- **Action required if stop daaecbf6 fires intraday**: Confirm fill, then execute PWR contingent buy (see Priority Watchlist below) if all sanity checks pass at that moment.

### MSFT trailing stop — APPROACHING TRIGGER
- Current price: ~$440.86 (+6.84% total). Trigger: $453.89 (+10% vs avg_cost $412.63).
- Gap to trigger: ~$13.03 (3.0%). MSFT is up +3.25% today; Microsoft Build conference next week (new AI model announcements expected). Month-end rebalancing could drive further upside.
- **If MSFT crosses $453.89 intraday**: Cancel stop order 790e2653 ($379.62). Place trailing stop at 7% below intraday high at time of placement (GTC). Record new stop order ID in portfolio.md and trade_log.md.

### Priority watchlist (enter first when concurrent slot opens)
1. **PWR** (Quanta Services) — Q1 2026 blowout (Apr 30): EPS $2.68 vs $1.98 est (+35.4%), revenue $7.87B +26.3% YoY, record backlog $48.5B, FY2026 guidance raised; $1B buyback. Next earnings: Jul 30, 2026 (62 days — safely outside 3-day window ✓). tradable=True, status=active ✓. No halt news ✓. Industrials sector — at entry would bring GEV+PWR to ~8.6% of portfolio (well under 30% ✓). Sizing: ~6 shares at ~$730–740, stop = fill × 0.92 (≤5% of equity ✓).
2. **ANET** (Arista Networks) — Q1 2026 beat (May 5): EPS $0.87 vs $0.79 est (+10.1%), revenue $2.71B, 27.7% revenue growth guidance for 2026 to $11.5B; Gartner Magic Quadrant Leader (May 22). Next earnings: Aug 3, 2026 (66 days — safe ✓). tradable=True, status=active ✓. IT sector — **WARNING**: IT currently at 25.2%; adding ANET at 5% of equity would bring IT to ~30.2% (marginally at cap). Must size ANET to ≤3% of equity (~$3,044) if entering, or verify IT falls below 25% first.

### Do NOT enter before June 3 earnings (3-day window)
- **AVGO** (Broadcom): earnings June 3 after close. AI rev guidance $10.7B +140% YoY — strong thesis, but pre-earnings entry violates 3-day rule. Revisit post-print (June 4+).
- **CRM** (Salesforce): earnings June 3 after close. Q1 FY2027 beat (EPS $3.88 vs $2.96 est +31.1%, $25B buyback, guidance raised May 27) was strong — but stock reacted only +0.42% afterhours. 3-day window opens June 2. Do NOT enter June 1 or after. Revisit post-print (June 4+).
- **CRWD** (CrowdStrike): earnings June 3 after close. Strong momentum +45% past month but DZ Bank Sell ($500 PT) warns overvaluation. Watchlist post-June 3.

### Macro context
- US-Iran tentative Strait of Hormuz deal (VP Vance: "couple language points" remain); oil WTI −1.4% to $87.66, Brent −1.3% to $92.47 — constructive for energy-cost-sensitive growth stocks.
- 10-yr Treasury yield: 4.442% (easing from 4.67% peak on May 20). Month-end today may see yield/rebalancing volatility.
- S&P 500 futures: edging higher pre-market. No data releases today. Macro deferral rule NOT triggered (futures not down >0.4%; yield not at multi-month high of 4.70%).
- DRY_RUN: false.

### Sanity checks (pre_market)
- Cash floor: $62,310.92 / $101,451.86 = 61.4% >> 10% ✓
- Max concurrent: 8/8 (full — no new buys possible) ✓
- IT sector: 25.2% of equity < 30% cap ✓
- All other sectors < 30% cap ✓
- New positions this week: 0/3 ✓ (moot — capacity full)
