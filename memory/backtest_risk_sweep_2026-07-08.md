# Parameter-Sweep Backtest — Entry-Quality Filters × Stop Width

*Generated: 2026-07-08 20:43 — window 2022-01-01→2025-12-31 (grid) + 2026 YTD cross-check; S&P 500 current constituents (survivorship-biased).*

**Research / diagnostic only — no `strategy.md` edit, no orders.** Same status as the stop audit (`memory/stop_audit_2026-07-07.md`), the S3 ATR-stop backtest (`backtest_report_ATR_STOP_WIDENED_V2.md`) and the chronic-exit backtest.

## 0. What this sweeps, and the honesty caveats up front

| Dimension | Values (current in **bold**) |
|-----------|------------------------------|
| EPS surprise threshold | **≥15%** · ≥12.5% · ≥10% |
| Score cutoff (proxy) | **≥6** · ≥5 · ≥4 |
| Stop width | **flat −8%** · flat −10% · flat −12% · max(8%, 1.5×ATR14) · max(8%, 2.0×ATR14) |

3 × 3 × 5 = **45 combinations**, each reported **separately for IS and OOS**.

- **IS / OOS split** (identical to the S3 and regime-gate audits): **IS = 2022–2024**, **OOS = 2025**. A combination that wins IS but loses OOS is a **rejected** combination and is labelled so — IS and OOS are never averaged into one number.
- **Baseline** = EPS ≥15% / score ≥6 / flat −8%. This reproduces the current live strategy and S3's V0 entry set exactly (**194 IS + 53 OOS** trades).
- **Score-cutoff is a PROXY, not the live 1–10 score.** The live pre-market score weights guidance-raise magnitude, analyst-upgrade counts, earnings-call tone, insider activity, sector-ETF momentum, short interest and regulatory (shelf/BIS) checks — **none reconstructible from price+earnings data** (same class of unbacktestable inputs the 2026-YTD and ENHANCED reports flagged). We proxy it as the count `q` of the three verifiable quality filters {volume ≥1.5×, relative-strength >0, new 52-wk high ≤45d}: **≥6 → q==3** (= current enhanced set), **≥5 → q≥2**, **≥4 → q≥1**. Read the score rows as *“how many verifiable quality signals must align”*, not as the literal live score. EPS-surprise magnitude is handled by the EPS dimension and is deliberately not double-counted in `q`.
- **Stop mechanics** are identical to S3: both fixed and ATR variants scale out 1/3 at +10% and trail the remaining 2/3 by 7%; 42-day time stop. **ATR variants use S3's risk-based sizing** (risk 0.8% of equity = $800/stop%, capped at 11%); **fixed variants use the current flat 11% ($11k) sizing.** Per-trade return %/win %/Sharpe are sizing-independent; profit factor, total P&L and max-drawdown use each variant's own sizing, so ATR's smaller average notional mechanically dampens both its P&L and its drawdown (flagged again where it matters).
- **Coverage:** 5835 of the committed 2022–2025 base candidates were re-simulated from re-fetched OHLC (4367 IS / 1468 OOS); 30 of the 30 committed 2026 enhanced trades.
- **Sharpe** = mean(per-trade return) / std(per-trade return) (rf≈0 at the trade horizon); a per-trade risk-adjusted ratio, **not** annualised, and deliberately **not** ×√n (so it does not reward a combo merely for admitting more trades). **Max drawdown** = deepest peak-to-trough of a sequential equity curve that reinvests each trade at its own position fraction (entry-date order; compounded so it stays bounded in 0–100%). It models **no** concurrency / capital constraint — the live book runs up to 8 positions at once — so it is a directional stress read (looser ⇒ deeper), not the live portfolio drawdown. High-trade-count loosened cells sequence hundreds of bets through one account, which inflates the figure; weight it accordingly.

## 1. Headline

- **Baseline (EPS≥15 / score≥6 / flat −8%)** — IS: 194 trades, 57.7% win, 1.81% avg, PF 1.678, Sharpe 0.21, MaxDD -15.78%. OOS: 53 trades, 49.1% win, 1.228% avg, PF 1.383, Sharpe 0.111, MaxDD -5.71%.
- **SPY buy-and-hold:** IS 28.2% · OOS 18.0% · 2026 YTD 10.0% (index total return; not directly comparable to a per-trade avg% on ~11% sizing — shown for the beat-the-benchmark bar).

## 2a. Full grid — OOS (2025)

Δavg = avg-return minus the same-period baseline (flat −8% / EPS≥15 / score≥6). `n` is the raw trade count (denominator for every rate in the row).

| EPS | Score | Stop | n | Win% | Avg% | Med% | PF | Sharpe | MaxDD% | MaxConsecL | AvgHold | TotP&L | Δavg vs base |
|----:|:-----:|------|--:|-----:|-----:|-----:|---:|-------:|------:|-----------:|--------:|-------:|-------------:|
| ≥15% | >=6 | flat -8% | 53 | 49.1 | 1.228 | -0.2 | 1.383 | 0.111 | -5.71 | 5 | 34.0 | $7,159 | baseline |
| ≥15% | >=6 | flat -10% | 53 | 49.1 | 0.708 | -0.2 | 1.19 | 0.06 | -7.71 | 5 | 36.0 | $4,127 | -0.52 |
| ≥15% | >=6 | flat -12% | 53 | 49.1 | 0.376 | -0.2 | 1.093 | 0.031 | -8.88 | 5 | 36.7 | $2,192 | -0.85 |
| ≥15% | >=6 | max(8%, 1.5xATR14) | 53 | 49.1 | 1.142 | -0.2 | 1.351 | 0.103 | -5.33 | 5 | 34.1 | $5,986 | -0.09 |
| ≥15% | >=6 | max(8%, 2.0xATR14) | 53 | 49.1 | 1.313 | -0.2 | 1.355 | 0.12 | -4.55 | 5 | 34.8 | $5,502 | +0.08 |
| ≥15% | >=5 | flat -8% | 190 | 53.7 | 0.626 | 0.907 | 1.182 | 0.067 | -25.19 | 8 | 32.2 | $13,078 | -0.60 |
| ≥15% | >=5 | flat -10% | 190 | 54.2 | 0.383 | 0.954 | 1.1 | 0.038 | -29.83 | 8 | 34.1 | $8,015 | -0.84 |
| ≥15% | >=5 | flat -12% | 190 | 55.8 | 0.484 | 1.404 | 1.127 | 0.047 | -30.66 | 8 | 35.3 | $10,117 | -0.74 |
| ≥15% | >=5 | max(8%, 1.5xATR14) | 190 | 53.7 | 0.518 | 0.907 | 1.172 | 0.055 | -23.06 | 8 | 32.2 | $11,158 | -0.71 |
| ≥15% | >=5 | max(8%, 2.0xATR14) | 190 | 54.2 | 0.672 | 0.954 | 1.204 | 0.069 | -21.76 | 8 | 33.0 | $12,445 | -0.56 |
| ≥15% | >=4 | flat -8% | 341 | 56.0 | 1.629 | 2.341 | 1.526 | 0.159 | -31.19 | 14 | 33.3 | $61,107 | +0.40 |
| ≥15% | >=4 | flat -10% | 341 | 57.5 | 1.635 | 2.462 | 1.501 | 0.152 | -36.4 | 14 | 35.4 | $61,347 | +0.41 |
| ≥15% | >=4 | flat -12% | 341 | 58.7 | 1.789 | 2.639 | 1.566 | 0.165 | -37.9 | 14 | 36.6 | $67,109 | +0.56 |
| ≥15% | >=4 | max(8%, 1.5xATR14) | 341 | 56.3 | 1.599 | 2.392 | 1.506 | 0.155 | -28.63 | 14 | 33.4 | $52,771 | +0.37 |
| ≥15% | >=4 | max(8%, 2.0xATR14) | 341 | 57.5 | 1.844 | 2.462 | 1.569 | 0.176 | -27.34 | 14 | 34.4 | $54,451 | +0.62 |
| ≥12.5% | >=6 | flat -8% | 61 | 45.9 | 0.49 | -0.354 | 1.14 | 0.046 | -8.94 | 6 | 33.4 | $3,289 | -0.74 |
| ≥12.5% | >=6 | flat -10% | 61 | 45.9 | -0.093 | -0.354 | 0.977 | -0.008 | -11.53 | 6 | 35.4 | $-621 | -1.32 |
| ≥12.5% | >=6 | flat -12% | 61 | 45.9 | -0.426 | -0.354 | 0.904 | -0.036 | -12.65 | 6 | 36.0 | $-2,857 | -1.65 |
| ≥12.5% | >=6 | max(8%, 1.5xATR14) | 61 | 45.9 | 0.416 | -0.354 | 1.125 | 0.039 | -8.09 | 6 | 33.5 | $2,668 | -0.81 |
| ≥12.5% | >=6 | max(8%, 2.0xATR14) | 61 | 45.9 | 0.547 | -0.354 | 1.122 | 0.051 | -7.16 | 6 | 34.2 | $2,377 | -0.68 |
| ≥12.5% | >=5 | flat -8% | 222 | 52.3 | 0.391 | 0.841 | 1.111 | 0.043 | -29.85 | 12 | 31.8 | $9,554 | -0.84 |
| ≥12.5% | >=5 | flat -10% | 222 | 52.7 | 0.062 | 0.89 | 1.016 | 0.006 | -35.27 | 12 | 33.7 | $1,514 | -1.17 |
| ≥12.5% | >=5 | flat -12% | 222 | 54.1 | 0.093 | 0.954 | 1.023 | 0.009 | -36.58 | 12 | 34.9 | $2,271 | -1.14 |
| ≥12.5% | >=5 | max(8%, 1.5xATR14) | 222 | 52.3 | 0.299 | 0.841 | 1.106 | 0.032 | -27.28 | 12 | 31.9 | $8,176 | -0.93 |
| ≥12.5% | >=5 | max(8%, 2.0xATR14) | 222 | 52.7 | 0.396 | 0.89 | 1.131 | 0.041 | -25.69 | 12 | 32.5 | $9,542 | -0.83 |
| ≥12.5% | >=4 | flat -8% | 413 | 56.2 | 1.553 | 2.392 | 1.496 | 0.155 | -36.92 | 19 | 32.9 | $70,546 | +0.32 |
| ≥12.5% | >=4 | flat -10% | 413 | 57.4 | 1.462 | 2.492 | 1.435 | 0.139 | -42.81 | 19 | 34.9 | $66,418 | +0.23 |
| ≥12.5% | >=4 | flat -12% | 413 | 58.6 | 1.581 | 2.78 | 1.48 | 0.149 | -44.94 | 19 | 36.2 | $71,822 | +0.35 |
| ≥12.5% | >=4 | max(8%, 1.5xATR14) | 413 | 56.4 | 1.528 | 2.408 | 1.48 | 0.152 | -33.78 | 19 | 33.1 | $61,187 | +0.30 |
| ≥12.5% | >=4 | max(8%, 2.0xATR14) | 413 | 57.4 | 1.696 | 2.492 | 1.529 | 0.166 | -31.98 | 19 | 33.9 | $62,360 | +0.47 |
| ≥10% | >=6 | flat -8% | 80 | 50.0 | 0.927 | -0.095 | 1.276 | 0.089 | -11.47 | 7 | 33.1 | $8,160 | -0.30 |
| ≥10% | >=6 | flat -10% | 80 | 50.0 | 0.363 | -0.095 | 1.093 | 0.033 | -14.59 | 7 | 35.0 | $3,198 | -0.86 |
| ≥10% | >=6 | flat -12% | 80 | 51.2 | 0.395 | 0.179 | 1.102 | 0.035 | -15.28 | 7 | 36.4 | $3,479 | -0.83 |
| ≥10% | >=6 | max(8%, 1.5xATR14) | 80 | 50.0 | 0.87 | -0.095 | 1.266 | 0.083 | -10.41 | 7 | 33.2 | $7,091 | -0.36 |
| ≥10% | >=6 | max(8%, 2.0xATR14) | 80 | 50.0 | 0.963 | -0.095 | 1.275 | 0.093 | -9.5 | 7 | 33.7 | $6,857 | -0.26 |
| ≥10% | >=5 | flat -8% | 275 | 53.8 | 0.593 | 0.997 | 1.18 | 0.067 | -31.97 | 12 | 32.4 | $17,935 | -0.64 |
| ≥10% | >=5 | flat -10% | 275 | 54.2 | 0.279 | 1.226 | 1.075 | 0.029 | -37.67 | 12 | 34.1 | $8,433 | -0.95 |
| ≥10% | >=5 | flat -12% | 275 | 55.6 | 0.345 | 1.582 | 1.093 | 0.035 | -38.8 | 12 | 35.3 | $10,422 | -0.88 |
| ≥10% | >=5 | max(8%, 1.5xATR14) | 275 | 53.8 | 0.518 | 0.997 | 1.175 | 0.058 | -29.28 | 12 | 32.4 | $15,761 | -0.71 |
| ≥10% | >=5 | max(8%, 2.0xATR14) | 275 | 54.2 | 0.591 | 1.226 | 1.204 | 0.064 | -27.62 | 12 | 33.0 | $17,418 | -0.64 |
| ≥10% | >=4 | flat -8% | 502 | 57.0 | 1.578 | 2.4 | 1.53 | 0.164 | -39.08 | 22 | 33.4 | $87,133 | +0.35 |
| ≥10% | >=4 | flat -10% | 502 | 58.0 | 1.458 | 2.518 | 1.454 | 0.144 | -45.69 | 22 | 35.2 | $80,494 | +0.23 |
| ≥10% | >=4 | flat -12% | 502 | 59.2 | 1.577 | 2.717 | 1.503 | 0.155 | -47.72 | 22 | 36.5 | $87,105 | +0.35 |
| ≥10% | >=4 | max(8%, 1.5xATR14) | 502 | 57.2 | 1.551 | 2.417 | 1.516 | 0.161 | -35.91 | 22 | 33.6 | $76,051 | +0.32 |
| ≥10% | >=4 | max(8%, 2.0xATR14) | 502 | 58.0 | 1.685 | 2.518 | 1.564 | 0.172 | -33.94 | 22 | 34.2 | $77,206 | +0.46 |

## 2b. Full grid — IS (2022-2024)

Δavg = avg-return minus the same-period baseline (flat −8% / EPS≥15 / score≥6). `n` is the raw trade count (denominator for every rate in the row).

| EPS | Score | Stop | n | Win% | Avg% | Med% | PF | Sharpe | MaxDD% | MaxConsecL | AvgHold | TotP&L | Δavg vs base |
|----:|:-----:|------|--:|-----:|-----:|-----:|---:|-------:|------:|-----------:|--------:|-------:|-------------:|
| ≥15% | >=6 | flat -8% | 194 | 57.7 | 1.81 | 1.984 | 1.678 | 0.21 | -15.78 | 9 | 35.5 | $38,624 | baseline |
| ≥15% | >=6 | flat -10% | 194 | 59.3 | 1.812 | 1.992 | 1.649 | 0.2 | -17.57 | 9 | 37.2 | $38,658 | +0.00 |
| ≥15% | >=6 | flat -12% | 194 | 59.3 | 1.803 | 1.992 | 1.643 | 0.197 | -17.09 | 9 | 38.5 | $38,467 | -0.01 |
| ≥15% | >=6 | max(8%, 1.5xATR14) | 194 | 57.7 | 1.79 | 1.984 | 1.672 | 0.207 | -14.32 | 9 | 35.5 | $34,707 | -0.02 |
| ≥15% | >=6 | max(8%, 2.0xATR14) | 194 | 58.2 | 1.899 | 1.992 | 1.718 | 0.215 | -14.09 | 9 | 35.9 | $36,047 | +0.09 |
| ≥15% | >=5 | flat -8% | 626 | 56.7 | 1.437 | 2.027 | 1.473 | 0.162 | -36.01 | 13 | 34.1 | $98,955 | -0.37 |
| ≥15% | >=5 | flat -10% | 626 | 58.5 | 1.564 | 2.273 | 1.52 | 0.172 | -35.2 | 10 | 36.7 | $107,699 | -0.25 |
| ≥15% | >=5 | flat -12% | 626 | 59.9 | 1.765 | 2.564 | 1.609 | 0.193 | -30.28 | 8 | 38.3 | $121,518 | -0.05 |
| ≥15% | >=5 | max(8%, 1.5xATR14) | 626 | 56.7 | 1.402 | 2.027 | 1.467 | 0.157 | -33.41 | 13 | 34.2 | $88,281 | -0.41 |
| ≥15% | >=5 | max(8%, 2.0xATR14) | 626 | 57.0 | 1.45 | 2.106 | 1.496 | 0.161 | -30.87 | 13 | 34.6 | $90,067 | -0.36 |
| ≥15% | >=4 | flat -8% | 1029 | 54.7 | 1.25 | 1.648 | 1.394 | 0.139 | -54.3 | 19 | 33.6 | $141,469 | -0.56 |
| ≥15% | >=4 | flat -10% | 1029 | 56.5 | 1.329 | 1.98 | 1.414 | 0.142 | -56.34 | 19 | 36.0 | $150,485 | -0.48 |
| ≥15% | >=4 | flat -12% | 1029 | 57.9 | 1.472 | 2.333 | 1.465 | 0.155 | -55.2 | 17 | 37.7 | $166,638 | -0.34 |
| ≥15% | >=4 | max(8%, 1.5xATR14) | 1029 | 54.7 | 1.175 | 1.648 | 1.383 | 0.129 | -51.07 | 19 | 33.7 | $124,247 | -0.64 |
| ≥15% | >=4 | max(8%, 2.0xATR14) | 1029 | 55.1 | 1.178 | 1.753 | 1.395 | 0.127 | -48.26 | 19 | 34.1 | $123,446 | -0.63 |
| ≥12.5% | >=6 | flat -8% | 233 | 58.8 | 1.732 | 2.104 | 1.68 | 0.209 | -16.98 | 7 | 35.9 | $44,383 | -0.08 |
| ≥12.5% | >=6 | flat -10% | 233 | 60.1 | 1.763 | 2.245 | 1.673 | 0.204 | -19.16 | 7 | 37.6 | $45,192 | -0.05 |
| ≥12.5% | >=6 | flat -12% | 233 | 60.1 | 1.732 | 2.245 | 1.653 | 0.197 | -18.53 | 7 | 38.7 | $44,389 | -0.08 |
| ≥12.5% | >=6 | max(8%, 1.5xATR14) | 233 | 58.8 | 1.715 | 2.104 | 1.675 | 0.207 | -15.44 | 7 | 35.9 | $39,943 | -0.09 |
| ≥12.5% | >=6 | max(8%, 2.0xATR14) | 233 | 59.2 | 1.806 | 2.245 | 1.715 | 0.213 | -15.21 | 7 | 36.2 | $41,283 | -0.00 |
| ≥12.5% | >=5 | flat -8% | 773 | 56.9 | 1.494 | 2.058 | 1.512 | 0.171 | -40.6 | 12 | 34.7 | $127,038 | -0.32 |
| ≥12.5% | >=5 | flat -10% | 773 | 58.5 | 1.599 | 2.259 | 1.553 | 0.179 | -39.99 | 10 | 37.2 | $135,995 | -0.21 |
| ≥12.5% | >=5 | flat -12% | 773 | 59.6 | 1.757 | 2.557 | 1.625 | 0.195 | -36.25 | 10 | 38.7 | $149,433 | -0.05 |
| ≥12.5% | >=5 | max(8%, 1.5xATR14) | 773 | 56.9 | 1.466 | 2.058 | 1.508 | 0.167 | -37.75 | 12 | 34.8 | $113,921 | -0.34 |
| ≥12.5% | >=5 | max(8%, 2.0xATR14) | 773 | 57.2 | 1.499 | 2.107 | 1.534 | 0.169 | -35.37 | 10 | 35.2 | $115,755 | -0.31 |
| ≥12.5% | >=4 | flat -8% | 1261 | 55.1 | 1.284 | 1.648 | 1.414 | 0.144 | -60.06 | 27 | 33.8 | $178,120 | -0.53 |
| ≥12.5% | >=4 | flat -10% | 1261 | 56.7 | 1.349 | 1.964 | 1.43 | 0.146 | -62.99 | 27 | 36.4 | $187,155 | -0.46 |
| ≥12.5% | >=4 | flat -12% | 1261 | 58.0 | 1.473 | 2.259 | 1.476 | 0.157 | -61.97 | 19 | 38.0 | $204,343 | -0.34 |
| ≥12.5% | >=4 | max(8%, 1.5xATR14) | 1261 | 55.1 | 1.223 | 1.648 | 1.404 | 0.136 | -56.71 | 27 | 34.0 | $157,103 | -0.59 |
| ≥12.5% | >=4 | max(8%, 2.0xATR14) | 1261 | 55.4 | 1.222 | 1.753 | 1.412 | 0.134 | -54.7 | 27 | 34.4 | $154,907 | -0.59 |
| ≥10% | >=6 | flat -8% | 281 | 58.4 | 1.717 | 2.245 | 1.669 | 0.209 | -17.93 | 9 | 36.1 | $53,083 | -0.09 |
| ≥10% | >=6 | flat -10% | 281 | 59.8 | 1.765 | 2.34 | 1.673 | 0.206 | -20.3 | 9 | 37.7 | $54,543 | -0.05 |
| ≥10% | >=6 | flat -12% | 281 | 59.8 | 1.751 | 2.34 | 1.665 | 0.202 | -20.1 | 9 | 38.9 | $54,139 | -0.06 |
| ≥10% | >=6 | max(8%, 1.5xATR14) | 281 | 58.4 | 1.704 | 2.245 | 1.662 | 0.207 | -16.32 | 9 | 36.1 | $47,661 | -0.11 |
| ≥10% | >=6 | max(8%, 2.0xATR14) | 281 | 58.7 | 1.779 | 2.281 | 1.689 | 0.212 | -16.2 | 9 | 36.4 | $48,641 | -0.03 |
| ≥10% | >=5 | flat -8% | 952 | 56.8 | 1.477 | 2.027 | 1.517 | 0.173 | -46.66 | 14 | 35.1 | $154,644 | -0.33 |
| ≥10% | >=5 | flat -10% | 952 | 58.4 | 1.584 | 2.27 | 1.558 | 0.181 | -46.8 | 10 | 37.3 | $165,843 | -0.23 |
| ≥10% | >=5 | flat -12% | 952 | 59.6 | 1.736 | 2.555 | 1.63 | 0.197 | -41.77 | 10 | 38.8 | $181,768 | -0.07 |
| ≥10% | >=5 | max(8%, 1.5xATR14) | 952 | 56.8 | 1.454 | 2.027 | 1.511 | 0.17 | -43.63 | 14 | 35.1 | $138,588 | -0.36 |
| ≥10% | >=5 | max(8%, 2.0xATR14) | 952 | 57.1 | 1.504 | 2.115 | 1.543 | 0.174 | -40.46 | 10 | 35.6 | $141,839 | -0.31 |
| ≥10% | >=4 | flat -8% | 1575 | 55.2 | 1.308 | 1.618 | 1.433 | 0.149 | -66.42 | 28 | 34.3 | $226,608 | -0.50 |
| ≥10% | >=4 | flat -10% | 1575 | 56.7 | 1.385 | 1.941 | 1.455 | 0.153 | -69.02 | 23 | 36.7 | $239,958 | -0.43 |
| ≥10% | >=4 | flat -12% | 1575 | 57.9 | 1.495 | 2.222 | 1.498 | 0.163 | -68.41 | 18 | 38.2 | $259,050 | -0.31 |
| ≥10% | >=4 | max(8%, 1.5xATR14) | 1575 | 55.2 | 1.259 | 1.618 | 1.423 | 0.142 | -62.94 | 28 | 34.4 | $200,499 | -0.55 |
| ≥10% | >=4 | max(8%, 2.0xATR14) | 1575 | 55.5 | 1.264 | 1.686 | 1.432 | 0.141 | -61.36 | 23 | 34.8 | $198,290 | -0.55 |

## 3. Rankings (OOS = 2025)

### Top 5 by OOS Sharpe

| # | Combination | n | Win% | Avg% | PF | Sharpe | MaxDD% | Beats baseline OOS? | IS check |
|--:|-------------|--:|-----:|-----:|---:|-------:|------:|:-------------------:|:--------:|
| 1 | EPS≥15% / score >=4 / max(8%, 2.0xATR14) | 341 | 57.5 | 1.844 | 1.569 | 0.176 | -27.34 | ✅ | IS 1.178% ✗(rej) |
| 2 | EPS≥10% / score >=4 / max(8%, 2.0xATR14) | 502 | 58.0 | 1.685 | 1.564 | 0.172 | -33.94 | ✅ | IS 1.264% ✗(rej) |
| 3 | EPS≥12.5% / score >=4 / max(8%, 2.0xATR14) | 413 | 57.4 | 1.696 | 1.529 | 0.166 | -31.98 | ✅ | IS 1.222% ✗(rej) |
| 4 | EPS≥15% / score >=4 / flat -12% | 341 | 58.7 | 1.789 | 1.566 | 0.165 | -37.9 | ✅ | IS 1.472% ✗(rej) |
| 5 | EPS≥10% / score >=4 / flat -8% | 502 | 57.0 | 1.578 | 1.53 | 0.164 | -39.08 | ✅ | IS 1.308% ✗(rej) |

### Top 5 by OOS Profit Factor

| # | Combination | n | Win% | Avg% | PF | Sharpe | MaxDD% | Beats baseline OOS? | IS check |
|--:|-------------|--:|-----:|-----:|---:|-------:|------:|:-------------------:|:--------:|
| 1 | EPS≥15% / score >=4 / max(8%, 2.0xATR14) | 341 | 57.5 | 1.844 | 1.569 | 0.176 | -27.34 | ✅ | IS 1.178% ✗(rej) |
| 2 | EPS≥15% / score >=4 / flat -12% | 341 | 58.7 | 1.789 | 1.566 | 0.165 | -37.9 | ✅ | IS 1.472% ✗(rej) |
| 3 | EPS≥10% / score >=4 / max(8%, 2.0xATR14) | 502 | 58.0 | 1.685 | 1.564 | 0.172 | -33.94 | ✅ | IS 1.264% ✗(rej) |
| 4 | EPS≥10% / score >=4 / flat -8% | 502 | 57.0 | 1.578 | 1.53 | 0.164 | -39.08 | ✅ | IS 1.308% ✗(rej) |
| 5 | EPS≥12.5% / score >=4 / max(8%, 2.0xATR14) | 413 | 57.4 | 1.696 | 1.529 | 0.166 | -31.98 | ✅ | IS 1.222% ✗(rej) |

*“IS check” compares the same combo's IS avg return vs the IS baseline (1.81%). **Wins-OOS-but-loses-IS, or wins-IS-but-loses-OOS ⇒ rejected.** No combo here is “validated”: every candidate is flagged for a forward walk-forward / paper-trading period before any `strategy.md` change (see §6).*

**Robustness cross-check — which of the 45 combos beat the baseline in BOTH IS and OOS avg return?**
- **1** combo(s) beat baseline in both periods:
  - EPS≥15% / score >=6 / max(8%, 2.0xATR14): IS 1.899% (base 1.81%), OOS 1.313% (base 1.228%), OOS MaxDD -4.55%. — but by a thin margin and on the same entries as baseline (wider stop only bites the high-ATR minority); **reverses on 2026** (§5), so still not robust across the full window.

## 4. Does loosening the entry filter change the S3 verdict on wider stops?

S3 (standalone) tested **max(8%, 2.0×ATR) [=atr20] vs flat −8% [=flat8] with the CURRENT entry filters** on OOS = **2025+2026** and concluded *V2 does not improve on V0 out-of-sample* (0.64% vs 0.70% avg; PF 1.08 vs 1.20 → **keep V0**). This sweep re-tests that pairing **inside every looser entry combo** — a distinct hypothesis (wider stop **combined with** a looser bar), since S3 only tested it in isolation at the current bar.

**Anchor — reproduce S3 on its own OOS window (2025+2026), current bar (n=83):**
| Stop | avg% (2025 only, n=53) | avg% (2025+2026, n=83) |
|------|----------------------:|----------------------:|
| flat -8% | 1.23 | 0.7 |
| flat -10% | 0.71 | 0.27 |
| flat -12% | 0.38 | -0.06 |
| max(8%, 1.5xATR14) | 1.14 | 0.63 |
| max(8%, 2.0xATR14) | 1.31 | 0.64 |

On S3's full OOS window (2025+2026) at the current bar, **flat −8% (0.7%) still beats 2.0×ATR (0.64%)** — an exact reproduction of S3's 0.70% vs 0.64%. The 2026 slice (§5) is where wider stops clearly lose; it drags the combined figure below flat −8%.

**Why the ATR variants ≈ flat −8%:** entry-day ATR averages 2.94%/day, so max(8%, k×ATR) only lifts the stop above 8% on **13.8%** of trades at 2.0×ATR (**4.3%** at 1.5×ATR). For ~86% of names the ATR stop *is* the flat 8% stop; any edge comes from the &lt;14% of high-ATR names dodging an early noise stop (the MU case S3 studied).

Per-combo OOS = **2025 only** (the only window available at looser bars — no 2026 base in the committed data): each wider stop minus flat −8% (avg return %, identical trades per row):

| EPS | Score | n | flat−8 avg% | −10% Δ | −12% Δ | 1.5×ATR Δ | 2.0×ATR (S3) Δ |
|----:|:-----:|--:|-----------:|-------:|-------:|----------:|---------------:|
| ≥15% | >=6 | 53 | 1.228 | -0.52 | -0.85 | -0.09 | +0.08 |
| ≥15% | >=5 | 190 | 0.626 | -0.24 | -0.14 | -0.11 | +0.05 |
| ≥15% | >=4 | 341 | 1.629 | +0.01 | +0.16 | -0.03 | +0.22 |
| ≥12.5% | >=6 | 61 | 0.49 | -0.58 | -0.92 | -0.07 | +0.06 |
| ≥12.5% | >=5 | 222 | 0.391 | -0.33 | -0.30 | -0.09 | +0.01 |
| ≥12.5% | >=4 | 413 | 1.553 | -0.09 | +0.03 | -0.02 | +0.14 |
| ≥10% | >=6 | 80 | 0.927 | -0.56 | -0.53 | -0.06 | +0.04 |
| ≥10% | >=5 | 275 | 0.593 | -0.31 | -0.25 | -0.07 | -0.00 |
| ≥10% | >=4 | 502 | 1.578 | -0.12 | -0.00 | -0.03 | +0.11 |

**Verdict — CONFIRMS S3; does NOT overturn it.**
1. On S3's own OOS window (2025+2026) at the current bar, flat −8% still wins (0.7% vs 0.64%) — reproduced exactly. 2. On 2025 alone, 2.0×ATR edges flat −8% at 8/9 bars, but the edge is razor-thin (≤+0.22 pp/trade), appears **at the current bar too** (≥15/≥6: +0.08) so it is **not** a loosening effect, and **reverses on 2026** (§5: atr20 −0.55% vs flat8 −0.23%). 3. **Fixed** wider stops (−10%/−12%) are worse OOS at 7/9 bars — they only help IS (§2b), the classic overfit signature. Loosening the entry bar therefore does **not** create a robust wider-stop edge; the standalone S3 rejection stands.

## 5. 2026 YTD cross-check — current filter only (stop width × 30 enhanced trades)

The committed 2026 dataset is the **30 enhanced trades** (all already EPS≥15% & q==3 = the baseline entry combo). The full 2026 BASE population needed for the loosened-filter cells is **not** in the committed data and cannot be rebuilt here (yfinance earnings endpoint blocked in this environment), so **every loosened-filter 2026 cell is N/A** — not fabricated. This panel therefore only extends S3's 2026 stop-width finding at the current bar.

| Stop | n | Win% | Avg% | Med% | PF | Sharpe | MaxDD% | AvgHold | TotP&L |
|------|--:|-----:|-----:|-----:|---:|-------:|------:|--------:|-------:|
| flat -8% | 30 | 50.0 | -0.225 | -0.614 | 0.945 | -0.02 | -4.98 | 28.8 | $-744 |
| flat -10% | 30 | 53.3 | -0.5 | 0.577 | 0.887 | -0.043 | -5.85 | 31.4 | $-1,649 |
| flat -12% | 30 | 53.3 | -0.827 | 0.577 | 0.826 | -0.07 | -6.88 | 32.3 | $-2,730 |
| max(8%, 1.5xATR14) | 30 | 50.0 | -0.283 | -0.614 | 0.801 | -0.025 | -4.47 | 29.0 | $-2,450 |
| max(8%, 2.0xATR14) | 30 | 50.0 | -0.547 | -0.614 | 0.731 | -0.048 | -4.51 | 29.0 | $-3,243 |

*SPY 2026 YTD buy-and-hold: 10.0%. n=30 is far too small for any conclusion; shown only to check the direction of the stop-width effect on the 2026 slice against S3.*

## 6. Discipline notes & recommendation

**Bottom line:** no swept combination is a validated improvement, and the current parameters (EPS ≥15% / score ≥6 / flat −8%) remain the best *consistent* (both-period) risk-adjusted choice.
- **Loosening the entry bar** (score ≥5/≥4 or EPS ≥12.5%/≥10%) raises the *raw* OOS 2025 return and win rate, but it **underperforms baseline in-sample** and multiplies drawdown (OOS MaxDD from ~−6% at baseline to ~−27% to −48%) and max-consecutive-losses (5 → 14–22). The best-looking OOS combos are the worst IS combos — the textbook overfit signature — so they are **rejected**, not endorsed.
- **Widening the stop** confirms S3 (§4): fixed −10%/−12% mostly hurt OOS; the ATR variants are ≈ flat −8% because the ATR term clears 8% on <14% of trades, and their sliver of 2025 edge reverses on 2026.
- **If anything is worth a forward test**, it is the single razor-thin both-period combo surfaced in §3 (EPS≥15 / score≥6 / 2.0×ATR floor) — i.e. keep the current entry bar and only widen the stop for genuinely high-ATR names — and even that must clear a walk-forward / paper period first (it lost on 2026). **Do not loosen the entry filters on this evidence.**

- **Nothing here is “validated.”** This is a single historical backtest on survivorship-biased, cost-free data. Any combo that looks attractive is at most a **candidate for a forward walk-forward or paper-trading validation period** before `strategy.md` is touched — and per `CLAUDE.md`, only the human operator edits `strategy.md`.
- **IS≠OOS ⇒ reject.** Combos that beat baseline IS but not OOS (or vice-versa) are curve-fit artifacts, not edges. See the “IS check” column in §3 and the two full grids in §2.
- **Every rate above carries its raw `n`.** Loosened-EPS / loosened-score cells admit more trades but the OOS denominators still range from ~53 (baseline) to ~500 (loosest) — the tighter OOS cells remain modest samples.
- **S3 re-statement:** this sweep tests wider stops *combined with looser entry filters*, a distinct hypothesis from the standalone S3 test (wider stop, current filters). See §4 for the explicit confirm/overturn verdict.

---
*Engine: reuses the S3 `simulate()` mechanics and the committed validated candidate set. Survivorship bias, zero transaction costs/slippage, and independent-per-trade sizing (no portfolio capital constraint) apply, as in every prior report in this repo.*