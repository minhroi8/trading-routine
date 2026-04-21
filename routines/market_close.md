# Market-close routine — 16:05 ET weekdays

## Scope

Reconcile, log the day's P&L, archive the day's plan, rotate old log entries, send the EOD Slack summary. **MUST NOT place orders.**

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence (but still post the Slack failure so the human sees it).
2. No market-open check needed — this routine runs after 16:00 ET by design.

## DRY_RUN check

This routine never trades, so `DRY_RUN` doesn't gate any action. Still read it and include the value in the Slack summary.

## Work

1. **Account snapshot.** GET `/v2/account` — record `equity`, `buying_power`, `cash`. Compute day P&L vs the previous `portfolio.md` equity stamp (or vs `/v2/account/portfolio/history?period=1D,timeframe=1D` if simpler).
2. **Position snapshot.** GET `/v2/positions` — rewrite `memory/portfolio.md` as the source-of-truth snapshot with `last_reconciled` set to now.
3. **Archive today's plan.** Copy `memory/plan.md` → `memory/archive/plan_<YYYY-MM-DD>.md`, then reset `memory/plan.md` to the empty template.
4. **Rotate logs.** Move `trade_log.md` entries older than 30 days to `memory/archive/trade_log_<YYYY-MM>.md`. Move `research_log.md` entries older than 14 days to `memory/archive/research_log_<YYYY-MM>.md`.
5. **SPY comparison.** web_search SPY's day return (or compute from a quote API). Append a one-line EOD summary to `research_log.md`:
   `EOD <YYYY-MM-DD> — equity $<X>, day P&L $<Y> (<z>%), SPY day <z>%`

## MUST NOT

- Place, modify, or cancel orders.
- Edit `memory/strategy.md` or `memory/lessons.md`.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "market_close: <YYYY-MM-DD> — equity $<X>, day P&L <pct>% (DRY_RUN: <true|false>)"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. Slack `#trading-bot`:

```
🔚 CLOSE <YYYY-MM-DD> (DRY_RUN: <true|false>)
Equity: $<X> | Day P&L: $<Y> (<z>%) | SPY day: <z>%
Positions: <N> | Cash: <pct>%
Fills today: <TICKERS or "none">
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
