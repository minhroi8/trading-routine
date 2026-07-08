"""
Episodic-pivot (earnings-gap continuation) backtest engine — RESEARCH ONLY.

Separate from PEAD and from the live 7-routine system. Nothing here trades, edits
memory files, or ships to production.

SURVIVORSHIP FRAMING (see report): this uses the SAME earnings-event universe and
price source as the existing PEAD baseline — the committed PEAD base trade CSVs
(ticker, earn_date, surprise_pct, sector) for the catalyst set, and the Yahoo
chart API (adjusted OHLCV) for prices, the same source
backtest_risk_sweep_entry_stop.py uses. It therefore inherits PEAD's known
survivorship limitation documented in backtesting/momentum_data_audit_2026-07-08.md.
This can answer "on the same imperfect dataset, does episodic pivot improve
expectancy or diversify PEAD?" It cannot answer "what would episodic pivot really
have produced across the true historical S&P 500?".

Data lineage note: yfinance's curl_cffi backend fails this environment's HTTPS
proxy, so prices are fetched with plain `requests` against the Yahoo chart API v8.
A live control ticker is fetched before trusting any empty result.
"""
import os, sys, io, time, pickle, math, json
import numpy as np
import pandas as pd
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
CACHE_DIR = os.path.join(SCRIPT_DIR, "data_cache")
REPORTS_DIR = os.path.join(SCRIPT_DIR, "reports")
PEAD_REPORTS = os.path.join(REPO_ROOT, "backtesting", "reports")
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

FETCH_START = "2021-06-01"     # deep enough for 20d lookback into early 2022
FETCH_END = "2026-07-08"       # resolve exits/time-stops on late-2025 entries

# ─── PRICE FETCH (requests + Yahoo chart API, disk-cached) ─────────────────────
def _fetch_chart(sym, p1=FETCH_START, p2=FETCH_END):
    sym = sym.replace(".", "-")
    P1 = int(pd.Timestamp(p1).timestamp()); P2 = int(pd.Timestamp(p2).timestamp())
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        url = (f"https://{host}/v8/finance/chart/{sym}"
               f"?period1={P1}&period2={P2}&interval=1d&events=div%2Csplits")
        for attempt in range(4):
            try:
                r = requests.get(url, timeout=30, headers={"User-Agent": UA})
                if r.status_code == 429:
                    time.sleep(3 * (attempt + 1)); continue
                if r.status_code != 200:
                    break
                res = r.json()["chart"]["result"][0]
                ts = res.get("timestamp")
                if not ts:
                    return None
                q = res["indicators"]["quote"][0]
                adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
                idx = (pd.to_datetime(ts, unit="s", utc=True)
                       .tz_convert("America/New_York").normalize().tz_localize(None))
                df = pd.DataFrame({"Open": q["open"], "High": q["high"], "Low": q["low"],
                                   "Close": q["close"], "Volume": q["volume"]}, index=idx)
                # Adjust O/H/L/C by the split+dividend factor so returns & gaps are
                # on one consistent adjusted basis (adjacent-day gap distortion from
                # a dividend ex-date is negligible vs a >=5% earnings gap).
                if adj is not None:
                    a = pd.Series(adj, index=idx)
                    factor = a / df["Close"]
                    for c in ("Open", "High", "Low"):
                        df[c] = df[c] * factor
                    df["Close"] = a
                df = df[~df.index.duplicated(keep="last")].sort_index()
                df = df.dropna(subset=["Open", "High", "Low", "Close"])
                return df if len(df) > 60 else None
            except Exception:
                time.sleep(2 * (attempt + 1))
    return None


def cached_history(ticker):
    path = os.path.join(CACHE_DIR, ticker.replace("/", "_") + ".pkl")
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    h = _fetch_chart(ticker)
    if h is not None:
        with open(path, "wb") as f:
            pickle.dump(h, f)
    time.sleep(0.2)
    return h


# ─── EVENT UNIVERSE (committed PEAD base artifacts = shared catalyst set) ───────
def load_events():
    """Union of PEAD base trade CSVs -> earnings-event catalyst set.
    Columns kept: ticker, earn_date, surprise_pct, sector, year.
    These are EPS-beat events (PEAD base gate = reported>estimate), the same
    catalyst universe PEAD operates on."""
    frames = []
    for f in ("backtest_trades_PEAD_2022_2024.csv",
              "backtest_trades_PEAD_2025_OOS.csv"):
        d = pd.read_csv(os.path.join(PEAD_REPORTS, f))
        d = d[["ticker", "sector", "earn_date", "surprise_pct"]].copy()
        frames.append(d)
    ev = pd.concat(frames, ignore_index=True)
    ev["earn_date"] = pd.to_datetime(ev["earn_date"]).dt.normalize()
    ev["surprise_pct"] = pd.to_numeric(ev["surprise_pct"], errors="coerce")
    ev["ticker"] = ev["ticker"].str.replace(".", "-", regex=False)
    ev = ev.dropna(subset=["earn_date"]).drop_duplicates(["ticker", "earn_date"])
    ev["year"] = ev["earn_date"].dt.year
    return ev.sort_values(["earn_date", "ticker"]).reset_index(drop=True)


def load_pead_trades():
    """PEAD realized trades re-pulled from artifacts (NOT re-simulated)."""
    frames = []
    for f in ("backtest_trades_PEAD_2022_2024.csv", "backtest_trades_PEAD_2025_OOS.csv"):
        d = pd.read_csv(os.path.join(PEAD_REPORTS, f))
        keep = ["ticker", "sector", "earn_date", "entry_date", "exit_date",
                "return_pct", "return_dollar", "holding_days", "surprise_pct"]
        d = d[[c for c in keep if c in d.columns]].copy()
        frames.append(d)
    t = pd.concat(frames, ignore_index=True)
    for c in ("earn_date", "entry_date", "exit_date"):
        t[c] = pd.to_datetime(t[c]).dt.normalize()
    t["ticker"] = t["ticker"].str.replace(".", "-", regex=False)
    t["return_pct"] = pd.to_numeric(t["return_pct"], errors="coerce")
    t["year"] = t["earn_date"].dt.year
    return t


# ─── SIGNAL: locate announcement bar, compute gap/vol/range features ───────────
def ann_bar_index(hist_index, earn_date):
    """First trading session on/after earn_date = the announcement/reaction bar."""
    after = hist_index[hist_index >= pd.Timestamp(earn_date).normalize()]
    return after[0] if len(after) else None


def compute_features(hist, earn_date, vol_window=20):
    """Return dict of announcement-bar features, or None if insufficient history.
    Uses ONLY data up to & including the announcement bar (no look-ahead)."""
    ann = ann_bar_index(hist.index, earn_date)
    if ann is None:
        return None
    prior = hist[hist.index < ann]
    if len(prior) < vol_window:
        return None
    pos = hist.index.get_loc(ann)
    if isinstance(pos, slice):
        pos = pos.start
    if pos < 1:
        return None
    row = hist.iloc[pos]
    prev_close = hist.iloc[pos - 1]["Close"]
    o, h, l, c, v = row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]
    if any(pd.isna(x) for x in (o, h, l, c, prev_close)) or prev_close <= 0 or h <= l:
        return None
    prior20 = prior.tail(vol_window)
    avg_vol = prior20["Volume"].mean()
    prior20_high = prior20["High"].max()
    gap = o / prev_close - 1.0
    ann_ret = c / prev_close - 1.0
    range_pos = (c - l) / (h - l)
    vol_ratio = (v / avg_vol) if avg_vol and avg_vol > 0 else np.nan
    return {
        "ann_date": ann, "ann_open": o, "ann_high": h, "ann_low": l,
        "ann_close": c, "prev_close": prev_close, "gap": gap, "ann_ret": ann_ret,
        "range_pos": range_pos, "vol_ratio": vol_ratio, "prior20_high": prior20_high,
        "ann_pos": pos,
    }


# ─── ENTRY: EP-A (next open) / EP-B (breakout within 5 sessions) ───────────────
def decide_entry(hist, feat, mode, breakout_window=5):
    """Return (entry_date, entry_fill_raw) or (None, None) if no entry."""
    pos = feat["ann_pos"]
    if mode == "next_open":
        if pos + 1 >= len(hist):
            return None, None
        d = hist.index[pos + 1]
        return d, float(hist.iloc[pos + 1]["Open"])
    elif mode == "breakout":
        trig = feat["ann_high"]
        for k in range(1, breakout_window + 1):
            if pos + k >= len(hist):
                break
            bar = hist.iloc[pos + k]
            if bar["High"] >= trig:
                fill = max(float(bar["Open"]), trig)   # stop-entry fill
                return hist.index[pos + k], fill
        return None, None
    raise ValueError(mode)


# ─── EXIT: parametric, supports isolated rules and combined earliest-trigger ────
def simulate_exit(hist, entry_date, entry_price, stop_price, next_earn,
                  rules, time_stop_sessions=20, trail_trigger=0.10,
                  trail_pct=0.07, hard_stop=-0.08):
    """Walk sessions from entry_date; return exit dict. `rules` is a set drawn from
    {'struct','hard','time','trail','earn'}. Earliest trigger wins."""
    entry_date = pd.Timestamp(entry_date).normalize()
    fut = hist[hist.index >= entry_date]
    if fut.empty:
        return None
    highest_close = entry_price
    trail_active = False
    hard_price = entry_price * (1 + hard_stop)
    for i, (dt, r) in enumerate(fut.iterrows()):
        close = r["Close"]
        low = r["Low"]
        if pd.isna(close):
            continue
        if close > highest_close:
            highest_close = close
        if highest_close >= entry_price * (1 + trail_trigger):
            trail_active = True
        # 'earn': exit at the close of the last session strictly before next_earn
        if "earn" in rules and next_earn is not None and dt < pd.Timestamp(next_earn):
            nxt = i + 1
            if nxt >= len(fut) or fut.index[nxt] >= pd.Timestamp(next_earn):
                return _exit(dt, close, "before_earn", i, entry_price)
        # intrabar stops evaluated on the low (stop is a resting order)
        if "struct" in rules and stop_price is not None and low <= stop_price:
            fill = min(float(r["Open"]), stop_price) if r["Open"] < stop_price else stop_price
            return _exit(dt, fill, "struct_stop", i, entry_price)
        if "hard" in rules and low <= hard_price:
            fill = min(float(r["Open"]), hard_price) if r["Open"] < hard_price else hard_price
            return _exit(dt, fill, "hard_stop", i, entry_price)
        if "trail" in rules and trail_active:
            tstop = highest_close * (1 - trail_pct)
            if close <= tstop:
                return _exit(dt, close, "trail_stop", i, entry_price)
        if "time" in rules and i >= time_stop_sessions:
            return _exit(dt, close, "time_stop", i, entry_price)
    last = fut.iloc[-1]
    return _exit(last.name, last["Close"], "data_end", len(fut) - 1, entry_price)


def _exit(dt, price, reason, sessions, entry_price):
    return {"exit_date": pd.Timestamp(dt).normalize(), "exit_price": float(price),
            "exit_reason": reason, "holding_sessions": int(sessions),
            "raw_return": float(price) / entry_price - 1.0}


# ─── FILTER STACKS ─────────────────────────────────────────────────────────────
def passes_ep(feat, surprise, gap_min, vol_min):
    """Full episodic-pivot setup filters."""
    if feat is None or pd.isna(feat["vol_ratio"]):
        return False
    return (surprise is not None and surprise >= 15.0
            and feat["gap"] >= gap_min
            and feat["ann_open"] > feat["prior20_high"]
            and feat["vol_ratio"] >= vol_min
            and feat["range_pos"] >= 0.75
            and feat["ann_ret"] >= 0.04)


def passes_simple_gap(feat, surprise, gap_min=0.05, vol_min=2.0):
    """Naive baseline: gap + volume only, no other conditions."""
    if feat is None or pd.isna(feat["vol_ratio"]):
        return False
    return feat["gap"] >= gap_min and feat["vol_ratio"] >= vol_min


# ─── SIGNAL BUILDER ────────────────────────────────────────────────────────────
def build_signals(ev, hist_cache, kind, gap_min, vol_min, entry_mode,
                  breakout_window=5, max_stop=0.08):
    """For each event, compute features, apply the filter stack, decide entry, and
    define the structural stop. Returns list of signal dicts. `kind` in {'ep','simple'}.
    Records per-stage denominators in the returned stats dict."""
    # next-earnings map (for the before-earn exit) from the same event set
    nxt = {}
    for tk, grp in ev.groupby("ticker"):
        ds = sorted(grp["earn_date"].tolist())
        nxt[tk] = ds
    sigs = []
    stats = {"events": 0, "have_hist": 0, "have_feat": 0, "passed_filter": 0,
             "entered": 0, "stop_ok": 0, "price_ok": 0}
    for _, e in ev.iterrows():
        stats["events"] += 1
        tk = e["ticker"]
        hist = hist_cache.get(tk)
        if hist is None:
            continue
        stats["have_hist"] += 1
        feat = compute_features(hist, e["earn_date"])
        if feat is None:
            continue
        stats["have_feat"] += 1
        if kind == "ep":
            ok = passes_ep(feat, e["surprise_pct"], gap_min, vol_min)
        else:
            ok = passes_simple_gap(feat, e["surprise_pct"], gap_min, vol_min)
        if not ok:
            continue
        stats["passed_filter"] += 1
        entry_date, entry_fill = decide_entry(hist, feat, entry_mode, breakout_window)
        if entry_date is None:
            continue
        stats["entered"] += 1
        if entry_fill is None or entry_fill < MIN_PRICE:
            continue
        stats["price_ok"] += 1
        stop_price = feat["ann_low"]
        if (entry_fill - stop_price) / entry_fill > max_stop:
            continue                    # structural stop wider than 8% -> skip
        stats["stop_ok"] += 1
        ds = nxt.get(tk, [])
        future_earn = [d for d in ds if d > e["earn_date"]]
        next_earn = min(future_earn) if future_earn else None
        sigs.append({
            "ticker": tk, "sector": e["sector"], "earn_date": e["earn_date"],
            "surprise_pct": e["surprise_pct"], "entry_date": entry_date,
            "entry_fill_raw": float(entry_fill), "stop_price": float(stop_price),
            "next_earn": next_earn, "gap": feat["gap"], "vol_ratio": feat["vol_ratio"],
            "range_pos": feat["range_pos"], "ann_ret": feat["ann_ret"],
            "year": int(pd.Timestamp(entry_date).year),
        })
    return sigs, stats


MIN_PRICE = 10.0


def attach_exits(sigs, hist_cache, rules, time_stop_sessions=20, trail_pct=0.07):
    """Compute each signal's exit (portfolio-independent: exits are price/time-based)."""
    out = []
    for s in sigs:
        hist = hist_cache[s["ticker"]]
        ex = simulate_exit(hist, s["entry_date"], s["entry_fill_raw"], s["stop_price"],
                           s["next_earn"], rules, time_stop_sessions, trail_pct=trail_pct)
        if ex is None:
            continue
        s2 = dict(s); s2.update(ex); out.append(s2)
    return out


# ─── PORTFOLIO SIMULATOR (daily, cash + sector caps, slippage, reconciled) ─────
def simulate_portfolio(sigs_with_exits, hist_cache, start_equity=100_000.0,
                       pos_frac=0.05, sector_cap=0.30, slippage=0.0010,
                       priority="gap"):
    """Event-driven daily portfolio sim. One open position per ticker. Returns
    (trades_df, equity_df, recon_ok, missed)."""
    if not sigs_with_exits:
        return pd.DataFrame(), pd.DataFrame(), True, {}
    spy = hist_cache["SPY"]
    entry_dates = [pd.Timestamp(s["entry_date"]) for s in sigs_with_exits]
    exit_dates = [pd.Timestamp(s["exit_date"]) for s in sigs_with_exits]
    cal = spy.index[(spy.index >= min(entry_dates)) & (spy.index <= max(exit_dates))]
    cal = cal.sort_values()
    # close panel for MTM (ffill within calendar)
    tickers = sorted({s["ticker"] for s in sigs_with_exits})
    closes = {t: hist_cache[t]["Close"].reindex(cal).ffill() for t in tickers}
    # index signals by entry date; priority order within a day
    by_day = {}
    for s in sigs_with_exits:
        by_day.setdefault(pd.Timestamp(s["entry_date"]), []).append(s)
    for d in by_day:
        by_day[d].sort(key=lambda x: -x.get(priority, 0))

    cash = start_equity
    open_pos = {}          # ticker -> dict(shares, buy_price, sell_price, exit_date, sector, cost)
    trades = []
    missed = {"already_open": 0, "cash": 0, "sector": 0, "zero_shares": 0}
    equity_rows = []
    prev_mtm = 0.0

    for d in cal:
        equity_open = cash + prev_mtm      # equity available to size new entries
        # ENTRIES at open
        for s in by_day.get(d, []):
            tk = s["ticker"]
            if tk in open_pos:
                missed["already_open"] += 1; continue
            notional = pos_frac * equity_open
            buy_price = s["entry_fill_raw"] * (1 + slippage)
            if cash < notional:
                missed["cash"] += 1; continue
            sec_cost = sum(p["cost"] for p in open_pos.values() if p["sector"] == s["sector"])
            if sec_cost + notional > sector_cap * equity_open:
                missed["sector"] += 1; continue
            shares = math.floor(notional / buy_price)
            if shares <= 0:
                missed["zero_shares"] += 1; continue
            cost = shares * buy_price
            cash -= cost
            open_pos[tk] = {
                "shares": shares, "buy_price": buy_price,
                "sell_price": s["exit_price"] * (1 - slippage),
                "exit_date": pd.Timestamp(s["exit_date"]), "sector": s["sector"],
                "cost": cost, "sig": s,
            }
        # EXITS at (their) exit_date == d
        for tk in [t for t, p in open_pos.items() if p["exit_date"] == d]:
            p = open_pos.pop(tk)
            proceeds = p["shares"] * p["sell_price"]
            cash += proceeds
            s = p["sig"]
            gross_ret = p["sell_price"] / p["buy_price"] - 1.0
            trades.append({
                "ticker": tk, "sector": p["sector"], "earn_date": s["earn_date"],
                "entry_date": s["entry_date"], "exit_date": d,
                "buy_price": p["buy_price"], "sell_price": p["sell_price"],
                "shares": p["shares"], "cost": p["cost"], "proceeds": proceeds,
                "pnl": proceeds - p["cost"], "net_return": gross_ret,
                "exit_reason": s["exit_reason"], "holding_sessions": s["holding_sessions"],
                "gap": s["gap"], "surprise_pct": s["surprise_pct"], "year": s["year"],
                "slip_cost": p["shares"] * (s["entry_fill_raw"] * slippage
                                            + s["exit_price"] * slippage),
            })
        # MARK-TO-MARKET at close
        mtm = sum(p["shares"] * closes[t].get(d, np.nan) for t, p in open_pos.items())
        mtm = float(np.nan_to_num(mtm))
        prev_mtm = mtm
        equity = cash + mtm
        equity_rows.append({"date": d, "cash": cash, "mtm": mtm, "equity": equity,
                            "n_pos": len(open_pos),
                            "invested_frac": (mtm / equity) if equity > 0 else 0.0})

    # close any still-open at last close (data_end safety)
    last = cal[-1]
    for tk, p in list(open_pos.items()):
        px = float(closes[tk].get(last, p["buy_price"]))
        cash += p["shares"] * px
        open_pos.pop(tk)

    trades_df = pd.DataFrame(trades)
    equity_df = pd.DataFrame(equity_rows).set_index("date")
    recon_ok = _reconcile(trades_df, equity_df, start_equity, cash)
    return trades_df, equity_df, recon_ok, missed


def _reconcile(trades_df, equity_df, start_equity, final_cash):
    """Daily identity equity==cash+mtm already holds by construction; here we check
    the aggregate: sum of trade PnL == final equity change (all positions closed)."""
    if trades_df.empty:
        return True
    total_pnl = trades_df["pnl"].sum()
    end_equity = equity_df["equity"].iloc[-1]
    # after force-closing leftovers final_cash reflects everything; compare to start+pnl
    return abs((start_equity + total_pnl) - final_cash) < 1.0


# ─── METRICS ────────────────────────────────────────────────────────────────────
def metrics(trades_df, equity_df, period_label, missed=None):
    if trades_df is None or trades_df.empty or equity_df is None or equity_df.empty:
        return {"period": period_label, "n_trades": 0, "note": "no trades"}
    r = trades_df["net_return"].values
    pnl = trades_df["pnl"].values
    wins = pnl[pnl > 0]; losses = pnl[pnl < 0]
    eq = equity_df["equity"]
    days = (eq.index[-1] - eq.index[0]).days or 1
    cagr = (eq.iloc[-1] / eq.iloc[0]) ** (365.0 / days) - 1.0
    roll_max = eq.cummax()
    mdd = ((eq - roll_max) / roll_max).min()
    dret = eq.pct_change().dropna()
    sharpe = (dret.mean() / dret.std() * math.sqrt(252)) if dret.std() > 0 else float("nan")
    total_profit = wins.sum()
    prof_factor = (wins.sum() / abs(losses.sum())) if losses.sum() != 0 else float("inf")
    top1 = np.sort(pnl)[::-1][:1].sum()
    top5 = np.sort(pnl)[::-1][:5].sum()
    turnover = trades_df["cost"].sum() / eq.mean() / (days / 365.0)
    return {
        "period": period_label,
        "n_trades": int(len(trades_df)),
        "total_return_pct": float(eq.iloc[-1] / eq.iloc[0] - 1) * 100,
        "cagr_pct": float(cagr) * 100,
        "max_drawdown_pct": float(mdd) * 100,
        "sharpe": float(sharpe),
        "win_rate_pct": float((r > 0).mean()) * 100,
        "n_wins": int((r > 0).sum()), "n_losses": int((r < 0).sum()),
        "expectancy_pct": float(np.mean(r)) * 100,
        "median_return_pct": float(np.median(r)) * 100,
        "profit_factor": float(prof_factor),
        "avg_hold_sessions": float(trades_df["holding_sessions"].mean()),
        "avg_invested_frac_pct": float(equity_df["invested_frac"].mean()) * 100,
        "pct_days_invested": float((equity_df["n_pos"] > 0).mean()) * 100,
        "turnover_annual_x": float(turnover),
        "slippage_cost_$": float(trades_df["slip_cost"].sum()),
        "largest_winner_contrib_pct": float(top1 / total_profit) * 100 if total_profit > 0 else float("nan"),
        "top5_winner_contrib_pct": float(top5 / total_profit) * 100 if total_profit > 0 else float("nan"),
        "expectancy_ex_top1_pct": float(np.mean(np.sort(r)[::-1][1:])) * 100 if len(r) > 1 else float("nan"),
        "expectancy_ex_top5_pct": float(np.mean(np.sort(r)[::-1][5:])) * 100 if len(r) > 5 else float("nan"),
        "missed_signals": missed or {},
    }


if __name__ == "__main__":
    # transport control
    ctrl = cached_history("AAPL")
    print("AAPL control:", None if ctrl is None else
          f"{len(ctrl)} rows [{ctrl.index.min().date()}..{ctrl.index.max().date()}]")
    ev = load_events()
    print("events:", len(ev), "tickers:", ev.ticker.nunique(),
          "years:", sorted(ev.year.unique()))
