---
screened_on: 2026-08-23
expires_on: 2026-08-30
total_passed: 294
total_rejected: 1241
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
| AAL | $13.83 | 27,019,024 | Industrials | mid | unknown | 2026-08-23 |
| AAPL | $309.27 | 557,769,620 | Information Technology | large | unknown | 2026-08-23 |
| ABBV | $264.99 | 65,879,074 | Health Care | large | unknown | 2026-08-23 |
| ABNB | $187.32 | 39,895,344 | Consumer Discretionary | large | unknown | 2026-08-23 |
| ABT | $116.64 | 49,798,697 | Health Care | large | unknown | 2026-08-23 |
| ACN | $185.31 | 52,327,103 | Information Technology | large | unknown | 2026-08-23 |
| ADBE | $275.29 | 56,011,183 | Information Technology | large | unknown | 2026-08-23 |
| ADI | $373.16 | 63,182,698 | Information Technology | large | unknown | 2026-08-23 |
| ADP | $280.79 | 31,158,520 | Industrials | large | unknown | 2026-08-23 |
| ADSK | $253.90 | 22,462,464 | Information Technology | large | unknown | 2026-08-23 |
| AEP | $120.87 | 21,565,501 | Utilities | large | unknown | 2026-08-23 |
| AKAM | $110.40 | 21,479,344 | Information Technology | large | unknown | 2026-08-23 |
| ALL | $253.69 | 24,437,187 | Unknown | large | unknown | 2026-08-23 |
| AMAT | $492.12 | 164,380,734 | Information Technology | large | unknown | 2026-08-23 |
| AMD | $473.20 | 348,946,369 | Information Technology | large | unknown | 2026-08-23 |
| AMGN | $439.40 | 38,109,707 | Health Care | large | unknown | 2026-08-23 |
| AMT | $175.77 | 22,672,425 | Real Estate | large | unknown | 2026-08-23 |
| AMZN | $258.57 | 533,042,455 | Consumer Discretionary | large | unknown | 2026-08-23 |
| ANET | $188.66 | 81,783,830 | Information Technology | large | unknown | 2026-08-23 |
| AON | $354.99 | 20,130,988 | Financials | large | unknown | 2026-08-23 |
| APH | $157.04 | 57,264,356 | Information Technology | large | unknown | 2026-08-23 |
| APO | $132.68 | 23,658,415 | Financials | large | unknown | 2026-08-23 |
| APP | $305.99 | 92,067,594 | Unknown | large | unknown | 2026-08-23 |
| ATI | $206.96 | 23,138,322 | Materials | mid | unknown | 2026-08-23 |
| AVGO | $368.37 | 261,278,939 | Information Technology | large | unknown | 2026-08-23 |
| AXON | $627.70 | 27,061,027 | Industrials | large | unknown | 2026-08-23 |
| AXP | $336.12 | 37,689,277 | Unknown | large | unknown | 2026-08-23 |
| AZO | $2957.08 | 32,575,209 | Consumer Discretionary | large | unknown | 2026-08-23 |
| BA | $214.20 | 62,720,183 | Industrials | large | unknown | 2026-08-23 |
| BAC | $61.70 | 122,825,444 | Financials | large | unknown | 2026-08-23 |
| BKNG | $209.62 | 60,530,201 | Consumer Discretionary | large | unknown | 2026-08-23 |
| BKR | $62.33 | 29,572,478 | Unknown | large | unknown | 2026-08-23 |
| BLK | $1156.44 | 43,414,798 | Unknown | large | unknown | 2026-08-23 |
| BMY | $67.02 | 53,413,344 | Health Care | large | unknown | 2026-08-23 |
| BRK.B | $495.77 | 61,596,083 | Financials | large | unknown | 2026-08-23 |
| BSX | $50.38 | 92,887,419 | Health Care | large | unknown | 2026-08-23 |
| BX | $143.39 | 32,578,389 | Financials | large | unknown | 2026-08-23 |
| C | $131.63 | 45,121,082 | Financials | large | unknown | 2026-08-23 |
| CAH | $229.54 | 21,732,147 | Unknown | large | unknown | 2026-08-23 |
| CARR | $60.37 | 24,374,911 | Unknown | large | unknown | 2026-08-23 |
| CAT | $827.83 | 120,748,021 | Industrials | large | unknown | 2026-08-23 |
| CB | $341.03 | 25,828,311 | Financials | large | unknown | 2026-08-23 |
| CCL | $25.72 | 30,485,794 | Unknown | large | unknown | 2026-08-23 |
| CDE | $20.98 | 22,741,701 | Unknown | mid | unknown | 2026-08-23 |
| CDNS | $318.83 | 44,464,199 | Unknown | large | unknown | 2026-08-23 |
| CEG | $272.83 | 35,617,573 | Unknown | large | unknown | 2026-08-23 |
| CHRW | $141.66 | 22,273,361 | Industrials | large | unknown | 2026-08-23 |
| CHTR | $150.09 | 22,257,992 | Unknown | large | unknown | 2026-08-23 |
| CI | $277.63 | 25,484,006 | Health Care | large | unknown | 2026-08-23 |
| CIEN | $395.89 | 48,807,520 | Unknown | large | unknown | 2026-08-23 |
| CL | $91.07 | 22,363,767 | Consumer Staples | large | unknown | 2026-08-23 |
| CMCSA | $26.85 | 43,467,407 | Unknown | large | unknown | 2026-08-23 |
| CME | $274.89 | 26,442,182 | Financials | large | unknown | 2026-08-23 |
| CMG | $36.87 | 51,343,885 | Consumer Discretionary | large | unknown | 2026-08-23 |
| CMI | $587.64 | 37,159,385 | Industrials | large | unknown | 2026-08-23 |
| COF | $217.97 | 30,587,962 | Financials | large | unknown | 2026-08-23 |
| COHR | $289.38 | 105,433,242 | Unknown | large | unknown | 2026-08-23 |
| COIN | $186.56 | 43,281,106 | Unknown | large | unknown | 2026-08-23 |
| COP | $134.92 | 47,535,444 | Energy | large | unknown | 2026-08-23 |
| COR | $318.02 | 26,859,693 | Unknown | large | unknown | 2026-08-23 |
| COST | $947.48 | 58,649,079 | Consumer Staples | large | unknown | 2026-08-23 |
| CPRT | $33.81 | 30,223,076 | Industrials | large | unknown | 2026-08-23 |
| CRH | $95.08 | 29,130,243 | Unknown | large | unknown | 2026-08-23 |
| CRM | $209.15 | 88,000,065 | Information Technology | large | unknown | 2026-08-23 |
| CRS | $492.58 | 24,733,005 | Materials | mid | unknown | 2026-08-23 |
| CRWD | $191.94 | 55,498,439 | Information Technology | large | unknown | 2026-08-23 |
| CSCO | $111.05 | 107,241,902 | Information Technology | large | unknown | 2026-08-23 |
| CSX | $51.59 | 37,450,564 | Industrials | large | unknown | 2026-08-23 |
| CTSH | $61.89 | 30,208,251 | Information Technology | large | unknown | 2026-08-23 |
| CTVA | $81.77 | 21,954,588 | Materials | large | unknown | 2026-08-23 |
| CVNA | $69.89 | 39,601,450 | Unknown | large | unknown | 2026-08-23 |
| CVS | $93.03 | 44,855,637 | Health Care | large | unknown | 2026-08-23 |
| CVX | $205.21 | 61,459,583 | Energy | large | unknown | 2026-08-23 |
| D | $66.61 | 20,024,369 | Utilities | large | unknown | 2026-08-23 |
| DAL | $82.42 | 20,565,278 | Industrials | large | unknown | 2026-08-23 |
| DASH | $223.52 | 52,069,044 | Unknown | large | unknown | 2026-08-23 |
| DDOG | $235.57 | 65,656,152 | Unknown | large | unknown | 2026-08-23 |
| DE | $647.75 | 41,167,331 | Industrials | large | unknown | 2026-08-23 |
| DELL | $441.55 | 99,332,976 | Information Technology | large | unknown | 2026-08-23 |
| DHR | $218.90 | 57,058,943 | Health Care | large | unknown | 2026-08-23 |
| DIS | $107.77 | 53,266,664 | Communication Services | large | unknown | 2026-08-23 |
| DLR | $190.61 | 21,717,029 | Unknown | large | unknown | 2026-08-23 |
| DOCN | $115.56 | 21,271,413 | Unknown | mid | unknown | 2026-08-23 |
| DOW | $32.34 | 20,735,188 | Materials | large | unknown | 2026-08-23 |
| DRI | $221.66 | 20,256,744 | Consumer Discretionary | large | unknown | 2026-08-23 |
| DT | $49.30 | 22,512,764 | Unknown | mid | unknown | 2026-08-23 |
| DUK | $119.85 | 23,745,705 | Utilities | large | unknown | 2026-08-23 |
| DVN | $49.10 | 35,594,205 | Energy | large | unknown | 2026-08-23 |
| DXCM | $92.35 | 24,959,346 | Health Care | large | unknown | 2026-08-23 |
| EBAY | $104.09 | 23,338,897 | Consumer Discretionary | large | unknown | 2026-08-23 |
| ECL | $281.65 | 22,758,143 | Materials | large | unknown | 2026-08-23 |
| EME | $776.00 | 21,349,511 | Unknown | large | unknown | 2026-08-23 |
| EMR | $157.23 | 21,318,712 | Industrials | large | unknown | 2026-08-23 |
| EOG | $153.05 | 25,227,510 | Energy | large | unknown | 2026-08-23 |
| EQIX | $1065.61 | 38,566,253 | Real Estate | large | unknown | 2026-08-23 |
| EQT | $53.72 | 27,698,102 | Unknown | large | unknown | 2026-08-23 |
| ETN | $419.33 | 49,556,317 | Industrials | large | unknown | 2026-08-23 |
| EXC | $43.75 | 20,467,428 | Utilities | large | unknown | 2026-08-23 |
| EXPE | $321.67 | 26,845,262 | Consumer Discretionary | large | unknown | 2026-08-23 |
| F | $14.41 | 33,248,098 | Consumer Discretionary | large | unknown | 2026-08-23 |
| FAST | $51.26 | 23,425,194 | Industrials | large | unknown | 2026-08-23 |
| FCX | $76.62 | 54,928,065 | Materials | large | unknown | 2026-08-23 |
| FDX | $325.08 | 35,824,247 | Industrials | large | unknown | 2026-08-23 |
| FERG | $242.27 | 44,208,456 | Unknown | large | unknown | 2026-08-23 |
| FICO | $1172.76 | 32,948,740 | Information Technology | large | unknown | 2026-08-23 |
| FIS | $41.33 | 23,547,455 | Financials | large | unknown | 2026-08-23 |
| FISV | $52.58 | 23,276,659 | Unknown | large | unknown | 2026-08-23 |
| FITB | $54.81 | 23,468,228 | Financials | large | unknown | 2026-08-23 |
| FIX | $1655.21 | 44,728,944 | Unknown | large | unknown | 2026-08-23 |
| FLEX | $110.42 | 26,803,116 | Unknown | large | unknown | 2026-08-23 |
| FN | $436.89 | 37,055,650 | Unknown | mid | unknown | 2026-08-23 |
| FSLR | $214.20 | 29,232,933 | Unknown | large | unknown | 2026-08-23 |
| FTNT | $153.51 | 34,290,975 | Information Technology | large | unknown | 2026-08-23 |
| GE | $348.26 | 54,333,824 | Industrials | large | unknown | 2026-08-23 |
| GEV | $956.44 | 108,623,301 | Industrials | large | unknown | 2026-08-23 |
| GILD | $146.06 | 35,148,763 | Health Care | large | unknown | 2026-08-23 |
| GIS | $39.98 | 22,168,446 | Consumer Staples | large | unknown | 2026-08-23 |
| GLW | $149.83 | 86,019,910 | Information Technology | large | unknown | 2026-08-23 |
| GOOG | $341.73 | 227,060,908 | Communication Services | large | unknown | 2026-08-23 |
| GOOGL | $344.75 | 348,038,682 | Communication Services | large | unknown | 2026-08-23 |
| GS | $1039.63 | 73,991,644 | Financials | large | unknown | 2026-08-23 |
| GWW | $1312.33 | 23,008,960 | Industrials | large | unknown | 2026-08-23 |
| HAL | $35.33 | 21,947,892 | Energy | large | unknown | 2026-08-23 |
| HBAN | $17.03 | 21,956,064 | Financials | large | unknown | 2026-08-23 |
| HCA | $429.29 | 34,130,684 | Health Care | large | unknown | 2026-08-23 |
| HD | $335.71 | 57,047,218 | Consumer Discretionary | large | unknown | 2026-08-23 |
| HL | $20.72 | 21,856,182 | Unknown | mid | unknown | 2026-08-23 |
| HLT | $326.60 | 38,429,960 | Consumer Discretionary | large | unknown | 2026-08-23 |
| HON | $215.99 | 26,907,121 | Industrials | large | unknown | 2026-08-23 |
| HONA | $164.71 | 38,715,456 | Unknown | large | unknown | 2026-08-23 |
| HOOD | $108.13 | 59,733,162 | Unknown | large | unknown | 2026-08-23 |
| HPE | $53.44 | 46,927,093 | Information Technology | large | unknown | 2026-08-23 |
| HPQ | $29.71 | 32,757,312 | Information Technology | large | unknown | 2026-08-23 |
| HUBB | $470.30 | 23,637,306 | Industrials | large | unknown | 2026-08-23 |
| HUM | $378.73 | 28,356,458 | Health Care | large | unknown | 2026-08-23 |
| HWM | $271.64 | 31,342,492 | Industrials | large | unknown | 2026-08-23 |
| IBKR | $93.89 | 20,520,537 | Unknown | large | unknown | 2026-08-23 |
| IBM | $235.58 | 56,765,880 | Information Technology | large | unknown | 2026-08-23 |
| ICE | $161.30 | 30,963,407 | Financials | large | unknown | 2026-08-23 |
| IDXX | $556.73 | 28,985,425 | Health Care | large | unknown | 2026-08-23 |
| ILMN | $219.43 | 28,339,757 | Health Care | mid | unknown | 2026-08-23 |
| INTC | $90.02 | 368,790,880 | Information Technology | large | unknown | 2026-08-23 |
| INTU | $366.98 | 69,470,629 | Information Technology | large | unknown | 2026-08-23 |
| IQV | $260.04 | 24,598,291 | Health Care | large | unknown | 2026-08-23 |
| ISRG | $378.85 | 57,780,981 | Health Care | large | unknown | 2026-08-23 |
| JCI | $143.17 | 30,041,864 | Industrials | large | unknown | 2026-08-23 |
| JNJ | $270.28 | 71,002,138 | Health Care | large | unknown | 2026-08-23 |
| JPM | $351.62 | 70,426,428 | Financials | large | unknown | 2026-08-23 |
| KDP | $32.04 | 28,259,829 | Consumer Staples | large | unknown | 2026-08-23 |
| KEYS | $316.37 | 28,605,858 | Information Technology | large | unknown | 2026-08-23 |
| KHC | $25.58 | 23,190,263 | Consumer Staples | large | unknown | 2026-08-23 |
| KKR | $108.47 | 29,681,237 | Unknown | large | unknown | 2026-08-23 |
| KLAC | $184.05 | 92,969,668 | Information Technology | large | unknown | 2026-08-23 |
| KMI | $30.98 | 21,934,270 | Energy | large | unknown | 2026-08-23 |
| KO | $91.10 | 91,838,639 | Consumer Staples | large | unknown | 2026-08-23 |
| KR | $57.86 | 23,899,529 | Consumer Staples | large | unknown | 2026-08-23 |
| KVUE | $19.05 | 21,598,597 | Unknown | large | unknown | 2026-08-23 |
| LHX | $266.62 | 24,778,879 | Industrials | large | unknown | 2026-08-23 |
| LII | $402.80 | 23,111,654 | Unknown | large | unknown | 2026-08-23 |
| LIN | $487.39 | 50,930,982 | Materials | large | unknown | 2026-08-23 |
| LITE | $866.81 | 166,068,221 | Unknown | large | unknown | 2026-08-23 |
| LLY | $1255.20 | 135,069,641 | Health Care | large | unknown | 2026-08-23 |
| LMT | $563.65 | 25,025,066 | Industrials | large | unknown | 2026-08-23 |
| LOW | $216.06 | 30,010,804 | Consumer Discretionary | large | unknown | 2026-08-23 |
| LRCX | $313.95 | 135,101,321 | Information Technology | large | unknown | 2026-08-23 |
| MA | $580.60 | 94,817,019 | Financials | large | unknown | 2026-08-23 |
| MAR | $356.45 | 29,670,058 | Unknown | large | unknown | 2026-08-23 |
| MCD | $271.07 | 48,952,591 | Consumer Discretionary | large | unknown | 2026-08-23 |
| MCHP | $76.09 | 33,072,760 | Information Technology | large | unknown | 2026-08-23 |
| MCK | $860.44 | 43,650,731 | Health Care | large | unknown | 2026-08-23 |
| MDLZ | $64.46 | 35,309,056 | Consumer Staples | large | unknown | 2026-08-23 |
| MDT | $93.35 | 44,586,652 | Health Care | large | unknown | 2026-08-23 |
| META | $549.58 | 389,720,029 | Communication Services | large | unknown | 2026-08-23 |
| MKSI | $279.02 | 32,570,837 | Information Technology | mid | unknown | 2026-08-23 |
| MLM | $534.85 | 28,740,467 | Materials | large | unknown | 2026-08-23 |
| MMM | $178.96 | 24,786,610 | Industrials | large | unknown | 2026-08-23 |
| MNST | $47.80 | 27,853,025 | Consumer Staples | large | unknown | 2026-08-23 |
| MO | $66.08 | 43,745,814 | Consumer Staples | large | unknown | 2026-08-23 |
| MPC | $360.60 | 37,019,478 | Energy | large | unknown | 2026-08-23 |
| MPWR | $1316.70 | 57,693,772 | Information Technology | large | unknown | 2026-08-23 |
| MRK | $152.56 | 54,229,016 | Health Care | large | unknown | 2026-08-23 |
| MRNA | $145.10 | 65,436,255 | Health Care | large | unknown | 2026-08-23 |
| MRVL | $237.07 | 127,272,521 | Unknown | large | unknown | 2026-08-23 |
| MS | $214.19 | 48,081,152 | Financials | large | unknown | 2026-08-23 |
| MSCI | $563.96 | 23,803,892 | Financials | large | unknown | 2026-08-23 |
| MSFT | $483.33 | 555,046,403 | Information Technology | large | unknown | 2026-08-23 |
| MSI | $480.42 | 27,279,944 | Information Technology | large | unknown | 2026-08-23 |
| MTSI | $266.62 | 20,189,230 | Unknown | mid | unknown | 2026-08-23 |
| MTZ | $266.37 | 33,454,785 | Unknown | mid | unknown | 2026-08-23 |
| MU | $966.54 | 894,484,277 | Information Technology | large | unknown | 2026-08-23 |
| NEE | $83.64 | 55,668,743 | Utilities | large | unknown | 2026-08-23 |
| NEM | $131.57 | 35,252,589 | Materials | large | unknown | 2026-08-23 |
| NFLX | $79.62 | 162,706,106 | Communication Services | large | unknown | 2026-08-23 |
| NI | $40.63 | 21,582,067 | Utilities | large | unknown | 2026-08-23 |
| NKE | $40.75 | 51,247,809 | Consumer Discretionary | large | unknown | 2026-08-23 |
| NOC | $551.11 | 20,599,316 | Industrials | large | unknown | 2026-08-23 |
| NOW | $128.52 | 109,080,523 | Information Technology | large | unknown | 2026-08-23 |
| NTAP | $192.29 | 23,789,946 | Information Technology | large | unknown | 2026-08-23 |
| NUE | $243.61 | 22,430,273 | Materials | large | unknown | 2026-08-23 |
| NVDA | $214.74 | 887,856,734 | Information Technology | large | unknown | 2026-08-23 |
| NVT | $151.95 | 21,705,054 | Industrials | mid | unknown | 2026-08-23 |
| NXPI | $225.50 | 46,385,694 | Unknown | large | unknown | 2026-08-23 |
| ON | $74.23 | 31,412,020 | Information Technology | large | unknown | 2026-08-23 |
| ONTO | $293.24 | 27,313,636 | Information Technology | mid | unknown | 2026-08-23 |
| ORCL | $146.47 | 135,050,599 | Information Technology | large | unknown | 2026-08-23 |
| ORLY | $89.09 | 26,518,622 | Consumer Discretionary | large | unknown | 2026-08-23 |
| OXY | $61.29 | 34,232,827 | Energy | large | unknown | 2026-08-23 |
| PANW | $357.90 | 86,419,245 | Unknown | large | unknown | 2026-08-23 |
| PATH | $16.39 | 27,953,761 | Unknown | mid | unknown | 2026-08-23 |
| PCAR | $131.07 | 23,097,438 | Industrials | large | unknown | 2026-08-23 |
| PCG | $17.61 | 33,610,232 | Utilities | large | unknown | 2026-08-23 |
| PEP | $143.47 | 34,120,278 | Consumer Staples | large | unknown | 2026-08-23 |
| PFE | $28.07 | 64,075,036 | Health Care | large | unknown | 2026-08-23 |
| PG | $144.72 | 68,888,208 | Consumer Staples | large | unknown | 2026-08-23 |
| PGR | $219.33 | 30,208,738 | Financials | large | unknown | 2026-08-23 |
| PH | $1001.97 | 41,469,279 | Industrials | large | unknown | 2026-08-23 |
| PINS | $23.40 | 20,027,530 | Unknown | mid | unknown | 2026-08-23 |
| PLD | $141.81 | 26,266,694 | Real Estate | large | unknown | 2026-08-23 |
| PLTR | $179.94 | 235,690,481 | Unknown | large | unknown | 2026-08-23 |
| PM | $188.28 | 38,981,449 | Consumer Staples | large | unknown | 2026-08-23 |
| PSX | $242.88 | 31,844,882 | Energy | large | unknown | 2026-08-23 |
| PWR | $639.42 | 55,519,792 | Industrials | large | unknown | 2026-08-23 |
| PYPL | $61.56 | 35,940,629 | Financials | large | unknown | 2026-08-23 |
| QCOM | $160.73 | 66,010,733 | Information Technology | large | unknown | 2026-08-23 |
| RCL | $291.92 | 33,305,314 | Consumer Discretionary | large | unknown | 2026-08-23 |
| RDDT | $153.28 | 53,823,979 | Unknown | large | unknown | 2026-08-23 |
| REGN | $833.92 | 29,148,882 | Health Care | large | unknown | 2026-08-23 |
| ROK | $437.64 | 25,917,022 | Industrials | large | unknown | 2026-08-23 |
| ROST | $239.04 | 39,667,135 | Consumer Discretionary | large | unknown | 2026-08-23 |
| RRX | $166.19 | 21,072,319 | Unknown | mid | unknown | 2026-08-23 |
| RTX | $209.88 | 44,892,273 | Industrials | large | unknown | 2026-08-23 |
| SBUX | $107.07 | 28,711,995 | Consumer Discretionary | large | unknown | 2026-08-23 |
| SCHW | $112.29 | 40,320,149 | Financials | large | unknown | 2026-08-23 |
| SHW | $346.79 | 31,943,323 | Materials | large | unknown | 2026-08-23 |
| SLB | $53.88 | 34,084,823 | Energy | large | unknown | 2026-08-23 |
| SMCI | $37.23 | 75,867,706 | Information Technology | large | unknown | 2026-08-23 |
| SNDK | $1596.37 | 591,422,405 | Unknown | large | unknown | 2026-08-23 |
| SNPS | $397.95 | 31,397,214 | Information Technology | large | unknown | 2026-08-23 |
| SO | $88.96 | 23,237,017 | Utilities | large | unknown | 2026-08-23 |
| SPGI | $431.04 | 49,504,727 | Financials | large | unknown | 2026-08-23 |
| STRL | $516.65 | 26,924,646 | Unknown | mid | unknown | 2026-08-23 |
| STX | $850.31 | 189,252,997 | Information Technology | large | unknown | 2026-08-23 |
| SYK | $329.31 | 44,700,578 | Health Care | large | unknown | 2026-08-23 |
| T | $25.31 | 61,848,770 | Communication Services | large | unknown | 2026-08-23 |
| TDG | $1200.37 | 46,341,757 | Industrials | large | unknown | 2026-08-23 |
| TEL | $203.52 | 33,784,251 | Information Technology | large | unknown | 2026-08-23 |
| TER | $375.94 | 61,051,194 | Information Technology | large | unknown | 2026-08-23 |
| TFC | $50.42 | 20,572,817 | Financials | large | unknown | 2026-08-23 |
| TGT | $165.46 | 34,411,477 | Consumer Discretionary | large | unknown | 2026-08-23 |
| TJX | $140.42 | 43,481,858 | Consumer Discretionary | large | unknown | 2026-08-23 |
| TLN | $314.26 | 22,115,682 | Unknown | mid | unknown | 2026-08-23 |
| TMO | $629.32 | 69,625,882 | Health Care | large | unknown | 2026-08-23 |
| TMUS | $182.98 | 35,558,331 | Communication Services | large | unknown | 2026-08-23 |
| TOST | $36.64 | 23,469,442 | Unknown | mid | unknown | 2026-08-23 |
| TPR | $130.27 | 23,764,535 | Consumer Discretionary | large | unknown | 2026-08-23 |
| TRGP | $299.07 | 22,696,865 | Unknown | large | unknown | 2026-08-23 |
| TRV | $363.60 | 27,909,931 | Financials | large | unknown | 2026-08-23 |
| TSCO | $34.98 | 33,503,334 | Consumer Discretionary | large | unknown | 2026-08-23 |
| TSLA | $362.78 | 281,159,072 | Consumer Discretionary | large | unknown | 2026-08-23 |
| TT | $453.47 | 31,617,988 | Industrials | large | unknown | 2026-08-23 |
| TTMI | $110.54 | 25,232,123 | Information Technology | mid | unknown | 2026-08-23 |
| TTWO | $239.60 | 27,440,410 | Communication Services | large | unknown | 2026-08-23 |
| TWLO | $225.35 | 32,190,744 | Unknown | mid | unknown | 2026-08-23 |
| TXN | $264.28 | 76,611,195 | Information Technology | large | unknown | 2026-08-23 |
| UBER | $78.79 | 82,034,093 | Unknown | large | unknown | 2026-08-23 |
| UNH | $390.12 | 78,839,040 | Health Care | large | unknown | 2026-08-23 |
| UNP | $308.20 | 39,208,408 | Industrials | large | unknown | 2026-08-23 |
| UPS | $102.02 | 23,570,919 | Industrials | large | unknown | 2026-08-23 |
| URI | $1097.51 | 33,375,756 | Industrials | large | unknown | 2026-08-23 |
| USB | $62.05 | 25,812,528 | Financials | large | unknown | 2026-08-23 |
| V | $371.08 | 104,311,531 | Financials | large | unknown | 2026-08-23 |
| VEEV | $248.01 | 20,266,549 | Unknown | large | unknown | 2026-08-23 |
| VLO | $348.81 | 38,119,640 | Energy | large | unknown | 2026-08-23 |
| VMC | $275.98 | 20,465,860 | Materials | large | unknown | 2026-08-23 |
| VRSK | $187.45 | 21,604,878 | Industrials | large | unknown | 2026-08-23 |
| VRT | $262.00 | 85,947,250 | Unknown | large | unknown | 2026-08-23 |
| VRTX | $548.03 | 31,022,568 | Health Care | large | unknown | 2026-08-23 |
| VST | $136.21 | 33,821,558 | Utilities | large | unknown | 2026-08-23 |
| VZ | $49.45 | 66,708,199 | Communication Services | large | unknown | 2026-08-23 |
| WAT | $410.73 | 23,179,805 | Health Care | large | unknown | 2026-08-23 |
| WBD | $28.56 | 41,881,496 | Communication Services | large | unknown | 2026-08-23 |
| WBS | $77.57 | 36,681,735 | Unknown | mid | unknown | 2026-08-23 |
| WDAY | $200.03 | 47,435,996 | Unknown | large | unknown | 2026-08-23 |
| WDC | $459.38 | 166,442,838 | Information Technology | large | unknown | 2026-08-23 |
| WELL | $239.28 | 33,001,893 | Real Estate | large | unknown | 2026-08-23 |
| WFC | $83.84 | 48,302,908 | Financials | large | unknown | 2026-08-23 |
| WM | $224.02 | 24,240,301 | Industrials | large | unknown | 2026-08-23 |
| WMB | $70.53 | 26,615,190 | Energy | large | unknown | 2026-08-23 |
| WMT | $103.70 | 124,554,069 | Consumer Staples | large | unknown | 2026-08-23 |
| XEL | $76.31 | 22,266,890 | Utilities | large | unknown | 2026-08-23 |
| XOM | $165.09 | 70,437,763 | Energy | large | unknown | 2026-08-23 |
| XYZ | $82.17 | 28,162,875 | Unknown | large | unknown | 2026-08-23 |
| YUM | $152.97 | 20,293,277 | Consumer Discretionary | large | unknown | 2026-08-23 |
| ZTS | $77.74 | 23,486,344 | Health Care | large | unknown | 2026-08-23 |
