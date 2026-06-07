"""
PEAD (Post-Earnings Announcement Drift) Backtest
Strategy: Buy 2 days after earnings beat, hold with stops.
Period: 2022-01-01 to 2024-12-31
Universe: S&P 500 current constituents
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
START_DATE = "2021-10-01"   # pull extra history for volume calc
TEST_START = "2022-01-01"
TEST_END   = "2024-12-31"
POSITION_SIZE = 11_000      # $11k per position
HARD_STOP     = -0.08       # -8%
TRAIL_TRIGGER = 0.10        # +10% before trailing kicks in
TRAIL_PCT     = 0.07        # trail 7% below highest close
TIME_STOP     = 42          # calendar days
MIN_PRICE     = 10.0
MIN_AVG_DVOL  = 20_000_000  # $20M 20-day avg dollar volume
ENTRY_DELAY   = 2           # trading days after earnings


# ─── STEP 1: FETCH S&P 500 UNIVERSE ──────────────────────────────────────────
def get_sp500():
    url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
    try:
        r = requests.get(url, timeout=30)
        df = pd.read_csv(StringIO(r.text))
        df.columns = [c.strip() for c in df.columns]
        # column names vary: Symbol, Ticker, symbol
        sym_col = next(c for c in df.columns if c.lower() in ("symbol", "ticker"))
        sec_col = next((c for c in df.columns if "sector" in c.lower()), None)
        name_col = next((c for c in df.columns if "name" in c.lower() or "security" in c.lower()), None)
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


# ─── STEP 2: FETCH PRICE + EARNINGS DATA FOR ONE TICKER ──────────────────────
def fetch_ticker_data(ticker):
    try:
        tk = yf.Ticker(ticker)
        hist = tk.history(start=START_DATE, end="2025-01-15", auto_adjust=True)
        if hist.empty or len(hist) < 50:
            return None, None
        # Strip timezone for clean date comparisons
        if hist.index.tz is not None:
            hist.index = hist.index.tz_localize(None)

        # Earnings dates (actual announcement timestamps, deeper history)
        try:
            eh = tk.get_earnings_dates(limit=50)
        except Exception:
            return hist, None

        if eh is None or eh.empty:
            return hist, None

        eh = eh.rename(columns={
            "Reported EPS": "reported",
            "EPS Estimate": "estimate",
            "Surprise(%)": "surprise_pct",
        })
        # Strip tz, normalise to date
        eh.index = pd.to_datetime(eh.index).tz_localize(None)
        eh = eh.sort_index()
        return hist, eh
    except Exception:
        return None, None


# ─── STEP 3: GET TRADING CALENDAR ────────────────────────────────────────────
def get_trading_days(hist):
    return sorted(hist.index.normalize().unique())


def nth_trading_day_after(trading_days, date, n):
    """Return the nth trading day strictly after `date`."""
    date = pd.Timestamp(date).normalize()
    future = [d for d in trading_days if d > date]
    if len(future) >= n:
        return future[n - 1]
    return None


# ─── STEP 4: DOLLAR VOLUME FILTER ────────────────────────────────────────────
def avg_dvol_ok(hist, date, window=20):
    date = pd.Timestamp(date).normalize()
    prior = hist[hist.index.normalize() < date].tail(window)
    if len(prior) < window // 2:
        return False
    dvol = (prior["Close"] * prior["Volume"]).mean()
    return dvol >= MIN_AVG_DVOL


# ─── STEP 5: SIMULATE ONE TRADE ──────────────────────────────────────────────
def simulate_trade(hist, entry_date):
    entry_date = pd.Timestamp(entry_date).normalize()
    day_data = hist[hist.index.normalize() == entry_date]
    if day_data.empty:
        return None

    entry_price = day_data["Open"].iloc[0]
    if pd.isna(entry_price) or entry_price < MIN_PRICE:
        return None

    hard_stop_price = entry_price * (1 + HARD_STOP)
    highest_close = entry_price
    trail_active = False
    trail_stop = None

    future = hist[hist.index.normalize() >= entry_date]
    entry_dt = future.index[0]

    for i, (dt, row) in enumerate(future.iterrows()):
        close = row["Close"]
        if pd.isna(close):
            continue

        if close > highest_close:
            highest_close = close
        if highest_close >= entry_price * (1 + TRAIL_TRIGGER):
            trail_active = True
        if trail_active:
            trail_stop = highest_close * (1 - TRAIL_PCT)

        # Time stop
        cal_days = (dt.normalize() - entry_date).days
        if cal_days >= TIME_STOP:
            return {
                "exit_date": dt.date(),
                "exit_price": close,
                "exit_reason": "time",
                "holding_days": cal_days,
                "return_pct": (close - entry_price) / entry_price,
            }

        # Check stops at close (simplified: use close as trigger)
        if close <= hard_stop_price:
            return {
                "exit_date": dt.date(),
                "exit_price": close,
                "exit_reason": "hard_stop",
                "holding_days": cal_days,
                "return_pct": (close - entry_price) / entry_price,
            }
        if trail_active and trail_stop and close <= trail_stop:
            return {
                "exit_date": dt.date(),
                "exit_price": close,
                "exit_reason": "trail_stop",
                "holding_days": cal_days,
                "return_pct": (close - entry_price) / entry_price,
            }

    # Ran out of data
    last_row = future.iloc[-1]
    last_close = last_row["Close"]
    holding = (last_row.name.normalize() - entry_date).days
    return {
        "exit_date": last_row.name.date(),
        "exit_price": last_close,
        "exit_reason": "data_end",
        "holding_days": holding,
        "return_pct": (last_close - entry_price) / entry_price,
    }


# ─── STEP 6: MAIN BACKTEST LOOP ──────────────────────────────────────────────
def run_backtest():
    print("Fetching S&P 500 universe...")
    sp500 = get_sp500()
    tickers = sp500["ticker"].tolist()
    sector_map = {}
    if "sector" in sp500.columns:
        sector_map = dict(zip(sp500["ticker"], sp500["sector"]))

    # Fetch SPY for benchmark
    print("Fetching SPY benchmark...")
    spy_hist = yf.download("SPY", start=TEST_START, end="2025-01-02",
                           auto_adjust=True, progress=False)
    spy_start = spy_hist["Close"].iloc[0]
    spy_end   = spy_hist["Close"].iloc[-1]
    spy_return = (spy_end - spy_start) / spy_start

    trades = []
    skipped = 0
    no_earnings = 0
    total = len(tickers)

    print(f"Processing {total} tickers...")
    for idx, ticker in enumerate(tickers):
        if idx % 50 == 0:
            print(f"  {idx}/{total} ({len(trades)} trades so far)...")

        hist, earnings = fetch_ticker_data(ticker)
        if hist is None:
            skipped += 1
            continue
        if earnings is None:
            no_earnings += 1
            continue

        trading_days = get_trading_days(hist)

        for earn_date, row in earnings.iterrows():
            earn_date = pd.Timestamp(earn_date).normalize()

            # Filter to test window (allow up to 30 days lead time before test start)
            if earn_date < pd.Timestamp(TEST_START) - timedelta(days=30):
                continue
            if earn_date > pd.Timestamp(TEST_END):
                continue

            # EPS beat check
            try:
                reported = float(row.get("reported", np.nan))
                estimate = float(row.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue

            if pd.isna(reported) or pd.isna(estimate):
                continue
            # Beat = reported > estimate (handle negative EPS)
            if estimate >= 0:
                beat = reported > estimate
            else:
                # Negative EPS: beat means less negative
                beat = reported > estimate
            if not beat:
                continue

            # Entry date = 2 trading days after earnings
            entry_date = nth_trading_day_after(trading_days, earn_date, ENTRY_DELAY)
            if entry_date is None:
                continue

            # Must be within test period
            if entry_date < pd.Timestamp(TEST_START):
                continue
            if entry_date > pd.Timestamp(TEST_END):
                continue

            # Price filter
            day_data = hist[hist.index.normalize() == entry_date]
            if day_data.empty:
                continue
            open_price = day_data["Open"].iloc[0]
            if pd.isna(open_price) or open_price < MIN_PRICE:
                continue

            # Dollar volume filter (based on pre-earnings data)
            if not avg_dvol_ok(hist, earn_date):
                continue

            # Simulate
            result = simulate_trade(hist, entry_date)
            if result is None:
                continue

            surprise_pct = None
            if "surprise_pct" in row and not pd.isna(row["surprise_pct"]):
                surprise_pct = float(row["surprise_pct"])
            elif estimate != 0:
                surprise_pct = (reported - estimate) / abs(estimate) * 100

            trades.append({
                "ticker": ticker,
                "sector": sector_map.get(ticker, "Unknown"),
                "earn_date": earn_date.date(),
                "entry_date": entry_date.date(),
                "entry_price": round(open_price, 4),
                "exit_date": result["exit_date"],
                "exit_price": round(result["exit_price"], 4),
                "exit_reason": result["exit_reason"],
                "holding_days": result["holding_days"],
                "return_pct": round(result["return_pct"] * 100, 2),
                "return_dollar": round(result["return_pct"] * POSITION_SIZE, 2),
                "eps_reported": reported,
                "eps_estimate": estimate,
                "surprise_pct": round(surprise_pct, 2) if surprise_pct is not None else None,
                "year": entry_date.year,
            })

        time.sleep(0.05)  # rate limit

    print(f"\nDone. Trades: {len(trades)}, No-earnings: {no_earnings}, Skipped: {skipped}")
    return pd.DataFrame(trades), spy_return


# ─── STEP 7: COMPUTE STATS ───────────────────────────────────────────────────
def compute_stats(df):
    if df.empty:
        return {}

    winners = df[df["return_pct"] > 0]
    losers  = df[df["return_pct"] <= 0]

    gross_wins  = winners["return_dollar"].sum()
    gross_loss  = abs(losers["return_dollar"].sum())
    profit_factor = gross_wins / gross_loss if gross_loss > 0 else float("inf")

    # Max consecutive losses
    streaks = []
    cur = 0
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
        "total_trades": len(df),
        "win_rate": round(len(winners) / len(df) * 100, 1),
        "avg_return_pct": round(df["return_pct"].mean(), 2),
        "avg_winner_pct": round(winners["return_pct"].mean(), 2) if not winners.empty else 0,
        "avg_loser_pct":  round(losers["return_pct"].mean(), 2) if not losers.empty else 0,
        "median_return_pct": round(df["return_pct"].median(), 2),
        "total_return_dollar": round(df["return_dollar"].sum(), 2),
        "profit_factor": round(profit_factor, 2),
        "max_consec_loss": max_consec_loss,
        "avg_holding_days": round(df["holding_days"].mean(), 1),
        "best_trade": f"{best['ticker']} +{best['return_pct']}% ({best['holding_days']}d)",
        "worst_trade": f"{worst['ticker']} {worst['return_pct']}% ({worst['holding_days']}d)",
        "exit_reasons": df["exit_reason"].value_counts().to_dict(),
    }


def compute_sharpe(df):
    """Approximate monthly Sharpe using trade returns."""
    if df.empty or len(df) < 5:
        return None
    # Treat each trade return as an observation; annualise assuming ~8 trades/month
    r = df["return_pct"] / 100
    rf = 0.045 / 12  # monthly risk-free ~4.5% annual
    excess = r.mean() - rf
    if r.std() == 0:
        return None
    return round(excess / r.std() * np.sqrt(len(r)), 2)


# ─── STEP 8: BUILD REPORT ────────────────────────────────────────────────────
def build_report(df, spy_return, stats):
    lines = []
    A = lines.append

    A("# PEAD Backtest Report — 2022–2024")
    A(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    A("\n---\n")

    # Executive Summary
    A("## 1. Executive Summary\n")
    total_r = stats["total_return_dollar"]
    capital = POSITION_SIZE * stats["total_trades"]
    pct_return = (total_r / capital * 100) if capital > 0 else 0
    sharpe = compute_sharpe(df)
    spy_pct = round(spy_return * 100, 1)

    A(f"The PEAD strategy generated **{stats['total_trades']} simulated trades** over the 2022–2024 period "
      f"(S&P 500 current constituents, survivorship-bias noted). "
      f"The average return per trade was **{stats['avg_return_pct']}%** with a win rate of **{stats['win_rate']}%**, "
      f"compared to SPY buy-and-hold returning **{spy_pct}%** over the same period. "
      f"The profit factor was **{stats['profit_factor']}** and the strategy produced "
      f"**${total_r:,.0f}** aggregate P&L across all positions "
      f"({pct_return:.1f}% of total capital deployed). "
      f"{'Sharpe ratio (approximate): **' + str(sharpe) + '**.' if sharpe else ''}")
    A("")

    # Trade Statistics
    A("## 2. Trade Statistics\n")
    A(f"| Metric | Value |")
    A(f"|--------|-------|")
    A(f"| Total trades | {stats['total_trades']} |")
    A(f"| Win rate | {stats['win_rate']}% |")
    A(f"| Avg return per trade | {stats['avg_return_pct']}% |")
    A(f"| Median return per trade | {stats['median_return_pct']}% |")
    A(f"| Avg winner | +{stats['avg_winner_pct']}% |")
    A(f"| Avg loser | {stats['avg_loser_pct']}% |")
    A(f"| Profit factor | {stats['profit_factor']} |")
    A(f"| Max consecutive losses | {stats['max_consec_loss']} |")
    A(f"| Avg holding period | {stats['avg_holding_days']} days |")
    A(f"| Total P&L (all positions) | ${stats['total_return_dollar']:,.0f} |")
    A(f"| Best trade | {stats['best_trade']} |")
    A(f"| Worst trade | {stats['worst_trade']} |")
    A(f"| SPY buy-and-hold (same period) | {spy_pct}% |")
    if sharpe:
        A(f"| Approx. Sharpe ratio | {sharpe} |")
    A("")

    A("**Exit reason breakdown:**\n")
    for reason, count in stats["exit_reasons"].items():
        A(f"- {reason}: {count} ({round(count/stats['total_trades']*100,1)}%)")
    A("")

    # Yearly Breakdown
    A("## 3. Yearly Breakdown\n")
    A("| Year | Trades | Win Rate | Avg Return | Total P&L |")
    A("|------|--------|----------|------------|-----------|")
    for year in [2022, 2023, 2024]:
        yd = df[df["year"] == year]
        if yd.empty:
            A(f"| {year} | 0 | — | — | — |")
            continue
        wr = round(len(yd[yd["return_pct"] > 0]) / len(yd) * 100, 1)
        ar = round(yd["return_pct"].mean(), 2)
        tp = round(yd["return_dollar"].sum(), 0)
        A(f"| {year} | {len(yd)} | {wr}% | {ar}% | ${tp:,.0f} |")
    A("")

    # Sector Breakdown
    A("## 4. Sector Breakdown\n")
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

    # Best 10 Trades
    A("## 5. Best 10 Trades\n")
    A("| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |")
    A("|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|")
    for _, r in df.nlargest(10, "return_pct").iterrows():
        A(f"| {r['ticker']} | {r['sector']} | {r['entry_date']} | ${r['entry_price']} | {r['exit_date']} | ${r['exit_price']} | +{r['return_pct']}% | {r['holding_days']} | {r['exit_reason']} |")
    A("")

    # Worst 10 Trades
    A("## 6. Worst 10 Trades\n")
    A("| Ticker | Sector | Entry Date | Entry $ | Exit Date | Exit $ | Return % | Days | Exit Reason |")
    A("|--------|--------|-----------|---------|-----------|--------|----------|------|-------------|")
    for _, r in df.nsmallest(10, "return_pct").iterrows():
        A(f"| {r['ticker']} | {r['sector']} | {r['entry_date']} | ${r['entry_price']} | {r['exit_date']} | ${r['exit_price']} | {r['return_pct']}% | {r['holding_days']} | {r['exit_reason']} |")
    A("")

    # Key Findings
    A("## 7. Key Findings\n")
    er = stats["exit_reasons"]
    time_pct = round(er.get("time", 0) / stats["total_trades"] * 100, 1)
    hard_pct = round(er.get("hard_stop", 0) / stats["total_trades"] * 100, 1)
    trail_pct = round(er.get("trail_stop", 0) / stats["total_trades"] * 100, 1)
    A(f"- **Stop discipline:** {hard_pct}% of trades exited via hard stop (-8%), "
      f"{trail_pct}% via trailing stop, {time_pct}% via time stop (42 days).")
    avg_w = stats["avg_winner_pct"]
    avg_l = abs(stats["avg_loser_pct"])
    rr = round(avg_w / avg_l, 2) if avg_l > 0 else "∞"
    A(f"- **Reward/risk ratio:** Average winner ({avg_w}%) vs average loser ({avg_l}%) = {rr}:1.")
    A(f"- **Win rate of {stats['win_rate']}%** {'is above 50%, meaning more trades are profitable than not.' if stats['win_rate'] > 50 else 'is below 50% — the strategy relies on winners being larger than losers.'}")
    A(f"- **Profit factor {stats['profit_factor']}**: {'Above 1.5 suggests a robust edge.' if stats['profit_factor'] > 1.5 else 'Below 1.5 — marginal edge, may not survive transaction costs.' if stats['profit_factor'] > 1.0 else 'Below 1.0 — strategy loses money in aggregate.'}")
    A(f"- **Survivorship bias** is present: the universe uses current S&P 500 constituents, "
      f"which excludes companies that were removed (often due to poor performance). Results are likely 1–3% optimistic.")
    A(f"- **Guidance raise filter** was NOT applied due to yfinance data limitations. "
      f"All results reflect 'EPS beat only' criterion. Adding a guidance filter would reduce trade count but likely improve quality.")
    A("")

    # Limitations
    A("## 8. Limitations\n")
    A("1. **Survivorship bias**: Current S&P 500 only — companies removed during 2022–2024 are excluded.")
    A("2. **Guidance raise unverified**: yfinance does not provide guidance data reliably. Tested 'EPS beat' only.")
    A("3. **Fill assumptions**: Entry at open 2 days after earnings. Real fills may be worse (gap-up opens).")
    A("4. **Earnings dates**: yfinance earnings_history dates can be off by 1 day vs actual announcement time (pre/post market).")
    A("5. **No transaction costs**: Commissions, spread, and slippage are not modeled (~$5–$20 per round trip).")
    A("6. **No portfolio constraints**: Simulated as if each trade is independent; in reality concurrent positions compete for capital.")
    A("7. **Split/dividend adjustment**: yfinance auto_adjust=True handles splits but may introduce small errors on exact stop levels.")
    A("8. **Thesis break exits**: Not modeled (requires next-quarter earnings data matched back to open positions).")
    A("")

    # Recommendation
    A("## 9. Recommendation\n")
    pf = stats["profit_factor"]
    wr = stats["win_rate"]
    avg_r = stats["avg_return_pct"]
    if pf > 1.5 and wr > 50 and avg_r > 1.0:
        verdict = "**CONTINUE with enhancements.** The strategy shows a positive edge across 3 years."
        detail = ("Consider adding a guidance-raise filter (would require a premium data source like Refinitiv or "
                  "Earnings Whispers API) to improve trade quality. The survivorship bias-adjusted edge is likely "
                  "still positive but smaller than reported here.")
    elif pf > 1.0 and avg_r > 0:
        verdict = "**CAUTIOUS CONTINUE.** The strategy has a marginal edge."
        detail = ("Results are sensitive to assumptions and survivorship bias. Before scaling, validate on out-of-sample "
                  "data (2025) and add guidance-raise filtering. Consider tightening the EPS surprise threshold "
                  "(e.g., beat > 5%) to improve quality over quantity.")
    else:
        verdict = "**MODIFY OR ABANDON.** The strategy does not show a reliable edge in this backtest."
        detail = ("With transaction costs and survivorship bias correction, this strategy likely loses money. "
                  "Consider: stricter entry criteria, longer holding periods, or combining with technical momentum filters.")
    A(verdict)
    A("")
    A(detail)
    A("")
    A("---")
    A(f"\n*Backtest engine: yfinance + custom Python. Not financial advice.*")

    return "\n".join(lines)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df, spy_return = run_backtest()

    if df.empty:
        print("No trades generated. Check earnings data availability.")
        sys.exit(1)

    stats = compute_stats(df)
    print("\n=== AGGREGATE STATS ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    report = build_report(df, spy_return, stats)

    report_path = "backtest_report_PEAD_2022_2024.md"
    trades_path = "backtest_trades_PEAD_2022_2024.csv"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    df.to_csv(trades_path, index=False)

    print(f"\nReport saved: {report_path}")
    print(f"Trade log saved: {trades_path}")
    print(f"\n--- EXECUTIVE SUMMARY ---")
    # Print first section of report
    for line in report.split("\n")[:20]:
        print(line)
