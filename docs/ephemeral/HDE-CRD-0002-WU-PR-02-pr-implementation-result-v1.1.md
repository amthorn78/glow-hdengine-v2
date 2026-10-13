---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.1.md
artifact_version: "1.1"
artifact_state: PR-35 CHECKPOINT (non-terminal; no PR-35 result is returned by this record)
phase: PR-35 (review resolution and merge readiness); this record is the checkpoint for PR-35's first corrective push
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; blob 5942994df870593c36d2a1ce0f2c77cfcd116d4e). Preserved unchanged; this v1.1 is its PR-35 successor in the same lineage
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d92f90b3389d56d498f12964a91a9)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5804a88bcf861f45ea24d8846288f)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope is open)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain), as planned by PR_IMPLEMENTATION_PLAN_ID v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112da05bbcc9fae7316f64d1657824ff; 50,181 bytes; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this PR-35 session, 432 lines to <eof>; unchanged on main 0cd7b84 and on the branch; active addenda 2.1 to 2.4)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (reviewer chain) and § 2.1 (TypeSafe reading)
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0 (Nathan's PR-30 invocation naming plan v1.0). PR-35 continues under it; no other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-02 PR-35 session, https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK; session_disposition NEW_DEDICATED (top-level session Nathan created); role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state as of 2026-10-12T02:30:15Z; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/intelligent-cannon-32u7tl; pull request amthorn78/glow-hdengine-v2#634 (open, not draft, base main 0cd7b84)
entry_head: 4d11089245e8c1730864fab24b04b1c2cd203929 (PR-30 result commit; parent c27c5e848b3c6587d73e385da5b1b39ec240b7bf, the implementation commit)
correction_commit: c0ca923a72057392981927d656d02ba5d675a142 ("fix(evidence): HDE-CRD-0002 WU-PR-02 — bind current-release labels to regenerated captures (S12)"; parent 4d11089; tree ce421669611f396d6c7fefe15294f14c497a320d, the exact tree every §4 check ran on)
checkpoint_commit: the commit that adds this file; its own identity is not written into itself
next_record: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.2.md (PR-35, written after the remote evidence below arrives)
created_at: 2026-10-13T18:55:00Z
---

# HDE-CRD-0002 WU-PR-02 — PR implementation result v1.1 (PR-35 checkpoint)

## 1. State

PR-35 checkpoint after the first corrective push. One Codex code-review finding (P1) on `c27c5e8` was substantive and in scope; it is corrected by `c0ca923`, locally validated (§4) and pushed together with this record. No PR-35 result is returned yet: hosted CI and the Codex code review on the pushed head are pending and arrive through this session's pull-request subscription. Nothing here merges, claims merge readiness, QA, acceptance or closure.

## 2. Entry recovery

| Check | Observation |
| :- | :- |
| PR #634 | open, not draft, base `main` `0cd7b84`, head `4d11089` (2 commits: `c27c5e8` implementation, `4d11089` result v1.0), `mergeable_state: unstable` while CI ran |
| Local checkout | branch `claude/intelligent-cannon-32u7tl` checked out from `origin` at `4d11089`; clean; no other worktree |
| WU-PR-02 artifacts | instruction v1.0 and plan v1.0 (+ prototype diff) on `main`; result v1.0 on the branch only |
| Base drift | `origin/main` is `0cd7b84`, the PR base; no commit after it |
| Subscription | `subscribe_pr_activity` for #634 confirmed that this session receives the pull request's events (2026-10-13, at entry) |
| Continuity (GCF-17) | same `WORK_UNIT_ID`, original Proceed, workspace, branch, pull request, instruction v1.0, plan v1.0, primary skill and lineage (result v1.0 → this v1.1) as PR-30 |

## 3. Review matrix

| # | Reviewer / location / head | Finding | Classification | Disposition | Evidence |
| :- | :- | :- | :- | :- | :- |
| CR-1 | Codex code review (chatgpt-codex-connector), review 5508104545, thread `PRRT_kwDOP103ks6sAH60` (comment 4262430575), `tools/evidence/update_evidence_index.py` L3855–3857, commit `c27c5e8` | P1 "Verify captures before relabeling them as current": the label was stamped from `catalog/manifest.json` on every listed path, so a manifest cut before the 23 producers rerun relabels captures whose bytes still describe the previous release, and the updater and Mirror validator then pass | Substantive, in scope. The approved interface IF-7 says "Rows for captures the current release **regenerates**" and acceptance (4) "Every Mirror row for a **regenerated** current-release capture"; HDE Schemas & Artifacts §6.2 binds the Index/Mirror row to "the owning capture's provenance" and says "Updating a current evidence ledger does not relabel a historical capture". Not material: no objective, acceptance criterion, protected boundary, dependency or other unit changes | Corrected by `c0ca923` (§5 ID-35-1). Thread reply and resolution follow the push | §4 rows 6–9 and the negative control |
| — | Codex review summary (issue comment 6152304678) | one row, Code Review, completed 2026-10-13T18:23:48Z on `c27c5e8`, trigger "PR opened" | — | read | — |
| — | Codex security review | — | not part of the chain (PF10 addendum 2.3, Rules 2 and 3) | not requested or waited on | — |

Formal reviews: 1 (Codex, COMMENTED, the CR-1 carrier). Review threads: 1 (CR-1). No other comment.

## 4. Local validation of `c0ca923`

Environment **E-CI**: `/usr/bin/python3.12 -m venv` in the session scratchpad, CPython 3.12.3, `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt` then `-e <checkout>` (setuptools 84.0.0); readiness `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version` → `pytest 8.4.2`. Rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `GH_TOKEN`, vendor, geocode and database variables unset. Every run that can write tracked files ran in a detached worktree of `c0ca923` (`PYTHONPATH` = worktree) or a clean clone, each ending with `git diff --exit-code` and an empty `git status --short --untracked-files=all`. The E-DEB rehearsal was not rerun: the correction does not touch `build_release_attestation.py` or `regenerate_identity_closure.py` (PR-30 result v1.0 §9 surface advice).

Run 2026-10-13T18:36:36Z–18:52:25Z, tested commit `c0ca923` (base `0cd7b84`).

| # | Check (plan §11 numbering) | Result |
| :- | :- | :- |
| 1 | `ci/checks/check_env_pins.sh`; `python3 ci/checks/check_agents_md_citations.py` | 0; 0 |
| 3 | Updater write twice in the worktree | 0, 0; `git diff --exit-code` 0, 0 untracked: the governed companions are byte-unchanged by the correction (every label already names the admitted release) |
| 4 | `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, `check_lf_endings.py`, `release_id_recompute.py --check-manifest-only` | all 0 |
| 5 | Classifier `--base 0cd7b84… --head c0ca923… --event-name pull_request` | exit 0; `lanes=evidence,release`; `product/compat/db/rails/qa=false`; `changed_tests=true`; `path_count=16`; the same five targets as PR-30 |
| 6 | Changed-test step (detached worktree, `PYTHONPATH` = worktree) | **198 passed**; `git diff --exit-code` 0; 0 untracked |
| 7 | Evidence lane as `ci.yml` runs it: the step-4 checks, then the six test files | checks 0; **129 passed** (621.1 s; 126 at `c27c5e8`, +3 net new cases) |
| 7b | `tests/config/test_config_artifacts.py`, `tests/evidence/test_engine_core_evidence.py` | **165 passed**; tree clean |
| 8 | Release-lane tests (`test_identity.py`, `test_release_attestation.py`, `test_release_manifest_content_binding.py`, `test_sanity_pipeline.py`) | **75 passed**; tree clean |
| 11 | qa lane, seven files (prudence; not selected by the classifier) | **488 passed**; tree clean |
| 9 | Release-lane build: clean clone at `c0ca923`, E-CI, `release_id_recompute.py --check-manifest-only` then `build_release_attestation.py --output <external empty> --require-clean`, then `--verify --require-clean` | 0, build 0, verify 0; `build.log` has no `build_backend_compat` line; `attestation.json` 28,163 bytes, SHA-256 `9dac45e5f10ca69c5e18f1f416b765afe78164ba61f126b19a8415dc7e641dae`, `source_commit c0ca923…`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| — | Narrow run before commit (S12 label and config-family selection) | 8 passed |

Negative control (the code Codex reviewed): the new test file at `c0ca923` run against PR-30's updater (`4d11089`, detached worktree), `-k "release or label or config_publication_lets or config_family_publication_converges"`: **4 failed** (`test_manifest_only_release_cut_stays_outside_the_evidence_graph`, `test_release_labels_follow_regenerated_captures_through_the_updater_alone`, `test_incoherent_capture_labels_are_refused_before_any_write`, `test_config_publication_lets_only_a_regenerated_capture_label_move`), 4 passed; with the correction, 8 passed. The adoption test passes on both, as intended (PR-30 also labelled unlabelled rows).

## 5. In-flight decisions

| ID | Decision | Why necessary to deliver the approved scope | Tested by (identity → outcome) |
| :- | :- | :- | :- |
| ID-35-1 | CR-1 correction in `tools/evidence/update_evidence_index.py`. Per listed path, the label is decided from the retained Index label and the `sha256` the Machine Mirror recorded at the last updater run: no label yet → the admitted release (initial adoption); label already equals the admitted release → kept; otherwise the admitted release's label only when the capture's current bytes differ from the recorded `sha256` (its owner regenerated it), else the prior label is kept. Rows of one path with different labels are refused, `CURRENT_RELEASE_LABEL_INCOHERENT:<path>`. An unreadable Mirror gives no regeneration evidence, so labels are kept. `_config_logical_delta` compares an existing row without its label only when that row's primary was regenerated by the config-family publication. Encoding (PD-4), roster (23 paths / 28 rows), strip points (PD-9) and every other behaviour are unchanged | IF-7 and acceptance (4) bind the label to captures the current release regenerates; PR-30's manifest-only derivation contradicted that and HDE Schemas & Artifacts §6.2. The config-delta change is needed because, under the correction, the two catalog logs and the four canonical-JSON logs take the new label during the config-family publication (Plan v1.1 §10 step 6) rather than at step 5; without it that publication would refuse with `CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT` | `test_manifest_only_release_cut_stays_outside_the_evidence_graph` (pass); `test_release_labels_follow_regenerated_captures_through_the_updater_alone` (pass); `test_unlabeled_capture_rows_take_the_admitted_release_on_adoption` (pass); `test_incoherent_capture_labels_are_refused_before_any_write` (pass); `test_config_publication_lets_only_a_regenerated_capture_label_move` (pass); negative control 4 failed against `4d11089`; governed companions byte-unchanged (§4 row 3) |
| ID-35-2 | PD-10 superseded in the test: `test_manifest_only_release_cut_stays_outside_the_evidence_graph` regains its original final assertions (`_checks` and an unchanged skeleton after the manifest-only cut) and adds an updater run that must leave the skeleton byte-unchanged and write no `release 1.0.1` label | Under ID-35-1 the original invariant holds again; keeping PD-10's "updater relabels every row" assertion would test the defect CR-1 names | same test (pass); fails against `4d11089` |
| ID-35-3 | `test_release_labels_follow_the_manifest_through_the_updater_alone` replaced by `test_release_labels_follow_regenerated_captures_through_the_updater_alone` | its premise (a release change alone relabels every row) is the CR-1 defect; D-1's "relabel rows through the updater alone" is kept: no constant is edited, and the updater relabels a capture once its owner regenerates it | the replacement (pass) |

Effect on downstream units (D-1, Plan v1.1 §10): unchanged procedure. At step 5 the updater relabels the captures already regenerated (the canonical JSON gate at step 4); the config family (step 6) and the producers (step 7) regenerate the rest, and the step-8 updater relabels them. A capture left byte-stable across a `release_id` change keeps the previous label, which the step-11 stale-binding sweep finds in the Mirror; D-1 already routes that case to the IA as a finding.

Residual (recorded, not built for): a capture regenerated under the previous release with no updater run between that regeneration and the manifest cut would be read as regenerated. Plan v1.1 §10 runs the updater after every producer and restarts at step 5 on any evidence-primary change; proving release identity from every capture's bytes would need per-family knowledge of 14 captures that carry the release only through derived digests, which the work unit does not own.

## 6. PR_REMOTE_ACTION_LEDGER (PR-35)

| Time (UTC) | Action | Fact |
| :- | :- | :- |
| 2026-10-13 ~18:26 | PR read; subscription | #634 open, head `4d11089`, `mergeable_state: unstable`; subscription confirmed |
| ~18:26 | Review reads: reviews, threads, issue comments, check runs | 1 review (Codex, on `c27c5e8`), 1 thread (CR-1), 1 issue comment (Codex summary); check `test` in progress on `4d11089` |
| ~18:28–18:33 | Correction and narrow tests | 8 passed (S12 label and config-family selection) |
| ~18:34 | Negative control | 4 failed against `4d11089`, as intended |
| 18:35:48 | Commit `c0ca923` (local) | 2 files: updater +75/−5, test +91/−25 |
| 18:36:36–18:52:25 | Local validation | §4, all 0 / passed |
| ~18:39 | Hosted CI read | run 38446041858 (job 115465311140) on `4d11089`: success 18:22:50Z–18:34:58Z; EVIDENCE and RELEASE success, other lanes skipped, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Stale: its candidate carries CR-1; not a gate. It completed before the correction was pushed, so nothing was cancelled |
| after this record's commit | Push 1 (PR-35) | `c0ca923` and this record, one push; result read back in v1.2 |
| after push | Thread reply and resolution for CR-1; PR description update | recorded in v1.2 |

**Remaining useful local action:** none. **Next evidence action:** hosted CI (`test`, lanes `evidence,release`, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and the Codex code review on the pushed head, received through the subscription; then v1.2.

## 7. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Hosted CI and Codex code review on the pushed head | this PR-35 session |
| PD-10 and PD-11 were flagged to Nathan with the plan. PD-10 is superseded by ID-35-2 (the original invariant is restored); PD-11 (catalog-log rows compared without the label) stands | Nathan / IA (PR-40) |
| Residual ordering case of §5 | recorded for the IA (PR-40) |
| OBS-W2-1, OBS-W2-2 (doc-delta candidates), OBS-W2-3 (other ambient probes) | plan §17 owners |
| OBS-17 (qa lane, `tests/qa/test_generate_epic_close_pack.py`) | QA tool and test owner through the IA |
| Prompt-use provenance writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent | pending, non-gating |

## Canon relied on

Read on `main` at `0cd7b84` (the branch changes no file under `docs/pfcanon/`):
- **PR-35 authority and review chain:** PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (read in full); PF10-HDE-Build-Notes v13.5.5 (read in full) addendum 2.3 Rules 1 to 4 and "Passages read under this rule" (only the Codex code review is read and resolved); addendum 2.1 (TypeSafe reading, for v1.2); PR instruction v1.0 §12 and §14; plan v1.0 §16 and §19; HDE Governance §9.1.1 "Change authority and exact-artifact lineage" (read: the Product Owner's `PR Implementation Proceed` is the only runtime approval of the detailed per-PR plan; PR implementation and its PR lineage stay with the same dedicated PR session under the normal review and evidence chain; PR merges remain Product Owner actions).
- **CR-1 disposition and ID-35-1:** HDE Schemas & Artifacts §6.2 "Distinct source, capture, release, and evidence identities" (the Human Index / Machine Mirror row carries "the owning capture's provenance; not another release-identity authority"; "Updating a current evidence ledger does not relabel a historical capture"); §6.2.1, the paragraph beginning "Checked-in release evidence remains historical capture evidence" (configuration evidence does not acquire release IDs "merely because a release is cut"); §6.3 and §6.4 (read in full, unchanged reading); §8.3 "Allowed top-level keys and unknown-key rejection" (`notes` is free-form, names-only commentary; the encoding stays inside it). In-flight: Implementation Plan v1.1 §5 IF-7, §7 WU-PR-02 acceptance (4), §10 re-cut procedure; PR instruction v1.0 §4 (IF-7, ID-1) and §8 D-1.
- **Operative documentation:** `AGENTS.md` (sole Index/Mirror writer; no hand edits; closed rails; pytest readiness; PR descriptions; evidence attribution; Codex review scope excludes Markdown and `docs/ephemeral/`).

## Nonclaims

No merge readiness, QA evidence, QA verdict, acceptance, PF09/PF30 movement, deployment, canon change or closure. Local green is not hosted CI; CI green is not QA.
