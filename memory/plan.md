# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

**2026-07-28** (pre_market ~08:18 ET). Prior plan (2026-07-27) archived by market_close 2026-07-27.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 qualifiers — see Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8 positions, 100% cash) — no positions to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**NO BUYS, NO SELLS, NO CONVERSIONS — 0 qualifiers (8th consecutive ~0-qualifier session).**

**Gates (all PASS):**
- Clock: `is_open=false`, `next_open=2026-07-28T09:30 ET` → market opens today (Tue), NOT a holiday → routine proceeds.
- Reconciliation 0/0 PASS: Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT book — zero divergence. Account ACTIVE, `trading_blocked=false`, `account_blocked=false`; equity $98,266.98, cash $98,266.98 (100%), buying_power $393,067.92. 0/8 concurrent.
- Universe cache FRESH: `expires_on 2026-08-02` > today (screened 2026-07-26, 287 rows).

**Overlays / regime:**
- **PEAD health STALE** — `pead_health.md` `expires_on 2026-07-26` < today 2026-07-28 → posture treated **NORMAL but flagged STALE**; **bar NOT raised** (step 1c: a stale overlay never raises the bar; the universe-cache gate is the hard halt and it PASSES). Last fresh reading (computed_on 2026-07-19): NORMAL, realized_health_60d **+1.225%**, n=318, health_ok=true.
- **SPY regime BULL** — latest trade $739.20 > 200MA $698.87 (n=200, +$40.33 / +5.77%; Jul 27 close $738.85). Standard thresholds: EPS >15% (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also streak≥2), max 5 new/week.
- **Macro-deferral NOT triggered** — premarket S&P 500 futures UP ~+0.9% (NDX ~+1.6%; Dow +0.7% on SHW/KO) → "futures down >0.4%" leg fails; 10-yr Treasury ~4.64% pulling back off last week's high (highest since Jan 2025) → not both legs.

**Screen result — 0 qualified.** Q2-2026 late-July tape dominated by a **memory-chip selloff** (MU/WDC/SK Hynix/Samsung crashing on memory-glut fears → semis avoided). The clean in-universe beats are all sub-15% or distorted:
- **SHW** (Materials) — Q2 adj EPS $2.35 vs $2.27 = **+3.5%** << 15%. DROP.
- **KO** (Cons Staples) — Q2 adj EPS $0.97 vs $0.93 = **+4.3%** << 15%; raised FY comparable-EPS growth to 9–10% (from 8–9%), but a guidance raise on an earnings-driven entry is NOT EPS-exempt (only analyst-revision / partnership catalysts are). DROP.
- **GOOGL** (Comm Svcs) — Q2 (Jul 22) GAAP EPS $9.11 vs $2.88 = +216% headline is **entirely a one-time ~$37.7B mark-to-market gain** on Anthropic/SpaceX stakes; ex-item EPS would have **MISSED** $2.63 consensus by ~$0.01; revenue beat only +2.8%; stock **FELL ~7%** on capex surge = anti-PEAD. DROP.
- **NOC** (Industrials) — Q2 adj EPS $7.68 vs $6.82 = **+12.66%** << **>20% Industrials bar** (two program charges held it back). DROP.
- **JPM** (Financials) — Q2 (Jul 14, 14d ago, drift window elapsed) headline $7.70 vs $5.55 = +38.7% but includes a $4.6B Visa windfall + $1.0B equity gains; **ex-Visa adj $6.14 = +10.6%** << 15%. DROP (stale + clean surprise sub-bar).
- **CVS** (Health Care) — the +16.47% beat ($2.57 vs $2.18) was **Q1 reported MAY 2026** (>60d, out of 30-day window); Q2 due Aug 5. DROP (stale signal).
- Other mid-July financials (GS +44% / TRV +85% / MS / WFC / C) all reported ~Jul 14–17 (drift elapsed) with headline surprises inflated by one-time trading/cat gains — no fresh clean PEAD.

**Watchlist flag (pending_review, human-only to activate):**
- **CLS (Celestica)** — Q2 (Jul 27 AC) revenue **$4.70B +62% YoY** (Comms/Cloud +84%), RAISED FY26 revenue guide to **$20.5B** (from $19.0B; vs $19.15B consensus), stock **+7%** = compelling non-universe catalyst → added to `watchlist.md` as `pending_review` + Discord flag. MUST NOT plan until human sets `active`. (EPS surprise only ~7.5% / 5-q streak — catalyst is the revenue beat + guidance raise, not a >15% EPS surprise.)
- **APLD (Applied Digital)** noted (fiscal Q3 +142.9% EPS beat, rev +139% YoY) but NOT flagged — serial diluter (chronic equity offerings = step-h.i dilution-risk profile) + speculative AI-datacenter micro. Logged in research_log only.

**Regulatory scan:** N/A (0 candidates reached shortlist / plan). No shelf-reg or BIS flags on any planned buy (0 planned).

**Sanity check vs strategy.md:** cash floor 100% ≥ 10% ✓; concurrent 0 ≤ 8 ✓; new-this-week 0 ≤ 5 ✓; no sector exposure. Nothing to trim.
