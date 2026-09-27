---
artifact_type: OPS_TASK
artifact_id: HDE-EPIC040-OPS01-OPS-TASK
artifact_version: "1.3"
predecessor: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.2.md
template: PF27 — Canon Plan Templates v2.0.4, §3 Ops Task Record (Template)
task_state: READY
execution_state: NOT_EXECUTED
change_class: EPIC
change_id: HDE-EPIC040
capture_time_utc: 2026-09-27T04:30:00Z
---

# HDE-EPIC040-OPS01 — Ops Task Record v1.3 (supplemental adverse checks)

This is task v1.2 restated in the PF27 §3 Ops Task Record template. Its scope is unchanged. It supersedes v1.1 and v1.2 as the executable record. It has not been executed.

## Ops Task record fields

| Field | Value |
| --- | --- |
| **Task ID** | `HDE-EPIC040-OPS01` |
| **Owner** | `PO` |
| **Facilitator** | `IA` (HDE-EPIC040-2, successor retained whole-change IA) |
| **Executor** | `PO` or `PO-delegated automated session agent` |
| **PO delegation record, when delegated** | A secret-free reference to Nathan's direct instruction. It names Task ID `HDE-EPIC040-OPS01`, this record (v1.3), the objective (A-5, A-6 and A-7 adverse checks), the target (clean `main`) and the approved scope (this record only; no merge). Not required when the PO executes personally |
| **Task-specific authorization identity and dispatch-boundary validity** | Not required. There is no credential, token or time-bound authorization. STOP CHECK before dispatch: preflight rows P-1 to P-5 pass |
| **Objective blocker and resume posture** | No blocker. The previous STOP (result v1.3) was an instruction defect: the repository package was not installed (receipt v1.1). Preserved: the attestation accepted in receipt v1.0, A-1 to A-4, and the attempt 1, 2 and 4 logs. Resume: execute this record |
| **PF07 posture** | `PF07-derived`: HD Engine repository (PF07 §5.1); local shell or Codespaces (PF07 §2.8) |
| **Infra/ops fact inventory** | Provider, project, service, base URL, port, database, and config key or value: **not applicable** (no external system is contacted). Target repository: `amthorn78/glow-hdengine-v2`, `main` at `5cf3189` or later. Governed evidence root: `audit/ops/hde-epic040/ops01/` |
| **PF07 gap statement** | None. No hosted-service fact is required |
| **External execution classification** | `not applicable`: local, closed-rails, source read-only verification |
| **Exact command proof** | See the controlled execution contract below |
| **Input identity boundary** | No app user IDs, no `person_uid`, no `user_id`, no chart data |
| **Secret persistence posture** | `not applicable`. No secret is used. `HD_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `GEO_API_KEY` and `DATABASE_URL` are recorded as SET or UNSET only |
| **Non-claims preserved** | Delegation does not turn OPS into PR or QA work. No QA PASS, Live QA completion, acceptance-token satisfaction, PF09 status change, epic completion, deployment success or closeout |
| **Completion-claim boundary** | OPS01 is complete only when the repo-stored, secret-free evidence below meets the success criteria and OPS-30 accepts it |
| **Intent / desired end state** | Evidence that the release attestation tool refuses a tampered attestation (A-5), tampered bundle evidence (A-6) and a committed change to a release member (A-7). Together with the attestation already accepted and A-1 to A-4, this satisfies Plan v2.1 §6.8 |
| **Constraints / safety rails** | Closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`, which the script pins). The candidate tree stays clean and HEAD unchanged. Nothing is written inside the repository before the script exits. Tampering happens only in disposable copies |
| **Success criteria** | The script exits 0 and prints `RESULT: PASS (A-5, A-6, A-7 refused as required)`. A-5 and A-6 refuse with an `attestation_*` code. A-7 refuses with any code other than `source_tree_not_clean`. The post-check passes |
| **Closure dimension** | Supports Plan v2.1 §6.8 (OPS01 external verification) only |
| **Closure mode** | `direct runtime validation` of the release tooling's refusal behaviour |
| **Unchanged runtime facts already evidenced** | Not applicable |
| **Governed evidence family to normalize** | Not applicable. The evidence is not promoted into the Index or Mirror, so no path proofs are produced (a stated non-claim) |
| **Superseded contradictory artifacts** | Result v1.2's claim of completion, rejected by receipt v1.0. Result v1.3 is a STOP; its cause is recorded in receipt v1.1 |
| **Evidence to capture** | See required evidence outputs below |
| **Rollback intent** | Delete the `/tmp` work directory. There is no repository state to revert |
| **Secret handling note** | No plaintext secrets in any document or evidence |
| **Canon-grounded instructions** | PF12 owns the attestation tool `tools/evidence/build_release_attestation.py` and its refusal codes. PF10 — HDE Build Notes (release-attestation posture) sets the external empty output and the source-clean requirement. `regenerate_identity_closure.py` refuses to run on the source tree and must not be invoked directly |

## Controlled execution contract

| Item | Value |
| --- | --- |
| **Command source** | `docs/ephemeral/HDE-EPIC040-OPS01-supplemental-run-v1.1.sh`, SHA-256 `8a6e0af8fee7d6f3d34916fef6efd7458cdb11020151a2ff4a875813fe7d361c`, 4,618 bytes |
| **Command substitution source** | `P0_FILE`: the path of a non-empty file holding the delegation record, or the statement that the PO executes personally. No other substitution |
| **Executable command artifact** | The script file above, used unedited |
| **Placeholder rule** | The only placeholder is `P0_FILE`. If it is missing or empty, the script STOPs (exit 3) |
| **Target classification** | `not applicable` (local, closed rails) |
| **Required target facts** | Command target: the repository root of a clean `main` checkout. Data source: tracked files only. Execution context: Python 3.11 with `requirements.txt`, `requirements-dev.txt` and the repository package installed (`pip install -e .`). Config keys: none. Deterministic pins and rails: pinned by the script |
| **Target facts not required** | All hosted-service, vendor and database facts. Nothing external is contacted |
| **Target-change rule** | Any change of target or classification returns the task to the IA (OPS-10) before execution |
| **Prerequisite proof** | Accepted attestation `audit/ops/hde-epic040/ops01/attestation.json` (receipt v1.0 §3); `audit/ops/hde-epic040/ops01/ops01_execution_log.attempt4.md` present on `main` (#524) |
| **Execution wrapper** | `P0_FILE=<file> bash <copy of the script>`, run from the repository root once preflight passes |
| **Run rules** | No edits to the script. One retry, and only for an environment failure before the tool body runs. A failure inside the tool is final. No guessed substitutions, no forced PASS, no out-of-scope agent action, no direct run of `regenerate_identity_closure.py`, no merge |
| **Outcome classification map** | **PASS:** exit 0 with the success criteria met. **FAIL_BEHAVIOR:** exit 2, meaning an adverse check did not refuse as required. **FAIL_TOOLING:** the tool crashes for a reason unrelated to candidate behaviour. **TOOLING_BLOCKED:** a preflight row fails. Exit 3 (STOP) is reported as `TOOLING_BLOCKED` with the script's reason |
| **Non-claims** | No QA PASS, Live QA completion, final acceptance, public-surface change, CLI flag change, PF09 status change, epic closure or PF-canon drain completion |

### Preflight matrix

| ID | Requirement | Required proof | Status rule |
| --- | --- | --- | --- |
| P-1 | Candidate is `main` at `5cf3189` or later | Full HEAD SHA | Otherwise `TOOLING_BLOCKED` |
| P-2 | Clean tree | `git status --porcelain` prints nothing | Otherwise `TOOLING_BLOCKED` |
| P-3 | Environment includes the repository package | `import engine, jsonschema` succeeds when run outside the repository | Otherwise `TOOLING_BLOCKED` |
| P-4 | Script identity | SHA-256 equals the value above | Otherwise `TOOLING_BLOCKED` |
| P-5 | Delegation record, if delegated | A non-empty `P0_FILE` | Otherwise `TOOLING_BLOCKED` |

The script itself also checks candidate equivalence with `edbd414` outside the records paths, cleanliness, and `release_id_recompute.py --check-manifest-only`.

### Required evidence outputs

All three go under the governed root on one branch and in one PR, which is not merged:

| File | Required content |
| --- | --- |
| `audit/ops/hde-epic040/ops01/ops01_execution_log.attempt5.md` | The script's own log, copied byte for byte. The script names the file `…attempt4.md` in its work directory; the stored name is authoritative. It carries the P-0 record, candidate HEAD, key probe, preflight, fixture build and verify exits, the A-5, A-6 and A-7 exit codes, refusal codes and stderr tails, the post-check, and the result line |
| `audit/ops/hde-epic040/ops01/SHA256SUMS` | A checksum ledger over `attestation.json`, `attestation.json.sha256`, `build.log`, and the attempt 1, 2, 4 and 5 logs |
| `docs/ephemeral/HDE-EPIC040-OPS01-ops-execution-result-v1.4.md` | The outcome classification, script exit code and result line, the A-5, A-6 and A-7 codes, the P-3 proof, candidate HEAD, the delegation record or personal-execution statement, the evidence paths, and the non-claims |

## Evidence posture

- **Artifacts:** `audit/ops/hde-epic040/ops01/`.
- **QA root:** none; the task produces no QA evidence.
- **Path proofs:** none. The evidence is not promoted into acceptance, the close-pack or the Index/Mirror (non-claim).
- Attempt 3's log is `NOT_PRODUCED` ("written to /tmp and not retained") and is not reconstructed.

## Build Checklist tracking

Task ID `HDE-EPIC040-OPS01`. Plan v2.1 §6.8, unit 8 of 8. Dependencies: PR01–PR07, all `ACCEPTED_FINAL`. Status: READY. Receipt owner: this IA under OPS-30.

## Provenance

- **Prompt use:** `GCFPE-USE-HDE-EPIC040-OPS-10-20260927-OPS01-04`. That is OPS-10 — Create Bounded Ops Task — 091426.1. Repository persistence: `PENDING / NON_GATING`.
- **Next prompt:** OPS-20 — Execute Bounded Ops Task, on this record, then OPS-30 in this IA session.
