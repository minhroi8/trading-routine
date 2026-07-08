#!/usr/bin/env python3
"""Compute IS/OOS performance stats for a signal's trade log, plus SPY/QQQ
buy-and-hold benchmarks over the identical calendar window. Chronological
70/30 split is done on the CALENDAR SPAN of the test window (not trade
count) -- i.e. "first 70% of the window" per the SOP's instruction, not
"first 70% of trades."
"""
import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bt_common import (
    DATA_CACHE, get_daily_bars, trade_stats, equity_curve_from_trades,
    cagr, sharpe_from_trade_equity, max_drawdown, buy_and_hold_stats,
)

API_KEY = os.environ["ALPACA_API_KEY_ID"]
API_SECRET = os.environ["ALPACA_SECRET_KEY"]


def split_is_oos(trades: pd.DataFrame, window_start: pd.Timestamp, window_end: pd.Timestamp):
    split_point = window_start + (window_end - window_start) * 0.7
    is_trades = trades[trades.entry_date <= split_point]
    oos_trades = trades[trades.entry_date > split_point]
    return is_trades, oos_trades, split_point


def summarize(trades: pd.DataFrame, label: str, start, end):
    out = {"label": label, "window_start": str(start), "window_end": str(end)}
    if trades.empty:
        out["n_trades"] = 0
        return out
    gross = trade_stats(trades, "gross_return")
    net = trade_stats(trades, "net_return")
    eq_gross = equity_curve_from_trades(trades, ret_col="gross_return")
    eq_net = equity_curve_from_trades(trades, ret_col="net_return")
    out.update({
        "n_trades": len(trades),
        "win_rate": net["win_rate"],
        "profit_factor_gross": gross["profit_factor"],
        "profit_factor_net": net["profit_factor"],
        "avg_return_gross": gross["avg_return"],
        "avg_return_net": net["avg_return"],
        "CAGR_gross": cagr(eq_gross, start, end) if not eq_gross.empty else np.nan,
        "CAGR_net": cagr(eq_net, start, end) if not eq_net.empty else np.nan,
        "Sharpe_gross": sharpe_from_trade_equity(eq_gross) if not eq_gross.empty else np.nan,
        "Sharpe_net": sharpe_from_trade_equity(eq_net) if not eq_net.empty else np.nan,
        "MaxDD_gross": max_drawdown(eq_gross) if not eq_gross.empty else np.nan,
        "MaxDD_net": max_drawdown(eq_net) if not eq_net.empty else np.nan,
        "exit_reason_counts": trades.exit_reason.value_counts().to_dict(),
    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--signal", choices=["a", "b"], required=True)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    args = ap.parse_args()

    trades = pd.read_parquet(DATA_CACHE / f"signal_{args.signal}_trades.parquet")
    trades["entry_date"] = pd.to_datetime(trades.entry_date)
    window_start = pd.Timestamp(args.start, tz="UTC")
    window_end = pd.Timestamp(args.end, tz="UTC")

    is_trades, oos_trades, split_point = split_is_oos(trades, window_start, window_end)
    print(f"Signal {args.signal.upper()}: {len(trades)} total trades, window {window_start.date()}"
          f" - {window_end.date()}, split at {split_point.date()}")
    print(f"  IS: {len(is_trades)} trades, OOS: {len(oos_trades)} trades")

    results = {
        "full": summarize(trades, "full", window_start, window_end),
        "in_sample": summarize(is_trades, "in_sample", window_start, split_point),
        "out_of_sample": summarize(oos_trades, "out_of_sample", split_point, window_end),
        "split_point": str(split_point),
    }

    # benchmarks
    for bench in ["SPY", "QQQ"]:
        bars = get_daily_bars(bench, args.start, args.end, API_KEY, API_SECRET)
        results[f"bench_{bench}_full"] = buy_and_hold_stats(bars, window_start, window_end)
        results[f"bench_{bench}_is"] = buy_and_hold_stats(bars, window_start, split_point)
        results[f"bench_{bench}_oos"] = buy_and_hold_stats(bars, split_point, window_end)

    out_path = DATA_CACHE / f"signal_{args.signal}_stats.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Wrote {out_path}")
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
