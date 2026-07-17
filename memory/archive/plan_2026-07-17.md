# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-17 (pre_market ~08:20 ET) — SPY **BULL** regime, PEAD health **STALE→NORMAL** (bar NOT raised), macro-deferral **NOT triggered** (borderline). Standard thresholds: EPS >15% (>20% Util/RE/Ind/Energy). Book **FLAT** (0/8, 100% cash) at start.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| GS | 9 | $1,110.00 | $1,021.20 | **Goldman Sachs — score 8/10.** Q2 2026 (reported Jul 14 BMO) **EPS $20.98 vs $14.46 consensus = +45.1% surprise**; **revenue $20.34B vs $16.40B = +24% beat** (+39% YoY). Operating-driven beat (equities desk $7.42B +72% YoY, equity underwriting $985M +130% YoY on the record SpaceX IPO + Alphabet raise); investment revenue only $441M so NOT an accounting mark-up. **Earnings streak: 5 consecutive quarters of EPS beats.** Earnings-day gap +3.58% (Jul 13 close $1,046.18 → Jul 14 open $1,083.62) — muted vs the +45% beat (confirmation −1), but day-1 closed +9.15%. **Volume 1.77x** 20d avg (130,233 vs 73,769; moderate confirmation). **52-wk high $1,153.54 on Jul 15 = 2 days ago** (top-priority recency). **RS vs SPY (5d) +3.85%** (GS +3.76% vs SPY −0.09%). **Sector ETF XLF vs SPY (20d) +4.38%** (XLF +4.42% vs +0.04% — money rotating INTO Financials, no penalty). **Analysts: 5 PT raises / 0 downgrades** post-print (Wells Fargo→$1,325, Jefferies→$1,299, Barclays→$1,245, KBW→$1,130, JPM→$955 — all above current $1,095.75). Short interest low (<2% float, neutral). Insider: no open-market buys, routine comp-selling only (Solomon sold May 1, outside 30d window) — neutral. Mgmt quote (Solomon): *"our backlog increased to its highest level in five years and its second-highest level on record."* **Shelf-reg: CLEAN** (net buybacks $4B Q2, div +25%, share count shrinking — no common-equity dilution). **BIS: N/A** (Financials). Next earnings ~Oct 13 (88d out, no event risk). Tradable/active NYSE ✓. **Top risk:** Q2's record was inflated by the once-in-history SpaceX IPO + heavy AI/capital-markets beta (next-Q consensus only ~$14.06) — a capital-markets/AI pullback could compress the very lines that drove the beat; GS also **gave back −4.87% on Jul 16** (post-earnings drift stalling from the Jul 15 high). Sized conservatively ~10.2% for that reason. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT at start — no open positions, no exit criteria to fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — | No open positions. |

## Notes

**Gates (all PASS):** clock `next_open`=2026-07-17T09:30 ET (opens today, not a holiday) ✓; **reconciliation 0/0 PASS** — Alpaca `/v2/positions`=[] matches portfolio.md FLAT, zero divergence; account ACTIVE, trading_blocked=false, equity **$98,266.98**, cash 100%, buying_power $393,067.92; **universe FRESH** (expires_on 2026-07-19 > today; 305 passed, rebuilt Jul 12). DRY_RUN: **false**.

**Regime (strategy.md regime-gate, computed live since pead_health is stale):** SPY close **$750.87** (Jul 16 IEX) vs **200MA $696.27** (n=200) → **BULL** (margin +7.84%). Standard thresholds; max **5** new/week; no ELEVATED_BAR position cap.

**PEAD signal-health overlay: STALE → treated NORMAL, bar NOT raised.** `pead_health.md` expires_on 2026-06-28 < today (2026-07-17) → step 1c freshness rule: a stale overlay never raises the bar (the universe-cache gate is the hard halt and it PASSES). Last reading was ELEVATED_BAR (realized_health_60d_pct −0.492%, health_sample_n 367, computed Jun 21). ⚠️ **PEAD_HEALTH_REFRESH_MISS persists** (7th+ consecutive week — Jul 12 universe_refresh rebuilt universe.md but did not recompute pead_health.md; known yfinance-vs-proxy transport bug, needs human/tooling fix).

**Macro-deferral rule (strategy.md): checked, NOT triggered (borderline).** Leg 1 (S&P futures/index down >0.4%): **YES** — index/futures ~−0.79% today (Iran strikes, crude elevated). Leg 2 (10-yr Treasury at a multi-month high): **NO** — 10-yr ~4.59%, *below* its own weekly peak of 4.62% (Jul 13), so no fresh multi-month high today. Both legs required; 2nd fails → rule NOT triggered → standard 15% threshold applied. Documented as a **stressed/elevated-caution session** (down tape + yields near 2-mo highs) — reflected in conservative GS sizing.

**Sizing convention / DISCREPANCY FLAG:** strategy.md `Max position size at entry` = **20%** (authoritative cap). Routine `pre_market.md` step 5 annotation reads "(currently 11%)", and established practice (prior GS plan Jul 15/16; market_open Jul 16) sizes ~11% with 20% as the ceiling. Sized GS at **11% target = 9 sh × $1,110 = $9,990 ≈ 10.2%** of equity (consistent with the prior 9-share GS plan). **Human to reconcile the strategy.md-20% vs routine-11% discrepancy.**

**Shortlist / drops (deep research a–i completed for GS + WFC; sweep for C, JPM, STT, BLK, GE, UAL):**
- **GS — 8/10 → PLANNED** (sole qualifier). Signal 3/3, Momentum 3/3, Confirmation ~1.5 (muted gap), Risk ~1.5 (peak-quarter/one-off exposure + Jul 16 give-back on a stressed day). Down from market_open's Jul-16 score of 9/10 because of the Jul 16 −4.87% give-back.
- **C — DROP.** +45% profit jump but EPS +16.7% and the **stock FELL post-earnings: RS 5d −5.50%, 20d −7.87%** (step f: negative spread = drop; broken drift).
- **WFC — 5.5/10 → DROP.** EPS +16.3% but beat quality diluted (~$0.04 tax benefit + $604M VC gains, mgmt-flagged); **NII guidance only reaffirmed (~$50B), not raised**; streak not clean (a miss in trailing 4Q); **stock fell ~3% on the print** ("beat-but-sell", NIM concerns). Below 6 bar → per strategy, plan fewer rather than lower the bar.
- **JPM — DROP.** Headline $7.70 inflated by one-time $4.6B Visa share-exchange gain; clean EPS ~+5% < 15%.
- **STT — DROP** (+8.6%), **BLK — DROP** (+10.5%) — below 15%.
- **GE — DROP.** Strong guidance raise but EPS beat only +8.6% ($2.02 vs $1.86); Industrials requires >20% AND streak≥2; earnings-driven entries are not exempt from the EPS threshold.
- **UAL — DROP.** Beat but issued **negative Q3 guidance** on fuel costs; Industrials (needs >20% + streak); stock fell ~3% → thesis not supportive.
- **ABT — DROP.** Only a slight EPS beat despite an FY guide raise — earnings-driven entry fails 15% EPS threshold.

**Sanity checks (step 6, all PASS):** cash floor after GS ≈ 89.8% ≥ 10% ✓; concurrent 1 ≤ 8 ✓; new-per-week **1/5** ≤ 5 (BULL; week of Mon Jul 13; 0 prior fills — GS deferred Jul 15/16 not filled) ✓; sector Financials ≈ 10.2% ≤ 30% ✓.

**Watchlist:** WDFC status `pending_review` (added Jul 13, WD-40 blowout) — **NOT traded** (human-only to set `active`; liquidity/S&P-1500 unverified). MRVL `active` but **no fresh qualifying catalyst** in last 30d (Computex spike was June) → not shortlisted. **No new watchlist additions** — all of today's movers (GS, banks, GE, ABT, UAL, BLK, STT) are already in the universe.
