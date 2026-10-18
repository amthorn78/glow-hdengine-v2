---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-05-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.1.md
artifact_version: "1.1"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review resolution and merge readiness), plan cycle 1; the checkpoint for PR-35's first corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; blob 20b170490447; 29,518 bytes; sha256 ab3e2367da9dca9180eaa1e036ab22854705a0a1f0208b052fe553aa79f013dc; read in full). Preserved unchanged; this v1.1 is its PR-35 successor in the same lineage
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0; Proceeded); companion docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0-prototype.diff
S19_RECORD: docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md (v1.0, RECORDED; blob 016e74e557ee; 52,542 bytes; unchanged by this phase)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; not edited)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.3, 2.5, 2.6, 2.7 (AD-4, AD-5), 2.8 and 2.9 as instruction v1.0 and plan v1.0 apply them (unchanged)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md (v13.6; the only PF10 file under docs/pfcanon/ on origin/main 8170cd8; blob f6f80d8779e8; 167,152 bytes; sha256 4ecdd9caf9dc172ecb07ab0c577b400ca7a96cc18cef4421448b99dd94fe28aa; docs/pfcanon/ last changed by 86e002c; the branch does not change docs/pfcanon/). Provenance, not a gate
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md §2.3 (review chain), §2.5 to §2.9 (carried), §2.1 (TypeSafe reading, at the final record)
pf10_addendum_created: none (PR-35 is not a qualifying approval prompt)
proceed: the original Product Owner Proceed recorded in result v1.0 (Nathan's PR-30 invocation naming plan v1.0). PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: the dedicated HDE-CRD-0002 WU-PR-05 PR-35 session, https://claude.ai/code/session_01UxcGLTM7Z2RFQLHeg8szTB; session_disposition NEW_DEDICATED (top-level session Nathan created from PR-30's handoff)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full at entry); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container; a fresh clone, not PR-30's container)
vehicle: branch ccr-ee766f88-s47rkh; pull request amthorn78/glow-hdengine-v2#656 (open, not draft, base main 8170cd8eb36b5e35adfab1fae9231bcd317d951c)
pr_subscription: active (subscribe_pr_activity confirmed delivery of #656 events to this session at entry)
entry_head: faf7b2b906c373890883d0cb453b807a126d8e38 (PR-30 result commit; ancestors 173bf97 S19 record, 176de33 convergence, d0f25b6 source)
correction_commit: ef3cda5447644642df373d13b281e5baba3e9cf8 (parent faf7b2b; tree 70191088eed8; the tree every §5 check ran on)
checkpoint_commit: the commit that adds this file, on top of ef3cda5; it changes only docs/ephemeral/; its own identity is not written into itself
release_id: 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (1.3.0, 45 members; unchanged by this phase: no member changes)
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.2.md (PR-35, written after the remote evidence of §7 arrives)
created_at: 2026-10-18T21:22Z
---

# HDE-CRD-0002 WU-PR-05 — PR Implementation Result v1.1 (PR-35 checkpoint)

## 1. State

**PR-35 checkpoint, non-terminal.** The Codex code review of [amthorn78/glow-hdengine-v2#656](https://github.com/amthorn78/glow-hdengine-v2/pull/656) raised one P2 finding, CX5-1: S19-F06's `None` log defaults stop the S9 ingest runner from writing its own logs. CX5-1 is corrected by `ef3cda5` and verified locally (§4, §5). This record rides the same push. The Codex re-review of the corrected head, its hosted CI, the thread resolution and the readiness decision follow in v1.2.

Nothing is merged. Nothing here claims merge readiness, QA, acceptance, Ops or closure.

## 2. Entry recovery

| Check | Observation |
| :- | :- |
| Pull request | #656 open, not draft, not merged; head `ccr-ee766f88-s47rkh` at `faf7b2b`; base `main` at `8170cd8` = `origin/main`; 4 commits (`d0f25b6`, `176de33`, `173bf97`, `faf7b2b`); 79 files (+1,436/−151); `mergeable_state: unstable` at entry (check running) |
| Local and remote | Fresh clone; one worktree on the session's default branch `ccr-6ad87aa6-4wk6oz` at `8170cd8` (no commits of its own; absent on the remote). The PR branch existed only on the remote; a tracking branch was created from it at `faf7b2b`, clean |
| Artifact lineage | result v1.0 (PR-30) on the branch, read in full; S19 record v1.0 (§§4, 7, 8, 10 read for F06 and X-03); plan v1.0 (P-3, P-11, P-15, §7.6, §8.1, PD-8, PD-13 read); instruction v1.0 (§5.5, §6, ID-9 to ID-11 read); no PR-35 record for WU-PR-05 existed |
| Tree identity | `git diff --name-only 176de33 faf7b2b` adds only the two records under `docs/ephemeral/`: the entry head's code tree is the one PR-30 validated |
| Earlier cycles | none: plan cycle 1 of WU-PR-05 |
| Subscription | active at entry for #656 |
| Repository skills | `.claude/skills/steward/` and `.claude/skills/babysit/` are absent on the head branch |

## 3. Review matrix

| ID | Source | Head | Location | Finding | Classification | Disposition |
| :- | :- | :- | :- | :- | :- | :- |
| CX5-1 | Codex code review (`chatgpt-codex-connector[bot]`), review 5564835342, thread `PRRT_kwDOP103ks6tuRXl` (comment r4308637602), P2 | `173bf97` (still applicable at `faf7b2b`; summary comment 6254839442 records the code review on `faf7b2b` as completed with `has_unresolved_findings: true`) | `engine/bodygraph/ingest.py` 138–139 | `scripts/ingest/run_vendor_ingest.py` deletes `SUCCESS_LOG` and `RETRY_LOG` on a fresh capture, then calls `ingest_vendor_bodygraph()` without either argument; with the new `None` defaults neither log is recreated, yet the runner writes its acceptance file and returns 0 with `ingest_success` and `retry_trace` false | Substantive in-scope correction. Verified: the runner is the only caller relying on the old defaults to write the S9 evidence; `artifacts/ingest/json_canon_compare.log` is untracked, so `_artifacts_exist` is false in a checkout and an operator's open-rails run reaches the fresh-capture path. The defect is introduced by this PR's S19-F06 | Fixed in `ef3cda5` (§4); thread reply and resolution after the push (§7) |
| — | Codex security review | — | — | not part of the review chain (PF10 addendum 2.3) | not applicable | none needed |
| — | Human review | — | — | none requested or present | — | — |

`scripts/bodygraph/run_refresh_worker.py` also calls `ingest_vendor_bodygraph(inputs, env=env)` with the defaults. It never reads or reports those logs; its old incidental writes to the tracked files are exactly what S19-F06 removes, so it is unchanged.

## 4. Correction CX5-1 (`ef3cda5`)

| Path | Change |
| :- | :- |
| `scripts/ingest/run_vendor_ingest.py` (not a release member) | the ingest call passes `retry_log=RETRY_LOG` and `success_log=SUCCESS_LOG` explicitly (2 lines). The acceptance and verify file lines do not move |
| `tests/bodygraph/test_ingest.py` | `test_s19_vendor_ingest_runner_passes_its_own_logs`: loads the runner, points every runner artifact path at `tmp_path`, wraps the real `ingest_vendor_bodygraph` with the module's `FakeClient` and `FakeDB`, and asserts both calls carry the runner's own log paths, the success log holds two lines and the summary reports `ingest_success` true. Negative control: with the runner change reverted it fails (1 failed) |
| `ci/checks/classify_ci_changes.py` | one `_PRODUCT_TEST_OWNER_PATHS` entry, `"scripts/ingest/run_vendor_ingest.py": ("tests/bodygraph/test_ingest.py",)`, with a one-line comment. Without it the classifier refuses the change (`CI_CHANGE_CLASSIFIER_ERROR:CI_PRODUCT_OWNER_TEST_MISSING:scripts/ingest/run_vendor_ingest.py`, exit 2, observed on `33bdb9d`, the unpushed first form of this commit). `tests/bodygraph/test_ingest.py` is already the registered owner of `engine/bodygraph/ingest.py`, so `_registered_owner_test_paths()` and the full-validation targets are unchanged and no pin moves (instruction ID-11; §5 rails lane) |

No member, manifest, evidence primary, path proof, Index or Mirror row changes, so no refresh or re-convergence runs (instruction ID-9; plan §20). The F03 hook is untouched (RK-8). No test module is added (PD-13).

## 5. Local validation of `ef3cda5`

Closed rails throughout (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), with `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV` unset and `XDG_STATE_HOME` an empty scratch directory. CPython 3.12.3 venvs with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .` of the worktree under test); pytest 8.4.2; `ruby` at `/usr/local/bin/ruby`.

| Check | Where | Result |
| :- | :- | :- |
| New test and negative control | branch tree | 1 passed; with the runner change stashed, 1 failed |
| Host module and the runner's other reader | branch tree | `tests/bodygraph/test_ingest.py` and `tests/evidence/test_env_matrix_snapshot_v3.py`: 29 passed |
| Classifier `8170cd8` → `ef3cda5` (`pull_request`, full SHAs) | detached worktree | exit 0; `reason=selected_lanes`; 81 paths; lanes product, compat, db, rails, evidence, qa and release (the classifier is a full-validation path); 166 changed-test targets |
| Classifier `faf7b2b` → `ef3cda5` | detached worktree | exit 0; 3 paths; all seven lanes; 165 targets |
| `check_agents_md_citations.py`; `check_env_pins.sh` | detached worktree | `AGENTS_MD_CITATIONS_OK`; env pins OK |
| Lanes, each step's `run` block extracted from `ci.yml` and run with `bash` in order, `RUNNER_TEMP` a scratch directory | detached worktree, own venv | changed tests 3,914 passed (isolated worktree, clean); product 77 passed; compat 119 passed, 3 skipped, 2 xfailed; db `DIRECT_DB_CONTRACT_OK`, 269 passed; rails `RAILS_GATE_EVIDENCE_OK` 155 passed, `RAILS_JOB_DEFINITIONS_OK`, 138 passed; evidence the seven checks exit 0, 130 passed; qa 488 passed (isolated worktree, clean; OBS-17 did not occur); release recompute exit 0, 79 passed in the isolated worktree, attestation build with `--require-clean` then `--verify`, both exit 0: `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `source_commit` `ef3cda5447644642df373d13b281e5baba3e9cf8`, `source_commit_exact` true, `release_id` `77204764…`. Every lane exit 0 (20:54:40Z to 21:19:02Z); clean tree afterwards |
| Full `tests/` sweep | second detached worktree, own venv | 5,186 passed, 3 skipped, 2 xfailed, 0 failed, 5 warnings (1,224 s; 20:54:09Z to 21:14:35Z), exit 0; clean tree; nothing under the scratch `XDG_STATE_HOME`. That is result v1.0's 5,185 plus the new case |

Not run: a re-convergence and the instruction §5.6 read-only family (no member or evidence byte changed; the evidence lane's `--check`s and the attestation cover the converged state); any live vendor, production or database call.

## 6. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | Tested |
| :- | :- | :- | :- |
| IF-35-1 | This phase's commits are pushed to the pull request's branch `ccr-ee766f88-s47rkh`, not to the session's default branch `ccr-6ad87aa6-4wk6oz` | The handoff continues #656; the work unit keeps one branch and one pull request (GCF-17 continuity). Same decision as WU-PR-04 result v1.1 IF-35-1 | remote head read back after the push (§7) |
| IF-35-2 | `scripts/ingest/run_vendor_ingest.py`, outside plan §8.1's paths, passes its own log paths | S19-F06 (plan §7.6) must stop incidental writes without breaking the owner that captures those logs; as delivered it made that owner report incomplete evidence as success. Two lines restore the owner and keep F06's default | `test_s19_vendor_ingest_runner_passes_its_own_logs` passed; negative control failed; full sweep and lanes (§5) |
| IF-35-3 | One classifier owner registration for that path | The classifier refuses any change to the unregistered path. Instruction §6 bounds `ci/checks/classify_ci_changes.py` to "the smallest registration a new path needs (ID-11)"; this is the smallest, it reuses an already-registered owner, and every pin stays true. PD-13's "no classifier change" concerned new test modules, of which there are none. WU-PR-04's lineage review records the same kind of change (two registry entries) as within ID-10 | classifier dry runs exit 0; rails lane (`test_rails_ci_workflow_integration.py`) and `test_http_reader_ci_ownership.py` in the full sweep pass |

Consequence for F-5 (instruction §8): WU-PR-06 now has one registration to read, IF-35-3's entry. Result v1.0 §9's "no registration added" is superseded by this row.

## 7. PR_REMOTE_ACTION_LEDGER (continuation of result v1.0 §12)

| Time (UTC) | Action | Evidence |
| :- | :- | :- |
| 20:4x | entry: #656 read; subscription confirmed; reviews, threads, summary comment and check runs read | head `faf7b2b`; one Codex review (5564835342, on `173bf97`); one open thread (CX5-1); summary comment: code review on `faf7b2b` completed, unresolved findings; security review null; check run `test` 117783823120 (run 39164247973) in progress on `faf7b2b` |
| after entry | run 39164247973 treated as stale: the head it tests is known to need CX5-1. Not cancelled (no supported cancellation interface in this session); the next push supersedes it under the workflow's `cancel-in-progress` rule for pull requests | not waited on and not a gate |
| 20:5x | local commit `33bdb9d` (runner fix and test); classifier refused it; amended locally, before any push, to `ef3cda5` with the registration | §4 |
| 20:54 to 21:19 | local validation of `ef3cda5` | §5 |
| after 21:22 | push 1 of PR-35: `ef3cda5` and the commit adding this record | remote head read back in v1.2 |
| next | reply on thread `PRRT_kwDOP103ks6tuRXl` naming `ef3cda5`, and resolve it; read the Codex re-review and the hosted CI run on the new head | v1.2 |

Remaining useful local action: none. Next evidence action: the Codex code review and hosted CI on the new head.

## 8. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Codex re-review of the new head; hosted CI with every selected lane and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; mergeability; thread resolution | PR-35 |
| S19-R01 to S19-R07 | Product Owner (unchanged) |
| O-01 to O-25, X-01 to X-04 | IA, or the owner each row names (unchanged) |
| IF-35-3's registration, for F-5 | WU-PR-06 reads it |
| Stale canon passages (result v1.0 §10) | Product Owner |
| Merge | Nathan / Product Owner (manual) |

## Canon relied on

Read on `origin/main` `8170cd8` (`docs/pfcanon/` last changed by `86e002c`; the branch does not change `docs/pfcanon/`).

| Topic | Sources |
| :- | :- |
| Phase authority, review-first execution, ledger, checkpoints, results | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (read in full); glow-hde-pr-development 1.4.0; HDE Governance §9.1.1 (as result v1.0 cites it) |
| Review chain | PF10-HDE-Build-Notes v13.6 addendum 2.3 (read in full): the Codex code review is read and resolved; the Codex security review is not part of the chain |
| Carried overlays and precedent | PF10 v13.6 addenda 2.5 to 2.9 as instruction v1.0 and plan v1.0 apply them; addendum 2.9 "Retained decisions and requirements" (classifier registry entries within ID-10 on WU-PR-04; OBS-17 and O-6 carried) |
| CX5-1 correction scope | instruction v1.0 §5.5, §6 (bounded files), ID-9, ID-10, ID-11; plan v1.0 P-3, P-15, §7.6, §8.1, PD-8, PD-13, §20; S19 record v1.0 §4 (S19-F06) and §8 (X-03) |
| Operative rules | `AGENTS.md` (closed rails, redaction, no hand edits of governed artifacts, pytest readiness, PR descriptions); `.github/workflows/ci.yml` (lanes, as run in §5) |

## Nonclaims

- No merge readiness is claimed: the corrected head's review and hosted CI have not been read.
- No QA verdict, acceptance, Ops, deployment, PF09 movement or closure is claimed.
- No fixed surface was run live, and no live vendor, production or database call was made.
- No canon was edited and no PF10 addendum was created. The routed findings are not decided.
