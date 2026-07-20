# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-20 (Monday) — pre_market ~08:15 ET. DRY_RUN: false.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none — 0 qualifiers)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none — book FLAT, 0/8)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none — 0 positions)_ | — | — | — | — | — |

## Notes

**NO ORDERS PLANNED — 0 candidates scored ≥6/10 after full a–i deep research.** Book stays FLAT (0/8, 100% cash). No sells (0 positions), no trailing conversions (0 positions).

**Gates (all PASS):**
- Clock: is_open=false, next_open=2026-07-20T09:30 ET → market opens today (Mon), NOT a holiday → routine proceeds.
- **Reconciliation 0/0 PASS:** Alpaca /v2/positions=[] MATCHES portfolio.md FLAT book — zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity $98,266.98, cash $98,266.98 (100%), buying_power $393,067.92.
- **Universe FRESH:** expires_on 2026-07-26 > today (screened 2026-07-19, 306 tickers).
- **PEAD health NORMAL & FRESH:** pead_health.md computed_on 2026-07-19, expires_on 2026-07-26; posture NORMAL (realized_health_60d +1.225%, health_sample_n=318, health_ok=true). Overlay is fresh and NOT ELEVATED_BAR → bar NOT raised; standard strategy.md thresholds apply (EPS >15%; >20% for Utilities/RE/Industrials/Energy; Industrials/Energy also streak≥2). This is the FIRST NORMAL posture since the overlay went stale Jun 21 — the recurring PEAD_HEALTH_REFRESH_MISS was FIXED by the Jul 19 universe_refresh (YF_DISABLE_CURL_CFFI=1 workaround). Max 5 new/week, no ELEVATED_BAR 2-position cap.
- **SPY regime BULL:** SPY close $743.28 (Jul 17 IEX) > 200MA $693.44 (+$49.84 / +7.19%). Standard thresholds; no bear-regime tightening.

**Macro (pre-market 2026-07-20):** S&P 500 futures modestly lower (~down, one source ~−1%; mixed prints on cooling housing — pending home sales −5.4% June). **10-yr Treasury yield ~4.5% — NOT at a multi-month high** (peak ~4.70% May 20). **Macro-deferral rule NOT triggered** (requires BOTH futures down >0.4% AND 10-yr at multi-month high — the 10-yr leg fails). Weekly slots 0/5 (new week, Mon Jul 20; last buy MU Jun 25).

**Screen — Q2 season week 2 (86 S&P names report Jul 20–24; mega-cap tech + Alphabet/Intel later this week). Candidates with real post-earnings drift data are last week's reporters. 0 qualified:**

- **GS (Financials) — DROP step f (post-earnings drift BROKEN).** Q2 reported Jul 14 (+45.1% EPS beat, record, 5-q streak) — but the drift has reversed: earnings-day close $1,141.87 → Jul 17 $1,065.71 = **−6.67%**, RS **−5.52pp** vs SPY; now −7.5% off the Jul 15 ATH ($1,151.95) and BELOW its 21-day EMA. market_open deferred GS 3× last week (Jul 15/16 Gate 6d chaotic-open, Jul 17 Gate 4 EMA). The "record equities-trading windfall → Q3-normalization sell-the-news" risk flagged at entry has played out. Positive PEAD drift is absent → NOT re-planned (no 4th defer). Consensus mean PT ~$1,127 now ≈ price (overshoot gone, but drift leg fails). Shelf-reg N/A, BIS N/A.
- **MS (Financials) — DROP step f (negative drift) + borderline EPS.** Q2 reported Jul 15 (EPS $3.46 vs consensus $3.03 = +14.2%, or vs $2.94 = +17.7% — sources disagree; borderline at/below the 15% Financials bar). Record rev/profit (+58%, equities-trading +69%), 4-q streak, analyst PTs $220–255 (KBW $250, Freedom $245 + upgrade, Wells $225, Citi $220, JPM $195), price ~$215 below cluster. BUT gapped **−2.38%** on the report and sold off: earnings-day close $228.48 → Jul 17 $215.42 = **−5.72%**, RS **−4.19pp** vs SPY. Same financials sell-the-news pattern as GS/C/WFC. Broken drift → DROP.
- **UNH (Health Care) — DROP step g (regulatory) + failed-breakout/distribution.** Q2 reported Jul 16: EPS $6.38 vs $4.90 = **+30.2% beat** ✓, FY guide RAISED to $19.50–20.00 (from >$18.25), MCR 86.7% (from 89.4%). BUT: (1) **Step g — mandatory drop:** active DOJ **civil AND criminal** Medicare Advantage investigation + Senate coding/billing report = material unresolved overhang that can break the thesis within 42 days (charge/settlement/headline risk). (2) **Failed breakout:** gapped +6.4% to open $452.73, spiked to a fleeting "52-wk high" $460.95 (+8.4%), then **closed $423.28 = −0.48% vs prior close** — gave back the entire gap on **2.86× volume** (distribution, not accumulation). (3) **No analyst upgrades**; consensus mean PT ~$373 < price $426 = trades above Street fair value (step-g overshoot). (4) Turnaround off multi-year lows = mean-reversion, not PEAD momentum; likely first-beat-after-cuts (weak streak, −1). Would score ~5/10 < 6 even setting aside the DOJ drop. Shelf-reg N/A.
- **ABT (Health Care) — DROP:** EPS $1.31 vs $1.28 = **+2.34% beat** << 15% bar; FY guide only marginally raised ($5.45–5.60 vs $5.38–5.58). The +11% pop is a relief rally, not a fundamental surprise of qualifying magnitude.
- **BLK (Financials) — DROP:** EPS $13.91 vs $12.59 = +10.5% beat < 15% Financials bar.
- **JBHT (Industrials) — DROP:** EPS $1.73 vs $1.55 = +11.6% beat; Industrials requires >20% AND streak≥2 (worst-sector backtest rule) — fails.
- **MAN (Industrials) — DROP:** EPS $0.99 vs $0.95 = +4.2% beat; +33% pop is a relief rally off a depressed base; Industrials needs >20%+streak — fails hard.
- **NFLX (Comm. Services) — DROP:** EPS $0.80 vs $0.79 = +1.5% surprise; Q3 guidance MISSED ($12.86B rev vs ~$13B, $0.82 EPS vs $0.84); stock −8.6% (negative reaction). Anti-PEAD.
- **MRVL (watchlist `active`, in universe) — carried DROP:** no fresh in-window earnings (Q1 FY2027 ~May 27 now ~54d stale, >30-day window); step-g overshoot pattern persists. Status stays `active` (human-only).
- **WDFC (watchlist `pending_review`) — MUST NOT plan** (human-only to set `active`); already on watchlist, no new flag. Q3 +48% beat but pending_review + likely fails $20M/day ADV liquidity gate.

**Pattern this cycle:** the big EPS surprises (GS +45%, MS +18%, C +15%, WFC +16%) all sold off post-earnings (financials sell-the-news → step-f fail); the big price pops (MAN +33%, ABT +11%, JBHT +7%, BLK +4.5%) all had sub-15% EPS surprises (relief rallies off depressed bases); UNH's +30% beat is buried under an active DOJ criminal probe and a distribution reversal. No candidate combined a >15% surprise WITH confirmed positive drift AND acceptable risk. Per routine, plan fewer buys rather than lower the bar. Q2 volume ramps hard this week (Alphabet, Intel, +84 others Jul 20–24) — fresh drift setups may qualify later in the week.

**No new watchlist `pending_review` adds** — all screened names are already in the universe (GS/MS/UNH/ABT/BLK/JBHT/NFLX) or on the watchlist (MRVL/WDFC); no compelling durable non-universe catalyst appeared.
