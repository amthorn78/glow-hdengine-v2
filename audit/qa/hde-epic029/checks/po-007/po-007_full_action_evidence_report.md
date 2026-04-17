# HDE-EPIC029 / po-007 - Full Action and Evidence Report

## Scope
This document is the single consolidated action log and full evidence output for step `po-007`.

- Epic: HDE-EPIC029 (Conjunction Pass 5)
- Step: po-007
- Approved QA plan: `r5 QA Plan HDE-EPIC029.md`
- Previous step report: `report po-006 QA Plan HDE-EPIC029.md`
- PF references used by step context: PF10 (current), PF05, PF02
- Governed evidence root: `audit/qa/hde-epic029/checks/po-007/`

## Step Intent (verbatim excerpt)
"The Live QA plan must prove changed behavior through at least one real functional check and must not rely only on artifact refresh or local smoke evidence."

## PASS Criteria (verbatim excerpt)
PASS if:
- the combined functional pytest bundle exits `0`
- the combined output log and rc capture are present under `audit/qa/hde-epic029/checks/po-007/`

## Executed Environment
Captured rails and pins:
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

Source of truth: `audit/qa/hde-epic029/checks/po-007/primary.log`

## Action Log
1. Re-asserted closed rails and determinism pins in the current shell.
2. Created the governed step directory `audit/qa/hde-epic029/checks/po-007/`.
3. Ran step-local pytest dependency preflight (`python -m pytest --version`) and captured output.
4. Ran the approved combined functional bundle:
   - `tests/adapter/test_dev_sampler_http.py`
   - `tests/http/test_dev_conjunction_http.py`
   - `tests/http/test_endpoint_catalog.py`
5. Recorded the combined bundle return code into `functional_bundle.rc.txt`.
6. Reviewed the output log as the real functional proof artifact for this step.
7. Set `PASS_FAIL=PASS` based on observed outcome.
8. Wrote canonical PF27 step receipt into `primary.log`.

## Canonical Final Outcome
Final canonical status: `PASS`.

- status: PASS
- fail_status: (empty)
- timestamp_utc: 2026-04-16T20:32:43Z
- check_id: po-007
- check_name: At least one real functional harness proof exists and passes

`primary.log` payload:

```json
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-04-16T20:32:43Z", "check_id": "po-007", "check_name": "At least one real functional harness proof exists and passes", "status": "PASS", "fail_status": "", "command": "python -m pytest --version | tee audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log; python -m pytest -q tests/adapter/test_dev_sampler_http.py tests/http/test_dev_conjunction_http.py tests/http/test_endpoint_catalog.py |& tee -a audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log; printf '%s\\n' \"${PIPESTATUS[0]}\" | tee audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt", "command_provenance": "Plan + PF10 dependency preflight", "evidence_artifacts": ["audit/qa/hde-epic029/checks/po-007/primary.log", "audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log", "audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 — HDE-Build Notes", "PF06 — Epic Process Guide", "PF19 — Glow QA Guide", "PF27 — Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}
```

## Full Evidence Output
### Required deliverables
- `audit/qa/hde-epic029/checks/po-007/primary.log`
- `audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log`
- `audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt`

### Integrity table (lines, bytes, sha256)
- `audit/qa/hde-epic029/checks/po-007/primary.log`
  - lines: 1
  - bytes: 1203
  - sha256: 705f9754e870ad64d94a41a74acd6005c7cda830c64223dc3a19bd67d8e22e27
- `audit/qa/hde-epic029/checks/po-007/functional_bundle.output.log`
  - lines: 3
  - bytes: 112
  - sha256: c9fe37df4bbf2f235d665249bb2379e96e3c8f9e183ce97b05243ead871a0b45
- `audit/qa/hde-epic029/checks/po-007/functional_bundle.rc.txt`
  - lines: 1
  - bytes: 2
  - sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa

### Evidence excerpts
#### Functional bundle output
From `functional_bundle.output.log`:

```text
pytest 9.0.3
..............                                                           [100%]
14 passed in 0.89s
```

#### Functional bundle return code
From `functional_bundle.rc.txt`:

```text
0
```

## Criteria-to-Evidence Mapping
1. Criterion: combined functional pytest bundle exits `0`.
   - Evidence: `functional_bundle.rc.txt` contains `0`.
2. Criterion: combined output log and rc capture are present under the governed po-007 path.
   - Evidence: both `functional_bundle.output.log` and `functional_bundle.rc.txt` exist in `audit/qa/hde-epic029/checks/po-007/`.
3. Criterion intent: at least one real functional proof bundle is exercised, not only artifact refresh.
   - Evidence: the combined run executed the three approved functional test files and produced passing runtime output (`14 passed`).

## Final Determination
PASS.

Reasoning:
- Dependency preflight succeeded and the combined functional bundle executed.
- The bundle exited with return code `0` and produced passing results.
- Required po-007 governed artifacts are present and complete.
