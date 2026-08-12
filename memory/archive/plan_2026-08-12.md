# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-12 (pre_market ~08:30 ET). Regime **BULL** (SPY $770.52 > 200MA $703.96, +9.45%). PEAD health **STALE→NORMAL** (computed 2026-08-02, expired 2026-08-09; treated NORMAL flagged STALE per step 1c — bar NOT raised; last fresh realized_health_60d +2.008%, n=269). Standard 15%/20% sector bars, max 5 new/week. Macro-deferral NOT triggered (premarket S&P futures +0.2% up; 10-yr leg moot). DRY_RUN: **false**.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,240.00 | $1,140.80 | **Eli Lilly — Health Care (large) — score 9.5/10.** Q2 2026 (reported Aug 5 AM) **adj EPS $8.38 vs ~$6.58 est = +27.3% surprise** (clears standard 15% Health-Care bar; >20% margin), **revenue $22.97B vs $20.62B = +11.4% beat / +48% YoY**; **RAISED FY26 guide** to $85–87B rev (from $82–85B) + adj-EPS midpoint ~$36.25 (+5.8%). Mounjaro+Zepbound $14.9B combined, +37% volume, 60.9% US obesity/diabetes share. **Streak:** established multi-quarter beat (+1 signal). **Earnings-day gap +6.15%** (faded intraday −1.43% → full-day +4.64%; drift confirmed — stock ran to $1,212.92, +8.5% over 5 sessions). **Vol 2.18x** 20-day avg (strong). **52-week high $1,248.53 on 2026-07-07 = 25 td ago (top-priority recency)**, now −2.9% below. **RS +8.62%** vs SPY (5-day). **Sector XLV +6.13% vs SPY +2.47% (20-day) = outperforming (+3.66%).** Analysts **Strong Buy 22/29**; Wells Fargo PT→$1,000. **Insider:** none flagged (neutral). **Short interest** low <2% (neutral). Verbatim (CEO Dave Ricks): *"it's hard to think of a time that we've been in a better position than this"* + oral space is *"expansionary, it's not cannibalizing Zepbound."* **Top risk:** Novo Nordisk competition + Jul-21 false-advertising lawsuit; CVS opting out of Medicare obesity coverage; rich valuation — none a 42-day thesis-breaker (LLY leading the GLP-1 race). **Regulatory:** shelf-reg CLEAN (no S-3/offering; stable 943M shares); BIS N/A (not IT). Next earnings ~90d out (not in 3-day window). Active/tradable NYSE. Sizing 9×~$1,213 ≈ 11.1% < 20% cap. |
| PLTR | 62 | $180.00 | $165.60 | **Palantir — Information Technology (large) — score 7/10.** Q2 2026 (reported after close Aug 3) **adj EPS $0.41 vs $0.35 est = +17.1% surprise** (clears standard 15% IT bar), **revenue $1.94B vs $1.81B = +7.2% beat / +93% YoY (highest ever)**; US commercial +149% YoY. **RAISED FY26 guide** to $8.15–8.16B (+82% YoY) + US-commercial +134%. **Streak: 8 consecutive beats (+1 signal).** **Earnings-day gap ≈+15%** (IEX; news "+12% pop") → >10% (+1 confirmation). **Vol ≈5.5x** 20-day avg (strong; IEX pre-earnings prints thin → magnitude approximate). **RS +7.66%** vs SPY (5-day). Analysts: Citi PT→$245, DA Davidson→$200, Baird $200 ("premier AI growth asset"); consensus Buy, avg PT $189.9. Verbatim (CEO Alex Karp): *"demand for AI sovereignty has now been unleashed"* / *"This revolution has taken off, and you can't put it back in the bag."* **Offsets:** **52-week high $207.50 on 2025-11-03 = 192 td ago (>90d → momentum downrank)**, now −15.7% below high; **sector XLK +1.38% vs SPY +2.47% (20-day) = underperforming (−1 momentum)**; **heavy insider selling** (Karp ~$2B/2yr under 10b5-1; −1 risk); **valuation ~130x fwd / ~40x P/S** (Citron short thesis). **Regulatory:** shelf-reg CLEAN (insider sales are 10b5-1 secondary, not dilution; no S-3/offering); BIS CLEAN — software, not a chip exporter (2026 BIS rules target advanced AI semiconductors only). Next earnings ~90d out (not in 3-day window). Active/tradable NASDAQ. Sizing 62×~$174.94 ≈ 11.05% < 20% cap. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME held: no exit criterion fired since market_close. Cur ~$825.84 (−1.0% vs cost $834.12), hard stop 96e4e855 @ $767.39 GTC intact (cushion ~7.1%); thesis intact (Q2 +25.31% surprise, RAISED FY26 guide, record RPO backlog $17.1B); held 7d (not 60d-stale); not −8%, not +10% trail. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME −1.0%, far below +10% trailing trigger. |

## Notes

- **Gates:** clock next_open=2026-08-12T09:30 ET (opens today, not a holiday) ✓. **Reconciliation 1/1 PASS** — Alpaca /v2/positions = EME 13 @ $834.12 matches portfolio.md exactly; zero divergence. Account ACTIVE, equity $98,159.33, cash $87,423.41 (89.1%), 1/8 concurrent. **Universe FRESH** (screened 2026-08-09, expires 2026-08-16, 302 rows). **PEAD health STALE** (expired 2026-08-09) → NORMAL flagged STALE, bar NOT raised (universe gate is the hard halt and PASSES). **4th consecutive week the Sunday universe_refresh updated universe.md but not pead_health.md — surfaced for human.**
- **Regime BULL** (SPY $770.52 > 200MA $703.96) → standard thresholds, max 5 new/week. Macro-deferral NOT triggered (futures +0.2%). **CPI report due today** — macro event risk; market_open should weigh the open.
- **Shortlist (2 qualified ≥6):** LLY 9.5/10, PLTR 7/10. Fewer than 3 cleared — planned 2 buys rather than lowering the bar (per routine step 3).
- **Dropped candidates:** **AXON** — Industrials adj EPS $1.88 vs $1.83 = **+2.73% surprise**, fails the Industrials **>20% EPS + streak≥2** gate (worst-backtest sector; shares fell after-hours despite the beat). **VRTX** — adj EPS $4.73 vs ~$4.75–4.79 est = **EPS MISS** (rev-only beat); fails earnings-beat entry criterion. **GOOGL** — reported EPS "+216%" is a **one-time Anthropic-stake markup** (rev beat only +2.3%); stock **sank** on capex hike → no positive PEAD drift; reported Jul 22 (aging). **AMD** — beat but **in-line guidance** weakens drift; semiconductor (BIS scan) — not shortlisted this session.
- **Watchlist:** only **MRVL** is `status: active`; no fresh 30-day earnings catalyst (last report ~2.5 mo ago; next earnings **Aug 27**, outside 3-day window) → not shortlisted. All other watchlist rows remain `pending_review` (human-only to activate). No new watchlist additions this session (LLY/PLTR/AXON/VRTX/GOOGL all already in universe).
- **Position sizing:** 11% target of equity $98,159 = $10,797; 20% is the hard cap (per strategy.md). LLY 9 sh ≈ 11.1%, PLTR 62 sh ≈ 11.05%. Stop = limit × 0.92 (−8%); market_open computes the real stop from fill price.
- **Sanity check (step 6) — all PASS:** cash floor after both fills ~67% >> 10% ✓; concurrent 1→3 ≤ 8 ✓; new-per-week 0→2 ≤ 5 (BULL) ✓; sector caps — Industrials (EME) 10.8%, Health Care (LLY) 11.1%, IT (PLTR) 11.05%, all << 30% ✓. No trims needed.
- **IEX data caveat:** PLTR pre-earnings daily bars are thin (Aug-4 prevclose $125.89 vs news "+12% pop") — gap/volume magnitudes are directional/approximate, not exact.
- market_open MUST re-run its own entry gates (sizing, 21-EMA, active/tradable, opening-range 6d/6e breakout) before sending any order; these are pre_market drafts only.
