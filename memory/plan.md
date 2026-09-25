# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-25 (Friday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | **0 candidates cleared ≥6/10 under the ELEVATED_BAR >20%-EPS-all-sectors bar.** See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash) — no positions to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — | Book FLAT — no positions to convert. |

## Notes

**pre_market 2026-09-25 (~08:2x ET, Fri): 0 PLANNABLE candidates → NO new buys. Book stays FLAT (0/8, 100% cash).**

- **Gates.** Alpaca `/v2/clock`: `is_open=false`, `next_open=2026-09-25T09:30 ET` → opens today, **NOT a holiday** → proceed (pre_market runs before the open by design). **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT; `/v2/orders?status=open=[]` (no orphans); zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity **$96,448.31**, cash $96,448.31 (100%), buying_power $385,793.24, long_mv $0.
- **Universe FRESH** (screened 2026-09-20, expires 2026-09-27, 244 rows) → freshness gate PASSES; no re-screen (universe_refresh owns screening).
- **PEAD health FRESH + ELEVATED_BAR** (computed 2026-09-20, expires 2026-09-27; `realized_health_60d_pct=-0.337%`, `health_sample_n=370`, `health_ok=false`) → per step 1c the session bar is **RAISED to >20% EPS-surprise for ALL sectors + max 2 new positions**. Overlay affects NEW entries only, never exits; may only tighten.
- **SPY regime BULL** (stored `spy_above_200ma=true`, SPY 761.69 > 200MA 712.48 per pead_health) → bear-regime rule NOT active; this is the bull-and-weak ELEVATED_BAR case.
- **Macro-deferral NOT triggered:** Sep-25 premarket S&P futures **~+0.02% to +0.36% (UP, risk-on)** → the "futures down >0.4%" leg FAILS; 10-yr Treasury ~5.1–5.15% (multi-year/2007 high) satisfies its leg BUT both are required → not triggered (moot anyway; ELEVATED_BAR already sets >20% all sectors).
- **Candidates → 0 plannable (overnight/earnings sweep):**
  - **COST (universe, Consumer Staples):** Q4 FY26 (reported Sep-24 AC) adj EPS **$6.75 vs $6.55 = +3.4% surprise** (rev $95.7B, +11.2%; $0.15 of EPS from non-recurring IEEPA tariff refunds) → **fails the >20% Consumer-Staples/ELEVATED_BAR bar** by a wide margin. Drop.
  - **CTAS (not in univ/watchlist):** reported Sep-23, adj EPS +3.0% surprise, in-line FY guide, stock fell ~1.2% → sub-bar + not tradeable. Drop.
  - **PAYX (universe, Industrials):** Q1 FY26 EPS $1.34 vs $1.32 = **+1.5% beat**, revenue in-line, **shares fell** → fails >20% bar. Drop.
  - **LEN (not in univ):** Q3 EPS $1.19 vs $1.29 = **-7.75% MISS** (reported Sep-16) → not a beat, not tradeable. Drop.
  - **JBL (not in univ):** Q4 FY26 not yet out (reports Sep-30). Not tradeable regardless.
  - **MRVL (sole ACTIVE watchlist, IT/semi):** most recent earnings Q2 FY27 (Aug-27, ~29d ago) — record rev +37% YoY + 2nd straight FY-outlook raise, but **EPS surprise only ~2%** → **fails ELEVATED_BAR >20% bar**; current momentum = analyst PT/partnership/Oct-6 Investor-Day anticipation, NOT a >20% earnings beat; next earnings Nov-26. Drop (consistent with every prior session).
  - **Premarket movers Sep-25** (Ichor — analyst upgrade; Evolution Metals — Russell-2000 inclusion): non-universe micro-caps with non-fundamental catalysts (not a >20% EPS beat/guidance raise) → NOT compelling enough for a watchlist add.
- **Backdrop:** Q2 season over; Q3 season starts ~mid-Oct → pre-Q3 earnings lull. **~18th consecutive session with ~0 in-universe qualifiers**, now under the stricter >20%-all-sectors ELEVATED_BAR bar. No fresh ≤30d in-universe or active-watchlist >20% EPS PEAD catalyst; no compelling non-universe catalyst → **NO watchlist add**.
- **DECISION: 0 candidates ≥6/10 → plan NO buys** (plan fewer rather than lower the bar, per MUST-NOT).
- **Sanity check (moot — no buys):** cash 100% (≥10% floor ✓), concurrent 0/8 (≤8 ✓), weekly new 0/2 this week (ELEVATED_BAR cap; DELL 09-17 = prior week, exited 09-24 ✓), sector caps N/A (flat). Regulatory flags among planned: NONE (no candidates). Watchlist flags: NONE.
- ⚠️ **Sizing note (flagged for human):** pre_market.md step 5 says "(currently **11%**)" but strategy.md `Max position size at entry` field = **20%**. strategy.md is authoritative per CLAUDE.md; discrepancy is moot this session (no buys). Human should reconcile the parenthetical.
- ⚠️ **portfolio.md bloat (~340KB, exceeds single-read limit)** — recurring human-trim flag (NOT auto-trimmed; deleting audit history needs human sign-off).
- **DRY_RUN: false.**
