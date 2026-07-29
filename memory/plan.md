# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-29 (pre_market ~08:20 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates scored ≥6/10. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — no open positions, no exit criteria to fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates (all PASS → routine ran):**
- Clock: `is_open=false`, `next_open=2026-07-29T09:30 ET` → market opens today (Wed), NOT a holiday → proceed.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` matches portfolio.md FLAT book — zero divergence. Account ACTIVE, `trading_blocked=false`, `account_blocked=false`; equity **$98,266.98**, cash $98,266.98 (100%), buying_power $393,067.92. 0/8 concurrent.
- Universe **FRESH**: `expires_on 2026-08-02` > today (screened 2026-07-26, 286 rows).

**Regime / overlays:**
- SPY 200-day regime **BULL**: SPY last close $740.80 > 200MA $699.21 (n=200, +$41.59 / +5.95%). Standard thresholds apply — max 5 new/week, no bear-regime tightening.
- PEAD health **STALE**: pead_health.md `expires_on 2026-07-26` < today 2026-07-29 → posture treated **NORMAL but flagged STALE**; the bar is **NOT raised** on a stale overlay (step 1c — the universe-cache gate is the hard halt and it PASSES). Last fresh reading (computed_on 2026-07-19): NORMAL, realized_health_60d +1.225%, n=318, health_ok=true.
- Macro-deferral: immaterial today — it can only *tighten* (raise the bar to >20%), and no candidate clears even the base 15% bar on quality/score, so the plan is unchanged either way.
- Net thresholds in effect: EPS surprise **>15%** (>20% for Utilities/Real Estate/Industrials/Energy; Industrials & Energy also require streak≥2), max position 20% equity, max 5 new/week (0/5 used this week; last actual fill MU Jun 25). Book FLAT.

**Overnight earnings sweep (Jul 28 reports) — universe names screened:**
- **SHW** (Materials, +8% on print): adj EPS $3.70 vs $3.50 = **+5.7%** surprise; rev $6.79B vs $6.61B (+2.7%); raised FY EPS guide to $11.80–12.20. **DROP — EPS surprise below the 15% bar** (guidance raise embedded in an earnings print is not the analyst-revision/partnership exemption).
- **KO** (Consumer Staples, +3% premkt): adj EPS $0.97 vs $0.93 = **+4.3%**; rev $13.38B (beat); raised FY. **DROP — below 15%.**
- **STX** (IT, beat + AI-storage story): non-GAAP EPS $5.71 vs $5.09 = **+12.1%**; rev $3.63B vs $3.49B (+4.0%); 4-qtr beat streak; +48.5% YoY rev. **DROP — +12.1% below the 15% IT bar** (also amid a 4-day semiconductor selloff — MU/AMD −8%).
- **RCL** (Consumer Disc): adj EPS $4.21 vs $4.02 = **+4.6%**; rev slightly light; raised FY EPS to $17.73–17.87 but *trimmed* rev-growth target on softening/geopolitical demand. **DROP — below 15%.**

**Candidate that cleared the 15% bar — Ford (F), deep-researched, DROPPED on score + step-g risk:**
- Reported Jul 28 **after the close** (the 07-28 IEX daily bar predates the report; AH reaction ~+6.6%). Today is a **day-1** PEAD entry → post-earnings drift, reaction-day volume, and RS-vs-SPY cannot be measured yet.
- (a) EPS $0.42 vs $0.35 = **+21.3%** surprise (clears 15%; Consumer Disc = standard bar). BUT **revenue MISSED −2.6%** ($48.3B vs $49.6B) — the beat was pricing/mix/cost-driven, not demand (weak PEAD signal quality).
- (b) Tone: CEO Farley — *"We delivered another strong quarter and raised our full-year guidance… Ford is becoming a more profitable, more disciplined and genuinely different company."* Guidance raised: FY adj EBIT $10–11B (from $8.5–10.5B, +$1B midpoint), adj FCF $6–7B — but partly a one-time **$1.3B IEEPA tariff refund** (~$500M flow-through) and dependent on tariff assumptions.
- (c) Analysts MIXED, mostly pre-earnings: Jefferies UPGRADE Hold→Buy PT $17.5 (Jul 27); JPM Overweight $16; BNP **Neutral** $14; Barclays **Equal-Weight** $14. Not the high-conviction "5 up / 0 down" profile.
- (d) 52-wk high $17.78 on 2026-05-29 = 40 trading days ago (normal band); stock ~16% below that high — downrank.
- (e) Volume: reaction-day (today) not yet measurable; 07-28 regular-session pre-report vol 2.15× — pre-report, not confirmation.
- (f) RS vs SPY: 0 post-earnings sessions — no drift to confirm.
- (i-ii) Overnight AH gap ~+6.6% (normal band, no adjustment). (i-iii) **XLY sector ETF −3.93% vs SPY −0.01% over 20d → Consumer Disc rotating OUT (−1 momentum pt).** (i-i) Streak only 2 consecutive (Q4 2025 was a MISS) → baseline, not a 3+ clean streak.
- (g) **Risk — thesis-breakers plausible within 42 days:** $1B tariff hit + **$2B aluminum/commodity headwind**, Novelis processing-plant fire disrupting automotive-aluminum supply (forcing tariffed imports up to 50%), and **record recalls (50 recalls / 11.2M vehicles YTD 2026)** with warranty-cost pressure. Tariff/policy outcomes are explicitly unresolved.
- (h) Regulatory scan: shelf-reg **clean** (mega-cap, no S-3 dilution); BIS export control **N/A** (auto, not semiconductor). No automatic regulatory drop.
- **Honest score ≈ 5/10** (signal ~1.5 / momentum ~1 / confirmation ~1 / risk ~1.5) — **below the ≥6 threshold**, and step-g flags material unresolved risk that could break the thesis within 42 days. **DROP** per "plan fewer buys rather than lower the bar."

**Watchlist flag (non-universe compelling catalyst):**
- **BE (Bloom Energy)** added to `watchlist.md` as `status: pending_review`. Q2 2026 (Jul 28 AC) blowout: EPS beat ~+90%, revenue beat ~+29% (+165% YoY), raised FY rev guide to $3.9–4.2B, $20–24B backlog (Oracle 2.8 GW + Brookfield $5B AI-infra). NOT in S&P 1500 (speculated for S&P 500 inclusion, not a member) → outside the screened universe; volatile fuel-cell name. **Cannot plan a trade until a human sets status: active.** Discord flag posted.

**Result: no planned buys, no planned sells, no trailing conversions. Book stays FLAT (0/8, 100% cash).** This is the pattern-consistent outcome for a season of high beat-rates but modest EPS-surprise *magnitudes* (S&P 500 Q2 surprise ex-Alphabet ≈ 12.6%) — most beats are quality but below the >15% PEAD threshold, and the one name clearing it (F) fails on quality/score/risk.
