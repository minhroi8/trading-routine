#!/usr/bin/env python3
"""Detect Signal B clusters: 2+ distinct insiders (CEO/CFO/director,
transaction code P only) buying the same ticker within 10 trading days.

No-lookahead: a cluster's "confirmation date" is the max(FILING_DATE) of
the two trades that establish the 2-distinct-insider threshold -- the
first moment a real observer watching EDGAR could know both purchases
happened. Entry is simulated on the next trading session after that.

De-duplication: once a cluster fires for a ticker, the accumulation
window resets, so a run of insider buying doesn't spawn overlapping
duplicate signals. This is conservative (fewer signals, not more).
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bt_common import trading_day_index, next_trading_day, DATA_CACHE

WINDOW_TRADING_DAYS = 10


def is_target_insider(relationship, title) -> bool:
    rel = relationship if isinstance(relationship, str) else ""
    if "Director" in rel:
        return True
    t = (title if isinstance(title, str) else "").lower()
    return ("chief executive" in t) or ("chief financial" in t) or t.strip() in ("ceo", "cfo")


def main():
    df = pd.read_parquet(DATA_CACHE / "form4_code_p_2019_2024.parquet")
    print(f"Loaded {len(df)} raw code-P Form 4 rows")

    # exclude 10b5-1-flagged transactions (only known for filings after
    # Apr-2023 when the checkbox was added; NaN = unknown, kept but flagged
    # in the report rather than silently treated as "not a 10b5-1 trade")
    df["is_10b5_1"] = df.AFF10B5ONE.astype(str).str.lower().isin(["1", "true"])
    before = len(df)
    df = df[~df.is_10b5_1]
    print(f"Excluded {before - len(df)} rows flagged as Rule 10b5-1 plan trades")

    df = df[df.ISSUERTRADINGSYMBOL.notna() & (df.ISSUERTRADINGSYMBOL.str.strip() != "")]
    df["is_target"] = df.apply(
        lambda r: is_target_insider(r.RPTOWNER_RELATIONSHIP, r.RPTOWNER_TITLE), axis=1)
    before = len(df)
    df = df[df.is_target]
    print(f"Kept {len(df)}/{before} rows where reporting owner is CEO/CFO/director")

    df["trans_date"] = pd.to_datetime(df.TRANS_DATE, format="%d-%b-%Y", errors="coerce")
    df["filing_date"] = pd.to_datetime(df.FILING_DATE, format="%d-%b-%Y", errors="coerce")
    df = df.dropna(subset=["trans_date", "filing_date"])
    df["ticker"] = df.ISSUERTRADINGSYMBOL.str.strip().str.upper()
    df["td_idx"] = df.trans_date.apply(trading_day_index)
    df = df.dropna(subset=["td_idx"])
    df["td_idx"] = df.td_idx.astype(int)

    df = df.sort_values(["ticker", "trans_date", "filing_date"])

    clusters = []
    for ticker, g in df.groupby("ticker"):
        g = g.sort_values(["trans_date", "filing_date"]).reset_index(drop=True)
        window = []  # list of dict rows
        for _, row in g.iterrows():
            # drop window entries older than WINDOW_TRADING_DAYS relative to this trade
            window = [w for w in window if row.td_idx - w["td_idx"] <= WINDOW_TRADING_DAYS]
            window.append(row.to_dict())
            distinct_owners = {w["RPTOWNERCIK"] for w in window}
            if len(distinct_owners) >= 2:
                confirm_date = max(w["filing_date"] for w in window)
                source_date = min(w["trans_date"] for w in window)
                clusters.append({
                    "ticker": ticker,
                    "issuer_cik": row.ISSUERCIK,
                    "issuer_name": row.ISSUERNAME,
                    "n_insiders": len(distinct_owners),
                    "insider_ciks": ",".join(str(int(c)) for c in distinct_owners),
                    "cluster_trades_n": len(window),
                    "source_trade_date": source_date,
                    "last_trade_date": row.trans_date,
                    "confirm_date": confirm_date,
                    "entry_date": next_trading_day(confirm_date),
                    "avg_trans_price": sum(w["TRANS_PRICEPERSHARE"] or 0 for w in window) / len(window),
                })
                window = []  # reset after firing

    cdf = pd.DataFrame(clusters)
    print(f"\nDetected {len(cdf)} raw Signal B clusters (pre shared-filter application)")
    if not cdf.empty:
        print("Date range (confirm_date):", cdf.confirm_date.min(), "to", cdf.confirm_date.max())
    out = DATA_CACHE / "signal_b_clusters_raw.parquet"
    cdf.to_parquet(out, index=False)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
