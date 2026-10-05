# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-10-05 (pre_market, Monday ~08:2x ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | **0 candidates cleared ≥6/10 under the ELEVATED_BAR >20%-EPS-all-sectors bar. No in-universe / active-watchlist name had a fresh (≤30d) >20% EPS beat with positive post-earnings drift → initial gate not passed → deep-research a–i not run. Plan fewer, do not lower the bar.** |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash) — no positions, so no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Book FLAT — no positions to convert. |

## Notes

**Session: 2026-10-05 pre_market. DECISION: NO new buys, NO sells, NO conversions. Book stays FLAT (0/8, 100% cash).**

**Gates**
- Gate 1 (calendar): Alpaca `/v2/clock` → `is_open=false`, `next_open=2026-10-05T09:30:00-04:00` = opens TODAY → NOT a holiday → proceed.
- Gate 2 (reconciliation): `/v2/positions=[]` MATCHES portfolio.md FLAT; `/v2/orders?status=open=[]` (no orphans) → **RECONCILIATION 0/0 PASS**, zero divergence. Account ACTIVE, `trading_blocked=false`; equity **$96,448.31**, cash $96,448.31 (100%), buying_power $385,793.24, long_mv $0.
- Gate 3 (universe freshness): `universe.md` screened 2026-10-04, `expires_on=2026-10-11` → FRESH (today 2026-10-05) → freshness gate PASSES; no re-screen. 266 tickers.

**Regime / overlay (new ENTRIES only; never halts, never affects exits)**
- **PEAD health FRESH + ELEVATED_BAR** — `pead_health.md` computed 2026-10-04, expires 2026-10-11; `realized_health_60d_pct = -0.292%`, `health_sample_n = 392`, `health_ok = false`. → Per pre_market step 1c: **EPS-surprise bar RAISED to >20% for ALL sectors + max 2 new positions** this session (the bull-and-weak case).
- **SPY regime BULL** — `spy_above_200ma = true` (SPY close 769.64 > 200MA 717.04). Bear-regime rule NOT triggered. Effective new-position cap = min(5 base, 2 ELEVATED_BAR) = **2**.
- **Macro-deferral MOOT** — even if the down-futures + multi-month-high-10yr both-legs condition were met (Oct-5 premkt futures only slightly lower, oil ~$69), ELEVATED_BAR already imposes >20%/cap-2 (equal-or-stricter). No additional effect.

**Overnight / weekend sweep (step 2) — nothing plannable**
- Backdrop: Oct-5 premkt futures slightly lower on new month/quarter; oil ~$69; focus on ADP jobs, ISM mfg, Fed (Warsh) remarks. Q3 S&P 500 reporting season does not ramp until ~mid-Oct (banks ~Oct 13–15); the pre-Q3 lull continues (~22nd consecutive session with ~0 in-universe / active-WL >20% qualifiers).
- **STZ (Constellation Brands, Cons. Staples):** reports Q2 FY2027 **Oct-6 AMC (tomorrow)** → INSIDE the 3-day earnings window (event risk) → ineligible regardless; not yet reported.
- **FSLR (First Solar, IT/solar):** best weekly gainer (~+14% wk) but move is tariff-clarity / renewables-momentum / analyst-upgrade driven; next earnings ~Oct-29; last earnings late-July (>60d, outside 30d window) → NO fresh ≤30d >20% EPS PEAD catalyst → drop.
- **MRVL (sole ACTIVE watchlist, IT/semi):** most recent earnings Q2 FY27 (Aug-27, now ~39d, OUTSIDE 30d window; ~2% EPS surprise then); current items = Oct-6 Investor-Day / analyst / partnership chatter, NOT a >20% beat; next earnings ~Nov-26 → drop (consistent every prior session; would also require the mandatory BIS scan if it ever qualified).
- **KMX (CarMax):** Q2 FY27 (Sep-29) +59.7% EPS surprise clears even the >20% bar, BUT it is **watchlist `pending_review` (human-only)** — MUST NOT plan until the human sets `status: active`. No action.
- Other recent "big beat/raise" headlines surfaced (Haemonetics +33.75%, Tenet +23%, Agilysys +23%) are stale July/August prints already tracked on the watchlist as `pending_review` — not fresh, not active → not plannable.
- No compelling non-universe catalyst surfaced this weekend → **NO new watchlist additions** this session (KMX already present pending_review).

**Decision rationale:** No name passed the initial >20%-EPS-in-30d + positive-drift signal gate, so the full step a–i deep-research protocol was not triggered (per MUST-NOT: a candidate cannot score ≥6 without completing a–i; nothing reached that stage). Plan fewer buys rather than lower the bar (mirrors 2026-09-25 → 2026-10-02).

**Sanity-check (step 6):** cash 100% (≥10% floor ✓); concurrent 0/8 (≤8 ✓); weekly new 0/2 this week under the ELEVATED_BAR cap ✓ (last entry DELL 2026-09-17, exited 2026-09-24 −8% hard stop); sector caps N/A (flat). Regulatory flags among planned: NONE (no candidate reached deep research). Watchlist flags: NONE.

**Flags for human**
- ⚠️ Sizing discrepancy: `routines/pre_market.md` step 5 annotation says "(currently 11%)" but `strategy.md` `Max position size at entry` field = **20%**. strategy.md is authoritative (human-only). Moot this session (no buys). Flagged for human to reconcile the stale routine annotation.
- ⚠️ `portfolio.md` bloat (~367KB accumulated audit comments, exceeds single-read limit) — recurring human-trim flag (NOT auto-trimmed; deleting audit history needs human sign-off).
- ℹ️ research_log rows dated 2026-09-18 (×2) and 2026-09-20 are now >14d old — flagged for today's `market_close` to rotate to `archive/research_log_2026-09.md` (pre_market appends only, per established division of labor).

DRY_RUN: false.
