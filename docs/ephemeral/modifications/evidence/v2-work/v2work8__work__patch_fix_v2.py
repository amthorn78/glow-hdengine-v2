"""§8b.9 v2 deltas over the drafter's simulated runner/scenarios: per-variant labels (C8), single-defect proof, new mutation counterparts."""
import sys, json
sys.dont_write_bytecode = True
from common import apply
root = sys.argv[1] + '/flowmaster-validate'
R = root + '/scripts/run_gcfpe_20260914_fixtures.py'
apply(R, [
 # variant-level expected_rule overrides the row label (C8, §12 verifier contradiction 8)
 ('                "expected_rule": negative_rules.get(row["id"]) if row["polarity"] == "NEGATIVE" else None,\n            })\n',
  '                "expected_rule": variant.get("expected_rule", negative_rules.get(row["id"])) if row["polarity"] == "NEGATIVE" else None,\n            })\n'
  '            if row["id"] == "REPLAN-NEG-01":\n'
  '                # Single-defect proof: the variant is REPLAN-POS-01 plus exactly its own defect,\n'
  '                # so reverting that one fact must restore acceptance.\n'
  '                repair = REPLAN_DEFECT_REPAIR.get((variant.get("expected_rule"), variant["name"]))\n'
  '                cases.append({\n'
  '                    "name": f"{row[\'id\']}::{variant[\'name\']}::single-defect",\n'
  '                    "passed": repair is not None and project_behavior(source, row["rule"], {**variant["input"], **repair}) == "REPLAN_NEW_PROCEED_ACCEPTED",\n'
  '                })\n'),
 ('EXPECTED_NEGATIVE_RULES = {',
  'REPLAN_DEFECT_REPAIR = {\n'
  '    ("PR40_REJECT_REPLAN_PROCEED", "second-proceed-same-plan"): {"second_proceed_same_plan": False},\n'
  '    ("PR40_REJECT_REPLAN_PROCEED", "proceed-between-pr30-and-pr35"): {"proceed_between_pr30_and_pr35": False},\n'
  '    ("PR40_REJECT_REPLAN_ROUTE", "reject-routed-to-pr30"): {"receiver": "PR-20"},\n'
  '}\n'
  'EXPECTED_REPLAN_VARIANT_RULES = {name: rule for rule, name in REPLAN_DEFECT_REPAIR}\n\n'
  'EXPECTED_NEGATIVE_RULES = {'),
 # document check: REPLAN-NEG-01 variant labels are exact
 ('    return sorted(set(errors))\n\n\ndef run(',
  '    replan = [row for row in rows or [] if isinstance(row, dict) and row.get("id") == "REPLAN-NEG-01"]\n'
  '    if len(replan) != 1 or {v.get("name"): v.get("expected_rule") for v in replan[0].get("variants", []) if isinstance(v, dict)} != EXPECTED_REPLAN_VARIANT_RULES:\n'
  '        errors.append("FIXTURE_REPLAN_VARIANT_RULES")\n'
  '    return sorted(set(errors))\n\n\ndef run('),
 # new mutation counterparts for the checks §12 adds
 ('    mutation("reject-r1-oracle-unchanged-claim",',
  '    mutation("reject-no-subscription-fallback-shorthand", lambda c: c["route_graph"].__setitem__("pr35_no_subscription_fallback", c["route_graph"].pop("pr35_merge_pending_fallback")), "ROUTE_GRAPH_SHORTHAND")\n'
  '    mutation("reject-same-session-phase-semantics", lambda c: c["route_graph_semantics"].__setitem__("same_session_phase_continuation", c["route_graph_semantics"].pop("pr30_to_pr35_phase_continuation")), "ROUTE_GRAPH_SEMANTICS")\n'
  '    mutation("reject-pr35-role-without-top-level-clause", lambda c: c["member_registry"]["PR-35"].__setitem__("receiving_role", "You are the dedicated PR-35 session for one work unit, entered from PR-30\'s handoff; you continue its existing pull request."), "PR35_TOP_LEVEL_ROLE")\n'
  '    mutation("reject-event-2-time-without-fallback-predicate", lambda c: c["post_merge_three_event_contract"]["event_2"].__setitem__("time", "later PR-40 invocation"), "POST_MERGE_THREE_EVENTS")\n'
  '    mutation("reject-missing-rs40-observed-merge-record", lambda c: c["post_merge_three_event_contract"]["observed_merge_edges"].pop(1), "POST_MERGE_CONTRACT")\n'
  '    mutation("reject-same-session-pr30-ownership", lambda c: c["pr_development_contract"]["pr30_ownership"].__setitem__(5, "complete same-session PR-35 handoff"), "PR_DEVELOPMENT_CONTRACT")\n'
  '    mutation("reject-shared-session-rescope-lineage", lambda c: c["rescope_contract"]["preserved_lineage"].__setitem__(1, "PR_DEVELOPMENT_SESSION"), "RESCOPE_CONTRACT")\n'
  '    mutation("reject-receiver-pr20-removed", lambda c: c["receiver_compatibility"].pop("PR-20"), "RECEIVER_CONTRACT:PR-20")\n'
  '    mutation("reject-handoff-branch-flag-removed", lambda c: c["transition_contract"].pop("no_branch_or_commit"), "HANDOFF_CONTRACT")\n'
  '    mutation("reject-r1-oracle-unchanged-claim",'),
], 'runner')
S = root + '/fixtures/gcfpe-20260914.1-091426.1/scenarios.json'
s = open(S, encoding='utf-8').read()
POS = {"decision": "REJECT", "precise_in_scope_defect": True, "receiver": "PR-20", "new_top_level_session_nathan_creates": True, "new_plan": True, "new_proceed_on_new_plan": True}
def row_json(d): return json.dumps(d, ensure_ascii=False, separators=(',', ':'))
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if '"id":"REPLAN-NEG-01"' in l]
assert len(idx) == 1
old = json.loads(lines[idx[0]].strip().rstrip(','))
new = {"id": "REPLAN-NEG-01", "polarity": "NEGATIVE", "rule": "replan",
       "input": {**POS, "receiver": "PR-30", "second_proceed_same_plan": True, "proceed_between_pr30_and_pr35": True},
       "expected": "VALIDATION_FAILURE", "variants": [
   {"name": "second-proceed-same-plan", "input": {**POS, "second_proceed_same_plan": True}, "expected": "VALIDATION_FAILURE", "expected_rule": "PR40_REJECT_REPLAN_PROCEED"},
   {"name": "proceed-between-pr30-and-pr35", "input": {**POS, "proceed_between_pr30_and_pr35": True}, "expected": "VALIDATION_FAILURE", "expected_rule": "PR40_REJECT_REPLAN_PROCEED"},
   {"name": "reject-routed-to-pr30", "input": {**POS, "receiver": "PR-30"}, "expected": "VALIDATION_FAILURE", "expected_rule": "PR40_REJECT_REPLAN_ROUTE"}]}
trail = ',' if lines[idx[0]].rstrip().endswith(',') else ''
indent = lines[idx[0]][:len(lines[idx[0]]) - len(lines[idx[0]].lstrip())]
lines[idx[0]] = indent + row_json(new) + trail
open(S, 'w', encoding='utf-8').write('\n'.join(lines))
json.loads(open(S).read())
print('patched runner and scenarios')
