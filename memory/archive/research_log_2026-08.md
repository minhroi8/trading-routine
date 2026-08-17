# Research Log — 2026-08 archive

Rotated entries (older than 14 days) from `memory/research_log.md`.

| date | source | ticker | note |
|------|--------|--------|------|
| 2026-08-02 | https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv | ALL | universe_refresh S&P 1500: 286 passed, 1214 rejected; sources: Wikipedia (S&P 400) + Wikipedia (S&P 600) + GitHub CSV (S&P 500) |
| 2026-08-02 | compute_pead_health.py (yfinance, YF_DISABLE_CURL_CFFI=1 plain-requests transport) + Alpaca SPY | ALL | **✅ PEAD_HEALTH_REFRESH SUCCESS — post-condition VERIFIED (computed_on 2026-08-02 == today).** universe_refresh Sun 2026-08-02: rebuilt universe.md (286 passed / 1214 rejected; large=265, mid=21, small=0; top rejections ADV<20M 1206, price<10 46, IPO<180d 7, no_bars 3; expires 2026-08-09). compute_pead_health.py ran clean and rewrote pead_health.md: **posture NORMAL** (health_ok=true), realized_health_60d **+2.008%** (up from +1.225% Jul 19), n=269 ≥ min 20; SPY close $747.03 > 200MA $697.41 (bull, +7.1%). Fix reapplied this run (runtime env only): **YF_DISABLE_CURL_CFFI=1** so yfinance uses plain-requests transport through the agent proxy (curl_cffi still unavailable → warning benign, all yfinance paths returned data). Effect on Mon pre_market: posture NORMAL → entry bar NOT raised (standard strategy.md thresholds; no ELEVATED_BAR cap). Note: prior pead_health.md was stale since computed_on 2026-07-19 (last week's Jul-26 refresh did not land a fresh overlay); now current. |
