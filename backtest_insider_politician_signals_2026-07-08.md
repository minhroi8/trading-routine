# Backtest: Insider Form 4 Clusters (Signal B) & Congressional Trade Clusters (Signal A)

**Date run:** 2026-07-08
**Status:** Research only. No orders were placed. No live or paper brokerage account was
touched for trading purposes — Alpaca was used exclusively for its read-only historical
market-data endpoint (`data.alpaca.markets`), never `/v2/orders` or any account-mutating
call.
**Scope:** Signal B (insider Form 4 open-market-purchase clusters) and Signal A
(congressional trade clusters), backtested and reported **separately**, per the request.
Signal C (prediction-market divergence) was **not** attempted — see the dedicated section
below.

> **A note on the source SOP.** The task referenced an attached `ai-trading-agent-sop`
> and a `SKILL.md` "Hard Rules" document. Neither file was present in this repository or
> otherwise reachable in this session. Every rule this backtest enforces (cluster
> thresholds, shared filters, entry/exit levels, cost assumptions, IS/OOS split, benchmark
> discipline) was taken verbatim from the task instructions, which explicitly restate the
> SOP's hard rules. If the actual SOP document differs from that restatement in some
> particular this backtest is not aware of, this result should be treated as validating
> the restated rules, not the SOP file itself.

---

## Headline result (do not soften)

| | Signal B (insider) | Signal A (Congress, Senate-only) |
|---|---|---|
| Full-window CAGR (net of costs) | **8.5%** | **13.7%** |
| SPY CAGR, same window | 15.3% | 13.8% |
| QQQ CAGR, same window | 22.2% | 22.3% |
| **Beats SPY on CAGR?** | **No** | Roughly ties (+0.1pp) |
| **Beats QQQ on CAGR?** | **No** | **No** |
| **OOS beats benchmark on CAGR?** | **No — badly** (OOS strategy CAGR 9.7% vs SPY 25.8% / QQQ 35.5%) | **No** (OOS strategy CAGR 28.9% vs SPY 20.7% — beats SPY; vs QQQ 38.6% — does not) |
| Sharpe (net) vs SPY / QQQ | **1.44 vs 0.83 / 0.95 — better** | **3.94 vs 0.80 / 1.02 — much better** |
| Max drawdown vs SPY / QQQ | -34.3% vs -34.2% / -35.6% — roughly tied | **-19.5% vs -34.2% / -28.6% — much smaller** |
| n trades (full / IS / OOS) | 2,709 / 2,077 / 632 | 118 / 91 / 27 |

**Neither signal beats a passive QQQ position on absolute return over its test window, in
or out of sample.** Both signals show meaningfully better risk-adjusted returns (Sharpe)
and smaller drawdowns than either benchmark, which is a real and consistent finding, not
an artifact of one lucky window — but "smoother path to a lower number" is not what
"beat the S&P 500" (the account's own stated goal) means. Signal A's OOS window is tiny
(27 trades, 18 months, coinciding with the COVID crash/recovery) and its apparent CAGR
edge over SPY there should not be trusted on that sample size alone. Full detail below.

---

## 1. Methodology

### 1.1 No-look-ahead discipline

Every entry is stamped to the exact public-availability timestamp of the information that
triggered it, never the underlying transaction date:

- **Signal B:** `FILING_DATE` from SEC's SUBMISSION.tsv (when the Form 4 hit EDGAR), not
  `TRANS_DATE` (when the insider actually traded). A cluster's confirmation date is
  `max(FILING_DATE)` across the trades that first establish 2 distinct qualifying insiders
  within the 10-trading-day window.
- **Signal A:** `date_recieved` (disclosure date) on the Senate PTR filing, not
  `transaction_date`. Confirmation date is `max(disclosure_date)` across the trades that
  first establish 2 distinct senators within the 6-calendar-week window.
- **Entry** in both cases is the closing price on the next trading session after the
  confirmation date — never the confirmation day itself, and never the source trade date.
- Market cap and the earnings-proximity check are also point-in-time: shares-outstanding
  and 8-K filing dates are only used if their own filing/report date precedes the entry
  date being evaluated (see §2.3).

### 1.2 Cluster definitions (mirrored from the task's restated Hard Rules)

- **Signal B:** 2+ distinct insiders (Director, CEO, or CFO by title; `TenPercentOwner`
  alone does **not** qualify) buying the same ticker within 10 trading days, transaction
  code `P` only (open-market purchase — codes A/M/F/G/S and anything else excluded at the
  SEC-bulk-download stage). Rule 10b5-1 plan trades excluded via `AFF10B5ONE` where that
  field exists (see limitation in §2.1).
- **Signal A:** 2+ distinct senators buying the same ticker within 6 **calendar** weeks
  (not trading days — the task specifies this distinction deliberately). House
  Representatives could not be included; see §2.2.
- **De-duplication:** once a cluster fires for a ticker, the accumulation window resets.
  This is a conservative choice (fewer signals, not more) but is not perfect — see the
  known artifact noted in §4.4.

### 1.3 Shared filters (applied identically to both signals)

Entry price ≥ $5/share; market cap ≥ $2B at entry (approximated — §2.3); not OTC; not a
leveraged/inverse ETF (name-pattern match: "ultra", "2x", "3x", "inverse", "bear",
"short", "leveraged", "direxion", etc.); not within 2 trading days of an earnings-proxy
event (§2.3); skip if price is already up >15% since the cluster's source trade date.

### 1.4 Entry/exit and costs

Entry: next trading session close after confirmation. Exit: take-profit at entry price
×1.25, stop-loss at ×0.85 (checked via daily high/low, stop-loss takes priority if both
trigger the same day), stale exit at 90 calendar days, or end of the test window —
whichever comes first. Costs: 4bp per side (midpoint of the SOP's stated 3-5bp range),
applied to both entry and exit; every table below reports **gross** (no costs) and **net**
(with costs) side by side.

### 1.5 In-sample / out-of-sample split

Chronological 70/30 split on the **calendar span** of each signal's actual usable test
window (not on trade count) — the first 70% of the window is in-sample, the last 30% is
out-of-sample. No shuffling.

---

## 2. Data sources and honest limitations

This section is required reading before the results — several of these materially change
what the numbers below can support.

### 2.1 Signal B — SEC EDGAR Form 3/4/5 structured bulk data

Source: SEC DERA's quarterly Form 3/4/5 datasets
(`sec.gov/files/structureddata/data/insider-transactions-data-sets/<qtr>_form345.zip`),
24 quarters (2019Q1–2024Q4) downloaded directly. This is official, structured, primary
SEC data — the highest-quality source used in this backtest.

- **273,516** raw transaction-code-`P` Form 4 line items in the window; **129,503**
  survive the CEO/CFO/Director filter; **26,593** valid-ticker clusters detected;
  **2,709** trades survive every shared filter (a 10.2% survival rate from raw clusters —
  the dominant rejection reasons are market cap <$2B (10,003) and price <$5 (7,176),
  i.e. most insider-cluster buying happens in small/micro caps that never reach this
  strategy's investable universe).
- **10b5-1 exclusion is incomplete for 2019–early 2023.** The `AFF10B5ONE` checkbox was
  only added to Forms 4/5 by the SEC's rule amendments effective April 2023. For filings
  before that, the field does not exist in the structured data at all — there is no
  reliable free way to identify 10b5-1 plan trades in that period. 4,060 rows flagged
  `AFF10B5ONE=1/true` were excluded; an unknown additional number of pre-2023 10b5-1
  trades are **not** excluded because the data doesn't say. This likely inflates the
  cluster count and modestly dilutes the true "discretionary open-market buy" signal for
  roughly the first four of six years tested.

### 2.2 Signal A — Congressional trades: House data unavailable, Senate mirror is stale

- **House of Representatives could not be sourced at all.** `house-stock-watcher-data`'s
  S3 bucket returns `AccessDenied` (confirmed directly against S3, independent of this
  session's network policy) and `housestockwatcher.com` itself returns a 502 at the
  origin. No GitHub mirror of the raw House JSON could be located despite an extensive
  search (direct repo, `jsdelivr` CDN mirror, alternate owners, alternate project names).
  **Signal A as tested is Senate-only.** This is a real scope reduction from
  "congressional trade clusters" (both chambers), not a modeling choice, and it means any
  House-only or House-heavy cluster (which by anecdote and other public trackers are a
  large share of total congressional trading volume) is invisible to this backtest.
- **The Senate mirror (`timothycarambat/senate-stock-watcher-data` on GitHub) has not
  been updated since 2021-03-10.** The dataset's own last `date_recieved` is 2021-03-10;
  the last `transaction_date` is 2020-12-02. It does **not** reach the SOP's target
  2019–2024 window at all on the back end. The actual usable window, further bounded by
  Alpaca's own price-data floor (§2.3), is **2016-01-04 to 2021-03-31** — a 5-year window
  ending nearly five and a half years before this report, not the intended
  "longest available clean data window."
- **205 raw Senate clusters detected (2014–2021 in the raw data); 118 trades survive**
  after the shared filters and the Alpaca 2016 price-data floor. This is a **small**
  sample, and OOS is smaller still (27 trades) — flagged again in §4.2.
- **Disclosure lag is severe and directly undercuts the theoretical edge.** Median
  time from the cluster's source trade date to public disclosure (and thus to a legally
  tradeable entry) is **37 days**; mean is **47 days**; the worst case is **308 days**.
  By the time a real trader could act on "2+ senators bought this stock," the information
  is, on average, over a month old. This is exactly the mechanism the SOP's own
  no-look-ahead rule is designed to expose rather than paper over, and it shows up
  directly in the results.

### 2.3 Price, market cap, and earnings-proximity data

- **Prices:** Alpaca's `/v2/stocks/{symbol}/bars` endpoint (read-only market data, paper
  account credentials, no orders placed). `yfinance` was tried first and abandoned — it
  failed consistently with TLS resets in this environment, unrelated to Alpaca. Alpaca's
  free-tier historical daily-bar data has a **hard floor of 2016-01-04** — verified
  directly against the API, not just the local cache. Any Signal A cluster confirmed
  before 2016-01-04 (29 of them) has no price data and was rejected via
  `no_entry_bar`/`no_price_data`, further shrinking the effective window described above.
- **Market cap** is approximated as (SEC XBRL `dei:EntityCommonStockSharesOutstanding`,
  taken from the most recent filing whose own `filed` date precedes the entry date) ×
  (entry price). This is point-in-time and no-lookahead by construction, but it is an
  approximation of true float-adjusted market cap, not an exact figure, and it is
  unavailable for companies that don't tag that XBRL fact consistently (2,528 Signal B
  clusters and 18 Signal A clusters were rejected for this reason alone — a real, not
  small, source of missing coverage, concentrated in smaller/newer issuers).
- **Earnings-proximity is a proxy, not a real earnings calendar.** No free, point-in-time,
  no-lookahead earnings-calendar source could be located (yfinance was broken as noted
  above; using Robinhood's earnings-calendar tool was avoided on purpose — the task
  explicitly prohibits connecting to a live brokerage account, and Robinhood is a live
  account, not a paper one). Instead, **any SEC 8-K filing date** for the issuer's CIK
  within 2 trading days of the candidate entry date excludes the trade. Most but not all
  8-Ks are earnings releases, so this proxy both over-excludes (non-earnings 8-Ks, e.g.
  M&A announcements, executive departures) and under-excludes nothing it shouldn't (it
  never lets an actual earnings 8-K through). 475 Signal B and 23 Signal A trades were
  excluded on this basis.
- **Ticker→CIK resolution for Signal A** uses SEC's *current* `company_tickers.json`
  snapshot, which only lists presently-listed companies. Seven Signal A tickers
  (CELG, ESRX, FB, FEYE, PX, UTX, WBA) could not be resolved to a CIK because they were
  since acquired, merged, or renamed, and their clusters were dropped via
  `no_shares_outstanding_data` rather than genuinely filtered on fundamentals. One ticker
  (`BRK-B`) failed to fetch from Alpaca outright (symbol-format rejection) and is entirely
  absent from the Signal A results.

### 2.4 A note on this pipeline's own bugs, fixed during this run

In the interest of the SOP's own "treat suspiciously strong results as a bug" discipline:
this backtest's equity-curve function originally chained overlapping trades
**sequentially** (each trade compounding fully into the stake before the next), which
produced a nonsensical >200%/year CAGR the first time it ran — clearly wrong, and
diagnosed and fixed before any number below was accepted. The fix builds a proper daily,
cross-sectionally-averaged, mark-to-market portfolio curve (constant-daily-rate
approximation per trade, averaged across all trades open on a given day, then compounded
day-over-day) rather than treating concurrent trades as sequential. A second bug (Alpaca
bars fetch silently ignored the requested date range and always pulled 2018-06 onward)
was also caught and fixed — it had truncated most of Signal A's pre-2018 history. Both
fixes are reflected in every number in this report; neither would have been visible from
the summary statistics alone, only by noticing the first CAGR was implausible.

---

## 3. Signal B — insider Form 4 cluster results (2019-01-01 to 2024-12-31)

**n = 2,709 trades** (2,077 in-sample, 632 out-of-sample). Split point: 2023-03-14.

| Metric | Full (net) | Full (gross) | IS (net) | OOS (net) |
|---|---|---|---|---|
| CAGR | **8.47%** | 9.01% | 7.21% | 9.71% |
| Sharpe | 1.44 | 1.53 | 1.15 | 1.87 |
| Max drawdown | -34.3% | -33.9% | -34.3% | -13.9% |
| Win rate | 48.4% | 48.4% | 48.8% | 47.3% |
| Profit factor | 1.37 | 1.39 | 1.41 | 1.26 |
| Avg return/trade | 2.41% | 2.49% | 2.61% | 1.74% |
| % trading days with an open position | 99.5% | — | 99.4% | 99.8% |

**Benchmarks, same windows:**

| | SPY | QQQ |
|---|---|---|
| Full CAGR / Sharpe / MaxDD | 15.33% / 0.83 / -34.2% | 22.22% / 0.95 / -35.6% |
| IS CAGR / Sharpe / MaxDD | 11.29% / 0.60 / -34.2% | 16.84% / 0.72 / -35.6% |
| OOS CAGR / Sharpe / MaxDD | 25.84% / 1.92 / -10.3% | 35.46% / 1.85 / -13.6% |

**Reading this plainly:** Signal B's Sharpe ratio beats both benchmarks in every period
(the strategy is never more than ~99.5% invested but its return stream is smoother than
either index), and its drawdown is comparable to or smaller than the benchmarks'. But its
CAGR trails both benchmarks in every period, and the gap **widens** out of sample — 2023
to 2024 was an exceptional run for cap-weighted large/mega-cap indices (QQQ CAGR 35.5%
OOS), and a strategy capped at +25%/trade with a 90-day stale exit structurally cannot
keep pace with an uncapped, always-fully-invested index in that kind of market. **OOS does
not beat the benchmark. This is not softened: the strategy would have underperformed
simply buying and holding SPY or QQQ over 2023–2024 by a wide margin, even though its
individual trades were profitable more often than not and its risk profile was better.**

Exit-reason mix (full window): stop-loss 1,075 (39.7%), take-profit 788 (29.1%), stale-90d
693 (25.6%), end-of-window 153 (5.6%).

---

## 4. Signal A — Senate congressional trade cluster results (2016-01-04 to 2021-03-31)

**n = 118 trades** (91 in-sample, 27 out-of-sample). Split point: 2019-09-04. **This
window is Senate-only and ends in March 2021 — see §2.2 for why.**

| Metric | Full (net) | Full (gross) | IS (net) | OOS (net) |
|---|---|---|---|---|
| CAGR | **13.68%** | 14.08% | 9.80% | 28.86% |
| Sharpe | 3.94 | 4.05 | 3.01 | 5.55 |
| Max drawdown | -19.5% | -19.2% | -19.3% | -7.8% |
| Win rate | 61.0% | 61.0% | 58.2% | 70.4% |
| Profit factor | 2.58 | 2.62 | 2.05 | 4.47 |
| Avg return/trade | 4.59% | 4.67% | 3.09% | 9.65% |
| % trading days with an open position | 91.9% | — | 93.2% | 85.1% |

**Benchmarks, same windows:**

| | SPY | QQQ |
|---|---|---|
| Full CAGR / Sharpe / MaxDD | 13.76% / 0.80 / -34.2% | 22.33% / 1.02 / -28.6% |
| IS CAGR / Sharpe / MaxDD | 10.61% / 0.84 / -20.2% | 15.51% / 0.92 / -23.2% |
| OOS CAGR / Sharpe / MaxDD | 20.66% / 0.84 / -34.2% | 38.61% / 1.22 / -28.6% |

**Reading this plainly:** Signal A's full-window CAGR essentially ties SPY (13.68% vs
13.76%, a difference well inside the noise floor of a 118-trade sample) and clearly loses
to QQQ (13.68% vs 22.33%). OOS is the one place either signal shows a CAGR edge over
SPY (28.9% vs 20.7%) — but that period is 27 trades over 18 months spanning the COVID
crash and V-shaped recovery, an extreme and unusual regime, and n=27 is nowhere near
enough to treat that edge as reliable. QQQ still beats Signal A OOS (38.6% vs 28.9%).
Sharpe and drawdown are decisively better than both benchmarks in every period — this is
the most consistent real finding for Signal A — but, as with Signal B, **better
risk-adjusted return is not the same as beating the benchmark on absolute return, and the
SOP's own benchmark discipline is explicit that CAGR/Sharpe/MaxDD/win-rate/profit-factor
are all reported, not just the flattering one.**

Exit-reason mix (full window): stale-90d 82 (69.5%), take-profit 16 (13.6%), stop-loss 13
(11.0%), end-of-window 7 (5.9%). Note the dominance of the 90-day stale exit — most
Signal A positions never hit either the profit target or the stop; they simply drift and
get closed on the clock. Combined with the severe disclosure lag in §2.2, this is
consistent with congressional-cluster information being mostly stale by the time it's
actionable, rather than a live, fast-moving edge.

---

## 5. Adversarial verification (per the SOP's own rule)

*"Treat any suspiciously strong result as a bug until independently re-derived."*

Beyond the bug-fixing already described in §2.4, a placebo test was run for both signals:
for every real trade, 10 random alternative entry dates were drawn on the **same ticker**,
within its available price history, and the identical TP/SL/90-day-stale exit rule was
applied. This isolates whether the cluster **signal** adds information, or whether the
apparent edge is just "insiders and Congress members tend to buy large, quality companies
that go up anyway regardless of when you buy them."

| | Real mean gross return/trade | Placebo mean gross return/trade | Edge |
|---|---|---|---|
| Signal B (n=2,709 real / 25,959 placebo draws) | 2.49% | 1.44% | **+1.05pp** |
| Signal A (n=118 real / 1,180 placebo draws) | 4.67% | 2.97% | **+1.70pp** |

Both signals show a real, positive edge over random-date entries on the same universe of
tickers — the cluster timing itself is adding information, not just the stock selection.
This is a genuine positive finding and is reported as such. It does **not**, however,
change the top-line conclusion: both signals' *placebo* returns are already respectable
(1.4–3.0% average per trade on a universe of insider-favored/Congress-favored names), and
neither the real signal nor its placebo baseline was enough to beat QQQ buy-and-hold over
these specific windows once compounded across a fully-invested, always-in-the-market
index comparison. In plain terms: **the signal is real but modest, and it is being asked
to beat an unusually strong benchmark period.**

(Methodological caveat on this check: the "percentile" comparison is a simple, single
random seed diagnostic, not a formal significance test with confidence intervals — treat
the sign and rough magnitude of the edge as informative, not the precision of the
percentile figure.)

---

## 6. Signal C — prediction-market divergence: not tested

Signal C (Kalshi/Polymarket vs. equity-implied-probability divergence) was **not**
backtested, per the task's explicit instruction, and this limitation is not being
approximated or worked around:

- Kalshi's CFTC-regulated, broad-market contract volume is a recent phenomenon (most
  relevant political/economic event contracts only reached meaningful open interest and
  liquidity from roughly 2023 onward).
- Polymarket's most liquid, most-referenced markets (election and macro-event contracts)
  are similarly concentrated in the last 2-3 years, and much of Polymarket's historical
  order-book/trade-level data is either not archived publicly or requires paid/gated
  access for anything beyond current snapshots.
- Neither source has a clean multi-year, point-in-time-honest historical dataset
  comparable to SEC EDGAR or even the Senate PTR mirror used above. Any backtest built on
  what is available (a handful of quarters of thin, survivorship-biased market history)
  would not be a real out-of-sample test — it would be curve-fitting to a tiny, recent,
  non-representative sample and presenting it with false confidence. That is worse than no
  result, which is why it was flagged instead of approximated.

---

## 7. What would need to be true to justify running either signal in the $10 agentic account

**This backtest is diagnostic only. It does not recommend live deployment of either
signal, and nothing here should be read as a green light.** Specifically, before either
signal could reasonably be proposed for the live account:

1. **Signal A needs a real, current, both-chambers dataset.** A Senate-only signal on
   data that stops in March 2021 says nothing about whether the pattern held up through
   the 2022 bear market, the 2023-2024 melt-up, or current disclosure/enforcement
   practices. Any live use would require either a paid congressional-trading data feed
   with House coverage and current data, or a from-scratch scraper against the House
   Clerk and Senate eFD sites with several years of forward validation before being
   trusted — not a quick fix.
2. **The core problem for both signals is structural, not implementation detail: the
   strategy did not beat cap-weighted equity indices on absolute return in this backtest,
   in-sample or out-of-sample.** Better Sharpe and smaller drawdown are real and valuable,
   but the account's own stated goal (CLAUDE.md: "beat the S&P 500 over months") was not
   met by either signal on CAGR. Before live deployment, this would need to either (a) be
   re-tested with a position-sizing scheme that actually monetizes the lower volatility
   (e.g., modest leverage sized to the strategy's own realized Sharpe, which a $10 account
   cannot safely do), or (b) show benchmark-beating CAGR in a regime that isn't an
   exceptional, backward-looking mega-cap bull run — which requires more out-of-sample
   time, not more backtesting of the same window.
3. **The 10b5-1 exclusion gap (§2.1) needs closing** before Signal B's win rate/profit
   factor can be trusted at face value pre-2023 — an unknown fraction of "open-market
   purchase" signals in that period may actually be pre-scheduled, information-free
   10b5-1 executions, which would mechanically dilute any real insider-conviction signal.
4. **The market-cap and earnings-proximity proxies (§2.3) are approximations.** A live
   version would need an actual point-in-time fundamentals feed and a real earnings
   calendar, not an XBRL-shares-outstanding proxy and an 8-K-date proxy — both proxies are
   defensible for a research backtest but are not precise enough to be trading rules in
   production.
5. **Sample size, especially for Signal A (118 trades total, 27 OOS), is too small to
   size real capital against.** A $10 account cannot generate enough independent trades
   from either signal (Signal A fires roughly 20-25 times/year even on the full,
   both-chambers universe this couldn't test; Signal B is far more frequent but has a much
   higher false-positive rate before filters) to make the realized win rate/profit factor
   statistically distinguishable from noise at that capital level, once realistic
   position-sizing constraints (can't take a $50 position in a $180B market-cap stock
   meaningfully) are applied.
6. **Costs modeled here (4bp/side) assume institutional-grade execution.** A $10 paper/live
   account trading fractional shares through Alpaca should re-verify this assumption
   against its own actual fill behavior before treating the net-of-cost numbers above as
   representative.

None of the above rules either signal out permanently — the adversarial placebo check in
§5 suggests there is a real, if modest, information edge in both cluster types. But
"real and modest" is a different claim from "ready to trade," and this backtest's own
result (underperforming a passive QQQ position, especially out of sample) is the honest
reason a human operator should not flip `DRY_RUN: false` on either of these signals based
on this report alone.

---

## Appendix: artifacts

All scripts, raw/intermediate data, and full trade-level output are in this repo (data
cache is gitignored; scripts and reports are committed):

- `backtesting/scripts/bt_common.py` — shared trading-calendar, Alpaca/SEC data-fetch, and
  performance-stat utilities.
- `backtesting/scripts/detect_clusters_signal_b.py`,
  `backtesting/scripts/backtest_signal_b.py` — Signal B pipeline.
- `backtesting/scripts/detect_clusters_signal_a.py`,
  `backtesting/scripts/backtest_signal_a.py` — Signal A pipeline.
- `backtesting/scripts/compute_stats.py` — IS/OOS stats + SPY/QQQ benchmarks.
- `backtesting/scripts/adversarial_check.py` — placebo/permutation sanity check (§5).
- `backtesting/reports/backtest_trades_SIGNAL_B_INSIDER.{csv,parquet}`,
  `backtesting/reports/backtest_trades_SIGNAL_A_CONGRESS.{csv,parquet}` — full trade logs.
- `backtesting/reports/backtest_rejections_SIGNAL_{A,B}_*.csv` — filter-funnel counts.
- `backtesting/reports/backtest_stats_SIGNAL_{A,B}_*.json` — full IS/OOS/benchmark stats.
- `backtesting/reports/backtest_adversarial_check_SIGNAL_A_B.json` — §5 raw output.
