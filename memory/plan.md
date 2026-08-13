# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-13 (pre_market ~08:30 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,260 | $1,122.37 | **TOP PICK — score 8/10 (Eli Lilly, Health Care, in-universe).** Q2 2026 (reported **Aug 5 BMO**): **rev $22.97B +48% YoY = +11.4% beat** (Mounjaro $9.9B +91%, Zepbound $4.9B +46%); adj EPS $8.38 noisy (incl. **$3.03/sh IPR&D charge** — ex-IPR&D operational beat well >15%; clean surprise ~+27%) → qualifies on **operational EPS beat >15% + analyst-revision/catalyst-exempt basis**. **FY26 rev guide RAISED to $85–87B** (from $82–85B); FY non-GAAP EPS $35.50–36.50. **4-qtr beat streak** (+1). **Earnings gap +6.15%** (normal band). **Reaction-day vol 2.18x** (strong institutional confirmation). **52-wk high $1,248.53 on 2026-07-07 = 26 sessions ago (top-priority <45d), only −2.3% below high.** **RS since earnings +3.98pp** (Aug5 $1,169.29→Aug12 $1,219.97 = +4.33% vs SPY +0.36%; drift INTACT, price +3.1% above 21d EMA $1,183.47). **XLV +4.02pp vs SPY 20d** (strong sector momentum). **PT raises 0 downgrades** (MS $1,419 OW, Cantor $1,410 OW, BMO $1,400 OP, JPM $1,400 OW top-pick, Truist $1,376 Buy; Street 22 buys / 2 sells). SI ~1% (neutral). Insider: routine exec sells (Zakrowski 2k @ $1,185 Aug 10, Hakim 5k @ $1,190 Aug 7), no buying — neutral. Ricks: *"Lilly's momentum continues, as we delivered 48% revenue growth and raised our full-year guidance."* **TOP RISK:** orforglipron/Foundayo launch softness + Novo oral-GLP-1 price war + MFN/TrumpRx pricing overhang + ~45x P/E — **none a 42-day binary** (core incretin franchise drove the raise; next earnings ~Oct 29 outside 42d window); −8% stop protects. **Shelf CLEAN** (only $9B debt/notes settled May 2026, non-dilutive; no equity offering). **BIS N/A** (pharma). Active/tradable NYSE ✓. Sized 9 sh × ~$1,220 ≈ $10,980 = **11.2%** of equity ($98,257.61), < 20% cap. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME (13 @ $834.12, hard stop 96e4e855 $767.39 GTC) — thesis INTACT (Q2 blowout +25.31% surprise, raised FY26 guide, record RPO backlog $17.1B); mark ~$833 = −0.09% vs cost; held 8d (not 60d-stale); not −8% (no hard-stop cut) and not +10% (no trailing trigger) → HOLD, no exit criterion fired. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME +0.x% far below +10% trailing trigger; no conversion. |

## Notes

- **Gates:** Alpaca `/v2/clock` `is_open=false`, `next_open=2026-08-13T09:30 ET` → opens **today (Thu), NOT a holiday** → proceed. **RECONCILIATION 1/1 PASS:** Alpaca `/v2/positions` = EME 13 @ $834.12 MATCHES portfolio.md exactly (hard stop 96e4e855 @ $767.39 GTC); zero divergence. Account ACTIVE, trading_blocked=false; equity **$98,257.61**, cash $87,423.41 (89.0%), 1/8 concurrent.
- **Universe FRESH** (screened 2026-08-09, expires 2026-08-16, 302 rows) → freshness gate PASSES.
- **PEAD health STALE** (computed 2026-08-02, expires 2026-08-09 < today → treated **NORMAL flagged STALE** per step 1c; bar NOT raised — universe gate is the hard halt and PASSES; last fresh NORMAL: realized_health_60d +2.008%, n=269). **3rd consecutive week the Sunday universe_refresh updated universe.md but NOT pead_health.md — surfaced for human.**
- **SPY regime BULL** (Aug 12 IEX close $772.54 > 200MA $701.69, n=200, +10.1%) → standard 15% bars, max 5 new/week (no ELEVATED_BAR cap).
- **Macro-deferral NOT triggered:** premarket S&P futures **UP ~+0.2%** → "futures down >0.4%" leg FAILS; **CPI (Aug 12) +0.1% MoM / +3.4% YoY in-line/disinflationary; PPI (Aug 13) below expectations** → risk-on; 10-yr ~4.67% elevated but **NOT a fresh multi-month high** (was 4.73% earlier Aug) → both legs required, standard bars apply.
- **Weekly slots:** week of Mon Aug 10 has **0 actual fills** (LLY deferred by market_open on Gate-6 Aug 10/11/12 — no fill; EME was Aug 5 = prior week) → **1/5 after LLY** (BULL/NORMAL).
- **1 QUALIFIED (LLY).** Deep-research a–i completed for LLY, PLTR, TWLO.
- **WATCH — NOT planned (extended / chase-the-top per give-back lessons):**
  - **PLTR (IT, in univ)** — score ~6.5/10 raw: strong signal (adj EPS $0.41 vs $0.35 = +17% > 15% IT bar; rev +93% YoY; US-comm +149%; largest-ever FY guide raise to ~$8.15B; **9-qtr beat streak**) BUT **entry timing poor: price $171.09 = +16% above 21d EMA $146.93, mid-fade** (topped Aug 11 $174.94, −3.3% Aug 12); **52-wk high 193 sessions ago (Nov 2025), −17.5% below → recovery rally NOT fresh breakout (step-d downrank)**; ~54x fwd sales + Jefferies Underperform $80. Chasing +16%-over-EMA mid-fade invites the give-back the lessons warn against → WATCH; re-eval on consolidation toward EMA.
  - **TWLO (IT mid, in univ)** — qualifies on **guidance-prong** (EPS $1.47 vs $1.34 = +11% BELOW 15% bar → catalyst-exempt via FY26 rev-growth guide RAISED 14–15%→18–18.5%); gap +22.5%, vol 4.03x, PT raises 0 downgrades, fresh 52-wk high Aug 11. BUT **price $246.56 = +15.7% above 21d EMA $213.10 (parabolic), mid-fade** (topped Aug 11 $255.82, −3.6%); drift only +2.15pp RS since reaction (mostly the gap); thin $27M ADV. Same chase-the-top setup dropped Aug 11 → WATCH; re-eval on consolidation.
- **DAY-0 / NOT-YET-MEASURABLE (watch next session):**
  - **SMCI (IT, in univ)** — reported **Aug 12 AC**: non-GAAP EPS $1.70 vs ~$0.70 = ~+139% surprise; **FY2027 rev guide $65–72B vs ~$53B consensus (~+27% above)**; +7% AH / indic. +17–19% Aug 13. BUT (a) **day-0 — no measurable post-earnings drift/RS yet** → incomplete a–i = auto-DQ today (FTNT/PLTR day-0 precedent); (b) **revenue MISS $11.12B vs ~$11.73B**; (c) **material governance risk** (EY resignation Oct 2024, BDO adverse ICFR opinion, delinquent 10-K); (d) **material BIS/export-control risk** — co-founder + 2 others arrested Mar 2026 for smuggling Nvidia servers to China. Speculative special situation, NOT a clean PEAD entry → watch only, do not plan.
- **Watchlist:** **TEAM (Atlassian, IT, pending_review)** — Q4 FY26 (Aug 6) beat-and-raise, **adj EPS $1.87 vs $1.50 = +24.7%**, rev +28% YoY, RPO +44%, +31–35% pop HELD through Aug 12 (~$152) = cleanest textbook PEAD in window — BUT it is **pending_review (human-only to activate) → MUST NOT plan**; FY27 guide decelerates to ~13% rev growth (caveat already noted in watchlist). MRVL active (reports ~late Aug, no in-window catalyst → no plan). WDFC/THC/CLS/BE/FORM/PAYC pending_review (human-only). **No new watchlist adds** (ATRO/Astronics +12.8% raised-guide small-cap is below the standout catalyst bar and not in univ — logged only, per CNMD/CRL precedent).
- **Regulatory scan (planned candidate):** LLY shelf CLEAN, BIS N/A → **NO flags.**
- **Earnings re-verify (step 4):** LLY next report ~Oct 29 — not within 3 days ✓.
- **Halt/tradable (4b):** LLY active/tradable NYSE per `/v2/assets`, no halt news ✓.
- **Sanity (step 6):** post-LLY-fill cash ~78% >> 10% floor ✓; 2/8 concurrent ✓; 1/5 weekly (BULL/NORMAL) ✓; sectors Health Care (LLY) 11.2% / Industrials (EME) 11.0% both < 30% ✓; sizing 11.2% < 20% cap ✓.
- **market_open note:** LLY has been deferred 4 consecutive sessions on the intraday breakout gate (Aug 7 6d, Aug 10 6d, Aug 11 6e, Aug 12 6e) — thesis fully intact and drift accelerating; re-planned again. market_open applies its own Gate-4 EMA / Gate-6 ORB-confirmation logic at the open.
- DRY_RUN: **false**.
