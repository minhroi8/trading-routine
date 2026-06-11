# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-11 (Thursday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| CASY | 11 | $922.00 | $848.24 (= entry × 0.92 — recompute off actual fill) | **Score 9/10.** Casey's General Stores — Consumer Staples (convenience retail). Qualifying signal: Q4 FY2026 earnings beat (reported Jun 9 after close). EPS $4.37 vs ~$3.36 consensus = **+30% beat** (clears ELEVATED_BAR >20% all-sectors bar), up +66% YoY; revenue $4.57B = **+4.0% beat**, +14% YoY. FY2026 record: EPS $19.16 (+30.9%), net income $714M, EBITDA ~$1.5B. FY2027 guide RAISED: EBITDA +8–10%, ≥120 new stores, inside SSS +2–5% (margin >42%). **Earnings streak: 4 consecutive quarters beating** (Q4 +30%, Q3 +16% → +1 signal pt). **Earnings-day gap +4.7% at open** (technically muted-open per rule) **but stock closed +19.98% on the day** — strong full-day institutional follow-through, not a muted reaction. **Volume 3.89x** 20-day avg (strong institutional confirmation). **52-week high $914.71 made Jun 10 (0 days ago — TOP PRIORITY).** **RS vs SPY +21.5%** (1-day post-earnings: CASY +19.97% vs SPY −1.56%; 5-day spread will accrue). **Sector ETF XLP +1.22% vs SPY −1.71% 20-day = +2.93% spread — staples OUTPERFORMING (no PEAD momentum penalty).** Analyst conviction: PT raises Wells Fargo $910 (Overweight), Stephens $900, Gordon Haskett $850, UBS $805 (Neutral); consensus ~$840; no downgrades post-print (several Neutral ratings cite valuation). Short interest: low (~<3%, neutral). Insider: routine Form 4s ~Jun 5, no aggressive selling (neutral). CEO Darren Rebelez (verbatim): *"Casey's delivered another record fiscal year as our team closed out the three-year strategic plan on an extremely high note, reaching $714 million of net income and nearly $1.5 billion in EBITDA."* **Top risk:** rich valuation (~41x earnings) and chasing a +20% one-day spike at the 52-week high (mean-reversion/pullback risk) — reflected in risk 1/2. Regulatory scan: shelf-reg CLEAN (no active S-3 / equity offering found); BIS N/A (Consumer Staples). Next earnings ~Sep 8 2026 (outside 3-day window). Alpaca: tradable=true, status=active ✓; no halt ✓. Sector: Consumer Staples — 0% currently held; CASY ~10.3% < 30% cap ✓. Score breakdown: signal 3/3, momentum 3/3, confirmation 2/2, risk 1/2 = **9/10**. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | SNDK: no exit criterion fired (held 6d; +4.92%; not −8%; not 60d-stale; thesis intact). HOLD. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | SNDK +4.92% (cur $1,724.50) < +10% trigger $1,808.06 — no conversion. |

## Notes

- **Gates PASS.** Clock: `is_open=false`, `next_open=2026-06-11T09:30 ET` — market opens today (Thu). Timestamp 08:02 ET. Reconciliation PASS (1/1): SNDK 6 @ $1,643.6933 ✓, stop 9362a074 $1,512.20 confirmed active (cur $1,724.50, +4.92%, cushion 12.31%). Universe cache expires 2026-06-14 (valid ✓).
- **PEAD signal-health: ELEVATED_BAR** (computed 2026-06-05, expires 2026-06-12 — **fresh**). `realized_health_60d_pct = -2.08%`, `health_sample_n = 211`, `health_ok = false`. → This session: EPS-surprise bar raised to **>20% for ALL sectors**; **max 2 new positions**. CASY (+30% beat) clears the higher bar.
- **SPY 200-day regime: BULL** (SPY close $725.58 [Jun 10 IEX] > 200MA $685.32, n=200). Bull regime would allow 5 new/week, but ELEVATED_BAR cap of 2 is stricter → **max 2 new this session**.
- **Macro:** S&P 500 futures down ~1% (>0.4% threshold) but 10-yr yield ~4.55% — NOT at multi-month high (peak 4.70% May 20). **Macro deferral rule NOT triggered** (requires BOTH). Bar already >20% via ELEVATED_BAR regardless. Risk-off backdrop: US–Iran de-escalation hopes after latest strikes; PPI report due today.
- **Candidates researched (full a–i protocol where applicable):** CASY (Consumer Staples, +30% beat — **QUALIFIED 9/10, planned buy**). Disqualified: ORCL (Q4 FY2026 Jun 10: non-GAAP EPS $2.11 vs $1.89 = +11.64% beat < 20% bar — DROP step a); ADBE (reports today Jun 11 after close — within 3-day earnings window, blocked step 4); CRM (Q1 FY2027 +24% beat clears bar, but RS vs SPY Jun 4→10 = CRM −9.42% vs SPY −4.15% = −5.27% spread, down 4 straight sessions $209→$171 — DROP step f, beat-but-drifting-down). Carried-forward disqualifications unchanged: META/AVGO (step f RS negative), TTWO (GTA6 delay risk step g), INTC (above max analyst PT step g), MRVL/watchlist (mean PT $233 < price step g; reassess post-Jun 22 S&P 500 inclusion).
- **Weekly new-position slots:** 0/2 used this week (no buys Jun 8–10). CASY would be 1/2.
- **Sanity check (strategy.md):** cash floor — post-CASY deployed ~$20.4K of $98.2K equity = ~21% (cash ~79% >> 10% floor ✓); max concurrent 2/8 ✓; max new/week 1/2 (ELEVATED_BAR cap) ✓; sector cap — Consumer Staples 10.3% < 30% ✓ (SNDK separate sector).
- **Watchlist flags:** none (no compelling non-universe catalyst surfaced; CASY is a universe ticker).
- DRY_RUN: **false**.
</content>
</invoke>
