# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-20

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| MSFT | 11 | $421.00 | $387.32 | Q3 FY2026 beat (Apr 29): EPS $4.27 vs $4.06 est, Azure +40% YoY (above 37-39% estimate), AI ARR $37B +123% YoY, Copilot seats >20M (+250% YoY); Wedbush raised PT to $575 on May 13, 38-analyst Strong Buy consensus PT $569 (+35% upside from $417.52 close); forward P/E 22.52; next earnings July 28, 2026 (69 days). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Notes

**Macro context:** 10-yr Treasury 4.687% (highest since Jan 2025); 30-yr briefly 5.19% (19-year high). Risk-off tape — S&P 500 down 3 consecutive sessions. Brent crude $110.60. NVDA reports after close today (sector catalyst for AMD, CSCO, GOOGL sympathy). WMT/TGT report tomorrow (within 3-day window; excluded).

**Position sizing:** Equity $99,752.94; 5% cap = $4,987.65. MSFT: 11 × $421 = $4,631 (4.64%) ✓. Stop $387.32 = entry × 0.92.

**Weekly new-position cap:** GLW opened May 18 (1st) + GEV opened May 19 (2nd) + MSFT today (3rd) = **3/3 at weekly cap**. market_open MUST NOT open any additional positions this week regardless of opportunity.

**AAPL trailing-stop pre-alert:** AAPL avg_cost $283.10; midday $299.18 (+5.68%). Trailing-stop trigger fires at +10% from avg_cost = $311.41. Pre-alert threshold (+8% = $305.75) not yet reached, but market_open should have a trailing GTC order ready to submit the moment AAPL crosses $311.41 intraday (convert hard stop $260.45 to trailing 7% below peak).

**AMD trailing-stop PRE-ALERT (URGENT):** AMD avg_cost $421.59; midday $448.43 (+6.37%). Trailing-stop trigger = avg_cost × 1.10 = **$463.75**. Current price is only **$15.32 below trigger**. OpenAI 6GW MI450 commitment + Meta $60B multi-year deal announced today — AMD could gap through $463.75 at tomorrow's open. market_open MUST: (1) monitor AMD immediately at open; (2) if AMD opens or trades at/above $463.75, cancel hard stop $387.86 and place trailing_stop sell, trail_percent=7, time_in_force=gtc. Do NOT wait for midday.

**MSFT ex-dividend May 21:** MSFT goes ex-dividend tomorrow ($0.91/share, 11 shares = $10.01). Stock expected to open ~$0.91 lower at tomorrow's open (normal dividend adjustment). Stop $379.62 remains appropriate; no adjustment needed (hard stop is set vs. entry price, not adjusted for dividends in our strategy).

**AMZN stop cushion:** Current $259.88, stop $248.14 (~4.5% cushion). Risk-off macro and high yields increase the probability this is tested. Monitor closely at midday; cut if intraday unrealized falls below −5%.

**Candidates dropped this pre-market:**
- **ETN** (Eaton): Q1 beat May 5 — data center orders +240%, backlog 228 GW, guidance raised; dropped due to (a) weekly cap and (b) −4.08% on May 18 as yield headwinds pressure electrification multiples. Priority for week of May 25 if 10-yr stabilizes.
- **PWR** (Quanta Services): Q1 blowout Apr 30 — EPS beat 35%, $48.5B record backlog, guidance raised; dropped due to weekly cap. Priority for week of May 25.
- **META**: Capex raised to $125–145B, 8,000 layoffs today, Board fiduciary-duty investigation (private firm, not SEC); Q1 EPS tax-boosted; watchlist.
- **GLW**: Post-JPMorgan conference price $169–180, below May 18 exit of $179.54; JPMorgan Neutral maintained; no re-entry.
- **NVDA**: Reports after close today — within 3-day window; excluded.

**Concurrent positions after MSFT fill:** 7/8 (GOOGL, AAPL, AMD, AMZN, CSCO, GEV, MSFT). One slot remains open.

**Sector caps after MSFT fill:**
- IT: AMD ($4,649) + CSCO ($4,843) + MSFT ($4,631) = $14,123 (14.2%) ✓ < 30%
- All other sectors ≤ 9.8% ✓
