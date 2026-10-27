#!/usr/bin/env python3
"""Merge every design worker's package redlines into plan/package-redlines.json (MODIFICATION-20261027-gcfpe-backlog-open-items).

PLAN, A3. Reads plan/work/W1.json, W3a.json, W4.json, W5.json and W7.json (W2, W3b, W6 and W8 carry none) and applies
the coordinator's decisions (plan/coordinator-decisions.md) mechanically:

  C-3    W3a's two change-flow lines (SKILL.md :436 and :453) are IN; the governance-audit lines are OUT (they are not
         skill_redlines in any worker file; recorded under not_applied).
  C-13   R-P1 is a conditional set, EXCLUDED by default (Nathan's opt-in): its ops are under conditional_sets, never
         in `ops`, so package_apply.py does not apply them.
  W7-D2  the four packages: change-flow, flowmaster-validate, glow-hde-pr-development, glow-graph-contract.
  W7-D3  revisions: change-flow 3.5.0, flowmaster-validate 3.5.0, glow-hde-pr-development 1.5.0.
  W7-D4  W4's SR-3/SR-4 QA_PLAN_REVIEW birth value goes into EXPECTED_POLICY_20261027 (merged into W5's SR-CF-9 and
         SR-FV-20), and EXPECTED_POLICY is not edited.
  W7     SR-W7-FV-11 replaces W5's SR-FV-29 (same old text); SR-W7-* apply after every other op.
  W5     count-0 entries are new files (SR-CF-8, SR-FV-35, SR-FV-36: written by build_r1_successor_20261027.py and
         bundled by the package build); SR-FV-34's prose is made a concrete count-checked insertion here.

  make_package_redlines_102726.py            write plan/package-redlines.json
  make_package_redlines_102726.py --check    rebuild in memory; exit 1 unless the file on disk is byte-identical
  make_package_redlines_102726.py --selftest each injected defect in a worker input must be refused

No prompt body is read or written. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OUT = HERE / "package-redlines.json"
WORK = HERE / "work"
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract")
BASE_DIGESTS = {  # W7 tooling.packages_that_change freeze_digest_before; re-measured by A3, 2026-10-27
    "change-flow": "25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2",
    "flowmaster-validate": "37 45c7d5d743fbcdf2100fa74ba6b2ff06609c0f056b7cfdee93a5fd74750f716d",
    "glow-hde-pr-development": "4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0",
    "glow-graph-contract": "9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9",
}
NEW_FILE_IDS = {"SR-CF-8", "SR-FV-35", "SR-FV-36"}

# SR-FV-34 (W5): "ADD two scenarios beside positive_post_closure_adr_drainage". Made concrete: inserted immediately
# before positive_post_closure_pf09_drainage, in the file's own layout. The negative's rule is the one W5 names
# (validate_flowmaster.py's undeclared-transition finding, FMV-GCF-EDGE-003).
SR_FV_34_ANCHOR = '    {\n      "id": "positive_post_closure_pf09_drainage",'
SR_FV_34_INSERT = (
    '    {\n'
    '      "id": "positive_close_stage_do_not_close_return",\n'
    '      "expected_pass": true,\n'
    '      "expected_rule_ids": [],\n'
    '      "coverage_mode": "COMPLETE",\n'
    '      "events": [\n'
    '        {"row": "GCF-24"}, {"row": "GCF-24.CLOSE"}, {"row": "GCF-25"},\n'
    '        {"row": "GCF-24.CLOSE"}, {"row": "GCF-25"}, {"row": "GCF-26"}\n'
    '      ]\n'
    '    },\n'
    '    {\n'
    '      "id": "negative_qa_report_skips_close_stage",\n'
    '      "expected_pass": false,\n'
    '      "expected_rule_ids": ["FMV-GCF-EDGE-003"],\n'
    '      "coverage_mode": "COMPLETE",\n'
    '      "events": [{"row": "GCF-23"}, {"row": "GCF-24"}, {"row": "GCF-25"}]\n'
    '    },\n'
)

# R-P1 (C-13, W1-Q3): Nathan's opt-in only. Same stale drained-addendum citation as ITEM-33 (W1 PART-26's wording).
# change-flow SKILL.md line 10 is the dated MB-008 note, which stays as written (AUTH-001, SR-W7-CF-04's own reason);
# its R-P1 piece is therefore a sentence added to the 102726.1 note that SR-W7-CF-04 writes, not an edit of line 10.
R_P1_OPS = [
    {"id": "RP1-FV-01", "skill": "flowmaster-validate", "file": "SKILL.md",
     "old": "(HDE Build Notes; PF04 §9.1.3)", "new": "(PF04 §9.1.3, *GCFPE model and reasoning-level guidance*)",
     "count": 1, "why": "flowmaster-validate SKILL.md:168 (W1-Q3); ITEM-33's wording"},
    {"id": "RP1-FV-02", "skill": "flowmaster-validate", "file": "scripts/run_gcfpe_20261009_fixtures.py",
     "old": "# F07 (HDE Build Notes; PF04 §9.1.3)", "new": "# F07 (PF04 §9.1.3)",
     "count": 1, "why": "fixture comment run_gcfpe_20261009_fixtures.py:320 (W1-Q3); the derived 102726.1 runner inherits it"},
    {"id": "RP1-CF-01", "skill": "change-flow", "file": "SKILL.md",
     "old": "Under current HDE Build Notes, the model and reasoning-level guidance for each GCFPE downstream session",
     "new": "Under PF04 §9.1.3, the model and reasoning-level guidance for each GCFPE downstream session",
     "count": 1, "why": "change-flow SKILL.md:305 (W1-Q3): states as current a home that no longer holds the rule"},
    {"id": "RP1-CF-02", "skill": "change-flow", "file": "SKILL.md",
     "old": "and CL-05's result goes to the class-matching closure decision. Change-specific behaviour changes, so the revision moves to 3.5.0.",
     "new": "and CL-05's result goes to the class-matching closure decision. The TypeSafe rule that the MB-008 note places under HDE Build Notes is PF04 §9.1.3's since its drain. Change-specific behaviour changes, so the revision moves to 3.5.0.",
     "count": 1, "requires": ["SR-W7-CF-04"],
     "why": "change-flow line 10 (W1-Q3), placed in the successor note because the dated MB-008 note stays as written (AUTH-001)"},
]


# A3-C1 corrects SR-W7-FV-11's new text in place (one op, as SR-W7-FV-11 itself replaced SR-FV-29), so the op that lands
# is the corrected one and no later op rewrites an earlier op's result.
A3_C1_FV11_NEW = ('        "references/glow-hde-canonical-change-flow-r1-runtime-map-20261027.json",\n'
                  '        "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json",\n    },')
A3_C1_WHY = ("A3-C1: OPTIONAL_REFERENCES is the exact set of references change-flow SKILL.md links (validate_flowmaster.py: "
             "'optional bundled reference is not linked'). SR-CF-* and SR-W7-CF-02 move both links to the 2026-10-27 map and "
             "the 102726.1 contract, so the two superseded entries must leave the set, as MB-008 replaced its predecessor's; "
             "the files stay bundled as history, unlinked, like the 091426.1 contract. W7's text kept both.")


# A3 corrections, found by running the suite on the PLAN scratch build (A3 receipt). Each makes concrete a change a
# worker designed in prose, or corrects a worker op the suite refuses; each is the coordinator's to accept (C-numbered
# decision needed) and applies after W7's ops.
A3_CORRECTIONS = [
    {"id": "A3-C2", "part": "PART-13", "skill": "flowmaster-validate", "file": "scripts/validate_flowmaster.py",
     "source": "W5.json validator_changes_needed FMV-ORACLE-019 (prose; no redline in W5 skill_redlines)",
     "old": ('        ids = [row.get("id") for row in rows]\n'
             '        history_ids = [row.get("id") for row in history_rows]\n'
             '        position_findings = 0\n'),
     "new": ('        # PART-13 (MODIFICATION-20261027-gcfpe-backlog-open-items): an added successor row has no historical row;\n'
             '        # it must sit immediately after its anchor row, and every other row keeps its historical neighbours.\n'
             '        all_ids = [row.get("id") for row in rows]\n'
             '        ids = [row_id for row_id in all_ids if row_id not in SUCCESSOR_ADDED_ROWS]\n'
             '        history_ids = [row.get("id") for row in history_rows]\n'
             '        position_findings = 0\n'
             '        for added, anchor in SUCCESSOR_ADDED_ROWS.items():\n'
             '            if (added in history_ids or all_ids.count(added) != 1 or anchor not in all_ids\n'
             '                    or all_ids.index(added) != all_ids.index(anchor) + 1):\n'
             '                position_findings += 1\n'
             '                results.append(finding(\n'
             '                    "FMV-ORACLE-019", str(oracle_path),\n'
             '                    f"row={added}; an added successor row must occur once, immediately after {anchor}, "\n'
             '                    f"and have no historical row",\n'
             '                ))\n'),
     "count": 1,
     "why": "W5: 'Remove SUCCESSOR_ADDED_ROWS ids before comparing ids with history_ids and before computing neighbours; require each added row to sit immediately after its anchor row'. Without it the suite reports GCF-24 and GCF-25 as moved (A3 scratch run)."},
    {"id": "A3-C3", "part": "PART-13", "skill": "flowmaster-validate", "file": "scripts/validate_flowmaster.py",
     "source": "W5.json validator_changes_needed FMV-ORACLE-020 (prose; no redline in W5 skill_redlines)",
     "old": "            [EXPECTED_ORACLE_PROFILE if token == history_profile else token for token in history_tokens]\n",
     "new": ("            [EXPECTED_ORACLE_PROFILE if token == history_profile\n"
             "             else \"R1_ROW_COVERAGE: 47/47\" if token == \"R1_ROW_COVERAGE: 46/46\" else token\n"
             "             for token in history_tokens]\n"),
     "count": 1,
     "why": "W5: \"required_global_tokens: the historical list with the profile_id replaced in place and 'R1_ROW_COVERAGE: 46/46' replaced in place by 'R1_ROW_COVERAGE: 47/47'\". Without it the suite refuses the 2026-10-27 oracle (A3 scratch run)."},
    {"id": "A3-C4", "part": "PART-13", "skill": "flowmaster-validate", "file": "scripts/validate_flowmaster.py",
     "source": "message for A3-C3",
     "old": ('f"required_global_tokens must be the historical list with only the historical profile_id {history_profile} "\n'
             '                f"replaced in place by {EXPECTED_ORACLE_PROFILE}",\n'),
     "new": ('f"required_global_tokens must be the historical list with only the historical profile_id {history_profile} "\n'
             '                f"replaced in place by {EXPECTED_ORACLE_PROFILE} and the row coverage token by R1_ROW_COVERAGE: 47/47",\n'),
     "count": 1, "why": "the finding names what the check now requires"},
]


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_workers() -> dict:
    return {w: json.loads((WORK / f"{w}.json").read_text(encoding="utf-8")) for w in ("W1", "W3a", "W4", "W5", "W7")}


def op(id_, part, source, pkg, file, old, new, count, why) -> dict:
    if pkg not in PACKAGES:
        raise SystemExit(f"{id_}: package {pkg!r} is not one of the four (W7-D2)")
    if not isinstance(old, str) or not old or not isinstance(new, str) or old == new:
        raise SystemExit(f"{id_}: old must be non-empty and differ from new")
    if not isinstance(count, int) or count < 1:
        raise SystemExit(f"{id_}: count must be a positive integer")
    return {"id": id_, "part": part, "source": source, "skill": pkg, "file": file, "old": old, "new": new,
            "count": count, "why": why}


def merge(W: dict) -> dict:
    ops, not_applied, new_files = [], [], []
    # W1: skill redlines then validator redlines (no ids in the worker file; ids assigned in file order)
    for i, r in enumerate(W["W1"]["skill_redlines"], 1):
        ops.append(op(f"W1-SR-{i:02d}", r["part"], f"W1.json skill_redlines[{i - 1}]", r["package"], r["file"],
                      r["old"], r["new"], r["count"], r["why"]))
    for i, r in enumerate(W["W1"]["validator_redlines"], 1):
        ops.append(op(f"W1-VR-{i:02d}", r["part"], f"W1.json validator_redlines[{i - 1}]", r["package"], r["file"],
                      r["old"], r["new"], r["count"], r["why"]))
    # W3a: C-3 takes both change-flow lines (their `conditional` is resolved by C-3)
    w3a = W["W3a"]["skill_redlines"]
    if len(w3a) != 2 or any(r["package"] != "change-flow" for r in w3a):
        raise SystemExit("W3a: C-3 expects exactly the two change-flow lines")
    for i, r in enumerate(w3a, 1):
        ops.append(op(f"W3a-SR-{i:02d}", r["part"], f"W3a.json skill_redlines[{i - 1}]; C-3", r["package"], r["file"],
                      r["old"], r["new"], r["count"], "ITEM-08 (C-3: change-flow :436 and :453 ride PART-07)"))
    not_applied.append({"source": "W3a Q-2 amthor-workspace-governance-audit SKILL.md:61, "
                                  "references/interoperability-contracts.md:62", "disposition": "OUT (C-3)",
                        "reason": "that package is otherwise unchanged; backlog (C-14); Nathan may opt in"})
    # W4: SR-1, SR-2 as written; SR-3/SR-4 merged into SR-CF-9/SR-FV-20 (W7-D4)
    w4 = {r["id"]: r for r in W["W4"]["skill_redlines"]}
    if set(w4) != {"SR-1", "SR-2", "SR-3", "SR-4"}:
        raise SystemExit(f"W4: unexpected redline ids {sorted(w4)}")
    for k in ("SR-1", "SR-2"):
        r = w4[k]
        ops.append(op(f"W4-{k}", r["part"], f"W4.json {k}", r["package"], r["file"], r["old"], r["new"], r["count"],
                      "PART-10 (DN-5 (a))"))
    m = re.fullmatch(r"'QA_PLAN_REVIEW': (\{.*\})", w4["SR-4"]["new"])
    if not m or w4["SR-3"]["new"] != w4["SR-4"]["new"] or w4["SR-3"]["old"] != w4["SR-4"]["old"]:
        raise SystemExit("W4: SR-3 and SR-4 must carry the same QA_PLAN_REVIEW value")
    birth = m.group(1)
    for k in ("SR-3", "SR-4"):
        not_applied.append({"source": f"W4.json {k}", "disposition": "MERGED (W7-D4)",
                            "reason": "its QA_PLAN_REVIEW value goes into EXPECTED_POLICY_20261027 (SR-CF-9, SR-FV-20); "
                                      "EXPECTED_POLICY is not edited, so the 091426.1 and 100926.1 contracts still validate"})
    # W5: count-0 entries are new files or (SR-FV-34) made concrete; SR-FV-29 is replaced by SR-W7-FV-11
    w7_ids = {r["id"]: r for r in W["W7"]["skill_redlines"]}
    replaced = {"SR-FV-29"} if "SR-W7-FV-11" in w7_ids and "SR-FV-29" in (w7_ids["SR-W7-FV-11"].get("replaces") or "") else set()
    if not replaced:
        raise SystemExit("W7: SR-W7-FV-11 must declare that it replaces SR-FV-29")
    anchor_20261027 = "EXPECTED_POLICY_20261027 = {**EXPECTED_POLICY, "
    for r in W["W5"]["skill_redlines"]:
        rid = r["id"]
        if rid in NEW_FILE_IDS:
            if r["count"] != 0 or r["old"] not in ("", None) or not str(r["new"]).startswith("NEW FILE"):
                raise SystemExit(f"{rid}: expected a NEW FILE entry")
            new_files.append({"id": rid, "skill": r["package"], "file": r["file"], "spec": r["new"],
                              "built_by": "build_r1_successor_20261027.py; bundled by package_build_102726.py step N"})
            continue
        if rid in replaced:
            not_applied.append({"source": f"W5.json {rid}", "disposition": "REPLACED by SR-W7-FV-11",
                                "reason": "same old text; W7's new text is SR-FV-29's plus one line"})
            continue
        new, count, why = r["new"], r["count"], r.get("note") or f"PART-13 (W5 {rid})"
        old = r["old"]
        if rid == "SR-FV-34":
            if r["count"] != 0 or "positive_post_closure_adr_drainage" not in r["new"]:
                raise SystemExit("SR-FV-34: expected W5's prose insertion")
            old, new, count = SR_FV_34_ANCHOR, SR_FV_34_INSERT + SR_FV_34_ANCHOR, 1
            why = ("W5 SR-FV-34 made concrete by A3: the two scenarios inserted after positive_post_closure_adr_drainage; "
                   "the negative is the R1 successor's injected regression (D14)")
        elif rid in ("SR-CF-9", "SR-FV-20"):
            if new.count(anchor_20261027) != 1:
                raise SystemExit(f"{rid}: EXPECTED_POLICY_20261027 anchor not found once")
            new = new.replace(anchor_20261027, anchor_20261027 + "'qa_artifact_births': {**EXPECTED_POLICY['qa_artifact_births'], "
                              "'QA_PLAN_REVIEW': " + birth + "}, ")
            why = (r.get("note") or "") + " W7-D4: W4's SR-3/SR-4 QA_PLAN_REVIEW birth value is carried in EXPECTED_POLICY_20261027."
        elif r["count"] == 0:
            raise SystemExit(f"{rid}: unhandled count-0 entry")
        ops.append(op(rid, r["part"], f"W5.json {rid}", r["package"], r["file"], old, new, count, why.strip()))
    # W7 last; SR-W7-FV-11 lands with A3-C1's correction
    for r in W["W7"]["skill_redlines"]:
        new, source, why = r["new"], f"W7.json {r['id']}", r["why"]
        if r["id"] == "SR-W7-FV-11":
            if "gcfpe-20261009.1-100926.1-direct-handoff-contract.json" not in new or not new.endswith("    },"):
                raise SystemExit("SR-W7-FV-11: the text A3-C1 corrects has moved")
            new, source, why = A3_C1_FV11_NEW, source + "; corrected by A3-C1", why + " " + A3_C1_WHY
            not_applied.append({"source": "W7.json SR-W7-FV-11 new text", "disposition": "CORRECTED (A3-C1)",
                                "reason": A3_C1_WHY})
        ops.append(op(r["id"], r["part"], source, r["package"], r["file"], r["old"], new, r["count"], why))
    for r in A3_CORRECTIONS:
        ops.append(op(r["id"], r["part"], r["source"], r["skill"], r["file"], r["old"], r["new"], r["count"], r["why"]))
    ids = [o["id"] for o in ops]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate op id")
    for o in R_P1_OPS:
        if o["skill"] not in PACKAGES:
            raise SystemExit(f"{o['id']}: package not in the four")
    return {
        "record_type": "BACKLOG_OPEN_ITEMS_PACKAGE_REDLINES",
        "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
        "date": "2026-10-27",
        "scope": ("Text redlines for the four packages that change in GCFPE-20261027.1 / 102726.1 (W7-D2): change-flow, "
                  "flowmaster-validate, glow-hde-pr-development, glow-graph-contract. Each `old` must occur exactly "
                  "`count` times when its turn comes (ops apply in list order, W7's last); plan/package_apply.py refuses "
                  "otherwise and refuses a second application. Generated files (bundled 102726.1 contract and graph, R1 "
                  "oracle, map and matrix, profile, fixtures, derived validators, SKILL_TREE_SHA256) are package_build_102726.py's, "
                  "listed under new_files and in its specification, not here."),
        "generated_by": "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/plan/make_package_redlines_102726.py",
        "base_digests": BASE_DIGESTS,
        "decisions_applied": ["C-3: W3a's change-flow :436 and :453 in; governance-audit lines out",
                              "C-13: R-P1 conditional, EXCLUDED by default",
                              "W7-D2: four packages", "W7-D3: change-flow 3.5.0, flowmaster-validate 3.5.0, glow-hde-pr-development 1.5.0",
                              "W7-D4: W4 SR-3/SR-4 merged into EXPECTED_POLICY_20261027",
                              "W7: SR-W7-FV-11 replaces SR-FV-29; SR-W7-* after every worker op",
                              "A3-C1 (SR-W7-FV-11 corrected in place) and A3-C2..C4 (last): found by the scratch suite run; each needs the coordinator's acceptance"],
        "sources": {f"plan/work/{w}.json": sha256_file(WORK / f"{w}.json") for w in ("W1", "W3a", "W4", "W5", "W7")},
        "op_counts": {"total": len(ops), **{p: sum(o["skill"] == p for o in ops) for p in PACKAGES}},
        "ops": ops,
        "conditional_sets": [{"set": "R-P1", "default": "EXCLUDED", "authority": "C-13 (Nathan, scope freeze); W1-Q3",
                              "applies_after": "every op in `ops`", "ops": R_P1_OPS}],
        "new_files": new_files,
        "not_applied": not_applied,
    }


def render(doc: dict) -> str:
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def selftest() -> dict:
    base = load_workers()
    rows = {}
    rows["clean_merge_passes"] = bool(merge(copy.deepcopy(base))["ops"])

    def refused(mutate) -> bool:
        W = copy.deepcopy(base)
        mutate(W)
        try:
            merge(W)
        except SystemExit:
            return True
        return False

    rows["rejects_fifth_package"] = refused(lambda W: W["W1"]["skill_redlines"][0].__setitem__("package", "glow-write-boundary"))
    rows["rejects_empty_old"] = refused(lambda W: W["W5"]["skill_redlines"][0].__setitem__("old", ""))
    rows["rejects_identity_op"] = refused(lambda W: W["W7"]["skill_redlines"][0].__setitem__("new", W["W7"]["skill_redlines"][0]["old"]))
    rows["rejects_w3a_third_line"] = refused(lambda W: W["W3a"]["skill_redlines"].append(dict(W["W3a"]["skill_redlines"][0])))
    rows["rejects_sr3_sr4_disagree"] = refused(lambda W: next(r for r in W["W4"]["skill_redlines"] if r["id"] == "SR-3").__setitem__("new", "'QA_PLAN_REVIEW': {'x': 1}"))
    rows["rejects_missing_replaces"] = refused(lambda W: next(r for r in W["W7"]["skill_redlines"] if r["id"] == "SR-W7-FV-11").pop("replaces"))
    rows["rejects_duplicate_id"] = refused(lambda W: W["W7"]["skill_redlines"].append(dict(W["W7"]["skill_redlines"][0])))
    rows["rejects_new_file_with_count"] = refused(lambda W: next(r for r in W["W5"]["skill_redlines"] if r["id"] == "SR-CF-8").__setitem__("count", 1))
    doc = merge(copy.deepcopy(base))
    ids = [o["id"] for o in doc["ops"]]
    rows["sr_fv_29_absent_w7_fv_11_present"] = "SR-FV-29" not in ids and "SR-W7-FV-11" in ids
    rows["sr3_sr4_absent"] = not any(i in ("W4-SR-3", "W4-SR-4") for i in ids)
    rows["timing_ops_carry_w4_value"] = all("APPROVED_QA_PLAN_WITH_DELIVERED_CHANGE" in o["new"] and "'QA_PLAN_REVIEW': {'after': 'COMPLETE_PENDING_QA_PLAN_OR_EXPLICIT" not in o["new"]
                                            for o in doc["ops"] if o["id"] in ("SR-CF-9", "SR-FV-20"))
    rows["r_p1_not_in_ops"] = not any(i.startswith("RP1-") for i in ids)
    n = len(A3_CORRECTIONS)
    rows["w7_then_a3_corrections_last"] = (ids[-32 - n:-n] == [r["id"] for r in base["W7"]["skill_redlines"]]
                                           and ids[-n:] == [r["id"] for r in A3_CORRECTIONS])
    return {"mode": "selftest", "rows": rows, "selftest_ok": all(rows.values())}


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        res = selftest()
        print(json.dumps(res, indent=1))
        return 0 if res["selftest_ok"] else 1
    text = render(merge(load_workers()))
    if "--check" in argv:
        equal = OUT.is_file() and OUT.read_text(encoding="utf-8") == text
        print(json.dumps({"mode": "check", "equal": equal, "sha256": hashlib.sha256(text.encode()).hexdigest()}))
        return 0 if equal else 1
    OUT.write_text(text, encoding="utf-8")
    doc = json.loads(text)
    print(json.dumps({"mode": "write", "path": str(OUT), "sha256": sha256_file(OUT), "op_counts": doc["op_counts"],
                      "conditional": {s["set"]: len(s["ops"]) for s in doc["conditional_sets"]},
                      "new_files": len(doc["new_files"]), "not_applied": len(doc["not_applied"])}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
