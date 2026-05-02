---
screened_on: 1970-01-01
expires_on: 1970-01-01
total_passed: 0
total_rejected: 0
source: unset
---

# Universe

Pre-computed list of tickers that pass `memory/strategy.md` universe filters:

- S&P 500 constituent
- Price ≥ $10/share
- 20-day average dollar volume ≥ $20M
- US primary listing
- Not a recent IPO (< 180 days since listing)

**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market`, `market_open`, and `midday`. The cache is valid for 7 days — if `expires_on` is in the past, trading routines abort with a Discord notice and wait for the next weekend refresh.

The `screened_on: 1970-01-01` placeholder above guarantees the cache reads as stale until the first real `universe_refresh` run.

## Columns

- `ticker` — symbol
- `last_price` — most recent daily close used in screening (USD)
- `avg_dollar_volume_20d` — mean of `close × volume` across the last 20 trading days (USD)
- `sector` — GICS sector from the S&P 500 list source
- `earnings_date_next` — next scheduled earnings report (ISO date; `unknown` if lookup failed). `pre_market` re-verifies this for every candidate before including it in `plan.md`.
- `screened_on` — date the row was produced

| ticker | last_price | avg_dollar_volume_20d | sector | earnings_date_next | screened_on |
|--------|------------|-----------------------|--------|---------------------|-------------|

_Empty — populated by the first `universe_refresh` run._
