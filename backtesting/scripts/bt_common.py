"""Shared utilities for the insider-cluster / congressional-cluster
backtests (Signal B / Signal A). Research-only -- no order placement,
no brokerage account access; Alpaca is used strictly as a read-only
historical market-data source (paper account market-data endpoint).
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pandas_market_calendars as mcal
import requests

DATA_CACHE = Path(__file__).resolve().parent.parent / "data_cache"
DATA_CACHE.mkdir(parents=True, exist_ok=True)

ALPACA_DATA_URL = "https://data.alpaca.markets/v2/stocks"
SEC_UA = "trading-routine-research contact: minhroi0708@gmail.com"

# ---------------------------------------------------------------------------
# Trading calendar
# ---------------------------------------------------------------------------
_nyse = mcal.get_calendar("NYSE")
_schedule = _nyse.schedule(start_date="2010-01-01", end_date="2025-12-31")
TRADING_DAYS = pd.DatetimeIndex(_schedule.index.normalize().unique()).sort_values()


def next_trading_day(date) -> pd.Timestamp:
    """First trading day strictly after `date`."""
    date = pd.Timestamp(date).normalize()
    idx = TRADING_DAYS.searchsorted(date, side="right")
    if idx >= len(TRADING_DAYS):
        return pd.NaT
    return TRADING_DAYS[idx]


def on_or_after_trading_day(date) -> pd.Timestamp:
    """`date` itself if it's a trading day, else the next one."""
    date = pd.Timestamp(date).normalize()
    idx = TRADING_DAYS.searchsorted(date, side="left")
    if idx >= len(TRADING_DAYS):
        return pd.NaT
    return TRADING_DAYS[idx]


def trading_day_index(date) -> int:
    """Integer position of `date` (or the next trading day) in the
    trading calendar -- lets us measure "N trading days apart" as a
    plain integer difference."""
    d = on_or_after_trading_day(date)
    if pd.isna(d):
        return None
    return int(TRADING_DAYS.searchsorted(d))


def add_trading_days(date, n: int) -> pd.Timestamp:
    i = trading_day_index(date)
    if i is None:
        return pd.NaT
    j = i + n
    if j < 0 or j >= len(TRADING_DAYS):
        return pd.NaT
    return TRADING_DAYS[j]


# ---------------------------------------------------------------------------
# Alpaca historical daily bars (read-only market data; no orders, no
# brokerage-account calls of any kind)
# ---------------------------------------------------------------------------
def get_daily_bars(symbol: str, start: str, end: str, api_key: str, api_secret: str,
                    cache_dir: Path = None) -> pd.DataFrame:
    cache_dir = cache_dir or (DATA_CACHE / "alpaca_bars")
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{symbol}.parquet"
    if cache_file.exists():
        df = pd.read_parquet(cache_file)
    else:
        df = pd.DataFrame()

    have_range = False
    if not df.empty:
        have_range = df.index.min() <= pd.Timestamp(start, tz="UTC") + pd.Timedelta(days=5) and \
                     df.index.max() >= pd.Timestamp(end, tz="UTC") - pd.Timedelta(days=5)
    if have_range:
        return df.loc[start:end]

    headers = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": api_secret}
    all_bars = []
    page_token = None
    url = f"{ALPACA_DATA_URL}/{symbol}/bars"
    for attempt in range(5):
        try:
            while True:
                # fetch a broad, fixed range (independent of the caller's
                # start/end) so the per-symbol cache file is reusable across
                # both signals regardless of which window asked for it first
                params = {"timeframe": "1Day", "start": "2013-01-01", "end": "2025-01-05",
                          "limit": 10000}
                if page_token:
                    params["page_token"] = page_token
                resp = requests.get(url, headers=headers, params=params, timeout=30)
                if resp.status_code == 429:
                    time.sleep(3)
                    continue
                resp.raise_for_status()
                data = resp.json()
                bars = data.get("bars") or []
                all_bars.extend(bars)
                page_token = data.get("next_page_token")
                if not page_token:
                    break
            break
        except Exception as e:
            if attempt == 4:
                print(f"  WARN: failed to fetch bars for {symbol}: {e}")
                return pd.DataFrame()
            time.sleep(2 * (attempt + 1))

    if not all_bars:
        empty = pd.DataFrame(columns=["open", "high", "low", "close", "volume"])
        empty.to_parquet(cache_file)
        return empty

    bdf = pd.DataFrame(all_bars)
    bdf["t"] = pd.to_datetime(bdf["t"])
    bdf = bdf.set_index("t").sort_index()
    bdf = bdf.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume"})
    bdf = bdf[["open", "high", "low", "close", "volume"]]
    bdf.to_parquet(cache_file)
    return bdf.loc[start:end]


def price_on_or_after(bars: pd.DataFrame, date, field="close", max_lookahead_days=5):
    """Close price on `date`, or the next available trading day within
    max_lookahead_days (handles the odd missing bar)."""
    if bars.empty:
        return None, None
    date = pd.Timestamp(date, tz="UTC").normalize()
    window = bars.loc[date: date + pd.Timedelta(days=max_lookahead_days)]
    if window.empty:
        return None, None
    return float(window.iloc[0][field]), window.index[0]


def price_on_or_before(bars: pd.DataFrame, date, field="close", max_lookback_days=5):
    if bars.empty:
        return None, None
    date = pd.Timestamp(date, tz="UTC").normalize()
    window = bars.loc[date - pd.Timedelta(days=max_lookback_days): date]
    if window.empty:
        return None, None
    return float(window.iloc[-1][field]), window.index[-1]


# ---------------------------------------------------------------------------
# SEC EDGAR: point-in-time shares outstanding (market-cap proxy) and 8-K
# filing dates (earnings-proximity proxy), both no-lookahead by
# construction (we only ever use values whose own filing/report date
# precedes the decision date).
# ---------------------------------------------------------------------------
def _sec_get(url, cache_file: Path, timeout=30):
    if cache_file.exists():
        return cache_file.read_bytes()
    for attempt in range(4):
        try:
            r = requests.get(url, headers={"User-Agent": SEC_UA}, timeout=timeout)
            if r.status_code == 200:
                cache_file.write_bytes(r.content)
                return r.content
            elif r.status_code == 404:
                cache_file.write_bytes(b"")
                return b""
            else:
                time.sleep(1 + attempt)
        except Exception:
            time.sleep(1 + attempt)
    return b""


def get_shares_outstanding_series(cik: int) -> pd.DataFrame:
    """Return a DataFrame of (filed_date, shares_outstanding) reported via
    dei:EntityCommonStockSharesOutstanding across the company's XBRL
    filings. `filed_date` is when that figure became public."""
    cache_dir = DATA_CACHE / "sec_companyfacts"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"CIK{cik:010d}.json"
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    content = _sec_get(url, cache_file)
    if not content:
        return pd.DataFrame(columns=["filed", "shares"])
    import json
    try:
        data = json.loads(content)
    except Exception:
        return pd.DataFrame(columns=["filed", "shares"])
    facts = data.get("facts", {}).get("dei", {}).get("EntityCommonStockSharesOutstanding")
    if not facts:
        return pd.DataFrame(columns=["filed", "shares"])
    rows = []
    for unit_vals in facts.get("units", {}).values():
        for v in unit_vals:
            rows.append({"filed": v.get("filed"), "shares": v.get("val")})
    if not rows:
        return pd.DataFrame(columns=["filed", "shares"])
    df = pd.DataFrame(rows)
    df["filed"] = pd.to_datetime(df["filed"])
    df = df.dropna().sort_values("filed")
    return df


def shares_outstanding_as_of(shares_df: pd.DataFrame, date) -> float:
    date = pd.Timestamp(date)
    prior = shares_df[shares_df.filed <= date]
    if prior.empty:
        return None
    return float(prior.iloc[-1].shares)


def get_8k_filing_dates(cik: int) -> pd.DatetimeIndex:
    """All 8-K filing dates for a CIK -- used as an earnings-proximity
    proxy (many but not all 8-Ks are earnings releases; documented as an
    approximation in the report, since a free, point-in-time, no-lookahead
    earnings-calendar source was not otherwise available)."""
    cache_dir = DATA_CACHE / "sec_submissions"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"CIK{cik:010d}.json"
    url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
    content = _sec_get(url, cache_file)
    if not content:
        return pd.DatetimeIndex([])
    import json
    try:
        data = json.loads(content)
    except Exception:
        return pd.DatetimeIndex([])
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    out = [d for f, d in zip(forms, dates) if f == "8-K"]
    if not out:
        return pd.DatetimeIndex([])
    return pd.DatetimeIndex(pd.to_datetime(out))


def near_earnings_proxy(filing_8k_dates: pd.DatetimeIndex, date, window_trading_days=2) -> bool:
    if filing_8k_dates is None or len(filing_8k_dates) == 0:
        return False
    date = pd.Timestamp(date)
    for d in filing_8k_dates:
        # trading-day distance via calendar index difference
        i1, i2 = trading_day_index(date), trading_day_index(d)
        if i1 is not None and i2 is not None and abs(i1 - i2) <= window_trading_days:
            return True
    return False


# ---------------------------------------------------------------------------
# Ticker -> CIK map (for Signal A, which only has tickers)
# ---------------------------------------------------------------------------
def get_ticker_to_cik_map() -> dict:
    cache_file = DATA_CACHE / "sec_company_tickers.json"
    content = _sec_get("https://www.sec.gov/files/company_tickers.json", cache_file)
    if not content:
        return {}
    import json
    data = json.loads(content)
    out = {}
    for v in data.values():
        out[v["ticker"].upper()] = int(v["cik_str"])
    return out


# ---------------------------------------------------------------------------
# Leveraged / inverse ETF + OTC filtering
# ---------------------------------------------------------------------------
LEVERAGED_INVERSE_KEYWORDS = [
    "ultra", "2x", "3x", "-1x", "1.5x", "inverse", "bear", "short",
    "leveraged", "daily target", "direxion", "3x shares",
]


def looks_leveraged_or_inverse(name) -> bool:
    if not isinstance(name, str) or not name:
        return False
    n = name.lower()
    return any(k in n for k in LEVERAGED_INVERSE_KEYWORDS)


def get_alpaca_asset(symbol: str, api_key: str, api_secret: str, cache_dir: Path = None) -> dict:
    cache_dir = cache_dir or (DATA_CACHE / "alpaca_assets")
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{symbol}.json"
    import json
    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass
    url = f"https://paper-api.alpaca.markets/v2/assets/{symbol}"
    headers = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": api_secret}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            d = r.json()
            cache_file.write_text(json.dumps(d))
            return d
        else:
            cache_file.write_text("{}")
            return {}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Performance stats
# ---------------------------------------------------------------------------
def trade_stats(trades: pd.DataFrame, ret_col="net_return"):
    if trades.empty:
        return {}
    wins = trades[trades[ret_col] > 0]
    losses = trades[trades[ret_col] <= 0]
    win_rate = len(wins) / len(trades)
    gross_profit = wins[ret_col].sum()
    gross_loss = -losses[ret_col].sum()
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else np.inf
    avg_ret = trades[ret_col].mean()
    return {
        "n_trades": len(trades),
        "win_rate": win_rate,
        "avg_return": avg_ret,
        "profit_factor": profit_factor,
        "gross_profit_sum": gross_profit,
        "gross_loss_sum": gross_loss,
    }


def equity_curve_from_trades(trades: pd.DataFrame, entry_col="entry_date", exit_col="exit_date",
                              ret_col="net_return", start_capital=100_000.0, n_concurrent=10):
    """Simple equal-weight equity curve: each trade risks 1/n_concurrent
    of capital at time of entry, compounding sequentially trade-by-trade
    ordered by exit date (a light-weight approximation, not a full
    intraday-accurate portfolio simulator)."""
    if trades.empty:
        return pd.Series(dtype=float)
    t = trades.sort_values(exit_col).copy()
    equity = start_capital
    curve = []
    for _, row in t.iterrows():
        stake = equity / n_concurrent
        equity = equity - stake + stake * (1 + row[ret_col])
        curve.append({"date": row[exit_col], "equity": equity})
    cdf = pd.DataFrame(curve).set_index("date")["equity"]
    return cdf


def cagr(equity: pd.Series, start_date, end_date) -> float:
    if equity.empty:
        return np.nan
    years = (pd.Timestamp(end_date) - pd.Timestamp(start_date)).days / 365.25
    if years <= 0:
        return np.nan
    total_return = equity.iloc[-1] / equity.iloc[0]
    return total_return ** (1 / years) - 1


def sharpe_from_trade_equity(equity: pd.Series, periods_per_year=252) -> float:
    if len(equity) < 3:
        return np.nan
    rets = equity.pct_change().dropna()
    if rets.std() == 0 or len(rets) == 0:
        return np.nan
    # equity here is indexed by trade-exit events, not daily -- annualize
    # using the actual observed trade cadence rather than assuming 252/yr
    span_years = (equity.index[-1] - equity.index[0]).days / 365.25
    if span_years <= 0:
        return np.nan
    trades_per_year = len(rets) / span_years
    return (rets.mean() / rets.std()) * np.sqrt(trades_per_year)


def max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return np.nan
    roll_max = equity.cummax()
    dd = equity / roll_max - 1
    return dd.min()


def buy_and_hold_stats(bars: pd.DataFrame, start_date, end_date):
    bars = bars.loc[pd.Timestamp(start_date, tz="UTC"):pd.Timestamp(end_date, tz="UTC")]
    if bars.empty or len(bars) < 2:
        return {}
    px = bars["close"]
    daily_ret = px.pct_change().dropna()
    years = (px.index[-1] - px.index[0]).days / 365.25
    total_return = px.iloc[-1] / px.iloc[0]
    c = total_return ** (1 / years) - 1 if years > 0 else np.nan
    sharpe = (daily_ret.mean() / daily_ret.std()) * np.sqrt(252) if daily_ret.std() > 0 else np.nan
    dd = max_drawdown(px)
    return {"CAGR": c, "Sharpe": sharpe, "MaxDD": dd, "total_return": total_return - 1,
            "start": px.index[0], "end": px.index[-1]}
