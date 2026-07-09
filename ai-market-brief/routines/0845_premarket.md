# 8:45 AM Premarket Routine

Read, in order:
1. `ai-market-brief/ai_brief_state.json`
2. `ai-market-brief/portfolio_snapshot.json`
3. The most recent file in `ai-market-brief/brief_history/`

Then produce an AI-focused premarket equity decision brief.

The purpose is not to generate a broad research report. The purpose is to
identify what materially changed since the saved state and decide whether
any stock has become more or less actionable.

## Required process

1. Treat the saved state (`ai_brief_state.json`) as the comparison baseline.
   Do not re-derive "what's new" from general knowledge of the news cycle —
   diff against the saved ticker entries specifically.
2. Review current primary-source and high-quality market evidence.
3. Separate every claim into: confirmed fact / market-implied signal / inference.
4. Search for evidence against the initial thesis before assigning or
   changing any rating.
5. Do not treat AI exposure as automatically bullish.
6. Do not infer supplier or customer relationships without confirmation.
7. Do not invent exact price levels when evidence does not support them —
   say what confirmation is missing instead.
8. Every invalidation must state its basis: `intraday`, `daily_close`, or
   `weekly_close`.
9. Allow the correct conclusion to be `NO_ACTION` or `INSUFFICIENT_EVIDENCE`.
10. Limit the main output to the highest-priority actionable changes —
    compress rather than cover every layer.

## Required output

### 1. What changed from saved state

| Ticker | Previous status | New status | What changed | Evidence quality |
|---|---|---|---|---|

Do not repeat unchanged tickers unless they are among the user's largest
portfolio holdings or their trigger is close to activating (within ~2% of
pullback/breakout/invalidation level).

### 2. Portfolio impact

Compute current position values from `portfolio_snapshot.json` shares ×
live price (never from a stored dollar figure). For every stock discussed,
include this literal three-way split:

- **Good company?**
- **Good stock setup?**
- **Good addition to this portfolio?**

Flag, using actual computed concentration percentages:
- excessive single-stock concentration
- overlapping AI-factor exposure (semiconductor, hyperscaler-capex,
  rate-sensitivity, speculative-position concentration)
- lack of available cash relative to any proposed new position

Do not recommend position sizing beyond what the available portfolio data
supports.

### 3. Top actionable decisions

No more than five names unless there is an exceptional market event. For
each:

- ticker
- status: `BUY_NOW`, `BUY_ONLY_IF`, `BUY_ON_PULLBACK`, `WAIT_FOR_EARNINGS`,
  `HOLD_DO_NOT_ADD`, `TRIM`, `SELL`, or `NO_ACTION`
- confidence: `high` / `medium` / `low`
- priority_rank
- current thesis
- why now versus later
- exact entry/confirmation condition, when defensible (pullback_level and/or
  breakout_level, with volume condition if applicable)
- setup type: pullback / breakout / earnings confirmation / valuation
  accumulation / watch-only
- invalidation level + basis
- strongest counterargument
- evidence that would change the rating
- next catalyst
- one-sentence execution instruction

Distinguish "good business" from "good stock at today's price" explicitly
for each name.

### 4. Updated state and alerts

- The exact revised JSON entries (matching the schema in `ai_brief_state.json`)
  for every ticker whose state changed.
- A concise alert table: pullback alert / breakout alert / invalidation
  alert, each with exact price, basis, and the action to take when triggered.

## Write-back procedure

1. Validate the full revised state object against the existing schema
   (required fields present, correct types, `confidence` and `status`
   values from the allowed enums) **before** committing.
   - If validation fails, do **not** commit. Log the specific validation
     error in the brief output instead, and leave `ai_brief_state.json`
     unchanged from its last valid commit.
2. `git pull --rebase` before committing, in case another routine run has
   updated the branch.
3. On successful validation, commit the revised `ai_brief_state.json` and
   push.
4. Save the full brief to `brief_history/YYYY-MM-DD-am.md`.
5. Do **not** modify `portfolio_snapshot.json` under any circumstances in
   this routine — it is only ever updated from real brokerage data or an
   explicit user statement.
6. Post a condensed summary to Discord via the existing PEAD bot webhook,
   using the same webhook credential path already configured for the
   other routines. The Discord message is **not** the full brief — send
   only:
   - The "What changed from saved state" table (section 1).
   - The "Top actionable decisions" table (section 3), collapsed to just
     ticker / status / confidence / priority_rank / one-sentence execution
     instruction — omit the long-form fields (thesis, counterargument,
     evidence-that-would-change-rating) to keep the message short.
   - A link or path reference to the full brief in `brief_history/` for
     anyone who wants the complete reasoning.
   - If step 1-4 resulted in `NO_ACTION` / `INSUFFICIENT_EVIDENCE` across
     the board with no state changes, send a single-line "no material
     changes since yesterday" message rather than an empty or repetitive
     table — don't post noise just to confirm the routine ran.
7. If the Discord post fails (webhook error, rate limit, etc.), do not
   retry indefinitely and do not treat it as a reason to skip or redo the
   git commit from steps 1-3 — the repo state is the source of truth:
   the Discord post is a notification layer on top of it, not a
   dependency for it.
