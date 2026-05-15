# Lessons

Written only by `weekly_review`. Each weekly entry records what worked, what didn't, performance vs SPY, and any proposed rule changes.

Proposed rule changes are suggestions only — the human operator applies them by editing `strategy.md` directly. The agent never edits `strategy.md`.

## 2026-05-07 — Expanded universe to S&P 1500

Reasoning: Felt the S&P 500 universe was missing legitimate momentum names (e.g., RKLB).
Tested research: bot's strategy logic (post-earnings momentum) still applies to mid/small caps.
Risk: mid-caps gap harder, less analyst coverage. ADV filter ($20M) provides some guardrail.
Review date: 2026-06-07 — evaluate whether new picks from S&P 400/600 outperformed or hurt.

---

## Week of 2026-05-11

- Perf: portfolio -0.31% vs SPY +0.36% (delta -0.67 pts)
- Trades: 2 fills (AMZN 18@$269.71 and CSCO 42@$117.42, both buys on May 14); 0 closed trades; win rate N/A
- Avg win: N/A | Avg loss: N/A (no closed trades this week)
- Best (open, unrealized vs cost): AAPL +5.94% ($299.91 close vs $283.10 avg_cost) — Q2 FY2026 beat thesis intact; iPhone +22%, Services ATH $31B, new CEO Ternus execution focus. Approaching +10% trailing stop trigger ($311.41). CSCO +0.42% on only day-2 — Q3 FY2026 blowout entry well-timed.
- Worst (open, unrealized vs cost): AMZN -2.28% ($263.57 close vs $269.71 avg_cost) — entered May 14; layoff news in Selling Partner Services deemed non-material to AWS/AI thesis (+28% YoY, $225B chip commitment); stop $248.14 active with ~5.7% cushion.
- What worked:
  - Portfolio outperformed SPY on the volatile Friday session (+0.85% relative alpha vs SPY -1.07% day)
  - AAPL continuing strong post-earnings momentum toward trailing stop trigger; +5.94% unrealized in ~9 days
  - CSCO and AMZN added cleanly within all sizing and sector constraints; CSCO immediately positive
  - Correctly excluded NVDA (earnings May 20, within 6-day window), QCOM (technical breakdown -11%), PLTR (sell-the-news pattern): discipline held
  - Sector concentration remained low: IT 14.8%, Comm Services 4.8%, Consumer Discretionary 4.8%; no sector > 30%
- What didn't:
  - Portfolio underperformed SPY for the week (-0.31% vs +0.36%, delta -0.67 pts); only ~24% capital deployed limits absolute return capture
  - Pre_market and market_open routines did not run May 11-12; market_open/midday also absent May 13 — 3 days of reduced monitoring. Positions and stops held fine, but any intraday breach would have gone undetected at the midday check
  - CSCO hard stop was placed 1 day late: filled May 14 but stop order 54eb2e8d not confirmed in Alpaca until May 15 market_open. Strategy.md requires immediate placement after fill
  - AMD closed -4.64% intraday on May 15 (threshold: -5% midday cut); midday check at 12:05 showed only -3.74% so rule did not trigger — but AMD came within 36 bps of the cut threshold at EOD
  - AMZN opened red from the first day; early execution risk when entering on the day of a post-earnings gap-up catalyst
- Rule adherence: one breach — CSCO stop placed 1 day late (plan.md had $108.10 stop; market_open May 14 could not place it because the CSCO fill was still pending confirmation; stop placed at market_open May 15). All other rules clean: sizing ≤5% ✓, cash floor 75.8% >> 10% ✓, sector caps all < 30% ✓, new positions 2/3 this week ✓, max concurrent 5/8 ✓, no orders outside market hours ✓, DRY_RUN: false maintained correctly ✓
- Proposed rule changes (for human review, not applied automatically):
  - Add "orphan stop queue" to market_open: at the start of every run, before any other logic, scan portfolio.md for positions missing a stop_order_id and place those stops first. This resolves the late-day-fill gap where a fill is confirmed after the normal stop-placement window.
  - Add trailing-stop pre-alert to pre_market: once any position crosses +8% unrealized, flag in plan.md notes that the +10% trailing stop trigger is imminent and the next market_open should have the trailing order ready to submit immediately.
  - Investigate why pre_market/market_open/midday did not run May 11-12 and market_open/midday did not run May 13. If routines are cron-triggered, verify the scheduling mechanism has not drifted or missed wake-up events.
