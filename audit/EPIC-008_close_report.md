# EPIC-008 Close Report

## Token → Artifact Proof Map

| Token | Artifact(s) |
| --- | --- |
| WRITERS_ERRORS_NOSTORE_NOETAG_OK | artifacts/headers/writer_error_400.json, artifacts/headers/writer_error_415.json, artifacts/headers/compat_writer_200.json |
| WRITERS_NO_304_OK | artifacts/proofs/writers_no_304.txt |
| WRITERS_HEAD_405_OK | artifacts/headers/writer_head_405.txt |
| WRITERS_OPTIONS_204_OK | artifacts/headers/writer_204.txt |
| ERROR_CTYPE_JSON_UTF8_OK | artifacts/headers/writer_error_400.json, artifacts/headers/writer_error_415.json |
| WRITERS_2XX_CTYPE_JSON_UTF8_OK | artifacts/headers/writer_200_diagnostic.json |
| WRITERS_SCHEMA_OK | artifacts/headers/writer_error_413.json, artifacts/headers/writer_error_422_invalid_input.json, artifacts/headers/writer_error_422_unknown_key.json |
| AUTHZ_BOUNDARY_OK | artifacts/headers/writer_error_401.json, artifacts/headers/writer_error_403.json |
| IDEMPOTENT_WRITE_OK | artifacts/idempotence/idempotent_write_status.log |
| PREIMAGE_RECOMPUTE_OK | artifacts/idempotence/preimage_compare.log |
| TWO_RUN_IDENTITY_OK | artifacts/idempotence/two_run_identity.log |
| JSON_CANONICAL_CHECK_OK | artifacts/idempotence/json_canonical_check.log |
| OBS_KEYS_ONLY_OK | artifacts/redaction/grep_guard_report.txt |
| PII_REDACTION_OK | artifacts/redaction/grep_guard_report.txt |
| SECRETS_READY_OK | dev/.env.codex |
| ENV_RAILS_POLICY_OK | dev/.env.codex |
| NO_PAYLOAD_ECHO_OK | artifacts/redaction/grep_guard_report.txt, artifacts/headers/writer_error_400.json |
| EVIDENCE_INDEX_UPDATED_OK | docs/evidence/INDEX.json |
| EVIDENCE_INDEX_MIRROR_OK | artifacts/evidence_index.jsonl |
| EVIDENCE_PATHS_VALIDATED_OK | artifacts/evidence_index.jsonl |
| EVIDENCE_INDEX_HASH_OK | artifacts/proofs/evidence_index_sha256.txt |
| RELEASE_ID_RECORDED_OK | artifacts/evidence_index.jsonl |

## Evidence Index Summary

- Human index: docs/evidence/INDEX.json (canonical JSON, LF-terminated).
- Machine mirror: artifacts/evidence_index.jsonl (PF12 keys, sorted by discovered_physical_path).
- Hash sentinel: artifacts/proofs/evidence_index_sha256.txt (sha256 of docs/evidence/INDEX.json).

## Migration Delivered

- migrations/008_writers_auth.sql

