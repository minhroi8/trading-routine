# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-27

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
| _(none)_ | — | — | — | — | — |

## Notes

**Portfolio at 8/8 capacity — no new buys possible today.** All 8 theses checked overnight and intact (see research_log.md 2026-05-27 entries).

### Macro

S&P 500 futures +0.37% (~7,565); S&P 500 closed at record 7,519.12 on May 26. 10-yr yield ~4.48–4.50% (lowest in ~2 weeks, easing from 4.67% peak). Macro deferral rule NOT triggered (futures positive; yield not at multi-month high). Risk-on backdrop. PCE data due May 28 — potential volatility event.

### Portfolio status (pre-market prices, 08:15 ET)

| ticker | avg_cost | pre-mkt price | unreal % | stop | key notes |
|--------|----------|---------------|----------|------|-----------|
| AAPL | $283.10 | $308.06 | +8.82% | $260.45 (hard, 3031ee47) | **Trigger at $311.41 (+10%) — $3.35 gap**; BofA PT raised $380; WWDC Jun 8 |
| AMD | $421.59 | $514.54 | +22.05% | trailing 9e760e91 (HWM $506.96, stop $471.47) | Alpaca auto-manages; **verify HWM updated at market_open** |
| AMZN | $269.71 | $264.18 | −2.05% | $248.14 (hard, f87a7a95) | AWS thesis intact; 6.1% cushion |
| CSCO | $117.42 | $117.68 | +0.22% | $108.10 (hard, 54eb2e8d) | AI orders $9B FY2026; 8.1% cushion |
| GEV | $996.47 | $1,068.00 | +7.18% | $916.75 (hard, 68f84ddd) | **Trigger at $1,096.12 — $28.12 gap**; div ex Jun 16 |
| GOOGL | $395.72 | $386.40 | −2.36% | $364.07 (hard, d8219caa) | Cloud +63.4% YoY; 57 analysts Buy; 5.8% cushion |
| MSFT | $412.63 | $412.61 | −0.01% | $379.62 (hard, 790e2653) | Azure +40% YoY; Q4 guide $87.9B; 7.9% cushion |
| NVDA | $223.30 | $214.91 | −3.76% | $205.43 (hard, daaecbf6) | **Tightest cushion 4.4%**; smuggling watch (below) |

### Key watch items for market_open / midday

1. **AAPL trailing-stop trigger imminent**: If AAPL trades ≥ $311.41 at any point intraday, `market_open` must cancel hard stop 3031ee47 ($260.45) and place a 7% trailing stop. WWDC June 8 is the likely catalyst. Do not wait until close.

2. **AMD trailing stop HWM update**: Trailing stop (order 9e760e91, 7% trail) managed by Alpaca. Pre-market $514.54 is above prior HWM $506.96. At market_open, fetch Alpaca order status for 9e760e91 and log updated HWM + stop level in portfolio.md.

3. **GEV trailing-stop trigger approaching**: If GEV trades ≥ $1,096.12 intraday (+10% vs avg_cost $996.47), cancel hard stop 68f84ddd ($916.75) and place 7% trailing stop. Currently $28 below trigger.

4. **NVDA stop cushion watch**: 4.4% cushion from $205.43 hard stop. If NVDA unrealized intraday drops below −5%, cut per midday rule. Export-control watch: Taiwan prosecutors investigating AI chip smuggling to China via Japan (third-party allegation, not NVDA disclosure — not thesis-breaking today, but monitor for escalation).

### Sanity checks (all pass — no trades planned)

- Cash floor: $62,310.92 / $101,081.12 = 61.6% >> 10% ✓
- Concurrent positions: 8/8 (at cap — no new buys today) ✓
- New positions this week (May 25–31): 0/3 ✓
- IT sector: AAPL + AMD + CSCO + MSFT + NVDA ≈ $25,107 / $101,081 = 24.9% < 30% ✓
- No planned trades → no sector exposure changes ✓

### Watchlist (enter on first available slot)

1. **PWR** — CEO at KeyBanc Industrials conference today (May 27). Q1 2026 blowout: EPS $2.68 vs $1.98 est (+35%), record backlog $48.5B, raised FY2026 guidance, $1B buyback. Analyst PTs: UBS $900, Truist $851, JPMorgan $805. Next earnings Jul 30, 2026 (64 days). tradable=True, status=active. **Top priority entry if a slot opens.** Sizing: ~6–7 shares at ~$742 (≤5% equity = ≤$5,054), stop ≈ entry × 0.92.

2. **ETN** — Record Q1 2026 sales, data center orders +240% YoY, raised organic growth guidance. BUT UBS downgraded to Neutral citing limited near-term EPS upside. Bernstein Outperform maintained. Secondary watchlist; wait for UBS downgrade reaction to stabilize. Next earnings Aug 4, 2026.
