# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-10-22 (Thu) — pre_market

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | **NO QUALIFYING CANDIDATES ≥6/10 under the ELEVATED_BAR >20%-EPS-all-sectors bar.** No universe or active-watchlist name presents a clean, verifiable >20% EPS surprise within the last 30 days with positive post-earnings drift. See Notes. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book is FLAT (0/8 positions, 100% cash). No open positions → no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

**Mode:** DRY_RUN = **false**. Market opens today 2026-10-22 09:30 ET (not a holiday). Book FLAT: 0/8 positions, 100% cash, equity **$96,448.31**.

**Gates (all passed):**
- Clock: `is_open=false` (pre-market ~08:29 ET), `next_open=2026-10-22T09:30 ET` → opens TODAY, not a holiday → proceed.
- Reconciliation **0/0 PASS**: Alpaca `/v2/positions=[]` MATCHES portfolio.md FLAT; zero divergence. Account ACTIVE, trading_blocked=false; equity $96,448.31, cash $96,448.31 (100%), buying_power $385,793.24, long_mv $0.
- Universe cache **FRESH**: screened 2026-10-18, expires 2026-10-25, 274 rows → consumed read-only, no re-screen.

**PEAD signal-health overlay:** posture **ELEVATED_BAR** (FRESH — computed 2026-10-18, expires 2026-10-25; `realized_health_60d_pct` = **−0.447%**, `health_sample_n` = **373**, `health_ok=false`). → EPS-surprise threshold RAISED to **>20% for ALL sectors**; **max 2 new positions** this session. Overlay governs NEW entries only (never halts, never affects exits).

**SPY regime:** BULL — `spy_close` 763.25 > `spy_200ma` 721.88 (per pead_health 2026-10-18) → bear-regime rule NOT active. Effective new-position cap = min(5 base, 2 ELEVATED_BAR) = **2**. Macro-deferral rule MOOT (ELEVATED_BAR already equal-or-stricter). This is the **bull-and-weak** case (SPY above 200MA but realized PEAD drift negative) — exactly what the signal-health leg is designed to catch.

**Overnight / Q3-2026 earnings sweep (step 2) — candidates reviewed and DROPPED (fresh names since Oct-21 run = Oct-21 AMC + Oct-22 BMO reporters):**
- **TSLA** (in-univ, Consumer Disc.) — Q3 (Oct-21 AMC) adj EPS $0.48 vs ~$0.44 = ~+9%; revenue ~$28.05B narrowly MISSED; −3% premarket. FAILS >20%. → DROP.
- **IBM** (in-univ, IT) — Q3 adj EPS $2.95 vs $2.86 = +3.1%; shares −5% after hours. FAILS >20%. → DROP.
- **META** (in-univ, Comm. Services) — Q3 EPS beat ~+7.3%; +~4% AH. FAILS >20%. → DROP.
- **GE** (in-univ, Industrials) — adj EPS $2.25 vs ~$1.99 = +13.1% (up 36% YoY, raised FY to $8.00–8.10); FAILS >20% (Industrials needs >20% AND streak≥2). → DROP.
- **LMT** (in-univ, Industrials) — Q3 beat + raised 2026 guide but only +3% premarket (modest defense-prime beat, nowhere near >20%); Industrials worst-backtest sector. → DROP.
- **FITB** (in-univ, Financials) — Q3 (Oct-19) GAAP EPS **$0.90**; adj EPS $1.13 excludes **$0.23 of Comerica-merger items**; consensus DISPUTED ($0.83 → +36% headline vs Zacks $1.09 → +3.7%); **muted ~+2% reaction** inconsistent with a true +36% surprise → market reads this as a low-single-digit beat. Adjusted/one-time-inflated, M&A-driven, ambiguous magnitude → NOT a clean high-conviction >20% PEAD setup. → DROP.
- **NFLX** (in-univ, Comm. Services) — Q3 (Oct-20) ~+3.6% surprise (per Oct-21 run); FAILS. → DROP.
- **TXN** (in-univ, IT) — Q3 (Oct-21 AMC) cons ~$2.42, guide $2.23–2.57; prior-qtr beat ~+12%; no clean >20% surprise surfaced, not a premarket gainer. → DROP.
- **LRCX** (in-univ, IT/semi) — Q3 (Oct-21 AMC) cons ~$2.15; actual not cleanly indexed; prior-qtr beat ~+8%; not a premarket gainer. No verifiable >20% beat. → DROP.
- **WDC** (in-univ, IT/memory) — Oct-22 result not cleanly verifiable; prior-qtr pattern = beat but SOLD OFF −15% on outlook; memory names reacting poorly. No verifiable clean >20% drift setup. → DROP.
- **BE** (**now in universe cache** row 64 @ $221.25; also watchlist `pending_review`) — Q3 reports TODAY (Oct-22 BMO); **actual not yet available/indexed** → cannot verify EPS surprise or complete deep-research a–i → cannot score. Highly volatile, formerly-unprofitable clean-energy name. → DROP (unverifiable this session; revisit once Q3 actuals publish).
- **Other Oct-21 AMC / Oct-22 BMO in-univ reporters** (TMO, DHR, MCO, CME, BX, URI, HON, UNP, VLO, NEM, CSX, PM, NEE, ELV, CMCSA, AAL) — none surfaced as a clean >20% blowout with a strong positive pop; none appear in today's premarket gainers; Q3-2026 beat magnitudes remain modest. → DROP.

**Active-watchlist review:** MRVL (sole `status: active` watchlist ticker, IT/semi) — last earnings Aug-27 (~56 days, OUTSIDE 30-day window), no fresh ≤30d catalyst, next report ~late Nov. → DROP. All other watchlist tickers are `status: pending_review` (human-gated) and MUST NOT be planned until a human sets them `active`.

**Non-universe compelling-catalyst review (step 2) — NO WATCHLIST ADDS:**
- **HAS (Hasbro, Consumer Disc., NOT in universe/watchlist)** — initial sweep snippet showed a garbled "+55.9%" beat, but verification against the SEC 8-K + TheFly shows actual Q3 adj EPS ≈ **$1.68 vs ~$1.63–1.88 consensus = roughly IN-LINE**, and the quarter is **inflated by one-time tariff-refund benefits** ($7M operating / $48M in Consumer Products adj op profit). NOT a clean >20% earnings surprise → **NOT added** (same adjusted/one-time trap as FITB).
- **BHVN +35% / PRDO / KMTS / AVEX** (today's premarket gainers) — not S&P 1500; BHVN is a biopharma clinical/regulatory catalyst, not an earnings PEAD beat. Not added.
- **SPOT (+5% on guidance) / DECK** — not in universe/active-watchlist; no clean verified >20% earnings surprise this session. Not added.

**Macro backdrop:** Q3-2026 season mid-stream — aggregate EPS surprise running only low-single-digit (~+2.6% per recent FactSet, "few large individual surprises"); heaviest reporting weight lands Oct 28–Nov 3. The >20%-all-sectors bar continues to find no qualifiers in this weak-surprise tape — the 5th consecutive pre_market session (Oct 16/19/20/21/22) with 0 buys. Consistent with the lessons.md observation that prolonged ELEVATED_BAR produces high cash drag by design ("raise the bar, not halt").

**DECISION:** 0 candidates cleared the initial >20%-EPS-in-30d + positive-drift + clean-quality gate → deep-research steps a–i not warranted (routine MUST NOT score ≥6 without completing a–i; conversely no name reached that stage). **Plan NO buys** — plan fewer rather than lower the bar. Book stays FLAT (0/8, 100% cash).

**Sanity check vs strategy.md:** cash 100% (≥10% floor ✓); concurrent 0/8 (≤8 ✓); weekly new 0/2 (ELEVATED_BAR cap ✓; last trade DELL exited 2026-09-24); sector caps N/A (flat). Regulatory scans (shelf-reg / BIS): none reached deep research. Watchlist flags: NONE new.

**⚠️ Carry-forward human flags (non-blocking, moot with no buys):**
- Doc discrepancy: `routines/pre_market.md` says target_qty sized per strategy.md "Max position size at entry (currently 11%)" but `strategy.md` field reads **20%**. strategy.md wins per CLAUDE.md. Flagged for human to reconcile.
- `memory/portfolio.md` bloat (~400KB accumulated audit-comment history, exceeds single-read limit) — recurring human-trim flag (NOT auto-trimmed; deleting audit history needs human sign-off).

DRY_RUN: false
