# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-08 (pre_market, ~08:12 ET) — **NO ORDERS PLANNED (0 qualifiers).**

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the eligibility gate (a fresh, in-window ≤30d earnings beat from a universe or active-watchlist name). Q1/Q2 earnings desert — Q2 season ramps next week (PEP Jul 9, DAL Jul 10, banks Jul 14–15, mega-cap tech Jul 22–30). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8 positions, 100% cash) — no positions to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Book FLAT — no positions to convert. |

## Notes

- **Gates (all PASS):** clock `next_open=2026-07-08T09:30 ET` = today (Wed), not a holiday → routine proceeds. **RECONCILIATION 0/0 PASS** — Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT book, zero divergence. Universe cache FRESH (`expires_on 2026-07-12` > today; screened 2026-07-05, 313 tickers). Account ACTIVE, trading_blocked=false, equity $98,266.98, cash $98,266.98 (100%), buying_power $393,067.92; 0 open orders (no orphan stops, book clean).
- **PEAD health overlay: STALE** — `pead_health.md` `expires_on 2026-06-28` < today 2026-07-08. Per pre_market step 1c, a stale overlay is treated as **posture NORMAL but flagged STALE — bar NOT raised** (the universe-cache freshness gate is the hard halt and it PASSES). Last reading was ELEVATED_BAR (realized −0.492%, n=367, computed 2026-06-21). ⚠️ Recurring **partial universe_refresh anomaly**: the Jul 5 refresh rebuilt universe.md (expires Jul 12) but did NOT recompute pead_health.md (still computed_on Jun 21 / expires Jun 28) — root cause diagnosed in the Jul 5 research_log entry (yfinance curl_cffi-vs-proxy transport failure + Yahoo HTTP 429 on the shared egress IP). Surfaced for human; flagged in Discord.
- **SPY regime: BULL** — close $747.77 (Jul 7 IEX dailyBar.c) > 200MA $693.16 (n=200), margin +$54.61 (+7.88%). Standard `strategy.md` thresholds in effect: EPS surprise >15% (>20% for Utilities/Real Estate/Industrials/Energy; Industrials/Energy also need streak≥2), max 5 new positions/week, no ELEVATED_BAR cap.
- **Macro:** deferral rule NOT triggered. 10-yr Treasury ~4.50% (Jul 7) — NOT at a multi-month high (peak ~4.70% May 20), so that leg fails regardless of futures (BOTH legs required). Prior session (Jul 7) closed firm (S&P 500 +0.72%, Nasdaq +1.12%) but the semiconductor complex is soft (Samsung Q2 disappointment Jul 7; MU/SNDK −4%, NVDA −1.5% on reports of Chinese firms adopting domestic chip alternatives). Fed minutes due this week.
- **Screen — 0 qualifiers (earnings desert):**
  - **LEVI** — reports today Jul 8 AC (after close): not in universe/watchlist AND inside the 3-day earnings window; nothing has reported yet, so no post-earnings drift signal exists. Ineligible.
  - **PEP** (Consumer Staples) — reports Jul 9 (tomorrow): has not reported yet (no fresh drift) AND inside the 3-day window. Blocked. (Would need >20% Staples bar post-print.)
  - **DAL** (Industrials) — reports Jul 10: has not reported yet AND inside the 3-day window. Blocked. (Industrials needs >20% + streak≥2 post-print.)
  - **MU** (IT, Q3 FY2026 Jun 24 +23.8% beat, 7-q streak, Q4 raise $50B/$31, $100B floor-priced backlog, BIS clean) — still within the 30-day window (14d) and fundamentally strongest, but **DROP on the risk leg (steps f + g, carried, decisively):** drift rolled over hard (−19.8% off the $1,215 peak to $975.40 per the Jul 7 log) and the mandatory fixed −8% stop sits well INSIDE MU's ±6–11% daily range → near-certain mechanical noise-stopout — the EXACT failure realized same-day Jun 25 (−8.08%, thesis intact, held 0 trading days). Fresh chip-complex pressure (Samsung, China domestic-chip adoption) compounds the risk. Next earnings ~Sep 22–29 (not within 3d). Live instance of the lessons.md volatility-scaled-stop proposal — flagged for human.
  - **MRVL** (watchlist `active`, in universe) — **DROP:** Q1 FY2027 earnings ~May 27 now ~42 days stale (>30-day window); still trades above consensus mean PT (step-g overshoot, carried). Status stays `active` (human-only).
  - **Overnight movers, none eligible:** CRNX +99% (Vertex all-cash buyout = merger-arb, at deal price, non-universe); RIVN −10% (secondary share offering = dilution, non-universe); FISV +5% (network-purchase M&A rumor — speculative, not a fresh in-window earnings beat); IBM +3% (BofA PT hike — a lone analyst PT bump; last earnings ~Apr is stale and next earnings ~Jul 22 is event risk; thin, low-conviction → no full a–i qualifier); TSLA (Q2 deliveries beat ~18% — a delivery number, NOT an EPS beat; actual Q2 earnings ~late July is a binary event within the hold horizon; MS kept Equal Weight → not a qualifying PEAD signal). The "3 companies raising guidance" (UNH/DGX/PWR) article is dated **May 7, 2026** — Q1 reports, >60d stale, not in-window.
  - **No compelling non-universe catalyst** fit the fundamentals-swing/PEAD framework (all M&A / dilution / binary-event / delivery-number), so **no watchlist `pending_review` add.**
- **Sanity check (step 6):** cash floor 100% ≥ 10% ✓; max concurrent 0 ≤ 8 ✓; new-per-week 0 ≤ 5 ✓ (BULL cap; weekly slots reset Mon Jul 6); sector caps N/A (no positions). No trims needed.
- **DRY_RUN: false.**
