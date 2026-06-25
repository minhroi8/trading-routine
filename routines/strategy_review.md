# Strategy Review routine — Saturday 10:00 ET (weekly, market-independent)

## Scope

Read accumulated weekly_review proposals from `memory/lessons.md`, cross-check against the current live `memory/strategy.md`, rank every still-open proposal by evidence strength, backtest only the STRONG ones, and post a ranked report to Discord + append it to a running log. **This routine RECOMMENDS only. It MUST NOT edit `memory/strategy.md` or any other live routine file. It never places trades.**

Read `CLAUDE.md` and `memory/strategy.md` at the start of this run — they supersede anything below.

## Load

Per `CLAUDE.md` start-of-run order, plus:
- `memory/lessons.md` (full — this is the proposal source)
- `memory/strategy.md` (to detect which proposals are already implemented)
- `backtesting/strategy_review_log.md` (the running log this routine maintains — create it if absent)
- `backtesting/scripts/` (the backtest scripts, for STRONG-proposal validation)

## Gates

1. This routine does not trade and has no market dependency. No clock check needed.
2. Run the position reconciliation step from `CLAUDE.md` as a read-only sanity check (do NOT abort the review if it diverges — just note it in the report; market_close owns reconciliation).
3. **Anti-overfitting guard (critical).** Before backtesting anything, read `backtesting/strategy_review_log.md` and count how many times each proposal has already been backtested. A proposal that has been backtested and rejected twice MUST NOT be re-backtested a third time on the same periods — re-running tweaked variants against the same data until something passes is curve-fitting. Instead, mark it `EXHAUSTED — needs new data or manual review` and stop testing it. Log this decision.

## Work

### Step 1 — Extract all open proposals

Parse `memory/lessons.md` for every "Proposed rule changes" entry across all weeks. For each proposal, record: the proposal text, the first week it appeared, and how many distinct weeks it has been flagged.

### Step 2 — Filter out already-implemented proposals

For each proposal, check whether it is already present in the current `memory/strategy.md` (or in a routine file). If implemented, move it to an "✅ Already implemented" section and do not rank or backtest it. This prevents re-recommending things you've already done.

### Step 3 — Score each remaining proposal by evidence strength

Assign each open proposal a tier:

- **STRONG** — flagged in 3+ distinct weeks, OR backed by an existing backtest with hard numbers, OR addresses a pattern that has caused a documented real-money loss (e.g. a recurring give-back, a repeated noise-stop). These get backtested in Step 4.
- **MODERATE** — flagged in exactly 1-2 weeks with sound reasoning and no contradicting evidence. Ranked and shown, but NOT auto-backtested (small-sample backtests on weak evidence produce low-confidence noise — wait for more weeks of evidence or a manual request).
- **WEAK** — speculative, thin reasoning, contradicted by other findings, or already tested and rejected. Listed briefly so nothing is silently dropped.

Record the tier and the reasoning for each in the running log.

### Step 4 — Backtest STRONG proposals only

For each STRONG proposal (that is not EXHAUSTED per Gate 3):

a. Identify the most relevant existing script in `backtesting/scripts/` (the variant-comparison engine is usually the right base). Use the cached data in `backtesting/data_cache/` if present — do not refetch if the cache covers the needed range.

b. Run the proposal as a single rule change against the current baseline, across **all three periods**: 2022-2024, 2025, and 2026 YTD. Report win rate, avg return, profit factor for baseline vs proposed, each period.

c. **Out-of-sample discipline (critical).** Treat 2022-2024 as in-sample and 2025 + 2026 as out-of-sample. A proposal only earns a "backtest supports" verdict if it improves or holds in the OUT-OF-SAMPLE periods, not just in-sample. A change that only helps 2022-2024 is in-sample overfitting — flag it as such, do not endorse it.

d. **Beat-the-benchmark bar.** A proposal that improves the strategy but still underperforms SPY buy-and-hold over the same period is not a real win — note SPY's return for context.

e. Record the full result in the running log with the date tested, so the anti-overfitting counter in Gate 3 stays accurate.

### Step 5 — Compose the ranked report

Build a report with these sections:
- **🔴 STRONG (backtested):** each proposal, weeks-flagged count, the 3-period backtest result, in-sample-vs-out-of-sample verdict, and — only if the backtest supports it out-of-sample — the exact `strategy.md` wording the human could paste. Make explicit: "human applies this; this routine does not."
- **🟡 MODERATE (ranked, not yet backtested):** proposal, weeks flagged, why it's not STRONG yet, what evidence would promote it.
- **⚪ WEAK / EXHAUSTED:** one line each.
- **✅ Already implemented:** one line each (confirms the loop is closing).

### Step 6 — Save + post

a. **Append** the full report to `backtesting/strategy_review_log.md` under a dated header (this is the running log — it accumulates, giving the routine cross-week memory). Include the anti-overfitting test counts so future runs can read them.

b. `git add -A`, commit (`strategy_review: <YYYY-MM-DD> ranked report`), push to main per `CLAUDE.md` end-of-run protocol.

c. POST the report summary to `DISCORD_WEBHOOK_URL`.

## MUST NOT

- Edit `memory/strategy.md` — recommend only; the human applies changes. This is the core guardrail that keeps the bot from drifting its own rules.
- Edit any routine file or any other live memory file except `backtesting/strategy_review_log.md`.
- Place or modify any order. This routine never touches Alpaca except the read-only reconciliation sanity check.
- Re-backtest a proposal that has already been tested and rejected twice on the same periods (Gate 3 anti-overfitting rule).
- Endorse a proposal that only improves in-sample (2022-2024) without out-of-sample (2025/2026) support.
- Backtest MODERATE or WEAK proposals — STRONG only.
- Auto-promote a proposal to "apply this" without out-of-sample backtest support.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "strategy_review: <YYYY-MM-DD> — <N> proposals ranked, <M> backtested"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. POST to Discord — HTTP POST to `DISCORD_WEBHOOK_URL`, `Content-Type: application/json`, body:

```json
{"content": "📊 STRATEGY REVIEW <YYYY-MM-DD>\n🔴 STRONG (backtested): <TICKER/rule — verdict, OOS support yes/no> ...\n🟡 MODERATE: <rule — weeks flagged> ...\n⚪ WEAK/EXHAUSTED: <count>\n✅ Already implemented this cycle: <count>\nFull report: backtesting/strategy_review_log.md\nReminder: recommendations only — human applies any strategy.md change.\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success. If the POST fails, log the failure but do NOT abort.
