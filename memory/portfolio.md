# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|------------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-13T09:35 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-13T09:35 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-13T09:35 ET |

<!-- last_reconciled: 2026-05-13T09:35 ET (market_open) — equity $100,422.83 | cash $85,801.10 (85.4%) | long_market_value $14,621.73 | day P&L +$30.74 (+0.03%) vs prior close $100,392.09 | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | prices at open: GOOGL $386.94 (-2.22% vs cost), AAPL $296.35 (+4.68% vs cost), AMD $451.22 (+7.03% vs cost) | unrealized P&L: GOOGL -$105.47, AAPL +$225.17, AMD +$325.93 | total unrealized +$445.63 | stop orders: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | trailing stop status: AMD +7.03% vs avg_cost (trigger at +10% = $463.75, not yet reached) | plan.md: no planned buys or sells — no orders placed | fills today: none -->
