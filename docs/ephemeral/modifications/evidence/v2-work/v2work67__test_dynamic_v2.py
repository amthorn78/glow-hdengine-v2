import copy, re, sys
sys.path.insert(0, "/tmp/claude-0/v2work67/wga/scripts"); sys.path.insert(0, "/tmp/claude-0/v2work67")
from audit_workspace_governance import load_data, _evaluate_assertions
import texts_v2 as T
from guards_v2 import GUARDS, LAT10, ASK4, G25_PR40_CANDIDATE
J = T.J
reg = load_data("/tmp/claude-0/v2work67/registry.new.md")
ROWS = {r["prompt_key"]: r for r in reg["prompts"]}
NPH = [k for k, r in ROWS.items() if any((x.get("value") if isinstance(x, dict) else x) == "NEXT_PROMPT_HANDOFF" for x in r["audit_assertions"].get("required_literals") or [])]
C_NOTION = ["PR-10", "PR-20", "PR-30", "PR-40", "OPS-10", "OPS-20", "OPS-30"]
HR = "Emit exactly one `NEXT_PROMPT_HANDOFF` block."
def body(k, layout):
    r = ROWS[k]
    p = [f"# {r['expected_title']}", f"Prompt ID: {k}\nNotion URL: {r['notion_url']}", "Read PF10 as controlled Markdown under docs/pfcanon/."]
    if k in C_NOTION: p.append(J["C-NOTION"])
    if k == "QA-10": p.append("Record results in " + J["step4 QA-10"] + ".")
    if k in ("PR-30", "PR-35", "RS-40"): p.append(J["C-SESSION"])
    if k in LAT10: p.append(J["C-LAT"])
    if k in ("PR-35", "RS-40"): p += [J["C-SUB"], J["C-DISPATCH"]]
    if k == "PR-40": p += [J["C-REPLAN"], J["W-4 PR-40 entry"]]
    if k == "PR-20": p.append(J["C-PR20-ENTRY"])
    if k == "PR-30": p += [J["C-PR30-ENTRY"], J["C-PROCEED"]]
    if k in ("PR-30", "PR-35", "RS-40"): p.append("## PR_IMPLEMENTATION_RESULT\n\n" + J["C-DEC"])
    if k in NPH:
        p.append("## Output\n\n" + J["C-ART"])
        place = J["C-PLACE ASK OK? variant"] if k in ASK4 else J["C-PLACE"]
        if layout == "A": p += [HR + " " + J["C-HANDOFF"], place + " " + J["C-TOP"]]
        else: p.append(" ".join([HR, J["C-HANDOFF"], place, J["C-TOP"]]))
    elif k != "GCFPE-MGMT-10":
        p.append("Return control to Nathan. " + J["C-TOP"])
    return "\n\n".join(p) + "\n"
def F(row, t): return {(f["rule_id"], f["observed"]["summary"]) for f in _evaluate_assertions(row, t, "x")}
NEW = {(v, rid) for _, _, v, rid, _, _ in GUARDS}
clean_bad = 0
for layout in "AB":
    for k in ROWS:
        fs = [f for f in _evaluate_assertions(ROWS[k], body(k, layout), "x") if (f["observed"]["summary"].split(": ", 1)[1], f["rule_id"]) in NEW]
        if fs: clean_bad += 1; print("CLEAN-FAIL", layout, k, [f["observed"]["summary"][:80] for f in fs])
print("new-guard findings on clean bodies, 55 rows x 2 layouts:", clean_bad)
def cut(t, s): assert s in t, s[:70]; return t.replace(s, "", 1)
def after(t, a, i): assert a in t, a[:70]; return t.replace(a, a + i, 1)
PID = lambda k: f"Prompt ID: {k}"
C_PLACE_1 = "The final response ends with the `NEXT_PROMPT_HANDOFF` block."
CASES = [
 ("G01", "PR-10", lambda t: t + "\nConcise authorized operational state and pointers remain `CONTROL_NOTION`.\n"),
 ("G02", "PR-10", lambda t: t + "\nOperational state and pointers stay in Notion.\n"),
 ("G03", "QA-10", lambda t: t + "\nUse Notion and repository persistence for results.\n"),
 ("G04", "CF-C-10", lambda t: after(t, HR, " Name each input artifact by repository path, or its direct Notion URL for a Notion-resident artifact.")),
 ("G05", "PR-35", lambda t: cut(t, J["C-ART"])),
 ("G06", "PR-35", lambda t: after(t, HR, " It carries the same session, worktree, branch, PR and head commit.")),
 ("G06", "PR-35", lambda t: after(t, J["C-HANDOFF"], " It carries the same session, worktree, branch, PR and head commit.")),
 ("G07", "PR-35", lambda t: cut(t, C_PLACE_1)),
 ("G07", "QA-60", lambda t: cut(t, C_PLACE_1)),
 ("G08", "QA-60", lambda t: t + "\nThe final response must end `ASK OK?`.\n"),
 ("G08A", "QA-60", lambda t: cut(t, " `ASK OK?` is the line immediately before the block.")),
 ("G08A", "RS-30", lambda t: cut(t, " `ASK OK?` is the line immediately before the block.")),
 ("G09", "PR-35", lambda t: cut(t, J["C-DEC"])),
 ("G09", "RS-40", lambda t: cut(t, J["C-DEC"])),
 ("G10", "PR-35", lambda t: cut(t, "**Decide it during work:**")),
 ("G11", "PR-35", lambda t: cut(t, J["C-LAT"].split("\n\n")[0])),
 ("G12", "PR-35", lambda t: after(t, PID("PR-35"), "\nPrompt Version: 091426.1")),
 ("G12", "PR-35", lambda t: after(t, PID("PR-35"), "\n**Prompt Version**: 091426.1")),
 ("G13", "PR-35", lambda t: after(t, PID("PR-35"), "\nEcosystem release: GCFPE-20260914.1")),
 ("G13", "PR-35", lambda t: after(t, PID("PR-35"), "\n| Ecosystem release: | GCFPE-20260914.1 |")),
 ("G14", "PR-35", lambda t: after(t, PID("PR-35"), "\nSet: GCFPE-20260914.1 / 091426.1")),
 ("G14", "PR-35", lambda t: after(t, PID("PR-35"), "\n- `Set:` GCFPE-20260914.1 / 091426.1")),
 ("G15", "PR-35", lambda t: t + "\nThe exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage.\n"),
 ("G15", "QA-10", lambda t: t + "\nIt shares the original Proceed, dedicated PR-development session and branch.\n"),
 ("G16", "PR-35", lambda t: cut(t, "; they do not share a session")),
 ("G16", "RS-40", lambda t: cut(t, "; they do not share a session")),
 ("G17", "PR-35", lambda t: cut(t, " PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.")),
 ("G17", "PR-30", lambda t: cut(t, " PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.")),
 ("G18", "PR-35", lambda t: cut(t, " " + J["C-TOP"])),
 ("G18", "PR-50", lambda t: cut(t, " " + J["C-TOP"])),
 ("G19", "PR-35", lambda t: t + "\nRun PR-35 as a subagent.\n"),
 ("G20", "PR-35", lambda t: t + "\nLaunch a new session for PR-40.\n"),
 ("G21", "PR-35", lambda t: t + "\nUse mcp__Claude_Code_Remote__create_session to open it.\n"),
 ("G22", "PR-35", lambda t: t + "\nEmit the PR-40 handoff: paste-ready, or launched as a new session where the surface provides one.\n"),
 ("G23", "PR-35", lambda t: cut(t, J["C-SUB"])),
 ("G24", "PR-35", lambda t: cut(t, "; stay subscribed and do not poll")),
 ("G24", "RS-40", lambda t: cut(t, "; stay subscribed and do not poll")),
 ("G25", "PR-35", lambda t: cut(t, " The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently.")),
 ("G25", "RS-40", lambda t: cut(t, " The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently.")),
 ("G26", "PR-40", lambda t: t + "\nReturn to the existing PR owner, which holds the original Proceed and a suitable actual authorized implementation vehicle.\n"),
 ("G27", "PR-20", lambda t: cut(t, J["C-PR20-ENTRY"])),
]
G = {g[0]: g for g in GUARDS}
fails = 0
for layout in "AB":
    for gid, k, mut in CASES:
        _, kind, value, rid, _, _ = G[gid]
        want = {(rid, ("Required pattern absent: " if kind == "required_regex" else "Forbidden pattern matched: ") + value)}
        c = body(k, layout); got = F(ROWS[k], mut(c)) - F(ROWS[k], c)
        ok = got == want; fails += not ok
        if not ok: print("FAIL", layout, gid, k, [(a, b[:80]) for a, b in got])
print("regression cases:", len(CASES), "x 2 layouts; REGRESSION FAILURES:", fails)
# worker phrasings appended to a clean MAIN54 body produce no new finding
for p in ["use subagents as workers within this task", "spawn worker subagents for parallel reads within this session", "Run PR-35's tests in a subagent.", "Nathan creates a new session for PR-40 and pastes the handoff."]:
    c = body("PR-35", "A"); print("worker phrasing on PR-35:", repr(p), "new findings:", sorted(F(ROWS["PR-35"], c + "\n" + p + "\n") - F(ROWS["PR-35"], c)))
# §12's G25 anchor on PR-40, and the candidate
pr40 = copy.deepcopy(ROWS["PR-40"]); g25 = G["G25"]
pr40["audit_assertions"]["required_regex"].append({"value": g25[2], "rule_id": g25[3]})
print("§12 G25 anchor on clean PR-40 body:", sorted(x[1][:80] for x in F(pr40, body("PR-40", "A")) if g25[2] in x[1]))
pr40 = copy.deepcopy(ROWS["PR-40"]); c = G25_PR40_CANDIDATE
pr40["audit_assertions"]["required_regex"].append({"value": c[2], "rule_id": c[3]})
b = body("PR-40", "A")
print("candidate on clean PR-40:", sorted(x for x in F(pr40, b) if c[2] in x[1]),
      "; after deleting the W-4 sentence:", sorted(F(pr40, cut(b, J["W-4 PR-40 entry"])) - F(pr40, b)))
# G06 distance probe
c = body("PR-35", "A"); m = after(c, J["C-HANDOFF"], " It carries the same session, worktree, branch, PR and head commit.")
i = m.find("worktree, branch, PR"); j = m.rfind("NEXT_PROMPT_HANDOFF", 0, i)
print("G06 end-of-paragraph distance:", i - j - len("NEXT_PROMPT_HANDOFF"))
