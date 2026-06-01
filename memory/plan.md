# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-01

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| _(none)_ | — | — | — | — |

**Capacity constraint:** 8/8 concurrent positions — no new buys unless a position closes first.

**Contingency — execute ONLY if AMD trailing stop fires at open (fires if AMD opens ≤ $490.30):**

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| PWR | 6 | $745.00 | entry × 0.92 | Q1 2026 EPS $2.68 vs $1.98 est (+35%); revenue $7.87B +26.3% YoY; record backlog $48.5B; FY2026 guidance raised; $1B buyback; Oppenheimer Outperform PT $800 (May 28). Next earnings Jul 30 2026 (59 days, safe). Industrials; GEV+PWR = ~8.7% << 30% cap. 6 × $745 = $4,470 ≈ 4.4% equity (≤5% ✓). 1/3 weekly cap. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

No exit criteria triggered: no hard stops at current prices, no thesis invalidations, no 60-day-with-<3%-gain positions (oldest GOOGL: 26 days).

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| MSFT | 790e2653 | $379.62 | Cancel hard stop; immediately place 7% trailing stop GTC on 11 shares | 7% below actual intraday high at time of placement | +10% trigger $453.89 crossed — pre-market $467.00 (+13.2% vs avg_cost $412.63). Hard stop $379.62 provides zero protection at current price. Build conference June 2-3 could trigger sell-the-news reversal — trailing stop locks in gains. |

## Notes

### Sanity checks
- **Cash floor:** $62,310.92 / $101,173.92 = 61.6% → >> 10% minimum ✓
- **Concurrent positions:** 8/8 → at cap; no new buys unless a position exits ✓
- **Weekly new positions (week of June 1):** 0/3 used ✓
- **IT sector concentration:** AAPL+AMD+CSCO+MSFT+NVDA = ~$25,657 / $101,174 = 25.3% → under 30% cap ✓
- **Universe freshness:** expires_on 2026-06-07 → valid ✓
- **Reconciliation:** PASS — all 8 Alpaca positions match portfolio.md exactly ✓
- **All 8 stops confirmed active (Alpaca):** AAPL trailing 4225eab6 (stop $292.95) ✓, AMD trailing 9e760e91 (stop $490.30) ✓, AMZN f87a7a95 ($248.14) ✓, CSCO 54eb2e8d ($108.10) ✓, GEV 68f84ddd ($916.75) ✓, GOOGL d8219caa ($364.07) ✓, MSFT 790e2653 ($379.62) ✓, NVDA daaecbf6 ($205.43) ✓
- **Macro deferral rule:** NOT triggered — futures +0.4% (NOT down >0.4%); 10-yr yield 4.47% (NOT at multi-month high of 4.70%) ✓
- **DRY_RUN:** false

### MSFT — trailing stop conversion REQUIRED at market_open
Pre-market $467.00 (+13.2% vs avg_cost $412.63). +10% trigger $453.89 was crossed. Hard stop 790e2653 at $379.62 provides no protection. Immediately at market_open: (1) cancel stop 790e2653; (2) place trailing stop 7% trail_percent, GTC, sell 11 MSFT. Record new order ID and HWM in portfolio.md.

Catalysts: Microsoft Build conference June 2-3 (new AI coding model), $1B EY partnership, Ackman stake. Build event creates sell-the-news risk — trailing stop protects the +13.2% gain.

### AMD — elevated stop risk ⚠️
Pre-market $498.00 (+18.1%). BIS new export-control guidance (June 1) closes third-country loophole for MI350x AI accelerators to Chinese-controlled entities outside mainland China (Singapore/Malaysia routes now require license). Core US demand thesis (OpenAI 6GW + Meta $60B multi-year) unaffected; third-country Asia channel at risk.

Trailing stop 9e760e91 at $490.30 — cushion only $7.70 (1.55%). Stop may execute at market open if selling pressure continues. If AMD stop fires: execute PWR contingency buy (6 shares limit $745). DO NOT manually cut AMD ahead of the stop — the rule requires either the hard stop fires or thesis genuinely broken (this does not meet the definition: no guidance cut, no earnings miss, no fraud).

### NVDA — dividend ex-date June 4
$0.25/share × 22 shares = $5.50 cash credit. Stop $205.43 active (4.8% cushion from $215.90). No action required.

### AAPL
Pre-market $309.72 (+9.40%). Trailing stop HWM $315.00, stop $292.95 (Alpaca-managed). WWDC June 8-12 is next major catalyst. No action.

### GOOGL — stop proximity watch
Pre-market $377.69 (−4.56%). Stop $364.07 (3.6% cushion). Ex-dividend June 8 ($0.22/share). No new negative news. Monitor — if GOOGL approaches $365 intraday, midday routine should assess thesis integrity before stop triggers.

### AMZN, CSCO, GEV
All theses intact, no news. AMZN cushion 7.7%, CSCO cushion 9.7%, GEV cushion 4.5%. GEV ex-div June 16 ($0.50/share × 4 = $2.00). No action required.

### Blocked tickers (3-day earnings rule — June 3 reports)
AVGO, CRM, CRWD: all report June 3 after close. No entries June 1-3. Post-earnings reassessment June 4 — AVGO (AI chip rev $10.7B est, +140% YoY) is the priority if space opens.

### Top catalyst of the day
MSFT Build conference June 2-3: new in-house AI coding model announcement. If successful, reinforces thesis. If underwhelming, trailing stop protects +13% gain.
