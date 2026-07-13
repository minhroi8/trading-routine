# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-07-13 (pre_market ~08:20 ET) — **NO ORDERS PLANNED (0 qualifiers).**

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | 0 candidates scored ≥6/10 — see Notes for per-candidate drop reasons. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) — nothing to exit. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | 0 positions — no stops to convert. |

## Notes

- **Gates PASS.** Clock: is_open=false, next_open=2026-07-13T09:30 ET → market opens today (Mon), NOT a holiday → routine proceeds. **Reconciliation 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT book (zero divergence). Account ACTIVE, trading_blocked=false; equity $98,266.98, cash 100%, buying_power $393,067.92. 0/8 concurrent.
- **Universe FRESH:** expires_on 2026-07-19 > today (rebuilt 2026-07-12, 305 tickers). Universe-cache hard gate PASSES.
- **PEAD health STALE → NORMAL (bar NOT raised).** pead_health.md expires_on 2026-06-28 < today → per step 1c a stale overlay never raises the bar. Last reading was ELEVATED_BAR (realized −0.492%, n=367, computed 2026-06-21). ⚠️ **4th+ consecutive weekly PEAD_HEALTH refresh MISS** — the Jul 12 universe_refresh rebuilt universe.md but `compute_pead_health.py` again failed (`SPY download failed after 5 retries`; known transport-layer bug — yfinance curl_cffi cannot traverse the TLS-re-terminating agent proxy; plain `requests` returns HTTP 200). NOT self-healing — needs a human/tooling fix. Surfaced continuously since Jun 29.
- **SPY regime: BULL** (close $754.94 [Jul 10 IEX] > 200MA $694.45, n=200, margin +$60.49 / +8.7%). Standard strategy.md thresholds apply: EPS surprise >15% (>20% Utilities/RE/Industrials/Energy; Industrials/Energy also require streak≥2), max 5 new positions/week, no ELEVATED_BAR cap. Weekly new-position slots **0/5** used (week of Mon Jul 13; last buy MU Jun 25 = prior week).
- **Macro:** premarket S&P 500 ~−0.23%, Nasdaq-100 ~−0.86% (mild risk-off); 10-yr ~4.5–4.6%, NOT a multi-month high → macro deferral rule NOT triggered (requires futures <−0.4% AND 10-yr multi-month high).

### Candidate screen — 0 qualified (Q2 season just starting; big-bank flow begins Tue Jul 14–15)

- **MU** (IT, Q3 FY2026 Jun 24, 19d in-window): +23.8% EPS beat ($25.11 vs $20.28), rev +17.6% ($41.46B vs $35.25B), Q4 guide $50B, data-center memory 7× — fundamentally strongest, clears standard 15% bar. **DROP step f (broken drift):** post-earnings drift decisively ROLLED OVER — peak close $1,215.46 (Jun 25) → $979.36 (Jul 10) = **−19.4% off peak**; we were mechanically stopped out −8.08% same-day Jun 25 (thesis intact). Fixed −8% stop sits inside MU's ±6–13%/day range → near-certain noise-stopout; poor risk-adjusted EV. Next earnings ~Sep 22–29. BIS: clean.
- **NKE** (Consumer Disc, Q4 FY2026 Jun 26): +53.8% EPS beat ($0.20 vs $0.13) BUT off a heavily depressed turnaround base; **negative earnings-day reaction** (fell on Greater-China sales −12%); deep multi-quarter downtrend, far below 52-wk high (~$44 now); recent 2-wk recovery ($40.74→$44.39, RS +~1.9pp/5d) is constructive but the beat is low-quality (declining fundamentals, not accelerating). **DROP — scores <6/10** (weak signal quality + negative gap on report + downtrend momentum).
- **GIS** (Consumer Staples, Q4 FY2026 Jul 1, 12d in-window): +17.3% EPS beat ($0.95 vs $0.81) — clears the 15% Staples bar; +8.6% earnings-day gap (Jun 30 $34.81 → Jul 1 $37.80), Jul 1 volume ~2× avg. **DROP — scores <6/10:** FY2027 guidance implies **operating profit −8-13% and declining adj EPS $3.00–3.20** (forward-profit contraction = thesis risk for a multi-week hold); the earnings pop has FADED ($37.80 → $36.22, RS ~flat/slightly negative vs SPY); stock sits far below its $54.18 52-wk high (deep downtrend → step-d downrank). Beat driven by cost savings, not top-line acceleration — a value/turnaround, not a PEAD momentum setup.
- **STZ** (Consumer Staples, Q1 FY2027 Jul 1): +6.85% EPS beat ($3.43 vs $3.21). **DROP — Staples needs EPS surprise >20%;** +6.85% nowhere near the bar.
- **DAL** (Industrials, Q2 Jul 10): +6.1% EPS beat ($1.56 vs $1.47). **DROP — Industrials needs >20% AND streak≥2;** +6.1% fails (2026 backtest: Industrials worst sector, 25% win / −4.82% avg). Shelf-reg/BIS N/A.
- **ACN** (IT, Q3 FY2026 Jun 18): +1.3% EPS beat ($3.80 vs $3.75), **revenue MISS** ($18.72B vs $18.93B est), bookings below prior year. **DROP — +1.3% << 15% IT bar** + revenue miss.
- **MRVL** (watchlist `active`, in universe): no fresh in-window earnings (Q1 FY2027 ~May 27 = ~47d stale, >30d window). **DROP (carried)** — only catalyst is analyst PT hikes; price broke down with the AI-semi complex; trades above/near consensus mean PT (step-g overshoot). Status stays `active` (human-only).

### Watchlist flag (non-universe catalyst → pending_review, NOT tradable today)

- **WDFC** (WD-40 Company, NASDAQ, specialty chemicals / Materials — S&P 600 small-cap, **NOT in universe.md** [likely fails the $20M/day dollar-volume liquidity filter — WD-40 is thinly traded] and NOT previously on watchlist): Q3 FY2026 reported Jul 9 — adj EPS **$2.33 vs $1.57 est = +48.4% beat** (+51% YoY), net sales **$195.1M (+24% YoY)**, beat rev by ~$25M; **RAISED** FY2026 EPS guidance to $6.05–$6.35 (from $5.75–$6.15) + new **$100M buyback**. Compelling catalyst → added to `watchlist.md` as `status: pending_review` + Discord flag. **Do NOT plan a trade until the human sets status to `active`** (and re-verify it clears the liquidity/price filters). One caution for human review: WDFC cut its FY gross-margin outlook to 54.5–55.5% on input-cost pressure.

- **Net: 0 qualifiers, NO BUYS.** Q2 earnings season is just starting — big-bank flow (JPM/GS/WFC/C/BAC Tue Jul 14, BLK/MS Wed Jul 15) and mega-cap tech (Jul 22–30) will refresh the pool. DRY_RUN: false.
