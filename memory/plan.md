# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-16 (pre_market, ~07:19 ET Mon)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $965.00 | $887.80 | **Score 8/10 (Health Care, in-universe).** Q3 2026 (reported Oct-30 BMO) non-GAAP **EPS $20.07 vs ~$16.08 cons = +24.8% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR; **revenue $5.116B = +11.2% beat** (+36% YoY). **Earnings streak 3+ quarters.** **Earnings-day gap +6.3%** overnight (Oct-29 close $817.17 → Oct-30 open $868.53; +13.5% full day). **Volume ~4–8× 20-day avg** on the reaction day (203,641 IEX vs ~25–47k prior days) — strong institutional confirmation. **52-week high $988.48 on Nov-4 (12 days ago → top-priority recency);** last close $955.66 (~3.3% below ATH). **RS vs SPY +3.6pp (5-day)** — the Nov-4 ATH blow-off reversal has recovered; REGN drifted $920.33 (Nov-9) → $955.66 (Nov-13) = +3.84% vs SPY +0.21%. **Sector ETF XLV +6.93% vs SPY −1.19% (20-day) = +8.1pp** — Health Care leading the market (PEAD tailwind). **~10 analyst PT raises / 0 downgrades** post-earnings. **Short interest <2%** (neutral). **Insider:** neutral (no aggressive post-earnings selling flagged). CEO Schleifer: *"an outstanding quarter… one of our strongest years ever"* (Dupixent / Eylea-HD / Libtayo each set new all-time quarterly highs). **Top risk:** legacy-Eylea biosimilar erosion (−41%, already priced) + an FDA cemdisiran (gMG label-expansion) decision expected in November (binary but a smaller indication, not a core driver) + near-ATH extension. **Regulatory scan — shelf-reg: CLEAN** (profitable large-cap, no 2026 offering); **BIS: N/A** (Health Care, not IT/semi). Next earnings ~late-Jan/early-Feb 2027 (NOT within 3 days; Jefferies conf presentation Nov-17 is not an earnings event). Asset tradable=true, status=active, no halt. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) since VRT −8% hard-stop exit 2026-11-02 — no positions, so no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

- **DRY_RUN: false** (strategy.md). pre_market never trades regardless; this handoff is for `market_open` to execute.
- **Regime: BULL** — SPY last close $754.27 (Nov-13) > 200MA $729.32 (per pead_health.md 2026-11-15), +3.4%. Standard regime-gate treatment.
- **PEAD signal-health posture: ELEVATED_BAR + FRESH** (pead_health.md computed 2026-11-15, expires 2026-11-22; realized_health_60d_pct **−0.358%**, health_sample_n **163**, health_ok=false). **For this session the EPS-surprise bar is raised to >20% for ALL sectors and max new positions capped at 2.** Overlay governs NEW entries only — never exits. REGN (+24.8%) clears the raised bar.
- **Bull-and-weak case:** SPY is above its 200MA (bull) but realized PEAD drift is weak → the ELEVATED_BAR overlay raises the bar even though the regime gate alone would not. When both caps apply, use the stricter (ELEVATED_BAR = 2) new-position cap.
- **Macro-deferral rule:** not separately re-evaluated as triggered — ELEVATED_BAR already imposes the >20%-all-sectors bar, the stricter condition.
- **Gates:** clock is_open=false (pre-market) but next_open 2026-11-16T09:30 ET → opens TODAY, not a holiday → PASS. Reconciliation 0/0 PASS (Alpaca /v2/positions=[] MATCHES portfolio.md FLAT; /v2/orders?status=open=[] no orphan stops; account ACTIVE, equity $94,946.98, 100% cash, bp $379,787.92). Universe cache FRESH (331 rows, screened 2026-11-15, expires 2026-11-22) → no re-screen.
- **Sizing:** REGN 19 sh @ $965 limit ≈ $18,335 ≈ **19.3%** of equity $94,946.98 (≤ strategy.md 20% cap; 20 sh would be 20.3% > cap). Hard stop $887.80 = limit × 0.92 (market_open resets to fill × 0.92 after fill).
- **Sanity check vs strategy.md:** post-fill if REGN executes → cash ~80.7% (≥10% ✓); concurrent 1/8 (✓); new-per-week 1/2 under ELEVATED_BAR cap (0 opened this week — last buy was VRT 2026-10-29 last week; REGN deferred all of Nov 10–13 with 0 fills ✓); Health Care sector 19.3% < 30% cap (✓). Regulatory flags: NONE.
- **Execution caveat for market_open:** REGN has been planned and DEFERRED on the chase-guard for 5 consecutive sessions (Nov 6–13) because it keeps opening extended above its opening-range high near the 52-wk high. The research thesis remains valid and improved (RS recovered, XLV leading). Respect the standard opening-range / chase-guard gates — do NOT chase a large gap above $965; a calm open near $955–965 is a valid fill.
- **DROPPED candidates (completed/partial research):** **APP** (AppLovin, IT, in-universe) — +31% pop but EPS $4.30 vs ~$3.94–4.04 cons = only **~6–9% beat**; fails the >20% bar. **IDXX** (IDEXX, HC, in-universe) — +20% pop but non-GAAP EPS $3.98 vs $3.71 = only **+7.3% beat**; fails the >20% bar (and standard 15%). **CEG** (Constellation, Utilities, in-universe) — adj EPS $5.06 vs ~$3.90 = ~+30% surprise (clears bar) BUT **52-wk high $379.91 was 2025-12-11 (~340 days ago), now 26% below high** (fails momentum/52wk-recency), muted +4.3% earnings-day gap despite the "beat," GAAP profit down YoY, Utilities = deprioritized weak-PEAD sector → scored ~5.5/10, below threshold. **MRVL** (active watchlist) — BROKEN: Nov-2 announced $115B all-stock Lumentum acquisition → crashed −12.7% day-of / −29.6% on the week; TD Cowen downgraded Buy→Hold, cut PT 50% ($350→$175) on dilution; no fresh beat catalyst + unreported Q3 due late-Nov → dropped.
- **Watchlist flag added:** **AAON** (Industrials, HVAC/data-center cooling, NOT in universe, NOT previously watchlisted) → `status: pending_review`. Q3 (reported Nov-9) diluted EPS $0.83 vs $0.57 cons = +45.6% surprise; revenue $707M +84% YoY; raised FY sales-growth guide to 72–75% (3rd raise); stock +22–23%. **Caveat: material control weakness + restated Q1/Q2 2026 financials** (governance/earnings-quality flag); Industrials = strategy-deprioritized (needs >20% EPS AND streak≥2). Human-only to set active.
- Season context: Q3 2026 ~91% reported, aggregate surprise just **2.7% (weakest in 4 years** vs 7.5% avg) — >20% in-universe beats are scarce this cycle, consistent with a thin shortlist.
- ⚠ Carry-forward (human): portfolio.md bloat (~467KB audit comments, exceeds single-read limit — needs human sign-off to trim); trade_log VRT buy+sell rows commit_sha `<pending>` (human backfill); doc discrepancy pre_market.md/market_open.md "(currently 11%)" vs strategy.md Max position size 20% (strategy.md wins per CLAUDE.md).
