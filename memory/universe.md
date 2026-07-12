---
screened_on: 2026-07-12
expires_on: 2026-07-19
total_passed: 305
total_rejected: 1195
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
| AA | $48.66 | $20,447,790 | Materials | mid | unknown | 2026-07-12 |
| AAL | $16.96 | $53,152,163 | Industrials | mid | unknown | 2026-07-12 |
| AAPL | $315.32 | $621,390,425 | Information Technology | large | unknown | 2026-07-12 |
| ABBV | $247.97 | $74,261,315 | Health Care | large | unknown | 2026-07-12 |
| ABNB | $148.60 | $23,637,905 | Consumer Discretionary | large | unknown | 2026-07-12 |
| ABT | $93.93 | $53,899,762 | Health Care | large | unknown | 2026-07-12 |
| ACN | $135.19 | $77,802,265 | Information Technology | large | unknown | 2026-07-12 |
| ADBE | $223.70 | $67,657,794 | Information Technology | large | unknown | 2026-07-12 |
| ADI | $395.73 | $84,744,592 | Information Technology | large | unknown | 2026-07-12 |
| ADP | $241.91 | $21,378,523 | Industrials | large | unknown | 2026-07-12 |
| ADSK | $208.45 | $30,769,658 | Information Technology | large | unknown | 2026-07-12 |
| AEIS | $307.82 | $20,973,921 | Information Technology | mid | unknown | 2026-07-12 |
| AEP | $135.41 | $25,933,705 | Utilities | large | unknown | 2026-07-12 |
| AJG | $253.00 | $27,780,980 | Financials | large | unknown | 2026-07-12 |
| AKAM | $126.16 | $25,821,340 | Information Technology | large | unknown | 2026-07-12 |
| AMAT | $602.31 | $313,161,252 | Information Technology | large | unknown | 2026-07-12 |
| AMD | $557.85 | $348,813,552 | Information Technology | large | unknown | 2026-07-12 |
| AMGN | $363.37 | $31,886,306 | Health Care | large | unknown | 2026-07-12 |
| AMKR | $70.49 | $22,481,007 | Information Technology | mid | unknown | 2026-07-12 |
| AMT | $168.54 | $28,969,639 | Real Estate | large | unknown | 2026-07-12 |
| AMZN | $245.35 | $597,318,769 | Consumer Discretionary | large | unknown | 2026-07-12 |
| ANET | $186.90 | $68,353,911 | Information Technology | large | unknown | 2026-07-12 |
| AON | $356.58 | $24,361,469 | Financials | large | unknown | 2026-07-12 |
| APD | $299.48 | $22,364,097 | Materials | large | unknown | 2026-07-12 |
| APH | $159.07 | $68,037,941 | Information Technology | large | unknown | 2026-07-12 |
| APO | $120.33 | $28,983,118 | Financials | large | unknown | 2026-07-12 |
| APP | $506.74 | $91,228,128 | Information Technology | large | unknown | 2026-07-12 |
| AVGO | $399.91 | $315,174,474 | Information Technology | large | unknown | 2026-07-12 |
| AXON | $565.62 | $28,114,832 | Industrials | large | unknown | 2026-07-12 |
| AXP | $350.48 | $43,110,265 | Financials | large | unknown | 2026-07-12 |
| AZO | $3071.80 | $56,464,260 | Consumer Discretionary | large | unknown | 2026-07-12 |
| BA | $222.22 | $44,999,931 | Industrials | large | unknown | 2026-07-12 |
| BAC | $59.64 | $136,431,286 | Financials | large | unknown | 2026-07-12 |
| BKNG | $178.43 | $67,204,765 | Consumer Discretionary | large | unknown | 2026-07-12 |
| BKR | $57.52 | $36,963,192 | Energy | large | unknown | 2026-07-12 |
| BLD | $353.73 | $34,405,021 | Consumer Discretionary | mid | unknown | 2026-07-12 |
| BLK | $1035.98 | $63,008,556 | Financials | large | unknown | 2026-07-12 |
| BMY | $57.56 | $42,283,141 | Health Care | large | unknown | 2026-07-12 |
| BRK.B | $493.63 | $67,439,489 | Financials | large | unknown | 2026-07-12 |
| BSX | $44.77 | $62,731,306 | Health Care | large | unknown | 2026-07-12 |
| BX | $123.07 | $26,159,323 | Financials | large | unknown | 2026-07-12 |
| C | $140.62 | $72,959,642 | Financials | large | unknown | 2026-07-12 |
| CAH | $235.63 | $28,391,737 | Health Care | large | unknown | 2026-07-12 |
| CARR | $69.34 | $21,005,743 | Industrials | large | unknown | 2026-07-12 |
| CAT | $951.67 | $150,053,434 | Industrials | large | unknown | 2026-07-12 |
| CB | $347.77 | $26,065,955 | Financials | large | unknown | 2026-07-12 |
| CBOE | $268.18 | $34,732,817 | Financials | large | unknown | 2026-07-12 |
| CCI | $79.66 | $20,668,573 | Real Estate | large | unknown | 2026-07-12 |
| CCL | $26.82 | $46,192,610 | Consumer Discretionary | large | unknown | 2026-07-12 |
| CDE | $15.99 | $26,831,524 | Materials | mid | unknown | 2026-07-12 |
| CDNS | $384.25 | $38,210,348 | Information Technology | large | unknown | 2026-07-12 |
| CEG | $251.34 | $49,677,218 | Utilities | large | unknown | 2026-07-12 |
| CFG | $70.34 | $26,723,564 | Financials | large | unknown | 2026-07-12 |
| CHTR | $130.66 | $24,198,815 | Communication Services | large | unknown | 2026-07-12 |
| CI | $293.32 | $20,398,726 | Health Care | large | unknown | 2026-07-12 |
| CL | $92.27 | $23,623,838 | Consumer Staples | large | unknown | 2026-07-12 |
| CMCSA | $23.57 | $59,407,260 | Communication Services | large | unknown | 2026-07-12 |
| CME | $240.29 | $61,210,404 | Financials | large | unknown | 2026-07-12 |
| CMG | $35.26 | $44,179,612 | Consumer Discretionary | large | unknown | 2026-07-12 |
| CMI | $675.92 | $38,347,132 | Industrials | large | unknown | 2026-07-12 |
| CNP | $43.55 | $20,085,558 | Utilities | large | unknown | 2026-07-12 |
| COF | $201.39 | $44,852,940 | Financials | large | unknown | 2026-07-12 |
| COIN | $159.09 | $36,097,668 | Financials | large | unknown | 2026-07-12 |
| COP | $109.03 | $56,676,429 | Energy | large | unknown | 2026-07-12 |
| COR | $303.52 | $28,577,614 | Health Care | large | unknown | 2026-07-12 |
| COST | $916.05 | $73,010,727 | Consumer Staples | large | unknown | 2026-07-12 |
| CPRT | $27.52 | $25,303,258 | Industrials | large | unknown | 2026-07-12 |
| CRH | $104.68 | $25,420,139 | Materials | large | unknown | 2026-07-12 |
| CRM | $163.36 | $76,800,628 | Information Technology | large | unknown | 2026-07-12 |
| CRS | $579.14 | $34,360,087 | Industrials | mid | unknown | 2026-07-12 |
| CRWD | $187.15 | $61,690,031 | Information Technology | large | unknown | 2026-07-12 |
| CSCO | $121.24 | $114,085,031 | Information Technology | large | unknown | 2026-07-12 |
| CSX | $49.40 | $45,613,521 | Industrials | large | unknown | 2026-07-12 |
| CTSH | $42.56 | $42,501,431 | Information Technology | large | unknown | 2026-07-12 |
| CVNA | $65.83 | $40,401,785 | Consumer Discretionary | large | unknown | 2026-07-12 |
| CVS | $104.17 | $39,156,250 | Health Care | large | unknown | 2026-07-12 |
| CVX | $176.32 | $61,491,398 | Energy | large | unknown | 2026-07-12 |
| D | $70.09 | $42,489,883 | Utilities | large | unknown | 2026-07-12 |
| DAL | $87.34 | $35,822,301 | Industrials | large | unknown | 2026-07-12 |
| DASH | $191.79 | $47,280,062 | Consumer Discretionary | large | unknown | 2026-07-12 |
| DDOG | $257.45 | $60,585,707 | Information Technology | large | unknown | 2026-07-12 |
| DE | $586.87 | $33,381,464 | Industrials | large | unknown | 2026-07-12 |
| DELL | $434.95 | $109,533,268 | Information Technology | large | unknown | 2026-07-12 |
| DHR | $199.02 | $35,456,959 | Health Care | large | unknown | 2026-07-12 |
| DIS | $95.59 | $51,783,549 | Communication Services | large | unknown | 2026-07-12 |
| DKS | $217.90 | $20,529,793 | Consumer Discretionary | mid | unknown | 2026-07-12 |
| DLR | $180.45 | $33,288,830 | Real Estate | large | unknown | 2026-07-12 |
| DOCN | $130.26 | $23,347,792 | Information Technology | mid | unknown | 2026-07-12 |
| DOW | $29.03 | $29,853,450 | Materials | large | unknown | 2026-07-12 |
| DRI | $204.32 | $23,851,788 | Consumer Discretionary | large | unknown | 2026-07-12 |
| DUK | $125.46 | $20,063,937 | Utilities | large | unknown | 2026-07-12 |
| DVN | $42.23 | $42,013,736 | Energy | large | unknown | 2026-07-12 |
| EA | $206.40 | $20,669,033 | Communication Services | large | unknown | 2026-07-12 |
| EFX | $166.53 | $21,500,653 | Industrials | large | unknown | 2026-07-12 |
| ELV | $416.33 | $29,920,004 | Health Care | large | unknown | 2026-07-12 |
| EMR | $138.81 | $22,440,995 | Industrials | large | unknown | 2026-07-12 |
| ENTG | $145.34 | $36,578,274 | Information Technology | mid | unknown | 2026-07-12 |
| EOG | $134.05 | $24,746,970 | Energy | large | unknown | 2026-07-12 |
| EQIX | $1051.10 | $46,894,758 | Real Estate | large | unknown | 2026-07-12 |
| EQT | $48.82 | $32,720,545 | Energy | large | unknown | 2026-07-12 |
| ETN | $407.11 | $46,899,414 | Industrials | large | unknown | 2026-07-12 |
| EW | $92.17 | $22,824,461 | Health Care | large | unknown | 2026-07-12 |
| EXC | $46.79 | $29,726,153 | Utilities | large | unknown | 2026-07-12 |
| F | $13.99 | $29,556,446 | Consumer Discretionary | large | unknown | 2026-07-12 |
| FANG | $183.34 | $24,847,049 | Energy | large | unknown | 2026-07-12 |
| FAST | $46.48 | $21,891,004 | Industrials | large | unknown | 2026-07-12 |
| FCX | $61.49 | $62,311,922 | Materials | large | unknown | 2026-07-12 |
| FDX | $314.44 | $49,248,840 | Industrials | large | unknown | 2026-07-12 |
| FICO | $1251.12 | $22,429,556 | Information Technology | large | unknown | 2026-07-12 |
| FISV | $50.43 | $23,453,711 | Financials | large | unknown | 2026-07-12 |
| FITB | $57.08 | $31,434,051 | Financials | large | unknown | 2026-07-12 |
| FIX | $1754.60 | $54,573,814 | Industrials | large | unknown | 2026-07-12 |
| FN | $471.16 | $38,976,734 | Information Technology | mid | unknown | 2026-07-12 |
| FOXA | $54.12 | $27,754,323 | Communication Services | large | unknown | 2026-07-12 |
| FSLR | $227.71 | $22,238,504 | Information Technology | large | unknown | 2026-07-12 |
| FTNT | $157.50 | $35,873,267 | Information Technology | large | unknown | 2026-07-12 |
| GE | $359.28 | $74,309,478 | Industrials | large | unknown | 2026-07-12 |
| GEV | $1090.02 | $158,248,077 | Industrials | large | unknown | 2026-07-12 |
| GILD | $129.81 | $42,819,197 | Health Care | large | unknown | 2026-07-12 |
| GIS | $36.22 | $25,787,659 | Consumer Staples | large | unknown | 2026-07-12 |
| GLW | $190.83 | $137,123,183 | Information Technology | large | unknown | 2026-07-12 |
| GM | $77.83 | $29,092,592 | Consumer Discretionary | large | unknown | 2026-07-12 |
| GOOG | $355.04 | $213,021,666 | Communication Services | large | unknown | 2026-07-12 |
| GOOGL | $357.17 | $402,187,439 | Communication Services | large | unknown | 2026-07-12 |
| GS | $1055.08 | $75,209,949 | Financials | large | unknown | 2026-07-12 |
| GWW | $1375.79 | $28,384,145 | Industrials | large | unknown | 2026-07-12 |
| HAL | $34.38 | $33,416,605 | Energy | large | unknown | 2026-07-12 |
| HBAN | $17.86 | $22,374,431 | Financials | large | unknown | 2026-07-12 |
| HCA | $406.56 | $28,289,293 | Health Care | large | unknown | 2026-07-12 |
| HD | $343.37 | $69,425,666 | Consumer Discretionary | large | unknown | 2026-07-12 |
| HLT | $335.39 | $38,467,357 | Consumer Discretionary | large | unknown | 2026-07-12 |
| HON | $226.40 | $53,463,626 | Industrials | large | unknown | 2026-07-12 |
| HOOD | $111.92 | $101,541,566 | Financials | large | unknown | 2026-07-12 |
| HPE | $48.50 | $81,199,588 | Information Technology | large | unknown | 2026-07-12 |
| HPQ | $24.21 | $26,452,933 | Information Technology | large | unknown | 2026-07-12 |
| HSY | $173.73 | $23,685,057 | Consumer Staples | large | unknown | 2026-07-12 |
| HUBB | $490.81 | $24,861,780 | Industrials | large | unknown | 2026-07-12 |
| HUM | $392.36 | $28,528,596 | Health Care | large | unknown | 2026-07-12 |
| HWM | $270.83 | $48,328,312 | Industrials | large | unknown | 2026-07-12 |
| IBM | $287.54 | $70,246,996 | Information Technology | large | unknown | 2026-07-12 |
| ICE | $135.18 | $30,454,710 | Financials | large | unknown | 2026-07-12 |
| IDXX | $563.53 | $23,481,595 | Health Care | large | unknown | 2026-07-12 |
| ILMN | $190.22 | $20,527,505 | Health Care | mid | unknown | 2026-07-12 |
| INTC | $109.85 | $408,986,920 | Information Technology | large | unknown | 2026-07-12 |
| INTU | $274.96 | $91,116,635 | Information Technology | large | unknown | 2026-07-12 |
| ISRG | $406.77 | $46,953,945 | Health Care | large | unknown | 2026-07-12 |
| JBL | $330.10 | $33,245,269 | Information Technology | large | unknown | 2026-07-12 |
| JCI | $142.76 | $31,240,155 | Industrials | large | unknown | 2026-07-12 |
| JNJ | $256.93 | $79,648,567 | Health Care | large | unknown | 2026-07-12 |
| JPM | $336.38 | $90,378,236 | Financials | large | unknown | 2026-07-12 |
| KDP | $31.67 | $36,857,793 | Consumer Staples | large | unknown | 2026-07-12 |
| KEYS | $322.04 | $28,913,479 | Information Technology | large | unknown | 2026-07-12 |
| KKR | $96.95 | $26,520,273 | Financials | large | unknown | 2026-07-12 |
| KLAC | $231.50 | $177,448,017 | Information Technology | large | unknown | 2026-07-12 |
| KMB | $112.38 | $20,516,993 | Consumer Staples | large | unknown | 2026-07-12 |
| KMI | $32.13 | $20,508,170 | Energy | large | unknown | 2026-07-12 |
| KNX | $75.18 | $21,175,134 | Industrials | mid | unknown | 2026-07-12 |
| KO | $83.48 | $98,990,628 | Consumer Staples | large | unknown | 2026-07-12 |
| KR | $60.55 | $30,113,282 | Consumer Staples | large | unknown | 2026-07-12 |
| KVUE | $19.46 | $28,753,045 | Consumer Staples | large | unknown | 2026-07-12 |
| LHX | $290.81 | $27,092,890 | Industrials | large | unknown | 2026-07-12 |
| LIN | $529.65 | $52,752,640 | Materials | large | unknown | 2026-07-12 |
| LLY | $1188.57 | $157,594,896 | Health Care | large | unknown | 2026-07-12 |
| LMT | $523.35 | $26,792,150 | Industrials | large | unknown | 2026-07-12 |
| LOW | $211.55 | $26,583,317 | Consumer Discretionary | large | unknown | 2026-07-12 |
| LRCX | $350.21 | $211,574,052 | Information Technology | large | unknown | 2026-07-12 |
| LSCC | $137.40 | $20,662,270 | Information Technology | mid | unknown | 2026-07-12 |
| LYV | $179.86 | $22,974,719 | Communication Services | large | unknown | 2026-07-12 |
| MA | $526.27 | $93,092,548 | Financials | large | unknown | 2026-07-12 |
| MAR | $376.01 | $35,502,266 | Consumer Discretionary | large | unknown | 2026-07-12 |
| MARA | $12.60 | $21,142,104 | Information Technology | small | unknown | 2026-07-12 |
| MCD | $274.56 | $52,558,621 | Consumer Discretionary | large | unknown | 2026-07-12 |
| MCHP | $88.59 | $39,690,312 | Information Technology | large | unknown | 2026-07-12 |
| MCK | $805.91 | $39,523,281 | Health Care | large | unknown | 2026-07-12 |
| MCO | $487.26 | $33,704,049 | Financials | large | unknown | 2026-07-12 |
| MDLZ | $58.81 | $43,558,186 | Consumer Staples | large | unknown | 2026-07-12 |
| MDT | $83.79 | $49,624,441 | Health Care | large | unknown | 2026-07-12 |
| META | $669.25 | $415,985,783 | Communication Services | large | unknown | 2026-07-12 |
| MKSI | $368.57 | $38,574,328 | Information Technology | mid | unknown | 2026-07-12 |
| MLM | $577.17 | $31,331,803 | Materials | large | unknown | 2026-07-12 |
| MMM | $157.46 | $22,856,528 | Industrials | large | unknown | 2026-07-12 |
| MNST | $97.37 | $24,089,605 | Consumer Staples | large | unknown | 2026-07-12 |
| MO | $71.75 | $29,625,206 | Consumer Staples | large | unknown | 2026-07-12 |
| MPC | $283.30 | $35,805,999 | Energy | large | unknown | 2026-07-12 |
| MPWR | $1353.06 | $67,438,261 | Information Technology | large | unknown | 2026-07-12 |
| MRK | $123.48 | $52,959,684 | Health Care | large | unknown | 2026-07-12 |
| MRNA | $68.26 | $22,143,734 | Health Care | large | unknown | 2026-07-12 |
| MRSH | $178.25 | $20,104,279 | Financials | large | unknown | 2026-07-12 |
| MS | $222.17 | $59,805,374 | Financials | large | unknown | 2026-07-12 |
| MSCI | $604.52 | $30,112,159 | Financials | large | unknown | 2026-07-12 |
| MSFT | $385.09 | $502,208,967 | Information Technology | large | unknown | 2026-07-12 |
| MSI | $422.94 | $21,602,869 | Information Technology | large | unknown | 2026-07-12 |
| MTD | $1294.77 | $20,367,281 | Health Care | large | unknown | 2026-07-12 |
| MTSI | $308.65 | $29,224,106 | Information Technology | mid | unknown | 2026-07-12 |
| MTZ | $373.08 | $31,852,822 | Industrials | mid | unknown | 2026-07-12 |
| MU | $979.36 | $1,156,922,139 | Information Technology | large | unknown | 2026-07-12 |
| NCLH | $19.61 | $22,110,562 | Consumer Discretionary | large | unknown | 2026-07-12 |
| NDAQ | $88.05 | $21,094,199 | Financials | large | unknown | 2026-07-12 |
| NEE | $87.96 | $76,193,762 | Utilities | large | unknown | 2026-07-12 |
| NEM | $95.20 | $45,781,406 | Materials | large | unknown | 2026-07-12 |
| NFLX | $73.38 | $245,240,140 | Communication Services | large | unknown | 2026-07-12 |
| NKE | $44.39 | $65,864,958 | Consumer Discretionary | large | unknown | 2026-07-12 |
| NOC | $539.53 | $33,789,207 | Industrials | large | unknown | 2026-07-12 |
| NOW | $107.68 | $87,798,453 | Information Technology | large | unknown | 2026-07-12 |
| NTAP | $168.85 | $24,033,788 | Information Technology | large | unknown | 2026-07-12 |
| NUE | $227.31 | $21,783,691 | Materials | large | unknown | 2026-07-12 |
| NVDA | $210.99 | $966,834,145 | Information Technology | large | unknown | 2026-07-12 |
| NVT | $160.96 | $20,794,196 | Industrials | mid | unknown | 2026-07-12 |
| NXPI | $292.10 | $47,511,160 | Information Technology | large | unknown | 2026-07-12 |
| NXT | $111.49 | $20,373,908 | Industrials | mid | unknown | 2026-07-12 |
| O | $63.32 | $24,137,344 | Real Estate | large | unknown | 2026-07-12 |
| ODFL | $227.57 | $22,902,819 | Industrials | large | unknown | 2026-07-12 |
| ON | $95.92 | $65,042,385 | Information Technology | large | unknown | 2026-07-12 |
| ONTO | $321.43 | $31,890,256 | Information Technology | mid | unknown | 2026-07-12 |
| ORCL | $140.68 | $172,309,676 | Information Technology | large | unknown | 2026-07-12 |
| ORLY | $86.22 | $32,142,932 | Consumer Discretionary | large | unknown | 2026-07-12 |
| OXY | $52.88 | $36,714,805 | Energy | large | unknown | 2026-07-12 |
| PANW | $325.82 | $86,713,333 | Information Technology | large | unknown | 2026-07-12 |
| PEP | $137.38 | $52,589,753 | Consumer Staples | large | unknown | 2026-07-12 |
| PFE | $24.19 | $64,899,656 | Health Care | large | unknown | 2026-07-12 |
| PG | $147.02 | $63,489,023 | Consumer Staples | large | unknown | 2026-07-12 |
| PGR | $230.67 | $36,226,630 | Financials | large | unknown | 2026-07-12 |
| PH | $960.77 | $38,977,375 | Industrials | large | unknown | 2026-07-12 |
| PINS | $22.51 | $20,935,872 | Communication Services | mid | unknown | 2026-07-12 |
| PLD | $140.83 | $22,741,804 | Real Estate | large | unknown | 2026-07-12 |
| PLTR | $126.75 | $158,066,052 | Information Technology | large | unknown | 2026-07-12 |
| PM | $181.62 | $37,384,065 | Consumer Staples | large | unknown | 2026-07-12 |
| PNC | $251.88 | $31,627,197 | Financials | large | unknown | 2026-07-12 |
| PPL | $35.78 | $23,362,798 | Utilities | large | unknown | 2026-07-12 |
| PSX | $188.34 | $25,508,130 | Energy | large | unknown | 2026-07-12 |
| PWR | $658.46 | $57,505,733 | Industrials | large | unknown | 2026-07-12 |
| PYPL | $46.33 | $28,032,198 | Financials | large | unknown | 2026-07-12 |
| QCOM | $189.11 | $123,035,715 | Information Technology | large | unknown | 2026-07-12 |
| RCL | $285.25 | $44,672,973 | Consumer Discretionary | large | unknown | 2026-07-12 |
| REGN | $664.56 | $43,225,528 | Health Care | large | unknown | 2026-07-12 |
| ROK | $472.28 | $23,759,435 | Industrials | large | unknown | 2026-07-12 |
| ROKU | $140.70 | $53,918,851 | Communication Services | mid | unknown | 2026-07-12 |
| ROST | $222.82 | $30,600,985 | Consumer Discretionary | large | unknown | 2026-07-12 |
| RRX | $214.81 | $22,331,738 | Industrials | mid | unknown | 2026-07-12 |
| RTX | $195.96 | $38,373,846 | Industrials | large | unknown | 2026-07-12 |
| SBUX | $106.00 | $35,281,577 | Consumer Discretionary | large | unknown | 2026-07-12 |
| SCHW | $103.12 | $66,482,028 | Financials | large | unknown | 2026-07-12 |
| SHW | $334.01 | $40,609,396 | Materials | large | unknown | 2026-07-12 |
| SLB | $47.77 | $50,341,908 | Energy | large | unknown | 2026-07-12 |
| SMCI | $28.31 | $72,749,526 | Information Technology | large | unknown | 2026-07-12 |
| SMTC | $136.12 | $28,787,670 | Information Technology | mid | unknown | 2026-07-12 |
| SNDK | $1916.50 | $581,926,453 | Information Technology | large | unknown | 2026-07-12 |
| SNPS | $445.46 | $40,719,254 | Information Technology | large | unknown | 2026-07-12 |
| SO | $95.61 | $28,686,560 | Utilities | large | unknown | 2026-07-12 |
| SPG | $218.76 | $20,550,110 | Real Estate | large | unknown | 2026-07-12 |
| SPGI | $430.40 | $57,812,649 | Financials | large | unknown | 2026-07-12 |
| STRL | $682.13 | $32,433,257 | Industrials | mid | unknown | 2026-07-12 |
| STT | $180.15 | $21,879,924 | Financials | large | unknown | 2026-07-12 |
| STX | $909.84 | $209,271,574 | Information Technology | large | unknown | 2026-07-12 |
| STZ | $133.99 | $21,506,521 | Consumer Staples | large | unknown | 2026-07-12 |
| SYK | $329.44 | $54,233,693 | Health Care | large | unknown | 2026-07-12 |
| T | $21.13 | $88,451,329 | Communication Services | large | unknown | 2026-07-12 |
| TDG | $1291.90 | $38,179,460 | Industrials | large | unknown | 2026-07-12 |
| TECH | $71.29 | $25,970,205 | Health Care | large | unknown | 2026-07-12 |
| TEL | $200.28 | $32,649,108 | Information Technology | large | unknown | 2026-07-12 |
| TER | $359.61 | $82,258,553 | Information Technology | large | unknown | 2026-07-12 |
| TFC | $51.69 | $36,377,727 | Financials | large | unknown | 2026-07-12 |
| TGT | $135.10 | $29,883,525 | Consumer Staples | large | unknown | 2026-07-12 |
| TJX | $151.27 | $44,672,224 | Consumer Discretionary | large | unknown | 2026-07-12 |
| TLN | $385.92 | $23,746,419 | Utilities | mid | unknown | 2026-07-12 |
| TMO | $526.95 | $55,784,841 | Health Care | large | unknown | 2026-07-12 |
| TMUS | $187.58 | $45,090,725 | Communication Services | large | unknown | 2026-07-12 |
| TRGP | $273.28 | $23,199,877 | Energy | large | unknown | 2026-07-12 |
| TRV | $338.86 | $23,274,922 | Financials | large | unknown | 2026-07-12 |
| TSCO | $30.43 | $26,829,705 | Consumer Discretionary | large | unknown | 2026-07-12 |
| TSLA | $407.77 | $403,129,208 | Consumer Discretionary | large | unknown | 2026-07-12 |
| TT | $479.78 | $36,967,234 | Industrials | large | unknown | 2026-07-12 |
| TTMI | $146.39 | $28,325,398 | Information Technology | mid | unknown | 2026-07-12 |
| TTWO | $243.18 | $31,950,546 | Communication Services | large | unknown | 2026-07-12 |
| TWLO | $214.69 | $22,844,784 | Information Technology | mid | unknown | 2026-07-12 |
| TXN | $311.49 | $115,710,388 | Information Technology | large | unknown | 2026-07-12 |
| UAL | $126.01 | $34,132,288 | Industrials | large | unknown | 2026-07-12 |
| UBER | $74.53 | $97,679,897 | Industrials | large | unknown | 2026-07-12 |
| UNH | $424.57 | $95,911,913 | Health Care | large | unknown | 2026-07-12 |
| UNP | $286.98 | $31,096,810 | Industrials | large | unknown | 2026-07-12 |
| UPS | $112.60 | $20,827,898 | Industrials | large | unknown | 2026-07-12 |
| URI | $1095.55 | $30,788,772 | Industrials | large | unknown | 2026-07-12 |
| USB | $62.42 | $38,944,770 | Financials | large | unknown | 2026-07-12 |
| V | $348.63 | $123,400,680 | Financials | large | unknown | 2026-07-12 |
| VLO | $280.58 | $38,881,240 | Energy | large | unknown | 2026-07-12 |
| VMC | $295.30 | $29,605,489 | Materials | large | unknown | 2026-07-12 |
| VRSK | $185.35 | $29,453,377 | Industrials | large | unknown | 2026-07-12 |
| VRTX | $485.36 | $41,428,371 | Health Care | large | unknown | 2026-07-12 |
| VSH | $44.65 | $22,971,229 | Information Technology | small | unknown | 2026-07-12 |
| VST | $158.79 | $29,429,904 | Utilities | large | unknown | 2026-07-12 |
| VZ | $42.11 | $97,096,697 | Communication Services | large | unknown | 2026-07-12 |
| WAT | $376.42 | $24,241,353 | Health Care | large | unknown | 2026-07-12 |
| WBD | $26.61 | $42,573,250 | Communication Services | large | unknown | 2026-07-12 |
| WBS | $76.53 | $20,630,983 | Financials | mid | unknown | 2026-07-12 |
| WDAY | $138.93 | $26,592,586 | Information Technology | large | unknown | 2026-07-12 |
| WDC | $582.61 | $241,448,570 | Information Technology | large | unknown | 2026-07-12 |
| WELL | $231.49 | $37,217,849 | Real Estate | large | unknown | 2026-07-12 |
| WFC | $87.08 | $87,538,125 | Financials | large | unknown | 2026-07-12 |
| WM | $233.35 | $23,717,594 | Industrials | large | unknown | 2026-07-12 |
| WMB | $75.00 | $30,697,493 | Energy | large | unknown | 2026-07-12 |
| WMT | $113.90 | $111,665,307 | Consumer Staples | large | unknown | 2026-07-12 |
| WWD | $406.78 | $26,814,702 | Industrials | mid | unknown | 2026-07-12 |
| XEL | $80.05 | $25,756,435 | Utilities | large | unknown | 2026-07-12 |
| XOM | $138.83 | $78,396,258 | Energy | large | unknown | 2026-07-12 |
| ZTS | $75.52 | $20,949,358 | Health Care | large | unknown | 2026-07-12 |
