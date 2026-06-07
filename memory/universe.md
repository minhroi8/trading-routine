---
screened_on: 2026-06-07
expires_on: 2026-06-14
total_passed: 299
total_rejected: 1235
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
| AAL | $13.50 | 30,330,323 | Industrials | mid | unknown | 2026-06-07 |
| AAPL | $307.59 | 428,507,478 | Information Technology | large | unknown | 2026-06-07 |
| ABBV | $227.09 | 51,093,806 | Health Care | large | unknown | 2026-06-07 |
| ABNB | $133.52 | 27,417,628 | Consumer Discretionary | large | unknown | 2026-06-07 |
| ABT | $91.06 | 45,674,547 | Health Care | large | unknown | 2026-06-07 |
| ACN | $178.30 | 50,371,453 | Information Technology | large | unknown | 2026-06-07 |
| ADBE | $251.43 | 43,491,696 | Information Technology | large | unknown | 2026-06-07 |
| ADI | $401.45 | 83,375,528 | Information Technology | large | unknown | 2026-06-07 |
| ADP | $231.93 | 28,050,940 | Industrials | large | unknown | 2026-06-07 |
| ADSK | $229.91 | 31,623,758 | Information Technology | large | unknown | 2026-06-07 |
| AEIS | $294.55 | 25,410,101 | Information Technology | mid | unknown | 2026-06-07 |
| AEP | $129.15 | 36,311,550 | Utilities | large | unknown | 2026-06-07 |
| AJG | $216.16 | 24,399,137 | Financials | large | unknown | 2026-06-07 |
| AKAM | $149.25 | 42,659,146 | Information Technology | large | unknown | 2026-06-07 |
| ALL | $221.11 | 20,023,327 | Unknown | large | unknown | 2026-06-07 |
| AMAT | $453.07 | 116,395,100 | Information Technology | large | unknown | 2026-06-07 |
| AMD | $466.46 | 339,290,020 | Information Technology | large | unknown | 2026-06-07 |
| AMGN | $349.54 | 25,922,141 | Health Care | large | unknown | 2026-06-07 |
| AMT | $193.94 | 27,754,040 | Real Estate | large | unknown | 2026-06-07 |
| AMZN | $246.15 | 487,115,607 | Consumer Discretionary | large | unknown | 2026-06-07 |
| ANET | $154.22 | 78,342,038 | Information Technology | large | unknown | 2026-06-07 |
| AON | $328.64 | 31,292,575 | Financials | large | unknown | 2026-06-07 |
| APH | $138.82 | 84,930,670 | Information Technology | large | unknown | 2026-06-07 |
| APO | $128.03 | 24,907,668 | Financials | large | unknown | 2026-06-07 |
| APP | $557.10 | 110,047,510 | Unknown | large | unknown | 2026-06-07 |
| ARES | $125.68 | 23,312,092 | Unknown | large | unknown | 2026-06-07 |
| AVGO | $385.73 | 363,099,912 | Information Technology | large | unknown | 2026-06-07 |
| AXON | $486.25 | 26,902,129 | Industrials | large | unknown | 2026-06-07 |
| AXP | $310.56 | 39,694,959 | Unknown | large | unknown | 2026-06-07 |
| AZO | $3115.62 | 59,233,122 | Consumer Discretionary | large | unknown | 2026-06-07 |
| BA | $215.43 | 55,332,096 | Industrials | large | unknown | 2026-06-07 |
| BAC | $53.82 | 126,684,028 | Financials | large | unknown | 2026-06-07 |
| BDX | $151.22 | 24,500,027 | Health Care | large | unknown | 2026-06-07 |
| BKNG | $165.90 | 61,294,773 | Consumer Discretionary | large | unknown | 2026-06-07 |
| BKR | $62.59 | 26,548,436 | Unknown | large | unknown | 2026-06-07 |
| BLD | $401.68 | 22,214,276 | Unknown | mid | unknown | 2026-06-07 |
| BLK | $996.52 | 41,032,590 | Unknown | large | unknown | 2026-06-07 |
| BMY | $57.28 | 38,672,739 | Health Care | large | unknown | 2026-06-07 |
| BNY | $142.39 | 22,254,862 | Unknown | large | unknown | 2026-06-07 |
| BRK.B | $488.12 | 67,043,651 | Financials | large | unknown | 2026-06-07 |
| BSX | $48.56 | 76,259,313 | Health Care | large | unknown | 2026-06-07 |
| BURL | $316.73 | 33,666,290 | Unknown | mid | unknown | 2026-06-07 |
| BX | $115.29 | 24,284,539 | Financials | large | unknown | 2026-06-07 |
| C | $132.47 | 61,180,426 | Financials | large | unknown | 2026-06-07 |
| CAH | $205.74 | 25,482,087 | Unknown | large | unknown | 2026-06-07 |
| CARR | $67.13 | 23,468,903 | Unknown | large | unknown | 2026-06-07 |
| CASY | $761.73 | 31,246,511 | Consumer Staples | large | unknown | 2026-06-07 |
| CAT | $903.99 | 101,651,013 | Industrials | large | unknown | 2026-06-07 |
| CB | $326.35 | 24,268,102 | Financials | large | unknown | 2026-06-07 |
| CBOE | $281.27 | 31,689,464 | Unknown | large | unknown | 2026-06-07 |
| CCL | $27.38 | 37,243,226 | Unknown | large | unknown | 2026-06-07 |
| CDNS | $376.25 | 44,491,255 | Unknown | large | unknown | 2026-06-07 |
| CEG | $254.81 | 66,563,581 | Unknown | large | unknown | 2026-06-07 |
| CFG | $63.95 | 20,109,106 | Financials | large | unknown | 2026-06-07 |
| CHTR | $132.01 | 21,329,967 | Unknown | large | unknown | 2026-06-07 |
| CI | $289.49 | 20,296,982 | Health Care | large | unknown | 2026-06-07 |
| CIEN | $488.20 | 66,817,379 | Unknown | large | unknown | 2026-06-07 |
| CL | $88.56 | 27,769,497 | Consumer Staples | large | unknown | 2026-06-07 |
| CMCSA | $23.81 | 63,561,743 | Unknown | large | unknown | 2026-06-07 |
| CME | $257.46 | 42,144,281 | Financials | large | unknown | 2026-06-07 |
| CMG | $29.30 | 42,066,519 | Consumer Discretionary | large | unknown | 2026-06-07 |
| CMI | $651.23 | 36,041,309 | Industrials | large | unknown | 2026-06-07 |
| COF | $180.70 | 49,119,367 | Financials | large | unknown | 2026-06-07 |
| COHR | $376.74 | 92,057,579 | Unknown | large | unknown | 2026-06-07 |
| COIN | $152.43 | 48,081,043 | Unknown | large | unknown | 2026-06-07 |
| COP | $117.11 | 48,466,632 | Energy | large | unknown | 2026-06-07 |
| COR | $275.05 | 32,994,124 | Unknown | large | unknown | 2026-06-07 |
| COST | $971.83 | 84,845,890 | Consumer Staples | large | unknown | 2026-06-07 |
| CPRT | $30.97 | 23,326,002 | Industrials | large | unknown | 2026-06-07 |
| CRH | $105.01 | 22,214,598 | Unknown | large | unknown | 2026-06-07 |
| CRM | $185.60 | 105,134,205 | Information Technology | large | unknown | 2026-06-07 |
| CRS | $483.67 | 21,905,924 | Materials | mid | unknown | 2026-06-07 |
| CRWD | $670.84 | 93,691,829 | Information Technology | large | unknown | 2026-06-07 |
| CSCO | $121.65 | 158,094,679 | Information Technology | large | unknown | 2026-06-07 |
| CSX | $47.00 | 42,774,504 | Industrials | large | unknown | 2026-06-07 |
| CTSH | $53.23 | 27,268,675 | Information Technology | large | unknown | 2026-06-07 |
| CVNA | $66.49 | 33,685,260 | Unknown | large | unknown | 2026-06-07 |
| CVS | $95.94 | 47,650,867 | Health Care | large | unknown | 2026-06-07 |
| CVX | $187.31 | 50,481,363 | Energy | large | unknown | 2026-06-07 |
| D | $66.92 | 41,547,257 | Utilities | large | unknown | 2026-06-07 |
| DAL | $79.40 | 26,147,166 | Industrials | large | unknown | 2026-06-07 |
| DASH | $156.82 | 40,346,484 | Unknown | large | unknown | 2026-06-07 |
| DDOG | $234.00 | 73,164,417 | Unknown | large | unknown | 2026-06-07 |
| DE | $584.22 | 50,001,478 | Industrials | large | unknown | 2026-06-07 |
| DELL | $394.43 | 131,805,513 | Information Technology | large | unknown | 2026-06-07 |
| DG | $103.64 | 28,054,999 | Consumer Staples | large | unknown | 2026-06-07 |
| DHR | $184.33 | 54,441,167 | Health Care | large | unknown | 2026-06-07 |
| DIS | $99.74 | 41,373,442 | Communication Services | large | unknown | 2026-06-07 |
| DKS | $214.38 | 21,777,526 | Consumer Discretionary | mid | unknown | 2026-06-07 |
| DLTR | $108.80 | 22,198,893 | Consumer Staples | large | unknown | 2026-06-07 |
| DOCN | $169.90 | 22,268,117 | Unknown | mid | unknown | 2026-06-07 |
| DOW | $33.99 | 26,917,842 | Materials | large | unknown | 2026-06-07 |
| DT | $42.24 | 21,227,130 | Unknown | mid | unknown | 2026-06-07 |
| DVN | $44.29 | 40,654,000 | Energy | large | unknown | 2026-06-07 |
| DXCM | $72.84 | 25,673,416 | Health Care | large | unknown | 2026-06-07 |
| EBAY | $109.33 | 23,250,713 | Consumer Discretionary | large | unknown | 2026-06-07 |
| ECL | $258.05 | 22,359,744 | Materials | large | unknown | 2026-06-07 |
| ELV | $415.68 | 28,977,826 | Unknown | large | unknown | 2026-06-07 |
| EME | $816.77 | 21,993,211 | Unknown | large | unknown | 2026-06-07 |
| EMR | $138.12 | 20,973,083 | Industrials | large | unknown | 2026-06-07 |
| ENPH | $56.07 | 20,774,059 | Information Technology | small | unknown | 2026-06-07 |
| ENTG | $125.28 | 21,463,072 | Unknown | mid | unknown | 2026-06-07 |
| EOG | $137.78 | 23,147,659 | Energy | large | unknown | 2026-06-07 |
| EQIX | $1081.04 | 29,279,334 | Real Estate | large | unknown | 2026-06-07 |
| EQT | $53.73 | 26,350,576 | Unknown | large | unknown | 2026-06-07 |
| ETN | $395.83 | 58,822,317 | Industrials | large | unknown | 2026-06-07 |
| EW | $85.96 | 23,015,124 | Health Care | large | unknown | 2026-06-07 |
| EXPE | $228.84 | 22,089,780 | Consumer Discretionary | large | unknown | 2026-06-07 |
| F | $14.91 | 85,286,092 | Consumer Discretionary | large | unknown | 2026-06-07 |
| FCX | $63.37 | 58,997,936 | Materials | large | unknown | 2026-06-07 |
| FDX | $331.15 | 28,363,635 | Industrials | large | unknown | 2026-06-07 |
| FICO | $1138.01 | 30,011,663 | Information Technology | large | unknown | 2026-06-07 |
| FIS | $40.97 | 20,504,611 | Financials | large | unknown | 2026-06-07 |
| FITB | $52.01 | 28,526,387 | Financials | large | unknown | 2026-06-07 |
| FIVE | $190.40 | 21,198,778 | Unknown | mid | unknown | 2026-06-07 |
| FIX | $1844.04 | 42,402,649 | Unknown | large | unknown | 2026-06-07 |
| FLEX | $151.89 | 53,554,301 | Unknown | mid | unknown | 2026-06-07 |
| FN | $620.98 | 49,232,549 | Unknown | mid | unknown | 2026-06-07 |
| FSLR | $278.95 | 36,030,415 | Unknown | large | unknown | 2026-06-07 |
| FTI | $66.81 | 24,332,744 | Unknown | mid | unknown | 2026-06-07 |
| FTNT | $144.71 | 34,483,138 | Information Technology | large | unknown | 2026-06-07 |
| GE | $328.13 | 66,436,806 | Industrials | large | unknown | 2026-06-07 |
| GEV | $933.11 | 103,432,669 | Industrials | large | unknown | 2026-06-07 |
| GILD | $129.00 | 38,652,265 | Health Care | large | unknown | 2026-06-07 |
| GIS | $33.14 | 20,712,587 | Consumer Staples | large | unknown | 2026-06-07 |
| GLW | $177.42 | 105,475,011 | Information Technology | large | unknown | 2026-06-07 |
| GM | $82.09 | 30,946,215 | Consumer Discretionary | large | unknown | 2026-06-07 |
| GOOG | $366.16 | 195,620,229 | Communication Services | large | unknown | 2026-06-07 |
| GOOGL | $368.98 | 395,227,829 | Communication Services | large | unknown | 2026-06-07 |
| GS | $1038.46 | 68,940,506 | Financials | large | unknown | 2026-06-07 |
| GWW | $1300.24 | 21,828,209 | Industrials | large | unknown | 2026-06-07 |
| HAL | $39.17 | 27,039,137 | Energy | large | unknown | 2026-06-07 |
| HBAN | $16.51 | 21,548,661 | Financials | large | unknown | 2026-06-07 |
| HCA | $372.15 | 40,800,739 | Health Care | large | unknown | 2026-06-07 |
| HD | $310.74 | 68,636,114 | Consumer Discretionary | large | unknown | 2026-06-07 |
| HLT | $343.09 | 27,092,376 | Consumer Discretionary | large | unknown | 2026-06-07 |
| HON | $213.98 | 40,775,971 | Industrials | large | unknown | 2026-06-07 |
| HOOD | $82.45 | 69,327,326 | Unknown | large | unknown | 2026-06-07 |
| HPE | $49.16 | 105,839,062 | Information Technology | large | unknown | 2026-06-07 |
| HPQ | $25.58 | 39,612,684 | Information Technology | large | unknown | 2026-06-07 |
| HUBB | $476.74 | 27,149,930 | Industrials | large | unknown | 2026-06-07 |
| HUM | $350.18 | 29,972,180 | Health Care | large | unknown | 2026-06-07 |
| HWM | $251.72 | 28,275,653 | Industrials | large | unknown | 2026-06-07 |
| IBM | $284.82 | 111,396,321 | Information Technology | large | unknown | 2026-06-07 |
| ICE | $141.47 | 31,228,702 | Financials | large | unknown | 2026-06-07 |
| IDXX | $562.36 | 20,681,088 | Health Care | large | unknown | 2026-06-07 |
| INTC | $98.97 | 367,981,862 | Information Technology | large | unknown | 2026-06-07 |
| INTU | $296.76 | 121,385,558 | Information Technology | large | unknown | 2026-06-07 |
| IQV | $183.43 | 21,201,019 | Health Care | large | unknown | 2026-06-07 |
| ISRG | $422.09 | 48,362,567 | Health Care | large | unknown | 2026-06-07 |
| JBL | $353.15 | 25,391,362 | Unknown | large | unknown | 2026-06-07 |
| JCI | $143.55 | 23,034,715 | Industrials | large | unknown | 2026-06-07 |
| JNJ | $232.71 | 60,336,627 | Health Care | large | unknown | 2026-06-07 |
| JPM | $312.38 | 78,399,054 | Financials | large | unknown | 2026-06-07 |
| KDP | $30.54 | 24,924,132 | Consumer Staples | large | unknown | 2026-06-07 |
| KEYS | $329.74 | 40,678,739 | Information Technology | large | unknown | 2026-06-07 |
| KHC | $22.59 | 20,426,334 | Consumer Staples | large | unknown | 2026-06-07 |
| KKR | $93.39 | 28,459,996 | Unknown | large | unknown | 2026-06-07 |
| KLAC | $1929.24 | 107,646,910 | Information Technology | large | unknown | 2026-06-07 |
| KNX | $78.56 | 22,186,670 | Unknown | mid | unknown | 2026-06-07 |
| KO | $79.50 | 67,439,568 | Consumer Staples | large | unknown | 2026-06-07 |
| KR | $63.56 | 20,165,043 | Consumer Staples | large | unknown | 2026-06-07 |
| KVUE | $17.71 | 24,361,836 | Unknown | large | unknown | 2026-06-07 |
| LIN | $507.93 | 44,723,574 | Materials | large | unknown | 2026-06-07 |
| LITE | $863.26 | 199,430,163 | Unknown | large | unknown | 2026-06-07 |
| LLY | $1132.80 | 134,857,728 | Health Care | large | unknown | 2026-06-07 |
| LMT | $523.91 | 24,701,161 | Industrials | large | unknown | 2026-06-07 |
| LOW | $210.75 | 34,439,512 | Consumer Discretionary | large | unknown | 2026-06-07 |
| LRCX | $303.26 | 94,139,584 | Information Technology | large | unknown | 2026-06-07 |
| LSCC | $135.43 | 25,189,097 | Unknown | mid | unknown | 2026-06-07 |
| MA | $491.14 | 113,683,246 | Financials | large | unknown | 2026-06-07 |
| MAR | $392.49 | 27,643,466 | Unknown | large | unknown | 2026-06-07 |
| MCD | $279.89 | 45,132,078 | Consumer Discretionary | large | unknown | 2026-06-07 |
| MCHP | $88.27 | 52,533,429 | Information Technology | large | unknown | 2026-06-07 |
| MCK | $775.79 | 48,948,936 | Health Care | large | unknown | 2026-06-07 |
| MCO | $451.26 | 32,257,373 | Financials | large | unknown | 2026-06-07 |
| MDLZ | $62.03 | 27,783,600 | Consumer Staples | large | unknown | 2026-06-07 |
| MDT | $81.64 | 65,882,898 | Health Care | large | unknown | 2026-06-07 |
| META | $592.85 | 306,715,377 | Communication Services | large | unknown | 2026-06-07 |
| MKSI | $301.61 | 22,535,054 | Information Technology | mid | unknown | 2026-06-07 |
| MLM | $576.01 | 26,100,874 | Materials | large | unknown | 2026-06-07 |
| MMM | $153.78 | 23,126,149 | Industrials | large | unknown | 2026-06-07 |
| MNST | $89.56 | 26,993,661 | Consumer Staples | large | unknown | 2026-06-07 |
| MO | $72.20 | 32,062,902 | Consumer Staples | large | unknown | 2026-06-07 |
| MPC | $262.04 | 26,703,375 | Energy | large | unknown | 2026-06-07 |
| MPWR | $1477.77 | 50,596,193 | Information Technology | large | unknown | 2026-06-07 |
| MRK | $120.88 | 39,904,617 | Health Care | large | unknown | 2026-06-07 |
| MRSH | $165.41 | 25,187,762 | Unknown | large | unknown | 2026-06-07 |
| MS | $212.02 | 64,976,657 | Financials | large | unknown | 2026-06-07 |
| MSCI | $615.38 | 29,268,801 | Financials | large | unknown | 2026-06-07 |
| MSFT | $416.63 | 397,377,508 | Information Technology | large | unknown | 2026-06-07 |
| MSI | $410.30 | 34,798,294 | Information Technology | large | unknown | 2026-06-07 |
| MTD | $1154.15 | 25,965,897 | Health Care | large | unknown | 2026-06-07 |
| MTSI | $345.11 | 34,115,997 | Unknown | mid | unknown | 2026-06-07 |
| MTZ | $363.57 | 26,505,395 | Unknown | mid | unknown | 2026-06-07 |
| MU | $865.00 | 787,029,065 | Information Technology | large | unknown | 2026-06-07 |
| NCLH | $18.73 | 20,578,834 | Unknown | large | unknown | 2026-06-07 |
| NEE | $85.83 | 73,302,883 | Utilities | large | unknown | 2026-06-07 |
| NEM | $99.71 | 30,249,426 | Materials | large | unknown | 2026-06-07 |
| NFLX | $82.20 | 174,291,723 | Communication Services | large | unknown | 2026-06-07 |
| NKE | $42.98 | 48,387,915 | Consumer Discretionary | large | unknown | 2026-06-07 |
| NOC | $544.21 | 24,555,819 | Industrials | large | unknown | 2026-06-07 |
| NOW | $112.44 | 138,265,394 | Information Technology | large | unknown | 2026-06-07 |
| NRG | $129.21 | 23,553,238 | Utilities | large | unknown | 2026-06-07 |
| NTAP | $167.06 | 35,482,634 | Information Technology | large | unknown | 2026-06-07 |
| NVDA | $205.17 | 1,080,251,672 | Information Technology | large | unknown | 2026-06-07 |
| NXPI | $296.10 | 50,926,505 | Unknown | large | unknown | 2026-06-07 |
| NXT | $131.60 | 23,153,440 | Unknown | mid | unknown | 2026-06-07 |
| O | $60.85 | 21,229,993 | Real Estate | large | unknown | 2026-06-07 |
| ODFL | $242.65 | 23,311,736 | Industrials | large | unknown | 2026-06-07 |
| OKTA | $118.67 | 25,850,348 | Information Technology | mid | unknown | 2026-06-07 |
| ON | $117.26 | 64,788,695 | Information Technology | large | unknown | 2026-06-07 |
| ORCL | $213.66 | 133,044,449 | Information Technology | large | unknown | 2026-06-07 |
| ORLY | $90.34 | 24,643,483 | Consumer Discretionary | large | unknown | 2026-06-07 |
| OXY | $56.94 | 38,653,263 | Energy | large | unknown | 2026-06-07 |
| PANW | $272.16 | 104,580,144 | Unknown | large | unknown | 2026-06-07 |
| PEP | $141.88 | 38,846,507 | Consumer Staples | large | unknown | 2026-06-07 |
| PFE | $26.04 | 40,159,140 | Health Care | large | unknown | 2026-06-07 |
| PG | $146.49 | 54,957,729 | Consumer Staples | large | unknown | 2026-06-07 |
| PGR | $204.02 | 31,352,293 | Financials | large | unknown | 2026-06-07 |
| PH | $882.40 | 45,985,502 | Industrials | large | unknown | 2026-06-07 |
| PINS | $21.41 | 26,469,781 | Unknown | mid | unknown | 2026-06-07 |
| PLTR | $135.60 | 158,746,874 | Unknown | large | unknown | 2026-06-07 |
| PM | $178.29 | 34,043,741 | Consumer Staples | large | unknown | 2026-06-07 |
| PPL | $35.73 | 21,280,983 | Utilities | large | unknown | 2026-06-07 |
| PWR | $695.21 | 54,809,431 | Industrials | large | unknown | 2026-06-07 |
| PYPL | $41.28 | 27,208,670 | Financials | large | unknown | 2026-06-07 |
| QCOM | $215.58 | 161,071,420 | Information Technology | large | unknown | 2026-06-07 |
| RCL | $280.00 | 40,959,805 | Consumer Discretionary | large | unknown | 2026-06-07 |
| REGN | $635.35 | 55,111,123 | Health Care | large | unknown | 2026-06-07 |
| RL | $366.32 | 23,506,671 | Consumer Discretionary | large | unknown | 2026-06-07 |
| ROK | $446.68 | 21,221,030 | Industrials | large | unknown | 2026-06-07 |
| ROST | $230.28 | 37,154,639 | Consumer Discretionary | large | unknown | 2026-06-07 |
| RSG | $210.26 | 27,406,002 | Industrials | large | unknown | 2026-06-07 |
| RTX | $181.02 | 35,404,280 | Industrials | large | unknown | 2026-06-07 |
| SATS | $116.27 | 36,938,234 | Communication Services | large | unknown | 2026-06-07 |
| SBUX | $95.28 | 35,628,707 | Consumer Discretionary | large | unknown | 2026-06-07 |
| SCHW | $88.78 | 65,514,544 | Financials | large | unknown | 2026-06-07 |
| SHW | $305.24 | 33,203,213 | Materials | large | unknown | 2026-06-07 |
| SITM | $629.56 | 26,654,752 | Unknown | mid | unknown | 2026-06-07 |
| SLB | $54.88 | 39,638,617 | Energy | large | unknown | 2026-06-07 |
| SMCI | $41.63 | 65,402,615 | Information Technology | large | unknown | 2026-06-07 |
| SMTC | $150.79 | 39,188,688 | Information Technology | small | unknown | 2026-06-07 |
| SNDK | $1557.74 | 366,271,019 | Unknown | large | unknown | 2026-06-07 |
| SNPS | $464.77 | 49,680,928 | Information Technology | large | unknown | 2026-06-07 |
| SO | $92.64 | 23,782,129 | Utilities | large | unknown | 2026-06-07 |
| SPGI | $424.62 | 52,701,042 | Financials | large | unknown | 2026-06-07 |
| STRL | $881.35 | 33,220,382 | Unknown | mid | unknown | 2026-06-07 |
| STX | $847.42 | 128,051,699 | Information Technology | large | unknown | 2026-06-07 |
| SYK | $305.64 | 61,897,174 | Health Care | large | unknown | 2026-06-07 |
| T | $22.76 | 54,113,440 | Communication Services | large | unknown | 2026-06-07 |
| TDG | $1238.89 | 35,488,629 | Industrials | large | unknown | 2026-06-07 |
| TEL | $212.56 | 38,684,946 | Information Technology | large | unknown | 2026-06-07 |
| TER | $358.03 | 48,703,103 | Information Technology | large | unknown | 2026-06-07 |
| TFC | $49.20 | 24,769,102 | Financials | large | unknown | 2026-06-07 |
| TGT | $122.55 | 32,862,074 | Consumer Discretionary | large | unknown | 2026-06-07 |
| TJX | $160.69 | 43,942,173 | Consumer Discretionary | large | unknown | 2026-06-07 |
| TLN | $364.91 | 20,380,963 | Unknown | mid | unknown | 2026-06-07 |
| TMO | $472.71 | 85,150,423 | Health Care | large | unknown | 2026-06-07 |
| TMUS | $177.99 | 35,741,937 | Communication Services | large | unknown | 2026-06-07 |
| TSCO | $29.78 | 28,843,704 | Consumer Discretionary | large | unknown | 2026-06-07 |
| TSLA | $390.82 | 331,854,368 | Consumer Discretionary | large | unknown | 2026-06-07 |
| TT | $456.83 | 35,390,679 | Industrials | large | unknown | 2026-06-07 |
| TTD | $19.95 | 20,449,854 | Unknown | large | unknown | 2026-06-07 |
| TTMI | $167.36 | 24,578,213 | Information Technology | mid | unknown | 2026-06-07 |
| TTWO | $214.45 | 29,728,850 | Communication Services | large | unknown | 2026-06-07 |
| TWLO | $226.11 | 32,687,397 | Unknown | mid | unknown | 2026-06-07 |
| TXN | $284.97 | 107,206,618 | Information Technology | large | unknown | 2026-06-07 |
| UAL | $105.70 | 25,243,662 | Industrials | large | unknown | 2026-06-07 |
| UBER | $70.72 | 84,251,052 | Unknown | large | unknown | 2026-06-07 |
| ULTA | $467.13 | 26,402,249 | Consumer Discretionary | large | unknown | 2026-06-07 |
| UNH | $399.59 | 94,810,921 | Health Care | large | unknown | 2026-06-07 |
| UNP | $272.36 | 42,340,880 | Industrials | large | unknown | 2026-06-07 |
| UPS | $108.54 | 23,901,303 | Industrials | large | unknown | 2026-06-07 |
| URI | $1067.45 | 32,552,499 | Industrials | large | unknown | 2026-06-07 |
| USB | $55.69 | 32,550,126 | Financials | large | unknown | 2026-06-07 |
| V | $323.66 | 122,265,886 | Financials | large | unknown | 2026-06-07 |
| VEEV | $172.65 | 28,954,324 | Unknown | large | unknown | 2026-06-07 |
| VLO | $255.78 | 31,169,640 | Energy | large | unknown | 2026-06-07 |
| VMC | $281.41 | 21,267,836 | Materials | large | unknown | 2026-06-07 |
| VRT | $300.49 | 83,155,293 | Unknown | large | unknown | 2026-06-07 |
| VRTX | $446.93 | 23,591,269 | Health Care | large | unknown | 2026-06-07 |
| VSH | $57.24 | 21,881,527 | Information Technology | small | unknown | 2026-06-07 |
| VST | $148.75 | 32,612,589 | Utilities | large | unknown | 2026-06-07 |
| VZ | $45.38 | 56,140,393 | Communication Services | large | unknown | 2026-06-07 |
| WAT | $365.34 | 30,754,500 | Health Care | large | unknown | 2026-06-07 |
| WBD | $26.25 | 38,986,440 | Communication Services | large | unknown | 2026-06-07 |
| WDAY | $144.29 | 36,513,055 | Unknown | large | unknown | 2026-06-07 |
| WDC | $511.40 | 120,167,527 | Information Technology | large | unknown | 2026-06-07 |
| WELL | $206.90 | 33,569,062 | Real Estate | large | unknown | 2026-06-07 |
| WFC | $81.96 | 86,591,294 | Financials | large | unknown | 2026-06-07 |
| WM | $220.21 | 20,486,275 | Industrials | large | unknown | 2026-06-07 |
| WMB | $71.98 | 28,447,149 | Energy | large | unknown | 2026-06-07 |
| WMT | $118.90 | 114,857,454 | Consumer Staples | large | unknown | 2026-06-07 |
| XEL | $79.02 | 31,699,658 | Utilities | large | unknown | 2026-06-07 |
| XOM | $150.03 | 101,694,764 | Energy | large | unknown | 2026-06-07 |
| XPO | $218.59 | 22,702,756 | Unknown | mid | unknown | 2026-06-07 |
| XYZ | $68.14 | 20,578,365 | Unknown | large | unknown | 2026-06-07 |
| ZTS | $79.43 | 39,399,865 | Health Care | large | unknown | 2026-06-07 |
