# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-15 (pre_market ~08:15 ET). DRY_RUN: false. SPY BULL regime. PEAD overlay STALE→NORMAL (standard 15% bar).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| GS | 9 | $1,160.00 | $1,067.20 | **Score 9.5/10.** Goldman Sachs Q2 2026 (reported Jul 14 BMO) — strongest quality of the earnings-season kickoff. **EPS surprise +45.1%** ($20.98 vs $14.46 cons; record, best qtr in GS's 157-yr history). **Revenue beat +24.0%** ($20.34B vs $16.40B). **Earnings streak: 5 consecutive quarters** beating (+1 signal pt). **Earnings-day gap +3.58%** (open $1,083.62 vs prior close $1,046.18), then ran to **+9.15% on the day** closing at a **fresh 52-wk high ($1,141.87; intraday high $1,143.79 = 0 days ago)** — textbook positive PEAD drift confirmation. **Volume 1.87x** 20-day avg (moderate-strong institutional confirmation). **RS vs SPY +9.05pp** (5-day). **Sector ETF XLF +3.92pp vs SPY (20-day)** — Financials outperforming, money rotating IN (no step-iii penalty). **Analyst conviction:** multiple PT raises — Wells/Mayo $1,195 OW, BofA $1,150 Buy, MS $1,099 EW, Evercore $1,075 OP; CNBC raised PT post-print on "blowout quarter, upbeat outlook." **Short interest** <2% float (mega-cap) — neutral. **Insider/capital return:** dividend RAISED +25% to $5.00/qtr — mgmt confidence. **Mgmt quote (Solomon):** "Momentum has accelerated throughout our businesses. Clients are turning to us to lead their most strategic and consequential transactions." Record $1T announced M&A deal volume H1'26; AUM record $4T, AWM mgmt fees +20% YoY. **Top risk:** the beat is heavily driven by record equities-trading revenue (AI-boom + SpaceX-IPO windfall) — Q3 trading normalization / sell-the-news is the primary 42-day hazard; partially offset by durable record M&A backlog + AWM fee growth. **Regulatory scan: shelf-reg CLEAN** (well-capitalized, raising dividend/buyback — no dilutive equity offering); **BIS N/A** (financial, not semiconductor). Next earnings ~mid-Oct (not within 3d). Active/tradable ✓. Sized 11% target → 9 sh × ~$1,160 = ~$10,440 = 10.6% of $98,267 equity (< 20% strategy cap). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8, 100% cash) — no positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates PASS.** Clock: next_open=2026-07-15T09:30 ET (today, Wed) — not a holiday → proceed. Reconciliation **0/0 PASS** (Alpaca /v2/positions=[] matches portfolio.md FLAT book, zero divergence). Account ACTIVE, trading_blocked=false; equity $98,266.98, cash 100%. Universe **FRESH** (expires 2026-07-19). 
- **PEAD health STALE** (pead_health.md expires_on 2026-06-28 < today) → per step 1c a stale overlay is treated **NORMAL and the bar is NOT raised** (universe-cache gate is the hard halt and it PASSES). Last reading ELEVATED_BAR (realized −0.492%, n=367, computed Jun 21). ⚠️ **PEAD_HEALTH_REFRESH_MISS continues** — Jul 12 universe_refresh rebuilt universe.md but did not recompute pead_health.md (known yfinance-vs-proxy transport bug); needs human/tooling fix.
- **SPY regime: BULL** — close $751.94 (Jul 14 IEX) > 200MA $695.34 (n=200, margin +$56.60 / +8.14%). Standard thresholds: EPS >15% (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also streak≥2), max 5 new/week.
- **Macro: risk-ON, deferral NOT triggered.** June CPI cooler than expected (−0.4% m/m, 3.5% y/y vs 3.8% est) → July Fed-hike odds fell 42%→17%; futures UP (not down >0.4%); 10-yr not at a multi-month high. Both legs of the macro-deferral rule fail.
- **Shortlist screened (Q2 season week-1, financials-heavy):** GS is the sole qualifier.
  - **GS — BUY (9.5/10):** +45.1% beat, confirmed +9.15% day-1 drift, fresh 52-wk high, 5-q streak. (Was flagged "strong WATCH, once drift establishes" by Jul 14 pre_market when it had 0 post-earnings days; the completed Jul 14 session now supplies steps e/f/i-ii.)
  - **MS — DROP (incomplete research / auto-DQ):** +17.7% beat ($3.46 vs $2.94), record rev/profit, 4-q streak — clears the 15% bar, BUT **reported this morning (Jul 15 BMO) → 0 completed post-earnings trading days** → steps e (announcement-day vol), f (5-day drift RS), i-ii (earnings-day gap) NOT computable with real data (incomplete a–i = auto-DQ, exactly the reason GS was dropped Jul 14). Premarket reaction muted (+0.97% to $230.31) and trading at the analyst PT cap ($220–230) = additional caution. **Strong WATCH** for a later pre_market once its drift establishes (in universe — no watchlist flag).
  - **BLK — DROP:** reported today (Jul 15); EPS $13.91 vs $12.70 = **+9.5% beat** — below the 15% Financials bar (record $15.3T AUM, +$192B inflows, but surprise too small). Also 0 post-earnings days.
  - **C — DROP (step f, negative drift):** +15.4% beat ($3.15, beat all 20 estimates) but the completed Jul 14 session was NEGATIVE — day −5.29%, gap −2.00%, RS −5.82pp, 52-wk high 16 days stale and falling. Sell-the-news; PEAD premise (positive drift) fails.
  - **WFC — DROP (step f, negative drift):** +16.3% beat ($2.00 vs $1.72) but Jul 14 gap −3.29%, day −2.65%, RS −2.61pp, 52-wk high 130 days stale (Jan 5). Distribution on 2.15x volume.
  - **JPM +5.0% / BAC ~+7% — DROP:** fail the 15% EPS bar outright. **IBM −20% (miss), PYPL** (Stripe/Advent $60.50 takeover offer — event-driven merger-arb, not a PEAD/fundamentals setup) — non-candidates.
- **Sanity vs strategy.md:** cash floor 89.4% cash >> 10% ✓; max concurrent 1 ≤ 8 ✓; new-per-week 1 ≤ 5 (0 buys prior this week) ✓; sector cap Financials 10.6% < 30% ✓; sizing 10.6% < 20% cap ✓.
- **Watchlist:** no new additions (all screened names are in-universe or event-driven). WDFC stays `pending_review`; MRVL stays `active`.
