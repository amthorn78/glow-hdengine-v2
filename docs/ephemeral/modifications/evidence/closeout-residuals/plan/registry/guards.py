"""Registry guard plan for MODIFICATION-20260923-closeout-residuals, PLAN repair round r1 (registry only).

Repairs the first-round draft (plan/registry/guards.py) under plan/r1/DECISIONS.md P-01..P-17 and P-28.
Patterns only; no prompt-body text. Each guard:
  (gid, shared_rule_ids, part, kind, value | {row: value}, rule_code, rows)
A value dict means per-row patterns (each row carries only its own alternative).

Changes against the first-round draft, by decision:
  P-01  R-26-BRANCH-RECV text: G-K22 unchanged (still matches); the PR-40 registry input follows the PR-40
        body (LPR-40-4 replacement at :4604, and LPR-40-5's P-01 line as its own input entry before W-4).
  P-02  G-K36 = the P-02 sentence; G-K35 split per row (each row only its own placement alternative).
  P-03  QA-10's G-K35 alternative = plain forbidden 'read-only audit and readiness role'.
  P-04  G-K39/G-K40 leave RS-40; GCFPE-MGMT-10's G-K40 = the P-04 variant; PR-35 keeps the base text.
  P-06  G-K19 PR-10 second alternative = 'dependency and evidence history; read-only substantiation ...'.
  P-08/P-42  G-K26: the DOC-10/DOC-20 site fragments appended to the first-round alternation (DOC-20 widened to
        '`?PR-40'), still one pattern on its 6 rows.
  P-15 (revised)  G-K47 = 'Do not fix it here\\.(?! This applies only before the whole approved run is complete)'.
  P-16  release-line suffix (?:\\*\\*|__|`){0,2}[ \\t]*: in the three PART-17 patterns.
  P-17  G-K08 = the PR drafter's amended pattern; on OPS-10/OPS-20 plus the ESC-30/RS-30 alternative.
  P-18/P-42  G-K52: CL-30 slot for LCL-30-2, filled with the dry-run-drafted pattern (dry B); a TBD value still
        stops the build (apply_registry.py --tbd K52 demonstrates it).
  P-38/P-42  G-K53: R-26-RSP's guard on PR-40.
  P-42  G-K54: the deleted 'A saved attachment ...' sentence (LOPS-30-1, LQA-10-P19) on OPS-30 and QA-10.
  P-12  every regression injection is at most 15 words (REGRESSIONS below).

Round 2 (plan/r1/DECISIONS.md P-55 to P-70; review wf_045af16b-3ed):
  P-55  G-K55 (forbidden 'outside the approved Plan, return the metadata\\b' on PR-30) guards LPR-30-2; its decision
        label is P-55 (summarize.py, build_guards_md.py).
  P-61  G-K24 (required W-4, 'PR-40 is entered on the observed merge event for the identified PR') goes on all 21
        ITEM-29 rows except PR-40 (20 rows: A7S1 without PR-40, A7CL, A7S3), and its shared rules gain R-A7-CL and
        R-A7-S3, which place W-4 on the CL and S3 rows. PR-40 keeps the parent's G25B ('PR-40 is entered on the
        observed merge event', CTR-002), which the same W-4 text satisfies (guard_tests.py T14).
  P-62  G-K39 (forbidden, the retired storage sentence) goes back on RS-40's row (A5_K39); G-K40 stays off RS-40.
"""

ALL55 = "ALL55"
TBD = "__TBD__"  # sentinel: apply_registry.py refuses to build while any guard value is TBD

# ---- PART-10 (ITEM-22): the six-ID mapping, ANALYZE-skill-evidence.md "Registry parent IDs" ----
PARENT_MAP = [
    # old id, old title, new id, new title, lane values, row values
    ("3c74590a05eb811d8433e7022629e213", "HDE Change Flow", "3db4590a05eb81d59059eb6b95ed5fcf",
     "HDE Change Flow — GCFPE-20260914.1 — 091426.1", 7, 18),
    ("3c74590a05eb81f2953de712f2adb6fa", "HDE IA", "3db4590a05eb8195a2ccf7c0959a8b6e",
     "HDE IA — GCFPE-20260914.1 — 091426.1", 5, 21),
    ("3c74590a05eb8149905fd694f6d2901a", "HDE QA", "3db4590a05eb814d96d3dcfa8835f96d",
     "HDE QA — GCFPE-20260914.1 — 091426.1", 1, 10),
    ("3c74590a05eb8123bc55ca7f99ce176c", "Escalation", "3db4590a05eb81cd938de84cfffead9c",
     "Escalation — GCFPE-20260914.1 — 091426.1", 1, 4),
    ("3c74590a05eb8176baf8cb59f1631f3c", "HDE TW", "3db4590a05eb811b9c14f2ae89c28df7",
     "HDE TW — GCFPE-20260914.1 — 091426.1", 1, 1),
    ("3cc4590a05eb8101b5ded32c12616eb6", "Glow HDE Prompt Flow Index", "3db4590a05eb81de9736ea69bac61016",
     "Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1", 1, 1),
]

# ---- PART-17 (ITEM-36): release-line guards, window -> whole body; P-16 suffix ----
OLD_HDR = r"\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?"
OLD_END = r"(?:\*\*|__|`)?[ \t]*:"
NEW_HDR = r"(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?"
NEW_END = r"(?:\*\*|__|`){0,2}[ \t]*:"                                                      # P-16
RELEASE_LABELS = [("Prompt [Vv]ersion", "SRC-001"), ("Ecosystem release", "INV-003"), ("Set", "SRC-001")]
# R-ITEM23's single pattern (engine RELEASE, P-16); the three registry patterns are its per-label split.
RELEASE_ALL = NEW_HDR + r"(?:Prompt [Vv]ersion|Ecosystem release|Set)" + NEW_END

# ---- PART-18 (ITEM-37): C-LAT decide block in the 8 non-implementing rows ----
CLAT8 = ["PR-10", "PR-20", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"]
CLAT_REQ = ("Decide it during work", "CTR-002")      # removed from required_regex on CLAT8
CLAT_FORBID = ("Decide it during work", "CTR-001")   # added to forbidden_regex on CLAT8

# ---- row sets from the shared rules' applies_to ----
A1A = ["CL-20", "CL-30", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30",
       "ESC-40", "OPS-10", "OPS-20", "PR-30", "PR-40", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50",
       "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"]
A1B = ["CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "QA-10"]                      # P-05: PR-10 in A1b
A2A = ["DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50",
       "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"]
A2B = ["CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"]
A2E = ["CL-C-10", "CL-E-10", "OPS-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"]
A2G = ["IA-10", "IA-20", "IA-30", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-40", "QA-10"]
P1 = ["OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"]
P3 = ["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"]
P4 = ["CL-C-10", "CL-E-10", "PR-40", "QA-10", "PR-10", "PR-20", "PR-30", "OPS-10", "OPS-20", "OPS-30"]  # P-13
A7S1 = ["OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"]
A7CL = ["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"]
A7S3 = ["CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "ESC-40", "QA-20"]
A7LOCAL = ["PR-10", "PR-20", "PR-40", "DOC-10", "DOC-20", "RS-40"]
OWN11 = ["CL-20", "CL-30", "CL-40", "CL-E-20", "DOC-20", "ESC-25", "GCFPE-MGMT-10", "PR-20", "PR-40", "PR-50", "QA-10"]
A10 = ["OPS-10", "OPS-30", "PR-40", "QA-10"]
A5 = ["GCFPE-MGMT-10", "PR-35"]                                                        # P-04: RS-40 leaves R-A5
A5_K39 = A5 + ["RS-40"]                                    # P-62: the forbidden G-K39 goes back on RS-40; G-K40 stays off
A7ALL = A7S1 + A7CL + A7S3                                                              # the 21 ITEM-29 rows
K24_ROWS = [r for r in A7ALL if r != "PR-40"]                  # P-61: 20 rows; PR-40 keeps the parent's G25B
A3A = ["CL-20", "CL-30", "CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"]
A4A = ["CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10"]

# ---- texts this Modification authors (DECISIONS.md), for the guards that follow them ----
RECV_TEXT = ("The branch, head and commits are verified at entry from the recorded vehicle and repository state; "
             "the handoff does not carry them.")                                                           # P-01
OWN_TEXT = ("Every statement in this prompt that it is read-only or does not change the repository excludes its own "
            "output artifacts, which it writes, commits and pushes, and any pull request that carries them.")   # P-02
QA10_ROLE_NEW = "This is an audit and readiness role."                                                     # P-03
A5_NEW = "This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`"
A5_MGMT = A5_NEW + ", the controls it maintains only under `docs/prompt_ecosystem_management/`"            # P-04

# ---- patterns (verbatim from the shared rules unless a decision is noted) ----
A1_FORBID = r"(?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|, in (?:the )?returned handoff\b"
A1_REQ = r"in the output artifact's (?:existing )?permitted metadata"
A2_FORBID = (r"substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery packages|every next and "
             r"recovery package)\b|review result and every native return\b|and every return package\b|receipt, review and "
             r"handoff metadata|receipt and handoff when applicable")
A2_REQ = r"(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff names"
A2E_REQ = r"unresolved facts in the output artifact, which each next or recovery handoff names"
A2F1_REQ = r"every native return names those artifacts"
A2F2_REQ = r"every return package names those artifacts"
# P-17: the PR drafter's amended pattern (plan_result.json bodies, PR-20 unplaceable[0], verbatim) ...
A2G_FORBID = (r"(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?: and artifact "
              r"lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive input)\b[^\n]*`?"
              r"CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete RS-\d+ package):"
              r"\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict "
              r"register\b)")
# ... plus, on OPS-10 and OPS-20, P-17's alternative, folded into the same outer group (one inline flag at the start)
A2G_OPS_EXT = r"^(?:Complete return to ESC-30|RS-30 native revision):[^\n]*CANON_CONFLICT_REGISTER"
A2G_FORBID_OPS = A2G_FORBID[:-1] + "|" + A2G_OPS_EXT + ")"
K08 = {row: (A2G_FORBID_OPS if row in ("OPS-10", "OPS-20") else A2G_FORBID) for row in A2G}
P1_FORBID = r"current status and lineage; decisions already made|Carry complete native inputs rather than referring to"
P1_REQ = (r"Then give the other fields the handoff rule above names; sections the artifact already holds are named, "
          r"not repeated\.")
P1B_FORBID = r"unresolved items/owners, next action, and expected (?:output|review state)"
P3_FORBID = r"lineage into its result and handoff\b"
P3_REQ = r"PF10/addendum lineage into its result artifact, which the handoff names"
P4_FORBID = r"Catalogs and runtime handoffs carry\b"
TASK_FORBID = r"native inputs, lineage, current state, gates, risks and required action"
TASK_REQ = r"each input artifact by repository path; the artifacts hold the rest"
CLOSE_FORBID = r"Carry the positive closure decision, complete post-closure results"
CLOSE_REQ = r"Name the positive closure decision and every post-closure result artifact by repository path"
# R-26-FRAME: each body's own fragments (first-round mapping; P-06 replaces PR-10's second fragment).
F = {
    "cls_rec": r"recovery package carries the original CLASS_SELECTION_REF",
    "unres": r"UNRESOLVED_CLASSIFICATION_CASE with the preserved source/change facts",
    "direct_spec": r"direct package contains the exact pending Specification, class/change lineage",
    "kick_rec": r"recovery carries the original kickoff link, exact defect, class/change lineage",
    "appr_reg": r"and approval lineage, the carried conflict register",
    "mode": r"actual mode, class/change/base lineage",
    "qual": r"carrying the exact qualified condition, lineage, evidence",
    "cand": r"Carry the complete candidate, positive closure and architecture-decision lineage",
    "spec": r"Carry exact (?:CRD|Epic) Specification",
    "runnable": r"Each runnable (?:direct-native )?package states",
    "ops_ret": r"must preserve in its execution result and return handoff",
    "pri": r"carry PR_INSTRUCTION_ID and its complete content",
    "dep_ev": r"dependency and evidence history; read-only substantiation of the mismatch; completed work",  # P-06
    "dep_ev2": r"dependency/evidence history, completed work and unaffected obligations",
    "merge_ev": r"all actual merge/commit/order/check evidence",
    "stage": r"current stage and suspended boundary, completed work, dependencies, evidence",
    "accept": r"PR instruction and implementation result; actual merged-state evidence",
    "dep_acc": r"dependency, acceptance and evidence history; completed work",
    "review_work": r"all completed review work; attempts; limitations",
}
FRAME_ROWS = {
    "CF-C-10": ["cls_rec", "unres"], "CF-E-10": ["cls_rec", "unres"],
    "CF-C-20": ["direct_spec", "kick_rec"], "CF-E-20": ["direct_spec", "kick_rec"],
    "CF-C-30": ["appr_reg"], "CF-E-30": ["appr_reg"],
    "CF-C-40": ["mode"], "CF-E-40": ["mode"],
    "CL-20": ["qual"], "CL-30": ["cand"],
    "CL-C-10": ["spec", "runnable"], "CL-E-10": ["spec", "runnable"],
    "OPS-10": ["ops_ret"],
    "PR-10": ["pri", "dep_ev"],
    "PR-20": ["dep_ev2", "merge_ev", "stage"],
    "PR-40": ["accept", "dep_acc", "review_work"],
}
FRAME_FORBID = {row: "|".join(F[k] for k in keys) for row, keys in FRAME_ROWS.items()}
BSEND_FORBID = (r"(?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original Proceed, "
                r"dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session, open PR|commit and "
                r"remote-head references; completed work|branch and repository/reference baseline")
BRECV_FORBID = (r"Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed work, "
                r"commits/local changes|reviews/checks already observed, unresolved items|with each actual PR reference, "
                r"commit identity, order")
BRECV_REQ = r"verified at entry from the recorded vehicle and repository state; the handoff does not carry them"  # P-01: unchanged
A7_FORBID = (r"Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies the later "
             r"asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval effect is "
             r"defined above")
W4_REQ = r"PR-40 is entered on the observed merge event for the identified PR"
G25B_REQ = r"PR-40 is entered on the observed merge event"   # the parent's G25B on PR-40 (spec v2 §6/§7), kept (P-61)
ONCE_REQ = r"PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives"
# P-08 / P-42: the first-round R-A7-LOCAL alternation (PR-10, PR-20, PR-40 sites) with the DOC-10 and DOC-20 site
# fragments appended (DOC-20's widened to '`?PR-40'); one pattern on the rule's 6 rows. PR-20's second site and RS-40's
# sites carry 'Nathan's ... invocation asserts', which G-K23 forbids on every row.
A7LOCAL_FORBID = (r"only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual merge "
                  r"occurred|Nathan's invocation supplies only the later manual-merge assertion|historical PR-35 "
                  r"`MERGE_PENDING` result, Nathan's later manual-merge assertion|"
                  r"Nathan manual merge, PR-40 read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|"
                  r"Nathan's later merge assertion and PR-40's independent|"
                  r"needed after Nathan's assertion: continue to `?PR-40")
ITEM21_REQ = r"that entry creates no runtime approval"
ITEM30_REQ = (r"`MERGE_OBSERVED`: [^\n]*?the subscribed PR-35 session observes the merge of the identified PR, "
              r"performed by Nathan")
ITEM30C_FORBID = r"sixth top-level PR-35 result"
ITEM30C_REQ = r"seventh top-level PR-35 result"
ITEM30D_FORBID = r"The PR-40 handoff must say:|Nathan's later paste asserts"
ITEM30D_REQ = r"for `MERGE_OBSERVED`, it is the same selected PR-40"
ITEM31_FORBID = r"ordinary in-scope defect remains with the existing PR owner"
ITEM31_REQ = r"re-plans through `?PR-20`?, as \*\*PRECISE IN-SCOPE DEFECT → re-plan\*\* states"
# P-02 / P-03: R-OWN forbidden, one alternative per row (its own placement anchor), not followed by the OWN sentence.
OWN_LOOK = (r"(?! Every statement in this prompt that it is read-only or does not change the repository excludes its "
            r"own output artifacts)")
OWN_ALT = {
    "PR-40": r"operating read-only",
    "CL-E-20": r"revalidation session, read-only",
    "DOC-20": r"do not edit documentation, Canon, PF10, or repository state",
    "ESC-25": r"read-only repository reviewer[^.\n]*",
    "PR-20": r"Do not mutate the repository in this authoring operation",
    "PR-50": r"otherwise mutating the workspace, worktree, branch, open PR, commits or evidence[^.\n]*",
    "GCFPE-MGMT-10": r"does not execute product Change Flow, implementation, repository work[^.\n]*",
    "CL-20": r"Use only the read-only tools, stores, repository access[^.\n]*",
    "CL-30": r"Use only the read-only tools, stores, repository access[^.\n]*",
    "CL-40": r"It does not edit Canonical PF09, PF10, Canon, a board, registry, repository[^.\n]*",
}
K35 = {row: alt + r"\." + OWN_LOOK for row, alt in OWN_ALT.items()}
K35["QA-10"] = r"read-only audit and readiness role"                                                     # P-03
OWN_REQ = (r"Every statement in this prompt that it is read-only or does not change the repository excludes its own "
           r"output artifacts, which it writes, commits and pushes, and any pull request that carries them\.")   # P-02
A10_FORBID = r"Reviewers remain read-only(?! toward the work they review)"
A10_REQ = r"Reviewers remain read-only toward the work they review"
A5_FORBID = r"Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written"
K40 = {"GCFPE-MGMT-10": A5_MGMT, "PR-35": A5_NEW}                                                         # P-04
A3A_FORBID = r"Embed only applicable workflow contracts"
A4A_FORBID = r"These candidate URL tokens must be replaced"
A4C_FORBID = r"This authoring candidate does not perform that update"
ITEM18_FORBID = r"\{\{CANDIDATE_CRD_LIST_URL\}\}"
ITEM18_REQ = (r"Notion page `?Candidate CRD Items List`? \(`?https://app\.notion\.com/p/[0-9a-f]{32}"
              r"(?:\?pvs=\d+)?`?\)")
ITEM19_REQ = r"when none is supplied, record the board update as pending, owned under PF04 §9\.1\.1"
ITEM34_FORBID = r"code/Ops remediation\. Do not fix it here\.(?! This applies only before the whole approved run is complete)"  # P-15 final: tied to its site
ITEM34_REQ = r"a completed failing run is `ACCEPT` and continues to QA-120"
ITEM35_FORBID = r"`WRONG_ROUTE_APPROVED_BASE` terminally"
ITEM35_REQ = r"routed as \*Required result and routing\* states"                                         # P-14: unchanged
# P-18 / P-42: CL-30's second A2 carrier (LCL-30-2). The slot was TBD until the dry run drafted it (dry B,
# plan/r1/dry/B/report.json proposed_guard); set CL30_A2_FORBID = TBD and the build refuses again.
CL30_A2_CANDIDATE = r"decision lineage; existing ADR/conflict history"
CL30_A2_FORBID = CL30_A2_CANDIDATE
RSP_FORBID = r"RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b"                                         # P-38 (engine R-26-RSP)
SAVED_FORBID = r"A saved attachment, link or scattered fields do not replace the handoff\."                # P-42

# gid, shared rules, part, kind, value, code, rows
GUARDS = [
    # PART-13 — ITEM-26/27/28 (handoff content and storage): forbidden TOP-001 (as the parent's G06), required CTR-002 (as G05)
    ("K01", ["R-A1a", "R-A1b", "R-A1c", "R-A1d", "R-A1e", "R-A1f"], "PART-13", "forbidden_regex", A1_FORBID, "TOP-001", ALL55),
    ("K02", ["R-A1a", "R-A1b"], "PART-13", "required_regex", A1_REQ, "CTR-002", A1A + A1B),
    ("K03", ["R-A2a", "R-A2b", "R-A2c", "R-A2d", "R-A2e", "R-A2f1", "R-A2f2"], "PART-13", "forbidden_regex", A2_FORBID, "TOP-001", ALL55),
    ("K04", ["R-A2a", "R-A2b", "R-A2c", "R-A2d"], "PART-13", "required_regex", A2_REQ, "CTR-002", A2A + A2B + ["OPS-10", "OPS-20"]),
    ("K05", ["R-A2e"], "PART-13", "required_regex", A2E_REQ, "CTR-002", A2E),
    ("K06", ["R-A2f1"], "PART-13", "required_regex", A2F1_REQ, "CTR-002", ["PR-40"]),
    ("K07", ["R-A2f2"], "PART-13", "required_regex", A2F2_REQ, "CTR-002", ["QA-10"]),
    ("K08", ["R-A2g"], "PART-13", "forbidden_regex", K08, "TOP-001", A2G),                            # P-17
    ("K09", ["R-26-P1"], "PART-13", "forbidden_regex", P1_FORBID, "TOP-001", ALL55),
    ("K10", ["R-26-P1"], "PART-13", "required_regex", P1_REQ, "CTR-002", P1),
    ("K11", ["R-26-P1b"], "PART-13", "forbidden_regex", P1B_FORBID, "TOP-001", ["IA-30", "UTIL-10"]),
    ("K12", ["R-26-P3"], "PART-13", "forbidden_regex", P3_FORBID, "TOP-001", P3),
    ("K13", ["R-26-P3"], "PART-13", "required_regex", P3_REQ, "CTR-002", P3),
    ("K14", ["R-26-P4"], "PART-13", "forbidden_regex", P4_FORBID, "TOP-001", P4),
    ("K15", ["R-26-TASK"], "PART-13", "forbidden_regex", TASK_FORBID, "TOP-001", ["OPS-30", "QA-10"]),
    ("K16", ["R-26-TASK"], "PART-13", "required_regex", TASK_REQ, "CTR-002", ["OPS-30", "QA-10"]),
    ("K17", ["R-26-CLOSE"], "PART-13", "forbidden_regex", CLOSE_FORBID, "TOP-001", ["CL-20", "CL-30"]),
    ("K18", ["R-26-CLOSE"], "PART-13", "required_regex", CLOSE_REQ, "CTR-002", ["CL-20", "CL-30"]),
    ("K19", ["R-26-FRAME"], "PART-13", "forbidden_regex", FRAME_FORBID, "TOP-001", list(FRAME_ROWS)),  # P-06 (PR-10)
    ("K20", ["R-26-BRANCH-SEND"], "PART-13", "forbidden_regex", BSEND_FORBID, "TOP-001", ["PR-10", "PR-20", "PR-30"]),
    ("K21", ["R-26-BRANCH-RECV", "R-26-FRAME"], "PART-13", "forbidden_regex", BRECV_FORBID, "TOP-001", ["PR-35", "PR-40", "RS-20", "RS-40"]),
    ("K22", ["R-26-BRANCH-RECV"], "PART-13", "required_regex", BRECV_REQ, "CTR-002", ["PR-35", "PR-40", "RS-20", "RS-40"]),
    # PART-14 — ITEM-21/29/30/31: forbidden CTR-001 (as the parent's PR-40 guard G26), required CTR-002 (as G25/G25B)
    ("K23", ["R-A7-S1a", "R-A7-S1b", "R-A7-S2", "R-A7-CL", "R-A7-S3", "R-ITEM21", "R-A7-LOCAL"], "PART-14", "forbidden_regex", A7_FORBID, "CTR-001", ALL55),
    ("K24", ["R-A7-S1b", "R-A7-S2", "R-A7-CL", "R-A7-S3"], "PART-14", "required_regex", W4_REQ, "CTR-002", K24_ROWS),  # P-61
    ("K25", ["R-A7-S1b", "R-A7-CL", "R-A7-S3"], "PART-14", "required_regex", ONCE_REQ, "CTR-002", A7S1 + A7CL + A7S3),
    ("K26", ["R-A7-LOCAL"], "PART-14", "forbidden_regex", A7LOCAL_FORBID, "CTR-001", A7LOCAL),        # P-08, P-42
    ("K27", ["R-ITEM21"], "PART-14", "required_regex", ITEM21_REQ, "CTR-002", ["CL-20", "CL-30", "CL-C-10", "CL-E-10"]),
    ("K28", ["R-ITEM30a", "R-ITEM30b"], "PART-14", "required_regex", ITEM30_REQ, "CTR-002", ["PR-35", "RS-40"]),
    ("K29", ["R-ITEM30a", "R-ITEM30c"], "PART-14", "forbidden_regex", ITEM30C_FORBID, "CTR-001", ["PR-35"]),
    ("K30", ["R-ITEM30c"], "PART-14", "required_regex", ITEM30C_REQ, "CTR-002", ["PR-35"]),
    ("K31", ["R-ITEM30d"], "PART-14", "forbidden_regex", ITEM30D_FORBID, "CTR-001", ["PR-35"]),
    ("K32", ["R-ITEM30d"], "PART-14", "required_regex", ITEM30D_REQ, "CTR-002", ["PR-35"]),
    ("K33", ["R-ITEM31"], "PART-14", "forbidden_regex", ITEM31_FORBID, "CTR-001", ["PR-40"]),
    ("K34", ["R-ITEM31"], "PART-14", "required_regex", ITEM31_REQ, "CTR-002", ["PR-40"]),
    # PART-05 — ITEM-17/32
    ("K35", ["R-OWN"], "PART-05", "forbidden_regex", K35, "CTR-001", OWN11),                          # P-02, P-03
    ("K36", ["R-OWN"], "PART-05", "required_regex", OWN_REQ, "CTR-002", OWN11),                       # P-02
    ("K37", ["R-A10"], "PART-05", "forbidden_regex", A10_FORBID, "CTR-001", ALL55),
    ("K38", ["R-A10"], "PART-05", "required_regex", A10_REQ, "CTR-002", A10),
    ("K39", ["R-A5"], "PART-05", "forbidden_regex", A5_FORBID, "CTR-001", A5_K39),                     # P-04, P-62
    ("K40", ["R-A5"], "PART-05", "required_regex", K40, "CTR-002", A5),                                # P-04
    # PART-15 — ITEM-33
    ("K41", ["R-A3a"], "PART-15", "forbidden_regex", A3A_FORBID, "CTR-001", A3A),
    ("K42", ["R-A4a"], "PART-15", "forbidden_regex", A4A_FORBID, "CTR-001", A4A),
    ("K43", ["R-A4c", "R-ITEM18"], "PART-15", "forbidden_regex", A4C_FORBID, "CTR-001", ["CL-40"]),
    # PART-06 — ITEM-18
    ("K44", ["R-ITEM18"], "PART-06", "forbidden_regex", ITEM18_FORBID, "CTR-001", ["CL-40"]),
    ("K45", ["R-ITEM18"], "PART-06", "required_regex", ITEM18_REQ, "CTR-002", ["CL-40"]),
    # PART-07 — ITEM-19
    ("K46", ["R-ITEM19"], "PART-07", "required_regex", ITEM19_REQ, "CTR-002", ["CL-20"]),
    # PART-16 — ITEM-34/35
    ("K47", ["R-ITEM34"], "PART-16", "forbidden_regex", ITEM34_FORBID, "CTR-001", ["QA-110"]),         # P-15 (revised)
    ("K48", ["R-ITEM34"], "PART-16", "required_regex", ITEM34_REQ, "CTR-002", ["QA-110"]),
    ("K49", ["R-ITEM35"], "PART-16", "forbidden_regex", ITEM35_FORBID, "CTR-001", ["QA-80"]),
    ("K50", ["R-ITEM35"], "PART-16", "required_regex", ITEM35_REQ, "CTR-002", ["QA-80"]),
    # PART-18 — ITEM-37 (the required G10 is removed from the same 8 rows by apply_registry.py)
    ("K51", ["R-CLAT"], "PART-18", "forbidden_regex", CLAT_FORBID[0], CLAT_FORBID[1], CLAT8),
    # PART-13 — ITEM-27, P-18: CL-30's second A2 carrier (LCL-30-2)
    ("K52", ["R-A2-CL30 (LCL-30-2, P-18)"], "PART-13", "forbidden_regex", CL30_A2_FORBID, "TOP-001", ["CL-30"]),
    # PART-13 — ITEM-26, P-38: PR-40's RS-20 package (engine rule R-26-RSP)
    ("K53", ["R-26-RSP (P-38)"], "PART-13", "forbidden_regex", RSP_FORBID, "TOP-001", ["PR-40"]),
    # PART-13 — ITEM-26, P-42: the deleted Task-only transport sentence (LOPS-30-1, LQA-10-P19)
    ("K54", ["LOPS-30-1, LQA-10-P19 (P-19, P-42)"], "PART-13", "forbidden_regex", SAVED_FORBID, "TOP-001", ["OPS-30", "QA-10"]),
    # PART-13 — ITEM-27 (A1 variant), P-55: PR-30's LPR-30-2
    ("K55", ["LPR-30-2 (P-55)"], "PART-13", "forbidden_regex", r"outside the approved Plan, return the metadata\b", "TOP-001", ["PR-30"]),
]

# ---- regression injections (P-12): at most 15 words each; forbidden: the text that must fire the guard when
# present; required: the retired wording that, put back in place of the new text, leaves the guard unmatched.
# {gid: {row or "*": text}}; the first row named is the row the regression line cites.
RELEASE_INJ = {"Prompt [Vv]ersion": "**`Prompt version`**: 3.3.1", "Ecosystem release": "**Ecosystem release:** GCFPE-20260914.1",
               "Set": "3. **`Set`**: 091426.1"}
REGRESSIONS = {
    "K01": {"*": "metadata or handoff"},
    "K02": {"*": "in permitted metadata or handoff"},
    "K03": {"*": "substantive artifact and handoff"},
    "K04": {"*": "in the existing substantive artifact and handoff"},
    "K05": {"*": "unresolved facts through all next/recovery packages"},
    "K06": {"*": "review result and every native return without deciding Canon"},
    "K07": {"*": "`QA_READINESS` and every return package"},
    "K08": {"*": "Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING; CANON_CONFLICT_REGISTER",
            "OPS-10": "Complete return to ESC-30: ORIGINATING_FINDING_REF, CANON_CONFLICT_REGISTER",
            "OPS-20": "RS-30 native revision: RESCOPE_REVIEW_ID, CANON_CONFLICT_REGISTER"},
    "K09": {"*": "current status and lineage; decisions already made"},
    "K10": {"*": "current status and lineage; decisions already made"},
    "K11": {"*": "unresolved items/owners, next action, and expected output"},
    "K12": {"*": "lineage into its result and handoff"},
    "K13": {"*": "PF10/addendum lineage into its result and handoff"},
    "K14": {"*": "Catalogs and runtime handoffs carry"},
    "K15": {"*": "native inputs, lineage, current state, gates, risks and required action"},
    "K16": {"*": "native inputs, lineage, current state, gates, risks and required action"},
    "K17": {"*": "Carry the positive closure decision, complete post-closure results"},
    "K18": {"*": "Carry the positive closure decision, complete post-closure results"},
    "K19": {r: None for r in FRAME_ROWS},   # filled below: each row's first fragment, literal
    "K20": {"*": "hands the workspace/worktree, branch"},
    "K21": {"*": "reviews/checks already observed, unresolved items", "PR-40": "with each actual PR reference, commit identity, order",
            "RS-20": "Carry original Proceed, dedicated PR session, workspace/worktree, branch",
            "RS-40": "current head; completed work, commits/local changes"},
    "K22": {"*": "open PR, tests, reviews/checks already observed, unresolved items"},
    "K23": {"*": "Nathan's later invocation asserts"},
    # P-61: each row's retired wording is the text its own W-4-placing rule replaces (R-A7-S2, R-A7-CL, R-A7-S3)
    "K24": {"*": "Nathan's later PR-40 invocation asserts that a manual merge occurred;",
            **{r: "Nathan's later manual PR-40 invocation asserts only that he manually merged the identified PR;"
               for r in A7CL},
            **{r: "PR-40 independently verifies the later asserted merge and landed lineage." for r in A7S3}},
    "K25": {"*": "PR-40 independently verifies the later asserted merge and landed lineage."},
    "K26": {"*": "only after Nathan asserts it occurred may PR-40",
            "PR-20": "Nathan invokes PR-40 asserting that manual merge occurred",
            "PR-40": "Nathan's invocation supplies only the later manual-merge assertion",
            "DOC-10": "Nathan manual merge, PR-40 read-only landed-lineage review",
            "DOC-20": "needed after Nathan's assertion: continue to `PR-40"},
    "K27": {"*": "The specific Product Owner PR-40 merge-approval effect is defined above"},
    "K28": {"*": "- `MERGE_PENDING`: every readiness predicate above passes."},
    "K29": {"*": "sixth top-level PR-35 result"},
    "K30": {"*": "sixth top-level PR-35 result"},
    "K31": {"*": "The PR-40 handoff must say:"},
    "K32": {"*": "conditionally usable only after Nathan's manual merge."},
    "K33": {"*": "ordinary in-scope defect remains with the existing PR owner"},
    "K34": {"*": "An ordinary in-scope defect remains with the existing PR owner."},
    "K35": {"PR-40": "operating read-only.", "CL-E-20": "revalidation session, read-only.",
            "DOC-20": "do not edit documentation, Canon, PF10, or repository state.",
            "ESC-25": "read-only repository reviewer.",
            "PR-20": "Do not mutate the repository in this authoring operation.",
            "PR-50": "otherwise mutating the workspace, worktree, branch, open PR, commits or evidence.",
            "GCFPE-MGMT-10": "does not execute product Change Flow, implementation, repository work.",
            "CL-20": "Use only the read-only tools, stores, repository access.",
            "CL-30": "Use only the read-only tools, stores, repository access.",
            "CL-40": "It does not edit Canonical PF09, PF10, Canon, a board, registry, repository.",
            "QA-10": "read-only audit and readiness role"},
    "K36": {"*": "excludes its own output artifacts, which it writes, commits and pushes."},
    "K37": {"*": "Reviewers remain read-only"},
    "K38": {"*": "Reviewers remain read-only and acceptance requires substantive evidence."},
    "K39": {"*": "Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written"},
    "K40": {"*": "Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written"},
    "K41": {"*": "Embed only applicable workflow contracts"},
    "K42": {"*": "These candidate URL tokens must be replaced"},
    "K43": {"*": "This authoring candidate does not perform that update"},
    "K44": {"*": "(`{{CANDIDATE_CRD_LIST_URL}}`)"},
    "K45": {"*": "Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`)"},
    "K46": {"*": "4. Include Master Scrum's precise board-update instruction for the board."},
    "K47": {"*": "code/Ops remediation. Do not fix it here."},
    "K55": {"*": "If that path is outside the approved Plan, return the metadata"},
    "K48": {"*": "code/Ops remediation. Do not fix it here."},
    "K49": {"*": "`WRONG_ROUTE_APPROVED_BASE` terminally"},
    "K50": {"*": "return `WRONG_ROUTE_APPROVED_BASE` terminally"},
    "K51": {"*": "**Decide it during work:**"},
    "K52": {"*": "decision lineage; existing ADR/conflict history"},
    "K53": {"*": "RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL"},
    "K54": {"*": "A saved attachment, link or scattered fields do not replace the handoff."},
}
REGRESSIONS["K19"] = {r: {"cls_rec": "recovery package carries the original CLASS_SELECTION_REF",
                          "direct_spec": "direct package contains the exact pending Specification, class/change lineage",
                          "appr_reg": "and approval lineage, the carried conflict register",
                          "mode": "actual mode, class/change/base lineage",
                          "qual": "carrying the exact qualified condition, lineage, evidence",
                          "cand": "Carry the complete candidate, positive closure and architecture-decision lineage",
                          "spec": "Carry exact Epic Specification",
                          "ops_ret": "must preserve in its execution result and return handoff",
                          "pri": "carry PR_INSTRUCTION_ID and its complete content",
                          "dep_ev2": "dependency/evidence history, completed work and unaffected obligations",
                          "accept": "PR instruction and implementation result; actual merged-state evidence"}[ks[0]]
                      for r, ks in FRAME_ROWS.items()}
REGRESSIONS["K19"]["PR-10"] = "dependency and evidence history; read-only substantiation of the mismatch; completed work"  # P-06

# ---- non-assertion fields ----
CL40_ALLOWED_NEW = ("Update the Notion page Candidate CRD Items List in place with this change's new CRD candidates, "
                    "and no other Notion page; that page is the list's only store, named by a destination rule")
PR40_INPUT_OLD = ("The complete ordered PR_REFS for this work unit, with each actual PR reference, commit identity, order, "
                  "review/check state and merge evidence")
# LPR-40-4 (the body's Inputs bullet after the edit; the bullet's final period is not in the registry value)
PR40_INPUT_NEW = ("The complete ordered PR_REFS for this work unit; PR-40 resolves each PR's commits, order, review/check "
                  "state and merge evidence from repository evidence")
# LPR-40-5: P-01's sentence on its own line after the last Inputs bullet, before the W-4 paragraph, which the
# registry already carries as its own input entry; so the sentence becomes its own entry right before W-4.
PR40_INPUT_RECV = RECV_TEXT
PR40_INPUT_AFTER = ("CANON_CONFLICT_REGISTER, recovery state, truthful pending, NOT PRODUCED and NOT EXECUTED values, and "
                    "all actual access limitations")
PR40_INPUT_W4_PREFIX = "PR-40 is entered on the observed merge event for the identified PR"
