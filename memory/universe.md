---
screened_on: 2026-07-26
expires_on: 2026-08-02
total_passed: 287
total_rejected: 1214
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
| AAL | $14.47 | $53,336,041 | Industrials | mid | unknown | 2026-07-26 |
| AAPL | $333.05 | $621,410,431 | Information Technology | large | unknown | 2026-07-26 |
| ABBV | $259.26 | $74,007,494 | Health Care | large | unknown | 2026-07-26 |
| ABNB | $141.06 | $22,363,149 | Consumer Discretionary | large | unknown | 2026-07-26 |
| ABT | $103.11 | $67,547,812 | Health Care | large | unknown | 2026-07-26 |
| ACN | $147.05 | $62,841,019 | Information Technology | large | unknown | 2026-07-26 |
| ADBE | $225.11 | $53,375,020 | Information Technology | large | unknown | 2026-07-26 |
| ADI | $371.99 | $63,710,346 | Information Technology | large | unknown | 2026-07-26 |
| ADP | $250.09 | $21,660,768 | Industrials | large | unknown | 2026-07-26 |
| ADSK | $209.81 | $21,565,961 | Information Technology | large | unknown | 2026-07-26 |
| AEP | $135.54 | $24,740,185 | Utilities | large | unknown | 2026-07-26 |
| AJG | $247.58 | $22,996,680 | Financials | large | unknown | 2026-07-26 |
| AKAM | $115.31 | $23,612,657 | Information Technology | large | unknown | 2026-07-26 |
| AMAT | $536.80 | $271,279,924 | Information Technology | large | unknown | 2026-07-26 |
| AMD | $522.03 | $347,689,660 | Information Technology | large | unknown | 2026-07-26 |
| AMGN | $376.03 | $28,285,489 | Health Care | large | unknown | 2026-07-26 |
| AMT | $166.69 | $27,692,270 | Real Estate | large | unknown | 2026-07-26 |
| AMZN | $232.10 | $513,535,476 | Consumer Discretionary | large | unknown | 2026-07-26 |
| ANET | $174.13 | $70,006,047 | Information Technology | large | unknown | 2026-07-26 |
| AON | $361.54 | $23,187,143 | Financials | large | unknown | 2026-07-26 |
| APD | $297.94 | $22,067,420 | Materials | large | unknown | 2026-07-26 |
| APH | $152.68 | $56,483,528 | Information Technology | large | unknown | 2026-07-26 |
| APO | $122.63 | $30,523,648 | Financials | large | unknown | 2026-07-26 |
| APP | $391.76 | $84,894,637 | Information Technology | large | unknown | 2026-07-26 |
| AVGO | $381.84 | $250,606,124 | Information Technology | large | unknown | 2026-07-26 |
| AXON | $502.52 | $27,158,862 | Industrials | large | unknown | 2026-07-26 |
| AXP | $326.19 | $51,275,683 | Financials | large | unknown | 2026-07-26 |
| AZO | $2957.08 | $41,664,952 | Consumer Discretionary | large | unknown | 2026-07-26 |
| BA | $209.49 | $43,984,585 | Industrials | large | unknown | 2026-07-26 |
| BAC | $62.05 | $148,138,792 | Financials | large | unknown | 2026-07-26 |
| BKNG | $177.40 | $49,692,681 | Consumer Discretionary | large | unknown | 2026-07-26 |
| BKR | $57.25 | $38,987,135 | Energy | large | unknown | 2026-07-26 |
| BLK | $1055.56 | $63,680,765 | Financials | large | unknown | 2026-07-26 |
| BMY | $62.09 | $41,316,013 | Health Care | large | unknown | 2026-07-26 |
| BNY | $158.91 | $26,799,747 | Financials | large | unknown | 2026-07-26 |
| BRK.B | $494.98 | $59,718,760 | Financials | large | unknown | 2026-07-26 |
| BSX | $44.27 | $58,551,257 | Health Care | large | unknown | 2026-07-26 |
| BX | $129.95 | $25,148,903 | Financials | large | unknown | 2026-07-26 |
| C | $132.22 | $76,242,363 | Financials | large | unknown | 2026-07-26 |
| CAH | $228.06 | $26,225,640 | Health Care | large | unknown | 2026-07-26 |
| CARR | $68.89 | $21,114,063 | Industrials | large | unknown | 2026-07-26 |
| CAT | $889.04 | $135,668,377 | Industrials | large | unknown | 2026-07-26 |
| CB | $359.72 | $36,642,843 | Financials | large | unknown | 2026-07-26 |
| CBOE | $285.61 | $20,606,740 | Financials | large | unknown | 2026-07-26 |
| CCL | $26.34 | $30,107,199 | Consumer Discretionary | large | unknown | 2026-07-26 |
| CDNS | $326.28 | $44,841,341 | Information Technology | large | unknown | 2026-07-26 |
| CEG | $274.39 | $45,780,538 | Utilities | large | unknown | 2026-07-26 |
| CFG | $71.89 | $27,556,251 | Financials | large | unknown | 2026-07-26 |
| CHRW | $186.45 | $20,599,819 | Industrials | large | unknown | 2026-07-26 |
| CHTR | $123.33 | $22,817,524 | Communication Services | large | unknown | 2026-07-26 |
| CI | $289.60 | $23,598,952 | Health Care | large | unknown | 2026-07-26 |
| CMCSA | $22.29 | $54,911,080 | Communication Services | large | unknown | 2026-07-26 |
| CME | $255.28 | $49,744,513 | Financials | large | unknown | 2026-07-26 |
| CMG | $31.81 | $48,252,394 | Consumer Discretionary | large | unknown | 2026-07-26 |
| CMI | $664.60 | $33,039,662 | Industrials | large | unknown | 2026-07-26 |
| CNP | $44.56 | $21,026,917 | Utilities | large | unknown | 2026-07-26 |
| COF | $202.84 | $43,551,687 | Financials | large | unknown | 2026-07-26 |
| COIN | $158.36 | $33,408,953 | Financials | large | unknown | 2026-07-26 |
| COP | $120.29 | $43,658,032 | Energy | large | unknown | 2026-07-26 |
| COR | $309.71 | $24,428,474 | Health Care | large | unknown | 2026-07-26 |
| COST | $935.35 | $74,655,895 | Consumer Staples | large | unknown | 2026-07-26 |
| CPRT | $27.94 | $24,812,502 | Industrials | large | unknown | 2026-07-26 |
| CRM | $163.62 | $74,273,688 | Information Technology | large | unknown | 2026-07-26 |
| CRS | $603.51 | $28,653,645 | Industrials | mid | unknown | 2026-07-26 |
| CRWD | $183.29 | $63,703,277 | Information Technology | large | unknown | 2026-07-26 |
| CSCO | $114.17 | $108,640,850 | Information Technology | large | unknown | 2026-07-26 |
| CSX | $53.21 | $49,046,242 | Industrials | large | unknown | 2026-07-26 |
| CTAS | $205.95 | $22,028,207 | Industrials | large | unknown | 2026-07-26 |
| CTSH | $45.45 | $30,949,468 | Information Technology | large | unknown | 2026-07-26 |
| CVNA | $60.47 | $31,480,968 | Consumer Discretionary | large | unknown | 2026-07-26 |
| CVS | $107.73 | $36,800,082 | Health Care | large | unknown | 2026-07-26 |
| CVX | $194.72 | $56,132,073 | Energy | large | unknown | 2026-07-26 |
| D | $71.09 | $33,366,666 | Utilities | large | unknown | 2026-07-26 |
| DAL | $85.05 | $32,647,010 | Industrials | large | unknown | 2026-07-26 |
| DASH | $172.92 | $41,521,035 | Consumer Discretionary | large | unknown | 2026-07-26 |
| DDOG | $246.71 | $59,958,273 | Information Technology | large | unknown | 2026-07-26 |
| DE | $628.25 | $35,314,415 | Industrials | large | unknown | 2026-07-26 |
| DELL | $437.20 | $104,145,582 | Information Technology | large | unknown | 2026-07-26 |
| DHR | $191.49 | $72,362,392 | Health Care | large | unknown | 2026-07-26 |
| DIS | $94.85 | $50,830,805 | Communication Services | large | unknown | 2026-07-26 |
| DLR | $198.98 | $39,813,841 | Real Estate | large | unknown | 2026-07-26 |
| DOCN | $123.46 | $23,524,189 | Information Technology | mid | unknown | 2026-07-26 |
| DOW | $29.85 | $23,162,457 | Materials | large | unknown | 2026-07-26 |
| DRI | $196.31 | $20,064,596 | Consumer Discretionary | large | unknown | 2026-07-26 |
| DVN | $45.05 | $35,604,109 | Energy | large | unknown | 2026-07-26 |
| EA | $209.08 | $23,959,849 | Communication Services | large | unknown | 2026-07-26 |
| ECHO | $87.89 | $28,347,628 | Communication Services | large | unknown | 2026-07-26 |
| EFX | $172.40 | $22,427,669 | Industrials | large | unknown | 2026-07-26 |
| ELV | $377.46 | $34,414,585 | Health Care | large | unknown | 2026-07-26 |
| EMR | $147.95 | $21,824,963 | Industrials | large | unknown | 2026-07-26 |
| ENTG | $129.28 | $26,383,607 | Information Technology | mid | unknown | 2026-07-26 |
| EQIX | $1083.75 | $45,221,621 | Real Estate | large | unknown | 2026-07-26 |
| EQT | $53.03 | $32,879,142 | Energy | large | unknown | 2026-07-26 |
| ETN | $404.01 | $48,307,888 | Industrials | large | unknown | 2026-07-26 |
| EW | $82.65 | $28,348,483 | Health Care | large | unknown | 2026-07-26 |
| EXC | $47.52 | $26,652,154 | Utilities | large | unknown | 2026-07-26 |
| F | $14.36 | $26,272,012 | Consumer Discretionary | large | unknown | 2026-07-26 |
| FANG | $204.68 | $21,404,564 | Energy | large | unknown | 2026-07-26 |
| FAST | $47.02 | $28,592,999 | Industrials | large | unknown | 2026-07-26 |
| FCX | $62.60 | $59,849,219 | Materials | large | unknown | 2026-07-26 |
| FDX | $314.95 | $38,465,677 | Industrials | large | unknown | 2026-07-26 |
| FICO | $1237.42 | $21,015,083 | Information Technology | large | unknown | 2026-07-26 |
| FITB | $57.41 | $31,083,749 | Financials | large | unknown | 2026-07-26 |
| FIX | $1732.36 | $53,751,046 | Industrials | large | unknown | 2026-07-26 |
| FLEX | $118.48 | $31,550,391 | Information Technology | large | unknown | 2026-07-26 |
| FN | $476.16 | $33,135,429 | Information Technology | mid | unknown | 2026-07-26 |
| FSLR | $202.84 | $21,282,360 | Information Technology | large | unknown | 2026-07-26 |
| FTNT | $152.38 | $32,564,835 | Information Technology | large | unknown | 2026-07-26 |
| GE | $353.74 | $73,054,940 | Industrials | large | unknown | 2026-07-26 |
| GEV | $1014.60 | $155,560,155 | Industrials | large | unknown | 2026-07-26 |
| GILD | $129.35 | $39,738,503 | Health Care | large | unknown | 2026-07-26 |
| GIS | $36.04 | $29,019,065 | Consumer Staples | large | unknown | 2026-07-26 |
| GLW | $146.62 | $120,838,789 | Information Technology | large | unknown | 2026-07-26 |
| GM | $82.62 | $23,277,471 | Consumer Discretionary | large | unknown | 2026-07-26 |
| GOOG | $319.15 | $232,810,016 | Communication Services | large | unknown | 2026-07-26 |
| GOOGL | $319.73 | $369,575,113 | Communication Services | large | unknown | 2026-07-26 |
| GS | $1061.25 | $75,179,214 | Financials | large | unknown | 2026-07-26 |
| GWW | $1380.85 | $25,885,482 | Industrials | large | unknown | 2026-07-26 |
| HAL | $33.35 | $31,507,743 | Energy | large | unknown | 2026-07-26 |
| HBAN | $17.36 | $22,632,918 | Financials | large | unknown | 2026-07-26 |
| HCA | $382.21 | $35,544,199 | Health Care | large | unknown | 2026-07-26 |
| HD | $332.98 | $59,706,647 | Consumer Discretionary | large | unknown | 2026-07-26 |
| HLT | $324.98 | $42,023,226 | Consumer Discretionary | large | unknown | 2026-07-26 |
| HON | $243.09 | $48,279,608 | Industrials | large | unknown | 2026-07-26 |
| HONA | $203.88 | $44,271,206 | Industrials | large | unknown | 2026-07-26 |
| HOOD | $94.91 | $91,677,503 | Financials | large | unknown | 2026-07-26 |
| HPE | $47.74 | $58,665,215 | Information Technology | large | unknown | 2026-07-26 |
| HPQ | $25.76 | $24,417,050 | Information Technology | large | unknown | 2026-07-26 |
| HUM | $388.90 | $28,000,783 | Health Care | large | unknown | 2026-07-26 |
| HWM | $289.40 | $36,339,661 | Industrials | large | unknown | 2026-07-26 |
| IBM | $214.07 | $119,486,315 | Information Technology | large | unknown | 2026-07-26 |
| ICE | $145.82 | $30,011,317 | Financials | large | unknown | 2026-07-26 |
| IDXX | $544.17 | $24,714,849 | Health Care | large | unknown | 2026-07-26 |
| ILMN | $194.06 | $20,719,743 | Health Care | mid | unknown | 2026-07-26 |
| INTC | $92.37 | $354,346,526 | Information Technology | large | unknown | 2026-07-26 |
| INTU | $296.29 | $78,882,742 | Information Technology | large | unknown | 2026-07-26 |
| ISRG | $337.41 | $67,365,089 | Health Care | large | unknown | 2026-07-26 |
| JBL | $312.45 | $21,762,178 | Information Technology | large | unknown | 2026-07-26 |
| JCI | $143.41 | $26,253,709 | Industrials | large | unknown | 2026-07-26 |
| JNJ | $263.42 | $101,629,560 | Health Care | large | unknown | 2026-07-26 |
| JPM | $353.14 | $90,926,872 | Financials | large | unknown | 2026-07-26 |
| KDP | $29.70 | $27,832,273 | Consumer Staples | large | unknown | 2026-07-26 |
| KEYS | $318.68 | $32,082,099 | Information Technology | large | unknown | 2026-07-26 |
| KKR | $99.37 | $21,146,814 | Financials | large | unknown | 2026-07-26 |
| KLAC | $210.43 | $142,993,327 | Information Technology | large | unknown | 2026-07-26 |
| KMI | $32.85 | $20,299,835 | Energy | large | unknown | 2026-07-26 |
| KO | $82.24 | $97,212,797 | Consumer Staples | large | unknown | 2026-07-26 |
| KR | $56.87 | $28,318,214 | Consumer Staples | large | unknown | 2026-07-26 |
| KVUE | $19.26 | $25,248,105 | Consumer Staples | large | unknown | 2026-07-26 |
| LHX | $300.24 | $21,306,691 | Industrials | large | unknown | 2026-07-26 |
| LIN | $512.42 | $48,354,294 | Materials | large | unknown | 2026-07-26 |
| LLY | $1196.14 | $147,047,042 | Health Care | large | unknown | 2026-07-26 |
| LMT | $582.67 | $28,321,920 | Industrials | large | unknown | 2026-07-26 |
| LOW | $207.64 | $25,839,812 | Consumer Discretionary | large | unknown | 2026-07-26 |
| LRCX | $305.42 | $174,651,766 | Information Technology | large | unknown | 2026-07-26 |
| LYV | $177.23 | $20,742,802 | Communication Services | large | unknown | 2026-07-26 |
| MA | $539.74 | $91,034,135 | Financials | large | unknown | 2026-07-26 |
| MAR | $374.43 | $27,970,598 | Consumer Discretionary | large | unknown | 2026-07-26 |
| MCD | $264.71 | $53,215,001 | Consumer Discretionary | large | unknown | 2026-07-26 |
| MCHP | $78.89 | $32,262,161 | Information Technology | large | unknown | 2026-07-26 |
| MCK | $841.14 | $38,436,976 | Health Care | large | unknown | 2026-07-26 |
| MCO | $471.51 | $31,702,950 | Financials | large | unknown | 2026-07-26 |
| MDLZ | $60.52 | $38,343,379 | Consumer Staples | large | unknown | 2026-07-26 |
| MDT | $83.19 | $43,773,157 | Health Care | large | unknown | 2026-07-26 |
| META | $595.18 | $486,563,992 | Communication Services | large | unknown | 2026-07-26 |
| MKSI | $328.88 | $34,299,267 | Information Technology | mid | unknown | 2026-07-26 |
| MLM | $559.62 | $26,747,939 | Materials | large | unknown | 2026-07-26 |
| MMM | $172.62 | $27,151,889 | Industrials | large | unknown | 2026-07-26 |
| MNST | $93.50 | $26,890,351 | Consumer Staples | large | unknown | 2026-07-26 |
| MO | $72.97 | $27,216,488 | Consumer Staples | large | unknown | 2026-07-26 |
| MPC | $309.18 | $39,980,010 | Energy | large | unknown | 2026-07-26 |
| MPWR | $1334.65 | $61,389,243 | Information Technology | large | unknown | 2026-07-26 |
| MRK | $131.06 | $45,107,615 | Health Care | large | unknown | 2026-07-26 |
| MRSH | $180.65 | $20,143,620 | Financials | large | unknown | 2026-07-26 |
| MRVL | $194.51 | $152,701,134 | Information Technology | large | unknown | 2026-07-26 |
| MS | $214.46 | $67,463,508 | Financials | large | unknown | 2026-07-26 |
| MSCI | $551.00 | $36,114,447 | Financials | large | unknown | 2026-07-26 |
| MSFT | $381.81 | $506,083,303 | Information Technology | large | unknown | 2026-07-26 |
| MTD | $1328.49 | $20,545,338 | Health Care | large | unknown | 2026-07-26 |
| MTSI | $267.04 | $24,536,937 | Information Technology | mid | unknown | 2026-07-26 |
| MTZ | $338.08 | $31,142,630 | Industrials | mid | unknown | 2026-07-26 |
| MU | $921.05 | $1,029,047,794 | Information Technology | large | unknown | 2026-07-26 |
| NDAQ | $92.08 | $21,231,384 | Financials | large | unknown | 2026-07-26 |
| NEE | $89.77 | $64,712,397 | Utilities | large | unknown | 2026-07-26 |
| NEM | $93.17 | $36,000,011 | Materials | large | unknown | 2026-07-26 |
| NFLX | $70.10 | $234,571,648 | Communication Services | large | unknown | 2026-07-26 |
| NKE | $41.61 | $60,908,634 | Consumer Discretionary | large | unknown | 2026-07-26 |
| NOC | $542.54 | $37,436,778 | Industrials | large | unknown | 2026-07-26 |
| NOW | $98.77 | $92,957,097 | Information Technology | large | unknown | 2026-07-26 |
| NTAP | $167.80 | $21,583,577 | Information Technology | large | unknown | 2026-07-26 |
| NVDA | $207.07 | $958,280,543 | Information Technology | large | unknown | 2026-07-26 |
| NXPI | $269.28 | $44,649,596 | Information Technology | large | unknown | 2026-07-26 |
| NXT | $100.09 | $20,271,366 | Industrials | mid | unknown | 2026-07-26 |
| O | $65.61 | $21,184,289 | Real Estate | large | unknown | 2026-07-26 |
| OKTA | $138.56 | $21,557,844 | Information Technology | mid | unknown | 2026-07-26 |
| ON | $86.93 | $50,815,711 | Information Technology | large | unknown | 2026-07-26 |
| ONTO | $271.69 | $29,421,967 | Information Technology | mid | unknown | 2026-07-26 |
| ORCL | $115.00 | $189,035,503 | Information Technology | large | unknown | 2026-07-26 |
| ORLY | $87.43 | $33,489,750 | Consumer Discretionary | large | unknown | 2026-07-26 |
| OXY | $57.29 | $37,826,700 | Energy | large | unknown | 2026-07-26 |
| PANW | $323.79 | $102,608,420 | Information Technology | large | unknown | 2026-07-26 |
| PATH | $10.85 | $22,281,926 | Information Technology | mid | unknown | 2026-07-26 |
| PEP | $136.66 | $47,582,941 | Consumer Staples | large | unknown | 2026-07-26 |
| PFE | $24.55 | $49,144,916 | Health Care | large | unknown | 2026-07-26 |
| PG | $147.38 | $47,535,479 | Consumer Staples | large | unknown | 2026-07-26 |
| PGR | $213.92 | $37,508,134 | Financials | large | unknown | 2026-07-26 |
| PH | $985.59 | $34,461,815 | Industrials | large | unknown | 2026-07-26 |
| PLD | $147.59 | $29,950,287 | Real Estate | large | unknown | 2026-07-26 |
| PLTR | $122.93 | $148,256,721 | Information Technology | large | unknown | 2026-07-26 |
| PM | $192.99 | $46,743,335 | Consumer Staples | large | unknown | 2026-07-26 |
| PNC | $250.94 | $25,881,343 | Financials | large | unknown | 2026-07-26 |
| PSX | $206.78 | $26,030,526 | Energy | large | unknown | 2026-07-26 |
| PWR | $625.69 | $45,749,107 | Industrials | large | unknown | 2026-07-26 |
| PYPL | $56.15 | $48,131,988 | Financials | large | unknown | 2026-07-26 |
| QCOM | $167.06 | $93,234,476 | Information Technology | large | unknown | 2026-07-26 |
| RCL | $293.50 | $40,976,403 | Consumer Discretionary | large | unknown | 2026-07-26 |
| REGN | $655.90 | $40,701,848 | Health Care | large | unknown | 2026-07-26 |
| RF | $30.84 | $22,986,131 | Financials | large | unknown | 2026-07-26 |
| ROK | $462.33 | $24,575,692 | Industrials | large | unknown | 2026-07-26 |
| ROST | $238.98 | $27,733,513 | Consumer Discretionary | large | unknown | 2026-07-26 |
| RRX | $212.78 | $20,434,408 | Industrials | mid | unknown | 2026-07-26 |
| RTX | $212.85 | $38,575,768 | Industrials | large | unknown | 2026-07-26 |
| SBUX | $103.22 | $31,760,001 | Consumer Discretionary | large | unknown | 2026-07-26 |
| SCHW | $101.98 | $56,767,130 | Financials | large | unknown | 2026-07-26 |
| SHW | $317.57 | $35,531,224 | Materials | large | unknown | 2026-07-26 |
| SLB | $52.45 | $40,621,123 | Energy | large | unknown | 2026-07-26 |
| SMCI | $30.11 | $55,938,658 | Information Technology | large | unknown | 2026-07-26 |
| SMTC | $125.84 | $24,671,092 | Information Technology | mid | unknown | 2026-07-26 |
| SNDK | $1436.64 | $559,870,515 | Information Technology | large | unknown | 2026-07-26 |
| SNPS | $373.40 | $39,273,920 | Information Technology | large | unknown | 2026-07-26 |
| SO | $97.28 | $22,716,130 | Utilities | large | unknown | 2026-07-26 |
| SPGI | $426.29 | $54,656,677 | Financials | large | unknown | 2026-07-26 |
| STRL | $660.63 | $30,756,242 | Industrials | mid | unknown | 2026-07-26 |
| STT | $185.45 | $24,101,474 | Financials | large | unknown | 2026-07-26 |
| STX | $851.76 | $190,225,914 | Information Technology | large | unknown | 2026-07-26 |
| STZ | $130.13 | $20,108,586 | Consumer Staples | large | unknown | 2026-07-26 |
| SYK | $330.37 | $51,361,458 | Health Care | large | unknown | 2026-07-26 |
| T | $24.11 | $94,358,271 | Communication Services | large | unknown | 2026-07-26 |
| TDG | $1236.45 | $37,062,642 | Industrials | large | unknown | 2026-07-26 |
| TECH | $71.59 | $20,363,600 | Health Care | large | unknown | 2026-07-26 |
| TEL | $203.00 | $40,991,869 | Information Technology | large | unknown | 2026-07-26 |
| TER | $349.93 | $65,051,698 | Information Technology | large | unknown | 2026-07-26 |
| TFC | $51.78 | $26,735,785 | Financials | large | unknown | 2026-07-26 |
| TGT | $136.77 | $27,283,531 | Consumer Staples | large | unknown | 2026-07-26 |
| TJX | $154.18 | $36,722,385 | Consumer Discretionary | large | unknown | 2026-07-26 |
| TMO | $568.15 | $79,265,535 | Health Care | large | unknown | 2026-07-26 |
| TMUS | $180.06 | $45,872,847 | Communication Services | large | unknown | 2026-07-26 |
| TOST | $29.06 | $23,204,578 | Financials | mid | unknown | 2026-07-26 |
| TPR | $142.63 | $20,725,233 | Consumer Discretionary | large | unknown | 2026-07-26 |
| TRGP | $281.42 | $21,971,140 | Energy | large | unknown | 2026-07-26 |
| TRV | $387.27 | $30,740,403 | Financials | large | unknown | 2026-07-26 |
| TSCO | $31.04 | $27,046,636 | Consumer Discretionary | large | unknown | 2026-07-26 |
| TSLA | $312.93 | $399,604,270 | Consumer Discretionary | large | unknown | 2026-07-26 |
| TT | $481.25 | $34,687,692 | Industrials | large | unknown | 2026-07-26 |
| TTMI | $131.43 | $26,647,360 | Information Technology | mid | unknown | 2026-07-26 |
| TTWO | $231.69 | $22,859,298 | Communication Services | large | unknown | 2026-07-26 |
| TWLO | $191.46 | $21,822,418 | Information Technology | mid | unknown | 2026-07-26 |
| TXN | $279.64 | $106,543,918 | Information Technology | large | unknown | 2026-07-26 |
| UAL | $118.25 | $29,685,932 | Industrials | large | unknown | 2026-07-26 |
| UBER | $65.94 | $83,305,387 | Industrials | large | unknown | 2026-07-26 |
| UNH | $420.67 | $102,620,015 | Health Care | large | unknown | 2026-07-26 |
| UNP | $307.57 | $49,683,203 | Industrials | large | unknown | 2026-07-26 |
| URI | $1141.80 | $32,721,514 | Industrials | large | unknown | 2026-07-26 |
| USB | $63.98 | $42,948,644 | Financials | large | unknown | 2026-07-26 |
| V | $355.62 | $121,028,703 | Financials | large | unknown | 2026-07-26 |
| VLO | $302.46 | $41,732,926 | Energy | large | unknown | 2026-07-26 |
| VMC | $279.73 | $23,840,964 | Materials | large | unknown | 2026-07-26 |
| VRSK | $201.36 | $24,375,181 | Industrials | large | unknown | 2026-07-26 |
| VRTX | $477.42 | $39,840,238 | Health Care | large | unknown | 2026-07-26 |
| VST | $163.37 | $30,675,980 | Utilities | large | unknown | 2026-07-26 |
| VZ | $46.42 | $99,495,128 | Communication Services | large | unknown | 2026-07-26 |
| WAT | $374.65 | $25,231,636 | Health Care | large | unknown | 2026-07-26 |
| WBD | $25.78 | $47,154,556 | Communication Services | large | unknown | 2026-07-26 |
| WBS | $76.09 | $20,245,908 | Financials | mid | unknown | 2026-07-26 |
| WCC | $332.59 | $20,689,889 | Industrials | mid | unknown | 2026-07-26 |
| WDAY | $135.30 | $24,302,049 | Information Technology | large | unknown | 2026-07-26 |
| WDC | $519.51 | $185,603,021 | Information Technology | large | unknown | 2026-07-26 |
| WELL | $252.60 | $34,582,242 | Real Estate | large | unknown | 2026-07-26 |
| WFC | $86.39 | $85,107,414 | Financials | large | unknown | 2026-07-26 |
| WM | $238.78 | $23,640,638 | Industrials | large | unknown | 2026-07-26 |
| WMB | $74.00 | $29,856,797 | Energy | large | unknown | 2026-07-26 |
| WMT | $109.46 | $109,335,458 | Consumer Staples | large | unknown | 2026-07-26 |
| WWD | $418.72 | $20,911,918 | Industrials | mid | unknown | 2026-07-26 |
| XEL | $81.68 | $23,580,576 | Utilities | large | unknown | 2026-07-26 |
| XOM | $156.93 | $75,261,377 | Energy | large | unknown | 2026-07-26 |
| XYZ | $77.16 | $20,247,038 | Financials | large | unknown | 2026-07-26 |
| YUM | $148.87 | $22,367,321 | Consumer Discretionary | large | unknown | 2026-07-26 |
