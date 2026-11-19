# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-19 (pre_market ~07:17 ET, Thursday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $950.00 | $874.00 | **Regeneron (Health Care, in-universe) — score 7/10.** Q3 2026 (Oct-30 BMO) non-GAAP EPS **$20.07 vs ~$16.08–16.25 cons = +23.5% to +24.8% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR/bear-regime bar; revenue **$5.12B +36% YoY** (beat ~$4.60B, ~+11–12%). **Earnings streak 3+ consecutive quarters beating** (+1 signal pt). **Earnings-day gap +6.29%** overnight (full-day +13.52%; 5–10% = normal, no adj). **Volume 5.69× 20-day avg** on Oct-30 (strong institutional confirmation). **52-wk high $988.48 on 2026-11-04 = 10 trading days ago (TOP priority <45d)**; Nov-18 close $945.36 = −4.36% below ATH (healthy consolidation, not extended). **RS +2.39pp 5d** (REGN −1.49% $959.67→$945.36 vs SPY −3.88% $759.80→$730.33 — outperforming on a risk-off week). **Sector ETF XLV +1.27% vs SPY −5.54% 20d = +6.81pp** (Health Care leading, rotation IN → tailwind, no penalty). **Analyst conviction ~10 post-Q3 PT raises / 0 downgrades** (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980). **Short interest <2%** (neutral); insider neutral. Mgmt (Q3 call): *"an outstanding quarter … one of our strongest years ever."* **Top risk:** EYLEA biosimilar / Kodiak competition (EYLEA ~31% of rev, priced; Q3 beat was Dupixent-driven despite EYLEA softness) + **cemdisiran gMG FDA PDUFA target ~November 2026** (binary regulatory event may land inside the 42-day hold window — but upside-biased: Phase 3 positive, priority review, PRV used; a secondary-pipeline-asset CRL would not break the core Dupixent thesis) + near-ATH extension. None thesis-breaking within 42d. **Regulatory scan — shelf-reg: CLEAN** (routine 2024 WKSI auto-S-3, no 2026 offering, ~103M shares stable, active buybacks); **BIS: N/A** (Health Care). Asset active/tradable (NASDAQ); next earnings Q4 2026 ~Jan-28-2027 (>3d). Sized 19sh @ $950 limit = $18,050 ≈ **19.0%** of equity ($94,946.98; 20% cap = $18,989 → 20sh = $19,000 = 20.01% > cap, so 19sh), stop $874.00 (= limit × 0.92). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash). No positions → no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | No open positions. |

## Notes

- **Gates PASS.** Clock: is_open=false (pre-mkt), next_open 2026-11-19T09:30 ET → opens TODAY, not a holiday → proceed. **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT (the VRT row below the table header is inside an HTML comment — VRT closed −8% hard-stop 2026-11-02, NOT a live row); `/v2/orders?status=open=[]` (no orphan stops); account ACTIVE, trading_blocked=false, equity **$94,946.98**, 100% cash, buying_power $379,787.92.
- **Universe FRESH** (331 rows, screened 2026-11-15, expires 2026-11-22) → consumed read-only, NO re-screen.
- **PEAD posture = ELEVATED_BAR + FRESH** (computed 2026-11-15, expires 2026-11-22; `realized_health_60d_pct = −0.358%`, `health_sample_n = 163`, health_ok=FALSE) → **raise EPS-surprise bar to >20% ALL sectors + cap new positions at 2** for this session (the drift edge is not paying — defensive). Overlay governs ENTRIES only; never halts, never loosens.
- **⚠️ REGIME FLIP → BEAR.** SPY Nov-18 close **$730.33 < 200-day MA $732.52 = −0.30%** (recomputed IEX, n=200). SPY has fallen through the 200MA (Nov-11 $759.80 → Nov-18 $730.33, −3.9% on the week) — the razor-thin bull of the prior sessions has flipped. **Bear regime applies: max new positions 2/week + EPS surprise >20% for ALL sectors** (strategy.md regime-gate). Both ELEVATED_BAR and bear now require >20% all-sectors and a 2-new cap — stricter-of-the-two cap = **2**. Neither halts; qualifying high-conviction setups still trade.
- **Macro-deferral MOOT** — >20%-all-sectors already enforced by both ELEVATED_BAR and bear regime.
- **Weekly new positions: 0/2 used this week** (Mon 11-16 → Fri 11-20). Last fill was VRT 2026-10-29 (stopped −8% 2026-11-02); 0 opened since. REGN planned-but-unfilled on ~9 consecutive prior sessions (market_open chase-guard rejected it while extended near the 52-wk high).
- **Sanity checks vs strategy.md (if REGN fills):** cash ~81.0% ≥10% floor ✓ | concurrent 1/8 ≤8 ✓ | new-this-week 1/2 under ELEVATED_BAR+bear cap ✓ | Health Care 19.0% < 30% sector cap ✓ | position size 19.0% < 20% cap ✓.
- **REGN execution caveat for market_open:** limit $950 is just above the Nov-18 close $945.36 and well below the 52-wk high $988.48 — DO NOT chase. On a bear tape (SPY below 200MA), apply opening-range / 21d-EMA / chase-guard gates STRICTLY; let the gates reject REGN if it opens extended. Mechanical −8% hard stop $874.00 must be placed immediately after any fill.
- **DROPS / screened this session:**
  - **PANW** (in-universe IT) — fiscal Q1 2027 (Oct-31, reported Nov-18 AMC): adj EPS $1.05 vs $0.97 = **+8.2% surprise** (+13% YoY) ≪ >20% bar; revenue $3.44B +39% YoY (+4% beat), NGS ARR +66% to $9.73B, FY27 guide raised. The catalyst is a revenue/ARR beat + guidance raise (NOT a >20% EPS surprise; guidance raise is not an EPS-exempt catalyst), plus a **$4.5B all-stock Applied Compute acquisition** (dilution/integration overhang) → **DROP on threshold**.
  - **NVDA** (in-universe IT) — Q3 FY27 (Nov-17 AMC) rev $57.0B +~22% beat-and-raise (Q4 guide ~$65B), but non-GAAP EPS surprise **~+8%** ≪ >20% bar (guidance-driven, not surprise-driven); semiconductor → BIS overhang → **DROP on threshold**.
  - **TJX** (in-universe Consumer Disc) — Q3 beat + lifted FY26 but soft Q4 guide; EPS surprise single-digit ≪ >20% bar → **DROP**.
  - **BRBR** (BellRing Brands, +24% Nov-18, NON-universe Consumer Staples) — snippet-level only, consensus $0.23 with a recent history of EPS *misses* (fiscal Q3 was −18.9%); the pop reads as FY27-outlook / new-CEO sentiment, not a verified clean >20% EPS surprise. **Observed, NOT auto-added** (insufficient verification + consistent sibling-restraint given the ~28-name unactioned pending_review backlog).
- **WATCHLIST:** only MRVL is `active` — thesis BROKEN (Nov-2 $115B all-stock Lumentum acquisition, −12.7% day, TD Cowen Buy→Hold PT $350→$175); next earnings ~Nov-26 (outside 3d), last report ~late-Aug (~80d, outside 30d) → no in-window catalyst → not plannable. **NO new watchlist adds.**
- **Regulatory flags:** NONE on the planned name (REGN shelf-reg CLEAN, BIS N/A).
- **Watchlist flags:** NONE.
- **Carry-forward (human):** portfolio.md ~490KB bloat (human-trim needed); trade_log VRT buy+sell commit_sha `<pending>` (backfill); strategy.md position-size is **20%** (the pre_market.md "(currently 11%)" doc line is stale — CLAUDE.md says strategy.md wins; REGN sized at 20% = 19sh). Log rotation DEFERRED to market_close (pre_market appends only).
- **DRY_RUN: false.**
