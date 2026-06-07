# Universe refresh routine — Sundays 18:00 ET

Cron: `0 18 * * 0` (US Eastern). UTC equivalent during EDT: `0 22 * * 0`. During EST: `0 23 * * 0`.

## Scope

Rebuild `memory/universe.md`: the pre-computed list of tickers that pass `strategy.md` universe filters. **This is the ONLY routine that writes to `memory/universe.md`** — every trading routine reads it as read-only.

This routine ALSO refreshes `memory/pead_health.md`: the weekly PEAD signal-health overlay that `pre_market` reads to decide whether to raise the entry bar. **This is the ONLY routine that writes to `memory/pead_health.md`**, and only via `compute_pead_health.py` (never by hand).

Read `CLAUDE.md` and `memory/strategy.md` first — they supersede anything below.

## Load

1. `CLAUDE.md`
2. `memory/strategy.md` (for the filter thresholds)
3. `memory/universe.md` (the existing cache — used only to diff against the new one for the Discord message; never kept on failure)

## Gates

- **No market-clock check.** Market is closed on Sunday evening by design.
- **No position reconciliation.** This routine never touches positions or orders.
- **Failure mode:** if the run cannot complete a full rebuild, **do not overwrite `memory/universe.md` with a partial file**. POST an error to `DISCORD_WEBHOOK_URL` so the human sees it before Monday pre-market, then exit non-zero. A stale-but-complete cache is safer than a half-written one.

## Work

1. **Pull the S&P 1500 list (combined: S&P 500 large-cap + S&P 400 mid-cap + S&P 600 small-cap).** Fetch all three indexes and combine into one ticker list. Sources in priority order for each index:

   **S&P 500 (large-cap, ~500 tickers):**
   - Primary: Wikipedia — `https://en.wikipedia.org/wiki/List_of_S%26P_500_companies`
   - Fallback 1: SlickCharts — `https://www.slickcharts.com/sp500`
   - Fallback 2: GitHub dataset — `https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv`

   **S&P 400 (mid-cap, ~400 tickers):**
   - Primary: Wikipedia — `https://en.wikipedia.org/wiki/List_of_S%26P_400_companies`
   - Fallback: SlickCharts — `https://www.slickcharts.com/indices/sp-400`

   **S&P 600 (small-cap, ~600 tickers):**
   - Primary: Wikipedia — `https://en.wikipedia.org/wiki/List_of_S%26P_600_companies`
   - Fallback: SlickCharts — `https://www.slickcharts.com/indices/sp-600`

   Combine all three into a single deduplicated ticker list. Tag each ticker with its source index (large/mid/small) for the universe.md output. Log the source URLs and timestamps to `memory/research_log.md`.

   **If any index fails entirely (all fallbacks blocked):** abort the run, keep the existing universe.md, and POST a failure message to Discord. Do not produce a partial S&P 500-only universe under the new spec — that would silently regress the change.

2. **Fetch daily bars in batches** from Alpaca `/v2/stocks/bars` with `timeframe=1Day` and a start/end covering the last ~40 calendar days. Batch up to 100 symbols per request. Respect rate limits (~0.4s between batches). Use `feed=iex` (paper account default). Note: with ~1,500 symbols, this means ~15 batches and ~6-10 minutes of fetch time. Plan accordingly.

3. **Compute per-ticker metrics.**
   - `last_price` = most recent daily close
   - `avg_dollar_volume_20d` = mean of `close × volume` across the last 20 trading days

4. **Apply universe filters from `strategy.md`.** Exclude a ticker if any of:
   - `last_price < 10`
   - `avg_dollar_volume_20d < 20_000_000` (this filter does the heavy lifting at S&P 1500 scale — most S&P 600 small-caps will be rejected by ADV)
   - "Date first added" to its index is < 180 days ago AND the ticker is a genuinely recent IPO
   - US primary listing is unclear (the S&P indexes are US-primary by construction; this is a safety net)
   - Missing bar data (fewer than 20 trading days returned) — treat as reject and record the reason
   Record rejection reasons so the Discord message can show the top 3–5 reasons.

5. **Earnings lookup for passing tickers.** OPTIONAL at this layer. `pre_market` re-verifies earnings for every candidate. Record `unknown` and move on if lookup fails.

6. **Halt / SEC check.** Optional at this layer. Trading routines web_search halts on their candidate shortlist instead.

7. **Write `memory/universe.md`** atomically with frontmatter:
```yaml
   ---
   screened_on: <YYYY-MM-DD of today>
   expires_on: <YYYY-MM-DD, today + 7 days>
   total_passed: <N>
   total_rejected: <M>
   universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
   source_500: <primary source URL used>
   source_400: <primary source URL used>
   source_600: <primary source URL used>
   ---
```

   Include a `cap_tier` column in the table (`large` / `mid` / `small`) so trading routines can apply tier-aware logic if needed in the future. Sort by ticker symbol.

   **Important:** Use `datetime.date.today()` for `screened_on` — never hardcode the date.

8. **Refresh the PEAD signal-health overlay.** Run `python compute_pead_health.py` (needs `yfinance`, `pandas`, `numpy` — install if missing). It computes the trailing-60d realized PEAD health across the S&P 500 plus the SPY 200-day regime, and writes `memory/pead_health.md` atomically with `posture: NORMAL|ELEVATED_BAR` in its frontmatter (ELEVATED_BAR = the drift edge is currently weak → `pre_market` raises the entry bar).
   - This step is **independent of the universe rebuild**: if `compute_pead_health.py` exits non-zero, log the error to `memory/research_log.md`, note it in the Discord message, and continue — do NOT fail the run or roll back a good `universe.md`. A stale `pead_health.md` is safe: `pre_market` fails OPEN (treats posture as NORMAL) on a stale overlay, and the universe-cache `expires_on` remains the hard gate.
   - Note: this script uses **yfinance** (for EPS-surprise history), not the Alpaca bars used above — that's intentional; the health signal was calibrated on yfinance data.
   - Do not hand-edit `memory/pead_health.md`; only the script writes it.

## MUST NOT

- Place, modify, or cancel orders.
- Write to any file other than `memory/universe.md`, `memory/pead_health.md`, and `memory/research_log.md`. (`pead_health.md` must be written by `compute_pead_health.py`, not by hand.)
- Leave a partially written `memory/universe.md` on disk if the run fails.
- Re-screen or refresh the universe from any other routine.
- Hardcode the current date anywhere in the script. Always derive from `datetime.date.today()`.
- Produce a partial universe (e.g., S&P 500 only) if S&P 400 or S&P 600 fetches fail. Either fully succeed or abort and keep the existing cache.

## End-of-run protocol (per `CLAUDE.md`)

Per the standard `CLAUDE.md` end-of-run protocol — `git pull --rebase`, commit directly to main, push, and POST to Discord with User-Agent header.

Discord body:

```json
{"content": "🔄 UNIVERSE REFRESH <YYYY-MM-DD>\nScope: S&P 1500\nPassed: <N> | Rejected: <M> | Errors: <E>\nBy tier: large=<X>, mid=<Y>, small=<Z>\nTop rejection reasons: price<10: A | ADV<20M: B | IPO<180d: C | no_bars: D\nExpires: <YYYY-MM-DD>\nPEAD health: <NORMAL|ELEVATED_BAR> (realized <pct>% n=<N> | SPY>200MA: <bool> | <ok|stale/failed>)\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success.
