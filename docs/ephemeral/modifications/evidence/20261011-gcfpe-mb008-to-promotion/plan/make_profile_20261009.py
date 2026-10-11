#!/usr/bin/env python3
"""Derive flowmaster-validate's GCFPE-20261009.1 / 100926.1 validator from its 091426.1 validator (F06).

MODIFICATION-20261011-gcfpe-mb008-to-promotion, PLAN, PART-01. The 091426.1 validator stays in the package
unchanged, as history; this writes `validate_gcfpe_20261009.py` beside it. Every change is a named substitution
whose old text must occur exactly the stated number of times, so a moved base fails loudly instead of being
half-edited. Release pins that depend on bytes (graph, contract, fixtures, routing surface, the PLAN document)
are measured from the files passed in, never typed.

  make_profile_20261009.py <base-validator.py> <out-validator.py> --contract <100926.1 bundled contract>
      --graph <100926.1 bundled graph json> --fixtures <100926.1 scenarios.json> --plan <PLAN document>
      [--list]      print the substitutions and their counts without writing

Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

OLD_REL, NEW_REL = "GCFPE-20260914.1", "GCFPE-20261009.1"
OLD_VER, NEW_VER = "091426.1", "100926.1"
OLD_BASE_REL, NEW_BASE_REL = "GCFPE-20260913.1", "GCFPE-20260914.1"
OLD_BASE_VER, NEW_BASE_VER = "091326.2", "091426.1"
NEW_MEMBER_RULE = ("54 successor runtime members + the GCFPE-MGMT-10 successor (D20 three-mode body); no additions or "
                   "removals")
PLAN_PATH_IN_REPO = "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md"
# F05 (parent Modification): the addendum format the graph states and the 100926.1 contract now carries.
FORMAT_HOME = 'PF06-Canon-Change-Process-Guide §0.1A and PF27-Canon-Plan-Templates, Canon precedence for template use, read from docs/pfcanon on main'
FORMAT_EXPECTATIONS = {
    "excluded_content": "role-addressed handling, publication, routing and record-maintenance instructions, which stay in the decision and handoff",
    "heading": "exactly one H2 carrying the next continuous addendum number, resolved by the producer from current controlled PF10 at creation, and a descriptive title",
    "number_carrier": "the H2 heading; no standalone pf10_addendum_number metadata field, which stays forbidden",
    "subject_matter": "page-ready, self-contained declarative statement of the approved decision and its approval status, durable requirements, exceptions, scope, exclusions and nonclaims, evidence, dependencies, conflicts, consequences and unresolved obligations, keeping completed work, future work, recommendations and unproven facts distinct",
    "subordinate_headings": "H3 or lower only"
}
TYPESAFE_RULE = "No agent gives its own recommendation, assessment or ranking of model, reasoning level or effort."
TYPESAFE_PROCEDURE = "run the installed TypeSafe scoring skill's script once"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def routing_surface(base_validator: Path, contract: dict) -> tuple[str, int]:
    sys.path.insert(0, str(base_validator.parent))
    spec = importlib.util.spec_from_file_location("base_validator_for_surface", base_validator)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.routing_surface(contract)


def substitutions(m: dict) -> list[tuple[str, str, str, int]]:
    """(name, old, new, expected count). Applied in order; release-wide literal renames come last."""
    return [
        ("S01 module title", 'Validate the versioned GCFPE-20260914.1 / 091426.1 candidate contract.',
         'Validate the versioned GCFPE-20261009.1 / 100926.1 contract (derived from the 091426.1 validator, F06).', 1),
        ("S02 routing surface pin",
         'EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"\nEXPECTED_ROUTING_SURFACE_ROWS = 284',
         f'EXPECTED_ROUTING_SURFACE = "{m["surface"]}"\nEXPECTED_ROUTING_SURFACE_ROWS = {m["surface_rows"]}', 1),
        ("S03 bundled byte pins",
         'EXPECTED_FROZEN_GRAPH_SHA256 = "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d"\n'
         'EXPECTED_FROZEN_GRAPH_BYTES = 575074\n'
         'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c"\n'
         'EXPECTED_CANDIDATE_CONTRACT_BYTES = 613326\n'
         'EXPECTED_FIXTURE_SHA256 = "c433aa09d63b4c8c42891d03086096a771f1092d8c24c325f1706ab00932fe71"',
         f'EXPECTED_FROZEN_GRAPH_SHA256 = "{m["graph_sha"]}"\n'
         f'EXPECTED_FROZEN_GRAPH_BYTES = {m["graph_bytes"]}\n'
         f'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "{m["contract_sha"]}"\n'
         f'EXPECTED_CANDIDATE_CONTRACT_BYTES = {m["contract_bytes"]}\n'
         f'EXPECTED_FIXTURE_SHA256 = "{m["fixture_sha"]}"', 1),
        ("S04 profile identity",
         '        "validator_revision": "3.3.2",', '        "validator_revision": "3.4.0",', 1),
        ("S05 profile staging identity",
         '        "selected_release_during_staging": "GCFPE-20260913.1",\n'
         '        "selected_prompt_version_during_staging": "091326.2",\n'
         '        "selected_member_count_during_staging": 54,\n    }, "PROFILE_IDENTITY")',
         '        "selected_release_during_staging": "GCFPE-20260914.1",\n'
         '        "selected_prompt_version_during_staging": "091426.1",\n'
         '        "selected_member_count_during_staging": 55,\n    }, "PROFILE_IDENTITY")', 1),
        ("S06 profile graph edge count", '        "edge_count": 229,', f'        "edge_count": {m["edge_count"]},', 1),
        ("S07 graph candidate and baseline profile",
         '        "release": "GCFPE-20260914.1",\n        "version_family": "091426.1",\n        "member_count": 55,\n'
         '        "member_rule": "54 selected predecessors + PR-35; no removals",\n    }, "GRAPH_CANDIDATE_PROFILE")\n'
         '    errors += subset_errors(graph.get("baseline"), {\n        "release": "GCFPE-20260913.1",\n'
         '        "version_family": "091326.2",\n        "member_count": 54,\n    }, "GRAPH_BASELINE_PROFILE")',
         '        "release": "GCFPE-20261009.1",\n        "version_family": "100926.1",\n        "member_count": 55,\n'
         f'        "member_rule": "{NEW_MEMBER_RULE}",\n    }}, "GRAPH_CANDIDATE_PROFILE")\n'
         '    errors += subset_errors(graph.get("baseline"), {\n        "release": "GCFPE-20260914.1",\n'
         '        "version_family": "091426.1",\n        "member_count": 55,\n    }, "GRAPH_BASELINE_PROFILE")', 1),
        ("S08 graph proofs: no added node",
         '        or proofs.get("sole_added_node") != ["PR-35"]', '        or proofs.get("sole_added_node") != []', 1),
        ("S09 contract identity",
         '        "contract_revision": "4.1.1",\n        "target_release": "GCFPE-20260914.1",\n'
         '        "predecessor_release": "GCFPE-20260913.1",\n        "prompt_version": "091426.1",\n'
         '        "predecessor_prompt_version": "091326.2",\n        "candidate_member_count": 55,\n'
         '        "selected_member_count_during_staging": 54,\n'
         '        "selected_release_during_staging": "GCFPE-20260913.1",\n'
         '        "selected_prompt_version_during_staging": "091326.2",\n        "sole_added_member": "PR-35",',
         '        "contract_revision": "4.2.0",\n        "target_release": "GCFPE-20261009.1",\n'
         '        "predecessor_release": "GCFPE-20260914.1",\n        "prompt_version": "100926.1",\n'
         '        "predecessor_prompt_version": "091426.1",\n        "candidate_member_count": 55,\n'
         '        "selected_member_count_during_staging": 55,\n'
         '        "selected_release_during_staging": "GCFPE-20260914.1",\n'
         '        "selected_prompt_version_during_staging": "091426.1",\n        "sole_added_member": None,', 1),
        ("S10 PR skill revision", '"primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.3.1",',
         '"primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.4.0",', 1),
        ("S11 F05 producer numbers the addendum",
         '"producer_allocates_pf10_number": False, "producer_claims_canonical_adoption": False,',
         '"producer_allocates_pf10_number": True, "producer_claims_canonical_adoption": False,', 1),
        ("S12 governing plan pin (repository file)",
         '    errors += subset_errors(source_snapshot.get("governing_plan"), {\n'
         '        "sha256": "e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01",\n'
         '        "byte_count": 53118,\n        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",\n'
         '    }, "REPAIR_PLAN_SOURCE_PIN")',
         '    errors += subset_errors(source_snapshot.get("governing_plan"), {\n'
         f'        "sha256": "{m["plan_sha"]}",\n        "byte_count": {m["plan_bytes"]},\n'
         '        "representation": "REPOSITORY_FILE_ON_MAIN",\n'
         f'        "repository_path": "{PLAN_PATH_IN_REPO}",\n'
         '    }, "REPAIR_PLAN_SOURCE_PIN")\n'
         '    errors += subset_errors(source_snapshot.get("predecessor_direct_handoff_contract"), {\n'
         '        "contract_id": "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED",\n'
         '        "sha256": "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c",\n'
         '    }, "PREDECESSOR_CONTRACT_PIN")\n'
         '    if "candidate_notion_url_map" in source_snapshot or "prompt_topology_move_readback" in source_snapshot:\n'
         '        errors.append("RETIRED_091426_STAGING_SOURCE")', 1),
        ("S14 F05 format keys join the closed addendum object",
         '    "standalone_overlay",\n})\n',
         '    "standalone_overlay",\n    "format_expectations",\n'
         + "".join(f'    "format_expectations.{k}",\n' for k in sorted(FORMAT_EXPECTATIONS))
         + '})\n', 1),
        ("S15 F05 format values pinned",
         '    }, "PF10_ADDENDUM_CONTRACT")\n',
         '    }, "PF10_ADDENDUM_CONTRACT")\n'
         '    if not isinstance(addendum, dict) or addendum.get("format_home") != ' + repr(FORMAT_HOME)
         + ' or addendum.get("format_expectations") != ' + repr(FORMAT_EXPECTATIONS) + ':\n'
         '        errors.append("PF10_ADDENDUM_FORMAT")\n', 1),
        ("S16 PF10 2.1 body check",
         '        if prompt_id not in HANDOFF_LITERAL_EXEMPT and "NEXT_PROMPT_HANDOFF" not in text:\n'
         '            errors.append(f"PROMPT_HANDOFF_LITERAL:{prompt_id}")\n',
         '        if prompt_id not in HANDOFF_LITERAL_EXEMPT and "NEXT_PROMPT_HANDOFF" not in text:\n'
         '            errors.append(f"PROMPT_HANDOFF_LITERAL:{prompt_id}")\n'
         '        # HDE Build Notes, the TypeSafe reading (MB-008 PART-02): every body that hands work to a session,\n'
         '        # and GCFPE-MGMT-10 for its next mode, carries the reading rule. PR-50 hands nothing on.\n'
         f'        if prompt_id != "PR-50" and ({TYPESAFE_RULE!r} not in text or {TYPESAFE_PROCEDURE!r} not in text):\n'
         '            errors.append(f"PROMPT_TYPESAFE_READING:{prompt_id}")\n', 1),
        ("S13 F09 PR-20 receives the pre-Proceed RS-20 return",
         '    "PR-20": {"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"],',
         '    "PR-20": {"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT", '
         '"RS-20:RESCOPE_REVIEW:APPROVE", "RS-20:RESCOPE_REVIEW:REJECT", "RS-20:RESCOPE_REVIEW:IN_SCOPE_REPAIR"], '
         '"rs20_returns_only_from_recorded_pr20_planning_origin_before_proceed": True,', 1),
        # Release-wide literal renames. Each count is the base's own; a changed base fails here.
        ("S90 bundled file names", "gcfpe-20260914.1-091426.1", "gcfpe-20261009.1-100926.1", m["n_file"]),
        ("S91 graph file name", "GCFPE-20260914.1-Candidate-Graph-Contract.json",
         "GCFPE-20261009.1-Candidate-Graph-Contract.json", m["n_graphfile"]),
        ("S92 profile id", '"GCFPE-20260914.1-091426.1-VALIDATION"', '"GCFPE-20261009.1-100926.1-VALIDATION"', 1),
        ("S93 graph contract id", '"GCFPE-20260914.1-CANDIDATE-GRAPH"', '"GCFPE-20261009.1-CANDIDATE-GRAPH"', 1),
        ("S94 contract ids", 'contract.get("contract_id") != "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-',
         'contract.get("contract_id") != "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-', 2),
        ("S95 member version", 'or member.get("version") != "091426.1"', 'or member.get("version") != "100926.1"', 1),
        ("S96 manifest page version", 'or page.get("version") != "091426.1"', 'or page.get("version") != "100926.1"', 1),
        ("S97 abort prompt version", '"id": "PR-50", "version": "091426.1",', '"id": "PR-50", "version": "100926.1",', 1),
        ("S98 profile target release",
         '        "target_release": "GCFPE-20260914.1",\n        "prompt_version": "091426.1",',
         '        "target_release": "GCFPE-20261009.1",\n        "prompt_version": "100926.1",', 1),
    ]


def build(base: Path, contract_path: Path, graph_path: Path, fixtures: Path, plan: Path) -> tuple[str, list]:
    src = base.read_text(encoding="utf-8")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    surface, rows = routing_surface(base, contract)
    m = {
        "surface": surface, "surface_rows": rows,
        "graph_sha": sha256(graph_path), "graph_bytes": graph_path.stat().st_size,
        "contract_sha": sha256(contract_path), "contract_bytes": contract_path.stat().st_size,
        "fixture_sha": sha256(fixtures), "edge_count": len(graph["edges"]),
        "plan_sha": sha256(plan), "plan_bytes": plan.stat().st_size,
        "n_file": src.count("gcfpe-20260914.1-091426.1"),
        "n_graphfile": src.count("GCFPE-20260914.1-Candidate-Graph-Contract.json"),
    }
    out, report = src, []
    for name, old, new, want in substitutions(m):
        got = out.count(old)
        if got != want:
            raise SystemExit(f"{name}: expected {want} occurrence(s), found {got}")
        out = out.replace(old, new)
        report.append({"substitution": name, "count": got})
    return out, report + [{"measured": {k: v for k, v in m.items() if not k.startswith("n_")}}]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("out")
    ap.add_argument("--contract", required=True); ap.add_argument("--graph", required=True)
    ap.add_argument("--fixtures", required=True); ap.add_argument("--plan", required=True)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    text, report = build(Path(a.base), Path(a.contract), Path(a.graph), Path(a.fixtures), Path(a.plan))
    if not a.list:
        Path(a.out).write_text(text, encoding="utf-8")
    print(json.dumps({"written": None if a.list else a.out, "report": report}, indent=1))
    return 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main())
