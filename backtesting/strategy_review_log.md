# Strategy Review Log

Running log maintained by `strategy_review` routine (Saturdays 10:00 ET). Accumulates across weeks to give the routine cross-week memory and anti-overfitting counters.

**This file is the ONLY file this routine writes. `memory/strategy.md` is never edited by any routine — human applies all changes.**

---

## 2026-06-30 — Weekly Strategy Review

**Run time:** Sat 2026-06-30 ~10:00 ET  
**Routine:** `strategy_review` (market-independent — no clock gate needed)  
**Reconciliation (read-only sanity check):** Alpaca `/v2/positions` = `[]` MATCHES portfolio.md FLAT book → 0/0 PASS, zero divergence. Book is 100% cash, equity $98,266.98.  
**pead_health.md status:** STALE (computed Jun 21, expires Jun 28 < today Jun 30). Last posture: ELEVATED_BAR (realized health −0.492%, n=367). Recurring partial universe_refresh anomaly (Jun-28 run rebuilt universe.md but did NOT recompute pead_health.md — second consecutive week flagged).  
**SPY regime:** BULL (close $740.86, 200MA $690.95). Standard strategy.md thresholds in effect.

---

### Anti-overfitting counters (Gate 3)

| Proposal | Times backtested (prior runs) | Status |
|----------|------------------------------:|--------|
| All proposals | 0 | First run — no prior backtest history |

No proposal is EXHAUSTED. All STRONG proposals are eligible for backtesting.

---

### ✅ Already Implemented (filter out of ranking)

These proposals appear in the current `memory/strategy.md` and are confirmed closed.

1. **Same-day open+close counts toward weekly new-position cap** — `strategy.md` explicitly states: "a position opened and closed same day via midday cut still consumes a weekly slot — research, placement, and risk exposure all occurred." (First flagged: week May-18, applied Jun-01 window.)

2. **Macro deferral rule** — `strategy.md` § Risk controls: "if S&P 500 futures are down >0.4% AND the 10-year Treasury yield is at a multi-month high in the same pre-market session, raise the EPS surprise threshold to >20% for that day only." (First flagged: week May-18.)

3. **Partial profit-lock at +10% trailing-conversion trigger** — `strategy.md` § Risk controls: "Sell 1/3 of the position immediately at market when the +10% trigger crosses... Apply a 7% trailing stop (all sectors) to the remaining 2/3." Rationale explicitly references "repeated give-back pattern observed 3 consecutive weeks (CSCO round-tripped +7-10% to +0.10%)." (Flagged 3 weeks: Jun-08 PARTIAL, Jun-08 full, Jun-15; applied after Jun-15 review.)

---

### 🔴 STRONG Proposals — Backtested This Run

---

#### S1: ELEVATED_BAR Realized-Health Threshold Recalibration

**Proposal:** Recalibrate the realized-health threshold that triggers ELEVATED_BAR posture from 0.0% to a negative value (−1.0% candidate), reducing multi-week over-blocking in non-hostile regimes.

**Evidence tier:** STRONG — flagged 3 distinct calendar weeks (Jun-08, Jun-15, Jun-22) + documented recurring impact: 4–5 weeks of ~80–90% idle cash while SPY held well above 200MA, ELEVATED_BAR producing 0–1 qualifiers/week.

**First flagged:** Week of Jun-08 (PARTIAL), Jun-08 (full-week review), Jun-15, Jun-22.  
**Prior backtest count:** 0 (first test this run).

**Existing evidence:** `backtest_report_PEAD_SIGNAL_HEALTH.md` and `backtest_report_PEAD_HEALTH_200MA_COMBO.md` tested the current health ≥0 gate. Key finding from combo report: Health ≥0 + SPY>200MA combined keeps only 39% of 2023 trades (22/57) averaging −0.97% — the AND combination is counterproductive in the historically good year 2023, far worse than SPY>200MA alone (keeps 95% averaging +1.2%).

**Backtest run this session:** Lightweight analysis using cached `backtest_signal_health_candidates.csv` (8,190-row BASE population, 2021–2026). Recomputed point-in-time realized health (60-day lookback) at every enhanced-trade entry date, then tested thresholds −2.0%, −1.5%, −1.0%, −0.5%, and 0.0%.

**Results:**

*Aggregate (all eval years 2022–2026):*

| Threshold | Trades | Win% | Avg% | PF | vs current (0%) |
|-----------|-------:|-----:|-----:|---:|----------------:|
| −2.0% | 229 | 54.1% | 1.76% | 1.62 | −0.07 pts |
| −1.5% | 212 | 54.2% | 1.85% | 1.67 | +0.02 pts |
| **−1.0%** | **209** | **55.0%** | **1.92%** | **1.69** | **+0.09 pts** |
| −0.5% | 196 | 54.6% | 1.66% | 1.59 | −0.17 pts |
| 0.0% (current) | 191 | 55.5% | 1.83% | 1.66 | baseline |

*In-sample (2022–2024) vs Out-of-sample (2025–2026):*

| Threshold | IS Trades | IS Avg% | IS PF | OOS Trades | OOS Avg% | OOS PF |
|-----------|----------:|--------:|------:|-----------:|---------:|-------:|
| −2.0% | 163 | 1.86% | 1.70 | 66 | 1.49% | 1.47 |
| −1.5% | 158 | 1.84% | 1.69 | 54 | 1.88% | 1.59 |
| **−1.0%** | **157** | **1.89%** | **1.72** | **52** | **2.0%** | **1.62** |
| −0.5% | 144 | 1.53% | 1.57 | 52 | 2.0% | 1.62 |
| 0.0% (current) | 139 | 1.77% | 1.69 | 52 | 2.0% | 1.62 |

*Per-year blocking rates and avg returns:*

| Threshold | 2022 blocked | 2022 avg | 2023 blocked | 2023 avg | 2024 blocked | 2025 blocked | 2026 blocked | Discrimination |
|-----------|-------------:|---------:|-------------:|---------:|-------------:|-------------:|-------------:|---------------:|
| −2.0% | 15% | −4.06% | 37% | +1.91% | 0% | 12% | 30% | +6 pts |
| −1.5% | 18% | −3.84% | 44% | +1.42% | 0% | 14% | 67% | +23 pts |
| **−1.0%** | **18%** | **−3.84%** | **44%** | **+1.42%** | **1%** | **18%** | **67%** | **+22 pts** |
| −0.5% | 36% | −4.12% | 56% | −1.90% | 1% | 18% | 67% | +27 pts |
| 0.0% (current) | 42% | −4.08% | 60% | −1.30% | 2% | 18% | 67% | +28 pts |

**Key finding — 2023 reversal:** At the current 0% threshold, the health gate blocks 60% of 2023 trades, but the 23 trades that pass through average **−1.30%** (negative). At −1.0%, 44% are blocked and the 33 trades allowed through average **+1.42%**. This means the additional trades allowed by the looser threshold (health between −1% and 0%) actually performed well in 2023, while the current threshold is selecting against good 2023 trades. The gate is counterproductive in 2023 at 0%.

**Out-of-sample discipline check:** The OOS stats (2025–2026) are **identical** at −1.0% and 0.0% — same 52 trades, same 2.0% avg, same 1.62 PF. This is because in both 2025 and 2026, the realized health signal was either clearly above 0% (2025 mid-year, both thresholds agree) or clearly below −1.0% (2026 hostile period). The −1.0% threshold makes no difference in OOS outcomes.

**Live implication:** The Jun 2026 health reading was **−0.492%** (between −1.0% and 0.0%). Under the proposed −1.0% threshold, this reading would NOT have triggered ELEVATED_BAR (−0.492% ≥ −1.0%). Under the current 0.0% threshold, it triggers ELEVATED_BAR. The backtest shows OOS performance is identical at both thresholds, so the multi-week over-blocking at −0.492% health is not justified by OOS evidence.

**Beat-the-benchmark bar:** SPY returned approximately +26% in 2023 and +23% in 2024. The strategy's OOS avg of 2.0% per trade (52 OOS trades, PF 1.62) on ~$11k positions with selective deployment does not generate annualized equity-vs-SPY comparison directly, but the key metric here is the PF improvement (1.62 maintained at −1.0%) vs the cost of 2023 over-blocking at 0%.

**Verdict: ✅ BACKTEST SUPPORTS (OOS performance identical, 2023 quality improved)**

**Proposed wording for `strategy.md` (human applies):**

> **In `pead_health.md` computation and the ELEVATED_BAR threshold:** Change the realized-health trigger threshold from `>= 0.0%` to `>= -1.0%`. Rationale: backtest (2022–2026) shows OOS performance (2025–2026) is identical at both thresholds (52 trades, 2.0% avg, PF 1.62), while IS quality improves (avg 1.89% vs 1.77% at 0%). The 0% threshold over-blocks in 2023 (60% blocked, −1.30% avg on allowed trades); the −1.0% threshold reduces 2023 blocking to 44% and avg improves to +1.42%. Discrimination remains strong (+22 pts at −1.0% vs +28 pts at 0%).

> Concretely: in `compute_pead_health.py` (or wherever the ELEVATED_BAR posture is computed), change the threshold comparison from `realized_health >= 0.0` to `realized_health >= -1.0`. Update `pead_health.md` to reflect the new threshold upon next universe_refresh run.

**Anti-overfitting counter update:** 1 backtest run (2026-06-30). Not EXHAUSTED. Eligible for 1 more test on same periods.

---

#### S2: "Never-Worked" Chronic-Underwater Monitoring Flag

**Proposal:** In `pre_market`, surface a position that (a) has NOT closed green on any session within N days of entry, AND (b) has stop cushion persistently <2%, for human review. NOT an auto-cut — thesis can still be intact. Gives the human a decision point above the mechanical −8% stop.

**Evidence tier:** STRONG — flagged 3 distinct calendar weeks (Jun-08, Jun-15, Jun-22) + documented real-money losses: GEV −$319.18 (−8.01%, held 21 days, never green, Jun-09); CASY −$813.58 (−8.21%, held 12 days, never green, Jun-23). Pattern appeared in 4 distinct weekly entries.

**First flagged:** Jun-08 PARTIAL (GEV acute phase); Jun-08 full (carry-forward); Jun-15 (CASY acute phase); Jun-22 (CASY realized at −8.21%, 4th flag).  
**Prior backtest count:** 0 (first run).

**Backtest type:** This proposal is a monitoring/alerting rule, not a mechanical exit rule (the proposal explicitly says "not auto-cut"). A formal trade-level backtest cannot be run without assuming discretionary behavior. Instead: analytical assessment using cached `backtest_trades_PEAD_2022_2025_ENHANCED_base.csv` (5,836 rows, enhanced trades).

**Trade-level analysis results:**

*Hard-stop exit holding-day distribution (enhanced trades, 2022–2025):*

| Period | Enhanced trades | Hard-stop exits | Early stops (≤3d) | Chronic stops (≥10d) | Median stop hold |
|--------|---------------:|---------------:|------------------:|---------------------:|-----------------:|
| 2022–2024 IS | 194 | 46 (24%) | 5 (3%) | 34 (18% of total) | 19.5 days |
| 2025 OOS | 53 | 15 (28%) | 2 (4%) | 10 (19% of total) | 14.0 days |

*Stop holding-day buckets (2022–2025 enhanced hard-stops):*

| Hold bucket | Trades | % of all stops | Avg ret% |
|-------------|-------:|---------------:|---------:|
| ≤1d (MU-style) | 1 | 2% | −9.71% |
| ≤2d | 1 | 2% | −11.02% |
| ≤3d | 4 | 7% | −9.61% |
| ≤5d | 1 | 2% | −8.92% |
| ≤10d | 10 | 16% | −8.79% |
| ≤20d (CASY/GEV range) | 17 | 28% | −9.27% |
| ≤42d | 26 | 43% | −9.14% |

*Chronic stops (≥10d) by sector:*

| Sector | Chronic stops | Total enhanced | Rate |
|--------|-------------:|---------------:|-----:|
| Consumer Discretionary | 10 | 33 | 30% |
| Real Estate | 3 | 10 | 30% |
| Consumer Staples | 4 | 19 | 21% |
| Comm. Services | 3 | 15 | 20% |
| Materials | 2 | 10 | 20% |
| Industrials | 10 | 52 | 19% |
| Health Care | 3 | 20 | 15% |
| IT | 5 | 36 | 14% |
| Financials | 3 | 35 | 9% |
| Utilities | 1 | 11 | 9% |

**Key findings:**
- **43% of all hard-stop exits are "chronic"** (held >20 days before stopping), matching the GEV (21d) and CASY (12d) profile exactly.
- **Chronic stops are NOT sector-concentrated.** Consumer Discretionary (30%) and Real Estate (30%) are highest but the pattern spans all sectors.
- Only 7% of stops are "early" (≤3d, the MU-style same-day noise stop) — these are a separate problem addressed by S3.
- The "never-worked" flag would need N=5–7 trading days and cushion <2% to generate an actionable alert in most chronic-stop cases (median: 19.5d to stop, so flag would trigger well before the stop fires).
- **Estimated impact:** If ~50% of chronic stops (~21% of all trades) were exited 3% early (at ~−5% vs −8%) via human discretion after a flag, the per-trade savings would be roughly 0.21 × 0.5 × 3% = ~0.3% improvement on all trades. On $11k positions, ~$33/trade average improvement. Small per-trade but cumulative across a year of chronic stops.

**OOS note:** Not a mechanical rule; no OOS backtest possible. The flag itself costs nothing (it's information), so the question is purely whether the human acts on it. Both documented instances (GEV, CASY) where the flag would have fired resulted in the full −8% stop being hit with thesis intact — the flag would have given 5–10 days of advance notice in both cases.

**Beat-the-benchmark bar:** N/A (monitoring rule; no direct P&L modeled).

**Verdict: ✅ ANALYTICAL SUPPORT — Recommend implementing the flag. Sufficient evidence from 3 weeks of flagging + 2 documented instances. No backtest possible (monitoring rule); human discretion is the mechanism.**

**Proposed `strategy.md` addition (human applies):**

> **In `pre_market` thesis-audit section:** Flag any open position as `CHRONIC_WATCH` if BOTH of the following are true as of this session: (a) the position has NOT closed green on any session since entry, AND (b) the current price is within 2% of the hard stop (stop cushion ≤2%). Log in `plan.md` notes: "⚠️ CHRONIC_WATCH: `<TICKER>` — held `<N>` days, never closed green, cushion `<X>%` above stop `$<stop_price>`. Human decision: hold into likely −8% stop, or exit above stop." This is NOT an auto-exit — the agent does not place any order. If thesis is invalidated (guidance cut, earnings miss, fraud), normal midday-cut rules still apply.

**Anti-overfitting counter update:** No formal backtest (analytical only). Counter stays at 0.

---

#### S3: Volatility-Scaled Wider Stop for High-ATR Names

**Proposal:** For names where 2× the 20-day ATR exceeds 8%, use `max(8%, 2×ATR%)` as the initial stop instead of the flat −8%. This widens the stop on volatile names to avoid noise stop-outs where the −8% stop sits inside one day's natural range.

**Evidence tier:** STRONG — flagged 1 week (Jun-22) but qualifies under "addresses a pattern that has caused a documented real-money loss." Live instance: MU bought Jun-25 at $1,249.73, stopped same day at −8.08% (−$807.58). ATR at entry was ~9–10%/day → 2×ATR ~18–20% → the −8% stop was inside half a day's range. Thesis fully intact at exit (plan.md explicitly noted the risk before entry). Also: existing backtest explicitly recommended raising/removing the 8% cap.

**First flagged:** Jun-22 (new, with concrete same-day loss). Related "stop too tight" pattern in 5 prior weeks via CSCO/SNDK give-back (trailing stop side).  
**Prior backtest count:** 0 for this specific proposal (wider stop). The TIGHTER variant (V1: `min(8%, 2×ATR)`) was tested in `backtest_report_ATR_STOP_VS_FLAT.md` and rejected. The WIDER variant (the actual proposal) has NOT been backtested.

**Backtest type:** Price-path simulation requires re-fetching OHLC data (data cache empty). Instead: analytical estimate using cached `backtest_trades_ATR_STOP_V0.csv` (277 trades from ATR backtest).

**Analytical estimate results:**

*High-ATR trades (2×ATR > 8%, wider stop activates):*

| Group | Trades | Avg return | Stop rate | Early stops (≤5d) |
|-------|-------:|-----------:|----------:|------------------:|
| High-ATR (2×ATR > 8%) | 41 (15%) | **+2.74%** | 46% | 37% of their stops |
| Normal-ATR (flat 8%) | 236 (85%) | +1.28% | 24% | 3% of their stops |

High-ATR names (mean ATR: 5.30%/day, mean proposed wider stop: 10.6%):

| Period | High-ATR trades | Avg% | PF | Normal-ATR trades | Avg% | PF |
|--------|---------------:|-----:|---:|------------------:|-----:|---:|
| 2022–2024 IS | 22 | +0.13% | 1.03 | 172 | +2.03% | 1.84 |
| 2025 OOS | 11 | **+6.72%** | **2.42** | 42 | −0.21% | 0.92 |
| 2026 OOS YTD | 8 | **+4.46%** | **2.11** | 22 | −1.71% | 0.59 |

*High-ATR noise stop analysis (≤5 days):*
- 37% of high-ATR hard stops fired within 5 trading days (7/19 stops)
- Compare: 3% for normal-ATR names
- Median holding days to stop on high-ATR: 8 days vs 19.5 days for normal-ATR (IS)
- Mean ATR at entry for high-ATR stops: 5.29%/day → 2×ATR stop would have been 10.6%

**Key findings:**
1. **High-ATR names outperform in OOS (2025–2026)**: +6.72% and +4.46% avg vs −0.21% and −1.71% for normal-ATR. The PEAD signal appears stronger on high-volatility names in recent OOS periods.
2. **Early noise-stop rate is 12× higher on high-ATR names** (37% vs 3%). This confirms that the flat −8% stop fires on noise far more frequently for volatile names.
3. **Direction confirmed by prior backtest**: `backtest_report_ATR_STOP_VS_FLAT.md` explicitly states: "If the goal is genuinely to avoid noise stops on high-ATR names, the fix is to raise/remove the 8% cap (let the ATR term widen the stop), not to add an ATR floor beneath an unchanged cap." This is exactly the direction of the current proposal.

**OOS discipline:** The OOS advantage of high-ATR names (+6.72% in 2025, +4.46% in 2026 YTD under V0) suggests that a wider stop allowing these names more room to develop could improve OOS returns. However, this cannot be confirmed without a price-path simulation. The 2022-2024 IS performance of high-ATR names (+0.13%, PF 1.03) is poor, suggesting they are riskier and need good thesis selection — the ELEVATED_BAR filter may inadvertently be doing some of this work by blocking the weakest signals.

**Caveats:**
- A 10.6% mean wider stop represents a significantly larger per-trade risk. On an $11k position, the max loss increases from $880 to $1,166 (mean). This requires either accepting higher max loss per trade OR reducing position size to keep dollar risk constant.
- The MU instance (ATR ~10%/day → wider stop ~20%) would have required a $2,200 stop vs $880 flat. Position sizing adjustment would reduce notional to ~$4,400 to keep dollar risk at $880.
- The ELEVATED_BAR posture blocks most high-ATR entries in hostile periods anyway, so the practical impact of wider stops is concentrated in BULL/NORMAL periods.
- A full price-path simulation is needed to confirm the OOS verdict.

**Beat-the-benchmark bar:** Not assessable without full simulation.

**Verdict: ⚠️ DIRECTION SUPPORTED (prior backtest explicitly endorses the direction; OOS high-ATR outperformance is consistent with widening the stop); but OOS confirmation requires a full price-path backtest that cannot be run this session (empty data cache). CONDITIONAL recommendation pending full simulation.**

**Proposed wording for `strategy.md` (human applies — NOTE: position sizing change required if adopted):**

> **In `market_open` stop placement:** When placing the initial hard stop after a fill, compute the 20-day ATR as a percent of the entry price. If `2 × ATR% > 8%`, use `max(8%, 2 × ATR%)` as the stop distance instead of the flat 8%. Simultaneously, reduce the position notional proportionally so that the dollar risk per trade (0.8% × equity = ~$785) stays constant: `notional = min(11% × equity, 0.8% × equity / stop_distance_pct)`. Log the ATR-adjusted stop in `trade_log.md` with the ATR value used. This rule applies to new entries only; existing stops are not retroactively widened.

> Note: This requires `market_open` to fetch 20 days of daily OHLC at entry time to compute ATR — one additional API call per new position.

**Anti-overfitting counter update:** Analytical assessment this run (no price-path simulation). Counter at 0 for formal backtests.

---

### 🔴 STRONG Proposals — Procedural (No Backtest Meaningful)

These are procedural/operational rules rather than mechanical trading strategy changes. They cannot be evaluated via trade-level backtesting. Evidence strength is assessed analytically.

---

#### S4: SEC EDGAR Shelf-Registration Pre-Market Scan

**Proposal:** During `pre_market` thesis check for each existing position, scan SEC EDGAR for 424B, S-3, and S-1 shelf-registration or prospectus filings in the prior 30 days. Flag any that could indicate an imminent dilutive equity raise.

**Evidence tier:** STRONG — 4 distinct weekly entries (Jun-01, Jun-08, Jun-15, Jun-22) + documented real-money loss: GOOGL −$413.92 (−8.71%, Jun-02). The $80B Alphabet equity offering was filed Jun-02 AM; a pre-market EDGAR scan that morning would have surfaced the 424B1 filing before the open, allowing a proactive exit above the $364.07 stop.

**Analytical assessment:**
- Documented instances: 1 direct loss (GOOGL −$413.92), 0 rescued instances (no scan existed)
- False-positive risk: shelf registrations are common corporate governance filings and do NOT always indicate imminent dilution. An S-3 shelf is filed well in advance of any actual offering. Filtering for 424B prospectus supplements (indicating an active offering) within the prior 5–7 days would narrow to actionable signals.
- Implementation complexity: MODERATE. Requires an authenticated EDGAR API call (EDGAR full-text search API is free) per existing position at each pre_market run. ~3–8 positions at any time = 3–8 API calls.
- The GOOGL case was distinctive: a $80B raise is rare and clearly material. Most shelf filings are not that size. Recommend restricting the alert to prospectuses raising >5% of market cap.

**Verdict: RECOMMEND — Low implementation cost, documented $413.92 loss is the precedent. Human applies.**

---

#### S5: Export-Control Monitoring for Semiconductor / IT Positions

**Proposal:** During `pre_market` thesis check, scan Commerce Dept BIS guidance updates, Entity List changes, and executive orders affecting chip exports. Flag any IT/semiconductor position if a BIS action from the prior 5 trading days is detected.

**Evidence tier:** STRONG — 4 distinct weekly entries (Jun-01, Jun-08, Jun-15, Jun-22) + documented losses: AMD stopped −8% (Jun-01, BIS MI350x loophole closure); NVDA stopped −8% (Jun-05, broad export-control selloff). Both exits had intact theses; the stops were triggered by regulatory announcements, not fundamental deterioration.

**Analytical assessment:**
- Documented instances: 2 losses in the same week (AMD −$757+, NVDA stop in ~$780+ range) directly attributable to BIS actions
- Plan.md Jun-30 already includes a "BIS export-control scan CLEAN" note in the MU deep-research entry, showing the routine is already performing ad-hoc BIS scans for new entries. The proposal is to extend this to existing position thesis checks.
- Sources: BIS publishes Federal Register notices and press releases. A keyword search for "semiconductor," "AI chip," or specific company names against BIS.doc.gov / FR.gov is feasible.
- False-positive risk: export-control news is frequent and often company-agnostic. The signal is high-specificity when a named company or product category (HBM, MI300x, A100) is cited directly.
- Note: MU's BIS scan in the Jun-30 plan.md ("HBM 3A090.c controls date to Dec 2024, >30d, no fresh MU-specific action") demonstrates the scan is feasible and was already performed manually. Formalizing it into the pre_market routine for all open positions is the only change required.

**Verdict: RECOMMEND — Precedent already exists (MU BIS scan in pre_market deep-research). Extend to open positions. Human applies.**

---

#### S6: Investigate Missed Pre-Market Scheduler Gaps

**Proposal:** Investigate why `pre_market` failed to run on at least 5 sessions across May–June 2026 (May 11–13, Jun-17, Jun-26). If routines are cron/trigger-driven, verify the scheduler mechanism has not drifted or missed wake-up events.

**Evidence tier:** STRONG — flagged 3 distinct calendar weeks (May-11, Jun-15, Jun-22) as a recurring pattern. Multiple consecutive missed sessions (May 11–13 = 3 sessions; Jun-17, Jun-26 = 2 more). Risk management (market_open/midday/market_close) still ran in all cases, so no trades were missed. But missing pre_market skips the morning research, thesis updates, and new candidate screen.

**Analytical assessment:**
- Impact: No real-money losses attributable to the gap (risk management continued); but missed research sessions reduce quality of entries and thesis monitoring
- Pattern: The May 11–13 gap is 3 consecutive days (suggests a structural failure, not a one-off). Jun-17 and Jun-26 are isolated (suggests intermittent failures)
- This is an operational issue, not a trading rule change. No backtest applicable.
- Resolution: The Claude Code remote environment schedules runs via triggers. Verifying trigger configuration and adding a heartbeat check (if `plan.md` was not updated today → alert to Discord) would detect future gaps.

**Verdict: RECOMMEND INVESTIGATION — Not a trading rule change; operational reliability improvement. Human action required to verify trigger configuration.**

---

### 🟡 MODERATE Proposals (ranked, not backtested)

---

**M1: Orphan Stop Queue in `market_open`** *(2 weeks: May-11, May-18)*

At the start of every `market_open` run, before any other logic, scan `portfolio.md` for positions missing a `stop_order_id` and place those stops first. Addresses the late-day-fill gap where a fill confirmed after the normal stop-placement window leaves a position unprotected until the next session.

*Documented instance:* CSCO stop placed 1 day late (May 14 fill, stop placed May 15). *Why not STRONG:* Only 1 documented instance; 2 weeks flagged (not 3+). *What would promote to STRONG:* A second documented instance of a same-session overnight gap without stop coverage.

---

**M2: Maximum Concurrent Positions 8 → 10** *(1 week: May-26)*

Raising the max concurrent positions from 8 to 10 to reduce opportunity cost when the book is full with 8/8 and high-conviction setups (PWR, ANET, ETN) are waiting. The existing 11% size cap, 10% cash floor, and 30% sector cap already prevent concentration risk.

*Documented opportunity cost:* May-26 PWR (+35% EPS beat, $48.5B backlog) and ANET (+10.1% beat) blocked by 8/8 cap. *Why not STRONG:* 1 week flagged; potential for over-deployment during hostile regimes if cap is loosened. *What would promote to STRONG:* 2+ more weeks of documented high-conviction-setup displacement, or a backtest showing that 10/8 concurrent would have improved OOS returns without increasing drawdown.

---

**M3: GTC Stop Behavior on Paper Account** *(1 week: Jun-01)*

HPE's GTC stop fired at 16:22 ET (22 min after market close) on the paper account. Evaluate whether to use DAY stops (re-entered each session) instead of GTC stops to avoid unintended after-hours fills on the paper platform.

*Documented instance:* HPE stopped after hours at −8%+, converting an intraday winning position to a max-loss outcome. *Why not STRONG:* 1 week flagged; behavior is paper-account-specific and may not manifest on a live account. *What would promote to STRONG:* A second after-hours stop fire, or confirmation that Alpaca paper consistently fills GTC stops post-close.

---

**M4: Sizing-Correction Process Clarification** *(1 week: Jun-01)*

When a pre_market position sizing calculation uses a different equity basis than the actual open equity (resulting in wrong share count), the correction buy should be logged as part of the original entry with full thesis re-verification. Add explicit share-count validation to `market_open` before submitting any order.

*Documented instance:* HPE initial position undersized ~5% vs 11% target; corrected same session with second buy. *Why not STRONG:* 1 week flagged; the correction process itself worked (HPE stop placed correctly after correction); the issue is documentation quality, not a trading risk. *What would promote to STRONG:* A second instance where the correction introduces a risk gap (e.g., cancellation fails or new stop is missed).

---

### ⚪ WEAK / Not Recommended

---

**W1: Trailing-Stop Pre-Alert at +8% Unrealized** *(1 week: May-11)*

Once any position crosses +8% unrealized, flag in `plan.md` that the +10% trailing-stop trigger is imminent. *Assessment:* The partial profit-lock rule (now implemented in strategy.md) addresses the underlying give-back concern. Additionally, pre_market already notes stop-trigger proximity as part of the thesis audit. Adding a specific +8% pre-alert adds process overhead without a clear edge. *Status:* WEAK — superseded by the partial profit-lock implementation. No action recommended.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported | Apply: tune threshold in compute_pead_health.py |
| 2 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss | Analytical — recommend | Add EDGAR scan to pre_market |
| 3 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions |
| 4 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 | Analytical — recommend | Add CHRONIC_WATCH alert to pre_market |
| 5 | S3 | Wider ATR stop for high-ATR names | 🔴 STRONG | 1 week + MU −$808 | ⚠️ Direction supported, needs full sim | Consider — requires position-size adjustment |
| 6 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks | Operational | Investigate trigger config; add heartbeat check |
| 7 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to market_open |
| 8 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 9 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 10 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to market_open checklist |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |

---

### Notes on this run

- **Data cache:** `backtesting/data_cache/` was empty (`.gitkeep` only). Backtests for S1 (ELEVATED_BAR threshold) and the analytical estimates for S2/S3 used existing candidate CSV files from prior backtest runs in `backtesting/reports/`. No yfinance re-fetch was needed.
- **S3 (wider ATR stop) caveat:** A formal price-path simulation is needed to confirm the OOS verdict. The analytical estimate strongly supports the direction (prior backtest recommendation + OOS high-ATR outperformance + noise-stop rate disparity) but cannot substitute for a trade-level backtest. If the human wants this elevated to a confirmed recommendation, request a full `backtest_atr_stop_vs_flat.py` variant with the cap raised/removed.
- **pead_health.md is STALE:** expires_on 2026-06-28 < today 2026-06-30. The S1 live implication (−0.492% health would not trigger ELEVATED_BAR at −1.0% threshold) is based on the last computed value. The actual health value after recomputing Sunday (Jun-30 or Jul-6 universe_refresh) could be different. Regardless, the backtest finding (OOS performance identical at 0% and −1.0%) is based on historical data and remains valid.
- **Proposals already implemented (not re-recommended):** Same-day cap, macro deferral, partial profit-lock — all confirmed in current `memory/strategy.md`.

---

## 2026-07-04 — Weekly Strategy Review (ad hoc run)

**Run time:** 2026-07-04, invoked ad hoc (off the normal Saturday 10:00 ET cadence)
**Routine:** `strategy_review` (market-independent — no clock gate needed)
**Reconciliation (read-only sanity check):** Alpaca `/v2/positions` = `[]` MATCHES `portfolio.md` FLAT book → 0/0 PASS, zero divergence. Equity $98,266.98 (100% cash).
**pead_health.md status:** Still STALE (`computed_on` 2026-06-21, `expires_on` 2026-06-28 < today). `universe.md` `screened_on` 2026-06-28, `expires_on` 2026-07-05 — the next `universe_refresh` (Sun 2026-07-05 18:00 ET) is the first run since the mandatory pead_health-refresh verification was added (commit 23d9d64) and will be the first live test of that fix.
**New source material since the 2026-06-30 review:** one new `weekly_review` entry — "Week of 2026-06-29" (Mon Jun 29 → Thu Jul 2, committed 2026-07-03, e8ccfdf). Book was FLAT/100% cash the entire week (0 trades, earnings-desert week); portfolio 0.00% vs SPY +2.13% (delta −2.13 pts). No new trade-level evidence (no fills), so no proposal gains a new *documented loss* this run — only carry-forward week-counts and framing updates.

---

### Anti-overfitting counters (Gate 3) — carried forward from 2026-06-30, updated

| Proposal | Times backtested (formal) | Status |
|----------|---------------------------:|--------|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported, not yet applied by human) | Not exhausted |
| S3 — ATR stop, TIGHTER/capped variant (V1) | 1 (2026-06-25, `backtest_report_ATR_STOP_VS_FLAT.md`) — **REJECTED** | Not exhausted (1 rejection < 2), but do not re-test this exact variant again without new evidence |
| S3 — ATR stop, WIDER/uncapped variant (V2, the actual live proposal) | 0 prior → **1 this run** (see below) | Not exhausted |
| All others (S2, S4, S5, S6, M1–M5) | 0 | No formal backtests — procedural/monitoring rules or insufficient evidence tier |

No proposal is EXHAUSTED.

---

### ✅ Already Implemented (additions since 2026-06-30 — moved out of ranking)

*(Items 1–3 — same-day cap, macro deferral, partial profit-lock — remain implemented per the 2026-06-30 entry; not repeated here.)*

4. **Mandatory `pead_health.md` refresh verification** (NEW). `routines/universe_refresh.md` (commit `23d9d64`, 2026-06-30) now reads back `pead_health.md` frontmatter after `compute_pead_health.py` runs and requires `computed_on == today`. On a miss it logs a greppable `PEAD_HEALTH_REFRESH_MISS <date>` line to `research_log.md` and adds a loud, un-buried Discord warning — instead of silently riding a stale overlay for weeks. This directly answers the "fix the partial universe_refresh" proposal escalated in the week-of-2026-06-29 review. **Not yet exercised live**: the last `universe_refresh` (Jun 28) predates this fix; the next run (Sun 2026-07-05) is the first opportunity to confirm it fires as designed. Flag for next `strategy_review` to confirm.

5. **Opening-range entry filter** (NEW). `routines/market_open.md` (commit `e36ad29`, 2026-06-25) added a mandatory OR/ATR check before any new buy: fetch the first three 5-minute bars, compute opening-range width vs 14-day ATR, and defer the entry if the open is "chaotic" (OR width > 0.5×ATR) or price hasn't confirmed above the opening-range high by 09:50 ET. This implements the *entry-timing* half of the recommendation from the week-of-2026-06-22 review (triggered by the MU 2026-06-25 same-day −8% noise stop-out: "...OR barring gap-chase entries... under ELEVATED_BAR"). It does **not** implement the *stop-width* half of that recommendation (S3 below) — those are two independent mitigations for the same root cause, and only one is live.

---

### 🔴 STRONG Proposals — Backtested This Run

---

#### S3 (re-tested): Wider ATR-Scaled Stop for High-ATR Names — the actual proposal, formally backtested for the first time

**Proposal (unchanged from 2026-06-30):** for new entries, use `max(8%, 2×14-day ATR%)` as the initial stop instead of the flat −8%, and shrink the position notional so dollar risk per trade stays roughly constant (`min(11% × equity, 0.8% × equity / stop_pct)`).

**Evidence tier:** STRONG (documented MU −$807.58 same-day noise stop-out, 2026-06-25; now 2 weeks flagged — Jun-22, Jun-29 carry-forward).

**This is a genuinely new backtest, not a re-test of the already-rejected V1.** V1 (`min(8%, max(4%, 2×ATR))`) was a CEILING at 8% — it could only ever be tighter than flat, never wider, and was rejected 2026-06-25. This run built a new script (`backtesting/scripts/backtest_atr_stop_widened.py`) implementing V2 (`max(8%, 2×ATR)`, a FLOOR with no ceiling) — the actual mechanic the proposal and the V1 report itself both called for ("raise/remove the 8% cap"). Ran on the same validated 277-trade candidate set as every other PEAD backtest in this repo, with freshly re-fetched OHLC (Yahoo chart API, same method as `backtest_report_ATR_STOP_VS_FLAT.md`).

**Results (full report: `backtesting/reports/backtest_report_ATR_STOP_WIDENED_V2.md`):**

| Period | Var | Trades | Win% | Avg% | PF | AvgLoss% |
|--------|-----|-------:|-----:|-----:|---:|---------:|
| 2022–2024 (IS) | V0 | 194 | 57.7% | 1.81% | 1.68 | −6.31% |
| 2022–2024 (IS) | V2 | 194 | 58.2% | **1.90%** | **1.72** | −6.46% |
| 2025 (OOS) | V0 | 53 | 49.1% | 1.23% | 1.38 | −6.29% |
| 2025 (OOS) | V2 | 53 | 49.1% | 1.31% | 1.36 | −6.12% |
| 2026 YTD (OOS) | V0 | 30 | 50.0% | −0.23% | 0.95 | −8.24% |
| 2026 YTD (OOS) | V2 | 30 | 50.0% | **−0.55%** | **0.73** | −8.88% |

**Out-of-sample discipline check (mandatory per Step 3c):** Combined OOS (2025+2026, 83 trades): V0 avg **0.70%** / PF **1.20** vs V2 avg **0.64%** / PF **1.08**. **V2 is WORSE out-of-sample.** In-sample it's marginally better (1.90% vs 1.81%, PF 1.72 vs 1.68). This is the textbook in-sample-only-improvement pattern the routine's discipline rule exists to catch.

**Noise-stop mechanism worked as designed, but didn't translate to better OOS P&L:** first-5-day noise-stop rate dropped in every period (2022–24: 4.1%→3.1%; 2025: 7.5%→5.7%; 2026 YTD: 6.7%→3.3%), and on the MU-style high-ATR IT subset (29 trades, mean ATR 4.76%/day) V2 avoided 2 of 3 V0 noise stops and introduced 0 new ones. Position sizing behaved exactly as specified: **100% of these 29 high-ATR trades had V2 notional below the $11k cap** (mean $8,523, range $4,439–$10,000) — the risk-parity downsizing genuinely engaged every time, it never defaulted back to the full $11k. **But** avoiding an early noise stop just delays the exit for names whose thesis was going to fail anyway — those trades go on to hit a wider (more expensive) hard stop or ride out to a worse time-stop exit later, which is visible in the 2026 YTD avg-loss widening from −8.24% to −8.88% and PF collapsing from 0.95 to 0.73. Net effect in the current OOS stretch: fewer noise stops, but each realized loss costs more, and the two effects roughly cancel or net slightly negative.

**Beat-the-benchmark bar:** SPY buy-and-hold was 28.2% (2022–24), 18.0% (2025), 11.1% (2026 YTD, partial). Per-trade avg% figures aren't directly comparable to a compounded index return (these are single-trade returns on ~11% position size, not a fully-invested return), but neither variant's per-trade edge changes that comparison in V2's favor.

**Verdict: ⚠️ NOT ENDORSED — fails the out-of-sample discipline bar.** Full-sample and in-sample results are marginally favorable, but the routine's own rule (Step 3c) requires OOS improvement-or-hold, and OOS here is worse on both avg return (0.64% vs 0.70%) and profit factor (1.08 vs 1.20). This supersedes the 2026-06-30 "direction supported, pending full sim" conditional verdict — the full sim has now been run, and it does not clear the bar. **No `strategy.md` wording is proposed this run** (the MUST NOT list bars endorsing an OOS-negative result).

**Anti-overfitting counter:** S3-V2 (wider/uncapped variant) now has 1 formal backtest (2026-07-04), verdict NOT SUPPORTED. This is a distinct variant from S3-V1 (rejected 2026-06-25) — 1 rejection each, neither is EXHAUSTED (would need 2 rejections on the *same* variant/periods). If a future week brings new evidence (e.g. a different ATR multiplier/cap combination, or a materially larger OOS sample), that would be a new variant eligible for one more test; re-running this exact V2 spec on these same three periods again would not add information and should be treated as EXHAUSTED-equivalent going forward (1 of the "twice" ceiling already used).

---

### 🔴 STRONG — carried forward unchanged from 2026-06-30 (no new trade-level evidence this week; book was FLAT all week)

- **S1 — ELEVATED_BAR realized-health threshold −1.0%.** Verdict unchanged: ✅ BACKTEST SUPPORTS (OOS identical at 0% vs −1.0%, IS quality improves). Still NOT applied by the human — `compute_pead_health.py` `HEALTH_THRESHOLD` constant confirmed still `0.0` this run. No new backtest needed (no new data since Jun-30; re-running the identical test on identical periods would violate the spirit of Gate 3 without adding evidence).
- **S2 — "Never-worked" chronic-underwater monitoring flag.** Analytical support unchanged (GEV −$319.18, CASY −$813.58). No new instance this week (book was flat). Verdict unchanged: recommend implementing the flag.
- **S4 — SEC EDGAR shelf-registration scan.** Unchanged (GOOGL −$413.92 precedent). No new instance this week.
- **S5 — Export-control (BIS) monitoring for semiconductor/IT positions.** Unchanged (AMD/NVDA precedent). No new instance this week.
- **S6 — Missed pre_market scheduler-gap investigation.** Unchanged. No new gap this week (all 4 sessions of the week-of-Jun-29 ran pre_market on schedule per the weekly review).

---

### 🟡 MODERATE Proposals (ranked, not backtested)

- **M1 — Orphan stop queue in `market_open`** *(still 2 weeks: May-11, May-18)* — unchanged; confirmed NOT implemented (no orphan/stop_order_id scan logic found in `routines/market_open.md` this run).
- **M2 — Max concurrent positions 8→10** *(still 1 week: May-26)* — unchanged; `strategy.md` still caps at 8.
- **M3 — GTC stop behavior on paper account** *(still 1 week: Jun-01)* — unchanged.
- **M4 — Sizing-correction process clarification** *(still 1 week: Jun-01)* — unchanged.
- **M5 — Between-seasons secondary entry lane (NEW, 1 week: Jun-29).** From the week-of-2026-06-29 review: the book sat 100% cash through the entire week not because of the ELEVATED_BAR overlay (which was stale→NORMAL, so the standard 15% bar was in effect) but because of a genuine seasonal Q1/Q2 earnings desert — 0 qualifiers even at the lower bar, and the 3 fresh "beats" that did appear (GIS, NKE, MU) were correctly rejected on quality. Proposal: consider using the already-threshold-exempt analyst-revision/partnership-catalyst entry lane more actively between earnings seasons to reduce multi-week 100%-cash stretches. *Why not STRONG:* only 1 week flagged, and the review's own framing hedges it ("...OR accept the desert as by-design — the discipline correctly avoided three low-quality beats that would likely have lost"). This is speculative and not yet evidence of a costly gap (no missed-and-would-have-won trade is documented — GIS/NKE/MU were all correctly rejected for cause). *What would promote to STRONG:* a documented instance of a high-quality analyst-revision/partnership candidate that was available but not researched/traded during a desert stretch, or 2+ more weeks of the same pattern with quantified opportunity cost.

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** — unchanged, superseded by the live partial profit-lock rule.
- **S3 tighter/capped variant (V1)** — REJECTED (backtested 2026-06-25); do not re-test this specific variant. (The wider/uncapped variant V2 is a distinct proposal, tested fresh above — this is not a repeat test of a rejected variant.)

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported (2026-06-30) | Apply: tune threshold in `compute_pead_health.py` — still not applied |
| 2 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss | Analytical — recommend | Add EDGAR scan to `pre_market` |
| 3 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions |
| 4 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 | Analytical — recommend | Add CHRONIC_WATCH alert to `pre_market` |
| 5 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks | Operational | Investigate trigger config; add heartbeat check |
| 6 | S3 | Wider ATR stop (V2) for high-ATR names | 🔴 STRONG | 2 weeks + MU −$808 | ⚠️ **NOT ENDORSED — fails OOS this run** | Do not apply; root-cause (MU noise stop) partially addressed via opening-range filter instead |
| 7 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to `market_open` |
| 8 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 9 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 10 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to `market_open` checklist |
| 11 | M5 | Between-seasons secondary entry lane (NEW) | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence — currently hedged/speculative |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |

*(S3 moves down in rank this run — from #5 conditional to #6 rejected — now that its full-sim OOS result is in. S1/S4/S5/S2/S6 keep their 2026-06-30 ranks unchanged; no new evidence this run.)*

---

### Notes on this run

- This run reused the exact validated candidate set (`backtest_trades_PEAD_2022_2025_ENHANCED_base.csv`, `backtest_trades_PEAD_2026_YTD.csv`) as every other PEAD backtest in the repo, so the entry population is identical across V0/V1/V2 comparisons.
- `backtesting/data_cache/` was empty at the start of this run (per `.gitignore`, per-ticker pickles are never committed); OHLC paths were re-fetched from Yahoo's chart API (same approach validated in `backtest_report_ATR_STOP_VS_FLAT.md`) and are not committed here either.
- New artifacts this run: `backtesting/scripts/backtest_atr_stop_widened.py`, `backtesting/reports/backtest_report_ATR_STOP_WIDENED_V2.md`, `backtesting/reports/backtest_trades_ATR_STOP_V2_widened.csv`, `backtesting/reports/backtest_trades_ATR_STOP_V2_widened_v0.csv`.
- Proposals already implemented (not re-recommended): same-day cap, macro deferral, partial profit-lock (all confirmed since 2026-06-30), plus the two NEW implementations this run (mandatory pead_health refresh verification, opening-range entry filter).

---

## 2026-07-11 — Weekly Strategy Review

**Run time:** Sat 2026-07-11 ~10:07 ET (`Alpaca /v2/clock` `is_open=false`, `next_open` 2026-07-13 — expected for a Saturday, no market dependency for this routine).
**Routine:** `strategy_review` (market-independent — no clock gate needed).
**Reconciliation (read-only sanity check):** Alpaca `/v2/positions` = `[]` MATCHES `memory/portfolio.md` FLAT book (last written by `market_close` 2026-07-10 15:47 ET, reconciled 0/0 PASS at that run too) → **0/0 PASS, zero divergence.**
**pead_health.md status:** Still **STALE** — `computed_on: 2026-06-21`, `expires_on: 2026-06-28` (both < today). `universe.md` is fresh (`screened_on` 2026-07-05, `expires_on` 2026-07-12). See the new dedicated finding below — the staleness now has a diagnosed root cause, not just a recurrence count.
**SPY regime:** not re-derived this run (no new Alpaca bars pulled beyond `/v2/clock`); per the Jul-10 `market_close` log SPY closed the week at $754.94, still firmly above the ~$694 200MA (BULL). Standard `strategy.md` thresholds in effect; `HEALTH_THRESHOLD` in `compute_pead_health.py` confirmed still `0.0` (S1 not yet applied by the human).
**New source material since the 2026-07-04 review:** one new `weekly_review` entry — "Week of 2026-07-06" (Mon Jul 6 → Fri Jul 10, committed `9ae146a`). Book was FLAT/100% cash all 5 sessions (0 fills, earnings-desert continuing into early Q2 season); portfolio 0.00% vs SPY +1.35% (delta −1.35 pts). No new trade-level ($ P&L) evidence this week (no fills), but three substantial **non-lessons** research artifacts landed since the last review and are folded in per Step 1 (this routine reads the whole repo state, not only `lessons.md`, when material bears directly on open proposals): `memory/backtest_risk_sweep_2026-07-08.md` (45-combo entry-quality × stop-width sweep), `memory/stop_audit_2026-07-07.md` (hard-stop outcome audit, 8 stops), and one human edit to `memory/strategy.md` (commit `55e87ed`, "Increase max position size at entry to 20%").

---

### Anti-overfitting counters (Gate 3) — carried forward, updated

| Proposal | Times backtested (formal) | Status |
|----------|---------------------------:|--------|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported, not yet applied by human) | Not exhausted |
| S3 — ATR stop, TIGHTER/capped variant (V1) | 1 (2026-06-25) — REJECTED | Not exhausted (only 1 rejection on this variant), but no new evidence to justify a re-test |
| **S3 — ATR stop, WIDER/uncapped variant (V2)** | **1 (2026-07-04, formal, REJECTED — fails OOS) + 1 (2026-07-08, independent parameter-sweep reproduction, explicitly "CONFIRMS S3; does NOT overturn it") = 2 rejections** | **EXHAUSTED as of this review. Do not re-backtest V2 on the 2022–2024/2025/2026 periods again without a materially new dataset (e.g. a fresh out-of-sample year) or a walk-forward/paper-trading design. Human/manual review only from here.** |
| All others (S2, S4, S5, S6, M1–M5) | 0 formal | No formal backtests — procedural/monitoring rules or insufficient evidence tier |

No *newly*-exhausted proposal this run other than S3-V2. Per Gate 3, S3-V2 is retired from the backtest queue.

---

### ✅ Already Implemented / Resolved (additions since 2026-07-04 — moved out of ranking)

*(Items 1–5 — same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter — remain implemented per the 2026-06-30/2026-07-04 entries; not repeated here.)*

6. **Max position size at entry: sizing-cap discrepancy RESOLVED (was M-adjacent, flagged Jul-06).** `git log -- memory/strategy.md` shows commit `55e87ed` ("Increase max position size at entry to 20%") — a direct human edit to the authoritative file. This confirms **20% is the intended, current value**; the "11%" figure quoted in several operational logs and the `weekly_review` routine text predates this edit and is simply stale prose in already-written log entries, not a live conflict. Per `CLAUDE.md`, `strategy.md` is authoritative and no reconciliation action against it is needed. **Residual note (informational, not actionable by this routine):** future `weekly_review`/`market_open` narrative should cite 20%, not 11%, going forward — this routine cannot edit those routine files (out of scope per its own MUST NOT list) so this is surfaced for the human/maintainer, not applied here.

7. **Mandatory `pead_health.md` refresh-verification — CONFIRMED WORKING LIVE (first real exercise, 2026-07-05).** The 2026-07-04 review noted this fix (`routines/universe_refresh.md` commit `23d9d64`) had not yet been exercised live. It now has: the 2026-07-05 `universe_refresh` run hit a genuine `compute_pead_health.py` failure (`SPY download failed after 5 retries`), and the verification step worked exactly as designed — it read back `pead_health.md`, detected `computed_on` had not advanced, logged a greppable `PEAD_HEALTH_REFRESH_MISS 2026-07-05` line to `memory/research_log.md` with full root-cause detail, and did not silently roll forward. **The detection mechanism is validated and should be considered closed as a distinct proposal.** The underlying transport failure it detected is a separate, still-open issue — see the new finding immediately below.

---

### 🔴 STRONG — new finding this run

---

#### S7 (NEW): `compute_pead_health.py` yfinance/curl_cffi transport failure — root cause now diagnosed, fix path specified

**What changed since the last review:** the Jul-06 `weekly_review` entry carried forward "fix the partial universe_refresh" as an escalated, 2-consecutive-Sunday-miss item. This routine's own read of `memory/research_log.md` (2026-07-05 entry) shows the miss is no longer a mystery — it is fully root-caused:

1. `yfinance` 1.5.1 uses `curl_cffi` (a browser-TLS-fingerprinting HTTP client) which cannot traverse this environment's re-terminating egress proxy — every request dies with `curl:(35) Recv failure: Connection reset by peer` (bypasses the proxy, hits the egress firewall directly).
2. Injecting a plain `requests.Session` into `yf.Ticker(session=...)` **was validated this run as fixing transport** — it does route through the proxy and reach Yahoo.
3. **But** Yahoo now hard-`429`-rate-limits the shared proxy egress IP across every endpoint (v8 chart, getcrumb, quoteSummary) needed for the ~500-ticker EPS-surprise history the realized-health computation requires. The `requests.Session` fix alone is therefore necessary but not sufficient.

**Evidence tier:** Judged **STRONG on an operational (not backtestable) basis** — while this is only the 2nd distinct `lessons.md`-flagged week (Jun-29 "NEW, escalated", Jul-06 "carry-forward, ESCALATED — now 2 consecutive Sunday misses, stale ~3 weeks") and causes no direct $ loss (the overlay fails open/safe to NORMAL), it now has a **named, reproducible root cause and two concrete fix candidates**, which is a materially stronger evidentiary basis than a recurring-but-undiagnosed operational gap. Distinguishing this from **S6** (missed `pre_market` scheduler sessions — a different mechanism, still 3 weeks flagged, no new instance this week since all 5 Jul-06-week sessions ran clean).

**Why not auto-applied:** this is a code/infrastructure fix to `compute_pead_health.py` and/or the egress configuration, not a `strategy.md` rule — outside this routine's scope regardless of tier (this routine's MUST NOT list bars editing any file except `backtesting/strategy_review_log.md`).

**Recommended action (human/maintainer, not this routine):**
> In `compute_pead_health.py`, pass an explicit `requests.Session()` to `yf.Ticker(..., session=...)` (or equivalent) to route yfinance traffic through the proxy instead of `curl_cffi`'s direct egress. This alone will not resolve the current staleness — Yahoo's 429 on the shared egress IP must also be addressed, e.g. by pacing/batching the ~500-ticker fetch, caching EPS-surprise history to avoid re-fetching unchanged prior-quarter data, or relocating the fetch to a non-rate-limited egress path. Until both are fixed, `pead_health.md` will keep missing its weekly refresh and the ELEVATED_BAR/NORMAL overlay will keep riding a stale (currently 3-week-old) reading — safely (fails to NORMAL), but a designed risk control remains effectively offline.

**Verdict: RECOMMEND — root cause and fix path are now well-specified; this is ready for a maintainer to pick up, unlike the vaguer "investigate the scheduler" framing this carried before.**

---

### 🔴 STRONG — carried forward unchanged from 2026-07-04 (no new $-loss evidence this week; book was FLAT all week, 0 fills)

- **S1 — ELEVATED_BAR realized-health threshold −1.0%.** Verdict unchanged: ✅ BACKTEST SUPPORTS. Confirmed **still not applied** by the human — `compute_pead_health.py` `HEALTH_THRESHOLD` constant read directly this run: still `0.0`. No new backtest run (no new data since 2026-06-30; would violate Gate 3's spirit to re-run the identical test on identical periods for no reason).
- **S2 — "Never-worked" chronic-underwater monitoring flag.** Evidence **substantially reinforced** by `memory/stop_audit_2026-07-07.md` (new since last review, n=8 hard-stop cohort): **4 of 8 hard-stop exits (50%) are "chronic never-worked"** (AMZN, PWR, CASY, NVDA-borderline) — closing underwater a median ~75% of holding days with 4–10 consecutive underwater sessions before the mechanical −8% finally fires, cleanly separated from the 2 same-day noise stopouts (HPE, MU) which the audit found do **not** mean-revert either (both kept falling post-stop, contradicting their own contemporaneous "sell-the-news, expect a bounce" trade-log rationale). This is now the single best-evidenced STRONG proposal in the queue even though it remains a monitoring/alerting rule with no formal P&L backtest possible (per its own design — "not auto-cut"). Verdict unchanged: recommend implementing the `CHRONIC_WATCH` flag.
- **S4 — SEC EDGAR shelf-registration scan.** Unchanged (GOOGL −$413.92 precedent). No new instance this week. Note: the stop audit above independently reclassifies the GOOGL stop as "catalyst-contaminated" (bucket E, not a stop-mechanism failure), which if anything strengthens the case for a proactive EDGAR scan as the correct remedy (vs. a stop-width fix, which would not have helped GOOGL).
- **S5 — Export-control (BIS) monitoring for semiconductor/IT positions.** Unchanged (AMD/NVDA precedent). No new instance this week.
- **S6 — Missed `pre_market` scheduler-gap investigation.** Unchanged, still 3 weeks flagged (May-11, Jun-17, Jun-26). **No new gap this week** — the Jul-06 week explicitly confirms all 5 sessions' `pre_market` ran on schedule, extending the clean streak to 2 consecutive weeks (Jun-29 week + Jul-06 week both had 0 gaps). Still open/unresolved (no evidence the scheduler mechanism itself was investigated), but the trend is positive.

---

### 🔴 STRONG — retired this run (EXHAUSTED, do not re-test)

- **S3 — Wider/uncapped ATR stop (V2), `max(8%, 2×ATR)`.** Independently reproduced by `memory/backtest_risk_sweep_2026-07-08.md` §4 (a 45-combo entry-quality × stop-width sweep run for an unrelated purpose — testing whether loosening entry filters changes the S3 verdict): explicit finding **"Verdict — CONFIRMS S3; does NOT overturn it."** On S3's own OOS window (2025+2026) at the current entry bar, flat −8% still beats 2.0×ATR (0.70% vs 0.64% avg, reproduced exactly from the 2026-07-04 test); across all 9 looser entry-bar combinations tested, the ATR variant's edge appears even at the *current* (unloosened) bar (so it isn't a loosening effect) and reverses on the 2026 slice. Fixed wider stops (−10%/−12%) are worse OOS at 7 of 9 bars, the classic in-sample-only overfit signature. **This is a second independent rejection of the same variant on the same periods** (2026-07-04 formal test + 2026-07-08 sweep reproduction) → **EXHAUSTED per Gate 3.** No `strategy.md` wording proposed. Do not re-test this variant again absent a materially new dataset or a walk-forward design.
- Also newly relevant: `memory/stop_audit_2026-07-07.md` independently concludes (its own words) **"None of this supports 'widen the stop' or 'the stop is broken' as a conclusion"** — a third, qualitative line of evidence pointing the same direction (chronic never-worked and catalyst-contamination, not volatility-driven noise stops, are the dominant hard-stop failure mode; see S2/S4 above for the corresponding remedies).

---

### 🟡 MODERATE Proposals (ranked, not backtested)

- **M1 — Orphan stop queue in `market_open`** *(still 2 weeks: May-11, May-18)* — unchanged; not implemented.
- **M2 — Max concurrent positions 8→10** *(still 1 week: May-26)* — unchanged; `strategy.md` still caps at 8.
- **M3 — GTC stop behavior on paper account** *(still 1 week: Jun-01)* — unchanged.
- **M4 — Sizing-correction process clarification** *(still 1 week: Jun-01)* — unchanged.
- **M5 — Between-seasons secondary entry lane** *(now 2 weeks: Jun-29, Jul-06)* — the Jul-06 week again saw a full 5-session earnings-desert week with 0 qualifiers (LEVI/PEP/DAL all correctly rejected on quality, not bar height). Cross-reference: `memory/backtest_risk_sweep_2026-07-08.md` independently confirms the *primary*-lane EPS/score bar should **not** be loosened (loosening overfits — raises raw OOS return but blows out MaxDD from ~−6% to −27%/−48% and consecutive losses from 5→14-22), which is indirect supporting evidence that M5's proposed remedy (lean more on the already-threshold-exempt secondary lane, not loosen the primary bar) is the more defensible lever if the human wants to address the cash-drag pattern. *Why still not STRONG:* no documented instance yet of a specific missed secondary-lane candidate (analyst-revision/partnership catalyst) that would have qualified and won — still speculative. *What would promote to STRONG:* one concrete missed-candidate instance, or a third consecutive week of the same desert pattern.

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** — unchanged, superseded by the live partial profit-lock rule.
- **S3-V1 (tighter/capped variant)** — REJECTED (2026-06-25); unchanged, 1 rejection, not re-tested.
- **S3-V2 (wider/uncapped variant)** — **NEWLY EXHAUSTED this run** (2 rejections: 2026-07-04 formal + 2026-07-08 independent reproduction). See STRONG-retired section above for full detail.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported (2026-06-30) | Apply: tune threshold in `compute_pead_health.py` — still not applied |
| 2 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 + NEW: 50% of all hard-stops are chronic per stop-audit | Analytical — recommend | Add `CHRONIC_WATCH` alert to `pre_market` |
| 3 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss (now reclassified catalyst-contaminated, strengthening the case) | Analytical — recommend | Add EDGAR scan to `pre_market` |
| 4 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions |
| 5 | S7 | Fix `compute_pead_health.py` yfinance transport + Yahoo 429 (NEW) | 🔴 STRONG (operational) | 2 weeks + root cause now diagnosed | N/A — infra fix | Inject `requests.Session`; pace/relocate egress off the rate-limited IP |
| 6 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks, 0 new (2 clean weeks running) | Operational | Investigate trigger config; add heartbeat check |
| 7 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to `market_open` |
| 8 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 9 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 10 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to `market_open` checklist |
| 11 | M5 | Between-seasons secondary entry lane | 🟡 MODERATE | 2 weeks | Not backtested (indirect support from Jul-08 sweep) | Wait for a concrete missed-candidate instance |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |
| — | S3-V1 | ATR stop, tighter/capped | ⚪ EXHAUSTED-adjacent | 1 rejection | Rejected 2026-06-25 | No re-test |
| — | S3-V2 | ATR stop, wider/uncapped | ⚪ **EXHAUSTED (NEW)** | 2 rejections | Rejected 2026-07-04 + confirmed 2026-07-08 | **Do not re-test — human/manual review only** |

*(S3-V2 drops out of the active STRONG queue entirely this run — moved to EXHAUSTED. S2 moves up to #2 on the strength of the new stop-audit evidence. S7 is newly added at #5. S1/S4/S5/S6 keep their relative order with evidence updates as noted.)*

---

### Notes on this run

- **No fills, no new $ P&L evidence this week** (book FLAT all 5 sessions, per the Jul-06 `weekly_review` entry) — this run's new material came entirely from (a) one human edit to `strategy.md` (sizing cap, now resolved/confirmed) and (b) three ad-hoc research artifacts committed by other sessions since 2026-07-04 (`backtest_risk_sweep_2026-07-08.md`, `stop_audit_2026-07-07.md`, and the `research_log.md` PEAD_HEALTH_REFRESH_MISS root-cause entry) that this routine is required to cross-check against open proposals per Step 1/Step 2 even when they didn't originate as a `weekly_review` "Proposed rule changes" bullet.
- **`backtesting/data_cache/` remains empty** (per `.gitignore` — per-ticker pickles are never committed); no new fetch was needed this run since no new formal backtest was warranted (S3-V2 is now EXHAUSTED, S1 unchanged, nothing else crossed into STRONG-needing-a-backtest this week).
- **pead_health.md is STALE and now root-caused (S7)** — this is a genuine, unresolved gap in a designed risk control, now 3 consecutive missed Sunday refreshes (last good compute 2026-06-21). Escalate this to the human alongside S1 (both touch the same file/mechanism: S1 changes the threshold `compute_pead_health.py` compares against; S7 fixes why the script keeps failing to run at all). Fixing S7 without S1 leaves the untuned 0.0% threshold in place once data starts flowing again; fixing S1 without S7 has no effect until the script can actually compute a fresh reading.
- Proposals already implemented (not re-recommended): same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification (now confirmed working live), opening-range entry filter (all confirmed since 2026-06-30/07-04), plus the sizing-cap discrepancy resolved this run (confirmed 20% is the human-intended value per direct `strategy.md` commit).

---

## 2026-07-18 — Weekly Strategy Review

**Run time:** Sat 2026-07-18 ~10:00 ET (market-independent — no clock gate needed for this routine).
**Routine:** `strategy_review`.
**Reconciliation (read-only sanity check):** Alpaca `GET /v2/positions` = `[]` MATCHES `memory/portfolio.md` FLAT book (last written by `market_close` 2026-07-17, itself 0/0 PASS) → **0/0 PASS, zero divergence.**
**pead_health.md status:** Still **STALE** — `computed_on: 2026-06-21`, `expires_on: 2026-06-28` (both far < today). Per `portfolio.md` Jul-17 close note, this is now the **8th+ consecutive session** (4th consecutive Sunday `universe_refresh`: Jun-28, Jul-05, Jul-12) that `compute_pead_health.py` failed to recompute — root cause unchanged from S7 (yfinance `curl_cffi` vs. agent-proxy transport + Yahoo 429 on shared egress IP). Fails safe to NORMAL; standard 15% bar in effect.
**SPY regime:** not re-derived this run (no new Alpaca bars pulled beyond the reconciliation call); per the Jul-17 `market_close` log SPY closed the week at $743.70/$743.28, still comfortably above the ~$684–694 200MA region last computed → **BULL**. `HEALTH_THRESHOLD` in `compute_pead_health.py` confirmed still `0.0` this run (S1 not yet applied by the human).
**New source material since the 2026-07-11 review:** one new `weekly_review` entry — "Week of 2026-07-13" (commit `098d9bb`). Book was FLAT/100% cash all 5 sessions (0 fills); portfolio **0.00%** vs SPY **−1.54%** (**+1.54 pts, OUTPERFORMED** — the first week in the current cash streak where sitting out helped rather than hurt). No new trade-level ($ P&L) evidence (no fills, no stops, no realized loss), so no existing STRONG proposal gains new *loss* evidence this run. The one substantive new item is an execution-layer observation, assessed as S8 below.

---

### Anti-overfitting counters (Gate 3) — carried forward, unchanged

| Proposal | Times backtested (formal) | Status |
|----------|---------------------------:|--------|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported, not yet applied by human) | Not exhausted |
| S3 — ATR stop, TIGHTER/capped variant (V1) | 1 (2026-06-25) — REJECTED | Not exhausted, but no new evidence to justify a re-test |
| S3 — ATR stop, WIDER/uncapped variant (V2) | 2 (2026-07-04 formal + 2026-07-08 independent sweep reproduction) — **EXHAUSTED** | Do not re-test on the 2022–2024/2025/2026 periods without a materially new dataset or a walk-forward design |
| All others (S2, S4, S5, S6, S7, M1–M5) | 0 formal | Procedural/monitoring rules or insufficient evidence tier — no formal backtest warranted |

No newly-exhausted proposal this run; no proposal crossed into STRONG-needing-a-backtest (see Step 4 note below).

---

### ✅ Already Implemented (unchanged — confirms the loop is closing)

1. Same-day open+close counts toward weekly new-position cap.
2. Macro deferral rule (futures/10yr-yield stress → 20% EPS bar for the day).
3. Partial profit-lock at +10% trigger (sell 1/3, trail remaining 2/3 at 7%).
4. Mandatory `pead_health.md` refresh verification in `universe_refresh` (confirmed working live — correctly logged `PEAD_HEALTH_REFRESH_MISS` every week since 2026-07-05, most recently Jul-12).
5. Opening-range entry filter (Gate 6) in `market_open`.
6. Max position size at entry — 20% (human commit `55e87ed`; confirmed live in practice again this week, GS sized at ~10.2% < 20% cap before every one of its 3 defers).

---

### 🔴 STRONG Proposals

*(No proposal crossed into "needs a fresh backtest" this run — S1's OOS-supported result stands from 2026-06-30 with no new data to re-test against; S3-V2 is EXHAUSTED; everything else below is procedural/analytical, carried forward with this week's evidence check.)*

- **S1 — ELEVATED_BAR realized-health threshold −1.0%.** Verdict unchanged: ✅ BACKTEST SUPPORTS (OOS 2025–2026 identical at 0% vs −1.0%: 52 trades, 2.0% avg, PF 1.62; IS 2022–2024 quality improves 1.89% vs 1.77%). **Still not applied** — `HEALTH_THRESHOLD` confirmed `0.0` this run. No re-backtest (no new data since 2026-06-30).
- **S2 — "Never-worked" chronic-underwater monitoring flag.** Unchanged — GEV −$319.18, CASY −$813.58, plus the `stop_audit_2026-07-07.md` finding that 50% of all hard-stops are chronic. No new instance this week (book flat, 0 fills). Verdict unchanged: recommend implementing the `CHRONIC_WATCH` flag in `pre_market`.
- **S4 — SEC EDGAR shelf-registration scan.** Unchanged (GOOGL −$413.92 precedent). No new instance this week.
- **S5 — Export-control (BIS) monitoring for semiconductor/IT positions.** Unchanged (AMD/NVDA precedent). No new instance this week.
- **S6 — Missed `pre_market` scheduler-gap investigation.** Unchanged, still 3 weeks originally flagged (May-11, Jun-17, Jun-26) — but **now 3 consecutive clean weeks running** (Jun-29, Jul-06, Jul-13 all ran all 5 sessions on schedule). The trend continues to be positive, but the underlying scheduler mechanism was never actually investigated/confirmed fixed — a clean streak is not the same as a diagnosed root cause. Keep open at STRONG tier (documented historical evidence stands) but note the risk of the issue quietly recurring is lower than it looked in June.
- **S7 — `compute_pead_health.py` yfinance/curl_cffi transport failure.** Unchanged and **escalating**: now a 4th consecutive Sunday miss (Jun-28, Jul-05, Jul-12), 8th+ consecutive session flagging it per `portfolio.md`. Root cause and fix path remain as specified 2026-07-11 (inject `requests.Session` into `yf.Ticker`; separately address Yahoo's 429 on the shared egress IP via pacing/caching/relocation). This is now the longest-running unresolved item in the queue and the routine's read-only view cannot fix it (code/infra change, out of this routine's scope). Recommend the human prioritize this alongside S1 — S1 has no effect until S7 restores fresh health data.

---

### 🟡 MODERATE Proposals (ranked, not backtested)

- **M1 — Orphan stop queue in `market_open`** *(still 2 weeks: May-11, May-18)* — unchanged; not implemented.
- **M2 — Max concurrent positions 8→10** *(still 1 week: May-26)* — unchanged; `strategy.md` still caps at 8.
- **M3 — GTC stop behavior on paper account** *(still 1 week: Jun-01)* — unchanged.
- **M4 — Sizing-correction process clarification** *(still 1 week: Jun-01)* — unchanged.
- **M5 — Between-seasons secondary entry lane** *(still 2 weeks: Jun-29, Jul-06)* — no new instance this week; GS was a primary-lane (earnings-driven) qualifier, not a secondary-lane one, so it neither promotes nor contradicts M5.
- **S8 (NEW): Review the intraday execution micro-gates vs. fresh-print PEAD entries.** From the week-of-2026-07-13 review: Gate 6d (opening-range width > 0.5×ATR) and Gate 4 (price < 21-day EMA) deferred the week's only qualifier — GS, a +45.1% EPS beat / 5-quarter streak / record quarter — on 3 consecutive sessions (Jul-15, Jul-16, Jul-17), extending the cash streak with a valid signal in hand never filled. **Tiering call (explicit, since `lessons.md` framed this as "the headline of the week"):** this is scored **MODERATE, not STRONG**, because none of the three STRONG criteria in Gate 3/Step 3 are met yet — it has been flagged in only **1** distinct week (not 3+), there is **no backtest** behind it, and GS was never filled so there is **no documented real-money loss** (this is an opportunity-cost/give-up, not a realized loss — distinguishable from S2/S4/S5 which each have a concrete $-loss precedent). The reasoning in the underlying weekly_review entry is sound and the tension it identifies (fresh-print PEAD names structurally trip opening-range and EMA guards in the exact window drift is strongest) is a real one worth tracking. *What would promote to STRONG:* a second distinct week where a comparable high-conviction fresh-print qualifier is deferred by the same gates, OR a lightweight backtest quantifying the drift given up across historical Gate-6d/Gate-4 defers on qualifying signals, OR a documented instance where the deferred name would have been profitable had it filled (turning opportunity cost into a quantifiable number). Until then: monitor, do not act.

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** — unchanged, superseded by the live partial profit-lock rule.
- **S3-V1 — ATR stop, tighter/capped variant** — REJECTED (2026-06-25); 1 rejection, not re-tested.
- **S3-V2 — ATR stop, wider/uncapped variant** — **EXHAUSTED** (2 rejections: 2026-07-04 formal + 2026-07-08 independent reproduction). Do not re-test without a materially new dataset.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported (2026-06-30) | Apply: tune threshold in `compute_pead_health.py` — still not applied |
| 2 | S7 | Fix `compute_pead_health.py` yfinance transport + Yahoo 429 | 🔴 STRONG (operational) | 4 consecutive Sunday misses, root cause diagnosed | N/A — infra fix | Inject `requests.Session`; pace/relocate egress off the rate-limited IP. Blocks S1 from mattering until fixed. |
| 3 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 + 50% of all hard-stops chronic (stop-audit) | Analytical — recommend | Add `CHRONIC_WATCH` alert to `pre_market` |
| 4 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss | Analytical — recommend | Add EDGAR scan to `pre_market` |
| 5 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions |
| 6 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks, now 3 consecutive clean weeks | Operational | Investigate trigger config to confirm root cause; risk trending down but unconfirmed |
| 7 | S8 | Execution micro-gates vs fresh-print entries (NEW) | 🟡 MODERATE | 1 week, opportunity cost only, no realized loss | Not backtested | Monitor for a 2nd instance or quantify give-up before acting |
| 8 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to `market_open` |
| 9 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 10 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 11 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to `market_open` checklist |
| 12 | M5 | Between-seasons secondary entry lane | 🟡 MODERATE | 2 weeks | Not backtested | Wait for a concrete missed-candidate instance |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |
| — | S3-V1 | ATR stop, tighter/capped | ⚪ Rejected | 1 rejection | Rejected 2026-06-25 | No re-test |
| — | S3-V2 | ATR stop, wider/uncapped | ⚪ **EXHAUSTED** | 2 rejections | Rejected 2026-07-04 + confirmed 2026-07-08 | Do not re-test — human/manual review only |

*(S7 moves up to #2 this run given its escalating duration and the fact it structurally blocks S1 from having any effect. S1/S2/S4/S5/S6 keep their relative standing. S8 enters at #7 as MODERATE, not STRONG — see tiering rationale above.)*

---

### Notes on this run

- **No fills, no new $ P&L evidence this week** (book FLAT all 5 sessions, per the Jul-13 `weekly_review` entry, commit `098d9bb`) — the only new material this run is the execution-micro-gate observation (S8) and the continued escalation of the pead_health staleness (S7).
- **No formal backtest was run this session.** Per Step 4/Gate 3, backtesting is reserved for STRONG proposals with a mechanical rule to test: S1 already has a standing OOS-supported result with no new data to re-test against; S3-V2 is EXHAUSTED; S2/S4/S5/S6/S7 are procedural/monitoring rules with no mechanical backtest possible; S8 is MODERATE and per the routine's own MUST NOT list, MODERATE proposals are not backtested.
- **`backtesting/data_cache/` remains empty** (per `.gitignore`); no fetch was needed this run.
- **Reconciliation:** Alpaca `/v2/positions` = `[]` matches `portfolio.md`'s FLAT book — 0/0 PASS, zero divergence (read-only sanity check per Gate 2; this routine does not own reconciliation and would not abort even on a mismatch).
- **Escalation flag for the human:** S1 and S7 are coupled — S7 (transport fix) must land before S1 (threshold retune) can have any live effect, since `compute_pead_health.py` cannot produce a fresh reading until the transport issue is fixed. Both remain the two highest-value, lowest-risk items in the queue and neither has been applied yet.
- Proposals already implemented (not re-recommended): same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter, sizing-cap discrepancy resolution (20%) — all confirmed unchanged since prior reviews.

---

## 2026-07-25 — Weekly Strategy Review

**Run time:** Sat 2026-07-25 ~10:00 ET (market-independent — no clock gate needed for this routine).
**Routine:** `strategy_review`.
**Reconciliation (read-only sanity check):** `GET /v2/positions` = `[]` MATCHES `memory/portfolio.md` FLAT book (last written by `market_close` 2026-07-24, itself 0/0 PASS) → **0/0 PASS, zero divergence.**
**pead_health.md status:** **FRESH & NORMAL** — `computed_on: 2026-07-19`, `expires_on: 2026-07-26` (both current), `realized_health_60d +1.225%`, `n=318`, `health_ok=true`. This is the first review to run since the transport fix landed (2026-07-19) — see S7 resolution below.
**SPY regime:** BULL per the most recent computed reading (Jul 21 close $748.155 > 200MA $693.44, +7.9%); `HEALTH_THRESHOLD` in `compute_pead_health.py` confirmed still `0.0` this run (S1 not yet applied by the human).
**New source material since the 2026-07-18 review:** one new `weekly_review` entry — "Week of 2026-07-20" (commit `31cc641`). Book was FLAT/100% cash all 5 sessions (0 fills); portfolio **0.00%** vs SPY **−0.59%** (**+0.59 pts, OUTPERFORMED**). No new trade-level ($ P&L) evidence this run (no fills, no stops). Two substantive developments: (1) the `pead_health.md` staleness bug (S7) is now confirmed fixed and live (Jul-19 `universe_refresh`, commit `f3b3d74`, root cause: yfinance `curl_cffi` vs. the TLS-re-terminating proxy — fixed via `YF_DISABLE_CURL_CFFI=1`); (2) INTC reported a ~+100% Q2 EPS beat Jul 23 AC, deferred day-0 (incomplete a–i, 0 completed drift days), and is flagged `#1 priority for Mon Jul 27 pre_market` — a high-ATR semiconductor name that will simultaneously test the (already-EXHAUSTED) wider-ATR-stop proposal and the (still-MODERATE) execution-micro-gate proposal once it re-screens.

---

### Anti-overfitting counters (Gate 3) — carried forward, unchanged

| Proposal | Times backtested (formal) | Status |
|----------|---------------------------:|--------|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported, not yet applied by human) | Not exhausted |
| S3 — ATR stop, TIGHTER/capped variant (V1) | 1 (2026-06-25) — REJECTED | Not exhausted, but no new evidence to justify a re-test |
| S3 — ATR stop, WIDER/uncapped variant (V2) | 2 (2026-07-04 formal + 2026-07-08 independent sweep reproduction) — **EXHAUSTED** | Do not re-test on the 2022–2024/2025/2026 periods without a materially new dataset or a walk-forward design |
| All others (S2, S4, S5, S6, S8, M1–M5) | 0 formal | Procedural/monitoring rules or insufficient evidence tier — no formal backtest warranted |

No newly-exhausted proposal this run; no proposal crossed into STRONG-needing-a-backtest (no new mechanical-rule evidence this week — see Step 4 note below). **S7 is retired from the queue entirely this run (RESOLVED, not exhausted)** — it was an infra/operational fix, never a backtestable mechanical rule, and it is now confirmed shipped and working.

---

### ✅ Already Implemented / Resolved (additions since 2026-07-18 — moved out of ranking)

*(Items 1–6 — same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter, max position size 20% — remain implemented per prior entries; not repeated here.)*

7. **S7 RESOLVED — `compute_pead_health.py` yfinance/curl_cffi transport failure, fixed and confirmed live.** The 2026-07-19 `universe_refresh` (commit `f3b3d74`) applied `YF_DISABLE_CURL_CFFI=1` (+ `lxml`) so yfinance routes through the plain-`requests` fallback instead of `curl_cffi`, which the agent proxy was resetting. Effect verified directly: `pead_health.md` now shows `computed_on: 2026-07-19`, posture flipped **ELEVATED_BAR → NORMAL** (realized_health_60d +1.225%, n=318, health_ok=true), and it remained the live, unexpired reading through the entire week of 2026-07-20 → 2026-07-24 (expires 2026-07-26). This closes out the item that was escalating for 6+ consecutive weeks (Jun-29 → Jul-18). **Residual note (informational, human/maintainer action, not this routine's scope):** the fix so far is a runtime env var (`YF_DISABLE_CURL_CFFI=1`), not a committed code change — confirm it is set as a durable environment variable in the routine's execution environment (not just exported ad hoc in the session that applied it on Jul-19) so it survives a fresh container/session. If the routine environment resets the var, this bug will silently recur.

---

### 🔴 STRONG Proposals — carried forward unchanged (no new $-loss evidence this week; book was FLAT all week, 0 fills)

- **S1 — ELEVATED_BAR realized-health threshold −1.0%.** Verdict unchanged: ✅ BACKTEST SUPPORTS (OOS 2025–2026 identical at 0% vs −1.0%: 52 trades, 2.0% avg, PF 1.62; IS 2022–2024 quality improves 1.89% vs 1.77%). **Still not applied** — `HEALTH_THRESHOLD` confirmed `0.0` this run. **Status change: now UNBLOCKED** — with S7 resolved and `pead_health.md` producing fresh weekly readings again, applying this threshold would take live effect for the first time since it was recommended (2026-06-30). No re-backtest (no new data since 2026-06-30; re-running the identical test on identical periods would add no information). This and S7-durability (above) are jointly the two highest-priority items for the human this week.
- **S2 — "Never-worked" chronic-underwater monitoring flag.** Unchanged — GEV −$319.18, CASY −$813.58, plus the `stop_audit_2026-07-07.md` finding that 50% of all hard-stops are chronic. No new instance this week (book flat, 0 fills, no open positions to ever go chronic). Verdict unchanged: recommend implementing the `CHRONIC_WATCH` flag in `pre_market`.
- **S4 — SEC EDGAR shelf-registration scan.** Unchanged (GOOGL −$413.92 precedent). No new instance this week.
- **S5 — Export-control (BIS) monitoring for semiconductor/IT positions.** Unchanged (AMD/NVDA precedent). No new instance this week. **Directly relevant next week:** if INTC (a semiconductor name) is entered Monday per its #1-priority flag, this scan would apply to it as an open position.
- **S6 — Missed `pre_market` scheduler-gap investigation.** Unchanged, still 3 weeks originally flagged (May-11, Jun-17, Jun-26) — now **4 consecutive clean weeks running** (Jun-29, Jul-06, Jul-13, Jul-20 all ran all 5 sessions on schedule per commit history and each week's `weekly_review`). The underlying scheduler mechanism was still never actually investigated/root-caused, so this stays open at STRONG tier on its historical evidence, but the live recurrence risk continues to look lower than it did in June.

---

### 🟡 MODERATE Proposals (ranked, not backtested)

- **M1 — Orphan stop queue in `market_open`** *(still 2 weeks: May-11, May-18)* — unchanged; not implemented.
- **M2 — Max concurrent positions 8→10** *(still 1 week: May-26)* — unchanged; `strategy.md` still caps at 8.
- **M3 — GTC stop behavior on paper account** *(still 1 week: Jun-01)* — unchanged.
- **M4 — Sizing-correction process clarification** *(still 1 week: Jun-01)* — unchanged.
- **M5 — Between-seasons secondary entry lane** *(still 2 weeks: Jun-29, Jul-06)* — no new instance this week; this week's rejections (COF, GM, TRV, BLK, TFC, ISRG) were all primary-lane earnings-driven candidates correctly rejected on quality, not a desert/secondary-lane situation.
- **S8 — Execution micro-gates vs. fresh-print PEAD entries** *(still 1 week: Jul-13, GS precedent)* — unchanged; no new instance this week. INTC was deferred day-0 for incomplete a–i (0 completed drift days), which is a different mechanism than the Gate 6d/Gate 4 defers that hit GS — so this week does NOT count as a second flag. **However, INTC is a live, explicitly-flagged setup for Monday 2026-07-27**, and if it clears the primary screen and then gets deferred by Gate 6d (chaotic opening range) or Gate 4 (21-day EMA) the way GS was, that would be the second distinct-week instance needed to promote S8 to STRONG. Watch directly next review.

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** — unchanged, superseded by the live partial profit-lock rule.
- **S3-V1 — ATR stop, tighter/capped variant** — REJECTED (2026-06-25); 1 rejection, not re-tested.
- **S3-V2 — ATR stop, wider/uncapped variant** — **EXHAUSTED** (2 rejections: 2026-07-04 formal + 2026-07-08 independent reproduction). Do not re-test without a materially new dataset. **Relevant next week:** if INTC enters and its ATR is high, per this EXHAUSTED verdict the flat −8% stop should still be used as-is — do not improvise a wider stop on the fly; the backtest evidence says it doesn't help OOS.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported (2026-06-30); **now unblocked (S7 resolved)** | Apply: tune threshold in `compute_pead_health.py` — still not applied, now would take live effect |
| 2 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 + 50% of all hard-stops chronic (stop-audit) | Analytical — recommend | Add `CHRONIC_WATCH` alert to `pre_market` |
| 3 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss | Analytical — recommend | Add EDGAR scan to `pre_market` |
| 4 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions — directly relevant if INTC enters |
| 5 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks, now 4 consecutive clean weeks | Operational | Investigate trigger config to confirm root cause; risk trending down but unconfirmed |
| 6 | S8 | Execution micro-gates vs fresh-print entries | 🟡 MODERATE | 1 week, opportunity cost only, no realized loss | Not backtested | INTC Monday is the live test for a 2nd instance |
| 7 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to `market_open` |
| 8 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 9 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 10 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to `market_open` checklist |
| 11 | M5 | Between-seasons secondary entry lane | 🟡 MODERATE | 2 weeks | Not backtested | Wait for a concrete missed-candidate instance |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |
| — | S3-V1 | ATR stop, tighter/capped | ⚪ Rejected | 1 rejection | Rejected 2026-06-25 | No re-test |
| — | S3-V2 | ATR stop, wider/uncapped | ⚪ **EXHAUSTED** | 2 rejections | Rejected 2026-07-04 + confirmed 2026-07-08 | Do not re-test — human/manual review only; use flat −8% on INTC |
| — | S7 | pead_health transport fix | ✅ **RESOLVED (moved to Already Implemented)** | — | — | Confirm `YF_DISABLE_CURL_CFFI=1` is durably set in the environment |

*(S7 exits the ranked queue entirely this run — moved to Already Implemented. S1 moves up to #1 given it is now unblocked and actionable for the first time since 2026-06-30 — S2/S4/S5/S6 hold their relative order. S8 remains MODERATE at #6, one live instance away from promotion.)*

---

### Notes on this run

- **No fills, no new $ P&L evidence this week** (book FLAT all 5 sessions, per the Jul-20 `weekly_review` entry, commit `31cc641`) — the substantive developments this run are the S7 resolution (confirmed via direct read of `pead_health.md` frontmatter) and the forward-looking INTC flag, which does not yet promote either S3 (EXHAUSTED, stays retired) or S8 (still only 1 week) but is worth watching at the next review.
- **No formal backtest was run this session.** Per Step 4/Gate 3, backtesting is reserved for STRONG proposals with a mechanical rule to test: S1 already has a standing OOS-supported result with no new data to re-test against; S3-V2 is EXHAUSTED; S2/S4/S5/S6 are procedural/monitoring rules with no mechanical backtest possible; S8 is MODERATE and per the routine's own MUST NOT list, MODERATE proposals are not backtested.
- **`backtesting/data_cache/` remains empty** (per `.gitignore`); no fetch was needed this run. `backtesting/scripts/` has no new scripts since the 2026-07-18 review (confirmed via `git log` on the directory).
- **Reconciliation:** `GET /v2/positions` = `[]` matches `memory/portfolio.md`'s FLAT book — 0/0 PASS, zero divergence (read-only sanity check per Gate 2; this routine does not own reconciliation and would not abort even on a mismatch).
- **`memory/strategy.md` unchanged** since the last human edit (commit `55e87ed`, sizing cap to 20%) — confirmed via `git log -- memory/strategy.md`; no new proposal has been applied by the human this week, so S1/S2/S4/S5/S6/S8 all remain open exactly as ranked above.
- Proposals already implemented (not re-recommended): same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter, sizing-cap discrepancy resolution (20%), and (NEW this run) the pead_health transport fix (S7) — all confirmed unchanged/resolved since prior reviews.

---

## 2026-08-01 — Weekly Strategy Review

**Run time:** Sat 2026-08-01 ~14:15 ET (market-independent — no clock gate needed for this routine).
**Routine:** `strategy_review`.
**Reconciliation (read-only sanity check):** `GET /v2/positions` = `[]` MATCHES `memory/portfolio.md` FLAT book (last written by `market_close` 2026-07-31, itself 0/0 PASS) → **0/0 PASS, zero divergence.**
**pead_health.md status:** **STALE — REGRESSED.** `computed_on: 2026-07-19`, `expires_on: 2026-07-26` — both now 6+ days past expiry (today 2026-08-01). Confirmed by direct read of the file's frontmatter this run. This **reverses last week's "S7 RESOLVED" call** — see S7 below.
**SPY regime:** not re-derived this run (no new Alpaca bars pulled beyond reconciliation); per the last computed reading (Jul 21 close $748.155 > 200MA $693.44) and the Jul-31 `market_close` log (SPY $746.79), still comfortably **BULL**. `HEALTH_THRESHOLD` in `compute_pead_health.py` confirmed still `0.0` this run (S1 not yet applied by the human).
**`memory/strategy.md`:** unchanged since the last human edit (still 20% sizing cap, 8 concurrent, 5/week base cap) — content matches the prior review's confirmed state; no new human edit this week.
**New source material since the 2026-07-25 review:** one new `weekly_review` entry — "Week of 2026-07-27" (commit `a6fce3a`, Mon Jul 27 → Fri Jul 31). Book was FLAT/100% cash all 5 sessions (0 fills); portfolio **0.00%** vs SPY **+1.07%** (**−1.07 pts, UNDERPERFORMED**). Two substantive developments this run:
1. **After a ~5-week 0-qualifier drought, PWR and AMZN both cleared the fundamental screen Jul 31 — the first buys planned since the MU stop-out Jun 25 — and BOTH were deferred at market_open by the intraday execution micro-gates (Gate 6d/6e).** This is the second distinct-week instance of the same gate family blocking fresh-print qualifiers (GS 3× the week of Jul-13, now PWR+AMZN together Jul-31) and crosses the proposal into STRONG tier for the first time (see S8 below).
2. **The `pead_health.md` transport fix (S7) did not survive into a fresh environment** — the Jul-26 `universe_refresh` rebuilt `universe.md` but did not recompute `pead_health.md` (still shows `computed_on: 2026-07-19`), because `YF_DISABLE_CURL_CFFI=1` was applied at runtime only, not durably. Confirmed independently this run via direct file read (see pead_health.md status above). This reopens S7.

---

### Anti-overfitting counters (Gate 3) — carried forward, unchanged

| Proposal | Times backtested (formal) | Status |
|----------|---------------------------:|--------|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported, not yet applied by human) | Not exhausted |
| S3 — ATR stop, TIGHTER/capped variant (V1) | 1 (2026-06-25) — REJECTED | Not exhausted, but no new evidence to justify a re-test |
| S3 — ATR stop, WIDER/uncapped variant (V2) | 2 (2026-07-04 formal + 2026-07-08 independent sweep reproduction) — **EXHAUSTED** | Do not re-test on the 2022–2024/2025/2026 periods without a materially new dataset or a walk-forward design |
| All others (S2, S4, S5, S6, S7, S8, M1–M5) | 0 formal | Procedural/monitoring rules, operational fix, or a mechanism with no daily-bar-backtestable proxy (S8 — see Step 4 note below) |

**⚠️ Anti-overfitting hygiene note:** `memory/lessons.md`'s "Week of 2026-07-27" entry again lists "volatility-scaled stop width for high-ATR names" in its carry-forward proposal list without noting it is EXHAUSTED (rejected twice: 2026-07-04 formal backtest + 2026-07-08 independent reproduction, both OOS-negative). Per Gate 3 this routine **did not re-test it** this run — flagging the discrepancy so a future run (or the human) doesn't mistake the lessons.md carry-forward listing for still-open, untested evidence. If a future high-ATR semiconductor name (INTC precedent) prompts a fresh proposal for this pattern, it needs a materially new dataset or a walk-forward/paper-trading design before any re-test — not a rerun of 2022–2024/2025/2026 on the same rule.

---

### ✅ Already Implemented (unchanged)

*(Items 1–6 — same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter, max position size 20% — remain implemented per prior entries; not repeated here.)*

---

### 🔴 STRONG Proposals

- **S1 — ELEVATED_BAR realized-health threshold −1.0%.** Verdict unchanged: ✅ BACKTEST SUPPORTS (OOS 2025–2026 identical at 0% vs −1.0%: 52 trades, 2.0% avg, PF 1.62; IS 2022–2024 quality improves 1.89% vs 1.77%). **Still not applied** — `HEALTH_THRESHOLD` confirmed `0.0` this run. **Re-blocked**: S7 regressed, so a threshold change would again have no live effect until `pead_health.md` is producing fresh weekly readings. No re-backtest (no new data since 2026-06-30; re-running the identical test on identical periods would add no information).
- **S2 — "Never-worked" chronic-underwater monitoring flag.** Unchanged — GEV −$319.18, CASY −$813.58, plus the `stop_audit_2026-07-07.md` finding that 50% of all hard-stops are chronic. No new instance this week (book flat, 0 fills). Verdict unchanged: recommend implementing a `CHRONIC_WATCH` surface flag in `pre_market` (not auto-cut).
- **S4 — SEC EDGAR shelf-registration scan.** Unchanged (GOOGL −$413.92 precedent). No new instance this week.
- **S5 — Export-control (BIS) monitoring for semiconductor/IT positions.** Unchanged (AMD/NVDA precedent). No new instance this week.
- **S6 — Missed `pre_market` scheduler-gap investigation.** Unchanged, originally flagged 3 weeks (May-11, Jun-17, Jun-26) — now **6 consecutive clean weeks running** (Jun-29 through Jul-27, all ran all 5 sessions on schedule per commit history). Root cause still never formally investigated, so this stays open at STRONG tier on its historical evidence, but live recurrence risk continues to look low.
- **S7 — `compute_pead_health.py` transport fix — REOPENED (regressed).** Was marked RESOLVED last review (2026-07-25) based on the Jul-19 fix holding through Jul-20→24. **That call is now contradicted by direct evidence**: `pead_health.md` frontmatter confirmed stale this run (`computed_on: 2026-07-19`, `expires_on: 2026-07-26`, unchanged since the fix — the Jul-26 `universe_refresh` did not recompute it). Root cause unchanged from 2026-07-11 diagnosis (`YF_DISABLE_CURL_CFFI=1` set at runtime only, not durably in the routine environment). Recommend the human (i) set `YF_DISABLE_CURL_CFFI=1` (+`lxml`) as a **durable environment variable**, not a per-run export, and (ii) add a `universe_refresh` self-check that aborts/flags if `pead_health.md`'s `computed_on` does not advance to the run date — this would have caught the Jul-26 regression immediately instead of it running stale for a second full week. Fails safe today (stale → NORMAL posture, standard thresholds), but a designed risk control is offline again, and it structurally blocks S1 from having any live effect.
- **S8 — Execution micro-gates (Gate 6d/6e) vs. fresh-print PEAD entries — PROMOTED to STRONG this run (first time).** Now flagged across 3 distinct `lessons.md` weeks (Jul-13 GS 3×, Jul-20 carry-forward, Jul-27 escalated — PWR+AMZN together), and the underlying Gate 6d/6e mechanism has now independently fired on two separate occasions (GS Jul-13/15/16/17; PWR+AMZN Jul-31) deferring 100% of fresh-print qualifiers screened since Gate 6 shipped (commit `e36ad29`, 2026-06-25). No realized $-loss (nothing was ever filled — pure opportunity cost), but the pattern is now structural, not a one-off. **Backtest attempted, blocked by an infrastructure gap, not by evidence quality:** Gate 6d/6e require Alpaca 5-minute intraday bars (`09:30–09:45 ET` opening range; see `routines/market_open.md` Gate 6) to compute Opening Range High/Low and range-vs-ATR width. The existing backtest engine (`backtest_pead_2026_ytd.py` and everything under `backtesting/scripts/`) is built entirely on **daily** OHLC bars from yfinance and has no intraday data source — confirmed by inspecting `bt_common.py` and the full `scripts/` directory; no intraday-capable script exists. A same-day daily-bar proxy (e.g. gap % vs. ATR) would not faithfully represent a 15-minute opening-range/breakout gate and risks producing a misleading low-confidence result — not attempted, per the routine's own standard against noise backtests on thin/mismatched methodology. **Recommend the human decide procedurally between (a) accept the gates as by-design chaotic-open protection, or (b) add a high-conviction override for fresh-print qualifiers (resting limit at/below prior close, waive Gate 6d/6e for the first N sessions post-beat, or a VWAP/mid-morning re-check instead of the 09:50 snapshot) — or (c) commission a new intraday-bar backtest script (would need Alpaca or another 5-min-bar source, not yfinance) before this can get a real out-of-sample validation.** This is now the single largest deployment blocker in the live book — 2 of 2 qualifying opportunities since Gate 6 shipped were deferred, not filled.

---

### 🟡 MODERATE Proposals (ranked, not backtested)

- **M1 — Orphan stop queue in `market_open`** *(still 2 weeks: May-11, May-18)* — unchanged; not implemented.
- **M2 — Max concurrent positions 8→10** *(still 1 week: May-26)* — unchanged; `strategy.md` still caps at 8.
- **M3 — GTC stop behavior on paper account** *(still 1 week: Jun-01)* — unchanged.
- **M4 — Sizing-correction process clarification** *(still 1 week: Jun-01)* — unchanged.
- **M5 — Between-seasons secondary entry lane** *(still 2 weeks: Jun-29, Jul-06)* — no new instance this week (book flat, no rejections to classify).

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** — unchanged, superseded by the live partial profit-lock rule.
- **S3-V1 — ATR stop, tighter/capped variant** — REJECTED (2026-06-25); 1 rejection, not re-tested.
- **S3-V2 — ATR stop, wider/uncapped variant** — **EXHAUSTED** (2 rejections: 2026-07-04 formal + 2026-07-08 independent reproduction). Do not re-test without a materially new dataset. `lessons.md` is still carrying this forward as a pending item as of Jul-27 — see the anti-overfitting hygiene note above.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence | Backtest verdict | Recommended action |
|------|----|----------|------|----------|------------------|--------------------|
| 1 | S8 | Execution micro-gates vs fresh-print entries | 🔴 STRONG (new) | 3 weeks, 2× independent Gate-6d/6e defer instances (GS, PWR+AMZN), 100% of fresh-print qualifiers blocked since Jun-25 | Blocked — needs intraday-bar backtest infra (does not exist) | Human decision: accept gates as-is, add high-conviction override, or commission intraday backtest tooling |
| 2 | S7 | Fix `compute_pead_health.py` transport durably | 🔴 STRONG (reopened) | Regressed after 1 week; 2nd full staleness cycle | N/A — infra fix | Set `YF_DISABLE_CURL_CFFI=1`+`lxml` as a durable env var; add a `universe_refresh` self-check on `computed_on` advancing |
| 3 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 weeks + data | ✅ OOS-supported (2026-06-30); re-blocked by S7 regression | Apply: tune threshold in `compute_pead_health.py` — has no live effect until S7 is durably fixed |
| 4 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 weeks + GEV −$319 + CASY −$814 + 50% of all hard-stops chronic (stop-audit) | Analytical — recommend | Add `CHRONIC_WATCH` alert to `pre_market` |
| 5 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 weeks + $413.92 loss | Analytical — recommend | Add EDGAR scan to `pre_market` |
| 6 | S5 | Export-control monitoring | 🔴 STRONG | 4 weeks + AMD/NVDA stops | Analytical — recommend | Extend BIS scan to open positions |
| 7 | S6 | Missed scheduler investigation | 🔴 STRONG | 3 weeks, now 6 consecutive clean weeks | Operational | Investigate trigger config to confirm root cause; risk trending down but unconfirmed |
| 8 | M1 | Orphan stop queue | 🟡 MODERATE | 2 weeks | Not backtested | Consider adding to `market_open` |
| 9 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 week | Not backtested | Wait for more evidence |
| 10 | M3 | GTC stop behavior | 🟡 MODERATE | 1 week | Not backtested | Monitor; investigate paper-acct behavior |
| 11 | M4 | Sizing-correction process | 🟡 MODERATE | 1 week | Not backtested | Low priority — add to `market_open` checklist |
| 12 | M5 | Between-seasons secondary entry lane | 🟡 MODERATE | 2 weeks | Not backtested | Wait for a concrete missed-candidate instance |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 week | Superseded | No action |
| — | S3-V1 | ATR stop, tighter/capped | ⚪ Rejected | 1 rejection | Rejected 2026-06-25 | No re-test |
| — | S3-V2 | ATR stop, wider/uncapped | ⚪ **EXHAUSTED** | 2 rejections | Rejected 2026-07-04 + confirmed 2026-07-08 | Do not re-test — human/manual review only; lessons.md still lists it as pending, correct via this note |

*(S8 enters the queue at #1 this run — first time promoted to STRONG, and it's the most consequential open item: it's actively blocking every fill the strategy has produced a qualifier for since Jun-25. S7 re-enters at #2 (regressed). S1 drops to #3, re-blocked by the S7 regression. S2/S4/S5/S6 hold their relative order.)*

---

### Notes on this run

- **No formal numeric backtest was run this session.** S1 has a standing OOS-supported result with no new data to re-test against; S3-V2 is EXHAUSTED (correctly not re-tested despite lessons.md still listing it as pending — see hygiene note above); S2/S4/S5/S6/S7 are procedural/operational with no mechanical backtest possible; S8 crossed into STRONG for the first time this run but is blocked by a genuine infrastructure gap (no intraday-bar data source in the backtest engine) rather than an evidence-quality problem — attempting a daily-bar proxy was considered and rejected as methodologically unsound (see S8 above).
- **`backtesting/data_cache/` remains empty** (per `.gitignore`); no fetch was needed this run. `backtesting/scripts/` has no new scripts since the 2026-07-25 review.
- **Reconciliation:** `GET /v2/positions` = `[]` matches `memory/portfolio.md`'s FLAT book — 0/0 PASS, zero divergence (read-only sanity check per Gate 2; this routine does not own reconciliation and would not abort even on a mismatch).
- **`memory/strategy.md` unchanged** since the last human edit — confirmed by content inspection (20% sizing cap, 8 concurrent, unchanged risk/entry/exit rules); no new proposal has been applied by the human this week, so S1/S2/S4/S5/S6/S7/S8 all remain open exactly as ranked above.
- **Correction to last week's log:** the 2026-07-25 entry moved S7 to "Already Implemented / Resolved." That call is superseded by this run's direct evidence (`pead_health.md` still stale). S7 is reopened above and returned to the ranked STRONG queue.
- Proposals already implemented (not re-recommended): same-day cap, macro deferral, partial profit-lock, mandatory pead_health refresh verification, opening-range entry filter, sizing-cap discrepancy resolution (20%).

---

## 2026-08-08 — Weekly Strategy Review

**Run time:** Sat 2026-08-08 ~10:00 ET (market-independent — no clock gate needed).
**Routine:** `strategy_review` (analysis/recommend-only — no orders placed, no memory files other than this log touched).
**Reconciliation (read-only sanity check, Gate 2):** **NOT PERFORMED LIVE this session** — no Alpaca credentials/network reachable in this analysis sandbox (`ALPACA_API_KEY_ID` unset; no live `GET /v2/positions` call made). Falling back to the last-known state in `memory/portfolio.md`, written by `market_close` 2026-08-07T15:47 ET: **EME 13 @ $834.12**, hard stop `96e4e855` @ $767.39 GTC active, cash ~89%. This is a disclosed limitation, not a pass/fail claim — per Gate 2 this routine does not abort on reconciliation issues either way.
**`memory/pead_health.md` status:** `computed_on: 2026-08-02`, `expires_on: 2026-08-09`, posture **NORMAL** (realized_health_60d +2.008%, n=269, `health_threshold_pct: 0.0` — confirms **S1 has NOT been applied** by the human). Still fresh as of today; **the next `universe_refresh` (Sun 2026-08-09) is the live test of whether the transport fix (S7) finally holds two refreshes in a row** — flag for next cycle.
**`memory/strategy.md`:** unchanged since last human edit (20% sizing cap, 8 concurrent, 5/week base cap, all risk/entry/exit rules as documented). No new human edits this week — everything below remains a recommendation only.
**New source material since the 2026-08-01 review:** one new `weekly_review` entry, "Week of 2026-08-03" (commit `c5d9c2a`, Mon Aug 3 → Fri Aug 7). Headline: **EME filled Aug 5** — the first actual fill in ~6 weeks, and it broke through Gate 6d/6e cleanly (narrow OR, wide ATR). But the book still ran only ~11% deployed while SPY rallied +3.53% to record highs (S&P 7,736.52 Aug 4) — portfolio −0.11% vs SPY +3.53%, **delta −3.64 pts, the worst relative week in the log.** LLY (top pick, 8/10) and CAT were both deferred/never filled on the year's best up-week.

---

### Anti-overfitting counters (Gate 3) — carried forward, **no new formal backtests run this cycle**

| Proposal | Times backtested (formal) | Status |
|---|---:|---|
| S1 — ELEVATED_BAR threshold −1.0% | 1 (2026-06-30, OOS-supported) | Not exhausted. No new data since 2026-06-30 → correctly **not** re-tested this cycle (re-running the identical test on identical periods adds no information). |
| S3-V1 — ATR stop, tighter/capped variant | 1 (2026-06-25, REJECTED) | Not exhausted, but no new evidence to justify a re-test. |
| S3-V2 — ATR stop, wider/uncapped variant | 2 (2026-07-04 formal + 2026-07-08 independent sweep reproduction, both REJECTED — fails OOS) | **EXHAUSTED.** Per Gate 3, correctly **not** re-tested this cycle despite `lessons.md`'s Aug-03 entry still carrying "volatility-scaled stop width" in its pending list — this is the same lessons.md/log hygiene gap flagged in the 2026-08-01 entry; it recurs again this week (see Notes). |
| S8 — execution micro-gates (Gate 6d/6e) | 0 formal | **Still blocked by an infrastructure gap, not evidence quality**: Gate 6d/6e need 5-minute intraday Alpaca bars (opening-range width, ORH/ORL); everything in `backtesting/scripts/` is built on **daily** OHLC only — confirmed again this cycle by re-inspecting `bt_common.py` (`get_daily_bars`, no intraday timeframe support anywhere in the module). No intraday-capable script exists. A daily-bar proxy was again considered and rejected as methodologically unsound (would not represent a 15-min opening-range gate faithfully). |
| All others (S2, S4, S5, S6, S7, S9, M1–M5) | 0 formal | Procedural/monitoring/documentation items — no mechanical rule to backtest. |

**Network check performed this cycle:** `curl` to Yahoo Finance's chart API returned **HTTP 429** (rate-limited), consistent with the previously-diagnosed shared-egress-IP throttling documented in this log. `backtesting/data_cache/` remains empty (`.gitkeep` only). This is moot this cycle since no proposal required a fresh backtest, but is recorded so a future cycle doesn't assume the transport issue is resolved.

**Conclusion for Step 4 this cycle: zero new backtests run.** Every STRONG proposal either (a) already has a standing OOS-tested verdict with no new data to justify a re-test, (b) is EXHAUSTED under Gate 3, or (c) is blocked by a genuine infrastructure gap (procedural or intraday-data-only). Running anything anyway would be either overfitting (re-testing on identical data) or fabricating a result on data the engine cannot produce.

---

### ✅ Already Implemented (confirmed against current `memory/strategy.md` + routine files)

1. **S&P 1500 universe expansion** — `strategy.md` § Universe: "S&P 500 + S&P 400 + S&P 600." (First flagged 2026-05-07.)
2. **Same-day open+close counts toward the weekly new-position cap** — `strategy.md` § Capital & sizing: "a position opened and closed same day via midday cut still consumes a weekly slot." (First flagged week of 2026-05-18.)
3. **Macro deferral rule** — `strategy.md` § Risk controls: "if S&P 500 futures are down >0.4% AND the 10-year Treasury yield is at a multi-month high... raise the EPS surprise threshold to >20% for that day only." (First flagged week of 2026-05-18.)
4. **Partial profit-lock at +10% trailing trigger** — `strategy.md` § Risk controls / Trailing stop on winners: sell 1/3 at +10%, trail remaining 2/3 at 7%. (First flagged Jun-08 PARTIAL; live in strategy.md as of the Jun-15 review.)
5. **Opening-range entry filter (Gate 6d/6e)** — implemented in `routines/market_open.md` §6 (shipped commit `e36ad29`, 2026-06-25), directly addressing the MU same-day noise-stop precedent from the entry side (rather than the stop-width side, which is S3/EXHAUSTED). **Partial credit only** — this is a routine-file implementation, not a `strategy.md` rule, and it is itself the subject of the still-open S8 proposal (whether it over-defers fresh-print qualifiers).
6. **`pead_health.md` staleness self-check (monitoring half of S7)** — implemented in `routines/universe_refresh.md` §7 ("VERIFY the refresh actually happened (mandatory post-condition)... `PEAD_HEALTH_REFRESH_MISS` tag..."). **This is only half of S7** — the underlying transport fix (`YF_DISABLE_CURL_CFFI=1` + `lxml` as a *durable* environment setting) is not confirmed durable; see S7 below, which stays open.

**Correction to a prior log claim:** the 2026-08-01 entry's "Already Implemented" list included *"sizing-cap discrepancy resolution (20%)."* **This was checked directly this cycle and is incorrect** — `routines/pre_market.md` (lines 40, 99), `routines/market_open.md` (line 19), and `routines/weekly_review.md` (line 32) **all still hardcode "11%"** as the sizing cap, while `memory/strategy.md` (the authoritative source per `CLAUDE.md`) says **20%**. `strategy.md`'s 20% figure is genuinely implemented (that was never in question); what was never done is updating the routine-text references to match. This proposal is reopened below as **S9**. Flagging this explicitly per the instruction to be rigorous about false/premature claims.

---

### 🔴 STRONG (backtested where mechanically possible; procedural items assessed analytically)

*Evidence-week counts below use the full "any mention, including bundled carry-forward one-liners in a later week's 'still pending' list, counts as flagged again" rule. Where this materially exceeds a prior cycle's count (which only counted dedicated paragraphs), both are shown for transparency.*

---

**S8 — Execution micro-gates (Gate 6d/6e) vs. fresh-print PEAD entries** *(4 distinct weeks: Jul-13, Jul-20, Jul-27, Aug-03)*

Gate 6d (opening-range width > 0.5×ATR ⇒ defer) and Gate 6e (price ≤ ORH ⇒ defer) have deferred **100% of fresh-print qualifiers for 3 straight instances** (GS ×3 Jul-13/16/17; PWR+AMZN together Jul-31) before **finally passing one (EME, Aug-5)** this week. No direct $-loss (nothing was ever filled on the deferred names — pure opportunity cost), but the cost is now realized and quantified: **−3.64 pts vs SPY the week of Aug-03**, the worst relative week in the log, with the #1-ranked pick (LLY, 8/10) and CAT both deferred on the year's best up-week.

**Backtest status:** blocked by infrastructure gap (no intraday bar source in the backtest engine — see Gate 3 table above). **Not backtested this cycle**, consistent with every prior cycle since S8 was promoted to STRONG (2026-08-01).

**New evidence this cycle (not a backtest, an observation):** EME's clean Aug-5 fill is the first proof the gates are a *filter*, not a *wall* — they let through a genuinely narrow-OR/wide-ATR breakout and deferred the choppy ones. This nuances, but does not resolve, the tradeoff: the framing shifts from "gates block everything" to "gates have a real false-defer rate on high-quality fresh prints, and this week that rate cost the single biggest relative-return week in the log."

**Verdict:** ⚠️ Not backtestable this cycle — **human decision required**, unchanged from 2026-08-01: (a) accept the gates as by-design chaotic-open protection (EME proves they can pass a real setup); (b) add a high-conviction override for fresh-print qualifiers — resting limit at/below prior close, waive Gate 6d/6e for the first N sessions post-beat, or replace the 09:50 opening-range snapshot with a VWAP/mid-morning re-check; or the newly surfaced Aug-03 refinement (c) a **partial/staggered entry** on a Gate-6 defer (fraction of target size immediately, remainder if the gate clears next session) so a record-high week isn't missed with zero fill. This is an execution-layer (`market_open.md`) tuning decision, not a `strategy.md` change — **no `strategy.md` wording is proposed; human applies any change to the routine file, this routine does not.**

---

**S7 — `compute_pead_health.py` transport fix (durability half)** *(6 distinct weeks: Jun-29, Jul-06, Jul-13, Jul-20, Jul-27, Aug-03)*

Root cause (diagnosed 2026-07-11): yfinance's `curl_cffi` transport is reset by the TLS-re-terminating proxy; `YF_DISABLE_CURL_CFFI=1` + `lxml` fixes it, but has twice been applied **runtime-only** and regressed on the next fresh cloud environment (fixed Jul-19, regressed Jul-26; the self-check now at least surfaces this loudly instead of silently — see Already Implemented #6).

**This cycle's status:** `pead_health.md` reads `computed_on: 2026-08-02`, `expires_on: 2026-08-09` — **currently fresh**, i.e. the Aug-02 `universe_refresh` succeeded. This is one data point, not confirmation of durability (the Jul-19 fix also looked resolved for one cycle before regressing). **The Aug-09 `universe_refresh` is the actual test** — if `computed_on` advances to 2026-08-09, that's two consecutive clean refreshes and a real signal the fix survived a fresh environment; if it doesn't, this is a 3rd occurrence of the same regression.

**Backtest status:** N/A — infrastructure fix, not a trading rule. Not backtestable.

**Verdict:** RECOMMEND (unchanged) — human sets `YF_DISABLE_CURL_CFFI=1` and installs `lxml` as a **durable environment variable** (not a per-run export) in the routine's execution environment. **This is an environment-config change outside this repo's files; this routine cannot apply it. Human applies this; this routine does not.**

---

**S1 — ELEVATED_BAR realized-health threshold: 0.0% → −1.0%** *(3 distinct weeks: Jun-08, Jun-15, Jun-22)*

**Standing backtest result (2026-06-30, not re-run this cycle — no new data):**

| Period | Trades | Avg return | PF |
|---|---:|---:|---:|
| 2022–2024 (IS) — threshold 0.0% (current) | 139 | +1.77% | 1.69 |
| 2022–2024 (IS) — threshold −1.0% (proposed) | 157 | +1.89% | 1.72 |
| 2025–2026 (OOS) — threshold 0.0% (current) | 52 | +2.0% | 1.62 |
| 2025–2026 (OOS) — threshold −1.0% (proposed) | 52 | +2.0% | 1.62 |

**OOS discipline:** OOS is **identical** at both thresholds (same 52 trades, same avg/PF) — the proposed threshold neither helps nor hurts OOS, and it fixes a documented IS problem (60% of 2023 trades blocked at 0.0%, and the 23 that passed averaged **−1.30%**; at −1.0% only 44% are blocked and the 33 that pass average **+1.42%**). **Verdict stands: ✅ BACKTEST SUPPORTS.**
**Benchmark check:** SPY returned ~+26% (2023) / ~+23% (2024) in the IS window; this proposal is a threshold tune inside an already-selective strategy, not a standalone return claim — the relevant comparison is PF-preserved-or-improved at both thresholds, which holds.

**Live blocker (unchanged):** `health_threshold_pct` confirmed still `0.0` in today's `pead_health.md` — **not applied by the human**, and its live effect remains gated on S7 producing durable weekly readings (a threshold change on a chronically-stale file does nothing).

**Proposed `strategy.md`/production wording (human applies; this routine does not):**
> In `compute_pead_health.py`, change the ELEVATED_BAR trigger comparison from `realized_health >= 0.0` to `realized_health >= -1.0`. Backtest (2022–2026, 191→209 trades): OOS (2025–2026) is unchanged (52 trades, +2.0% avg, PF 1.62 at both thresholds); IS quality improves (avg +1.89% vs +1.77%, PF 1.72 vs 1.69), and the counterproductive 2023 over-blocking (60% blocked, −1.30% avg on survivors at 0.0%) is corrected (44% blocked, +1.42% avg survivors at −1.0%).

---

**S2 — "Never-worked" chronic-underwater monitoring flag** *(3 dedicated weeks — Jun-08, Jun-15, Jun-22 — carried forward in every subsequent week's pending list through Aug-03: **9 distinct weeks total** on the strict counting rule)*

Documented real (paper) losses: **GEV −$319.18 (−8.01%, 21 days, never green)**, **CASY −$813.58 (−8.21%, 12 days, never green)**. Standing analytical finding (2026-06-30, cached `backtest_trades_PEAD_2022_2025_ENHANCED_base.csv`, 5,836 rows): **43% of all hard-stop exits are "chronic"** (held >20 days before stopping) — the GEV/CASY pattern is structural, not anecdotal. **This week's watch item:** EME (open, −1.0% to −3.1% intra-week, never closed green in 3 sessions as of Aug-07) is the live instance to monitor next cycle; no new realized loss this week.

**Backtest status:** explicitly a monitoring/alerting rule, not a mechanical exit ("NOT auto-cut" per the proposal itself) — no formal price-path backtest is meaningful; the standing analytical assessment is unchanged.

**Verdict:** ✅ ANALYTICAL SUPPORT (unchanged) — recommend implementing.

**Proposed `strategy.md` addition (human applies; this routine does not):**
> In `pre_market`'s thesis-audit section: flag any open position `CHRONIC_WATCH` if (a) it has not closed green on any session since entry, AND (b) current price is within 2% of the hard stop. Log in `plan.md`: `"⚠️ CHRONIC_WATCH: <TICKER> — held <N> days, never closed green, cushion <X>% above stop $<price>."` This is NOT an auto-exit — no order is placed by the agent.

---

**S9 — Reconcile the routine-text sizing-cap discrepancy (11% vs. `strategy.md`'s 20%)** *(5 distinct weeks: Jul-06, Jul-13, Jul-20, Jul-27, Aug-03 — reopened this cycle; see correction above)*

`strategy.md` § Capital & sizing says **20%**. `routines/pre_market.md` (×2 references), `routines/market_open.md`, and `routines/weekly_review.md` all still hardcode **11%**. No breach has occurred yet because live entries have all sized 10–11% of equity (well under both figures), but the routine text disagreeing with the authoritative file is a live latent-bug risk — a future sizing calculation keyed off the routine text would under-size (or a human reading the routine text would misjudge risk) relative to `strategy.md`'s actual 20% cap.

**Backtest status:** N/A — documentation-sync fix, not a trading rule. Not backtestable, and doesn't need to be — this is unambiguous.

**Verdict:** RECOMMEND — human confirms 20% is intended (it is the authoritative value per `CLAUDE.md`) and edits the three routine files to read 20% instead of 11%. **This routine cannot edit `routines/*.md` files (only `backtesting/strategy_review_log.md`) — human applies this.**

---

**S4 — SEC EDGAR shelf-registration pre-market scan** *(4 dedicated weeks — Jun-01, Jun-08, Jun-15, Jun-22 — carried forward every week through Aug-03: **10 distinct weeks total**)*

Documented loss: **GOOGL −$413.92 (−8.71%, Jun-02)** — the $80B Alphabet offering (424B1 filed the same morning) gapped the stock below its stop at the open; a pre-market EDGAR scan would have surfaced it before the open. No new instance this week.

**Backtest status:** not backtestable — external filing data is not in the engine's daily-OHLC universe. Analytical assessment unchanged: MODERATE implementation cost (EDGAR full-text search API is free; ~3–8 calls/day at current book size), recommend restricting to prospectuses raising >5% of market cap to cut false positives from routine shelf filings.

**Verdict:** RECOMMEND — human applies; this routine does not.

---

**S5 — Export-control (BIS) monitoring for semiconductor/IT positions** *(4 dedicated weeks — Jun-01, Jun-08, Jun-15, Jun-22 — carried forward through Aug-03: **10 distinct weeks total**)*

Documented losses: **AMD stopped −8% (Jun-01, BIS MI350x loophole closure)**; **NVDA stopped −8% (Jun-05, broader export-control selloff)**. Precedent already exists in practice (MU's Jun-30 pre_market deep-research included an ad-hoc BIS scan) — the proposal is to formalize this for all open IT/semi positions, not just new candidates.

**Backtest status:** not backtestable — same reason as S4 (external event data, not in the engine).

**Verdict:** RECOMMEND — human applies; this routine does not.

---

**S6 — Missed pre-market scheduler-gap investigation** *(originally 3 dedicated weeks — May-11, Jun-15, Jun-22 — carried forward through Jul-27: **8 distinct weeks total**, but zero recurrence and zero mentions in the Aug-03 entry)*

No trading-rule content — root cause of the May 11–13 / Jun-17 / Jun-26 missed `pre_market` sessions was never formally diagnosed, but recurrence has been **zero for 7 consecutive weeks** (Jun-29 through Aug-07 inclusive). Risk trending toward resolved but not formally confirmed.

**Backtest status:** N/A — operational/infra, not a trading rule.

**Verdict:** RECOMMEND CLOSING OUT pending human confirmation — 7 clean weeks is a strong signal this either self-resolved or was fixed as a side effect of other environment work; recommend the human either (a) do a final check of the trigger/scheduler configuration and close this item, or (b) explicitly keep it open only if there's a known reason it could recur.

---

### 🟡 MODERATE (ranked, not backtested per Gate 3/MUST-NOT)

- **M1 — Orphan stop queue in `market_open`** *(2 weeks: May-11, May-18)* — scan `portfolio.md` at the start of `market_open` for positions missing a `stop_order_id`, place those first. One documented instance (CSCO stop placed 1 day late). Would promote to STRONG on a second same-pattern instance.
- **M2 — Max concurrent positions 8→10** *(1 week: May-26)* — unchanged; `strategy.md` still caps at 8. Note: in every subsequent week where the book was under-deployed, the binding constraint was signal supply or execution gates, **never** the 8-position cap itself — the original opportunity-cost rationale (PWR/ANET blocked by 8/8) hasn't recurred. Borderline WEAK on current evidence; kept at MODERATE pending a fresh concrete instance.
- **M3 — GTC stop behavior on paper account** *(1 week: Jun-01)* — HPE's after-hours GTC fill (16:22 ET). No second instance since.
- **M4 — Sizing-correction process clarification** *(1 week: Jun-01)* — HPE sizing-basis correction. No recurrence; process appears to have self-corrected.
- **M5 — Between-seasons secondary entry lane** *(2 weeks: Jun-29, Jul-06)* — use the already-threshold-exempt analyst-revision/partnership-catalyst lane more actively during earnings deserts. No new concrete missed-candidate instance since Jul-06 (the binding constraint shifted to execution gates, not signal supply, from Jul-13 onward).

---

### ⚪ WEAK / EXHAUSTED

- **W1 — Trailing-stop pre-alert at +8% unrealized** *(1 week: May-11)* — superseded by the live partial-profit-lock rule (Already Implemented #4).
- **S3-V1 — ATR stop, tighter/capped variant** — 1 rejection (2026-06-25); not EXHAUSTED but no new evidence to justify a re-test.
- **S3-V2 — ATR stop, wider/uncapped variant** — **EXHAUSTED** (2 rejections: 2026-07-04 formal, OOS avg 0.64% vs baseline 0.70% / PF 1.08 vs 1.20; 2026-07-08 independent 45-combo sweep reproduction, explicitly "CONFIRMS S3; does NOT overturn it"). **Do not re-test without a materially new dataset or a walk-forward design.** `lessons.md`'s Aug-03 entry again lists "volatility-scaled stop width for high-ATR names" in its carry-forward pending list without flagging EXHAUSTED status — same hygiene gap noted in the 2026-08-01 log entry, recurring. Correctly **not** re-tested this cycle.

---

### Ranked summary table

| Rank | ID | Proposal | Tier | Evidence-weeks | Backtest status | Recommended action |
|---|---|---|---|---:|---|---|
| 1 | S8 | Execution micro-gates vs. fresh-print entries | 🔴 STRONG | 4 | Blocked — no intraday-bar backtest infra | Human: accept as-is, add override, or commission intraday tooling |
| 2 | S7 | `compute_pead_health.py` durable transport fix | 🔴 STRONG | 6 | N/A — infra fix | Set env var durably; watch Aug-09 refresh |
| 3 | S1 | ELEVATED_BAR threshold −1.0% | 🔴 STRONG | 3 | ✅ OOS-supported (standing, 2026-06-30) | Apply in `compute_pead_health.py` — no live effect until S7 durable |
| 4 | S2 | "Never-worked" chronic flag | 🔴 STRONG | 3 (9 incl. carry-forward) | Analytical support | Add `CHRONIC_WATCH` to `pre_market` |
| 5 | S9 | Sizing-cap doc discrepancy (11% vs 20%) | 🔴 STRONG (reopened) | 5 | N/A — doc fix | Update 3 routine files to 20% |
| 6 | S4 | EDGAR shelf-registration scan | 🔴 STRONG | 4 (10 incl. carry-forward) | Not backtestable (external data) | Add to `pre_market` |
| 7 | S5 | BIS export-control monitoring | 🔴 STRONG | 4 (10 incl. carry-forward) | Not backtestable (external data) | Extend to open positions |
| 8 | S6 | Scheduler-gap investigation | 🔴 STRONG | 3 (8 incl. carry-forward) | N/A — operational | Recommend closing pending final human check (7 clean weeks) |
| 9 | M1 | Orphan stop queue | 🟡 MODERATE | 2 | Not backtested | Consider adding |
| 10 | M2 | Max concurrent 8→10 | 🟡 MODERATE | 1 | Not backtested | Evidence has weakened — wait |
| 11 | M3 | GTC stop behavior | 🟡 MODERATE | 1 | Not backtested | Monitor |
| 12 | M4 | Sizing-correction process | 🟡 MODERATE | 1 | Not backtested | Low priority |
| 13 | M5 | Secondary entry lane | 🟡 MODERATE | 2 | Not backtested | Wait for fresh instance |
| — | W1 | Trailing-stop pre-alert | ⚪ WEAK | 1 | Superseded | No action |
| — | S3-V1 | ATR stop, tighter/capped | ⚪ Rejected | 1 rejection | No re-test | No action |
| — | S3-V2 | ATR stop, wider/uncapped | ⚪ **EXHAUSTED** | 2 rejections | Do not re-test | No action |

---

### Notes on this run

- **Zero new formal backtests this cycle** — every STRONG proposal is either standing-verdict/no-new-data (S1), EXHAUSTED (S3-V2), or genuinely un-backtestable with this engine (S2, S4, S5, S6, S7, S8, S9 are procedural/monitoring/infra). This is a legitimate outcome per the routine's own anti-overfitting discipline, not a shortfall.
- **Correction issued this cycle:** the 2026-08-01 log entry's claim that the sizing-cap discrepancy was resolved is **wrong** — verified directly against `routines/pre_market.md`, `routines/market_open.md`, `routines/weekly_review.md` this session; all three still say 11% vs. `strategy.md`'s 20%. Reopened as S9.
- **Recount methodology note:** several proposals' "weeks flagged" figures are meaningfully higher this cycle than in prior log entries (e.g. S2: 3 dedicated weeks vs. 9 total including every "still pending" carry-forward bundle; S4/S5: 4 vs. 10) because this cycle applied the instruction that any carry-forward mention — including a one-line bundled "still pending" reference — counts as a fresh flag. This does not change any tier outcome (all were already STRONG) but is a more complete evidence count than prior cycles used.
- **`lessons.md`/log hygiene gap recurs:** `lessons.md`'s Aug-03 entry again lists the EXHAUSTED wider-ATR-stop proposal in its pending carry-forward list without noting its EXHAUSTED status, same as the 2026-08-01 entry flagged. Recommend the human (or `weekly_review`) stop carrying EXHAUSTED items forward as if open, to avoid a future cycle mistaking the listing for untested evidence.
- **Reconciliation not performed live** (no Alpaca network/credentials in this analysis session) — this is a disclosed sandbox limitation, not a reconciliation failure; `market_close`'s last-written `portfolio.md` state (EME 13 @ $834.12) was used for reference only.
- **`memory/strategy.md` unchanged** since the last human edit — none of the recommendations in this report have been applied. All STRONG items with a proposed wording are explicitly labeled below: **the human applies these edits; this routine never edits `strategy.md` or any routine file.**
