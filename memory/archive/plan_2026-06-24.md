# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-24 (pre_market ~08:03 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates cleared the ELEVATED_BAR >20% EPS all-sectors bar. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8 positions, 100% cash) — nothing to sell. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | No open positions. |

## Notes

- **Gates PASS.** Clock: is_open=false, next_open 2026-06-24T09:30 ET — market opens today (Wed), NOT a holiday → routine proceeds. Reconciliation **0/0 PASS**: Alpaca `/v2/positions` = [] (empty) MATCHES portfolio.md FLAT book — zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity **$99,074.58**, cash $99,074.58 (**100%**), buying_power $396,298.32. No open orders (no orphan stops; book clean). Universe expires 2026-06-28 (fresh, 4d). 0/8 concurrent.
- **PEAD posture: ELEVATED_BAR** (pead_health.md: realized −0.492%, n=367, computed Jun 21 / expires Jun 28 — fresh; health_ok=false) → entry bar raised to **>20% EPS for ALL sectors**, **max 2 new positions** this session.
- **SPY regime: BULL** (close $733.62 [Jun 23 IEX] > 200MA $689.26, n=200, margin +$44.36). Standard thresholds would apply, but ELEVATED_BAR governs the higher bar.
- **Macro: STRESSED but deferral rule NOT triggered.** S&P 500 futures **−1.5%** (exceeds the >0.4% leg) on a broad AI/semiconductor selloff (KOSPI −10%, Samsung/SK Hynix −10%+, Nasdaq-100 futures −2.6%, Dow futures −0.7%). 10-yr Treasury yield **~4.48%** (slipped 3bps) — **NOT** at a multi-month high (peak 4.70% May 20). The macro-deferral rule requires BOTH legs (futures down >0.4% AND 10-yr at multi-month high); only one met → NOT triggered. Bar is already >20% via ELEVATED_BAR regardless. The semi-led risk-off tape directly raises step-g/risk-check stop-out odds for any volatile chip name.
- **Candidates screened — 0 qualified under ELEVATED_BAR:**
  - **FDX** (Industrials) — fresh reporter (Q4 FY2026, after close Jun 23): adj **EPS $6.31 vs $6.02 = +4.8% beat**, revenue $25.0B vs $24.28B = +3.0% beat, CY2026 guide adj EPS $16.90–18.10 / rev ~+11%. **DROP step a** — +4.8% surprise is far below the >20% ELEVATED_BAR bar (Industrials also independently requires >20% per strategy.md). Last quarter before the FedEx Freight spin-off (completed Jun 1).
  - **MU** (IT) — reports **tonight Wed Jun 24 after close, INSIDE the 3-day earnings window** → **blocked** for new entries (event risk). BofA raised PT to $1,500 (from $950) Jun 23, 6 straight quarters of beats — revisit only after it reports and clears the window.
  - **MRVL** (watchlist `active`, also in universe since the Jun 22 S&P 500 inclusion) — earnings path FAILS (Q1 FY2027 ~May 22, EPS $0.80 vs $0.79 = +1.3% « >20%). Analyst-revision/catalyst path: BofA PT→$365 (Jun 23) and KeyBanc $385 (Jun 18) are fresh bullish outliers, but consensus **mean PT ~$238.75** (41 analysts) — cur **$279.115** (Jun 23 close, −9.5% on the day) still trades **~17% ABOVE consensus**. **DROP step f/g** — negative momentum into the selloff (−9.5% Jun 23, another leg down expected on the −2.6% Nasdaq-futures AI rout), extreme ±10–17%/day volatility ⇒ a fixed −8% hard stop very likely fires on noise; ELEVATED_BAR demands highest-conviction only. Watchlist status stays `active` (human-only); reassess on a quieter base or if the consensus mean (not just outliers) clears $300.
  - Carried drops (no fresh catalyst): KR (+2.2% « bar), CRM (+24% May 27 but anti-PEAD drift), ADBE (+6.43%), ORCL (+11.64%) — all fail the >20% bar or step f.
- **No non-universe catalyst** warranting a watchlist `pending_review` add (still the Q1/Q2 earnings desert; prior 20%+ beaters all >40d stale).
- **No exits / no conversions** — book is FLAT (0 positions). Weekly new-position slots 0/2 used (ELEVATED_BAR cap). DRY_RUN: false.
