"""§8b.7 v2: validator reversals in flowmaster-validate/scripts/validate_gcfpe_20260914.py (scratch copy)."""
import sys, json
sys.dont_write_bytecode = True
from common import apply
from cand import RECEIVERS, TRANSITION, OBS, V3_TIME, W8_CONT, W8_REPLAN, W4
path = sys.argv[1] + '/flowmaster-validate/scripts/validate_gcfpe_20260914.py'
C0 = json.load(open('/tmp/claude-0/spec/s6/after_contract.json'))
SEM = dict(C0['route_graph_semantics']); SEM.pop('same_session_phase_continuation')
SEM.update({'pr30_to_pr35_phase_continuation': W8_CONT, 'pr40_entry': W4, 'pr40_reject_replan': W8_REPLAN})
SEM = dict(sorted(SEM.items()))
COND_PR35 = "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
COND_RS40 = "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
def pyrepr(v, indent=4):
    return json.dumps(v, ensure_ascii=False, indent=indent).replace(': true', ': True').replace(': false', ': False').replace('true,', 'True,').replace('false,', 'False,')
TX = {k: v for k, v in TRANSITION.items() if k != 'prohibited_references'}
apply(path, [
 ('EXPECTED_PR35_RESULTS = [\n    "MERGE_PENDING", "RESCOPE_PENDING",',
  'EXPECTED_PR35_RESULTS = [\n    "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING",'),
 ('    "WORK_UNIT_ID", "original Product Owner Proceed", "dedicated PR-development session",\n    "workspace/worktree",',
  '    "WORK_UNIT_ID", "original Product Owner Proceed",\n    "workspace/worktree",'),
 ('PROMPT_VERSION_HEADER_RE = re.compile(r"^Prompt [Vv]ersion: `?091426\\.1`?$")',
  'RELEASE_HEADER_KEYS = ("Prompt Version:", "Prompt version:", "Set:", "Ecosystem release:")'),
 ('    return bool(\n        len(nonblank) >= 7\n        and nonblank[0] == member.get("title")\n        and any(PROMPT_VERSION_HEADER_RE.match(line) for line in nonblank[:8])\n        and any(line in header_value_lines("Prompt ID:", prompt_id) for line in nonblank[:8])\n        and any(\n            line in header_value_lines("Ecosystem release:", "GCFPE-20260914.1")\n            for line in nonblank[:8]\n        )\n        and url_line_ok\n    )\n',
  '    return bool(\n        len(nonblank) >= 4\n        and nonblank[0] == member.get("title")\n        and any(line in header_value_lines("Prompt ID:", prompt_id) for line in nonblank[:8])\n        and url_line_ok\n    )\n\n\ndef prompt_body_release_header(nonblank: list[str]) -> bool:\n    """True when the header window carries a release-bound line, which D23-G prohibits."""\n\n    stripped = [governance_line_normalised(line) for line in nonblank[:8]]\n    return any(line.startswith(key) for line in stripped for key in RELEASE_HEADER_KEYS)\n'),
 ('        if not prompt_identity_header_valid(nonblank, member, prompt_id):\n            errors.append(f"PROMPT_BODY_IDENTITY:{prompt_id}")\n',
  '        if not prompt_identity_header_valid(nonblank, member, prompt_id):\n            errors.append(f"PROMPT_BODY_IDENTITY:{prompt_id}")\n        if prompt_body_release_header(nonblank):\n            errors.append(f"PROMPT_BODY_RELEASE_HEADER:{prompt_id}")\n'),
 ('        "contract_revision": "4.0.6",', '        "contract_revision": "4.1.0",'),
 # rule 11: HANDOFF_CONTRACT exact keys and values; prohibited refs own value
 ('    errors += subset_errors(transition, {\n        "transport": "DIRECT_NATIVE_PROMPT_HANDOFF", "block": "NEXT_PROMPT_HANDOFF",\n        "fence_language": "text", "first_line": "NEXT_PROMPT_HANDOFF",\n        "exactly_one_per_nonterminal_result": True, "terminal_has_no_handoff": True,\n        "actual_branch_only": True, "actual_pasteable_complete_prompt": True,\n        "metadata_only_or_routing_summary_prohibited": True,\n        "blank_form_menu_or_reconstruction_prohibited": True,\n        "exact_destination_full_name_version_direct_notion_url": True,\n        "receiving_role_and_exact_session": True, "epic_change_and_work_unit": True,\n        "every_required_repository_and_pr_reference": True,\n        "status_completed_work_decisions_constraints_unresolved_authority": True,\n        "next_action_and_expected_output": True,\n    }, "HANDOFF_CONTRACT")\n',
  '    if (\n        not isinstance(transition, dict)\n        or set(transition) != set(EXPECTED_TRANSITION_CONTRACT) | {"prohibited_references"}\n        or any(transition.get(key) != value for key, value in EXPECTED_TRANSITION_CONTRACT.items())\n    ):\n        errors.append("HANDOFF_CONTRACT")\n'),
 ('        "model/strength/reasoning/eligibility/suitability/account/configuration route",\n    }:\n        errors.append("HANDOFF_PROHIBITED_REFERENCES")',
  '        "model/strength/reasoning/eligibility/suitability/account/configuration route",\n        "branch", "commit", "restated artifact content",\n        "menu", "metadata-only summary", "blank form", "placeholder after publication",\n    }:\n        errors.append("HANDOFF_PROHIBITED_REFERENCES")'),
 # W-8: pr30_ownership inside PR_DEVELOPMENT_CONTRACT; primary skill revision
 ('        "primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.2.5",',
  '        "primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.3.0",\n        "pr30_ownership": [\n            "recovery", "implementation", "local testing", "coherent commit creation",\n            "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session",\n        ],'),
 # W-8: preserved_lineage inside RESCOPE_CONTRACT
 ('        "accepted_final_replay": False, "automatic_abort_route": False,\n    }, "RESCOPE_CONTRACT")',
  '        "accepted_final_replay": False, "automatic_abort_route": False,\n        "preserved_lineage": [\n            "PR_RETURN_PHASE", "PR_PHASE_SESSION", "WORKSPACE", "WORKTREE", "BRANCH",\n            "OPEN_PR_WHEN_ONE_EXISTS", "COMMIT", "ORIGINAL_PROCEED", "COMPLETED_WORK", "TESTS",\n            "REVIEWS", "CI_STATE", "DECISION", "ARTIFACTS", "UNRESOLVED_WORK",\n        ],\n    }, "RESCOPE_CONTRACT")'),
 # rule 2 + 3
 ('    if not isinstance(development, dict) or any(value != 0 for value in development.get("added_boundaries", {}).values()):\n        errors.append("PR35_ADDED_BOUNDARY")\n    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY:\n        errors.append("PR_PHASE_CONTINUITY")',
  '    if not isinstance(development, dict) or development.get("added_boundaries") != EXPECTED_PR35_ADDED_BOUNDARIES:\n        errors.append("PR35_ADDED_BOUNDARY")\n    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY or "dedicated PR-development session" in development.get("shared_exactly_one", []):\n        errors.append("PR_PHASE_CONTINUITY")'),
 ('EXPECTED_MERGE_PENDING_REQUIREMENTS = {',
  'EXPECTED_PR35_ADDED_BOUNDARIES = {\n    "approval": 0, "cross_session_route": 1, "duplicate_work_vehicle": 0, "merge_authority": 0,\n    "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0,\n    "work_vehicle": 0,\n}\n'
  'EXPECTED_TRANSITION_CONTRACT = ' + pyrepr(TX) + '\n'
  'EXPECTED_OBSERVED_MERGE_EDGES = ' + pyrepr(OBS) + '\n'
  'EXPECTED_EVENT_2 = ' + pyrepr({"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted", "time": V3_TIME, "value": True}) + '\n'
  'EXPECTED_RECEIVERS = ' + pyrepr(dict(sorted(RECEIVERS.items()))) + '\n'
  'EXPECTED_ROUTE_GRAPH_SEMANTICS = ' + pyrepr(SEM) + '\n'
  'PR35_TOP_LEVEL_ROLE_PHRASE = "never as a subagent, forked agent or workflow agent of PR-30"\n'
  'OBSERVED_MERGE_EDGE_CONDITIONS = {\n    "PR-35": ' + json.dumps(COND_PR35) + ',\n    "RS-40": ' + json.dumps(COND_RS40) + ',\n}\n\n\n'
  'def observed_merge_edge_errors(edges) -> bool:\n    """True unless PR-35 and RS-40 each have exactly one lawful MERGE_OBSERVED edge to PR-40."""\n\n    found = [e for e in edges if isinstance(e, dict) and e.get("to") == "PR-40" and e.get("from") in OBSERVED_MERGE_EDGE_CONDITIONS]\n    if sorted(e.get("from") for e in found) != ["PR-35", "RS-40"]:\n        return True\n    for e in found:\n        branches = e.get("route_branches")\n        if (\n            e.get("from_kind") != "prompt" or e.get("to_kind") != "prompt" or e.get("automatic") is not False\n            or e.get("transport") != "COMPLETE_NEXT_PROMPT_HANDOFF" or e.get("state_predicates") != ["MERGE_OBSERVED"]\n            or not isinstance(branches, list) or len(branches) != 1 or not isinstance(branches[0], dict)\n            or branches[0].get("branch_id") != "merge_observed" or branches[0].get("state") != "MERGE_OBSERVED"\n            or branches[0].get("applicable_states") != ["MERGE_OBSERVED"]\n            or branches[0].get("condition") != OBSERVED_MERGE_EDGE_CONDITIONS[e["from"]]\n        ):\n            return True\n    return False\n\n\nEXPECTED_MERGE_PENDING_REQUIREMENTS = {'),
 # rule 7: POST_MERGE_CONTRACT gains observed_merge_edges (V-2); POST_MERGE_THREE_EVENTS checks event_2 exactly (V-3)
 ('        "agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False,\n    }, "POST_MERGE_CONTRACT")',
  '        "agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False,\n        "observed_merge_edges": EXPECTED_OBSERVED_MERGE_EDGES,\n    }, "POST_MERGE_CONTRACT")'),
 ('        or (postmerge.get("event_2") or {}).get("actor") != "Nathan / Product Owner"\n        or (postmerge.get("event_2") or {}).get("fact") != "product_owner_manual_merge_assertion"\n',
  '        or postmerge.get("event_2") != EXPECTED_EVENT_2\n'),
 # rule 8
 ('        "ordinary_pr_work_unit": [\n            "PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35",\n            "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40",\n        ],',
  '        "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],\n        "pr35_merge_pending_fallback": ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],\n        "pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],'),
 ('    if contract.get("route_graph") != expected_route_graph:\n        errors.append("ROUTE_GRAPH_SHORTHAND")\n',
  '    if contract.get("route_graph") != expected_route_graph:\n        errors.append("ROUTE_GRAPH_SHORTHAND")\n    if contract.get("route_graph_semantics") != EXPECTED_ROUTE_GRAPH_SEMANTICS:\n        errors.append("ROUTE_GRAPH_SEMANTICS")\n    if PR35_TOP_LEVEL_ROLE_PHRASE not in str(((contract.get("member_registry") or {}).get("PR-35") or {}).get("receiving_role", "")):\n        errors.append("PR35_TOP_LEVEL_ROLE")\n'),
 # rule 5 + 9 (contract side)
 ('        if any(edge.get("from") == "PR-35" and edge.get("to") == "PR-40" for edge in edges if isinstance(edge, dict)):\n            errors.append("DIRECT_PR35_PR40_EDGE")',
  '        if observed_merge_edge_errors(edges):\n            errors.append("DIRECT_PR35_PR40_EDGE")\n        replan = [e for e in edges if isinstance(e, dict) and e.get("from") == "PR-40" and any(isinstance(b, dict) and b.get("branch_id") in {"reject_replan", "reject_existing_pr_owner"} for b in e.get("route_branches", []))]\n        if len(replan) != 1 or replan[0].get("to") != "PR-20" or any(isinstance(e, dict) and e.get("from") == "PR-40" and e.get("to") == "PR-30" for e in edges):\n            errors.append("PR40_REJECT_REPLAN_ROUTE")'),
 # rule 5 (graph side)
 ('        and edge.get("from") in {"PR-30", "PR-35"}\n        and edge.get("to") == "PR-40"\n        for edge in edges\n    ):\n        errors.append("GRAPH_DIRECT_PR40_EDGE")',
  '        and edge.get("from") in {"PR-30"}\n        and edge.get("to") == "PR-40"\n        for edge in edges\n    ) or observed_merge_edge_errors(edges):\n        errors.append("GRAPH_DIRECT_PR40_EDGE")'),
 # rule 11 subset check (V-6), graph side
 ('        errors.append("GRAPH_HANDOFF_CONTRACT_MISMATCH")\n',
  '        errors.append("GRAPH_HANDOFF_CONTRACT_MISMATCH")\n    if not isinstance(graph_handoff, dict) or not isinstance(transition, dict) or not set(graph_handoff.get("prohibited", [])) <= set(transition.get("prohibited_references", [])):\n        errors.append("GRAPH_HANDOFF_PROHIBITED_REFERENCES")\n'),
 # rule 6
 ('    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt"]',
  '    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt" and edge.get("from") not in OBSERVED_MERGE_EDGE_CONDITIONS]'),
 # rule 14 markers
 ('        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING"),',
  '        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING", "MERGE_OBSERVED"),'),
 ('        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES),',
  '        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES, "MERGE_OBSERVED"),'),
 # rule 12
 ('        "r1_rows": 46, "flowmaster_primary_core_changed": False,\n        "r1_oracle_changed": False, "pr35_adds_r1_row": False,',
  '        "r1_rows": 46, "flowmaster_primary_core_changed": False,\n        "r1_oracle_changed": True, "pr35_adds_r1_row": False,'),
 ('        "automatic_pr50_edges": 0, "protected_primary_core_unchanged": True,\n        "protected_r1_46_rows_unchanged": True,',
  '        "automatic_pr50_edges": 0, "protected_primary_core_unchanged": True,\n        "protected_r1_46_rows_unchanged": False,'),
 # rule 10
 ('    errors.extend(validate_artifact_timing_contract(contract))\n    return sorted(set(errors))\n\n\ndef find_skill(',
  '    receivers = contract.get("receiver_compatibility")\n    for receiver in sorted(set(EXPECTED_RECEIVERS) | set(receivers if isinstance(receivers, dict) else {})):\n        if not isinstance(receivers, dict) or receivers.get(receiver) != EXPECTED_RECEIVERS.get(receiver):\n            errors.append(f"RECEIVER_CONTRACT:{receiver}")\n    errors.extend(validate_artifact_timing_contract(contract))\n    return sorted(set(errors))\n\n\ndef find_skill('),
 # rule 14 pins
 ('        "edge_count": 227,', '        "edge_count": 229,'),
 ('EXPECTED_ROUTING_SURFACE = "7380cd14430777675f1e8b2cdfa4a0da"\nEXPECTED_ROUTING_SURFACE_ROWS = 282',
  'EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"\nEXPECTED_ROUTING_SURFACE_ROWS = 284'),
 ('        "validator_revision": "3.2.14",', '        "validator_revision": "3.3.0",'),
], 'fv')
print('patched')
