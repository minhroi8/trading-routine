# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|------------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-13T16:05 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-13T16:05 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-13T16:05 ET |

<!-- last_reconciled: 2026-05-13T16:05 ET (market_close) — equity $100,658.58 | cash $85,801.10 (85.2%) | long_market_value $14,857.48 | day P&L +$266.49 (+0.27%) vs prior close $100,392.09 | SPY day +0.71% ($738.19→$743.45) — underperformance | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | prices at close: GOOGL $403.11 (+1.87% vs cost), AAPL $299.40 (+5.76% vs cost), AMD $448.22 (+6.32% vs cost) | unrealized P&L: GOOGL +$88.63, AAPL +$277.12, AMD +$292.91 | total unrealized +$658.66 | intraday P&L: GOOGL +$189.12 (+4.07%), AAPL +$78.22 (+1.56%), AMD -$0.77 (-0.02%) | stop orders: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | trailing stop status: AMD +6.32% vs avg_cost (trigger at +10% = $463.75, not yet reached) | fills today: none -->
