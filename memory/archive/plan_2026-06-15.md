# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-15 (Monday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 qualifiers cleared ELEVATED_BAR (>20% EPS all sectors) + steps a–i. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | No exit criterion fired on CASY or SNDK (not −8%, not 60d-stale, theses intact). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | SNDK already on 7% trail (36402808, converted Jun 12, ratcheting/Alpaca-managed). CASY below +10% trigger. |

## Notes

- **Gates: ALL PASS.** Clock: `is_open=false`, `next_open=2026-06-15T09:30 ET` — market opens today (Mon), timestamp ~08:01 ET (normal pre-market run, not a holiday). Reconciliation **PASS 2/2** zero divergence vs Alpaca `/v2/positions`: CASY 11 @ $900.626364 ✓; SNDK 6 @ $1,643.693333 ✓. Universe cache expires 2026-06-21 (valid). DRY_RUN: **false**.
- **PEAD signal-health: ELEVATED_BAR** (pead_health.md computed 2026-06-14, expires 2026-06-21 — FRESH). realized_health_60d_pct **−1.025%**, health_sample_n **282**, health_ok=false. → EPS-surprise bar raised to **>20% for ALL sectors**; **max 2 new positions** this session. Overlay TIGHTENS only; governs new entries only (never exits). (Health improved from −2.08% prior but still <0.)
- **SPY 200-day regime: BULL.** SPY $741.67 close (Jun 12 IEX) > 200MA $686.28 (n=200), margin +$55.39. Standard sector thresholds apply (no bear tightening); ELEVATED_BAR is the binding constraint.
- **Macro: risk-ON.** S&P 500 futures **+0.5%** on completed U.S.–Iran peace deal (Strait of Hormuz reopening); oil tumbling; gold +2.8%; SpaceX +5.3% post-IPO. 10-yr yield ~4.5% — NOT at multi-month high (peak 4.70% May 20). **Macro deferral rule NOT triggered** (futures up, not down >0.4%). Bar already >20% via ELEVATED_BAR regardless.
- **Candidates screened — 0 qualified** (>20%-EPS bar + steps a–i, 30-day catalyst window = since ~May 16):
  - **CRM** (Salesforce, Q1 FY2027 May 27, +24% EPS beat — clears >20% bar, in window): **DROPPED step f.** Last 5 trading days CRM −9.05% ($182.54 Jun 8 → $166.02 Jun 12) vs SPY +0.33% = **RS spread −9.38%**, strongly negative. Beat-but-drifting-down anti-PEAD profile; clear downtrend ($209 pre-earnings → $166); 52-wk high $276.80 ~67% above current; one PT reset to $160. 4th consecutive session flagged at step f.
  - **MRVL** (watchlist `active`, +46% AI catalyst, S&P 500 inclusion Jun 22): **DROPPED step g.** Trading ~$281 vs analyst consensus mean PT $235.70 (median $240) — stock ~19% ABOVE consensus; most recent note Rosenblatt Jun 12 PT $240 implies −14.6% downside. Extreme volatility ($316 Jun 4 → $263 Jun 5) + dilution overhang (26M+ convertible preferred). S&P 500 inclusion is mechanical/priced-in, not fundamental. Watchlist stays active; reassess post-Jun 22 only if PTs materially rise above $300.
  - **STRL** (+57.46% Q1, infrastructure): stale — reported May 5 = 41 days ago, OUTSIDE 30-day catalyst window. Drop.
  - **ADBE** (+6.43%), **ORCL** (+11.64%), **DG** (+5.8%): all fail step a (<20% bar). Quiet inter-season earnings week (aggregate beat magnitude 16.7%, below our bar); no new >20% universe reporters Jun 8–12. No notable pre-open earnings Mon Jun 15.
  - No compelling catalyst on a non-universe ticker → **no new watchlist `pending_review` add.**
- **Open-position theses (both HOLD, no exit fired):**
  - **CASY** 11 @ $900.626364 (held 4d, −0.63%, cur $895; hard stop 33027bf9 $828.58, cushion ~7.5%): dividend +14% to $0.65 (Jun 10), board appt Stanley Sutula III (Jun 8), Q4 FY2026 EPS $4.37 +66% YoY, added to S&P 500. No guidance cut/miss/fraud. Thesis intact.
  - **SNDK** 6 @ $1,643.693333 (held 10d, **+28.5%**, cur $2,111.97; 7% trailing 36402808 — HWM $2,021.65/stop $1,880.13 at Jun 12 close, ratchets higher today): AI-NAND upcycle accelerating, Morgan Stanley upgrade, +6.7% leading Nasdaq, $42B backlog, Q3 sales +251%. Valuation chatter (P/E ~58) is opinion, not a thesis break. Thesis intact/reinforced.
- **⚠️ Note for human / market_open re: partial-profit-lock rule (strategy.md ll.18–22, recently added):** SNDK crossed the +10% trigger and was converted to a **full-position** 7% trailing stop on Jun 12 — *before* the new "sell 1/3 at the +10% trigger, trail remaining 2/3" rule existed. The partial-sell leg was therefore not applied to SNDK (it's now at +28.5% on a full 7% trail). pre_market does not place/plan discretionary sells; whether to retroactively lock 1/3 of an already-trailing position is a human/market_open decision, surfaced here for visibility. No action planned by this routine.
- **Plan sanity vs strategy.md:** 0 new buys → all caps trivially satisfied. Weekly new-position slots **0/2** (ELEVATED_BAR cap; CASY opened Jun 11 = prior week). Concurrent **2/8**. Cash $77,897.31 = **77.6%** (>> 10% floor). Sectors: Consumer Staples (CASY) ~9.8%, IT (SNDK) ~12.6% — both << 30% cap. Equity $100,414.11; 11% max position size = ~$11,046.
