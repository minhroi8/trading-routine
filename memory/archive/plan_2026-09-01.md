# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-01 (pre_market run ~08:2x ET). Regime **BULL**, PEAD posture **NORMAL (flagged STALE)**. **0 candidates ≥6/10 → NO planned buys.** Book stays FLAT (0/8, 100% cash).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | No candidate scored ≥6/10 — see Notes. Plan fewer rather than lower the bar (routine + strategy.md). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT — no open positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates (all PASS → proceed):**
- **Clock:** `is_open=false`, `next_open=2026-09-01T09:30 ET` → market opens TODAY (Tue), NOT a holiday → proceed (pre-market run).
- **Reconciliation 0/0 PASS:** Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT — zero divergence; no open/orphan orders. Account ACTIVE, `trading_blocked=false`; **equity $97,328.01** (=cash 100%), 0/8 concurrent.
- **Universe FRESH:** screened 2026-08-30, expires 2026-09-06, 259 rows → freshness gate PASSES (hard gate).
- **⚠️ PEAD health STALE:** `pead_health.md` `expires_on=2026-08-30` is in the PAST (compute_pead_health.py Yahoo IP rate-limit miss on the Aug-30 refresh — documented, recurring). Per step 1c: **treat posture NORMAL but flagged STALE → do NOT raise the bar** (universe-cache is the hard gate; it passed). Last real reading (2026-08-23): NORMAL, realized_health_60d +2.284%, n=91. → **standard 15% bars, max 5 new/week.**
- **SPY regime BULL:** Alpaca IEX 200-day: SPY $766.87 (Aug 31 close) > 200MA $710.24 (+8.0%); bear rule NOT active → standard thresholds, max 5 new/week.
- **Macro-deferral NOT triggered:** premarket S&P futures **~+0.04% (UP)** → "down >0.4%" leg FAILS; 10-yr **~4.75% = multi-month high** (US–Iran hot war, oil Brent ~$90, Fed rate-hike fears) satisfies its leg, BUT BOTH required → standard bars stand (no >20% override). Risk-off tape noted; strategy.md says do NOT skip entries — be selective.

**Candidates evaluated → 0 qualified ≥6/10:**
- **CRWD** (CrowdStrike, IT, in univ) — **strongest momentum name; DROPPED on the 15% EPS bar.** Q2 FY27 (Aug 26 AC): clean **EPS surprise only ~7%** ($0.31 vs $0.29) < 15% IT earnings bar. The rally was driven by **record net-new ARR $332.8M (+51% YoY)** + rev $1.47B +26% + RAISED guidance, not the EPS surprise. Genuinely clean PEAD *pattern*: corrected −18% into the print ($225 Aug13→$185.32 Aug25), then **+23.0% reaction Aug 27** ($185.32→$227.99) and drifted UP to a **fresh 52wk high ~$230.98 (Aug 31)**; vol Aug27 ~3.4x; XLK +4.65% vs SPY +1.21% (20d, IT leading). But strategy.md's 15% clean-EPS-surprise bar governs **earnings-driven entries**, and the enumerated exemptions are **analyst-revision / partnership** catalysts — a guidance raise alone is NOT an enumerated exemption. Same disciplined treatment as NVDA (+6%), VEEV (+6%), ADSK (+6%) this cycle. **⚠️ HUMAN FLAG:** this is arguably a *cleaner* PEAD setup than the CRM the routine planned on 2026-08-31 (CRM used a "guidance-raise + Anthropic-**partnership** catalyst-exempt" framing; CRWD lacks a partnership). Applied the letter of strategy.md (drop); flagging the consistency question for human review. NOT planned (planning it would override the 15% bar without explicit human authorization).
- **XYZ** (Block, Financials/fintech, in univ) — **DROPPED: failed PEAD (negative reaction/drift).** Q2 (Aug 5 AC): clean **EPS surprise +18.6%** ($1.02 vs $0.86) clears the 15% bar; rev $6.62B (+1.2% beat); RAISED FY26 guide (gross profit $12.51B +21%, adj EPS to +70% YoY). BUT market SOLD it: reaction day Aug 6 **−6.1%** ($84.22→$79.06); 27 days later still BELOW pre-earnings level (Aug 31 $82.03). Negative earnings-day reaction + no positive drift → step-f DROP. Catalyst also aging (27d, edge of 30d window).
- **PANW** (Palo Alto Networks, IT, in univ) — **DROPPED: earnings window.** Reports **TODAY Sept 1 after close** (Q4 FY26) → inside the 3-day earnings window (event risk tonight) → cannot enter pre-earnings per step 4 / strategy.md.
- **WAT** (Waters, Health Care, in univ, at 52wk high) — **DROPPED on EPS bar.** Q2: adj EPS $3.05 vs $3.01 = **+1.3% surprise** ≪ 15% HC bar; modest guidance raise + instrument-replacement-cycle momentum, not a clean EPS-surprise PEAD input.
- **FTNT** (Fortinet, IT, in univ, at 52wk high) — **DROPPED: catalyst >30d old.** Reported Jul 29 (34 days ago) → outside the 30-day fresh-signal window; drift was already spent/reversed (dropped 5/10 on 2026-08-26; Piper downgrade). At a 52wk high now on momentum, but no fresh ≤30d earnings catalyst.
- **MRVL** (active watchlist, IT/semi) — **DROPPED: negative drift (sold the news).** Q2 (Aug 27 AC) rev beat + raised FY28 ~$18B outlook but ~0% EPS surprise and **sold the news −8%+**; now ~$180 (down from $241 post-print) → negative PEAD step-f. No fresh positive catalyst.
- **PLTR** (IT, in univ) — **DROPPED: catalyst stale + chase.** Aug 3 report (29 days ago), drift largely spent, previously flagged extended/chase; little PEAD runway left.
- Other fresh late-Aug reporters checked and dropped: **NVDA** (+6% EPS surprise < bar), **VEEV** (+6%), **ADSK** (−5% sell-the-news), **HP** (−4% negative reaction), **NetApp** (modest beat), **Dell** (extreme +260% YTD chase). The strongest fresh >15% beats (**AFRM** ~+100%, **AMBA** +27%, **OKTA** +17%, **EL** +22%, **HAE** +34%, **CAVA** +35%) are all **watchlist `pending_review`** (human-only to activate) → MUST NOT plan.

**Decision:** 0 candidates ≥6/10 → plan NO buys (routine + strategy.md: plan fewer rather than lower the bar). Book stays FLAT (0/8, 100% cash), 6th consecutive session with ~0 qualifiers as Q2 earnings season winds down. Planned sells: none (flat book). Weekly slots 0/5 unused. **No new watchlist adds** — the compelling non-universe catalysts are already on `watchlist.md` as `pending_review`; today's candidates (CRWD/XYZ/PANW/WAT/FTNT/PLTR/MRVL) are all in-universe or already active. Regulatory flags among planned: **NONE** (no buys).

⚠️ Sizing note (informational, no buys today): pre_market.md "(currently 11%)" vs strategy.md `Max position size at entry` field "20%" — precedent has sized ~11% within the 20% cap; flagged for human. DRY_RUN: false.
