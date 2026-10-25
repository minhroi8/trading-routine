---
screened_on: 2026-10-25
expires_on: 2026-11-01
total_passed: 285
total_rejected: 1247
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
| A | $173.01 | 24,006,943 | Unknown | large | unknown | 2026-10-25 |
| AAL | $12.11 | 31,055,236 | Industrials | mid | unknown | 2026-10-25 |
| AAPL | $347.69 | 387,232,468 | Information Technology | large | unknown | 2026-10-25 |
| ABBV | $285.73 | 61,927,857 | Health Care | large | unknown | 2026-10-25 |
| ABNB | $172.02 | 32,191,228 | Consumer Discretionary | large | unknown | 2026-10-25 |
| ABT | $103.68 | 52,105,777 | Health Care | large | unknown | 2026-10-25 |
| ACN | $249.41 | 87,401,609 | Information Technology | large | unknown | 2026-10-25 |
| ADBE | $263.88 | 40,185,102 | Information Technology | large | unknown | 2026-10-25 |
| ADI | $391.22 | 48,175,832 | Information Technology | large | unknown | 2026-10-25 |
| ADP | $304.23 | 24,071,937 | Industrials | large | unknown | 2026-10-25 |
| ADSK | $252.12 | 29,376,343 | Information Technology | large | unknown | 2026-10-25 |
| AIG | $81.26 | 31,195,945 | Financials | large | unknown | 2026-10-25 |
| AKAM | $93.53 | 24,437,812 | Information Technology | large | unknown | 2026-10-25 |
| ALL | $253.28 | 25,970,805 | Unknown | large | unknown | 2026-10-25 |
| AMAT | $377.31 | 143,678,517 | Information Technology | large | unknown | 2026-10-25 |
| AMD | $516.85 | 292,149,867 | Information Technology | large | unknown | 2026-10-25 |
| AMGN | $439.19 | 48,342,142 | Health Care | large | unknown | 2026-10-25 |
| AMT | $189.00 | 29,705,898 | Real Estate | large | unknown | 2026-10-25 |
| AMZN | $247.99 | 312,778,635 | Consumer Discretionary | large | unknown | 2026-10-25 |
| ANET | $172.33 | 58,160,382 | Information Technology | large | unknown | 2026-10-25 |
| AON | $303.48 | 27,344,819 | Financials | large | unknown | 2026-10-25 |
| APH | $74.09 | 46,662,109 | Information Technology | large | unknown | 2026-10-25 |
| APO | $112.81 | 24,102,617 | Financials | large | unknown | 2026-10-25 |
| APP | $260.21 | 48,994,558 | Unknown | large | unknown | 2026-10-25 |
| AVGO | $321.74 | 240,126,799 | Information Technology | large | unknown | 2026-10-25 |
| AXP | $313.11 | 43,076,441 | Unknown | large | unknown | 2026-10-25 |
| AZO | $3204.34 | 40,239,134 | Consumer Discretionary | large | unknown | 2026-10-25 |
| BA | $188.28 | 61,539,294 | Industrials | large | unknown | 2026-10-25 |
| BAC | $50.55 | 153,813,130 | Financials | large | unknown | 2026-10-25 |
| BE | $193.10 | 104,106,174 | Unknown | large | unknown | 2026-10-25 |
| BKNG | $155.80 | 59,357,391 | Consumer Discretionary | large | unknown | 2026-10-25 |
| BLK | $1117.64 | 47,046,896 | Unknown | large | unknown | 2026-10-25 |
| BMY | $61.49 | 53,904,570 | Health Care | large | unknown | 2026-10-25 |
| BNY | $145.26 | 25,323,987 | Unknown | large | unknown | 2026-10-25 |
| BRK.B | $542.15 | 81,280,548 | Financials | large | unknown | 2026-10-25 |
| BSX | $45.66 | 51,951,236 | Health Care | large | unknown | 2026-10-25 |
| BURL | $247.66 | 26,517,103 | Unknown | mid | unknown | 2026-10-25 |
| BX | $117.97 | 31,276,626 | Financials | large | unknown | 2026-10-25 |
| C | $120.65 | 51,725,816 | Financials | large | unknown | 2026-10-25 |
| CAH | $249.46 | 20,272,769 | Unknown | large | unknown | 2026-10-25 |
| CASY | $699.74 | 22,360,811 | Consumer Staples | large | unknown | 2026-10-25 |
| CAT | $686.75 | 90,127,756 | Industrials | large | unknown | 2026-10-25 |
| CB | $355.11 | 26,311,354 | Financials | large | unknown | 2026-10-25 |
| CBOE | $340.16 | 25,102,763 | Unknown | large | unknown | 2026-10-25 |
| CCI | $86.02 | 21,624,313 | Unknown | large | unknown | 2026-10-25 |
| CCL | $26.11 | 38,687,455 | Unknown | large | unknown | 2026-10-25 |
| CDE | $13.46 | 23,256,837 | Unknown | mid | unknown | 2026-10-25 |
| CDNS | $316.58 | 46,738,533 | Unknown | large | unknown | 2026-10-25 |
| CEG | $253.39 | 49,252,457 | Unknown | large | unknown | 2026-10-25 |
| CFG | $65.14 | 23,716,675 | Financials | large | unknown | 2026-10-25 |
| CI | $306.91 | 22,470,077 | Health Care | large | unknown | 2026-10-25 |
| CIEN | $320.11 | 58,095,412 | Unknown | large | unknown | 2026-10-25 |
| CL | $94.03 | 24,958,978 | Consumer Staples | large | unknown | 2026-10-25 |
| CMCSA | $22.70 | 42,166,335 | Unknown | large | unknown | 2026-10-25 |
| CME | $305.73 | 29,557,933 | Financials | large | unknown | 2026-10-25 |
| CMG | $27.52 | 48,166,943 | Consumer Discretionary | large | unknown | 2026-10-25 |
| CMI | $517.56 | 35,467,752 | Industrials | large | unknown | 2026-10-25 |
| CMS | $69.59 | 22,251,164 | Unknown | large | unknown | 2026-10-25 |
| CNP | $41.09 | 21,664,132 | Unknown | large | unknown | 2026-10-25 |
| COF | $201.31 | 40,684,778 | Financials | large | unknown | 2026-10-25 |
| COHR | $209.25 | 80,673,382 | Unknown | large | unknown | 2026-10-25 |
| COIN | $164.44 | 40,403,292 | Unknown | large | unknown | 2026-10-25 |
| COP | $150.82 | 35,459,573 | Energy | large | unknown | 2026-10-25 |
| COR | $330.81 | 23,286,551 | Unknown | large | unknown | 2026-10-25 |
| COST | $1003.18 | 87,329,062 | Consumer Staples | large | unknown | 2026-10-25 |
| CPRT | $29.00 | 20,561,344 | Industrials | large | unknown | 2026-10-25 |
| CRH | $84.88 | 21,856,363 | Unknown | large | unknown | 2026-10-25 |
| CRL | $345.09 | 23,504,718 | Health Care | large | unknown | 2026-10-25 |
| CRM | $248.48 | 76,029,594 | Information Technology | large | unknown | 2026-10-25 |
| CRWD | $257.55 | 77,444,105 | Information Technology | large | unknown | 2026-10-25 |
| CSCO | $106.49 | 64,519,126 | Information Technology | large | unknown | 2026-10-25 |
| CSX | $50.79 | 40,780,398 | Industrials | large | unknown | 2026-10-25 |
| CTSH | $70.53 | 22,402,747 | Information Technology | large | unknown | 2026-10-25 |
| CVNA | $57.79 | 27,987,745 | Unknown | large | unknown | 2026-10-25 |
| CVS | $93.48 | 43,389,787 | Health Care | large | unknown | 2026-10-25 |
| CVX | $233.23 | 64,602,097 | Energy | large | unknown | 2026-10-25 |
| D | $65.22 | 24,914,261 | Utilities | large | unknown | 2026-10-25 |
| DAL | $76.76 | 31,298,854 | Industrials | large | unknown | 2026-10-25 |
| DASH | $179.37 | 36,794,029 | Unknown | large | unknown | 2026-10-25 |
| DDOG | $269.65 | 41,070,821 | Unknown | large | unknown | 2026-10-25 |
| DE | $646.03 | 42,535,950 | Industrials | large | unknown | 2026-10-25 |
| DELL | $456.62 | 111,714,734 | Information Technology | large | unknown | 2026-10-25 |
| DHI | $147.44 | 23,119,063 | Consumer Discretionary | large | unknown | 2026-10-25 |
| DHR | $230.44 | 69,214,992 | Health Care | large | unknown | 2026-10-25 |
| DIS | $112.50 | 45,727,449 | Communication Services | large | unknown | 2026-10-25 |
| DKS | $144.62 | 25,153,836 | Consumer Discretionary | mid | unknown | 2026-10-25 |
| DT | $64.05 | 25,596,499 | Unknown | mid | unknown | 2026-10-25 |
| DUK | $124.97 | 23,711,062 | Utilities | large | unknown | 2026-10-25 |
| DVN | $51.38 | 35,635,939 | Energy | large | unknown | 2026-10-25 |
| EBAY | $121.40 | 20,494,834 | Consumer Discretionary | large | unknown | 2026-10-25 |
| ECHO | $89.10 | 20,468,419 | Unknown | large | unknown | 2026-10-25 |
| ECL | $288.60 | 22,628,549 | Materials | large | unknown | 2026-10-25 |
| EFX | $182.39 | 20,400,728 | Industrials | large | unknown | 2026-10-25 |
| ELV | $439.98 | 33,584,739 | Unknown | large | unknown | 2026-10-25 |
| EMR | $161.59 | 22,607,072 | Industrials | large | unknown | 2026-10-25 |
| EOG | $163.06 | 22,281,773 | Energy | large | unknown | 2026-10-25 |
| EQIX | $954.60 | 32,932,832 | Real Estate | large | unknown | 2026-10-25 |
| EQT | $55.62 | 27,536,565 | Unknown | large | unknown | 2026-10-25 |
| ETN | $366.04 | 58,417,543 | Industrials | large | unknown | 2026-10-25 |
| EXPE | $289.00 | 27,525,481 | Consumer Discretionary | large | unknown | 2026-10-25 |
| FANG | $205.78 | 25,087,707 | Unknown | large | unknown | 2026-10-25 |
| FAST | $51.92 | 27,779,916 | Industrials | large | unknown | 2026-10-25 |
| FCX | $65.21 | 39,947,203 | Materials | large | unknown | 2026-10-25 |
| FICO | $814.77 | 38,343,066 | Information Technology | large | unknown | 2026-10-25 |
| FITB | $52.99 | 37,498,341 | Financials | large | unknown | 2026-10-25 |
| FIX | $1159.45 | 46,460,055 | Unknown | large | unknown | 2026-10-25 |
| FLEX | $76.54 | 24,906,257 | Unknown | large | unknown | 2026-10-25 |
| FN | $315.06 | 23,595,733 | Unknown | mid | unknown | 2026-10-25 |
| FTNT | $179.98 | 23,208,338 | Information Technology | large | unknown | 2026-10-25 |
| GD | $349.41 | 20,769,172 | Industrials | large | unknown | 2026-10-25 |
| GE | $285.63 | 64,236,312 | Industrials | large | unknown | 2026-10-25 |
| GEV | $814.80 | 107,365,040 | Industrials | large | unknown | 2026-10-25 |
| GILD | $156.06 | 38,378,226 | Health Care | large | unknown | 2026-10-25 |
| GLW | $123.64 | 52,707,941 | Information Technology | large | unknown | 2026-10-25 |
| GM | $75.92 | 40,087,299 | Consumer Discretionary | large | unknown | 2026-10-25 |
| GOOG | $317.21 | 127,044,674 | Communication Services | large | unknown | 2026-10-25 |
| GOOGL | $320.23 | 235,098,678 | Communication Services | large | unknown | 2026-10-25 |
| GS | $875.50 | 82,745,702 | Financials | large | unknown | 2026-10-25 |
| GWW | $1349.67 | 20,473,676 | Industrials | large | unknown | 2026-10-25 |
| HAL | $34.92 | 25,495,576 | Energy | large | unknown | 2026-10-25 |
| HBAN | $15.72 | 22,921,978 | Financials | large | unknown | 2026-10-25 |
| HCA | $469.33 | 26,349,837 | Health Care | large | unknown | 2026-10-25 |
| HD | $319.76 | 76,776,535 | Consumer Discretionary | large | unknown | 2026-10-25 |
| HLT | $349.66 | 43,471,612 | Consumer Discretionary | large | unknown | 2026-10-25 |
| HON | $221.16 | 21,714,571 | Industrials | large | unknown | 2026-10-25 |
| HOOD | $95.06 | 57,233,559 | Unknown | large | unknown | 2026-10-25 |
| HPE | $56.69 | 66,788,988 | Information Technology | large | unknown | 2026-10-25 |
| HPQ | $33.65 | 26,637,185 | Information Technology | large | unknown | 2026-10-25 |
| HUM | $422.30 | 38,214,017 | Health Care | large | unknown | 2026-10-25 |
| HWM | $185.89 | 45,714,836 | Industrials | large | unknown | 2026-10-25 |
| IBM | $253.59 | 50,951,801 | Information Technology | large | unknown | 2026-10-25 |
| ICE | $162.71 | 26,437,260 | Financials | large | unknown | 2026-10-25 |
| IDXX | $560.57 | 20,306,286 | Health Care | large | unknown | 2026-10-25 |
| ILMN | $269.26 | 45,835,425 | Health Care | large | unknown | 2026-10-25 |
| INTC | $86.96 | 265,896,225 | Information Technology | large | unknown | 2026-10-25 |
| INTU | $343.33 | 51,019,628 | Information Technology | large | unknown | 2026-10-25 |
| IQV | $279.35 | 23,988,119 | Health Care | large | unknown | 2026-10-25 |
| IR | $73.45 | 20,562,081 | Industrials | large | unknown | 2026-10-25 |
| ISRG | $452.26 | 44,323,586 | Health Care | large | unknown | 2026-10-25 |
| JBL | $274.03 | 33,755,365 | Unknown | large | unknown | 2026-10-25 |
| JCI | $143.89 | 28,436,001 | Industrials | large | unknown | 2026-10-25 |
| JNJ | $263.84 | 81,654,890 | Health Care | large | unknown | 2026-10-25 |
| JPM | $331.53 | 86,073,369 | Financials | large | unknown | 2026-10-25 |
| KDP | $34.67 | 30,260,146 | Consumer Staples | large | unknown | 2026-10-25 |
| KEYS | $314.60 | 24,555,676 | Information Technology | large | unknown | 2026-10-25 |
| KKR | $91.33 | 27,933,914 | Unknown | large | unknown | 2026-10-25 |
| KLAC | $145.56 | 75,140,396 | Information Technology | large | unknown | 2026-10-25 |
| KMB | $110.15 | 22,438,594 | Consumer Staples | large | unknown | 2026-10-25 |
| KMI | $34.44 | 29,942,541 | Energy | large | unknown | 2026-10-25 |
| KO | $92.70 | 93,514,541 | Consumer Staples | large | unknown | 2026-10-25 |
| KR | $66.79 | 33,175,239 | Consumer Staples | large | unknown | 2026-10-25 |
| KVUE | $19.56 | 27,047,486 | Unknown | large | unknown | 2026-10-25 |
| LEN | $84.94 | 23,654,060 | Consumer Discretionary | large | unknown | 2026-10-25 |
| LHX | $253.96 | 21,017,342 | Industrials | large | unknown | 2026-10-25 |
| LIN | $508.76 | 50,512,551 | Materials | large | unknown | 2026-10-25 |
| LITE | $756.23 | 171,703,778 | Unknown | large | unknown | 2026-10-25 |
| LLY | $1274.27 | 122,943,235 | Health Care | large | unknown | 2026-10-25 |
| LMT | $604.65 | 26,724,544 | Industrials | large | unknown | 2026-10-25 |
| LOW | $198.68 | 27,007,515 | Consumer Discretionary | large | unknown | 2026-10-25 |
| LRCX | $230.04 | 121,372,017 | Information Technology | large | unknown | 2026-10-25 |
| MA | $623.38 | 90,401,532 | Financials | large | unknown | 2026-10-25 |
| MAR | $390.68 | 26,040,665 | Unknown | large | unknown | 2026-10-25 |
| MCD | $248.49 | 47,650,168 | Consumer Discretionary | large | unknown | 2026-10-25 |
| MCHP | $74.06 | 31,220,661 | Information Technology | large | unknown | 2026-10-25 |
| MCK | $1000.76 | 33,558,869 | Health Care | large | unknown | 2026-10-25 |
| MCO | $483.34 | 24,734,362 | Financials | large | unknown | 2026-10-25 |
| MDLZ | $63.79 | 34,335,340 | Consumer Staples | large | unknown | 2026-10-25 |
| MDT | $95.40 | 129,878,534 | Health Care | large | unknown | 2026-10-25 |
| META | $642.24 | 489,073,483 | Communication Services | large | unknown | 2026-10-25 |
| MKSI | $196.49 | 21,771,673 | Information Technology | mid | unknown | 2026-10-25 |
| MLM | $507.20 | 22,281,631 | Materials | large | unknown | 2026-10-25 |
| MMM | $173.47 | 27,648,330 | Industrials | large | unknown | 2026-10-25 |
| MNST | $46.20 | 30,486,180 | Consumer Staples | large | unknown | 2026-10-25 |
| MO | $74.31 | 34,370,206 | Consumer Staples | large | unknown | 2026-10-25 |
| MPC | $457.27 | 43,445,006 | Energy | large | unknown | 2026-10-25 |
| MPWR | $1140.56 | 41,384,598 | Information Technology | large | unknown | 2026-10-25 |
| MRK | $145.27 | 62,692,030 | Health Care | large | unknown | 2026-10-25 |
| MRNA | $200.12 | 120,967,054 | Health Care | large | unknown | 2026-10-25 |
| MRSH | $197.58 | 25,132,978 | Unknown | large | unknown | 2026-10-25 |
| MRVL | $228.61 | 135,038,083 | Unknown | large | unknown | 2026-10-25 |
| MS | $179.49 | 61,860,129 | Financials | large | unknown | 2026-10-25 |
| MSCI | $615.18 | 21,755,730 | Financials | large | unknown | 2026-10-25 |
| MSFT | $524.38 | 342,117,912 | Information Technology | large | unknown | 2026-10-25 |
| MSI | $481.90 | 21,994,809 | Information Technology | large | unknown | 2026-10-25 |
| MTSI | $236.25 | 24,143,767 | Unknown | mid | unknown | 2026-10-25 |
| MTZ | $171.09 | 21,101,681 | Unknown | mid | unknown | 2026-10-25 |
| MU | $877.38 | 642,570,825 | Information Technology | large | unknown | 2026-10-25 |
| NEE | $82.10 | 70,758,942 | Utilities | large | unknown | 2026-10-25 |
| NEM | $108.83 | 30,496,986 | Materials | large | unknown | 2026-10-25 |
| NFLX | $65.86 | 158,614,653 | Communication Services | large | unknown | 2026-10-25 |
| NKE | $37.32 | 68,872,585 | Consumer Discretionary | large | unknown | 2026-10-25 |
| NOC | $551.62 | 30,749,714 | Industrials | large | unknown | 2026-10-25 |
| NOW | $158.96 | 78,763,189 | Information Technology | large | unknown | 2026-10-25 |
| NTAP | $215.65 | 30,293,486 | Information Technology | large | unknown | 2026-10-25 |
| NVDA | $211.02 | 695,181,882 | Information Technology | large | unknown | 2026-10-25 |
| NVR | $5977.54 | 20,961,927 | Consumer Discretionary | large | unknown | 2026-10-25 |
| NVT | $125.41 | 20,008,621 | Industrials | mid | unknown | 2026-10-25 |
| NXPI | $234.92 | 31,440,590 | Unknown | large | unknown | 2026-10-25 |
| O | $56.89 | 28,654,520 | Real Estate | large | unknown | 2026-10-25 |
| OKTA | $213.01 | 36,701,321 | Information Technology | mid | unknown | 2026-10-25 |
| ON | $72.26 | 35,402,369 | Information Technology | large | unknown | 2026-10-25 |
| ORCL | $126.10 | 116,343,959 | Information Technology | large | unknown | 2026-10-25 |
| OXY | $64.16 | 44,268,464 | Energy | large | unknown | 2026-10-25 |
| P | $123.36 | 30,772,981 | Unknown | large | unknown | 2026-10-25 |
| PANW | $380.61 | 83,036,598 | Unknown | large | unknown | 2026-10-25 |
| PCG | $12.62 | 28,588,358 | Utilities | large | unknown | 2026-10-25 |
| PEG | $72.00 | 20,263,129 | Utilities | large | unknown | 2026-10-25 |
| PEP | $135.76 | 54,275,966 | Consumer Staples | large | unknown | 2026-10-25 |
| PFE | $30.01 | 46,099,579 | Health Care | large | unknown | 2026-10-25 |
| PG | $161.12 | 62,767,338 | Consumer Staples | large | unknown | 2026-10-25 |
| PGR | $228.09 | 34,819,334 | Financials | large | unknown | 2026-10-25 |
| PH | $880.02 | 33,709,271 | Industrials | large | unknown | 2026-10-25 |
| PLD | $126.39 | 24,360,748 | Real Estate | large | unknown | 2026-10-25 |
| PLTR | $196.74 | 104,268,914 | Unknown | large | unknown | 2026-10-25 |
| PM | $199.50 | 42,813,194 | Consumer Staples | large | unknown | 2026-10-25 |
| PNC | $224.41 | 23,389,617 | Financials | large | unknown | 2026-10-25 |
| PSX | $283.10 | 47,423,099 | Energy | large | unknown | 2026-10-25 |
| PTC | $193.78 | 50,272,359 | Information Technology | large | unknown | 2026-10-25 |
| PWR | $546.13 | 46,284,416 | Industrials | large | unknown | 2026-10-25 |
| PYPL | $57.00 | 23,879,216 | Financials | large | unknown | 2026-10-25 |
| QCOM | $175.98 | 56,803,059 | Information Technology | large | unknown | 2026-10-25 |
| RCL | $276.50 | 43,013,092 | Consumer Discretionary | large | unknown | 2026-10-25 |
| RDDT | $144.22 | 25,002,398 | Unknown | large | unknown | 2026-10-25 |
| REGN | $805.34 | 30,905,320 | Health Care | large | unknown | 2026-10-25 |
| ROK | $426.17 | 24,490,275 | Industrials | large | unknown | 2026-10-25 |
| ROST | $229.37 | 23,425,884 | Consumer Discretionary | large | unknown | 2026-10-25 |
| RTX | $190.99 | 45,611,301 | Industrials | large | unknown | 2026-10-25 |
| SBUX | $100.80 | 40,156,488 | Consumer Discretionary | large | unknown | 2026-10-25 |
| SCHW | $90.58 | 43,580,225 | Financials | large | unknown | 2026-10-25 |
| SHW | $337.09 | 24,454,699 | Materials | large | unknown | 2026-10-25 |
| SLB | $53.05 | 48,124,766 | Energy | large | unknown | 2026-10-25 |
| SMCI | $32.95 | 51,909,872 | Information Technology | large | unknown | 2026-10-25 |
| SMTC | $131.76 | 29,238,247 | Information Technology | mid | unknown | 2026-10-25 |
| SNDK | $1237.64 | 296,388,762 | Unknown | large | unknown | 2026-10-25 |
| SNPS | $430.07 | 63,526,474 | Information Technology | large | unknown | 2026-10-25 |
| SO | $92.90 | 26,609,144 | Utilities | large | unknown | 2026-10-25 |
| SPGI | $450.26 | 40,625,045 | Financials | large | unknown | 2026-10-25 |
| STT | $167.74 | 22,981,031 | Financials | large | unknown | 2026-10-25 |
| STX | $630.30 | 170,703,197 | Information Technology | large | unknown | 2026-10-25 |
| SWKS | $83.43 | 25,750,721 | Information Technology | large | unknown | 2026-10-25 |
| SYK | $307.14 | 43,444,420 | Health Care | large | unknown | 2026-10-25 |
| T | $20.93 | 63,663,495 | Communication Services | large | unknown | 2026-10-25 |
| TDG | $1105.50 | 30,866,405 | Industrials | large | unknown | 2026-10-25 |
| TEL | $208.02 | 23,883,049 | Information Technology | large | unknown | 2026-10-25 |
| TER | $308.95 | 43,393,669 | Information Technology | large | unknown | 2026-10-25 |
| TFC | $48.45 | 30,282,691 | Financials | large | unknown | 2026-10-25 |
| TGT | $152.72 | 31,579,275 | Consumer Discretionary | large | unknown | 2026-10-25 |
| TJX | $145.00 | 52,164,559 | Consumer Discretionary | large | unknown | 2026-10-25 |
| TLN | $327.83 | 29,283,287 | Unknown | mid | unknown | 2026-10-25 |
| TMO | $673.84 | 104,435,860 | Health Care | large | unknown | 2026-10-25 |
| TMUS | $146.58 | 45,527,992 | Communication Services | large | unknown | 2026-10-25 |
| TOST | $32.71 | 20,045,759 | Unknown | mid | unknown | 2026-10-25 |
| TRGP | $302.44 | 21,751,736 | Unknown | large | unknown | 2026-10-25 |
| TRV | $398.31 | 21,161,949 | Financials | large | unknown | 2026-10-25 |
| TSCO | $33.41 | 33,900,815 | Consumer Discretionary | large | unknown | 2026-10-25 |
| TSLA | $372.15 | 262,806,081 | Consumer Discretionary | large | unknown | 2026-10-25 |
| TT | $444.74 | 45,890,606 | Industrials | large | unknown | 2026-10-25 |
| TTMI | $80.17 | 23,220,282 | Information Technology | mid | unknown | 2026-10-25 |
| TTWO | $203.71 | 24,705,652 | Communication Services | large | unknown | 2026-10-25 |
| TWLO | $261.79 | 45,694,917 | Unknown | large | unknown | 2026-10-25 |
| TXN | $284.77 | 69,160,420 | Information Technology | large | unknown | 2026-10-25 |
| UAL | $97.91 | 26,164,019 | Industrials | large | unknown | 2026-10-25 |
| UBER | $66.67 | 55,792,802 | Unknown | large | unknown | 2026-10-25 |
| UNH | $418.06 | 122,766,068 | Health Care | large | unknown | 2026-10-25 |
| UNP | $292.89 | 36,550,482 | Industrials | large | unknown | 2026-10-25 |
| URI | $1099.10 | 42,500,010 | Industrials | large | unknown | 2026-10-25 |
| USB | $59.58 | 37,481,923 | Financials | large | unknown | 2026-10-25 |
| UTHR | $587.42 | 33,645,007 | Health Care | mid | unknown | 2026-10-25 |
| V | $408.00 | 107,634,936 | Financials | large | unknown | 2026-10-25 |
| VEEV | $322.95 | 26,201,492 | Unknown | large | unknown | 2026-10-25 |
| VLO | $419.35 | 56,509,615 | Energy | large | unknown | 2026-10-25 |
| VRT | $194.26 | 63,895,232 | Unknown | large | unknown | 2026-10-25 |
| VRTX | $523.92 | 31,752,189 | Health Care | large | unknown | 2026-10-25 |
| VST | $140.25 | 51,304,672 | Utilities | large | unknown | 2026-10-25 |
| VZ | $44.60 | 71,272,869 | Communication Services | large | unknown | 2026-10-25 |
| WAT | $453.46 | 26,817,854 | Health Care | large | unknown | 2026-10-25 |
| WCC | $317.37 | 21,619,278 | Unknown | mid | unknown | 2026-10-25 |
| WDC | $343.46 | 146,966,982 | Information Technology | large | unknown | 2026-10-25 |
| WELL | $237.33 | 37,863,881 | Real Estate | large | unknown | 2026-10-25 |
| WFC | $82.38 | 88,357,181 | Financials | large | unknown | 2026-10-25 |
| WM | $239.39 | 26,023,200 | Industrials | large | unknown | 2026-10-25 |
| WMB | $71.68 | 33,444,213 | Energy | large | unknown | 2026-10-25 |
| WMT | $119.87 | 98,745,179 | Consumer Staples | large | unknown | 2026-10-25 |
| XEL | $78.04 | 24,337,914 | Utilities | large | unknown | 2026-10-25 |
| XOM | $183.21 | 59,849,056 | Energy | large | unknown | 2026-10-25 |
