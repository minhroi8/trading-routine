---
screened_on: 2026-09-13
expires_on: 2026-09-20
total_passed: 227
total_rejected: 1273
universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
source_500: https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv
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
| A | $146.90 | $22,481,208 | Health Care | large | unknown | 2026-09-13 |
| AAL | $13.00 | $21,827,562 | Industrials | mid | unknown | 2026-09-13 |
| AAPL | $332.25 | $404,429,903 | Information Technology | large | unknown | 2026-09-13 |
| ABBV | $257.13 | $42,754,352 | Health Care | large | unknown | 2026-09-13 |
| ABNB | $170.22 | $36,903,406 | Consumer Discretionary | large | unknown | 2026-09-13 |
| ABT | $101.97 | $41,426,141 | Health Care | large | unknown | 2026-09-13 |
| ACN | $183.89 | $37,533,853 | Information Technology | large | unknown | 2026-09-13 |
| ADBE | $252.32 | $49,272,815 | Information Technology | large | unknown | 2026-09-13 |
| ADI | $378.80 | $49,209,018 | Information Technology | large | unknown | 2026-09-13 |
| ADP | $268.29 | $20,450,354 | Industrials | large | unknown | 2026-09-13 |
| ADSK | $212.43 | $26,357,677 | Information Technology | large | unknown | 2026-09-13 |
| ALL | $253.61 | $21,956,660 | Financials | large | unknown | 2026-09-13 |
| AMAT | $456.56 | $116,877,897 | Information Technology | large | unknown | 2026-09-13 |
| AMD | $516.12 | $225,603,975 | Information Technology | large | unknown | 2026-09-13 |
| AMGN | $377.29 | $42,494,576 | Health Care | large | unknown | 2026-09-13 |
| AMZN | $256.80 | $305,008,222 | Consumer Discretionary | large | unknown | 2026-09-13 |
| ANET | $199.74 | $42,381,651 | Information Technology | large | unknown | 2026-09-13 |
| AON | $302.67 | $24,301,217 | Financials | large | unknown | 2026-09-13 |
| APH | $83.92 | $47,556,381 | Information Technology | large | unknown | 2026-09-13 |
| APP | $323.88 | $48,230,245 | Information Technology | large | unknown | 2026-09-13 |
| ATI | $198.47 | $21,960,166 | Industrials | mid | unknown | 2026-09-13 |
| AVGO | $361.90 | $305,613,585 | Information Technology | large | unknown | 2026-09-13 |
| AXP | $324.78 | $36,458,786 | Financials | large | unknown | 2026-09-13 |
| AZO | $2878.99 | $31,436,802 | Consumer Discretionary | large | unknown | 2026-09-13 |
| BA | $210.48 | $45,070,842 | Industrials | large | unknown | 2026-09-13 |
| BAC | $62.69 | $115,689,243 | Financials | large | unknown | 2026-09-13 |
| BKNG | $173.94 | $50,311,456 | Consumer Discretionary | large | unknown | 2026-09-13 |
| BKR | $59.05 | $25,489,447 | Energy | large | unknown | 2026-09-13 |
| BLK | $1080.15 | $34,906,400 | Financials | large | unknown | 2026-09-13 |
| BMY | $63.62 | $28,961,294 | Health Care | large | unknown | 2026-09-13 |
| BRK.B | $510.25 | $50,882,643 | Financials | large | unknown | 2026-09-13 |
| BSX | $42.95 | $80,005,482 | Health Care | large | unknown | 2026-09-13 |
| BURL | $239.21 | $32,704,013 | Consumer Discretionary | mid | unknown | 2026-09-13 |
| C | $138.78 | $36,432,228 | Financials | large | unknown | 2026-09-13 |
| CAT | $818.57 | $75,826,842 | Industrials | large | unknown | 2026-09-13 |
| CB | $338.44 | $23,417,123 | Financials | large | unknown | 2026-09-13 |
| CCL | $22.74 | $28,108,998 | Consumer Discretionary | large | unknown | 2026-09-13 |
| CDE | $20.59 | $23,018,580 | Materials | mid | unknown | 2026-09-13 |
| CDNS | $289.41 | $41,787,586 | Information Technology | large | unknown | 2026-09-13 |
| CEG | $284.76 | $23,777,593 | Utilities | large | unknown | 2026-09-13 |
| CHTR | $145.82 | $23,364,866 | Communication Services | large | unknown | 2026-09-13 |
| CIEN | $349.29 | $42,291,546 | Information Technology | large | unknown | 2026-09-13 |
| CMCSA | $25.19 | $34,374,105 | Communication Services | large | unknown | 2026-09-13 |
| CME | $275.73 | $21,967,467 | Financials | large | unknown | 2026-09-13 |
| CMG | $36.20 | $36,190,630 | Consumer Discretionary | large | unknown | 2026-09-13 |
| CMI | $556.38 | $30,015,881 | Industrials | large | unknown | 2026-09-13 |
| COF | $208.39 | $26,756,585 | Financials | large | unknown | 2026-09-13 |
| COIN | $175.31 | $45,295,915 | Financials | large | unknown | 2026-09-13 |
| COP | $137.41 | $41,125,863 | Energy | large | unknown | 2026-09-13 |
| COR | $321.65 | $20,646,088 | Health Care | large | unknown | 2026-09-13 |
| COST | $904.83 | $50,375,891 | Consumer Staples | large | unknown | 2026-09-13 |
| CPRT | $29.94 | $24,805,164 | Industrials | large | unknown | 2026-09-13 |
| CRH | $88.55 | $20,489,444 | Materials | large | unknown | 2026-09-13 |
| CRM | $247.70 | $150,746,392 | Information Technology | large | unknown | 2026-09-13 |
| CRWD | $206.72 | $70,193,648 | Information Technology | large | unknown | 2026-09-13 |
| CSCO | $112.19 | $64,085,343 | Information Technology | large | unknown | 2026-09-13 |
| CSX | $48.95 | $29,411,633 | Industrials | large | unknown | 2026-09-13 |
| CTVA | $83.78 | $21,565,133 | Materials | large | unknown | 2026-09-13 |
| CVNA | $69.15 | $25,859,548 | Consumer Discretionary | large | unknown | 2026-09-13 |
| CVS | $94.67 | $31,955,882 | Health Care | large | unknown | 2026-09-13 |
| CVX | $214.06 | $54,827,947 | Energy | large | unknown | 2026-09-13 |
| D | $64.52 | $21,167,170 | Utilities | large | unknown | 2026-09-13 |
| DASH | $202.00 | $44,513,733 | Consumer Discretionary | large | unknown | 2026-09-13 |
| DDOG | $221.16 | $37,484,214 | Information Technology | large | unknown | 2026-09-13 |
| DE | $676.03 | $51,273,815 | Industrials | large | unknown | 2026-09-13 |
| DELL | $567.13 | $124,268,824 | Information Technology | large | unknown | 2026-09-13 |
| DHR | $200.04 | $37,604,146 | Health Care | large | unknown | 2026-09-13 |
| DIS | $106.56 | $35,060,177 | Communication Services | large | unknown | 2026-09-13 |
| DKS | $134.97 | $28,848,192 | Consumer Discretionary | mid | unknown | 2026-09-13 |
| DVN | $50.24 | $35,856,865 | Energy | large | unknown | 2026-09-13 |
| EBAY | $107.71 | $20,675,740 | Consumer Discretionary | large | unknown | 2026-09-13 |
| ECL | $276.23 | $26,894,969 | Materials | large | unknown | 2026-09-13 |
| EQIX | $1037.46 | $30,668,490 | Real Estate | large | unknown | 2026-09-13 |
| EQT | $54.07 | $26,317,031 | Energy | large | unknown | 2026-09-13 |
| ETN | $425.52 | $36,821,855 | Industrials | large | unknown | 2026-09-13 |
| EXPE | $280.87 | $28,276,142 | Consumer Discretionary | large | unknown | 2026-09-13 |
| F | $13.97 | $25,091,931 | Consumer Discretionary | large | unknown | 2026-09-13 |
| FCX | $71.12 | $56,078,159 | Materials | large | unknown | 2026-09-13 |
| FDX | $311.93 | $41,459,689 | Industrials | large | unknown | 2026-09-13 |
| FICO | $985.87 | $25,789,314 | Information Technology | large | unknown | 2026-09-13 |
| FIX | $1688.80 | $32,101,642 | Industrials | large | unknown | 2026-09-13 |
| FN | $414.89 | $27,123,016 | Information Technology | mid | unknown | 2026-09-13 |
| FTNT | $156.12 | $26,287,529 | Information Technology | large | unknown | 2026-09-13 |
| GE | $323.65 | $51,978,224 | Industrials | large | unknown | 2026-09-13 |
| GEV | $956.90 | $87,241,036 | Industrials | large | unknown | 2026-09-13 |
| GILD | $143.76 | $24,079,924 | Health Care | large | unknown | 2026-09-13 |
| GIS | $35.84 | $21,523,532 | Consumer Staples | large | unknown | 2026-09-13 |
| GLW | $166.39 | $49,300,758 | Information Technology | large | unknown | 2026-09-13 |
| GOOG | $335.38 | $200,522,569 | Communication Services | large | unknown | 2026-09-13 |
| GOOGL | $338.44 | $235,225,814 | Communication Services | large | unknown | 2026-09-13 |
| GS | $1028.89 | $60,177,143 | Financials | large | unknown | 2026-09-13 |
| HAL | $35.83 | $25,030,123 | Energy | large | unknown | 2026-09-13 |
| HCA | $426.95 | $28,669,497 | Health Care | large | unknown | 2026-09-13 |
| HD | $308.75 | $45,372,000 | Consumer Discretionary | large | unknown | 2026-09-13 |
| HL | $19.78 | $22,053,690 | Materials | mid | unknown | 2026-09-13 |
| HLT | $306.10 | $27,740,082 | Consumer Discretionary | large | unknown | 2026-09-13 |
| HOOD | $112.59 | $75,931,891 | Financials | large | unknown | 2026-09-13 |
| HPE | $62.08 | $61,304,871 | Information Technology | large | unknown | 2026-09-13 |
| HPQ | $35.48 | $37,355,413 | Information Technology | large | unknown | 2026-09-13 |
| HUM | $409.86 | $20,070,830 | Health Care | large | unknown | 2026-09-13 |
| HWM | $229.59 | $45,597,820 | Industrials | large | unknown | 2026-09-13 |
| IBM | $243.36 | $40,831,602 | Information Technology | large | unknown | 2026-09-13 |
| ICE | $157.44 | $24,436,512 | Financials | large | unknown | 2026-09-13 |
| ILMN | $206.44 | $26,735,162 | Health Care | mid | unknown | 2026-09-13 |
| INTC | $102.92 | $280,182,989 | Information Technology | large | unknown | 2026-09-13 |
| INTU | $321.58 | $66,837,624 | Information Technology | large | unknown | 2026-09-13 |
| IQV | $262.02 | $21,075,608 | Health Care | large | unknown | 2026-09-13 |
| ISRG | $369.24 | $37,624,982 | Health Care | large | unknown | 2026-09-13 |
| JCI | $146.01 | $20,963,507 | Industrials | large | unknown | 2026-09-13 |
| JNJ | $265.69 | $59,851,548 | Health Care | large | unknown | 2026-09-13 |
| JPM | $356.43 | $60,667,056 | Financials | large | unknown | 2026-09-13 |
| KEYS | $338.99 | $24,855,503 | Information Technology | large | unknown | 2026-09-13 |
| KHC | $24.61 | $24,678,884 | Consumer Staples | large | unknown | 2026-09-13 |
| KKR | $101.14 | $24,958,513 | Financials | large | unknown | 2026-09-13 |
| KLAC | $180.67 | $56,466,036 | Information Technology | large | unknown | 2026-09-13 |
| KMI | $30.86 | $26,012,162 | Energy | large | unknown | 2026-09-13 |
| KO | $88.26 | $68,284,764 | Consumer Staples | large | unknown | 2026-09-13 |
| KR | $58.46 | $23,592,308 | Consumer Staples | large | unknown | 2026-09-13 |
| KVUE | $17.76 | $31,708,057 | Consumer Staples | large | unknown | 2026-09-13 |
| LHX | $245.60 | $20,091,550 | Industrials | large | unknown | 2026-09-13 |
| LIN | $466.26 | $35,389,000 | Materials | large | unknown | 2026-09-13 |
| LLY | $1114.83 | $118,120,951 | Health Care | large | unknown | 2026-09-13 |
| LMT | $524.31 | $20,149,269 | Industrials | large | unknown | 2026-09-13 |
| LOW | $196.87 | $32,380,401 | Consumer Discretionary | large | unknown | 2026-09-13 |
| LRCX | $298.17 | $96,368,361 | Information Technology | large | unknown | 2026-09-13 |
| LULU | $98.97 | $21,470,989 | Consumer Discretionary | large | unknown | 2026-09-13 |
| MA | $569.44 | $65,810,033 | Financials | large | unknown | 2026-09-13 |
| MAR | $334.79 | $22,017,073 | Consumer Discretionary | large | unknown | 2026-09-13 |
| MCD | $252.56 | $39,947,852 | Consumer Discretionary | large | unknown | 2026-09-13 |
| MCHP | $74.21 | $21,753,589 | Information Technology | large | unknown | 2026-09-13 |
| MCK | $881.42 | $32,926,254 | Health Care | large | unknown | 2026-09-13 |
| MDLZ | $62.42 | $29,839,239 | Consumer Staples | large | unknown | 2026-09-13 |
| MDT | $90.96 | $42,574,623 | Health Care | large | unknown | 2026-09-13 |
| META | $647.97 | $368,489,568 | Communication Services | large | unknown | 2026-09-13 |
| MKSI | $267.26 | $21,073,100 | Information Technology | mid | unknown | 2026-09-13 |
| MLM | $510.06 | $34,409,579 | Materials | large | unknown | 2026-09-13 |
| MMM | $164.93 | $20,626,881 | Industrials | large | unknown | 2026-09-13 |
| MNST | $43.37 | $21,367,599 | Consumer Staples | large | unknown | 2026-09-13 |
| MO | $68.97 | $32,605,987 | Consumer Staples | large | unknown | 2026-09-13 |
| MPC | $395.96 | $40,812,656 | Energy | large | unknown | 2026-09-13 |
| MPWR | $1233.98 | $34,848,611 | Information Technology | large | unknown | 2026-09-13 |
| MRK | $143.91 | $61,365,736 | Health Care | large | unknown | 2026-09-13 |
| MRNA | $143.97 | $109,416,002 | Health Care | large | unknown | 2026-09-13 |
| MS | $214.46 | $33,272,977 | Financials | large | unknown | 2026-09-13 |
| MSFT | $495.58 | $272,737,088 | Information Technology | large | unknown | 2026-09-13 |
| MSI | $466.37 | $31,422,947 | Information Technology | large | unknown | 2026-09-13 |
| MTZ | $240.47 | $26,606,632 | Industrials | mid | unknown | 2026-09-13 |
| MU | $975.12 | $566,198,993 | Information Technology | large | unknown | 2026-09-13 |
| NEE | $82.31 | $49,792,490 | Utilities | large | unknown | 2026-09-13 |
| NEM | $126.86 | $35,150,054 | Materials | large | unknown | 2026-09-13 |
| NFLX | $77.39 | $111,810,733 | Communication Services | large | unknown | 2026-09-13 |
| NKE | $36.81 | $49,120,980 | Consumer Discretionary | large | unknown | 2026-09-13 |
| NOW | $132.55 | $87,157,449 | Information Technology | large | unknown | 2026-09-13 |
| NTAP | $199.33 | $24,113,208 | Information Technology | large | unknown | 2026-09-13 |
| NVDA | $218.17 | $766,978,033 | Information Technology | large | unknown | 2026-09-13 |
| NXPI | $236.77 | $26,254,656 | Information Technology | large | unknown | 2026-09-13 |
| OKTA | $166.53 | $28,707,139 | Information Technology | mid | unknown | 2026-09-13 |
| ON | $76.15 | $23,624,381 | Information Technology | large | unknown | 2026-09-13 |
| ORCL | $150.30 | $115,836,319 | Information Technology | large | unknown | 2026-09-13 |
| OXY | $61.45 | $29,526,250 | Energy | large | unknown | 2026-09-13 |
| PANW | $330.60 | $77,007,925 | Information Technology | large | unknown | 2026-09-13 |
| PATH | $13.75 | $28,504,779 | Information Technology | mid | unknown | 2026-09-13 |
| PCG | $13.78 | $58,360,428 | Utilities | large | unknown | 2026-09-13 |
| PEP | $136.28 | $28,626,532 | Consumer Staples | large | unknown | 2026-09-13 |
| PFE | $27.69 | $51,571,341 | Health Care | large | unknown | 2026-09-13 |
| PG | $145.27 | $62,177,663 | Consumer Staples | large | unknown | 2026-09-13 |
| PGR | $217.66 | $29,061,551 | Financials | large | unknown | 2026-09-13 |
| PH | $950.40 | $26,262,611 | Industrials | large | unknown | 2026-09-13 |
| PLTR | $167.25 | $138,329,523 | Information Technology | large | unknown | 2026-09-13 |
| PM | $191.09 | $34,161,230 | Consumer Staples | large | unknown | 2026-09-13 |
| PSX | $259.54 | $31,125,099 | Energy | large | unknown | 2026-09-13 |
| PWR | $650.79 | $41,542,618 | Industrials | large | unknown | 2026-09-13 |
| PYPL | $53.70 | $34,784,019 | Financials | large | unknown | 2026-09-13 |
| QCOM | $181.95 | $52,793,419 | Information Technology | large | unknown | 2026-09-13 |
| RCL | $260.19 | $31,481,159 | Consumer Discretionary | large | unknown | 2026-09-13 |
| ROST | $230.67 | $35,414,921 | Consumer Discretionary | large | unknown | 2026-09-13 |
| RTX | $197.72 | $29,834,939 | Industrials | large | unknown | 2026-09-13 |
| SBUX | $98.74 | $22,295,156 | Consumer Discretionary | large | unknown | 2026-09-13 |
| SCHW | $107.24 | $44,673,776 | Financials | large | unknown | 2026-09-13 |
| SLB | $56.05 | $38,142,463 | Energy | large | unknown | 2026-09-13 |
| SMCI | $40.09 | $62,707,804 | Information Technology | large | unknown | 2026-09-13 |
| SMTC | $167.32 | $29,182,979 | Information Technology | mid | unknown | 2026-09-13 |
| SNDK | $1632.99 | $430,413,492 | Information Technology | large | unknown | 2026-09-13 |
| SNPS | $397.46 | $34,761,478 | Information Technology | large | unknown | 2026-09-13 |
| SO | $87.20 | $26,369,423 | Utilities | large | unknown | 2026-09-13 |
| SPGI | $410.78 | $39,186,145 | Financials | large | unknown | 2026-09-13 |
| STX | $830.41 | $123,618,194 | Information Technology | large | unknown | 2026-09-13 |
| SWKS | $88.38 | $23,391,432 | Information Technology | large | unknown | 2026-09-13 |
| SYK | $275.44 | $45,335,804 | Health Care | large | unknown | 2026-09-13 |
| T | $26.05 | $46,361,054 | Communication Services | large | unknown | 2026-09-13 |
| TDG | $1139.93 | $25,282,383 | Industrials | large | unknown | 2026-09-13 |
| TEL | $211.93 | $30,617,172 | Information Technology | large | unknown | 2026-09-13 |
| TER | $379.78 | $34,878,058 | Information Technology | large | unknown | 2026-09-13 |
| TGT | $155.81 | $32,995,768 | Consumer Staples | large | unknown | 2026-09-13 |
| TJX | $126.05 | $52,160,630 | Consumer Discretionary | large | unknown | 2026-09-13 |
| TMO | $610.03 | $56,576,303 | Health Care | large | unknown | 2026-09-13 |
| TMUS | $182.43 | $29,174,463 | Communication Services | large | unknown | 2026-09-13 |
| TOST | $32.11 | $20,724,798 | Financials | mid | unknown | 2026-09-13 |
| TPR | $118.51 | $21,145,211 | Consumer Discretionary | large | unknown | 2026-09-13 |
| TRGP | $290.25 | $23,058,155 | Energy | large | unknown | 2026-09-13 |
| TRV | $375.21 | $22,497,130 | Financials | large | unknown | 2026-09-13 |
| TSCO | $33.02 | $21,630,596 | Consumer Discretionary | large | unknown | 2026-09-13 |
| TSLA | $365.49 | $276,015,425 | Consumer Discretionary | large | unknown | 2026-09-13 |
| TTWO | $215.38 | $27,570,835 | Communication Services | large | unknown | 2026-09-13 |
| TWLO | $227.35 | $22,494,123 | Information Technology | mid | unknown | 2026-09-13 |
| TXN | $268.72 | $53,981,966 | Information Technology | large | unknown | 2026-09-13 |
| UBER | $71.65 | $59,900,575 | Industrials | large | unknown | 2026-09-13 |
| ULTA | $546.88 | $21,577,231 | Consumer Discretionary | large | unknown | 2026-09-13 |
| UNH | $378.87 | $70,029,345 | Health Care | large | unknown | 2026-09-13 |
| UNP | $284.40 | $36,656,442 | Industrials | large | unknown | 2026-09-13 |
| URI | $987.97 | $26,300,468 | Industrials | large | unknown | 2026-09-13 |
| USB | $62.83 | $23,422,633 | Financials | large | unknown | 2026-09-13 |
| V | $370.47 | $80,214,264 | Financials | large | unknown | 2026-09-13 |
| VLO | $390.53 | $35,864,071 | Energy | large | unknown | 2026-09-13 |
| VRTX | $515.65 | $25,167,713 | Health Care | large | unknown | 2026-09-13 |
| VST | $148.45 | $24,060,893 | Utilities | large | unknown | 2026-09-13 |
| VZ | $50.59 | $47,409,918 | Communication Services | large | unknown | 2026-09-13 |
| WBD | $28.05 | $38,118,754 | Communication Services | large | unknown | 2026-09-13 |
| WDAY | $185.62 | $40,890,495 | Information Technology | large | unknown | 2026-09-13 |
| WDC | $447.01 | $112,307,532 | Information Technology | large | unknown | 2026-09-13 |
| WELL | $235.57 | $21,288,633 | Real Estate | large | unknown | 2026-09-13 |
| WFC | $90.28 | $51,312,396 | Financials | large | unknown | 2026-09-13 |
| WM | $213.53 | $21,246,518 | Industrials | large | unknown | 2026-09-13 |
| WMB | $72.84 | $25,579,078 | Energy | large | unknown | 2026-09-13 |
| WMT | $107.12 | $109,534,034 | Consumer Staples | large | unknown | 2026-09-13 |
| XEL | $75.49 | $22,029,736 | Utilities | large | unknown | 2026-09-13 |
| XOM | $165.99 | $65,241,887 | Energy | large | unknown | 2026-09-13 |
