# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|------------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-08T16:05 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-08T16:05 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-08T16:05 ET |

<!-- last_reconciled: 2026-05-08T16:05 ET (market_close) — equity $100,553.71 | cash $85,801.10 (85.3%) | long_market_value $14,752.61 | day P&L +$597.19 (+0.60%) vs prior close $99,956.52 | SPY day +0.80% ($731.53→$737.42) — slight underperformance | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | prices at close: GOOGL $400.70 (+1.26% vs cost), AAPL $293.68 (+3.74% vs cost), AMD $450.15 (+6.77% vs cost) | unrealized P&L: GOOGL +$59.71, AAPL +$179.86, AMD +$314.14 | total unrealized +$553.71 | intraday P&L: GOOGL +$32.52 (+0.68%), AAPL +$106.08 (+2.17%), AMD +$458.59 (+10.21%) | stop orders: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | trailing stop status: AMD +6.77% vs avg_cost (trigger at +10% = $463.75, not yet reached) | fills today: none -->
