#!/usr/bin/env python3
"""Signal B backtest: insider Form 4 open-market-purchase clusters.

Pipeline:
  1. Load raw clusters (detect_clusters_signal_b.py output).
  2. Clean tickers; drop malformed symbols.
  3. Per unique ticker: fetch Alpaca daily bars (2018-06 .. 2025-01, cached),
     Alpaca asset metadata (exchange/OTC check, cached), SEC shares-
     outstanding series (market-cap proxy, cached), SEC 8-K filing dates
     (earnings-proximity proxy, cached).
  4. Per cluster: apply shared filters (>=$5, >=$2B mkt cap, not OTC, not
     leveraged/inverse, not within 2 trading days of an 8-K, not already
     up >15% since the source trade date).
  5. Simulate the trade: entry = close on entry_date; exit = TP +25% /
     SL -15% (checked via daily high/low) / 90-calendar-day stale / end
     of window (2024-12-31), whichever comes first.
  6. Apply 4bp-per-side cost model (gross and net both saved).

No live orders are placed; Alpaca is used only for its read-only
historical market-data endpoint.
"""
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bt_common import (
    DATA_CACHE, get_daily_bars, get_alpaca_asset, get_shares_outstanding_series,
    shares_outstanding_as_of, get_8k_filing_dates, near_earnings_proxy,
    looks_leveraged_or_inverse, trading_day_index,
)

API_KEY = os.environ["ALPACA_API_KEY_ID"]
API_SECRET = os.environ["ALPACA_SECRET_KEY"]

TEST_START = pd.Timestamp("2019-01-01", tz="UTC")
TEST_END = pd.Timestamp("2024-12-31", tz="UTC")
COST_BPS_PER_SIDE = 0.0004  # 4 bp, midpoint of the SOP's stated 3-5bp range

VALID_TICKER_RE = r"^[A-Z]{1,6}(\.[A-Z])?$"


def simulate_exit(bars: pd.DataFrame, entry_date, entry_price):
    tp = entry_price * 1.25
    sl = entry_price * 0.85
    stale_cutoff = entry_date + pd.Timedelta(days=90)
    window = bars.loc[entry_date + pd.Timedelta(days=1): min(stale_cutoff, TEST_END)]
    for dt, row in window.iterrows():
        if row["low"] <= sl:
            return dt, sl, "stop_loss"
        if row["high"] >= tp:
            return dt, tp, "take_profit"
    if not window.empty and window.index[-1] >= stale_cutoff - pd.Timedelta(days=2):
        last_dt = window.index[-1]
        return last_dt, float(window.loc[last_dt, "close"]), "stale_90d"
    # ran off the end of the available window (end of test period)
    tail = bars.loc[:min(stale_cutoff, TEST_END)]
    if tail.empty:
        return None, None, "no_data"
    last_dt = tail.index[-1]
    return last_dt, float(tail.loc[last_dt, "close"]), "end_of_window"


def main():
    cdf = pd.read_parquet(DATA_CACHE / "signal_b_clusters_raw.parquet")
    cdf = cdf[cdf.ticker.str.match(VALID_TICKER_RE, na=False)].copy()
    cdf = cdf.dropna(subset=["entry_date"])
    print(f"{len(cdf)} clusters with valid ticker + entry_date")

    tickers = sorted(cdf.ticker.unique())
    print(f"{len(tickers)} unique tickers to enrich")
    ticker_to_cik = cdf.drop_duplicates("ticker").set_index("ticker").issuer_cik.astype(int).to_dict()

    def fetch_ticker(ticker):
        cik = ticker_to_cik[ticker]
        bars = get_daily_bars(ticker, "2018-06-01", "2025-01-05", API_KEY, API_SECRET)
        asset = get_alpaca_asset(ticker, API_KEY, API_SECRET)
        return ticker, bars, asset

    def fetch_cik(cik):
        shares_df = get_shares_outstanding_series(cik)
        k8_dates = get_8k_filing_dates(cik)
        return cik, shares_df, k8_dates

    print("Prefetching Alpaca bars + assets (parallel)...", flush=True)
    t0 = time.time()
    bars_by_ticker, asset_by_ticker = {}, {}
    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(fetch_ticker, t): t for t in tickers}
        for i, fut in enumerate(as_completed(futs)):
            ticker, bars, asset = fut.result()
            bars_by_ticker[ticker] = bars
            asset_by_ticker[ticker] = asset
            if i % 400 == 0:
                print(f"  [alpaca {i}/{len(tickers)}] elapsed {time.time()-t0:.0f}s", flush=True)
    print(f"Alpaca prefetch done in {time.time()-t0:.0f}s", flush=True)

    unique_ciks = sorted(set(ticker_to_cik.values()))
    print(f"Prefetching SEC data for {len(unique_ciks)} CIKs (parallel, throttled)...", flush=True)
    t0 = time.time()
    shares_by_cik, k8_by_cik = {}, {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch_cik, c): c for c in unique_ciks}
        for i, fut in enumerate(as_completed(futs)):
            cik, shares_df, k8_dates = fut.result()
            shares_by_cik[cik] = shares_df
            k8_by_cik[cik] = k8_dates
            if i % 400 == 0:
                print(f"  [sec {i}/{len(unique_ciks)}] elapsed {time.time()-t0:.0f}s", flush=True)
    print(f"SEC prefetch done in {time.time()-t0:.0f}s", flush=True)

    reject_counts = {}
    trades = []
    for i, ticker in enumerate(tickers):
        sub = cdf[cdf.ticker == ticker]
        cik = ticker_to_cik[ticker]

        bars = bars_by_ticker.get(ticker)
        if bars is None or bars.empty:
            reject_counts["no_price_data"] = reject_counts.get("no_price_data", 0) + len(sub)
            continue

        asset = asset_by_ticker.get(ticker) or {}
        exchange = asset.get("exchange", "")
        asset_class = asset.get("class", "")
        shares_df = shares_by_cik.get(cik)
        k8_dates = k8_by_cik.get(cik)

        for _, cl in sub.iterrows():
            entry_date = pd.Timestamp(cl.entry_date, tz="UTC")
            if entry_date < TEST_START or entry_date > TEST_END:
                reject_counts["outside_window"] = reject_counts.get("outside_window", 0) + 1
                continue

            entry_price, actual_entry_dt = None, None
            window = bars.loc[entry_date: entry_date + pd.Timedelta(days=5)]
            if not window.empty:
                entry_price = float(window.iloc[0]["close"])
                actual_entry_dt = window.index[0]
            if entry_price is None:
                reject_counts["no_entry_bar"] = reject_counts.get("no_entry_bar", 0) + 1
                continue

            if entry_price < 5.0:
                reject_counts["price_below_5"] = reject_counts.get("price_below_5", 0) + 1
                continue

            if exchange in ("OTC", "") and asset_class != "us_equity":
                reject_counts["otc_or_unknown_exchange"] = reject_counts.get("otc_or_unknown_exchange", 0) + 1
                continue
            if exchange == "OTC":
                reject_counts["otc"] = reject_counts.get("otc", 0) + 1
                continue

            if looks_leveraged_or_inverse(cl.issuer_name):
                reject_counts["leveraged_inverse_name"] = reject_counts.get("leveraged_inverse_name", 0) + 1
                continue

            shares_out = shares_outstanding_as_of(shares_df, actual_entry_dt.tz_localize(None))
            if shares_out is None:
                reject_counts["no_shares_outstanding_data"] = reject_counts.get("no_shares_outstanding_data", 0) + 1
                continue
            mkt_cap = shares_out * entry_price
            if mkt_cap < 2e9:
                reject_counts["mktcap_below_2b"] = reject_counts.get("mktcap_below_2b", 0) + 1
                continue

            if near_earnings_proxy(k8_dates, actual_entry_dt.tz_localize(None), window_trading_days=2):
                reject_counts["near_earnings_8k_proxy"] = reject_counts.get("near_earnings_8k_proxy", 0) + 1
                continue

            src_window = bars.loc[
                pd.Timestamp(cl.source_trade_date, tz="UTC") - pd.Timedelta(days=5):
                pd.Timestamp(cl.source_trade_date, tz="UTC") + pd.Timedelta(days=5)]
            if src_window.empty:
                reject_counts["no_source_price"] = reject_counts.get("no_source_price", 0) + 1
                continue
            src_price = float(src_window.iloc[0]["close"])
            runup = entry_price / src_price - 1
            if runup > 0.15:
                reject_counts["runup_over_15pct"] = reject_counts.get("runup_over_15pct", 0) + 1
                continue

            exit_dt, exit_price, exit_reason = simulate_exit(bars, actual_entry_dt, entry_price)
            if exit_dt is None:
                reject_counts["no_exit_data"] = reject_counts.get("no_exit_data", 0) + 1
                continue

            gross_return = exit_price / entry_price - 1
            eff_entry = entry_price * (1 + COST_BPS_PER_SIDE)
            eff_exit = exit_price * (1 - COST_BPS_PER_SIDE)
            net_return = eff_exit / eff_entry - 1

            trades.append({
                "ticker": ticker, "issuer_cik": cik, "issuer_name": cl.issuer_name,
                "n_insiders": cl.n_insiders, "confirm_date": cl.confirm_date,
                "entry_date": actual_entry_dt, "entry_price": entry_price,
                "exit_date": exit_dt, "exit_price": exit_price, "exit_reason": exit_reason,
                "market_cap_at_entry": mkt_cap, "gross_return": gross_return,
                "net_return": net_return, "holding_days": (exit_dt - actual_entry_dt).days,
            })

    tdf = pd.DataFrame(trades)
    print(f"\n{len(tdf)} trades survived all filters")
    print("\nRejection reasons:")
    for k, v in sorted(reject_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    out = DATA_CACHE / "signal_b_trades.parquet"
    tdf.to_parquet(out, index=False)
    print(f"\nWrote {out}")

    reject_df = pd.DataFrame(sorted(reject_counts.items(), key=lambda x: -x[1]),
                              columns=["reason", "count"])
    reject_df.to_csv(DATA_CACHE / "signal_b_rejections.csv", index=False)


if __name__ == "__main__":
    main()
