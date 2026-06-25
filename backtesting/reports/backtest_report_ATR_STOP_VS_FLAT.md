# Backtest: ATR-Based Stop (V1) vs Flat −8% Stop (V0)

*Generated: 2026-06-25 22:59 — window 2022-01-01→2026-06-25, S&P 500 current constituents (survivorship-biased).*

Same candidate set, same entry rules, same trailing/time exits. Only the initial stop-loss and position size differ between the two variants.

- **V0 (baseline):** flat −8% stop; position = 11% of equity ($11k on $100k).
- **V1 (ATR stop):** stop = 2×14-day ATR, floored at 4%, capped at 8%; position sized to risk 0.9% of equity, hard-capped at 11% of equity.

Both variants scale out 1/3 at +10% and trail the remaining 2/3 by 7% below the peak; 42-calendar-day time stop.

## 1. Verdict

Across the full sample (277 trades), **V0 avg/trade = 1.5%** (PF 1.51) vs **V1 avg/trade = 1.23%** (PF 1.42). _Winner per-period detail below._

**Mechanical note that drives everything:** the V1 stop is `min(8%, max(4%, 2×ATR))`, so it is **always ≤ the flat 8% stop** — it can only ever be tighter, never wider. And the 0.9% risk-sizing target implies a notional of `$900 / stop_frac`, which is **≥ $11,250 even at the 8% cap** — so the 11% ($11k) notional cap binds on **100% of V1 trades** (verified: every single one). The 0.9% risk-target never actually applies. Net effect: V1 is, in practice, *the same ~$11k position as V0 but with an equal-or-tighter stop.* Tighter stops cut the size of each loss but fire more often (more noise stops).

## 2. Comparison Table — V0 vs V1 by period

| Period | Var | Trades | Win% | Avg% | Med% | AvgWin% | AvgLoss% | PF | MaxConsecL | AvgHold | Total P&L |
|--------|-----|-------:|-----:|-----:|-----:|--------:|---------:|---:|-----------:|--------:|----------:|
| 2022-2024 | V0 | 194 | 57.7% | 1.81% | 1.98% | 7.76% | -6.31% | 1.68 | 9 | 35.5d | $38,624 |
| 2022-2024 | V1 | 194 | 52.6% | 1.47% | 0.76% | 8.04% | -5.81% | 1.53 | 11 | 30.3d | $31,354 |
| 2025 | V0 | 53 | 49.1% | 1.23% | -0.2% | 9.03% | -6.29% | 1.38 | 5 | 34.0d | $7,159 |
| 2025 | V1 | 53 | 47.2% | 1.27% | -0.24% | 9.11% | -5.73% | 1.42 | 5 | 31.3d | $7,406 |
| 2026 YTD | V0 | 30 | 50.0% | -0.07% | -0.61% | 8.1% | -8.24% | 0.98 | 5 | 28.7d | $-228 |
| 2026 YTD | V1 | 30 | 43.3% | -0.38% | -4.97% | 8.81% | -7.4% | 0.91 | 5 | 24.6d | $-1,238 |

_Position size is ~$11k for both variants (the 11% cap binds for V1), so the P&L and profit-factor deltas come purely from the different stop paths._

## 3. Noise-Stop Analysis (stops inside first 5 trading days)

| Period | Var | #Stops | #Stops in first 5d | Noise-stop rate | First-5d stops as % of all trades |
|--------|-----|-------:|-------------------:|----------------:|----------------------------------:|
| 2022-2024 | V0 | 47 | 8 | 17.0% | 4.1% |
| 2022-2024 | V1 | 78 | 22 | 28.2% | 11.3% |
| 2025 | V0 | 16 | 4 | 25.0% | 7.5% |
| 2025 | V1 | 19 | 5 | 26.3% | 9.4% |
| 2026 YTD | V0 | 12 | 2 | 16.7% | 6.7% |
| 2026 YTD | V1 | 16 | 4 | 25.0% | 13.3% |

**Did V1 reduce first-5-day stop-outs?** Full sample: V0 had 14 first-5-day stops (5.1% of all trades); V1 had 31 (11.2%). Because the ATR stop is never wider than the flat 8% stop, V1 did NOT reduce early stop-outs — it produced at least as many.

## 4. ATR Stop-Width Distribution (V1) — validates the 4–8% collar

| Effective stop bucket | Trades | Share |
|-----------------------|-------:|------:|
| 4% (floor) | 42 | 15.2% |
| 4–5% | 69 | 24.9% |
| 5–6% | 64 | 23.1% |
| 6–7% | 38 | 13.7% |
| 7–8% | 23 | 8.3% |
| 8% (cap) | 41 | 14.8% |

Mean effective V1 stop: **5.67%** (vs flat 8% for V0). 15.2% of trades hit the 4% floor, 14.8% hit the 8% cap. Mean entry-day ATR: 3.0% of price.

## 5. MU-Style Analysis — high-ATR semiconductor / IT names

Filter: IT-sector names with daily ATR > 3.0% of price. Matched **29** trades.

- Mean ATR of these names: 4.76%/day → mean V1 stop 7.72% (vs flat 8%).
- V0 first-5-day noise stops: **3**.
- V1 first-5-day noise stops: **4**.
- V0 noise stops *avoided* under V1: **0**.
- *New* noise stops V1 introduced (V0 survived, V1 stopped early): **1**.
- V0 avg return on these names: 6.1%; V1 avg: 5.71%.

Because 2×ATR for these names is **at or above the 8% cap only when daily ATR ≥ 4%** — and is *tighter* than 8% whenever daily ATR is 2–4% — the ATR rule as specified gives high-vol names an **equal-or-tighter** stop than the flat 8%. It therefore cannot rescue the MU-style noise stop the proposal was designed to avoid: to widen the stop on a volatile name you would need to *raise or remove the 8% cap*, not add an ATR term beneath it.

## 6. Recommendation

V1 beat V0 on average return in **1 of 3** periods. 
**Keep V0.** V1's tighter-only stops increase early stop-outs without a compensating return edge, and the 8% cap means it never delivers the wider stop the proposal intended for volatile names. If the goal is genuinely to avoid noise stops on high-ATR names, the fix is to **raise/remove the 8% cap** (let the ATR term widen the stop), not to add an ATR floor beneath an unchanged cap.

---
**Methodology / data provenance.** The *entry set* (every trade that passed the full entry stack — EPS surprise ≥15%, announcement volume ≥1.5×, relative strength >0 vs SPY, new 52-wk high ≤45d, price ≥$10, 20-day $-vol ≥$20M, entry day+2 at open) is read from this repo's existing validated candidate files (`backtest_trades_PEAD_2022_2025_ENHANCED_base.csv` + `backtest_trades_PEAD_2026_YTD.csv`), so both variants run on an identical, already-validated candidate set. Daily auto-adjusted OHLC paths were re-fetched from Yahoo's chart API and cached under `backtesting/data_cache/`; ATR, entry fills, stops and the 1/3 scale-out are all simulated on that fresh series. Survivorship bias (current S&P 500 constituents) and zero transaction costs apply, as in all prior reports in this repo. Relative-strength was measured earnings-close→entry-eve (no lookahead at the day+2 open).*