# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-12 (Thu) — drafted by pre_market ~07:20 ET. DRY_RUN: false.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 10 | $965.00 | $887.80 | **Regeneron (Health Care) — score 9.5/10.** Q3 2026 (Oct-30 BMO) CLEAN beat: non-GAAP EPS **$20.07 vs ~$16.08 cons = +24.8% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR bar on a clean basis; revenue **$5.116B = +11–12% beat / +36% YoY** (Dupixent/EYLEA-HD/Libtayo records). **FRESH catalyst (the re-qualifier): positive Phase 3 registrational-cohort data for poze-cemdi (pozelimab + cemdisiran) in PNH, released ~Nov-10/11** → drove REGN **+4.77% on Nov-11** ($915.94→$959.67) on ~2.4× daily volume to near its 52-wk high; de-risks the C5 complement franchise. Earnings streak **3+ consecutive beats**. Earnings-day **gap +13.5%** (Oct-29 $817.17 → Oct-30). **Volume ratio 5.69×** 20-day avg on the Oct-30 print (203,641 vs 35,770). **52-wk high $974.59 on Nov-3 (9 days ago → TOP priority, <45d)**; current $959.67 (~1.5% off high). **RS vs SPY +2.75pp** 5-day (REGN +6.34% vs SPY +3.59%, Nov-5→11). **Sector ETF XLV +8.64% vs SPY −1.28% 20-day = +9.92pp** (Health Care leading — rotation INTO sector, PEAD-supportive). Analyst conviction: **~10 post-Q3 PT raises / 0 downgrades** (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980). Short interest **<2%** (neutral). Insider activity: none flagged (neutral). Mgmt quote (Q3 call): *"an outstanding quarter … one of our strongest years ever."* **Top risk:** legacy EYLEA biosimilar erosion (−41%, already priced in) + mild give-back/overbought after the run; cemdisiran gMG FDA decision due Nov-2026 is binary but upside-biased. **Regulatory scan — shelf-reg: CLEAN** (only a routine 2024 WKSI auto-shelf S-3ASR; no 2026 equity offering; shares outstanding stable ~103M); **BIS: N/A** (not a semiconductor/IT name). Asset active/tradable (Alpaca /v2/assets); next earnings Q4 ~early-Feb-2027 (>3d). Sized 10 sh @ $965 limit = **~10.16% of $94,946.98 equity** (≤11% doc / ≤20% strategy.md cap); stop $887.80 = entry × 0.92 (−8% hard stop, place immediately after fill). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash). No open positions → no exit criteria could fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates (all PASS):** `/v2/clock` is_open=false (pre-mkt ~07:19 ET), next_open **2026-11-12T09:30 ET → opens TODAY, not a holiday** → proceed. **RECONCILIATION 0/0 PASS:** Alpaca /v2/positions=[] MATCHES portfolio.md FLAT (the VRT row is inside an HTML comment — VRT closed −8% hard stop 2026-11-02); /v2/orders?status=open=[] (no orphan stops). Account ACTIVE, trading_blocked=false, account_blocked=false, equity **$94,946.98**, cash $94,946.98 (100%), long_mv $0, buying_power $379,787.92, balance_asof 2026-11-11.
- **Universe FRESH** — 347 rows, screened 2026-11-08, expires 2026-11-15 → no re-screen (universe_refresh owns screening).
- **PEAD posture ELEVATED_BAR + FRESH** (computed 2026-11-08, expires 2026-11-15; **realized_health_60d_pct −0.951%, health_sample_n 260**, health_ok=false) → **EPS-surprise bar raised to >20% for ALL sectors + max new positions capped at 2** for this session. The drift edge is not currently paying → defensive; only high-conviction setups clearing the higher bar trade. Overlay governs NEW entries only (never exits).
- **Regime BULL** — SPY Nov-11 close **$759.80 > 200-day MA $731.28** (+3.9%, recomputed from IEX bars) → bear-regime rule inactive. ELEVATED_BAR new-position cap (2) is the binding one.
- **Macro-deferral rule:** MOOT — even if triggered it only raises the EPS bar to >20%, already enforced by ELEVATED_BAR.
- **Weekly new-position count:** 0 opened this week (Mon Nov-9 → Fri Nov-13); last buy was VRT (Oct-29, prior week, stopped −8% Nov-2). Planning REGN → **1/2** under the ELEVATED_BAR cap. ✓
- **Sanity checks:** cash floor after REGN fill ≈ 89.8% (≥10% ✓); concurrent 0→1 (≤8 ✓); max new-per-week 1/2 under ELEVATED_BAR (≤2 ✓); sector REGN Health Care ~10.2% (<30% ✓).
- **LLY DROPPED (documented):** Q3 (Oct-29) rev $24.4B +39% YoY beat + FY rev guide raised to $91–92B (3rd raise); making fresh ATHs ($1,437.79 Nov-11, strong drift). BUT the EPS surprise is ambiguous (one-time $4.57 IPR&D charge → +12–34% range), so it does NOT cleanly clear the mandatory >20% ELEVATED_BAR earnings-driven bar; a guidance-raise entry is not among strategy.md's EPS-exempt catalysts (only analyst-revision / partnership are). No fresh in-window catalyst since Nov-6. Under the defensive ELEVATED_BAR posture (and consistent with the Nov 9–11 ELEVATED_BAR runs that declined to re-plan it), LLY is dropped in favor of the single cleanest setup. Not a thesis failure — a bar/posture call.
- **Other screens:** AMAT & CSCO (both in-universe, IT) **report TODAY Nov-12 AMC → inside the 3-day earnings window → excluded** (event risk, no post-earnings signal yet). SN (in-universe) remains dropped — its headline >20% beat is substantially an IEEPA tariff-duty refund (ex-refund ≈ a miss). Qnity (+12% EPS, non-universe, below bar), ELAN (+28.6% EPS beat + raised FY, Health Care, non-universe, but only +7.6% muted reaction + ~1wk stale) — logged in research_log, NOT watchlist-added (muted PEAD reaction + large pending_review backlog).
- **Watchlist:** only MRVL is `active` — next earnings ~Nov-26 (outside 3d), last report ~late-Aug (~76d) → no ≤30-day fundamentals catalyst → not plannable. No new watchlist adds (REGN is already an in-universe constituent; no compelling non-universe catalyst surfaced).
- **Regulatory flags:** none on the planned name (REGN shelf-reg clean, BIS N/A).
- **Watchlist flags:** none.
- **Carry-forward (human):** portfolio.md ~460KB audit-comment bloat (recurring human-trim flag; not auto-trimmed); trade_log VRT buy/sell commit_sha `<pending>` (human backfill); sizing-doc "(11%)" vs strategy.md 20% (strategy.md wins; REGN sized ~10.2% is compliant under both). Log rotation DEFERRED to market_close (pre_market appends only).
- **market_open reminder:** apply opening-range / 21-day-EMA / chase-guard gates STRICTLY on REGN (it is extended near its 52-wk high after a +4.77% day); do NOT chase above the $965 limit — let the gates reject if it gaps up hard. Place the −8% hard stop immediately after fill.
