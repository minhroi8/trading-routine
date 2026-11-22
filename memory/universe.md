---
screened_on: 2026-11-22
expires_on: 2026-11-29
total_passed: 338
total_rejected: 1193
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
| A | $170.31 | 24,493,140 | Unknown | large | unknown | 2026-11-22 |
| AAL | $11.92 | 30,053,817 | Industrials | mid | unknown | 2026-11-22 |
| AAPL | $343.40 | 526,766,460 | Information Technology | large | unknown | 2026-11-22 |
| ABBV | $286.42 | 67,243,370 | Health Care | large | unknown | 2026-11-22 |
| ABNB | $170.41 | 43,778,887 | Consumer Discretionary | large | unknown | 2026-11-22 |
| ABT | $103.18 | 50,939,211 | Health Care | large | unknown | 2026-11-22 |
| ACN | $221.19 | 64,839,828 | Information Technology | large | unknown | 2026-11-22 |
| ADBE | $217.81 | 36,788,415 | Information Technology | large | unknown | 2026-11-22 |
| ADI | $346.55 | 76,659,422 | Information Technology | large | unknown | 2026-11-22 |
| ADP | $302.03 | 29,253,656 | Industrials | large | unknown | 2026-11-22 |
| ADSK | $244.56 | 29,885,124 | Information Technology | large | unknown | 2026-11-22 |
| AEP | $125.17 | 25,012,558 | Utilities | large | unknown | 2026-11-22 |
| AJG | $279.21 | 33,218,833 | Financials | large | unknown | 2026-11-22 |
| AKAM | $85.06 | 30,748,549 | Information Technology | large | unknown | 2026-11-22 |
| ALL | $267.14 | 27,255,451 | Unknown | large | unknown | 2026-11-22 |
| AMAT | $302.14 | 116,448,143 | Information Technology | large | unknown | 2026-11-22 |
| AMD | $424.30 | 587,837,926 | Information Technology | large | unknown | 2026-11-22 |
| AME | $222.86 | 24,243,255 | Industrials | large | unknown | 2026-11-22 |
| AMGN | $436.05 | 42,595,002 | Health Care | large | unknown | 2026-11-22 |
| AMT | $183.96 | 27,632,362 | Real Estate | large | unknown | 2026-11-22 |
| AMZN | $247.12 | 535,900,045 | Consumer Discretionary | large | unknown | 2026-11-22 |
| ANET | $167.47 | 94,440,114 | Information Technology | large | unknown | 2026-11-22 |
| AON | $332.74 | 27,220,465 | Financials | large | unknown | 2026-11-22 |
| APH | $69.73 | 82,295,459 | Information Technology | large | unknown | 2026-11-22 |
| APO | $111.11 | 24,722,132 | Financials | large | unknown | 2026-11-22 |
| APP | $348.47 | 79,893,920 | Unknown | large | unknown | 2026-11-22 |
| ATI | $165.81 | 22,830,203 | Materials | mid | unknown | 2026-11-22 |
| AVGO | $304.25 | 352,978,377 | Information Technology | large | unknown | 2026-11-22 |
| AWK | $149.54 | 22,344,426 | Utilities | large | unknown | 2026-11-22 |
| AXON | $291.50 | 30,602,586 | Industrials | large | unknown | 2026-11-22 |
| AXP | $301.76 | 46,762,532 | Unknown | large | unknown | 2026-11-22 |
| AZO | $3256.39 | 36,346,330 | Consumer Discretionary | large | unknown | 2026-11-22 |
| BA | $155.94 | 80,539,576 | Industrials | large | unknown | 2026-11-22 |
| BAC | $47.07 | 128,450,204 | Financials | large | unknown | 2026-11-22 |
| BDX | $212.33 | 27,824,811 | Health Care | large | unknown | 2026-11-22 |
| BE | $142.41 | 102,763,074 | Unknown | large | unknown | 2026-11-22 |
| BKNG | $144.99 | 61,134,768 | Consumer Discretionary | large | unknown | 2026-11-22 |
| BKR | $44.83 | 30,600,256 | Unknown | large | unknown | 2026-11-22 |
| BLK | $1102.02 | 45,855,043 | Unknown | large | unknown | 2026-11-22 |
| BMY | $58.83 | 31,167,219 | Health Care | large | unknown | 2026-11-22 |
| BNY | $141.28 | 22,429,707 | Unknown | large | unknown | 2026-11-22 |
| BRK.B | $569.92 | 99,728,218 | Financials | large | unknown | 2026-11-22 |
| BSX | $42.00 | 83,982,394 | Health Care | large | unknown | 2026-11-22 |
| BURL | $245.43 | 25,429,452 | Unknown | mid | unknown | 2026-11-22 |
| BX | $110.82 | 29,758,698 | Financials | large | unknown | 2026-11-22 |
| C | $110.67 | 47,072,149 | Financials | large | unknown | 2026-11-22 |
| CAH | $272.85 | 24,578,877 | Unknown | large | unknown | 2026-11-22 |
| CARR | $49.97 | 23,428,101 | Unknown | large | unknown | 2026-11-22 |
| CART | $57.33 | 27,551,284 | Unknown | mid | unknown | 2026-11-22 |
| CAT | $510.44 | 122,737,865 | Industrials | large | unknown | 2026-11-22 |
| CB | $371.59 | 32,233,583 | Financials | large | unknown | 2026-11-22 |
| CBOE | $357.75 | 24,742,275 | Unknown | large | unknown | 2026-11-22 |
| CCI | $82.44 | 24,776,710 | Unknown | large | unknown | 2026-11-22 |
| CCL | $26.59 | 36,209,563 | Unknown | large | unknown | 2026-11-22 |
| CDE | $10.68 | 23,965,195 | Unknown | mid | unknown | 2026-11-22 |
| CDNS | $281.50 | 40,256,928 | Unknown | large | unknown | 2026-11-22 |
| CEG | $237.49 | 48,132,803 | Unknown | large | unknown | 2026-11-22 |
| CHTR | $128.81 | 20,025,445 | Unknown | large | unknown | 2026-11-22 |
| CI | $270.85 | 29,287,809 | Health Care | large | unknown | 2026-11-22 |
| CIEN | $234.45 | 52,660,589 | Unknown | large | unknown | 2026-11-22 |
| CL | $98.72 | 32,544,520 | Consumer Staples | large | unknown | 2026-11-22 |
| CMCSA | $24.92 | 46,864,977 | Unknown | large | unknown | 2026-11-22 |
| CME | $307.67 | 29,920,938 | Financials | large | unknown | 2026-11-22 |
| CMG | $35.59 | 44,475,886 | Consumer Discretionary | large | unknown | 2026-11-22 |
| CMI | $404.10 | 41,339,764 | Industrials | large | unknown | 2026-11-22 |
| CNC | $63.80 | 27,030,206 | Unknown | large | unknown | 2026-11-22 |
| CNP | $39.12 | 34,766,677 | Unknown | large | unknown | 2026-11-22 |
| COF | $178.65 | 44,272,496 | Financials | large | unknown | 2026-11-22 |
| COHR | $187.27 | 99,169,742 | Unknown | large | unknown | 2026-11-22 |
| COIN | $102.00 | 38,282,938 | Unknown | large | unknown | 2026-11-22 |
| COP | $136.21 | 49,245,027 | Energy | large | unknown | 2026-11-22 |
| COR | $339.23 | 29,132,602 | Unknown | large | unknown | 2026-11-22 |
| COST | $1104.36 | 105,769,047 | Consumer Staples | large | unknown | 2026-11-22 |
| CPRT | $31.12 | 24,274,683 | Industrials | large | unknown | 2026-11-22 |
| CRH | $88.06 | 26,707,939 | Unknown | large | unknown | 2026-11-22 |
| CRL | $314.42 | 26,938,438 | Health Care | large | unknown | 2026-11-22 |
| CRM | $180.66 | 74,610,845 | Information Technology | large | unknown | 2026-11-22 |
| CRS | $254.07 | 26,937,505 | Materials | mid | unknown | 2026-11-22 |
| CRWD | $229.53 | 83,965,199 | Information Technology | large | unknown | 2026-11-22 |
| CSCO | $90.69 | 82,785,544 | Information Technology | large | unknown | 2026-11-22 |
| CSX | $49.13 | 46,590,339 | Industrials | large | unknown | 2026-11-22 |
| CTAS | $219.81 | 23,752,212 | Industrials | large | unknown | 2026-11-22 |
| CTSH | $58.07 | 21,386,275 | Information Technology | large | unknown | 2026-11-22 |
| CVNA | $63.88 | 45,468,190 | Unknown | large | unknown | 2026-11-22 |
| CVS | $80.86 | 70,023,838 | Health Care | large | unknown | 2026-11-22 |
| CVX | $208.44 | 57,154,266 | Energy | large | unknown | 2026-11-22 |
| D | $66.29 | 29,070,763 | Utilities | large | unknown | 2026-11-22 |
| DAL | $80.01 | 25,362,835 | Industrials | large | unknown | 2026-11-22 |
| DASH | $152.56 | 71,001,995 | Unknown | large | unknown | 2026-11-22 |
| DDOG | $157.51 | 51,246,997 | Unknown | large | unknown | 2026-11-22 |
| DE | $609.28 | 51,755,833 | Industrials | large | unknown | 2026-11-22 |
| DELL | $277.89 | 123,706,032 | Information Technology | large | unknown | 2026-11-22 |
| DHI | $145.49 | 24,600,851 | Consumer Discretionary | large | unknown | 2026-11-22 |
| DHR | $220.69 | 45,722,948 | Health Care | large | unknown | 2026-11-22 |
| DIS | $117.97 | 60,432,947 | Communication Services | large | unknown | 2026-11-22 |
| DLR | $162.65 | 31,936,106 | Unknown | large | unknown | 2026-11-22 |
| DOCN | $66.78 | 20,811,431 | Unknown | mid | unknown | 2026-11-22 |
| DT | $43.49 | 26,510,716 | Unknown | mid | unknown | 2026-11-22 |
| DUK | $129.82 | 34,561,704 | Utilities | large | unknown | 2026-11-22 |
| DVN | $41.55 | 45,401,377 | Energy | large | unknown | 2026-11-22 |
| EAT | $186.91 | 21,970,258 | Consumer Discretionary | mid | unknown | 2026-11-22 |
| EBAY | $115.65 | 29,514,726 | Consumer Discretionary | large | unknown | 2026-11-22 |
| ECHO | $84.30 | 23,535,019 | Unknown | large | unknown | 2026-11-22 |
| ECL | $294.77 | 31,176,983 | Materials | large | unknown | 2026-11-22 |
| EL | $99.46 | 25,537,488 | Consumer Staples | large | unknown | 2026-11-22 |
| ELV | $394.85 | 36,798,054 | Unknown | large | unknown | 2026-11-22 |
| EMR | $150.97 | 25,449,328 | Industrials | large | unknown | 2026-11-22 |
| ENTG | $124.53 | 24,423,221 | Unknown | mid | unknown | 2026-11-22 |
| EOG | $148.68 | 31,633,897 | Energy | large | unknown | 2026-11-22 |
| EQIX | $968.45 | 49,259,032 | Real Estate | large | unknown | 2026-11-22 |
| EQT | $48.90 | 39,932,721 | Unknown | large | unknown | 2026-11-22 |
| ETN | $311.45 | 70,285,079 | Industrials | large | unknown | 2026-11-22 |
| EW | $101.88 | 32,404,415 | Health Care | large | unknown | 2026-11-22 |
| EXC | $45.71 | 31,115,058 | Utilities | large | unknown | 2026-11-22 |
| EXPE | $235.03 | 34,503,336 | Consumer Discretionary | large | unknown | 2026-11-22 |
| F | $11.17 | 25,862,868 | Consumer Discretionary | large | unknown | 2026-11-22 |
| FANG | $175.77 | 30,248,824 | Unknown | large | unknown | 2026-11-22 |
| FAST | $50.64 | 21,693,546 | Industrials | large | unknown | 2026-11-22 |
| FCX | $46.00 | 52,423,295 | Materials | large | unknown | 2026-11-22 |
| FDX | $304.00 | 37,625,630 | Industrials | large | unknown | 2026-11-22 |
| FERG | $240.60 | 22,984,177 | Unknown | large | unknown | 2026-11-22 |
| FFIV | $303.89 | 21,048,096 | Information Technology | large | unknown | 2026-11-22 |
| FICO | $694.88 | 29,189,966 | Information Technology | large | unknown | 2026-11-22 |
| FIS | $25.83 | 24,998,026 | Financials | large | unknown | 2026-11-22 |
| FISV | $55.93 | 44,712,324 | Unknown | large | unknown | 2026-11-22 |
| FITB | $49.41 | 29,612,037 | Financials | large | unknown | 2026-11-22 |
| FIX | $1043.22 | 55,303,037 | Unknown | large | unknown | 2026-11-22 |
| FLEX | $66.26 | 26,594,537 | Unknown | large | unknown | 2026-11-22 |
| FN | $284.50 | 30,131,618 | Unknown | mid | unknown | 2026-11-22 |
| FOXA | $62.96 | 29,263,464 | Communication Services | large | unknown | 2026-11-22 |
| FSLR | $137.62 | 27,825,636 | Unknown | large | unknown | 2026-11-22 |
| FTNT | $124.51 | 38,208,824 | Information Technology | large | unknown | 2026-11-22 |
| GD | $341.71 | 21,697,442 | Industrials | large | unknown | 2026-11-22 |
| GE | $309.72 | 89,317,708 | Industrials | large | unknown | 2026-11-22 |
| GEV | $699.26 | 169,696,398 | Industrials | large | unknown | 2026-11-22 |
| GILD | $166.43 | 48,169,050 | Health Care | large | unknown | 2026-11-22 |
| GIS | $35.74 | 20,376,965 | Consumer Staples | large | unknown | 2026-11-22 |
| GKOS | $237.29 | 24,632,098 | Health Care | mid | unknown | 2026-11-22 |
| GLW | $94.42 | 65,902,625 | Information Technology | large | unknown | 2026-11-22 |
| GM | $78.74 | 29,107,804 | Consumer Discretionary | large | unknown | 2026-11-22 |
| GOOG | $264.14 | 268,440,475 | Communication Services | large | unknown | 2026-11-22 |
| GOOGL | $265.62 | 478,429,769 | Communication Services | large | unknown | 2026-11-22 |
| GPN | $91.80 | 24,301,413 | Unknown | large | unknown | 2026-11-22 |
| GS | $790.82 | 84,119,324 | Financials | large | unknown | 2026-11-22 |
| GWW | $1359.39 | 27,140,017 | Industrials | large | unknown | 2026-11-22 |
| HAL | $30.52 | 21,545,105 | Energy | large | unknown | 2026-11-22 |
| HCA | $475.41 | 43,195,515 | Health Care | large | unknown | 2026-11-22 |
| HD | $339.27 | 78,000,427 | Consumer Discretionary | large | unknown | 2026-11-22 |
| HLT | $356.45 | 47,033,037 | Consumer Discretionary | large | unknown | 2026-11-22 |
| HON | $212.76 | 23,645,618 | Industrials | large | unknown | 2026-11-22 |
| HONA | $150.78 | 26,003,717 | Unknown | large | unknown | 2026-11-22 |
| HOOD | $62.18 | 57,813,371 | Unknown | large | unknown | 2026-11-22 |
| HPE | $40.92 | 45,618,765 | Information Technology | large | unknown | 2026-11-22 |
| HPQ | $27.97 | 30,238,966 | Information Technology | large | unknown | 2026-11-22 |
| HSY | $175.57 | 23,288,735 | Consumer Staples | large | unknown | 2026-11-22 |
| HUBB | $403.38 | 22,569,658 | Industrials | large | unknown | 2026-11-22 |
| HUBS | $193.97 | 20,823,229 | Unknown | mid | unknown | 2026-11-22 |
| HUM | $389.91 | 51,595,845 | Health Care | large | unknown | 2026-11-22 |
| HWM | $209.24 | 51,975,357 | Industrials | large | unknown | 2026-11-22 |
| IBKR | $71.25 | 23,321,789 | Unknown | large | unknown | 2026-11-22 |
| IBM | $224.50 | 35,399,476 | Information Technology | large | unknown | 2026-11-22 |
| ICE | $170.12 | 36,645,768 | Financials | large | unknown | 2026-11-22 |
| IDXX | $675.99 | 25,315,854 | Health Care | large | unknown | 2026-11-22 |
| ILMN | $193.05 | 34,667,353 | Health Care | large | unknown | 2026-11-22 |
| INTC | $51.37 | 305,222,999 | Information Technology | large | unknown | 2026-11-22 |
| INTU | $270.29 | 55,192,138 | Information Technology | large | unknown | 2026-11-22 |
| IQV | $245.97 | 27,646,615 | Health Care | large | unknown | 2026-11-22 |
| ISRG | $399.50 | 60,659,061 | Health Care | large | unknown | 2026-11-22 |
| ITW | $273.58 | 20,311,380 | Industrials | large | unknown | 2026-11-22 |
| JCI | $130.28 | 47,036,218 | Industrials | large | unknown | 2026-11-22 |
| JHX | $26.48 | 27,318,105 | Unknown | mid | unknown | 2026-11-22 |
| JNJ | $270.83 | 86,640,460 | Health Care | large | unknown | 2026-11-22 |
| JPM | $310.75 | 79,986,448 | Financials | large | unknown | 2026-11-22 |
| KDP | $34.85 | 65,754,484 | Consumer Staples | large | unknown | 2026-11-22 |
| KEYS | $261.96 | 28,328,850 | Information Technology | large | unknown | 2026-11-22 |
| KHC | $25.40 | 24,680,523 | Consumer Staples | large | unknown | 2026-11-22 |
| KKR | $88.51 | 21,525,187 | Unknown | large | unknown | 2026-11-22 |
| KLAC | $127.21 | 83,852,277 | Information Technology | large | unknown | 2026-11-22 |
| KMB | $106.39 | 36,402,308 | Consumer Staples | large | unknown | 2026-11-22 |
| KMI | $30.40 | 33,704,877 | Energy | large | unknown | 2026-11-22 |
| KO | $97.00 | 115,603,376 | Consumer Staples | large | unknown | 2026-11-22 |
| KR | $68.45 | 22,395,964 | Consumer Staples | large | unknown | 2026-11-22 |
| LHX | $249.70 | 27,338,440 | Industrials | large | unknown | 2026-11-22 |
| LIN | $502.87 | 51,686,124 | Materials | large | unknown | 2026-11-22 |
| LITE | $461.30 | 172,426,353 | Unknown | large | unknown | 2026-11-22 |
| LLY | $1348.20 | 192,522,052 | Health Care | large | unknown | 2026-11-22 |
| LMT | $565.52 | 40,220,230 | Industrials | large | unknown | 2026-11-22 |
| LOW | $220.88 | 39,491,903 | Consumer Discretionary | large | unknown | 2026-11-22 |
| LRCX | $183.60 | 123,512,341 | Information Technology | large | unknown | 2026-11-22 |
| LSCC | $98.22 | 21,368,870 | Unknown | mid | unknown | 2026-11-22 |
| LYV | $174.83 | 25,694,145 | Communication Services | large | unknown | 2026-11-22 |
| MA | $626.15 | 136,689,315 | Financials | large | unknown | 2026-11-22 |
| MAR | $406.64 | 36,313,477 | Unknown | large | unknown | 2026-11-22 |
| MCD | $273.42 | 63,888,104 | Consumer Discretionary | large | unknown | 2026-11-22 |
| MCHP | $55.42 | 46,692,030 | Information Technology | large | unknown | 2026-11-22 |
| MCK | $1069.69 | 47,596,340 | Health Care | large | unknown | 2026-11-22 |
| MCO | $466.89 | 25,131,380 | Financials | large | unknown | 2026-11-22 |
| MDLZ | $66.29 | 42,105,904 | Consumer Staples | large | unknown | 2026-11-22 |
| MDT | $99.95 | 39,054,615 | Health Care | large | unknown | 2026-11-22 |
| META | $561.24 | 510,178,136 | Communication Services | large | unknown | 2026-11-22 |
| MKSI | $184.50 | 21,121,693 | Information Technology | mid | unknown | 2026-11-22 |
| MLM | $501.13 | 33,215,928 | Materials | large | unknown | 2026-11-22 |
| MMM | $178.00 | 31,331,275 | Industrials | large | unknown | 2026-11-22 |
| MNST | $43.71 | 30,956,262 | Consumer Staples | large | unknown | 2026-11-22 |
| MO | $74.87 | 29,132,196 | Consumer Staples | large | unknown | 2026-11-22 |
| MPC | $367.23 | 52,816,125 | Energy | large | unknown | 2026-11-22 |
| MPWR | $1143.97 | 66,343,722 | Information Technology | large | unknown | 2026-11-22 |
| MRK | $133.70 | 70,621,691 | Health Care | large | unknown | 2026-11-22 |
| MRNA | $195.15 | 76,950,802 | Health Care | large | unknown | 2026-11-22 |
| MRSH | $206.27 | 26,114,936 | Unknown | large | unknown | 2026-11-22 |
| MRVL | $122.28 | 164,474,538 | Unknown | large | unknown | 2026-11-22 |
| MS | $165.74 | 75,595,132 | Financials | large | unknown | 2026-11-22 |
| MSCI | $609.86 | 25,202,989 | Financials | large | unknown | 2026-11-22 |
| MSFT | $485.34 | 559,510,918 | Information Technology | large | unknown | 2026-11-22 |
| MSI | $520.42 | 38,438,039 | Information Technology | large | unknown | 2026-11-22 |
| MTD | $1667.17 | 22,536,757 | Health Care | large | unknown | 2026-11-22 |
| MTSI | $194.91 | 20,914,235 | Unknown | mid | unknown | 2026-11-22 |
| MTZ | $144.74 | 23,428,339 | Unknown | mid | unknown | 2026-11-22 |
| MU | $594.84 | 635,848,753 | Information Technology | large | unknown | 2026-11-22 |
| NCLH | $15.99 | 23,292,481 | Unknown | large | unknown | 2026-11-22 |
| NDAQ | $102.99 | 21,744,205 | Financials | large | unknown | 2026-11-22 |
| NEE | $83.52 | 82,338,799 | Utilities | large | unknown | 2026-11-22 |
| NEM | $94.68 | 37,809,012 | Materials | large | unknown | 2026-11-22 |
| NFLX | $56.76 | 151,664,853 | Communication Services | large | unknown | 2026-11-22 |
| NI | $44.30 | 20,651,172 | Utilities | large | unknown | 2026-11-22 |
| NKE | $32.94 | 53,323,162 | Consumer Discretionary | large | unknown | 2026-11-22 |
| NOC | $534.43 | 32,045,942 | Industrials | large | unknown | 2026-11-22 |
| NOW | $87.65 | 112,135,776 | Information Technology | large | unknown | 2026-11-22 |
| NUE | $239.68 | 21,450,955 | Materials | large | unknown | 2026-11-22 |
| NVDA | $125.65 | 1,687,876,879 | Information Technology | large | unknown | 2026-11-22 |
| NVT | $101.84 | 25,137,668 | Industrials | mid | unknown | 2026-11-22 |
| NXPI | $235.45 | 67,281,000 | Unknown | large | unknown | 2026-11-22 |
| NXT | $67.08 | 20,291,424 | Unknown | mid | unknown | 2026-11-22 |
| O | $58.03 | 23,175,987 | Real Estate | large | unknown | 2026-11-22 |
| ODFL | $168.26 | 23,437,290 | Industrials | large | unknown | 2026-11-22 |
| OKTA | $191.47 | 44,363,067 | Information Technology | large | unknown | 2026-11-22 |
| ON | $60.84 | 28,454,569 | Information Technology | large | unknown | 2026-11-22 |
| ORCL | $101.15 | 190,513,647 | Information Technology | large | unknown | 2026-11-22 |
| ORLY | $92.70 | 29,555,982 | Consumer Discretionary | large | unknown | 2026-11-22 |
| OTIS | $76.05 | 22,140,442 | Unknown | large | unknown | 2026-11-22 |
| OXY | $53.90 | 46,373,834 | Energy | large | unknown | 2026-11-22 |
| P | $92.03 | 23,494,903 | Unknown | large | unknown | 2026-11-22 |
| PANW | $343.51 | 122,916,510 | Unknown | large | unknown | 2026-11-22 |
| PCAR | $102.26 | 20,880,320 | Industrials | large | unknown | 2026-11-22 |
| PCG | $13.79 | 21,822,175 | Utilities | large | unknown | 2026-11-22 |
| PEP | $140.57 | 54,465,428 | Consumer Staples | large | unknown | 2026-11-22 |
| PFE | $27.43 | 64,251,707 | Health Care | large | unknown | 2026-11-22 |
| PG | $169.56 | 77,993,609 | Consumer Staples | large | unknown | 2026-11-22 |
| PGR | $231.53 | 32,590,863 | Financials | large | unknown | 2026-11-22 |
| PH | $872.02 | 42,310,525 | Industrials | large | unknown | 2026-11-22 |
| PLTR | $143.65 | 123,311,930 | Unknown | large | unknown | 2026-11-22 |
| PM | $184.18 | 56,581,212 | Consumer Staples | large | unknown | 2026-11-22 |
| PPL | $34.66 | 24,371,252 | Utilities | large | unknown | 2026-11-22 |
| PSA | $325.67 | 20,535,002 | Real Estate | large | unknown | 2026-11-22 |
| PSX | $239.38 | 56,850,766 | Energy | large | unknown | 2026-11-22 |
| PWR | $559.46 | 65,943,925 | Industrials | large | unknown | 2026-11-22 |
| PYPL | $53.31 | 28,865,503 | Financials | large | unknown | 2026-11-22 |
| QCOM | $150.08 | 81,553,947 | Information Technology | large | unknown | 2026-11-22 |
| RCL | $296.44 | 41,655,023 | Consumer Discretionary | large | unknown | 2026-11-22 |
| RDDT | $85.29 | 35,021,950 | Unknown | large | unknown | 2026-11-22 |
| REGN | $921.22 | 47,093,596 | Health Care | large | unknown | 2026-11-22 |
| RMD | $235.81 | 23,450,429 | Health Care | large | unknown | 2026-11-22 |
| ROK | $361.92 | 27,264,281 | Industrials | large | unknown | 2026-11-22 |
| ROP | $460.05 | 28,133,405 | Industrials | large | unknown | 2026-11-22 |
| ROST | $213.53 | 28,953,496 | Consumer Discretionary | large | unknown | 2026-11-22 |
| RRC | $48.04 | 26,081,181 | Energy | mid | unknown | 2026-11-22 |
| RSG | $246.59 | 21,109,043 | Industrials | large | unknown | 2026-11-22 |
| RTX | $190.34 | 40,428,372 | Industrials | large | unknown | 2026-11-22 |
| RVTY | $145.32 | 20,226,906 | Unknown | large | unknown | 2026-11-22 |
| SBUX | $103.17 | 41,642,118 | Consumer Discretionary | large | unknown | 2026-11-22 |
| SCHW | $90.22 | 48,644,181 | Financials | large | unknown | 2026-11-22 |
| SHW | $339.80 | 38,169,661 | Materials | large | unknown | 2026-11-22 |
| SITM | $360.75 | 21,000,893 | Unknown | mid | unknown | 2026-11-22 |
| SLB | $45.90 | 44,639,879 | Energy | large | unknown | 2026-11-22 |
| SMCI | $21.68 | 51,548,704 | Information Technology | large | unknown | 2026-11-22 |
| SMTC | $87.96 | 21,902,757 | Information Technology | mid | unknown | 2026-11-22 |
| SN | $212.69 | 26,302,527 | Unknown | mid | unknown | 2026-11-22 |
| SNDK | $79.25 | 279,430,617 | Unknown | large | unknown | 2026-11-22 |
| SNPS | $396.59 | 45,994,810 | Information Technology | large | unknown | 2026-11-22 |
| SO | $93.16 | 42,556,359 | Utilities | large | unknown | 2026-11-22 |
| SPGI | $439.73 | 39,575,003 | Financials | large | unknown | 2026-11-22 |
| SRE | $76.19 | 20,507,812 | Utilities | large | unknown | 2026-11-22 |
| STRL | $247.93 | 23,053,725 | Unknown | mid | unknown | 2026-11-22 |
| STX | $458.05 | 155,779,903 | Information Technology | large | unknown | 2026-11-22 |
| SYF | $67.79 | 22,062,942 | Financials | large | unknown | 2026-11-22 |
| SYK | $310.14 | 63,266,329 | Health Care | large | unknown | 2026-11-22 |
| T | $22.33 | 63,814,653 | Communication Services | large | unknown | 2026-11-22 |
| TDG | $1121.80 | 67,309,799 | Industrials | large | unknown | 2026-11-22 |
| TEL | $200.12 | 25,398,621 | Information Technology | large | unknown | 2026-11-22 |
| TER | $204.68 | 48,180,070 | Information Technology | large | unknown | 2026-11-22 |
| TFC | $45.82 | 30,061,023 | Financials | large | unknown | 2026-11-22 |
| TGT | $165.98 | 34,061,493 | Consumer Discretionary | large | unknown | 2026-11-22 |
| TJX | $139.69 | 53,773,567 | Consumer Discretionary | large | unknown | 2026-11-22 |
| TLN | $333.13 | 26,741,401 | Unknown | mid | unknown | 2026-11-22 |
| TMO | $670.16 | 82,633,135 | Health Care | large | unknown | 2026-11-22 |
| TMUS | $165.59 | 48,106,180 | Communication Services | large | unknown | 2026-11-22 |
| TOST | $31.43 | 23,232,715 | Unknown | mid | unknown | 2026-11-22 |
| TPR | $119.99 | 21,921,210 | Consumer Discretionary | large | unknown | 2026-11-22 |
| TRGP | $278.18 | 25,270,236 | Unknown | large | unknown | 2026-11-22 |
| TRV | $393.36 | 25,506,147 | Financials | large | unknown | 2026-11-22 |
| TSCO | $38.47 | 26,393,996 | Consumer Discretionary | large | unknown | 2026-11-22 |
| TSLA | $346.23 | 353,169,175 | Consumer Discretionary | large | unknown | 2026-11-22 |
| TT | $386.52 | 50,447,328 | Industrials | large | unknown | 2026-11-22 |
| TTMI | $58.93 | 21,143,070 | Information Technology | mid | unknown | 2026-11-22 |
| TTWO | $210.28 | 41,913,678 | Communication Services | large | unknown | 2026-11-22 |
| TWLO | $172.09 | 36,256,848 | Unknown | large | unknown | 2026-11-22 |
| TXN | $263.95 | 100,031,456 | Information Technology | large | unknown | 2026-11-22 |
| TYL | $404.76 | 24,197,198 | Information Technology | large | unknown | 2026-11-22 |
| UAL | $101.08 | 33,536,512 | Industrials | large | unknown | 2026-11-22 |
| UBER | $63.48 | 70,435,156 | Unknown | large | unknown | 2026-11-22 |
| UNH | $340.03 | 140,729,887 | Health Care | large | unknown | 2026-11-22 |
| UNP | $287.21 | 47,514,412 | Industrials | large | unknown | 2026-11-22 |
| UPS | $106.22 | 38,759,965 | Industrials | large | unknown | 2026-11-22 |
| URI | $973.14 | 41,869,719 | Industrials | large | unknown | 2026-11-22 |
| USB | $56.06 | 28,643,673 | Financials | large | unknown | 2026-11-22 |
| V | $402.43 | 177,569,959 | Financials | large | unknown | 2026-11-22 |
| VEEV | $266.21 | 21,742,831 | Unknown | large | unknown | 2026-11-22 |
| VLO | $334.29 | 57,899,999 | Energy | large | unknown | 2026-11-22 |
| VRT | $166.03 | 99,276,409 | Unknown | large | unknown | 2026-11-22 |
| VRTX | $514.89 | 45,716,973 | Health Care | large | unknown | 2026-11-22 |
| VST | $115.26 | 39,593,681 | Utilities | large | unknown | 2026-11-22 |
| VZ | $46.52 | 60,719,906 | Communication Services | large | unknown | 2026-11-22 |
| WAT | $440.31 | 33,399,273 | Health Care | large | unknown | 2026-11-22 |
| WDAY | $174.63 | 20,248,826 | Unknown | large | unknown | 2026-11-22 |
| WDC | $261.02 | 112,309,829 | Information Technology | large | unknown | 2026-11-22 |
| WEC | $117.08 | 25,857,403 | Unknown | large | unknown | 2026-11-22 |
| WELL | $240.48 | 50,142,145 | Real Estate | large | unknown | 2026-11-22 |
| WFC | $78.64 | 61,773,586 | Financials | large | unknown | 2026-11-22 |
| WM | $239.69 | 28,195,710 | Industrials | large | unknown | 2026-11-22 |
| WMB | $64.33 | 42,250,900 | Energy | large | unknown | 2026-11-22 |
| WMT | $128.04 | 122,124,950 | Consumer Staples | large | unknown | 2026-11-22 |
| WSM | $210.69 | 21,576,329 | Unknown | large | unknown | 2026-11-22 |
| WST | $390.56 | 21,063,564 | Health Care | large | unknown | 2026-11-22 |
| XEL | $79.30 | 51,171,588 | Utilities | large | unknown | 2026-11-22 |
| XOM | $159.99 | 99,144,246 | Energy | large | unknown | 2026-11-22 |
| XPO | $174.54 | 21,205,893 | Unknown | mid | unknown | 2026-11-22 |
| XYZ | $69.72 | 28,497,030 | Unknown | large | unknown | 2026-11-22 |
| YUM | $160.77 | 22,247,446 | Consumer Discretionary | large | unknown | 2026-11-22 |
