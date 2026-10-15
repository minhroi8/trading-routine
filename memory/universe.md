---
screened_on: 2026-10-15
expires_on: 2026-10-22
total_passed: 261
total_rejected: 1235
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
| A | $173.94 | $23,468,897 | Health Care | large | unknown | 2026-10-15 |
| AAL | $11.79 | $28,739,192 | Industrials | mid | unknown | 2026-10-15 |
| AAPL | $343.01 | $377,830,615 | Information Technology | large | unknown | 2026-10-15 |
| ABBV | $283.55 | $47,191,946 | Health Care | large | unknown | 2026-10-15 |
| ABNB | $167.15 | $38,871,520 | Consumer Discretionary | large | unknown | 2026-10-15 |
| ABT | $102.99 | $41,490,333 | Health Care | large | unknown | 2026-10-15 |
| ACN | $214.99 | $70,027,571 | Information Technology | large | unknown | 2026-10-15 |
| ADBE | $240.78 | $38,127,442 | Information Technology | large | unknown | 2026-10-15 |
| ADI | $403.56 | $42,265,055 | Information Technology | large | unknown | 2026-10-15 |
| ADP | $280.48 | $25,343,252 | Industrials | large | unknown | 2026-10-15 |
| ADSK | $231.21 | $28,194,716 | Information Technology | large | unknown | 2026-10-15 |
| AKAM | $91.66 | $28,002,893 | Information Technology | large | unknown | 2026-10-15 |
| ALL | $236.15 | $31,260,160 | Financials | large | unknown | 2026-10-15 |
| AMAT | $446.63 | $133,242,217 | Information Technology | large | unknown | 2026-10-15 |
| AMD | $570.96 | $341,095,197 | Information Technology | large | unknown | 2026-10-15 |
| AMGN | $426.27 | $49,370,773 | Health Care | large | unknown | 2026-10-15 |
| AMT | $179.47 | $23,948,314 | Real Estate | large | unknown | 2026-10-15 |
| AMZN | $254.18 | $279,808,904 | Consumer Discretionary | large | unknown | 2026-10-15 |
| ANET | $195.44 | $49,531,948 | Information Technology | large | unknown | 2026-10-15 |
| AON | $275.35 | $31,279,255 | Financials | large | unknown | 2026-10-15 |
| APH | $82.66 | $46,047,536 | Information Technology | large | unknown | 2026-10-15 |
| APO | $113.39 | $24,327,312 | Financials | large | unknown | 2026-10-15 |
| APP | $262.28 | $58,993,336 | Information Technology | large | unknown | 2026-10-15 |
| AVGO | $346.34 | $240,077,058 | Information Technology | large | unknown | 2026-10-15 |
| AXP | $306.82 | $41,670,271 | Financials | large | unknown | 2026-10-15 |
| AZO | $2912.18 | $62,836,768 | Consumer Discretionary | large | unknown | 2026-10-15 |
| BA | $184.58 | $64,839,599 | Industrials | large | unknown | 2026-10-15 |
| BAC | $51.41 | $148,049,782 | Financials | large | unknown | 2026-10-15 |
| BKNG | $160.68 | $91,784,823 | Consumer Discretionary | large | unknown | 2026-10-15 |
| BKR | $55.38 | $20,547,404 | Energy | large | unknown | 2026-10-15 |
| BLK | $1074.88 | $33,930,686 | Financials | large | unknown | 2026-10-15 |
| BMY | $59.28 | $53,793,440 | Health Care | large | unknown | 2026-10-15 |
| BRK.B | $526.55 | $81,418,445 | Financials | large | unknown | 2026-10-15 |
| BSX | $43.01 | $57,113,595 | Health Care | large | unknown | 2026-10-15 |
| BURL | $263.20 | $26,543,370 | Consumer Discretionary | mid | unknown | 2026-10-15 |
| BX | $106.19 | $26,306,870 | Financials | large | unknown | 2026-10-15 |
| C | $122.26 | $55,035,402 | Financials | large | unknown | 2026-10-15 |
| CASY | $653.25 | $21,797,490 | Consumer Staples | large | unknown | 2026-10-15 |
| CAT | $748.38 | $82,048,549 | Industrials | large | unknown | 2026-10-15 |
| CB | $350.30 | $23,142,193 | Financials | large | unknown | 2026-10-15 |
| CBOE | $300.97 | $21,298,486 | Financials | large | unknown | 2026-10-15 |
| CCL | $25.98 | $38,469,131 | Consumer Discretionary | large | unknown | 2026-10-15 |
| CDE | $14.99 | $24,409,207 | Materials | mid | unknown | 2026-10-15 |
| CDNS | $329.51 | $44,592,884 | Information Technology | large | unknown | 2026-10-15 |
| CEG | $279.66 | $43,707,430 | Utilities | large | unknown | 2026-10-15 |
| CI | $289.55 | $20,319,905 | Health Care | large | unknown | 2026-10-15 |
| CIEN | $359.42 | $53,567,850 | Information Technology | large | unknown | 2026-10-15 |
| CL | $92.82 | $23,524,698 | Consumer Staples | large | unknown | 2026-10-15 |
| CMCSA | $21.06 | $39,106,028 | Communication Services | large | unknown | 2026-10-15 |
| CME | $285.62 | $24,539,909 | Financials | large | unknown | 2026-10-15 |
| CMG | $30.52 | $42,020,574 | Consumer Discretionary | large | unknown | 2026-10-15 |
| CMI | $526.00 | $31,258,606 | Industrials | large | unknown | 2026-10-15 |
| CNP | $39.69 | $21,317,695 | Utilities | large | unknown | 2026-10-15 |
| COF | $194.40 | $34,026,090 | Financials | large | unknown | 2026-10-15 |
| COHR | $263.24 | $80,954,240 | Information Technology | large | unknown | 2026-10-15 |
| COIN | $172.87 | $47,371,284 | Financials | large | unknown | 2026-10-15 |
| COP | $142.33 | $35,260,841 | Energy | large | unknown | 2026-10-15 |
| COR | $336.10 | $21,216,194 | Health Care | large | unknown | 2026-10-15 |
| COST | $982.38 | $87,732,399 | Consumer Staples | large | unknown | 2026-10-15 |
| CRH | $79.19 | $21,774,275 | Materials | large | unknown | 2026-10-15 |
| CRL | $301.90 | $21,168,896 | Health Care | large | unknown | 2026-10-15 |
| CRM | $236.03 | $86,053,117 | Information Technology | large | unknown | 2026-10-15 |
| CRWD | $249.35 | $78,174,497 | Information Technology | large | unknown | 2026-10-15 |
| CSCO | $113.67 | $77,462,693 | Information Technology | large | unknown | 2026-10-15 |
| CSX | $48.31 | $41,042,951 | Industrials | large | unknown | 2026-10-15 |
| CTSH | $62.51 | $20,135,954 | Information Technology | large | unknown | 2026-10-15 |
| CTVA | $13.40 | $21,635,355 | Materials | large | unknown | 2026-10-15 |
| CVNA | $58.03 | $26,982,444 | Consumer Discretionary | large | unknown | 2026-10-15 |
| CVS | $90.44 | $47,996,319 | Health Care | large | unknown | 2026-10-15 |
| CVX | $222.09 | $65,017,575 | Energy | large | unknown | 2026-10-15 |
| D | $62.81 | $24,183,548 | Utilities | large | unknown | 2026-10-15 |
| DAL | $76.66 | $30,401,587 | Industrials | large | unknown | 2026-10-15 |
| DASH | $183.93 | $46,829,747 | Consumer Discretionary | large | unknown | 2026-10-15 |
| DDOG | $269.29 | $43,994,894 | Information Technology | large | unknown | 2026-10-15 |
| DE | $651.12 | $44,375,862 | Industrials | large | unknown | 2026-10-15 |
| DELL | $507.38 | $107,095,754 | Information Technology | large | unknown | 2026-10-15 |
| DHI | $133.65 | $23,815,617 | Consumer Discretionary | large | unknown | 2026-10-15 |
| DHR | $224.74 | $59,343,782 | Health Care | large | unknown | 2026-10-15 |
| DIS | $109.01 | $45,126,754 | Communication Services | large | unknown | 2026-10-15 |
| DKS | $136.98 | $22,491,586 | Consumer Discretionary | mid | unknown | 2026-10-15 |
| DT | $63.58 | $26,177,771 | Information Technology | mid | unknown | 2026-10-15 |
| DUK | $119.65 | $22,066,229 | Utilities | large | unknown | 2026-10-15 |
| DVN | $49.92 | $37,846,646 | Energy | large | unknown | 2026-10-15 |
| ELV | $428.10 | $27,509,775 | Health Care | large | unknown | 2026-10-15 |
| EMR | $160.97 | $20,569,028 | Industrials | large | unknown | 2026-10-15 |
| EOG | $154.17 | $20,262,902 | Energy | large | unknown | 2026-10-15 |
| EQIX | $995.82 | $29,889,253 | Real Estate | large | unknown | 2026-10-15 |
| EQT | $52.77 | $25,490,150 | Energy | large | unknown | 2026-10-15 |
| ETN | $408.71 | $48,535,314 | Industrials | large | unknown | 2026-10-15 |
| EXPE | $274.77 | $34,041,882 | Consumer Discretionary | large | unknown | 2026-10-15 |
| F | $12.05 | $22,069,163 | Consumer Discretionary | large | unknown | 2026-10-15 |
| FANG | $197.55 | $31,249,334 | Energy | large | unknown | 2026-10-15 |
| FAST | $52.02 | $24,921,709 | Industrials | large | unknown | 2026-10-15 |
| FCX | $69.61 | $39,588,557 | Materials | large | unknown | 2026-10-15 |
| FDX | $291.22 | $21,689,367 | Industrials | large | unknown | 2026-10-15 |
| FICO | $719.53 | $36,589,656 | Information Technology | large | unknown | 2026-10-15 |
| FITB | $49.67 | $33,052,364 | Financials | large | unknown | 2026-10-15 |
| FIX | $1541.13 | $32,026,652 | Industrials | large | unknown | 2026-10-15 |
| FN | $393.28 | $23,568,265 | Information Technology | mid | unknown | 2026-10-15 |
| FTNT | $184.11 | $22,369,629 | Information Technology | large | unknown | 2026-10-15 |
| GD | $334.64 | $22,286,462 | Industrials | large | unknown | 2026-10-15 |
| GE | $307.05 | $55,160,201 | Industrials | large | unknown | 2026-10-15 |
| GEN | $23.80 | $20,910,371 | Information Technology | large | unknown | 2026-10-15 |
| GEV | $941.67 | $83,784,608 | Industrials | large | unknown | 2026-10-15 |
| GILD | $153.56 | $35,506,733 | Health Care | large | unknown | 2026-10-15 |
| GIS | $32.14 | $21,544,150 | Consumer Staples | large | unknown | 2026-10-15 |
| GLW | $140.93 | $47,299,835 | Information Technology | large | unknown | 2026-10-15 |
| GM | $83.02 | $42,719,766 | Consumer Discretionary | large | unknown | 2026-10-15 |
| GOOG | $343.76 | $137,281,612 | Communication Services | large | unknown | 2026-10-15 |
| GOOGL | $347.78 | $261,718,887 | Communication Services | large | unknown | 2026-10-15 |
| GS | $878.69 | $86,165,268 | Financials | large | unknown | 2026-10-15 |
| GWW | $1330.09 | $22,981,859 | Industrials | large | unknown | 2026-10-15 |
| HAL | $32.84 | $21,284,469 | Energy | large | unknown | 2026-10-15 |
| HBAN | $15.10 | $25,989,900 | Financials | large | unknown | 2026-10-15 |
| HCA | $470.46 | $27,406,206 | Health Care | large | unknown | 2026-10-15 |
| HD | $295.47 | $77,602,770 | Consumer Discretionary | large | unknown | 2026-10-15 |
| HLT | $328.01 | $33,302,508 | Consumer Discretionary | large | unknown | 2026-10-15 |
| HON | $207.66 | $20,165,410 | Industrials | large | unknown | 2026-10-15 |
| HOOD | $101.09 | $64,070,548 | Financials | large | unknown | 2026-10-15 |
| HPE | $63.17 | $59,790,478 | Information Technology | large | unknown | 2026-10-15 |
| HPQ | $30.46 | $29,132,636 | Information Technology | large | unknown | 2026-10-15 |
| HUM | $427.92 | $36,688,540 | Health Care | large | unknown | 2026-10-15 |
| HWM | $217.46 | $33,337,991 | Industrials | large | unknown | 2026-10-15 |
| IBM | $228.00 | $41,866,633 | Information Technology | large | unknown | 2026-10-15 |
| ICE | $155.12 | $23,400,774 | Financials | large | unknown | 2026-10-15 |
| INTC | $98.11 | $293,606,712 | Information Technology | large | unknown | 2026-10-15 |
| INTU | $310.51 | $48,807,914 | Information Technology | large | unknown | 2026-10-15 |
| IQV | $262.10 | $23,313,721 | Health Care | large | unknown | 2026-10-15 |
| IR | $77.93 | $20,988,203 | Industrials | large | unknown | 2026-10-15 |
| ISRG | $420.32 | $41,558,978 | Health Care | large | unknown | 2026-10-15 |
| JBL | $293.92 | $31,804,073 | Information Technology | large | unknown | 2026-10-15 |
| JCI | $152.43 | $23,494,580 | Industrials | large | unknown | 2026-10-15 |
| JNJ | $253.91 | $73,953,168 | Health Care | large | unknown | 2026-10-15 |
| JPM | $335.29 | $100,671,586 | Financials | large | unknown | 2026-10-15 |
| KDP | $33.13 | $25,069,535 | Consumer Staples | large | unknown | 2026-10-15 |
| KEYS | $357.33 | $21,415,960 | Information Technology | large | unknown | 2026-10-15 |
| KKR | $85.53 | $25,549,769 | Financials | large | unknown | 2026-10-15 |
| KLAC | $178.74 | $63,071,013 | Information Technology | large | unknown | 2026-10-15 |
| KMI | $33.38 | $26,436,194 | Energy | large | unknown | 2026-10-15 |
| KO | $91.81 | $90,361,172 | Consumer Staples | large | unknown | 2026-10-15 |
| KR | $63.09 | $31,423,508 | Consumer Staples | large | unknown | 2026-10-15 |
| KVUE | $18.00 | $24,934,266 | Consumer Staples | large | unknown | 2026-10-15 |
| LEN | $73.53 | $22,710,181 | Consumer Discretionary | large | unknown | 2026-10-15 |
| LIN | $492.81 | $50,528,607 | Materials | large | unknown | 2026-10-15 |
| LITE | $896.58 | $158,320,429 | Information Technology | large | unknown | 2026-10-15 |
| LLY | $1210.90 | $104,865,624 | Health Care | large | unknown | 2026-10-15 |
| LMT | $522.10 | $21,317,857 | Industrials | large | unknown | 2026-10-15 |
| LOW | $188.35 | $22,515,334 | Consumer Discretionary | large | unknown | 2026-10-15 |
| LRCX | $286.72 | $117,600,431 | Information Technology | large | unknown | 2026-10-15 |
| MA | $603.29 | $82,474,118 | Financials | large | unknown | 2026-10-15 |
| MAR | $371.95 | $21,169,784 | Consumer Discretionary | large | unknown | 2026-10-15 |
| MCD | $238.25 | $50,028,416 | Consumer Discretionary | large | unknown | 2026-10-15 |
| MCHP | $71.27 | $25,224,439 | Information Technology | large | unknown | 2026-10-15 |
| MCK | $978.24 | $32,945,006 | Health Care | large | unknown | 2026-10-15 |
| MDLZ | $62.59 | $29,596,767 | Consumer Staples | large | unknown | 2026-10-15 |
| MDT | $94.25 | $131,131,043 | Health Care | large | unknown | 2026-10-15 |
| META | $738.24 | $554,674,213 | Communication Services | large | unknown | 2026-10-15 |
| MLM | $470.71 | $25,497,410 | Materials | large | unknown | 2026-10-15 |
| MMM | $164.35 | $20,029,813 | Industrials | large | unknown | 2026-10-15 |
| MNST | $44.23 | $28,747,628 | Consumer Staples | large | unknown | 2026-10-15 |
| MO | $73.16 | $29,680,391 | Consumer Staples | large | unknown | 2026-10-15 |
| MPC | $484.80 | $47,405,980 | Energy | large | unknown | 2026-10-15 |
| MPWR | $1242.09 | $44,415,862 | Information Technology | large | unknown | 2026-10-15 |
| MRK | $147.50 | $53,135,118 | Health Care | large | unknown | 2026-10-15 |
| MRNA | $225.56 | $96,900,470 | Health Care | large | unknown | 2026-10-15 |
| MRSH | $178.43 | $22,283,884 | Financials | large | unknown | 2026-10-15 |
| MS | $181.58 | $57,356,068 | Financials | large | unknown | 2026-10-15 |
| MSFT | $534.04 | $375,515,561 | Information Technology | large | unknown | 2026-10-15 |
| MSI | $451.36 | $20,001,850 | Information Technology | large | unknown | 2026-10-15 |
| MTD | $1610.69 | $22,268,162 | Health Care | large | unknown | 2026-10-15 |
| MTSI | $291.50 | $23,102,067 | Information Technology | mid | unknown | 2026-10-15 |
| MTZ | $194.37 | $23,866,224 | Industrials | mid | unknown | 2026-10-15 |
| MU | $914.32 | $616,515,205 | Information Technology | large | unknown | 2026-10-15 |
| NEE | $78.41 | $62,703,851 | Utilities | large | unknown | 2026-10-15 |
| NEM | $111.53 | $26,616,863 | Materials | large | unknown | 2026-10-15 |
| NFLX | $70.58 | $135,392,510 | Communication Services | large | unknown | 2026-10-15 |
| NKE | $35.32 | $74,582,063 | Consumer Discretionary | large | unknown | 2026-10-15 |
| NOC | $495.63 | $28,170,266 | Industrials | large | unknown | 2026-10-15 |
| NOW | $139.93 | $57,418,934 | Information Technology | large | unknown | 2026-10-15 |
| NTAP | $222.25 | $30,117,530 | Information Technology | large | unknown | 2026-10-15 |
| NVDA | $221.49 | $650,881,822 | Information Technology | large | unknown | 2026-10-15 |
| NXPI | $220.87 | $25,089,964 | Information Technology | large | unknown | 2026-10-15 |
| O | $55.18 | $28,198,226 | Real Estate | large | unknown | 2026-10-15 |
| OKTA | $211.84 | $36,233,419 | Information Technology | mid | unknown | 2026-10-15 |
| ON | $73.33 | $37,367,015 | Information Technology | large | unknown | 2026-10-15 |
| ORCL | $130.56 | $125,907,634 | Information Technology | large | unknown | 2026-10-15 |
| OXY | $61.42 | $39,140,589 | Energy | large | unknown | 2026-10-15 |
| PANW | $374.90 | $80,012,366 | Information Technology | large | unknown | 2026-10-15 |
| PCAR | $108.58 | $20,519,937 | Industrials | large | unknown | 2026-10-15 |
| PCG | $13.16 | $29,590,647 | Utilities | large | unknown | 2026-10-15 |
| PEG | $70.57 | $21,338,362 | Utilities | large | unknown | 2026-10-15 |
| PEP | $129.34 | $53,284,494 | Consumer Staples | large | unknown | 2026-10-15 |
| PFE | $29.23 | $44,640,971 | Health Care | large | unknown | 2026-10-15 |
| PG | $156.56 | $44,987,101 | Consumer Staples | large | unknown | 2026-10-15 |
| PGR | $213.59 | $41,960,357 | Financials | large | unknown | 2026-10-15 |
| PH | $956.78 | $27,448,263 | Industrials | large | unknown | 2026-10-15 |
| PLD | $130.56 | $21,062,176 | Real Estate | large | unknown | 2026-10-15 |
| PLTR | $200.97 | $103,032,972 | Information Technology | large | unknown | 2026-10-15 |
| PM | $205.60 | $34,430,410 | Consumer Staples | large | unknown | 2026-10-15 |
| PSX | $297.35 | $54,384,951 | Energy | large | unknown | 2026-10-15 |
| PTC | $193.59 | $42,023,415 | Information Technology | large | unknown | 2026-10-15 |
| PWR | $660.59 | $35,896,239 | Industrials | large | unknown | 2026-10-15 |
| PYPL | $56.12 | $26,079,563 | Financials | large | unknown | 2026-10-15 |
| QCOM | $172.71 | $66,621,709 | Information Technology | large | unknown | 2026-10-15 |
| RCL | $274.35 | $50,075,070 | Consumer Discretionary | large | unknown | 2026-10-15 |
| REGN | $778.86 | $28,406,984 | Health Care | large | unknown | 2026-10-15 |
| ROST | $230.66 | $23,002,620 | Consumer Discretionary | large | unknown | 2026-10-15 |
| RTX | $186.43 | $30,680,997 | Industrials | large | unknown | 2026-10-15 |
| SBUX | $93.31 | $38,198,513 | Consumer Discretionary | large | unknown | 2026-10-15 |
| SCHW | $96.78 | $42,248,201 | Financials | large | unknown | 2026-10-15 |
| SHW | $324.51 | $23,112,858 | Materials | large | unknown | 2026-10-15 |
| SLB | $48.54 | $42,293,143 | Energy | large | unknown | 2026-10-15 |
| SMCI | $35.80 | $58,793,401 | Information Technology | large | unknown | 2026-10-15 |
| SMTC | $160.29 | $30,607,178 | Information Technology | mid | unknown | 2026-10-15 |
| SNDK | $1403.36 | $312,672,439 | Information Technology | large | unknown | 2026-10-15 |
| SNPS | $479.92 | $54,762,556 | Information Technology | large | unknown | 2026-10-15 |
| SO | $89.37 | $23,529,120 | Utilities | large | unknown | 2026-10-15 |
| SPGI | $408.61 | $32,958,218 | Financials | large | unknown | 2026-10-15 |
| STT | $166.79 | $22,365,301 | Financials | large | unknown | 2026-10-15 |
| STX | $713.12 | $159,958,968 | Information Technology | large | unknown | 2026-10-15 |
| SWKS | $76.89 | $26,478,154 | Information Technology | large | unknown | 2026-10-15 |
| SYK | $281.68 | $41,016,966 | Health Care | large | unknown | 2026-10-15 |
| T | $23.09 | $54,544,675 | Communication Services | large | unknown | 2026-10-15 |
| TDG | $1109.12 | $25,562,106 | Industrials | large | unknown | 2026-10-15 |
| TEL | $210.30 | $20,434,534 | Information Technology | large | unknown | 2026-10-15 |
| TER | $359.29 | $36,862,178 | Information Technology | large | unknown | 2026-10-15 |
| TFC | $45.59 | $25,447,404 | Financials | large | unknown | 2026-10-15 |
| TGT | $155.22 | $28,702,790 | Consumer Staples | large | unknown | 2026-10-15 |
| TJX | $142.83 | $63,980,371 | Consumer Discretionary | large | unknown | 2026-10-15 |
| TLN | $358.28 | $25,402,633 | Utilities | mid | unknown | 2026-10-15 |
| TMO | $673.27 | $93,109,914 | Health Care | large | unknown | 2026-10-15 |
| TMUS | $157.84 | $51,024,632 | Communication Services | large | unknown | 2026-10-15 |
| TSCO | $32.74 | $21,652,420 | Consumer Discretionary | large | unknown | 2026-10-15 |
| TSLA | $367.41 | $239,227,148 | Consumer Discretionary | large | unknown | 2026-10-15 |
| TT | $471.30 | $39,646,022 | Industrials | large | unknown | 2026-10-15 |
| TTWO | $201.23 | $27,495,314 | Communication Services | large | unknown | 2026-10-15 |
| TXN | $280.71 | $59,909,422 | Information Technology | large | unknown | 2026-10-15 |
| UAL | $98.90 | $23,275,267 | Industrials | large | unknown | 2026-10-15 |
| UBER | $69.31 | $48,664,616 | Industrials | large | unknown | 2026-10-15 |
| UNH | $395.69 | $91,943,535 | Health Care | large | unknown | 2026-10-15 |
| UNP | $286.55 | $33,721,110 | Industrials | large | unknown | 2026-10-15 |
| URI | $1034.24 | $35,168,712 | Industrials | large | unknown | 2026-10-15 |
| USB | $56.29 | $32,532,860 | Financials | large | unknown | 2026-10-15 |
| UTHR | $540.05 | $31,050,033 | Health Care | mid | unknown | 2026-10-15 |
| V | $391.42 | $91,242,791 | Financials | large | unknown | 2026-10-15 |
| VLO | $459.90 | $67,937,507 | Energy | large | unknown | 2026-10-15 |
| VRT | $222.84 | $56,203,380 | Industrials | large | unknown | 2026-10-15 |
| VRTX | $500.06 | $26,418,207 | Health Care | large | unknown | 2026-10-15 |
| VST | $151.77 | $43,351,956 | Utilities | large | unknown | 2026-10-15 |
| VZ | $44.42 | $65,137,886 | Communication Services | large | unknown | 2026-10-15 |
| WAT | $436.92 | $23,331,342 | Health Care | large | unknown | 2026-10-15 |
| WBD | $30.97 | $102,720,922 | Communication Services | large | unknown | 2026-10-15 |
| WDC | $364.06 | $141,277,435 | Information Technology | large | unknown | 2026-10-15 |
| WELL | $232.22 | $38,457,497 | Real Estate | large | unknown | 2026-10-15 |
| WFC | $80.89 | $74,576,945 | Financials | large | unknown | 2026-10-15 |
| WM | $215.73 | $21,486,606 | Industrials | large | unknown | 2026-10-15 |
| WMB | $72.81 | $27,815,583 | Energy | large | unknown | 2026-10-15 |
| WMT | $116.20 | $88,196,144 | Consumer Staples | large | unknown | 2026-10-15 |
| XEL | $75.39 | $24,767,177 | Utilities | large | unknown | 2026-10-15 |
| XOM | $176.97 | $62,589,644 | Energy | large | unknown | 2026-10-15 |
| YUM | $146.68 | $22,138,271 | Consumer Discretionary | large | unknown | 2026-10-15 |
