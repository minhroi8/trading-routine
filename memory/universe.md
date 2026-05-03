---
screened_on: 2026-05-03
expires_on: 2026-05-10
total_passed: 241
total_rejected: 262
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
| AAPL | $280.11 | $331,983,170 | Information Technology | unknown | 2026-05-03 |
| ABBV | $206.66 | $55,488,742 | Health Care | unknown | 2026-05-03 |
| ABT | $89.47 | $52,417,069 | Health Care | unknown | 2026-05-03 |
| ACN | $179.80 | $44,492,585 | Information Technology | unknown | 2026-05-03 |
| ADBE | $250.78 | $43,840,501 | Information Technology | unknown | 2026-05-03 |
| ADI | $397.71 | $50,596,415 | Information Technology | unknown | 2026-05-03 |
| ADP | $214.16 | $28,643,774 | Industrials | unknown | 2026-05-03 |
| ADSK | $244.17 | $23,665,423 | Information Technology | unknown | 2026-05-03 |
| AJG | $208.09 | $31,775,456 | Financials | unknown | 2026-05-03 |
| AKAM | $103.87 | $25,373,429 | Information Technology | unknown | 2026-05-03 |
| AMAT | $388.88 | $83,677,000 | Information Technology | unknown | 2026-05-03 |
| AMD | $360.55 | $198,178,654 | Information Technology | unknown | 2026-05-03 |
| AMGN | $329.80 | $36,469,617 | Health Care | unknown | 2026-05-03 |
| AMP | $467.20 | $21,674,420 | Financials | unknown | 2026-05-03 |
| AMT | $181.65 | $25,593,226 | Real Estate | unknown | 2026-05-03 |
| AMZN | $268.29 | $476,342,679 | Consumer Discretionary | unknown | 2026-05-03 |
| ANET | $172.74 | $54,620,295 | Information Technology | unknown | 2026-05-03 |
| AON | $311.65 | $30,336,617 | Financials | unknown | 2026-05-03 |
| APD | $301.14 | $21,693,767 | Materials | unknown | 2026-05-03 |
| APH | $142.31 | $57,441,389 | Information Technology | unknown | 2026-05-03 |
| APO | $130.49 | $35,364,798 | Financials | unknown | 2026-05-03 |
| APP | $459.95 | $57,373,677 | Information Technology | unknown | 2026-05-03 |
| AVGO | $421.21 | $245,029,857 | Information Technology | unknown | 2026-05-03 |
| AXON | $402.31 | $20,350,821 | Industrials | unknown | 2026-05-03 |
| AXP | $319.71 | $42,845,686 | Financials | unknown | 2026-05-03 |
| AZO | $3595.95 | $31,637,422 | Consumer Discretionary | unknown | 2026-05-03 |
| BA | $227.40 | $48,687,808 | Industrials | unknown | 2026-05-03 |
| BAC | $53.23 | $96,194,048 | Financials | unknown | 2026-05-03 |
| BDX | $149.44 | $25,529,611 | Health Care | unknown | 2026-05-03 |
| BK | $133.76 | $24,304,237 | Financials | unknown | 2026-05-03 |
| BKNG | $169.61 | $82,611,068 | Consumer Discretionary | unknown | 2026-05-03 |
| BKR | $69.12 | $27,135,150 | Energy | unknown | 2026-05-03 |
| BLK | $1062.20 | $45,417,132 | Financials | unknown | 2026-05-03 |
| BMY | $58.20 | $30,384,221 | Health Care | unknown | 2026-05-03 |
| BRK.B | $473.07 | $52,391,758 | Financials | unknown | 2026-05-03 |
| BSX | $56.52 | $79,760,172 | Health Care | unknown | 2026-05-03 |
| BX | $126.35 | $33,595,570 | Financials | unknown | 2026-05-03 |
| C | $127.42 | $51,344,880 | Financials | unknown | 2026-05-03 |
| CAH | $195.23 | $21,535,658 | Health Care | unknown | 2026-05-03 |
| CARR | $67.64 | $29,572,946 | Industrials | unknown | 2026-05-03 |
| CAT | $890.32 | $67,398,867 | Industrials | unknown | 2026-05-03 |
| CB | $326.30 | $25,675,925 | Financials | unknown | 2026-05-03 |
| CCL | $26.64 | $38,395,288 | Consumer Discretionary | unknown | 2026-05-03 |
| CDNS | $341.00 | $41,013,591 | Information Technology | unknown | 2026-05-03 |
| CEG | $307.75 | $38,483,696 | Utilities | unknown | 2026-05-03 |
| CF | $122.77 | $22,742,091 | Materials | unknown | 2026-05-03 |
| CFG | $64.42 | $20,531,781 | Financials | unknown | 2026-05-03 |
| CHRW | $177.31 | $21,717,858 | Industrials | unknown | 2026-05-03 |
| CHTR | $171.93 | $32,164,662 | Communication Services | unknown | 2026-05-03 |
| CL | $87.28 | $25,690,776 | Consumer Staples | unknown | 2026-05-03 |
| CMCSA | $27.18 | $53,352,387 | Communication Services | unknown | 2026-05-03 |
| CME | $289.63 | $36,926,473 | Financials | unknown | 2026-05-03 |
| CMG | $32.99 | $38,580,779 | Consumer Discretionary | unknown | 2026-05-03 |
| CMI | $657.83 | $31,191,704 | Industrials | unknown | 2026-05-03 |
| COF | $191.90 | $49,820,169 | Financials | unknown | 2026-05-03 |
| COIN | $191.37 | $37,650,978 | Financials | unknown | 2026-05-03 |
| COP | $123.28 | $61,470,424 | Energy | unknown | 2026-05-03 |
| COR | $304.08 | $24,841,245 | Health Care | unknown | 2026-05-03 |
| COST | $1011.69 | $56,540,755 | Consumer Staples | unknown | 2026-05-03 |
| CRM | $183.78 | $91,951,177 | Information Technology | unknown | 2026-05-03 |
| CRWD | $455.58 | $45,199,554 | Information Technology | unknown | 2026-05-03 |
| CSCO | $91.85 | $74,343,485 | Information Technology | unknown | 2026-05-03 |
| CSX | $45.08 | $39,450,697 | Industrials | unknown | 2026-05-03 |
| CTRA | $35.37 | $20,692,162 | Energy | unknown | 2026-05-03 |
| CVS | $82.08 | $31,233,593 | Health Care | unknown | 2026-05-03 |
| CVX | $190.66 | $71,174,540 | Energy | unknown | 2026-05-03 |
| DAL | $68.98 | $34,095,181 | Industrials | unknown | 2026-05-03 |
| DASH | $175.88 | $37,933,633 | Consumer Discretionary | unknown | 2026-05-03 |
| DDOG | $140.55 | $29,331,527 | Information Technology | unknown | 2026-05-03 |
| DE | $577.57 | $45,563,229 | Industrials | unknown | 2026-05-03 |
| DELL | $210.24 | $48,498,830 | Information Technology | unknown | 2026-05-03 |
| DHI | $150.00 | $22,065,909 | Consumer Discretionary | unknown | 2026-05-03 |
| DHR | $175.13 | $56,753,078 | Health Care | unknown | 2026-05-03 |
| DIS | $103.11 | $41,567,227 | Communication Services | unknown | 2026-05-03 |
| DLR | $200.74 | $20,123,438 | Real Estate | unknown | 2026-05-03 |
| DOW | $40.30 | $35,026,952 | Materials | unknown | 2026-05-03 |
| DPZ | $337.75 | $24,323,139 | Consumer Discretionary | unknown | 2026-05-03 |
| DVN | $50.56 | $33,227,127 | Energy | unknown | 2026-05-03 |
| EBAY | $104.03 | $28,193,746 | Consumer Discretionary | unknown | 2026-05-03 |
| EFX | $173.91 | $21,710,697 | Industrials | unknown | 2026-05-03 |
| ELV | $372.82 | $31,158,515 | Health Care | unknown | 2026-05-03 |
| EMR | $137.49 | $22,992,712 | Industrials | unknown | 2026-05-03 |
| EOG | $139.01 | $29,713,830 | Energy | unknown | 2026-05-03 |
| EQIX | $1085.18 | $38,517,637 | Real Estate | unknown | 2026-05-03 |
| EQT | $58.69 | $29,290,203 | Energy | unknown | 2026-05-03 |
| ETN | $425.56 | $52,310,576 | Industrials | unknown | 2026-05-03 |
| EW | $83.99 | $24,687,888 | Health Care | unknown | 2026-05-03 |
| EXC | $46.51 | $23,690,272 | Utilities | unknown | 2026-05-03 |
| EXPE | $251.95 | $22,144,902 | Consumer Discretionary | unknown | 2026-05-03 |
| F | $11.88 | $24,986,226 | Consumer Discretionary | unknown | 2026-05-03 |
| FANG | $207.44 | $25,618,232 | Energy | unknown | 2026-05-03 |
| FCX | $56.56 | $59,503,804 | Materials | unknown | 2026-05-03 |
| FDX | $393.85 | $28,448,400 | Industrials | unknown | 2026-05-03 |
| FICO | $1035.37 | $30,967,814 | Information Technology | unknown | 2026-05-03 |
| FITB | $50.43 | $21,009,030 | Financials | unknown | 2026-05-03 |
| FTNT | $86.28 | $21,020,611 | Information Technology | unknown | 2026-05-03 |
| GD | $345.86 | $26,619,552 | Industrials | unknown | 2026-05-03 |
| GE | $286.53 | $98,155,982 | Industrials | unknown | 2026-05-03 |
| GEV | $1063.32 | $99,237,194 | Industrials | unknown | 2026-05-03 |
| GILD | $131.63 | $26,895,749 | Health Care | unknown | 2026-05-03 |
| GLW | $158.27 | $75,217,241 | Information Technology | unknown | 2026-05-03 |
| GM | $75.78 | $29,674,733 | Consumer Discretionary | unknown | 2026-05-03 |
| GOOG | $383.28 | $130,369,386 | Communication Services | unknown | 2026-05-03 |
| GOOGL | $385.79 | $299,029,659 | Communication Services | unknown | 2026-05-03 |
| GS | $923.71 | $63,409,096 | Financials | unknown | 2026-05-03 |
| GWW | $1148.97 | $20,911,049 | Industrials | unknown | 2026-05-03 |
| HAL | $41.66 | $39,136,415 | Energy | unknown | 2026-05-03 |
| HCA | $433.22 | $26,421,676 | Health Care | unknown | 2026-05-03 |
| HD | $323.92 | $43,420,160 | Consumer Discretionary | unknown | 2026-05-03 |
| HLT | $318.56 | $34,798,800 | Consumer Discretionary | unknown | 2026-05-03 |
| HON | $212.44 | $31,593,486 | Industrials | unknown | 2026-05-03 |
| HOOD | $73.67 | $68,937,179 | Financials | unknown | 2026-05-03 |
| HPE | $28.59 | $28,744,589 | Information Technology | unknown | 2026-05-03 |
| HSY | $182.34 | $20,396,456 | Consumer Staples | unknown | 2026-05-03 |
| HUBB | $508.31 | $21,155,606 | Industrials | unknown | 2026-05-03 |
| HUM | $233.79 | $21,008,193 | Health Care | unknown | 2026-05-03 |
| HWM | $239.54 | $22,772,450 | Industrials | unknown | 2026-05-03 |
| IBM | $232.29 | $60,125,299 | Information Technology | unknown | 2026-05-03 |
| ICE | $154.81 | $25,130,648 | Financials | unknown | 2026-05-03 |
| INTC | $99.66 | $278,709,444 | Information Technology | unknown | 2026-05-03 |
| INTU | $398.95 | $87,397,360 | Information Technology | unknown | 2026-05-03 |
| ISRG | $457.85 | $46,311,748 | Health Care | unknown | 2026-05-03 |
| ITW | $255.46 | $21,103,227 | Industrials | unknown | 2026-05-03 |
| JBL | $342.52 | $21,367,861 | Information Technology | unknown | 2026-05-03 |
| JNJ | $227.17 | $74,919,295 | Health Care | unknown | 2026-05-03 |
| JPM | $312.48 | $63,771,400 | Financials | unknown | 2026-05-03 |
| KDP | $29.10 | $23,606,241 | Consumer Staples | unknown | 2026-05-03 |
| KEYS | $352.35 | $23,470,656 | Information Technology | unknown | 2026-05-03 |
| KKR | $103.66 | $27,633,953 | Financials | unknown | 2026-05-03 |
| KLAC | $1725.08 | $107,238,758 | Information Technology | unknown | 2026-05-03 |
| KMI | $32.53 | $22,959,365 | Energy | unknown | 2026-05-03 |
| KO | $78.58 | $64,855,320 | Consumer Staples | unknown | 2026-05-03 |
| LHX | $313.53 | $34,734,541 | Industrials | unknown | 2026-05-03 |
| LIN | $508.09 | $46,208,388 | Materials | unknown | 2026-05-03 |
| LLY | $963.76 | $108,981,307 | Health Care | unknown | 2026-05-03 |
| LMT | $512.94 | $39,628,063 | Industrials | unknown | 2026-05-03 |
| LOW | $233.41 | $25,409,308 | Consumer Discretionary | unknown | 2026-05-03 |
| LRCX | $256.71 | $88,345,515 | Information Technology | unknown | 2026-05-03 |
| LYB | $74.96 | $30,241,458 | Materials | unknown | 2026-05-03 |
| LYV | $158.28 | $21,720,971 | Communication Services | unknown | 2026-05-03 |
| MA | $495.40 | $86,616,869 | Financials | unknown | 2026-05-03 |
| MAR | $354.90 | $30,935,657 | Consumer Discretionary | unknown | 2026-05-03 |
| MCD | $286.69 | $34,725,858 | Consumer Discretionary | unknown | 2026-05-03 |
| MCHP | $93.94 | $38,420,111 | Information Technology | unknown | 2026-05-03 |
| MCK | $814.54 | $30,452,595 | Health Care | unknown | 2026-05-03 |
| MCO | $455.83 | $28,539,017 | Financials | unknown | 2026-05-03 |
| MDLZ | $61.37 | $29,101,711 | Consumer Staples | unknown | 2026-05-03 |
| MDT | $80.00 | $53,487,408 | Health Care | unknown | 2026-05-03 |
| META | $608.61 | $320,766,204 | Communication Services | unknown | 2026-05-03 |
| MMM | $142.51 | $22,415,610 | Industrials | unknown | 2026-05-03 |
| MO | $74.55 | $41,259,118 | Consumer Staples | unknown | 2026-05-03 |
| MPC | $246.22 | $26,615,550 | Energy | unknown | 2026-05-03 |
| MPWR | $1583.36 | $57,079,686 | Information Technology | unknown | 2026-05-03 |
| MRK | $112.17 | $46,418,969 | Health Care | unknown | 2026-05-03 |
| MRSH | $166.21 | $21,420,213 | Financials | unknown | 2026-05-03 |
| MS | $190.17 | $46,930,815 | Financials | unknown | 2026-05-03 |
| MSCI | $588.82 | $20,324,981 | Financials | unknown | 2026-05-03 |
| MSFT | $414.46 | $372,841,923 | Information Technology | unknown | 2026-05-03 |
| MSI | $436.06 | $22,956,747 | Information Technology | unknown | 2026-05-03 |
| MU | $542.26 | $286,984,822 | Information Technology | unknown | 2026-05-03 |
| NEE | $96.95 | $37,664,138 | Utilities | unknown | 2026-05-03 |
| NEM | $108.61 | $39,333,737 | Materials | unknown | 2026-05-03 |
| NFLX | $92.09 | $207,149,523 | Communication Services | unknown | 2026-05-03 |
| NKE | $44.41 | $48,776,902 | Consumer Discretionary | unknown | 2026-05-03 |
| NOC | $568.30 | $26,999,021 | Industrials | unknown | 2026-05-03 |
| NOW | $91.15 | $99,969,445 | Information Technology | unknown | 2026-05-03 |
| NRG | $153.32 | $24,244,181 | Utilities | unknown | 2026-05-03 |
| NVDA | $198.39 | $834,561,293 | Information Technology | unknown | 2026-05-03 |
| NXPI | $295.27 | $37,251,630 | Information Technology | unknown | 2026-05-03 |
| ODFL | $205.78 | $24,095,113 | Industrials | unknown | 2026-05-03 |
| ON | $103.02 | $44,220,290 | Information Technology | unknown | 2026-05-03 |
| ORCL | $171.83 | $138,773,371 | Information Technology | unknown | 2026-05-03 |
| ORLY | $96.68 | $20,657,046 | Consumer Discretionary | unknown | 2026-05-03 |
| OXY | $58.73 | $35,215,774 | Energy | unknown | 2026-05-03 |
| PANW | $181.08 | $48,912,899 | Information Technology | unknown | 2026-05-03 |
| PCG | $16.45 | $23,807,064 | Utilities | unknown | 2026-05-03 |
| PEP | $157.41 | $34,527,533 | Consumer Staples | unknown | 2026-05-03 |
| PFE | $26.33 | $45,338,493 | Health Care | unknown | 2026-05-03 |
| PG | $147.26 | $50,047,377 | Consumer Staples | unknown | 2026-05-03 |
| PGR | $199.34 | $24,049,931 | Financials | unknown | 2026-05-03 |
| PH | $881.87 | $55,276,510 | Industrials | unknown | 2026-05-03 |
| PLD | $141.48 | $21,280,796 | Real Estate | unknown | 2026-05-03 |
| PLTR | $144.06 | $137,306,528 | Information Technology | unknown | 2026-05-03 |
| PM | $166.45 | $34,367,941 | Consumer Staples | unknown | 2026-05-03 |
| PNC | $220.75 | $25,520,355 | Financials | unknown | 2026-05-03 |
| PSX | $176.22 | $29,485,415 | Energy | unknown | 2026-05-03 |
| PWR | $742.01 | $40,119,964 | Industrials | unknown | 2026-05-03 |
| PYPL | $50.43 | $27,545,971 | Financials | unknown | 2026-05-03 |
| QCOM | $177.03 | $66,359,346 | Information Technology | unknown | 2026-05-03 |
| RCL | $265.63 | $38,071,309 | Consumer Discretionary | unknown | 2026-05-03 |
| REGN | $701.26 | $30,837,872 | Health Care | unknown | 2026-05-03 |
| ROP | $358.28 | $23,906,819 | Information Technology | unknown | 2026-05-03 |
| RSG | $206.51 | $21,523,644 | Industrials | unknown | 2026-05-03 |
| RTX | $173.97 | $39,612,587 | Industrials | unknown | 2026-05-03 |
| SBUX | $105.92 | $32,596,340 | Consumer Discretionary | unknown | 2026-05-03 |
| SCHW | $91.54 | $58,415,944 | Financials | unknown | 2026-05-03 |
| SHW | $318.03 | $30,871,437 | Materials | unknown | 2026-05-03 |
| SLB | $56.94 | $50,102,680 | Energy | unknown | 2026-05-03 |
| SMCI | $27.08 | $31,035,860 | Information Technology | unknown | 2026-05-03 |
| SNPS | $488.92 | $35,761,139 | Information Technology | unknown | 2026-05-03 |
| SO | $96.73 | $21,050,375 | Utilities | unknown | 2026-05-03 |
| SPGI | $426.03 | $42,472,448 | Financials | unknown | 2026-05-03 |
| STX | $726.85 | $91,518,740 | Information Technology | unknown | 2026-05-03 |
| SYK | $294.70 | $45,553,138 | Health Care | unknown | 2026-05-03 |
| SYY | $74.09 | $24,792,505 | Consumer Staples | unknown | 2026-05-03 |
| T | $26.13 | $57,805,505 | Communication Services | unknown | 2026-05-03 |
| TDG | $1154.51 | $30,174,197 | Industrials | unknown | 2026-05-03 |
| TEL | $207.60 | $43,349,188 | Information Technology | unknown | 2026-05-03 |
| TER | $345.44 | $62,528,519 | Information Technology | unknown | 2026-05-03 |
| TFC | $50.93 | $25,480,157 | Financials | unknown | 2026-05-03 |
| TGT | $128.91 | $28,348,395 | Consumer Staples | unknown | 2026-05-03 |
| TJX | $156.84 | $24,174,189 | Consumer Discretionary | unknown | 2026-05-03 |
| TMO | $469.06 | $68,836,583 | Health Care | unknown | 2026-05-03 |
| TMUS | $196.03 | $60,882,159 | Communication Services | unknown | 2026-05-03 |
| TSCO | $33.84 | $25,068,258 | Consumer Discretionary | unknown | 2026-05-03 |
| TSLA | $390.71 | $327,227,331 | Consumer Discretionary | unknown | 2026-05-03 |
| TT | $486.56 | $41,783,904 | Industrials | unknown | 2026-05-03 |
| TXN | $280.95 | $83,238,687 | Information Technology | unknown | 2026-05-03 |
| UAL | $92.52 | $31,224,447 | Industrials | unknown | 2026-05-03 |
| UBER | $75.16 | $54,083,371 | Industrials | unknown | 2026-05-03 |
| UNH | $368.78 | $108,300,976 | Health Care | unknown | 2026-05-03 |
| UNP | $266.38 | $47,132,169 | Industrials | unknown | 2026-05-03 |
| UPS | $107.60 | $21,063,867 | Industrials | unknown | 2026-05-03 |
| URI | $949.06 | $42,195,985 | Industrials | unknown | 2026-05-03 |
| USB | $56.30 | $32,154,582 | Financials | unknown | 2026-05-03 |
| V | $328.08 | $129,907,017 | Financials | unknown | 2026-05-03 |
| VLO | $246.87 | $38,311,545 | Energy | unknown | 2026-05-03 |
| VST | $155.32 | $25,721,084 | Utilities | unknown | 2026-05-03 |
| VTR | $88.07 | $21,710,810 | Real Estate | unknown | 2026-05-03 |
| VZ | $48.14 | $61,478,417 | Communication Services | unknown | 2026-05-03 |
| WAB | $265.11 | $20,342,199 | Industrials | unknown | 2026-05-03 |
| WAT | $307.03 | $23,077,308 | Health Care | unknown | 2026-05-03 |
| WBD | $26.98 | $31,739,407 | Communication Services | unknown | 2026-05-03 |
| WDAY | $127.03 | $33,057,946 | Information Technology | unknown | 2026-05-03 |
| WDC | $431.62 | $88,498,858 | Information Technology | unknown | 2026-05-03 |
| WELL | $216.97 | $26,227,846 | Real Estate | unknown | 2026-05-03 |
| WFC | $80.81 | $71,391,099 | Financials | unknown | 2026-05-03 |
| WM | $228.75 | $23,746,121 | Industrials | unknown | 2026-05-03 |
| WMB | $75.56 | $24,268,162 | Energy | unknown | 2026-05-03 |
| WMT | $131.62 | $67,182,726 | Consumer Staples | unknown | 2026-05-03 |
| XOM | $152.76 | $104,750,121 | Energy | unknown | 2026-05-03 |
