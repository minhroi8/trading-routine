# Universe refresh routine — Sundays 18:00 ET

Cron: `0 18 * * 0` (US Eastern).

## Scope

Rebuild `memory/universe.md`: the pre-computed list of tickers that pass `strategy.md` universe filters. **This is the ONLY routine that writes to `memory/universe.md`** — every trading routine reads it as read-only.

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

1. `CLAUDE.md`
2. `memory/strategy.md` (for the filter thresholds)
3. `memory/universe.md` (the existing cache — used only to diff against the new one for the Slack summary; never kept on failure)

## Gates

- **No market-clock check.** Market is closed on Sunday evening by design.
- **No position reconciliation.** This routine never touches positions or orders.
- **Failure mode:** if the run cannot complete a full rebuild, **do not overwrite `memory/universe.md` with a partial file**. Fail loudly to Slack so the human sees it before Monday pre-market, then exit non-zero. A stale-but-complete cache is safer than a half-written one (pre-market will catch the stale cache on Monday via `expires_on`).

## Work

1. **Pull the S&P 500 list.** Primary source: Wikipedia — `https://en.wikipedia.org/wiki/List_of_S%26P_500_companies`. It gives ticker, company name, GICS sector, and "date first added" in one table. Fallback: SlickCharts — `https://www.slickcharts.com/sp500`. Log the source URL and timestamp to `memory/research_log.md`.

2. **Fetch daily bars in batches** from Alpaca `/v2/stocks/bars` with `timeframe=1Day` and a start/end covering the last ~30 calendar days (to guarantee 20 trading days). Batch up to 100 symbols per request (Alpaca's multi-symbol bars API). Respect rate limits; parallelize carefully.

3. **Compute per-ticker metrics.**
   - `last_price` = most recent daily close
   - `avg_dollar_volume_20d` = mean of `close × volume` across the last 20 trading days

4. **Apply universe filters from `strategy.md`.** Exclude a ticker if any of:
   - `last_price < 10`
   - `avg_dollar_volume_20d < 20_000_000`
   - "Date first added" to S&P 500 is < 180 days ago AND the ticker is a genuinely recent IPO (date added is an imperfect proxy — if unsure, web_search the actual listing date)
   - US primary listing is unclear (Wikipedia's list is US-primary by construction; this is a safety net for edge cases)
   - Missing bar data (fewer than 20 trading days returned) — treat as reject and record the reason
   Record rejection reasons so the Slack summary can show the top 3–5 reasons.

5. **Earnings lookup for passing tickers.** web_search each pass-filter ticker's next scheduled earnings date. Preferred sources: the company's Investor Relations page, Nasdaq, or Zacks earnings calendars. Record as ISO date (`YYYY-MM-DD`); if the lookup fails or is ambiguous, record `unknown` and move on — do not abort the run for a single missing earnings date.

6. **Halt / SEC check.** Optional at this layer. Regular-hours halts are intraday and unreliable to check on a Sunday evening; the trading routines web_search for halts on their candidate shortlist (small N) instead of here (500 tickers). If you do find a publicly known active SEC investigation against a ticker during the S&P 500 pull, exclude it and note the reason.

7. **Write `memory/universe.md`** atomically (write to a temp path, then rename) with frontmatter:
   ```yaml
   ---
   screened_on: <YYYY-MM-DD of today>
   expires_on: <YYYY-MM-DD, today + 7 days>
   total_passed: <N>
   total_rejected: <M>
   source: <primary source URL used>
   ---
   ```
   Then the documentation block (copy from the template) and the table of passing tickers, one row per ticker, sorted by ticker symbol.

## MUST NOT

- Place, modify, or cancel orders.
- Write to any file other than `memory/universe.md` and `memory/research_log.md`.
- Leave a partially written `memory/universe.md` on disk if the run fails — keep the last good cache in place and fail to Slack.
- Re-screen or refresh the universe from any other routine. That is this routine's exclusive job.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "universe_refresh: <YYYY-MM-DD> — <N> tickers passed filters"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. Slack `#trading-bot`:

```
🔄 UNIVERSE REFRESH <YYYY-MM-DD>
Passed: <N> | Rejected: <M> | Errors: <E>
Top rejection reasons: <price<10: X | ADV<20M: Y | IPO<180d: Z | no bars: W>
Expires: <YYYY-MM-DD>
Commit: https://github.com/minhroi8/trading-routine/commit/<sha>
```
