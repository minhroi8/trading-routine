---
screened_on: 2026-05-31
expires_on: 2026-06-07
total_passed: 303
total_rejected: 1203
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
| AAL | $14.62 | 33,058,238 | Unknown | mid | unknown | 2026-05-31 |
| AAPL | $312.01 | 416,597,323 | Unknown | large | unknown | 2026-05-31 |
| ABBV | $217.76 | 51,086,949 | Unknown | large | unknown | 2026-05-31 |
| ABNB | $133.29 | 27,112,882 | Unknown | large | unknown | 2026-05-31 |
| ABT | $85.58 | 50,085,505 | Unknown | large | unknown | 2026-05-31 |
| ACN | $187.13 | 51,297,060 | Unknown | large | unknown | 2026-05-31 |
| ADBE | $259.17 | 40,272,756 | Unknown | large | unknown | 2026-05-31 |
| ADI | $413.90 | 79,033,247 | Unknown | large | unknown | 2026-05-31 |
| ADP | $221.94 | 28,146,941 | Unknown | large | unknown | 2026-05-31 |
| ADSK | $231.41 | 30,810,958 | Unknown | large | unknown | 2026-05-31 |
| AEIS | $302.43 | 28,341,381 | Unknown | mid | unknown | 2026-05-31 |
| AEP | $126.77 | 34,056,681 | Unknown | large | unknown | 2026-05-31 |
| AJG | $201.12 | 26,881,453 | Unknown | large | unknown | 2026-05-31 |
| AKAM | $149.57 | 46,306,766 | Unknown | large | unknown | 2026-05-31 |
| ALB | $176.37 | 20,883,995 | Unknown | large | unknown | 2026-05-31 |
| ALL | $206.05 | 22,023,640 | Unknown | large | unknown | 2026-05-31 |
| AMAT | $450.24 | 104,542,882 | Unknown | large | unknown | 2026-05-31 |
| AMD | $516.26 | 348,849,059 | Unknown | large | unknown | 2026-05-31 |
| AMGN | $336.77 | 25,594,286 | Unknown | large | unknown | 2026-05-31 |
| AMT | $186.85 | 26,197,035 | Unknown | large | unknown | 2026-05-31 |
| AMZN | $270.61 | 466,726,357 | Unknown | large | unknown | 2026-05-31 |
| ANET | $159.52 | 90,735,367 | Unknown | large | unknown | 2026-05-31 |
| AON | $315.98 | 32,093,196 | Unknown | large | unknown | 2026-05-31 |
| APH | $148.80 | 86,310,857 | Unknown | large | unknown | 2026-05-31 |
| APO | $128.62 | 26,018,918 | Unknown | large | unknown | 2026-05-31 |
| APP | $612.97 | 117,065,643 | Unknown | large | unknown | 2026-05-31 |
| ARES | $128.50 | 25,745,028 | Unknown | large | unknown | 2026-05-31 |
| AVGO | $447.41 | 264,755,511 | Unknown | large | unknown | 2026-05-31 |
| AXON | $448.76 | 23,271,999 | Unknown | large | unknown | 2026-05-31 |
| AXP | $316.54 | 38,889,102 | Unknown | large | unknown | 2026-05-31 |
| AZO | $2936.08 | 53,434,935 | Unknown | large | unknown | 2026-05-31 |
| BA | $231.20 | 52,245,890 | Unknown | large | unknown | 2026-05-31 |
| BAC | $51.61 | 114,815,539 | Unknown | large | unknown | 2026-05-31 |
| BDX | $147.15 | 29,840,320 | Unknown | large | unknown | 2026-05-31 |
| BKNG | $167.43 | 61,967,003 | Unknown | large | unknown | 2026-05-31 |
| BKR | $63.89 | 28,198,146 | Unknown | large | unknown | 2026-05-31 |
| BLD | $417.89 | 23,630,940 | Unknown | mid | unknown | 2026-05-31 |
| BLK | $1046.57 | 36,877,999 | Unknown | large | unknown | 2026-05-31 |
| BMY | $57.18 | 36,556,900 | Unknown | large | unknown | 2026-05-31 |
| BNY | $139.47 | 21,605,277 | Unknown | large | unknown | 2026-05-31 |
| BRK.B | $474.49 | 64,868,721 | Unknown | large | unknown | 2026-05-31 |
| BSX | $48.34 | 72,928,327 | Unknown | large | unknown | 2026-05-31 |
| BURL | $323.50 | 29,152,966 | Unknown | mid | unknown | 2026-05-31 |
| BX | $116.98 | 22,246,802 | Unknown | large | unknown | 2026-05-31 |
| C | $125.88 | 61,537,438 | Unknown | large | unknown | 2026-05-31 |
| CAH | $196.79 | 28,363,449 | Unknown | large | unknown | 2026-05-31 |
| CARR | $63.97 | 22,873,233 | Unknown | large | unknown | 2026-05-31 |
| CASY | $767.34 | 30,774,630 | Unknown | large | unknown | 2026-05-31 |
| CAT | $875.74 | 94,536,856 | Unknown | large | unknown | 2026-05-31 |
| CB | $311.76 | 21,237,753 | Unknown | large | unknown | 2026-05-31 |
| CBOE | $332.81 | 24,604,315 | Unknown | large | unknown | 2026-05-31 |
| CCL | $28.06 | 43,710,058 | Unknown | large | unknown | 2026-05-31 |
| CDNS | $374.97 | 34,462,380 | Unknown | large | unknown | 2026-05-31 |
| CEG | $287.79 | 55,214,260 | Unknown | large | unknown | 2026-05-31 |
| CF | $112.38 | 20,362,062 | Unknown | large | unknown | 2026-05-31 |
| CHRW | $178.67 | 23,296,887 | Unknown | large | unknown | 2026-05-31 |
| CHTR | $144.09 | 22,228,843 | Unknown | large | unknown | 2026-05-31 |
| CI | $277.32 | 22,512,125 | Unknown | large | unknown | 2026-05-31 |
| CIEN | $582.13 | 57,141,895 | Unknown | large | unknown | 2026-05-31 |
| CL | $90.14 | 27,569,418 | Unknown | large | unknown | 2026-05-31 |
| CMCSA | $24.85 | 58,035,599 | Unknown | large | unknown | 2026-05-31 |
| CME | $273.52 | 32,188,423 | Unknown | large | unknown | 2026-05-31 |
| CMG | $31.88 | 36,335,748 | Unknown | large | unknown | 2026-05-31 |
| CMI | $646.78 | 41,465,873 | Unknown | large | unknown | 2026-05-31 |
| COF | $187.87 | 52,499,031 | Unknown | large | unknown | 2026-05-31 |
| COHR | $361.85 | 95,370,701 | Unknown | large | unknown | 2026-05-31 |
| COIN | $189.01 | 46,233,581 | Unknown | large | unknown | 2026-05-31 |
| COP | $114.03 | 54,968,335 | Unknown | large | unknown | 2026-05-31 |
| COR | $269.40 | 40,123,760 | Unknown | large | unknown | 2026-05-31 |
| COST | $956.10 | 78,006,988 | Unknown | large | unknown | 2026-05-31 |
| CPRT | $32.76 | 21,276,916 | Unknown | large | unknown | 2026-05-31 |
| CRH | $108.82 | 25,192,699 | Unknown | large | unknown | 2026-05-31 |
| CRM | $191.12 | 91,151,278 | Unknown | large | unknown | 2026-05-31 |
| CRS | $468.82 | 21,385,164 | Unknown | mid | unknown | 2026-05-31 |
| CRWD | $731.09 | 69,408,170 | Unknown | large | unknown | 2026-05-31 |
| CSCO | $120.46 | 133,370,633 | Unknown | large | unknown | 2026-05-31 |
| CSX | $45.26 | 40,413,699 | Unknown | large | unknown | 2026-05-31 |
| CTSH | $55.75 | 25,388,427 | Unknown | large | unknown | 2026-05-31 |
| CVNA | $73.04 | 38,419,998 | Unknown | large | unknown | 2026-05-31 |
| CVS | $90.99 | 46,234,457 | Unknown | large | unknown | 2026-05-31 |
| CVX | $182.46 | 56,138,366 | Unknown | large | unknown | 2026-05-31 |
| D | $66.96 | 37,157,922 | Unknown | large | unknown | 2026-05-31 |
| DAL | $82.52 | 27,481,400 | Unknown | large | unknown | 2026-05-31 |
| DASH | $159.23 | 47,224,983 | Unknown | large | unknown | 2026-05-31 |
| DDOG | $247.45 | 63,293,179 | Unknown | large | unknown | 2026-05-31 |
| DE | $542.44 | 38,758,557 | Unknown | large | unknown | 2026-05-31 |
| DELL | $421.61 | 92,500,974 | Unknown | large | unknown | 2026-05-31 |
| DG | $110.58 | 25,032,628 | Unknown | large | unknown | 2026-05-31 |
| DHR | $182.74 | 54,281,631 | Unknown | large | unknown | 2026-05-31 |
| DIS | $101.87 | 50,166,951 | Unknown | large | unknown | 2026-05-31 |
| DKS | $227.54 | 20,363,022 | Unknown | mid | unknown | 2026-05-31 |
| DLTR | $116.47 | 21,655,615 | Unknown | large | unknown | 2026-05-31 |
| DOCN | $156.07 | 27,851,690 | Unknown | mid | unknown | 2026-05-31 |
| DOW | $33.77 | 29,684,649 | Unknown | large | unknown | 2026-05-31 |
| DT | $42.59 | 21,660,939 | Unknown | mid | unknown | 2026-05-31 |
| DVN | $44.51 | 42,600,750 | Unknown | large | unknown | 2026-05-31 |
| DXCM | $73.77 | 25,893,727 | Unknown | large | unknown | 2026-05-31 |
| EBAY | $109.29 | 34,461,302 | Unknown | large | unknown | 2026-05-31 |
| ECL | $256.07 | 23,033,982 | Unknown | large | unknown | 2026-05-31 |
| ELV | $393.76 | 28,643,699 | Unknown | large | unknown | 2026-05-31 |
| EME | $827.50 | 23,475,980 | Unknown | large | unknown | 2026-05-31 |
| EMR | $143.88 | 24,602,814 | Unknown | large | unknown | 2026-05-31 |
| ENTG | $138.88 | 22,163,203 | Unknown | mid | unknown | 2026-05-31 |
| EOG | $133.46 | 27,520,083 | Unknown | large | unknown | 2026-05-31 |
| EQIX | $1067.71 | 28,445,679 | Unknown | large | unknown | 2026-05-31 |
| EQT | $54.90 | 30,388,593 | Unknown | large | unknown | 2026-05-31 |
| ETN | $400.75 | 72,968,521 | Unknown | large | unknown | 2026-05-31 |
| EW | $86.49 | 20,442,452 | Unknown | large | unknown | 2026-05-31 |
| EXC | $45.64 | 21,545,799 | Unknown | large | unknown | 2026-05-31 |
| EXPE | $225.78 | 22,199,414 | Unknown | large | unknown | 2026-05-31 |
| F | $17.45 | 77,804,839 | Unknown | large | unknown | 2026-05-31 |
| FCX | $65.73 | 54,580,591 | Unknown | large | unknown | 2026-05-31 |
| FDX | $411.69 | 31,091,807 | Unknown | large | unknown | 2026-05-31 |
| FICO | $1251.06 | 32,974,224 | Unknown | large | unknown | 2026-05-31 |
| FIS | $43.01 | 22,851,109 | Unknown | large | unknown | 2026-05-31 |
| FITB | $49.94 | 23,274,395 | Unknown | large | unknown | 2026-05-31 |
| FIX | $1828.62 | 44,008,812 | Unknown | large | unknown | 2026-05-31 |
| FLEX | $150.83 | 55,488,295 | Unknown | mid | unknown | 2026-05-31 |
| FN | $653.84 | 51,335,764 | Unknown | mid | unknown | 2026-05-31 |
| FSLR | $306.75 | 33,262,742 | Unknown | large | unknown | 2026-05-31 |
| FTI | $68.41 | 27,124,702 | Unknown | mid | unknown | 2026-05-31 |
| FTNT | $137.93 | 33,390,378 | Unknown | large | unknown | 2026-05-31 |
| GD | $346.88 | 21,445,439 | Unknown | large | unknown | 2026-05-31 |
| GE | $323.88 | 72,078,424 | Unknown | large | unknown | 2026-05-31 |
| GEV | $969.34 | 99,429,531 | Unknown | large | unknown | 2026-05-31 |
| GILD | $134.46 | 35,456,005 | Unknown | large | unknown | 2026-05-31 |
| GLW | $181.29 | 112,283,811 | Unknown | large | unknown | 2026-05-31 |
| GM | $83.25 | 28,763,606 | Unknown | large | unknown | 2026-05-31 |
| GOOG | $376.37 | 183,100,957 | Unknown | large | unknown | 2026-05-31 |
| GOOGL | $380.38 | 366,886,108 | Unknown | large | unknown | 2026-05-31 |
| GS | $1025.61 | 66,956,313 | Unknown | large | unknown | 2026-05-31 |
| GWW | $1234.52 | 25,657,032 | Unknown | large | unknown | 2026-05-31 |
| HAL | $38.85 | 27,384,067 | Unknown | large | unknown | 2026-05-31 |
| HBAN | $16.36 | 21,096,738 | Unknown | large | unknown | 2026-05-31 |
| HCA | $378.50 | 33,001,628 | Unknown | large | unknown | 2026-05-31 |
| HD | $317.20 | 72,563,411 | Unknown | large | unknown | 2026-05-31 |
| HLT | $327.88 | 28,559,648 | Unknown | large | unknown | 2026-05-31 |
| HON | $238.01 | 33,072,921 | Unknown | large | unknown | 2026-05-31 |
| HOOD | $94.35 | 65,673,370 | Unknown | large | unknown | 2026-05-31 |
| HPE | $43.09 | 62,497,808 | Unknown | large | unknown | 2026-05-31 |
| HPQ | $27.06 | 31,898,313 | Unknown | large | unknown | 2026-05-31 |
| HSY | $194.12 | 20,695,277 | Unknown | large | unknown | 2026-05-31 |
| HUBB | $473.47 | 29,892,304 | Unknown | large | unknown | 2026-05-31 |
| HUM | $305.60 | 26,400,956 | Unknown | large | unknown | 2026-05-31 |
| HWM | $258.40 | 33,524,565 | Unknown | large | unknown | 2026-05-31 |
| IBM | $297.97 | 76,085,612 | Unknown | large | unknown | 2026-05-31 |
| ICE | $147.79 | 25,064,642 | Unknown | large | unknown | 2026-05-31 |
| IDXX | $563.00 | 21,122,118 | Unknown | large | unknown | 2026-05-31 |
| INTC | $114.67 | 362,081,662 | Unknown | large | unknown | 2026-05-31 |
| INTU | $331.58 | 103,114,236 | Unknown | large | unknown | 2026-05-31 |
| IQV | $182.22 | 21,247,482 | Unknown | large | unknown | 2026-05-31 |
| ISRG | $424.38 | 43,738,783 | Unknown | large | unknown | 2026-05-31 |
| ITW | $247.24 | 21,211,484 | Unknown | large | unknown | 2026-05-31 |
| JBL | $364.53 | 29,189,455 | Unknown | large | unknown | 2026-05-31 |
| JCI | $134.08 | 23,135,892 | Unknown | large | unknown | 2026-05-31 |
| JNJ | $225.23 | 60,105,324 | Unknown | large | unknown | 2026-05-31 |
| JPM | $299.33 | 72,135,774 | Unknown | large | unknown | 2026-05-31 |
| KDP | $30.05 | 23,483,829 | Unknown | large | unknown | 2026-05-31 |
| KEYS | $338.44 | 38,375,382 | Unknown | large | unknown | 2026-05-31 |
| KKR | $96.02 | 32,228,932 | Unknown | large | unknown | 2026-05-31 |
| KLAC | $1922.91 | 104,522,835 | Unknown | large | unknown | 2026-05-31 |
| KMI | $31.09 | 21,890,281 | Unknown | large | unknown | 2026-05-31 |
| KNX | $75.62 | 21,038,058 | Unknown | mid | unknown | 2026-05-31 |
| KO | $79.01 | 65,131,623 | Unknown | large | unknown | 2026-05-31 |
| KVUE | $17.29 | 21,784,619 | Unknown | large | unknown | 2026-05-31 |
| LHX | $315.19 | 23,554,963 | Unknown | large | unknown | 2026-05-31 |
| LIN | $497.72 | 44,366,472 | Unknown | large | unknown | 2026-05-31 |
| LITE | $854.97 | 197,307,041 | Unknown | large | unknown | 2026-05-31 |
| LLY | $1105.00 | 135,311,016 | Unknown | large | unknown | 2026-05-31 |
| LMT | $530.49 | 29,316,494 | Unknown | large | unknown | 2026-05-31 |
| LOW | $214.26 | 35,659,340 | Unknown | large | unknown | 2026-05-31 |
| LRCX | $318.33 | 93,311,214 | Unknown | large | unknown | 2026-05-31 |
| LSCC | $147.20 | 28,356,849 | Unknown | mid | unknown | 2026-05-31 |
| LYB | $66.65 | 23,936,458 | Unknown | large | unknown | 2026-05-31 |
| LYV | $168.65 | 20,164,849 | Unknown | large | unknown | 2026-05-31 |
| MA | $494.20 | 103,541,843 | Unknown | large | unknown | 2026-05-31 |
| MAR | $375.63 | 28,343,961 | Unknown | large | unknown | 2026-05-31 |
| MCD | $279.31 | 44,397,989 | Unknown | large | unknown | 2026-05-31 |
| MCHP | $94.68 | 52,221,715 | Unknown | large | unknown | 2026-05-31 |
| MCK | $742.57 | 58,071,758 | Unknown | large | unknown | 2026-05-31 |
| MCO | $453.27 | 34,016,219 | Unknown | large | unknown | 2026-05-31 |
| MDLZ | $61.17 | 26,411,541 | Unknown | large | unknown | 2026-05-31 |
| MDT | $73.82 | 54,106,740 | Unknown | large | unknown | 2026-05-31 |
| META | $632.52 | 262,186,009 | Unknown | large | unknown | 2026-05-31 |
| MKSI | $324.74 | 26,912,376 | Unknown | mid | unknown | 2026-05-31 |
| MLM | $581.86 | 26,993,540 | Unknown | large | unknown | 2026-05-31 |
| MMM | $153.18 | 25,464,084 | Unknown | large | unknown | 2026-05-31 |
| MNST | $88.08 | 25,415,594 | Unknown | large | unknown | 2026-05-31 |
| MO | $69.61 | 39,944,745 | Unknown | large | unknown | 2026-05-31 |
| MPC | $248.71 | 26,414,585 | Unknown | large | unknown | 2026-05-31 |
| MPWR | $1566.50 | 53,694,671 | Unknown | large | unknown | 2026-05-31 |
| MRK | $118.73 | 40,269,631 | Unknown | large | unknown | 2026-05-31 |
| MRSH | $159.98 | 23,030,165 | Unknown | large | unknown | 2026-05-31 |
| MS | $208.04 | 57,187,599 | Unknown | large | unknown | 2026-05-31 |
| MSCI | $630.76 | 28,098,454 | Unknown | large | unknown | 2026-05-31 |
| MSFT | $449.44 | 353,846,483 | Unknown | large | unknown | 2026-05-31 |
| MSI | $403.24 | 36,708,115 | Unknown | large | unknown | 2026-05-31 |
| MTD | $1183.00 | 24,625,571 | Unknown | large | unknown | 2026-05-31 |
| MTSI | $364.76 | 32,358,381 | Unknown | mid | unknown | 2026-05-31 |
| MTZ | $378.31 | 29,424,722 | Unknown | mid | unknown | 2026-05-31 |
| MU | $970.64 | 725,557,443 | Unknown | large | unknown | 2026-05-31 |
| NCLH | $18.34 | 23,202,030 | Unknown | large | unknown | 2026-05-31 |
| NEE | $86.97 | 66,659,042 | Unknown | large | unknown | 2026-05-31 |
| NEM | $109.85 | 28,914,158 | Unknown | large | unknown | 2026-05-31 |
| NFLX | $86.01 | 172,920,874 | Unknown | large | unknown | 2026-05-31 |
| NKE | $46.22 | 46,068,604 | Unknown | large | unknown | 2026-05-31 |
| NOC | $563.71 | 21,695,633 | Unknown | large | unknown | 2026-05-31 |
| NOW | $124.48 | 107,498,065 | Unknown | large | unknown | 2026-05-31 |
| NRG | $134.03 | 26,452,949 | Unknown | large | unknown | 2026-05-31 |
| NTAP | $173.94 | 29,042,712 | Unknown | large | unknown | 2026-05-31 |
| NVDA | $211.16 | 957,316,733 | Unknown | large | unknown | 2026-05-31 |
| NXPI | $321.38 | 54,234,445 | Unknown | large | unknown | 2026-05-31 |
| NXT | $156.41 | 22,018,286 | Unknown | mid | unknown | 2026-05-31 |
| O | $61.27 | 20,415,731 | Unknown | large | unknown | 2026-05-31 |
| ODFL | $225.21 | 24,309,956 | Unknown | large | unknown | 2026-05-31 |
| ON | $120.71 | 67,234,372 | Unknown | large | unknown | 2026-05-31 |
| ORCL | $225.84 | 120,785,415 | Unknown | large | unknown | 2026-05-31 |
| ORLY | $86.88 | 22,630,681 | Unknown | large | unknown | 2026-05-31 |
| OXY | $56.66 | 39,409,347 | Unknown | large | unknown | 2026-05-31 |
| PANW | $281.96 | 79,981,651 | Unknown | large | unknown | 2026-05-31 |
| PEP | $144.17 | 33,208,642 | Unknown | large | unknown | 2026-05-31 |
| PFE | $26.17 | 42,329,121 | Unknown | large | unknown | 2026-05-31 |
| PG | $143.56 | 50,179,180 | Unknown | large | unknown | 2026-05-31 |
| PGR | $190.37 | 29,071,196 | Unknown | large | unknown | 2026-05-31 |
| PH | $844.74 | 49,803,298 | Unknown | large | unknown | 2026-05-31 |
| PINS | $20.06 | 27,563,057 | Unknown | mid | unknown | 2026-05-31 |
| PLNT | $53.53 | 20,006,617 | Unknown | mid | unknown | 2026-05-31 |
| PLTR | $156.58 | 166,275,089 | Unknown | large | unknown | 2026-05-31 |
| PM | $177.41 | 36,611,781 | Unknown | large | unknown | 2026-05-31 |
| PODD | $145.03 | 20,270,585 | Unknown | large | unknown | 2026-05-31 |
| PRIM | $125.81 | 23,705,385 | Unknown | small | unknown | 2026-05-31 |
| PWR | $712.28 | 64,071,823 | Unknown | large | unknown | 2026-05-31 |
| PYPL | $44.75 | 31,417,056 | Unknown | large | unknown | 2026-05-31 |
| QCOM | $251.17 | 175,985,816 | Unknown | large | unknown | 2026-05-31 |
| RCL | $284.74 | 39,815,563 | Unknown | large | unknown | 2026-05-31 |
| REGN | $612.54 | 51,003,654 | Unknown | large | unknown | 2026-05-31 |
| RL | $363.99 | 22,200,759 | Unknown | large | unknown | 2026-05-31 |
| ROK | $451.14 | 24,741,895 | Unknown | large | unknown | 2026-05-31 |
| ROST | $231.69 | 35,669,280 | Unknown | large | unknown | 2026-05-31 |
| RRX | $201.83 | 22,574,511 | Unknown | mid | unknown | 2026-05-31 |
| RSG | $200.46 | 27,303,766 | Unknown | large | unknown | 2026-05-31 |
| RTX | $179.63 | 36,776,582 | Unknown | large | unknown | 2026-05-31 |
| SATS | $129.25 | 33,893,767 | Unknown | large | unknown | 2026-05-31 |
| SBUX | $99.15 | 32,150,487 | Unknown | large | unknown | 2026-05-31 |
| SCHW | $87.36 | 59,808,279 | Unknown | large | unknown | 2026-05-31 |
| SHW | $303.78 | 32,347,338 | Unknown | large | unknown | 2026-05-31 |
| SITM | $710.99 | 29,034,178 | Unknown | mid | unknown | 2026-05-31 |
| SLB | $54.55 | 39,446,547 | Unknown | large | unknown | 2026-05-31 |
| SMCI | $46.11 | 61,239,809 | Unknown | large | unknown | 2026-05-31 |
| SMTC | $152.61 | 36,134,704 | Unknown | small | unknown | 2026-05-31 |
| SNDK | $1694.38 | 410,703,445 | Unknown | large | unknown | 2026-05-31 |
| SNPS | $475.50 | 42,581,076 | Unknown | large | unknown | 2026-05-31 |
| SO | $92.03 | 26,451,662 | Unknown | large | unknown | 2026-05-31 |
| SPGI | $424.10 | 46,079,957 | Unknown | large | unknown | 2026-05-31 |
| STRL | $861.94 | 33,734,700 | Unknown | mid | unknown | 2026-05-31 |
| STX | $880.12 | 144,458,691 | Unknown | large | unknown | 2026-05-31 |
| SYK | $305.21 | 70,182,735 | Unknown | large | unknown | 2026-05-31 |
| T | $24.79 | 43,911,797 | Unknown | large | unknown | 2026-05-31 |
| TDG | $1258.84 | 37,186,673 | Unknown | large | unknown | 2026-05-31 |
| TEL | $213.38 | 39,409,525 | Unknown | large | unknown | 2026-05-31 |
| TER | $374.54 | 47,589,104 | Unknown | large | unknown | 2026-05-31 |
| TFC | $48.20 | 21,107,193 | Unknown | large | unknown | 2026-05-31 |
| TGT | $127.06 | 31,214,684 | Unknown | large | unknown | 2026-05-31 |
| TJX | $154.77 | 44,411,636 | Unknown | large | unknown | 2026-05-31 |
| TMO | $492.58 | 87,060,626 | Unknown | large | unknown | 2026-05-31 |
| TMUS | $187.43 | 34,621,795 | Unknown | large | unknown | 2026-05-31 |
| TSCO | $31.55 | 27,575,512 | Unknown | large | unknown | 2026-05-31 |
| TSLA | $435.57 | 335,548,781 | Unknown | large | unknown | 2026-05-31 |
| TT | $451.41 | 38,901,641 | Unknown | large | unknown | 2026-05-31 |
| TTD | $21.57 | 22,034,741 | Unknown | large | unknown | 2026-05-31 |
| TTMI | $173.67 | 22,398,729 | Unknown | mid | unknown | 2026-05-31 |
| TTWO | $224.16 | 26,998,834 | Unknown | large | unknown | 2026-05-31 |
| TWLO | $190.73 | 31,703,859 | Unknown | mid | unknown | 2026-05-31 |
| TXN | $305.70 | 94,037,463 | Unknown | large | unknown | 2026-05-31 |
| TXRH | $180.57 | 20,150,129 | Unknown | mid | unknown | 2026-05-31 |
| UAL | $114.78 | 29,136,167 | Unknown | large | unknown | 2026-05-31 |
| UBER | $70.40 | 90,109,118 | Unknown | large | unknown | 2026-05-31 |
| ULTA | $508.90 | 21,932,678 | Unknown | large | unknown | 2026-05-31 |
| UNH | $380.28 | 86,146,741 | Unknown | large | unknown | 2026-05-31 |
| UNP | $262.76 | 44,050,452 | Unknown | large | unknown | 2026-05-31 |
| UPS | $106.81 | 25,854,230 | Unknown | large | unknown | 2026-05-31 |
| URI | $996.39 | 30,849,356 | Unknown | large | unknown | 2026-05-31 |
| USB | $54.85 | 32,285,044 | Unknown | large | unknown | 2026-05-31 |
| V | $326.46 | 122,483,795 | Unknown | large | unknown | 2026-05-31 |
| VEEV | $174.32 | 35,195,205 | Unknown | large | unknown | 2026-05-31 |
| VLO | $245.00 | 33,381,062 | Unknown | large | unknown | 2026-05-31 |
| VMC | $282.87 | 20,105,358 | Unknown | large | unknown | 2026-05-31 |
| VRT | $315.98 | 88,824,983 | Unknown | large | unknown | 2026-05-31 |
| VRTX | $447.44 | 22,845,504 | Unknown | large | unknown | 2026-05-31 |
| VST | $160.23 | 35,091,165 | Unknown | large | unknown | 2026-05-31 |
| VZ | $47.84 | 50,412,887 | Unknown | large | unknown | 2026-05-31 |
| WAT | $384.00 | 35,364,153 | Unknown | large | unknown | 2026-05-31 |
| WBD | $27.00 | 29,788,216 | Unknown | large | unknown | 2026-05-31 |
| WDAY | $146.19 | 32,163,771 | Unknown | large | unknown | 2026-05-31 |
| WDC | $531.09 | 127,860,850 | Unknown | large | unknown | 2026-05-31 |
| WELL | $205.71 | 32,309,599 | Unknown | large | unknown | 2026-05-31 |
| WFC | $77.53 | 79,518,279 | Unknown | large | unknown | 2026-05-31 |
| WMB | $71.40 | 32,208,618 | Unknown | large | unknown | 2026-05-31 |
| WMT | $115.71 | 94,866,622 | Unknown | large | unknown | 2026-05-31 |
| XEL | $79.49 | 31,802,063 | Unknown | large | unknown | 2026-05-31 |
| XOM | $145.34 | 105,127,995 | Unknown | large | unknown | 2026-05-31 |
| XPO | $214.20 | 23,968,737 | Unknown | mid | unknown | 2026-05-31 |
| ZTS | $77.64 | 42,526,543 | Unknown | large | unknown | 2026-05-31 |
