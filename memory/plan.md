# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM>.md`.

## Date

2026-06-18 (pre_market, ~08:02 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates qualified under ELEVATED_BAR (>20% EPS all sectors). See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | CASY held — no exit criterion fired (−4.96%, hard stop 33027bf9 $828.58 cushion 3.20%; thesis intact; held 7d). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | CASY far below +10% trigger; only holding. |

## Notes

**Posture: ELEVATED_BAR (pead_health, expires 2026-06-21) — >20% EPS surprise ALL sectors, max 2 new positions/week. SPY regime BULL (close $741.02 > 200MA $687.80). DRY_RUN: false.**

Gates (all PASS): clock `next_open`=2026-06-18T09:30 ET (today, not a holiday) → proceed; reconciliation 1/1 CASY ✓ zero divergence vs Alpaca; account ACTIVE; universe cache valid (expires 2026-06-21). Macro: futures higher, Fed held rates Jun 17 (slower growth/higher inflation projection), oil sliding, U.S.–Iran developments — macro deferral rule NOT triggered (futures up, not down >0.4%).

**No buys — 0 of 3 candidates qualified (weekly slots used 0/2):**
- **MRVL** (watchlist `active`) — Q1 FY2027 (~May 22) non-GAAP **EPS $0.80 vs $0.79 = +1.3% surprise**; fails the >20% ELEVATED_BAR earnings bar. Catalyst-exemption path (strong guidance raise FY27/FY28, $3B/q by Q3 ahead of schedule; broad analyst PT raises) scores only ~6/10 borderline. **DROP**: (i) trades $289.71, ~23% ABOVE consensus mean PT ~$235.70 (B.Riley $345 / CFRA $300 are outliers) — step-g fail, consistent with every prior session; (ii) the watchlist's own "enter after dust settles" condition is UNMET — MRVL is in violent ±10%/day chop ($308.90 Jun 15 → $278.55 Jun 16 → $289.72 Jun 17), so a fixed −8% hard stop would very likely fire on noise; (iii) ELEVATED_BAR requires highest-conviction only. 52-wk high $323.97 (Jun 3, 10d, recent) but −10.6% off it; RS5 +12.4% vs SPY. Status stays `active`; reassess on a cleaner/quieter base or PTs raised above $300.
- **INTC** (universe) — Trump-announced Apple foundry deal (+9% premarket); partnership catalyst with no near-term financials (ramps 2027–28), yield-execution caveats, already ran enormously → **DROP step g** (speculative headline / gap-chase risk).
- **HPE** (universe) — Q2 FY2026 (Jun 1) EPS +46% clears the >20% bar, but post-earnings drift FAILED: now $48.19, ~−26% below its Jun 2 earnings-day high (~$65) and BELOW our own Jun 2 −8% stop-out ($54.63); momentum broken, 17d stale → **DROP step d/f**, no re-entry warrant.
- No other fresh >20% EPS-surprise universe reporter in-window (Jun 15–19 light; AVGO already screened/rejected prior week). No non-universe catalyst → no watchlist `pending_review` add.

**No sells / no conversions:** CASY (only holding, Consumer Staples 9.5% << 30% cap) — thesis intact (Q4 FY2026 EPS +30%/+66% YoY, FY2027 guide raised, S&P 500 addition, 4-qtr beat streak); −4.96% is a post-runup pullback, no exit criterion fired (not −8%, not +10% trigger, not 60d-stale). Hard stop 33027bf9 $828.58 remains active (market_open to confirm). 1/8 concurrent, ~9.5% deployed (~90.5% cash) — heavy cash is the expected ELEVATED_BAR posture (multi-week 0–1 qualifier pattern), not a directive to lower the bar.
