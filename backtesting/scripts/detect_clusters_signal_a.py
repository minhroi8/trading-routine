#!/usr/bin/env python3
"""Detect Signal A clusters: 2+ distinct Congress members buying the same
ticker within 6 weeks (calendar weeks, per the SOP's own definition --
Signal B uses trading days, Signal A uses calendar weeks, deliberately).

SENATE ONLY: see fetch_congress.py docstring for why House data could not
be sourced (S3 bucket AccessDenied, housestockwatcher.com down, no GitHub
mirror found). This is a real scope reduction from "congressional trade
clusters," not an approximation choice.

No-lookahead: confirmation date = max(disclosure_date) of the 2 filings
that establish the cluster (disclosure_date == date_recieved by the
Senate Ethics office, i.e. when the PTR became public) -- never
transaction_date, which the SOP explicitly forbids trading on directly.
Entry = next trading session after confirmation.
"""
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bt_common import next_trading_day, DATA_CACHE

WINDOW_DAYS = 42  # 6 calendar weeks


def clean_ticker(raw):
    if not isinstance(raw, str):
        return None
    # some entries are HTML anchors e.g. '<a href="...">DNKN</a>'
    m = re.search(r">([A-Z.\-]{1,6})<", raw)
    if m:
        return m.group(1)
    raw = raw.strip()
    if re.match(r"^[A-Z.\-]{1,6}$", raw) and raw not in ("N/A", "--"):
        return raw
    return None


def main():
    df = pd.read_parquet(DATA_CACHE / "senate_transactions_raw.parquet")
    print(f"Loaded {len(df)} raw Senate transaction rows")

    df = df[df.type == "Purchase"].copy()
    print(f"{len(df)} Purchase-type rows")

    df["ticker"] = df.ticker_raw.apply(clean_ticker)
    df = df.dropna(subset=["ticker"])
    print(f"{len(df)} rows with a resolvable ticker")

    df["transaction_date"] = pd.to_datetime(df.transaction_date, format="%m/%d/%Y", errors="coerce")
    df["disclosure_date"] = pd.to_datetime(df.disclosure_date, format="%m/%d/%Y", errors="coerce")
    df = df.dropna(subset=["transaction_date", "disclosure_date"])

    # a senator can appear more than once per filing (different transactions);
    # dedupe to (senator, ticker, transaction_date) so the same disclosed
    # trade isn't counted twice
    df = df.drop_duplicates(subset=["bioguide", "senator", "ticker", "transaction_date", "amount"])
    df = df.sort_values(["ticker", "transaction_date", "disclosure_date"])

    clusters = []
    for ticker, g in df.groupby("ticker"):
        g = g.sort_values(["transaction_date", "disclosure_date"]).reset_index(drop=True)
        window = []
        for _, row in g.iterrows():
            window = [w for w in window
                      if (row.transaction_date - w["transaction_date"]).days <= WINDOW_DAYS]
            window.append(row.to_dict())
            distinct_members = {w["bioguide"] or w["senator"] for w in window}
            if len(distinct_members) >= 2:
                confirm_date = max(w["disclosure_date"] for w in window)
                source_date = min(w["transaction_date"] for w in window)
                clusters.append({
                    "ticker": ticker,
                    "n_members": len(distinct_members),
                    "members": ",".join(sorted(str(m) for m in distinct_members)),
                    "cluster_txns_n": len(window),
                    "source_trade_date": source_date,
                    "last_trade_date": row.transaction_date,
                    "confirm_date": confirm_date,
                    "entry_date": next_trading_day(confirm_date),
                })
                window = []

    cdf = pd.DataFrame(clusters)
    print(f"\nDetected {len(cdf)} raw Signal A (Senate) clusters")
    if not cdf.empty:
        print("Date range (confirm_date):", cdf.confirm_date.min(), "to", cdf.confirm_date.max())
    out = DATA_CACHE / "signal_a_clusters_raw.parquet"
    cdf.to_parquet(out, index=False)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
