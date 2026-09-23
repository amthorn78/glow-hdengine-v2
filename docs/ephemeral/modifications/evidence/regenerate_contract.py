#!/usr/bin/env python3
"""A1-2 contract regenerator for the 091426.1 direct-handoff contract (spec v2 §6).

    regenerate(template, graph, graph_bytes, value_table) -> contract
      1. deep-copy the template T;
      2. write every mirrored path of §6.2 from the graph build G (42 contract paths + 12 fields x 55 members);
      3. apply the contract-only value table (§6.3): set, delete (removal) and rename (delete old + set new);
      4. serialise: json.dumps(indent=2, sort_keys=True, ensure_ascii=False) + "\\n", UTF-8.

No value-table entry may target a mirrored path (checked). The value table is held here, never read from G.

Commands (run with PYTHONDONTWRITEBYTECODE=1):
  acceptance <base-parts-dir> <builder> <template-contract> <fv-scripts> <scratch>
        strip every mirrored path from today's contract, regenerate from today's build with an empty value
        table, require 2b78f877.../606657 B; then the negative control (one changed edge condition).
  generate <graph-md-or-embedded-json> <template-contract> <oracle-file> <out-contract> [<out-contract> ...]
        write the new contract (revision 4.1.0) from the final build and the §6.3 value table.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True

MEMBER_PAIRS = {  # contract member_registry[id] field <- graph node field (§6.2)
    "notion_url": "candidate_url",
    "version": "candidate_version",
    "title": "title",
    "lane": "lane",
    "native_function": "native_function",
    "receiving_role": "receiving_role",
    "session_class": "session_class",
    "r1_mapping": "r1_mapping",
    "output_artifacts": "output_artifacts",
    "result_states": "result_states",
    "predecessor": "predecessor",
    "graph_predecessor_union_destinations": "predecessor_union_destinations",
}

TOP_AND_NESTED = [  # (contract path, graph getter) (§6.2)
    (("selection_status",), lambda g, b: g["selection_status"]),
    (("route_edges",), lambda g, b: g["edges"]),
    (("state_routes",), lambda g, b: g["state_routes"]),
    (("artifact_availability_contract",), lambda g, b: g["artifact_availability_contract"]),
    (("qa_closure_contract",), lambda g, b: g["qa_closure_contract"]),
    (("boundary_nodes",), lambda g, b: sorted(g["boundary_nodes"])),
    (("boundary_transitions",), lambda g, b: g["boundary_transitions"]),
    (("terminal_contract",), lambda g, b: g["terminal_contract"]),
    (("post_merge_three_event_contract",), lambda g, b: g["post_merge_three_event_contract"]),
    (("authoring_context_vocabulary",), lambda g, b: g["state_vocabularies"]["AUTHORING_CONTEXT"]),
    (("transition_contract", "first_line"), lambda g, b: g["handoff_contract"]["first_line"]),
    (("transition_contract", "fence_language"), lambda g, b: g["handoff_contract"]["fence_language"]),
    (("transition_contract", "actual_branch_only"), lambda g, b: g["handoff_contract"]["actual_branch_only"]),
    (("pf10_addendum_contract", "exact_producer_set"), lambda g, b: g["pf10_addendum_contract"]["exact_producer_set"]),
    (("pf10_addendum_contract", "exactly_one_per_qualifying_approval"),
     lambda g, b: g["pf10_addendum_contract"]["exactly_one_per_qualifying_approval"]),
    (("pf10_addendum_contract", "producer_edits_pf10"), lambda g, b: g["pf10_addendum_contract"]["producer_edits_pf10"]),
    (("pf10_addendum_contract", "producer_allocates_pf10_number"),
     lambda g, b: g["pf10_addendum_contract"]["producer_allocates_pf10_number"]),
    (("pf10_addendum_contract", "producer_claims_canonical_adoption"),
     lambda g, b: g["pf10_addendum_contract"]["producer_claims_canonical_adoption"]),
    (("pf10_addendum_contract", "native_outcome_normalization"),
     lambda g, b: g["pf10_addendum_contract"]["native_outcome_normalization"]),
    (("pf10_addendum_contract", "never_for"), lambda g, b: g["pf10_addendum_contract"]["never_for"]),
    (("pr_development_contract", "pr30_result_vocabulary"), lambda g, b: g["state_vocabularies"]["PR-30_RESULT"]),
    (("pr_development_contract", "pr35_result_vocabulary"), lambda g, b: g["state_vocabularies"]["PR-35_RESULT"]),
    (("pr_return_phase_contract", "routes"), lambda g, b: g["state_vocabularies"]["PR_RETURN_PHASE"]),
    (("rescope_contract", "decision_vocabulary"), lambda g, b: g["state_vocabularies"]["RS-20_DECISION"]),
    (("pr_development_contract", "r1_row"), lambda g, b: g["pr_continuity_contract"]["r1_row"]),
    (("pr_development_contract", "primary_skill"), lambda g, b: g["pr_continuity_contract"]["primary_skill"]),
    (("pr_development_contract", "added_boundaries"), lambda g, b: g["pr_continuity_contract"]["adds"]),
    (("pr_development_contract", "shared_exactly_one"), lambda g, b: g["pr_continuity_contract"]["shared_exactly_one"]),
    (("pr_development_contract", "invented_session_inspection_endpoint_prohibited"),
     lambda g, b: g["pr_continuity_contract"]["invented_session_inspection_endpoint_prohibited"]),
    (("pr_development_contract", "unsupported_platform_limitation_claim_prohibited"),
     lambda g, b: g["pr_continuity_contract"]["unsupported_platform_limitation_claim_prohibited"]),
    (("route_graph", "prepublication_rescope"),
     lambda g, b: g["pr_continuity_contract"]["phase_aware_rescope_sequences"]["PR-30_PREPUBLICATION"]),
    (("route_graph", "postpublication_pr30_rescope"),
     lambda g, b: g["pr_continuity_contract"]["phase_aware_rescope_sequences"]["PR-30_POSTPUBLICATION"]),
    (("route_graph", "pr35_rescope"), lambda g, b: g["pr_continuity_contract"]["phase_aware_rescope_sequences"]["PR-35"]),
    (("abort_prompt", "id"), lambda g, b: g["abort_contract"]["prompt"]),
    (("abort_prompt", "invoker"), lambda g, b: g["abort_contract"]["manual_invoker"]),
    (("abort_prompt", "exact_identified_pr_required"), lambda g, b: g["abort_contract"]["identified_pr_required"]),
    (("abort_prompt", "prompt_originated_inbound_edges"), lambda g, b: g["abort_contract"]["prompt_inbound_edges"]),
    (("abort_prompt", "automatic_inbound_edges"), lambda g, b: g["abort_contract"]["automatic_inbound_edges"]),
    (("graph_proofs", "route_edge_count"), lambda g, b: len(g["edges"])),
    (("source_snapshot", "frozen_candidate_graph", "sha256"), lambda g, b: hashlib.sha256(b).hexdigest()),
    (("source_snapshot", "corrected_source_manifest", "sha256"),
     lambda g, b: g["source_bindings"]["source_manifest_file_sha256"]),
    (("source_snapshot", "corrected_source_manifest", "source_snapshot_sha256"),
     lambda g, b: g["source_bindings"]["source_snapshot_sha256"]),
]

# ---------------------------------------------------------------------------------------------
# §6.3 contract-only value table. Ops: ("set", path, value) | ("delete", path). A W-8 rename is a
# delete of the old key plus a set of the new one. SUCCESSOR_ORACLE_SHA256 is the one E2 value
# (§5.11 step 2); `generate` re-checks it against the oracle file's bytes.
# ---------------------------------------------------------------------------------------------
SUCCESSOR_ORACLE_SHA256 = "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52"
W4 = ("PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session "
      "as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion "
      "that he manually merged it.")
W8_CONTINUATION = ("PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, "
                   "which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent.")
W8_REPLAN = ("A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session "
             "that Nathan creates, with a new Proceed for the new plan (D23-F).")
TC = ("transition_contract",)
VALUE_TABLE = [
    ("set", ("contract_revision",), "4.1.0"),
    # transition_contract (V-6): four deletions, five additions, the 12-entry prohibited list.
    ("delete", TC + ("status_completed_work_decisions_constraints_unresolved_authority",)),
    ("delete", TC + ("epic_change_and_work_unit",)),
    ("delete", TC + ("next_action_and_expected_output",)),
    ("delete", TC + ("every_required_repository_and_pr_reference",)),
    ("set", TC + ("artifact_repository_paths_with_labels",), True),
    ("set", TC + ("pr_reference_when_continuing",), True),
    ("set", TC + ("exceptional_context_only",), True),
    ("set", TC + ("no_branch_or_commit",), True),
    ("set", TC + ("no_restated_artifact_content",), True),
    ("set", TC + ("prohibited_references",), [
        "Library ID", "unlinked filename", "above", "conversation reconstruction",
        "model/strength/reasoning/eligibility/suitability/account/configuration route",
        "branch", "commit", "restated artifact content",
        "menu", "metadata-only summary", "blank form", "placeholder after publication"]),
    # receiver_compatibility (V-5): all seven receivers.
    ("set", ("receiver_compatibility",), {
        "PR-20": {"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"],
                  "earlier_cycle_pr_is_landed_history": True, "existing_work_unit_replan": True,
                  "new_proceed_for_new_plan": True, "new_top_level_session_created_by_nathan": True},
        "PR-30": {"accepted_contexts": ["PROCEEDED_PREPUBLICATION", "OPEN_PR_POSTPUBLICATION_RECOVERY"],
                  "accepted_final_replay": False, "delta_in_force_from_turn_after_addendum_created": True,
                  "overlay_approvals": ["RS-20:APPROVE", "ESC-40:APPROVE", "IA-30:QUALIFYING_DELTA_APPROVE"]},
        "PR-35": {"context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION", "dedicated_top_level_pr35_session": True,
                  "same_workspace_worktree_branch_open_pr_original_proceed": True},
        "PR-40": {"attribution_skill_read_only": True,
                  "entry_fact": "MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED",
                  "independent_actual_merged_state_and_landed_lineage_verification": True,
                  "prior_merge_pending_is_historical_premerge_evidence": True},
        "RS-20": {"accepted_inputs": ["RESCOPE_REQUEST", "RESCOPE_PROPOSAL"], "bounded_implementation_delta_only": True,
                  "decision_owner": "SAME_WHOLE_CHANGE_IA"},
        "RS-30": {"invented_ia_denial": False, "same_artifact_type_author_and_decision_owner": True},
        "RS-40": {"accepted_approval": "RS-20:RESCOPE_REVIEW:APPROVE", "contexts": ["PR-30_POSTPUBLICATION", "PR-35"],
                  "delta_in_force_from_turn_after_addendum_created": True, "original_proceed": True,
                  "requires_existing_open_pr": True},
    }),
    # route_graph (V-4, C8): contract-only keys; the three rescope sequences are mirrored.
    ("set", ("route_graph", "ordinary_pr_work_unit"), ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"]),
    ("set", ("route_graph", "pr35_merge_pending_fallback"), ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]),
    ("set", ("route_graph", "pr40_reject_replan"), ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"]),
    # route_graph_semantics (W-4, W-8): rename + two values.
    ("delete", ("route_graph_semantics", "same_session_phase_continuation")),
    ("set", ("route_graph_semantics", "pr30_to_pr35_phase_continuation"), W8_CONTINUATION),
    ("set", ("route_graph_semantics", "pr40_entry"), W4),
    ("set", ("route_graph_semantics", "pr40_reject_replan"), W8_REPLAN),
    # pr_development_contract contract-only fields (A1-6, W-8).
    ("set", ("pr_development_contract", "pr30_ownership"), [
        "recovery", "implementation", "local testing", "coherent commit creation",
        "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session"]),
    ("set", ("pr_development_contract", "primary_skill_revision"), "1.3.0"),
    # rescope_contract.preserved_lineage[1] (sweep:10).
    ("set", ("rescope_contract", "preserved_lineage"), [
        "PR_RETURN_PHASE", "PR_PHASE_SESSION", "WORKSPACE", "WORKTREE", "BRANCH", "OPEN_PR_WHEN_ONE_EXISTS", "COMMIT",
        "ORIGINAL_PROCEED", "COMPLETED_WORK", "TESTS", "REVIEWS", "CI_STATE", "DECISION", "ARTIFACTS",
        "UNRESOLVED_WORK"]),
    # protected identities and graph proofs (A1-2, V-7).
    ("set", ("protected_identities", "r1_oracle_changed"), True),
    ("set", ("protected_identities", "r1_oracle_sha256"), SUCCESSOR_ORACLE_SHA256),
    ("set", ("graph_proofs", "protected_r1_46_rows_unchanged"), False),
    # §12 OQ-14 / §5.8: the historical oracle and map filenames join the non-executable references.
    ("set", ("historical_non_executable_references",), [
        "integrated-qa-readiness-correction.json", "final-cycle-scan-extension.json",
        "alpha-feedback-correction.json", "strength-analyzer-middleware-correction.json",
        "epic-alpha-repair-correction.json", "epic-reengineering-correction.json",
        "glow-hde-canonical-change-flow-r1.json", "glow-hde-canonical-change-flow-r1-runtime-map.json"]),
]


def mirrored_paths(graph: dict) -> list[tuple]:
    paths = [p for p, _ in TOP_AND_NESTED]
    for node in graph["nodes"]:
        for field in MEMBER_PAIRS:
            paths.append(("member_registry", node["id"], field))
    return paths


def _set(obj: dict, path: tuple, value) -> None:
    for key in path[:-1]:
        obj = obj.setdefault(key, {})
    obj[path[-1]] = copy.deepcopy(value)


def _delete(obj: dict, path: tuple) -> None:
    for key in path[:-1]:
        obj = obj[key]
    del obj[path[-1]]


def _overlaps(a: tuple, b: tuple) -> bool:
    n = min(len(a), len(b))
    return a[:n] == b[:n]


def strip(contract: dict, graph: dict) -> dict:
    out = copy.deepcopy(contract)
    for path in mirrored_paths(graph):
        _delete(out, path)
    return out


def regenerate(template: dict, graph: dict, graph_bytes: bytes, value_table=()) -> dict:
    out = copy.deepcopy(template)
    assert "PF10_POST_DRAIN_VERIFICATION" not in graph["state_vocabularies"], "retired drainage vocabulary in graph"
    assert "pf10_post_drain_verification" not in out, "retired drainage key in template"
    mirrored = mirrored_paths(graph)
    for op in value_table:
        assert op[1][0] != "member_registry" and not any(_overlaps(op[1], m) for m in mirrored), \
            f"value-table entry targets a mirrored path: {op[1]}"
    for path, get in TOP_AND_NESTED:
        _set(out, path, get(graph, graph_bytes))
    for node in graph["nodes"]:
        for field, gfield in MEMBER_PAIRS.items():
            _set(out, ("member_registry", node["id"], field), node[gfield])
    for op in value_table:
        if op[0] == "set":
            _set(out, op[1], op[2])
        elif op[0] == "delete":
            _delete(out, op[1])
        else:
            raise ValueError(op)
    assert set(out["member_registry"]) == {n["id"] for n in graph["nodes"]}, "member set != graph node set"
    return out


def serialise(contract: dict) -> bytes:
    return (json.dumps(contract, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def graph_block(path: str) -> bytes:
    """§6.1 input 1: embedded JSON of a graph_parts.py build (or an already-extracted block)."""
    raw = open(path, encoding="utf-8").read()
    if raw.lstrip().startswith("{"):
        return raw.encode("utf-8")
    lines = raw.split("\n")
    start = next(i for i, line in enumerate(lines) if line == "```json")
    end = max(i for i, line in enumerate(lines) if line == "```")
    return ("\n".join(lines[start + 1:end]) + "\n").encode("utf-8")


def _build(builder: str, parts: str, out_md: str) -> tuple[dict, bytes, str]:
    r = subprocess.run([sys.executable, builder, "build", parts, out_md], capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    assert r.returncode == 0 and "WARNING" not in r.stdout + r.stderr, r.stdout + r.stderr
    b = graph_block(out_md)
    return json.loads(b), b, " | ".join(r.stdout.split("\n")).strip()


def acceptance(base_parts: str, builder: str, template_path: str, fv_scripts: str, scratch: str) -> int:
    sys.path.insert(0, fv_scripts)
    import validate_gcfpe_20260914 as V  # noqa: E402
    target_sha, target_bytes = "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b", 606657
    os.makedirs(scratch, exist_ok=True)
    t_bytes = open(template_path, "rb").read()
    assert hashlib.sha256(t_bytes).hexdigest() == target_sha
    contract = json.loads(t_bytes)
    rep: dict = {}
    g0, b0, rep["build_today"] = _build(builder, base_parts, os.path.join(scratch, "graph_today.md"))
    rep["build_today_bytes_sha256"] = [len(b0), hashlib.sha256(b0).hexdigest()]
    paths = mirrored_paths(g0)
    rep["mirrored_paths"] = [len(paths), sum(1 for p in paths if p[0] != "member_registry"),
                             sum(1 for p in paths if p[0] == "member_registry")]
    stripped = strip(contract, g0)
    sb = serialise(stripped)
    rep["stripped_template"] = [len(sb), hashlib.sha256(sb).hexdigest()]
    rep["noop_on_stripped_equals_target"] = hashlib.sha256(sb).hexdigest() == target_sha
    regen = regenerate(stripped, g0, b0)
    out = serialise(regen)
    rep["regenerated"] = [len(out), hashlib.sha256(out).hexdigest()]
    rep["ACCEPTANCE_PASS"] = hashlib.sha256(out).hexdigest() == target_sha and len(out) == target_bytes
    rep["validate_graph_contract"] = V.validate_graph_contract(regen, g0)
    rep["validate_contract"] = V.validate_contract(regen)
    rep["routing_surface"] = list(V.routing_surface(regen))
    lo = []
    for i in range(len(TOP_AND_NESTED)):
        saved = TOP_AND_NESTED[:]
        del TOP_AND_NESTED[i]
        try:
            if hashlib.sha256(serialise(regenerate(stripped, g0, b0))).hexdigest() == target_sha:
                lo.append(".".join(saved[i][0]))
        finally:
            TOP_AND_NESTED[:] = saved
    saved_pairs = dict(MEMBER_PAIRS)
    for f in list(saved_pairs):
        MEMBER_PAIRS.pop(f)
        try:
            if hashlib.sha256(serialise(regenerate(stripped, g0, b0))).hexdigest() == target_sha:
                lo.append("member_registry.*." + f)
        finally:
            MEMBER_PAIRS.clear(); MEMBER_PAIRS.update(saved_pairs)
    rep["leave_one_out_not_load_bearing"] = lo
    # Negative control: one changed edge condition in a scratch copy of the parts.
    neg = os.path.join(scratch, "parts_neg")
    shutil.rmtree(neg, ignore_errors=True)
    shutil.copytree(base_parts, neg)
    p10 = os.path.join(neg, "prompts", "PR-10.json")
    part = json.load(open(p10, encoding="utf-8"))
    hits = 0
    for e in part["edges"]:
        for br in e["route_branches"]:
            if br["branch_id"] == "material_boundary" and e["to"] == "RS-10":
                br["condition"] += " (negative control)"
                hits += 1
    assert hits == 1
    open(p10, "w", encoding="utf-8").write(json.dumps(part, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    g1, b1, rep["neg_build"] = _build(builder, neg, os.path.join(scratch, "graph_neg.md"))
    rep["neg_build_bytes_sha256"] = [len(b1), hashlib.sha256(b1).hexdigest()]
    regen1 = regenerate(stripped, g1, b1)
    rep["neg_changed_top_level_keys"] = sorted(k for k in set(regen) | set(regen1) if regen.get(k) != regen1.get(k))
    rep["neg_regenerated_vs_new_graph"] = V.validate_graph_contract(regen1, g1)
    rep["neg_stale_contract_vs_new_graph"] = V.validate_graph_contract(contract, g1)
    rep["neg_routing_surface"] = list(V.routing_surface(regen1))
    rep["NEGATIVE_CONTROL_PASS"] = (rep["neg_regenerated_vs_new_graph"] == []
                                    and rep["neg_stale_contract_vs_new_graph"] != [])
    print(json.dumps(rep, indent=1))
    return 0 if rep["ACCEPTANCE_PASS"] and rep["NEGATIVE_CONTROL_PASS"] and not lo else 1


def generate(graph_path: str, template_path: str, oracle_path: str, outs: list[str]) -> int:
    gb = graph_block(graph_path)
    g = json.loads(gb)
    assert hashlib.sha256(open(oracle_path, "rb").read()).hexdigest() == SUCCESSOR_ORACLE_SHA256, "oracle digest"
    assert g["protected_identities"]["r1_oracle_sha256"] == SUCCESSOR_ORACLE_SHA256, "graph G16 not applied"
    t = json.loads(open(template_path, "rb").read())
    out = serialise(regenerate(t, g, gb, VALUE_TABLE))
    for p in outs:
        open(p, "wb").write(out)
    print(json.dumps({"graph": [len(gb), hashlib.sha256(gb).hexdigest()],
                      "contract": [len(out), hashlib.sha256(out).hexdigest()], "written": outs}, indent=1))
    return 0


if __name__ == "__main__":
    if sys.argv[1] == "acceptance":
        raise SystemExit(acceptance(*sys.argv[2:7]))
    if sys.argv[1] == "generate":
        raise SystemExit(generate(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]))
    raise SystemExit(__doc__)
