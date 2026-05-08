# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|-----------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-08T12:07 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-08T12:07 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-08T12:07 ET |

<!-- last_reconciled: 2026-05-08T12:07 ET (midday) — equity ~$100,397.07 | cash $85,801.10 (85.46%) | long_market_value $14,595.97 | intraday P&L +$440.56 (+0.44%) | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | prices at 12:07 ET: GOOGL $398.76 (+0.77% vs cost), AAPL $292.57 (+3.34% vs cost), AMD $439.75 (+4.31% vs cost) | unrealized P&L (vs avg_cost): GOOGL +$36.43 (+0.77%), AAPL +$160.91 (+3.34%), AMD +$199.74 (+4.31%) | total unrealized +$397.08 | intraday P&L: GOOGL +$9.24 (+0.19%), AAPL +$87.13 (+1.78%), AMD +$344.19 (+7.66%) | stop orders: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | midday actions: none (no cuts, no trail conversions, no thesis exits, no stales) -->
