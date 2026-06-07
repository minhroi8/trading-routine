# PEAD 2026 YTD Out-of-Sample Backtest — Enhanced Strategy

*Generated: 2026-06-06 23:39*

*Test window: 2026-01-01 → 2026-06-04 (S&P 500 current constituents).*

---

## 1. 2026 YTD Verdict

**MIXED — profitable but did not clearly beat 2025.**

The enhanced stack produced 30 trades at 36.7% win rate and 0.16% average return — positive, but not a clear improvement over the 2025 baseline (55.5% / +1.54%). The extra filters mostly cut trade count rather than lifting per-trade quality over this window.

> **Sample-size caveat.** 2026 YTD spans only ~107 trading days and ~2 earnings seasons. The ≥15% surprise filter is intentionally strict, so the enhanced trade count is small and all 2026 conclusions are low-confidence relative to the multi-year baselines.

## 2. Comparison — 2022-2024 vs 2025 OOS vs 2026 YTD

| Metric | 2022-2024 (in-sample) | 2025 (OOS) | 2026 YTD (enhanced) |
|--------|----------------------:|-----------:|--------------------:|
| Total trades | 4387 | 1454 | 30 |
| Win rate | 54.8% | 55.5% | 36.7% |
| Avg return / trade | 1.32% | 1.54% | 0.16% |
| Avg winner | +7.74% | +7.84% | +10.26% |
| Avg loser | -6.45% | -6.31% | -5.69% |
| Profit factor | 1.45 | 1.55 | 1.04 |
| Max consec. losses | 41 | 13 | 5 |
| Avg holding days | 35.6 | 35.8 | 27.0 |
| SPY buy-and-hold | 28.2% | 18.0% | 11.1% |

*2026 holding days and SPY return are partial-period (5 months); the 42-day time stop has not fully cycled for spring entries.*

## 3. Filter Impact Analysis

BASE candidate set (EPS beat + price ≥ $10 + 20d avg $vol ≥ $20M): **697 trades**, win rate **37.9%**, avg **-1.24%**.

Each filter below is applied *independently* to the BASE set. "Removed" = BASE candidates that FAIL that filter; a well-designed filter should remove trades whose win rate is *below* the BASE win rate (i.e. it strips losers).

| Filter | Kept | Removed | Win% kept | Win% removed | Avg% removed | Verdict |
|--------|-----:|--------:|----------:|-------------:|-------------:|---------|
| EPS surprise ≥ 15% | 194 | 503 | 43.3% | 35.8% | -1.8% | ✓ strips losers |
| Volume ≥ 1.5× 20d avg | 472 | 225 | 36.0% | 41.8% | -0.49% | ✗ removed winners |
| Rel. strength vs SPY > 0 | 338 | 359 | 34.6% | 40.9% | -0.93% | ✗ removed winners |
| New 52-wk high ≤ 45d | 289 | 408 | 45.0% | 32.8% | -2.13% | ✓ strips losers |
| Not within 3d of next earnings | 697 | 0 | 37.9% | —% | —% | removed nothing |

**Scenario sensitivity (guidance-raise filter unverifiable in yfinance):**

| Scenario | Definition | Trades | Win% | Avg% | Profit factor |
|----------|------------|-------:|-----:|-----:|--------------:|
| A | EPS beat ≥ 15% only | 194 | 43.3% | 0.22% | 1.06 |
| B | EPS beat ≥ 15% + volume 1.5× | 125 | 39.2% | -0.81% | 0.82 |
| Full | All verifiable enhanced filters | 30 | 36.7% | 0.16% | 1.04 |

## 4. Trailing-Stop Analysis — 7% vs 12% for IT

IT/semiconductor trades in the enhanced set: **7**.

| Trailing stop | IT avg return | IT win rate |
|---------------|--------------:|------------:|
| 7% (old, all sectors) | 11.33% | 57.1% |
| 12% (new, IT only) | 9.76% | 42.9% |

The wider 12% IT trail gave back 1.57% per IT trade on average (letting IT winners run through normal volatility instead of being shaken out at 7%).

Aggregate effect across 7 IT trades: **-1,210** P&L vs the old 7% trail.

## 5. Full Trade Statistics (enhanced set)

| Metric | Value |
|--------|-------|
| Total trades | 30 |
| Win rate | 36.7% |
| Avg return per trade | 0.16% |
| Median return | -1.3% |
| Avg winner | +10.26% |
| Avg loser | -5.69% |
| Profit factor | 1.04 |
| Max consecutive losses | 5 |
| Avg holding period | 27.0 days |
| Total P&L (all positions) | $513 |
| Best trade | LITE +56.07% (27d) |
| Worst trade | FIX -12.53% (11d) |
| SPY buy-and-hold 2026 YTD | 11.1% |
| Approx. Sharpe ratio | -0.1 |

**Exit reason breakdown:**

- hard_stop: 9 (30.0%)
- time: 8 (26.7%)
- data_end: 7 (23.3%)
- trail_stop: 6 (20.0%)

*Note: `data_end` exits are trades still open at 2026-06-04 (time stop not yet reached) — their returns are marked-to-market, not realised.*

## 6. Regime Analysis (SPY vs 200-day MA)

**Bull regime (SPY > 200MA)** — 29 trades
- Win rate: 37.9%
- Avg return: 0.23%
- Profit factor: 1.06

**Bear regime (SPY < 200MA)** — 1 trades
- Win rate: 0.0%
- Avg return: -1.97%
- Profit factor: 0.0

*2025 finding was that the bear regime outperformed. 2026 YTD: bull avg 0.23% vs bear avg -1.97% — bull outperformed, NOT replicating the 2025 pattern.*

## 7. Sector Breakdown (enhanced set)

| Sector | Trades | Win Rate | Avg Return | Total P&L |
|--------|-------:|---------:|-----------:|----------:|
| Information Technology ⭐ | 7.0 | 42.9% | 9.76% | $7,516 |
| Utilities | 2.0 | 100.0% | 2.93% | $646 |
| Health Care | 3.0 | 66.7% | 1.47% | $487 |
| Real Estate | 1.0 | 100.0% | 2.7% | $298 |
| Consumer Staples | 3.0 | 33.3% | 0.67% | $223 |
| Energy | 2.0 | 0.0% | -5.21% | $-1,146 |
| Consumer Discretionary | 2.0 | 0.0% | -6.86% | $-1,510 |
| Financials | 2.0 | 0.0% | -7.96% | $-1,752 |
| Industrials | 8.0 | 25.0% | -4.82% | $-4,246 |

⭐ = Information Technology (subject to the wider 12% trailing stop).

## 8. Best & Worst Trades (enhanced set)

**Best 10**

| Ticker | Sector | Entry | Entry $ | Exit | Exit $ | Return % | Days | Reason |
|--------|--------|-------|--------:|------|-------:|---------:|-----:|--------|
| LITE | Information Technology | 2026-02-05 | $436.22 | 2026-03-04 | $680.8 | +56.07% | 27 | trail_stop |
| CASY | Consumer Staples | 2026-03-11 | $688.7521 | 2026-04-22 | $782.3672 | +13.59% | 42 | time |
| STX | Information Technology | 2026-04-30 | $655.18 | 2026-05-19 | $733.35 | +11.93% | 19 | trail_stop |
| GNRC | Industrials | 2026-05-01 | $260.02 | 2026-06-04 | $278.14 | +6.97% | 34 | data_end |
| TXN | Information Technology | 2026-04-24 | $286.3749 | 2026-06-04 | $305.37 | +6.63% | 41 | data_end |
| PNW | Utilities | 2026-02-27 | $98.7643 | 2026-04-10 | $102.6796 | +3.96% | 42 | time |
| VRT | Industrials | 2026-04-24 | $328.0 | 2026-05-18 | $339.73 | +3.58% | 24 | trail_stop |
| CVS | Health Care | 2026-05-08 | $88.0 | 2026-05-26 | $90.73 | +3.10% | 18 | trail_stop |
| IRM | Real Estate | 2026-05-04 | $126.82 | 2026-06-04 | $130.25 | +2.70% | 31 | data_end |
| PFE | Health Care | 2026-02-05 | $26.3255 | 2026-03-19 | $26.9649 | +2.43% | 42 | time |

**Worst 10**

| Ticker | Sector | Entry | Entry $ | Exit | Exit $ | Return % | Days | Reason |
|--------|--------|-------|--------:|------|-------:|---------:|-----:|--------|
| FIX | Industrials | 2026-02-23 | $1461.6676 | 2026-03-06 | $1278.5591 | -12.53% | 11 | hard_stop |
| BEN | Financials | 2026-02-03 | $26.6899 | 2026-03-12 | $23.4276 | -12.22% | 37 | hard_stop |
| ROK | Industrials | 2026-02-09 | $408.7751 | 2026-03-06 | $368.6927 | -9.81% | 25 | hard_stop |
| HAS | Consumer Discretionary | 2026-02-12 | $104.3106 | 2026-03-05 | $94.5953 | -9.31% | 21 | hard_stop |
| BKR | Energy | 2026-04-27 | $69.7667 | 2026-05-07 | $63.53 | -8.94% | 10 | hard_stop |
| HSY | Consumer Staples | 2026-02-09 | $228.9056 | 2026-03-19 | $208.9734 | -8.71% | 38 | hard_stop |
| GEV | Industrials | 2026-04-24 | $1161.02 | 2026-04-29 | $1063.11 | -8.43% | 5 | hard_stop |
| PWR | Industrials | 2026-05-04 | $749.6 | 2026-06-01 | $687.48 | -8.29% | 28 | hard_stop |
| EME | Industrials | 2026-05-01 | $899.9 | 2026-05-29 | $826.82 | -8.12% | 28 | hard_stop |
| TPR | Consumer Discretionary | 2026-02-09 | $150.6547 | 2026-03-23 | $144.0087 | -4.41% | 42 | time |

## 9. Key Findings — what changed vs 2025

- **Selectivity exploded, sample shrank.** The 2025 baseline used EPS-beat-only and produced 1,454 trades. The 2026 enhanced stack cut the 697 EPS-beat BASE candidates down to **30** — a far smaller, higher-conviction set.
- **The raw 2026 PEAD signal was negative.** EPS-beat-only (the 2025 methodology) returned 37.9% win / -1.24% avg on 697 trades in 2026 YTD — versus 55.5% / +1.54% in 2025. PEAD simply did not work in early 2026; this is a regime problem, not a filter problem.
- **The filters added value against that backdrop:** they lifted avg return from -1.24% (BASE) toward 0.16% (full stack) / Scenario A 0.22% — i.e. the enhancements did roughly what they were designed to do, but could not rescue a losing-signal regime.
- **Headline quality:** enhanced 2026 win rate 36.7% / avg 0.16% vs 2025's 55.5% / +1.54%.
- **Most valuable filter:** "New 52-wk high ≤ 45d" removed trades with the lowest win rate relative to BASE (≈5.1 pts below the BASE win rate), i.e. it stripped the most losers.
- **SPY 2026 YTD: 11.1%.** At 0.16% avg per trade (PF 1.04, ~27.0d holds) the enhanced strategy was roughly flat and badly lagged passive SPY this period.
- **Regulatory filters (BIS export-control, SEC shelf registration) were NOT applied** — they cannot be reconstructed from yfinance. Real-world deployment with those filters would remove additional names.
- **Guidance-raise filter NOT applied** (no reliable data); Scenarios A/B bracket its likely impact.

## 10. Recommendation

**MODIFY — filters cut count without clearly improving quality.**

Over 2026 YTD the enhanced stack did not beat the simpler 2025 baseline on per-trade return. Re-validate each filter on the full 2022-2025 history before committing; some filters may be removing winners.

---
### Limitations

1. **Survivorship bias** — current S&P 500 constituents only.
2. **Short window** — 2026-01-01→2026-06-04 is ~107 trading days; spring entries have not completed the 42-day time stop (`data_end` exits are marked-to-market).
3. **Relative strength** measured earnings-close → pre-entry close (no lookahead); the literal "5 days since earnings" rule would require day+5 data for a day+2 entry, which is forward-looking, so a non-lookahead proxy was used.
4. **Guidance raise, BIS export-control, SEC shelf-registration filters NOT applied** (not reconstructable from yfinance).
5. **No transaction costs / slippage; no portfolio-level capital constraint** (each trade simulated independently at 11% sizing).
6. **Earnings timestamps** from yfinance can be off by a day vs the true pre/post-market announcement.

*Backtest engine: yfinance + custom Python. Not financial advice.*