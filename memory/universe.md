---
screened_on: 2026-10-04
expires_on: 2026-10-11
total_passed: 266
total_rejected: 1267
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
| A | $167.73 | 20,990,419 | Unknown | large | unknown | 2026-10-04 |
| AAL | $12.94 | 29,068,482 | Industrials | mid | unknown | 2026-10-04 |
| AAPL | $333.75 | 398,713,374 | Information Technology | large | unknown | 2026-10-04 |
| ABBV | $262.92 | 42,400,097 | Health Care | large | unknown | 2026-10-04 |
| ABNB | $162.48 | 40,095,658 | Consumer Discretionary | large | unknown | 2026-10-04 |
| ABT | $97.49 | 41,565,231 | Health Care | large | unknown | 2026-10-04 |
| ACN | $198.97 | 58,525,221 | Information Technology | large | unknown | 2026-10-04 |
| ADBE | $237.64 | 47,561,086 | Information Technology | large | unknown | 2026-10-04 |
| ADI | $417.32 | 42,156,503 | Information Technology | large | unknown | 2026-10-04 |
| ADP | $257.64 | 28,938,328 | Industrials | large | unknown | 2026-10-04 |
| ADSK | $212.07 | 29,883,988 | Information Technology | large | unknown | 2026-10-04 |
| AKAM | $108.90 | 26,052,598 | Information Technology | large | unknown | 2026-10-04 |
| ALL | $223.69 | 31,272,378 | Unknown | large | unknown | 2026-10-04 |
| AMAT | $540.03 | 118,109,882 | Information Technology | large | unknown | 2026-10-04 |
| AMD | $633.75 | 349,353,212 | Information Technology | large | unknown | 2026-10-04 |
| AMGN | $403.09 | 50,655,674 | Health Care | large | unknown | 2026-10-04 |
| AMZN | $251.42 | 292,094,355 | Consumer Discretionary | large | unknown | 2026-10-04 |
| ANET | $207.34 | 41,860,141 | Information Technology | large | unknown | 2026-10-04 |
| AON | $269.50 | 42,018,373 | Financials | large | unknown | 2026-10-04 |
| APH | $87.01 | 49,470,637 | Information Technology | large | unknown | 2026-10-04 |
| APO | $114.02 | 20,836,846 | Financials | large | unknown | 2026-10-04 |
| APP | $268.20 | 63,839,170 | Unknown | large | unknown | 2026-10-04 |
| AVGO | $355.12 | 254,877,266 | Information Technology | large | unknown | 2026-10-04 |
| AXON | $413.41 | 20,906,151 | Industrials | large | unknown | 2026-10-04 |
| AXP | $302.69 | 43,121,931 | Unknown | large | unknown | 2026-10-04 |
| AZO | $2795.67 | 70,921,780 | Consumer Discretionary | large | unknown | 2026-10-04 |
| BA | $193.56 | 65,354,683 | Industrials | large | unknown | 2026-10-04 |
| BAC | $53.78 | 146,486,296 | Financials | large | unknown | 2026-10-04 |
| BE | $289.21 | 118,715,800 | Unknown | large | unknown | 2026-10-04 |
| BKNG | $159.02 | 101,603,087 | Consumer Discretionary | large | unknown | 2026-10-04 |
| BKR | $56.00 | 25,059,411 | Unknown | large | unknown | 2026-10-04 |
| BLK | $1059.76 | 31,006,250 | Unknown | large | unknown | 2026-10-04 |
| BMY | $61.16 | 44,026,060 | Health Care | large | unknown | 2026-10-04 |
| BNY | $145.38 | 24,227,320 | Unknown | large | unknown | 2026-10-04 |
| BRK.B | $502.69 | 77,092,942 | Financials | large | unknown | 2026-10-04 |
| BSX | $42.60 | 63,465,967 | Health Care | large | unknown | 2026-10-04 |
| BURL | $275.44 | 28,676,278 | Unknown | mid | unknown | 2026-10-04 |
| BX | $111.72 | 25,037,603 | Financials | large | unknown | 2026-10-04 |
| C | $128.53 | 50,702,801 | Financials | large | unknown | 2026-10-04 |
| CARR | $55.11 | 20,203,598 | Unknown | large | unknown | 2026-10-04 |
| CASY | $618.17 | 27,955,903 | Consumer Staples | large | unknown | 2026-10-04 |
| CAT | $845.57 | 69,615,131 | Industrials | large | unknown | 2026-10-04 |
| CB | $331.00 | 21,703,583 | Financials | large | unknown | 2026-10-04 |
| CCL | $25.78 | 37,534,539 | Unknown | large | unknown | 2026-10-04 |
| CDE | $17.66 | 22,877,349 | Unknown | mid | unknown | 2026-10-04 |
| CDNS | $351.49 | 43,222,620 | Unknown | large | unknown | 2026-10-04 |
| CEG | $257.52 | 28,688,916 | Unknown | large | unknown | 2026-10-04 |
| CI | $270.63 | 21,204,817 | Health Care | large | unknown | 2026-10-04 |
| CIEN | $391.38 | 44,106,017 | Unknown | large | unknown | 2026-10-04 |
| CL | $84.27 | 20,452,473 | Consumer Staples | large | unknown | 2026-10-04 |
| CMCSA | $21.58 | 41,762,641 | Unknown | large | unknown | 2026-10-04 |
| CME | $263.04 | 22,093,285 | Financials | large | unknown | 2026-10-04 |
| CMG | $32.43 | 32,272,881 | Consumer Discretionary | large | unknown | 2026-10-04 |
| CMI | $528.34 | 31,104,931 | Industrials | large | unknown | 2026-10-04 |
| COF | $194.71 | 32,234,611 | Financials | large | unknown | 2026-10-04 |
| COHR | $337.09 | 72,350,042 | Unknown | large | unknown | 2026-10-04 |
| COIN | $182.95 | 51,352,102 | Unknown | large | unknown | 2026-10-04 |
| COO | $56.92 | 20,768,302 | Unknown | large | unknown | 2026-10-04 |
| COP | $126.75 | 34,942,080 | Energy | large | unknown | 2026-10-04 |
| COR | $309.13 | 20,707,363 | Unknown | large | unknown | 2026-10-04 |
| COST | $920.83 | 78,767,158 | Consumer Staples | large | unknown | 2026-10-04 |
| CRH | $81.93 | 23,830,471 | Unknown | large | unknown | 2026-10-04 |
| CRM | $234.61 | 116,098,277 | Information Technology | large | unknown | 2026-10-04 |
| CRWD | $270.05 | 79,941,914 | Information Technology | large | unknown | 2026-10-04 |
| CSCO | $112.18 | 79,238,070 | Information Technology | large | unknown | 2026-10-04 |
| CSX | $47.45 | 40,915,560 | Industrials | large | unknown | 2026-10-04 |
| CTAS | $192.96 | 20,466,240 | Industrials | large | unknown | 2026-10-04 |
| CTSH | $58.52 | 20,918,230 | Information Technology | large | unknown | 2026-10-04 |
| CTVA | $11.92 | 21,343,208 | Materials | large | unknown | 2026-10-04 |
| CVNA | $63.76 | 25,592,465 | Unknown | large | unknown | 2026-10-04 |
| CVS | $86.49 | 36,480,559 | Health Care | large | unknown | 2026-10-04 |
| CVX | $206.71 | 64,351,694 | Energy | large | unknown | 2026-10-04 |
| D | $61.31 | 23,278,300 | Utilities | large | unknown | 2026-10-04 |
| DAL | $84.11 | 23,412,735 | Industrials | large | unknown | 2026-10-04 |
| DASH | $189.13 | 50,228,452 | Unknown | large | unknown | 2026-10-04 |
| DDOG | $277.27 | 44,547,388 | Unknown | large | unknown | 2026-10-04 |
| DE | $686.92 | 41,465,067 | Industrials | large | unknown | 2026-10-04 |
| DELL | $562.40 | 119,957,088 | Information Technology | large | unknown | 2026-10-04 |
| DHI | $135.00 | 25,023,874 | Consumer Discretionary | large | unknown | 2026-10-04 |
| DHR | $214.01 | 54,533,983 | Health Care | large | unknown | 2026-10-04 |
| DIS | $102.16 | 44,068,013 | Communication Services | large | unknown | 2026-10-04 |
| DKS | $135.87 | 21,487,535 | Consumer Discretionary | mid | unknown | 2026-10-04 |
| DOCN | $140.01 | 20,966,889 | Unknown | mid | unknown | 2026-10-04 |
| DT | $59.29 | 22,500,287 | Unknown | mid | unknown | 2026-10-04 |
| DVN | $47.68 | 41,955,217 | Energy | large | unknown | 2026-10-04 |
| EBAY | $106.44 | 21,541,547 | Consumer Discretionary | large | unknown | 2026-10-04 |
| ELV | $386.45 | 24,841,352 | Unknown | large | unknown | 2026-10-04 |
| EOG | $141.41 | 20,996,611 | Energy | large | unknown | 2026-10-04 |
| EQIX | $1025.89 | 28,294,730 | Real Estate | large | unknown | 2026-10-04 |
| EQT | $50.18 | 26,908,804 | Unknown | large | unknown | 2026-10-04 |
| ETN | $436.02 | 48,804,168 | Industrials | large | unknown | 2026-10-04 |
| EXPE | $265.04 | 40,918,912 | Consumer Discretionary | large | unknown | 2026-10-04 |
| F | $12.11 | 26,653,677 | Consumer Discretionary | large | unknown | 2026-10-04 |
| FANG | $184.63 | 31,994,704 | Unknown | large | unknown | 2026-10-04 |
| FCX | $72.05 | 44,494,757 | Materials | large | unknown | 2026-10-04 |
| FDX | $290.35 | 22,408,975 | Industrials | large | unknown | 2026-10-04 |
| FICO | $661.42 | 32,859,799 | Information Technology | large | unknown | 2026-10-04 |
| FITB | $50.89 | 27,126,679 | Financials | large | unknown | 2026-10-04 |
| FIX | $1728.54 | 24,017,206 | Unknown | large | unknown | 2026-10-04 |
| FTNT | $180.94 | 23,993,286 | Information Technology | large | unknown | 2026-10-04 |
| GD | $330.07 | 21,335,220 | Industrials | large | unknown | 2026-10-04 |
| GE | $309.55 | 51,938,417 | Industrials | large | unknown | 2026-10-04 |
| GEV | $989.42 | 83,112,889 | Industrials | large | unknown | 2026-10-04 |
| GILD | $144.72 | 34,043,547 | Health Care | large | unknown | 2026-10-04 |
| GIS | $32.02 | 22,239,141 | Consumer Staples | large | unknown | 2026-10-04 |
| GLW | $164.14 | 50,755,634 | Information Technology | large | unknown | 2026-10-04 |
| GM | $78.29 | 42,201,616 | Consumer Discretionary | large | unknown | 2026-10-04 |
| GOOG | $340.35 | 157,899,275 | Communication Services | large | unknown | 2026-10-04 |
| GOOGL | $343.47 | 274,883,725 | Communication Services | large | unknown | 2026-10-04 |
| GS | $902.68 | 74,517,395 | Financials | large | unknown | 2026-10-04 |
| GWW | $1280.89 | 25,037,631 | Industrials | large | unknown | 2026-10-04 |
| HAL | $31.85 | 25,180,771 | Energy | large | unknown | 2026-10-04 |
| HBAN | $15.32 | 28,464,821 | Financials | large | unknown | 2026-10-04 |
| HCA | $426.74 | 30,629,846 | Health Care | large | unknown | 2026-10-04 |
| HD | $282.88 | 69,241,302 | Consumer Discretionary | large | unknown | 2026-10-04 |
| HLT | $319.33 | 33,135,539 | Consumer Discretionary | large | unknown | 2026-10-04 |
| HON | $213.99 | 21,550,048 | Industrials | large | unknown | 2026-10-04 |
| HONA | $154.48 | 30,722,582 | Unknown | large | unknown | 2026-10-04 |
| HOOD | $112.68 | 72,228,762 | Unknown | large | unknown | 2026-10-04 |
| HPE | $69.32 | 64,546,738 | Information Technology | large | unknown | 2026-10-04 |
| HPQ | $32.12 | 35,502,118 | Information Technology | large | unknown | 2026-10-04 |
| HUBS | $214.63 | 20,599,950 | Unknown | mid | unknown | 2026-10-04 |
| HUM | $388.56 | 22,371,468 | Health Care | large | unknown | 2026-10-04 |
| HWM | $231.34 | 41,345,825 | Industrials | large | unknown | 2026-10-04 |
| IBM | $222.63 | 48,677,762 | Information Technology | large | unknown | 2026-10-04 |
| ICE | $150.08 | 22,823,536 | Financials | large | unknown | 2026-10-04 |
| ILMN | $273.04 | 43,635,036 | Health Care | large | unknown | 2026-10-04 |
| INTC | $119.32 | 300,810,643 | Information Technology | large | unknown | 2026-10-04 |
| INTU | $280.99 | 48,372,852 | Information Technology | large | unknown | 2026-10-04 |
| IQV | $258.31 | 24,332,132 | Health Care | large | unknown | 2026-10-04 |
| IR | $76.06 | 20,489,669 | Industrials | large | unknown | 2026-10-04 |
| ISRG | $391.92 | 47,080,159 | Health Care | large | unknown | 2026-10-04 |
| JBL | $304.36 | 30,816,410 | Unknown | large | unknown | 2026-10-04 |
| JCI | $156.21 | 20,955,019 | Industrials | large | unknown | 2026-10-04 |
| JNJ | $256.02 | 63,273,895 | Health Care | large | unknown | 2026-10-04 |
| JPM | $332.22 | 97,778,823 | Financials | large | unknown | 2026-10-04 |
| KDP | $30.37 | 23,850,976 | Consumer Staples | large | unknown | 2026-10-04 |
| KHC | $22.19 | 23,759,349 | Consumer Staples | large | unknown | 2026-10-04 |
| KKR | $90.28 | 23,634,919 | Unknown | large | unknown | 2026-10-04 |
| KLAC | $206.71 | 60,556,067 | Information Technology | large | unknown | 2026-10-04 |
| KMI | $31.07 | 29,931,805 | Energy | large | unknown | 2026-10-04 |
| KO | $85.66 | 86,847,146 | Consumer Staples | large | unknown | 2026-10-04 |
| KR | $59.02 | 32,439,271 | Consumer Staples | large | unknown | 2026-10-04 |
| KVUE | $17.22 | 36,890,302 | Unknown | large | unknown | 2026-10-04 |
| LEN | $79.78 | 21,068,496 | Consumer Discretionary | large | unknown | 2026-10-04 |
| LHX | $236.60 | 20,747,331 | Industrials | large | unknown | 2026-10-04 |
| LIN | $479.39 | 45,810,047 | Materials | large | unknown | 2026-10-04 |
| LITE | $1085.12 | 142,197,982 | Unknown | large | unknown | 2026-10-04 |
| LLY | $1143.54 | 95,926,293 | Health Care | large | unknown | 2026-10-04 |
| LMT | $506.25 | 21,990,773 | Industrials | large | unknown | 2026-10-04 |
| LOW | $180.78 | 24,659,116 | Consumer Discretionary | large | unknown | 2026-10-04 |
| LRCX | $347.46 | 118,337,497 | Information Technology | large | unknown | 2026-10-04 |
| LULU | $94.46 | 24,708,688 | Unknown | large | unknown | 2026-10-04 |
| MA | $552.44 | 68,196,211 | Financials | large | unknown | 2026-10-04 |
| MAR | $358.96 | 29,447,182 | Unknown | large | unknown | 2026-10-04 |
| MCD | $231.99 | 48,753,171 | Consumer Discretionary | large | unknown | 2026-10-04 |
| MCHP | $81.31 | 21,884,621 | Information Technology | large | unknown | 2026-10-04 |
| MCK | $902.73 | 30,897,910 | Health Care | large | unknown | 2026-10-04 |
| MDLZ | $58.19 | 29,741,521 | Consumer Staples | large | unknown | 2026-10-04 |
| MDT | $86.35 | 69,819,067 | Health Care | large | unknown | 2026-10-04 |
| META | $728.09 | 560,309,592 | Communication Services | large | unknown | 2026-10-04 |
| MLM | $482.62 | 29,803,296 | Materials | large | unknown | 2026-10-04 |
| MMM | $161.90 | 22,661,405 | Industrials | large | unknown | 2026-10-04 |
| MNST | $42.95 | 26,499,531 | Consumer Staples | large | unknown | 2026-10-04 |
| MO | $67.37 | 27,443,128 | Consumer Staples | large | unknown | 2026-10-04 |
| MPC | $422.36 | 49,171,296 | Energy | large | unknown | 2026-10-04 |
| MPWR | $1438.95 | 44,003,243 | Information Technology | large | unknown | 2026-10-04 |
| MRK | $144.31 | 45,940,446 | Health Care | large | unknown | 2026-10-04 |
| MRNA | $189.97 | 76,310,694 | Health Care | large | unknown | 2026-10-04 |
| MRSH | $170.14 | 20,829,483 | Unknown | large | unknown | 2026-10-04 |
| MRVL | $272.33 | 98,963,543 | Unknown | large | unknown | 2026-10-04 |
| MS | $190.25 | 51,105,928 | Financials | large | unknown | 2026-10-04 |
| MSFT | $517.32 | 326,819,243 | Information Technology | large | unknown | 2026-10-04 |
| MSI | $447.54 | 21,965,357 | Information Technology | large | unknown | 2026-10-04 |
| MTD | $1486.37 | 20,265,259 | Health Care | large | unknown | 2026-10-04 |
| MTZ | $215.95 | 22,593,524 | Unknown | mid | unknown | 2026-10-04 |
| MU | $1074.71 | 611,271,947 | Information Technology | large | unknown | 2026-10-04 |
| NEE | $76.82 | 64,628,068 | Utilities | large | unknown | 2026-10-04 |
| NEM | $115.56 | 31,956,874 | Materials | large | unknown | 2026-10-04 |
| NFLX | $67.07 | 128,729,692 | Communication Services | large | unknown | 2026-10-04 |
| NKE | $33.89 | 69,418,334 | Consumer Discretionary | large | unknown | 2026-10-04 |
| NOC | $478.12 | 27,426,324 | Industrials | large | unknown | 2026-10-04 |
| NOW | $134.35 | 61,316,234 | Information Technology | large | unknown | 2026-10-04 |
| NTAP | $226.51 | 27,215,462 | Information Technology | large | unknown | 2026-10-04 |
| NVDA | $234.00 | 611,470,040 | Information Technology | large | unknown | 2026-10-04 |
| NXPI | $243.70 | 24,684,117 | Unknown | large | unknown | 2026-10-04 |
| O | $54.13 | 26,326,724 | Real Estate | large | unknown | 2026-10-04 |
| OKTA | $211.31 | 36,252,179 | Information Technology | mid | unknown | 2026-10-04 |
| ON | $84.88 | 38,711,811 | Information Technology | large | unknown | 2026-10-04 |
| ORCL | $142.41 | 155,012,988 | Information Technology | large | unknown | 2026-10-04 |
| ORLY | $84.89 | 21,271,209 | Consumer Discretionary | large | unknown | 2026-10-04 |
| OXY | $58.10 | 38,695,535 | Energy | large | unknown | 2026-10-04 |
| P | $140.13 | 23,829,222 | Unknown | large | unknown | 2026-10-04 |
| PANW | $403.22 | 84,283,105 | Unknown | large | unknown | 2026-10-04 |
| PATH | $13.11 | 25,497,632 | Unknown | mid | unknown | 2026-10-04 |
| PCAR | $109.71 | 20,325,071 | Industrials | large | unknown | 2026-10-04 |
| PCG | $12.30 | 29,563,524 | Utilities | large | unknown | 2026-10-04 |
| PEP | $125.86 | 48,505,104 | Consumer Staples | large | unknown | 2026-10-04 |
| PFE | $27.80 | 44,400,670 | Health Care | large | unknown | 2026-10-04 |
| PG | $144.89 | 50,376,555 | Consumer Staples | large | unknown | 2026-10-04 |
| PGR | $210.40 | 35,401,622 | Financials | large | unknown | 2026-10-04 |
| PH | $972.55 | 27,534,235 | Industrials | large | unknown | 2026-10-04 |
| PLTR | $188.80 | 96,795,309 | Unknown | large | unknown | 2026-10-04 |
| PM | $187.46 | 32,192,079 | Consumer Staples | large | unknown | 2026-10-04 |
| PSX | $264.57 | 48,744,315 | Energy | large | unknown | 2026-10-04 |
| PWR | $677.10 | 28,133,279 | Industrials | large | unknown | 2026-10-04 |
| PYPL | $52.78 | 27,518,898 | Financials | large | unknown | 2026-10-04 |
| QCOM | $184.85 | 78,844,882 | Information Technology | large | unknown | 2026-10-04 |
| RCL | $277.89 | 51,987,317 | Consumer Discretionary | large | unknown | 2026-10-04 |
| RDDT | $148.01 | 30,375,289 | Unknown | large | unknown | 2026-10-04 |
| REGN | $735.28 | 24,627,595 | Health Care | large | unknown | 2026-10-04 |
| ROST | $228.54 | 22,071,996 | Consumer Discretionary | large | unknown | 2026-10-04 |
| RTX | $184.64 | 28,007,711 | Industrials | large | unknown | 2026-10-04 |
| RVTY | $151.43 | 20,092,583 | Unknown | large | unknown | 2026-10-04 |
| SBUX | $94.73 | 28,918,540 | Consumer Discretionary | large | unknown | 2026-10-04 |
| SCHW | $96.69 | 41,013,159 | Financials | large | unknown | 2026-10-04 |
| SHW | $319.57 | 23,279,945 | Materials | large | unknown | 2026-10-04 |
| SLB | $48.74 | 42,500,430 | Energy | large | unknown | 2026-10-04 |
| SMCI | $43.69 | 63,509,737 | Information Technology | large | unknown | 2026-10-04 |
| SMTC | $194.91 | 32,183,994 | Information Technology | mid | unknown | 2026-10-04 |
| SNDK | $1719.36 | 328,992,681 | Unknown | large | unknown | 2026-10-04 |
| SNPS | $490.00 | 45,889,169 | Information Technology | large | unknown | 2026-10-04 |
| SO | $83.73 | 22,361,250 | Utilities | large | unknown | 2026-10-04 |
| SPGI | $386.24 | 35,699,454 | Financials | large | unknown | 2026-10-04 |
| STX | $848.78 | 135,459,399 | Information Technology | large | unknown | 2026-10-04 |
| SWKS | $85.05 | 31,029,997 | Information Technology | large | unknown | 2026-10-04 |
| SYK | $275.47 | 50,016,002 | Health Care | large | unknown | 2026-10-04 |
| T | $24.31 | 47,664,596 | Communication Services | large | unknown | 2026-10-04 |
| TDG | $1090.40 | 25,412,545 | Industrials | large | unknown | 2026-10-04 |
| TEL | $220.27 | 22,343,204 | Information Technology | large | unknown | 2026-10-04 |
| TER | $448.65 | 36,652,006 | Information Technology | large | unknown | 2026-10-04 |
| TFC | $46.46 | 22,648,547 | Financials | large | unknown | 2026-10-04 |
| TGT | $155.95 | 23,674,021 | Consumer Discretionary | large | unknown | 2026-10-04 |
| TJX | $132.74 | 59,226,453 | Consumer Discretionary | large | unknown | 2026-10-04 |
| TMO | $655.10 | 85,943,572 | Health Care | large | unknown | 2026-10-04 |
| TMUS | $163.56 | 44,153,352 | Communication Services | large | unknown | 2026-10-04 |
| TRV | $360.56 | 20,138,190 | Financials | large | unknown | 2026-10-04 |
| TSCO | $31.10 | 20,333,283 | Consumer Discretionary | large | unknown | 2026-10-04 |
| TSLA | $370.64 | 275,053,831 | Consumer Discretionary | large | unknown | 2026-10-04 |
| TT | $463.88 | 31,504,880 | Industrials | large | unknown | 2026-10-04 |
| TTWO | $202.76 | 23,482,348 | Communication Services | large | unknown | 2026-10-04 |
| TWLO | $294.54 | 40,429,155 | Unknown | mid | unknown | 2026-10-04 |
| TXN | $293.74 | 56,613,981 | Information Technology | large | unknown | 2026-10-04 |
| UBER | $68.10 | 54,204,144 | Unknown | large | unknown | 2026-10-04 |
| UNH | $371.77 | 71,593,977 | Health Care | large | unknown | 2026-10-04 |
| UNP | $278.27 | 33,347,146 | Industrials | large | unknown | 2026-10-04 |
| URI | $1081.01 | 32,117,125 | Industrials | large | unknown | 2026-10-04 |
| USB | $57.51 | 31,269,088 | Financials | large | unknown | 2026-10-04 |
| UTHR | $541.53 | 25,904,954 | Health Care | mid | unknown | 2026-10-04 |
| V | $360.62 | 80,514,720 | Financials | large | unknown | 2026-10-04 |
| VLO | $405.66 | 71,392,061 | Energy | large | unknown | 2026-10-04 |
| VRT | $252.15 | 67,051,552 | Unknown | large | unknown | 2026-10-04 |
| VRTX | $504.69 | 21,047,340 | Health Care | large | unknown | 2026-10-04 |
| VST | $140.06 | 30,486,741 | Utilities | large | unknown | 2026-10-04 |
| VZ | $45.94 | 54,231,677 | Communication Services | large | unknown | 2026-10-04 |
| WBD | $30.94 | 89,105,932 | Communication Services | large | unknown | 2026-10-04 |
| WDAY | $186.07 | 21,169,308 | Unknown | large | unknown | 2026-10-04 |
| WDC | $415.37 | 123,949,222 | Information Technology | large | unknown | 2026-10-04 |
| WELL | $227.96 | 25,605,222 | Real Estate | large | unknown | 2026-10-04 |
| WFC | $80.45 | 61,526,728 | Financials | large | unknown | 2026-10-04 |
| WM | $204.54 | 22,295,024 | Industrials | large | unknown | 2026-10-04 |
| WMB | $70.54 | 27,394,754 | Energy | large | unknown | 2026-10-04 |
| WMT | $104.29 | 86,330,787 | Consumer Staples | large | unknown | 2026-10-04 |
| XEL | $71.41 | 27,690,505 | Utilities | large | unknown | 2026-10-04 |
| XOM | $164.11 | 68,053,114 | Energy | large | unknown | 2026-10-04 |
| YUM | $136.21 | 20,966,050 | Consumer Discretionary | large | unknown | 2026-10-04 |
