"""
compute_pead_health.py — produce memory/pead_health.md for the live AND gate.

Run weekly by routines/universe_refresh.md. Computes the two gate components that
were validated in the 2022-2026 backtests (see backtest_report_PEAD_HEALTH_200MA_COMBO.md):

  1. REALIZED SIGNAL HEALTH — the trailing-60d mean return of S&P 500 "BASE" PEAD
     trades (buy 2 trading days after an EPS beat, exit on -8% stop / 7% trailing
     stop after +10% / 42-day time stop) that have ALREADY EXITED. Measures whether
     post-earnings drift is currently paying, INDEPENDENT of the index — so it can
     flag a weak tape even while SPY is in a bull regime (the 2026 case).
  2. SPY 200-DAY REGIME — SPY close vs its 200-day moving average. Fast bear-turn
     protection (the 2022 case that realized-health lags on).

GATE = RISK_ON  iff  (SPY > 200MA)  AND  (realized_health >= 0)        [logical AND]
       RISK_OFF otherwise.
On thin data (< MIN_SAMPLE realized trades) the health leg defaults to OK
(fail-open) — only the SPY leg can flip the gate in that case.

Data source: yfinance (same source the gate was calibrated on). Writes the file
atomically. Exits non-zero on hard failure so universe_refresh can surface it.
"""

import sys
import os
import time
import argparse
from datetime import datetime, timedelta, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import pandas as pd
import yfinance as yf

import backtest_pead_2026_ytd as eng

# ─── gate parameters (frozen from the validated backtest) ─────────────────────
HEALTH_WINDOW_DAYS = 60       # realized trades must have EXITED within this trailing window
EARN_LOOKBACK_DAYS = 110      # scan earnings this far back (entry + 42d time-stop must fit)
MIN_SAMPLE         = 20       # < this many realized trades -> health leg fails OPEN
HEALTH_THRESHOLD   = 0.0      # realized mean return % must be >= this
BASE_TRAIL_PCT     = 0.07     # BASE PEAD trade uses the 7% trailing stop
OUT_PATH_DEFAULT   = os.path.join("memory", "pead_health.md")


def robust_spy(start, end):
    for attempt in range(5):
        spy = yf.download("SPY", start=start, end=end, auto_adjust=True, progress=False)
        if isinstance(spy.columns, pd.MultiIndex):
            spy.columns = spy.columns.get_level_values(0)
        if not spy.empty and "Close" in spy.columns and spy["Close"].notna().sum() > 200:
            return spy
        print(f"  SPY attempt {attempt+1} insufficient; retrying...")
        time.sleep(3)
    raise RuntimeError("SPY download failed after 5 retries")


def compute(run_date):
    today = pd.Timestamp(run_date).normalize()
    eng.HIST_START = (today - timedelta(days=400)).strftime("%Y-%m-%d")
    eng.DATA_END   = (today + timedelta(days=1)).strftime("%Y-%m-%d")

    # ── SPY 200MA leg ─────────────────────────────────────────────────────────
    print("SPY 200MA...")
    spy = robust_spy((today - timedelta(days=400)).strftime("%Y-%m-%d"),
                     (today + timedelta(days=1)).strftime("%Y-%m-%d"))
    spy_close_s = spy["Close"].dropna()
    spy_close = float(spy_close_s.iloc[-1])
    spy_200ma = float(spy_close_s.rolling(200, min_periods=100).mean().iloc[-1])
    spy_above = spy_close > spy_200ma

    # ── realized signal-health leg ────────────────────────────────────────────
    print("Signal health (S&P 500 trailing PEAD outcomes)...")
    sp500 = eng.get_sp500()
    tickers = sp500["ticker"].tolist()
    earn_floor = today - timedelta(days=EARN_LOOKBACK_DAYS)
    exit_floor = today - timedelta(days=HEALTH_WINDOW_DAYS)

    returns = []
    scanned = 0
    for i, t in enumerate(tickers):
        if i % 100 == 0:
            print(f"  {i}/{len(tickers)} ({len(returns)} realized trades)...")
        hist, earn = eng.fetch_ticker_data(t)
        if hist is None or earn is None:
            continue
        td = eng.get_trading_days(hist)
        for ed, er in earn.iterrows():
            ed = pd.Timestamp(ed).normalize()
            if ed < earn_floor or ed > today:
                continue
            try:
                rep = float(er.get("reported", np.nan)); est = float(er.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(rep) or pd.isna(est) or not (rep > est):
                continue
            en = eng.nth_trading_day_after(td, ed, eng.ENTRY_DELAY)
            if en is None or en > today:
                continue
            dd = hist[hist.index == en]
            if dd.empty:
                continue
            op = dd["Open"].iloc[0]
            if pd.isna(op) or op < eng.MIN_PRICE or not eng.avg_dvol_ok(hist, ed):
                continue
            res = eng.simulate_trade(hist, en, BASE_TRAIL_PCT)
            if res is None or res["exit_reason"] == "data_end":
                continue                                  # still open -> not realized
            xd = pd.Timestamp(res["exit_date"])
            if xd < exit_floor or xd > today:
                continue                                  # exited outside the trailing window
            returns.append(res["return_pct"] * 100)
            scanned += 1
        time.sleep(0.02)

    n = len(returns)
    health = float(np.mean(returns)) if n >= MIN_SAMPLE else None
    health_ok = (health is None) or (health >= HEALTH_THRESHOLD)
    gate = "RISK_ON" if (spy_above and health_ok) else "RISK_OFF"

    return {
        "computed_on": today.strftime("%Y-%m-%d"),
        "expires_on": (today + timedelta(days=7)).strftime("%Y-%m-%d"),
        "gate": gate,
        "spy_close": round(spy_close, 2),
        "spy_200ma": round(spy_200ma, 2),
        "spy_above_200ma": bool(spy_above),
        "realized_health_60d_pct": (round(health, 3) if health is not None else None),
        "health_sample_n": n,
        "health_threshold_pct": HEALTH_THRESHOLD,
        "health_ok": bool(health_ok),
        "window_days": HEALTH_WINDOW_DAYS,
        "min_sample": MIN_SAMPLE,
    }


def render(d):
    hv = "null" if d["realized_health_60d_pct"] is None else d["realized_health_60d_pct"]
    fm = [
        "---",
        f"computed_on: {d['computed_on']}",
        f"expires_on: {d['expires_on']}",
        f"gate: {d['gate']}",
        f"spy_close: {d['spy_close']}",
        f"spy_200ma: {d['spy_200ma']}",
        f"spy_above_200ma: {str(d['spy_above_200ma']).lower()}",
        f"realized_health_60d_pct: {hv}",
        f"health_sample_n: {d['health_sample_n']}",
        f"health_threshold_pct: {d['health_threshold_pct']}",
        f"health_ok: {str(d['health_ok']).lower()}",
        f"window_days: {d['window_days']}",
        f"min_sample: {d['min_sample']}",
        "source: yfinance",
        "---",
        "",
        "# PEAD signal-health gate",
        "",
        "Weekly snapshot of whether the post-earnings-drift edge is currently \"on\". "
        "**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed "
        "read-only by `pre_market` as the **AND gate** on NEW entries. It never blocks exits.",
        "",
        "## The gate",
        "",
        "```",
        "RISK_ON  iff  (spy_above_200ma == true)  AND  (health_ok == true)",
        "RISK_OFF otherwise",
        "```",
        "",
        "- **SPY 200-day regime** — fast bear-turn protection.",
        "- **Realized signal health** — trailing-"
        f"{d['window_days']}d mean return of S&P 500 EPS-beat PEAD trades that have already "
        "exited (buy +2 days after beat; -8% stop / 7% trail / 42d time stop). Measures the "
        "drift edge directly, so it can read RISK_OFF even in a bull market (the 2026 case).",
        f"- `health_ok` is true when `realized_health_60d_pct >= {d['health_threshold_pct']}` "
        f"OR fewer than {d['min_sample']} realized trades exist (fail-open on thin data — only "
        "the SPY leg can flip the gate then).",
        "",
        "## Current reading",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Gate | **{d['gate']}** |",
        f"| SPY close | {d['spy_close']} |",
        f"| SPY 200MA | {d['spy_200ma']} |",
        f"| SPY > 200MA | {str(d['spy_above_200ma']).lower()} |",
        f"| Realized health (trailing {d['window_days']}d) | {hv}% |",
        f"| Health sample size | {d['health_sample_n']} |",
        f"| Health OK (>= {d['health_threshold_pct']}%) | {str(d['health_ok']).lower()} |",
        "",
        "Validated in `backtest_report_PEAD_HEALTH_200MA_COMBO.md`: the AND combo gave the "
        "best risk-adjusted result (PF 1.60 → 1.99) and the strongest regime discrimination "
        "(+57 pts). Threshold is 0 (untuned). Known limitation: realized health lags at "
        "regime TURNS, so the gate can stay RISK_OFF a little into a fresh recovery.",
    ]
    return "\n".join(fm) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    help="run date YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--out", default=OUT_PATH_DEFAULT)
    args = ap.parse_args()

    try:
        data = compute(args.date)
    except Exception as e:
        print(f"[FATAL] pead_health computation failed: {e}", file=sys.stderr)
        sys.exit(1)

    text = render(data)
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    tmp = args.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, args.out)                              # atomic
    print(f"\nWrote {args.out}")
    print(f"  GATE={data['gate']}  spy_above_200ma={data['spy_above_200ma']}  "
          f"health={data['realized_health_60d_pct']}% (n={data['health_sample_n']})")


if __name__ == "__main__":
    main()
