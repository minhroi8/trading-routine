# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-10 (pre_market ~08:30 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,215 | $1,117.80 | **Eli Lilly — Health Care — score 8/10 (TOP PICK).** Q2 2026 reported **Aug 5 BMO**: **rev $22.97B +48% YoY = +9.75% beat** vs $20.93B est (Mounjaro $9.94B +91%, Zepbound $4.93B); headline adj EPS $8.38 vs ~$6.07 = +38% but **noisy (incl. ~$3.03/sh IPR&D charge; ex-IPR&D operational beat far larger)** → qualifies on **analyst-revision/catalyst-exempt basis** AND operational EPS beat >15%. **FY26 revenue guide RAISED to $85–87B** (from $82–85B). **Earnings streak: 4 consecutive beats** (Q2'25→Q2'26; +1). **Earnings-day gap +6.15%** (Aug4 $1,117.47→Aug5 open $1,186.24; normal, no adj). **Reaction-day volume ~2.05x** 20d avg (strong institutional confirmation). **52-wk high $1,248.53 on 2026-07-07 = 23 td ago (top-priority <45d band), only −5.0% below hi.** **RS vs SPY +0.99pp** post-reaction (Aug5 $1,169.29→Aug7 $1,185.96 +1.43% vs SPY +0.44% — drift INTACT, price ABOVE 21d EMA $1,172.05 by +1.2%). **Sector ETF XLV +0.56pp vs SPY (20d, positive momentum, no penalty).** **Analyst: 4+ post-print PT RAISES, 0 downgrades** (MS $1,419 OW / BMO $1,400 OP / Truist $1,376 Buy / Wells $1,330 OW). **Short interest ~1% float (neutral).** **Insider: none notable (mega-cap, n/a).** Mgmt (CEO David Ricks) characterized outlook as **"…never been brighter"** (beat-and-raise). **TOP RISK: Foundayo/orforglipron launch softness (weekly scripts stalled ~5 wks; Goldman cut 2026 US est $1.1B→$755M) + Novo competition/lawsuit + ~45x P/E + US drug-price policy — none a 42-day binary thesis-breaker (core Mounjaro/Zepbound franchise, not Foundayo, drives the raise); −8% stop protects.** **Regulatory scan: shelf-reg CLEAN (mega-cap FCF, no dilution risk); BIS N/A (pharma).** Next earnings ~late Oct/Nov (not within 3d ✓). Active/tradable NYSE ✓. Sized 9 sh × ~$1,193 ≈ $10,737 = **~10.9%** of $98,242.92 equity (< 20% cap; routine "(currently 11%)" convention). Stop = limit $1,215 × 0.92 = $1,117.80 (−8%). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME held (opened Aug 5, −0.22% vs cost): thesis intact (record Q2 rev $5.15B +19.8%, RAISED FY26 guide, record RPO backlog $17.1B / data-center RPO +112% YoY, fresh PTs Oppenheimer $1,200 / UBS $1,065); no exit criterion fired (not −8% hard stop, not +10% trail, not 60d-stale). Hard stop 96e4e855 @ $767.39 handles downside. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME +... below +10% trigger (−0.22%); no conversion. |

## Notes

- **Gates (all PASS):** Gate 1 clock — is_open=false at 08:25 ET, **next_open 2026-08-10T09:30 ET → opens today (Mon), NOT a holiday** → proceed. Gate 2 **RECONCILIATION 1/1 PASS** — Alpaca /v2/positions = EME 13 @ $834.12 MATCHES portfolio.md exactly (hard stop 96e4e855 @ $767.39 GTC active in /v2/orders); zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity **$98,242.92**, cash $87,423.41 (89.0%), 1/8 concurrent. Gate 3 **Universe FRESH** (screened 2026-08-09, expires 2026-08-16, 302 rows) → freshness gate PASSES (trading allowed).
- **PEAD health STALE:** pead_health.md computed_on 2026-08-02, **expires 2026-08-09 < today 2026-08-10** → treated **NORMAL but flagged STALE** per step 1c — bar NOT raised (the universe-cache freshness gate is the hard halt and it PASSES; realized-health leg fails-open on stale overlay). Last fresh reading NORMAL (realized_health_60d +2.008%, n=269, health_ok=true). Note: Sunday Aug 9 universe_refresh updated universe.md but pead_health.md still carries the Aug 2 stamp — surfaced for human/next refresh.
- **Regime BULL:** SPY Aug 7 IEX close **$773.16 > 200MA $702.94 (+10.0%)**, n=200 → standard thresholds, max **5** new/week (no bear-regime bar-raise, no ELEVATED_BAR cap).
- **Macro-deferral NOT triggered:** premarket S&P futures **UP ~+0.1% to +0.6%** → "futures down >0.4%" leg FAILS; 10-yr **~4.65% steady/drifting DOWN** week-over-week (softer July jobs: −23k payrolls; Sept hike odds 67%→44%) → NOT a fresh multi-month high. Both legs required → standard 15% bars apply.
- **Weekly new-position slots:** new week (Mon Aug 10); last actual fill EME Aug 5 (prior week, week of Aug 3) → **0/5 used this week** → 1/5 after LLY plan (BULL/NORMAL cap 5).
- **DROPPED candidates (drift/EMA legs failed — step f/Gate-4):** **CAT** (Industrials) — post-earnings drift BROKEN, price $842.34 **BELOW 21d EMA $872.50 (−3.5%)**, gap fully faded (Aug4 $877.09→Aug7 $842.34, RS −4.23pp); market_open would defer on Gate 4 anyway → drop. **AMZN** (Cons Disc) — **RS −5.47pp** (topped Aug3 $284.12→Aug7 $274.37; 4 consecutive Gate-6 defers), drift reversed → drop per step f. **FTNT** (IT) — faded from 52wk-hi Aug5 $168.27 to $159.58 (−5.2%, RS −0.77pp), beat-got-sold, Piper downgrade + CEO selling → drop. **PLTR** (IT) — RS **+5.51pp** positive (huge +10% Aug7 pop) BUT price **+24.6% over 21d EMA** (parabolic/extended), 52wk-hi 190 td ago (−17%, step-d downrank), ~45–48x fwd sales valuation + relentless insider selling, XLK −1.26pp → too extended to initiate a new position (chase-the-top risk per give-back lessons); logged as strong-momentum watch, NOT planned. "Plan fewer, don't lower the bar."
- **Sanity check (step 6):** post-fill cash ≈ $76,533 = **~78% >> 10% floor** ✓; concurrent **2/8** ≤ 8 ✓; weekly **1/5** ≤ 5 (BULL/NORMAL) ✓; sectors Health Care (LLY) ~10.9% / Industrials (EME) ~11.0% — both **< 30% cap** ✓. Regulatory flags among planned: **NONE** (LLY shelf clean, BIS N/A).
- **Regulatory scan results:** LLY — shelf-reg CLEAN, BIS N/A. (No planned candidate flagged.)
- **Watchlist:** MRVL active — no in-window earnings catalyst (reports ~late Aug; Aug 4 +12.7% was sector/sympathy, not a company print) → no plan; status stays active (human-only). WDFC/THC/CLS/BE/FORM/PAYC pending_review — human-only to set active, MUST NOT plan. **No new watchlist adds** (no compelling non-universe catalyst surfaced in the overnight/weekend sweep).
- **Overnight/weekend sweep:** market cautious-positive near record highs (tech/energy leading, staples/real-estate lagging); CPI Wed Aug 13; Strait-of-Hormuz/Iran headlines + oil +1.3%. Aug 10 reporters (RKLB/HIMS/FERG/PLUG/SMCI) report AMC or are not clean universe PEAD setups → no action. No adverse news on EME or LLY.
- DRY_RUN: **false**. This routine places NO orders (pre_market drafts only); market_open executes.
</content>
</invoke>
