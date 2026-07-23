# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-23 (pre_market ~08:15 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 qualifiers — see Notes |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — nothing to sell |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**NO TRADES for 2026-07-23 — 0 qualifiers (4th consecutive 0-qualifier day: Jul 20/21/22/23).** Book stays FLAT (0/8, 100% cash, equity $98,266.98).

**Gates (all PASS):**
- Clock: `is_open=false` at 08:14 ET but `next_open=2026-07-23T09:30 ET` = today → normal pre-market run (not a holiday). Proceed.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions` = [] MATCHES portfolio.md FLAT book. Zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false.
- Universe cache FRESH: `expires_on 2026-07-26` ≥ today; 306 tickers.
- PEAD health FRESH & **NORMAL**: `pead_health.md` computed_on 2026-07-19, expires 2026-07-26; realized_health_60d +1.225%, n=318, health_ok=true → standard `strategy.md` thresholds (no ELEVATED_BAR).
- Regime **BULL**: SPY 743.29 > 200MA 693.44 (+7.2%, per pead_health.md Jul 19; huge cushion, unchanged) → standard thresholds, max 5 new/week.

**Thresholds in effect this session:** standard `strategy.md` — 15% EPS surprise (all sectors) except >20% for Utilities/Real Estate, and >20% + streak≥2 for Industrials/Energy. Max new positions 5/week (0/5 used this week).

**Candidates screened and DROPPED (Q2-2026 earnings tape):**
- **SMCI** (IT, in universe) — Jul 22 preliminary Q4'26 business update: gross margins 15–17% vs prior guide 8.2–8.4% (huge beat), >$60B new orders / record backlog; stock +19.8% to $30.56. Genuinely compelling catalyst, BUT **DROPPED on step h (regulatory scan) + step g (risk)**: (1) DILUTION RISK — active S-3 shelf registration filed Jun 9 2026 (mixed shelf, undisclosed amount) + $7.0B equity/equity-linked financing announced Jun 9 ($5B underwritten + $2B ATM) + large 2029/2030 convertible tranches; step h mandates an automatic drop on an active shelf or recent offering. (2) EXPORT-CONTROL RISK — DOJ indictment (Mar 19 2026) of three SMCI-associated individuals for export-control violation conspiracy. (3) Accounting risk — ongoing SEC investigation, DOJ subpoenas, EY auditor resignation over internal-control weaknesses, forensic-accounting review engaged Apr 2026, securities-fraud class actions. Any one is thesis-breaking within 42d. Also revenue only near low end ($11B of $11–12.5B) and full report (with unresolved accounting) due Aug 11. **Automatic disqualification.**
- **GM** (Consumer Disc, in universe) — Q2 rep Jul 21: adj EPS $3.57 vs $3.20 = **+11.6% < 15% standard bar** → DROP. (Guidance raised twice, 16th straight beat, but earnings-driven entry must clear 15%; not exempt.)
- **EQT** (Energy, in universe) — Q2 rep Jul 21: adj EPS $0.39 vs $0.42 = **EPS MISS** (rev small beat, raised volume guide). Energy requires >20% surprise + streak≥2; a miss fails outright → DROP.
- **DHR** (Danaher, Health Care) — Q2 rep Jul 21: EPS $1.94 vs $1.84 = +5.4% beat but stock **FELL −13.7%** on weak Q3 revenue guidance (broken drift, step f) → DROP.
- **INTC** (IT, in universe) — reports **today Jul 23 after close** = inside 3-day earnings window (event risk, no drift) → DROP.
- **RTX, LMT** (Industrials, in universe) — report today Jul 23; not yet reported; Industrials gated (>20%+streak≥2) → not shortlisted.
- **WDC** (IT, in universe) — has NOT reported (next Aug 5); Jul 22 tape move was sympathy/pre-earnings, not an earnings catalyst; last report Apr 30 (>30d) → no fresh 30-day signal → DROP.
- **AT&T** (+10.2% beat), **Novartis** (+12.1% core beat, foreign ADR — US-primary-listing rule excludes), **3M/MMM** (Industrials, raised guide but not in universe), **HAS** (+10%, not in universe), **SYF** (Synchrony, +24.5% beat + raised 2026 EPS outlook — see universe-gap note below).
- **MRVL** (watchlist, active) — no fresh qualifying catalyst in last 30d (Computex/endorsement spike was June); dropped repeatedly in prior runs on step g (trades above consensus PT); next earnings ~late Aug → not shortlisted.
- **WDFC** (watchlist, pending_review) — human-only to activate; NOT traded.

**Universe-coverage observation (for `universe_refresh` / human — NOT a trade and NOT a watchlist add):** **SYF (Synchrony Financial)** posted the cleanest large beat of the week — Q2 adj EPS $2.59 vs consensus, a **+24.5% surprise**, AND raised its 2026 EPS outlook (Financials, clears the 15% bar). SYF is a confirmed **S&P 500** member, so it belongs in the *universe*, yet it is absent from the 306-ticker `universe.md` cache (screened_on 2026-07-19). Pre_market MUST NOT re-screen the universe, and the watchlist is scoped to *non*-S&P-1500 names only — so SYF is intentionally NOT added to the watchlist (that would miscategorize an index member). Flagging the cache gap so `universe_refresh` can confirm SYF's inclusion next Sunday. No watchlist additions this session.

**Sanity check vs strategy.md:** N/A (no buys). Cash 100% ≥ 10% floor ✓; 0/8 concurrent ≤ 8 ✓; 0/5 new-this-week ≤ 5 ✓; no sector exposure ✓.
