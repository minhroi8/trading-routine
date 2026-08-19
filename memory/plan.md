# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-08-19 (pre_market ~08:2x ET). DRY_RUN: false.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| LLY | 16 | $1,275.00 | fill × 0.92 (≈ $1,127.67 off $1,225.73 ref) | **Eli Lilly — Health Care — score 9/10.** Q2 2026 (reported Aug 5 AM): adj EPS **$8.38 vs ~$6.58 = +27.3% surprise** (vs $6.07 = +38%; report absorbed $3.03 of acquired-IPR&D so underlying beat even larger); revenue **$22.97B, +48% YoY**, beat ~$20.9B by **+9.8%**; Mounjaro+Zepbound $14.9B combined (Mounjaro +91% to $9.94B). **RAISED FY26 guide 2nd straight quarter** to $85–87B rev / $35.50–36.50 adj EPS. Streak: multi-quarter beat-and-raise (3+). Earnings-day gap **+5.2%**, full day **+4.9%**, volume **2.63×** 20-day avg. 52-wk high $1,249.45 **30 trading days ago** (top-priority recency), last −1.9% from high. RS **+1.28% vs SPY** (5-day, +0.88% vs −0.40%). Sector XLV **+5.92% vs SPY +2.56%** (20-day) — Health Care leading. Analyst conviction: Wells Fargo PT→$1,000 (OW), Cantor→$630, CNBC IC raised; avg PT ~$1,270. Short interest low (<2%, neutral). Insider: none flagged. Verbatim (CEO David Ricks): Mounjaro global adoption was *"an upside beat in a pretty big way [of] our own expectations, but also the Street's"*; oral market is *"expansionary, it's not cannibalizing Zepbound."* US obesity Rx +78% YoY. Top risk: pharma-tariff overhang (~25% floated, temporary reprieve) + orforglipron US FDA timing (binary, but core is tirzepatide franchise — not thesis-breaking in 42d). Regulatory scan: **shelf-reg CLEAN** (only a boilerplate universal S-3ASR; NO equity offering / dilution — LLY is a net buyback name); **BIS N/A** (pharma). Earnings re-verify: next report late Oct — outside 3-day window ✓. Halt/status: active/tradable NYSE ✓. |
| PWR | 25 | $725.00 | fill × 0.92 (≈ $640.46 off $696.15 ref) | **Quanta Services — Industrials — score 9/10.** Carryover: scored 9/10 in pre_market 2026-08-18, deferred by market_open on the intraday opening-range confirmation gate (Gate 6e) — NOT fundamentally disqualified; re-verified fresh today with drift resuming. Q2 2026 (reported Jul 30): adj diluted EPS **$4.24 vs $3.29 = +28.9% surprise** (clears strict Industrials **>20% AND streak≥2** gate — **3 consecutive beats**); revenue **$9.6B, +41% YoY / +12.1% beat**; adj EBITDA $1.1B; **record backlog $53.4B**; **RAISED FY26 adj EPS guide ~+20%**; four acquisitions closed in-quarter. Earnings-day gap **+15.3%**, full day **+17.3%**, volume **2.91×** 20-day avg. 52-wk high $788.75 **71 trading days ago** (normal recency), last −11.7% from high. RS **+4.21% vs SPY** (5-day, +3.81% vs −0.40%) — drift re-accelerating. Sector XLI **+2.75% vs SPY +2.56%** (20-day, roughly in line). Analyst conviction: **4 PT raises post-print** — Citi $871 (Buy), Jefferies $833 (Buy), TD Cowen $785 (Buy), Mizuho $741 (Neutral). Short interest low (<2%, neutral). Insider: none flagged. Verbatim (CEO Duke Austin): results *"meaningfully exceeded expectations"* on *"broad-based organic strength"*; company is *"still in the early stages"* of a decade-long infrastructure buildout. Top risk: cyclical Industrials + integration risk from 4 acquisitions (data-center/grid/electrification tailwind intact). Regulatory scan: **shelf-reg CLEAN** (Aug 3 424B5 was a **$500M DEBT** offering — investment-grade, NOT equity/dilutive); **BIS N/A** (not semiconductor). Earnings re-verify: next report ~late Oct — outside 3-day window ✓. Halt/status: active/tradable NYSE ✓. **Sizing trimmed to 25 sh ($17,404 = 17.73%) — see Notes (30% Industrials sector cap with EME).** |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | EME (13 @ $834.12, −1.15%) thesis intact — no exit criterion fired (not −8% hard stop; no guidance cut/miss/fraud; held 14d, not 60d-stale). Hard stop 96e4e855 $767.39 active. HOLD. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|-------|
| _(none)_ | — | — | — | — | EME −1.15%, far below +10% partial-profit-lock trigger — no conversion. |

## Notes

- **PEAD signal-health posture: NORMAL** (realized_health_60d_pct 0.906%, health_sample_n 113; pead_health.md computed 2026-08-16, expires 2026-08-23 — fresh). Standard `strategy.md` thresholds apply; no raised bar / no ≤2 cap from the overlay.
- **Regime gate: BULL** (SPY close 776.34 > 200MA 702.75 per pead_health.md). Normal operation — standard thresholds, max 5 new/week.
- **Macro deferral rule: NOT triggered.** 10-yr Treasury 4.70% (easing from the week's highs, NOT a fresh multi-month high today); S&P 500 futures flat-to-+0.6%. Standard 15% EPS bar (20% for Utilities/Real Estate/Industrials/Energy).
- **Sizing: 20% of equity** ($98,142.30 equity → 20% = $19,628) per `strategy.md` "Max position size at entry" (supersedes the routine's stale "11%" annotation). LLY: 16 sh × $1,225.73 = $19,612 = **19.98%** ✓. PWR: 25 sh × $696.15 = $17,404 = **17.73%** (trimmed).
- **PWR sector-cap trim:** full 20% would push Industrials to ~30.8% (EME 10.92% + PWR 19.86%), over the 30% cap. Trimmed PWR to **25 sh (17.73%)** → Industrials total **28.65%** < 30% ✓ (cushion for intraday marks). `market_open` should re-verify the sector cap at fill and trim further if EME/PWR have risen.
- **Sanity check vs strategy.md:** cash floor — after both buys ~51% cash ≫ 10% ✓; max concurrent — EME+LLY+PWR = 3/8 ✓; new-per-week — 0 placed this week (Aug 18 PWR was *deferred*, no fill) + 2 = **2/5** ✓; sector caps — Health Care 19.98%, Industrials 28.65%, both < 30% ✓; position size ≤ 20% ✓; EPS thresholds — LLY (HC) +27.3% > 15% ✓, PWR (Industrials) +28.9% > 20% AND streak 3 ≥ 2 ✓.
- **Candidates researched & dropped:** PLTR (score ~6, DROP — momentum leg broken: 52-wk high 197 td ago, −17.3% below it, **negative 5-day RS −1.54% vs SPY**; analyst skepticism, Jefferies Underperform PT $80; extreme valuation ~50× sales / ~149× P/E; heavy insider selling — drift stalled/faded, low-conviction new entry). KEYS (DROP — **fell −5.6% on the print** despite +23.8% EPS beat: negative/failed PEAD reaction, gap −3.1%). SMCI (DROP — revenue MISS, muted +0.4% reaction despite big margin beat, −40% below a high 263 td ago, governance/accounting history). ABNB (DROP — EPS +9.5% surprise FAILS 15% bar; pop faded). NTAP (DROP — reporting imminently ~Aug 20, inside 3-day earnings window / event risk). MRVL (watchlist active; no fresh 30-day catalyst — reports Aug 27, entering right before earnings — SKIP).
- DRY_RUN: false.
