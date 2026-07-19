---
screened_on: 2026-07-19
expires_on: 2026-07-26
total_passed: 306
total_rejected: 1228
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
| AAL | $14.98 | 56,096,334 | Industrials | mid | unknown | 2026-07-19 |
| AAPL | $333.75 | 666,552,434 | Information Technology | large | unknown | 2026-07-19 |
| ABBV | $254.52 | 81,174,176 | Health Care | large | unknown | 2026-07-19 |
| ABNB | $145.93 | 22,963,594 | Consumer Discretionary | large | unknown | 2026-07-19 |
| ABT | $100.68 | 67,889,546 | Health Care | large | unknown | 2026-07-19 |
| ACN | $143.51 | 81,810,650 | Information Technology | large | unknown | 2026-07-19 |
| ADBE | $237.19 | 56,821,273 | Information Technology | large | unknown | 2026-07-19 |
| ADI | $375.20 | 77,691,582 | Information Technology | large | unknown | 2026-07-19 |
| ADP | $255.37 | 21,305,690 | Industrials | large | unknown | 2026-07-19 |
| ADSK | $218.37 | 26,219,832 | Information Technology | large | unknown | 2026-07-19 |
| AEP | $132.12 | 27,478,104 | Utilities | large | unknown | 2026-07-19 |
| AJG | $253.93 | 28,419,647 | Financials | large | unknown | 2026-07-19 |
| AKAM | $120.21 | 24,676,335 | Information Technology | large | unknown | 2026-07-19 |
| AMAT | $529.12 | 314,906,712 | Information Technology | large | unknown | 2026-07-19 |
| AMD | $495.17 | 343,905,290 | Information Technology | large | unknown | 2026-07-19 |
| AMGN | $366.18 | 28,756,509 | Health Care | large | unknown | 2026-07-19 |
| AMT | $169.99 | 27,452,922 | Real Estate | large | unknown | 2026-07-19 |
| AMZN | $247.15 | 593,190,591 | Consumer Discretionary | large | unknown | 2026-07-19 |
| ANET | $168.53 | 72,236,504 | Information Technology | large | unknown | 2026-07-19 |
| AON | $367.09 | 24,949,628 | Financials | large | unknown | 2026-07-19 |
| APD | $295.52 | 21,963,343 | Materials | large | unknown | 2026-07-19 |
| APH | $151.21 | 61,311,509 | Information Technology | large | unknown | 2026-07-19 |
| APO | $120.44 | 32,803,354 | Financials | large | unknown | 2026-07-19 |
| APP | $424.36 | 92,614,061 | Unknown | large | unknown | 2026-07-19 |
| AVGO | $370.69 | 279,226,620 | Information Technology | large | unknown | 2026-07-19 |
| AXON | $510.82 | 28,338,469 | Industrials | large | unknown | 2026-07-19 |
| AXP | $355.35 | 43,444,100 | Unknown | large | unknown | 2026-07-19 |
| AZO | $3044.01 | 53,881,731 | Consumer Discretionary | large | unknown | 2026-07-19 |
| BA | $214.12 | 40,503,598 | Industrials | large | unknown | 2026-07-19 |
| BAC | $61.28 | 145,325,706 | Financials | large | unknown | 2026-07-19 |
| BKNG | $181.62 | 62,088,241 | Consumer Discretionary | large | unknown | 2026-07-19 |
| BKR | $55.94 | 38,332,494 | Unknown | large | unknown | 2026-07-19 |
| BLD | $353.73 | 34,405,020 | Unknown | mid | unknown | 2026-07-19 |
| BLK | $1072.46 | 72,567,926 | Unknown | large | unknown | 2026-07-19 |
| BMY | $60.74 | 46,115,361 | Health Care | large | unknown | 2026-07-19 |
| BNY | $157.12 | 23,484,895 | Unknown | large | unknown | 2026-07-19 |
| BRK.B | $490.88 | 66,643,186 | Financials | large | unknown | 2026-07-19 |
| BSX | $44.02 | 64,318,523 | Health Care | large | unknown | 2026-07-19 |
| BX | $126.85 | 24,674,275 | Financials | large | unknown | 2026-07-19 |
| C | $129.34 | 82,216,876 | Financials | large | unknown | 2026-07-19 |
| CAH | $228.56 | 28,191,302 | Unknown | large | unknown | 2026-07-19 |
| CARR | $68.69 | 20,665,654 | Unknown | large | unknown | 2026-07-19 |
| CASY | $859.39 | 31,229,803 | Consumer Staples | large | unknown | 2026-07-19 |
| CAT | $880.31 | 155,708,395 | Industrials | large | unknown | 2026-07-19 |
| CB | $352.21 | 28,850,725 | Financials | large | unknown | 2026-07-19 |
| CBOE | $273.28 | 26,971,939 | Unknown | large | unknown | 2026-07-19 |
| CCL | $26.40 | 37,501,327 | Unknown | large | unknown | 2026-07-19 |
| CDE | $14.37 | 22,939,245 | Unknown | mid | unknown | 2026-07-19 |
| CDNS | $330.05 | 40,705,579 | Unknown | large | unknown | 2026-07-19 |
| CEG | $252.36 | 46,864,356 | Unknown | large | unknown | 2026-07-19 |
| CFG | $72.39 | 28,720,663 | Financials | large | unknown | 2026-07-19 |
| CHTR | $131.29 | 22,108,199 | Unknown | large | unknown | 2026-07-19 |
| CI | $281.46 | 23,655,298 | Health Care | large | unknown | 2026-07-19 |
| CIEN | $374.32 | 56,498,247 | Unknown | large | unknown | 2026-07-19 |
| CL | $92.95 | 21,489,640 | Consumer Staples | large | unknown | 2026-07-19 |
| CMCSA | $23.78 | 55,829,683 | Unknown | large | unknown | 2026-07-19 |
| CME | $245.03 | 51,494,422 | Financials | large | unknown | 2026-07-19 |
| CMG | $34.43 | 47,883,942 | Consumer Discretionary | large | unknown | 2026-07-19 |
| CMI | $648.39 | 34,404,381 | Industrials | large | unknown | 2026-07-19 |
| CNP | $43.12 | 21,785,681 | Unknown | large | unknown | 2026-07-19 |
| COF | $208.01 | 42,114,150 | Financials | large | unknown | 2026-07-19 |
| COHR | $277.65 | 75,859,971 | Unknown | large | unknown | 2026-07-19 |
| COIN | $157.09 | 33,916,040 | Unknown | large | unknown | 2026-07-19 |
| COP | $114.70 | 49,106,332 | Energy | large | unknown | 2026-07-19 |
| COR | $307.84 | 28,622,890 | Unknown | large | unknown | 2026-07-19 |
| COST | $940.84 | 78,383,091 | Consumer Staples | large | unknown | 2026-07-19 |
| CPRT | $27.59 | 25,354,566 | Industrials | large | unknown | 2026-07-19 |
| CRH | $102.88 | 21,558,902 | Unknown | large | unknown | 2026-07-19 |
| CRM | $170.82 | 75,881,043 | Information Technology | large | unknown | 2026-07-19 |
| CRS | $557.50 | 33,024,931 | Materials | mid | unknown | 2026-07-19 |
| CRWD | $203.12 | 62,737,703 | Information Technology | large | unknown | 2026-07-19 |
| CSCO | $111.97 | 115,519,134 | Information Technology | large | unknown | 2026-07-19 |
| CSX | $50.74 | 43,963,705 | Industrials | large | unknown | 2026-07-19 |
| CTSH | $44.75 | 43,509,237 | Information Technology | large | unknown | 2026-07-19 |
| CVNA | $67.35 | 35,433,424 | Unknown | large | unknown | 2026-07-19 |
| CVS | $107.47 | 38,495,035 | Health Care | large | unknown | 2026-07-19 |
| CVX | $187.35 | 61,153,546 | Energy | large | unknown | 2026-07-19 |
| D | $71.05 | 36,108,481 | Utilities | large | unknown | 2026-07-19 |
| DAL | $84.15 | 33,709,585 | Industrials | large | unknown | 2026-07-19 |
| DASH | $184.12 | 46,126,850 | Unknown | large | unknown | 2026-07-19 |
| DDOG | $258.73 | 62,794,855 | Unknown | large | unknown | 2026-07-19 |
| DE | $597.36 | 34,325,487 | Industrials | large | unknown | 2026-07-19 |
| DELL | $396.40 | 112,452,270 | Information Technology | large | unknown | 2026-07-19 |
| DHR | $203.75 | 41,090,639 | Health Care | large | unknown | 2026-07-19 |
| DIS | $97.66 | 52,876,626 | Communication Services | large | unknown | 2026-07-19 |
| DKS | $217.43 | 20,717,778 | Consumer Discretionary | mid | unknown | 2026-07-19 |
| DLR | $173.85 | 32,936,522 | Unknown | large | unknown | 2026-07-19 |
| DOCN | $118.93 | 23,747,688 | Unknown | mid | unknown | 2026-07-19 |
| DOW | $29.93 | 27,754,252 | Materials | large | unknown | 2026-07-19 |
| DRI | $198.51 | 24,096,636 | Consumer Discretionary | large | unknown | 2026-07-19 |
| DVN | $43.83 | 38,126,372 | Energy | large | unknown | 2026-07-19 |
| EA | $208.90 | 27,161,114 | Communication Services | large | unknown | 2026-07-19 |
| ECHO | $91.99 | 42,373,121 | Unknown | large | unknown | 2026-07-19 |
| ELV | $372.94 | 34,048,547 | Unknown | large | unknown | 2026-07-19 |
| EME | $743.66 | 20,907,682 | Unknown | large | unknown | 2026-07-19 |
| EMR | $139.47 | 21,862,712 | Industrials | large | unknown | 2026-07-19 |
| ENTG | $138.74 | 33,939,153 | Unknown | mid | unknown | 2026-07-19 |
| EOG | $139.89 | 21,484,933 | Energy | large | unknown | 2026-07-19 |
| EQIX | $1020.22 | 45,604,845 | Real Estate | large | unknown | 2026-07-19 |
| EQT | $49.56 | 31,275,074 | Unknown | large | unknown | 2026-07-19 |
| ETN | $399.86 | 50,196,184 | Industrials | large | unknown | 2026-07-19 |
| EW | $85.70 | 24,509,762 | Health Care | large | unknown | 2026-07-19 |
| EXC | $46.27 | 27,852,720 | Utilities | large | unknown | 2026-07-19 |
| EXPE | $268.67 | 20,109,664 | Consumer Discretionary | large | unknown | 2026-07-19 |
| F | $14.21 | 27,527,892 | Consumer Discretionary | large | unknown | 2026-07-19 |
| FANG | $195.55 | 22,587,477 | Unknown | large | unknown | 2026-07-19 |
| FAST | $45.46 | 28,691,561 | Industrials | large | unknown | 2026-07-19 |
| FCX | $58.37 | 59,982,889 | Materials | large | unknown | 2026-07-19 |
| FDX | $312.99 | 46,896,681 | Industrials | large | unknown | 2026-07-19 |
| FICO | $1257.10 | 22,756,761 | Information Technology | large | unknown | 2026-07-19 |
| FITB | $58.01 | 32,475,878 | Financials | large | unknown | 2026-07-19 |
| FIX | $1670.91 | 52,490,107 | Unknown | large | unknown | 2026-07-19 |
| FLEX | $119.20 | 41,130,914 | Unknown | large | unknown | 2026-07-19 |
| FN | $479.04 | 36,713,295 | Unknown | mid | unknown | 2026-07-19 |
| FSLR | $211.75 | 21,633,679 | Unknown | large | unknown | 2026-07-19 |
| FTNT | $161.60 | 34,898,168 | Information Technology | large | unknown | 2026-07-19 |
| GE | $348.77 | 78,498,463 | Industrials | large | unknown | 2026-07-19 |
| GEV | $1057.40 | 160,114,980 | Industrials | large | unknown | 2026-07-19 |
| GILD | $134.23 | 41,834,209 | Health Care | large | unknown | 2026-07-19 |
| GIS | $37.97 | 28,846,930 | Consumer Staples | large | unknown | 2026-07-19 |
| GLW | $154.64 | 146,909,991 | Information Technology | large | unknown | 2026-07-19 |
| GM | $76.03 | 24,268,154 | Consumer Discretionary | large | unknown | 2026-07-19 |
| GOOG | $346.17 | 220,254,833 | Communication Services | large | unknown | 2026-07-19 |
| GOOGL | $346.76 | 400,305,637 | Communication Services | large | unknown | 2026-07-19 |
| GS | $1065.71 | 83,713,134 | Financials | large | unknown | 2026-07-19 |
| GWW | $1395.21 | 27,652,294 | Industrials | large | unknown | 2026-07-19 |
| HAL | $35.22 | 32,054,770 | Energy | large | unknown | 2026-07-19 |
| HCA | $371.43 | 32,565,242 | Health Care | large | unknown | 2026-07-19 |
| HD | $338.91 | 66,267,623 | Consumer Discretionary | large | unknown | 2026-07-19 |
| HLT | $321.33 | 46,174,624 | Consumer Discretionary | large | unknown | 2026-07-19 |
| HON | $225.00 | 46,309,889 | Industrials | large | unknown | 2026-07-19 |
| HONA | $212.19 | 36,653,857 | Unknown | large | unknown | 2026-07-19 |
| HOOD | $99.95 | 98,644,040 | Unknown | large | unknown | 2026-07-19 |
| HPE | $45.82 | 75,979,620 | Information Technology | large | unknown | 2026-07-19 |
| HPQ | $24.83 | 27,889,552 | Information Technology | large | unknown | 2026-07-19 |
| HSY | $171.41 | 20,352,895 | Consumer Staples | large | unknown | 2026-07-19 |
| HUBB | $488.86 | 21,979,205 | Industrials | large | unknown | 2026-07-19 |
| HUM | $400.21 | 31,210,197 | Health Care | large | unknown | 2026-07-19 |
| HWM | $272.38 | 44,734,241 | Industrials | large | unknown | 2026-07-19 |
| IBM | $212.67 | 114,143,320 | Information Technology | large | unknown | 2026-07-19 |
| ICE | $139.72 | 29,301,067 | Financials | large | unknown | 2026-07-19 |
| IDXX | $567.10 | 25,976,962 | Health Care | large | unknown | 2026-07-19 |
| ILMN | $186.76 | 21,459,635 | Health Care | mid | unknown | 2026-07-19 |
| INTC | $95.03 | 377,003,792 | Information Technology | large | unknown | 2026-07-19 |
| INTU | $291.04 | 89,608,743 | Information Technology | large | unknown | 2026-07-19 |
| ISRG | $345.40 | 62,496,007 | Health Care | large | unknown | 2026-07-19 |
| JBHT | $291.43 | 20,507,273 | Industrials | large | unknown | 2026-07-19 |
| JBL | $300.83 | 28,754,779 | Unknown | large | unknown | 2026-07-19 |
| JCI | $140.48 | 30,595,383 | Industrials | large | unknown | 2026-07-19 |
| JNJ | $253.01 | 95,523,846 | Health Care | large | unknown | 2026-07-19 |
| JPM | $341.10 | 95,368,227 | Financials | large | unknown | 2026-07-19 |
| KDP | $30.90 | 32,291,619 | Consumer Staples | large | unknown | 2026-07-19 |
| KEYS | $315.76 | 32,640,319 | Information Technology | large | unknown | 2026-07-19 |
| KKR | $100.92 | 26,988,427 | Unknown | large | unknown | 2026-07-19 |
| KLAC | $212.84 | 165,066,763 | Information Technology | large | unknown | 2026-07-19 |
| KMB | $108.31 | 22,096,452 | Consumer Staples | large | unknown | 2026-07-19 |
| KNX | $76.66 | 20,165,669 | Unknown | mid | unknown | 2026-07-19 |
| KO | $81.56 | 109,473,822 | Consumer Staples | large | unknown | 2026-07-19 |
| KR | $58.86 | 31,191,579 | Consumer Staples | large | unknown | 2026-07-19 |
| KVUE | $18.98 | 32,346,173 | Unknown | large | unknown | 2026-07-19 |
| LHX | $281.92 | 24,710,256 | Industrials | large | unknown | 2026-07-19 |
| LIN | $513.01 | 51,979,840 | Materials | large | unknown | 2026-07-19 |
| LITE | $732.49 | 149,186,681 | Unknown | large | unknown | 2026-07-19 |
| LLY | $1178.57 | 152,556,325 | Health Care | large | unknown | 2026-07-19 |
| LMT | $508.78 | 24,542,265 | Industrials | large | unknown | 2026-07-19 |
| LOW | $208.71 | 25,630,558 | Consumer Discretionary | large | unknown | 2026-07-19 |
| LRCX | $313.12 | 201,487,376 | Information Technology | large | unknown | 2026-07-19 |
| LSCC | $125.21 | 20,610,108 | Unknown | mid | unknown | 2026-07-19 |
| LYV | $180.26 | 22,550,630 | Communication Services | large | unknown | 2026-07-19 |
| MA | $543.49 | 90,090,336 | Financials | large | unknown | 2026-07-19 |
| MAR | $366.25 | 33,646,550 | Unknown | large | unknown | 2026-07-19 |
| MARA | $10.70 | 21,221,802 | Financials | small | unknown | 2026-07-19 |
| MCD | $267.67 | 52,999,097 | Consumer Discretionary | large | unknown | 2026-07-19 |
| MCHP | $80.94 | 36,495,124 | Information Technology | large | unknown | 2026-07-19 |
| MCK | $841.44 | 43,300,897 | Health Care | large | unknown | 2026-07-19 |
| MCO | $510.70 | 30,661,336 | Financials | large | unknown | 2026-07-19 |
| MDLZ | $60.98 | 41,051,843 | Consumer Staples | large | unknown | 2026-07-19 |
| MDT | $83.19 | 50,008,481 | Health Care | large | unknown | 2026-07-19 |
| META | $646.03 | 490,259,835 | Communication Services | large | unknown | 2026-07-19 |
| MKSI | $324.53 | 40,441,079 | Information Technology | mid | unknown | 2026-07-19 |
| MLM | $562.65 | 27,689,440 | Materials | large | unknown | 2026-07-19 |
| MNST | $97.47 | 26,988,894 | Consumer Staples | large | unknown | 2026-07-19 |
| MO | $74.20 | 28,508,756 | Consumer Staples | large | unknown | 2026-07-19 |
| MPC | $312.62 | 35,051,855 | Energy | large | unknown | 2026-07-19 |
| MPWR | $1310.84 | 66,714,227 | Information Technology | large | unknown | 2026-07-19 |
| MRK | $127.48 | 50,896,705 | Health Care | large | unknown | 2026-07-19 |
| MRNA | $61.80 | 20,094,494 | Health Care | large | unknown | 2026-07-19 |
| MRVL | $188.66 | 238,370,318 | Unknown | large | unknown | 2026-07-19 |
| MS | $215.42 | 70,237,254 | Financials | large | unknown | 2026-07-19 |
| MSCI | $628.73 | 29,767,445 | Financials | large | unknown | 2026-07-19 |
| MSFT | $394.01 | 520,326,712 | Information Technology | large | unknown | 2026-07-19 |
| MSI | $413.41 | 21,507,296 | Information Technology | large | unknown | 2026-07-19 |
| MTD | $1309.47 | 20,845,224 | Health Care | large | unknown | 2026-07-19 |
| MTSI | $267.33 | 28,580,204 | Unknown | mid | unknown | 2026-07-19 |
| MTZ | $329.70 | 33,913,706 | Unknown | mid | unknown | 2026-07-19 |
| MU | $849.46 | 1,187,744,864 | Information Technology | large | unknown | 2026-07-19 |
| NDAQ | $91.64 | 21,523,390 | Financials | large | unknown | 2026-07-19 |
| NEE | $88.78 | 69,244,546 | Utilities | large | unknown | 2026-07-19 |
| NEM | $89.78 | 41,144,373 | Materials | large | unknown | 2026-07-19 |
| NFLX | $68.87 | 251,866,823 | Communication Services | large | unknown | 2026-07-19 |
| NKE | $43.76 | 65,468,405 | Consumer Discretionary | large | unknown | 2026-07-19 |
| NOC | $521.62 | 34,052,660 | Industrials | large | unknown | 2026-07-19 |
| NOW | $103.22 | 80,769,628 | Information Technology | large | unknown | 2026-07-19 |
| NTAP | $163.73 | 24,645,483 | Information Technology | large | unknown | 2026-07-19 |
| NVDA | $202.80 | 950,342,679 | Information Technology | large | unknown | 2026-07-19 |
| NVT | $154.92 | 21,257,926 | Industrials | mid | unknown | 2026-07-19 |
| NXPI | $266.59 | 47,383,648 | Unknown | large | unknown | 2026-07-19 |
| NXT | $103.14 | 21,460,398 | Unknown | mid | unknown | 2026-07-19 |
| O | $65.69 | 24,184,743 | Real Estate | large | unknown | 2026-07-19 |
| ODFL | $233.85 | 20,486,459 | Industrials | large | unknown | 2026-07-19 |
| OKTA | $149.32 | 21,411,801 | Information Technology | mid | unknown | 2026-07-19 |
| ON | $87.41 | 60,816,547 | Information Technology | large | unknown | 2026-07-19 |
| ONTO | $279.50 | 33,418,970 | Information Technology | mid | unknown | 2026-07-19 |
| ORCL | $126.43 | 191,031,701 | Information Technology | large | unknown | 2026-07-19 |
| ORLY | $86.06 | 33,508,709 | Consumer Discretionary | large | unknown | 2026-07-19 |
| OXY | $54.85 | 38,330,774 | Energy | large | unknown | 2026-07-19 |
| PANW | $358.62 | 93,023,376 | Unknown | large | unknown | 2026-07-19 |
| PEP | $137.08 | 51,205,114 | Consumer Staples | large | unknown | 2026-07-19 |
| PFE | $25.05 | 63,701,669 | Health Care | large | unknown | 2026-07-19 |
| PG | $149.98 | 55,185,692 | Consumer Staples | large | unknown | 2026-07-19 |
| PGR | $207.83 | 41,155,876 | Financials | large | unknown | 2026-07-19 |
| PH | $952.67 | 37,121,539 | Industrials | large | unknown | 2026-07-19 |
| PLD | $149.71 | 25,956,314 | Real Estate | large | unknown | 2026-07-19 |
| PLTR | $132.37 | 160,209,340 | Unknown | large | unknown | 2026-07-19 |
| PM | $192.79 | 38,233,984 | Consumer Staples | large | unknown | 2026-07-19 |
| PNC | $252.93 | 30,168,164 | Financials | large | unknown | 2026-07-19 |
| PPL | $35.85 | 20,984,617 | Utilities | large | unknown | 2026-07-19 |
| PSX | $206.85 | 26,074,448 | Energy | large | unknown | 2026-07-19 |
| PWR | $628.24 | 55,376,994 | Industrials | large | unknown | 2026-07-19 |
| PYPL | $56.58 | 42,888,609 | Financials | large | unknown | 2026-07-19 |
| QCOM | $171.77 | 120,313,197 | Information Technology | large | unknown | 2026-07-19 |
| RCL | $287.02 | 42,073,221 | Consumer Discretionary | large | unknown | 2026-07-19 |
| REGN | $676.57 | 39,795,825 | Health Care | large | unknown | 2026-07-19 |
| RF | $31.66 | 21,412,067 | Financials | large | unknown | 2026-07-19 |
| ROK | $461.73 | 25,543,310 | Industrials | large | unknown | 2026-07-19 |
| ROKU | $144.49 | 30,831,666 | Unknown | mid | unknown | 2026-07-19 |
| ROST | $233.57 | 30,707,267 | Consumer Discretionary | large | unknown | 2026-07-19 |
| RRX | $207.04 | 22,242,421 | Unknown | mid | unknown | 2026-07-19 |
| RTX | $193.47 | 33,872,277 | Industrials | large | unknown | 2026-07-19 |
| SBUX | $105.47 | 31,675,852 | Consumer Discretionary | large | unknown | 2026-07-19 |
| SCHW | $101.60 | 58,911,395 | Financials | large | unknown | 2026-07-19 |
| SHW | $331.24 | 37,944,058 | Materials | large | unknown | 2026-07-19 |
| SLB | $46.99 | 42,888,465 | Energy | large | unknown | 2026-07-19 |
| SMCI | $24.18 | 56,585,734 | Information Technology | large | unknown | 2026-07-19 |
| SMTC | $124.91 | 28,378,665 | Information Technology | mid | unknown | 2026-07-19 |
| SNDK | $1352.67 | 596,737,088 | Unknown | large | unknown | 2026-07-19 |
| SNPS | $384.29 | 40,492,043 | Information Technology | large | unknown | 2026-07-19 |
| SO | $95.31 | 25,546,548 | Utilities | large | unknown | 2026-07-19 |
| SPGI | $450.81 | 57,586,424 | Financials | large | unknown | 2026-07-19 |
| STRL | $638.35 | 32,792,136 | Unknown | mid | unknown | 2026-07-19 |
| STT | $182.53 | 25,620,507 | Financials | large | unknown | 2026-07-19 |
| STX | $786.60 | 217,596,221 | Information Technology | large | unknown | 2026-07-19 |
| STZ | $132.87 | 21,335,415 | Consumer Staples | large | unknown | 2026-07-19 |
| SYK | $319.74 | 56,207,795 | Health Care | large | unknown | 2026-07-19 |
| T | $21.80 | 85,888,500 | Communication Services | large | unknown | 2026-07-19 |
| TDG | $1213.96 | 38,616,643 | Industrials | large | unknown | 2026-07-19 |
| TECH | $72.11 | 27,084,756 | Health Care | large | unknown | 2026-07-19 |
| TEL | $203.23 | 30,675,623 | Information Technology | large | unknown | 2026-07-19 |
| TER | $322.02 | 79,794,283 | Information Technology | large | unknown | 2026-07-19 |
| TFC | $52.51 | 29,032,649 | Financials | large | unknown | 2026-07-19 |
| TGT | $139.62 | 29,867,217 | Consumer Discretionary | large | unknown | 2026-07-19 |
| TJX | $154.47 | 38,598,102 | Consumer Discretionary | large | unknown | 2026-07-19 |
| TLN | $372.55 | 21,903,946 | Unknown | mid | unknown | 2026-07-19 |
| TMO | $532.16 | 59,932,333 | Health Care | large | unknown | 2026-07-19 |
| TMUS | $192.44 | 41,795,694 | Communication Services | large | unknown | 2026-07-19 |
| TPR | $141.47 | 21,422,150 | Consumer Discretionary | large | unknown | 2026-07-19 |
| TRGP | $283.43 | 22,866,169 | Unknown | large | unknown | 2026-07-19 |
| TRV | $369.10 | 26,775,187 | Financials | large | unknown | 2026-07-19 |
| TSCO | $30.48 | 24,994,838 | Consumer Discretionary | large | unknown | 2026-07-19 |
| TSLA | $380.90 | 384,137,901 | Consumer Discretionary | large | unknown | 2026-07-19 |
| TT | $469.85 | 39,829,028 | Industrials | large | unknown | 2026-07-19 |
| TTMI | $132.02 | 28,104,442 | Information Technology | mid | unknown | 2026-07-19 |
| TTWO | $236.68 | 30,851,850 | Communication Services | large | unknown | 2026-07-19 |
| TWLO | $206.61 | 23,146,268 | Unknown | mid | unknown | 2026-07-19 |
| TXN | $284.02 | 108,388,713 | Information Technology | large | unknown | 2026-07-19 |
| UAL | $115.39 | 31,876,989 | Industrials | large | unknown | 2026-07-19 |
| UBER | $72.47 | 89,744,832 | Unknown | large | unknown | 2026-07-19 |
| UNH | $426.06 | 106,354,151 | Health Care | large | unknown | 2026-07-19 |
| UNP | $301.65 | 39,460,016 | Industrials | large | unknown | 2026-07-19 |
| URI | $1045.26 | 28,877,422 | Industrials | large | unknown | 2026-07-19 |
| USB | $63.16 | 40,509,544 | Financials | large | unknown | 2026-07-19 |
| V | $358.51 | 127,447,091 | Financials | large | unknown | 2026-07-19 |
| VEEV | $195.28 | 21,198,077 | Unknown | large | unknown | 2026-07-19 |
| VLO | $309.64 | 40,640,606 | Energy | large | unknown | 2026-07-19 |
| VMC | $288.17 | 26,566,349 | Materials | large | unknown | 2026-07-19 |
| VRSK | $200.72 | 28,080,041 | Industrials | large | unknown | 2026-07-19 |
| VRT | $289.44 | 94,464,427 | Unknown | large | unknown | 2026-07-19 |
| VRTX | $485.58 | 41,908,465 | Health Care | large | unknown | 2026-07-19 |
| VSH | $37.82 | 21,926,296 | Information Technology | small | unknown | 2026-07-19 |
| VST | $155.23 | 32,003,706 | Utilities | large | unknown | 2026-07-19 |
| VZ | $43.59 | 96,736,558 | Communication Services | large | unknown | 2026-07-19 |
| WAT | $368.77 | 22,843,077 | Health Care | large | unknown | 2026-07-19 |
| WBD | $26.85 | 46,689,737 | Communication Services | large | unknown | 2026-07-19 |
| WBS | $75.96 | 20,584,721 | Unknown | mid | unknown | 2026-07-19 |
| WCC | $327.87 | 20,550,520 | Unknown | mid | unknown | 2026-07-19 |
| WDAY | $144.77 | 25,052,977 | Unknown | large | unknown | 2026-07-19 |
| WDC | $477.01 | 242,526,788 | Information Technology | large | unknown | 2026-07-19 |
| WELL | $243.33 | 36,138,148 | Real Estate | large | unknown | 2026-07-19 |
| WFC | $87.52 | 93,389,266 | Financials | large | unknown | 2026-07-19 |
| WM | $239.32 | 23,705,904 | Industrials | large | unknown | 2026-07-19 |
| WMB | $73.39 | 33,513,521 | Energy | large | unknown | 2026-07-19 |
| WMT | $114.22 | 107,402,715 | Consumer Staples | large | unknown | 2026-07-19 |
| WWD | $392.73 | 23,971,148 | Industrials | mid | unknown | 2026-07-19 |
| XEL | $78.74 | 25,233,133 | Utilities | large | unknown | 2026-07-19 |
| XOM | $147.39 | 75,087,555 | Energy | large | unknown | 2026-07-19 |
| YUM | $147.89 | 20,607,165 | Consumer Discretionary | large | unknown | 2026-07-19 |
