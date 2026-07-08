# Cross-Sectional Momentum — Data-Availability Audit

**Date:** 2026-07-08
**Module:** `backtesting/momentum/` (research only — completely separate from PEAD)
**Author routine:** ad-hoc research task (not one of the live 7 routines)
**Branch:** `claude/momentum-backtest-module-7es7t2`

---

## 0. Verdict (read this first)

> **AUDIT RESULT: FAIL.** The primary point-in-time momentum backtest **was not run**
> and **must not be run** on the data reachable from this environment.
>
> The two gating requirements — **(1) point-in-time S&P 500 membership with
> entry/exit dates** and **(2) delisted-price coverage** — are **not satisfiable**.
> Delisted names return HTTP 404 from the only price source available, so a
> momentum strategy cannot see the very stocks it would have rotated out of. This
> is a **fatal survivorship problem**, not a transport hiccup.

Per the task's own rule — *"A failed audit is a valid, useful final result — stop
there and report it"* and *"if the data audit fails, write to
`backtesting/momentum_data_audit_2026-07-08.md` and stop"* — **this document is the
final deliverable.** No trade/equity logs, no CAGR/Sharpe/drawdown tables, no
variant matrix were produced, because producing them would mean reporting numbers
I know to be biased.

### Per-check scorecard

| # | Check | Result | One-line reason |
|---|-------|--------|-----------------|
| 1 | Point-in-time membership entry/exit dates (≥3 removed names) | **FAIL** | Only a *current* constituents snapshot is available; the reachable change-log (Wikipedia) is incomplete, retroactively editable, and not a frozen PIT series. |
| 2 | Delisted-price history for ≥1 removed name | **FAIL** | All 6 tested removed names (SIVB, FRC, TWTR, CTXS, ATVI, XEC) return **HTTP 404**. Yahoo purges delisted tickers. |
| 3 | Split/dividend adjustment applied | **PASS** | Yahoo `adjclose` is continuous across AAPL 4:1, NVDA 10:1, TSLA 3:1, AMZN 20:1 (jump ratio ≈ 1.00). |
| 4 | Ticker-change handling | **FAIL** | Old symbols (FB, ANTM, DISCA, RE) 404; history is silently folded into the new symbol. No programmatic rename map. |
| 5 | No future-membership leakage | **FAIL** | Current-only list ⇒ survivorship bias + look-ahead. 215/503 current members were added after 2012-01-01. |

Gate logic: the primary backtest requires **1 AND 2 AND 5**. All three fail. Even
though split/dividend adjustment (3) works, it cannot rescue a universe that is
missing its removed names.

---

## 1. Why the audit ran first, and how transport failure was ruled out

The task requires the audit to gate everything, and specifically to *"test the
data source's actual point-in-time correctness with specific cases before trusting
it."* A naïve run is dangerous here because a **transport failure can masquerade
as missing data** — you must not report "data unavailable" when the real cause is
a proxy/TLS problem.

**First attempt used `yfinance` and failed with `curl (35) Recv failure: Connection
reset by peer`** for *every* ticker, including live ones. Diagnosis: yfinance's
`curl_cffi` backend does not honor this environment's HTTPS proxy (`HTTPS_PROXY`)
or its CA bundle (`/root/.ccr/ca-bundle.crt`). This is a **client-configuration
failure, not a data-availability signal**, so it was discarded.

**Second attempt used plain `requests` against the Yahoo chart API v8** — the exact
transport the existing `backtesting/scripts/backtest_risk_sweep_entry_stop.py`
already uses successfully. `requests` honors `HTTPS_PROXY` and the system CA.

To prove the transport works before trusting any 404, a **live control ticker
(AAPL) is fetched first**:

```
CHECK -1 — Transport control
  AAPL control: OK, rows=1258 [2019-01-02..2023-12-29]
  -> transport confirmed working; subsequent empties/404s are REAL.
```

Because the control succeeds, every 404 reported below is a genuine
data-availability finding.

**Audit script:** `backtesting/momentum/audit_data_availability.py`
**Raw log:** `backtesting/momentum/data_cache/audit_raw_output.txt`
**Machine-readable results:** `backtesting/momentum/data_cache/audit_results.json`

---

## 2. Data sources evaluated

| Role | Source | PIT membership? | Delisted prices? | Notes |
|------|--------|-----------------|------------------|-------|
| Membership (in-repo) | `scripts/sp500_source.csv` | No | n/a | Columns `symbol, sector, date_added`. **Entry dates only, no exit dates, no removed names.** 503 rows. |
| Membership (engine) | `datasets/s-and-p-500-companies` GitHub CSV (what `backtest_pead_2026_ytd.get_sp500()` uses) | No | n/a | Columns include `Date added` only. **Current snapshot**, 503 rows. |
| Membership changes | Wikipedia "Selected changes to the list of S&P 500 components" | Partial / unreliable | n/a | Reachable, but see Check 1. |
| Prices | Yahoo Finance chart API v8 (via `requests`) | n/a | **No** | Live names OK & split/div-adjusted; delisted names 404. |

Other MCP data surfaces present in the environment (Robinhood `get_equity_historicals`,
Alpaca bars) were **not** adopted: both serve only *currently tradable* instruments,
so neither can return history for delisted names (the exact gap that fails the
audit), and neither carries point-in-time index membership. Adopting them would
not change any verdict below. The audit deliberately uses the **same** price source
the existing PEAD research uses, so this finding is directly comparable to the
rest of the repo's tooling.

---

## 3. Evidence, check by check

### Check 1 — Point-in-time membership entry/exit dates — **FAIL**

Neither reachable constituents file carries exit dates or removed names — both are
**current snapshots**. The only reachable *change log* is Wikipedia's "Selected
changes" table (402 rows, columns: `Effective Date`, `Added Ticker/Security`,
`Removed Ticker/Security`, `Reason`). It **does** contain datable change events for
all six test names:

```
removed=SIVB  rows: 2 | dates: March 15, 2023 ; March 19, 2018
removed=FRC   rows: 2 | dates: May 4, 2023 ; January 2, 2019
removed=TWTR  rows: 2 | dates: November 1, 2022 ; June 7, 2018
removed=CTXS  rows: 1 | dates: October 3, 2022
removed=ATVI  rows: 2 | dates: October 18, 2023 ; August 28, 2015
removed=XEC   rows: 2 | dates: March 2, 2020 ; June 20, 2014
```

**Why this still fails the requirement:** the task needs *point-in-time-correct*
membership — an authoritative record, frozen as-of each date, with continuous
entry→exit intervals and no future leakage. Wikipedia's live table is:
- **Incomplete** for older years (it is "selected changes," not a complete ledger);
- **Retroactively editable** — today's page is not what was true on a 2014 rebalance date;
- **Interval-incomplete** — each row is one side of a transition, not a membership span;
- **Not cross-validatable** here — no authoritative reference (CRSP/Compustat/S&P
  index files) is reachable to confirm the reconstruction.

So membership dates are *partially discoverable* but **not trustworthy as a PIT
series**, and — critically — Check 2 shows the prices for these names are gone
regardless, so a perfect membership map would not rescue the backtest.

### Check 2 — Delisted-price history — **FAIL (decisive)**

```
SIVB  (delisted ~2023-03-15): HTTP 404  -> NO DATA
FRC   (delisted ~2023-05-04): HTTP 404  -> NO DATA
TWTR  (delisted ~2022-11-08): HTTP 404  -> NO DATA
CTXS  (delisted ~2022-09-30): HTTP 404  -> NO DATA
ATVI  (delisted ~2023-10-13): HTTP 404  -> NO DATA
XEC   (merged   ~2021-10-01): HTTP 404  -> NO DATA
Removed names with usable price history: NONE
```

The control ticker returns 1,258 rows over the same transport, so these 404s are
real: **Yahoo does not retain price history for delisted tickers.** Zero of six
removed names are recoverable. This alone is disqualifying (see §4).

### Check 3 — Split/dividend adjustment — **PASS**

Yahoo's `adjclose` series is continuous across major splits (a correctly adjusted
series shows ≈ 1.00 across the split date, not a 1/ratio cliff):

```
AAPL  4:1 : adj 121.06 -> 125.17  ratio=1.034  ADJUSTED (continuous)
NVDA 10:1 : adj 120.82 -> 121.72  ratio=1.007  ADJUSTED (continuous)
TSLA  3:1 : adj 297.10 -> 296.07  ratio=0.997  ADJUSTED (continuous)
AMZN 20:1 : adj 122.35 -> 124.79  ratio=1.020  ADJUSTED (continuous)
```

Split and dividend adjustment is trustworthy **for surviving names**. (This is the
one check that passes; it is necessary but nowhere near sufficient.)

### Check 4 — Ticker-change handling — **FAIL**

```
FB   -> META : OLD FB    HTTP 400 (no data) ; NEW META rows=3028 [2012-05-18..], spans rename: True
ANTM -> ELV  : OLD ANTM  HTTP 404 (no data) ; NEW ELV  rows=3627 [2010-01-04..], spans rename: True
DISCA-> WBD  : OLD DISCA HTTP 404 (no data) ; NEW WBD  rows=3627 [2010-01-04..], spans rename: True
RE   -> EG   : OLD RE    HTTP 404 (no data) ; NEW EG   rows=3627 [2010-01-04..], spans rename: True
```

The new symbol carries the full pre-rename history, but the **old symbol 404s**.
There is **no programmatic rename map** from the price API. A PIT backtest that knows
a name only by its *historical* ticker on a rebalance date (e.g., `FB` in 2021) would
fetch nothing and **silently drop the name**, distorting the ranked universe. A
correct pipeline needs a hand-maintained rename map — which was not built, because
Checks 1/2/5 already fail the gate.

### Check 5 — No future-membership leakage — **FAIL**

```
Current list: 503 names.
  added after 2012-01-01: 215  (would leak if used before their add date)
  added after 2023-01-01: 56
  missing/unparseable date_added: 0
```

Using the current snapshot as the historical universe causes **both** classic biases:
- **(a) Survivorship bias** — names that were in the index during 2012–2026 but have
  since been removed are simply absent, and their prices 404 (Check 2), so they
  cannot be restored.
- **(b) Look-ahead / future-membership leakage** — 215 of 503 current members were
  added after 2012-01-01; using them before their add date front-runs the index
  committee. `date_added` can partially guard (b) but does **nothing** for (a).

---

## 4. Why this is especially fatal for *momentum* (not just a generic caveat)

Survivorship bias is not a rounding error for this strategy — it is structurally
aligned with the signal:

- **Removed names are disproportionately the losers.** Index deletions come from
  price collapse, distress, bankruptcy, and failed takeovers (SIVB, FRC, TWTR under
  duress). A 6-1 momentum screen would have **ranked these names into the bottom
  decile and, in the isolated-exit tests, sold them** — but with their price
  history deleted, the backtest never holds them *and never books their losses.*
- **The bias inflates exactly the metric under study.** Removing terminal losers
  lifts CAGR, compresses drawdown, and raises Sharpe/profit-factor. A momentum
  backtest on survivors would look *better* than reality precisely where it matters.
- **Merger/rename gaps compound it.** Because old tickers 404 (Check 4), the
  historical universe on any past rebalance date is silently thinned toward names
  that kept their ticker — another selection distortion.

Any headline number from a survivors-only run would therefore be **upward-biased by
construction** and must never be read as strategy evidence.

---

## 5. What a PASSING data setup would require

To lift this gate and run the primary backtest as specified, the environment needs:

1. **Point-in-time S&P 500 membership** with entry **and** exit dates and continuous
   intervals — e.g., CRSP/Compustat index constituents, S&P's own index files,
   Norgate Data, or a vendor with a documented as-of methodology. Not a live wiki.
2. **Delisted (dead) price history** — split/dividend-adjusted OHLCV that survives
   after delisting — from the same class of vendor (CRSP is the canonical academic
   source; Norgate/Sharadar/Polygon "delisted" tiers are commercial options).
3. **A ticker-change / CUSIP-permno map** so historical symbols resolve to a stable
   security identifier across renames (FB→META, ANTM→ELV, …).
4. *(Optional but specified)* **Point-in-time earnings dates** as-known (not a
   later-corrected calendar) for the earnings-exclusion entry filter. If absent, the
   task says to drop that filter from the baseline and disclose it — moot here since
   the backtest does not run.

Split/dividend adjustment (Check 3) is already adequate and would carry over.

---

## 6. Items deliberately NOT produced (and why)

- **Primary backtest (6-1, top-10, combined exit) + canonical validation** — not run.
  Gate failed. This is the intended outcome, not an incomplete task.
- **Variant matrix (portfolio construction / lookback / isolated exits)** — not run;
  only reachable after canonical validation, which is gated off.
- **Survivorship-biased "pipeline test" on current constituents** — **declined.** The
  task permits it *only if explicitly labeled and never treated as strategy evidence*,
  and simultaneously instructs "produce only a data-availability report … and stop."
  Building it now would manufacture biased numbers whose main risk is being misread
  later. It can be run later as a clearly-labeled, evidence-free *code smoke-test* if
  the operator explicitly requests it; it is intentionally omitted here.
- **PEAD monthly-return correlation** — **not computable**, for two independent
  reasons: (a) the momentum backtest produced no return series to correlate; and
  (b) the PEAD artifacts in `backtesting/reports/` are **trade-level CSVs**
  (`ticker, entry_date, exit_date, return_pct, …`) with **no dated portfolio
  return/equity series**, so they do not export a compatible dated series. Per the
  task, this is reported as *"not computable from available PEAD artifacts"* rather
  than reconstructed from summary statistics.

---

## 7. Reproducibility

```bash
cd /home/user/trading-routine
pip install pandas numpy requests lxml        # yfinance NOT needed (its curl_cffi
                                              # backend fails this env's proxy; the
                                              # audit uses requests + Yahoo chart API)
python3 backtesting/momentum/audit_data_availability.py
# -> prints the five checks, writes:
#    backtesting/momentum/data_cache/audit_raw_output.txt
#    backtesting/momentum/data_cache/audit_results.json
```

The script fetches a live control ticker first and **aborts with a transport-failure
verdict** if the control fails, so it can never confuse a proxy problem with a data
gap.

---

## 8. Scope & compliance statement

- **Research only.** No orders were placed; no Alpaca/Robinhood trading endpoints
  were called.
- **`memory/strategy.md` was not read for edits and was not modified.** No memory
  file was modified. This module is isolated under `backtesting/momentum/` and the
  report file under `backtesting/`.
- **Not merged into the live 7-routine system.** No routine, `compute_pead_health.py`,
  or PEAD artifact was touched. Work is on branch
  `claude/momentum-backtest-module-7es7t2`, not `main`.
- **Diagnostic only. No live-deployment recommendation is made or implied.**
