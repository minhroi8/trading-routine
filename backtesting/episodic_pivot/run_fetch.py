"""Fetch & cache adjusted OHLCV for all event tickers + benchmarks. Reports
coverage — missing names document the shared survivorship gap."""
import json, os, sys
import ep_engine as E

def main():
    ev = E.load_events()
    tickers = sorted(ev.ticker.unique())
    print(f"Fetching {len(tickers)} event tickers + SPY,QQQ ...")
    ok, missing = [], []
    for i, t in enumerate(tickers):
        h = E.cached_history(t)
        (ok if h is not None else missing).append(t)
        if i % 50 == 0:
            print(f"  {i}/{len(tickers)}  ok={len(ok)} missing={len(missing)}")
    for b in ("SPY", "QQQ"):
        h = E.cached_history(b)
        print(f"  benchmark {b}: {'OK '+str(len(h))+' rows' if h is not None else 'MISSING'}")
    print(f"\nCoverage: {len(ok)}/{len(tickers)} fetched; {len(missing)} missing")
    print("Missing (likely delisted/renamed — the survivorship gap):", missing)
    cov = {"n_tickers": len(tickers), "n_ok": len(ok), "n_missing": len(missing),
           "missing": missing}
    with open(os.path.join(E.REPORTS_DIR, "coverage.json"), "w") as f:
        json.dump(cov, f, indent=2)

if __name__ == "__main__":
    sys.path.insert(0, E.SCRIPT_DIR)
    main()
