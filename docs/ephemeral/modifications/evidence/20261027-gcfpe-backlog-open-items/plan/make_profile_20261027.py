#!/usr/bin/env python3
"""Derive flowmaster-validate's GCFPE-20261027.1 / 102726.1 validator and profile from its 100926.1 validator.

MODIFICATION-20261027-gcfpe-backlog-open-items, PLAN, PART-24 (W7 tooling precedent_scripts M; adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/make_profile_20261009.py). The 100926.1
validator stays in the package unchanged, as history; this writes `validate_gcfpe_20261027.py` beside it. Every
change is a named substitution whose old text must occur exactly the stated number of times, or a named segment
whose old bytes must hash to the pinned digest, so a moved base fails loudly instead of being half-edited. Release
pins that depend on bytes (routing surface, graph, contract, fixtures, the PLAN document) are measured from the
files passed in; successor-dependent values (each member's version, the superseded 100926.1 pages) come from the
successor map; the contract-only literals (QA closure route graph and semantics) from plan/release-values-102726.1.json.
Nothing is typed twice.

  make_profile_20261027.py build <base-validator.py> <out-validator.py> --contract C --graph G --fixtures F
      --plan P --map M [--members-tsv T] [--stand-in-ok] [--profile-base PB --profile-out PO] [--list]
        C and G are the bundled 102726.1 direct-handoff contract and the bundled graph (embedded JSON).
  make_profile_20261027.py dryrun <installed-skills-root> <scratch> --production-md MD --production-contract C
      --r1-dir D --plan P --map M [--stand-in-ok]
        the PLAN dry run: scratch copies of change-flow and flowmaster-validate with the production contract and
        graph bundled, the 2026-10-27 runtime map and EXPECTED_POLICY_20261027 in place (stand-ins for EXECUTE's
        package build), the validator and profile generated, the profile run on the production contract, and each
        new check fired on its injected regression. Prints a receipt; the expected-pending errors are named.

Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("successor_map_102726", HERE / "successor_map_102726.py")
SM = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(SM)

PLAN_PATH_IN_REPO = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md"
NEW_ORACLE = "f1b221e91cd3c22ce9923d555671bce0e7af25335b69dabab60e097f3fa8d46d"
NEW_MAP = "4785525661444c26f2a4521a6409f5986d07f534a605f3d66737a5130c444add"
OLD_ORACLE = "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52"
OLD_MAP = "aa6ed8e34363b77e08e8467d9f31b4dc795c2c9fa2c2c3c7ed1cea6cf4202ee4"
PRED_CONTRACT_SHA = "cd291f17ac832cc0aad62b5cc7e554bd6d524e18de7aea7f2f4fec5a1651317f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def routing_surface(base_validator: Path, contract: dict) -> tuple[str, int]:
    sys.path.insert(0, str(base_validator.parent))
    spec = importlib.util.spec_from_file_location("base_validator_for_surface", base_validator)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.routing_surface(contract)


# ------------------------------------------------------------------------------------------------ new code
QA_CLOSURE_CONTRACT_FN = '''def validate_qa_closure_contract(contract: dict[str, Any]) -> list[str]:
    """Check the close-mutation-set stage and class compatibility (MODIFICATION-20261027 PART-13, PF06 §3.5.1).

    QA-120 PASS goes to CL-05 for both classes; CL-05's CLOSE_PR_READY exits to the class-matching Isis receiver;
    CL-C-10 and CL-E-10 each return a close-mutation-set DO_NOT_CLOSE to CL-05, never to ESC-30."""
    errors: list[str] = []
    stage = "CL-05"
    exits = {"EPIC": "CL-E-10", "CRD": "CL-C-10"}
    errors += subset_errors(contract.get("qa_closure_contract"), {
        "classification_source": "EXISTING_PRODUCT_OWNER_CLASSIFICATION_AND_APPROVED_SPECIFICATION",
        "pass_receivers": {"EPIC": stage, "CRD": stage},
        "close_stage": stage,
        "close_stage_result": "CLOSE_MUTATION_SET_RESULT",
        "close_stage_exit_receivers": exits,
        "close_mutation_set_precedes_closure": True,
        "close_mutation_set_is_post_closure": False,
        "do_not_close_close_mutation_set_route": stage,
        "close_tooling_repair_route": "CL-05_NOT_ESC",
        "epic_close_run_family_admitted": False,
        "required_artifacts": ["QA_REPORT", "QA_RCA"],
        "closure_actor": "Isis",
        "closure_session": "RETAIN_EXISTING",
        "qa_pass_closes_change": False,
        "epic_strategy_card": "EXISTING_APPROVED_SPECIFICATION_STRATEGY_CARD",
        "crd_strategy_card_required": False,
        "unresolved_class_effect": "NATHAN_TERMINAL_RETURN_NO_HANDOFF",
        "unresolved_receiver_evidence_effect": "NATHAN_TERMINAL_RETURN_NO_HANDOFF",
        "valid_result_reuse": True,
    }, "QA_CLOSURE_CONTRACT")
    state_routes = contract.get("state_routes") or {}
    edges = [e for e in contract.get("route_edges", []) if isinstance(e, dict)]
    registry = contract.get("member_registry") or {}
    routes = state_routes.get("QA-120", [])
    passes = [r for r in routes if isinstance(r, dict) and "PASS" in r.get("applicable_states", [])]
    if len(passes) != 2 or {r.get("change_class") for r in passes} != set(exits):
        errors.append("QA_PASS_CLASS_ROUTES")
    for cls in exits:
        matches = [r for r in passes if r.get("change_class") == cls]
        if len(matches) != 1:
            continue
        row = matches[0]
        if (row.get("state") != "PASS" or row.get("destinations") != [stage]
                or row.get("required_artifacts") != ["QA_REPORT", "QA_RCA"]
                or row.get("next_prompt_handoff_count") != 1
                or row.get("terminal_for_invocation") is not False):
            errors.append("QA_PASS_CLASS_ROUTES")
        matching_edges = [e for e in edges if e.get("from") == "QA-120"
                          and any(b.get("branch_id") == row.get("branch_id")
                                  for b in e.get("route_branches", []) if isinstance(b, dict))]
        if len(matching_edges) != 1 or matching_edges[0].get("to") != stage:
            errors.append("QA_PASS_CLASS_EDGES")
        elif not any(b.get("change_class") == cls
                     and b.get("required_artifacts") == ["QA_REPORT", "QA_RCA"]
                     for b in matching_edges[0].get("route_branches", [])):
            errors.append("QA_PASS_CLASS_EDGES")
    if any(e.get("from") == "QA-120" and e.get("to") in exits.values() for e in edges):
        errors.append("QA_PASS_CLASS_EDGES")
    member = registry.get(stage, {}) if isinstance(registry.get(stage), dict) else {}
    if (member.get("session_class") != "DEDICATED_ONE_OFF"
            or "Close Implementer" not in member.get("receiving_role", "")
            or "CLOSE_MUTATION_SET_RESULT" not in member.get("output_artifacts", [])):
        errors.append("QA_PASS_RECEIVER_CONTRACT")
    for destination in exits.values():
        receiver = registry.get(destination, {}) if isinstance(registry.get(destination), dict) else {}
        if (receiver.get("session_class") != "ROLE_CONTINUING"
                or "Isis" not in receiver.get("receiving_role", "")
                or "CHANGE_CLOSURE_DECISION" not in receiver.get("output_artifacts", [])):
            errors.append(f"QA_CLOSE_EXIT_RECEIVER_CONTRACT:{destination}")
    ready = sorted((str(r.get("change_class")), tuple(r.get("destinations") or []))
                   for r in state_routes.get(stage, []) if isinstance(r, dict) and r.get("state") == "CLOSE_PR_READY")
    exit_edges = sorted(e.get("to") for e in edges if e.get("from") == stage and e.get("state_predicates") == ["CLOSE_PR_READY"])
    if ready != [("CRD", ("CL-C-10",)), ("EPIC", ("CL-E-10",))] or exit_edges != ["CL-C-10", "CL-E-10"]:
        errors.append("CL05_CLOSE_EXIT_ROUTES")
    for destination in exits.values():
        back = [b for e in edges if e.get("from") == destination and e.get("to") == stage
                for b in e.get("route_branches", []) if isinstance(b, dict) and b.get("state") == "DO_NOT_CLOSE"]
        if len(back) != 1:
            errors.append(f"DO_NOT_CLOSE_CLOSE_SET_ROUTE:{destination}")
    categories = (contract.get("artifact_availability_contract") or {}).get("stage_categories") or {}
    if categories.get(stage) != "CLOSE_MUTATION_SET":
        errors.append("CLOSE_STAGE_CATEGORY")
    return sorted(set(errors))


'''

QA_CLOSURE_BODIES_BLOCK = '''_CODE_OPEN, _CODE_CLOSE = r"(?:`|<code>)", r"(?:`|</code>)"
QA_PASS_ROW_PIPE_RE = re.compile(
    r"(?m)^\\|\\s*" + _CODE_OPEN + r"PASS" + _CODE_CLOSE + r"\\s*\\|\\s*" + _CODE_OPEN + r"(EPIC|CRD)" + _CODE_CLOSE
    + r"\\s*\\|\\s*" + _CODE_OPEN + r"(CL-05) — [^`<]+" + _CODE_CLOSE + r"\\s+at\\s+(.+?),\\s+which exits to\\s+"
    + _CODE_OPEN + r"(CL-[EC]-10) — [^`<]+" + _CODE_CLOSE + r"\\s*\\|$"
)
QA_PASS_ROW_HTML_RE = re.compile(
    r"<tr>\\s*<td>\\s*" + _CODE_OPEN + r"PASS" + _CODE_CLOSE + r"\\s*</td>\\s*<td>\\s*" + _CODE_OPEN + r"(EPIC|CRD)"
    + _CODE_CLOSE + r"\\s*</td>\\s*<td>\\s*" + _CODE_OPEN + r"(CL-05) — [^`<]+" + _CODE_CLOSE
    + r"\\s+at\\s+(.*?),\\s+which exits to\\s+" + _CODE_OPEN + r"(CL-[EC]-10) — [^`<]+" + _CODE_CLOSE
    + r"\\s*</td>\\s*</tr>",
    re.S,
)
CLOSE_SET_REPAIR_SENTENCE_RE = re.compile(r"(?i)close-tooling defect is CL-05's to repair, not ESC-30 work")


def qa_pass_class_rows(producer: str) -> list[tuple[str, str, str, str]]:
    """QA-120's PASS class map: (class, close stage, destination field, exit receiver), in either rendering.

    MODIFICATION-20261027 PART-13: each PASS row names CL-05 at its page and the class-matching Isis receiver it
    exits to. The destination field is resolved to a page identity by the caller, never compared as text."""

    rows = [m.groups() for m in QA_PASS_ROW_PIPE_RE.finditer(producer)]
    rows += [m.groups() for m in QA_PASS_ROW_HTML_RE.finditer(producer)]
    return rows


def validate_qa_closure_bodies(bodies: dict[str, str], contract: dict[str, Any]) -> list[str]:
    """Compare the producer's class table with the close stage and both complete native intakes."""
    errors: list[str] = []
    producer = bodies.get("QA-120", "")
    exits = {"EPIC": "CL-E-10", "CRD": "CL-C-10"}
    rows = qa_pass_class_rows(producer)
    if len(rows) != 2 or {r[0]: (r[1], r[3]) for r in rows} != {c: ("CL-05", d) for c, d in exits.items()}:
        errors.append("QA_PASS_BODY_CLASS_MAP")
    expected_identity = notion_page_identity(
        (contract.get("member_registry") or {}).get("CL-05", {}).get("notion_url") or ""
    )
    for _cls, _stage, url_field, _exit in rows:
        if not expected_identity or notion_page_identity(url_field) != expected_identity:
            errors.append("QA_PASS_BODY_CLASS_MAP")
    if ("class evidence is missing or conflicting" not in producer
            or "without a closure handoff" not in producer
            or "Do not infer a class" not in producer):
        errors.append("QA_CLASS_UNRESOLVED_HANDOFF")
    if any(marker not in producer for marker in (
        "`QA_REPORT_ID`", "`QA_RCA_ID`", "Implementation Plan/review",
        "Ops receipts/documentation completion", "QA-10 Reality Audit",
        "Change Audit Triage", "continuing Isis", "existing Strategy Card",
        "A CRD has no Strategy Card requirement.",
    )):
        errors.append("QA_PASS_BODY_INTAKE")
    for cls, destination in exits.items():
        receiver = bodies.get(destination, "")
        label = "Epic" if cls == "EPIC" else "CRD"
        if (f"complete approved `{label}` Specification" not in receiver
                or f"Confirm exact `{cls}` class/change" not in receiver
                or any(token not in receiver for token in (
                    "`QA_REPORT_ID`", "`QA_RCA_ID`", "You are Isis, continuing",
                    "`artifact_type: CHANGE_CLOSURE_DECISION`", "`decision: DO_NOT_CLOSE`",
                ))):
            errors.append(f"QA_PASS_RECEIVER_BODY:{destination}")
        if not CLOSE_SET_REPAIR_SENTENCE_RE.search(receiver):
            errors.append(f"QA_CLOSE_SET_REPAIR_ROUTE_BODY:{destination}")
    return sorted(set(errors))


'''

BINDING_CHECK = '''            errors.append(f"PROMPT_FORBIDDEN_REFERENCE:{prompt_id}")
        # G-W7-BIND-1 (D23-B with D23-G; PF04 §9.1.6): no body binds the superseded 100926.1 page of a member that
        # has a 102726.1 successor. The superseded pages come from the successor-page map, never typed.
        cited = {re.sub(r"-", "", m).lower() for m in NOTION_PAGE_IN_TEXT_RE.findall(text)}
        for superseded_member, superseded_page in sorted(SUPERSEDED_MEMBER_PAGES.items()):
            if superseded_page in cited:
                errors.append(f"PROMPT_BINDING_SUPERSEDED:{prompt_id}:{superseded_member}")
'''


def substitutions(m: dict) -> list[tuple]:
    """(name, old, new, expected count) or ("segment", name, start, end, old-sha256, new)."""
    rv = m["rv_ops"]
    rule = json.dumps(m["member_rule"], ensure_ascii=False)
    versions = ",\n".join(f'    "{k}": "{v}"' for k, v in sorted(m["versions"].items()))
    superseded = ",\n".join(f'    "{k}": "{v}"' for k, v in sorted(m["superseded"].items()))
    epic_route = json.dumps(rv[("route_graph", "epic_qa_pass_closure")])
    crd_route = json.dumps(rv[("route_graph", "crd_qa_pass_closure")])
    qa_sem = json.dumps(rv[("route_graph_semantics", "qa_pass_closure")], ensure_ascii=False)
    return [
        ("S01 module title", 'Validate the versioned GCFPE-20261009.1 / 100926.1 contract (derived from the 091426.1 validator, F06).',
         'Validate the versioned GCFPE-20261027.1 / 102726.1 contract (derived from the 100926.1 validator, '
         'MODIFICATION-20261027-gcfpe-backlog-open-items).', 1),
        ("S02 artifact timing import",
         "from validate_gcfpe_artifact_timing import validate_artifact_timing_contract, validate_artifact_timing_bodies",
         "from validate_gcfpe_artifact_timing import (EXPECTED_POLICY_20261027, validate_artifact_timing_contract,\n"
         "                                            validate_artifact_timing_bodies)", 1),
        ("S03 CL-05 joins the members", '    "CL-20", "CL-30", "CL-40", "CL-C-10",',
         '    "CL-05", "CL-20", "CL-30", "CL-40", "CL-C-10",', 1),
        ("S04 member versions and superseded pages from the successor map",
         'EXPECTED_PRODUCERS = {"CF-C-30"',
         "# From the successor-page map (W7-D8; C-1): 102726.1 for SUCCESSOR and ADDED members, 100926.1 for KEPT.\n"
         "EXPECTED_MEMBER_VERSIONS = {\n" + versions + ",\n}\n"
         "# The 100926.1 page of every member with a 102726.1 successor (G-W7-BIND-1); a body naming one is stale.\n"
         "SUPERSEDED_MEMBER_PAGES = {\n" + superseded + ",\n}\n"
         'NOTION_PAGE_IN_TEXT_RE = re.compile(r"app\\.notion\\.com/p/([0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?'
         '[0-9a-fA-F]{4}-?[0-9a-fA-F]{12})")\n'
         'EXPECTED_PRODUCERS = {"CF-C-30"', 1),
        ("S05 routing surface pin",
         'EXPECTED_ROUTING_SURFACE = "d3a08833964a2610f88bd754b7e7510d"\nEXPECTED_ROUTING_SURFACE_ROWS = 290',
         f'EXPECTED_ROUTING_SURFACE = "{m["surface"]}"\nEXPECTED_ROUTING_SURFACE_ROWS = {m["surface_rows"]}', 1),
        ("S06 merge-pending real-input P1 (C-7)",
         '    "resolved current-head reviews", "resolved required review threads",\n',
         '    "resolved current-head reviews", "resolved required review threads", "no open P1 thread on a real input",\n', 1),
        ("S07 qa_pass_closure semantics (release values)",
         '    "qa_pass_closure": "Verified EPIC PASS routes directly to CL-E-10; verified CRD PASS routes directly to CL-C-10. '
         'Both carry separate QA Report/RCA and the complete matching intake to continuing Isis. Unresolved class or '
         'receiver evidence returns terminally to Nathan with no handoff; QA never decides closure.",',
         f'    "qa_pass_closure": {qa_sem},', 1),
        ("S08 bundled byte pins",
         'EXPECTED_FROZEN_GRAPH_SHA256 = "43f84f29b9921c21f63ffbe21dd36a14bd846a89ae697ba3cf38746c2f887eb1"\n'
         'EXPECTED_FROZEN_GRAPH_BYTES = 593569\n'
         'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "cd291f17ac832cc0aad62b5cc7e554bd6d524e18de7aea7f2f4fec5a1651317f"\n'
         'EXPECTED_CANDIDATE_CONTRACT_BYTES = 631061\n'
         'EXPECTED_FIXTURE_SHA256 = "e24c881d03c2286ee404c098dd5ae26e530e62f37102a179d72cb0c70c277ef4"',
         f'EXPECTED_FROZEN_GRAPH_SHA256 = "{m["graph_sha"]}"\n'
         f'EXPECTED_FROZEN_GRAPH_BYTES = {m["graph_bytes"]}\n'
         f'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "{m["contract_sha"]}"\n'
         f'EXPECTED_CANDIDATE_CONTRACT_BYTES = {m["contract_bytes"]}\n'
         f'EXPECTED_FIXTURE_SHA256 = "{m["fixture_sha"]}"', 1),
        ("S09 profile identity", '        "validator_revision": "3.4.1",', '        "validator_revision": "3.5.0",', 1),
        ("S10 profile release and staging identity",
         '        "target_release": "GCFPE-20261009.1",\n        "prompt_version": "100926.1",\n'
         '        "candidate_member_count": 55,\n'
         '        "selected_release_during_staging": "GCFPE-20260914.1",\n'
         '        "selected_prompt_version_during_staging": "091426.1",\n'
         '        "selected_member_count_during_staging": 55,\n    }, "PROFILE_IDENTITY")',
         '        "target_release": "GCFPE-20261027.1",\n        "prompt_version": "102726.1",\n'
         '        "candidate_member_count": 56,\n'
         '        "selected_release_during_staging": "GCFPE-20261009.1",\n'
         '        "selected_prompt_version_during_staging": "100926.1",\n'
         '        "selected_member_count_during_staging": 55,\n    }, "PROFILE_IDENTITY")', 1),
        ("S11 profile graph counts", '        "node_count": 55,\n        "edge_count": 235,',
         f'        "node_count": {m["node_count"]},\n        "edge_count": {m["edge_count"]},', 1),
        ("S12 profile fixture count", '"schema_version": "gcfpe-scenarios/2.0", "count": 54,',
         f'"schema_version": "gcfpe-scenarios/2.0", "count": {m["fixture_count"]},', 1),
        ("S13 profile R1 pins",
         f'        "r1_oracle_sha256": "{OLD_ORACLE}",\n        "r1_runtime_map_sha256": "{OLD_MAP}",\n'
         '        "r1_rows": 46,\n    }, "PROFILE_PROTECTED_IDENTITIES")',
         f'        "r1_oracle_sha256": "{NEW_ORACLE}",\n        "r1_runtime_map_sha256": "{NEW_MAP}",\n'
         '        "r1_rows": 47,\n    }, "PROFILE_PROTECTED_IDENTITIES")', 1),
        ("S14 graph candidate and baseline profile",
         '        "release": "GCFPE-20261009.1",\n        "version_family": "100926.1",\n        "member_count": 55,\n'
         '        "member_rule": "54 successor runtime members + the GCFPE-MGMT-10 successor (D20 three-mode body); no additions '
         'or removals",\n    }, "GRAPH_CANDIDATE_PROFILE")\n'
         '    errors += subset_errors(graph.get("baseline"), {\n        "release": "GCFPE-20260914.1",\n'
         '        "version_family": "091426.1",\n        "member_count": 55,\n    }, "GRAPH_BASELINE_PROFILE")',
         '        "release": "GCFPE-20261027.1",\n        "version_family": "102726.1",\n        "member_count": 56,\n'
         f'        "member_rule": {rule},\n    }}, "GRAPH_CANDIDATE_PROFILE")\n'
         '    errors += subset_errors(graph.get("baseline"), {\n        "release": "GCFPE-20261009.1",\n'
         '        "version_family": "100926.1",\n        "member_count": 55,\n    }, "GRAPH_BASELINE_PROFILE")', 1),
        ("S15 graph node count", 'if len(nodes) != 55 or len(graph_nodes) != 55 or set(graph_nodes) != EXPECTED_MEMBERS:',
         'if len(nodes) != 56 or len(graph_nodes) != 56 or set(graph_nodes) != EXPECTED_MEMBERS:', 1),
        ("S16 graph proofs: node count", 'proofs.get("candidate_node_count") != 55',
         'proofs.get("candidate_node_count") != 56', 1),
        ("S17 graph proofs: CL-05 added", '        or proofs.get("sole_added_node") != []',
         '        or proofs.get("sole_added_node") != ["CL-05"]', 1),
        ("S18 graph protected identities",
         f'        "r1_material_rows": 20,\n        "r1_oracle_sha256": "{OLD_ORACLE}",\n        "r1_rows": 46,\n    }}:',
         f'        "r1_material_rows": 21,\n        "r1_oracle_sha256": "{NEW_ORACLE}",\n        "r1_rows": 47,\n    }}:', 1),
        ("S19 historical references gain the 2026-09-23 pair (C-11)",
         '    "glow-hde-canonical-change-flow-r1-runtime-map.json",\n})',
         '    "glow-hde-canonical-change-flow-r1-runtime-map.json",\n'
         '    "glow-hde-canonical-change-flow-r1-20260923.json",\n'
         '    "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json",\n})', 1),
        ("S20 contract identity",
         '        "contract_revision": "4.2.0",\n        "target_release": "GCFPE-20261009.1",\n'
         '        "predecessor_release": "GCFPE-20260914.1",\n        "prompt_version": "100926.1",\n'
         '        "predecessor_prompt_version": "091426.1",\n        "candidate_member_count": 55,\n'
         '        "selected_member_count_during_staging": 55,\n'
         '        "selected_release_during_staging": "GCFPE-20260914.1",\n'
         '        "selected_prompt_version_during_staging": "091426.1",\n        "sole_added_member": None,',
         '        "contract_revision": "4.3.0",\n        "target_release": "GCFPE-20261027.1",\n'
         '        "predecessor_release": "GCFPE-20261009.1",\n        "prompt_version": "102726.1",\n'
         '        "predecessor_prompt_version": "100926.1",\n        "candidate_member_count": 56,\n'
         '        "selected_member_count_during_staging": 55,\n'
         '        "selected_release_during_staging": "GCFPE-20261009.1",\n'
         '        "selected_prompt_version_during_staging": "100926.1",\n        "sole_added_member": "CL-05",', 1),
        ("S21 contract ids", 'contract.get("contract_id") != "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-',
         'contract.get("contract_id") != "GCFPE-20261027.1-102726.1-DIRECT-HANDOFF-', 2),
        ("S22 selected member count", 'or contract.get("selected_member_count") != 55',
         'or contract.get("selected_member_count") != 56', 1),
        ("S23 member set", 'len(members) != 55 or len(set(members)) != 55', 'len(members) != 56 or len(set(members)) != 56', 1),
        ("S24 member version from the map", 'or member.get("version") != "100926.1"',
         'or member.get("version") != EXPECTED_MEMBER_VERSIONS.get(prompt_id)', 1),
        ("S25 manifest page version from the map", 'or page.get("version") != "100926.1"',
         'or page.get("version") != EXPECTED_MEMBER_VERSIONS.get(prompt_id)', 1),
        ("S26 governing plan and predecessor contract pins",
         '        "sha256": "4de47784d63a895fe002283965032844409a247f7c8d0c4632c97c8b9dcd4d5b",\n'
         '        "byte_count": 50156,\n        "representation": "REPOSITORY_FILE_ON_MAIN",\n'
         '        "repository_path": "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md",\n'
         '    }, "REPAIR_PLAN_SOURCE_PIN")\n'
         '    errors += subset_errors(source_snapshot.get("predecessor_direct_handoff_contract"), {\n'
         '        "contract_id": "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED",\n'
         '        "sha256": "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c",',
         f'        "sha256": "{m["plan_sha"]}",\n'
         f'        "byte_count": {m["plan_bytes"]},\n        "representation": "REPOSITORY_FILE_ON_MAIN",\n'
         f'        "repository_path": "{PLAN_PATH_IN_REPO}",\n'
         '    }, "REPAIR_PLAN_SOURCE_PIN")\n'
         '    errors += subset_errors(source_snapshot.get("predecessor_direct_handoff_contract"), {\n'
         '        "contract_id": "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-SELECTED",\n'
         f'        "sha256": "{PRED_CONTRACT_SHA}",', 1),
        ("S27 PR skill revision in the contract", '"primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.4.0",',
         '"primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.5.0",', 1),
        ("S28 abort prompt version from the map", '"id": "PR-50", "version": "100926.1",',
         '"id": "PR-50", "version": EXPECTED_MEMBER_VERSIONS["PR-50"],', 1),
        ("S29 QA closure route graph (release values)",
         '        "epic_qa_pass_closure": ["QA-120", "CL-E-10", "CL-20"],\n'
         '        "crd_qa_pass_closure": ["QA-120", "CL-C-10", "CL-20"],',
         f'        "epic_qa_pass_closure": {epic_route},\n        "crd_qa_pass_closure": {crd_route},', 1),
        ("S30 PR40_MANUAL_MERGE_BOUNDARY: no prompt-originated recovery entry (W1, CD-1)",
         '        or any(\n            edge.get("from") != "DOC-20"\n            or edge.get("automatic") is not False\n'
         '            or not edge.get("route_branches")\n            or any(\n'
         '                "after Nathan asserts the manual merge" not in str(branch.get("condition", ""))\n'
         '                for branch in edge.get("route_branches", [])\n                if isinstance(branch, dict)\n'
         '            )\n            for edge in recovery_pr40\n        )\n',
         '        # MODIFICATION-20261027 PART-08 (CD-1): no prompt-originated PR-40 entry but the two observed-merge edges.\n'
         '        or bool(recovery_pr40)\n', 1),
        ("S31 contract graph proofs member count", '"member_count": 55, "unique_member_ids": True,',
         '"member_count": 56, "unique_member_ids": True,', 1),
        ("S32 contract protected identities",
         f'        "r1_core_rows": 26, "r1_material_rows": 20,\n        "r1_oracle_sha256": "{OLD_ORACLE}",\n'
         '        "r1_rows": 46, "flowmaster_primary_core_changed": False,',
         f'        "r1_core_rows": 26, "r1_material_rows": 21,\n        "r1_oracle_sha256": "{NEW_ORACLE}",\n'
         '        "r1_rows": 47, "flowmaster_primary_core_changed": False,', 1),
        ("S33 artifact timing policy 20261027 (W7-D4)", "errors.extend(validate_artifact_timing_contract(contract))",
         "errors.extend(validate_artifact_timing_contract(contract, EXPECTED_POLICY_20261027))", 1),
        ("S34 PR skill revision marker", '"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.4.0", "REMOTE_EVIDENCE_PENDING",',
         '"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.5.0", "REMOTE_EVIDENCE_PENDING",', 1),
        ("S35 R1 runtime map pin",
         'runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"\n'
         f'    if not runtime_map.is_file() or sha256(runtime_map) != "{OLD_MAP}":',
         'runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20261027.json"\n'
         f'    if not runtime_map.is_file() or sha256(runtime_map) != "{NEW_MAP}":', 1),
        ("S36 PROMPT_BINDING_SUPERSEDED body check (G-W7-BIND-1)",
         '            errors.append(f"PROMPT_FORBIDDEN_REFERENCE:{prompt_id}")\n', BINDING_CHECK, 1),
        ("segment", "S37 QA closure contract: the close-mutation-set stage (W5)",
         "def validate_qa_closure_contract(contract: dict[str, Any]) -> list[str]:\n", "QA_PASS_ROW_PIPE_RE = re.compile(",
         m["seg_contract_sha"], QA_CLOSURE_CONTRACT_FN),
        ("segment", "S38 QA closure bodies: CL-05 rows and the close-set repair sentence (W5)",
         "QA_PASS_ROW_PIPE_RE = re.compile(", "# The two rows the approved registry does NOT require",
         m["seg_bodies_sha"], QA_CLOSURE_BODIES_BLOCK),
        # Release-wide literal renames. Each count is the base's own; a changed base fails here.
        ("S90 bundled file names", "gcfpe-20261009.1-100926.1", "gcfpe-20261027.1-102726.1", m["n_file"]),
        ("S91 graph file name", "GCFPE-20261009.1-Candidate-Graph-Contract.json",
         "GCFPE-20261027.1-Candidate-Graph-Contract.json", m["n_graphfile"]),
        ("S92 profile id", '"GCFPE-20261009.1-100926.1-VALIDATION"', '"GCFPE-20261027.1-102726.1-VALIDATION"', 1),
        ("S93 graph contract id", '"GCFPE-20261009.1-CANDIDATE-GRAPH"', '"GCFPE-20261027.1-CANDIDATE-GRAPH"', 1),
    ]


def segment(src: str, start: str, end: str) -> tuple[int, int]:
    assert src.count(start) == 1 and src.count(end) == 1, (start, end)
    i, j = src.index(start), src.index(end)
    assert i < j
    return i, j


def measure(base: Path, contract_path: Path, graph_path: Path, fixtures: Path, plan: Path, smap: dict,
            rv_path: Path) -> dict:
    src = base.read_text(encoding="utf-8")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    surface, rows = routing_surface(base, contract)
    rv = json.loads(rv_path.read_text(encoding="utf-8"))
    versions, superseded = {}, {}
    for pid, row in smap["members"].items():
        versions[pid] = "100926.1" if row["disposition"] == "KEPT" else "102726.1"
        if row["disposition"] == "SUCCESSOR":
            superseded[pid] = row["predecessor_page_id"]
    a, b = segment(src, "def validate_qa_closure_contract(contract: dict[str, Any]) -> list[str]:\n",
                   "QA_PASS_ROW_PIPE_RE = re.compile(")
    c, d = segment(src, "QA_PASS_ROW_PIPE_RE = re.compile(", "# The two rows the approved registry does NOT require")
    return {
        "surface": surface, "surface_rows": rows,
        "graph_sha": sha256(graph_path), "graph_bytes": graph_path.stat().st_size,
        "contract_sha": sha256(contract_path), "contract_bytes": contract_path.stat().st_size,
        "fixture_sha": sha256(fixtures),
        "fixture_count": len(json.loads(fixtures.read_text(encoding="utf-8"))["scenarios"]),
        "edge_count": len(graph["edges"]), "node_count": len(graph["nodes"]),
        "member_rule": graph["candidate"]["member_rule"],
        "plan_sha": sha256(plan), "plan_bytes": plan.stat().st_size,
        "versions": versions, "superseded": superseded,
        "rv_ops": {tuple(op[1]): op[2] for op in rv["ops"] if op[0] == "set"},
        "seg_contract_sha": hashlib.sha256(src[a:b].encode("utf-8")).hexdigest(),
        "seg_bodies_sha": hashlib.sha256(src[c:d].encode("utf-8")).hexdigest(),
        "n_file": src.count("gcfpe-20261009.1-100926.1"),
        "n_graphfile": src.count("GCFPE-20261009.1-Candidate-Graph-Contract.json"),
        "stand_in_used": smap.get("stand_in") is True,
    }


# Pinned from the installed 100926.1 validator (flowmaster-validate 3.4.1), measured 2026-10-27 in PLAN.
# Base file validate_gcfpe_20261009.py sha256 31387584b0e4cc0fe822eae4c99b3e350d97366086b1c10f908ea460d608a7a0.
PINNED_SEGMENTS = {"seg_contract_sha": "566cbe4672dd20cf1acd399d7fda0a96e6bf30a086c53e1c417f520f7bd1248f",
                   "seg_bodies_sha": "dd5082a1b08fb90ecb9d26df734d1756857810b86fc0f65c6ffa0c9b3e1d5b1e"}


def build(base: Path, contract_path: Path, graph_path: Path, fixtures: Path, plan: Path, smap: dict,
          rv_path: Path) -> tuple[str, list, dict]:
    src = base.read_text(encoding="utf-8")
    m = measure(base, contract_path, graph_path, fixtures, plan, smap, rv_path)
    for key, pinned in PINNED_SEGMENTS.items():
        if m[key] != pinned:
            raise SystemExit(f"{key}: base segment digest {m[key]} differs from the pinned {pinned}")
    out, report = src, []
    for sub in substitutions(m):
        if sub[0] == "segment":
            _, name, start, end, want, new = sub
            a, b = segment(out, start, end)
            got = hashlib.sha256(out[a:b].encode("utf-8")).hexdigest()
            if got != want:
                raise SystemExit(f"{name}: segment digest {got}, expected {want}")
            out = out[:a] + new + out[b:]
            report.append({"substitution": name, "segment_sha256": got})
            continue
        name, old, new, want = sub
        got = out.count(old)
        if got != want:
            raise SystemExit(f"{name}: expected {want} occurrence(s), found {got}")
        out = out.replace(old, new)
        report.append({"substitution": name, "count": got})
    left = {k: out.count(k) for k in ("GCFPE-20260914.1", "091426.1", OLD_ORACLE, OLD_MAP, "\"3.4.1\"", "100926.1")}
    return out, report, {"measured": {k: v for k, v in m.items() if k not in ("rv_ops", "versions", "superseded")
                                      and not k.startswith("n_")},
                         "successor_members": len(m["superseded"]), "kept_members": sorted(
                             k for k, v in m["versions"].items() if v == "100926.1"),
                         "leftover_literal_counts": left}


def make_profile(base_profile: Path, out: Path, contract_path: Path, graph_path: Path, fixtures: Path) -> dict:
    prof = json.loads(base_profile.read_text(encoding="utf-8"))
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    prof.update(profile_id="GCFPE-20261027.1-102726.1-VALIDATION", prompt_version="102726.1",
                target_release="GCFPE-20261027.1", candidate_member_count=56,
                selected_member_count_during_staging=55, selected_prompt_version_during_staging="100926.1",
                selected_release_during_staging="GCFPE-20261009.1", validator_revision="3.5.0",
                installed_skill_revisions={"change-flow": "3.5.0", "glow-hde-pr-development": "1.5.0"})
    prof["candidate_contract"].update(
        bundled_relative_path="references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json",
        relative_to_change_flow="references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json",
        byte_count=contract_path.stat().st_size, sha256=sha256(contract_path))
    prof["frozen_graph"].update(
        bundled_relative_path="references/gcfpe-20261027.1-102726.1-candidate-graph-contract.json",
        relative_to_candidate_root="graph/GCFPE-20261027.1-Candidate-Graph-Contract.json",
        byte_count=graph_path.stat().st_size, sha256=sha256(graph_path), edge_count=len(graph["edges"]),
        node_count=len(graph["nodes"]))
    prof["fixtures"].update(relative_path="fixtures/gcfpe-20261027.1-102726.1/scenarios.json", sha256=sha256(fixtures),
                            count=len(json.loads(fixtures.read_text(encoding="utf-8"))["scenarios"]))
    prof["protected_identities"].update(r1_oracle_sha256=NEW_ORACLE, r1_runtime_map_sha256=NEW_MAP, r1_rows=47)
    out.write_text(json.dumps(prof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"profile": str(out), "sha256": sha256(out), "bytes": out.stat().st_size}


def cmd_build(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="make_profile_20261027.py build")
    ap.add_argument("base"); ap.add_argument("out")
    for k in ("--contract", "--graph", "--fixtures", "--plan", "--map"):
        ap.add_argument(k, required=True)
    ap.add_argument("--members-tsv", default=str(HERE / "members-100926.1.tsv"))
    ap.add_argument("--release-values", default=str(HERE / "release-values-102726.1.json"))
    ap.add_argument("--stand-in-ok", action="store_true")
    ap.add_argument("--profile-base"); ap.add_argument("--profile-out")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args(argv)
    smap = SM.load(a.map, a.members_tsv, a.stand_in_ok)
    text, report, info = build(Path(a.base), Path(a.contract), Path(a.graph), Path(a.fixtures), Path(a.plan), smap,
                               Path(a.release_values))
    res = {"written": None if a.list else a.out, "report": report, **info,
           "stand_in_used": smap.get("stand_in") is True}
    if not a.list:
        Path(a.out).write_text(text, encoding="utf-8")
        res["validator_sha256"] = sha256(Path(a.out))
        if a.profile_base and a.profile_out:
            res["profile_written"] = make_profile(Path(a.profile_base), Path(a.profile_out), Path(a.contract),
                                                  Path(a.graph), Path(a.fixtures))
    print(json.dumps(res, indent=1))
    return 0


# ------------------------------------------------------------------------------------------------ dry run
def _graph_block(md: Path) -> str:
    lines = md.read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(lines) if l == "```json")
    e = max(i for i, l in enumerate(lines) if l == "```")
    return "\n".join(lines[s + 1:e]) + "\n"


def timing_standin(fv_scripts: Path) -> dict:
    """Scratch stand-in for the merged package redline W7-D4 describes: W5's SR-FV-20 (EXPECTED_POLICY_20261027 with
    CL-05's stage category and a policy argument) with W4's SR-4 QA_PLAN_REVIEW value moved into the 20261027 policy
    rather than into EXPECTED_POLICY. EXECUTE's package build owns the real text."""
    w5 = json.loads((HERE / "work/W5.json").read_text(encoding="utf-8"))
    w4 = json.loads((HERE / "work/W4.json").read_text(encoding="utf-8"))
    sr20 = next(r for r in w5["skill_redlines"] if r["id"] == "SR-FV-20")
    sr4 = next(r for r in w4["skill_redlines"] if r["id"] == "SR-4")
    p = fv_scripts / "validate_gcfpe_artifact_timing.py"
    text = p.read_text(encoding="utf-8")
    assert text.count(sr20["old"]) == 1 and text.count(sr4["old"]) == 1
    text = text.replace(sr20["old"], sr20["new"])
    new_birth = re.search(r"'QA_PLAN_REVIEW': (\{.*\})$", sr4["new"]).group(1)
    anchor = "EXPECTED_POLICY_20261027 = {**EXPECTED_POLICY, "
    assert text.count(anchor) == 1
    text = text.replace(anchor, anchor + "'qa_artifact_births': {**EXPECTED_POLICY['qa_artifact_births'], "
                        "'QA_PLAN_REVIEW': " + new_birth + "}, ")
    p.write_text(text, encoding="utf-8")
    return {"sr_fv_20_applied": True, "w4_sr4_value_in_20261027_policy": True, "expected_policy_unchanged": True}


def cmd_dryrun(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="make_profile_20261027.py dryrun")
    ap.add_argument("skills"); ap.add_argument("scratch")
    for k in ("--production-md", "--production-contract", "--r1-dir", "--plan", "--map"):
        ap.add_argument(k, required=True)
    ap.add_argument("--members-tsv", default=str(HERE / "members-100926.1.tsv"))
    ap.add_argument("--stand-in-ok", action="store_true")
    a = ap.parse_args(argv)
    S, W = Path(a.skills), Path(a.scratch) / "profile-dryrun"
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    smap = SM.load(a.map, a.members_tsv, a.stand_in_ok)
    fv, cf = W / "flowmaster-validate", W / "change-flow"
    for k, d in (("flowmaster-validate", fv), ("change-flow", cf)):
        shutil.copytree(S / k, d, ignore=shutil.ignore_patterns("__pycache__"))
    # The skills validate_package reads beside change-flow, unchanged (read-only copies).
    for k in ("glow-hde-pr-development", "glow-merged-change-attribution-lock", "flowmaster-primary"):
        shutil.copytree(S / k, W / k, ignore=shutil.ignore_patterns("__pycache__"))
    rec = {"stand_in_used": smap.get("stand_in") is True,
           "stand_ins": ["successor map" if smap.get("stand_in") else None,
                         "plan file " + a.plan, "EXPECTED_POLICY_20261027 (timing_standin)",
                         "fixtures: the 100926.1 scenarios with release fields moved (package build adds cases)",
                         "change-flow SKILL.md and glow-hde-pr-development as installed (revisions move in EXECUTE)"]}
    rec["timing_standin"] = timing_standin(fv / "scripts")
    gj = _graph_block(Path(a.production_md))
    names = {"contract": "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json",
             "graph": "references/gcfpe-20261027.1-102726.1-candidate-graph-contract.json"}
    for d in (fv, cf):
        (d / names["graph"]).write_text(gj, encoding="utf-8")
        shutil.copyfile(a.production_contract, d / names["contract"])
    shutil.copyfile(Path(a.r1_dir) / "map-glow-hde-canonical-change-flow-r1-runtime-map-20261027.json",
                    cf / "references/glow-hde-canonical-change-flow-r1-runtime-map-20261027.json")
    fxd = fv / "fixtures/gcfpe-20261027.1-102726.1"
    fxd.mkdir(parents=True)
    fx = json.loads((fv / "fixtures/gcfpe-20261009.1-100926.1/scenarios.json").read_text(encoding="utf-8"))
    fx.update(suite_id="GCFPE-20261027.1-102726.1-SECTION-13", release="GCFPE-20261027.1", prompt_version="102726.1")
    (fxd / "scenarios.json").write_text(json.dumps(fx, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out_v = fv / "scripts/validate_gcfpe_20261027.py"
    b = subprocess.run([sys.executable, __file__, "build", str(fv / "scripts/validate_gcfpe_20261009.py"), str(out_v),
                        "--contract", str(fv / names["contract"]), "--graph", str(fv / names["graph"]),
                        "--fixtures", str(fxd / "scenarios.json"), "--plan", a.plan, "--map", a.map,
                        "--members-tsv", a.members_tsv,
                        "--profile-base", str(fv / "references/gcfpe-20261009.1-100926.1-validation-profile.json"),
                        "--profile-out", str(fv / "references/gcfpe-20261027.1-102726.1-validation-profile.json")]
                       + (["--stand-in-ok"] if a.stand_in_ok else []), capture_output=True, text=True,
                       env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    if b.returncode:
        rec["build"] = {"exit": b.returncode, "stderr": b.stderr[-1500:]}
        rec["ok"] = False
        print(json.dumps(rec, indent=1))
        return 1
    built = json.loads(b.stdout)
    rec["build"] = {"exit": 0, "substitutions": len(built["report"]), "report": built["report"],
                    "measured": built["measured"], "leftover_literal_counts": built["leftover_literal_counts"],
                    "successor_members": built["successor_members"], "kept_members": built["kept_members"],
                    "validator_sha256": built["validator_sha256"], "profile": built["profile_written"]}
    r = subprocess.run([sys.executable, "scripts/validate_gcfpe_20261027.py", str(cf), "--contract",
                        str(cf / names["contract"])], cwd=fv, capture_output=True, text=True,
                       env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    try:
        run = json.loads(r.stdout)
    except json.JSONDecodeError:
        rec["profile_run"] = {"exit": r.returncode, "stderr": r.stderr[-1500:]}
        rec["ok"] = False
        print(json.dumps(rec, indent=1))
        return 1
    errs = run.get("errors", [])
    pending = {"CHANGE_FLOW_CONTRACT:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.5.0",
               "SKILL_CONTRACT:glow-hde-pr-development:GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.5.0"}
    unexpected = [e for e in errs if e not in pending and not e.startswith("SKILL_SELF_IDENTITY:")]
    rec["profile_run"] = {"exit": r.returncode, "ok_flag": run.get("ok"), "errors": errs,
                          "expected_pending": sorted(set(errs) - set(unexpected)), "unexpected_errors": unexpected,
                          "profile": run.get("profile"), "contract_status": run.get("contract_status"),
                          "frozen_graph_node_count": run.get("frozen_graph_node_count"),
                          "frozen_graph_edge_count": run.get("frozen_graph_edge_count"),
                          "prompt_body_checks_not_evaluated": run.get("prompt_body_checks_not_evaluated"),
                          "pending_by_design": "change-flow 3.5.0 and glow-hde-pr-development 1.5.0 land with their "
                                               "redlines in EXECUTE's package build; SKILL_TREE_SHA256 is recomputed last "
                                               "(I step), so the scratch tree's self-identity differs"}
    rec["regressions"] = regressions(fv, cf, names, smap)
    rec["ok"] = (not unexpected and all(rec["regressions"].values()))
    print(json.dumps(rec, indent=1))
    return 0 if rec["ok"] else 1


def regressions(fv: Path, cf: Path, names: dict, smap: dict) -> dict:
    """Each new check fires on its injected regression, in memory, on the production contract."""
    sys.path.insert(0, str(fv / "scripts"))
    spec = importlib.util.spec_from_file_location("v1027", fv / "scripts/validate_gcfpe_20261027.py")
    V = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V)
    base = json.loads((cf / names["contract"]).read_text(encoding="utf-8"))
    clean = V.validate_contract(base)
    rows = {"clean_contract_no_contract_errors": clean == []}

    def fires(code_prefix: str, mutate) -> bool:
        c = copy.deepcopy(base)
        mutate(c)
        return any(e.startswith(code_prefix) for e in V.validate_contract(c))

    def qa120_edge_to(c, cls, to):
        for e in c["route_edges"]:
            if e["from"] == "QA-120" and any(b.get("change_class") == cls for b in e["route_branches"]):
                e["to"] = to
        for r in c["state_routes"]["QA-120"]:
            if r.get("change_class") == cls:
                r["destinations"] = [to]
    rows["rejects_qa_pass_straight_to_closure"] = fires("QA_PASS_CLASS", lambda c: qa120_edge_to(c, "CRD", "CL-C-10"))

    def cl05_wrong_class(c):
        for r in c["state_routes"]["CL-05"]:
            if r.get("change_class") == "CRD":
                r["destinations"] = ["CL-E-10"]
    rows["rejects_cl05_exit_wrong_class"] = fires("CL05_CLOSE_EXIT_ROUTES", cl05_wrong_class)

    def close_set_to_esc30(c):
        for e in c["route_edges"]:
            if e["from"] == "CL-C-10" and e["to"] == "CL-05":
                e["to"] = "ESC-30"
    rows["rejects_do_not_close_close_set_to_esc30"] = fires("DO_NOT_CLOSE_CLOSE_SET_ROUTE:CL-C-10", close_set_to_esc30)
    rows["rejects_close_set_as_post_closure"] = fires("CLOSE_STAGE_CATEGORY", lambda c: c[
        "artifact_availability_contract"]["stage_categories"].__setitem__("CL-05", "POST_CLOSURE"))
    rows["rejects_qa_closure_map_both_to_crd"] = fires("QA_CLOSURE_CONTRACT", lambda c: c["qa_closure_contract"][
        "close_stage_exit_receivers"].__setitem__("EPIC", "CL-C-10"))

    def doc20_pr40(c):
        e = copy.deepcopy(next(x for x in c["route_edges"] if x["from"] == "DOC-20" and x["to"] == "QA-10"))
        e["to"] = "PR-40"
        e["route_branches"][0]["condition"] = "actual merged state or landed-lineage review is required after Nathan asserts the manual merge"
        c["route_edges"].append(e)
    rows["rejects_doc20_inbound_pr40"] = fires("PR40_MANUAL_MERGE_BOUNDARY", doc20_pr40)
    off_map = next(k for k, v in smap["members"].items() if v["disposition"] == "SUCCESSOR")
    rows["rejects_member_version_off_map"] = fires(f"MEMBER_BINDING:{off_map}", lambda c: c["member_registry"][
        off_map].__setitem__("version", "100926.1"))
    rows["rejects_kept_member_at_102726"] = fires("MEMBER_BINDING:GCFPE-MGMT-10", lambda c: c["member_registry"][
        "GCFPE-MGMT-10"].__setitem__("version", "102726.1"))

    def fifty_five(c):
        c["candidate_prompt_ids"].remove("CL-05")
    rows["rejects_55_member_contract"] = fires("MEMBER_SET", fifty_five)
    rows["rejects_merge_pending_without_real_input_p1"] = fires("MERGE_PENDING_REQUIREMENTS", lambda c: c[
        "pr_development_contract"]["merge_pending_requirements"].remove("no open P1 thread on a real input"))
    rows["rejects_old_r1_oracle_pin"] = fires("PROTECTED_IDENTITIES", lambda c: c["protected_identities"].__setitem__(
        "r1_oracle_sha256", OLD_ORACLE))
    rows["rejects_20260923_oracle_not_historical"] = fires("HISTORICAL_NON_EXECUTABLE_REFERENCES", lambda c: c[
        "historical_non_executable_references"].remove("glow-hde-canonical-change-flow-r1-20260923.json"))
    # Body checks on synthetic text (no prompt body is read or written here).
    member = off_map
    superseded = smap["members"][member]["predecessor_page_id"]
    fake = "000000000000000000000000000000ab"
    head = f"{base['member_registry']['PR-10']['title']}\nPrompt ID: PR-10\n"
    errs_bad = V.validate_prompt_bodies({"PR-10": head + f'see <mention url="https://app.notion.com/p/{superseded}" />\n'},
                                        base)[0]
    errs_dash = V.validate_prompt_bodies({"PR-10": head + "see https://app.notion.com/p/" + "-".join(
        [superseded[:8], superseded[8:12], superseded[12:16], superseded[16:20], superseded[20:]]) + "\n"}, base)[0]
    errs_ok = V.validate_prompt_bodies({"PR-10": head + f"see https://app.notion.com/p/{fake}?pvs=204\n"}, base)[0]
    rows["binding_superseded_fires"] = f"PROMPT_BINDING_SUPERSEDED:PR-10:{member}" in errs_bad
    rows["binding_superseded_fires_on_dashed_id"] = f"PROMPT_BINDING_SUPERSEDED:PR-10:{member}" in errs_dash
    rows["binding_superseded_silent_on_other_page"] = not any(e.startswith("PROMPT_BINDING_SUPERSEDED") for e in errs_ok)
    cl05 = base["member_registry"]["CL-05"]["notion_url"]
    row = ("| `PASS` | `{c}` | `CL-05 — Prepare and Publish the Close Mutation Set — 102726.1` at "
           '<mention url="' + cl05.split("?")[0] + '" />, which exits to `{d} — Closure` |')
    good = row.format(c="EPIC", d="CL-E-10") + "\n" + row.format(c="CRD", d="CL-C-10") + "\n"
    swapped = row.format(c="EPIC", d="CL-C-10") + "\n" + row.format(c="CRD", d="CL-C-10") + "\n"
    rows["qa_pass_rows_parse_two"] = len(V.qa_pass_class_rows(good)) == 2
    rows["qa_pass_rows_html_code_form"] = len(V.qa_pass_class_rows(good.replace("`", "<code>", 1))) in (1, 2)
    rows["qa_pass_body_map_clean"] = "QA_PASS_BODY_CLASS_MAP" not in V.validate_qa_closure_bodies({"QA-120": good}, base)
    rows["qa_pass_body_map_rejects_wrong_exit"] = "QA_PASS_BODY_CLASS_MAP" in V.validate_qa_closure_bodies(
        {"QA-120": swapped}, base)
    rows["qa_pass_body_map_rejects_straight_to_closure"] = "QA_PASS_BODY_CLASS_MAP" in V.validate_qa_closure_bodies(
        {"QA-120": good.replace("`CL-05 — ", "`CL-C-10 — ")}, base)
    rec = V.validate_qa_closure_bodies({"QA-120": good, "CL-C-10": "A close-tooling defect is CL-05's to repair, not ESC-30 work."}, base)
    rows["close_set_repair_sentence_present_passes"] = "QA_CLOSE_SET_REPAIR_ROUTE_BODY:CL-C-10" not in rec
    rows["close_set_repair_sentence_removed_fails"] = "QA_CLOSE_SET_REPAIR_ROUTE_BODY:CL-C-10" in V.validate_qa_closure_bodies(
        {"QA-120": good, "CL-C-10": "nothing"}, base)
    return rows


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("build", "dryrun"):
        sys.exit(__doc__)
    sys.exit((cmd_build if sys.argv[1] == "build" else cmd_dryrun)(sys.argv[2:]))
