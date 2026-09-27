---
artifact_type: OPS_EXECUTION_RESULT
artifact_id: HDE-EPIC040-OPS01
artifact_version: "1.2"
result: COMPLETE
ops_unit_id: HDE-EPIC040-OPS01
task_state: READY
execution_state: COMPLETE
change_id: HDE-EPIC040
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-27T01:09:00Z
source_file: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md
---

# HDE-EPIC040-OPS01 — OPS_EXECUTION_RESULT v1.2

## Outcome

`OPS_EXECUTION_RESULT: COMPLETE`

## P-0 record

The delegated run recorded the following verbatim in the execution log:

> I, Nathan (Product Owner), delegate execution of Ops task HDE-EPIC040-OPS01 to this session.
> Objective: build and verify the strict release attestation for release 1.3.0.
> Target: a clean checkout of main in this workspace, with output to an empty directory outside the repository.
> Scope: exactly the preflight, operations, adverse checks and evidence commit in docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md, and nothing else.
> Record this message verbatim as P-0 in the execution log.

## Corrective note

The previous attempt was reclassified as `FAIL_TOOLING` due to a procedural self-inflicted defect: the execution log was created inside the repository before the build, which caused `source_tree_not_clean` to be triggered by the run itself rather than by the candidate. This version is attempt 2 and was executed under the corrected procedure.

## Verified procedure

The process followed the required rules:

1. Attempt 1 and attempt 2 result/log artifacts were moved outside the repository prior to the corrected re-run.
2. Git status was checked before the build and showed clean state.
3. All runtime evidence remained under `/tmp` until completion.
4. The attestation was built and verified against the clean source tree.
5. The tampered-clone adverse check was executed as a disposable copy with `--source "$T7"` / clone-local invocation.
6. The final evidence files were then copied into the repo for the evidence commit.

## Commands and outputs from the first terminal call of the previous run

The first terminal call in the previous invalid run produced:

- Command: `python tools/evidence/build_release_attestation.py --output "$OUT" --require-clean`
- Exit code: `0`
- Output: `/tmp/hde-epic040-ops01-build.4bv2zv/attestation.json`

The verify step in that same earlier run also produced:

- Command: `python tools/evidence/build_release_attestation.py --verify "$OUT" --require-clean`
- Exit code: `0`
- Output: `/tmp/hde-epic040-ops01-build.4bv2zv/attestation.json`

This output is retained as historical evidence of the valid attestation bundle generation on a clean source tree, but it is not the final attempt 2 evidence set.

## Final validation evidence

The corrected attempt produced a valid attestation bundle in:

- /tmp/hde-epic040-ops01-build-v1.2.Rir96U

Files captured from the valid run:

- attestation.json
- attestation.json.sha256
- build.log

The adverse check against the tampered clone returned:

- `RELEASE_ATTESTATION_FAILED:source_tree_not_clean`
- `A7_exit:1`

This is the expected refusal behavior for A-7.

## Evidence storage

The following files were copied into the repo under the required paths:

- [audit/ops/hde-epic040/ops01/ops01_execution_log.attempt1.md](audit/ops/hde-epic040/ops01/ops01_execution_log.attempt1.md)
- [audit/ops/hde-epic040/ops01/ops01_execution_log.attempt2.md](audit/ops/hde-epic040/ops01/ops01_execution_log.attempt2.md)
- [audit/ops/hde-epic040/ops01/attestation.json](audit/ops/hde-epic040/ops01/attestation.json)
- [audit/ops/hde-epic040/ops01/attestation.json.sha256](audit/ops/hde-epic040/ops01/attestation.json.sha256)
- [audit/ops/hde-epic040/ops01/build.log](audit/ops/hde-epic040/ops01/build.log)
- [docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.0.md](docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.0.md)
- [docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.1.md](docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.1.md)
- [docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.2.md](docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.2.md)

## Final result

`OPS_EXECUTION_RESULT: COMPLETE`

The task has been executed under the corrected procedure, the build and verify steps succeeded, the adverse check refused as expected, and the evidence was preserved in the required repo locations.
