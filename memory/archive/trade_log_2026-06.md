# Trade Log Archive — 2026-06

Entries rotated out of `memory/trade_log.md` (30-day retention) by `market_close`.

| date | time_et | ticker | side | qty | price | rationale | commit_sha |
|------|---------|--------|------|-----|-------|-----------|------------|
| 2026-06-01 | 13:49 ET | AMD | sell | 11 | $490.44 | Trailing stop 9e760e91 fired. HWM $527.20, stop triggered at $490.30 (fill $490.44 avg). BIS export control guidance (Jun 1) closed third-country loophole for MI350x to Chinese-controlled subsidiaries (Singapore/Malaysia); AMD price declined throughout session on the overhang. Core US demand thesis (OpenAI 6GW + Meta $60B multi-year) intact at exit. Realized P&L: +$757.31 (+16.33% vs avg_cost $421.59). Holding period: 26 days (2026-05-06 to 2026-06-01). PWR contingency NOT triggered (stop fired 13:49 ET, not at open; midday routine did not run). | bdd0130 |
| 2026-06-01 | 09:38 ET | MSFT | stop-convert | 11 | — | Trailing stop conversion per plan.md. +10% trigger $453.89 crossed (pre-market $467.00, open ~$463.39, +12.30% vs avg_cost $412.63). Cancelled hard stop 790e2653 ($379.62). Placed trailing stop order d1228e16 (7% trail_percent, GTC); HWM $462.20, initial stop $429.85 as of placement. Microsoft Build conference June 2-3 ahead; trailing stop locks in gain. AMD stop NOT fired ($495.63 > $490.30 — PWR contingency NOT triggered). | a1d0434 |
