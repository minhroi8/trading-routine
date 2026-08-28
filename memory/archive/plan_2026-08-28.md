# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-28 (pre_market ~08:2x ET) — **0 candidates scored ≥6/10 → NO planned buys. Book stays FLAT (0/8, 100% cash).**

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the standard 15% EPS-surprise bar with a positive fresh drift — see Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT — no open positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Regime / posture (this session):**
- **DRY_RUN: false.**
- **Regime BULL** — SPY Aug 27 IEX close $771.18 > 200-day MA $709.38 (+8.7%). Standard sector thresholds apply.
- **PEAD health FRESH + NORMAL** (computed 2026-08-23, expires 2026-08-30; realized_health_60d +2.284%, n=91, health_ok=true) → standard **15% EPS-surprise bar** (20%+ for Utilities/Real Estate/Industrials/Energy), **max 5 new/week**. No ELEVATED_BAR overlay.
- **Macro-deferral NOT triggered:** pre-market S&P 500 futures ~−0.07% (fails the "down >0.4%" leg); 10-yr Treasury ~4.24% (retreating, NOT a multi-month high — fails its leg). Both legs required → standard bars.
- **Universe FRESH** (screened 2026-08-23, expires 2026-08-30, 294 rows).
- **Reconciliation 0/0 PASS** — Alpaca /v2/positions=[] matches portfolio.md FLAT; no open/orphan orders. Account ACTIVE, equity $97,328.01 (=cash 100%), 0/8 concurrent. Weekly new-position slots 0/5 used.

**Candidates researched — 0 qualified (the fresh Aug 26–27 earnings batch was single-digit EPS surprises or negative reactions):**
- **VEEV (Veeva Systems, Health Care, in univ) — DROP on EPS bar.** Q2 FY27 (reported Aug 26 AC): adj EPS $2.35 vs $2.22 = **+5.9% surprise** — BELOW the 15% Health-Care bar; rev $928M +17.6% (+2.7% beat); RAISED FY27 guide (rev $3.69B from $3.64B ≈ +1.4%; adj EPS $9.21 from $9.05 ≈ +1.8% — a *modest* raise, NOT a catalyst-exempt guidance event). Technically the strongest setup of the batch (+15.1% day-of pop, **vol 3.56x** 20d avg, price $282.18 > 21d EMA $237.62, XLV +4.96% vs SPY +3.98% over 20d = HC slightly leading) BUT the earnings-surprise magnitude — the PEAD input — is single-digit and the guide raise is too small to qualify as an analyst-revision/partnership catalyst exemption. Same treatment as NVDA (+6.2%), CRM (single-digit), ROST (+5.6% clean) this month. Shelf CLEAN, BIS N/A. 52wk-hi $310.32 (2025-10-07, >90d ago → recency downrank). Only 1 day of post-earnings drift.
- **ADSK (Autodesk, IT, in univ) — DROP on EPS bar + negative reaction.** Q2 FY27 (reported Aug 27 AC): adj EPS $3.30 vs $3.12 = **+5.8% surprise** — BELOW the 15% IT bar; rev $2.05B +16% (+2.0% beat); RAISED FY27 rev/billings guide (MaintainX contribution) BUT **shares fell ~5% AH to ~$257** on a cut to the FY free-cash-flow midpoint (sell-the-news). The Aug 27 +6.3% IEX close was a pre-earnings run-up now reversing → negative post-earnings drift. Double disqualified.
- **MRVL (active watchlist, IT/semiconductor) — DROP on EPS bar + sharply negative reaction.** Q2 FY27 (reported Aug 27 AC): rev $2.739B +37% YoY (record, +~1% beat); non-GAAP EPS $0.94 = **in-line with consensus (~0% surprise)** — fails the 15% IT bar; RAISED FY27 rev outlook to ~$12B and FY28 to ~$18B (data-center +46% YoY). BUT stock gave back gains AH and is **−7.75% premarket Aug 28** (latest trade $222.58 vs Aug 27 close $241.29) → negative PEAD reaction (step-f fail). Semiconductor → BIS scan would be required, but dropped on EPS bar + negative drift regardless.
- **LLY (Health Care, in univ, carryover) — DROP, catalyst stale/decayed.** Aug 5 Q2 beat (+27% operational surprise) is now 23d old and drift is DEAD: price $1,175.64 **BELOW 21d EMA $1,208.63** (−2.7%), Aug 27 vol 0.83x. Rolled over after 10 consecutive market_open ORB/EMA defers — no longer a valid fresh-drift entry.
- **NVDA (+6.2% surprise), CRM (single-digit clean surprise), HPQ (beat but −12.5%)** — all dropped in prior sessions / on negative reaction.

**Decision:** fewer than 3 candidates scored ≥6/10 → **plan NO buys** (routine rule: plan fewer rather than lower the bar). Book stays FLAT.

**Watchlist flag (compelling non-universe catalyst, pending_review — human-only to activate):**
- **OKTA** (IT / identity-security, NOT in universe cache) — Q2 FY27 (reported Aug 26 AC): rev $805M +11% YoY (beat guidance $790–794M and consensus $793M), **RAISED FY27 rev guide to $3.185–3.205B** + strong FCF ($227M, 28% margin); stock **+17.4%** on the print. Clean guidance-raise reaction (no one-time-item distortion). OKTA is an S&P 500 constituent ABSENT from the universe cache — likely a screen-source gap (like PAYC/NET/AFRM/EL), not a real liquidity/price failure. Full a–i deep-research (exact EPS surprise %, drift, RS, analyst-conviction) pending. Added pending_review; human must confirm universe/liquidity gates before setting active.

**⚠️ Universe screen-source gap:** the current cache (294 rows, 271 large-caps) is missing many S&P 500 names — this week's strong reporters OKTA (+17.4%), Dollar General (+12%), Abercrombie/ANF, Agilent (A) are all ABSENT. Same recurring gap flagged for PAYC/NET/AFRM/EL. Not fixable by pre_market (universe is read-only here) — next `universe_refresh` (Sun 2026-08-30) should widen the S&P 500 source coverage.
