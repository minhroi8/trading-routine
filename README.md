# trading-routine

A 24/7 AI trading agent built with Claude Code Routines. Claude Opus 4.7 runs scheduled prompts that research, plan, and (paper-)trade US equities on Alpaca — aiming to beat SPY over months with fundamentals-based swing trades.

## How it works

Each routine run is **stateless**. All memory lives as markdown files in this repo. Every run:

1. Reads `CLAUDE.md` + `memory/*.md` for current state.
2. Reconciles `memory/portfolio.md` against Alpaca's live positions (abort on any divergence).
3. Does its scoped work (research / execute / review / close / weekly).
4. Updates touched memory files.
5. Commits and pushes to `main` — the next run sees the changes.

## Routines (US Eastern time)

| Time           | Routine                         | Scope                                                     |
| -------------- | ------------------------------- | --------------------------------------------------------- |
| Sun 18:00      | `routines/universe_refresh.md`  | Rebuild `memory/universe.md` cache (7-day TTL)            |
| 07:00 (wkday)  | `routines/pre_market.md`        | Research, draft `plan.md` from `universe.md` — **no trades** |
| 09:35 (wkday)  | `routines/market_open.md`       | Execute `plan.md`, set -8% stops                          |
| 12:30 (wkday)  | `routines/midday.md`            | Cut losers past -5%, trail winners past +10%              |
| 16:05 (wkday)  | `routines/market_close.md`      | Log P&L, archive plan, rotate logs, EOD Slack             |
| Fri 16:30      | `routines/weekly_review.md`     | Score vs SPY, append to `lessons.md`                      |

## Safety

- **`DRY_RUN: true`** flag in `memory/strategy.md` — for the first 14 days, `market_open` and `midday` write intended orders to `plan.md` and Slack but call no Alpaca order endpoint. Only a human edit to `strategy.md` flips it off.
- Hard scope per routine: `pre_market` cannot trade, `midday` cannot open new positions, `weekly_review` cannot edit `strategy.md`, etc.
- Every run reconciles memory vs live Alpaca state; any divergence aborts the run and posts a `RECONCILIATION FAIL` to Slack.
- Strategy guardrails: 5% max position size, 8 max concurrent, 3 max new-per-week, 30% sector cap, 10% cash floor, -8% hard stop. Full rules in `memory/strategy.md`.

## Secrets

Set these env vars in the routine environment — never in the repo:

- `ALPACA_API_KEY_ID`
- `ALPACA_SECRET_KEY`
- `ALPACA_BASE_URL` (= `https://paper-api.alpaca.markets`)

`.gitignore` excludes `.env`, `.env.*`, `*.key`, and `secrets/`.

## Repo layout

```
CLAUDE.md                 system rules loaded at the start of every run
memory/
  strategy.md             sizing, risk, universe, entry/exit rules (DRY_RUN flag)
  portfolio.md            current positions snapshot
  plan.md                 today's intended orders (pre_market → market_open handoff)
  universe.md             weekly pre-computed tradable universe (7-day cache)
  trade_log.md            append-only ledger of every fill
  research_log.md         dated catalyst + macro notes
  lessons.md              weekly reviews
  archive/                rotated logs and archived daily plans
routines/
  universe_refresh.md
  pre_market.md
  market_open.md
  midday.md
  market_close.md
  weekly_review.md
```

## Notifications

Every routine ends with a summary posted to Slack `#trading-bot` (via the Claude Slack connector), including the commit SHA and a link to the commit on GitHub.
