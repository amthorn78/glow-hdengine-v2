# EPIC-008 QA Report

- **Epic:** HDE-EPIC008
- **Commit:** 858b9164 (858b91642a9b3b51cd9be28805e40aadd7d14293)
- **Release ID:** 6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925
- **Invocation Tag:** INV-f2ac55d77ce9aacc
- **Run Timestamp:** 2025-11-05T10:11:49Z

Validated the diagnostic and compat writers across transport, auth, schema guards, idempotence, and logging while confirming the evidence indices and release metadata.

## Acceptance Token Matrix

| Token | Status | Proof Artifacts |
| --- | --- | --- |
| WRITERS_ERRORS_NOSTORE_NOETAG_OK | PASS | artifacts/headers/writer_error_400.json<br>artifacts/headers/writer_error_415.json<br>artifacts/headers/compat_writer_200.json |
| WRITERS_NO_304_OK | PASS | artifacts/proofs/writers_no_304.txt |
| WRITERS_HEAD_405_OK | PASS | artifacts/headers/writer_head_405.txt |
| WRITERS_OPTIONS_204_OK | PASS | artifacts/headers/writer_204.txt |
| ERROR_CTYPE_JSON_UTF8_OK | PASS | artifacts/headers/writer_error_400.json<br>artifacts/headers/writer_error_415.json |
| WRITERS_2XX_CTYPE_JSON_UTF8_OK | PASS | artifacts/headers/writer_200_diagnostic.json |
| WRITERS_SCHEMA_OK | PASS | artifacts/headers/writer_error_413.json<br>artifacts/headers/writer_error_422_invalid_input.json<br>artifacts/headers/writer_error_422_unknown_key.json |
| AUTHZ_BOUNDARY_OK | PASS | artifacts/headers/writer_error_401.json<br>artifacts/headers/writer_error_403.json |
| IDEMPOTENT_WRITE_OK | PASS | artifacts/idempotence/idempotent_write_status.log |
| PREIMAGE_RECOMPUTE_OK | PASS | artifacts/idempotence/preimage_compare.log |
| TWO_RUN_IDENTITY_OK | PASS | artifacts/idempotence/two_run_identity.log |
| JSON_CANONICAL_CHECK_OK | PASS | artifacts/idempotence/json_canonical_check.log |
| OBS_KEYS_ONLY_OK | PASS | artifacts/redaction/grep_guard_report.txt |
| PII_REDACTION_OK | PASS | artifacts/redaction/grep_guard_report.txt |
| SECRETS_READY_OK | PASS | dev/.env.codex |
| ENV_RAILS_POLICY_OK | PASS | dev/.env.codex |
| NO_PAYLOAD_ECHO_OK | PASS | artifacts/redaction/grep_guard_report.txt<br>artifacts/headers/writer_error_400.json |
| EVIDENCE_INDEX_UPDATED_OK | PASS | docs/evidence/INDEX.json |
| EVIDENCE_INDEX_MIRROR_OK | PASS | artifacts/evidence_index.jsonl |
| EVIDENCE_PATHS_VALIDATED_OK | PASS | artifacts/evidence_index.jsonl |
| EVIDENCE_INDEX_HASH_OK | PASS | artifacts/proofs/evidence_index_sha256.txt |
| RELEASE_ID_RECORDED_OK | PASS | artifacts/evidence_index.jsonl |

## Residual Risks

- Pending operational application of migrations/008_writers_auth.sql by deployment tooling.

## Test Evidence

- pytest tests/adapter/test_diagnostic_writer.py
- pytest tests/adapter/test_compat_writer_transport.py
- pytest tests/compliance/test_log_shape_snapshot.py
- pytest tests/compliance/test_logging_filter_keys_only_and_redactions.py

## Evidence Footnote

- Artifacts referenced: 21
- Machine index lines: 20
- Human index sha256: d800aae876074d6208fed7e19014f155b0569027e801505e4a87ce3096a20b35
