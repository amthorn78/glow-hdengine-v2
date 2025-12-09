# EPIC021 Doc-delta readiness (PF09, PF20, PF04, PF19)

This note is for doc owners preparing PF-Canon updates after EPIC021 close. It is scoped to repository evidence and does not adjust PF-Canon text.

## PF09 — HDE-Build Checklist

- **HDE-CALC002 (evidence indexing) / HDE-CALC003 (sanity + env pins)**
  - Status to set: **Done — Epic: HDE-EPIC021**.
  - Evidence pointers: Evidence Index + Mirror (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`), registry_report path proof, sanity pipeline log + path proof.
  - QA_ROOT anchors: `audit/qa/hde-epic021/qa_step_logs_manifest.json`, per-run `step_evidence_d2.log` and `step_sanity_d2.log`.
- **HDE-CALC004 (QA discipline + acceptance bindings)**
  - Status to set: **Done — Epic: HDE-EPIC021**.
  - Evidence pointers: QA bootstrap log (`audit/qa/hde-epic021/test_tooling_bootstrap.log`), QA step manifest, acceptance-map viability log, and doc-delta readiness note (this file).

## PF20 — HDE-Phased Epics (EPIC021 record)

- **D1 — Canonical serializer/parity/guards**
  - Tokens: `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`, `JSON_CANONICAL_CHECK_OK`, `ERROR_JSON_CANON_OK`, `CLI_SERIALIZER_GUARD_OK`.
  - Evidence: CLI + Reader parity suites (`tests/cli/test_showcompat_parity_and_identity.py`, `tests/cli/test_bg_resolve.py`, `tests/cli/test_cli_canonical_bytes.py`, `tests/cli/test_aux_preview.py`), guard logs (`artifacts/cli/guards/*.log|*.txt`), QA serializer step logs in QA_ROOT.
- **D2 — Evidence catalog + sanity pipeline wiring**
  - Tokens: `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `DETERMINISM_ENV_PINS_OK`, `SANITY_PIPELINE_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`.
  - Evidence: Registry report and sanity artifacts plus path proofs under `artifacts/registry/` and `artifacts/sanity/`, Evidence Index + Mirror, env-pin enforcement tests, QA evidence and sanity step logs.
- **D3 — QA harness + viability**
  - Tokens: `SANITY_PIPELINE_LOGGED_OK`, `QA_STEP_LOGS_CONSOLIDATED_OK`, doc-delta placeholders `PF04-DD-QA-BOOTSTRAP-TOKENS`, `PF19-DD-QA-PLAN-VIABILITY-TOKENS`.
  - Evidence: QA bootstrap canonical log, per-run bootstrap/sanity/acceptance-map step logs, QA step manifest, acceptance-map viability log, doc-delta readiness note.

## PF04 — Governance Docs (QA bootstrap tokens)

- Placeholder token: `PF04-DD-QA-BOOTSTRAP-TOKENS` (token naming to be finalized in PF04).
- Evidence available now: QA bootstrap canonical log, QA step logs manifest, per-run `D0_bootstrap.log` entries.
- Doc-delta action: update PF04 QA bootstrap token roster to adopt the EPIC021 behavior without changing repo token names here.

## PF19 — Glow QA Guide (plan viability tokens)

- Placeholder token: `PF19-DD-QA-PLAN-VIABILITY-TOKENS` (token naming to be finalized in PF19).
- Evidence available now: Acceptance-map viability log, QA step logs manifest, per-run `step_acceptance_map_d3.log` entries.
- Doc-delta action: refresh PF19 plan viability/token naming to absorb EPIC021 QA_ROOT viability evidence while keeping repository tokens unchanged.
