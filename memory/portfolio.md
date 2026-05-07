# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|-----------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-07T16:05 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-07T16:05 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-07T16:05 ET |

<!-- last_reconciled: 2026-05-07T16:05 ET (market_close) — equity $99,931.22 | cash $85,801.10 (85.86%) | long_market_value $14,130.12 | day P&L -$169.32 (-0.17%) | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | close prices: GOOGL $396.84, AAPL $286.68, AMD $408.58 | unrealized P&L (vs avg_cost): GOOGL +$13.38 (+0.28%), AAPL +$60.86 (+1.27%), AMD -$143.18 (-3.09%) | total unrealized -$68.94 | intraday P&L: GOOGL -$14.41 (-0.30%), AAPL -$14.11 (-0.29%), AMD -$140.97 (-3.04%) | stop orders confirmed active: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | fills today: none | SPY day -0.34% ($733.77→$731.25) | portfolio outperformed SPY (-0.17% vs -0.34%) -->
