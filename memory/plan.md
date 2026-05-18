# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-18

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| GLW | 26 | $191.50 | $176.18 | Q1 2026 blowout (April 28): core sales $4.35B +18% YoY, core EPS $0.70 +30% vs $0.69 est; Optical Communications +36% YoY driven by AI hyperscaler demand; Meta $6B multi-year deal + 2 additional hyperscale mega-deals of similar size; Nvidia partnership (May 6) with $3.2B investment, 10x US optical capacity expansion, 3 new factories (NC/TX); Q2 guidance raised to ~$4.6B +14% YoY, EPS $0.73–0.77 +25% YoY. Stock pulled back ~14% from post-Nvidia-deal high on profit-taking and broad market weakness — buy-the-dip entry on an intact AI infrastructure thesis. J.P. Morgan Technology Conference presentation May 19. Next earnings July 28, 2026 (>70 days). No halt, tradable=True, status=active. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Notes

### Sizing and constraint checks (equity $100,183.51 as of 08:01 ET pre-market)

| check | value | limit | status |
|-------|-------|-------|--------|
| GLW position size | 26 × $191.50 = $4,979 (4.97% equity) | ≤5% | ✓ |
| Cash floor after GLW | ($76,014.70 − $4,979) / $100,183 = 71.0% | ≥10% | ✓ |
| Concurrent positions after GLW | 5 existing + 1 new = 6 | ≤8 | ✓ |
| New positions this week (May 18–22) | 1 / 3 | ≤3 | ✓ |
| IT sector after GLW | AAPL $4,813 + AMD $4,638 + CSCO $4,932 + GLW ~$4,979 = $19,362 / $100,183 = 19.3% | ≤30% | ✓ |
| Comm Services | GOOGL $4,749 = 4.7% | ≤30% | ✓ |
| Consumer Discretionary | AMZN $4,855 = 4.8% | ≤30% | ✓ |

### Candidates dropped

| ticker | reason |
|--------|--------|
| APP | Active SEC investigation into data collection practices (confirmed active Feb 2026, ongoing as of May 2026) — hard NO per strategy.md |
| NVDA | Q3 earnings May 20, 2026 — within 3-day window |
| ADI | Q2 earnings May 20, 2026 — within 3-day window |
| TJX, LOW, INTU | Earnings May 20, 2026 — within 3-day window |
| DE | Q2 earnings May 21, 2026 — within 3-day window; also Q2 EPS expected −12.5% YoY (no positive fundamentals signal) |
| WMT, TGT | Earnings May 21, 2026 — within 3-day window |
| MSFT | Q3 FY2026 beat (April 29): EPS +5.2% vs est, Azure +40%, AI ARR $37B +123%. BUT market sold off on $190B capex (+61% YoY); stock down 12% YTD with no recovery. Rising yields (4.63%) are headwind for capex-heavy mega-tech. Watchlist — revisit week of May 25 if yields stabilize. |
| META | Q1 2026 beat (April 29): EPS $7.31 vs $6.79 est, revenue $56.3B vs $55.5B est. BUT stock fell ~7% post-earnings on user growth miss and $125–145B capex increase. Same pattern as MSFT. Watchlist — revisit next week. |

### Macro and risk flags for market_open

- **Bearish macro today**: S&P 500 futures −0.5%, Dow −0.7%, Nasdaq −0.4%; Brent crude >$110/bbl; 10-yr yield 4.63% (highest since Feb 2025); Iran drone attack on UAE nuclear plant — no peace deal imminent. Expect weak/volatile open.
- **GLW limit strategy**: Limit set at $191.50 (below May 17 close of $191.92) to account for macro-driven downward drift. If GLW opens below $191 and the open is broadly volatile, market_open may hold the limit or tighten further — judgement call per conditions.
- **NVDA earnings Wednesday May 20**: Big catalyst for AI infrastructure broadly (positive or negative read-through for GLW optical demand thesis). If NVDA data-center guidance disappoints, GLW may trade lower — stop at $176.18 (−8%) provides protection.
- **AAPL trailing stop pre-alert**: AAPL at +5.54% ($298.77 vs avg_cost $283.10 at pre-market). Trigger: +10% = $311.41. Currently ~4.2% below trigger. Not imminent today, but market_open should be ready to immediately convert stop order to trailing stop if AAPL hits $311.41 intraday.
- **AMZN monitoring**: −2.62% vs cost; stop $248.14 (~5.8% cushion). If AMZN falls below $260 on macro weakness, stop at $248.14 will be tested (~4.9% additional decline needed). Thesis (AWS +28% YoY, Q2 guide $194–199B) remains intact.

### Prior-day exit criteria review (no exits planned)

| ticker | unrealized | stop | 60d rotation | status |
|--------|-----------|------|--------------|--------|
| GOOGL | −0.23% ($394.80 vs $395.72) | $364.07 (−7.8% cushion) | no (12d old) | Hold ✓ |
| AAPL | +5.54% ($298.77 vs $283.10) | $260.45 (−12.8% cushion) | no (12d old) | Hold ✓ |
| AMD | +0.94% ($425.55 vs $421.59) | $387.86 (−8.9% cushion) | no (12d old) | Hold ✓ |
| AMZN | −2.62% ($262.65 vs $269.71) | $248.14 (−5.5% cushion) | no (4d old) | Hold ✓ |
| CSCO | +0.18% ($117.63 vs $117.42) | $108.10 (−8.1% cushion) | no (4d old) | Hold ✓ |

No hard stops triggered, no midday cuts pending (pre-market), no trailing stop triggers, no 60-day rotation candidates. Thesis intact for all five positions.

### DRY_RUN

DRY_RUN: false — market_open WILL call /v2/orders for the GLW limit order.
