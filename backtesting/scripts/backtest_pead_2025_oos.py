"""
PEAD Out-of-Sample Backtest — 2025
IDENTICAL strategy rules to backtest_pead.py (2022-2024 in-sample run).
NO rule changes allowed — this is the validation test.
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
import os

# --- Path anchoring: reports/trade CSVs resolve under backtesting/reports/ ----
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPORTS_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "reports"))

warnings.filterwarnings("ignore")

# ─── CONFIG (IDENTICAL to in-sample run) ─────────────────────────────────────
START_DATE  = "2024-07-01"   # pull extra history for volume / 200MA calc
TEST_START  = "2025-01-01"
TEST_END    = "2025-12-31"
POSITION_SIZE = 11_000
HARD_STOP     = -0.08
TRAIL_TRIGGER = 0.10
TRAIL_PCT     = 0.07
TIME_STOP     = 42
MIN_PRICE     = 10.0
MIN_AVG_DVOL  = 20_000_000
ENTRY_DELAY   = 2

# In-sample baseline (2022-2024) for comparison table
BASELINE = {
    "period": "2022-2024",
    "total_trades": 4387,
    "win_rate": 54.8,
    "avg_return_pct": 1.32,
    "avg_winner_pct": 7.74,
    "avg_loser_pct": -6.45,
    "profit_factor": 1.45,
    "max_consec_loss": 41,
    "avg_holding_days": 35.6,
    "spy_return_pct": 28.2,
}


# ─── STEP 1: S&P 500 UNIVERSE ────────────────────────────────────────────────
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
        if sec_col:
            result["sector"] = df[sec_col]
        if name_col:
            result["name"] = df[name_col]
        result["ticker"] = result["ticker"].str.replace(".", "-", regex=False)
        return result
    except Exception as e:
        print(f"[ERROR] Could not fetch S&P 500 list: {e}")
        sys.exit(1)


# ─── STEP 2: FETCH PRICE + EARNINGS ──────────────────────────────────────────
def fetch_ticker_data(ticker):
    try:
        tk   = yf.Ticker(ticker)
        # Pull through end of Jan 2026 so time-stop exits in Dec 2025 have data
        hist = tk.history(start=START_DATE, end="2026-02-15", auto_adjust=True)
        if hist.empty or len(hist) < 50:
            return None, None
        if hist.index.tz is not None:
            hist.index = hist.index.tz_localize(None)

        try:
            eh = tk.get_earnings_dates(limit=20)
        except Exception:
            return hist, None

        if eh is None or eh.empty:
            return hist, None

        eh = eh.rename(columns={
            "Reported EPS": "reported",
            "EPS Estimate":  "estimate",
            "Surprise(%)":   "surprise_pct",
        })
        eh.index = pd.to_datetime(eh.index).tz_localize(None)
        eh = eh.sort_index()
        return hist, eh
    except Exception:
        return None, None


# ─── STEP 3: TRADING CALENDAR HELPERS ────────────────────────────────────────
def get_trading_days(hist):
    return sorted(hist.index.normalize().unique())


def nth_trading_day_after(trading_days, date, n):
    date   = pd.Timestamp(date).normalize()
    future = [d for d in trading_days if d > date]
    return future[n - 1] if len(future) >= n else None


# ─── STEP 4: DOLLAR VOLUME FILTER ────────────────────────────────────────────
def avg_dvol_ok(hist, date, window=20):
    date  = pd.Timestamp(date).normalize()
    prior = hist[hist.index.normalize() < date].tail(window)
    if len(prior) < window // 2:
        return False
    dvol = (prior["Close"] * prior["Volume"]).mean()
    return dvol >= MIN_AVG_DVOL


# ─── STEP 5: SIMULATE ONE TRADE ──────────────────────────────────────────────
def simulate_trade(hist, entry_date):
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data   = hist[hist.index.normalize() == entry_date]
    if day_data.empty:
        return None

    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1 + HARD_STOP)
    highest_close   = entry_price
    trail_active    = False
    trail_stop      = None

    future = hist[hist.index.normalize() >= entry_date]

    for dt, row in future.iterrows():
        close = row["Close"]
        if pd.isna(close):
            continue

        if close > highest_close:
            highest_close = close
        if highest_close >= entry_price * (1 + TRAIL_TRIGGER):
            trail_active = True
        if trail_active:
            trail_stop = highest_close * (1 - TRAIL_PCT)

        cal_days = (dt.normalize() - entry_date).days

        if cal_days >= TIME_STOP:
            return {"exit_date": dt.date(), "exit_price": close,
                    "exit_reason": "time", "holding_days": cal_days,
                    "return_pct": (close - entry_price) / entry_price}

        if close <= hard_stop_price:
            return {"exit_date": dt.date(), "exit_price": close,
                    "exit_reason": "hard_stop", "holding_days": cal_days,
                    "return_pct": (close - entry_price) / entry_price}

        if trail_active and trail_stop and close <= trail_stop:
            return {"exit_date": dt.date(), "exit_price": close,
                    "exit_reason": "trail_stop", "holding_days": cal_days,
                    "return_pct": (close - entry_price) / entry_price}

    last_row  = future.iloc[-1]
    last_close = last_row["Close"]
    holding    = (last_row.name.normalize() - entry_date).days
    return {"exit_date": last_row.name.date(), "exit_price": last_close,
            "exit_reason": "data_end", "holding_days": holding,
            "return_pct": (last_close - entry_price) / entry_price}


# ─── STEP 6: SPY 200-DAY MA REGIME ───────────────────────────────────────────
def build_spy_regime(spy_hist):
    """Returns a Series indexed by date: True = above 200MA (bull regime)."""
    close = spy_hist["Close"].squeeze()
    ma200 = close.rolling(200, min_periods=100).mean()
    regime = close > ma200
    regime.index = pd.to_datetime(regime.index).normalize()
    if regime.index.tz is not None:
        regime.index = regime.index.tz_localize(None)
    return regime


def get_regime(regime_series, date):
    date = pd.Timestamp(date).normalize()
    try:
        return bool(regime_series.asof(date))
    except Exception:
        return None


# ─── STEP 7: MAIN BACKTEST LOOP ──────────────────────────────────────────────
def run_backtest():
    print("Fetching S&P 500 universe...")
    sp500      = get_sp500()
    tickers    = sp500["ticker"].tolist()
    sector_map = {}
    if "sector" in sp500.columns:
        sector_map = dict(zip(sp500["ticker"], sp500["sector"]))

    print("Fetching SPY benchmark + 200MA regime...")
    spy_hist = yf.download("SPY", start="2024-01-01", end="2026-02-15",
                           auto_adjust=True, progress=False)
    if isinstance(spy_hist.columns, pd.MultiIndex):
        spy_hist.columns = spy_hist.columns.get_level_values(0)
    spy_hist.index = pd.to_datetime(spy_hist.index).normalize()
    if spy_hist.index.tz is not None:
        spy_hist.index = spy_hist.index.tz_localize(None)

    # 2025 SPY return
    spy_2025 = spy_hist[(spy_hist.index >= TEST_START) & (spy_hist.index <= TEST_END)]
    spy_start = float(spy_2025["Close"].iloc[0])
    spy_end   = float(spy_2025["Close"].iloc[-1])
    spy_return = (spy_end - spy_start) / spy_start

    # Need longer history for 200MA — pull from an earlier start if possible
    spy_full = yf.download("SPY", start="2023-01-01", end="2026-02-15",
                            auto_adjust=True, progress=False)
    if isinstance(spy_full.columns, pd.MultiIndex):
        spy_full.columns = spy_full.columns.get_level_values(0)
    spy_full.index = pd.to_datetime(spy_full.index).normalize()
    if spy_full.index.tz is not None:
        spy_full.index = spy_full.index.tz_localize(None)
    regime_series = build_spy_regime(spy_full)

    trades   = []
    skipped  = 0
    no_earn  = 0
    total    = len(tickers)

    print(f"Processing {total} tickers...")
    for idx, ticker in enumerate(tickers):
        if idx % 50 == 0:
            print(f"  {idx}/{total} ({len(trades)} trades so far)...")

        hist, earnings = fetch_ticker_data(ticker)
        if hist is None:
            skipped += 1
            continue
        if earnings is None:
            no_earn += 1
            continue

        trading_days = get_trading_days(hist)

        for earn_date, erow in earnings.iterrows():
            earn_date = pd.Timestamp(earn_date).normalize()

            # Test window gate (allow 30-day lead so Jan 2025 entries are caught)
            if earn_date < pd.Timestamp(TEST_START) - timedelta(days=30):
                continue
            if earn_date > pd.Timestamp(TEST_END):
                continue

            # EPS beat check
            try:
                reported = float(erow.get("reported", np.nan))
                estimate = float(erow.get("estimate",  np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(reported) or pd.isna(estimate):
                continue
            if not (reported > estimate):
                continue

            # Entry date = 2 trading days after earnings
            entry_date = nth_trading_day_after(trading_days, earn_date, ENTRY_DELAY)
            if entry_date is None:
                continue
            if entry_date < pd.Timestamp(TEST_START):
                continue
            if entry_date > pd.Timestamp(TEST_END):
                continue

            # Price filter at entry
            day_data = hist[hist.index.normalize() == entry_date]
            if day_data.empty:
                continue
            open_price = day_data["Open"].iloc[0]
            if pd.isna(open_price) or open_price < MIN_PRICE:
                continue

            # Dollar volume filter (pre-earnings)
            if not avg_dvol_ok(hist, earn_date):
                continue

            # Simulate
            result = simulate_trade(hist, entry_date)
            if result is None:
                continue

            # Surprise magnitude
            surprise_pct = None
            if "surprise_pct" in erow and not pd.isna(erow["surprise_pct"]):
                surprise_pct = float(erow["surprise_pct"])
            elif estimate != 0:
                surprise_pct = (reported - estimate) / abs(estimate) * 100

            # Regime flag
            spy_bull = get_regime(regime_series, entry_date)

            trades.append({
                "ticker":       ticker,
                "sector":       sector_map.get(ticker, "Unknown"),
                "earn_date":    earn_date.date(),
                "entry_date":   entry_date.date(),
                "entry_price":  round(open_price, 4),
                "exit_date":    result["exit_date"],
                "exit_price":   round(result["exit_price"], 4),
                "exit_reason":  result["exit_reason"],
                "holding_days": result["holding_days"],
                "return_pct":   round(result["return_pct"] * 100, 2),
                "return_dollar":round(result["return_pct"] * POSITION_SIZE, 2),
                "eps_reported": reported,
                "eps_estimate": estimate,
                "surprise_pct": round(surprise_pct, 2) if surprise_pct is not None else None,
                "spy_bull_regime": spy_bull,
                "year":         entry_date.year,
            })

        time.sleep(0.05)

    print(f"\nDone. Trades: {len(trades)}, No-earnings: {no_earn}, Skipped: {skipped}")
    return pd.DataFrame(trades), spy_return, regime_series


# ─── STEP 8: COMPUTE STATS ───────────────────────────────────────────────────
def compute_stats(df):
    if df.empty:
        return {}
    winners = df[df["return_pct"] > 0]
    losers  = df[df["return_pct"] <= 0]

    gross_wins = winners["return_dollar"].sum()
    gross_loss = abs(losers["return_dollar"].sum())
    profit_factor = gross_wins / gross_loss if gross_loss > 0 else float("inf")

    streaks, cur = [], 0
    for r in df.sort_values("entry_date")["return_pct"]:
        if r <= 0:
            cur += 1
            streaks.append(cur)
        else:
            cur = 0
    max_consec_loss = max(streaks) if streaks else 0

    best  = df.loc[df["return_pct"].idxmax()]
    worst = df.loc[df["return_pct"].idxmin()]

    return {
        "total_trades":       len(df),
        "win_rate":           round(len(winners) / len(df) * 100, 1),
        "avg_return_pct":     round(df["return_pct"].mean(), 2),
        "avg_winner_pct":     round(winners["return_pct"].mean(), 2) if not winners.empty else 0,
        "avg_loser_pct":      round(losers["return_pct"].mean(), 2)  if not losers.empty else 0,
        "median_return_pct":  round(df["return_pct"].median(), 2),
        "total_return_dollar":round(df["return_dollar"].sum(), 2),
        "profit_factor":      round(profit_factor, 2),
        "max_consec_loss":    max_consec_loss,
        "avg_holding_days":   round(df["holding_days"].mean(), 1),
        "best_trade":  f"{best['ticker']} +{best['return_pct']}% ({best['holding_days']}d)",
        "worst_trade": f"{worst['ticker']} {worst['return_pct']}% ({worst['holding_days']}d)",
        "exit_reasons": df["exit_reason"].value_counts().to_dict(),
    }


def compute_sharpe(df):
    if df.empty or len(df) < 5:
        return None
    r      = df["return_pct"] / 100
    rf     = 0.045 / 12
    excess = r.mean() - rf
    if r.std() == 0:
        return None
    return round(excess / r.std() * np.sqrt(len(r)), 2)


# ─── STEP 9: BUILD REPORT ────────────────────────────────────────────────────
def build_report(df, spy_return, stats):
    lines = []
    A = lines.append

    A("# PEAD Out-of-Sample Backtest Report — 2025")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    A("\n---\n")

    # ── Section 1: Out-of-Sample Verdict ────────────────────────────────────
    A("## 1. Out-of-Sample Verdict\n")
    pf  = stats["profit_factor"]
    wr  = stats["win_rate"]
    avg = stats["avg_return_pct"]

    if pf >= 1.4 and wr >= 52 and avg >= 1.0:
        verdict = "**YES — Strategy held up in 2025.**"
        expl = (f"The strategy produced a profit factor of {pf}, win rate of {wr}%, "
                f"and average return of {avg}% on completely out-of-sample data. "
                "Performance was broadly consistent with the 2022-2024 in-sample baseline, "
                "confirming the PEAD edge is real and not an artefact of curve-fitting.")
    elif pf >= 1.1 and avg >= 0.3:
        verdict = "**MIXED — Strategy partially held up in 2025.**"
        expl = (f"The strategy remained profitable (PF {pf}, avg return {avg}%) but metrics "
                f"degraded vs the 2022-2024 baseline. The edge is smaller in 2025, possibly "
                "reflecting a different macro regime, higher analyst forecast accuracy, or "
                "increased competition for the PEAD signal.")
    elif pf >= 1.0 and avg >= 0:
        verdict = "**MARGINAL — Barely profitable, edge deteriorated significantly.**"
        expl = (f"The strategy scraped out a small profit (PF {pf}) but at {avg}% avg return "
                "the edge is too thin to survive realistic transaction costs. The 2025 regime "
                "was materially different from in-sample conditions.")
    else:
        verdict = "**NO — Strategy failed out-of-sample.**"
        expl = (f"The strategy lost money in 2025 (PF {pf}, avg return {avg}%). "
                "The in-sample results likely reflected favourable conditions that did not "
                "persist. This is a strong signal the strategy requires fundamental revision "
                "before any live deployment.")

    A(verdict)
    A("")
    A(expl)
    A("")

    # ── Section 2: Comparison Table ──────────────────────────────────────────
    A("## 2. 2025 vs 2022-2024 Comparison\n")
    A("| Metric | 2022-2024 (in-sample) | 2025 (out-of-sample) | Direction |")
    A("|--------|-----------------------|----------------------|-----------|")

    def dir_arrow(new, old, higher_is_better=True):
        if new is None or old is None:
            return "—"
        diff = new - old
        if abs(diff) < 0.01:
            return "→ flat"
        if higher_is_better:
            return "↑ better" if diff > 0 else "↓ worse"
        else:
            return "↓ better" if diff < 0 else "↑ worse"

    spy_pct = round(spy_return * 100, 1)
    rows = [
        ("Total trades",         BASELINE["total_trades"],      stats["total_trades"],       None),
        ("Win rate",             f"{BASELINE['win_rate']}%",    f"{wr}%",                    dir_arrow(wr, BASELINE["win_rate"])),
        ("Avg return / trade",   f"{BASELINE['avg_return_pct']}%", f"{avg}%",               dir_arrow(avg, BASELINE["avg_return_pct"])),
        ("Avg winner",           f"+{BASELINE['avg_winner_pct']}%", f"+{stats['avg_winner_pct']}%", dir_arrow(stats["avg_winner_pct"], BASELINE["avg_winner_pct"])),
        ("Avg loser",            f"{BASELINE['avg_loser_pct']}%",   f"{stats['avg_loser_pct']}%",  dir_arrow(abs(stats["avg_loser_pct"]), abs(BASELINE["avg_loser_pct"]), higher_is_better=False)),
        ("Profit factor",        BASELINE["profit_factor"],     stats["profit_factor"],      dir_arrow(pf, BASELINE["profit_factor"])),
        ("Max consec. losses",   BASELINE["max_consec_loss"],   stats["max_consec_loss"],    dir_arrow(stats["max_consec_loss"], BASELINE["max_consec_loss"], higher_is_better=False)),
        ("Avg holding days",     BASELINE["avg_holding_days"],  stats["avg_holding_days"],   None),
        ("SPY buy-and-hold",     f"{BASELINE['spy_return_pct']}%", f"{spy_pct}%",           None),
    ]
    for label, old, new, arrow in rows:
        arr = arrow if arrow is not None else "—"
        A(f"| {label} | {old} | {new} | {arr} |")
    A("")

    # ── Section 3: Full Trade Statistics ────────────────────────────────────
    A("## 3. Full Trade Statistics\n")
    A("| Metric | Value |")
    A("|--------|-------|")
    A(f"| Total trades | {stats['total_trades']} |")
    A(f"| Win rate | {wr}% |")
    A(f"| Avg return per trade | {avg}% |")
    A(f"| Median return per trade | {stats['median_return_pct']}% |")
    A(f"| Avg winner | +{stats['avg_winner_pct']}% |")
    A(f"| Avg loser | {stats['avg_loser_pct']}% |")
    A(f"| Profit factor | {pf} |")
    A(f"| Max consecutive losses | {stats['max_consec_loss']} |")
    A(f"| Avg holding period | {stats['avg_holding_days']} days |")
    A(f"| Total P&L (all positions) | ${stats['total_return_dollar']:,.0f} |")
    A(f"| Best trade | {stats['best_trade']} |")
    A(f"| Worst trade | {stats['worst_trade']} |")
    A(f"| SPY buy-and-hold 2025 | {spy_pct}% |")
    sharpe = compute_sharpe(df)
    if sharpe:
        A(f"| Approx. Sharpe ratio | {sharpe} |")
    A("")
    A("**Exit reason breakdown:**\n")
    er = stats["exit_reasons"]
    for reason, count in er.items():
        A(f"- {reason}: {count} ({round(count/stats['total_trades']*100,1)}%)")
    A("")

    # ── Section 4: Regime Analysis ──────────────────────────────────────────
    A("## 4. Regime Analysis (SPY vs 200-Day MA)\n")
    if "spy_bull_regime" in df.columns and df["spy_bull_regime"].notna().any():
        for regime_val, label in [(True, "Bull regime (SPY > 200MA)"),
                                   (False, "Bear regime (SPY < 200MA)")]:
            sub = df[df["spy_bull_regime"] == regime_val]
            if sub.empty:
                A(f"**{label}:** No trades.")
                continue
            sub_wr  = round((sub["return_pct"] > 0).mean() * 100, 1)
            sub_avg = round(sub["return_pct"].mean(), 2)
            sub_pf_wins = sub[sub["return_pct"] > 0]["return_dollar"].sum()
            sub_pf_loss = abs(sub[sub["return_pct"] <= 0]["return_dollar"].sum())
            sub_pf = round(sub_pf_wins / sub_pf_loss, 2) if sub_pf_loss > 0 else float("inf")
            A(f"**{label}** — {len(sub)} trades")
            A(f"- Win rate: {sub_wr}%")
            A(f"- Avg return: {sub_avg}%")
            A(f"- Profit factor: {sub_pf}")
            A("")
    else:
        A("*Regime data unavailable — SPY 200MA could not be computed.*\n")

    # ── Section 5: EPS Surprise Analysis ────────────────────────────────────
    A("## 5. EPS Surprise Analysis\n")
    if "surprise_pct" in df.columns and df["surprise_pct"].notna().any():
        A("| Surprise Group | Trades | Win Rate | Avg Return | Profit Factor |")
        A("|----------------|--------|----------|------------|---------------|")
        bins = [
            ("Small (0–5%)",   df[(df["surprise_pct"] >= 0) & (df["surprise_pct"] < 5)]),
            ("Medium (5–15%)", df[(df["surprise_pct"] >= 5) & (df["surprise_pct"] < 15)]),
            ("Large (>15%)",   df[df["surprise_pct"] >= 15]),
        ]
        for label, sub in bins:
            if sub.empty:
                A(f"| {label} | 0 | — | — | — |")
                continue
            sub_wr  = round((sub["return_pct"] > 0).mean() * 100, 1)
            sub_avg = round(sub["return_pct"].mean(), 2)
            sw = sub[sub["return_pct"] > 0]["return_dollar"].sum()
            sl = abs(sub[sub["return_pct"] <= 0]["return_dollar"].sum())
            sub_pf = round(sw / sl, 2) if sl > 0 else float("inf")
            A(f"| {label} | {len(sub)} | {sub_wr}% | {sub_avg}% | {sub_pf} |")
    else:
        A("*EPS surprise data unavailable for most trades.*\n")
    A("")

    # ── Section 6: Holding Period Analysis ──────────────────────────────────
    A("## 6. Holding Period Analysis\n")
    A("| Holding Group | Trades | Win Rate | Avg Return |")
    A("|---------------|--------|----------|------------|")
    hp_bins = [
        ("≤ 14 days (≤2 weeks)",     df[df["holding_days"] <= 14]),
        ("15–28 days (2–4 weeks)",   df[(df["holding_days"] > 14) & (df["holding_days"] <= 28)]),
        ("29–42 days (time stop)",   df[df["holding_days"] > 28]),
    ]
    for label, sub in hp_bins:
        if sub.empty:
            A(f"| {label} | 0 | — | — |")
            continue
        sub_wr  = round((sub["return_pct"] > 0).mean() * 100, 1)
        sub_avg = round(sub["return_pct"].mean(), 2)
        A(f"| {label} | {len(sub)} | {sub_wr}% | {sub_avg}% |")
    A("")

    # ── Section 7: Sector Breakdown ─────────────────────────────────────────
    A("## 7. Sector Breakdown\n")
    A("| Sector | Trades | Win Rate | Avg Return | Total P&L |")
    A("|--------|--------|----------|------------|-----------|")
    sect = df.groupby("sector").agg(
        trades=("return_pct", "count"),
        win_rate=("return_pct", lambda x: round((x > 0).mean() * 100, 1)),
        avg_ret=("return_pct", lambda x: round(x.mean(), 2)),
        total_pnl=("return_dollar", lambda x: round(x.sum(), 0)),
    ).sort_values("total_pnl", ascending=False)
    for sec, row in sect.iterrows():
        A(f"| {sec} | {row['trades']} | {row['win_rate']}% | {row['avg_ret']}% | ${row['total_pnl']:,.0f} |")
    A("")

    # ── Section 8: Best 10 Trades ────────────────────────────────────────────
    A("## 8. Best 10 Trades\n")
    A("| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |")
    A("|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|")
    for _, r in df.nlargest(10, "return_pct").iterrows():
        A(f"| {r['ticker']} | {r['sector']} | {r['entry_date']} | ${r['entry_price']} "
          f"| {r['exit_date']} | ${r['exit_price']} | +{r['return_pct']}% "
          f"| {r['holding_days']} | {r['exit_reason']} |")
    A("")

    # ── Section 9: Worst 10 Trades ───────────────────────────────────────────
    A("## 9. Worst 10 Trades\n")
    A("| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |")
    A("|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|")
    for _, r in df.nsmallest(10, "return_pct").iterrows():
        A(f"| {r['ticker']} | {r['sector']} | {r['entry_date']} | ${r['entry_price']} "
          f"| {r['exit_date']} | ${r['exit_price']} | {r['return_pct']}% "
          f"| {r['holding_days']} | {r['exit_reason']} |")
    A("")

    # ── Section 10: Key Findings ─────────────────────────────────────────────
    A("## 10. Key Findings\n")

    time_pct  = round(er.get("time",       0) / stats["total_trades"] * 100, 1)
    hard_pct  = round(er.get("hard_stop",  0) / stats["total_trades"] * 100, 1)
    trail_pct = round(er.get("trail_stop", 0) / stats["total_trades"] * 100, 1)

    avg_w = stats["avg_winner_pct"]
    avg_l = abs(stats["avg_loser_pct"])
    rr    = round(avg_w / avg_l, 2) if avg_l > 0 else "∞"

    A(f"- **vs 2022–2024 baseline:** Avg return shifted from +1.32% to {avg}%; "
      f"win rate from 54.8% to {wr}%; profit factor from 1.45 to {pf}.")
    A(f"- **Exit mix:** {hard_pct}% hard stop, {trail_pct}% trailing stop, "
      f"{time_pct}% time stop — "
      + ("similar exit profile to in-sample." if abs(hard_pct - 24.2) < 5 else
         "hard-stop rate changed meaningfully vs in-sample (24.2%), suggesting different volatility regime."))
    A(f"- **Reward/risk:** {avg_w}% avg winner vs {avg_l}% avg loser = {rr}:1.")
    A(f"- **SPY 2025:** {spy_pct}% buy-and-hold. "
      + ("Strategy alpha positive." if avg > 0 and pf > 1.0 else
         "Strategy underperformed passive SPY."))

    # Regime finding
    if "spy_bull_regime" in df.columns and df["spy_bull_regime"].notna().any():
        bull = df[df["spy_bull_regime"] == True]
        bear = df[df["spy_bull_regime"] == False]
        if not bull.empty and not bear.empty:
            bull_avg = round(bull["return_pct"].mean(), 2)
            bear_avg = round(bear["return_pct"].mean(), 2)
            A(f"- **Regime dependency:** Bull-regime trades averaged {bull_avg}% vs "
              f"bear-regime {bear_avg}%. "
              + ("Strategy works predominantly in bull conditions." if bull_avg > bear_avg + 1 else
                 "Performance relatively regime-agnostic." if abs(bull_avg - bear_avg) < 1 else
                 "Bear regime trades outperformed — strategy may be counter-trend."))

    # Surprise finding
    if "surprise_pct" in df.columns and df["surprise_pct"].notna().any():
        large = df[df["surprise_pct"] >= 15]
        small = df[(df["surprise_pct"] >= 0) & (df["surprise_pct"] < 5)]
        if not large.empty and not small.empty:
            large_avg = round(large["return_pct"].mean(), 2)
            small_avg = round(small["return_pct"].mean(), 2)
            A(f"- **Surprise magnitude:** Large beats (>15% surprise) averaged {large_avg}% "
              f"vs small beats (0-5%) at {small_avg}%. "
              + ("Filter for large beats could improve selectivity." if large_avg > small_avg + 0.5 else
                 "Surprise size does not significantly predict drift magnitude."))

    A(f"- **Survivorship bias** remains present (current S&P 500 constituents only).")
    A("")

    # ── Section 11: Recommendation ───────────────────────────────────────────
    A("## 11. Recommendation\n")
    A("*Based on combined in-sample (2022-2024) + out-of-sample (2025) evidence:*\n")

    if pf >= 1.4 and wr >= 52 and avg >= 1.0:
        rec = "**CONTINUE — Deploy the live bot.** Both in-sample and out-of-sample tests confirm a real edge."
        detail = (
            "The strategy passes the critical out-of-sample test with metrics that closely track the "
            "in-sample baseline. Recommend going live on the paper account with `DRY_RUN: false`, "
            "monitoring weekly. Priority enhancements: (1) add a guidance-raise filter using a premium "
            "data source to improve trade quality; (2) consider filtering for large EPS surprises (>15%) "
            "if the surprise-magnitude analysis shows meaningful separation."
        )
    elif pf >= 1.1 and avg >= 0.3:
        rec = "**CAUTIOUS CONTINUE — Paper-trade with monitoring before going live.**"
        detail = (
            "The strategy retained a positive edge out-of-sample but performance degraded. "
            "Continue paper trading and re-evaluate after 3 months of live data. "
            "Consider tightening filters: EPS surprise > 5%, or adding a momentum filter "
            "(price above 50MA at entry). Do not increase position size until metrics stabilize."
        )
    elif pf >= 1.0 and avg >= 0:
        rec = "**MODIFY — Tighten filters before any live use.**"
        detail = (
            "The edge is too thin (< transaction costs at realistic fill quality). "
            "Required changes before live deployment: (1) require EPS surprise > 10%; "
            "(2) require price above 50-day MA at entry; (3) consider raising the dollar-volume "
            "filter to $50M to reduce slippage. Re-backtest on 2022-2025 with new filters."
        )
    else:
        rec = "**STOP — Do not deploy. Strategy failed out-of-sample.**"
        detail = (
            "Positive in-sample results were not durable. The 2025 out-of-sample failure "
            "strongly suggests the 2022-2024 results reflected regime-specific conditions "
            "(post-COVID recovery + bull market) rather than a persistent PEAD edge. "
            "Fundamental strategy revision required before further testing."
        )

    A(rec)
    A("")
    A(detail)
    A("")
    A("---")
    A(f"\n*Backtest engine: yfinance + custom Python. Identical rules to 2022-2024 in-sample run. Not financial advice.*")

    return "\n".join(lines)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df, spy_return, regime_series = run_backtest()

    if df.empty:
        print("No trades generated. Check earnings data availability for 2025.")
        sys.exit(1)

    stats = compute_stats(df)

    print("\n=== 2025 OUT-OF-SAMPLE STATS ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    report = build_report(df, spy_return, stats)

    report_path = os.path.join(_REPORTS_DIR, "backtest_report_PEAD_2025_OOS.md")
    trades_path = os.path.join(_REPORTS_DIR, "backtest_trades_PEAD_2025_OOS.csv")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    df.to_csv(trades_path, index=False)

    print(f"\nReport saved:     {report_path}")
    print(f"Trade log saved:  {trades_path}")
    print(f"\n--- QUICK SUMMARY ---")
    print(f"  Trades:         {stats['total_trades']}")
    print(f"  Win rate:       {stats['win_rate']}%")
    print(f"  Avg return:     {stats['avg_return_pct']}%")
    print(f"  Profit factor:  {stats['profit_factor']}")
    print(f"  SPY 2025:       {round(spy_return*100,1)}%")
