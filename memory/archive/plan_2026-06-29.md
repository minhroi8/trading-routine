# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-29 (pre_market ~08:02 ET) — **NO ORDERS PLANNED** (0 qualified buys; book FLAT, no sells/conversions).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the full screen. Sole shortlisted name MU (+23.8% beat) dropped on the risk leg — see Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) since the MU −8% same-day stop Jun 25. Nothing to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | No open positions. |

## Notes

- **Gates (all PASS).** Clock: `is_open=false`, `next_open=2026-06-29T09:30 ET` = today (Mon), not a holiday → proceed. Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` matches portfolio.md FLAT book, zero divergence; account ACTIVE, `trading_blocked=false`, equity $98,266.98, 100% cash; no open orders (no orphan stops). Universe cache fresh (expires **2026-07-05**, refreshed Jun 28).
- **PEAD health overlay STALE → posture NORMAL (flagged STALE), bar NOT raised.** `pead_health.md` `expires_on=2026-06-28` < today 2026-06-29. Per pre_market step 1c, a stale overlay is treated NORMAL and may **never** raise the bar (the universe-cache gate is the only hard halt, and it PASSES). Last (now-stale) reading was ELEVATED_BAR, realized −0.492%, n=367. **⚠️ Operational anomaly for human:** the Jun 28 `universe_refresh` rebuilt `universe.md` (screened 2026-06-28) but did **NOT** recompute `pead_health.md` (still computed 2026-06-21) — a **partial universe_refresh** (universe written, PEAD overlay skipped). Next Sunday refresh should restore it; surfaced in Discord.
- **SPY regime: BULL.** Close $729.35 (Jun 26 IEX) > 200-day MA $690.51 (n=200), +5.6% above. Standard `strategy.md` thresholds this session: EPS surprise **>15%** (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also need streak≥2), **max 5 new positions/week** (slots reset today → 0/5), no ELEVATED_BAR cap.
- **Macro deferral NOT triggered.** S&P futures **+0.2–0.8%** (UP; U.S.–Iran agreed to halt hostilities), 10-yr yield ~4.376% (not at a multi-month high). Neither leg met.
- **Why 0 buys (the binding read).** Late-June is between earnings seasons and the tape is a **"beat-and-sell" / tech-malaise** risk-off — every fresh catalyst name faded ~10%+. Full screen of universe + active watchlist:
  - **MU** (IT) — *sole shortlisted candidate, full a–i research; DROPPED on risk.* Q3 FY2026 **+23.8% EPS beat** ($25.11 vs $20.28), **7 consecutive quarters** beating, Q4 guide RAISED to rev $50B / EPS $31, ~$22B commitments / $100B floor-priced backlog, ~12 PT raises / 0 downgrades, 52-wk high within days, post-earnings vol ~2×, **BIS scan CLEAN** (HBM controls are Dec-2024, not fresh; no entity-list action), XLK 20d vs SPY neutral (+0.1pt). **But:** the mandatory **fixed −8% stop sits well inside MU's ±9–16% daily range** → another mechanical noise-stopout is highly likely — this *exact* failure occurred **4 trading days ago** (Jun 25 same-day −8% stopout, thesis intact). Drift is also rolling over (Jun 25 $1,215 → Jun 26 $1,123.835 = −7.5%; −10% from peak). Rubric ~7/10 on fundamentals, but the position cannot be structured to survive its own mandated stop → **drop**. *Live instance of the lessons.md proposed volatility-scaled-stop rule — for human review.*
  - **QCOM** (IT) — Investor Day Jun 24 (Meta CPU partnership, 2029 $40B target) faded: $204.11 (Jun 23) → $188.62 (Jun 26) = −7.6% vs SPY −1% → **step-f drop**.
  - **JBL** (IT, Jun 17) — EPS surprise only **+1.3%**; +10% pop round-tripped same day → −13.5% to $359 → **drop** (sub-bar + negative drift).
  - **ACN** (Jun 20) — +2.7% beat, revenue MISS, stock **−18%** → drop. **DRI** (Jun 25) — +0.8% surprise, rev miss, −3.4% → drop.
  - **KEYS** (+23.7%) reported **May 19 = 41d** → outside 30-day window. **ADSK** (+10.7%, May 28) sub-bar + 32d stale.
  - **NKE** (Jun 30 AC) and **GIS** (Jul 1) → inside 3-day earnings window, blocked.
  - **MRVL** (watchlist active) — earnings catalyst now >30d stale; still trades above consensus mean PT (~$238.75 vs $265.84) → step-g drop (carried). **INTC** +10.6% record-high move is speculative/headline (no fresh beat) → step-g drop.
  - Top June gainers (INHD/CAST/NVCT/RTB/STI) are micro-caps outside the S&P 1500 universe.
- **No watchlist `pending_review` additions** — no compelling non-universe catalyst surfaced that isn't already covered (MRVL already on the watchlist).
- **Constraint check (no orders, so trivially satisfied):** cash floor 100% >> 10% ✓; concurrent 0/8 ✓; new-per-week 0/5 ✓; no sector exposure. Per pre_market guidance, planned **fewer buys rather than lowering the bar** — MU's fundamentals were strong but the fixed −8% stop is structurally incompatible with its volatility.
- DRY_RUN: false. `market_open` should take **no actions** from this plan (no buys, no sells, no conversions). Book remains FLAT.
