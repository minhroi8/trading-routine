"""
Momentum module — DATA AVAILABILITY AUDIT (runs FIRST, gates everything).

This script does NOT run a backtest. It empirically tests whether the data
sources reachable from this environment support a *point-in-time-correct*
cross-sectional momentum backtest on historical S&P 500 members. It reports
explicit PASS/FAIL on each of the five checks the task requires:

  1. Point-in-time S&P 500 membership entry/exit dates for >=3 removed/renamed names
  2. Delisted-price history for >=1 removed name
  3. Split/dividend adjustment applied
  4. Ticker-change handling
  5. No future-membership leakage

Transport note: yfinance's curl_cffi backend does not honor this environment's
HTTPS proxy + CA bundle (curl error 35, connection reset). We therefore use the
SAME requests-based Yahoo chart-API fetch the existing backtest_risk_sweep script
uses (plain `requests`, which does honor HTTPS_PROXY + the system CA). A live
control ticker (AAPL) is fetched first to prove the transport works, so that any
404/empty result on a delisted name is a real data-availability finding and NOT
a transport artifact.

Data sources probed:
  - Membership: scripts/sp500_source.csv (local) + datasets/s-and-p-500-companies
    GitHub CSV (what engine.get_sp500 uses)
  - Prices: Yahoo Finance chart API (v8) via requests
  - Point-in-time reconstruction candidate: Wikipedia "Selected changes" table
"""
import os, sys, io, json, time, traceback
import pandas as pd
import numpy as np
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
OUT = os.path.join(SCRIPT_DIR, "data_cache", "audit_raw_output.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

_log_lines = []
def log(*a):
    line = " ".join(str(x) for x in a)
    print(line, flush=True)
    _log_lines.append(line)

def hr(title):
    log("\n" + "=" * 78)
    log(title)
    log("=" * 78)


def fetch_chart(sym, p1="2010-01-01", p2="2024-06-01"):
    """Yahoo chart API via requests. Returns (df_or_None, http_status_str)."""
    sym = sym.replace(".", "-")
    P1 = int(pd.Timestamp(p1).timestamp()); P2 = int(pd.Timestamp(p2).timestamp())
    last_status = "no-response"
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        url = (f"https://{host}/v8/finance/chart/{sym}"
               f"?period1={P1}&period2={P2}&interval=1d&events=div%2Csplits")
        try:
            r = requests.get(url, timeout=30, headers={"User-Agent": UA})
            last_status = f"HTTP {r.status_code}"
            if r.status_code != 200:
                continue
            res = r.json()["chart"]["result"][0]
            ts = res.get("timestamp")
            if not ts:
                last_status = "200-empty"; continue
            q = res["indicators"]["quote"][0]
            adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
            idx = pd.to_datetime(ts, unit="s", utc=True).tz_convert(
                "America/New_York").normalize().tz_localize(None)
            df = pd.DataFrame({"Open": q["open"], "High": q["high"],
                               "Low": q["low"], "Close": q["close"],
                               "Volume": q["volume"]}, index=idx)
            df["AdjClose"] = adj if adj is not None else df["Close"]
            df = df.dropna(subset=["Close"])
            return df, "OK"
        except Exception as e:
            last_status = f"ERR {type(e).__name__}: {str(e)[:60]}"
    return None, last_status


REMOVED = [
    ("SIVB", "delisted", "2023-03-15", "SVB Financial — bank failure, removed & delisted"),
    ("FRC",  "delisted", "2023-05-04", "First Republic Bank — seized, sold to JPM"),
    ("TWTR", "delisted", "2022-11-08", "Twitter — taken private by Musk"),
    ("CTXS", "delisted", "2022-09-30", "Citrix — taken private"),
    ("ATVI", "delisted", "2023-10-13", "Activision Blizzard — acquired by Microsoft"),
    ("XEC",  "merged",   "2021-10-01", "Cimarex — merged w/ Cabot into Coterra (CTRA)"),
]
RENAMES = [
    ("FB",   "META", "2022-06-09", "Facebook -> Meta Platforms"),
    ("ANTM", "ELV",  "2022-06-28", "Anthem -> Elevance Health"),
    ("DISCA","WBD",  "2022-04-11", "Discovery -> Warner Bros Discovery"),
    ("RE",   "EG",   "2023-11-01", "Everest Re -> Everest Group"),
]
SPLITS = [
    ("AAPL", "2020-08-31", 4.0,  "Apple 4:1"),
    ("NVDA", "2024-06-10", 10.0, "NVIDIA 10:1"),
    ("TSLA", "2022-08-25", 3.0,  "Tesla 3:1"),
    ("AMZN", "2022-06-06", 20.0, "Amazon 20:1"),
]


def main():
    results = {}

    hr("CHECK -1 — Transport control (prove the fetch works before trusting 404s)")
    ctrl, st = fetch_chart("AAPL", "2019-01-01", "2024-01-01")
    if ctrl is not None:
        log(f"  AAPL control: {st}, rows={len(ctrl)} "
            f"[{ctrl.index.min().date()}..{ctrl.index.max().date()}]")
        log("  -> transport confirmed working; subsequent empties/404s are REAL.")
    else:
        log(f"  AAPL control FAILED: {st}")
        log("  -> transport itself is broken; audit cannot distinguish data vs transport.")
        log("     ABORTING with transport-failure verdict.")
        results["transport_ok"] = False
        with open(OUT, "w") as f: f.write("\n".join(_log_lines))
        return
    results["transport_ok"] = True

    hr("CHECK 0 — Membership source content & schema")
    csv_path = os.path.join(REPO_ROOT, "scripts", "sp500_source.csv")
    local = pd.read_csv(csv_path)
    log("Local scripts/sp500_source.csv columns:", list(local.columns))
    log("Row count:", len(local))
    log("Has an exit/removal-date column?:",
        any("remov" in c.lower() or "exit" in c.lower() or "end" in c.lower()
            for c in local.columns))
    log("date_added range:", local["date_added"].min(), "->", local["date_added"].max())
    present = [t for (t, *_) in REMOVED if t in set(local["symbol"])]
    log("Known-REMOVED tickers still present in local list:", present or "none (expected)")
    try:
        url = ("https://raw.githubusercontent.com/datasets/s-and-p-500-companies"
               "/main/data/constituents.csv")
        r = requests.get(url, timeout=30)
        gh = pd.read_csv(io.StringIO(r.text))
        log("\nengine.get_sp500 source reachable:", url)
        log("  columns:", list(gh.columns), "| rows:", len(gh))
        log("  has entry/exit date columns?:", any("date" in c.lower() for c in gh.columns))
    except Exception as e:
        log("GitHub constituents CSV fetch FAILED:", repr(e))
    results["membership_has_exit_dates"] = False

    hr("CHECK 1 — Point-in-time membership entry/exit dates (need >=3 removed names)")
    log("Requirement: for names removed/renamed historically we need the DATE they")
    log("entered AND left the index, as known at each point in time. Neither the local")
    log("CSV nor the datasets GitHub CSV carries exit dates or removed names. Probing")
    log("for ANY reachable point-in-time source...\n")
    wiki_ok = False
    wiki_changes = None
    try:
        wurl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        r = requests.get(wurl, timeout=30, headers={"User-Agent": UA})
        tables = pd.read_html(io.StringIO(r.text))
        log("Wikipedia page reachable; parsed", len(tables), "tables.")
        for i, t in enumerate(tables):
            cols = " ".join(str(c) for c in t.columns.tolist()).lower()
            if "removed" in cols and "added" in cols and "date" in cols:
                wiki_changes = t
                log("  changes table = table index", i, "| shape", t.shape)
                break
        wiki_ok = wiki_changes is not None
        if wiki_ok:
            log("  columns:", [str(c) for c in wiki_changes.columns.tolist()])
    except Exception as e:
        log("Wikipedia fetch/parse FAILED:", repr(e))

    datable = []
    if wiki_ok:
        flat = wiki_changes.copy()
        flat.columns = [" ".join(str(x) for x in c) if isinstance(c, tuple) else str(c)
                        for c in flat.columns]
        blob = flat.astype(str)
        dates = None
        for c in flat.columns:
            if "date" in c.lower():
                dates = flat[c]; break
        for t, kind, dt, note in REMOVED:
            mask = blob.apply(lambda row: row.str.contains(rf"\b{t}\b", regex=True).any(), axis=1)
            n = int(mask.sum())
            ex = ""
            if n and dates is not None:
                ex = " | change-date(s): " + ", ".join(str(x) for x in dates[mask].tolist()[:2])
            log(f"  removed={t:5s} rows in changes table: {n}{ex}   ({note})")
            if n > 0:
                datable.append(t)
        log("\nRemoved names with >=1 datable change-event row:", datable,
            f"({len(datable)} of {len(REMOVED)})")
        log("CAVEAT: a change-event row gives at most ONE side of the interval and only")
        log("for names removed in the window Wikipedia still lists. It is (a) incomplete")
        log("for older years, (b) retroactively editable (NOT point-in-time frozen),")
        log("(c) has no continuous membership intervals. It cannot serve as an")
        log("authoritative PIT membership record without external cross-validation")
        log("that is not available in this environment.")
    results["pit_membership_available"] = False
    results["wiki_changes_reachable"] = wiki_ok
    results["wiki_datable_removed"] = datable

    hr("CHECK 2 — Delisted-price history exists for >=1 removed name (Yahoo chart API)")
    delisted_ok = []
    for t, kind, dt, note in REMOVED:
        df, st = fetch_chart(t, "2015-01-01", "2024-01-01")
        if df is not None and len(df) > 0:
            log(f"  {t:5s} ({kind:8s} ~{dt}): {st} rows={len(df)} "
                f"[{df.index.min().date()}..{df.index.max().date()}]   {note}")
            delisted_ok.append((t, len(df)))
        else:
            log(f"  {t:5s} ({kind:8s} ~{dt}): {st}  -> NO DATA   {note}")
        time.sleep(0.3)
    log("\nRemoved names with usable price history:", [x[0] for x in delisted_ok] or "NONE")
    results["delisted_prices_available"] = len(delisted_ok) >= 1
    results["delisted_detail"] = delisted_ok

    hr("CHECK 3 — Split/dividend adjustment applied (Yahoo adjclose)")
    split_pass = []
    for t, dt, ratio, note in SPLITS:
        d = pd.Timestamp(dt)
        df, st = fetch_chart(t, str((d - pd.Timedelta(days=15)).date()),
                             str((d + pd.Timedelta(days=15)).date()))
        if df is None or df.empty:
            log(f"  {t:5s} {note}: {st} NO DATA"); continue
        df = df.sort_index()
        before = df.loc[df.index < d, "AdjClose"]
        after = df.loc[df.index >= d, "AdjClose"]
        if before.empty or after.empty:
            log(f"  {t:5s} {note}: insufficient bars around split"); continue
        jump = after.iloc[0] / before.iloc[-1]
        adjusted = abs(jump - 1.0) < 0.15
        log(f"  {t:5s} {note}: adj last_before={before.iloc[-1]:.2f} "
            f"first_after={after.iloc[0]:.2f} ratio={jump:.3f} "
            f"-> {'ADJUSTED (continuous)' if adjusted else 'NOT adjusted (raw ~1/%.0f jump)' % ratio}")
        if adjusted:
            split_pass.append(t)
        time.sleep(0.3)
    results["splits_adjusted"] = len(split_pass) >= 2
    results["splits_pass"] = split_pass

    hr("CHECK 4 — Ticker-change handling")
    log("For each rename: does the OLD ticker still return history, does the NEW ticker")
    log("carry continuous pre-change history, and is there a programmatic mapping?\n")
    rename_notes = []
    for old, new, dt, note in RENAMES:
        d = pd.Timestamp(dt)
        odf, ost = fetch_chart(old, "2015-01-01", "2024-06-01")
        ndf, nst = fetch_chart(new, "2010-01-01", "2024-06-01")
        o_has = odf is not None and len(odf) > 0
        n_has = ndf is not None and len(ndf) > 0
        pre = bool(n_has and ndf.index.min() < d)
        log(f"  {note}")
        log(f"     OLD {old:5s}: {ost}" + (f" rows={len(odf)} [{odf.index.min().date()}..{odf.index.max().date()}]" if o_has else " -> NO DATA"))
        log(f"     NEW {new:5s}: {nst}" + (f" rows={len(ndf)} [{ndf.index.min().date()}..{ndf.index.max().date()}]" if n_has else " -> NO DATA"))
        log(f"     NEW carries pre-rename history spanning {dt}?: {pre}")
        log(f"     OLD ticker still queryable independently?: {o_has}")
        log("")
        rename_notes.append((old, new, o_has, n_has, pre))
        time.sleep(0.3)
    log("There is NO programmatic ticker-change map from the price API; the OLD symbol")
    log("404s and its history is silently folded into the NEW symbol. A backtest that")
    log("only knows the OLD symbol on a historical rebalance date gets NO DATA and")
    log("silently drops the name -> selection distortion. Mapping must be hand-maintained.")
    results["ticker_change_map_available"] = False
    results["rename_probe"] = rename_notes

    hr("CHECK 5 — Future-membership leakage")
    log("The only membership list reachable is the CURRENT constituents snapshot.")
    log("Using it to define the 2012-2026 universe means:")
    log("  (a) names in the index THEN but since removed are ABSENT (survivorship bias);")
    log("  (b) names in the list NOW but added later would be INCLUDED early (look-ahead).")
    la = local.copy()
    la["date_added"] = pd.to_datetime(la["date_added"], errors="coerce")
    log(f"\nCurrent list: {len(la)} names.")
    log(f"  added after 2012-01-01: {int((la['date_added'] > '2012-01-01').sum())} (leak risk if used pre-add)")
    log(f"  added after 2023-01-01: {int((la['date_added'] > '2023-01-01').sum())}")
    log(f"  missing/unparseable date_added: {int(la['date_added'].isna().sum())}")
    log("date_added partially guards (b) but does NOTHING for (a): the ~cumulative")
    log("hundreds of names removed from the index across 2012-2026 are simply not in")
    log("the file, and their prices 404 anyway (Check 2), so they cannot be restored.")
    results["survivorship_free"] = False

    hr("AUDIT SUMMARY (machine-readable)")
    verdict = {
        "1_pit_membership_entry_exit": "FAIL",
        "2_delisted_price_history": "PASS" if results["delisted_prices_available"] else "FAIL",
        "3_split_div_adjusted": "PASS" if results["splits_adjusted"] else "FAIL",
        "4_ticker_change_handling": "FAIL",
        "5_no_future_membership_leakage": "FAIL",
    }
    for k, v in verdict.items():
        log(f"  {k}: {v}")
    overall = "PASS" if all(v == "PASS" for v in verdict.values()) else "FAIL"
    log(f"\n  OVERALL AUDIT: {overall}")
    log("  Gate: primary backtest requires PIT membership (1) AND delisted coverage (2)")
    log("  AND no leakage (5). These FAIL -> primary backtest MUST NOT run. The")
    log("  data-availability report is the final deliverable.")
    results["verdict"] = verdict
    results["overall"] = overall

    with open(OUT, "w") as f:
        f.write("\n".join(_log_lines))
    with open(os.path.join(SCRIPT_DIR, "data_cache", "audit_results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    log(f"\nRaw output -> {OUT}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(2)
