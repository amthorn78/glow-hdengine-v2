---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002/REMEDIATION-QA110-F01/PROPOSAL-V1.0/ESC-40-APPROVE_AS_CHANGED
approved_delta_digest: sha256 6b3b4945591e6d309bde1006dbc02e725cbe4e5b74bba77934dbc9c2ff3fc470 (the reviewed proposal v1.0's file bytes), with change C-1 of the review
producing_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
approval_decision: HDE-CRD-0002-REMEDIATION-REVIEW-QA110-F01 v1.0, APPROVE_AS_CHANGED, docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md
immutable_base: HDE-CRD-0002 Implementation Plan v1.1 (IA-30 review v1.1, INITIAL_APPROVE), docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, with Plan delta 01 v1.1 (addendum 2.19) and the FND-001 overlay (addenda 2.23, 2.24); Specification v1.1-approved with Specification delta 01 (addendum 2.20); QA Plan v1.2 (QA-70 review v1.2, APPROVE), docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md. None is edited
applicable_prior_addenda: 2.11; 2.12; 2.14; 2.17; 2.18; 2.19; 2.20; 2.21; 2.23; 2.24; 2.25 (all in docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md)
approved_delta: R-1 to R-6, V-1 to V-6, the business case and WU-REM-02 of proposal v1.0 §6, with C-1 (the return route for check 13's step-3 count), below
affected_surfaces: below, "Affected surfaces and consequences"
exclusions: below, "Exclusions and nonclaims"
conflicts: NONE (CR-1 to CR-11 carried unchanged)
unresolved_items: below, "Unresolved obligations and owners"
return_phase: PR-10 — Create PR Work-Unit Instructions — 100926.1, WORK_UNIT_ID WU-REM-02, instruction v1.0; then the ordinary unit lineage; then Kronos's verification of QA Plan v1.2 check 13
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; last addendum in the file 2.26); this addendum takes the next number
---

## 2.27 HDE-CRD-0002: remediation of QA-110 finding QA110-F01 is approved as changed — the pre-push check's throwaway copies own their objects, so a full-history checkout stays unchanged, through new work unit WU-REM-02

Timestamp: 102526 03:54 (UTC). Details: Records the ESC-40 approval, as changed, of Thoth's remediation proposal v1.0 for the HDE-CRD-0002 QA-110 finding QA110-F01 (requirement S20; QA Plan v1.2 check 13 `qa-13-prepush-check`, task T13, attempt 1). The delivered read-only pre-push check, `tools/ci/prepush_check.py`, exits 4 (`PREPUSH_CHECK_READ_ONLY_VIOLATION`) on a full-history checkout although every report passes. The remedy changes how the tool makes its throwaway copies, names the changed entries when the guard trips, and adds regression tests. A new routed work unit, WU-REM-02, delivers it. WU-PR-06 stays accepted-final (addendum 2.12).

### Source and approval

* Producing prompt: ESC-40 — Review and Return Approved Remediation — 100926.1; release GCFPE-20261009.1 / 100926.1.
* Decision: APPROVE_AS_CHANGED by Isis, the continuing HDE-CRD-0002 Lead Developer, recorded in docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md, 2026-10-25. One change, C-1, corrects the proposal's return route.
* Reviewed proposal: docs/ephemeral/HDE-CRD-0002-remediation-proposal-QA110-F01-v1.0.md (Thoth, ESC-30; file SHA-256 6b3b4945591e6d309bde1006dbc02e725cbe4e5b74bba77934dbc9c2ff3fc470; [\#730](https://github.com/amthorn78/glow-hdengine-v2/pull/730)).
* Originating finding: docs/ephemeral/HDE-CRD-0002-ESC10-qa-escalation-report-v1.0.md ([\#729](https://github.com/amthorn78/glow-hdengine-v2/pull/729)), from docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md §6 ([\#728](https://github.com/amthorn78/glow-hdengine-v2/pull/728)). Evidence of record: audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log.
* Immutable bases: as the front matter lists. Not edited.

### Cause

* `make_copy` in `tools/ci/prepush_check.py` makes every throwaway copy with `git clone --shared`. Such a copy borrows the source checkout's object store through `.git/objects/info/alternates`.
* When git writes an object that already exists in a store it reaches, it writes nothing and instead updates the timestamps (mtime and ctime) of the file holding the object (a "freshen"). Through the borrowed store, that file is the source checkout's pack.
* In replay step 08, the tool's own owner test `tests/tools/test_prepush_check.py` commits in `--shared` fixture clones of the replay copy. Those commits freshen the source's pack. The guard, which compares the lstat identity of every file under the source's `.git`, correctly reports the change.
* Git version is not the factor. A shallow source disables `--shared`, so the copy gets its own packs: the earlier passing runs used shallow sources. QA Plan v1.2's E-L is a full-history clone, the operator's real environment, and engages the mechanism.
* A timestamp change to a file under the checkout's `.git`, made by code the tool runs, is a write to the repository under the WU-PR-06 instruction's ID-2 reading of S20 ("No report may create, modify or delete any file there"). The defect is in the copy mechanism. The guard's precision is correct and stays.

### Approved delta

* **R-1. The copy owns its objects.** `make_copy` makes every throwaway copy with `git clone --quiet --no-hardlinks --dissociate --no-checkout -- <source> <destination>` and the detached checkout as before. A copy whose `.git/objects/info/alternates` exists after the clone is a `ToolingError`. All copying reports (`lanes`, `membership`, `sweep`, `replay`) use it.
* **R-2. A violation names what changed.** `repository_state()` keeps the git-metadata entries by name. A new `state_changes(before, after)` lists each differing entry with the fields that moved, capped at 20 lines plus a count. `main` prints each as `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: <line>` on stderr after the existing violation line. Exit status 4, stdout and the result line are unchanged. Paths and field names only; no file content, no environment value.
* **R-3. The guard's precision is unchanged.** Every field compared before is compared after, by equality of the whole state.
* **R-4. Regression tests** in `tests/tools/test_prepush_check.py`:
  * (a) a copy of a packed and of a loose source owns its objects, and a write in it of an existing blob leaves the source's state equal; in the same test, a negative control shows a `--shared` copy changing the source's metadata only;
  * (b) a copy of a source that itself borrows objects reaches neither the source nor its base;
  * (c) `state_changes` names a rewritten tracked file and a rewritten `.git/config` and carries no file content.

  The existing 137 tests stay as they are.
* **R-5. Documentation.** README.md "Pre-push check (HDE-CRD-0002)": the exit-status line says the changed entries are named on stderr, and the Limits list states that the copies own their objects, so a source that borrows objects is dissociated in the copy at the cost of a repack.
* **R-6. File set.** Only `tools/ci/prepush_check.py`, `tests/tools/test_prepush_check.py` and `README.md`. No report's output lines, inventory pin, child environment, temporary-directory rule, exit code or classifier registration changes.
* **Work unit.** WU-REM-02: PR; Distillation; not production-affecting; S20. It lands after WU-REM-01 and before the QA-120 report. Proposal v1.0 §6.3's prototype is one rehearsed implementation; the WU-REM-02 plan may adopt or improve it within R-1 to R-6.
* **Stated limits.** Each copy holds the source's object store by value (about 58 MB for this repository). A borrowing source costs one repack in the copy. A shallow source still gives copies ref-reachable history only (LR6-O7). Concurrent git activity in the checkout is still reported as a violation (IF-35-24), now with the changed entries named.
* **C-1. Return route for check 13.** QA Plan v1.2 is an approved base. Once WU-REM-02 lands, check 13 step 3's literal "137 passed" no longer matches the owner test. Its expected count therefore changes through a standalone bounded delta to the approved QA Plan:
  * Kronos authors the delta, as the Plan's owner at the return (Glow QA Guide §10.6 step 5).
  * Isis decides it at QA-70 in `APPROVED_QA_PLAN_DELTA_REVIEW` mode.
  * The delta does not go through QA-80, which revises only pending Plans.
  * Check 13's objective, target, step 1 and step 2 predicates and outcome map are unchanged.

### Verification

* V-1: the owner test passes on the WU-REM-02 head (141 tests if R-4 lands as specified), in the PR session's clone with CI's install, Python 3.12, `ruby`, `bash`, `curl`, under closed rails.
* V-2: on a full-history scratch clone of the candidate head, check 13 step 1's command exits 0 with every report `PASS` and the final `PREPUSH_CHECK_RESULT: PASS` line reporting the repository unchanged; step 2 exits 0; the clone's `git status --porcelain` is empty before and after.
* V-3: a negative control at the command level. With `make_copy` reverted to `--shared` in the scratch clone only, the same command exits 4 and names the pack's `(mtime, ctime)`.
* V-4: hosted CI on the pull request is green, including the changed-tests step that runs the registered owner test.
* V-5: PR-40 confirms the landed blobs equal the reviewed head and records V-1 to V-4.
* V-6: Kronos verifies check 13 in the QA-100 venue class (E-L, full history) under the Plan as amended by C-1's delta.

Evidence already observed before approval (planning validation, not V-1 to V-6):
* The proposal's rehearsals under git 2.43.0 and 2.53.0.
* The reviewer's independent runs on full-history clones at main `1dc12b0d` (git 2.43.0, CPython 3.12.3, `ruby` 3.3.6, closed rails):
  * the delivered tool exited 4, with the source pack's mtime and ctime moved and its size and `git status` unchanged;
  * the prototype exited 0 with all five reports `PASS`, replay step 08 "4527 passed", and "repository unchanged", with the source pack untouched.

### Business case (addendum 2.11 rule 1, as addendum 2.18 narrows it)

* Beneficiary: every PR session and operator who runs the tool on a full-history checkout; Kronos, who can then verify check 13; the HDE-CRD-0002 close, which a `FAIL_BEHAVIOR` check blocks (addendum 2.17 resolution A).
* Evidence: QA110-F01, two executions in attempt 1, reproduced by the proposal and by the review.
* Benefit: exit 0 with "repository unchanged" on a full-history checkout. When a violation does occur, the tool names its cause.
* Measure: V-6, and the regression tests green on hosted CI on the pull request and on `main`. At PR-40, V-1 to V-4 are the proxy and the measure is "not yet measurable" (addendum 2.18 rule 5).
* This fixes a breach of the read-only guarantee on a real input (addendum 2.11 rules 4(b) and 7). No cost ceiling applies (addendum 2.18).

### Affected surfaces and consequences

* Requirement S20: met on full-history checkouts once delivered; its text and acceptance are unchanged.
* `tools/ci/prepush_check.py`: not a release member; release 1.3.0 and its `release_id` are unchanged.
* `tests/tools/test_prepush_check.py` and `README.md`: as R-4 and R-5.
* CI: the classifier's lanes for the three paths. The registered owner test runs in the changed-tests step. No `ci.yml` change.
* QA Plan v1.2 check 13: step 3's count changes through C-1's delta. The rest of the check is unchanged.
* Downstream: check 13's verification, the QA-120 report and the S21 close decision.
* Not affected: production, the deployed service, release members, vendor and database paths, the evidence graph and PF canon.

### Exclusions and nonclaims

* No change to the guard's fields or equality rule. No change to the owner test's existing `--shared` fixtures (observation O-A stays with the Product Owner).
* No change to `ci.yml`, the classifier, the sweep definition, the child environment, the temporary-directory rules, exit codes, `AGENTS.md` or PF canon.
* Specification S20 is unchanged. The Product Owner decisions D-1/LR6-O1 (whether S20 is removed) and FND-028 (whether `replay` is removed) are not presumed. If S20 is removed, WU-REM-02 is moot.
* The OPS03 cross-device failure (O-1) is an independent defect outside S20 and this remedy (Glow QA Guide §3.4.8). It is routed to the Product Owner.
* This addendum is not QA, acceptance, a merge, deployment or closure. Check 13 stays `FAIL_BEHAVIOR` until its verification under the remediation return. The original failure stays visible as failure context (Glow QA Guide §10.6).

### Unresolved obligations and owners

* WU-REM-02 instruction (PR-10) and the delivery lineage through PR-40: the whole-change Implementation Agent, the WU-REM-02 PR session and the Product Owner (Proceed, merge).
* C-1's QA Plan delta for check 13 step 3: Kronos (author); Isis (QA-70 decision).
* Check 13's verification: Kronos.
* O-1 (OPS03 `EXDEV`) and O-A (the owner test's fixtures freshen the developer's checkout): the Product Owner, as later-change candidates.
* D-1/LR6-O1 and FND-028: the Product Owner, unchanged.
* PR35-C1/FND-024: unchanged (addendum 2.21). A verification run red with that signature is `FAIL_TOOLING` under check 13's Outcomes.
* Publication of this addendum into the controlled PF10 file: the Product Owner.
