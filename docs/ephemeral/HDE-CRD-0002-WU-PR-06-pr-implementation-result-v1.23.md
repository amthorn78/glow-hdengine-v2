---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-06-PR-IMPLEMENTATION-RESULT
artifact_version: "1.23"
record_kind: PR-35 checkpoint for the twenty-third corrective push (non-terminal; no PR-35 result is returned with it)
phase: PR-35 (review resolution and merge readiness), plan cycle 1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.22.md (v1.22, PR-35 checkpoint; blob c4fa8f8f0bc7; 32,857 bytes; sha256 0485b69011391b709936fc6ed2ec6f46cdcb806b84a6956af8740dab7396b32b); v1.21 (blob 7a495445b837), v1.20 (blob 5df92bdae297), v1.19 (blob a694b81ce84a), v1.18 (blob b8ae075c826f), v1.17 (blob 78cc146ad6e9), v1.16 (blob 0d7b2026f6b4), v1.15 (blob 08cf62c76359), v1.14 (blob 456818eb3364), v1.13 (blob 6bce49444702), v1.12 (blob b8cba496e256), v1.11 (blob 0043d6495344), v1.10 (blob 7ba2d03ad6a5), v1.9 (blob cbaf9d77715f), v1.8 (blob 19bd19aae0f3), v1.7 (blob cce2ac485fa2), v1.6 (blob 1d2c326dc483), v1.5 (blob e4175f2a960d), v1.4 (blob 5b31c53c5309), v1.3 (blob 980eed838fd4), v1.2 (blob c0be05f3f13a), v1.1 (blob 8d103888fc24) and v1.0 (blob b506bff32c5c) of the same lineage. All preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob f3a6a8855ec0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md (v1.0; blob 2848847e8bee)
effective_baseline: unchanged from result v1.0 (approved base + PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9, 2.10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; unchanged on origin/main 0442d23). Provenance, not a gate
pf10_addendum_created: none
proceed: the original Proceed of result v1.0. No other Proceed exists or is needed
session: the dedicated HDE-CRD-0002 WU-PR-06 PR-35 session, https://claude.ai/code/session_01SVmct81WDzDqX36ZasAijn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e); primary skill glow-hde-pr-development 1.4.0; support skill glow-write-boundary
pull_request: amthorn78/glow-hdengine-v2#660 (https://github.com/amthorn78/glow-hdengine-v2/pull/660), branch claude/youthful-gauss-d9e0ab into main
commits_this_phase: 2894628, 7303b26, 302ab95, 76483d7, 11d4aa5, b7bc20b, c9d9196, be4000b, d9171d1, b5694ae, 1895e56, 574bbd4, 36d292b, 2d567a3, 0f4bb07, 78b5172, 89e0828, 2fa03de, 2c6dd5c, 3601f54, 14a5858, 7fc63d6, efff0bb, 9855694, 7a3b7b2, 55a973b, 161941f, d1a8969, 0783969, 0575fb0, ef06f44, 7be75ef, ba65334, bb52426, a7f1fdc, e4cda7d, a062ff7, d01599c, 153b67b, 5280748, 9fc2b10, 657c22b, fffd679, 30158af and e01a766, pushed; 7b9e95f3551bde15d2c41c465abe0696cd4e02aa (CX6-50; parent e01a766); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-20T09:55Z
next_step: push 7b9e95f and this record; answer the CX6-50 thread naming 7b9e95f and resolve it; move the safety-net check-in; read the Codex re-review and hosted CI of the new head over the active subscription; then the next record
---




# HDE-CRD-0002 WU-PR-06 — PR Implementation Result v1.23 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex re-review of `e01a766` raised two P2 findings, and I applied PO-35-5 to each (§2):
- **CX6-50 is fixed in `7b9e95f`.** It is a gap in the read-only check, of the same kind as CX6-46 and CX6-48.
- **CX6-49 is answered and resolved without a change.** It shows no wrong result on the real `ci.yml` or tree. It is the limit the Product Owner declined as CX6-12. It is neither a P1 nor a security finding, so no question to Nathan was needed.

The change is verified locally (§5). This record rides the same push. The Codex re-review of the new head, its hosted CI and the readiness decision follow in the next record.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Review matrix (cumulative)

| ID | Source | Head | Finding | Disposition |
| :- | :- | :- | :- | :- |
| CX6-1 to CX6-45 | Codex reviews 5571963225 to 5581255096 | `d2ed4fc` to `9fc2b10` | as results v1.1 to v1.21 | fixed, or CX6-12 declined by PO-35-1; threads resolved |
| CX6-46 to CX6-48 | Codex review 5581590543 | `fffd679` | as result v1.22 | fixed in `30158af`, or for CX6-47 addressed by the pin (result v1.22); replies r4323356125, r4323356710 and r4323356381; threads resolved |
| CX6-49 | Codex review 5583115082 (on `e01a766`), comment r4323386683, P2 | `e01a766` | `tools/ci/prepush_check.py` 1552: "When an unchanged workflow step invokes a repository script that starts consulting `GITHUB_WORKSPACE`, `GITHUB_REF`, `RUNNER_OS`, or another runner default, the workflow hash and direct `run:` scan do not detect that dependency"; "Populate the modeled runner defaults or otherwise fail closed for invoked code that depends on them" | **Not changed (PO-35-5).** Traced at `e01a766`: code the pinned workflow runs reads two runner variables directly, `GITHUB_OUTPUT` and `RUNNER_TEMP`, in `ci/checks/classify_ci_changes.py`, and the replay sets both. A `git grep` of the tree outside `docs/`, `audit/`, `artifacts/` and Markdown finds `GITHUB_WORKSPACE`, `GITHUB_REF`, `RUNNER_OS` and the other defaults only in the tool and its owner test, apart from `.audit_src/` and `.devcontainer/` files no step runs. The finding needs a future script change; the stated limit is CX6-12's (PO-35-1, IF-35-8), in the comment above `REPLAY_RUNNER_VARIABLES`. Reply r4323440277; thread resolved |
| CX6-50 | same review, comment r4323386670, P2 | `e01a766` | `tools/ci/prepush_check.py` 287–291: "For non-object Git metadata, this digest records only the path and bytes. If a report rewrites an existing file such as `.git/config`, `.git/index`, or a ref with identical bytes, its ctime changes but the before/after states remain equal"; "Record lstat identity for these entries too, not only files under `objects/`" | Confirmed at `e01a766`: in a scratch repository, rewriting `.git/config`, `.git/HEAD`, `.git/index` or a branch ref with its own bytes left `repository_state` equal. A gap in the read-only check, as CX6-46 and CX6-48 were, so fixed under PO-35-5, in `7b9e95f` (§3) |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3) | not applicable |
| — | Human review | — | none requested or present | — |

Product Owner decisions PO-35-1 to PO-35-5 are as results v1.7, v1.8 and v1.22 §2a; no new decision was needed.

## 3. Correction CX6-50 (`7b9e95f`)

Both paths are in plan §6.1. No path outside the change set moves (instruction ID-12 not engaged).

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` (blob `4dc098566620`; 1,755 lines; +7/−7 on `e01a766`) | `_metadata_digest` now enters every file and symlink under each git directory by its `lstat` identity (mode, size, `mtime_ns`, `ctime_ns`). Files outside `objects/` are also digested by their bytes, as before. Objects are still not read. Directories stay entered by name (IF-35-22). The docstring says so |
| `tests/tools/test_prepush_check.py` (blob `8d2c0be36e2e`; 1,070 lines; +5/−0) | `test_repository_state_covers_ignored_files` rewrites `.git/config` with its own bytes and checks that the metadata changes. 137 cases, as before |

## 4. CI on `e01a766`

Run 39399160507 (job 118549253003) on `e01a766` started at 09:13:57Z. The job completed on its own at 09:35:12Z with conclusion `success`, the redesign's first hosted run. Its final audit lists the changed tests and all seven lanes as selected with outcome `success`, and printed `CI_APPLICABILITY_AND_EXACT_HEAD_OK` at 09:35:10Z. It became stale at 09:17:52Z, when review 5583115082 posted CX6-49 and CX6-50. It was not waited on and is not a gate. Its result covers `e01a766` only, whose metadata digest `7b9e95f` changes.

## 5. Local validation of `7b9e95f`

**Environment and clones.** These are as result v1.22 §5. `cand`, `cand2` and `sweep` were moved to `7b9e95f` after `git clean -fdX`, each then clean with only its main worktree. Exit statuses are the producer's own.

**Scope.** The commit changes one function and one test, so the negative controls run are the six that guard the repository-state snapshot. The other 65 controls disable code this commit leaves unchanged; at `30158af` all of them failed as intended (result v1.22 §5 item 5).

| # | Check | Result |
| -: | :- | :- |
| 1 | Owner test (`cand2`) | 137 passed in 156.5 s, pytest exit 0. The session checkout's run before the commit: 137 passed in 116.8 s |
| 2 | Pin and neighbouring files (`cand2`), one at a time | `test_rails_ci_workflow_integration.py` 138, `test_http_reader_ci_ownership.py` 4, `test_architecture_snapshot.py` 5, `test_epic020_bundle_tool.py` 6 passed; each pytest exit 0 |
| 3 | Classifier `0442d23..7b9e95f`, `pull_request` | exit 0; `reason=selected_lanes;paths=26;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets, the owner test and the close-pack test among them |
| 4 | `check_agents_md_citations.py`; `check_env_pins.sh`; `--help`; `lanes --base 0442d23…`; `lanes --path`; `membership --path` (two paths); `build-notes`; `sweep --no-run` at the head and at `a429c7c` | `AGENTS_MD_CITATIONS_OK`, exit 0. `[env-pins] OK: …`, exit 0. `--help` exit 0. `lanes` exit 0, eleven output records. `lanes --path` exit 0, `lanes=product`. `membership` exit 0, `not-member tools/ci/prepush_check.py`, `member engine/core/core.py`. `build-notes` exit 0, PF10 v13.6.1, sha256 `ca2d91c5…`. `sweep --no-run` at the head `uncovered=0`, exit 0. Each of these five reports ended `PASS` and "repository unchanged" under the new comparison. `sweep --no-run` at `a429c7c` gave `uncovered=135`, exit 1, as in result v1.15 |
| 5 | Negative controls NC-35, NC-40, NC-88, NC-91, NC-92 and NC-103, each in a fresh clone at `7b9e95f` (09:23:03Z to 09:32:11Z, two at a time) | All six fail as intended, each in `test_repository_state_covers_ignored_files` (1 failed, 136 passed), each clone clean afterwards. NC-35, NC-40, NC-88 and NC-91 fail as at `30158af`. NC-92 (objects by name and size only), retargeted to the rewritten line, fails at the object overwrite (test line 731). New NC-103 (other metadata by bytes only, the code before this fix) fails at the new `.git/config` case (test line 736) |
| 6 | The real `ci.yml`, install step and environment through the tool at `cand2` (integ5) | exit 0; output byte-identical to round 24's (result v1.22 §5 item 6) |
| 7 | Premises at `e01a766` (that head's tool, scratch only), and the fix | At `e01a766` each of the four same-byte rewrites of §2 left the state equal. At `7b9e95f` each changes it, and two snapshots with nothing between them stay equal. Rounds 15 to 24's premise scripts give their round-24 outputs, all of them |
| 8 | `replay --base 0442d23…` from `cand` | exit 0; 09:23:03Z to 09:51:45Z (concurrent with items 5 and 9). `workflow … sha256=d02021f3… (the modelled one)`; classify `reason=selected_lanes;paths=26`, all seven lanes; every one of the 16 steps SUCCESS. Changed tests 4,023 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails last pytest 138; evidence 130; qa 488; release 79, and the attestation built and verified from the replay's `RUNNER_TEMP`. `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; step time 1,716.4 s. `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`: a 29-minute run against a real checkout, ending with every git metadata file's identity unchanged. `cand` before and after, by the scratch digest of result v1.1 §5: `head=7b9e95f…`, `status_lines=0`, `git_metadata_digest=43b24ea708195c498ab966c4a35243678b97856eaa7eb1d10faf6841a302308f`, identical; no temporary directory left |
| 9 | Full `tests/` sweep (`sweep`), `XDG_STATE_HOME` an empty scratch directory, `PYTHONPATH` the clone, `-p no:cacheprovider` | **5,323 passed, 3 skipped, 2 xfailed, 0 failed**, 5 warnings, 1,529.7 s (09:23:03Z to 09:48:35Z, concurrent with items 5 and 8); pytest exit 0. `git diff --exit-code` exit 0, untracked status empty, no file under the scratch `XDG_STATE_HOME`; an ignored `.pytest_cache/` was present afterwards, as after earlier sweeps. The same counts as result v1.22's sweep; the skips, xfails and `datetime.utcnow()` warnings are the pre-existing ones |

Every clone ended with `git diff --exit-code` exit 0 and an empty untracked status.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 to IF-35-23 | as results v1.1 to v1.22 §6 | unchanged | as recorded there |
| IF-35-24 | Every git metadata file now enters the snapshot by its `lstat` identity, not only objects. Consequence: any process that writes a git metadata file in the checkout during a run fails the run's read-only check (exit 4), even when it writes the same bytes. An editor's `git status` that refreshes the index is one such write. Before, only a change in content was seen. The tool's own git commands write no metadata (`GIT_OPTIONAL_LOCKS=0`); §5 items 4 and 8 show every report ending "repository unchanged" under the new comparison | The tool's read-only claim covers the git metadata, and PO-35-5 treats a gap in that check as a fix. Plan §5.2's digest ("every file under the git dir and the common dir by content, plus names and sizes under `objects/`") now records every file's identity too | §5 items 1, 4, 5, 7, 8 |

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.22 §7)

| Time (UTC, 2026-10-20) | Action | Evidence |
| :- | :- | :- |
| 09:13:48 | push 22 of PR-35: `fffd679..e01a766` (`30158af`, the v1.22 record), fast-forward, no force | remote head `e01a766…`; v1.22 read back from the remote: blob `c4fa8f8f0bc7`, 32,857 bytes, sha256 equal to the local file |
| about 09:14 | replies naming `30158af`: r4323356125 (CX6-46), r4323356381 (CX6-48), r4323356710 (CX6-47); the three threads resolved | GitHub ids returned; "is now resolved", each |
| 09:14:27 | safety-net check-in `trig_013ukt2jQR92KGpkuENHQ76d` re-armed for 10:04Z, its text now naming PO-35-4 and PO-35-5 | it creates no session |
| from 09:13:57 | CI run 39399160507 on `e01a766`: stale | §4 |
| 09:14:09 to 09:17:52 | Codex code review on `e01a766`: review 5583115082, findings CX6-49 and CX6-50 | summary comment 6267808148: completed, `has_unresolved_findings: true` |
| about 09:20 | CX6-50 premise confirmed at `e01a766`; CX6-49 traced on the tree | §2 |
| 09:22:39 | local commit `7b9e95f` | §3 |
| 09:23:03 to 09:51:45 | local validation of `7b9e95f`, all passed | §5 |
| about 09:24 | reply r4323440277 to CX6-49 with the traced path and the stated limit; thread resolved (PO-35-5) | GitHub id returned; "is now resolved" |
| after this record | push 23 of PR-35: `7b9e95f` and the commit adding this record, fast-forward onto `e01a766`, no force | read back in the next record |
| next | answer the CX6-50 thread naming `7b9e95f` and resolve it; move the check-in; read the Codex re-review and hosted CI of the new head | next record |

No `[skip ci]` or other CI suppression is used. No CI run was retriggered or re-run. No merge, auto-merge or merge request.

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

As result v1.22 §8, with these changes:

| Item | Owner | State |
| :- | :- | :- |
| Codex re-review of the new head; hosted CI with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35, under PO-35-5 | pending |
| The changed-tests failure of result v1.13 §4 | PR-35 watches each new head's CI | did not recur on `161941f`, `0783969`, `ef06f44`, `ba65334`, `a7f1fdc`, `a062ff7`, `153b67b`, `9fc2b10`, `fffd679` or `e01a766` (results v1.14 to v1.23 §4); intermittent, mechanism not established |
| Runner defaults other than the modelled ones are not given to steps or to the scripts they call, and scripts are not scanned for them (CX6-12, CX6-49) | declined by PO-35-1; answered under PO-35-5; stated limit (IF-35-8) | recorded |
| Directories under `.git` are compared by name; a change to such a directory's mode alone is not seen. Every file under it is compared by `lstat` identity, and by content outside `objects/` (IF-35-22, IF-35-24) | stated limit | recorded |
| Concurrent git activity in the checkout during a run fails the read-only check (IF-35-24) | stated behaviour; WU-DOC-01's usage note (G-1) | recorded |

## 9. Session and model record

Nathan has not stated the model and setting for this session; none is recorded.

## Canon relied on

As result v1.22 "Canon relied on". This round's subjects are the git metadata snapshot and runner variables. I searched `docs/pfcanon/` on `main` at `0442d23` for `GITHUB_` and `RUNNER_` names, "runner default", "runner variable", "runner environment", "git metadata", `.git/config`, "lstat" and "ctime". Canon holds nothing on either subject. The hits concern another runner (PF10's S10 start command and the CX5-1 retry runner) and a historical Codespaces `.git/config` note (PF20). The governing text is plan v1.0 §5.2 ("The tool's own assertion") and §5.7, instruction v1.0 ID-2 and ID-8, and PO-35-1 and PO-35-5.

| Topic | Sources and sections |
| :- | :- |
| Phase authority, review chain, stale CI, merge boundary | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (all sections); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 |
| Review chain overlay | PF10-HDE-Build-Notes v13.6.1 addendum 2.3 (Rules 1 to 5) |
| Sweep tools | PF10-HDE-Build-Notes v13.6.1 addendum 2.2 ("WU-PR-06's sweep environment must provide ruby") |
| Tooling vs behavior; closed rails | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 and §2.2.6 |
| In-flight scope | instruction v1.0 ID-2, ID-8, ID-12, §8, §9.1, §14; plan v1.0 §5.2, §5.7, §6.1; PO-35-1, PO-35-4 and PO-35-5 (results v1.7 and v1.22 §2a) |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Code review guidelines" and "Code review scope"; "Truncation/retrieval-failure guardrail" and its corollary on exit statuses |

## Nonclaims

The tool's green is not CI's green and not QA; its output is not governed evidence. This record establishes no QA verdict, acceptance, Ops, deployment, PF09 movement, closure or merge readiness, and makes no canon edit.
