# HDE-EPIC029 Token ↔ Evidence Matrix

Sequencing posture: **sequencing correction only** (contributory/intermediate only).
Close-pack acceptance binding remains blocked until mapped PF09 row-closing work is complete for `HDE-CONJ009.1`, `HDE-CONJ008.1`, and `HDE-CONJ001.4`.

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| DOC_DELTA_PRESENT_OK | PF04 — HDE Governance §2.0.0 | audit/docdeltas/hde-epic029_doc_deltas.md; audit/docdeltas/hde-epic029_drain_targets.md | Bound by close-pack generator outputs | acceptance_map_viability.log | Planned | Deferred by sequencing gate: contributory/intermediate only; later row-closing work required before close-pack binding. |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Index | docs/evidence/INDEX.json | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Planned | Deferred by sequencing gate: no status change to Done in this slice. |
| MACHINE_MIRROR_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Mirror | artifacts/evidence_index.jsonl | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Planned | Deferred by sequencing gate: no status change to Done in this slice. |
| EVIDENCE_INDEX_HASH_OK | PF12 — Schemas & Artifacts §Evidence Hash Discipline | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Planned | Deferred by sequencing gate: no status change to Done in this slice. |
| ENV_RAILS_POLICY_OK | PF10 — HDE Build Notes §Closed Rails | artifacts/proofs/env_pins.txt | ci/checks/check_env_pins.sh (via sanity pipeline) | acceptance_map_viability.log | Planned | Deferred by sequencing gate until mapped PF09 row closures are complete. |
| JSON_CANONICAL_CHECK_OK | PF10 — HDE Build Notes §Canonical JSON Gate | audit/gates/json_gate/canonical/json_gate_structured_record.json; audit/gates/canonical_json/json_canonical_check.log | tools/evidence/run_canonical_json_gate.py (governed) | acceptance_map_viability.log | Planned | Deferred by sequencing gate until mapped PF09 row closures are complete. |
| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | Existing epic-close live QA output only | acceptance_map_viability.log | Planned | Deferred by sequencing gate: keep token spelling exact but do not promote early in this sequencing-only slice. |
| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | Existing precommit checklist output only | acceptance_map_viability.log | Planned | Deferred by sequencing gate: keep token spelling exact but do not promote early in this sequencing-only slice. |
| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | Existing postcommit checklist output only | acceptance_map_viability.log | Planned | Deferred by sequencing gate: keep token spelling exact but do not promote early in this sequencing-only slice. |

## PF09 scope bindings (status-only; not acceptance tokens)

- `HDE-CONJ009` / `HDE-CONJ009.1`: mixed blocker; not supportable to Done in this slice.
- `HDE-CONJ008` / `HDE-CONJ008.1`: governed approval/evidence blocker; not supportable to Done in this slice.
- `HDE-CONJ001` / `HDE-CONJ001.4`: closed by explicit binding-equivalence normalization in OPS-01.
