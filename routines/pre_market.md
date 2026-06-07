# Pre-market routine — 07:00 ET weekdays

## Scope

Research overnight news and draft today's trade plan in `memory/plan.md`, using ONLY the tickers in `memory/universe.md` and `memory/watchlist.md`. **MUST NOT place any orders. MUST NOT re-screen the universe.**

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

1. **Load the universe.** Read the ticker table from `memory/universe.md`. These are the only tickers this routine may consider unless also on the watchlist. **Do not re-screen, do not refetch the S&P 500 list, do not recompute filters** — `universe_refresh` owns all of that.

1b. **Load the watchlist.** Read `memory/watchlist.md`. For each ticker with `status: active`, treat it identically to a universe ticker for the rest of this routine — it may be shortlisted, researched, and planned just like any universe name. All strategy.md rules still apply. Log watchlist tickers considered in `memory/research_log.md`.

1c. **PEAD signal-health posture (raise-the-bar overlay).** Read `memory/pead_health.md` frontmatter.
   - **Freshness:** if `expires_on` is in the past, or the file is missing/placeholder (`source: unset`), treat posture as **NORMAL but flagged STALE** — do NOT raise the bar on a stale overlay (the universe-cache freshness gate above is the hard halt). Note the staleness in `research_log.md` and the Discord message.
   - **If `posture: ELEVATED_BAR`** (trailing realized PEAD drift is currently weak — see `realized_health_60d_pct`, `health_sample_n`): for THIS session only, raise the EPS-surprise threshold to **>20% for ALL sectors** (overriding the standard 15% in `strategy.md` entry criteria; for sectors already at >20% it stays >20%) and cap **max new positions at 2**. This mirrors `strategy.md`'s bear-regime treatment — **do NOT halt**: high-conviction setups clearing the higher bar still trade. Record posture, `realized_health_60d_pct`, and `health_sample_n` in `plan.md` notes and the Discord message.
   - **If `posture: NORMAL`:** standard `strategy.md` thresholds apply.
   - This overlay governs new ENTRIES only — it never affects exits, and it can only TIGHTEN (never loosen) a `strategy.md` rule.
   - The SPY 200-day regime is enforced separately by `strategy.md`'s own regime-gate rule; this is the *signal-health* leg, which can raise the bar even when SPY is bullish (the bull-and-weak case). When both apply, use the stricter (lower) new-position cap.

2. **Overnight news sweep.** web_search for overnight market-moving news, earnings releases, guidance updates, and analyst actions. Focus on names already in `universe.md` and `watchlist.md`. Log salient items to `memory/research_log.md` (date, source, ticker, note). If a compelling catalyst appears for a ticker NOT in `universe.md` AND NOT in `watchlist.md`: add a new row to `memory/watchlist.md` with `status: pending_review` and POST a Discord flag — do NOT plan a trade on it until human sets status to `active`.

3. **Shortlist 3–5 candidates** from universe + active watchlist tickers with a positive fundamentals signal in the last 30 days (earnings beat, guidance raise, positive analyst revision, or clear catalyst). Apply all scoring filters below — higher-scoring candidates rank above lower-scoring ones. **Use the EPS-surprise threshold in effect for this session** — the standard `strategy.md` thresholds, OR >20% for all sectors if step 1c set `ELEVATED_BAR` (or the bear-regime rule is active).

   **Deep research protocol — run steps a through i for EVERY candidate before scoring:**

   a. **Earnings data (full article fetch):** web_search `"<TICKER> Q[N] [year] earnings results"`. Fetch the full article from the top result (prefer Seeking Alpha, MotleyFool, or company IR page over aggregators). Extract: exact EPS beat %, exact revenue beat %, guidance language verbatim, and any forward commentary from management. Do not rely on snippet alone.

   b. **Earnings call tone (full fetch):** web_search `"<TICKER> earnings call transcript summary [year]"`. Fetch the top result in full. Look for verbatim management quotes about demand, guidance, and competitive position. Record specific phrases — not just "positive" or "negative" but the actual words used. Examples of bullish language: "accelerating," "record demand," "raising again," "strong visibility," "ahead of schedule." Examples of cautious language: "monitoring closely," "uncertain environment," "cautious about second half," "headwinds."

   c. **Analyst reactions (full fetch):** web_search `"<TICKER> analyst upgrade rating [month] [year]"`. Fetch the top 2 results in full. Record which firms upgraded, their new price targets, and their specific reasoning. Note any downgrades or cautious notes from bears. A stock with 5 upgrades and 0 downgrades post-earnings scores higher than one with 2 upgrades and 1 downgrade.

   d. **52-week high recency:** web_search `"<TICKER> 52-week high"`. Also fetch Alpaca bars for the last 252 trading days (`GET /v2/stocks/{ticker}/bars?timeframe=1Day&limit=252&feed=iex`) to calculate the exact 52-week high date and price. Record how many days ago the high occurred. Stocks where 52-week high was within 45 days: top priority. 46–90 days: normal priority. Over 90 days: downrank.

   e. **Volume confirmation:** Fetch Alpaca bars for the earnings announcement date and the 20 days prior. Calculate: announcement-day volume ÷ 20-day average volume. Record the exact ratio. ≥2x: strong institutional confirmation. 1.5–2x: moderate confirmation. <1.5x: weak — downrank candidate.

   f. **Relative strength vs SPY:** Fetch Alpaca bars for both the ticker and SPY (`bars?timeframe=1Day&limit=5&feed=iex`) for the last 5 trading days since earnings. Calculate exact % return for each. Record the spread (ticker return minus SPY return). Positive spread = outperforming → proceed. Negative spread = underperforming → drop or heavily downrank.

   g. **Risk check (full fetch):** web_search `"<TICKER> risks concerns [month] [year]"`. Fetch the top result in full. Note any material risks: regulatory, competitive, supply chain, customer concentration, insider selling. If any risk could plausibly break the thesis within 42 days, drop the candidate entirely and log why.

   h. **Regulatory risk scan (required for all candidates):**

      i. **SEC shelf registration check:** web_search `"<TICKER> SEC S-3 shelf registration 2026"` AND web_search `"<TICKER> equity offering dilution 2026"`. If an active shelf registration (Form S-3) is found OR a recent equity offering announcement exists, flag as **DILUTION RISK** and drop the candidate. Record finding in plan.md notes.

      ii. **BIS export control check (IT/semiconductor candidates only):** web_search `"BIS export control <TICKER> 2026"` AND web_search `"<TICKER> China export restriction 2026"`. For any IT sector candidate — especially semiconductors (AMD, NVDA, MRVL, MU, AVGO, QCOM, etc.) — check for recent BIS rule changes, license requirement expansions, or entity list additions that affect China revenue. If material BIS news exists within the last 30 days, flag as **EXPORT CONTROL RISK** and drop or heavily downrank. Record finding in plan.md notes.

      **If either regulatory scan finds a material flag: drop the candidate regardless of score on steps a–g.**

   i. **New signal checks (research-backed additions):**

      i. **Multi-quarter earnings streak:** web_search `"<TICKER> earnings history last 3 quarters"`. Check whether the company has beaten EPS estimates for 2+ consecutive quarters — not just the most recent one. Research shows Sharpe ratios nearly double for stocks with multi-quarter streaks vs first-time beats. Score adjustment:
         - First-time beat only: signal quality score −1 pt
         - 2 consecutive quarters beating: no adjustment (baseline)
         - 3+ consecutive quarters beating: signal quality score +1 pt
         Record the streak count in the thesis.

      ii. **Earnings day gap size:** Check the stock's price change from prior close to earnings-day open (the overnight gap). A large positive gap shows institutional conviction in real time. Score adjustment:
         - Gap >10% upward: confirmation score +1 pt (strong institutional buy)
         - Gap 5–10% upward: no adjustment (normal)
         - Gap <5% despite large EPS beat: confirmation score −1 pt (muted reaction, weak drift signal)
         Use Alpaca bars or web_search `"<TICKER> earnings reaction gap [date]"` to verify.

      iii. **Sector ETF momentum:** Identify the candidate's GICS sector ETF (XLK=IT, XLI=Industrials, XLF=Financials, XLV=Healthcare, XLY=Consumer Disc., XLE=Energy, XLP=Consumer Staples, XLU=Utilities, XLRE=Real Estate, XLB=Materials). Fetch Alpaca bars for the sector ETF over the last 20 trading days. If the sector ETF is underperforming SPY over that window: momentum score −1 pt. PEAD is weakest when money is rotating OUT of a sector. Record sector ETF vs SPY 20-day spread in thesis.

      iv. **Short interest amplifier (optional but noted):** web_search `"<TICKER> short interest percent float"`. If short interest >10% of float before earnings and the stock had a large beat: flag as potential short squeeze amplifier — confirmation score +0.5 pt. If short interest <2%: neutral. Record in thesis.

      v. **Insider activity:** web_search `"<TICKER> insider buying Form 4 [month] [year]"`. If C-suite or directors purchased shares within 30 days post-earnings: signal quality score +0.5 pt (management conviction). If insiders are selling aggressively post-earnings: risk score −1 pt. Record in thesis.

   **After completing a–i, score each candidate 1–10:**
   - Signal quality (EPS surprise size, guidance raise magnitude, earnings streak, insider activity): 1–3 pts
   - Momentum (52-week recency, relative strength vs SPY, sector ETF momentum): 1–3 pts
   - Confirmation (volume ratio, analyst conviction count, earnings day gap): 1–2 pts
   - Risk (lower risk = higher score, regulatory flags = automatic drop): 1–2 pts

   **Only proceed with candidates scoring ≥6/10.** If fewer than 3 candidates score ≥6, plan fewer buys rather than lowering the bar.

4. **Earnings re-verification (shortlist only).** For each shortlisted candidate, web_search the next earnings date to confirm it is NOT within 3 days. The cached `earnings_date_next` in `universe.md` may be up to 7 days stale. Drop any candidate inside the 3-day window. Record the reason.

4b. **Halt / trading-status check (shortlist only).** For each surviving candidate, web_search `"<TICKER> stock halt"` AND fetch Alpaca `GET /v2/assets/<TICKER>`. Drop if `tradable` is false, `status` is not `active`, or recent halt news is present. Record the reason in `research_log.md`.

5. **Draft `memory/plan.md`** for each surviving candidate:
   - Planned buy: ticker, `target_qty` sized per `strategy.md` `Max position size at entry` field (currently **11%**) of current equity (from Alpaca `/v2/account`), `limit_price`, `stop_price` = `entry × 0.92`.
   - Full thesis must include: score X/10, EPS surprise %, revenue beat %, earnings streak (N quarters), earnings day gap %, volume ratio vs 20-day avg, 52-week high recency (days ago), relative strength vs SPY (5-day spread %), sector ETF vs SPY (20-day spread %), analyst upgrade count, short interest %, insider activity, one verbatim management quote from earnings call, top risk flagged, regulatory scan result (shelf reg: clean/flagged, BIS: clean/flagged/N/A).
   - Planned sells: any positions whose exit criteria (per `strategy.md`) have fired since `market_close` — e.g. thesis invalidation, 60-day-with-<3%-gain rotation flag from midday.

6. **Sanity-check the plan** against `strategy.md`: cash floor ≥ 10%, max concurrent ≤ 8, max new-per-week ≤ 5 — **but ≤ 2 if step 1c posture is `ELEVATED_BAR` or the bear-regime rule is active** (count recent buys in `trade_log.md`), sector cap ≤ 30% (use the `sector` column in `universe.md`). Trim if needed, log the reasons in the `plan.md` notes section.

## MUST NOT

- Call Alpaca `/v2/orders`.
- Consider tickers not in `memory/universe.md` OR `memory/watchlist.md`. If a compelling catalyst appears for a ticker outside both lists, add it to `watchlist.md` with `status: pending_review` and POST a Discord flag — do not plan a trade until human sets status to `active`.
- Re-run any universe filters. That's `universe_refresh`'s job.
- Leave `plan.md` blank if you had candidates — if nothing qualified, write that reason explicitly under Notes.
- Score a candidate ≥6 without completing all of steps a–i. Incomplete research = automatic disqualification.
- Proceed with any candidate flagged by the regulatory scan in step h.
- Ignore an `ELEVATED_BAR` posture from step 1c: when set (and not stale), the >20%-all-sectors EPS bar and ≤2 new-position cap are mandatory for the session. The overlay may only tighten, never loosen.

## End-of-run protocol (per `CLAUDE.md`)

1. `git pull --rebase origin main`
2. `git add -A`
3. `git commit -m "pre_market: <YYYY-MM-DD> — planned <TICKERS or 'no trades'>"`
4. `git push origin main` (retry once on rebase conflict, then abort)
5. POST to Discord — HTTP POST to `DISCORD_WEBHOOK_URL`, `Content-Type: application/json`, body:

```json
{"content": "🌅 PRE-MARKET <YYYY-MM-DD> (DRY_RUN: <true|false>)\nUniverse: <N> tickers (expires <YYYY-MM-DD>)\nPEAD health: <NORMAL|ELEVATED_BAR|STALE> (realized <pct>% n=<N>) — <standard 15% bar | raised to 20% all sectors, max 2 new>\nPlanned buys: <TICKER qty @ limit, stop | score X/10 | EPS +X% | streak Nq | gap +X% | vol Xx | RS +X% vs SPY | sector ETF +X% vs SPY | shelf-reg: clean | BIS: clean> ...\nPlanned sells: <TICKER — reason> ...\nTop catalyst: <one line>\nRegulatory flags: <TICKER — shelf-reg/BIS flag description> or none\nWatchlist flags: <TICKER added as pending_review — reason> or none\nCommit: https://github.com/minhroi8/trading-routine/commit/<sha>"}
```

A 204 response means success. If the POST fails, log the failure but do NOT abort.
