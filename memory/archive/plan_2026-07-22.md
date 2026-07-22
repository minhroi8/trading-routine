# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-22 (pre_market ~08:15 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates qualified — see Notes |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — nothing to sell |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Book FLAT — no positions to trail |

## Notes

**Determination: NO BUYS, NO SELLS, NO CONVERSIONS — 0 qualifiers.** Third consecutive 0-qualifier day (Jul 20, 21, 22), same Q2-2026 weak-PEAD tape: the big EPS surprises are selling off and the pops carry sub-15% surprises.

**Gates (all PASS to proceed with research):**
- Clock: `is_open=false`, `next_open=2026-07-22T09:30 ET` → market opens today (Wed), NOT a holiday → routine proceeds.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT book — zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity **$98,266.98**, cash $98,266.98 (100%), buying_power $393,067.92.
- Universe cache **FRESH**: `expires_on 2026-07-26` > today (screened Jul 19, 305 ticker rows).

**PEAD health overlay:** posture **NORMAL & FRESH** (pead_health.md computed_on 2026-07-19, expires 2026-07-26; realized_health_60d **+1.225%**, n=318, health_ok=true). Bar NOT raised → standard strategy.md thresholds: EPS >15% (>20% for Utilities/RE/Industrials/Energy; Industrials & Energy also need streak≥2); **max 5 new/week**, no ELEVATED_BAR cap.

**Regime:** SPY **BULL** — Jul 21 close $748.155 (IEX) > 200MA $693.44 (+$54.72 / +7.9%). Standard operation.

**Macro-deferral rule:** not triggered — no evidence both legs fire (S&P futures not down >0.4% AND 10-yr at multi-month high); bar stays at standard 15%.

**Candidates screened — 0 qualified:**
- **COF (Capital One, Financials, in universe) DROP — sell-the-news / broken drift + 0 completed drift days + low-quality beat.** Q2 reported Jul 21 AC: adj EPS **$5.81 vs ~$4.68 consensus = +24.2% beat** (clears 15% Financials bar); revenue $15.85B +26.9% YoY but only +0.96% surprise. BUT beat is credit-provision-driven ($662M reserve release; provision fell $1.1B QoQ) = low-quality PEAD surprise. Stock **fell −7.6% after-hours** and traded broadly flat/lower premarket (below $210) on Discover-integration & top-line concerns → anti-PEAD reaction. Reported after close Jul 21 → **0 completed regular-session drift days** at this pre-market → step f/i-ii not computable = incomplete a–i = auto-DQ, and the negative AH reaction independently breaks the drift thesis (same pattern as GS/MS/UNH this week). Shelf/BIS N/A.
- **GM (Consumer Disc, in universe) DROP — EPS surprise below the 15% bar.** Q2 reported Jul 21 BMO: EPS **$3.57 vs ~$3.13–3.20 consensus = +11.6% to +14.1% beat** — **below the 15% Consumer Discretionary threshold** → fails the earnings-driven entry gate (guidance raise alone is not EPS-threshold-exempt; only analyst-revision/partnership catalysts are). Drift day-1 IS positive (Jul 20 $75.82 → Jul 21 $79.56 = **+4.93%**, RS **+4.12pp** vs SPY +0.81%; 4-quarter beat streak, raised FY EBIT guide to $14–16B on favorable tariff adj) — but only 1 completed drift day and the surprise doesn't clear the bar. Strong WATCH if a future beat clears 15%; not planned today.
- **BLK (Financials) DROP** — Q2 EPS $13.91 vs $12.69 = +9.6% < 15% Financials bar (best-day-in-a-year +7% pop, but sub-bar surprise).
- **MS DROP** (+14.2%/+17.7% borderline, sold off −5.7% since report — dropped Jul 20). **UNH DROP** (DOJ MA probe step-g + distribution reversal — dropped Jul 20). **GS DROP** (+45.1% beat but drift broken −6.7%, 3× market_open defer last wk — not re-planned). **TRV DROP** (cat-reversal risk step-g, flat drift — dropped Jul 21). **ISRG/TFC/ABT/JBHT/MAN/NFLX** all dropped prior days (sub-bar surprise or anti-PEAD reaction).
- **TXN (IT/semi, in universe) DROP — reports TODAY Jul 22 AC → earnings event risk (step 4, inside 3-day window) + BIS export-control scan required.** 0 drift days. Not plannable today.
- **TSLA / GOOGL (in universe) DROP — report TODAY Jul 22 AC** → event risk, 0 drift days.
- **CB (Financials, in universe) DROP — reports TODAY Jul 22 BMO** → 0 drift days, not yet evaluable.

**Out-of-universe reporters (no pending_review add warranted):** MMM (3M, beat-and-raise +9% pop but Industrials → needs >20% surprise + streak≥2; not in universe), HAS (Hasbro +10% relief pop; not in universe) — neither clears strategy.md thresholds nor rises to the WDFC +48%-beat precedent for a compelling non-universe add.

**Watchlist carries:** MRVL (active, in universe) — Q1 FY27 ~May 27 now ~56d stale (>30d), step-g overshoot; status stays active (human-only), no new plan. WDFC (pending_review) — MUST NOT plan (human-only to set active); already listed, no new flag.

**Sanity check (moot — 0 buys):** cash floor 100% >> 10% ✓; concurrent 0/8 ✓; weekly new positions 0/5 (BULL regime; week of Mon Jul 20; last actual fill MU Jun 25 = prior weeks) ✓; no sector exposure ✓. DRY_RUN: **false**.
