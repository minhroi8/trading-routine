# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-26

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| AMD | d5c0c6ab | $387.86 | Cancel hard stop → place trailing stop at 7% below peak | ~$448.95 (use actual intraday peak at time of placement) | +14.50% vs avg_cost $421.59; trigger crossed (+10% = $463.75); all-time high $481.41 on May 22, pre-mkt $482.74 |
| AAPL | 3031ee47 | $260.45 | IF opens ≥ $311.41: cancel hard stop → place trailing stop at 7% below peak | ~$289–291 (use actual intraday peak at time of placement) | +9.82% vs avg_cost $283.10; trigger $311.41 ($0.51 above pre-mkt $310.90); WWDC June 8 catalyst intact |

## Notes

**No new buys — portfolio at maximum concurrent capacity (8/8 per strategy.md ≤ 8). All candidates below were shortlisted and passed earnings/halt checks but trimmed at sanity check due to capacity.**

### Shortlisted watchlist (deferred — not executable today)

| ticker | catalyst | next_earnings | limit_price_est | stop_price_est | trim_reason |
|--------|---------|--------------|-----------------|----------------|-------------|
| PWR | Q1 2026 blowout: EPS $2.68 vs $1.98 est (+35% beat), revenue $7.9B, record backlog $48.5B; $1B buyback authorized May 20; analyst PTs UBS $900, JPMorgan $805, Evercore $800, Truist $851 | Jul 30, 2026 (65d — clear) | ~$730–740 | ~$671–681 (−8%) | 8/8 concurrent cap |
| ETN | Q1 2026 beat: record sales $7.45B, data center orders +240% YoY, FY2026 guidance raised; NVIDIA "grid-to-chip" platform; avg PT $450.60 | Aug 4, 2026 (70d — clear) | ~$390–395 | ~$359–364 (−8%) | 8/8 concurrent cap; monitor Warsh/yield headwind |

### Macro flags for today

- **Kevin Warsh as Fed Chair (HIGH):** Hawkish posture, no rate cuts signaled; some FOMC members floating rate hike possibility. June 16–17 is first FOMC under Warsh. Watch for any public remarks today.
- **PCE data Wednesday May 28 (HIGH):** Hot print reinforces hawkish Fed; could hit high-multiple growth names broadly.
- **10-yr yield 4.67%, 30-yr near 19-year high (MEDIUM-HIGH):** Iran + Warsh inflation dynamics. Headwind for high-multiple names (AMD ~59x fwd P/E, GEV).
- **S&P 500 futures +0.54% pre-market (POSITIVE):** Iran talks progressing. Risk-on open expected.
- **AMD trailing stop (IMMEDIATE):** Must convert at market_open. Cancel stop order d5c0c6ab ($387.86). Place trailing stop at 7% below AMD's intraday high at time of placement (~$448.95 if peak = $482.74).
- **AAPL trailing stop (CONDITIONAL):** If AAPL opens ≥ $311.41, cancel stop order 3031ee47 ($260.45) and place trailing stop at 7% below peak. WWDC June 8 — thesis intact, do not sell.
- **NVDA post-earnings drift (MEDIUM):** Sell-the-news pattern may continue. Stop $205.43 active. Watch $215–220 support range.

### Thesis checks — all 8 positions

| ticker | pre_mkt_px | vs_avg_cost | stop | trailing_trigger | status |
|--------|-----------|------------|------|-----------------|--------|
| AAPL | $310.90 | +9.82% | $260.45 | $311.41 (IMMINENT) | Intact — WWDC June 8 catalyst |
| AMD | $482.74 | +14.50% | $387.86→trailing | $463.75 (TRIGGERED) | Intact + reinforced — trailing stop conversion required |
| AMZN | $267.38 | −0.87% | $248.14 | — | Intact — AWS +28% YoY, $364B backlog |
| CSCO | $121.20 | +3.21% | $108.10 | — | Intact — AI orders $9B FY2026 target |
| GEV | $1,052.00 | +5.57% | $916.75 | $1,096.12 | Intact — new nuclear+gas deal, India hydropower |
| GOOGL | $383.60 | −3.06% | $364.07 | — | Intact — AI pricing war, antitrust overhang known |
| MSFT | $418.90 | +1.52% | $379.62 | — | Intact — Azure +40%, AI ARR $37B, backlog $392B |
| NVDA | $218.10 | −2.33% | $205.43 | — | Intact — sell-the-news expected, PT $295.34 avg |

**DRY_RUN: false**
