# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-19

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| GEV | 4 | $1,015.00 | $933.80 | Q1 2026 blowout (April 30): EPS $2.01 vs $1.67 est (+20% beat), revenue $9.34B +16% YoY; orders $18.3B (+71% YoY, nearly fully booked through 2027); Electrification segment booked $2.4B in Q1 data center orders alone (exceeding entire 2025 data center total); FY2026 revenue guidance raised to $44.5–$45.5B; EBITDA margin guide raised to 12–14% (+1pp). Structural AI data center power demand — uniquely positioned as US grid electrification accelerates. Stock pulled back from $1,048.81 (May 15 close, universe reference) to $1,012.36 (May 18 close, −3.5%) on macro weakness. Industrials sector provides portfolio diversification from tech-heavy holdings. Next earnings July 29, 2026 (>70 days, confirmed). tradable=True, status=active (Alpaca confirmed), no halt or SEC investigation. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Notes

### Sizing and constraint checks (equity $99,775.52, cash $75,748.26 as of pre-market 08:04 ET)

| check | value | limit | status |
|-------|-------|-------|--------|
| GEV position size | 4 × $1,015.00 = $4,060 (4.07% equity) | ≤5% | ✓ |
| Cash floor after GEV | ($75,748.26 − $4,060) / $99,775.52 = 71.8% | ≥10% | ✓ |
| Concurrent positions after GEV | 5 existing + 1 new = 6 | ≤8 | ✓ |
| New positions this week (May 18–22) | GLW (opened+cut May 18 = 1) + GEV = 2/3 | ≤3 | ✓ |
| Industrials sector after GEV | GEV $4,060 / $99,775.52 = 4.1% | ≤30% | ✓ |
| IT sector | AAPL $5,031 + AMD $4,546 + CSCO $4,928 = $14,505 / $99,775 = 14.5% | ≤30% | ✓ |
| Comm Services | GOOGL $4,786 = 4.8% | ≤30% | ✓ |
| Consumer Discretionary | AMZN $4,737 = 4.7% | ≤30% | ✓ |

### Prior-day exit criteria review (no exits planned)

| ticker | unrealized (pre-market) | stop | 60d rotation | status |
|--------|-------------------------|------|--------------|--------|
| GOOGL | +0.78% ($398.80 vs $395.72) | $364.07 (−8.7% cushion) | no (13d old) | Hold ✓ |
| AAPL | +4.54% ($295.94 vs $283.10) | $260.45 (−11.9% cushion) | no (13d old) | Hold ✓ |
| AMD | −1.97% ($413.30 vs $421.59) | $387.86 (−6.1% cushion) | no (13d old) | Hold ✓ |
| AMZN | −2.44% ($263.14 vs $269.71) | $248.14 (−5.7% cushion) | no (5d old) | Hold ✓ |
| CSCO | −0.07% ($117.33 vs $117.42) | $108.10 (−7.9% cushion) | no (5d old) | Hold ✓ |

No hard stops triggered, no midday cuts pending (pre-market), no trailing stop triggers (AAPL +4.54%, trigger at +10% = $311.41 not reached), no 60-day rotation candidates. All theses intact.

### Candidates dropped

| ticker | reason |
|--------|--------|
| STX | Negative catalyst May 18: CEO Dave Mosley rejected factory expansion plans at JPMorgan conference ("would take too long"); stock fell 7.5%–8.87% to ~$736. Capacity ceiling concern partially damages the AI HDD demand growth thesis. Dropped. |
| SBUX | Current price ~$106.73 is above analyst consensus average PT ~$104.93; limited upside to consensus. Turnaround thesis intact (Q2 rev +9%, comp +6.2%, EPS $0.50 +22%) but no margin of safety at current entry. Watchlist — revisit on analyst PT upgrade cycle. |
| MSFT | Capex overhang + 10-yr yield ~4.60% (Moody's Aa1 downgrade aftershock) headwind for capex-heavy mega-tech ($190B capex guidance). Stock down ~12% YTD despite Q3 beat. Revisit week of May 25 if yields stabilize. |
| META | Same capex-selloff pattern as MSFT; still ~23% below April 2026 high of ~$796; not yet technically stabilized. 96% analyst Buy, avg PT $839 (37% upside). Revisit next week. |
| PLTR | 97× forward PE makes it acutely yield-sensitive; rate cut expectations nearly priced out (40% probability +25bps hike). Moody's downgrade = further yield pressure. Fundamental thesis excellent but valuation headwind severe. Watchlist. |
| NVDA | Q1 FY2027 earnings May 20, 2026 (tomorrow) — within 3-day window. No entry. |

### Macro and risk flags for market_open

- **Risk-off environment**: S&P 500 futures −0.4%, Nasdaq 100 futures −0.6%; chip stocks continuing to sell off. Moody's downgraded US sovereign debt to Aa1 Friday May 15 after close — 10-yr yield ~4.60%, 30-yr briefly >5.01% Monday May 18. Rate cut expectations nearly priced out; ~40% implied probability of a +25bps hike in 2026. Oil modestly lower on Trump-Iran news (WTI −1.4% to $102.90, Brent −1.8% to $110.10).
- **NVDA earnings TOMORROW (May 20, after close)**: Consensus $78B revenue / $1.77 EPS / $73B data center; whisper $80B+; options pricing 8–10% implied move. If NVDA disappoints, broad AI/tech sell-off could affect AMD, GOOGL, CSCO (directly) and GEV (indirectly via data center demand sentiment). market_open should assess sector tone before committing to GEV limit order.
- **GEV limit note**: Limit $1,015 is set just above May 18 close ($1,012.36). GEV is NYSE-listed Industrials (power grid/electrification infrastructure) — less correlated to chip-sector NVDA event than pure semis. However, if broad market sells off sharply (S&P 500 −1.5%+), consider holding the order. Limit is already conservative; do not chase above $1,020.
- **AAPL trailing stop pre-alert**: AAPL +4.54% ($295.94 vs avg_cost $283.10). Trigger: +10% = $311.41. Currently ~5.2% below trigger. Not imminent today, but market_open should be prepared to immediately convert stop order to trailing stop 7% below peak if AAPL hits $311.41 intraday.
- **AMD sector sympathy**: AMD at −1.97% vs cost ($413.30 current); chip sector under pressure ahead of NVDA earnings May 20. Stop $387.86 active (~6.1% below current). If AMD sells off −5%+ intraday ahead of NVDA, midday will flag for cut threshold check.
- **AMZN monitoring**: −2.44% vs cost ($263.14); stop $248.14 (5.6% below current). AWS thesis intact; no immediate stop risk at normal market movements.

### DRY_RUN

DRY_RUN: false — market_open WILL call /v2/orders for the GEV limit order, subject to conditions judgment at open.
