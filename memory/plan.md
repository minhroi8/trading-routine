# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-27 (pre_market ~07:16 ET). **Half-day session — early close 13:00 ET (day after Thanksgiving).**

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $980.00 | $901.60 | **Regeneron (Health Care, in-universe) — score 8/10.** Q3 2026 (Oct-30 BMO) non-GAAP **EPS $20.07 vs ~$16.08–16.25 cons = +23.5% to +24.8% surprise** (+70% YoY) — CLEAN beat (Dupixent-driven), clears the >20% ELEVATED_BAR/bear bar on every source; **revenue $5.12B +36% YoY (~+11–12% beat)**. **Earnings streak 3+ quarters** of EPS beats (+1 signal pt). **Earnings-day gap +6.29% overnight / +13.5% full day** (5–10% band = normal). **Volume ratio 5.69× 20-day avg** on the Oct-30 print (strong institutional confirmation). **52-week high recency: NEW 52-wk high $991.72 intraday Nov-25 (~2 trading days ago = TOP priority <45d)**; last close $981.97. **Relative strength +5.73pp 5-day** (REGN +3.87% Nov-18→25 vs SPY −1.86% on a down tape). **Sector ETF XLV 20d +2.14% vs SPY −7.19% = +9.33pp** (HC leading, rotation IN — tailwind, no momentum penalty). **Analyst conviction: ~10 post-Q3 PT raises / 0 downgrades** (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980) + **Truist reiterated Buy $982 post-FDA-approval**. **Short interest <2%** (neutral). **Insider: neutral** (no notable Form-4 buying/selling). **Mgmt verbatim (Q3 call):** *"an outstanding quarter … one of our strongest years ever."* **FRESH re-qualifying catalyst (within 30d):** cemdisiran (brand **Livsayis**) **FDA APPROVED Nov-18/19 for anti-AChR+ generalized myasthenia gravis** — the prior binary PDUFA overhang RESOLVED POSITIVELY; stock broke out to a new 52-wk high on it. **Top risk:** near-ATH extension / chase risk on a bear tape + legacy EYLEA biosimilar & Kodiak competition (EYLEA ~31% rev, priced; Q3 beat came despite EYLEA softness) — neither thesis-breaking within the 42-day hold. **Regulatory scan: shelf-reg CLEAN** (routine 2024 WKSI auto-S-3, no 2026 offering, ~103M sh stable, runs buybacks); **BIS N/A** (Health Care). Asset active/tradable (NASDAQ); next earnings Q4 ~late-Jan/Feb-2027 (>3d). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8 positions, 100% cash). No open position has fired an exit criterion. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

**Account / reconciliation.** Alpaca ACTIVE, trading_blocked=false, **equity $94,946.98, 100% cash** ($94,946.98), bp ~$379,787. **RECONCILIATION 0/0 PASS** — `/v2/positions=[]` MATCHES `portfolio.md` FLAT (the VRT row is inside an HTML comment, closed −8% hard-stop 2026-11-02; not a live row). No open orders / no orphan stops.

**Gates.** (1) Clock `is_open=false` (pre-market 07:16 ET), **`next_open=2026-11-27T09:30 ET` = TODAY → not a holiday → proceed.** Half-day, early close 13:00 ET. (2) Reconciliation PASS (above). (3) **Universe cache FRESH** — `universe.md` screened 2026-11-22, expires 2026-11-29 (338 rows) → consumed read-only, NO re-screen.

**DRY_RUN: false.**

**PEAD signal-health overlay (fresh).** `pead_health.md` computed 2026-11-22, expires 2026-11-29 → FRESH. **posture = ELEVATED_BAR** (realized_health_60d **−3.468%**, health_sample_n **175**, health_ok=false — the drift edge is not paying). → **Raise EPS-surprise threshold to >20% for ALL sectors and cap new positions at 2 this session.**

**Regime gate (strategy.md).** Fresh IEX recompute: **SPY Nov-25 close $716.74 < 200-day MA $733.14 (−2.24%) → BEAR REGIME.** Bear rule: max new 2/week + EPS >20% all sectors. Coincides with ELEVATED_BAR; stricter-of new-position cap = **2**. Neither halts — high-conviction setups clearing the higher bar still trade. Macro-deferral rule MOOT (>20% already enforced). Context: SPY logged a ~7-session losing streak into Nov-21 (−3.7% that day), then firmed Nov-24/25 on rate-cut hopes; still below the 200MA. Broad **AI-infrastructure derisking** this week (NVDA CEO saga: Huang resigned Nov-11/12, reinstated Nov-23) drove sharp moves in AI-capex names.

**Weekly new-position count:** 0/2 used this week (last fill VRT 2026-10-29, stopped −8% 11-02; 0 buys since). Planning REGN → 1/2 under the ELEVATED_BAR + bear cap (≤2 ✓).

**Post-fill sanity check (if REGN fills 19 @ $980):** deployed ~$18,620 ≈ **19.6%** (20% cap $18,989 → 19 sh; 20 sh = 20.6% > cap); cash ~80.4% (≥10% floor ✓); concurrent 1/8 (≤8 ✓); new-per-week 1/2 (≤2 ✓); Health Care 19.6% (<30% sector cap ✓). Stop $901.60 = limit × 0.92 (−8% hard stop, placed by market_open after fill).

**REGN execution caveat (for market_open).** REGN has been planned-but-UNFILLED for ~10 prior sessions — market_open's chase-guard correctly rejected it each time while it was extended near its 52-wk high. It is now at a **NEW 52-wk high** after a strong run. The limit is set at **$980 (just BELOW the Nov-25 close $981.97) to enforce a no-chase entry** — fill only on a flat/down open. On a bear tape (SPY < 200MA) apply the opening-range / 21-day-EMA / chase-guard discipline STRICTLY; do NOT chase above the high. The earnings catalyst is now ~28 days old (edge of the 30-day window) — the FDA-approval breakout (Nov-18/19) is what keeps the thesis fresh and the momentum active; if the opening-range/chase gates reject, let it go (no fill is an acceptable outcome).

**Candidates screened and DROPPED today (overnight/last-30-day sweep):**
- **DELL** (in-universe, IT) — Q3 FY2027 (Nov-23 AMC) a huge AI-server beat (record $132.3B AI backlog, $60.2B AI orders), BUT shares **FELL ~−12.4% on the print** ($335.46→$293.98 Nov-24) and sit ~$297 (~−23% off the mid-Nov peak) — a textbook "sell-the-news" after a steep anticipatory run-up, in the middle of broad AI-capex derisking. **Negative post-earnings reaction = fails the positive-drift PEAD premise** (RS strongly negative, gap-DOWN on the beat, below 52-wk high); plus IT/AI-server → **BIS export-control risk** (China). Cannot score ≥6 → DROP.
- **A (Agilent)** (in-universe) — fiscal Q4 (Nov-24) adj EPS $1.86 vs $1.73 = **~+7.5% surprise** (ex-tariff-refund $1.79 ≈ +3.5%); FY27 guide described as "cautious." **Below the >20% bar** → DROP on threshold.
- **NVDA** (in-universe, IT) — Q3 FY27 (Nov-17/18) rev beat-and-raise but **EPS surprise ~+8% ≪ >20%**; China export-control overhang (guide assumes no China DC compute) + reported SEC investigation; semi → BIS → DROP on threshold.
- Season context: FactSet aggregate Q3 EPS surprise ~2.7–3.5% (weakest in 4+ yrs), avg beat-stock +0.8% reaction — very few names cleared >20% with a clean positive drift.

**Non-universe movers OBSERVED, NOT auto-added** (consistent with recent-run sibling-restraint; pending_review backlog ~28 unactioned by human; snippet/aggregator-level evidence only, full a–i not run): **DKS** (Dick's Sporting Goods +14% Nov-24, beat + guidance upgrade, Consumer Disc), **DY** (Dycom +25.8%, earnings + guidance beat). Logged in `research_log.md`. **Watchlist flags: NONE.**

**Watchlist.** Only **MRVL** is `status: active` — thesis remains broken (Nov-2 $115B all-stock Lumentum acquisition, −12.7% day; TD Cowen Buy→Hold) and no in-window catalyst → not plannable. All other watchlist rows are `pending_review` (human-only to activate) → not plannable.

**Regulatory flags on planned name:** NONE (REGN shelf-reg clean, BIS N/A).

**Carry-forward for human (non-blocking):** (a) `portfolio.md` ~499KB bloat (accumulated audit comments exceed single-read limit) — needs human trim. (b) `trade_log.md` VRT buy+sell rows carry `commit_sha <pending>` — backfill. (c) **Doc discrepancy:** `pre_market.md`/`market_open.md` say position size "(currently 11%)" but `strategy.md` `Max position size at entry = 20%` — **strategy.md wins per CLAUDE.md; REGN sized at 20% (19 sh).** (d) research_log rotation of the 2026-11-11 & 2026-11-12 rows (now >14 days) DEFERRED to market_close per the append-only pre_market convention.
