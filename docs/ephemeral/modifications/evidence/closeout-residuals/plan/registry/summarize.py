#!/usr/bin/env python3
"""Build row_assertions.json (the shape plan/r1/engine/dryrun.py load_guards() reads) from guards.py.

Forbidden guards: "regression" = "inject into <ROW>: <text>" (dryrun strips the prefix and appends <text> as its
own line to the edited body). Required guards: "regression" = "in <ROW>, put the retired wording back in place of
the new text: <text>" (dryrun tests required guards by removal instead). Every <text> is at most 15 words (P-12).
The TBD guard (G-K52) is emitted with an empty pattern, which load_guards() skips, and "status": "TBD".
Round 2: decision labels P-55 (G-K55), P-61 (G-K24 on 20 rows) and P-62 (G-K39 back on RS-40).
"""
import json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import guards as G  # noqa: E402

DECISION = {"K08": "P-17", "K19": "P-06 (PR-10)", "K22": "P-01 (unchanged)", "K26": "P-08, P-42", "K35": "P-02, P-03, P-40",
            "K36": "P-02", "K39": "P-04, P-62", "K40": "P-04", "K47": "P-15 (revised)", "K52": "P-18, P-42",
            "K53": "P-38, P-42", "K54": "P-19, P-42", "K02": "P-05 (rows unchanged)", "K14": "P-13", "K50": "P-14 (unchanged)",
            "K24": "P-61", "K55": "P-55"}


def rows_of(sel):
    return ["ALL55 (every row)"] if sel == G.ALL55 else list(sel)


def reg_line(kind, row, text):
    if kind == "forbidden_regex":
        return f"inject into {row}: {text}"
    return f"in {row}, put the retired wording back in place of the new text: {text}"


out = []
for gid, rules, part, kind, value, rid, sel in G.GUARDS:
    R = G.REGRESSIONS[gid]
    base = {"rule_id": f"G-{gid} " + ", ".join(rules), "part": part, "kind": kind, "rule_code": rid,
            "decision": DECISION.get(gid, "")}
    if value == G.TBD:
        text = R["*"]
        out.append({**base, "rows": list(sel), "pattern": "", "status": "TBD",
                    "candidate": G.CL30_A2_CANDIDATE, "candidate_source": "plan/r1/dry/B/report.json proposed_guard",
                    "regression": reg_line(kind, sel[0], text), "regression_words": len(text.split()),
                    "note": "apply_registry.py refuses to build while this is TBD; --allow-tbd omits it"})
        continue
    if isinstance(value, dict):
        groups = {}
        for r in sel:
            groups.setdefault(value[r], []).append(r)
        items = list(groups.items())
    else:
        items = [(value, rows_of(sel))]
    for pat, rws in items:
        if rws[0].startswith("ALL55"):
            first, per_row = "CL-20", {}
        else:
            first, per_row = rws[0], {r: (R.get(r) or R.get("*")) for r in rws}
        text = R.get(first) or R.get("*")
        e = {**base, "rows": rws, "pattern": pat, "regression": reg_line(kind, first, text), "regression_words": len(text.split())}
        if per_row and len(set(per_row.values())) > 1:
            e["regressions_per_row"] = {r: reg_line(kind, r, t) for r, t in per_row.items()}
        out.append(e)
for label, rid in G.RELEASE_LABELS:
    t = G.RELEASE_INJ[label]
    out.append({"rule_id": "PART-17 ITEM-36 (replaces the \\A{0,7} window guard in place, same list position)", "part": "PART-17",
                "rows": ["ALL55 (every row)"], "kind": "forbidden_regex", "pattern": G.NEW_HDR + label + G.NEW_END,
                "rule_code": rid, "decision": "P-16", "regression": f"inject into CL-20: {t}", "regression_words": len(t.split())})
out += [
    {"rule_id": "R-CLAT (PART-18, ITEM-37): required removed", "part": "PART-18", "rows": G.CLAT8, "kind": "other",
     "pattern": "Decide it during work", "rule_code": "CTR-002 (removed from required_regex)", "decision": "ITEM-37",
     "regression": "none needed: the forbidden twin G-K51 carries the regression; the Material required regex stays on all 10 rows and PR-30/PR-35 keep the required decide pattern"},
    {"rule_id": "PR-40 inputs (P-01)", "part": "PART-13", "rows": ["PR-40"], "kind": "other", "pattern": "",
     "rule_code": "none", "decision": "P-01",
     "regression": "not an assertion: the PR_REFS input follows LPR-40-4, and P-01's sentence becomes its own input entry before W-4 (LPR-40-5)"},
    {"rule_id": "CL-40 mutations.allowed (PART-06)", "part": "PART-06", "rows": ["CL-40"], "kind": "other", "pattern": "",
     "rule_code": "none", "decision": "ruling 5 Q1 (A)", "regression": "not an assertion: one allowed entry names the Candidate CRD Items List page write"},
    {"rule_id": "ITEM-07 (PART-03)", "part": "PART-03", "rows": [], "kind": "other", "pattern": "", "rule_code": "none",
     "regression": "none: a governance-audit behavioral-fixture prose line, not a registry row; §A lists ITEM-07 as unguarded (D24 review holds it)"},
    {"rule_id": "R-ITEM38 (PART-15)", "part": "PART-15", "rows": ["PR-10"], "kind": "other", "pattern": "material change \\(D23-C\\) change\\b",
     "rule_code": "none", "regression": "not placed: §A lists ITEM-38 as unguarded (a typo with no behaviour); the regex is the drafter's readback check only"},
    {"rule_id": "R-ITEM23, R-ITEM40 (PART-11)", "part": "PART-11", "rows": ["GCFPE-MGMT-10-PROPOSED (not a registry row)"], "kind": "other",
     "pattern": G.RELEASE_ALL, "rule_code": "none", "decision": "P-09, P-16",
     "regression": "not placed: the proposed body has no registry row; the PART-11 gate runs R-ITEM40's pattern and then R-ITEM23's (this one) directly"},
]
over = [o["rule_id"] for o in out if o.get("regression_words", 0) > 15]
assert not over, over
json.dump(out, open(HERE + "/row_assertions.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(out), "entries;", sum(1 for o in out if o["kind"] in ("forbidden_regex", "required_regex") and o["pattern"]), "with a pattern;",
      "TBD:", [o["rule_id"] for o in out if o.get("status") == "TBD"])
