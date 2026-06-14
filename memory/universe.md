---
screened_on: 2026-06-14
expires_on: 2026-06-21
total_passed: 286
total_rejected: 1220
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
| AAL | $14.96 | 33,988,985 | Industrials | mid | unknown | 2026-06-14 |
| AAPL | $291.08 | 486,012,780 | Information Technology | large | unknown | 2026-06-14 |
| ABBV | $227.67 | 48,762,305 | Health Care | large | unknown | 2026-06-14 |
| ABNB | $132.28 | 24,115,268 | Consumer Discretionary | large | unknown | 2026-06-14 |
| ABT | $88.09 | 47,013,968 | Health Care | large | unknown | 2026-06-14 |
| ACN | $170.22 | 40,309,155 | Information Technology | large | unknown | 2026-06-14 |
| ADBE | $204.02 | 59,295,691 | Information Technology | large | unknown | 2026-06-14 |
| ADI | $417.70 | 80,498,353 | Information Technology | large | unknown | 2026-06-14 |
| ADP | $226.29 | 25,080,439 | Industrials | large | unknown | 2026-06-14 |
| ADSK | $198.44 | 33,560,767 | Information Technology | large | unknown | 2026-06-14 |
| AEIS | $354.51 | 24,607,098 | Information Technology | mid | unknown | 2026-06-14 |
| AEP | $129.25 | 32,932,665 | Utilities | large | unknown | 2026-06-14 |
| AJG | $218.77 | 22,033,923 | Financials | large | unknown | 2026-06-14 |
| AKAM | $133.50 | 32,353,000 | Information Technology | large | unknown | 2026-06-14 |
| AMAT | $567.15 | 135,900,061 | Information Technology | large | unknown | 2026-06-14 |
| AMD | $511.74 | 327,387,033 | Information Technology | large | unknown | 2026-06-14 |
| AMGN | $355.31 | 30,554,788 | Health Care | large | unknown | 2026-06-14 |
| AMT | $187.11 | 26,477,022 | Real Estate | large | unknown | 2026-06-14 |
| AMZN | $238.56 | 489,426,968 | Consumer Discretionary | large | unknown | 2026-06-14 |
| ANET | $163.25 | 63,994,226 | Information Technology | large | unknown | 2026-06-14 |
| AON | $335.25 | 29,036,677 | Financials | large | unknown | 2026-06-14 |
| APH | $153.90 | 76,463,628 | Information Technology | large | unknown | 2026-06-14 |
| APO | $133.89 | 23,437,238 | Financials | large | unknown | 2026-06-14 |
| APP | $496.74 | 107,956,780 | Information Technology | large | unknown | 2026-06-14 |
| AVGO | $381.95 | 397,320,181 | Information Technology | large | unknown | 2026-06-14 |
| AXON | $441.84 | 25,757,175 | Industrials | large | unknown | 2026-06-14 |
| AXP | $325.44 | 38,155,979 | Financials | large | unknown | 2026-06-14 |
| AZO | $3115.02 | 59,806,201 | Consumer Discretionary | large | unknown | 2026-06-14 |
| BA | $219.12 | 47,880,069 | Industrials | large | unknown | 2026-06-14 |
| BAC | $55.99 | 133,075,175 | Financials | large | unknown | 2026-06-14 |
| BKNG | $164.94 | 60,892,888 | Consumer Discretionary | large | unknown | 2026-06-14 |
| BKR | $63.14 | 27,738,597 | Energy | large | unknown | 2026-06-14 |
| BLD | $411.77 | 27,301,086 | Consumer Discretionary | mid | unknown | 2026-06-14 |
| BLK | $1032.34 | 40,001,771 | Financials | large | unknown | 2026-06-14 |
| BMY | $57.12 | 40,511,814 | Health Care | large | unknown | 2026-06-14 |
| BNY | $143.97 | 22,188,109 | Financials | large | unknown | 2026-06-14 |
| BRK.B | $489.14 | 64,961,897 | Financials | large | unknown | 2026-06-14 |
| BSX | $46.89 | 76,586,507 | Health Care | large | unknown | 2026-06-14 |
| BURL | $338.12 | 31,992,073 | Consumer Discretionary | mid | unknown | 2026-06-14 |
| BX | $122.79 | 24,877,291 | Financials | large | unknown | 2026-06-14 |
| C | $139.78 | 66,053,360 | Financials | large | unknown | 2026-06-14 |
| CAH | $223.84 | 24,668,239 | Health Care | large | unknown | 2026-06-14 |
| CARR | $69.90 | 26,233,286 | Industrials | large | unknown | 2026-06-14 |
| CASY | $894.94 | 41,279,732 | Consumer Staples | large | unknown | 2026-06-14 |
| CAT | $910.76 | 101,805,137 | Industrials | large | unknown | 2026-06-14 |
| CB | $328.27 | 26,269,467 | Financials | large | unknown | 2026-06-14 |
| CBOE | $294.76 | 34,009,586 | Financials | large | unknown | 2026-06-14 |
| CCL | $29.16 | 38,810,744 | Consumer Discretionary | large | unknown | 2026-06-14 |
| CDNS | $384.83 | 44,855,035 | Information Technology | large | unknown | 2026-06-14 |
| CEG | $253.72 | 54,713,418 | Utilities | large | unknown | 2026-06-14 |
| CFG | $67.65 | 22,861,559 | Financials | large | unknown | 2026-06-14 |
| CHTR | $145.78 | 20,134,083 | Communication Services | large | unknown | 2026-06-14 |
| CIEN | $445.70 | 81,592,833 | Information Technology | large | unknown | 2026-06-14 |
| CL | $89.46 | 27,765,394 | Consumer Staples | large | unknown | 2026-06-14 |
| CMCSA | $24.50 | 57,723,310 | Communication Services | large | unknown | 2026-06-14 |
| CME | $269.49 | 44,906,064 | Financials | large | unknown | 2026-06-14 |
| CMG | $32.23 | 43,824,019 | Consumer Discretionary | large | unknown | 2026-06-14 |
| CMI | $659.68 | 35,503,502 | Industrials | large | unknown | 2026-06-14 |
| COF | $184.70 | 48,298,930 | Financials | large | unknown | 2026-06-14 |
| COHR | $385.21 | 96,142,051 | Information Technology | large | unknown | 2026-06-14 |
| COIN | $159.72 | 39,511,188 | Financials | large | unknown | 2026-06-14 |
| COP | $116.97 | 52,590,107 | Energy | large | unknown | 2026-06-14 |
| COR | $281.53 | 26,026,184 | Health Care | large | unknown | 2026-06-14 |
| COST | $982.32 | 79,994,497 | Consumer Staples | large | unknown | 2026-06-14 |
| CPRT | $30.74 | 25,278,595 | Industrials | large | unknown | 2026-06-14 |
| CRH | $106.44 | 23,364,679 | Materials | large | unknown | 2026-06-14 |
| CRM | $166.02 | 112,199,568 | Information Technology | large | unknown | 2026-06-14 |
| CRS | $561.56 | 23,913,092 | Industrials | mid | unknown | 2026-06-14 |
| CRWD | $682.92 | 96,204,418 | Information Technology | large | unknown | 2026-06-14 |
| CSCO | $121.06 | 144,932,447 | Information Technology | large | unknown | 2026-06-14 |
| CSX | $47.58 | 41,106,588 | Industrials | large | unknown | 2026-06-14 |
| CTSH | $52.18 | 29,462,927 | Information Technology | large | unknown | 2026-06-14 |
| CVNA | $64.07 | 34,047,017 | Consumer Discretionary | large | unknown | 2026-06-14 |
| CVS | $101.95 | 43,221,019 | Health Care | large | unknown | 2026-06-14 |
| CVX | $187.20 | 55,373,992 | Energy | large | unknown | 2026-06-14 |
| D | $67.89 | 45,217,758 | Utilities | large | unknown | 2026-06-14 |
| DAL | $83.06 | 27,787,906 | Industrials | large | unknown | 2026-06-14 |
| DASH | $150.62 | 37,013,803 | Consumer Discretionary | large | unknown | 2026-06-14 |
| DDOG | $229.92 | 70,381,213 | Information Technology | large | unknown | 2026-06-14 |
| DE | $577.34 | 51,463,027 | Industrials | large | unknown | 2026-06-14 |
| DELL | $395.91 | 140,564,556 | Information Technology | large | unknown | 2026-06-14 |
| DG | $114.81 | 24,280,448 | Consumer Staples | large | unknown | 2026-06-14 |
| DHR | $180.09 | 44,477,778 | Health Care | large | unknown | 2026-06-14 |
| DIS | $100.01 | 40,030,096 | Communication Services | large | unknown | 2026-06-14 |
| DKS | $220.65 | 22,717,340 | Consumer Discretionary | mid | unknown | 2026-06-14 |
| DLTR | $114.00 | 21,082,941 | Consumer Staples | large | unknown | 2026-06-14 |
| DOCN | $170.15 | 20,359,459 | Information Technology | mid | unknown | 2026-06-14 |
| DOW | $33.84 | 27,998,587 | Materials | large | unknown | 2026-06-14 |
| DVN | $45.29 | 43,266,467 | Energy | large | unknown | 2026-06-14 |
| DXCM | $75.36 | 26,919,021 | Health Care | large | unknown | 2026-06-14 |
| EBAY | $108.59 | 22,439,458 | Consumer Discretionary | large | unknown | 2026-06-14 |
| ECL | $265.38 | 20,371,353 | Materials | large | unknown | 2026-06-14 |
| ELV | $403.85 | 29,613,181 | Health Care | large | unknown | 2026-06-14 |
| ENPH | $54.60 | 21,295,756 | Information Technology | small | unknown | 2026-06-14 |
| EOG | $136.65 | 22,603,953 | Energy | large | unknown | 2026-06-14 |
| EQIX | $1055.45 | 31,308,755 | Real Estate | large | unknown | 2026-06-14 |
| EQT | $51.94 | 24,107,009 | Energy | large | unknown | 2026-06-14 |
| ETN | $391.66 | 55,087,829 | Industrials | large | unknown | 2026-06-14 |
| EW | $85.13 | 22,732,452 | Health Care | large | unknown | 2026-06-14 |
| F | $14.82 | 65,827,798 | Consumer Discretionary | large | unknown | 2026-06-14 |
| FANG | $192.13 | 20,548,247 | Energy | large | unknown | 2026-06-14 |
| FCX | $68.40 | 61,500,830 | Materials | large | unknown | 2026-06-14 |
| FDX | $338.23 | 32,203,138 | Industrials | large | unknown | 2026-06-14 |
| FICO | $1178.65 | 26,831,201 | Information Technology | large | unknown | 2026-06-14 |
| FITB | $54.73 | 31,227,829 | Financials | large | unknown | 2026-06-14 |
| FIVE | $198.47 | 20,811,483 | Consumer Discretionary | mid | unknown | 2026-06-14 |
| FIX | $1878.39 | 47,853,723 | Industrials | large | unknown | 2026-06-14 |
| FLEX | $149.66 | 45,995,154 | Information Technology | mid | unknown | 2026-06-14 |
| FN | $610.95 | 45,924,532 | Information Technology | mid | unknown | 2026-06-14 |
| FSLR | $267.18 | 36,710,672 | Information Technology | large | unknown | 2026-06-14 |
| FTI | $70.77 | 22,189,659 | Energy | mid | unknown | 2026-06-14 |
| FTNT | $146.26 | 37,738,180 | Information Technology | large | unknown | 2026-06-14 |
| GE | $335.29 | 66,998,958 | Industrials | large | unknown | 2026-06-14 |
| GEV | $940.01 | 117,999,532 | Industrials | large | unknown | 2026-06-14 |
| GILD | $125.60 | 40,250,065 | Health Care | large | unknown | 2026-06-14 |
| GIS | $34.50 | 20,669,711 | Consumer Staples | large | unknown | 2026-06-14 |
| GLW | $179.34 | 84,051,504 | Information Technology | large | unknown | 2026-06-14 |
| GM | $81.48 | 32,760,131 | Consumer Discretionary | large | unknown | 2026-06-14 |
| GOOG | $358.09 | 217,622,580 | Communication Services | large | unknown | 2026-06-14 |
| GOOGL | $359.65 | 392,768,018 | Communication Services | large | unknown | 2026-06-14 |
| GS | $1062.71 | 78,422,839 | Financials | large | unknown | 2026-06-14 |
| GWW | $1315.81 | 21,421,704 | Industrials | large | unknown | 2026-06-14 |
| HAL | $39.59 | 28,184,047 | Energy | large | unknown | 2026-06-14 |
| HBAN | $17.52 | 22,262,879 | Financials | large | unknown | 2026-06-14 |
| HCA | $386.75 | 38,540,413 | Health Care | large | unknown | 2026-06-14 |
| HD | $328.38 | 65,395,620 | Consumer Discretionary | large | unknown | 2026-06-14 |
| HLT | $345.92 | 24,783,759 | Consumer Discretionary | large | unknown | 2026-06-14 |
| HON | $220.32 | 44,576,188 | Industrials | large | unknown | 2026-06-14 |
| HOOD | $93.18 | 75,495,333 | Financials | large | unknown | 2026-06-14 |
| HPE | $48.17 | 110,978,448 | Information Technology | large | unknown | 2026-06-14 |
| HPQ | $25.24 | 41,817,912 | Information Technology | large | unknown | 2026-06-14 |
| HUBB | $476.41 | 26,072,390 | Industrials | large | unknown | 2026-06-14 |
| HUM | $379.28 | 23,425,111 | Health Care | large | unknown | 2026-06-14 |
| HWM | $264.62 | 27,272,448 | Industrials | large | unknown | 2026-06-14 |
| IBM | $272.19 | 113,398,925 | Information Technology | large | unknown | 2026-06-14 |
| ICE | $140.50 | 32,956,356 | Financials | large | unknown | 2026-06-14 |
| INTC | $124.55 | 430,322,179 | Information Technology | large | unknown | 2026-06-14 |
| INTU | $276.69 | 128,379,117 | Information Technology | large | unknown | 2026-06-14 |
| ISRG | $411.00 | 42,437,619 | Health Care | large | unknown | 2026-06-14 |
| JBL | $384.87 | 22,585,960 | Information Technology | large | unknown | 2026-06-14 |
| JCI | $144.94 | 24,105,086 | Industrials | large | unknown | 2026-06-14 |
| JNJ | $240.84 | 63,130,262 | Health Care | large | unknown | 2026-06-14 |
| JPM | $320.71 | 76,145,908 | Financials | large | unknown | 2026-06-14 |
| KDP | $31.72 | 28,656,288 | Consumer Staples | large | unknown | 2026-06-14 |
| KEYS | $350.55 | 40,017,260 | Information Technology | large | unknown | 2026-06-14 |
| KKR | $96.23 | 24,840,609 | Financials | large | unknown | 2026-06-14 |
| KLAC | $254.65 | 115,841,407 | Information Technology | large | unknown | 2026-06-14 |
| KNX | $81.50 | 23,803,777 | Industrials | mid | unknown | 2026-06-14 |
| KO | $82.61 | 74,067,380 | Consumer Staples | large | unknown | 2026-06-14 |
| KR | $64.72 | 22,527,569 | Consumer Staples | large | unknown | 2026-06-14 |
| KVUE | $18.13 | 22,823,840 | Consumer Staples | large | unknown | 2026-06-14 |
| LIN | $523.53 | 45,325,431 | Materials | large | unknown | 2026-06-14 |
| LITE | $921.10 | 183,649,077 | Information Technology | large | unknown | 2026-06-14 |
| LLY | $1132.99 | 149,982,184 | Health Care | large | unknown | 2026-06-14 |
| LMT | $540.25 | 23,841,779 | Industrials | large | unknown | 2026-06-14 |
| LOW | $220.79 | 33,783,584 | Consumer Discretionary | large | unknown | 2026-06-14 |
| LRCX | $366.75 | 115,864,092 | Information Technology | large | unknown | 2026-06-14 |
| LSCC | $144.59 | 24,292,445 | Information Technology | mid | unknown | 2026-06-14 |
| MA | $489.94 | 113,445,663 | Financials | large | unknown | 2026-06-14 |
| MAR | $402.46 | 29,272,272 | Consumer Discretionary | large | unknown | 2026-06-14 |
| MCD | $284.80 | 44,159,863 | Consumer Discretionary | large | unknown | 2026-06-14 |
| MCHP | $95.22 | 44,711,634 | Information Technology | large | unknown | 2026-06-14 |
| MCK | $783.58 | 40,668,652 | Health Care | large | unknown | 2026-06-14 |
| MCO | $447.88 | 29,792,594 | Financials | large | unknown | 2026-06-14 |
| MDLZ | $62.99 | 28,887,477 | Consumer Staples | large | unknown | 2026-06-14 |
| MDT | $80.17 | 67,218,494 | Health Care | large | unknown | 2026-06-14 |
| META | $566.92 | 313,523,095 | Communication Services | large | unknown | 2026-06-14 |
| MKSI | $355.58 | 22,038,255 | Information Technology | mid | unknown | 2026-06-14 |
| MLM | $576.06 | 27,697,326 | Materials | large | unknown | 2026-06-14 |
| MMM | $158.34 | 25,060,057 | Industrials | large | unknown | 2026-06-14 |
| MNST | $92.83 | 23,919,265 | Consumer Staples | large | unknown | 2026-06-14 |
| MO | $71.92 | 30,350,821 | Consumer Staples | large | unknown | 2026-06-14 |
| MPC | $263.52 | 29,110,183 | Energy | large | unknown | 2026-06-14 |
| MPWR | $1576.88 | 51,500,623 | Information Technology | large | unknown | 2026-06-14 |
| MRK | $119.03 | 45,746,809 | Health Care | large | unknown | 2026-06-14 |
| MRSH | $168.66 | 24,420,644 | Financials | large | unknown | 2026-06-14 |
| MS | $214.07 | 67,532,140 | Financials | large | unknown | 2026-06-14 |
| MSCI | $599.05 | 26,946,435 | Financials | large | unknown | 2026-06-14 |
| MSFT | $390.67 | 415,065,017 | Information Technology | large | unknown | 2026-06-14 |
| MSI | $412.08 | 24,906,157 | Information Technology | large | unknown | 2026-06-14 |
| MTD | $1130.88 | 23,138,075 | Health Care | large | unknown | 2026-06-14 |
| MTSI | $380.07 | 31,131,246 | Information Technology | mid | unknown | 2026-06-14 |
| MTZ | $363.01 | 24,484,606 | Industrials | mid | unknown | 2026-06-14 |
| MU | $981.27 | 791,180,323 | Information Technology | large | unknown | 2026-06-14 |
| NCLH | $19.44 | 22,502,900 | Consumer Discretionary | large | unknown | 2026-06-14 |
| NEE | $85.94 | 80,398,116 | Utilities | large | unknown | 2026-06-14 |
| NEM | $100.21 | 33,523,923 | Materials | large | unknown | 2026-06-14 |
| NFLX | $80.33 | 191,734,586 | Communication Services | large | unknown | 2026-06-14 |
| NKE | $44.89 | 48,291,941 | Consumer Discretionary | large | unknown | 2026-06-14 |
| NOC | $549.60 | 26,381,226 | Industrials | large | unknown | 2026-06-14 |
| NOW | $102.21 | 143,112,966 | Information Technology | large | unknown | 2026-06-14 |
| NRG | $125.45 | 20,938,729 | Utilities | large | unknown | 2026-06-14 |
| NTAP | $161.61 | 36,611,643 | Information Technology | large | unknown | 2026-06-14 |
| NVDA | $205.17 | 1,102,619,277 | Information Technology | large | unknown | 2026-06-14 |
| NXPI | $304.82 | 47,535,604 | Information Technology | large | unknown | 2026-06-14 |
| NXT | $121.89 | 20,013,581 | Industrials | mid | unknown | 2026-06-14 |
| O | $62.71 | 21,389,437 | Real Estate | large | unknown | 2026-06-14 |
| ODFL | $245.53 | 24,334,057 | Industrials | large | unknown | 2026-06-14 |
| OKTA | $116.31 | 26,782,537 | Information Technology | mid | unknown | 2026-06-14 |
| ON | $116.80 | 64,974,925 | Information Technology | large | unknown | 2026-06-14 |
| ONTO | $323.64 | 20,997,672 | Information Technology | mid | unknown | 2026-06-14 |
| ORCL | $184.16 | 151,180,128 | Information Technology | large | unknown | 2026-06-14 |
| ORLY | $91.01 | 26,296,888 | Consumer Discretionary | large | unknown | 2026-06-14 |
| OXY | $56.53 | 39,567,976 | Energy | large | unknown | 2026-06-14 |
| PANW | $279.59 | 101,896,391 | Information Technology | large | unknown | 2026-06-14 |
| PEP | $144.32 | 42,865,522 | Consumer Staples | large | unknown | 2026-06-14 |
| PFE | $26.21 | 44,252,481 | Health Care | large | unknown | 2026-06-14 |
| PG | $149.58 | 56,688,782 | Consumer Staples | large | unknown | 2026-06-14 |
| PGR | $203.07 | 29,778,106 | Financials | large | unknown | 2026-06-14 |
| PH | $903.41 | 45,740,874 | Industrials | large | unknown | 2026-06-14 |
| PINS | $20.19 | 27,473,770 | Communication Services | mid | unknown | 2026-06-14 |
| PLTR | $127.98 | 148,720,737 | Information Technology | large | unknown | 2026-06-14 |
| PM | $184.34 | 29,564,799 | Consumer Staples | large | unknown | 2026-06-14 |
| PNC | $237.71 | 20,535,572 | Financials | large | unknown | 2026-06-14 |
| PPL | $35.83 | 20,876,416 | Utilities | large | unknown | 2026-06-14 |
| PWR | $708.12 | 50,940,505 | Industrials | large | unknown | 2026-06-14 |
| PYPL | $41.52 | 26,857,287 | Financials | large | unknown | 2026-06-14 |
| QCOM | $211.54 | 135,964,752 | Information Technology | large | unknown | 2026-06-14 |
| RCL | $294.35 | 43,192,267 | Consumer Discretionary | large | unknown | 2026-06-14 |
| REGN | $611.96 | 59,315,514 | Health Care | large | unknown | 2026-06-14 |
| RL | $403.95 | 23,546,728 | Consumer Discretionary | large | unknown | 2026-06-14 |
| ROST | $240.11 | 35,424,363 | Consumer Discretionary | large | unknown | 2026-06-14 |
| RSG | $209.90 | 25,435,578 | Industrials | large | unknown | 2026-06-14 |
| RTX | $183.56 | 36,270,749 | Industrials | large | unknown | 2026-06-14 |
| SATS | $114.23 | 57,072,406 | Communication Services | large | unknown | 2026-06-14 |
| SBUX | $103.06 | 37,889,701 | Consumer Discretionary | large | unknown | 2026-06-14 |
| SCHW | $91.11 | 68,404,690 | Financials | large | unknown | 2026-06-14 |
| SHW | $317.35 | 34,025,063 | Materials | large | unknown | 2026-06-14 |
| SITM | $729.80 | 23,772,397 | Information Technology | mid | unknown | 2026-06-14 |
| SLB | $56.17 | 45,249,624 | Energy | large | unknown | 2026-06-14 |
| SMCI | $30.45 | 85,640,006 | Information Technology | large | unknown | 2026-06-14 |
| SMTC | $166.73 | 36,962,944 | Information Technology | small | unknown | 2026-06-14 |
| SNDK | $1981.01 | 361,344,146 | Information Technology | large | unknown | 2026-06-14 |
| SNPS | $453.66 | 51,261,196 | Information Technology | large | unknown | 2026-06-14 |
| SO | $94.02 | 25,395,757 | Utilities | large | unknown | 2026-06-14 |
| SPGI | $418.94 | 50,611,973 | Financials | large | unknown | 2026-06-14 |
| STRL | $859.24 | 33,815,484 | Industrials | mid | unknown | 2026-06-14 |
| STX | $930.75 | 104,991,415 | Information Technology | large | unknown | 2026-06-14 |
| SYK | $312.10 | 56,076,204 | Health Care | large | unknown | 2026-06-14 |
| T | $23.57 | 62,138,187 | Communication Services | large | unknown | 2026-06-14 |
| TDG | $1256.44 | 34,156,664 | Industrials | large | unknown | 2026-06-14 |
| TEL | $210.31 | 35,666,778 | Information Technology | large | unknown | 2026-06-14 |
| TER | $403.30 | 50,642,774 | Information Technology | large | unknown | 2026-06-14 |
| TFC | $51.66 | 27,461,302 | Financials | large | unknown | 2026-06-14 |
| TGT | $135.21 | 32,578,437 | Consumer Staples | large | unknown | 2026-06-14 |
| TJX | $168.41 | 46,860,000 | Consumer Discretionary | large | unknown | 2026-06-14 |
| TMO | $469.39 | 70,580,463 | Health Care | large | unknown | 2026-06-14 |
| TMUS | $189.12 | 34,953,882 | Communication Services | large | unknown | 2026-06-14 |
| TSCO | $31.25 | 28,504,046 | Consumer Discretionary | large | unknown | 2026-06-14 |
| TSLA | $406.54 | 338,582,038 | Consumer Discretionary | large | unknown | 2026-06-14 |
| TT | $458.20 | 34,524,625 | Industrials | large | unknown | 2026-06-14 |
| TTD | $19.26 | 20,351,454 | Communication Services | large | unknown | 2026-06-14 |
| TTMI | $193.91 | 24,758,200 | Information Technology | mid | unknown | 2026-06-14 |
| TTWO | $211.73 | 27,785,307 | Communication Services | large | unknown | 2026-06-14 |
| TWLO | $204.23 | 30,116,781 | Information Technology | mid | unknown | 2026-06-14 |
| TXN | $301.03 | 108,354,606 | Information Technology | large | unknown | 2026-06-14 |
| UAL | $115.52 | 27,867,070 | Industrials | large | unknown | 2026-06-14 |
| UBER | $68.77 | 89,515,357 | Industrials | large | unknown | 2026-06-14 |
| ULTA | $467.60 | 25,417,193 | Consumer Discretionary | large | unknown | 2026-06-14 |
| UNH | $408.49 | 95,269,643 | Health Care | large | unknown | 2026-06-14 |
| UNP | $272.63 | 41,811,595 | Industrials | large | unknown | 2026-06-14 |
| UPS | $108.11 | 24,412,097 | Industrials | large | unknown | 2026-06-14 |
| URI | $1073.77 | 32,256,891 | Industrials | large | unknown | 2026-06-14 |
| USB | $58.93 | 33,511,045 | Financials | large | unknown | 2026-06-14 |
| V | $322.39 | 114,646,462 | Financials | large | unknown | 2026-06-14 |
| VEEV | $159.56 | 27,486,468 | Health Care | large | unknown | 2026-06-14 |
| VLO | $258.56 | 32,266,349 | Energy | large | unknown | 2026-06-14 |
| VMC | $286.51 | 22,675,207 | Materials | large | unknown | 2026-06-14 |
| VRT | $302.77 | 81,913,788 | Industrials | large | unknown | 2026-06-14 |
| VRTX | $444.92 | 23,300,233 | Health Care | large | unknown | 2026-06-14 |
| VSH | $59.41 | 25,431,333 | Information Technology | small | unknown | 2026-06-14 |
| VST | $148.06 | 30,565,133 | Utilities | large | unknown | 2026-06-14 |
| VZ | $48.09 | 60,351,261 | Communication Services | large | unknown | 2026-06-14 |
| WAT | $355.09 | 26,958,155 | Health Care | large | unknown | 2026-06-14 |
| WBD | $26.97 | 45,516,371 | Communication Services | large | unknown | 2026-06-14 |
| WDAY | $130.88 | 38,225,610 | Information Technology | large | unknown | 2026-06-14 |
| WDC | $562.88 | 112,028,824 | Information Technology | large | unknown | 2026-06-14 |
| WELL | $214.01 | 32,459,461 | Real Estate | large | unknown | 2026-06-14 |
| WFC | $83.73 | 85,348,616 | Financials | large | unknown | 2026-06-14 |
| WM | $219.45 | 20,659,163 | Industrials | large | unknown | 2026-06-14 |
| WMB | $72.08 | 26,719,006 | Energy | large | unknown | 2026-06-14 |
| WMT | $121.05 | 127,812,958 | Consumer Staples | large | unknown | 2026-06-14 |
| XEL | $79.22 | 29,992,713 | Utilities | large | unknown | 2026-06-14 |
| XOM | $147.03 | 100,628,502 | Energy | large | unknown | 2026-06-14 |
| XPO | $228.33 | 21,752,690 | Industrials | mid | unknown | 2026-06-14 |
| ZTS | $79.56 | 28,294,012 | Health Care | large | unknown | 2026-06-14 |
