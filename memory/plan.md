# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-10 (Wednesday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — | No exit criteria fired. PWR + SNDK theses intact (see Notes). |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | Neither position is +10%; both negative. No conversion. |

## Notes

**Gates (all PASS).** Clock: is_open=false, next_open=2026-06-10T09:30 ET — market opens today (not a holiday). Reconciliation PASS (2/2): PWR 15 @ $707.0493 ✓, SNDK 6 @ $1,643.6933 ✓ — match Alpaca exactly. Both stops confirmed active (PWR $650.49 order 10b684b0; SNDK $1,512.20 order 9362a074). Universe cache valid (expires 2026-06-14). Equity $97,780.82, cash $78,054.08 (79.83%). DRY_RUN: false.

**PEAD signal-health posture: ELEVATED_BAR (fresh).** `pead_health.md` computed 2026-06-05, expires 2026-06-12 (valid today). realized_health_60d_pct = −2.08%, health_sample_n = 211, health_ok = false. For THIS session: EPS-surprise threshold raised to **>20% for ALL sectors** (overriding standard 15%) and **max new positions capped at 2**. Overlay tightens entries only; never affects exits.

**SPY 200-day regime: BULL.** SPY close $737.07 (Jun 9) > 200d MA $684.92 (computed from IEX bars, n=200). Bear-regime rule NOT triggered. This is the "bull-and-weak" case: signal-health leg raises the bar even though SPY is above its 200MA. When both a regime cap and the health cap would apply, use the stricter — here only ELEVATED_BAR applies (cap 2 new).

**Macro (Jun 10).** Risk-off: U.S.–Iran conflict escalation (strikes near Strait of Hormuz; oil rising), S&P futures lower, Polymarket implying ~22% odds of a higher open. **May CPI released this morning** — consensus 4.2% YoY (first >4% since May 2023), inflation risk. 10-yr yield ~4.57% — NOT at multi-month high (peak 4.70% May 20). **Macro deferral rule NOT triggered** (requires BOTH futures down >0.4% AND yield at multi-month high; yield condition fails). Bar is already at >20% via ELEVATED_BAR regardless.

**Candidates researched — 0 qualified.**
- **CRM (Salesforce, IT)** — only recent in-window EPS beat clearing the raised >20% gate (Q1 May 27: EPS $3.88 vs $3.13 = +24%). **DROPPED at step f (relative strength).** 5-day return −12.67% vs SPY −2.95% = **−9.72% RS spread**, strongly negative; closed $175.41 Jun 9 (another −3.9% day). Structural downtrend: −19.86% trailing 1-yr, 52-wk high $276.80 ≈ 52% above current (step d downrank, >90 days). The +24% beat does not overcome a collapsing tape — exactly the "beat-but-drifting-down" profile ELEVATED_BAR exists to filter. Score well below 6/10.
- **ADBE (Adobe, IT)** — reports Q2 FY2026 **June 11 (tomorrow)** → inside the 3-day earnings window. Blocked (step 4). Reassess Jun 12+.
- **ORCL (Oracle, IT)** — reports Q4 FY2026 **today June 10 after close** → earnings event, not a PEAD entry (results not out at pre-market). Blocked. Reassess Jun 11+.
- **Analyst-revision / catalyst names carried from Jun 9 (EPS-threshold-exempt) remain disqualified, and a risk-off open only worsens their RS:** META (step f RS negative), AVGO (step f RS strongly negative), TTWO (step g — repeated GTA6 delay risk), INTC (step g — stock above max analyst PT), MRVL/watchlist (step g — mean PT $233 below price; reassess post-Jun 22 S&P 500 inclusion).

No compelling catalyst surfaced for any non-universe / non-watchlist ticker → no watchlist additions (no `pending_review` flag this session).

**Open positions — thesis checks (both HOLD, no exit fired):**
- **PWR (Industrials) 15 @ $707.0493** — pre-market $680.00 (−1.73% intraday, −3.83% total). Stop $650.49 (10b684b0), cushion **4.34%**. Thesis intact/reinforced: FY2026 guidance raised (rev $34.7–35.2B, adj EPS $13.55–14.25), backlog ~$50B, Oppenheimer Outperform PT $800, Buy consensus mean PT $761, data-center/grid modernization expansion. No exit criterion fired (held 8 days; not −8%; not 60-day stale). HOLD.
- **SNDK (IT) 6 @ $1,643.6933** — pre-market $1,587.79 (−3.57% intraday, −3.40% total). Stop $1,512.20 (9362a074), cushion **4.76%**. Thesis reinforced: PT hikes BofA $2,100 / Cantor $2,900 / Mizuho $2,200 (all Buy); Q3 EPS +67.2% beat, $42B backlog, Q4 guide EPS $30–33. No exit criterion fired (held 5 days). HOLD. (Drift on a risk-off semiconductor tape, not a thesis break.)

**Sanity check vs strategy.md:** cash floor 79.83% ≫ 10% ✓; concurrent 2/8 ✓; new-per-week 0/2 used (ELEVATED_BAR cap 2), 0 planned ✓; sector exposure PWR Industrials ~10.4% + SNDK IT ~9.7%, both ≪ 30% ✓. Deployment remains low (~20% invested) — persistent ELEVATED_BAR cash drag noted in weekly_review; not a rule breach (the overlay raises the bar, it does not halt). No trims required.
