# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-18 (pre_market, ~07:18 ET, Wed)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $960.00 | $883.20 | **Score 7/10 (Health Care, in-universe).** Q3 2026 (Oct-30 BMO) non-GAAP EPS **$20.07 vs ~$16.25 cons = +23.5% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR all-sector bar; revenue **$5.12B +36% YoY** (beat ~$4.60B). **Earnings streak 3+ quarters** (+1). **Earnings-day gap +6.29% overnight** (full-day +13.5%; normal). **Volume ratio ~5.69× 20-day avg** on the Oct-30 print (strong institutional confirmation). **52-week high $988.48 on 2026-11-04 = ~9 trading days ago (TOP priority <45d)**; Nov-17 close $957.75 = −3.1% below ATH. **Relative strength +6.90pp 5-day** (REGN +4.56% $915.94→$957.75 vs SPY −2.34% $749.93→$732.41) — strong outperformance on a sharp risk-off week. **Sector ETF XLV +3.05% vs SPY −4.77% 20-day = +7.82pp** (Health Care leading, rotation IN → tailwind, no penalty). **~10 post-Q3 PT raises / 0 downgrades** (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980). **Short interest <2%** (neutral); insider neutral. Mgmt call: *"an outstanding quarter … one of our strongest years ever."* **Top risk:** EYLEA biosimilar / Kodiak competition (EYLEA ~31% of rev, priced; Q3 beat came despite EYLEA softness, Dupixent-driven) + **cemdisiran gMG FDA PDUFA target date in November 2026** (a binary regulatory event that may land inside the holding window — but upside-biased: Phase 3 positive, priority review, PRV used; cemdisiran is a secondary pipeline asset, a CRL would not break the core thesis) + near-ATH extension. None thesis-breaking within 42d. **Regulatory scan: shelf-reg CLEAN** (routine 2024 WKSI auto-S-3, no 2026 offering, ~103M shares stable, runs buybacks); **BIS N/A** (Health Care). Asset active/tradable (NASDAQ); next earnings Q4 ~late-Jan/Feb 2027 (>3d). Sized 19sh @ $960 limit = $18,240 ≈ 19.2% of equity (20% cap = $18,989; 20sh = 20.2% > cap), stop $883.20 (= limit × 0.92). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) since VRT −8% hard-stop exit 2026-11-02. No positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Book FLAT (0/8, 100% cash), equity $94,946.98** (cash $94,946.98, buying_power $379,787.92). Book unchanged since VRT −8% hard-stop exit 2026-11-02.
- **Gates:** /v2/clock is_open=false (pre-mkt, 07:18 ET), **next_open 2026-11-18T09:30 ET = TODAY, not a holiday → proceed.** **RECONCILIATION 0/0 PASS** — Alpaca /v2/positions=[] MATCHES portfolio.md FLAT (the VRT row is inside an HTML comment, closed −8% 11-02, NOT a live row); /v2/orders?status=open=[] (no orphan stops); account ACTIVE, trading_blocked=false, account_blocked=false.
- **Universe FRESH** (331 rows, screened 2026-11-15, expires 2026-11-22) → consumed read-only, NO re-screen.
- **PEAD posture ELEVATED_BAR + FRESH** (computed 2026-11-15, expires 2026-11-22; **realized_health_60d_pct −0.358%, health_sample_n=163, health_ok=false**) → for THIS session: **EPS-surprise bar raised to >20% for ALL sectors + max new positions capped at 2.** The drift edge is not currently paying — defensive overlay; governs NEW entries only, never exits. Overlay only tightens, never loosens.
- **Regime: BULL but RAZOR-THIN** — SPY last close **$732.41 (Nov-17) vs 200-day MA $732.32 = +0.01% above** (recomputed from IEX bars, n=247). SPY sold off sharply this week ($759.80 Nov-11 → $732.41 Nov-17, −3.6%) and now sits essentially ON its 200MA — one more down day flips to bear regime. Bear-rule inactive this session (SPY still > 200MA); ELEVATED_BAR cap(2) binds regardless. Macro-deferral MOOT (>20% bar already enforced by ELEVATED_BAR).
- **Weekly new buys: 0/2** under the ELEVATED_BAR cap (last actual fill was VRT buy 10-29, stopped −8% 11-02; REGN has been planned but NOT executed every session since). After REGN fills → 1/2.
- **REGN execution caveat for market_open:** REGN has now been planned on **8 consecutive sessions (Nov 3/5/6/12/13/16/17 + today) and executed NONE of them** — market_open's opening-range / 21-day-EMA / chase-guard gates rejected each one as extended near its 52-week high. Limit $960 is just above the Nov-17 close ($957.75) and below the 52-wk high ($988.48). **DO NOT chase above the limit.** Apply the opening-range confirmation and chase-guard gates strictly; if REGN prints below its opening-range high at the 09:50 check, defer again (do NOT drop — pre_market re-evaluates tomorrow). On a market sitting right on its 200MA, let the gates do their job.
- **Sanity checks vs strategy.md:** cash floor post-fill ~80.8% ≥ 10% ✓; max concurrent 0→1/8 ≤ 8 ✓; max new/week 0→1/2 under ELEVATED_BAR cap ✓; Health Care sector 19.2% < 30% ✓; sizing 19.2% < 20% cap ✓ (routine prompt's "(currently 11%)" parenthetical is STALE — strategy.md's `Max position size at entry` = 20% field wins per CLAUDE.md; VRT precedent 10-29 = 77×$243.32 ≈ 19.4% confirms 20% is operative).
- **NVDA DROPPED:** Q3 FY2027 (Nov-17 AMC) revenue $115.8B +103% YoY (~6% beat), Q4 guide $130B ±3% — strong beat-and-raise, BUT non-GAAP EPS $2.68 vs ~$2.48 = **+8.1% surprise ≪ >20% ELEVATED_BAR bar** → DROP on threshold (also IT/semiconductor → BIS risk, and just reported Nov-17 so inside the data-digestion window). A guidance-driven move, not a >20% EPS surprise.
- **Other screens / non-universe observed, NOT added** (sibling-restraint; pending_review backlog ~28 names unactioned): MDB (MongoDB EPS crush, ~+15% AH — but report-date unverified/possibly stale, not in universe cache); PSTG (Pure Storage beat+raise but FELL ~12% AH → NEGATIVE reaction, not a clean PEAD); NXT (Nextpower +8.6%, non-universe). None a compelling clean in-window >20% PEAD setup → no new watchlist adds.
- **Watchlist:** only MRVL is `status: active` — thesis BROKEN (Nov-2 $115B all-stock Lumentum acquisition, −12.7% day/−29.6% week, TD Cowen Buy→Hold PT $350→$175 on dilution); next earnings ~Nov-26 (outside 3d), last report ~late-Aug (~80d, outside 30d) → no in-window positive catalyst → NOT plannable. All other watchlist rows are `pending_review` (human-only to set `active`). No new WL adds.
- **Regulatory flags:** none on the planned name (REGN shelf-reg clean, BIS N/A).
- **Watchlist flags:** none.
- **Carry-forward (human):** portfolio.md ~473KB bloat (human-trim needed — exceeds single-read limit); trade_log VRT buy+sell commit_sha `<pending>` (human backfill); sizing-doc "(11%)" vs strategy.md 20% (strategy.md wins). Log rotation DEFERRED to market_close (pre_market appends only).
- **DRY_RUN: false.**
