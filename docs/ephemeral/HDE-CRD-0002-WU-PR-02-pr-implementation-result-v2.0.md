---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-02-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v2.0.md
artifact_version: "2.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30 (implementation and initial publication), plan cycle 2
predecessor: none in plan cycle 2 (first result of cycle 2). Cycle-1 records docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md to v1.4.md are landed history, preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v2.0.md (v2.0; landed on main by amthorn78/glow-hdengine-v2#636 as 5e39ee2)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
PR_WORK_UNIT_LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v1.0.md (PR-40, REJECT on LR-1; bounded correction §8)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
PR_RETURN_PHASE: none (no rescope)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_baseline: approved base + PF10 addendum 2.3 (reviewer chain), with lineage review v1.0 §8 binding the corrective scope, as planned by plan v2.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112d; sha256 fb2899266ec3635e7c734a880136fcfdd4cc5ebc5e2a340ae51cd7e33dca54d2; read in full by this session; unchanged on main 5e39ee2)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md § 2.3 (reviewer chain); § 2.1 (TypeSafe reading)
pf10_addendum_created: none (PR-30 is not a qualifying approval prompt)
proceed: Nathan / Product Owner's invocation of PR-30 — PR Implementation Proceed — 100926.1 in this session, by pasting the handoff that names exactly plan v2.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v2.0.md), instruction v1.0 and lineage review v1.0, after #636 merged. The cycle-1 Proceed (plan v1.0) is spent and was not used
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-02 PR engineering session, plan cycle 2 (PR-20 then PR-30), https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A; session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
vehicle: branch claude/peaceful-thompson-5topv9; pull request amthorn78/glow-hdengine-v2#637 (new; created 2026-10-13T22:52Z; base main 5e39ee2fcd84a76dfc6c96b6b477e9ea7431e2d1)
implementation_commit: c8ac4ef2631376d27eabdcc0fd817b0892d23103 (tree 0674b75ff020043a571691704225fd90f3b944e3)
record_commit: the commit that adds this file, on top of c8ac4ef; it changes only docs/ephemeral/
created_at: 2026-10-13T22:52:13Z
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); carried unchanged; no new entry
---

# HDE-CRD-0002 WU-PR-02 — PR Implementation Result v2.0 (PR-30, plan cycle 2)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** Plan v2.0's corrective scope (C-1, C-2) is implemented exactly as written. It is locally validated under plan §10 (§4), committed as one coherent commit `c8ac4ef`, pushed and published as [amthorn78/glow-hdengine-v2#637](https://github.com/amthorn78/glow-hdengine-v2/pull/637). PR-35 owns review retrieval and correction, current-head CI and merge readiness. Nothing here is merged, and nothing claims merge readiness, QA, acceptance or closure.

## 2. Recovery (plan §8 step 1)

| Check | Observation |
| :- | :- |
| Open pull requests (GitHub API, before any work) | none |
| Local worktrees and branches | one worktree, `/home/user/glow-hdengine-v2`, on `claude/peaceful-thompson-5topv9` at `67d7216` (the plan commit, squash-merged by #636 as `5e39ee2`); clean |
| Remote branch `claude/peaceful-thompson-5topv9` | absent (`git ls-remote` empty; removed after #636 merged) |
| WU-PR-02 cycle-2 artifacts | plan v2.0 on `main`, identical to the branch copy; no `*-WU-PR-02-pr-implementation-result-v2*` file; no branch or PR carrying C-1 |
| `git diff --stat ef3972b 5e39ee2 -- tests/evidence/test_hdapi_v2_contract_inventory.py tools/evidence/update_evidence_index.py ci/checks/classify_ci_changes.py` | empty; `git diff --name-only ef3972b 5e39ee2` is the plan file only, so plan §4 facts hold at the base |
| Action | branch restarted from `origin/main` (`git checkout -B`), keeping its name; its only commit held merged history. #634, its branch `claude/intelligent-cannon-32u7tl` and the cycle-1 Proceed were not used |

## 3. Implementation

C-1 applied to `tests/evidence/test_hdapi_v2_contract_inventory.py`, in `test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent`, after `monkeypatch.setattr(indexer, "HUMAN_INDEX", human_index)`, exactly as plan §6.1 writes it:

```python
    # tmp_path has no catalog/manifest.json, from which the updater derives the
    # release label (and refuses without one); this test concerns supersession.
    label = "current-release capture: release 0.0.0, release_id " + "0" * 64
    monkeypatch.setattr(indexer, "_current_release_label", lambda: label)
```

The working-tree diff was compared with the plan's prototype commit `3952915` (`git diff` against `git show 3952915`): identical. Commit `c8ac4ef` changes exactly one path (`git show --stat`: 1 file, 4 insertions, 0 deletions). No tool, CI, catalog, release member or governed artifact changed, and no governed artifact was regenerated (§4 V-11, V-12).

C-2 is this record.

## 4. Local validation (plan §10)

Environment E-CI: `/usr/bin/python3.12 -m venv`, CPython 3.12.3, CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <clone>`); pytest readiness per `AGENTS.md` (`python -m pip install -r requirements-dev.txt` exit 0, then `python -m pytest --version` → `pytest 8.4.2`); `ruby 3.3.6 (2024-11-05 revision 75015d4c1f) [x86_64-linux]` on `PATH`. Every run under `env -i` closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH` = the worktree; no vendor, geocode, database or `GH_TOKEN` variable), in detached worktrees of a scratch clone, never in the repository checkout. Tested commit: `c8ac4ef` (base `5e39ee2`). Runs 2026-10-13T22:31Z–22:51:38Z.

| # | Plan §10 step | Check | Result |
| :- | :- | :- | :- |
| V-1 | 1 | `python3 ci/checks/check_agents_md_citations.py`; `ci/checks/check_env_pins.sh` | `AGENTS_MD_CITATIONS_OK`, exit 0; `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC`, exit 0 |
| V-2 | 2 | LR-1 test alone at the base `5e39ee2` | **1 failed** (exit 1), `SystemExit: CURRENT_RELEASE_LABEL_MANIFEST_INVALID` |
| V-3 | 2 | LR-1 test alone at `c8ac4ef` | **1 passed** (exit 0) |
| V-4 | 2 | Negative control: in a worktree of `c8ac4ef`, the two lines of `_load_human_index` that exclude `EPIC034_PR04_SUPERSEDED_INDEX_KEYS` removed (1 file, 2 deletions) | **1 failed** (exit 1), `AssertionError: assert not …`; worktree restored (`git diff` 0, status empty). The candidate's updater is untouched |
| V-5 | 3 | Classifier CLI `--base 5e39ee2fcd84… --head c8ac4ef26313… --event-name pull_request` (full SHAs; outputs outside the tree) | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=1;lanes=evidence`; product, compat, db, rails, qa, release `false`; `evidence=true`; `needs_python=true`; `changed_tests=true`; `path_count=1`; targets `tests/evidence/test_hdapi_v2_contract_inventory.py`, `tests/evidence/test_http_reader_ci_ownership.py` (equal to plan P-4) |
| V-6 | 4 | Changed-test step as `ci.yml` runs it (the two V-5 targets, one `python -m pytest -q -p no:cacheprovider --` process) | **304 passed** in 125.47 s, exit 0 (plan P-7: 304); `git diff --exit-code` 0; status empty; 0 tracked files newer than the pre-run marker (no OBS-4 rewrite) |
| V-7 | 5 | Every test file that imports or runs the updater: `git grep -l update_evidence_index c8ac4ef -- tests/` (excluding `.md`) returns the same 24 files plan §10 step 5 lists | **1,406 passed** in 840.83 s, exit 0 (plan P-10: 1,406); `git diff --exit-code` 0; status empty. Includes `tests/qa/test_generate_epic_close_pack.py` (OBS-17), which passed |
| V-8 | 6 | Evidence lane: `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `ci/checks/check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_final_lf.sh` (the `.sh` files invoked directly by path, as `ci.yml` does), plus `check_lf_endings.py` | all 8 exit 0 |
| V-9 | 6 | The six evidence-lane test files | **130 passed** in 600.84 s, exit 0 (plan P-8: 130); `git diff --exit-code` 0; status empty |
| V-10 | 7 | `python scripts/release_id_recompute.py --check-manifest-only`; the four release-lane test files | exit 0; **79 passed** in 2.72 s, exit 0 (plan P-9: 79); `git diff --exit-code` 0; status empty. The attestation build was not run: the release lane is not selected (V-5) and no release input changed (plan §10 step 7) |
| V-11 | 8 | Updater written twice in a worktree of `c8ac4ef` | exit 0, 0; `git diff --exit-code` 0 and status empty after each (fixed point) |
| V-12 | 8 | `git diff --quiet 5e39ee2 c8ac4ef -- docs/evidence artifacts/evidence_index.jsonl artifacts/evidence_index.jsonl.sha256 audit/gates/topology catalog tools ci .github` | exit 0 (byte-identical) |
| V-13 | 9 | Full sweep `python -m pytest -q -p no:cacheprovider -rfE tests/` | **4,529 passed, 3 skipped, 2 xfailed, 0 failed** in 1,185.31 s, exit 0 (2026-10-13T22:31:49Z–22:51:38Z; plan P-13: the same counts); `git diff --exit-code` 0; status empty. The lineage review's sweep at `1d2c834` had 1 failed, 4,528 passed, 3 skipped, 2 xfailed; the only difference is the LR-1 test, now passing |
| V-14 | 10 | `git diff --check 5e39ee2 c8ac4ef`; `git diff --name-only 5e39ee2 c8ac4ef` | exit 0; `tests/evidence/test_hdapi_v2_contract_inventory.py` only |

Every count equals the plan's prototype count on `3952915`, whose code tree differs from `c8ac4ef`'s only by the plan file under `docs/ephemeral/`.

## 5. Requirement and obligation coverage (plan §9)

| Obligation | Status | Evidence |
| :- | :- | :- |
| LR-1; lineage review §8 item 1 (pass again, keep the intent, test-only) | met locally | V-2, V-3, V-4; V-14 |
| CX-3 refusal and CX-1/IF-7 label semantics unchanged | met | V-12 (no tool change); `test_release_label_refuses_a_manifest_that_fails_full_validation` passed in V-7 and V-9 |
| Lineage review §8 item 2 (no further regression; the corrective sweep confirms it) | met locally | V-13 |
| Lineage review §8 validation: every updater-consuming test file, or the full sweep | met (both run) | V-7, V-13 |
| Lineage review §8 validation: evidence and release lane sets | met | V-8, V-9, V-10 |
| Lineage review §8 validation: Index, Mirror and governed companions byte-identical | met | V-11, V-12 |
| S03 outcome held across units; Plan v1.1 WU-PR-02 risk "Mirror consumers rejecting added fields" | met locally | V-7, V-13 |
| WU-PR-02 acceptance (1) to (5); contracts D-1 to D-5; C-5 no member change | unchanged | V-10 (`--check-manifest-only` 0); V-12 |
| Hosted CI (evidence lane, changed-test step, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) | pending | PR-35 |

## 6. In-flight decisions

| Decision | Why necessary | Tested by |
| :- | :- | :- |
| Restart the designated branch from `origin/main` (`git checkout -B`), keeping its name | its only commit was plan v2.0, already squash-merged by #636; a merged vehicle is never reused, and its remote branch no longer existed | §2; remote head read back after the push (§7) |

No other decision was taken. Plan decisions PD-12 to PD-15 were implemented as written.

## 7. PR_REMOTE_ACTION_LEDGER

| Time (UTC) | Action | Fact |
| :- | :- | :- |
| before work | Open-PR read | none |
| 22:31:18 | Local commit | `c8ac4ef` (C-1) |
| 22:31–22:51:38Z | Local validation | §4 |
| 22:51:47 | Push 1 | `git push -u origin claude/peaceful-thompson-5topv9`: `[new branch]` (the remote branch did not exist; no force); remote head read back `c8ac4ef2631376d27eabdcc0fd817b0892d23103` |
| ~22:52 | PR | #637 created (base `main`, head `claude/peaceful-thompson-5topv9`, not draft), body with the `.github/pull_request_template.md` headings and the `AGENTS.md` content rules |
| after this record | Push 2 (record only, `docs/ephemeral/`) | read back after push; selects no CI lane |
| — | Review reads | none (PR-35) |
| — | CI | none observed by PR-30; expected: evidence lane and the two-target changed-test step on the PR head (V-5) |
| — | Mergeability | not read by PR-30 (PR-35) |
| next | Evidence action | PR-35: Codex code review on the current head; hosted `test` job with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the hosted `ruby` version if the job log shows it (O-6) |

## 8. GCF-17 continuity (PR-30 and PR-35 share each value)

`WORK_UNIT_ID` WU-PR-02; original Proceed (front matter); workspace `/home/user/glow-hdengine-v2` in this cloud container (PR-35 recovers it from the branch if its container differs); branch `claude/peaceful-thompson-5topv9`; pull request amthorn78/glow-hdengine-v2#637; PR instruction v1.0; detailed plan v2.0; primary skill glow-hde-pr-development; recovery lineage: lineage review v1.0 → plan v2.0 → this result v2.0.

## 9. Constraints and unresolved items

| Item | Owner |
| :- | :- |
| Codex code review findings on the PR (none read yet); no Codex security review (PF10 addendum 2.3) | PR-35 |
| Hosted CI on the current head (evidence lane; changed-test step with the contract-inventory file, which needs `ruby` on the runner, PF10 addendum 2.2 B-8) | PR-35 |
| O-6: hosted `ruby` version unprinted | PR-35 records it if the job log shows it; IA |
| CX-2 residual / LR-O1, LR-O2, LR-O3 | IA, in later instructions (lineage review §7) |
| OBS-W2-1, OBS-W2-2, OBS-W2-3; OBS-17 (passed locally in V-7); AQ-1 | owners named in plan §17 |
| Prompt-use provenance writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent | pending, non-gating (§11) |
| Merge | Nathan / Product Owner (manual) |

## 10. TypeSafe reading for the receiving session (PR-35, WU-PR-02 cycle 2)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation is given beside it.

Action sent (v6): "In a new dedicated session, take an already published corrective pull request for one work unit of an approved change (a 4-line test-only change to one existing test in a 4,400-line test file plus a result record, already locally tested with a full sweep of about 4,500 tests) to merge readiness: read and resolve every automated code review finding, retest locally, push coherent corrections only when needed, use paid CI economically, verify the current-head evidence lane and changed-test step, confirm mergeability, and record the result. No merge, no live vendor, production or database run; a lineage review follows the Product Owner's manual merge."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.15 (confidence 0.79); rung probabilities low 0.00, medium 0.09, high 0.68, extra high 0.23, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.99 (confidence 0.98). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.09, Opus 5.5 at high 0.67, Opus 5.5 at extra high 0.23, Opus 5.5 at max 0.00, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.00, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T22:37:24Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T22:37:24Z; HTTP 200 in 0.57 s; 4249 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- **One send.** The Notion row was not written (this executing-flow session writes nothing to Notion).
- **Nathan's pick for PR-35:** not stated. **For this PR-20/PR-30 session:** not stated (the reading for PR-30 is in plan v2.0 §20).

**Surface advice (facts, not a model recommendation):**
- PR-35 runs as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with GitHub access to the PR (reviews, threads, check runs, and a pull-request activity subscription) and Notion read access for the prompt.
- Local retesting needs Python 3.12 with CI's install (package-index access to build it) and `ruby` on `PATH`; the cloud container provides `/usr/bin/python3.12` and `ruby` 3.3.6. No Debian rehearsal and no vendor, production or database access are needed.
- Measured here: the changed-test step about 2 minutes; the evidence-lane test set about 10 minutes; the updater-consumer set about 14 minutes; the full sweep about 20 minutes (with other runs sharing 4 cores).

## 11. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-30 / implementation 2 (plan cycle 2) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-02 (LR-1 correction) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08Z) |
| role/stage | dedicated WU-PR-02 PR engineering session (cycle 2) / PR-30 |
| capture time | 2026-10-13T22:52:13Z |
| execution identity | https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A |
| inherited usage | PR-10 instruction 1; PR-20 plan 1 and plan 2 (plan v2.0 §21); PR-30 implementation 1; PR-35 review resolution 1; PR-40 lineage review 1 |
| repository persistence | recorded here only (writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent at `5e39ee2`; pending, non-gating) |

## Canon relied on

Read on `main` at `5e39ee2` (`docs/pfcanon/` unchanged since `cc3dc33`): plan v2.0 "Canon relied on" (PF10-HDE-Build-Notes v13.5.5, read in full: addenda 2.1, 2.2 B-8, 2.3 Rules 2 and 3; PF04-Canon-HDE-Governance v2.8.7 §9.1.1, §9.1.2, §9.7.7; PF27-Canon-Plan-Templates v2.0.5 "Repository loci and file minting" and "CI lane classification and automated budget-control discipline"); PR-30 — PR Implementation Proceed — 100926.1 (read in full); `AGENTS.md` (closed rails, pytest readiness, sole Index/Mirror writer, evidence attribution, PR descriptions).

## Nonclaims

No QA evidence for HDE-CRD-0002, no QA verdict, acceptance, PF09/PF30 movement, deployment, canon change, merge readiness or closure. Local green is not hosted CI; CI green is not QA. WU-PR-02 is not accepted by this record; PR-40 decides that after Nathan's merge. #634 and its description are unchanged and remain landed history.
