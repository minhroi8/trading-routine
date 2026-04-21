# Trade Log

Append-only ledger of every fill. Entries older than 30 days are rotated to `memory/archive/trade_log_<YYYY-MM>.md` at the start of each run.

| date | time_et | ticker | side | qty | price | rationale | commit_sha |
|------|---------|--------|------|-----|-------|-----------|------------|
