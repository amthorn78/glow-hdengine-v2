# HDE-EPIC029 Token ↔ Evidence Matrix

Sequencing posture: **supportable from repo evidence**.
Close-pack acceptance binding is supportable for the controlled PF09 rows in this bounded EPIC029 closeout.

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| DOC_DELTA_PRESENT_OK | PF04 — HDE Governance §2.0.0 | audit/docdeltas/hde-epic029_doc_deltas.md; audit/docdeltas/hde-epic029_drain_targets.md | python tools/qa/generate_epic029_close_pack.py | acceptance_map_viability.log | Implemented | Doc-delta and drain-target ledgers are generated and bound for close-pack readiness. |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Index | docs/evidence/INDEX.json | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when INDEX.json and INDEX.json.path_proof.txt are present. |
| MACHINE_MIRROR_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Mirror | artifacts/evidence_index.jsonl | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when evidence_index.jsonl and evidence_index.jsonl.path_proof.txt are present. |
| EVIDENCE_INDEX_HASH_OK | PF12 — Schemas & Artifacts §Evidence Hash Discipline | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when sha256 sidecars and path proofs exist and hashes match current bytes. |
| ENV_RAILS_POLICY_OK | PF10 — HDE Build Notes §Closed Rails | artifacts/proofs/env_pins.txt | ci/checks/check_env_pins.sh | acceptance_map_viability.log | Implemented | Determinism env pins evidence remains present for closed-rails posture. |
| JSON_CANONICAL_CHECK_OK | PF10 — HDE Build Notes §Canonical JSON Gate | audit/gates/json_gate/canonical/json_gate_structured_record.json; audit/gates/canonical_json/json_canonical_check.log | python tools/evidence/run_canonical_json_gate.py --check-only | acceptance_map_viability.log | Implemented | Canonical JSON gate evidence is bound without introducing new token names. |
| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | python -m pytest -q -p no:cacheprovider tests/adapter/test_dev_sampler_http.py tests/http/test_dev_conjunction_http.py tests/http/test_endpoint_catalog.py | acceptance_map_viability.log | Implemented | Bound to a fresh complete-family requalification result. |
| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | ci/checks/check_env_pins.sh; ci/checks/check_cli_help.sh; ci/checks/check_final_lf.sh | acceptance_map_viability.log | Implemented | Bound to a fresh ordered non-shell requalification result. |
| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | python tools/evidence/run_sanity_pipeline.py | acceptance_map_viability.log | Implemented | Bound to a fresh release-sanity result and verified fixed point. |

## PF09 scope bindings (status-only; not acceptance tokens)

- Supportable from repo evidence: `HDE-CONJ009.1` -> Done.
- Supportable from repo evidence: `HDE-CONJ009` -> Done.
- Supportable from repo evidence: `HDE-CONJ008.1` -> Done.
- Supportable from repo evidence: `HDE-CONJ008` -> Done.
- Supportable from repo evidence: `HDE-CONJ001.4` -> Done after OPS-01 normalization.
- `HDE-CONJ001` remains task-level done in PF09; this report only states subtask supportability from repo evidence.
