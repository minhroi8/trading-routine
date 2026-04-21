# Pre-market routine — 07:00 ET weekdays

## Scope

Research overnight news and draft today's trade plan in `memory/plan.md`. **MUST NOT place any orders.**

Read `CLAUDE.md` and `memory/strategy.md` at the start of this run — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order: `CLAUDE.md`, `memory/strategy.md`, `memory/portfolio.md`, `memory/plan.md`, last 30 days of `memory/trade_log.md`, last 14 days of `memory/research_log.md`, `memory/lessons.md`.

## Gates

1. GET Alpaca `/v2/clock`. If `next_open` is not today (market holiday), Slack "market closed" and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.

## DRY_RUN check

Not strictly needed here (this routine never trades), but still read `DRY_RUN` from `strategy.md` — the value is included in the Slack summary so the human knows which mode the day is running in.

## Work

1. **Universe refresh.** web_search the current S&P 500 list from SlickCharts (https://www.slickcharts.com/sp500) or Wikipedia. Cache the list under today's date in `research_log.md` with the source URL.
2. **Overnight news sweep.** web_search for overnight market-moving news, earnings releases, guidance updates, and analyst actions. Log salient items to `research_log.md`.
3. **Earnings-calendar filter.** For any ticker you're considering, confirm it is **not within 3 days** of an earnings report. Skip if it is.
4. **Screen for candidates.** Apply `strategy.md` universe filters: price ≥ $10, 20-day average dollar volume ≥ $20M, US primary listing, not an IPO < 180 days old, not halted. Shortlist 3–5 tickers with a positive fundamentals signal in the last 30 days (earnings beat, guidance raise, positive analyst revision, clear catalyst).
5. **Draft `memory/plan.md`.** For each planned buy: ticker, target_qty (sized to ≤ 5% of current equity from `/v2/account`), limit_price, stop_price = `entry × 0.92`, and a 2–3 sentence thesis. For planned sells: any positions whose exit criteria (per `strategy.md`) have fired since `market_close`.
6. **Sanity-check the plan** against `strategy.md`: cash floor ≥ 10%, max concurrent ≤ 8, max new-per-week ≤ 3 (count recent buys in `trade_log.md`), sector cap ≤ 30%. Trim if needed, log reasons in `plan.md` notes.

## MUST NOT

- Call Alpaca `/v2/orders`.
- Plan positions outside the S&P 500 universe or that fail any filter.
- Leave `plan.md` blank if you had candidates — if nothing qualified, write that reason explicitly under Notes.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "pre_market: <YYYY-MM-DD> — planned <TICKERS or 'no trades'>"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. Slack `#trading-bot`:

```
🌅 PRE-MARKET <YYYY-MM-DD> (DRY_RUN: <true|false>)
Planned buys: <TICKER qty @ limit, stop> ...
Planned sells: <TICKER — reason> ...
Top catalyst: <one line>
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
