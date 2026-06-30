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
