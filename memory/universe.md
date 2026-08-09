---
screened_on: 2026-08-09
expires_on: 2026-08-16
total_passed: 302
total_rejected: 1198
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
| AAL | $15.94 | $43,092,224 | Industrials | mid | unknown | 2026-08-09 |
| AAPL | $313.29 | $635,207,422 | Information Technology | large | unknown | 2026-08-09 |
| ABBV | $245.96 | $70,459,136 | Health Care | large | unknown | 2026-08-09 |
| ABNB | $178.19 | $28,842,300 | Consumer Discretionary | large | unknown | 2026-08-09 |
| ABT | $107.81 | $72,914,121 | Health Care | large | unknown | 2026-08-09 |
| ACN | $175.72 | $60,061,960 | Information Technology | large | unknown | 2026-08-09 |
| ADBE | $265.17 | $59,391,745 | Information Technology | large | unknown | 2026-08-09 |
| ADI | $389.87 | $57,998,313 | Information Technology | large | unknown | 2026-08-09 |
| ADP | $271.29 | $31,187,810 | Industrials | large | unknown | 2026-08-09 |
| ADSK | $249.12 | $25,178,953 | Information Technology | large | unknown | 2026-08-09 |
| AEP | $125.73 | $25,087,434 | Utilities | large | unknown | 2026-08-09 |
| AKAM | $110.55 | $23,947,528 | Information Technology | large | unknown | 2026-08-09 |
| AMAT | $538.68 | $190,249,767 | Information Technology | large | unknown | 2026-08-09 |
| AMD | $483.27 | $396,560,203 | Information Technology | large | unknown | 2026-08-09 |
| AMGN | $410.93 | $35,714,597 | Health Care | large | unknown | 2026-08-09 |
| AMT | $172.38 | $29,126,463 | Real Estate | large | unknown | 2026-08-09 |
| AMZN | $274.37 | $587,811,439 | Consumer Discretionary | large | unknown | 2026-08-09 |
| ANET | $188.64 | $81,414,336 | Information Technology | large | unknown | 2026-08-09 |
| AON | $358.21 | $25,197,167 | Financials | large | unknown | 2026-08-09 |
| APH | $169.26 | $59,850,725 | Information Technology | large | unknown | 2026-08-09 |
| APO | $127.50 | $25,052,802 | Financials | large | unknown | 2026-08-09 |
| APP | $346.64 | $97,684,454 | Information Technology | large | unknown | 2026-08-09 |
| ATI | $228.02 | $20,791,727 | Industrials | mid | unknown | 2026-08-09 |
| AVGO | $427.57 | $223,454,433 | Information Technology | large | unknown | 2026-08-09 |
| AXON | $571.76 | $23,315,781 | Industrials | large | unknown | 2026-08-09 |
| AXP | $340.98 | $46,819,327 | Financials | large | unknown | 2026-08-09 |
| AZO | $3129.05 | $32,740,026 | Consumer Discretionary | large | unknown | 2026-08-09 |
| BA | $234.52 | $62,003,919 | Industrials | large | unknown | 2026-08-09 |
| BAC | $63.15 | $148,963,351 | Financials | large | unknown | 2026-08-09 |
| BKNG | $214.36 | $62,798,780 | Consumer Discretionary | large | unknown | 2026-08-09 |
| BKR | $61.57 | $34,367,861 | Energy | large | unknown | 2026-08-09 |
| BLK | $1136.84 | $59,986,036 | Financials | large | unknown | 2026-08-09 |
| BMY | $64.70 | $54,450,986 | Health Care | large | unknown | 2026-08-09 |
| BRK.B | $520.96 | $58,446,004 | Financials | large | unknown | 2026-08-09 |
| BSX | $49.32 | $68,593,562 | Health Care | large | unknown | 2026-08-09 |
| BX | $137.14 | $31,192,004 | Financials | large | unknown | 2026-08-09 |
| C | $134.96 | $71,944,956 | Financials | large | unknown | 2026-08-09 |
| CAH | $236.40 | $22,406,637 | Health Care | large | unknown | 2026-08-09 |
| CARR | $63.99 | $27,378,141 | Industrials | large | unknown | 2026-08-09 |
| CAT | $842.34 | $126,313,008 | Industrials | large | unknown | 2026-08-09 |
| CB | $350.31 | $34,800,747 | Financials | large | unknown | 2026-08-09 |
| CCL | $28.98 | $30,711,458 | Consumer Discretionary | large | unknown | 2026-08-09 |
| CDNS | $339.23 | $49,593,703 | Information Technology | large | unknown | 2026-08-09 |
| CEG | $269.85 | $41,504,999 | Utilities | large | unknown | 2026-08-09 |
| CFG | $72.67 | $23,396,552 | Financials | large | unknown | 2026-08-09 |
| CHRW | $149.38 | $29,981,165 | Industrials | large | unknown | 2026-08-09 |
| CHTR | $152.57 | $23,133,521 | Communication Services | large | unknown | 2026-08-09 |
| CI | $282.45 | $31,498,984 | Health Care | large | unknown | 2026-08-09 |
| CIEN | $412.62 | $42,787,051 | Information Technology | large | unknown | 2026-08-09 |
| CL | $93.28 | $22,196,740 | Consumer Staples | large | unknown | 2026-08-09 |
| CMCSA | $25.36 | $47,797,384 | Communication Services | large | unknown | 2026-08-09 |
| CME | $263.71 | $35,621,342 | Financials | large | unknown | 2026-08-09 |
| CMG | $32.80 | $55,332,176 | Consumer Discretionary | large | unknown | 2026-08-09 |
| CMI | $644.19 | $41,244,557 | Industrials | large | unknown | 2026-08-09 |
| CNP | $40.67 | $22,084,492 | Utilities | large | unknown | 2026-08-09 |
| COF | $217.65 | $44,536,483 | Financials | large | unknown | 2026-08-09 |
| COIN | $153.61 | $37,066,751 | Financials | large | unknown | 2026-08-09 |
| COP | $117.64 | $43,265,569 | Energy | large | unknown | 2026-08-09 |
| COR | $320.51 | $24,634,623 | Health Care | large | unknown | 2026-08-09 |
| COST | $947.73 | $65,429,158 | Consumer Staples | large | unknown | 2026-08-09 |
| CPRT | $29.65 | $25,710,625 | Industrials | large | unknown | 2026-08-09 |
| CRH | $100.49 | $23,724,508 | Materials | large | unknown | 2026-08-09 |
| CRM | $192.71 | $88,127,268 | Information Technology | large | unknown | 2026-08-09 |
| CRS | $570.30 | $28,855,192 | Industrials | mid | unknown | 2026-08-09 |
| CRWD | $214.38 | $55,273,714 | Information Technology | large | unknown | 2026-08-09 |
| CSCO | $121.42 | $102,732,387 | Information Technology | large | unknown | 2026-08-09 |
| CSX | $50.25 | $48,498,951 | Industrials | large | unknown | 2026-08-09 |
| CTAS | $203.01 | $24,531,114 | Industrials | large | unknown | 2026-08-09 |
| CTSH | $57.67 | $34,829,069 | Information Technology | large | unknown | 2026-08-09 |
| CTVA | $76.84 | $20,123,115 | Materials | large | unknown | 2026-08-09 |
| CVNA | $70.84 | $38,324,104 | Consumer Discretionary | large | unknown | 2026-08-09 |
| CVS | $95.67 | $48,799,080 | Health Care | large | unknown | 2026-08-09 |
| CVX | $186.56 | $54,516,340 | Energy | large | unknown | 2026-08-09 |
| D | $67.38 | $25,733,465 | Utilities | large | unknown | 2026-08-09 |
| DAL | $91.35 | $26,213,465 | Industrials | large | unknown | 2026-08-09 |
| DASH | $216.13 | $44,770,544 | Consumer Discretionary | large | unknown | 2026-08-09 |
| DDOG | $233.84 | $63,275,874 | Information Technology | large | unknown | 2026-08-09 |
| DE | $621.05 | $35,359,565 | Industrials | large | unknown | 2026-08-09 |
| DELL | $453.46 | $109,778,082 | Information Technology | large | unknown | 2026-08-09 |
| DHR | $204.80 | $92,148,484 | Health Care | large | unknown | 2026-08-09 |
| DIS | $104.91 | $60,687,680 | Communication Services | large | unknown | 2026-08-09 |
| DLR | $193.70 | $31,711,257 | Real Estate | large | unknown | 2026-08-09 |
| DOCN | $123.98 | $24,170,145 | Information Technology | mid | unknown | 2026-08-09 |
| DOW | $29.34 | $23,410,641 | Materials | large | unknown | 2026-08-09 |
| DPZ | $351.04 | $20,534,566 | Consumer Discretionary | large | unknown | 2026-08-09 |
| DUK | $124.87 | $20,955,653 | Utilities | large | unknown | 2026-08-09 |
| DVN | $42.97 | $33,789,459 | Energy | large | unknown | 2026-08-09 |
| DXCM | $84.78 | $24,471,175 | Health Care | large | unknown | 2026-08-09 |
| EA | $209.86 | $42,756,955 | Communication Services | large | unknown | 2026-08-09 |
| EBAY | $111.94 | $23,317,596 | Consumer Discretionary | large | unknown | 2026-08-09 |
| EFX | $182.54 | $22,716,763 | Industrials | large | unknown | 2026-08-09 |
| ELV | $394.22 | $29,064,537 | Health Care | large | unknown | 2026-08-09 |
| EME | $817.55 | $23,746,999 | Industrials | large | unknown | 2026-08-09 |
| EMR | $158.26 | $22,975,206 | Industrials | large | unknown | 2026-08-09 |
| ENTG | $152.02 | $21,171,635 | Information Technology | mid | unknown | 2026-08-09 |
| EOG | $134.76 | $21,013,607 | Energy | large | unknown | 2026-08-09 |
| EQIX | $1042.49 | $45,311,686 | Real Estate | large | unknown | 2026-08-09 |
| EQT | $51.71 | $30,484,159 | Energy | large | unknown | 2026-08-09 |
| ETN | $448.48 | $57,965,478 | Industrials | large | unknown | 2026-08-09 |
| EW | $89.69 | $26,953,019 | Health Care | large | unknown | 2026-08-09 |
| EXC | $45.62 | $24,322,593 | Utilities | large | unknown | 2026-08-09 |
| EXPE | $310.67 | $26,108,214 | Consumer Discretionary | large | unknown | 2026-08-09 |
| F | $13.97 | $33,403,207 | Consumer Discretionary | large | unknown | 2026-08-09 |
| FAST | $51.82 | $30,170,089 | Industrials | large | unknown | 2026-08-09 |
| FCX | $69.62 | $58,007,191 | Materials | large | unknown | 2026-08-09 |
| FDX | $318.42 | $23,471,368 | Industrials | large | unknown | 2026-08-09 |
| FICO | $1040.65 | $32,758,650 | Information Technology | large | unknown | 2026-08-09 |
| FIS | $42.78 | $23,853,152 | Financials | large | unknown | 2026-08-09 |
| FISV | $52.38 | $21,304,642 | Financials | large | unknown | 2026-08-09 |
| FITB | $57.09 | $29,422,481 | Financials | large | unknown | 2026-08-09 |
| FIX | $1692.86 | $52,189,961 | Industrials | large | unknown | 2026-08-09 |
| FN | $562.35 | $33,905,698 | Information Technology | mid | unknown | 2026-08-09 |
| FSLR | $250.06 | $28,133,397 | Information Technology | large | unknown | 2026-08-09 |
| FTNT | $159.58 | $37,505,395 | Information Technology | large | unknown | 2026-08-09 |
| GE | $370.21 | $66,960,092 | Industrials | large | unknown | 2026-08-09 |
| GEHC | $71.77 | $21,716,510 | Health Care | large | unknown | 2026-08-09 |
| GEV | $990.33 | $143,352,292 | Industrials | large | unknown | 2026-08-09 |
| GILD | $133.10 | $38,396,793 | Health Care | large | unknown | 2026-08-09 |
| GIS | $36.88 | $26,586,499 | Consumer Staples | large | unknown | 2026-08-09 |
| GLW | $165.74 | $98,663,997 | Information Technology | large | unknown | 2026-08-09 |
| GM | $87.60 | $24,490,953 | Consumer Discretionary | large | unknown | 2026-08-09 |
| GNRC | $212.29 | $20,978,866 | Industrials | large | unknown | 2026-08-09 |
| GOOG | $353.42 | $239,323,428 | Communication Services | large | unknown | 2026-08-09 |
| GOOGL | $354.35 | $427,647,266 | Communication Services | large | unknown | 2026-08-09 |
| GS | $1040.00 | $85,333,388 | Financials | large | unknown | 2026-08-09 |
| GWW | $1277.25 | $26,787,652 | Industrials | large | unknown | 2026-08-09 |
| HAL | $31.89 | $29,669,092 | Energy | large | unknown | 2026-08-09 |
| HBAN | $17.55 | $24,895,697 | Financials | large | unknown | 2026-08-09 |
| HCA | $413.27 | $41,465,295 | Health Care | large | unknown | 2026-08-09 |
| HD | $355.61 | $58,241,147 | Consumer Discretionary | large | unknown | 2026-08-09 |
| HLT | $317.52 | $43,736,417 | Consumer Discretionary | large | unknown | 2026-08-09 |
| HON | $246.15 | $32,269,341 | Industrials | large | unknown | 2026-08-09 |
| HOOD | $93.28 | $74,278,916 | Financials | large | unknown | 2026-08-09 |
| HPE | $53.22 | $50,434,441 | Information Technology | large | unknown | 2026-08-09 |
| HPQ | $30.05 | $31,471,601 | Information Technology | large | unknown | 2026-08-09 |
| HUBB | $514.25 | $23,328,877 | Industrials | large | unknown | 2026-08-09 |
| HUM | $385.07 | $32,349,598 | Health Care | large | unknown | 2026-08-09 |
| HWM | $281.90 | $27,349,961 | Industrials | large | unknown | 2026-08-09 |
| IBKR | $87.83 | $20,881,464 | Financials | large | unknown | 2026-08-09 |
| IBM | $237.19 | $121,284,730 | Information Technology | large | unknown | 2026-08-09 |
| ICE | $150.32 | $33,022,173 | Financials | large | unknown | 2026-08-09 |
| IDXX | $586.77 | $30,021,101 | Health Care | large | unknown | 2026-08-09 |
| ILMN | $188.04 | $26,081,226 | Health Care | mid | unknown | 2026-08-09 |
| INTC | $101.64 | $363,509,993 | Information Technology | large | unknown | 2026-08-09 |
| INTU | $325.22 | $75,079,268 | Information Technology | large | unknown | 2026-08-09 |
| IQV | $238.74 | $21,934,122 | Health Care | large | unknown | 2026-08-09 |
| IR | $86.97 | $22,335,432 | Industrials | large | unknown | 2026-08-09 |
| ISRG | $378.86 | $75,190,077 | Health Care | large | unknown | 2026-08-09 |
| ITW | $296.61 | $21,548,835 | Industrials | large | unknown | 2026-08-09 |
| JCI | $152.17 | $25,253,941 | Industrials | large | unknown | 2026-08-09 |
| JNJ | $259.25 | $102,880,161 | Health Care | large | unknown | 2026-08-09 |
| JPM | $357.56 | $89,408,190 | Financials | large | unknown | 2026-08-09 |
| KDP | $30.01 | $26,774,952 | Consumer Staples | large | unknown | 2026-08-09 |
| KEYS | $340.76 | $28,939,875 | Information Technology | large | unknown | 2026-08-09 |
| KHC | $25.32 | $24,971,617 | Consumer Staples | large | unknown | 2026-08-09 |
| KKR | $102.80 | $22,730,342 | Financials | large | unknown | 2026-08-09 |
| KLAC | $198.07 | $102,991,553 | Information Technology | large | unknown | 2026-08-09 |
| KNX | $70.05 | $20,876,522 | Industrials | mid | unknown | 2026-08-09 |
| KO | $87.06 | $103,988,645 | Consumer Staples | large | unknown | 2026-08-09 |
| KR | $56.73 | $24,809,183 | Consumer Staples | large | unknown | 2026-08-09 |
| KVUE | $19.22 | $23,814,288 | Consumer Staples | large | unknown | 2026-08-09 |
| LHX | $286.70 | $23,797,246 | Industrials | large | unknown | 2026-08-09 |
| LII | $439.48 | $23,001,781 | Industrials | large | unknown | 2026-08-09 |
| LIN | $489.86 | $54,270,307 | Materials | large | unknown | 2026-08-09 |
| LLY | $1185.96 | $137,742,824 | Health Care | large | unknown | 2026-08-09 |
| LMT | $587.93 | $29,949,085 | Industrials | large | unknown | 2026-08-09 |
| LOW | $223.33 | $25,690,231 | Consumer Discretionary | large | unknown | 2026-08-09 |
| LRCX | $311.31 | $140,730,754 | Information Technology | large | unknown | 2026-08-09 |
| LYV | $180.61 | $21,428,998 | Communication Services | large | unknown | 2026-08-09 |
| MA | $562.87 | $96,655,598 | Financials | large | unknown | 2026-08-09 |
| MAR | $353.87 | $33,001,825 | Consumer Discretionary | large | unknown | 2026-08-09 |
| MCD | $274.48 | $54,827,354 | Consumer Discretionary | large | unknown | 2026-08-09 |
| MCHP | $84.70 | $35,096,629 | Information Technology | large | unknown | 2026-08-09 |
| MCK | $869.27 | $44,667,169 | Health Care | large | unknown | 2026-08-09 |
| MCO | $477.40 | $27,095,414 | Financials | large | unknown | 2026-08-09 |
| MDLZ | $62.59 | $38,494,330 | Consumer Staples | large | unknown | 2026-08-09 |
| MDT | $87.16 | $42,189,968 | Health Care | large | unknown | 2026-08-09 |
| META | $591.83 | $457,573,966 | Communication Services | large | unknown | 2026-08-09 |
| MKSI | $305.11 | $36,456,056 | Information Technology | mid | unknown | 2026-08-09 |
| MLM | $548.59 | $23,890,573 | Materials | large | unknown | 2026-08-09 |
| MMM | $182.92 | $32,223,140 | Industrials | large | unknown | 2026-08-09 |
| MNST | $90.36 | $28,427,625 | Consumer Staples | large | unknown | 2026-08-09 |
| MO | $68.33 | $36,277,207 | Consumer Staples | large | unknown | 2026-08-09 |
| MPC | $298.02 | $38,586,375 | Energy | large | unknown | 2026-08-09 |
| MPWR | $1400.64 | $67,699,407 | Information Technology | large | unknown | 2026-08-09 |
| MRK | $128.56 | $39,720,643 | Health Care | large | unknown | 2026-08-09 |
| MRSH | $191.65 | $21,520,252 | Financials | large | unknown | 2026-08-09 |
| MS | $216.34 | $70,195,986 | Financials | large | unknown | 2026-08-09 |
| MSCI | $563.06 | $35,200,528 | Financials | large | unknown | 2026-08-09 |
| MSFT | $499.88 | $637,077,855 | Information Technology | large | unknown | 2026-08-09 |
| MSI | $467.54 | $20,606,918 | Information Technology | large | unknown | 2026-08-09 |
| MTD | $1430.20 | $20,804,919 | Health Care | large | unknown | 2026-08-09 |
| MTSI | $310.29 | $20,290,555 | Information Technology | mid | unknown | 2026-08-09 |
| MTZ | $272.56 | $31,984,769 | Industrials | mid | unknown | 2026-08-09 |
| MU | $878.41 | $1,024,107,372 | Information Technology | large | unknown | 2026-08-09 |
| NEE | $84.67 | $56,219,891 | Utilities | large | unknown | 2026-08-09 |
| NEM | $112.98 | $32,791,147 | Materials | large | unknown | 2026-08-09 |
| NFLX | $74.12 | $223,218,986 | Communication Services | large | unknown | 2026-08-09 |
| NKE | $41.70 | $44,806,370 | Consumer Discretionary | large | unknown | 2026-08-09 |
| NOC | $571.22 | $29,953,809 | Industrials | large | unknown | 2026-08-09 |
| NOW | $124.85 | $120,746,287 | Information Technology | large | unknown | 2026-08-09 |
| NRG | $118.01 | $21,272,712 | Utilities | large | unknown | 2026-08-09 |
| NTAP | $189.60 | $21,586,867 | Information Technology | large | unknown | 2026-08-09 |
| NVDA | $223.93 | $937,114,351 | Information Technology | large | unknown | 2026-08-09 |
| NVT | $164.77 | $20,567,660 | Industrials | mid | unknown | 2026-08-09 |
| NXPI | $240.08 | $51,881,578 | Information Technology | large | unknown | 2026-08-09 |
| NXT | $103.30 | $21,205,375 | Industrials | mid | unknown | 2026-08-09 |
| ODFL | $216.26 | $21,969,986 | Industrials | large | unknown | 2026-08-09 |
| ON | $81.15 | $35,024,255 | Information Technology | large | unknown | 2026-08-09 |
| ONTO | $307.92 | $25,664,390 | Information Technology | mid | unknown | 2026-08-09 |
| ORCL | $146.94 | $168,674,721 | Information Technology | large | unknown | 2026-08-09 |
| ORLY | $93.51 | $33,420,603 | Consumer Discretionary | large | unknown | 2026-08-09 |
| OXY | $55.90 | $36,153,871 | Energy | large | unknown | 2026-08-09 |
| PANW | $363.88 | $100,526,347 | Information Technology | large | unknown | 2026-08-09 |
| PATH | $15.03 | $26,838,664 | Information Technology | mid | unknown | 2026-08-09 |
| PCAR | $133.13 | $23,442,526 | Industrials | large | unknown | 2026-08-09 |
| PCG | $17.46 | $26,657,689 | Utilities | large | unknown | 2026-08-09 |
| PEP | $139.01 | $37,681,052 | Consumer Staples | large | unknown | 2026-08-09 |
| PFE | $26.75 | $54,986,071 | Health Care | large | unknown | 2026-08-09 |
| PG | $145.78 | $52,034,416 | Consumer Staples | large | unknown | 2026-08-09 |
| PGR | $215.39 | $32,223,649 | Financials | large | unknown | 2026-08-09 |
| PH | $1074.05 | $43,186,883 | Industrials | large | unknown | 2026-08-09 |
| PINS | $23.70 | $21,295,349 | Communication Services | mid | unknown | 2026-08-09 |
| PLD | $140.11 | $36,565,209 | Real Estate | large | unknown | 2026-08-09 |
| PLTR | $172.00 | $193,109,107 | Information Technology | large | unknown | 2026-08-09 |
| PM | $189.43 | $48,418,887 | Consumer Staples | large | unknown | 2026-08-09 |
| PNC | $252.49 | $22,216,192 | Financials | large | unknown | 2026-08-09 |
| PSX | $203.91 | $28,549,362 | Energy | large | unknown | 2026-08-09 |
| PWR | $671.74 | $48,100,470 | Industrials | large | unknown | 2026-08-09 |
| PYPL | $59.05 | $54,388,452 | Financials | large | unknown | 2026-08-09 |
| QCOM | $167.85 | $86,162,028 | Information Technology | large | unknown | 2026-08-09 |
| RCL | $319.99 | $42,039,629 | Consumer Discretionary | large | unknown | 2026-08-09 |
| REGN | $784.15 | $38,677,235 | Health Care | large | unknown | 2026-08-09 |
| RF | $31.43 | $23,341,859 | Financials | large | unknown | 2026-08-09 |
| ROK | $440.88 | $27,391,684 | Industrials | large | unknown | 2026-08-09 |
| ROST | $255.19 | $26,275,670 | Consumer Discretionary | large | unknown | 2026-08-09 |
| RRX | $178.12 | $20,229,569 | Industrials | mid | unknown | 2026-08-09 |
| RTX | $223.10 | $48,080,450 | Industrials | large | unknown | 2026-08-09 |
| SBUX | $105.60 | $32,692,955 | Consumer Discretionary | large | unknown | 2026-08-09 |
| SCHW | $107.58 | $45,728,286 | Financials | large | unknown | 2026-08-09 |
| SHW | $369.72 | $36,160,674 | Materials | large | unknown | 2026-08-09 |
| SLB | $50.52 | $42,379,476 | Energy | large | unknown | 2026-08-09 |
| SMCI | $31.11 | $53,303,857 | Information Technology | large | unknown | 2026-08-09 |
| SNDK | $1212.81 | $589,223,059 | Information Technology | large | unknown | 2026-08-09 |
| SNPS | $415.92 | $41,783,144 | Information Technology | large | unknown | 2026-08-09 |
| SO | $92.69 | $24,108,006 | Utilities | large | unknown | 2026-08-09 |
| SPGI | $408.17 | $48,534,353 | Financials | large | unknown | 2026-08-09 |
| STRL | $546.78 | $33,095,660 | Industrials | mid | unknown | 2026-08-09 |
| STT | $184.70 | $21,814,436 | Financials | large | unknown | 2026-08-09 |
| STX | $812.76 | $209,393,785 | Information Technology | large | unknown | 2026-08-09 |
| SYK | $338.92 | $49,671,305 | Health Care | large | unknown | 2026-08-09 |
| T | $23.80 | $84,538,161 | Communication Services | large | unknown | 2026-08-09 |
| TDG | $1224.88 | $46,931,738 | Industrials | large | unknown | 2026-08-09 |
| TEL | $216.39 | $43,079,417 | Information Technology | large | unknown | 2026-08-09 |
| TER | $379.12 | $66,690,851 | Information Technology | large | unknown | 2026-08-09 |
| TFC | $52.35 | $26,785,075 | Financials | large | unknown | 2026-08-09 |
| TGT | $149.71 | $25,606,385 | Consumer Staples | large | unknown | 2026-08-09 |
| THC | $262.17 | $22,856,940 | Health Care | mid | unknown | 2026-08-09 |
| TJX | $161.31 | $33,142,807 | Consumer Discretionary | large | unknown | 2026-08-09 |
| TMO | $594.02 | $89,598,753 | Health Care | large | unknown | 2026-08-09 |
| TMUS | $177.11 | $39,431,342 | Communication Services | large | unknown | 2026-08-09 |
| TOST | $34.46 | $22,650,835 | Financials | mid | unknown | 2026-08-09 |
| TRGP | $256.91 | $20,321,621 | Energy | large | unknown | 2026-08-09 |
| TRV | $384.32 | $36,102,452 | Financials | large | unknown | 2026-08-09 |
| TSCO | $34.58 | $29,061,850 | Consumer Discretionary | large | unknown | 2026-08-09 |
| TSLA | $328.49 | $347,856,568 | Consumer Discretionary | large | unknown | 2026-08-09 |
| TT | $482.55 | $38,417,120 | Industrials | large | unknown | 2026-08-09 |
| TTMI | $137.25 | $25,226,099 | Information Technology | mid | unknown | 2026-08-09 |
| TTWO | $246.45 | $23,049,466 | Communication Services | large | unknown | 2026-08-09 |
| TWLO | $241.56 | $27,329,728 | Information Technology | mid | unknown | 2026-08-09 |
| TXN | $286.05 | $92,246,012 | Information Technology | large | unknown | 2026-08-09 |
| UAL | $129.59 | $24,324,887 | Industrials | large | unknown | 2026-08-09 |
| UBER | $75.02 | $84,471,439 | Industrials | large | unknown | 2026-08-09 |
| UNH | $407.09 | $104,144,423 | Health Care | large | unknown | 2026-08-09 |
| UNP | $293.13 | $56,992,883 | Industrials | large | unknown | 2026-08-09 |
| UPS | $104.50 | $26,801,950 | Industrials | large | unknown | 2026-08-09 |
| URI | $1161.75 | $40,073,476 | Industrials | large | unknown | 2026-08-09 |
| USB | $63.92 | $39,673,716 | Financials | large | unknown | 2026-08-09 |
| V | $362.59 | $115,477,967 | Financials | large | unknown | 2026-08-09 |
| VLO | $298.30 | $44,302,966 | Energy | large | unknown | 2026-08-09 |
| VMC | $284.62 | $22,576,258 | Materials | large | unknown | 2026-08-09 |
| VRSK | $191.88 | $24,171,419 | Industrials | large | unknown | 2026-08-09 |
| VRTX | $496.21 | $27,578,311 | Health Care | large | unknown | 2026-08-09 |
| VST | $140.63 | $38,579,046 | Utilities | large | unknown | 2026-08-09 |
| VZ | $47.05 | $84,420,930 | Communication Services | large | unknown | 2026-08-09 |
| WAB | $291.82 | $20,278,657 | Industrials | large | unknown | 2026-08-09 |
| WAT | $406.91 | $26,478,912 | Health Care | large | unknown | 2026-08-09 |
| WBD | $26.77 | $51,865,281 | Communication Services | large | unknown | 2026-08-09 |
| WBS | $79.05 | $21,090,649 | Financials | mid | unknown | 2026-08-09 |
| WCC | $363.58 | $20,568,523 | Industrials | mid | unknown | 2026-08-09 |
| WDAY | $179.63 | $35,079,402 | Information Technology | large | unknown | 2026-08-09 |
| WDC | $434.12 | $176,613,232 | Information Technology | large | unknown | 2026-08-09 |
| WELL | $236.98 | $37,820,601 | Real Estate | large | unknown | 2026-08-09 |
| WFC | $87.26 | $78,343,614 | Financials | large | unknown | 2026-08-09 |
| WM | $227.68 | $26,522,464 | Industrials | large | unknown | 2026-08-09 |
| WMB | $70.42 | $30,825,409 | Energy | large | unknown | 2026-08-09 |
| WMT | $111.82 | $115,662,232 | Consumer Staples | large | unknown | 2026-08-09 |
| XEL | $78.04 | $23,540,884 | Utilities | large | unknown | 2026-08-09 |
| XOM | $152.93 | $75,293,414 | Energy | large | unknown | 2026-08-09 |
| XYZ | $79.02 | $28,236,628 | Financials | large | unknown | 2026-08-09 |
| YUM | $150.77 | $21,223,514 | Consumer Discretionary | large | unknown | 2026-08-09 |
| ZTS | $72.68 | $23,710,118 | Health Care | large | unknown | 2026-08-09 |
