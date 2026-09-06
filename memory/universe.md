---
screened_on: 2026-09-06
expires_on: 2026-09-13
total_passed: 235
total_rejected: 1269
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
| A | $150.93 | 21,401,829 | Unknown | large | unknown | 2026-09-06 |
| AAL | $13.12 | 21,627,286 | Industrials | mid | unknown | 2026-09-06 |
| AAPL | $319.95 | 378,147,091 | Information Technology | large | unknown | 2026-09-06 |
| ABBV | $256.35 | 44,429,612 | Health Care | large | unknown | 2026-09-06 |
| ABNB | $181.82 | 42,946,342 | Consumer Discretionary | large | unknown | 2026-09-06 |
| ABT | $108.27 | 39,613,336 | Health Care | large | unknown | 2026-09-06 |
| ACN | $186.59 | 38,889,078 | Information Technology | large | unknown | 2026-09-06 |
| ADBE | $266.51 | 45,418,906 | Information Technology | large | unknown | 2026-09-06 |
| ADI | $362.03 | 49,525,752 | Information Technology | large | unknown | 2026-09-06 |
| ADP | $277.53 | 21,362,779 | Industrials | large | unknown | 2026-09-06 |
| ADSK | $217.95 | 23,126,587 | Information Technology | large | unknown | 2026-09-06 |
| ALL | $259.68 | 23,518,851 | Unknown | large | unknown | 2026-09-06 |
| AMAT | $454.54 | 126,865,409 | Information Technology | large | unknown | 2026-09-06 |
| AMD | $477.45 | 205,304,770 | Information Technology | large | unknown | 2026-09-06 |
| AMGN | $437.13 | 33,608,703 | Health Care | large | unknown | 2026-09-06 |
| AMZN | $258.40 | 311,530,418 | Consumer Discretionary | large | unknown | 2026-09-06 |
| ANET | $193.78 | 49,472,958 | Information Technology | large | unknown | 2026-09-06 |
| APH | $82.80 | 46,317,216 | Information Technology | large | unknown | 2026-09-06 |
| APP | $320.50 | 58,410,746 | Unknown | large | unknown | 2026-09-06 |
| ATI | $210.68 | 22,062,636 | Materials | mid | unknown | 2026-09-06 |
| AVGO | $357.83 | 290,831,396 | Information Technology | large | unknown | 2026-09-06 |
| AXON | $516.05 | 22,722,779 | Industrials | large | unknown | 2026-09-06 |
| AXP | $326.15 | 33,890,134 | Unknown | large | unknown | 2026-09-06 |
| AZO | $2982.76 | 27,844,410 | Consumer Discretionary | large | unknown | 2026-09-06 |
| BA | $212.19 | 44,790,817 | Industrials | large | unknown | 2026-09-06 |
| BAC | $62.68 | 115,487,090 | Financials | large | unknown | 2026-09-06 |
| BKNG | $193.30 | 41,349,562 | Consumer Discretionary | large | unknown | 2026-09-06 |
| BKR | $63.49 | 23,838,300 | Unknown | large | unknown | 2026-09-06 |
| BLK | $1122.15 | 36,112,697 | Unknown | large | unknown | 2026-09-06 |
| BMY | $66.83 | 31,682,404 | Health Care | large | unknown | 2026-09-06 |
| BRK.B | $505.92 | 53,936,366 | Financials | large | unknown | 2026-09-06 |
| BSX | $47.80 | 78,761,886 | Health Care | large | unknown | 2026-09-06 |
| BURL | $265.36 | 31,539,444 | Unknown | mid | unknown | 2026-09-06 |
| BX | $136.17 | 23,991,584 | Financials | large | unknown | 2026-09-06 |
| C | $137.72 | 35,488,340 | Financials | large | unknown | 2026-09-06 |
| CAT | $813.80 | 83,700,930 | Industrials | large | unknown | 2026-09-06 |
| CB | $341.59 | 24,197,468 | Financials | large | unknown | 2026-09-06 |
| CCL | $23.52 | 27,683,458 | Unknown | large | unknown | 2026-09-06 |
| CDE | $21.25 | 23,938,059 | Unknown | mid | unknown | 2026-09-06 |
| CDNS | $292.66 | 42,432,138 | Unknown | large | unknown | 2026-09-06 |
| CEG | $299.00 | 25,934,541 | Unknown | large | unknown | 2026-09-06 |
| CHTR | $151.98 | 20,200,905 | Unknown | large | unknown | 2026-09-06 |
| CIEN | $321.01 | 46,761,647 | Unknown | large | unknown | 2026-09-06 |
| CMCSA | $26.48 | 32,234,613 | Unknown | large | unknown | 2026-09-06 |
| CME | $281.31 | 22,146,361 | Financials | large | unknown | 2026-09-06 |
| CMG | $36.95 | 38,122,390 | Consumer Discretionary | large | unknown | 2026-09-06 |
| CMI | $560.76 | 28,897,394 | Industrials | large | unknown | 2026-09-06 |
| COF | $219.57 | 25,003,493 | Financials | large | unknown | 2026-09-06 |
| COHR | $281.86 | 80,034,088 | Unknown | large | unknown | 2026-09-06 |
| COIN | $184.63 | 45,368,933 | Unknown | large | unknown | 2026-09-06 |
| COP | $134.25 | 44,490,816 | Energy | large | unknown | 2026-09-06 |
| COR | $331.00 | 23,697,705 | Unknown | large | unknown | 2026-09-06 |
| COST | $915.68 | 51,109,055 | Consumer Staples | large | unknown | 2026-09-06 |
| CPRT | $33.72 | 22,186,805 | Industrials | large | unknown | 2026-09-06 |
| CRH | $94.24 | 25,721,067 | Unknown | large | unknown | 2026-09-06 |
| CRM | $259.30 | 138,445,345 | Information Technology | large | unknown | 2026-09-06 |
| CRWD | $213.04 | 71,587,806 | Information Technology | large | unknown | 2026-09-06 |
| CSCO | $109.15 | 84,443,075 | Information Technology | large | unknown | 2026-09-06 |
| CSX | $49.41 | 30,428,304 | Industrials | large | unknown | 2026-09-06 |
| CTSH | $62.33 | 20,054,973 | Information Technology | large | unknown | 2026-09-06 |
| CTVA | $87.89 | 20,423,311 | Materials | large | unknown | 2026-09-06 |
| CVNA | $74.56 | 27,454,651 | Unknown | large | unknown | 2026-09-06 |
| CVS | $96.74 | 33,615,391 | Health Care | large | unknown | 2026-09-06 |
| CVX | $208.55 | 52,522,199 | Energy | large | unknown | 2026-09-06 |
| DASH | $211.67 | 48,373,404 | Unknown | large | unknown | 2026-09-06 |
| DDOG | $212.94 | 44,531,129 | Unknown | large | unknown | 2026-09-06 |
| DE | $693.61 | 46,706,697 | Industrials | large | unknown | 2026-09-06 |
| DELL | $523.65 | 120,153,158 | Information Technology | large | unknown | 2026-09-06 |
| DHR | $207.64 | 37,152,232 | Health Care | large | unknown | 2026-09-06 |
| DIS | $105.30 | 34,954,792 | Communication Services | large | unknown | 2026-09-06 |
| DKS | $139.13 | 30,372,667 | Consumer Discretionary | mid | unknown | 2026-09-06 |
| DT | $51.90 | 20,508,386 | Unknown | mid | unknown | 2026-09-06 |
| DUK | $120.24 | 20,784,560 | Utilities | large | unknown | 2026-09-06 |
| DVN | $48.07 | 33,454,015 | Energy | large | unknown | 2026-09-06 |
| ECL | $279.46 | 23,830,100 | Materials | large | unknown | 2026-09-06 |
| EOG | $145.13 | 23,719,454 | Energy | large | unknown | 2026-09-06 |
| EQIX | $1035.50 | 30,847,305 | Real Estate | large | unknown | 2026-09-06 |
| EQT | $55.16 | 27,207,455 | Unknown | large | unknown | 2026-09-06 |
| ETN | $410.81 | 34,081,609 | Industrials | large | unknown | 2026-09-06 |
| EXPE | $297.87 | 24,147,332 | Consumer Discretionary | large | unknown | 2026-09-06 |
| F | $14.62 | 23,252,828 | Consumer Discretionary | large | unknown | 2026-09-06 |
| FCX | $72.69 | 55,099,413 | Materials | large | unknown | 2026-09-06 |
| FDX | $322.36 | 45,104,888 | Industrials | large | unknown | 2026-09-06 |
| FERG | $228.41 | 22,758,879 | Unknown | large | unknown | 2026-09-06 |
| FICO | $934.60 | 22,235,296 | Information Technology | large | unknown | 2026-09-06 |
| FIX | $1611.28 | 33,065,568 | Unknown | large | unknown | 2026-09-06 |
| FN | $407.32 | 29,350,774 | Unknown | mid | unknown | 2026-09-06 |
| FTNT | $156.25 | 27,178,900 | Information Technology | large | unknown | 2026-09-06 |
| GE | $337.03 | 47,746,694 | Industrials | large | unknown | 2026-09-06 |
| GEV | $943.13 | 88,637,202 | Industrials | large | unknown | 2026-09-06 |
| GILD | $151.00 | 25,713,666 | Health Care | large | unknown | 2026-09-06 |
| GIS | $38.28 | 21,069,266 | Consumer Staples | large | unknown | 2026-09-06 |
| GLW | $154.24 | 50,650,346 | Information Technology | large | unknown | 2026-09-06 |
| GOOG | $335.25 | 217,201,349 | Communication Services | large | unknown | 2026-09-06 |
| GOOGL | $338.34 | 239,196,542 | Communication Services | large | unknown | 2026-09-06 |
| GS | $1037.91 | 60,379,493 | Financials | large | unknown | 2026-09-06 |
| HAL | $37.08 | 23,652,952 | Energy | large | unknown | 2026-09-06 |
| HCA | $405.06 | 25,423,572 | Health Care | large | unknown | 2026-09-06 |
| HD | $321.04 | 45,414,385 | Consumer Discretionary | large | unknown | 2026-09-06 |
| HL | $20.68 | 22,954,689 | Unknown | mid | unknown | 2026-09-06 |
| HLT | $310.94 | 28,675,347 | Consumer Discretionary | large | unknown | 2026-09-06 |
| HON | $209.59 | 21,745,058 | Industrials | large | unknown | 2026-09-06 |
| HONA | $161.00 | 29,953,606 | Unknown | large | unknown | 2026-09-06 |
| HOOD | $122.06 | 69,528,837 | Unknown | large | unknown | 2026-09-06 |
| HPE | $52.00 | 56,203,157 | Information Technology | large | unknown | 2026-09-06 |
| HPQ | $32.64 | 35,231,315 | Information Technology | large | unknown | 2026-09-06 |
| HWM | $259.27 | 36,155,401 | Industrials | large | unknown | 2026-09-06 |
| IBM | $234.80 | 38,351,644 | Information Technology | large | unknown | 2026-09-06 |
| ICE | $161.25 | 24,127,115 | Financials | large | unknown | 2026-09-06 |
| ILMN | $218.17 | 25,773,733 | Health Care | mid | unknown | 2026-09-06 |
| INTC | $95.80 | 316,496,498 | Information Technology | large | unknown | 2026-09-06 |
| INTU | $332.70 | 70,149,948 | Information Technology | large | unknown | 2026-09-06 |
| ISRG | $366.63 | 41,698,902 | Health Care | large | unknown | 2026-09-06 |
| JCI | $144.90 | 20,994,631 | Industrials | large | unknown | 2026-09-06 |
| JNJ | $275.24 | 59,350,411 | Health Care | large | unknown | 2026-09-06 |
| JPM | $358.48 | 59,170,406 | Financials | large | unknown | 2026-09-06 |
| KDP | $32.58 | 20,330,755 | Consumer Staples | large | unknown | 2026-09-06 |
| KEYS | $327.16 | 25,855,352 | Information Technology | large | unknown | 2026-09-06 |
| KHC | $24.84 | 21,110,424 | Consumer Staples | large | unknown | 2026-09-06 |
| KKR | $107.73 | 27,113,966 | Unknown | large | unknown | 2026-09-06 |
| KLAC | $185.55 | 59,306,814 | Information Technology | large | unknown | 2026-09-06 |
| KMI | $31.41 | 23,542,763 | Energy | large | unknown | 2026-09-06 |
| KO | $88.07 | 68,423,519 | Consumer Staples | large | unknown | 2026-09-06 |
| KR | $58.58 | 22,217,705 | Consumer Staples | large | unknown | 2026-09-06 |
| KVUE | $18.71 | 22,076,738 | Unknown | large | unknown | 2026-09-06 |
| LIN | $477.43 | 32,334,654 | Materials | large | unknown | 2026-09-06 |
| LITE | $881.44 | 145,041,228 | Unknown | large | unknown | 2026-09-06 |
| LLY | $1148.47 | 121,320,826 | Health Care | large | unknown | 2026-09-06 |
| LMT | $525.29 | 20,972,374 | Industrials | large | unknown | 2026-09-06 |
| LOW | $204.47 | 33,361,063 | Consumer Discretionary | large | unknown | 2026-09-06 |
| LRCX | $307.64 | 98,000,275 | Information Technology | large | unknown | 2026-09-06 |
| MA | $579.35 | 70,226,071 | Financials | large | unknown | 2026-09-06 |
| MCD | $255.68 | 41,882,225 | Consumer Discretionary | large | unknown | 2026-09-06 |
| MCHP | $74.14 | 23,129,933 | Information Technology | large | unknown | 2026-09-06 |
| MCK | $908.01 | 35,560,641 | Health Care | large | unknown | 2026-09-06 |
| MDLZ | $61.27 | 29,244,215 | Consumer Staples | large | unknown | 2026-09-06 |
| MDT | $94.17 | 45,382,538 | Health Care | large | unknown | 2026-09-06 |
| META | $616.75 | 317,719,556 | Communication Services | large | unknown | 2026-09-06 |
| MLM | $514.93 | 31,029,032 | Materials | large | unknown | 2026-09-06 |
| MNST | $43.83 | 22,092,337 | Consumer Staples | large | unknown | 2026-09-06 |
| MO | $68.87 | 36,405,202 | Consumer Staples | large | unknown | 2026-09-06 |
| MPC | $389.28 | 39,541,079 | Energy | large | unknown | 2026-09-06 |
| MPWR | $1221.53 | 33,685,332 | Information Technology | large | unknown | 2026-09-06 |
| MRK | $150.35 | 61,642,451 | Health Care | large | unknown | 2026-09-06 |
| MRNA | $145.51 | 102,479,269 | Health Care | large | unknown | 2026-09-06 |
| MRVL | $223.41 | 123,286,822 | Unknown | large | unknown | 2026-09-06 |
| MS | $217.71 | 34,743,344 | Financials | large | unknown | 2026-09-06 |
| MSFT | $499.55 | 306,454,284 | Information Technology | large | unknown | 2026-09-06 |
| MSI | $468.29 | 29,911,785 | Information Technology | large | unknown | 2026-09-06 |
| MTZ | $237.08 | 29,388,021 | Unknown | mid | unknown | 2026-09-06 |
| MU | $1015.00 | 587,986,389 | Information Technology | large | unknown | 2026-09-06 |
| NEE | $83.42 | 49,500,770 | Utilities | large | unknown | 2026-09-06 |
| NEM | $128.09 | 35,212,415 | Materials | large | unknown | 2026-09-06 |
| NFLX | $78.25 | 119,729,342 | Communication Services | large | unknown | 2026-09-06 |
| NKE | $38.41 | 49,141,888 | Consumer Discretionary | large | unknown | 2026-09-06 |
| NOW | $141.28 | 91,796,592 | Information Technology | large | unknown | 2026-09-06 |
| NTAP | $185.59 | 24,670,381 | Information Technology | large | unknown | 2026-09-06 |
| NVDA | $230.19 | 840,669,990 | Information Technology | large | unknown | 2026-09-06 |
| NXPI | $227.66 | 27,213,540 | Unknown | large | unknown | 2026-09-06 |
| OKTA | $170.57 | 25,464,320 | Information Technology | mid | unknown | 2026-09-06 |
| ON | $74.40 | 22,347,536 | Information Technology | large | unknown | 2026-09-06 |
| ONTO | $268.14 | 21,693,170 | Information Technology | mid | unknown | 2026-09-06 |
| ORCL | $158.77 | 107,850,169 | Information Technology | large | unknown | 2026-09-06 |
| OXY | $60.05 | 29,474,195 | Energy | large | unknown | 2026-09-06 |
| PANW | $333.23 | 79,538,057 | Unknown | large | unknown | 2026-09-06 |
| PATH | $15.20 | 28,633,811 | Unknown | mid | unknown | 2026-09-06 |
| PCG | $14.31 | 56,399,610 | Utilities | large | unknown | 2026-09-06 |
| PEP | $137.58 | 27,632,560 | Consumer Staples | large | unknown | 2026-09-06 |
| PFE | $28.45 | 54,756,872 | Health Care | large | unknown | 2026-09-06 |
| PG | $146.41 | 61,405,663 | Consumer Staples | large | unknown | 2026-09-06 |
| PGR | $218.92 | 30,066,955 | Financials | large | unknown | 2026-09-06 |
| PH | $962.15 | 28,448,983 | Industrials | large | unknown | 2026-09-06 |
| PLTR | $174.25 | 173,316,128 | Unknown | large | unknown | 2026-09-06 |
| PM | $182.54 | 31,390,090 | Consumer Staples | large | unknown | 2026-09-06 |
| PSX | $254.97 | 30,998,291 | Energy | large | unknown | 2026-09-06 |
| PWR | $624.27 | 44,617,859 | Industrials | large | unknown | 2026-09-06 |
| PYPL | $54.95 | 32,830,329 | Financials | large | unknown | 2026-09-06 |
| QCOM | $168.76 | 44,067,428 | Information Technology | large | unknown | 2026-09-06 |
| RCL | $265.15 | 28,253,866 | Consumer Discretionary | large | unknown | 2026-09-06 |
| RDDT | $154.41 | 34,349,971 | Unknown | large | unknown | 2026-09-06 |
| REGN | $827.51 | 21,803,893 | Health Care | large | unknown | 2026-09-06 |
| ROST | $230.57 | 38,563,320 | Consumer Discretionary | large | unknown | 2026-09-06 |
| RTX | $200.72 | 31,566,830 | Industrials | large | unknown | 2026-09-06 |
| SCHW | $109.29 | 45,359,252 | Financials | large | unknown | 2026-09-06 |
| SHW | $333.63 | 20,216,045 | Materials | large | unknown | 2026-09-06 |
| SLB | $57.51 | 36,798,204 | Energy | large | unknown | 2026-09-06 |
| SMCI | $39.59 | 77,663,993 | Information Technology | large | unknown | 2026-09-06 |
| SMTC | $147.79 | 25,810,592 | Information Technology | mid | unknown | 2026-09-06 |
| SNDK | $1739.91 | 445,974,414 | Unknown | large | unknown | 2026-09-06 |
| SNPS | $393.89 | 33,991,542 | Information Technology | large | unknown | 2026-09-06 |
| SO | $88.11 | 24,726,570 | Utilities | large | unknown | 2026-09-06 |
| SPGI | $443.55 | 41,145,147 | Financials | large | unknown | 2026-09-06 |
| STX | $849.49 | 124,006,445 | Information Technology | large | unknown | 2026-09-06 |
| SYK | $303.08 | 34,860,302 | Health Care | large | unknown | 2026-09-06 |
| T | $25.66 | 42,714,619 | Communication Services | large | unknown | 2026-09-06 |
| TDG | $1162.20 | 29,885,560 | Industrials | large | unknown | 2026-09-06 |
| TEL | $208.57 | 29,173,684 | Information Technology | large | unknown | 2026-09-06 |
| TER | $356.50 | 34,417,237 | Information Technology | large | unknown | 2026-09-06 |
| TGT | $164.35 | 36,536,990 | Consumer Discretionary | large | unknown | 2026-09-06 |
| TJX | $132.10 | 50,315,388 | Consumer Discretionary | large | unknown | 2026-09-06 |
| TMO | $613.78 | 57,089,878 | Health Care | large | unknown | 2026-09-06 |
| TMUS | $181.49 | 29,266,409 | Communication Services | large | unknown | 2026-09-06 |
| TOST | $33.95 | 21,397,934 | Unknown | mid | unknown | 2026-09-06 |
| TPR | $122.11 | 24,098,560 | Consumer Discretionary | large | unknown | 2026-09-06 |
| TRGP | $290.14 | 21,893,949 | Unknown | large | unknown | 2026-09-06 |
| TRV | $369.34 | 22,522,401 | Financials | large | unknown | 2026-09-06 |
| TSCO | $35.00 | 27,251,585 | Consumer Discretionary | large | unknown | 2026-09-06 |
| TSLA | $353.89 | 271,172,022 | Consumer Discretionary | large | unknown | 2026-09-06 |
| TTWO | $214.72 | 28,268,054 | Communication Services | large | unknown | 2026-09-06 |
| TWLO | $232.90 | 26,363,985 | Unknown | mid | unknown | 2026-09-06 |
| TXN | $258.27 | 54,151,851 | Information Technology | large | unknown | 2026-09-06 |
| UBER | $75.75 | 59,736,932 | Unknown | large | unknown | 2026-09-06 |
| ULTA | $564.34 | 22,574,386 | Consumer Discretionary | large | unknown | 2026-09-06 |
| UNH | $396.81 | 63,756,598 | Health Care | large | unknown | 2026-09-06 |
| UNP | $289.51 | 36,670,094 | Industrials | large | unknown | 2026-09-06 |
| URI | $1009.86 | 25,655,054 | Industrials | large | unknown | 2026-09-06 |
| USB | $63.35 | 21,911,472 | Financials | large | unknown | 2026-09-06 |
| V | $374.96 | 79,975,281 | Financials | large | unknown | 2026-09-06 |
| VEEV | $274.59 | 25,349,797 | Unknown | large | unknown | 2026-09-06 |
| VLO | $370.50 | 33,602,715 | Energy | large | unknown | 2026-09-06 |
| VRT | $280.52 | 47,874,866 | Unknown | large | unknown | 2026-09-06 |
| VRTX | $546.17 | 28,452,679 | Health Care | large | unknown | 2026-09-06 |
| VST | $149.30 | 21,663,931 | Utilities | large | unknown | 2026-09-06 |
| VZ | $50.13 | 45,711,683 | Communication Services | large | unknown | 2026-09-06 |
| WBD | $28.25 | 39,326,246 | Communication Services | large | unknown | 2026-09-06 |
| WBS | $77.57 | 36,681,735 | Unknown | mid | unknown | 2026-09-06 |
| WDAY | $195.73 | 46,614,718 | Unknown | large | unknown | 2026-09-06 |
| WDC | $467.44 | 116,798,399 | Information Technology | large | unknown | 2026-09-06 |
| WELL | $236.21 | 24,626,883 | Real Estate | large | unknown | 2026-09-06 |
| WFC | $89.96 | 48,019,274 | Financials | large | unknown | 2026-09-06 |
| WM | $218.97 | 20,347,109 | Industrials | large | unknown | 2026-09-06 |
| WMB | $74.17 | 24,299,002 | Energy | large | unknown | 2026-09-06 |
| WMT | $107.14 | 114,576,362 | Consumer Staples | large | unknown | 2026-09-06 |
| XEL | $75.72 | 20,713,607 | Utilities | large | unknown | 2026-09-06 |
| XOM | $159.46 | 63,742,012 | Energy | large | unknown | 2026-09-06 |
