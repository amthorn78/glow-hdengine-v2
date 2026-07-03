# HDE-EPIC036 Live QA Action Report

- Epic: `HDE-EPIC036` (Fermentation Pass 7)
- Scope: `step-0b-doc-delta-capture`, `po-001` ... `po-009`
- Repo: `amthorn78/glow-hdengine-v2`
- Branch: `main`
- Generated at (UTC): `2026-07-03T01:21:35Z`

## Manifest Header

- Artifact Map: `HDE-EPIC: HDE-EPIC036 / Fermentation Pass 7`
- Approved QA Plan File: `QA Plan HDE-EPIC036.md`
- Approval Doc File: `approval QA Plan HDE-EPIC036.md`
- Previous Step Report File: `none`
- Canon consulted: `PF10 (current) + PF05 + PF02`
- Rails pins used: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`

## Executive Summary

- Overall result: `PASS` for all requested checks.
- Check count: `10/10 PASS`
- Primary logs and sibling path proofs: present for all checks.

## Check step-0b-doc-delta-capture

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:08Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py step-0b-doc-delta-capture`
- Primary log: `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`)
- Intended tokens: `['DOC_DELTA_PRESENT_OK']`
- Claimed tokens: `['DOC_DELTA_PRESENT_OK']`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`
- `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`
- `audit/docdeltas/hde-epic036_doc_deltas.md`
- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`
- `audit/qa/hde-epic036/00_meta/doc_deltas.md`
- `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt`

## Check po-001

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:15Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-001`
- Primary log: `audit/qa/hde-epic036/checks/po-001/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`)
- Intended tokens: `['NO_EXTERNAL_IO_ON_REFUSAL_OK']`
- Claimed tokens: `['NO_EXTERNAL_IO_ON_REFUSAL_OK']`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-001/primary.log`
- `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
- `tests/bodygraph/test_bg_resolve_route_policy.py`

## Check po-002

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:15Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-002`
- Primary log: `audit/qa/hde-epic036/checks/po-002/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`)
- Intended tokens: `['ENV_RAILS_POLICY_OK']`
- Claimed tokens: `['ENV_RAILS_POLICY_OK']`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-002/primary.log`
- `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `audit/qa/hde-epic036/route_policy_decision.log`

## Check po-003

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:15Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-003`
- Primary log: `audit/qa/hde-epic036/checks/po-003/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-003/primary.log`
- `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

## Check po-004

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-004`
- Primary log: `audit/qa/hde-epic036/checks/po-004/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-004/primary.log`
- `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
- `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

## Check po-005

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-005`
- Primary log: `audit/qa/hde-epic036/checks/po-005/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-005/primary.log`
- `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `tests/bodygraph/test_bg_resolve_route_policy.py`

## Check po-006

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-006`
- Primary log: `audit/qa/hde-epic036/checks/po-006/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-006/primary.log`
- `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`

## Check po-007

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-007`
- Primary log: `audit/qa/hde-epic036/checks/po-007/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-007/primary.log`
- `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`
- `docs/acceptance_map_epic036.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
- `audit/qa/hde-epic036/route_policy_decision.log`

## Check po-008

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-008`
- Primary log: `audit/qa/hde-epic036/checks/po-008/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-008/primary.log`
- `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
- `audit/qa/hde-epic036/route_policy_decision.log`
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`
- `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`

## Check po-009

- Status: `PASS`
- Exit code: `0`
- Timestamp (UTC): `2026-07-03T01:13:16Z`
- Schema: `pf27.step_log_header.v1`
- Command: `python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-009`
- Primary log: `audit/qa/hde-epic036/checks/po-009/primary.log`
- Primary path proof present: `True` (`audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`)
- Intended tokens: `[]`
- Claimed tokens: `[]`

Evidence artifacts declared in header:

- `audit/qa/hde-epic036/checks/po-009/primary.log`
- `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
- `docs/acceptance_map_epic036.json`
- `audit/qa/hde-epic036/route_policy_decision.log`

## Status Matrix

| Check ID | Status | Exit | Timestamp UTC | Primary Log |
|---|---|---:|---|---|
| `step-0b-doc-delta-capture` | `PASS` | `0` | `2026-07-03T01:13:08Z` | `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log` |
| `po-001` | `PASS` | `0` | `2026-07-03T01:13:15Z` | `audit/qa/hde-epic036/checks/po-001/primary.log` |
| `po-002` | `PASS` | `0` | `2026-07-03T01:13:15Z` | `audit/qa/hde-epic036/checks/po-002/primary.log` |
| `po-003` | `PASS` | `0` | `2026-07-03T01:13:15Z` | `audit/qa/hde-epic036/checks/po-003/primary.log` |
| `po-004` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-004/primary.log` |
| `po-005` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-005/primary.log` |
| `po-006` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-006/primary.log` |
| `po-007` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-007/primary.log` |
| `po-008` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-008/primary.log` |
| `po-009` | `PASS` | `0` | `2026-07-03T01:13:16Z` | `audit/qa/hde-epic036/checks/po-009/primary.log` |

## Consolidated Evidence Outputs

- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json` (exists=`True`)
- `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt` (exists=`True`)
- `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` (exists=`True`)
- `audit/docdeltas/hde-epic036_doc_deltas.md` (exists=`True`)

## Test Run Update (2026-07-03 UTC)

- Pytest readiness proof: `python3 -m pip install -r requirements-dev.txt && python3 -m pytest --version` completed; reported `pytest 8.4.2`.
- Harness execution check (implemented scope): `python3 audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-009` returned `status=PASS exit_code=0`.
- Harness execution check (requested po-010): `python3 audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-010` returned `UNKNOWN_CHECK:po-010`.
- Conclusion: current runtime evidence confirms the existing helper-locus contradiction for po-010; execution remains blocked until po-010 is registered in the harness.

## Moon Loop Remediation Update (2026-07-03 UTC)

- Remediation applied: `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` now registers executable `po-010` behavior probing.
- Remediation execution: `python3 audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-010` returned `status=PASS exit_code=0`.
- Behavior proof captured by remediation run:
	- `error.code=PROVIDER_ROUTE_UNSUPPORTED`
	- `route_policy.classification=unsupported_runtime_nonclaim`
	- `HD_API_BASE_URL=REDACTED` in `live_route_policy.log`
- New generated po-010 artifacts:
	- `audit/qa/hde-epic036/checks/po-010/primary.log`
	- `audit/qa/hde-epic036/checks/po-010/primary.log.path_proof.txt`
	- `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`
	- `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`
- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/doc_deltas.md` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-001/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-002/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-003/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-004/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-005/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-006/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-007/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-008/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-009/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log` (exists=`True`)
- `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/route_policy_decision.log` (exists=`True`)
- `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt` (exists=`True`)
- `docs/acceptance_map_epic036.json` (exists=`True`)
- `tests/bodygraph/test_bg_resolve_route_policy.py` (exists=`True`)

## Additional Step-0B Deliverables

- `audit/docdeltas/hde-epic036_doc_deltas.md` (exists=`True`)
- `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/doc_deltas.md` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py` (exists=`True`)
- `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt` (exists=`True`)

## Notes

- Report compiled from the generated `primary.log` headers and filesystem existence checks only.
- No product/runtime code paths were modified as part of this reporting step.
