---
screened_on: 2026-09-20
expires_on: 2026-09-27
total_passed: 244
total_rejected: 1291
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
| A | $156.46 | 21,723,156 | Unknown | large | unknown | 2026-09-20 |
| AAL | $12.96 | 24,588,409 | Industrials | mid | unknown | 2026-09-20 |
| AAPL | $335.73 | 393,087,295 | Information Technology | large | unknown | 2026-09-20 |
| ABBV | $263.86 | 39,128,978 | Health Care | large | unknown | 2026-09-20 |
| ABNB | $166.13 | 34,959,474 | Consumer Discretionary | large | unknown | 2026-09-20 |
| ABT | $102.57 | 41,751,425 | Health Care | large | unknown | 2026-09-20 |
| ACN | $181.19 | 37,069,503 | Information Technology | large | unknown | 2026-09-20 |
| ADBE | $248.87 | 47,806,263 | Information Technology | large | unknown | 2026-09-20 |
| ADI | $375.89 | 42,323,676 | Information Technology | large | unknown | 2026-09-20 |
| ADP | $271.16 | 22,505,540 | Industrials | large | unknown | 2026-09-20 |
| ADSK | $216.87 | 30,253,650 | Information Technology | large | unknown | 2026-09-20 |
| ALL | $249.81 | 20,904,455 | Unknown | large | unknown | 2026-09-20 |
| AMAT | $444.66 | 100,672,292 | Information Technology | large | unknown | 2026-09-20 |
| AMD | $559.68 | 244,924,699 | Information Technology | large | unknown | 2026-09-20 |
| AMGN | $385.61 | 44,537,065 | Health Care | large | unknown | 2026-09-20 |
| AMZN | $253.70 | 292,000,503 | Consumer Discretionary | large | unknown | 2026-09-20 |
| ANET | $199.43 | 42,676,950 | Information Technology | large | unknown | 2026-09-20 |
| AON | $295.48 | 35,564,644 | Financials | large | unknown | 2026-09-20 |
| APH | $77.57 | 46,169,842 | Information Technology | large | unknown | 2026-09-20 |
| APP | $308.00 | 54,995,268 | Unknown | large | unknown | 2026-09-20 |
| ATI | $191.75 | 22,917,587 | Materials | mid | unknown | 2026-09-20 |
| AVGO | $357.74 | 282,077,026 | Information Technology | large | unknown | 2026-09-20 |
| AXON | $447.95 | 23,172,438 | Industrials | large | unknown | 2026-09-20 |
| AXP | $311.80 | 40,709,470 | Unknown | large | unknown | 2026-09-20 |
| AZO | $2856.37 | 38,314,827 | Consumer Discretionary | large | unknown | 2026-09-20 |
| BA | $198.27 | 47,741,061 | Industrials | large | unknown | 2026-09-20 |
| BAC | $57.70 | 137,278,872 | Financials | large | unknown | 2026-09-20 |
| BDX | $180.78 | 20,823,242 | Health Care | large | unknown | 2026-09-20 |
| BKNG | $167.74 | 56,839,516 | Consumer Discretionary | large | unknown | 2026-09-20 |
| BKR | $57.23 | 24,322,856 | Unknown | large | unknown | 2026-09-20 |
| BLK | $1069.31 | 35,740,232 | Unknown | large | unknown | 2026-09-20 |
| BMY | $63.03 | 29,063,781 | Health Care | large | unknown | 2026-09-20 |
| BRK.B | $509.66 | 65,068,338 | Financials | large | unknown | 2026-09-20 |
| BSX | $43.40 | 74,329,159 | Health Care | large | unknown | 2026-09-20 |
| BURL | $237.03 | 31,698,702 | Unknown | mid | unknown | 2026-09-20 |
| C | $131.75 | 41,139,413 | Financials | large | unknown | 2026-09-20 |
| CARR | $53.87 | 20,058,552 | Unknown | large | unknown | 2026-09-20 |
| CASY | $597.46 | 23,304,760 | Consumer Staples | large | unknown | 2026-09-20 |
| CAT | $808.56 | 65,534,291 | Industrials | large | unknown | 2026-09-20 |
| CB | $340.51 | 21,553,831 | Financials | large | unknown | 2026-09-20 |
| CCL | $21.84 | 27,702,483 | Unknown | large | unknown | 2026-09-20 |
| CDE | $19.73 | 21,767,957 | Unknown | mid | unknown | 2026-09-20 |
| CDNS | $282.82 | 40,242,720 | Unknown | large | unknown | 2026-09-20 |
| CEG | $254.73 | 25,634,856 | Unknown | large | unknown | 2026-09-20 |
| CHTR | $128.13 | 22,416,169 | Unknown | large | unknown | 2026-09-20 |
| CIEN | $349.18 | 43,110,840 | Unknown | large | unknown | 2026-09-20 |
| CMCSA | $22.72 | 36,364,610 | Unknown | large | unknown | 2026-09-20 |
| CME | $276.02 | 22,949,109 | Financials | large | unknown | 2026-09-20 |
| CMG | $33.43 | 32,009,631 | Consumer Discretionary | large | unknown | 2026-09-20 |
| CMI | $531.90 | 32,443,139 | Industrials | large | unknown | 2026-09-20 |
| COF | $202.28 | 28,354,212 | Financials | large | unknown | 2026-09-20 |
| COHR | $317.19 | 57,677,774 | Unknown | large | unknown | 2026-09-20 |
| COIN | $194.31 | 53,196,728 | Unknown | large | unknown | 2026-09-20 |
| COP | $131.84 | 40,220,792 | Energy | large | unknown | 2026-09-20 |
| COR | $308.61 | 20,033,638 | Unknown | large | unknown | 2026-09-20 |
| COST | $895.75 | 54,391,714 | Consumer Staples | large | unknown | 2026-09-20 |
| CRH | $86.18 | 20,789,953 | Unknown | large | unknown | 2026-09-20 |
| CRM | $237.91 | 163,897,486 | Information Technology | large | unknown | 2026-09-20 |
| CRWD | $237.61 | 83,708,423 | Information Technology | large | unknown | 2026-09-20 |
| CSCO | $109.51 | 62,480,235 | Information Technology | large | unknown | 2026-09-20 |
| CSX | $47.08 | 32,232,148 | Industrials | large | unknown | 2026-09-20 |
| CTVA | $80.55 | 23,040,327 | Materials | large | unknown | 2026-09-20 |
| CVNA | $65.10 | 22,715,815 | Unknown | large | unknown | 2026-09-20 |
| CVS | $88.85 | 30,071,861 | Health Care | large | unknown | 2026-09-20 |
| CVX | $209.40 | 56,585,735 | Energy | large | unknown | 2026-09-20 |
| D | $63.56 | 22,069,476 | Utilities | large | unknown | 2026-09-20 |
| DASH | $192.89 | 41,283,614 | Unknown | large | unknown | 2026-09-20 |
| DDOG | $229.89 | 38,031,025 | Unknown | large | unknown | 2026-09-20 |
| DE | $683.94 | 45,197,426 | Industrials | large | unknown | 2026-09-20 |
| DELL | $569.00 | 134,435,785 | Information Technology | large | unknown | 2026-09-20 |
| DHR | $211.77 | 38,737,304 | Health Care | large | unknown | 2026-09-20 |
| DIS | $102.65 | 37,631,327 | Communication Services | large | unknown | 2026-09-20 |
| DKS | $121.17 | 27,804,205 | Consumer Discretionary | mid | unknown | 2026-09-20 |
| DT | $55.15 | 20,656,022 | Unknown | mid | unknown | 2026-09-20 |
| DVN | $48.60 | 36,994,234 | Energy | large | unknown | 2026-09-20 |
| EBAY | $111.86 | 21,258,425 | Consumer Discretionary | large | unknown | 2026-09-20 |
| ECL | $269.44 | 24,772,132 | Materials | large | unknown | 2026-09-20 |
| ELV | $410.92 | 20,129,906 | Unknown | large | unknown | 2026-09-20 |
| EOG | $144.22 | 20,910,351 | Energy | large | unknown | 2026-09-20 |
| EQIX | $1021.59 | 28,304,136 | Real Estate | large | unknown | 2026-09-20 |
| EQT | $49.98 | 24,926,745 | Unknown | large | unknown | 2026-09-20 |
| ETN | $424.80 | 43,928,768 | Industrials | large | unknown | 2026-09-20 |
| EXPE | $279.39 | 32,357,260 | Consumer Discretionary | large | unknown | 2026-09-20 |
| F | $13.21 | 24,677,546 | Consumer Discretionary | large | unknown | 2026-09-20 |
| FANG | $192.43 | 25,705,360 | Unknown | large | unknown | 2026-09-20 |
| FCX | $71.55 | 53,265,615 | Materials | large | unknown | 2026-09-20 |
| FDX | $303.64 | 30,091,235 | Industrials | large | unknown | 2026-09-20 |
| FICO | $950.05 | 23,899,598 | Information Technology | large | unknown | 2026-09-20 |
| FIX | $1651.93 | 26,456,417 | Unknown | large | unknown | 2026-09-20 |
| FN | $388.64 | 20,924,504 | Unknown | mid | unknown | 2026-09-20 |
| FTNT | $169.85 | 29,489,839 | Information Technology | large | unknown | 2026-09-20 |
| GE | $313.99 | 52,411,872 | Industrials | large | unknown | 2026-09-20 |
| GEV | $940.00 | 89,051,205 | Industrials | large | unknown | 2026-09-20 |
| GILD | $149.99 | 25,470,808 | Health Care | large | unknown | 2026-09-20 |
| GIS | $36.34 | 21,088,454 | Consumer Staples | large | unknown | 2026-09-20 |
| GLW | $150.11 | 50,070,459 | Information Technology | large | unknown | 2026-09-20 |
| GOOG | $344.34 | 186,283,410 | Communication Services | large | unknown | 2026-09-20 |
| GOOGL | $349.23 | 251,923,116 | Communication Services | large | unknown | 2026-09-20 |
| GS | $941.99 | 71,272,148 | Financials | large | unknown | 2026-09-20 |
| HAL | $33.64 | 26,787,241 | Energy | large | unknown | 2026-09-20 |
| HBAN | $15.87 | 21,765,519 | Financials | large | unknown | 2026-09-20 |
| HCA | $427.99 | 31,255,195 | Health Care | large | unknown | 2026-09-20 |
| HD | $299.93 | 40,834,503 | Consumer Discretionary | large | unknown | 2026-09-20 |
| HL | $18.94 | 22,076,148 | Unknown | mid | unknown | 2026-09-20 |
| HLT | $305.71 | 25,927,609 | Consumer Discretionary | large | unknown | 2026-09-20 |
| HON | $206.37 | 21,649,951 | Industrials | large | unknown | 2026-09-20 |
| HONA | $163.59 | 32,265,716 | Unknown | large | unknown | 2026-09-20 |
| HOOD | $119.83 | 83,253,848 | Unknown | large | unknown | 2026-09-20 |
| HPE | $60.73 | 66,169,970 | Information Technology | large | unknown | 2026-09-20 |
| HPQ | $34.44 | 41,370,613 | Information Technology | large | unknown | 2026-09-20 |
| HUM | $385.96 | 20,339,168 | Health Care | large | unknown | 2026-09-20 |
| HWM | $229.78 | 45,338,370 | Industrials | large | unknown | 2026-09-20 |
| IBM | $229.58 | 45,154,129 | Information Technology | large | unknown | 2026-09-20 |
| ICE | $155.53 | 23,827,750 | Financials | large | unknown | 2026-09-20 |
| ILMN | $239.53 | 32,824,368 | Health Care | mid | unknown | 2026-09-20 |
| INTC | $108.67 | 253,188,020 | Information Technology | large | unknown | 2026-09-20 |
| INTU | $303.11 | 66,288,155 | Information Technology | large | unknown | 2026-09-20 |
| IQV | $266.56 | 22,947,698 | Health Care | large | unknown | 2026-09-20 |
| ISRG | $393.13 | 39,610,115 | Health Care | large | unknown | 2026-09-20 |
| JNJ | $269.93 | 58,632,571 | Health Care | large | unknown | 2026-09-20 |
| JPM | $349.40 | 75,445,762 | Financials | large | unknown | 2026-09-20 |
| KHC | $24.43 | 27,444,684 | Consumer Staples | large | unknown | 2026-09-20 |
| KKR | $98.78 | 21,982,192 | Unknown | large | unknown | 2026-09-20 |
| KLAC | $177.01 | 53,458,030 | Information Technology | large | unknown | 2026-09-20 |
| KMI | $31.84 | 29,152,890 | Energy | large | unknown | 2026-09-20 |
| KO | $88.14 | 69,795,689 | Consumer Staples | large | unknown | 2026-09-20 |
| KR | $60.04 | 26,685,264 | Consumer Staples | large | unknown | 2026-09-20 |
| KVUE | $17.81 | 38,350,879 | Unknown | large | unknown | 2026-09-20 |
| LHX | $247.18 | 20,908,118 | Industrials | large | unknown | 2026-09-20 |
| LIN | $460.25 | 35,601,157 | Materials | large | unknown | 2026-09-20 |
| LITE | $931.63 | 119,590,796 | Unknown | large | unknown | 2026-09-20 |
| LLY | $1152.46 | 104,397,204 | Health Care | large | unknown | 2026-09-20 |
| LOW | $192.50 | 28,907,797 | Consumer Discretionary | large | unknown | 2026-09-20 |
| LRCX | $287.77 | 92,709,053 | Information Technology | large | unknown | 2026-09-20 |
| LULU | $98.12 | 22,949,041 | Unknown | large | unknown | 2026-09-20 |
| MA | $565.08 | 60,975,815 | Financials | large | unknown | 2026-09-20 |
| MAR | $338.95 | 26,631,651 | Unknown | large | unknown | 2026-09-20 |
| MCD | $248.38 | 43,734,130 | Consumer Discretionary | large | unknown | 2026-09-20 |
| MCK | $875.15 | 34,539,439 | Health Care | large | unknown | 2026-09-20 |
| MDLZ | $60.84 | 29,722,078 | Consumer Staples | large | unknown | 2026-09-20 |
| MDT | $92.13 | 44,224,220 | Health Care | large | unknown | 2026-09-20 |
| META | $665.39 | 369,432,359 | Communication Services | large | unknown | 2026-09-20 |
| MKSI | $252.28 | 21,288,687 | Information Technology | mid | unknown | 2026-09-20 |
| MLM | $490.91 | 32,058,419 | Materials | large | unknown | 2026-09-20 |
| MMM | $166.01 | 21,035,946 | Industrials | large | unknown | 2026-09-20 |
| MNST | $44.68 | 20,276,603 | Consumer Staples | large | unknown | 2026-09-20 |
| MO | $69.51 | 28,639,030 | Consumer Staples | large | unknown | 2026-09-20 |
| MPC | $424.59 | 44,570,836 | Energy | large | unknown | 2026-09-20 |
| MPWR | $1219.88 | 37,102,721 | Information Technology | large | unknown | 2026-09-20 |
| MRK | $146.75 | 49,011,600 | Health Care | large | unknown | 2026-09-20 |
| MRNA | $153.99 | 77,618,182 | Health Care | large | unknown | 2026-09-20 |
| MRVL | $244.30 | 112,657,973 | Unknown | large | unknown | 2026-09-20 |
| MS | $202.56 | 39,662,560 | Financials | large | unknown | 2026-09-20 |
| MSFT | $493.10 | 283,870,522 | Information Technology | large | unknown | 2026-09-20 |
| MSI | $459.04 | 29,740,863 | Information Technology | large | unknown | 2026-09-20 |
| MTZ | $214.47 | 26,354,033 | Unknown | mid | unknown | 2026-09-20 |
| MU | $1015.53 | 516,460,393 | Information Technology | large | unknown | 2026-09-20 |
| NEE | $80.46 | 52,764,041 | Utilities | large | unknown | 2026-09-20 |
| NEM | $123.38 | 35,330,855 | Materials | large | unknown | 2026-09-20 |
| NFLX | $71.80 | 114,023,278 | Communication Services | large | unknown | 2026-09-20 |
| NKE | $35.54 | 48,127,935 | Consumer Discretionary | large | unknown | 2026-09-20 |
| NOW | $135.17 | 80,882,050 | Information Technology | large | unknown | 2026-09-20 |
| NTAP | $197.73 | 22,935,344 | Information Technology | large | unknown | 2026-09-20 |
| NVDA | $222.04 | 733,976,637 | Information Technology | large | unknown | 2026-09-20 |
| NXPI | $228.22 | 25,226,730 | Unknown | large | unknown | 2026-09-20 |
| O | $56.63 | 20,010,030 | Real Estate | large | unknown | 2026-09-20 |
| OKTA | $182.30 | 34,667,747 | Information Technology | mid | unknown | 2026-09-20 |
| ON | $70.00 | 27,856,163 | Information Technology | large | unknown | 2026-09-20 |
| ORCL | $147.60 | 124,376,211 | Information Technology | large | unknown | 2026-09-20 |
| ORLY | $84.69 | 20,200,361 | Consumer Discretionary | large | unknown | 2026-09-20 |
| OXY | $58.83 | 31,657,839 | Energy | large | unknown | 2026-09-20 |
| PANW | $363.57 | 86,142,258 | Unknown | large | unknown | 2026-09-20 |
| PATH | $13.38 | 26,629,840 | Unknown | mid | unknown | 2026-09-20 |
| PCG | $13.19 | 54,940,306 | Utilities | large | unknown | 2026-09-20 |
| PEP | $129.62 | 37,208,269 | Consumer Staples | large | unknown | 2026-09-20 |
| PFE | $27.60 | 46,413,953 | Health Care | large | unknown | 2026-09-20 |
| PG | $146.32 | 53,152,469 | Consumer Staples | large | unknown | 2026-09-20 |
| PGR | $213.43 | 22,628,192 | Financials | large | unknown | 2026-09-20 |
| PH | $943.06 | 27,607,197 | Industrials | large | unknown | 2026-09-20 |
| PLTR | $177.49 | 126,329,406 | Unknown | large | unknown | 2026-09-20 |
| PM | $188.63 | 31,069,563 | Consumer Staples | large | unknown | 2026-09-20 |
| PSX | $273.20 | 31,318,203 | Energy | large | unknown | 2026-09-20 |
| PWR | $636.60 | 33,797,042 | Industrials | large | unknown | 2026-09-20 |
| PYPL | $52.42 | 29,899,511 | Financials | large | unknown | 2026-09-20 |
| QCOM | $178.01 | 65,634,429 | Information Technology | large | unknown | 2026-09-20 |
| RCL | $245.77 | 32,914,846 | Consumer Discretionary | large | unknown | 2026-09-20 |
| RDDT | $150.87 | 28,656,659 | Unknown | large | unknown | 2026-09-20 |
| REGN | $784.95 | 20,343,185 | Health Care | large | unknown | 2026-09-20 |
| ROST | $226.60 | 30,027,785 | Consumer Discretionary | large | unknown | 2026-09-20 |
| RTX | $193.91 | 28,333,099 | Industrials | large | unknown | 2026-09-20 |
| SBUX | $95.80 | 25,368,728 | Consumer Discretionary | large | unknown | 2026-09-20 |
| SCHW | $105.22 | 42,480,146 | Financials | large | unknown | 2026-09-20 |
| SHW | $320.65 | 20,037,547 | Materials | large | unknown | 2026-09-20 |
| SLB | $51.12 | 42,190,490 | Energy | large | unknown | 2026-09-20 |
| SMCI | $39.11 | 56,994,875 | Information Technology | large | unknown | 2026-09-20 |
| SMTC | $185.03 | 31,388,932 | Information Technology | mid | unknown | 2026-09-20 |
| SNDK | $1791.83 | 350,846,449 | Unknown | large | unknown | 2026-09-20 |
| SNPS | $384.76 | 36,954,336 | Information Technology | large | unknown | 2026-09-20 |
| SO | $85.50 | 25,750,114 | Utilities | large | unknown | 2026-09-20 |
| SPGI | $405.46 | 39,279,518 | Financials | large | unknown | 2026-09-20 |
| STX | $858.47 | 111,229,967 | Information Technology | large | unknown | 2026-09-20 |
| SWKS | $88.75 | 28,779,832 | Information Technology | large | unknown | 2026-09-20 |
| SYK | $274.94 | 44,950,601 | Health Care | large | unknown | 2026-09-20 |
| T | $25.41 | 47,733,837 | Communication Services | large | unknown | 2026-09-20 |
| TDG | $1085.77 | 25,225,198 | Industrials | large | unknown | 2026-09-20 |
| TEL | $205.43 | 26,800,349 | Information Technology | large | unknown | 2026-09-20 |
| TER | $371.48 | 34,372,333 | Information Technology | large | unknown | 2026-09-20 |
| TFC | $48.53 | 20,000,938 | Financials | large | unknown | 2026-09-20 |
| TGT | $158.16 | 29,520,704 | Consumer Discretionary | large | unknown | 2026-09-20 |
| TJX | $127.25 | 55,002,468 | Consumer Discretionary | large | unknown | 2026-09-20 |
| TMO | $651.24 | 69,869,084 | Health Care | large | unknown | 2026-09-20 |
| TMUS | $168.15 | 37,421,048 | Communication Services | large | unknown | 2026-09-20 |
| TOST | $29.74 | 20,400,703 | Unknown | mid | unknown | 2026-09-20 |
| TRV | $374.56 | 21,306,904 | Financials | large | unknown | 2026-09-20 |
| TSLA | $364.30 | 274,369,718 | Consumer Discretionary | large | unknown | 2026-09-20 |
| TT | $428.91 | 22,652,237 | Industrials | large | unknown | 2026-09-20 |
| TTWO | $205.47 | 27,732,847 | Communication Services | large | unknown | 2026-09-20 |
| TWLO | $243.91 | 23,015,629 | Unknown | mid | unknown | 2026-09-20 |
| TXN | $266.71 | 55,495,489 | Information Technology | large | unknown | 2026-09-20 |
| UBER | $70.50 | 53,845,031 | Unknown | large | unknown | 2026-09-20 |
| ULTA | $541.09 | 21,497,348 | Consumer Discretionary | large | unknown | 2026-09-20 |
| UNH | $376.94 | 68,632,643 | Health Care | large | unknown | 2026-09-20 |
| UNP | $279.34 | 33,419,241 | Industrials | large | unknown | 2026-09-20 |
| URI | $1014.32 | 24,386,171 | Industrials | large | unknown | 2026-09-20 |
| USB | $60.04 | 27,564,601 | Financials | large | unknown | 2026-09-20 |
| V | $367.63 | 78,632,493 | Financials | large | unknown | 2026-09-20 |
| VEEV | $260.35 | 23,544,013 | Unknown | large | unknown | 2026-09-20 |
| VLO | $413.02 | 48,275,624 | Energy | large | unknown | 2026-09-20 |
| VMRK | $61.21 | 20,278,855 | Unknown | large | unknown | 2026-09-20 |
| VRT | $248.91 | 66,883,055 | Unknown | large | unknown | 2026-09-20 |
| VRTX | $508.29 | 21,107,348 | Health Care | large | unknown | 2026-09-20 |
| VST | $140.69 | 23,883,821 | Utilities | large | unknown | 2026-09-20 |
| VZ | $48.12 | 50,142,233 | Communication Services | large | unknown | 2026-09-20 |
| WBD | $27.82 | 37,844,283 | Communication Services | large | unknown | 2026-09-20 |
| WDAY | $193.84 | 34,964,012 | Unknown | large | unknown | 2026-09-20 |
| WDC | $441.48 | 96,959,761 | Information Technology | large | unknown | 2026-09-20 |
| WELL | $228.85 | 22,220,621 | Real Estate | large | unknown | 2026-09-20 |
| WFC | $86.11 | 53,087,072 | Financials | large | unknown | 2026-09-20 |
| WM | $211.05 | 21,823,460 | Industrials | large | unknown | 2026-09-20 |
| WMB | $72.07 | 27,405,120 | Energy | large | unknown | 2026-09-20 |
| WMT | $106.68 | 96,001,443 | Consumer Staples | large | unknown | 2026-09-20 |
| WWD | $321.80 | 20,905,373 | Industrials | mid | unknown | 2026-09-20 |
| XEL | $72.28 | 26,140,740 | Utilities | large | unknown | 2026-09-20 |
| XOM | $163.19 | 63,673,595 | Energy | large | unknown | 2026-09-20 |
