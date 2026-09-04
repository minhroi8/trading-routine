# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-04 (pre_market ~08:2x ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates scored ≥6/10 — see Notes. No buy qualifies. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash) — nothing to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — | No open positions. |

## Notes

**pre_market 2026-09-04 — 0 QUALIFIED → NO BUYS. Book stays FLAT (0/8, 100% cash).**

**Gates (all pass, no hard halt):**
- Clock: `is_open=false`, `next_open=2026-09-04T09:30 ET` → opens today (Fri), NOT a holiday → proceed.
- **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT — zero divergence; no open/orphan orders (`/v2/orders?status=open=[]`). Account ACTIVE, `trading_blocked=false`; equity **$97,328.01** (=cash 100%), 0/8 concurrent.
- **Universe FRESH:** screened 2026-08-30, `expires_on=2026-09-06` (in the future) → freshness gate PASSES (259 rows). No re-screen.
- **⚠️ PEAD health STALE:** `pead_health.md expires_on=2026-08-30` is in the PAST (recurring compute_pead_health.py Yahoo rate-limit miss on the Aug-30 refresh). Per step 1c: treat posture **NORMAL but flagged STALE → do NOT raise the bar** (universe-cache is the hard gate, and it passed). Last real reading (2026-08-23): NORMAL, realized +2.284%, n=91. → standard 15% bars, max 5 new/week.

**Regime & macro (standard thresholds):**
- SPY regime **BULL** — Alpaca IEX 200-day MA: SPY **$773.12** (Sep-3 close) > **200MA $711.60** (+8.6%). Bear-regime rule NOT active.
- **Macro-deferral NOT triggered:** Sep-3 tape rallied (S&P +1.06%) with **Treasury yields FALLING** ("Stocks Rally as Treasury Yields Fall") → 10-yr is NOT at a multi-month high, and futures are not down >0.4% → both required legs FAIL → standard 15% bars stand (no >20% override).

**Candidates evaluated → 0 ≥6/10:**
- **ULTA (Ulta Beauty, Consumer Disc, in univ) — DROPPED (EPS bar + negative reaction):** Q2 FY26 EPS **$6.55 vs $6.17 est = +6.2% surprise ≪ 15% bar**; rev $3.0B (+0.7% beat); raised FY26 guide ($28.70–29.00 EPS) + $1.8B buyback — but the operating **EPS surprise is single-digit** and one headline notes **"shares fall"** on the print (sell-the-news / negative step-f). Next earnings Dec 3 (>3d ✓), but sub-bar surprise + negative reaction → clear drop.
- **ABNB (Airbnb, Consumer Disc, in univ) — DROPPED (EPS bar + stale catalyst):** Q2 CY26 (reported **Aug 6** = 29d ago, edge of 30-day window) EPS **$1.37**, surprise cited **+9.6% (vs $1.25) to +14.17% (vs $1.20) — best case still < 15% bar**; rev +0.81% beat; +9–10.5% pop on the print. Catalyst 29 days old → PEAD drift essentially spent; not a fresh entry. Sub-bar surprise → drop.
- **CRM (Salesforce, IT, in univ) — DROPPED (re-score <6, catalyst decayed — consistent with 08-31/09-01/09-02):** reported Aug 26/27 (~8d ago). Real non-GAAP EPS ~$3.40 ≈ +4% vs $3.27 → **below 15% bar** (the "$5.90/+80%" headline is a one-time ~$2.6B Anthropic-stake gain, not recurring); qualifies only via guidance-raise/partnership exempt path. **Entry legs decayed:** the +22–24% 2-day pop is spent, price has FADED back to ~$256 (round-tripping — the give-back pattern lessons.md flags); **52wk-hi $268.98 was ~2025-12-29 (>90d ago) and price is still below it = a bounce in a 20-month downtrend, NOT a fresh-ATH breakout** → weak momentum leg. Re-score ~5/10 → below 6. Drop (keeps the 3-session consensus consistent).
- **MRVL (active watchlist, IT/semi) — DROPPED (no fresh catalyst + negative PEAD):** June Computex catalyst long stale; Q2 (Aug 26/27) rev beat but **~0% EPS surprise and sold-the-news −8/−10%**; now ~$180 (from ~$241). No fresh positive fundamentals signal in the last 30 days → drop.
- **AVGO (Broadcom, IT, in univ) — DROPPED (negative reaction):** Q3 (Sep 3) EPS $3.32 vs $3.22 beat but stock **−~3%** on a disappointing fiscal-Q4 revenue forecast → negative step-f.
- **HPE / HPQ — DROPPED (negative reaction):** both beat but fell (HPE −4%, HPQ −11%).

**Non-universe strong reporters — NOT planned (consumed read-only rule / already flagged):**
- **SNOW (Snowflake, +20% Sep-2, clean guidance-raise beat)** — already on watchlist as `pending_review` (added 2026-09-03). Human-only to set `active`. MUST NOT plan. No new action.
- **DG (Dollar General, Consumer Staples, +12.4% Aug-27)** — CONSIDERED, NOT re-flagged. Headline EPS $2.48 vs $2.01 = +23.5% is **inflated by a ~$0.25 one-time tariff-refund benefit**; clean surprise ex-refund ≈ ($2.23 vs $2.01) **+11% < 15% bar** — same one-time-item distortion that dropped ROST/ANF/TGT. Already considered & declined by prior sessions (08-28, 08-31) and surfaced for the next universe_refresh (screen-source cache gap; DG is an S&P 500 name). Consistent with prior deliberate calls → not added.
- Petco (+9% on EBITDA-margin beat, small-cap, not a clean >15% EPS surprise), GOOGL/AMZN (huge Q2 beats but inflated by one-time investment gains AND >30d old) — not planned.

**DECISION: 0 candidates ≥6/10 → plan NO buys** (routine: plan fewer rather than lower the bar). ~9th consecutive session of ~0 qualifiers as Q2 earnings season winds down. Planned sells: none (flat book). Weekly slots 0/5 unused. **No new watchlist adds.** Regulatory flags among planned: NONE (no buys — no shelf-reg/BIS scans required).

⚠️ Sizing note (carryover, moot with no buys): pre_market.md step 5 says "(currently 11%)" vs strategy.md `Max position size at entry` field "20%" — flagged for human. DRY_RUN: **false**.
