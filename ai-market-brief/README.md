# ai-market-brief

A daily AI-focused equity decision system, run as two Claude Code routines
alongside the existing PEAD trading bot in this repo. Kept in its own
folder so this logic never mixes with the PEAD bot's operational files.

## Files

- **`ai_brief_state.json`** — Non-sensitive research state. One entry per
  actively-tracked ticker: status, confidence, priority rank, entry
  conditions (pullback/breakout levels, split into discrete numeric
  fields), invalidation level + basis, thesis, and strongest
  counterargument. This is the diffing baseline every routine run reads
  first and compares against before writing anything back.

- **`portfolio_snapshot.json`** — Personal position data: cash, and per
  position, share count + cost basis per share (not dollar market value —
  the routine computes current value and concentration % at read time
  using live prices, so this file only changes when you actually trade).
  **Never auto-written by either routine.** Only updated by you, from real
  brokerage data. Contains no account numbers, credentials, or tax IDs.

- **`routines/0845_premarket.md`** — The premarket routine prompt. Diffs
  against saved state, checks portfolio impact, produces up to five
  ranked actionable ideas, writes back state changes.

- **`routines/1130_intraday.md`** — The midday confirmation routine
  prompt. Checks whether the morning's setups confirmed, failed, or are
  unresolved; does not originate new theses except for a genuinely
  exceptional event. Writes back only if something actually changed.

- **`brief_history/`** — One file per run: `YYYY-MM-DD-am.md` and
  `YYYY-MM-DD-1130.md`. Append-only archive; never edited retroactively.

## Design principles

1. **State lives in the repo, not in conversation memory.** Every routine
   run reads the prior state file first — "what changed" is a real diff
   against stored values, not an inference from the news cycle.
2. **Every rating requires a bear case.** Confirmed fact, market-implied
   signal, and inference are kept explicitly separate throughout.
3. **Portfolio fit is separate from stock quality.** Every actionable name
   gets the literal three-way split — good company / good setup / good
   addition to *this* portfolio — computed against actual current
   concentration, not evaluated in isolation.
4. **Fail closed on bad writes.** Both routines validate the revised JSON
   against the schema before committing. A failed validation aborts the
   commit and leaves the last known-good state in place; it does not
   partially write or corrupt the file. `git pull --rebase` runs before
   each commit to avoid overwriting a newer state from another run.
5. **No invented numbers.** If evidence doesn't support a specific price
   level, the routine says what confirmation is missing instead of
   guessing.

## Setup checklist

- [ ] Fill in real cash balance and positions (shares + cost basis per
      share) in `portfolio_snapshot.json`; delete the example entry.
- [ ] Seed `ai_brief_state.json` with any tickers you're already tracking,
      or leave it with just the two examples for the first run to build on.
- [ ] Wire `routines/0845_premarket.md` and `routines/1130_intraday.md`
      into Claude Code the same way the seven PEAD bot routines are
      configured.
- [ ] Confirm the routine's GitHub write access is scoped to this repo
      only, the same credential path already used for `memory/lessons.md`.
