#!/usr/bin/env python3
"""Synthetic guard tests for the closeout-residuals registry draft, PLAN repair r1. No prompt body is read.

Inputs: registry.new.md (apply_registry.py --allow-tbd), the canonical texts read verbatim from spec v2 §3 and
the decision record's once-per-merge successor, the authored new texts (DECISIONS.md literals, plan_result.json
canon.rules new_text and bodies local_edits new_text, the r1 engine's AUTHORED texts and locals.json new_text),
and regression injections of at most 15 words (guards.REGRESSIONS and the per-rule CASES below).

  T1  every regex in the edited registry (and the K52 candidate) compiles on this Python;
  T2  per rule: forbidden guards silent on the after-text, fire on each injection; required guards match the
      after-text, fail on each injection, and fail when their own match is removed;
  T3  new/changed forbidden guards vs every canonical and authored text (intended hits listed);
  T4  per row (P-12): a synthetic document of canonical texts + the row's after-texts satisfies every new
      required guard and trips no new forbidden guard; every regression (CASES and REGRESSIONS), swapped in or
      appended as the dry run does, makes the row fail;
  T5  P-01 and P-02 sentences: no forbidden pattern of the new registry fires on them; G06 silent with the
      P-01 sentence right after a NEXT_PROMPT_HANDOFF mention and no blank line;
  T6  PART-17 with the P-16 suffix;
  T7  NAM-002 prototype in memory (nam002_live.py on a synthetic child list; no Notion fetch);
  T8  regressions: word counts (<= 15), each fires, minimality of forbidden fragments;
  T9  GUARD-001 anchor-level coverage of every r1 LOCAL edit (anchor fires a row guard, new_text silent);
  T10 P-15: G-K47 under DECISIONS' placement and under the r1 engine's 'P-15 rev.' placement;
  T11 P-18: the dry-run B candidate for the TBD G-K52.
"""
import hashlib, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, HERE + "/wga_scripts")
from audit_workspace_governance import load_data  # noqa: E402
import guards as G  # noqa: E402
import nam002_live as N2  # noqa: E402

REPO = "/home/user/glow-hdengine-v2"
new = load_data(HERE + "/registry.new.md")
old = load_data(HERE + "/registry.head.md")
ROWS = {r["prompt_key"]: r for r in new["prompts"]}
KEYS = list(ROWS)
val = lambda x: x["value"] if isinstance(x, dict) else x
out = {"inputs": {}}
words = lambda s: len(s.split())


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ---- canonical texts, read verbatim --------------------------------------------------------------
SPEC = REPO + "/docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md"
spec = open(SPEC, encoding="utf-8").read()
s3 = spec[spec.index("## §3 Canonical wording, final"):spec.index("## §4 Graph transforms")]
CANON = [b for b in re.findall(r"```text\n(.*?)\n```", s3, re.S)
         if not b.startswith(("ends with the `?", "texts checked", "source of each new text", r"\b(?:launch"))]
CANON += list(json.loads(re.findall(r"```json\n(.*?)\n```", s3, re.S)[0]).values())
DRP = REPO + "/docs/prompt_ecosystem_management/gcfpe.decision-record.md"
dr = open(DRP, encoding="utf-8").read()
_H = "### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)"
_sec = dr[dr.index(_H) + len(_H):]
_sec = _sec[:min(i for i in (_sec.find("\n### "), _sec.find("\n## ")) if i >= 0)]
_q = [l[2:].strip() for l in _sec.split("\n") if l.startswith("> ")]
assert len(_q) == 2, _q
ONCE = " ".join(_q)
CANON.append(ONCE)
C = {name: next(b for b in CANON if b.startswith(p)) for name, p in [
    ("C-ART", "Before emitting any handoff"), ("C-HANDOFF", "The block names the exact destination"),
    ("C-PLACE", "The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything"),
    ("C-LAT", "**Material** means"), ("C-SESSION", "PR-30 and PR-35 are two phases"),
    ("C-DISPATCH", "At `MERGE_PENDING`"), ("C-REPLAN", "**PRECISE IN-SCOPE DEFECT"),
    ("W-4", "PR-40 is entered on the observed merge event"), ("C-TOP", "This prompt runs in a top-level session")]}
CLAT_MATERIAL, CLAT_DECIDE = C["C-LAT"].split("\n\n", 1)
assert CLAT_DECIDE.startswith("**Decide it during work:**")
W4 = C["W-4"]
out["inputs"]["canonical_texts"] = len(CANON)
out["inputs"]["spec_v2_sha256"] = sha(SPEC)
out["inputs"]["decision_record_sha256"] = sha(DRP)
out["inputs"]["once_per_merge_read"] = ONCE.startswith("PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff")

# ---- authored texts -----------------------------------------------------------------------------------
PLAN = json.load(open(SCR.rsplit("/plan", 1)[0] + "/plan_result.json", encoding="utf-8"))
ENG = SCR + "/r1/engine"
LOC = json.load(open(ENG + "/locals.json", encoding="utf-8"))
out["inputs"]["plan_result_sha256"] = sha(SCR.rsplit("/plan", 1)[0] + "/plan_result.json")
out["inputs"]["r1_engine_locals_sha256"] = sha(ENG + "/locals.json")
out["inputs"]["r1_engine_rules_sha256"] = sha(ENG + "/closeout_rules.py")
out["inputs"]["decisions_sha256"] = sha(SCR + "/r1/DECISIONS.md")
eng_src = open(ENG + "/closeout_rules.py", encoding="utf-8").read()
sys.path.insert(0, ENG)
import closeout_rules as ER  # noqa: E402  (the r1 engine; importing runs no edit)
ns = vars(ER)
ENG_AUTH = {k: ns[k] for k in ("OWN", "RECV", "A5_NEW", "A5_MGMT", "A10_NEW", "P1_NEW", "P4_NEW", "TASK_NEW", "CLOSE_NEW",
                                "A2E_NEW", "ITEM21_NEW", "ITEM31_NEW", "ITEM18_NEW", "ITEM19_NEW", "ITEM34_NEW", "ITEM35_NEW",
                                "ITEM30D1_NEW", "ITEM30D2_NEW")}
assert ENG_AUTH["OWN"] == G.OWN_TEXT and ENG_AUTH["RECV"] == G.RECV_TEXT and ENG_AUTH["A5_MGMT"] == G.A5_MGMT
DECISIONS_TEXTS = {
    "P-01": G.RECV_TEXT, "P-02": G.OWN_TEXT, "P-03": G.QA10_ROLE_NEW,
    "P-04": G.A5_MGMT,
    "P-14": ", routed as *Required result and routing* states",
    "P-32": ("When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or "
             "review session, the block comes last and the named state is the line immediately before it. Nothing "
             "follows the block."),
}
dtext = open(SCR + "/r1/DECISIONS.md", encoding="utf-8").read()
out["inputs"]["decisions_literals_found_verbatim"] = {k: (v.strip(", ") in dtext) for k, v in DECISIONS_TEXTS.items()}
AUTH = []  # (source, text)
AUTH += [("DECISIONS " + k, v) for k, v in DECISIONS_TEXTS.items()]
AUTH += [("plan_result rule " + r["rule_id"], r["new_text"]) for r in PLAN["canon"]["rules"] if r.get("new_text")]
AUTH += [(f"plan_result local {b['prompt_id']} L{i + 1}", e["new_text"]) for g in PLAN["bodies"] for b in g["bodies"]
         for i, e in enumerate(b["local_edits"]) if e.get("new_text")]
AUTH += [("r1 engine " + k, v) for k, v in ENG_AUTH.items()]
AUTH += [("r1 local " + e["id"], e["new_text"]) for pid, es in LOC.items() for e in es if e.get("new_text")]
out["inputs"]["authored_texts"] = len(AUTH)

# ---- per-rule cases: rows, after-texts, injections (each injection at most 15 words) ------------------
PRED = "only where no `MERGE_OBSERVED` result was returned for this merge"
OWN_S = " " + G.OWN_TEXT
RECV_S = G.RECV_TEXT
URL = "https://app.notion.com/p/0123456789abcdef0123456789abcdef"
LX = {e["id"]: e for es in LOC.values() for e in es}
FRAME_AFTER = {
    "CF-C-10": "The recovery package names CLASS_SELECTION_REF, SOURCE_REF and the BLOCKED kickoff artifact by repository path; the artifacts hold the rest.",
    "CF-C-20": "The direct package names the pending Specification and the kickoff artifact by repository path; the artifacts hold the rest.",
    "CF-C-30": "The approval handoff names the approved Specification and its review by repository path; the artifacts hold the rest.",
    "CF-C-40": "The handoff names the Specification and the class selection artifact by repository path; the artifacts hold the rest.",
    "CL-20": "Continue to CL-30 naming the closure record by repository path; the artifacts hold the rest.",
    "CL-30": LX["LCL-30-1"]["new_text"],
    "CL-C-10": "Name the exact Specification and closure candidate by repository path; the artifacts hold the rest. Each runnable direct-native package names its destination, receiving role and session, and input artifacts by repository path.",
    "OPS-10": "The execution result names OPS_TASK and its receipt; " + LX["LOPS-10-1"]["new_text"] + ".",
    "PR-10": LX["LPR-10-1"]["new_text"] + "\n" + LX["LPR-10-4"]["new_text"],
    "PR-20": "\n".join(LX[i]["new_text"] for i in ("LPR-20-6", "LPR-20-7", "LPR-20-8")),
    "PR-40": "\n".join(LX[i]["new_text"] for i in ("LPR-40-1", "LPR-40-2", "LPR-40-3")),
}
for a, b in (("CF-E-10", "CF-C-10"), ("CF-E-20", "CF-C-20"), ("CF-E-30", "CF-C-30"), ("CF-E-40", "CF-C-40"), ("CL-E-10", "CL-C-10")):
    FRAME_AFTER[a] = FRAME_AFTER[b]
FRAME_INJ = {"cls_rec": "the recovery package carries the original CLASS_SELECTION_REF and SOURCE_REF",
             "unres": "UNRESOLVED_CLASSIFICATION_CASE with the preserved source/change facts",
             "direct_spec": "The direct package contains the exact pending Specification, class/change lineage",
             "kick_rec": "recovery carries the original kickoff link, exact defect, class/change lineage",
             "appr_reg": "review and approval lineage, the carried conflict register",
             "mode": "actual mode, class/change/base lineage",
             "qual": "carrying the exact qualified condition, lineage, evidence, owner, gates",
             "cand": "Carry the complete candidate, positive closure and architecture-decision lineage",
             "spec": "Carry exact Epic Specification, closure candidate and approval lineage",
             "runnable": "Each runnable direct-native package states its destination, lineage and evidence",
             "ops_ret": "must preserve in its execution result and return handoff",
             "pri": "carry PR_INSTRUCTION_ID and its complete content",
             "dep_ev": "dependency and evidence history; read-only substantiation of the mismatch; completed work",  # P-06
             "dep_ev2": "dependency/evidence history, completed work and unaffected obligations",
             "merge_ev": "all actual merge/commit/order/check evidence",
             "stage": "current stage and suspended boundary, completed work, dependencies, evidence",
             "accept": "PR instruction and implementation result; actual merged-state evidence",
             "dep_acc": "dependency, acceptance and evidence history; completed work",
             "review_work": "all completed review work; attempts; limitations"}
RECV_AFTER = {"PR-35": LX["LPR-35-1"]["new_text"] + LX["LPR-35-2"]["new_text"],
              "PR-40": "- " + G.PR40_INPUT_NEW + "." + LX["LPR-40-5"]["new_text"],
              "RS-20": LX["LRS-20-1"]["new_text"],
              "RS-40": LX["LRS-40-1"]["new_text"]}
RECV_INJ = {"PR-35": "open PR, tests, reviews/checks already observed, unresolved items",
            "PR-40": "PR_REFS, with each actual PR reference, commit identity, order",
            "RS-20": "Carry original Proceed, dedicated PR session, workspace/worktree, branch, open PR/head",
            "RS-40": "branch, pull request, and current head; completed work, commits/local changes"}
OWN_ANCHOR = {"PR-40": "You are the designated PR reviewer for the complete work unit, operating read-only.",
              "CL-E-20": "You are the explicitly assigned Lead Developer revalidation session, read-only.",
              "DOC-20": "Acting read-only, do not edit documentation, Canon, PF10, or repository state.",
              "ESC-25": "You are the explicitly named read-only repository reviewer or authorized environment operator.",
              "QA-10": "This is a read-only audit and readiness role.",
              "PR-20": "Do not mutate the repository in this authoring operation.",
              "PR-50": "Recover without otherwise mutating the workspace, worktree, branch, open PR, commits or evidence.",
              "GCFPE-MGMT-10": "It does not execute product Change Flow, implementation, repository work or releases.",
              "CL-20": "Use only the read-only tools, stores, repository access and environment permissions actually supplied.",
              "CL-30": "Use only the read-only tools, stores, repository access and environment permissions actually supplied.",
              "CL-40": "It does not edit Canonical PF09, PF10, Canon, a board, registry, repository or product state."}
OWN_AFTER = {r: a + OWN_S for r, a in OWN_ANCHOR.items()}
OWN_AFTER["QA-10"] = G.QA10_ROLE_NEW + OWN_S                                         # P-03 after R-OWN
A7_W4O = W4 + " " + ONCE
A7L_AFTER = {"PR-10": LX["LPR-10-3"]["new_text"] + " review it.",
             "PR-20": LX["LPR-20-4"]["new_text"] + ".\n" + LX["LPR-20-5"]["new_text"],
             "PR-40": LX["LPR-40-6"]["new_text"] + ", not a review verdict.\n" + LX["LPR-40-7"]["new_text"],
             "DOC-10": LX["LDOC-10-1"]["new_text"],
             "DOC-20": LX["LDOC-20-1"]["new_text"] + "\n" + LX["LDOC-20-2"]["new_text"] + " continue to `PR-40",
             "RS-40": LX["LRS-40-2"]["new_text"] + " the block directs `PR-40`."}
A7L_INJ = {"PR-10": ["only after Nathan asserts it occurred may PR-40 review it"],
           "PR-20": ["Nathan invokes PR-40 asserting that manual merge occurred",
                     "Nathan's PR-40 invocation asserts that the identified PR was manually merged;"],
           "PR-40": ["Nathan's invocation supplies only the later manual-merge assertion and review authorization",
                     "historical PR-35 `MERGE_PENDING` result, Nathan's later manual-merge assertion,"],
           "DOC-10": ["Nathan manual merge, PR-40 read-only landed-lineage review"],
           "DOC-20": ["separately from Nathan's later merge assertion and PR-40's independent landed-lineage evidence",
                      "landed-lineage review needed after Nathan's assertion: continue to `PR-40"],
           "RS-40": ["states that Nathan's later invocation asserts the manual merge,"]}
SITE_ONLY = {"RS-40 LRS-40-2": "Return one conditional block for use only after Nathan manually merges the identified PR;"}
ITEM34_BODY = "4. Decide `ESCALATION_REQUIRED` when a behavior defect needs code/Ops remediation."
ITEM34_AFTER_P15 = ITEM34_BODY + ENG_AUTH["ITEM34_NEW"] + " Do not fix it here."  # DECISIONS P-15 (insert between)
ITEM34_AFTER_REV = ITEM34_BODY + " Do not fix it here." + ENG_AUTH["ITEM34_NEW"]                             # engine 'P-15 rev.'
CL30_BEFORE = "full change/class/decision lineage; existing ADR/conflict history; classifications; actual review status"
CL30_AFTER = CL30_BEFORE.replace("; existing ADR/conflict history;", LX["LCL-30-2"]["new_text"])

A2G_INJ_BASE = ["Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING; CANON_CONFLICT_REGISTER; storage state.",
                "Required native inputs:\n- the approved Plan\n- CANON_CONFLICT_REGISTER and approved/rejected history",
                "send PLAN_PENDING to IA-20 carrying the conflict register",
                "Complete native inputs: exact finding; CANON_CONFLICT_REGISTER",                        # P-17 'Complete '
                "Complete RS-30 package:\n- recovery, CANON_CONFLICT_REGISTER, Product Owner/manual prerequisites",  # P-17
                "Complete RS-10 package: GCF-17.RESCOPE; CANON_CONFLICT_REGISTER"]
A2G_INJ_OPS = ["Complete return to ESC-30: ORIGINATING_FINDING_REF, CANON_CONFLICT_REGISTER, all evidence.",
               "RS-30 native revision: RESCOPE_REVIEW_ID, CANON_CONFLICT_REGISTER and manual prerequisites."]
A1C_ROWS = ["CL-C-10", "CL-E-10", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30",
            "ESC-40", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10", "QA-100", "QA-110",
            "QA-120", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30"]
CASES = [
 # rule, rows, after (str or {row: str}), injections (list or {row: [..]})
 ("R-A1a", G.A1A, "preserve complete usage and task/result/attempt mappings in the output artifact's permitted metadata, label repository persistence pending.",
  ["preserve complete usage and task/result/attempt mappings in permitted metadata or handoff"]),
 ("R-A1b", G.A1B, "preserve complete usage and task/result/attempt mappings in the output artifact's existing permitted metadata.",
  ["mappings in the existing permitted metadata or handoff", "mappings in existing permitted metadata or the handoff"]),
 ("R-A1c", A1C_ROWS, "Add a compact GCFPE_PROMPT_USES entry to permitted artifact lineage metadata: usage ID.",
  ["entry to permitted artifact lineage metadata or the returned handoff: usage ID",
   "existing artifact's permitted lineage metadata or returned handoff.", "existing permitted artifact lineage or the handoff."]),
 ("R-A1d", ["CL-C-10", "CL-E-10", "OPS-10", "OPS-30", "PR-10", "PR-20", "QA-10"],
  "Populate result artifact/PR/commit references after they actually exist, in the output artifact's lineage metadata or later authorized record.",
  ["references after they actually exist, in the returned handoff or later authorized record."]),
 ("R-A1e", ["CL-20", "CL-30", "CL-C-10", "CL-E-10", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-40", "QA-10"],
  "Keep the runtime requirement-to-source mapping and exact resolved evidence in the existing permitted artifact metadata.",
  ["exact resolved evidence in the existing permitted artifact metadata or handoff."]),
 ("R-A1f", ["PR-35"], "Record exact GCFPE prompt-use provenance in permitted artifact metadata.",
  ["Record exact GCFPE prompt-use provenance in permitted artifact/handoff metadata."]),
 ("R-A2a", G.A2A, "Preserve one `CANON_CONFLICT_REGISTER` in the existing substantive artifact, which the handoff names, within this actor's permitted output.",
  ["Preserve one `CANON_CONFLICT_REGISTER` in the existing substantive artifact and handoff"]),
 ("R-A2b", G.A2B, "Preserve one CANON_CONFLICT_REGISTER in existing applicable substantive artifact metadata/content, which the handoff names.",
  ["Preserve one CANON_CONFLICT_REGISTER in existing applicable substantive artifact metadata/content and handoffs."]),
 ("R-A2c", ["OPS-10"], "Preserve one CANON_CONFLICT_REGISTER in applicable task, receipt and review metadata, which the handoff names.",
  ["Preserve one CANON_CONFLICT_REGISTER in applicable task, receipt, review and handoff metadata."]),
 ("R-A2d", ["OPS-20"], "Preserve one `CANON_CONFLICT_REGISTER` in the task, execution result and receipt, which the handoff names, when applicable.",
  ["in the task, execution result, receipt and handoff when applicable."]),
 ("R-A2e", G.A2E, ENG_AUTH["A2E_NEW"] + ".",
  ["Carry exact register lineage, publication evidence and unresolved facts through all next/recovery packages.",
   "unresolved facts through every next and recovery package."]),
 ("R-A2f1", ["PR-40"], "Carry one CANON_CONFLICT_REGISTER through the instruction, Plan and review result without deciding Canon; every native return names those artifacts.",
  ["ordered PR lineage, review result and every native return without deciding Canon."]),
 ("R-A2f2", ["QA-10"], "Carry `CANON_CONFLICT_REGISTER` through the `REALITY_AUDIT`, `CHANGE_AUDIT_TRIAGE` and `QA_READINESS`; every return package names those artifacts.",
  ["`CHANGE_AUDIT_TRIAGE`, `QA_READINESS` and every return package."]),
 ("R-A2g", G.A2G, "Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING; storage state.\n"
  + LX["LOPS-10-2"]["new_text"] + ".", {r: A2G_INJ_BASE + (A2G_INJ_OPS if r in ("OPS-10", "OPS-20") else []) for r in G.A2G}),
 ("R-26-P1", G.P1, ENG_AUTH["P1_NEW"],
  ["current status and lineage; decisions already made; constraints and manual prerequisites",
   "Carry complete native inputs rather than referring to prior chat."]),
 ("R-26-P1b", ["IA-30", "UTIL-10"], "Return exactly one fenced `text` block beginning `NEXT_PROMPT_HANDOFF`.",
  ["naming the result, unresolved items/owners, next action, and expected output.",
   "unresolved items/owners, next action, and expected review state."]),
 ("R-26-P3", G.P3, "carries the exact PF10/addendum lineage into its result artifact, which the handoff names.",
  ["carries the exact PF10/addendum lineage into its result and handoff."]),
 ("R-26-P4", G.P4, ENG_AUTH["P4_NEW"],
  ["Catalogs and runtime handoffs carry the verified direct Notion links and repository paths"]),
 ("R-26-TASK", ["OPS-30", "QA-10"], ENG_AUTH["TASK_NEW"], ["native inputs, lineage, current state, gates, risks and required action."]),
 ("R-26-CLOSE", ["CL-20", "CL-30"], ENG_AUTH["CLOSE_NEW"],
  ["Carry the positive closure decision, complete post-closure results, unresolved observations"]),
 ("R-26-FRAME", list(G.FRAME_ROWS), FRAME_AFTER, {r: [FRAME_INJ[k] for k in ks] for r, ks in G.FRAME_ROWS.items()}),
 ("R-26-BRANCH-SEND", ["PR-10", "PR-20", "PR-30"],
  "PR-30 hands off naming `PR_IMPLEMENTATION_RESULT` by repository path and the pull request reference; the artifacts hold the rest.",
  ["PR-30 then hands the workspace/worktree, branch, open PR, current head, commit",
   "Carry the exact dedicated session, open PR, current head", "commit and remote-head references; completed work",
   "branch and repository/reference baseline"]),
 ("R-26-BRANCH-RECV", ["PR-35", "PR-40", "RS-20", "RS-40"], RECV_AFTER, {r: [v] for r, v in RECV_INJ.items()}),
 ("R-A7-S1a", G.A7S1, "Its conditional PR-40 handoff is usable only after Nathan later manually merges the identified PR and " + PRED + ".",
  ["Its conditional PR-40 handoff is usable only after Nathan later manually merges the identified PR."]),
 ("R-A7-S1b", G.A7S1, "That earlier `MERGE_PENDING` remains historical pre-merge evidence. " + A7_W4O +
  " PR-40 independently verifies actual merged state and landed attribution.",
  ["historical pre-merge evidence; Nathan's later invocation asserts a merge occurred;"]),
 ("R-A7-S2", G.A7S1, W4 + " PR-40 independently verifies actual merged state and landed lineage.",
  ["Nathan's later PR-40 invocation asserts that a manual merge occurred;",
   "Nathan's PR-40 invocation asserts the manual-merge event, while"]),
 ("R-A7-CL", G.A7CL, A7_W4O + " PR-40 independently verifies actual merged state and landed lineage.",
  ["Nathan's later manual PR-40 invocation asserts only that he manually merged the identified PR;"]),
 ("R-A7-S3", G.A7S3, "Nathan performs the manual merge. " + A7_W4O + " PR-40 independently verifies the merged state and landed lineage.",
  ["Nathan performs the manual merge. PR-40 independently verifies the later asserted merge and landed lineage."]),
 ("R-A7-LOCAL", G.A7LOCAL, A7L_AFTER, A7L_INJ),
 ("R-ITEM21", ["CL-20", "CL-30", "CL-C-10", "CL-E-10"], ENG_AUTH["ITEM21_NEW"] + " and supplies no review verdict.",
  ["The specific Product Owner PR-40 merge-approval effect is defined above"]),
 ("R-ITEM30a", ["PR-35"], "- `MERGE_PENDING`: every readiness predicate above passes.\n- `MERGE_OBSERVED`: "
  "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan.",
  ["- `MERGE_PENDING`: every readiness predicate above passes."]),
 ("R-ITEM30b", ["RS-40"], "- `MERGE_PENDING`: recorded PR-35 phase result.\n- `MERGE_OBSERVED`: resumed PR-35 "
  "phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan.",
  ["- `MERGE_PENDING`: recorded PR-35 phase result."]),
 ("R-ITEM30c", ["PR-35"], "A source-resolution failure does not become a seventh top-level PR-35 result.",
  ["A source-resolution failure does not become a sixth top-level PR-35 result"]),
 ("R-ITEM30d", ["PR-35"], "The PR-40 block is conditionally usable only after Nathan's manual merge" + ENG_AUTH["ITEM30D1_NEW"]
  + ". " + ENG_AUTH["ITEM30D2_NEW"],
  ["The PR-40 handoff must say: use it only after Nathan manually merges", "Nathan's later paste asserts that manual merge occurred;"]),
 ("R-ITEM31", ["PR-40"], ENG_AUTH["ITEM31_NEW"], ["An ordinary in-scope defect remains with the existing PR owner."]),
 ("R-OWN", G.OWN11, OWN_AFTER, {r: [a] for r, a in OWN_ANCHOR.items()}),
 ("R-A10", ["OPS-10", "OPS-30", "PR-40", "QA-10"], ENG_AUTH["A10_NEW"] + " and acceptance requires substantive evidence.",
  ["Reviewers remain read-only and acceptance requires substantive evidence."]),
 ("R-A5", G.A5, {"GCFPE-MGMT-10": G.A5_MGMT + ", and `docs/pfcanon/` is read-only.",
                 "PR-35": G.A5_NEW + ", and `docs/pfcanon/` is read-only."},
  ["Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written, and `docs/pfcanon/` is read-only."]),
 ("R-A3a", G.A3A, "Resolve the current authoritative subject-matter sources.",
  ["Embed only applicable workflow contracts: actor ownership, sequence, permitted actions, lineage, recovery and handoff."]),
 ("R-A4a", G.A4A, "Use only the binding for the actual result branch.",
  ["These candidate URL tokens must be replaced by observed direct Notion URLs."]),
 ("R-A4c", ["CL-40"], "This narrow exception grants no Canon, board, registry, repository, PR, or development mutation.",
  ["This authoring candidate does not perform that update."]),
 ("R-ITEM18", ["CL-40"], ENG_AUTH["ITEM18_NEW"].replace("{{CANDIDATE_CRD_LIST_URL}}", URL).strip(),
  ["Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`), which a destination rule names."]),
 ("R-ITEM19", ["CL-20"], "4. Include Master Scrum's precise board-update instruction for the board." + ENG_AUTH["ITEM19_NEW"],
  ["4. Include Master Scrum's precise board-update instruction for the board."]),
 ("R-ITEM34", ["QA-110"], ITEM34_AFTER_REV, [ITEM34_BODY + " Do not fix it here."]),
 ("R-ITEM35", ["QA-80"], "If the target is already approved, return `WRONG_ROUTE_APPROVED_BASE`" + ENG_AUTH["ITEM35_NEW"] + ".",
  ["If the target is already approved, return `WRONG_ROUTE_APPROVED_BASE` terminally"]),
 ("R-CLAT", G.CLAT8, "Use this branch only for a substantiated genuine boundary.", ["**Decide it during work:**"]),
 ("R-A2-CL30 (LCL-30-2, P-18)", ["CL-30"], CL30_AFTER, [CL30_BEFORE]),
 ("R-26-RSP (P-38)", ["PR-40"], "RESCOPE_PROPOSAL_ID, naming the RESCOPE_PROPOSAL by repository path; exact PR_WORK_UNIT_LINEAGE_REVIEW finding",
  ["RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL; exact PR_WORK_UNIT_LINEAGE_REVIEW finding"]),
 ("LOPS-30-1, LQA-10-P19 (P-19, P-42)", ["OPS-30", "QA-10"], "Before final output, check the actual result branch.",
  ["A saved attachment, link or scattered fields do not replace the handoff."]),
]
_rsp = [r for r in ER.RULES if r[0] == "R-26-RSP"][0]
assert _rsp[1] == G.RSP_FORBID and "RESCOPE_PROPOSAL_ID, naming the RESCOPE_PROPOSAL by repository path" == _rsp[3]

# which guards belong to which rule
RULE_GUARDS = {}
for gid, rules, part, kind, value, rid, sel in G.GUARDS:
    for r in rules:
        RULE_GUARDS.setdefault(r, []).append(gid)
GBY = {g[0]: g for g in G.GUARDS}
ACTIVE = [g for g in G.GUARDS if g[4] != G.TBD]


def gval(gid, row):
    v = GBY[gid][4]
    return v[row] if isinstance(v, dict) else v


def grows(gid):
    sel = GBY[gid][6]
    return KEYS if sel == G.ALL55 else list(sel)


def on_row(gid, row):
    v = GBY[gid][4]
    return v != G.TBD and row in grows(gid) and (not isinstance(v, dict) or row in v)


def pick(x, row):
    return x[row] if isinstance(x, dict) else x


def injs_of(inj, row):
    return (inj.get(row, []) if isinstance(inj, dict) else inj)


# ---- T1 --------------------------------------------------------------------------------------------
bad = []
for r in new["prompts"]:
    for l in ("required_regex", "forbidden_regex"):
        for x in r["audit_assertions"].get(l) or []:
            try:
                re.compile(val(x), re.M)
            except re.error as e:
                bad.append((r["prompt_key"], val(x)[:60], str(e)))
for p in (G.CL30_A2_CANDIDATE, G.RELEASE_ALL):
    re.compile(p, re.M)
out["T1_regex_compile_failures"] = bad
out["T1_python"] = sys.version.split()[0]

# ---- T2 --------------------------------------------------------------------------------------------
t2, t2_runs = [], 0
for rule, rows, after, inj in CASES:
    for row in rows:
        a = pick(after, row)
        for gid in RULE_GUARDS.get(rule, []):
            if not on_row(gid, row):
                continue
            kind, p = GBY[gid][3], gval(gid, row)
            t2_runs += 1
            if kind == "forbidden_regex":
                if re.search(p, a, re.M):
                    t2.append((rule, row, "G-" + gid, "forbidden fires on after-text"))
            else:
                if not re.search(p, a, re.M):
                    t2.append((rule, row, "G-" + gid, "required absent from after-text"))
                elif re.search(p, re.sub(p, "", a, flags=re.M), re.M):
                    t2.append((rule, row, "G-" + gid, "required still matches after its match is removed"))
        for s in injs_of(inj, row):
            fired = []
            for gid in RULE_GUARDS.get(rule, []):
                if not on_row(gid, row):
                    continue
                kind, p = GBY[gid][3], gval(gid, row)
                if kind == "forbidden_regex" and re.search(p, s, re.M):
                    fired.append(gid)
                if kind == "required_regex" and not re.search(p, s, re.M):
                    fired.append(gid + "(req)")
            if not fired:
                t2.append((rule, row, "injection not caught", s[:70]))
out["T2_checks_run"] = t2_runs
out["T2_failures"] = t2

# ---- T3: new/changed forbidden guards vs canonical and authored texts -------------------------------
new_forb = [("G-" + gid, v) for gid, _, _, kind, value, _, _ in ACTIVE if kind == "forbidden_regex"
            for v in sorted(set(value.values() if isinstance(value, dict) else [value]))]
new_forb += [("PART-17:" + lab, G.NEW_HDR + lab + G.NEW_END) for lab, _ in G.RELEASE_LABELS]
new_forb += [("G-K52 candidate", G.CL30_A2_CANDIDATE)]
t3_canon, t3_auth = [], []
for gid, p in new_forb:
    for c in CANON:
        if re.search(p, c, re.M):
            t3_canon.append((gid, c[:50]))
    for src, a in AUTH:
        if re.search(p, a, re.M):
            t3_auth.append((gid, src, a[:60]))
INTENDED = {("G-K51", "canonical C-LAT"): "the D23-C successor removes C-LAT's decide block from the 8 rows",
            ("G-K44", "{{CANDIDATE_CRD_LIST_URL}}"): "R-ITEM18's new text carries the placeholder until EXECUTE fills the URL"}
out["T3_new_forbidden_on_canonical"] = t3_canon
out["T3_new_forbidden_on_authored"] = t3_auth
out["T3_texts"] = {"canonical": len(CANON), "authored": len(AUTH), "patterns": len(new_forb)}
t3_unexpected = [x for x in t3_canon if not (x[0] == "G-K51" and C["C-LAT"].startswith(x[1]))]
t3_unexpected += [x for x in t3_auth if not (x[0] == "G-K44" and "{{CANDIDATE_CRD_LIST_URL}}" in dict(AUTH).get(x[1], "") )]
t3_unexpected = [x for x in t3_unexpected if not (x[0] == "G-K44" and "CANDIDATE_CRD_LIST_URL" in x[-1])]
out["T3_unexpected_hits"] = t3_unexpected

# ---- T4: per-row synthetic documents (P-12) --------------------------------------------------------
CANON_BLOCK = "\n\n".join(CANON)
CANON_BLOCK_CLAT8 = CANON_BLOCK.replace(C["C-LAT"], CLAT_MATERIAL)
docs = {k: [] for k in KEYS}
for rule, rows, after, inj in CASES:
    for row in rows:
        docs[row].append((rule, pick(after, row), injs_of(inj, row)))
new_req = [(gid, row) for gid, _, _, kind, _, _, _ in ACTIVE if kind == "required_regex" for row in grows(gid) if on_row(gid, row)]
new_forb_row = lambda row: [(gid, gval(gid, row)) for gid, _, _, kind, _, _, _ in ACTIVE if kind == "forbidden_regex" and on_row(gid, row)]
t4_req, t4_forb, t4_reg, t4_old_forb, runs = [], [], [], [], 0
for row in KEYS:
    base = CANON_BLOCK_CLAT8 if row in G.CLAT8 else CANON_BLOCK
    parts = [a for _, a, _ in docs[row]]
    text = base + "\n\n" + "\n\n".join(parts)
    aa = ROWS[row]["audit_assertions"]
    for gid, r2 in new_req:
        if r2 == row and not re.search(gval(gid, row), text, re.M):
            t4_req.append((row, "G-" + gid))
    for gid, p in new_forb_row(row):
        if re.search(p, text, re.M) and not (gid == "K44" and False):
            t4_forb.append((row, "G-" + gid))
    for lab, _ in G.RELEASE_LABELS:
        if re.search(G.NEW_HDR + lab + G.NEW_END, text, re.M):
            t4_forb.append((row, "PART-17:" + lab))
    after_only = "\n\n".join(parts)
    for x in aa.get("forbidden_regex") or []:
        if re.search(val(x), after_only, re.M):
            t4_old_forb.append((row, val(x)[:60]))
    # regressions: swap each rule's injection in place of its after-text; the row must fail
    for i, (rule, a, injs) in enumerate(docs[row]):
        for s in injs:
            runs += 1
            t = base + "\n\n" + "\n\n".join((s if j == i else b) for j, b in enumerate(parts))
            fails = [val(x)[:40] for x in aa.get("forbidden_regex") or [] if re.search(val(x), t, re.M)]
            fails += ["REQ:" + val(x)[:40] for x in aa.get("required_regex") or []
                      if re.search(val(x), text, re.M) and not re.search(val(x), t, re.M)]
            if not fails:
                t4_reg.append((row, rule, s[:60]))
out["T4_rows_with_docs"] = sum(1 for k in KEYS if docs[k])
out["T4_required_unsatisfied"] = t4_req
out["T4_new_forbidden_hits_on_docs"] = t4_forb
out["T4_any_row_forbidden_on_after_texts"] = t4_old_forb
out["T4_case_regressions_run"] = runs
out["T4_case_regressions_not_caught"] = t4_reg

# ---- T8: REGRESSIONS (the registry spec's regression column) ----------------------------------------
def reg_rows(gid):
    r = G.REGRESSIONS[gid]
    return {row: (r.get(row) or r.get("*")) for row in grows(gid) if on_row(gid, row) or gid == "K52"}


def minimal(p, s):
    toks = s.split(" ")
    for n in range(1, len(toks)):
        for i in range(0, len(toks) - n + 1):
            w = " ".join(toks[i:i + n])
            if re.search(p, w, re.M):
                return w
    return s


t8, t8_runs, t8_words, t8_nonmin = [], 0, {}, []
for gid, _, _, kind, value, _, sel in G.GUARDS:
    if value == G.TBD:
        continue
    for row, s in reg_rows(gid).items():
        t8_runs += 1
        t8_words[f"G-{gid} {row}"] = words(s)
        p = gval(gid, row)
        base = CANON_BLOCK_CLAT8 if row in G.CLAT8 else CANON_BLOCK
        text = base + "\n\n" + "\n\n".join(a for _, a, _ in docs[row])
        if kind == "forbidden_regex":
            standalone = bool(re.search(p, s, re.M))
            appended = bool(re.search(p, text + "\n" + s + "\n", re.M))  # as dryrun.py injects
            if not (standalone and appended):
                t8.append((f"G-{gid}", row, "forbidden regression does not fire", standalone, appended))
            m = minimal(p, s)
            if m != s:
                t8_nonmin.append((f"G-{gid}", row, words(s), words(m), m))
        else:
            if re.search(p, s, re.M):
                t8.append((f"G-{gid}", row, "required matches its own regression"))
            removed = re.sub(p, s.replace("\\", "\\\\"), text, flags=re.M)  # the retired wording put back in place
            if re.search(p, removed, re.M):
                t8.append((f"G-{gid}", row, "required still satisfied after the retired wording replaces the new text"))
for lab, rid in G.RELEASE_LABELS:
    s = G.RELEASE_INJ[lab]
    t8_words["PART-17 " + lab] = words(s)
    for row in KEYS:
        text = CANON_BLOCK + "\n\n" + "\n\n".join(a for _, a, _ in docs[row])
        if not re.search(G.NEW_HDR + lab + G.NEW_END, text + "\n" + s + "\n", re.M):
            t8.append(("PART-17 " + lab, row, "does not fire"))
    t8_runs += len(KEYS)
case_words = {f"{rule} {row}": words(s) for rule, rows, _, inj in CASES for row in rows for s in injs_of(inj, row)}
out["T8_regression_runs"] = t8_runs
out["T8_failures"] = t8
out["T8_max_words"] = {"REGRESSIONS": max(t8_words.values()), "CASES": max(case_words.values())}
out["T8_over_15_words"] = sorted([k for k, v in t8_words.items() if v > 15] + [k for k, v in case_words.items() if v > 15])
out["T8_forbidden_not_minimal"] = t8_nonmin
out["T8_body_anchor_quotes_over_15_words"] = [k for k, v in {**OWN_ANCHOR, "ITEM34_BODY": ITEM34_BODY}.items() if words(v) > 15]

# ---- T5: P-01 / P-02 sentences; G06 --------------------------------------------------------------------
G06 = next(val(x) for x in ROWS["CF-C-10"]["audit_assertions"]["forbidden_regex"]
           if val(x).startswith("(?<!\\bno )(?<!\\bno `)NEXT_PROMPT_HANDOFF"))
all_forb = sorted({val(x) for r in new["prompts"] for x in r["audit_assertions"].get("forbidden_regex") or []})
hits = {}
for name, s in (("P-01", G.RECV_TEXT), ("P-02", G.OWN_TEXT)):
    hits[name] = [p[:70] for p in all_forb if re.search(p, s, re.M)]
    for row, a in OWN_ANCHOR.items():  # P-02 placed after each row's own anchor: that row's G-K35 must be silent
        if name == "P-02" and row != "QA-10" and re.search(G.K35[row], a + " " + s, re.M):
            hits[name].append(f"G-K35 {row} after its anchor")
LEADS = ["The `NEXT_PROMPT_HANDOFF` block follows.\n", "Return exactly one fenced `text` block beginning `NEXT_PROMPT_HANDOFF`.\n",
         "NEXT_PROMPT_HANDOFF\n", "The `NEXT_PROMPT_HANDOFF` block names the destination. ", "- `NEXT_PROMPT_HANDOFF`: the block.\n"]
g06 = {}
for name, s in (("P-01", G.RECV_TEXT), ("P-02", G.OWN_TEXT), ("PR-40 input + P-01", "- " + G.PR40_INPUT_NEW + "." + LX["LPR-40-5"]["new_text"]),
                ("LPR-20-3", LX["LPR-20-3"]["new_text"]), ("LRS-20-1", LX["LRS-20-1"]["new_text"]),
                ("LRS-40-1", LX["LRS-40-1"]["new_text"]), ("LPR-35-1+2", LX["LPR-35-1"]["new_text"] + LX["LPR-35-2"]["new_text"])):
    g06[name] = [bool(re.search(G06, lead + s)) for lead in LEADS]
OLD_RECV = ("Branch, worktree, head and commit identity are verified at entry from the recorded vehicle and repository "
            "state; the handoff does not carry them.")
out["T5_forbidden_patterns_in_new_registry"] = len(all_forb)
out["T5_forbidden_hits_on_P01_P02"] = hits
out["T5_G06_hits_per_lead"] = g06
out["T5_G06_on_first_round_sentence (control, expected true)"] = [bool(re.search(G06, lead + OLD_RECV)) for lead in LEADS]
out["T5_G06_rows"] = sum(1 for r in new["prompts"] if any(val(x) == G06 for x in r["audit_assertions"].get("forbidden_regex") or []))
out["T5_G-K22_matches_P01"] = bool(re.search(G.BRECV_REQ, G.RECV_TEXT))
out["T5_G-K36_matches_P02"] = bool(re.search(G.OWN_REQ, G.OWN_TEXT))

# ---- T6: PART-17 (P-16) ----------------------------------------------------------------------------
pad = "\n".join(f"line {i} of the body." for i in range(12)) + "\n"
lines = {"**`Prompt version`**: x": True, "3. **`Set`**: x": True, "- Settings: x": False, "Set up the run:": False,
         "Prompt version: 1.2.0": True, "**Set:** x": True, "`Set`: x": True, "> **Ecosystem release**: x": True,
         "| Ecosystem release | x |": False, "The check rejects `Prompt version:` in a header.": False,
         "__Prompt Version__: x": True, "- **`Ecosystem release`**: x": True, "Settings: x": False, "Setup: x": False}
t6 = {}
for line, want in lines.items():
    got = {lab: bool(re.search(G.NEW_HDR + lab + G.NEW_END, pad + line + "\n", re.M)) for lab, _ in G.RELEASE_LABELS}
    first = {lab: bool(re.search(G.NEW_HDR + lab + G.OLD_END, pad + line + "\n", re.M)) for lab, _ in G.RELEASE_LABELS}
    union = any(got.values())
    t6[line] = {"expected": want, "new (P-16)": union, "first-round suffix": any(first.values()),
                "R-ITEM23 single pattern agrees": bool(re.search(G.RELEASE_ALL, pad + line + "\n", re.M)) == union,
                "old window guard": any(bool(re.search(G.OLD_HDR + lab + G.OLD_END, pad + line + "\n")) for lab, _ in G.RELEASE_LABELS)}
out["T6_release_lines"] = t6
out["T6_ok"] = all(v["expected"] == v["new (P-16)"] and v["R-ITEM23 single pattern agrees"] for v in t6.values())
out["T6_new_patterns_on_canonical"] = [c[:40] for c in CANON if re.search(G.RELEASE_ALL, c, re.M)]
out["T6_engine_RELEASE_equals_R-ITEM23_pattern"] = ns["RELEASE"] == G.RELEASE_ALL

# ---- T7: NAM-002 (prototype; the EXECUTE run uses nam002_live.py on the live child lists) -------------
idmap = {o: n for o, _, n, _, _, _ in G.PARENT_MAP}
children = {}
for r in old["prompts"]:
    children.setdefault(idmap[r["expected_parent_id"]], []).append({"id": r["notion_page_id"], "title": r["expected_title"]})
syn = {"captured_at": "SYNTHETIC (PLAN; parents from the ANALYZE mapping)", "hubs": [{"id": h, "children": c} for h, c in children.items()]}
res_new = N2.run(HERE + "/registry.new.md", syn, inject=None)
res_old = N2.run(HERE + "/registry.head.md", syn, inject=None)
res_inj = N2.run(HERE + "/registry.new.md", syn, inject=("ESC-10", "3db4590a05eb81d59059eb6b95ed5fcf"))
out["T7_NAM002"] = {"old registry": res_old["summary"], "new registry": res_new["summary"],
                    "new registry, ESC-10 parent injected wrong": res_inj["summary"]}
out["T7_ok"] = (res_old["summary"]["NAM-002"] == 55 and res_new["summary"]["NAM-002"] == 0
                and res_inj["summary"]["NAM-002_rows"] == ["ESC-10"] and res_new["summary"]["other_errors"] == 0)

# ---- T9: GUARD-001, anchor-level coverage of every r1 LOCAL edit (heuristic; the dry run is authoritative) ----
from altsplit import top_alts  # noqa: E402


def lit_tokens(p):
    x = re.sub(r"\(\?[:=!<]+|\(\?<[=!]|\\b|\[\^[^\]]*\]\*|[()?*+|^$]|\{\d+(?:,\d*)?\}", " ", p)
    x = x.replace("\\", "")
    return [t.strip(",;:.`'").lower() for t in x.split() if t.strip(",;:.`'")]


def overlap(a, b):
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best


t9 = []
for pid, es in LOC.items():
    if pid not in ROWS:
        for e in es:
            t9.append({"edit": e["id"], "row": pid, "kind": "not a registry row (PART-11 gate)", "guards": []})
        continue
    aa = ROWS[pid]["audit_assertions"]
    for e in es:
        at = [t.strip(",;:.`'").lower() for t in e["anchor"].split()]
        g = []
        if e["action"] in ("replace", "delete"):
            for x in aa.get("forbidden_regex") or []:
                p = val(x)
                if re.search(p, e["anchor"], re.M):
                    g.append(("fires on anchor", p[:50], not re.search(p, e["new_text"], re.M)))
                    continue
                for alt in top_alts(p[4:] if p.startswith("(?m)") else p):
                    if overlap(lit_tokens(alt), at) >= 4:
                        g.append(("overlaps anchor (>=4 words)", alt[:50], not re.search(p, e["new_text"], re.M)))
                        break
        for x in aa.get("required_regex") or []:
            p = val(x)
            if e["new_text"] and re.search(p, e["new_text"], re.M) and not re.search(p, e["anchor"], re.M):
                g.append(("required matches new_text", p[:50], True))
        t9.append({"edit": e["id"], "row": pid, "action": e["action"], "kind": "registry row", "guards": g,
                   "silent_after": all(s_ for _, _, s_ in g)})
out["T9_local_edits"] = len(t9)
out["T9_unguarded_heuristic"] = [(x["edit"], x["row"], x.get("action")) for x in t9 if x["kind"] == "registry row" and not x["guards"]]
out["T9_guard_not_silent_on_new_text"] = [(x["edit"], x["row"]) for x in t9 if x["guards"] and not x.get("silent_after", True)]
out["T9_detail"] = t9

# ---- T10: P-15 (revised) ------------------------------------------------------------------------------
SITE = r"code/Ops remediation\. Do not fix it here\.(?! This applies only before the whole approved run is complete)"
t10 = {}
before = ITEM34_BODY + " Do not fix it here."
for name, after in (("P-15 (revised): insert after 'Do not fix it here.' (engine)", ITEM34_AFTER_REV),
                    ("first P-15: insert between", ITEM34_AFTER_P15)):
    t10[name] = {"G-K47 fires before": bool(re.search(G.ITEM34_FORBID, before + "\n")),
                 "G-K47 silent after": not re.search(G.ITEM34_FORBID, after),
                 "G-K48 matches after": bool(re.search(G.ITEM34_REQ, after)),
                 "G-K47 fires when the new sentence is deleted": bool(re.search(G.ITEM34_FORBID, before + "\n"))}
t10["engine R-ITEM34 anchor"] = [x for x in eng_src.splitlines() if '"R-ITEM34"' in x][0].strip()[:120]
t10["engine anchor = P-15 (revised) placement"] = "(?<=code/Ops remediation\\. Do not fix it here\\.)" in eng_src
t10["G-K47 on a second, unrelated 'Do not fix it here.' line (fires: the pattern is not site-scoped)"] = bool(
    re.search(G.ITEM34_FORBID, ITEM34_AFTER_REV + "\n5. Report the defect. Do not fix it here.\n"))
t10["site-scoped variant"] = SITE
t10["site-scoped variant: fires before / silent after / silent on a second line"] = [
    bool(re.search(SITE, before + "\n")), not re.search(SITE, ITEM34_AFTER_REV),
    not re.search(SITE, ITEM34_AFTER_REV + "\n5. Report the defect. Do not fix it here.\n")]
out["T10_P15"] = t10

# ---- T11: P-18 candidate -----------------------------------------------------------------------------
out["T11_K52"] = {"pattern": G.CL30_A2_FORBID, "equals dry-run B candidate": G.CL30_A2_FORBID == G.CL30_A2_CANDIDATE, "fires on pre-edit clause": bool(re.search(G.CL30_A2_CANDIDATE, CL30_BEFORE)),
                            "silent after LCL-30-2": not re.search(G.CL30_A2_CANDIDATE, CL30_AFTER),
                            "regression words": words(G.REGRESSIONS["K52"]["*"]),
                            "regression fires": bool(re.search(G.CL30_A2_CANDIDATE, G.REGRESSIONS["K52"]["*"])),
                            "silent on CL-30 synthetic doc": not re.search(G.CL30_A2_CANDIDATE, CANON_BLOCK + "\n\n" + "\n\n".join(a for _, a, _ in docs["CL-30"]), re.M),
                            "hits on canonical/authored": [s for s, a in AUTH if re.search(G.CL30_A2_CANDIDATE, a)] + [c[:30] for c in CANON if re.search(G.CL30_A2_CANDIDATE, c)]}

# ---- T12: row_assertions.json read by the dry run's own load_guards(); each injection fires on each row --------
t12, t12_runs = [], 0
if os.path.exists(HERE + "/row_assertions.json"):
    import dryrun as DR  # noqa: E402  (plan/r1/engine/dryrun.py; importing runs no fetch)
    for g in DR.load_guards(HERE + "/row_assertions.json"):
        rows = KEYS if g["rows"] == "ALL" else [r for r in g["rows"] if r in ROWS]
        for row in rows:
            base = CANON_BLOCK_CLAT8 if row in G.CLAT8 else CANON_BLOCK
            doc = base + "\n\n" + "\n\n".join(a for _, a, _ in docs[row])
            t12_runs += 1
            if g["kind"] == "forbidden_regex":
                if re.search(g["pattern"], doc, re.M):
                    t12.append((g["id"], row, "fires on the synthetic after-document"))
                if g["inject"] is None or not re.search(g["pattern"], doc + "\n" + g["inject"] + "\n", re.M):
                    t12.append((g["id"], row, "injection does not fire"))
            else:
                if not re.search(g["pattern"], doc, re.M):
                    t12.append((g["id"], row, "required absent from the synthetic after-document"))
                elif re.search(g["pattern"], re.sub(g["pattern"], "", doc, flags=re.M), re.M):
                    t12.append((g["id"], row, "required survives removal"))
out["T12_dryrun_load_guards_runs"] = t12_runs
out["T12_failures"] = t12

# ---- T13: LOCAL phrases guarded only at site level ----------------------------------------------------
t13 = {}
for k_, s_ in SITE_ONLY.items():
    row_ = k_.split()[0]
    alone = [val(x)[:50] for x in ROWS[row_]["audit_assertions"].get("forbidden_regex") or [] if re.search(val(x), s_, re.M)]
    bullet = s_ + " the block directs `PR-40`, states that Nathan's later invocation asserts the manual merge,"
    with_sibling = [val(x)[:50] for x in ROWS[row_]["audit_assertions"].get("forbidden_regex") or [] if re.search(val(x), bullet, re.M)]
    t13[k_] = {"words": words(s_), "row guards firing on the phrase alone": alone, "row guards firing on the pre-edit bullet": with_sibling}
out["T13_site_level_only"] = t13

out["ALL_OK"] = (not out["T1_regex_compile_failures"] and not out["T2_failures"] and not out["T3_unexpected_hits"]
                 and not out["T4_required_unsatisfied"] and not out["T4_new_forbidden_hits_on_docs"]
                 and not out["T4_any_row_forbidden_on_after_texts"] and not out["T4_case_regressions_not_caught"]
                 and not out["T8_failures"] and not out["T8_over_15_words"] and not out["T8_body_anchor_quotes_over_15_words"]
                 and not any(out["T5_forbidden_hits_on_P01_P02"].values())
                 and not any(any(v) for v in out["T5_G06_hits_per_lead"].values())
                 and out["T5_G-K22_matches_P01"] and out["T5_G-K36_matches_P02"] and out["T6_ok"] and out["T7_ok"]
                 and out["inputs"]["once_per_merge_read"] and not out.get("T12_failures"))
json.dump(out, open(HERE + "/guard_tests.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in out.items() if k not in ("T9_detail",)}, indent=1, ensure_ascii=False))
