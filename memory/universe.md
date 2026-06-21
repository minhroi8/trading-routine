---
screened_on: 2026-06-21
expires_on: 2026-06-28
total_passed: 294
total_rejected: 1238
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
| AAL | $15.98 | 39,431,431 | Industrials | mid | unknown | 2026-06-21 |
| AAPL | $297.86 | 489,718,966 | Information Technology | large | unknown | 2026-06-21 |
| ABBV | $216.50 | 45,587,667 | Health Care | large | unknown | 2026-06-21 |
| ABNB | $142.37 | 23,967,856 | Consumer Discretionary | large | unknown | 2026-06-21 |
| ABT | $88.42 | 47,850,189 | Health Care | large | unknown | 2026-06-21 |
| ACN | $128.29 | 49,407,031 | Information Technology | large | unknown | 2026-06-21 |
| ADBE | $195.12 | 63,550,460 | Information Technology | large | unknown | 2026-06-21 |
| ADI | $434.10 | 73,277,972 | Information Technology | large | unknown | 2026-06-21 |
| ADP | $218.40 | 23,047,859 | Industrials | large | unknown | 2026-06-21 |
| ADSK | $193.70 | 37,191,865 | Information Technology | large | unknown | 2026-06-21 |
| AEIS | $372.92 | 23,798,595 | Information Technology | mid | unknown | 2026-06-21 |
| AEP | $127.67 | 28,833,133 | Utilities | large | unknown | 2026-06-21 |
| AJG | $214.15 | 22,018,143 | Financials | large | unknown | 2026-06-21 |
| AKAM | $124.94 | 25,810,854 | Information Technology | large | unknown | 2026-06-21 |
| AMAT | $616.83 | 154,194,442 | Information Technology | large | unknown | 2026-06-21 |
| AMD | $537.13 | 336,411,610 | Information Technology | large | unknown | 2026-06-21 |
| AMGN | $337.47 | 31,934,388 | Health Care | large | unknown | 2026-06-21 |
| AMT | $175.95 | 24,973,652 | Real Estate | large | unknown | 2026-06-21 |
| AMZN | $244.61 | 491,403,229 | Consumer Discretionary | large | unknown | 2026-06-21 |
| ANET | $169.64 | 64,171,352 | Information Technology | large | unknown | 2026-06-21 |
| AON | $317.70 | 27,500,909 | Financials | large | unknown | 2026-06-21 |
| APH | $163.94 | 80,778,543 | Information Technology | large | unknown | 2026-06-21 |
| APO | $137.47 | 22,179,162 | Financials | large | unknown | 2026-06-21 |
| APP | $469.45 | 96,559,651 | Unknown | large | unknown | 2026-06-21 |
| ATI | $201.24 | 21,482,579 | Materials | mid | unknown | 2026-06-21 |
| AVGO | $411.07 | 421,383,003 | Information Technology | large | unknown | 2026-06-21 |
| AXON | $423.06 | 25,039,519 | Industrials | large | unknown | 2026-06-21 |
| AXP | $338.15 | 36,873,513 | Unknown | large | unknown | 2026-06-21 |
| AZO | $3063.30 | 62,469,455 | Consumer Discretionary | large | unknown | 2026-06-21 |
| BA | $222.74 | 47,663,959 | Industrials | large | unknown | 2026-06-21 |
| BAC | $56.15 | 133,108,086 | Financials | large | unknown | 2026-06-21 |
| BKNG | $171.77 | 65,091,407 | Consumer Discretionary | large | unknown | 2026-06-21 |
| BKR | $58.41 | 27,709,623 | Unknown | large | unknown | 2026-06-21 |
| BLD | $425.95 | 26,831,554 | Unknown | mid | unknown | 2026-06-21 |
| BLK | $1051.15 | 40,028,732 | Unknown | large | unknown | 2026-06-21 |
| BMY | $54.00 | 40,580,171 | Health Care | large | unknown | 2026-06-21 |
| BNY | $143.63 | 21,638,362 | Unknown | large | unknown | 2026-06-21 |
| BRK.B | $489.31 | 63,687,314 | Financials | large | unknown | 2026-06-21 |
| BSX | $45.28 | 72,640,090 | Health Care | large | unknown | 2026-06-21 |
| BURL | $336.94 | 30,098,894 | Unknown | mid | unknown | 2026-06-21 |
| BX | $123.81 | 26,839,608 | Financials | large | unknown | 2026-06-21 |
| C | $143.08 | 76,698,921 | Financials | large | unknown | 2026-06-21 |
| CAH | $221.83 | 24,376,474 | Unknown | large | unknown | 2026-06-21 |
| CARR | $71.80 | 26,128,255 | Unknown | large | unknown | 2026-06-21 |
| CASY | $842.30 | 41,114,732 | Consumer Staples | large | unknown | 2026-06-21 |
| CAT | $985.23 | 98,027,887 | Industrials | large | unknown | 2026-06-21 |
| CB | $323.49 | 26,422,089 | Financials | large | unknown | 2026-06-21 |
| CBOE | $250.84 | 41,439,408 | Unknown | large | unknown | 2026-06-21 |
| CCL | $30.86 | 42,056,062 | Unknown | large | unknown | 2026-06-21 |
| CDE | $17.48 | 24,560,041 | Unknown | mid | unknown | 2026-06-21 |
| CDNS | $387.29 | 47,097,334 | Unknown | large | unknown | 2026-06-21 |
| CEG | $274.09 | 56,251,783 | Unknown | large | unknown | 2026-06-21 |
| CFG | $67.04 | 24,294,265 | Financials | large | unknown | 2026-06-21 |
| CHTR | $126.19 | 20,781,192 | Unknown | large | unknown | 2026-06-21 |
| CIEN | $428.25 | 80,361,985 | Unknown | large | unknown | 2026-06-21 |
| CL | $89.47 | 27,982,864 | Consumer Staples | large | unknown | 2026-06-21 |
| CMCSA | $22.41 | 57,953,906 | Unknown | large | unknown | 2026-06-21 |
| CME | $246.28 | 54,249,197 | Financials | large | unknown | 2026-06-21 |
| CMG | $32.48 | 45,193,774 | Consumer Discretionary | large | unknown | 2026-06-21 |
| CMI | $716.25 | 41,363,584 | Industrials | large | unknown | 2026-06-21 |
| COF | $201.61 | 48,862,802 | Financials | large | unknown | 2026-06-21 |
| COHR | $389.65 | 97,831,702 | Unknown | large | unknown | 2026-06-21 |
| COIN | $163.31 | 39,180,560 | Unknown | large | unknown | 2026-06-21 |
| COP | $107.73 | 56,332,959 | Energy | large | unknown | 2026-06-21 |
| COR | $271.89 | 24,212,560 | Unknown | large | unknown | 2026-06-21 |
| COST | $951.80 | 72,533,156 | Consumer Staples | large | unknown | 2026-06-21 |
| CPRT | $30.21 | 24,697,568 | Industrials | large | unknown | 2026-06-21 |
| CRH | $111.22 | 24,139,334 | Unknown | large | unknown | 2026-06-21 |
| CRM | $151.78 | 112,507,558 | Information Technology | large | unknown | 2026-06-21 |
| CRS | $586.32 | 27,633,361 | Materials | mid | unknown | 2026-06-21 |
| CRWD | $685.31 | 86,346,638 | Information Technology | large | unknown | 2026-06-21 |
| CSCO | $119.42 | 135,732,902 | Information Technology | large | unknown | 2026-06-21 |
| CSX | $45.61 | 43,785,971 | Industrials | large | unknown | 2026-06-21 |
| CTSH | $43.67 | 34,812,214 | Information Technology | large | unknown | 2026-06-21 |
| CVNA | $66.55 | 37,951,629 | Unknown | large | unknown | 2026-06-21 |
| CVS | $98.38 | 40,922,676 | Health Care | large | unknown | 2026-06-21 |
| CVX | $173.59 | 55,193,490 | Energy | large | unknown | 2026-06-21 |
| D | $68.38 | 43,358,804 | Utilities | large | unknown | 2026-06-21 |
| DAL | $84.18 | 29,208,671 | Industrials | large | unknown | 2026-06-21 |
| DASH | $173.36 | 35,918,332 | Unknown | large | unknown | 2026-06-21 |
| DDOG | $222.86 | 70,019,485 | Unknown | large | unknown | 2026-06-21 |
| DE | $589.29 | 49,830,742 | Industrials | large | unknown | 2026-06-21 |
| DELL | $409.15 | 158,254,666 | Information Technology | large | unknown | 2026-06-21 |
| DG | $113.53 | 24,868,215 | Consumer Staples | large | unknown | 2026-06-21 |
| DHR | $177.19 | 39,845,469 | Health Care | large | unknown | 2026-06-21 |
| DIS | $103.91 | 43,116,305 | Communication Services | large | unknown | 2026-06-21 |
| DKS | $232.97 | 23,168,210 | Consumer Discretionary | mid | unknown | 2026-06-21 |
| DLR | $188.09 | 21,491,575 | Unknown | large | unknown | 2026-06-21 |
| DLTR | $111.65 | 20,224,606 | Consumer Staples | large | unknown | 2026-06-21 |
| DOW | $31.73 | 28,373,595 | Materials | large | unknown | 2026-06-21 |
| DVN | $42.12 | 44,320,228 | Energy | large | unknown | 2026-06-21 |
| DXCM | $72.48 | 21,749,957 | Health Care | large | unknown | 2026-06-21 |
| ECL | $269.12 | 20,789,527 | Materials | large | unknown | 2026-06-21 |
| ELV | $388.60 | 27,856,523 | Unknown | large | unknown | 2026-06-21 |
| EMR | $150.66 | 20,139,515 | Industrials | large | unknown | 2026-06-21 |
| ENTG | $178.78 | 22,307,513 | Unknown | mid | unknown | 2026-06-21 |
| EOG | $129.97 | 23,684,905 | Energy | large | unknown | 2026-06-21 |
| EQIX | $1091.89 | 34,567,674 | Real Estate | large | unknown | 2026-06-21 |
| EQT | $50.75 | 25,170,610 | Unknown | large | unknown | 2026-06-21 |
| ETN | $421.70 | 51,869,348 | Industrials | large | unknown | 2026-06-21 |
| EW | $87.45 | 22,897,773 | Health Care | large | unknown | 2026-06-21 |
| EXC | $45.81 | 22,221,829 | Utilities | large | unknown | 2026-06-21 |
| F | $14.05 | 60,780,795 | Consumer Discretionary | large | unknown | 2026-06-21 |
| FANG | $183.59 | 23,044,836 | Unknown | large | unknown | 2026-06-21 |
| FCX | $68.66 | 60,981,308 | Materials | large | unknown | 2026-06-21 |
| FDX | $326.25 | 32,293,411 | Industrials | large | unknown | 2026-06-21 |
| FICO | $1095.62 | 25,168,487 | Information Technology | large | unknown | 2026-06-21 |
| FITB | $52.72 | 32,783,188 | Financials | large | unknown | 2026-06-21 |
| FIX | $1967.42 | 46,547,144 | Unknown | large | unknown | 2026-06-21 |
| FLEX | $147.53 | 45,745,156 | Unknown | large | unknown | 2026-06-21 |
| FN | $573.90 | 41,880,698 | Unknown | mid | unknown | 2026-06-21 |
| FSLR | $257.64 | 36,541,348 | Unknown | large | unknown | 2026-06-21 |
| FTI | $65.14 | 21,903,750 | Unknown | mid | unknown | 2026-06-21 |
| FTNT | $144.67 | 37,674,916 | Information Technology | large | unknown | 2026-06-21 |
| GE | $357.67 | 68,529,697 | Industrials | large | unknown | 2026-06-21 |
| GEV | $1109.33 | 128,044,968 | Industrials | large | unknown | 2026-06-21 |
| GILD | $123.63 | 43,233,358 | Health Care | large | unknown | 2026-06-21 |
| GIS | $33.42 | 21,386,038 | Consumer Staples | large | unknown | 2026-06-21 |
| GLW | $195.09 | 80,187,610 | Information Technology | large | unknown | 2026-06-21 |
| GM | $79.31 | 34,788,546 | Consumer Discretionary | large | unknown | 2026-06-21 |
| GOOG | $367.18 | 221,634,448 | Communication Services | large | unknown | 2026-06-21 |
| GOOGL | $367.93 | 390,927,740 | Communication Services | large | unknown | 2026-06-21 |
| GS | $1096.99 | 79,549,989 | Financials | large | unknown | 2026-06-21 |
| GWW | $1363.62 | 24,403,627 | Industrials | large | unknown | 2026-06-21 |
| HAL | $34.92 | 28,375,432 | Energy | large | unknown | 2026-06-21 |
| HBAN | $16.88 | 24,307,066 | Financials | large | unknown | 2026-06-21 |
| HCA | $374.92 | 37,207,080 | Health Care | large | unknown | 2026-06-21 |
| HD | $334.24 | 64,482,493 | Consumer Discretionary | large | unknown | 2026-06-21 |
| HLT | $348.70 | 26,838,063 | Consumer Discretionary | large | unknown | 2026-06-21 |
| HON | $229.06 | 46,828,821 | Industrials | large | unknown | 2026-06-21 |
| HOOD | $108.17 | 92,635,253 | Unknown | large | unknown | 2026-06-21 |
| HPE | $47.41 | 123,288,145 | Information Technology | large | unknown | 2026-06-21 |
| HPQ | $23.50 | 44,116,968 | Information Technology | large | unknown | 2026-06-21 |
| HSY | $172.55 | 20,983,514 | Consumer Staples | large | unknown | 2026-06-21 |
| HUBB | $523.64 | 26,252,792 | Industrials | large | unknown | 2026-06-21 |
| HUM | $360.85 | 22,606,557 | Health Care | large | unknown | 2026-06-21 |
| HWM | $277.73 | 30,426,186 | Industrials | large | unknown | 2026-06-21 |
| IBM | $249.01 | 119,345,184 | Information Technology | large | unknown | 2026-06-21 |
| ICE | $133.85 | 34,414,356 | Financials | large | unknown | 2026-06-21 |
| INTC | $133.80 | 450,275,972 | Information Technology | large | unknown | 2026-06-21 |
| INTU | $266.50 | 130,985,888 | Information Technology | large | unknown | 2026-06-21 |
| IQV | $167.84 | 20,683,521 | Health Care | large | unknown | 2026-06-21 |
| ISRG | $406.59 | 44,101,756 | Health Care | large | unknown | 2026-06-21 |
| JBL | $371.80 | 26,232,352 | Unknown | large | unknown | 2026-06-21 |
| JCI | $144.87 | 24,702,123 | Industrials | large | unknown | 2026-06-21 |
| JNJ | $228.34 | 66,457,994 | Health Care | large | unknown | 2026-06-21 |
| JPM | $325.23 | 87,989,188 | Financials | large | unknown | 2026-06-21 |
| KDP | $30.76 | 29,379,288 | Consumer Staples | large | unknown | 2026-06-21 |
| KEYS | $363.31 | 32,375,869 | Information Technology | large | unknown | 2026-06-21 |
| KHC | $22.80 | 20,452,515 | Consumer Staples | large | unknown | 2026-06-21 |
| KKR | $97.01 | 21,109,268 | Unknown | large | unknown | 2026-06-21 |
| KLAC | $259.01 | 125,530,050 | Information Technology | large | unknown | 2026-06-21 |
| KNX | $74.16 | 25,319,045 | Unknown | mid | unknown | 2026-06-21 |
| KO | $79.36 | 82,091,861 | Consumer Staples | large | unknown | 2026-06-21 |
| KR | $56.62 | 25,826,228 | Consumer Staples | large | unknown | 2026-06-21 |
| KVUE | $18.14 | 21,998,125 | Unknown | large | unknown | 2026-06-21 |
| LIN | $512.17 | 48,983,756 | Materials | large | unknown | 2026-06-21 |
| LITE | $850.16 | 177,588,957 | Unknown | large | unknown | 2026-06-21 |
| LLY | $1098.76 | 154,022,249 | Health Care | large | unknown | 2026-06-21 |
| LMT | $511.06 | 25,247,553 | Industrials | large | unknown | 2026-06-21 |
| LOW | $222.31 | 31,033,735 | Consumer Discretionary | large | unknown | 2026-06-21 |
| LRCX | $388.86 | 134,080,087 | Information Technology | large | unknown | 2026-06-21 |
| LSCC | $153.61 | 22,478,466 | Unknown | mid | unknown | 2026-06-21 |
| MA | $489.81 | 106,924,227 | Financials | large | unknown | 2026-06-21 |
| MAR | $396.11 | 31,664,397 | Unknown | large | unknown | 2026-06-21 |
| MCD | $278.75 | 47,921,950 | Consumer Discretionary | large | unknown | 2026-06-21 |
| MCHP | $99.71 | 46,109,481 | Information Technology | large | unknown | 2026-06-21 |
| MCK | $751.42 | 37,467,773 | Health Care | large | unknown | 2026-06-21 |
| MCO | $450.69 | 30,187,158 | Financials | large | unknown | 2026-06-21 |
| MDLZ | $60.10 | 32,342,277 | Consumer Staples | large | unknown | 2026-06-21 |
| MDT | $79.41 | 65,351,741 | Health Care | large | unknown | 2026-06-21 |
| META | $577.29 | 337,287,470 | Communication Services | large | unknown | 2026-06-21 |
| MKSI | $406.02 | 23,233,482 | Information Technology | mid | unknown | 2026-06-21 |
| MLM | $609.13 | 26,505,996 | Materials | large | unknown | 2026-06-21 |
| MMM | $160.65 | 24,379,549 | Industrials | large | unknown | 2026-06-21 |
| MNST | $91.34 | 22,745,380 | Consumer Staples | large | unknown | 2026-06-21 |
| MO | $69.13 | 29,125,282 | Consumer Staples | large | unknown | 2026-06-21 |
| MPC | $242.82 | 33,749,991 | Energy | large | unknown | 2026-06-21 |
| MPWR | $1563.49 | 54,357,609 | Information Technology | large | unknown | 2026-06-21 |
| MRK | $113.89 | 49,845,042 | Health Care | large | unknown | 2026-06-21 |
| MRSH | $162.37 | 22,948,754 | Unknown | large | unknown | 2026-06-21 |
| MRVL | $310.97 | 401,791,216 | Unknown | large | unknown | 2026-06-21 |
| MS | $223.19 | 71,735,915 | Financials | large | unknown | 2026-06-21 |
| MSCI | $581.29 | 26,916,400 | Financials | large | unknown | 2026-06-21 |
| MSFT | $379.08 | 424,295,040 | Information Technology | large | unknown | 2026-06-21 |
| MSI | $395.02 | 23,080,906 | Information Technology | large | unknown | 2026-06-21 |
| MTD | $1145.12 | 20,526,161 | Health Care | large | unknown | 2026-06-21 |
| MTSI | $390.95 | 29,698,729 | Unknown | mid | unknown | 2026-06-21 |
| MTZ | $379.58 | 23,795,446 | Unknown | mid | unknown | 2026-06-21 |
| MU | $1132.59 | 852,622,894 | Information Technology | large | unknown | 2026-06-21 |
| NCLH | $20.43 | 23,438,802 | Unknown | large | unknown | 2026-06-21 |
| NEE | $86.73 | 70,498,784 | Utilities | large | unknown | 2026-06-21 |
| NEM | $103.80 | 38,603,710 | Materials | large | unknown | 2026-06-21 |
| NFLX | $77.33 | 218,047,923 | Communication Services | large | unknown | 2026-06-21 |
| NKE | $45.20 | 46,903,206 | Consumer Discretionary | large | unknown | 2026-06-21 |
| NOC | $521.82 | 25,430,244 | Industrials | large | unknown | 2026-06-21 |
| NOW | $95.16 | 139,898,066 | Information Technology | large | unknown | 2026-06-21 |
| NTAP | $159.64 | 38,598,948 | Information Technology | large | unknown | 2026-06-21 |
| NVDA | $210.38 | 1,087,159,436 | Information Technology | large | unknown | 2026-06-21 |
| NXPI | $313.15 | 47,494,080 | Unknown | large | unknown | 2026-06-21 |
| O | $60.24 | 22,119,806 | Real Estate | large | unknown | 2026-06-21 |
| ODFL | $220.95 | 26,871,315 | Industrials | large | unknown | 2026-06-21 |
| OKTA | $117.86 | 27,532,329 | Information Technology | mid | unknown | 2026-06-21 |
| ON | $121.52 | 66,902,571 | Information Technology | large | unknown | 2026-06-21 |
| ORCL | $184.31 | 154,692,474 | Information Technology | large | unknown | 2026-06-21 |
| ORLY | $86.85 | 28,055,850 | Consumer Discretionary | large | unknown | 2026-06-21 |
| OXY | $51.81 | 39,721,973 | Energy | large | unknown | 2026-06-21 |
| PANW | $287.60 | 90,171,586 | Unknown | large | unknown | 2026-06-21 |
| PEP | $141.94 | 46,213,025 | Consumer Staples | large | unknown | 2026-06-21 |
| PFE | $25.22 | 46,321,607 | Health Care | large | unknown | 2026-06-21 |
| PG | $150.42 | 62,090,348 | Consumer Staples | large | unknown | 2026-06-21 |
| PGR | $204.72 | 30,666,402 | Financials | large | unknown | 2026-06-21 |
| PH | $953.14 | 45,776,010 | Industrials | large | unknown | 2026-06-21 |
| PINS | $20.29 | 27,844,965 | Unknown | mid | unknown | 2026-06-21 |
| PLTR | $128.44 | 145,763,693 | Unknown | large | unknown | 2026-06-21 |
| PM | $178.43 | 29,980,450 | Consumer Staples | large | unknown | 2026-06-21 |
| PNC | $231.96 | 25,750,338 | Financials | large | unknown | 2026-06-21 |
| PPL | $35.38 | 21,444,450 | Utilities | large | unknown | 2026-06-21 |
| PWR | $702.54 | 45,259,749 | Industrials | large | unknown | 2026-06-21 |
| PYPL | $42.48 | 29,265,573 | Financials | large | unknown | 2026-06-21 |
| QCOM | $226.09 | 133,593,814 | Information Technology | large | unknown | 2026-06-21 |
| RCL | $312.75 | 46,028,390 | Consumer Discretionary | large | unknown | 2026-06-21 |
| REGN | $610.05 | 53,253,808 | Health Care | large | unknown | 2026-06-21 |
| RL | $413.04 | 22,659,688 | Consumer Discretionary | large | unknown | 2026-06-21 |
| ROKU | $138.05 | 38,272,133 | Unknown | mid | unknown | 2026-06-21 |
| ROST | $232.84 | 32,654,017 | Consumer Discretionary | large | unknown | 2026-06-21 |
| RSG | $204.95 | 23,566,268 | Industrials | large | unknown | 2026-06-21 |
| RTX | $185.64 | 37,865,538 | Industrials | large | unknown | 2026-06-21 |
| SATS | $109.21 | 68,930,512 | Communication Services | large | unknown | 2026-06-21 |
| SBUX | $100.61 | 38,247,169 | Consumer Discretionary | large | unknown | 2026-06-21 |
| SCHW | $91.70 | 71,048,395 | Financials | large | unknown | 2026-06-21 |
| SHW | $320.99 | 36,058,954 | Materials | large | unknown | 2026-06-21 |
| SITM | $729.60 | 20,067,886 | Unknown | mid | unknown | 2026-06-21 |
| SLB | $48.09 | 53,034,737 | Energy | large | unknown | 2026-06-21 |
| SMCI | $30.66 | 91,505,803 | Information Technology | large | unknown | 2026-06-21 |
| SMTC | $158.24 | 37,367,392 | Information Technology | mid | unknown | 2026-06-21 |
| SNDK | $2185.16 | 394,490,306 | Unknown | large | unknown | 2026-06-21 |
| SNPS | $455.54 | 55,403,896 | Information Technology | large | unknown | 2026-06-21 |
| SO | $93.12 | 25,360,689 | Utilities | large | unknown | 2026-06-21 |
| SPGI | $410.89 | 51,148,773 | Financials | large | unknown | 2026-06-21 |
| STRL | $863.04 | 32,601,212 | Unknown | mid | unknown | 2026-06-21 |
| STX | $1070.19 | 129,084,816 | Information Technology | large | unknown | 2026-06-21 |
| SYK | $308.00 | 49,416,042 | Health Care | large | unknown | 2026-06-21 |
| T | $22.00 | 68,586,561 | Communication Services | large | unknown | 2026-06-21 |
| TDG | $1329.57 | 36,020,848 | Industrials | large | unknown | 2026-06-21 |
| TEL | $217.72 | 35,627,927 | Information Technology | large | unknown | 2026-06-21 |
| TER | $437.80 | 54,171,936 | Information Technology | large | unknown | 2026-06-21 |
| TFC | $48.31 | 36,348,754 | Financials | large | unknown | 2026-06-21 |
| TGT | $130.74 | 30,361,368 | Consumer Discretionary | large | unknown | 2026-06-21 |
| TJX | $163.91 | 43,015,837 | Consumer Discretionary | large | unknown | 2026-06-21 |
| TLN | $436.07 | 22,055,418 | Unknown | mid | unknown | 2026-06-21 |
| TMO | $464.76 | 62,231,995 | Health Care | large | unknown | 2026-06-21 |
| TMUS | $181.56 | 35,056,675 | Communication Services | large | unknown | 2026-06-21 |
| TSCO | $30.25 | 28,876,879 | Consumer Discretionary | large | unknown | 2026-06-21 |
| TSLA | $400.49 | 338,278,868 | Consumer Discretionary | large | unknown | 2026-06-21 |
| TT | $483.15 | 31,842,393 | Industrials | large | unknown | 2026-06-21 |
| TTD | $18.50 | 20,063,373 | Unknown | large | unknown | 2026-06-21 |
| TTMI | $216.28 | 24,831,905 | Information Technology | mid | unknown | 2026-06-21 |
| TTWO | $239.39 | 29,920,462 | Communication Services | large | unknown | 2026-06-21 |
| TWLO | $186.22 | 28,623,825 | Unknown | mid | unknown | 2026-06-21 |
| TXN | $322.58 | 113,493,135 | Information Technology | large | unknown | 2026-06-21 |
| UAL | $118.29 | 29,596,449 | Industrials | large | unknown | 2026-06-21 |
| UBER | $71.66 | 94,618,613 | Unknown | large | unknown | 2026-06-21 |
| ULTA | $455.56 | 24,513,415 | Consumer Discretionary | large | unknown | 2026-06-21 |
| UNH | $401.13 | 94,590,897 | Health Care | large | unknown | 2026-06-21 |
| UNP | $256.98 | 39,253,773 | Industrials | large | unknown | 2026-06-21 |
| UPS | $105.06 | 25,803,145 | Industrials | large | unknown | 2026-06-21 |
| URI | $1075.96 | 32,320,190 | Industrials | large | unknown | 2026-06-21 |
| USB | $58.09 | 35,276,826 | Financials | large | unknown | 2026-06-21 |
| V | $327.25 | 118,678,438 | Financials | large | unknown | 2026-06-21 |
| VEEV | $153.30 | 26,270,997 | Unknown | large | unknown | 2026-06-21 |
| VLO | $236.46 | 32,327,135 | Energy | large | unknown | 2026-06-21 |
| VMC | $302.81 | 24,483,477 | Materials | large | unknown | 2026-06-21 |
| VRSK | $173.82 | 23,205,598 | Industrials | large | unknown | 2026-06-21 |
| VRT | $333.19 | 77,345,499 | Unknown | large | unknown | 2026-06-21 |
| VRTX | $451.76 | 23,308,258 | Health Care | large | unknown | 2026-06-21 |
| VSH | $64.91 | 27,583,125 | Information Technology | small | unknown | 2026-06-21 |
| VST | $163.71 | 29,274,939 | Utilities | large | unknown | 2026-06-21 |
| VZ | $45.38 | 62,154,713 | Communication Services | large | unknown | 2026-06-21 |
| WAT | $355.52 | 26,346,518 | Health Care | large | unknown | 2026-06-21 |
| WBD | $26.16 | 48,710,385 | Communication Services | large | unknown | 2026-06-21 |
| WDAY | $116.92 | 39,584,904 | Unknown | large | unknown | 2026-06-21 |
| WDC | $746.38 | 146,621,914 | Information Technology | large | unknown | 2026-06-21 |
| WELL | $206.70 | 35,502,772 | Real Estate | large | unknown | 2026-06-21 |
| WFC | $82.23 | 99,115,148 | Financials | large | unknown | 2026-06-21 |
| WM | $214.53 | 21,360,792 | Industrials | large | unknown | 2026-06-21 |
| WMB | $73.14 | 25,561,694 | Energy | large | unknown | 2026-06-21 |
| WMT | $117.19 | 134,314,730 | Consumer Staples | large | unknown | 2026-06-21 |
| WWD | $430.13 | 21,542,650 | Industrials | mid | unknown | 2026-06-21 |
| XEL | $77.38 | 31,211,232 | Utilities | large | unknown | 2026-06-21 |
| XOM | $137.81 | 85,552,708 | Energy | large | unknown | 2026-06-21 |
| XPO | $199.47 | 22,512,832 | Unknown | mid | unknown | 2026-06-21 |
| XYZ | $74.77 | 20,086,289 | Unknown | large | unknown | 2026-06-21 |
| ZTS | $78.71 | 27,127,742 | Health Care | large | unknown | 2026-06-21 |
