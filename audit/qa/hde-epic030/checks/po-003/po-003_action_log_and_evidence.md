# CHECK po-003 Action Log and Evidence Output

## Step identity
- Check ID: po-003
- Check name: Viewer-preference normalization must reject invalid input while preserving deterministic, stable output for valid input.
- Scope: HDE-EPIC030 / Dissolution Pass 3 / normalization proof surface
- Canon posture: retrieval-first and proof-first; closed rails; no route/scope widening

## Deterministic execution posture
The check was executed with the required pinned environment:
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

Evidence: PF27 header captured environment in [primary.log](primary.log).

## Command provenance and execution notes
Approved command identity (plan-aligned) was used for the authoritative run:
1. python --version
2. python -m pytest --version
3. python -m pip install -r requirements-dev.txt (only if pytest readiness fails)
4. python -m pytest tests/unit/test_viewer_prefs_normalization.py
5. python tools/evidence/generate_epic030_pr01_normalization_evidence.py
6. PF27 inline header writer to build check header JSON
7. Append preflight/pytest/generator stdout logs into primary.log

Command provenance recorded in header:
- Copy/paste from approved plan with QA syntax-safe dependency capture

Evidence: [primary.log](primary.log)

## Detailed action log
1. Created check output directory.
- Path: audit/qa/hde-epic030/checks/po-003
- Result: completed
- Evidence: [primary.log](primary.log)

2. Initialized step-local output files.
- Files initialized: preflight_stdout.log, preflight_stderr.log, pytest_stdout.log, pytest_stderr.log, generator_stdout.log, generator_stderr.log
- Result: completed
- Evidence: [primary.log](primary.log)

3. Ran dependency readiness checks.
- Python version probe: success (Python 3.11.15)
- Pytest version probe: success (pytest 8.4.2)
- Repo loci probes: both required loci present
  - tests/unit/test_viewer_prefs_normalization.py
  - tools/evidence/generate_epic030_pr01_normalization_evidence.py
- Result: readiness passed; no install action required on authoritative run
- Evidence: [preflight_stdout.log](preflight_stdout.log)

4. Executed viewer-preference normalization pytest target.
- Command: python -m pytest tests/unit/test_viewer_prefs_normalization.py
- Result: 4 collected, 4 passed
- pytest rc: 0
- Evidence:
  - [pytest_stdout.log](pytest_stdout.log)
  - [pytest_rc.txt](pytest_rc.txt)

5. Executed PR-01 normalization evidence generator.
- Command: python tools/evidence/generate_epic030_pr01_normalization_evidence.py
- Result: completed without stderr output
- generator rc: 0
- Evidence:
  - [generator_rc.txt](generator_rc.txt)
  - [generator_stdout.log](generator_stdout.log)
  - [generator_stderr.log](generator_stderr.log)

6. Validated required PR-01 artifacts are present and non-empty.
- audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log: non-empty (124 bytes)
- audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log: non-empty (151 bytes)
- Result: pass
- Evidence:
  - [invalid_viewer_prefs.log](../../pr-01/invalid_viewer_prefs.log)
  - [normalization_canonical_compare.log](../../pr-01/normalization_canonical_compare.log)

7. Wrote PF27-style primary log header and appended execution logs.
- Header schema: pf27.step_log_header.v1
- Header status: PASS
- Header exit_code: 0
- Result: completed
- Evidence: [primary.log](primary.log)

8. Computed final step classification.
- PASS/FAIL status: PASS
- Step exit code: 0
- Evidence:
  - [primary.log](primary.log)
  - [exit_code.txt](exit_code.txt)

## PASS/FAIL determination (deliverable-linked)
PASS criteria required:
- pytest exit code is 0
- generator exit code is 0
- invalid_viewer_prefs.log exists and is non-empty
- normalization_canonical_compare.log exists and is non-empty

Observed values:
- pytest rc: 0 ([pytest_rc.txt](pytest_rc.txt))
- generator rc: 0 ([generator_rc.txt](generator_rc.txt))
- invalid_viewer_prefs.log: 124 bytes ([invalid_viewer_prefs.log](../../pr-01/invalid_viewer_prefs.log))
- normalization_canonical_compare.log: 151 bytes ([normalization_canonical_compare.log](../../pr-01/normalization_canonical_compare.log))

Decision:
- PASS

## Evidence artifact inventory
Check-local artifacts:
- [primary.log](primary.log)
- [preflight_stdout.log](preflight_stdout.log)
- [preflight_stderr.log](preflight_stderr.log)
- [pytest_stdout.log](pytest_stdout.log)
- [pytest_stderr.log](pytest_stderr.log)
- [pytest_rc.txt](pytest_rc.txt)
- [generator_stdout.log](generator_stdout.log)
- [generator_stderr.log](generator_stderr.log)
- [generator_rc.txt](generator_rc.txt)
- [exit_code.txt](exit_code.txt)

PR-01 evidence artifacts used by this check:
- [invalid_viewer_prefs.log](../../pr-01/invalid_viewer_prefs.log)
- [normalization_canonical_compare.log](../../pr-01/normalization_canonical_compare.log)

## Artifact size snapshot (bytes)
- primary.log: 1831
- preflight_stdout.log: 28
- preflight_stderr.log: 0
- pytest_stdout.log: 416
- pytest_stderr.log: 0
- generator_stdout.log: 0
- generator_stderr.log: 0
- invalid_viewer_prefs.log: 124
- normalization_canonical_compare.log: 151

## Final outcome summary
CHECK po-003 is recorded as PASS under closed deterministic rails, with required test/generator return codes at 0 and both required PR-01 normalization evidence logs present and non-empty.
