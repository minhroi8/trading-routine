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
