# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-14 (pre_market ~08:55 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,245 | $1,112 (≈ fill × 0.92; market_open sets −8% off actual fill) | **Eli Lilly — Health Care — score 8/10 — TOP PICK (6th trading day as top pick; deferred by market_open Gate-6 Aug 7/10/11/12/13, never filled — re-planned).** Q2 2026 reported **Aug 5 BMO**: **revenue $22.97B +48% YoY = +11.4% beat** (Mounjaro $9.9B +91%, Zepbound $4.9B +46%); adj EPS $8.38 NOISY (incl. ~$3.03/sh IPR&D charge → ex-IPR&D operational beat >15%, clean ~+27%) → qualifies on **operational EPS beat + analyst-revision/catalyst-exempt basis** (strategy.md exempts catalyst entries from the 15% threshold; Health Care standard bar anyway). **FY26 revenue guide RAISED to $85–87B.** Earnings **streak 4 quarters** (+1 score). **Earnings-day gap +6.15%** (normal 5–10% band). **Reaction-day volume 2.18x** 20-day avg (strong institutional confirmation). **52-week high $1,248.53 on 2026-07-07 = 27 td ago (top-priority <45d band), only −3.2% below.** **RS vs SPY:** since earnings Aug 5→13 LLY +3.40% vs SPY +1.05% = **+2.35pp**; trailing-5d Aug 7→13 +1.95% vs +0.61% = **+1.34pp** (drift INTACT, price **+2.02% above 21d EMA $1,185.17**). **Sector ETF XLV 20d +4.05% vs SPY +3.59% = +0.46pp** (positive momentum). **Analyst: 5+ post-print PT raises, 0 downgrades** (MS $1,419 OW / Cantor $1,410 OW / BMO $1,400 OP / JPM $1,400 OW top-pick / Truist $1,376 Buy; Truist reiterated Buy Aug 13); Street ~22 buy / 2 sell. **Short interest ~1%** (neutral). **Insider:** routine 10b5-1 sells, no buying (neutral). CEO Ricks: *"Lilly's momentum continues… we delivered 48% revenue growth and raised our full-year guidance."* **TOP RISK:** ~45x P/E + orforglipron/Foundayo launch softness + Novo oral-GLP-1 competition + MFN/TrumpRx drug-pricing overhang — none a 42-day binary (core incretin franchise drove the raise; −8% stop protects). **Regulatory: shelf-reg CLEAN** (no S-3/equity offering — mega-cap; only non-dilutive debt May 2026), **BIS N/A** (pharma). ⚠️ **LLY trades EX-DIVIDEND today (Aug 14, $1.73/sh)** — the open is mechanically ~$1.73 lower; do NOT misread as weakness. Next earnings ~Oct 29 (not within 3d ✓); active/tradable NYSE ✓. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME (13 @ $834.12, +0.42% at $837.61) — no exit criterion fired (not −8% stop, not +10% trigger, thesis intact, held 9d < 60d). Hard stop 96e4e855 @ $767.39 GTC active. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME +0.42% far below +10% partial-profit-lock/trail trigger — no conversion. |

## Notes

- **Regime & posture:** SPY **BULL** (Aug 13 IEX close $777.84 > 200MA $704.97, n=200, **+10.34%**) → standard thresholds, max 5 new/week. **PEAD health STALE** (pead_health.md computed 2026-08-02, expires 2026-08-09 < today) → treated **NORMAL flagged STALE** per pre_market step 1c; bar NOT raised (universe-cache freshness is the hard halt and it PASSES). Last fresh reading was NORMAL (realized_health_60d +2.008%, n=269). **This is the 4th consecutive week the Sunday universe_refresh updated universe.md but NOT pead_health.md — surfaced for human.**
- **Macro-deferral NOT triggered:** premarket S&P futures **+0.06% (UP)** → "futures down >0.4%" leg FAILS; 10-yr **~4.65%**, pulled back from the ~4.75% Aug-11 19-month high → NOT a fresh multi-month high → "multi-month high" leg FAILS. Both legs required → standard 15% bars (20% for Utilities/RE/Industrials/Energy). Session risk today: **July Retail Sales 08:30 ET**, UMich sentiment 10:00 ET.
- **Gates:** clock is_open=false, next_open=2026-08-14T09:30 ET → opens today (Fri), not a holiday → proceed. **Reconciliation 1/1 PASS:** Alpaca /v2/positions = EME 13 @ $834.12 matches portfolio.md exactly (stop 96e4e855 @ $767.39 GTC); zero divergence. Account ACTIVE, trading_blocked=false, equity **$98,312.34**, cash $87,423.41 (88.9%), 1/8 concurrent. **Universe FRESH** (screened 2026-08-09, expires 2026-08-16, 302 rows) → freshness gate PASSES.
- **Weekly slots:** week of Mon Aug 10 — actual fills this week **0** (LLY deferred by market_open Gate-6 Aug 10/11/12/13, no fill) → **1/5 after LLY**.
- **Shortlist result: 1 QUALIFIED (LLY 8/10, sole qualifier).** Fewer than 3 qualified → plan fewer, do NOT lower the bar (strategy.md).
- **DROPS:** **SMCI** (IT, in univ) — reported Aug 11, non-GAAP EPS ~+75–100% surprise BUT **revenue MISS (~$11.12B, ~$610M light)** + **material governance risk** (EY resignation Oct 2024, BDO adverse ICFR opinion, delinquent 10-K) + **material BIS/export-control risk** (co-founder + 2 arrested Mar 2026 for smuggling Nvidia servers to China) → **step-h regulatory scan = automatic DROP** regardless of score. **AMAT** (IT, in univ) — Q3 Aug 13 EPS $3.50 vs $3.40 = **+2.9% surprise < 15% IT bar** → drop. **CAVA** (not in univ) — EPS +5.5% < bar. **PLTR/TWLO** (in univ) — remain WATCH per Aug 13 (extended, +14–16% over EMA, mid-fade — chase-the-top give-back risk).
- **Regulatory flags among PLANNED:** NONE (LLY shelf CLEAN / BIS N/A).
- **Watchlist:** **NET (Cloudflare) ADDED pending_review** (compelling non-universe catalyst — Q2 reported Aug 6: EPS beat ~+38%, rev $696.1M +36% YoY, **RAISED FY26 guide to $2.864–2.870B rev / $1.25–1.26 EPS**; +17.4% AH then continued to a **fresh 52-wk high $332.13 on Aug 13**, drift +13% since report, price +14.65% over 21d EMA — textbook clean guidance-raise PEAD; Cloudflare is an S&P 500 name ABSENT from the cache, likely a screen-source gap like PAYC; human-only to set active). MRVL active (no in-window catalyst, reports ~late Aug → no plan). WDFC/THC/CLS/BE/EME/FORM/PAYC/TEAM pending_review (human-only, MUST NOT plan). EME already held via prior fill.
- **Sanity (step 6):** post-fill cash ~77.9% >> 10% floor ✓; 2/8 concurrent ≤ 8 ✓; 1/5 weekly (BULL/NORMAL) ≤ 5 ✓; sectors Health Care (LLY) 11.1% / Industrials (EME) 11.1% both < 30% cap ✓; sizing 11.07% < 20% cap ✓.
- DRY_RUN: false.
