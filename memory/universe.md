---
screened_on: 2026-10-18
expires_on: 2026-10-25
total_passed: 274
total_rejected: 1258
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
| A | $172.97 | 23,850,223 | Unknown | large | unknown | 2026-10-18 |
| AAL | $11.88 | 29,348,096 | Industrials | mid | unknown | 2026-10-18 |
| AAPL | $343.39 | 387,572,513 | Information Technology | large | unknown | 2026-10-18 |
| ABBV | $285.46 | 53,648,954 | Health Care | large | unknown | 2026-10-18 |
| ABNB | $173.68 | 41,774,341 | Consumer Discretionary | large | unknown | 2026-10-18 |
| ABT | $104.88 | 41,677,569 | Health Care | large | unknown | 2026-10-18 |
| ACN | $229.68 | 76,061,594 | Information Technology | large | unknown | 2026-10-18 |
| ADBE | $245.25 | 39,647,680 | Information Technology | large | unknown | 2026-10-18 |
| ADI | $395.32 | 44,594,661 | Information Technology | large | unknown | 2026-10-18 |
| ADP | $289.01 | 26,059,551 | Industrials | large | unknown | 2026-10-18 |
| ADSK | $239.98 | 29,253,830 | Information Technology | large | unknown | 2026-10-18 |
| AKAM | $87.84 | 29,925,212 | Information Technology | large | unknown | 2026-10-18 |
| ALL | $247.94 | 31,683,102 | Unknown | large | unknown | 2026-10-18 |
| AMAT | $409.25 | 138,359,542 | Information Technology | large | unknown | 2026-10-18 |
| AMD | $528.77 | 341,951,663 | Information Technology | large | unknown | 2026-10-18 |
| AMGN | $432.63 | 48,672,299 | Health Care | large | unknown | 2026-10-18 |
| AMT | $185.21 | 24,094,483 | Real Estate | large | unknown | 2026-10-18 |
| AMZN | $249.92 | 294,052,399 | Consumer Discretionary | large | unknown | 2026-10-18 |
| ANET | $177.02 | 51,871,014 | Information Technology | large | unknown | 2026-10-18 |
| AON | $292.58 | 31,707,384 | Financials | large | unknown | 2026-10-18 |
| APH | $79.37 | 47,654,963 | Information Technology | large | unknown | 2026-10-18 |
| APO | $110.83 | 25,417,799 | Financials | large | unknown | 2026-10-18 |
| APP | $266.24 | 57,795,489 | Unknown | large | unknown | 2026-10-18 |
| AVGO | $328.69 | 246,780,634 | Information Technology | large | unknown | 2026-10-18 |
| AXP | $313.62 | 39,735,454 | Unknown | large | unknown | 2026-10-18 |
| AZO | $3121.19 | 61,428,513 | Consumer Discretionary | large | unknown | 2026-10-18 |
| BA | $190.07 | 62,944,837 | Industrials | large | unknown | 2026-10-18 |
| BAC | $51.23 | 156,462,754 | Financials | large | unknown | 2026-10-18 |
| BE | $221.25 | 100,199,927 | Unknown | large | unknown | 2026-10-18 |
| BKNG | $163.42 | 92,473,438 | Consumer Discretionary | large | unknown | 2026-10-18 |
| BKR | $55.70 | 20,295,768 | Unknown | large | unknown | 2026-10-18 |
| BLK | $1133.32 | 39,732,551 | Unknown | large | unknown | 2026-10-18 |
| BMY | $59.83 | 52,486,181 | Health Care | large | unknown | 2026-10-18 |
| BNY | $143.37 | 27,266,572 | Unknown | large | unknown | 2026-10-18 |
| BRK.B | $532.03 | 73,939,368 | Financials | large | unknown | 2026-10-18 |
| BSX | $44.38 | 55,498,896 | Health Care | large | unknown | 2026-10-18 |
| BURL | $262.58 | 27,956,885 | Unknown | mid | unknown | 2026-10-18 |
| BX | $106.64 | 27,815,414 | Financials | large | unknown | 2026-10-18 |
| C | $124.26 | 55,399,478 | Financials | large | unknown | 2026-10-18 |
| CASY | $689.37 | 22,436,317 | Consumer Staples | large | unknown | 2026-10-18 |
| CAT | $730.84 | 86,271,017 | Industrials | large | unknown | 2026-10-18 |
| CB | $359.77 | 24,013,083 | Financials | large | unknown | 2026-10-18 |
| CBOE | $315.09 | 22,799,344 | Unknown | large | unknown | 2026-10-18 |
| CCL | $25.90 | 40,005,174 | Unknown | large | unknown | 2026-10-18 |
| CDE | $15.46 | 24,735,993 | Unknown | mid | unknown | 2026-10-18 |
| CDNS | $319.61 | 48,394,468 | Unknown | large | unknown | 2026-10-18 |
| CEG | $271.36 | 44,299,372 | Unknown | large | unknown | 2026-10-18 |
| CFG | $63.35 | 20,032,858 | Financials | large | unknown | 2026-10-18 |
| CI | $302.33 | 21,948,465 | Health Care | large | unknown | 2026-10-18 |
| CIEN | $332.98 | 53,253,935 | Unknown | large | unknown | 2026-10-18 |
| CL | $94.10 | 25,637,050 | Consumer Staples | large | unknown | 2026-10-18 |
| CMCSA | $21.91 | 37,591,080 | Unknown | large | unknown | 2026-10-18 |
| CME | $293.97 | 24,566,107 | Financials | large | unknown | 2026-10-18 |
| CMG | $29.87 | 43,903,126 | Consumer Discretionary | large | unknown | 2026-10-18 |
| CMI | $531.16 | 33,381,989 | Industrials | large | unknown | 2026-10-18 |
| CNP | $40.55 | 21,998,398 | Unknown | large | unknown | 2026-10-18 |
| COF | $201.77 | 36,102,435 | Financials | large | unknown | 2026-10-18 |
| COHR | $233.00 | 82,798,417 | Unknown | large | unknown | 2026-10-18 |
| COIN | $173.18 | 44,951,819 | Unknown | large | unknown | 2026-10-18 |
| COP | $146.51 | 34,837,918 | Energy | large | unknown | 2026-10-18 |
| COR | $340.81 | 22,241,633 | Unknown | large | unknown | 2026-10-18 |
| COST | $989.34 | 94,089,647 | Consumer Staples | large | unknown | 2026-10-18 |
| CRH | $83.65 | 22,666,691 | Unknown | large | unknown | 2026-10-18 |
| CRL | $300.23 | 21,507,056 | Health Care | large | unknown | 2026-10-18 |
| CRM | $240.77 | 79,963,677 | Information Technology | large | unknown | 2026-10-18 |
| CRWD | $227.30 | 79,219,203 | Information Technology | large | unknown | 2026-10-18 |
| CSCO | $107.39 | 78,190,543 | Information Technology | large | unknown | 2026-10-18 |
| CSX | $48.70 | 40,396,336 | Industrials | large | unknown | 2026-10-18 |
| CTSH | $66.04 | 21,348,422 | Information Technology | large | unknown | 2026-10-18 |
| CTVA | $12.88 | 20,755,440 | Materials | mid | unknown | 2026-10-18 |
| CVNA | $58.85 | 28,599,456 | Unknown | large | unknown | 2026-10-18 |
| CVS | $92.39 | 48,971,002 | Health Care | large | unknown | 2026-10-18 |
| CVX | $224.99 | 64,555,586 | Energy | large | unknown | 2026-10-18 |
| D | $63.56 | 25,572,091 | Utilities | large | unknown | 2026-10-18 |
| DAL | $75.37 | 30,066,884 | Industrials | large | unknown | 2026-10-18 |
| DASH | $189.12 | 46,117,096 | Unknown | large | unknown | 2026-10-18 |
| DDOG | $247.03 | 44,581,957 | Unknown | large | unknown | 2026-10-18 |
| DE | $641.46 | 46,087,534 | Industrials | large | unknown | 2026-10-18 |
| DELL | $451.44 | 120,199,656 | Information Technology | large | unknown | 2026-10-18 |
| DHI | $139.38 | 23,570,220 | Consumer Discretionary | large | unknown | 2026-10-18 |
| DHR | $229.01 | 59,114,529 | Health Care | large | unknown | 2026-10-18 |
| DIS | $110.59 | 45,224,528 | Communication Services | large | unknown | 2026-10-18 |
| DKS | $144.31 | 24,467,330 | Consumer Discretionary | mid | unknown | 2026-10-18 |
| DT | $61.12 | 25,601,106 | Unknown | mid | unknown | 2026-10-18 |
| DUK | $121.48 | 22,971,917 | Utilities | large | unknown | 2026-10-18 |
| DVN | $50.73 | 36,529,862 | Energy | large | unknown | 2026-10-18 |
| ELV | $428.56 | 28,993,749 | Unknown | large | unknown | 2026-10-18 |
| EMR | $161.41 | 21,567,756 | Industrials | large | unknown | 2026-10-18 |
| EOG | $158.06 | 21,524,129 | Energy | large | unknown | 2026-10-18 |
| EQIX | $986.02 | 32,218,985 | Real Estate | large | unknown | 2026-10-18 |
| EQT | $54.33 | 26,007,952 | Unknown | large | unknown | 2026-10-18 |
| ETN | $391.20 | 50,442,464 | Industrials | large | unknown | 2026-10-18 |
| EW | $86.61 | 20,332,430 | Health Care | large | unknown | 2026-10-18 |
| EXPE | $289.01 | 35,508,139 | Consumer Discretionary | large | unknown | 2026-10-18 |
| F | $12.42 | 21,974,369 | Consumer Discretionary | large | unknown | 2026-10-18 |
| FANG | $204.03 | 29,240,593 | Unknown | large | unknown | 2026-10-18 |
| FAST | $51.02 | 26,875,700 | Industrials | large | unknown | 2026-10-18 |
| FCX | $69.50 | 40,589,702 | Materials | large | unknown | 2026-10-18 |
| FDX | $293.55 | 21,573,895 | Industrials | large | unknown | 2026-10-18 |
| FERG | $231.75 | 20,048,875 | Unknown | large | unknown | 2026-10-18 |
| FICO | $770.96 | 38,157,114 | Information Technology | large | unknown | 2026-10-18 |
| FITB | $50.39 | 33,343,417 | Financials | large | unknown | 2026-10-18 |
| FIX | $1438.35 | 36,154,232 | Unknown | large | unknown | 2026-10-18 |
| FN | $363.42 | 23,429,717 | Unknown | mid | unknown | 2026-10-18 |
| FTNT | $169.10 | 21,793,356 | Information Technology | large | unknown | 2026-10-18 |
| GD | $344.17 | 21,742,080 | Industrials | large | unknown | 2026-10-18 |
| GE | $313.99 | 55,098,688 | Industrials | large | unknown | 2026-10-18 |
| GEN | $24.14 | 20,791,467 | Information Technology | large | unknown | 2026-10-18 |
| GEV | $920.54 | 88,140,840 | Industrials | large | unknown | 2026-10-18 |
| GILD | $156.22 | 35,371,667 | Health Care | large | unknown | 2026-10-18 |
| GIS | $33.12 | 22,292,028 | Consumer Staples | large | unknown | 2026-10-18 |
| GLW | $131.96 | 47,062,305 | Information Technology | large | unknown | 2026-10-18 |
| GM | $83.96 | 41,342,380 | Consumer Discretionary | large | unknown | 2026-10-18 |
| GOOG | $336.95 | 132,552,968 | Communication Services | large | unknown | 2026-10-18 |
| GOOGL | $340.62 | 251,377,929 | Communication Services | large | unknown | 2026-10-18 |
| GS | $880.50 | 82,607,669 | Financials | large | unknown | 2026-10-18 |
| GWW | $1330.52 | 23,652,850 | Industrials | large | unknown | 2026-10-18 |
| HAL | $33.51 | 20,579,563 | Energy | large | unknown | 2026-10-18 |
| HBAN | $15.27 | 24,561,237 | Financials | large | unknown | 2026-10-18 |
| HCA | $458.68 | 27,924,941 | Health Care | large | unknown | 2026-10-18 |
| HD | $309.64 | 84,376,601 | Consumer Discretionary | large | unknown | 2026-10-18 |
| HLT | $345.01 | 35,056,306 | Consumer Discretionary | large | unknown | 2026-10-18 |
| HON | $211.45 | 20,151,029 | Industrials | large | unknown | 2026-10-18 |
| HOOD | $98.89 | 63,049,289 | Unknown | large | unknown | 2026-10-18 |
| HPE | $55.13 | 67,841,588 | Information Technology | large | unknown | 2026-10-18 |
| HPQ | $30.01 | 28,123,602 | Information Technology | large | unknown | 2026-10-18 |
| HUM | $413.06 | 37,711,065 | Health Care | large | unknown | 2026-10-18 |
| HWM | $220.84 | 35,154,780 | Industrials | large | unknown | 2026-10-18 |
| IBM | $232.12 | 39,316,088 | Information Technology | large | unknown | 2026-10-18 |
| ICE | $161.62 | 24,488,956 | Financials | large | unknown | 2026-10-18 |
| ILMN | $262.52 | 49,825,256 | Health Care | large | unknown | 2026-10-18 |
| INTC | $89.77 | 287,464,111 | Information Technology | large | unknown | 2026-10-18 |
| INTU | $325.20 | 49,120,492 | Information Technology | large | unknown | 2026-10-18 |
| IQV | $266.89 | 22,798,128 | Health Care | large | unknown | 2026-10-18 |
| IR | $77.81 | 21,003,504 | Industrials | large | unknown | 2026-10-18 |
| ISRG | $426.91 | 40,922,096 | Health Care | large | unknown | 2026-10-18 |
| JBL | $278.30 | 33,856,115 | Unknown | large | unknown | 2026-10-18 |
| JCI | $145.50 | 25,860,126 | Industrials | large | unknown | 2026-10-18 |
| JNJ | $255.53 | 79,133,715 | Health Care | large | unknown | 2026-10-18 |
| JPM | $339.66 | 101,699,620 | Financials | large | unknown | 2026-10-18 |
| KDP | $34.63 | 25,726,196 | Consumer Staples | large | unknown | 2026-10-18 |
| KEYS | $331.21 | 23,511,224 | Information Technology | large | unknown | 2026-10-18 |
| KKR | $86.05 | 26,999,207 | Unknown | large | unknown | 2026-10-18 |
| KLAC | $165.74 | 66,791,659 | Information Technology | large | unknown | 2026-10-18 |
| KMI | $34.19 | 25,212,302 | Energy | large | unknown | 2026-10-18 |
| KO | $93.86 | 95,446,064 | Consumer Staples | large | unknown | 2026-10-18 |
| KR | $63.62 | 30,433,346 | Consumer Staples | large | unknown | 2026-10-18 |
| KVUE | $18.90 | 25,159,025 | Unknown | large | unknown | 2026-10-18 |
| LEN | $77.10 | 23,091,033 | Consumer Discretionary | large | unknown | 2026-10-18 |
| LHX | $248.43 | 20,105,215 | Industrials | large | unknown | 2026-10-18 |
| LIN | $498.57 | 51,410,166 | Materials | large | unknown | 2026-10-18 |
| LITE | $823.01 | 168,103,527 | Unknown | large | unknown | 2026-10-18 |
| LLY | $1257.32 | 116,800,117 | Health Care | large | unknown | 2026-10-18 |
| LMT | $552.22 | 21,789,184 | Industrials | large | unknown | 2026-10-18 |
| LOW | $197.30 | 25,408,637 | Consumer Discretionary | large | unknown | 2026-10-18 |
| LRCX | $263.91 | 123,178,050 | Information Technology | large | unknown | 2026-10-18 |
| MA | $617.51 | 87,991,082 | Financials | large | unknown | 2026-10-18 |
| MAR | $388.12 | 23,008,992 | Unknown | large | unknown | 2026-10-18 |
| MCD | $242.91 | 52,098,357 | Consumer Discretionary | large | unknown | 2026-10-18 |
| MCHP | $73.84 | 29,836,608 | Information Technology | large | unknown | 2026-10-18 |
| MCK | $1005.29 | 32,504,903 | Health Care | large | unknown | 2026-10-18 |
| MCO | $485.00 | 20,880,431 | Financials | large | unknown | 2026-10-18 |
| MDLZ | $63.92 | 32,169,734 | Consumer Staples | large | unknown | 2026-10-18 |
| MDT | $94.77 | 134,334,693 | Health Care | large | unknown | 2026-10-18 |
| META | $709.42 | 566,297,293 | Communication Services | large | unknown | 2026-10-18 |
| MLM | $500.87 | 25,999,815 | Materials | large | unknown | 2026-10-18 |
| MMM | $164.68 | 20,460,459 | Industrials | large | unknown | 2026-10-18 |
| MNST | $45.74 | 30,699,808 | Consumer Staples | large | unknown | 2026-10-18 |
| MO | $75.10 | 32,545,922 | Consumer Staples | large | unknown | 2026-10-18 |
| MPC | $478.21 | 46,036,164 | Energy | large | unknown | 2026-10-18 |
| MPWR | $1210.45 | 43,992,133 | Information Technology | large | unknown | 2026-10-18 |
| MRK | $145.96 | 55,914,719 | Health Care | large | unknown | 2026-10-18 |
| MRNA | $217.55 | 102,675,706 | Health Care | large | unknown | 2026-10-18 |
| MRSH | $188.60 | 24,450,401 | Unknown | large | unknown | 2026-10-18 |
| MRVL | $227.73 | 133,531,470 | Unknown | large | unknown | 2026-10-18 |
| MS | $180.57 | 58,789,171 | Financials | large | unknown | 2026-10-18 |
| MSFT | $528.99 | 381,947,407 | Information Technology | large | unknown | 2026-10-18 |
| MSI | $463.25 | 20,909,758 | Information Technology | large | unknown | 2026-10-18 |
| MTD | $1621.41 | 20,851,496 | Health Care | large | unknown | 2026-10-18 |
| MTSI | $262.08 | 23,496,598 | Unknown | mid | unknown | 2026-10-18 |
| MTZ | $191.09 | 21,467,444 | Unknown | mid | unknown | 2026-10-18 |
| MU | $878.78 | 645,995,383 | Information Technology | large | unknown | 2026-10-18 |
| NEE | $79.78 | 68,044,575 | Utilities | large | unknown | 2026-10-18 |
| NEM | $118.60 | 27,367,723 | Materials | large | unknown | 2026-10-18 |
| NFLX | $70.55 | 135,711,249 | Communication Services | large | unknown | 2026-10-18 |
| NKE | $37.12 | 74,835,190 | Consumer Discretionary | large | unknown | 2026-10-18 |
| NOC | $519.97 | 29,569,118 | Industrials | large | unknown | 2026-10-18 |
| NOW | $141.98 | 62,821,021 | Information Technology | large | unknown | 2026-10-18 |
| NTAP | $203.79 | 30,912,592 | Information Technology | large | unknown | 2026-10-18 |
| NVDA | $214.12 | 676,688,399 | Information Technology | large | unknown | 2026-10-18 |
| NXPI | $229.52 | 27,287,036 | Unknown | large | unknown | 2026-10-18 |
| O | $56.09 | 28,280,740 | Real Estate | large | unknown | 2026-10-18 |
| OKTA | $187.19 | 39,387,642 | Information Technology | mid | unknown | 2026-10-18 |
| ON | $72.00 | 36,175,571 | Information Technology | large | unknown | 2026-10-18 |
| ORCL | $128.22 | 131,337,724 | Information Technology | large | unknown | 2026-10-18 |
| OXY | $62.39 | 40,906,968 | Energy | large | unknown | 2026-10-18 |
| P | $124.01 | 36,685,223 | Unknown | large | unknown | 2026-10-18 |
| PANW | $341.94 | 81,297,644 | Unknown | large | unknown | 2026-10-18 |
| PCG | $13.08 | 29,678,601 | Utilities | large | unknown | 2026-10-18 |
| PEG | $71.50 | 21,461,099 | Utilities | large | unknown | 2026-10-18 |
| PEP | $131.50 | 52,366,353 | Consumer Staples | large | unknown | 2026-10-18 |
| PFE | $29.57 | 46,363,426 | Health Care | large | unknown | 2026-10-18 |
| PG | $159.34 | 48,142,465 | Consumer Staples | large | unknown | 2026-10-18 |
| PGR | $218.56 | 42,131,962 | Financials | large | unknown | 2026-10-18 |
| PH | $963.66 | 30,733,925 | Industrials | large | unknown | 2026-10-18 |
| PLD | $125.75 | 23,822,886 | Real Estate | large | unknown | 2026-10-18 |
| PLTR | $186.03 | 110,134,151 | Unknown | large | unknown | 2026-10-18 |
| PM | $204.93 | 39,368,157 | Consumer Staples | large | unknown | 2026-10-18 |
| PNC | $217.41 | 21,801,883 | Financials | large | unknown | 2026-10-18 |
| PSX | $293.39 | 53,073,026 | Energy | large | unknown | 2026-10-18 |
| PTC | $192.92 | 45,179,502 | Information Technology | large | unknown | 2026-10-18 |
| PWR | $631.62 | 37,978,608 | Industrials | large | unknown | 2026-10-18 |
| PYPL | $56.70 | 27,531,493 | Financials | large | unknown | 2026-10-18 |
| QCOM | $172.08 | 62,407,530 | Information Technology | large | unknown | 2026-10-18 |
| RCL | $277.57 | 51,131,341 | Consumer Discretionary | large | unknown | 2026-10-18 |
| RDDT | $156.14 | 25,683,485 | Unknown | large | unknown | 2026-10-18 |
| REGN | $791.25 | 29,153,803 | Health Care | large | unknown | 2026-10-18 |
| ROST | $236.92 | 23,280,564 | Consumer Discretionary | large | unknown | 2026-10-18 |
| RTX | $193.95 | 30,671,679 | Industrials | large | unknown | 2026-10-18 |
| SBUX | $97.52 | 39,947,561 | Consumer Discretionary | large | unknown | 2026-10-18 |
| SCHW | $91.95 | 45,644,657 | Financials | large | unknown | 2026-10-18 |
| SHW | $334.99 | 25,118,457 | Materials | large | unknown | 2026-10-18 |
| SLB | $49.51 | 42,575,174 | Energy | large | unknown | 2026-10-18 |
| SMCI | $31.63 | 55,097,002 | Information Technology | large | unknown | 2026-10-18 |
| SMTC | $136.73 | 31,552,342 | Information Technology | mid | unknown | 2026-10-18 |
| SNDK | $1299.04 | 316,512,299 | Unknown | large | unknown | 2026-10-18 |
| SNPS | $454.75 | 59,177,139 | Information Technology | large | unknown | 2026-10-18 |
| SO | $91.17 | 24,405,611 | Utilities | large | unknown | 2026-10-18 |
| SPGI | $429.50 | 35,272,821 | Financials | large | unknown | 2026-10-18 |
| STT | $165.74 | 23,175,252 | Financials | large | unknown | 2026-10-18 |
| STX | $639.19 | 177,257,957 | Information Technology | large | unknown | 2026-10-18 |
| SWKS | $79.68 | 26,323,784 | Information Technology | large | unknown | 2026-10-18 |
| SYK | $294.69 | 42,941,849 | Health Care | large | unknown | 2026-10-18 |
| T | $23.43 | 56,506,418 | Communication Services | large | unknown | 2026-10-18 |
| TDG | $1138.61 | 25,457,662 | Industrials | large | unknown | 2026-10-18 |
| TEL | $212.52 | 21,182,117 | Information Technology | large | unknown | 2026-10-18 |
| TER | $324.91 | 38,823,121 | Information Technology | large | unknown | 2026-10-18 |
| TFC | $47.08 | 29,113,789 | Financials | large | unknown | 2026-10-18 |
| TGT | $154.27 | 29,923,287 | Consumer Discretionary | large | unknown | 2026-10-18 |
| TJX | $147.32 | 61,160,645 | Consumer Discretionary | large | unknown | 2026-10-18 |
| TLN | $354.73 | 26,618,558 | Unknown | mid | unknown | 2026-10-18 |
| TMO | $690.12 | 91,594,008 | Health Care | large | unknown | 2026-10-18 |
| TMUS | $159.07 | 45,548,489 | Communication Services | large | unknown | 2026-10-18 |
| TRGP | $294.78 | 20,018,933 | Unknown | large | unknown | 2026-10-18 |
| TSCO | $33.16 | 24,111,545 | Consumer Discretionary | large | unknown | 2026-10-18 |
| TSLA | $354.65 | 243,526,769 | Consumer Discretionary | large | unknown | 2026-10-18 |
| TT | $458.74 | 43,332,905 | Industrials | large | unknown | 2026-10-18 |
| TTWO | $205.28 | 27,338,662 | Communication Services | large | unknown | 2026-10-18 |
| TWLO | $244.45 | 50,920,696 | Unknown | large | unknown | 2026-10-18 |
| TXN | $276.55 | 57,915,521 | Information Technology | large | unknown | 2026-10-18 |
| UAL | $96.11 | 23,355,626 | Industrials | large | unknown | 2026-10-18 |
| UBER | $70.34 | 49,412,220 | Unknown | large | unknown | 2026-10-18 |
| UNH | $401.45 | 107,740,803 | Health Care | large | unknown | 2026-10-18 |
| UNP | $289.07 | 36,304,274 | Industrials | large | unknown | 2026-10-18 |
| URI | $1030.46 | 36,703,013 | Industrials | large | unknown | 2026-10-18 |
| USB | $58.73 | 36,155,230 | Financials | large | unknown | 2026-10-18 |
| UTHR | $533.35 | 31,592,545 | Health Care | mid | unknown | 2026-10-18 |
| V | $402.66 | 99,504,240 | Financials | large | unknown | 2026-10-18 |
| VEEV | $310.92 | 23,905,340 | Unknown | large | unknown | 2026-10-18 |
| VLO | $444.70 | 64,684,122 | Energy | large | unknown | 2026-10-18 |
| VRT | $206.42 | 58,470,994 | Unknown | large | unknown | 2026-10-18 |
| VRTX | $499.78 | 29,284,183 | Health Care | large | unknown | 2026-10-18 |
| VST | $152.05 | 46,602,348 | Utilities | large | unknown | 2026-10-18 |
| VZ | $44.78 | 65,010,860 | Communication Services | large | unknown | 2026-10-18 |
| WAT | $436.95 | 24,925,895 | Health Care | large | unknown | 2026-10-18 |
| WDC | $331.87 | 151,107,502 | Information Technology | large | unknown | 2026-10-18 |
| WELL | $234.82 | 39,285,860 | Real Estate | large | unknown | 2026-10-18 |
| WFC | $83.88 | 89,448,366 | Financials | large | unknown | 2026-10-18 |
| WM | $227.00 | 22,934,069 | Industrials | large | unknown | 2026-10-18 |
| WMB | $71.28 | 31,198,996 | Energy | large | unknown | 2026-10-18 |
| WMT | $118.80 | 93,448,294 | Consumer Staples | large | unknown | 2026-10-18 |
| XEL | $76.32 | 26,296,659 | Utilities | large | unknown | 2026-10-18 |
| XOM | $179.01 | 64,348,756 | Energy | large | unknown | 2026-10-18 |
| YUM | $150.48 | 21,493,387 | Consumer Discretionary | large | unknown | 2026-10-18 |
