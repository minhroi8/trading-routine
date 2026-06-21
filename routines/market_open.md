# Market-open routine — 09:35 ET weekdays

## Scope

Execute the orders listed in `memory/plan.md` and set hard stops. **MUST NOT open positions that aren't in `plan.md`.**

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. GET `/v2/clock` — confirm `is_open: true`. Otherwise POST `{"content": "market closed — skipping"}` to `DISCORD_WEBHOOK_URL` and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.
3. Re-check each planned buy against `strategy.md` right before sending the order: position sizing per `strategy.md` (`Max position size at entry` field, currently **11%**) using **current** equity from `/v2/account`, 90% cash floor, max concurrent 8, max new-per-week **5** (**≤ 2** if the day's plan was drafted under `ELEVATED_BAR` posture or the SPY bear-regime rule — `pre_market` already enforced this when sizing the plan), 30% sector cap. Drop any that no longer fit — log the reason in `trade_log.md` notes column.
4. **EMA entry filter (per planned buy).** For each planned buy, fetch the last 21 daily bars from Alpaca `GET /v2/stocks/{ticker}/bars?timeframe=1Day&limit=21&feed=iex`. Calculate the 21-day EMA. If the current price (from `/v2/quotes/{ticker}`) is **below** the 21-day EMA at entry time: **skip this order for today**, log `"deferred — price below 21 EMA at entry (price=$X, EMA=$Y)"` in `trade_log.md` notes column, and POST a note to `DISCORD_WEBHOOK_URL`. Do NOT permanently drop the candidate — pre_market will re-evaluate tomorrow. If price is above 21 EMA: proceed with the order.
5. **Halt / trading-status gate (per order).** For each ticker in `memory/plan.md` — both planned buys and planned sells — fetch Alpaca `GET /v2/assets/<TICKER>`. If `tradable` is false or `status` is not `active`: **skip the order**, append a skip row to `memory/trade_log.md` with rationale `"halted / not-tradable per /v2/assets (status=<status>, tradable=<bool>)"`, and POST a warning to `DISCORD_WEBHOOK_URL`. **Do not send the order.** A halted position you already hold stays put; it will be re-evaluated at midday or when the halt lifts.

## DRY_RUN check

Read `DRY_RUN` from `memory/strategy.md` frontmatter.

- If `DRY_RUN: true`: write intended orders to `plan.md` under a `### Simulated fills` section with the hypothetical fill price (use the current quote) and stop price. Include any intended **+10% partial profit-locks** (the simulated 1/3 market sell and the 2/3 trailing-stop conversion). **Do not call `/v2/orders`.** Still run all gates and reconciliation, including the EMA check. Skip to End-of-run.
- If `DRY_RUN: false`: proceed to Execute.

## Execute (live mode only)

1. **Planned sells first.** For each, POST `/v2/orders` as `market` `sell` for the full position. On fill: remove the position from `portfolio.md`, append a row to `trade_log.md` (with rationale), and cancel any existing stop order for that ticker.

1b. **Trailing-stop conversions (+10% partial profit-lock).** Process each row in `plan.md`'s **Trailing stop conversions (market_open actions)** table — these are positions that `market_close`/`pre_market` flagged as having crossed the **+10%** trailing trigger. For each such position (skip any already on a trailing stop), execute the `strategy.md` **partial profit-lock**, then trail the remainder:
   a. **Compute the 1/3 lot.** `one_third = floor(current_qty / 3)` — round **DOWN** to the nearest whole share.
   b. **If `one_third == 0`** (position too small to split): **skip the partial sell** and trail the **full** position — cancel the existing hard stop, then POST `trailing_stop sell` for the full `current_qty` with `trail_percent: 7`, `time_in_force: gtc`. Log to `trade_log.md` with rationale `"+10% trigger — position too small to split, trailed full position at 7%"`. Done with this row.
   c. **Otherwise, sell 1/3 at market.** POST a `market sell` for `one_third` shares. Wait briefly, then GET `/v2/orders` to confirm the fill price.
   d. **Cancel the existing hard stop** for this ticker (confirm HTTP 204 / canceled).
   e. **Trail the remaining 2/3.** POST a `trailing_stop sell` for `remaining_qty = current_qty - one_third` with `trail_percent: 7`, `time_in_force: gtc`.
   f. **Log the partial sell** to `trade_log.md`: date, time_et, ticker, side `sell`, qty `one_third`, fill price, rationale `"partial profit-lock at +10% trailing trigger"`, and **realized P&L on the sold portion** = `(fill_price - avg_cost) × one_third`.
   g. **Reflect the reduced share count** in `portfolio.md` (qty → `remaining_qty`, update the `stop_price` cell to the new trailing-stop id/price; leave `avg_cost` unchanged). The step-6 portfolio rewrite from `/v2/positions` will confirm this.

2. **Planned buys.** For each surviving planned buy (passed all gates including EMA filter), POST `/v2/orders` as `limit` `buy` with `limit_price` from plan; `time_in_force: day`.
3. **Wait briefly, then GET `/v2/orders`** to check fills.
4. **For each filled buy**: immediately POST a child order `stop` `sell`, `qty = filled qty`, `stop_price = fill_price × 0.92`, `time_in_force: gtc`.
5. **Append every fill to `trade_log.md`**: date, time_et, ticker, side, qty, price, 2–3-sentence rationale copied from plan, and `commit_sha` left as `<pending>` (updated during End-of-run step 3 via a sed/replace before commit — OR simply left `<pending>` and backfilled next run; do whichever your implementation prefers, but be consistent).
6. **Rewrite `memory/portfolio.md`** from `/v2/positions` after all fills: each row = ticker, qty, avg_cost, stop_price, thesis, opened_date, last_reconciled (now).

## MUST NOT

- Place orders for tickers absent from `plan.md`.
- Skip the stop-loss child order.
- Trade pre-market or extended hours.
- Use market orders for entries (limit only); market orders are OK only for exits where speed matters.
- Permanently drop a candidate solely because of the EMA filter — log and defer to tomorrow only.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "market_open: <YYYY-MM-DD> — filled <TICKER qty@price> ... (DRY_RUN: <true|false>)"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. POST to Discord — HTTP POST to `DISCORD_WEBHOOK_URL`, `Content-Type: application/json`, body:

```json
{"content": "🔔 MARKET-OPEN <YYYY-MM-DD> (DRY_RUN: <true|false>)\nFilled: <TICKER qty @ fill_price, stop @ stop_price> ...\nPartial profit-locks: <TICKER sold 1/3 (N sh) @ price, realized $X | remaining 2/3 trailed 7%> or none\nSkipped: <TICKER — reason> ...\nDeferred (EMA): <TICKER — price $X below 21 EMA $Y> ...\nPortfolio: <N> positions | Cash: <pct>%\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success. If the POST fails, log the failure but do NOT abort.
