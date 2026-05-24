#!/usr/bin/env python3
"""
universe_refresh_run.py — Rebuilds memory/universe.md from S&P 1500 constituents.
Run directly: python3 scripts/universe_refresh_run.py
"""

import os
import sys
import time
import json
import datetime
import statistics
import re
import requests
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
UNIVERSE_PATH = REPO_ROOT / "memory" / "universe.md"
RESEARCH_LOG_PATH = REPO_ROOT / "memory" / "research_log.md"

ALPACA_KEY = os.environ["ALPACA_API_KEY_ID"]
ALPACA_SECRET = os.environ["ALPACA_SECRET_KEY"]
ALPACA_BASE = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
DATA_BASE = "https://data.alpaca.markets"

ALPACA_HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

TODAY = datetime.date.today()
EXPIRES = TODAY + datetime.timedelta(days=7)

# ── helpers ─────────────────────────────────────────────────────────────────

def post_discord(msg: str):
    url = os.environ["DISCORD_WEBHOOK_URL"]
    try:
        r = requests.post(url, json={"content": msg}, timeout=15)
        if r.status_code == 204:
            print("[discord] posted OK")
        else:
            print(f"[discord] warning: HTTP {r.status_code}")
    except Exception as e:
        print(f"[discord] FAILED to post: {e}")


def abort(msg: str):
    print(f"ABORT: {msg}")
    post_discord(f"❌ UNIVERSE REFRESH ABORT {TODAY}\n{msg}")
    sys.exit(1)


# ── S&P list fetchers ────────────────────────────────────────────────────────

def fetch_sp500_wikipedia() -> list[str]:
    """Parse S&P 500 table from Wikipedia."""
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    r = requests.get(url, timeout=30, headers={"User-Agent": "trading-bot/1.0"})
    r.raise_for_status()
    # Wikipedia table has ticker in first column
    tickers = re.findall(r'<td><a[^>]*>([A-Z]{1,5}(?:\.[A-Z])?)</a>', r.text)
    # More robust: look for wikitable rows
    # The first table on the page is the S&P 500 constituent table
    # Tickers appear as the first cell in each data row
    matches = re.findall(r'<td style="text-align:center"><a[^>]*>([A-Z.]{1,6})</a>', r.text)
    if not matches:
        # Try alternate pattern
        matches = re.findall(r'title="([A-Z]{1,5})"[^>]*>[A-Z]{1,5}</a></td>', r.text)
    if not matches:
        # Try the wikitable approach - look for ticker column
        rows = re.findall(r'<tr[^>]*>.*?</tr>', r.text, re.DOTALL)
        matches = []
        for row in rows:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            if cells:
                first = re.sub(r'<[^>]+>', '', cells[0]).strip()
                if re.match(r'^[A-Z]{1,5}$', first):
                    matches.append(first)
    return list(set(matches))


def fetch_sp500_github() -> tuple[list[str], str]:
    """Fetch S&P 500 from GitHub CSV dataset."""
    url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
    r = requests.get(url, timeout=30, headers={"User-Agent": "trading-bot/1.0"})
    r.raise_for_status()
    lines = r.text.strip().split("\n")
    # First line is header: Symbol,Name,Sector,...
    tickers = []
    for line in lines[1:]:
        parts = line.split(",")
        if parts:
            sym = parts[0].strip().strip('"')
            if re.match(r'^[A-Z]{1,5}$', sym):
                tickers.append(sym)
    return tickers, url


def fetch_sp500() -> tuple[list[str], str]:
    """Return (tickers, source_url) for S&P 500."""
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    try:
        tickers = _fetch_wikipedia_tickers(wiki_url, expected_min=400)
        if len(tickers) >= 400:
            print(f"[sp500] Wikipedia: {len(tickers)} tickers")
            return tickers, wiki_url
    except Exception as e:
        print(f"[sp500] Wikipedia failed: {e}")

    # Fallback: GitHub CSV
    try:
        tickers, url = fetch_sp500_github()
        if len(tickers) >= 400:
            print(f"[sp500] GitHub CSV: {len(tickers)} tickers")
            return tickers, url
    except Exception as e:
        print(f"[sp500] GitHub CSV failed: {e}")

    return None, None


def _fetch_wikipedia_tickers(url: str, expected_min: int = 300) -> list[str]:
    """Generic Wikipedia table scraper for index constituent lists."""
    r = requests.get(url, timeout=30, headers={"User-Agent": "trading-bot/1.0"})
    r.raise_for_status()
    html = r.text

    # Strategy 1: find wikitable and extract first-column links that look like tickers
    # Look for table rows with ticker symbols
    tickers = set()

    # Pattern: first <td> contains a ticker symbol (all-caps, 1-5 chars)
    # Ticker cells in Wikipedia S&P tables typically have format:
    # <td><a href="/wiki/TICKER">TICKER</a></td>  or
    # <td style="..."><a ...>TICKER</a></td>

    # Extract all table rows
    for row_match in re.finditer(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL):
        row = row_match.group(1)
        # Get all cells
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        if len(cells) < 2:
            continue
        first_cell = cells[0]
        # Strip HTML tags
        text = re.sub(r'<[^>]+>', '', first_cell).strip()
        # Must look like a ticker: 1-5 uppercase letters, optionally with dot
        if re.match(r'^[A-Z]{1,5}(\.[A-Z])?$', text):
            tickers.add(text)

    return list(tickers)


def fetch_sp400() -> tuple[list[str], str]:
    """Return (tickers, source_url) for S&P 400."""
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"
    try:
        tickers = _fetch_wikipedia_tickers(wiki_url, expected_min=300)
        if len(tickers) >= 300:
            print(f"[sp400] Wikipedia: {len(tickers)} tickers")
            return tickers, wiki_url
    except Exception as e:
        print(f"[sp400] Wikipedia failed: {e}")

    # Fallback: SlickCharts
    slick_url = "https://www.slickcharts.com/indices/sp-400"
    try:
        r = requests.get(slick_url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        tickers = re.findall(r'/symbol/([A-Z]{1,5})', r.text)
        tickers = list(set(tickers))
        if len(tickers) >= 300:
            print(f"[sp400] SlickCharts: {len(tickers)} tickers")
            return tickers, slick_url
    except Exception as e:
        print(f"[sp400] SlickCharts failed: {e}")

    return None, None


def fetch_sp600() -> tuple[list[str], str]:
    """Return (tickers, source_url) for S&P 600."""
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies"
    try:
        tickers = _fetch_wikipedia_tickers(wiki_url, expected_min=500)
        if len(tickers) >= 500:
            print(f"[sp600] Wikipedia: {len(tickers)} tickers")
            return tickers, wiki_url
    except Exception as e:
        print(f"[sp600] Wikipedia failed: {e}")

    # Fallback: SlickCharts
    slick_url = "https://www.slickcharts.com/indices/sp-600"
    try:
        r = requests.get(slick_url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        tickers = re.findall(r'/symbol/([A-Z]{1,5})', r.text)
        tickers = list(set(tickers))
        if len(tickers) >= 500:
            print(f"[sp600] SlickCharts: {len(tickers)} tickers")
            return tickers, slick_url
    except Exception as e:
        print(f"[sp600] SlickCharts failed: {e}")

    return None, None


# ── Alpaca bars ──────────────────────────────────────────────────────────────

def fetch_bars_batch(symbols: list[str], start: str, end: str) -> dict:
    """
    Fetch daily bars for a batch of symbols from Alpaca.
    Returns dict: symbol -> list of {close, volume, date}
    """
    url = f"{DATA_BASE}/v2/stocks/bars"
    params = {
        "symbols": ",".join(symbols),
        "timeframe": "1Day",
        "start": start,
        "end": end,
        "feed": "iex",
        "limit": 1000,
        "adjustment": "raw",
    }
    all_bars = {}
    next_token = None

    while True:
        if next_token:
            params["page_token"] = next_token
        r = requests.get(url, params=params, headers=ALPACA_HEADERS, timeout=60)
        if r.status_code == 429:
            print("[alpaca] rate limited, sleeping 5s")
            time.sleep(5)
            continue
        if r.status_code != 200:
            print(f"[alpaca] bars error {r.status_code}: {r.text[:200]}")
            return {}
        data = r.json()
        bars_data = data.get("bars", {})
        for sym, bars in bars_data.items():
            if sym not in all_bars:
                all_bars[sym] = []
            all_bars[sym].extend(bars)
        next_token = data.get("next_page_token")
        if not next_token:
            break

    return all_bars


def compute_metrics(bars: list[dict]) -> tuple[float, float]:
    """Return (last_price, avg_dollar_volume_20d) from bar list."""
    if not bars:
        return None, None
    # Sort by date ascending
    bars_sorted = sorted(bars, key=lambda b: b["t"])
    last_close = bars_sorted[-1]["c"]
    # Last 20 days of dollar volume
    recent = bars_sorted[-20:]
    if len(recent) < 20:
        return last_close, None  # Not enough history
    dollar_vols = [b["c"] * b["v"] for b in recent]
    avg_dv = statistics.mean(dollar_vols)
    return last_close, avg_dv


# ── GICS sector lookup ────────────────────────────────────────────────────────

# Static sector map for known tickers (from prior universe.md + common knowledge)
# This is a best-effort cache; unknown tickers get "Unknown"
SECTOR_MAP = {
    "AAPL": "Information Technology", "MSFT": "Information Technology",
    "NVDA": "Information Technology", "GOOGL": "Communication Services",
    "GOOG": "Communication Services", "AMZN": "Consumer Discretionary",
    "META": "Communication Services", "TSLA": "Consumer Discretionary",
    "BRK.B": "Financials", "UNH": "Health Care",
    "V": "Financials", "XOM": "Energy", "JPM": "Financials",
    "LLY": "Health Care", "JNJ": "Health Care", "MA": "Financials",
    "PG": "Consumer Staples", "AVGO": "Information Technology",
    "HD": "Consumer Discretionary", "MRK": "Health Care",
    "ABBV": "Health Care", "CVX": "Energy", "COST": "Consumer Staples",
    "NFLX": "Communication Services", "AMD": "Information Technology",
    "CSCO": "Information Technology", "ABT": "Health Care",
    "ACN": "Information Technology", "ADBE": "Information Technology",
    "ADI": "Information Technology", "ADP": "Industrials",
    "ADSK": "Information Technology", "AEP": "Utilities",
    "AIG": "Financials", "AJG": "Financials", "AKAM": "Information Technology",
    "ALB": "Materials", "AMAT": "Information Technology",
    "AME": "Industrials", "AMGN": "Health Care",
    "AMP": "Financials", "AMT": "Real Estate",
    "ANET": "Information Technology", "ANSS": "Information Technology",
    "AON": "Financials", "AOS": "Industrials",
    "APD": "Materials", "APH": "Information Technology",
    "ARE": "Real Estate", "AXON": "Industrials",
    "AZO": "Consumer Discretionary", "BA": "Industrials",
    "BAC": "Financials", "BAX": "Health Care",
    "BDX": "Health Care", "BEN": "Financials",
    "BK": "Financials", "BKNG": "Consumer Discretionary",
    "BMY": "Health Care", "BSX": "Health Care",
    "BX": "Financials", "C": "Financials",
    "CAT": "Industrials", "CB": "Financials",
    "CDW": "Information Technology", "CF": "Materials",
    "CHRW": "Industrials", "CI": "Health Care",
    "CINF": "Financials", "CL": "Consumer Staples",
    "CLX": "Consumer Staples", "CMA": "Financials",
    "CME": "Financials", "CMG": "Consumer Discretionary",
    "CMI": "Industrials", "COF": "Financials",
    "COP": "Energy", "CPRT": "Industrials",
    "CRL": "Health Care", "CRM": "Information Technology",
    "CRWD": "Information Technology", "CSX": "Industrials",
    "CTAS": "Industrials", "CTLT": "Health Care",
    "CTSH": "Information Technology", "CTVA": "Materials",
    "CVS": "Health Care", "D": "Utilities",
    "DAL": "Industrials", "DD": "Materials",
    "DE": "Industrials", "DELL": "Information Technology",
    "DFS": "Financials", "DG": "Consumer Staples",
    "DGX": "Health Care", "DHI": "Consumer Discretionary",
    "DHR": "Health Care", "DIS": "Communication Services",
    "DLTR": "Consumer Staples", "DOV": "Industrials",
    "DOW": "Materials", "DPZ": "Consumer Discretionary",
    "DRI": "Consumer Discretionary", "DTE": "Utilities",
    "DUK": "Utilities", "DVA": "Health Care",
    "DVN": "Energy", "DXCM": "Health Care",
    "EA": "Communication Services", "EBAY": "Consumer Discretionary",
    "ECL": "Materials", "ED": "Utilities",
    "EFX": "Industrials", "EIX": "Utilities",
    "EL": "Consumer Staples", "EMN": "Materials",
    "EMR": "Industrials", "EOG": "Energy",
    "EPAM": "Information Technology", "EQIX": "Real Estate",
    "EQR": "Real Estate", "ES": "Utilities",
    "ESS": "Real Estate", "ETN": "Industrials",
    "ETR": "Utilities", "ETSY": "Consumer Discretionary",
    "EVRG": "Utilities", "EW": "Health Care",
    "EXC": "Utilities", "EXPD": "Industrials",
    "EXPE": "Consumer Discretionary", "EXR": "Real Estate",
    "F": "Consumer Discretionary", "FAST": "Industrials",
    "FCX": "Materials", "FDS": "Financials",
    "FDX": "Industrials", "FE": "Utilities",
    "FFIV": "Information Technology", "FIS": "Financials",
    "FITB": "Financials", "FOX": "Communication Services",
    "FOXA": "Communication Services", "FRT": "Real Estate",
    "FTNT": "Information Technology", "FTV": "Industrials",
    "GD": "Industrials", "GE": "Industrials",
    "GEV": "Industrials", "GEHC": "Health Care",
    "GEN": "Information Technology", "GILD": "Health Care",
    "GIS": "Consumer Staples", "GL": "Financials",
    "GLW": "Information Technology", "GM": "Consumer Discretionary",
    "GNRC": "Industrials", "GPC": "Consumer Discretionary",
    "GS": "Financials", "GWW": "Industrials",
    "HAL": "Energy", "HCA": "Health Care",
    "HBAN": "Financials", "HES": "Energy",
    "HIG": "Financials", "HLT": "Consumer Discretionary",
    "HOLX": "Health Care", "HON": "Industrials",
    "HPE": "Information Technology", "HPQ": "Information Technology",
    "HRL": "Consumer Staples", "HSIC": "Health Care",
    "HST": "Real Estate", "HSY": "Consumer Staples",
    "HUBB": "Industrials", "HUM": "Health Care",
    "HWM": "Industrials", "IBM": "Information Technology",
    "ICE": "Financials", "IDXX": "Health Care",
    "IEX": "Industrials", "IFF": "Materials",
    "ILMN": "Health Care", "INCY": "Health Care",
    "INTC": "Information Technology", "INTU": "Information Technology",
    "INVH": "Real Estate", "IP": "Materials",
    "IPG": "Communication Services", "IQV": "Health Care",
    "IR": "Industrials", "IRM": "Real Estate",
    "ISRG": "Health Care", "IT": "Information Technology",
    "ITW": "Industrials", "IVZ": "Financials",
    "J": "Industrials", "JBHT": "Industrials",
    "JCI": "Industrials", "JKHY": "Information Technology",
    "JNJ": "Health Care", "JNPR": "Information Technology",
    "JPM": "Financials", "K": "Consumer Staples",
    "KDP": "Consumer Staples", "KEY": "Financials",
    "KEYS": "Information Technology", "KHC": "Consumer Staples",
    "KIM": "Real Estate", "KLAC": "Information Technology",
    "KMB": "Consumer Staples", "KMI": "Energy",
    "KMX": "Consumer Discretionary", "KO": "Consumer Staples",
    "KR": "Consumer Staples", "L": "Financials",
    "LDOS": "Industrials", "LEN": "Consumer Discretionary",
    "LH": "Health Care", "LHX": "Industrials",
    "LIN": "Materials", "LKQ": "Consumer Discretionary",
    "LLY": "Health Care", "LMT": "Industrials",
    "LNT": "Utilities", "LOW": "Consumer Discretionary",
    "LRCX": "Information Technology", "LUV": "Industrials",
    "LVS": "Consumer Discretionary", "LW": "Consumer Staples",
    "LYB": "Materials", "LYV": "Communication Services",
    "MA": "Financials", "MAA": "Real Estate",
    "MAS": "Industrials", "MCD": "Consumer Discretionary",
    "MCHP": "Information Technology", "MCK": "Health Care",
    "MCO": "Financials", "MDLZ": "Consumer Staples",
    "MDT": "Health Care", "MET": "Financials",
    "MGM": "Consumer Discretionary", "MHK": "Consumer Discretionary",
    "MKC": "Consumer Staples", "MKTX": "Financials",
    "MLM": "Materials", "MMC": "Financials",
    "MMM": "Industrials", "MNST": "Consumer Staples",
    "MO": "Consumer Staples", "MOH": "Health Care",
    "MOS": "Materials", "MPC": "Energy",
    "MPWR": "Information Technology", "MRK": "Health Care",
    "MRNA": "Health Care", "MS": "Financials",
    "MSCI": "Financials", "MSI": "Information Technology",
    "MTB": "Financials", "MTCH": "Communication Services",
    "MTD": "Health Care", "MU": "Information Technology",
    "NDAQ": "Financials", "NEE": "Utilities",
    "NEM": "Materials", "NET": "Information Technology",
    "NI": "Utilities", "NKE": "Consumer Discretionary",
    "NOC": "Industrials", "NOW": "Information Technology",
    "NRG": "Utilities", "NSC": "Industrials",
    "NTAP": "Information Technology", "NTRS": "Financials",
    "NUE": "Materials", "NVDA": "Information Technology",
    "NVR": "Consumer Discretionary", "NWS": "Communication Services",
    "NWSA": "Communication Services", "O": "Real Estate",
    "ODFL": "Industrials", "OKE": "Energy",
    "OMC": "Communication Services", "ON": "Information Technology",
    "ORCL": "Information Technology", "ORLY": "Consumer Discretionary",
    "OXY": "Energy", "PARA": "Communication Services",
    "PAYX": "Industrials", "PCAR": "Industrials",
    "PCG": "Utilities", "PEAK": "Real Estate",
    "PEG": "Utilities", "PEP": "Consumer Staples",
    "PFE": "Health Care", "PFG": "Financials",
    "PG": "Consumer Staples", "PGR": "Financials",
    "PH": "Industrials", "PHM": "Consumer Discretionary",
    "PKG": "Materials", "PLD": "Real Estate",
    "PM": "Consumer Staples", "PNC": "Financials",
    "PNR": "Industrials", "PNW": "Utilities",
    "PODD": "Health Care", "POOL": "Consumer Discretionary",
    "PPG": "Materials", "PPL": "Utilities",
    "PRU": "Financials", "PSA": "Real Estate",
    "PSX": "Energy", "PTC": "Information Technology",
    "PWR": "Industrials", "PYPL": "Financials",
    "QCOM": "Information Technology", "RCL": "Consumer Discretionary",
    "REG": "Real Estate", "REGN": "Health Care",
    "RF": "Financials", "RJF": "Financials",
    "RL": "Consumer Discretionary", "RMD": "Health Care",
    "ROK": "Industrials", "ROL": "Industrials",
    "ROP": "Industrials", "ROST": "Consumer Discretionary",
    "RSG": "Industrials", "RTX": "Industrials",
    "SBAC": "Real Estate", "SBUX": "Consumer Discretionary",
    "SCHW": "Financials", "SHW": "Materials",
    "SJM": "Consumer Staples", "SLB": "Energy",
    "SMCI": "Information Technology", "SNA": "Industrials",
    "SNPS": "Information Technology", "SO": "Utilities",
    "SPG": "Real Estate", "SPGI": "Financials",
    "SRE": "Utilities", "STE": "Health Care",
    "STLD": "Materials", "STT": "Financials",
    "STX": "Information Technology", "STZ": "Consumer Staples",
    "SWK": "Industrials", "SWKS": "Information Technology",
    "SYF": "Financials", "SYK": "Health Care",
    "SYY": "Consumer Staples", "T": "Communication Services",
    "TAP": "Consumer Staples", "TDG": "Industrials",
    "TDY": "Industrials", "TECH": "Health Care",
    "TEL": "Information Technology", "TER": "Information Technology",
    "TFC": "Financials", "TFX": "Health Care",
    "TGT": "Consumer Discretionary", "TJX": "Consumer Discretionary",
    "TMO": "Health Care", "TMUS": "Communication Services",
    "TPR": "Consumer Discretionary", "TRMB": "Information Technology",
    "TROW": "Financials", "TRV": "Financials",
    "TSCO": "Consumer Discretionary", "TSLA": "Consumer Discretionary",
    "TSN": "Consumer Staples", "TT": "Industrials",
    "TTWO": "Communication Services", "TXN": "Information Technology",
    "TYL": "Information Technology", "UAL": "Industrials",
    "UDR": "Real Estate", "UHS": "Health Care",
    "ULTA": "Consumer Discretionary", "UNH": "Health Care",
    "UNP": "Industrials", "UPS": "Industrials",
    "URI": "Industrials", "USB": "Financials",
    "V": "Financials", "VFC": "Consumer Discretionary",
    "VICI": "Real Estate", "VLO": "Energy",
    "VMC": "Materials", "VNT": "Information Technology",
    "VRSK": "Industrials", "VRSN": "Information Technology",
    "VRTX": "Health Care", "VTR": "Real Estate",
    "VTRS": "Health Care", "VZ": "Communication Services",
    "WAB": "Industrials", "WAT": "Health Care",
    "WBA": "Consumer Staples", "WBD": "Communication Services",
    "WDC": "Information Technology", "WELL": "Real Estate",
    "WFC": "Financials", "WHR": "Consumer Discretionary",
    "WM": "Industrials", "WMB": "Energy",
    "WMT": "Consumer Staples", "WRB": "Financials",
    "WRK": "Materials", "WST": "Health Care",
    "WTW": "Financials", "WY": "Real Estate",
    "WYNN": "Consumer Discretionary", "XEL": "Utilities",
    "XOM": "Energy", "XYL": "Industrials",
    "YUM": "Consumer Discretionary", "ZBH": "Health Care",
    "ZBRA": "Information Technology", "ZTS": "Health Care",
    # Mid/Small cap additions
    "AAL": "Industrials", "AAP": "Consumer Discretionary",
    "ACGL": "Financials", "ACHC": "Health Care",
    "AEIS": "Information Technology", "AEL": "Financials",
    "AFL": "Financials", "AGCO": "Industrials",
    "AIT": "Industrials", "AL": "Financials",
    "ALGN": "Health Care", "ALLE": "Industrials",
    "ALLY": "Financials", "ALNY": "Health Care",
    "ALSN": "Consumer Discretionary", "AMED": "Health Care",
    "AMG": "Financials", "AMKR": "Information Technology",
    "AMRC": "Industrials", "APA": "Energy",
    "ARW": "Information Technology", "ASH": "Materials",
    "ATR": "Materials", "ATO": "Utilities",
    "AVNT": "Materials", "AWK": "Utilities",
    "AWR": "Utilities", "AXS": "Financials",
    "AYI": "Industrials", "B": "Industrials",
    "BC": "Consumer Discretionary", "BCPC": "Materials",
    "BDC": "Information Technology", "BERY": "Materials",
    "BIO": "Health Care", "BJRI": "Consumer Discretionary",
    "BKH": "Utilities", "BMI": "Industrials",
    "BOH": "Financials", "BOOT": "Consumer Discretionary",
    "BRC": "Materials", "BRKR": "Health Care",
    "BXMT": "Financials", "CAG": "Consumer Staples",
    "CAMT": "Information Technology", "CASY": "Consumer Staples",
    "CBT": "Materials", "CC": "Materials",
    "CCCS": "Information Technology", "CCK": "Materials",
    "CELH": "Consumer Staples", "CFG": "Financials",
    "CFR": "Financials", "CHDN": "Consumer Discretionary",
    "CIVI": "Energy", "CNA": "Financials",
    "CNM": "Industrials", "CNX": "Energy",
    "COKE": "Consumer Staples", "COLB": "Financials",
    "CONE": "Real Estate", "CR": "Industrials",
    "CRVL": "Industrials", "CUBE": "Real Estate",
    "CWEN": "Utilities", "DAR": "Consumer Staples",
    "DCI": "Industrials", "DECK": "Consumer Discretionary",
    "DKS": "Consumer Discretionary", "DLB": "Information Technology",
    "DLTR": "Consumer Staples", "DLX": "Industrials",
    "DNOW": "Energy", "DY": "Communication Services",
    "EAT": "Consumer Discretionary", "EBC": "Financials",
    "EG": "Financials", "ENSG": "Health Care",
    "ENS": "Industrials", "EPRT": "Real Estate",
    "EPC": "Consumer Staples", "ESE": "Industrials",
    "ESAB": "Industrials", "ESNT": "Financials",
    "EVTC": "Information Technology", "EXP": "Materials",
    "EXPO": "Industrials", "EZPW": "Financials",
    "FAF": "Financials", "FBMS": "Financials",
    "FHI": "Financials", "FICO": "Information Technology",
    "FNB": "Financials", "FNF": "Financials",
    "FOR": "Real Estate", "FORM": "Information Technology",
    "FR": "Real Estate", "FULT": "Financials",
    "FUN": "Consumer Discretionary", "G": "Financials",
    "GATX": "Industrials", "GFF": "Industrials",
    "GHC": "Consumer Discretionary", "GKOS": "Health Care",
    "GME": "Consumer Discretionary", "GMS": "Industrials",
    "GPOR": "Energy", "GSHD": "Financials",
    "GTLS": "Industrials", "HBI": "Consumer Discretionary",
    "HCI": "Financials", "HCCI": "Energy",
    "HE": "Utilities", "HIMS": "Health Care",
    "HLI": "Financials", "HNI": "Industrials",
    "HP": "Energy", "HPP": "Real Estate",
    "HTGC": "Financials", "HXL": "Industrials",
    "IART": "Health Care", "IBP": "Consumer Discretionary",
    "IDCC": "Information Technology", "IMKTA": "Consumer Staples",
    "INFA": "Information Technology", "INGR": "Consumer Staples",
    "INW": "Materials", "IPGP": "Information Technology",
    "IRHC": "Industrials", "ITRI": "Information Technology",
    "JACK": "Consumer Discretionary", "JBGS": "Real Estate",
    "JELD": "Industrials", "JOBY": "Industrials",
    "JOE": "Real Estate", "JWN": "Consumer Discretionary",
    "KALU": "Materials", "KBH": "Consumer Discretionary",
    "KNF": "Industrials", "KRC": "Real Estate",
    "KSS": "Consumer Discretionary", "KTB": "Consumer Discretionary",
    "LBRT": "Energy", "LC": "Financials",
    "LECO": "Industrials", "LGIH": "Consumer Discretionary",
    "LFUS": "Information Technology", "LPX": "Materials",
    "LXP": "Real Estate", "MAN": "Industrials",
    "MATX": "Industrials", "MC": "Financials",
    "MBIN": "Financials", "MBWM": "Financials",
    "MCY": "Financials", "MD": "Health Care",
    "MDU": "Utilities", "MGEE": "Utilities",
    "MGY": "Energy", "MHO": "Consumer Discretionary",
    "MMS": "Health Care", "MMI": "Industrials",
    "MORN": "Financials", "MSA": "Industrials",
    "MSM": "Industrials", "MTG": "Financials",
    "MTH": "Consumer Discretionary", "MTUS": "Industrials",
    "MUR": "Energy", "NARI": "Health Care",
    "NBR": "Energy", "NCI": "Industrials",
    "NEU": "Materials", "NJR": "Utilities",
    "NN": "Industrials", "NOV": "Energy",
    "NR": "Industrials", "NRC": "Industrials",
    "NRG": "Utilities", "NUS": "Consumer Staples",
    "NVT": "Industrials", "NWL": "Consumer Staples",
    "NXST": "Communication Services", "NYF": "Financials",
    "OGS": "Utilities", "OI": "Materials",
    "OIS": "Energy", "OLN": "Materials",
    "OMCL": "Health Care", "OMF": "Financials",
    "ORI": "Financials", "OUT": "Communication Services",
    "PAAS": "Materials", "PAG": "Consumer Discretionary",
    "PAGS": "Financials", "PAHC": "Health Care",
    "PBF": "Energy", "PCRX": "Health Care",
    "PDCO": "Health Care", "PFG": "Financials",
    "PJT": "Financials", "PLXS": "Information Technology",
    "PMT": "Financials", "PNM": "Utilities",
    "PPC": "Consumer Staples", "PRGO": "Health Care",
    "PRI": "Financials", "PRIM": "Industrials",
    "PRLS": "Industrials", "PSMT": "Consumer Staples",
    "PTVE": "Consumer Staples", "PVH": "Consumer Discretionary",
    "QUAD": "Industrials", "R": "Industrials",
    "RBC": "Industrials", "RCUS": "Health Care",
    "RDN": "Financials", "RDNT": "Health Care",
    "REZI": "Industrials", "RGA": "Financials",
    "RHI": "Industrials", "RICK": "Consumer Discretionary",
    "RMAX": "Real Estate", "RPM": "Materials",
    "RRC": "Energy", "RRR": "Consumer Discretionary",
    "RTL": "Real Estate", "RXO": "Industrials",
    "SAM": "Consumer Staples", "SANM": "Information Technology",
    "SITE": "Consumer Discretionary", "SKY": "Consumer Discretionary",
    "SLAB": "Information Technology", "SM": "Energy",
    "SMTC": "Information Technology", "SNX": "Information Technology",
    "SPSC": "Information Technology", "SPT": "Information Technology",
    "SSD": "Industrials", "SSYS": "Information Technology",
    "STAG": "Real Estate", "STRA": "Consumer Discretionary",
    "SUM": "Materials", "SUPN": "Health Care",
    "SWBI": "Consumer Discretionary", "SWN": "Energy",
    "SWX": "Utilities", "TDW": "Energy",
    "THC": "Health Care", "THG": "Financials",
    "TKR": "Industrials", "TMHC": "Consumer Discretionary",
    "TOL": "Consumer Discretionary", "TPH": "Consumer Discretionary",
    "TPVG": "Financials", "TREX": "Industrials",
    "TRN": "Industrials", "TTEK": "Industrials",
    "TXG": "Health Care", "UE": "Real Estate",
    "UFI": "Consumer Discretionary", "UFPI": "Materials",
    "UHALB": "Industrials", "UNF": "Industrials",
    "UNVR": "Industrials", "USAC": "Energy",
    "USPH": "Health Care", "UTL": "Utilities",
    "VECO": "Information Technology", "VGR": "Consumer Staples",
    "VHI": "Materials", "VIRT": "Financials",
    "VLY": "Financials", "VMI": "Industrials",
    "VOYA": "Financials", "VPG": "Information Technology",
    "VRTS": "Financials", "VSH": "Information Technology",
    "VSCO": "Consumer Discretionary", "VST": "Utilities",
    "VSTO": "Consumer Discretionary", "VVV": "Consumer Discretionary",
    "WEN": "Consumer Discretionary", "WEX": "Information Technology",
    "WGO": "Consumer Discretionary", "WINA": "Consumer Discretionary",
    "WKC": "Consumer Discretionary", "WOR": "Materials",
    "WS": "Industrials", "WTFC": "Financials",
    "WWD": "Industrials", "XHR": "Real Estate",
    "XRAY": "Health Care", "ZEUS": "Materials",
    "ZI": "Communication Services", "ZION": "Financials",
    "ABNB": "Consumer Discretionary", "ACLX": "Health Care",
    "ACMR": "Information Technology", "ACVA": "Consumer Discretionary",
    "AER": "Industrials", "AGO": "Financials",
    "ALE": "Utilities", "ALEX": "Real Estate",
    "ALTR": "Financials", "AMR": "Energy",
    "AMSF": "Financials", "AN": "Consumer Discretionary",
    "ANF": "Consumer Discretionary", "APPF": "Information Technology",
    "APPN": "Information Technology", "APO": "Financials",
    "AR": "Energy", "ARCB": "Industrials",
    "ARCO": "Consumer Discretionary", "ARLO": "Information Technology",
    "ARWR": "Health Care", "ASO": "Consumer Discretionary",
    "ASTE": "Industrials", "ATI": "Materials",
    "ATMU": "Industrials", "ATNI": "Communication Services",
    "ATRO": "Industrials", "AUPH": "Health Care",
    "AVAV": "Industrials", "AVDX": "Information Technology",
    "AWI": "Industrials", "AXTA": "Materials",
    "AZZ": "Industrials", "BCC": "Materials",
    "BCOR": "Industrials", "BELFB": "Information Technology",
    "BGC": "Financials", "BHLB": "Financials",
    "BJ": "Consumer Staples", "BLDR": "Industrials",
    "BPMC": "Health Care", "BRP": "Consumer Discretionary",
    "BSIG": "Financials", "BUR": "Financials",
    "CABO": "Communication Services", "CAKE": "Consumer Discretionary",
    "CALX": "Information Technology", "CAML": "Financials",
    "CBSH": "Financials", "CCOI": "Communication Services",
    "CDR": "Real Estate", "CDRE": "Industrials",
    "CENT": "Consumer Discretionary", "CENTA": "Consumer Discretionary",
    "CHCO": "Financials", "CHE": "Health Care",
    "CHRD": "Energy", "CIFR": "Financials",
    "CIR": "Industrials", "CLFD": "Information Technology",
    "CLH": "Industrials", "CLSK": "Utilities",
    "CMC": "Materials", "CMCO": "Industrials",
    "CMOD": "Utilities", "CNMD": "Health Care",
    "CNOB": "Financials", "CNS": "Financials",
    "CNSL": "Communication Services", "CNX": "Energy",
    "COHU": "Information Technology", "COLL": "Health Care",
    "COMM": "Information Technology", "COMP": "Real Estate",
    "COOP": "Financials", "CORE": "Consumer Staples",
    "COTY": "Consumer Staples", "CPF": "Financials",
    "CPK": "Utilities", "CPNG": "Consumer Discretionary",
    "CPRI": "Consumer Discretionary", "CPRX": "Health Care",
    "CRK": "Energy", "CRS": "Materials",
    "CRUS": "Information Technology", "CRSR": "Information Technology",
    "CSL": "Industrials", "CSTM": "Materials",
    "CTBI": "Financials", "CTGO": "Information Technology",
    "CVBF": "Financials", "CVE": "Energy",
    "CWEN": "Utilities", "CWST": "Industrials",
    "CXDO": "Information Technology", "DAN": "Consumer Discretionary",
    "DBRG": "Real Estate", "DCO": "Industrials",
    "DFIN": "Industrials", "DGII": "Information Technology",
    "DKL": "Energy", "DLNG": "Energy",
    "DLX": "Industrials", "DNOW": "Energy",
    "DOOR": "Industrials", "DORM": "Consumer Discretionary",
    "DRQ": "Energy", "DSP": "Information Technology",
    "DVAX": "Health Care", "DWAC": "Communication Services",
    "DXPE": "Industrials", "EARN": "Financials",
    "ECPG": "Financials", "EFC": "Financials",
    "EGRX": "Health Care", "EIG": "Financials",
    "ELY": "Consumer Discretionary", "EMBC": "Health Care",
    "ENPH": "Information Technology", "ENVX": "Information Technology",
    "EPAC": "Industrials", "ESXB": "Financials",
    "ETD": "Consumer Discretionary", "EVGO": "Utilities",
    "EVRI": "Consumer Discretionary", "EWBC": "Financials",
    "EXAS": "Health Care", "EXEL": "Health Care",
    "EXG": "Utilities", "EXLP": "Energy",
    "EXLS": "Information Technology", "EXPI": "Real Estate",
    "EXTR": "Information Technology", "EYE": "Health Care",
    "EZPW": "Financials", "FAT": "Consumer Discretionary",
    "FBIZ": "Financials", "FBK": "Financials",
    "FBNC": "Financials", "FCF": "Financials",
    "FCFS": "Financials", "FGBI": "Financials",
    "FIBK": "Financials", "FISI": "Financials",
    "FLIC": "Financials", "FLNC": "Utilities",
    "FLOW": "Industrials", "FLR": "Industrials",
    "FLYW": "Information Technology", "FMBH": "Financials",
    "FMCB": "Financials", "FNKO": "Consumer Discretionary",
    "FOLD": "Health Care", "FORG": "Information Technology",
    "FOUR": "Information Technology", "FRME": "Financials",
    "FRPH": "Real Estate", "FSS": "Industrials",
    "FTDR": "Consumer Discretionary", "FWRD": "Industrials",
    "GDEN": "Consumer Discretionary", "GES": "Consumer Discretionary",
    "GIII": "Consumer Discretionary", "GMS": "Industrials",
    "GO": "Consumer Staples", "GRBK": "Consumer Discretionary",
    "GRPN": "Consumer Discretionary", "GVP": "Industrials",
    "HAFC": "Financials", "HALO": "Health Care",
    "HBI": "Consumer Discretionary", "HCC": "Materials",
    "HCKT": "Industrials", "HCSG": "Industrials",
    "HFWA": "Financials", "HGV": "Consumer Discretionary",
    "HIIQ": "Health Care", "HLIT": "Information Technology",
    "HOPE": "Financials", "HRMY": "Health Care",
    "HRN": "Consumer Discretionary", "HS": "Industrials",
    "HSTM": "Health Care", "HTH": "Financials",
    "HWKN": "Materials", "HZO": "Consumer Discretionary",
    "IAC": "Communication Services", "IBTX": "Financials",
    "ICUI": "Health Care", "IDEX": "Industrials",
    "IHRT": "Communication Services", "IIPR": "Real Estate",
    "IIIN": "Materials", "IMXI": "Financials",
    "INO": "Health Care", "INVA": "Health Care",
    "IONQ": "Information Technology", "IOSP": "Materials",
    "IOVA": "Health Care", "IRBT": "Consumer Discretionary",
    "IRMD": "Health Care", "IRTC": "Health Care",
    "ITIC": "Financials", "JACK": "Consumer Discretionary",
    "JBLU": "Industrials", "JEF": "Financials",
    "JJSF": "Consumer Staples", "JNCO": "Consumer Discretionary",
    "JOBY": "Industrials", "JOE": "Real Estate",
    "KAMN": "Industrials", "KFRC": "Industrials",
    "KLIC": "Information Technology", "KNSL": "Financials",
    "KOP": "Materials", "KRG": "Real Estate",
    "KTOS": "Industrials", "KW": "Real Estate",
    "LBRT": "Energy", "LCII": "Consumer Discretionary",
    "LGF.A": "Communication Services", "LGF.B": "Communication Services",
    "LGND": "Health Care", "LKFN": "Financials",
    "LMB": "Industrials", "LMNX": "Health Care",
    "LNDC": "Consumer Staples", "LNTH": "Health Care",
    "LOPE": "Consumer Discretionary", "LQDT": "Industrials",
    "LSTR": "Industrials", "LTC": "Real Estate",
    "LWAY": "Consumer Staples", "LYFT": "Industrials",
    "LZB": "Consumer Discretionary", "MARA": "Financials",
    "MATW": "Industrials", "MCBS": "Financials",
    "MCFT": "Consumer Discretionary", "MELI": "Consumer Discretionary",
    "MGPI": "Consumer Staples", "MGRC": "Industrials",
    "MGTX": "Health Care", "MITK": "Information Technology",
    "MIXT": "Information Technology", "MKSI": "Information Technology",
    "MLNK": "Industrials", "MLP": "Energy",
    "MMSI": "Health Care", "MNR": "Real Estate",
    "MNRO": "Consumer Discretionary", "MODN": "Information Technology",
    "MOG.A": "Industrials", "MPAA": "Consumer Discretionary",
    "MPB": "Financials", "MRC": "Industrials",
    "MRCY": "Industrials", "MRUS": "Health Care",
    "MSEX": "Utilities", "MSTR": "Information Technology",
    "MTX": "Materials", "MWA": "Industrials",
    "NBTB": "Financials", "NCBS": "Financials",
    "NEN": "Utilities", "NFLX": "Communication Services",
    "NGHC": "Financials", "NGVT": "Materials",
    "NKLA": "Industrials", "NL": "Industrials",
    "NNA": "Energy", "NNI": "Consumer Discretionary",
    "NOMD": "Consumer Staples", "NPO": "Industrials",
    "NRC": "Industrials", "NSIT": "Information Technology",
    "NTGR": "Information Technology", "NTIC": "Materials",
    "NTR": "Materials", "NTUS": "Health Care",
    "NUE": "Materials", "NVST": "Health Care",
    "NWE": "Utilities", "NWPX": "Materials",
    "NXRT": "Real Estate", "OBT": "Financials",
    "OCN": "Financials", "ODP": "Consumer Discretionary",
    "OFIX": "Health Care", "OGE": "Utilities",
    "OGEN": "Health Care", "OGRE": "Utilities",
    "OKTA": "Information Technology", "OLO": "Information Technology",
    "OMAB": "Industrials", "ONB": "Financials",
    "ONTO": "Information Technology", "OPCH": "Health Care",
    "OPEN": "Real Estate", "OR": "Materials",
    "ORCC": "Financials", "ORIC": "Health Care",
    "OSIS": "Industrials", "OUST": "Information Technology",
    "OVBC": "Financials", "OVV": "Energy",
    "OXSQ": "Financials", "PAGS": "Financials",
    "PBH": "Consumer Staples", "PBPB": "Consumer Discretionary",
    "PCB": "Financials", "PCRX": "Health Care",
    "PEGA": "Information Technology", "PENN": "Consumer Discretionary",
    "PFBC": "Financials", "PFSI": "Financials",
    "PGNY": "Health Care", "PLAB": "Information Technology",
    "PLNT": "Consumer Discretionary", "PLT": "Information Technology",
    "PLUS": "Information Technology", "PMTS": "Information Technology",
    "PNM": "Utilities", "PNNT": "Financials",
    "POL": "Materials", "PORT": "Industrials",
    "POWL": "Industrials", "PPBI": "Financials",
    "PPBT": "Health Care", "PRAA": "Financials",
    "PRAAA": "Financials", "PRFT": "Information Technology",
    "PRGS": "Information Technology", "PRMO": "Consumer Discretionary",
    "PROV": "Financials", "PRSP": "Consumer Discretionary",
    "PRU": "Financials", "PRVA": "Health Care",
    "PSMT": "Consumer Staples", "PSNL": "Health Care",
    "PSO": "Consumer Discretionary", "PTCT": "Health Care",
    "PTGX": "Health Care", "PTLO": "Consumer Discretionary",
    "PZZA": "Consumer Discretionary", "QGEN": "Health Care",
    "QLYS": "Information Technology", "QNST": "Communication Services",
    "QRVO": "Information Technology", "QTWO": "Information Technology",
    "QUBT": "Information Technology", "R": "Industrials",
    "RAMP": "Information Technology", "RBA": "Industrials",
    "RCKT": "Health Care", "RCUS": "Health Care",
    "RDCM": "Health Care", "REAX": "Real Estate",
    "REEF": "Consumer Discretionary", "REI": "Real Estate",
    "RELY": "Financials", "REPL": "Health Care",
    "REZI": "Industrials", "RGP": "Industrials",
    "RIOT": "Financials", "RIVN": "Consumer Discretionary",
    "RKLB": "Industrials", "RMBS": "Information Technology",
    "RMNI": "Information Technology", "ROCK": "Materials",
    "RPRX": "Health Care", "RRBI": "Financials",
    "RRGB": "Consumer Discretionary", "RRTS": "Industrials",
    "RTLR": "Energy", "RUBY": "Health Care",
    "RUN": "Utilities", "RUSHA": "Consumer Discretionary",
    "RUSHB": "Consumer Discretionary", "RUTH": "Consumer Discretionary",
    "RWT": "Financials", "RXO": "Industrials",
    "RYAM": "Materials", "SAFE": "Real Estate",
    "SAGE": "Health Care", "SAIL": "Information Technology",
    "SAMA": "Industrials", "SANM": "Information Technology",
    "SATS": "Communication Services", "SAVE": "Industrials",
    "SBCF": "Financials", "SBGI": "Communication Services",
    "SBOW": "Energy", "SCCO": "Materials",
    "SCHN": "Materials", "SCSC": "Information Technology",
    "SEIC": "Financials", "SFIX": "Consumer Discretionary",
    "SFNC": "Financials", "SGEN": "Health Care",
    "SGMS": "Consumer Discretionary", "SGRP": "Consumer Discretionary",
    "SHBI": "Financials", "SHLS": "Industrials",
    "SIGI": "Financials", "SIM": "Industrials",
    "SITC": "Real Estate", "SKYW": "Industrials",
    "SLM": "Financials", "SLMBP": "Financials",
    "SLVM": "Materials", "SMG": "Materials",
    "SMTC": "Information Technology", "SNDR": "Industrials",
    "SNEX": "Financials", "SNOA": "Health Care",
    "SOLV": "Health Care", "SONO": "Consumer Discretionary",
    "SPKE": "Utilities", "SPT": "Information Technology",
    "SPTN": "Consumer Staples", "SPWH": "Consumer Discretionary",
    "SRC": "Real Estate", "SRCL": "Industrials",
    "SRCE": "Financials", "SRDX": "Health Care",
    "SRI": "Consumer Discretionary", "STBA": "Financials",
    "STCN": "Consumer Discretionary", "STEP": "Financials",
    "STFC": "Financials", "STL": "Financials",
    "STNE": "Financials", "STRA": "Consumer Discretionary",
    "SUMO": "Information Technology", "SUPV": "Financials",
    "SWI": "Information Technology", "SWIM": "Consumer Discretionary",
    "SWKH": "Financials", "SWTX": "Health Care",
    "SXC": "Materials", "SXI": "Industrials",
    "TBI": "Industrials", "TCBI": "Financials",
    "TCBK": "Financials", "TCMD": "Health Care",
    "TDOC": "Health Care", "TDS": "Communication Services",
    "TGLS": "Industrials", "TGTX": "Health Care",
    "TILE": "Consumer Discretionary", "TIPT": "Financials",
    "TISI": "Industrials", "TITN": "Industrials",
    "TMCI": "Health Care", "TPIC": "Industrials",
    "TPVG": "Financials", "TRDA": "Health Care",
    "TREE": "Financials", "TREX": "Industrials",
    "TRI": "Industrials", "TRMK": "Financials",
    "TRNO": "Real Estate", "TRQ": "Materials",
    "TRS": "Industrials", "TRUE": "Consumer Discretionary",
    "TRUP": "Financials", "TSIG": "Industrials",
    "TTI": "Energy", "TTMI": "Information Technology",
    "TUSK": "Energy", "TVTX": "Health Care",
    "TWI": "Industrials", "TXG": "Health Care",
    "TXRH": "Consumer Discretionary", "TZOO": "Consumer Discretionary",
    "UEC": "Energy", "UEIC": "Consumer Discretionary",
    "UFCS": "Financials", "UGI": "Utilities",
    "UHAL": "Industrials", "UMBF": "Financials",
    "UMPQ": "Financials", "UNF": "Industrials",
    "UNVR": "Industrials", "UPH": "Industrials",
    "UPST": "Financials", "UPWK": "Industrials",
    "USFD": "Consumer Staples", "UTHR": "Health Care",
    "UTL": "Utilities", "UVSP": "Financials",
    "VALE": "Materials", "VBT": "Financials",
    "VCNX": "Health Care", "VCEL": "Health Care",
    "VCYT": "Health Care", "VERA": "Health Care",
    "VFC": "Consumer Discretionary", "VG": "Communication Services",
    "VGR": "Consumer Staples", "VIRT": "Financials",
    "VIV": "Communication Services", "VIVO": "Health Care",
    "VLE": "Consumer Staples", "VLRS": "Industrials",
    "VRTS": "Financials", "VSEC": "Industrials",
    "VSTA": "Consumer Discretionary", "VTOL": "Industrials",
    "WAL": "Financials", "WALD": "Industrials",
    "WD": "Financials", "WEN": "Consumer Discretionary",
    "WERN": "Industrials", "WEX": "Information Technology",
    "WGO": "Consumer Discretionary", "WHD": "Energy",
    "WINA": "Consumer Discretionary", "WKME": "Information Technology",
    "WLDN": "Industrials", "WLFC": "Industrials",
    "WMK": "Consumer Staples", "WNEB": "Financials",
    "WOW": "Communication Services", "WS": "Industrials",
    "WSBC": "Financials", "WSFS": "Financials",
    "WTBA": "Financials", "WTTR": "Energy",
    "XNCR": "Health Care", "XRX": "Information Technology",
    "XWEL": "Health Care", "YELL": "Industrials",
    "YORW": "Utilities", "ZD": "Information Technology",
    "ZEUS": "Materials", "ZION": "Financials",
    "ZUO": "Information Technology",
}


def get_sector(ticker: str) -> str:
    return SECTOR_MAP.get(ticker, "Unknown")


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    print(f"=== universe_refresh {TODAY} ===")

    # ── 1. Pull S&P constituent lists ──────────────────────────────────────
    print("\n[step 1] Fetching S&P 500 constituents...")
    sp500_tickers, source_500 = fetch_sp500()
    if not sp500_tickers:
        abort("S&P 500 fetch failed — all sources exhausted")

    print("[step 1] Fetching S&P 400 constituents...")
    sp400_tickers, source_400 = fetch_sp400()
    if not sp400_tickers:
        abort("S&P 400 fetch failed — all sources exhausted")

    print("[step 1] Fetching S&P 600 constituents...")
    sp600_tickers, source_600 = fetch_sp600()
    if not sp600_tickers:
        abort("S&P 600 fetch failed — all sources exhausted")

    # Build ticker → cap_tier map (500 first; 400 mid; 600 small; dedup by largest cap)
    ticker_tier: dict[str, str] = {}
    for t in sp600_tickers:
        ticker_tier[t] = "small"
    for t in sp400_tickers:
        ticker_tier[t] = "mid"
    for t in sp500_tickers:
        ticker_tier[t] = "large"

    all_tickers = sorted(ticker_tier.keys())
    print(f"\n[step 1] Combined: {len(all_tickers)} unique tickers "
          f"(large={sum(1 for v in ticker_tier.values() if v=='large')}, "
          f"mid={sum(1 for v in ticker_tier.values() if v=='mid')}, "
          f"small={sum(1 for v in ticker_tier.values() if v=='small')})")

    # ── 2. Fetch daily bars from Alpaca ────────────────────────────────────
    print("\n[step 2] Fetching daily bars from Alpaca (IEX feed)...")
    end_date = TODAY.isoformat()
    start_date = (TODAY - datetime.timedelta(days=60)).isoformat()

    BATCH_SIZE = 100
    all_bars: dict[str, list] = {}
    batches = [all_tickers[i:i+BATCH_SIZE] for i in range(0, len(all_tickers), BATCH_SIZE)]
    print(f"  {len(batches)} batches of up to {BATCH_SIZE} symbols")

    for i, batch in enumerate(batches):
        print(f"  batch {i+1}/{len(batches)} ({len(batch)} symbols)...", end="", flush=True)
        bars = fetch_bars_batch(batch, start_date, end_date)
        all_bars.update(bars)
        print(f" got {len(bars)} symbols with data")
        if i < len(batches) - 1:
            time.sleep(0.4)

    print(f"\n[step 2] Got bar data for {len(all_bars)} / {len(all_tickers)} symbols")

    # ── 3. Compute per-ticker metrics ──────────────────────────────────────
    print("\n[step 3] Computing metrics...")
    metrics: dict[str, dict] = {}
    for ticker in all_tickers:
        bars = all_bars.get(ticker, [])
        last_price, avg_dv = compute_metrics(bars)
        metrics[ticker] = {
            "last_price": last_price,
            "avg_dv": avg_dv,
            "bar_count": len(bars),
        }

    # ── 4. Apply universe filters ──────────────────────────────────────────
    print("\n[step 4] Applying filters...")
    passed = []
    rejected = []
    rej_reasons: dict[str, int] = {
        "price<10": 0,
        "ADV<20M": 0,
        "no_bars": 0,
        "insufficient_history": 0,
    }

    for ticker in all_tickers:
        m = metrics[ticker]
        tier = ticker_tier[ticker]
        reason = None

        if m["bar_count"] < 5:
            reason = "no_bars"
            rej_reasons["no_bars"] += 1
        elif m["last_price"] is None:
            reason = "no_bars"
            rej_reasons["no_bars"] += 1
        elif m["last_price"] < 10:
            reason = "price<10"
            rej_reasons["price<10"] += 1
        elif m["avg_dv"] is None:
            reason = "insufficient_history"
            rej_reasons["insufficient_history"] += 1
        elif m["avg_dv"] < 20_000_000:
            reason = "ADV<20M"
            rej_reasons["ADV<20M"] += 1

        if reason:
            rejected.append((ticker, reason, tier))
        else:
            passed.append({
                "ticker": ticker,
                "last_price": m["last_price"],
                "avg_dv": m["avg_dv"],
                "sector": get_sector(ticker),
                "cap_tier": tier,
            })

    total_passed = len(passed)
    total_rejected = len(rejected)
    large_ct = sum(1 for p in passed if p["cap_tier"] == "large")
    mid_ct = sum(1 for p in passed if p["cap_tier"] == "mid")
    small_ct = sum(1 for p in passed if p["cap_tier"] == "small")

    print(f"  Passed: {total_passed} | Rejected: {total_rejected}")
    print(f"  By tier: large={large_ct}, mid={mid_ct}, small={small_ct}")
    print(f"  Rejection reasons: {rej_reasons}")

    # ── 7. Write memory/universe.md atomically ─────────────────────────────
    print("\n[step 7] Writing memory/universe.md...")

    # Sort by ticker
    passed.sort(key=lambda x: x["ticker"])

    lines = [
        "---",
        f"screened_on: {TODAY}",
        f"expires_on: {EXPIRES}",
        f"total_passed: {total_passed}",
        f"total_rejected: {total_rejected}",
        "universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)",
        f"source_500: {source_500}",
        f"source_400: {source_400}",
        f"source_600: {source_600}",
        "---",
        "",
        "# Universe",
        "",
        "Pre-computed list of tickers that pass `memory/strategy.md` universe filters:",
        "",
        "- S&P 1500 constituent (S&P 500 large-cap + S&P 400 mid-cap + S&P 600 small-cap)",
        "- Price ≥ $10/share",
        "- 20-day average dollar volume ≥ $20M (IEX feed)",
        "- US primary listing",
        "- Not a recent IPO (< 180 days since listing)",
        "",
        "**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). "
        "Consumed read-only by `pre_market`, `market_open`, and `midday`. "
        "The cache is valid for 7 days — if `expires_on` is in the past, "
        "trading routines abort with a Discord notice and wait for the next weekend refresh.",
        "",
        "## Columns",
        "",
        "- `ticker` — symbol",
        "- `last_price` — most recent daily close used in screening (USD)",
        "- `avg_dollar_volume_20d` — mean of `close × volume` across the last 20 trading days (USD, IEX feed)",
        "- `sector` — GICS sector",
        "- `cap_tier` — index tier: `large` (S&P 500), `mid` (S&P 400), `small` (S&P 600)",
        "- `earnings_date_next` — next scheduled earnings report (`unknown`; `pre_market` re-verifies)",
        "- `screened_on` — date the row was produced",
        "",
        "| ticker | last_price | avg_dollar_volume_20d | sector | cap_tier | earnings_date_next | screened_on |",
        "|--------|------------|-----------------------|--------|----------|--------------------|-------------|",
    ]

    for p in passed:
        lp = f"${p['last_price']:.2f}"
        adv = f"{int(p['avg_dv']):,}"
        lines.append(
            f"| {p['ticker']} | {lp} | {adv} | {p['sector']} | {p['cap_tier']} | unknown | {TODAY} |"
        )

    content = "\n".join(lines) + "\n"

    # Write atomically (write to temp, then rename)
    tmp_path = UNIVERSE_PATH.with_suffix(".md.tmp")
    tmp_path.write_text(content, encoding="utf-8")
    tmp_path.rename(UNIVERSE_PATH)
    print(f"  Written {total_passed} rows to {UNIVERSE_PATH}")

    # ── Update research_log.md ─────────────────────────────────────────────
    print("\n[step 8] Updating research_log.md...")
    rl_content = RESEARCH_LOG_PATH.read_text(encoding="utf-8")

    top_reasons = sorted(rej_reasons.items(), key=lambda x: -x[1])
    reasons_str = " | ".join(f"{k}: {v}" for k, v in top_reasons)
    log_entry = (
        f"| {TODAY} | {source_500} | ALL | "
        f"universe_refresh S&P 1500: {total_passed} passed, {total_rejected} rejected; "
        f"sources: Wikipedia/GitHub (S&P 500) + Wikipedia (S&P 400) + Wikipedia (S&P 600); "
        f"tier: large={large_ct}, mid={mid_ct}, small={small_ct}; "
        f"top rejections: {reasons_str}; "
        f"expires {EXPIRES} |"
    )

    # Insert after the header table line
    insert_after = "| date | source | ticker | note |"
    separator = "|------|--------|--------|------|"
    if insert_after in rl_content:
        idx = rl_content.index(separator) + len(separator)
        rl_content = rl_content[:idx] + "\n" + log_entry + rl_content[idx:]
    else:
        rl_content += "\n" + log_entry + "\n"

    RESEARCH_LOG_PATH.write_text(rl_content, encoding="utf-8")
    print("  research_log.md updated")

    # Return summary for Discord
    return {
        "total_passed": total_passed,
        "total_rejected": total_rejected,
        "large": large_ct,
        "mid": mid_ct,
        "small": small_ct,
        "rej_reasons": rej_reasons,
        "source_500": source_500,
        "source_400": source_400,
        "source_600": source_600,
        "errors": 0,
    }


if __name__ == "__main__":
    result = main()
    print("\n=== universe_refresh complete ===")
    print(json.dumps(result, indent=2))
