# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|-----------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-07T09:39 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-07T09:39 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-07T09:39 ET |

<!-- last_reconciled: 2026-05-07T12:10 ET (midday) — equity $99,914.14 | cash $85,801.10 (85.87%) | long_market_value $14,113.04 | day P&L -$186.40 (-0.186%) | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓) | intraday prices: GOOGL $394.52, AAPL $289.36, AMD $405.92 | unrealized P&L (vs avg_cost): GOOGL -$14.45 (-0.30%), AAPL +$106.42 (+2.21%), AMD -$172.39 (-3.72%) | total unrealized -$80.42 | intraday P&L: GOOGL -$42.24 (-0.88%), AAPL +$31.45 (+0.64%), AMD -$170.17 (-3.67%) | stop orders confirmed active: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓ | midday actions: no cuts (all above -5% intraday threshold), no trailing stops (no position ≥+10%), no stale positions (all 1 day old), all theses intact -->
