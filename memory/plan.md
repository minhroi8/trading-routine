# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

**2026-09-17** (Thu) — drafted by `pre_market` ~08:1x ET. DRY_RUN: **false**. Prior plan archived: 2026-09-16 → `memory/archive/plan_2026-09-16.md`.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| DELL | 19 | $565.00 | $519.80 | **Dell Technologies (Information Technology, in universe, ADV ~$124M) — score 8/10.** Q2 FY27 (reported Sep-1 AC) **adj EPS $7.04 vs $4.92 cons = +43.1% surprise** (≫15% IT bar); rev $46.97B **+58% YoY / +4.6% beat**; ISG $31.8B +89%; **RAISED FY27 guide to ~$192B rev / ~$25.50 adj EPS (+42.5% mid)**; Q3 guide $49B/$6.50; AI-server orders $60.9B, record ~$95B backlog. **Earnings streak ~10 quarters** (multi-quarter, +1). **Earnings-day gap +8.52%** (5–10% band, no adj). **Volume 4.03x** 20-day avg on reaction day (Sep-2, 823.5k vs 204.6k). **52-wk high FRESH: intraday $576.61 on Sep-16 (0 sessions ago = top priority).** **RS vs SPY +6.31pp (5d)** (DELL +5.21% vs SPY −1.10% Sep-9→Sep-16). **XLK vs SPY 20d +0.90pp** (sector leading → no momentum penalty). Analysts Citi/BofA Buy **PT $600**, no downgrades. **Short interest ~5% float** (neutral). **Insider: aggressive scheduled 10b5-1 selling + Silver Lake Form 144 secondary, 0 buys/90d (−1 risk, not thesis-breaking).** Mgmt quote — CFO Kennedy: *"AI momentum is accelerating."* **Top risk: parabolic extension / chase risk — +266% 1yr, +12.4% above 21d EMA ($500.98), repeated −5–6% intraday reversals (Sep-10 −5.3%, Sep-14 −5.9%) even while grinding to fresh ATHs; run may whipsaw.** FOMC now PAST (Sep-16 hiked +25bp to 3.75–4.00%, first hike since 2023, signaled 1–2 more) — market took it well, Sep-17 futures +0.3%, 10-yr eased ~2bp; the pre-FOMC overhang that pressured high-multiple tech is behind us, though further-hike guidance keeps a multiple-compression backdrop. Regulatory: **shelf-reg CLEAN** (Sep-15 completed $5.0B = senior NOTES/DEBT to repay 4.9% First Lien Notes due 2026 + GCP, NOT equity; S-3ASR = routine WKSI debt auto-shelf, no offering announced; Dell is a net repurchaser); **BIS CLEAN** (server OEM not chipmaker; no material ≤30d rule/entity-list change gating China revenue). Next earnings ~Dec 1, 2026 (>3d ✓). Tradable/active NYSE, no halt (per /v2/assets: status=active, tradable=true). Sub-scores: signal 3 / momentum 2 / confirmation 2 / risk 1. Sized 19 sh × $565 = **$10,735 = 11.0%** of $97,328.01 equity (< 20% cap; post-fill cash ~89.0% >> 10% floor; 0→1/8 concurrent; weekly 0→1/5 BULL/NORMAL; IT 11.0% < 30% cap). **9th consecutive DELL plan** (Sep-3/8/9/10/11/14/15/16 all deferred at market_open on 6d/6e opening-range chase-guards — deferred NOT dropped; pre_market re-evaluates). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash). No open positions → no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | — |

## Notes

**Gates (all PASS → proceed):**
- **Clock:** is_open=false, next_open=2026-09-17T09:30 ET → **opens today, NOT a holiday** → proceed (pre_market runs pre-open; clock timestamp 08:10 ET).
- **Reconciliation 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT — zero divergence. Account ACTIVE, status=ACTIVE. **Equity $97,328.01** (=cash 100%, buying_power $389,312.04), 0/8 concurrent.
- **Universe FRESH:** screened 2026-09-13, **expires 2026-09-20**, 227 rows → freshness gate PASSES; no re-screen.

**Overlays / regime:**
- **⚠️ PEAD health STALE:** `pead_health.md` expires_on=2026-09-13 in the PAST (recurring weekly-refresh miss). Per step 1c: **treat posture NORMAL but flagged STALE → do NOT raise the bar** (universe-cache is the hard gate, passed). Last real reading (2026-09-06): NORMAL, realized_health_60d **+0.03%**, n=186 (drift essentially FLAT). → **standard 15% bars, max 5 new/week.**
- **SPY regime BULL:** fresh Alpaca IEX 200-day — SPY **$754.05** (Sep-16 close) > 200MA **$715.45** (+5.4%); bear rule NOT active → standard thresholds, max 5 new/week.
- **Macro-deferral NOT triggered:** Sep-17 premarket **S&P futures +0.3% (UP)** → "futures down >0.4%" leg **FAILS**; 10-yr eased ~2bp after the FOMC hike (still near multi-year highs) satisfies its leg only partially — both legs required → standard bars (no >20% override; **moot for DELL** whose +43.1% clears any bar). **FOMC Sep-16: first rate hike since 2023 (+25bp → 3.75–4.00%), signaled 1–2 more; market reacted positively, Sep-17 futures green.**

**Sanity-check vs strategy.md:** cash floor post-would-be-fill ~89.0% >> 10% ✓ | max concurrent 1/8 ≤ 8 ✓ | max new/week 1/5 ≤ 5 (BULL/NORMAL; 0 fills so far this week — Sep-14/15/16 all defers) ✓ | IT sector 11.0% ≤ 30% ✓. No trims needed.

**Candidates screened, DROPPED (0 others ≥6/10):**
- **MRVL (Marvell, active watchlist, IT/semiconductor) — DROP (no fresh catalyst + negative momentum):** last earnings Aug-26/27 sold-the-news/~0% EPS surprise = no fresh ≤30d qualifying beat; price $229.74 (Sep-16), **52-wk high $329.85 was 61 sessions ago (Jun-18) → downrank**; **5d RS −1.12pp vs SPY** (negative step-f). Current items = AI-Infra-Summit / GOOGL custom-silicon relationship (analyst/conference momentum, not a PEAD beat). Consistent with every prior session's MRVL drop.
- **CRM / ORCL / PANW / ZS / MDB / AVGO** — dropped in prior sessions and no fresh ≤30d qualifying catalyst overnight: CRM manufactured surprise (~+3% ex one-time gain); ORCL +10.3% sub-bar + negative reaction; PANW +4.1% sub-bar + LOWERED FY26 outlook; ZS ~+9% sub-bar AND not in cache/watchlist (cannot plan); MDB fell −12.5%; AVGO weak drift/vol.
- **Overnight sweep:** no compelling fresh in-universe PEAD earnings catalyst (Q2 season over). Sep-17 premarket movers AXTI/PLXS/BVN/ROG are analyst/technical/foreign-miss driven, not fresh in-universe earnings beats → nothing to shortlist or watchlist.

**Decision:** 1 candidate ≥6/10 → **plan 1 buy (DELL).** Planned sells: none (flat). Weekly slots 0→1/5. Regulatory flags among planned: **NONE** (DELL shelf-reg clean, BIS clean). Watchlist flags: **NONE** (all candidates in-univ or already active; no new compelling non-universe catalyst overnight).

**⚠️ Standing human flags:**
- Sizing: pre_market.md step 5 says "(currently 11%)" but strategy.md `Max position size at entry` field = **20%**. Sized DELL at ~11.0% (precedent-consistent, well within the 20% cap) — flagged for human to reconcile which value is authoritative.
- `memory/portfolio.md` bloat (~314KB, exceeds single-read limit) — recurring human-trim request.
- `pead_health.md` recurring weekly staleness — human should set `YF_DISABLE_CURL_CFFI=1` permanently in the routine env (per 2026-09-06 research_log fix).
