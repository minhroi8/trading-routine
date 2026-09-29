# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-29 (pre_market)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | **NO QUALIFYING CANDIDATES** — no tradeable name (universe + active watchlist) carries a fresh (last-30-day) fundamentals signal clearing the ELEVATED_BAR >20%-EPS-all-sectors bar with clean positive PEAD drift. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash) — no positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — | (no open positions) |

## Notes

**Run context (2026-09-29, pre_market):**
- **Book:** FLAT — 0/8 positions, 100% cash. Reconciliation PASS (Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT; account ACTIVE, trading_blocked=false; equity $96,448.31, cash $96,448.31, buying_power $385,793.24). Last exit DELL −8% hard stop 2026-09-24.
- **DRY_RUN:** false.
- **Regime (strategy.md SPY-200MA gate):** BULL — SPY 771.35 > 200MA 714.84 (per pead_health.md, computed 2026-09-27). Standard regime thresholds apply; regime gate not tightening.
- **PEAD signal-health overlay (pead_health.md, computed 2026-09-27, expires 2026-10-04 — FRESH):** posture = **ELEVATED_BAR** (realized_health_60d_pct = **−0.32%**, health_sample_n = **394**, threshold 0.0, health_ok=false). Per pre_market step 1c: EPS-surprise bar raised to **>20% for ALL sectors** and **max new positions capped at 2** for this session. Overlay governs NEW entries only — never exits, tighten-only. Not stale.
- **Macro deferral rule (strategy.md):** NOT triggered — SPY futures ~+0.17% premarket (not down >0.4%). (Moot anyway; ELEVATED_BAR already imposes the >20% bar.)
- **Universe cache:** FRESH — screened 2026-09-27, expires 2026-10-04, 250 tickers. Read-only; not re-screened (universe_refresh owns that).
- **Weekly new-position slots:** 0/2 used (ELEVATED_BAR cap). Last fill DELL 2026-09-17 (prior week), exited 2026-09-24.

**Overnight news sweep + candidate screen (why 0 buys):**
Late-September pre-Q3-earnings lull continues — most S&P 1500 names next report mid-to-late October. Fresh (last-30-day) earnings catalysts screened this session and rejected at the >20% EPS gate before deep research (a–i):
- **KBH** (KB Home, Consumer Disc) — Q3 EPS $1.05 vs $0.89 = **+18.0% surprise → FAILS >20% ELEVATED_BAR bar**; also cut Q4 margin outlook and shares slipped after-hours (negative PEAD reaction). Also NOT in the current universe cache → not tradeable. Drop.
- **CTAS** (Cintas) — adj EPS $1.39 vs $1.36 = **+2.2%** (raised guide) → far below bar; not in universe cache. Drop.
- **PAYX** (Paychex) — adj EPS $1.34 vs $1.32 = **+1.5%** → far below bar; not in universe cache. Drop.
- **DRI** (Darden) — Q1 FY27 EPS $2.05 vs $2.05 = **in-line, no beat**; not in universe cache. Drop.
- **MU** (Micron, IT, in universe) — reports **2026-09-30 AMC** → inside the 3-day earnings window (event risk). Excluded regardless.
- **JBL / ACN** — report this week (Sep 30 / this week); no clean post-earnings drift to act on yet. Excluded.
- **MRVL** (IT/semis; in universe AND active watchlist) — last earnings ~2026-08-28 (**outside the 30-day fundamentals window**); only fresh item is a thin single-firm analyst initiation (Seaport Buy, Sep 21). No fresh >20% earnings catalyst and no clean new PEAD drift leg — does not reach a qualifying score. Would also require the mandatory BIS export-control scan (step h.ii) as a semiconductor. Drop.
- Big movers **SNOW (+20%, Sep 2)** and **OKTA (+17%, Aug 26)** are on the watchlist as **status: pending_review (non-active)** → human-only to activate; pre_market MUST NOT plan them. **Tilly's (+31%), ChargePoint (+16%)** are not in universe or watchlist and are not compelling for this strategy (micro/thin, sub-20% or non-qualifying) → no watchlist additions.

**Regulatory scans (step h):** none reached deep research (no candidate cleared the EPS gate) — no shelf-registration / BIS flags to record.

**Watchlist flags:** none added this session (no new compelling non-universe, non-watchlist catalyst).

**Conclusion:** 0 planned buys, 0 planned sells, 0 trailing conversions. Not lowering the bar (pre_market rule: if <3 candidates score ≥6/10, plan fewer buys rather than loosen). ELEVATED_BAR + pre-Q3 lull → disciplined flat/cash hold consistent with recent sessions. `market_open` should take NO ACTIONS on this plan.
