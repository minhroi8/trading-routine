# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-05-28

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis_ref |
|--------|------------|-------------|------------|------------|
| PWR *(contingent — execute ONLY if NVDA stop daaecbf6 fills first)* | 6 | $735 | fill × 0.92 (~$676) | Q1 2026 EPS $2.68 vs $1.98 est (+35% beat), record backlog $48.5B, $1B buyback, FY2026 guidance raised. CEO + CFO at Bernstein conference at 1:30 PM ET today. Earnings re-verified Jul 30, 2026 (63 days, clear). tradable=True, status=active (Alpaca). No halt, no SEC investigation. Industrials sector. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none — proactively)_ | — | NVDA stop daaecbf6 ($205.43) is Alpaca-managed. Pre-market price $210.42 = only ~$5.00 cushion (~2.4%). PCE data at 8:30 ET is a volatility catalyst. If stop fires, market_open executes PWR contingent buy above. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

### Macro (2026-05-28 pre-market, ~08:14 ET)

- **PCE data (April 2026)**: Scheduled 8:30 AM ET. Pre-release consensus: Headline PCE ~3.8% YoY (3-year high), Core PCE ~3.3% YoY. One source suggests actual April PCE may print lower (~2.7% headline/core). **market_open must check actual print before trading.** A hot print (at or above consensus) would pressure tech; a cool/below-consensus print would be bullish and ease NVDA stop risk.
- **S&P 500 futures**: Flat-to-slightly-up (~ES 7,534–7,538). NOT down >0.4%.
- **10-yr yield**: ~4.50%, elevated but NOT at multi-month high (peak was 4.70% on May 20).
- **Macro deferral rule**: NOT triggered (requires both futures >0.4% down AND yield at multi-month high — neither condition met). ✓
- **Oil**: ~$90/bbl WTI (new US military strikes on Iranian facility overnight). Geopolitical risk elevated.
- **DRY_RUN**: false

### Portfolio status (pre-market prices, ~08:14 ET)

| ticker | avg_cost | pre-mkt price | unreal % | stop / order | key notes |
|--------|----------|---------------|----------|------|-----------|
| AAPL | $283.10 | $310.20 | +9.57% | trailing 4225eab6 (HWM $313.26, stop $291.33) | Melius PT $385; BofA PT $380. **WWDC Jun 8–12.** Trailing auto-managed. |
| AMD | $421.59 | $489.50 | +16.11% | trailing 9e760e91 (HWM $510.07, stop $474.37) | ~$15.50 cushion above stop. OpenAI/Meta demand intact. Auto-managed. |
| AMZN | $269.71 | $272.07 | +0.87% | hard f87a7a95 ($248.14) | New Street PT $350. AWS +28% YoY intact. 8.8% cushion. |
| CSCO | $117.42 | $119.49 | +1.77% | hard 54eb2e8d ($108.10) | BofA PT $135. AI orders $9B FY2026. 9.5% cushion. |
| GEV | $996.47 | $1,030.00 | +3.37% | hard 68f84ddd ($916.75) | Q3 div $0.50 declared (ex Jun 16). Turbine fleet 4M hrs milestone. **Trigger $1,096.12 ($66 gap).** 11.0% cushion. |
| GOOGL | $395.72 | $387.22 | −2.15% | hard d8219caa ($364.07) | Chrome non-divestiture ruling (April 2026) pre-existing positive; DOJ cross-appealing — long tail but no near-term structural risk. No new catalyst today. 6.0% cushion. |
| MSFT | $412.63 | $415.50 | +0.69% | hard 790e2653 ($379.62) | Azure +40% YoY intact. DOD CETA contract positive. Pre-mkt −0.75% is macro-driven. 8.6% cushion. |
| NVDA | $223.30 | $210.42 | −5.77% | hard daaecbf6 ($205.43) | **HIGHEST RISK.** Stop only ~$5.00 away (2.4% cushion). Q1 FY2027 blowout thesis intact ($81.6B rev, Q2 guide $91B). China Huawei concession is pre-existing known risk. PCE print could test stop. Alpaca manages stop; no action from pre_market. |

### Key watch items for market_open

1. **PCE print (8:30 ET)**: Check actual vs. consensus. If headline PCE ≥3.8% YoY and/or core ≥3.3% YoY, macro deferral rule re-evaluated (requires futures to also drop >0.4% simultaneously). If PCE is below consensus → relief rally → NVDA stop risk eases.

2. **NVDA stop watch**: If NVDA drops ≤$205.43 during the session, Alpaca stop order daaecbf6 fires automatically. After fill confirmation: immediately execute PWR contingent buy (6 shares, limit $735, stop = fill × 0.92).

3. **AMD trailing stop (9e760e91)**: Verify Alpaca HWM at market_open. Pre-market price $489.50 vs. HWM $510.07 — no new HWM expected unless AMD rallies sharply. Stop at $474.37 remains; cushion ~$15.50.

4. **GEV trailing trigger**: If GEV trades ≥$1,096.12 intraday (+10% vs avg_cost $996.47), cancel hard stop 68f84ddd ($916.75) and place 7% trailing stop. Currently $66 below trigger.

5. **PWR Bernstein conference (1:30 PM ET)**: CEO Duke Austin + CFO Jayshree Desai fireside chat with analyst Chad Dillard. Any new backlog, margin, or AI data-center commentary could be a price catalyst. If NVDA stop fires before 1:30 PM, consider timing PWR limit order to capture pre-conference momentum.

### Sanity checks (no unconditional trades planned)

- Cash floor: $62,310.92 / $100,855.47 = 61.8% >> 10% ✓
- Concurrent positions: 8/8 (at cap — no unconditional new buys) ✓
- New positions this week (May 25–31): 0/3 ✓
- IT sector: AAPL + AMD + CSCO + MSFT + NVDA MV ≈ $24,882 / $100,855 = 24.7% < 30% ✓
- **Contingent check (if NVDA exits + PWR enters):**
  - Cash: $62,311 + NVDA proceeds (~$4,519) − PWR cost (6 × $735 = $4,410) ≈ $62,420 = 61.9% >> 10% ✓
  - Concurrent: 8 − 1 + 1 = 8 ✓
  - Weekly new positions: 0 + 1 = 1/3 ✓
  - Industrials sector: GEV $4,120 + PWR $4,410 = $8,530 / ~$101K = 8.4% << 30% ✓

### Watchlist (for human reference — no capacity today unless a position exits)

1. **PWR** (~$723–$735) — Top priority. CEO/CFO at Bernstein conference 1:30 PM ET. Contingent buy planned above if NVDA exits. Q1 2026 EPS +35%, record backlog $48.5B, $1B buyback. Next earnings Jul 30, 2026.

2. **ETN** (~$403) — Q1 2026 beat, data center orders +240% YoY. UBS downgraded to Neutral (watch for stabilization). Next earnings Aug 4, 2026.

3. **AVGO** (~$422) — Strong AI thesis (revenue +140% YoY est). **Earnings June 3, 2026 (6 calendar days). 3-day window opens effectively June 2 (Mon). DO NOT plan entry May 30 (Sat) or later. Revisit post-earnings if beat confirms AI trajectory.**
