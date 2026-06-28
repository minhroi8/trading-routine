---
screened_on: 2026-06-28
expires_on: 2026-07-05
total_passed: 315
total_rejected: 1188
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
| AA | $54.10 | 20,999,003 | Materials | mid | unknown | 2026-06-28 |
| AAL | $17.87 | 41,079,445 | Industrials | mid | unknown | 2026-06-28 |
| AAPL | $281.31 | 616,681,529 | Information Technology | large | unknown | 2026-06-28 |
| ABBV | $251.79 | 61,310,383 | Health Care | large | unknown | 2026-06-28 |
| ABNB | $145.54 | 24,766,845 | Consumer Discretionary | large | unknown | 2026-06-28 |
| ABT | $93.86 | 55,224,815 | Health Care | large | unknown | 2026-06-28 |
| ACN | $128.90 | 67,411,251 | Information Technology | large | unknown | 2026-06-28 |
| ADBE | $202.75 | 69,486,478 | Information Technology | large | unknown | 2026-06-28 |
| ADI | $384.61 | 85,925,062 | Information Technology | large | unknown | 2026-06-28 |
| ADP | $223.53 | 23,808,390 | Industrials | large | unknown | 2026-06-28 |
| ADSK | $196.08 | 36,363,188 | Information Technology | large | unknown | 2026-06-28 |
| AEIS | $348.37 | 23,563,611 | Information Technology | mid | unknown | 2026-06-28 |
| AEP | $138.77 | 27,974,675 | Utilities | large | unknown | 2026-06-28 |
| AJG | $225.77 | 25,379,961 | Financials | large | unknown | 2026-06-28 |
| AKAM | $113.21 | 27,219,912 | Information Technology | large | unknown | 2026-06-28 |
| AMAT | $624.00 | 231,783,002 | Information Technology | large | unknown | 2026-06-28 |
| AMD | $520.20 | 337,547,406 | Information Technology | large | unknown | 2026-06-28 |
| AMGN | $357.75 | 33,702,473 | Health Care | large | unknown | 2026-06-28 |
| AMKR | $78.50 | 21,164,331 | Information Technology | mid | unknown | 2026-06-28 |
| AMT | $175.33 | 26,395,475 | Real Estate | large | unknown | 2026-06-28 |
| AMZN | $230.60 | 602,636,877 | Consumer Discretionary | large | unknown | 2026-06-28 |
| ANET | $157.71 | 60,995,965 | Information Technology | large | unknown | 2026-06-28 |
| AON | $328.17 | 28,613,583 | Financials | large | unknown | 2026-06-28 |
| APH | $163.47 | 70,884,257 | Information Technology | large | unknown | 2026-06-28 |
| APO | $118.28 | 24,521,902 | Financials | large | unknown | 2026-06-28 |
| APP | $476.75 | 88,889,395 | Information Technology | large | unknown | 2026-06-28 |
| ATI | $197.21 | 21,522,483 | Industrials | mid | unknown | 2026-06-28 |
| AVGO | $363.91 | 439,554,727 | Information Technology | large | unknown | 2026-06-28 |
| AXON | $464.67 | 24,302,930 | Industrials | large | unknown | 2026-06-28 |
| AXP | $340.48 | 36,633,193 | Financials | large | unknown | 2026-06-28 |
| AZO | $3124.44 | 58,711,504 | Consumer Discretionary | large | unknown | 2026-06-28 |
| BA | $217.34 | 47,872,679 | Industrials | large | unknown | 2026-06-28 |
| BAC | $57.81 | 140,713,777 | Financials | large | unknown | 2026-06-28 |
| BKNG | $181.07 | 71,821,322 | Consumer Discretionary | large | unknown | 2026-06-28 |
| BKR | $56.50 | 28,299,053 | Energy | large | unknown | 2026-06-28 |
| BLD | $425.94 | 34,473,628 | Consumer Discretionary | mid | unknown | 2026-06-28 |
| BLK | $963.65 | 56,919,457 | Financials | large | unknown | 2026-06-28 |
| BMY | $57.50 | 45,468,755 | Health Care | large | unknown | 2026-06-28 |
| BNY | $143.43 | 23,036,704 | Financials | large | unknown | 2026-06-28 |
| BRK.B | $497.49 | 69,595,014 | Financials | large | unknown | 2026-06-28 |
| BSX | $44.13 | 65,324,232 | Health Care | large | unknown | 2026-06-28 |
| BURL | $320.69 | 23,559,077 | Consumer Discretionary | mid | unknown | 2026-06-28 |
| BX | $115.37 | 28,953,552 | Financials | large | unknown | 2026-06-28 |
| C | $141.79 | 83,826,612 | Financials | large | unknown | 2026-06-28 |
| CAH | $237.82 | 25,882,059 | Health Care | large | unknown | 2026-06-28 |
| CARR | $73.55 | 25,805,842 | Industrials | large | unknown | 2026-06-28 |
| CASY | $778.84 | 41,002,680 | Consumer Staples | large | unknown | 2026-06-28 |
| CAT | $998.18 | 135,711,570 | Industrials | large | unknown | 2026-06-28 |
| CB | $341.37 | 27,061,305 | Financials | large | unknown | 2026-06-28 |
| CBOE | $242.06 | 46,480,717 | Financials | large | unknown | 2026-06-28 |
| CCI | $82.52 | 22,380,039 | Real Estate | large | unknown | 2026-06-28 |
| CCL | $29.03 | 46,276,136 | Consumer Discretionary | large | unknown | 2026-06-28 |
| CDE | $16.04 | 28,755,168 | Materials | mid | unknown | 2026-06-28 |
| CDNS | $376.60 | 49,511,557 | Information Technology | large | unknown | 2026-06-28 |
| CEG | $264.14 | 56,358,284 | Utilities | large | unknown | 2026-06-28 |
| CFG | $70.41 | 25,413,029 | Financials | large | unknown | 2026-06-28 |
| CHTR | $133.65 | 21,257,483 | Communication Services | large | unknown | 2026-06-28 |
| CIEN | $479.66 | 90,049,773 | Information Technology | large | unknown | 2026-06-28 |
| CL | $92.01 | 29,286,403 | Consumer Staples | large | unknown | 2026-06-28 |
| CMCSA | $23.14 | 57,915,841 | Communication Services | large | unknown | 2026-06-28 |
| CME | $221.05 | 61,656,252 | Financials | large | unknown | 2026-06-28 |
| CMG | $33.33 | 49,424,445 | Consumer Discretionary | large | unknown | 2026-06-28 |
| CMI | $685.54 | 38,697,056 | Industrials | large | unknown | 2026-06-28 |
| COF | $204.05 | 48,328,848 | Financials | large | unknown | 2026-06-28 |
| COHR | $380.00 | 105,836,709 | Information Technology | large | unknown | 2026-06-28 |
| COIN | $149.20 | 40,941,433 | Financials | large | unknown | 2026-06-28 |
| COP | $105.80 | 57,882,530 | Energy | large | unknown | 2026-06-28 |
| COR | $286.08 | 27,252,741 | Health Care | large | unknown | 2026-06-28 |
| COST | $950.39 | 69,571,777 | Consumer Staples | large | unknown | 2026-06-28 |
| CPRT | $30.50 | 22,253,392 | Industrials | large | unknown | 2026-06-28 |
| CRH | $112.29 | 24,874,437 | Materials | large | unknown | 2026-06-28 |
| CRM | $158.37 | 107,384,453 | Information Technology | large | unknown | 2026-06-28 |
| CRS | $591.50 | 34,924,677 | Industrials | mid | unknown | 2026-06-28 |
| CRWD | $700.04 | 80,806,354 | Information Technology | large | unknown | 2026-06-28 |
| CSCO | $113.45 | 133,688,366 | Information Technology | large | unknown | 2026-06-28 |
| CSX | $47.61 | 46,260,477 | Industrials | large | unknown | 2026-06-28 |
| CTSH | $39.98 | 39,984,067 | Information Technology | large | unknown | 2026-06-28 |
| CVNA | $62.34 | 40,631,468 | Consumer Discretionary | large | unknown | 2026-06-28 |
| CVS | $104.34 | 43,895,514 | Health Care | large | unknown | 2026-06-28 |
| CVX | $170.89 | 52,444,306 | Energy | large | unknown | 2026-06-28 |
| D | $69.40 | 41,372,182 | Utilities | large | unknown | 2026-06-28 |
| DAL | $92.56 | 30,848,252 | Industrials | large | unknown | 2026-06-28 |
| DASH | $182.95 | 42,197,224 | Consumer Discretionary | large | unknown | 2026-06-28 |
| DDOG | $239.66 | 70,426,612 | Information Technology | large | unknown | 2026-06-28 |
| DE | $613.81 | 44,665,886 | Industrials | large | unknown | 2026-06-28 |
| DELL | $394.31 | 157,404,723 | Information Technology | large | unknown | 2026-06-28 |
| DG | $119.48 | 23,516,000 | Consumer Staples | large | unknown | 2026-06-28 |
| DHR | $195.71 | 40,312,105 | Health Care | large | unknown | 2026-06-28 |
| DIS | $98.80 | 47,474,557 | Communication Services | large | unknown | 2026-06-28 |
| DKS | $239.27 | 20,773,112 | Consumer Discretionary | mid | unknown | 2026-06-28 |
| DLR | $193.23 | 23,934,218 | Real Estate | large | unknown | 2026-06-28 |
| DOCN | $139.38 | 22,580,821 | Information Technology | mid | unknown | 2026-06-28 |
| DOW | $29.06 | 30,033,371 | Materials | large | unknown | 2026-06-28 |
| DRI | $213.50 | 21,330,468 | Consumer Discretionary | large | unknown | 2026-06-28 |
| DVN | $42.18 | 43,529,646 | Energy | large | unknown | 2026-06-28 |
| DXCM | $70.09 | 20,358,877 | Health Care | large | unknown | 2026-06-28 |
| EA | $205.20 | 21,000,589 | Communication Services | large | unknown | 2026-06-28 |
| ECHO | $97.43 | 73,965,412 | Communication Services | large | unknown | 2026-06-28 |
| ECL | $283.54 | 21,842,648 | Materials | large | unknown | 2026-06-28 |
| EFX | $158.41 | 21,273,842 | Industrials | large | unknown | 2026-06-28 |
| ELV | $395.20 | 30,573,774 | Health Care | large | unknown | 2026-06-28 |
| EME | $798.45 | 20,542,010 | Industrials | large | unknown | 2026-06-28 |
| EMR | $143.45 | 21,948,860 | Industrials | large | unknown | 2026-06-28 |
| ENTG | $161.43 | 29,661,327 | Information Technology | mid | unknown | 2026-06-28 |
| EOG | $132.58 | 26,443,742 | Energy | large | unknown | 2026-06-28 |
| EQIX | $1091.09 | 41,873,337 | Real Estate | large | unknown | 2026-06-28 |
| EQT | $52.70 | 28,972,388 | Energy | large | unknown | 2026-06-28 |
| ETN | $402.34 | 50,065,697 | Industrials | large | unknown | 2026-06-28 |
| EW | $90.82 | 23,096,301 | Health Care | large | unknown | 2026-06-28 |
| EXC | $47.41 | 24,716,163 | Utilities | large | unknown | 2026-06-28 |
| EXPE | $262.78 | 20,969,460 | Consumer Discretionary | large | unknown | 2026-06-28 |
| F | $14.10 | 44,078,165 | Consumer Discretionary | large | unknown | 2026-06-28 |
| FANG | $179.74 | 25,862,203 | Energy | large | unknown | 2026-06-28 |
| FCX | $62.31 | 66,238,267 | Materials | large | unknown | 2026-06-28 |
| FDX | $318.17 | 44,234,262 | Industrials | large | unknown | 2026-06-28 |
| FICO | $1181.53 | 21,783,652 | Information Technology | large | unknown | 2026-06-28 |
| FITB | $56.34 | 34,360,933 | Financials | large | unknown | 2026-06-28 |
| FIX | $1853.70 | 55,249,937 | Industrials | large | unknown | 2026-06-28 |
| FLEX | $146.44 | 51,406,335 | Information Technology | large | unknown | 2026-06-28 |
| FN | $525.20 | 45,227,336 | Information Technology | mid | unknown | 2026-06-28 |
| FOXA | $49.94 | 23,347,310 | Communication Services | large | unknown | 2026-06-28 |
| FSLR | $238.95 | 30,777,219 | Information Technology | large | unknown | 2026-06-28 |
| FTNT | $151.29 | 38,823,574 | Information Technology | large | unknown | 2026-06-28 |
| GE | $368.49 | 72,739,647 | Industrials | large | unknown | 2026-06-28 |
| GEV | $1044.33 | 146,277,967 | Industrials | large | unknown | 2026-06-28 |
| GILD | $127.65 | 46,272,397 | Health Care | large | unknown | 2026-06-28 |
| GIS | $36.01 | 23,426,297 | Consumer Staples | large | unknown | 2026-06-28 |
| GLW | $223.06 | 108,507,795 | Information Technology | large | unknown | 2026-06-28 |
| GM | $78.13 | 36,529,411 | Consumer Discretionary | large | unknown | 2026-06-28 |
| GOOG | $334.58 | 230,717,102 | Communication Services | large | unknown | 2026-06-28 |
| GOOGL | $335.79 | 466,245,175 | Communication Services | large | unknown | 2026-06-28 |
| GS | $1018.74 | 86,718,585 | Financials | large | unknown | 2026-06-28 |
| GWW | $1353.03 | 26,249,095 | Industrials | large | unknown | 2026-06-28 |
| HAL | $34.18 | 32,764,775 | Energy | large | unknown | 2026-06-28 |
| HBAN | $17.80 | 23,549,149 | Financials | large | unknown | 2026-06-28 |
| HCA | $391.62 | 34,615,605 | Health Care | large | unknown | 2026-06-28 |
| HD | $348.11 | 69,484,819 | Consumer Discretionary | large | unknown | 2026-06-28 |
| HLT | $332.94 | 36,509,657 | Consumer Discretionary | large | unknown | 2026-06-28 |
| HON | $231.40 | 48,235,219 | Industrials | large | unknown | 2026-06-28 |
| HOOD | $98.71 | 99,288,079 | Financials | large | unknown | 2026-06-28 |
| HPE | $43.66 | 131,623,695 | Information Technology | large | unknown | 2026-06-28 |
| HPQ | $22.87 | 37,549,831 | Information Technology | large | unknown | 2026-06-28 |
| HSY | $179.10 | 21,477,108 | Consumer Staples | large | unknown | 2026-06-28 |
| HUBB | $516.90 | 25,609,438 | Industrials | large | unknown | 2026-06-28 |
| HUM | $383.89 | 26,981,000 | Health Care | large | unknown | 2026-06-28 |
| HWM | $268.74 | 42,127,432 | Industrials | large | unknown | 2026-06-28 |
| IBM | $271.41 | 109,741,075 | Information Technology | large | unknown | 2026-06-28 |
| ICE | $123.86 | 35,265,824 | Financials | large | unknown | 2026-06-28 |
| IDXX | $551.06 | 21,311,698 | Health Care | large | unknown | 2026-06-28 |
| INTC | $127.68 | 493,801,523 | Information Technology | large | unknown | 2026-06-28 |
| INTU | $267.01 | 109,690,229 | Information Technology | large | unknown | 2026-06-28 |
| ISRG | $404.75 | 48,079,661 | Health Care | large | unknown | 2026-06-28 |
| ITW | $267.67 | 20,029,346 | Industrials | large | unknown | 2026-06-28 |
| JBL | $359.05 | 31,566,836 | Information Technology | large | unknown | 2026-06-28 |
| JCI | $138.19 | 28,677,917 | Industrials | large | unknown | 2026-06-28 |
| JNJ | $254.36 | 75,507,022 | Health Care | large | unknown | 2026-06-28 |
| JPM | $327.50 | 95,108,676 | Financials | large | unknown | 2026-06-28 |
| KDP | $33.39 | 33,626,917 | Consumer Staples | large | unknown | 2026-06-28 |
| KEYS | $332.62 | 28,949,624 | Information Technology | large | unknown | 2026-06-28 |
| KHC | $23.71 | 21,139,682 | Consumer Staples | large | unknown | 2026-06-28 |
| KKR | $90.11 | 26,856,327 | Financials | large | unknown | 2026-06-28 |
| KLAC | $247.55 | 145,557,437 | Information Technology | large | unknown | 2026-06-28 |
| KNX | $76.61 | 27,443,660 | Industrials | mid | unknown | 2026-06-28 |
| KO | $82.61 | 95,718,566 | Consumer Staples | large | unknown | 2026-06-28 |
| KR | $57.72 | 26,844,899 | Consumer Staples | large | unknown | 2026-06-28 |
| KVUE | $19.12 | 29,951,373 | Consumer Staples | large | unknown | 2026-06-28 |
| LHX | $291.23 | 23,884,859 | Industrials | large | unknown | 2026-06-28 |
| LIN | $519.62 | 53,103,042 | Materials | large | unknown | 2026-06-28 |
| LITE | $814.63 | 179,211,102 | Information Technology | large | unknown | 2026-06-28 |
| LLY | $1206.57 | 160,226,230 | Health Care | large | unknown | 2026-06-28 |
| LMT | $507.10 | 24,765,461 | Industrials | large | unknown | 2026-06-28 |
| LOW | $222.53 | 29,028,706 | Consumer Discretionary | large | unknown | 2026-06-28 |
| LRCX | $377.99 | 166,664,737 | Information Technology | large | unknown | 2026-06-28 |
| LSCC | $138.25 | 22,813,575 | Information Technology | mid | unknown | 2026-06-28 |
| LULU | $117.50 | 20,499,983 | Consumer Discretionary | large | unknown | 2026-06-28 |
| LYV | $179.31 | 20,358,606 | Communication Services | large | unknown | 2026-06-28 |
| MA | $498.79 | 111,664,709 | Financials | large | unknown | 2026-06-28 |
| MAR | $377.06 | 36,884,473 | Consumer Discretionary | large | unknown | 2026-06-28 |
| MCD | $269.69 | 52,916,910 | Consumer Discretionary | large | unknown | 2026-06-28 |
| MCHP | $87.62 | 47,158,550 | Information Technology | large | unknown | 2026-06-28 |
| MCK | $762.61 | 38,545,643 | Health Care | large | unknown | 2026-06-28 |
| MCO | $449.85 | 32,544,811 | Financials | large | unknown | 2026-06-28 |
| MDLZ | $60.72 | 37,945,877 | Consumer Staples | large | unknown | 2026-06-28 |
| MDT | $80.98 | 66,036,169 | Health Care | large | unknown | 2026-06-28 |
| META | $549.92 | 356,879,628 | Communication Services | large | unknown | 2026-06-28 |
| MKSI | $388.26 | 29,372,132 | Information Technology | mid | unknown | 2026-06-28 |
| MLM | $615.96 | 25,363,684 | Materials | large | unknown | 2026-06-28 |
| MMM | $164.10 | 24,883,633 | Industrials | large | unknown | 2026-06-28 |
| MNST | $96.19 | 23,996,974 | Consumer Staples | large | unknown | 2026-06-28 |
| MO | $73.77 | 31,204,468 | Consumer Staples | large | unknown | 2026-06-28 |
| MPC | $253.99 | 34,406,163 | Energy | large | unknown | 2026-06-28 |
| MPWR | $1310.70 | 64,436,307 | Information Technology | large | unknown | 2026-06-28 |
| MRK | $128.37 | 53,634,442 | Health Care | large | unknown | 2026-06-28 |
| MRSH | $168.88 | 23,874,514 | Financials | large | unknown | 2026-06-28 |
| MRVL | $265.84 | 424,616,236 | Information Technology | large | unknown | 2026-06-28 |
| MS | $212.03 | 69,896,276 | Financials | large | unknown | 2026-06-28 |
| MSCI | $554.20 | 30,619,051 | Financials | large | unknown | 2026-06-28 |
| MSFT | $371.67 | 499,185,845 | Information Technology | large | unknown | 2026-06-28 |
| MSI | $402.96 | 22,255,067 | Information Technology | large | unknown | 2026-06-28 |
| MTD | $1264.18 | 23,758,941 | Health Care | large | unknown | 2026-06-28 |
| MTSI | $368.55 | 31,213,736 | Information Technology | mid | unknown | 2026-06-28 |
| MTZ | $396.55 | 30,407,841 | Industrials | mid | unknown | 2026-06-28 |
| MU | $1123.84 | 1,037,925,964 | Information Technology | large | unknown | 2026-06-28 |
| NCLH | $21.23 | 24,065,694 | Consumer Discretionary | large | unknown | 2026-06-28 |
| NEE | $88.26 | 73,568,621 | Utilities | large | unknown | 2026-06-28 |
| NEM | $96.09 | 44,075,171 | Materials | large | unknown | 2026-06-28 |
| NFLX | $73.63 | 256,603,244 | Communication Services | large | unknown | 2026-06-28 |
| NKE | $40.74 | 51,029,275 | Consumer Discretionary | large | unknown | 2026-06-28 |
| NOC | $499.77 | 28,419,077 | Industrials | large | unknown | 2026-06-28 |
| NOW | $98.42 | 136,993,647 | Information Technology | large | unknown | 2026-06-28 |
| NTAP | $152.40 | 35,198,315 | Information Technology | large | unknown | 2026-06-28 |
| NVDA | $191.97 | 1,037,171,055 | Information Technology | large | unknown | 2026-06-28 |
| NVT | $162.79 | 20,055,557 | Industrials | mid | unknown | 2026-06-28 |
| NXPI | $275.98 | 50,531,918 | Information Technology | large | unknown | 2026-06-28 |
| NXT | $107.05 | 21,297,379 | Industrials | mid | unknown | 2026-06-28 |
| O | $63.09 | 24,430,042 | Real Estate | large | unknown | 2026-06-28 |
| ODFL | $218.89 | 27,690,958 | Industrials | large | unknown | 2026-06-28 |
| OKTA | $124.30 | 26,281,303 | Information Technology | mid | unknown | 2026-06-28 |
| ON | $90.38 | 72,760,092 | Information Technology | large | unknown | 2026-06-28 |
| ONTO | $323.86 | 25,771,249 | Information Technology | mid | unknown | 2026-06-28 |
| ORCL | $148.65 | 175,329,146 | Information Technology | large | unknown | 2026-06-28 |
| ORLY | $89.36 | 29,906,539 | Consumer Discretionary | large | unknown | 2026-06-28 |
| OXY | $49.98 | 38,284,698 | Energy | large | unknown | 2026-06-28 |
| PANW | $303.60 | 89,807,837 | Information Technology | large | unknown | 2026-06-28 |
| PCAR | $120.75 | 20,033,157 | Industrials | large | unknown | 2026-06-28 |
| PEP | $141.23 | 47,814,917 | Consumer Staples | large | unknown | 2026-06-28 |
| PFE | $24.28 | 58,419,538 | Health Care | large | unknown | 2026-06-28 |
| PG | $148.95 | 65,506,499 | Consumer Staples | large | unknown | 2026-06-28 |
| PGR | $224.25 | 35,033,760 | Financials | large | unknown | 2026-06-28 |
| PH | $968.26 | 46,639,522 | Industrials | large | unknown | 2026-06-28 |
| PINS | $20.78 | 28,123,951 | Communication Services | mid | unknown | 2026-06-28 |
| PLD | $139.85 | 23,293,780 | Real Estate | large | unknown | 2026-06-28 |
| PLTR | $112.82 | 145,185,102 | Information Technology | large | unknown | 2026-06-28 |
| PM | $180.76 | 30,860,829 | Consumer Staples | large | unknown | 2026-06-28 |
| PNC | $244.97 | 32,959,028 | Financials | large | unknown | 2026-06-28 |
| PPL | $37.03 | 25,187,375 | Utilities | large | unknown | 2026-06-28 |
| PRIM | $93.21 | 20,642,679 | Industrials | small | unknown | 2026-06-28 |
| PSX | $171.67 | 21,431,098 | Energy | large | unknown | 2026-06-28 |
| PWR | $687.39 | 54,826,687 | Industrials | large | unknown | 2026-06-28 |
| PYPL | $44.29 | 30,842,246 | Financials | large | unknown | 2026-06-28 |
| QCOM | $188.62 | 139,065,285 | Information Technology | large | unknown | 2026-06-28 |
| RCL | $318.29 | 47,042,682 | Consumer Discretionary | large | unknown | 2026-06-28 |
| REGN | $633.29 | 51,200,391 | Health Care | large | unknown | 2026-06-28 |
| ROK | $476.45 | 20,851,031 | Industrials | large | unknown | 2026-06-28 |
| ROKU | $135.37 | 49,770,462 | Communication Services | mid | unknown | 2026-06-28 |
| ROST | $213.19 | 34,159,645 | Consumer Discretionary | large | unknown | 2026-06-28 |
| RTX | $187.94 | 40,441,843 | Industrials | large | unknown | 2026-06-28 |
| SBUX | $104.61 | 37,281,122 | Consumer Discretionary | large | unknown | 2026-06-28 |
| SCHW | $90.26 | 70,949,504 | Financials | large | unknown | 2026-06-28 |
| SHW | $344.02 | 39,795,604 | Materials | large | unknown | 2026-06-28 |
| SITM | $670.42 | 21,033,083 | Information Technology | mid | unknown | 2026-06-28 |
| SLB | $46.95 | 55,367,862 | Energy | large | unknown | 2026-06-28 |
| SMCI | $30.64 | 94,145,181 | Information Technology | large | unknown | 2026-06-28 |
| SMTC | $149.85 | 28,846,626 | Information Technology | mid | unknown | 2026-06-28 |
| SNDK | $2092.28 | 470,115,274 | Information Technology | large | unknown | 2026-06-28 |
| SNPS | $453.31 | 53,186,005 | Information Technology | large | unknown | 2026-06-28 |
| SO | $97.02 | 30,578,499 | Utilities | large | unknown | 2026-06-28 |
| SPGI | $408.17 | 56,350,191 | Financials | large | unknown | 2026-06-28 |
| STRL | $805.91 | 38,583,036 | Industrials | mid | unknown | 2026-06-28 |
| STT | $168.03 | 21,104,139 | Financials | large | unknown | 2026-06-28 |
| STX | $896.74 | 175,356,403 | Information Technology | large | unknown | 2026-06-28 |
| SYK | $332.30 | 50,703,843 | Health Care | large | unknown | 2026-06-28 |
| T | $22.70 | 77,464,744 | Communication Services | large | unknown | 2026-06-28 |
| TDG | $1324.42 | 38,836,438 | Industrials | large | unknown | 2026-06-28 |
| TEL | $198.01 | 35,646,498 | Information Technology | large | unknown | 2026-06-28 |
| TER | $435.82 | 70,929,697 | Information Technology | large | unknown | 2026-06-28 |
| TFC | $50.44 | 40,251,775 | Financials | large | unknown | 2026-06-28 |
| TGT | $140.31 | 29,476,597 | Consumer Staples | large | unknown | 2026-06-28 |
| TJX | $155.39 | 41,183,920 | Consumer Discretionary | large | unknown | 2026-06-28 |
| TLN | $403.59 | 24,051,740 | Utilities | mid | unknown | 2026-06-28 |
| TMO | $512.74 | 63,542,723 | Health Care | large | unknown | 2026-06-28 |
| TMUS | $182.62 | 38,320,142 | Communication Services | large | unknown | 2026-06-28 |
| TRV | $327.45 | 21,988,232 | Financials | large | unknown | 2026-06-28 |
| TSCO | $31.20 | 31,210,630 | Consumer Discretionary | large | unknown | 2026-06-28 |
| TSLA | $379.00 | 364,228,860 | Consumer Discretionary | large | unknown | 2026-06-28 |
| TT | $477.85 | 37,893,757 | Industrials | large | unknown | 2026-06-28 |
| TTD | $18.30 | 20,795,243 | Communication Services | large | unknown | 2026-06-28 |
| TTMI | $192.38 | 25,649,179 | Information Technology | mid | unknown | 2026-06-28 |
| TTWO | $238.36 | 30,685,904 | Communication Services | large | unknown | 2026-06-28 |
| TWLO | $191.62 | 29,983,235 | Information Technology | mid | unknown | 2026-06-28 |
| TXN | $285.42 | 125,122,538 | Information Technology | large | unknown | 2026-06-28 |
| TYL | $294.17 | 20,876,706 | Information Technology | large | unknown | 2026-06-28 |
| UAL | $136.03 | 30,298,608 | Industrials | large | unknown | 2026-06-28 |
| UBER | $76.03 | 104,315,078 | Industrials | large | unknown | 2026-06-28 |
| ULTA | $488.11 | 27,004,365 | Consumer Discretionary | large | unknown | 2026-06-28 |
| UNH | $427.44 | 109,538,093 | Health Care | large | unknown | 2026-06-28 |
| UNP | $268.34 | 35,190,571 | Industrials | large | unknown | 2026-06-28 |
| UPS | $108.15 | 24,869,292 | Industrials | large | unknown | 2026-06-28 |
| URI | $1122.83 | 36,841,814 | Industrials | large | unknown | 2026-06-28 |
| USB | $60.91 | 40,005,171 | Financials | large | unknown | 2026-06-28 |
| USFD | $98.33 | 20,156,488 | Consumer Staples | mid | unknown | 2026-06-28 |
| V | $335.44 | 124,037,984 | Financials | large | unknown | 2026-06-28 |
| VEEV | $171.28 | 27,121,735 | Health Care | large | unknown | 2026-06-28 |
| VLO | $259.41 | 35,564,053 | Energy | large | unknown | 2026-06-28 |
| VMC | $311.47 | 28,059,614 | Materials | large | unknown | 2026-06-28 |
| VRSK | $182.16 | 25,885,686 | Industrials | large | unknown | 2026-06-28 |
| VRT | $303.46 | 91,720,701 | Industrials | large | unknown | 2026-06-28 |
| VRTX | $491.10 | 30,009,259 | Health Care | large | unknown | 2026-06-28 |
| VSH | $56.30 | 27,509,188 | Information Technology | small | unknown | 2026-06-28 |
| VST | $163.60 | 28,381,063 | Utilities | large | unknown | 2026-06-28 |
| VZ | $46.50 | 67,056,286 | Communication Services | large | unknown | 2026-06-28 |
| WAT | $374.11 | 27,954,841 | Health Care | large | unknown | 2026-06-28 |
| WBD | $26.68 | 52,961,819 | Communication Services | large | unknown | 2026-06-28 |
| WDAY | $123.99 | 36,291,290 | Information Technology | large | unknown | 2026-06-28 |
| WDC | $586.46 | 209,761,003 | Information Technology | large | unknown | 2026-06-28 |
| WELL | $227.28 | 38,323,417 | Real Estate | large | unknown | 2026-06-28 |
| WFC | $83.88 | 105,616,707 | Financials | large | unknown | 2026-06-28 |
| WM | $225.49 | 23,682,047 | Industrials | large | unknown | 2026-06-28 |
| WMB | $77.97 | 28,670,774 | Energy | large | unknown | 2026-06-28 |
| WMT | $115.30 | 123,330,337 | Consumer Staples | large | unknown | 2026-06-28 |
| WWD | $431.23 | 24,175,665 | Industrials | mid | unknown | 2026-06-28 |
| XEL | $82.20 | 29,537,951 | Utilities | large | unknown | 2026-06-28 |
| XOM | $136.40 | 79,768,005 | Energy | large | unknown | 2026-06-28 |
| XPO | $201.52 | 23,850,784 | Industrials | mid | unknown | 2026-06-28 |
| ZTS | $76.07 | 23,879,419 | Health Care | large | unknown | 2026-06-28 |
