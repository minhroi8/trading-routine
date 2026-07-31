# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

**2026-07-31** (Friday) — pre_market ~08:20 ET. Book FLAT at plan time (0/8, 100% cash, equity $98,266.98). DRY_RUN: false.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| PWR | 16 | $680.00 | $625.60 | **score 8/10 · Industrials — clears strict gate (EPS surprise +28.9% > 20% ✓ AND 3-qtr streak ≥2 ✓).** Q2 2026 (reported **Jul 30 BMO**): adj EPS **$4.24 vs $3.29 = +28.9% surprise**; rev **$9.56B vs ~$8.53B = +12.1% beat** (+41% YoY); **record backlog $53.4B**; **RAISED FY26 guide** adj EPS $16.45–16.95 / rev $39.3–39.7B. Earnings-day **gap +16.3%** (Jul 29 $560.92 → Jul 30 open $652.11), **closed +17.3% at $657.90 (gap HELD** — drift confirming; pre-mkt Jul 31 ~$669). **Vol 3.48x** 20d-avg. 52wk-high $788.75 (May 6, ~86d ago, −16.6% below → mild downrank). RS day-1 +17.3% vs SPY ~flat. Sector **XLI −2.21% vs SPY 20d (−1 mom)**. Analyst: mixed — Mizuho PT $645 raise, Truist Buy, JPM downgrade→Neutral (Jul 20); consensus Buy ~$761. **SI 3.96%** float. Insider: mild selling (Nobel 4,000 sh @ $756.98). Quote (CEO Duke Austin): *"broad-based organic strength across our segments, service lines, and end markets… record backlog of $53 billion."* Top risk: rich ~89x P/E + downtrend into print. **Shelf-reg: CLEAN. BIS: N/A.** Next earnings ~Oct/Nov (not <3d). Active/tradable ✓. Sizing 10.9% of equity < 20% cap. |
| AMZN | 41 | $264.00 | $242.88 | **score 8/10 · CATALYST basis (AWS reacceleration) — EPS-threshold-EXEMPT.** (Clean operating EPS surprise ~low-teens % < 15% Cons-Disc bar; the +216% headline EPS is a non-cash Anthropic mark-up, NOT used as the basis.) Q2 2026 (reported **Jul 30 AC**): **AWS rev $42.2B +36.7% YoY** (fastest in 18 qtrs, **5th straight accel**, beat +4.2%); total rev $200.6B +20% (beat +2.1%); **op income $27.5B +43% YoY**; **backlog $496B +triple-digit**. Earnings-day **gap +11.5%** (AH $255.25 vs $226.82 close; holding pre-mkt). 52wk-high $278.53 (May 5, ~86d ago, −15.4% below → weak, reversal-off-drawdown). Vol ~1.74x proxy (true spike bar Jul 31 pending). RS 5d +0.44% vs SPY; gap adds decisive RS. Sector **XLY −4.29% vs SPY 20d (−1 mom)**. Analyst: **4+ post-print PT raises, 0 downgrades** (GS $375, Barclays $365, BofA $320, MS OW $335), consensus Strong Buy. **SI 0.93%** (low). Insider: no material 2026 selling (clean). Streak 2 consec beats. Quote (CEO Andy Jassy): *"Our backlog stands at $496 billion, growing triple digits year-over-year… even at [$220B capex] we will still not have enough capacity to meet all the demand."* Top risk: **light Q3 rev guide (−2.2% vs cons)** + $220B capex / negative FCF; dirty headline EPS. **Shelf-reg: CLEAN** (mixed shelf backs debt, no equity dilution). **BIS: N/A.** Next earnings ~late Oct (not <3d). Active/tradable ✓. Sizing 10.8% of equity < 20% cap. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0 positions) — no exit criteria to evaluate. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates:** clock `is_open=false`, `next_open=2026-07-31T09:30 ET` → market opens today (Fri), NOT a holiday → proceed. **Reconciliation 0/0 PASS** — Alpaca `/v2/positions=[]` matches portfolio.md FLAT book, zero divergence. Account ACTIVE, trading_blocked=false; equity $98,266.98, cash 100%, 0/8 concurrent. **Universe FRESH** (expires_on 2026-08-02 > today, screened 2026-07-26, 287 rows).

**PEAD health STALE** (pead_health.md expires_on 2026-07-26 < today → posture treated **NORMAL flagged STALE**; bar NOT raised per step 1c — a stale overlay never raises the bar, the universe-cache gate is the hard halt and it PASSES). Last fresh reading (computed_on 2026-07-19): NORMAL, realized_health_60d +1.225%, n=318, health_ok=true.

**SPY regime BULL** (Jul 30 IEX close $741.63 > 200d-MA ~$698.72, +6.1%, n=208) → standard strategy.md thresholds: EPS >15% (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also streak≥2), **max 5 new/week**, no ELEVATED_BAR cap. **Macro-deferral NOT triggered:** S&P 500 futures **+0.24% (UP)** pre-market (AMZN/AAPL/MSFT earnings lifting tech) → the "futures down >0.4%" leg fails; 10-yr ~4.62–4.67% (near-but-not-fresh multi-month high) → both legs not met. DRY_RUN: false.

**Shortlist deep-researched (steps a–i):**
- **PWR — QUALIFY 8/10** → planned buy (above). Clears strict Industrials gate (+28.9% EPS > 20%, 3-qtr streak). Held its +17% earnings gap = clean positive drift.
- **AMZN — QUALIFY 8/10 (catalyst basis)** → planned buy (above). AWS +36.7% reacceleration + Street re-rating; EPS-exempt.
- **LRCX — DROP 4/10.** EPS surprise only ~+7.7% (fails 15% IT bar) — headline +18% was the *stock* move, an oversold relief bounce off a −32% drawdown; heavy insider selling; China/BIS overhang. No entry.
- **FTNT — DROP 6/10 (drift gate failed).** Elite fundamentals (+20% EPS beat, +52% product, 6-qtr streak, raised guide) BUT day-1 was a **gap-and-fade** (opened +8.6%, closed +0.5%) on 2.68x *distribution* volume; RS −1.15% vs SPY; ~58x P/E; CEO selling. PEAD longs need the pop to hold — it was rejected. (Was flagged "lead watch" Jul 30; the day-2 read resolved DOWN.)

**Other movers dropped before full a–i (failed at EPS/reaction gate):** MSFT +11.8% EPS < 15% IT bar (also EPS lifted by $3.2B Anthropic gain); AAPL +6.9% EPS < 15% + slid −6% on cautious/supply-constrained Sept guide (anti-PEAD); META EPS **MISS** −13.8%, −8.75% (anti-PEAD); SHW +3.9% EPS < 15% Materials bar.

**Watchlist flags (pending_review, Discord-flagged — MUST NOT plan until human sets `active`):**
- **EME (EMCOR, Industrials, NOT in universe cache):** Q2 +18% on a blowout beat + RAISED FY2026 guidance + record project backlog. Compelling non-universe Industrials PEAD catalyst → added pending_review.
- **FORM (FormFactor, IT/semiconductor, NOT in universe):** Q2 rev $258.2M +32% YoY (beat ~$240M consensus), stock +27% on strong semi-test demand. Compelling non-universe catalyst → added pending_review.

**Watchlist carries (no action):** MRVL (active) — no fresh in-window catalyst (reports ~Aug 27; Erste downgrade Jul 14) → no plan; status stays active (human-only). WDFC / THC / CLS / BE (pending_review) — MUST NOT plan (human-only).

**Sanity-check vs strategy.md:** cash floor after both fills ~78% >> 10% ✓; max concurrent 2/8 ✓; new-per-week 2/5 (BULL; last actual fill MU Jun 25, 0 buys this week) ✓; sector caps — Industrials (PWR) 10.9%, Consumer Disc (AMZN) 10.8%, both << 30% ✓. Both survivors re-verified: next earnings NOT within 3 days; both active/tradable/not halted.
