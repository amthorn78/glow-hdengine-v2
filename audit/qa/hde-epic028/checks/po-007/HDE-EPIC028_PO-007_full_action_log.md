# HDE-EPIC028 PO-007 Full Action Log

## Manifest Header
- HDE-EPIC: HDE-EPIC028 / Conjunction Pass 4
- Step: PO-007 - One coherent current-epic acceptance binding
- Approved QA Plan File: r9 Live QA Plan HDE-EPIC028.md
- Approval Doc File: none
- Previous Step Report File: report - po-006 QA HDE-EPIC028.md
- PF-Canon consulted: PF10 (current) + PF05 + PF02 (+ PF12 + PF19 for one execution gap)
- Generated at (UTC): 2026-04-03T15:26:50Z

## Outcome
- Final status: PASS
- Fail status: (empty)
- Scope: snapshot-and-verify only (no ledger regeneration, no relocation, no alternate homes)

## Rails and Repo State
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC
- git HEAD: e5703d58447f38394f25cbcd113eebf6883366b5
- git status (po-007 scope):

?? audit/qa/hde-epic028/checks/po-007/

## Executed Actions
1. Confirmed D0 and all four approved source loci exist at expected paths.
2. Captured snapshots for acceptance map, token matrix, and viability log into check-scoped outputs.
3. Captured EPIC028 binding rows from the machine mirror into mirror_binding_snapshot.jsonl.
4. Evaluated lane criteria: required homes present, expected mirror rows present, no alternate acceptance-map home detected.
5. Wrote primary.log with the resulting status lane and decision note.

## Commands Used
- set -euo pipefail
- export LC_ALL=C
- export LANG=C
- export TZ=UTC
- export SAFE_MODE=1
- export ALLOW_NETWORK=0
- export APP_ENV=dev
- mkdir -p audit/qa/hde-epic028/checks/po-007
- test -f audit/qa/hde-epic028/checks/d0/primary.log
- test -f docs/acceptance_map_epic028.json
- test -f audit/qa/hde-epic028/token_evidence_matrix.md
- test -f audit/qa/hde-epic028/acceptance_map_viability.log
- test -f artifacts/evidence_index.jsonl
- python: capture acceptance_map_snapshot.json from docs/acceptance_map_epic028.json
- python: capture token_matrix_snapshot.txt from audit/qa/hde-epic028/token_evidence_matrix.md
- python: capture acceptance_map_viability_snapshot.txt from audit/qa/hde-epic028/acceptance_map_viability.log
- python: extract EPIC028 mirror rows to mirror_binding_snapshot.jsonl from artifacts/evidence_index.jsonl
- python: evaluate PASS/FAIL/FAIL_TOOLING lane and write primary.log

## Evidence Outputs (Metadata)
- audit/qa/hde-epic028/checks/po-007/primary.log
  - sha256: 364b28ffa23185b59b5b769deae3537f7476c41632ce30914bef9f956bd47b39
  - size_bytes: 2518
  - mtime_epoch: 1775229896
- audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json
  - sha256: 86a42ba30ab17925bb7d27802e288d2ed6b349b3919e2e5fa72bba50bcb2587f
  - size_bytes: 2222
  - mtime_epoch: 1775229895
- audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt
  - sha256: 626e61164b023e6bbc9bd6d043d708b39b2dada16162cfb405146d08668b0eb5
  - size_bytes: 3448
  - mtime_epoch: 1775229895
- audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt
  - sha256: da8202bb2cf82eea897515d37cd4ac0a7f6d9138645cf065e9236ce90180d2cb
  - size_bytes: 485
  - mtime_epoch: 1775229895
- audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl
  - sha256: 3ccb35ef76b10ef04e414346ad958885bf41cab132833747c3177b2eb49ffa9e
  - size_bytes: 1100
  - mtime_epoch: 1775229896

## Evidence Outputs (Full Verbatim Content)
### audit/qa/hde-epic028/checks/po-007/primary.log

{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-007","check_name":"One coherent current-epic acceptance binding","claimed_tokens":[],"command":"python -c \"from pathlib import Path; src=Path('docs/acceptance_map_epic028.json').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json').write_text('\\\\n'.join(src[:40])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('audit/qa/hde-epic028/token_evidence_matrix.md').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt').write_text('\\\\n'.join(src[:40])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('audit/qa/hde-epic028/acceptance_map_viability.log').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt').write_text('\\\\n'.join(src[:60])+'\\\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; lines=Path('artifacts/evidence_index.jsonl').read_text(encoding='utf-8').splitlines(); keep=[line for line in lines if 'epic028.acceptance_map' in line or 'epic028.acceptance_map_viability' in line or 'epic028.token_matrix' in line]; Path('audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl').write_text('\\\\n'.join(keep)+'\\\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-007/primary.log","audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json","audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt","audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt","audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 — HDE-Build Notes","PF05 — HDE-CLI-API-Vendor-Ref","PF02 — HDE-Architecture","PF12 — HDE-Schemas-and-Artifacts","PF19 — Glow QA Guide","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-03T15:24:56Z"}
planned_step: capture the acceptance map, token matrix, viability log, and mirror bindings
decision_note: the current epic acceptance binding remains single-home at docs/acceptance_map_epic028.json, audit/qa/hde-epic028/token_evidence_matrix.md, and audit/qa/hde-epic028/acceptance_map_viability.log, and the machine mirror includes matching rows for all three

### audit/qa/hde-epic028/checks/po-007/acceptance_map_snapshot.json

{"epic_id":"HDE-EPIC028","tokens":[{"evidence_titles":["artifacts/proofs/success_get.txt"],"name":"A7_GET_QUOTED_ETAG_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["artifacts/proofs/success_head.txt","artifacts/proofs/success_get.txt"],"name":"A7_HEAD_PARITY_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["artifacts/proofs/success_304.txt"],"name":"A7_304_OMITS_CT_CL_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["artifacts/proofs/success_get.txt","artifacts/proofs/success_head.txt"],"name":"A7_VARY_AUTH_AE_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["artifacts/proofs/success_encoding_invariance.txt","artifacts/proofs/encoding_invariance.txt"],"name":"A7_ENCODING_INVARIANCE_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["docs/ENDPOINTS_CATALOG.json","docs/ENDPOINTS_CATALOG.json.sha256"],"name":"ENDPOINTS_CATALOG_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["docs/ENDPOINTS_CATALOG.json","artifacts/proofs/endpoints_env_gate_proof.log"],"name":"ENDPOINTS_CATALOG_ENV_GATE_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["artifacts/proofs/success_get.txt","tests/http/test_reader_a7_transport.py"],"name":"READER_200_CTYPE_JSON_UTF8_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["catalog/magic10.json","tests/categories/test_registry_and_purity.py"],"name":"MAGIC10_DOMAIN_CLOSED_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"},{"evidence_titles":["tests/http/test_compat_endpoint_contract.py","engine/compat/categories.py"],"name":"PREFS_KEYSET_10_OK","owner_pf":"PF04 \u2014 Canon-HDE-Governance \u00a72.0 Acceptance Tokens","status":"implemented"}]}

### audit/qa/hde-epic028/checks/po-007/token_matrix_snapshot.txt

# HDE-EPIC028 Token ↔ Evidence Matrix

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| A7_GET_QUOTED_ETAG_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_get.txt | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | Reader A7 GET proof bound on cataloged /reader success route. |
| A7_HEAD_PARITY_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_head.txt; artifacts/proofs/success_get.txt | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | HEAD parity proof reuses existing governed captures. |
| A7_304_OMITS_CT_CL_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_304.txt | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | 304 omission of Content-Type/Content-Length is preserved. |
| A7_VARY_AUTH_AE_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_get.txt; artifacts/proofs/success_head.txt | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | Vary header parity remains Authorization, Accept-Encoding. |
| A7_ENCODING_INVARIANCE_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_encoding_invariance.txt; artifacts/proofs/encoding_invariance.txt | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | Encoding invariance capture is retained under governed proof path. |
| ENDPOINTS_CATALOG_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/ENDPOINTS_CATALOG.json; docs/ENDPOINTS_CATALOG.json.sha256 | python -m pytest -q tests/http/test_endpoint_catalog.py | acceptance_map_viability.log | Implemented | Endpoint catalog single-home inventory is validated. |
| ENDPOINTS_CATALOG_ENV_GATE_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/ENDPOINTS_CATALOG.json; artifacts/proofs/endpoints_env_gate_proof.log | python -m pytest -q tests/http/test_endpoint_catalog.py tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | Catalog env-gate representation and blocked-call proof are both present. |
| READER_200_CTYPE_JSON_UTF8_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/proofs/success_get.txt; tests/http/test_reader_a7_transport.py | python -m pytest -q tests/http/test_reader_a7_transport.py | acceptance_map_viability.log | Implemented | Reader 200 contract asserts six-key envelope and JSON UTF-8 content-type. |
| MAGIC10_DOMAIN_CLOSED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | catalog/magic10.json; tests/categories/test_registry_and_purity.py | python -m pytest -q tests/categories/test_registry_and_purity.py | acceptance_map_viability.log | Implemented | Magic10 registry/domain closure proof reused from existing category tests. |
| PREFS_KEYSET_10_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | engine/compat/categories.py; tests/http/test_compat_endpoint_contract.py | python -m pytest -q tests/http/test_compat_endpoint_contract.py | acceptance_map_viability.log | Implemented | Viewer prefs keyset contract is bound to compat endpoint contract tests. |

### audit/qa/hde-epic028/checks/po-007/acceptance_map_viability_snapshot.txt

run:epic028-reader-ledger utc:2026-03-27T11:40:53.724019+00:00
token A7_GET_QUOTED_ETAG_OK: COVERED
token A7_HEAD_PARITY_OK: COVERED
token A7_304_OMITS_CT_CL_OK: COVERED
token A7_VARY_AUTH_AE_OK: COVERED
token A7_ENCODING_INVARIANCE_OK: COVERED
token ENDPOINTS_CATALOG_OK: COVERED
token ENDPOINTS_CATALOG_ENV_GATE_OK: COVERED
token READER_200_CTYPE_JSON_UTF8_OK: COVERED
token MAGIC10_DOMAIN_CLOSED_OK: COVERED
token PREFS_KEYSET_10_OK: COVERED
summary: COVERED=10 PLANNED=0 MISSING=0

### audit/qa/hde-epic028/checks/po-007/mirror_binding_snapshot.jsonl

{"artifact_key":"epic028.acceptance_map","discovered_physical_path":"docs/acceptance_map_epic028.json","epic_id":"HDE-EPIC028","produced_at_utc":"2026-03-27T11:40:53Z","proof_anchor":"docs/acceptance_map_epic028.json.path_proof.txt","role":"snapshot","sha256":"86a42ba30ab17925bb7d27802e288d2ed6b349b3919e2e5fa72bba50bcb2587f","size_bytes":2222}
{"artifact_key":"epic028.acceptance_map_viability","discovered_physical_path":"audit/qa/hde-epic028/acceptance_map_viability.log","epic_id":"HDE-EPIC028","produced_at_utc":"2026-03-27T11:40:53Z","proof_anchor":"audit/qa/hde-epic028/acceptance_map_viability.log.path_proof.txt","role":"log","sha256":"da8202bb2cf82eea897515d37cd4ac0a7f6d9138645cf065e9236ce90180d2cb","size_bytes":485}
{"artifact_key":"epic028.token_matrix","discovered_physical_path":"audit/qa/hde-epic028/token_evidence_matrix.md","epic_id":"HDE-EPIC028","produced_at_utc":"2026-03-27T11:40:53Z","proof_anchor":"audit/qa/hde-epic028/token_evidence_matrix.md.path_proof.txt","role":"snapshot","sha256":"626e61164b023e6bbc9bd6d043d708b39b2dada16162cfb405146d08668b0eb5","size_bytes":3448}
