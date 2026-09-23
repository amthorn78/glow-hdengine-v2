#!/usr/bin/env python3
"""Measure four G06 alternatives on the E3 bodies, in memory (plan's-author request after the first E4).

usage: <{id: unedited body} JSON> | PYTHONDONTWRITEBYTECODE=1 python3 g06_alternatives.py <edited-skills-root>

(a) G06 as it is in the registry.
(b) (a) with a NEXT_PROMPT_HANDOFF token preceded by "no " (so also "contains no "), with or without an
    opening backtick, excluded by negative lookbehind.
(c) (a) with its window also ended at C-HANDOFF's closing "unlinked filenames." and at a heading line.
(d) (a) without "working branch" and "remote head" in its term list. This one is a weakening.

For each alternative, it reports:
- the hits on the 54 edited main bodies;
- whether both §7.3 G06 regressions (PR-35) still yield exactly that alternative's finding;
- whether every canonical text and the seven §7.3 combined paragraphs stay clean.

It prints JSON holding no body text beyond matched phrases of 12 words or fewer, and writes nothing.
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_rules as R  # noqa: E402

K = Path(sys.argv[1])
sys.path.insert(0, str(K / "amthor-workspace-governance-audit/scripts"))
import audit_workspace_governance as A  # noqa: E402

T = R.T
raw = json.load(sys.stdin)
edited, _ = R.apply(raw)
reg = A.load_data(R.REGISTRY)
rows = {r["prompt_key"]: r for r in reg["prompts"]}
G06 = next(e["value"] for e in rows["PR-35"]["audit_assertions"]["forbidden_regex"]
           if e.get("rule_id") == "TOP-001")
REGISTERED = G06
LB = "(?<!\\bno )(?<!\\bno `)"
if G06.startswith(LB):  # alternative (b), applied to the registry after Nathan's approval (g06_apply.py)
    G06 = G06[len(LB):]
assert G06.startswith("NEXT_PROMPT_HANDOFF(?:[^\\n]|\\n(?![ \\t]*\\n)){0,1500}?")
HEAD = "NEXT_PROMPT_HANDOFF(?:[^\\n]|\\n(?![ \\t]*\\n)){0,1500}?"
TAIL = G06[len(HEAD):]
ALT = {
    "a": G06,
    "b": "(?<!\\bno )(?<!\\bno `)" + G06,
    "c": "NEXT_PROMPT_HANDOFF(?:(?!unlinked filenames\\.)[^\\n]|\\n(?![ \\t]*\\n)(?![ \\t]*#)){0,1500}?" + TAIL,
    "d": G06.replace("|\\bworking branch\\b", "").replace("|\\bremote head\\b", ""),
}
assert ALT["d"] != G06 and "working branch" not in ALT["d"] and "remote head" not in ALT["d"]

RULE = ("Every nonterminal result ends with exactly one fenced `text` block beginning `NEXT_PROMPT_HANDOFF`.")
CANON = {k: v for k, v in T.items() if k not in ("STEP22", "STEP22-BEFORE", "STEP4")}
COMBINED = {
    "place+handoff+session+top": " ".join([T["C-PLACE"], T["C-HANDOFF"], T["C-SESSION"], T["C-TOP"]]),
    "rule+handoff+place+top": " ".join([RULE, T["C-HANDOFF"], T["C-PLACE"], T["C-TOP"]]),
    "place+session": " ".join([T["C-PLACE"], T["C-SESSION"]]),
    "dispatch+sub+top": " ".join([T["C-DISPATCH"], T["C-SUB"], T["C-TOP"]]),
    "rule+handoff+ask+top": " ".join([RULE, T["C-HANDOFF"], T["ASK-VARIANT"], T["C-TOP"]]),
    "replan+proceed+pr30+top": " ".join([T["C-REPLAN"], T["C-PROCEED"], T["C-PR30-ENTRY"], T["C-TOP"]]),
    "long": " ".join([RULE, T["C-HANDOFF"], T["C-SESSION"], T["C-DISPATCH"], T["C-SUB"], T["C-PLACE"], T["C-TOP"],
                      T["C-PROCEED"], T["C-REPLAN"], T["W4"]]),
}
SENT = " It carries the same session, worktree, branch, PR and head commit."


def reg_a(t):
    lines = t.split("\n")
    i = next(i for i, x in enumerate(lines) if T["C-HANDOFF"] in x)
    lines[i] = lines[i].replace(" " + T["C-HANDOFF"], SENT + " " + T["C-HANDOFF"], 1)
    return "\n".join(lines)


def reg_b(t):
    lines = t.split("\n")
    i = next(i for i, x in enumerate(lines) if T["C-HANDOFF"] in x)
    lines[i] = lines[i] + SENT
    return "\n".join(lines)


def F(row, text):
    return {(f["rule_id"], f["observed"]["summary"]) for f in A._evaluate_assertions(row, text, "g06-alt")}


def phrase(m):
    w = m.group(0).split()
    return " ".join(w[-12:])


out = {}
main54 = sorted(k for k in rows if k != "GCFPE-MGMT-10")
for key, val in ALT.items():
    rx = re.compile(val, re.MULTILINE)
    hits = [{"body": p, "phrase": phrase(m)} for p in main54 for m in [rx.search(edited[p])] if m]
    row = json.loads(json.dumps(rows["PR-35"]))
    row["audit_assertions"]["forbidden_regex"] = [
        dict(e, value=val) if e.get("value") == G06 else e for e in row["audit_assertions"]["forbidden_regex"]]
    want = [("TOP-001", "Forbidden pattern matched: " + val)]
    regs = {name: sorted(F(row, fn(edited["PR-35"])) - F(row, edited["PR-35"])) == want
            for name, fn in (("after_token", reg_a), ("end_of_c_handoff_paragraph", reg_b))}
    dirty = [k for k, v in {**CANON, **COMBINED}.items() if rx.search(v)]
    out[key] = {"value": val, "hits_on_54": hits, "hit_count": len(hits), "regressions_exact": regs,
                "canonical_and_combined_texts_matched": dirty,
                "canonical_texts_tested": len(CANON), "combined_paragraphs_tested": len(COMBINED)}
out["d_is_a_weakening"] = True
out["registered_value_equals_b"] = REGISTERED == ALT["b"]
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
print()
