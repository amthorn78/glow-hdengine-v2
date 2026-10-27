---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; landed at b996a20, #632)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 91831e94c1c5804a88bcf861f45ea24d8846288f; landed at 0cd7b84, #633)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, approved)
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base + PF10 addendum 2.3 (PF10 v13.5.5, docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md, unchanged since the plan; read in full by this session)
proceed: Nathan / Product Owner, by pasting in this session the PR-30 invocation that names plan v1.0 at its repository path (2026-10-13, after #633 merged). PR-30 resolves an unambiguous reference to the presented plan directly; no other approval object exists or is required
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated WU-PR-02 PR engineering session (PR-20 and PR-30 phases), https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a; role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14); primary skill glow-hde-pr-development 1.4.0
repository_baseline: origin/main 0cd7b843462df94273bb686def5e4a353d0b98ba (b996a20 plus the two plan files under docs/ephemeral/ only)
branch: claude/intelligent-cannon-32u7tl (restarted from origin/main after #633 merged; it carried only merged history)
pull_request: amthorn78/glow-hdengine-v2#634 (open, base main)
implementation_commit: c27c5e848b3c6587d73e385da5b1b39ec240b7bf (the tested commit; remote head read back after push)
record_commit: the commit that adds this file, after c27c5e8; it changes only docs/ephemeral/
canon_conflict_register: CR-1 to CR-5 carried unchanged; no new entry
created_at: 2026-10-13T18:19:52Z
next_phase: PR-35 — Resolve PR Reviews and Reach Merge Readiness, in its own dedicated session
---

# HDE-CRD-0002 WU-PR-02 — PR Implementation Result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** The approved work unit is implemented exactly as plan v1.0 §5 to §8 specify, locally validated (§4), committed as one coherent commit `c27c5e8`, pushed, and published as [amthorn78/glow-hdengine-v2#634](https://github.com/amthorn78/glow-hdengine-v2/pull/634). PR-35 owns review retrieval and correction, current-head CI and merge readiness. Nothing here is merged, and nothing claims merge readiness, QA, acceptance or closure.

## 2. Recovery (C0)

| Check | Observation |
| :- | :- |
| Open pull requests | none (listed 2026-10-13 before work) |
| Local branches and worktrees | `claude/intelligent-cannon-32u7tl` only, clean, at `d30ebff` (the plan commit, squash-merged as `0cd7b84` by #633); one worktree |
| WU-PR-02 artifacts on `main` | instruction v1.0, plan v1.0 and its prototype diff; no earlier result |
| `git diff b996a20 origin/main` | the two plan files under `docs/ephemeral/` only; no §6 path, manifest or roster primary changed, so plan §4 facts hold |
| Action | branch restarted from `origin/main` (`git checkout -B`), keeping its name; the prior remote head held only merged history and was replaced with `--force-with-lease` against `d30ebff` |

## 3. Implementation

Applied the plan's companion diff (`docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff`) to `0cd7b84`, then corrected the one difference plan §4.4 names: readable `ids=` on the two parametrized tests (`system-mod-present`, `patched-backend`, `unpatched-backend`, `no-setuptools`; `copy-refuses-ambient-admits`, `copy-admits-ambient-refuses`). Every hunk was re-read against plan §5; no other difference.

Governed regeneration: `python tools/evidence/update_evidence_index.py` twice (second run byte-stable). Changed companions: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256` and their four `.path_proof.txt` files; `audit/gates/topology/orientation_demo.txt` unchanged. 28 Mirror rows (23 paths) carry `current-release capture: release 1.3.0, release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.

`c27c5e8` changes exactly 15 paths: the four tools/validator files, the three test files and the eight governed companions (`git diff --numstat`: builder +54/−1, closure +29/−4, updater +135/−28, validator +5/−0, tests +193/−0 (attestation), +48/−0 (engine core), +217/−5 (evidence index)).

## 4. Local validation (plan §11)

Environments: **E-CI** `/usr/bin/python3.12 -m venv`, CPython 3.12.3, `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <checkout>` (setuptools 84.0.0, pytest 8.4.2; `python -m pip install -r requirements-dev.txt` then `python -m pytest --version` → `pytest 8.4.2`); in this venv `_distutils_system_mod` resolves to `/usr/lib/python3.12/_distutils_system_mod.py`, so the compat is not applied. **E-DEB** `/usr/bin/python3 -m venv --system-site-packages`, CPython 3.13.16, setuptools 68.1.2 from `/usr/lib/python3/dist-packages` (Ubuntu `python3-setuptools` 68.1.2-2ubuntu1.2), repository requirements installed, no `-e .`, `_distutils_system_mod` and `engine` not importable. Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode, database and `GH_TOKEN` variables unset; attestation runs under `env -i`. Tested commit: `c27c5e8` (base `0cd7b84`). Run 2026-10-13T17:56:15Z–18:18:58Z.

| # | Check | Result |
| :- | :- | :- |
| 1 | `ci/checks/check_env_pins.sh`; `python3 ci/checks/check_agents_md_citations.py` | 0; 0 |
| 3 | Updater write twice | 0, 0; second run byte-stable |
| 4 | `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, `check_lf_endings.py`, `release_id_recompute.py --check-manifest-only` | all 0 |
| 5 | Classifier `--base 0cd7b84… --head c27c5e8… --event-name pull_request` | exit 0; `lanes=evidence,release`; `product/compat/db/rails/qa=false`; `changed_tests=true`; `path_count=15`; targets `tests/config/test_config_artifacts.py`, `tests/evidence/test_aux_preview_identity_parity.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_internal_version_manifest_captures.py` |
| 6 | Changed-test step (detached worktree, `PYTHONPATH` = worktree) | **198 passed**; `git diff --exit-code` 0; 0 untracked |
| 7 | Evidence lane: the step-4 checks, then the six `ci.yml` test files | checks 0; **126 passed** (776.9 s) |
| 8 | Release-lane tests (`test_identity.py`, `test_release_attestation.py`, `test_release_manifest_content_binding.py`, `test_sanity_pipeline.py`) | **75 passed** |
| 11 | qa lane, seven files (prudence; not selected by the classifier) | **488 passed** |
| — | Worktree after all lanes | `git diff --exit-code` 0; 0 untracked |
| 12 | S13 negative control: base probe restored in the worktree, `-k closure_probe` | **4 failed**, as intended; restored, clean |
| 2 / C2 | S06 before: clean clone at `0cd7b84`, E-DEB, `--output <external empty> --require-clean` | exit 1; `RELEASE_ATTESTATION_FAILED:isolated_package_install_failed`; receipt `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}`; clone clean |
| 10 | S06 after: clean clone at `c27c5e8`, E-DEB | build 0, `--verify --require-clean` 0; `build.log` has `build_backend_compat=distribution_install_layout`; `attestation.json` 28,163 bytes, SHA-256 `475cf4823f95bf30c2e7cd5ebe9001abf3bbaa70150f63721583d4199faa9ea6`, `source_commit c27c5e8…`, `release_id 52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, 174 files bound, 14 omitted; clone clean |
| 9 | Release-lane build: clean clone at `c27c5e8`, E-CI | build 0, verify 0; no compat line; SHA-256 `3d6e93b774f9a545d9de62e090ecee789e179414c0f04eaf2909a93a84dd9e19`; same identity and counts; clone clean |
| — | Focused files before commit (attestation, engine core, sanity, identity, manifest binding; S22/S12 fast cases) | 87 passed; 8 passed |

Acceptance (plan v1.1 §7 WU-PR-02) as locally evidenced: (1) before/after rows above (hosted release lane pending, PR-35); (2) `test_closure_probe_follows_the_isolated_copy_with_no_ambient_engine` and the negative control; (3) `test_core_evidence_release_check_fails_when_the_admitted_release_id_differs`; (4) the label tests and step-4 validators; (5) `test_crd_0002_fixture_root_publishes_beside_crd_0001`, `test_crd_publication_refuses_an_unadmitted_id_by_name`, `test_absent_admitted_crd_root_publishes_nothing`, `test_mirror_schema_accepts_crd_id_and_refuses_epic_and_crd_together`.

## 5. In-flight decisions

| Decision | Why necessary | Tested by |
| :- | :- | :- |
| Restart the designated branch from `origin/main` and replace its remote head with `--force-with-lease` | its only commit was the plan, already squash-merged by #633; a merged vehicle is never reused | read-back of remote head `c27c5e8` |
| Add readable `ids=` to the two parametrized tests | plan §8.1 and §8.2 require them; the prototype diff lacked them (plan §4.4) | evidence and release lanes above |

No other decision was taken; plan decisions PD-1 to PD-11 were implemented as written.

## 6. PR_REMOTE_ACTION_LEDGER

| Action | Fact |
| :- | :- |
| Local checks | §4, all on `c27c5e8` |
| Commits | `c27c5e8` (implementation); the record commit adding this file |
| Push 1 | `--force-with-lease=claude/intelligent-cannon-32u7tl:d30ebff`; `d30ebff...c27c5e8 (forced update)`; remote head read back `c27c5e848b3c6587d73e385da5b1b39ec240b7bf` |
| PR | #634 created (base `main`, head `claude/intelligent-cannon-32u7tl`), not draft |
| Push 2 | this record (docs/ephemeral only); supersedes CI on `c27c5e8` under the workflow's pull-request cancel-in-progress |
| Review reads | none yet (PR-35) |
| CI | none observed by PR-30; expected lanes `evidence,release` on the PR head |
| Mergeability | not read by PR-30 (PR-35) |
| Next evidence action | PR-35: Codex code review on the current head; hosted `test` job with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, including the release lane's attestation build and verify |

## 7. GCF-17 continuity (PR-30 and PR-35 share each value)

`WORK_UNIT_ID` WU-PR-02; original Proceed (front matter); workspace `/home/user/glow-hdengine-v2` in this cloud container (PR-35 recovers it from the branch if the container differs); branch `claude/intelligent-cannon-32u7tl`; pull request #634; PR instruction v1.0; detailed plan v1.0; primary skill glow-hde-pr-development; recovery lineage: plan v1.0 → this result v1.0.

## 8. Constraints and unresolved items

| Item | Owner |
| :- | :- |
| Codex code review findings on #634 (none read yet); no Codex security review (PF10 addendum 2.3) | PR-35 |
| Hosted CI on the current head (evidence and release lanes, attestation on the hosted runner) | PR-35 |
| PD-10 and PD-11 (two pinned tests adapted to the label) were flagged to Nathan with the plan; if he or the IA reads either as a protected boundary, the route is RS-10/RS-20 | Nathan / IA |
| OBS-W2-1, OBS-W2-2 (doc-delta candidates), OBS-W2-3 (other ambient probes) | plan §17 owners |
| OBS-17: a qa-lane failure of `tests/qa/test_generate_epic_close_pack.py` on hosted CI is recorded, never fixed here (qa lane not selected) | QA tool and test owner through the IA |
| Prompt-use provenance writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent | pending, non-gating (§10) |

## 9. TypeSafe reading for the receiving session (PR-35, WU-PR-02)

Action sent (v6): "In a new dedicated session, take an already published pull request for one work unit of an approved change (about seven source and test files across four release-evidence tools and one validator, plus governed index and mirror companions regenerated only by their owner tool, all locally tested with the attestation rehearsed in two environments) to merge readiness: read and resolve every automated code review finding, retest locally, push coherent corrections only when needed, use paid CI economically, verify the current-head evidence and release lanes including the hosted attestation build, confirm mergeability, and record the result. No merge, no live vendor, production or database run; a lineage review follows the Product Owner's manual merge."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.59 (confidence 0.72); rung probabilities low 0.00, medium 0.01, high 0.39, extra high 0.59, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.98 (confidence 0.96). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.38, Opus 5.5 at extra high 0.58, Opus 5.5 at max 0.01, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between high and extra high. Sent 2026-10-13T17:56:23Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T17:56:23Z; HTTP 200 in 0.61 s; 4254 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5. Flags: boundary between high and extra high.
- **Notion row:** not written. **Nathan's pick for PR-35:** not stated. **For this PR-30 session:** not stated (reading in plan v1.0 §21).

**Surface advice:** run PR-35 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with GitHub access for #634 (reviews, threads, checks, and a pull-request activity subscription). Local retesting needs the E-CI environment of §4 (package-index access to build it); the E-DEB rehearsal is needed only if a correction touches `tools/evidence/build_release_attestation.py` or `tools/evidence/regenerate_identity_closure.py`. The evidence-lane test set takes about 13 minutes locally. No vendor, production or database access is needed.

## 10. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-30 / implementation 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page last edited 2026-10-12T02:30:08Z) |
| role/stage | dedicated WU-PR-02 PR engineering session / PR-30 |
| capture time | 2026-10-13T18:19:52Z |
| execution identity | https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan 1 (plan §22) |
| repository persistence | recorded here only (writer absent; pending, non-gating) |

## Canon relied on

The plan's "Canon relied on" (read on `main`), unchanged at `0cd7b84`; PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 2 and 3 (review chain) and 2.1 (reading); `AGENTS.md` (sole Index/Mirror writer, closed rails, pytest readiness, PR descriptions, evidence attribution).

## Nonclaims

No QA evidence for HDE-CRD-0002 (admission readiness only), no QA verdict, acceptance, PF09/PF30 movement, deployment, canon change, merge readiness or closure. Local green is not hosted CI; CI green is not QA.
