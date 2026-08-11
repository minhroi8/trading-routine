# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-11 (pre_market ~08:30 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,262 | $1,132.43 (−8% off ~$1,231 ref; market_open sets exact off fill = fill×0.92) | **Eli Lilly — Health Care (in universe) — score 8/10 — TOP PICK (only qualifier).** Q2 2026 reported **Aug 5 BMO**: **revenue $22.97B +48% YoY = +11% beat** vs ~$20.7B est (Mounjaro $9.94B +91%, Zepbound $4.93B); headline adj EPS $8.38 vs ~$6.01 is NOISY (incl. ~$3.03/sh IPR&D charge → ex-IPR&D operational beat far exceeds 15%) → qualifies on **analyst-revision/catalyst-exempt basis + operational EPS beat >15%**. **FY26 revenue guide RAISED to $85–87B.** **Earnings streak: 4 consecutive quarters beating** (+1 signal). **Earnings-day gap +6.15%** (Aug4 $1,117.47→Aug5 open ~$1,186; normal, no adj). **Reaction-day volume 2.18x** 20-day avg (strong institutional confirmation). **52-week high $1,248.53 on 2026-07-07 = 24 td ago (top-priority <45d band), only −1.4% below hi.** **Relative strength since earnings +4.85pp** (LLY Aug5 $1,169.29→Aug10 $1,230.90 = +5.27% vs SPY +0.42%; drift INTACT and ACCELERATING — LLY made a fresh post-earnings high Aug 10; price ABOVE 21d EMA $1,175.67 by +4.70%). **Sector ETF XLV +1.20pp vs SPY 20d** (positive sector momentum). **Analyst conviction: 4+ post-print PT raises, 0 downgrades** (Truist $1,376 Buy, Cantor raise, MS $1,419 OW, BMO $1,400 OP; Leerink UPGRADE→Outperform; CNBC/Cramer raising PT on "another beat-and-raise quarter"). Short interest ~1% (neutral); insider n/a (mega-cap). Mgmt (Ricks): outlook *"has never been brighter."* **TOP RISK: orforglipron/Foundayo launch softness + Novo competition + ~45x P/E + drug-price policy — none a 42-day binary (core GLP-1 franchise, not Foundayo, drove the raise); −8% stop protects.** **Regulatory scan: shelf-reg CLEAN** (no S-3/offering — mega-cap, no dilution); **BIS N/A** (pharma). Next earnings ~Oct 29 (not within 3d ✓); active/tradable NYSE ✓. NOTE: LLY was planned Aug 10 and DEFERRED by market_open on the Gate-6d chaotic-open guard (execution, not fundamentals) — re-planned today with the drift thesis re-verified and strengthening. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME HOLD — no exit criterion fired. Current $809.33 vs cost $834.12 (−2.97%), hard stop 96e4e855 @ $767.39 GTC active (cushion ~5.2%); not −8%; not +10% trigger; thesis intact (Q2 blowout +25.31% surprise, raised FY26 guide, record RPO backlog $17.1B — no negative catalyst); held 6 days (not 60-day-stale). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — | EME −2.97% is far below the +10% trailing trigger — no conversion. |

## Notes

- **Gates:** clock `is_open=false`, `next_open=2026-08-11T09:30 ET` → opens today (Tue), NOT a holiday → proceed. **RECONCILIATION 1/1 PASS:** Alpaca `/v2/positions` = EME 13 @ $834.12 MATCHES portfolio.md exactly (hard stop 96e4e855 @ $767.39 GTC); zero divergence. Account ACTIVE, trading_blocked=false; equity **$97,944.70**, cash $87,423.41 (89.3%), EME mv $10,521.29 (−2.97%), 1/8 concurrent.
- **Universe FRESH:** screened 2026-08-09, expires 2026-08-16 (302 rows) → freshness gate PASSES.
- **PEAD health STALE:** computed 2026-08-02, expires 2026-08-09 < today → treated **NORMAL but flagged STALE** per step 1c; **bar NOT raised** (universe-cache gate is the hard halt and PASSES). Last fresh reading NORMAL (realized_health_60d +2.008%, n=269). NB the Sunday Aug 9 universe_refresh updated `universe.md` but did NOT refresh `pead_health.md` — surfaced for human (2nd consecutive week stale).
- **SPY regime BULL:** Aug 10 IEX close $773.02 > 200MA $703.45 (n=200 of 257 bars, +9.9%) → standard 15% EPS bars, max 5 new/week.
- **Macro-deferral NOT triggered:** premarket S&P futures **UP ~+0.07%** → "futures down >0.4%" leg FAILS; 10-yr ~4.73% IS elevated (near highest since Jan, oil/Iran-driven) but both legs are required → standard bars. Context: CPI Wed Aug 12, PPI Thu Aug 13; Fed Sept-hike odds ~51%.
- **Thresholds in effect this session:** standard `strategy.md` — 15% EPS surprise (20% for Utilities/Real Estate/Industrials/Energy; Industrials & Energy also need streak ≥2), max 5 new/week, sizing ≤20% cap (target ~11%), cash floor ≥10%, sector cap ≤30%, max concurrent ≤8.
- **Weekly slots:** week of Mon Aug 10. Actual fills this week: 0 (Aug 10 LLY was DEFERRED by market_open, no fill). → 1/5 after LLY.
- **TWLO (IT mid, in universe) — SCORED ~7.5/10 raw but LOGGED AS STRONG WATCH, NOT PLANNED:** Q2 2026 (reported Aug 6 AC) rev $1.50B (+4.9% beat), non-GAAP EPS $1.47 vs $1.32 = **+11.4% surprise (BELOW the 15% IT bar → catalyst-exempt guide-raise basis only)**; FY26 guide RAISED 14–15%→18–18.5% reported rev growth; reaction-day vol **4.03x**, gap +25% (Aug6 $193.29→Aug7 $241.56), fresh 52-wk high Aug 10 (0 td), RS +3.61pp, PT raises BTIG $285/Needham $280 (0 downgrades). **DROP-to-WATCH rationale: price $250.25 is +21.8% ABOVE its 21d EMA ($205.42) — parabolic/extended, the SAME chase-the-top setup this system dropped on PLTR Aug 10 (+24.6% over EMA, "strong-momentum WATCH, not planned per give-back lessons"). Entering a name +25% gapped & +21.8% over trend on a below-standard-EPS catalyst-exempt basis puts the −8% stop ~18% below and invites a mean-reversion give-back.** Re-evaluate if it consolidates back toward its EMA. No watchlist action (already in universe).
- **DROPS:** **CAT** (Industrials) — drift BROKEN, price $837.58 BELOW 21d EMA $869.18 (−3.64%), gap fully faded (Aug4 $877.09→Aug10 $837.58), RS −4.75pp since earnings; market_open would defer on the EMA gate anyway → drop (3rd consecutive CAT EMA/drift failure). **ABNB** (Cons Disc) — EPS $1.37 vs $1.25 = +9.6% surprise < 15% bar, no exemption basis, muted +7% reaction → drop. **FOXA/FOX** (Comm Services) — +28.8% EPS surprise but NOT in universe/watchlist AND muted +5.5% media reaction (weak PEAD) → log only, no watchlist add.
- **Watchlist flag:** **TEAM (Atlassian)** added to `watchlist.md` as `status: pending_review` (compelling non-universe catalyst — Q4 FY26 Aug 6: rev $1.766B +28% YoY, cloud +31%, GAAP profitability returned, ARR $6.6B +23%, RPO +44%, stock +29%). Caveat noted in the row: **FY2027 guide DECELERATES to ~13% rev growth (vs +26% FY26)** — the pop was Q4-beat + AI-momentum + profitability-turn driven; human must confirm index/liquidity/price gates AND weigh the growth deceleration before setting `active`. MUST NOT plan a trade until human sets `active`.
- Existing watchlist: **MRVL active** (no in-window earnings catalyst — reports ~late Aug; no plan); WDFC/THC/CLS/BE/FORM/PAYC pending_review (human-only, MUST NOT plan).
- **Earnings re-verify (step 4):** LLY reported Aug 5, next ~Oct 29 — not within 3d ✓.
- **Halt/tradable (step 4b):** LLY active/tradable NYSE per /v2/assets, no halt news ✓.
- **Sanity-check (step 6):** post-fill cash ~78% >> 10% floor ✓; 2/8 concurrent ✓; 1/5 weekly (BULL/NORMAL) ✓; sectors Health Care (LLY) 11.3% / Industrials (EME) 10.7% both < 30% cap ✓; sizing 11.31% < 20% cap ✓. Regulatory flags among planned: **NONE**.
- DRY_RUN: false.
