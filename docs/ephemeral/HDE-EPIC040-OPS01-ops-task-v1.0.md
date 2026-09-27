---
artifact_type: OPS_TASK
artifact_id: HDE-EPIC040-OPS01-OPS-TASK
artifact_version: "1.0"
task_state: READY
execution_state: NOT_EXECUTED
change_class: EPIC
change_id: HDE-EPIC040
ops_unit_id: HDE-EPIC040-OPS01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
creator: retained whole-change HDE-EPIC040 Implementation Architect (OPS-10); task-acceptance owner (OPS-30)
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-27T00:30:00Z
---

# HDE-EPIC040-OPS01 — Ops Task v1.0: final clean-candidate external verification

This task **has not been executed**. It creates the task only. It claims no operation, result or attestation.

## 1. Identity and lineage

| Field | Value |
| --- | --- |
| Task ID | `HDE-EPIC040-OPS01` |
| Owner / facilitator / executor | Owner: `PO` (Nathan). Facilitator: `IA`. Executor: the PO, or a PO-delegated automated session agent (PF27 §3) |
| IMMUTABLE_APPROVED_BASE | Implementation Plan v2.1: `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` (SHA-256 `10732f93…`), §6.8 |
| IMMUTABLE_APPROVED_BASE | Plan Review v2.1 (Isis-50 APPROVE): `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` |
| REMEDIATION_REVIEW_ID | none |
| CURRENT_PF10_MARKDOWN_LINK | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md` (SHA-256 `af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`) |
| ACTIVE_PF10_ADDENDA_LINKS | `docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` |
| Overlay scope | The PR06a addendum changed OPS01 in two ways: it now requires all PR units, including PR06a, and it verifies the re-cut release. The PR06b addendum set that release to `1.3.0`. The PR06-F01 addendum makes the attestation carry current identity alongside frozen captures that keep their capture-time identity; the attestation must claim nothing more about those captures. The §6.8 action boundary is otherwise unchanged |
| Dependency receipts | PR01–PR06, PR06a, PR06b and PR07 are all `ACCEPTED_FINAL`. The last review is `docs/ephemeral/HDE-EPIC040-PR07-pr-work-unit-lineage-review-v1.0.md` |
| Other PF sources read | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md` §3 (Ops Task Record); `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md` §§2.7–2.8, §5.1 |
| Receipt destination | The same creator IA, under OPS-30 — Review Ops Execution Receipt — 091426.1 |

## 2. Purpose and intent

Verify the final post-documentation candidate and produce the governed external release attestation without mutating the repository (Plan §6.8).

The task is done when a strict `hde.release_attestation.v1` bundle has been built and verified against the exact, clean candidate commit. That bundle must bind release `1.3.0` with 45 members, and the adverse cases in §6 must all refuse.

## 3. Target facts

| Fact | Value |
| --- | --- |
| PF07 posture | `PF07-derived` for the repository: the HD Engine repo (PF07 §5.1), in a local shell or Codespaces (PF07 §2.8). No hosted-service, Railway, database, vendor or DNS fact is required, because the task makes no external call |
| External execution classification | `not applicable`. This is local, closed-rails, source-read-only verification. It is not a CLI-local vendor smoke, a hosted-service operation or a vendor-backed smoke |
| Target repository | `amthorn78/glow-hdengine-v2`, branch `main` |
| Candidate | `origin/main` HEAD at execution time. It must be tree-equal to `edbd414`, the PR07 landing, apart from `docs/ephemeral/` (see P-2). No fixed acceptance SHA is invented; the executor records the actual commit |
| Expected release | `catalog/manifest.json`: version `1.3.0`, 45 files, `built_at_utc` `2026-08-24T18:04:49Z`, `release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` |
| Tool | `tools/evidence/build_release_attestation.py` (`--output <dir>` or `--verify <dir>`, plus `--source` and `--require-clean`) |
| Rails | `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`. The builder also pins `PIP_NO_INDEX=1` inside its isolated copy |
| Required config / credential keys | None. `HD_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `GEO_API_KEY` and `DATABASE_URL` must be unset; record them as SET/UNSET only |
| Input identity boundary | No app user IDs, no `person_uid` and no `user_id`. No chart data is supplied |
| Secret persistence posture | `presence-only`. No plaintext secrets anywhere |

## 4. Prerequisites and preflight

| ID | Requirement | Proof | Status rule |
| --- | --- | --- | --- |
| P-0 | Nathan's explicit, secret-free delegation of this exact Task ID to the executing session, given when OPS-20 is invoked | Quote the instruction verbatim in the result | Missing → `TOOLING_BLOCKED`; nothing is executed |
| P-1 | A fresh clone or fetch of `main`; Python with `requirements.txt` and `requirements-dev.txt` installed | `git rev-parse HEAD`; `python -m pytest --version` | Failure → `TOOLING_BLOCKED` |
| P-2 | The candidate equals the PR07 landing outside `docs/ephemeral/` | `git diff --stat edbd414 HEAD -- . ':!docs/ephemeral'` prints nothing | Any output → STOP; return to the IA (a candidate change, not a failure) |
| P-3 | Clean tree | `git status --porcelain` prints nothing | Otherwise → STOP; do not clean the candidate to pass |
| P-4 | Release identity at the source | `python scripts/release_id_recompute.py --check-manifest-only` exits 0; a manifest read shows `1.3.0` / 45 / the `release_id` in §3 | Mismatch → `FAIL_BEHAVIOR` |
| P-5 | Admission | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; print(type(l()).__name__)"` prints `AdmittedMechanicsBundle` | Otherwise → `FAIL_BEHAVIOR` |
| P-6 | External output directory | `OUT=$(mktemp -d)`, outside the clone, not a symlink, and empty | Otherwise → recreate it; never reuse a used directory |

## 5. Bounded operations (in order)

1. Run preflight P-0 to P-6 and record each result.
2. **Build:** `python tools/evidence/build_release_attestation.py --output "$OUT" --require-clean`. Capture stdout, stderr and the exit code. Expect exit 0, and stdout exactly `"$OUT/attestation.json"`.
3. **Verify:** `python tools/evidence/build_release_attestation.py --verify "$OUT" --require-clean`. Capture stdout, stderr and the exit code. Expect exit 0.
4. **Read the payload.** In `"$OUT/attestation.json"`, confirm and record:
   - `schema` = `hde.release_attestation.v1`;
   - `source_commit` = the candidate commit, and `source_commit_exact` = true;
   - `release_id` as in §3;
   - `validation_result` = `PASS`;
   - `release_admission` = `PR06R_B_FINAL_PASS`;
   - `pipeline_stop` = null;
   - the `nonclaims` list;
   - the counts of `files` and `omitted_files`.

   Also confirm that `"$OUT/failure.json"` does not exist.
5. **Post-check:** the source clone's `git status --porcelain` is still empty, and HEAD is unchanged.
6. **Adverse checks** (§6). Run them only against disposable copies, never against the candidate clone.
7. **Evidence storage** (§8). This happens after steps 1–6. It is a separate evidence-storage commit and is never part of the verified candidate.

## 6. Adverse checks (each must refuse; none may yield success)

Run each one in a disposable directory, never in the candidate clone. Record the command, the exit code and the stderr code for each.

| ID | Setup | Expected |
| --- | --- | --- |
| A-1 Dirty candidate | Throwaway clone, plus one untracked file | `--output` exit 1, `RELEASE_ATTESTATION_FAILED:source_tree_not_clean` |
| A-2 Output inside repo | `--output <clone>/tmp-out` | exit 1, `output_root_must_be_outside_source` |
| A-3 Non-empty output | An external directory containing one file | exit 1, `output_root_not_empty` |
| A-4 Symlink output | An external symlink to an empty directory | exit 1, `output_root_symlink_refused` |
| A-5 Tampered attestation | Copy of `$OUT` with one byte changed in `attestation.json` | `--verify` exit 1, with an `attestation_*` refusal code |
| A-6 Tampered evidence | Copy of `$OUT` with one byte changed in a file under `evidence/` | `--verify` exit 1, with an `attestation_*` refusal code |
| A-7 Missing or changed member | Throwaway clone: delete or alter one manifest member, commit locally (no push), then `--output` to a new empty directory | exit 1. Record the code; a release-not-admitted or sanity stop is expected |

A refusal code other than the one expected is not a failure, as long as the check refused. Record the code actually observed.

## 7. Allowed mutations and prohibitions

**Allowed:**
- creating the external `$OUT` and the disposable directories and clones, and deleting them afterwards;
- the §8 evidence commit on a working branch, with a PR that Nathan merges.

**Prohibited:**
- any change to the candidate clone or to `main`;
- merging, or enabling auto-merge;
- retrying after a failure with edited commands or a cleaned candidate, or forcing a PASS;
- any vendor call, database connection, deployment, activation, promotion, network access or production request;
- any PF-Canon edit;
- running `regenerate_identity_closure.py` directly;
- any Index/Mirror, path-proof or governed-evidence write;
- plaintext secrets.

**Retries:** one retry is allowed, and only for an infrastructure failure before the tool body runs (install or checkout). A second failure is final.

## 8. Evidence and destinations

Evidence goes to `audit/ops/hde-epic040/ops01/` (PF27 §3 evidence posture), secret-free. It is committed on a working branch in a separate PR:

| File | Content |
| --- | --- |
| `ops01_execution_log.md` | P-0 delegation quote; executor and session; UTC times; candidate commit and tree; rails and SET/UNSET key probe; every command with its exit code, stdout and stderr; payload field readout (§5.4); post-check; A-1 to A-7 table; outcome classification |
| `attestation.json`, `attestation.json.sha256`, `build.log` | Copied byte-for-byte from `$OUT` |
| `SHA256SUMS` | `sha256sum` of the files above |

- The `evidence/` subtree of the bundle is **not** copied. The attestation binds each of its files by hash, and it is regenerable from the candidate.
- This evidence is not promoted into Index/Mirror, so no path proofs are written. State that as a nonclaim.
- If repository storage is unavailable, keep the full log in the OPS-20 result and mark storage pending.

## 9. Outcome classification

- **PASS:** P-0 to P-6 hold, §5 steps 2 to 5 behave as expected, and all of A-1 to A-7 refuse.
- **FAIL_BEHAVIOR:** the build or verify fails on the clean candidate; any payload field differs from §3/§5.4; the source is mutated; or an adverse check yields success.
- **FAIL_TOOLING:** the tool crashes for a reason unrelated to candidate behaviour.
- **TOOLING_BLOCKED:** P-0 or P-1 is missing.
- **P-2 or P-3 STOP:** return to the IA and preserve the evidence.

## 10. Recovery and escalation

A failed build leaves `failure.json` in `$OUT`; preserve it and all logs. The candidate is never modified.

**Rollback:** delete the external and disposable directories. There is no repository state to revert.

**Escalation:** return to the creator IA through OPS-30 with the exact failure. A candidate defect goes to the IA under change control (ESC or RS routes) and is not fixed inside this task.

## 11. Non-claims

This task and its result do not claim any of the following:
- QA PASS, Live QA or acceptance-token satisfaction;
- PF09 movement;
- release activation, promotion or deployment;
- Epic closure;
- PF-Canon drainage;
- that the frozen historical captures were produced by release `1.3.0` (PR06-F01 condition 7).

`PR06R_B_FINAL_PASS` is a PF12-owned wire literal, not inherited acceptance. PO delegation does not turn OPS into PR or QA work.

**Completion claim:** OPS01 is complete only when OPS-30 has accepted the stored, secret-free evidence.

## 12. Register and carried items

`CANON_CONFLICT_REGISTER`: C040-01 to C040-08 are carried unchanged. OPS01 opens no entry.

Carried, non-gating:
- **O-12:** a packaged wheel install is not admitted. This task verifies the source-tree release only; the attestation installs its own packaged console entrypoint inside the isolated copy.
- O-P06a-22, O-P06a-03, O-P06a-23 and O-P06b-17 stay with their owners.

## 13. Provenance

- **Prompt use:** `GCFPE-USE-HDE-EPIC040-OPS-10-20260927-OPS01-01`. This is OPS-10 — Create Bounded Ops Task — 091426.1 (GCFPE-20260914.1), run by the whole-change IA. Repository persistence is `PENDING / NON_GATING`.
- **Prior art:** CI's release lane built and verified the same strict bundle on the PR #513 and #518 heads. That is supporting context only, not this task's evidence.

## 14. Recipient completeness

The executor can act from this file, the repository and P-0 alone. No unknown infrastructure fact remains. The single manual prerequisite is P-0, Nathan's delegation.
