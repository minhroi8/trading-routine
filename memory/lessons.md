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
