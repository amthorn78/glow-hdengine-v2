#!/usr/bin/env python3
"""E4 items 7, 8 and 9 (spec v2 §9; §7.1, §7.3, §7.7) on the E3 bodies, in memory.

usage: <{id: unedited body} JSON> | PYTHONDONTWRITEBYTECODE=1 python3 run_e4.py <edited-skills-root>

Reads the unedited bodies on stdin, derives the edited bodies with body_rules.apply, and prints a JSON
result on stdout that holds no body text, no fragment of one beyond a matched guard phrase of at most
12 words (clean-control hits only), and no body hash. Nothing is written to disk.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_rules as R  # noqa: E402

K = Path(sys.argv[1])
REPO = Path("/home/user/glow-hdengine-v2")
REG = REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
sys.path.insert(0, str(K / "amthor-workspace-governance-audit/scripts"))
import audit_workspace_governance as A  # noqa: E402

T = R.T
raw = json.load(sys.stdin)
edited, report = R.apply(raw, str(REG))
reg = A.load_data(REG)
rows = {r["prompt_key"]: r for r in reg["prompts"]}
MAIN54 = sorted(k for k in rows if k != "GCFPE-MGMT-10")
result = {}


def F(row, text):
    return {(f["rule_id"], f["observed"]["summary"]) for f in A._evaluate_assertions(row, text, "e4-in-memory")}


# ---- item 7: the edited validator, bodies piped ------------------------------------------------
contract = K / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
cmd = [sys.executable, str(K / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"), str(K / "change-flow"),
       "--contract", str(contract), "--bodies-stdin"]
p = subprocess.run(cmd, input=json.dumps(edited), capture_output=True, text=True,
                   env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/e2/tmp"})
v = json.loads(p.stdout)
result["item7"] = {
    "exit": p.returncode, "ok": v.get("ok"),
    "prompt_bodies_validated": len(v.get("prompt_bodies_validated") or []),
    "all_55_validated": sorted(v.get("prompt_bodies_validated") or []) == sorted(rows),
    "prompt_body_checks_not_evaluated": v.get("prompt_body_checks_not_evaluated"),
    "errors": v.get("errors"),
}

# ---- item 8: registry assertions, zero findings on every row ------------------------------------
per_row = {k: sorted(F(rows[k], edited[k])) for k in rows}
result["item8"] = {"rows": len(rows), "assertions": sum(len(v) for r in reg["prompts"]
                                                        for v in (r["audit_assertions"] or {}).values() if isinstance(v, list)),
                   "rows_with_findings": {k: v for k, v in per_row.items() if v}}
# §7.7 role parity, with its two must-fail regressions
g35 = json.loads((REPO / "docs/graph/parts/prompts/PR-35.json").read_text(encoding="utf-8"))["node"]["receiving_role"]
g40 = json.loads((REPO / "docs/graph/parts/prompts/RS-40.json").read_text(encoding="utf-8"))["node"]["receiving_role"]
W1 = "never as a subagent, forked agent or workflow agent of PR-30"


def parity(r35, gr35, r40, gr40):
    out = []
    if r35 != gr35:
        out.append("ROLE_PARITY")
    if W1 not in gr35:
        out.append("ROLE_CLAUSE")
    if r40 != gr40:
        out.append("ROLE_PARITY")
    return out


strip = lambda s: s.replace(", and " + W1 + " or of any other session", "")  # noqa: E731
result["item8"]["role_parity"] = {
    "clean": parity(rows["PR-35"]["session_role"], g35, rows["RS-40"]["session_role"], g40),
    "clause_removed_registry_only": parity(strip(rows["PR-35"]["session_role"]), g35, rows["RS-40"]["session_role"], g40),
    "clause_removed_both": parity(strip(rows["PR-35"]["session_role"]), strip(g35), rows["RS-40"]["session_role"], g40),
    "clause_strip_effective": strip(g35) != g35,
}

# ---- item 9: guard regressions -----------------------------------------------------------------
# Each guard is identified by its list, rule_id and a distinguishing fragment of its value; the value
# itself is read from the working-tree registry, so the test runs what the registry holds.
GUARDS = {
    "G01": ("forbidden_regex", "CTR-001", "CONTROL_NOTION"),
    "G02": ("forbidden_regex", "CTR-001", "operational state[^"),
    "G03": ("forbidden_regex", "CTR-001", "Notion and repository persistence"),
    "G04": ("forbidden_regex", "CTR-001", "Notion-resident artifact"),
    "G05": ("required_regex", "CTR-002", "never\\s+carries"),
    "G06": ("forbidden_regex", "TOP-001", "NEXT_PROMPT_HANDOFF(?:[^\\n]|"),
    "G07": ("required_regex", "TOP-001", "The final response ends with"),
    "G08": ("forbidden_regex", "CTR-002", "\\bends? `ASK OK"),
    "G08A": ("required_regex", "TOP-001", "is the line immediately before the block"),
    "G09": ("required_regex", "CTR-002", "In-flight decisions"),
    "G10": ("required_regex", "CTR-002", "Decide it during work"),
    "G11": ("required_regex", "CTR-002", "Material\\*{0,2} means"),
    "G12": ("forbidden_regex", "SRC-001", "Prompt [Vv]ersion(?:"),
    "G13": ("forbidden_regex", "INV-003", "Ecosystem release(?:"),
    "G14": ("forbidden_regex", "SRC-001", "(?:\\*\\*|__)?Set(?:"),
    "G15": ("forbidden_regex", "CTR-001", "dedicated PR-development session"),
    "G16": ("required_regex", "CTR-002", "they do not share a session"),
    "G17": ("required_regex", "CTR-002", "workflow\\s+agent\\s+of\\s+PR-30"),
    "G18": ("required_regex", "CTR-002", "of\\s+another\\s+session"),
    "G19": ("forbidden_regex", "CTR-001", "(?:run|execute|invoke|dispatch"),
    "G20": ("forbidden_regex", "CTR-001", "(?<!Nathan )"),
    "G21": ("forbidden_regex", "CTR-001", "create_session|create_trigger"),
    "G22": ("forbidden_regex", "CTR-001", "launched as a new session"),
    "G23": ("required_regex", "CTR-002", "ubscribe to the pull request"),
    "G24": ("required_regex", "CTR-002", "stay subscribed and do not poll"),
    "G25": ("required_regex", "CTR-002", "The observed merge event is the fact"),
    "G25B": ("required_regex", "CTR-002", "PR-40 is entered on the observed merge event"),
    "G26": ("forbidden_regex", "CTR-001", "suitable actual authorized implementation vehicle"),
    "G27": ("required_regex", "CTR-002", "PR_WORK_UNIT_LINEAGE_REVIEW`?\\s+whose"),
}
EXPECTED_ROWS = {"G01": 55, "G02": 55, "G03": 1, "G04": 10, "G05": 53, "G06": 53, "G07": 53, "G08": 4, "G08A": 4,
                 "G09": 3, "G10": 10, "G11": 10, "G12": 55, "G13": 55, "G14": 55, "G15": 54, "G16": 3, "G17": 3,
                 "G18": 54, "G19": 54, "G20": 54, "G21": 54, "G22": 2, "G23": 2, "G24": 2, "G25": 2, "G25B": 1,
                 "G26": 1, "G27": 1}
gval, grows = {}, {}
for gid, (lst, rid, frag) in GUARDS.items():
    vals = {}
    for k, r in rows.items():
        for e in (r["audit_assertions"].get(lst) or []):
            if isinstance(e, dict) and e.get("rule_id") == rid and frag in e["value"]:
                vals.setdefault(e["value"], []).append(k)
    assert len(vals) == 1, (gid, len(vals))
    (gval[gid], grows[gid]), = vals.items()
result["guard_rows"] = {g: len(v) for g, v in grows.items()}
result["guard_rows_as_expected"] = all(len(grows[g]) == n for g, n in EXPECTED_ROWS.items())


def summary(gid):
    lst = GUARDS[gid][0]
    return (GUARDS[gid][1], ("Required pattern absent: " if lst == "required_regex" else "Forbidden pattern matched: ") + gval[gid])


def append(t, s):
    return t + "\n" + s


def delete(t, s):
    assert t.count(s) == 1, ("anchor count", t.count(s), s[:40])
    return t.replace(s, "", 1)


def after_prompt_id(line):
    def m(t):
        lines = t.split("\n")
        i = next(i for i, x in enumerate(lines) if x.startswith("Prompt ID:"))
        return "\n".join(lines[:i + 1] + [line] + lines[i + 1:])
    return m


def g06_after_token(t):
    lines = t.split("\n")
    i = next(i for i, x in enumerate(lines) if T["C-HANDOFF"] in x)
    lines[i] = lines[i].replace(" " + T["C-HANDOFF"], " It carries the same session, worktree, branch, PR and head commit. " + T["C-HANDOFF"], 1)
    return "\n".join(lines)


def g06_end_of_paragraph(t):
    lines = t.split("\n")
    i = next(i for i, x in enumerate(lines) if T["C-HANDOFF"] in x)
    lines[i] = lines[i] + " It carries the same session, worktree, branch, PR and head commit."
    return "\n".join(lines)


def g04_insert(t):
    return t.replace(T["C-HANDOFF"], T["C-HANDOFF"] + " Name each input artifact by repository path, or its direct Notion URL for a Notion-resident artifact.", 1)


LAT_P1 = T["C-LAT"].split("\n\n")[0]
A18 = " " + T["C-SESSION"].split(". ")[-1]  # A1-8's sentence, the last one of C-SESSION
OLD_LIST = ("The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; "
            "dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; "
            "primary skill authority; continuous recovery/artifact lineage.")
CASES = [
    ("G01", "PR-10", lambda t: append(t, "Concise authorized operational state and pointers remain `CONTROL_NOTION`.")),
    ("G02", "PR-10", lambda t: append(t, "Operational state and pointers stay in Notion.")),
    ("G03", "QA-10", lambda t: append(t, "Use Notion and repository persistence for results.")),
    ("G04", "CF-C-10", g04_insert),
    ("G05", "PR-35", lambda t: delete(t, T["C-ART"])),
    ("G06", "PR-35", g06_after_token),
    ("G06", "PR-35", g06_end_of_paragraph),
    ("G07", "PR-35", lambda t: delete(t, "The final response ends with the `NEXT_PROMPT_HANDOFF` block.")),
    ("G07", "QA-60", lambda t: delete(t, "The final response ends with the `NEXT_PROMPT_HANDOFF` block.")),
    ("G08", "QA-60", lambda t: append(t, "The final response must end `ASK OK?`.")),
    ("G08A", "QA-60", lambda t: delete(t, "`ASK OK?` is the line immediately before the block.")),
    ("G08A", "RS-30", lambda t: delete(t, "`ASK OK?` is the line immediately before the block.")),
    ("G09", "PR-35", lambda t: delete(t, T["C-DEC"])),
    ("G09", "RS-40", lambda t: delete(t, T["C-DEC"])),
    ("G10", "PR-35", lambda t: delete(t, "**Decide it during work:**")),
    ("G11", "PR-35", lambda t: delete(t, LAT_P1)),
    ("G12", "PR-35", after_prompt_id("Prompt Version: 091426.1")),
    ("G12", "PR-35", after_prompt_id("**Prompt Version**: 091426.1")),
    ("G13", "PR-35", after_prompt_id("Ecosystem release: GCFPE-20260914.1")),
    ("G13", "PR-35", after_prompt_id("| Ecosystem release: | GCFPE-20260914.1 |")),
    ("G14", "PR-35", after_prompt_id("Set: GCFPE-20260914.1 / 091426.1")),
    ("G14", "PR-35", after_prompt_id("- `Set:` GCFPE-20260914.1 / 091426.1")),
    ("G15", "PR-35", lambda t: append(t, OLD_LIST)),
    ("G15", "QA-10", lambda t: append(t, "It shares the original Proceed, dedicated PR-development session and branch.")),
    ("G16", "PR-35", lambda t: delete(t, "; they do not share a session")),
    ("G16", "RS-40", lambda t: delete(t, "; they do not share a session")),
    ("G17", "PR-35", lambda t: delete(t, A18)),
    ("G17", "PR-30", lambda t: delete(t, A18)),
    ("G18", "PR-35", lambda t: delete(t, T["C-TOP"])),
    ("G18", "PR-50", lambda t: delete(t, T["C-TOP"])),
    ("G19", "PR-35", lambda t: append(t, "Run PR-35 as a subagent.")),
    ("G20", "PR-35", lambda t: append(t, "Launch a new session for PR-40.")),
    ("G21", "PR-35", lambda t: append(t, "Use mcp__Claude_Code_Remote__create_session to open it.")),
    ("G22", "PR-35", lambda t: append(t, "Emit the PR-40 handoff: paste-ready, or launched as a new session where the surface provides one.")),
    ("G23", "PR-35", lambda t: delete(t, T["C-SUB"])),
    ("G23", "RS-40", lambda t: delete(t, T["C-SUB"])),
    ("G24", "PR-35", lambda t: delete(t, "; stay subscribed and do not poll")),
    ("G24", "RS-40", lambda t: delete(t, "; stay subscribed and do not poll")),
    ("G25", "PR-35", lambda t: delete(t, " The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently.")),
    ("G25", "RS-40", lambda t: delete(t, " The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently.")),
    ("G25B", "PR-40", lambda t: delete(t, T["W4"])),
    ("G26", "PR-40", lambda t: append(t, "Return to the existing PR owner, which holds the original Proceed and a suitable actual authorized implementation vehicle.")),
    ("G27", "PR-20", lambda t: delete(t, T["C-PR20-ENTRY"])),
]
reg_out = []
for gid, pid, mut in CASES:
    row, clean = rows[pid], edited[pid]
    try:
        got = sorted(F(row, mut(clean)) - F(row, clean))
    except AssertionError as e:
        got = [("MUTATION_ANCHOR", str(e.args[0][:2]))]
    reg_out.append({"guard": gid, "row": pid, "exact": got == [summary(gid)], "delta_count": len(got),
                    "delta_rule_ids": [g[0] for g in got]})
result["item9_regressions"] = {"cases": len(reg_out), "exact": sum(c["exact"] for c in reg_out),
                               "failures": [c for c in reg_out if not c["exact"]], "all": reg_out}
# G27 clean control on today's PR-20, before any edit: it must produce its finding
result["item9_G27_clean_control_unedited_PR20"] = summary("G27") in F(rows["PR-20"], raw["PR-20"])


# ---- clean control: every guard over the 54 edited main bodies ---------------------------------
def phrase(m):
    words = m.group(0).split()
    return " ".join(words[-12:]) if len(words) > 12 else m.group(0)


control = {}
for gid, (lst, rid, frag) in GUARDS.items():
    rx = re.compile(gval[gid], re.MULTILINE)
    hits_on, hits_off, absent_on = [], [], []
    for pid in MAIN54:
        m = rx.search(edited[pid])
        on_row = pid in grows[gid]
        if lst == "forbidden_regex" and m:
            (hits_on if on_row else hits_off).append({"body": pid, "phrase": phrase(m)})
        if lst == "required_regex" and on_row and not m:
            absent_on.append(pid)
    control[gid] = {"list": lst, "rows": len(grows[gid]),
                    "forbidden_hits_on_its_rows": hits_on, "forbidden_hits_on_other_bodies": hits_off,
                    "required_absent_on_its_rows": absent_on}
result["clean_control_54"] = control
result["edit_report"] = report
json.dump(result, sys.stdout, indent=1, ensure_ascii=False)
print()
