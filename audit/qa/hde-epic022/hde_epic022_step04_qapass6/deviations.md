# Deviations — STEP-04 (HDE-EPIC022 / HDE Separation Pass 2)

## DEV-01
- What changed: STEP-04 could not run the evidence index + mirror parity checks as written because `tools/qa/evidence_index_validate.py` is missing; step exited early with `STATUS=FAIL_TOOLING`, `EXIT_CODE=2`, `MANIFEST_VALID=0`.
- Why: The required script path does not exist in the repo, so the command `python tools/qa/evidence_index_validate.py --epic "HDE-EPIC022"` fails before validation can proceed.
- Original plan reference: Approved Plan — Step ID: STEP-04 (parity + manifest validity checks under closed rails).
- Commands actually run: See `stdout/step-04.stdout.txt` and `stderr/step-04.stderr.txt` (stderr records the missing file error) and the recorded step log at `step_logs/step-04.log` within this bundle.
- Evidence files impacted: `results/step-04.result.env` (FAIL_TOOLING, MANIFEST_VALID=0); `artifacts/manifest_valid.txt` was not produced; `artifacts/qa_step_logs_manifest.json` copied for context.
