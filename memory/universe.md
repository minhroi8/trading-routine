---
screened_on: 2026-07-05
expires_on: 2026-07-12
total_passed: 313
total_rejected: 1186
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
| AA | $48.69 | $22,571,013 | Materials | mid | unknown | 2026-07-05 |
| AAL | $17.91 | $45,664,181 | Industrials | mid | unknown | 2026-07-05 |
| AAPL | $308.24 | $664,057,412 | Information Technology | large | unknown | 2026-07-05 |
| ABBV | $261.14 | $66,920,138 | Health Care | large | unknown | 2026-07-05 |
| ABNB | $148.98 | $24,785,683 | Consumer Discretionary | large | unknown | 2026-07-05 |
| ABT | $95.28 | $55,891,161 | Health Care | large | unknown | 2026-07-05 |
| ACN | $137.36 | $72,588,705 | Information Technology | large | unknown | 2026-07-05 |
| ADBE | $219.65 | $68,547,350 | Information Technology | large | unknown | 2026-07-05 |
| ADI | $377.44 | $88,654,359 | Information Technology | large | unknown | 2026-07-05 |
| ADP | $242.25 | $22,175,446 | Industrials | large | unknown | 2026-07-05 |
| ADSK | $207.45 | $31,354,989 | Information Technology | large | unknown | 2026-07-05 |
| AEIS | $311.20 | $21,117,771 | Information Technology | mid | unknown | 2026-07-05 |
| AEP | $138.54 | $26,797,544 | Utilities | large | unknown | 2026-07-05 |
| AJG | $252.11 | $26,514,005 | Financials | large | unknown | 2026-07-05 |
| AKAM | $113.23 | $26,171,751 | Information Technology | large | unknown | 2026-07-05 |
| AMAT | $603.33 | $295,469,902 | Information Technology | large | unknown | 2026-07-05 |
| AMD | $518.25 | $360,881,324 | Information Technology | large | unknown | 2026-07-05 |
| AMGN | $373.97 | $34,956,800 | Health Care | large | unknown | 2026-07-05 |
| AMKR | $69.67 | $22,675,680 | Information Technology | mid | unknown | 2026-07-05 |
| AMT | $165.99 | $28,311,328 | Real Estate | large | unknown | 2026-07-05 |
| AMZN | $242.30 | $633,202,500 | Consumer Discretionary | large | unknown | 2026-07-05 |
| ANET | $160.10 | $62,334,704 | Information Technology | large | unknown | 2026-07-05 |
| AON | $357.37 | $26,442,633 | Financials | large | unknown | 2026-07-05 |
| APD | $313.98 | $23,490,450 | Materials | large | unknown | 2026-07-05 |
| APH | $164.63 | $71,304,048 | Information Technology | large | unknown | 2026-07-05 |
| APO | $118.62 | $26,856,597 | Financials | large | unknown | 2026-07-05 |
| APP | $526.90 | $89,238,025 | Information Technology | large | unknown | 2026-07-05 |
| ATI | $188.08 | $20,639,215 | Industrials | mid | unknown | 2026-07-05 |
| AVGO | $360.50 | $392,628,422 | Information Technology | large | unknown | 2026-07-05 |
| AXON | $597.13 | $26,030,468 | Industrials | large | unknown | 2026-07-05 |
| AXP | $351.88 | $36,139,399 | Financials | large | unknown | 2026-07-05 |
| AZO | $3158.03 | $56,630,045 | Consumer Discretionary | large | unknown | 2026-07-05 |
| BA | $226.37 | $46,078,939 | Industrials | large | unknown | 2026-07-05 |
| BAC | $58.69 | $143,532,582 | Financials | large | unknown | 2026-07-05 |
| BKNG | $184.56 | $72,536,474 | Consumer Discretionary | large | unknown | 2026-07-05 |
| BKR | $52.78 | $31,659,653 | Energy | large | unknown | 2026-07-05 |
| BLD | $353.73 | $34,405,021 | Consumer Discretionary | mid | unknown | 2026-07-05 |
| BLK | $994.64 | $58,349,768 | Financials | large | unknown | 2026-07-05 |
| BMY | $58.11 | $44,031,107 | Health Care | large | unknown | 2026-07-05 |
| BRK.B | $507.45 | $69,029,527 | Financials | large | unknown | 2026-07-05 |
| BSX | $45.11 | $71,005,462 | Health Care | large | unknown | 2026-07-05 |
| BX | $122.82 | $27,691,782 | Financials | large | unknown | 2026-07-05 |
| C | $139.97 | $77,302,632 | Financials | large | unknown | 2026-07-05 |
| CAH | $238.75 | $26,306,400 | Health Care | large | unknown | 2026-07-05 |
| CARR | $70.08 | $23,385,375 | Industrials | large | unknown | 2026-07-05 |
| CAT | $963.60 | $144,305,611 | Industrials | large | unknown | 2026-07-05 |
| CB | $361.22 | $26,499,674 | Financials | large | unknown | 2026-07-05 |
| CBOE | $249.33 | $39,668,687 | Financials | large | unknown | 2026-07-05 |
| CCI | $76.57 | $22,832,439 | Real Estate | large | unknown | 2026-07-05 |
| CCL | $27.89 | $46,769,437 | Consumer Discretionary | large | unknown | 2026-07-05 |
| CDE | $17.30 | $29,597,942 | Materials | mid | unknown | 2026-07-05 |
| CDNS | $372.98 | $44,025,015 | Information Technology | large | unknown | 2026-07-05 |
| CEG | $239.20 | $52,774,841 | Utilities | large | unknown | 2026-07-05 |
| CFG | $70.99 | $24,879,671 | Financials | large | unknown | 2026-07-05 |
| CHTR | $137.21 | $24,917,568 | Communication Services | large | unknown | 2026-07-05 |
| CI | $287.58 | $20,472,253 | Health Care | large | unknown | 2026-07-05 |
| CL | $95.12 | $26,432,661 | Consumer Staples | large | unknown | 2026-07-05 |
| CMCSA | $23.76 | $67,621,856 | Communication Services | large | unknown | 2026-07-05 |
| CME | $236.72 | $59,770,221 | Financials | large | unknown | 2026-07-05 |
| CMG | $35.38 | $47,889,822 | Consumer Discretionary | large | unknown | 2026-07-05 |
| CMI | $661.50 | $39,536,470 | Industrials | large | unknown | 2026-07-05 |
| COF | $204.96 | $45,506,170 | Financials | large | unknown | 2026-07-05 |
| COIN | $165.44 | $40,335,116 | Financials | large | unknown | 2026-07-05 |
| COP | $104.75 | $57,613,738 | Energy | large | unknown | 2026-07-05 |
| COR | $296.68 | $25,372,896 | Health Care | large | unknown | 2026-07-05 |
| COST | $952.02 | $71,700,615 | Consumer Staples | large | unknown | 2026-07-05 |
| CPRT | $30.00 | $25,715,281 | Industrials | large | unknown | 2026-07-05 |
| CRH | $107.40 | $25,434,555 | Materials | large | unknown | 2026-07-05 |
| CRM | $166.14 | $89,543,053 | Information Technology | large | unknown | 2026-07-05 |
| CRS | $596.94 | $35,893,515 | Industrials | mid | unknown | 2026-07-05 |
| CRWD | $193.73 | $73,222,287 | Information Technology | large | unknown | 2026-07-05 |
| CSCO | $112.69 | $129,263,967 | Information Technology | large | unknown | 2026-07-05 |
| CSX | $48.87 | $45,081,172 | Industrials | large | unknown | 2026-07-05 |
| CTSH | $41.99 | $41,239,442 | Information Technology | large | unknown | 2026-07-05 |
| CVNA | $68.61 | $42,450,075 | Consumer Discretionary | large | unknown | 2026-07-05 |
| CVS | $104.72 | $44,410,740 | Health Care | large | unknown | 2026-07-05 |
| CVX | $169.13 | $58,811,285 | Energy | large | unknown | 2026-07-05 |
| D | $69.75 | $39,878,322 | Utilities | large | unknown | 2026-07-05 |
| DAL | $92.78 | $30,564,123 | Industrials | large | unknown | 2026-07-05 |
| DASH | $192.11 | $44,029,059 | Consumer Discretionary | large | unknown | 2026-07-05 |
| DDOG | $260.20 | $55,885,811 | Information Technology | large | unknown | 2026-07-05 |
| DE | $620.65 | $39,808,894 | Industrials | large | unknown | 2026-07-05 |
| DELL | $394.19 | $120,942,890 | Information Technology | large | unknown | 2026-07-05 |
| DHR | $197.87 | $38,045,374 | Health Care | large | unknown | 2026-07-05 |
| DIS | $99.43 | $50,535,042 | Communication Services | large | unknown | 2026-07-05 |
| DKS | $236.06 | $21,504,062 | Consumer Discretionary | mid | unknown | 2026-07-05 |
| DLR | $173.38 | $31,899,798 | Real Estate | large | unknown | 2026-07-05 |
| DOCN | $130.29 | $22,759,266 | Information Technology | mid | unknown | 2026-07-05 |
| DOW | $27.70 | $30,054,256 | Materials | large | unknown | 2026-07-05 |
| DRI | $204.34 | $22,356,940 | Consumer Discretionary | large | unknown | 2026-07-05 |
| DVN | $40.47 | $42,513,486 | Energy | large | unknown | 2026-07-05 |
| EA | $205.13 | $21,697,729 | Communication Services | large | unknown | 2026-07-05 |
| ECL | $283.32 | $21,691,119 | Materials | large | unknown | 2026-07-05 |
| EFX | $172.09 | $21,047,878 | Industrials | large | unknown | 2026-07-05 |
| ELV | $417.45 | $32,572,949 | Health Care | large | unknown | 2026-07-05 |
| EMR | $139.06 | $22,400,669 | Industrials | large | unknown | 2026-07-05 |
| ENTG | $146.49 | $35,486,445 | Information Technology | mid | unknown | 2026-07-05 |
| EOG | $130.84 | $25,881,780 | Energy | large | unknown | 2026-07-05 |
| EQIX | $1001.90 | $47,381,028 | Real Estate | large | unknown | 2026-07-05 |
| EQT | $52.60 | $30,814,429 | Energy | large | unknown | 2026-07-05 |
| ETN | $398.67 | $50,933,588 | Industrials | large | unknown | 2026-07-05 |
| EW | $94.38 | $21,746,780 | Health Care | large | unknown | 2026-07-05 |
| EXC | $47.87 | $27,123,418 | Utilities | large | unknown | 2026-07-05 |
| EXPE | $268.74 | $20,666,826 | Consumer Discretionary | large | unknown | 2026-07-05 |
| F | $13.35 | $32,140,309 | Consumer Discretionary | large | unknown | 2026-07-05 |
| FANG | $172.04 | $28,282,383 | Energy | large | unknown | 2026-07-05 |
| FAST | $48.58 | $21,444,744 | Industrials | large | unknown | 2026-07-05 |
| FCX | $60.95 | $65,908,160 | Materials | large | unknown | 2026-07-05 |
| FDX | $313.07 | $46,314,797 | Industrials | large | unknown | 2026-07-05 |
| FICO | $1270.41 | $22,347,074 | Information Technology | large | unknown | 2026-07-05 |
| FISV | $52.31 | $20,377,512 | Financials | large | unknown | 2026-07-05 |
| FITB | $57.15 | $33,323,503 | Financials | large | unknown | 2026-07-05 |
| FIX | $1739.58 | $55,770,688 | Industrials | large | unknown | 2026-07-05 |
| FN | $500.29 | $40,390,139 | Information Technology | mid | unknown | 2026-07-05 |
| FOXA | $56.47 | $26,597,372 | Communication Services | large | unknown | 2026-07-05 |
| FSLR | $224.55 | $26,245,506 | Information Technology | large | unknown | 2026-07-05 |
| FTNT | $156.21 | $36,606,090 | Information Technology | large | unknown | 2026-07-05 |
| GE | $377.49 | $73,169,003 | Industrials | large | unknown | 2026-07-05 |
| GEV | $1113.27 | $151,897,834 | Industrials | large | unknown | 2026-07-05 |
| GILD | $131.24 | $43,216,477 | Health Care | large | unknown | 2026-07-05 |
| GIS | $37.55 | $26,993,312 | Consumer Staples | large | unknown | 2026-07-05 |
| GLW | $196.68 | $138,425,566 | Information Technology | large | unknown | 2026-07-05 |
| GM | $75.98 | $32,980,579 | Consumer Discretionary | large | unknown | 2026-07-05 |
| GOOG | $356.03 | $230,805,723 | Communication Services | large | unknown | 2026-07-05 |
| GOOGL | $359.69 | $446,954,734 | Communication Services | large | unknown | 2026-07-05 |
| GS | $1020.89 | $83,103,515 | Financials | large | unknown | 2026-07-05 |
| GWW | $1342.77 | $28,743,424 | Industrials | large | unknown | 2026-07-05 |
| HAL | $32.94 | $33,037,345 | Energy | large | unknown | 2026-07-05 |
| HBAN | $17.87 | $22,463,777 | Financials | large | unknown | 2026-07-05 |
| HCA | $410.39 | $29,390,045 | Health Care | large | unknown | 2026-07-05 |
| HD | $357.78 | $69,799,985 | Consumer Discretionary | large | unknown | 2026-07-05 |
| HIMS | $36.79 | $20,417,591 | Health Care | mid | unknown | 2026-07-05 |
| HLT | $338.14 | $37,941,731 | Consumer Discretionary | large | unknown | 2026-07-05 |
| HON | $229.95 | $52,390,385 | Industrials | large | unknown | 2026-07-05 |
| HOOD | $112.71 | $98,642,129 | Financials | large | unknown | 2026-07-05 |
| HPE | $41.20 | $92,884,331 | Information Technology | large | unknown | 2026-07-05 |
| HPQ | $21.92 | $29,728,555 | Information Technology | large | unknown | 2026-07-05 |
| HSY | $182.13 | $22,516,519 | Consumer Staples | large | unknown | 2026-07-05 |
| HUBB | $486.76 | $27,415,984 | Industrials | large | unknown | 2026-07-05 |
| HUM | $396.25 | $29,713,797 | Health Care | large | unknown | 2026-07-05 |
| HWM | $270.55 | $49,521,150 | Industrials | large | unknown | 2026-07-05 |
| IBM | $289.22 | $79,583,726 | Information Technology | large | unknown | 2026-07-05 |
| ICE | $132.97 | $29,424,679 | Financials | large | unknown | 2026-07-05 |
| IDXX | $559.38 | $21,312,748 | Health Care | large | unknown | 2026-07-05 |
| INTC | $120.39 | $471,797,806 | Information Technology | large | unknown | 2026-07-05 |
| INTU | $275.36 | $102,384,307 | Information Technology | large | unknown | 2026-07-05 |
| ISRG | $426.00 | $46,273,996 | Health Care | large | unknown | 2026-07-05 |
| ITW | $272.70 | $20,896,454 | Industrials | large | unknown | 2026-07-05 |
| JBL | $341.35 | $32,746,045 | Information Technology | large | unknown | 2026-07-05 |
| JCI | $140.81 | $33,776,415 | Industrials | large | unknown | 2026-07-05 |
| JNJ | $263.04 | $75,581,515 | Health Care | large | unknown | 2026-07-05 |
| JPM | $334.26 | $92,170,188 | Financials | large | unknown | 2026-07-05 |
| KDP | $33.30 | $36,620,951 | Consumer Staples | large | unknown | 2026-07-05 |
| KEYS | $313.84 | $28,911,511 | Information Technology | large | unknown | 2026-07-05 |
| KHC | $25.37 | $21,629,522 | Consumer Staples | large | unknown | 2026-07-05 |
| KKR | $93.83 | $27,601,794 | Financials | large | unknown | 2026-07-05 |
| KLAC | $235.81 | $179,815,128 | Information Technology | large | unknown | 2026-07-05 |
| KMB | $114.67 | $20,097,492 | Consumer Staples | large | unknown | 2026-07-05 |
| KMI | $32.07 | $21,064,022 | Energy | large | unknown | 2026-07-05 |
| KNX | $76.33 | $27,073,850 | Industrials | mid | unknown | 2026-07-05 |
| KO | $83.96 | $103,778,963 | Consumer Staples | large | unknown | 2026-07-05 |
| KR | $58.23 | $25,718,337 | Consumer Staples | large | unknown | 2026-07-05 |
| KVUE | $19.81 | $30,520,032 | Consumer Staples | large | unknown | 2026-07-05 |
| LHX | $301.94 | $25,890,818 | Industrials | large | unknown | 2026-07-05 |
| LIN | $546.68 | $54,391,208 | Materials | large | unknown | 2026-07-05 |
| LLY | $1210.79 | $170,757,336 | Health Care | large | unknown | 2026-07-05 |
| LMT | $545.86 | $26,173,915 | Industrials | large | unknown | 2026-07-05 |
| LOW | $227.37 | $28,315,245 | Consumer Discretionary | large | unknown | 2026-07-05 |
| LRCX | $351.50 | $204,746,190 | Information Technology | large | unknown | 2026-07-05 |
| LSCC | $136.47 | $23,143,104 | Information Technology | mid | unknown | 2026-07-05 |
| LYV | $186.53 | $22,223,059 | Communication Services | large | unknown | 2026-07-05 |
| MA | $539.36 | $112,399,982 | Financials | large | unknown | 2026-07-05 |
| MAR | $372.94 | $37,144,389 | Consumer Discretionary | large | unknown | 2026-07-05 |
| MARA | $12.38 | $20,186,191 | Information Technology | small | unknown | 2026-07-05 |
| MCD | $280.39 | $51,742,887 | Consumer Discretionary | large | unknown | 2026-07-05 |
| MCHP | $84.64 | $44,839,471 | Information Technology | large | unknown | 2026-07-05 |
| MCK | $786.29 | $39,646,449 | Health Care | large | unknown | 2026-07-05 |
| MCO | $490.65 | $34,344,180 | Financials | large | unknown | 2026-07-05 |
| MDLZ | $60.88 | $42,829,037 | Consumer Staples | large | unknown | 2026-07-05 |
| MDT | $83.19 | $58,590,294 | Health Care | large | unknown | 2026-07-05 |
| META | $582.76 | $363,876,681 | Communication Services | large | unknown | 2026-07-05 |
| MKSI | $365.99 | $36,146,949 | Information Technology | mid | unknown | 2026-07-05 |
| MLM | $599.40 | $28,939,941 | Materials | large | unknown | 2026-07-05 |
| MMM | $160.42 | $25,776,914 | Industrials | large | unknown | 2026-07-05 |
| MNST | $97.66 | $24,641,585 | Consumer Staples | large | unknown | 2026-07-05 |
| MO | $72.72 | $31,895,063 | Consumer Staples | large | unknown | 2026-07-05 |
| MPC | $266.23 | $35,262,144 | Energy | large | unknown | 2026-07-05 |
| MPWR | $1289.34 | $70,460,793 | Information Technology | large | unknown | 2026-07-05 |
| MRK | $129.51 | $56,604,869 | Health Care | large | unknown | 2026-07-05 |
| MRSH | $178.38 | $21,223,271 | Financials | large | unknown | 2026-07-05 |
| MS | $213.89 | $63,892,271 | Financials | large | unknown | 2026-07-05 |
| MSCI | $603.24 | $29,068,506 | Financials | large | unknown | 2026-07-05 |
| MSFT | $389.79 | $480,861,072 | Information Technology | large | unknown | 2026-07-05 |
| MSI | $422.60 | $21,982,324 | Information Technology | large | unknown | 2026-07-05 |
| MTD | $1307.90 | $22,615,536 | Health Care | large | unknown | 2026-07-05 |
| MTSI | $322.01 | $30,715,976 | Information Technology | mid | unknown | 2026-07-05 |
| MTZ | $373.36 | $31,713,562 | Industrials | mid | unknown | 2026-07-05 |
| MU | $975.40 | $1,113,384,394 | Information Technology | large | unknown | 2026-07-05 |
| NCLH | $19.76 | $24,568,013 | Consumer Discretionary | large | unknown | 2026-07-05 |
| NEE | $88.36 | $74,397,418 | Utilities | large | unknown | 2026-07-05 |
| NEM | $97.05 | $47,554,394 | Materials | large | unknown | 2026-07-05 |
| NFLX | $77.59 | $270,301,875 | Communication Services | large | unknown | 2026-07-05 |
| NKE | $44.08 | $65,292,158 | Consumer Discretionary | large | unknown | 2026-07-05 |
| NOC | $548.20 | $32,724,015 | Industrials | large | unknown | 2026-07-05 |
| NOW | $106.16 | $107,281,229 | Information Technology | large | unknown | 2026-07-05 |
| NTAP | $154.11 | $24,628,702 | Information Technology | large | unknown | 2026-07-05 |
| NUE | $220.72 | $20,847,030 | Materials | large | unknown | 2026-07-05 |
| NVDA | $194.51 | $980,259,991 | Information Technology | large | unknown | 2026-07-05 |
| NVT | $152.24 | $20,286,861 | Industrials | mid | unknown | 2026-07-05 |
| NXPI | $273.50 | $51,509,286 | Information Technology | large | unknown | 2026-07-05 |
| NXT | $112.85 | $21,112,223 | Industrials | mid | unknown | 2026-07-05 |
| O | $63.83 | $25,146,889 | Real Estate | large | unknown | 2026-07-05 |
| ODFL | $217.81 | $25,057,873 | Industrials | large | unknown | 2026-07-05 |
| ON | $91.25 | $75,329,390 | Information Technology | large | unknown | 2026-07-05 |
| ONTO | $308.54 | $29,890,953 | Information Technology | mid | unknown | 2026-07-05 |
| ORCL | $140.29 | $167,319,568 | Information Technology | large | unknown | 2026-07-05 |
| ORLY | $90.22 | $32,740,943 | Consumer Discretionary | large | unknown | 2026-07-05 |
| OXY | $48.89 | $35,383,437 | Energy | large | unknown | 2026-07-05 |
| PANW | $347.88 | $79,681,893 | Information Technology | large | unknown | 2026-07-05 |
| PEP | $144.16 | $51,588,520 | Consumer Staples | large | unknown | 2026-07-05 |
| PFE | $24.31 | $65,140,385 | Health Care | large | unknown | 2026-07-05 |
| PG | $151.50 | $64,455,040 | Consumer Staples | large | unknown | 2026-07-05 |
| PGR | $232.25 | $34,559,419 | Financials | large | unknown | 2026-07-05 |
| PH | $962.90 | $42,543,215 | Industrials | large | unknown | 2026-07-05 |
| PINS | $22.07 | $25,643,588 | Communication Services | mid | unknown | 2026-07-05 |
| PLD | $139.46 | $22,610,238 | Real Estate | large | unknown | 2026-07-05 |
| PLTR | $129.18 | $146,866,784 | Information Technology | large | unknown | 2026-07-05 |
| PM | $182.33 | $34,802,473 | Consumer Staples | large | unknown | 2026-07-05 |
| PNC | $249.48 | $33,370,206 | Financials | large | unknown | 2026-07-05 |
| PPL | $36.88 | $25,880,162 | Utilities | large | unknown | 2026-07-05 |
| PRIM | $88.30 | $20,177,216 | Industrials | small | unknown | 2026-07-05 |
| PSX | $176.32 | $22,683,833 | Energy | large | unknown | 2026-07-05 |
| PWR | $667.89 | $57,992,038 | Industrials | large | unknown | 2026-07-05 |
| PYPL | $45.45 | $30,453,743 | Financials | large | unknown | 2026-07-05 |
| QCOM | $176.12 | $135,784,793 | Information Technology | large | unknown | 2026-07-05 |
| RCL | $296.35 | $47,386,853 | Consumer Discretionary | large | unknown | 2026-07-05 |
| REGN | $654.36 | $48,360,051 | Health Care | large | unknown | 2026-07-05 |
| ROK | $471.98 | $22,018,785 | Industrials | large | unknown | 2026-07-05 |
| ROKU | $142.46 | $53,352,982 | Communication Services | mid | unknown | 2026-07-05 |
| ROST | $213.36 | $31,781,695 | Consumer Discretionary | large | unknown | 2026-07-05 |
| RRX | $218.35 | $21,142,438 | Industrials | mid | unknown | 2026-07-05 |
| RTX | $199.22 | $39,826,597 | Industrials | large | unknown | 2026-07-05 |
| SBUX | $104.28 | $36,401,315 | Consumer Discretionary | large | unknown | 2026-07-05 |
| SCHW | $96.96 | $68,914,234 | Financials | large | unknown | 2026-07-05 |
| SHW | $352.05 | $41,130,110 | Materials | large | unknown | 2026-07-05 |
| SITM | $601.57 | $20,537,404 | Information Technology | mid | unknown | 2026-07-05 |
| SLB | $45.12 | $54,339,257 | Energy | large | unknown | 2026-07-05 |
| SMCI | $27.22 | $88,368,049 | Information Technology | large | unknown | 2026-07-05 |
| SMTC | $135.27 | $28,078,760 | Information Technology | mid | unknown | 2026-07-05 |
| SNDK | $1743.66 | $554,523,771 | Information Technology | large | unknown | 2026-07-05 |
| SNPS | $437.25 | $46,945,166 | Information Technology | large | unknown | 2026-07-05 |
| SO | $97.94 | $29,741,452 | Utilities | large | unknown | 2026-07-05 |
| SPG | $225.76 | $20,465,880 | Real Estate | large | unknown | 2026-07-05 |
| SPGI | $439.70 | $61,109,910 | Financials | large | unknown | 2026-07-05 |
| STRL | $700.19 | $37,269,068 | Industrials | mid | unknown | 2026-07-05 |
| STT | $170.64 | $20,443,942 | Financials | large | unknown | 2026-07-05 |
| STX | $820.58 | $194,387,130 | Information Technology | large | unknown | 2026-07-05 |
| STZ | $137.19 | $20,955,870 | Consumer Staples | large | unknown | 2026-07-05 |
| SYK | $326.57 | $51,218,959 | Health Care | large | unknown | 2026-07-05 |
| T | $20.57 | $93,600,642 | Communication Services | large | unknown | 2026-07-05 |
| TDG | $1349.80 | $40,264,498 | Industrials | large | unknown | 2026-07-05 |
| TECH | $70.83 | $24,142,003 | Health Care | large | unknown | 2026-07-05 |
| TEL | $197.53 | $34,787,452 | Information Technology | large | unknown | 2026-07-05 |
| TER | $369.03 | $82,472,445 | Information Technology | large | unknown | 2026-07-05 |
| TFC | $50.97 | $38,484,555 | Financials | large | unknown | 2026-07-05 |
| TGT | $130.25 | $29,673,269 | Consumer Staples | large | unknown | 2026-07-05 |
| TJX | $154.15 | $43,795,525 | Consumer Discretionary | large | unknown | 2026-07-05 |
| TLN | $365.20 | $24,421,007 | Utilities | mid | unknown | 2026-07-05 |
| TMO | $523.39 | $59,752,857 | Health Care | large | unknown | 2026-07-05 |
| TMUS | $177.50 | $45,302,295 | Communication Services | large | unknown | 2026-07-05 |
| TRGP | $258.90 | $21,000,764 | Energy | large | unknown | 2026-07-05 |
| TRV | $342.25 | $22,045,486 | Financials | large | unknown | 2026-07-05 |
| TSCO | $31.76 | $28,009,160 | Consumer Discretionary | large | unknown | 2026-07-05 |
| TSLA | $392.82 | $407,142,279 | Consumer Discretionary | large | unknown | 2026-07-05 |
| TT | $478.00 | $37,839,683 | Industrials | large | unknown | 2026-07-05 |
| TTD | $19.08 | $20,381,233 | Communication Services | large | unknown | 2026-07-05 |
| TTMI | $155.96 | $26,989,878 | Information Technology | mid | unknown | 2026-07-05 |
| TTWO | $254.99 | $31,007,984 | Communication Services | large | unknown | 2026-07-05 |
| TWLO | $208.91 | $25,706,480 | Information Technology | mid | unknown | 2026-07-05 |
| TXN | $293.10 | $126,428,995 | Information Technology | large | unknown | 2026-07-05 |
| TYL | $317.95 | $21,019,555 | Information Technology | large | unknown | 2026-07-05 |
| UAL | $133.34 | $31,471,395 | Industrials | large | unknown | 2026-07-05 |
| UBER | $74.45 | $105,332,919 | Industrials | large | unknown | 2026-07-05 |
| ULTA | $461.33 | $22,405,208 | Consumer Discretionary | large | unknown | 2026-07-05 |
| UNH | $424.95 | $111,121,894 | Health Care | large | unknown | 2026-07-05 |
| UNP | $282.22 | $33,217,593 | Industrials | large | unknown | 2026-07-05 |
| UPS | $110.67 | $21,772,085 | Industrials | large | unknown | 2026-07-05 |
| URI | $1098.64 | $32,625,279 | Industrials | large | unknown | 2026-07-05 |
| USB | $61.72 | $41,012,888 | Financials | large | unknown | 2026-07-05 |
| USFD | $104.30 | $20,990,400 | Consumer Staples | mid | unknown | 2026-07-05 |
| V | $361.65 | $122,494,098 | Financials | large | unknown | 2026-07-05 |
| VLO | $267.69 | $37,454,692 | Energy | large | unknown | 2026-07-05 |
| VMC | $303.36 | $29,600,709 | Materials | large | unknown | 2026-07-05 |
| VRSK | $188.32 | $29,179,516 | Industrials | large | unknown | 2026-07-05 |
| VRTX | $528.03 | $32,835,680 | Health Care | large | unknown | 2026-07-05 |
| VSH | $45.98 | $26,530,826 | Information Technology | small | unknown | 2026-07-05 |
| VST | $151.07 | $29,030,642 | Utilities | large | unknown | 2026-07-05 |
| VZ | $42.55 | $95,088,710 | Communication Services | large | unknown | 2026-07-05 |
| WAT | $379.44 | $26,288,823 | Health Care | large | unknown | 2026-07-05 |
| WBD | $26.45 | $53,115,106 | Communication Services | large | unknown | 2026-07-05 |
| WDAY | $135.34 | $29,266,751 | Information Technology | large | unknown | 2026-07-05 |
| WDC | $538.79 | $229,720,067 | Information Technology | large | unknown | 2026-07-05 |
| WELL | $235.91 | $37,155,451 | Real Estate | large | unknown | 2026-07-05 |
| WFC | $85.51 | $98,538,600 | Financials | large | unknown | 2026-07-05 |
| WM | $230.40 | $23,554,310 | Industrials | large | unknown | 2026-07-05 |
| WMB | $73.15 | $30,438,385 | Energy | large | unknown | 2026-07-05 |
| WMT | $111.72 | $122,445,668 | Consumer Staples | large | unknown | 2026-07-05 |
| WSM | $227.50 | $20,496,850 | Consumer Discretionary | large | unknown | 2026-07-05 |
| WWD | $418.15 | $28,868,376 | Industrials | mid | unknown | 2026-07-05 |
| XEL | $81.93 | $26,366,565 | Utilities | large | unknown | 2026-07-05 |
| XOM | $136.97 | $77,827,754 | Energy | large | unknown | 2026-07-05 |
| XPO | $206.36 | $22,260,854 | Industrials | mid | unknown | 2026-07-05 |
| ZTS | $74.80 | $21,591,486 | Health Care | large | unknown | 2026-07-05 |
