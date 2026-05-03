---
screened_on: 2026-05-03
expires_on: 2026-05-10
total_passed: 502
total_rejected: 1
source: https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv
---

# Universe

Pre-computed list of tickers that pass `memory/strategy.md` universe filters:

- S&P 500 constituent
- Price ≥ $10/share
- 20-day average dollar volume ≥ $20M
- US primary listing
- Not a recent IPO (< 180 days since listing)

**Written only by `routines/universe_refresh.md`** (Sundays 18:00 ET). Consumed read-only by `pre_market`, `market_open`, and `midday`. The cache is valid for 7 days — if `expires_on` is in the past, trading routines abort with a Discord notice and wait for the next weekend refresh.

## Columns

- `ticker` — symbol
- `last_price` — most recent daily close used in screening (USD)
- `avg_dollar_volume_20d` — mean of `close × volume` across the last 20 trading days (USD)
- `sector` — GICS sector from the S&P 500 list source
- `earnings_date_next` — next scheduled earnings report (ISO date; `unknown` if lookup failed). `pre_market` re-verifies this for every candidate before including it in `plan.md`.
- `screened_on` — date the row was produced

| ticker | last_price | avg_dollar_volume_20d | sector | earnings_date_next | screened_on |
|--------|------------|-----------------------|--------|---------------------|-------------|
| A | $114.52 | $215,748,025 | Health Care | unknown | 2026-05-03 |
| AAPL | $280.14 | $12,274,098,818 | Information Technology | 2026-07-30 | 2026-05-03 |
| ABBV | $206.60 | $1,430,377,978 | Health Care | unknown | 2026-05-03 |
| ABNB | $141.66 | $441,196,390 | Consumer Discretionary | unknown | 2026-05-03 |
| ABT | $89.46 | $1,252,933,723 | Health Care | unknown | 2026-05-03 |
| ACGL | $93.82 | $202,274,882 | Financials | unknown | 2026-05-03 |
| ACN | $179.83 | $948,482,446 | Information Technology | unknown | 2026-05-03 |
| ADBE | $250.71 | $1,312,692,722 | Information Technology | unknown | 2026-05-03 |
| ADI | $397.69 | $1,182,925,868 | Information Technology | unknown | 2026-05-03 |
| ADM | $74.94 | $230,266,131 | Consumer Staples | unknown | 2026-05-03 |
| ADP | $214.21 | $606,973,109 | Industrials | unknown | 2026-05-03 |
| ADSK | $244.35 | $445,657,135 | Information Technology | unknown | 2026-05-03 |
| AEE | $113.56 | $180,520,691 | Utilities | unknown | 2026-05-03 |
| AEP | $136.91 | $330,024,205 | Utilities | unknown | 2026-05-03 |
| AES | $14.28 | $141,288,333 | Utilities | unknown | 2026-05-03 |
| AFL | $112.88 | $246,698,632 | Financials | unknown | 2026-05-03 |
| AIG | $78.77 | $351,817,274 | Financials | unknown | 2026-05-03 |
| AIZ | $231.51 | $82,275,880 | Financials | unknown | 2026-05-03 |
| AJG | $208.11 | $388,404,564 | Financials | unknown | 2026-05-03 |
| AKAM | $103.87 | $476,527,284 | Information Technology | unknown | 2026-05-03 |
| ALB | $193.88 | $393,576,308 | Materials | unknown | 2026-05-03 |
| ALGN | $178.91 | $194,935,473 | Health Care | unknown | 2026-05-03 |
| ALL | $216.59 | $274,586,592 | Financials | unknown | 2026-05-03 |
| ALLE | $135.49 | $150,210,037 | Industrials | unknown | 2026-05-03 |
| AMAT | $389.08 | $2,187,355,672 | Information Technology | unknown | 2026-05-03 |
| AMCR | $37.75 | $155,922,448 | Materials | unknown | 2026-05-03 |
| AMD | $360.54 | $11,698,261,025 | Information Technology | unknown | 2026-05-03 |
| AME | $230.48 | $278,575,486 | Industrials | unknown | 2026-05-03 |
| AMGN | $329.82 | $884,454,966 | Health Care | unknown | 2026-05-03 |
| AMP | $467.19 | $321,376,815 | Financials | unknown | 2026-05-03 |
| AMT | $181.61 | $535,561,721 | Real Estate | unknown | 2026-05-03 |
| AMZN | $268.26 | $12,521,429,792 | Consumer Discretionary | unknown | 2026-05-03 |
| ANET | $172.70 | $1,158,996,619 | Information Technology | unknown | 2026-05-03 |
| AON | $311.51 | $434,399,685 | Financials | unknown | 2026-05-03 |
| AOS | $60.35 | $108,101,940 | Industrials | unknown | 2026-05-03 |
| APA | $40.13 | $272,704,027 | Energy | unknown | 2026-05-03 |
| APD | $301.07 | $313,594,006 | Materials | unknown | 2026-05-03 |
| APH | $142.30 | $1,083,329,007 | Information Technology | unknown | 2026-05-03 |
| APO | $130.46 | $520,805,767 | Financials | unknown | 2026-05-03 |
| APP | $460.00 | $1,732,663,663 | Information Technology | unknown | 2026-05-03 |
| APTV | $60.49 | $151,804,738 | Consumer Discretionary | unknown | 2026-05-03 |
| ARE | $41.39 | $109,127,254 | Real Estate | unknown | 2026-05-03 |
| ARES | $119.00 | $384,575,356 | Financials | unknown | 2026-05-03 |
| ATO | $188.54 | $144,268,748 | Utilities | unknown | 2026-05-03 |
| AVB | $183.45 | $161,399,351 | Real Estate | unknown | 2026-05-03 |
| AVGO | $421.28 | $8,492,254,893 | Information Technology | unknown | 2026-05-03 |
| AVY | $163.03 | $105,738,631 | Materials | unknown | 2026-05-03 |
| AWK | $127.38 | $258,000,289 | Utilities | unknown | 2026-05-03 |
| AXON | $402.31 | $442,636,928 | Industrials | unknown | 2026-05-03 |
| AXP | $319.68 | $1,000,423,849 | Financials | unknown | 2026-05-03 |
| AZO | $3594.08 | $777,163,223 | Consumer Discretionary | unknown | 2026-05-03 |
| BA | $227.38 | $1,331,543,620 | Industrials | unknown | 2026-05-03 |
| BAC | $53.24 | $1,728,944,212 | Financials | unknown | 2026-05-03 |
| BALL | $61.33 | $145,210,560 | Materials | unknown | 2026-05-03 |
| BAX | $17.21 | $138,143,128 | Health Care | unknown | 2026-05-03 |
| BBY | $60.05 | $203,116,252 | Consumer Discretionary | unknown | 2026-05-03 |
| BDX | $149.31 | $433,997,968 | Health Care | unknown | 2026-05-03 |
| BEN | $29.84 | $155,714,941 | Financials | unknown | 2026-05-03 |
| BG | $124.61 | $182,067,655 | Consumer Staples | unknown | 2026-05-03 |
| BIIB | $187.06 | $240,778,627 | Health Care | unknown | 2026-05-03 |
| BK | $133.78 | $525,084,580 | Financials | unknown | 2026-05-03 |
| BKNG | $169.63 | $1,284,716,537 | Consumer Discretionary | unknown | 2026-05-03 |
| BKR | $69.12 | $542,467,964 | Energy | unknown | 2026-05-03 |
| BLDR | $75.72 | $199,056,252 | Industrials | unknown | 2026-05-03 |
| BLK | $1061.68 | $728,118,712 | Financials | unknown | 2026-05-03 |
| BMY | $58.22 | $579,880,090 | Health Care | unknown | 2026-05-03 |
| BR | $155.25 | $192,553,187 | Industrials | unknown | 2026-05-03 |
| BRK.B | $473.01 | $2,226,098,282 | Financials | unknown | 2026-05-03 |
| BRO | $57.63 | $180,307,039 | Financials | unknown | 2026-05-03 |
| BSX | $56.50 | $1,107,196,885 | Health Care | unknown | 2026-05-03 |
| BX | $126.35 | $807,953,125 | Financials | unknown | 2026-05-03 |
| BXP | $59.37 | $109,384,112 | Real Estate | unknown | 2026-05-03 |
| C | $127.44 | $1,422,116,278 | Financials | unknown | 2026-05-03 |
| CAG | $14.06 | $204,515,193 | Consumer Staples | unknown | 2026-05-03 |
| CAH | $195.24 | $347,420,112 | Health Care | unknown | 2026-05-03 |
| CARR | $67.62 | $441,722,304 | Industrials | unknown | 2026-05-03 |
| CASY | $835.92 | $622,299,891 | Consumer Staples | unknown | 2026-05-03 |
| CAT | $889.67 | $1,866,519,659 | Industrials | unknown | 2026-05-03 |
| CB | $326.22 | $540,289,905 | Financials | unknown | 2026-05-03 |
| CBOE | $326.96 | $255,307,694 | Financials | unknown | 2026-05-03 |
| CBRE | $141.81 | $278,421,884 | Real Estate | unknown | 2026-05-03 |
| CCI | $89.26 | $254,461,260 | Real Estate | unknown | 2026-05-03 |
| CCL | $26.66 | $663,251,720 | Consumer Discretionary | unknown | 2026-05-03 |
| CDNS | $340.94 | $797,781,310 | Information Technology | unknown | 2026-05-03 |
| CDW | $136.03 | $182,293,936 | Information Technology | unknown | 2026-05-03 |
| CEG | $307.81 | $782,501,487 | Utilities | unknown | 2026-05-03 |
| CF | $122.69 | $436,409,988 | Materials | unknown | 2026-05-03 |
| CFG | $64.42 | $301,273,409 | Financials | unknown | 2026-05-03 |
| CHD | $96.02 | $189,903,110 | Consumer Staples | unknown | 2026-05-03 |
| CHRW | $177.30 | $349,199,241 | Industrials | unknown | 2026-05-03 |
| CHTR | $171.74 | $639,662,906 | Communication Services | unknown | 2026-05-03 |
| CI | $282.90 | $416,894,279 | Health Care | unknown | 2026-05-03 |
| CIEN | $535.29 | $1,198,512,513 | Information Technology | unknown | 2026-05-03 |
| CINF | $162.05 | $123,616,090 | Financials | unknown | 2026-05-03 |
| CL | $87.26 | $459,276,052 | Consumer Staples | unknown | 2026-05-03 |
| CLX | $87.11 | $294,849,088 | Consumer Staples | unknown | 2026-05-03 |
| CMCSA | $27.19 | $839,988,826 | Communication Services | unknown | 2026-05-03 |
| CME | $289.54 | $705,759,964 | Financials | unknown | 2026-05-03 |
| CMG | $32.98 | $548,266,111 | Consumer Discretionary | unknown | 2026-05-03 |
| CMI | $657.44 | $454,726,503 | Industrials | unknown | 2026-05-03 |
| CMS | $76.03 | $229,398,025 | Utilities | unknown | 2026-05-03 |
| CNC | $53.34 | $295,226,239 | Health Care | unknown | 2026-05-03 |
| CNP | $43.35 | $203,629,322 | Utilities | unknown | 2026-05-03 |
| COF | $191.91 | $831,942,125 | Financials | unknown | 2026-05-03 |
| COHR | $329.50 | $1,754,743,410 | Information Technology | unknown | 2026-05-03 |
| COIN | $191.25 | $1,843,043,054 | Financials | unknown | 2026-05-03 |
| COO | $62.36 | $141,571,171 | Health Care | unknown | 2026-05-03 |
| COP | $123.19 | $1,078,861,988 | Energy | unknown | 2026-05-03 |
| COR | $304.00 | $424,177,584 | Health Care | unknown | 2026-05-03 |
| COST | $1011.70 | $1,780,266,907 | Consumer Staples | unknown | 2026-05-03 |
| CPAY | $307.22 | $155,862,598 | Financials | unknown | 2026-05-03 |
| CPB | $20.73 | $166,514,838 | Consumer Staples | unknown | 2026-05-03 |
| CPRT | $33.27 | $261,398,407 | Industrials | unknown | 2026-05-03 |
| CPT | $104.45 | $120,552,502 | Real Estate | unknown | 2026-05-03 |
| CRH | $115.45 | $524,170,029 | Materials | unknown | 2026-05-03 |
| CRL | $165.78 | $136,019,875 | Health Care | unknown | 2026-05-03 |
| CRM | $183.82 | $2,471,937,427 | Information Technology | unknown | 2026-05-03 |
| CRWD | $455.64 | $1,407,683,701 | Information Technology | unknown | 2026-05-03 |
| CSCO | $91.85 | $1,503,167,222 | Information Technology | unknown | 2026-05-03 |
| CSGP | $34.72 | $239,980,356 | Real Estate | unknown | 2026-05-03 |
| CSX | $45.09 | $525,747,230 | Industrials | unknown | 2026-05-03 |
| CTAS | $169.61 | $340,402,421 | Industrials | unknown | 2026-05-03 |
| CTRA | $35.38 | $229,277,633 | Energy | unknown | 2026-05-03 |
| CTSH | $52.43 | $367,645,895 | Information Technology | unknown | 2026-05-03 |
| CTVA | $80.85 | $260,744,620 | Materials | unknown | 2026-05-03 |
| CVNA | $382.60 | $1,063,805,061 | Consumer Discretionary | unknown | 2026-05-03 |
| CVS | $82.09 | $597,532,558 | Health Care | unknown | 2026-05-03 |
| CVX | $190.63 | $2,021,617,652 | Energy | unknown | 2026-05-03 |
| D | $63.94 | $284,607,238 | Utilities | unknown | 2026-05-03 |
| DAL | $68.98 | $689,986,751 | Industrials | unknown | 2026-05-03 |
| DASH | $175.84 | $646,863,771 | Consumer Discretionary | unknown | 2026-05-03 |
| DD | $46.24 | $135,836,942 | Materials | unknown | 2026-05-03 |
| DDOG | $140.53 | $593,267,798 | Information Technology | unknown | 2026-05-03 |
| DE | $577.26 | $636,743,896 | Industrials | unknown | 2026-05-03 |
| DECK | $100.88 | $164,837,387 | Consumer Discretionary | unknown | 2026-05-03 |
| DELL | $210.17 | $1,192,188,594 | Information Technology | unknown | 2026-05-03 |
| DG | $114.43 | $336,167,526 | Consumer Staples | unknown | 2026-05-03 |
| DGX | $192.67 | $213,512,675 | Health Care | unknown | 2026-05-03 |
| DHI | $149.98 | $404,912,013 | Consumer Discretionary | unknown | 2026-05-03 |
| DHR | $175.15 | $883,086,961 | Health Care | unknown | 2026-05-03 |
| DIS | $103.08 | $762,202,982 | Communication Services | 2026-05-06 | 2026-05-03 |
| DLR | $200.70 | $425,332,707 | Real Estate | unknown | 2026-05-03 |
| DLTR | $94.67 | $362,001,970 | Consumer Staples | unknown | 2026-05-03 |
| DOC | $16.42 | $130,910,791 | Real Estate | unknown | 2026-05-03 |
| DOV | $225.79 | $232,577,819 | Industrials | unknown | 2026-05-03 |
| DOW | $40.29 | $558,791,549 | Materials | unknown | 2026-05-03 |
| DPZ | $337.77 | $360,705,283 | Consumer Discretionary | unknown | 2026-05-03 |
| DRI | $194.76 | $235,127,492 | Consumer Discretionary | unknown | 2026-05-03 |
| DTE | $148.79 | $166,972,658 | Utilities | unknown | 2026-05-03 |
| DUK | $128.60 | $370,119,286 | Utilities | unknown | 2026-05-03 |
| DVA | $151.65 | $90,019,215 | Health Care | unknown | 2026-05-03 |
| DVN | $50.56 | $572,456,769 | Energy | unknown | 2026-05-03 |
| DXCM | $61.35 | $291,056,590 | Health Care | unknown | 2026-05-03 |
| EA | $202.09 | $310,009,886 | Communication Services | unknown | 2026-05-03 |
| EBAY | $104.07 | $574,664,642 | Consumer Discretionary | unknown | 2026-05-03 |
| ECL | $259.51 | $358,916,740 | Materials | unknown | 2026-05-03 |
| ED | $110.49 | $187,724,304 | Utilities | unknown | 2026-05-03 |
| EFX | $173.85 | $302,481,087 | Industrials | unknown | 2026-05-03 |
| EG | $353.57 | $115,066,662 | Financials | unknown | 2026-05-03 |
| EIX | $69.88 | $198,923,919 | Utilities | unknown | 2026-05-03 |
| EL | $79.30 | $289,962,774 | Consumer Staples | unknown | 2026-05-03 |
| ELV | $372.68 | $594,379,662 | Health Care | unknown | 2026-05-03 |
| EME | $903.50 | $303,976,729 | Industrials | unknown | 2026-05-03 |
| EMR | $137.45 | $377,787,064 | Industrials | unknown | 2026-05-03 |
| EOG | $138.95 | $540,275,015 | Energy | unknown | 2026-05-03 |
| EPAM | $112.33 | $178,330,084 | Information Technology | unknown | 2026-05-03 |
| EQIX | $1085.03 | $584,406,057 | Real Estate | unknown | 2026-05-03 |
| EQR | $65.17 | $167,330,856 | Real Estate | unknown | 2026-05-03 |
| EQT | $58.66 | $454,895,623 | Energy | unknown | 2026-05-03 |
| ERIE | $214.96 | $55,555,944 | Financials | unknown | 2026-05-03 |
| ES | $71.07 | $130,774,110 | Utilities | unknown | 2026-05-03 |
| ESS | $263.35 | $117,867,021 | Real Estate | unknown | 2026-05-03 |
| ETN | $425.55 | $930,369,742 | Industrials | unknown | 2026-05-03 |
| ETR | $116.43 | $327,456,289 | Utilities | unknown | 2026-05-03 |
| EVRG | $82.61 | $130,150,214 | Utilities | unknown | 2026-05-03 |
| EW | $83.98 | $466,686,602 | Health Care | unknown | 2026-05-03 |
| EXC | $46.50 | $385,902,829 | Utilities | unknown | 2026-05-03 |
| EXE | $100.12 | $334,171,549 | Energy | unknown | 2026-05-03 |
| EXPD | $147.23 | $145,113,528 | Industrials | unknown | 2026-05-03 |
| EXPE | $251.84 | $382,245,918 | Consumer Discretionary | unknown | 2026-05-03 |
| EXR | $142.02 | $180,909,181 | Real Estate | unknown | 2026-05-03 |
| F | $11.88 | $493,401,829 | Consumer Discretionary | unknown | 2026-05-03 |
| FANG | $207.65 | $559,277,420 | Energy | unknown | 2026-05-03 |
| FAST | $44.91 | $337,312,557 | Industrials | unknown | 2026-05-03 |
| FCX | $56.55 | $1,023,810,005 | Materials | unknown | 2026-05-03 |
| FDS | $227.58 | $202,310,299 | Financials | unknown | 2026-05-03 |
| FDX | $393.67 | $552,522,064 | Industrials | unknown | 2026-05-03 |
| FE | $46.92 | $256,342,703 | Utilities | unknown | 2026-05-03 |
| FFIV | $323.20 | $249,127,270 | Information Technology | unknown | 2026-05-03 |
| FICO | $1035.50 | $437,071,495 | Information Technology | unknown | 2026-05-03 |
| FIS | $46.54 | $260,379,854 | Financials | unknown | 2026-05-03 |
| FISV | $62.14 | $310,331,053 | Financials | unknown | 2026-05-03 |
| FITB | $50.43 | $317,961,168 | Financials | unknown | 2026-05-03 |
| FIX | $1867.02 | $669,010,410 | Industrials | unknown | 2026-05-03 |
| FOX | $56.93 | $56,255,596 | Communication Services | unknown | 2026-05-03 |
| FOXA | $63.35 | $170,737,022 | Communication Services | unknown | 2026-05-03 |
| FRT | $115.32 | $102,627,461 | Real Estate | unknown | 2026-05-03 |
| FSLR | $211.71 | $435,421,684 | Information Technology | unknown | 2026-05-03 |
| FTNT | $86.29 | $454,905,607 | Information Technology | unknown | 2026-05-03 |
| FTV | $59.03 | $193,196,576 | Industrials | unknown | 2026-05-03 |
| GD | $345.84 | $513,957,524 | Industrials | unknown | 2026-05-03 |
| GDDY | $86.76 | $182,607,666 | Information Technology | unknown | 2026-05-03 |
| GE | $286.51 | $1,998,335,276 | Industrials | unknown | 2026-05-03 |
| GEHC | $61.03 | $338,066,870 | Health Care | unknown | 2026-05-03 |
| GEN | $19.37 | $118,767,272 | Information Technology | unknown | 2026-05-03 |
| GEV | $1062.95 | $2,680,465,010 | Industrials | unknown | 2026-05-03 |
| GILD | $131.65 | $721,570,351 | Health Care | unknown | 2026-05-03 |
| GIS | $34.72 | $285,482,245 | Consumer Staples | unknown | 2026-05-03 |
| GL | $152.72 | $75,917,248 | Financials | unknown | 2026-05-03 |
| GLW | $158.26 | $1,715,863,016 | Information Technology | unknown | 2026-05-03 |
| GM | $75.77 | $513,339,718 | Consumer Discretionary | unknown | 2026-05-03 |
| GNRC | $259.34 | $185,748,955 | Industrials | unknown | 2026-05-03 |
| GOOG | $383.22 | $6,108,236,699 | Communication Services | unknown | 2026-05-03 |
| GOOGL | $385.69 | $9,226,305,400 | Communication Services | unknown | 2026-05-03 |
| GPC | $104.99 | $198,635,879 | Consumer Discretionary | unknown | 2026-05-03 |
| GPN | $72.36 | $188,027,354 | Financials | unknown | 2026-05-03 |
| GRMN | $242.42 | $203,854,492 | Consumer Discretionary | unknown | 2026-05-03 |
| GS | $923.71 | $1,778,423,695 | Financials | unknown | 2026-05-03 |
| GWW | $1148.62 | $275,184,961 | Industrials | unknown | 2026-05-03 |
| HAL | $41.66 | $550,346,851 | Energy | unknown | 2026-05-03 |
| HAS | $95.27 | $167,892,877 | Consumer Discretionary | unknown | 2026-05-03 |
| HBAN | $16.63 | $350,525,822 | Financials | unknown | 2026-05-03 |
| HCA | $433.09 | $513,044,385 | Health Care | unknown | 2026-05-03 |
| HD | $323.88 | $1,187,681,830 | Consumer Discretionary | 2026-05-19 | 2026-05-03 |
| HIG | $135.81 | $200,461,610 | Financials | unknown | 2026-05-03 |
| HII | $360.60 | $166,644,722 | Industrials | unknown | 2026-05-03 |
| HLT | $318.61 | $548,698,157 | Consumer Discretionary | unknown | 2026-05-03 |
| HON | $212.50 | $849,533,142 | Industrials | unknown | 2026-05-03 |
| HOOD | $73.66 | $2,855,861,514 | Financials | unknown | 2026-05-03 |
| HPE | $28.57 | $376,996,103 | Information Technology | unknown | 2026-05-03 |
| HPQ | $20.83 | $317,193,217 | Information Technology | unknown | 2026-05-03 |
| HRL | $21.33 | $105,439,841 | Consumer Staples | unknown | 2026-05-03 |
| HSIC | $73.93 | $80,127,253 | Health Care | unknown | 2026-05-03 |
| HST | $21.13 | $163,158,875 | Real Estate | unknown | 2026-05-03 |
| HSY | $182.34 | $384,103,745 | Consumer Staples | unknown | 2026-05-03 |
| HUBB | $508.43 | $294,752,398 | Industrials | unknown | 2026-05-03 |
| HUM | $233.63 | $425,942,828 | Health Care | unknown | 2026-05-03 |
| HWM | $239.51 | $501,633,543 | Industrials | unknown | 2026-05-03 |
| IBKR | $80.46 | $355,010,010 | Financials | unknown | 2026-05-03 |
| IBM | $232.20 | $1,547,434,693 | Information Technology | unknown | 2026-05-03 |
| ICE | $154.75 | $474,658,324 | Financials | unknown | 2026-05-03 |
| IDXX | $567.46 | $305,611,310 | Health Care | unknown | 2026-05-03 |
| IEX | $214.93 | $149,657,915 | Industrials | unknown | 2026-05-03 |
| IFF | $70.81 | $102,034,170 | Materials | unknown | 2026-05-03 |
| INCY | $96.91 | $139,476,418 | Health Care | unknown | 2026-05-03 |
| INTC | $99.62 | $10,322,589,824 | Information Technology | unknown | 2026-05-03 |
| INTU | $399.04 | $1,271,950,812 | Information Technology | unknown | 2026-05-03 |
| INVH | $28.53 | $143,226,936 | Real Estate | unknown | 2026-05-03 |
| IP | $31.76 | $263,954,188 | Materials | unknown | 2026-05-03 |
| IQV | $157.77 | $253,600,077 | Health Care | unknown | 2026-05-03 |
| IR | $77.99 | $316,907,520 | Industrials | unknown | 2026-05-03 |
| IRM | $127.19 | $192,195,825 | Real Estate | unknown | 2026-05-03 |
| ISRG | $457.78 | $1,023,276,823 | Health Care | unknown | 2026-05-03 |
| IT | $146.40 | $198,621,724 | Information Technology | unknown | 2026-05-03 |
| ITW | $255.47 | $359,530,570 | Industrials | unknown | 2026-05-03 |
| IVZ | $25.89 | $168,577,890 | Financials | unknown | 2026-05-03 |
| J | $128.92 | $97,174,003 | Industrials | unknown | 2026-05-03 |
| JBHT | $248.73 | $224,660,077 | Industrials | unknown | 2026-05-03 |
| JBL | $342.47 | $336,992,105 | Information Technology | unknown | 2026-05-03 |
| JCI | $145.08 | $411,617,872 | Industrials | unknown | 2026-05-03 |
| JKHY | $154.03 | $127,566,360 | Financials | unknown | 2026-05-03 |
| JNJ | $227.19 | $1,801,933,794 | Health Care | unknown | 2026-05-03 |
| JPM | $312.47 | $2,498,248,350 | Financials | unknown | 2026-05-03 |
| KDP | $29.09 | $337,913,682 | Consumer Staples | unknown | 2026-05-03 |
| KEY | $21.87 | $275,178,721 | Financials | unknown | 2026-05-03 |
| KEYS | $352.41 | $363,926,961 | Information Technology | unknown | 2026-05-03 |
| KHC | $22.49 | $297,815,895 | Consumer Staples | unknown | 2026-05-03 |
| KIM | $23.38 | $104,759,125 | Real Estate | unknown | 2026-05-03 |
| KKR | $103.68 | $471,458,595 | Financials | unknown | 2026-05-03 |
| KLAC | $1726.26 | $1,627,117,438 | Information Technology | unknown | 2026-05-03 |
| KMB | $97.67 | $475,281,998 | Consumer Staples | unknown | 2026-05-03 |
| KMI | $32.53 | $395,087,416 | Energy | unknown | 2026-05-03 |
| KO | $78.58 | $1,061,309,947 | Consumer Staples | unknown | 2026-05-03 |
| KR | $67.77 | $321,724,656 | Consumer Staples | unknown | 2026-05-03 |
| KVUE | $17.43 | $292,912,906 | Consumer Staples | unknown | 2026-05-03 |
| L | $111.70 | $69,275,360 | Financials | unknown | 2026-05-03 |
| LDOS | $149.23 | $126,815,726 | Industrials | unknown | 2026-05-03 |
| LEN | $88.45 | $242,308,062 | Consumer Discretionary | unknown | 2026-05-03 |
| LH | $255.84 | $176,174,673 | Health Care | unknown | 2026-05-03 |
| LHX | $313.37 | $481,225,196 | Industrials | unknown | 2026-05-03 |
| LII | $526.33 | $261,471,981 | Industrials | unknown | 2026-05-03 |
| LIN | $507.92 | $974,597,910 | Materials | unknown | 2026-05-03 |
| LITE | $949.93 | $4,788,722,433 | Information Technology | unknown | 2026-05-03 |
| LLY | $963.33 | $2,880,496,632 | Health Care | unknown | 2026-05-03 |
| LMT | $512.77 | $844,517,030 | Industrials | unknown | 2026-05-03 |
| LNT | $74.06 | $146,669,263 | Utilities | unknown | 2026-05-03 |
| LOW | $233.33 | $592,002,507 | Consumer Discretionary | unknown | 2026-05-03 |
| LRCX | $256.72 | $2,343,057,510 | Information Technology | unknown | 2026-05-03 |
| LULU | $133.58 | $423,693,042 | Consumer Discretionary | unknown | 2026-05-03 |
| LUV | $38.76 | $299,830,481 | Industrials | unknown | 2026-05-03 |
| LVS | $53.79 | $235,883,167 | Consumer Discretionary | unknown | 2026-05-03 |
| LYB | $74.99 | $508,079,479 | Materials | unknown | 2026-05-03 |
| LYV | $158.25 | $435,925,821 | Communication Services | unknown | 2026-05-03 |
| MA | $495.46 | $1,728,063,805 | Financials | unknown | 2026-05-03 |
| MAA | $128.56 | $121,693,585 | Real Estate | unknown | 2026-05-03 |
| MAR | $354.97 | $500,643,386 | Consumer Discretionary | unknown | 2026-05-03 |
| MAS | $71.24 | $237,366,833 | Industrials | unknown | 2026-05-03 |
| MCD | $286.64 | $949,872,728 | Consumer Discretionary | unknown | 2026-05-03 |
| MCHP | $93.95 | $778,361,510 | Information Technology | unknown | 2026-05-03 |
| MCK | $814.02 | $660,592,438 | Health Care | unknown | 2026-05-03 |
| MCO | $455.77 | $469,875,629 | Financials | unknown | 2026-05-03 |
| MDLZ | $61.37 | $472,107,616 | Consumer Staples | unknown | 2026-05-03 |
| MDT | $80.00 | $751,340,495 | Health Care | unknown | 2026-05-03 |
| MET | $80.23 | $254,162,463 | Financials | unknown | 2026-05-03 |
| META | $608.75 | $10,409,842,142 | Communication Services | unknown | 2026-05-03 |
| MGM | $38.50 | $171,067,314 | Consumer Discretionary | unknown | 2026-05-03 |
| MKC | $50.24 | $220,516,440 | Consumer Staples | unknown | 2026-05-03 |
| MLM | $614.49 | $275,402,569 | Materials | unknown | 2026-05-03 |
| MMM | $142.50 | $551,030,547 | Industrials | unknown | 2026-05-03 |
| MNST | $77.12 | $333,131,391 | Consumer Staples | unknown | 2026-05-03 |
| MO | $74.55 | $618,101,866 | Consumer Staples | unknown | 2026-05-03 |
| MOS | $23.15 | $199,929,457 | Materials | unknown | 2026-05-03 |
| MPC | $246.15 | $480,542,285 | Energy | unknown | 2026-05-03 |
| MPWR | $1583.48 | $898,563,583 | Information Technology | unknown | 2026-05-03 |
| MRK | $112.16 | $1,130,790,454 | Health Care | unknown | 2026-05-03 |
| MRNA | $45.37 | $291,237,791 | Health Care | unknown | 2026-05-03 |
| MRSH | $166.18 | $495,574,422 | Financials | unknown | 2026-05-03 |
| MS | $190.17 | $1,058,889,122 | Financials | unknown | 2026-05-03 |
| MSCI | $588.85 | $341,073,189 | Financials | unknown | 2026-05-03 |
| MSFT | $414.44 | $14,199,203,130 | Information Technology | unknown | 2026-05-03 |
| MSI | $435.90 | $356,611,909 | Information Technology | unknown | 2026-05-03 |
| MTB | $216.44 | $219,705,986 | Financials | unknown | 2026-05-03 |
| MTD | $1267.07 | $172,039,938 | Health Care | unknown | 2026-05-03 |
| MU | $542.21 | $18,141,331,263 | Information Technology | unknown | 2026-05-03 |
| NCLH | $18.81 | $385,223,541 | Consumer Discretionary | unknown | 2026-05-03 |
| NDAQ | $91.32 | $287,444,405 | Financials | unknown | 2026-05-03 |
| NDSN | $283.20 | $90,515,758 | Industrials | unknown | 2026-05-03 |
| NEE | $96.95 | $812,483,269 | Utilities | unknown | 2026-05-03 |
| NEM | $108.62 | $875,467,783 | Materials | unknown | 2026-05-03 |
| NFLX | $92.06 | $4,100,052,950 | Communication Services | unknown | 2026-05-03 |
| NI | $48.08 | $236,337,159 | Utilities | unknown | 2026-05-03 |
| NKE | $44.40 | $978,047,103 | Consumer Discretionary | unknown | 2026-05-03 |
| NOC | $568.14 | $526,401,398 | Industrials | unknown | 2026-05-03 |
| NOW | $91.16 | $2,668,804,612 | Information Technology | unknown | 2026-05-03 |
| NRG | $153.37 | $406,333,805 | Utilities | unknown | 2026-05-03 |
| NSC | $315.90 | $379,515,083 | Industrials | unknown | 2026-05-03 |
| NTAP | $112.08 | $210,213,042 | Information Technology | unknown | 2026-05-03 |
| NTRS | $164.48 | $198,051,151 | Financials | unknown | 2026-05-03 |
| NUE | $226.04 | $332,405,101 | Materials | unknown | 2026-05-03 |
| NVDA | $198.45 | $29,322,752,129 | Information Technology | 2026-05-20 | 2026-05-03 |
| NVR | $6154.14 | $153,847,717 | Consumer Discretionary | unknown | 2026-05-03 |
| NWS | $30.41 | $27,118,835 | Communication Services | unknown | 2026-05-03 |
| NWSA | $26.24 | $84,021,590 | Communication Services | unknown | 2026-05-03 |
| NXPI | $295.24 | $846,528,774 | Information Technology | unknown | 2026-05-03 |
| O | $63.81 | $324,519,508 | Real Estate | unknown | 2026-05-03 |
| ODFL | $205.81 | $434,050,945 | Industrials | unknown | 2026-05-03 |
| OKE | $90.36 | $374,084,613 | Energy | unknown | 2026-05-03 |
| OMC | $76.92 | $328,096,859 | Communication Services | unknown | 2026-05-03 |
| ON | $103.03 | $895,898,928 | Information Technology | unknown | 2026-05-03 |
| ORCL | $171.83 | $5,341,227,190 | Information Technology | unknown | 2026-05-03 |
| ORLY | $96.67 | $471,059,047 | Consumer Discretionary | unknown | 2026-05-03 |
| OTIS | $77.08 | $267,551,601 | Industrials | unknown | 2026-05-03 |
| OXY | $58.71 | $780,559,947 | Energy | unknown | 2026-05-03 |
| PANW | $181.08 | $1,263,201,573 | Information Technology | unknown | 2026-05-03 |
| PAYX | $93.02 | $291,233,680 | Industrials | unknown | 2026-05-03 |
| PCAR | $116.08 | $363,706,776 | Industrials | unknown | 2026-05-03 |
| PCG | $16.45 | $396,260,254 | Utilities | unknown | 2026-05-03 |
| PEG | $80.15 | $186,529,573 | Utilities | unknown | 2026-05-03 |
| PEP | $157.41 | $906,192,600 | Consumer Staples | unknown | 2026-05-03 |
| PFE | $26.33 | $909,383,033 | Health Care | unknown | 2026-05-03 |
| PFG | $101.09 | $137,691,658 | Financials | unknown | 2026-05-03 |
| PG | $147.26 | $1,273,947,957 | Consumer Staples | unknown | 2026-05-03 |
| PGR | $199.31 | $509,778,799 | Financials | unknown | 2026-05-03 |
| PH | $882.23 | $630,881,983 | Industrials | unknown | 2026-05-03 |
| PHM | $119.21 | $246,635,929 | Consumer Discretionary | unknown | 2026-05-03 |
| PKG | $218.06 | $193,988,415 | Materials | unknown | 2026-05-03 |
| PLD | $141.41 | $516,136,019 | Real Estate | unknown | 2026-05-03 |
| PLTR | $144.07 | $6,726,888,212 | Information Technology | unknown | 2026-05-03 |
| PM | $166.38 | $750,677,412 | Consumer Staples | unknown | 2026-05-03 |
| PNC | $220.71 | $484,186,908 | Financials | unknown | 2026-05-03 |
| PNR | $79.10 | $170,948,548 | Industrials | unknown | 2026-05-03 |
| PNW | $103.54 | $104,029,869 | Utilities | unknown | 2026-05-03 |
| PODD | $175.04 | $203,259,776 | Health Care | unknown | 2026-05-03 |
| POOL | $208.09 | $159,027,407 | Consumer Discretionary | unknown | 2026-05-03 |
| PPG | $107.51 | $233,107,480 | Materials | unknown | 2026-05-03 |
| PPL | $37.60 | $310,872,469 | Utilities | unknown | 2026-05-03 |
| PRU | $98.62 | $224,982,170 | Financials | unknown | 2026-05-03 |
| PSA | $301.55 | $322,755,651 | Real Estate | unknown | 2026-05-03 |
| PSKY | $11.09 | $121,610,158 | Communication Services | unknown | 2026-05-03 |
| PSX | $176.19 | $465,517,168 | Energy | unknown | 2026-05-03 |
| PTC | $136.53 | $158,262,365 | Information Technology | unknown | 2026-05-03 |
| PWR | $742.21 | $618,353,016 | Industrials | unknown | 2026-05-03 |
| PYPL | $50.44 | $603,915,650 | Financials | unknown | 2026-05-03 |
| Q | $143.33 | $212,263,623 | Information Technology | unknown | 2026-05-03 |
| QCOM | $177.01 | $2,593,662,099 | Information Technology | unknown | 2026-05-03 |
| RCL | $265.55 | $730,057,196 | Consumer Discretionary | unknown | 2026-05-03 |
| REG | $78.65 | $115,682,967 | Real Estate | unknown | 2026-05-03 |
| REGN | $701.42 | $542,706,409 | Health Care | unknown | 2026-05-03 |
| RF | $28.19 | $266,182,477 | Financials | unknown | 2026-05-03 |
| RJF | $156.20 | $223,708,710 | Financials | unknown | 2026-05-03 |
| RL | $362.21 | $190,510,329 | Consumer Discretionary | unknown | 2026-05-03 |
| RMD | $205.02 | $261,280,238 | Health Care | unknown | 2026-05-03 |
| ROK | $407.43 | $261,953,710 | Industrials | unknown | 2026-05-03 |
| ROL | $54.78 | $147,446,483 | Industrials | unknown | 2026-05-03 |
| ROP | $358.22 | $414,372,883 | Information Technology | unknown | 2026-05-03 |
| ROST | $228.84 | $439,284,326 | Consumer Discretionary | unknown | 2026-05-03 |
| RSG | $206.56 | $354,349,674 | Industrials | unknown | 2026-05-03 |
| RTX | $173.99 | $948,691,256 | Industrials | unknown | 2026-05-03 |
| RVTY | $86.68 | $93,700,669 | Health Care | unknown | 2026-05-03 |
| SATS | $123.18 | $652,576,929 | Communication Services | unknown | 2026-05-03 |
| SBAC | $218.58 | $312,196,661 | Real Estate | unknown | 2026-05-03 |
| SBUX | $105.90 | $731,046,062 | Consumer Discretionary | 2026-05-05 | 2026-05-03 |
| SCHW | $91.54 | $1,111,756,052 | Financials | unknown | 2026-05-03 |
| SHW | $318.00 | $541,393,479 | Materials | unknown | 2026-05-03 |
| SJM | $96.97 | $178,247,124 | Consumer Staples | unknown | 2026-05-03 |
| SLB | $56.92 | $778,566,989 | Energy | unknown | 2026-05-03 |
| SMCI | $27.09 | $783,905,553 | Information Technology | unknown | 2026-05-03 |
| SNA | $380.39 | $157,903,766 | Industrials | unknown | 2026-05-03 |
| SNDK | $1187.00 | $14,499,480,623 | Information Technology | unknown | 2026-05-03 |
| SNPS | $489.02 | $749,841,874 | Information Technology | unknown | 2026-05-03 |
| SO | $96.71 | $418,826,823 | Utilities | unknown | 2026-05-03 |
| SOLV | $66.63 | $76,799,083 | Health Care | unknown | 2026-05-03 |
| SPG | $202.44 | $252,859,318 | Real Estate | unknown | 2026-05-03 |
| SPGI | $426.06 | $747,737,893 | Financials | unknown | 2026-05-03 |
| SRE | $94.67 | $302,010,826 | Utilities | unknown | 2026-05-03 |
| STE | $214.40 | $138,226,020 | Health Care | unknown | 2026-05-03 |
| STLD | $229.27 | $247,701,207 | Materials | unknown | 2026-05-03 |
| STT | $152.00 | $332,278,655 | Financials | unknown | 2026-05-03 |
| STX | $726.93 | $2,499,257,052 | Information Technology | unknown | 2026-05-03 |
| STZ | $152.82 | $342,196,652 | Consumer Staples | unknown | 2026-05-03 |
| SW | $39.43 | $206,061,044 | Materials | unknown | 2026-05-03 |
| SWK | $78.53 | $187,364,946 | Industrials | unknown | 2026-05-03 |
| SWKS | $69.40 | $189,372,667 | Information Technology | unknown | 2026-05-03 |
| SYF | $75.76 | $288,678,360 | Financials | unknown | 2026-05-03 |
| SYK | $294.73 | $677,866,389 | Health Care | unknown | 2026-05-03 |
| SYY | $74.05 | $411,777,225 | Consumer Staples | unknown | 2026-05-03 |
| T | $26.12 | $981,482,352 | Communication Services | unknown | 2026-05-03 |
| TAP | $42.14 | $139,408,243 | Consumer Staples | unknown | 2026-05-03 |
| TDG | $1154.45 | $439,809,733 | Industrials | unknown | 2026-05-03 |
| TDY | $640.33 | $235,598,714 | Information Technology | unknown | 2026-05-03 |
| TECH | $55.02 | $111,512,625 | Health Care | unknown | 2026-05-03 |
| TEL | $207.43 | $585,633,403 | Information Technology | unknown | 2026-05-03 |
| TER | $345.42 | $1,299,902,982 | Information Technology | unknown | 2026-05-03 |
| TFC | $50.93 | $430,958,277 | Financials | unknown | 2026-05-03 |
| TGT | $128.89 | $577,234,954 | Consumer Staples | 2026-05-20 | 2026-05-03 |
| TJX | $156.83 | $640,062,680 | Consumer Discretionary | unknown | 2026-05-03 |
| TKO | $185.95 | $238,329,966 | Communication Services | unknown | 2026-05-03 |
| TMO | $469.21 | $992,521,402 | Health Care | unknown | 2026-05-03 |
| TMUS | $196.06 | $1,279,148,095 | Communication Services | unknown | 2026-05-03 |
| TPL | $433.62 | $198,944,767 | Energy | unknown | 2026-05-03 |
| TPR | $142.74 | $241,661,800 | Consumer Discretionary | unknown | 2026-05-03 |
| TRGP | $254.28 | $292,137,730 | Energy | unknown | 2026-05-03 |
| TRMB | $68.42 | $103,659,921 | Information Technology | unknown | 2026-05-03 |
| TROW | $103.42 | $209,188,887 | Financials | unknown | 2026-05-03 |
| TRV | $304.72 | $436,908,405 | Financials | unknown | 2026-05-03 |
| TSCO | $33.83 | $391,137,209 | Consumer Discretionary | unknown | 2026-05-03 |
| TSLA | $390.82 | $25,132,318,725 | Consumer Discretionary | unknown | 2026-05-03 |
| TSN | $63.68 | $162,490,330 | Consumer Staples | unknown | 2026-05-03 |
| TT | $486.48 | $592,275,411 | Industrials | unknown | 2026-05-03 |
| TTD | $24.24 | $370,462,173 | Communication Services | unknown | 2026-05-03 |
| TTWO | $216.03 | $300,266,360 | Communication Services | unknown | 2026-05-03 |
| TXN | $281.02 | $1,997,890,300 | Information Technology | unknown | 2026-05-03 |
| TXT | $94.72 | $119,633,535 | Industrials | unknown | 2026-05-03 |
| TYL | $335.50 | $165,270,228 | Information Technology | unknown | 2026-05-03 |
| UAL | $92.52 | $768,108,299 | Industrials | unknown | 2026-05-03 |
| UBER | $75.12 | $1,024,300,169 | Industrials | unknown | 2026-05-03 |
| UDR | $36.39 | $123,581,316 | Real Estate | unknown | 2026-05-03 |
| UHS | $167.00 | $130,830,816 | Health Care | unknown | 2026-05-03 |
| ULTA | $531.95 | $347,156,721 | Consumer Discretionary | unknown | 2026-05-03 |
| UNH | $368.78 | $3,086,525,660 | Health Care | unknown | 2026-05-03 |
| UNP | $266.32 | $811,603,414 | Industrials | unknown | 2026-05-03 |
| UPS | $107.57 | $543,487,801 | Industrials | unknown | 2026-05-03 |
| URI | $949.23 | $501,170,584 | Industrials | unknown | 2026-05-03 |
| USB | $56.30 | $501,363,424 | Financials | unknown | 2026-05-03 |
| V | $328.03 | $2,185,792,010 | Financials | unknown | 2026-05-03 |
| VICI | $28.58 | $218,453,508 | Real Estate | unknown | 2026-05-03 |
| VLO | $246.87 | $725,319,195 | Energy | unknown | 2026-05-03 |
| VLTO | $87.63 | $169,916,016 | Industrials | unknown | 2026-05-03 |
| VMC | $297.32 | $278,455,903 | Materials | unknown | 2026-05-03 |
| VRSK | $181.11 | $371,462,761 | Industrials | unknown | 2026-05-03 |
| VRSN | $272.44 | $245,857,479 | Information Technology | unknown | 2026-05-03 |
| VRT | $328.31 | $1,689,537,736 | Industrials | unknown | 2026-05-03 |
| VRTX | $423.92 | $452,492,008 | Health Care | unknown | 2026-05-03 |
| VST | $155.28 | $574,788,266 | Utilities | unknown | 2026-05-03 |
| VTR | $88.02 | $373,195,543 | Real Estate | unknown | 2026-05-03 |
| VTRS | $15.04 | $136,165,010 | Health Care | unknown | 2026-05-03 |
| VZ | $48.11 | $1,245,068,787 | Communication Services | unknown | 2026-05-03 |
| WAB | $264.95 | $289,507,295 | Industrials | unknown | 2026-05-03 |
| WAT | $307.12 | $281,996,478 | Health Care | unknown | 2026-05-03 |
| WBD | $26.97 | $504,948,614 | Communication Services | unknown | 2026-05-03 |
| WDAY | $126.96 | $633,832,478 | Information Technology | unknown | 2026-05-03 |
| WDC | $431.52 | $2,816,438,609 | Information Technology | unknown | 2026-05-03 |
| WEC | $117.46 | $197,673,484 | Utilities | unknown | 2026-05-03 |
| WELL | $216.91 | $558,524,818 | Real Estate | unknown | 2026-05-03 |
| WFC | $80.81 | $1,352,862,384 | Financials | unknown | 2026-05-03 |
| WM | $228.77 | $458,145,187 | Industrials | unknown | 2026-05-03 |
| WMB | $75.54 | $411,540,938 | Energy | unknown | 2026-05-03 |
| WMT | $131.60 | $2,118,892,669 | Consumer Staples | 2026-05-14 | 2026-05-03 |
| WRB | $66.38 | $143,557,829 | Financials | unknown | 2026-05-03 |
| WSM | $179.99 | $194,692,117 | Consumer Discretionary | unknown | 2026-05-03 |
| WST | $300.68 | $270,817,334 | Health Care | unknown | 2026-05-03 |
| WTW | $256.34 | $206,809,105 | Financials | unknown | 2026-05-03 |
| WY | $23.99 | $113,051,495 | Real Estate | unknown | 2026-05-03 |
| WYNN | $105.98 | $139,353,629 | Consumer Discretionary | unknown | 2026-05-03 |
| XEL | $82.58 | $371,239,061 | Utilities | unknown | 2026-05-03 |
| XOM | $152.75 | $2,851,644,883 | Energy | unknown | 2026-05-03 |
| XYL | $115.37 | $319,332,582 | Industrials | unknown | 2026-05-03 |
| XYZ | $71.81 | $327,664,184 | Financials | unknown | 2026-05-03 |
| YUM | $158.36 | $258,634,215 | Consumer Discretionary | unknown | 2026-05-03 |
| ZBH | $82.90 | $231,211,895 | Health Care | unknown | 2026-05-03 |
| ZBRA | $227.08 | $178,984,655 | Information Technology | unknown | 2026-05-03 |
| ZTS | $114.16 | $395,697,405 | Health Care | unknown | 2026-05-03 |
