# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-21 (pre_market ~08:20 ET). Regime: **BULL** (SPY $762.62 > 200MA $707.10). PEAD posture: **NORMAL** (fresh, expires 2026-08-23; realized 0.906% n=113) → standard strategy.md thresholds (15% EPS most sectors; 20%+streak≥2 for Industrials/Energy; 20% for Utilities/Real Estate). Weekly new-position cap 5 (0 used this week).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 8 | $1,300.00 | ~$1,145.91 (= fill × 0.92) | **Eli Lilly — Health Care — score 9/10.** Q2 2026 (reported Aug 5 BMO): rev **$23.0B +48% YoY** (+11.4% beat; Mounjaro $9.9B +91%, Zepbound $4.9B +44%); adj EPS $8.38 (headline noisy — incl. ~$3.03/sh IPR&D charge; operational EPS beat = **+27% surprise** > standard 15% HC bar; also qualifies analyst-revision/catalyst-exempt). **RAISED FY26 rev guide to $85–87B** (2nd straight raise). **4-qtr beat streak** (+1 signal). Earnings-day gap **+6.15%** (normal, no adj), volume **2.18x** 20-day avg (strong institutional confirmation). **Fresh 52-wk high $1,292.51 set Aug 19 (1 day ago — top-priority recency); drift INTACT & re-accelerating.** Price $1,245.55 = **+3.66% above 21d EMA $1,201.60**. RS vs SPY **+4.97 (5d), +1.73 (20d)** — outperforming both windows. Sector XLV **+3.48 vs SPY (20d)** — Health Care leading, sector tailwind (no PEAD-rotation penalty). Analyst conviction: **6+ post-print PT raises, 0 downgrades** (BofA→$1,251, Cantor/Citi/RBC/Morgan Stanley/Jefferies all lifted into $1,200–1,600; Jim Cramer/CNBC raised on "another beat-and-raise quarter"); lone caution = Berenberg Hold. Mgmt (CEO Ricks): retatrutide showed "profound levels of weight loss… approaching bariatric surgery levels"; Lilly is global GLP-1 leader ~55% share (+~2pp QoQ). Insider: EVP Jonsson sold 6,500 sh (~$7.6M) under a pre-arranged **10b5-1** plan (weak bearish signal). Top risk: Novo Nordisk oral-GLP-1 competition (Foundayo early Rx headwinds; ~-9% US realized price) + premium >$1T valuation — structural/ongoing, none thesis-breaking within 42d. **Regulatory: shelf-reg CLEAN** (no S-3/424B; bolt-ons funded from Mounjaro/Zepbound cash), **BIS N/A** (pharma). Next earnings Oct 29 (outside 3-day window). Active/tradable NYSE ✓, no halt. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME held: no exit criterion fired. Unrealized ~−4.10% ($799.94 vs $834.12), hard stop 96e4e855 $767.39 GTC active (cushion ~4.1%); thesis intact (record Q2 rev $5.15B +19.8%, +25.31% EPS surprise, RAISED FY26 guide, record RPO backlog $17.1B); held 16d (opened Aug 5, not 60d-stale); far below +10% trailing trigger. HOLD. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME −4.10% (far below +10% partial-profit-lock trigger); no conversion. |

## Notes

- **Gates all PASS.** Clock: `next_open` 2026-08-21 = today (trading day, not a holiday). Reconciliation 1/1 zero divergence vs Alpaca /v2/positions (EME 13 @ $834.12 ✓; sole open order = hard stop 96e4e855 $767.39, no orphans). Universe cache fresh (expires 2026-08-23, 294 tickers). Account ACTIVE, trading_blocked=false, equity $97,822.63, cash $87,423.41 (89.4%). DRY_RUN: false.
- **Regime / posture.** SPY $762.62 > 200MA $707.10 → BULL (standard thresholds). PEAD posture NORMAL (realized_health_60d 0.906%, n=113, health_ok=true) — standard 15% bar, no ELEVATED_BAR tightening. Weekly cap 5; 0 fills this week (last fill EME Aug 5) → 1/5 after LLY.
- **Sizing.** LLY 8 sh × $1,245.55 ref = $9,964 = **10.19% of equity** (target ~11%, well under 20% cap). Post-would-be-fill cash ~79% >> 10% floor. Concurrent 1→2/8. Sectors: EME Industrials ~10.6% + LLY Health Care ~10.2% (different sectors, each << 30% cap). All strategy.md sanity checks PASS.
- **LLY entry-gate caveat (for market_open).** LLY has been the top pick for ~2 weeks but has DEFERRED 8 consecutive sessions on the market_open opening-range/EMA whipsaw guards (Gate 6d/6e/4) — it repeatedly prints its OR high then fades intraday. The setup is excellent (fresh 52-wk high Aug 19, drift re-accelerating), so it stays the #1 planned buy; but expect the same disciplined entry — only fill on a **confirmed** breakout above the opening-range high with price ≥ 21d EMA (Gate 4 + 6d + 6e). Do NOT chase if it fades below ORH again; defer and re-evaluate.
- **Shortlist scoring (candidates screened, only LLY ≥6 cleared to plan):**
  - **LLY 9/10** — PLANNED (see thesis). Signal 3/3, Momentum 3/3, Confirmation 2/2, Risk ~1.5/2.
  - **PWR (Quanta, Industrials) — DROPPED (~6, momentum decayed).** Fundamentals still qualify (Q2 Jul 30 EPS +28.9% > strict Industrials 20%+streak≥2; 4-qtr streak; record backlog $53.4B; gap +16.26%, vol 3.23x), BUT the post-earnings drift has **rolled over**: price $662.62 now **−1.32% BELOW 21d EMA $671.47**, 20d RS **−2.04 vs SPY** (underperforming), 52-wk high 73d ago (May 6), and sector **XLI −4.54 vs SPY (20d) — money rotating OUT of Industrials** (PEAD is weakest in that condition). 3+ consecutive market_open Gate-4/6e defers confirm the stall. Dropped rather than re-list a decayed signal; re-add only if it reclaims trend with fresh RS.
  - **CAT (Caterpillar, Industrials) — DROPPED (<6, momentum broken).** Q2 Aug 4 EPS +31.7% qualified, but price $815.40 = **−4.74% BELOW 21d EMA $855.94**, 20d RS **−12.10 vs SPY** (badly underperforming), sector XLI rotating out. Post-earnings drift dead. (Already dropped from the active plan after Aug 7.)
  - **PLTR (Palantir, IT) — DROPPED (~5–6, weak/muted drift + chase risk).** Q2 Aug 3 EPS +17–20% > 15% IT bar, rev +93% YoY, 8-qtr streak, +9.54% above EMA — but earnings-day gap only **+3.02% despite the large beat (muted reaction = weak PEAD drift signal, −1)**, 52-wk high **199 days ago (Nov 2025 — heavy recency downrank)**, 5d RS **−0.86** (near-term stalling), and it is **extended (+41% in 20 days)**. Buying a +41% 20-day run that is stalling near-term is a chase, not a clean multi-week PEAD entry. Not planned.
- **Overnight news sweep (Aug 20→21).** Quiet pre-open: no major S&P 1500 earnings or macro data Aug 21. FCX firmer on copper +0.74%; KRMN pulling back on profit-taking (overextended, Truist/KeyCorp PT cuts). No new compelling non-universe catalyst → no watchlist additions this session. Active watchlist (MRVL) shows no fresh ≤30-day catalyst (June Computex spike now stale; monitor for its Q2 print). Logged to research_log.md.
