# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-25 (pre_market ~08:05 ET). DRY_RUN: false. Book FLAT at open (0/8, 100% cash, equity $99,074.58). Regime BULL (SPY $733.32 > 200MA $689.69, +$43.63). PEAD posture ELEVATED_BAR (realized −0.492%, n=367, fresh/expires Jun 28) → >20% EPS all sectors, max 2 new positions/week. Weekly slots 0/2 used.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| MU | 8 | $1,250.00 | $1,150.00 | **Score 8/10.** Micron Q3 FY2026 (reported Jun 24 after close): **adj EPS $25.11 vs ~$20.78 consensus = +20.8% beat** (clears ELEVATED_BAR >20% all-sectors bar; some feeds est $20.20 → +24.3%); **revenue $41.46B vs $35.84B = +15.7% beat** (+346% YoY, +74% QoQ); **record gross margin 84.9%**; data center revenue 7x YoY to $11.5B. **Q4 FY2026 guide RAISED hard: revenue $50B ±$1B (vs ~$43.6B est), GM ~86%, diluted EPS $31 ±$1, capex ~$10B.** Structural de-risk: **16 strategic customer agreements ≈ $100B minimum contracted revenue** (cal 2026–2030), covering ~20% DRAM / ~33% NAND volume, with **floor pricing** protecting margins above prior-cycle peaks — directly blunts the cyclical/oversupply bear case. HBM4 12-high ramping "twice as fast as HBM3E," >$1B HBM4 already shipped. **Momentum:** 52-wk high $1,213.07 on Jun 22 = **2 trading days ago** (top recency); RS5 **+5.0%** (MU +2.71% vs SPY −2.30%); **premarket +17.1%** ($1,227 vs $1,047.92 prior close). **Confirmation:** ~12+ post-print PT raises Jun 24–25 (BofA $1,500, JPMorgan $1,540, UBS $1,625, Needham $1,550–1,650, Stifel/TD Cowen/Raymond James $1,500, Morgan Stanley raised, Wedbush/Bernstein $1,300, Citi $1,200, Wolfe $1,250), **0 downgrades**; current ~$1,227 trades BELOW the analyst PT cluster (room to consensus — the opposite of MRVL's PT overshoot). Pre-reaction vol 1.2x 20d (IEX, partial feed; reaction-day volume will be large). Mgmt: CEO called the quarter "exceptional"; CFO cited "higher visibility and improved stability." **Top risk:** buying a +17% gap into a fresh ATH on a name swinging ±13%/day this week ($1,211→$1,051→$1,047→$1,227) — a fixed −8% stop ($1,150) sits inside the recent daily range, so noise-stopout / sell-the-news pullback is the real near-term hazard; Goldman Sachs is the lone bear (Neutral, $900 = ~27% below premarket). Next earnings ~Sep 22–29 (not within 3 days); MU active/tradable (NASDAQ). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT — no open positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates PASS:** clock `next_open=2026-06-25T09:30 ET` (today, Thu — not a holiday); reconciliation **0/0 PASS** (Alpaca /v2/positions=[] matches FLAT book); universe cache fresh (expires 2026-06-28); account ACTIVE, trading_blocked=false. DRY_RUN: false.
- **Posture ELEVATED_BAR** (>20% EPS all sectors, max 2 new/week) + **BULL regime** (SPY $733.32 > 200MA $689.69). Macro: S&P futures +0.7% / Nasdaq futures +2.1% (Micron-led AI rally; chip names SNDK/WDC/LRCX/KLAC/AMAT up in sympathy); 10-yr yield NOT at a multi-month high and **futures are UP** → macro deferral rule NOT triggered. PCE inflation print due today.
- **MU is the single qualifier** — the first fresh in-window >20% EPS beat in weeks (Q1/Q2 earnings desert; Q2 season starts mid-July). Other chip names rising are sympathy moves with no fresh earnings catalyst of their own → not eligible (entry requires the ticker's own positive fundamentals signal in last 30 days).
- **MRVL** (watchlist `active` + in universe): no fresh catalyst today; Q1 FY2027 EPS +1.3% fails the bar; still chops ±10%/day. No change — stays `active`, not planned.
- **Sizing/limit discipline:** 11% of equity = $10,898; at limit $1,250 → **8 shares = $10,000 ≈ 10.1%** (< 11% cap; 9 sh would be 11.4% → over). Limit $1,250 caps the chase to ~+1.8% above the $1,227 premarket print. **market_open:** do NOT fill above the $1,250 limit (don't chase a runaway open); set the actual hard stop at **fill × 0.92** immediately after fill (GTC). If MU gaps far above $1,250 at the open, skip rather than chase.
- **Sanity checks:** cash floor after buy ~89.9% >> 10% ✓; max concurrent 1/8 ✓; new-per-week 1/2 (ELEVATED_BAR cap) ✓; sector IT one position ~10% << 30% cap ✓.
- No non-universe catalyst warranting a watchlist `pending_review` add today.
