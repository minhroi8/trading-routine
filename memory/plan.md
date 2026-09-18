# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-09-18 (Friday). Drafted by `pre_market` ~08:1x ET.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| _(none)_ | — | — | — | — |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | — |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none — DELL +2.26% << +10% trigger)_ | 3837d86d | $531.70 | hold | — | DELL far from +10% partial-lock/trail trigger; hard −8% stop stays GTC |

## Notes

**0 plannable candidates ≥6/10 → NO new buys.** Book stays DELL-only (1/8, ~11.5% deployed, ~88.5% cash).

**Carried position:** DELL 19 @ $577.93 (opened 2026-09-17), −8% hard stop 3837d86d @ $531.70 GTC (working, confirmed via /v2/orders). Current ~$591 (+2.26% unrealized). Thesis intact (Q2 FY27 +43.1% EPS surprise, RAISED FY27 guide, AI-server backlog ~$95B, ~10-qtr beat streak). No exit criterion fired (not −8%, not +10%, not 60d, thesis not broken) → **no planned sell.** market_open/midday handle mechanical exits.

**Gates (all PASS):**
- Clock: is_open=false but next_open=2026-09-18T09:30 ET → opens today, NOT a holiday → proceed.
- **RECONCILIATION 1/1 PASS:** Alpaca /v2/positions = [DELL 19 @ $577.93 avg] MATCHES portfolio.md; sole open order = −8% hard stop 3837d86d (sell 19 @ $531.70 GTC, status=new), no orphans; zero divergence. Account ACTIVE, trading_blocked=false, account_blocked=false; equity $97,576.34, cash $86,347.34 (88.5%), buying_power $376,830.56, long_mv $11,229.
- **Universe FRESH** (screened 2026-09-13, expires 2026-09-20, 227 rows) → freshness gate PASSES; no re-screen.

**Overlays:**
- **⚠️ PEAD health STALE** — pead_health.md expires_on=2026-09-13 in the PAST (recurring weekly-refresh miss). Per step 1c: treat posture **NORMAL but flagged STALE → do NOT raise the bar** (universe-cache is the hard gate, passed). Last real reading (2026-09-06): NORMAL, realized_health_60d **+0.03%**, n=186 (drift essentially FLAT). → standard 15% bars, max 5 new/week.
- **Regime BULL** — fresh Alpaca IEX 200-day: SPY $762.64 (Sep-17 close) > 200MA **$715.84** (+6.54%); bear rule NOT active → standard sector thresholds, max 5 new/week.
- **Macro-deferral NOT triggered** — Sep-18 premarket S&P futures **+0.3% (UP)**, Nasdaq +0.6%, Dow/Russell +0.2% → "futures down >0.4%" leg FAILS; 10-yr near ~5% multi-month/year high (post-Sep-16 Fed hike, first hike in 3 yrs) satisfies its leg BUT both required → standard bars (no >20% override). Note: **monthly Triple-Witching options expiration today** → potential close-of-day volatility.

**Candidates considered → 0 plannable qualifiers:**
- **DELL** — already held (1/8); not a new-buy candidate (no add-on rule). Thesis intact; carried with hard stop.
- **MRVL (active watchlist, IT/semi) — DROPPED:** no fresh ≤30d earnings catalyst; last print (Aug-26/27) sold-the-news / ~0% surprise; **−25% over 3 months = broken momentum** (52-wk high ~Jun, >90d ago; negative/weak RS vs SPY, ~$221–230). Current items = GlobalFoundries SiGe-capacity manufacturing agreement + GOOGL custom-silicon relationship + AI Infra Summit (Sep-15–17) — analyst/conference/partnership momentum, NOT a fresh beat. Consistent with every prior session's MRVL drop.
- **FDX (in-universe, Industrials, large) — not a candidate:** FedEx FY27 Q1 reports ~this week (at/inside the 3-day earnings window = event risk) AND Industrials requires **>20% EPS surprise AND streak≥2** — no fresh qualifying catalyst (FedEx historically single-digit surprises). DQ.
- Sep-18 premarket top gainers = micro-cap/junk (TNMG, GIPR, IMCC, SSM, etc.) — none in S&P 1500 universe or watchlist.
- Q3 earnings season has NOT started (begins ~mid-Oct) → pre-Q3 lull; no fresh in-universe PEAD catalysts. ~11th consecutive session of ~0 in-universe qualifiers.

**Watchlist flag (compelling non-universe catalyst → pending_review, human-only):**
- **GNRC (Generac, Industrials/electrical, S&P 500) — ADDED to watchlist.md pending_review + Discord flag.** Sep-16 8-K: Amazon **Transaction Agreement + long-term supply agreement** — Amazon warrant for up to 1,693,745 sh @ $200.93 (307,954 vest immediately, rest vesting on cumulative payments for backup-power generators for AWS data centers, up to **$8B**); initial deliveries **$2.4B across 2027–2028**. Stock **+19% Sep-17** (opened +27.8%, +45% after-hours on the Sep-16 news); analyst PT raises. Verified via SEC EDGAR 8-K + Bloomberg/Benzinga. **NOT in the 227-row universe cache** (S&P 500 member → likely screen-source gap like PAYC/NET/OKTA/SNOW/ANF) AND **NOT previously watchlisted** → per pre_market step 2, added pending_review; **MUST NOT plan until human sets status: active.** ⚠️ Caveat for human: it's a **partnership/warrant catalyst** (EPS-threshold-exempt path) but GNRC is **Industrials** — strategy.md deprioritizes Industrials (2026 YTD backtest: 25% win rate, −4.82% avg return, worst sector); the warrant is also mildly dilutive. Human must weigh sector deprioritization + dilution before activating. (Mirrors the Apr-2026 Oracle→Bloom Energy warrant-stake precedent already reflected by BE on the watchlist.)

**Sanity checks vs strategy.md (moot — no buys):** cash floor 88.5% >> 10% ✓; max concurrent 1/8 ✓; weekly new 1/5 this week (DELL 2026-09-17; BULL/NORMAL cap 5) ✓; IT sector ~11.5% < 30% ✓. Regulatory flags among planned: NONE (no buys).

⚠️ **Sizing note (recurring, flagged for human):** pre_market.md step 5 says "(currently 11%)" but strategy.md `Max position size at entry` field reads **20%** — moot today (no buys); precedent has sized ~11%. Human to reconcile the parenthetical.

⚠️ **portfolio.md bloat ~319KB** (exceeds single-read limit) — recurring human-trim flag.

DRY_RUN: false.
