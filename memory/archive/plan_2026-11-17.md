# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-17 (pre_market, ~07:19 ET Tue)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $960.00 | $883.20 | **Score 8/10 (Health Care, in-universe).** Q3 2026 (reported Oct-30 BMO) non-GAAP **EPS $20.07 vs cons $16.08–16.56 = +21.2% to +24.8% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR bar on every consensus source; **revenue $5.116B = +11–12% beat** (+36% YoY). **Earnings streak 3+ quarters** (+1 signal pt). **Earnings-day gap +6.29% overnight** (Oct-29 close $817.17 → Oct-30 open $868.53; +13.5% full day to $927.63) — normal reaction (no adj). **Reaction-day volume ~5.69× 20-day avg** (Oct-30 203,641 IEX vs ~35,790 prior-20d avg) — strong institutional confirmation. **52-week high $988.48 on Nov-4 (≈9 trading days ago → top-priority recency <45d);** Nov-16 close $952.665 = −3.6% below ATH. **RS vs SPY +5.3pp (5-day)** — REGN Nov-10 $915.94 → Nov-16 $952.665 = +4.01% vs SPY $749.93 → $740.04 = −1.32%; and on the Nov-16 −1.89% risk-off day REGN fell only −0.31% = **+1.58pp resilience**. **Sector ETF XLV +6.93% vs SPY −1.19% (20-day) = +8.1pp** — Health Care leading the market (PEAD tailwind, no step-i.iii penalty). **~10 analyst PT raises / 0 downgrades** post-earnings (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980). **Short interest <2%** (neutral). **Insider:** neutral (no aggressive post-earnings selling flagged). CEO Schleifer: *"an outstanding quarter… one of our strongest years ever"* (Dupixent / Eylea-HD / Libtayo each set new all-time quarterly highs). **Top risk:** legacy-Eylea biosimilar erosion (EYLEA ~31% of rev, −41%, already priced; Q3 beat came despite EYLEA softness, Dupixent-driven) + near-ATH extension — known multi-quarter overhang, not thesis-breaking within 42d. **Regulatory scan — shelf-reg: CLEAN** (profitable large-cap, routine 2024 WKSI auto-shelf, no 2026 offering, ~103M shares stable, runs buybacks); **BIS: N/A** (Health Care, not IT/semi). Next earnings Q4 2026 ~Jan 28, 2027 (NOT within 3 days). Asset tradable=true, status=active, no halt. |

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
- **Regime: BULL** — SPY last close $740.04 (Nov-16) > 200MA $729.32 (per pead_health.md 2026-11-15), +1.5%. Standard regime-gate treatment. (Nov-16 was a sharp −1.89% risk-off day; SPY still comfortably above its 200MA.)
- **PEAD signal-health posture: ELEVATED_BAR + FRESH** (pead_health.md computed 2026-11-15, expires 2026-11-22; realized_health_60d_pct **−0.358%**, health_sample_n **163**, health_ok=false). **For this session the EPS-surprise bar is raised to >20% for ALL sectors and max new positions capped at 2.** Overlay governs NEW entries only — never exits. REGN (+21.2–24.8%) clears the raised bar.
- **Bull-and-weak case:** SPY is above its 200MA (bull) but realized PEAD drift is weak → the ELEVATED_BAR overlay raises the bar even though the regime gate alone would not. When both caps apply, use the stricter (ELEVATED_BAR = 2) new-position cap.
- **Macro-deferral rule:** not separately re-evaluated as triggered — ELEVATED_BAR already imposes the >20%-all-sectors bar, the stricter condition.
- **Gates:** clock is_open=false (pre-market) but next_open 2026-11-17T09:30 ET → opens TODAY, not a holiday → PASS. Reconciliation 0/0 PASS (Alpaca /v2/positions=[] MATCHES portfolio.md FLAT — the VRT row is inside an HTML comment, closed −8% 11-02; /v2/orders?status=open=[] no orphan stops; account ACTIVE, equity $94,946.98, 100% cash, bp $379,787.92). Universe cache FRESH (331 rows, screened 2026-11-15, expires 2026-11-22) → no re-screen.
- **Sizing:** REGN 19 sh @ $960 limit ≈ $18,240 ≈ **19.2%** of equity $94,946.98 (≤ strategy.md 20% cap; 20 sh = $19,200 = 20.2% > cap). Hard stop $883.20 = limit × 0.92 (market_open resets to fill × 0.92 after fill). ⚠ Sizing uses strategy.md's 20% field; the pre_market.md/market_open.md doc note "(currently 11%)" is stale — strategy.md wins per CLAUDE.md.
- **Sanity check vs strategy.md:** post-fill if REGN executes → cash ~80.8% (≥10% ✓); concurrent 1/8 (✓); new-per-week 1/2 under ELEVATED_BAR cap (0 opened this week — last buy was VRT 2026-10-29, stopped 11-02; REGN deferred all of Nov 6–16 with 0 fills ✓); Health Care sector 19.2% < 30% cap (✓). Regulatory flags: NONE.
- **Execution caveat for market_open:** REGN has been planned and DEFERRED on the chase-guard for 6 consecutive sessions (Nov 6–16) because it keeps opening extended above its opening-range high near the 52-wk high. The research thesis remains valid (RS strong incl. +1.58pp resilience on the Nov-16 down day, XLV leading, streak 3+, shelf-reg clean). Respect the standard opening-range / 21d-EMA / chase-guard gates — do NOT chase a large gap above $960; a calm open near $952–960 is a valid fill.
- **DROPPED / screened this session:** No fresh in-universe >20% catalyst appeared in the Nov 13–16 reporter set. Observed movers were all NON-universe or sub-bar: **CRWV** (CoreWeave +24.7% Nov-11, recent-IPO/unprofitable, not clean PEAD, not S&P 1500); **MDB** (MongoDB crush — not in universe, report-date unverified/possibly stale); **BRZE / NXT / NIQ / Rubrik** (non-universe); **TJX** (in-universe, Consumer Disc — beat + lifted FY26 but **soft Q4 guide** and EPS surprise well below the >20% bar → DROP); **NVO** (non-US ADR, not S&P 1500). **NVDA** (in-universe) reports Q3 **today Nov-17 AMC** → inside the 3-day earnings window → EXCLUDED. **MRVL** (sole active watchlist) — thesis BROKEN (Nov-2 $115B all-stock Lumentum acquisition, crashed −12.7% day / −29.6% week, TD Cowen Buy→Hold PT $350→$175 on dilution); next earnings ~Nov-26; no in-window positive catalyst → not plannable.
- **Watchlist flags:** NONE added. No verified compelling non-universe catalyst this session; the pending_review backlog is already ~28 names unactioned by the human (sibling-restraint precedent — snippet-level movers logged in research_log, not auto-added).
- **Season context:** Q3 2026 ~91% reported, aggregate surprise ~2.7% (weakest in 4 years vs ~7.5% avg) — >20% in-universe beats are scarce this cycle, consistent with a 1-name shortlist and a 7th consecutive REGN-only plan.
- ⚠ Carry-forward (human): portfolio.md bloat (~471KB of audit comments, exceeds single-read limit — needs human sign-off to trim); trade_log VRT buy+sell rows commit_sha `<pending>` (human backfill); doc discrepancy pre_market.md/market_open.md "(currently 11%)" vs strategy.md Max position size 20% (strategy.md wins per CLAUDE.md).
