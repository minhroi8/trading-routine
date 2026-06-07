---
DRY_RUN: false
---
# Strategy
Fundamentals-based swing trading, US cash equities only, paper account only. Not a day trader. Holding period: days to weeks.
**Only the human operator edits this file.** The agent must never write to `strategy.md`.

## Capital & sizing
- Starting paper capital: **$100,000**
- Max position size at entry: **11%** of current portfolio equity
- Max concurrent positions: **8**
- Max new positions opened per week: **5** (a position opened and closed same day via midday cut still consumes a weekly slot — research, placement, and risk exposure all occurred)
- Cash floor: never deploy more than **90%** of equity (keep 10% dry powder)

## Risk controls
- **Hard stop-loss: -8% from entry.** Placed as a stop order at Alpaca immediately after fill in `market_open`.
- **Midday cut: only exit early if the hard stop (-8%) is hit OR the thesis is genuinely broken** (guidance cut, earnings miss, fraud, material negative catalyst). Do NOT cut on temporary intraday weakness alone. Backtest data shows positions held to 42 days win 65.8% of the time — patience is the edge.
- **Trailing stop on winners:** once a position is up +10%, convert the stop to a trailing stop 7% below peak for all sectors. Backtest data (2026 YTD, 7 IT trades) confirmed 7% outperforms 12% for IT sector — wider trail gives back more gains than it captures.
- **Single-sector cap:** no more than 30% of portfolio in any one GICS sector.
- **Sector deprioritization:**
  - Utilities and Real Estate picks require EPS surprise >20% to qualify — historically underperform on PEAD strategy.
  - **Industrials and Energy picks require EPS surprise >20% AND 2+ consecutive quarters of earnings beats (streak ≥2) to qualify.** 2026 YTD backtest showed Industrials at 25% win rate and -4.82% avg return — worst performing sector. Energy showed 0% win rate. Standard 15% threshold does not apply to these sectors.
  - All other sectors use the standard 15% EPS surprise threshold.
- **Macro deferral rule:** if S&P 500 futures are down >0.4% AND the 10-year Treasury yield is at a multi-month high in the same pre-market session, raise the EPS surprise threshold to >20% for that day only. Do NOT skip entries entirely — bear regime entries historically outperform bull regime entries. Only the highest-conviction setups enter on stressed macro days.
- **Regime gate (SPY 200-day MA):** At pre_market, check whether SPY is trading above or below its 200-day moving average (fetch Alpaca bars: `GET /v2/stocks/SPY/bars?timeframe=1Day&limit=200&feed=iex`). Apply the following rules:
  - **Bull regime (SPY > 200MA):** normal operation — all standard thresholds apply.
  - **Bear regime (SPY < 200MA):** reduce max new positions to **2 per week** and require EPS surprise **>20% for ALL sectors** regardless of sector-specific rules. Do not stop trading entirely — qualifying bear-regime entries historically produce strong returns when the signal clears the higher bar. Log the regime status in `plan.md` notes every day.
  - Backtest evidence: adding this gate raised win rate from 55.0%→58.5%, avg return from +1.75%→+2.20%, and profit factor from 1.62→1.88 across 2022-2025 (207 trades). Best single improvement available.

## Universe
- **S&P 1500 constituents (S&P 500 + S&P 400 + S&P 600) only.** `pre_market` pulls the current list via web_search from a reliable source (SlickCharts or Wikipedia) and caches it for the day in `research_log.md`.
- Minimum price: **$10/share**
- Minimum 20-day average dollar volume: **$20M/day**
- US primary listing only
- No recent IPOs (< 180 days since listing)
- No halted stocks or stocks under active SEC investigation

## Hard NOs (never, ever)
- No options, no shorts, no crypto, no futures
- No leveraged ETFs (3x, 2x, etc.)
- No inverse ETFs
- No OTC / pink sheets
- No trading outside regular market hours
- No overriding these rules, even temporarily, without an explicit human edit to this file

## Entry criteria (thesis required for every buy)
- Positive fundamentals signal in the last **30 days**: earnings beat, guidance raise, positive analyst revision, or clear catalyst
- **EPS surprise must exceed 15% above consensus estimate** for earnings-driven entries (20%+ for Utilities, Real Estate, Industrials, and Energy sectors). Analyst revision or partnership catalyst entries are exempt from this threshold.
- **Earnings streak preferred:** candidates with 2+ consecutive quarters of EPS beats score higher in pre_market research. First-time beats are valid but lower conviction.
- **Not within 3 days** of an upcoming earnings report (avoid event risk)
- 2–3 sentence thesis logged in `trade_log.md` **before** the order is placed

## Exit criteria (any one triggers an exit)
- Hard stop hit (-8%)
- Trailing stop triggered (7% below peak, all sectors)
- Thesis invalidated (bad earnings, guidance cut, negative catalyst)
- Held 60+ days with < 3% gain (opportunity cost — rotate capital)
