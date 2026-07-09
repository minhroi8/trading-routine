# 11:30 AM Intraday Confirmation Routine

Read, in order:
1. `ai-market-brief/ai_brief_state.json`
2. `ai-market-brief/portfolio_snapshot.json`
3. Today's `ai-market-brief/brief_history/YYYY-MM-DD-am.md`

Then perform an intraday confirmation check.

The purpose is to determine whether the morning setups confirmed, failed,
became too extended, or remain unresolved. Do not generate new trade ideas
merely because a stock is moving — this routine evaluates the morning's
theses, it does not originate new ones (a genuinely exceptional,
unambiguous new event is the only exception, and must be justified
explicitly if included).

## Required process

1. Restate the morning condition for each ticker before evaluating it.
2. Use current price, intraday range, relative volume, sector movement,
   market breadth, and any fresh news since the morning brief.
3. Classify each ticker as one of: setup confirmed / setup unconfirmed /
   false breakout / failed pullback / too extended to chase / thesis
   invalidated.
4. Do not convert an intraday touch of a level into a confirmed breakout
   unless the morning condition explicitly allowed intraday confirmation.
5. Respect the invalidation basis stored in the state file exactly. A
   `daily_close` invalidation is **not** triggered by an intraday wick
   through the level — say so explicitly if a ticker wicked through its
   invalidation level intraday but the basis requires a close.
6. Actively search for fresh contradictory evidence, not just confirming
   evidence for the morning thesis.
7. Allow `WAIT` or `NO_ACTION` when the evidence is unclear.

## Required output

### 1. Intraday decision table

| Ticker | Morning condition | Current status | What changed | Next action |
|---|---|---|---|---|

Allowed statuses: `BUY_NOW`, `BUY_ONLY_IF`, `WAIT`, `HOLD`, `CANCEL_SETUP`,
`EXIT_REDUCE`.

### 2. Portfolio relevance

For each actionable name, the same three-way split as the morning routine:
- **Good company?**
- **Good stock setup?**
- **Good addition to this portfolio?**

Explain whether executing the trade would increase an existing
concentration risk, using current computed values from
`portfolio_snapshot.json` (shares × live price).

### 3. Price alerts to set now

No more than three alerts per relevant ticker: pullback alert / breakout
alert / invalidation (downside) alert. For each:
- exact price
- crossing direction
- confirmation method (e.g., once per 15-minute bar close, or daily close)
- plain-English meaning
- action to take when triggered

### 4. State changes

Only update `ai_brief_state.json` when one of the following actually
changed since the morning: status, trigger level(s), invalidation level or
basis, thesis, confidence, or the setup was confirmed/canceled. If nothing
meets this bar, state that explicitly and skip the write.

## Write-back procedure

Same validate-before-commit procedure as the 8:45 routine:
1. Validate revised JSON against schema before committing; abort and log
   on failure, leaving the last valid state untouched.
2. `git pull --rebase` before committing.
3. Commit and push only on successful validation.
4. Save the report to `brief_history/YYYY-MM-DD-1130.md`.
5. Never modify `portfolio_snapshot.json` in this routine.
