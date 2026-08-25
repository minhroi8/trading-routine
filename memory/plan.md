# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-25 (pre_market ~08:22 ET) — DRY_RUN: false — BULL regime (SPY $763.46 > 200MA $704.98) / PEAD posture NORMAL (realized +2.284% n=91). Standard 15% EPS bar, max 5 new/week.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| PLTR | 59 | $181.50 | $166.98 | **Palantir — score 7/10. IT (standard 15% bar; +20.6% clears).** Q2 2026 (reported Aug 3 AC): adj EPS **$0.41 vs $0.34 = +20.6% surprise**; revenue **$1.94B +6.8% beat, +93% YoY** (US commercial +149%); **RAISED FY26 rev guide to $8.15–8.16B** (from $7.65–7.66B, ~+6.5%; +82% YoY growth), adj FCF $4.5–4.7B. **Earnings streak: 8+ consecutive beats (+1).** Earnings-day gap **+15.3%** (>10% → confirmation +1); day-of pop **+29%**. **Volume ratio 5.5x** 20-day avg (very strong institutional confirmation). **Post-earnings drift +8.2%** over 14 sessions since reaction-close $162.61 → $175.89 (positive, textbook PEAD). **5-day RS +3.1% vs SPY** (outperforming); RS since earnings +9.2%. 52-wk high $207.50 on 2025-11-03 (201 sessions ago → −1 momentum; still ~15% below it — recovering, not extended). Sector ETF XLK 20d ≈ flat vs SPY (−0.04 → −1). Analyst reaction strongly positive: **Citi PT $245 (from $200), DA Davidson $200 (from $175), Baird $200 ("premier AI growth asset")**, no downgrades; consensus Moderate Buy. Mgmt quote (Q2 call): "premier AI growth asset" thesis — US commercial "boomed 149%". **Top risk: extreme valuation** (fwd P/E >80x, ~41x NTM EV/rev — negligible margin for error) **+ aggressive insider selling** (CEO Karp filed to sell ~402k sh / $70M on Aug 20; ~$809M insider sales/12mo → risk −1); NHS-contract regulatory scrutiny (not a 42-day thesis-breaker). Short interest $12B (largest $ short; squeeze partly played on the print → mild +0.5). **Regulatory scan: shelf-reg CLEAN** (no S-3 / equity offering; $4.5B+ FCF, no need to raise); **BIS N/A** (software/data-analytics, minimal China rev). Next earnings **Nov 9, 2026** (outside 3-day window ✓). Tradable=true/active NASDAQ ✓. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8) at start of session — no open positions, no exit criteria to evaluate. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Regime / posture:** BULL (SPY $763.46 > 200MA $704.98, per pead_health.md computed 2026-08-23, fresh, expires 2026-08-30). PEAD posture **NORMAL** (realized_health_60d +2.284%, n=91, health_ok=true) → standard strategy.md thresholds; NO ELEVATED_BAR overlay. Universe cache fresh (screened 2026-08-23, expires 2026-08-30, 294 tickers). Both freshness gates PASS.
- **Sizing:** 1 buy planned. PLTR 59 sh × $181.50 = $10,708.50 = **11.0%** of $97,328 equity (≤ 20% cap ✓). Post-fill: cash ~89% (≥10% floor ✓), 0→1/8 concurrent (≤8 ✓), **1/5 new this week** (bull/normal cap 5 ✓), IT 11% (≤30% sector cap ✓). stop_price $166.98 = $181.50 × 0.92 (−8% hard stop; market_open sets the real stop off actual fill). limit_price is a reference — market_open computes its own opening-range execution limit.
- **⚠️ Event risk — NVDA reports Wed 2026-08-26 after close + PCE data Wed.** PLTR carries AI-sentiment beta (not direct semiconductor exposure — it's software: US gov + Western commercial). A weak NVDA print could pressure AI-adjacent names; the −8% hard stop caps downside. Flagged for market_open/midday awareness; not a reason to skip a clean PEAD setup with a positive, continuing drift.
- **Candidates researched and DROPPED (logged in research_log):**
  - **ANET (IT)** — +15.9% EPS beat (clears bar), 5-qtr streak, guide raise (3rd), +12% pop/gap +10.7%, vol 2.64x, analysts raised PTs (~$226 consensus). **DROPPED: post-earnings drift NEGATIVE −4.5% (peaked $214.62 on the Aug-5 reaction day, faded to $188.25); 5-day RS −5.5% vs SPY (underperforming).** strategy PEAD step-f: negative RS → drop/heavily downrank. The pop reversed — central PEAD confirmation failed. Score ~5/10.
  - **FSLR (IT/solar)** — +43.1% EPS beat headline, BUT **drift −14.6%, 5-day RS −3.3%, earnings-day gap only +0.22%** (muted reaction despite huge EPS beat → confirmation −1) + revenue MISS (−4% YoY) + guidance only REAFFIRMED (not raised). Classic muted-reaction/negative-drift → DROP.
  - **VST (Utilities) / TLN (Utilities-IPP)** — Utilities sector requires >20% EPS surprise (deprioritization rule). VST +16.9% EPS < 20% → fails. TLN no clean EPS-surprise data + same 20% bar. DROP.
  - **HOOD (Financials)** — +47.6% EPS surprise but reported Jul 29 (edge of 30-day window), stock FELL −3.3% on print (crypto rev −38%, cautious opex outlook) → negative reaction/drift. DROP.
  - **DDOG** +12.1% EPS (< 15% bar) & stock −17% on AI-customer usage cut; **APP** EPS in-line + rev miss, −21%; **CVNA** EPS in-line, −10/−20% on weak guide; **COIN** big miss/loss, fell. All DROP.
  - **Retail wave (TGT/TJX/ROST)** — all beat but EPS surprises single-digit (TGT adj +5.6%, TJX ~small, ROST +5.6%) — below the 15% EPS bar. DROP.
  - **AXON (Industrials)** — revenue/guidance beat but not a >20% EPS surprise + Industrials needs >20% AND streak≥2. DROP.
- **Watchlist:** no NEW non-universe catalyst to flag today — the day's biggest movers researched (PLTR/ANET/FSLR) are all in the universe; prior strong non-universe names (AFRM, AMBA, NET, TEAM, EL, etc.) remain `pending_review` (human-only to activate). MRVL (active watchlist) reports Thu Aug 27 → inside the 3-day earnings window → not eligible this session.
- **MUST NOT reminder:** pre_market placed NO orders and did NOT re-screen the universe. Execution is market_open's job.
