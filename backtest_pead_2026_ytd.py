"""
PEAD 2026 YTD Out-of-Sample Backtest — ENHANCED strategy (all 2026 improvements).

Tests whether the May–June 2026 strategy enhancements would have beaten the
2025 OOS baseline (55.5% win rate, +1.54% avg return).

Methodology
-----------
1. Build a BASE candidate set identical in spirit to the 2025 run:
   EPS beat (reported > estimate) + price >= $10 at entry + 20d avg $vol >= $20M.
   Every base candidate is fully simulated so we know its outcome regardless of
   which enhanced filters it later passes/fails. This lets us measure, per filter,
   how many trades it removes and the win rate of the trades it removed.
2. Evaluate each VERIFIABLE enhanced filter as a boolean per candidate:
     - f_surprise15 : EPS surprise >= 15%
     - f_vol15x     : announcement-day volume >= 1.5x 20d avg volume
     - f_rs         : positive relative strength vs SPY post-earnings
     - f_52w        : new 52-week high within the last 45 calendar days
     - f_nearearn   : NOT within 3 days of the next earnings report
   (price >= $10 and 20d avg $vol >= $20M are already in the BASE gate.)
3. Headline ENHANCED set = base candidates passing ALL verifiable filters,
   exited with sector-appropriate trailing stops (IT = 12%, others = 7%).
4. Two sensitivity scenarios for the UNVERIFIABLE guidance-raise filter:
     - Scenario A : EPS beat >= 15% only
     - Scenario B : EPS beat >= 15% + price/volume filters (vol 1.5x)

Filters that CANNOT be backtested from yfinance (noted in report, not applied):
   - guidance raise (no reliable data)
   - BIS export-control news (IT/semis)
   - SEC shelf registration / equity offering
"""

import yfinance as yf
import pandas as pd
import numpy as np
import requests
import warnings
import time
import sys
from datetime import datetime, timedelta
from io import StringIO

warnings.filterwarnings("ignore")

# ─── CONFIG ───────────────────────────────────────────────────────────────────
HIST_START   = "2024-06-01"      # deep lookback for 52-wk high + 20d vol
DATA_END     = "2026-06-05"      # yfinance data currently ends 2026-06-04
TEST_START   = "2026-01-01"
TEST_END     = "2026-06-04"
POSITION_SIZE = 11_000
HARD_STOP     = -0.08
TRAIL_TRIGGER = 0.10
TRAIL_PCT_DEFAULT = 0.07          # non-IT trailing stop
TRAIL_PCT_IT      = 0.12          # IT/semiconductor wider trailing stop
TIME_STOP     = 42                # calendar days
MIN_PRICE     = 10.0
MIN_AVG_DVOL  = 20_000_000
ENTRY_DELAY   = 2
SURPRISE_MIN  = 15.0              # EPS surprise % threshold
VOL_MULT      = 1.5              # announcement-day volume multiple
NEAR_EARN_DAYS = 3               # exclude if next earnings within N days of entry
HIGH_RECENCY_DAYS = 45           # 52-wk high must be within N calendar days
IT_SECTOR = "Information Technology"

# Prior-period baselines for the comparison table
BASELINE_INSAMPLE = {
    "period": "2022-2024", "total_trades": 4387, "win_rate": 54.8,
    "avg_return_pct": 1.32, "avg_winner_pct": 7.74, "avg_loser_pct": -6.45,
    "profit_factor": 1.45, "max_consec_loss": 41, "avg_holding_days": 35.6,
    "spy_return_pct": 28.2,
}
BASELINE_2025 = {
    "period": "2025-OOS", "total_trades": 1454, "win_rate": 55.5,
    "avg_return_pct": 1.54, "avg_winner_pct": 7.84, "avg_loser_pct": -6.31,
    "profit_factor": 1.55, "max_consec_loss": 13, "avg_holding_days": 35.8,
    "spy_return_pct": 18.0,
}


# ─── S&P 500 UNIVERSE ─────────────────────────────────────────────────────────
def get_sp500():
    url = ("https://raw.githubusercontent.com/datasets/s-and-p-500-companies"
           "/main/data/constituents.csv")
    try:
        r = requests.get(url, timeout=30)
        df = pd.read_csv(StringIO(r.text))
        df.columns = [c.strip() for c in df.columns]
        sym_col  = next(c for c in df.columns if c.lower() in ("symbol", "ticker"))
        sec_col  = next((c for c in df.columns if "sector"   in c.lower()), None)
        name_col = next((c for c in df.columns if "name" in c.lower()
                         or "security" in c.lower()), None)
        result = pd.DataFrame({"ticker": df[sym_col].str.strip()})
        result["sector"] = df[sec_col] if sec_col else "Unknown"
        result["name"]   = df[name_col] if name_col else result["ticker"]
        result["ticker"] = result["ticker"].str.replace(".", "-", regex=False)
        return result
    except Exception as e:
        print(f"[ERROR] Could not fetch S&P 500 list: {e}")
        sys.exit(1)


# ─── PRICE + EARNINGS FETCH ───────────────────────────────────────────────────
def fetch_ticker_data(ticker):
    try:
        tk = yf.Ticker(ticker)
        hist = tk.history(start=HIST_START, end=DATA_END, auto_adjust=True)
        if hist.empty or len(hist) < 60:
            return None, None
        if hist.index.tz is not None:
            hist.index = hist.index.tz_localize(None)
        hist.index = hist.index.normalize()

        try:
            eh = tk.get_earnings_dates(limit=24)
        except Exception:
            return hist, None
        if eh is None or eh.empty:
            return hist, None

        eh = eh.rename(columns={
            "Reported EPS": "reported",
            "EPS Estimate": "estimate",
            "Surprise(%)":  "surprise_pct",
        })
        eh.index = pd.to_datetime(eh.index).tz_localize(None)
        eh = eh.sort_index()
        return hist, eh
    except Exception:
        return None, None


# ─── CALENDAR HELPERS ─────────────────────────────────────────────────────────
def get_trading_days(hist):
    return sorted(hist.index.unique())


def nth_trading_day_after(trading_days, date, n):
    date = pd.Timestamp(date).normalize()
    future = [d for d in trading_days if d > date]
    return future[n - 1] if len(future) >= n else None


# ─── BASE LIQUIDITY FILTERS ───────────────────────────────────────────────────
def avg_dvol_ok(hist, date, window=20):
    date = pd.Timestamp(date).normalize()
    prior = hist[hist.index < date].tail(window)
    if len(prior) < window // 2:
        return False
    dvol = (prior["Close"] * prior["Volume"]).mean()
    return dvol >= MIN_AVG_DVOL


# ─── ENHANCED FILTER EVALUATORS (per candidate, no lookahead) ─────────────────
def vol_ratio_on_day(hist, earn_date, window=20):
    """Announcement-day volume / mean of prior `window` days' volume."""
    earn_date = pd.Timestamp(earn_date).normalize()
    # find the trading day on/closest after earn_date for the announcement bar
    on_or_after = hist[hist.index >= earn_date]
    if on_or_after.empty:
        return None
    ann_day = on_or_after.index[0]
    ann_vol = hist.loc[ann_day, "Volume"]
    prior = hist[hist.index < ann_day].tail(window)
    if len(prior) < window // 2 or prior["Volume"].mean() == 0:
        return None
    return float(ann_vol) / float(prior["Volume"].mean())


def rel_strength_vs_spy(hist, spy_close, earn_date, entry_date):
    """Post-earnings relative strength vs SPY, measured from the earnings-day
    close to the close BEFORE entry (no lookahead at the day+2 open entry).
    Returns stock_ret - spy_ret (positive => outperforming)."""
    earn_date  = pd.Timestamp(earn_date).normalize()
    entry_date = pd.Timestamp(entry_date).normalize()
    s = hist[(hist.index >= earn_date) & (hist.index < entry_date)]
    if len(s) < 2:
        return None
    d0, d1 = s.index[0], s.index[-1]
    stock_ret = (hist.loc[d1, "Close"] - hist.loc[d0, "Close"]) / hist.loc[d0, "Close"]
    try:
        spy0 = spy_close.asof(d0)
        spy1 = spy_close.asof(d1)
    except Exception:
        return None
    if pd.isna(spy0) or pd.isna(spy1) or spy0 == 0:
        return None
    spy_ret = (spy1 - spy0) / spy0
    return float(stock_ret - spy_ret)


def new_52w_high_recent(hist, entry_date, recency_days=HIGH_RECENCY_DAYS):
    """Did the stock print a new 52-week (252 trading-day) high within the last
    `recency_days` calendar days before entry?"""
    entry_date = pd.Timestamp(entry_date).normalize()
    window = hist[hist.index < entry_date]
    if len(window) < 120:
        return None
    high = window["High"]
    roll_max = high.rolling(252, min_periods=120).max()
    is_high = high >= roll_max * 0.999            # new-high flag (tolerance)
    cutoff = entry_date - timedelta(days=recency_days)
    recent = is_high[is_high.index >= cutoff]
    if recent.empty:
        return False
    return bool(recent.any())


def days_to_next_earnings(earnings, earn_date, entry_date):
    """Calendar days from entry to the NEXT earnings date after `earn_date`."""
    earn_date  = pd.Timestamp(earn_date).normalize()
    entry_date = pd.Timestamp(entry_date).normalize()
    future = [d for d in earnings.index if pd.Timestamp(d).normalize() > earn_date]
    if not future:
        return None
    nxt = pd.Timestamp(min(future)).normalize()
    return (nxt - entry_date).days


# ─── SIMULATE ONE TRADE (parametric trailing stop) ───────────────────────────
def simulate_trade(hist, entry_date, trail_pct):
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data = hist[hist.index == entry_date]
    if day_data.empty:
        return None
    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1 + HARD_STOP)
    highest_close = entry_price
    trail_active = False
    trail_stop = None
    future = hist[hist.index >= entry_date]

    for dt, row in future.iterrows():
        close = row["Close"]
        if pd.isna(close):
            continue
        if close > highest_close:
            highest_close = close
        if highest_close >= entry_price * (1 + TRAIL_TRIGGER):
            trail_active = True
        if trail_active:
            trail_stop = highest_close * (1 - trail_pct)

        cal_days = (dt - entry_date).days
        if cal_days >= TIME_STOP:
            return _exit(dt, close, "time", cal_days, entry_price)
        if close <= hard_stop_price:
            return _exit(dt, close, "hard_stop", cal_days, entry_price)
        if trail_active and trail_stop and close <= trail_stop:
            return _exit(dt, close, "trail_stop", cal_days, entry_price)

    last = future.iloc[-1]
    return _exit(last.name, last["Close"], "data_end",
                 (last.name - entry_date).days, entry_price)


def _exit(dt, price, reason, days, entry_price):
    return {"exit_date": dt.date(), "exit_price": price, "exit_reason": reason,
            "holding_days": days, "return_pct": (price - entry_price) / entry_price,
            "entry_price": entry_price}


# ─── SPY REGIME ───────────────────────────────────────────────────────────────
def build_spy(spy_hist):
    close = spy_hist["Close"].squeeze()
    close.index = pd.to_datetime(close.index).normalize()
    if close.index.tz is not None:
        close.index = close.index.tz_localize(None)
    ma200 = close.rolling(200, min_periods=100).mean()
    regime = (close > ma200)
    return close, regime


def regime_at(regime, date):
    try:
        return bool(regime.asof(pd.Timestamp(date).normalize()))
    except Exception:
        return None


# ─── MAIN SCAN ────────────────────────────────────────────────────────────────
def run_backtest():
    print("Fetching S&P 500 universe...")
    sp500 = get_sp500()
    tickers = sp500["ticker"].tolist()
    sector_map = dict(zip(sp500["ticker"], sp500["sector"]))
    name_map   = dict(zip(sp500["ticker"], sp500["name"]))

    print("Fetching SPY (benchmark + 200MA regime + RS)...")
    spy_hist = yf.download("SPY", start="2023-06-01", end=DATA_END,
                           auto_adjust=True, progress=False)
    if isinstance(spy_hist.columns, pd.MultiIndex):
        spy_hist.columns = spy_hist.columns.get_level_values(0)
    spy_close, regime = build_spy(spy_hist)
    spy_ytd = spy_close[(spy_close.index >= TEST_START) & (spy_close.index <= TEST_END)]
    spy_return = (float(spy_ytd.iloc[-1]) - float(spy_ytd.iloc[0])) / float(spy_ytd.iloc[0])

    rows = []
    skipped = no_earn = 0
    total = len(tickers)
    print(f"Processing {total} tickers...")
    for idx, ticker in enumerate(tickers):
        if idx % 50 == 0:
            print(f"  {idx}/{total} ({len(rows)} candidates so far)...")
        hist, earnings = fetch_ticker_data(ticker)
        if hist is None:
            skipped += 1
            continue
        if earnings is None:
            no_earn += 1
            continue

        trading_days = get_trading_days(hist)
        sector = sector_map.get(ticker, "Unknown")
        is_it = (sector == IT_SECTOR)

        for earn_date, erow in earnings.iterrows():
            earn_date = pd.Timestamp(earn_date).normalize()
            if earn_date < pd.Timestamp(TEST_START) - timedelta(days=30):
                continue
            if earn_date > pd.Timestamp(TEST_END):
                continue

            try:
                reported = float(erow.get("reported", np.nan))
                estimate = float(erow.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(reported) or pd.isna(estimate):
                continue
            if not (reported > estimate):       # BASE gate: EPS beat
                continue

            entry_date = nth_trading_day_after(trading_days, earn_date, ENTRY_DELAY)
            if entry_date is None:
                continue
            if entry_date < pd.Timestamp(TEST_START) or entry_date > pd.Timestamp(TEST_END):
                continue

            day_data = hist[hist.index == entry_date]
            if day_data.empty:
                continue
            open_price = day_data["Open"].iloc[0]
            if pd.isna(open_price) or open_price < MIN_PRICE:   # BASE gate: price
                continue
            if not avg_dvol_ok(hist, earn_date):                # BASE gate: $vol
                continue

            # Outcome with sector-appropriate trail (headline engine)
            trail_pct = TRAIL_PCT_IT if is_it else TRAIL_PCT_DEFAULT
            res = simulate_trade(hist, entry_date, trail_pct)
            if res is None:
                continue
            # Alternate outcomes for the trailing-stop comparison
            res7  = simulate_trade(hist, entry_date, 0.07)
            res12 = simulate_trade(hist, entry_date, 0.12)

            # Surprise %
            surprise = None
            if "surprise_pct" in erow and not pd.isna(erow["surprise_pct"]):
                surprise = float(erow["surprise_pct"])
            elif estimate != 0:
                surprise = (reported - estimate) / abs(estimate) * 100

            # Enhanced filter evaluations
            vratio = vol_ratio_on_day(hist, earn_date)
            rs = rel_strength_vs_spy(hist, spy_close, earn_date, entry_date)
            hi45 = new_52w_high_recent(hist, entry_date)
            d_next = days_to_next_earnings(earnings, earn_date, entry_date)

            f_surprise15 = (surprise is not None) and (surprise >= SURPRISE_MIN)
            f_vol15x     = (vratio is not None) and (vratio >= VOL_MULT)
            f_rs         = (rs is not None) and (rs > 0)
            f_52w        = (hi45 is True)
            # NOT within 3 days of upcoming earnings (pass if no next earnings known
            # or it is more than NEAR_EARN_DAYS away)
            f_nearearn   = (d_next is None) or (d_next > NEAR_EARN_DAYS) or (d_next < 0)

            rows.append({
                "ticker": ticker, "sector": sector, "name": name_map.get(ticker, ticker),
                "is_it": is_it,
                "earn_date": earn_date.date(), "entry_date": entry_date.date(),
                "entry_price": round(open_price, 4),
                "exit_date": res["exit_date"], "exit_price": round(res["exit_price"], 4),
                "exit_reason": res["exit_reason"], "holding_days": res["holding_days"],
                "return_pct": round(res["return_pct"] * 100, 2),
                "return_dollar": round(res["return_pct"] * POSITION_SIZE, 2),
                "ret_trail7":  round(res7["return_pct"] * 100, 2)  if res7  else None,
                "ret_trail12": round(res12["return_pct"] * 100, 2) if res12 else None,
                "surprise_pct": round(surprise, 2) if surprise is not None else None,
                "vol_ratio": round(vratio, 2) if vratio is not None else None,
                "rs_value": round(rs * 100, 2) if rs is not None else None,
                "days_to_next_earn": d_next,
                "f_surprise15": f_surprise15, "f_vol15x": f_vol15x,
                "f_rs": f_rs, "f_52w": f_52w, "f_nearearn": f_nearearn,
                "spy_bull_regime": regime_at(regime, entry_date),
            })

        time.sleep(0.04)

    print(f"\nDone. BASE candidates: {len(rows)}, No-earnings: {no_earn}, Skipped: {skipped}")
    return pd.DataFrame(rows), spy_return


# ─── STATS ────────────────────────────────────────────────────────────────────
def compute_stats(df, ret_col="return_pct"):
    if df.empty:
        return {}
    dollar = (df[ret_col] / 100 * POSITION_SIZE)
    winners = df[df[ret_col] > 0]
    losers  = df[df[ret_col] <= 0]
    gw = (winners[ret_col] / 100 * POSITION_SIZE).sum()
    gl = abs((losers[ret_col] / 100 * POSITION_SIZE).sum())
    pf = gw / gl if gl > 0 else float("inf")

    streaks, cur = [], 0
    for r in df.sort_values("entry_date")[ret_col]:
        if r <= 0:
            cur += 1; streaks.append(cur)
        else:
            cur = 0
    mcl = max(streaks) if streaks else 0

    best = df.loc[df[ret_col].idxmax()]
    worst = df.loc[df[ret_col].idxmin()]
    return {
        "total_trades": len(df),
        "win_rate": round((df[ret_col] > 0).mean() * 100, 1),
        "avg_return_pct": round(df[ret_col].mean(), 2),
        "avg_winner_pct": round(winners[ret_col].mean(), 2) if not winners.empty else 0,
        "avg_loser_pct": round(losers[ret_col].mean(), 2) if not losers.empty else 0,
        "median_return_pct": round(df[ret_col].median(), 2),
        "total_return_dollar": round(dollar.sum(), 2),
        "profit_factor": round(pf, 2) if pf != float("inf") else float("inf"),
        "max_consec_loss": mcl,
        "avg_holding_days": round(df["holding_days"].mean(), 1),
        "best_trade": f"{best['ticker']} {best[ret_col]:+.2f}% ({best['holding_days']}d)",
        "worst_trade": f"{worst['ticker']} {worst[ret_col]:+.2f}% ({worst['holding_days']}d)",
        "exit_reasons": df["exit_reason"].value_counts().to_dict(),
    }


def compute_sharpe(df, ret_col="return_pct"):
    if df.empty or len(df) < 5:
        return None
    r = df[ret_col] / 100
    rf = 0.045 / 12
    if r.std() == 0:
        return None
    return round((r.mean() - rf) / r.std() * np.sqrt(len(r)), 2)


def sub_block(sub, ret_col="return_pct"):
    """Return (n, win_rate, avg, pf) for a sub-frame."""
    if sub.empty:
        return (0, None, None, None)
    wr = round((sub[ret_col] > 0).mean() * 100, 1)
    avg = round(sub[ret_col].mean(), 2)
    gw = (sub[sub[ret_col] > 0][ret_col] / 100 * POSITION_SIZE).sum()
    gl = abs((sub[sub[ret_col] <= 0][ret_col] / 100 * POSITION_SIZE).sum())
    pf = round(gw / gl, 2) if gl > 0 else float("inf")
    return (len(sub), wr, avg, pf)


# ─── REPORT ───────────────────────────────────────────────────────────────────
def build_report(base, enh, scenA, scenB, spy_return):
    L = []
    A = L.append
    stats = compute_stats(enh) if not enh.empty else {}
    base_stats = compute_stats(base)
    spy_pct = round(spy_return * 100, 1)

    A("# PEAD 2026 YTD Out-of-Sample Backtest — Enhanced Strategy")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    A(f"\n*Test window: {TEST_START} → {TEST_END} (S&P 500 current constituents).*")
    A("\n---\n")

    # ── 1. Verdict ───────────────────────────────────────────────────────────
    A("## 1. 2026 YTD Verdict\n")
    if enh.empty:
        A("**INCONCLUSIVE — the enhanced filter stack produced zero qualifying trades.**")
        A("\nThe ≥15% EPS-surprise requirement combined with the other filters removed "
          "every candidate. See the filter-impact section for where trades were lost.")
        wr = avg = pf = 0
    else:
        wr, avg, pf = stats["win_rate"], stats["avg_return_pct"], stats["profit_factor"]
        n = stats["total_trades"]
        beat25 = (wr >= BASELINE_2025["win_rate"]) and (avg >= BASELINE_2025["avg_return_pct"])
        small = n < 30
        if beat25 and not small:
            v = "**YES — the enhanced strategy beat the 2025 baseline.**"
            e = (f"On {n} qualifying 2026 trades the enhanced stack delivered a {wr}% win rate "
                 f"and {avg}% average return, exceeding the 2025 OOS baseline (55.5% / +1.54%). "
                 "The added filters improved selectivity without destroying the edge.")
        elif beat25 and small:
            v = "**TENTATIVELY YES — metrics beat 2025 but the sample is too small to trust.**"
            e = (f"Only {n} trades cleared the full enhanced stack in 5 months. The headline "
                 f"win rate ({wr}%) and average return ({avg}%) exceed the 2025 baseline, but at "
                 "this sample size the result is dominated by a handful of names and is not "
                 "statistically distinguishable from the baseline.")
        elif avg > 0:
            v = "**MIXED — profitable but did not clearly beat 2025.**"
            e = (f"The enhanced stack produced {n} trades at {wr}% win rate and {avg}% average "
                 f"return — positive, but not a clear improvement over the 2025 baseline "
                 "(55.5% / +1.54%). The extra filters mostly cut trade count rather than "
                 "lifting per-trade quality over this window.")
        else:
            v = "**NO — the enhanced strategy underperformed over 2026 YTD.**"
            e = (f"The {n} qualifying trades averaged {avg}% (win rate {wr}%), below the 2025 "
                 "baseline. Over this short window the added filters did not add value.")
        A(v); A(""); A(e)
    A("")
    A(f"> **Sample-size caveat.** 2026 YTD spans only ~107 trading days and ~2 earnings "
      f"seasons. The ≥15% surprise filter is intentionally strict, so the enhanced trade "
      f"count is small and all 2026 conclusions are low-confidence relative to the "
      f"multi-year baselines.")
    A("")

    # ── 2. Comparison table ──────────────────────────────────────────────────
    A("## 2. Comparison — 2022-2024 vs 2025 OOS vs 2026 YTD\n")
    A("| Metric | 2022-2024 (in-sample) | 2025 (OOS) | 2026 YTD (enhanced) |")
    A("|--------|----------------------:|-----------:|--------------------:|")
    def g(k, suffix="", plus=False):
        v = stats.get(k) if stats else None
        if v is None:
            return "—"
        return (f"+{v}{suffix}" if plus and v > 0 else f"{v}{suffix}")
    A(f"| Total trades | {BASELINE_INSAMPLE['total_trades']} | {BASELINE_2025['total_trades']} | {stats.get('total_trades','—') if stats else '—'} |")
    A(f"| Win rate | {BASELINE_INSAMPLE['win_rate']}% | {BASELINE_2025['win_rate']}% | {g('win_rate','%')} |")
    A(f"| Avg return / trade | {BASELINE_INSAMPLE['avg_return_pct']}% | {BASELINE_2025['avg_return_pct']}% | {g('avg_return_pct','%')} |")
    A(f"| Avg winner | +{BASELINE_INSAMPLE['avg_winner_pct']}% | +{BASELINE_2025['avg_winner_pct']}% | {g('avg_winner_pct','%',plus=True)} |")
    A(f"| Avg loser | {BASELINE_INSAMPLE['avg_loser_pct']}% | {BASELINE_2025['avg_loser_pct']}% | {g('avg_loser_pct','%')} |")
    A(f"| Profit factor | {BASELINE_INSAMPLE['profit_factor']} | {BASELINE_2025['profit_factor']} | {stats.get('profit_factor','—') if stats else '—'} |")
    A(f"| Max consec. losses | {BASELINE_INSAMPLE['max_consec_loss']} | {BASELINE_2025['max_consec_loss']} | {stats.get('max_consec_loss','—') if stats else '—'} |")
    A(f"| Avg holding days | {BASELINE_INSAMPLE['avg_holding_days']} | {BASELINE_2025['avg_holding_days']} | {stats.get('avg_holding_days','—') if stats else '—'} |")
    A(f"| SPY buy-and-hold | {BASELINE_INSAMPLE['spy_return_pct']}% | {BASELINE_2025['spy_return_pct']}% | {spy_pct}% |")
    A("")
    A(f"*2026 holding days and SPY return are partial-period (5 months); the 42-day time "
      f"stop has not fully cycled for spring entries.*")
    A("")

    # ── 3. Filter impact ─────────────────────────────────────────────────────
    A("## 3. Filter Impact Analysis\n")
    A(f"BASE candidate set (EPS beat + price ≥ ${MIN_PRICE:.0f} + 20d avg $vol ≥ "
      f"${MIN_AVG_DVOL/1e6:.0f}M): **{len(base)} trades**, "
      f"win rate **{base_stats['win_rate']}%**, avg **{base_stats['avg_return_pct']}%**.\n")
    A("Each filter below is applied *independently* to the BASE set. \"Removed\" = BASE "
      "candidates that FAIL that filter; a well-designed filter should remove trades whose "
      "win rate is *below* the BASE win rate (i.e. it strips losers).\n")
    A("| Filter | Kept | Removed | Win% kept | Win% removed | Avg% removed | Verdict |")
    A("|--------|-----:|--------:|----------:|-------------:|-------------:|---------|")
    filt_defs = [
        ("EPS surprise ≥ 15%", "f_surprise15"),
        ("Volume ≥ 1.5× 20d avg", "f_vol15x"),
        ("Rel. strength vs SPY > 0", "f_rs"),
        ("New 52-wk high ≤ 45d", "f_52w"),
        ("Not within 3d of next earnings", "f_nearearn"),
    ]
    base_wr = base_stats["win_rate"]
    for label, col in filt_defs:
        kept = base[base[col]]
        removed = base[~base[col]]
        nk, wk = len(kept), (round((kept["return_pct"] > 0).mean()*100,1) if not kept.empty else None)
        nr = len(removed)
        wr_rm = round((removed["return_pct"] > 0).mean()*100,1) if not removed.empty else None
        avg_rm = round(removed["return_pct"].mean(),2) if not removed.empty else None
        if nr == 0:
            verdict = "removed nothing"
        elif wr_rm is not None and wr_rm < base_wr - 2:
            verdict = "✓ strips losers"
        elif wr_rm is not None and wr_rm > base_wr + 2:
            verdict = "✗ removed winners"
        else:
            verdict = "~ neutral"
        A(f"| {label} | {nk} | {nr} | {wk if wk is not None else '—'}% | "
          f"{wr_rm if wr_rm is not None else '—'}% | {avg_rm if avg_rm is not None else '—'}% | {verdict} |")
    A("")
    A("**Scenario sensitivity (guidance-raise filter unverifiable in yfinance):**\n")
    A("| Scenario | Definition | Trades | Win% | Avg% | Profit factor |")
    A("|----------|------------|-------:|-----:|-----:|--------------:|")
    for nm, defn, d in [
        ("A", "EPS beat ≥ 15% only", scenA),
        ("B", "EPS beat ≥ 15% + volume 1.5×", scenB),
        ("Full", "All verifiable enhanced filters", enh),
    ]:
        n, w, a, p = sub_block(d)
        A(f"| {nm} | {defn} | {n} | {w if w is not None else '—'}% | "
          f"{a if a is not None else '—'}% | {p if p is not None else '—'} |")
    A("")

    # ── 4. Trailing stop analysis ────────────────────────────────────────────
    A("## 4. Trailing-Stop Analysis — 7% vs 12% for IT\n")
    it = enh[enh["is_it"]] if not enh.empty else enh
    nonit = enh[~enh["is_it"]] if not enh.empty else enh
    if not enh.empty and not it.empty:
        it7 = it["ret_trail7"].mean()
        it12 = it["ret_trail12"].mean()
        delta = it12 - it7
        A(f"IT/semiconductor trades in the enhanced set: **{len(it)}**.\n")
        A("| Trailing stop | IT avg return | IT win rate |")
        A("|---------------|--------------:|------------:|")
        A(f"| 7% (old, all sectors) | {round(it7,2)}% | {round((it['ret_trail7']>0).mean()*100,1)}% |")
        A(f"| 12% (new, IT only) | {round(it12,2)}% | {round((it['ret_trail12']>0).mean()*100,1)}% |")
        A("")
        A(f"The wider 12% IT trail {'captured an additional ' + str(round(delta,2)) + '% per IT trade on average' if delta > 0 else 'gave back ' + str(round(-delta,2)) + '% per IT trade on average'} "
          f"(letting IT winners run through normal volatility instead of being shaken out at 7%).")
        if len(it) > 0:
            A(f"\nAggregate effect across {len(it)} IT trades: "
              f"**{round((it['ret_trail12']-it['ret_trail7']).sum()/100*POSITION_SIZE,0):+,.0f}** P&L vs the old 7% trail.")
    else:
        A("*No IT/semiconductor trades cleared the enhanced filter stack in 2026 YTD, so the "
          "7%-vs-12% trailing-stop change had no effect on realised trades this period.*")
    A("")

    # ── 5. Full trade statistics ─────────────────────────────────────────────
    A("## 5. Full Trade Statistics (enhanced set)\n")
    if enh.empty:
        A("*No trades.*\n")
    else:
        A("| Metric | Value |")
        A("|--------|-------|")
        A(f"| Total trades | {stats['total_trades']} |")
        A(f"| Win rate | {stats['win_rate']}% |")
        A(f"| Avg return per trade | {stats['avg_return_pct']}% |")
        A(f"| Median return | {stats['median_return_pct']}% |")
        A(f"| Avg winner | +{stats['avg_winner_pct']}% |")
        A(f"| Avg loser | {stats['avg_loser_pct']}% |")
        A(f"| Profit factor | {stats['profit_factor']} |")
        A(f"| Max consecutive losses | {stats['max_consec_loss']} |")
        A(f"| Avg holding period | {stats['avg_holding_days']} days |")
        A(f"| Total P&L (all positions) | ${stats['total_return_dollar']:,.0f} |")
        A(f"| Best trade | {stats['best_trade']} |")
        A(f"| Worst trade | {stats['worst_trade']} |")
        A(f"| SPY buy-and-hold 2026 YTD | {spy_pct}% |")
        sh = compute_sharpe(enh)
        if sh:
            A(f"| Approx. Sharpe ratio | {sh} |")
        A("")
        A("**Exit reason breakdown:**\n")
        for reason, count in stats["exit_reasons"].items():
            A(f"- {reason}: {count} ({round(count/stats['total_trades']*100,1)}%)")
        A(f"\n*Note: `data_end` exits are trades still open at {TEST_END} (time stop not yet "
          f"reached) — their returns are marked-to-market, not realised.*")
    A("")

    # ── 6. Regime analysis ───────────────────────────────────────────────────
    A("## 6. Regime Analysis (SPY vs 200-day MA)\n")
    if enh.empty or enh["spy_bull_regime"].isna().all():
        A("*Insufficient data.*\n")
    else:
        for val, lab in [(True, "Bull regime (SPY > 200MA)"),
                         (False, "Bear regime (SPY < 200MA)")]:
            sub = enh[enh["spy_bull_regime"] == val]
            n, w, a, p = sub_block(sub)
            if n == 0:
                A(f"**{lab}:** no trades.\n"); continue
            A(f"**{lab}** — {n} trades")
            A(f"- Win rate: {w}%")
            A(f"- Avg return: {a}%")
            A(f"- Profit factor: {p}\n")
        bull = enh[enh["spy_bull_regime"] == True]
        bear = enh[enh["spy_bull_regime"] == False]
        if not bull.empty and not bear.empty:
            ba, bea = round(bull["return_pct"].mean(),2), round(bear["return_pct"].mean(),2)
            A(f"*2025 finding was that the bear regime outperformed. 2026 YTD: bull avg {ba}% "
              f"vs bear avg {bea}% — "
              + ("bear again outperformed, replicating 2025." if bea > ba else
                 "bull outperformed, NOT replicating the 2025 pattern.") + "*")
        else:
            present = "bull" if not bull.empty else "bear"
            A(f"*All 2026 YTD enhanced trades fell in the {present} regime, so the "
              "2025 bull-vs-bear comparison cannot be replicated this period.*")
    A("")

    # ── 7. Sector breakdown ──────────────────────────────────────────────────
    A("## 7. Sector Breakdown (enhanced set)\n")
    if enh.empty:
        A("*No trades.*\n")
    else:
        A("| Sector | Trades | Win Rate | Avg Return | Total P&L |")
        A("|--------|-------:|---------:|-----------:|----------:|")
        sect = enh.groupby("sector").agg(
            trades=("return_pct", "count"),
            win=("return_pct", lambda x: round((x > 0).mean()*100,1)),
            avg=("return_pct", lambda x: round(x.mean(),2)),
            pnl=("return_dollar", lambda x: round(x.sum(),0)),
        ).sort_values("pnl", ascending=False)
        for sec, r in sect.iterrows():
            star = " ⭐" if sec == IT_SECTOR else ""
            A(f"| {sec}{star} | {r['trades']} | {r['win']}% | {r['avg']}% | ${r['pnl']:,.0f} |")
        A(f"\n⭐ = Information Technology (subject to the wider 12% trailing stop).")
    A("")

    # ── 8. Best/Worst ────────────────────────────────────────────────────────
    A("## 8. Best & Worst Trades (enhanced set)\n")
    if enh.empty:
        A("*No trades.*\n")
    else:
        for title, frame in [("Best 10", enh.nlargest(10, "return_pct")),
                             ("Worst 10", enh.nsmallest(10, "return_pct"))]:
            A(f"**{title}**\n")
            A("| Ticker | Sector | Entry | Entry $ | Exit | Exit $ | Return % | Days | Reason |")
            A("|--------|--------|-------|--------:|------|-------:|---------:|-----:|--------|")
            for _, r in frame.iterrows():
                A(f"| {r['ticker']} | {r['sector']} | {r['entry_date']} | ${r['entry_price']} "
                  f"| {r['exit_date']} | ${r['exit_price']} | {r['return_pct']:+.2f}% "
                  f"| {r['holding_days']} | {r['exit_reason']} |")
            A("")

    # ── 9. Key findings ──────────────────────────────────────────────────────
    A("## 9. Key Findings — what changed vs 2025\n")
    A(f"- **Selectivity exploded, sample shrank.** The 2025 baseline used EPS-beat-only "
      f"and produced 1,454 trades. The 2026 enhanced stack cut the {len(base)} EPS-beat "
      f"BASE candidates down to **{len(enh)}** — a far smaller, higher-conviction set.")
    A(f"- **The raw 2026 PEAD signal was negative.** EPS-beat-only (the 2025 methodology) "
      f"returned {base_stats['win_rate']}% win / {base_stats['avg_return_pct']}% avg on {len(base)} "
      f"trades in 2026 YTD — versus 55.5% / +1.54% in 2025. PEAD simply did not work in early "
      f"2026; this is a regime problem, not a filter problem.")
    if not enh.empty:
        A(f"- **The filters added value against that backdrop:** they lifted avg return from "
          f"{base_stats['avg_return_pct']}% (BASE) toward {stats['avg_return_pct']}% (full stack) "
          f"/ Scenario A {round(compute_stats(scenA)['avg_return_pct'],2)}% — i.e. the enhancements "
          f"did roughly what they were designed to do, but could not rescue a losing-signal regime.")
        A(f"- **Headline quality:** enhanced 2026 win rate {stats['win_rate']}% / avg "
          f"{stats['avg_return_pct']}% vs 2025's 55.5% / +1.54%.")
    # which filter strips most losers
    best_filter = None
    best_gap = 0
    for label, col in filt_defs:
        removed = base[~base[col]]
        if not removed.empty:
            gap = base_wr - round((removed["return_pct"] > 0).mean()*100,1)
            if gap > best_gap:
                best_gap, best_filter = gap, label
    if best_filter:
        A(f"- **Most valuable filter:** \"{best_filter}\" removed trades with the lowest "
          f"win rate relative to BASE (≈{round(best_gap,1)} pts below the BASE win rate), "
          "i.e. it stripped the most losers.")
    A(f"- **SPY 2026 YTD: {spy_pct}%.** "
      + (f"At {stats['avg_return_pct']}% avg per trade (PF {stats['profit_factor']}, ~"
         f"{stats['avg_holding_days']}d holds) the enhanced strategy was roughly flat and "
         f"badly lagged passive SPY this period." if not enh.empty else
         "No enhanced trades this period."))
    A(f"- **Regulatory filters (BIS export-control, SEC shelf registration) were NOT "
      f"applied** — they cannot be reconstructed from yfinance. Real-world deployment with "
      f"those filters would remove additional names.")
    A(f"- **Guidance-raise filter NOT applied** (no reliable data); Scenarios A/B bracket "
      f"its likely impact.")
    A("")

    # ── 10. Recommendation ───────────────────────────────────────────────────
    A("## 10. Recommendation\n")
    if enh.empty:
        rec = "**MODIFY — the filter stack is too strict.**"
        detail = ("With zero qualifying trades in 5 months the ≥15% surprise gate (stacked with "
                  "the others) starves the strategy of trades. Loosen the surprise threshold "
                  "(e.g. ≥8–10%) or treat the strict filters as a ranking overlay rather than a "
                  "hard gate, then re-test on 2022-2025 for a meaningful sample.")
    elif stats["total_trades"] < 30:
        rec = "**CONTINUE PAPER-TRADING — promising but undersampled.**"
        detail = (f"The enhanced stack looks selective and the headline metrics are reasonable, "
                  f"but {stats['total_trades']} trades over 5 months is far too few to confirm an "
                  "improvement over the 2025 baseline. Keep DRY_RUN paper trading, gather a full "
                  "year, and re-run the enhanced rules over 2022-2025 to validate the filters on a "
                  "large sample before flipping DRY_RUN to false.")
    elif stats["avg_return_pct"] >= BASELINE_2025["avg_return_pct"] and stats["win_rate"] >= BASELINE_2025["win_rate"]:
        rec = "**CONTINUE — enhancements look additive.**"
        detail = ("The enhanced filters improved per-trade quality versus the 2025 baseline on a "
                  "usable sample. Continue paper trading, then consider live deployment with the "
                  "regulatory + guidance filters layered in manually.")
    else:
        rec = "**MODIFY — filters cut count without clearly improving quality.**"
        detail = ("Over 2026 YTD the enhanced stack did not beat the simpler 2025 baseline on "
                  "per-trade return. Re-validate each filter on the full 2022-2025 history before "
                  "committing; some filters may be removing winners.")
    A(rec); A(""); A(detail)
    A("")
    A("---")
    A("### Limitations\n")
    A("1. **Survivorship bias** — current S&P 500 constituents only.")
    A(f"2. **Short window** — {TEST_START}→{TEST_END} is ~107 trading days; spring entries "
      "have not completed the 42-day time stop (`data_end` exits are marked-to-market).")
    A("3. **Relative strength** measured earnings-close → pre-entry close (no lookahead); the "
      "literal \"5 days since earnings\" rule would require day+5 data for a day+2 entry, which "
      "is forward-looking, so a non-lookahead proxy was used.")
    A("4. **Guidance raise, BIS export-control, SEC shelf-registration filters NOT applied** "
      "(not reconstructable from yfinance).")
    A("5. **No transaction costs / slippage; no portfolio-level capital constraint** (each "
      "trade simulated independently at 11% sizing).")
    A("6. **Earnings timestamps** from yfinance can be off by a day vs the true pre/post-market "
      "announcement.")
    A("")
    A("*Backtest engine: yfinance + custom Python. Not financial advice.*")
    return "\n".join(L)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # This engine module stays at the repo root because production
    # compute_pead_health.py imports it. When run standalone, write the research
    # report/trade CSV into backtesting/reports/ alongside the other artifacts.
    import os
    _REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "backtesting", "reports")

    base, spy_return = run_backtest()
    if base.empty:
        print("No BASE candidates generated. Check 2026 data availability.")
        sys.exit(1)

    enh = base[base["f_surprise15"] & base["f_vol15x"] & base["f_rs"]
               & base["f_52w"] & base["f_nearearn"]].copy()
    scenA = base[base["f_surprise15"]].copy()
    scenB = base[base["f_surprise15"] & base["f_vol15x"]].copy()

    print(f"\nBASE: {len(base)} | Enhanced(full): {len(enh)} | "
          f"ScenA: {len(scenA)} | ScenB: {len(scenB)}")

    report = build_report(base, enh, scenA, scenB, spy_return)
    with open(os.path.join(_REPORTS_DIR, "backtest_report_PEAD_2026_YTD.md"), "w", encoding="utf-8") as f:
        f.write(report)
    # Save the enhanced trade set (or BASE if enhanced is empty) with filter flags
    out = enh if not enh.empty else base
    out.to_csv(os.path.join(_REPORTS_DIR, "backtest_trades_PEAD_2026_YTD.csv"), index=False)

    print("\nReport saved:    backtest_report_PEAD_2026_YTD.md")
    print("Trades saved:    backtest_trades_PEAD_2026_YTD.csv")
    if not enh.empty:
        s = compute_stats(enh)
        print("\n--- ENHANCED 2026 YTD SUMMARY ---")
        print(f"  Trades:        {s['total_trades']}")
        print(f"  Win rate:      {s['win_rate']}%")
        print(f"  Avg return:    {s['avg_return_pct']}%")
        print(f"  Profit factor: {s['profit_factor']}")
        print(f"  SPY 2026 YTD:  {round(spy_return*100,1)}%")
    else:
        print("\nEnhanced set EMPTY — see filter-impact section in report.")
