# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-24 (Friday) — drafted by `pre_market`. Book FLAT (0/8, 100% cash).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none — 0 qualifiers)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none — book FLAT, no positions)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none — book FLAT)_ | — | — | — | — | — |

## Notes

**5th consecutive 0-qualifier day (Jul 20 / 21 / 22 / 23 / 24).** No buys, no sells, no conversions. Book remains FLAT (0/8 positions, 100% cash) — unchanged since the MU −8% mechanical stop Jun 25.

**Gates (all PASS):**
- Clock: `is_open=false` @08:13 ET, `next_open=2026-07-24T09:30 ET` (today) → normal pre-market run.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT book — zero divergence.
- Universe cache FRESH (`expires_on 2026-07-26`, 306 tickers, screened 2026-07-19).
- PEAD health FRESH & **NORMAL** (`computed_on 2026-07-19`, `expires 2026-07-26`; `realized_health_60d +1.225%`, `n=318`, `health_ok=true`) → standard `strategy.md` thresholds, no raised bar, no cap.
- Regime **BULL**: SPY Jul 23 close $738.06 > 200-day MA $698.18 (+5.7%) [data.alpaca.markets IEX, 200-bar window]. Standard thresholds; max 5 new positions/week.
- Account: equity $98,266.98, cash $98,266.98 (100%), buying_power $393,067.92. ACTIVE, trading_blocked=false. 0/5 weekly new-position slots used (last actual fill MU Jun 25). DRY_RUN: **false**.

**Candidate screen — Q2-2026 season, this week's fresh reporters:**
- **INTC (Information Technology, large — in universe) — STANDOUT CATALYST, DEFERRED (not dropped).** Q2-2026 reported **Jul 23 after market close**: non-GAAP EPS **$0.42 vs $0.21 est = ~+100% surprise** (doubled), revenue **$16.1B vs $14.42B (+11.6% beat, +25% YoY** — fastest growth since ~2011), swung to GAAP profit YoY, **Q3 guide raised** (EPS $0.38 vs $0.27 est; rev $15.8–16.8B vs $15.1B est). Stock +13% after-hours. Easily clears the 15% IT EPS-surprise bar on signal quality. **Deferred because it reported only last night — today (Jul 24) is day-0 post-earnings, so the drift-confirmation steps of the deep-research protocol cannot be computed: step e (reaction-day volume ÷ 20d avg — reaction day is TODAY, not yet complete), step f (5-day relative strength vs SPY since earnings — ZERO completed post-earnings sessions), step i.ii (earnings-day open gap — today's open hasn't printed). Per the protocol, an incomplete a–i = automatic disqualification for today.** This also matches the strategy's own PEAD entry cadence ("buy +2 days after the beat" on confirmed drift, not into the day-0/day-1 pop). **→ #1 priority for Monday Jul 27 pre_market**, when Jul 24 (reaction) and Jul 27 sessions supply drift data. NOTE for Monday's full research: INTC carries two step-h risk areas that MUST be cleared before any entry — (h.i) dilution history (2025 US-government equity stake, SoftBank/other strategic issuances — check for any active S-3 / offering in the trailing 30d) and (h.ii) BIS export-control / China exposure (semiconductor — check for fresh rule changes/entity-list actions in the trailing 30d).
- **RTX (Industrials / Aerospace-Defense) — DROP.** Q2-2026 (Jul 23) adj EPS $1.89 vs $1.66 = **+13.9% surprise**; guide raised. Industrials requires **>20% AND streak ≥2** — 13.9% < 20% bar → drop.
- **LMT (Industrials / Aerospace-Defense) — DROP.** Q2-2026 (Jul 23) EPS $7.94 vs $7.22 = **+9.97% surprise**; guide raised. Below >20% Industrials bar → drop.
- **MMM (Industrials) — DROP.** Q2-2026 (Jul 21) EPS $2.40 vs $2.27 = **+6.8% surprise**; guide raised. Below >20% Industrials bar → drop.
- **GM (Consumer Discretionary) — DROP** (carried from Jul 23 screen): Q2-2026 (Jul 21) adj EPS $3.57 vs $3.20 = +11.6% < 15% Cons Disc bar.
- **GOOGL (Communication Services) — DROP:** beat Q2 but shares fell on the 2026 capex hike to $195–205B → broken post-earnings drift (step f fail).
- **AXP (Financials) — no data:** reports **today Jul 24 pre-open** (not yet released; consensus $4.40, Earnings ESP only ~+0.6% → small expected surprise, likely sub-15%). Zero post-earnings data and reports intraday → not researchable this session.

**Regulatory flags:** none acted on (no candidate advanced to a planned buy). INTC's dilution/export-control checks are deferred to Monday's full research (see above).

**Watchlist flags:** none added. INTC is already a universe member (no watchlist row needed). MRVL (active) — no fresh 30d catalyst (Computex spike was June; next earnings ~late Aug) → not shortlisted. WDFC (pending_review) — human-only to activate, not traded. No compelling catalyst appeared for any ticker outside universe+watchlist this session.

**SYF (Synchrony) coverage-gap reminder (carried):** S&P 500 member with a clean Q2 +24.5% beat + raised outlook, but ABSENT from the universe.md 306-ticker cache (screened 2026-07-19). pre_market MUST NOT re-screen and MUST NOT add an index member to the (non-S&P-1500) watchlist → still flagged for the next Sunday `universe_refresh` to fix coverage.

**Sanity check:** no buys to size → cash floor (100% > 10% ✓), max concurrent (0/8 ✓), weekly new (0/5 ✓), sector cap (n/a) all trivially satisfied. Nothing to trim.
