#!/usr/bin/env python3
"""Apply Nathan's approved G06 heading stop to the working-tree registry ("approved", 2026-09-23, E6).

Why: Notion stores paragraphs as blocks, so a blank line between paragraphs reads back as one line break.
G06's window (TOP-001, forbidden_regex, NPH53) stopped only at a blank line, so on 10 landed or landable bodies
(CF-C-10..40, CF-E-10..40, CF-PO-10, MGR-10) it ran past the new handoff paragraph into the next section, where
"working branch" is legitimate. Change: the window also stops at a heading line:
  \n(?![ \t]*\n)   ->   \n(?![ \t]*\n|[ \t]*#)
The lookbehinds (option (b)), the 1 500-character bound and the term list are unchanged.

Method and checks: those of e3/g06_apply.py (line-anchored replacement of the exact two-line entry on the 53
NPH53 rows; load_data semantic diff; YAML round trip; structure check; D13 drift), which this script reuses.

usage: PYTHONDONTWRITEBYTECODE=1 python3 g06_heading_stop.py <skills-root> [--write]
"""
import json
import os
import subprocess
import sys

sys.dont_write_bytecode = True
import yaml  # noqa: E402

K = sys.argv[1]
WRITE = "--write" in sys.argv[2:]
REPO = "/home/user/glow-hdengine-v2"
REG = REPO + "/docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
PARTS = REPO + "/docs/graph/parts"
sys.path.insert(0, K + "/amthor-workspace-governance-audit/scripts")
import audit_workspace_governance as A  # noqa: E402

B = "(?<!\\bno )(?<!\\bno `)NEXT_PROMPT_HANDOFF"
T = ("{0,1500}?(?<!\\bno )(?:(?<![/\\w-])worktree\\b|\\bworking branch\\b"
     "|\\bbranch name\\b|\\bgit branch\\b|\\bhead (?:commit|SHA)\\b|\\bcommit (?:SHA|hash|identity|id)\\b|\\bremote head\\b)")
OLD = B + "(?:[^\\n]|\\n(?![ \\t]*\\n))" + T
NEW = B + "(?:[^\\n]|\\n(?![ \\t]*\\n|[ \\t]*#))" + T


def q(s):
    return "'" + s.replace("'", "''") + "'"


def rows_of(lines):
    starts = [i for i, x in enumerate(lines) if x.startswith("- prompt_key: ")]
    end = next(i for i, x in enumerate(lines) if x.startswith("global_literals:"))
    return {lines[s][len("- prompt_key: "):].strip(): (s, (starts + [end])[k + 1]) for k, s in enumerate(starts)}


def drift(reg):
    P = {f[:-5]: json.load(open(PARTS + "/prompts/" + f, encoding="utf-8")) for f in os.listdir(PARTS + "/prompts")}
    out = []
    for r in reg["prompts"]:
        part = P[r["prompt_key"]]
        want = sorted({e["to"] for e in part["edges"] if e["to_kind"] == "prompt" and e["to"] != part["id"]})
        cons = {c for o in r["outputs"] for c in (o.get("consumers") or [])}
        st = {s for o in r["outputs"] for s in (o.get("states") or [])}
        if r["required_interfaces"] != want or cons != set(want) or st != set(part["node"]["result_states"]):
            out.append(r["prompt_key"])
    return out


def main():
    src = open(REG, encoding="utf-8").read()
    lines = src.split("\n")
    old_line, new_line, rid_line = "    - value: " + q(OLD), "    - value: " + q(NEW), "      rule_id: TOP-001"
    edited_rows = []
    for key, (s, e) in rows_of(lines).items():
        hits = [i for i in range(s, e) if lines[i] == old_line and lines[i + 1] == rid_line]
        assert len(hits) <= 1, (key, len(hits))
        if hits:
            lines[hits[0]] = new_line
            edited_rows.append(key)
    assert len(edited_rows) == 53, len(edited_rows)
    new = "\n".join(lines)
    # YAML single-quote round trip of the new value
    assert yaml.safe_load("- value: " + q(NEW) + "\n  rule_id: TOP-001") == [{"value": NEW, "rule_id": "TOP-001"}]
    # semantic diff through load_data
    tmp = "/tmp/claude-0/e2/tmp/registry_g06_heading_check.md"
    open(tmp, "w", encoding="utf-8").write(new)
    a, b = A.load_data(REG), A.load_data(tmp)
    assert {k: v for k, v in a.items() if k != "prompts"} == {k: v for k, v in b.items() if k != "prompts"}
    assert [r["prompt_key"] for r in a["prompts"]] == [r["prompt_key"] for r in b["prompts"]]
    changed = []
    for ra, rb in zip(a["prompts"], b["prompts"]):
        fa = {k: v for k, v in ra.items() if k != "audit_assertions"}
        fb = {k: v for k, v in rb.items() if k != "audit_assertions"}
        assert fa == fb, ra["prompt_key"]
        for lst in set(ra["audit_assertions"]) | set(rb["audit_assertions"]):
            la, lb = ra["audit_assertions"].get(lst) or [], rb["audit_assertions"].get(lst) or []
            assert len(la) == len(lb), (ra["prompt_key"], lst)
            for x, y in zip(la, lb):
                if x != y:
                    assert x == {"value": OLD, "rule_id": "TOP-001"} and y == {"value": NEW, "rule_id": "TOP-001"}
                    changed.append(ra["prompt_key"])
    assert sorted(changed) == sorted(edited_rows) and len(set(changed)) == 53
    structure = subprocess.run([sys.executable, K + "/amthor-workspace-governance-audit/scripts/validate_project_prompt_registry.py", tmp],
                               capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    d = drift(b)
    os.unlink(tmp)
    print(json.dumps({"rows_edited": len(edited_rows), "semantic_diff": "only G06 value on 53 rows (heading stop)",
                      "yaml_round_trip": True, "structure": json.loads(structure.stdout), "structure_exit": structure.returncode,
                      "d13_drift": d, "assertions_before": sum(len(v) for r in a["prompts"] for v in r["audit_assertions"].values() if isinstance(v, list)),
                      "written": WRITE}, indent=1))
    assert structure.returncode == 0 and d == []
    if WRITE:
        open(REG, "w", encoding="utf-8").write(new)


if __name__ == "__main__":
    main()
