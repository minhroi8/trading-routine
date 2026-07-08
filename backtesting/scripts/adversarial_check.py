#!/usr/bin/env python3
"""Adversarial verification (per the SOP's own rule): any suspiciously
strong result should be treated as a bug until independently re-derived.

Placebo test: for every real signal trade (ticker, holding_days), draw N
random alternative entry dates on the SAME ticker within its available
history, apply the identical TP/SL/stale/end-of-window exit rule, and
compare the aggregate placebo return distribution to the real signal's
aggregate return. If the signal's return is not meaningfully better than
random-date entries on the same universe of tickers, the "signal" isn't
adding information beyond stock selection (mega-cap/insider-heavy names
that trend up anyway).
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bt_common import DATA_CACHE

N_DRAWS = 10
RNG = np.random.default_rng(42)


def simulate_exit_from(bars, entry_dt, entry_price, hard_end):
    tp = entry_price * 1.25
    sl = entry_price * 0.85
    stale_cutoff = entry_dt + pd.Timedelta(days=90)
    window = bars.loc[entry_dt + pd.Timedelta(days=1): min(stale_cutoff, hard_end)]
    for dt, row in window.iterrows():
        if row["low"] <= sl:
            return exit_return(entry_price, sl)
        if row["high"] >= tp:
            return exit_return(entry_price, tp)
    if not window.empty:
        return exit_return(entry_price, float(window.iloc[-1]["close"]))
    tail = bars.loc[:min(stale_cutoff, hard_end)]
    if tail.empty:
        return None
    return exit_return(entry_price, float(tail.iloc[-1]["close"]))


def exit_return(entry_price, exit_price):
    return exit_price / entry_price - 1


def run(signal_label, trades_path, hard_end_ts):
    trades = pd.read_parquet(trades_path)
    trades["entry_date"] = pd.to_datetime(trades.entry_date)
    real_returns = trades["gross_return"].values

    placebo_returns = []
    bars_cache = {}
    for _, row in trades.iterrows():
        ticker = row.ticker
        if ticker not in bars_cache:
            p = DATA_CACHE / "alpaca_bars" / f"{ticker}.parquet"
            bars_cache[ticker] = pd.read_parquet(p) if p.exists() else pd.DataFrame()
        bars = bars_cache[ticker]
        if bars.empty:
            continue
        eligible = bars.index[bars.index <= hard_end_ts - pd.Timedelta(days=5)]
        if len(eligible) < 10:
            continue
        for _ in range(N_DRAWS):
            alt_entry_dt = RNG.choice(eligible)
            alt_entry_dt = pd.Timestamp(alt_entry_dt)
            entry_price = float(bars.loc[alt_entry_dt, "close"])
            if entry_price < 5.0:
                continue
            r = simulate_exit_from(bars, alt_entry_dt, entry_price, hard_end_ts)
            if r is not None:
                placebo_returns.append(r)

    placebo_returns = np.array(placebo_returns)
    print(f"\n=== {signal_label} adversarial placebo check ===")
    print(f"Real signal trades: n={len(real_returns)}, mean gross return={real_returns.mean():.4f}, "
          f"win rate={np.mean(real_returns>0):.4f}")
    print(f"Placebo (random-date, same tickers) draws: n={len(placebo_returns)}, "
          f"mean gross return={placebo_returns.mean():.4f}, win rate={np.mean(placebo_returns>0):.4f}")
    percentile = (placebo_returns < real_returns.mean()).mean() * 100
    print(f"Real mean return sits at the {percentile:.1f}th percentile of the placebo distribution")
    edge = real_returns.mean() - placebo_returns.mean()
    print(f"Signal edge over placebo (mean return difference): {edge:+.4f}")
    return {
        "real_mean_return": float(real_returns.mean()),
        "real_win_rate": float(np.mean(real_returns > 0)),
        "placebo_mean_return": float(placebo_returns.mean()),
        "placebo_win_rate": float(np.mean(placebo_returns > 0)),
        "real_percentile_in_placebo_dist": float(percentile),
        "edge_vs_placebo": float(edge),
        "n_real": len(real_returns),
        "n_placebo": len(placebo_returns),
    }


if __name__ == "__main__":
    import json
    results = {}
    results["signal_b"] = run("Signal B (insider clusters)",
                               DATA_CACHE / "signal_b_trades.parquet",
                               pd.Timestamp("2024-12-31", tz="UTC"))
    results["signal_a"] = run("Signal A (Senate clusters)",
                               DATA_CACHE / "signal_a_trades.parquet",
                               pd.Timestamp("2021-03-31", tz="UTC"))
    with open(DATA_CACHE / "adversarial_check.json", "w") as f:
        json.dump(results, f, indent=2)
