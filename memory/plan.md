# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-20 (pre_market ~07:0x ET). DRY_RUN: false.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 8 | $1,305.00 | fill × 0.92 (≈ $1,178 off $1,281 ref) | **Eli Lilly — Health Care — score 9/10.** Q2 2026 (reported Aug 5 BMO): adj EPS **$8.38 vs ~$6.58 = +27% surprise** (clears standard 15% HC bar and the raised 20% bar); revenue **$23.0B, +48% YoY, +11.4% beat** (Mounjaro $9.9B +91%, Zepbound $4.9B). **FY26 REVENUE guide RAISED to $85–87B** (from $82–85B); ⚠️ non-GAAP EPS top-end trimmed $0.50 ($37.00→$36.50) on deal-related IPR&D charges (NOT demand — revenue clearly raised). Streak **4/4 quarters** beating. Earnings-day gap **+6.15%**, full day +4.64%, volume **2.18×** 20-day avg. **52-wk high $1,292.51 set Aug 19 = 0 td ago (FRESH BREAKOUT, top priority)** — closed $1,280.56 (+4.4% Aug 19). RS **+5.41% vs SPY** (5-day, LLY +4.97% vs SPY −0.45%). Sector **XLV +7.34% vs SPY** (20-day) — Health Care leading; rotation out of tech into pharma. Analyst conviction: **Leerink UPGRADE to Outperform PT $886→$1,104** + JPM/BofA/CNBC PT raises, **0 downgrades**; avg PT ~$1,302. Short interest **~1.15%** (low, neutral). Insider: routine 10b5-1 selling, no open-market buying (neutral). Verbatim (CEO David Ricks): *"Lilly's momentum continues, as we delivered 48% revenue growth and raised our full-year guidance."* Top risk: MFN pricing + Novo oral-GLP-1 competition + rich ~45× P/E — chronic, NOT a 42-day binary (−8% stop protects). Regulatory scan: **shelf-reg CLEAN** (no dilutive S-3/equity offering — LLY is a net-buyback name); **BIS N/A** (pharma). Earnings re-verify: next report **Oct 29** — outside 3-day window ✓. Active/tradable NYSE, no halt ✓. Price +6.96% above 21d EMA ($1,197). #1 pick. |
| PWR | 15 | $695.00 | fill × 0.92 (≈ $639 off $695 ref) | **Quanta Services — Industrials — score 7/10 (lower-conviction #2; momentum stalling).** Q2 2026 (reported Jul 30): adj EPS **$4.24 vs $3.29 = +28.9% surprise** (clears strict Industrials **>20% AND streak≥2** gate ✓; +71% YoY); revenue **$9.56B, +41% YoY, +11–12% beat**; **record backlog $53.4B**; **FY26 guide RAISED ~20% midpoint** (rev $39.3–39.7B, adj EPS $16.45–16.95). Streak **4/4 quarters** beating. Earnings-day gap **+16.26%**, full day +17.29%, volume **3.23×** 20-day avg (strong). 52-wk high $788.75 on May 6 = **72 td ago (>45d, downranked; −14.1% below)**. ⚠️ **RS +0.33% vs SPY** (5-day — DECAYED from +4.21% on Aug 19; price rolled over $722→$677 = −6% over Aug 18–19). Sector **XLI −1.14% vs SPY** (20-day — Industrials rotating OUT, −1 momentum pt). Analyst: **Guggenheim + KeyBanc upgrades** (KeyBanc→OW PT $807), TD Cowen→$785 / Mizuho→$741 PT raises, Argus trimmed PT $900→$800 (kept Buy), **0 downgrades**; avg PT ~$761. Short interest **~2.3%** (low). Insider: no notable selling since earnings (CAO sale was May, pre-earnings). Verbatim (CEO Duke Austin): *"The business has structurally and fundamentally changed, with two growing addressable TAMs"*; large 765kV/500kV corridors *"about 95% not yet in backlog."* Top risk: rich ~42× fwd P/E → whippy on risk-off/rate-up days (no 42-day binary; −8% stop). **NOTE: Aug 18–19 −6% rollover = broad AI/semi/rate-driven risk-off session, NOT a PWR-specific catalyst — thesis INTACT but drift stalling on macro.** Regulatory scan: **shelf-reg CLEAN** (early-Aug S-3 = $2B senior notes/DEBT, non-dilutive); **BIS N/A** (Industrials). Earnings re-verify: next report **Oct 29** — outside 3-day window ✓. Active/tradable NYSE, no halt ✓. Price only +0.74% above 21d EMA ($672) — marginal trend (deferred by market_open on ORB Gate 6e Aug 18 & 19). #2 pick. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME held 15d (opened Aug 5), total −3.5% (mark ~$805 vs cost $834.12). NO exit criterion fired: not −8% hard stop ($767.39, cushion ~4.8%), thesis intact (Q2 rev $5.15B +19.8% beat, +25.31% EPS surprise, RAISED FY26 guide, record RPO backlog $17.1B), not 60d-stale, below +10% trail trigger. HOLD. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME below +10% partial-profit-lock trigger; no conversion. |

## Notes

- **Gates:** clock `is_open=false`, `next_open=2026-08-20T09:30 ET` → opens today (Thu), NOT a holiday → proceed. **RECONCILIATION 1/1 PASS:** Alpaca /v2/positions = EME 13 @ $834.12 MATCHES portfolio.md exactly (hard stop 96e4e855 @ $767.39 GTC active in /v2/orders — sole open order, no orphans); zero divergence. Account ACTIVE, trading_blocked=false; equity **$97,888.41**, cash $87,423.41 (89.3%), EME mv $10,465 (−3.5%), 1/8 concurrent.
- **Universe FRESH** (screened 2026-08-16, expires 2026-08-23, 294 rows) → freshness gate PASSES.
- **PEAD health FRESH & NORMAL** (computed 2026-08-16, expires 2026-08-23; realized_health_60d **+0.906%**, n=113, health_ok=true) → **standard 15% bar, max 5 new/week (no ELEVATED_BAR)**.
- **SPY regime BULL** (Aug 19 IEX close $769.09 > 200MA $706.70, +8.8%) → standard sector thresholds, max 5 new/week.
- **Macro-deferral NOT triggered:** pre-market S&P futures **+0.16% (UP)** → "down >0.4%" leg FAILS; **10-yr ~4.64%, eased off the Aug-18 ~4.75% (19–20-month) high → NOT a fresh high today** → leg FAILS; both required → standard bars. (FOMC minutes released Aug 19; Jackson Hole Aug 27–29 is the next event risk.)
- **Weekly slots:** 0 actual fills this week (Mon Aug 17; last actual fill EME Aug 5 — Aug 17/18/19 were all market_open ORB defers, no fills) → **0/5 → 2/5** after LLY + PWR (BULL/NORMAL cap 5).
- **Sizing:** ~11% of equity per `pre_market.md` step 5 ("currently 11%"). ⚠️ **Discrepancy flagged for human:** `strategy.md` "Max position size at entry" field = **20%**, but `pre_market.md` parenthetical says 11%. Sized conservatively at ~11% (dominant recent precedent); market_open's own 20%-cap trim still applies as a ceiling. LLY 8 sh ≈ 10.7% @ limit; PWR 15 sh ≈ 10.4%.
- **Sector cap:** Health Care (LLY) ~10.7% < 30% ✓; Industrials (EME ~10.7% + PWR ~10.4%) ≈ **21.1% < 30%** ✓.
- **Post-fill sanity:** cash ~$66.6K ≈ **68% >> 10% floor** ✓; 1→3/8 concurrent ✓; 0→2/5 weekly ✓.
- **Regulatory flags among planned: NONE** (LLY shelf clean / BIS N/A; PWR shelf clean $2B debt / BIS N/A).
- **Dropped candidates:** **EL (Estée Lauder, +21.9% EPS surprise Aug 19, guide raise, +12–18% pop)** — NOT in universe/active-watchlist → **added to watchlist.md as `pending_review` + Discord flag; MUST NOT plan** (human-only to activate). **ADI** (EPS +3.3% surprise < 15% IT bar; guidance-raise catalyst but day-0/1 drift; semi → BIS scan pending) → log only. **TGT** (~+5–6% clean surprise; headline inflated by one-time tariff refund < 15%) → drop. **TJX** (modest surprise < 15%) → drop. **WMT** (raised guide but stock FELL on slow US comps — fails positive-reaction test) → drop. **HD** (rev miss, lowered FY outlook) → drop. **DE** (reported Aug-20 AM, day-0, no drift/reaction yet) → re-eval. **NTAP** (next report ~late Aug, outside window) → skip.
- **Watchlist:** MRVL **active** — no fresh ≤30-day catalyst; reports **~Aug 27** (entering now = right before earnings event risk) → NOT shortlisted. WDFC/THC/CLS/BE/FORM/PAYC/NET/TEAM + new **EL** all `pending_review` (human-only, MUST NOT plan).
- **Earnings re-verify (step 4):** LLY next Oct 29 ✓; PWR next Oct 29 ✓ — both outside 3-day window. **Halt/tradable (4b):** LLY + PWR both active/tradable NYSE, no halt news ✓.
- DRY_RUN: false.
