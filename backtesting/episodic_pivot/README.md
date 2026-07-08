# backtesting/episodic_pivot/ — earnings-gap continuation research module

**Research only. Separate from PEAD and from the live 7-routine system.** Nothing here
trades, edits memory files, or ships to production.

**Verdict: do NOT promote.** On the same survivorship-biased dataset as PEAD, the
specified episodic-pivot setup is (1) too rare to evaluate out-of-sample (6 OOS trades;
no grid cell reaches 40), (2) single-trade fragile (top trade = 79% of OOS profit),
(3) shows no selection skill over a random same-sector control, and (4) is a concurrent
**sub-set of PEAD** (100% event overlap, 93% concurrent holding) — not a diversifier.

Full write-up: **`../episodic_pivot_backtest_2026-07-08.md`**

## Files

| File | Purpose |
|---|---|
| `ep_engine.py` | Library: price fetch (requests + Yahoo chart API, cached), event loader (PEAD base artifacts), signal features, parametric exit sim, reconciled daily portfolio sim, metrics. |
| `run_fetch.py` | Cache all event-ticker prices + SPY/QQQ; writes `reports/coverage.json`. |
| `run_canonical.py` | Canonical run + **validation** (daily & aggregate reconciliation + manual trade re-derivation). Gate before the grid. |
| `diag_funnel.py` | Per-filter pass-rate funnel (confirms rarity is real, not a bug). |
| `run_full.py` | 54-cell grid, isolated exits, comparisons (SPY / PEAD-from-artifacts / simple-gap / random control), PEAD overlap. |
| `reports/` | Committed CSV/JSON artifacts (grid, comparisons, overlap, canonical trades/equity). |
| `data_cache/` | Gitignored per-ticker price pkls (`*.pkl`), rebuilt on demand. |

## Data note

Catalyst = committed PEAD base trade CSVs (same universe as PEAD). Prices = Yahoo chart
API via `requests` (yfinance's curl_cffi backend fails this env's proxy). OOS is 2025
only: 2026 H1 base earnings **announcement dates** are not available in the artifacts,
and the live `earningsHistory` endpoint returns fiscal-period-end dates (off by weeks),
so 2026 is a documented coverage gap rather than fabricated. Inherits PEAD's
survivorship limitation (see `../momentum_data_audit_2026-07-08.md`).

## Re-run

```bash
pip install pandas numpy requests
python3 backtesting/episodic_pivot/run_fetch.py
python3 backtesting/episodic_pivot/run_canonical.py
python3 backtesting/episodic_pivot/run_full.py
```
