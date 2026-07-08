# backtesting/ — PEAD research artifacts

This folder holds the **research** that validated the PEAD (post-earnings
announcement drift) strategy and its signal-health overlay. Nothing here runs as
part of the live trading routines — it is the audit trail behind the rules in
`memory/strategy.md` and the production overlay script. These scripts are run
manually, on demand, when re-validating or extending the strategy.

```
backtesting/
  scripts/      backtest research scripts (backtest_*.py)
  reports/      generated .md reports + .csv trade/candidate logs
  data_cache/   gitignored per-ticker yfinance cache (may be empty)
  README.md     this file
```

> **Production note — read before moving anything.**
> `compute_pead_health.py` is **NOT** here. It lives at the **repo root** because
> it is wired into the live `routines/universe_refresh.md` routine (run weekly as
> `python compute_pead_health.py`) and writes `memory/pead_health.md`. It is
> production code and must stay at the root. It *imports* the research engine
> `backtest_pead_2026_ytd.py`, which is why that one engine module **also stays
> at the repo root** rather than moving into `scripts/` (see "Why the engine
> stays at root" below). Everything else `backtest_*` lives under
> `backtesting/scripts/`.

## Scripts

All scripts write their report/CSV outputs into `backtesting/reports/` and use
`backtesting/data_cache/` for the on-disk price cache, regardless of the working
directory you launch them from (paths are anchored to each script's own
location via `__file__`).

| Script | Location | What it does | Produces |
|--------|----------|--------------|----------|
| `backtest_pead.py` | `scripts/` | Original in-sample PEAD backtest, 2022–2024. | `backtest_report_PEAD_2022_2024.md`, `backtest_trades_PEAD_2022_2024.csv` |
| `backtest_pead_2025_oos.py` | `scripts/` | Out-of-sample replay on 2025 to check the edge wasn't curve-fit. | `backtest_report_PEAD_2025_OOS.md`, `backtest_trades_PEAD_2025_OOS.csv` |
| `backtest_pead_2026_ytd.py` | **root** | Enhanced-filter PEAD engine + 2026-YTD run. **Shared engine** imported by the production health script and by the other research scripts. | `backtest_report_PEAD_2026_YTD.md`, `backtest_trades_PEAD_2026_YTD.csv` |
| `backtest_validate_filters_2022_2025.py` | `scripts/` | Applies the enhanced filter stack to a large 2022–2025 sample to judge each filter. Also defines the disk cache (`cached_fetch`, `CACHE_DIR`) and `robust_spy`, reused by the scripts below. | `backtest_report_PEAD_2022_2025_ENHANCED.md`, `backtest_trades_PEAD_2022_2025_ENHANCED.csv`, `..._ENHANCED_base.csv` |
| `backtest_signal_health_gate.py` | `scripts/` | Tests realized/drift signal-health gates on the EPS-beat population. | `backtest_report_PEAD_SIGNAL_HEALTH.md`, `backtest_signal_health_candidates.csv` |
| `backtest_health_200ma_combo.py` | `scripts/` | Combines the realized-health gate with the SPY>200MA regime filter — the overlay that ships in production. Reuses the cached candidate set. | `backtest_report_PEAD_HEALTH_200MA_COMBO.md` |
| `backtest_variants_compare.py` | `scripts/` | Compares rule variants (drop 52-wk filter, 7% trail, bull-regime gate, …) against current rules. | `backtest_report_PEAD_VARIANTS.md`, `backtest_variants_candidates.csv` |
| `backtest_risk_sweep_entry_stop.py` | `scripts/` | Grid parameter sweep: EPS-surprise threshold × score-cutoff (verifiable-filter proxy) × stop width (flat −8/−10/−12%, ATR-scaled), IS=2022-24 / OOS=2025 + 2026 cross-check. Reuses the committed candidate set and the S3 `simulate()` mechanics; re-fetches OHLC via the Yahoo chart API. **Diagnostic only** — confirms S3's wider-stop rejection and finds no validated entry/stop improvement. | `memory/backtest_risk_sweep_<date>.md` (report), `backtest_risk_sweep_grid_<date>.csv`, `backtest_risk_sweep_trades_<date>.csv` |

### Dependency map

```
backtest_pead_2026_ytd.py  (root, shared engine)
        ▲                ▲
        │                │ import backtest_pead_2026_ytd
        │                │
compute_pead_health.py    backtest_validate_filters_2022_2025.py  (defines cached_fetch / robust_spy / CACHE_DIR)
   (root, PRODUCTION)              ▲
                                   │ from backtest_validate_filters_2022_2025 import ...
                                   │
        backtest_signal_health_gate.py
        backtest_health_200ma_combo.py
        backtest_variants_compare.py
```

`backtest_pead.py` and `backtest_pead_2025_oos.py` are standalone (no cross-imports).

### Why the engine stays at root

`compute_pead_health.py` (production) runs from the repo root and does
`import backtest_pead_2026_ytd as eng`. Python resolves that against the root
directory, so the engine module must remain at the root for the live routine to
keep working. Moving it would silently break `universe_refresh`. The research
scripts under `scripts/` reach the root engine via a small `sys.path` bootstrap
at the top of each importing file — they do **not** require the engine to be
co-located.

## How `data_cache/` works

- Per-ticker `(history, earnings)` tuples fetched from **yfinance** are pickled
  into `backtesting/data_cache/<TICKER>.pkl` by `cached_fetch()` in
  `backtest_validate_filters_2022_2025.py`. Subsequent runs read from the cache,
  so reruns are fast and deterministic.
- The directory is **gitignored** (`.pkl` files are large and reproducible).
  Only an empty `.gitkeep` is committed, so a fresh clone has the folder but no
  data. If the cache is absent, the first run simply rebuilds it from yfinance.

### Refreshing / rebuilding the cache

The cache has no automatic expiry — it persists across runs once populated.
To force a refresh (e.g. after stale or corrupt data, or to pull newer bars):

```bash
# from the repo root
rm -rf backtesting/data_cache/*.pkl      # drop cached pickles (keeps .gitkeep)
python3 backtesting/scripts/backtest_validate_filters_2022_2025.py   # repopulates on the fly
```

Any research script that calls `cached_fetch` will re-fetch and re-cache missing
tickers on its next run, so deleting individual `<TICKER>.pkl` files refreshes
just those names.

Dependencies: `yfinance`, `pandas`, `numpy`, `requests` (install into the
environment before running).

## How `routines/strategy_review.md` will consume this

A future `strategy_review` routine (not yet created — referenced here so the
wiring is documented) will drive these scripts to periodically re-validate the
live rules: re-run the enhanced-filter and variant comparisons over the latest
data, diff the headline win-rate / profit-factor against the historical reports
in `reports/`, and flag drift for human review. It will treat this folder as
read-mostly tooling — it runs the scripts and reads the reports, but (like every
routine) it will **not** edit `memory/strategy.md`. It will not touch the
production `compute_pead_health.py` at root either; that script's weekly refresh
stays owned by `universe_refresh`.

## Historical reports

| Report | Test period | Headline | Status |
|--------|-------------|----------|--------|
| `backtest_report_PEAD_2022_2024.md` | 2022–2024 (in-sample) | 4,387 trades, **54.8%** win, PF 1.45 | Validated — original in-sample baseline |
| `backtest_report_PEAD_2025_OOS.md` | 2025 (out-of-sample) | 1,454 trades, **55.5%** win, PF 1.55 | Validated — OOS confirmed the edge is real |
| `backtest_report_PEAD_2022_2025_ENHANCED.md` | 2022–2025 (full sample) | Full enhanced stack **55.5%** win, PF 1.70 (vs BASE 54.6% / PF 1.48) | Validated — filters add value at scale |
| `backtest_report_PEAD_2026_YTD.md` | 2026 YTD (enhanced) | 30 trades, **36.7%** win, PF 1.44 | Low-confidence (tiny sample); motivated the health overlay |
| `backtest_report_PEAD_SIGNAL_HEALTH.md` | 2022–2026 | Realized-health ≥0 gate **55.5%** win, PF 1.66 (vs ungated 53.3%) | Superseded by the 200MA combo below |
| `backtest_report_PEAD_HEALTH_200MA_COMBO.md` | 2022–2026 | AND(health & SPY>200MA) **58.6%** win, PF 1.99 | **Validated — shipped**; basis for `compute_pead_health.py` |
| `backtest_report_PEAD_VARIANTS.md` | 2022–2025 / 2026 YTD | V4 bull-regime gate best (58.5% / PF 1.88 over 2022–2025) | Research — variant exploration |

Trade-level CSVs (`backtest_trades_*.csv`) and candidate caches
(`backtest_signal_health_candidates.csv`, `backtest_variants_candidates.csv`)
accompany the reports above in `reports/`.
