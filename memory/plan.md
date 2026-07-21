# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-21 (Tuesday) — pre_market ~08:15 ET. DRY_RUN: false.

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
- Clock: is_open=false, next_open=2026-07-21T09:30 ET → market opens today (Tue), NOT a holiday → routine proceeds.
- **Reconciliation 0/0 PASS:** Alpaca /v2/positions=[] MATCHES portfolio.md FLAT book — zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity $98,266.98, cash $98,266.98 (100%), buying_power $393,067.92.
- **Universe FRESH:** expires_on 2026-07-26 > today (screened 2026-07-19, 306 tickers).
- **PEAD health NORMAL & FRESH:** pead_health.md computed_on 2026-07-19, expires_on 2026-07-26; posture NORMAL (realized_health_60d +1.225%, health_sample_n=318, health_ok=true). Overlay fresh and NOT ELEVATED_BAR → bar NOT raised; standard strategy.md thresholds apply (EPS >15%; >20% for Utilities/RE/Industrials/Energy; Industrials/Energy also streak≥2). Max 5 new/week, no ELEVATED_BAR 2-position cap.
- **SPY regime BULL:** SPY close $742.15 (Jul 20 IEX) > 200MA $697.05 (+$45.10 / +6.47%). Standard thresholds; no bear-regime tightening.

**Macro (pre-market 2026-07-21):** S&P 500 futures modestly higher (~+0.2%; Nasdaq-100 ~+0.4%; Polymarket ~95% implied higher open). **10-yr Treasury yield ~4.55% — NOT at a multi-month high** (peak ~4.70% May 20). **Macro-deferral rule NOT triggered** (requires BOTH futures down >0.4% AND 10-yr at multi-month high — both legs fail). Weekly slots 0/5 (week of Mon Jul 20; last buy MU Jun 25; Jul 20 planned 0 buys).

**Screen — Q2 season week 2 (86 S&P names report Jul 20–24; mega-cap tech Alphabet/Tesla Wed, Intel Thu). Names with real post-earnings drift data are last week's reporters; this week's reporters (Mon Jul 20 AC / Tue Jul 21 BMO) have 0 completed drift days → incomplete a–i (steps e/f/i-ii not computable) = auto-DQ. 0 qualified:**

- **TRV (Financials/insurance) — DROP step g (Q3 catastrophe-reversal risk) + weak PEAD signal quality.** Q2 reported Jul 17 BMO: core income $10.04/sh vs consensus $5.41 = **+85.6% headline beat**, core income $2.16B +44% YoY. **BUT the beat is catastrophe-loss/reserve-driven, not underlying:** cat losses HALVED to $518M (vs $927M Q2'25); consolidated combined ratio 83.6% (from 90.3%); **underlying combined ratio only improved 0.6pp to 84.1%** — the underlying business barely changed. A cat-driven insurance beat is the textbook low-quality PEAD surprise (favorable-weather quarter, not demand/pricing/margin acceleration → historically does not drift like a demand beat). Confirmation strong (vol **2.96×** 20-day avg; earnings-day move **+9.25%** [gap +1.4% then intraday accumulation]; fresh 52-wk high $370.39 = 0–1d ago; PT hikes Raymond James $400 Strong Buy / Truist init Buy $395 / Piper $389 OW; **but KBW cut to Market Perform, PT $356 BELOW price** on valuation). **Drift is FLAT (step f not confirming):** earnings-day close $369.10 (Jul 17) → $368.47 (Jul 20) = **−0.17%** vs SPY −0.15% → RS ≈ **−0.02pp** (popped-and-stopped; only 1 of 5 post-earnings sessions completed = thin). **Step g:** Q3 = peak Atlantic hurricane season (Aug–Oct) = direct catastrophe-reversal risk to the exact driver of the beat, within the 42-day hold — a single major cat event breaks the thesis. Score ~5–6/10 → DROP. Shelf-reg N/A, BIS N/A.
- **GM (Consumer Disc, in universe) — DROP: 0 drift days, incomplete a–i (auto-DQ).** Reported today Jul 21 BMO (consensus $3.11–3.13, ~+22% YoY; raised FY EBIT guide on ~$0.5B favorable tariff adjustment after the Supreme Court tariff decision; gross tariff cost cut to $2.5–3.5B). 0 completed post-earnings trading days → steps e (vol ratio), f (5d RS drift), i-ii (earnings-day gap confirmed) NOT computable → auto-DQ (same reason GS Jul 14 / MS Jul 15 were DQ'd). Strong WATCH for a later pre_market once drift establishes (already in universe — no watchlist flag). Autos also carry a tariff overhang.
- **TFC (Financials) — DROP:** +14% EPS beat < 15% Financials bar.
- **ISRG (Health Care) — DROP:** +12% EPS beat AND declined on a weak forward outlook (anti-PEAD; forward outlook trumped the backward beat).
- **CCK (Crown Holdings, Materials) — OUT OF SCOPE (not in universe, not on watchlist).** Q2 Jul 20 AC: EPS $2.49 vs $2.16–2.18 = +14–15% beat, rev $3.67B (+8–9%), +5% AH / ~+2% premkt. Borderline at the 15% Materials bar; 0 drift days; likely absent from the universe cache on the $20M/day ADV filter. NOT compelling/durable enough for a `pending_review` add (a modest packaging beat, far below the WDFC +48% blowout precedent). No watchlist flag.
- **STLD (Materials) — OUT OF SCOPE (not in universe) + mixed:** EPS $3.69 MISS vs $3.77, rev $6.09B beat vs $5.57B; −1% reaction (anti-PEAD).
- **Other Jul 20 AC reporters (PKE/MCRI/CALX/SFBS + MMM Tue):** out of universe, or misses/mixed (CALX rev miss −12%, SFBS EPS+rev miss, MCRI rev miss). Non-candidates.
- **MRVL (watchlist `active`, in universe) — carried DROP:** no fresh in-window earnings (Q1 FY2027 ~May 27 now ~55d stale, >30-day window); step-g consensus-PT-overshoot pattern persists. Status stays `active` (human-only).
- **WDFC (watchlist `pending_review`) — MUST NOT plan** (human-only to set `active`); already on watchlist, no new flag. (Q3 +48% beat but pending_review + likely fails the $20M/day ADV liquidity gate.)

**Pattern this cycle (unchanged from Jul 20):** the large EPS surprises with drift (GS +45%, MS +18%, TRV +86%) are either selling the news (GS/MS step-f fails) or driven by low-quality one-off items (TRV cat losses) heading into a reversal-risk quarter; the large price pops (MAN, ABT, CCK) have sub-15% or borderline surprises (relief rallies); this week's genuine reporters (GM, 3M, and the mega-caps Wed–Thu) have 0 completed drift days. No candidate combined a high-quality >15% surprise WITH confirmed positive drift AND acceptable 42-day risk. Per routine, plan fewer buys rather than lower the bar. Q2 volume peaks Wed–Thu (Alphabet/Tesla/Intel + dozens more) — fresh drift setups may qualify later in the week once 1–2 sessions of drift print.

**No new watchlist `pending_review` adds** — GM/TRV/TFC/ISRG are already in the universe; CCK/STLD/MMM are non-universe but not compelling/durable enough for a manual add (modest/borderline beats, no standout catalyst). No compelling durable non-universe catalyst appeared.
