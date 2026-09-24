# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-24 (pre_market ~08:2x ET, Thu)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the ≥6/10 bar under the ELEVATED_BAR >20%-EPS-all-sectors threshold. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | DELL held — thesis intact, no exit criterion fired (see Notes). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | DELL far below +10% partial-lock trigger ($635.72); no conversion. |

## Notes

- **DRY_RUN: false.**
- **Gates:** Gate 1 clock `is_open=false`, `next_open=2026-09-24T09:30 ET` → opens today, NOT a holiday → proceed. **RECONCILIATION 1/1 PASS** — Alpaca `/v2/positions` = DELL 19 @ $577.93 avg MATCHES portfolio.md; sole open order = −8% hard stop `3837d86d` (sell 19 @ $531.70 GTC, status new), no orphans; zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false. Equity **$96,601.45**, cash $86,347.34 (89.4%), long_mv $10,254.11, bp $374,100.87; DELL cur $539.69, unrealized −$726.56 / −6.62%.
- **Universe FRESH** (screened 2026-09-20, expires 2026-09-27, 244 rows) → freshness gate PASSES; no re-screen.
- **PEAD health FRESH + ELEVATED_BAR** (computed 2026-09-20, expires 2026-09-27; `realized_health_60d_pct` **−0.337%**, `health_sample_n` **370**, health_ok=false). Per step 1c: **EPS-surprise bar RAISED to >20% for ALL sectors** and **max new positions capped at 2** for this session. Overlay tightens only; governs new entries only.
- **SPY regime: BULL** — stored `spy_above_200ma=true` (SPY $761.69 > 200MA $712.48 per pead_health frontmatter; strategy.md regime gate reads this file). Bear-regime rule NOT active. Combined with ELEVATED_BAR, stricter cap (2) governs.
- **MACRO-DEFERRAL TRIGGERED (both legs):** Sep-24 premkt S&P futures **−0.6%** (>0.4%-down leg MET; Nasdaq-100 futures −1%) AND 10-yr **~5.15% = highest since 2007** (multi-month-high leg MET) → also raises EPS bar to >20% all sectors. Moot — already at >20% via ELEVATED_BAR. Reinforces the higher-conviction-only posture on a soaring-yields, risk-off tape.
- **Candidates → 0 plannable ≥6/10:**
  - **DELL** — already held (not a new-buy candidate). Thesis INTACT (raised FY27 guide ~$192B rev / ~$25.50 adj EPS, $60.9B AI orders, record ~$95B backlog, Buy consensus PT $581.38, no guidance cut/fraud/negative catalyst overnight). No exit criterion fired: −8% stop $531.70 NOT hit (cur $539.69, ~1.5% cushion — flagged for market_open/midday to watch), +10% partial-lock $635.72 NOT hit, held 7 days (not 60d), thesis not broken. → carried with −8% hard stop; NO planned sell.
  - **DROP — MRVL (active watchlist, IT/semiconductor):** no fresh ≤30d earnings catalyst. Last print Aug-27 sold-the-news (~0% surprise). Current items = MS PT raise to $268 (Sep-21) ahead of Oct-6 Investor Day + Microsoft/Utimaco $5B cloud-payment push (Sep-17) + 2nm optical-interconnect demos = analyst/partnership/conference momentum, NOT a >20% EPS beat. Next earnings Nov-26. Fails the earnings-catalyst requirement (consistent with every prior session's MRVL drop).
  - **NOT a candidate — MU (Micron, universe, IT/semiconductor):** no fresh beat — reports fiscal Q4 **Sep-30** (6 days away, >3d so not the 3-day-window DQ, but an upcoming binary event inside a days-to-weeks hold; the only "catalyst" is pre-earnings analyst PT hikes = anticipatory momentum, not PEAD). Parabolic at ~ATH. Dropped.
  - **DROP — CTAS (Cintas, NOT in universe/watchlist):** reported Sep-23, adj EPS $1.39 vs $1.35 = **+3.0% surprise** ≪ 20% bar (even ≪ standard 15%); rev +1.0% beat; FY27 guide ~in-line; stock FELL ~1.2% premkt → negative reaction. Not in universe → cannot plan anyway. Not watchlisted (sub-bar, no compelling catalyst).
  - Off-cycle reporters this/next week (ACN, NKE, FDX, KMX, CCL, LEN) are UPCOMING (not fresh beats) and/or historically single-digit surprises that cannot clear the >20% bar; FDX/ACN also near/inside their earnings windows. None shortlisted.
- **Overnight sweep:** Q2 season over; Q3 season starts ~mid-Oct → pre-Q3 lull (~14th+ consecutive session with ~0 in-universe qualifiers, now under the stricter >20% ELEVATED_BAR). No fresh in-universe >20% PEAD catalyst overnight. No compelling non-universe catalyst warranting a watchlist add (CTAS sub-bar/negative; Petco not in scope).
- **DECISION: 0 candidates ≥6/10 under the >20% bar → plan NO buys** (plan fewer rather than lower the bar, per MUST NOT). Planned sells: none (DELL held, thesis intact). Trailing conversions: none.
- **Sanity vs strategy.md:** cash 89.4% (≥10% floor ✓); concurrent 1/8 (≤8 ✓); weekly new 0/2 this week under ELEVATED_BAR cap (DELL bought 2026-09-17 = prior week; ≤2 ✓); sector: IT 10.6% of equity via DELL (≤30% ✓). No trims needed (no new buys).
- **Regulatory flags among planned:** NONE (no buys).
- **Watchlist flags:** none added (only MRVL is `active`; it was considered and dropped for lack of a fresh earnings catalyst).
- ⚠️ Sizing note: pre_market.md step 5 says "(currently 11%)" vs strategy.md `Max position size at entry` field **20%** — moot today (no buys); flagged for human reconciliation (recurring).
- ⚠️ portfolio.md bloat (~340KB, exceeds single-read limit) — recurring flag for human trim (NOT auto-trimmed; deleting audit history needs human sign-off).
