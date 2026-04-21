# Midday routine — 12:30 ET weekdays

## Scope

Review open positions. Cut losers past the midday threshold. Tighten stops on winners. **MUST NOT open any new positions.**

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. GET `/v2/clock` — confirm market open. Otherwise Slack and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.

## DRY_RUN check

Read `DRY_RUN` from `memory/strategy.md`.

- If `DRY_RUN: true`: record intended midday actions (cuts, trails, thesis exits) to `plan.md` under a `### Midday intentions` section, and post them to Slack. **Do not call any Alpaca order endpoint.** Skip to End-of-run.
- If `DRY_RUN: false`: proceed to Work.

## Work (live mode)

For each open position, GET the current quote:

1. **Midday cut.** If unrealized intraday P&L is worse than **-5%**: cancel the existing stop order, then POST `market sell` for the full position. Append to `trade_log.md` with rationale `"midday cut per strategy.md"`.
2. **Trailing stop on winners.** If unrealized P&L ≥ **+10%** and the position doesn't already have a trailing stop: cancel the existing stop, POST `trailing_stop sell` with `trail_percent: 7`, `time_in_force: gtc`.
3. **Thesis check.** web_search for material news on each ticker since market open. If news invalidates the thesis (guidance cut, fraud allegation, major negative catalyst): exit at market. Note the invalidation reason in `trade_log.md`.
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
5. Slack `#trading-bot`:

```
🕧 MIDDAY <YYYY-MM-DD> (DRY_RUN: <true|false>)
Cuts: <TICKER @ price, P&L%> ...
Trails tightened: <TICKER trail 7%> ...
Stale flagged for tomorrow: <TICKER> ...
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
