# Episodic-Pivot (Earnings-Gap Continuation) — Research Backtest

**Date:** 2026-07-08
**Module:** `backtesting/episodic_pivot/` (research only — separate from PEAD and from the live 7-routine system)
**Branch:** `claude/momentum-backtest-module-7es7t2`
**Status:** Canonical run validated (reconciliation + manual re-derivation PASS). Full matrix + comparisons run. **Verdict: do NOT promote. Diagnostic only.**

---

## Survivorship-bias framing (read before any number)

This backtest uses **exactly the same earnings-event universe and price source as the
existing PEAD baseline**: the catalyst set is the committed PEAD *base* trade CSVs
(`backtesting/reports/backtest_trades_PEAD_2022_2024.csv` + `...2025_OOS.csv` →
`ticker, earn_date, surprise_pct, sector`), and prices are split/dividend-adjusted
OHLCV from the Yahoo chart API — the same source
`backtest_risk_sweep_entry_stop.py` uses. It therefore **inherits PEAD's known
survivorship limitation, documented in `backtesting/momentum_data_audit_2026-07-08.md`.**

> **This test can answer:** *"using the same imperfect dataset, does episodic pivot
> improve expectancy or diversify PEAD?"*
> **It cannot answer:** *"what would episodic pivot really have produced across the
> true historical S&P 500?"*

A concrete symptom of the shared bias: price fetches succeeded for **501/501**
event tickers with **zero misses**. That is not clean data — it is because the
PEAD-derived universe already contains only *survivors* (removed/delisted names were
never in it, and their prices 404 anyway, per the audit). Every table below is a
**relative comparison on survivorship-biased data — not absolute strategy evidence.**

---

## Executive summary

1. **The fully-specified episodic-pivot setup is extremely rare** on this
   large-cap universe: **33 qualifying events across 2022–2025 (~8/year)** →
   **21 in-sample trades (2022–2024) and 6 out-of-sample (2025)**. The binding
   filter is *opening gap ≥5%*, which only **11.8%** of ≥15% EPS beats satisfy.
2. **Out-of-sample is inconclusive by the spec's own bar.** No configuration in the
   54-cell grid reaches even 12 OOS trades (max = 10); **zero cells hit the 40–50
   trade minimum.**
3. **The result is single-trade fragile** — exactly episodic pivot's known failure
   mode. OOS: the **top trade is 79% of gross profit**; removing it turns OOS
   expectancy **negative (−1.46%/trade)**. IS: removing the top 5 trades turns
   expectancy negative (−1.58%/trade).
4. **It is not a diversifying second strategy — it is a selective sub-set of PEAD.**
   100% of EP events are PEAD events, 100% of EP tickers are PEAD tickers, and
   **93% of EP holding-days are concurrent with a PEAD position in the same name.**
5. **No demonstrated selection skill:** a random same-sector earnings name entered
   on the same dates returned **as much or more** than the EP selection
   (IS random +0.80% vs EP +0.59%; OOS random +1.34% vs EP +0.87% per trade).
6. **Recommendation: do not promote.** Fails OOS-sample, single-trade-concentration,
   and diversification criteria; the nominal passes (PF>1.25) rest on ≤6 trades.

---

## 1. Data source, universe, and known deviations (stated explicitly)

| Item | This backtest | PEAD baseline | Deviation? |
|---|---|---|---|
| Catalyst universe | PEAD base beat-events (committed CSVs) | same | none |
| Price source | Yahoo chart API, adj OHLCV, via `requests` | yfinance (same Yahoo data) | transport only (curl_cffi fails this env's proxy) |
| Surprise threshold | ≥15% | 15% (enhanced filter) | none |
| Position size | **5%** | live 11% / 20% | **intentional — risk params tested independently, not inherited** |
| Sector cap | 30% | n/a | EP-specific |
| Costs | 10 bps/side (spread+slippage) applied to fills | n/a in artifacts | EP-specific, stated below |
| In-sample | 2022–2024 | 2022–2024 | none |
| Out-of-sample | **2025 only** | 2025 (+2026 YTD) | **2026 H1 excluded — see below** |

**Why OOS stops at 2025 (documented gap, not a silent omission).** The committed
artifacts contain a full *base* earnings-event set for 2022–2024 and 2025, but only a
30-row *enhanced-filtered* file for 2026 — not a base universe. The reachable live
Yahoo `earningsHistory` endpoint returns fiscal-**period-end** dates (e.g.,
`2026-03-31`), **not announcement dates**, so it cannot locate a 2026 gap bar without
being wrong by weeks. Rather than fabricate 2026 entries, 2026 H1 is reported as a
coverage gap. (Verified during the audit; same discipline as the momentum audit.)

**Cost assumption (exact):** each fill is moved against the strategy by **10 bps**
(≈5 bps half-spread + 5 bps slippage): buys fill at `raw × 1.0010`, sells at
`raw × 0.9990`. Next-session execution only; no same-bar fills. Reported
`slippage_cost_$` is the aggregate dollar drag.

---

## 2. Signal definition & the rarity funnel

Announcement bar = first session on/after `earn_date`. All features use data up to and
including that bar (no look-ahead). Entry is the **next** session (EP-A) or a breakout
above the announcement-day high within 5 sessions (EP-B).

**EP setup filters:** `surprise ≥15%` **and** `open-gap ≥5%` **and**
`open > prior-20-day high` **and** `announcement volume ≥2× prior-20-day avg`
**and** `close in upper 25% of day range` **and** `announcement close ≥+4%`.

**Table 2.1 — Filter funnel on the ≥15% EPS-beat population — relative comparison, survivorship-biased**

| Stage | Events remaining | Pass-rate of stage |
|---|---|---|
| ≥15% surprise beats (with valid features) | 1,516 | — |
| … `gap ≥5%` | 179 | 11.8% ← **binding** |
| … `+ vol ≥2×` | 153 | (41.9% standalone) |
| … `+ open > 20-day high` | 107 | (18.9% standalone) |
| … `+ close in top 25% of range` | 33 | (31.1% standalone) |
| … `+ close ≥+4%` | 33 | (21.5% standalone) |
| **Full EP setup** | **33** | **2.2% of ≥15% beats** |
| … after "skip if structural stop >8%" | 27 | |

By year (full EP setup): **2022 = 5, 2023 = 7, 2024 = 11, 2025 = 10.** ~8 setups/year.
This is not a bug (per-filter counts above); large-cap S&P names simply rarely gap
≥5% at the open on earnings *and* close in the top quartile *and* above the 20-day high.

---

## 3. Canonical run — VALIDATION FIRST (gate before the matrix)

Canonical config: `gap≥5%, vol≥2×, next-open entry, structural stop below
announcement-day low (capped 8%), combined earliest-trigger exit
{structural stop, 20-session time stop, 7% trail after +10%}`.

**Reconciliation (both PASS):**
- **Daily:** `equity == cash + mark-to-market` every day (max residual < 1e-6); cash
  never negative; invested fraction never > 1 (no leverage); sector ≤ 30%.
- **Aggregate:** `start_equity + Σ(trade PnL) == final cash` to < $1.

**Manual trade re-derivation (independent recompute from raw OHLCV — all matched):**

**Table 3.1 — Hand-verified trades — relative comparison, survivorship-biased**

| Ticker | earn_date | gap | vol× | range | ann.ret | entry date (engine=manual) | entry fill | exit | net |
|---|---|---|---|---|---|---|---|---|---|
| UBER | 2023-02-08 | 7.25% | 4.87 | 0.76 | 5.53% | 2023-02-09 ✓ | 36.93 | struct_stop | −6.94% |
| LDOS | 2024-10-29 | 7.23% | 3.63 | 0.89 | 9.50% | 2024-10-30 ✓ | 184.81 | struct_stop | −5.97% |
| TGT | 2023-11-15 | 13.80% | 7.77 | 0.84 | 17.75% | 2023-11-16 ✓ | 116.20 | time_stop | +8.51% |
| KVUE | 2024-08-06 | 10.78% | 2.60 | 0.94 | 14.68% | 2024-08-07 ✓ | 19.07 | time_stop | +9.63% |

Recomputed features match the filter thresholds; entry dates match; fills equal the
next-session open × (1 + 10 bps). **Canonical validation passes → matrix authorized.**

**Table 3.2 — Canonical results by period — relative comparison, survivorship-biased**

| Metric | IS 2022–2024 | OOS 2025 |
|---|---|---|
| Qualifying trades (n) | **21** | **6** |
| Total return (portfolio) | 0.66% | 0.07% |
| CAGR | 0.23% | 0.08% |
| Max drawdown | −1.76% | −0.68% |
| Sharpe (daily) | 0.24 | 0.09 |
| Win rate | 47.6% (10/21) | 50.0% (3/6) |
| Expectancy / trade | 0.59% | 0.87% |
| Median return / trade | −0.29% | −0.05% |
| Profit factor | 1.27 | 1.49 |
| Avg hold (sessions) | 13.7 | 14.5 |
| Avg invested fraction | 2.06% | 2.09% |
| % days ≥1 position | 29.9% | 29.0% |
| Turnover (annualized) | 0.37× | 0.36× |
| Est. slippage cost | $208 | $60 |
| **Largest-winner contribution** | **16.8%** | **79.2%** |
| Top-5-winner contribution | 65.2% | 70.5% |
| **Expectancy ex-top-1** | 0.14% | **−1.46%** |
| **Expectancy ex-top-5** | **−1.58%** | −5.93% |

Portfolio CAGR is ~0 **because the signal fires ~8×/year at 5% size, so capital is
~98% idle** (avg invested ~2%). Return *per unit of deployed capital* (crude
exposure-adjustment = total return ÷ avg invested fraction) is ~32% IS / ~3% OOS —
but that scaling assumes ~50× more concurrent signals than exist, so it is a
capacity fiction, not an achievable return. The honest read is the **per-trade**
block, and it is **single-trade-fragile** (rows in bold).

---

## 4. Parameter grid (54 cells) — after validation

Grid = `gap{5,8,10%} × vol{1.5,2,3×} × entry{next-open,breakout} × maxhold{10,20,30}`,
each run for IS and OOS (108 rows). **All cells reconcile.** Full data:
`backtesting/episodic_pivot/reports/grid_results.csv`.

**Table 4.1 — Trade-count reality across the grid — relative comparison, survivorship-biased**

| Period | min trades | max trades | mean | cells ≥40 trades |
|---|---|---|---|---|
| IS 2022–2024 | 5 | 23 | 10.4 | 0 |
| OOS 2025 | 2 | 10 | 3.8 | **0** |

The loosest cell (`gap5/vol1.5/next-open`) yields the most: 23 IS / 10 OOS.
**Every cell is below the OOS-sample bar.** Higher gap/vol thresholds only shrink
the count. Cell-level expectancies swing widely (IS −0.22% to +1.69%; OOS −0.34% to
+5.67%) — noise at n≤23. One consistent (but low-confidence) pattern: **shorter
max-hold (10 sessions) improves IS expectancy-ex-top1** (1.26% vs ≤0.25% at 20/30),
i.e., cutting winners' giveback helps — but this rests on ~20 trades.

---

## 5. Isolated exit experiments (canonical filter, exits tested one at a time)

**Table 5.1 — Isolated vs combined exits — relative comparison, survivorship-biased**

| Exit rule | Period | n | Win% | Expectancy | Median | PF | Largest-winner% |
|---|---|---|---|---|---|---|---|
| −8% hard only¹ | IS | 20 | 20.0% | 12.61% | −8.18% | 2.77 | 36.9% |
| −8% hard only¹ | OOS | 6 | 33.3% | 9.81% | −8.18% | 2.63 | 74.7% |
| 20-sess time only | IS | 21 | 47.6% | −0.51% | −0.29% | 0.84 | 17.5% |
| 20-sess time only | OOS | 6 | 66.7% | 0.47% | +1.65% | 1.16 | 62.5% |
| 7% trail after +10% | IS | 19 | 78.9% | 3.21% | +4.80% | 1.52 | 22.6% |
| 7% trail after +10% | OOS | 6 | 83.3% | 7.92% | +6.15% | 2.52 | 45.3% |
| Exit-before-next-earn | IS | 21 | 47.6% | −0.06% | −2.91% | 0.98 | 25.4% |
| Exit-before-next-earn | OOS | 6 | 66.7% | 20.98% | +14.63% | 7.14 | 52.3% |
| **Combined (canonical)** | IS | 21 | 47.6% | 0.59% | −0.29% | 1.27 | 16.8% |
| **Combined (canonical)** | OOS | 6 | 50.0% | 0.87% | −0.05% | 1.49 | 79.2% |

¹ **"−8% hard only" is misleading and flagged:** with no time/trail exit, winners are
held to end-of-data (up to years), inflating expectancy — an artifact, not tradeable.
The trailing-stop exit looks best in isolation (rides winners, exits on pullback), but
on 19 IS / 6 OOS trades this is not a conclusion.

---

## 6. Required comparisons (canonical config, identical dates/costs)

**Table 6.1 — Episodic pivot vs benchmarks — relative comparison, survivorship-biased**

| Strategy | Period | n | Win% | Expectancy/trade | PF | Total ret (portfolio) | Largest-winner% |
|---|---|---|---|---|---|---|---|
| Episodic pivot | IS | 21 | 47.6% | 0.59% | 1.27 | 0.66% | 16.8% |
| Episodic pivot | OOS | 6 | 50.0% | 0.87% | 1.49 | 0.07% | 79.2% |
| Simple gap (gap+vol only) | IS | 246 | 35.0% | 1.12% | 1.68 | 14.14% | 4.8% |
| Simple gap (gap+vol only) | OOS | 91 | 22.0% | −0.38% | 0.82 | −1.46% | 20.0% |
| PEAD (from artifacts²) | IS | 4,387 | 54.8% | 1.32% | 1.45 | — | — |
| PEAD (from artifacts²) | OOS | 1,454 | 55.5% | 1.54% | 1.55 | — | — |
| Random matched control³ | IS | 105 | 30.5% | 0.80% | — | — | — |
| Random matched control³ | OOS | 30 | 33.3% | 1.34% | — | — | — |
| SPY buy-and-hold | IS | — | — | — | — | **+40.4%** (CAGR 12.7%, DD −22%) | — |
| SPY buy-and-hold | OOS | — | — | — | — | **+12.8%** (CAGR 15.7%) | — |

² PEAD re-pulled from its own trade artifacts (NOT re-simulated); PEAD's own sizing &
~42-cal-day hold — trade-level, not portfolio-CAGR-comparable to EP.
³ For each EP trade: random same-sector beat within ±10 days, next-open entry, same
exits; mean over 5 seeds. Raw per-trade returns.

**What the comparisons say:**
- **vs PEAD:** PEAD has ~150–700× more trades and a **higher per-trade expectancy**
  (1.32%/1.54% vs 0.59%/0.87%). EP adds no expectancy and far less capacity.
- **vs SPY:** SPY buy-hold dwarfs EP's portfolio return — but this is mostly EP's ~2%
  exposure, not a per-trade indictment. Still, EP cannot deploy capital.
- **vs simple gap baseline:** the naive gap+vol baseline has *more* trades (246/91) and
  *lower* single-trade concentration (4.8% IS), and it **loses money OOS** (PF 0.82) —
  so the earnings-gap idea itself does not survive 2025 OOS even with a usable sample.
- **vs random control:** EP's careful selection does **not** beat a random same-sector
  earnings name (random ≥ EP in both periods). No evidence of selection skill.

---

## 7. Overlap with PEAD (the key diversification question)

**Table 7.1 — EP vs PEAD overlap (all 27 canonical trades, 2022–2025) — relative comparison, survivorship-biased**

| Dimension | Value |
|---|---|
| EP tickers | 23 |
| Shared with PEAD | 23 (**100%**) |
| EP earnings events | 27 |
| Shared with PEAD | 27 (**100%**) |
| EP holding business-days | 416 |
| Concurrent with a PEAD position, same ticker | 387 (**93%**) |
| Monthly realized-PnL correlation⁴ | **+0.57** (20 monthly points) |

⁴ **Realized-PnL-by-exit-month proxy only.** A true daily mark-to-market return
correlation is **NOT computable** from PEAD's artifacts, which are trade-level CSVs with
no dated portfolio return series (consistent with the momentum audit's finding). The
proxy buckets each side's realized PnL by exit month.

**Conclusion, stated plainly and not softened: episodic pivot as specified is a PEAD
sub-variant, not a diversifying second strategy.** Every EP trade is a PEAD trade on the
same earnings event; EP is concurrently long the same names 93% of the time; monthly
PnL is positively correlated. It selects a small, high-gap slice of PEAD's own beat
universe.

---

## 8. Pass-criteria evaluation → **DO NOT PROMOTE**

**Table 8.1 — Promotion checklist (OOS) — relative comparison, survivorship-biased**

| Criterion | Threshold | Result | Verdict |
|---|---|---|---|
| Positive net expectancy after costs | >0 | +0.87% | ⚠ nominal, but ex-top-1 = −1.46% |
| Profit factor | > ~1.25 | 1.49 | ⚠ on 6 trades only |
| Drawdown vs PEAD | acceptable | −0.68% | ⚠ artifact of ~2% exposure |
| OOS trade count | ≥ 40–50 | **6** | ❌ **fail (inconclusive)** |
| Positive across >1 calendar year | ≥2 yrs | only 2025 available | ❌ not satisfiable |
| No single trade > 20% of profit | <20% | **79%** | ❌ **fail** |
| Meaningfully different from PEAD | yes | 100% event overlap, 93% concurrent | ❌ **fail** |

Fails outright on trade count, single-trade concentration, and diversification; the
multi-year criterion is unsatisfiable given the 2026 data gap; the three nominal passes
rest on ≤6 trades and vanish when the best trade is removed. **No live-deployment
recommendation is made.**

---

## 9. Discipline notes

- **Raw counts & denominators** are given for every rate (funnel §2, trade counts §3–6).
- **IS and OOS are reported separately**, never averaged; OOS parameters never fed IS choice.
- **Not judged by win rate** (which is ~50%); judged by expectancy, sample size,
  single-trade concentration, and overlap.
- **Unusually strong cells flagged as artifacts:** the "−8% hard only" 12.6% expectancy
  is a hold-to-data-end artifact; high OOS PFs (e.g., earn-only 7.14) are single-trade
  driven at n=6.
- **This is diagnostic only.** No orders placed; `memory/strategy.md` and all memory
  files untouched; nothing merged into the live 7-routine system.

---

## 10. Reproducibility

```bash
cd /home/user/trading-routine
pip install pandas numpy requests
python3 backtesting/episodic_pivot/run_fetch.py       # cache prices (coverage.json)
python3 backtesting/episodic_pivot/run_canonical.py   # canonical + validation
python3 backtesting/episodic_pivot/diag_funnel.py     # per-filter funnel
python3 backtesting/episodic_pivot/run_full.py         # grid + comparisons + overlap
```

Artifacts: `backtesting/episodic_pivot/reports/` — `grid_results.csv`,
`isolated_exits.csv`, `comparisons.json`, `overlap.json`, `canonical_results.json`,
`canonical_trades_*.csv`, `canonical_equity_*.csv`, `coverage.json`.

**Bottom line:** On the same survivorship-biased dataset as PEAD, the specified
episodic-pivot strategy is too rare to evaluate out-of-sample, single-trade-fragile,
shows no selection skill over random same-sector earnings names, and is a concurrent
sub-set of PEAD rather than a diversifier. It does not improve or diversify PEAD here,
and this says nothing about its true historical performance on the full S&P 500.
