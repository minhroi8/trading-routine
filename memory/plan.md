# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-08

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

### Gates & Regime

- **Market clock**: is_open=false, next_open=2026-06-08T09:30:00-04:00 ET (opens today) ✓
- **Reconciliation**: PASS (5/5) — AAPL 17 ✓ ($308.29, trailing 4225eab6 HWM $316.93 stop $294.74, +8.90%); CSCO 42 ✓ ($122.59, trailing 5dccb5cd HWM $126.00 stop $117.18, +4.41%); GEV 4 ✓ ($947.50, stop 68f84ddd $916.75, −4.92% — cushion 3.25% ⚠️); PWR 15 ✓ ($706.00, stop 10b684b0 $650.49, −0.15% — cushion 7.86%); SNDK 6 ✓ ($1,629.91, stop 9362a074 $1,512.20, −0.84% — cushion 7.22%). All 5 stops confirmed active.
- **Universe freshness**: expires_on=2026-06-14 ✓ (screened 2026-06-07, 299 tickers)
- **PEAD health (pead_health.md, expires 2026-06-12)**: posture=**ELEVATED_BAR** | realized_health_60d_pct=−2.08% | n=211 → **EPS threshold raised to >20% for ALL sectors; max new positions: 2 this session.** (fresh, not stale)
- **SPY regime (from pead_health.md)**: spy_close=$737.55, spy_200ma=$681.56 → SPY > 200MA = **BULL regime**. Standard position cap = 5/week; ELEVATED_BAR cap = 2/session → use 2 (stricter).
- **DRY_RUN**: false
- **Weekly new-position count**: 0/2 used (week resets today June 8)
- **Concurrent positions**: 5/8 ✓

### Macro

- S&P 500 futures edging higher (+0.3–0.5% approx) despite Middle East escalation (Israel struck Iranian petrochemical sites overnight; Iran retaliatory strikes on Kuwait/Bahrain). Oil rising.
- 10-year Treasury yield ~4.54% — **NOT at multi-month high** (peak was 4.70% May 20). Macro deferral rule requires BOTH futures >−0.4% down AND yield at multi-month high. Yield condition NOT met → **macro deferral rule NOT triggered**. Standard thresholds apply (subject to ELEVATED_BAR overlay).
- MRVL announced as new S&P 500 addition (June 22 effective); stock +9% premarket to ~$287.

### Portfolio Thesis Checks

- **AAPL** ($308.29, +8.90% vs cost, trailing stop 4225eab6 HWM $316.93 stop $294.74, cushion 4.40%): **WWDC 2026 started today.** Apple opened WWDC with a sweeping Gemini-powered Siri overhaul (multi-year ~$1B/year Google deal); iOS 27 previewed with third-party AI model selection; Siri gains chat mode, on-screen awareness, personal context. Morgan Stanley, Wedbush, BofA all bullish ("key catalyst"). Stock edging +0.34% premarket. Thesis **STRONGLY REINFORCED**. Next earnings Jul 30 (52 days). HOLD ✓.
- **CSCO** ($122.59, +4.41% vs cost, trailing stop 5dccb5cd HWM $126.00 stop $117.18, cushion 4.41%): CVE-2026-20245 SD-WAN zero-day (7th in 2026, no patch yet, CVSS 7.8, requires netadmin privileges) escalated. This affects SD-WAN management software — **not** core AI networking products (G300 chip, Silicon One, hyperscaler orders). No guidance cut, no earnings miss. AI networking thesis (hyperscaler AI orders triple-digits YoY, G300 AI switch unveiled June 2) remains intact. SD-WAN CVE overhang is reputational risk for a legacy product, not thesis-invalidating per strategy.md. Trailing stop $117.18 provides protection. Next earnings Aug 12 (65 days). HOLD ✓.
- **GEV** ($947.50, −4.92% vs cost, hard stop 68f84ddd $916.75, cushion 3.25% ⚠️): GEV ex-div June 16 ($0.50/share × 4 = $2.00). Recovering from June 5 close of $932.92 to $947.50 today (+1.56%). $163B backlog; management targeting $200B backlog by 2027; AI data center electrification thesis intact. Cushion still tight — Alpaca stop is managed; no pre-market action. Next earnings Jul 29 (51 days). HOLD ✓.
- **PWR** ($706.00, −0.15% vs cost, hard stop 10b684b0 $650.49, cushion 7.86%): No new news. Oppenheimer Outperform + Q1 +35% EPS beat + $48.5B record backlog thesis intact. Next earnings Jul 30 (52 days). HOLD ✓.
- **SNDK** ($1,629.91, −0.84% vs cost, hard stop 9362a074 $1,512.20, cushion 7.22%): No new company-specific negative news. June 5 selloff was broad semiconductor sector event (AVGO down, Broadcom sector weakness). SNDK $42B backlog + Q3 EPS +67.2% + structural AI NAND demand intact. Recovering +4.36% from June 5 close $1,559.32. Next earnings Q4 FY2026 ~late Jul/Aug (50–80 days). HOLD ✓.

### Research Summary — No New Buys (ELEVATED_BAR, 0/12 candidates qualified)

All 12 candidates researched and disqualified. Under **ELEVATED_BAR** conditions (>20% EPS required for all sectors, max 2 new positions), no candidate cleared the ≥6/10 scoring minimum.

| ticker | status | EPS beat | disqualify reason |
|--------|--------|----------|-------------------|
| CRM | Disqualified (step scoring) | +24.0% (within 30d, May 27) | Score ~5.5/10: 52-week high ~$276.80 likely >90 days ago (stock −33% from high); earnings day gap DOWN −4.9% (negative confirmation −1 pt); Q2 FY27 guidance slightly missed estimates; sector ETF (XLK) underperforming SPY; revenue growth modest 9-13%. Does not clear ≥6 minimum. |
| LLY | Disqualified (step 3 window) | +22.67% | Q1 2026 reported April 30 = **39 days ago**, outside 30-day window. Foundayo FDA approval April 1 = 68 days. No qualifying catalyst within 30 days identified. Next earnings Aug 4. |
| AVGO | Disqualified (step f) | +1.7% (Jun 3) | RS vs SPY since earnings: AVGO −22% vs SPY −2.2% (2 trading days post-earnings) = RS spread −20pp. **Step f DROP.** Multiple analyst upgrades qualify as analyst revision catalyst but RS is deeply negative; reassess if RS turns positive. |
| MRVL | Disqualified (step g) | +6.67% (May 27) | S&P 500 inclusion announced June 5 (joins June 22) is a new catalyst. BUT: mean analyst PT $233 vs current ~$281 = −17% below current price. Dilution overhang 26M+ shares (Celestial AI, XConn, NVDA convertible preferred) remains. EBIT margin −12.23%. Step g risk: plausible −17% decline to consensus PT within 42 days. Watchlist status: active; reassess after S&P 500 inclusion dust settles (June 22+) and if analysts raise consensus PTs above $281. |
| DDOG | Disqualified (threshold) | +18.3% | 18.3% < 20% ELEVATED_BAR threshold. Fails by 1.7pp. |
| NVT | Disqualified (threshold) | +15.96% | 15.96% < 20% threshold. |
| PANW | Disqualified (threshold) | +6.7% (Jun 2) | 6.7% < 20% threshold. Within 30-day window but fails. |
| APP | Disqualified (threshold) | +4.83% | 4.83% < 20% threshold. |
| WDAY | Disqualified (threshold) | +3.9–6.8% | Varying consensus sources; all below 20% threshold. |
| AXON | Disqualified (threshold) | +0.63% | 0.63% < 20% threshold. |
| COST | Disqualified (EPS miss) | Below est | Q3 FY2026 EPS missed estimates. |
| INTC | Disqualified (step g) | +16% (Apr 27 = 42d, outside window) | June 2 analyst upgrades: Mizuho $128 / Wells Fargo $110 / Barclays $100 (all Hold/Neutral, avg PT $112.67). After Foxconn partnership announcement June 3–4, INTC rallied to ~$130. Stock above all three upgraded PTs ($100–128). Step g risk: all Hold/Neutral ratings, stock at or above upgraded PTs. No Buy upgrades with PTs substantially above current. |

**ORCL**: Blocked — Q4 FY2026 earnings scheduled June 10 (2 trading days away = within 3-day pre-earnings window). Pre_market.md step 4. Reassess June 11 post-earnings per June 5 pre_market note.

### Sanity Check

- Cash floor: $64,433.77 / $98,986.79 = 65.1% ≥ 10% ✓
- Concurrent positions: 5/8 ✓
- Weekly new positions: 0/2 (ELEVATED_BAR cap = 2) ✓
- IT sector: $20,164.66 / $98,986.79 = 20.4% < 30% ✓
- Industrials sector: $14,374.00 / $98,986.79 = 14.5% < 30% ✓
- No new buys → no sanity trimming needed
