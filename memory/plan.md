# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-06

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| GOOGL | 12 | $396.00 | $364.32 | Q1 2026 blowout reported April 30: EPS $5.11 vs $2.63 est (+94%), revenue $109.9B +22% YoY; Search +19%, Cloud +63% YoY; AI ROI clearly visible; after-hours trade $394.31 on May 5 reflects continued strength; next earnings ~July 22 2026 (>3 months out). |
| AAPL | 17 | $285.00 | $262.20 | Q2 FY2026 beat reported April 30: revenue $111.2B +17% YoY, iPhone +22% (record cycle), Services ATH $31B; June-qtr guidance raised to 14-17% vs 9.5% consensus; May 5 close $284.18; next earnings July 30 2026 confirmed. Thesis intact, no new negatives. |
| AMD | 11 | $422.00 | $388.24 | Q1 2026 blowout reported May 5 after close: EPS $1.37 vs $1.28 est (+43% YoY), revenue $10.25B vs $9.89B est (+38% YoY); Data Center $5.8B +57% YoY on MI-series AI accelerator demand; Q2 guidance $11.2B vs $10.52B est — massive raise; premarket May 6 ~$418.53 (+17.8%); Morgan Stanley raised PT to $360 pre-earnings (further revision likely); next earnings ~late July 2026. Freshest catalyst available; gap-up entry risk acknowledged but fundamental re-rating is justified. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|

_No open positions — no planned sells._

## Notes

**Date**: 2026-05-06 | **DRY_RUN: false** — market_open WILL place real orders at Alpaca.

**Universe cache**: expires 2026-05-10 ✓ (502 tickers)

**Macro environment**: US-Iran ceasefire nearing — S&P 500 futures +0.83%, Nasdaq 100 +1.43%, Dow +1.01% premarket. Oil pulling back (WTI -1.5% to ~$100.73/bbl after multi-day spike). Risk-on tailwind supports growth tech names GOOGL, AAPL, AMD.

**Earnings risk tickers excluded (within 3-day window as of 2026-05-06)**:
- DIS: earnings today (May 6) — excluded
- MCD: earnings May 7 — within 3-day window, excluded

**PLTR dropped**: Q1 2026 blowout reported May 4 after close (EPS $0.33, rev +85% YoY, guidance raised to 71% growth), but stock sold off -7.1% on May 5 (close $135.99 vs prior close $146.12) and continued to $135 after hours — classic "sell the news" on valuation concerns. Market rejection signals near-term technical headwinds despite strong fundamentals. Not a clean swing entry. Noted for human review.

**AMD gap-up entry rationale**: AMD premarket +17.8% to ~$418.53 after Q1 blowout. Limit set at $422 to capture the trade without excessive overpay vs current premarket. Stop at $388.24 limits max loss to -8%. If AMD opens above $422 and keeps accelerating, market_open should reassess risk/reward before placing the order.

**SBUX noted for human — not traded**: Q2 FY2026 beat April 28 (comp +6.2%, EPS $0.50 vs $0.44 est, guidance raised to ≥5% SSS from prior 3%). Reached the 3-new-positions-per-week cap before SBUX could be considered. Universe.md has stale earnings_date_next = 2026-05-05 (actual Q2 was April 28; next Q3 est ~July 28–Aug 4, 2026). Strong candidate for next week if positions come free.

**Halt / trading-status checks (Alpaca /v2/assets)**:
- GOOGL: tradable=True, status=active ✓
- AAPL: tradable=True, status=active ✓
- AMD: tradable=True, status=active ✓

**Sanity checks**:
- Cash floor: GOOGL 12×$396=$4,752 + AAPL 17×$285=$4,845 + AMD 11×$422=$4,642 = $14,239 deployed (14.24%); cash 85.76% ≥ 10% ✓
- Max concurrent positions: 0 existing + 3 new = 3. Max 8 ✓
- Max new per week: 0 real fills in trade_log + 3 planned = 3. Cap is 3 ✓ (AT THE CAP — no more new positions this week)
- Sector cap: Communication Services (GOOGL) 4.75%; Information Technology (AAPL + AMD) 9.49%. No sector near 30% ✓
- All tickers confirmed in universe.md (502-ticker cache, screened 2026-05-03, expires 2026-05-10) ✓
