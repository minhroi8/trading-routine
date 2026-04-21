# Market-open routine — 09:35 ET weekdays

## Scope

Execute the orders listed in `memory/plan.md` and set hard stops. **MUST NOT open positions that aren't in `plan.md`.**

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. GET `/v2/clock` — confirm `is_open: true`. Otherwise Slack "market closed" and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.
3. Re-check each planned buy against `strategy.md` right before sending the order: 5% sizing using **current** equity from `/v2/account`, 90% cash floor, max concurrent 8, max new-per-week 3, 30% sector cap. Drop any that no longer fit — log the reason in `trade_log.md` notes column.
4. **Halt / trading-status gate (per order).** For each ticker in `memory/plan.md` — both planned buys and planned sells — fetch Alpaca `GET /v2/assets/<TICKER>`. If `tradable` is false or `status` is not `active`: **skip the order**, append a skip row to `memory/trade_log.md` with rationale `"halted / not-tradable per /v2/assets (status=<status>, tradable=<bool>)"`, and post a warning to Slack `#trading-bot`. **Do not send the order.** A halted position you already hold stays put; it will be re-evaluated at midday or when the halt lifts.

## DRY_RUN check

Read `DRY_RUN` from `memory/strategy.md` frontmatter.

- If `DRY_RUN: true`: write intended orders to `plan.md` under a `### Simulated fills` section with the hypothetical fill price (use the current quote) and stop price. **Do not call `/v2/orders`.** Still run all gates and reconciliation. Skip to End-of-run.
- If `DRY_RUN: false`: proceed to Execute.

## Execute (live mode only)

1. **Planned sells first.** For each, POST `/v2/orders` as `market` `sell` for the full position. On fill: remove the position from `portfolio.md`, append a row to `trade_log.md` (with rationale), and cancel any existing stop order for that ticker.
2. **Planned buys.** For each, POST `/v2/orders` as `limit` `buy` with `limit_price` from plan; `time_in_force: day`.
3. **Wait briefly, then GET `/v2/orders`** to check fills.
4. **For each filled buy**: immediately POST a child order `stop` `sell`, `qty = filled qty`, `stop_price = fill_price × 0.92`, `time_in_force: gtc`.
5. **Append every fill to `trade_log.md`**: date, time_et, ticker, side, qty, price, 2–3-sentence rationale copied from plan, and `commit_sha` left as `<pending>` (updated during End-of-run step 3 via a sed/replace before commit — OR simply left `<pending>` and backfilled next run; do whichever your implementation prefers, but be consistent).
6. **Rewrite `memory/portfolio.md`** from `/v2/positions` after all fills: each row = ticker, qty, avg_cost, stop_price, thesis, opened_date, last_reconciled (now).

## MUST NOT

- Place orders for tickers absent from `plan.md`.
- Skip the stop-loss child order.
- Trade pre-market or extended hours.
- Use market orders for entries (limit only); market orders are OK only for exits where speed matters.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "market_open: <YYYY-MM-DD> — filled <TICKER qty@price> ... (DRY_RUN: <true|false>)"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. Slack `#trading-bot`:

```
🔔 MARKET-OPEN <YYYY-MM-DD> (DRY_RUN: <true|false>)
Filled: <TICKER qty @ fill_price, stop @ stop_price> ...
Skipped: <TICKER — reason> ...
Portfolio: <N> positions | Cash: <pct>%
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
