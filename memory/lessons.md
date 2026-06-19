# Lessons

Written only by `weekly_review`. Each weekly entry records what worked, what didn't, performance vs SPY, and any proposed rule changes.

Proposed rule changes are suggestions only — the human operator applies them by editing `strategy.md` directly. The agent never edits `strategy.md`.

## 2026-05-07 — Expanded universe to S&P 1500

Reasoning: Felt the S&P 500 universe was missing legitimate momentum names (e.g., RKLB).
Tested research: bot's strategy logic (post-earnings momentum) still applies to mid/small caps.
Risk: mid-caps gap harder, less analyst coverage. ADV filter ($20M) provides some guardrail.
Review date: 2026-06-07 — evaluate whether new picks from S&P 400/600 outperformed or hurt.

---

## Week of 2026-05-11

- Perf: portfolio -0.31% vs SPY +0.36% (delta -0.67 pts)
- Trades: 2 fills (AMZN 18@$269.71 and CSCO 42@$117.42, both buys on May 14); 0 closed trades; win rate N/A
- Avg win: N/A | Avg loss: N/A (no closed trades this week)
- Best (open, unrealized vs cost): AAPL +5.94% ($299.91 close vs $283.10 avg_cost) — Q2 FY2026 beat thesis intact; iPhone +22%, Services ATH $31B, new CEO Ternus execution focus. Approaching +10% trailing stop trigger ($311.41). CSCO +0.42% on only day-2 — Q3 FY2026 blowout entry well-timed.
- Worst (open, unrealized vs cost): AMZN -2.28% ($263.57 close vs $269.71 avg_cost) — entered May 14; layoff news in Selling Partner Services deemed non-material to AWS/AI thesis (+28% YoY, $225B chip commitment); stop $248.14 active with ~5.7% cushion.
- What worked:
  - Portfolio outperformed SPY on the volatile Friday session (+0.85% relative alpha vs SPY -1.07% day)
  - AAPL continuing strong post-earnings momentum toward trailing stop trigger; +5.94% unrealized in ~9 days
  - CSCO and AMZN added cleanly within all sizing and sector constraints; CSCO immediately positive
  - Correctly excluded NVDA (earnings May 20, within 6-day window), QCOM (technical breakdown -11%), PLTR (sell-the-news pattern): discipline held
  - Sector concentration remained low: IT 14.8%, Comm Services 4.8%, Consumer Discretionary 4.8%; no sector > 30%
- What didn't:
  - Portfolio underperformed SPY for the week (-0.31% vs +0.36%, delta -0.67 pts); only ~24% capital deployed limits absolute return capture
  - Pre_market and market_open routines did not run May 11-12; market_open/midday also absent May 13 — 3 days of reduced monitoring. Positions and stops held fine, but any intraday breach would have gone undetected at the midday check
  - CSCO hard stop was placed 1 day late: filled May 14 but stop order 54eb2e8d not confirmed in Alpaca until May 15 market_open. Strategy.md requires immediate placement after fill
  - AMD closed -4.64% intraday on May 15 (threshold: -5% midday cut); midday check at 12:05 showed only -3.74% so rule did not trigger — but AMD came within 36 bps of the cut threshold at EOD
  - AMZN opened red from the first day; early execution risk when entering on the day of a post-earnings gap-up catalyst
- Rule adherence: one breach — CSCO stop placed 1 day late (plan.md had $108.10 stop; market_open May 14 could not place it because the CSCO fill was still pending confirmation; stop placed at market_open May 15). All other rules clean: sizing ≤5% ✓, cash floor 75.8% >> 10% ✓, sector caps all < 30% ✓, new positions 2/3 this week ✓, max concurrent 5/8 ✓, no orders outside market hours ✓, DRY_RUN: false maintained correctly ✓
- Proposed rule changes (for human review, not applied automatically):
  - Add "orphan stop queue" to market_open: at the start of every run, before any other logic, scan portfolio.md for positions missing a stop_order_id and place those stops first. This resolves the late-day-fill gap where a fill is confirmed after the normal stop-placement window.
  - Add trailing-stop pre-alert to pre_market: once any position crosses +8% unrealized, flag in plan.md notes that the +10% trailing stop trigger is imminent and the next market_open should have the trailing order ready to submit immediately.
  - Investigate why pre_market/market_open/midday did not run May 11-12 and market_open/midday did not run May 13. If routines are cron-triggered, verify the scheduling mechanism has not drifted or missed wake-up events.

---

## Week of 2026-05-18

- Perf: portfolio +0.38% vs SPY +0.89% (delta −0.51 pts) | equity $100,264→$100,647; SPY $739.10→$745.67
- Trades: 5 fills (4 buys: GEV, MSFT, NVDA + GLW buy; 1 midday-cut sell: GLW); 1 closed trade
- Win rate: 0 wins / 1 closed = 0% (GLW only)
- Avg win: N/A | Avg loss: −5.40% (GLW: −$266.50)
- Best (open unrealized at May 22 close): AAPL +9.82% ($310.90 vs avg $283.10) — Q2 FY2026 beat thesis intact; within $0.51 of +10% trailing-stop trigger $311.41 with WWDC June 8 as next catalyst
- Worst closed: GLW −5.40% (−$266.50) — bought May 18 on Q1 blowout + Nvidia $3.2B partnership; cut same day per mandatory −5% intraday rule; thesis intact at exit (macro-driven selloff, not GLW-specific); stock subsequently traded $169–$180, below exit price of $179.54, confirming the rule saved incremental loss
- What worked:
  - Mandatory −5% midday cut on GLW worked correctly: rule preserved capital even though thesis was intact; subsequent price action ($169–$180 vs $179.54 exit) validated the rule
  - GEV immediate winner (+5.57% at May 22 close): Q1 blowout + S&P 100 index addition + $10B buyback + dividend raise; backlog $163B provides multi-year earnings visibility
  - AMD advancing strongly (+10.89% unrealized at May 22 close) on OpenAI 6GW + Meta $60B multi-year MI450 demand; trailing-stop trigger $463.75 crossed May 22; AMD all-time high $481.41 on May 22
  - AAPL approaching +10% trailing-stop trigger (closed May 22 at $310.90, trigger at $311.41 — $0.51 gap); WWDC June 8 catalyst ahead
  - Portfolio outperformed SPY on the two down days (May 18: −0.30% vs −0.09% is worse, but May 19: −0.35% vs −0.62% outperformed by +0.27pp)
  - IT sector concentration stayed well under 30% cap at 24.8% (AAPL + AMD + CSCO + MSFT + NVDA at May 22 close)
- What didn't:
  - Portfolio underperformed SPY week overall (+0.38% vs +0.89%, delta −0.51 pts); low deployment (38% in equities, 62% cash) limits upside capture on strong up days (May 20: SPY +1.02%, portfolio +0.64%)
  - GLW entry timing poor — opened on a major risk-off day (Iran drone strike, 10-yr yield 4.63% multi-month high, SPY futures −0.5%); no intraday catalyst to distinguish entry vs waiting
  - AMZN mildly underwater (−0.86% unrealized at May 22 close); AWS thesis intact but macro/FCF-narrative headwinds slow the recovery
  - GOOGL mildly underwater (−3.06% at May 22 close); DOJ antitrust overhang and Moody's risk-off pressure on growth stocks continue
  - NVDA post-earnings sell-the-news (−2.33% at May 22 close); expected after 20% pre-earnings run; thesis strongly intact (Q2 guide $91B, +4.8% above consensus)
- Rule adherence: BORDERLINE breach — 4 new positions opened this week (GLW May 18, GEV May 19, MSFT May 20, NVDA May 21); strategy.md cap is 3/week. May 20 pre_market correctly noted "3/3 cap reached" after MSFT, but market_open May 21 still purchased NVDA (reasoning: GLW was opened+closed same day, so treated as not consuming a weekly slot). This interpretation is not specified in strategy.md and represents an inconsistency — flagged for human review. All other rules clean: sizing all ≤5% at entry ✓, cash floor 62% >> 10% ✓, IT sector cap 24.8% < 30% ✓, concurrent 8/8 (full after NVDA) ✓, no orders outside market hours ✓, DRY_RUN: false ✓
- Proposed rule changes (for human review, not applied automatically):
  - Clarify "new positions opened per week: 3" — explicitly state whether a position opened and closed same day (via midday cut) counts toward the cap. Recommended: yes, it consumes a weekly slot (research, placement, and risk exposure all occurred). This would have blocked NVDA on May 21, though the NVDA blowout was arguably the highest-quality setup of the week.
  - Add macro-conditions filter: when S&P 500 futures are down >0.4% AND 10-yr yield is at a multi-month high on the same pre-market session, defer new entries by 1 trading day. GLW would have been avoided under this rule. The risk-off signal was clear from multiple sources.
  - Carry forward: implement "orphan stop queue" from prior week recommendation (AMZN stop "$248.14 (stop f87a7a95)" and CSCO stop "$108.10 (stop 54eb2e8d)" both appear confirmed by May 26; verify these are active in Alpaca on every market_open run).

---

## Week of 2026-05-26 (first trading day; Mon May 25 = Memorial Day — 4-day week)

- Perf: portfolio +0.62% vs SPY +1.43% (delta −0.81 pts) | equity $100,647→$101,269; SPY $745.67→$756.34
- Trades: 0 fills, 0 closed trades (2 trailing stop conversions: AMD May 26, AAPL May 27); win rate N/A
- Avg win: N/A | Avg loss: N/A (no closed trades)
- Best (open unrealized): AMD +22.16% ($421.59 avg_cost; trailing stop HWM $527.20, stop $490.30) — OpenAI 6GW + Meta $60B MI450 multi-year demand thesis; conversion executed cleanly May 26 at +14.52% trigger
- Worst (open unrealized): NVDA −4.79% ($223.30 avg_cost, current $212.59) — post-earnings sell-the-news pattern after 20% pre-earnings run; stop $205.43 ACTIVE with 5.4% cushion
- What worked:
  - AMD trailing stop conversion executed cleanly May 26 (trigger $463.75 crossed at open); Alpaca auto-managed HWM $480.79→$527.20 over the week, stop lifting to $490.30 — protecting +22% gain on a position that was entered at +14.5%
  - AAPL trailing stop conversion executed May 27 ($311.41 trigger crossed at 09:39); HWM $315.00, stop $292.95; position now +9.94% with downside protected by Alpaca trailing
  - MSFT inflected strongly this week (+8.79% unrealized by week-end, was +1.52% Monday open); Bill Ackman $2B+ Pershing Square disclosure May 28 + Microsoft Build 2026 catalyst ahead; trailing trigger $453.89 within striking distance ($11.17 gap at close)
  - CSCO turned comfortably positive (+2.84%); BofA PT $135 intact; HSBC double-upgraded to Buy (PT $137 from $77) on May 26–27; AI hyperscaler order momentum well-supported
  - AMZN recovered from −2.21% Monday to +0.31% Friday; Snowflake $6B AWS deal + ARK/institutional buying signals; thesis intact
  - Pre-market thesis checks caught all key catalyst events: MSFT trailing trigger imminence, NVDA stop proximity, GEV first bearish analyst note — no surprises at market_open on any day
  - 10-yr yield eased significantly: 4.67% peak (May 20) → 4.44% (May 29); macro tailwind for high-multiple growth names building into next week
  - All 8 stop orders confirmed active at every market_open and midday check; zero reconciliation failures all week
- What didn't:
  - Portfolio underperformed SPY all 4 trading days and week overall (+0.62% vs +1.43%, −0.81 pts delta); primary structural cause: 61.5% cash drag — market rallied and the majority of capital sat uninvested
  - NVDA sell-the-news continued (−4.79% unrealized); stop $205.43 is the tightest cushion in the portfolio (5.4%); this is expected behavior after a 20% pre-earnings run but the stop proximity makes NVDA the weekly risk watch
  - GOOGL underperforming (−3.85% unrealized) despite Q1 EPS +94% beat thesis; DOJ antitrust appellate process + AI search monetization uncertainty are persistent valuation headwinds; thesis intact but mark-to-market drag
  - GEV gave back gains (−2.82% unrealized from entry); first bearish analyst valuation note emerged May 28; UBS $1,400 PT thesis intact, but valuation debate between electrification growth bulls and "disconnected from physical limitations" bears is now active
  - 8/8 concurrent capacity cap blocked entry into PWR (Q1 +35% EPS beat, record backlog $48.5B, PT UBS $900) and ANET (Q1 +10.1% beat, 27.7% revenue growth guidance) — both high-conviction setups fully researched and waiting; opportunity cost clearly visible
  - AMZN slow to recover despite the strongest fundamental catalyst of any position (Q1 EPS +70% beat); FCF compression narrative persists as overhang even though it's capex-cycle-driven
- Rule adherence: clean — 0 new positions this week (0/3 weekly cap ✓); all 8 stops confirmed active every session ✓; no orders outside regular market hours ✓; all positions ≤5.0% of equity at entry and current (well under 11% cap ✓); IT sector 25.3% of equity (AAPL+AMD+CSCO+MSFT+NVDA) < 30% cap ✓; cash floor 61.5% >> 10% ✓; trailing stop conversions correctly executed per plan ✓; DRY_RUN: false ✓
- Proposed rule changes (for human review, not applied automatically):
  - Consider raising max concurrent positions from 8 to 10: with 8 slots continuously full and high-quality post-earnings setups (PWR, ANET, ETN) waiting on the bench, the cap is generating visible opportunity cost drag every week. The existing risk guardrails — 11% size cap, 10% cash floor, 30% sector cap — already prevent concentration risk from additional positions. Adding 2 slots would allow ~$9–10K more equity deployment without breaching any sector or sizing limit.
  - MSFT trailing stop alert for next pre_market (May 30 or next open): trigger $453.89 is +10% vs avg_cost $412.63; current $448.92 (gap $4.97/1.1% at this snapshot); next market_open must be ready to immediately cancel stop 790e2653 and place trailing stop at 7% below peak if MSFT opens ≥$453.89.
  - NVDA stop monitoring: $205.43 hard stop (5.4% cushion from $212.59 current) remains the portfolio's primary daily risk; trailing stop trigger is +10% = $245.62 (still $33 away). No rule change needed — just flag as the highest-priority daily watch item for every pre_market and market_open scan until cushion widens above 8%.

---

## Week of 2026-06-01

- Perf: portfolio −2.80% vs SPY −2.50% (delta −0.30 pts) | equity $101,269→$98,430; SPY $757.30→$738.34
- Trades: 11 fills (6 closed, 3 new opened); 2 stop-converts (MSFT Jun 1, CSCO Jun 5); win rate 2/6 = 33.3%
- Avg win: +10.70% | Avg loss: −8.20%
- Best: AMD +16.33% (+$757.31) — BIS export control Jun 1 closed third-country MI350x loophole; Alpaca-managed trailing stop fired at $490.30 (HWM $527.20); core US demand thesis (OpenAI 6GW, Meta $60B) intact at exit; held 26 days; clean execution
- Worst: GOOGL −8.71% (−$413.92) — Alphabet $80B equity offering (Jun 2 pre-market) gapped stock below $364.07 stop at open; holding period 27 days; dilutive raise mirrors META/MSFT selloff pattern from prior weeks; thesis partially invalidated
- What worked:
  - AMD trailing stop executed cleanly — converted at +14.52% on May 26, Alpaca auto-ran HWM to $527.20 and stop to $490.30; exit at +16.33% (peak +22.16%) without manual intervention
  - Mechanical stops worked exactly as designed on every exit: all four losses (GOOGL, HPE, AMZN, NVDA) hit −8% per strategy; no rule overrides or "just this once" exceptions
  - MSFT trailing stop converted Jun 1 at +12.30% (trigger $453.89 crossed in pre-market); stop fired Jun 3 morning at +5.07% — exited a winning position without discretionary interference
  - Portfolio outperformed SPY on the worst day of the week (Jun 5: −1.55% vs SPY −2.46%, +0.91 pp alpha); multi-sector positioning cushioned the selloff
  - Sector and concentration discipline held all week: IT peaked at 26.3% < 30% cap ✓; all 3 new entries (HPE, PWR, SNDK) within weekly 5-slot cap; cash floor 62–70% well above 10% minimum ✓
- What didn't:
  - Portfolio underperformed SPY for the week (−2.80% vs −2.50%, −0.30 pts); four of six closed trades hit the maximum −8% stop — stop cluster in a single week is the model's primary source of drawdown when it occurs
  - HPE same-day blowup: entered at gap-up open (Jun 2), sizing correction added shares at 10:53 ET, stop fired after hours at 16:22 ET after the stock completed its full gap fill; thesis was intact at market close; the after-hours GTC fill on a paper account is a known risk that converted an intraday winning position into a max-loss outcome
  - Three unrelated macro/regulatory events drove three separate stops in five sessions: GOOGL $80B equity raise (Jun 2), AMZN continued macro decline (Jun 3), NVDA export-control selloff + SPY −2.46% (Jun 5) — bad-luck clustering, but the four simultaneous −8% outcomes in a week underscore why the 10% cash floor and 11% position cap exist
  - Export controls impacted AMD (Jun 1 BIS loophole closure) and NVDA (Jun 5 broader regulatory selloff) within the same week; this risk factor has now appeared in three separate sessions and is structural for semiconductor holdings
  - GOOGL $80B equity offering was not foreshadowed in pre_market; no screening step currently checks for pending SEC shelf registrations or prospectus filings that could indicate an imminent dilutive raise
- Rule adherence: mostly clean
  - HPE initial position undersized (~5% vs 11% target) due to routine prompt error; corrected same session at 10:53 ET with second buy and stop re-placement; wash-trade sequencing (cancel-stop → buy → new-stop) executed correctly; brief window with no stop during correction ⚠️
  - CSCO trailing stop conversion carried 1 day (Jun 4 close trigger → Jun 5 open; hard stop 54eb2e8d remained active overnight — stop coverage was continuous throughout) — minor timing ✓
  - HPE GTC stop fired at 16:22 ET (after regular-hours close): paper-account behavior; flagged for human review; no explicit strategy.md rule on after-hours GTC fills; stop was placed correctly per rules
  - New positions 3/5 this week (HPE + PWR + SNDK) ✓; concurrent peak 8/8 (Jun 1–2, now 5/8 ✓); all sector caps clean ✓; DRY_RUN: false ✓
- Proposed rule changes (for human review, not applied automatically):
  - Add SEC EDGAR shelf-registration check to pre_market catalyst scan for each existing position: scan 424B, S-3, and S-1 filings in the prior 30 days. The GOOGL $80B offering (424B1 filed Jun 2 morning) gapped the stop by $2.85 at open — a pre-market flag would have allowed a proactive exit above the stop price.
  - Add export control monitoring to pre_market thesis check for all semiconductor and IT positions: Commerce Dept BIS guidance updates, Entity List changes, and executive orders affecting chip exports. AMD (Jun 1) and NVDA (Jun 5) were both impacted in the same week; this risk is now demonstrated as material and recurring.
  - Review GTC stop behavior on paper account for after-hours fills: HPE stop fired at 16:22 ET (22 min after close). If paper account consistently fills GTC stops after hours, consider requiring DAY stops (re-entered each session) or adding logic to cancel and re-enter stops at market_close to avoid unintended after-hours fills.
  - Clarify sizing-correction process in market_open: when a pre_market position sizing calculation uses a different equity basis than the actual open equity (resulting in wrong share count), the correction buy should be logged as part of the original entry with full thesis re-verification, not treated as a separate decision. Add explicit share-count validation step to market_open before submitting any order.

---

## Week of 2026-06-08 (PARTIAL — mid-week run on Tue Jun 9 eve; only Jun 8–9 sessions completed)

_Note: this review was invoked mid-week (Tue 2026-06-09 ~20:23 ET), not at the usual Friday 16:30 ET. It covers the two completed sessions of the week (Mon Jun 8, Tue Jun 9). Numbers are week-to-date EOD marks; the normal Friday review will close out the full week._

- Perf: portfolio −0.28% vs SPY −0.05% (delta −0.23 pts) | equity $98,430→$98,151 (EOD marks, Fri Jun 5 close → Tue Jun 9 close); SPY IEX 737.45→737.07. Live equity at run time $98,338.60.
- Trades: 3 fills (all Jun 9, all mechanical stop exits; 0 buys); 3 closed trades
- Win rate: 2 wins / 3 closed = 66.7%
- Avg win: +2.17% | Avg loss: −8.01%
- Best: AAPL +4.24% (+$204.28) — trailing stop 4225eab6 fired 10:03 ET (17@$295.116471, HWM $317.40), held 34 days. Thesis intact at exit (WWDC 2026 Gemini-Siri overhaul, Q2 FY2026 rev +17% YoY, Services ATH $31B); pure mechanical trailing-stop execution on a broad-selloff open, NOT a thesis break. Locked in the gain from the May 27 +10% trailing conversion.
- Worst: GEV −8.01% (−$319.18) — hard stop 68f84ddd fired 10:17 ET (4@$916.67), held 21 days. Thesis (Gas Power + Electrification data-center orders, FY2026 guide raised $44.5–45.5B) intact at exit; the Vineyard Wind court ruling (May 29) was correctly judged Wind-segment-only and NOT thesis-invalidating. Stop fired on a gap-down open after the position sat at CRITICAL <1.5% cushion for multiple sessions; never worked from entry. Missed ex-div Jun 16 ($2.00) by the stop.
- Thesis audit:
  - AAPL — thesis held up; exit was mechanical (trailing stop), not a thesis failure. Trailing stop did its job: protected a position that ran to HWM $317.40 and gave back to $295.12 on the WWDC sell-the-news + macro selloff. Win.
  - CSCO — thesis intact (AI networking structural demand, hyperscaler orders triple-digits YoY). Trailing stop 5dccb5cd fired 12:38 ET at +0.10% (HWM $126.435 → exit $117.54). The 7% trail let a position that had been +7–10% round-trip to breakeven in a single down session. Pattern repeat of give-back risk on wide trails during sharp single-day selloffs.
  - GEV — thesis intact but the position never traded positive over its 21-day life and sat at CRITICAL stop cushion (1.06–1.50%) for days before the −8% hard stop finally fired. Correctly NOT cut early on the Vineyard Wind ruling; let the mechanical stop handle it.
  - Common pattern: all three exits clustered on a single broad-selloff session (Jun 9). 2 of 3 were winners locked in by trailing stops (system working as designed); 1 was the −8% hard stop on a chronically-underwater name. Zero discretionary overrides — clean mechanical execution.
- What worked:
  - Trailing stops on AAPL (+4.24%) and CSCO (+0.10%) executed cleanly and without discretion → 2/3 wins, 66.7% win rate on the week's closed trades
  - Discipline under ELEVATED_BAR held: 8 candidates researched Jun 9 (CRM, INTC, TTWO, META, AVGO, ADBE, ORCL, MRVL), 0 qualified (>20% EPS bar + step-f RS / step-g consensus-PT screens); no forced entries
  - Correctly held GEV through the Vineyard Wind court ruling as a Wind-division-only event (not a guidance cut / earnings miss / fraud / material thesis catalyst) rather than panic-cutting; mechanical stop took the exit
  - Portfolio outperformed SPY intraday on the Jun 9 down day (+0.16 pp per EOD log); multi-name positioning cushioned the selloff before the stops cleared
  - Reconciliation clean both sessions; all stops confirmed active every run; DRY_RUN: false maintained
- What didn't:
  - Portfolio underperformed SPY week-to-date (−0.28% vs −0.05%, −0.23 pts)
  - CSCO trailing-stop give-back: HWM $126.435 → exit $117.54 (+0.10%); the 7% trail let a +7–10% position round-trip to breakeven on one selloff day. Late conversion (Jun 4 close trigger → Jun 5 open) plus the wide trail meant almost none of the gain was realized
  - GEV chronic underwater hold: never positive across 21 days, sat at <1.5% stop cushion (CRITICAL) for multiple sessions before stopping at the full −8%
  - Stop-cluster on a single day (Jun 9): 3 simultaneous exits left the book at 2 positions / ~79.5% cash — heavy cash drag now limits upside capture
  - Deployment very low (~20% invested): ELEVATED_BAR (>20% EPS for ALL sectors) + strict step-f/g screens have produced 0 qualifiers for many consecutive sessions; the cash drag is a real and persistent opportunity cost
- Rule adherence: clean
  - 0 new positions opened this week (0/5 weekly cap ✓); no sizing decisions to breach the 11% cap
  - Cash floor: 79.5% cash >> 10% minimum ✓ (well above — the issue is too much cash, not too little)
  - Sector cap: post-exits the book is PWR (Industrials) + SNDK (IT) — each well under the 30% cap ✓
  - All stops confirmed active every session ✓; no orders outside regular market hours ✓; DRY_RUN: false ✓
- Proposed rule changes (for human review, not applied automatically):
  - Trailing-stop give-back: CSCO round-tripped from +7–10% to +0.10% under the 7% trail in a single down session. strategy.md already chose 7% over 12% for IT, but consider adding a partial profit-lock at the +10% trailing-conversion trigger (e.g., sell 1/3 of the position) so a subsequent sharp selloff can't erase the entire unrealized gain. Would have banked part of CSCO's run.
  - Cash-drag under prolonged ELEVATED_BAR: with ~80% cash and 0 qualifiers across many sessions, the >20%-EPS-all-sectors + step-f/g combination may be over-restrictive when sustained for weeks. The overlay is "raise the bar, not halt" by design, but a multi-week 0-entry / 80%-cash streak is a measurable opportunity cost. Suggest the human review whether (a) the health threshold (currently 0, untuned) should be recalibrated, or (b) ELEVATED_BAR should slightly loosen the step-f/g RS screens while keeping the higher EPS bar.
  - Chronic-underwater review: GEV was never positive over 21 days and sat at CRITICAL (<1.5%) cushion for multiple sessions before stopping at −8%. Consider a "never-worked" flag in pre_market: if a position has not closed green on any session within N days of entry AND its stop cushion is persistently <2%, surface it for proactive human review (not auto-cut — thesis can still be intact, as GEV's was).

---

## Week of 2026-06-08 (FULL-WEEK close-out — supersedes the mid-week PARTIAL entry above)

_This is the normal Friday 2026-06-12 16:30 ET review covering the complete Mon Jun 8 → Fri Jun 12 week. It closes out and supersedes the PARTIAL entry above (which only covered Jun 8–9). Performance measured Jun 5 close → Jun 12 close from Alpaca portfolio/history (base_value $98,284.44 asof Jun 5 → live equity $99,623.30 at Fri close) and SPY IEX daily closes ($737.45 → $741.67)._

- Perf: portfolio **+1.36%** vs SPY **+0.57%** (delta **+0.79 pts — OUTPERFORMED**) | equity $98,284.44→$99,623.30; SPY $737.45→$741.67
- Trades: 5 fills (4 closing sells Jun 9–10 + 1 opening buy CASY Jun 11); 1 trailing-stop conversion (SNDK Jun 12, order-mgmt only, not a fill); 4 closed trades
- Win rate: 2 wins / 4 closed = **50.0%**
- Avg win: **+2.17%** | Avg loss: **−8.04%**
- Best closed: **AAPL +4.24% (+$204.28)** — trailing stop 4225eab6 fired Jun 9 10:03 ET (17@$295.116471, HWM $317.40), held 34 days. Thesis intact at exit (WWDC 2026 Gemini-Siri overhaul, Q2 FY2026 rev +17% YoY, Services ATH $31B); pure mechanical trailing-stop on a broad-selloff open, NOT a thesis break. Locked in the gain from the May 27 +10% trailing conversion.
- Worst closed: **PWR −8.07% (−$855.59)** — hard stop 10b684b0 fired Jun 10 11:15 ET (15@$650.01), held 8 days. Thesis intact at exit (FY2026 guide raised rev $34.7–35.2B / adj EPS $13.55–14.25, record ~$50B backlog, Oppenheimer Outperform PT $800). Stopped on a risk-off tape (U.S.–Iran escalation near Strait of Hormuz, May CPI +4.2% YoY first >4% print since 2023, SPY −1.36% day) — pure mechanical stop execution, not a company event.
- Thesis audit (all 4 closed trades — thesis was intact at every exit; all exits mechanical, zero discretionary overrides):
  - AAPL — thesis held; trailing stop did its job, protecting a position that ran to HWM $317.40 and gave back to $295.12 on the WWDC sell-the-news + macro selloff. Win.
  - CSCO — thesis intact (AI networking structural demand, hyperscaler orders triple-digits YoY). Trailing stop 5dccb5cd fired Jun 9 12:38 ET at +0.10% (HWM $126.435 → exit $117.54). The 7% trail let a +7–10% position round-trip to breakeven in a single down session. **Give-back pattern repeat** (3rd consecutive week flagged).
  - GEV — thesis intact but the position never traded positive over its 21-day life and sat at CRITICAL stop cushion (1.06–1.50%) for multiple sessions before the −8% hard stop fired Jun 9. Correctly NOT cut early on the Vineyard Wind court ruling (Wind-segment-only, not a guidance cut / earnings miss / fraud). Missed ex-div Jun 16 ($2.00) by the stop.
  - PWR — thesis intact; stopped Jun 10 on the U.S.–Iran/Strait-of-Hormuz + CPI risk-off tape, not a company catalyst. Held 8 days. Pure mechanical −8%.
  - Common pattern: 3 of 4 exits (AAPL, GEV, CSCO) clustered on the single Jun 9 broad-selloff session; PWR followed Jun 10 on the macro escalation day. All four theses were intact at exit — these were mechanical risk-management exits, not stock-picking failures. The week's two survivors (SNDK, CASY) carried the outperformance.
- What worked:
  - **Portfolio beat SPY for the week (+1.36% vs +0.57%, +0.79 pts)** — the first clear weekly outperformance in the recent log, driven almost entirely by SNDK's AI-NAND run to +20.6% and a well-timed CASY entry; mechanical stops cleared the four underperformers/chronic-underwater names cleanly
  - SNDK ran to +20.6% unrealized on the AI-NAND upcycle (NAND supply-constrained into 2028, fresh PT raises Cantor $2,900 / BofA $2,100 / Mizuho $2,200); the +10% trailing-stop conversion executed cleanly Jun 12 09:33 ET (cancel hard stop 9362a074, place 7% trail 36402808), then ratcheted HWM $1,872.74→$2,021.65 / stop $1,741.65→$1,880.13 intraday — locking the gain mechanically
  - CASY entry (Jun 11, 11@$900.626364) was the ONLY candidate to clear the ELEVATED_BAR >20% EPS bar across the entire week: Q4 FY2026 EPS $4.37 = +30% beat (+66% YoY), 4 consecutive quarters beating, FY2027 guide raised, added to S&P 500, 27th consecutive dividend increase (+14% to $0.65); sized at 10.1% < 11% cap
  - Mechanical stops executed without discretion on all 4 exits — zero rule overrides, zero "just this once" exceptions; trailing stops protected the AAPL gain
  - Discipline under ELEVATED_BAR held all week: many candidates screened and correctly rejected (ADBE +6.43% EPS, ORCL +11.64%, DG +5.8%, STRL +57.46% but 38d-stale, CRM/META/AVGO step-f RS-negative, TTWO/INTC/MRVL step-g) — only CASY's +30% beat qualified
  - Reconciliation clean every session; all stops confirmed active at every pre_market/market_open/midday/market_close run; DRY_RUN: false maintained throughout
- What didn't:
  - Two −8% stops in the week (GEV −8.01% Jun 9, PWR −8.07% Jun 10) — GEV was a chronic underwater hold (never positive across 21 days), PWR a macro-driven stop on the U.S.–Iran escalation day; both theses intact at exit
  - **CSCO trailing give-back recurs**: HWM $126.435 → exit $117.54 (+0.10%); the 7% trail let a +7–10% position round-trip to breakeven on one selloff day. This is the 3rd straight week this give-back pattern has appeared on a wide-trail name during a sharp single-day decline
  - **Cash drag is the dominant structural issue**: the book sat at ~78% cash for most of the week; the ELEVATED_BAR (>20% EPS for ALL sectors) overlay produced only 1 qualifier (CASY) across five sessions of screening. Outperformance this week came in spite of ~80% idle capital, not because of full deployment — on a stronger up-week the cash drag would have cost relative return
  - Stop-cluster front-loaded the week: 3 exits Jun 9 + PWR Jun 10 dropped the book to 2 positions / ~80% cash by mid-week, leaving little working capital to capture the back-half recovery (SPY $725.58 Jun 10 → $741.67 Jun 12)
- Rule adherence: **clean**
  - New positions: 1 opened this week (CASY Jun 11) vs ELEVATED_BAR cap of 2/week → 1/2 ✓ (strategy.md base cap is 5/week; ELEVATED_BAR tightens to 2)
  - Sizing: CASY 10.1% < 11% cap ✓; no other entries
  - Cash floor: 78–90% cash all week >> 10% minimum ✓ (the problem is too much cash, not too little)
  - Sector caps: Consumer Staples (CASY) ~10%, IT (SNDK) ~12% at week-end — both far under the 30% cap ✓
  - All stops confirmed active every session ✓; SNDK +10% trailing conversion executed correctly per plan Jun 12 ✓; no orders outside regular market hours ✓; DRY_RUN: false ✓; reconciliation 2/2 zero divergence at this review ✓
- Proposed rule changes (for human review, not applied automatically):
  - **Partial profit-lock at the +10% trailing-conversion trigger** (carry-forward, now 3rd week): CSCO again round-tripped a +7–10% gain to +0.10% under the 7% trail. Consider selling 1/3 of the position at the +10% trigger so a subsequent sharp selloff cannot erase the entire unrealized gain. This is directly relevant NOW: SNDK is sitting at +20.6% under a 7% trail (HWM $2,021.65) — a single −7% session would give back ~$420/share of locked HWM gain on the same mechanic that cost CSCO its run.
  - **Recalibrate or sunset the ELEVATED_BAR overlay given the SPY recovery**: pead_health.md expires today (Jun 12) and universe_refresh recomputes Sunday. SPY closed Jun 12 at a fresh $741.67 (well above the 200MA $685.79), risk-on macro (U.S.–Iran peace-deal optimism), yet the realized-health reading (−2.08%, threshold untuned at 0.0) has held the bar at >20%-all-sectors for many weeks, yielding ~1 qualifier/week and ~80% cash. Recommend the human review whether (a) the 0.0 threshold should be tuned, or (b) ELEVATED_BAR should slightly loosen the step-f/g RS screens while keeping the higher EPS bar — the multi-week 0–1 qualifier / 80% cash streak is now a measured, recurring opportunity cost. Note the documented lag: realized health stays ELEVATED_BAR into a fresh recovery, which may be exactly the current situation.
  - **"Never-worked" chronic-underwater flag** (carry-forward): GEV again illustrates it — never green over 21 days, CRITICAL (<1.5%) cushion for multiple sessions before the −8% stop. Suggest a pre_market surface (not auto-cut) when a position has not closed green within N days of entry AND its stop cushion is persistently <2%.
  - Still pending from prior weeks (no new instances this week, keep on the list): SEC EDGAR shelf-registration scan in pre_market (GOOGL $80B raise precedent) and BIS export-control monitoring for semiconductor/IT positions (AMD/NVDA precedent).

---

## Week of 2026-06-15 (4-session week — Fri Jun 19 = Juneteenth market holiday; review runs Friday regardless)

_Normal Friday 2026-06-19 16:30 ET review. NYSE was CLOSED Fri Jun 19 (Juneteenth) — Alpaca /v2/clock returned next_open 2026-06-22, and no Jun 19 daily bar exists for any symbol, so the trading week was Mon Jun 15 → Thu Jun 18 (4 sessions). Performance measured Fri Jun 12 close → Thu Jun 18 close (prior-Friday-close → week-end-close convention) from Alpaca portfolio/history (base $99,624.45 asof Jun 12 → equity $99,246.04 at Jun 18 close) and SPY IEX daily closes ($741.67 → $746.75)._

- Perf: portfolio **−0.38%** vs SPY **+0.68%** (delta **−1.06 pts — UNDERPERFORMED**) | equity $99,624.45→$99,246.04; SPY $741.67→$746.75
- Trades: 1 fill (SNDK trailing-stop sell Jun 16; 0 buys, 0 trailing conversions); 1 closed trade
- Win rate: 1 win / 1 closed = **100%**
- Avg win: **+22.53%** | Avg loss: **N/A (no losing trades this week)**
- Best: **SNDK +22.53% (+$2,221.84)** — Alpaca-managed 7% trailing stop 36402808 fired Jun 16 11:39 ET (6@$2,014.00 avg, HWM $2,167.33), held 11 days (Jun 5→Jun 16). Thesis intact at exit (2026 NAND capacity sold out, $42B backlog, PTs $2,200–$2,900) — pure mechanical trailing-stop on a name that ran the AI-NAND upcycle to +30%+ then gave back 7% intraday. NOT a thesis break.
- Worst: **N/A** — the only closed trade was a win. (Live laggard is CASY: held since Jun 11, never green, closed the week −6.48% with hard-stop cushion down to ~1.6% — see "what didn't.")
- Thesis audit:
  - SNDK — thesis held up; exit was mechanical (trailing stop), not a thesis failure. The trail did exactly its job: it let SNDK run far past the +10% conversion trigger (HWM $2,167.33, +30%+) and then locked a large +22.53% realized gain when the name pulled back 7% intraday. This is the trailing system working as designed on a genuine runner — the opposite of the CSCO give-back problem (CSCO round-tripped +7–10% to +0.10% because it never ran far past +10%). Note SNDK was on a FULL-position 7% trail (converted Jun 12, before the strategy.md partial-profit-lock edit), so all 6 shares exited on the trail; the new sell-1/3-at-+10% rule was never applied. For a runner like SNDK the full trail captured MORE than the partial rule would have — the partial-lock rule helps give-back names (CSCO) but mildly caps runners. Net outcome here was excellent.
  - CASY (open) — thesis intact (Q4 FY2026 EPS $4.37 = +30% beat / +66% YoY, FY2027 guide raised, 27th consecutive dividend increase, added to S&P 500, 4-quarter beat streak; fresh bullish PTs Evercore $915 / Wells $910), but the position has NEVER closed green since the Jun 11 entry at $900.63 and drifted down all week ($871.97 Jun 15 → $842.31 Jun 18, −6.48%). Correctly NOT cut (no guidance cut / miss / fraud / negative catalyst; strategy.md bars cutting on temporary weakness). This is the GEV "never-worked" pattern repeating — see proposed rule changes.
  - Common pattern: the only realized trade was a clean mechanical win; the book's drag is the chronic-underwater CASY hold and ~90% idle cash, not stock-picking failure.
- What worked:
  - **SNDK trailing stop captured +22.53% (+$2,221.84) mechanically** — the single largest realized win in the recent log; the 7% trail let the AI-NAND runner extend to +30%+ HWM and still banked a +22.5% gain with zero discretionary intervention. Trailing-stop system working exactly as designed on a true runner.
  - Discipline under ELEVATED_BAR held all 4 sessions: candidates screened and correctly rejected (CRM step-f anti-PEAD drift, HPE step-d/f drift-failed + already stopped, TJX +8.9%<20%, MRVL +1.3% EPS / above-consensus-PT step-g, INTC speculative Trump/Apple headline step-g); 0 forced entries
  - Portfolio OUTPERFORMED SPY on the down day Jun 17 (−0.15% vs SPY −1.27%, +1.12 pp) — the ~90% cash cushion damped the down tape
  - Reconciliation clean every session (0 divergence); CASY hard stop 33027bf9 $828.58 confirmed active every run; SNDK exit cleanly explained by confirmed fill (not a divergence); DRY_RUN: false maintained throughout
- What didn't:
  - **Portfolio underperformed SPY for the week (−0.38% vs +0.68%, −1.06 pts)** — SPY rallied hard early (Jun 15 +1.74% on the U.S.–Iran peace deal) while the book sat ~78%→91% cash; after the SNDK exit Jun 16 the remaining holding (CASY) drifted lower, so the portfolio captured the downside (CASY −6%) without the index's upside
  - **CASY chronic-underwater ("never-worked")**: bought Jun 11 at $900.63, never closed green, ended the week at $842.31 (−6.48%) with hard-stop cushion compressed to ~1.6% (it sat at 0.95% on the Jun 18 intraday low). Same profile as GEV (stopped −8% after never working). Thesis is genuinely intact, but a single down leg likely fires the mechanical −8% stop near $828.58.
  - **Cash drag remains the dominant structural issue**: after the SNDK exit the book is 1 position / ~91% cash; ELEVATED_BAR (>20% EPS all sectors) produced 0 qualifiers across all 4 sessions. This is now a multi-week pattern — ~1 qualifier every week or two, ~80–90% idle capital — a measured, recurring opportunity cost that this week directly cost relative return on a SPY up-week.
  - **Operational gap: pre_market did NOT run for Jun 17** (no plan written, no universe screen) — surfaced by market_open + midday Jun 17. Risk management (market_open/midday/market_close) still ran and the open book + stops were unaffected, but the morning screen/plan was skipped for one session. Recurrence of the "missed scheduled run" issue flagged in prior weeks.
- Rule adherence: **clean**
  - New positions: 0 opened (ELEVATED_BAR cap 2/week → 0/2 ✓; strategy.md base cap 5/week)
  - Sizing: no entries → no 11% breach
  - Cash floor: 78%→91% cash all week >> 10% minimum ✓ (problem is too much cash, not too little)
  - Sector caps: Consumer Staples (CASY) ~9.5%, IT (SNDK, until Jun 16 exit) ~12% — both far under the 30% cap ✓
  - All stops confirmed active every session ✓; SNDK trailing-stop exit mechanical per Alpaca order 36402808 ✓; no orders outside regular market hours ✓; DRY_RUN: false ✓; reconciliation 1/1 zero divergence at this review (CASY 11 @ $900.626364 matches Alpaca /v2/positions) ✓
  - Non-rule operational note (not a trading breach): pre_market run missing Jun 17 (scheduler gap)
- Proposed rule changes (for human review, not applied automatically):
  - **"Never-worked" chronic-underwater flag** (carry-forward, now CASY is the live example after GEV): CASY has not closed green on any session since the Jun 11 entry and its hard-stop cushion compressed to <2% (0.95% intraday Jun 18). Suggest a pre_market SURFACE (not auto-cut — thesis can stay intact, as CASY's is) when a position has not closed green within N days of entry AND its stop cushion is persistently <2%, so the human can decide whether to hold into the likely −8% mechanical stop or exit proactively above it.
  - **Recalibrate or sunset the ELEVATED_BAR overlay** (carry-forward, now multi-week): SPY closed Jun 18 at $746.75, firmly above the 200MA (~$688), strong bull regime, yet the untuned realized-health threshold (0.0) has held the bar at >20%-all-sectors for many consecutive weeks, producing 0 qualifiers this week and ~90% cash. pead_health.md (computed Jun 14, ELEVATED_BAR, realized −1.025%, expires Jun 21) recomputes this Sunday — recommend the human review whether (a) the 0.0 threshold should be tuned off the multi-week 0–1-qualifier / ~85% cash streak, or (b) ELEVATED_BAR should slightly loosen the step-f/g RS screens while keeping the higher EPS bar. Documented lag caveat: realized health stays ELEVATED_BAR into a fresh recovery, which is plausibly the current situation.
  - **Partial-profit-lock observation** (rule now LIVE in strategy.md): SNDK predated the sell-1/3-at-+10% edit (converted to a full trail Jun 12) and exited the full 6 shares at +22.53% — for a runner that extends well past +10%, the full trail outperforms the partial-lock. The rule's value is concentrated in give-back names (CSCO type) that stall just past +10%; it mildly caps true runners. No change recommended — just observe how the rule behaves on the next +10% crossing now that it is active.
  - **Investigate the missed pre_market run on Jun 17** (carry-forward of the "missed scheduled run" item): one of four sessions this week had no pre_market screen/plan. If routines are cron/trigger-driven, verify the scheduler did not drift or miss a wake-up; the gap leaves a session with no morning research even though risk management still ran.
  - Still pending from prior weeks (no new instances this week, keep on the list): SEC EDGAR shelf-registration scan in pre_market (GOOGL $80B raise precedent) and BIS export-control monitoring for semiconductor/IT positions (AMD/NVDA precedent).
