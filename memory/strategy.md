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
- Max new positions opened per week: **3**
- Cash floor: never deploy more than **90%** of equity (keep 10% dry powder)

## Risk controls

- **Hard stop-loss: -8% from entry.** Placed as a stop order at Alpaca immediately after fill in `market_open`.
- **Midday cut: if an open position is down > 5% intraday unrealized, exit at the midday check** rather than waiting for the hard stop.
- **Trailing stop on winners:** once a position is up +10%, convert the stop to a trailing stop 7% below peak.
- **Single-sector cap:** no more than 30% of portfolio in any one GICS sector.

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
- **Not within 3 days** of an upcoming earnings report (avoid event risk)
- 2–3 sentence thesis logged in `trade_log.md` **before** the order is placed

## Exit criteria (any one triggers an exit)

- Hard stop hit (-8%)
- Midday threshold hit (-5% intraday)
- Trailing stop triggered
- Thesis invalidated (bad earnings, guidance cut, negative catalyst)
- Held 60+ days with < 3% gain (opportunity cost — rotate capital)
