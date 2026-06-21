# Midday routine — 12:30 ET weekdays

## Scope

Review open positions. Cut losers past the midday threshold. Tighten stops on winners. **MUST NOT open any new positions.**

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. GET `/v2/clock` — confirm market open. Otherwise POST `{"content": "market closed — skipping"}` to `DISCORD_WEBHOOK_URL` and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.

## DRY_RUN check

Read `DRY_RUN` from `memory/strategy.md`.

- If `DRY_RUN: true`: record intended midday actions (cuts, partial profit-locks, trailing-stop conversions, thesis exits) to `plan.md` under a `### Midday intentions` section, and post them to Discord. **Do not call any Alpaca order endpoint.** Skip to End-of-run.
- If `DRY_RUN: false`: proceed to Work.

## Work (live mode)

For each open position, GET the current quote:

1. **Midday cut (hard stop or thesis break only).** Per `strategy.md`, only exit early if the **hard stop (-8% from entry) has been hit** OR the **thesis is genuinely broken** (guidance cut, earnings miss, fraud, material negative catalyst). **Do NOT cut on temporary intraday weakness alone** — backtest data shows positions held to 42 days win 65.8% of the time, so patience is the edge. If the hard stop is hit: cancel the existing stop order, then POST `market sell` for the full position, and append to `trade_log.md` with rationale `"hard stop -8% hit (midday)"`. (Thesis-break exits are handled in step 3 below.)
2. **Trailing stop on winners (+10% partial profit-lock).** If unrealized P&L vs `avg_cost` is ≥ **+10%** and the position is **not already on a trailing stop**, execute the `strategy.md` **partial profit-lock**, then trail the remainder:

   a. **Compute the 1/3 lot.** `one_third = floor(current_qty / 3)` — round **DOWN** to the nearest whole share.
   b. **If `one_third == 0`** (position too small to split): **skip the partial sell** and trail the **full** position — cancel the existing hard stop, then POST `trailing_stop sell` for the full `current_qty` with `trail_percent: 7`, `time_in_force: gtc`. Log to `trade_log.md` with rationale `"+10% trigger — position too small to split, trailed full position at 7%"`. Done with this position.
   c. **Otherwise, sell 1/3 at market.** POST a `market sell` for `one_third` shares. Wait briefly, GET `/v2/orders` to confirm the fill price.
   d. **Cancel the existing hard stop** for this ticker (confirm HTTP 204 / canceled).
   e. **Trail the remaining 2/3.** POST a `trailing_stop sell` for `remaining_qty = current_qty - one_third` with `trail_percent: 7`, `time_in_force: gtc`.
   f. **Log the partial sell** to `trade_log.md`: date, time_et, ticker, side `sell`, qty `one_third`, fill price, rationale `"partial profit-lock at +10% trailing trigger"`, and **realized P&L on the sold portion** = `(fill_price - avg_cost) × one_third`.
   g. **Update `memory/portfolio.md`**: reduce the position's `qty` to `remaining_qty` and update its `stop_price` cell to the new trailing-stop id/price. Do not change `avg_cost`.
3. **Thesis check.** web_search for material news on each ticker since market open. If news invalidates the thesis (guidance cut, fraud allegation, major negative catalyst): exit at market (cancel any existing stop first, then `market sell` the full position). Note the invalidation reason in `trade_log.md` with rationale `"thesis break (midday) — <reason>"`.
4. **Stale-position flag.** If a position has been held **60+ days** with **< 3% gain**: queue it for tomorrow's `plan.md` sell list — do NOT sell it here. Rotations happen at `market_open`, not midday.

## MUST NOT

- Open new positions (entry is `market_open`'s job).
- Adjust stops on positions outside the cut/trail rules.
- Call `/v2/orders` when `DRY_RUN: true`.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "midday: <YYYY-MM-DD> — <cuts/trails/no changes, tickers> (DRY_RUN: <true|false>)"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. POST to Discord — HTTP POST to `DISCORD_WEBHOOK_URL`, `Content-Type: application/json`, body:

```json
{"content": "🕧 MIDDAY <YYYY-MM-DD> (DRY_RUN: <true|false>)\nCuts: <TICKER @ price, P&L% — hard stop / thesis break> ...\nPartial profit-locks: <TICKER sold 1/3 (N sh) @ price, realized $X | remaining 2/3 trailed 7%> ...\nTrails (full position): <TICKER trail 7% — too small to split> ...\nStale flagged for tomorrow: <TICKER> ...\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success. If the POST fails, log the failure but do NOT abort.
