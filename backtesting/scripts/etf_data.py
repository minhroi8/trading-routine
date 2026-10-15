"""
ETF daily-bar loader + GATE 0 integrity checks for the ETF trend backtest.

Transport: the same requests + Yahoo v8 chart API approach used by the other
research scripts in this repo (browser User-Agent, query1 -> query2 fallback,
429 back-off). Raw responses are cached as pickles in backtesting/data_cache/
(gitignored).

Columns returned per ticker (index = NY trading date):
  Open, High, Low, Close  -- Yahoo "quote" fields: split-adjusted, NOT
                             dividend-adjusted ("raw" for fill purposes)
  AdjClose                -- split + dividend adjusted (total-return series)
  Div, Split              -- cash dividend per share / split ratio on ex-date
  Volume

GATE 0 distinguishes TRANSPORT failures (HTTP / parse errors) from DATA
findings (gaps, missing history, discontinuities). A transport error is never
reported as a data finding.
"""

import os
import pickle
import time

import numpy as np
import pandas as pd
import requests

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backtesting/
CACHE_DIR = os.path.join(HERE, "data_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

UNIVERSE = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "GLD",
            "XLK", "XLF", "XLE", "XLV", "XLY", "XLP", "XLI", "XLB", "XLU"]
FETCH_START = "2004-01-01"     # extra year of warm-up for SMA200 / 12-1 momentum
REQUIRED_START = "2005-01-03"

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


class TransportError(Exception):
    pass


def _fetch_chart(ticker, start=FETCH_START, end=None):
    p1 = int(pd.Timestamp(start).timestamp())
    p2 = int((pd.Timestamp(end) if end else pd.Timestamp.now("UTC").tz_localize(None)
              + pd.Timedelta(days=1)).timestamp())
    errors = []
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        url = (f"https://{host}/v8/finance/chart/{ticker}"
               f"?period1={p1}&period2={p2}&interval=1d&events=div%2Csplits")
        for attempt in range(4):
            try:
                r = requests.get(url, timeout=30, headers={"User-Agent": _UA})
            except Exception as e:  # network-level
                errors.append(f"{host}: {type(e).__name__}: {e}")
                time.sleep(2 * (attempt + 1))
                continue
            if r.status_code == 429:
                errors.append(f"{host}: HTTP 429")
                time.sleep(3 * (attempt + 1))
                continue
            if r.status_code != 200:
                errors.append(f"{host}: HTTP {r.status_code}")
                break
            try:
                return r.json()["chart"]["result"][0]
            except Exception as e:
                errors.append(f"{host}: parse error {type(e).__name__}: {e}")
                break
    raise TransportError(f"{ticker}: " + " | ".join(errors[-4:]))


def _to_frame(res):
    ts = res.get("timestamp") or []
    q = res["indicators"]["quote"][0]
    adj = res["indicators"]["adjclose"][0]["adjclose"]
    idx = (pd.to_datetime(ts, unit="s", utc=True)
           .tz_convert("America/New_York").normalize().tz_localize(None))
    df = pd.DataFrame({"Open": q["open"], "High": q["high"], "Low": q["low"],
                       "Close": q["close"], "Volume": q["volume"],
                       "AdjClose": adj}, index=idx)
    df = df[~df.index.duplicated(keep="last")].sort_index()
    df["Div"] = 0.0
    df["Split"] = 1.0
    ev = res.get("events", {}) or {}
    for d in (ev.get("dividends") or {}).values():
        day = (pd.Timestamp(d["date"], unit="s", tz="UTC")
               .tz_convert("America/New_York").normalize().tz_localize(None))
        if day in df.index:
            df.loc[day, "Div"] += float(d["amount"])
    for s in (ev.get("splits") or {}).values():
        day = (pd.Timestamp(s["date"], unit="s", tz="UTC")
               .tz_convert("America/New_York").normalize().tz_localize(None))
        if day in df.index:
            df.loc[day, "Split"] = float(s["numerator"]) / float(s["denominator"])
    return df


def load(ticker, refresh=False):
    """Return the daily frame for `ticker` (raises TransportError)."""
    path = os.path.join(CACHE_DIR, f"etf_{ticker}.pkl")
    if os.path.exists(path) and not refresh:
        with open(path, "rb") as f:
            res = pickle.load(f)
    else:
        res = _fetch_chart(ticker)
        with open(path, "wb") as f:
            pickle.dump(res, f)
    df = _to_frame(res)
    # drop a possibly-partial bar if run before today's 16:00 ET close
    now_ny = pd.Timestamp.now("America/New_York")
    today_ny = now_ny.normalize().tz_localize(None)
    if now_ny.hour < 16:
        df = df[df.index < today_ny]
    return df


def load_universe(refresh=False):
    return {t: load(t, refresh=refresh) for t in UNIVERSE}


# --------------------------------------------------------------------------
# GATE 0
# --------------------------------------------------------------------------
def gate0():
    """Return (passed: bool, report_lines: list[str], data: dict)."""
    lines, passed = [], True
    # 1. live control fetch (forces network, no cache)
    try:
        spy = load("SPY", refresh=True)
    except TransportError as e:
        return False, [f"TRANSPORT FAILURE fetching control ticker SPY: {e}",
                       "This is a transport error, not a data finding."], {}
    lines.append(f"- Control ticker SPY fetched live: {len(spy)} bars, "
                 f"{spy.index[0].date()} -> {spy.index[-1].date()}, "
                 f"last AdjClose {spy['AdjClose'].iloc[-1]:.2f}.")

    data = {"SPY": spy}
    transport_fail = []
    for t in UNIVERSE:
        if t == "SPY":
            continue
        try:
            data[t] = load(t, refresh=True)
        except TransportError as e:
            transport_fail.append(str(e))
    if transport_fail:
        lines.append("- TRANSPORT FAILURES (not data findings): " + "; ".join(transport_fail))
        return False, lines, data

    # 2. SPY total-return continuity across dividends.
    # On each ex-date, AdjClose return should equal (Close + Div)/prevClose - 1.
    d = spy.dropna(subset=["Close", "AdjClose"])
    r_adj = d["AdjClose"].pct_change()
    r_tr = (d["Close"] + d["Div"]) / d["Close"].shift(1) - 1
    exd = d.index[d["Div"] > 0]
    exd = exd[exd > d.index[0]]
    err = (r_adj - r_tr).loc[exd].abs()
    lines.append(f"- SPY dividends since {FETCH_START}: {len(exd)} ex-dates; "
                 f"max |AdjClose return - (Close+Div)/prevClose return| on ex-dates "
                 f"= {err.max()*1e4:.2f} bp (median {err.median()*1e4:.2f} bp).")
    if err.max() > 0.0010:
        passed = False
        lines.append("  **FAIL**: adjusted-close does not reflect dividends.")
    # dividend yield implied by the AdjClose/Close drift
    tr = d["AdjClose"].iloc[-1] / d["AdjClose"].iloc[0]
    pr = d["Close"].iloc[-1] / d["Close"].iloc[0]
    lines.append(f"- SPY total-return multiple {tr:.2f}x vs price-only {pr:.2f}x "
                 f"(difference = reinvested dividends).")

    # 3. Every ETF: start date, gaps, split continuity, extreme jumps.
    lines.append("")
    lines.append("| ETF | first bar | bars | max cal-day gap | splits in data | max |1d adj ret| (date) | non-dividend AdjClose/Close factor jumps |")
    lines.append("|---|---|---|---|---|---|---|")
    spy_idx = spy.index
    for t in UNIVERSE:
        df = data[t]
        first = df.index[0]
        ok_start = first <= pd.Timestamp(REQUIRED_START)
        has_0103 = pd.Timestamp(REQUIRED_START) in df.index
        sub = df.loc[REQUIRED_START:]
        nan_rows = int(sub[["Open", "Close", "AdjClose"]].isna().any(axis=1).sum())
        missing_vs_spy = len(spy_idx[spy_idx >= REQUIRED_START].difference(sub.index))
        gap = sub.index.to_series().diff().dt.days.max()
        ret = sub["AdjClose"].pct_change()
        mx = ret.abs().idxmax()
        # factor = AdjClose/Close should change only on dividend ex-dates
        fac = (sub["AdjClose"] / sub["Close"])
        fchg = (fac / fac.shift(1) - 1).abs()
        bad = fchg[(fchg > 1e-4) & (sub["Div"] == 0)]
        # split continuity: the split-adjusted Close must not jump on split dates
        spl = df[df["Split"] != 1.0]
        spl_txt = ", ".join(f"{i.date()} {v:g}:1" for i, v in spl["Split"].items()) or "none"
        spl_ok = True
        for i in spl.index:
            loc = df.index.get_loc(i)
            if loc > 0:
                jr = df["Close"].iloc[loc] / df["Close"].iloc[loc - 1] - 1
                if abs(jr) > 0.2:
                    spl_ok = False
        status = []
        if not (ok_start and has_0103):
            status.append("NO 2005-01-03 BAR")
        if nan_rows:
            status.append(f"{nan_rows} NaN rows")
        if missing_vs_spy:
            status.append(f"{missing_vs_spy} SPY dates missing")
        if not spl_ok:
            status.append("SPLIT DISCONTINUITY")
        if abs(ret.loc[mx]) > 0.25:
            status.append("JUMP>25%")
        if len(bad):
            status.append(f"{len(bad)} unexplained factor jumps")
        if status:
            passed = False
        lines.append(f"| {t} | {first.date()} | {len(sub)} | {int(gap)}d | {spl_txt} | "
                     f"{ret.loc[mx]*100:+.1f}% ({mx.date()}) | "
                     f"{len(bad)}{' — ' + '; '.join(status) if status else ''} |")
    return passed, lines, data


if __name__ == "__main__":
    ok, lines, _ = gate0()
    print("\n".join(lines))
    print("\nGATE 0:", "PASS" if ok else "FAIL")
