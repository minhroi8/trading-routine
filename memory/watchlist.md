---
last_updated: 2026-07-13
note: Manually-curated tickers outside S&P 1500 approved for trading.
      Pre_market treats these identically to universe tickers.
      Added automatically when bot spots compelling catalyst on non-universe stock.
      Removed manually by human operator when thesis is dead or stock joins S&P 1500.
---

# Watchlist — Non-S&P 1500 Approved Tickers

These tickers are NOT in the S&P 1500 universe but are approved for trading
by the human operator due to strong fundamental catalysts. Pre_market may
plan buys from this list using the same entry criteria as universe tickers.

All strategy.md rules still apply: EPS surprise >15%, guidance raise,
earnings window, sector cap, position sizing, stops, etc.

| ticker | added_date | reason | status | notes |
|--------|------------|--------|--------|-------|
| MRVL | 2026-06-03 | Jensen Huang $1T endorsement at Computex; custom ASIC AI infrastructure; S&P 500 inclusion likely near-term; +46% earnings catalyst | active | Monitor for PEAD entry after dust settles post-Computex spike |
| WDFC | 2026-07-13 | Q3 FY2026 (reported Jul 9) blowout: adj EPS $2.33 vs $1.57 est = +48.4% beat (+51% YoY); net sales $195.1M +24% YoY (beat ~$25M); RAISED FY26 EPS guide to $6.05–6.35 (from $5.75–6.15); new $100M buyback. Auto-added by pre_market (compelling catalyst on non-universe ticker). | pending_review | NOT in S&P 1500 universe — WD-40 is a thinly-traded small-cap that likely fails the $20M/day dollar-volume liquidity filter; human must confirm it clears strategy.md liquidity/price gates before setting `active`. Caution: FY gross-margin outlook cut to 54.5–55.5% on specialty-chemical/base-oil input costs. Human-only to set status: active. |
