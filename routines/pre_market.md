# Pre-market routine — 07:00 ET weekdays

## Scope

Research overnight news and draft today's trade plan in `memory/plan.md`, using ONLY the tickers in `memory/universe.md`. **MUST NOT place any orders. MUST NOT re-screen the universe.**

Read `CLAUDE.md` and `memory/strategy.md` at the start of this run — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order.

## Gates

1. GET Alpaca `/v2/clock`. If `next_open` is not today (market holiday), POST `{"content": "market closed — skipping"}` to `DISCORD_WEBHOOK_URL` and exit.
2. Run the position reconciliation step from `CLAUDE.md`. Abort on any divergence.
3. **Universe cache freshness.** Read `expires_on` from `memory/universe.md` frontmatter. If `expires_on` is in the past (or the file is empty / placeholder), POST to `DISCORD_WEBHOOK_URL`:
   `{"content": "⚠️ Universe cache stale (expires_on=<date>) — skipping research. Next universe_refresh will fix it."}`
   Then exit 0. **Do not overwrite `plan.md`**, do not draft, do not research. Trading blind on stale data is worse than skipping a day.

## DRY_RUN check

Not strictly needed here (this routine never trades), but still read `DRY_RUN` from `strategy.md` — the value is included in the Discord message so the human knows which mode the day is running in.

## Work

1. **Load the universe.** Read the ticker table from `memory/universe.md`. These are the only tickers this routine may consider. **Do not re-screen, do not refetch the S&P 500 list, do not recompute filters** — `universe_refresh` owns all of that.
2. **Overnight news sweep.** web_search for overnight market-moving news, earnings releases, guidance updates, and analyst actions. Focus on names already in `universe.md`. Log salient items to `memory/research_log.md` (date, source, ticker, note).
3. **Shortlist 3–5 candidates from `universe.md`** with a positive fundamentals signal in the last 30 days (earnings beat, guidance raise, positive analyst revision, or clear catalyst from the news sweep).
4. **Earnings re-verification (shortlist only).** For each shortlisted candidate, web_search the next earnings date to confirm it is NOT within 3 days. The cached `earnings_date_next` in `universe.md` may be up to 7 days stale; earnings are often scheduled mid-week. Drop any candidate whose earnings now fall inside the 3-day window. Record the reason.
4b. **Halt / trading-status check (shortlist only).** For each surviving candidate, web_search `"<TICKER> stock halt"` AND fetch Alpaca `GET /v2/assets/<TICKER>`. Drop the candidate if any of: `tradable` is false, `status` is not `active`, or recent halt news is present. Record the reason in `research_log.md` and omit from `plan.md`.
5. **Draft `memory/plan.md`** for each surviving candidate:
   - Planned buy: ticker, target_qty` sized per `strategy.md` `Max position size at entry` field (currently **11%**) of current equity (from Alpaca `/v2/account`), `limit_price`, `stop_price` = `entry × 0.92`, and a 2–3 sentence thesis.
   - Planned sells: any positions whose exit criteria (per `strategy.md`) have fired since `market_close` — e.g. thesis invalidation, 60-day-with-<3%-gain rotation flag from midday.
6. **Sanity-check the plan** against `strategy.md`: cash floor ≥ 10%, max concurrent ≤ 8, max new-per-week ≤ 3 (count recent buys in `trade_log.md`), sector cap ≤ 30% (use the `sector` column in `universe.md`). Trim if needed, log the reasons in the `plan.md` notes section.

## MUST NOT

- Call Alpaca `/v2/orders`.
- Consider tickers not in `memory/universe.md`. If a compelling catalyst appears for a ticker outside the universe, note it in `research_log.md` for the human to review — do not plan a trade on it.
- Re-run any universe filters. That's `universe_refresh`'s job.
- Leave `plan.md` blank if you had candidates — if nothing qualified, write that reason explicitly under Notes.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "pre_market: <YYYY-MM-DD> — planned <TICKERS or 'no trades'>"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. POST to Discord — HTTP POST to `DISCORD_WEBHOOK_URL`, `Content-Type: application/json`, body:

```json
{"content": "🌅 PRE-MARKET <YYYY-MM-DD> (DRY_RUN: <true|false>)\nUniverse: <N> tickers (expires <YYYY-MM-DD>)\nPlanned buys: <TICKER qty @ limit, stop> ...\nPlanned sells: <TICKER — reason> ...\nTop catalyst: <one line>\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success. If the POST fails, log the failure but do NOT abort.
