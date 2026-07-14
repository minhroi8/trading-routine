# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-14 (pre_market ~08:10 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 qualifiers scored ≥6/10 with complete research — see Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8 positions, 100% cash) — nothing to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Book FLAT — no open positions, no stops to convert. |

## Notes

**NO ORDERS PLANNED — 0 qualifiers after full screen. Book FLAT (0/8, 100% cash).**

**Gates (all PASS):**
- Clock: `is_open=false`, `next_open=2026-07-14T09:30 ET` — market opens today (Tue), not a holiday → proceed.
- Reconciliation 0/0 PASS: Alpaca `/v2/positions=[]` matches portfolio.md FLAT book — zero divergence. Account ACTIVE, equity $98,266.98, cash 100%.
- Universe FRESH: `expires_on 2026-07-19` > today (rebuilt Jul 12, 305 tickers passed).
- **PEAD health STALE** (`expires_on 2026-06-28` < today) → per step 1c a stale overlay is treated **NORMAL, bar NOT raised** (the universe-cache gate is the hard halt and it PASSES). Standard 15% EPS threshold in effect. ⚠️ 5th+ consecutive PEAD_HEALTH_REFRESH_MISS (Jul 12 universe_refresh rebuilt universe.md but did not recompute pead_health.md — known yfinance-vs-proxy transport bug; needs human fix).
- SPY regime: **BULL** (close $749.13 [Jul 13 IEX] > 200MA $694.88, n=200, +7.81%). Standard thresholds: EPS >15% (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also need streak≥2), max 5 new/week, no ELEVATED_BAR cap.
- Macro: premarket S&P 500 ~−0.06% (Nasdaq +0.61%, Dow −0.63% on Mideast/oil headlines); 10-yr not at a multi-month high → **macro-deferral rule NOT triggered**.

**Candidate screen (Q2 earnings season week 1 — big banks reported THIS MORNING; mega-cap tech Jul 22–30):**
- **GS** (Financials, Q2 reported today Jul 14 BMO): adj EPS $20.98 vs $14.48 = **+44.9% beat**, rev $20.34B vs $16.13B = +26.1% beat, +1.4% premkt — fundamentally the standout, clears 15% bar easily. **DROP — incomplete research:** reported this morning → **0 post-earnings trading days** → steps e (announcement-day volume ratio), f (5-day RS vs SPY drift), i-ii (earnings-day gap) are NOT computable with real data (incomplete a–i = automatic DQ). Also a same-day "buy the pop" is not confirmed PEAD drift. **Strong WATCH** for a later pre_market once drift establishes (already in universe — no watchlist flag needed). Shelf-reg: N/A (large-cap bank); BIS: N/A.
- **WFC** (Financials, today): $2.00 vs $1.72 = +16.3% beat, rev +3.6%; muted/negative reaction (−1% premkt) → same incomplete-research DROP + weak signal.
- **JPM** (+5% beat) / **BAC** (+7% beat): fail the 15% EPS bar outright, reported today → DROP.
- **MU** (IT, Q3 Jun 24, 20d in-window): strong beat (rev $41.46B vs $35.84B est) but **NEGATIVE drift** — stopped −8.08% Jun 25 (~$1,148), now $979 = down ~15% since; Jul 7 closed −4.7% on semi rotation (the Jul 8 +7% was a $3B capex announcement, not earnings drift) → broken PEAD, DROP step f. Consensus PT ~$1,264 (stock below it). Next earnings ~Sep.
- **DAL** (Industrials, Jul 10): EPS $1.56 vs ~$1.51 = ~3–5% beat → DROP (Industrials requires >20% AND streak≥2).
- **PEP** (Consumer Staples, Jul 9): core EPS $2.20 vs $2.19–2.21 = ~in-line (+0.5%/−0.45%); the +125% op-profit headline is a base-effect optic → DROP (Staples needs >20%).
- **MRVL** (watchlist `active`, in universe): no fresh in-window earnings (Q1 FY27 ~May 27 = ~48d stale), trades above consensus mean PT → DROP step g (carried); status stays `active` (human-only).
- **WDFC** (WD-40, watchlist `pending_review`): Q3 Jul 9 +48% beat, but status is **pending_review** → MUST NOT plan a trade (human-only to set `active`). Already on watchlist — no new flag.
- IBM (−20%, preliminary miss), AAPL (KeyBanc downgrade), IONS (−24% trial miss) — non-candidates.

**Result:** 0 candidates scored ≥6/10 with complete research → plan zero buys (do not lower the bar). Weekly new-position slots 0/5. Sector exposure: none (100% cash). DRY_RUN: false.
