---
screened_on: 2026-09-27
expires_on: 2026-10-04
total_passed: 250
total_rejected: 1283
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
| A | $172.78 | 21,317,916 | Unknown | large | unknown | 2026-09-27 |
| AAL | $13.87 | 26,951,701 | Industrials | mid | unknown | 2026-09-27 |
| AAPL | $341.02 | 401,456,333 | Information Technology | large | unknown | 2026-09-27 |
| ABBV | $264.28 | 39,996,530 | Health Care | large | unknown | 2026-09-27 |
| ABNB | $157.41 | 41,624,375 | Consumer Discretionary | large | unknown | 2026-09-27 |
| ABT | $101.26 | 40,778,003 | Health Care | large | unknown | 2026-09-27 |
| ACN | $176.05 | 41,365,480 | Information Technology | large | unknown | 2026-09-27 |
| ADBE | $235.48 | 46,191,755 | Information Technology | large | unknown | 2026-09-27 |
| ADI | $393.56 | 39,586,930 | Information Technology | large | unknown | 2026-09-27 |
| ADP | $263.72 | 26,663,592 | Industrials | large | unknown | 2026-09-27 |
| ADSK | $209.35 | 30,835,202 | Information Technology | large | unknown | 2026-09-27 |
| AKAM | $113.87 | 21,808,059 | Information Technology | large | unknown | 2026-09-27 |
| ALL | $227.47 | 25,955,594 | Unknown | large | unknown | 2026-09-27 |
| AMAT | $484.83 | 102,740,873 | Information Technology | large | unknown | 2026-09-27 |
| AMD | $630.47 | 313,901,247 | Information Technology | large | unknown | 2026-09-27 |
| AMGN | $414.67 | 48,867,832 | Health Care | large | unknown | 2026-09-27 |
| AMZN | $249.63 | 301,336,480 | Consumer Discretionary | large | unknown | 2026-09-27 |
| ANET | $206.49 | 39,544,384 | Information Technology | large | unknown | 2026-09-27 |
| AON | $278.05 | 43,533,942 | Financials | large | unknown | 2026-09-27 |
| APH | $84.09 | 46,278,776 | Information Technology | large | unknown | 2026-09-27 |
| APP | $310.69 | 59,722,534 | Unknown | large | unknown | 2026-09-27 |
| AVGO | $352.72 | 285,594,693 | Information Technology | large | unknown | 2026-09-27 |
| AXON | $430.04 | 23,495,650 | Industrials | large | unknown | 2026-09-27 |
| AXP | $308.80 | 42,194,128 | Unknown | large | unknown | 2026-09-27 |
| AZO | $2872.56 | 60,942,117 | Consumer Discretionary | large | unknown | 2026-09-27 |
| BA | $198.09 | 49,903,010 | Industrials | large | unknown | 2026-09-27 |
| BAC | $56.67 | 140,982,093 | Financials | large | unknown | 2026-09-27 |
| BE | $288.63 | 111,217,609 | Unknown | large | unknown | 2026-09-27 |
| BKNG | $163.89 | 96,154,544 | Consumer Discretionary | large | unknown | 2026-09-27 |
| BKR | $57.85 | 25,361,360 | Unknown | large | unknown | 2026-09-27 |
| BLK | $1086.35 | 34,151,618 | Unknown | large | unknown | 2026-09-27 |
| BMY | $62.89 | 32,711,223 | Health Care | large | unknown | 2026-09-27 |
| BNY | $150.18 | 22,456,579 | Unknown | large | unknown | 2026-09-27 |
| BRK.B | $505.43 | 69,831,547 | Financials | large | unknown | 2026-09-27 |
| BSX | $43.91 | 61,344,374 | Health Care | large | unknown | 2026-09-27 |
| BURL | $254.75 | 30,823,795 | Unknown | mid | unknown | 2026-09-27 |
| BX | $118.43 | 21,519,083 | Financials | large | unknown | 2026-09-27 |
| C | $134.27 | 47,627,305 | Financials | large | unknown | 2026-09-27 |
| CASY | $598.58 | 25,523,745 | Consumer Staples | large | unknown | 2026-09-27 |
| CAT | $821.04 | 70,406,136 | Industrials | large | unknown | 2026-09-27 |
| CB | $333.48 | 21,928,955 | Financials | large | unknown | 2026-09-27 |
| CCL | $22.27 | 30,592,360 | Unknown | large | unknown | 2026-09-27 |
| CDE | $19.23 | 21,833,014 | Unknown | mid | unknown | 2026-09-27 |
| CDNS | $326.13 | 39,388,878 | Unknown | large | unknown | 2026-09-27 |
| CEG | $263.30 | 26,616,892 | Unknown | large | unknown | 2026-09-27 |
| CHTR | $112.99 | 21,415,444 | Unknown | large | unknown | 2026-09-27 |
| CIEN | $356.57 | 45,344,107 | Unknown | large | unknown | 2026-09-27 |
| CMCSA | $21.92 | 40,253,846 | Unknown | large | unknown | 2026-09-27 |
| CME | $264.48 | 23,316,169 | Financials | large | unknown | 2026-09-27 |
| CMG | $31.32 | 30,334,428 | Consumer Discretionary | large | unknown | 2026-09-27 |
| CMI | $525.10 | 32,962,489 | Industrials | large | unknown | 2026-09-27 |
| COF | $200.24 | 31,561,353 | Financials | large | unknown | 2026-09-27 |
| COHR | $295.78 | 64,247,163 | Unknown | large | unknown | 2026-09-27 |
| COIN | $195.00 | 51,894,875 | Unknown | large | unknown | 2026-09-27 |
| COP | $127.29 | 34,669,807 | Energy | large | unknown | 2026-09-27 |
| COST | $922.76 | 72,175,238 | Consumer Staples | large | unknown | 2026-09-27 |
| CRH | $85.07 | 21,872,946 | Unknown | large | unknown | 2026-09-27 |
| CRM | $234.04 | 147,871,117 | Information Technology | large | unknown | 2026-09-27 |
| CRWD | $252.10 | 85,945,045 | Information Technology | large | unknown | 2026-09-27 |
| CSCO | $106.69 | 77,593,140 | Information Technology | large | unknown | 2026-09-27 |
| CSX | $46.78 | 38,143,426 | Industrials | large | unknown | 2026-09-27 |
| CTVA | $78.51 | 21,951,028 | Materials | large | unknown | 2026-09-27 |
| CVNA | $65.06 | 22,158,664 | Unknown | large | unknown | 2026-09-27 |
| CVS | $89.12 | 34,258,230 | Health Care | large | unknown | 2026-09-27 |
| CVX | $204.44 | 61,972,747 | Energy | large | unknown | 2026-09-27 |
| D | $60.70 | 24,450,362 | Utilities | large | unknown | 2026-09-27 |
| DAL | $84.92 | 20,968,666 | Industrials | large | unknown | 2026-09-27 |
| DASH | $193.38 | 47,318,480 | Unknown | large | unknown | 2026-09-27 |
| DDOG | $268.13 | 42,687,643 | Unknown | large | unknown | 2026-09-27 |
| DE | $690.08 | 45,602,309 | Industrials | large | unknown | 2026-09-27 |
| DELL | $563.28 | 148,248,130 | Information Technology | large | unknown | 2026-09-27 |
| DHI | $141.46 | 21,809,824 | Consumer Discretionary | large | unknown | 2026-09-27 |
| DHR | $224.58 | 46,464,341 | Health Care | large | unknown | 2026-09-27 |
| DIS | $106.16 | 38,474,610 | Communication Services | large | unknown | 2026-09-27 |
| DOCN | $139.94 | 20,790,912 | Unknown | mid | unknown | 2026-09-27 |
| DT | $57.95 | 22,522,701 | Unknown | mid | unknown | 2026-09-27 |
| DVN | $47.05 | 42,767,621 | Energy | large | unknown | 2026-09-27 |
| EBAY | $107.89 | 23,009,098 | Consumer Discretionary | large | unknown | 2026-09-27 |
| ELV | $396.29 | 24,197,277 | Unknown | large | unknown | 2026-09-27 |
| EOG | $140.33 | 21,276,785 | Energy | large | unknown | 2026-09-27 |
| EQIX | $1008.54 | 29,439,107 | Real Estate | large | unknown | 2026-09-27 |
| EQT | $50.80 | 24,564,066 | Unknown | large | unknown | 2026-09-27 |
| ETN | $440.07 | 45,787,164 | Industrials | large | unknown | 2026-09-27 |
| EXPE | $264.11 | 40,631,787 | Consumer Discretionary | large | unknown | 2026-09-27 |
| F | $12.71 | 27,268,622 | Consumer Discretionary | large | unknown | 2026-09-27 |
| FANG | $186.63 | 29,958,961 | Unknown | large | unknown | 2026-09-27 |
| FCX | $72.28 | 45,651,178 | Materials | large | unknown | 2026-09-27 |
| FDX | $285.79 | 26,187,679 | Industrials | large | unknown | 2026-09-27 |
| FICO | $863.72 | 22,534,172 | Information Technology | large | unknown | 2026-09-27 |
| FITB | $52.10 | 23,940,596 | Financials | large | unknown | 2026-09-27 |
| FIX | $1657.03 | 23,288,394 | Unknown | large | unknown | 2026-09-27 |
| FTNT | $173.45 | 27,449,343 | Information Technology | large | unknown | 2026-09-27 |
| GD | $336.69 | 21,129,729 | Industrials | large | unknown | 2026-09-27 |
| GE | $327.02 | 51,545,157 | Industrials | large | unknown | 2026-09-27 |
| GEV | $957.17 | 86,678,670 | Industrials | large | unknown | 2026-09-27 |
| GILD | $150.88 | 30,548,307 | Health Care | large | unknown | 2026-09-27 |
| GIS | $33.64 | 22,859,916 | Consumer Staples | large | unknown | 2026-09-27 |
| GLW | $156.58 | 49,124,567 | Information Technology | large | unknown | 2026-09-27 |
| GM | $82.66 | 27,288,001 | Consumer Discretionary | large | unknown | 2026-09-27 |
| GOOG | $341.03 | 173,157,244 | Communication Services | large | unknown | 2026-09-27 |
| GOOGL | $343.85 | 268,392,748 | Communication Services | large | unknown | 2026-09-27 |
| GS | $935.26 | 72,185,756 | Financials | large | unknown | 2026-09-27 |
| GWW | $1242.55 | 22,013,084 | Industrials | large | unknown | 2026-09-27 |
| HAL | $32.76 | 26,249,020 | Energy | large | unknown | 2026-09-27 |
| HBAN | $15.63 | 24,860,093 | Financials | large | unknown | 2026-09-27 |
| HCA | $435.64 | 30,738,180 | Health Care | large | unknown | 2026-09-27 |
| HD | $293.18 | 57,880,929 | Consumer Discretionary | large | unknown | 2026-09-27 |
| HL | $18.20 | 21,888,689 | Unknown | mid | unknown | 2026-09-27 |
| HLT | $314.10 | 29,498,024 | Consumer Discretionary | large | unknown | 2026-09-27 |
| HON | $212.55 | 21,498,804 | Industrials | large | unknown | 2026-09-27 |
| HONA | $158.78 | 31,813,479 | Unknown | large | unknown | 2026-09-27 |
| HOOD | $119.39 | 78,159,205 | Unknown | large | unknown | 2026-09-27 |
| HPE | $62.94 | 72,064,938 | Information Technology | large | unknown | 2026-09-27 |
| HPQ | $31.30 | 37,331,382 | Information Technology | large | unknown | 2026-09-27 |
| HUM | $398.16 | 20,666,037 | Health Care | large | unknown | 2026-09-27 |
| HWM | $232.59 | 48,201,812 | Industrials | large | unknown | 2026-09-27 |
| IBM | $225.54 | 45,287,636 | Information Technology | large | unknown | 2026-09-27 |
| ICE | $154.31 | 25,597,666 | Financials | large | unknown | 2026-09-27 |
| ILMN | $270.06 | 37,745,938 | Health Care | large | unknown | 2026-09-27 |
| INTC | $122.98 | 272,011,962 | Information Technology | large | unknown | 2026-09-27 |
| INTU | $275.70 | 55,140,970 | Information Technology | large | unknown | 2026-09-27 |
| IQV | $270.26 | 23,525,596 | Health Care | large | unknown | 2026-09-27 |
| ISRG | $405.12 | 45,793,822 | Health Care | large | unknown | 2026-09-27 |
| JBL | $316.70 | 22,573,859 | Unknown | large | unknown | 2026-09-27 |
| JNJ | $271.20 | 63,402,254 | Health Care | large | unknown | 2026-09-27 |
| JPM | $342.88 | 94,156,299 | Financials | large | unknown | 2026-09-27 |
| KDP | $31.95 | 21,185,609 | Consumer Staples | large | unknown | 2026-09-27 |
| KHC | $23.63 | 26,505,071 | Consumer Staples | large | unknown | 2026-09-27 |
| KKR | $96.67 | 24,407,381 | Unknown | large | unknown | 2026-09-27 |
| KLAC | $187.92 | 56,286,603 | Information Technology | large | unknown | 2026-09-27 |
| KMI | $30.75 | 28,955,614 | Energy | large | unknown | 2026-09-27 |
| KO | $87.81 | 78,451,162 | Consumer Staples | large | unknown | 2026-09-27 |
| KR | $58.75 | 29,163,185 | Consumer Staples | large | unknown | 2026-09-27 |
| KVUE | $17.81 | 38,369,733 | Unknown | large | unknown | 2026-09-27 |
| LHX | $237.61 | 21,142,089 | Industrials | large | unknown | 2026-09-27 |
| LIN | $469.77 | 38,757,895 | Materials | large | unknown | 2026-09-27 |
| LITE | $941.41 | 120,096,697 | Unknown | large | unknown | 2026-09-27 |
| LLY | $1183.99 | 96,938,597 | Health Care | large | unknown | 2026-09-27 |
| LMT | $519.49 | 21,876,592 | Industrials | large | unknown | 2026-09-27 |
| LOW | $189.22 | 28,406,482 | Consumer Discretionary | large | unknown | 2026-09-27 |
| LRCX | $315.19 | 108,403,244 | Information Technology | large | unknown | 2026-09-27 |
| LULU | $101.34 | 25,505,607 | Unknown | large | unknown | 2026-09-27 |
| MA | $567.50 | 64,832,171 | Financials | large | unknown | 2026-09-27 |
| MAR | $352.03 | 29,893,698 | Unknown | large | unknown | 2026-09-27 |
| MCD | $236.53 | 50,022,972 | Consumer Discretionary | large | unknown | 2026-09-27 |
| MCHP | $78.64 | 22,057,901 | Information Technology | large | unknown | 2026-09-27 |
| MCK | $866.22 | 32,813,497 | Health Care | large | unknown | 2026-09-27 |
| MDLZ | $60.25 | 29,742,798 | Consumer Staples | large | unknown | 2026-09-27 |
| MDT | $88.60 | 52,298,623 | Health Care | large | unknown | 2026-09-27 |
| META | $751.26 | 513,108,948 | Communication Services | large | unknown | 2026-09-27 |
| MLM | $484.20 | 34,612,195 | Materials | large | unknown | 2026-09-27 |
| MMM | $169.50 | 21,594,117 | Industrials | large | unknown | 2026-09-27 |
| MNST | $43.10 | 22,649,469 | Consumer Staples | large | unknown | 2026-09-27 |
| MO | $68.81 | 27,992,484 | Consumer Staples | large | unknown | 2026-09-27 |
| MPC | $393.26 | 51,280,634 | Energy | large | unknown | 2026-09-27 |
| MPWR | $1366.90 | 42,336,767 | Information Technology | large | unknown | 2026-09-27 |
| MRK | $148.77 | 46,062,619 | Health Care | large | unknown | 2026-09-27 |
| MRNA | $198.84 | 68,588,124 | Health Care | large | unknown | 2026-09-27 |
| MRVL | $261.80 | 102,906,072 | Unknown | large | unknown | 2026-09-27 |
| MS | $196.32 | 43,113,400 | Financials | large | unknown | 2026-09-27 |
| MSFT | $516.15 | 324,639,680 | Information Technology | large | unknown | 2026-09-27 |
| MSI | $456.77 | 25,232,882 | Information Technology | large | unknown | 2026-09-27 |
| MTZ | $212.78 | 24,159,620 | Unknown | mid | unknown | 2026-09-27 |
| MU | $1082.01 | 558,549,203 | Information Technology | large | unknown | 2026-09-27 |
| NEE | $76.08 | 61,177,176 | Utilities | large | unknown | 2026-09-27 |
| NEM | $121.41 | 32,418,200 | Materials | large | unknown | 2026-09-27 |
| NFLX | $71.14 | 113,128,218 | Communication Services | large | unknown | 2026-09-27 |
| NKE | $35.75 | 53,771,220 | Consumer Discretionary | large | unknown | 2026-09-27 |
| NOC | $510.51 | 22,454,859 | Industrials | large | unknown | 2026-09-27 |
| NOW | $135.62 | 75,906,198 | Information Technology | large | unknown | 2026-09-27 |
| NTAP | $201.23 | 23,008,259 | Information Technology | large | unknown | 2026-09-27 |
| NVDA | $225.04 | 647,946,613 | Information Technology | large | unknown | 2026-09-27 |
| NXPI | $238.03 | 25,791,622 | Unknown | large | unknown | 2026-09-27 |
| O | $55.53 | 23,645,498 | Real Estate | large | unknown | 2026-09-27 |
| OKTA | $195.16 | 38,412,696 | Information Technology | mid | unknown | 2026-09-27 |
| ON | $77.18 | 31,766,752 | Information Technology | large | unknown | 2026-09-27 |
| ORCL | $137.06 | 143,858,328 | Information Technology | large | unknown | 2026-09-27 |
| ORLY | $86.11 | 23,272,425 | Consumer Discretionary | large | unknown | 2026-09-27 |
| OXY | $56.87 | 34,778,546 | Energy | large | unknown | 2026-09-27 |
| P | $125.98 | 20,456,404 | Unknown | large | unknown | 2026-09-27 |
| PANW | $374.56 | 91,629,180 | Unknown | large | unknown | 2026-09-27 |
| PATH | $12.47 | 26,133,826 | Unknown | mid | unknown | 2026-09-27 |
| PCG | $12.32 | 55,682,013 | Utilities | large | unknown | 2026-09-27 |
| PEP | $128.62 | 42,956,989 | Consumer Staples | large | unknown | 2026-09-27 |
| PFE | $28.68 | 46,051,243 | Health Care | large | unknown | 2026-09-27 |
| PG | $146.24 | 53,027,999 | Consumer Staples | large | unknown | 2026-09-27 |
| PGR | $205.47 | 32,762,663 | Financials | large | unknown | 2026-09-27 |
| PH | $977.39 | 29,078,291 | Industrials | large | unknown | 2026-09-27 |
| PLTR | $189.63 | 111,188,840 | Unknown | large | unknown | 2026-09-27 |
| PM | $190.49 | 32,328,619 | Consumer Staples | large | unknown | 2026-09-27 |
| PSX | $255.70 | 39,732,027 | Energy | large | unknown | 2026-09-27 |
| PWR | $648.99 | 28,454,609 | Industrials | large | unknown | 2026-09-27 |
| PYPL | $55.05 | 32,205,856 | Financials | large | unknown | 2026-09-27 |
| QCOM | $202.03 | 76,507,781 | Information Technology | large | unknown | 2026-09-27 |
| RCL | $242.76 | 42,237,320 | Consumer Discretionary | large | unknown | 2026-09-27 |
| RDDT | $149.98 | 29,504,317 | Unknown | large | unknown | 2026-09-27 |
| REGN | $787.54 | 20,963,474 | Health Care | large | unknown | 2026-09-27 |
| ROST | $236.00 | 21,977,796 | Consumer Discretionary | large | unknown | 2026-09-27 |
| RTX | $189.37 | 28,106,582 | Industrials | large | unknown | 2026-09-27 |
| SBUX | $94.88 | 27,249,900 | Consumer Discretionary | large | unknown | 2026-09-27 |
| SCHW | $99.02 | 42,854,640 | Financials | large | unknown | 2026-09-27 |
| SHW | $328.98 | 21,817,132 | Materials | large | unknown | 2026-09-27 |
| SLB | $51.55 | 43,778,288 | Energy | large | unknown | 2026-09-27 |
| SMCI | $43.26 | 61,569,296 | Information Technology | large | unknown | 2026-09-27 |
| SMTC | $182.30 | 30,020,042 | Information Technology | mid | unknown | 2026-09-27 |
| SNDK | $1777.01 | 350,733,319 | Unknown | large | unknown | 2026-09-27 |
| SNPS | $425.88 | 34,227,859 | Information Technology | large | unknown | 2026-09-27 |
| SO | $82.90 | 22,877,656 | Utilities | large | unknown | 2026-09-27 |
| SPGI | $403.27 | 38,158,108 | Financials | large | unknown | 2026-09-27 |
| STX | $916.75 | 124,597,499 | Information Technology | large | unknown | 2026-09-27 |
| SWKS | $89.36 | 30,938,935 | Information Technology | large | unknown | 2026-09-27 |
| SYK | $272.41 | 48,825,072 | Health Care | large | unknown | 2026-09-27 |
| T | $25.39 | 49,377,208 | Communication Services | large | unknown | 2026-09-27 |
| TDG | $1116.30 | 24,614,923 | Industrials | large | unknown | 2026-09-27 |
| TEL | $218.64 | 23,384,540 | Information Technology | large | unknown | 2026-09-27 |
| TER | $398.13 | 35,748,998 | Information Technology | large | unknown | 2026-09-27 |
| TFC | $47.65 | 20,426,846 | Financials | large | unknown | 2026-09-27 |
| TGT | $157.43 | 23,656,278 | Consumer Discretionary | large | unknown | 2026-09-27 |
| TJX | $130.09 | 57,258,748 | Consumer Discretionary | large | unknown | 2026-09-27 |
| TMO | $674.65 | 76,486,974 | Health Care | large | unknown | 2026-09-27 |
| TMUS | $165.49 | 42,117,360 | Communication Services | large | unknown | 2026-09-27 |
| TRV | $362.92 | 20,741,196 | Financials | large | unknown | 2026-09-27 |
| TSLA | $372.09 | 274,582,413 | Consumer Discretionary | large | unknown | 2026-09-27 |
| TT | $454.48 | 23,837,295 | Industrials | large | unknown | 2026-09-27 |
| TTWO | $201.33 | 27,643,591 | Communication Services | large | unknown | 2026-09-27 |
| TWLO | $275.82 | 32,228,853 | Unknown | mid | unknown | 2026-09-27 |
| TXN | $277.96 | 56,476,109 | Information Technology | large | unknown | 2026-09-27 |
| UBER | $69.60 | 52,167,456 | Unknown | large | unknown | 2026-09-27 |
| UNH | $376.70 | 69,872,187 | Health Care | large | unknown | 2026-09-27 |
| UNP | $273.60 | 34,685,653 | Industrials | large | unknown | 2026-09-27 |
| URI | $1046.75 | 24,233,598 | Industrials | large | unknown | 2026-09-27 |
| USB | $59.32 | 30,002,811 | Financials | large | unknown | 2026-09-27 |
| V | $367.34 | 78,604,103 | Financials | large | unknown | 2026-09-27 |
| VEEV | $280.81 | 20,297,289 | Unknown | large | unknown | 2026-09-27 |
| VLO | $387.10 | 67,018,756 | Energy | large | unknown | 2026-09-27 |
| VRT | $253.24 | 67,266,154 | Unknown | large | unknown | 2026-09-27 |
| VRTX | $526.28 | 23,594,339 | Health Care | large | unknown | 2026-09-27 |
| VST | $138.47 | 24,745,479 | Utilities | large | unknown | 2026-09-27 |
| VZ | $47.09 | 52,205,680 | Communication Services | large | unknown | 2026-09-27 |
| WBD | $30.86 | 77,155,423 | Communication Services | large | unknown | 2026-09-27 |
| WDAY | $189.42 | 28,413,673 | Unknown | large | unknown | 2026-09-27 |
| WDC | $456.61 | 105,899,132 | Information Technology | large | unknown | 2026-09-27 |
| WELL | $231.41 | 23,406,895 | Real Estate | large | unknown | 2026-09-27 |
| WFC | $82.97 | 61,435,859 | Financials | large | unknown | 2026-09-27 |
| WM | $206.80 | 21,875,106 | Industrials | large | unknown | 2026-09-27 |
| WMB | $69.28 | 26,709,216 | Energy | large | unknown | 2026-09-27 |
| WMT | $107.97 | 90,200,034 | Consumer Staples | large | unknown | 2026-09-27 |
| WWD | $330.40 | 20,093,453 | Industrials | mid | unknown | 2026-09-27 |
| XEL | $69.79 | 27,344,694 | Utilities | large | unknown | 2026-09-27 |
| XOM | $160.56 | 66,133,069 | Energy | large | unknown | 2026-09-27 |
