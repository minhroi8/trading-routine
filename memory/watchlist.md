---
last_updated: 2026-07-28
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
| THC | 2026-07-27 | Q2 2026 (reported Jul 23) big beat: adj EPS $6.12 vs $4.23 est = +44.7% surprise (+52% YoY); revenue $5.63B +7% YoY (beat +3.7%); adj EBITDA $1.304B +16.3% YoY; RAISED FY26 guide +$295M at midpoint (adj EPS now $20.30–21.69 vs Street ~$17.85) + share buyback; stock +17% on the print. Health Care (standard 15% EPS bar; +44.7% clears it easily). Auto-added by pre_market (compelling catalyst on non-universe ticker — Tenet is absent from the current universe.md cache). | pending_review | NOT in the current S&P 1500 universe cache (screened 2026-07-26) — human must confirm it clears strategy.md universe/liquidity/price gates before setting `active`. Strong positive PEAD reaction (gap up, +17% day-of); ambulatory-surgery (USPI) network strength drove the raise. Human-only to set status: active. |
| CLS | 2026-07-28 | Q2 2026 (reported Jul 27 AC) beat + major guidance raise: revenue $4.70B +62% YoY (Communications & Cloud Solutions segment +84%); RAISED FY2026 revenue guide to $20.5B (from $19.0B; vs $19.15B consensus) + strong 2027 outlook; stock +7% on the print. Auto-added by pre_market (compelling catalyst on non-universe ticker — Celestica is absent from the current universe.md cache). | pending_review | NOT in the current S&P 1500 universe cache (screened 2026-07-26). EPS-surprise magnitude is modest (~7.5%, 5-straight-beat streak) — the catalyst is the revenue beat + ~$1.5B revenue-guidance raise, not a >15% EPS surprise; human must confirm it clears strategy.md universe/liquidity/price + entry-threshold gates before setting `active`. IT / electronics-manufacturing (AI-server ODM) — cloud/AI-infra demand driven; rose +7% despite the memory-chip selloff. Human-only to set status: active. |
