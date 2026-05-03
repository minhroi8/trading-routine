#!/usr/bin/env python3
"""Universe refresh routine — rebuilds memory/universe.md from scratch."""

import csv
import os
import json
import time
import datetime
import requests

# ── credentials ───────────────────────────────────────────────────────────────
ALPACA_KEY    = os.environ['ALPACA_API_KEY_ID']
ALPACA_SECRET = os.environ['ALPACA_SECRET_KEY']
DATA_BASE     = 'https://data.alpaca.markets'

ALPACA_HEADERS = {
    'APCA-API-KEY-ID':     ALPACA_KEY,
    'APCA-API-SECRET-KEY': ALPACA_SECRET,
}

# ── constants ──────────────────────────────────────────────────────────────────
TODAY            = datetime.date(2026, 5, 3)
SCREENED_ON      = TODAY.isoformat()
EXPIRES_ON       = (TODAY + datetime.timedelta(days=7)).isoformat()
START_DATE       = (TODAY - datetime.timedelta(days=40)).isoformat()
END_DATE         = TODAY.isoformat()

MIN_PRICE        = 10.0
MIN_ADV_20D      = 20_000_000
MIN_LISTING_DAYS = 180
BATCH_SIZE       = 100

REPO_ROOT     = '/home/user/trading-routine'
SP500_CSV     = f'{REPO_ROOT}/scripts/sp500_source.csv'
UNIVERSE_PATH = f'{REPO_ROOT}/memory/universe.md'
UNIVERSE_TMP  = f'{REPO_ROOT}/memory/universe.md.tmp'
SOURCE_URL    = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv'


# ── load S&P 500 list from local CSV ──────────────────────────────────────────
def load_sp500():
    tickers = []
    with open(SP500_CSV, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sym = row['symbol'].strip()
            date_added = None
            raw_date = row.get('date_added', '').strip()
            if raw_date:
                try:
                    date_added = datetime.date.fromisoformat(raw_date[:10])
                except ValueError:
                    pass
            tickers.append({
                'ticker':     sym,
                'sector':     row.get('sector', '').strip(),
                'date_added': date_added,
                'date_added_str': raw_date,
            })
    print(f"[csv] loaded {len(tickers)} S&P 500 tickers from local CSV")
    return tickers


# ── Alpaca bars ────────────────────────────────────────────────────────────────
def fetch_bars_batch(symbols, start, end, retries=3):
    url = f'{DATA_BASE}/v2/stocks/bars'
    params = {
        'symbols':    ','.join(symbols),
        'timeframe':  '1Day',
        'start':      start,
        'end':        end,
        'limit':      10000,
        'adjustment': 'raw',
        'feed':       'iex',
    }
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=ALPACA_HEADERS,
                                params=params, timeout=60)
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"  [rate-limit] waiting {wait}s")
                time.sleep(wait)
                continue
            if resp.status_code == 400 and len(symbols) > 1:
                # Bad symbol in batch — bisect to isolate it
                mid = len(symbols) // 2
                result = {}
                for half in [symbols[:mid], symbols[mid:]]:
                    try:
                        result.update(fetch_bars_batch(half, start, end, retries=1))
                    except Exception:
                        pass
                return result
            resp.raise_for_status()
            return resp.json().get('bars', {})
        except Exception as e:
            if attempt == retries - 1:
                raise
            print(f"  [retry {attempt+1}] {e}")
            time.sleep(5)
    return {}


def fetch_all_bars(symbols, start, end):
    all_bars = {}
    total = len(symbols)
    total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, total, BATCH_SIZE):
        batch = symbols[i:i + BATCH_SIZE]
        bn = i // BATCH_SIZE + 1
        print(f"[alpaca] batch {bn}/{total_batches}: {len(batch)} symbols")
        try:
            bars = fetch_bars_batch(batch, start, end)
            all_bars.update(bars)
        except Exception as e:
            print(f"  [ERROR] batch {bn} failed: {e} — symbols will be no_bars")
        time.sleep(0.4)
    print(f"[alpaca] received bars for {len(all_bars)} symbols")
    return all_bars


# ── metrics computation ────────────────────────────────────────────────────────
def compute_metrics(all_bars):
    metrics = {}
    for ticker, bars in all_bars.items():
        if not bars:
            metrics[ticker] = {'error': 'empty bar list'}
            continue
        sorted_bars = sorted(bars, key=lambda b: b['t'])
        last_20 = sorted_bars[-20:]
        if len(last_20) < 20:
            metrics[ticker] = {'error': f'only {len(last_20)} trading days'}
            continue
        last_close   = last_20[-1]['c']
        avg_dv       = sum(b['c'] * b['v'] for b in last_20) / 20
        metrics[ticker] = {
            'last_price':            last_close,
            'avg_dollar_volume_20d': avg_dv,
        }
    return metrics


# ── filter logic ───────────────────────────────────────────────────────────────
def apply_filters(sp500, metrics, today):
    passing  = []
    rejected = []
    for t in sp500:
        ticker  = t['ticker']
        reasons = []

        if t['date_added'] is not None:
            age = (today - t['date_added']).days
            if age < MIN_LISTING_DAYS:
                reasons.append(f'IPO<180d (added {t["date_added_str"]}, {age}d ago)')

        if ticker not in metrics:
            reasons.append('no_bars')
        else:
            m = metrics[ticker]
            if 'error' in m:
                reasons.append(f'no_bars ({m["error"]})')
            else:
                if m['last_price'] < MIN_PRICE:
                    reasons.append(f'price<10 (${m["last_price"]:.2f})')
                if m['avg_dollar_volume_20d'] < MIN_ADV_20D:
                    adv_m = m['avg_dollar_volume_20d'] / 1_000_000
                    reasons.append(f'ADV<20M (${adv_m:.1f}M)')

        if reasons:
            rejected.append({**t, 'reject_reasons': reasons})
        else:
            passing.append({**t, 'metrics': metrics[ticker],
                            'earnings_date_next': 'unknown'})

    return passing, rejected


def tally_reasons(rejected):
    counts = {}
    for r in rejected:
        for reason in r['reject_reasons']:
            key = ('price<10' if 'price<10' in reason
                   else 'ADV<20M' if 'ADV<20M' in reason
                   else 'IPO<180d' if 'IPO<180d' in reason
                   else 'no_bars' if 'no_bars' in reason
                   else reason)
            counts[key] = counts.get(key, 0) + 1
    return counts


# ── universe.md writer ─────────────────────────────────────────────────────────
HEADER = """\
---
screened_on: {screened_on}
expires_on: {expires_on}
total_passed: {total_passed}
total_rejected: {total_rejected}
source: {source}
---

# Universe

Pre-computed list of tickers that pass `memory/strategy.md` universe filters:

- S&P 500 constituent
- Price ≥ $10/share
- 20-day average dollar volume ≥ $20M
- US primary listing
- Not a recent IPO (< 180 days since listing)

**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market`, `market_open`, and `midday`. The cache is valid for 7 days — if `expires_on` is in the past, trading routines abort with a Discord notice and wait for the next weekend refresh.

## Columns

- `ticker` — symbol
- `last_price` — most recent daily close used in screening (USD)
- `avg_dollar_volume_20d` — mean of `close × volume` across the last 20 trading days (USD)
- `sector` — GICS sector from the S&P 500 list source
- `earnings_date_next` — next scheduled earnings report (ISO date; `unknown` if lookup failed). `pre_market` re-verifies this for every candidate before including it in `plan.md`.
- `screened_on` — date the row was produced

| ticker | last_price | avg_dollar_volume_20d | sector | earnings_date_next | screened_on |
|--------|------------|-----------------------|--------|---------------------|-------------|
"""


def write_universe(passing, rejected, source_url):
    header = HEADER.format(
        screened_on=SCREENED_ON,
        expires_on=EXPIRES_ON,
        total_passed=len(passing),
        total_rejected=len(rejected),
        source=source_url,
    )
    rows = []
    for p in passing:
        m = p['metrics']
        rows.append(
            f"| {p['ticker']} | ${m['last_price']:.2f} | "
            f"${m['avg_dollar_volume_20d']:,.0f} | {p['sector']} | "
            f"{p['earnings_date_next']} | {SCREENED_ON} |"
        )
    content = header + '\n'.join(rows) + '\n'

    with open(UNIVERSE_TMP, 'w') as f:
        f.write(content)
    os.rename(UNIVERSE_TMP, UNIVERSE_PATH)
    print(f"[write] universe.md written — {len(passing)} tickers, {len(rejected)} rejected")


# ── research_log append ────────────────────────────────────────────────────────
def append_research_log(source_url, n_passed, n_rejected):
    log_path = f'{REPO_ROOT}/memory/research_log.md'
    with open(log_path) as f:
        content = f.read()
    note = (f'universe_refresh: {n_passed} passed, {n_rejected} rejected; '
            f'source: {source_url}')
    new_row = f'| {SCREENED_ON} | {source_url} | ALL | {note} |'
    if '|------|' in content:
        content = content.replace(
            '|------|--------|--------|------|',
            '|------|--------|--------|------|\n' + new_row,
        )
    else:
        content = content.rstrip('\n') + '\n' + new_row + '\n'
    with open(log_path, 'w') as f:
        f.write(content)
    print("[log] research_log.md updated")


# ── main ───────────────────────────────────────────────────────────────────────
def main():
    print(f"=== universe_refresh  {SCREENED_ON} ===")

    sp500 = load_sp500()
    symbols = [t['ticker'] for t in sp500]

    all_bars = fetch_all_bars(symbols, START_DATE, END_DATE)
    metrics  = compute_metrics(all_bars)

    passing, rejected = apply_filters(sp500, metrics, TODAY)
    passing.sort(key=lambda x: x['ticker'])
    reason_counts = tally_reasons(rejected)
    errors = sum(1 for r in rejected
                 if any('no_bars' in rr for rr in r['reject_reasons']))

    print(f"[filter] passed={len(passing)}  rejected={len(rejected)}  no_bars={errors}")
    print(f"[filter] breakdown: {json.dumps(reason_counts)}")

    write_universe(passing, rejected, SOURCE_URL)
    append_research_log(SOURCE_URL, len(passing), len(rejected))

    return {
        'passed':        len(passing),
        'rejected':      len(rejected),
        'errors':        errors,
        'reason_counts': reason_counts,
        'expires_on':    EXPIRES_ON,
        'source_url':    SOURCE_URL,
    }


if __name__ == '__main__':
    result = main()
    print('RESULT_JSON:' + json.dumps(result))
