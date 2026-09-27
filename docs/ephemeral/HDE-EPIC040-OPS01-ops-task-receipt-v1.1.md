---
artifact_type: OPS_TASK_RECEIPT
artifact_id: HDE-EPIC040-OPS01-OPS-TASK-RECEIPT
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-receipt-v1.0.md
decision: REJECT
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
ops_task_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.1.md
ops_execution_result_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.3.md (PR #524)
reviewer: HDE-EPIC040-2, successor retained whole-change HDE-EPIC040 Implementation Architect (task creator and acceptance owner), OPS-30
capture_time_utc: 2026-09-27T03:10:00Z
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_OPS-30
---

# HDE-EPIC040-OPS01 — Ops Task Receipt v1.1

## 1. Decision

**REJECT, with the corrective task ready** (`docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.2.md`).

- **What happened.** Result v1.3 is a correct STOP. The executor followed the task exactly. The fixture build failed in the isolated `closure_write_and_check` stage, so A-5, A-6 and A-7 never ran. Receipt v1.0 §5 is still unsatisfied.
- **The cause is an instruction defect, not a candidate or release defect.** Task v1.0 P-1 (carried into v1.1) told the executor to install `requirements.txt` and `requirements-dev.txt`. It left out the repository's own package (`pip install -e .`). CI (`.github/workflows/ci.yml`, install step) and the devcontainer (`.devcontainer/scripts/post-create.sh:12`) both install it. The executor's environment did not have it.
- **Why that breaks the build.** The first thing `tools/evidence/regenerate_identity_closure.py` does in `main()` is `release_not_admitted_observed()`. That function runs `from engine.config.registry_loader import …`. It is started as a script, so its import path holds `tools/evidence/` and not the repository root. The builder's child environment keeps only `PATH`, `TMPDIR` and the rails (`_clean_child_env`, `build_release_attestation.py:328`). So `engine` imports only when the package is installed in that Python. Without it: `ModuleNotFoundError: No module named 'engine'`, exit 1, `isolated_stage_failed`.
- **The attestation accepted in v1.0 stands.** It is unaffected.

## 2. Evidence (IA diagnosis, scratch only, not OPS evidence)

All of this ran outside the repository, in this reviewer's container, under closed rails. The candidate checkout stayed clean throughout. It is diagnosis for this receipt, not a substitute for the OPS-20 run.

| Step | Result |
| --- | --- |
| Builder at `24b8457` and at `6f53d82` (the commit whose attestation v1.0 accepted), fresh venv with the two requirements files only | Both fail identically: `isolated_stage_failed` at `closure_write_and_check`. The new commits did not cause it |
| The failing stage's stderr, captured by wrapping `subprocess.run` | `ModuleNotFoundError: No module named 'engine'`, raised from `release_not_admitted_observed` (`regenerate_identity_closure.py:387`) |
| Same venv plus `pip install --no-deps -e .`, builder `--output` and then `--verify` at `24b8457` | Both exit 0. `source_commit` `24b8457d6ec5…`; `validation_result` `PASS`; `release_admission` `PR06R_B_FINAL_PASS`; `release_id` `52be45584acb…`; 174 files, 14 omitted. The tree was clean afterward |
| Supplemental script v1.1 run unedited, in the same environment, with a P0 file that says "IA diagnostic rehearsal only" | Exit 0. A-5 refused with `attestation_contract_invalid`. A-6 refused with `attestation_file_binding_invalid` (file `./artifacts/audit/ENDPOINTS_CATALOG.json`). A-7 refused with `isolated_stage_failed` (tampered clone clean, head `3c363d4e`). Post-check passed |

The rehearsal shows that the script is correct and that the environment step is the only missing piece. It is not the task's evidence. That evidence must come from the delegated OPS-20 run of v1.2.

## 3. Criterion-by-criterion (result v1.3)

| Criterion | Disposition |
| --- | --- |
| P-0 | Met. The delegation is recorded in the attempt 4 log and in v1.3 |
| Script identity | Met. SHA-256 `8a6e0af8…d361c`, run unedited |
| Run 1 retry | Correctly used. A missing dependency before the tool body is the one retry v1.0 §7 allows |
| Run 2 stop | Correct. The script stopped at the failed fixture build, and the executor did not force a third run |
| Candidate unmodified | Met. HEAD `24b8457` and the tree are unchanged before and after both runs |
| A-5, A-6, A-7 | **Not met.** Not run |
| Evidence storage | Met for what ran: attempt 4 log, `SHA256SUMS`, result v1.3 (PR #524) |

## 4. Correction (OPS-10 → OPS-20)

Task v1.2 is v1.1 with one added step: set up the environment the way the repository does, `python -m pip install -r requirements.txt -r requirements-dev.txt -e .`. It runs before the script, and there is a readiness probe that `engine` imports. The script and its hash are unchanged. Receipt v1.0 §5 is otherwise unchanged.

## 5. Carried items

| ID | Item | Owner | Gating |
| --- | --- | --- | --- |
| O-OPS01-01 | The isolated closure's admission probe imports `engine` from the ambient installed package, not from the isolated copy. An editable install points at the source clone. The exact-copy check keeps the bytes equal on a clean candidate, but the stage is not self-contained, and it fails with an unrecorded traceback when the package is absent | Evidence-tool owner, through change control | No. OPS01 runs in the repository's standard environment |
| O-OPS01-02 | Product Owner direction (2026-09-27): Nathan must never have to compose delegation text. Every Ops handoff carries the delegation line pre-written for him to paste. Recording it word for word is the executor's job. PF27 §3 still requires the explicit delegation itself | This IA for its own Ops tasks. For the OPS-10 and OPS-20 prompt bodies, the prompt-ecosystem owner | No |
| — | O-12, O-P06a-22, O-P06a-03, O-P06a-23, O-P06b-17 | Unchanged owners | No |

## 6. Residual state and non-claims

- PR #524 (result v1.3 evidence) is open and should be merged as the record of attempt 4. Merging it preserves the record and approves nothing.
- No QA, acceptance, PF09 movement, deployment, activation or closure is claimed.
- `CANON_CONFLICT_REGISTER` C040-01 to C040-08 are unchanged.

## 7. Provenance and next prompt

- `GCFPE-USE-HDE-EPIC040-OPS-30-20260927-OPS01-02`: OPS-30 — Review Ops Execution Receipt — 091426.1. The same use also authored task v1.2 as OPS-10 (`GCFPE-USE-HDE-EPIC040-OPS-10-20260927-OPS01-03`). Repository persistence is `PENDING / NON_GATING`.
- **Next prompt:** OPS-20 — Execute Bounded Ops Task, on task v1.2, in the existing executor session, under Nathan's pasted delegation. Its result returns to OPS-30 in this IA session.
