#!/usr/bin/env python3
"""Signal A backtest: congressional (Senate-only) trade clusters.

Same filter/simulation logic as backtest_signal_b.py -- see that file's
docstring for the shared mechanics (entry/exit rules, cost model,
no-lookahead posture). Differences specific to Signal A:
  - Universe is 85 large/mega-cap tickers (Congress members trade blue
    chips overwhelmingly), so market-cap and OTC/leveraged-ETF rejects
    should be rare; that itself is informative and reported.
  - No per-cluster issuer CIK is available from the Senate data (unlike
    Form 4, which comes with ISSUERCIK). Ticker -> CIK is resolved via
    SEC's company_tickers.json, then market cap and the 8-K
    earnings-proximity proxy are computed exactly as in Signal B.
  - SPY is a fund, not an operating company; it has no XBRL shares
    outstanding and no 8-Ks. It is exempted from the market-cap and
    earnings-proxy filters (documented) rather than silently dropped.
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
    looks_leveraged_or_inverse, get_ticker_to_cik_map,
)

API_KEY = os.environ["ALPACA_API_KEY_ID"]
API_SECRET = os.environ["ALPACA_SECRET_KEY"]

# Senate mirror only has usable disclosure dates ~2014-01 through 2021-03;
# we do not artificially extend the window -- see fetch_congress.py.
TEST_START = pd.Timestamp("2014-01-01", tz="UTC")
TEST_END = pd.Timestamp("2021-03-31", tz="UTC")
COST_BPS_PER_SIDE = 0.0004

FUND_EXEMPT = {"SPY", "QQQ"}  # broad-market funds: exempt from mkt-cap/8-K/earnings checks


def simulate_exit(bars: pd.DataFrame, entry_date, entry_price, hard_end):
    tp = entry_price * 1.25
    sl = entry_price * 0.85
    stale_cutoff = entry_date + pd.Timedelta(days=90)
    window = bars.loc[entry_date + pd.Timedelta(days=1): min(stale_cutoff, hard_end)]
    for dt, row in window.iterrows():
        if row["low"] <= sl:
            return dt, sl, "stop_loss"
        if row["high"] >= tp:
            return dt, tp, "take_profit"
    if not window.empty and window.index[-1] >= stale_cutoff - pd.Timedelta(days=2):
        last_dt = window.index[-1]
        return last_dt, float(window.loc[last_dt, "close"]), "stale_90d"
    tail = bars.loc[:min(stale_cutoff, hard_end)]
    if tail.empty:
        return None, None, "no_data"
    last_dt = tail.index[-1]
    return last_dt, float(tail.loc[last_dt, "close"]), "end_of_window"


def main():
    cdf = pd.read_parquet(DATA_CACHE / "signal_a_clusters_raw.parquet")
    cdf = cdf.dropna(subset=["entry_date"])
    print(f"{len(cdf)} clusters with valid entry_date")

    tickers = sorted(cdf.ticker.unique())
    print(f"{len(tickers)} unique tickers")

    print("Resolving ticker -> CIK via SEC company_tickers.json ...")
    t2c = get_ticker_to_cik_map()
    ticker_cik = {t: t2c.get(t.replace("-", ".")) or t2c.get(t) for t in tickers}
    missing_cik = [t for t, c in ticker_cik.items() if c is None and t not in FUND_EXEMPT]
    if missing_cik:
        print(f"  no CIK resolved for: {missing_cik}")

    def fetch_ticker(ticker):
        bars = get_daily_bars(ticker, "2013-06-01", "2021-06-01", API_KEY, API_SECRET)
        asset = get_alpaca_asset(ticker, API_KEY, API_SECRET)
        return ticker, bars, asset

    def fetch_cik(cik):
        return cik, get_shares_outstanding_series(cik), get_8k_filing_dates(cik)

    t0 = time.time()
    bars_by_ticker, asset_by_ticker = {}, {}
    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(fetch_ticker, t): t for t in tickers}
        for fut in as_completed(futs):
            ticker, bars, asset = fut.result()
            bars_by_ticker[ticker] = bars
            asset_by_ticker[ticker] = asset
    print(f"Alpaca prefetch done in {time.time()-t0:.0f}s")

    unique_ciks = sorted({c for c in ticker_cik.values() if c is not None})
    t0 = time.time()
    shares_by_cik, k8_by_cik = {}, {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch_cik, c): c for c in unique_ciks}
        for fut in as_completed(futs):
            cik, shares_df, k8_dates = fut.result()
            shares_by_cik[cik] = shares_df
            k8_by_cik[cik] = k8_dates
    print(f"SEC prefetch done in {time.time()-t0:.0f}s")

    reject_counts = {}
    trades = []
    for ticker in tickers:
        sub = cdf[cdf.ticker == ticker]
        bars = bars_by_ticker.get(ticker)
        if bars is None or bars.empty:
            reject_counts["no_price_data"] = reject_counts.get("no_price_data", 0) + len(sub)
            continue
        asset = asset_by_ticker.get(ticker) or {}
        exchange = asset.get("exchange", "")
        cik = ticker_cik.get(ticker)
        is_fund = ticker in FUND_EXEMPT
        shares_df = shares_by_cik.get(cik) if cik else None
        k8_dates = k8_by_cik.get(cik) if cik else None

        for _, cl in sub.iterrows():
            entry_date = pd.Timestamp(cl.entry_date, tz="UTC")
            if entry_date < TEST_START or entry_date > TEST_END:
                reject_counts["outside_window"] = reject_counts.get("outside_window", 0) + 1
                continue

            window = bars.loc[entry_date: entry_date + pd.Timedelta(days=5)]
            if window.empty:
                reject_counts["no_entry_bar"] = reject_counts.get("no_entry_bar", 0) + 1
                continue
            entry_price = float(window.iloc[0]["close"])
            actual_entry_dt = window.index[0]

            if entry_price < 5.0:
                reject_counts["price_below_5"] = reject_counts.get("price_below_5", 0) + 1
                continue
            if exchange == "OTC":
                reject_counts["otc"] = reject_counts.get("otc", 0) + 1
                continue
            if looks_leveraged_or_inverse(asset.get("name", "")):
                reject_counts["leveraged_inverse_name"] = reject_counts.get("leveraged_inverse_name", 0) + 1
                continue

            if not is_fund:
                if shares_df is None or shares_df.empty:
                    reject_counts["no_shares_outstanding_data"] = reject_counts.get("no_shares_outstanding_data", 0) + 1
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
            else:
                mkt_cap = None

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

            exit_dt, exit_price, exit_reason = simulate_exit(bars, actual_entry_dt, entry_price, TEST_END)
            if exit_dt is None:
                reject_counts["no_exit_data"] = reject_counts.get("no_exit_data", 0) + 1
                continue

            gross_return = exit_price / entry_price - 1
            eff_entry = entry_price * (1 + COST_BPS_PER_SIDE)
            eff_exit = exit_price * (1 - COST_BPS_PER_SIDE)
            net_return = eff_exit / eff_entry - 1

            trades.append({
                "ticker": ticker, "n_members": cl.n_members, "confirm_date": cl.confirm_date,
                "source_trade_date": cl.source_trade_date,
                "entry_date": actual_entry_dt, "entry_price": entry_price,
                "exit_date": exit_dt, "exit_price": exit_price, "exit_reason": exit_reason,
                "market_cap_at_entry": mkt_cap, "gross_return": gross_return,
                "net_return": net_return, "holding_days": (exit_dt - actual_entry_dt).days,
                "disclosure_lag_days": (cl.confirm_date - cl.source_trade_date).days,
            })

    tdf = pd.DataFrame(trades)
    print(f"\n{len(tdf)} trades survived all filters")
    print("\nRejection reasons:")
    for k, v in sorted(reject_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    out = DATA_CACHE / "signal_a_trades.parquet"
    tdf.to_parquet(out, index=False)
    print(f"\nWrote {out}")
    pd.DataFrame(sorted(reject_counts.items(), key=lambda x: -x[1]), columns=["reason", "count"]) \
        .to_csv(DATA_CACHE / "signal_a_rejections.csv", index=False)


if __name__ == "__main__":
    main()
