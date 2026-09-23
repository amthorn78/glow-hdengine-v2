"""Measurement candidate: §6's prototype after-state with every §12 value applied (V-1..V-8, W-1, W-2, W-8, W-10).
Stand-ins: the R1 successor digest (§5 supplies it). Not a deliverable; §4/§6 own the values."""
import json, copy
C0 = json.load(open('/tmp/claude-0/spec/s6/after_contract.json'))
G0 = json.load(open('/tmp/claude-0/spec/s6/after_graph.json'))
W1 = "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session."
W2 = "You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35."
V8_OLD = "and return MERGE_PENDING without merging."
V8_NEW = "and return MERGE_PENDING without merging; return MERGE_OBSERVED when an active subscription observes Nathan's merge."
W4 = "PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it."
W8_CONT = "PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent."
W8_REPLAN = "A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new Proceed for the new plan (D23-F)."
V3_TIME = "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge"
OBS = [{"from": f, "to": "PR-40", "branch_id": "merge_observed", "state": "MERGE_OBSERVED", "automatic": False, "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"} for f in ("PR-35", "RS-40")]
RECEIVERS = copy.deepcopy(C0['receiver_compatibility'])
RECEIVERS['PR-20'] = {"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"], "earlier_cycle_pr_is_landed_history": True, "existing_work_unit_replan": True, "new_proceed_for_new_plan": True, "new_top_level_session_created_by_nathan": True}
RECEIVERS['PR-35'] = {"context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION", "dedicated_top_level_pr35_session": True, "same_workspace_worktree_branch_open_pr_original_proceed": True}
RECEIVERS['PR-40'] = {"attribution_skill_read_only": True, "entry_fact": "MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED", "independent_actual_merged_state_and_landed_lineage_verification": True, "prior_merge_pending_is_historical_premerge_evidence": True}
TRANSITION = {
 "actual_branch_only": True, "actual_pasteable_complete_prompt": True, "artifact_repository_paths_with_labels": True,
 "blank_form_menu_or_reconstruction_prohibited": True, "block": "NEXT_PROMPT_HANDOFF",
 "exact_destination_full_name_version_direct_notion_url": True, "exactly_one_per_nonterminal_result": True,
 "exceptional_context_only": True, "fence_language": "text", "first_line": "NEXT_PROMPT_HANDOFF",
 "metadata_only_or_routing_summary_prohibited": True, "no_branch_or_commit": True, "no_restated_artifact_content": True,
 "pr_reference_when_continuing": True,
 "prohibited_references": ["Library ID", "unlinked filename", "above", "conversation reconstruction",
   "model/strength/reasoning/eligibility/suitability/account/configuration route",
   "branch", "commit", "restated artifact content", "menu", "metadata-only summary", "blank form", "placeholder after publication"],
 "receiving_role_and_exact_session": True, "terminal_has_no_handoff": True, "transport": "DIRECT_NATIVE_PROMPT_HANDOFF",
}
W10_REQUIRED = ["exact selected prompt full name/version/direct Notion URL", "receiving role and exact session",
 "input artifact repository paths with one-line labels", "pull request reference when the receiver continues an existing PR",
 "minimum exceptional context only for a condition the artifacts do not record"]
def build():
    c = copy.deepcopy(C0); g = copy.deepcopy(G0)
    # V-1
    c['pr_development_contract']['added_boundaries']['cross_session_route'] = 1
    g['pr_continuity_contract']['adds']['cross_session_route'] = 1
    for n in g['nodes']:
        if n.get('id') == 'PR-35':
            n['cross_session_route'] = True; n['adds_session'] = True   # §4 P35-8, P35-9
    # V-2, V-3 (mirrored in graph and contract)
    for d in (c['post_merge_three_event_contract'], g['post_merge_three_event_contract']):
        d['event_2']['time'] = V3_TIME
        d['observed_merge_edges'] = copy.deepcopy(OBS)
    # V-4, route_graph
    c['route_graph']['pr35_merge_pending_fallback'] = ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]
    # V-5
    c['receiver_compatibility'] = copy.deepcopy(RECEIVERS)
    # V-6
    c['transition_contract'] = copy.deepcopy(TRANSITION)
    # W-10 (graph)
    g['handoff_contract']['required'] = list(W10_REQUIRED)
    g['handoff_contract']['prohibited'] = g['handoff_contract']['prohibited'] + ["branch", "commit", "restated artifact content"]
    # W-8
    s = c['route_graph_semantics']; s.pop('same_session_phase_continuation')
    s['pr30_to_pr35_phase_continuation'] = W8_CONT; s['pr40_entry'] = W4; s['pr40_reject_replan'] = W8_REPLAN
    c['pr_development_contract']['pr30_ownership'][5] = "complete PR-35 handoff to the dedicated PR-35 session"
    # W-1, W-2, V-8 (graph nodes mirrored into member_registry)
    for n in g['nodes']:
        if n.get('id') == 'PR-35':
            n['receiving_role'] = W1; n['native_function'] = n['native_function'].replace(V8_OLD, V8_NEW)
        if n.get('id') == 'RS-40':
            n['receiving_role'] = W2
    c['member_registry']['PR-35']['receiving_role'] = W1
    c['member_registry']['PR-35']['native_function'] = c['member_registry']['PR-35']['native_function'].replace(V8_OLD, V8_NEW)
    c['member_registry']['RS-40']['receiving_role'] = W2
    # V-7
    c['graph_proofs']['protected_r1_46_rows_unchanged'] = False
    c['protected_identities']['r1_oracle_changed'] = True
    return c, g
if __name__ == '__main__':
    c, g = build()
    json.dump(c, open('cand_contract.json', 'w'), ensure_ascii=False, indent=2, sort_keys=True)
    json.dump(g, open('cand_graph.json', 'w'), ensure_ascii=False, indent=2, sort_keys=True)
    print('ok', len(g['edges']))
