"""
Checks the PEAD portfolio simulation report before it is committed
(adapted from check_etf_trend_v2_report.py). Fails (exit 1) on:
  1. any markdown table row whose cell count differs from its header
     (a stray pipe character inside a cell);
  2. any claim in the claims JSON whose value differs from the table cell it
     cites, or whose prose line is missing from the report;
  3. any number in prose (outside tables, code fences and `code` spans) that
     is neither a cited table value on that line nor a pre-registered constant
     listed in ALLOWED below.

Usage: python3 check_pead_portfolio_report.py <report.md> <claims.json>
"""

import json
import re
import sys

# Pre-registered constants and conventions that may appear in prose. Results
# never appear here: they must be cited from a table.
ALLOWED = {
    "0", "1", "2", "3", "5", "7", "8", "10", "13", "15", "20", "30", "40", "42", "45", "52",
    "60", "100", "200", "252", "500",
    "1.5", "8%", "-8%", "10%", "11%", "15%", "20%", "30%",
}
YEAR = re.compile(r"^(19|20)\d\d$")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
NUM = re.compile(r"(?<![A-Za-z0-9.^_])[-−+]?\d+(?:\.\d+)?%?")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def main(md_path, claims_path):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    claims = json.load(open(claims_path, encoding="utf-8"))
    errors = []

    # ---- parse tables
    tables, tid, fence = {}, None, False
    prose = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            fence = not fence
            i += 1
            continue
        if fence:
            i += 1
            continue
        m = re.match(r"<!-- table:(\S+) -->", ln)
        if m:
            tid = m.group(1)
            i += 1
            continue
        if ln.startswith("|"):
            hdr = cells(ln)
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                r = cells(lines[j])
                if len(r) != len(hdr):
                    errors.append(f"line {j+1}: table row has {len(r)} cells, header has {len(hdr)} "
                                  f"(pipe inside a cell?): {lines[j][:100]}")
                rows.append(r)
                j += 1
            if tid:
                tables[tid] = (hdr, rows)
            tid = None
            i = j
            continue
        prose.append((i + 1, ln))
        i += 1

    # ---- claims vs tables
    by_line = {}
    for c in claims:
        by_line.setdefault(c["line"], []).append(c)
        if c["line"] not in lines:
            errors.append(f"claimed prose line not found in report: {c['line'][:100]}")
        for r in c["refs"]:
            t = tables.get(r["table"])
            if t is None:
                errors.append(f"claim cites missing table {r['table']}")
                continue
            hdr, rows = t
            match = [x for x in rows if x[0] == r["row"]]
            if len(match) != 1 or r["col"] not in hdr:
                errors.append(f"claim cites missing cell {r['table']}/{r['row']}/{r['col']}")
                continue
            cell = match[0][hdr.index(r["col"])]
            if cell != r["value"]:
                errors.append(f"MISMATCH {r['table']}/{r['row']}/{r['col']}: prose '{r['value']}' "
                              f"vs table '{cell}'")
            if r["value"] not in c["line"]:
                errors.append(f"cited value '{r['value']}' not present in its prose line")

    # ---- every prose number must be cited or an allowed constant
    for n, ln in prose:
        if ln.startswith("<!--"):
            continue
        rest = re.sub(r"`[^`]*`", " ", ln)
        for c in by_line.get(ln, []):
            for r in sorted(c["refs"], key=lambda r: -len(r["value"])):
                rest = rest.replace(r["value"], " ", 1)
        rest = DATE.sub(" ", rest)
        for tok in NUM.findall(rest):
            t = tok.lstrip("+").replace("−", "-")
            if t in ALLOWED or YEAR.match(t):
                continue
            errors.append(f"line {n}: uncited number '{tok}' in prose: {ln[:120]}")

    n_refs = sum(len(c["refs"]) for c in claims)
    if errors:
        print(f"REPORT CHECK FAILED — {len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"REPORT CHECK PASSED — {len(tables)} tables, {len(claims)} prose lines with "
          f"{n_refs} cited numbers, no uncited prose numbers, no malformed table rows.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
