# Report CHECK po-004 HDE-EPIC027

Date (UTC): 2026-03-18
Check: po-004
Status: PASS

## Intent
Prove the operator-facing CLI is explicitly covered for installability, entrypoint behavior, help and argument handling, deterministic pair behavior, and current contract conformance.

## Preconditions
- po-003 PASS present in audit/qa/hde-epic027/qa_step_logs_manifest.json.
- Existing manifest pair present at:
  - audit/qa/hde-epic027/qa_step_logs_manifest.json
  - audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt
- PF02 preflighted required loci:
  - pyproject.toml
  - tests/cli/test_cli_install_help.py
  - tests/cli/test_bg_resolve.py
  - scripts/hdctl.py

## Rails and Determinism Pins Used
- LC_ALL=C
- LANG=C
- TZ=UTC
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev

## Executed Proof Commands
1. Entrypoint proof:
- { grep -nE '^\[project\.scripts\]' pyproject.toml; grep -nE '^hdctl\s*=\s*"engine\.cli\.main:cli"' pyproject.toml; }

2. Install/help test:
- python -m pytest -q tests/cli/test_cli_install_help.py

3. bg:resolve test:
- python -m pytest -q tests/cli/test_bg_resolve.py

4. bg:resolve help surface:
- python scripts/hdctl.py bg:resolve --help

## Results
- Entrypoint proof found explicit pyproject console binding:
  - [project.scripts]
  - hdctl = "engine.cli.main:cli"
- tests/cli/test_cli_install_help.py: 1 passed
- tests/cli/test_bg_resolve.py: 6 passed
- bg:resolve --help returned usage text with rc=0

## Deliverables Produced
- audit/qa/hde-epic027/checks/po-004/entrypoint_proof.txt
- audit/qa/hde-epic027/checks/po-004/cli_install_help.txt
- audit/qa/hde-epic027/checks/po-004/bg_resolve_test.txt
- audit/qa/hde-epic027/checks/po-004/bg_resolve_help.txt
- audit/qa/hde-epic027/checks/po-004/primary.log
- updated audit/qa/hde-epic027/qa_step_logs_manifest.json
- refreshed audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt

## PO Inputs Resolved
1. Exact approved command string for test_cli_install_help.py capture:
- Used: python -m pytest -q tests/cli/test_cli_install_help.py
- Captured to: audit/qa/hde-epic027/checks/po-004/cli_install_help.txt

2. Exact approved command string for test_bg_resolve.py capture:
- Used: python -m pytest -q tests/cli/test_bg_resolve.py
- Captured to: audit/qa/hde-epic027/checks/po-004/bg_resolve_test.txt

3. Approved help-surface capture for this step:
- Used: python scripts/hdctl.py bg:resolve --help
- This uses the same repo-local CLI surface required by the runbook.

4. Manifest update workflow for po-004:
- No dedicated po-004 helper invocation exists in-repo.
- Used the same governed workflow as earlier checks: read first-line JSON header from audit/qa/hde-epic027/checks/po-004/primary.log and upsert po-004 in audit/qa/hde-epic027/qa_step_logs_manifest.json with check_id, check_name, status, fail_status, log_path, timestamp_utc.

5. Path-proof refresh workflow for po-004:
- No dedicated po-004 helper invocation exists in-repo.
- Refreshed audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt via tools.evidence.update_evidence_index._write_path_proof after manifest update.

6. Governed header-write workflow for po-004 primary.log:
- Wrote required governed first-line JSON header before transcript bytes.
- Header command field records the full ordered command sequence executed in this step.

## Evidence Snapshot (Current)
- po-004 primary header status: PASS
- manifest po-004 entry status: PASS
- manifest path-proof sha256: 8939b65675a251a9995e52ea9681ab85e758b4b5e081d5cf834938c3e4d59026
- manifest path-proof produced_at_utc: 2026-03-18T00:42:31Z
