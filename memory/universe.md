---
screened_on: 2026-11-01
expires_on: 2026-11-08
total_passed: 310
total_rejected: 1222
universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
source_500: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
source_400: https://en.wikipedia.org/wiki/List_of_S%26P_400_companies
source_600: https://en.wikipedia.org/wiki/List_of_S%26P_600_companies
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
| A | $174.92 | 22,933,073 | Unknown | large | unknown | 2026-11-01 |
| AAL | $12.60 | 29,983,549 | Industrials | mid | unknown | 2026-11-01 |
| AAPL | $344.77 | 393,241,434 | Information Technology | large | unknown | 2026-11-01 |
| ABBV | $294.81 | 63,060,649 | Health Care | large | unknown | 2026-11-01 |
| ABNB | $164.37 | 27,547,134 | Consumer Discretionary | large | unknown | 2026-11-01 |
| ABT | $106.24 | 53,423,657 | Health Care | large | unknown | 2026-11-01 |
| ACN | $258.13 | 78,899,218 | Information Technology | large | unknown | 2026-11-01 |
| ADBE | $250.12 | 40,442,577 | Information Technology | large | unknown | 2026-11-01 |
| ADI | $417.16 | 54,417,794 | Information Technology | large | unknown | 2026-11-01 |
| ADP | $293.86 | 26,713,510 | Industrials | large | unknown | 2026-11-01 |
| ADSK | $249.66 | 29,675,408 | Information Technology | large | unknown | 2026-11-01 |
| AIG | $81.91 | 26,214,069 | Financials | large | unknown | 2026-11-01 |
| AJG | $276.25 | 22,642,474 | Financials | large | unknown | 2026-11-01 |
| AKAM | $92.74 | 23,490,456 | Information Technology | large | unknown | 2026-11-01 |
| ALL | $259.85 | 22,549,068 | Unknown | large | unknown | 2026-11-01 |
| AMAT | $390.07 | 127,336,465 | Information Technology | large | unknown | 2026-11-01 |
| AMD | $505.20 | 308,470,987 | Information Technology | large | unknown | 2026-11-01 |
| AMGN | $466.10 | 46,296,094 | Health Care | large | unknown | 2026-11-01 |
| AMT | $187.90 | 31,541,313 | Real Estate | large | unknown | 2026-11-01 |
| AMZN | $240.34 | 371,668,768 | Consumer Discretionary | large | unknown | 2026-11-01 |
| ANET | $168.79 | 59,914,304 | Information Technology | large | unknown | 2026-11-01 |
| AON | $321.73 | 30,978,894 | Financials | large | unknown | 2026-11-01 |
| APH | $79.33 | 51,149,832 | Information Technology | large | unknown | 2026-11-01 |
| APP | $228.47 | 44,117,824 | Unknown | large | unknown | 2026-11-01 |
| ARES | $128.28 | 20,300,164 | Unknown | large | unknown | 2026-11-01 |
| ATI | $165.57 | 20,334,101 | Materials | mid | unknown | 2026-11-01 |
| AVGO | $326.15 | 244,838,955 | Information Technology | large | unknown | 2026-11-01 |
| AXP | $319.16 | 42,417,063 | Unknown | large | unknown | 2026-11-01 |
| AZO | $3169.56 | 34,014,769 | Consumer Discretionary | large | unknown | 2026-11-01 |
| BA | $171.57 | 72,220,954 | Industrials | large | unknown | 2026-11-01 |
| BAC | $50.01 | 149,783,672 | Financials | large | unknown | 2026-11-01 |
| BE | $203.21 | 104,163,854 | Unknown | large | unknown | 2026-11-01 |
| BIIB | $253.61 | 20,889,968 | Unknown | large | unknown | 2026-11-01 |
| BKNG | $148.13 | 57,848,800 | Consumer Discretionary | large | unknown | 2026-11-01 |
| BKR | $55.23 | 22,246,721 | Unknown | large | unknown | 2026-11-01 |
| BLK | $1147.74 | 48,746,207 | Unknown | large | unknown | 2026-11-01 |
| BMY | $62.47 | 44,457,228 | Health Care | large | unknown | 2026-11-01 |
| BNY | $147.12 | 22,865,199 | Unknown | large | unknown | 2026-11-01 |
| BRK.B | $542.82 | 80,766,623 | Financials | large | unknown | 2026-11-01 |
| BSX | $41.97 | 71,096,680 | Health Care | large | unknown | 2026-11-01 |
| BURL | $236.98 | 24,319,979 | Unknown | mid | unknown | 2026-11-01 |
| BX | $118.53 | 29,126,468 | Financials | large | unknown | 2026-11-01 |
| C | $122.64 | 50,120,135 | Financials | large | unknown | 2026-11-01 |
| CAH | $250.62 | 22,552,754 | Unknown | large | unknown | 2026-11-01 |
| CART | $56.47 | 25,462,214 | Unknown | mid | unknown | 2026-11-01 |
| CASY | $680.67 | 21,408,379 | Consumer Staples | large | unknown | 2026-11-01 |
| CAT | $622.77 | 108,999,418 | Industrials | large | unknown | 2026-11-01 |
| CB | $364.17 | 29,169,722 | Financials | large | unknown | 2026-11-01 |
| CBOE | $335.33 | 24,234,639 | Unknown | large | unknown | 2026-11-01 |
| CCI | $88.70 | 27,429,334 | Unknown | large | unknown | 2026-11-01 |
| CCL | $28.80 | 32,875,986 | Unknown | large | unknown | 2026-11-01 |
| CDE | $13.09 | 21,529,314 | Unknown | mid | unknown | 2026-11-01 |
| CDNS | $327.98 | 48,844,314 | Unknown | large | unknown | 2026-11-01 |
| CEG | $262.39 | 49,466,801 | Unknown | large | unknown | 2026-11-01 |
| CFG | $63.80 | 22,138,249 | Financials | large | unknown | 2026-11-01 |
| CI | $298.34 | 21,027,067 | Health Care | large | unknown | 2026-11-01 |
| CIEN | $320.67 | 60,525,260 | Unknown | large | unknown | 2026-11-01 |
| CL | $95.30 | 26,482,342 | Consumer Staples | large | unknown | 2026-11-01 |
| CMCSA | $23.24 | 47,028,200 | Unknown | large | unknown | 2026-11-01 |
| CME | $303.20 | 32,291,096 | Financials | large | unknown | 2026-11-01 |
| CMG | $31.88 | 52,809,388 | Consumer Discretionary | large | unknown | 2026-11-01 |
| CMI | $500.11 | 34,557,028 | Industrials | large | unknown | 2026-11-01 |
| CMS | $70.11 | 22,983,914 | Unknown | large | unknown | 2026-11-01 |
| CNC | $68.46 | 20,162,898 | Unknown | large | unknown | 2026-11-01 |
| CNP | $42.45 | 24,898,572 | Unknown | large | unknown | 2026-11-01 |
| COF | $204.99 | 40,796,574 | Financials | large | unknown | 2026-11-01 |
| COHR | $210.28 | 83,261,572 | Unknown | large | unknown | 2026-11-01 |
| COIN | $143.28 | 42,925,364 | Unknown | large | unknown | 2026-11-01 |
| COP | $154.05 | 37,123,835 | Energy | large | unknown | 2026-11-01 |
| COR | $330.99 | 22,725,268 | Unknown | large | unknown | 2026-11-01 |
| COST | $1012.52 | 87,835,421 | Consumer Staples | large | unknown | 2026-11-01 |
| CPRT | $30.13 | 23,897,249 | Industrials | large | unknown | 2026-11-01 |
| CRH | $90.83 | 20,606,502 | Unknown | large | unknown | 2026-11-01 |
| CRL | $359.50 | 28,146,022 | Health Care | large | unknown | 2026-11-01 |
| CRM | $229.15 | 72,448,607 | Information Technology | large | unknown | 2026-11-01 |
| CRS | $283.17 | 23,221,460 | Materials | mid | unknown | 2026-11-01 |
| CRWD | $250.40 | 82,373,904 | Information Technology | large | unknown | 2026-11-01 |
| CSCO | $104.53 | 65,870,940 | Information Technology | large | unknown | 2026-11-01 |
| CSX | $51.98 | 43,048,501 | Industrials | large | unknown | 2026-11-01 |
| CTSH | $65.12 | 23,661,321 | Information Technology | large | unknown | 2026-11-01 |
| CVNA | $68.22 | 31,952,431 | Unknown | large | unknown | 2026-11-01 |
| CVS | $90.23 | 42,087,648 | Health Care | large | unknown | 2026-11-01 |
| CVX | $235.64 | 66,044,034 | Energy | large | unknown | 2026-11-01 |
| D | $66.63 | 24,996,468 | Utilities | large | unknown | 2026-11-01 |
| DAL | $80.15 | 30,341,826 | Industrials | large | unknown | 2026-11-01 |
| DASH | $179.06 | 46,563,466 | Unknown | large | unknown | 2026-11-01 |
| DDOG | $235.50 | 41,567,186 | Unknown | large | unknown | 2026-11-01 |
| DE | $675.29 | 43,070,919 | Industrials | large | unknown | 2026-11-01 |
| DELL | $423.98 | 121,181,383 | Information Technology | large | unknown | 2026-11-01 |
| DHI | $146.02 | 23,093,001 | Consumer Discretionary | large | unknown | 2026-11-01 |
| DHR | $232.30 | 63,073,719 | Health Care | large | unknown | 2026-11-01 |
| DIS | $110.96 | 43,295,262 | Communication Services | large | unknown | 2026-11-01 |
| DKS | $143.81 | 21,621,904 | Consumer Discretionary | mid | unknown | 2026-11-01 |
| DLR | $180.74 | 22,592,396 | Unknown | large | unknown | 2026-11-01 |
| DT | $57.70 | 29,411,889 | Unknown | mid | unknown | 2026-11-01 |
| DUK | $127.43 | 21,717,828 | Utilities | large | unknown | 2026-11-01 |
| DVN | $52.15 | 37,613,067 | Energy | large | unknown | 2026-11-01 |
| DXCM | $82.30 | 22,397,866 | Health Care | large | unknown | 2026-11-01 |
| EAT | $212.20 | 21,426,522 | Consumer Discretionary | mid | unknown | 2026-11-01 |
| EBAY | $121.63 | 25,241,371 | Consumer Discretionary | large | unknown | 2026-11-01 |
| ECHO | $96.95 | 22,871,048 | Unknown | large | unknown | 2026-11-01 |
| ECL | $302.91 | 25,242,333 | Materials | large | unknown | 2026-11-01 |
| EL | $109.23 | 20,729,345 | Consumer Staples | large | unknown | 2026-11-01 |
| ELV | $420.01 | 36,462,657 | Unknown | large | unknown | 2026-11-01 |
| EMR | $164.87 | 21,058,056 | Industrials | large | unknown | 2026-11-01 |
| EOG | $165.59 | 21,529,063 | Energy | large | unknown | 2026-11-01 |
| EQIX | $1013.62 | 37,834,987 | Real Estate | large | unknown | 2026-11-01 |
| EQT | $55.38 | 41,939,208 | Unknown | large | unknown | 2026-11-01 |
| ETN | $369.85 | 61,795,103 | Industrials | large | unknown | 2026-11-01 |
| EXC | $46.15 | 22,456,666 | Utilities | large | unknown | 2026-11-01 |
| EXPE | $286.06 | 23,782,902 | Consumer Discretionary | large | unknown | 2026-11-01 |
| F | $12.22 | 21,384,411 | Consumer Discretionary | large | unknown | 2026-11-01 |
| FANG | $212.16 | 22,318,120 | Unknown | large | unknown | 2026-11-01 |
| FAST | $51.91 | 28,300,126 | Industrials | large | unknown | 2026-11-01 |
| FCX | $62.45 | 39,465,781 | Materials | large | unknown | 2026-11-01 |
| FDX | $312.82 | 22,115,931 | Industrials | large | unknown | 2026-11-01 |
| FFIV | $338.12 | 20,428,326 | Information Technology | large | unknown | 2026-11-01 |
| FICO | $711.40 | 32,383,785 | Information Technology | large | unknown | 2026-11-01 |
| FITB | $53.90 | 39,887,645 | Financials | large | unknown | 2026-11-01 |
| FIX | $1232.14 | 53,444,640 | Unknown | large | unknown | 2026-11-01 |
| FLEX | $86.53 | 31,408,253 | Unknown | large | unknown | 2026-11-01 |
| FN | $326.89 | 25,514,205 | Unknown | mid | unknown | 2026-11-01 |
| FTNT | $136.02 | 31,227,151 | Information Technology | large | unknown | 2026-11-01 |
| GD | $372.73 | 20,402,624 | Industrials | large | unknown | 2026-11-01 |
| GE | $301.81 | 81,936,319 | Industrials | large | unknown | 2026-11-01 |
| GEV | $857.52 | 129,500,783 | Industrials | large | unknown | 2026-11-01 |
| GILD | $170.95 | 44,688,021 | Health Care | large | unknown | 2026-11-01 |
| GLW | $123.32 | 63,846,786 | Information Technology | large | unknown | 2026-11-01 |
| GM | $87.40 | 32,624,023 | Consumer Discretionary | large | unknown | 2026-11-01 |
| GOOG | $278.30 | 173,997,492 | Communication Services | large | unknown | 2026-11-01 |
| GOOGL | $279.90 | 320,623,427 | Communication Services | large | unknown | 2026-11-01 |
| GS | $894.09 | 87,180,497 | Financials | large | unknown | 2026-11-01 |
| HAL | $36.18 | 25,510,560 | Energy | large | unknown | 2026-11-01 |
| HBAN | $15.78 | 20,320,482 | Financials | large | unknown | 2026-11-01 |
| HCA | $473.21 | 33,757,004 | Health Care | large | unknown | 2026-11-01 |
| HD | $329.24 | 66,892,992 | Consumer Discretionary | large | unknown | 2026-11-01 |
| HLT | $356.97 | 48,730,463 | Consumer Discretionary | large | unknown | 2026-11-01 |
| HON | $218.37 | 22,915,940 | Industrials | large | unknown | 2026-11-01 |
| HONA | $154.15 | 22,367,225 | Unknown | large | unknown | 2026-11-01 |
| HOOD | $85.00 | 60,876,317 | Unknown | large | unknown | 2026-11-01 |
| HPE | $55.11 | 61,559,168 | Information Technology | large | unknown | 2026-11-01 |
| HPQ | $28.78 | 29,073,035 | Information Technology | large | unknown | 2026-11-01 |
| HUBB | $422.47 | 23,397,428 | Industrials | large | unknown | 2026-11-01 |
| HUM | $414.50 | 37,130,361 | Health Care | large | unknown | 2026-11-01 |
| HWM | $199.30 | 51,204,291 | Industrials | large | unknown | 2026-11-01 |
| IBM | $257.84 | 49,257,550 | Information Technology | large | unknown | 2026-11-01 |
| ICE | $168.85 | 32,552,853 | Financials | large | unknown | 2026-11-01 |
| IDXX | $551.48 | 21,252,369 | Health Care | large | unknown | 2026-11-01 |
| ILMN | $235.99 | 46,008,944 | Health Care | large | unknown | 2026-11-01 |
| INTC | $65.78 | 302,752,261 | Information Technology | large | unknown | 2026-11-01 |
| INTU | $341.12 | 53,569,973 | Information Technology | large | unknown | 2026-11-01 |
| IQV | $267.33 | 25,611,111 | Health Care | large | unknown | 2026-11-01 |
| IR | $80.06 | 20,783,890 | Industrials | large | unknown | 2026-11-01 |
| ISRG | $432.13 | 49,657,956 | Health Care | large | unknown | 2026-11-01 |
| ITW | $278.72 | 20,177,608 | Industrials | large | unknown | 2026-11-01 |
| JBL | $272.81 | 26,046,809 | Unknown | large | unknown | 2026-11-01 |
| JCI | $149.02 | 36,901,635 | Industrials | large | unknown | 2026-11-01 |
| JNJ | $273.25 | 80,224,633 | Health Care | large | unknown | 2026-11-01 |
| JPM | $337.14 | 79,691,425 | Financials | large | unknown | 2026-11-01 |
| KDP | $35.86 | 33,881,821 | Consumer Staples | large | unknown | 2026-11-01 |
| KEYS | $307.34 | 27,340,959 | Information Technology | large | unknown | 2026-11-01 |
| KKR | $94.42 | 25,629,893 | Unknown | large | unknown | 2026-11-01 |
| KLAC | $157.83 | 82,551,808 | Information Technology | large | unknown | 2026-11-01 |
| KMB | $107.98 | 23,363,591 | Consumer Staples | large | unknown | 2026-11-01 |
| KMI | $33.87 | 35,172,701 | Energy | large | unknown | 2026-11-01 |
| KO | $94.12 | 95,762,768 | Consumer Staples | large | unknown | 2026-11-01 |
| KR | $66.77 | 31,217,647 | Consumer Staples | large | unknown | 2026-11-01 |
| KVUE | $19.27 | 29,212,375 | Unknown | large | unknown | 2026-11-01 |
| LHX | $277.58 | 25,820,105 | Industrials | large | unknown | 2026-11-01 |
| LIN | $514.30 | 51,489,641 | Materials | large | unknown | 2026-11-01 |
| LITE | $840.81 | 188,920,890 | Unknown | large | unknown | 2026-11-01 |
| LLY | $1417.01 | 142,219,876 | Health Care | large | unknown | 2026-11-01 |
| LMT | $637.12 | 35,493,334 | Industrials | large | unknown | 2026-11-01 |
| LOW | $209.06 | 28,763,808 | Consumer Discretionary | large | unknown | 2026-11-01 |
| LRCX | $239.16 | 116,227,684 | Information Technology | large | unknown | 2026-11-01 |
| MA | $638.16 | 117,941,600 | Financials | large | unknown | 2026-11-01 |
| MAR | $399.62 | 29,477,980 | Unknown | large | unknown | 2026-11-01 |
| MCD | $258.06 | 49,506,415 | Consumer Discretionary | large | unknown | 2026-11-01 |
| MCHP | $77.36 | 34,685,731 | Information Technology | large | unknown | 2026-11-01 |
| MCK | $995.46 | 35,124,345 | Health Care | large | unknown | 2026-11-01 |
| MCO | $493.90 | 26,191,053 | Financials | large | unknown | 2026-11-01 |
| MDLZ | $64.94 | 35,615,186 | Consumer Staples | large | unknown | 2026-11-01 |
| MDT | $96.56 | 109,267,741 | Health Care | large | unknown | 2026-11-01 |
| META | $614.86 | 562,159,350 | Communication Services | large | unknown | 2026-11-01 |
| MKSI | $201.81 | 21,099,039 | Information Technology | mid | unknown | 2026-11-01 |
| MLM | $540.42 | 26,060,996 | Materials | large | unknown | 2026-11-01 |
| MMM | $174.31 | 27,691,444 | Industrials | large | unknown | 2026-11-01 |
| MNST | $47.35 | 28,671,681 | Consumer Staples | large | unknown | 2026-11-01 |
| MO | $78.00 | 35,790,354 | Consumer Staples | large | unknown | 2026-11-01 |
| MPC | $444.64 | 49,221,728 | Energy | large | unknown | 2026-11-01 |
| MPWR | $1212.42 | 45,044,973 | Information Technology | large | unknown | 2026-11-01 |
| MRK | $149.54 | 70,831,137 | Health Care | large | unknown | 2026-11-01 |
| MRNA | $221.60 | 116,152,885 | Health Care | large | unknown | 2026-11-01 |
| MRSH | $200.53 | 25,366,389 | Unknown | large | unknown | 2026-11-01 |
| MRVL | $196.40 | 155,249,610 | Unknown | large | unknown | 2026-11-01 |
| MS | $184.34 | 66,376,808 | Financials | large | unknown | 2026-11-01 |
| MSCI | $624.48 | 22,564,073 | Financials | large | unknown | 2026-11-01 |
| MSFT | $521.97 | 364,534,338 | Information Technology | large | unknown | 2026-11-01 |
| MSI | $491.66 | 25,155,251 | Information Technology | large | unknown | 2026-11-01 |
| MTD | $1675.11 | 21,382,511 | Health Care | large | unknown | 2026-11-01 |
| MTSI | $234.31 | 23,619,668 | Unknown | mid | unknown | 2026-11-01 |
| MTZ | $186.07 | 22,206,724 | Unknown | mid | unknown | 2026-11-01 |
| MU | $884.57 | 603,758,182 | Information Technology | large | unknown | 2026-11-01 |
| NCLH | $17.58 | 21,327,690 | Unknown | large | unknown | 2026-11-01 |
| NEE | $83.76 | 71,612,894 | Utilities | large | unknown | 2026-11-01 |
| NEM | $106.58 | 31,307,080 | Materials | large | unknown | 2026-11-01 |
| NFLX | $62.09 | 158,299,004 | Communication Services | large | unknown | 2026-11-01 |
| NI | $44.57 | 21,519,402 | Utilities | large | unknown | 2026-11-01 |
| NKE | $38.69 | 54,542,473 | Consumer Discretionary | large | unknown | 2026-11-01 |
| NOC | $557.70 | 31,057,837 | Industrials | large | unknown | 2026-11-01 |
| NOW | $105.12 | 111,356,559 | Information Technology | large | unknown | 2026-11-01 |
| NTAP | $199.19 | 24,890,511 | Information Technology | large | unknown | 2026-11-01 |
| NVDA | $204.76 | 675,198,957 | Information Technology | large | unknown | 2026-11-01 |
| NVR | $5961.80 | 20,447,212 | Consumer Discretionary | large | unknown | 2026-11-01 |
| NVT | $125.88 | 24,299,979 | Industrials | mid | unknown | 2026-11-01 |
| NXPI | $259.63 | 44,617,317 | Unknown | large | unknown | 2026-11-01 |
| O | $56.94 | 27,748,420 | Real Estate | large | unknown | 2026-11-01 |
| ODFL | $172.57 | 22,131,874 | Industrials | large | unknown | 2026-11-01 |
| OKTA | $208.14 | 40,707,778 | Information Technology | mid | unknown | 2026-11-01 |
| ON | $71.67 | 31,118,965 | Information Technology | large | unknown | 2026-11-01 |
| ORCL | $130.68 | 135,495,393 | Information Technology | large | unknown | 2026-11-01 |
| ORLY | $88.12 | 22,045,656 | Consumer Discretionary | large | unknown | 2026-11-01 |
| OXY | $63.99 | 44,263,300 | Energy | large | unknown | 2026-11-01 |
| P | $127.01 | 29,405,982 | Unknown | large | unknown | 2026-11-01 |
| PANW | $365.98 | 85,708,130 | Unknown | large | unknown | 2026-11-01 |
| PCG | $13.18 | 28,878,675 | Utilities | large | unknown | 2026-11-01 |
| PEP | $137.34 | 55,607,451 | Consumer Staples | large | unknown | 2026-11-01 |
| PFE | $30.50 | 46,976,747 | Health Care | large | unknown | 2026-11-01 |
| PG | $161.57 | 63,206,776 | Consumer Staples | large | unknown | 2026-11-01 |
| PGR | $231.26 | 30,684,060 | Financials | large | unknown | 2026-11-01 |
| PH | $899.43 | 37,977,005 | Industrials | large | unknown | 2026-11-01 |
| PINS | $19.36 | 20,922,766 | Unknown | mid | unknown | 2026-11-01 |
| PLD | $128.02 | 23,292,305 | Real Estate | large | unknown | 2026-11-01 |
| PLTR | $184.10 | 113,318,005 | Unknown | large | unknown | 2026-11-01 |
| PM | $208.86 | 45,010,973 | Consumer Staples | large | unknown | 2026-11-01 |
| PNC | $227.94 | 25,856,738 | Financials | large | unknown | 2026-11-01 |
| PSX | $282.83 | 44,047,001 | Energy | large | unknown | 2026-11-01 |
| PTC | $195.50 | 52,496,669 | Information Technology | large | unknown | 2026-11-01 |
| PWR | $620.46 | 51,914,250 | Industrials | large | unknown | 2026-11-01 |
| PYPL | $57.02 | 26,882,441 | Financials | large | unknown | 2026-11-01 |
| QCOM | $164.78 | 58,687,093 | Information Technology | large | unknown | 2026-11-01 |
| RCL | $307.19 | 38,698,035 | Consumer Discretionary | large | unknown | 2026-11-01 |
| RDDT | $91.66 | 31,267,125 | Unknown | large | unknown | 2026-11-01 |
| REGN | $927.63 | 36,098,415 | Health Care | large | unknown | 2026-11-01 |
| ROK | $436.34 | 24,463,569 | Industrials | large | unknown | 2026-11-01 |
| ROP | $466.62 | 22,010,330 | Industrials | large | unknown | 2026-11-01 |
| ROST | $228.28 | 24,806,305 | Consumer Discretionary | large | unknown | 2026-11-01 |
| RRC | $54.65 | 21,438,885 | Energy | mid | unknown | 2026-11-01 |
| RTX | $199.85 | 52,662,718 | Industrials | large | unknown | 2026-11-01 |
| SBUX | $103.65 | 44,503,076 | Consumer Discretionary | large | unknown | 2026-11-01 |
| SCHW | $88.02 | 43,855,560 | Financials | large | unknown | 2026-11-01 |
| SHW | $332.67 | 29,907,386 | Materials | large | unknown | 2026-11-01 |
| SLB | $53.74 | 44,655,170 | Energy | large | unknown | 2026-11-01 |
| SMCI | $32.96 | 50,473,241 | Information Technology | large | unknown | 2026-11-01 |
| SMTC | $127.36 | 27,875,220 | Information Technology | mid | unknown | 2026-11-01 |
| SNDK | $1152.04 | 299,636,333 | Unknown | large | unknown | 2026-11-01 |
| SNPS | $467.80 | 61,564,548 | Information Technology | large | unknown | 2026-11-01 |
| SO | $93.70 | 28,667,222 | Utilities | large | unknown | 2026-11-01 |
| SPGI | $466.55 | 45,702,029 | Financials | large | unknown | 2026-11-01 |
| STRL | $346.04 | 21,385,635 | Unknown | mid | unknown | 2026-11-01 |
| STT | $169.86 | 21,205,358 | Financials | large | unknown | 2026-11-01 |
| STX | $644.46 | 175,458,490 | Information Technology | large | unknown | 2026-11-01 |
| SWKS | $87.46 | 25,375,230 | Information Technology | large | unknown | 2026-11-01 |
| SYK | $291.42 | 48,320,989 | Health Care | large | unknown | 2026-11-01 |
| T | $21.43 | 71,370,001 | Communication Services | large | unknown | 2026-11-01 |
| TDG | $1147.34 | 40,500,480 | Industrials | large | unknown | 2026-11-01 |
| TEL | $213.16 | 27,475,969 | Information Technology | large | unknown | 2026-11-01 |
| TER | $274.23 | 49,756,960 | Information Technology | large | unknown | 2026-11-01 |
| TFC | $48.82 | 33,161,632 | Financials | large | unknown | 2026-11-01 |
| TGT | $154.23 | 32,778,735 | Consumer Discretionary | large | unknown | 2026-11-01 |
| TJX | $140.29 | 45,764,909 | Consumer Discretionary | large | unknown | 2026-11-01 |
| TLN | $343.34 | 27,885,963 | Unknown | mid | unknown | 2026-11-01 |
| TMO | $696.91 | 104,786,366 | Health Care | large | unknown | 2026-11-01 |
| TMUS | $156.50 | 52,231,957 | Communication Services | large | unknown | 2026-11-01 |
| TRGP | $315.03 | 21,213,300 | Unknown | large | unknown | 2026-11-01 |
| TRV | $396.22 | 23,321,100 | Financials | large | unknown | 2026-11-01 |
| TSCO | $33.94 | 34,583,720 | Consumer Discretionary | large | unknown | 2026-11-01 |
| TSLA | $399.80 | 282,444,669 | Consumer Discretionary | large | unknown | 2026-11-01 |
| TT | $410.24 | 49,036,446 | Industrials | large | unknown | 2026-11-01 |
| TTMI | $82.97 | 26,491,568 | Information Technology | mid | unknown | 2026-11-01 |
| TTWO | $190.14 | 24,457,006 | Communication Services | large | unknown | 2026-11-01 |
| TWLO | $205.92 | 44,046,186 | Unknown | large | unknown | 2026-11-01 |
| TXN | $301.11 | 78,025,095 | Information Technology | large | unknown | 2026-11-01 |
| UAL | $104.23 | 28,722,166 | Industrials | large | unknown | 2026-11-01 |
| UBER | $65.23 | 63,212,770 | Unknown | large | unknown | 2026-11-01 |
| UNH | $406.92 | 128,095,732 | Health Care | large | unknown | 2026-11-01 |
| UNP | $303.96 | 35,640,519 | Industrials | large | unknown | 2026-11-01 |
| UPS | $108.27 | 24,361,833 | Industrials | large | unknown | 2026-11-01 |
| URI | $1169.23 | 39,537,609 | Industrials | large | unknown | 2026-11-01 |
| USB | $59.45 | 35,540,108 | Financials | large | unknown | 2026-11-01 |
| UTHR | $598.88 | 22,971,840 | Health Care | mid | unknown | 2026-11-01 |
| V | $413.53 | 131,781,691 | Financials | large | unknown | 2026-11-01 |
| VEEV | $312.94 | 27,545,516 | Unknown | large | unknown | 2026-11-01 |
| VLO | $400.09 | 61,007,567 | Energy | large | unknown | 2026-11-01 |
| VRT | $232.53 | 85,773,763 | Unknown | large | unknown | 2026-11-01 |
| VRTX | $559.04 | 41,093,454 | Health Care | large | unknown | 2026-11-01 |
| VST | $138.38 | 48,484,531 | Utilities | large | unknown | 2026-11-01 |
| VTR | $84.83 | 20,540,430 | Real Estate | large | unknown | 2026-11-01 |
| VZ | $44.74 | 75,872,550 | Communication Services | large | unknown | 2026-11-01 |
| WAT | $462.65 | 30,049,881 | Health Care | large | unknown | 2026-11-01 |
| WCC | $343.59 | 24,993,162 | Unknown | mid | unknown | 2026-11-01 |
| WDAY | $197.81 | 21,975,431 | Unknown | large | unknown | 2026-11-01 |
| WDC | $365.91 | 142,132,049 | Information Technology | large | unknown | 2026-11-01 |
| WELL | $234.73 | 47,423,550 | Real Estate | large | unknown | 2026-11-01 |
| WFC | $83.43 | 87,191,508 | Financials | large | unknown | 2026-11-01 |
| WM | $233.46 | 29,956,757 | Industrials | large | unknown | 2026-11-01 |
| WMB | $74.37 | 35,913,808 | Energy | large | unknown | 2026-11-01 |
| WMT | $123.51 | 99,135,486 | Consumer Staples | large | unknown | 2026-11-01 |
| XEL | $79.85 | 25,510,830 | Utilities | large | unknown | 2026-11-01 |
| XOM | $187.26 | 69,688,580 | Energy | large | unknown | 2026-11-01 |
