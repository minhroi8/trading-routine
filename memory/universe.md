---
screened_on: 2026-08-16
expires_on: 2026-08-23
total_passed: 294
total_rejected: 1210
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
| AAL | $14.82 | 32,502,452 | Industrials | mid | unknown | 2026-08-16 |
| AAPL | $305.94 | 593,839,592 | Information Technology | large | unknown | 2026-08-16 |
| ABBV | $249.34 | 63,960,895 | Health Care | large | unknown | 2026-08-16 |
| ABNB | $184.04 | 37,044,875 | Consumer Discretionary | large | unknown | 2026-08-16 |
| ABT | $111.26 | 53,814,043 | Health Care | large | unknown | 2026-08-16 |
| ACN | $176.96 | 55,834,345 | Information Technology | large | unknown | 2026-08-16 |
| ADBE | $264.03 | 55,440,380 | Information Technology | large | unknown | 2026-08-16 |
| ADI | $389.43 | 56,948,362 | Information Technology | large | unknown | 2026-08-16 |
| ADP | $272.95 | 30,915,973 | Industrials | large | unknown | 2026-08-16 |
| ADSK | $251.61 | 24,125,537 | Information Technology | large | unknown | 2026-08-16 |
| AEP | $125.56 | 22,291,762 | Utilities | large | unknown | 2026-08-16 |
| AKAM | $124.98 | 24,516,674 | Information Technology | large | unknown | 2026-08-16 |
| ALL | $261.32 | 21,711,091 | Unknown | large | unknown | 2026-08-16 |
| AMAT | $507.12 | 173,055,103 | Information Technology | large | unknown | 2026-08-16 |
| AMD | $514.39 | 378,758,742 | Information Technology | large | unknown | 2026-08-16 |
| AMGN | $415.16 | 36,060,693 | Health Care | large | unknown | 2026-08-16 |
| AMT | $175.66 | 27,049,243 | Real Estate | large | unknown | 2026-08-16 |
| AMZN | $262.64 | 544,647,075 | Consumer Discretionary | large | unknown | 2026-08-16 |
| ANET | $198.72 | 80,728,261 | Information Technology | large | unknown | 2026-08-16 |
| AON | $355.78 | 21,963,111 | Financials | large | unknown | 2026-08-16 |
| APH | $166.98 | 57,457,840 | Information Technology | large | unknown | 2026-08-16 |
| APO | $140.72 | 23,878,514 | Financials | large | unknown | 2026-08-16 |
| APP | $315.52 | 94,355,860 | Unknown | large | unknown | 2026-08-16 |
| ATI | $228.44 | 21,584,722 | Materials | mid | unknown | 2026-08-16 |
| AVGO | $393.02 | 221,143,523 | Information Technology | large | unknown | 2026-08-16 |
| AXON | $613.15 | 26,503,432 | Industrials | large | unknown | 2026-08-16 |
| AXP | $342.51 | 44,123,337 | Unknown | large | unknown | 2026-08-16 |
| AZO | $3025.71 | 31,193,455 | Consumer Discretionary | large | unknown | 2026-08-16 |
| BA | $231.70 | 61,508,671 | Industrials | large | unknown | 2026-08-16 |
| BAC | $64.48 | 130,725,452 | Financials | large | unknown | 2026-08-16 |
| BKNG | $212.09 | 60,434,115 | Consumer Discretionary | large | unknown | 2026-08-16 |
| BKR | $64.82 | 32,533,996 | Unknown | large | unknown | 2026-08-16 |
| BLK | $1173.65 | 49,493,204 | Unknown | large | unknown | 2026-08-16 |
| BMY | $63.84 | 51,168,095 | Health Care | large | unknown | 2026-08-16 |
| BNY | $163.11 | 20,525,592 | Unknown | large | unknown | 2026-08-16 |
| BRK.B | $503.95 | 59,504,399 | Financials | large | unknown | 2026-08-16 |
| BSX | $51.83 | 74,818,035 | Health Care | large | unknown | 2026-08-16 |
| BX | $143.95 | 35,752,312 | Financials | large | unknown | 2026-08-16 |
| C | $139.32 | 51,327,145 | Financials | large | unknown | 2026-08-16 |
| CAH | $235.15 | 22,394,945 | Unknown | large | unknown | 2026-08-16 |
| CARR | $62.77 | 25,773,052 | Unknown | large | unknown | 2026-08-16 |
| CAT | $857.10 | 119,874,420 | Industrials | large | unknown | 2026-08-16 |
| CB | $343.63 | 32,757,665 | Financials | large | unknown | 2026-08-16 |
| CCL | $28.12 | 29,333,540 | Unknown | large | unknown | 2026-08-16 |
| CDE | $18.82 | 20,019,370 | Unknown | mid | unknown | 2026-08-16 |
| CDNS | $324.83 | 49,427,758 | Unknown | large | unknown | 2026-08-16 |
| CEG | $282.49 | 39,945,355 | Unknown | large | unknown | 2026-08-16 |
| CHRW | $148.45 | 26,467,277 | Industrials | large | unknown | 2026-08-16 |
| CHTR | $154.27 | 22,629,689 | Unknown | large | unknown | 2026-08-16 |
| CI | $282.31 | 28,195,065 | Health Care | large | unknown | 2026-08-16 |
| CIEN | $428.57 | 46,905,978 | Unknown | large | unknown | 2026-08-16 |
| CL | $91.92 | 22,318,950 | Consumer Staples | large | unknown | 2026-08-16 |
| CMCSA | $26.20 | 46,079,511 | Unknown | large | unknown | 2026-08-16 |
| CME | $269.78 | 32,734,017 | Financials | large | unknown | 2026-08-16 |
| CMG | $33.51 | 51,125,925 | Consumer Discretionary | large | unknown | 2026-08-16 |
| CMI | $631.42 | 37,893,813 | Industrials | large | unknown | 2026-08-16 |
| CNP | $40.83 | 20,980,504 | Unknown | large | unknown | 2026-08-16 |
| COF | $227.26 | 38,393,328 | Financials | large | unknown | 2026-08-16 |
| COHR | $325.86 | 96,900,907 | Unknown | large | unknown | 2026-08-16 |
| COIN | $148.45 | 35,613,226 | Unknown | large | unknown | 2026-08-16 |
| COP | $126.78 | 45,317,511 | Energy | large | unknown | 2026-08-16 |
| COR | $313.91 | 27,306,122 | Unknown | large | unknown | 2026-08-16 |
| COST | $960.84 | 59,435,514 | Consumer Staples | large | unknown | 2026-08-16 |
| CPRT | $31.61 | 25,636,266 | Industrials | large | unknown | 2026-08-16 |
| CRH | $97.14 | 29,996,929 | Unknown | large | unknown | 2026-08-16 |
| CRM | $196.19 | 85,891,454 | Information Technology | large | unknown | 2026-08-16 |
| CRS | $544.57 | 25,957,561 | Materials | mid | unknown | 2026-08-16 |
| CRWD | $216.93 | 51,898,358 | Information Technology | large | unknown | 2026-08-16 |
| CSCO | $111.68 | 109,185,144 | Information Technology | large | unknown | 2026-08-16 |
| CSX | $50.17 | 46,747,770 | Industrials | large | unknown | 2026-08-16 |
| CTAS | $199.50 | 20,357,118 | Industrials | large | unknown | 2026-08-16 |
| CTSH | $58.80 | 32,286,993 | Information Technology | large | unknown | 2026-08-16 |
| CVNA | $75.60 | 38,291,989 | Unknown | large | unknown | 2026-08-16 |
| CVS | $97.17 | 48,167,146 | Health Care | large | unknown | 2026-08-16 |
| CVX | $200.02 | 56,021,291 | Energy | large | unknown | 2026-08-16 |
| D | $68.78 | 23,298,267 | Utilities | large | unknown | 2026-08-16 |
| DAL | $89.36 | 23,067,838 | Industrials | large | unknown | 2026-08-16 |
| DASH | $216.97 | 48,323,025 | Unknown | large | unknown | 2026-08-16 |
| DDOG | $255.37 | 66,722,854 | Unknown | large | unknown | 2026-08-16 |
| DE | $608.71 | 32,612,376 | Industrials | large | unknown | 2026-08-16 |
| DELL | $490.97 | 101,222,534 | Information Technology | large | unknown | 2026-08-16 |
| DHR | $202.41 | 87,000,060 | Health Care | large | unknown | 2026-08-16 |
| DIS | $106.88 | 57,808,162 | Communication Services | large | unknown | 2026-08-16 |
| DLR | $200.11 | 30,118,963 | Unknown | large | unknown | 2026-08-16 |
| DOCN | $129.93 | 23,112,691 | Unknown | mid | unknown | 2026-08-16 |
| DOW | $31.08 | 21,975,427 | Materials | large | unknown | 2026-08-16 |
| DT | $49.16 | 20,125,125 | Unknown | mid | unknown | 2026-08-16 |
| DUK | $123.92 | 24,706,806 | Utilities | large | unknown | 2026-08-16 |
| DVN | $45.84 | 32,501,411 | Energy | large | unknown | 2026-08-16 |
| DXCM | $89.80 | 23,718,081 | Health Care | large | unknown | 2026-08-16 |
| EBAY | $103.09 | 22,397,252 | Consumer Discretionary | large | unknown | 2026-08-16 |
| ECHO | $91.87 | 20,591,960 | Unknown | large | unknown | 2026-08-16 |
| EFX | $180.85 | 21,293,671 | Industrials | large | unknown | 2026-08-16 |
| ELV | $400.25 | 20,383,579 | Unknown | large | unknown | 2026-08-16 |
| EME | $836.66 | 21,837,612 | Unknown | large | unknown | 2026-08-16 |
| EMR | $163.16 | 24,440,420 | Industrials | large | unknown | 2026-08-16 |
| EOG | $142.62 | 25,939,185 | Energy | large | unknown | 2026-08-16 |
| EQIX | $1102.06 | 41,502,097 | Real Estate | large | unknown | 2026-08-16 |
| EQT | $54.42 | 30,285,326 | Unknown | large | unknown | 2026-08-16 |
| ETN | $451.48 | 50,536,030 | Industrials | large | unknown | 2026-08-16 |
| EW | $91.54 | 23,604,688 | Health Care | large | unknown | 2026-08-16 |
| EXC | $45.87 | 22,748,786 | Utilities | large | unknown | 2026-08-16 |
| EXPE | $332.73 | 26,790,827 | Consumer Discretionary | large | unknown | 2026-08-16 |
| F | $14.37 | 33,936,301 | Consumer Discretionary | large | unknown | 2026-08-16 |
| FAST | $51.03 | 24,414,246 | Industrials | large | unknown | 2026-08-16 |
| FCX | $66.45 | 56,386,076 | Materials | large | unknown | 2026-08-16 |
| FDX | $334.68 | 26,453,833 | Industrials | large | unknown | 2026-08-16 |
| FERG | $245.21 | 43,275,022 | Unknown | large | unknown | 2026-08-16 |
| FICO | $1085.48 | 31,199,152 | Information Technology | large | unknown | 2026-08-16 |
| FIS | $42.91 | 23,246,445 | Financials | large | unknown | 2026-08-16 |
| FISV | $54.38 | 23,181,622 | Unknown | large | unknown | 2026-08-16 |
| FITB | $58.03 | 24,498,555 | Financials | large | unknown | 2026-08-16 |
| FIX | $1774.51 | 49,081,339 | Unknown | large | unknown | 2026-08-16 |
| FLEX | $126.20 | 27,749,516 | Unknown | large | unknown | 2026-08-16 |
| FN | $570.11 | 32,854,014 | Unknown | mid | unknown | 2026-08-16 |
| FSLR | $225.64 | 29,000,137 | Unknown | large | unknown | 2026-08-16 |
| FTNT | $159.97 | 34,968,744 | Information Technology | large | unknown | 2026-08-16 |
| GE | $368.30 | 53,667,952 | Industrials | large | unknown | 2026-08-16 |
| GEV | $1063.00 | 119,524,738 | Industrials | large | unknown | 2026-08-16 |
| GILD | $138.36 | 35,362,472 | Health Care | large | unknown | 2026-08-16 |
| GIS | $39.19 | 23,356,114 | Consumer Staples | large | unknown | 2026-08-16 |
| GLW | $165.99 | 86,961,232 | Information Technology | large | unknown | 2026-08-16 |
| GM | $86.75 | 23,870,571 | Consumer Discretionary | large | unknown | 2026-08-16 |
| GOOG | $343.52 | 239,180,967 | Communication Services | large | unknown | 2026-08-16 |
| GOOGL | $345.86 | 404,889,649 | Communication Services | large | unknown | 2026-08-16 |
| GS | $1038.99 | 69,308,308 | Financials | large | unknown | 2026-08-16 |
| GWW | $1322.53 | 24,817,650 | Industrials | large | unknown | 2026-08-16 |
| HAL | $34.42 | 28,118,364 | Energy | large | unknown | 2026-08-16 |
| HBAN | $17.91 | 25,600,639 | Financials | large | unknown | 2026-08-16 |
| HCA | $404.67 | 35,116,010 | Health Care | large | unknown | 2026-08-16 |
| HD | $338.80 | 54,487,744 | Consumer Discretionary | large | unknown | 2026-08-16 |
| HL | $18.37 | 20,143,032 | Unknown | mid | unknown | 2026-08-16 |
| HLT | $327.27 | 38,393,062 | Consumer Discretionary | large | unknown | 2026-08-16 |
| HON | $233.81 | 32,618,707 | Industrials | large | unknown | 2026-08-16 |
| HONA | $166.24 | 36,242,136 | Unknown | large | unknown | 2026-08-16 |
| HOOD | $95.54 | 57,311,300 | Unknown | large | unknown | 2026-08-16 |
| HPE | $58.70 | 44,888,628 | Information Technology | large | unknown | 2026-08-16 |
| HPQ | $30.10 | 30,799,305 | Information Technology | large | unknown | 2026-08-16 |
| HUBB | $511.83 | 23,051,086 | Industrials | large | unknown | 2026-08-16 |
| HUM | $389.25 | 27,949,231 | Health Care | large | unknown | 2026-08-16 |
| HWM | $289.22 | 29,335,909 | Industrials | large | unknown | 2026-08-16 |
| IBKR | $92.06 | 21,603,638 | Unknown | large | unknown | 2026-08-16 |
| IBM | $234.43 | 76,775,361 | Information Technology | large | unknown | 2026-08-16 |
| ICE | $154.69 | 32,328,382 | Financials | large | unknown | 2026-08-16 |
| IDXX | $551.03 | 27,494,745 | Health Care | large | unknown | 2026-08-16 |
| ILMN | $190.81 | 25,340,609 | Health Care | mid | unknown | 2026-08-16 |
| INTC | $102.53 | 361,992,413 | Information Technology | large | unknown | 2026-08-16 |
| INTU | $345.69 | 70,786,392 | Information Technology | large | unknown | 2026-08-16 |
| IQV | $236.69 | 22,323,023 | Health Care | large | unknown | 2026-08-16 |
| IR | $83.33 | 20,539,448 | Industrials | large | unknown | 2026-08-16 |
| ISRG | $394.48 | 68,094,067 | Health Care | large | unknown | 2026-08-16 |
| JCI | $153.62 | 24,775,666 | Industrials | large | unknown | 2026-08-16 |
| JNJ | $260.31 | 82,357,122 | Health Care | large | unknown | 2026-08-16 |
| JPM | $362.82 | 74,669,554 | Financials | large | unknown | 2026-08-16 |
| KDP | $31.45 | 26,719,620 | Consumer Staples | large | unknown | 2026-08-16 |
| KEYS | $357.76 | 23,065,631 | Information Technology | large | unknown | 2026-08-16 |
| KHC | $25.52 | 24,706,334 | Consumer Staples | large | unknown | 2026-08-16 |
| KKR | $114.02 | 26,958,743 | Unknown | large | unknown | 2026-08-16 |
| KLAC | $203.68 | 98,742,531 | Information Technology | large | unknown | 2026-08-16 |
| KO | $87.71 | 89,460,488 | Consumer Staples | large | unknown | 2026-08-16 |
| KR | $56.69 | 23,127,534 | Consumer Staples | large | unknown | 2026-08-16 |
| LHX | $291.71 | 25,042,050 | Industrials | large | unknown | 2026-08-16 |
| LII | $421.94 | 23,725,482 | Unknown | large | unknown | 2026-08-16 |
| LIN | $482.62 | 49,700,975 | Materials | large | unknown | 2026-08-16 |
| LITE | $925.91 | 163,397,285 | Unknown | large | unknown | 2026-08-16 |
| LLY | $1180.33 | 129,374,965 | Health Care | large | unknown | 2026-08-16 |
| LMT | $608.51 | 30,729,888 | Industrials | large | unknown | 2026-08-16 |
| LOW | $218.41 | 26,165,434 | Consumer Discretionary | large | unknown | 2026-08-16 |
| LRCX | $332.44 | 130,201,512 | Information Technology | large | unknown | 2026-08-16 |
| LYV | $188.38 | 20,500,704 | Communication Services | large | unknown | 2026-08-16 |
| MA | $569.20 | 93,728,874 | Financials | large | unknown | 2026-08-16 |
| MAR | $356.69 | 30,976,228 | Unknown | large | unknown | 2026-08-16 |
| MCD | $272.82 | 51,801,427 | Consumer Discretionary | large | unknown | 2026-08-16 |
| MCHP | $79.20 | 34,099,992 | Information Technology | large | unknown | 2026-08-16 |
| MCK | $868.89 | 44,130,699 | Health Care | large | unknown | 2026-08-16 |
| MCO | $484.69 | 25,813,949 | Financials | large | unknown | 2026-08-16 |
| MDLZ | $63.62 | 37,605,137 | Consumer Staples | large | unknown | 2026-08-16 |
| MDT | $91.25 | 41,393,169 | Health Care | large | unknown | 2026-08-16 |
| META | $589.76 | 363,049,223 | Communication Services | large | unknown | 2026-08-16 |
| MKSI | $310.69 | 32,943,487 | Information Technology | mid | unknown | 2026-08-16 |
| MLM | $548.48 | 24,153,095 | Materials | large | unknown | 2026-08-16 |
| MMM | $182.54 | 31,987,964 | Industrials | large | unknown | 2026-08-16 |
| MNST | $46.84 | 26,554,832 | Consumer Staples | large | unknown | 2026-08-16 |
| MO | $65.69 | 40,351,327 | Consumer Staples | large | unknown | 2026-08-16 |
| MPC | $355.48 | 37,917,263 | Energy | large | unknown | 2026-08-16 |
| MPWR | $1403.83 | 63,386,745 | Information Technology | large | unknown | 2026-08-16 |
| MRK | $135.84 | 37,770,414 | Health Care | large | unknown | 2026-08-16 |
| MRSH | $187.63 | 20,534,586 | Unknown | large | unknown | 2026-08-16 |
| MRVL | $222.13 | 110,433,718 | Unknown | large | unknown | 2026-08-16 |
| MS | $217.34 | 55,115,121 | Financials | large | unknown | 2026-08-16 |
| MSCI | $569.10 | 35,640,157 | Financials | large | unknown | 2026-08-16 |
| MSFT | $495.35 | 599,357,557 | Information Technology | large | unknown | 2026-08-16 |
| MSI | $466.78 | 20,356,867 | Information Technology | large | unknown | 2026-08-16 |
| MTD | $1418.60 | 20,256,489 | Health Care | large | unknown | 2026-08-16 |
| MTZ | $297.73 | 32,412,044 | Unknown | mid | unknown | 2026-08-16 |
| MU | $971.98 | 944,537,357 | Information Technology | large | unknown | 2026-08-16 |
| NEE | $86.20 | 56,576,535 | Utilities | large | unknown | 2026-08-16 |
| NEM | $117.74 | 32,003,475 | Materials | large | unknown | 2026-08-16 |
| NFLX | $78.17 | 184,660,461 | Communication Services | large | unknown | 2026-08-16 |
| NKE | $40.73 | 46,616,543 | Consumer Discretionary | large | unknown | 2026-08-16 |
| NOC | $585.66 | 26,528,636 | Industrials | large | unknown | 2026-08-16 |
| NOW | $124.03 | 118,557,178 | Information Technology | large | unknown | 2026-08-16 |
| NTAP | $207.10 | 21,468,954 | Information Technology | large | unknown | 2026-08-16 |
| NVDA | $225.16 | 933,310,602 | Information Technology | large | unknown | 2026-08-16 |
| NXPI | $234.66 | 50,174,252 | Unknown | large | unknown | 2026-08-16 |
| ODFL | $210.82 | 21,228,254 | Industrials | large | unknown | 2026-08-16 |
| ON | $82.64 | 32,324,592 | Information Technology | large | unknown | 2026-08-16 |
| ONTO | $331.58 | 24,722,031 | Information Technology | mid | unknown | 2026-08-16 |
| ORCL | $150.33 | 146,404,218 | Information Technology | large | unknown | 2026-08-16 |
| ORLY | $91.05 | 30,081,275 | Consumer Discretionary | large | unknown | 2026-08-16 |
| OXY | $58.37 | 33,297,785 | Energy | large | unknown | 2026-08-16 |
| PANW | $384.24 | 95,149,691 | Unknown | large | unknown | 2026-08-16 |
| PATH | $16.02 | 28,116,753 | Unknown | mid | unknown | 2026-08-16 |
| PCAR | $130.79 | 24,453,296 | Industrials | large | unknown | 2026-08-16 |
| PCG | $17.84 | 30,887,909 | Utilities | large | unknown | 2026-08-16 |
| PEP | $140.79 | 33,478,087 | Consumer Staples | large | unknown | 2026-08-16 |
| PFE | $26.79 | 56,386,787 | Health Care | large | unknown | 2026-08-16 |
| PG | $144.56 | 56,767,837 | Consumer Staples | large | unknown | 2026-08-16 |
| PGR | $209.38 | 27,071,056 | Financials | large | unknown | 2026-08-16 |
| PH | $1055.78 | 41,997,381 | Industrials | large | unknown | 2026-08-16 |
| PINS | $24.05 | 20,306,956 | Unknown | mid | unknown | 2026-08-16 |
| PLD | $140.99 | 33,099,210 | Real Estate | large | unknown | 2026-08-16 |
| PLTR | $174.02 | 217,506,319 | Unknown | large | unknown | 2026-08-16 |
| PM | $190.34 | 45,843,603 | Consumer Staples | large | unknown | 2026-08-16 |
| PSX | $233.62 | 29,309,115 | Energy | large | unknown | 2026-08-16 |
| PWR | $685.42 | 47,945,347 | Industrials | large | unknown | 2026-08-16 |
| PYPL | $61.64 | 37,093,919 | Financials | large | unknown | 2026-08-16 |
| QCOM | $165.84 | 72,282,113 | Information Technology | large | unknown | 2026-08-16 |
| RCL | $305.02 | 38,914,824 | Consumer Discretionary | large | unknown | 2026-08-16 |
| REGN | $803.52 | 36,809,984 | Health Care | large | unknown | 2026-08-16 |
| ROK | $449.28 | 26,649,307 | Industrials | large | unknown | 2026-08-16 |
| ROST | $245.38 | 28,037,253 | Consumer Discretionary | large | unknown | 2026-08-16 |
| RTX | $222.96 | 47,508,601 | Industrials | large | unknown | 2026-08-16 |
| SBUX | $107.67 | 29,942,607 | Consumer Discretionary | large | unknown | 2026-08-16 |
| SCHW | $111.09 | 43,403,354 | Financials | large | unknown | 2026-08-16 |
| SHW | $358.93 | 35,115,844 | Materials | large | unknown | 2026-08-16 |
| SLB | $53.76 | 41,703,310 | Energy | large | unknown | 2026-08-16 |
| SMCI | $39.85 | 78,209,240 | Information Technology | large | unknown | 2026-08-16 |
| SNDK | $1641.28 | 565,407,643 | Unknown | large | unknown | 2026-08-16 |
| SNPS | $421.44 | 36,748,472 | Information Technology | large | unknown | 2026-08-16 |
| SO | $92.81 | 23,992,761 | Utilities | large | unknown | 2026-08-16 |
| SPGI | $418.72 | 51,101,438 | Financials | large | unknown | 2026-08-16 |
| STRL | $576.34 | 29,435,932 | Unknown | mid | unknown | 2026-08-16 |
| STX | $973.36 | 201,164,750 | Information Technology | large | unknown | 2026-08-16 |
| SYK | $338.83 | 42,768,692 | Health Care | large | unknown | 2026-08-16 |
| T | $24.88 | 80,291,716 | Communication Services | large | unknown | 2026-08-16 |
| TDG | $1256.26 | 49,071,978 | Industrials | large | unknown | 2026-08-16 |
| TEL | $216.29 | 39,950,844 | Information Technology | large | unknown | 2026-08-16 |
| TER | $418.82 | 61,584,242 | Information Technology | large | unknown | 2026-08-16 |
| TFC | $53.09 | 22,879,857 | Financials | large | unknown | 2026-08-16 |
| TGT | $154.53 | 26,855,169 | Consumer Discretionary | large | unknown | 2026-08-16 |
| TJX | $152.10 | 33,814,100 | Consumer Discretionary | large | unknown | 2026-08-16 |
| TMO | $588.00 | 88,032,158 | Health Care | large | unknown | 2026-08-16 |
| TMUS | $182.56 | 40,117,085 | Communication Services | large | unknown | 2026-08-16 |
| TOST | $34.75 | 23,015,573 | Unknown | mid | unknown | 2026-08-16 |
| TPR | $128.99 | 22,109,233 | Consumer Discretionary | large | unknown | 2026-08-16 |
| TRV | $370.29 | 33,251,524 | Financials | large | unknown | 2026-08-16 |
| TSCO | $35.84 | 36,042,675 | Consumer Discretionary | large | unknown | 2026-08-16 |
| TSLA | $342.35 | 330,125,426 | Consumer Discretionary | large | unknown | 2026-08-16 |
| TT | $479.67 | 33,081,117 | Industrials | large | unknown | 2026-08-16 |
| TTMI | $140.04 | 25,322,614 | Information Technology | mid | unknown | 2026-08-16 |
| TTWO | $246.90 | 24,409,778 | Communication Services | large | unknown | 2026-08-16 |
| TWLO | $238.22 | 30,894,750 | Unknown | mid | unknown | 2026-08-16 |
| TXN | $279.72 | 87,992,907 | Information Technology | large | unknown | 2026-08-16 |
| UAL | $125.32 | 20,153,366 | Industrials | large | unknown | 2026-08-16 |
| UBER | $75.91 | 83,655,511 | Unknown | large | unknown | 2026-08-16 |
| UNH | $401.67 | 85,315,087 | Health Care | large | unknown | 2026-08-16 |
| UNP | $293.76 | 46,654,498 | Industrials | large | unknown | 2026-08-16 |
| UPS | $104.50 | 25,572,910 | Industrials | large | unknown | 2026-08-16 |
| URI | $1153.99 | 38,590,341 | Industrials | large | unknown | 2026-08-16 |
| USB | $65.41 | 31,696,684 | Financials | large | unknown | 2026-08-16 |
| V | $364.20 | 104,044,697 | Financials | large | unknown | 2026-08-16 |
| VLO | $341.55 | 41,185,585 | Energy | large | unknown | 2026-08-16 |
| VMC | $282.10 | 21,638,680 | Materials | large | unknown | 2026-08-16 |
| VRSK | $181.65 | 23,693,265 | Industrials | large | unknown | 2026-08-16 |
| VRT | $293.88 | 84,212,438 | Unknown | large | unknown | 2026-08-16 |
| VRTX | $505.46 | 28,042,085 | Health Care | large | unknown | 2026-08-16 |
| VST | $148.15 | 34,227,512 | Utilities | large | unknown | 2026-08-16 |
| VZ | $48.47 | 77,878,871 | Communication Services | large | unknown | 2026-08-16 |
| WAB | $299.39 | 21,372,077 | Industrials | large | unknown | 2026-08-16 |
| WAT | $412.18 | 26,449,526 | Health Care | large | unknown | 2026-08-16 |
| WBD | $28.00 | 45,788,166 | Communication Services | large | unknown | 2026-08-16 |
| WBS | $78.98 | 23,723,490 | Unknown | mid | unknown | 2026-08-16 |
| WDAY | $198.64 | 43,516,763 | Unknown | large | unknown | 2026-08-16 |
| WDC | $510.03 | 161,596,137 | Information Technology | large | unknown | 2026-08-16 |
| WELL | $235.51 | 38,007,215 | Real Estate | large | unknown | 2026-08-16 |
| WFC | $88.78 | 55,405,924 | Financials | large | unknown | 2026-08-16 |
| WM | $224.65 | 25,034,884 | Industrials | large | unknown | 2026-08-16 |
| WMB | $75.06 | 26,938,255 | Energy | large | unknown | 2026-08-16 |
| WMT | $115.27 | 114,069,481 | Consumer Staples | large | unknown | 2026-08-16 |
| XEL | $79.17 | 20,248,793 | Utilities | large | unknown | 2026-08-16 |
| XOM | $160.10 | 69,277,768 | Energy | large | unknown | 2026-08-16 |
| XYZ | $82.86 | 28,025,500 | Unknown | large | unknown | 2026-08-16 |
| ZTS | $73.74 | 25,066,458 | Health Care | large | unknown | 2026-08-16 |
