---
screened_on: 2026-08-02
expires_on: 2026-08-09
total_passed: 286
total_rejected: 1214
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
| AAL | $15.26 | $51,643,992 | Industrials | mid | unknown | 2026-08-02 |
| AAPL | $308.73 | $604,407,399 | Information Technology | large | unknown | 2026-08-02 |
| ABBV | $250.88 | $71,156,264 | Health Care | large | unknown | 2026-08-02 |
| ABNB | $151.42 | $21,274,043 | Consumer Discretionary | large | unknown | 2026-08-02 |
| ABT | $105.72 | $72,771,335 | Health Care | large | unknown | 2026-08-02 |
| ACN | $165.97 | $62,544,661 | Information Technology | large | unknown | 2026-08-02 |
| ADBE | $250.36 | $62,313,821 | Information Technology | large | unknown | 2026-08-02 |
| ADI | $367.49 | $57,149,821 | Information Technology | large | unknown | 2026-08-02 |
| ADP | $266.55 | $27,232,073 | Industrials | large | unknown | 2026-08-02 |
| ADSK | $234.31 | $24,017,178 | Information Technology | large | unknown | 2026-08-02 |
| AEP | $127.86 | $24,691,781 | Utilities | large | unknown | 2026-08-02 |
| AJG | $249.42 | $21,821,268 | Financials | large | unknown | 2026-08-02 |
| AKAM | $115.15 | $22,598,025 | Information Technology | large | unknown | 2026-08-02 |
| AMAT | $508.08 | $214,624,308 | Information Technology | large | unknown | 2026-08-02 |
| AMD | $476.03 | $372,562,621 | Information Technology | large | unknown | 2026-08-02 |
| AMGN | $385.21 | $31,242,212 | Health Care | large | unknown | 2026-08-02 |
| AMT | $173.40 | $29,536,967 | Real Estate | large | unknown | 2026-08-02 |
| AMZN | $271.46 | $520,549,932 | Consumer Discretionary | large | unknown | 2026-08-02 |
| ANET | $180.32 | $68,799,185 | Information Technology | large | unknown | 2026-08-02 |
| AON | $360.68 | $25,086,646 | Financials | large | unknown | 2026-08-02 |
| APH | $160.71 | $58,673,816 | Information Technology | large | unknown | 2026-08-02 |
| APO | $125.64 | $26,876,496 | Financials | large | unknown | 2026-08-02 |
| APP | $395.81 | $83,204,965 | Information Technology | large | unknown | 2026-08-02 |
| AVGO | $389.30 | $238,423,523 | Information Technology | large | unknown | 2026-08-02 |
| AXON | $527.38 | $22,277,709 | Industrials | large | unknown | 2026-08-02 |
| AXP | $336.23 | $53,345,381 | Financials | large | unknown | 2026-08-02 |
| AZO | $3019.77 | $37,302,108 | Consumer Discretionary | large | unknown | 2026-08-02 |
| BA | $216.20 | $52,809,063 | Industrials | large | unknown | 2026-08-02 |
| BAC | $61.98 | $148,290,187 | Financials | large | unknown | 2026-08-02 |
| BKNG | $192.88 | $50,315,538 | Consumer Discretionary | large | unknown | 2026-08-02 |
| BKR | $60.48 | $40,106,711 | Energy | large | unknown | 2026-08-02 |
| BLK | $1090.16 | $62,840,422 | Financials | large | unknown | 2026-08-02 |
| BMY | $65.30 | $44,902,577 | Health Care | large | unknown | 2026-08-02 |
| BRK.B | $511.42 | $59,724,183 | Financials | large | unknown | 2026-08-02 |
| BSX | $46.73 | $62,048,568 | Health Care | large | unknown | 2026-08-02 |
| BX | $127.75 | $28,181,439 | Financials | large | unknown | 2026-08-02 |
| C | $132.43 | $74,243,335 | Financials | large | unknown | 2026-08-02 |
| CAH | $230.01 | $25,084,328 | Health Care | large | unknown | 2026-08-02 |
| CARR | $61.81 | $27,787,075 | Industrials | large | unknown | 2026-08-02 |
| CAT | $814.55 | $126,958,822 | Industrials | large | unknown | 2026-08-02 |
| CB | $350.88 | $36,868,576 | Financials | large | unknown | 2026-08-02 |
| CCL | $27.82 | $31,315,877 | Consumer Discretionary | large | unknown | 2026-08-02 |
| CDNS | $339.98 | $49,107,125 | Information Technology | large | unknown | 2026-08-02 |
| CEG | $262.75 | $40,746,004 | Utilities | large | unknown | 2026-08-02 |
| CFG | $71.63 | $29,019,134 | Financials | large | unknown | 2026-08-02 |
| CHRW | $147.75 | $28,779,507 | Industrials | large | unknown | 2026-08-02 |
| CHTR | $144.90 | $22,731,032 | Communication Services | large | unknown | 2026-08-02 |
| CI | $279.03 | $26,387,404 | Health Care | large | unknown | 2026-08-02 |
| CL | $91.30 | $21,464,708 | Consumer Staples | large | unknown | 2026-08-02 |
| CMCSA | $23.96 | $46,617,988 | Communication Services | large | unknown | 2026-08-02 |
| CME | $267.83 | $42,976,349 | Financials | large | unknown | 2026-08-02 |
| CMG | $37.25 | $49,553,337 | Consumer Discretionary | large | unknown | 2026-08-02 |
| CMI | $634.29 | $35,323,603 | Industrials | large | unknown | 2026-08-02 |
| CNP | $42.05 | $21,520,840 | Utilities | large | unknown | 2026-08-02 |
| COF | $209.08 | $46,206,980 | Financials | large | unknown | 2026-08-02 |
| COIN | $146.25 | $35,160,870 | Financials | large | unknown | 2026-08-02 |
| COP | $120.48 | $42,448,825 | Energy | large | unknown | 2026-08-02 |
| COR | $311.93 | $24,352,232 | Health Care | large | unknown | 2026-08-02 |
| COST | $951.61 | $69,650,211 | Consumer Staples | large | unknown | 2026-08-02 |
| CPRT | $29.13 | $25,986,914 | Industrials | large | unknown | 2026-08-02 |
| CRH | $95.00 | $21,424,140 | Materials | large | unknown | 2026-08-02 |
| CRM | $184.00 | $86,981,392 | Information Technology | large | unknown | 2026-08-02 |
| CRS | $519.82 | $28,559,563 | Industrials | mid | unknown | 2026-08-02 |
| CRWD | $190.86 | $56,948,441 | Information Technology | large | unknown | 2026-08-02 |
| CSCO | $116.00 | $105,454,025 | Information Technology | large | unknown | 2026-08-02 |
| CSX | $50.38 | $50,347,459 | Industrials | large | unknown | 2026-08-02 |
| CTAS | $204.59 | $25,273,288 | Industrials | large | unknown | 2026-08-02 |
| CTSH | $55.33 | $33,993,974 | Information Technology | large | unknown | 2026-08-02 |
| CVNA | $62.36 | $37,546,980 | Consumer Discretionary | large | unknown | 2026-08-02 |
| CVS | $104.42 | $39,648,514 | Health Care | large | unknown | 2026-08-02 |
| CVX | $196.85 | $54,336,905 | Energy | large | unknown | 2026-08-02 |
| D | $69.19 | $30,239,235 | Utilities | large | unknown | 2026-08-02 |
| DAL | $87.42 | $31,134,847 | Industrials | large | unknown | 2026-08-02 |
| DASH | $196.26 | $40,169,872 | Consumer Discretionary | large | unknown | 2026-08-02 |
| DDOG | $267.97 | $60,005,820 | Information Technology | large | unknown | 2026-08-02 |
| DE | $592.66 | $35,213,869 | Industrials | large | unknown | 2026-08-02 |
| DELL | $405.27 | $108,255,509 | Information Technology | large | unknown | 2026-08-02 |
| DHR | $195.01 | $87,242,205 | Health Care | large | unknown | 2026-08-02 |
| DIS | $96.23 | $54,101,007 | Communication Services | large | unknown | 2026-08-02 |
| DLR | $188.51 | $33,807,967 | Real Estate | large | unknown | 2026-08-02 |
| DOCN | $117.51 | $22,621,134 | Information Technology | mid | unknown | 2026-08-02 |
| DOW | $30.30 | $24,431,594 | Materials | large | unknown | 2026-08-02 |
| DRI | $203.87 | $20,194,524 | Consumer Discretionary | large | unknown | 2026-08-02 |
| DVN | $45.13 | $36,264,500 | Energy | large | unknown | 2026-08-02 |
| DXCM | $83.46 | $22,626,471 | Health Care | large | unknown | 2026-08-02 |
| EA | $209.89 | $30,771,796 | Communication Services | large | unknown | 2026-08-02 |
| EFX | $172.79 | $23,660,406 | Industrials | large | unknown | 2026-08-02 |
| ELV | $375.86 | $30,549,654 | Health Care | large | unknown | 2026-08-02 |
| EME | $797.79 | $23,395,790 | Industrials | large | unknown | 2026-08-02 |
| EMR | $149.82 | $20,200,749 | Industrials | large | unknown | 2026-08-02 |
| ENTG | $119.01 | $21,878,129 | Information Technology | mid | unknown | 2026-08-02 |
| EQIX | $1019.28 | $43,804,447 | Real Estate | large | unknown | 2026-08-02 |
| EQT | $53.28 | $31,705,237 | Energy | large | unknown | 2026-08-02 |
| ETN | $415.36 | $52,736,022 | Industrials | large | unknown | 2026-08-02 |
| EW | $86.03 | $29,305,673 | Health Care | large | unknown | 2026-08-02 |
| EXC | $45.83 | $26,453,100 | Utilities | large | unknown | 2026-08-02 |
| EXPE | $294.81 | $20,398,579 | Consumer Discretionary | large | unknown | 2026-08-02 |
| F | $14.67 | $32,994,303 | Consumer Discretionary | large | unknown | 2026-08-02 |
| FAST | $47.72 | $29,003,928 | Industrials | large | unknown | 2026-08-02 |
| FCX | $62.62 | $57,416,318 | Materials | large | unknown | 2026-08-02 |
| FDX | $307.35 | $29,726,952 | Industrials | large | unknown | 2026-08-02 |
| FICO | $1122.97 | $29,939,055 | Information Technology | large | unknown | 2026-08-02 |
| FITB | $56.49 | $31,327,840 | Financials | large | unknown | 2026-08-02 |
| FIX | $1727.79 | $54,224,489 | Industrials | large | unknown | 2026-08-02 |
| FN | $435.69 | $32,345,442 | Information Technology | mid | unknown | 2026-08-02 |
| FSLR | $211.16 | $20,676,784 | Information Technology | large | unknown | 2026-08-02 |
| FTNT | $161.89 | $39,049,583 | Information Technology | large | unknown | 2026-08-02 |
| GE | $360.14 | $69,846,881 | Industrials | large | unknown | 2026-08-02 |
| GEHC | $68.03 | $21,512,152 | Health Care | large | unknown | 2026-08-02 |
| GEV | $990.15 | $159,696,996 | Industrials | large | unknown | 2026-08-02 |
| GILD | $130.19 | $37,982,550 | Health Care | large | unknown | 2026-08-02 |
| GIS | $35.77 | $26,893,354 | Consumer Staples | large | unknown | 2026-08-02 |
| GLW | $138.29 | $102,165,525 | Information Technology | large | unknown | 2026-08-02 |
| GM | $88.80 | $25,386,468 | Consumer Discretionary | large | unknown | 2026-08-02 |
| GOOG | $356.64 | $223,910,315 | Communication Services | large | unknown | 2026-08-02 |
| GOOGL | $356.06 | $365,692,121 | Communication Services | large | unknown | 2026-08-02 |
| GS | $1017.60 | $81,117,242 | Financials | large | unknown | 2026-08-02 |
| GWW | $1382.23 | $22,700,167 | Industrials | large | unknown | 2026-08-02 |
| HAL | $32.24 | $30,981,092 | Energy | large | unknown | 2026-08-02 |
| HBAN | $17.02 | $25,219,379 | Financials | large | unknown | 2026-08-02 |
| HCA | $402.67 | $44,587,107 | Health Care | large | unknown | 2026-08-02 |
| HD | $332.02 | $59,559,573 | Consumer Discretionary | large | unknown | 2026-08-02 |
| HLT | $320.49 | $40,865,613 | Consumer Discretionary | large | unknown | 2026-08-02 |
| HON | $243.09 | $36,317,438 | Industrials | large | unknown | 2026-08-02 |
| HOOD | $86.57 | $84,573,652 | Financials | large | unknown | 2026-08-02 |
| HPE | $47.88 | $52,795,822 | Information Technology | large | unknown | 2026-08-02 |
| HPQ | $27.27 | $28,858,608 | Information Technology | large | unknown | 2026-08-02 |
| HUBB | $472.32 | $20,429,656 | Industrials | large | unknown | 2026-08-02 |
| HUM | $363.85 | $31,094,724 | Health Care | large | unknown | 2026-08-02 |
| HWM | $282.40 | $25,590,585 | Industrials | large | unknown | 2026-08-02 |
| IBM | $223.80 | $124,396,430 | Information Technology | large | unknown | 2026-08-02 |
| ICE | $152.50 | $33,792,025 | Financials | large | unknown | 2026-08-02 |
| IDXX | $559.01 | $24,139,165 | Health Care | large | unknown | 2026-08-02 |
| ILMN | $205.10 | $23,679,038 | Health Care | mid | unknown | 2026-08-02 |
| INTC | $90.21 | $374,987,693 | Information Technology | large | unknown | 2026-08-02 |
| INTU | $316.12 | $80,822,831 | Information Technology | large | unknown | 2026-08-02 |
| IR | $83.40 | $20,950,962 | Industrials | large | unknown | 2026-08-02 |
| ISRG | $353.34 | $71,853,010 | Health Care | large | unknown | 2026-08-02 |
| ITW | $287.00 | $21,561,807 | Industrials | large | unknown | 2026-08-02 |
| JCI | $146.61 | $23,682,097 | Industrials | large | unknown | 2026-08-02 |
| JNJ | $256.46 | $103,755,267 | Health Care | large | unknown | 2026-08-02 |
| JPM | $351.86 | $91,932,976 | Financials | large | unknown | 2026-08-02 |
| KDP | $31.13 | $25,664,696 | Consumer Staples | large | unknown | 2026-08-02 |
| KEYS | $319.33 | $31,121,624 | Information Technology | large | unknown | 2026-08-02 |
| KHC | $25.86 | $22,316,123 | Consumer Staples | large | unknown | 2026-08-02 |
| KLAC | $182.68 | $117,578,991 | Information Technology | large | unknown | 2026-08-02 |
| KNX | $69.56 | $21,404,574 | Industrials | mid | unknown | 2026-08-02 |
| KO | $87.58 | $103,524,536 | Consumer Staples | large | unknown | 2026-08-02 |
| KR | $57.70 | $29,194,692 | Consumer Staples | large | unknown | 2026-08-02 |
| KVUE | $19.23 | $21,627,113 | Consumer Staples | large | unknown | 2026-08-02 |
| LHX | $277.09 | $22,669,730 | Industrials | large | unknown | 2026-08-02 |
| LII | $415.82 | $21,495,536 | Industrials | large | unknown | 2026-08-02 |
| LIN | $478.46 | $51,847,774 | Materials | large | unknown | 2026-08-02 |
| LLY | $1148.86 | $126,019,729 | Health Care | large | unknown | 2026-08-02 |
| LMT | $582.90 | $29,340,281 | Industrials | large | unknown | 2026-08-02 |
| LOW | $207.92 | $26,196,258 | Consumer Discretionary | large | unknown | 2026-08-02 |
| LRCX | $293.49 | $151,520,854 | Information Technology | large | unknown | 2026-08-02 |
| LYV | $174.19 | $22,144,767 | Communication Services | large | unknown | 2026-08-02 |
| MA | $573.41 | $97,052,332 | Financials | large | unknown | 2026-08-02 |
| MAR | $372.88 | $27,092,879 | Consumer Discretionary | large | unknown | 2026-08-02 |
| MCD | $270.63 | $50,907,683 | Consumer Discretionary | large | unknown | 2026-08-02 |
| MCHP | $74.28 | $31,201,029 | Information Technology | large | unknown | 2026-08-02 |
| MCK | $856.25 | $37,562,479 | Health Care | large | unknown | 2026-08-02 |
| MCO | $477.96 | $28,306,305 | Financials | large | unknown | 2026-08-02 |
| MDLZ | $62.31 | $38,107,000 | Consumer Staples | large | unknown | 2026-08-02 |
| MDT | $85.39 | $45,470,239 | Health Care | large | unknown | 2026-08-02 |
| META | $556.60 | $505,987,317 | Communication Services | large | unknown | 2026-08-02 |
| MKSI | $297.17 | $32,850,368 | Information Technology | mid | unknown | 2026-08-02 |
| MLM | $524.98 | $25,179,652 | Materials | large | unknown | 2026-08-02 |
| MMM | $176.28 | $30,519,248 | Industrials | large | unknown | 2026-08-02 |
| MNST | $96.38 | $25,165,181 | Consumer Staples | large | unknown | 2026-08-02 |
| MO | $68.28 | $30,659,799 | Consumer Staples | large | unknown | 2026-08-02 |
| MPC | $316.34 | $40,161,225 | Energy | large | unknown | 2026-08-02 |
| MPWR | $1424.59 | $66,082,764 | Information Technology | large | unknown | 2026-08-02 |
| MRK | $130.21 | $38,656,894 | Health Care | large | unknown | 2026-08-02 |
| MRSH | $189.72 | $21,204,946 | Financials | large | unknown | 2026-08-02 |
| MS | $210.56 | $70,266,835 | Financials | large | unknown | 2026-08-02 |
| MSCI | $573.03 | $34,366,853 | Financials | large | unknown | 2026-08-02 |
| MSFT | $464.70 | $580,691,578 | Information Technology | large | unknown | 2026-08-02 |
| MTD | $1416.08 | $20,192,215 | Health Care | large | unknown | 2026-08-02 |
| MTZ | $262.86 | $31,238,596 | Industrials | mid | unknown | 2026-08-02 |
| MU | $823.21 | $1,081,401,602 | Information Technology | large | unknown | 2026-08-02 |
| NEE | $86.95 | $57,512,792 | Utilities | large | unknown | 2026-08-02 |
| NEM | $93.71 | $30,386,388 | Materials | large | unknown | 2026-08-02 |
| NFLX | $71.69 | $224,153,076 | Communication Services | large | unknown | 2026-08-02 |
| NKE | $41.72 | $43,408,402 | Consumer Discretionary | large | unknown | 2026-08-02 |
| NOC | $542.47 | $32,189,642 | Industrials | large | unknown | 2026-08-02 |
| NOW | $111.26 | $111,830,907 | Information Technology | large | unknown | 2026-08-02 |
| NTAP | $178.60 | $21,600,866 | Information Technology | large | unknown | 2026-08-02 |
| NVDA | $200.74 | $996,233,560 | Information Technology | large | unknown | 2026-08-02 |
| NVT | $153.97 | $21,430,303 | Industrials | mid | unknown | 2026-08-02 |
| NXPI | $229.40 | $50,773,196 | Information Technology | large | unknown | 2026-08-02 |
| NXT | $89.83 | $20,047,341 | Industrials | mid | unknown | 2026-08-02 |
| ODFL | $212.09 | $22,090,217 | Industrials | large | unknown | 2026-08-02 |
| OKTA | $141.93 | $21,136,923 | Information Technology | mid | unknown | 2026-08-02 |
| ON | $81.58 | $37,244,805 | Information Technology | large | unknown | 2026-08-02 |
| ONTO | $258.57 | $25,201,609 | Information Technology | mid | unknown | 2026-08-02 |
| ORCL | $129.88 | $175,864,990 | Information Technology | large | unknown | 2026-08-02 |
| ORLY | $89.34 | $34,955,873 | Consumer Discretionary | large | unknown | 2026-08-02 |
| OXY | $57.07 | $38,155,795 | Energy | large | unknown | 2026-08-02 |
| PANW | $331.84 | $100,358,037 | Information Technology | large | unknown | 2026-08-02 |
| PATH | $12.77 | $24,244,259 | Information Technology | mid | unknown | 2026-08-02 |
| PCAR | $132.69 | $21,396,213 | Industrials | large | unknown | 2026-08-02 |
| PCG | $17.38 | $21,388,872 | Utilities | large | unknown | 2026-08-02 |
| PEP | $139.60 | $45,223,765 | Consumer Staples | large | unknown | 2026-08-02 |
| PFE | $25.03 | $48,237,394 | Health Care | large | unknown | 2026-08-02 |
| PG | $144.51 | $51,593,948 | Consumer Staples | large | unknown | 2026-08-02 |
| PGR | $211.37 | $34,896,618 | Financials | large | unknown | 2026-08-02 |
| PH | $977.67 | $33,826,857 | Industrials | large | unknown | 2026-08-02 |
| PLD | $144.71 | $29,505,283 | Real Estate | large | unknown | 2026-08-02 |
| PLTR | $123.03 | $129,967,197 | Information Technology | large | unknown | 2026-08-02 |
| PM | $190.61 | $47,701,912 | Consumer Staples | large | unknown | 2026-08-02 |
| PNC | $249.87 | $23,917,660 | Financials | large | unknown | 2026-08-02 |
| PSX | $211.69 | $27,001,500 | Energy | large | unknown | 2026-08-02 |
| PWR | $667.40 | $49,187,329 | Industrials | large | unknown | 2026-08-02 |
| PYPL | $57.20 | $52,714,113 | Financials | large | unknown | 2026-08-02 |
| QCOM | $147.70 | $89,093,305 | Information Technology | large | unknown | 2026-08-02 |
| RCL | $318.18 | $43,644,854 | Consumer Discretionary | large | unknown | 2026-08-02 |
| REGN | $762.72 | $40,916,759 | Health Care | large | unknown | 2026-08-02 |
| RF | $30.95 | $22,651,013 | Financials | large | unknown | 2026-08-02 |
| ROK | $480.27 | $22,880,657 | Industrials | large | unknown | 2026-08-02 |
| ROST | $251.00 | $26,335,341 | Consumer Discretionary | large | unknown | 2026-08-02 |
| RTX | $215.22 | $47,582,864 | Industrials | large | unknown | 2026-08-02 |
| SBUX | $105.23 | $33,310,954 | Consumer Discretionary | large | unknown | 2026-08-02 |
| SCHW | $105.25 | $52,914,721 | Financials | large | unknown | 2026-08-02 |
| SHW | $340.76 | $35,961,419 | Materials | large | unknown | 2026-08-02 |
| SLB | $49.60 | $41,329,330 | Energy | large | unknown | 2026-08-02 |
| SMCI | $28.40 | $50,035,386 | Information Technology | large | unknown | 2026-08-02 |
| SMTC | $117.75 | $21,027,927 | Information Technology | mid | unknown | 2026-08-02 |
| SNDK | $1214.05 | $577,470,527 | Information Technology | large | unknown | 2026-08-02 |
| SNPS | $388.82 | $40,571,619 | Information Technology | large | unknown | 2026-08-02 |
| SO | $94.60 | $22,685,109 | Utilities | large | unknown | 2026-08-02 |
| SPGI | $411.51 | $49,780,684 | Financials | large | unknown | 2026-08-02 |
| STRL | $596.82 | $31,966,496 | Industrials | mid | unknown | 2026-08-02 |
| STT | $184.21 | $24,992,769 | Financials | large | unknown | 2026-08-02 |
| STX | $855.57 | $198,428,781 | Information Technology | large | unknown | 2026-08-02 |
| SYK | $325.56 | $50,367,661 | Health Care | large | unknown | 2026-08-02 |
| T | $23.27 | $86,691,699 | Communication Services | large | unknown | 2026-08-02 |
| TDG | $1253.91 | $33,766,119 | Industrials | large | unknown | 2026-08-02 |
| TEL | $205.66 | $44,540,373 | Information Technology | large | unknown | 2026-08-02 |
| TER | $367.56 | $61,696,708 | Information Technology | large | unknown | 2026-08-02 |
| TFC | $51.85 | $28,036,649 | Financials | large | unknown | 2026-08-02 |
| TGT | $144.51 | $27,429,148 | Consumer Staples | large | unknown | 2026-08-02 |
| THC | $254.81 | $22,561,314 | Health Care | mid | unknown | 2026-08-02 |
| TJX | $157.33 | $35,092,886 | Consumer Discretionary | large | unknown | 2026-08-02 |
| TMO | $574.39 | $84,969,834 | Health Care | large | unknown | 2026-08-02 |
| TMUS | $172.69 | $42,675,453 | Communication Services | large | unknown | 2026-08-02 |
| TOST | $32.27 | $20,665,320 | Financials | mid | unknown | 2026-08-02 |
| TRGP | $270.50 | $20,884,404 | Energy | large | unknown | 2026-08-02 |
| TRV | $374.36 | $35,543,560 | Financials | large | unknown | 2026-08-02 |
| TSCO | $30.77 | $24,283,784 | Consumer Discretionary | large | unknown | 2026-08-02 |
| TSLA | $311.19 | $373,776,312 | Consumer Discretionary | large | unknown | 2026-08-02 |
| TT | $455.05 | $38,902,554 | Industrials | large | unknown | 2026-08-02 |
| TTMI | $115.34 | $23,990,821 | Information Technology | mid | unknown | 2026-08-02 |
| TTWO | $242.93 | $21,249,015 | Communication Services | large | unknown | 2026-08-02 |
| TWLO | $197.38 | $20,584,743 | Information Technology | mid | unknown | 2026-08-02 |
| TXN | $275.81 | $97,293,023 | Information Technology | large | unknown | 2026-08-02 |
| UAL | $121.31 | $27,979,411 | Industrials | large | unknown | 2026-08-02 |
| UBER | $70.38 | $70,600,439 | Industrials | large | unknown | 2026-08-02 |
| UNH | $414.43 | $100,527,017 | Health Care | large | unknown | 2026-08-02 |
| UNP | $292.15 | $55,592,884 | Industrials | large | unknown | 2026-08-02 |
| UPS | $104.22 | $25,008,290 | Industrials | large | unknown | 2026-08-02 |
| URI | $1079.93 | $36,717,773 | Industrials | large | unknown | 2026-08-02 |
| USB | $63.01 | $39,717,237 | Financials | large | unknown | 2026-08-02 |
| V | $366.07 | $131,034,602 | Financials | large | unknown | 2026-08-02 |
| VLO | $312.89 | $42,989,397 | Energy | large | unknown | 2026-08-02 |
| VMC | $268.61 | $23,854,860 | Materials | large | unknown | 2026-08-02 |
| VRSK | $194.88 | $25,009,635 | Industrials | large | unknown | 2026-08-02 |
| VRTX | $477.02 | $32,697,319 | Health Care | large | unknown | 2026-08-02 |
| VST | $148.20 | $31,241,166 | Utilities | large | unknown | 2026-08-02 |
| VZ | $46.83 | $84,014,049 | Communication Services | large | unknown | 2026-08-02 |
| WAT | $377.25 | $23,052,481 | Health Care | large | unknown | 2026-08-02 |
| WBD | $26.29 | $48,007,291 | Communication Services | large | unknown | 2026-08-02 |
| WCC | $343.46 | $22,052,486 | Industrials | mid | unknown | 2026-08-02 |
| WDAY | $160.36 | $34,213,537 | Information Technology | large | unknown | 2026-08-02 |
| WDC | $544.61 | $166,222,478 | Information Technology | large | unknown | 2026-08-02 |
| WELL | $234.61 | $35,640,922 | Real Estate | large | unknown | 2026-08-02 |
| WFC | $86.45 | $83,660,754 | Financials | large | unknown | 2026-08-02 |
| WM | $226.66 | $25,040,526 | Industrials | large | unknown | 2026-08-02 |
| WMB | $71.57 | $28,666,556 | Energy | large | unknown | 2026-08-02 |
| WMT | $111.23 | $110,581,794 | Consumer Staples | large | unknown | 2026-08-02 |
| WST | $341.01 | $20,121,371 | Health Care | large | unknown | 2026-08-02 |
| XEL | $78.23 | $23,546,972 | Utilities | large | unknown | 2026-08-02 |
| XOM | $155.41 | $77,331,374 | Energy | large | unknown | 2026-08-02 |
| XYZ | $81.27 | $22,540,196 | Financials | large | unknown | 2026-08-02 |
| YUM | $153.31 | $23,004,562 | Consumer Discretionary | large | unknown | 2026-08-02 |
