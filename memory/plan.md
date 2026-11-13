# Daily Plan

Handoff from `pre_market` → `market_open`. Rewritten fresh each pre-market. `market_close` archives the prior day's plan to `memory/archive/plan_<YYYY-MM-DD>.md`.

## Date

2026-11-13 (pre_market)

## Planned buys

| ticker | target_qty | limit_price | stop_price | thesis |
|--------|------------|-------------|------------|--------|
| REGN | 19 | $958.00 | $881.36 | **Regeneron (Health Care) — score 7/10.** Q3 2026 PEAD beat-and-raise (reported 2026-10-30): non-GAAP **EPS $20.07 vs ~$16.19 cons = +23.9% surprise** (clears the ELEVATED_BAR >20%-all-sectors bar), revenue **$5.12B +36% YoY** (~+12% beat), shares jumped **~+13%** on the print. **Earnings streak ≥3** (Q3 +23.9%, Q2 +40.6% [$14.29 vs ~$10.16], Q1 +3.9% → +1 signal pt). **Earnings-day gap +6.29%** open (full-day +13.5%; normal, no adj). **Volume 5.69× 20-day avg** (strong institutional confirmation). **52-wk high $988.48 on 2026-11-04 = 6 trading days ago** (top-priority recency; now consolidating −3.7% below high at $951.84, above 21-day EMA ~$879.78). **RS +2.24pp vs SPY (5-day)** (REGN +5.48% vs SPY +3.24% → outperforming). **Sector XLV +7.92pp vs SPY (20-day)** (Health Care rotating IN → no momentum penalty; +20d REGN +19.53%). Mgmt call (verbatim): *"modest refinements to our 2026 financial guidance as we enter the last quarter of the year"* — record Dupixent sales + EYLEA HD rebound + higher Sanofi collaboration income. **Analyst conviction: MIXED/weak** (no strong post-earnings upgrade wave; Citigroup Neutral pre-earnings on Kodiak competition, RBC ~$625 valuation) → confirmation leg tempered. **Top risk: EYLEA biosimilar/Kodiak competition** (EYLEA franchise ~31% of revenue, US sales −1% YoY, 2mg biosimilar launches + pricing pressure) — a known multi-quarter overhang, NOT a fresh thesis-breaking catalyst within 42d; Q3 beat came despite EYLEA softness (Dupixent-driven). Older overhangs (May-2026 melanoma Ph3 miss, Jul-2026 disclosure lawsuit) >42d, already priced. **Shelf-reg: CLEAN** (only routine Oct-2024 automatic S-3ASR; no 2026 offering/dilution — runs buybacks). **BIS: N/A** (Health Care). Next earnings ~late-Jan 2027 (>3-day window OK). Alpaca asset active/tradable. Short interest <2% (neutral), insider activity none-noted (neutral). Hard stop −8% @ $881.36. |

## Planned sells

| ticker | reason | notes |
|--------|--------|-------|
| _(none)_ | — | Book FLAT (0/8, 100% cash) since VRT −8% hard-stop exit 2026-11-02 — no positions, no exit criteria can fire. |

## Trailing stop conversions (market_open actions)

| ticker | current_stop_id | current_stop_price | action | target_new_stop | basis |
|--------|-----------------|-------------------|--------|-----------------|--------|
| _(none)_ | — | — | — | — | — |

## Notes

- **Gates (pre_market):** (1) Clock: `next_open` = 2026-11-13 = today → NOT a holiday, proceed (pre_market runs pre-open, is_open=false expected). (2) **Reconciliation 0/0 PASS** — Alpaca /v2/positions=[] MATCHES portfolio.md FLAT; /v2/orders?status=open=[] (no orphan stops); account ACTIVE, trading_blocked=false, equity $94,946.98, cash $94,946.98 (100%), buying_power $379,787.92. (3) **Universe cache FRESH** — screened 2026-11-08, expires 2026-11-15 (347 tickers); not stale.
- **PEAD health overlay (1c): ELEVATED_BAR + FRESH** (computed 2026-11-08, expires 2026-11-15; realized_health_60d_pct **−0.951%**, health_sample_n **260**, health_ok=false). → EPS bar raised to **>20% for ALL sectors**, **max new positions capped at 2** this session. Overlay governs NEW entries only; never halts, never affects exits.
- **Regime gate (strategy.md): BULL** — SPY last close $757.16 > 200-day MA $731.59 (computed from Alpaca IEX bars this run; consistent with pead_health spy_above_200ma=true). No bear-regime override; but ELEVATED_BAR independently enforces the same >20%/≤2 treatment (bull-and-weak case). Stricter new-position cap = **2**.
- **Weekly new-position slots:** 0 buys in the last 7 days (last trade = VRT exit 2026-11-02) → **0/2 ELEVATED_BAR slots used**; planning 1 (REGN) → 1/2 after.
- **Sizing basis:** strategy.md `Max position size at entry` = **20%** of equity (= $18,989; 19 sh × $958 = $18,202 ≈ 19.2%). ⚠ Doc discrepancy carry-forward: pre_market.md/market_open.md step-5 parenthetical "(currently 11%)" is STALE vs strategy.md's 20% field — strategy.md wins per CLAUDE.md, and the actual executed precedent (VRT 2026-10-29 77×$243.32 ≈ 19.4%) confirms 20% sizing. Flagged for human to reconcile the doc.
- **Plan sanity (step 6):** cash floor after buy ≈ 80.8% (≥10% ✓); max concurrent 1 (≤8 ✓); new-per-week 1 (≤2 ELEVATED_BAR cap ✓); Health Care sector 19.2% (≤30% ✓); EPS +23.9% (>20% ELEVATED_BAR bar ✓); not within 3d of earnings ✓; active/tradable ✓.
- **REGN execution caveat (for market_open):** REGN has been planned on 4 prior sessions (Nov 3/5/6/12) and NOT executed — market_open's opening-range/chase-guard/21-EMA gates rejected it as extended near its 52-wk high. It has since pulled back from the $988.48 (Nov-4) high to $951.84 (Nov-12, −3.7%), a cleaner/less-extended setup; limit $958 is set just above Nov-12 close and below the 52-wk high and the prior $965 attempts (do NOT chase above the limit). If the opening-range filter still rejects it, DO NOT force the entry.
- **Other screened names (dropped):** KEYS — the +23.8% adj-EPS beat was fiscal-Q3 reported **2026-08-18** (~87d, OUTSIDE the 30-day window; stock then FELL 5.4%) AND KEYS next reports Q4 FY26 on **2026-11-19** (6d out → earnings-window exclusion) → DROP. CSCO — fiscal-Q1 beat-and-raise (record $18.5B rev, EPS $1.40) but shares SLIPPED after-hours on gross-margin compression (memory costs) → negative/muted PEAD reaction, DROP. AMAT — beat + FY raise but only ~+3.6% EPS beat (far below >20% bar) → DROP. 
- **Watchlist / non-universe observed (NOT added):** CBRS (Cerebras) +17.77% AH on Q3 beat + Q4 guide raise ($310–330M) — compelling, but a recent-IPO (2025), highly-volatile AI-semiconductor name NOT in S&P 1500 and requiring a BIS export-control scan; logged in research_log as OBSERVED, NOT auto-added (sibling-restraint precedent — pending_review backlog already 25 names unactioned by human). Nebius −16.8% (capex guide above range) — not a candidate. No new pending_review rows added this session.
- **Watchlist active set:** only MRVL is `status: active` (no qualifying >20% fresh catalyst for MRVL this session; next MRVL earnings not imminent). All other 25 watchlist rows are `pending_review` (human-only to activate).
- **DRY_RUN: false** (pre_market never trades regardless — this is a handoff plan for market_open).
