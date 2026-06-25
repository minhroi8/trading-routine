"""
PEAD signal-health gate — detects when the post-earnings-drift signal itself is
weak, INCLUDING in bull markets (unlike a SPY>200MA regime filter).

Idea
----
The strategy's fortunes are dominated by whether PEAD is "paying" right now. We
measure that directly from the broad EPS-beat (BASE) population — NOT from SPY —
using only information known at the moment of each entry (strict point-in-time,
no lookahead). Two health signals, both as-of entry date D:

  HEALTH_REALIZED : mean return of BASE trades whose EXIT date falls in [D-L_real, D).
                    Complete but laggy (a trade can take up to 42 days to resolve).
  HEALTH_DRIFT    : mean of the first-5-trading-day post-entry return of BASE entries
                    whose +5d mark is < D, entered in [D-L_drift, D).
                    Faster warning — catches fading drift before full exits resolve.

Gate: take an (enhanced) trade only if the chosen health signal >= threshold.
If the trailing window has < MIN_N samples, default to ALLOW (don't block on
thin data — only the very start of the sample is affected).

We then check the property that matters: does the gate cut HOSTILE years
(2022, 2026 YTD) much more than FAVOURABLE years (2023-2025)?
"""

import os
import time
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 console chokes on → ✓ ⛔
except Exception:
    pass
import pandas as pd
import numpy as np
from datetime import timedelta

import yfinance as yf

# --- Path anchoring (research artifacts consolidated under backtesting/) ------
# Engine backtest_pead_2026_ytd.py stays at the repo root (production
# compute_pead_health.py imports it); add the repo root to sys.path so the bare
# import below resolves. Reports/candidate CSVs resolve relative to this file.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
_REPORTS_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "reports"))

import backtest_pead_2026_ytd as eng
from backtest_validate_filters_2022_2025 import cached_fetch, robust_spy

eng.HIST_START = "2020-06-01"
eng.DATA_END   = "2026-06-05"
BUILD_START = "2021-01-01"     # warm-up so the health window is populated by 2022
EVAL_START  = "2022-01-01"     # only evaluate/report gated results from here
SCAN_END    = "2026-06-04"
P = eng.POSITION_SIZE

L_REAL  = 60      # calendar-day lookback for realized health
L_DRIFT = 35      # calendar-day lookback for drift health
MIN_N   = 25      # minimum samples in window, else ALLOW
DRIFT_DAYS = 5    # trading days for the early-drift measure


def ret_n_days(hist, entry_date, n):
    """Return (ret over first n trading days from entry open, date it becomes known)."""
    fut = hist[hist.index >= entry_date]
    if len(fut) <= n:
        return None, None
    op = fut["Open"].iloc[0]
    if pd.isna(op) or op == 0:
        return None, None
    px = fut["Close"].iloc[n]
    return (px - op) / op, fut.index[n]


def build():
    sp500 = eng.get_sp500()
    tickers = sp500["ticker"].tolist()
    sector_map = dict(zip(sp500["ticker"], sp500["sector"]))
    print("SPY...")
    spy_close, regime = eng.build_spy(robust_spy())
    assert spy_close.notna().sum() > 200

    rows = []
    for i, t in enumerate(tickers):
        if i % 100 == 0:
            print(f"  {i}/{len(tickers)} ({len(rows)})...")
        hist, earn = cached_fetch(t)
        if hist is None or earn is None:
            continue
        td = eng.get_trading_days(hist)
        is_it = (sector_map.get(t) == eng.IT_SECTOR)
        # Precompute 52-wk-high flag ONCE per ticker (was the per-candidate bottleneck)
        roll252 = hist["High"].rolling(252, min_periods=120).max()
        is_high = (hist["High"] >= roll252 * 0.999)
        for ed, er in earn.iterrows():
            ed = pd.Timestamp(ed).normalize()
            if ed < pd.Timestamp(BUILD_START) - timedelta(days=30) or ed > pd.Timestamp(SCAN_END):
                continue
            try:
                rep = float(er.get("reported", np.nan)); est = float(er.get("estimate", np.nan))
            except (ValueError, TypeError):
                continue
            if pd.isna(rep) or pd.isna(est) or not (rep > est):
                continue
            en = eng.nth_trading_day_after(td, ed, eng.ENTRY_DELAY)
            if en is None or en < pd.Timestamp(BUILD_START) or en > pd.Timestamp(SCAN_END):
                continue
            dd = hist[hist.index == en]
            if dd.empty:
                continue
            op = dd["Open"].iloc[0]
            if pd.isna(op) or op < eng.MIN_PRICE or not eng.avg_dvol_ok(hist, ed):
                continue
            r7 = eng.simulate_trade(hist, en, 0.07)
            r12 = eng.simulate_trade(hist, en, 0.12)
            if r7 is None:
                continue
            ret5, ret5_known = ret_n_days(hist, en, DRIFT_DAYS)
            surprise = None
            if "surprise_pct" in er and not pd.isna(er["surprise_pct"]):
                surprise = float(er["surprise_pct"])
            elif est != 0:
                surprise = (rep - est) / abs(est) * 100
            vr = eng.vol_ratio_on_day(hist, ed)
            rs = eng.rel_strength_vs_spy(hist, spy_close, ed, en)
            cutoff = en - timedelta(days=eng.HIGH_RECENCY_DAYS)
            wmask = (is_high.index >= cutoff) & (is_high.index < en)
            hi = bool(is_high[wmask].any()) if wmask.any() else False
            dn = eng.days_to_next_earnings(earn, ed, en)
            enhanced = (
                (surprise is not None and surprise >= eng.SURPRISE_MIN)
                and (vr is not None and vr >= eng.VOL_MULT)
                and (rs is not None and rs > 0)
                and (hi is True)
                and ((dn is None) or (dn > eng.NEAR_EARN_DAYS) or (dn < 0))
            )
            rows.append({
                "ticker": t, "is_it": is_it, "year": en.year,
                "entry_date": pd.Timestamp(en), "exit_date": pd.Timestamp(r7["exit_date"]),
                "ret_base": round(r7["return_pct"] * 100, 2),                 # BASE outcome (7% trail)
                "ret_sector": round((r12 if is_it else r7)["return_pct"] * 100, 2),  # enhanced engine (12%IT/7%)
                "ret5": round(ret5 * 100, 2) if ret5 is not None else np.nan,
                "ret5_known": pd.Timestamp(ret5_known) if ret5_known is not None else pd.NaT,
                "enhanced": enhanced,
            })
        time.sleep(0.0)
    df = pd.DataFrame(rows).sort_values("entry_date").reset_index(drop=True)
    return df


# ─── point-in-time health signals ─────────────────────────────────────────────
def health_realized(base, D, L=L_REAL):
    w = base[(base.exit_date < D) & (base.exit_date >= D - pd.Timedelta(days=L))]
    if len(w) < MIN_N:
        return None, len(w)
    return float(w.ret_base.mean()), len(w)


def health_drift(base, D, L=L_DRIFT):
    w = base[(base.ret5_known < D) & (base.ret5_known.notna())
             & (base.entry_date >= D - pd.Timedelta(days=L))]
    w = w[w.ret5.notna()]
    if len(w) < MIN_N:
        return None, len(w)
    return float(w.ret5.mean()), len(w)


def stat(df, col="ret_sector"):
    if df.empty:
        return (0, None, None, None)
    wr = round((df[col] > 0).mean() * 100, 1)
    avg = round(df[col].mean(), 2)
    gw = (df[df[col] > 0][col] / 100 * P).sum()
    gl = abs((df[df[col] <= 0][col] / 100 * P).sum())
    pf = round(gw / gl, 2) if gl > 0 else float("inf")
    return (len(df), wr, avg, pf)


def apply_gate(base, enh, signal_fn, thresh=0.0):
    """Return a boolean Series over enh: True = trade allowed by the gate."""
    allow = []
    for _, r in enh.iterrows():
        val, n = signal_fn(base, r.entry_date)
        allow.append(True if val is None else (val >= thresh))   # thin data -> allow
    return pd.Series(allow, index=enh.index)


def main():
    df = build()
    df.to_csv(os.path.join(_REPORTS_DIR, "backtest_signal_health_candidates.csv"), index=False)
    base = df                                  # health computed on full EPS-beat population
    enh = df[(df.enhanced) & (df.entry_date >= pd.Timestamp(EVAL_START))].copy()
    print(f"\nBASE pop {len(base)} | enhanced (eval) {len(enh)}")

    gates = {
        "Ungated":            pd.Series(True, index=enh.index),
        "SPY>200MA (ref)":    None,            # filled below for reference if regime present
        "Realized health ≥0": apply_gate(base, enh, health_realized, 0.0),
        "Drift health ≥0":    apply_gate(base, enh, health_drift, 0.0),
        "Both ≥0":            None,            # combined below
    }
    gates["Both ≥0"] = gates["Realized health ≥0"] & gates["Drift health ≥0"]
    del gates["SPY>200MA (ref)"]               # keep focus on signal-based gates

    L = []; A = L.append
    A("# PEAD Signal-Health Gate\n")
    A(f"*Window {EVAL_START}→{SCAN_END}. Health signals measured on the broad EPS-beat "
      "(BASE) population, strictly point-in-time (only outcomes known at entry). Gate is "
      "applied to the enhanced trade set. n / win% / avg% / PF.*\n")

    # Aggregate
    A("## Aggregate (all eval years)\n")
    A("| Gate | Trades | Win% | Avg% | PF | vs ungated avg |")
    A("|------|-------:|-----:|-----:|---:|---------------:|")
    n0, w0, a0, p0 = stat(enh)
    for name, mask in gates.items():
        sub = enh[mask]
        n, w, a, p = stat(sub)
        delta = "—" if name == "Ungated" else f"{(a - a0):+.2f} pts"
        A(f"| {name} | {n} | {w}% | {a}% | {p} | {delta} |")
    A("")

    # Per-year: the real test (cut bad years, keep good years)
    A("## Per-year — does it cut hostile years but keep favourable ones?\n")
    for name, mask in gates.items():
        A(f"### {name}\n")
        A("| Year | Trades | Win% | Avg% | PF | % blocked |")
        A("|------|-------:|-----:|-----:|---:|----------:|")
        for y in [2022, 2023, 2024, 2025, 2026]:
            full_y = enh[enh.year == y]
            sub_y = enh[mask & (enh.year == y)]
            n, w, a, p = stat(sub_y)
            blocked = (1 - len(sub_y) / len(full_y)) * 100 if len(full_y) else 0
            tag = " ⛔hostile" if y in (2022, 2026) else ""
            A(f"| {y}{tag} | {n} | {w if w is not None else '—'}% | "
              f"{a if a is not None else '—'}% | {p if p is not None else '—'} | {blocked:.0f}% |")
        A("")

    # Discrimination summary
    A("## Regime discrimination (the key property)\n")
    A("| Gate | Blocked in hostile yrs (2022,2026) | Blocked in good yrs (2023-25) | Discrimination |")
    A("|------|-----------------------------------:|------------------------------:|---------------:|")
    hostile = enh[enh.year.isin([2022, 2026])]
    good = enh[enh.year.isin([2023, 2024, 2025])]
    for name, mask in gates.items():
        if name == "Ungated":
            continue
        bh = (1 - mask[hostile.index].mean()) * 100
        bg = (1 - mask[good.index].mean()) * 100
        disc = bh - bg
        verdict = "✓ targets bad regimes" if disc > 10 else ("~ weak" if disc > 0 else "✗ backwards")
        A(f"| {name} | {bh:.0f}% | {bg:.0f}% | {disc:+.0f} pts {verdict} |")
    A("\n*A good gate blocks a much larger share of trades in hostile years than in good "
      "years (positive discrimination), unlike SPY>200MA which fired bull-and-weak 2026 "
      "as 'risk-on'.*\n")

    A("## Live implementation note\n")
    A("The gate needs a rolling read of the broad PEAD signal, which the live agent does not "
      "get automatically (it only trades the enhanced set). To run this live, add a weekly "
      "**PEAD breadth monitor** (in `universe_refresh` or `pre_market`): sample recent S&P 500 "
      "EPS beats and record their 5-trading-day post-earnings drift; gate entries when the "
      "trailing-35d mean drift (and/or trailing-60d realized BASE return) drops below 0. This "
      "is a research/monitoring change — it does NOT alter `memory/strategy.md` rules, which "
      "are human-edit-only.\n")
    rep = "\n".join(L)
    with open(os.path.join(_REPORTS_DIR, "backtest_report_PEAD_SIGNAL_HEALTH.md"), "w", encoding="utf-8") as f:
        f.write(rep)
    print("\n" + rep)
    print("\nSaved: backtest_report_PEAD_SIGNAL_HEALTH.md, backtest_signal_health_candidates.csv")


if __name__ == "__main__":
    main()
