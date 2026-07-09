# Backtest — ELEVATED_BAR health threshold (S1), research-only comparison

*Generated 2026-07-08. **Diagnostic only.** No `strategy.md` edit, no orders, not merged into the
live 7-routine system. Reconstructed entirely from committed repo CSVs (no network). Survivorship-biased
(current S&P 500 constituents), zero transaction costs/slippage — same limitations as every prior report
in `backtesting/`.*

Grid tested: health threshold ∈ **{0.0% (baseline/live), −0.5%, −1.0%, −1.5%}**. Lowering the threshold
makes ELEVATED_BAR trigger **less** often (only when realized health is more deeply negative).

---

## TL;DR (raw counts in every cell below; flagged results are diagnostic, not validated)

1. **The health threshold is nearly inert on the actual (live-faithful) traded strategy.** Over 2022–2025,
   moving the threshold across the whole grid {0.0 → −1.5} changes the enhanced traded book by **~13 trades
   (out of ~206)** and leaves win rate, avg return, profit factor, per-trade Sharpe and drawdown essentially
   unchanged (avg return 2.16%→2.17%; per-trade Sharpe 0.196→0.198). Turning the overlay **off entirely**
   (always-NORMAL) barely moves it either (n=219, avg 2.17%).
2. **The trades ELEVATED_BAR blocks were, in hindsight, net WINNERS, not losers** — so the gate did not add
   value on this candidate stream and, if anything, marginally cost return. Enhanced bar, blocked at 0.0:
   **n=13, 53.8% win, +2.41% avg, PF 2.93** (vs admitted +2.16%). Base-bar (larger sample) blocked at 0.0:
   **n=130, 58.5% win, +2.18% avg** vs admitted **+1.58%**. Direction is consistent; **samples are small**.
3. **Why:** the live realized-health metric is **market-wide** (mean outcome of *all* S&P 500 EPS-beat base
   trades) — it flags when the *average* beat drifts down, but the strategy actually trades the *high-surprise,
   high-quality* subset, which kept drifting up even when the average did not. The market-wide gate is a weak
   predictor of the enhanced subset's outcomes.
4. **Availability gate: PARTIAL PASS.** Posture/health series is reconstructable 2022→2026-06-04; the
   EPS-bar retained-vs-blocked trade counterfactual is reconstructable 2022–2025. **A true portfolio-level
   equity curve (CAGR / daily-MTM Sharpe / max drawdown) is NOT reconstructible** and is deliberately **not
   reported as a backtest** (two load-bearing inputs are missing — see §2). 2026 has **no** portfolio
   counterfactual (base candidate population unavailable).
5. **Step-7 sanity check FAILED on exact values.** My baseline (0.0%) reconstruction reads **+0.28%…+0.38%
   (NORMAL, n≈393–426)** at the three June-2026 dates where the live `pead_health.md` logged **−2.08% / −1.025%
   / −0.492% (ELEVATED_BAR, n=211/282/367)**. Direction agrees (weak, recovering spring 2026); levels and the
   zero-crossing do **not** reconcile. This caps confidence in all numbers here.

**No threshold is recommended. Only the human operator edits `strategy.md`.**

---

## Step 1 — the live logic, read from the code (verbatim), not assumed

Sources read: `memory/pead_health.md`, `compute_pead_health.py` (root, production), its engine
`backtest_pead_2026_ytd.py` (root), and `memory/strategy.md`.

### (a) Exact 60-day realized-health formula

From `compute_pead_health.py` (lines 43–130). For run date `today`:

- Scan **S&P 500** constituents (`eng.get_sp500()`). For each earnings date in `[today−110d, today]` with
  `reported > estimate` (**any positive EPS beat**, no surprise-magnitude floor):
  - entry = **2nd trading day after** the earnings date (`ENTRY_DELAY = 2`); require entry ≤ today, price ≥
    `MIN_PRICE=$10`, 20-day avg $-volume ≥ `MIN_AVG_DVOL=$20M`.
  - outcome = `eng.simulate_trade(hist, entry, BASE_TRAIL_PCT=0.07)` = **−8% hard stop / +10% trigger → 7%
    trailing stop / 42-calendar-day time stop** (full position; **no** 1/3 scale-out — the live health metric
    itself omits it). Skip if still open (`exit_reason == "data_end"`).
  - keep only trades whose **exit date** `xd` satisfies `today−60d ≤ xd ≤ today`.
- `health = mean(return_pct×100)` over the kept trades **iff** `n ≥ MIN_SAMPLE=20`, else `None`.
- `health_ok = (health is None) or (health ≥ HEALTH_THRESHOLD)`; `posture = ELEVATED_BAR if not health_ok else NORMAL`.

**Precise definitions (as Step 2 requires):** "60-day" = **60 calendar days**; the controlling timestamp is the
**EXIT (realized-close) date**; entry is fixed at earn-date **+2 trading days**; thin-data (`n<20`) **fails open
to NORMAL**.

### (b) Exact current threshold

`HEALTH_THRESHOLD = 0.0` (`compute_pead_health.py:47`). `health_ok` requires `realized_health_60d_pct ≥ 0.0`.
`pead_health.md` front-matter confirms `health_threshold_pct: 0.0`. It is documented as **untuned** ("Threshold
is 0 (untuned)").

### (c) Exactly what changes when posture flips to ELEVATED_BAR

From `pead_health.md` and cross-checked with `strategy.md`:
- **EPS-surprise bar raised to `>20%` for ALL sectors** (overrides the standard 15%, and the sector-specific
  20% for Utilities/Real Estate/Industrials/Energy — i.e., every sector now needs >20%).
- **New positions capped at 2** for the session (`pead_health.md`: "caps new positions at 2 for the session";
  `strategy.md` bear-regime analogue: "max new positions to 2 per week"). *Interpretation used here: 2 new
  positions/week — see §2 caveat on the session-vs-week ambiguity.*
- It **never halts trading** and **never affects exits**. It is a NEW-entry "raise the bar" overlay only.
- The SPY-200MA regime gate lives **separately** in `strategy.md` and is not part of this overlay.

### ⚠️ Correction to the task's stated construction (this is why Step 1 says "read the actual logic")

The task prompt asks each threshold to "generate its own **recursive** posture and portfolio history" and warns
that "a blocked trade must be allowed to change future … **realized health**." **That premise does not match the
live system.** The live realized-health metric is computed over the **entire S&P 500 EPS-beat population**, and
`compute_pead_health.py` **never references the portfolio's own trades**. Therefore:

- **A blocked trade does NOT change future realized health.** The health series is **market-wide and identical
  across thresholds** — reusing one health series across thresholds is not a forbidden shortcut here, it is the
  *correct* live behaviour. (The prompt's prohibition on reusing a health series was premised on a
  portfolio-recursive metric the live system does not use.)
- The **genuine** path-dependence (cash, open slots, sector exposure, which later candidates get entered)
  operates only through the **position caps** — and, as §2 shows, that dimension is exactly the part that is
  **not reconstructible** from committed data.
- The EPS-bar gate itself is a **per-candidate mechanical test** (is this beat >20%?) that needs **no**
  recursion at all.

So the faithful construction is: **one market-wide health series → per-threshold posture → per-candidate EPS-bar
gate**, which is what this report implements.

---

## Step 2 — candidate-stream availability gate (run before anything else): **PARTIAL PASS**

The recursive counterfactual needs three inputs. Their availability differs:

| Input | Needed for | Source in repo | Available? |
|---|---|---|---|
| Market-wide realized-health series | posture / threshold flips | `backtest_signal_health_candidates.csv` (8,190 rows, 2021→2026-06-04; `ret_base` = the exact `simulate_trade(·,0.07)` outcome the live metric averages; `exit_date`) | **YES, 2022 → 2026-06-04** |
| Pre-posture tradeable candidate stream **with `surprise_pct` + `sector`** | EPS-bar admit/block decision | `backtest_trades_PEAD_2022_2025_ENHANCED_base.csv` (5,836 rows = **every positive EPS beat** passing the $10/$20M liquidity gate; surprise from ~0% up — 4,331 rows are <15%; has `ret_trail7`, `entry_date`, `holding_days`, filter booleans) | **YES, 2022–2025 only** |
| Same, for **2026** | 2026 portfolio counterfactual | only `backtest_trades_PEAD_2026_YTD.csv` = **30 already-filtered** trades (all surprise≥15 & q==3); the full 2026 base population is explicitly **absent** ("yfinance earnings endpoint blocked", per the risk-sweep report) | **NO** |
| Cap-binding **selection rule** | resolving which of >2 weekly qualifiers to keep | the live pre_market **conviction score** (guidance magnitude, analyst upgrades, call tone, insider, sector-ETF, short-interest, regulatory) — **not reconstructible from price+earnings**, documented repo-wide | **NO** |
| Daily position **marks** | true daily-MTM equity curve → CAGR/Sharpe/maxDD | committed CSVs hold **per-trade returns + entry/exit dates only** — no daily marks | **NO** |

**Verdict.**
- The candidate **stream** (including candidates blocked at the EPS bar) **is** present for 2022–2025, so the
  gate **passes** for the EPS-bar counterfactual over that window — reported in §4–§5.
- It **fails** for **2026** (no base population) and for the **position-cap** dimension of ELEVATED_BAR (needs the
  unbacktestable conviction score).
- A true portfolio **CAGR / daily-MTM Sharpe / max drawdown** is therefore **not validly reconstructible**, and
  per the task's own honesty clause it is **not reported as a full backtest.** What follows is the rigorous
  EPS-bar retained-vs-blocked trade analysis (needs no selection score), plus a clearly-labelled per-trade
  dispersion view — **never** a portfolio equity curve.

**Population note:** the two files draw the same "all-positive-beats, +2d, liquidity-gated" universe but from
different builds (5,890 vs 5,836 rows for 2022–2025 — ~1% diff from data-vintage/warm-up). Health uses the
purpose-built full-span file; tradeable candidates use the surprise+sector file. Cross-checked consistent on the
hand-verify dates (§3).

---

## Step 3 — canonical validation before the grid

Hand-verified 5 dates by recomputing `health(D) = mean(ret_base | exit_date ∈ (D−60cal, D])` and its baseline
(0.0) posture directly from the row-level data. Because health is market-wide (not portfolio state), the
relevant reconciliation is **regime plausibility** and internal consistency (not "cash + positions = equity",
which does not apply to a market-wide gauge). All five are sensible:

| Date | 60-day window | n | mean `ret_base` | posture@0.0 | in-window win% | regime read |
|---|---|--:|--:|:--:|--:|---|
| 2022-06-15 | (04-16, 06-15] | 317 | **−5.86%** | ELEVATED_BAR | 17.4% | 2022 bear — correctly ELEVATED |
| 2023-06-15 | (04-16, 06-15] | 270 | +0.05% | NORMAL (barely) | 45.6% | flat recovery |
| 2024-06-28 | (04-29, 06-28] | 346 | +1.80% | NORMAL | 59.8% | healthy tape |
| 2025-06-16 | (04-17, 06-16] | 261 | +6.31% | NORMAL | 78.2% | strong tape |
| 2026-06-04 | (04-05, 06-04] | 426 | +0.38% | NORMAL (knife-edge) | 45.3% | weak/recovering |

Thin-data fail-open days across 2022–2026: **0** (the 60-day window is always ≥20 by design). The recursive
mechanics that *do* apply here (posture derived only from trades whose exit precedes D — no look-ahead) are
respected: every trade entering a health window has already closed on or before D.

---

## Step 4 — grid: posture timeline per threshold (fully reconstructed, exact)

% of trading days (business-day calendar; excludes exchange holidays — immaterial to a percentage) in
ELEVATED_BAR posture, by period and threshold:

| Period | trading days | @0.0 (live) | @−0.5 | @−1.0 | @−1.5 |
|---|--:|--:|--:|--:|--:|
| **IS 2022–2024** | 782 | 48.6% | 44.9% | 36.1% | 29.8% |
| **OOS 2025** | 261 | 38.7% | 36.8% | 35.2% | 32.2% |
| 2026 (partial → 06-04) | 111 | 70.3% | 69.4% | 68.5% | 65.8% |
| ALL | 1,154 | 48.4% | 45.4% | 39.0% | 33.8% |

Lowering the threshold does meaningfully reduce ELEVATED frequency in-sample (48.6%→29.8% IS) but only modestly
OOS (38.7%→32.2%) — in 2025 the negative excursions were mostly deep enough to clear even −1.5. 2026 spring was
deeply negative (Mar–May health −2 to −3, i.e., ELEVATED at every threshold) and recovered to a knife-edge
+0.38% by 06-04.

---

## Step 5 — per-threshold results (2022–2025; IS/OOS separated, never averaged)

### 5a. Enhanced bar — the live-faithful traded set (surprise≥15 non-deprio / ≥20 deprio, **q==3**, not-near-earnings)

**Admitted book** (what the strategy trades under each threshold), per-trade stats from actual `ret_trail7`:

| | IS 2022–2024 | | | | OOS 2025 | | | |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **thr** | n | win% | avg% | PF | n | win% | avg% | PF |
| 0.0 (live) | 163 | 58.3 | 2.306 | 1.85 | 43 | 48.8 | 1.594 | 1.47 |
| −0.5 | 165 | 57.6 | 2.253 | 1.84 | 43 | 48.8 | 1.594 | 1.47 |
| −1.0 | 166 | 57.8 | 2.319 | 1.87 | 43 | 48.8 | 1.594 | 1.47 |
| −1.5 | 166 | 57.8 | 2.319 | 1.87 | 43 | 48.8 | 1.594 | 1.47 |

The book barely moves (IS swings by 3 trades; **OOS is identical** — no enhanced qualifier landed in the 15–20%
band on an ELEVATED day in 2025). Per-trade dispersion (ALL 2022–2025, **per-trade — NOT a daily-MTM portfolio
curve**; 11% notional, sequence-compounded drawdown, no concurrency/cash constraint):

| thr | n | avg% | per-trade Sharpe | trade-sequence maxDD |
|---|--:|--:|--:|--:|
| 0.0 | 206 | 2.157 | 0.196 | −12.0% |
| −0.5 | 208 | 2.117 | 0.193 | −12.4% |
| −1.0 | 209 | 2.170 | 0.198 | −12.4% |
| −1.5 | 209 | 2.170 | 0.198 | −12.4% |
| *overlay OFF (always-NORMAL)* | 219 | 2.172 | 0.202 | −12.0% |

**Blocked trades** (normal-eligible but killed by the >20% bar on an ELEVATED day) — *were they winners or losers
in hindsight?*

| thr | n blocked (IS+OOS) | win% | avg `ret_trail7` | PF | verdict |
|---|--:|--:|--:|--:|---|
| 0.0 | **13** (13 IS, 0 OOS) | 53.8 | **+2.41%** | 2.93 | **winners** → blocking cost return |
| −0.5 | 11 | 63.6 | +3.21% | 3.91 | winners |
| −1.0 | 10 | 60.0 | +2.22% | 2.83 | winners |
| −1.5 | 10 | 60.0 | +2.22% | 2.83 | winners |

**Marginal effect of loosening from 0.0** (trades blocked by 0.0 but admitted by the lower threshold, i.e.
entered on days with health ∈ [thr, 0)): 0.0→−0.5 **n=2** (−2.04% avg); 0.0→−1.0 **n=3** (+3.01%); 0.0→−1.5 **n=3**
(+3.01%). Samples are **too small to conclude**; shown for completeness.

### 5b. Base bar — drop the q==3 quality filter for a larger, higher-power sample (robustness, less live-faithful)

| thr | admitted n | admitted avg% | **blocked n** | **blocked win%** | **blocked avg%** | blocked PF |
|---|--:|--:|--:|--:|--:|--:|
| 0.0 | 1,229 | 1.577 | **130** | 58.5 | **+2.184** | 1.78 |
| −0.5 | 1,242 | 1.508 | 117 | 63.2 | +2.988 | 2.18 |
| −1.0 | 1,262 | 1.631 | 97 | 57.7 | +1.696 | 1.57 |
| −1.5 | 1,273 | 1.664 | 86 | 53.5 | +1.206 | 1.36 |

At the base bar the signal is clearer and same-signed: **blocked trades (+2.18% avg, 58.5% win) beat the admitted
book (+1.58%)** at threshold 0.0 → the gate removed better-than-average trades. Marginal 0.0→−0.5 is a noisy
loss (**n=13, +…−5.05% avg**, one bad cluster), but 0.0→−1.0 (n=33, +3.62%) and 0.0→−1.5 (n=44, +4.10%) add
winners — i.e., beyond the first increment, loosening re-admits mostly-profitable trades. Non-monotonic and
sample-thin; directional only.

**Swing universe (max blockable):** enhanced **48** trades (39 IS, 9 OOS) over 4 years; base bar **299**. Full
48-row enhanced list in the Appendix and in `backtesting/reports/backtest_elevated_bar_swing_2026-07-08.csv`.

### 5c. What is deliberately NOT reported (and why)

- **Portfolio CAGR, daily-MTM Sharpe, max drawdown, % blocked-slots-later-refilled** — require (i) daily position
  marks (absent) and (ii) the cap-binding conviction score (unbacktestable). At the enhanced density (~1.2
  qualifiers/week, clustered to 13 in a peak week), the 2-per-week ELEVATED cap and the 8-concurrent / 90%-cash
  / 30%-sector caps **do** bind in earnings-season clusters, so a portfolio composition is genuinely
  selection-sensitive and cannot be pinned down. Reporting a portfolio equity curve would be fabricating the
  selection mechanism. Per the task's Step-2 clause, these figures are withheld rather than guessed.
- The analysis above **isolates the EPS-bar gate**; the **position-cap** half of ELEVATED_BAR is not captured.

---

## Step 6 — time split

- **IS = 2022–2024** and **OOS = 2025** are reported **separately** throughout §4–§5 (never averaged).
- **2026 YTD:** data coverage does **not** support a portfolio counterfactual (no base candidate population;
  only 30 pre-filtered trades). The **health/posture series** is reconstructable through **2026-06-04** (§4, §7)
  but not beyond, and cannot be certified against the live readings (§7). So 2026 is reported for **posture
  only**, with an explicit reconciliation failure — **not** as an OOS trade result.

---

## Step 7 — current-moment relevance + reconciliation vs live `pead_health.md`

**Reconciliation (the sanity check that the reconstruction itself is correct): does NOT match exactly.**

| live `pead_health.md` (logged) | reconstruction (this report) |
|---|---|
| 2026-06-05: −2.08%, n=211, **ELEVATED_BAR** | +0.38%, n=426, NORMAL |
| 2026-06-14: −1.025%, n=282, **ELEVATED_BAR** | +0.29%, n=398, NORMAL |
| 2026-06-21: −0.492%, n=367, **ELEVATED_BAR** | +0.28%, n=393, NORMAL |

- **Direction agrees:** the reconstruction shows 2026 spring deeply negative (Mar–May health −2 to −3, ELEVATED
  at every threshold) recovering toward zero by June — the same "weak but improving" arc the live −2.08→−1.03→−0.49
  trend shows.
- **Levels and the zero-crossing do NOT reconcile:** the reconstruction sits ~0.7–2.5 pts higher and crosses to
  *positive* right at the June boundary, so it reads **NORMAL** where the live system read **ELEVATED_BAR**.
- **Most likely causes (not fully resolvable from here):** (i) the committed research file's data ends
  **2026-06-04**, before all three live as-of dates; (ii) my window carries **~2× the sample** (n≈393–426 vs live
  211–367), consistent with the live June runs computing on a **partial S&P 500 fetch** — the repo's own logs
  document `yfinance` transport failures + Yahoo HTTP 429 on the shared egress IP in this exact period; (iii)
  different constituent-list snapshot / EPS revisions between builds. A smaller, incompletely-fetched live sample
  can easily skew below zero near a knife-edge reading.
- **Consequence:** the reconstruction validates the **methodology** (the hand-checks in §3 are internally sound)
  but **cannot be certified against the live numbers.** Every threshold figure here inherits that uncertainty —
  a further reason to treat this as diagnostic only. *(It also raises a separate, out-of-scope question for the
  operator: whether the live June-2026 ELEVATED_BAR posture was partly a data-completeness artifact. Flagged, not
  concluded.)*

**Current-moment posture.** Using the latest computable health (as-of the 2026-06-04 data end): reconstructed
health **+0.38% (n=426) → NORMAL at all four thresholds.** The live book has, in practice, been treating the
overlay as **STALE → NORMAL** since it expired 2026-06-28 (per recent `pre_market` logs), with the last fresh
reading being ELEVATED_BAR (−0.492%, Jun 21). So at this moment the threshold choice is **moot** — every
candidate value yields NORMAL on the reconstructable data. (Live 2026-06-21 was ELEVATED only under the
un-reconcilable live sample.)

---

## Discipline notes & caveats

- **Raw counts shown for every rate.** The load-bearing swing samples are **small**: 13 enhanced blocked / 130
  base blocked over four years; marginal increments of 2–13 trades. Treat all "blocked were winners" statements
  as **directional**, not established.
- **Flagged-as-suspicious-until-re-derived:** the "blocked trades outperform admitted" result and the very high
  blocked PFs (2.9–3.9) were re-derived independently at both the enhanced and base bars and by inspecting the
  actual 48-name swing list (Appendix) — the pattern holds, but on small n and survivorship-biased, cost-free
  data. Not validated.
- **Survivorship + no costs/slippage** inflate every absolute return here (both admitted and blocked share the
  bias, so the *comparison* is the more reliable read).
- **Session-vs-week ambiguity** in the ELEVATED cap ("2 for the session" vs "2 per week") is unresolved in the
  live docs; it does not affect the EPS-bar results above (which don't model the cap) but would matter to any
  future portfolio sim.
- **No recommendation.** Nothing here is validated; no threshold is endorsed. Only the human operator edits
  `strategy.md`. This artifact is diagnostic input for that decision, not the decision.

---

## Appendix

### A. Method / data lineage
- **Health series:** `backtest_signal_health_candidates.csv` → `health(D)=mean(ret_base | exit_date∈(D−60cal,D])`,
  n≥20 else NORMAL. `ret_base = simulate_trade(entry, 0.07)` = the exact live metric input.
- **Tradeable candidates:** `backtest_trades_PEAD_2022_2025_ENHANCED_base.csv`; outcome = `ret_trail7` (same
  7%-trail engine, health-consistent). NORMAL bar = surprise≥15 (non-deprio) / ≥20 (Util/RE/Ind/Energy) & q==3 &
  not-near-earnings; ELEVATED bar = surprise≥20 all sectors & q==3 & not-near-earnings. (Industrials/Energy
  streak≥2 rule not modelled — those sectors need >20% under both postures, so they never enter the swing set.)
- Reproduction script: `backtesting/scripts/backtest_elevated_bar_threshold.py`. Artifacts:
  `backtesting/reports/backtest_elevated_bar_health_series_2026-07-08.csv`,
  `backtesting/reports/backtest_elevated_bar_swing_2026-07-08.csv`.

### B. The 48 enhanced swing trades (surprise 15–20%, non-deprioritized, q==3) — the only trades ELEVATED_BAR can block

See `backtest_elevated_bar_swing_2026-07-08.csv`. Notable: winners NVDA +7.25, CAH +9.41, ANET +13.12, WFC
+23.66, APP +37.52; losers REGN −9.95, PPG −9.04, MTB −8.30, META −9.13. On ELEVATED days (health<0), the IS
subset (n=12–13) still averaged **+2.4–2.7%** — the basis for the "blocked were winners" finding.
