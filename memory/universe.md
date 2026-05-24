---
screened_on: 2026-05-24
expires_on: 2026-05-31
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
| AAL | $13.86 | 28,240,956 | Industrials | mid | unknown | 2026-05-24 |
| AAPL | $308.81 | 385,153,693 | Information Technology | large | unknown | 2026-05-24 |
| ABBV | $215.75 | 57,502,326 | Health Care | large | unknown | 2026-05-24 |
| ABNB | $132.37 | 26,662,483 | Consumer Discretionary | large | unknown | 2026-05-24 |
| ABT | $87.45 | 52,339,005 | Health Care | large | unknown | 2026-05-24 |
| ACN | $179.26 | 50,346,385 | Information Technology | large | unknown | 2026-05-24 |
| ADBE | $244.78 | 39,462,748 | Information Technology | large | unknown | 2026-05-24 |
| ADI | $397.02 | 74,453,061 | Information Technology | large | unknown | 2026-05-24 |
| ADP | $225.39 | 32,494,028 | Industrials | large | unknown | 2026-05-24 |
| ADSK | $241.00 | 25,463,009 | Information Technology | large | unknown | 2026-05-24 |
| AEIS | $324.73 | 23,838,767 | Information Technology | mid | unknown | 2026-05-24 |
| AEP | $131.60 | 30,738,717 | Utilities | large | unknown | 2026-05-24 |
| AJG | $204.63 | 31,106,083 | Financials | large | unknown | 2026-05-24 |
| AKAM | $147.24 | 44,855,374 | Information Technology | large | unknown | 2026-05-24 |
| ALB | $171.55 | 20,261,894 | Materials | large | unknown | 2026-05-24 |
| ALL | $216.52 | 22,419,618 | Unknown | large | unknown | 2026-05-24 |
| AMAT | $432.16 | 107,971,720 | Information Technology | large | unknown | 2026-05-24 |
| AMD | $467.64 | 339,350,897 | Information Technology | large | unknown | 2026-05-24 |
| AMGN | $339.20 | 29,307,720 | Health Care | large | unknown | 2026-05-24 |
| AMP | $452.44 | 20,189,093 | Financials | large | unknown | 2026-05-24 |
| AMT | $183.77 | 26,491,054 | Real Estate | large | unknown | 2026-05-24 |
| AMZN | $266.27 | 513,575,280 | Consumer Discretionary | large | unknown | 2026-05-24 |
| ANET | $154.06 | 85,722,564 | Information Technology | large | unknown | 2026-05-24 |
| AON | $324.84 | 32,839,807 | Financials | large | unknown | 2026-05-24 |
| APD | $289.37 | 21,072,083 | Materials | large | unknown | 2026-05-24 |
| APH | $132.13 | 83,165,225 | Information Technology | large | unknown | 2026-05-24 |
| APO | $128.49 | 26,953,159 | Financials | large | unknown | 2026-05-24 |
| APP | $481.70 | 97,669,477 | Unknown | large | unknown | 2026-05-24 |
| ARES | $124.40 | 25,619,588 | Unknown | large | unknown | 2026-05-24 |
| AVGO | $414.01 | 255,766,224 | Information Technology | large | unknown | 2026-05-24 |
| AXON | $385.93 | 21,720,043 | Industrials | large | unknown | 2026-05-24 |
| AXP | $311.78 | 38,470,200 | Unknown | large | unknown | 2026-05-24 |
| AZO | $3400.87 | 45,516,040 | Consumer Discretionary | large | unknown | 2026-05-24 |
| BA | $219.03 | 51,628,712 | Industrials | large | unknown | 2026-05-24 |
| BAC | $51.79 | 106,316,583 | Financials | large | unknown | 2026-05-24 |
| BDX | $147.62 | 30,582,901 | Health Care | large | unknown | 2026-05-24 |
| BKNG | $161.04 | 69,878,448 | Consumer Discretionary | large | unknown | 2026-05-24 |
| BKR | $66.02 | 28,423,445 | Unknown | large | unknown | 2026-05-24 |
| BLD | $407.80 | 27,582,576 | Unknown | mid | unknown | 2026-05-24 |
| BLK | $1072.73 | 35,842,353 | Unknown | large | unknown | 2026-05-24 |
| BMY | $59.45 | 37,849,762 | Health Care | large | unknown | 2026-05-24 |
| BNY | $139.24 | 23,316,241 | Unknown | large | unknown | 2026-05-24 |
| BRK.B | $486.31 | 65,223,255 | Financials | large | unknown | 2026-05-24 |
| BSX | $57.76 | 67,675,512 | Health Care | large | unknown | 2026-05-24 |
| BURL | $324.41 | 20,608,227 | Unknown | mid | unknown | 2026-05-24 |
| BX | $118.48 | 23,355,271 | Financials | large | unknown | 2026-05-24 |
| C | $125.06 | 56,812,724 | Financials | large | unknown | 2026-05-24 |
| CAH | $200.66 | 29,859,132 | Unknown | large | unknown | 2026-05-24 |
| CARR | $63.13 | 26,776,732 | Unknown | large | unknown | 2026-05-24 |
| CASY | $825.22 | 26,699,267 | Consumer Staples | large | unknown | 2026-05-24 |
| CAT | $879.93 | 93,435,548 | Industrials | large | unknown | 2026-05-24 |
| CB | $327.90 | 22,438,498 | Financials | large | unknown | 2026-05-24 |
| CBOE | $357.57 | 23,450,119 | Unknown | large | unknown | 2026-05-24 |
| CCL | $25.97 | 44,072,910 | Unknown | large | unknown | 2026-05-24 |
| CDNS | $373.67 | 42,137,516 | Unknown | large | unknown | 2026-05-24 |
| CEG | $294.00 | 54,732,521 | Unknown | large | unknown | 2026-05-24 |
| CF | $121.65 | 20,512,003 | Materials | large | unknown | 2026-05-24 |
| CHRW | $174.19 | 25,904,780 | Industrials | large | unknown | 2026-05-24 |
| CHTR | $145.08 | 29,177,599 | Unknown | large | unknown | 2026-05-24 |
| CI | $286.19 | 22,868,031 | Health Care | large | unknown | 2026-05-24 |
| CIEN | $583.71 | 56,648,326 | Unknown | large | unknown | 2026-05-24 |
| CL | $90.60 | 29,413,152 | Consumer Staples | large | unknown | 2026-05-24 |
| CMCSA | $25.20 | 58,962,618 | Unknown | large | unknown | 2026-05-24 |
| CME | $291.17 | 30,947,223 | Financials | large | unknown | 2026-05-24 |
| CMG | $32.88 | 41,168,807 | Consumer Discretionary | large | unknown | 2026-05-24 |
| CMI | $639.42 | 41,140,431 | Industrials | large | unknown | 2026-05-24 |
| COF | $187.69 | 51,832,280 | Financials | large | unknown | 2026-05-24 |
| COHR | $377.49 | 98,119,056 | Unknown | large | unknown | 2026-05-24 |
| COIN | $184.97 | 46,308,463 | Unknown | large | unknown | 2026-05-24 |
| COP | $120.44 | 63,055,734 | Energy | large | unknown | 2026-05-24 |
| COR | $274.99 | 39,569,420 | Unknown | large | unknown | 2026-05-24 |
| COST | $1027.85 | 64,297,868 | Consumer Staples | large | unknown | 2026-05-24 |
| CRH | $100.38 | 25,428,773 | Unknown | large | unknown | 2026-05-24 |
| CRM | $180.10 | 81,044,696 | Information Technology | large | unknown | 2026-05-24 |
| CRS | $434.23 | 25,758,372 | Materials | mid | unknown | 2026-05-24 |
| CRWD | $663.32 | 62,791,882 | Information Technology | large | unknown | 2026-05-24 |
| CSCO | $120.39 | 123,103,362 | Information Technology | large | unknown | 2026-05-24 |
| CSX | $45.52 | 37,751,537 | Industrials | large | unknown | 2026-05-24 |
| CTSH | $52.73 | 24,010,630 | Information Technology | large | unknown | 2026-05-24 |
| CVNA | $68.29 | 44,483,615 | Unknown | large | unknown | 2026-05-24 |
| CVS | $93.25 | 46,771,294 | Health Care | large | unknown | 2026-05-24 |
| CVX | $191.43 | 57,616,884 | Energy | large | unknown | 2026-05-24 |
| D | $67.66 | 32,519,522 | Utilities | large | unknown | 2026-05-24 |
| DAL | $76.16 | 25,711,830 | Industrials | large | unknown | 2026-05-24 |
| DASH | $160.27 | 48,330,441 | Unknown | large | unknown | 2026-05-24 |
| DDOG | $222.36 | 57,847,088 | Unknown | large | unknown | 2026-05-24 |
| DE | $529.26 | 39,646,027 | Industrials | large | unknown | 2026-05-24 |
| DELL | $295.23 | 62,282,543 | Information Technology | large | unknown | 2026-05-24 |
| DG | $105.67 | 23,354,404 | Consumer Staples | large | unknown | 2026-05-24 |
| DHR | $171.96 | 54,005,294 | Health Care | large | unknown | 2026-05-24 |
| DIS | $103.00 | 48,883,595 | Communication Services | large | unknown | 2026-05-24 |
| DOCN | $158.47 | 27,611,661 | Unknown | mid | unknown | 2026-05-24 |
| DOW | $35.99 | 29,103,315 | Materials | large | unknown | 2026-05-24 |
| DPZ | $316.53 | 24,255,178 | Consumer Discretionary | large | unknown | 2026-05-24 |
| DT | $41.21 | 22,675,028 | Unknown | mid | unknown | 2026-05-24 |
| DVN | $47.23 | 42,387,663 | Energy | large | unknown | 2026-05-24 |
| DXCM | $72.12 | 24,796,039 | Health Care | large | unknown | 2026-05-24 |
| EBAY | $115.72 | 38,676,697 | Consumer Discretionary | large | unknown | 2026-05-24 |
| ECL | $253.24 | 23,271,628 | Materials | large | unknown | 2026-05-24 |
| ELV | $394.51 | 31,118,961 | Unknown | large | unknown | 2026-05-24 |
| EME | $848.56 | 25,030,289 | Unknown | large | unknown | 2026-05-24 |
| EMR | $136.48 | 23,712,142 | Industrials | large | unknown | 2026-05-24 |
| ENTG | $135.30 | 24,448,188 | Unknown | mid | unknown | 2026-05-24 |
| EOG | $141.22 | 28,176,823 | Energy | large | unknown | 2026-05-24 |
| EQIX | $1079.63 | 35,430,018 | Real Estate | large | unknown | 2026-05-24 |
| EQT | $57.90 | 31,107,737 | Unknown | large | unknown | 2026-05-24 |
| ETN | $391.39 | 72,546,017 | Industrials | large | unknown | 2026-05-24 |
| ETR | $112.39 | 20,404,292 | Utilities | large | unknown | 2026-05-24 |
| EW | $85.81 | 21,938,231 | Health Care | large | unknown | 2026-05-24 |
| EXC | $46.22 | 23,380,514 | Utilities | large | unknown | 2026-05-24 |
| EXPE | $214.62 | 23,370,170 | Consumer Discretionary | large | unknown | 2026-05-24 |
| F | $14.95 | 63,384,609 | Consumer Discretionary | large | unknown | 2026-05-24 |
| FCX | $61.97 | 58,174,884 | Materials | large | unknown | 2026-05-24 |
| FDX | $394.32 | 30,397,624 | Industrials | large | unknown | 2026-05-24 |
| FICO | $1239.79 | 32,555,287 | Information Technology | large | unknown | 2026-05-24 |
| FIS | $43.56 | 22,261,783 | Financials | large | unknown | 2026-05-24 |
| FITB | $49.50 | 20,447,425 | Financials | large | unknown | 2026-05-24 |
| FIX | $1830.11 | 46,035,112 | Unknown | large | unknown | 2026-05-24 |
| FLEX | $132.46 | 50,559,109 | Unknown | mid | unknown | 2026-05-24 |
| FN | $704.01 | 50,186,490 | Unknown | mid | unknown | 2026-05-24 |
| FSLR | $257.88 | 27,641,445 | Unknown | large | unknown | 2026-05-24 |
| FTI | $70.96 | 23,974,410 | Unknown | mid | unknown | 2026-05-24 |
| FTNT | $133.99 | 29,723,331 | Information Technology | large | unknown | 2026-05-24 |
| GD | $342.93 | 26,177,913 | Industrials | large | unknown | 2026-05-24 |
| GE | $302.80 | 81,834,021 | Industrials | large | unknown | 2026-05-24 |
| GEHC | $64.25 | 24,512,446 | Health Care | large | unknown | 2026-05-24 |
| GEV | $1039.80 | 101,666,351 | Industrials | large | unknown | 2026-05-24 |
| GILD | $134.37 | 34,998,763 | Health Care | large | unknown | 2026-05-24 |
| GLW | $193.78 | 121,236,585 | Information Technology | large | unknown | 2026-05-24 |
| GM | $78.80 | 31,994,630 | Consumer Discretionary | large | unknown | 2026-05-24 |
| GOOG | $379.40 | 175,322,399 | Communication Services | large | unknown | 2026-05-24 |
| GOOGL | $383.03 | 386,889,064 | Communication Services | large | unknown | 2026-05-24 |
| GS | $996.73 | 65,772,714 | Financials | large | unknown | 2026-05-24 |
| GWW | $1247.87 | 24,924,579 | Industrials | large | unknown | 2026-05-24 |
| HAL | $41.46 | 28,506,938 | Energy | large | unknown | 2026-05-24 |
| HCA | $394.41 | 34,454,735 | Health Care | large | unknown | 2026-05-24 |
| HD | $313.06 | 71,208,525 | Consumer Discretionary | large | unknown | 2026-05-24 |
| HLT | $321.14 | 33,080,860 | Consumer Discretionary | large | unknown | 2026-05-24 |
| HON | $227.94 | 31,518,437 | Industrials | large | unknown | 2026-05-24 |
| HOOD | $73.63 | 60,221,524 | Unknown | large | unknown | 2026-05-24 |
| HPE | $37.58 | 46,004,817 | Information Technology | large | unknown | 2026-05-24 |
| HPQ | $25.25 | 22,003,646 | Information Technology | large | unknown | 2026-05-24 |
| HSY | $194.74 | 21,643,621 | Consumer Staples | large | unknown | 2026-05-24 |
| HUBB | $475.02 | 31,168,350 | Industrials | large | unknown | 2026-05-24 |
| HUM | $307.98 | 30,882,638 | Health Care | large | unknown | 2026-05-24 |
| HWM | $256.49 | 33,142,157 | Industrials | large | unknown | 2026-05-24 |
| IBM | $253.80 | 62,924,878 | Information Technology | large | unknown | 2026-05-24 |
| ICE | $152.99 | 23,894,613 | Financials | large | unknown | 2026-05-24 |
| IDXX | $559.49 | 21,393,639 | Health Care | large | unknown | 2026-05-24 |
| INTC | $119.85 | 387,071,523 | Information Technology | large | unknown | 2026-05-24 |
| INTU | $320.17 | 90,013,421 | Information Technology | large | unknown | 2026-05-24 |
| ISRG | $438.20 | 42,490,188 | Health Care | large | unknown | 2026-05-24 |
| ITW | $252.19 | 22,753,770 | Industrials | large | unknown | 2026-05-24 |
| JBL | $364.34 | 30,117,514 | Unknown | large | unknown | 2026-05-24 |
| JCI | $138.32 | 23,486,454 | Industrials | large | unknown | 2026-05-24 |
| JNJ | $234.37 | 61,474,570 | Health Care | large | unknown | 2026-05-24 |
| JPM | $306.34 | 63,123,510 | Financials | large | unknown | 2026-05-24 |
| KDP | $29.12 | 25,804,144 | Consumer Staples | large | unknown | 2026-05-24 |
| KEYS | $346.49 | 37,977,066 | Information Technology | large | unknown | 2026-05-24 |
| KKR | $94.03 | 32,378,268 | Unknown | large | unknown | 2026-05-24 |
| KLAC | $1888.64 | 119,753,202 | Information Technology | large | unknown | 2026-05-24 |
| KMI | $33.78 | 22,851,757 | Energy | large | unknown | 2026-05-24 |
| KNX | $70.17 | 20,179,491 | Unknown | mid | unknown | 2026-05-24 |
| KO | $81.49 | 72,696,602 | Consumer Staples | large | unknown | 2026-05-24 |
| KVUE | $17.54 | 22,094,964 | Unknown | large | unknown | 2026-05-24 |
| LHX | $311.95 | 28,507,070 | Industrials | large | unknown | 2026-05-24 |
| LIN | $517.68 | 45,403,439 | Materials | large | unknown | 2026-05-24 |
| LITE | $946.68 | 198,391,355 | Unknown | large | unknown | 2026-05-24 |
| LLY | $1065.60 | 129,734,275 | Health Care | large | unknown | 2026-05-24 |
| LMT | $533.41 | 32,386,441 | Industrials | large | unknown | 2026-05-24 |
| LOW | $214.94 | 34,454,441 | Consumer Discretionary | large | unknown | 2026-05-24 |
| LRCX | $305.43 | 91,375,540 | Information Technology | large | unknown | 2026-05-24 |
| LSCC | $143.23 | 29,019,778 | Unknown | mid | unknown | 2026-05-24 |
| LYB | $69.72 | 25,176,882 | Materials | large | unknown | 2026-05-24 |
| MA | $498.55 | 113,332,466 | Financials | large | unknown | 2026-05-24 |
| MAR | $369.14 | 27,492,228 | Unknown | large | unknown | 2026-05-24 |
| MCD | $282.31 | 43,937,112 | Consumer Discretionary | large | unknown | 2026-05-24 |
| MCHP | $93.42 | 53,260,368 | Information Technology | large | unknown | 2026-05-24 |
| MCK | $766.23 | 54,939,441 | Health Care | large | unknown | 2026-05-24 |
| MCO | $449.27 | 34,104,846 | Financials | large | unknown | 2026-05-24 |
| MDLZ | $61.75 | 29,237,029 | Consumer Staples | large | unknown | 2026-05-24 |
| MDT | $78.59 | 52,474,294 | Health Care | large | unknown | 2026-05-24 |
| META | $610.42 | 305,829,197 | Communication Services | large | unknown | 2026-05-24 |
| MKSI | $320.61 | 27,321,299 | Information Technology | mid | unknown | 2026-05-24 |
| MLM | $536.87 | 25,432,275 | Materials | large | unknown | 2026-05-24 |
| MMM | $152.44 | 26,565,759 | Industrials | large | unknown | 2026-05-24 |
| MNST | $86.79 | 23,484,405 | Consumer Staples | large | unknown | 2026-05-24 |
| MO | $73.88 | 50,561,298 | Consumer Staples | large | unknown | 2026-05-24 |
| MPC | $254.68 | 26,963,276 | Energy | large | unknown | 2026-05-24 |
| MPWR | $1590.23 | 60,626,672 | Information Technology | large | unknown | 2026-05-24 |
| MRK | $122.44 | 41,893,709 | Health Care | large | unknown | 2026-05-24 |
| MRSH | $164.13 | 21,863,310 | Unknown | large | unknown | 2026-05-24 |
| MS | $200.95 | 43,538,098 | Financials | large | unknown | 2026-05-24 |
| MSCI | $588.87 | 24,845,670 | Financials | large | unknown | 2026-05-24 |
| MSFT | $418.50 | 354,345,354 | Information Technology | large | unknown | 2026-05-24 |
| MSI | $404.08 | 37,714,256 | Information Technology | large | unknown | 2026-05-24 |
| MTD | $1102.71 | 21,248,862 | Health Care | large | unknown | 2026-05-24 |
| MTSI | $386.11 | 28,759,342 | Unknown | mid | unknown | 2026-05-24 |
| MTZ | $381.85 | 30,212,068 | Unknown | mid | unknown | 2026-05-24 |
| MU | $751.09 | 612,356,304 | Information Technology | large | unknown | 2026-05-24 |
| NCLH | $16.30 | 22,388,306 | Unknown | large | unknown | 2026-05-24 |
| NEE | $88.54 | 61,811,053 | Utilities | large | unknown | 2026-05-24 |
| NEM | $107.64 | 30,677,555 | Materials | large | unknown | 2026-05-24 |
| NFLX | $88.59 | 177,566,791 | Communication Services | large | unknown | 2026-05-24 |
| NKE | $44.67 | 44,594,628 | Consumer Discretionary | large | unknown | 2026-05-24 |
| NOC | $555.80 | 21,481,041 | Industrials | large | unknown | 2026-05-24 |
| NOW | $102.13 | 95,153,293 | Information Technology | large | unknown | 2026-05-24 |
| NRG | $137.67 | 25,731,062 | Utilities | large | unknown | 2026-05-24 |
| NVDA | $215.34 | 984,123,763 | Information Technology | large | unknown | 2026-05-24 |
| NVT | $164.73 | 20,191,905 | Industrials | mid | unknown | 2026-05-24 |
| NXPI | $316.46 | 58,268,202 | Unknown | large | unknown | 2026-05-24 |
| ODFL | $210.54 | 27,620,365 | Industrials | large | unknown | 2026-05-24 |
| ON | $116.17 | 64,565,536 | Information Technology | large | unknown | 2026-05-24 |
| ORCL | $192.09 | 121,508,011 | Information Technology | large | unknown | 2026-05-24 |
| ORLY | $91.74 | 23,596,607 | Consumer Discretionary | large | unknown | 2026-05-24 |
| OXY | $58.83 | 38,307,644 | Energy | large | unknown | 2026-05-24 |
| PANW | $260.67 | 74,893,909 | Unknown | large | unknown | 2026-05-24 |
| PEP | $150.56 | 30,697,476 | Consumer Staples | large | unknown | 2026-05-24 |
| PFE | $25.90 | 44,581,509 | Health Care | large | unknown | 2026-05-24 |
| PG | $144.40 | 49,420,782 | Consumer Staples | large | unknown | 2026-05-24 |
| PGR | $199.57 | 26,557,482 | Financials | large | unknown | 2026-05-24 |
| PH | $866.58 | 57,579,165 | Industrials | large | unknown | 2026-05-24 |
| PINS | $19.28 | 25,447,427 | Unknown | mid | unknown | 2026-05-24 |
| PLNT | $52.02 | 20,618,497 | Consumer Discretionary | mid | unknown | 2026-05-24 |
| PLTR | $136.84 | 140,990,939 | Unknown | large | unknown | 2026-05-24 |
| PM | $188.98 | 37,344,870 | Consumer Staples | large | unknown | 2026-05-24 |
| PODD | $154.81 | 21,429,375 | Health Care | large | unknown | 2026-05-24 |
| PPL | $36.33 | 21,057,287 | Utilities | large | unknown | 2026-05-24 |
| PRIM | $117.55 | 21,000,677 | Industrials | small | unknown | 2026-05-24 |
| PSX | $177.75 | 24,600,296 | Energy | large | unknown | 2026-05-24 |
| PWR | $723.18 | 71,987,517 | Industrials | large | unknown | 2026-05-24 |
| PYPL | $44.23 | 33,072,969 | Financials | large | unknown | 2026-05-24 |
| QCOM | $238.23 | 183,384,234 | Information Technology | large | unknown | 2026-05-24 |
| RCL | $256.23 | 41,400,092 | Consumer Discretionary | large | unknown | 2026-05-24 |
| REGN | $638.62 | 47,452,947 | Health Care | large | unknown | 2026-05-24 |
| ROK | $452.42 | 25,292,322 | Industrials | large | unknown | 2026-05-24 |
| ROST | $234.79 | 30,911,992 | Consumer Discretionary | large | unknown | 2026-05-24 |
| RRX | $200.71 | 23,291,241 | Unknown | mid | unknown | 2026-05-24 |
| RSG | $208.89 | 27,139,350 | Industrials | large | unknown | 2026-05-24 |
| RTX | $177.05 | 38,149,749 | Industrials | large | unknown | 2026-05-24 |
| SATS | $124.19 | 28,390,366 | Communication Services | large | unknown | 2026-05-24 |
| SBUX | $103.06 | 38,853,801 | Consumer Discretionary | large | unknown | 2026-05-24 |
| SCHW | $90.11 | 52,163,212 | Financials | large | unknown | 2026-05-24 |
| SHW | $309.23 | 33,332,780 | Materials | large | unknown | 2026-05-24 |
| SITM | $729.33 | 27,175,131 | Unknown | mid | unknown | 2026-05-24 |
| SLB | $57.27 | 40,706,496 | Energy | large | unknown | 2026-05-24 |
| SMCI | $35.58 | 48,158,900 | Information Technology | large | unknown | 2026-05-24 |
| SMTC | $156.73 | 26,490,715 | Information Technology | small | unknown | 2026-05-24 |
| SNDK | $1478.76 | 399,414,105 | Unknown | large | unknown | 2026-05-24 |
| SNPS | $524.81 | 37,545,943 | Information Technology | large | unknown | 2026-05-24 |
| SO | $94.52 | 28,722,974 | Utilities | large | unknown | 2026-05-24 |
| SPGI | $418.75 | 46,684,499 | Financials | large | unknown | 2026-05-24 |
| STRL | $732.31 | 28,501,966 | Unknown | mid | unknown | 2026-05-24 |
| STX | $812.98 | 151,708,631 | Information Technology | large | unknown | 2026-05-24 |
| SWKS | $82.41 | 20,501,310 | Information Technology | large | unknown | 2026-05-24 |
| SYK | $316.47 | 67,722,207 | Health Care | large | unknown | 2026-05-24 |
| T | $25.25 | 44,171,068 | Communication Services | large | unknown | 2026-05-24 |
| TDG | $1213.41 | 35,830,021 | Industrials | large | unknown | 2026-05-24 |
| TEL | $202.82 | 38,731,290 | Information Technology | large | unknown | 2026-05-24 |
| TER | $358.38 | 64,773,864 | Information Technology | large | unknown | 2026-05-24 |
| TFC | $48.38 | 21,209,374 | Financials | large | unknown | 2026-05-24 |
| TGT | $125.58 | 30,002,595 | Consumer Discretionary | large | unknown | 2026-05-24 |
| TJX | $158.22 | 38,339,301 | Consumer Discretionary | large | unknown | 2026-05-24 |
| TMO | $448.20 | 82,863,999 | Health Care | large | unknown | 2026-05-24 |
| TMUS | $191.46 | 45,646,793 | Communication Services | large | unknown | 2026-05-24 |
| TRGP | $276.75 | 20,016,494 | Unknown | large | unknown | 2026-05-24 |
| TSCO | $31.60 | 25,304,030 | Consumer Discretionary | large | unknown | 2026-05-24 |
| TSLA | $425.95 | 330,813,430 | Consumer Discretionary | large | unknown | 2026-05-24 |
| TT | $451.19 | 43,814,396 | Industrials | large | unknown | 2026-05-24 |
| TTD | $22.38 | 22,862,773 | Unknown | large | unknown | 2026-05-24 |
| TTMI | $190.04 | 20,326,582 | Information Technology | mid | unknown | 2026-05-24 |
| TTWO | $227.64 | 23,656,686 | Communication Services | large | unknown | 2026-05-24 |
| TWLO | $187.88 | 32,558,439 | Unknown | mid | unknown | 2026-05-24 |
| TXN | $309.05 | 94,940,674 | Information Technology | large | unknown | 2026-05-24 |
| UAL | $99.97 | 25,102,420 | Industrials | large | unknown | 2026-05-24 |
| UBER | $71.83 | 83,186,675 | Unknown | large | unknown | 2026-05-24 |
| ULTA | $515.17 | 22,687,618 | Consumer Discretionary | large | unknown | 2026-05-24 |
| UNH | $388.55 | 96,676,601 | Health Care | large | unknown | 2026-05-24 |
| UNP | $265.83 | 42,591,258 | Industrials | large | unknown | 2026-05-24 |
| UPS | $100.99 | 26,413,220 | Industrials | large | unknown | 2026-05-24 |
| URI | $938.80 | 35,409,227 | Industrials | large | unknown | 2026-05-24 |
| USB | $54.82 | 34,736,908 | Financials | large | unknown | 2026-05-24 |
| V | $328.90 | 153,586,404 | Financials | large | unknown | 2026-05-24 |
| VEEV | $160.33 | 32,929,094 | Unknown | large | unknown | 2026-05-24 |
| VLO | $246.85 | 35,558,895 | Energy | large | unknown | 2026-05-24 |
| VMC | $260.54 | 21,844,051 | Materials | large | unknown | 2026-05-24 |
| VRSK | $171.16 | 20,648,202 | Industrials | large | unknown | 2026-05-24 |
| VRT | $327.50 | 94,769,969 | Unknown | large | unknown | 2026-05-24 |
| VRTX | $434.55 | 22,088,780 | Health Care | large | unknown | 2026-05-24 |
| VST | $156.28 | 35,501,488 | Utilities | large | unknown | 2026-05-24 |
| VTR | $88.17 | 28,178,823 | Real Estate | large | unknown | 2026-05-24 |
| VZ | $48.36 | 53,177,245 | Communication Services | large | unknown | 2026-05-24 |
| WAT | $342.72 | 33,971,590 | Health Care | large | unknown | 2026-05-24 |
| WBD | $27.01 | 28,385,873 | Communication Services | large | unknown | 2026-05-24 |
| WCC | $363.47 | 21,481,757 | Unknown | mid | unknown | 2026-05-24 |
| WDAY | $128.06 | 28,668,675 | Unknown | large | unknown | 2026-05-24 |
| WDC | $484.12 | 123,673,470 | Information Technology | large | unknown | 2026-05-24 |
| WELL | $216.18 | 32,062,596 | Real Estate | large | unknown | 2026-05-24 |
| WFC | $76.40 | 76,090,394 | Financials | large | unknown | 2026-05-24 |
| WM | $217.99 | 22,429,194 | Industrials | large | unknown | 2026-05-24 |
| WMB | $78.45 | 32,009,356 | Energy | large | unknown | 2026-05-24 |
| WMT | $120.26 | 84,221,436 | Consumer Staples | large | unknown | 2026-05-24 |
| XEL | $81.07 | 28,475,573 | Utilities | large | unknown | 2026-05-24 |
| XOM | $154.83 | 109,564,536 | Energy | large | unknown | 2026-05-24 |
| XPO | $202.87 | 24,682,255 | Unknown | mid | unknown | 2026-05-24 |
| ZTS | $81.33 | 39,624,543 | Health Care | large | unknown | 2026-05-24 |
