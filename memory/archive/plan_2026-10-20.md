# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-10-20 (pre_market, Tue)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | **NO QUALIFYING CANDIDATES ≥6/10** under the ELEVATED_BAR >20%-EPS-all-sectors bar. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — no positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — | Book FLAT — no winners to trail. |

## Notes

**pre_market 2026-10-20 (~08:2x ET, Tue): 0 plannable candidates ≥6/10 → NO new buys. Book stays FLAT (0/8, 100% cash). WATCHLIST ADD: CLF (pending_review).**

- **Gates:** `/v2/clock` is_open=false (pre-market ~08:2x ET), next_open=2026-10-20T09:30 ET → opens TODAY, NOT a holiday → proceed. **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT; `/v2/orders?status=open`=[] (no orphan stops); zero divergence. Account ACTIVE, trading_blocked=false; equity **$96,448.31**, cash $96,448.31 (100%), buying_power $385,793.24, long_mv $0.
- **Universe FRESH:** screened 2026-10-18, expires 2026-10-25, 274 rows → freshness gate PASSES; no re-screen.
- **PEAD health FRESH + ELEVATED_BAR:** computed 2026-10-18, expires 2026-10-25; realized_health_60d **−0.447%**, n=373, health_ok=false → per step 1c **EPS bar RAISED to >20% ALL SECTORS + max 2 new positions** (bull-and-weak case; NEW entries only, never halts).
- **SPY regime BULL:** spy_close 763.25 > 200MA 721.88 (spy_above_200ma=true, per pead_health computed 2026-10-18) → bear-rule NOT active; effective new-position cap = min(5 weekly, 2 ELEVATED_BAR) = **2**. Weekly new used: 0/2 (DELL exited 2026-09-24, prior week).
- **Macro-deferral MOOT:** ELEVATED_BAR already imposes >20%/cap-2 (equal-or-stricter than the macro-deferral >20% leg), so the macro leg changes nothing regardless of futures/yields.

**Candidate review (Q3-2026 season ramping; this morning's / overnight reporters):**

- **RTX (in-univ, Industrials, large) — ONLY in-univ nominal >20% EPS beat → DROP (<6):** Q3 (reported Oct-20 **BMO today**) adj EPS **$2.26 vs $1.78 cons = +27% headline**, rev $24.97B +11% YoY (+3.3% beat), FY adj-EPS guide raised to $7.65–7.75 (3rd raise of 2026; midpoint ~$7.70 only ~1.1% above Street $7.64), record $340B backlog, >$81B new awards. **Disqualifiers:** (1) **~$0.25 of the $2.26 adj EPS is a one-time IEEPA tariff-cost recovery** → ex-item recurring beat ≈ **+13%**, FAILS the >20% bar on a clean basis (and even the standard 15%); (2) **reported THIS MORNING = 0 trading days of post-earnings drift** → PEAD drift / 5-day-RS-vs-SPY legs (step f) are UNMEASURABLE; (3) **muted reaction**: +2.1% immediately post-print on a +27% headline beat = **gap <5% despite large EPS beat → confirmation −1** (step i.ii); (4) **Industrials is strategy.md's WORST sector** (2026 YTD backtest 25% win, −4.82% avg) and requires **>20% AND streak ≥2** — the clean ex-item number fails the >20% leg. Low-quality, one-time-inflated, muted, same-day-no-drift PEAD setup (mirrors the GS drop pattern) → scores <6 → DROP (plan fewer, don't lower the bar).
- **FITB (in-univ, Financials, large) — DROP:** Q3 (reported ~Oct-17 BMO) GAAP EPS **$0.91 vs $0.86 cons ≈ +5.8%** (net income $608M vs $532M; rev $1.525B +6.9%) → FAILS >20% cleanly. A data-aggregator figure of **$1.13 vs $0.83 (+36%)** conflicts with the GAAP release and is attributable "mainly to **Comerica integration**" (M&A/purchase-accounting-driven, not organic) → low-quality PEAD signal regardless of which figure is used. DROP.
- **HAL (in-univ, Energy, large) — DROP:** Q3 (Oct-20) beat EPS+rev (~+3.4% premkt), but Q3 cons was only ~$0.58–0.61 and the magnitude is a few % (prior Q beat +2%) → FAILS >20%; Energy also requires **>20% AND streak ≥2** and is a 0%-win backtest sector. DROP.
- **GE / GE Aerospace (in-univ, Industrials) — DROP:** adj EPS $2.25 vs $2.00 = **+12.5%** → FAILS >20%; stock slipped ~−1.4% on the print. DROP.
- **GPC (Genuine Parts, NOT in universe) — DROP:** narrow beat but NARROWED FY guide, −8.2% → not a compelling catalyst.
- **MRVL (sole ACTIVE watchlist, IT/semi) — DROP:** last earnings Aug-27 (~54d, OUTSIDE 30d window), no fresh ≤30d catalyst; next ~late Nov. Consistent with prior sessions.
- **NFLX / PG / ABT / TMUS — NOT YET REPORTED:** NFLX Oct-20 AMC (tonight), ABT Oct-21 BMO, PG ~Oct-22, TMUS ~Oct-22 → not reported + inside/near earnings window → INELIGIBLE this run.

**Non-universe compelling-catalyst review (step 2) → WATCHLIST ADD: CLF (pending_review) + Discord flag.** Cleveland-Cliffs (Materials/steel, NOT in universe cache, NOT previously watchlisted) Q3 (reported Oct-19 BMO) **adj EPS $0.28 vs ~$0.22 cons = +27% surprise** AND an earnings INFLECTION (Q2 was a −$0.20 loss) with Q3 EBITDA guided ~$575M (≈2× Q2's $286M). Clears the >20% bar nominally; genuine profitability turn. **Caveats:** Materials/commodity-cyclical (PEAD historically weaker — same caution as AA last week); aggregator/snippet-level evidence only, GAAP-vs-adjusted split unverified, full a–i deep-research NOT run. **MUST NOT plan until human sets status: active.** CLF added to watchlist.md as pending_review; Discord flagged.

- **DECISION: 0 ≥6/10 → plan NO buys** (no in-univ / active-WL name cleared the initial >20%-EPS-in-30d + positive-drift gate with clean quality → full a–i deep-research not warranted; plan fewer, don't lower the bar). Planned sells: none (FLAT). Trailing conversions: none (FLAT).
- **Sanity-check vs strategy.md:** cash 100% (≥10% floor ✓); concurrent 0/8 (≤8 ✓); weekly new 0/2 (ELEVATED_BAR cap ✓); sector caps N/A (no positions). Regulatory flags (step h): NONE reached deep research (no candidate cleared the initial gate). Watchlist flags: **CLF (pending_review)**.
- ⚠️ Doc discrepancy carry-forward: pre_market.md step 5 "(currently 11%)" vs strategy.md `Max position size at entry` = **20%** — moot (no buys); strategy.md wins per CLAUDE.md; flagged for human.
- ⚠️ portfolio.md bloat (~387KB accumulated audit comments, exceeds single-read limit) — recurring human-trim flag (NOT auto-trimmed; deleting audit history needs human sign-off).

DRY_RUN: false
