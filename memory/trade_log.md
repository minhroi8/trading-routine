# Trade Log

Append-only ledger of every fill. Entries older than 30 days are rotated to `memory/archive/trade_log_<YYYY-MM>.md` at the start of each run.

| date | time_et | ticker | side | qty | price | rationale | commit_sha |
|------|---------|--------|------|-----|-------|-----------|------------|
| 2026-05-14 | 09:36 ET | AMZN | buy | 18 | $269.71 | Q1 2026 blowout (Apr 29): EPS $2.78 vs $1.64 est (+70%), AWS $37.6B +28% YoY (fastest in 15 qtrs), custom AI chips >$20B annualized run rate; Q2 guide $194–199B (+16–19% YoY); 41 analysts Strong Buy, avg PT $306; Trump-Xi summit tailwind (potential AWS China unlock). Limit 18@$272.00 filled at $269.71 (better than limit). Stop placed at $248.14 (−8%). | <pending> |
| 2026-05-06 | 09:40 ET | GOOGL | buy | 12 | $395.72 | Q1 2026 blowout reported April 30: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63% YoY; AI ROI clearly visible; next earnings ~July 22 2026 (>3 months out). Stop placed at $364.07 (−8%). | 8d21c44 |
| 2026-05-06 | 09:40 ET | AAPL | buy | 17 | $283.10 | Q2 FY2026 beat reported April 30: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; next earnings July 30 2026. Stop placed at $260.45 (−8%). | 8d21c44 |
| 2026-05-06 | 09:48 ET | AMD | buy | 11 | $421.59 | Q1 2026 blowout reported May 5 after close: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B vs $9.89B est (+38% YoY); Data Center $5.8B +57% YoY on MI-series AI accelerator demand; Q2 guidance $11.2B vs $10.52B est; Meta deploying up to 6GW AMD Instinct GPUs. Limit order placed at market_open filled at $421.59; stop placed at $387.86 (−8%) by midday routine. | 5bbbe59 |
