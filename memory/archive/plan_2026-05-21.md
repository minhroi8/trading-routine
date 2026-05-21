# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-21

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| NVDA | 22 | $224.00 | $206.08 | Q1 FY2027 blowout (May 20 after close): Rev $81.6B vs $79.2B est (+85% YoY), non-GAAP EPS $1.87 vs $1.76 est (+6.3% beat); Data Center $75.2B (+92% YoY); Q2 FY2027 guide $91.0B vs $86.84B consensus (+4.8% beat on forward — street high). $80B buyback authorized + dividend raised $0.01→$0.25/share. Next earnings Aug 26, 2026 (97 days). Alpaca tradable=True, status=active; no halt, no SEC investigation. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Notes

**Sanity checks (per strategy.md):**
- Cash floor: post-trade cash ~$62,295 (62.3% of equity $100,028) >> 10% minimum ✓
- Max concurrent positions: 8/8 after NVDA fill — no new buys until a position closes ✓
- Max new-per-week: 3/3 this week (GEV May 19 + MSFT May 20 + NVDA May 21) — no new positions until week of May 25 ✓
- Sector cap — IT: AAPL+AMD+CSCO+MSFT = 19.3% + NVDA 4.93% = 24.2% << 30% cap ✓
- Sizing: 22 × $224 = $4,928 = 4.93% of equity ≤ 5% max ✓
- DRY_RUN: false — market_open MUST place actual Alpaca limit order + stop order

**NVDA thesis:** Freshest catalyst available today (reported last night May 20). Q2 guide $91.0B vs $86.84B consensus is 4.8% above street — not priced in pre-earnings. Data Center +92% YoY is the fastest segment growth NVDA has ever reported at this revenue base. Pre-market muted reaction (+1.93%) after a 20% pre-earnings run means the entry is actually at a slight discount to the May 17 universe screen price ($225.31). Analyst PT raises from overnight will flow in today and Friday, providing near-term price support. Stop $206.08 = $224 × 0.92 (-8%). Next earnings 97 days out — clear window.

**AMD trailing-stop alert (high priority for market_open):** AMD closed May 20 at $447.21 (+6.08% vs avg_cost $421.59). Trailing-stop trigger at +10% = $463.75. Stock is only $16.54/share below trigger. OpenAI 6 GW + Meta ~$60B MI450 contracts announced May 20 are fresh catalysts — AMD could gap toward trigger at open. market_open MUST be ready to convert hard stop $387.86 → 7% trailing stop below session peak immediately if AMD trades ≥ $463.75 at any point during the session.

**MSFT ex-dividend today May 21:** $0.91/share × 11 shares = $10.01 cash credit to account. Stock expected to open ~$0.91 lower (~$420.54 adjusted reference). Stop $379.62 unaffected by ex-div adjustment.

**Candidates dropped — both caps exhausted after NVDA:**
- PWR (Industrials, ~$773 premarket): Q1 2026 blowout Apr 30 (EPS $2.68 vs $2.03 est, record backlog $48.5B); analyst PTs $775–$900 (UBS $900, Evercore $800, JPMorgan $805); NVDA blowout confirms AI infrastructure demand. Dropped: 8/8 concurrent + 3/3 weekly cap. **Priority watchlist for week of May 25.**
- ETN (Industrials, ~$380): Q1 beat May 5 (data center orders +240% YoY), analyst PTs $453–$509 (Morgan Stanley $500, Bernstein $509). Dropped: same cap constraints + 10-yr yield 4.67% headwind on high-multiple industrials. **Priority watchlist for week of May 25 if yields stabilize.**

**Macro context:** 10-yr yield 4.67% (near 16-month high), Iran talks stalled (Supreme Leader directive to keep enriched uranium in-country), Moody's Aa1 downgrade overhang. S&P 500 futures −0.2%, Nasdaq −0.4% pre-market. NVDA earnings are a partial offset for AI/semiconductor names. Risk environment remains elevated — honor stops, do not average down on any position.
