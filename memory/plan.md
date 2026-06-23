# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-23 (pre_market ~08:03 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates qualified under ELEVATED_BAR (>20% EPS surprise, all sectors). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | CASY thesis intact, no exit criterion fired. Hard-stop cushion 0.37% ⚠️ — mechanical −8% exit (Alpaca stop 33027bf9 $828.58) will fire automatically on the next leg down; no discretionary cut warranted (strategy.md bars cutting on temporary weakness; requires hard-stop hit OR broken thesis). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | CASY far below the +10% trailing trigger (held −7.66%). No conversion. |

## Notes

**Gates (all PASS):** Alpaca `/v2/clock` is_open=false, next_open=2026-06-23T09:30 ET → market opens today (Tue), not a holiday → routine proceeds. Reconciliation 1/1: CASY 11 @ $900.626364 matches Alpaca `/v2/positions` exactly — zero divergence. Universe cache expires 2026-06-28 (fresh, 5d). Account ACTIVE, trading_blocked=false.

**Regime / overlays:**
- PEAD posture **ELEVATED_BAR** (realized health −0.492%, n=367; computed Jun 21, expires Jun 28 — fresh) → entry bar **>20% EPS surprise for ALL sectors**, max **2** new positions this week.
- SPY regime **BULL** (close $744.27 > 200-day MA $688.84, n=200 IEX, margin +$55.43) — no additional bear-regime tightening; ELEVATED_BAR is the binding constraint.
- Macro: S&P futures ~−0.2% (not >0.4% down), 10-yr ~4.48% (not at a multi-month high; peak 4.70% May 20) → **macro deferral rule NOT triggered**. Bar already >20% via ELEVATED_BAR regardless.

**Why no buys (candidates screened, 0 qualified):**
- **MRVL** (watchlist `active`, in universe since S&P 500 inclusion Jun 22) — **DROP step g**: cur $313.57 trades ~31% ABOVE consensus mean PT $238.75 (44 analysts, S&P Global) / MarketBeat $228.71; only outliers KeyBanc $385 (Jun 18) & B.Riley $345 (Jun 12) exceed $300, not consensus. Earnings path fails (Q1 FY2027 EPS $0.80 vs $0.79 = +1.3% « >20% bar). Extreme ±10–17%/day chop + fixed −8% hard stop ⇒ stop likely fires on noise; S&P inclusion mechanical/priced-in. Mean-reversion to ~$240 a plausible 42-day thesis-breaker. Watchlist status stays `active` (reassess only if consensus PTs clear $300).
- **MU** (IT) — reports Wed Jun 24, **inside the 3-day earnings window** → blocked.
- **FDX** (Industrials) — reports late Tue Jun 23, **inside the 3-day earnings window**, not yet reported → blocked.
- **KR** (+2.2% Jun 18), **CRM** (+24% May 27 but step-f anti-PEAD drift, still falling), **ADBE** (+6.43% Jun 11), **ORCL** (+11.64% Jun 10) — all carried drops (fail >20% bar or negative post-earnings drift).
- Earnings desert between Q1/Q2 seasons (Q2 season starts mid-July). No fresh in-window >20% EPS universe beat. No non-universe catalyst → no watchlist `pending_review` add.

**Open position — CASY (HOLD):** Consumer Staples, 11 @ $900.626364, held 12d, cur $831.67 (−7.66%), hard stop 33027bf9 $828.58 (cushion **0.37%** ⚠️⚠️). Thesis genuinely intact (Q4 FY2026 EPS $4.37 = +30% beat / +66% YoY, FY2027 guide raised, 27th consecutive dividend increase, S&P 500 add, 4-quarter beat streak; fresh PTs DB $1,000 / BofA $975 / JPM $975). **Investor Day TOMORROW Jun 24** (9:30am–1:30pm ET, new 3-year plan) — a potential near-term catalyst (not an earnings report). Chronic "never-worked" / GEV-style pattern; the mechanical −8% stop will execute on any further leg below $828.58 — Alpaca handles it automatically. No discretionary action; market_open executes plan only.

**Sanity checks (no new buys, all moot but recorded):** cash floor 90.8% >> 10% ✓; max concurrent 1/8 ✓; max new-per-week 0/2 under ELEVATED_BAR (last buy CASY Jun 11) ✓; sector cap Consumer Staples (CASY) ~9.2% < 30% ✓.

_(reset by market_close 2026-06-22 — this plan written by pre_market 2026-06-23)_
