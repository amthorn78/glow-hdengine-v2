"""Canonical texts for the v2 re-test, read from v1 §3 (the compiled final wording) with §12 applied.
Superseded §P texts and source-wrapped forms come from the earlier extractor (read-only import)."""
import re, sys
V1 = "/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/v2/v1.md"
lines = open(V1, encoding="utf-8").read().split("\n")
s = next(i for i, l in enumerate(lines) if l.startswith("## §3 "))
e = next(i for i, l in enumerate(lines) if l.startswith("## §4 "))
blocks, cur, name, inb = [], [], None, False
for l in lines[s:e]:
    if not inb:
        m = re.match(r"^\*\*([^*]+)\*\*", l)
        if m:
            name = m.group(1)
        if l == "```text":
            inb, cur = True, []
    else:
        if l == "```":
            blocks.append((name, "\n".join(cur))); inb = False
        else:
            cur.append(l)
T = {}
for n, b in blocks:
    k = n.strip()
    while k in T:
        k += "'"
    T[k] = b
J = {
 "C-NOTION": T["C-NOTION"], "C-ART": T["C-ART"], "C-HANDOFF": T["C-HANDOFF"], "C-PLACE": T["C-PLACE"],
 "C-DEC": T["C-DEC"], "C-LAT": T["C-LAT"], "C-VERSION": T["C-VERSION"], "C-D22": T["C-D22"],
 "C-SESSION": T["C-SESSION"], "C-SUB": T["C-SUB"], "C-DISPATCH": T["C-DISPATCH"], "C-TOP": T["C-TOP"],
 "GCFPE override": T["GCFPE override"], "C-PLACE ASK OK? variant": T["C-PLACE, `ASK OK?` variant"],
 "C-REPLAN": T["C-REPLAN"], "C-PROCEED": T["C-PROCEED"], "C-PR20-ENTRY": T["C-PR20-ENTRY"],
 "C-PR30-ENTRY": T["C-PR30-ENTRY"],
 "governance invariant": T["Governance-audit invariant"],
 "step2 relay": T["Step 2"], "step4 QA-10": T["Step 4"], "step22": T["Step 22"],
 # §12 W-1, W-2, W-4 and the §12 PR-20 input
 "W-1 PR-35 role": "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.",
 "W-2 RS-40 role": "You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.",
 "W-2 RS-40 creator": "the recorded phase's own dedicated session for the exact suspended work unit.",
 "W-4 PR-40 entry": "PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.",
 "W-4 PR-35 result input": "The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.",
 "PR-20 input": "PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the same WORK_UNIT_ID in a new dedicated session Nathan seeds",
 "W-8 pr30_to_pr35": "PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent.",
 "W-8 pr40_reject_replan": "A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new Proceed for the new plan (D23-F).",
 "W-9 GCF-14": "GCF-14 — Nathan creates one dedicated top-level PR session for one planned PR work unit.",
 "W-9 relay": "For a GCFPE main-ecosystem stage, return the paste-ready `NEXT_PROMPT_HANDOFF` and stop for Nathan; provisioning does not apply.",
 "S-6 relay": "A runtime handoff still names its destination by full name, version and direct Notion URL (C-HANDOFF); `NOTION_REFERENCE` stays versionless for reusable prompt text.",
 "S-7 relay": "`NOTION` means a maintenance surface that a destination rule names; live task, handoff and decision state lives in the repository.",
 "S-2 N2": "`required_regex` binds the Canon source and the `D23` canonical wordings; `forbidden_regex` guards `D7`, the `D23` reversals and session creation.",
 "scope line": "its subagents are maintenance workers, and never a way to run a main-ecosystem prompt.",
}
# texts that are skill or registry text, not body text (required guards need not be silent on them)
NON_BODY = {"GCFPE override", "governance invariant", "step2 relay", "W-1 PR-35 role", "W-2 RS-40 role",
            "W-2 RS-40 creator", "W-4 PR-35 result input", "PR-20 input", "W-8 pr30_to_pr35", "W-8 pr40_reject_replan",
            "W-9 GCF-14", "W-9 relay", "S-6 relay", "S-7 relay", "S-2 N2", "scope line", "C-D22", "C-VERSION"}
# source-wrapped forms (hard wraps kept) from the earlier extractor, where it has the same text
sys.path.insert(0, "/tmp/claude-0/spec/s7-registry")
import texts as old
PAIRS = {"C-NOTION": "P:C-NOTION", "C-ART": "P:C-ART", "C-HANDOFF": "P:C-HANDOFF", "C-PLACE": "P:C-PLACE",
         "C-DEC": "P:C-DEC", "C-LAT": "P:C-LAT", "C-VERSION": "P:C-VERSION", "C-SUB": "A1-5:C-SUB",
         "C-DISPATCH": "A1-5:C-DISPATCH", "C-TOP": "A1-8:C-TOP", "GCFPE override": "A1-6:override",
         "C-REPLAN": "child:C-REPLAN", "C-PROCEED": "child:C-PROCEED", "C-PR20-ENTRY": "child:C-PR20-ENTRY",
         "C-PR30-ENTRY": "child:C-PR30-ENTRY", "C-SESSION": "C-SESSION(amended,no backticks)"}
W = {k: old.W[v] for k, v in PAIRS.items() if old.J[v] == J[k]}
MISMATCH = [k for k, v in PAIRS.items() if old.J[v] != J[k]]
SUPERSEDED = {"§P C-SUB": old.J["P:C-SUB"], "§P C-DISPATCH": old.J["P:C-DISPATCH"],
              "C-SESSION §P backticks": old.J["C-SESSION(amended,§P backticks)"]}
if __name__ == "__main__":
    print(len(blocks), "text blocks;", len(J), "texts; wrapped forms:", len(W), "; mismatched with source extractor:", MISMATCH)
