# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-22 (pre_market, ~08:04 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared ELEVATED_BAR (>20% EPS all sectors, highest-conviction only). See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | CASY held — no exit criterion fired (hard stop $828.58 NOT yet hit; thesis intact; not +10%; not 60d-stale). ⚠️ Stop cushion critically thin (0.49%) — a mechanical −8% exit is likely on the next leg down. Alpaca stop 33027bf9 will handle it automatically; pre_market does not place orders. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | CASY far below +10% trigger (held −7.55%). |

## Notes

- **Gates PASS.** Clock: is_open=false, next_open=2026-06-22T09:30 ET → market opens today (Mon), not a holiday. Reconciliation PASS (1/1): CASY 11 @ $900.626364 matches Alpaca /v2/positions (zero divergence). Universe expires 2026-06-28 (fresh, 6d). Account ACTIVE, trading_blocked=false. DRY_RUN: false.
- **Posture: ELEVATED_BAR** (pead_health.md computed 2026-06-21, expires 2026-06-28, fresh; realized health −0.492%, n=367, health_ok=false) → EPS-surprise bar >20% for ALL sectors, max 2 new positions/week.
- **Regime: BULL** (SPY close $746.75 [Jun 18 IEX] > 200MA $688.34, n=200, margin +$58.41). Standard thresholds; ELEVATED_BAR overlay is the binding constraint.
- **Macro: deferral rule NOT triggered.** S&P futures −0.1% (not down >0.4%); 10-yr yield ~4.49% (NOT at multi-month high; peak 4.70% May 20). Backdrop: "encouraging progress" reported in U.S.–Iran talks (Bürgenstock, Switzerland), oil easing (WTI ~$75); Greenspan died at 100. Bar already >20% via ELEVATED_BAR regardless.
- **Earnings desert (between Q1/Q2 seasons).** No fresh >20% EPS-surprise universe reporter in the 30-day window.
- **Candidates screened — 0 qualified:**
  - **MRVL** (watchlist `active` + now in universe; S&P 500 inclusion effective today Jun 22). Earnings path FAILS (Q1 FY2027 ~May 22, EPS $0.80 vs $0.79 = +1.3% surprise « >20% bar). Catalyst/analyst-revision path: step d 52-wk high $329.85 made Jun 18 (0 trading days ago — top recency) ✓; step f RS5 +9.51% (MRVL +10.74% vs SPY +1.23%) ✓; BUT **DROP step g** — current $310.97 trades ~30% ABOVE consensus mean PT ~$238.75 (44 analysts, S&P Global) / median $240; only outlier targets (KeyBanc $385 Jun 18, B.Riley $345 Jun 12) exceed $300. Extreme volatility (−17% Jun 5, −10% Jun 16, +11% Jun 15; ±10–17% daily swings) + a fixed −8% hard stop ⇒ stop very likely fires on noise; mean-reversion toward the ~$240 consensus is a plausible thesis-breaker within 42 days. S&P inclusion = mechanical index buying, priced-in, not fundamental. Watchlist condition "reassess only if PTs raised above $300" is met only by 2 outliers, not the consensus. Status stays `active`; reassess on a quieter base or if the consensus mean clears $300.
  - **KR** (Kroger, Consumer Staples): Q1 reported Jun 18, EPS $1.49 vs $1.46 = +2.2% beat « >20% bar; only identical-sales guide raised, adj-EPS guide held. DROP step a.
  - **MU** (Micron, IT): reports Wed Jun 24 — INSIDE the 3-day earnings window, and not yet reported. Blocked.
  - **ADBE** (+6.43% Jun 11), **ORCL** (+11.64% Jun 10): fail >20% bar (carried). **HPE** (+46% Jun 1): drift-failed, already stopped Jun 2 (carried). **CRM** (+24% May 27): step-f anti-PEAD drift, carried.
- **No non-universe catalyst warranting a watchlist add.** A TPR (Tapestry) "beat + raised guide" item surfaced in an aggregator snippet but with no clear/verified report date in-window and TPR is outside both lists — not added on thin evidence (avoid a noise pending_review flag).
- **Sanity check (no buys → trivially clean):** weekly slots 0/2 (ELEVATED_BAR cap); 1/8 concurrent (CASY); cash ~$89,981 (90.8%) >> 10% floor; Consumer Staples (CASY) ~9.2% << 30% sector cap.
- **⚠️ CASY watch (chronic "never-worked"):** held since Jun 11, never closed green, now −7.55% ($832.65 vs cost $900.626364); hard stop 33027bf9 $828.58 active with cushion just **0.49%**. Thesis still intact (Q4 FY2026 EPS $4.37 +66% YoY, FY2027 guide raised, 27th consecutive dividend increase, added to S&P 500, 4-quarter beat streak; fresh bullish PTs Evercore $915 / Wells $910). Per strategy.md, NOT cut on temporary weakness; the mechanical −8% stop will execute if the next down leg breaches $828.58. Flagged for market_open/midday (pre_market places no orders). This is the GEV-style chronic-underwater pattern flagged repeatedly in lessons.md.
- **INFRA NOTE:** the cloud working copy was again an orphaned/divergent clone (local main history ended 2026-06-04, NO common ancestor with origin/main after an upstream force-update); synced local main to authoritative origin/main (6cf655d) before running. The reset discarded only stale disjoint local commits — all canonical trading state lives on origin and was healthy/current. No destructive history rewrite of origin.
