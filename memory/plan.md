# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-31 (Monday) — pre_market ~08:2x ET

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| CRM | 41 | $258.00 | $237.36 | **Salesforce — score 7/10 (IT, large, in universe). Guidance-raise + partnership catalyst entry (strategy.md-exempt from the 15% EPS bar).** Q2 FY2027 (reported Aug 26 AC). **EPS surprise: real non-GAAP EPS ~$3.40 = ~+4% vs $3.27 consensus — BELOW the 15% bar; the syndicated "$5.90 / +80% beat" is inflated by a one-time ~$2.6B Anthropic-stake investment gain (≈$2.63/sh), NOT recurring — so this is a CATALYST entry, not an EPS-surprise entry.** Revenue $11.35B +11% YoY (~+0.25% beat, thin). **Catalyst = the fundamentals under the pop: cRPO $33.5B +14% cc = "fastest bookings growth in four years" (1pt ahead of guide); RAISED FY27 rev guide +$300M → $46.1–46.4B ($100M organic Agentforce/Data360/Slack + $200M pending Contentful/Fin acquisitions); Agentforce ARR $1.5B +240% YoY, AI+data ARR ~$4B, work-unit usage +97% QoQ.** Earnings streak: **4/4 quarters beating** (3+ → +1 signal). Earnings-day gap **+12.6%** overnight (>10% → +1 confirmation). Volume ratio **5.26x** 20-day avg (very strong institutional). 52-week high recency: $268.98 on 2025-12-29 = **245 days ago (>90d → downrank)**; still ~5% below it — this is a downtrend-reversal, not a fresh-ATH breakout (momentum leg's weak point). Relative strength vs SPY (Aug26→28): **+24.0% spread** (huge outperformance; price $256.01 vs 21d EMA $205.89 = +24%). Sector ETF XLK vs SPY (20d): **+2.91%** (sector outperforming, no penalty). Analyst upgrades: Jefferies PT→$300 (from $250), Raymond James →$310 (from $290), Morgan Stanley →$235; "SaaSpocalypse fears squashed" (Benzinga). Stale consensus avg PT $258.52 lags the fresh post-earnings revisions ($300+). Short interest 4.2% float (low, neutral). Insider: net sellers ($59.8M sold vs $27.4M bought/yr) — mild neg, no fresh post-earnings buys. Verbatim mgmt (Benioff, Q2 call): net-new annual contract value growth *"strongest in four years,"* attrition near its lowest, contract terms improved across new business and renewals. Top risk: **chase risk** — entering after a +24% two-day vertical move on a risk-off geopolitical tape; the headline beat is investment-gain-inflated so part of the pop could fade; bears cite Agentforce revenue-inflection doubts / "value trap." Regulatory scan: **shelf-reg CLEAN** (mega-cap, no S-3/offering); **BIS N/A** (enterprise software, not semiconductor). Next earnings **Dec 2, 2026** (outside 3-day window ✓). Tradable/active NYSE ✓, no halt. Sized 41 sh @ $258 = $10,578 = **10.87% of equity** (< 20% cap; conservative non-chase limit near last close $256.01). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — no open positions, no exit criteria to fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates (all PASS):** clock is_open=false, `next_open=2026-08-31T09:30 ET` → market opens today (Mon), NOT a holiday → proceed. **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT book — zero divergence; no open/orphan orders. Account ACTIVE, trading_blocked=false; **equity $97,328.01** (=cash 100%), buying_power $389,312.04, 0/8 concurrent.
- **Universe FRESH** — screened 2026-08-30, `expires_on 2026-09-06` (in the future) → freshness gate PASSES; 259 rows. Consumed read-only (no re-screen).
- **PEAD health STALE** — `pead_health.md` `expires_on=2026-08-30` is in the past (universe_refresh's compute_pead_health.py missed again Aug 30 — Yahoo rate-limit; documented). Per pre_market step 1c: **treat posture as NORMAL but flagged STALE → do NOT raise the bar** (universe-cache gate is the hard halt, and it passed). Last real reading (computed 2026-08-23): posture NORMAL, realized_health_60d +2.284%, n=91. → **standard 15% bars, max 5 new/week.**
- **SPY regime: BULL** — computed from Alpaca IEX 200-day bars: SPY last close $769.28 (Aug 28) > 200MA $709.82 (+8.4%). Standard thresholds; bear-regime rule NOT active.
- **Macro-deferral NOT triggered** — Iran/Strait-of-Hormuz strike + retaliation over the weekend spiked oil (USO +3.7% pre-mkt, crude +3%) and lifted energy; hawkish Fed (Warsh Jackson Hole) pushed 10-yr to **~4.73%, a multi-month high (rate-hike bets rising)** → its leg SATISFIED. **BUT S&P 500 futures only ~−0.1–0.2% → the "futures down >0.4%" leg FAILS.** Both legs required → **standard bars stand** (no >20% override). Risk-off backdrop noted; strategy.md says do NOT skip entries — be selective (CRM's −8% stop caps geopolitical/oil-shock downside).
- **Overnight sweep decisions:** **CRM** = sole qualifier (planned). **MRVL** (active watchlist, IT/semi) — Q2 (Aug 26 AC) revenue beat but **sold the news: −10% Aug 28** (raised FY28 ~$18B outlook missed elevated expectations; ~0% EPS surprise) → negative PEAD step-f → DROP. **HPQ** (IT, in univ) — beat + raised guide but **stock fell ~4%** on memory-chip cost/margin concerns → negative reaction → DROP. **DG** (Dollar General, +12% on FY EPS guide raise to $7.80–8.00) — **NOT in universe cache and NOT on the active watchlist**; already considered & declined by pre_market 2026-08-28 (Consumer Staples requires >20% EPS surprise; the move is a guidance raise, not a >20% EPS beat; also a screen-source cache gap). Not re-flagged (consistent with the prior deliberate call) — surfaced to human via research_log for the next universe_refresh. No other in-universe fresh (≤30d) catalyst clearing the bar.
- **CRM decision rationale:** headline EPS "beat" is investment-gain-inflated (real surprise ~+4%, sub-15%), so this is NOT an EPS-surprise entry — it qualifies on the **guidance-raise + expanded-Anthropic-partnership catalyst** (strategy.md exempts these from the 15% threshold), now backed by **overwhelming market confirmation** the Aug 27 pre_market lacked at day-0: +12.6% gap, 5.26x volume, +24% RS vs SPY, multiple analyst PT raises, above 21d EMA. The genuine fundamental is **cRPO +14% cc — fastest bookings in 4 years** + Agentforce ARR $1.5B/+240%. Score 7/10 (signal 2 / momentum 2 / confirmation 2 / risk 1). Weak points priced in: sub-15% operating surprise, 245-day-stale 52wk-high (downtrend reversal), chase risk on a +24% 2-day vertical → hence the conservative ~11% size and a non-chase limit ($258 ≈ last close). market_open's own EMA/opening-range guards will (correctly) defer rather than chase if CRM gaps up hard.
- **Sanity-check (step 6):** post-fill cash ~89.1% >> 10% floor ✓; concurrent 0→1/8 ≤ 8 ✓; weekly new 0→1/5 ≤ 5 (BULL/NORMAL cap) ✓; sector IT (CRM) 10.87% ≤ 30% ✓. Regulatory flags among planned buys: **NONE**.
- **Watchlist flags today: none added** (DG already evaluated/declined Aug 28; no new compelling non-universe/active catalyst). MRVL is the only `active` watchlist name and was dropped on negative reaction.
- **Sizing note:** pre_market.md line 99 says "(currently 11%)" while strategy.md's `Max position size at entry` field now reads **20%**. Sized to ~11% (recent-run precedent; conservative), well within the 20% ceiling. Flagged for human to reconcile the two documents.
- DRY_RUN: false. (pre_market never trades regardless.)
