# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-24 (pre_market ~07:17 ET, Tue)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none — book FLAT, 0 positions)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

**Outcome: 0 planned buys, 0 planned sells. No candidate scored ≥6/10 under the session's raised bar.** market_open 2026-11-24 has NO actions to execute (flat book, no plan rows).

### Account / reconciliation
- Book **FLAT** (0/8 positions, 100% cash). Equity **$94,946.98**, cash $94,946.98, buying_power $379,787.92, long_mv $0. Account ACTIVE, trading_blocked=false, account_blocked=false.
- **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md (0 active rows; the only table row, VRT, is inside an HTML comment — closed −8% hard stop 2026-11-02). `/v2/orders?status=open`=[] (no orphan stops).
- Gates: `/v2/clock` is_open=false (pre-market), next_open 2026-11-24T09:30 ET → opens TODAY, not a holiday → proceed. Universe cache **FRESH** (338 rows, screened 2026-11-22, expires 2026-11-29) → no re-screen.

### Regime / posture (new-entry bar for THIS session)
- **PEAD posture: ELEVATED_BAR + FRESH** (pead_health.md computed 2026-11-22, expires 2026-11-29). `realized_health_60d_pct` = **−3.468%**, `health_sample_n` = **175**, health_ok=false → realized PEAD drift edge is NOT paying.
- **Regime: BEAR** — SPY < 200-day MA (pead_health.md: spy_close $689.81 < 200MA $730.29; SPY has since rallied but Nov-23 close $722.56 remains < 200MA).
- Combined effect (take the stricter): **EPS-surprise bar raised to >20% for ALL sectors; max new positions capped at 2 for the session.** Overlay governs NEW ENTRIES only; never halts, never affects exits.
- Macro-deferral rule: MOOT (>20% bar already enforced; SPY +4.6% on Nov-23 — not a stressed-futures day).
- Weekly new-position count: **0/2** used this week (last actual buy VRT 2026-10-29, stopped −8% 2026-11-02).
- DRY_RUN: **false**.

### Screen result — why nothing qualified
Overnight/last-30d earnings sweep over universe + active watchlist (only MRVL active). Under the >20%-all-sectors EPS bar, **no in-universe name clears the threshold with a positive post-earnings drift**:
- **CEG** (Constellation, Utilities) — reported Nov-9; adj op EPS $5.06 vs ~$3.88 consensus = **+30% surprise (clears >20%)**, FY guide raised 2nd time. **DROPPED on step f (relative strength / drift):** post-earnings close Nov-9 $276.22 → Nov-23 $251.66 = **−8.9%**, vs SPY −4.0% over the same window → **underperformed SPY ≈ −4.9pp**; the +30% pop fully round-tripped (now below the pre-report $249.77). Reaction muted/negative (AI-datacenter debt concerns; one-time drivers — PJM capacity prices, Calpine, nuclear output; biggest contract wins ramp post-2028; mgmt warned outperformance may not repeat). Failed-drift PEAD → cannot score ≥6.
- **APP** (AppLovin) — Q3 (~Nov-5): GAAP EPS surprise **+6.6%** / adj +4.6% (rev +55% YoY, stock +~25% on guide + $3.2B buyback). Fails >20% EPS bar (earnings-driven entry). Risk flag: new securities class action filed 2026-09-16 (alleged misleading ad-model disclosures). DROP.
- **IDXX** (Idexx, Health Care) — Q3 (Nov-2, 22d stale): EPS surprise **~+8%** (beat-and-raise, 3rd raise), but lowered op-margin outlook + CoVet dilution; modest +2.6% reaction. Fails >20% bar. DROP.
- Sub-bar beats (all < 20% EPS surprise, DROP): **ROST** +2.7%, **Agilent (A)** +8% (incl. tariff-refund benefit), **Keysight (KEYS)** +7%, **NVDA** ~+7%, **WMT** +1.5%, **TGT/LOW/TJX** modest.
- Big >20% movers screened out as **outside universe** (small/mid, not S&P-1500 cache): ZIP, TTEC, CRWV, CARL, REED, Gap, Astera/ALAB. None are swing-trade quality OR had an EPS beat (CRWV/RKLB missed EPS; ALAB sector rebound; Gap cut guidance). No new watchlist add warranted.
- **MRVL** (only active watchlist ticker) — reports Q3 FY2027 on **2026-12-01** (company-confirmed); last beat (~Aug) is >30d old → no ≤30-day catalyst, and entering now sits 7 days ahead of a binary earnings event. Not plannable.
- **REGN** — cemdisiran gMG PDUFA target action date in Nov-2026 = imminent binary FDA event risk; analyst ratings split (one firm Sell, PT $680). Not a clean positive-revision catalyst under event risk. DROP.

Per MUST-NOT: a candidate cannot score ≥6 without completing all of steps a–i; CEG was the only name to clear the >20% EPS gate and it failed the drift/RS leg (step f) before reaching the earnings-date (step 4) / halt (step 4b) re-verification, so those shortlist-only checks were not needed.

### Regulatory flags
None reached a plannable score. (APP securities litigation noted as a drop reason; no shelf-registration / BIS export-control flags triggered on a scored candidate.)

### Watchlist flags
None added this session. Every >20%-ish beat screened was either already an in-universe constituent or a non-universe small-cap that did not meet swing-trade/catalyst quality for a `pending_review` add.

### Carry-forward housekeeping (human)
- `memory/portfolio.md` bloat (~492KB of accumulated HTML-comment audit logs, exceeds single-read limit) — recurring human-trim flag (deleting audit history needs human sign-off; not auto-trimmed).
- Doc discrepancy: `routines/pre_market.md` line 99 says sizing "(currently 11%)" vs `strategy.md` Max position size = **20%** — strategy.md wins per CLAUDE.md; moot today (0 buys).
- `trade_log.md` VRT buy/sell rows carry `commit_sha <pending>` — flagged for human backfill.
- Log rotation DEFERRED to market_close (pre_market appends only); research_log has 2× rows dated 2026-11-09 now >14d old for market_close to archive.
