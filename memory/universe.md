---
screened_on: 2026-11-08
expires_on: 2026-11-15
total_passed: 347
total_rejected: 1184
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
| A | $174.81 | 23,326,736 | Unknown | large | unknown | 2026-11-08 |
| AAL | $13.16 | 31,965,282 | Industrials | mid | unknown | 2026-11-08 |
| AAPL | $342.41 | 476,184,295 | Information Technology | large | unknown | 2026-11-08 |
| ABBV | $291.53 | 73,416,897 | Health Care | large | unknown | 2026-11-08 |
| ABNB | $190.01 | 37,959,778 | Consumer Discretionary | large | unknown | 2026-11-08 |
| ABT | $109.98 | 59,584,416 | Health Care | large | unknown | 2026-11-08 |
| ACN | $260.51 | 80,313,199 | Information Technology | large | unknown | 2026-11-08 |
| ADBE | $239.25 | 41,050,093 | Information Technology | large | unknown | 2026-11-08 |
| ADI | $363.14 | 69,481,391 | Information Technology | large | unknown | 2026-11-08 |
| ADP | $303.30 | 29,021,692 | Industrials | large | unknown | 2026-11-08 |
| ADSK | $261.82 | 30,558,195 | Information Technology | large | unknown | 2026-11-08 |
| AEP | $126.50 | 20,542,903 | Utilities | large | unknown | 2026-11-08 |
| AIG | $77.75 | 26,954,647 | Financials | large | unknown | 2026-11-08 |
| AJG | $281.57 | 30,257,751 | Financials | large | unknown | 2026-11-08 |
| AKAM | $83.04 | 27,568,039 | Information Technology | large | unknown | 2026-11-08 |
| ALL | $254.77 | 26,823,721 | Unknown | large | unknown | 2026-11-08 |
| AMAT | $332.70 | 133,025,875 | Information Technology | large | unknown | 2026-11-08 |
| AMD | $447.46 | 382,598,527 | Information Technology | large | unknown | 2026-11-08 |
| AME | $228.53 | 24,603,727 | Industrials | large | unknown | 2026-11-08 |
| AMGN | $460.26 | 47,488,514 | Health Care | large | unknown | 2026-11-08 |
| AMT | $188.84 | 31,649,297 | Real Estate | large | unknown | 2026-11-08 |
| AMZN | $259.45 | 462,815,536 | Consumer Discretionary | large | unknown | 2026-11-08 |
| ANET | $170.68 | 78,195,614 | Information Technology | large | unknown | 2026-11-08 |
| AON | $334.85 | 33,957,558 | Financials | large | unknown | 2026-11-08 |
| APH | $74.60 | 63,960,097 | Information Technology | large | unknown | 2026-11-08 |
| APO | $116.76 | 25,310,271 | Financials | large | unknown | 2026-11-08 |
| APP | $391.26 | 63,703,700 | Unknown | large | unknown | 2026-11-08 |
| ARES | $133.97 | 21,388,807 | Unknown | large | unknown | 2026-11-08 |
| ATI | $175.63 | 23,167,309 | Materials | mid | unknown | 2026-11-08 |
| AVGO | $293.41 | 256,486,478 | Information Technology | large | unknown | 2026-11-08 |
| AWK | $150.31 | 23,825,889 | Utilities | large | unknown | 2026-11-08 |
| AXON | $312.88 | 23,493,979 | Industrials | large | unknown | 2026-11-08 |
| AXP | $321.09 | 44,439,447 | Unknown | large | unknown | 2026-11-08 |
| AZO | $3215.06 | 34,452,555 | Consumer Discretionary | large | unknown | 2026-11-08 |
| BA | $173.40 | 77,065,035 | Industrials | large | unknown | 2026-11-08 |
| BAC | $49.41 | 161,065,397 | Financials | large | unknown | 2026-11-08 |
| BDX | $211.95 | 23,160,013 | Health Care | large | unknown | 2026-11-08 |
| BE | $173.06 | 115,213,703 | Unknown | large | unknown | 2026-11-08 |
| BKNG | $160.68 | 71,361,906 | Consumer Discretionary | large | unknown | 2026-11-08 |
| BKR | $47.87 | 26,586,796 | Unknown | large | unknown | 2026-11-08 |
| BLK | $1178.91 | 55,439,717 | Unknown | large | unknown | 2026-11-08 |
| BMY | $62.14 | 41,552,886 | Health Care | large | unknown | 2026-11-08 |
| BNY | $147.72 | 24,597,706 | Unknown | large | unknown | 2026-11-08 |
| BRK.B | $571.12 | 96,062,789 | Financials | large | unknown | 2026-11-08 |
| BSX | $42.75 | 79,298,900 | Health Care | large | unknown | 2026-11-08 |
| BURL | $246.67 | 26,746,702 | Unknown | mid | unknown | 2026-11-08 |
| BX | $119.50 | 35,725,091 | Financials | large | unknown | 2026-11-08 |
| C | $119.08 | 54,125,120 | Financials | large | unknown | 2026-11-08 |
| CAH | $271.61 | 25,238,558 | Unknown | large | unknown | 2026-11-08 |
| CARR | $52.35 | 21,784,143 | Unknown | large | unknown | 2026-11-08 |
| CART | $58.14 | 29,683,620 | Unknown | mid | unknown | 2026-11-08 |
| CASY | $688.18 | 20,203,411 | Consumer Staples | large | unknown | 2026-11-08 |
| CAT | $558.66 | 122,663,046 | Industrials | large | unknown | 2026-11-08 |
| CB | $365.06 | 31,353,346 | Financials | large | unknown | 2026-11-08 |
| CBOE | $353.28 | 24,978,676 | Unknown | large | unknown | 2026-11-08 |
| CCI | $88.61 | 29,539,884 | Unknown | large | unknown | 2026-11-08 |
| CCL | $29.59 | 37,251,258 | Unknown | large | unknown | 2026-11-08 |
| CDE | $15.47 | 21,679,163 | Unknown | mid | unknown | 2026-11-08 |
| CDNS | $320.04 | 49,273,787 | Unknown | large | unknown | 2026-11-08 |
| CEG | $249.77 | 45,810,195 | Unknown | large | unknown | 2026-11-08 |
| CFG | $63.25 | 21,119,332 | Financials | large | unknown | 2026-11-08 |
| CI | $293.62 | 24,800,333 | Health Care | large | unknown | 2026-11-08 |
| CIEN | $243.28 | 60,809,813 | Unknown | large | unknown | 2026-11-08 |
| CL | $96.54 | 27,563,266 | Consumer Staples | large | unknown | 2026-11-08 |
| CMCSA | $24.39 | 51,193,974 | Unknown | large | unknown | 2026-11-08 |
| CME | $305.98 | 30,801,939 | Financials | large | unknown | 2026-11-08 |
| CMG | $34.42 | 49,538,257 | Consumer Discretionary | large | unknown | 2026-11-08 |
| CMI | $450.18 | 42,249,179 | Industrials | large | unknown | 2026-11-08 |
| CMS | $69.19 | 23,733,054 | Unknown | large | unknown | 2026-11-08 |
| CNC | $69.73 | 25,540,260 | Unknown | large | unknown | 2026-11-08 |
| CNP | $40.68 | 34,748,726 | Unknown | large | unknown | 2026-11-08 |
| COF | $201.96 | 45,099,814 | Financials | large | unknown | 2026-11-08 |
| COHR | $192.79 | 86,383,154 | Unknown | large | unknown | 2026-11-08 |
| COIN | $134.70 | 43,836,489 | Unknown | large | unknown | 2026-11-08 |
| COP | $136.33 | 44,392,071 | Energy | large | unknown | 2026-11-08 |
| COR | $333.54 | 28,910,844 | Unknown | large | unknown | 2026-11-08 |
| COST | $1053.46 | 97,845,131 | Consumer Staples | large | unknown | 2026-11-08 |
| CPRT | $31.95 | 27,969,343 | Industrials | large | unknown | 2026-11-08 |
| CRH | $94.84 | 26,056,313 | Unknown | large | unknown | 2026-11-08 |
| CRL | $337.36 | 31,700,072 | Health Care | large | unknown | 2026-11-08 |
| CRM | $213.64 | 79,926,712 | Information Technology | large | unknown | 2026-11-08 |
| CRS | $278.51 | 26,056,611 | Materials | mid | unknown | 2026-11-08 |
| CRWD | $216.97 | 81,672,165 | Information Technology | large | unknown | 2026-11-08 |
| CSCO | $93.80 | 70,289,130 | Information Technology | large | unknown | 2026-11-08 |
| CSX | $49.10 | 50,444,966 | Industrials | large | unknown | 2026-11-08 |
| CTAS | $222.43 | 21,716,666 | Industrials | large | unknown | 2026-11-08 |
| CTSH | $64.74 | 25,770,648 | Information Technology | large | unknown | 2026-11-08 |
| CVNA | $73.50 | 41,000,934 | Unknown | large | unknown | 2026-11-08 |
| CVS | $83.84 | 53,083,362 | Health Care | large | unknown | 2026-11-08 |
| CVX | $212.63 | 69,888,769 | Energy | large | unknown | 2026-11-08 |
| D | $68.61 | 29,629,021 | Utilities | large | unknown | 2026-11-08 |
| DAL | $87.20 | 29,372,750 | Industrials | large | unknown | 2026-11-08 |
| DASH | $179.58 | 64,172,751 | Unknown | large | unknown | 2026-11-08 |
| DDOG | $179.16 | 52,341,930 | Unknown | large | unknown | 2026-11-08 |
| DE | $673.28 | 43,369,117 | Industrials | large | unknown | 2026-11-08 |
| DELL | $328.53 | 134,831,147 | Information Technology | large | unknown | 2026-11-08 |
| DHI | $152.26 | 23,940,394 | Consumer Discretionary | large | unknown | 2026-11-08 |
| DHR | $230.36 | 62,174,842 | Health Care | large | unknown | 2026-11-08 |
| DIS | $116.73 | 44,171,184 | Communication Services | large | unknown | 2026-11-08 |
| DKS | $140.87 | 20,959,822 | Consumer Discretionary | mid | unknown | 2026-11-08 |
| DLR | $173.96 | 28,364,522 | Unknown | large | unknown | 2026-11-08 |
| DOCN | $72.50 | 23,018,870 | Unknown | mid | unknown | 2026-11-08 |
| DOW | $31.39 | 20,129,276 | Materials | large | unknown | 2026-11-08 |
| DT | $43.44 | 32,561,605 | Unknown | mid | unknown | 2026-11-08 |
| DUK | $127.80 | 25,332,167 | Utilities | large | unknown | 2026-11-08 |
| DVN | $42.23 | 42,933,161 | Energy | large | unknown | 2026-11-08 |
| DXCM | $79.41 | 23,044,228 | Health Care | large | unknown | 2026-11-08 |
| EAT | $206.61 | 22,179,945 | Consumer Discretionary | mid | unknown | 2026-11-08 |
| EBAY | $121.95 | 29,239,381 | Consumer Discretionary | large | unknown | 2026-11-08 |
| ECHO | $94.62 | 24,473,542 | Unknown | large | unknown | 2026-11-08 |
| ECL | $300.69 | 31,235,476 | Materials | large | unknown | 2026-11-08 |
| EFX | $189.62 | 22,811,597 | Industrials | large | unknown | 2026-11-08 |
| EL | $110.11 | 25,560,138 | Consumer Staples | large | unknown | 2026-11-08 |
| ELV | $425.73 | 37,948,370 | Unknown | large | unknown | 2026-11-08 |
| EME | $608.25 | 21,325,642 | Unknown | large | unknown | 2026-11-08 |
| EMR | $162.27 | 24,906,316 | Industrials | large | unknown | 2026-11-08 |
| ENTG | $128.13 | 22,281,607 | Unknown | mid | unknown | 2026-11-08 |
| EOG | $147.23 | 25,299,607 | Energy | large | unknown | 2026-11-08 |
| EQIX | $1012.56 | 46,252,605 | Real Estate | large | unknown | 2026-11-08 |
| EQT | $49.40 | 43,358,414 | Unknown | large | unknown | 2026-11-08 |
| ETN | $341.77 | 76,219,957 | Industrials | large | unknown | 2026-11-08 |
| EW | $102.13 | 27,657,391 | Health Care | large | unknown | 2026-11-08 |
| EXC | $45.62 | 27,912,891 | Utilities | large | unknown | 2026-11-08 |
| EXPE | $259.12 | 33,237,155 | Consumer Discretionary | large | unknown | 2026-11-08 |
| F | $12.45 | 24,318,484 | Consumer Discretionary | large | unknown | 2026-11-08 |
| FANG | $178.92 | 20,550,369 | Unknown | large | unknown | 2026-11-08 |
| FAST | $52.98 | 29,855,635 | Industrials | large | unknown | 2026-11-08 |
| FCX | $59.42 | 44,741,924 | Materials | large | unknown | 2026-11-08 |
| FDX | $308.21 | 35,567,065 | Industrials | large | unknown | 2026-11-08 |
| FERG | $233.70 | 20,466,414 | Unknown | large | unknown | 2026-11-08 |
| FFIV | $310.86 | 22,936,957 | Information Technology | large | unknown | 2026-11-08 |
| FICO | $704.95 | 29,678,506 | Information Technology | large | unknown | 2026-11-08 |
| FIS | $28.72 | 21,000,345 | Financials | large | unknown | 2026-11-08 |
| FISV | $62.88 | 27,471,301 | Unknown | large | unknown | 2026-11-08 |
| FITB | $53.05 | 38,625,556 | Financials | large | unknown | 2026-11-08 |
| FIX | $1016.58 | 63,922,060 | Unknown | large | unknown | 2026-11-08 |
| FLEX | $69.76 | 34,116,690 | Unknown | large | unknown | 2026-11-08 |
| FN | $327.29 | 28,979,933 | Unknown | mid | unknown | 2026-11-08 |
| FOXA | $66.66 | 23,426,679 | Communication Services | large | unknown | 2026-11-08 |
| FSLR | $201.10 | 23,018,832 | Unknown | large | unknown | 2026-11-08 |
| FTNT | $118.78 | 33,545,359 | Information Technology | large | unknown | 2026-11-08 |
| GD | $354.08 | 22,355,534 | Industrials | large | unknown | 2026-11-08 |
| GE | $323.30 | 91,538,743 | Industrials | large | unknown | 2026-11-08 |
| GEV | $774.16 | 162,721,059 | Industrials | large | unknown | 2026-11-08 |
| GILD | $166.87 | 52,240,629 | Health Care | large | unknown | 2026-11-08 |
| GIS | $35.51 | 20,526,618 | Consumer Staples | large | unknown | 2026-11-08 |
| GKOS | $224.20 | 21,051,570 | Health Care | mid | unknown | 2026-11-08 |
| GLW | $106.16 | 72,874,990 | Information Technology | large | unknown | 2026-11-08 |
| GM | $86.18 | 35,034,580 | Consumer Discretionary | large | unknown | 2026-11-08 |
| GOOG | $283.73 | 204,276,320 | Communication Services | large | unknown | 2026-11-08 |
| GOOGL | $284.72 | 376,041,431 | Communication Services | large | unknown | 2026-11-08 |
| GS | $865.97 | 92,580,523 | Financials | large | unknown | 2026-11-08 |
| GWW | $1440.66 | 25,873,894 | Industrials | large | unknown | 2026-11-08 |
| HAL | $31.84 | 27,119,785 | Energy | large | unknown | 2026-11-08 |
| HBAN | $15.49 | 20,163,799 | Financials | large | unknown | 2026-11-08 |
| HCA | $494.75 | 43,200,118 | Health Care | large | unknown | 2026-11-08 |
| HD | $343.43 | 75,851,379 | Consumer Discretionary | large | unknown | 2026-11-08 |
| HLT | $370.47 | 53,261,384 | Consumer Discretionary | large | unknown | 2026-11-08 |
| HON | $220.10 | 24,437,096 | Industrials | large | unknown | 2026-11-08 |
| HONA | $153.02 | 24,667,161 | Unknown | large | unknown | 2026-11-08 |
| HOOD | $80.91 | 58,946,482 | Unknown | large | unknown | 2026-11-08 |
| HPE | $44.75 | 60,011,587 | Information Technology | large | unknown | 2026-11-08 |
| HPQ | $28.46 | 32,072,385 | Information Technology | large | unknown | 2026-11-08 |
| HUBB | $429.54 | 24,916,446 | Industrials | large | unknown | 2026-11-08 |
| HUM | $433.84 | 32,763,312 | Health Care | large | unknown | 2026-11-08 |
| HWM | $205.86 | 59,730,814 | Industrials | large | unknown | 2026-11-08 |
| IBKR | $75.82 | 23,952,649 | Unknown | large | unknown | 2026-11-08 |
| IBM | $244.99 | 51,228,146 | Information Technology | large | unknown | 2026-11-08 |
| ICE | $172.30 | 34,202,366 | Financials | large | unknown | 2026-11-08 |
| IDXX | $676.26 | 26,325,964 | Health Care | large | unknown | 2026-11-08 |
| ILMN | $213.07 | 42,226,839 | Health Care | large | unknown | 2026-11-08 |
| INTC | $56.31 | 333,398,253 | Information Technology | large | unknown | 2026-11-08 |
| INTU | $341.53 | 55,515,672 | Information Technology | large | unknown | 2026-11-08 |
| IQV | $271.73 | 27,003,038 | Health Care | large | unknown | 2026-11-08 |
| IR | $82.97 | 21,017,186 | Industrials | large | unknown | 2026-11-08 |
| ISRG | $452.76 | 63,974,236 | Health Care | large | unknown | 2026-11-08 |
| ITW | $280.99 | 21,943,601 | Industrials | large | unknown | 2026-11-08 |
| JBL | $239.04 | 25,655,184 | Unknown | large | unknown | 2026-11-08 |
| JCI | $134.97 | 46,817,483 | Industrials | large | unknown | 2026-11-08 |
| JNJ | $276.33 | 91,118,785 | Health Care | large | unknown | 2026-11-08 |
| JPM | $334.46 | 87,644,989 | Financials | large | unknown | 2026-11-08 |
| KDP | $36.61 | 50,382,266 | Consumer Staples | large | unknown | 2026-11-08 |
| KEYS | $271.73 | 28,369,316 | Information Technology | large | unknown | 2026-11-08 |
| KHC | $24.62 | 20,880,107 | Consumer Staples | large | unknown | 2026-11-08 |
| KKR | $96.44 | 25,224,418 | Unknown | large | unknown | 2026-11-08 |
| KLAC | $137.94 | 89,761,594 | Information Technology | large | unknown | 2026-11-08 |
| KMB | $108.44 | 31,366,045 | Consumer Staples | large | unknown | 2026-11-08 |
| KMI | $29.96 | 39,682,559 | Energy | large | unknown | 2026-11-08 |
| KO | $95.67 | 110,040,648 | Consumer Staples | large | unknown | 2026-11-08 |
| KR | $67.69 | 31,204,310 | Consumer Staples | large | unknown | 2026-11-08 |
| LHX | $260.08 | 29,023,957 | Industrials | large | unknown | 2026-11-08 |
| LIN | $515.19 | 49,024,668 | Materials | large | unknown | 2026-11-08 |
| LITE | $538.08 | 212,580,562 | Unknown | large | unknown | 2026-11-08 |
| LLY | $1354.77 | 180,923,934 | Health Care | large | unknown | 2026-11-08 |
| LMT | $567.13 | 45,188,461 | Industrials | large | unknown | 2026-11-08 |
| LOW | $224.60 | 34,731,996 | Consumer Discretionary | large | unknown | 2026-11-08 |
| LRCX | $200.30 | 128,050,122 | Information Technology | large | unknown | 2026-11-08 |
| LYV | $175.44 | 22,339,716 | Communication Services | large | unknown | 2026-11-08 |
| MA | $652.87 | 136,413,775 | Financials | large | unknown | 2026-11-08 |
| MAR | $416.47 | 35,063,859 | Unknown | large | unknown | 2026-11-08 |
| MCD | $276.45 | 55,417,944 | Consumer Discretionary | large | unknown | 2026-11-08 |
| MCHP | $58.33 | 46,612,219 | Information Technology | large | unknown | 2026-11-08 |
| MCK | $1060.65 | 45,183,370 | Health Care | large | unknown | 2026-11-08 |
| MCO | $505.73 | 29,829,325 | Financials | large | unknown | 2026-11-08 |
| MDLZ | $66.00 | 37,759,826 | Consumer Staples | large | unknown | 2026-11-08 |
| MDT | $101.80 | 59,479,260 | Health Care | large | unknown | 2026-11-08 |
| META | $610.12 | 605,998,495 | Communication Services | large | unknown | 2026-11-08 |
| MKSI | $192.22 | 24,168,188 | Information Technology | mid | unknown | 2026-11-08 |
| MLM | $518.16 | 33,088,800 | Materials | large | unknown | 2026-11-08 |
| MMM | $185.23 | 33,900,697 | Industrials | large | unknown | 2026-11-08 |
| MNST | $45.70 | 32,116,050 | Consumer Staples | large | unknown | 2026-11-08 |
| MO | $76.13 | 34,767,135 | Consumer Staples | large | unknown | 2026-11-08 |
| MPC | $372.91 | 51,540,097 | Energy | large | unknown | 2026-11-08 |
| MPWR | $1188.02 | 58,133,768 | Information Technology | large | unknown | 2026-11-08 |
| MRK | $146.75 | 70,525,833 | Health Care | large | unknown | 2026-11-08 |
| MRNA | $254.49 | 108,454,837 | Health Care | large | unknown | 2026-11-08 |
| MRSH | $204.84 | 27,343,709 | Unknown | large | unknown | 2026-11-08 |
| MRVL | $141.08 | 164,773,967 | Unknown | large | unknown | 2026-11-08 |
| MS | $181.41 | 73,076,176 | Financials | large | unknown | 2026-11-08 |
| MSCI | $641.08 | 26,535,231 | Financials | large | unknown | 2026-11-08 |
| MSFT | $530.58 | 439,754,108 | Information Technology | large | unknown | 2026-11-08 |
| MSI | $514.34 | 32,770,309 | Information Technology | large | unknown | 2026-11-08 |
| MTD | $1721.59 | 24,409,652 | Health Care | large | unknown | 2026-11-08 |
| MTSI | $210.84 | 23,409,779 | Unknown | mid | unknown | 2026-11-08 |
| MTZ | $174.61 | 24,197,792 | Unknown | mid | unknown | 2026-11-08 |
| MU | $689.67 | 684,440,648 | Information Technology | large | unknown | 2026-11-08 |
| NCLH | $17.91 | 21,923,370 | Unknown | large | unknown | 2026-11-08 |
| NDAQ | $107.09 | 20,579,509 | Financials | large | unknown | 2026-11-08 |
| NEE | $86.95 | 86,098,842 | Utilities | large | unknown | 2026-11-08 |
| NEM | $120.90 | 35,631,427 | Materials | large | unknown | 2026-11-08 |
| NFLX | $63.39 | 165,480,666 | Communication Services | large | unknown | 2026-11-08 |
| NI | $44.15 | 23,027,027 | Utilities | large | unknown | 2026-11-08 |
| NKE | $38.59 | 51,368,913 | Consumer Discretionary | large | unknown | 2026-11-08 |
| NOC | $525.33 | 35,872,095 | Industrials | large | unknown | 2026-11-08 |
| NOW | $101.96 | 127,144,986 | Information Technology | large | unknown | 2026-11-08 |
| NTAP | $169.16 | 22,549,752 | Information Technology | large | unknown | 2026-11-08 |
| NUE | $244.89 | 21,440,434 | Materials | large | unknown | 2026-11-08 |
| NVDA | $186.70 | 794,753,869 | Information Technology | large | unknown | 2026-11-08 |
| NVR | $6309.17 | 21,978,390 | Consumer Discretionary | large | unknown | 2026-11-08 |
| NVT | $106.22 | 26,602,929 | Industrials | mid | unknown | 2026-11-08 |
| NXPI | $248.23 | 61,172,167 | Unknown | large | unknown | 2026-11-08 |
| O | $59.05 | 28,227,707 | Real Estate | large | unknown | 2026-11-08 |
| ODFL | $165.00 | 22,266,297 | Industrials | large | unknown | 2026-11-08 |
| OKTA | $168.75 | 46,151,902 | Information Technology | large | unknown | 2026-11-08 |
| ON | $63.42 | 33,178,064 | Information Technology | large | unknown | 2026-11-08 |
| ORCL | $116.07 | 195,141,027 | Information Technology | large | unknown | 2026-11-08 |
| ORLY | $89.93 | 24,945,172 | Consumer Discretionary | large | unknown | 2026-11-08 |
| OTIS | $78.97 | 24,270,598 | Unknown | large | unknown | 2026-11-08 |
| OXY | $56.41 | 46,599,940 | Energy | large | unknown | 2026-11-08 |
| P | $96.76 | 24,862,343 | Unknown | large | unknown | 2026-11-08 |
| PANW | $313.78 | 95,998,404 | Unknown | large | unknown | 2026-11-08 |
| PCG | $12.98 | 24,635,855 | Utilities | large | unknown | 2026-11-08 |
| PEP | $141.31 | 51,941,932 | Consumer Staples | large | unknown | 2026-11-08 |
| PFE | $29.39 | 57,003,648 | Health Care | large | unknown | 2026-11-08 |
| PG | $165.39 | 77,214,707 | Consumer Staples | large | unknown | 2026-11-08 |
| PGR | $227.80 | 32,988,578 | Financials | large | unknown | 2026-11-08 |
| PH | $917.21 | 49,198,436 | Industrials | large | unknown | 2026-11-08 |
| PINS | $18.95 | 21,843,315 | Unknown | mid | unknown | 2026-11-08 |
| PLD | $126.97 | 24,375,887 | Real Estate | large | unknown | 2026-11-08 |
| PLTR | $160.35 | 125,373,813 | Unknown | large | unknown | 2026-11-08 |
| PM | $197.83 | 50,400,740 | Consumer Staples | large | unknown | 2026-11-08 |
| PNC | $225.46 | 25,762,470 | Financials | large | unknown | 2026-11-08 |
| PPL | $35.82 | 22,014,890 | Utilities | large | unknown | 2026-11-08 |
| PSX | $245.65 | 49,459,647 | Energy | large | unknown | 2026-11-08 |
| PTC | $195.02 | 28,544,408 | Information Technology | large | unknown | 2026-11-08 |
| PWR | $540.86 | 67,832,455 | Industrials | large | unknown | 2026-11-08 |
| PYPL | $59.24 | 29,265,783 | Financials | large | unknown | 2026-11-08 |
| QCOM | $165.71 | 74,717,147 | Information Technology | large | unknown | 2026-11-08 |
| RCL | $326.95 | 39,882,341 | Consumer Discretionary | large | unknown | 2026-11-08 |
| RDDT | $95.09 | 35,242,243 | Unknown | large | unknown | 2026-11-08 |
| REGN | $904.61 | 43,772,736 | Health Care | large | unknown | 2026-11-08 |
| RF | $28.30 | 20,756,066 | Financials | large | unknown | 2026-11-08 |
| RMD | $235.35 | 23,090,399 | Health Care | large | unknown | 2026-11-08 |
| ROK | $375.77 | 30,360,240 | Industrials | large | unknown | 2026-11-08 |
| ROP | $476.71 | 28,159,512 | Industrials | large | unknown | 2026-11-08 |
| ROST | $231.00 | 24,297,888 | Consumer Discretionary | large | unknown | 2026-11-08 |
| RRC | $48.71 | 24,190,579 | Energy | mid | unknown | 2026-11-08 |
| RTX | $189.52 | 56,814,656 | Industrials | large | unknown | 2026-11-08 |
| RVTY | $155.13 | 21,614,565 | Unknown | large | unknown | 2026-11-08 |
| SBUX | $105.39 | 40,378,916 | Consumer Discretionary | large | unknown | 2026-11-08 |
| SCHW | $91.48 | 45,522,392 | Financials | large | unknown | 2026-11-08 |
| SHW | $344.05 | 34,168,569 | Materials | large | unknown | 2026-11-08 |
| SITM | $416.86 | 23,330,777 | Unknown | mid | unknown | 2026-11-08 |
| SLB | $49.91 | 51,327,365 | Energy | large | unknown | 2026-11-08 |
| SMCI | $28.75 | 54,464,727 | Information Technology | large | unknown | 2026-11-08 |
| SMTC | $103.34 | 29,226,346 | Information Technology | mid | unknown | 2026-11-08 |
| SN | $222.98 | 20,947,194 | Unknown | mid | unknown | 2026-11-08 |
| SNDK | $835.15 | 314,858,586 | Unknown | large | unknown | 2026-11-08 |
| SNPS | $450.32 | 60,000,040 | Information Technology | large | unknown | 2026-11-08 |
| SO | $92.33 | 38,724,704 | Utilities | large | unknown | 2026-11-08 |
| SPGI | $467.83 | 49,814,390 | Financials | large | unknown | 2026-11-08 |
| STRL | $252.87 | 26,171,319 | Unknown | mid | unknown | 2026-11-08 |
| STX | $460.95 | 170,539,192 | Information Technology | large | unknown | 2026-11-08 |
| SWKS | $82.20 | 23,323,525 | Information Technology | large | unknown | 2026-11-08 |
| SYK | $325.93 | 61,199,680 | Health Care | large | unknown | 2026-11-08 |
| T | $21.62 | 71,726,362 | Communication Services | large | unknown | 2026-11-08 |
| TDG | $1197.41 | 44,111,121 | Industrials | large | unknown | 2026-11-08 |
| TEL | $206.99 | 29,874,661 | Information Technology | large | unknown | 2026-11-08 |
| TER | $218.22 | 56,542,179 | Information Technology | large | unknown | 2026-11-08 |
| TFC | $49.39 | 33,674,104 | Financials | large | unknown | 2026-11-08 |
| TGT | $158.40 | 30,220,814 | Consumer Discretionary | large | unknown | 2026-11-08 |
| TJX | $135.31 | 39,063,860 | Consumer Discretionary | large | unknown | 2026-11-08 |
| TLN | $338.58 | 27,490,002 | Unknown | mid | unknown | 2026-11-08 |
| TMO | $695.02 | 107,835,404 | Health Care | large | unknown | 2026-11-08 |
| TMUS | $161.96 | 52,811,967 | Communication Services | large | unknown | 2026-11-08 |
| TOST | $34.66 | 24,327,820 | Unknown | mid | unknown | 2026-11-08 |
| TRGP | $264.60 | 25,386,094 | Unknown | large | unknown | 2026-11-08 |
| TRV | $395.22 | 25,871,696 | Financials | large | unknown | 2026-11-08 |
| TSCO | $36.34 | 34,121,123 | Consumer Discretionary | large | unknown | 2026-11-08 |
| TSLA | $358.21 | 346,718,653 | Consumer Discretionary | large | unknown | 2026-11-08 |
| TT | $402.06 | 49,887,374 | Industrials | large | unknown | 2026-11-08 |
| TTMI | $66.53 | 29,699,244 | Information Technology | mid | unknown | 2026-11-08 |
| TTWO | $214.89 | 26,002,393 | Communication Services | large | unknown | 2026-11-08 |
| TWLO | $201.96 | 41,712,310 | Unknown | large | unknown | 2026-11-08 |
| TXN | $276.76 | 97,193,534 | Information Technology | large | unknown | 2026-11-08 |
| TXRH | $184.02 | 20,494,859 | Consumer Discretionary | mid | unknown | 2026-11-08 |
| TYL | $420.70 | 23,874,578 | Information Technology | large | unknown | 2026-11-08 |
| UAL | $112.77 | 29,559,055 | Industrials | large | unknown | 2026-11-08 |
| UBER | $68.60 | 71,580,284 | Unknown | large | unknown | 2026-11-08 |
| UNH | $394.22 | 127,976,579 | Health Care | large | unknown | 2026-11-08 |
| UNP | $290.26 | 42,583,177 | Industrials | large | unknown | 2026-11-08 |
| UPS | $108.31 | 27,448,792 | Industrials | large | unknown | 2026-11-08 |
| URI | $1055.75 | 46,135,675 | Industrials | large | unknown | 2026-11-08 |
| USB | $59.46 | 35,276,167 | Financials | large | unknown | 2026-11-08 |
| UTHR | $562.28 | 22,295,369 | Health Care | mid | unknown | 2026-11-08 |
| V | $422.67 | 164,596,301 | Financials | large | unknown | 2026-11-08 |
| VEEV | $303.80 | 28,483,833 | Unknown | large | unknown | 2026-11-08 |
| VLO | $346.34 | 65,335,621 | Energy | large | unknown | 2026-11-08 |
| VMC | $282.86 | 21,710,072 | Materials | large | unknown | 2026-11-08 |
| VRT | $182.78 | 99,061,287 | Unknown | large | unknown | 2026-11-08 |
| VRTX | $546.99 | 50,556,794 | Health Care | large | unknown | 2026-11-08 |
| VST | $124.77 | 47,538,451 | Utilities | large | unknown | 2026-11-08 |
| VZ | $45.71 | 72,315,168 | Communication Services | large | unknown | 2026-11-08 |
| WAT | $457.80 | 35,613,497 | Health Care | large | unknown | 2026-11-08 |
| WCC | $292.69 | 24,451,516 | Unknown | mid | unknown | 2026-11-08 |
| WDAY | $192.98 | 23,253,826 | Unknown | large | unknown | 2026-11-08 |
| WDC | $263.56 | 137,589,151 | Information Technology | large | unknown | 2026-11-08 |
| WELL | $245.03 | 43,151,960 | Real Estate | large | unknown | 2026-11-08 |
| WFC | $83.94 | 91,322,217 | Financials | large | unknown | 2026-11-08 |
| WM | $236.36 | 32,306,722 | Industrials | large | unknown | 2026-11-08 |
| WMB | $64.09 | 46,066,650 | Energy | large | unknown | 2026-11-08 |
| WMT | $125.47 | 118,704,651 | Consumer Staples | large | unknown | 2026-11-08 |
| XEL | $79.68 | 30,471,601 | Utilities | large | unknown | 2026-11-08 |
| XOM | $165.88 | 84,901,034 | Energy | large | unknown | 2026-11-08 |
| XPO | $176.55 | 20,170,492 | Unknown | mid | unknown | 2026-11-08 |
| XYZ | $85.50 | 27,031,271 | Unknown | large | unknown | 2026-11-08 |
| YUM | $161.21 | 20,953,042 | Consumer Discretionary | large | unknown | 2026-11-08 |
