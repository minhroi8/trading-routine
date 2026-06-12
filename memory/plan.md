# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-06-12 (Friday)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | No candidate cleared the ELEVATED_BAR >20% EPS-surprise bar. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Both open positions (CASY, SNDK) — theses intact, no exit criterion fired. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| SNDK | 9362a074 | $1,512.20 | Cancel hard stop → place 7% trailing stop GTC | 7% below peak (Alpaca-managed) | +10% trigger $1,808.06 crossed; SNDK now +15.18% vs entry $1,643.693333 (cur ~$1,893). market_close 2026-06-11 flagged this; market_open MUST convert immediately (cancel 9362a074 first to avoid wash-trade block, then place trailing). |

## Notes

- **Gates:** clock PASS (is_open=false, next_open=2026-06-12T09:30 ET — market opens today, Friday, not a holiday); reconciliation PASS 2/2 (CASY 11 @ $900.626364 ✓, SNDK 6 @ $1,643.693333 ✓ — zero divergence vs Alpaca `/v2/positions`); universe cache fresh (expires 2026-06-14). DRY_RUN: **false**.
- **PEAD signal-health overlay: ELEVATED_BAR** (fresh — `pead_health.md` expires_on 2026-06-12 = today, not past). realized_health_60d_pct = **−2.08%**, health_sample_n = **211**, health_ok = false. For this session: EPS-surprise bar raised to **>20% for ALL sectors**, max new positions capped at **2**.
- **SPY regime: BULL** — live SPY close $737.67 (Jun 11 IEX) > 200MA $685.79 (n=200). Normal regime; ELEVATED_BAR is the binding (stricter) constraint. Combined new-position cap = 2.
- **Macro:** S&P 500 futures **+0.18%** (risk-on — Trump/Iran peace-deal optimism, U.S. strikes called off; WTI −3.97% to ~$84; SpaceX IPO debut ~$75B). Futures NOT down >0.4% → **macro deferral rule NOT triggered** (and moot — bar already >20% via ELEVATED_BAR).
- **Weekly slots:** 1/2 used this week (CASY opened Jun 11). 1 slot remains under the ELEVATED_BAR cap of 2 — but no qualifier today.
- **Candidates screened (0 qualified):**
  - **ADBE** (IT) — Q2 FY2026 reported Jun 11 after close: non-GAAP EPS $5.96 vs $5.60 = **+6.43% beat**. Fails the >20% ELEVATED_BAR bar (and the standard 15% bar). Revenue $6.62B +13% YoY, FY26 guide raised, AI-first ARR tripled >$500M — strong fundamentals but EPS surprise too small. **DROP step a.**
  - **ORCL** (IT) — Q4 FY2026 (Jun 10): EPS beat ~**+11.64%**; below the >20% bar. Plus plans to raise ~$20B more capital for data centers (FCF negative). **DROP step a.**
  - **DG** (Consumer Staples) — Q1 (this week): EPS $2.00 vs $1.89 = **+5.8% beat**, FY26 guide raised — below >20% bar. **DROP step a.**
  - **STRL** (mid, infrastructure/Industrials) — Q1 2026 EPS $3.59 vs $2.28 = +57.46% surprise, but reported **May 5 = 38 days ago, OUTSIDE the 30-day catalyst window**. Stock already ran +46% to ~$881 (52-wk-high chase). **DROP (stale catalyst).**
  - **CBRL** — not in S&P 1500 universe (and not on watchlist). Not considered.
  - **CRM / META / AVGO** — carried-forward **step f** disqualifications (negative RS vs SPY, multi-week post-earnings downtrends). One risk-on session (Jun 12) does not flip multi-week relative-strength downtrends.
  - **TTWO** — carried-forward **step g** (GTA6 delayed twice; further-delay risk within 42d). **INTC** — carried-forward **step g** (trades above max analyst PT). **MRVL** (watchlist, active) — carried-forward **step g** (mean PT below price; reassess post-Jun 22 S&P 500 inclusion if PTs materially raised).
- **Regulatory scans:** none run (no candidate reached step h). No new shelf-registration / equity-offering / BIS export-control flags surfaced for held names (CASY, SNDK).
- **Open-position thesis checks (HOLD both):**
  - **CASY** (Consumer Staples, opened Jun 11, held 1d, +3.28% cur ~$930): thesis intact/reinforced — added to S&P 500, quarterly dividend +14% to $0.65 (27th consecutive annual increase), FY27 guide raised. No negative catalyst. Stop 33027bf9 $828.58 active.
  - **SNDK** (IT, opened Jun 5, held 7d, **+15.18%** cur ~$1,893): thesis strongly reinforced — AI NAND/memory upcycle (Morgan Stanley: DRAM/NAND supply-constrained into AI ramp); fresh PT raises BofA $2,100, Cantor $2,900, Mizuho $2,200. No exit criterion fired. **Crossed +10% trailing trigger → conversion required at market_open (see table above).** Stop 9362a074 $1,512.20 active until converted.
- **Watchlist flags:** none added. No compelling catalyst surfaced for a ticker outside universe + watchlist.
- **Account:** equity $99,488.29, cash $77,897.31 (78.3%), 2/8 concurrent. Sectors: Consumer Staples ~10.3% (CASY), IT ~11.4% (SNDK) — both << 30% cap.
