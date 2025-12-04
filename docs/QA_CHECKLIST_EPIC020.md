# HDE-EPIC020 QA checklist and rails

This checklist records the EPIC020-specific QA expectations. It complements PF19 and PF20 and does **not** open any new rails.

## Pre-commit checklist (EPIC020-impacting changes)
- Run the EPIC020 deterministic suites locally with closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=LANG=C`, `TZ=UTC`):
  - `tests/adapter/test_jsonschema.py`
  - `tests/cli/test_cli_usage_and_errors.py`
  - `tests/cli/test_errors_parity.py`
  - `tests/cli/test_cli_canonical_bytes.py`
  - `tests/cli/test_showcompat_parity_and_identity.py`
  - `tests/cli/test_serializer_guards.py`
  - `tests/transport/test_internal_version_contract.py`
- If evidence or acceptance artifacts changed, run `python tools/evidence/update_evidence_index.py --check` and `python tools/evidence/orientation_demo.py --check` under the same rails.
- Verify env pins with `ci/checks/check_env_pins.sh` so that `audit/gates/determinism/env_pins.log` stays fresh and indexed.

## Post-commit checklist (EPIC020 close-out)
- All CI jobs, including the "epic020 acceptance suites" job, are green under closed rails.
- Determinism env-pin evidence (`audit/gates/determinism/env_pins.log` + path proof) is present and referenced in the Evidence Index/Mirror.
- Optional Live QA follows PF19: one command → one primary artifact stored under `audit/qa/hde-epic020/{errors,cli_presenter,internal_version}/`.

## Evidence-only pull requests
- Treat a PR as evidence-only when the diff is limited to evidence directories and QA harness material (e.g., `docs/evidence/**`, `artifacts/**`, `audit/qa/hde-epic020/**`, `errors/**`, `parity/**`).
- Minimal CI for evidence-only PRs:
  - `ci/checks/check_env_pins.sh`
  - `python tools/evidence/update_evidence_index.py --check`
  - `python tools/evidence/orientation_demo.py --check`
- No new runtime behavior should change; skip heavier engine suites unless the diff includes code or schemas.

## Diff-scoped CI expectations
- When changes are confined to EPIC020 evidence or presenter/internal-version paths, run the EPIC020 deterministic suites listed above plus `ci/checks/check_env_pins.sh`.
- If code surfaces outside EPIC020 move, fall back to full CI to avoid under-testing.
- Do not add rails-open jobs; keep the SAFE_MODE/ALLOW_NETWORK/locale/TZ pins in place for any scoped run.

## Rails posture (applies to all items above)
- Closed rails are mandatory for EPIC020 QA and CI: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
- Artifacts supporting QA and rails tokens should be mirrored in the Evidence Index/Mirror with the EPIC020 epic ID where applicable.
