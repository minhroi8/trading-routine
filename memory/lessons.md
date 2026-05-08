# Lessons

Written only by `weekly_review`. Each weekly entry records what worked, what didn't, performance vs SPY, and any proposed rule changes.

Proposed rule changes are suggestions only — the human operator applies them by editing `strategy.md` directly. The agent never edits `strategy.md`.

## 2026-05-07 — Expanded universe to S&P 1500

Reasoning: Felt the S&P 500 universe was missing legitimate momentum names (e.g., RKLB).
Tested research: bot's strategy logic (post-earnings momentum) still applies to mid/small caps.
Risk: mid-caps gap harder, less analyst coverage. ADV filter ($20M) provides some guardrail.
Review date: 2026-06-07 — evaluate whether new picks from S&P 400/600 outperformed or hurt.

---

## Week of 2026-05-04

- Perf: portfolio +0.59% vs SPY +2.35% (delta -1.76 pts)
- Trades: 3 total, 0 wins / 0 losses (win rate N/A — no closed trades; all 3 positions still open)
- Avg win: N/A | Avg loss: N/A
- Best: AMD +7.97% unrealized — Q1 2026 blowout (EPS +43% YoY, Data Center +57%, Q2 guide beat) + Meta 6GW GPU deployment news; Morgan Stanley PT raise mid-week reinforced thesis
- Worst: GOOGL +1.06% unrealized — thesis intact, slowest mover of the three; UK ad-tech lawsuit and DOJ antitrust appeal are ongoing overhangs with no new escalation
- What worked:
  - Post-earnings momentum entry strategy fired immediately: all 3 positions profitable within days of entry
  - Waited for DRY_RUN: false confirmation before trading (May 4–5 cash) — prevented unauthorized live orders
  - 3-new-positions/week cap enforced cleanly; correctly blocked MSFT, SBUX, PLTR, and other candidates that had marginal theses or valuation concerns
  - Risk controls held: no position exceeded 5% of equity at entry; cash floor stayed at 85%+; no sector cap breach (IT at 14.7%)
  - AMD: "sell the news" on PLTR ($135.99, -7.1% post-earnings) was flagged and correctly avoided; AMD substituted and immediately outperformed
  - Thesis audit at midday on May 6, 7, 8 caught nothing material — all exit criteria remained unmet
- What didn't:
  - All 3 positions in the same sector (Information Technology / GICS). The 30% sector cap was never approached, but correlated drawdown risk is elevated. On May 7 all three fell together (-0.17% portfolio vs -0.34% SPY still an outperform, but the correlation was clear).
  - Positions opened mid-week (Wednesday May 6), so the portfolio missed the market's Monday–Tuesday gains (+0.99% SPY May 5 alone). The 3/week cap and DRY_RUN gate contributed to this — both are correct guardrails, but the timing cost was real.
  - AAPL gross-margin risk flagged (Tim Cook's "significantly higher memory costs" comment) but not fully quantified. Watch Q3 FY2026 guidance closely.
  - NFP print outcome not logged — research_log noted elevated volatility expected May 8 8:30 AM but no post-NFP note. Fill the gap next week.
- Rule adherence: CLEAN — no breaches detected
  - Sizing: GOOGL 4.75%, AAPL 4.81%, AMD 4.64% — all < 5% cap ✓
  - Cash floor: 85.8% cash ✓ (well above 10% minimum)
  - Sector cap: IT at 14.7% of equity ✓ (< 30%)
  - New positions: 3/3 cap exactly met ✓
  - No orders outside 09:30–16:00 ET ✓
  - DRY_RUN: false — live orders confirmed ✓
- Proposed rule changes (for human review, not applied automatically):
  - Consider adding an intra-sector diversification soft guideline: e.g., "prefer no more than 2 positions in the same GICS sector simultaneously unless conviction is highest tier." This week GOOGL + AAPL + AMD are all IT; correlated risk is real even though sector cap is 14.7%.
  - Consider logging NFP / major macro report outcomes in research_log the same day — this week's pre-NFP note existed but the result was never recorded.
  - Next-week priority queue: AMZN (highest conviction — Q1 blowout EPS +70%, AWS +28%), QCOM (strong — beat + $20B buyback + auto revenue record), MCD (lower conviction — SSS deceleration guidance offsets beat).

---
