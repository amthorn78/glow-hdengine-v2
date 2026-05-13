# HDE-EPIC031 — Fermentation Pass 2 — Action Report (Remediated)

## Overview
This report consolidates PO-001, PO-002, and PO-003 execution and evidence under closed rails and addresses remediation gaps by adding explicit proof for:

1. PO-001 primary-log PASS with exit code 0.
2. PO-001 first-slice scope-boundary closure evidence.
3. PO-003 refusal-before-input/ingest ordering evidence.

Execution posture for all three checks:

- Command pattern: `python audit/qa/hde-epic031/00_meta/live_qa_harness.py <check-id>`
- Rails/env: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`

## Step PO-001 — Fermentation First-Slice Scope Boundary

### Deliverables
- `audit/qa/hde-epic031/checks/po-001/primary.log`
- `audit/qa/hde-epic031/checks/po-001/result.json`

### Full Evidence Output
#### `audit/qa/hde-epic031/checks/po-001/primary.log` (header line)
```json
{
  "captured_env": {
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC"
  },
  "check_id": "po-001",
  "check_name": "PO-001",
  "command": "python audit/qa/hde-epic031/00_meta/live_qa_harness.py po-001",
  "command_provenance": "Copy/paste from plan",
  "evidence_artifacts": [
    "audit/qa/hde-epic031/checks/po-001/primary.log",
    "audit/qa/hde-epic031/checks/po-001/result.json"
  ],
  "exit_code": 0,
  "schema_version": "pf27.step_log_header.v1",
  "status": "PASS",
  "timestamp_utc": "2026-05-13T11:31:43Z"
}
```

#### `audit/qa/hde-epic031/checks/po-001/result.json`
```json
{
  "endpoint_catalog_present": true,
  "has_known_catalog_surfaces": true,
  "no_epic031_public_surface": true,
  "schema": "hde_epic031.po001.scope_boundary.v1",
  "status": "PASS"
}
```

### Remediation Proof Addendum (PO-001 Scope Boundary)
The PO-001 result confirms public-surface closure (`no_epic031_public_surface: true`). The plan-level broader first-slice boundary is additionally evidenced by EPIC031 scope-guardrail/coherence artifacts:

#### `audit/qa/hde-epic031/pr-03/evidence_family_map.json` (scope guardrails)
```json
{
  "scope_guardrails": {
    "acceptance_tokens_created": false,
    "follow_up_scope_implemented": false,
    "live_vendor_call_executed": false,
    "public_reader_contract_changed": false
  }
}
```

#### `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json` (out-of-scope confirmations)
```json
{
  "out_of_scope_confirmations": {
    "hdapi_v2_runtime_conformance_implemented": false,
    "live_vendor_call_executed": false,
    "po_only_open_rails_v2_smoke_executed": false,
    "public_reader_output_changed": false,
    "token_evidence_matrix_rows_created": false
  }
}
```

#### `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`
```text
scope: hde-epic031-pr-02-local-deterministic
live_vendor_calls: forbidden
rails:
  SAFE_MODE = 1
  ALLOW_NETWORK = 0
```

Required exclusion-to-evidence mapping (plan criterion alignment):

- Later vendor-version/runtime expansion remains excluded: `hdapi_v2_runtime_conformance_implemented: false`.
- Later database/runtime follow-up expansion remains excluded: `follow_up_scope_implemented: false`.
- Later router/public-contract expansion remains excluded: `public_reader_contract_changed: false` and `public_reader_output_changed: false`.
- Public-surface expansion remains excluded: `no_epic031_public_surface: true`.
- Close-pack/acceptance expansion remains excluded in this slice: `token_evidence_matrix_rows_created: false` and `acceptance_tokens_created: false`.

### PO-001 Validation Outcome
- `primary.log` records `status: PASS` and `exit_code: 0`.
- `result.json` records `status: PASS` and `no_epic031_public_surface: true`.
- Supplemental EPIC031 scope artifacts record no live-vendor execution and no public-surface widening.

### Status: **PASS**

## Step PO-002 — Closed-by-Default Provider Access with Explicit Bounded Opening

### Deliverables
- `audit/qa/hde-epic031/checks/po-002/primary.log`
- `audit/qa/hde-epic031/checks/po-002/result.json`

### Full Evidence Output
#### `audit/qa/hde-epic031/checks/po-002/primary.log` (header line)
```json
{
  "check_id": "po-002",
  "exit_code": 0,
  "status": "PASS",
  "timestamp_utc": "2026-05-13T11:36:18Z"
}
```

#### `audit/qa/hde-epic031/checks/po-002/result.json`
```json
{
  "closed_default_refusal": true,
  "no_live_vendor_policy": true,
  "open_exception_proof_present": true,
  "pytest": {
    "cmd": [
      "/usr/local/bin/python",
      "-m",
      "pytest",
      "tests/bodygraph/test_vendor_client.py",
      "tests/bodygraph/test_resolver_vendor.py",
      "-q"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": ".................                                                        [100%]\n17 passed in 0.16s\n"
  },
  "schema": "hde_epic031.po002.closed_default_open_exception.v1",
  "status": "PASS"
}
```

### PO-002 Validation Outcome
- Provider tests pass (`pytest.returncode: 0`, `17 passed`).
- Closed-default refusal evidence present.
- Bounded opening evidence present.
- No-live-vendor policy preserved.

### Status: **PASS**

## Step PO-003 — Deterministic Typed Provider Refusal When External Access is Not Allowed

### Deliverables
- `audit/qa/hde-epic031/checks/po-003/primary.log`
- `audit/qa/hde-epic031/checks/po-003/result.json`

### Full Evidence Output
#### `audit/qa/hde-epic031/checks/po-003/primary.log` (header line)
```json
{
  "check_id": "po-003",
  "exit_code": 0,
  "status": "PASS",
  "timestamp_utc": "2026-05-13T11:38:48Z"
}
```

#### `audit/qa/hde-epic031/checks/po-003/result.json`
```json
{
  "closed_evidence_contains_refusal": true,
  "pytest": {
    "cmd": [
      "/usr/local/bin/python",
      "-m",
      "pytest",
      "tests/bodygraph/test_vendor_client.py",
      "tests/bodygraph/test_resolver_vendor.py",
      "-q"
    ],
    "returncode": 0,
    "stderr": "",
    "stdout": ".................                                                        [100%]\n17 passed in 0.04s\n"
  },
  "schema": "hde_epic031.po003.refusal.v1",
  "source_contains_network_blocked": true,
  "source_contains_provider_refused": true,
  "status": "PASS"
}
```

### Remediation Proof Addendum (PO-003 Ordering Before Input/Ingest)
The ordering requirement is proven by both source control flow and tests that assert input resolution must not run when rails are closed/blocked:

#### Resolver control-flow evidence (`engine/bodygraph/resolver.py`)
```text
if safe_mode_closed: return PROVIDER_REFUSED
if not allow_network: return PROVIDER_NETWORK_BLOCKED
vendor_inputs = _resolve_inputs(...)
outcome = ingest_vendor_bodygraph(...)
```

This order demonstrates refusal branches execute before vendor input resolution (`_resolve_inputs`) and before ingest (`ingest_vendor_bodygraph`).

#### Test evidence (`tests/bodygraph/test_resolver_vendor.py`)
```text
test_vendor_resolver_refuses_closed_safe_rails_before_input_or_ingest
  fail_resolve_inputs -> AssertionError("closed SAFE rails must not resolve vendor inputs")
  assert error code == PROVIDER_REFUSED

test_vendor_resolver_requires_open_network_exception_before_ingest
  fail_resolve_inputs -> AssertionError("blocked rails must not resolve vendor inputs")
  assert error code == PROVIDER_NETWORK_BLOCKED
```

### PO-003 Validation Outcome
- Typed refusal markers are present in result/source evidence.
- Provider tests pass (`pytest.returncode: 0`, `17 passed`).
- Ordering criterion is explicitly proven by resolver branch order plus tests that fail if input resolution is attempted before refusal.

### Status: **PASS**

## Final Verdict
REMEDIATION APPLIED. The report now contains step-level proof for PO-001 primary-log PASS/exit, expanded first-slice scope-boundary evidence, and PO-003 refusal-before-input/ingest ordering evidence.