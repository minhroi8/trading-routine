# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

**2026-09-15** (Tue) — drafted by `pre_market` ~08:1x ET. DRY_RUN: **false**. Book FLAT (0/8, 100% cash, equity $97,328.01).

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| DELL | 20 | $535.00 | $492.20 | **Score 8/10.** Dell Q2 FY2027 (reported AC 2026-09-01, reaction Sep-2): **adj (non-GAAP) EPS $7.04 vs $4.92 cons = +43.1% surprise** (≫15% IT bar); **rev $46.97B +58% YoY (+4.6% beat)**; ISG $31.8B +89%. **RAISED FY27 guide to ~$192B rev (from $167B) / ~$25.50 adj EPS (+42.5% mid)**; Q3 guide $49B/$6.50 (vs $41.4B/$4.48 cons) — massive. AI orders $60.9B, **backlog ~$95B**. **Earnings streak: ~10 straight beats** (3+ → +1 signal). **Earnings-day gap +8.52%** (5–10% band, no adj). **Volume 4.03x** 20d-avg on reaction (strong institutional confirmation). **52-wk high $567.52 on 2026-09-11 = 3 sess ago** (top-priority recency), **but pulled back to $534.06 Sep-14 (−5.9% off ATH in one session — top risk, see notes)**. **RS vs SPY +3.21% (5d) / +8.78% (20d)** — outperforming. **Sector XLK 20d −1.03% vs SPY** (money mildly rotating out of tech → −1 momentum). Analysts: Citi & BofA Buy, PT raised to **$600** (~41% upside), "more room to run"; no downgrades. **Short interest ~5% float** (neutral). **Insider: aggressive scheduled selling, 0 buys/90d** (10b5-1 diversification → −1 risk, not thesis-breaking). Mgmt (CFO Kennedy): *"AI momentum is accelerating."* **Top risk: Sep-14 −5.9% reversal off the Sep-11 ATH — parabolic PEAD run may be pausing/topping.** **Regulatory scan: shelf-reg CLEAN** (S-3ASR is the routine automatic WKSI shelf filed 2026-06-11; NO equity offering announced; Dell is a net repurchaser + raised guide — not a dilutive draw); **BIS CLEAN** (server OEM, not a chip designer; no material ≤30-day BIS rule/entity-list change gating Dell's China revenue; the Singapore end-user-fraud case is third-party enforcement, not a Dell-revenue restriction). Next earnings **Dec 1, 2026** (>3d ✓). Alpaca asset `active`/`tradable`, no halt. Sub-scores: signal 3 / momentum 2 / confirmation 2 / risk 1. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | Book FLAT (0/8) — no open positions, no exit criteria to evaluate. | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates (all PASS):**
- **Clock:** `/v2/clock` is_open=false, `next_open`=2026-09-15T09:30 ET → opens today (Tue), NOT a holiday → proceed (pre_market runs pre-open by design).
- **Reconciliation 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT — zero divergence. Account ACTIVE, equity **$97,328.01** (=cash 100%), 0/8 concurrent.
- **Universe cache FRESH:** screened 2026-09-13, `expires_on`=2026-09-20 (future) → freshness gate PASSES; 227 rows; no re-screen (universe_refresh owns screening).

**Overlays / regime:**
- **PEAD health STALE:** `pead_health.md` `expires_on`=2026-09-13 is in the PAST (recurring weekly-refresh miss). Per step 1c: **treat posture NORMAL but flagged STALE → do NOT raise the bar** (universe-cache is the hard gate, and it passed). Last real reading (2026-09-06): NORMAL, realized_health_60d +0.03%, n=186 (drift essentially FLAT — near the ELEVATED_BAR flip; watch next refresh). → standard 15% bars, max 5 new/week.
- **SPY regime BULL:** fresh Alpaca IEX 200-day — SPY $760.75 (Sep-14) > 200MA **$712.50** (+6.8%); bear rule NOT active → standard sector thresholds, max 5 new/week.
- **Macro-deferral NOT triggered:** S&P futures **−0.2%** premkt → "down >0.4%" leg FAILS; 10-yr **~5.04% = highest since 2007 (multi-year high)** satisfies its leg BUT both required (AND) → standard bars (no >20% override). (Moot for DELL: +43% clears >20% anyway.) Elevated-yield / pre-FOMC risk-off tape noted — be selective; DELL −8% stop caps shock.

**Candidates researched (5 examined, 1 qualified ≥6/10):**
- **QUALIFIED → DELL (IT, in univ) 8/10** — see buy row. (7th consecutive DELL plan; Sep-3/8/9/10/11/14 all deferred at market_open on chase-guards 6d/6e — deferred NOT dropped; re-planned. **Guard for market_open:** post-pullback this is less of a chase, but standard 6d/6e opening-range guards still apply; do not chase above ORH.)
- **DROPPED → CRM (Salesforce, IT, in univ)** — headline non-GAAP EPS $5.90 vs $3.27 (+80%) is inflated by a **one-time $2.6B strategic-investment gain (+$2.53/sh)**; **clean operating EPS ≈$3.37 vs $3.27 = ~+3% surprise ≪ 15% IT bar**; revenue in-line (+0.3%); organic FY27 guide raise only +$100M ($200M of the +$300M is Contentful/Fin M&A) — too thin to qualify as a "clear catalyst." Strong tape (gap +12.6%, vol 5.26x, +32% 20d RS) but the fundamental surprise is manufactured → below 6. (Consistent with 08-31/09-01/09-02/09-09 CRM drops.)
- **DROPPED → MDB (MongoDB, IT, in univ)** — beat +18% EPS & raised guide but **stock FELL −12.5%** on Atlas-growth-slowdown fears → negative step-f reaction/drift.
- **DROPPED → ORCL (Oracle, IT, in univ)** — Q1 FY27 (Sep-10): adj EPS $1.92 vs $1.74 = **+10.3% ≪ 15% bar**; rev +0.8%; record RPO $664B (+$209B YoY) is a real backlog catalyst BUT market rejected it — **closed ~2% LOWER** on cash-flow concerns; analysts mixed (BMO cut PT to $195) → negative reaction, sub-bar.
- **DROPPED → AVGO (Broadcom, IT, in univ)** — Q3 (reaction Sep-8): gap +1.65%, **vol 1.03x (weak)**, drifting **−6.51% since**, 52-wk high 103d ago, RS −2.46%/−12.31% vs SPY → failing on every leg.
- **DROPPED → MRVL (active watchlist, IT/semi)** — Q2 FY27 (Aug-27) beat + raised FY guide but **negative earnings-day gap −6.71%** (sold the news), RS slightly negative, 52-wk high 88d ago → negative step-f.

**Sizing:** 11% of equity ($97,328.01 × 0.11 = $10,706) → DELL 20 sh @ $535 = **$10,700 = 11.0%** (<20% strategy.md cap ✓; stop $535×0.92=$492.20 = −8% ✓).

**Sanity check (strategy.md):** cash floor after fill ~89% (≥10% ✓); max concurrent 0→1 (≤8 ✓); max new/week 0→1 (≤5 ✓, bull regime); **IT sector exposure 1 position ~11% (<30% cap ✓** — note: all recent strong beats are IT; 2 IT ≈22% would still fit, 3 would breach ~33%, so the pool + cap naturally limit to ≤2 IT — moot today with 1 buy). Regulatory flags among planned: **NONE** (DELL shelf CLEAN, BIS CLEAN).

**Watchlist flags:** NONE — no compelling catalyst on a ticker outside universe+active-watchlist (all of today's candidates are in-universe or already active-watchlist).

**Standing human flags (unchanged):**
- ⚠️ **Sizing ambiguity:** `pre_market.md` line 99 says "(currently 11%)" while `strategy.md` `Max position size at entry` field = **20%**. Sized ~11% per precedent (within the 20% cap). Please reconcile the two files.
- ⚠️ **portfolio.md bloat (~308KB)** — the single FLAT-book "thesis" cell is a giant run-on paragraph, exceeds the single-read limit. Recurring human-trim flag.
- ⚠️ **PEAD-health weekly refresh** keeps going stale (recurring). Prior note: set `YF_DISABLE_CURL_CFFI=1` in the routine env so `compute_pead_health.py` stops silently failing.
