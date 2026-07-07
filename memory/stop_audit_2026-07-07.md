# Hard-Stop Outcome Audit — 2026-07-07

Research-only diagnostic. No orders placed, no edits to `memory/strategy.md`, no historical trade records modified. Nothing in this file should be read as a validated production rule.

## 1. Executive summary

Exploratory audit only. The full sample contains 13 closed trades and 8 hard-stop exits. Results are hypothesis-generating, not sufficient to validate a production rule.

The audit covers every trade closed between 2026-05-06 and 2026-07-07: **8 hard-stop exits** (primary cohort) and **5 trailing-stop exits** (comparison cohort). A 14th closed trade in the window, GLW (2026-05-18, midday rule cut), is neither a hard stop nor a trailing stop and is excluded from both cohorts — see Limitations (§10).

Key findings, all sample-size-qualified:

- **Chronic never-worked positions, not volatility spikes, are the modal hard-stop outcome.** 4 of 8 hard-stop trades (AMZN, PWR, CASY, and NVDA on a borderline basis) spent the large majority of their holding period closing underwater and never confirmed a +3% close before eventually hitting -8%. Zero trades fell into the classic "same-day noise stop that then recovers" bucket.
- **The two same-day stopouts (HPE, MU) both continued falling after the stop**, not reverting — directly contradicting the "sell-the-news noise stop" framing used in MU's own contemporaneous trade-log rationale.
- **Post-stop recovery is real but concentrated in 2 of 8 names (GEV, PWR), not systematic.** Median SPY-relative return across the hard-stop cohort was slightly negative at +5 trading days and roughly flat-to-mixed at +10/+20 days depending on which trades have data available yet.
- **Hard-stop and trailing-stop trades are cleanly separated by early underwater behavior**, not by day-1 direction: hard-stop trades (excluding same-day) closed underwater a median of ~75% of holding days with underwater streaks of 4–10 consecutive sessions; trailing-stop (winning) trades closed underwater a median of ~17% of days with streaks capped at 0–2 sessions. This separation is not visible on day 1 (3 of 6 non-same-day hard-stop trades also opened with a green close) but becomes visible after several sessions.
- **1 of 8 hard-stop trades (GOOGL) was catalyst-contaminated** (dilutive equity offering announced during the hold) and should not be used as evidence about the stop mechanism itself.

None of this supports "widen the stop" or "the stop is broken" as a conclusion. See §11 (Interpretation) and the hypothesis section (§12-equivalent, folded into the summary below) for the full evidence-for/evidence-against breakdown.

## 2. Full per-trade table

All returns are simple (not annualized). ATR = Wilder ATR(14) on daily bars, computed from completed sessions strictly before entry. "N/A" = insufficient data per the price-history-completeness rule; no case in this sample required N/A on ATR (all 13 trades had ≥46 completed pre-entry sessions available).

| ticker | cohort | entry date | entry px | exit date | exit px | hold (td) | entry ATR14 | entry ATR% | stop dist % | stop dist/ATR | MFE % | MAE % | % closes underwater | max consec. underwater | bucket |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | hard stop | 2026-05-21 | 223.295455 | 2026-06-05 | 205.427272 | 11 | 7.5024 | 3.36% | 8.00% | 2.381 | +4.02% | -8.48% | 10/11 (90.9%) | 6 | C (borderline, see note) |
| AMZN | hard stop | 2026-05-14 | 269.71 | 2026-06-03 | 248.06 | 14 | 6.7927 | 2.52% | 8.00% | 3.175 | +1.84% | -8.15% | 11/14 (78.6%) | 8 | C |
| HPE | hard stop | 2026-06-02 | 59.4002 | 2026-06-02 | 54.6275 | 0 (same-day) | 1.9829 | 3.34% | 8.00% | 2.396 | -0.10% (intraday) | -9.95% (intraday) | n/a (same-day) | n/a | A |
| GOOGL | hard stop | 2026-05-06 | 395.72 | 2026-06-02 | 361.23 | 19 | 9.6466 | 2.44% | 8.00% | 3.281 | +3.25% | -9.40% | 12/19 (63.2%) | 10 | E (catalyst) |
| GEV | hard stop | 2026-05-19 | 996.465 | 2026-06-09 | 916.67 | 15 | 47.0435 | 4.72% | 8.00% | 1.694 | +9.83% | -11.87% | 9/15 (60.0%) | 9 | D |
| PWR | hard stop | 2026-06-02 | 707.0493 | 2026-06-10 | 650.01 | 7 | 24.7389 | 3.50% | 8.00% | 2.286 | +3.21% | -9.16% | 5/7 (71.4%) | 4 | C |
| CASY | hard stop | 2026-06-11 | 900.626364 | 2026-06-23 | 826.664545 | 8 | 31.3369 | 3.48% | 8.00% | 2.299 | +2.66% | -8.16% | 7/8 (87.5%) | 7 | C |
| MU | hard stop | 2026-06-25 | 1249.7275 | 2026-06-25 | 1148.78 | 0 (same-day) | 87.7338 | 7.02% | 8.00% | 1.140 | +0.03% (intraday) | -8.25% (intraday) | n/a (same-day) | n/a | A |
| MSFT | trailing | 2026-05-20 | 412.634545 | 2026-06-03 | 433.576364 | 10 | 11.2539 | 2.73% | — | — | +13.00% | -0.72% | 0/10 (0.0%) | 0 | (profitable) |
| AMD | trailing | 2026-05-06 | 421.59 | 2026-06-01 | 490.44 | 18 | 16.1278 | 3.83% | — | — | +25.00% | -6.66% | 4/18 (22.2%) | 2 | (profitable) |
| AAPL | trailing | 2026-05-06 | 283.10 | 2026-06-09 | 295.116471 | 24 | 6.5269 | 2.31% | — | — | +12.11% | -0.71% | 0/24 (0.0%) | 0 | (profitable) |
| CSCO | trailing | 2026-05-14 | 117.42 | 2026-06-09 | 117.54 | 18 | 2.3820 | 2.03% | — | — | +11.03% | -3.25% | 3/18 (16.7%) | 2 | (profitable) |
| SNDK | trailing | 2026-06-05 | 1643.693333 | 2026-06-16 | 2014.00 | 8 | 107.8451 | 6.56% | — | — | +31.75% | -7.83% | 3/8 (37.5%) | 2 | (profitable) |

Excluded from cohorts (see §10): GLW, midday-rule exit, 2026-05-18, same-day, entry $189.79 → exit $179.54 (-5.40%), intraday low $174.255 (-8.19%, i.e. would very likely have hit its -8% hard stop at $174.60 within the same session had the midday cut not fired first).

## 3. Hard-stop cohort analysis

n = 8. Same-day stopouts = 2/8 (25.0%: HPE, MU).

- **Entry volatility:** median entry ATR% = 3.42%; range 2.44% (GOOGL) – 7.02% (MU). MU is a clear outlier — more than double the cohort median and the widest ATR% in the entire 13-trade sample (hard-stop + trailing).
- **Stop distance relative to volatility:** median stop-distance/ATR = 2.34. Distribution: <1 ATR 0/8 (0.0%), 1–2 ATR 2/8 (25.0%: GEV 1.694, MU 1.140), >2 ATR 6/8 (75.0%). The fixed -8% stop is *not* uniformly tight relative to volatility — for 6 of 8 names it sat comfortably beyond 2 ATR. The two exceptions (GEV, MU) are exactly the two highest-ATR% names in the cohort, i.e., the fixed dollar-percent stop compresses toward the volatility floor precisely when a stock is already the most volatile one in the book.
- **Never-worked rate (non-same-day trades only, n=6):** +1%: 0/6 (0.0%); +2%: 1/6 (16.7%, AMZN); +3%: 2/6 (33.3%, AMZN, CASY); +5%: 5/6 (83.3%, all but GEV). Sensitivity note: at the +5% bar, nearly the entire non-same-day hard-stop cohort qualifies as "never worked" — the bar that actually discriminates in this sample is closer to +3–5%, not +1–2%.
- **Descriptive bucket distribution:** A (immediate adverse continuation) 2/8 (25.0%: HPE, MU); B (possible volatility/noise stop) 0/8 (0.0%); C (chronic never-worked) 4/8 (50.0%: AMZN, PWR, CASY, NVDA-borderline); D (worked then failed) 1/8 (12.5%: GEV); E (catalyst-contaminated) 1/8 (12.5%: GOOGL); F (ambiguous) 0/8.

NVDA is flagged borderline C/D: its intraday MFE (+4.02%, day 8) exceeds the +3% never-worked threshold, but that high was never confirmed by a daily close (max close gain only +0.50%) and 10/11 closes were underwater — on a close-confirmed basis it behaves exactly like the other Bucket-C trades, so it is counted with C in the headline bucket tally above.

## 4. Same-day stopout analysis

2/8 hard-stop trades exited same-day: HPE and MU. Intraday (5-minute bar) MFE/MAE used for both since no daily-close data exists during the hold.

| ticker | entry ATR% | stop dist/ATR | intraday MFE | intraday MAE | post-stop 5d return (from exit) | post-stop 5d SPY-relative | recovered entry within available window |
|---|---|---|---|---|---|---|---|
| HPE | 3.34% | 2.396 | -0.10% | -9.95% | -11.67% | -8.72% | No |
| MU | 7.02% | 1.140 | +0.03% | -8.25% | -15.09% | -16.66% | No |

Neither same-day stopout shows the "sell the news, then mean-revert" pattern that both trades' own contemporaneous rationales assumed at exit (both trade-log entries explicitly called the stop "pure mechanical," "not a thesis break," implying an expected bounce). Both instead continued falling materially over the following days — MU especially sharply (-21.95% from entry at +5 trading days). This is the most important disconfirming evidence against treating same-day hard stops as routine noise in this strategy's current form; note n=2, both could plausibly be explained by different mechanisms (HPE: earnings-gap-fade; MU: extreme entry-day volatility, ATR% more than double the cohort median).

HPE's exit itself is also flagged as an execution anomaly, not a strategy-rule issue: the fill timestamp in `trade_log.md` (16:22 ET) is after the 16:00 ET regular-session close, meaning the GTC stop executed after hours on the paper venue. This does not change the outcome classification but should be reviewed separately as an infrastructure/execution question, not folded into the stop-distance analysis.

## 5. Chronic never-worked analysis

4/8 hard-stop trades (AMZN, PWR, CASY, NVDA) never confirmed a meaningful gain before grinding to the hard stop:

| ticker | hold (td) | max close gain | % closes underwater | max consec. underwater | post-stop 5d return | recovered entry within available window |
|---|---|---|---|---|---|---|
| NVDA | 11 | +0.50% | 90.9% | 6 | -0.13% | No |
| AMZN | 14 | +1.58% | 78.6% | 8 | -4.07% | No |
| PWR | 7 | +1.69% | 71.4% | 4 | +9.96% | Yes (5d) |
| CASY | 8 | +1.72% | 87.5% | 7 | -3.87% | No |

Two of four (PWR, CASY) had at least one green close on day 1 before reversing into a sustained underwater grind — i.e., an early positive close does not rule out the chronic-never-worked pattern; persistence over the following sessions is the discriminator (see §7/§9).

Post-stop paths diverge sharply within this bucket: 3/4 (NVDA, AMZN, CASY) continued to underperform or stayed flat after the stop, while PWR fully round-tripped (+9.96% from exit, +7.83% SPY-relative, at 5 trading days) on what its own trade-log rationale attributes to a broad macro risk-off day (Iran/Strait-of-Hormuz headlines, hot CPI print, SPY -1.36%), not a company-specific issue. This means "chronic never-worked" and "eventually recovers" are not mutually exclusive in this sample — a hypothetical early chronic-exit rule would have avoided further loss on 3/4 but locked in a loss that the market subsequently reversed on the 4th (PWR). See §12 (H4).

## 6. Post-stop recovery analysis

For hard-stop exits, return from actual exit price and from original entry price, at +5/+10/+20 trading days. Denominators shrink at longer horizons because several exits (GEV, PWR, CASY, MU) are recent enough that fewer than 20 (in some cases fewer than 10) completed trading sessions have elapsed since exit as of the last completed session used in this audit (2026-07-06; 2026-07-07 excluded as a potentially in-progress session).

| horizon | median return from exit (n) | median return from entry (n) | % recovered entry price within available window (n) |
|---|---|---|---|
| +5 trading days | -2.00% (n=8) | — | 25.0% (2/8: GEV, PWR) |
| +10 trading days | +2.45% (n=6†) | — | 25.0% (2/8, same two — no additional recoveries by 10d) |
| +20 trading days | -2.32% (n=3‡) | — | 25.0% (2/8; 20-day window is partial/incomplete for GEV, PWR, CASY, MU — see §10) |

† CASY and MU have only 8 and 6 completed post-exit sessions available respectively — excluded from the +10d median. ‡ Only AMZN, HPE, GOOGL have a full 20 completed post-exit sessions available; NVDA is 1 session short (19 available) and is also excluded from the +20d median; GEV/PWR/CASY/MU have materially fewer than 20 sessions elapsed and are excluded.

`recovered_stop_loss_within_20d` (price traded back up to at least the stop-trigger level) was true for 8/8 trades — this is expected and not informative by construction, since the fill price on a hard-stop exit is by definition within a few cents of the stop-trigger level, so almost any subsequent intraday uptick satisfies it. `recovered_entry_within_*` (price traded back to the original entry price) is the meaningful recovery metric and is reported above.

Full recovered-entry detail by trade (available-window basis, "—" = not yet enough post-exit history to evaluate that horizon):

| ticker | sessions elapsed since exit (thru 2026-07-06) | recovered entry 5d | recovered entry 10d | recovered entry 20d (or max available) |
|---|---|---|---|---|
| NVDA | 19 | No | No | No |
| AMZN | 21 | No | No | No |
| HPE | 22 | No | No | No |
| GOOGL | 22 | No | No | No |
| GEV | 17 | Yes | Yes | Yes (window capped at 17) |
| PWR | 16 | Yes | Yes | Yes (window capped at 16) |
| CASY | 8 | No | — | — (window capped at 8) |
| MU | 6 | No | — | — (window capped at 6) |

## 7. SPY-relative analysis

Ticker return minus SPY return over the same trading-day window, measured from the stop-exit date.

| horizon | median SPY-relative return | n |
|---|---|---|
| +5 trading days | -0.49% | 8 |
| +10 trading days | +2.57% | 6 |
| +20 trading days | -1.09% | 3 |

The +10d positive median is driven almost entirely by GEV (+15.9%) and PWR (+9.5%); with those two removed the remaining names (NVDA, AMZN, HPE, GOOGL) are flat-to-negative versus SPY at every horizon with data. This distinguishes genuine stock-specific recovery (GEV, PWR) from broad-market beta — in this sample the recovery is not "the whole cohort drifted up with a rallying market," it is two specific names outperforming.

## 8. Catalyst-contaminated cases

1/8 (12.5%): **GOOGL.** During the 19-trading-day hold, GOOGL announced an ~$80–90B dilutive equity capital raise (disclosed 2026-06-02, the same session the stop fired), which the trade-log exit rationale itself describes as partially invalidating the entry thesis ("mirrors META/MSFT selloff patterns; thesis partially invalidated"). This trade should not be used as evidence about the mechanical stop-distance/volatility question — the exit coincided with a real, company-specific negative catalyst, not a pure stop-distance or noise dynamic. It is retained in the headline cohort tables above (bucket E) but excluded from the "never worked" and "pure noise vs. chronic" mechanism discussion.

No other hard-stop or trailing-stop trade in this window carries a flagged thesis-breaking catalyst per its own trade-log rationale; PWR and NVDA/GEV's declines are attributed in-log to broad macro/market-wide selloffs (Iran/CPI, export-control-narrative tech selloff) rather than company-specific negative news, and are treated as market-wide, not catalyst-contaminated, in this audit.

## 9. Comparison against profitable trailing-stop cohort

n = 5 (MSFT, AMD, AAPL, CSCO, SNDK), all closed profitably.

| metric | hard-stop cohort (n=8, or n=6 for underwater-only) | trailing-stop cohort (n=5) |
|---|---|---|
| median entry ATR% | 3.42% | 2.73% |
| median MFE | +2.94% (all 8, incl. same-day) | +13.00% |
| median % closes underwater (non-same-day) | 75.0% (n=6) | 16.7% (n=5) |
| max consecutive underwater streak, median | 6.5 sessions (n=6) | 2 sessions (n=5) |
| median days to MFE | 4.5 (n=6, non-same-day) | 15 (n=5) |

The two cohorts are cleanly separated on sustained underwater behavior, not on day-1 direction: 3 of 6 non-same-day hard-stop trades (GOOGL, GEV, CASY) also closed positive on day 1, same as the trailing-cohort trades, so day-1 direction alone would not have distinguished a future winner from a future hard-stop. What separates them is persistence over the following several sessions — the trailing-cohort trades never accumulate more than a 2-session underwater streak, while 5 of 6 non-same-day hard-stop trades accumulate a 4+ session streak. Entry ATR% is also modestly, not dramatically, higher for the hard-stop cohort (median 3.42% vs 2.73%; overlapping ranges).

## 10. Limitations

- **Sample size.** 8 hard-stop and 5 trailing-stop trades is far too small to validate any rule change. Every percentage above should be read with its stated numerator/denominator, not in isolation.
- **GLW excluded from both cohorts.** GLW (2026-05-18) closed via the midday -5% rule cut, not a hard stop or trailing stop, so it sits outside this audit's two-cohort design. Its intraday low that same session (-8.19%) suggests it would very likely have hit its -8% hard stop later the same day had the midday cut not intervened first — worth noting as a related but distinct rule (midday cut vs. hard stop) that this audit does not evaluate.
- **Daily-bar granularity for MFE/MAE on multi-day trades.** For the 6 non-same-day hard-stop trades and all 5 trailing-stop trades, MFE/MAE are derived from daily high/low bars spanning the full entry-to-exit date range (inclusive of both the entry day and exit day). This slightly overstates precision on the entry and exit days themselves, where the true post-entry/pre-exit intraday path is unknown from daily bars alone; only the two same-day trades (HPE, MU) use true intraday (5-minute) bars.
- **Post-stop and counterfactual windows are truncated by "today."** Because the audit runs on 2026-07-07 and the most recent hard-stop exit (MU, 2026-06-25) has had only 6 completed trading sessions since exit, the +10d/+20d post-stop metrics and the 42-calendar-day counterfactual time-stop are N/A or based on partial windows for the four most recent hard-stop trades (GEV, PWR, CASY, MU). These are marked N/A rather than estimated; do not treat the reported 20d medians (n=3) as representative of the full 8-trade cohort.
- **`recovered_stop_loss_within_20d` is close to tautological** given exit price is by construction ~8% from entry and within a few cents of the stop-trigger price; it registered true for 8/8 trades and carries essentially no discriminating information. `recovered_entry_within_*` is the metric actually used for recovery conclusions in this report.
- **Same-day trades (HPE, MU) are excluded from all close-based metrics** (never-worked thresholds, underwater-day counts, first-positive-close-day) because no daily close occurred during the hold. Their intraday MFE (HPE -0.10%, MU +0.03%) would trivially satisfy every never-worked threshold tested if a reader chose to include them, which would push the cohort-wide "never worked at +5%" rate from 5/6 (83.3%) toward 7/8 (87.5%) — noted for completeness, not incorporated into the headline denominator to keep the same-day/multi-day methodologies separate as specified.
- **Execution-timing anomaly (HPE).** HPE's stop fill is logged at 16:22 ET, after the 16:00 ET regular session close — a paper-account GTC-stop after-hours execution artifact flagged in the original trade log. This is a possible data-quality / infrastructure issue distinct from the stop-distance question this audit targets, and is not adjusted for.
- **All price data is single-source (Alpaca, feed=iex, adjustment=raw).** No vendor-mixing occurred; all ATR, MFE/MAE, and post-stop figures in this report use the same feed throughout.
- **No slippage/execution modeling.** Reported exit prices are the actual logged fill prices (which already embed real slippage/partial-fill effects per the original trade-log entries), but the counterfactual-hold and post-stop-path figures assume a clean mark-to-close and do not model what exiting at those later points would actually have cost in slippage.
- **Catalyst screening is qualitative**, based on each trade's own contemporaneous trade-log exit rationale plus a review of price action; it is not a systematic news-event scan, so an unflagged catalyst could exist that this audit did not surface.

---

## Hypothesis evaluation (H1–H6)

**H1 — High entry ATR predicts same-day stopouts.**
*For:* MU, the only extreme case, had the highest entry ATR% in the entire 13-trade sample (7.02%, >2x the hard-stop cohort median) and the tightest stop-distance/ATR (1.14) — a clean, if singular, illustration.
*Against:* HPE, the other same-day stopout, had entry ATR% (3.34%) essentially at the cohort median and a stop-distance/ATR (2.396) above the cohort median — the opposite profile a tight-ATR mechanism would predict. HPE's same-day failure looks driven by an earnings-gap-fade pattern, not raw volatility.
*Verdict:* mixed on n=2 same-day cases; MU is suggestive, HPE contradicts. Not testable at this sample size.

**H2 — Low stop-distance/ATR predicts recoverable noise stops.**
*For:* GEV (stop-distance/ATR 1.694, second-tightest in cohort) fully recovered — reclaimed entry within 5 trading days, +15.9% SPY-relative at 10d.
*Against:* MU (stop-distance/ATR 1.140, tightest in cohort) showed zero recovery and continued falling sharply (-21.95% from entry at 5d).
*Verdict:* 1-for-2 on the only two sub-2-ATR cases; not supported as a reliable predictor in this sample.

**H3 — Most hard-stop losses are chronic never-worked positions rather than volatility spikes.**
*For:* 4/8 (50%) trades bucket as chronic never-worked (AMZN, PWR, CASY, NVDA-borderline); 0/8 bucket as a classic recoverable same-day noise stop (Bucket B empty); median underwater-close rate for non-same-day hard-stop trades is 75%.
*Against:* GEV (worked-then-failed, genuine +9.8% MFE before reversing) and GOOGL (catalyst-driven) together account for 2/8 — a quarter of the cohort — that are not chronic-never-worked stories.
*Verdict:* best-supported hypothesis in this audit; chronic never-worked is the modal but not universal outcome.

**H4 — A chronic-position exit concept deserves testing before any wider-stop concept.**
*For:* given H3, a rule targeting chronically-underwater/never-confirmed positions would address the largest single loss-driving bucket (50% of hard-stop trades) without touching stop distance, which was >2 ATR for 75% of the cohort and thus not obviously "too tight" on average.
*Against:* 2 of the 4 chronic-never-worked trades (PWR, CASY) later showed post-stop price action worth noting — PWR fully recovered within 5 trading days (macro-driven dip, not company-specific), meaning an earlier chronic-exit rule would have locked in a loss on at least one name the market subsequently reversed. A chronic-exit concept carries its own recovery-tradeoff risk and is not a free lunch.
*Verdict:* directionally supported by loss-bucket composition; requires a dedicated backtest weighing avoided losses (NVDA, AMZN, CASY-type cases) against foregone recoveries (PWR-type cases) before any conclusion.

**H5 — Hard-stopped trades systematically recover relative to SPY after exit.**
*Against (primary):* only 2/8 (25%) reclaimed entry price within the available window; median SPY-relative return is slightly negative at +5d (-0.49%) and mixed/thin at +20d (-1.09%, n=3).
*For (partial):* median SPY-relative return at +10d is +2.57% (n=6), but this is driven by 2 names (GEV, PWR) pulling the median up, not a cohort-wide pattern; sign flips depending on which subset of trades has data at each horizon.
*Verdict:* not supported as "systematic." Where recovery happens, it is concentrated in specific names, not the cohort as a whole.

**H6 — Profitable trailing-stop trades show distinguishable early path behavior from eventual hard-stop trades.**
*For:* clean separation on sustained underwater behavior — trailing cohort median 16.7% underwater-close days / 2-session max streak vs. hard-stop cohort (non-same-day) median 75% underwater-close days / 6.5-session max streak. Entry ATR% also modestly higher for the hard-stop cohort (3.42% vs 2.73% median).
*Against/caveat:* day-1 direction alone does not distinguish the cohorts — 3 of 6 non-same-day hard-stop trades also opened with a green close, same as the trailing cohort. The distinguishing signal requires several sessions of persistence to show up, not a single day-1 read.
*Verdict:* supported, with the caveat that any operational rule built on this would need a multi-session confirmation window, not a same-day trigger.

**Sample-size warning (repeated):** 8 hard-stop and 5 trailing-stop trades. Every hypothesis above is directional and hypothesis-generating only. None should inform a change to `memory/strategy.md` without a much larger backtest sample (the existing 2022–2025, 207-trade regime-gate backtest referenced in `strategy.md` is the right scale to test any of H1–H6 properly).

**Next recommended backtest:** run a systematic backtest (ideally on the same 2022–2025 multi-year dataset already used for the regime-gate backtest) of a chronic-never-worked early-exit rule — e.g., exit or tighten the stop if MFE has not reached +3% by trading day D and the position has closed underwater for K consecutive sessions — directly testing H4: does avoiding the chronic-never-worked bleed (this audit's largest single loss bucket) outweigh the cost of exiting positions that would have reverted (as PWR and CASY did in this small sample)? This is a more targeted and better-supported next step than testing a wider fixed-stop-distance rule, since 75% of this cohort's hard stops sat beyond 2 ATR — the stop-distance itself was not obviously the binding constraint in most cases.
