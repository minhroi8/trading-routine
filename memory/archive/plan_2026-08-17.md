# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-17 (pre_market ~08:40 ET)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 9 | $1,205 | $1,108.60 | **Eli Lilly — Health Care — score 7/10 (DOWN from 8/10 on momentum decay; ENTRY-SAFETY LEG).** Q2 2026 (Aug 5 BMO): **rev $22.97B +48% YoY = +11% beat** (Mounjaro $9.9B +91%, Zepbound $4.9B); adj EPS $8.38 NOISY (incl. ~$3.03/sh IPR&D charge) → qualifies on **operational EPS beat >15% + analyst-revision/catalyst-exempt basis**; **FY26 rev guide RAISED $85–87B**. **Earnings streak 4 qtrs (+1).** **Gap +6.15%** (Aug4 $1,117.47→Aug5 open $1,186.24; normal 5–10%). **Reaction-day vol 2.18x** 20d-avg (strong confirmation). **52wk-hi $1,248.53 on 2026-07-07 = 28 td ago (top-priority <45d band), −5.46% below.** ⚠️ **RS 5-day spread NEGATIVE −0.88pp** (Aug7 $1,185.96→Aug14 $1,180.33 = −0.48% vs SPY +0.41%); drift-since-reaction only +0.10pp (Aug5→Aug14 +0.94% vs SPY +0.85%) — **post-earnings drift has DECAYED: topped Aug 10 $1,230.90, now −4.11% off peak, price $1,180.33 BELOW 21d EMA $1,184.75 (−0.37%).** **Sector XLV vs SPY 20d −0.55pp** (Health Care lagging, step i.iii −1pt). **Analysts: 5+ PT raises, 0 downgrades**, Strong Buy consensus, avg PT ~$1,251–1,277. **Short interest ~1%** (neutral). **Insider: routine 10b5-1 sells, no buying** (neutral). Mgmt (Ricks): *"Lilly's momentum continues… we delivered 48% revenue growth and raised our full-year guidance."* **FRESH POSITIVE catalyst: UK MHRA approved orforglipron (Foundayo) ~Aug 11 — Europe's first oral GLP-1 weight-loss approval; stock dipped only ~2.25% (profit-taking, not breakdown).** **Top risk:** ~45x P/E + MFN/TrumpRx pricing overhang + Novo oral-GLP-1 competition — none a 42-day binary; −8% stop protects. **Regulatory: shelf CLEAN (no S-3/offering — mega-cap), BIS N/A (pharma).** Next earnings ~Oct 29 (not <3d ✓); active/tradable NYSE ✓. **ENTRY-SAFETY LEG (CAT-precedent): price is below the 21d EMA → market_open MUST enter ONLY on an EMA/ORB reclaim (Gate 4/6); if the drift stays rolled over, defer again (would be 7th consecutive defer) — do NOT chase below trend.** |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME (Industrials, 13 @ $834.12) — no exit criterion fired: not −8% (mark ~$840.48, +0.76%), not +10% partial-lock/trail trigger, held 12d (not 60d-stale), thesis INTACT/REINFORCED (record Q2 EPS $9.06 +25% surprise, RPO backlog $17.14B +44%, FY26 guide RAISED; PT $1,200 Buy). Hard stop 96e4e855 $767.39 GTC active (cushion ~8.5%). HOLD. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME +0.76% far below the +10% partial-profit-lock/trailing trigger — no conversion. |

## Notes

- **Gates (all PASS):** Gate 1 clock — is_open=false, next_open 2026-08-17T09:30 ET → **opens today (Mon), NOT a holiday** → proceed. Gate 2 reconciliation **1/1 zero divergence**: Alpaca /v2/positions = EME 13 @ $834.12 matches portfolio.md exactly (hard stop 96e4e855 $767.39 GTC); account ACTIVE, trading_blocked=false; **equity $98,349.65**, cash $87,423.41 (88.9%), 1/8 concurrent. Gate 3 universe cache **FRESH** (screened 2026-08-16, expires 2026-08-23, 294 rows).
- **PEAD health FRESH & NORMAL** (computed 2026-08-16, expires 2026-08-23; realized_health_60d **+0.906%**, n=113, health_ok=true) → **standard 15% bar, max 5 new/week (no ELEVATED_BAR)**. First successful pead_health refresh in ~5 weeks (root cause: yfinance curl_cffi TLS reset through egress proxy — fixed via YF_DISABLE_CURL_CFFI=1; **durable fix needs human env-var/code change or it regresses next Sunday**).
- **SPY regime BULL** (Aug 14 IEX close $776.30 > 200MA $702.75, +10.5%) → standard bars.
- **Macro-deferral NOT triggered:** premarket S&P futures **+0.11% (UP)** → "futures down >0.4%" leg FAILS; **10-yr ~4.69%, easing −1bp — NOT a fresh multi-month high** → leg FAILS; both legs required → standard bars. This week: **FOMC minutes Wed Aug 20**, big-box retail earnings (HD Tue; TGT/TJX/LOW Wed; WMT Thu), **Jackson Hole next week (Aug 27–29, Warsh keynote)**. Tone mildly risk-on (AI-capex/Anthropic read-through lifting semis).
- **Weekly slots: 0/5 used** (new week Mon Aug 17; last actual fill EME Aug 5) → 1/5 after LLY.
- **Sizing:** 9 sh × ~$1,180 ≈ $10,620 = **~10.8%** of equity < 20% cap (strategy.md ceiling; routine parenthetical "currently 11%"). Cash floor post-fill ~78% >> 10% ✓. Sectors after fill: Health Care (LLY) ~10.8% / Industrials (EME) ~11.1% — both << 30% ✓. 1→2/8 concurrent ✓.
- **LLY momentum caveat (why 7/10, not 8):** the post-earnings drift has rolled over — trailing-5d RS negative, price below 21d EMA, XLV lagging SPY, −5.46% off 52wk high. Thesis and fresh UK catalyst keep it a qualifier (≥6), but it is planned as an **entry-safety leg**: market_open's EMA/ORB gates are the momentum filter and will defer again if trend is not reclaimed. This mirrors the CAT Aug 6–7 entry-safety handling and the 6 prior LLY Gate-4/6 defers (Aug 7/10/11/12/13/14) — zero capital lost.
- **Fresh-catalyst scan (Aug 11–15 reporters):** NO clean US-listed >15%-EPS-surprise + guidance-raise + multi-day-drift setup. **CAVA (Aug 12, +12%)** EPS beat only ~+6% < 15% bar → logged, not planned. AMD/SMCI/CRWV reported prior week (extended drift; SMCI carries governance + BIS/export-control flags per prior logs) → not fresh. Retail names (HD/TGT/TJX/LOW/WMT) report THIS week — not yet reported. No new watchlist adds.
- **Watchlist:** MRVL active (reports ~late Aug, no in-window catalyst → no plan); WDFC/THC/CLS/BE/EME/FORM/PAYC/NET/TEAM pending_review (human-only — MUST NOT plan). No new pending_review adds this run.
- **Regulatory flags among planned:** NONE (LLY shelf CLEAN / BIS N/A).
- DRY_RUN: false.
