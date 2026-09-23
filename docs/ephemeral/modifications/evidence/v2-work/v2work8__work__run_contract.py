"""Clean control and must-fail regressions for 8b.7 on the §12 candidate. Pass = findings(mutated) - findings(clean) == expected set."""
import sys, json, copy, importlib.util
sys.dont_write_bytecode = True
B = '/tmp/claude-0/v2work8/M/flowmaster-validate/scripts'
sys.path.insert(0, B)
spec = importlib.util.spec_from_file_location('V', B + '/validate_gcfpe_20260914.py')
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
from cand import build
c0, g0 = build()
def run(c, g):
    return set(V.validate_contract(c)), set(V.validate_graph_contract(c, g))
C0, G0 = run(c0, g0)
print('CLEAN validate_contract:', sorted(C0)); print('CLEAN validate_graph_contract:', sorted(G0))
print('routing surface:', V.routing_surface(c0), 'edges', len(g0['edges']))
def edge(c, frm, to):
    r = [e for e in c['route_edges'] if e['from'] == frm and e['to'] == to]
    assert len(r) == 1, (frm, to, len(r)); return r[0]
cases = []
def case(rid, mut, exp_c, exp_g=None, both=False, gmut=None):
    c = copy.deepcopy(c0); g = copy.deepcopy(g0)
    if mut: mut(c)
    if gmut: gmut(g)
    if both:
        g['edges'] = c['route_edges']; g['state_routes'] = c['state_routes']
    C, G = run(c, g)
    dc, dg = sorted(C - C0), sorted(G - G0)
    ok = dc == sorted(exp_c) and (exp_g is None or dg == sorted(exp_g)) and not (C0 - C)
    cases.append((rid, ok, dc, dg))
RS = 'ROUTING_SURFACE_CHANGED'
pd = lambda c: c['pr_development_contract']
case('R-AB-1', lambda c: pd(c)['added_boundaries'].__setitem__('session', 0), ['PR35_ADDED_BOUNDARY'])
case('R-AB-2', lambda c: pd(c)['added_boundaries'].__setitem__('cross_session_route', 0), ['PR35_ADDED_BOUNDARY'])
case('R-AB-3', lambda c: pd(c)['added_boundaries'].__setitem__('proceed', 1), ['PR35_ADDED_BOUNDARY'])
case('R-PC', lambda c: pd(c)['shared_exactly_one'].insert(2, 'dedicated PR-development session'), ['PR_PHASE_CONTINUITY'])
case('R-V-1', lambda c: pd(c).__setitem__('pr35_result_vocabulary', [x for x in V.EXPECTED_PR35_RESULTS if x != 'MERGE_OBSERVED']), ['PR35_RESULT_VOCABULARY'])
case('R-V-2', lambda c: c['member_registry']['PR-35']['result_states'].remove('MERGE_OBSERVED'), ['PR35_STATE_ROUTES', 'STATE_REGISTRY_MISMATCH:PR-35'])
case('R-DE-1', lambda c: c['route_edges'].append({'from': 'PR-35', 'to': 'PR-40', 'automatic': False}), ['DIRECT_PR35_PR40_EDGE', RS])
case('R-DE-2', lambda c: edge(c, 'PR-35', 'PR-40').__setitem__('automatic', True), ['DIRECT_PR35_PR40_EDGE', RS])
case('R-DE-3', lambda c: edge(c, 'RS-40', 'PR-40').__setitem__('automatic', True), ['DIRECT_PR35_PR40_EDGE', RS])
case('R-DE-4', lambda c: edge(c, 'PR-35', 'PR-40')['route_branches'][0].__setitem__('condition', 'PR-35 returns its result'), ['DIRECT_PR35_PR40_EDGE', RS])
case('R-DE-5', lambda c: (edge(c, 'PR-35', 'PR-40').__setitem__('state_predicates', ['MERGE_PENDING']), edge(c, 'PR-35', 'PR-40')['route_branches'][0].update({'state': 'MERGE_PENDING', 'applicable_states': ['MERGE_PENDING']})), ['DIRECT_PR35_PR40_EDGE', RS])
case('R-DE-6', lambda c: c['route_edges'].remove(edge(c, 'RS-40', 'PR-40')), ['DIRECT_PR35_PR40_EDGE', RS, 'STATE_EDGE_MISMATCH:RS-40:merge_observed'])
case('R-DE-7', lambda c: c['route_edges'].append({'from': 'PR-30', 'to': 'PR-40', 'automatic': False}), ['DIRECT_PR30_PR40_EDGE', RS])
case('R-DE-8', lambda c: c['route_edges'].append(copy.deepcopy(edge(c, 'PR-35', 'PR-40'))), ['DIRECT_PR35_PR40_EDGE', RS], ['GRAPH_DIRECT_PR40_EDGE'], both=True)
case('R-MB-1', lambda c: c['route_edges'].remove(edge(c, 'NATHAN_MANUAL_MERGE_ASSERTION', 'PR-40')), ['PR40_MANUAL_MERGE_BOUNDARY', RS])
case('R-MB-2', lambda c: edge(c, 'NATHAN_MANUAL_MERGE_ASSERTION', 'PR-40').__setitem__('automatic', True), ['PR40_MANUAL_MERGE_BOUNDARY', RS])
case('R-MB-3', lambda c: edge(c, 'DOC-20', 'PR-40')['route_branches'][0].__setitem__('condition', 'actual merged state review is required'), ['PR40_MANUAL_MERGE_BOUNDARY', RS])
case('R-MB-4', lambda c: c['route_edges'].append({'from': 'QA-10', 'from_kind': 'prompt', 'to': 'PR-40', 'automatic': False, 'route_branches': [{'condition': 'x'}]}), ['PR40_MANUAL_MERGE_BOUNDARY', RS])
pm = lambda c: c['post_merge_three_event_contract']
case('R-PM-1', lambda c: pm(c).__setitem__('direct_PR35_to_PR40_automatic_edge', True), ['POST_MERGE_CONTRACT'])
case('R-PM-2', lambda c: pm(c)['event_2'].__setitem__('fact', 'product_owner_manual_merge_assertion'), ['POST_MERGE_THREE_EVENTS'])
case('R-PM-3', lambda c: pm(c).__setitem__('agent_merge_authorized', True), ['POST_MERGE_CONTRACT'])
case('R-PM-4', lambda c: pm(c)['event_2'].__setitem__('time', 'observed by the subscribed PR-35 session, else asserted at the later PR-40 invocation'), ['POST_MERGE_THREE_EVENTS'])
case('R-PM-5', lambda c: pm(c)['observed_merge_edges'].pop(1), ['POST_MERGE_CONTRACT'])
case('R-PM-6', lambda c: pm(c)['observed_merge_edges'][0].__setitem__('automatic', True), ['POST_MERGE_CONTRACT'])
case('R-RG-1', lambda c: c['route_graph'].__setitem__('ordinary_pr_work_unit', ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]), ['ROUTE_GRAPH_SHORTHAND'])
case('R-RG-2', lambda c: c['route_graph'].pop('pr40_reject_replan'), ['ROUTE_GRAPH_SHORTHAND'])
case('R-RG-3', lambda c: c['route_graph'].__setitem__('pr35_no_subscription_fallback', c['route_graph'].pop('pr35_merge_pending_fallback')), ['ROUTE_GRAPH_SHORTHAND'])
def to30(c):
    [e.__setitem__('to', 'PR-30') for e in c['route_edges'] if e['from'] == 'PR-40' and e['route_branches'][0]['branch_id'] == 'reject_replan']
    [r.__setitem__('destinations', ['PR-30']) for r in c['state_routes']['PR-40'] if r.get('branch_id') == 'reject_replan']
case('R-RP-1', to30, ['PR40_REJECT_REPLAN_ROUTE', RS])
case('R-RP-2', lambda c: c['rescope_contract'].__setitem__('new_proceed_required', True), ['RESCOPE_CONTRACT'])
rc = lambda c: c['receiver_compatibility']
case('R-RC-1', lambda c: rc(c).__setitem__('PR-35', {"context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION", "same_session_workspace_worktree_branch_open_pr_original_proceed": True}), ['RECEIVER_CONTRACT:PR-35'])
case('R-RC-2', lambda c: rc(c)['PR-40'].__setitem__('nathan_manual_merge_assertion_required', True), ['RECEIVER_CONTRACT:PR-40'])
case('R-RC-3', lambda c: rc(c)['PR-30']['accepted_contexts'].append('PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT'), ['RECEIVER_CONTRACT:PR-30'])
case('R-RC-4', lambda c: rc(c).pop('PR-20'), ['RECEIVER_CONTRACT:PR-20'])
case('R-RC-5', lambda c: rc(c)['RS-40'].__setitem__('accepted_approval', 'PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT'), ['RECEIVER_CONTRACT:RS-40'])
case('R-RC-6', lambda c: rc(c)['PR-40'].__setitem__('entry_fact', 'OBSERVED_MERGE_EVENT_OR_NATHAN_ASSERTION_WHERE_NO_SUBSCRIPTION'), ['RECEIVER_CONTRACT:PR-40'])
tc = lambda c: c['transition_contract']
case('R-HC-1', lambda c: tc(c).__setitem__('status_completed_work_decisions_constraints_unresolved_authority', True), ['HANDOFF_CONTRACT'])
case('R-HC-2', lambda c: tc(c).__setitem__('actual_pasteable_complete_prompt', False), ['HANDOFF_CONTRACT'])
case('R-HC-3', lambda c: tc(c)['prohibited_references'].remove('branch'), ['HANDOFF_PROHIBITED_REFERENCES'])
case('R-HC-4', lambda c: tc(c).pop('no_branch_or_commit'), ['HANDOFF_CONTRACT'])
case('R-HC-5', lambda c: tc(c).__setitem__('every_required_repository_and_pr_reference', True), ['HANDOFF_CONTRACT'])
case('R-HC-6', None, [], ['GRAPH_HANDOFF_PROHIBITED_REFERENCES'], gmut=lambda g: g['handoff_contract']['prohibited'].append('phase history'))
case('R-HC-7', lambda c: tc(c)['prohibited_references'].remove('menu'), ['HANDOFF_PROHIBITED_REFERENCES'], ['GRAPH_HANDOFF_PROHIBITED_REFERENCES'])
case('R-R1-1', lambda c: c['protected_identities'].__setitem__('r1_oracle_changed', False), ['PROTECTED_IDENTITIES'])
case('R-R1-2', lambda c: c['graph_proofs'].__setitem__('protected_r1_46_rows_unchanged', True), ['GRAPH_PROOFS'])
case('R-R1-3', lambda c: c['protected_identities'].__setitem__('pr35_adds_r1_row', True), ['PROTECTED_IDENTITIES'])
case('R-ID', lambda c: c.__setitem__('contract_revision', '4.0.6'), ['CONTRACT_IDENTITY'])
case('R-PS', lambda c: pd(c).__setitem__('primary_skill_revision', '1.2.5'), ['PR_DEVELOPMENT_CONTRACT'])
case('R-OWN', lambda c: pd(c)['pr30_ownership'].__setitem__(5, 'complete same-session PR-35 handoff'), ['PR_DEVELOPMENT_CONTRACT'])
case('R-LIN', lambda c: c['rescope_contract']['preserved_lineage'].__setitem__(1, 'PR_DEVELOPMENT_SESSION'), ['RESCOPE_CONTRACT'])
def sem_old(c):
    s = c['route_graph_semantics']; s.pop('pr30_to_pr35_phase_continuation')
    s['same_session_phase_continuation'] = "PR-30 to PR-35 is one lawful same-session phase continuation inside GCF-17, not a new work unit or cross-session route."
case('R-SEM-1', sem_old, ['ROUTE_GRAPH_SEMANTICS'])
case('R-SEM-2', lambda c: c['route_graph_semantics'].__setitem__('pr40_entry', "Requires Nathan's later manual-merge assertion and PR-40's independent read-only verification."), ['ROUTE_GRAPH_SEMANTICS'])
case('R-SEM-3', lambda c: c['route_graph_semantics'].pop('pr40_reject_replan'), ['ROUTE_GRAPH_SEMANTICS'])
case('R-ROLE', lambda c: c['member_registry']['PR-35'].__setitem__('receiving_role', "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request."), ['PR35_TOP_LEVEL_ROLE'])
for x in cases:
    print(('PASS ' if x[1] else 'FAIL ') + x[0], '| contract +', x[2], '| graph +', x[3])
print(sum(1 for x in cases if x[1]), 'of', len(cases), 'regressions exact')
