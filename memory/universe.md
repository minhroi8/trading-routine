---
screened_on: 2026-05-09
expires_on: 2026-05-16
total_passed: 273
total_rejected: 1232
universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
source_500: https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv
source_400: https://www.ishares.com/us/products/239763/ishares-core-sp-midcap-etf/1467271812596.ajax?fileType=csv&fileName=IJH_holdings&dataType=fund
source_600: https://www.ishares.com/us/products/239774/ishares-core-sp-smallcap-etf/1467271812596.ajax?fileType=csv&fileName=IJR_holdings&dataType=fund
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
| AAL | $13.36 | $31,185,718 | Industrials | mid | unknown | 2026-05-09 |
| AAPL | $293.15 | $373,999,796 | Information Technology | large | unknown | 2026-05-09 |
| ABBV | $201.36 | $55,724,426 | Health Care | large | unknown | 2026-05-09 |
| ABNB | $141.46 | $22,639,350 | Consumer Discretionary | large | unknown | 2026-05-09 |
| ABT | $84.29 | $58,409,487 | Health Care | large | unknown | 2026-05-09 |
| ACN | $180.47 | $46,371,227 | Information Technology | large | unknown | 2026-05-09 |
| ADBE | $252.99 | $44,298,589 | Information Technology | large | unknown | 2026-05-09 |
| ADI | $416.52 | $57,029,261 | Information Technology | large | unknown | 2026-05-09 |
| ADP | $213.04 | $29,667,874 | Industrials | large | unknown | 2026-05-09 |
| ADSK | $244.39 | $23,762,301 | Information Technology | large | unknown | 2026-05-09 |
| AJG | $198.75 | $30,284,669 | Financials | large | unknown | 2026-05-09 |
| AKAM | $147.78 | $31,950,967 | Information Technology | large | unknown | 2026-05-09 |
| ALB | $203.53 | $22,393,881 | Materials | large | unknown | 2026-05-09 |
| AMAT | $435.33 | $90,082,007 | Information Technology | large | unknown | 2026-05-09 |
| AMD | $455.07 | $285,897,681 | Information Technology | large | unknown | 2026-05-09 |
| AMGN | $331.72 | $33,400,717 | Health Care | large | unknown | 2026-05-09 |
| AMP | $465.03 | $20,557,995 | Financials | large | unknown | 2026-05-09 |
| AMT | $176.53 | $23,373,509 | Real Estate | large | unknown | 2026-05-09 |
| AMZN | $272.54 | $496,229,182 | Consumer Discretionary | large | unknown | 2026-05-09 |
| ANET | $141.72 | $76,686,662 | Information Technology | large | unknown | 2026-05-09 |
| AON | $312.84 | $29,865,593 | Financials | large | unknown | 2026-05-09 |
| APH | $127.95 | $69,314,931 | Information Technology | large | unknown | 2026-05-09 |
| APO | $133.13 | $35,165,128 | Financials | large | unknown | 2026-05-09 |
| APP | $468.39 | $71,892,068 | Information Technology | large | unknown | 2026-05-09 |
| AVGO | $429.87 | $245,989,933 | Information Technology | large | unknown | 2026-05-09 |
| AXON | $403.29 | $20,709,766 | Industrials | large | unknown | 2026-05-09 |
| AXP | $315.99 | $45,986,655 | Financials | large | unknown | 2026-05-09 |
| AZO | $3496.19 | $35,418,646 | Consumer Discretionary | large | unknown | 2026-05-09 |
| BA | $237.40 | $50,752,760 | Industrials | large | unknown | 2026-05-09 |
| BAC | $51.28 | $100,595,331 | Financials | large | unknown | 2026-05-09 |
| BDX | $149.41 | $30,517,762 | Health Care | large | unknown | 2026-05-09 |
| BK | $130.49 | $26,639,649 | Financials | large | unknown | 2026-05-09 |
| BKNG | $165.94 | $76,432,798 | Consumer Discretionary | large | unknown | 2026-05-09 |
| BKR | $63.90 | $29,655,160 | Energy | large | unknown | 2026-05-09 |
| BLD | $427.98 | $40,053,998 | Consumer Discretionary | mid | unknown | 2026-05-09 |
| BLK | $1083.86 | $43,781,193 | Financials | large | unknown | 2026-05-09 |
| BMY | $56.16 | $33,629,128 | Health Care | large | unknown | 2026-05-09 |
| BRK.B | $475.65 | $61,226,961 | Financials | large | unknown | 2026-05-09 |
| BSX | $53.90 | $82,221,014 | Health Care | large | unknown | 2026-05-09 |
| BX | $123.68 | $31,550,488 | Financials | large | unknown | 2026-05-09 |
| C | $125.55 | $61,427,948 | Financials | large | unknown | 2026-05-09 |
| CAH | $183.73 | $25,105,971 | Health Care | large | unknown | 2026-05-09 |
| CAR | $145.54 | $57,217,941 | Industrials | mid | unknown | 2026-05-09 |
| CARR | $66.78 | $30,889,712 | Industrials | large | unknown | 2026-05-09 |
| CAT | $897.03 | $79,939,006 | Industrials | large | unknown | 2026-05-09 |
| CB | $319.56 | $25,576,810 | Financials | large | unknown | 2026-05-09 |
| CBOE | $347.99 | $21,343,651 | Financials | large | unknown | 2026-05-09 |
| CCL | $26.39 | $41,989,004 | Consumer Discretionary | large | unknown | 2026-05-09 |
| CDNS | $362.50 | $45,746,262 | Information Technology | large | unknown | 2026-05-09 |
| CEG | $303.50 | $40,819,415 | Utilities | large | unknown | 2026-05-09 |
| CF | $115.06 | $21,958,739 | Materials | large | unknown | 2026-05-09 |
| CHRW | $171.39 | $25,026,710 | Industrials | large | unknown | 2026-05-09 |
| CHTR | $154.75 | $34,328,610 | Communication Services | large | unknown | 2026-05-09 |
| CI | $288.11 | $21,907,113 | Health Care | large | unknown | 2026-05-09 |
| CL | $87.54 | $28,392,131 | Consumer Staples | large | unknown | 2026-05-09 |
| CMCSA | $25.39 | $57,406,662 | Communication Services | large | unknown | 2026-05-09 |
| CME | $281.09 | $33,607,223 | Financials | large | unknown | 2026-05-09 |
| CMG | $32.47 | $41,999,150 | Consumer Discretionary | large | unknown | 2026-05-09 |
| CMI | $679.58 | $37,796,393 | Industrials | large | unknown | 2026-05-09 |
| COF | $189.40 | $51,502,684 | Financials | large | unknown | 2026-05-09 |
| COIN | $201.28 | $43,215,051 | Financials | large | unknown | 2026-05-09 |
| COP | $113.76 | $66,178,166 | Energy | large | unknown | 2026-05-09 |
| COR | $261.29 | $34,428,311 | Health Care | large | unknown | 2026-05-09 |
| COST | $1008.54 | $55,511,345 | Consumer Staples | large | unknown | 2026-05-09 |
| CRM | $181.66 | $92,318,687 | Information Technology | large | unknown | 2026-05-09 |
| CRS | $427.76 | $27,669,703 | Industrials | mid | unknown | 2026-05-09 |
| CRWD | $527.68 | $41,287,409 | Information Technology | large | unknown | 2026-05-09 |
| CSCO | $96.57 | $75,718,930 | Information Technology | large | unknown | 2026-05-09 |
| CSX | $44.80 | $39,932,815 | Industrials | large | unknown | 2026-05-09 |
| CTRA | $32.56 | $22,273,659 | Energy | large | unknown | 2026-05-09 |
| CTSH | $51.69 | $20,585,629 | Information Technology | large | unknown | 2026-05-09 |
| CVS | $90.56 | $35,254,006 | Health Care | large | unknown | 2026-05-09 |
| CVX | $181.48 | $62,596,375 | Energy | large | unknown | 2026-05-09 |
| DAL | $73.33 | $30,597,405 | Industrials | large | unknown | 2026-05-09 |
| DASH | $163.84 | $46,084,430 | Consumer Discretionary | large | unknown | 2026-05-09 |
| DDOG | $200.23 | $45,676,246 | Information Technology | large | unknown | 2026-05-09 |
| DE | $574.57 | $39,215,864 | Industrials | large | unknown | 2026-05-09 |
| DELL | $260.31 | $56,280,315 | Information Technology | large | unknown | 2026-05-09 |
| DHR | $171.12 | $57,333,230 | Health Care | large | unknown | 2026-05-09 |
| DIS | $107.98 | $51,186,267 | Communication Services | large | unknown | 2026-05-09 |
| DOCN | $164.07 | $25,207,195 | Information Technology | mid | unknown | 2026-05-09 |
| DOW | $36.87 | $32,679,264 | Materials | large | unknown | 2026-05-09 |
| DPZ | $323.37 | $25,442,679 | Consumer Discretionary | large | unknown | 2026-05-09 |
| DVN | $45.62 | $36,495,973 | Energy | large | unknown | 2026-05-09 |
| EBAY | $107.66 | $36,720,810 | Consumer Discretionary | large | unknown | 2026-05-09 |
| EFX | $175.75 | $22,085,994 | Industrials | large | unknown | 2026-05-09 |
| ELV | $377.64 | $32,717,147 | Health Care | large | unknown | 2026-05-09 |
| EME | $921.71 | $21,079,801 | Industrials | large | unknown | 2026-05-09 |
| EMR | $141.28 | $24,336,359 | Industrials | large | unknown | 2026-05-09 |
| ENTG | $149.10 | $21,863,583 | Information Technology | mid | unknown | 2026-05-09 |
| EOG | $129.92 | $31,969,450 | Energy | large | unknown | 2026-05-09 |
| EQIX | $1071.32 | $40,010,760 | Real Estate | large | unknown | 2026-05-09 |
| EQT | $55.95 | $33,444,111 | Energy | large | unknown | 2026-05-09 |
| ETN | $401.56 | $66,159,632 | Industrials | large | unknown | 2026-05-09 |
| EW | $79.95 | $24,093,840 | Health Care | large | unknown | 2026-05-09 |
| EXC | $43.89 | $27,201,539 | Utilities | large | unknown | 2026-05-09 |
| EXPE | $229.78 | $23,585,015 | Consumer Discretionary | large | unknown | 2026-05-09 |
| F | $12.32 | $27,773,605 | Consumer Discretionary | large | unknown | 2026-05-09 |
| FANG | $188.43 | $26,726,773 | Energy | large | unknown | 2026-05-09 |
| FCX | $61.64 | $63,535,950 | Materials | large | unknown | 2026-05-09 |
| FDX | $378.38 | $34,737,768 | Industrials | large | unknown | 2026-05-09 |
| FE | $44.33 | $21,216,406 | Utilities | large | unknown | 2026-05-09 |
| FICO | $1125.88 | $31,834,213 | Information Technology | large | unknown | 2026-05-09 |
| FLEX | $142.09 | $34,713,116 | Information Technology | mid | unknown | 2026-05-09 |
| FN | $621.00 | $39,110,049 | Information Technology | mid | unknown | 2026-05-09 |
| FSLR | $220.02 | $20,647,986 | Information Technology | large | unknown | 2026-05-09 |
| FTNT | $114.05 | $23,735,395 | Information Technology | large | unknown | 2026-05-09 |
| GD | $346.75 | $28,820,061 | Industrials | large | unknown | 2026-05-09 |
| GE | $297.10 | $100,814,728 | Industrials | large | unknown | 2026-05-09 |
| GEHC | $63.45 | $20,142,082 | Health Care | large | unknown | 2026-05-09 |
| GEV | $1040.04 | $101,195,274 | Industrials | large | unknown | 2026-05-09 |
| GILD | $131.31 | $32,191,320 | Health Care | large | unknown | 2026-05-09 |
| GLW | $186.91 | $92,724,542 | Information Technology | large | unknown | 2026-05-09 |
| GM | $78.75 | $29,853,430 | Consumer Discretionary | large | unknown | 2026-05-09 |
| GOOG | $396.89 | $150,300,142 | Communication Services | large | unknown | 2026-05-09 |
| GOOGL | $400.67 | $343,104,401 | Communication Services | large | unknown | 2026-05-09 |
| GS | $936.82 | $68,419,013 | Financials | large | unknown | 2026-05-09 |
| GWW | $1232.84 | $24,643,318 | Industrials | large | unknown | 2026-05-09 |
| HAL | $39.83 | $33,640,905 | Energy | large | unknown | 2026-05-09 |
| HCA | $434.93 | $27,335,648 | Health Care | large | unknown | 2026-05-09 |
| HD | $317.38 | $54,799,769 | Consumer Discretionary | large | unknown | 2026-05-09 |
| HIMS | $28.31 | $24,682,675 | Health Care | mid | unknown | 2026-05-09 |
| HLT | $316.76 | $36,076,093 | Consumer Discretionary | large | unknown | 2026-05-09 |
| HON | $213.07 | $31,539,436 | Industrials | large | unknown | 2026-05-09 |
| HOOD | $77.03 | $74,348,370 | Financials | large | unknown | 2026-05-09 |
| HPE | $31.33 | $30,770,293 | Information Technology | large | unknown | 2026-05-09 |
| HUBB | $492.56 | $23,714,598 | Industrials | large | unknown | 2026-05-09 |
| HUM | $274.77 | $22,187,617 | Health Care | large | unknown | 2026-05-09 |
| HWM | $270.49 | $31,192,448 | Industrials | large | unknown | 2026-05-09 |
| IBM | $229.62 | $61,698,023 | Information Technology | large | unknown | 2026-05-09 |
| ICE | $155.69 | $26,406,312 | Financials | large | unknown | 2026-05-09 |
| INTC | $124.91 | $343,987,103 | Information Technology | large | unknown | 2026-05-09 |
| INTU | $396.17 | $67,493,927 | Information Technology | large | unknown | 2026-05-09 |
| ISRG | $449.91 | $48,699,543 | Health Care | large | unknown | 2026-05-09 |
| ITW | $254.56 | $22,904,390 | Industrials | large | unknown | 2026-05-09 |
| JBL | $355.06 | $26,851,411 | Information Technology | large | unknown | 2026-05-09 |
| JCI | $139.48 | $21,108,627 | Industrials | large | unknown | 2026-05-09 |
| JNJ | $221.27 | $73,854,253 | Health Care | large | unknown | 2026-05-09 |
| JPM | $302.10 | $64,955,330 | Financials | large | unknown | 2026-05-09 |
| KDP | $28.83 | $25,212,645 | Consumer Staples | large | unknown | 2026-05-09 |
| KEYS | $360.26 | $25,041,102 | Information Technology | large | unknown | 2026-05-09 |
| KKR | $102.50 | $31,228,978 | Financials | large | unknown | 2026-05-09 |
| KLAC | $1869.11 | $116,589,251 | Information Technology | large | unknown | 2026-05-09 |
| KMI | $31.39 | $24,132,731 | Energy | large | unknown | 2026-05-09 |
| KO | $78.42 | $67,294,181 | Consumer Staples | large | unknown | 2026-05-09 |
| KVUE | $17.58 | $20,106,872 | Consumer Staples | large | unknown | 2026-05-09 |
| LHX | $299.63 | $35,933,516 | Industrials | large | unknown | 2026-05-09 |
| LIN | $492.97 | $45,192,847 | Materials | large | unknown | 2026-05-09 |
| LLY | $948.51 | $121,052,941 | Health Care | large | unknown | 2026-05-09 |
| LMT | $506.60 | $40,670,873 | Industrials | large | unknown | 2026-05-09 |
| LOW | $229.03 | $27,949,891 | Consumer Discretionary | large | unknown | 2026-05-09 |
| LRCX | $293.98 | $99,973,318 | Information Technology | large | unknown | 2026-05-09 |
| LSCC | $127.11 | $24,579,049 | Information Technology | mid | unknown | 2026-05-09 |
| LYB | $71.78 | $28,838,989 | Materials | large | unknown | 2026-05-09 |
| LYV | $163.22 | $23,780,085 | Communication Services | large | unknown | 2026-05-09 |
| MA | $495.44 | $100,016,644 | Financials | large | unknown | 2026-05-09 |
| MAR | $353.00 | $32,200,515 | Consumer Discretionary | large | unknown | 2026-05-09 |
| MCD | $275.74 | $39,573,767 | Consumer Discretionary | large | unknown | 2026-05-09 |
| MCHP | $99.17 | $49,474,970 | Information Technology | large | unknown | 2026-05-09 |
| MCK | $736.45 | $42,853,975 | Health Care | large | unknown | 2026-05-09 |
| MCO | $451.39 | $31,729,187 | Financials | large | unknown | 2026-05-09 |
| MDLZ | $61.53 | $28,762,370 | Consumer Staples | large | unknown | 2026-05-09 |
| MDT | $76.12 | $54,439,727 | Health Care | large | unknown | 2026-05-09 |
| META | $609.54 | $310,006,630 | Communication Services | large | unknown | 2026-05-09 |
| MKSI | $312.96 | $25,947,233 | Information Technology | mid | unknown | 2026-05-09 |
| MLM | $590.48 | $22,317,244 | Materials | large | unknown | 2026-05-09 |
| MMM | $143.26 | $24,284,453 | Industrials | large | unknown | 2026-05-09 |
| MO | $68.11 | $44,725,309 | Consumer Staples | large | unknown | 2026-05-09 |
| MPC | $244.97 | $27,681,476 | Energy | large | unknown | 2026-05-09 |
| MPWR | $1600.13 | $61,009,578 | Information Technology | large | unknown | 2026-05-09 |
| MRK | $111.35 | $43,795,632 | Health Care | large | unknown | 2026-05-09 |
| MRSH | $163.15 | $22,239,028 | Financials | large | unknown | 2026-05-09 |
| MS | $193.05 | $47,528,782 | Financials | large | unknown | 2026-05-09 |
| MSCI | $585.36 | $23,108,602 | Financials | large | unknown | 2026-05-09 |
| MSFT | $414.96 | $380,812,230 | Information Technology | large | unknown | 2026-05-09 |
| MSI | $383.86 | $27,429,180 | Information Technology | large | unknown | 2026-05-09 |
| MTSI | $359.47 | $21,219,509 | Information Technology | mid | unknown | 2026-05-09 |
| MTZ | $414.16 | $21,528,768 | Industrials | mid | unknown | 2026-05-09 |
| MU | $747.10 | $374,454,622 | Information Technology | large | unknown | 2026-05-09 |
| NCLH | $17.07 | $21,784,710 | Consumer Discretionary | large | unknown | 2026-05-09 |
| NEE | $93.06 | $42,387,272 | Utilities | large | unknown | 2026-05-09 |
| NEM | $116.50 | $34,732,705 | Materials | large | unknown | 2026-05-09 |
| NFLX | $87.47 | $216,846,393 | Communication Services | large | unknown | 2026-05-09 |
| NKE | $44.16 | $47,129,254 | Consumer Discretionary | large | unknown | 2026-05-09 |
| NOC | $549.27 | $25,856,905 | Industrials | large | unknown | 2026-05-09 |
| NOW | $91.11 | $96,530,543 | Information Technology | large | unknown | 2026-05-09 |
| NRG | $138.09 | $27,025,723 | Utilities | large | unknown | 2026-05-09 |
| NVDA | $215.21 | $890,290,123 | Information Technology | large | unknown | 2026-05-09 |
| NXPI | $294.68 | $47,485,667 | Information Technology | large | unknown | 2026-05-09 |
| ODFL | $198.29 | $26,303,619 | Industrials | large | unknown | 2026-05-09 |
| ON | $103.18 | $60,602,045 | Information Technology | large | unknown | 2026-05-09 |
| ORCL | $195.93 | $157,050,291 | Information Technology | large | unknown | 2026-05-09 |
| ORLY | $92.94 | $21,911,215 | Consumer Discretionary | large | unknown | 2026-05-09 |
| OXY | $53.02 | $35,139,444 | Energy | large | unknown | 2026-05-09 |
| PANW | $207.87 | $46,828,288 | Information Technology | large | unknown | 2026-05-09 |
| PCG | $16.05 | $23,434,800 | Utilities | large | unknown | 2026-05-09 |
| PEP | $154.57 | $33,933,085 | Consumer Staples | large | unknown | 2026-05-09 |
| PFE | $25.66 | $47,515,275 | Health Care | large | unknown | 2026-05-09 |
| PG | $146.38 | $50,817,161 | Consumer Staples | large | unknown | 2026-05-09 |
| PGR | $193.84 | $24,125,123 | Financials | large | unknown | 2026-05-09 |
| PH | $878.08 | $58,229,572 | Industrials | large | unknown | 2026-05-09 |
| PINS | $21.29 | $20,947,518 | Communication | mid | unknown | 2026-05-09 |
| PLD | $144.01 | $21,449,615 | Real Estate | large | unknown | 2026-05-09 |
| PLTR | $137.79 | $135,290,131 | Information Technology | large | unknown | 2026-05-09 |
| PM | $170.97 | $36,143,608 | Consumer Staples | large | unknown | 2026-05-09 |
| PNC | $216.74 | $23,595,088 | Financials | large | unknown | 2026-05-09 |
| PSX | $171.53 | $27,251,963 | Energy | large | unknown | 2026-05-09 |
| PWR | $744.84 | $53,144,630 | Industrials | large | unknown | 2026-05-09 |
| PYPL | $45.37 | $34,980,202 | Financials | large | unknown | 2026-05-09 |
| QCOM | $219.19 | $114,500,906 | Information Technology | large | unknown | 2026-05-09 |
| RCL | $275.22 | $41,010,016 | Consumer Discretionary | large | unknown | 2026-05-09 |
| REGN | $714.49 | $32,607,030 | Health Care | large | unknown | 2026-05-09 |
| ROK | $453.76 | $23,256,995 | Industrials | large | unknown | 2026-05-09 |
| ROP | $343.26 | $22,846,544 | Information Technology | large | unknown | 2026-05-09 |
| ROST | $225.74 | $20,601,628 | Consumer Discretionary | large | unknown | 2026-05-09 |
| RRX | $214.38 | $24,238,693 | Industrials | mid | unknown | 2026-05-09 |
| RSG | $199.89 | $23,469,406 | Industrials | large | unknown | 2026-05-09 |
| RTX | $176.04 | $44,386,047 | Industrials | large | unknown | 2026-05-09 |
| SBUX | $104.91 | $32,419,846 | Consumer Discretionary | large | unknown | 2026-05-09 |
| SCHW | $88.58 | $57,280,076 | Financials | large | unknown | 2026-05-09 |
| SHW | $316.78 | $30,321,503 | Materials | large | unknown | 2026-05-09 |
| SLB | $53.26 | $52,282,227 | Energy | large | unknown | 2026-05-09 |
| SMCI | $35.38 | $44,183,043 | Information Technology | large | unknown | 2026-05-09 |
| SNPS | $516.37 | $38,990,544 | Information Technology | large | unknown | 2026-05-09 |
| SO | $91.77 | $25,492,860 | Utilities | large | unknown | 2026-05-09 |
| SPGI | $419.94 | $45,939,889 | Financials | large | unknown | 2026-05-09 |
| STX | $782.53 | $113,819,267 | Information Technology | large | unknown | 2026-05-09 |
| SYK | $285.53 | $52,710,829 | Health Care | large | unknown | 2026-05-09 |
| SYY | $72.44 | $22,025,318 | Consumer Staples | large | unknown | 2026-05-09 |
| T | $25.16 | $53,603,376 | Communication Services | large | unknown | 2026-05-09 |
| TDG | $1214.53 | $38,400,124 | Industrials | large | unknown | 2026-05-09 |
| TEL | $206.16 | $47,340,036 | Information Technology | large | unknown | 2026-05-09 |
| TER | $359.81 | $63,174,986 | Information Technology | large | unknown | 2026-05-09 |
| TFC | $49.11 | $22,136,513 | Financials | large | unknown | 2026-05-09 |
| TGT | $125.23 | $28,594,442 | Consumer Staples | large | unknown | 2026-05-09 |
| TJX | $153.30 | $26,274,439 | Consumer Discretionary | large | unknown | 2026-05-09 |
| TMO | $464.99 | $78,878,430 | Health Care | large | unknown | 2026-05-09 |
| TMUS | $193.50 | $59,736,279 | Communication Services | large | unknown | 2026-05-09 |
| TSCO | $30.64 | $29,780,923 | Consumer Discretionary | large | unknown | 2026-05-09 |
| TSLA | $428.31 | $320,965,511 | Consumer Discretionary | large | unknown | 2026-05-09 |
| TT | $465.96 | $43,985,503 | Industrials | large | unknown | 2026-05-09 |
| TTD | $23.07 | $22,479,840 | Communication Services | large | unknown | 2026-05-09 |
| TWLO | $201.92 | $26,525,514 | Information Technology | mid | unknown | 2026-05-09 |
| TXN | $287.90 | $98,398,448 | Information Technology | large | unknown | 2026-05-09 |
| UAL | $99.57 | $31,609,742 | Industrials | large | unknown | 2026-05-09 |
| UBER | $75.44 | $73,671,271 | Industrials | large | unknown | 2026-05-09 |
| ULTA | $521.46 | $20,248,905 | Consumer Discretionary | large | unknown | 2026-05-09 |
| UNH | $379.79 | $104,689,486 | Health Care | large | unknown | 2026-05-09 |
| UNP | $264.54 | $45,798,682 | Industrials | large | unknown | 2026-05-09 |
| UPS | $100.75 | $25,699,571 | Industrials | large | unknown | 2026-05-09 |
| URI | $935.63 | $43,371,464 | Industrials | large | unknown | 2026-05-09 |
| USB | $55.52 | $35,225,267 | Financials | large | unknown | 2026-05-09 |
| V | $318.69 | $154,742,863 | Financials | large | unknown | 2026-05-09 |
| VLO | $240.99 | $36,778,768 | Energy | large | unknown | 2026-05-09 |
| VMC | $283.74 | $20,323,063 | Materials | large | unknown | 2026-05-09 |
| VST | $147.70 | $31,330,648 | Utilities | large | unknown | 2026-05-09 |
| VTR | $87.24 | $24,317,297 | Real Estate | large | unknown | 2026-05-09 |
| VZ | $47.23 | $57,362,098 | Communication Services | large | unknown | 2026-05-09 |
| WAT | $355.30 | $32,237,391 | Health Care | large | unknown | 2026-05-09 |
| WBD | $27.09 | $28,292,742 | Communication Services | large | unknown | 2026-05-09 |
| WDAY | $127.81 | $29,489,683 | Information Technology | large | unknown | 2026-05-09 |
| WDC | $480.01 | $109,409,292 | Information Technology | large | unknown | 2026-05-09 |
| WELL | $214.60 | $27,755,269 | Real Estate | large | unknown | 2026-05-09 |
| WFC | $75.64 | $83,030,359 | Financials | large | unknown | 2026-05-09 |
| WM | $215.29 | $24,266,843 | Industrials | large | unknown | 2026-05-09 |
| WMB | $71.93 | $27,869,355 | Energy | large | unknown | 2026-05-09 |
| WMT | $130.40 | $65,383,770 | Consumer Staples | large | unknown | 2026-05-09 |
| WST | $325.96 | $20,437,836 | Health Care | large | unknown | 2026-05-09 |
| WWD | $369.86 | $21,319,233 | Industrials | mid | unknown | 2026-05-09 |
| XEL | $79.36 | $24,270,317 | Utilities | large | unknown | 2026-05-09 |
| XOM | $144.38 | $86,561,628 | Energy | large | unknown | 2026-05-09 |
| XPO | $204.28 | $22,555,502 | Industrials | mid | unknown | 2026-05-09 |
| ZTS | $82.81 | $28,600,549 | Health Care | large | unknown | 2026-05-09 |
