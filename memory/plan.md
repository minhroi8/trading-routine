# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-24 (pre_market ~08:20 ET) — BULL regime / PEAD posture NORMAL (standard 15% bar).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 8 | $1,290.00 | fill × 0.92 (≈ $1,154.78 at last close $1,255.20) | **Eli Lilly — Health Care — score 9/10.** Q2 2026 reported Aug 5 BMO: adj EPS $8.38 (operational **~+27% surprise** > standard 15% HC bar; headline noisy w/ IPR&D charge → also analyst-revision/catalyst-exempt), revenue **$22.97B +48% YoY = +11.4% beat** (Mounjaro $9.9B +91%, Zepbound $4.9B +44%, intl +80%); **RAISED FY26 revenue guide to $85–87B (2nd straight quarter)**. **Earnings streak 3q** (Q2'26 / Q3'25 +16.6% / Q2'25 +12.5% all beats). Earnings-day gap **+6.15%** (Aug 5), volume **2.18x** 20-day avg. **Fresh 52-wk high $1,280.56 set Aug 19 (2 td ago — top-priority recency)**. Relative strength **+13.03% vs SPY** since earnings (strong drift continuation). Sector **XLV +3.79% vs SPY (20d)** — Health Care rotating IN. Analysts: **4+ post-earnings PT raises (MS $1,419, JPM $1,400 top pick, Leerink UPGRADE to Outperform, Citi/RBC/BofA raises), 0 downgrades**. Short interest **~1.15%** (very low). Insider: routine 10b5-1 selling, no open-market buys (neutral/mild-neg). Mgmt (CEO David Ricks): *"The number of people taking incretins grew, and Lilly's portfolio of medicines extended its leadership position."* Top risk: **valuation at ATH** + **orforglipron GI-safety watch item** (William Blair flagged AEs not tapering) — but NO binary readout in the 6-week window (orforglipron already FDA-approved; retatrutide submission early-2027). Regulatory: **shelf-reg CLEAN** (no equity dilution shelf; routine debt FWP only); **BIS N/A** (Health Care, non-semi). ⚠️ **CARRY-FORWARD CAVEAT:** LLY has been the #1 planned buy for ~2 weeks and market_open has deferred it 9+ consecutive sessions on the ORB/EMA whipsaw guards (repeatedly prints its opening-range high then fades intraday — do NOT chase). Fundamentals/PEAD remain strong → re-planned; market_open applies Gate 4 (21d EMA) + Gate 6d/6e (chaotic-open / breakout-confirmation) as usual. Sizing 8 sh × $1,255.20 last = **$10,041.60 = 10.3% of $97,425.87 equity** (< 20% cap; matches recent convention). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME exit criteria have NOT fired (stop not hit; thesis intact; held 19d < 60d). See Notes for stop-cushion watch. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME is DOWN (−7.76%), far below the +10% trailing trigger — no conversion. |

## Notes

- **Gates all PASS.** Clock: `next_open` = today 2026-08-24 09:30 ET ✓ (pre_market runs pre-open; is_open=false expected). Reconciliation 1/1 zero divergence: Alpaca EME 13 @ $834.12 matches portfolio.md exactly ✓. Universe cache fresh (`expires_on` 2026-08-30) ✓. Account ACTIVE, trading_blocked=false. Equity $97,425.87, cash $87,423.41 (89.7%).
- **PEAD health posture: NORMAL** (realized_health_60d_pct 2.284%, health_sample_n 91, health_ok true; fresh, expires 2026-08-30) → **standard 15% EPS bar, no new-position cap tightening.** SPY 200-day regime: **BULL** (SPY $765.72 > 200MA $704.98 per pead_health.md) → normal thresholds, weekly cap 5.
- **DRY_RUN: false.**
- **Weekly slots:** fresh week (Mon Aug 24) — 0 buys this week so far → planning LLY = **1/5** (BULL/NORMAL cap 5). ✓
- **Sanity checks (step 6) PASS:** cash floor after LLY ~$10k → deployed EME $10k + LLY $10k ≈ 21% of equity, cash ~79% >> 10% floor ✓; max concurrent EME+LLY = 2/8 ✓; sector caps — Health Care (LLY) 10.3%, Industrials (EME) 10.3%, both << 30% ✓ (no sector conflict).
- **⚠️ EME stop-cushion WATCH (no action for pre_market):** EME mark $769.42 vs hard stop $767.39 (order 96e4e855, −8% GTC) = **0.26% cushion**. A mechanical −8% stop-out is likely on any further downtick — handled automatically by Alpaca. Thesis intact (Q2 blowout, raised FY26 guide, record $17.1B backlog; no negative catalyst). No exit criterion has FIRED → no planned sell; midday/market_open manage the open book.
- **Candidates DROPPED (deep-research + gates):**
  - **ROST** (Ross Stores, Consumer Disc) — **DROPPED on step-h regulatory scan: ACTIVE $3.25B COMMON-STOCK shelf registration filed May 2026 = DILUTION RISK** (mandatory hard-drop per step h.i / MUST-NOT). Corroborating yellow flags: gapped +5.97% but **faded to +4.43% close** (muted vs +8% premarket headline); still **~6% BELOW** its pre-earnings 52-wk high (recovering, not making new highs); **~$0.60/sh of the raised guide is one-time tariff refunds** (ex-refund FY EPS ≈ $8.01–8.17); H2 comps guided to decelerate (+10% → +4–7%); insider selling / zero buying. (EPS +37.1%, vol 4.56x, 3-qtr streak, 6 PT raises / 0 downgrades were positives — overridden by the shelf.)
  - **PLTR** (Palantir, IT) — dropped: 52-wk high $207.39 was **200 trading days ago** (Nov 2025); now −13% below it; Aug 4 earnings drift exhausted (~3 weeks stale). Momentum leg fails.
  - **MRVL** (active watchlist, IT/semi) — dropped: **reports Aug 27 AC — inside the 3-day earnings window** (event risk) per step 4.
  - PFE, considered from the sweep but downranked — beat+raise reported late July (~4 weeks ago), drift largely complete; stale for a fresh PEAD entry.
- **Watchlist flags (step 2 — compelling catalyst on non-universe/non-watchlist tickers, added pending_review; human-only to set active):**
  - **AFRM** (Affirm) — Q2 EPS $0.20 vs $0.10 est (~+100% surprise), rev $876.4M beat $837.0M, stock +20.1% on the print. Not in universe cache / not on watchlist → added pending_review (S&P 500 screen-gap likely, like PAYC/NET).
  - **AMBA** (Ambarella) — Q2 EPS+sales beat, guided Q3 sales above est, stock +26.8%. IT/semiconductor (mandatory BIS scan pending). Not in universe/watchlist → added pending_review.
