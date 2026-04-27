# ESCALATION — UID Requirement Leak on Public Compatibility Surface (po-006)

## Escalation metadata
- Epic: HDE-EPIC030 (Dissolution Pass 3)
- Check: po-006
- Date (UTC context): 2026-04-27
- Escalation reason: Public compatibility execution path currently requires person_uid semantics and explicit compat metadata args at call-time, conflicting with no-user / birth-input expectations and causing po-006 behavioral failure.

## Problem statement
The current compatibility compute path requires caller-provided user identity fields and expanded invocation metadata even for chart/birth-derived payloads. This creates a contract mismatch at the public compatibility test surface and breaks po-006.

User requirement captured for escalation:
- Nothing in this system should require a UID to run.

Observed conflict:
- Ordering logic hard-fails when person_uid is missing.
- Public compat compute signature also requires extended args in direct calls.
- Legacy/consumer-style call patterns that pass chart payloads directly fail unless tests inject synthetic person_uid values.

## Current po-006 status (authoritative)
- Step status: FAIL_BEHAVIOR
- Exit code: 1
- pytest rc: 1
- grep rc: 0
- Numeric-free marker present: True

Evidence:
- [po-006 primary header and appended logs](audit/qa/hde-epic030/checks/po-006/primary.log#L1)
- [po-006 exit code](audit/qa/hde-epic030/checks/po-006/exit_code.txt)
- [po-006 pytest rc](audit/qa/hde-epic030/checks/po-006/pytest_rc.txt)
- [po-006 grep rc](audit/qa/hde-epic030/checks/po-006/grep_rc.txt)
- [po-006 numeric-free grep output](audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt)

## Evidence of the defect
### 1) Hard UID gate in ordering
The ordering layer rejects missing/invalid person_uid:
- [engine/compat/ordering.py](engine/compat/ordering.py#L6)
- [engine/compat/ordering.py](engine/compat/ordering.py#L10)
- [engine/compat/ordering.py](engine/compat/ordering.py#L14)

Quoted behavior:
- `_uid` reads person_uid and raises ValueError("invalid or missing person_uid") when absent/invalid.
- `normalize_pair` always calls `_uid` for both inputs before ordering.

### 2) Public compute call requires expanded invocation args
The compute function signature requires viewer and invocation metadata args:
- [engine/compat/compute.py](engine/compat/compute.py#L36)

Quoted behavior:
- `compat_public(a, b, viewer_top, viewer_weights, engine_tag, release_id, invocation_tag)`

### 3) po-006 failure trace shows public-surface break
Failure trace recorded under po-006:
- [po-006 pytest output](audit/qa/hde-epic030/checks/po-006/pytest_stdout.log)

Quoted failure from recorded step evidence:
- `TypeError: compat_public() missing 5 required positional arguments: 'viewer_top', 'viewer_weights', 'engine_tag', 'release_id', and 'invocation_tag'`
- Failing test: `tests/compat/test_compat_public_lf_bom.py::test_public_bytes_lf_and_no_bom`

### 4) Local test workaround now required to satisfy current contract
Current local test file had to be expanded to pass required args and inject person_uid values:
- [tests/compat/test_compat_public_lf_bom.py](tests/compat/test_compat_public_lf_bom.py#L7)
- [tests/compat/test_compat_public_lf_bom.py](tests/compat/test_compat_public_lf_bom.py#L15)
- [tests/compat/test_compat_public_lf_bom.py](tests/compat/test_compat_public_lf_bom.py#L16)

This indicates contract drift from no-user birth/chart input assumptions.

## PF05 alignment analysis (command syntax + rails)
### Canon clauses relevant to this escalation
PF05 states pre-Glow QA compatibility should use birth-based showcompat with explicit vendor source and open rails for vendor acquisition:
- [PF05 pre-Glow compat guidance](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L332)
- [PF05 source=vendor requirement](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L334)
- [PF05 open-rails requirement for vendor acquisition](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L335)

PF05 also codifies showcompat input-family syntax and source behavior:
- [PF05 showcompat input requirement](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L401)
- [PF05 showcompat DB user syntax](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L411)
- [PF05 source semantics and vendor-open-rails note](docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.0.3.md#L419)

### What this means for po-006
- po-006 is a pytest-driven check, not a direct showcompat command execution.
- Opening rails was done and captured in po-006 header, but it did not resolve the failing pytest contract issue.
- The observed po-006 fail is contract-shape related (function signature/input assumptions), not grep/tooling and not rails gating.

## Impact
- po-006 cannot pass under current test/compute contract mismatch.
- Public compatibility assurance (band-only and numeric-free) is partially demonstrated (grep marker is present) but blocked by failing pytest behavior gate.
- UID-coupling remains observable in compute ordering path and is inconsistent with the no-user requirement for this stage.

## Reproduction summary (from evidence)
1. Execute po-006 flow under open rails (SAFE_MODE=0, ALLOW_NETWORK=1).
2. Observe `pytest_rc=1`, `grep_rc=0`, `exit=1`.
3. Inspect pytest output and see compat_public call-shape failure.
4. Observe numeric-free marker still present in grep artifact.

Evidence:
- [po-006 primary.log](audit/qa/hde-epic030/checks/po-006/primary.log)
- [po-006 pytest output](audit/qa/hde-epic030/checks/po-006/pytest_stdout.log)
- [po-006 numeric-free grep](audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt)

## Root-cause hypothesis (technical)
Primary:
- Public compat compute and tests are not fully aligned on invocation contract.

Contributing:
- Ordering implementation is UID-first and rejects payloads lacking person_uid.
- Test surface historically expected simpler direct invocation from chart payloads.

## Escalation decision request
Please decide which canonical direction to apply:
1. Contract-first direction: Keep strict compat_public invocation and UID-dependent ordering; update all callers/tests to provide required metadata and identity fields through a sanctioned pre-normalization layer.
2. No-UID direction: Refactor ordering/compute to support deterministic pair identity without requiring person_uid, then adjust PF05/PF10-aligned proofs accordingly.
3. Adapter boundary direction: Keep compute strict internally but guarantee public/birth-facing adapters always supply canonical synthetic identity and invocation metadata before calling compat_public.

## Proposed remediation tracks (no implementation in this escalation file)
- Track A (fastest for po-006): Normalize test invocation to match compute contract and ensure deterministic identity provisioning in fixture/setup layer.
- Track B (policy-aligned no-user posture): Define and implement UID-independent deterministic ordering key for chart payloads, then update tests and evidence generators.
- Track C (hybrid): Preserve internal strictness but require adapter-level coercion with explicit documented invariants and evidence.

## Closing note
This escalation intentionally records evidence and impact without asserting a final architecture choice. The immediate blocker is confirmed, reproducible, and tied to concrete code and po-006 artifacts listed above.
