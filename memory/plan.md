# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-05

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| SNDK | 6 | $1,790 | fill × 0.92 (set at market_open after fill) | **Score 9/10.** Entry catalyst: Barclays analyst upgrade May 27 (Overweight, PT $2,300 from $1,200, within 30 days — analyst revision entry, exempt from 15% EPS threshold). Q3 FY2026 (April 30): EPS $23.41 vs ~$14 consensus = **+67.2% beat**; revenue $5.95B +97% QoQ (above guidance); $42B min revenue backlog (3 contracts Q3); Q4 FY2026 guide $7.75–8.25B (+34% QoQ), EPS $30–33 (+34% QoQ). CEO David Goeckeler verbatim: *"NAND flash is emerging as the only economically viable solution to deliver the capacity, performance, and efficiency required to keep models accessible for real-time inference at scale."* | EPS beat +67.2%; revenue vol ratio 1.53x (May 1 vs 20-day avg 15.15M); 52-week high $1,861 on June 3 (2 days ago — TOP PRIORITY); RS vs SPY since Barclays upgrade (May 27→June 4): SNDK +10.68% vs SPY +0.88% = **+9.80% spread**; analyst upgrade count: Barclays (May 27, PT $2,300), 22 analysts 86% Strong Buy, mean PT $1,714; top risk: NAND cyclicality + hyperscaler customer concentration (backlog mitigates). Next earnings Q4 FY2026 ~late July/early August 2026 (7–9 weeks). Alpaca: tradable=true, status=active ✓. Size: 6 × $1,790 = $10,740 = 10.76% equity ($99,763.86) ≤ 11% ✓. IT sector after entry: AAPL+CSCO+NVDA+SNDK ≈ 26.3% < 30% ✓. Cash after buy: ~$59,036 = 59.1% >> 10% floor ✓. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | No exit criteria triggered. All 5 positions hold (no hard stops hit, no thesis invalidations, no 60-day-with-<3%-gain rotations). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| CSCO | 54eb2e8d | $108.10 | **⚠️ CARRY-FORWARD FROM JUNE 4 — EXECUTE IMMEDIATELY AT OPEN**: Cancel 54eb2e8d; place trailing_stop 42@7% trail_percent GTC | Cancel 54eb2e8d; place trailing_stop 42 @ trail_percent=7 GTC. HWM = $129.45 (June 4 close). New stop ≈ $129.45 × 0.93 = $120.39. | CSCO closed $129.45 on June 4 (above trigger $129.16 = +10% vs avg_cost $117.42). Hard stop 54eb2e8d ($108.10) still active. Conversion NOT executed during June 4 session (no routine between midday 12:10 ET and close). market_open June 5 MUST cancel 54eb2e8d and place 7% trailing stop GTC immediately — before any other action. |

## Notes

### Macro (pre-market June 5)
- S&P 500 futures: **−0.61%** (moderately weak open expected)
- 10-year Treasury yield: **4.46%** (−4 bps; NOT at multi-month high; peak 4.70% on May 20)
- **Macro deferral rule: NOT triggered** — requires BOTH futures >−0.4% down AND yield at multi-month high; yield condition not met today
- **NFP (May 2026)** releases at 8:30 AM ET today — consensus ~65–85K; potential market swing factor; market_open must account for post-NFP reaction
- Middle East de-escalation narrative reducing oil/yield pressure — mild bullish backdrop

### Portfolio thesis checks (all intact)
- **AAPL** ($311.38 pre-mkt): WWDC June 8–12 (3 days away) — Siri 2.0, iOS 27, iPhone Fold support. Trail trigger $311.41 = **$0.03 above pre-market price** — any gap-up through $311.41 triggers Alpaca HWM update automatically. No sell.
- **CSCO** ($129.34 pre-mkt): Cisco Live AI platform fully priced; AI orders $9B FY2026; all-time high this week. Thesis intact. Trail conversion action at open.
- **GEV** ($952.20 pre-mkt): Orchestrate 2026 conference June 9–12 (potential catalyst); ex-div June 16 ($0.50×4=$2.00); UBS PT $1,400. Cushion: 3.72% above stop $916.75. Thesis intact.
- **NVDA** ($215.31 pre-mkt): Computex completed (RTX Spark launched); ex-div June 4 paid; Q2 FY2027 guide $91B intact. Cushion: 4.59% above stop $205.43. Thesis intact.
- **PWR** ($714.40 pre-mkt): Record backlog $48.5B, Oppenheimer Outperform; next earnings Jul 30 (55 days). Cushion: 8.95% above stop $650.49. Thesis intact.

### Candidates researched and disqualified
1. **MRVL** (watchlist active): Score 6/10 — **dropped at step g**. Qualifying signal: Computex June 2 / NVDA $2B investment (partnership catalyst). BUT: ALL analyst PTs at or below current price (Stifel $321 street-high vs current $316.43 = +1.4%); mean analyst PT $233 = −26.3% below current; 26M+ share dilution overhang (Celestial AI + XConn + NVDA convertible); negative EBIT margin (−12.23%); stock +54% in 5 days. Risk of −26% decline to consensus PT within 42 days is plausible. Watchlist note: "Monitor for PEAD entry **after dust settles** post-Computex spike." Entry premature.

2. **AVGO** (universe): Dropped at step f. Multiple analyst upgrades June 4 (Jefferies $550, JPM $580, GS $525 — all well above current ~$410), but stock −12% post-earnings vs SPY +0.41% = RS spread −12.4%. Negative momentum. Q3 guide $29.4B extraordinary; reassess if AVGO stabilizes above $420+.

3. **CRWD** (universe): EPS gate failed (+2.8% beat; threshold 15%). Stock −11% AH. Negative RS. Disqualified.

4. **INTC** (universe): Foxconn partnership June 3–4 (within 30 days) qualifies as clear catalyst. BUT: analyst consensus HOLD (48 analysts), mean PT $88.71 vs current ~$130 = −31.8% to consensus. Step g risk: −32% to consensus PT plausible within 42 days. Disqualified.

5. **ORCL** (universe): Wedbush PT $275 May 13 + Oppenheimer PT $235 May 12 (both within 30 days) qualify as analyst revisions. BUT: Q4 FY2026 earnings June 10 = 3 trading days away (June 8, 9, 10); entering today effectively creates earnings exposure on a new position within the holding period. Disqualified for today — reassess June 11 post-earnings if beat occurs.

6. **CIEN** (universe): Previously disqualified June 4 (score 5/10 — P/E 399x, Morgan Stanley PT $405 = −33% below current; insider selling $27.2M). No new catalyst. Skip.

### Sanity checks
- Cash floor: ✓ (after SNDK buy: ~$59,036 = 59.1% >> 10% minimum)
- Max concurrent: ✓ (6/8 after SNDK)
- Max new positions per week: ✓ (3/5: HPE June 2, PWR June 2, SNDK June 5)
- Sector caps: ✓ (IT ≈ 26.3% after SNDK; Industrials ≈ 14.6%; all < 30%)
- DRY_RUN: **false** → SNDK order is a real order for market_open to execute
