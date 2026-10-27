---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-REM-02-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
predecessor: none (the first instruction for WU-REM-02)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-02
work_unit_title: "Pre-push check copies own their objects (PR; Distillation; not production-affecting; S20; remedy for QA110-F01)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (INITIAL_APPROVE). Neither is edited. QA Plan v1.2 (QA-70 review v1.2, APPROVE) is also an approved base and is not edited here
applicable_overlays: (1) Specification delta 01 (addendum 2.20); (2) Implementation Plan delta 01 v1.1 (addendum 2.19); (3) the FND-001 overlay (addenda 2.23, 2.24); (4) the QA110-F01 remedy, REMEDIATION_REVIEW v1.0 APPROVE_AS_CHANGED with C-1, recorded as addendum 2.27 (record only; not yet in the PF10 file); (5) addendum 2.18 (no cost ceiling) and 2.11 rules 1, 2 and 4 to 8 as 2.18 narrows them; (6) addendum 2.14 (P1); (7) addendum 2.3 (no Codex security review)
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S20 (unchanged), with docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (approved; addendum 2.20)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 WU-PR-06 (acceptance (1) and (3), unchanged in meaning), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md. WU-REM-02 is a routed work unit added by the remediation overlay (review §5), not by a Plan revision
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-QA110-F01 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md (APPROVE_AS_CHANGED, C-1; "ASK OK."; Isis; blob 324ab0552f02; #731, squash 91df9ab)
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-QA110-F01 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-proposal-QA110-F01-v1.0.md (Thoth; blob f0ecc382072f; SHA-256 6b3b4945591e6d309bde1006dbc02e725cbe4e5b74bba77934dbc9c2ff3fc470; #730). §6.1 (with C-1 in place of its QA Plan row) and §6.2 to §6.6 are the approved overlay
remediation_addendum: docs/ephemeral/HDE-CRD-0002-remediation-QA110-F01-PF10-build-notes-addendum-v1.0.md (numbered 2.27; blob 4bcb06ba4a67). PF10 v13.7.8's last addendum is 2.26; publication is the Product Owner's
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-ESC10-qa-escalation-report-v1.0.md (QA_ESCALATION_REPORT v1.0; blob 2cfc8e558a32), finding QA110-F01, from docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md §6 (blob 0a797250aa81); evidence of record audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log
originating_stage_and_return: QA-110 (ESCALATION_REQUIRED) → ESC-10, Kronos. Return: Kronos, QA Plan v1.2 check 13's verification under the remediation return (escalation report §12; Glow QA Guide §10.6 step 5), after C-1's approved-Plan delta for step 3's count
affected_delivery_lineage: docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md (ID-2, §5.7, §5.8; blob f3a6a8855ec0) and docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-work-unit-lineage-review-v1.0.md (ACCEPT; blob 1b69f1370c80; addendum 2.12). WU-PR-06 stays accepted-final and is not reopened
form_precedent: docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.1.md
business_case_ref: proposal v1.0 §6.6, approved by review §5 and addendum 2.27 "Business case"
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
CURRENT_PF10_MARKDOWN_LINK: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (519,440 bytes; sha256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; last addendum 2.26)
ACTIVE_PF10_ADDENDA_LINKS:
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.3 (Codex security review deprecated)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.11 (business case; real inputs; finding disposition; repeated finding class), as §2.18 narrows it
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.12 (WU-PR-06 accepted; LR6-O1, LR6-O6, LR6-O7)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.14 (P1 findings)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.17 (resolution A: a FAIL_BEHAVIOR check blocks a v2 SATISFIED close)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.18 (no cost ceiling; rule 5)
  - docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md §2.21 (PR35-C1, the auto-maintenance race)
  - docs/ephemeral/HDE-CRD-0002-remediation-QA110-F01-PF10-build-notes-addendum-v1.0.md (2.27, the approved remedy; record pending publication)
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state of 2026-10-12T02:29:33.739Z, read in full in this session and unchanged)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-25T04:20:00Z
repository_baseline: origin/main 91df9ab (#731). Every repository fact in §5 was measured at this head
receiver: a new dedicated HDE-CRD-0002 WU-REM-02 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1 to CR-8, CR-10 decided; CR-9 PROPOSED; CR-11 APPROVED_AS_CHANGED (a); all carried unchanged; no new entry (§16)
---

# HDE-CRD-0002 WU-REM-02 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one PR instruction for WU-REM-02, the remedy Isis approved as changed for QA-110 finding QA110-F01 (S20; QA Plan v1.2 check 13).

- **The defect.** `tools/ci/prepush_check.py` makes every throwaway copy with `git clone --shared`. On a full-history checkout, the copy borrows the source's object store through `.git/objects/info/alternates`. In replay step 08, the owner test commits in fixture clones of the copy, and git "freshens" (re-timestamps) the source's pack instead of writing a duplicate object. The tool's guard correctly sees a changed file under the source's `.git` and exits 4 (`PREPUSH_CHECK_READ_ONLY_VIOLATION`), although every report passed. Under WU-PR-06's ID-2 reading of S20 that is a write to the repository.
- **The unit.** Three files (§6):
  - `tools/ci/prepush_check.py` (R-1, R-2, R-3);
  - `tests/tools/test_prepush_check.py` (R-4);
  - `README.md` (R-5).
- **The proof.** V-1 to V-6 (§10). V-1 to V-4 belong to the PR lineage, V-5 to PR-40, and V-6 to Kronos at the return.

This instruction issues the approved remedy into one work unit. It does not approve a plan, give a Proceed, implement, merge or decide QA. WU-PR-06 stays accepted-final (addendum 2.12) and is not reopened. Check 13 stays `FAIL_BEHAVIOR` until Kronos verifies it under the remediation return.

## 2. Identity and lineage

| Item | Value |
| :- | :- |
| Unit | WU-REM-02, a PR unit in the Distillation phase, not production-affecting, requirement S20. It lands after WU-REM-01 (accepted, addendum 2.25) and before the QA-120 report (review §5) |
| Approved bases (immutable) | Specification v1.1 with delta 01; Implementation Plan v1.1 with its review v1.1, Plan delta 01 v1.1 and the FND-001 overlay; QA Plan v1.2 |
| Remediation overlay | Proposal v1.0 §6.1 (with C-1 in place of its QA Plan row) and §6.2 to §6.6; review v1.0 §4 and §5; addendum 2.27 record |
| Affected accepted lineage | WU-PR-06: instruction v1.0 ID-2's example mechanism "Measured feasible: `git clone --shared` plus a detached checkout" is superseded for WU-REM-02 (proposal §6.1). ID-2's rule stands as written |
| Originating finding | QA110-F01 (escalation report v1.0), with its evidence of record |
| Return owner | Kronos, check 13's verification; first C-1's approved-Plan delta (Kronos authors, Isis decides at QA-70) |
| PR lineage owner | This IA (PR-10 now, PR-40 after the merge) |
| `PR_RETURN_PHASE` | Not applicable: WU-REM-02 has no Proceed or pull request |

## 3. Unit selection and dependency state

- **Selected because:** review v1.0 routes the approved remedy to PR-10 for WU-REM-02 (its `next_prompt`; addendum 2.27 `return_phase`).
- **Dependencies:** none on unmerged work. WU-REM-01 is merged (#716, addendum 2.25), #731 is merged.
- **Open Product Owner decisions, not presumed** (review §2 row 7; addendum 2.27 "Exclusions"): D-1/LR6-O1 (whether S20 is removed by a later Specification delta) and FND-028 (whether the `replay` report is removed). If S20 is removed, WU-REM-02 is moot and stops. If only `replay` is removed, R-1 still governs the three other copying reports. Neither decision blocks this unit.
- **Order after this unit:** PR-20 → Product Owner Proceed → PR-30 → PR-35 → Nathan's merge → PR-40 → C-1's QA Plan delta (Kronos; Isis at QA-70) → check 13's verification (Kronos, QA-90 under the remediation return).

## 4. Required behaviour (approved overlay; addendum 2.27 "Approved delta")

**R-1. The copy owns its objects.** "`make_copy` makes every throwaway copy with `git clone --quiet --no-hardlinks --dissociate --no-checkout -- <source> <destination>` and the detached checkout as before. A copy whose `.git/objects/info/alternates` exists after the clone is a `ToolingError`. All copying reports (`lanes`, `membership`, `sweep`, `replay`) use it."
- Today `make_copy` (line 365) clones with `--quiet --shared --no-checkout` (line 368).
- `--no-hardlinks` avoids the hardlink clone's ctime change on the source. `--dissociate` repacks away any alternates the source itself borrows (proposal §6.2; alternative (f)).

**R-2. A violation names what changed.** "`repository_state()` keeps the git-metadata entries by name. A new `state_changes(before, after)` lists each differing entry with the fields that moved, capped at 20 lines plus a count. `main` prints each as `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: <line>` on stderr after the existing violation line. Exit status 4, stdout and the result line are unchanged. Paths and field names only; no file content, no environment value."
- Today `repository_state` (line 353) folds each metadata directory into one digest through `_metadata_digest` (line 268), and `main` prints one violation line (line 1743). Exit 4 is `EXIT_READ_ONLY_VIOLATION` (line 84).
- Proposal §6.2 gives the entry fields: path with mode, size, mtime, ctime, and a SHA-256 of the bytes outside `objects/`.

**R-3. The guard's precision is unchanged.** "Every field compared before is compared after, by equality of the whole state." Only the representation of the metadata changes (entries instead of one digest per directory), so that R-2 can name them.

**R-4. Regression tests** in `tests/tools/test_prepush_check.py`:
- (a) a copy of a packed source and of a loose source owns its objects, and a write in it of an existing blob leaves the source's state equal. In the same test, a negative control shows a `--shared` copy changing the source's metadata only, with `state_changes` naming the object file with `mtime, ctime`;
- (b) a copy of a source that itself borrows objects reaches neither the source nor its base;
- (c) `state_changes` names a rewritten tracked file and a rewritten `.git/config` and carries no file content.
- "The existing 137 tests stay as they are." Expected total: 141 if R-4 lands as four test items (addendum 2.27 V-1).

**R-5. Documentation.** In `README.md` "Pre-push check (HDE-CRD-0002)" (line 169):
- the exit-status line (today "… 4 when the repository changed during the run.") gains that the changed entries are named on stderr;
- the Limits list gains one line: the throwaway copies own their objects, so a source that borrows objects (`--shared`, `--reference`) is dissociated in the copy, at the cost of a repack.
- `AGENTS.md` is not touched.

**R-6. File set.** "Only `tools/ci/prepush_check.py`, `tests/tools/test_prepush_check.py` and `README.md`. No report's output lines, inventory pin, child environment, temporary-directory rule, exit code or classifier registration changes."

**Stated limits** (addendum 2.27; proposal §6.4):
- each copy holds the source's object store by value, about 58 MB for this repository;
- a borrowing source costs one repack in the copy;
- a shallow source still gives copies ref-reachable history only (LR6-O7);
- concurrent git activity in the checkout is still reported as a violation (IF-35-24), now with the changed entries named.

**Exclusions** (addendum 2.27; review §6): no change to the guard's fields or equality rule; no change to the owner test's existing `--shared` fixtures (`_clone`, line 92; `_clone_at`, line 876; observation O-A stays with the Product Owner); no `ci.yml`, classifier, sweep definition, child environment, temporary-directory rule, exit code, `AGENTS.md` or PF canon change; no fix of O-1 (OPS03 `EXDEV`).

**The prototype.** Proposal v1.0 §6.3 is one rehearsed implementation of R-1 to R-4 (two files, +125/−18; from scratch commit `386b86b4` against `16437685`). It does not include R-5. The plan may adopt or improve it within R-1 to R-6 (review §5). `tools/ci/prepush_check.py` must keep out every string constant the existing no-hook test forbids in it (proposal §6.3).

## 5. Current repository and reference baseline (measured at `91df9ab`)

### 5.1 Files

| Path | Lines | Blob | sha256 | Release member | Last changed |
| :- | :- | :- | :- | :- | :- |
| `tools/ci/prepush_check.py` | 1,755 | `4dc098566620` | `f4c833d295c8f84a28d519fd541a1c630ff6d7203d8a336876bec8db647b0a82` | no | `b963ed4` (#660, WU-PR-06) |
| `tests/tools/test_prepush_check.py` | 1,070 | `8d2c0be36e2e` | `b8c2481225bed5e8b40ef4318b320cd410fb41488f9efd73d8ed5978bb1b5fe1` | no | WU-PR-06 |
| `README.md` | 254 | `ab98a1b0bc74` | `2c649484a387d032d8796e185814ea66eeed096b708c1d46e1a550a4c04f5ad2` | no | — |
| `ci/checks/classify_ci_changes.py` (unchanged by this unit) | 2,092 | `cf5be0d25a13` | `1a190cbc3377d46c1cffd002e45b0e7c8702248ce9f09f00a33be95d9c20ab06` | no | — |
| `.github/workflows/ci.yml` (unchanged by this unit) | 420 | `3836bad11c39` | `d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b` | no | — |

The tool and test blobs are the ones WU-PR-06 landed and QA tested at `2e03a268` (proposal front matter). "Release member" means 0 matches in `catalog/manifest.json`; release 1.3.0 and its `release_id` are unaffected.

### 5.2 Code facts

- **`make_copy`** (line 365) clones with `["git", "clone", "--quiet", "--shared", "--no-checkout", "--", str(repo), str(destination)]` (line 368) and raises `ToolingError` when the clone fails (line 375).
- **The guard:** `_metadata_digest` (268), `RepositoryState` (344), `repository_state` (353). The comparison in `main` is at line 1719 (refusal path) and lines 1743–1745 (the violation line and exit 4).
- **The owner test:** 137 tests collected at `91df9ab` (`pytest --collect-only`, closed rails, this IA). Its fixtures `_clone` (line 92) and `_clone_at` (line 876) use `--shared`. A comment at line 805 records that a shallow source makes `git clone --shared` fall back to copying ref history.
- **The owner registration:** `"tools/ci/prepush_check.py": ("tests/tools/test_prepush_check.py",)` at `ci/checks/classify_ci_changes.py:861`.
- **The README section** "Pre-push check (HDE-CRD-0002)" starts at line 169. Its exit-status line and its Limits list (including "A shallow source makes the throwaway copies hold ref-reachable history only.") are inside it.
- **The prototype** extracted from proposal §6.3 (218 lines) passes `git apply --check` on `91df9ab` (2 files, +125/−18).

### 5.3 CI facts

- **Classification** (`classify_paths` and `changed_test_targets`, run read-only at `91df9ab`):
  - the three files together: lanes `product` and `release`, `reason=selected_lanes`, `path_count=3`; one changed-test target, `tests/tools/test_prepush_check.py`;
  - `tools/ci/prepush_check.py` alone: `product`;
  - `tests/tools/test_prepush_check.py` alone: `product`, `release`;
  - `README.md` alone: no lane.
- So the WU-REM-02 pull request runs the product lane, the release lane and the changed-test step with the owner test. PR-20 re-measures this as `ci.yml` calls the classifier.
- **The tool's replay** is pinned to `ci.yml` by `REPLAY_WORKFLOW_SHA256` (LR6-O5). The unit does not touch `ci.yml`, so the pin is unaffected.

### 5.4 QA facts (for the return, not for this unit to change)

- QA Plan v1.2 check 13 (lines 405–426): step 1 runs `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay`; step 2 runs `--path docs/ADAPTER_009.md lanes`; step 3 runs the owner test and predicates "137 passed"; step 4 is `git status --porcelain`. Env E-L is a clean full-history clone with `ruby`, `bash` and `curl`. Exit 4 is `FAIL_BEHAVIOR`; the PR35-C1 signature is `FAIL_TOOLING`.
- After WU-REM-02, step 3's "137 passed" no longer matches. Under C-1 that count changes only through Kronos's approved-Plan delta, decided by Isis at QA-70. This unit does not edit the QA Plan.

## 6. Bounded files and components

| Path | Change |
| :- | :- |
| `tools/ci/prepush_check.py` | R-1, R-2, R-3 |
| `tests/tools/test_prepush_check.py` | R-4 only (four tests added; the existing 137 unchanged) |
| `README.md` | R-5 only (two lines in "Pre-push check (HDE-CRD-0002)") |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-02-*` | The unit's records: the plan and its prototype diff, and the result records |

Expected unchanged: every other file, including `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`, `AGENTS.md`, the QA Plan, every QA primary under `audit/qa/hde-crd-0002/`, the governed evidence (Index, Mirror, sentinels, path proofs, orientation), every release member and `docs/pfcanon/**`.

## 7. Exclusions

As §4 "Exclusions", plus:
- no HDE-CRD-0002 QA evidence is produced, edited or republished (check 13's republication is Kronos's, at the return);
- no Specification change; D-1/LR6-O1 and FND-028 are not presumed;
- no re-run or reopening of WU-PR-06;
- no tool-version pin: the remedy is version-independent (review §2 row 9; Product Owner direction `docs/ephemeral/HDE-CRD-0002-po-direction-tool-version-pinning-v1.0.md`);
- PR35-C1 / FND-024 stays with its recorded owner (addendum 2.21).

## 8. Interface contracts

- **Callers of the tool** (PR sessions, operators, QA check 13): stdout lines, exit codes 0 to 4 and the final `PREPUSH_CHECK_RESULT` line are unchanged. On exit 4, stderr adds `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: <line>` lines after the existing violation line, at most 20 plus a count. Paths and field names only.
- **The four copying reports** share `make_copy`; none can freshen the source once R-1 lands.
- **The classifier registration** keeps `tests/tools/test_prepush_check.py` as the tool's owner test; the changed-test step runs it.
- **The replay pin** (`REPLAY_WORKFLOW_SHA256`) and the inventory pin are untouched.
- **QA Plan v1.2 check 13** keeps its objective, target, step 1, 2 and 4 predicates and outcome map; only step 3's count changes, through C-1.

## 9. Disposition rules PR-20 must apply and record

1. **Design choices recorded in the plan:**
   - whether to adopt proposal §6.3's prototype as is or improve it within R-1 to R-6;
   - the shape of the metadata entries and of `state_changes`, and the ordering and cap of its lines;
   - the exact R-5 wording, within the two lines R-5 states;
   - the four R-4 tests' names and fixtures (the negative control in (a) is part of R-4, not an extra test).
2. **Prototype.** Run the change in a throwaway **full-history** clone (`git rev-parse --is-shallow-repository` prints `false`; a shallow clone does not engage the mechanism), with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), Python 3.12, `ruby`, `bash` and `curl` on `PATH`, under closed rails through `env -i` (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `HOME` an empty scratch directory). Nothing else may touch the clone during a command-level run (IF-35-24). Record exact counts, times and exit codes.
3. **Copy cost.** Measure the per-copy size and time and the owner test's run time in the plan's venue, against LR6-O6's 130 s and proposal §6.4's figures.
4. **Re-check the baseline.** Confirm §5's facts at the plan's head; record any decisive change; a change in scope goes through §14.
5. **Real inputs** (addendum 2.11 rules 4 to 6): the source is the operator's full-history checkout, a shallow checkout, or a checkout that itself borrows objects (`--shared`, `--reference`). Inputs outside that set get a stated limit, not a model.

## 10. Acceptance, tests and evidence (addendum 2.27 "Verification")

| ID | Where | Pass condition | Owner |
| :- | :- | :- | :- |
| V-1 | The PR session's clone (CI's install, Python 3.12, `ruby`, `bash`, `curl`, closed rails) | `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` passes; 141 tests if R-4 lands as four items | PR-30 |
| V-2 | A full-history scratch clone of the candidate head | Check 13 step 1's command exits 0 with every report `PASS` and the final `PREPUSH_CHECK_RESULT: PASS` line reporting the repository unchanged; step 2 exits 0; the clone's `git status --porcelain` is empty before and after | PR-30, PR-35 |
| V-3 | The same scratch clone | Negative control: with `make_copy` reverted to `--shared` in the scratch clone only, the same command exits 4 and its stderr names the pack's `(mtime, ctime)`; reverted before commit | PR-30 |
| V-4 | Hosted CI on the pull request | Every lane the classifier selects (today product and release) and the changed-test step with the owner test are green, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | PR-35 |
| V-5 | PR-40 | The landed blobs equal the reviewed head; V-1 to V-4 recorded; the owner test's collected count at the merged head recorded (C-1's delta uses it) | This IA |
| V-6 | The return: Kronos, in the QA-100 venue class (E-L, full history) | Check 13 under QA Plan v1.2 as amended by C-1's delta | Kronos |

- **Evidence obligations:** the PR result record names every check run, with commands, counts, times and exit codes, and includes the V-2 and V-3 outputs (the violation's named entries for V-3). Nothing from a scratch clone is committed.
- **Business case** (proposal §6.6; addendum 2.27; addendum 2.11 rule 1 as 2.18 narrows it):
  - **Beneficiary:** every PR session and operator who runs the tool on a full-history checkout; Kronos, who can then verify check 13; the HDE-CRD-0002 close, which a `FAIL_BEHAVIOR` check blocks (addendum 2.17 resolution A).
  - **Evidence:** QA110-F01, two executions in attempt 1, reproduced by the proposal and by the review.
  - **Benefit:** exit 0 with "repository unchanged" on a full-history checkout; a violation, when one occurs, names its cause.
  - **Measure:** V-6, and the regression tests green on hosted CI on the pull request and on `main`. At PR-40, V-1 to V-4 are the proxy and the measure is "not yet measurable" (addendum 2.18 rule 5).
  - **No cost ceiling** (addendum 2.18 rule 1). It fixes a breach of the read-only guarantee on a real input (addendum 2.11 rules 4(b) and 7), not tooling for its own sake.

## 11. Migration and security constraints

- **Migration:** none. **Rollback:** the Product Owner reverts the squash commit; no release member changes, so no manifest refresh.
- **Security:**
  - the tool stays read-only by construction (ID-2) and runs children under closed rails (ID-9);
  - R-2's stderr lines carry paths and field names only: no file content, no environment value, no secret;
  - every local run uses `env -i`, so the container's vendor, database and GitHub keys reach no process.
- **Real inputs:** §9.5.

## 12. Engineering, review, CI and merge obligations

**PR-20, in a new dedicated WU-REM-02 PR session:**
- reads this instruction and its lineage, with the three files, `ci.yml` and QA Plan v1.2 check 13 on `main`;
- applies §9 and writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`, with a prototype diff covering all three files;
- returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.

**PR-30**, after Nathan's Proceed for that exact plan, given against the business case:
- recovers existing work first; changes only the three files;
- runs V-1 to V-3 and the pre-push check (`python tools/ci/prepush_check.py lanes build-notes`, and `--path <each changed path> membership`);
- commits coherently, publishes `PR_CANDIDATE_PUBLISHED` and hands off to PR-35 in its own session.

**PR-35**, in its own dedicated session:
- **Codex code review:** dispositions findings under addendum 2.11 rule 7 and addendum 2.14. A P1 on a real input is fixed; declining a P1 goes to the Product Owner first; rule 8 applies to a repeated finding class. A finding on an input outside §9.5's set gets the traced path and the stated limit.
- **No security review** (addendum 2.3).
- **CI:** V-4 and mergeability on the current head. A red run with the PR35-C1 signature is a known execution fault (addendum 2.21), not a reason to widen the unit; a failure red on the base too is base-red.
- **Re-runs:** V-1 after any correction; V-2 and V-3 when a correction touches `make_copy`, the guard or `main`'s violation output.
- **Returns** `MERGE_PENDING` without merging.

**Other obligations:**
- **PR description:** the `.github/pull_request_template.md` headings, filled under the `AGENTS.md` rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40** (this IA, after the merge is observed or asserted): verifies R-1 to R-6 on the merged head and V-1 to V-4 from the records and the hosted run; records the owner test's collected count (V-5); records the measure as "not yet measurable". On ACCEPT the next stage is the remediation return: C-1's approved-Plan delta and Kronos's check 13 verification (review §7; escalation report §12).
- **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change; no QA evidence produced or edited.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect worktrees, branches, pull requests and `docs/ephemeral/` before creating anything.
- **Rehearsals:** only in throwaway full-history clones. Discard and re-clone on failure. Nothing from them is committed.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version.
- **Abort:** only by Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material:** a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or scope or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional; RS-30 for revisions); this IA reviews it through RS-20. After Proceed, PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Changes to the approved remedy itself** (R-1 to R-6, V-1 to V-6, C-1) belong to Isis through ESC-30 and ESC-40, not to RS-20, as for WU-REM-01.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:** a needed change outside the three files (for example the classifier, `ci.yml`, or the owner test's `--shared` fixtures under O-A); a guard change that narrows R-3's equality; a V-2 failure that R-1 cannot fix; the Product Owner deciding D-1 to remove S20.
- **Not a trigger:** a §9.1 design choice, or a measured copy cost within proposal §6.4's stated limit.

## 15. Unresolved items, carried observations and owners

| Item | Owner |
| :- | :- |
| C-1's approved-Plan delta for check 13 step 3's count, after PR-40 records it | Kronos (author); Isis, QA-70 (decision) |
| Check 13's verification under the remediation return (V-6) | Kronos |
| Publication of addendum 2.27 into PF10 | Product Owner |
| O-1 (OPS03 `EXDEV`) and O-A (the owner test's `--shared` fixtures freshen the developer's checkout) | Product Owner, later-change candidates |
| D-1/LR6-O1 (S20's fate) and FND-028 (`replay`'s fate) | Product Owner, unchanged |
| PR35-C1 / FND-024 | As recorded (addendum 2.21) |
| CR-9 | Isis, IA-30, unchanged |

## 16. Canon-conflict register

Carried unchanged (review §8; proposal §13):

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | WU-PR-01 disposition §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner | addendum 2.7 |
| CR-9 | PROPOSED, not yet reviewed | Isis (IA-30) | `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md` §13 |
| CR-10 | APPROVED, alternative (a) | Isis (ESC-40) | addendum 2.24 |
| CR-11 | APPROVED_AS_CHANGED, alternative (a) | Isis (QA-70 review v1.0) | applied in QA Plan check 1 |

**No new conflict.** ID-2's "Measured feasible: `git clone --shared`" is an example mechanism, and C-1 is a routing correction under prompt rules (review §8). Canon is silent on git object-store borrowing (§Canon relied on), so ID-2's reading and S20's text govern.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Owned by | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S20 "writing nothing to the repository" | No file under the checkout, `.git` included, changes during a run | §1; R-1 removes the borrowing that freshens the source's pack | WU-REM-02 | V-2, V-3, V-6 | PR result; QA |
| WU-PR-06 ID-2 rule | No report creates, modifies or deletes a file in the checkout, git metadata included | R-3: guard unchanged; R-1: copy mechanism changed | WU-REM-02 (WU-PR-06 untouched) | V-1, V-2 | PR result |
| Plan v1.1 WU-PR-06 acceptance (1), (3) | Tree byte-identical before and after; no writes | Unchanged in meaning; delivered on full-history checkouts | WU-REM-02 | V-2, V-6 | PR result; QA |
| R-1 | Copies own their objects; alternates after clone is a `ToolingError`; all four copying reports | §4 R-1; §5.2 line 368 | PR-20; PR-30 | V-1 (R-4 (a), (b)), V-2, V-3 | PR result |
| R-2 | Changed entries named on stderr, capped at 20 plus a count; exit, stdout, result line unchanged; no content or env | §4 R-2; §8 | PR-20; PR-30 | V-1 (R-4 (c)), V-3 | PR result |
| R-3 | Same fields, whole-state equality | §4 R-3 | PR-20; PR-30 | V-1 (existing 137) | PR result |
| R-4 | Four tests, including the in-test negative control; existing 137 unchanged | §4 R-4 | PR-20; PR-30 | V-1, V-4 | PR result; hosted CI |
| R-5 | Two README lines | §4 R-5 | PR-20; PR-30 | PR-40 attribution | Merged diff |
| R-6 and exclusions | Three files only; no pin, env, temp-dir, exit-code or registration change | §4, §6, §7 | All phases | PR-40 attribution | Merged diff |
| C-1 | Step 3's count changes by Kronos's approved-Plan delta at QA-70, not QA-80 | §5.4; §8; §12 PR-40 | Kronos; Isis | V-5 records the count; V-6 | PR-40; QA-70; QA |
| Business case | Beneficiary, evidence, benefit, measure; no ceiling | §10 | Product Owner (Proceed); IA (PR-40 records the measure) | Measure later | QA (V-6); hosted CI on `main` |
| Stated limits | 58 MB per copy; repack for a borrowing source; shallow history; concurrent activity still trips | §4 | PR-20 measures | — | Plan |
| WU-PR-06 accepted-final; D-1, FND-028 open | Not reopened; not presumed | §1, §3 | — | — | — |

- **Numeric domains:** "137" is the owner test's collected count at `91df9ab`; "141" is 137 plus R-4's four items; "20" is the cap on named lines, followed by a count; exit 4 is `EXIT_READ_ONLY_VIOLATION`.
- **Decisive comparisons:** none fails.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated WU-REM-02 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Returns to this IA:** RS-20 for a rescope; PR-10 for an instruction defect; PR-40 after Nathan's merge.
- **Final return:** after PR-40 ACCEPT, the remediation return to Kronos: C-1's QA Plan delta (Isis at QA-70), then check 13's verification as a QA-90 task.

## 19. TypeSafe reading for the receiving session (PR-20, WU-REM-02)

Action sent (v8.2): "Plan, as a new dedicated pull-request engineering author, one detailed implementation plan for a remediation work unit with an approved instruction: change how a read-only developer tool makes its throwaway git copies so they own their objects instead of borrowing the checkout's object store, make its read-only violation message name the changed entries, add four regression tests including an in-test negative control, and add two documentation lines, across three files of a Python tool of about 1,750 lines and its test of about 1,070 lines. A rehearsed prototype diff for two of the files exists. The plan states the code design, prototypes it in a throwaway full-history clone, measures the copy cost, and defines verification including a roughly 25-minute command-level run of the tool and a negative control. It is a Markdown plan with a prototype diff; no code is committed; a Product Owner Proceed, implementation, review and an independent lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.28 (confidence 0.77). Rung probabilities: low 0.00, medium 0.03, high 0.67, extra high 0.29, max 0.01, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.10, Opus 5.5 0.82, Sonnet 5.5 0.08, Haiku 5.5 0.00 (confidence 0.76).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.003, Fable 5.1 at high 0.067, Fable 5.1 at extra high 0.029, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.025, Opus 5.5 at high 0.549, Opus 5.5 at extra high 0.238, Opus 5.5 at max 0.008, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.054, Sonnet 5.5 at extra high 0.023, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: none printed.
  - Sent 2026-10-25T04:12:01Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-25T04:12:01Z; HTTP 200 in 0.56 s; 5537 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is in review v1.0 §9.

**Surface advice:** run PR-20 in a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, dedicated to WU-REM-02, with Notion read access for the prompt.
- **Prototype venue:** a throwaway **full-history** clone (not a shallow one), CI's full install on Python 3.12, `ruby`, `bash` and `curl`, closed rails through `env -i`. Allow about 25 minutes per command-level run of check 13's step 1 (V-2, and again for V-3), with nothing else touching the clone, and about 2 to 3 minutes for the owner test.
- **Writes:** only the plan and its prototype diff, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway and database access.
- **Order:** this instruction's pull request is merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| Usage ID | `GCFPE-USE-HDE-CRD-0002-PR-10-20261025-WU-REM-02-01` |
| Change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| Requirement / work unit | S20; QA110-F01; WU-REM-02 |
| Prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, page state of 2026-10-12T02:29:33.739Z |
| Release | GCFPE-20261009.1 / 100926.1 |
| Role and stage | whole-change IA, PR-10 |
| Capture time | 2026-10-25T04:20:00Z |
| Execution identity | session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N) |
| Inherited usage | `GCFPE-USE-HDE-CRD-0002-ESC-40-20261025-QA110-F01-01` (review v1.0) and those it lists |
| Repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) |

## Canon relied on

Read on `main` at `91df9ab`. PF10 is v13.7.8.

| Decision topic | Sources and sections |
| :- | :- |
| Instruction contract, readiness, routing | PR-10 — Create PR Work-Unit Instructions — 100926.1 ("Execute" 1 to 8, "Semantic readiness before INSTRUCTION_READY", "Required result", "Next step and recovery"), read in full in this session; page state unchanged |
| The approved remedy | `docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md`, read in full; the 2.27 addendum record, read in full; proposal v1.0 front matter, §6.1, §6.2, §6.4 to §14 read in full, §6.3 extracted and applied with `git apply --check` |
| The originating finding and the return | Escalation report v1.0 §9 to §12, read |
| S20 and WU-PR-06 | Specification v1.1-approved S20 row, the Distillation and not-production-affecting rows; Implementation Plan v1.1 §7 WU-PR-06; WU-PR-06 instruction v1.0 ID-2, §5.7 and §5.8, read |
| Remediation cycle, delivery and return owner | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6 "Common remediation cycle and return owner", read in full |
| QA Plan check 13 (for C-1 and the return) | `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md` check 13 (lines 405–426), read |
| Business case, real inputs, finding disposition, no ceiling | PF10 v13.7.8 §2.11 and §2.18, read in full earlier in this session in v13.7.6; v13.7.6 → v13.7.8 only adds lines (addenda 2.25 and 2.26 and their index lines), so their text is unchanged |
| WU-PR-06 acceptance and limits | PF10 v13.7.8 §2.12, read at LR6-O1, LR6-O5 to LR6-O7 and the owner-test lines |
| Review chain | PF10 v13.7.8 §2.3 and §2.14, read in full earlier in this session in v13.7.6; unchanged in v13.7.8 |
| Repository rules | `AGENTS.md`: closed rails, "Pytest readiness rule", "Pre-push check", "Code review guidelines" (real-input rule), "Governed evidence rules", "PR descriptions" |
| Repository facts | `tools/ci/prepush_check.py` lines 84, 268, 344–375, 1719, 1743–1745; `tests/tools/test_prepush_check.py` lines 92, 805, 876, with `--collect-only`; `README.md` lines 169–200; `ci/checks/classify_ci_changes.py:861` with `classify_paths` and `changed_test_targets`, run read-only; `catalog/manifest.json` |

Canon searched (`git grep -n -i` on `origin/main -- docs/pfcanon/`) for `prepush`, `pre-push`, `WU-REM-02`, `QA110-F01`, `alternates`, `freshen` and `clone --shared`:
- PF10 v13.7.8 has 27 matching lines, in the WU-PR-06 and later HDE-CRD-0002 addenda (2.11, 2.12, 2.21, 2.25, 2.26), read where they bear on the tool. `WU-REM-02` and `QA110-F01` have no match: addendum 2.27 is a record pending publication.
- The other hits are "alternates" in the sense of alternate spellings or serializers (HDE Architecture, HDE Governance, CLI/API/Vendor Ref, Change Process Guide, HDE Schemas and Artifacts, HDE Mechanics Guide, Narrative Deliverables). None bears on git object borrowing. Canon is silent on it, as the proposal and review found.
