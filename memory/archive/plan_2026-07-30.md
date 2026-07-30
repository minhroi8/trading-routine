# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-30 (pre_market ~08:15 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates scored ≥6/10. Two strong beats screened (BKR, FTNT) — BKR dropped ~5.5/10 on fading drift + worst-sector prior; FTNT is day-1 (drift/volume/RS unmeasurable → auto-DQ). See Notes. |

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
- Clock: `is_open=false`, `next_open=2026-07-30T09:30 ET` → market opens today (Thu), NOT a holiday → proceed.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` matches portfolio.md FLAT book — zero divergence. Account ACTIVE, `trading_blocked=false`, `account_blocked=false`; equity **$98,266.98**, cash $98,266.98 (100%), buying_power $393,067.92. 0/8 concurrent.
- Universe **FRESH**: `expires_on 2026-08-02` > today (screened 2026-07-26, 287 rows).

**Regime / overlays:**
- SPY 200-day regime **BULL**: SPY last close (Jul 29) $729.57 > 200MA $699.50 (n=200, +$30.07 / +4.30%). Standard thresholds apply — max 5 new/week, no bear-regime tightening.
- PEAD health **STALE**: pead_health.md `expires_on 2026-07-26` < today 2026-07-30 → posture treated **NORMAL but flagged STALE**; the bar is **NOT raised** on a stale overlay (step 1c — the universe-cache gate is the hard halt and it PASSES). Last fresh reading (computed_on 2026-07-19): NORMAL, realized_health_60d +1.225%, n=318, health_ok=true.
- Macro-deferral: immaterial today — it can only *tighten* (raise the bar to >20%), and no candidate clears the ≥6 quality threshold on the base bar anyway, so the plan is unchanged either way.
- Net thresholds in effect: EPS surprise **>15%** (>20% for Utilities/Real Estate/Industrials/Energy; Industrials & Energy also require streak≥2), max position 20% equity, max 5 new/week (0/5 used this week; last actual fill MU Jun 25). Book FLAT.

**Overnight earnings sweep (Jul 29 AC + Jul 30 BMO reports) — universe names screened:**
- **MSFT** (IT, +8.3% premkt on Azure): FY26 Q4 EPS $4.74 vs $4.24 = **+11.8%** surprise; rev $90.01B vs $87.63B (+2.7%); Azure +43%, crossed $100B FY; raised FQ1 guide. **DROP — +11.8% below the 15% IT bar** (also reported Jul 29 AC → day-1, no drift/reaction-vol/RS measurable yet).
- **CDNS** (IT, Jul 27): EPS $2.11 vs $2.10 = **+0.5%**. **DROP — far below 15%.**
- **CMG** (Consumer Disc, Jul 29 AC): adj EPS $0.33 vs est = **+4%**; rev $3.35B (+9.3% YoY). **DROP — below 15%.**
- **SHW** (Materials, Jul 29, +8% on print): adj EPS $3.70 vs $3.56 = **+3.9%**; raised FY. **DROP — below 15%.**
- **KO** (Consumer Staples, Jul 28): adj EPS $0.97 vs $0.93 = **+4.3%**. **DROP — below 15%.**
- **META** (Comm Svcs, Jul 29 AC): rev beat but **MISSED EPS** + soft Q3 guide + $130–145B AI-capex plan + 91% FCF drop → stock **−9%**. **DROP — EPS miss, anti-PEAD.**

**Candidate #1 — Baker Hughes (BKR, Energy) — deep-researched a–i, DROPPED ~5.5/10 on fading drift + worst-sector prior:**
- Reported Jul 26 (call Jul 27); today Jul 30 = day-3/4 → drift measurable.
- (a) adj EPS **$0.64 vs $0.51 = +25.5%** surprise (clears the Energy >20% bar); revenue $6.74B vs $6.49B = **+3.9%** (modest). Adj EBITDA $1.23B > high end of guide; margin 18.3%; FCF $1.1B.
- (b) Tone bullish: record **$7.1B IET orders (doubling YoY)**, book-to-bill **2.2x**, RPO +19% to $37.1B; $2.6B power-systems orders incl. 2.7 GW gas turbines for **data centers**; raised FY26 rev guide to **$27.35B** and adj EBITDA to **$4.85B**; raised IET Horizon-2 (2026–28) orders target to >$45B. Chart Industries acquisition closed Jul 16 (3rd segment from Q3). Mgmt flagged **"Middle East uncertainty."**
- (c) Analysts strong: **24 Buy / 4 Hold / 0 Sell**, avg PT $74.21; post-earnings PT raises — Piper $73 (from $71), Stifel $75 (from $74), Susquehanna $72 (from $70), Citi $75 (from $74), Freedom Broker raised; Wall Street Zen upgrade to Buy. Stock $58.75 → ~26% to avg PT.
- (d) 52-wk high **$70.31 (2026-04-27, 64 td ago)** → normal band (46–90d) but stock **−16.4% below** the high → downrank.
- (e) Reaction-day (Jul 27) volume **~1.55x** 20-day avg → moderate confirmation (not ≥2x).
- (f) 5-day RS: BKR **+3.82%** vs SPY **−2.40%** → spread **+6.21%** (mechanically "proceed") — BUT this is defensive (SPY fell in the chip selloff), not earnings drift: **reaction popped +5.8% (Jul 27 $60.58) then FADED to $58.45 (−3.5%, Jul 28) / $58.75 (Jul 29)** = only **+2.6%** above pre-report $57.25 → 2 post-reaction days net **−3.0%** (drift stalling/reversing — the core PEAD edge deteriorating).
- (i-i) Streak **4 consecutive beats** (avg 14.61%) → satisfies Energy streak≥2. (i-ii) Reaction gap +5.8% → normal band (5–10%), no adjustment. (i-iii) **XLE 20d +10.35%** → Energy sector momentum strong (no −1 penalty).
- (g) Risk: **Energy is strategy.md's worst-documented sector (0% backtest win rate)**; Middle-East uncertainty (mgmt-cited); commodity/cyclical + oil-price sensitivity within the 42-day hold; the beat's revenue leg was thin (+3.9%).
- (h) Regulatory: shelf-reg **clean** — only routine 2026 LTIP (+9.5M sh) / ESPP (+9.5M sh) employee-plan reserves (S-8-type comp dilution), **not** a capital-raising S-3 or equity offering → no dilution-risk auto-drop. BIS export control **N/A** (energy equipment, not semiconductor).
- **Honest score ≈ 5.5/10** (signal ~2.5 / momentum ~1.0 / confirmation ~1.0 / risk ~1.0). Clears the mechanical Energy carve-out but fails the discretionary ≥6 quality bar: the **post-reaction drift is fading** (most direct evidence the specific PEAD trade won't continue) and it sits in the strategy's worst sector. **DROP** per "plan fewer buys rather than lower the bar" (consistent with GS Jul 20 step-f-broken-drift and F Jul 29 score+risk precedents). Asset check: active/tradable NASDAQ ✓.

**Candidate #2 — Fortinet (FTNT, IT) — genuinely strong, DROPPED today on day-1 auto-DQ; lead WATCH for next session:**
- Reported **Jul 29 after close → today is day-1**. The 07-29 daily bar predates the AH report, so step (e) reaction-day volume ratio and step (f) 5-day RS-vs-SPY drift are **structurally unmeasurable** (0 post-report trading days). Per MUST-NOT ("score ≥6 requires all of a–i; incomplete research = automatic disqualification"), FTNT **cannot be scored ≥6 today → DROP-for-today**.
- Signal is strong: non-GAAP **EPS $0.90 vs $0.75 = +20% surprise** (clears the 15% IT bar), rev **$2.05B vs $1.89B (+8.6%, +25.6% YoY)**, **product revenue +52%** (firewall refresh cycle), **6-consecutive-quarter beat streak**, RAISED FY26 guide (rev $8.02–8.18B, non-GAAP EPS $3.41–3.47). IT/cybersecurity (a strong sector, unlike Energy). Already in-universe (no watchlist action needed). Asset check: active/tradable ✓.
- **Action: re-evaluate at the next pre_market** once day-1 trading completes and reaction volume + RS drift become measurable — this is the strongest clean in-universe PEAD setup screened in weeks. The strategy's own PEAD design buys "+2 days after beat," so FTNT's natural entry window is the next 1–2 sessions if the drift confirms.

**Watchlist flags (non-universe compelling catalysts):**
- None new today. CNMD (CONMED, +24.3% EPS surprise Jul 29 AC) noted but **not added** — EPS-only beat with a thin revenue beat (+1.8%), no major guidance raise, smaller surgical-device name → below the compelling-catalyst bar set by existing adds (WDFC/THC/CLS/BE, all 40–90% surprises or large guidance raises + backlogs). Logged in research_log only.
- Existing watchlist pending_review items (WDFC, THC, CLS, BE) and active MRVL unchanged — MRVL has no fresh in-window earnings (reports ~late Aug); human-only to change any status.

**Result: no planned buys, no planned sells, no trailing conversions. Book stays FLAT (0/8, 100% cash).** Two of the strongest beats of the season screened today, but both fail the entry logic for a different structural reason: BKR clears the mechanical Energy bar yet its post-earnings drift is already fading in the worst-performing sector (~5.5/10), and FTNT is a genuinely high-quality setup that is simply too fresh (day-1) to measure. FTNT carries forward as the lead watch for the next session.
