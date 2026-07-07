# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-07 (pre_market) — **NO ORDERS PLANNED**

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the screen — see Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — nothing to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Book FLAT — no positions to trail. |

## Notes

**Gates (all PASS):** clock `next_open`=2026-07-07T09:30 ET = **today** (Tue, not a holiday) ✓; **RECONCILIATION 0/0 PASS** (Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT book — zero divergence) ✓; universe.md `expires_on` 2026-07-12 > today → **FRESH** ✓; account ACTIVE, trading_blocked=false, equity **$98,266.98** (100% cash, buying_power $393,067.92). No open orders (`status=open`=0 — no orphan stops, book clean).

**PEAD health overlay: STALE.** `pead_health.md` `expires_on` 2026-06-28 < today → per pre_market step 1c, treat posture as **NORMAL but flagged STALE** — bar NOT raised (the universe-cache freshness gate is the hard halt and it PASSES; universe fresh to 2026-07-12). Recurring partial-`universe_refresh` anomaly (PEAD overlay not recomputed since Jun 21; Jul 5 refresh MISS = yfinance curl_cffi-vs-proxy transport failure + Yahoo HTTP 429 on the shared egress IP — diagnosed in the Jul 5 research_log). **Standard `strategy.md` thresholds apply: 15% EPS (20% for Utilities/RealEstate/Industrials/Energy), weekly cap 5.**

**Regime: BULL.** SPY close $744.86 (Jul 2 IEX dailyBar.c) > 200MA **$692.26**, +7.60%. Standard operation.

**Macro deferral: NOT triggered.** 10-yr yield ~4.45–4.50% (a two-week high, NOT a multi-month high) and S&P futures not down >0.4% — both legs are required and neither is met.

**Why 0 buys — Q1/Q2 earnings desert.** Q2 season unofficial start is later this week (PEP Jul 9, DAL Jul 10, banks Jul 14–15, mega-cap tech Jul 22–30), so there are no fresh in-window post-earnings-drift setups yet. The overnight movers were all non-earnings catalysts and were dropped:

- **LRCX / AMAT / KLAC** (all IT/semi, in universe) — Morgan Stanley PT hikes today. Analyst-revision catalyst (EPS-exempt), BUT last earnings ~late-April = **70+ days stale** (next: LRCX Jul 29, KLA Jul 30) → **no fresh post-earnings drift to ride**; the deep-research steps a–i are earnings-drift-anchored and cannot be legitimately completed without a fresh earnings event → **auto-DQ** per routine. Also extended (+~4% premarket on the upgrade) and in the exact volatile semi sector that same-day stopped out MU Jun 25. **DROP.**
- **IBM** (in universe) — BofA PT $330 (analyst revision), earnings Jul 22 (outside 3-day window, but no fresh beat). Low conviction, no drift signal. **DROP.**
- **MU** (in universe) — drift rolled over −19.8% off the $1,215 peak to $975.40, still chopping ±6–11%/day; its fixed −8% stop sits inside that ATR range — the exact failure that stopped it out same-day Jun 25. **DROP (risk leg).**
- **MRVL** (watchlist, active) — earnings May 27 = **41 days stale**; trades above consensus mean PT (step-g overshoot). No fresh signal. **DROP.**

**Regulatory scan:** N/A — no candidate advanced to full a–i scoring, so no shelf-registration or BIS export-control flags were opened. (Had any semi qualified, step h.ii BIS scan would have been mandatory.)

**Non-universe overnight catalysts (noted, NOT added to watchlist — none fit the fundamentals-swing PEAD framework):**
- **CRNX** +99% — Vertex all-cash $85 buyout; already at deal price → merger-arb, not a swing thesis. Skip.
- **WULF (TeraWulf)** +16% — 20-yr Anthropic data-center deal (~$19B). Real catalyst but a speculative crypto-miner, not S&P 1500, doesn't fit US-cash-equity fundamentals-swing discipline. Noted, not flagged.
- **VERA** +6% — into a Jul-7 PDUFA decision; binary FDA event = precisely the event risk `strategy.md` avoids. Skip.

**Watchlist flags:** none added this session.

**Sanity check:** N/A (0 planned buys). Cash floor 100% ≥ 10% ✓; concurrent 0/8 ≤ 8 ✓; weekly new 0/5 ≤ 5 ✓; no sector exposure. Leaving the book FLAT is the correct posture through the earnings desert — the next fresh in-window beats arrive with Q2 season later this week.
