---
artifact_type: OPS_TASK_RECEIPT
artifact_id: HDE-EPIC040-OPS01-OPS-TASK-RECEIPT
artifact_version: "1.0"
decision: REJECT
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
ops_task_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md
ops_execution_result_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.2.md
reviewer: retained whole-change HDE-EPIC040 Implementation Architect (task creator and acceptance owner), OPS-30
capture_time_utc: 2026-09-27T01:40:00Z
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_OPS-30
---

# HDE-EPIC040-OPS01 — Ops Task Receipt v1.0

## 1. Decision

**REJECT.** The rejection is narrow, and the core result is sound.

- **What stands:** the strict attestation built and verified against the exact clean candidate, and I confirmed that independently (§3).
- **Why it is rejected:** the task's success criterion requires every adverse check A-1 to A-7 to refuse. For the valid run, three of those checks are not evidenced:
  - A-5 and A-6 were never actually exercised.
  - A-7 refused for the wrong reason.
- **Missing log:** the valid run's own execution log was not stored.

The correction is bounded (§5). Acceptance of the attestation itself is not in dispute.

## 2. Lineage

**Inputs**
- Task: `docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md`, landed via #520.
- Results: v1.0 (attempt 1, BLOCKED), v1.1 (attempt 2, FAIL_BEHAVIOR, later reclassified FAIL_TOOLING) and v1.2 (attempt 3, COMPLETE), all under `docs/ephemeral/`.

**Where the evidence landed on `main`**
- `70f0e01` was merged by merge commit `177aa40` (branch `ops/hde-epic040-ops01`, PR #521).
- It holds `audit/ops/hde-epic040/ops01/{attestation.json, attestation.json.sha256, build.log, ops01_execution_log.attempt1.md, ops01_execution_log.attempt2.md}`.

**Governing sources**
- Bases: Plan v2.1 §6.8 and Plan Review v2.1.
- PF10: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md`.
- Overlays: the PR06-F01, PR06a and PR06b addenda under `docs/ephemeral/`.
- PF27 §3; PF07 §§2.8, 5.1.

**Delegation.** The P-0 delegation is recorded verbatim in the attempt 2 log and in result v1.2.

## 3. Independent verification (read-only)

| Check | Result |
| --- | --- |
| Candidate `6f53d82` versus the PR07 landing `edbd414` outside `docs/ephemeral/` | No difference. P-2 holds |
| Stored `attestation.json` | Canonical bytes, schema-valid, and SHA-256 `9ffd1929…6dff` matches its sidecar |
| Payload | `hde.release_attestation.v1`; `source_commit` `6f53d82…`; `source_commit_exact` true; `release_id` = `manifest_sha256` = `52be4558…fe96`; `validation_result` PASS; `release_admission` `PR06R_B_FINAL_PASS`; `pipeline_stop` null; closed rails; 174 files; 14 omitted; five nonclaims |
| `source_tree_sha256` | I recomputed it with the tool's own digest over a clean worktree of `6f53d82` and got `60c80451…e1c1`, which **equals** the attested value. The bundle binds the exact candidate |
| `build.log` | All five isolated stages exit 0 |

## 4. Criterion-by-criterion

| Criterion | Disposition | Evidence |
| --- | --- | --- |
| P-0 delegation | Met | Verbatim in the attempt 2 log and in v1.2 |
| P-1 to P-6 preflight for the valid run | **Not evidenced** | v1.2 states that the tree was clean, but the attempt 3 log was not stored. Attempt 2's preflight shows a dirty tree it caused itself |
| Build and verify exit 0 on the clean candidate | Met | Stored attestation and §3. An earlier build in attempt 2's first call also exited 0 (reported in v1.2) |
| Payload fields (§5.4) | Met | §3 |
| Source unchanged after the run | Met by inference. The attestation's exact-source check passed; the post-check was not logged |
| A-1 dirty candidate | Met | Attempt 2 log: `source_tree_not_clean`, exit 1. This check does not depend on a bundle |
| A-2 output inside repo | Met | `output_root_must_be_outside_source` |
| A-3 non-empty output | Met | `output_root_not_empty` |
| A-4 symlink output | Met | `output_root_symlink_refused` |
| A-5 tampered attestation | **Not met** | Attempt 2 had no bundle (`FileNotFoundError`), and v1.2 does not report A-5 |
| A-6 tampered evidence | **Not met** | Attempt 2 had no bundle (`StopIteration`), and v1.2 does not report A-6 |
| A-7 changed member | **Not met** | Refused with `source_tree_not_clean`, which means the tampered-member path was never reached |
| Evidence set (§8) | Partial | Missing: the attempt 3 log and `SHA256SUMS` |
| Secrets | Met | No secret values in the stored evidence |

## 5. Bounded correction (to OPS-10, then OPS-20)

The correction is a supplemental run under the same P-0 delegation and the same candidate-cleanliness rules. It covers:

- a fresh build into an empty `/tmp` directory, used only as a fixture;
- A-5 and A-6 against copies of that bundle, which must refuse with an `attestation_*` code;
- A-7 in a throwaway clone whose tampered member is **committed**, confirmed clean with `git status --porcelain`, and built with `--source` into a new empty directory; it must refuse with a code other than `source_tree_not_clean`;
- a complete log of that run and `SHA256SUMS`, stored under `audit/ops/hde-epic040/ops01/` and committed after the run.

Nothing else is re-run. The accepted attestation above stays as the task's attestation.

## 6. Residual state and nonclaims

- **Residual state:** none on `main` beyond the stored evidence. The `/tmp` bundles are outside the repository.
- **Nonclaims:** no QA, acceptance, PF09 movement, deployment, activation or closure.
- **Register:** `CANON_CONFLICT_REGISTER` C040-01 to C040-08 are unchanged.

## 7. Provenance

`GCFPE-USE-HDE-EPIC040-OPS-30-20260927-OPS01-01`: OPS-30 — Review Ops Execution Receipt — 091426.1. Repository persistence is `PENDING / NON_GATING`.
