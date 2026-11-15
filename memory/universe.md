---
screened_on: 2026-11-15
expires_on: 2026-11-22
total_passed: 331
total_rejected: 1164
universe_scope: S&P 1500 (S&P 500 + S&P 400 + S&P 600)
source_500: https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv
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
| A | $173.91 | $23,812,484 | Health Care | large | unknown | 2026-11-15 |
| AAL | $13.16 | $32,422,469 | Industrials | mid | unknown | 2026-11-15 |
| AAPL | $356.40 | $476,670,919 | Information Technology | large | unknown | 2026-11-15 |
| ABBV | $295.00 | $65,338,542 | Health Care | large | unknown | 2026-11-15 |
| ABNB | $186.73 | $40,325,545 | Consumer Discretionary | large | unknown | 2026-11-15 |
| ABT | $108.51 | $59,501,304 | Health Care | large | unknown | 2026-11-15 |
| ACN | $250.44 | $72,395,762 | Information Technology | large | unknown | 2026-11-15 |
| ADBE | $243.03 | $38,409,322 | Information Technology | large | unknown | 2026-11-15 |
| ADI | $397.76 | $73,531,055 | Information Technology | large | unknown | 2026-11-15 |
| ADP | $309.93 | $29,214,410 | Industrials | large | unknown | 2026-11-15 |
| ADSK | $264.45 | $29,191,447 | Information Technology | large | unknown | 2026-11-15 |
| AEP | $129.17 | $22,398,538 | Utilities | large | unknown | 2026-11-15 |
| AIG | $82.86 | $26,532,407 | Financials | large | unknown | 2026-11-15 |
| AJG | $282.82 | $33,193,662 | Financials | large | unknown | 2026-11-15 |
| AKAM | $85.35 | $28,379,770 | Information Technology | large | unknown | 2026-11-15 |
| ALL | $267.82 | $26,279,355 | Financials | large | unknown | 2026-11-15 |
| AMAT | $370.37 | $120,691,914 | Information Technology | large | unknown | 2026-11-15 |
| AMD | $534.15 | $490,447,371 | Information Technology | large | unknown | 2026-11-15 |
| AME | $242.03 | $24,476,627 | Industrials | large | unknown | 2026-11-15 |
| AMGN | $465.55 | $43,075,222 | Health Care | large | unknown | 2026-11-15 |
| AMT | $191.62 | $29,966,283 | Real Estate | large | unknown | 2026-11-15 |
| AMZN | $266.58 | $502,863,789 | Consumer Discretionary | large | unknown | 2026-11-15 |
| ANET | $197.34 | $87,949,794 | Information Technology | large | unknown | 2026-11-15 |
| AON | $338.25 | $28,153,475 | Financials | large | unknown | 2026-11-15 |
| APH | $78.22 | $75,773,718 | Information Technology | large | unknown | 2026-11-15 |
| APO | $123.50 | $24,535,060 | Financials | large | unknown | 2026-11-15 |
| APP | $409.00 | $74,513,477 | Information Technology | large | unknown | 2026-11-15 |
| ATI | $183.16 | $24,021,725 | Industrials | mid | unknown | 2026-11-15 |
| AVGO | $346.71 | $310,549,791 | Information Technology | large | unknown | 2026-11-15 |
| AWK | $149.59 | $24,515,260 | Utilities | large | unknown | 2026-11-15 |
| AXON | $315.38 | $28,778,171 | Industrials | large | unknown | 2026-11-15 |
| AXP | $320.51 | $45,434,599 | Financials | large | unknown | 2026-11-15 |
| AZO | $3259.16 | $34,081,474 | Consumer Discretionary | large | unknown | 2026-11-15 |
| BA | $171.52 | $80,627,293 | Industrials | large | unknown | 2026-11-15 |
| BAC | $51.01 | $124,086,464 | Financials | large | unknown | 2026-11-15 |
| BDX | $218.05 | $24,548,333 | Health Care | large | unknown | 2026-11-15 |
| BKNG | $159.52 | $68,023,915 | Consumer Discretionary | large | unknown | 2026-11-15 |
| BKR | $49.44 | $29,331,357 | Energy | large | unknown | 2026-11-15 |
| BLK | $1222.75 | $48,887,692 | Financials | large | unknown | 2026-11-15 |
| BMY | $63.42 | $33,167,404 | Health Care | large | unknown | 2026-11-15 |
| BRK.B | $592.86 | $97,818,624 | Financials | large | unknown | 2026-11-15 |
| BSX | $44.35 | $83,376,301 | Health Care | large | unknown | 2026-11-15 |
| BURL | $242.86 | $24,492,010 | Consumer Discretionary | mid | unknown | 2026-11-15 |
| BX | $120.17 | $32,669,721 | Financials | large | unknown | 2026-11-15 |
| C | $124.03 | $42,467,060 | Financials | large | unknown | 2026-11-15 |
| CAH | $281.10 | $23,652,648 | Health Care | large | unknown | 2026-11-15 |
| CARR | $54.22 | $21,902,731 | Industrials | large | unknown | 2026-11-15 |
| CART | $58.89 | $28,860,566 | Consumer Staples | mid | unknown | 2026-11-15 |
| CAT | $600.18 | $119,804,288 | Industrials | large | unknown | 2026-11-15 |
| CB | $375.67 | $30,618,843 | Financials | large | unknown | 2026-11-15 |
| CBOE | $375.80 | $24,477,004 | Financials | large | unknown | 2026-11-15 |
| CCI | $90.84 | $28,086,074 | Real Estate | large | unknown | 2026-11-15 |
| CCL | $29.23 | $36,670,834 | Consumer Discretionary | large | unknown | 2026-11-15 |
| CDE | $13.97 | $21,760,164 | Materials | mid | unknown | 2026-11-15 |
| CDNS | $322.90 | $42,040,020 | Information Technology | large | unknown | 2026-11-15 |
| CEG | $280.11 | $47,225,100 | Utilities | large | unknown | 2026-11-15 |
| CI | $297.01 | $25,568,731 | Health Care | large | unknown | 2026-11-15 |
| CIEN | $280.57 | $56,784,592 | Information Technology | large | unknown | 2026-11-15 |
| CL | $99.68 | $26,893,372 | Consumer Staples | large | unknown | 2026-11-15 |
| CMCSA | $25.19 | $51,427,173 | Communication Services | large | unknown | 2026-11-15 |
| CME | $317.92 | $30,584,294 | Financials | large | unknown | 2026-11-15 |
| CMG | $35.30 | $46,897,668 | Consumer Discretionary | large | unknown | 2026-11-15 |
| CMI | $452.11 | $42,646,827 | Industrials | large | unknown | 2026-11-15 |
| CMS | $70.37 | $21,216,253 | Utilities | large | unknown | 2026-11-15 |
| CNC | $71.28 | $26,019,405 | Health Care | large | unknown | 2026-11-15 |
| CNP | $41.20 | $33,612,583 | Utilities | large | unknown | 2026-11-15 |
| COF | $195.13 | $44,825,300 | Financials | large | unknown | 2026-11-15 |
| COHR | $218.10 | $95,223,193 | Information Technology | large | unknown | 2026-11-15 |
| COIN | $127.59 | $40,012,369 | Financials | large | unknown | 2026-11-15 |
| COP | $142.35 | $45,550,866 | Energy | large | unknown | 2026-11-15 |
| COR | $359.02 | $29,134,716 | Health Care | large | unknown | 2026-11-15 |
| COST | $1106.43 | $101,458,621 | Consumer Staples | large | unknown | 2026-11-15 |
| CPRT | $31.85 | $26,897,215 | Industrials | large | unknown | 2026-11-15 |
| CRH | $93.15 | $27,036,059 | Materials | large | unknown | 2026-11-15 |
| CRL | $338.01 | $32,241,956 | Health Care | large | unknown | 2026-11-15 |
| CRM | $217.86 | $74,263,708 | Information Technology | large | unknown | 2026-11-15 |
| CRS | $291.40 | $27,255,424 | Industrials | mid | unknown | 2026-11-15 |
| CRWD | $226.61 | $80,628,648 | Information Technology | large | unknown | 2026-11-15 |
| CSCO | $95.64 | $80,887,674 | Information Technology | large | unknown | 2026-11-15 |
| CSX | $52.06 | $50,137,928 | Industrials | large | unknown | 2026-11-15 |
| CTAS | $226.22 | $21,576,714 | Industrials | large | unknown | 2026-11-15 |
| CTSH | $63.04 | $23,708,107 | Information Technology | large | unknown | 2026-11-15 |
| CVNA | $72.35 | $41,145,051 | Consumer Discretionary | large | unknown | 2026-11-15 |
| CVS | $89.35 | $56,044,981 | Health Care | large | unknown | 2026-11-15 |
| CVX | $219.85 | $60,816,399 | Energy | large | unknown | 2026-11-15 |
| D | $67.66 | $26,897,263 | Utilities | large | unknown | 2026-11-15 |
| DAL | $86.25 | $28,771,127 | Industrials | large | unknown | 2026-11-15 |
| DASH | $171.44 | $66,120,828 | Consumer Discretionary | large | unknown | 2026-11-15 |
| DDOG | $184.12 | $50,333,322 | Information Technology | large | unknown | 2026-11-15 |
| DE | $673.53 | $43,094,725 | Industrials | large | unknown | 2026-11-15 |
| DELL | $344.32 | $121,610,992 | Information Technology | large | unknown | 2026-11-15 |
| DHI | $145.56 | $23,553,667 | Consumer Discretionary | large | unknown | 2026-11-15 |
| DHR | $232.99 | $59,427,473 | Health Care | large | unknown | 2026-11-15 |
| DIS | $118.98 | $43,474,896 | Communication Services | large | unknown | 2026-11-15 |
| DLR | $179.93 | $31,763,143 | Real Estate | large | unknown | 2026-11-15 |
| DOCN | $86.30 | $21,746,102 | Information Technology | mid | unknown | 2026-11-15 |
| DOW | $33.05 | $20,632,877 | Materials | large | unknown | 2026-11-15 |
| DT | $44.79 | $28,869,619 | Information Technology | mid | unknown | 2026-11-15 |
| DUK | $129.12 | $29,272,802 | Utilities | large | unknown | 2026-11-15 |
| DVN | $46.60 | $43,830,118 | Energy | large | unknown | 2026-11-15 |
| DXCM | $83.28 | $22,894,793 | Health Care | large | unknown | 2026-11-15 |
| EAT | $198.46 | $23,159,050 | Consumer Discretionary | mid | unknown | 2026-11-15 |
| EBAY | $120.98 | $27,697,918 | Consumer Discretionary | large | unknown | 2026-11-15 |
| ECL | $309.14 | $30,217,878 | Materials | large | unknown | 2026-11-15 |
| EFX | $188.19 | $22,554,974 | Industrials | large | unknown | 2026-11-15 |
| EL | $111.68 | $26,705,357 | Consumer Staples | large | unknown | 2026-11-15 |
| ELV | $429.63 | $35,057,589 | Health Care | large | unknown | 2026-11-15 |
| EME | $659.47 | $21,017,068 | Industrials | large | unknown | 2026-11-15 |
| EMR | $166.42 | $24,343,205 | Industrials | large | unknown | 2026-11-15 |
| ENTG | $147.41 | $24,398,364 | Information Technology | mid | unknown | 2026-11-15 |
| EOG | $158.28 | $28,528,624 | Energy | large | unknown | 2026-11-15 |
| EQIX | $1053.38 | $47,980,071 | Real Estate | large | unknown | 2026-11-15 |
| EQT | $52.83 | $43,285,811 | Energy | large | unknown | 2026-11-15 |
| ETN | $352.94 | $73,214,611 | Industrials | large | unknown | 2026-11-15 |
| EW | $107.19 | $31,038,350 | Health Care | large | unknown | 2026-11-15 |
| EXC | $46.26 | $29,088,768 | Utilities | large | unknown | 2026-11-15 |
| EXPE | $257.91 | $33,938,548 | Consumer Discretionary | large | unknown | 2026-11-15 |
| F | $11.91 | $24,677,138 | Consumer Discretionary | large | unknown | 2026-11-15 |
| FAST | $55.22 | $21,523,706 | Industrials | large | unknown | 2026-11-15 |
| FCX | $59.26 | $45,580,894 | Materials | large | unknown | 2026-11-15 |
| FDX | $324.22 | $36,486,067 | Industrials | large | unknown | 2026-11-15 |
| FFIV | $308.98 | $21,783,668 | Information Technology | large | unknown | 2026-11-15 |
| FICO | $719.77 | $29,679,431 | Information Technology | large | unknown | 2026-11-15 |
| FIS | $29.54 | $23,259,943 | Financials | large | unknown | 2026-11-15 |
| FISV | $63.78 | $36,241,297 | Financials | large | unknown | 2026-11-15 |
| FITB | $54.51 | $35,114,510 | Financials | large | unknown | 2026-11-15 |
| FIX | $1111.88 | $61,365,375 | Industrials | large | unknown | 2026-11-15 |
| FN | $327.46 | $30,514,878 | Information Technology | mid | unknown | 2026-11-15 |
| FOXA | $68.44 | $28,868,941 | Communication Services | large | unknown | 2026-11-15 |
| FSLR | $171.48 | $24,945,220 | Information Technology | large | unknown | 2026-11-15 |
| FTNT | $127.12 | $36,119,459 | Information Technology | large | unknown | 2026-11-15 |
| GD | $363.44 | $21,960,602 | Industrials | large | unknown | 2026-11-15 |
| GE | $331.81 | $92,550,513 | Industrials | large | unknown | 2026-11-15 |
| GEV | $802.58 | $170,744,576 | Industrials | large | unknown | 2026-11-15 |
| GILD | $168.04 | $51,088,170 | Health Care | large | unknown | 2026-11-15 |
| GKOS | $245.68 | $22,403,121 | Health Care | mid | unknown | 2026-11-15 |
| GLW | $114.05 | $72,417,682 | Information Technology | large | unknown | 2026-11-15 |
| GM | $86.04 | $34,731,550 | Consumer Discretionary | large | unknown | 2026-11-15 |
| GOOG | $292.50 | $243,741,730 | Communication Services | large | unknown | 2026-11-15 |
| GOOGL | $295.81 | $427,839,513 | Communication Services | large | unknown | 2026-11-15 |
| GPN | $91.94 | $21,439,031 | Financials | large | unknown | 2026-11-15 |
| GS | $916.16 | $76,474,662 | Financials | large | unknown | 2026-11-15 |
| GWW | $1489.57 | $26,021,133 | Industrials | large | unknown | 2026-11-15 |
| HAL | $33.78 | $27,074,535 | Energy | large | unknown | 2026-11-15 |
| HCA | $498.88 | $40,774,995 | Health Care | large | unknown | 2026-11-15 |
| HD | $348.71 | $68,126,762 | Consumer Discretionary | large | unknown | 2026-11-15 |
| HLT | $373.12 | $54,290,554 | Consumer Discretionary | large | unknown | 2026-11-15 |
| HON | $222.46 | $23,194,697 | Industrials | large | unknown | 2026-11-15 |
| HOOD | $77.87 | $54,355,742 | Financials | large | unknown | 2026-11-15 |
| HPE | $48.29 | $48,997,817 | Information Technology | large | unknown | 2026-11-15 |
| HPQ | $29.36 | $31,641,981 | Information Technology | large | unknown | 2026-11-15 |
| HSY | $174.20 | $20,771,036 | Consumer Staples | large | unknown | 2026-11-15 |
| HUBB | $436.98 | $24,588,854 | Industrials | large | unknown | 2026-11-15 |
| HUM | $450.47 | $43,092,234 | Health Care | large | unknown | 2026-11-15 |
| HWM | $220.90 | $58,836,285 | Industrials | large | unknown | 2026-11-15 |
| IBKR | $81.75 | $24,755,796 | Financials | large | unknown | 2026-11-15 |
| IBM | $247.01 | $49,225,587 | Information Technology | large | unknown | 2026-11-15 |
| ICE | $178.48 | $35,720,541 | Financials | large | unknown | 2026-11-15 |
| IDXX | $704.46 | $25,257,829 | Health Care | large | unknown | 2026-11-15 |
| INTC | $59.66 | $310,698,165 | Information Technology | large | unknown | 2026-11-15 |
| INTU | $341.63 | $50,442,002 | Information Technology | large | unknown | 2026-11-15 |
| IQV | $265.03 | $26,871,330 | Health Care | large | unknown | 2026-11-15 |
| IR | $85.08 | $21,089,660 | Industrials | large | unknown | 2026-11-15 |
| ISRG | $443.47 | $64,869,009 | Health Care | large | unknown | 2026-11-15 |
| ITW | $287.44 | $21,417,914 | Industrials | large | unknown | 2026-11-15 |
| JBL | $254.13 | $20,088,323 | Information Technology | large | unknown | 2026-11-15 |
| JCI | $139.33 | $47,627,788 | Industrials | large | unknown | 2026-11-15 |
| JHX | $27.81 | $27,043,702 | Materials | mid | unknown | 2026-11-15 |
| JNJ | $285.96 | $82,157,664 | Health Care | large | unknown | 2026-11-15 |
| JPM | $346.26 | $70,426,543 | Financials | large | unknown | 2026-11-15 |
| KDP | $36.35 | $63,220,125 | Consumer Staples | large | unknown | 2026-11-15 |
| KEYS | $297.69 | $26,721,047 | Information Technology | large | unknown | 2026-11-15 |
| KHC | $25.11 | $21,996,724 | Consumer Staples | large | unknown | 2026-11-15 |
| KKR | $98.05 | $20,973,144 | Financials | large | unknown | 2026-11-15 |
| KLAC | $152.29 | $88,773,224 | Information Technology | large | unknown | 2026-11-15 |
| KMB | $109.44 | $34,165,656 | Consumer Staples | large | unknown | 2026-11-15 |
| KMI | $31.93 | $38,672,817 | Energy | large | unknown | 2026-11-15 |
| KO | $99.25 | $108,774,429 | Consumer Staples | large | unknown | 2026-11-15 |
| KR | $70.82 | $27,239,663 | Consumer Staples | large | unknown | 2026-11-15 |
| LHX | $272.44 | $26,286,975 | Industrials | large | unknown | 2026-11-15 |
| LIN | $525.98 | $48,452,531 | Materials | large | unknown | 2026-11-15 |
| LITE | $596.67 | $189,179,559 | Information Technology | large | unknown | 2026-11-15 |
| LLY | $1444.80 | $183,428,564 | Health Care | large | unknown | 2026-11-15 |
| LMT | $596.11 | $44,966,855 | Industrials | large | unknown | 2026-11-15 |
| LOW | $227.78 | $34,399,938 | Consumer Discretionary | large | unknown | 2026-11-15 |
| LRCX | $226.05 | $124,104,544 | Information Technology | large | unknown | 2026-11-15 |
| LYV | $178.38 | $24,289,022 | Communication Services | large | unknown | 2026-11-15 |
| MA | $661.16 | $136,474,988 | Financials | large | unknown | 2026-11-15 |
| MAR | $423.19 | $38,769,584 | Consumer Discretionary | large | unknown | 2026-11-15 |
| MCD | $271.99 | $61,241,248 | Consumer Discretionary | large | unknown | 2026-11-15 |
| MCHP | $61.67 | $44,973,957 | Information Technology | large | unknown | 2026-11-15 |
| MCK | $1103.90 | $45,438,018 | Health Care | large | unknown | 2026-11-15 |
| MCO | $508.03 | $27,930,140 | Financials | large | unknown | 2026-11-15 |
| MDLZ | $67.54 | $35,702,412 | Consumer Staples | large | unknown | 2026-11-15 |
| MDT | $102.86 | $42,350,376 | Health Care | large | unknown | 2026-11-15 |
| META | $641.90 | $561,641,834 | Communication Services | large | unknown | 2026-11-15 |
| MKSI | $215.65 | $22,046,326 | Information Technology | mid | unknown | 2026-11-15 |
| MLM | $513.20 | $31,976,966 | Materials | large | unknown | 2026-11-15 |
| MMM | $183.64 | $36,261,486 | Industrials | large | unknown | 2026-11-15 |
| MNST | $46.48 | $27,951,577 | Consumer Staples | large | unknown | 2026-11-15 |
| MO | $78.63 | $31,021,620 | Consumer Staples | large | unknown | 2026-11-15 |
| MPC | $414.70 | $52,778,701 | Energy | large | unknown | 2026-11-15 |
| MPWR | $1389.41 | $64,378,689 | Information Technology | large | unknown | 2026-11-15 |
| MRK | $147.76 | $69,268,403 | Health Care | large | unknown | 2026-11-15 |
| MRNA | $223.22 | $102,811,100 | Health Care | large | unknown | 2026-11-15 |
| MRSH | $207.66 | $25,362,347 | Financials | large | unknown | 2026-11-15 |
| MS | $190.65 | $70,506,574 | Financials | large | unknown | 2026-11-15 |
| MSCI | $658.28 | $24,908,202 | Financials | large | unknown | 2026-11-15 |
| MSFT | $524.19 | $459,643,164 | Information Technology | large | unknown | 2026-11-15 |
| MSI | $531.25 | $35,364,978 | Information Technology | large | unknown | 2026-11-15 |
| MTD | $1739.52 | $23,012,252 | Health Care | large | unknown | 2026-11-15 |
| MTSI | $231.89 | $22,688,101 | Information Technology | mid | unknown | 2026-11-15 |
| MTZ | $183.01 | $23,289,853 | Industrials | mid | unknown | 2026-11-15 |
| MU | $778.11 | $646,736,929 | Information Technology | large | unknown | 2026-11-15 |
| NCLH | $17.97 | $23,000,036 | Consumer Discretionary | large | unknown | 2026-11-15 |
| NDAQ | $108.47 | $22,045,180 | Financials | large | unknown | 2026-11-15 |
| NEE | $85.15 | $86,874,713 | Utilities | large | unknown | 2026-11-15 |
| NEM | $113.16 | $35,937,609 | Materials | large | unknown | 2026-11-15 |
| NFLX | $62.15 | $156,387,639 | Communication Services | large | unknown | 2026-11-15 |
| NI | $46.06 | $21,201,048 | Utilities | large | unknown | 2026-11-15 |
| NKE | $37.99 | $45,976,129 | Consumer Discretionary | large | unknown | 2026-11-15 |
| NOC | $550.54 | $34,074,820 | Industrials | large | unknown | 2026-11-15 |
| NOW | $102.26 | $121,007,360 | Information Technology | large | unknown | 2026-11-15 |
| NUE | $251.74 | $21,276,518 | Materials | large | unknown | 2026-11-15 |
| NVDA | $162.84 | $1,381,148,461 | Information Technology | large | unknown | 2026-11-15 |
| NVT | $114.63 | $25,135,828 | Industrials | mid | unknown | 2026-11-15 |
| NXPI | $264.99 | $64,394,595 | Information Technology | large | unknown | 2026-11-15 |
| O | $58.83 | $24,499,031 | Real Estate | large | unknown | 2026-11-15 |
| ODFL | $174.56 | $23,023,644 | Industrials | large | unknown | 2026-11-15 |
| ON | $71.02 | $31,601,800 | Information Technology | large | unknown | 2026-11-15 |
| ORCL | $125.37 | $195,266,487 | Information Technology | large | unknown | 2026-11-15 |
| ORLY | $92.19 | $25,559,628 | Consumer Discretionary | large | unknown | 2026-11-15 |
| OTIS | $77.50 | $24,513,832 | Industrials | large | unknown | 2026-11-15 |
| OXY | $58.75 | $50,397,648 | Energy | large | unknown | 2026-11-15 |
| PANW | $322.09 | $93,564,422 | Information Technology | large | unknown | 2026-11-15 |
| PCG | $13.25 | $22,207,758 | Utilities | large | unknown | 2026-11-15 |
| PEP | $145.48 | $54,408,365 | Consumer Staples | large | unknown | 2026-11-15 |
| PFE | $28.90 | $58,957,109 | Health Care | large | unknown | 2026-11-15 |
| PG | $169.83 | $80,189,259 | Consumer Staples | large | unknown | 2026-11-15 |
| PGR | $235.74 | $30,573,360 | Financials | large | unknown | 2026-11-15 |
| PH | $955.54 | $46,214,959 | Industrials | large | unknown | 2026-11-15 |
| PINS | $19.16 | $20,152,636 | Communication Services | mid | unknown | 2026-11-15 |
| PLD | $128.72 | $20,642,287 | Real Estate | large | unknown | 2026-11-15 |
| PLTR | $168.05 | $116,224,397 | Information Technology | large | unknown | 2026-11-15 |
| PM | $198.92 | $50,161,215 | Consumer Staples | large | unknown | 2026-11-15 |
| PNC | $232.33 | $21,345,289 | Financials | large | unknown | 2026-11-15 |
| PPL | $35.67 | $24,391,104 | Utilities | large | unknown | 2026-11-15 |
| PSX | $264.87 | $50,749,832 | Energy | large | unknown | 2026-11-15 |
| PTC | $196.04 | $20,172,109 | Information Technology | large | unknown | 2026-11-15 |
| PWR | $602.10 | $67,014,590 | Industrials | large | unknown | 2026-11-15 |
| PYPL | $59.27 | $28,401,330 | Financials | large | unknown | 2026-11-15 |
| QCOM | $172.42 | $79,680,040 | Information Technology | large | unknown | 2026-11-15 |
| RCL | $323.23 | $42,803,489 | Consumer Discretionary | large | unknown | 2026-11-15 |
| REGN | $955.65 | $45,934,556 | Health Care | large | unknown | 2026-11-15 |
| RMD | $239.53 | $23,406,728 | Health Care | large | unknown | 2026-11-15 |
| ROIV | $39.52 | $23,279,573 | Health Care | mid | unknown | 2026-11-15 |
| ROK | $402.64 | $30,199,186 | Industrials | large | unknown | 2026-11-15 |
| ROP | $479.87 | $29,748,500 | Information Technology | large | unknown | 2026-11-15 |
| ROST | $231.67 | $24,310,460 | Consumer Discretionary | large | unknown | 2026-11-15 |
| RRC | $51.82 | $26,018,225 | Energy | mid | unknown | 2026-11-15 |
| RTX | $198.65 | $53,920,597 | Industrials | large | unknown | 2026-11-15 |
| RVTY | $154.54 | $20,722,758 | Health Care | large | unknown | 2026-11-15 |
| SBUX | $106.47 | $37,829,812 | Consumer Discretionary | large | unknown | 2026-11-15 |
| SCHW | $92.95 | $43,285,431 | Financials | large | unknown | 2026-11-15 |
| SHW | $349.90 | $35,347,581 | Materials | large | unknown | 2026-11-15 |
| SITM | $444.00 | $22,731,283 | Information Technology | mid | unknown | 2026-11-15 |
| SLB | $51.67 | $49,492,701 | Energy | large | unknown | 2026-11-15 |
| SMCI | $26.86 | $56,476,400 | Information Technology | large | unknown | 2026-11-15 |
| SMTC | $114.55 | $24,402,385 | Information Technology | mid | unknown | 2026-11-15 |
| SN | $226.15 | $22,196,038 | Consumer Discretionary | mid | unknown | 2026-11-15 |
| SNDK | $884.88 | $281,509,304 | Information Technology | large | unknown | 2026-11-15 |
| SNPS | $455.14 | $49,618,925 | Information Technology | large | unknown | 2026-11-15 |
| SO | $93.61 | $41,133,105 | Utilities | large | unknown | 2026-11-15 |
| SPGI | $473.60 | $46,191,074 | Financials | large | unknown | 2026-11-15 |
| SRE | $79.57 | $20,482,943 | Utilities | large | unknown | 2026-11-15 |
| STRL | $292.16 | $24,545,626 | Industrials | mid | unknown | 2026-11-15 |
| STX | $528.12 | $163,019,808 | Information Technology | large | unknown | 2026-11-15 |
| SWKS | $90.00 | $20,896,061 | Information Technology | large | unknown | 2026-11-15 |
| SYF | $72.26 | $22,844,550 | Financials | large | unknown | 2026-11-15 |
| SYK | $309.64 | $63,302,403 | Health Care | large | unknown | 2026-11-15 |
| T | $22.19 | $66,678,440 | Communication Services | large | unknown | 2026-11-15 |
| TDG | $1217.50 | $66,922,157 | Industrials | large | unknown | 2026-11-15 |
| TEL | $216.44 | $27,254,198 | Information Technology | large | unknown | 2026-11-15 |
| TER | $249.48 | $54,554,947 | Information Technology | large | unknown | 2026-11-15 |
| TFC | $49.98 | $29,851,203 | Financials | large | unknown | 2026-11-15 |
| TGT | $161.44 | $27,612,669 | Consumer Staples | large | unknown | 2026-11-15 |
| TJX | $134.33 | $36,746,199 | Consumer Discretionary | large | unknown | 2026-11-15 |
| TLN | $376.12 | $26,120,428 | Utilities | mid | unknown | 2026-11-15 |
| TMO | $700.18 | $99,162,736 | Health Care | large | unknown | 2026-11-15 |
| TMUS | $169.97 | $51,343,144 | Communication Services | large | unknown | 2026-11-15 |
| TOST | $34.68 | $24,259,881 | Financials | mid | unknown | 2026-11-15 |
| TPR | $132.43 | $20,532,697 | Consumer Discretionary | large | unknown | 2026-11-15 |
| TRGP | $297.25 | $26,319,570 | Energy | large | unknown | 2026-11-15 |
| TRV | $403.07 | $27,274,203 | Financials | large | unknown | 2026-11-15 |
| TSCO | $36.45 | $31,397,296 | Consumer Discretionary | large | unknown | 2026-11-15 |
| TSLA | $390.24 | $367,808,598 | Consumer Discretionary | large | unknown | 2026-11-15 |
| TT | $418.08 | $49,272,791 | Industrials | large | unknown | 2026-11-15 |
| TTMI | $74.08 | $25,194,967 | Information Technology | mid | unknown | 2026-11-15 |
| TTWO | $227.81 | $29,846,602 | Communication Services | large | unknown | 2026-11-15 |
| TXN | $303.59 | $104,796,151 | Information Technology | large | unknown | 2026-11-15 |
| TYL | $424.01 | $23,981,559 | Information Technology | large | unknown | 2026-11-15 |
| UAL | $109.23 | $33,263,803 | Industrials | large | unknown | 2026-11-15 |
| UBER | $69.67 | $72,103,804 | Industrials | large | unknown | 2026-11-15 |
| UNH | $407.52 | $106,725,451 | Health Care | large | unknown | 2026-11-15 |
| UNP | $302.54 | $41,496,067 | Industrials | large | unknown | 2026-11-15 |
| UPS | $112.40 | $28,957,519 | Industrials | large | unknown | 2026-11-15 |
| URI | $1124.30 | $43,881,297 | Industrials | large | unknown | 2026-11-15 |
| USB | $61.00 | $29,911,593 | Financials | large | unknown | 2026-11-15 |
| UTHR | $590.62 | $20,042,315 | Health Care | mid | unknown | 2026-11-15 |
| V | $425.73 | $173,497,674 | Financials | large | unknown | 2026-11-15 |
| VEEV | $301.68 | $23,747,240 | Health Care | large | unknown | 2026-11-15 |
| VLO | $379.78 | $64,665,830 | Energy | large | unknown | 2026-11-15 |
| VMC | $278.56 | $20,586,288 | Materials | large | unknown | 2026-11-15 |
| VRT | $202.08 | $99,162,876 | Industrials | large | unknown | 2026-11-15 |
| VRTX | $538.54 | $46,915,297 | Health Care | large | unknown | 2026-11-15 |
| VST | $132.94 | $42,895,665 | Utilities | large | unknown | 2026-11-15 |
| VZ | $46.37 | $68,025,459 | Communication Services | large | unknown | 2026-11-15 |
| WAT | $460.58 | $34,206,232 | Health Care | large | unknown | 2026-11-15 |
| WCC | $321.74 | $21,835,838 | Industrials | mid | unknown | 2026-11-15 |
| WDAY | $196.50 | $20,094,306 | Information Technology | large | unknown | 2026-11-15 |
| WDC | $295.50 | $115,968,734 | Information Technology | large | unknown | 2026-11-15 |
| WEC | $117.61 | $20,831,608 | Utilities | large | unknown | 2026-11-15 |
| WELL | $244.49 | $45,517,291 | Real Estate | large | unknown | 2026-11-15 |
| WFC | $86.05 | $64,903,558 | Financials | large | unknown | 2026-11-15 |
| WM | $243.89 | $29,944,288 | Industrials | large | unknown | 2026-11-15 |
| WMB | $69.12 | $41,945,268 | Energy | large | unknown | 2026-11-15 |
| WMT | $128.12 | $114,271,474 | Consumer Staples | large | unknown | 2026-11-15 |
| XEL | $81.62 | $39,973,846 | Utilities | large | unknown | 2026-11-15 |
| XOM | $170.61 | $91,400,864 | Energy | large | unknown | 2026-11-15 |
| XYZ | $84.58 | $26,691,341 | Financials | large | unknown | 2026-11-15 |
| YUM | $161.29 | $22,845,006 | Consumer Discretionary | large | unknown | 2026-11-15 |
