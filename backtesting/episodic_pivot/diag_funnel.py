"""Diagnostic: per-filter pass counts on the surprise>=15% population, to confirm
the EP setup is genuinely selective (not a bug over-filtering)."""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ep_engine as E

ev = E.load_events()
cache = {t: E.cached_history(t) for t in list(ev.ticker.unique()) + ["SPY"]}

rows = []
for _, e in ev.iterrows():
    h = cache.get(e["ticker"])
    if h is None:
        continue
    f = E.compute_features(h, e["earn_date"])
    if f is None or pd.isna(f["vol_ratio"]):
        continue
    rows.append({"year": e["year"], "surprise": e["surprise_pct"], "gap": f["gap"],
                 "vol_ratio": f["vol_ratio"], "range_pos": f["range_pos"],
                 "ann_ret": f["ann_ret"],
                 "open_gt_20dhigh": f["ann_open"] > f["prior20_high"]})
d = pd.DataFrame(rows)
print("events with features:", len(d))
sub = d[d["surprise"] >= 15].copy()
print("surprise>=15%:", len(sub))
conds = {
    "gap>=5%": sub["gap"] >= 0.05,
    "vol>=2x": sub["vol_ratio"] >= 2.0,
    "open>20d-high": sub["open_gt_20dhigh"],
    "range>=0.75": sub["range_pos"] >= 0.75,
    "annret>=4%": sub["ann_ret"] >= 0.04,
}
print("\nIndividual filter pass-rate on surprise>=15% population:")
for k, v in conds.items():
    print(f"  {k:16s}: {int(v.sum()):4d} / {len(sub)}  ({100*v.mean():.1f}%)")
allc = np.logical_and.reduce([v.values for v in conds.values()])
print(f"\n  ALL EP conditions (+surprise): {int(allc.sum())} / {len(sub)}")
print("\nBy year (surprise>=15% -> all EP conds):")
for y in sorted(sub["year"].unique()):
    m = sub["year"] == y
    a = np.logical_and.reduce([c.values for c in conds.values()]) & m.values
    print(f"  {y}: surprise15={int(m.sum()):4d}  full-EP={int(a.sum())}")
# incremental (cumulative AND) funnel
print("\nCumulative AND funnel:")
cum = pd.Series(True, index=sub.index)
for k, v in conds.items():
    cum = cum & v
    print(f"  after {k:16s}: {int(cum.sum())}")
