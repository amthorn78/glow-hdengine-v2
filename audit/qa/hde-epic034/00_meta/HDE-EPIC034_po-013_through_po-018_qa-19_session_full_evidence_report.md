# HDE-EPIC034 PO-013 Through PO-018 and QA-19 Session Full Evidence Report

Session date: 2026-06-26
Epic: HDE-EPIC034 / Fermentation Pass 5
Step cluster: po-013, po-014, po-015, po-016, po-017, po-018, qa-19-close-out-deliverables

## Session Summary

The QA-created harness at `audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py` was refreshed to support the selected approved checks `po-013` through `po-018` and `qa-19-close-out-deliverables`.

The harness was adjusted so read-only subprocesses used by `po-017` run under closed rails and do not inherit local vendor/base URL secrets from the shell environment. This preserved the intended `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC` posture for targeted tests and evidence gates.

Dev test dependencies were confirmed with `python -m pip install -r requirements-dev.txt`, followed by `python -m pytest --version`, which reported `pytest 8.4.2`.

The selected checks were run under closed rails. `po-013` through `po-018` passed, and `qa-19-close-out-deliverables` passed. `po-017` initially exposed a stale governed path proof for `audit/ops/hde-epic034/ops-02/files_sha256.txt`; the canonical evidence updater was used to refresh the governed index/mirror/path-proof family, then canonical checks were rerun successfully.

Final verification included:

* `python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py`: 333 passed.
* `python tools/evidence/validate_evidence_paths.py`: exit 0.
* `python tools/evidence/check_lf_endings.py`: exit 0.
* `python tools/evidence/update_evidence_index.py --check`: exit 0.
* `python tools/evidence/orientation_demo.py --check`: exit 0.
* `python ci/checks/check_mirror_schema.sh`: exit 0.
* `bash ci/checks/check_evidence_index_hash.sh`: exit 0.
* `bash ci/checks/check_final_lf.sh`: exit 0.

## Produced Evidence Files Included Verbatim

This report includes the full contents of the selected-step evidence files produced in this session:

* `audit/qa/hde-epic034/checks/po-013/primary.log`
* `audit/qa/hde-epic034/checks/po-013/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/po-014/primary.log`
* `audit/qa/hde-epic034/checks/po-014/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/po-015/primary.log`
* `audit/qa/hde-epic034/checks/po-015/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/po-016/primary.log`
* `audit/qa/hde-epic034/checks/po-016/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/po-017/primary.log`
* `audit/qa/hde-epic034/checks/po-017/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/po-018/primary.log`
* `audit/qa/hde-epic034/checks/po-018/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log`
* `audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.path_proof.txt`
* `audit/qa/hde-epic034/qa_step_logs_manifest.json`
* `audit/qa/hde-epic034/qa_step_logs_manifest.json.path_proof.txt`
* `audit/qa/hde-epic034/00_meta/discovery_artifact.md`
* `audit/qa/hde-epic034/00_meta/discovery_artifact.md.path_proof.txt`
* `audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md`
* `audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`

## Evidence Contents

### audit/qa/hde-epic034/checks/po-013/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:48:06Z", "check_id": "po-013", "check_name": "PO-013", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-013", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-013/primary.log", "audit/qa/hde-epic034/checks/po-013/primary.log.path_proof.txt", "audit/ops/hde-epic034/ops-02/env_presence_redacted.json", "audit/ops/hde-epic034/ops-02/request_summary.json", "audit/ops/hde-epic034/ops-02/result_summary.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-013
check_name=PO-013
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-013
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json sha256=566d06758ad3dc34d57427e6228e4808263fa7107b8abd28123df95397cd2fc5
FILE_OK audit/ops/hde-epic034/ops-02/request_summary.json sha256=40a29a73564be3945386134a231905c4daf99a77c5bde362aa4316eed8abb241
FILE_OK audit/ops/hde-epic034/ops-02/result_summary.json sha256=a8e41e93d4f9b2f1330b8bd13e692b65398033695b5fe0fc41bca413070a45ac
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: HD_API_KEY='SET'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: GEO_API_KEY='SET'
JSON_OK audit/ops/hde-epic034/ops-02/env_presence_redacted.json :: HD_API_BASE_URL='SET'
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: raw_secret_persisted=False
JSON_OK audit/ops/hde-epic034/ops-02/result_summary.json :: full_vendor_payload_persisted=False
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: auth_header_posture='Authorization: Bearer <redacted>'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: input_tuple_posture='synthetic non-PII coordinates tuple; full request body not persisted'
JSON_OK audit/ops/hde-epic034/ops-02/request_summary.json :: request_url_posture='redacted base URL; version-neutral resource path joined by HdApiClient'
```

### audit/qa/hde-epic034/checks/po-013/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-013/primary.log
size_bytes: 2351
sha256: 0ee71812dd44ad035ba19d29b98901190878e2121c1f701522c78e32c5bea60f
mtime_utc: 2026-06-26T14:48:06Z
produced_at_utc: 2026-06-26T14:48:06Z
```

### audit/qa/hde-epic034/checks/po-014/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:48:06Z", "check_id": "po-014", "check_name": "PO-014", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-014", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-014/primary.log", "audit/qa/hde-epic034/checks/po-014/primary.log.path_proof.txt", "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-014
check_name=PO-014
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-014
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log sha256=4911de3748f85d25adb3c2ca2c930f619c966f0a0fb516a34b37808460f0271f
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: ops02_classification=PASS
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: validation_rails=closed rails for PR-06 binding; OPS-02 open-rails smoke not rerun
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: final_classification=PASS_PR06_EVIDENCE_BINDING_ONLY
```

### audit/qa/hde-epic034/checks/po-014/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-014/primary.log
size_bytes: 1497
sha256: 6b6d6400b97e445662037f18ec32b8e12ec301ae10c9b28041b52a8014aefe92
mtime_utc: 2026-06-26T14:48:06Z
produced_at_utc: 2026-06-26T14:48:06Z
```

### audit/qa/hde-epic034/checks/po-015/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:48:06Z", "check_id": "po-015", "check_name": "PO-015", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-015", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-015/primary.log", "audit/qa/hde-epic034/checks/po-015/primary.log.path_proof.txt", "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-015
check_name=PO-015
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-015
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log sha256=4911de3748f85d25adb3c2ca2c930f619c966f0a0fb516a34b37808460f0271f
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_hde_ferm008_3_error_retry_rate_limit_mapping=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_hde_ferm008_4_normalized_live_data_path_proof=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_hde_ferm008_5_full_live_conformance_evidence_loop=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_full_humandesignapi_v2_runtime_conformance=true
```

### audit/qa/hde-epic034/checks/po-015/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-015/primary.log
size_bytes: 1644
sha256: 389367e1b9e26ddc2177eed89578243f1c301502a96066ee2f96fe59e0eafa03
mtime_utc: 2026-06-26T14:48:06Z
produced_at_utc: 2026-06-26T14:48:06Z
```

### audit/qa/hde-epic034/checks/po-016/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:48:06Z", "check_id": "po-016", "check_name": "PO-016", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-016", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-016/primary.log", "audit/qa/hde-epic034/checks/po-016/primary.log.path_proof.txt", "audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-016
check_name=PO-016
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-016
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log sha256=4911de3748f85d25adb3c2ca2c930f619c966f0a0fb516a34b37808460f0271f
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_public_reader_change=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_public_route=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_public_flag=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_public_payload_change=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_new_http_home=true
TEXT_OK audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log :: nonclaim_ai_scope=true
```

### audit/qa/hde-epic034/checks/po-016/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-016/primary.log
size_bytes: 1717
sha256: dac45c3ff51474a10e5816a23118d81acfcff910c79e54df5f68596a1da80a4f
mtime_utc: 2026-06-26T14:48:06Z
produced_at_utc: 2026-06-26T14:48:06Z
```

### audit/qa/hde-epic034/checks/po-017/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:50:49Z", "check_id": "po-017", "check_name": "PO-017", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-017", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-017/primary.log", "audit/qa/hde-epic034/checks/po-017/primary.log.path_proof.txt", "tests/bodygraph/test_vendor_client.py", "tests/evidence/test_hdapi_v2_contract_inventory.py", "tools/evidence/validate_evidence_paths.py", "tools/evidence/check_lf_endings.py", "tools/evidence/update_evidence_index.py", "ci/checks/check_mirror_schema.sh", "ci/checks/check_evidence_index_hash.sh", "ci/checks/check_final_lf.sh", "docs/evidence/INDEX.json", "docs/evidence/INDEX.sha256", "artifacts/evidence_index.jsonl", "artifacts/evidence_index.jsonl.sha256", "docs/acceptance_map_epic034.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": ["EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_INDEX_HASH_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK"], "claimed_tokens": ["EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_INDEX_HASH_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "TESTS_PASS_OK"]}
check_id=po-017
check_name=PO-017
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-017
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
PYTEST_IMPORT_OK
FILE_OK tests/bodygraph/test_vendor_client.py sha256=beddc94ef57ba51685285245ff477637cf9c504f13c883f41d4f20282c73d8d9
FILE_OK tests/evidence/test_hdapi_v2_contract_inventory.py sha256=f9152695e7d4fa53e040808781c89087237f2d36b634c43e710fb21869cd8716
FILE_OK tools/evidence/validate_evidence_paths.py sha256=bce88fdacf4b5af09f94829aa6fcc806256b2576e8d7ec443ba07cc4c8d29102
FILE_OK tools/evidence/check_lf_endings.py sha256=046a43fb5dfa4cb7ebec3195a7a57633f07d8423337c90c9e3cb5130ff11297e
FILE_OK tools/evidence/update_evidence_index.py sha256=1f3625577b203ee3db8d5e6c346502971e0b5eb351cdb387241a3fc455005a6a
FILE_OK ci/checks/check_mirror_schema.sh sha256=867d00961e78955df15c50a499836d1150093d41bd5ff8df585011c27295e09f
FILE_OK ci/checks/check_evidence_index_hash.sh sha256=f5cd0cc92fb4175d6cb692a94011afd1c21ceda29caedaf36530b77cfec04d75
FILE_OK ci/checks/check_final_lf.sh sha256=eaa6feaf740bf06fdd33f7fe87519477325f2d785adc1d818bd93d47c00ec80c
FILE_OK docs/evidence/INDEX.json sha256=54fdf8f25ec6e3de3d545f4cb37b05b8d38cc8bdc940d36a593f2fca48ff2dbe
FILE_OK docs/evidence/INDEX.sha256 sha256=fc1b05cc760210c7e7db836cab6d4be1ed23dd0efed0e796b14316b43b9897a8
FILE_OK artifacts/evidence_index.jsonl sha256=993805e1bc8f1de5ce2209dbeebc6b518984a005a92381596f5b71b69f50cd92
FILE_OK artifacts/evidence_index.jsonl.sha256 sha256=a6dde2e0c56d1766e74a138bde057432145412ac2c09218299e9c7b3b6fb2b48
FILE_OK docs/acceptance_map_epic034.json sha256=e34966e96a40b4132c2d1c4dbbc21cc9713ee59b04b2e35944ab7e270e9627ec
COMMAND /usr/local/bin/python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_hdapi_v2_contract_inventory.py
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.4.2, pluggy-1.6.0
rootdir: /workspaces/glow-hdengine-v2
configfile: pytest.ini
plugins: cov-4.1.0, mock-3.15.1
collected 333 items

tests/bodygraph/test_vendor_client.py .................................. [ 10%]
.                                                                        [ 10%]
tests/evidence/test_hdapi_v2_contract_inventory.py ..................... [ 16%]
........................................................................ [ 38%]
........................................................................ [ 60%]
........................................................................ [ 81%]
.............................................................            [100%]

============================= 333 passed in 57.48s =============================
EXIT_CODE 0
COMMAND /usr/local/bin/python tools/evidence/validate_evidence_paths.py
EXIT_CODE 0
COMMAND /usr/local/bin/python tools/evidence/check_lf_endings.py
EXIT_CODE 0
COMMAND /usr/local/bin/python tools/evidence/update_evidence_index.py --check
[evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC
EXIT_CODE 0
COMMAND /usr/local/bin/python ci/checks/check_mirror_schema.sh
EXIT_CODE 0
COMMAND bash ci/checks/check_evidence_index_hash.sh
EXIT_CODE 0
COMMAND bash ci/checks/check_final_lf.sh
EXIT_CODE 0
TEXT_OK docs/acceptance_map_epic034.json :: "EVIDENCE_INDEX_UPDATED_OK"
TEXT_OK docs/acceptance_map_epic034.json :: "MACHINE_MIRROR_UPDATED_OK"
TEXT_OK docs/acceptance_map_epic034.json :: "TESTS_PASS_OK"
```

### audit/qa/hde-epic034/checks/po-017/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-017/primary.log
size_bytes: 5023
sha256: 74291f5ba761166c7004831d3c28c1b280068944a88c0ac6cd91fab5143d6788
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```

### audit/qa/hde-epic034/checks/po-018/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:50:49Z", "check_id": "po-018", "check_name": "PO-018", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-018", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/po-018/primary.log", "audit/qa/hde-epic034/checks/po-018/primary.log.path_proof.txt", "docs/acceptance_map_epic034.json"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=po-018
check_name=PO-018
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py po-018
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
FILE_OK docs/acceptance_map_epic034.json sha256=e34966e96a40b4132c2d1c4dbbc21cc9713ee59b04b2e35944ab7e270e9627ec
TEXT_OK docs/acceptance_map_epic034.json :: "acceptance_claims_mode":"baseline_existing_tokens_only"
TEXT_OK docs/acceptance_map_epic034.json :: No vendor-v2-specific acceptance token is minted or claimed.
NO_VENDOR_SPECIFIC_ACCEPTANCE_MARKER_OK
```

### audit/qa/hde-epic034/checks/po-018/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/po-018/primary.log
size_bytes: 1324
sha256: bb05e79dddf065cd2b48c4688b63cbc22e626b7d2e4cbe113ca9eca4f6478c54
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```

### audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log

```text
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-06-26T14:50:49Z", "check_id": "qa-19-close-out-deliverables", "check_name": "Close-out deliverables", "status": "PASS", "fail_status": "", "command": "python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py qa-19-close-out-deliverables", "command_provenance": "Copy/paste from PO instructions via QA-created harness", "exit_code": 0, "evidence_artifacts": ["audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log", "audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.path_proof.txt", "audit/qa/hde-epic034/qa_step_logs_manifest.json", "audit/qa/hde-epic034/qa_step_logs_manifest.json.path_proof.txt", "audit/qa/hde-epic034/00_meta/discovery_artifact.md", "audit/qa/hde-epic034/00_meta/discovery_artifact.md.path_proof.txt", "audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md", "audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF19 - Glow QA Guide", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
check_id=qa-19-close-out-deliverables
check_name=Close-out deliverables
command=python audit/qa/hde-epic034/00_meta/hde034_live_qa_harness.py qa-19-close-out-deliverables
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
pins=LC_ALL=C LANG=C TZ=UTC
manifest=audit/qa/hde-epic034/qa_step_logs_manifest.json
discovery_artifact=audit/qa/hde-epic034/00_meta/discovery_artifact.md
qa_rca_doc_delta_summary=audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md
```

### audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.path_proof.txt

```text
path: audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log
size_bytes: 1677
sha256: b1e8066444af3b305d8eaebf9817a7adec1385bc6fdfede921278b69348099ab
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```

### audit/qa/hde-epic034/qa_step_logs_manifest.json

```json
{"entries":[{"check_id":"step-0b-doc-delta-capture","log_path":"audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-001","log_path":"audit/qa/hde-epic034/checks/po-001/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-001/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-002","log_path":"audit/qa/hde-epic034/checks/po-002/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-002/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-003","log_path":"audit/qa/hde-epic034/checks/po-003/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-003/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-004","log_path":"audit/qa/hde-epic034/checks/po-004/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-004/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-005","log_path":"audit/qa/hde-epic034/checks/po-005/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-005/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-006","log_path":"audit/qa/hde-epic034/checks/po-006/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-006/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-007","log_path":"audit/qa/hde-epic034/checks/po-007/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-007/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-008","log_path":"audit/qa/hde-epic034/checks/po-008/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-008/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-009","log_path":"audit/qa/hde-epic034/checks/po-009/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-009/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-010","log_path":"audit/qa/hde-epic034/checks/po-010/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-010/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-011","log_path":"audit/qa/hde-epic034/checks/po-011/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-011/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-012","log_path":"audit/qa/hde-epic034/checks/po-012/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-012/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-013","log_path":"audit/qa/hde-epic034/checks/po-013/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-013/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-014","log_path":"audit/qa/hde-epic034/checks/po-014/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-014/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-015","log_path":"audit/qa/hde-epic034/checks/po-015/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-015/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-016","log_path":"audit/qa/hde-epic034/checks/po-016/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-016/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-017","log_path":"audit/qa/hde-epic034/checks/po-017/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-017/primary.log.path_proof.txt","status":"PASS"},{"check_id":"po-018","log_path":"audit/qa/hde-epic034/checks/po-018/primary.log","path_proof_path":"audit/qa/hde-epic034/checks/po-018/primary.log.path_proof.txt","status":"PASS"}],"epic_id":"HDE-EPIC034","schema_version":"pf27.qa_step_logs_manifest.v1"}
```

### audit/qa/hde-epic034/qa_step_logs_manifest.json.path_proof.txt

```text
path: audit/qa/hde-epic034/qa_step_logs_manifest.json
size_bytes: 3564
sha256: 63564726b393aa06f9aff333569dabbe5ee3e8f8d8a98326b316bb3ad6d21780
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```

### audit/qa/hde-epic034/00_meta/discovery_artifact.md

```md
# HDE-EPIC034 Live QA Discovery Artifact

Discovery posture: repo loci used by this Live QA plan were prechecked from current repo reality, structured repo audit, or QA-created output posture.
Rails posture: PO-012 is the bounded PO-authorized open-rails Live QA step. All other checks in this closeout run are closed rails.
Out-of-scope boundaries: no public Reader expansion, no public route/flag/payload expansion, no new HTTP home, no AI scope, no full HumanDesignAPI v2 runtime conformance, and no HDE-FERM008 parent completion.
```

### audit/qa/hde-epic034/00_meta/discovery_artifact.md.path_proof.txt

```text
path: audit/qa/hde-epic034/00_meta/discovery_artifact.md
size_bytes: 534
sha256: 39c92a74500ec0f0b9761e67d154df44ac822947dc42fbe190ed5cc03e7631f3
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```

### audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md

```md
# HDE-EPIC034 QA RCA and Doc Delta Summary

Coverage vs plan:
* step-0b-doc-delta-capture: PASS - audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log
* po-001: PASS - audit/qa/hde-epic034/checks/po-001/primary.log
* po-002: PASS - audit/qa/hde-epic034/checks/po-002/primary.log
* po-003: PASS - audit/qa/hde-epic034/checks/po-003/primary.log
* po-004: PASS - audit/qa/hde-epic034/checks/po-004/primary.log
* po-005: PASS - audit/qa/hde-epic034/checks/po-005/primary.log
* po-006: PASS - audit/qa/hde-epic034/checks/po-006/primary.log
* po-007: PASS - audit/qa/hde-epic034/checks/po-007/primary.log
* po-008: PASS - audit/qa/hde-epic034/checks/po-008/primary.log
* po-009: PASS - audit/qa/hde-epic034/checks/po-009/primary.log
* po-010: PASS - audit/qa/hde-epic034/checks/po-010/primary.log
* po-011: PASS - audit/qa/hde-epic034/checks/po-011/primary.log
* po-012: PASS - audit/qa/hde-epic034/checks/po-012/primary.log
* po-013: PASS - audit/qa/hde-epic034/checks/po-013/primary.log
* po-014: PASS - audit/qa/hde-epic034/checks/po-014/primary.log
* po-015: PASS - audit/qa/hde-epic034/checks/po-015/primary.log
* po-016: PASS - audit/qa/hde-epic034/checks/po-016/primary.log
* po-017: PASS - audit/qa/hde-epic034/checks/po-017/primary.log
* po-018: PASS - audit/qa/hde-epic034/checks/po-018/primary.log

Doc-delta posture:
Step-0B records the current HDE-EPIC034 doc-delta surfaces. No PF document edit is performed by this runbook.

Known non-claims:
No full HumanDesignAPI v2 runtime conformance, no later HDE-FERM008.3/8.4/8.5 completion, no public Reader change, no public route/flag/payload expansion, no new HTTP home, and no AI scope is claimed by this Live QA run.

Closeout posture:
This closeout assembly check creates QA evidence deliverables only. It does not perform PO closeout, board update, merge, or canon drain.
```

### audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt

```text
path: audit/qa/hde-epic034/00_meta/qa_rca_doc_delta_summary.md
size_bytes: 1843
sha256: 54a5ca84dce91b124210cab3cb69663ec48970ab0223fc2de01c22fa3b860a94
mtime_utc: 2026-06-26T14:50:49Z
produced_at_utc: 2026-06-26T14:50:49Z
```
