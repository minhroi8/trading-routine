# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-04

## Planned buys

_(none — no candidates scored ≥6/10; see Notes)_

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| CSCO | 54eb2e8d | $108.10 | Convert to 7% trailing stop GTC if CSCO trades at or above $129.16 | Cancel 54eb2e8d; place trailing_stop 42@7% trail_percent GTC | CSCO pre-market $127.969 (+8.99% vs cost); trigger $129.16 = $1.19/0.93% above pre-market price. Monitor from open; convert immediately when crossed. |

## Notes

---

### AVGO — EPS gate failed → Discord flag, no entry; monitor June 8

AVGO Q2 FY2026 reported after close June 3:
- **Non-GAAP EPS: $2.44** vs $2.40 est = **+1.7% beat** → FAR below +15% threshold requiring **$2.76** → **GATE FAILS**
- AI semiconductor revenue: **$10.8B** (+143% YoY) ✓ (exceeds $10.7B gate)
- Q3 FY2026 guide: **$29.4B** (+84% YoY) — extraordinary; far exceeds $23.0B gate criterion
- No NEW hyperscaler ASIC partnerships disclosed (Google/Anthropic/OpenAI/Meta all pre-existing)
- Per plan.md rules: EPS $2.44 is in the "$2.44–$2.75 modest beat" range but **no new hyperscaler ASIC partnership disclosed** → per plan.md branch: **no auto-entry; Discord flag posted** for human confirmation
- Stock: −14% AH, ~$413 pre-market (low ~$405.51, high ~$496.02 intraday June 4)
- Hock Tan verbatim: *"Bookings for AI semiconductors were over $30 billion against the $10.8 billion we shipped."* *"Our visibility runs all the way to 2028 right now."*
- FY2027 AI revenue guide: "more than $100 billion" — extraordinary forward-looking signal
- **If human confirms entry**: re-evaluate June 8 (3 weekly slots reset); limit price ~$420 area (stock more attractive than original $535 plan); stop = fill × 0.92
- Next earnings: Q3 FY2026 ~September 2026 ✓ (>3 days)
- Alpaca: tradable=True, status=active ✓

---

### CRWD — EPS gate failed → DISQUALIFIED

CrowdStrike Q1 FY2027 reported after close June 3:
- EPS: **$1.10** vs $1.07 est = **+2.8% beat** → below +15% threshold requiring **$1.23** → **GATE FAILS**
- Net New ARR: $256M (+32% YoY) ✓; Revenue $1.39B (+26% YoY) ✓
- Stock: −9 to −11% AH on billings miss; +60% YTD pre-earnings (extreme sell-the-news)
- 4-for-1 stock split announced (July 2026)
- **DISQUALIFIED** (EPS 2.8% vs 15% required; stock falling materially)
- Monitor for June 8 pre_market if stock stabilizes; note IT sector cap concerns if AVGO also considered

---

### CIEN — Deep research score 5/10 → DISQUALIFIED (dropped at step g)

Ciena Q2 2026 reported before open June 4 (universe member, last screened $582.13 May 31):

**Steps a–g completed:**

**(a) Earnings data:** EPS **$1.64** vs $1.45 est = **+13.1% beat** (below 15% earnings-entry threshold); revenue $1.57B vs $1.50B (+4.7%, +40% YoY); FY2026 guide raised to $6.3B ±$100M (+32% YoY at midpoint); Q3 guide $1.625B ±$50M.

**(b) Earnings call tone:** CEO Gary Smith: *"Our long-term strategy to be the global leader in high-speed connectivity—both across the WAN and in and around the data center—is tightly aligned to the structural, multi-year opportunities created by AI-driven demand."* Also: "disciplined execution in a dynamic supply environment." Bullish but somewhat cautious undertone.

**(c) Analyst reactions:** Pre-earnings: Citi PT $658 (May 18, +91% raise), TD Cowen PT $675 (May 26, +59% raise), BofA PT $660 (May 26), Stifel PT $585 (May 5). BUT **Morgan Stanley maintains PT $405** — 33% below current ~$620. B. Riley: Neutral, PT $531. 14 analysts Buy consensus.

**(d) 52-week high recency:** $637.51 on **June 3** (1 day ago — TOP PRIORITY) ✓

**(e) Volume confirmation:** Data unavailable — Alpaca bars returned null for CIEN. Cannot calculate earnings-day volume ratio. Unconfirmed → partial deduction.

**(f) Relative strength vs SPY:** CIEN +53% last month vs SPY flat-to-slightly-up → massively positive RS ✓

**(g) Risk check — DROPPED HERE:** P/E **399x vs 5-year median 40x (884% above historical)**; GuruFocus "significantly overvalued"; Morgan Stanley PT $405 = 33% below current ~$620; insider selling $27.2M last 3 months; GF Value implies extreme overvaluation. Morgan Stanley's credible $405 target constitutes a risk that **could plausibly break the thesis within 42 days** (any sector rotation, macro headwind, or guidance miss could trigger -20% to -33% reversion). **DROPPED under step (g).**

**Score: 2 (signal) + 3 (momentum) + 1 (confirmation) + 0 (risk) = 5/10 → DISQUALIFIED (need ≥6/10)**

Alpaca: tradable=True, status=active ✓. Next earnings Q3 FY2026 ~Sep 2026 ✓. EPS +13.1% below 15% threshold for earnings-driven entry; analyst revision exemption argument noted but overridden by step (g) drop.

---

### ORCL — No qualifying catalyst → NOT shortlisted

Oracle Q4 FY2026 reports June 10 after close (6 calendar days away; outside 3-day window on June 4). Last earnings was Q3 FY2026 in March 2026 (>30 days ago) — no qualifying fundamental signal within 30-day window. No analyst revision within 30 days identified. NOT shortlisted.

---

### MRVL (watchlist, status: active) — carried forward

Score 4/10 from June 3 deep research (EPS +6.67% below 15% threshold; volume 1.40x below 1.5x threshold; GF Value $106 vs current ~$301). No change to June 3 conclusion. Monitor; re-evaluate June 8 pre_market.

---

### Portfolio sanity check — June 4

- Equity: **$99,483.65** | Cash: **$69,776.55 (70.1%)** > 10% floor ✓
- Concurrent: **5/8** ✓ | Weekly slots: **2/3** (HPE+PWR June 2) → 1 remaining ✓ (no qualified candidates today)
- IT: AAPL+CSCO+NVDA ≈ **15.5%** ✓ | Industrials: GEV+PWR ≈ **14.4%** ✓
- All sector caps well under 30% ✓
- DRY_RUN: false

---

### Macro context — June 4

- S&P 500 futures: slightly softer pre-market (prediction markets 86% probability of opening down)
- 10-yr yield: ~4.48% (NOT multi-month high; peak 4.70% May 20) → macro deferral rule **NOT triggered**
- Economic data today: Q1 nonfarm productivity, Challenger May job cuts
- Upcoming: **NFP June 6** (nonfarm payrolls — potential volatility), **FOMC Warsh June 6–7** (no rate cut expected)

---

### Portfolio stop watch — critical market_open actions

1. **CSCO trailing trigger**: $127.969 pre-market vs trigger $129.16 (0.93% away). If CSCO ≥ $129.16 at any point today: cancel stop 54eb2e8d, place 7% trail_percent GTC trailing stop on 42 shares; log new order ID, initial HWM and stop price.
2. **NVDA ex-div June 4**: $0.25 × 22 shares = **$5.50 cash credit** (Alpaca-managed; verify credit in account balance at market_open).
3. **GEV stop proximity**: $949.00 current vs $916.75 stop = 3.40% cushion — WATCH. Ex-div June 16 ($0.50 × 4 = $2.00) approaching.
4. **NVDA stop proximity**: $212.63 current vs $205.43 stop = 3.39% cushion — WATCH.
5. **AAPL WWDC June 8–12**: Key trailing stop management decision ahead — rebuilt Siri/Gemini AI platform could push stock to $365-$385 analyst targets (BofA $380, Morgan Stanley).
6. **AVGO**: No entry today. Discord flag posted. Hock Tan quote logged.
