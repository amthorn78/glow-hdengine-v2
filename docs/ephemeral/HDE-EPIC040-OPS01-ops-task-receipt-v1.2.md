---
artifact_type: OPS_TASK_RECEIPT
artifact_id: HDE-EPIC040-OPS01-OPS-TASK-RECEIPT
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-receipt-v1.1.md
decision: ACCEPT
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
ops_task_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.3.md
ops_execution_result_ref: docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.4.md (PR #527, merged as 6cb410a8)
reviewer: HDE-EPIC040-2, successor retained whole-change HDE-EPIC040 Implementation Architect (task creator and acceptance owner), OPS-30
capture_time_utc: 2026-09-27T04:45:00Z
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_OPS-30
---

# HDE-EPIC040-OPS01 — Ops Task Receipt v1.2

## 1. Decision

**ACCEPT. HDE-EPIC040-OPS01 is complete.**

The evidence on `main` meets every success criterion in task v1.3:
- The strict release attestation for `1.3.0` was built and verified against the exact clean candidate (accepted in receipt v1.0 §3).
- Adverse checks A-1 to A-4 refused (receipt v1.0 §4).
- A-5, A-6 and A-7 refused as required in the supplemental run (result v1.4).

Receipt v1.0 §5 is satisfied.

## 2. Independent verification (read-only, at `main` `6cb410a8`)

| Check | Result |
| --- | --- |
| PR #527 scope | 3 files, all under `audit/ops/hde-epic040/ops01/` and `docs/ephemeral/`: the attempt 5 log, `SHA256SUMS` and result v1.4. Merged as `6cb410a8`. No other path touched |
| `sha256sum -c SHA256SUMS` | 7 of 7 OK: attestation, sidecar, build log, attempt 1, 2, 4 and 5 logs |
| Accepted attestation unchanged | `attestation.json` SHA-256 `9ffd1929…6dff` equals its sidecar. Last changed in `70f0e01` (the original storage) |
| Candidate | `6e4b3a10` (#526). No difference from the PR07 landing `edbd414` outside `docs/ephemeral/` and `audit/ops/hde-epic040/` |
| Script identity | SHA-256 `8a6e0af8…d361c` recorded by the executor and matching task v1.3 |
| Environment (P-3) | `env_ready` from `/tmp` after installing `requirements.txt`, `requirements-dev.txt` and `-e .`. The receipt v1.1 cause was addressed |
| Log content | Preflight P-2, P-3 and P-4 OK; keys UNSET; fixture build and verify exit 0 |
| A-5 tampered attestation | Exit 1, `attestation_contract_invalid`. Meets criterion (`attestation_*`) |
| A-6 tampered evidence (`artifacts/audit/ENDPOINTS_CATALOG.json`) | Exit 1, `attestation_file_binding_invalid`. Meets criterion |
| A-7 committed member change (`schemas/reader.v2.schema.json`, clean clone `9a553249`) | Exit 1, `isolated_stage_failed`, which is not `source_tree_not_clean`. Meets criterion |
| Post-check | `post_check=OK`. The candidate was unchanged |
| Secrets | None. One pattern hit was a false positive (the substring `sk-` inside "task-") |
| Consistency with the IA scratch rehearsal (receipt v1.1 §2) | Identical refusal codes and A-6 target file |

## 3. Criterion-by-criterion (task v1.3)

| Criterion | Disposition |
| --- | --- |
| P-1 candidate at or after `5cf3189`, P-2 clean tree | Met |
| P-3 repository package importable | Met |
| P-4 script identity | Met |
| P-5 delegation record | Met. It is recorded in the attempt 5 log and names the Task ID, the task record, the objective, the target and the no-merge scope (PF27 §3) |
| Success criteria (exit 0, three refusals, post-check) | Met |
| Required evidence outputs (3 files, one PR) | Met |
| Run rules | Met. One run, script unedited, nothing merged by the executor |

## 4. Plan v2.1 §6.8 expected evidence and adverse checks

| §6.8 item | Evidence |
| --- | --- |
| Source commit, clean state, manifest SHA and `release_id`, member tree, validation results, attestation files | Attestation (`source_commit_exact` true, `release_id` `52be4558…fe96`, `validation_result` PASS, `release_admission` `PR06R_B_FINAL_PASS`), receipt v1.0 §3 |
| Dirty candidate | A-1 |
| Output inside the repository, non-empty output, symlinked output | A-2, A-3, A-4 |
| Tampered attestation | A-5 |
| Hash-mismatched bytes | A-6 |
| Missing or changed member, partial release | A-7 |

## 5. Carried items

| ID | Item | Owner | Gating |
| --- | --- | --- | --- |
| O-OPS01-01 | The isolated closure's admission probe depends on the ambient installed package (receipt v1.1 §5) | Evidence-tool owner, through change control | No |
| O-OPS01-02 | Nathan is never asked to compose delegation text. Ops tasks use the PF27 §3 template | This IA; the owner of the OPS-10 and OPS-20 prompts | No |
| — | O-12, O-P06a-22, O-P06a-03, O-P06a-23, O-P06b-17, O-P07-01 to O-P07-09; drainage of C040-06, C040-07 and C040-08 | Unchanged owners | No |

## 6. Non-claims

OPS01 completion claims none of the following:
- QA PASS or Live QA;
- acceptance-token satisfaction;
- PF09 movement;
- release activation, promotion or deployment;
- PF-Canon drainage;
- epic closure;
- that the frozen historical captures were produced by `1.3.0`.

The evidence is not promoted into the Index/Mirror, so no path proofs exist. `CANON_CONFLICT_REGISTER` C040-01 to C040-08 are unchanged.

## 7. Provenance and next prompt

- **Prompt use:** `GCFPE-USE-HDE-EPIC040-OPS-30-20260927-OPS01-03`. That is OPS-30 — Review Ops Execution Receipt — 091426.1. Repository persistence: `PENDING / NON_GATING`.
- **Where the accepted receipt goes:** to the Plan-progress owner, this same whole-change IA (OPS-30 `accept_native_consumer`). With PR01–PR07 `ACCEPTED_FINAL` and OPS01 accepted, all eight Plan v2.1 units are complete.
- **Next prompt:** DOC-20 — Verify Final Repository Documentation Completion — 091426.1, in this same IA session, read-only. Its inputs:
  - `PR_INSTRUCTION_ID`: `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md`
  - `PR_WORK_UNIT_LINEAGE_REVIEW_ID`: `docs/ephemeral/HDE-EPIC040-PR07-pr-work-unit-lineage-review-v1.0.md`
  - `DOCUMENTATION_UNIT_ID`: `HDE-EPIC040-PR07`
  - `PLAN_REVIEW_ID`: `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`
  - `REMEDIATION_REVIEW_ID`: none
- **After DOC-20:** on `COMPLETE`, it routes to QA-10 — Audit Implementation and Establish QA Readiness (Isis).
