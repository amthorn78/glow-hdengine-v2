# HDE-EPIC021 — Live QA Summary

Date/time (UTC): 2025-12-11T18:19:14Z
Branch: qa/hde-epic021-live
Commit: 0be542faa73054d96b20c674f2421904d938a85c

## Commands executed (Steps 1–6)

- Step 1: Initialize QA branch and Live QA directory
  - cd /workspaces/glow-hdengine-v2
  - git checkout -b qa/hde-epic021-live || git checkout qa/hde-epic021-live
  - mkdir -p audit/qa/hde-epic021/live-qa
  - ls -1 tools/qa/epic021_qa.py tests/qa/test_epic021_harness_entrypoint.py tests/qa/test_tooling_bootstrap.py tests/qa/test_epic021_acceptance_alignment.py > audit/qa/hde-epic021/live-qa/STEP1_harness_and_tests_check.txt
  - ls -R audit/qa/hde-epic021 | tee audit/qa/hde-epic021/live-qa/STEP1_init_snapshot.txt

- Step 2: Run EPIC021 harness entrypoint under closed rails (run_id=live-qa-1)
  - export SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC EPIC021_QA_RUN_ID=live-qa-1
  - python -m tools.qa.epic021_qa
  - grep '^summary:' audit/qa/hde-epic021/acceptance_map_viability.log | tee audit/qa/hde-epic021/live-qa/STEP2_acceptance_map_viability_summary.txt
  - python (manifest extract) -> STEP2_manifest_run_live-qa-1.json

- Step 3: Run EPIC021 harness entrypoint tests (closed rails)
  - SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
    pytest tests/qa/test_epic021_harness_entrypoint.py -q \
      | tee audit/qa/hde-epic021/live-qa/STEP3_test_epic021_harness_entrypoint.log

- Step 4: Run generic harness tests (closed rails)
  - SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
    pytest tests/qa/test_generic_qa_harness.py -q \
      | tee audit/qa/hde-epic021/live-qa/STEP4_test_generic_qa_harness.log

- Step 5: Run bootstrap and acceptance alignment tests (closed rails)
  - SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
    pytest tests/qa/test_tooling_bootstrap.py -q \
      | tee audit/qa/hde-epic021/live-qa/STEP5_test_tooling_bootstrap.log
  - SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC \
    pytest tests/qa/test_epic021_acceptance_alignment.py -q \
      | tee audit/qa/hde-epic021/live-qa/STEP5_test_epic021_acceptance_alignment.log

- Step 6: Summarize QA_ROOT state for EPIC021 after Live QA
  - python (summary snippet) -> audit/qa/hde-epic021/live-qa/STEP6_qa_root_summary.json


## Evidence files

All under `audit/qa/hde-epic021/...`:

- STEP1_harness_and_tests_check.txt
- STEP1_init_snapshot.txt
- live-qa-1/D0_bootstrap.log
- live-qa-1/step_bootstrap.log
- live-qa-1/step_serializer_cli_d1.log
- live-qa-1/step_evidence_d2.log
- live-qa-1/step_sanity_d2.log
- live-qa-1/step_acceptance_map_d3.log
- qa_step_logs_manifest.json (updated)
- acceptance_map_viability.log (updated)
- STEP2_acceptance_map_viability_summary.txt
- STEP2_manifest_run_live-qa-1.json
- STEP3_test_epic021_harness_entrypoint.log
- STEP4_test_generic_qa_harness.log
- STEP5_test_tooling_bootstrap.log
- STEP5_test_epic021_acceptance_alignment.log
- STEP6_qa_root_summary.json


## PF references and verdict

References (titles/sections only):
- Live QA Guide for HDE-EPIC021 §1.1–§1.2
- PF10 — HDE-Build Notes (EPIC021 addenda: entrypoint, generic harness, step-level evidence)
- PF09 — HDE-Build Checklist (Calcination QA harness tasks)
- PF19 — Canon-Glow QA Guide (Live QA via Codespaces, closed-rails env pins)

Verdict: EPIC021 D3 QA bootstrap and viability logging acceptance is satisfied for run_id=live-qa-1, based on Steps 1–6.

## Deviations / issues

- Earlier EPIC021 QA harness entrypoint run failed with FAIL_TOOLING (missing pytest); remediated by installing pytest and re-running under closed rails, now passing.
- Final EPIC021 D3 QA evidence (Steps 1–6) shows all harness, generic harness, bootstrap, viability, and acceptance alignment tests passing under closed rails, with no missing tokens (viability summary: COVERED=21 PLANNED=2 MISSING=0).

