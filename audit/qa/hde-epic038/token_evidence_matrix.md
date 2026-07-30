# HDE-EPIC038 DEV-01 Token Evidence Matrix

> Nonclaim: all 33 tokens are UNCLAIMED. Matrix construction, artifact presence, historical PASS text, validation, PR creation, and Gate B review do not satisfy an acceptance token.

Each numbered row is canonical; semicolon-separated values are exact bindings.

## 1. `TESTS_PASS_OK`
- Canonical governance token: `TESTS_PASS_OK`
- Acceptance-map token: `TESTS_PASS_OK`
- Manifest token: `TESTS_PASS_OK`
- Test/stable identifier: `tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml); planned commands: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized; python tools/evidence/generate_hde_epic038_closeout.py --check; python -m pytest -q tests/evidence/test_hde_epic038_closeout.py`
- Live QA: `N/A: the planned closeout artifact is repository-local DEV evidence and no Live QA execution is authorized.`
- Primary governed evidence: `audit/EPIC-038_close_report.md`
- Human Index / Machine Mirror artifact keys: `epic038.close_report`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/EPIC-038_close_report.md.path_proof.txt`
- Current posture: UNCLAIMED: planned-new evidence owned by DEV-03 does not exist and has not been executed; DEV-01 makes no token claim.
- Classification: `planned-new`
- Owning task: `DEV-03`
- Intended future claim and prerequisite: Future status may become CLAIMED only after DEV-03 canonically produces `audit/EPIC-038_close_report.md` and `audit/EPIC-038_close_report.md.path_proof.txt`, registers exact artifact key `epic038.close_report`, the planned commands execute successfully on the exact head, and independent Gate B records PASS.

## 2. `DOC_DELTA_PRESENT_OK`
- Canonical governance token: `DOC_DELTA_PRESENT_OK`
- Acceptance-map token: `DOC_DELTA_PRESENT_OK`
- Manifest token: `DOC_DELTA_PRESENT_OK`
- Test/stable identifier: `tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml); planned commands: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized; python tools/evidence/generate_hde_epic038_closeout.py --check; python -m pytest -q tests/evidence/test_hde_epic038_closeout.py`
- Live QA: `N/A: the planned closeout artifact is repository-local DEV evidence and no Live QA execution is authorized.`
- Primary governed evidence: `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md`
- Human Index / Machine Mirror artifact keys: `epic038.closeout_remediation_ledger`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt`
- Current posture: UNCLAIMED: planned-new evidence owned by DEV-02 does not exist and has not been executed; DEV-01 makes no token claim.
- Classification: `planned-new`
- Owning task: `DEV-02`
- Intended future claim and prerequisite: Future status may become CLAIMED only after DEV-02 canonically produces `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md` and `audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt`, registers exact artifact key `epic038.closeout_remediation_ledger`, the planned commands execute successfully on the exact head, and independent Gate B records PASS.

## 3. `EVIDENCE_INDEX_UPDATED_OK`
- Canonical governance token: `EVIDENCE_INDEX_UPDATED_OK`
- Acceptance-map token: `EVIDENCE_INDEX_UPDATED_OK`
- Manifest token: `EVIDENCE_INDEX_UPDATED_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `docs/evidence/INDEX.json`
- Human Index / Machine Mirror artifact keys: `index.human_index`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/evidence/INDEX.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 4. `MACHINE_MIRROR_UPDATED_OK`
- Canonical governance token: `MACHINE_MIRROR_UPDATED_OK`
- Acceptance-map token: `MACHINE_MIRROR_UPDATED_OK`
- Manifest token: `MACHINE_MIRROR_UPDATED_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `artifacts/evidence_index.jsonl`
- Human Index / Machine Mirror artifact keys: `index.machine_mirror`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/evidence_index.jsonl.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 5. `EVIDENCE_INDEX_HASH_OK`
- Canonical governance token: `EVIDENCE_INDEX_HASH_OK`
- Acceptance-map token: `EVIDENCE_INDEX_HASH_OK`
- Manifest token: `EVIDENCE_INDEX_HASH_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `docs/evidence/INDEX.sha256`
- Human Index / Machine Mirror artifact keys: `docs.evidence.INDEX.sha256`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/evidence/INDEX.sha256.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 6. `QA_PRECOMMIT_CHECKLIST_OK`
- Canonical governance token: `QA_PRECOMMIT_CHECKLIST_OK`
- Acceptance-map token: `QA_PRECOMMIT_CHECKLIST_OK`
- Manifest token: `QA_PRECOMMIT_CHECKLIST_OK`
- Test/stable identifier: `tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml); planned commands: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized; python tools/evidence/generate_hde_epic038_closeout.py --check; python -m pytest -q tests/evidence/test_hde_epic038_closeout.py`
- Live QA: `N/A: the planned closeout artifact is repository-local DEV evidence and no Live QA execution is authorized.`
- Primary governed evidence: `audit/qa/hde-epic038/acceptance_map_viability.log`
- Human Index / Machine Mirror artifact keys: `epic038.acceptance_map_viability`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt`
- Current posture: UNCLAIMED: planned-new evidence owned by DEV-03 does not exist and has not been executed; DEV-01 makes no token claim.
- Classification: `planned-new`
- Owning task: `DEV-03`
- Intended future claim and prerequisite: Future status may become CLAIMED only after DEV-03 canonically produces `audit/qa/hde-epic038/acceptance_map_viability.log` and `audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt`, registers exact artifact key `epic038.acceptance_map_viability`, the planned commands execute successfully on the exact head, and independent Gate B records PASS.

## 7. `QA_POSTCOMMIT_CHECKLIST_OK`
- Canonical governance token: `QA_POSTCOMMIT_CHECKLIST_OK`
- Acceptance-map token: `QA_POSTCOMMIT_CHECKLIST_OK`
- Manifest token: `QA_POSTCOMMIT_CHECKLIST_OK`
- Test/stable identifier: `tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml); planned commands: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized; python tools/evidence/generate_hde_epic038_closeout.py --check; python -m pytest -q tests/evidence/test_hde_epic038_closeout.py`
- Live QA: `N/A: the planned closeout artifact is repository-local DEV evidence and no Live QA execution is authorized.`
- Primary governed evidence: `audit/EPIC-038_MANIFEST.json`
- Human Index / Machine Mirror artifact keys: `epic038.manifest`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/EPIC-038_MANIFEST.json.path_proof.txt`
- Current posture: UNCLAIMED: planned-new evidence owned by DEV-03 does not exist and has not been executed; DEV-01 makes no token claim.
- Classification: `planned-new`
- Owning task: `DEV-03`
- Intended future claim and prerequisite: Future status may become CLAIMED only after DEV-03 canonically produces `audit/EPIC-038_MANIFEST.json` and `audit/EPIC-038_MANIFEST.json.path_proof.txt`, registers exact artifact key `epic038.manifest`, the planned commands execute successfully on the exact head, and independent Gate B records PASS.

## 8. `ENV_RAILS_POLICY_OK`
- Canonical governance token: `ENV_RAILS_POLICY_OK`
- Acceptance-map token: `ENV_RAILS_POLICY_OK`
- Manifest token: `ENV_RAILS_POLICY_OK`
- Test/stable identifier: `tests/invariance/test_determinism_env_helper.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-03-po-003`
- Primary governed evidence: `artifacts/runtime/env_matrix.snapshot.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr01.env_matrix_snapshot_v3`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 9. `PREIMAGE_RECOMPUTE_OK`
- Canonical governance token: `PREIMAGE_RECOMPUTE_OK`
- Acceptance-map token: `PREIMAGE_RECOMPUTE_OK`
- Manifest token: `PREIMAGE_RECOMPUTE_OK`
- Test/stable identifier: `tests/evidence/test_determinism_gate_proofs.py; tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-04-po-004`
- Primary governed evidence: `audit/gates/parity/reader_cli/summary.json; audit/gates/parity/reader_cli/ab.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.reader_cli_summary; epic038.pr02.reader_cli_ab`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/gates/parity/reader_cli/summary.json.path_proof.txt; audit/gates/parity/reader_cli/ab.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after `tools.evidence.run_sanity_pipeline.validate_current_reader_cli_determinism` recomputes the canonical preimage with `idempotence_hash` removed, the governed summary records equal 64-hex stored/recomputed hashes and `preimage_hash_match=true`, the exact-head `test` job succeeds, and post-generation Gate D derives the result from finalized outputs.

## 10. `CLI_READER_PARITY_OK`
- Canonical governance token: `CLI_READER_PARITY_OK`
- Acceptance-map token: `CLI_READER_PARITY_OK`
- Manifest token: `CLI_READER_PARITY_OK`
- Test/stable identifier: `tests/adapter/test_compat_http_parity.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-06-po-006`
- Primary governed evidence: `audit/gates/parity/reader_cli/summary.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.reader_cli_summary`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/gates/parity/reader_cli/summary.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 11. `COMPOSITE_ABBA_IDENTITY_OK`
- Canonical governance token: `COMPOSITE_ABBA_IDENTITY_OK`
- Acceptance-map token: `COMPOSITE_ABBA_IDENTITY_OK`
- Manifest token: `COMPOSITE_ABBA_IDENTITY_OK`
- Test/stable identifier: `tests/cli/test_showcompat_parity_and_identity.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-04-po-004`
- Primary governed evidence: `audit/gates/determinism/abba.bytes`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.abba_bytes`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/gates/determinism/abba.bytes.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 12. `TWO_RUN_IDENTITY_OK`
- Canonical governance token: `TWO_RUN_IDENTITY_OK`
- Acceptance-map token: `TWO_RUN_IDENTITY_OK`
- Manifest token: `TWO_RUN_IDENTITY_OK`
- Test/stable identifier: `tests/cli/test_showcompat_parity_and_identity.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-04-po-004`
- Primary governed evidence: `audit/gates/determinism/tworun_identity.sha256`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.tworun_identity`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/gates/determinism/tworun_identity.sha256.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 13. `JSON_CANONICAL_CHECK_OK`
- Canonical governance token: `JSON_CANONICAL_CHECK_OK`
- Acceptance-map token: `JSON_CANONICAL_CHECK_OK`
- Manifest token: `JSON_CANONICAL_CHECK_OK`
- Test/stable identifier: `tests/cli/test_cli_canonical_bytes.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-04-po-004`
- Primary governed evidence: `audit/gates/json_gate/canonical/json_gate_structured_record.json`
- Human Index / Machine Mirror artifact keys: `audit.gates.json_gate.canonical.json_gate_structured_record.json`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 14. `A7_GET_QUOTED_ETAG_OK`
- Canonical governance token: `A7_GET_QUOTED_ETAG_OK`
- Acceptance-map token: `A7_GET_QUOTED_ETAG_OK`
- Manifest token: `A7_GET_QUOTED_ETAG_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 15. `A7_HEAD_PARITY_OK`
- Canonical governance token: `A7_HEAD_PARITY_OK`
- Acceptance-map token: `A7_HEAD_PARITY_OK`
- Manifest token: `A7_HEAD_PARITY_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 16. `A7_304_OMITS_CT_CL_OK`
- Canonical governance token: `A7_304_OMITS_CT_CL_OK`
- Acceptance-map token: `A7_304_OMITS_CT_CL_OK`
- Manifest token: `A7_304_OMITS_CT_CL_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 17. `A7_VARY_AUTH_AE_OK`
- Canonical governance token: `A7_VARY_AUTH_AE_OK`
- Acceptance-map token: `A7_VARY_AUTH_AE_OK`
- Manifest token: `A7_VARY_AUTH_AE_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 18. `A7_ENCODING_INVARIANCE_OK`
- Canonical governance token: `A7_ENCODING_INVARIANCE_OK`
- Acceptance-map token: `A7_ENCODING_INVARIANCE_OK`
- Manifest token: `A7_ENCODING_INVARIANCE_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 19. `A7_TRANSPORT_PROOF_OK`
- Canonical governance token: `A7_TRANSPORT_PROOF_OK`
- Acceptance-map token: `A7_TRANSPORT_PROOF_OK`
- Manifest token: `A7_TRANSPORT_PROOF_OK`
- Test/stable identifier: `tests/http/test_reader_a7_transport.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/reader_success_get_head_304.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_reader_success_composite`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/reader_success_get_head_304.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 20. `ENDPOINTS_CATALOG_OK`
- Canonical governance token: `ENDPOINTS_CATALOG_OK`
- Acceptance-map token: `ENDPOINTS_CATALOG_OK`
- Manifest token: `ENDPOINTS_CATALOG_OK`
- Test/stable identifier: `tests/http/test_endpoint_catalog.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `docs/ENDPOINTS_CATALOG.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.endpoint_catalog`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/ENDPOINTS_CATALOG.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 21. `ENDPOINTS_CATALOG_ENV_GATE_OK`
- Canonical governance token: `ENDPOINTS_CATALOG_ENV_GATE_OK`
- Acceptance-map token: `ENDPOINTS_CATALOG_ENV_GATE_OK`
- Manifest token: `ENDPOINTS_CATALOG_ENV_GATE_OK`
- Test/stable identifier: `tests/http/test_endpoint_catalog.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-05-po-005`
- Primary governed evidence: `artifacts/proofs/endpoints_env_gate_proof.log`
- Human Index / Machine Mirror artifact keys: `epic038.pr02.a7_env_gate`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/proofs/endpoints_env_gate_proof.log.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 22. `ENV_LC_ALL_C_OK`
- Canonical governance token: `ENV_LC_ALL_C_OK`
- Acceptance-map token: `ENV_LC_ALL_C_OK`
- Manifest token: `ENV_LC_ALL_C_OK`
- Test/stable identifier: `tests/invariance/test_determinism_env_helper.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-03-po-003`
- Primary governed evidence: `artifacts/runtime/env_matrix.snapshot.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr01.env_matrix_snapshot_v3`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/runtime/env_matrix.snapshot.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 23. `EVIDENCE_INDEX_MIRROR_OK`
- Canonical governance token: `EVIDENCE_INDEX_MIRROR_OK`
- Acceptance-map token: `EVIDENCE_INDEX_MIRROR_OK`
- Manifest token: `EVIDENCE_INDEX_MIRROR_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `docs/evidence/INDEX.json`
- Human Index / Machine Mirror artifact keys: `index.human_index`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/evidence/INDEX.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 24. `EVIDENCE_PATHS_VALIDATED_OK`
- Canonical governance token: `EVIDENCE_PATHS_VALIDATED_OK`
- Acceptance-map token: `EVIDENCE_PATHS_VALIDATED_OK`
- Manifest token: `EVIDENCE_PATHS_VALIDATED_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `docs/evidence/INDEX.json`
- Human Index / Machine Mirror artifact keys: `index.human_index`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/evidence/INDEX.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 25. `DB_RUNTIME_SEARCH_PATH_OK`
- Canonical governance token: `DB_RUNTIME_SEARCH_PATH_OK`
- Acceptance-map token: `DB_RUNTIME_SEARCH_PATH_OK`
- Manifest token: `DB_RUNTIME_SEARCH_PATH_OK`
- Test/stable identifier: `tests/ops/test_hde_epic038_ops03.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-22-po-022`
- Primary governed evidence: `audit/ops/hde-epic038/ops-03/db_posture_summary.json`
- Human Index / Machine Mirror artifact keys: `epic038.ops03.db_posture_summary`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/ops/hde-epic038/ops-03/db_posture_summary.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 26. `DB_ROLE_OK`
- Canonical governance token: `DB_ROLE_OK`
- Acceptance-map token: `DB_ROLE_OK`
- Manifest token: `DB_ROLE_OK`
- Test/stable identifier: `tests/ops/test_hde_epic038_ops03.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-22-po-022`
- Primary governed evidence: `audit/ops/hde-epic038/ops-03/db_posture_summary.json`
- Human Index / Machine Mirror artifact keys: `epic038.ops03.db_posture_summary`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/ops/hde-epic038/ops-03/db_posture_summary.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 27. `DB_SCHEMA_FINGERPRINT_OK`
- Canonical governance token: `DB_SCHEMA_FINGERPRINT_OK`
- Acceptance-map token: `DB_SCHEMA_FINGERPRINT_OK`
- Manifest token: `DB_SCHEMA_FINGERPRINT_OK`
- Test/stable identifier: `tests/ops/test_hde_epic038_ops03.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-22-po-022`
- Primary governed evidence: `audit/ops/hde-epic038/ops-03/db_posture_summary.json`
- Human Index / Machine Mirror artifact keys: `epic038.ops03.db_posture_summary`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/ops/hde-epic038/ops-03/db_posture_summary.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 28. `DB_CONN_ENV_OK`
- Canonical governance token: `DB_CONN_ENV_OK`
- Acceptance-map token: `DB_CONN_ENV_OK`
- Manifest token: `DB_CONN_ENV_OK`
- Test/stable identifier: `tests/db/test_direct_db_pr06r.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-12-po-012`
- Primary governed evidence: `artifacts/runtime/direct_db_selection.snapshot.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr06r.direct_db_selection`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/runtime/direct_db_selection.snapshot.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 29. `EVIDENCE_PATH_PROOFS_OK`
- Canonical governance token: `EVIDENCE_PATH_PROOFS_OK`
- Acceptance-map token: `EVIDENCE_PATH_PROOFS_OK`
- Manifest token: `EVIDENCE_PATH_PROOFS_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `docs/evidence/INDEX.json`
- Human Index / Machine Mirror artifact keys: `index.human_index`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `docs/evidence/INDEX.json.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 30. `CI_CHECK_MIRROR_SCHEMA_OK`
- Canonical governance token: `CI_CHECK_MIRROR_SCHEMA_OK`
- Acceptance-map token: `CI_CHECK_MIRROR_SCHEMA_OK`
- Manifest token: `CI_CHECK_MIRROR_SCHEMA_OK`
- Test/stable identifier: `tests/ops/test_evidence_index.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `artifacts/evidence_index.jsonl`
- Human Index / Machine Mirror artifact keys: `index.machine_mirror`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/evidence_index.jsonl.path_proof.txt`
- Current posture: UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 31. `CI_CHECK_FINAL_LF_OK`
- Canonical governance token: `CI_CHECK_FINAL_LF_OK`
- Acceptance-map token: `CI_CHECK_FINAL_LF_OK`
- Manifest token: `CI_CHECK_FINAL_LF_OK`
- Test/stable identifier: `ci/checks/check_final_lf.sh; tests/evidence/test_hde_epic038_closeout.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml): Run ci/checks/check_final_lf.sh`
- Live QA: `qa-19-po-019`
- Primary governed evidence: `audit/qa/hde-epic038/qa_step_logs_manifest.json`
- Human Index / Machine Mirror artifact keys: `epic038.qa_step_logs_manifest`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `audit/qa/hde-epic038/qa_step_logs_manifest.json.path_proof.txt`
- Current posture: UNCLAIMED: the governed QA-19 manifest hash-binds a closed-rails execution log for the repository-wide final-LF gate; historical PASS text and current file presence are not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after the exact-head `Run ci/checks/check_final_lf.sh` workflow step succeeds with the current matrix and proof plus every present approved planned closeout output covered, the QA-19 manifest and hash-bound execution log remain coherent, and independent Gate B records PASS against that same exact head.

## 32. `NO_EXTERNAL_IO_ON_REFUSAL_OK`
- Canonical governance token: `NO_EXTERNAL_IO_ON_REFUSAL_OK`
- Acceptance-map token: `NO_EXTERNAL_IO_ON_REFUSAL_OK`
- Manifest token: `NO_EXTERNAL_IO_ON_REFUSAL_OK`
- Test/stable identifier: `tests/evidence/test_v2_mapped_cache_evidence.py`
- Closed-rails CI binding: `test (.github/workflows/ci.yml)`
- Live QA: `qa-16-po-016`
- Primary governed evidence: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log; artifacts/bodygraph/v2_mapped_cache/manifest.json`
- Human Index / Machine Mirror artifact keys: `epic038.pr05.v2_mapped_cache.closed_rails_refusal; epic038.pr05.v2_mapped_cache.manifest`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log.path_proof.txt; artifacts/bodygraph/v2_mapped_cache/manifest.json.path_proof.txt`
- Current posture: UNCLAIMED: indexed closed-rails evidence records zero vendor and database calls and a bound zero-external-I/O predicate; evidence presence and historical PASS text are not acceptance.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.

## 33. `RELEASE_ID_RECOMPUTE_OK`
- Canonical governance token: `RELEASE_ID_RECOMPUTE_OK`
- Acceptance-map token: `RELEASE_ID_RECOMPUTE_OK`
- Manifest token: `RELEASE_ID_RECOMPUTE_OK`
- Test/stable identifier: `scripts/release_id_recompute.py; tools/evidence/build_release_attestation.py; tests/evidence/test_release_manifest_content_binding.py; tests/evidence/test_release_attestation.py`
- Closed-rails CI binding: `sanity-pipeline (.github/workflows/ci.yml): Build PR-06R-B release attestation outside the source tree; Run canonical JSON gate (closed rails); Publish exact-head release attestation`
- Live QA: `qa-21-po-021`
- Primary governed evidence: `catalog/manifest.json`
- Human Index / Machine Mirror artifact keys: `epic038.release.catalog_manifest`
- Epic: `epic_id=HDE-EPIC038`
- Proof anchors: `catalog/manifest.json.path_proof.txt`
- Current posture: UNCLAIMED: the canonical manifest is the exact current source input; frozen capture-time identity artifacts and historical PASS text are not current release evidence.
- Classification: `existing/reused`
- Owning task: `N/A: existing/reused evidence`
- Intended future claim and prerequisite: Future status may become CLAIMED only when the workflow artifact `hde-release-attestation-${{ github.event.pull_request.head.sha || github.sha }}/attestation.json` verifies `source_commit_exact=true`, `manifest_sha256=0ace495485ca82d6929f26d9d4920215ee7e3ca18b646310d9ef79db1c97a57f`, `release_id=manifest_sha256`, `validation_result=PASS`, `release_admission=PR06R_B_FINAL_PASS`, `pipeline_stop=null`, closed rails, and independent Gate B PASS against that same exact head.
