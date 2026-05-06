# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|-----------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-06T09:40 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-06T09:40 ET |

<!-- last_reconciled: 2026-05-06T09:40 ET — equity $100,000.00 | cash ~$85,761 (est.) | DRY_RUN: false | reconciliation: PASS -->
<!-- AMD limit order (6b251986-2fe5-464b-a582-7d0a69cea364) resting at $422.00 day — not yet filled as of 09:41 ET; gap-opened above limit (ask $427.50 at 09:41). Stop order NOT yet placed. Midday routine must check fill status and place stop immediately if filled. -->
