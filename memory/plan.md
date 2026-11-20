# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-20 (Fri) — pre_market ~07:17 ET. Book FLAT (0/8, 100% cash), equity $94,946.98.

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 20 | $930.00 | $855.60 | **Score 7/10 (Health Care, in-universe).** Q3 2026 (Oct-30 BMO) non-GAAP **EPS $20.07 vs ~$16.08–16.25 cons = +23.5% to +24.8% surprise** (+70% YoY) — clears the >20% ELEVATED_BAR + bear-regime bar. Revenue **$5.12B +36% YoY**, beat ~$4.60B (+11–12%). **Earnings streak 3+ consecutive beats** (+1 signal pt). Earnings-day gap **+6.29% overnight** (full-day +13.5%; 5–10% band → no adj). **Volume 5.69× 20d avg** on Oct-30 print (strong institutional confirmation). **52-wk high $988.48 on 2026-11-04 = 11 trading days ago (TOP priority <45d)**; Nov-19 close $923.60 = **−6.56% below ATH** (healthy pullback; only +2.08% above 21d EMA ~$904.82 — far less extended than prior sessions near $960). **RS +2.49pp 5d** (REGN −2.97% vs SPY −5.46% — outperforming on a risk-off week). **XLV 20d −2.12% vs SPY −6.31% = +4.18pp** (Health Care leading, rotation IN, tailwind). **~10 post-Q3 analyst PT raises / 0 downgrades** (Canaccord $1,175 / Guggenheim $1,100 / BofA $1,030 / Leerink $997 / Truist $982 / Cantor $980). **Short interest <2%** (neutral). **Insider neutral.** Mgmt call: *"an outstanding quarter … one of our strongest years ever."* **Top risk:** EYLEA biosimilar/Kodiak competition (EYLEA ~31% rev, priced; Q3 beat was Dupixent-driven) + **cemdisiran gMG FDA PDUFA target ~Nov-2026** (binary, may land inside the 42-day hold window — upside-biased: Phase 3 NIMBLE positive, published in The Lancet, priority review; secondary pipeline asset, a CRL would not break the core thesis). None thesis-breaking in 42d. **Shelf-reg: CLEAN** (routine 2024 WKSI auto-S-3, no 2026 offering, ~103M shares stable, active buybacks). **BIS: N/A** (Health Care). Asset active/tradable (NASDAQ); next earnings Q4 ~Jan-2027 (>3d). Sized 20sh @ $930 = $18,600 ≈ **19.6%** of equity (20% cap $18,989; 21sh = $19,530 = 20.6% > cap → 20sh). |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0 positions) — no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates PASS.** `/v2/clock` is_open=false (07:17 ET pre-market) but **next_open 2026-11-20T09:30 ET = TODAY → not a holiday → proceed.** **RECONCILIATION 0/0 PASS:** Alpaca `/v2/positions`=[] MATCHES portfolio.md FLAT (the VRT row is inside an HTML comment, closed −8% hard stop 2026-11-02); `/v2/orders?status=open`=[] (no orphan stops); account ACTIVE, trading_blocked=false, equity $94,946.98, 100% cash, buying_power $379,787.92.
- **Universe FRESH** — 330 rows, screened 2026-11-15, expires 2026-11-22 (today 2026-11-20 is before expiry). No re-screen (universe_refresh owns that).
- **PEAD posture: ELEVATED_BAR + FRESH** (computed 2026-11-15, expires 2026-11-22; **realized_health_60d_pct −0.358%, health_sample_n 163**, health_ok=FALSE). → **EPS-surprise bar raised to >20% for ALL sectors + max new positions capped at 2** for this session. Overlay governs NEW entries only (never exits).
- **⚠️ REGIME: BEAR.** Recomputed SPY 200-day MA on IEX daily bars (n=200): **SPY Nov-19 close $715.84 < 200MA $732.67 = −2.30%.** SPY fell −2.0% on Nov-19 and is now decisively below the 200MA (the Nov-18 bear flip at −0.30% deepened). **Bear regime → max new 2/week + >20% EPS all sectors** (strategy.md regime-gate) — coincides with ELEVATED_BAR; stricter-of new-position cap = **2**. Neither rule halts; high-conviction setups clearing the higher bar still trade. **Macro-deferral rule MOOT** (>20% already enforced by both overlays).
- **Weekly new-position slots: 0/2 used** (last fill VRT 2026-10-29, stopped −8% 2026-11-02; REGN planned-not-filled ~10 consecutive sessions). REGN would be 1/2 if it fills.
- **Post-fill compliance (if REGN fills ~19.6%):** cash ~80.4% (≥10% ✓), concurrent 1/8 (≤8 ✓), new-this-week 1/2 under ELEVATED_BAR+bear cap (≤2 ✓), Health Care 19.6% < 30% sector cap ✓.
- **⚠️ REGN execution caveat (for market_open):** REGN has been planned-but-unfilled ~10 consecutive sessions — market_open's chase-guard rejected it each time while extended near its 52-wk high. **Today's setup is cleaner: −6.56% off the ATH and only +2.08% above the 21d EMA** (vs ~−3% off high / more extended in prior runs). Limit $930 is just ~0.7% above the Nov-19 close $923.60 — below the ATH and below prior $950–965 attempts. On a BEAR tape (SPY < 200MA) apply opening-range / 21d-EMA / chase-guard discipline strictly; **do not chase above the $930 limit.**
- **DROPS / screened this session:**
  - **TGT** (in-universe, Consumer Staples) Q3 adj EPS $2.65 vs ~$2.07 exp ≈ +28% headline, BUT the beat is **tariff-refund-inflated** and the stock **slumped / holiday outlook missed** (negative reaction) → contaminated signal + negative PEAD reaction (same pattern as SN/HAS/ANF tariff-refund drops) → **DROP**.
  - **NVDA** (in-universe, IT) Q3 FY27 (Nov-17 AMC) rev $115.8B +103% beat-and-raise but EPS surprise **~+8% ≪ >20% bar**; guidance-driven, semi→BIS → DROP.
  - **PANW** (in-universe, IT) fiscal Q1 FY27 (Nov-18 AMC) adj EPS +8.2% surprise ≪ >20%; guide-raise + $4.5B all-stock Applied Compute acquisition (dilution) → DROP.
  - **TJX** (in-universe, Consumer Disc) Q3 beat + lifted FY26 but **soft Q4 guide**, single-digit EPS surprise ≪ >20% → DROP.
  - **LOW** (in-universe, Consumer Disc) beat but weak guidance, negative reaction → DROP.
  - **INTU** (in-universe, IT) Q1 FY27 (Nov-19 AMC) guided non-GAAP EPS $2.44–2.48 — software name, single-digit surprise at best, no verified >20% clean beat → DROP on threshold.
  - **ROST** (in-universe, Consumer Disc) off-price retail (TJX sibling), single-digit surprises historically, no verified >20% clean beat → DROP on threshold.
- **Watchlist:** every watchlist row is `status: pending_review` — **NONE are `active`**, so none are plannable this session (human-gated). MRVL thesis remains BROKEN (Nov-2 $115B all-stock Lumentum acquisition, −12.7% day, TD Cowen Buy→Hold). No new watchlist adds (this week's fresh beats — TGT/NVDA/PANW/TJX/LOW/INTU/ROST — are all already in-universe; no compelling clean non-universe catalyst; pending_review backlog ~28).
- **Regulatory flags:** none on the planned name (REGN shelf-reg CLEAN, BIS N/A).
- **Watchlist flags:** none.
- **Carry-forward (human):** portfolio.md ~483KB bloat (accumulated audit comments, exceeds single-read limit — recurring human-trim flag, needs human sign-off); trade_log VRT buy+sell rows carry commit_sha `<pending>` (human backfill); doc discrepancy pre_market.md/market_open.md "(currently 11%)" vs strategy.md `Max position size at entry` = 20% (strategy.md wins per CLAUDE.md; REGN sized to 20% field).
- **DRY_RUN: false.** (pre_market never trades regardless.)
