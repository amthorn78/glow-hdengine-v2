#!/usr/bin/env python3
"""MODIFICATION-20260923-closeout-residuals: the body rules, as one mechanical engine.

`apply(pid, text)` returns the edited body and a report. Order inside a body (P-10): the shared RULES in table
order, then the body's LOCAL edits in their listed order. Every rule and edit asserts its expected count; a
mismatch is reported, never forced. CHECKS are the LOCAL-only rules' anchors (R-26-FRAME, R-26-BRANCH-SEND,
R-26-BRANCH-RECV, R-A7-LOCAL, R-ITEM40): each must read 0 on its rows after all edits.

No prompt body is held here. Anchors are clauses of at most 15 words; new texts are canonical texts (read from
their repository homes by canon.py) or texts this Modification authors.
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon as C  # noqa: E402

LOCAL = json.loads((HERE / "locals.json").read_text(encoding="utf-8"))

# ---- texts this Modification authors (each written once, here) -------------------------------------------
OWN = ("Every statement in this prompt that it is read-only or does not change the repository excludes its own "
       "output artifacts, which it writes, commits and pushes, and any pull request that carries them.")        # P-02
RECV = ("The branch, head and commits are verified at entry from the recorded vehicle and repository state; the "
        "handoff does not carry them.")                                                                     # P-01
A5_NEW = "This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`"
A5_MGMT = (A5_NEW + ", the controls it maintains only under `docs/prompt_ecosystem_management/`")          # P-04
A10_NEW = "Reviewers remain read-only toward the work they review"
P1_NEW = "Then give the other fields the handoff rule above names; " + C.STEP16 + "."
P4_NEW = ("Catalogs carry the verified direct Notion links, repository paths and exact selected prompt versions "
          "required by this release; a runtime handoff names its destination and input artifacts by those links, "
          "versions and paths, and the artifacts hold their lineage.")
TASK_NEW = ("Populate the exact immediate destination or actual owner, the receiving role and session, and each input "
            "artifact by repository path; the artifacts hold the rest.")
CLOSE_NEW = ("Name the positive closure decision and every post-closure result artifact by repository path; those "
             "artifacts hold the unresolved observations and manual-action dispositions.")
A2E_NEW = ("Keep exact register lineage, publication evidence and unresolved facts in the output artifact, which each "
           "next or recovery handoff names")
ITEM21_NEW = ("PR-40's entry, on `MERGE_OBSERVED` or, " + C.PRED + ", on Nathan's merge assertion, is defined in "
              "*Product Owner merge action, PR phase ownership, and abort boundary*; that entry creates no runtime "
              "approval")
ITEM31_NEW = ("A precise in-scope defect in landed work returns `REJECT` and re-plans through `PR-20`, as "
              + C.REPLAN_HEAD[:-3] + "** states.")
ITEM18_NEW = ("The Candidate CRD Items List is the Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`), "
              "which a destination rule names; it is the list's only store, and this prompt writes to it only as this "
              "section directs. ")
ITEM19_NEW = (" Name the board by the board reference the change context supplies; when none is supplied, record the "
              "board update as pending, owned under PF04 §9.1.1 by the authorized manual operator and the actual "
              "receiving owners.")
ITEM34_NEW = (" This applies only before the whole approved run is complete: a completed failing run is `ACCEPT` and "
              "continues to QA-120.")
ITEM35_NEW = ", routed as *Required result and routing* states"                                             # P-14
ITEM30D1_NEW = " and " + C.PRED + "; for `MERGE_OBSERVED`, it is the same selected PR-40"
ITEM30D2_NEW = ("The conditional `PR-40` block states only its manual prerequisite: it is usable only after Nathan "
                "manually merges the identified PR and " + C.PRED + "; `PR-40`'s own body holds the verification rules.")
RELEASE = r"(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?(?:Prompt [Vv]ersion|Ecosystem release|Set)(?:\*\*|__|`){0,2}[ \t]*:"  # P-16

AUTHORED = {"OWN": OWN, "RECV": RECV, "A5_NEW": A5_NEW, "A5_MGMT": A5_MGMT, "A10_NEW": A10_NEW, "P1_NEW": P1_NEW,
            "P4_NEW": P4_NEW, "TASK_NEW": TASK_NEW, "CLOSE_NEW": CLOSE_NEW, "A2E_NEW": A2E_NEW,
            "ITEM21_NEW": ITEM21_NEW, "ITEM31_NEW": ITEM31_NEW, "ITEM18_NEW": ITEM18_NEW, "ITEM19_NEW": ITEM19_NEW,
            "ITEM34_NEW": ITEM34_NEW, "ITEM35_NEW": ITEM35_NEW, "ITEM30D1_NEW": ITEM30D1_NEW,
            "ITEM30D2_NEW": ITEM30D2_NEW}


def each(pids, n=1):
    return {p: n for p in pids}


# R-OWN: each body's own placement anchor (P-02; G-K35 per row)
OWN_AT = {
    "PR-40": r"(?<=operating read-only\.)",
    "CL-E-20": r"(?<=revalidation session, read-only\.)",
    "DOC-20": r"(?<=do not edit documentation, Canon, PF10, or repository state\.)",
    "QA-10": r"(?<=This is a read-only audit and readiness role\.)",
    "PR-50": r"otherwise mutating the workspace, worktree, branch, open PR, commits or evidence[^.\n]*\.",  # dry A
    "ESC-25": r"read-only repository reviewer[^.\n]*\.",
    "PR-20": r"(?<=Do not mutate the repository in this authoring operation\.)",  # dry E1: Execute step 2
    "GCFPE-MGMT-10": r"does not execute product Change Flow, implementation, repository work[^.\n]*\.",
    "CL-20": r"Use only the read-only tools, stores, repository access[^.\n]*\.",
    "CL-30": r"Use only the read-only tools, stores, repository access[^.\n]*\.",
    "CL-40": r"It does not edit Canonical PF09, PF10, Canon, a board, registry, repository[^.\n]*\.",
}

A2G = (r"; `?CANON_CONFLICT_REGISTER`?(?=;)|`?CANON_CONFLICT_REGISTER`? and approved/rejected (?:history|dispositions); "
       r"|, `?CANON_CONFLICT_REGISTER`?(?= and )|; (?:and )?`?CANON_CONFLICT_REGISTER`?(?=\.)|(?<=, )conflict register, ")

# (id, anchor or {pid: anchor}, action, new text or {pid: text}, {pid: expected})
RULES = [
    ("R-A1a", r"\bin permitted metadata or (?:the )?handoff\b", "replace", "in the output artifact's permitted metadata",
     each(["CL-20", "CL-30", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40",
           "OPS-10", "OPS-20", "PR-30", "PR-40", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50", "QA-60", "QA-70",
           "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"])),                                                  # P-05
    ("R-A1b", r"\bin (?:the )?existing permitted metadata or (?:the )?handoff\b", "replace",
     "in the output artifact's existing permitted metadata", each(["CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "QA-10"])),
    ("R-A1c", r"(?:(?<=lineage metadata)|(?<=artifact lineage)) or (?:the )?(?:returned )?handoff(?=[:.,;])", "delete", "",
     each(["CL-C-10", "CL-E-10", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30",
           "ESC-40", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10", "QA-100", "QA-110",
           "QA-120", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"])),
    ("R-A1d", r"(?<=exist, )in (?:the )?returned handoff\b", "replace", "in the output artifact's lineage metadata",
     each(["CL-C-10", "CL-E-10", "OPS-10", "OPS-30", "PR-10", "PR-20", "QA-10"])),
    ("R-A1e", r"(?<=artifact metadata) or handoff(?=\.)", "delete", "",
     each(["CL-20", "CL-30", "CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A1f", r"permitted artifact/handoff metadata", "replace", "permitted artifact metadata", each(["PR-35"])),
    ("R-A2a", r"(?<=in the existing substantive artifact) and handoff\b", "replace", ", which the handoff names",
     each(["DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50",
           "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"])),
    ("R-A2b", r"(?<=substantive artifact metadata/content) and handoffs\b", "replace", ", which the handoff names",
     each(["CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A2c", r"task, receipt, review and handoff metadata", "replace",
     "task, receipt and review metadata, which the handoff names", each(["OPS-10"])),
    ("R-A2d", r"task, execution result, receipt and handoff when applicable", "replace",
     "task, execution result and receipt, which the handoff names, when applicable", each(["OPS-20"])),
    ("R-A2e", r"Carry exact register lineage, publication evidence and unresolved facts through "
              r"(?:all next/recovery packages|every next and recovery package)", "replace", A2E_NEW,
     each(["CL-C-10", "CL-E-10", "OPS-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A2f1", r"review result and every native return without deciding Canon", "replace",
     "review result without deciding Canon; every native return names those artifacts", each(["PR-40"])),
    ("R-A2f2", r", `QA_READINESS` and every return package", "replace",
     " and `QA_READINESS`; every return package names those artifacts", each(["QA-10"])),
    ("R-A2g", {"*": A2G, "IA-30": r"(?<=dependency state, )conflict register, "}, "delete", "",               # P-07
     {"IA-10": 1, "IA-20": 1, "IA-30": 1, "OPS-10": 4, "OPS-20": 4, "OPS-30": 5, "PR-10": 4, "PR-20": 4, "PR-40": 6,
      "QA-10": 6}),
    ("R-26-P1", r"Then identify the required receiving role/session[^\n]*?expected output/state\.(?: Carry complete native "
                r"inputs[^\n]*?filename\.)?", "replace", P1_NEW,
     each(["OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-26-P1b", r",? naming [^.\n]*\bunresolved items/owners, next action, and expected (?:output|review state)(?=\.)",
     "delete", "", each(["IA-30", "UTIL-10"])),
    ("R-26-P3", r"(?<=PF10/addendum lineage )into its result and handoff\b", "replace",
     "into its result artifact, which the handoff names", each(["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"])),
    ("R-26-P4", r"Catalogs and runtime handoffs carry the verified direct Notion links[^.\n]*\.", "replace", P4_NEW,
     {**each(["CL-C-10", "CL-E-10", "PR-40", "QA-10", "PR-10", "PR-20", "PR-30", "OPS-30"]), "OPS-10": 0, "OPS-20": 0}),  # P-13
    ("R-26-TASK", r"Populate the exact immediate destination or actual owner, actor/session continuity, native "
                  r"inputs,[^.\n]*required action\.", "replace", TASK_NEW, each(["OPS-30", "QA-10"])),
    ("R-26-CLOSE", r"Carry the positive closure decision, complete post-closure results, unresolved observations[^.\n]*\.",
     "replace", CLOSE_NEW, each(["CL-20", "CL-30"])),
    ("R-A7-S1a", r"(?<=usable only after Nathan later manually merges the identified PR)(?=\.)", "replace",
     " and " + C.PRED, each(["OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A7-S1b", r"; Nathan's later invocation asserts a merge occurred; (?=PR-40 independently verifies)", "replace",
     ". " + C.W4 + " " + C.ONCE + " ", each(["OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A7-S2", r"Nathan's (?:later PR-40 invocation asserts that a manual merge occurred; |PR-40 invocation asserts the "
                r"manual-merge event, while )(?=PR-40 independently verifies)", "replace", C.W4 + " ",
     each(["OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A7-CL", r"Nathan's later manual PR-40 invocation asserts only that he manually merged the identified PR; ",
     "replace", C.W4 + " " + C.ONCE + " ", each(["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"])),
    ("R-A7-S3", r"PR-40 independently verifies the later asserted merge and landed lineage\.", "replace",
     C.W4 + " " + C.ONCE + " PR-40 independently verifies the merged state and landed lineage.",
     each(["CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40", "QA-20"])),
    ("R-ITEM21", r"(?:The (?:specific )?)?Product Owner PR-40 merge-approval effect is defined above", "replace",
     ITEM21_NEW, each(["CL-20", "CL-30", "CL-C-10", "CL-E-10"])),
    ("R-ITEM30a", r"(?m)^- `MERGE_PENDING`: every readiness predicate above passes\.$", "insert_after",
     "\n- `MERGE_OBSERVED`: " + C.COND35 + ".", each(["PR-35"])),
    ("R-ITEM30b", r"(?m)^- `MERGE_PENDING`[^\n]*$", "insert_after", "\n- `MERGE_OBSERVED`: " + C.COND40 + ".", each(["RS-40"])),
    ("R-ITEM30c", r"\bsixth top-level PR-35 result\b", "replace", "seventh top-level PR-35 result", each(["PR-35"])),
    ("R-ITEM30d1", r"(?<=conditionally usable only after Nathan's manual merge)(?=\.)", "replace", ITEM30D1_NEW,
     each(["PR-35"])),                                                                                       # P-11
    ("R-ITEM30d2", r"The PR-40 handoff must say: [^\n]*?agent merge\.", "replace", ITEM30D2_NEW, each(["PR-35"])),
    ("R-26-RSP", r"RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b", "replace",
     "RESCOPE_PROPOSAL_ID, naming the RESCOPE_PROPOSAL by repository path", each(["PR-40"])),               # P-38
    ("R-ITEM31", r"An ordinary in-scope defect remains with the existing PR owner\.", "replace", ITEM31_NEW,
     each(["PR-40"])),
    ("R-OWN", OWN_AT, "insert_after", " " + OWN, each(list(OWN_AT))),
    ("R-A10", r"Reviewers remain read-only(?! toward the work they review)", "replace", A10_NEW,
     each(["OPS-10", "OPS-30", "PR-40", "QA-10"])),
    ("R-A5", r"Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written", "replace",
     {"*": A5_NEW, "GCFPE-MGMT-10": A5_MGMT}, each(["GCFPE-MGMT-10", "PR-35"])),                           # P-04
    ("R-A3a", r"Embed only applicable workflow contracts: [^.\n]*\. ?", "delete", "",
     each(["CL-20", "CL-30", "CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"])),
    ("R-A4a", r" These candidate URL tokens must be replaced by observed direct Notion URLs[^.\n]*\.", "delete", "",
     each(["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"])),
    ("R-A4c", r" This authoring candidate does not perform that update\.", "delete", "", each(["CL-40"])),
    ("R-CLAT", r"(?m)^\*\*Decide it during work:\*\*\n1\. [^\n]*\n2\. [^\n]*\n3\. [^\n]*\n?", "delete", "",
     each(["PR-10", "PR-20", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"])),
    ("R-ITEM18", r"(?=The existing noncanonical Candidate CRD Items List may be updated in place)", "replace",
     ITEM18_NEW, each(["CL-40"])),
    ("R-ITEM19", r"(?m)^4\. Include Master Scrum's precise board-update instruction[^.\n]*\.", "insert_after",
     ITEM19_NEW, each(["CL-20"])),
    ("R-ITEM34", r"(?<=code/Ops remediation\. Do not fix it here\.)", "replace", ITEM34_NEW, each(["QA-110"])),  # P-15 rev.
    ("R-ITEM35", r"(?<=`WRONG_ROUTE_APPROVED_BASE`) terminally\b", "replace", ITEM35_NEW, each(["QA-80"])),  # P-14
    ("R-ITEM38", r"material change \(D23-C\) change\b", "replace", "material change (D23-C)", each(["PR-10"])),
    ("R-ITEM23", RELEASE + r"[^\n]*\n?", "delete", "", {"GCFPE-MGMT-10-PROPOSED": 2}),                       # P-16
]

A7_LOCAL = (r"only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual merge occurred|"
            r"Nathan's PR-40 invocation asserts that the identified PR was manually merged|Nathan's invocation supplies "
            r"only the later manual-merge assertion|historical PR-35 `MERGE_PENDING` result, Nathan's later manual-merge "
            r"assertion|Nathan manual merge, PR-40 read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|"
            r"Nathan's later merge assertion and PR-40's independent|needed after Nathan's assertion: continue to `?PR-40|"
            r"states that Nathan's later invocation asserts the manual merge|"
            r"Return one conditional block for use only after Nathan manually merges the identified PR;")  # P-08

# LOCAL-only rules: anchors that must read 0 on their rows after all edits
CHECKS = [
    ("R-26-FRAME", r"recovery package carries the original CLASS_SELECTION_REF|UNRESOLVED_CLASSIFICATION_CASE with the "
                   r"preserved source/change facts|direct package contains the exact pending Specification, class/change "
                   r"lineage|recovery carries the original kickoff link, exact defect, class/change lineage|and approval "
                   r"lineage, the carried conflict register|actual mode, class/change/base lineage|carrying the exact "
                   r"qualified condition, lineage, evidence|Carry the complete candidate, positive closure and "
                   r"architecture-decision lineage|Carry exact (?:CRD|Epic) Specification|Each runnable (?:direct-native )?"
                   r"package states|must preserve in its execution result and return handoff|carry PR_INSTRUCTION_ID and "
                   r"its complete content|dependency and evidence history; read-only substantiation of the mismatch; "
                   r"completed work|dependency/evidence history, completed work and unaffected obligations|all actual "
                   r"merge/commit/order/check evidence|PR instruction and implementation result; actual merged-state "
                   r"evidence|dependency, acceptance and evidence history",
     ["CF-C-10", "CF-E-10", "CF-C-20", "CF-E-20", "CF-C-30", "CF-E-30", "CF-C-40", "CF-E-40", "CL-20", "CL-30",
      "CL-C-10", "CL-E-10", "OPS-10", "PR-10", "PR-20", "PR-35", "PR-40"]),
    ("R-26-BRANCH-SEND", r"(?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original "
                         r"Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session, "
                         r"open PR|commit and remote-head references; completed work|branch and repository/reference baseline",
     ["PR-10", "PR-20", "PR-30"]),
    ("R-26-BRANCH-RECV", r"Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed "
                         r"work, commits/local changes|reviews/checks already observed, unresolved items|with each actual PR "
                         r"reference, commit identity, order|dedicated session, workspace/worktree, branch, pull request, and "
                         r"current head",
     ["PR-35", "PR-40", "RS-20", "RS-40"]),
    ("R-A7-LOCAL", A7_LOCAL, ["PR-10", "PR-20", "PR-40", "DOC-10", "DOC-20", "RS-40"]),
    ("R-ITEM40", r"(?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|, in (?:the )?"
                 r"returned handoff\b|substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery "
                 r"packages|every next and recovery package)\b|Embed only applicable workflow contracts|These candidate "
                 r"URL tokens must be replaced|Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not "
                 r"written", ["GCFPE-MGMT-10-PROPOSED"]),                                                    # P-09
    ("R-ITEM23-gate", RELEASE, ["GCFPE-MGMT-10-PROPOSED"]),
    ("R-26-RSP-scan", r"RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b", ["PR-10", "PR-20", "PR-40"]),  # P-38
]

# LOCAL span kinds (the drafters' SPAN notes): anchor only (default), to end of line, to end of sentence, or through
SPAN = {
    **{k: "eol" for k in ["LPR-10-1", "LPR-10-4", "LPR-20-1", "LPR-20-3", "LPR-20-5", "LPR-20-6", "LPR-20-7", "LPR-20-8",
                          "LPR-35-1", "LPR-40-1", "LPR-40-2", "LPR-40-3"]},
    **{k: "eos" for k in ["LCL-20-1", "LCL-30-1", "LCL-C-10-1", "LCL-C-10-2", "LCL-E-10-1", "LCL-E-10-2"]},
    "LPR-10-2": ("through", "which runs in its own dedicated session."),
    "LPR-20-2": ("through", "and unresolved lineage."),
    "LPR-30-1": ("through", "and recovery lineage."),
    "LRS-20-1": ("through", "and unresolved work."),
    "LRS-40-1": ("through", "and return condition."),
    "LOPS-30-1": "anchor+space",
    "LQA-10-P19": "anchor+space",                                                                   # P-19, dry F
}


def local_pattern(e):
    a = re.escape(e["anchor"])
    s = SPAN.get(e["id"], "anchor")
    if s == "eol":
        return a + r"[^\n]*"
    if s == "eos":
        return a + r"[^.\n]*\."
    if s == "anchor+space":
        return a + r" ?"
    if isinstance(s, tuple):
        return a + r"[^\n]*?" + re.escape(s[1])
    return a


def _pick(v, pid):
    return v.get(pid, v.get("*")) if isinstance(v, dict) else v


def _edit(text, pattern, action, new, flags=0):
    ms = list(re.finditer(pattern, text, flags))
    def repl(m):
        if action == "replace":
            return new
        if action == "delete":
            return ""
        if action == "insert_after":
            return m.group(0) + new
        if action == "insert_before":
            return new + m.group(0)
        raise ValueError(action)
    return re.sub(pattern, repl, text, flags=flags), ms


def apply(pid, text):
    """The edited body and a per-rule report {id: {"hits", "expected", "ok"}}; nothing is forced."""
    rep = {}
    t = text
    for rid, anchor, action, new, expected in RULES:
        if pid not in expected:
            continue
        pat, nt = _pick(anchor, pid), _pick(new, pid)
        if rid == "R-CLAT":
            for m in re.finditer(pat, t):
                assert C.collapse(m.group(0)).rstrip("\n") == C.collapse(C.CLAT_DECIDE), "C-LAT block differs from canonical"
        t, ms = _edit(t, pat, action, nt)
        rep[rid] = {"hits": len(ms), "expected": expected[pid], "ok": len(ms) == expected[pid]}
    for e in LOCAL.get(pid, []):
        t, ms = _edit(t, local_pattern(e), e["action"], e["new_text"])
        rep[e["id"]] = {"hits": len(ms), "expected": 1, "ok": len(ms) == 1}
    for cid, pat, rows in CHECKS:
        if pid in rows:
            n = len(re.findall(pat, t))
            rep["CHECK " + cid] = {"hits": n, "expected": 0, "ok": n == 0}
    return t, rep


def pids():
    s = set()
    for _, _, _, _, expected in RULES:
        s |= set(expected)
    for _, _, rows in CHECKS:
        s |= set(rows)
    return sorted(s | {p for p, v in LOCAL.items() if v})


if __name__ == "__main__":
    # Self-test: no forbidden check reads any authored or canonical text; every anchor compiles.
    for rid, anchor, *_ in RULES:
        for p in (anchor.values() if isinstance(anchor, dict) else [anchor]):
            re.compile(p)
    texts = list(AUTHORED.values()) + list(C.CANON.values())
    bad = [(cid, k) for cid, pat, _ in CHECKS if cid != "R-ITEM23-gate" for k, v in {**AUTHORED, **C.CANON}.items()
           if re.search(pat, v)]
    print(json.dumps({"rules": len(RULES), "checks": len(CHECKS), "locals": sum(len(v) for v in LOCAL.values()),
                      "bodies": len(pids()), "checks_matching_authored_or_canonical": bad}, indent=1))
