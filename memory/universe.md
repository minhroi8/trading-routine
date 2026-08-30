---
screened_on: 2026-08-30
expires_on: 2026-09-06
total_passed: 259
total_rejected: 1276
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
| AAL | $13.63 | 22,842,225 | Industrials | mid | unknown | 2026-08-30 |
| AAPL | $319.58 | 424,778,561 | Information Technology | large | unknown | 2026-08-30 |
| ABBV | $255.56 | 52,322,939 | Health Care | large | unknown | 2026-08-30 |
| ABNB | $189.37 | 42,932,247 | Consumer Discretionary | large | unknown | 2026-08-30 |
| ABT | $112.42 | 41,779,496 | Health Care | large | unknown | 2026-08-30 |
| ACN | $189.59 | 40,344,276 | Information Technology | large | unknown | 2026-08-30 |
| ADBE | $291.55 | 44,211,936 | Information Technology | large | unknown | 2026-08-30 |
| ADI | $361.67 | 55,899,130 | Information Technology | large | unknown | 2026-08-30 |
| ADP | $287.38 | 24,329,377 | Industrials | large | unknown | 2026-08-30 |
| ADSK | $260.77 | 21,727,439 | Information Technology | large | unknown | 2026-08-30 |
| AKAM | $107.41 | 20,824,543 | Information Technology | large | unknown | 2026-08-30 |
| ALL | $260.78 | 24,735,710 | Unknown | large | unknown | 2026-08-30 |
| AMAT | $461.50 | 135,020,559 | Information Technology | large | unknown | 2026-08-30 |
| AMD | $465.61 | 266,946,577 | Information Technology | large | unknown | 2026-08-30 |
| AMGN | $432.46 | 36,657,192 | Health Care | large | unknown | 2026-08-30 |
| AMZN | $266.39 | 398,289,559 | Consumer Discretionary | large | unknown | 2026-08-30 |
| ANET | $195.44 | 73,708,550 | Information Technology | large | unknown | 2026-08-30 |
| APH | $157.72 | 48,425,280 | Information Technology | large | unknown | 2026-08-30 |
| APP | $317.88 | 84,385,805 | Unknown | large | unknown | 2026-08-30 |
| ATI | $210.66 | 24,384,717 | Materials | mid | unknown | 2026-08-30 |
| AVGO | $368.75 | 255,841,650 | Information Technology | large | unknown | 2026-08-30 |
| AXON | $600.80 | 26,638,269 | Industrials | large | unknown | 2026-08-30 |
| AXP | $333.10 | 34,659,276 | Unknown | large | unknown | 2026-08-30 |
| AZO | $2963.74 | 30,336,665 | Consumer Discretionary | large | unknown | 2026-08-30 |
| BA | $209.74 | 53,033,048 | Industrials | large | unknown | 2026-08-30 |
| BAC | $62.33 | 117,226,485 | Financials | large | unknown | 2026-08-30 |
| BKNG | $205.63 | 54,927,249 | Consumer Discretionary | large | unknown | 2026-08-30 |
| BKR | $62.41 | 25,100,900 | Unknown | large | unknown | 2026-08-30 |
| BLK | $1164.19 | 36,500,930 | Unknown | large | unknown | 2026-08-30 |
| BMY | $66.58 | 44,583,481 | Health Care | large | unknown | 2026-08-30 |
| BRK.B | $505.06 | 57,148,326 | Financials | large | unknown | 2026-08-30 |
| BSX | $46.83 | 83,585,573 | Health Care | large | unknown | 2026-08-30 |
| BURL | $273.06 | 26,058,699 | Unknown | mid | unknown | 2026-08-30 |
| BX | $142.39 | 27,406,680 | Financials | large | unknown | 2026-08-30 |
| C | $132.87 | 39,883,886 | Financials | large | unknown | 2026-08-30 |
| CAH | $234.58 | 20,774,664 | Unknown | large | unknown | 2026-08-30 |
| CAT | $799.67 | 97,086,837 | Industrials | large | unknown | 2026-08-30 |
| CB | $339.88 | 25,000,423 | Financials | large | unknown | 2026-08-30 |
| CCL | $24.75 | 27,972,237 | Unknown | large | unknown | 2026-08-30 |
| CDE | $21.14 | 25,049,371 | Unknown | mid | unknown | 2026-08-30 |
| CDNS | $340.40 | 38,832,184 | Unknown | large | unknown | 2026-08-30 |
| CEG | $276.84 | 29,175,000 | Unknown | large | unknown | 2026-08-30 |
| CHTR | $153.58 | 20,092,342 | Unknown | large | unknown | 2026-08-30 |
| CIEN | $377.98 | 42,909,074 | Unknown | large | unknown | 2026-08-30 |
| CMCSA | $27.05 | 37,824,649 | Unknown | large | unknown | 2026-08-30 |
| CME | $285.77 | 22,006,170 | Financials | large | unknown | 2026-08-30 |
| CMG | $38.03 | 47,068,149 | Consumer Discretionary | large | unknown | 2026-08-30 |
| CMI | $564.70 | 31,984,726 | Industrials | large | unknown | 2026-08-30 |
| COF | $215.67 | 26,941,588 | Financials | large | unknown | 2026-08-30 |
| COHR | $279.07 | 97,300,858 | Unknown | large | unknown | 2026-08-30 |
| COIN | $178.53 | 43,146,446 | Unknown | large | unknown | 2026-08-30 |
| COP | $130.42 | 48,017,867 | Energy | large | unknown | 2026-08-30 |
| COR | $322.02 | 26,582,588 | Unknown | large | unknown | 2026-08-30 |
| COST | $945.84 | 52,699,804 | Consumer Staples | large | unknown | 2026-08-30 |
| CPRT | $33.00 | 23,705,957 | Industrials | large | unknown | 2026-08-30 |
| CRH | $95.84 | 26,787,632 | Unknown | large | unknown | 2026-08-30 |
| CRM | $256.01 | 116,144,882 | Information Technology | large | unknown | 2026-08-30 |
| CRS | $476.46 | 20,476,732 | Materials | mid | unknown | 2026-08-30 |
| CRWD | $218.46 | 65,421,439 | Information Technology | large | unknown | 2026-08-30 |
| CSCO | $109.92 | 91,476,054 | Information Technology | large | unknown | 2026-08-30 |
| CSX | $51.28 | 30,034,678 | Industrials | large | unknown | 2026-08-30 |
| CTSH | $64.05 | 24,066,498 | Information Technology | large | unknown | 2026-08-30 |
| CVNA | $74.05 | 29,102,523 | Unknown | large | unknown | 2026-08-30 |
| CVS | $93.06 | 42,323,978 | Health Care | large | unknown | 2026-08-30 |
| CVX | $201.84 | 55,991,933 | Energy | large | unknown | 2026-08-30 |
| DASH | $236.68 | 52,190,106 | Unknown | large | unknown | 2026-08-30 |
| DDOG | $236.83 | 58,702,206 | Unknown | large | unknown | 2026-08-30 |
| DE | $630.82 | 39,155,991 | Industrials | large | unknown | 2026-08-30 |
| DELL | $455.96 | 89,429,745 | Information Technology | large | unknown | 2026-08-30 |
| DHR | $216.10 | 41,444,624 | Health Care | large | unknown | 2026-08-30 |
| DIS | $108.10 | 46,075,906 | Communication Services | large | unknown | 2026-08-30 |
| DKS | $135.10 | 30,271,823 | Consumer Discretionary | mid | unknown | 2026-08-30 |
| DT | $53.66 | 24,606,805 | Unknown | mid | unknown | 2026-08-30 |
| DUK | $120.22 | 22,494,889 | Utilities | large | unknown | 2026-08-30 |
| DVN | $47.35 | 32,667,952 | Energy | large | unknown | 2026-08-30 |
| DXCM | $90.80 | 20,082,066 | Health Care | large | unknown | 2026-08-30 |
| EBAY | $105.61 | 23,009,214 | Consumer Discretionary | large | unknown | 2026-08-30 |
| ECL | $286.82 | 23,300,299 | Materials | large | unknown | 2026-08-30 |
| EOG | $143.32 | 25,563,891 | Energy | large | unknown | 2026-08-30 |
| EQIX | $1044.56 | 32,682,098 | Real Estate | large | unknown | 2026-08-30 |
| EQT | $54.56 | 28,449,171 | Unknown | large | unknown | 2026-08-30 |
| ETN | $402.56 | 40,609,832 | Industrials | large | unknown | 2026-08-30 |
| EXPE | $329.35 | 26,690,020 | Consumer Discretionary | large | unknown | 2026-08-30 |
| F | $13.88 | 23,632,438 | Consumer Discretionary | large | unknown | 2026-08-30 |
| FCX | $76.45 | 58,841,176 | Materials | large | unknown | 2026-08-30 |
| FDX | $330.79 | 42,784,303 | Industrials | large | unknown | 2026-08-30 |
| FERG | $228.46 | 41,373,610 | Unknown | large | unknown | 2026-08-30 |
| FICO | $1153.54 | 22,868,888 | Information Technology | large | unknown | 2026-08-30 |
| FIS | $41.45 | 20,558,452 | Financials | large | unknown | 2026-08-30 |
| FISV | $53.17 | 20,911,069 | Unknown | large | unknown | 2026-08-30 |
| FITB | $54.53 | 20,396,226 | Financials | large | unknown | 2026-08-30 |
| FIX | $1518.38 | 37,151,980 | Unknown | large | unknown | 2026-08-30 |
| FN | $414.19 | 34,202,897 | Unknown | mid | unknown | 2026-08-30 |
| FSLR | $204.47 | 26,840,255 | Unknown | large | unknown | 2026-08-30 |
| FTNT | $165.97 | 28,595,723 | Information Technology | large | unknown | 2026-08-30 |
| GE | $342.60 | 51,487,624 | Industrials | large | unknown | 2026-08-30 |
| GEV | $911.91 | 90,677,320 | Industrials | large | unknown | 2026-08-30 |
| GILD | $145.67 | 32,125,880 | Health Care | large | unknown | 2026-08-30 |
| GIS | $41.55 | 21,165,390 | Consumer Staples | large | unknown | 2026-08-30 |
| GLW | $148.86 | 57,055,657 | Information Technology | large | unknown | 2026-08-30 |
| GOOG | $342.78 | 225,530,986 | Communication Services | large | unknown | 2026-08-30 |
| GOOGL | $346.61 | 313,242,683 | Communication Services | large | unknown | 2026-08-30 |
| GS | $1033.39 | 65,039,059 | Financials | large | unknown | 2026-08-30 |
| GWW | $1305.97 | 21,801,603 | Industrials | large | unknown | 2026-08-30 |
| HAL | $36.17 | 22,289,988 | Energy | large | unknown | 2026-08-30 |
| HCA | $417.85 | 24,957,850 | Health Care | large | unknown | 2026-08-30 |
| HD | $330.11 | 48,958,943 | Consumer Discretionary | large | unknown | 2026-08-30 |
| HL | $20.36 | 22,991,479 | Unknown | mid | unknown | 2026-08-30 |
| HLT | $321.90 | 31,896,596 | Consumer Discretionary | large | unknown | 2026-08-30 |
| HON | $217.44 | 25,047,936 | Industrials | large | unknown | 2026-08-30 |
| HONA | $162.35 | 39,067,850 | Unknown | large | unknown | 2026-08-30 |
| HOOD | $104.17 | 58,565,173 | Unknown | large | unknown | 2026-08-30 |
| HPE | $52.29 | 44,109,117 | Information Technology | large | unknown | 2026-08-30 |
| HPQ | $30.50 | 34,753,279 | Information Technology | large | unknown | 2026-08-30 |
| HUM | $385.64 | 22,775,680 | Health Care | large | unknown | 2026-08-30 |
| HWM | $264.65 | 29,367,503 | Industrials | large | unknown | 2026-08-30 |
| IBM | $235.52 | 45,585,393 | Information Technology | large | unknown | 2026-08-30 |
| ICE | $162.34 | 24,226,960 | Financials | large | unknown | 2026-08-30 |
| IDXX | $554.92 | 27,115,808 | Health Care | large | unknown | 2026-08-30 |
| ILMN | $215.65 | 28,043,948 | Health Care | mid | unknown | 2026-08-30 |
| INTC | $89.49 | 340,033,572 | Information Technology | large | unknown | 2026-08-30 |
| INTU | $358.07 | 68,866,149 | Information Technology | large | unknown | 2026-08-30 |
| ISRG | $372.55 | 48,234,103 | Health Care | large | unknown | 2026-08-30 |
| JCI | $139.60 | 24,102,292 | Industrials | large | unknown | 2026-08-30 |
| JNJ | $268.02 | 63,199,181 | Health Care | large | unknown | 2026-08-30 |
| JPM | $357.53 | 59,575,572 | Financials | large | unknown | 2026-08-30 |
| KDP | $32.17 | 24,189,032 | Consumer Staples | large | unknown | 2026-08-30 |
| KEYS | $319.60 | 26,657,889 | Information Technology | large | unknown | 2026-08-30 |
| KHC | $25.70 | 20,588,420 | Consumer Staples | large | unknown | 2026-08-30 |
| KKR | $108.67 | 26,576,546 | Unknown | large | unknown | 2026-08-30 |
| KLAC | $175.53 | 65,677,535 | Information Technology | large | unknown | 2026-08-30 |
| KMI | $31.55 | 22,811,458 | Energy | large | unknown | 2026-08-30 |
| KO | $89.64 | 74,434,125 | Consumer Staples | large | unknown | 2026-08-30 |
| KR | $57.72 | 23,130,004 | Consumer Staples | large | unknown | 2026-08-30 |
| KVUE | $19.16 | 22,265,104 | Unknown | large | unknown | 2026-08-30 |
| LHX | $262.78 | 21,487,854 | Industrials | large | unknown | 2026-08-30 |
| LIN | $489.49 | 39,658,838 | Materials | large | unknown | 2026-08-30 |
| LITE | $894.52 | 157,718,532 | Unknown | large | unknown | 2026-08-30 |
| LLY | $1173.85 | 137,726,160 | Health Care | large | unknown | 2026-08-30 |
| LMT | $563.95 | 21,646,538 | Industrials | large | unknown | 2026-08-30 |
| LOW | $208.10 | 28,944,825 | Consumer Discretionary | large | unknown | 2026-08-30 |
| LRCX | $301.78 | 104,668,634 | Information Technology | large | unknown | 2026-08-30 |
| MA | $595.22 | 77,345,945 | Financials | large | unknown | 2026-08-30 |
| MAR | $351.12 | 25,283,968 | Unknown | large | unknown | 2026-08-30 |
| MCD | $264.91 | 48,178,227 | Consumer Discretionary | large | unknown | 2026-08-30 |
| MCHP | $72.85 | 28,149,296 | Information Technology | large | unknown | 2026-08-30 |
| MCK | $894.35 | 42,378,723 | Health Care | large | unknown | 2026-08-30 |
| MDLZ | $62.35 | 29,864,529 | Consumer Staples | large | unknown | 2026-08-30 |
| MDT | $91.20 | 39,771,268 | Health Care | large | unknown | 2026-08-30 |
| META | $577.90 | 337,224,020 | Communication Services | large | unknown | 2026-08-30 |
| MKSI | $255.66 | 26,279,845 | Information Technology | mid | unknown | 2026-08-30 |
| MLM | $530.91 | 26,060,988 | Materials | large | unknown | 2026-08-30 |
| MMM | $174.32 | 20,544,073 | Industrials | large | unknown | 2026-08-30 |
| MNST | $46.85 | 25,630,628 | Consumer Staples | large | unknown | 2026-08-30 |
| MO | $68.67 | 40,287,688 | Consumer Staples | large | unknown | 2026-08-30 |
| MPC | $368.80 | 37,925,669 | Energy | large | unknown | 2026-08-30 |
| MPWR | $1255.66 | 40,545,337 | Information Technology | large | unknown | 2026-08-30 |
| MRK | $148.32 | 61,375,439 | Health Care | large | unknown | 2026-08-30 |
| MRNA | $137.93 | 87,111,501 | Health Care | large | unknown | 2026-08-30 |
| MRVL | $216.55 | 128,430,228 | Unknown | large | unknown | 2026-08-30 |
| MS | $214.75 | 40,189,561 | Financials | large | unknown | 2026-08-30 |
| MSFT | $513.67 | 402,504,068 | Information Technology | large | unknown | 2026-08-30 |
| MSI | $486.02 | 30,258,236 | Information Technology | large | unknown | 2026-08-30 |
| MTZ | $240.88 | 30,324,641 | Unknown | mid | unknown | 2026-08-30 |
| MU | $932.58 | 652,113,811 | Information Technology | large | unknown | 2026-08-30 |
| NEE | $81.81 | 53,700,886 | Utilities | large | unknown | 2026-08-30 |
| NEM | $127.93 | 37,330,038 | Materials | large | unknown | 2026-08-30 |
| NFLX | $81.73 | 133,793,462 | Communication Services | large | unknown | 2026-08-30 |
| NI | $40.58 | 21,724,206 | Utilities | large | unknown | 2026-08-30 |
| NKE | $39.59 | 53,974,627 | Consumer Discretionary | large | unknown | 2026-08-30 |
| NOW | $144.69 | 93,973,242 | Information Technology | large | unknown | 2026-08-30 |
| NTAP | $186.97 | 23,249,828 | Information Technology | large | unknown | 2026-08-30 |
| NUE | $250.51 | 20,365,046 | Materials | large | unknown | 2026-08-30 |
| NVDA | $217.54 | 852,461,084 | Information Technology | large | unknown | 2026-08-30 |
| NXPI | $223.47 | 32,267,016 | Unknown | large | unknown | 2026-08-30 |
| OKTA | $166.22 | 22,004,410 | Information Technology | mid | unknown | 2026-08-30 |
| ON | $72.59 | 27,826,190 | Information Technology | large | unknown | 2026-08-30 |
| ONTO | $270.67 | 25,455,421 | Information Technology | mid | unknown | 2026-08-30 |
| ORCL | $150.61 | 123,318,190 | Information Technology | large | unknown | 2026-08-30 |
| OXY | $59.09 | 32,057,977 | Energy | large | unknown | 2026-08-30 |
| PANW | $371.53 | 79,705,719 | Unknown | large | unknown | 2026-08-30 |
| PATH | $18.15 | 27,410,706 | Unknown | mid | unknown | 2026-08-30 |
| PCG | $16.61 | 37,184,483 | Utilities | large | unknown | 2026-08-30 |
| PEP | $141.03 | 28,886,486 | Consumer Staples | large | unknown | 2026-08-30 |
| PFE | $27.95 | 59,520,011 | Health Care | large | unknown | 2026-08-30 |
| PG | $143.72 | 57,639,872 | Consumer Staples | large | unknown | 2026-08-30 |
| PGR | $218.66 | 26,981,790 | Financials | large | unknown | 2026-08-30 |
| PH | $995.12 | 39,000,300 | Industrials | large | unknown | 2026-08-30 |
| PLD | $140.72 | 24,424,703 | Real Estate | large | unknown | 2026-08-30 |
| PLTR | $186.24 | 244,339,705 | Unknown | large | unknown | 2026-08-30 |
| PM | $191.94 | 33,951,343 | Consumer Staples | large | unknown | 2026-08-30 |
| PSX | $244.09 | 30,356,173 | Energy | large | unknown | 2026-08-30 |
| PWR | $602.51 | 45,451,662 | Industrials | large | unknown | 2026-08-30 |
| PYPL | $53.66 | 31,353,082 | Financials | large | unknown | 2026-08-30 |
| QCOM | $164.06 | 47,800,220 | Information Technology | large | unknown | 2026-08-30 |
| RCL | $279.42 | 25,814,939 | Consumer Discretionary | large | unknown | 2026-08-30 |
| RDDT | $152.91 | 37,718,319 | Unknown | large | unknown | 2026-08-30 |
| REGN | $793.96 | 22,768,152 | Health Care | large | unknown | 2026-08-30 |
| RMD | $240.24 | 20,036,863 | Health Care | large | unknown | 2026-08-30 |
| ROK | $430.68 | 23,471,602 | Industrials | large | unknown | 2026-08-30 |
| ROST | $228.45 | 40,312,294 | Consumer Discretionary | large | unknown | 2026-08-30 |
| RTX | $211.71 | 34,165,059 | Industrials | large | unknown | 2026-08-30 |
| SBUX | $107.86 | 21,460,922 | Consumer Discretionary | large | unknown | 2026-08-30 |
| SCHW | $110.12 | 44,307,069 | Financials | large | unknown | 2026-08-30 |
| SHW | $344.81 | 23,494,632 | Materials | large | unknown | 2026-08-30 |
| SLB | $57.32 | 33,651,865 | Energy | large | unknown | 2026-08-30 |
| SMCI | $37.08 | 77,713,774 | Information Technology | large | unknown | 2026-08-30 |
| SMTC | $131.15 | 25,956,201 | Information Technology | mid | unknown | 2026-08-30 |
| SNDK | $1484.30 | 474,761,570 | Unknown | large | unknown | 2026-08-30 |
| SNPS | $442.71 | 32,472,783 | Information Technology | large | unknown | 2026-08-30 |
| SO | $88.24 | 25,846,173 | Utilities | large | unknown | 2026-08-30 |
| SPGI | $442.86 | 39,395,319 | Financials | large | unknown | 2026-08-30 |
| STX | $829.61 | 149,359,768 | Information Technology | large | unknown | 2026-08-30 |
| SYK | $330.67 | 36,775,917 | Health Care | large | unknown | 2026-08-30 |
| T | $26.00 | 48,363,592 | Communication Services | large | unknown | 2026-08-30 |
| TDG | $1185.59 | 43,992,305 | Industrials | large | unknown | 2026-08-30 |
| TEL | $202.63 | 27,362,565 | Information Technology | large | unknown | 2026-08-30 |
| TER | $354.19 | 46,042,746 | Information Technology | large | unknown | 2026-08-30 |
| TGT | $163.20 | 36,323,187 | Consumer Discretionary | large | unknown | 2026-08-30 |
| TJX | $135.13 | 48,113,052 | Consumer Discretionary | large | unknown | 2026-08-30 |
| TMO | $622.14 | 61,407,558 | Health Care | large | unknown | 2026-08-30 |
| TMUS | $181.43 | 30,294,357 | Communication Services | large | unknown | 2026-08-30 |
| TOST | $35.15 | 24,502,170 | Unknown | mid | unknown | 2026-08-30 |
| TPR | $125.52 | 25,481,518 | Consumer Discretionary | large | unknown | 2026-08-30 |
| TRGP | $288.12 | 21,485,677 | Unknown | large | unknown | 2026-08-30 |
| TRV | $369.85 | 23,442,135 | Financials | large | unknown | 2026-08-30 |
| TSCO | $34.75 | 31,284,874 | Consumer Discretionary | large | unknown | 2026-08-30 |
| TSLA | $348.75 | 244,383,509 | Consumer Discretionary | large | unknown | 2026-08-30 |
| TT | $448.92 | 21,942,700 | Industrials | large | unknown | 2026-08-30 |
| TTMI | $118.64 | 21,617,994 | Information Technology | mid | unknown | 2026-08-30 |
| TTWO | $235.41 | 28,205,588 | Communication Services | large | unknown | 2026-08-30 |
| TWLO | $237.66 | 34,435,259 | Unknown | mid | unknown | 2026-08-30 |
| TXN | $258.58 | 59,782,236 | Information Technology | large | unknown | 2026-08-30 |
| UBER | $78.81 | 78,154,921 | Unknown | large | unknown | 2026-08-30 |
| ULTA | $517.57 | 20,949,032 | Consumer Discretionary | large | unknown | 2026-08-30 |
| UNH | $392.96 | 69,742,182 | Health Care | large | unknown | 2026-08-30 |
| UNP | $307.37 | 33,980,297 | Industrials | large | unknown | 2026-08-30 |
| URI | $1030.06 | 30,403,658 | Industrials | large | unknown | 2026-08-30 |
| USB | $62.46 | 24,163,729 | Financials | large | unknown | 2026-08-30 |
| V | $381.55 | 82,201,915 | Financials | large | unknown | 2026-08-30 |
| VEEV | $276.48 | 24,500,039 | Unknown | large | unknown | 2026-08-30 |
| VLO | $352.36 | 34,759,346 | Energy | large | unknown | 2026-08-30 |
| VRT | $256.84 | 57,936,050 | Unknown | large | unknown | 2026-08-30 |
| VRTX | $541.72 | 28,603,679 | Health Care | large | unknown | 2026-08-30 |
| VST | $137.10 | 28,826,136 | Utilities | large | unknown | 2026-08-30 |
| VZ | $50.08 | 53,475,555 | Communication Services | large | unknown | 2026-08-30 |
| WAT | $414.58 | 21,183,841 | Health Care | large | unknown | 2026-08-30 |
| WBD | $28.77 | 39,850,014 | Communication Services | large | unknown | 2026-08-30 |
| WDAY | $204.43 | 44,586,290 | Unknown | large | unknown | 2026-08-30 |
| WDC | $459.51 | 148,648,848 | Information Technology | large | unknown | 2026-08-30 |
| WELL | $237.85 | 28,261,501 | Real Estate | large | unknown | 2026-08-30 |
| WFC | $86.69 | 43,390,160 | Financials | large | unknown | 2026-08-30 |
| WM | $219.62 | 22,387,222 | Industrials | large | unknown | 2026-08-30 |
| WMB | $73.72 | 25,084,745 | Energy | large | unknown | 2026-08-30 |
| WMT | $103.10 | 116,273,160 | Consumer Staples | large | unknown | 2026-08-30 |
| XEL | $76.45 | 21,677,081 | Utilities | large | unknown | 2026-08-30 |
| XOM | $156.69 | 67,263,262 | Energy | large | unknown | 2026-08-30 |
| XYZ | $83.60 | 24,422,496 | Unknown | large | unknown | 2026-08-30 |
| ZTS | $77.36 | 22,315,540 | Health Care | large | unknown | 2026-08-30 |
