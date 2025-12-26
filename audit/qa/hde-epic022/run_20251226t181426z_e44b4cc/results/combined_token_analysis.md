# Combined EPIC022 QA Analysis Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-26

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_roster_pf20.txt

```
TESTS_PASS_OK
DOC_DELTA_PRESENT_OK
EVIDENCE_INDEX_UPDATED_OK
EVIDENCE_INDEX_HASH_OK
EVIDENCE_INDEX_MIRROR_OK
EVIDENCE_PATHS_VALIDATED_OK
MACHINE_MIRROR_UPDATED_OK
QA_PRECOMMIT_CHECKLIST_OK
QA_POSTCOMMIT_CHECKLIST_OK
ENV_RAILS_POLICY_OK
DETERMINISM_ENV_PINS_OK
SANITY_PIPELINE_OK
CLOSE_PACK_FILES_PRESENT_OK
ERROR_JSON_CANON_OK
ERROR_TOKEN_MAP_OK
CLI_READER_PARITY_OK
TWO_RUN_IDENTITY_OK
CLI_STDOUT_LF_OK
INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK
INTERNAL_VERSION_HEAD_PARITY_OK
INTERNAL_VERSION_CONDITIONALS_IGNORED_OK
INTERNAL_VERSION_NO_ETAG_OK
INTERNAL_VERSION_NO_STORE_OK
RELEASE_ID_RECOMPUTE_OK
RELEASE_ID_FROM_MANIFEST_OK
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_registry_validation.json

```json
{
  "captured_at_utc": "2025-12-26T19:52:27Z",
  "pf04_validation_model": "EPIC022 plan-time PF04 presence check; absent tokens treated as UNREGISTERED_ACCEPTANCE_TOKEN per PF10 §2.7",
  "results": [
    {
      "pf04_registered": true,
      "token": "TESTS_PASS_OK"
    },
    {
      "pf04_registered": true,
      "token": "DOC_DELTA_PRESENT_OK"
    },
    {
      "pf04_registered": true,
      "token": "EVIDENCE_INDEX_UPDATED_OK"
    },
    {
      "pf04_registered": true,
      "token": "EVIDENCE_INDEX_HASH_OK"
    },
    {
      "pf04_registered": true,
      "token": "EVIDENCE_INDEX_MIRROR_OK"
    },
    {
      "pf04_registered": true,
      "token": "EVIDENCE_PATHS_VALIDATED_OK"
    },
    {
      "pf04_registered": true,
      "token": "MACHINE_MIRROR_UPDATED_OK"
    },
    {
      "pf04_registered": false,
      "token": "QA_PRECOMMIT_CHECKLIST_OK"
    },
    {
      "pf04_registered": false,
      "token": "QA_POSTCOMMIT_CHECKLIST_OK"
    },
    {
      "pf04_registered": true,
      "token": "ENV_RAILS_POLICY_OK"
    },
    {
      "pf04_registered": true,
      "token": "DETERMINISM_ENV_PINS_OK"
    },
    {
      "pf04_registered": true,
      "token": "SANITY_PIPELINE_OK"
    },
    {
      "pf04_registered": false,
      "token": "CLOSE_PACK_FILES_PRESENT_OK"
    },
    {
      "pf04_registered": false,
      "token": "ERROR_JSON_CANON_OK"
    },
    {
      "pf04_registered": false,
      "token": "ERROR_TOKEN_MAP_OK"
    },
    {
      "pf04_registered": true,
      "token": "CLI_READER_PARITY_OK"
    },
    {
      "pf04_registered": true,
      "token": "TWO_RUN_IDENTITY_OK"
    },
    {
      "pf04_registered": true,
      "token": "CLI_STDOUT_LF_OK"
    },
    {
      "pf04_registered": true,
      "token": "INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK"
    },
    {
      "pf04_registered": true,
      "token": "INTERNAL_VERSION_HEAD_PARITY_OK"
    },
    {
      "pf04_registered": true,
      "token": "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK"
    },
    {
      "pf04_registered": true,
      "token": "INTERNAL_VERSION_NO_ETAG_OK"
    },
    {
      "pf04_registered": true,
      "token": "INTERNAL_VERSION_NO_STORE_OK"
    },
    {
      "pf04_registered": true,
      "token": "RELEASE_ID_RECOMPUTE_OK"
    },
    {
      "pf04_registered": true,
      "token": "RELEASE_ID_FROM_MANIFEST_OK"
    }
  ],
  "source_roster": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_roster_pf20.txt",
  "unregistered_tokens": [
    "QA_PRECOMMIT_CHECKLIST_OK",
    "QA_POSTCOMMIT_CHECKLIST_OK",
    "CLOSE_PACK_FILES_PRESENT_OK",
    "ERROR_JSON_CANON_OK",
    "ERROR_TOKEN_MAP_OK"
  ]
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_registry_validation.summary.md

# Token roster validation (PF20 roster vs PF04 registry posture)

captured_at_utc: 2025-12-26T19:52:27Z

## UNREGISTERED_ACCEPTANCE_TOKEN (blocking canon gap; do not claim in step logs)

- QA_PRECOMMIT_CHECKLIST_OK
- QA_POSTCOMMIT_CHECKLIST_OK
- CLOSE_PACK_FILES_PRESENT_OK
- ERROR_JSON_CANON_OK
- ERROR_TOKEN_MAP_OK

## Registered (claimable if evidence satisfied)

- TESTS_PASS_OK
- DOC_DELTA_PRESENT_OK
- EVIDENCE_INDEX_UPDATED_OK
- EVIDENCE_INDEX_HASH_OK
- EVIDENCE_INDEX_MIRROR_OK
- EVIDENCE_PATHS_VALIDATED_OK
- MACHINE_MIRROR_UPDATED_OK
- ENV_RAILS_POLICY_OK
- DETERMINISM_ENV_PINS_OK
- SANITY_PIPELINE_OK
- CLI_READER_PARITY_OK
- TWO_RUN_IDENTITY_OK
- CLI_STDOUT_LF_OK
- INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK
- INTERNAL_VERSION_HEAD_PARITY_OK
- INTERNAL_VERSION_CONDITIONALS_IGNORED_OK
- INTERNAL_VERSION_NO_ETAG_OK
- INTERNAL_VERSION_NO_STORE_OK
- RELEASE_ID_RECOMPUTE_OK
- RELEASE_ID_FROM_MANIFEST_OK

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0D_token_roster_validate_pf04.log

```log
check_id: 0D
status: TOOLING_BLOCKED
started_at_utc: 2025-12-26T19:52:27Z
ended_at_utc: 2025-12-26T19:52:27Z
rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
pf_refs: PF04 — HDE-Governance, §2.0; PF10 — HDE-Build Notes, §2.7
tokens:
command: python 'audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/tools/token_roster_validate_pf04.py' --roster 'audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_roster_pf20.txt' --out-json 'audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_registry_validation.json' --out-summary-md 'audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/token_registry_validation.summary.md'
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
exit_code: 2
--- stdout ---

--- stderr ---

```

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
[
  {
    "check_id": "0A",
    "ended_at_utc": "2025-12-26T18:16:15Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0A_bootstrap_and_codespaces_snapshot.log",
    "pf_refs": "PF19 — Glow QA Guide, §14.4.3; PF27 — Plan Templates, §4.2",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:16:15Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "0710287ebdc583a08974ea6b7205269a34d81b0c4edfb69fdf3d471cda1d4b98",
    "tokens": []
  },
  {
    "check_id": "0B",
    "ended_at_utc": "2025-12-26T18:41:55Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0B_doc_delta_capture.log",
    "pf_refs": "PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.7",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:41:55Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": [
      "DOC_DELTA_PRESENT_OK"
    ]
  },
  {
    "check_id": "0C",
    "ended_at_utc": "2025-12-26T19:11:10Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0C_prod_handshake.log",
    "pf_refs": "PF19 — Glow QA Guide, §2.3",
    "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T19:11:10Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": []
  },
  {
    "check_id": "0D",
    "ended_at_utc": "2025-12-26T19:44:11Z",
    "exit_code": 2,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0D_token_roster_validate_pf04.log",
    "pf_refs": "PF04 — HDE-Governance, §2.0; PF10 — HDE-Build Notes, §2.7",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T19:44:11Z",
    "status": "TOOLING_BLOCKED",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": []
  },
  {
    "check_id": "0D",
    "ended_at_utc": "2025-12-26T19:52:27Z",
    "exit_code": 2,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0D_token_roster_validate_pf04.log",
    "pf_refs": "PF04 — HDE-Governance, §2.0; PF10 — HDE-Build Notes, §2.7",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T19:52:27Z",
    "status": "TOOLING_BLOCKED",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": []
  }
]
```

---

## File: audit/qa/hde-epic022/step0d_deviations.md

**Status**: File not found (does not exist in repository)
