# HDE-EPIC036 PR-02 Token Evidence Matrix

epic_id=HDE-EPIC036
pf09_task_id=HDE-FERM008
pf09_subtask_id=HDE-FERM008.6
pr_scope=PR-02 governed evidence-loop binding only
selected_route_policy_classification=unsupported_runtime_nonclaim
bodygraph_detail_sufficiency=UNSUPPORTED_RUNTIME_NONCLAIM
v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=false
ops_01_required_by_pr01=false
ops_01_executed_for_pr02=false
live_qa_runbook=false
qa_pass_claim=false
ops_completion_claim=false
pf09_status_movement_claim=false
epic_closeout_claim=false
full_runtime_conformance_claim=false
public_reader_change_claim=false
public_route_claim=false
public_flag_claim=false
public_payload_or_transport_change_claim=false
new_http_home_claim=false
app_side_humandesignapi_credential_ownership_claim=false
raw_payload_persistence_claim=false
ai_scope_claim=false
vendor_v2_specific_tokens=NONE

| Token | Evidence paths | Posture |
| --- | --- | --- |
| TESTS_PASS_OK | tests/evidence/test_hde_epic036_pr02_evidence_loop.py; tests/bodygraph/test_bg_resolve_route_policy.py | Targeted validation only; not a QA PASS claim. |
| DOC_DELTA_PRESENT_OK | audit/docdeltas/hde-epic036_doc_deltas.md; audit/qa/hde-epic036/00_meta/doc_deltas.md | Candidate doc-delta surfaces only; PF-Canon not edited. |
| EVIDENCE_INDEX_UPDATED_OK | docs/evidence/INDEX.json | Human Evidence Index includes PR-02 governed artifacts after update_evidence_index.py. |
| MACHINE_MIRROR_UPDATED_OK | artifacts/evidence_index.jsonl | Machine Evidence Mirror includes PR-02 governed artifacts after update_evidence_index.py. |
| EVIDENCE_INDEX_HASH_OK | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | Hash sentinels match current ledger bytes. |
| EVIDENCE_PATHS_VALIDATED_OK | tools/evidence/validate_evidence_paths.py; tools/evidence/update_evidence_index.py --check | Closed-rails path/index validation posture. |
| EVIDENCE_PATH_PROOFS_OK | docs/acceptance_map_epic036.json.path_proof.txt; audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt; audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt; audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt; audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt | Sibling path proofs for PR-02 artifacts plus retained PR-01 proofs. |
| JSON_CANONICAL_CHECK_OK | docs/acceptance_map_epic036.json; artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json; artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json; artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json; artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json; artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json | Canonical JSON artifacts only; records-only index entries do not duplicate payload bytes. |
| NO_EXTERNAL_IO_ON_REFUSAL_OK | artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json; tests/bodygraph/test_bg_resolve_route_policy.py | Configured-v2 bg:resolve refuses before legacy BodyGraph request construction. |
| ENV_RAILS_POLICY_OK | audit/qa/hde-epic036/route_policy_decision.log; artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json | Closed rails only: SAFE_MODE=1, ALLOW_NETWORK=0. |

Already-landed PR-01 route-policy evidence:
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`
- `audit/qa/hde-epic036/route_policy_decision.log`
- `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`

PR-02 evidence-loop artifacts:
- `docs/acceptance_map_epic036.json`
- `audit/qa/hde-epic036/token_evidence_matrix.md`
- `audit/qa/hde-epic036/acceptance_map_viability.log`
- `audit/docdeltas/hde-epic036_doc_deltas.md`
- `audit/qa/hde-epic036/00_meta/doc_deltas.md`

No Live QA runbook execution is claimed. OPS-01 was not executed for PR-02 and no OPS completion is claimed. PF09 status movement remains a separate documentation/status-drain action.
