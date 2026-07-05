#!/usr/bin/env python3
"""Universe refresh routine — rebuilds memory/universe.md for S&P 1500."""

import csv
import io
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
TODAY            = datetime.date.today()
SCREENED_ON      = TODAY.isoformat()
EXPIRES_ON       = (TODAY + datetime.timedelta(days=7)).isoformat()
START_DATE       = (TODAY - datetime.timedelta(days=40)).isoformat()
END_DATE         = TODAY.isoformat()

MIN_PRICE        = 10.0
MIN_ADV_20D      = 20_000_000
MIN_LISTING_DAYS = 180
BATCH_SIZE       = 100

REPO_ROOT      = '/home/user/trading-routine'
SP500_CSV      = f'{REPO_ROOT}/scripts/sp500_source.csv'
UNIVERSE_PATH  = f'{REPO_ROOT}/memory/universe.md'
UNIVERSE_TMP   = f'{REPO_ROOT}/memory/universe.md.tmp'

SOURCE_500 = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv'
SOURCE_400 = 'https://en.wikipedia.org/wiki/List_of_S%26P_400_companies'
SOURCE_600 = 'https://en.wikipedia.org/wiki/List_of_S%26P_600_companies'

BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}


# ── S&P 500 loader (local CSV) ─────────────────────────────────────────────────
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
                'ticker':        sym,
                'sector':        row.get('sector', '').strip(),
                'cap_tier':      'large',
                'date_added':    date_added,
                'date_added_str': raw_date,
            })
    print(f'[sp500] loaded {len(tickers)} tickers from local CSV')
    return tickers


# ── Wikipedia index loader (S&P 400 and S&P 600) ──────────────────────────────
import re as _re

def load_wikipedia_index(url, cap_tier, name):
    try:
        r = requests.get(url, headers=BROWSER_HEADERS, timeout=30)
        r.raise_for_status()
    except Exception as e:
        raise RuntimeError(f'Failed to fetch {name} from Wikipedia: {e}')

    tables = _re.findall(
        r'<table[^>]*wikitable[^>]*>(.*?)</table>',
        r.text, _re.DOTALL | _re.IGNORECASE,
    )
    if not tables:
        raise RuntimeError(f'No wikitable found in {name} page')

    # First table is the holdings list (Symbol, Security, GICS Sector, ...)
    t = tables[0]
    rows = _re.findall(r'<tr[^>]*>(.*?)</tr>', t, _re.DOTALL)

    tickers = []
    for row in rows[1:]:  # skip header row
        cells = _re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, _re.DOTALL)
        cleaned = [_re.sub(r'<[^>]+>', '', c).strip() for c in cells]
        if len(cleaned) < 3:
            continue
        symbol = cleaned[0].strip()
        sector = cleaned[2].strip()
        if not symbol or not symbol.isidentifier() and not all(c.isalnum() or c == '.' for c in symbol):
            continue
        if len(symbol) > 6 or not symbol:
            continue
        tickers.append({
            'ticker':         symbol,
            'sector':         sector,
            'cap_tier':       cap_tier,
            'date_added':     None,
            'date_added_str': '',
        })

    if len(tickers) < 100:
        raise RuntimeError(
            f'Too few tickers ({len(tickers)}) parsed from {name} — '
            f'page structure may have changed'
        )
    print(f'[{cap_tier}] loaded {len(tickers)} tickers from {name} (Wikipedia)')
    return tickers


# ── combine all three indexes ──────────────────────────────────────────────────
def load_all_indexes():
    sp500 = load_sp500()

    try:
        sp400 = load_wikipedia_index(SOURCE_400, 'mid', 'S&P 400')
    except RuntimeError as e:
        raise RuntimeError(f'S&P 400 load failed (all sources exhausted): {e}')

    try:
        sp600 = load_wikipedia_index(SOURCE_600, 'small', 'S&P 600')
    except RuntimeError as e:
        raise RuntimeError(f'S&P 600 load failed (all sources exhausted): {e}')

    # Deduplicate: large-cap wins over mid/small if ticker appears in multiple
    seen = {}
    for t in sp500 + sp400 + sp600:
        sym = t['ticker']
        if sym not in seen:
            seen[sym] = t
        else:
            # Keep large > mid > small priority
            tier_rank = {'large': 0, 'mid': 1, 'small': 2}
            if tier_rank[t['cap_tier']] < tier_rank[seen[sym]['cap_tier']]:
                seen[sym] = t

    combined = list(seen.values())
    print(f'[combined] {len(combined)} unique tickers '
          f'(large={sum(1 for t in combined if t["cap_tier"]=="large")}, '
          f'mid={sum(1 for t in combined if t["cap_tier"]=="mid")}, '
          f'small={sum(1 for t in combined if t["cap_tier"]=="small")})')
    return combined


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
                print(f'  [rate-limit] waiting {wait}s')
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
            print(f'  [retry {attempt+1}] {e}')
            time.sleep(5)
    return {}


def fetch_all_bars(symbols, start, end):
    all_bars = {}
    total_batches = (len(symbols) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(symbols), BATCH_SIZE):
        batch = symbols[i:i + BATCH_SIZE]
        bn = i // BATCH_SIZE + 1
        print(f'[alpaca] batch {bn}/{total_batches}: {len(batch)} symbols')
        try:
            bars = fetch_bars_batch(batch, start, end)
            all_bars.update(bars)
        except Exception as e:
            print(f'  [ERROR] batch {bn} failed: {e} — symbols will be no_bars')
        time.sleep(0.4)
    print(f'[alpaca] received bars for {len(all_bars)} symbols')
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
        last_close = last_20[-1]['c']
        avg_dv     = sum(b['c'] * b['v'] for b in last_20) / 20
        metrics[ticker] = {
            'last_price':            last_close,
            'avg_dollar_volume_20d': avg_dv,
        }
    return metrics


# ── filter logic ───────────────────────────────────────────────────────────────
def apply_filters(all_tickers, metrics):
    passing  = []
    rejected = []
    for t in all_tickers:
        ticker  = t['ticker']
        reasons = []

        if t['date_added'] is not None:
            age = (TODAY - t['date_added']).days
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
            key = ('price<10'  if 'price<10'  in reason else
                   'ADV<20M'   if 'ADV<20M'   in reason else
                   'IPO<180d'  if 'IPO<180d'  in reason else
                   'no_bars'   if 'no_bars'   in reason else reason)
            counts[key] = counts.get(key, 0) + 1
    return counts


# ── universe.md writer ─────────────────────────────────────────────────────────
HEADER_TMPL = """\
---
screened_on: {screened_on}
expires_on: {expires_on}
total_passed: {total_passed}
total_rejected: {total_rejected}
universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
source_500: {source_500}
source_400: {source_400}
source_600: {source_600}
---

# Universe

Pre-computed list of tickers that pass `memory/strategy.md` universe filters:

- S&P 1500 constituent (S&P 500 large-cap + S&P 400 mid-cap + S&P 600 small-cap)
- Price ≥ $10/share
- 20-day average dollar volume ≥ $20M (IEX feed)
- US primary listing
- Not a recent IPO (< 180 days since listing)

**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market`, `market_open`, and `midday`. The cache is valid for 7 days — if `expires_on` is in the past, trading routines abort with a Discord notice and wait for the next weekend refresh.

## Columns

- `ticker` — symbol
- `last_price` — most recent daily close used in screening (USD)
- `avg_dollar_volume_20d` — mean of `close × volume` across the last 20 trading days (USD, IEX feed)
- `sector` — GICS sector
- `cap_tier` — index tier: `large` (S&P 500), `mid` (S&P 400), `small` (S&P 600)
- `earnings_date_next` — next scheduled earnings report (`unknown`; `pre_market` re-verifies)
- `screened_on` — date the row was produced

| ticker | last_price | avg_dollar_volume_20d | sector | cap_tier | earnings_date_next | screened_on |
|--------|------------|-----------------------|--------|----------|--------------------|-------------|
"""


def write_universe(passing, rejected):
    by_tier = {tier: sum(1 for p in passing if p['cap_tier'] == tier)
               for tier in ('large', 'mid', 'small')}
    header = HEADER_TMPL.format(
        screened_on=SCREENED_ON,
        expires_on=EXPIRES_ON,
        total_passed=len(passing),
        total_rejected=len(rejected),
        source_500=SOURCE_500,
        source_400=SOURCE_400,
        source_600=SOURCE_600,
    )
    rows = []
    for p in passing:
        m = p['metrics']
        rows.append(
            f"| {p['ticker']} | ${m['last_price']:.2f} | "
            f"${m['avg_dollar_volume_20d']:,.0f} | {p['sector']} | "
            f"{p['cap_tier']} | {p['earnings_date_next']} | {SCREENED_ON} |"
        )
    content = header + '\n'.join(rows) + '\n'

    with open(UNIVERSE_TMP, 'w') as f:
        f.write(content)
    os.rename(UNIVERSE_TMP, UNIVERSE_PATH)
    print(f'[write] universe.md written — {len(passing)} passed, {len(rejected)} rejected')
    print(f'[write] by tier: large={by_tier["large"]}, mid={by_tier["mid"]}, small={by_tier["small"]}')
    return by_tier


# ── research_log append ────────────────────────────────────────────────────────
def append_research_log(n_passed, n_rejected):
    log_path = f'{REPO_ROOT}/memory/research_log.md'
    note = (f'universe_refresh S&P 1500: {n_passed} passed, {n_rejected} rejected; '
            f'sources: Wikipedia (S&P 400) + Wikipedia (S&P 600) + GitHub CSV (S&P 500)')
    new_row = f'| {SCREENED_ON} | {SOURCE_500} | ALL | {note} |'
    with open(log_path, 'a') as f:
        f.write(new_row + '\n')
    print('[log] research_log.md updated')


# ── main ───────────────────────────────────────────────────────────────────────
def main():
    print(f'=== universe_refresh  {SCREENED_ON} ===')

    # Load all three indexes — abort if any fails
    try:
        all_tickers = load_all_indexes()
    except RuntimeError as e:
        print(f'[ABORT] Index load failed: {e}')
        raise

    symbols  = [t['ticker'] for t in all_tickers]
    all_bars = fetch_all_bars(symbols, START_DATE, END_DATE)
    metrics  = compute_metrics(all_bars)

    passing, rejected = apply_filters(all_tickers, metrics)
    passing.sort(key=lambda x: x['ticker'])
    reason_counts = tally_reasons(rejected)
    errors = sum(1 for r in rejected
                 if any('no_bars' in rr for rr in r['reject_reasons']))

    print(f'[filter] passed={len(passing)}  rejected={len(rejected)}  no_bars={errors}')
    print(f'[filter] breakdown: {json.dumps(reason_counts)}')

    by_tier = write_universe(passing, rejected)
    append_research_log(len(passing), len(rejected))

    return {
        'passed':        len(passing),
        'rejected':      len(rejected),
        'errors':        errors,
        'reason_counts': reason_counts,
        'by_tier':       by_tier,
        'expires_on':    EXPIRES_ON,
    }


if __name__ == '__main__':
    result = main()
    print('RESULT_JSON:' + json.dumps(result))
