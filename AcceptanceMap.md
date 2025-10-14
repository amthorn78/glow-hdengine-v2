# EPIC-2 Acceptance Map (Mechanics & Stability)

| token | evidence | status |
|---|---|---|
| ENUMS_CANON_OK | artifacts/canon/CANON_CHECKSUMS.json | PASS |
| CHECKSUMS_V2_FIELDS_OK | artifacts/canon/CANON_CHECKSUMS.json | PASS |
| CHECKSUMS_TWO_RUN_IDENTITY_OK | artifacts/canon/CANON_CHECKSUMS.json.sha256, artifacts/canon/manifest.json.sha256 | PASS |
| READER_200_ETAG_OK | artifacts/headers/headers_200_identity.json | PASS |
| VARY_HEADER_OK | artifacts/headers/headers_200_identity.json | PASS |
| CONTENT_ENCODING_IDENTITY_NONE_OK | artifacts/headers/headers_200_identity.json | PASS |
| READER_HEAD_CL_MATCH_OK | artifacts/headers/headers_HEAD.json, artifacts/headers/body_identity.json | PASS |
| READER_304_BODYLESS_OK | artifacts/headers/headers_304.json, artifacts/headers/return_304.code | PASS |
| READER_304_NO_CL_CTYPE_OK | artifacts/headers/headers_304.json | PASS |
| ERROR_NO_ETAG_NOSTORE_OK | artifacts/errors/headers_400.json, artifacts/errors/headers_403.json | PASS |
| ERROR_SNAKE_CASE_OK | artifacts/errors/body_400.json | PASS |
| TWO_RUN_IDENTITY_OK | artifacts/serializer/determinism_report.txt | PASS |
| TRAILING_LF_OK | artifacts/serializer/determinism_report.txt | PASS |
| EMIT_PATH_NO_JSON_DUMPS_GUARD_INSTALLED_OK | tools/lint_emit_paths.py, scripts/run_sanity.sh | PASS |
| EMIT_PATH_NO_JSON_DUMPS_OK | (run `bash scripts/run_sanity.sh`) | FAIL (5 offenders recorded) |
| CONTENT_ENCODING_GZIP_OK | (dev server doesn’t compress) | N/A |
| CLI_READER_PARITY_OK | (no CLI in this repo) | N/A |
| ERROR_429_RETRY_AFTER_INT_OK | (no 429 path in harness) | GAP |
| ERROR_429_MS_MATCH_OK | (no 429 path in harness) | GAP |
