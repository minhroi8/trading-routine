# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-03 (pre_market ~08:25 ET). DRY_RUN: false. Regime: BULL (SPY $747.03 > 200MA $697.41). PEAD posture: NORMAL (fresh). Standard 15% EPS bar, max 5 new/week.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| EME | 13 | $805.00 | $740.60 | **Score 7/10.** EMCOR (Industrials, in universe). Q2 2026 reported Jul 30 AM: diluted EPS **$9.06 vs ~$7.23 = +25.31% surprise** (clears strict Industrials >20% gate); revenue **$5.15B +19.8% YoY**; **3-quarter beat streak** (Q4'25 $7.19, Q1'26 $6.84/+16%, Q2'26 $9.06/+25% → streak ≥2 ✓); **record RPO backlog $17.1B**; RAISED FY26 guide to $20.0–20.5B revenue / ~$32.63 EPS midpoint. Earnings-day gap **+14.75%** (>10%, +1 confirmation); volume **1.88x** 20-day avg (near-strong); 52wk-high $951.96 was **59 days ago** (46–90d normal priority); held the +18% pop (−0.62% next day, no give-back); analyst PT **~$1,000 (~25% upside)**. CEO Tony Guzzi: *"We delivered another outstanding quarter"* — AI data centers need 1.5–2x mechanical/electrical content; network & communications (data-center) revenue **+45%**. Top risk: **insider NET SELLING ~$11.2M over 3 months** (one exec sold 27% of holding @ ~$895) + premium valuation + execution risk on large pipeline. Sector ETF **XLI −2.5% vs SPY 20d** (momentum headwind, −1). Regulatory: shelf-reg **CLEAN** (none found), BIS **N/A** (Industrials). |
| AMZN | 39 | $274.00 | $252.08 | **Score 8.5/10.** Amazon (Consumer Discretionary, in universe). Q2 2026 reported Jul 30 AC: revenue **$200.6B +20% YoY** (beat +2.26%); **AWS $42.2B +36.8% YoY — fastest growth in 18 quarters, accelerating** (beat +4.28%, AWS op margin 39% +650bps); operating income **$27.5B +43%**. Earnings-reaction gap **+12.53%** (Jul 30 close→Jul 31 open, >10%, +1); Jul 31 close **+15.32%** → relative strength **+14.6% vs SPY** (very strong drift); volume **2.6x** 20-day avg (strong institutional confirmation); near 52wk-high ($278.56, 60d ago; now ~−2.5%); **5+ analyst PT raises** ($335–$400: Benchmark $400, JPM $365, BMO $360, MS/KeyBanc $335), "best quarter in a decade." Long multi-quarter beat streak. Mgmt: capacity-constrained into 2027–2028; capex raised to ~$220B (2026) → near-term FCF headwind (demand-driven, not thesis-breaking). Note: headline EPS surprise (+217%) is **inflated by an investment-valuation gain** — thesis rests on the clean AWS re-acceleration + revenue beat + strong price/volume reaction, NOT the EPS number. Top risk: FTC antitrust (known, not a 42-day catalyst) + capex/FCF drag. Sector ETF **XLY −1.1% vs SPY 20d** (momentum headwind, −1). Regulatory: shelf-reg **N/A** (no dilutive offerings), BIS **N/A** (retail/cloud). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8 positions, 100% cash). No open positions → no exit criteria fired. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates:** Gate 1 clock `is_open=false`, `next_open=2026-08-03T09:30 ET` → market opens today (Monday), NOT a holiday → proceed (pre_market runs pre-open). Gate 2 **RECONCILIATION 0/0 PASS** (Alpaca `/v2/positions=[]` matches portfolio.md FLAT book, zero divergence). Gate 3 universe cache **FRESH** (screened 2026-08-02, expires 2026-08-09, 286 rows).
- **PEAD signal-health overlay:** posture **NORMAL**, FRESH (computed 2026-08-02, expires 2026-08-09; realized_health_60d **+2.008%**, health_sample_n **269**, health_ok=true). Bar NOT raised → standard `strategy.md` thresholds (15% EPS; 20% for Utilities/RE/Industrials/Energy). Max 5 new/week.
- **Regime gate:** SPY close $747.03 > 200-day MA $697.41 (+7.1%) → **BULL** → normal operation, all standard thresholds.
- **Sizing:** strategy.md `Max position size at entry` = **20% ceiling** (stable since Jul 17 commit 170d4bb). Routine text says "(currently 11%)" and every recent plan (e.g. Jul-31 AMZN 41@$264 ≈ 11%) sized at ~11%. Sized both buys at **~11%** of equity ($98,266.98 × 11% ≈ $10,809) — well within the 20% cap, consistent with routine text and recent practice, and risk-prudent. EME 13×$805=$10,465 (10.65%); AMZN 39×$274=$10,686 (10.87%). **If the human intends the full 20%, market_open should confirm.**
- **Sanity checks vs strategy.md:** cash floor — deploying ~21.5% → **78.5% cash** (≥10% floor ✓); max concurrent — 2/8 after fills (≤8 ✓); max new-per-week — 2/5 (bull/NORMAL cap 5; trade_log shows no buys this week ✓); sector cap — Industrials (EME) 10.65% and Consumer Disc (AMZN) 10.87%, distinct sectors, each ≤30% ✓. No trims needed.
- **Stops:** hard stop = entry × 0.92 (−8% per strategy.md), placed by `market_open` as GTC stop immediately after fill.
- **Dropped candidates:** **FIX** (Industrials) — reported Jul 23, −5.54% vs SPY +1.20% since = RS **−6.7% (broken drift)** + volume 1.41x (<1.5, weak) despite a +20% EPS beat; PEAD signal failed step-f/step-e. **LRCX** (IT) — EPS surprise only **+7.69%** (<15% bar) despite a guidance smash; earnings-driven entry fails the threshold. **MSFT** (IT) — headline +11.81% but a $3.2B Anthropic one-time gain contributed ~$0.33 of the ~$0.50 beat → **operational surprise ~4%**, fails 15% bar + low earnings quality. **STRL** — reports **today Aug 3 AC** (inside the 3-day earnings window, event risk).
- **Watchlist:** only **MRVL** is `active` (monitored; no fresh catalyst clearing the bar today). WDFC/THC/CLS/BE/FORM remain `pending_review` (human-only to activate). EME (formerly watchlisted) is now IN the refreshed universe cache → traded as a universe ticker. No new pending_review additions this run.
- **Watchlist flags:** none.
- **Regulatory flags:** none (EME shelf-reg clean/BIS N/A; AMZN shelf-reg N/A/BIS N/A).
