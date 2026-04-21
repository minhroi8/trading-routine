# Weekly review — Friday 16:30 ET

## Scope

Score the week, compare vs SPY, and propose rule changes by appending to `memory/lessons.md`. **MUST NOT place orders. MUST NOT edit `strategy.md`** — only the human operator does that. **MUST NOT edit `portfolio.md`** — that's `market_close`'s responsibility.

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order, plus last 14 days of `trade_log.md` and `research_log.md` (not just 30/14-day windows — this routine looks across the whole week).

## Gates

1. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.
2. No clock check — the week's close has already happened.

## DRY_RUN check

This routine never trades. Still read `DRY_RUN` and include it in the Slack summary.

## Work

1. **Portfolio history.** GET `/v2/account/portfolio/history?period=1W&timeframe=1D`. Compute weekly return = `(equity_end - equity_start) / equity_start`.
2. **SPY benchmark.** web_search SPY's 1-week return for the same Mon→Fri window (or compute from quote history).
3. **Trade stats (this week).**
   - Total trades (fills)
   - Win rate = closed trades with P&L > 0 / closed trades
   - Average win %, average loss %
   - Best and worst closed trades (ticker, P&L, whether thesis held up)
4. **Thesis audit.** For each closed trade this week, did the thesis play out? Why or why not? Log patterns.
5. **Rule adherence audit.** Did any run breach sizing (5% cap), cash floor (10%), sector cap (30%), or max-3-new-per-week? Flag each breach with the run and reason.
6. **Append to `memory/lessons.md`**:

```
## Week of <YYYY-MM-DD> (Mon date of the week)

- Perf: portfolio <+/-X.X>% vs SPY <+/-Y.Y>% (delta <Z.Z> pts)
- Trades: <N> total, <W> wins / <L> losses (win rate <pct>%)
- Avg win: <+X.X>% | Avg loss: <-Y.Y>%
- Best: <TICKER> <+X.X>% — <thesis note>
- Worst: <TICKER> <-Y.Y>% — <thesis note>
- What worked: <bullets>
- What didn't: <bullets>
- Rule adherence: <clean | breach notes>
- Proposed rule changes (for human review, not applied automatically):
  - <suggestion>
```

## MUST NOT

- Place orders.
- Edit `memory/strategy.md`.
- Rewrite `memory/portfolio.md` (append-only notes into `lessons.md` is the lane).
- Skip the commit/push step even if there's nothing noteworthy — record a "quiet week" entry.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "weekly_review: week of <YYYY-MM-DD> — port <pct>% vs SPY <pct>%"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. Slack `#trading-bot`:

```
📊 WEEKLY REVIEW — week of <YYYY-MM-DD> (DRY_RUN: <true|false>)
Portfolio: <+/-X.X>% | SPY: <+/-Y.Y>% | Delta: <Z.Z> pts
Trades: <N> (<W>W / <L>L, win rate <pct>%)
Top lesson: <one line>
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
