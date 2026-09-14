# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-14 (pre_market draft, ~08:1x ET). DRY_RUN: **false**.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| DELL | 19 | $560.00 | $515.20 | **Score 8/10** (IT, in universe, ADV ~$124M). Q2 FY27 (reported Sep 1 AC) blowout PEAD: **adj EPS $7.04 vs ~$4.90 = +43.7% surprise** (≫ today's raised 20% bar); revenue **$47.0B +58% YoY** (+4.8% beat, +$2.16B); **RAISED FY27 guide to ~$192B rev (+$25B) / adj EPS $25.50 (from $17.90)**; AI-server orders $60.9B, **record $95B backlog**, traditional servers +122%, CSG +20% (fastest in 5yr). **Earnings streak 4 consecutive quarters** (+1 signal, step i.i). Earnings-day **gap +8.52%** (5–10% band, no adj). **Volume 4.03x** 20-day avg (strong institutional confirmation). **52-week high 1 day ago** — fresh ATH $567.13 on Sep 11 (top-priority momentum). **RS vs SPY 5-day +11.09 pts** (DELL +9.93% vs SPY −1.16%). **Sector ETF XLK vs SPY 20-day +0.14 pts** (in-line, no penalty). **Analyst conviction strong:** Citi $515→$600, BofA $505→$600, Evercore →$650, Daiwa upgrade to Outperform; 0 downgrades (consensus Buy, avg PT $564.46 — NOTE: now BELOW Fri close, stock extended past target). Short interest low (<2%, neutral). **Insider activity NEGATIVE** — aggressive post-earnings selling: CHRO Saavedra 25,251 sh @ $520 (Sep 4), director E. Durban (Sep 4/8), heavy Silver Lake affiliate sales Sep 3–9 → **risk −1 pt** (step i.v). Mgmt quote: *"delivered another record quarter, capping a very strong first half… executing exceptionally well, driving record revenue, record EPS."* **Top risk:** AI-server margin mix + **server DRAM cost inflation +13–18% sequential into Q3** (guide assumes value-engineering margin recovery H2). Regulatory: **shelf-reg CLEAN** (June-2026 S-3 is debt-only, no equity dilution); **BIS CLEAN** (hardware OEM; no fresh 30-day export-control action). Next earnings ~Dec 1 (not within 3 days ✓). Asset active/tradable ✓. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8), no positions → no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates (all PASS → proceed):**
- Clock: `is_open=false`, `next_open=2026-09-14T09:30 ET` → opens today (Mon), NOT a holiday → pre_market proceeds (routine gate #1).
- **Reconciliation 0/0 PASS:** Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT — zero divergence. Account ACTIVE; equity **$97,328.01** (100% cash), 0/8 concurrent.
- **Universe FRESH** (screened 2026-09-13, expires 2026-09-20, 226 rows) → freshness gate PASSES; no re-screen.
- **PEAD health STALE** (computed 2026-09-06, **expires 2026-09-13 — in the past**) → per step 1c treat posture as **NORMAL but flagged STALE**; do NOT raise the bar on the stale overlay (last reading was NORMAL: realized_health_60d +0.03%, n=186). universe.md was refreshed Sun 2026-09-13 but pead_health.md was NOT — its refresh is universe_refresh's responsibility (read-only here); flagged for human.

**Regime & macro (this is the session's decisive constraint):**
- **SPY regime BULL** — SPY $764.14 (Sep-11 IEX close) vs 200-day MA **$714.20** (+6.99%); bear-regime rule NOT active (max new/week stays 5, no 20% bear override from the regime leg).
- **MACRO-DEFERRAL RULE TRIGGERED (both legs) → EPS surprise bar raised to >20% for ALL sectors today:**
  1. S&P 500 futures **down ~0.5%** premarket (Nasdaq-100 −1.1%; semis/AI under pressure) → ">0.4% down" leg MET.
  2. 10-year Treasury **~4.97%, highest since Oct 2023** → multi-month-high leg MET.
  - Context: ~86% odds of a Fed **rate HIKE** Wed (FOMC), Aug headline CPI 3.4%, elevated energy. Per strategy.md the rule RAISES the bar but does NOT halt entries — only highest-conviction setups clearing >20% enter. DELL clears at +43.7%.

**Sizing note (doc discrepancy, flagged for human):** pre_market.md step 5 says size per "strategy.md Max position size at entry field (currently 11%)" while strategy.md's field reads **20%** (a MAX/cap). Resolved by sizing at the routine's stated **11%** target ($10,706), which is compliant (below the 20% cap): DELL 19 @ $560 = $10,640 = **10.93% of equity**. Stop $515.20 = entry × 0.92 (−8% hard stop per strategy.md).

**Candidates screened / dropped this session (all vs the raised >20% bar):**
- **ORCL** (Sep 10, IT, in-univ): EPS $1.92 vs $1.73 = **+11%** — FAILS 20% bar (RPO/guidance story, not >20% EPS); also already spiked ~+36% day-of = heavily extended. Dropped.
- **ADBE** (Sep 11, IT, in-univ): EPS beat but stock **fell ~2%** AH on cautious/freemium-monetization guidance → negative PEAD reaction (RS leg fails). Dropped.
- **DG** (Aug 27, Consumer, in-univ): headline EPS +24% but ~$0.25 tariff-refund benefit → **adjusted surprise ~+11.5%** — FAILS 20% bar. Dropped.
- **MRVL** (active watchlist, non-univ semis): catalyst (+46% earnings) is 3+ months old — no fresh 30-day signal; semis weak today. Not shortlisted.
- Watchlist `pending_review` names (SNOW, GTLB, ANF, OKTA, HAE, CAVA, AFRM, AMBA, NET, TEAM, PAYC, EL, CLS, BE, FORM, THC, WDFC, EME) — human-only to set `active`; NOT tradeable, not planned.

**Sanity check vs strategy.md:** cash floor 89.07% (≥10% ✓); max concurrent 0→1 (≤8 ✓); max new/week 0→1 (≤5 ✓); single-sector IT 10.93% (≤30% ✓). 1 planned buy: DELL.

**Recurring-defer caution for market_open:** DELL has been planned 6+ sessions running (Aug 31–Sep 11) and DEFERRED every time by chase-guards (Gate 6d chaotic-open / 6e price ≤ ORH). It is now at a FRESH ATH after a wild ±5–12% two-day swing (Sep 10 −5.33%, Sep 11 +11.9%) and faces a tech-hostile open. Limit set at $560 (below Fri close $567.13) as a disciplined ceiling; expect market_open's chase-guards to gate execution.
