# backtesting/momentum/ — cross-sectional momentum research module

**Status: gated at the data-availability audit (FAIL). No backtest was run.**

This module is a **completely separate research track from PEAD**. It shares no
memory files, no live routine, and no `compute_pead_health.py` wiring. It exists to
evaluate a cross-sectional 6-1 / 12-1 momentum strategy on point-in-time S&P 500
members — *if and only if* the data supports it.

The task requires a data-availability audit to run **first** and gate everything.
That audit **failed**: point-in-time index membership (with exit dates) and
delisted-price history are not obtainable from this environment, so the primary
backtest was correctly **not run**.

## Files

| File | What it is |
|------|-----------|
| `audit_data_availability.py` | The audit. Fetches a live control ticker first, then runs the 5 point-in-time correctness checks. Uses `requests` + Yahoo chart API (yfinance's curl_cffi backend fails this env's proxy). |
| `data_cache/audit_raw_output.txt` | Full printed audit log (committed as evidence). |
| `data_cache/audit_results.json` | Machine-readable pass/fail per check. |

## The report

Full write-up (verdict, evidence, what a passing setup needs):
**`../momentum_data_audit_2026-07-08.md`**

## Re-run

```bash
pip install pandas numpy requests lxml
python3 backtesting/momentum/audit_data_availability.py
```

If a passing data source is later wired in (PIT membership + delisted prices +
rename map), the canonical run — 6-1 momentum, fixed top-10, combined
earliest-trigger exit — must be validated by daily cash/holdings reconciliation
**before** any variant matrix is produced, per the task spec.
