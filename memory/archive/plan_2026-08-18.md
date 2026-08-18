# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-18 (pre_market ~08:20 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| PWR | 15 | $745.00 | $685.40 | **Quanta Services — Industrials — Score 9/10.** Q2 2026 (reported Jul 30) adj diluted EPS **$4.24 vs $3.29 consensus = +28.9% surprise** (clears strict Industrials **>20% AND streak≥2** gate) ; revenue **$9.56B vs $8.53B = +12.1% beat** (+41% YoY); **RAISED FY26 guide** (rev $39.3–39.7B, adj EPS $16.45–16.95, FCF $2.0–2.5B); **record total backlog $53.4B** (RPO $33.6B). Earnings streak **3 consecutive beats** (Q4'25 +7.8%, Q1'26 +12.6%, Q2'26 +28.9%). Earnings-day gap **+16.26%** (prior close $560.92 → open $652.11; close +17.29%). Volume **3.23x** 20-day avg on announcement day (strong institutional confirmation). 52-wk high **104 days ago** ($788.75 on May 6 — downranked; post-earnings pop still ~8% below the May high, NOT a new-high breakout). RS vs SPY **+9.31%** (5-day spread; PWR +9.26% vs SPY −0.05%). Sector ETF XLI vs SPY **+0.47%** (20-day; sector slightly leading, no penalty). Analyst upgrades **2, downgrades 0** (KeyBanc→Overweight PT $807 Aug 7; Guggenheim→Buy Jul 31; Street avg PT ~$770–783, Buy consensus). Short interest **~2.11%** (low, no squeeze). Insider: **mild net selling** (CAO Nobel sold 4,000 @ $756.98; minor RSU vesting). Mgmt quote (CEO Duke Austin): *"Revenue, adjusted EBITDA and adjusted diluted earnings per share all achieved strong double-digit growth."* Top risk: **rich valuation (~75x P/E vs industry ~40x)** — downside if growth/backlog momentum cools; secondary data-center permitting / project-lumpiness risk (none thesis-breaking within 42d). Regulatory scan: **shelf-reg CLEAN** (Aug 2026 S-3 was senior *notes*/debt, no equity dilution); **BIS N/A** (Industrials). Next earnings ~Oct 29 (not within 3d); not halted, tradable. Same secular data-center/grid/electrification tailwind as our EME position. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME held (only open position, +2.4%, no exit criterion fired — not −8% hard stop, not +10% trail, thesis intact, held 13d not 60d-stale). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME +2.4%, far below +10% partial-profit-lock/trail trigger — no conversion. |

## Notes

- **Gates (all PASS):** Alpaca `/v2/clock` `next_open` = 2026-08-18 (today) → NOT a holiday, proceed. **Reconciliation 1/1 PASS** — Alpaca `/v2/positions` = EME 13 @ $834.12 MATCHES portfolio.md exactly; hard stop 96e4e855 @ $767.39 GTC active; zero divergence. Account ACTIVE, trading_blocked=false; equity $98,524.11, cash $87,423.41 (88.7%), 1/8 concurrent. **Universe FRESH** (screened 2026-08-16, expires 2026-08-23, 294 rows). **PEAD health FRESH & NORMAL** (computed 2026-08-16, expires 2026-08-23; realized_health_60d **+0.906%**, n=113, health_ok=true) → **standard 15% EPS bar, max 5 new/week — no ELEVATED_BAR**.
- **Regime BULL** (SPY $776.34 > 200MA $702.75, +10.5%) → standard sector thresholds (15%; 20%+streak≥2 for Industrials/Energy; 20% for Utilities/Real Estate).
- **Macro-deferral NOT triggered:** premarket S&P futures **−0.13%** (leg 1 "down >0.4%" FAILS); **10-yr yield ~4.297%, falling** (leg 2 "fresh multi-month high" FAILS) → standard bars, no >20% macro override.
- **1 QUALIFIED buy: PWR (9/10).** Deep-research a–i complete. Industrials strict gate MET.
- **4 candidates DROPPED after full a–i deep research:**
  - **SMCI (IT)** — DROP (risk-gate auto-disqualify): unremediated internal-control **material weakness >1yr**; **active S-3 shelf (Jun 9 2026) + completed ~$7B equity/convertible raise (Jun 2026) = DILUTION flag**; **DOJ Mar-2026 export-diversion indictment** of insiders. Also a revenue MISS (−3.9%) with margin-driven EPS beat analysts call "not sustainable." Any one flag drops it; all three → unambiguous drop.
  - **LLY (Health Care)** — DROP: fundamentals elite (+38.1% EPS surprise, +9.8% rev beat, raised guide, 4-qtr streak) but **PEAD drift DECAYED** — price pinned ON the 21D EMA (+0.02%), 52-wk high was **pre-earnings** (Jul 7) and never reclaimed, RS vs SPY **−3.67%**, no volume follow-through (next-day 0.84x). **8th look after 7 consecutive gate deferrals = DROP.** Revisit only on a fresh catalyst that puts price decisively above the 21D EMA with confirming volume.
  - **AMZN (Consumer Disc, catalyst/analyst-revision basis)** — DROP today: strong signal/confirmation (AWS +36.7% reaccel, +12.5% gap, 2.6x volume, 52-wk high 15d ago, wall of PT raises / 0 downgrades) but **drift is fading** — RS vs SPY **−5.98%** (5d), −9% off its Aug-3 high, sector ETF XLY lags SPY (−2.24% 20d). Per strategy step f (negative RS → drop/heavily downrank). Re-qualifies on price stabilization / RS reclaim.
  - **LITE (IT)** — DROP today: **EPS surprise +8.8% FAILS the IT >15% earnings bar** (earnings-driven entry, reported Aug 11). Drift is exceptional (+19% RS vs SPY, 2.05x volume, 8-qtr streak, huge guidance raise) but the entry is earnings-driven and does not clear the surprise gate; also extreme valuation (~150x P/E "priced for perfection", ~20% short interest, net insider selling). **Not lowering the bar** — watch as a strong momentum name; re-qualify if a future signal is analyst-revision/catalyst-driven or the EPS bar is cleared. (NB: universe cache LITE last_price $925.91 is one session stale = Aug-14 close; actual ~$968 Aug-17 — flag for next universe_refresh, not a data error.)
- **Watchlist:** MRVL (active) — no fresh ≤30d catalyst (next earnings Aug 27, 9d out); held, not shortlisted. No new `pending_review` additions (DAY +26% is a Thoma Bravo cash M&A buyout, not a PEAD catalyst and not in universe/watchlist → skipped).
- **Sanity checks:** cash floor 88.7% → ~77.7% post-PWR (>>10% ✓); max concurrent 1→2 ≤ 8 ✓; weekly new 0→1 ≤ 5 (BULL/NORMAL) ✓; sector Industrials EME 11.3% + PWR ~11.0% ≈ 22.4% < 30% cap ✓; PWR sizing 15 sh ≈ $10,831 @ close = 11.0% (11.3% @ limit $745) < 20% cap ✓.
- **⚠️ SIZING DISCREPANCY (human review):** `routines/pre_market.md` step 5 says size per strategy.md "Max position size at entry (currently **11%**)", but `strategy.md` now reads **20%**. Every recent entry (EME, CASY, LLY plans) used ~11% and market_open checks against a 20% cap. Sized PWR at ~11% (consistent precedent, within the 20% cap). Human should reconcile the routine annotation vs strategy.md value.
- DRY_RUN: false.
