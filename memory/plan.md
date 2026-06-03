# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-04

⚠️ **Override note:** This plan was written at ~15:45 ET on June 3, 2026 under human-operator override of the market-gate check. AVGO/CRWD earnings were not yet released at time of writing — entry criteria are conditional and must be verified by market_open June 4 once results are known.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| AVGO | 22 | $535 | entry × 0.92 | CONDITIONAL — execute only if ALL gate criteria in Notes are satisfied at market_open June 4. Score 7–8/10 IF criteria met. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| CSCO | 54eb2e8d | $108.10 | Convert to 7% trailing stop GTC if CSCO trades at or above $129.16 | Cancel 54eb2e8d; place trailing_stop 42@7% trail_percent GTC | CSCO closed $127.27 (+8.39%); trigger $129.16 = 1.49% above close. Monitor intraday; convert immediately when crossed. |

## Notes

---

### AVGO — Conditional buy (binary gate; verify at market_open June 4)

**Background:** AVGO (Broadcom) Q2 FY2026 reports after close June 3. Universe-listed (large cap). 44/47 analysts Buy, consensus PT ~$480–$487. Q2 estimates: EPS $2.40, revenue $22.04–$22.12B, AI chip revenue ~$10.7B (+140% YoY). Current price ~$481–$497 (as of June 3 intraday).

**Pre-earnings score estimate (IF criteria met): 7–8/10**
- Signal quality (EPS ≥$2.76 + AI rev ≥$10.7B): 3/3 pts
- Momentum (52-week high within 1–2 days; new ATH territory): 3/3 pts
- Confirmation (44/47 analysts Buy; volume at open TBD): 1–2/2 pts
- Risk (options ±10.65% implied move; historical avg beat ~1.93%; "priced for perfection"): 1/2 pts

**Binary gate — market_open June 4 must verify ALL before placing order:**
1. **EPS ≥ $2.76:** Non-GAAP EPS +15% above $2.40 consensus (strategy.md earnings-entry threshold). If EPS $2.44–$2.75 (modest beat) but call discloses a NEW hyperscaler ASIC partnership contract not previously disclosed: post Discord flag for human confirmation, do NOT auto-execute.
2. **AI revenue ≥ $10.7B:** Confirms 140% YoY growth thesis.
3. **Q3 FY2026 guide ≥ $23.0B:** Acceleration from $22B Q2 run-rate.
4. **Stock opens ≤ $535:** Do NOT chase if euphoric gap pushes above $535.
5. **Next earnings ≥ 3 days away:** Confirm Q3 FY2026 ~September 2026 (expected ✓).
6. **Alpaca tradable=True, status=active:** Verify /v2/assets/AVGO.

**If ALL criteria met — execute:**
- Limit buy 22 shares AVGO @ $535
- Stop: fill × 0.92 (−8% hard stop), GTC
- Sector: IT. Post-buy IT: AAPL+CSCO+NVDA+AVGO ≈ 26.3% of equity (< 30% ✓)
- Uses the final weekly slot (3/3; week resets June 8)
- Include full thesis in trade_log.md: score, EPS actual, AI rev actual, volume ratio at open, management verbatim quote, risk flagged

**If criteria NOT met:** No buys for June 4. Post Discord note. Monitor AVGO for June 8 pre_market (3 weekly slots reset).

---

### CRWD — DROPPED

Reports tonight June 3. **Two independent disqualifiers:**
1. **IT sector cap:** AAPL+CSCO+NVDA+AVGO = 26.3%; adding CRWD = 37.3%+ → exceeds 30% cap.
2. **Extreme sell-the-news risk:** +72% pre-earnings in 30 days; DZ Bank Strong Sell; options 7–10% implied move.
If AVGO does NOT qualify and CRWD beats EPS ≥ $1.23 (+15% above $1.07) with Net New ARR ≥ $250M AND stock holds after-hours: flag for June 8 pre_market, do NOT enter June 4.

---

### CRM (Salesforce) — DROPPED

Already reported May 27 (prior plan.md error said tonight). EPS $3.88 vs $3.12 (+24% beat) but guidance disappointed; stock fell −4.5%. Negative 5-day RS vs SPY → disqualified per routine step f.

---

### MRVL (watchlist, status: active) — DROPPED, score 4/10

Deep research steps a–g completed:
- (a) May 27 EPS: $0.80 vs $0.75 est = **+6.67% — below 15% threshold**
- (b) Call tone: "unprecedented visibility" — bullish, but no new contract
- (c) Analysts: 44 Buy, mean PT $233 vs current $301 — all targets exceeded
- (d) 52-week high: within 1 day (top priority) ✓
- (e) Volume June 2: 59.4M vs 20-day avg 42.51M = **1.40x — below 1.5x weak threshold** ✗
- (f) RS vs SPY: massively positive ✓
- (g) Risk: GF Value $106.26 fair value vs $301 current; reversal risk after +50% in 2 days ✗
- **Score: 4/10 — DISQUALIFIED (need ≥6)**

---

### CSCO trailing stop — monitor at market_open

CSCO closed $127.27 (+8.39%; trigger $129.16 = 1.49% away). At market_open June 4:
1. Check CSCO opening price
2. If CSCO ≥ $129.16 at any point: cancel stop 54eb2e8d, place 7% trail_percent GTC trailing stop; log order ID and initial HWM/stop
3. If below: monitor intraday

---

### NVDA ex-dividend June 4

$0.25/share × 22 shares = **$5.50 cash credit** (Alpaca-managed, no action needed). NVDA closed $216.30 (−3.40% unrealized), stop $205.43 = 4.77% cushion — **monitor at market_open.**

---

### Portfolio sanity check — June 4 (using market_close June 3 data)

- Equity: **$99,788.72** | Cash: **$69,776.57 (69.9%)** > 10% floor ✓
- Concurrent: **5/8** ✓ | Weekly slots: **2/3** (HPE+PWR June 2) → 1 remaining ✓
- IT: AAPL+CSCO+NVDA = **~15.5%** ✓ | Industrials: GEV+PWR = **~14.7%** ✓
- If AVGO added: IT ≈ **26.3%** ✓ | concurrent 6/8 ✓ | weekly 3/3 ✓
- DRY_RUN: false

---

### Upcoming catalysts

- **AAPL WWDC June 8–12** (rebuilt Siri / AI platform — key trailing stop management decision)
- **NVDA ex-div June 4** ($5.50 credit, Alpaca-managed)
- **CSCO trailing stop** — monitor; trigger $129.16 = 1.49% from $127.27 close
- **GEV ex-div June 16** ($0.50 × 4 = $2.00 credit, Alpaca-managed)
- **FOMC June 6–7** (Warsh first meeting; no rate cut expected)
- **NFP June 6** (nonfarm payrolls — potential volatility)
- **Weekly slots reset June 8** (0/3 used next week)
