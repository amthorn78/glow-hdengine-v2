#!/usr/bin/env python3
"""X8 package build for MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN §3 PART-01, §5 X8).

  package_build.py <installed-copies-dir> <out-dir> --contract <100926.1 production contract>
      --graph <100926.1 production graph json> --plan <approved PLAN document> [--check]

<installed-copies-dir> holds verified scratch copies of the installed skills (never the synced install
directory). The six packages are written to <out-dir>, which must not exist. In order:

  A   copy the six skills; apply plan/package_apply.py's redlines; apply the glow-graph-contract patch;
  A2  apply execute/d24-repair-redlines.json, the repair of the D24 round-1 REQUIRED findings (X10);
  B   bundle the production contract and graph into change-flow and flowmaster-validate;
  F   write the 100926.1 fixtures: the 091426.1 scenarios with their release fields moved, plus 17 cases
      for F01, F02, F05, F07, F08 and F09;
  P   write the 100926.1 validation profile, measured from the bundled files;
  M   derive flowmaster-validate's validate_gcfpe_20261009.py with plan/make_profile_20261009.py, then the
      X8 additions (M-A1 to M-A2);
  R   derive run_gcfpe_20261009_fixtures.py from the 091426.1 runner;
  C   derive change-flow's validate_gcfpe_20261009.py from its 091426.1 sibling, without the URL map and
      topology readback, which 100926.1 does not have;
  V   apply V1 to V6 to flowmaster-validate's suite, its current-overlay scripts and its change-flow fixtures;
  G   apply the glow-hde-pr-development validator changes;
  D   apply the documentation changes;
  I   recompute flowmaster-validate's SKILL_TREE_SHA256, last (V7).

Every edit is a named substitution whose old text must occur exactly the stated number of times, so a moved
base fails before its file is written. Byte pins are measured from the files, never typed. --check rebuilds
into a temporary directory and reports whether <out-dir> is byte-identical to it, writing nothing else.
Prints one JSON report. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN_DIR = HERE.parent / "plan"
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract",
            "session-relay-flowmaster", "amthor-workspace-governance-audit")
NEW = "gcfpe-20261009.1-100926.1"
OLD = "gcfpe-20260914.1-091426.1"
TYPESAFE_RULE = "No agent gives its own recommendation, assessment or ranking of model, reasoning level or effort."
TYPESAFE_PROCEDURE = "run the installed TypeSafe scoring skill's script once"
CF_RECOVERY = "recover the role's session from the role and its artifacts (`D27`)"
CF_VERDICTS = "exactly one of APPROVE, APPROVE_AS_CHANGED or DENY"
FORMAT_KEYS = ("excluded_content", "heading", "number_carrier", "subject_matter", "subordinate_headings")
PR_RECOVERY = "the receiving side recovers the PR-35 phase from its role, work unit and artifacts (`D27`)"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def substitute(path: Path, subs: list[tuple[str, str, str, int]], report: list) -> None:
    text = path.read_text(encoding="utf-8")
    for name, old, new, want in subs:
        got = text.count(old)
        if got != want:
            raise SystemExit(f"{name} ({path.name}): expected {want} occurrence(s), found {got}")
        text = text.replace(old, new)
        report.append({"substitution": name, "file": path.as_posix().split("/out/")[-1], "count": got})
    path.write_text(text, encoding="utf-8")


def load(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sys.path.pop(0)
    return mod


# --------------------------------------------------------------------------------------------- F: fixtures
NEW_NEGATIVE_RULES = {
    "CONT-NEG-01": "D27_ROLE_ARTIFACT_CONTINUITY",
    "QAEXEC-NEG-01": "D27_QA_EXECUTION_ARRANGEMENT",
    "PF10NUM-NEG-01": "PF06_PRODUCER_NUMBERS_ADDENDUM",
    "TS-NEG-01": "PF10_TYPESAFE_READING_ONLY",
    "REM-NEG-01": "ESC40_NATIVE_REMEDIATION_VERDICT",
    "RS20PR-NEG-01": "PR20_RS20_PRE_PROCEED_RETURN",
}
_TS_OK = {"reading_in_artifact": True, "named_before_block": True, "surface_advice_in_artifact": True}
_REM_OK = {"reviewer": "ESC-40", "decision": "APPROVE_AS_CHANGED", "affected_bases_exist_at_origin": True}
_RS20_OK = {"origin": "RS-20", "receiver": "PR-20", "decision": "APPROVE", "recorded_pr20_planning_origin": True,
            "before_proceed": True}
NEW_SCENARIOS = [
    # F01 (D27): continuity is the role, the work unit and its artifacts.
    {"id": "CONT-POS-01", "polarity": "POSITIVE", "rule": "role_continuity",
     "input": {"recorded_session_unavailable": True, "role": "PR-35", "work_unit_id": True, "artifacts_read_back": True},
     "expected": "RECOVER_FROM_ROLE_AND_ARTIFACTS"},
    {"id": "CONT-POS-02", "polarity": "POSITIVE", "rule": "role_continuity",
     "input": {"recorded_session_available": True, "role": "PR-35"}, "expected": "CONTINUE_RECORDED_SESSION"},
    {"id": "CONT-NEG-01", "polarity": "NEGATIVE", "rule": "role_continuity",
     "input": {"recorded_session_available": True, "role": "PR-35", "moved_to_different_session": True},
     "expected": "VALIDATION_FAILURE", "variants": [
         {"name": "recovery-without-artifacts", "input": {"recorded_session_unavailable": True, "role": "PR-35",
                                                          "work_unit_id": True, "artifacts_read_back": False},
          "expected": "VALIDATION_FAILURE"},
         {"name": "recovery-with-new-proceed", "input": {"recorded_session_unavailable": True, "role": "PR-35",
                                                         "work_unit_id": True, "artifacts_read_back": True,
                                                         "new_proceed": True}, "expected": "VALIDATION_FAILURE"},
         {"name": "recovery-as-new-work-unit", "input": {"recorded_session_unavailable": True, "role": "PR-35",
                                                         "work_unit_id": True, "artifacts_read_back": True,
                                                         "new_work_unit": True}, "expected": "VALIDATION_FAILURE"}]},
    # F02 (D27): QA execution follows the arrangement the Product Owner chooses; Kronos never executes Ops.
    {"id": "QAEXEC-POS-01", "polarity": "POSITIVE", "rule": "qa_execution",
     "input": {"actor": "Kronos", "lane": "QA", "product_owner_chose_arrangement": True},
     "expected": "QA_EXECUTION_UNDER_CHOSEN_ARRANGEMENT"},
    {"id": "QAEXEC-POS-02", "polarity": "POSITIVE", "rule": "qa_execution",
     "input": {"actor": "DEVOPS_OPERATOR", "lane": "OPS"}, "expected": "OPS_EXECUTION_BY_AUTHORIZED_OPERATOR"},
    {"id": "QAEXEC-NEG-01", "polarity": "NEGATIVE", "rule": "qa_execution",
     "input": {"actor": "Kronos", "lane": "OPS"}, "expected": "VALIDATION_FAILURE", "variants": [
         {"name": "kronos-qa-not-chosen", "input": {"actor": "Kronos", "lane": "QA",
                                                    "product_owner_chose_arrangement": False},
          "expected": "VALIDATION_FAILURE"},
         {"name": "execution-claims-acceptance", "input": {"actor": "Kronos", "lane": "QA",
                                                           "product_owner_chose_arrangement": True,
                                                           "execution_claims_acceptance": True},
          "expected": "VALIDATION_FAILURE"}]},
    # F05 (PF06 §0.1A, PF27): the producer numbers its addendum at creation; the Product Owner pastes.
    {"id": "PF10NUM-POS-01", "polarity": "POSITIVE", "rule": "pf10_numbering",
     "input": {"resolved_at_creation_from_current_pf10": True, "number_in_h2_heading": True,
               "product_owner_pastes": True}, "expected": "PRODUCER_NUMBERS_ADDENDUM"},
    {"id": "PF10NUM-NEG-01", "polarity": "NEGATIVE", "rule": "pf10_numbering",
     "input": {"product_owner_numbers": True, "product_owner_pastes": True}, "expected": "VALIDATION_FAILURE",
     "variants": [
         {"name": "standalone-number-field", "input": {"resolved_at_creation_from_current_pf10": True,
                                                       "number_in_h2_heading": True, "product_owner_pastes": True,
                                                       "standalone_number_field": True},
          "expected": "VALIDATION_FAILURE"},
         {"name": "number-not-resolved-at-creation", "input": {"resolved_at_creation_from_current_pf10": False,
                                                               "number_in_h2_heading": True,
                                                               "product_owner_pastes": True},
          "expected": "VALIDATION_FAILURE"}]},
    # F07 (HDE Build Notes; PF04 §9.1.3): the TypeSafe reading and surface advice live in the artifact.
    {"id": "TS-POS-01", "polarity": "POSITIVE", "rule": "typesafe_reading", "input": dict(_TS_OK),
     "expected": "TYPESAFE_READING_RECORDED"},
    {"id": "TS-POS-02", "polarity": "POSITIVE", "rule": "typesafe_reading",
     "input": {"not_read_with_reason": True, "named_before_block": True, "surface_advice_in_artifact": True},
     "expected": "TYPESAFE_NOT_READ_RECORDED"},
    {"id": "TS-NEG-01", "polarity": "NEGATIVE", "rule": "typesafe_reading",
     "input": {**_TS_OK, "agent_own_recommendation": True}, "expected": "VALIDATION_FAILURE", "variants": [
         {"name": "reading-in-block", "input": {**_TS_OK, "in_block": True}, "expected": "VALIDATION_FAILURE"},
         {"name": "reading-as-route-or-gate", "input": {**_TS_OK, "route_or_gate": True},
          "expected": "VALIDATION_FAILURE"},
         {"name": "notion-row-written", "input": {**_TS_OK, "notion_row_written": True},
          "expected": "VALIDATION_FAILURE"},
         {"name": "surface-advice-with-model-content", "input": {**_TS_OK, "surface_advice_has_model_content": True},
          "expected": "VALIDATION_FAILURE"},
         {"name": "no-surface-advice", "input": {**_TS_OK, "surface_advice_in_artifact": False},
          "expected": "VALIDATION_FAILURE"}]},
    # F08: ESC-40 decides APPROVE, APPROVE_AS_CHANGED or DENY; ESC-25 and ESC-30 take a proposal or a legacy plan id.
    {"id": "REM-POS-01", "polarity": "POSITIVE", "rule": "remediation_review", "input": dict(_REM_OK),
     "expected": "REMEDIATION_DECIDED"},
    {"id": "REM-POS-02", "polarity": "POSITIVE", "rule": "remediation_review",
     "input": {"receiver": "ESC-30", "input_id": "REMEDIATION_PLAN_ID", "legacy_semantics_equivalent": True},
     "expected": "REMEDIATION_INPUT_ACCEPTED"},
    {"id": "REM-POS-03", "polarity": "POSITIVE", "rule": "remediation_review",
     "input": {"receiver": "ESC-25", "input_id": "REMEDIATION_PROPOSAL_ID"}, "expected": "REMEDIATION_INPUT_ACCEPTED"},
    {"id": "REM-NEG-01", "polarity": "NEGATIVE", "rule": "remediation_review",
     "input": {**_REM_OK, "decision": "REVISION_REQUIRED"}, "expected": "VALIDATION_FAILURE", "variants": [
         {"name": "requires-absent-base", "input": {**_REM_OK, "requires_absent_base": True},
          "expected": "VALIDATION_FAILURE"},
         {"name": "decided-outside-esc40", "input": {**_REM_OK, "reviewer": "ESC-30"}, "expected": "VALIDATION_FAILURE"},
         {"name": "legacy-id-without-equivalent-semantics", "input": {"receiver": "ESC-30",
                                                                      "input_id": "REMEDIATION_PLAN_ID",
                                                                      "legacy_semantics_equivalent": False},
          "expected": "VALIDATION_FAILURE"}]},
    # F09: PR-20 receives RS-20's return only from its own recorded planning origin, before Proceed.
    {"id": "RS20PR-POS-01", "polarity": "POSITIVE", "rule": "rs20_pre_proceed_return", "input": dict(_RS20_OK),
     "expected": "PR20_PLANNING_RESUMED"},
    {"id": "RS20PR-NEG-01", "polarity": "NEGATIVE", "rule": "rs20_pre_proceed_return",
     "input": {**_RS20_OK, "recorded_pr20_planning_origin": False}, "expected": "VALIDATION_FAILURE", "variants": [
         {"name": "after-proceed", "input": {**_RS20_OK, "before_proceed": False}, "expected": "VALIDATION_FAILURE"},
         {"name": "decision-outside-accepted-inputs", "input": {**_RS20_OK, "decision": "DENY"},
          "expected": "VALIDATION_FAILURE"}]},
]


MB008_CASES_NOTE = ("MODIFICATION-20261011-gcfpe-mb008-to-promotion PLAN §3 PART-01 and PART-04: 17 cases for F01, F02, "
                    "F05, F07, F08 and F09 after the 37 section-13 cases of the 091426.1 suite")


def write_fixtures(fv: Path) -> Path:
    """The 091426.1 file, edited in its own layout: header values, appended ids, attributions and scenario lines."""
    raw = (fv / f"fixtures/{OLD}/scenarios.json").read_text(encoding="utf-8")
    base = json.loads(raw)
    text = raw
    edits = [
        ('  "suite_id": "GCFPE-20260914.1-091426.1-SECTION-13",\n', '  "suite_id": "GCFPE-20261009.1-100926.1-SECTION-13",\n'),
        ('  "release": "GCFPE-20260914.1",\n', '  "release": "GCFPE-20261009.1",\n'),
        ('  "prompt_version": "091426.1",\n', '  "prompt_version": "100926.1",\n'),
        ('  "governing_plan_section": "13",\n',
         '  "governing_plan_section": "13",\n' f'  "mb008_cases": {json.dumps(MB008_CASES_NOTE, ensure_ascii=False)},\n'),
    ]
    ids = [s["id"] for s in NEW_SCENARIOS]
    id_lines = ",\n".join("    " + ", ".join(json.dumps(i) for i in ids[n:n + 4]) for n in range(0, len(ids), 4))
    edits.append(('    "REPLAN-NEG-01"\n  ],\n', '    "REPLAN-NEG-01",\n' + id_lines + "\n  ],\n"))
    attr = ",\n".join(f"    {json.dumps(k)}: {json.dumps(v)}" for k, v in NEW_NEGATIVE_RULES.items())
    edits.append(('    "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED"\n  },\n',
                  '    "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED",\n' + attr + "\n  },\n"))
    rows = ",\n".join("    " + json.dumps(s, separators=(",", ":"), ensure_ascii=False) for s in NEW_SCENARIOS)
    edits.append(("}\n  ]\n}\n", "},\n" + rows + "\n  ]\n}\n"))
    for old, new in edits:
        if text.count(old) != 1:
            raise SystemExit(f"fixtures: anchor {old[:40]!r} occurs {text.count(old)} times")
        text = text.replace(old, new)
    doc = json.loads(text)
    want = dict(base)
    want.update(suite_id="GCFPE-20261009.1-100926.1-SECTION-13", release="GCFPE-20261009.1", prompt_version="100926.1",
                mb008_cases=MB008_CASES_NOTE, required_fixture_ids=base["required_fixture_ids"] + ids,
                negative_rule_attribution={**base["negative_rule_attribution"], **NEW_NEGATIVE_RULES},
                scenarios=base["scenarios"] + NEW_SCENARIOS)
    if doc != want:
        raise SystemExit("fixtures: the edited file does not read back as intended")
    out = fv / f"fixtures/{NEW}/scenarios.json"
    out.parent.mkdir(parents=True)
    out.write_text(text, encoding="utf-8")
    return out


# ---------------------------------------------------------------------------------------------- P: profile
def write_profile(fv: Path, fixture_path: Path) -> Path:
    prof = json.loads((fv / f"references/{OLD}-validation-profile.json").read_text(encoding="utf-8"))
    cpath, gpath = fv / f"references/{NEW}-direct-handoff-contract.json", fv / f"references/{NEW}-candidate-graph-contract.json"
    graph = json.loads(gpath.read_text(encoding="utf-8"))
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    prof.update(profile_id="GCFPE-20261009.1-100926.1-VALIDATION", prompt_version="100926.1",
                target_release="GCFPE-20261009.1", selected_member_count_during_staging=55,
                selected_prompt_version_during_staging="091426.1", selected_release_during_staging="GCFPE-20260914.1",
                validator_revision="3.4.0",
                installed_skill_revisions={"change-flow": "3.4.0", "glow-hde-pr-development": "1.4.0"})
    prof["candidate_contract"].update(bundled_relative_path=f"references/{NEW}-direct-handoff-contract.json",
                                      relative_to_change_flow=f"references/{NEW}-direct-handoff-contract.json",
                                      byte_count=cpath.stat().st_size, sha256=sha256(cpath))
    prof["frozen_graph"].update(bundled_relative_path=f"references/{NEW}-candidate-graph-contract.json",
                                relative_to_candidate_root="graph/GCFPE-20261009.1-Candidate-Graph-Contract.json",
                                byte_count=gpath.stat().st_size, sha256=sha256(gpath), edge_count=len(graph["edges"]),
                                node_count=len(graph["nodes"]))
    prof["fixtures"].update(relative_path=f"fixtures/{NEW}/scenarios.json", sha256=sha256(fixture_path),
                            count=len(fixtures["scenarios"]))
    out = fv / f"references/{NEW}-validation-profile.json"
    out.write_text(json.dumps(prof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out


# -------------------------------------------------------------------------- M: X8 additions to the profile
def m_additions(n_fixtures: int) -> list[tuple[str, str, str, int]]:
    return [
        ("M-A1 fixture count", '        "schema_version": "gcfpe-scenarios/2.0", "count": 37,',
         f'        "schema_version": "gcfpe-scenarios/2.0", "count": {n_fixtures},', 1),
        # make_profile's dry run (N6) ran before the redlines (N8) moved the PR skill to 1.4.0, so its 25
        # substitutions did not reach this marker. V6's reading-rule phrases for glow-hde-pr-development join it.
        ("M-A2 PR skill revision and reading rule",
         '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1", "REMOTE_EVIDENCE_PENDING",\n',
         '            "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.4.0", "REMOTE_EVIDENCE_PENDING",\n'
         f'            {TYPESAFE_RULE!r},\n            {TYPESAFE_PROCEDURE!r},\n', 1),
    ]


# ------------------------------------------------------------------------------------------- R: the runner
NEW_RULES = '''    # MB-008 (MODIFICATION-20261011-gcfpe-mb008-to-promotion), PART-01 and PART-04: one rule per repaired
    # finding. Each projects only from a declared invariant: of the contract, or of change-flow's own text where
    # the contract carries no field for the term (F01's recovery sentence, F02's tokens, F08's verdicts). The
    # suite removes each invariant once (`dependency-*` cases), so none of these is a guard nobody has fired.
    if rule == "role_continuity":  # F01 (D27)
        shared = development.get("shared_exactly_one", [])
        boundaries = development.get("added_boundaries", {})
        if facts.get("moved_to_different_session") or facts.get("new_proceed") or facts.get("new_work_unit"):
            return "VALIDATION_FAILURE"
        if facts.get("recorded_session_available"):
            return "CONTINUE_RECORDED_SESSION"
        if (
            facts.get("recorded_session_unavailable") and facts.get("role") and facts.get("work_unit_id")
            and facts.get("artifacts_read_back")
            and "continuous recovery/artifact lineage" in shared and "WORK_UNIT_ID" in shared
            and boundaries.get("proceed") == 0 and boundaries.get("work_unit") == 0
            and CF_RECOVERY in skill_text
        ):
            return "RECOVER_FROM_ROLE_AND_ARTIFACTS"
        return "VALIDATION_FAILURE"

    if rule == "qa_execution":  # F02 (D27)
        if (
            facts.get("execution_claims_acceptance")
            or "QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE" not in skill_text
            or "KRONOS_NEVER_EXECUTES_OPS" not in skill_text
        ):
            return "VALIDATION_FAILURE"
        if facts.get("lane") == "OPS":
            return "VALIDATION_FAILURE" if facts.get("actor") == "Kronos" else "OPS_EXECUTION_BY_AUTHORIZED_OPERATOR"
        if facts.get("lane") == "QA" and facts.get("product_owner_chose_arrangement"):
            return "QA_EXECUTION_UNDER_CHOSEN_ARRANGEMENT"
        return "VALIDATION_FAILURE"

    if rule == "pf10_numbering":  # F05 (PF06 §0.1A, PF27)
        carrier = str((addendum.get("format_expectations") or {}).get("number_carrier", ""))
        if (
            facts.get("product_owner_numbers") or facts.get("standalone_number_field")
            or not facts.get("resolved_at_creation_from_current_pf10")
        ):
            return "VALIDATION_FAILURE"
        if (
            facts.get("number_in_h2_heading") and facts.get("product_owner_pastes")
            and addendum.get("producer_allocates_pf10_number") is True
            and carrier.startswith("the H2 heading")
            and "pf10_addendum_number" in addendum.get("forbidden_fields", [])
        ):
            return "PRODUCER_NUMBERS_ADDENDUM"
        return "VALIDATION_FAILURE"

    if rule == "typesafe_reading":  # F07 (HDE Build Notes; PF04 §9.1.3)
        prohibited = set(contract.get("prohibited_active_routing", []))
        if any(facts.get(key) for key in (
            "agent_own_recommendation", "in_block", "route_or_gate", "notion_row_written",
            "surface_advice_has_model_content",
        )):
            return "VALIDATION_FAILURE"
        if not {"MODEL_OR_STRENGTH_ASSESSMENT", "REASONING_RECOMMENDATION"} <= prohibited:
            return "VALIDATION_FAILURE"
        if not (facts.get("named_before_block") and facts.get("surface_advice_in_artifact")):
            return "VALIDATION_FAILURE"
        if facts.get("reading_in_artifact"):
            return "TYPESAFE_READING_RECORDED"
        if facts.get("not_read_with_reason"):
            return "TYPESAFE_NOT_READ_RECORDED"
        return "VALIDATION_FAILURE"

    if rule == "remediation_review":  # F08 (ESC-25, ESC-30, ESC-40)
        native = contract.get("native_remediation_contract", {})
        identity = (contract.get("artifact_availability_contract") or {}).get("remediation_artifact_identity", {})
        if facts.get("input_id"):
            proposal = facts["input_id"] == "REMEDIATION_PROPOSAL_ID" and identity.get("proposal") == "REMEDIATION_PROPOSAL"
            legacy = (
                facts["input_id"] == "REMEDIATION_PLAN_ID" and facts.get("legacy_semantics_equivalent")
                and "REMEDIATION_PLAN/" in str(identity.get("legacy_alias_rule", ""))
            )
            return "REMEDIATION_INPUT_ACCEPTED" if facts.get("receiver") in {"ESC-25", "ESC-30"} and (proposal or legacy) else "VALIDATION_FAILURE"
        if (
            facts.get("reviewer") == native.get("approval_prompt") == "ESC-40"
            and native.get("approval_artifact") == "REMEDIATION_REVIEW"
            and CF_VERDICTS in skill_text
            and facts.get("decision") in {"APPROVE", "APPROVE_AS_CHANGED", "DENY"}
            and facts.get("affected_bases_exist_at_origin") and not facts.get("requires_absent_base")
        ):
            return "REMEDIATION_DECIDED"
        return "VALIDATION_FAILURE"

    if rule == "rs20_pre_proceed_return":  # F09
        receiver = (contract.get("receiver_compatibility") or {}).get("PR-20", {})
        if (
            facts.get("origin") == "RS-20" and facts.get("receiver") == "PR-20"
            and f"RS-20:RESCOPE_REVIEW:{facts.get('decision')}" in receiver.get("accepted_inputs", [])
            and receiver.get("rs20_returns_only_from_recorded_pr20_planning_origin_before_proceed") is True
            and facts.get("recorded_pr20_planning_origin") and facts.get("before_proceed")
        ):
            return "PR20_PLANNING_RESUMED"
        return "VALIDATION_FAILURE"
'''

DEPENDENCY_CASES = '''
    # MB-008: each new rule's positive projection depends on its declared invariant. Removing the invariant from a
    # copy of the contract, or from the change-flow text, must turn that positive into VALIDATION_FAILURE.
    rows_by_id = {row["id"]: row for row in fixtures.get("scenarios", []) if isinstance(row, dict)}

    def dependency_case(name: str, fixture_id: str, mutate=None, text: str | None = None) -> None:
        changed = copy.deepcopy(source)
        if mutate is not None:
            mutate(changed)
        row = rows_by_id.get(fixture_id)
        observed = project_behavior(changed, row["rule"], row["input"], skill_text if text is None else text) if row else None
        cases.append({"name": name, "passed": observed == "VALIDATION_FAILURE", "observed": observed,
                      "expected": "VALIDATION_FAILURE"})

    dependency_case("dependency-f01-recovery-lineage", "CONT-POS-01",
                    lambda c: c["pr_development_contract"]["shared_exactly_one"].remove("continuous recovery/artifact lineage"))
    dependency_case("dependency-f01-recovery-sentence", "CONT-POS-01", text=skill_text.replace(CF_RECOVERY, ""))
    dependency_case("dependency-f02-arrangement-token", "QAEXEC-POS-01",
                    text=skill_text.replace("QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE", ""))
    dependency_case("dependency-f02-kronos-ops-token", "QAEXEC-POS-02",
                    text=skill_text.replace("KRONOS_NEVER_EXECUTES_OPS", ""))
    dependency_case("dependency-f05-producer-numbers", "PF10NUM-POS-01",
                    lambda c: c["pf10_addendum_contract"].__setitem__("producer_allocates_pf10_number", False))
    dependency_case("dependency-f05-number-carrier", "PF10NUM-POS-01",
                    lambda c: c["pf10_addendum_contract"]["format_expectations"].__setitem__("number_carrier", "a pf10_addendum_number field"))
    dependency_case("dependency-f07-prohibited-routing", "TS-POS-01",
                    lambda c: c["prohibited_active_routing"].remove("REASONING_RECOMMENDATION"))
    dependency_case("dependency-f08-approval-prompt", "REM-POS-01",
                    lambda c: c["native_remediation_contract"].__setitem__("approval_prompt", "ESC-30"))
    dependency_case("dependency-f08-verdict-sentence", "REM-POS-01", text=skill_text.replace(CF_VERDICTS, ""))
    dependency_case("dependency-f08-proposal-identity", "REM-POS-03",
                    lambda c: c["artifact_availability_contract"]["remediation_artifact_identity"].__setitem__("proposal", "REMEDIATION_PLAN"))
    dependency_case("dependency-f08-legacy-alias-rule", "REM-POS-02",
                    lambda c: c["artifact_availability_contract"]["remediation_artifact_identity"].__setitem__("legacy_alias_rule", "none"))
    dependency_case("dependency-f09-accepted-input", "RS20PR-POS-01",
                    lambda c: c["receiver_compatibility"]["PR-20"]["accepted_inputs"].remove("RS-20:RESCOPE_REVIEW:APPROVE"))
    dependency_case("dependency-f09-origin-flag", "RS20PR-POS-01",
                    lambda c: c["receiver_compatibility"]["PR-20"].__setitem__("rs20_returns_only_from_recorded_pr20_planning_origin_before_proceed", False))
'''


def runner_subs(base_text: str, n_pos: int, n_neg: int) -> list[tuple[str, str, str, int]]:
    total = n_pos + n_neg
    neg_lines = "".join(f'    "{k}": "{v}",\n' for k, v in NEW_NEGATIVE_RULES.items())
    return [
        ("R01 docstring", '"""Run the 37 deterministic GCFPE v2 repair fixtures and contract mutations."""',
         f'"""Run the {total} deterministic GCFPE-20261009.1 / 100926.1 fixtures and contract mutations.\n\n'
         'Derived from the 091426.1 runner by MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN PART-01): the 37\n'
         'section-13 cases with their release fields moved, and 17 cases for F01, F02, F05, F07, F08 and F09.\n"""', 1),
        ("R02 validator import", "from validate_gcfpe_20260914 import (", "from validate_gcfpe_20261009 import (", 1),
        ("R03 constants", "REPLAN_DEFECT_REPAIR = {\n",
         f"CF_RECOVERY = {CF_RECOVERY!r}\nCF_VERDICTS = {CF_VERDICTS!r}\n\nREPLAN_DEFECT_REPAIR = {{\n", 1),
        ("R04 negative rules", '    "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED",\n}',
         '    "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED",\n' + neg_lines + "}", 1),
        ("R05 projection signature",
         "def project_behavior(contract: dict[str, Any], rule: str, facts: dict[str, Any]) -> str:",
         'def project_behavior(contract: dict[str, Any], rule: str, facts: dict[str, Any], skill_text: str = "") -> str:', 1),
        ("R06 MB-008 rules", '    return "VALIDATION_FAILURE"\n\n\ndef as_selected_production',
         NEW_RULES + '    return "VALIDATION_FAILURE"\n\n\ndef as_selected_production', 1),
        ("R07 fixture counts",
         "    if not isinstance(required, list) or len(required) != 37 or len(set(required)) != 37:",
         f"    if not isinstance(required, list) or len(required) != {total} or len(set(required)) != {total}:", 1),
        ("R08 fixture row count", "    if not isinstance(rows, list) or len(rows) != 37:",
         f"    if not isinstance(rows, list) or len(rows) != {total}:", 1),
        ("R09 polarity counts", 'if polarities.count("POSITIVE") != 20 or polarities.count("NEGATIVE") != 17:',
         f'if polarities.count("POSITIVE") != {n_pos} or polarities.count("NEGATIVE") != {n_neg}:', 1),
        ("R10 change-flow text", '    negative_rules = fixtures.get("negative_rule_attribution", {})\n',
         '    negative_rules = fixtures.get("negative_rule_attribution", {})\n'
         '    skill_path = change_skill_dir / "SKILL.md"\n'
         '    skill_text = skill_path.read_text(encoding="utf-8") if skill_path.is_file() else ""\n', 1),
        ("R11 scenario projection", 'project_behavior(source, row["rule"], row["input"])',
         'project_behavior(source, row["rule"], row["input"], skill_text)', 1),
        ("R12 variant projection", 'project_behavior(source, row["rule"], variant["input"])',
         'project_behavior(source, row["rule"], variant["input"], skill_text)', 1),
        ("R13 dependency cases",
         '        behavior_case(f"independent-alpha-history-{historical.lower()}", "alpha", {"source": historical}, "HISTORICAL_HANDOFF_REJECTED")\n',
         '        behavior_case(f"independent-alpha-history-{historical.lower()}", "alpha", {"source": historical}, "HISTORICAL_HANDOFF_REJECTED")\n'
         + DEPENDENCY_CASES, 1),
        ("R14 report revision", '        "validator_revision": "3.3.2",', '        "validator_revision": "3.4.0",', 1),
        ("R90 contract ids", "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-", "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-",
         base_text.count("GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-")),
        ("R91 release literal", "GCFPE-20260914.1", "GCFPE-20261009.1", None),
        ("R92 version literal", "091426.1", "100926.1", None),
    ]


# -------------------------------------------------------------------- C: change-flow's 100926.1 validator
def change_flow_subs(m: dict) -> list[tuple[str, str, str, int]]:
    return [
        ("C01 docstring", '"""Deterministic checks for the GCFPE-20260914.1 Change Flow successor."""',
         '"""Deterministic checks for the GCFPE-20261009.1 / 100926.1 Change Flow contract.\n\n'
         "Derived from the 091426.1 checks by MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN PART-01). The 100926.1\n"
         "release has no prompt URL map and no topology readback: its members' URLs and parents are the graph's, and the\n"
         "contract names its governing plan as a repository file and the 091426.1 contract as its predecessor.\n\"\"\"", 1),
        ("C02 retired staging files",
         f'URL_MAP = ROOT / "references" / "{OLD}-prompt-url-map.json"\n'
         f'TOPOLOGY_READBACK = ROOT / "references" / "{OLD}-prompt-topology-readback.json"\n', "", 1),
        ("C03 graph and plan pins",
         'EXPECTED_GRAPH_SHA = "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d"\n'
         'EXPECTED_PLAN_SHA = "e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01"\n',
         f'EXPECTED_GRAPH_SHA = "{m["graph_sha"]}"\nEXPECTED_PLAN_SHA = "{m["plan_sha"]}"\n'
         f'EXPECTED_PLAN_BYTES = {m["plan_bytes"]}\n'
         f'EXPECTED_PLAN_PATH = "{m["plan_path"]}"\n'
         'EXPECTED_PREDECESSOR_CONTRACT_SHA = "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c"\n', 1),
        ("C04 retired staging pins",
         'EXPECTED_URL_MAP_SHA = "af03c3531ca421c000fd9536978fbe4671a41395f4a993f81c76e2c5aba087b6"\n'
         'EXPECTED_TOPOLOGY_SHA = "705f5acfad74c9b32b91f4305e64372098f5cd82d7cd91f2388888ca7db661e3"\n', "", 1),
        ("C05 routing surface pin",
         'EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"\nEXPECTED_ROUTING_SURFACE_ROWS = 284',
         f'EXPECTED_ROUTING_SURFACE = "{m["surface"]}"\nEXPECTED_ROUTING_SURFACE_ROWS = {m["surface_rows"]}', 1),
        ("C06 retired staging reads",
         "    url_map_bytes = URL_MAP.read_bytes()\n    url_map = json.loads(url_map_bytes.decode(\"utf-8\"))\n"
         "    topology_bytes = TOPOLOGY_READBACK.read_bytes()\n    topology = json.loads(topology_bytes.decode(\"utf-8\"))\n",
         "", 1),
        ("C07 revision", '"CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1" in skill',
         '"CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0" in skill', 1),
        ("C08 contract identity",
         '    require(contract["target_release"] == "GCFPE-20260914.1", "target release")\n'
         '    require(contract["contract_revision"] == "4.1.1", "corrected-source contract revision")\n'
         '    require(contract["prompt_version"] == "091426.1", "prompt family")\n',
         '    require(contract["target_release"] == "GCFPE-20261009.1", "target release")\n'
         '    require(contract["contract_revision"] == "4.2.0", "graph-derived contract revision")\n'
         '    require(contract["prompt_version"] == "100926.1", "prompt family")\n'
         '    require(contract["predecessor_release"] == "GCFPE-20260914.1" and contract["predecessor_prompt_version"] == "091426.1", "predecessor release")\n', 1),
        ("C09 governing plan and repair-baseline pins",
         '    require(plan["sha256"] == EXPECTED_PLAN_SHA and plan["byte_count"] == 53118, "exact raw governing-plan pin")\n',
         '    require(\n'
         '        plan["sha256"] == EXPECTED_PLAN_SHA and plan["byte_count"] == EXPECTED_PLAN_BYTES\n'
         '        and plan["representation"] == "REPOSITORY_FILE_ON_MAIN" and plan["repository_path"] == EXPECTED_PLAN_PATH,\n'
         '        "governing plan pinned as a repository file",\n'
         '    )\n', 1),
        ("C10 representations",
         '    require(plan["representation"] == pf10["representation"] == "EXACT_RAW_DRIVE_FILE_BYTES", "raw source representations")\n',
         '    require(pf10["representation"] == "EXACT_RAW_DRIVE_FILE_BYTES", "raw PF10 repair-baseline representation")\n', 1),
        ("C11 predecessor contract instead of the Drive plan binding",
         '    bindings = {row["external_id"]: row for row in graph["source_bindings"]["bindings"]}\n'
         '    require(bindings[plan["drive_file_id"]]["sha256"] == EXPECTED_PLAN_SHA, "graph governing-plan pin")\n',
         '    predecessor = contract["source_snapshot"]["predecessor_direct_handoff_contract"]\n'
         '    require(\n'
         '        predecessor["sha256"] == EXPECTED_PREDECESSOR_CONTRACT_SHA\n'
         '        and predecessor["contract_id"] == "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED",\n'
         '        "predecessor contract pin",\n'
         '    )\n', 1),
        ("C12 retired staging byte pins",
         '    require(sha256(url_map_bytes) == EXPECTED_URL_MAP_SHA, "bundled URL-map bytes")\n'
         '    require(sha256(topology_bytes) == EXPECTED_TOPOLOGY_SHA, "bundled topology-readback bytes")\n', "", 1),
        ("C13 retired staging sources absent",
         '    require(\n'
         '        contract["source_snapshot"]["candidate_notion_url_map"]["sha256"] == EXPECTED_URL_MAP_SHA\n'
         '        and contract["source_snapshot"]["candidate_notion_url_map"]["path"] == URL_MAP.relative_to(ROOT).as_posix(),\n'
         '        "bundled URL-map pin",\n'
         '    )\n'
         '    require(\n'
         '        contract["source_snapshot"]["prompt_topology_move_readback"]["sha256"] == EXPECTED_TOPOLOGY_SHA\n'
         '        and contract["source_snapshot"]["prompt_topology_move_readback"]["path"]\n'
         '        == TOPOLOGY_READBACK.relative_to(ROOT).as_posix(),\n'
         '        "bundled topology-readback pin",\n'
         '    )\n',
         '    require(\n'
         '        "candidate_notion_url_map" not in contract["source_snapshot"]\n'
         '        and "prompt_topology_move_readback" not in contract["source_snapshot"],\n'
         '        "no 091426.1 staging source",\n'
         '    )\n', 1),
        ("C14 edge count",
         '    # D15 left 227 edges after the drainage removal re-pointed the qualifying-approval\n'
         "    # branches; D23's two observed-merge edges (Amendment 1, A1-7) make 229. Measured\n"
         '    # against the graph and the contract\'s own declared count, so the two cannot drift apart again.\n'
         '    require(\n        len(graph["edges"]) == 229\n',
         '    # 091426.1 had 229 edges. The MGMT-10 successor\'s part has one edge to NATHAN_TERMINAL_RETURN where the\n'
         f'    # 091426.1 manager had three, so 100926.1 has {m["edge_count"]} (MB-008 PART-05). Measured against the graph and the\n'
         '    # contract\'s own declared count, so the two cannot drift apart again.\n'
         f'    require(\n        len(graph["edges"]) == {m["edge_count"]}\n', 1),
        ("C15 retired staging identity parity",
         '    require(set(member_ids) == set(url_map["members"]), "URL-map/member registry identity parity")\n'
         '    require(\n'
         '        set(member_ids) == {page["stable_id"] for page in topology["pages"]},\n'
         '        "topology/member registry identity parity",\n'
         '    )\n', "", 1),
        ("C16 retired staging binding parity",
         '    require(\n'
         '        all(registry[prompt_id]["notion_url"] == url_map["members"][prompt_id]["url"] for prompt_id in registry),\n'
         '        "bundled URL-map binding parity",\n'
         '    )\n'
         '    topology_by_id = {page["stable_id"]: page for page in topology["pages"]}\n'
         '    require(topology["result"] == "PASS" and len(topology_by_id) == 55, "complete topology readback")\n'
         '    require(\n'
         '        all(\n'
         '            topology_by_id[prompt_id]["page_url"] == registry[prompt_id]["notion_url"]\n'
         '            and topology_by_id[prompt_id]["new_parent"]["page_id"] == registry[prompt_id]["staged_parent_id"]\n'
         '            and topology_by_id[prompt_id]["result"] == "PASS"\n'
         '            for prompt_id in registry\n'
         '        ),\n'
         '        "bundled topology binding parity",\n'
         '    )\n',
         '    require(\n'
         '        all(\n'
         '            registry[prompt_id]["notion_url"] == graph_by_id[prompt_id]["candidate_url"]\n'
         '            for prompt_id in registry\n'
         '        ),\n'
         '        "member Notion URLs are the graph\'s",\n'
         '    )\n', 1),
        ("C17 MB-008 skill clauses",
         '        "Alpha state is what the Epic\'s own artifacts under `docs/ephemeral/` record",\n    ):\n'
         '        require(text in skill, f"missing skill clause: {text}")\n',
         '        "Alpha state is what the Epic\'s own artifacts under `docs/ephemeral/` record",\n'
         '        # MB-008: F01, F02, F07 and F08 as change-flow states them.\n'
         f'        {CF_RECOVERY!r},\n'
         '        "KRONOS_NEVER_EXECUTES_OPS.",\n'
         '        "QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE",\n'
         f'        {TYPESAFE_RULE!r},\n'
         f'        {TYPESAFE_PROCEDURE!r},\n'
         f'        {CF_VERDICTS!r},\n'
         '    ):\n'
         '        require(text in skill, f"missing skill clause: {text}")\n', 1),
        ("C18 MB-008 retired clauses",
         '        "source revision/content identity",\n    ):\n'
         '        require(text.lower() not in skill.lower(), f"retired skill clause present: {text}")\n',
         '        "source revision/content identity",\n'
         '        # MB-008: the retired F02 token and F05 sentence.\n'
         '        "KRONOS_NEVER_EXECUTES_OPS_OR_QA",\n'
         '        "allocate canon numbering",\n'
         '    ):\n'
         '        require(text.lower() not in skill.lower(), f"retired skill clause present: {text}")\n', 1),
        ("C19 result line", 'print("PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy")',
         'print("PASS: change-flow GCFPE-20261009.1 contract and Markdown-only source policy")', 1),
        ("C20 F05 format keys join the closed addendum object",
         '    "standalone_overlay",\n})\n',
         '    "standalone_overlay",\n    "format_expectations",\n'
         + "".join(f'    "format_expectations.{k}",\n' for k in FORMAT_KEYS) + '})\n', 1),
        ("C21 F05 producer numbers its addendum",
         '        set(contract["pf10_addendum_contract"]["exact_producer_set"]) == EXPECTED_PRODUCERS,\n'
         '        "exact PF10 producer set",\n    )\n',
         '        set(contract["pf10_addendum_contract"]["exact_producer_set"]) == EXPECTED_PRODUCERS,\n'
         '        "exact PF10 producer set",\n    )\n'
         '    require(\n'
         '        contract["pf10_addendum_contract"]["producer_allocates_pf10_number"] is True\n'
         '        and contract["pf10_addendum_contract"]["format_expectations"]["number_carrier"].startswith("the H2 heading"),\n'
         '        "the producer numbers its addendum in the H2 heading (F05)",\n'
         '    )\n', 1),
        ("C90 bundled file names", OLD, NEW, 2),
        ("C91 graph contract id", '"GCFPE-20260914.1-CANDIDATE-GRAPH"', '"GCFPE-20261009.1-CANDIDATE-GRAPH"', 1),
    ]


# ------------------------------------------------------------------------- V: suite and current overlay
V_CURRENT_DISPATCH = (
    '    if contract.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
    '        from validate_gcfpe_20260914 import validate_contract as validate_contract_v4\n',
    '    if contract.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
    '        # MB-008 (V5): two releases share schema 4.0; each contract runs its own release\'s profile.\n'
    '        if contract.get("target_release") == "GCFPE-20260914.1":\n'
    '            from validate_gcfpe_20260914 import validate_contract as validate_contract_v4\n'
    '        else:\n'
    '            from validate_gcfpe_20261009 import validate_contract as validate_contract_v4\n',
)


def suite_subs() -> list[tuple[str, str, str, int]]:
    return [
        ("V1a change-flow revision",
         '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1",\n        "For every GCFPE main-ecosystem stage,',
         '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0",\n        "For every GCFPE main-ecosystem stage,', 1),
        ("V1b Kronos pair and V6 change-flow reading rule", '        "KRONOS_NEVER_EXECUTES_OPS_OR_QA",\n',
         '        "KRONOS_NEVER_EXECUTES_OPS",\n        "QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE",\n'
         f'        {TYPESAFE_RULE!r},\n        {TYPESAFE_PROCEDURE!r},\n', 1),
        ("V1c retired Kronos token forbidden",
         '        "KRONOS_EXECUTES_QA",\n        # D22 (ITEM-06, ITEM-16)',
         '        "KRONOS_EXECUTES_QA",\n        # MB-008 (F02, D27): the retired combined token.\n'
         '        "KRONOS_NEVER_EXECUTES_OPS_OR_QA",\n        # D22 (ITEM-06, ITEM-16)', 1),
        ("V1d maintenance mapping",
         '    # The immutable R1 projection also contains two historical package/lifecycle\n'
         '    # metadata anchors. Current PO-authorized GCFPE maintenance supersedes only\n'
         '    # those exact anchors; every runtime row, actor, approval and edge is still\n'
         '    # compared to the unchanged, hash-verified oracle below.\n'
         '    maintenance_metadata = {\n'
         '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0":\n'
         '            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1",\n',
         '    # The immutable R1 projection also contains two historical package/lifecycle\n'
         '    # metadata anchors and, since D27 (MB-008, F02), one superseded Kronos token.\n'
         '    # Current PO-authorized GCFPE maintenance supersedes only those exact anchors;\n'
         '    # every runtime row, actor, approval and edge is still compared to the\n'
         '    # unchanged, hash-verified oracle below. The Kronos token maps to its Ops half;\n'
         '    # its QA half is QA_EXECUTION_ARRANGEMENT, required in CONTRACT_REQUIRED.\n'
         '    maintenance_metadata = {\n'
         '        "CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0":\n'
         '            "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0",\n'
         '        "KRONOS_NEVER_EXECUTES_OPS_OR_QA":\n'
         '            "KRONOS_NEVER_EXECUTES_OPS",\n', 1),
        ("V2 session-relay revision and V6 reading rule",
         '        "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.2.0",\n',
         '        "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.3.0",\n'
         f'        {TYPESAFE_RULE!r},\n        {TYPESAFE_PROCEDURE!r},\n', 1),
        ("V3a self-forbidden profile phrase",
         f'    "references/{OLD}-validation-profile.json": (\n        "complete 55-member prompt corpus",\n    ),\n',
         f'    "references/{OLD}-validation-profile.json": (\n        "complete 55-member prompt corpus",\n    ),\n'
         f'    "references/{NEW}-validation-profile.json": (\n        "complete 55-member prompt corpus",\n    ),\n', 1),
        ("V3b required change-flow files",
         '        "scripts/pf_header_parity.py",\n'
         '        "scripts/validate_gcfpe_20260914.py",\n'
         f'        "references/{OLD}-direct-handoff-contract.json",\n    ),\n',
         '        "scripts/pf_header_parity.py",\n'
         '        "scripts/validate_gcfpe_20261009.py",\n'
         f'        "references/{NEW}-direct-handoff-contract.json",\n'
         f'        "references/{NEW}-candidate-graph-contract.json",\n'
         '        # History (MB-008): the 091426.1 checks and contract stay bundled, superseded.\n'
         '        "scripts/validate_gcfpe_20260914.py",\n'
         f'        "references/{OLD}-direct-handoff-contract.json",\n    ),\n', 1),
        ("V3c required flowmaster-validate files",
         '        "scripts/run_gcfpe_current_fixtures.py",\n'
         '        "scripts/validate_gcfpe_20260914.py",\n',
         '        "scripts/run_gcfpe_current_fixtures.py",\n'
         '        "scripts/validate_gcfpe_20261009.py",\n'
         '        "scripts/run_gcfpe_20261009_fixtures.py",\n'
         f'        "fixtures/{NEW}/scenarios.json",\n'
         f'        "references/{NEW}-validation-profile.json",\n'
         f'        "references/{NEW}-direct-handoff-contract.json",\n'
         f'        "references/{NEW}-candidate-graph-contract.json",\n'
         '        # History (MB-008): the 091426.1 profile, its validator, fixtures, contract and graph.\n'
         '        "scripts/validate_gcfpe_20260914.py",\n', 1),
        ("V3d linked change-flow reference",
         f'        "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json",\n'
         f'        "references/{OLD}-direct-handoff-contract.json",\n    }},\n',
         f'        "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json",\n'
         f'        "references/{NEW}-direct-handoff-contract.json",\n    }},\n', 1),
        ("V4 Kronos QA finding",
         '    if payload.get("kronos_executes_qa"):\n        results.append(\n'
         '            finding("FMV-GCF-ROLE-QA-001", subject, "Kronos performs QA execution")\n        )\n',
         '    # MB-008 (F02, D27): Kronos may execute QA when the Product Owner chose that arrangement.\n'
         '    if payload.get("kronos_executes_qa") and not payload.get("product_owner_chose_qa_arrangement"):\n'
         '        results.append(\n'
         '            finding("FMV-GCF-ROLE-QA-001", subject, "Kronos performs QA execution the Product Owner did not choose")\n'
         '        )\n', 1),
        ("V5a R1 literal-tie validator", 'CANDIDATE_VALIDATOR_RELATIVE = Path("scripts/validate_gcfpe_20260914.py")',
         'CANDIDATE_VALIDATOR_RELATIVE = Path("scripts/validate_gcfpe_20261009.py")', 1),
        ("V5b current overlay",
         '    # The current overlay (the 091426.1 contract, §12 S-5) is always regression-tested\n',
         '    # The current overlay (the 100926.1 contract, MB-008 V5) is always regression-tested\n', 1),
        ("V5c current overlay finding path",
         f'                str(change_dir / "references" / "{OLD}-direct-handoff-contract.json"),\n',
         f'                str(change_dir / "references" / "{NEW}-direct-handoff-contract.json"),\n', 1),
        ("V5d explicit contract dispatch",
         '    if gcfpe_contract is not None:\n'
         '        from validate_gcfpe_20260914 import validate_package as validate_candidate\n'
         '        from run_gcfpe_20260914_fixtures import run as run_candidate_fixtures\n',
         '    if gcfpe_contract is not None:\n'
         '        # MB-008 (V5): an explicit contract runs its own release\'s profile; the 091426.1 profile\n'
         '        # runs only when the 091426.1 contract is passed explicitly.\n'
         '        try:\n'
         '            explicit_release = json.loads(gcfpe_contract.read_text(encoding="utf-8")).get("target_release")\n'
         '        except (OSError, UnicodeError, json.JSONDecodeError, AttributeError):\n'
         '            explicit_release = None\n'
         '        if explicit_release == "GCFPE-20260914.1":\n'
         '            from validate_gcfpe_20260914 import validate_package as validate_candidate\n'
         '            from run_gcfpe_20260914_fixtures import run as run_candidate_fixtures\n'
         '        else:\n'
         '            from validate_gcfpe_20261009 import validate_package as validate_candidate\n'
         '            from run_gcfpe_20261009_fixtures import run as run_candidate_fixtures\n', 1),
        ("V5e explicit fixture labels", '"fixture:GCFPE-20260914.1-091426.1"', 'f"fixture:{explicit_release}"', 3),
        ("V5f candidate-root help", 'help="Candidate root holding graph/GCFPE-20260914.1-Candidate-Graph-Contract.json only; "',
         'help="Candidate root holding only graph/GCFPE-<release>-Candidate-Graph-Contract.json for the contract\'s release; "', 1),
        ("V7a suite revision", '            "validator_revision": "3.3.2",', '            "validator_revision": "3.4.0",', 1),
    ]


def current_subs() -> list[tuple[str, str, str, int]]:
    return [
        ("V5g current validate_contract dispatch", V_CURRENT_DISPATCH[0], V_CURRENT_DISPATCH[1], 1),
        ("V5h current default contract",
         f'    contract_path = contract_path or change_skill_dir / "references" / "{OLD}-direct-handoff-contract.json"\n',
         f'    contract_path = contract_path or change_skill_dir / "references" / "{NEW}-direct-handoff-contract.json"\n', 1),
        ("V5i current validate_package dispatch",
         '    if contract.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
         '        from validate_gcfpe_20260914 import validate_package as validate_package_v4\n',
         '    if contract.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
         '        if contract.get("target_release") == "GCFPE-20260914.1":\n'
         '            from validate_gcfpe_20260914 import validate_package as validate_package_v4\n'
         '        else:\n'
         '            from validate_gcfpe_20261009 import validate_package as validate_package_v4\n', 1),
        ("V2b installed revisions on the schema-3.1 path", "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1",
         "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0", 2),
        ("V2c PR skill revision on the schema-3.1 path", "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1",
         "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.4.0", 1),
    ]


def current_fixture_subs() -> list[tuple[str, str, str, int]]:
    return [
        ("V5j current fixtures default contract",
         f'    contract_path = contract_path or change_skill_dir / "references" / "{OLD}-direct-handoff-contract.json"\n',
         f'    contract_path = contract_path or change_skill_dir / "references" / "{NEW}-direct-handoff-contract.json"\n', 1),
        ("V5k current fixtures dispatch",
         '    if source.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
         '        from run_gcfpe_20260914_fixtures import run as run_v4\n',
         '    if source.get("schema_version") == "gcfpe-direct-handoff-contract/4.0":\n'
         '        # MB-008 (V5): each schema-4 contract runs its own release\'s fixtures.\n'
         '        if source.get("target_release") == "GCFPE-20260914.1":\n'
         '            from run_gcfpe_20260914_fixtures import run as run_v4\n'
         '        else:\n'
         '            from run_gcfpe_20261009_fixtures import run as run_v4\n', 1),
    ]


V4_FIXTURES = [
    {"id": "positive_kronos_qa_execution_product_owner_choice", "expected_pass": True, "expected_rule_ids": [],
     "coverage_mode": "COMPLETE", "kronos_executes_qa": True, "product_owner_chose_qa_arrangement": True,
     "final_qa_report": True, "qa_rca": True, "events": [{"row": "GCF-23"}, {"row": "GCF-24"}]},
    {"id": "negative_kronos_qa_execution_without_product_owner_choice", "expected_pass": False,
     "expected_rule_ids": ["FMV-GCF-ROLE-QA-001"], "coverage_mode": "COMPLETE", "kronos_executes_qa": True,
     "product_owner_chose_qa_arrangement": False, "events": [{"row": "GCF-23"}, {"row": "GCF-24"}]},
]


def write_v4_fixtures(fv: Path, report: list) -> None:
    """Append the two V4 scenarios in the file's own hand layout (one key per line, inline event objects)."""
    path = fv / "fixtures/change-flow/scenarios.json"
    raw = path.read_text(encoding="utf-8")
    ids = {s["id"] for s in json.loads(raw)["scenarios"]}
    if any(s["id"] in ids for s in V4_FIXTURES):
        raise SystemExit("V4 fixtures already present")
    blocks = []
    for s in V4_FIXTURES:
        lines = [f"      {json.dumps(k)}: {json.dumps(v)}" for k, v in s.items()]
        blocks.append("    {\n" + ",\n".join(lines) + "\n    }")
    tail = "\n    }\n  ]\n}\n"
    if raw.count(tail) != 1 or not raw.endswith(tail):
        raise SystemExit("V4 fixtures: the scenarios array does not end as expected")
    text = raw[: -len(tail)] + "\n    },\n" + ",\n".join(blocks) + "\n  ]\n}\n"
    if json.loads(text)["scenarios"][-len(V4_FIXTURES):] != V4_FIXTURES:
        raise SystemExit("V4 fixtures: the appended scenarios do not read back equal")
    path.write_text(text, encoding="utf-8")
    report.append({"substitution": "V4 change-flow fixtures", "file": "flowmaster-validate/fixtures/change-flow/scenarios.json",
                   "count": len(V4_FIXTURES)})


# --------------------------------------------------------------------------- G: the PR skill's validator
def pr_subs() -> list[tuple[str, str, str, int]]:
    return [
        ("G1 revision", '        "revision": "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1",\n',
         '        "revision": "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.4.0",\n'
         f'        # MB-008: the TypeSafe reading (F07), D27 recovery (F01) and producer numbering (F05).\n'
         f'        "reading rule": {TYPESAFE_RULE!r},\n'
         f'        "reading procedure": {TYPESAFE_PROCEDURE!r},\n'
         f'        "D27 recovery": {PR_RECOVERY!r},\n'
         '        "producer numbering": "the responsible producer numbers it at creation from the current controlled PF10 Markdown",\n', 1),
        ("G2 retired F05 sentences",
         '        "package containing the actual finding",\n    ]\n',
         '        "package containing the actual finding",\n'
         '        # MB-008 (F05): the Product Owner pastes; the producer numbers.\n'
         '        "pastes and numbers",\n'
         '        "select final PF10 numbering",\n    ]\n', 1),
    ]


# ------------------------------------------------------------------------------------------ D: docs
def fv_doc_subs(n_total: int) -> list[tuple[str, str, str, int]]:
    return [
        ("D-FV-1 contract binding",
         "The 20260914 candidate contract revision 4.1.1 binds the corrected complete raw-byte repair-plan and PF10 "
         "evidence, the corrected source manifest, and the preserved native recovery/owner graph.",
         "The 100926.1 contract revision 4.2.0 is regenerated from the final candidate graph. It binds its governing "
         "plan as a repository file on `main`, names the selected 091426.1 contract as its predecessor, and carries "
         "forward, as repair-baseline evidence, the raw-byte PF10 pin and corrected source manifest that the 20260914 "
         "contract revision 4.1.1 bound.", 1),
        ("D-FV-2 current overlay",
         f"The current overlay `references/{OLD}-direct-handoff-contract.json` must match that live binding;",
         f"The current overlay `references/{NEW}-direct-handoff-contract.json` must match that live binding;", 1),
        ("D-FV-3 profile",
         "The `GCFPE-20260914.1 / 091426.1` profile pins and re-reads a byte-identical candidate contract and "
         "55-member frozen graph whose sole addition is PR-35.",
         "The `GCFPE-20261009.1 / 100926.1` profile pins and re-reads the bundled production contract and its "
         "55-member frozen graph, which add no member. The `GCFPE-20260914.1 / 091426.1` profile, validator, fixtures, "
         "contract and graph stay bundled as history and run only when that contract is passed explicitly.", 1),
        ("D-FV-4 candidate root",
         "the root holds only `graph/GCFPE-20260914.1-Candidate-Graph-Contract.json`, which must equal the bundled graph",
         "the root holds only the contract release's `graph/GCFPE-<release>-Candidate-Graph-Contract.json`, which must "
         "equal that release's bundled graph", 1),
        ("D-FV-5 suite example",
         f"  --gcfpe-contract /exact/change-flow-skill/references/{OLD}-direct-handoff-contract.json \\\n"
         "  --gcfpe-candidate-root /exact/GCFPE-20260914.1-candidate-root\n",
         f"  --gcfpe-contract /exact/change-flow-skill/references/{NEW}-direct-handoff-contract.json \\\n"
         "  --gcfpe-candidate-root /exact/GCFPE-20261009.1-candidate-root\n", 1),
        ("D-FV-6 direct examples",
         "python3 scripts/validate_gcfpe_20260914.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{OLD}-direct-handoff-contract.json \\\n"
         "  --candidate-root /exact/GCFPE-20260914.1-candidate-root\n"
         "python3 scripts/run_gcfpe_20260914_fixtures.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{OLD}-direct-handoff-contract.json\n",
         "python3 scripts/validate_gcfpe_20261009.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{NEW}-direct-handoff-contract.json \\\n"
         "  --candidate-root /exact/GCFPE-20261009.1-candidate-root\n"
         "python3 scripts/run_gcfpe_20261009_fixtures.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{NEW}-direct-handoff-contract.json\n", 1),
        ("D-FV-7 body example",
         "echo \"$bodies\" | python3 scripts/validate_gcfpe_20260914.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{OLD}-direct-handoff-contract.json \\\n",
         "echo \"$bodies\" | python3 scripts/validate_gcfpe_20261009.py /exact/change-flow-skill \\\n"
         f"  --contract /exact/change-flow-skill/references/{NEW}-direct-handoff-contract.json \\\n", 1),
        ("D-FV-8 default profile",
         "By default the suite validates the 091426.1 current overlay and its schema-4 fixtures; the 54-member "
         "`GCFPE-20260913.1 / 091326.2` alias is validated only when passed explicitly. When both explicit candidate "
         "arguments are supplied, it additionally validates `GCFPE-20260914.1 / 091426.1 / 55`, its byte-pinned "
         "bundled contract and frozen graph, and all 37 section-13 fixtures. Candidate inputs never replace, redirect, "
         "or relax the current-overlay validation, which always runs the 091426.1 contract and its fixtures first.",
         "By default the suite validates the 100926.1 current overlay and its schema-4 fixtures; the 091426.1 contract "
         "and the 54-member `GCFPE-20260913.1 / 091326.2` alias are validated only when passed explicitly, each by its "
         "own release's profile. When both explicit candidate arguments are supplied, it additionally validates that "
         f"contract, its bundled contract and frozen graph, and its fixtures: for 100926.1, all {n_total} (the 37 "
         "section-13 cases and 17 cases for F01, F02, F05, F07, F08 and F09). Candidate inputs never replace, redirect, "
         "or relax the current-overlay validation, which always runs the 100926.1 contract and its fixtures first.", 1),
        ("D-FV-9 fixture report",
         "The fixture report separates 37 required fixture IDs, independent variants, and exact contract-mutation rule "
         "attribution.",
         f"The fixture report separates the {n_total} required fixture IDs, independent variants, exact contract-mutation "
         "rule attribution and, for each MB-008 rule, a case removing the invariant it projects from.", 1),
    ]


def gg_doc_subs() -> list[tuple[str, str, str, int]]:
    return [
        ("D-GG-1 release values",
         "A new\ncontract is written to both bundled copies, and every pin of its digest and\nrevisions moves with it in "
         "the same change.\n",
         "A new\ncontract is written to both bundled copies, and every pin of its digest and\nrevisions moves with it in "
         "the same change.\n\n"
         "A later release's contract is generated the same way from its own build, with\n"
         "`--release-values <file>`: a JSON file of the release's literals that no graph\n"
         "field carries (its predecessor catalog and manager, governing plan, predecessor\n"
         "contract and added members). Member page ids, the Notion page manifest, the\n"
         "five named prompt references, the release and version pairs, the lifecycle\n"
         "values and the PF10 addendum format are derived from the graph. `promoted_at`\n"
         "is carried only when the graph is the template's own release, selected.\n"
         "Generation refuses a file with an unfilled `@` marker or one naming another\n"
         "release. The 100926.1 contracts were generated this way (MB-008); the shipped\n"
         "091426.1 contract still regenerates byte for byte with no file passed.\n", 1),
    ]


# ------------------------------------------------------------------------------------------- build
def build(installed: Path, out: Path, contract: Path, graph: Path, plan: Path) -> dict:
    if "/skills/synced/" in str(installed.resolve()) or "/skills/synced/" in str(out.resolve()):
        raise SystemExit("refusing the synced install directory")
    if out.exists():
        raise SystemExit(f"{out} exists")
    out.mkdir(parents=True)
    report: list = []
    for k in PACKAGES:
        shutil.copytree(installed / k, out / k, ignore=shutil.ignore_patterns("__pycache__"))
    # A: redlines and the glow-graph-contract patch
    applied = subprocess.run([sys.executable, PLAN_DIR / "package_apply.py", out], capture_output=True, text=True, env=ENV)
    if applied.returncode != 0:
        raise SystemExit(f"package_apply: {applied.stdout[-400:]}{applied.stderr[-400:]}")
    report.append({"step": "A redlines", "ops": len(json.loads(applied.stdout)["rows"])})
    patched = subprocess.run(["patch", "-p2", "--batch", "--no-backup-if-mismatch", "-d", out / "glow-graph-contract",
                              "-i", PLAN_DIR / "patches/glow-graph-contract-mb008.patch"],
                             capture_output=True, text=True)
    if patched.returncode != 0:
        raise SystemExit(f"patch: {patched.stdout}{patched.stderr}")
    report.append({"step": "A glow-graph-contract patch", "files": patched.stdout.count("patching file")})
    # A2: the D24 round-1 repair (REVIEW-D24-A R-1, R-2), after the approved redlines have all landed
    landed = subprocess.run([sys.executable, PLAN_DIR / "package_apply.py", out, "--check"], capture_output=True, text=True, env=ENV)
    if landed.returncode != 0 or any(r["state"] != "LANDED" for r in json.loads(landed.stdout)["rows"]):
        raise SystemExit("package_apply --check: not every approved redline landed before the repair")
    repair = json.loads((HERE / "d24-repair-redlines.json").read_text(encoding="utf-8"))["ops"]
    for op in repair:
        substitute(out / op["skill"] / op["file"], [(op["id"], op["old"], op["new"], op["count"])], report)
    cf, fv, pr, gg = out / "change-flow", out / "flowmaster-validate", out / "glow-hde-pr-development", out / "glow-graph-contract"
    # B: bundle
    for k in (cf, fv):
        shutil.copyfile(contract, k / f"references/{NEW}-direct-handoff-contract.json")
        shutil.copyfile(graph, k / f"references/{NEW}-candidate-graph-contract.json")
    # F, P
    fixture_path = write_fixtures(fv)
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    n_pos = sum(s["polarity"] == "POSITIVE" for s in fixtures["scenarios"])
    n_neg = sum(s["polarity"] == "NEGATIVE" for s in fixtures["scenarios"])
    write_profile(fv, fixture_path)
    # M: the profile validator, then the X8 additions
    made = subprocess.run([sys.executable, PLAN_DIR / "make_profile_20261009.py", fv / "scripts/validate_gcfpe_20260914.py",
                           fv / "scripts/validate_gcfpe_20261009.py",
                           "--contract", fv / f"references/{NEW}-direct-handoff-contract.json",
                           "--graph", fv / f"references/{NEW}-candidate-graph-contract.json",
                           "--fixtures", fixture_path, "--plan", plan], capture_output=True, text=True, env=ENV)
    if made.returncode != 0:
        raise SystemExit(f"make_profile: {made.stdout[-600:]}{made.stderr[-600:]}")
    made_report = json.loads(made.stdout)["report"]
    report.append({"step": "M make_profile_20261009.py",
                   "substitutions": sum(1 for r in made_report if "substitution" in r),
                   "measured": next(r["measured"] for r in made_report if "measured" in r)})
    substitute(fv / "scripts/validate_gcfpe_20261009.py", m_additions(len(fixtures["scenarios"])), report)
    # R: the runner
    base_runner = (fv / "scripts/run_gcfpe_20260914_fixtures.py").read_text(encoding="utf-8")
    runner = fv / "scripts/run_gcfpe_20261009_fixtures.py"
    runner.write_text(base_runner, encoding="utf-8")
    subs = runner_subs(base_runner, n_pos, n_neg)
    interim = base_runner
    resolved = []
    for name, old, new, want in subs:
        if want is None:
            want = interim.count(old)
        resolved.append((name, old, new, want))
        interim = interim.replace(old, new)
    substitute(runner, resolved, report)
    # C: change-flow's validator
    base_cf = cf / "scripts/validate_gcfpe_20260914.py"
    cf_mod = load(base_cf, "cf_base_validator_for_surface")
    surface, rows = cf_mod.routing_surface(json.loads(contract.read_text(encoding="utf-8")))
    graph_doc = json.loads(graph.read_text(encoding="utf-8"))
    m = {"graph_sha": sha256(graph), "plan_sha": sha256(plan), "plan_bytes": plan.stat().st_size,
         "plan_path": "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md",
         "surface": surface, "surface_rows": rows, "edge_count": len(graph_doc["edges"])}
    cf_new = cf / "scripts/validate_gcfpe_20261009.py"
    shutil.copyfile(base_cf, cf_new)
    substitute(cf_new, change_flow_subs(m), report)
    report.append({"step": "C measured", "measured": m})
    # V
    substitute(fv / "scripts/validate_flowmaster.py", suite_subs(), report)
    substitute(fv / "scripts/validate_gcfpe_current.py", current_subs(), report)
    substitute(fv / "scripts/run_gcfpe_current_fixtures.py", current_fixture_subs(), report)
    write_v4_fixtures(fv, report)
    # G, D
    substitute(pr / "scripts/validate_glow_hde_pr_development.py", pr_subs(), report)
    substitute(fv / "SKILL.md", fv_doc_subs(len(fixtures["scenarios"])), report)
    substitute(gg / "SKILL.md", gg_doc_subs(), report)
    # I: self-identity, last
    for p in out.rglob("__pycache__"):
        shutil.rmtree(p)
    ident = load(fv / "scripts/validate_gcfpe_20261009.py", "fv_identity")
    text = (fv / "SKILL.md").read_text(encoding="utf-8")
    old_line = next(l for l in text.splitlines() if l.startswith("SKILL_TREE_SHA256: "))
    for p in out.rglob("__pycache__"):
        shutil.rmtree(p)
    digest = ident.skill_tree_digest(fv)
    (fv / "SKILL.md").write_text(text.replace(old_line + "\n", f"SKILL_TREE_SHA256: {digest}\n", 1), encoding="utf-8")
    report.append({"step": "I self-identity", "old": old_line.split()[-1], "new": digest,
                   "verified": not ident.validate_self_identity(fv)})
    return {"fixtures": {"total": len(fixtures["scenarios"]), "positive": n_pos, "negative": n_neg},
            "report": report}


def tree_digest(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): sha256(p) for p in sorted(root.rglob("*")) if p.is_file()}


def main() -> int:
    sys.dont_write_bytecode = True
    ap = argparse.ArgumentParser()
    ap.add_argument("installed"); ap.add_argument("out")
    ap.add_argument("--contract", required=True); ap.add_argument("--graph", required=True)
    ap.add_argument("--plan", required=True); ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    installed, out = Path(a.installed).resolve(), Path(a.out).resolve()
    args = (Path(a.contract).resolve(), Path(a.graph).resolve(), Path(a.plan).resolve())
    if a.check:
        with tempfile.TemporaryDirectory() as tmp:
            result = build(installed, Path(tmp) / "out", *args)
            want, have = tree_digest(Path(tmp) / "out"), tree_digest(out)
        diff = sorted(k for k in set(want) | set(have) if want.get(k) != have.get(k))
        print(json.dumps({"mode": "check", "equal": not diff, "differing": diff, "files": len(have)}, indent=1))
        return 0 if not diff else 1
    result = build(installed, out, *args)
    print(json.dumps({"mode": "build", "out": str(out), **result}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
