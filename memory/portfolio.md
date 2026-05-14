# Portfolio

Snapshot of current open positions. Rewritten by `market_close` (and `market_open` after fills). Compared against Alpaca `/v2/positions` at every routine start — any divergence aborts the run.

| ticker | qty | avg_cost | stop_price | thesis | opened_date | last_reconciled |
|--------|-----|----------|------------|--------|-------------|------------------|
| GOOGL | 12 | $395.72 | $364.07 | Q1 2026 blowout: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63%; AI ROI clearly visible; next earnings ~Jul 22 2026. | 2026-05-06 | 2026-05-14T09:37 ET |
| AAPL | 17 | $283.10 | $260.45 | Q2 FY2026 beat: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings Jul 30 2026. | 2026-05-06 | 2026-05-14T09:37 ET |
| AMD | 11 | $421.59 | $387.86 | Q1 2026 blowout: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B +38% YoY; Data Center $5.8B +57% YoY; Q2 guidance $11.2B vs $10.52B est; Meta deploying 6GW Instinct GPUs. next earnings ~late Jul 2026. | 2026-05-06 | 2026-05-14T09:37 ET |
| AMZN | 18 | $269.71 | $248.14 | Q1 2026 blowout (Apr 29): EPS $2.78 vs $1.64 est (+70%), AWS $37.6B +28% YoY (fastest in 15 qtrs), custom AI chips >$20B annualized run rate; Q2 guide $194–199B (+16–19% YoY); 41 analysts Strong Buy; Trump-Xi summit AWS China tailwind. Next earnings Jul 30 2026. | 2026-05-14 | 2026-05-14T09:37 ET |

<!-- last_reconciled: 2026-05-14T09:37 ET (market_open) — equity ~$100,490 | cash ~$81,091 (after AMZN fill $4,854.86) | long_market_value ~$19,557 | fills today: AMZN 18@$269.71 (stop $248.14 placed) | CSCO limit 42@$117.50 pending (market trading ~$118.93, GTC day) | DRY_RUN: false | reconciliation: PASS (GOOGL 12 ✓, AAPL 17 ✓, AMD 11 ✓, AMZN 18 ✓ post-fill) | stop orders: GOOGL $364.07 ✓, AAPL $260.45 ✓, AMD $387.86 ✓, AMZN $248.14 ✓ | trailing stop status: AMD +4.40% vs avg_cost (trigger at +10% = $463.75, not yet reached) -->
