---
screened_on: 2026-05-17
expires_on: 2026-05-24
total_passed: 289
total_rejected: 1217
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
| AAL | $12.30 | $27,716,336 | Industrials | mid | unknown | 2026-05-17 |
| AAPL | $300.19 | $371,166,793 | Information Technology | large | unknown | 2026-05-17 |
| ABBV | $210.48 | $55,395,115 | Health Care | large | unknown | 2026-05-17 |
| ABNB | $132.87 | $24,332,523 | Consumer Discretionary | large | unknown | 2026-05-17 |
| ABT | $84.46 | $55,707,620 | Health Care | large | unknown | 2026-05-17 |
| ACN | $168.78 | $51,316,175 | Information Technology | large | unknown | 2026-05-17 |
| ADBE | $247.59 | $41,353,426 | Information Technology | large | unknown | 2026-05-17 |
| ADI | $417.30 | $64,725,077 | Information Technology | large | unknown | 2026-05-17 |
| ADP | $214.47 | $31,092,754 | Industrials | large | unknown | 2026-05-17 |
| ADSK | $236.63 | $23,649,766 | Information Technology | large | unknown | 2026-05-17 |
| AEIS | $323.38 | $23,051,809 | Information Technology | mid | unknown | 2026-05-17 |
| AEP | $125.10 | $24,856,899 | Utilities | large | unknown | 2026-05-17 |
| AJG | $199.90 | $30,724,183 | Financials | large | unknown | 2026-05-17 |
| AKAM | $150.84 | $37,316,072 | Information Technology | large | unknown | 2026-05-17 |
| ALB | $180.42 | $21,553,218 | Materials | large | unknown | 2026-05-17 |
| AMAT | $436.33 | $102,645,658 | Information Technology | large | unknown | 2026-05-17 |
| AMD | $423.97 | $321,370,690 | Information Technology | large | unknown | 2026-05-17 |
| AMGN | $326.31 | $31,181,588 | Health Care | large | unknown | 2026-05-17 |
| AMP | $470.56 | $21,452,094 | Financials | large | unknown | 2026-05-17 |
| AMT | $170.79 | $25,172,184 | Real Estate | large | unknown | 2026-05-17 |
| AMZN | $264.22 | $499,551,360 | Consumer Discretionary | large | unknown | 2026-05-17 |
| ANET | $141.95 | $88,889,695 | Information Technology | large | unknown | 2026-05-17 |
| AON | $316.98 | $32,024,871 | Financials | large | unknown | 2026-05-17 |
| APD | $295.27 | $20,413,228 | Materials | large | unknown | 2026-05-17 |
| APH | $125.00 | $78,479,993 | Information Technology | large | unknown | 2026-05-17 |
| APO | $135.37 | $29,805,710 | Financials | large | unknown | 2026-05-17 |
| APP | $501.00 | $83,670,490 | Information Technology | large | unknown | 2026-05-17 |
| AVGO | $425.03 | $251,967,477 | Information Technology | large | unknown | 2026-05-17 |
| AXON | $392.04 | $20,744,441 | Industrials | large | unknown | 2026-05-17 |
| AXP | $313.43 | $39,665,271 | Financials | large | unknown | 2026-05-17 |
| AZO | $3316.59 | $38,940,053 | Consumer Discretionary | large | unknown | 2026-05-17 |
| BA | $220.53 | $57,766,239 | Industrials | large | unknown | 2026-05-17 |
| BAC | $49.77 | $97,523,430 | Financials | large | unknown | 2026-05-17 |
| BDX | $143.47 | $29,433,614 | Health Care | large | unknown | 2026-05-17 |
| BK | $135.03 | $24,321,240 | Financials | large | unknown | 2026-05-17 |
| BKNG | $154.19 | $74,959,576 | Consumer Discretionary | large | unknown | 2026-05-17 |
| BKR | $64.11 | $29,584,801 | Energy | large | unknown | 2026-05-17 |
| BLD | $400.68 | $44,172,877 | Consumer Discretionary | mid | unknown | 2026-05-17 |
| BLK | $1081.97 | $34,170,065 | Financials | large | unknown | 2026-05-17 |
| BMY | $57.02 | $35,844,883 | Health Care | large | unknown | 2026-05-17 |
| BRK.B | $482.69 | $63,756,564 | Financials | large | unknown | 2026-05-17 |
| BSX | $52.67 | $85,374,698 | Health Care | large | unknown | 2026-05-17 |
| BX | $117.88 | $27,480,566 | Financials | large | unknown | 2026-05-17 |
| C | $123.38 | $54,361,361 | Financials | large | unknown | 2026-05-17 |
| CAH | $195.21 | $28,151,734 | Health Care | large | unknown | 2026-05-17 |
| CAR | $150.28 | $39,977,263 | Industrials | mid | unknown | 2026-05-17 |
| CARR | $64.67 | $25,616,171 | Industrials | large | unknown | 2026-05-17 |
| CAT | $888.13 | $86,099,613 | Industrials | large | unknown | 2026-05-17 |
| CB | $324.18 | $25,161,816 | Financials | large | unknown | 2026-05-17 |
| CBOE | $361.79 | $23,212,353 | Financials | large | unknown | 2026-05-17 |
| CCL | $24.64 | $40,625,010 | Consumer Discretionary | large | unknown | 2026-05-17 |
| CDNS | $347.30 | $45,985,841 | Information Technology | large | unknown | 2026-05-17 |
| CEG | $267.10 | $54,012,410 | Utilities | large | unknown | 2026-05-17 |
| CF | $125.19 | $20,995,160 | Materials | large | unknown | 2026-05-17 |
| CHRW | $163.59 | $23,982,790 | Industrials | large | unknown | 2026-05-17 |
| CHTR | $140.37 | $35,121,165 | Communication Services | large | unknown | 2026-05-17 |
| CI | $285.26 | $24,311,561 | Health Care | large | unknown | 2026-05-17 |
| CL | $88.12 | $28,632,703 | Consumer Staples | large | unknown | 2026-05-17 |
| CMCSA | $24.75 | $63,044,906 | Communication Services | large | unknown | 2026-05-17 |
| CME | $298.87 | $33,112,690 | Financials | large | unknown | 2026-05-17 |
| CMG | $32.66 | $41,138,969 | Consumer Discretionary | large | unknown | 2026-05-17 |
| CMI | $696.74 | $38,163,798 | Industrials | large | unknown | 2026-05-17 |
| COF | $187.17 | $52,898,217 | Financials | large | unknown | 2026-05-17 |
| COIN | $195.50 | $47,613,772 | Financials | large | unknown | 2026-05-17 |
| COP | $122.38 | $62,476,923 | Energy | large | unknown | 2026-05-17 |
| COR | $257.40 | $40,090,593 | Health Care | large | unknown | 2026-05-17 |
| COST | $1049.30 | $54,779,241 | Consumer Staples | large | unknown | 2026-05-17 |
| CRM | $173.48 | $88,340,507 | Information Technology | large | unknown | 2026-05-17 |
| CRS | $408.86 | $27,194,459 | Industrials | mid | unknown | 2026-05-17 |
| CRWD | $594.23 | $49,827,787 | Information Technology | large | unknown | 2026-05-17 |
| CSCO | $118.25 | $109,154,133 | Information Technology | large | unknown | 2026-05-17 |
| CSX | $45.67 | $43,499,425 | Industrials | large | unknown | 2026-05-17 |
| CTSH | $47.13 | $21,670,823 | Information Technology | large | unknown | 2026-05-17 |
| CVS | $95.93 | $44,084,313 | Health Care | large | unknown | 2026-05-17 |
| CVX | $191.10 | $56,963,244 | Energy | large | unknown | 2026-05-17 |
| D | $61.74 | $20,479,071 | Utilities | large | unknown | 2026-05-17 |
| DAL | $70.24 | $25,309,651 | Industrials | large | unknown | 2026-05-17 |
| DASH | $159.17 | $45,337,108 | Consumer Discretionary | large | unknown | 2026-05-17 |
| DDOG | $207.96 | $50,167,457 | Information Technology | large | unknown | 2026-05-17 |
| DE | $561.75 | $34,290,596 | Industrials | large | unknown | 2026-05-17 |
| DELL | $242.11 | $57,238,760 | Information Technology | large | unknown | 2026-05-17 |
| DG | $102.34 | $22,276,259 | Consumer Staples | large | unknown | 2026-05-17 |
| DHR | $161.92 | $62,195,720 | Health Care | large | unknown | 2026-05-17 |
| DIS | $102.75 | $49,172,131 | Communication Services | large | unknown | 2026-05-17 |
| DLR | $188.59 | $20,500,486 | Real Estate | large | unknown | 2026-05-17 |
| DOCN | $154.80 | $26,117,415 | Information Technology | mid | unknown | 2026-05-17 |
| DOW | $38.74 | $29,920,395 | Materials | large | unknown | 2026-05-17 |
| DPZ | $302.47 | $25,662,537 | Consumer Discretionary | large | unknown | 2026-05-17 |
| DT | $38.35 | $21,508,587 | Information Technology | mid | unknown | 2026-05-17 |
| DVN | $49.49 | $38,066,152 | Energy | large | unknown | 2026-05-17 |
| EBAY | $116.15 | $38,355,201 | Consumer Discretionary | large | unknown | 2026-05-17 |
| ECL | $247.65 | $21,849,102 | Materials | large | unknown | 2026-05-17 |
| EFX | $158.41 | $21,011,949 | Industrials | large | unknown | 2026-05-17 |
| ELV | $392.47 | $37,792,936 | Health Care | large | unknown | 2026-05-17 |
| EME | $914.52 | $24,530,399 | Industrials | large | unknown | 2026-05-17 |
| EMR | $133.06 | $23,552,676 | Industrials | large | unknown | 2026-05-17 |
| ENTG | $133.05 | $24,664,051 | Information Technology | mid | unknown | 2026-05-17 |
| EOG | $140.23 | $31,759,303 | Energy | large | unknown | 2026-05-17 |
| EQIX | $1059.74 | $38,745,574 | Real Estate | large | unknown | 2026-05-17 |
| EQT | $56.20 | $33,493,086 | Energy | large | unknown | 2026-05-17 |
| ETN | $399.83 | $73,056,088 | Industrials | large | unknown | 2026-05-17 |
| ETR | $109.05 | $20,713,277 | Utilities | large | unknown | 2026-05-17 |
| EW | $81.38 | $24,190,157 | Health Care | large | unknown | 2026-05-17 |
| EXC | $43.39 | $25,336,753 | Utilities | large | unknown | 2026-05-17 |
| EXPE | $217.71 | $23,152,203 | Consumer Discretionary | large | unknown | 2026-05-17 |
| F | $13.42 | $52,920,144 | Consumer Discretionary | large | unknown | 2026-05-17 |
| FANG | $203.43 | $21,271,334 | Energy | large | unknown | 2026-05-17 |
| FCX | $62.99 | $65,603,384 | Materials | large | unknown | 2026-05-17 |
| FDX | $375.88 | $31,480,743 | Industrials | large | unknown | 2026-05-17 |
| FE | $43.82 | $20,169,060 | Utilities | large | unknown | 2026-05-17 |
| FICO | $1099.00 | $33,806,604 | Information Technology | large | unknown | 2026-05-17 |
| FIS | $41.79 | $21,779,442 | Financials | large | unknown | 2026-05-17 |
| FLEX | $137.85 | $44,047,076 | Information Technology | mid | unknown | 2026-05-17 |
| FN | $722.49 | $44,524,904 | Information Technology | mid | unknown | 2026-05-17 |
| FSLR | $233.32 | $23,142,197 | Information Technology | large | unknown | 2026-05-17 |
| FTI | $71.28 | $21,808,758 | Energy | mid | unknown | 2026-05-17 |
| FTNT | $122.81 | $25,596,059 | Information Technology | large | unknown | 2026-05-17 |
| GD | $334.45 | $28,015,319 | Industrials | large | unknown | 2026-05-17 |
| GE | $281.47 | $96,952,763 | Industrials | large | unknown | 2026-05-17 |
| GEHC | $60.76 | $22,490,278 | Health Care | large | unknown | 2026-05-17 |
| GEV | $1048.81 | $107,990,300 | Industrials | large | unknown | 2026-05-17 |
| GILD | $129.59 | $34,418,856 | Health Care | large | unknown | 2026-05-17 |
| GLW | $191.92 | $114,957,754 | Information Technology | large | unknown | 2026-05-17 |
| GM | $74.86 | $31,262,743 | Consumer Discretionary | large | unknown | 2026-05-17 |
| GOOG | $393.21 | $162,148,649 | Communication Services | large | unknown | 2026-05-17 |
| GOOGL | $396.75 | $362,360,670 | Communication Services | large | unknown | 2026-05-17 |
| GS | $948.74 | $61,568,880 | Financials | large | unknown | 2026-05-17 |
| GWW | $1272.32 | $25,102,702 | Industrials | large | unknown | 2026-05-17 |
| HAL | $41.76 | $31,332,846 | Energy | large | unknown | 2026-05-17 |
| HCA | $422.94 | $31,194,074 | Health Care | large | unknown | 2026-05-17 |
| HD | $297.53 | $61,267,066 | Consumer Discretionary | large | unknown | 2026-05-17 |
| HIMS | $25.05 | $21,883,560 | Health Care | mid | unknown | 2026-05-17 |
| HLT | $316.11 | $34,299,415 | Consumer Discretionary | large | unknown | 2026-05-17 |
| HON | $213.24 | $33,170,439 | Industrials | large | unknown | 2026-05-17 |
| HOOD | $77.12 | $63,328,604 | Financials | large | unknown | 2026-05-17 |
| HPE | $33.10 | $39,956,887 | Information Technology | large | unknown | 2026-05-17 |
| HSY | $187.00 | $20,740,738 | Consumer Staples | large | unknown | 2026-05-17 |
| HUBB | $480.22 | $26,869,427 | Industrials | large | unknown | 2026-05-17 |
| HUM | $305.31 | $29,558,364 | Health Care | large | unknown | 2026-05-17 |
| HWM | $260.28 | $33,527,022 | Industrials | large | unknown | 2026-05-17 |
| IBM | $219.44 | $62,515,706 | Information Technology | large | unknown | 2026-05-17 |
| ICE | $154.37 | $24,378,671 | Financials | large | unknown | 2026-05-17 |
| IDXX | $528.63 | $20,536,316 | Health Care | large | unknown | 2026-05-17 |
| INTC | $108.87 | $373,901,176 | Information Technology | large | unknown | 2026-05-17 |
| INTU | $392.98 | $68,098,898 | Information Technology | large | unknown | 2026-05-17 |
| ISRG | $421.11 | $51,603,754 | Health Care | large | unknown | 2026-05-17 |
| ITW | $247.72 | $21,772,928 | Industrials | large | unknown | 2026-05-17 |
| JBL | $339.75 | $29,216,026 | Information Technology | large | unknown | 2026-05-17 |
| JCI | $143.09 | $21,157,591 | Industrials | large | unknown | 2026-05-17 |
| JNJ | $226.75 | $68,686,053 | Health Care | large | unknown | 2026-05-17 |
| JPM | $297.79 | $60,966,054 | Financials | large | unknown | 2026-05-17 |
| KDP | $28.95 | $26,374,856 | Consumer Staples | large | unknown | 2026-05-17 |
| KEYS | $349.06 | $28,340,665 | Information Technology | large | unknown | 2026-05-17 |
| KKR | $96.98 | $31,348,221 | Financials | large | unknown | 2026-05-17 |
| KLAC | $1803.53 | $121,161,122 | Information Technology | large | unknown | 2026-05-17 |
| KMI | $33.63 | $23,304,336 | Energy | large | unknown | 2026-05-17 |
| KO | $80.84 | $69,494,231 | Consumer Staples | large | unknown | 2026-05-17 |
| KVUE | $17.09 | $21,680,702 | Consumer Staples | large | unknown | 2026-05-17 |
| LHX | $303.49 | $35,399,037 | Industrials | large | unknown | 2026-05-17 |
| LIN | $506.19 | $45,712,312 | Materials | large | unknown | 2026-05-17 |
| LLY | $1004.70 | $126,320,391 | Health Care | large | unknown | 2026-05-17 |
| LMT | $516.11 | $40,143,242 | Industrials | large | unknown | 2026-05-17 |
| LOW | $218.31 | $29,294,456 | Consumer Discretionary | large | unknown | 2026-05-17 |
| LRCX | $284.37 | $94,507,062 | Information Technology | large | unknown | 2026-05-17 |
| LSCC | $120.03 | $27,030,102 | Information Technology | mid | unknown | 2026-05-17 |
| LYB | $75.03 | $26,014,300 | Materials | large | unknown | 2026-05-17 |
| MA | $494.32 | $106,574,666 | Financials | large | unknown | 2026-05-17 |
| MAR | $353.29 | $28,525,310 | Consumer Discretionary | large | unknown | 2026-05-17 |
| MCD | $276.39 | $43,055,694 | Consumer Discretionary | large | unknown | 2026-05-17 |
| MCHP | $93.84 | $56,345,318 | Information Technology | large | unknown | 2026-05-17 |
| MCK | $760.75 | $50,433,735 | Health Care | large | unknown | 2026-05-17 |
| MCO | $429.08 | $35,326,577 | Financials | large | unknown | 2026-05-17 |
| MDLZ | $60.45 | $30,889,579 | Consumer Staples | large | unknown | 2026-05-17 |
| MDT | $76.14 | $53,490,324 | Health Care | large | unknown | 2026-05-17 |
| META | $614.38 | $315,377,797 | Communication Services | large | unknown | 2026-05-17 |
| MKSI | $303.16 | $27,314,983 | Information Technology | mid | unknown | 2026-05-17 |
| MLM | $558.62 | $21,970,413 | Materials | large | unknown | 2026-05-17 |
| MMM | $146.26 | $28,640,047 | Industrials | large | unknown | 2026-05-17 |
| MNST | $87.08 | $22,572,569 | Consumer Staples | large | unknown | 2026-05-17 |
| MO | $73.07 | $49,843,621 | Consumer Staples | large | unknown | 2026-05-17 |
| MPC | $255.06 | $25,795,502 | Energy | large | unknown | 2026-05-17 |
| MPWR | $1549.80 | $62,024,564 | Information Technology | large | unknown | 2026-05-17 |
| MRK | $111.35 | $40,828,680 | Health Care | large | unknown | 2026-05-17 |
| MRSH | $161.11 | $22,724,360 | Financials | large | unknown | 2026-05-17 |
| MS | $192.45 | $40,398,420 | Financials | large | unknown | 2026-05-17 |
| MSCI | $561.88 | $26,396,708 | Financials | large | unknown | 2026-05-17 |
| MSFT | $422.00 | $357,284,898 | Information Technology | large | unknown | 2026-05-17 |
| MSI | $393.37 | $34,262,330 | Information Technology | large | unknown | 2026-05-17 |
| MTSI | $375.57 | $25,675,168 | Information Technology | mid | unknown | 2026-05-17 |
| MTZ | $414.95 | $26,887,590 | Industrials | mid | unknown | 2026-05-17 |
| MU | $724.09 | $514,663,600 | Information Technology | large | unknown | 2026-05-17 |
| MXL | $92.21 | $20,369,962 | Information Technology | small | unknown | 2026-05-17 |
| NCLH | $15.52 | $21,801,947 | Consumer Discretionary | large | unknown | 2026-05-17 |
| NEE | $93.37 | $44,718,557 | Utilities | large | unknown | 2026-05-17 |
| NEM | $109.08 | $32,395,563 | Materials | large | unknown | 2026-05-17 |
| NFLX | $87.05 | $193,652,390 | Communication Services | large | unknown | 2026-05-17 |
| NKE | $41.90 | $45,789,749 | Consumer Discretionary | large | unknown | 2026-05-17 |
| NOC | $540.43 | $24,890,076 | Industrials | large | unknown | 2026-05-17 |
| NOW | $95.08 | $94,714,788 | Information Technology | large | unknown | 2026-05-17 |
| NRG | $127.83 | $26,007,334 | Utilities | large | unknown | 2026-05-17 |
| NVDA | $225.31 | $915,100,058 | Information Technology | large | unknown | 2026-05-17 |
| NXPI | $291.70 | $56,047,849 | Information Technology | large | unknown | 2026-05-17 |
| ODFL | $203.04 | $28,094,401 | Industrials | large | unknown | 2026-05-17 |
| ON | $113.04 | $68,383,637 | Information Technology | large | unknown | 2026-05-17 |
| ORCL | $192.98 | $140,794,688 | Information Technology | large | unknown | 2026-05-17 |
| ORLY | $88.47 | $23,966,877 | Consumer Discretionary | large | unknown | 2026-05-17 |
| OXY | $59.62 | $34,912,431 | Energy | large | unknown | 2026-05-17 |
| PANW | $242.85 | $61,109,353 | Information Technology | large | unknown | 2026-05-17 |
| PCG | $16.15 | $21,384,059 | Utilities | large | unknown | 2026-05-17 |
| PEP | $149.07 | $27,823,479 | Consumer Staples | large | unknown | 2026-05-17 |
| PFE | $25.32 | $47,065,285 | Health Care | large | unknown | 2026-05-17 |
| PG | $141.57 | $51,851,274 | Consumer Staples | large | unknown | 2026-05-17 |
| PGR | $199.83 | $23,912,336 | Financials | large | unknown | 2026-05-17 |
| PH | $862.59 | $55,833,469 | Industrials | large | unknown | 2026-05-17 |
| PINS | $19.49 | $23,249,507 | Communication Services | mid | unknown | 2026-05-17 |
| PLTR | $133.97 | $133,178,773 | Information Technology | large | unknown | 2026-05-17 |
| PM | $189.63 | $41,489,648 | Consumer Staples | large | unknown | 2026-05-17 |
| PNC | $212.91 | $20,719,166 | Financials | large | unknown | 2026-05-17 |
| PODD | $147.40 | $20,909,652 | Health Care | large | unknown | 2026-05-17 |
| PSX | $176.34 | $24,755,022 | Energy | large | unknown | 2026-05-17 |
| PWR | $769.82 | $60,216,850 | Industrials | large | unknown | 2026-05-17 |
| PYPL | $44.40 | $34,311,146 | Financials | large | unknown | 2026-05-17 |
| QCOM | $201.56 | $156,250,781 | Information Technology | large | unknown | 2026-05-17 |
| RCL | $260.31 | $36,484,501 | Consumer Discretionary | large | unknown | 2026-05-17 |
| REGN | $698.22 | $36,333,733 | Health Care | large | unknown | 2026-05-17 |
| ROK | $448.75 | $24,401,817 | Industrials | large | unknown | 2026-05-17 |
| ROP | $320.89 | $21,389,885 | Information Technology | large | unknown | 2026-05-17 |
| ROST | $212.70 | $25,352,329 | Consumer Discretionary | large | unknown | 2026-05-17 |
| RRX | $197.22 | $23,350,118 | Industrials | mid | unknown | 2026-05-17 |
| RSG | $208.38 | $25,480,104 | Industrials | large | unknown | 2026-05-17 |
| RTX | $171.15 | $45,911,043 | Industrials | large | unknown | 2026-05-17 |
| SBUX | $106.79 | $35,583,648 | Consumer Discretionary | large | unknown | 2026-05-17 |
| SCHW | $90.89 | $56,099,466 | Financials | large | unknown | 2026-05-17 |
| SHW | $300.35 | $31,853,107 | Materials | large | unknown | 2026-05-17 |
| SITM | $774.02 | $21,802,208 | Information Technology | mid | unknown | 2026-05-17 |
| SLB | $55.39 | $47,008,075 | Energy | large | unknown | 2026-05-17 |
| SMCI | $31.04 | $46,632,656 | Information Technology | large | unknown | 2026-05-17 |
| SMTC | $137.66 | $22,770,326 | Information Technology | small | unknown | 2026-05-17 |
| SNPS | $502.46 | $39,772,082 | Information Technology | large | unknown | 2026-05-17 |
| SO | $92.55 | $26,553,671 | Utilities | large | unknown | 2026-05-17 |
| SPGI | $403.09 | $48,273,602 | Financials | large | unknown | 2026-05-17 |
| STRL | $849.21 | $24,031,428 | Industrials | mid | unknown | 2026-05-17 |
| STX | $795.27 | $139,885,986 | Information Technology | large | unknown | 2026-05-17 |
| SYK | $306.75 | $59,514,178 | Health Care | large | unknown | 2026-05-17 |
| T | $24.05 | $48,168,154 | Communication Services | large | unknown | 2026-05-17 |
| TDG | $1149.08 | $37,503,216 | Industrials | large | unknown | 2026-05-17 |
| TEL | $205.28 | $53,148,600 | Information Technology | large | unknown | 2026-05-17 |
| TER | $337.92 | $64,424,807 | Information Technology | large | unknown | 2026-05-17 |
| TFC | $46.96 | $22,884,795 | Financials | large | unknown | 2026-05-17 |
| TGT | $121.53 | $24,579,494 | Consumer Staples | large | unknown | 2026-05-17 |
| TJX | $147.44 | $30,112,681 | Consumer Discretionary | large | unknown | 2026-05-17 |
| TMO | $438.15 | $90,315,374 | Health Care | large | unknown | 2026-05-17 |
| TMUS | $185.13 | $56,777,736 | Communication Services | large | unknown | 2026-05-17 |
| TSCO | $30.57 | $30,156,695 | Consumer Discretionary | large | unknown | 2026-05-17 |
| TSLA | $422.27 | $323,646,877 | Consumer Discretionary | large | unknown | 2026-05-17 |
| TT | $466.45 | $42,982,951 | Industrials | large | unknown | 2026-05-17 |
| TTD | $21.16 | $23,056,904 | Communication Services | large | unknown | 2026-05-17 |
| TWLO | $198.14 | $32,100,844 | Information Technology | mid | unknown | 2026-05-17 |
| TXN | $302.69 | $109,530,681 | Information Technology | large | unknown | 2026-05-17 |
| UAL | $92.83 | $27,782,721 | Industrials | large | unknown | 2026-05-17 |
| UBER | $75.10 | $77,394,560 | Industrials | large | unknown | 2026-05-17 |
| ULTA | $494.32 | $21,398,892 | Consumer Discretionary | large | unknown | 2026-05-17 |
| UNH | $393.52 | $115,502,736 | Health Care | large | unknown | 2026-05-17 |
| UNP | $270.52 | $46,531,095 | Industrials | large | unknown | 2026-05-17 |
| UPS | $98.92 | $25,957,568 | Industrials | large | unknown | 2026-05-17 |
| URI | $961.26 | $43,769,957 | Industrials | large | unknown | 2026-05-17 |
| USB | $53.12 | $34,702,147 | Financials | large | unknown | 2026-05-17 |
| V | $325.74 | $159,693,972 | Financials | large | unknown | 2026-05-17 |
| VLO | $250.74 | $34,361,712 | Energy | large | unknown | 2026-05-17 |
| VMC | $267.84 | $20,659,251 | Materials | large | unknown | 2026-05-17 |
| VRSK | $162.59 | $20,478,614 | Industrials | large | unknown | 2026-05-17 |
| VST | $139.70 | $30,894,428 | Utilities | large | unknown | 2026-05-17 |
| VTR | $87.45 | $26,770,618 | Real Estate | large | unknown | 2026-05-17 |
| VZ | $46.39 | $55,425,878 | Communication Services | large | unknown | 2026-05-17 |
| WAT | $329.20 | $35,116,576 | Health Care | large | unknown | 2026-05-17 |
| WBD | $27.00 | $27,817,882 | Communication Services | large | unknown | 2026-05-17 |
| WDAY | $125.03 | $28,584,721 | Information Technology | large | unknown | 2026-05-17 |
| WDC | $481.87 | $125,879,347 | Information Technology | large | unknown | 2026-05-17 |
| WELL | $213.78 | $30,267,202 | Real Estate | large | unknown | 2026-05-17 |
| WFC | $73.43 | $78,967,300 | Financials | large | unknown | 2026-05-17 |
| WM | $219.88 | $23,284,407 | Industrials | large | unknown | 2026-05-17 |
| WMB | $77.71 | $30,491,513 | Energy | large | unknown | 2026-05-17 |
| WMT | $131.50 | $62,201,489 | Consumer Staples | large | unknown | 2026-05-17 |
| WST | $303.10 | $21,433,653 | Health Care | large | unknown | 2026-05-17 |
| WWD | $349.26 | $20,606,860 | Industrials | mid | unknown | 2026-05-17 |
| XEL | $77.88 | $27,308,960 | Utilities | large | unknown | 2026-05-17 |
| XOM | $157.93 | $90,173,246 | Energy | large | unknown | 2026-05-17 |
| XPO | $204.30 | $23,508,642 | Industrials | mid | unknown | 2026-05-17 |
| ZTS | $74.27 | $37,778,350 | Health Care | large | unknown | 2026-05-17 |
