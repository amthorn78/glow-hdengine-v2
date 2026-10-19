---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-06-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-06
work_unit_title: "Read-only pre-push and pre-plan check (PR; Distillation; S20)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.2 ("The coverage definition contracted to WU-PR-06 is unchanged; WU-PR-06's sweep environment must provide ruby"; "The WU-PR-06 instruction carries the ruby requirement of the sweep environment"); addendum 2.3 (the reviewer chain without the Codex security review); addendum 2.4 (WU-PR-01 accepted, with its contracts C-1 to C-6 met and its observations O-1 to O-6 carried); addendum 2.5 (OBS-17 as a qa-lane risk; a record commit still selects lanes because the classifier compares base to head); addendum 2.9 (OBS-P4-1 to WU-PR-06 or a later classifier unit); addendum 2.10 (WU-PR-05 accepted, and its list "Carried into the WU-PR-06 instruction"). Addenda 2.6, 2.7 and 2.8 have no item for this unit: it changes no release member, so no refresh runs. Addendum 2.1 governs §19 only
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2; no note for this unit)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — §3, §5.2, §5.3, §6 S03 and S20 and §7.1 EC-9 bind this unit; §5 below re-measures them at the current baseline
predecessor_unit_acceptance: WU-PR-01 (the dependency) docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT across #627 and #630; blob 2ae866d6bab1; addendum 2.4), with review v1.0 (blob 2cfbb5ec33d8; its §6 O-1 to O-6 stand); WU-PR-02 to WU-PR-04 (addenda 2.5, 2.8, 2.9); WU-PR-05 (the unit before this one in the merge order) docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-work-unit-lineage-review-v1.0.md (ACCEPT on #656; blob 80d6fe69878d; landed by #657 as 7d9dbbc; addendum 2.10)
coverage_contract_read: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (blob 24597a31fbb9) §5.1 "Computation (binding definition for acceptance (1) and for WU-PR-06's `sweep`)" and §8 contracts C-3, C-4 and C-6
structure_precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (blob ee5acb997fcc)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md (v13.6.1, effective 2026.10.19; blob 7eca21acb410; 208,266 bytes; sha256 ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e; Product Owner commit 5e62a65, "PF10 update"). Read for this unit, in this invocation: the complete v13.6 → v13.6.1 diff (the version lines, one index line and addendum 2.10 appended; nothing else changed), with 2.10 read in full; 2.1, 2.2, 2.3, 2.4 and 2.5 in full; a search of the whole file for this unit's terms (WU-PR-06, pre-push, the carried observation IDs), which finds items only in 2.2, 2.5, 2.9 and 2.10. Addendum 2.9 was read in full at PR-10 for WU-PR-05, and 2.6 to 2.8 at PR-10 for WU-PR-04, both on 2026-10-18 in this session; the diff shows them byte-unchanged since
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md §2.2, §2.3, §2.4, §2.5, §2.9, §2.10; §2.1 for §19
pf10_note: addendum 2.10 names `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md` for the `build-notes` report. The Product Owner's 5e62a65 replaced that file with v13.6.1 after the review was written. The report resolves the file by pattern (ID-6), so the rename changes nothing in this unit
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state as of 2026-10-12T02:29:33.739Z, re-fetched in this invocation, byte-identical to the copy used for WU-PR-05, and read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: @@CREATED@@
repository_baseline: origin/main 5e62a65d6e89d9a84557b73a9e70ab46ee953aeb (tree cececdb14470). Outside docs/ephemeral/ and docs/pfcanon/, every byte equals 822ce15 (#656, accepted WU-PR-05): the two later commits add the WU-PR-05 lineage review (7d9dbbc, #657) and rename PF10 to v13.6.1 (5e62a65). Every repository fact in §5 was measured at 5e62a65 in detached scratch copies
receiver: dedicated HDE-CRD-0002 WU-PR-06 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, re-fetched in this invocation and byte-identical to the copy used for WU-PR-05)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-PR-06 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-06 of HDE-CRD-0002. The whole-change IA issues it from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- author the detailed per-file plan, the tool's design or its test. Those are the PR session's (§9);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- decide a canon, product or scope question;
- change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-06 (Plan v1.1 §7 heading "WU-PR-06 — Read-only pre-push and pre-plan check (PR; Distillation)") |
| Requirement | S20 (source item 7) |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above). Review v1.0 and v1.1 carry no note for this unit |
| Overlays | PF10 addenda 2.2, 2.3, 2.4, 2.5, 2.9 and 2.10, as named in the header |
| Upstream units | WU-PR-01 to WU-PR-05, all accepted |
| Phase | Distillation |
| Live QA class (Specification table; Plan §6) | Not production-affecting ("read-only repository tooling") |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1, INITIAL_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.**
  - Plan v1.1 §7: "Sixth; after WU-PR-01 (lane lists and sweep definition final)."
  - Specification v1.1, Distillation row: "S20 follows S03 to S05." S03 to S05 are WU-PR-01's.
  - WU-PR-01 is accepted (lineage review v2.0; addendum 2.4). Its contracts C-3 (coverage definition) and C-4 (final lane lists) are met: the definition and the lane names and step structure are unchanged (review v1.0 §5).
  - WU-PR-05, the unit before this one in the merge order, is accepted (lineage review v1.0 on #656; addendum 2.10).
  - No `HDE-CRD-0002-WU-PR-06-*` file exists on `main`.
  - No QA Guide, QA Plan or Ops receipt is a prerequisite (Plan §9 item 4).
- **Order.** WU-PR-01 → WU-PR-02 → WU-PR-03 → WU-PR-04 → WU-PR-05 → **WU-PR-06** → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7). WU-PR-07 may be prepared in parallel but merges after this unit.
- **Downstream dependents** (contracts in §8):
  - WU-DOC-01 documents the tool's usage ("pre-push check usage" in `README.md`, Plan v1.1 §7 WU-DOC-01 bounded scope);
  - every later PR session may use the tool for its pre-plan and pre-push picture; no later unit depends on it to merge;
  - a later change to `ci.yml`'s steps, to the coverage definition or to the classifier's interface must keep the tool's pins true in the same pull request (G-2, G-3).

## 4. Required behavior

**Acceptance intent and constraints**, verbatim from the approved Specification:

| ID | Scope | Acceptance intent |
| :- | :- | :- |
| S20 | "One read-only pre-push and pre-plan check with its own test" | "One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository" |

- **Constraint "Duplication."** "S20 duplicates CI logic and must track `ci.yml` changes."
- **Constraint "Uncovered tests."** "Running the uncovered files in the repository tree can rewrite tracked evidence (O-11), so any sweep runs in a throwaway copy."
- **Exclusions** that bind this unit: "No SessionStart hook (item 7)"; "No change to the code-review tooling (item 6)"; "No canon change beyond S21's ADR-covered close-pack change"; "No new evidence family, acceptance token or token matrix, except a home for close-workflow run evidence that S21's ADR admits (S21)"; "As implementation work: no deployment, no production configuration change, and no live vendor call made by an implementation work unit".
- **Live QA row.** S20 is "Not production-affecting".

**Plan v1.1 §7 WU-PR-06 block**, verbatim:
- **Purpose.** "Give every PR session one read-only command for its pre-push picture."
- **Bounded scope.** "S20; EC-9; IF-9."
- **Inputs.** "Audit §5.2, §5.3 (sweep definition), §6 S20; the classifier CLI; the `ci.yml` lane steps."
- **Deliverables.** "`tools/ci/prepush_check.py` (new); `tests/tools/test_prepush_check.py` (new owner test); `ci/checks/classify_ci_changes.py` (lanes and owner for the new path)."
- **Acceptance and verification.** "(1) Each IF-9 report runs and the repository tree is byte-identical before and after (asserted by the tool and by its test). (2) `lanes` output equals the classifier's for the same inputs; `membership` matches `ADMITTED_RELEASE_ROSTER`; `build-notes` resolves exactly one `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` and prints its SHA-256; `sweep` reproduces the Audit §3(b) set and runs it in a throwaway export; `replay` covers every lane step name in `ci.yml` (pinned by the test). (3) No hook, no writes, no network. (4) Lanes green (full validation, classifier changed)."
- **Evidence obligations.** "PR result record with one captured run."
- **Risks and recovery.** "Drift from `ci.yml` (the pinning test)."
- **Nonclaims.** "The tool's green is not CI's green and not QA."

**Plan v1.1 §5 IF-9**, verbatim: "`python tools/ci/prepush_check.py` with sub-reports: `lanes` (classifier delegation for given paths and base/head), `membership` (roster membership of given paths), `build-notes` (unique PF10 path and SHA-256), `sweep` (uncovered set in a throwaway export), `replay` (every `ci.yml` lane step in a throwaway worktree); writes only under a temporary directory; asserts a clean tree before and after; exit 0 only when every requested report succeeds."

**Audit §6 S20 "Required behavior"**, verbatim: "One command (proposed `tools/ci/prepush_check.py`, §7.1 EC-9) with sub-reports: lanes and changed-test targets for given paths (delegating to the classifier, not re-implementing it); release membership of given paths; Build Notes path and SHA-256; the uncovered sweep (classifier-derived set) run in a throwaway export; a `ci.yml` replay in a throwaway worktree; every report read-only with respect to the repository (writes only under a temporary directory; asserts a clean tree before and after)." Its "Feasibility": "duplication of CI logic is bounded by delegating to the classifier and by replaying `ci.yml` text rather than copying its commands (the unit decides the replay mechanism; a test pins that the replay covers every lane step name in `ci.yml`)." EC-9: "Tool path `tools/ci/prepush_check.py` with owner test `tests/tools/test_prepush_check.py`; delegates to the classifier; replays `ci.yml` text."

**Origin (context, not scope):** item 7's observed need, "Each PR session re-derives by hand, or skips, the base-versus-head sweep of tests no lane runs, CI-lane impact, release membership and the `ci.yml` replay. PR04 had 4 failed CI runs out of 19" (kickoff and briefs v1.2). The briefs' proposed step "sets up a Python 3.12 venv" did not enter the approved Specification; the tool uses the caller's environment (ID-8).

### 4.1 Requirements mapped to canon

| # | Requirement | Governing canon on `main` (read for this instruction) |
| :- | :- | :- |
| C1 | The tool is non-mutating | Glow QA Guide §2.2.11 "Evidence-governed CI sequence (names-only)": "A non-writing check MUST NOT mutate the repository or external state"; `AGENTS.md` "Truncation/retrieval-failure guardrail" for exit statuses (ID-2, ID-3) |
| C2 | Closed rails and no network | Glow QA Guide §2.2.6 "Rails posture in CI (default CLOSED)": "Run pre-commit/CI with `SAFE_MODE=1`, `ALLOW_NETWORK=0` by default"; HDE Mechanics Guide §1.2 "CI default CLOSED & evidence"; `AGENTS.md` closed-rails default and redaction rule (ID-9) |
| C3 | Tooling failures stay distinct from behavior failures | Glow QA Guide §2.2.5 "Tooling vs behavior failures (pytest and harnesses)", including "Import-time dependency failures are tooling, not behavior" (ID-7, ID-8, ID-9) |
| C4 | `lanes` mirrors the classifier; a reduced lane set is sufficient CI scope | Change Process Guide §0.2: "When the current workflow's applicability classifier validly selects a reduced lane set, a passing final applicability audit is sufficient machine evidence for that CI scope" (ID-4, ID-8) |
| C5 | The tool is a durable, repository-owned control, not a new required CI suite; the implementation task, not this instruction, chooses its mechanism | Plan Templates "CI lane classification and automated budget-control discipline": "Durable control MAY use … repository-owned validation tooling"; "Manual push limits, agent self-reporting … are not CI budget controls"; "The authorized implementation task selects the smallest safe repository-grounded design; a plan or review MUST NOT invent a YAML arrangement, job name, tool, cache implementation, concurrency syntax, or change-detection mechanism". Here the tool itself is approved scope (Specification S20; Plan IF-9), and its mechanism is the PR-20 plan's and PR-30's (ID-1, §7, §9) |
| C6 | New files only within established homes; tool output is not governed evidence | Plan Templates "Repository loci and file minting": "File minting is allowed within established governed homes"; "If `scripts/`, `tools/`, or another auxiliary root is treated as governed evidence, the plan MUST bind it to an evidence family … Otherwise, it MUST classify the output as non-governed tooling output and exclude it from acceptance claims" (ID-1, §7) |
| C7 | Authority, Proceed and merge | HDE Governance §9.1.1 (PR Instructions are the IA's; Proceed per detailed PR plan; merges are Product Owner actions); §9.1.2 (canon precedence; in-flight documents govern within their scope) |

Canon has no rule about git hooks, pre-push scripts or SessionStart hooks (whole-canon search, §16). "No hook" binds through the Specification's Exclusions and the Plan's acceptance (3).

### 4.2 Binding IA decisions (canon-conforming readings; HDE Governance §9.1.2)

**ID-1. One command, five reports.**
- The tool is `tools/ci/prepush_check.py`, run as `python tools/ci/prepush_check.py` with report names exactly `lanes`, `membership`, `build-notes`, `sweep` and `replay` (IF-9). It is a script: `tools/` is not a packaged directory (`pyproject.toml` includes only `engine*`, `adapter*`, `presenter*`, `catalog*`, `math*`; §5.6), so the tool changes no distribution.
- PR-20 chooses the argument syntax, whether one invocation may request several reports, the output format and the exit codes for usage errors, and records each choice with its reason (C5). Two rules bind: exit 0 only when every requested report succeeds (IF-9), and the output is plain text on stdout that names each report, its inputs as resolved and its status.
- The tool's output is non-governed tooling output (C6). It is not evidence, does not go to `docs/evidence/`, `artifacts/` or `audit/`, and supports no acceptance claim. "The tool's green is not CI's green and not QA" (Plan).

**ID-2. "Writing nothing to the repository" (binding reading).**
- The repository is the session's checkout: its working tree, ignored files included, and its `.git` directory.
- No report may create, modify or delete any file there. That includes files `.gitignore` hides (`__pycache__/`, `*.pyc`, `.pytest_cache/`) and git metadata: `HEAD`, refs, the index, `config`, `hooks/` and the worktree registry under `.git/worktrees/`.
- Every write goes under one temporary directory outside the repository, which the tool creates owner-only and removes at exit, also when a report fails.
- Three ordinary operations write to the repository without changing `git status`. Each was measured at the baseline (§5.7), and the plan must show how the tool avoids each:
  - importing repository modules writes `__pycache__/` unless bytecode writing is off;
  - a plain `git status` rewrites `.git/index` after a timestamp change, while `git --no-optional-locks status` (or `GIT_OPTIONAL_LOCKS=0`) does not;
  - `git worktree add` registers an entry under the source repository's `.git/worktrees/`.
- "Throwaway worktree" (Specification) and "throwaway export" (Plan) therefore mean a working copy of the committed head **outside** the repository, made without writing to the repository: for example a clone of the repository into the temporary directory. Measured feasible: `git clone --shared` plus a detached checkout (§5.8). The plan states the mechanism and why it writes nothing to the repository.

**ID-3. Clean tree, committed state, local refs only.**
- Every invocation first asserts a clean tree, then runs the reports, then asserts the tree is still clean and `HEAD` is unchanged (IF-9). A dirty tree, untracked files included, is refused before any report runs, with a distinct message.
- The reports act on committed revisions, never on uncommitted bytes. `sweep` and `replay` use a copy of the given head (default `HEAD`).
- Base and head are resolved from local refs only (for example `git rev-parse --verify`). No `git fetch` and no network (ID-9). The report prints the full SHAs it used. A stale local `origin/main` is the caller's responsibility, and the report says which ref it resolved.

**ID-4. `lanes` delegates to the classifier and re-implements none of it.**
- **Base and head.** The result equals what `python ci/checks/classify_ci_changes.py --base <base> --head <head> --event-name <event> --github-output <f> --changed-tests-output <g>` produces at the same revisions:
  - the `CI_CHANGE_CLASSIFICATION:` line;
  - every `--github-output` key (the seven lanes, `needs_python`, `changed_tests`, `reason`, `path_count`);
  - the changed-test target list.

  The classifier's two output files go to the temporary directory. The event defaults to `pull_request`, as in CI, so the pull-request merge-base rule applies; addendum 2.5 records that a record commit still selects lanes because the classifier compares base to head, and the report shows exactly that.
- **Given paths.** For a path list (pre-plan use: planned paths may not exist yet), the result is the classifier's own `classify_paths(paths, governed_paths=_load_governed_primary_paths(<root>))`, combined with `changed_test_targets(<root>, paths)` exactly as `classify_git_change` combines them. The report notes that changed-test targets are computed against the files of the head, so a planned file that does not exist yet selects no target of its own (§5.3).
- **Refusals.** A classifier refusal (`CI_CHANGE_SURFACE_UNCLASSIFIED:<path>`, `CI_CHANGE_CLASSIFIER_ERROR:…`, a missing merge base) is reported verbatim and makes the report fail. For example, `tools/ci/prepush_check.py` is refused at the baseline (§5.3); a pre-plan run shows a session that a new path needs registration.
- **Equality** with the classifier for the same inputs is acceptance (2) and is tested (ID-10).
- **Path filter.** The report may state that `reason=documentation_only` means the workflow's `on.paths` filter starts no hosted run. That equivalence is already pinned by `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths` (§5.3), so stating it needs no logic of its own.

**ID-5. `membership`.**
- For each given path, the report states whether it is a member of `ADMITTED_RELEASE_ROSTER` in `engine/config/registry_loader.py`, read without writing bytecode (ID-2) and without calling admission. Acceptance (2): "`membership` matches `ADMITTED_RELEASE_ROSTER`."
- It may also print the release version and the `release_id` (the SHA-256 of `catalog/manifest.json`'s bytes, `AGENTS.md` "Release identity"). If it does, it states that a change to a member forces a same-version manifest refresh with convergence (Plan v1.1 §10), as information only.
- It never runs the cutter, the updater or any owner tool.

**ID-6. `build-notes`.**
- The report resolves `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` in the checkout. Exactly one match: it prints the repository-relative path and the SHA-256 of the file's bytes.
- Zero or several matches: the report fails and names what it found. There is no fallback to another source (PR-10 "Canonical PF source predicate": "there is no fallback").
- At the baseline: `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md`, `ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e` (§5.5). The test uses fixtures for the zero and two-file cases; it never asserts the current version's name or hash, which change whenever the Product Owner updates PF10.

**ID-7. `sweep`: the coverage definition (contract C-3, LR O-1).**
- **Binding definition**, restated from WU-PR-01 instruction v1.0 §5.1 and applied to the head's own files:
  - The set is every tracked `tests/**/test_*.py` file of the head (by `git ls-files`) that is not covered.
  - A file is covered when its path equals, or lies under, a `tests/...` token in a `python -m pytest` command of a step in the head's `.github/workflows/ci.yml`.
  - A file is also covered when its path equals, or lies under, an entry of `_full_validation_test_targets()` from the head's `ci/checks/classify_ci_changes.py`.
- **The guard's wider token set (WU-PR-01 lineage review v1.0, O-1).** The guard test `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target` counts every `tests/` token anywhere in `ci.yml` (regex `tests/[A-Za-z0-9_./-]+`).
  - At the baseline both token sets are the same 39 tokens, and both uncovered sets are empty (§5.4).
  - The tool uses the definition above. It can flag a file the guard accepts, but never miss one the guard flags.
  - The owner test pins that the two token sets are equal on the repository. A future divergence then fails the test and is decided in that pull request.
- **Reproduction (Plan acceptance (2), "`sweep` reproduces the Audit §3(b) set").** The Plan's WU-PR-01 acceptance (1) names the Audit §3(b) computation with the lane-or-target criterion, and the WU-PR-01 instruction made that the binding definition above. "Reproduces" therefore means: the same computation gives the WU-PR-01 instruction §5.1 list of 135 files at `a429c7c` and 0 files at the PR head. The result record shows both (§10).
  - PR-20 decides whether the tool accepts a revision for this, or whether the reproduction runs the tool's computation function against that revision's `ci.yml` and classifier in a throwaway copy.
  - An old classifier is imported only in a separate process from its own copy, never into the process that holds the head's classifier.
- **The run.** When the set is not empty, the report runs exactly those files: `python -m pytest -q -p no:cacheprovider <files>` in a throwaway copy of the head, under the job environment of `ci.yml` (ID-9), with `PYTHONPATH` set to the copy. The copy is a git checkout, so tests that read git metadata run.
  - Afterwards it records the copy's `git diff --exit-code` and untracked status, because uncovered files may rewrite tracked files (Specification constraint "Uncovered tests"; O-11).
  - It reports each file's outcome, keeping tooling failures (collection or import errors, missing `ruby`, a missing interpreter) apart from behavior failures (C3).
- **Status.** The report succeeds only when the set is empty. CI's coverage guard runs only when the rails lane or full validation is selected, so a new uncovered test file can merge unseen; the sweep exists to show it first. A non-empty set fails the report whatever the run's outcome. The per-file results tell the session whether to register the file or fix it.

**ID-8. `replay`: the head's `ci.yml`, step by step, in a throwaway copy.**
- **Inventory.** The replay reads the steps of the `test` job from the head's `.github/workflows/ci.yml` text with the Python standard library. PyYAML is not in CI's install (§5.6), and the Plan adds no dependency (§7).
  - Every step of the job is either executed or excluded with a fixed reason.
  - **Excluded:**
    - the `uses:` steps "Check out exact candidate head" (replaced by the throwaway copy of the head) and "Set up Python 3.12" (replaced by the caller's interpreter);
    - "Install applicable validation dependencies" (it needs the package index; the caller's environment must already have CI's install).
  - **Executed:** every other step, by its `run:` text, in file order. At the baseline these are:
    - "Classify affected CI lanes" and "Check AGENTS.md cites no project documents";
    - "Verify pytest readiness" and "Verify closed deterministic environment";
    - "Run affected behavioral tests in isolation" and the seven lane steps;
    - "Verify truthful applicability and clean candidate tree".
  - The owner test pins that executed plus excluded equals the job's step names, and that exactly those three steps are excluded. A new, renamed or removed step then fails the test (Plan "Drift from `ci.yml` (the pinning test)"; contract C-4).
- **Conditions and expressions.**
  - Each step's `if:` is evaluated from the replay's own classification of the given base and head, so the replay runs what CI would run.
  - `${{ github.event_name }}`, the base and head SHAs and `${{ steps.<id>.outcome }}` resolve from the replay's inputs and its own step outcomes.
  - `$RUNNER_TEMP` and `$GITHUB_OUTPUT` point into the temporary directory.
- **Full validation.** For identical base and head, the classifier itself returns full validation (`reason=identical_refs_full_validation`: all seven lanes and the 165 full-validation targets; §5.3). The replay therefore reaches every lane step and every full-validation target without a classifier change.
  - PR-20 decides whether to offer this as a named option.
  - It is how the tool lets a session cover OBS-P3-5 and OBS-P4-1 (ID-11).
- **Environment.**
  - The job-level `env:` block of `ci.yml` (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `PYTHONDONTWRITEBYTECODE=1`), plus each step's own `env:`.
  - The child environment drops the vendor, database and GitHub keys (ID-9).
- **The copy.** The head is replayed in a throwaway git copy outside the repository (ID-2). Steps that run `git worktree add`, `git diff` or `git status` act inside the copy and write only its `.git`.
- **Interpreter.** The replay runs with the caller's interpreter, and its "Verify pytest readiness" step proves pytest runs.
  - The report prints that interpreter's version. A major.minor version other than the `python-version` the workflow's setup step names (`'3.12'` at the baseline) is a tooling failure of the report, so a green replay always means the workflow's Python.
  - The plan states how the report shows where an installed `engine` or `hdctl` resolves (OBS-W5-5, §15).
- **Results.** Each step's outcome (success, failure, skipped, excluded), its duration and its last lines. Tooling failures stay apart from behavior failures (C3). The final audit step runs with the replay's own outcomes, so `CI_APPLICABILITY_AND_EXACT_HEAD_OK` appears only when CI's own rule would print it.
- **Feasibility, measured.** A standard-library prototype of exactly this inventory, made by this IA in scratch and not a deliverable, replayed the head at the baseline in full-validation mode in a throwaway clone (§5.8). @@REPLAY_SUMMARY@@
- **Runtime.** Hosted CI took 20 min 55 s for all seven lanes on `f7d610e` (§5.9). A replay takes minutes, which is acceptable for a pre-push tool (Audit §6 S20 "Risks").

**ID-9. Closed rails, no network, keys-only output.**
- No report opens a network connection or runs `pip`, `git fetch` or any installer.
- Child processes get the `ci.yml` job environment (closed rails). The tool removes `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HD_GEOCODE_KEY`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `GH_TOKEN` and `GITHUB_TOKEN` from the child environment. It never prints an environment value except the rails and determinism pins.
- The release lane's wheel build needs no network: `tools/evidence/build_release_attestation.py` runs `pip wheel --no-index --no-build-isolation` (§5.6).
- A dependency the caller's environment lacks (`ruby` for `tests/evidence/test_hdapi_v2_contract_inventory.py`, addendum 2.2; pytest; CI's requirements) is reported as a tooling failure with what is missing. It is never installed by the tool, and never reported as a behavior failure (C3).

**ID-10. Classifier registration, the owner test and the CI shape.**
- **Registration.** The smallest registration that classifies `tools/ci/prepush_check.py`, gives it lanes and makes `tests/tools/test_prepush_check.py` its owner test (Plan deliverable "lanes and owner for the new path"; Audit §7.5: an unregistered `.py` under `tools/ci/` fails classification).
  - The owner test also becomes a full-validation target, so the WU-PR-01 coverage guard still finds zero uncovered files.
  - The owner registry keeps its fail-closed shape (contract C-6).
  - `tests/tools/` already exists, with one registered test (§5.4).
  - Every pin in `tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py` stays true. A pin that enumerates the registry the new entry joins may gain exactly that entry.
- **CI shape.** A change to `ci/checks/classify_ci_changes.py` is a full-validation path, so all seven lanes run (§5.3; acceptance (4)). No workflow step, lane or job is added. The tool runs only on a session's demand; its owner test is what CI runs.
- **The owner test.** It is fast and hermetic: it never runs the repository's own test suite, a real lane step or the attestation build. It proves:
  1. each report on known inputs, through fixtures or a temporary git repository where the real repository is too slow;
  2. `lanes` equals the classifier's CLI and functions for the same inputs, in both modes, including a refusal;
  3. `membership` against `ADMITTED_RELEASE_ROSTER`;
  4. `build-notes` with one, zero and two candidate files;
  5. `sweep`'s set computation against the binding definition and against the guard's token set on the repository (equal and empty at the baseline), plus a synthetic non-empty case and the success rule;
  6. the `replay` inventory pin of ID-8 against the real `ci.yml`, plus the condition and expression handling on a synthetic workflow;
  7. the read-only rule of ID-2 for every report: the repository's files, ignored files included, and its `.git` state named in ID-2 are byte-identical before and after;
  8. the dirty-tree refusal (ID-3);
  9. the closed-rails child environment and key removal (ID-9).
- Each guard the test relies on gets a negative control in the plan's validation (the read-only assertion, the inventory pin, the refusal). The test records its runtime.
- No test is skipped, deselected, marked `xfail` or quarantined.

**ID-11. Carried classifier gaps and observation O-14.**
- **OBS-P4-1** (a resolver-only or CLI-only change does not select the override tests) and **OBS-P3-5** (a `VERIFY.sh`-only change does not select the owner test that runs `VERIFY.sh`) are classifier gaps, re-measured at the baseline (§5.3).
  - This unit does not close them: its classifier deliverable is bounded to the new path's lanes and owner.
  - The tool surfaces them. `lanes` shows the classifier's actual selection. A full-validation replay (ID-8) runs every full-validation target, and the tests these gaps leave out are full-validation targets at the baseline: `tests/scripts/test_dev_start_reader.py` (it runs `VERIFY.sh`), `tests/bodygraph/test_vendor_prod_override.py`, `tests/cli/test_bg_resolve.py` and `tests/cli/test_aux_preview.py`.
  - The gaps themselves go to the Product Owner as later classifier change candidates: no later planned unit of Plan v1.1 is a classifier unit. The result record names them so.
- **O-14** (S19 record: "the workflow's path filter hard-codes the governed exceptions under exempt prefixes; they agree with the Index today, with no test tying them") does not reproduce at the baseline.
  - `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths`, landed by #627 (WU-PR-01), derives the expected filter from `_load_governed_primary_paths`, which reads `docs/evidence/INDEX.json`, and asserts `ci.yml` matches it.
  - This IA's negative control: removing one governed exception from `ci.yml` makes it fail (§5.3).
  - Nothing is owed by this unit. The S19 record's row stays as written; it is a historical record.

**ID-12. A correction outside the plan's change set** (lesson LR5-O2 from the WU-PR-05 lineage review).
- If PR-30 or PR-35 must correct this unit's own change in a path outside the plan's change set, it records an in-flight decision with the path, the reason, the validation and the review coverage. A Codex finding on the tool that needs one more line in a test helper is an example.
- That is a rescope trigger (§14) only when the path is in §6's expected-unchanged list or the change is material.

## 5. Current repository and reference baseline (measured at `5e62a65`)

Every fact below was measured by this IA at `5e62a65` under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, database and GitHub keys unset). The measurements used detached scratch copies of a scratch clone and a scratch venv with CI's install, whose editable install maps to that clone's checkout of `5e62a65`. Every copy ended with an empty `git status --short --untracked-files=all`. PR-20 re-verifies at its own head before planning edits (Plan Templates "Repository loci and file minting").

### 5.1 Repository state

- `origin/main` `5e62a65` (tree `cececdb14470`). `git diff --name-only 822ce15 5e62a65 -- . ':!docs/ephemeral' ':!docs/pfcanon'` is empty. The two commits since the WU-PR-05 merge add `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-work-unit-lineage-review-v1.0.md` (#657) and rename PF10 v13.6 to v13.6.1 (5e62a65).
- No code or test reads the PF10 file by a versioned name (`git grep` over `tests`, `tools`, `ci`, `scripts`, `engine`, `adapter`). `ci/checks/check_agents_md_citations.py` globs `docs/pfcanon/*.md` and excludes PF10 by stem.

### 5.2 The workflow (`.github/workflows/ci.yml`, 420 lines, blob `3836bad11c39`, SHA-256 `d02021f3bbeb22ec569fe6282c046d68468af003f0f0370313c5e76f58b6ab9b`; unchanged since #627)

- **Triggers.** `pull_request` and `push` to `main`, each with an `on.paths` filter: `'**'`, the eight negated documentation prefixes, `'**.path_proof.txt'`, and the two governed primaries `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json`.
- **Run controls.** `permissions: contents: read`; concurrency group with `cancel-in-progress` on pull requests.
- **The job.** One job `test`, `runs-on: ubuntu-latest`. Its job-level `env:` is `LC_ALL: C`, `LANG: C`, `TZ: UTC`, `SAFE_MODE: "1"`, `ALLOW_NETWORK: "0"`, `APP_ENV: dev`, `PYTHONDONTWRITEBYTECODE: "1"`.
- **Sixteen steps, in order**, with id and condition:

  | # | Step name | id | Condition | Kind |
  | -: | :- | :- | :- | :- |
  | 1 | Check out exact candidate head | — | — | `uses: actions/checkout@v4` (`fetch-depth: 0`) |
  | 2 | Classify affected CI lanes | `classify` | — | `run` (env `BASE_SHA`, `HEAD_SHA` from `${{ }}`) |
  | 3 | Check AGENTS.md cites no project documents | — | — | `run` |
  | 4 | Set up Python 3.12 | `python_setup` | `needs_python` | `uses: actions/setup-python@v5` |
  | 5 | Install applicable validation dependencies | `dependencies` | `needs_python` | `run` (`pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`) |
  | 6 | Verify pytest readiness | `pytest_readiness` | `needs_python` | `run` |
  | 7 | Verify closed deterministic environment | `env_pins` | `needs_python` | `run` (`ci/checks/check_env_pins.sh`) |
  | 8 | Run affected behavioral tests in isolation | `changed_tests` | `changed_tests` | `run` (detached `git worktree`; `PYTHONPATH` the worktree; `git diff --exit-code`; empty untracked status) |
  | 9 | Run product mechanics and ordering lane | `product_lane` | `product` | `run` |
  | 10 | Run CLI and compatibility lane | `compat_lane` | `compat` | `run` |
  | 11 | Run database and runtime-contract lane | `db_lane` | `db` | `run` |
  | 12 | Run rails policy and secret-safety lane | `rails_lane` | `rails` | `run` (includes `tests/evidence/test_rails_ci_workflow_integration.py`) |
  | 13 | Run governed evidence integrity lane | `evidence_lane` | `evidence` | `run` |
  | 14 | Run approved generic QA subsystem lane in isolation | `qa_lane` | `qa` | `run` (detached `git worktree`) |
  | 15 | Build and verify exact-source release attestation | `release_lane` | `release` | `run` (detached `git worktree`; attestation into `$RUNNER_TEMP`) |
  | 16 | Verify truthful applicability and clean candidate tree | `final_audit` | `always()` | `run` (env from `${{ steps.*.outcome }}` and the classify outputs; prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) |

- **Expressions used.** `${{ github.event.pull_request.base.sha || github.event.before }}`, `${{ github.event.pull_request.head.sha || github.sha }}`, `${{ github.event_name }}`, `${{ steps.classify.outputs.<flag> }}`, `${{ steps.<id>.outcome }}`, `${{ always() }}`, plus `$RUNNER_TEMP` and `$GITHUB_OUTPUT` in scripts.
- **`python -m pytest` commands.** They name 39 distinct `tests/...` tokens. The set of every `tests/` token anywhere in the file, by the guard test's own regex `tests/[A-Za-z0-9_./-]+`, is the same 39 (§5.4).

### 5.3 The classifier (`ci/checks/classify_ci_changes.py`, 2,057 lines, blob `e43181370783`)

- **CLI.** `--base BASE --head HEAD --event-name {pull_request,push} [--repo-root] [--github-output] [--changed-tests-output]`.
  - Both output paths are required: without them it exits 2 with `CI_CHANGE_CLASSIFIER_GITHUB_OUTPUT_MISSING` or `CI_CHANGE_CLASSIFIER_CHANGED_TESTS_OUTPUT_MISSING`.
  - Base and head must be full hexadecimal SHAs (`_validate_sha`).
  - `pull_request` compares the merge base with the head (`_comparison_base`).
  - Identical base and head return `_full("identical_refs_full_validation")`: all seven lanes and `_full_validation_test_targets()` (165 at the baseline).
- **Public functions the tool can delegate to.** `classify_paths(paths, *, governed_paths=None)` (raises `ValueError("CI_CHANGE_SURFACE_UNCLASSIFIED:<path>")`); `changed_test_targets(repo_root, paths)`; `classify_git_change(repo_root, base, head, *, event_name)`; `git_changed_paths`; `_load_governed_primary_paths(repo_root)` (reads `docs/evidence/INDEX.json`); `_full_validation_test_targets()`; `_registered_owner_test_paths()`; `LANES` (`product`, `compat`, `db`, `rails`, `evidence`, `qa`, `release`).
- **Full-validation inputs.** Prefixes `.claude/` and `.github/`. Paths `.gitignore`, `ci/checks/classify_ci_changes.py`, `pyproject.toml`, `pytest.ini`, `requirements-dev.txt`, `requirements.txt`, `tests/evidence/test_rails_ci_workflow_integration.py`. A change to the classifier alone selects all seven lanes.
- **Probes with the classifier's own functions** (no bytecode written; tree clean afterwards):

  | Path list | Result |
  | :- | :- |
  | `tools/ci/prepush_check.py` | refused: `CI_CHANGE_SURFACE_UNCLASSIFIED:tools/ci/prepush_check.py` |
  | `tests/tools/test_prepush_check.py` (file absent) | `selected_lanes`: `product`, `release`; no changed-test target |
  | `scripts/ingest/run_vendor_ingest.py` (WU-PR-05 F-5 registration, IF-35-3) | `db`, `product`, `release`; its owner `tests/bodygraph/test_ingest.py` is already in the db lane's list, so no separate target |
  | `VERIFY.sh` | `product` only, no target: OBS-P3-5 holds |
  | `engine/bodygraph/resolver.py` | `product`, `release`; five targets, not including `tests/bodygraph/test_vendor_prod_override.py`: OBS-P4-1 holds for the resolver half |
  | `docs/ephemeral/x.md` | `documentation_only`, no lane |
  | `ci/checks/classify_ci_changes.py` | all seven lanes |

- **CLI dry run** `822ce15..5e62a65`, `pull_request`: `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=3;lanes=none`; exit 0; `changed_tests=false`. The PF10 rename counts as two paths.
- **Path-filter test and O-14.**
  - `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths` passes (1 passed).
  - With one `pull_request` exception (`docs/run/PROD_ENDPOINTS.json`) removed from `ci.yml` in a scratch copy, it fails (1 failed); the file was restored and the copy's status was empty.
  - The test landed in `7136040` (#627).

### 5.4 Test inventory and coverage

| Set | Count |
| :- | -: |
| Tracked `tests/**/test_*.py` files | 214 |
| Reached by a `ci.yml` `python -m pytest` token | 49 |
| `_full_validation_test_targets()` | 165 |
| `_registered_owner_test_paths()` | 206 |
| `_FULL_VALIDATION_INACTIVE_TESTS` | 0 (empty) |
| `pytest.ini` `testpaths` entries | 80 |
| `ci.yml` `tests/` tokens in pytest commands / anywhere | 39 / 39 (equal) |
| **Uncovered set, binding definition (ID-7)** | **0** |
| Uncovered set, the guard's token set | 0 |

- `tests/tools/` exists with one file, `tests/tools/test_epic020_bundle_tool.py`, a registered owner and a full-validation target.
- **Reproduction target for ID-7, checked.** This IA computed the binding definition at `a429c7c` from that revision's own `ci.yml` and classifier, imported in a separate process from a throwaway `git archive` export with no bytecode written. The tracked set comes from `git ls-tree` of that revision. Result: 278 tracked test files, 39 pytest-command tokens, 94 full-validation targets, **135 uncovered**, equal file for file to the WU-PR-01 instruction §5.1 list. At `5e62a65` the same computation gives 0.

### 5.5 Release identity and Build Notes

- Admission (`load_active_mechanics_bundle()`): `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, 45 files, `1.3.0`. Manifest SHA-256 equals the `release_id`. `ADMITTED_RELEASE_ROSTER` has 45 paths, equal as a set to the manifest's `files`; `ADMITTED_RELEASE_VERSION` is `1.3.0`.
- `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` matches exactly one file: `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md`, SHA-256 `ca2d91c5dfe6ef9d0e643acee2280210bf6d846eca9748e63f1c7d78e6338e3e`.

### 5.6 Environment and packaging facts

- **Toolchain.** CPython 3.12.3 with CI's install; pytest 8.4.2; `ruby` 3.3.6 at `/usr/local/bin/ruby`; git 2.43.0.
- **PyYAML is not installed** by CI's install (`import yaml` fails; no `yaml` in `requirements*.txt`). The existing workflow tests read `ci.yml` as text (for example `_workflow_path_filters` and `_ci_lane_test_tokens` in the integration test).
- **Packaging.** `pyproject.toml` `[tool.setuptools.packages.find]` includes `engine*`, `adapter*`, `presenter*`, `catalog*`, `math*`; `tools/` is not packaged.
- **Layout.** `tools/ci/` does not exist. The existing `tools/` subdirectories are `audit`, `bodygraph`, `cli`, `config`, `diagnostics`, `errors`, `evidence`, `ops`, `order`, `presenter`, `qa`.
- **Ignore rules.** `.gitignore` ignores `.venv/`, `__pycache__/` and `*.pyc`.
- **Release lane.** `tools/evidence/build_release_attestation.py` builds its wheel with `pip wheel --disable-pip-version-check --no-index --no-build-isolation`.
- **CI pre-checks.** `python3 ci/checks/check_agents_md_citations.py` printed `AGENTS_MD_CITATIONS_OK`, exit 0. `ci/checks/check_env_pins.sh` printed `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC`, exit 0.

### 5.7 Hidden repository writes, measured in a throwaway clone of `5e62a65`

| Operation | Effect | `git status` shows it |
| :- | :- | :- |
| `import ci.checks.classify_ci_changes` with bytecode writing on | creates `ci/checks/__pycache__/` | no (ignored) |
| `git status` after touching a tracked file's timestamp | rewrites `.git/index` (new mtime and new bytes) | no |
| `GIT_OPTIONAL_LOCKS=0 git status` after the same touch | `.git/index` unchanged | no |
| `git worktree add --detach <dir> HEAD` | creates `.git/worktrees/<name>` in the source repository; `git worktree remove --force` deletes it again | no |

### 5.8 Replay feasibility

@@REPLAY_DETAIL@@

### 5.9 Hosted CI reference

On #656's final head `f7d610e` (code equal to `5e62a65`), check run 117798448239 of run 39169173040 took 20 min 55 s (21:44:36Z to 22:05:31Z). The classification (`reason=selected_lanes`, 83 paths) selected all seven lanes, and the changed-test step ran 166 targets:

| Step | Duration | Result |
| :- | :- | :- |
| changed tests | 6 min 41 s | 3,914 passed |
| product | 12 s | 77 passed |
| compat | 11 s | 119 passed, 3 skipped, 2 xfailed |
| db | 12 s | 269 passed |
| rails | 43 s | 120, 113, 155 and 138 passed |
| evidence | 9 min 27 s | 130 passed |
| qa | 24 s | 488 passed |
| release | 2 min 37 s | 79 passed, then the attestation built and verified |

### 5.10 Full `tests/` sweep at `5e62a65`

@@SWEEP_DETAIL@@

## 6. Bounded files and components

| Path | Bound |
| :- | :- |
| `tools/ci/prepush_check.py` (new; the first file under `tools/ci/`) | the tool (ID-1 to ID-9) |
| `tests/tools/test_prepush_check.py` (new, in the existing `tests/tools/`) | the owner test (ID-10), with any fixtures it creates at run time under `tmp_path` |
| `ci/checks/classify_ci_changes.py` | the smallest registration for the new path and its owner test (ID-10) |
| `tests/evidence/test_rails_ci_workflow_integration.py` | only where a pin enumerates the registry the new entry joins (ID-10) |
| `docs/ephemeral/` PR result records | evidence obligations (§10) |

Expected unchanged, so that a needed change is a finding under §14:
- `.github/workflows/ci.yml` and every other workflow; `ci/jobs/*.yml`; `ci/checks/*` other than the classifier;
- `requirements*.txt`, `pyproject.toml`, `pytest.ini`, `.gitignore`;
- every release member and `catalog/manifest.json`; `engine/config/registry_loader.py` (admission constants and roster);
- every governed evidence artifact, the Index and Mirror, path proofs and every frozen family; `tools/evidence/**` and every other existing tool;
- every existing test file other than the pin file above;
- `README.md`, `AGENTS.md`, `CHANGELOG.md`, `docs/**` outside `docs/ephemeral/`; `docs/pfcanon/**`;
- `.claude/**` and any git hook.

## 7. Exclusions

- **Hooks.** No git hook of any kind is installed, written or suggested by the tool: no `pre-push` hook, despite the name. No SessionStart hook (Specification Exclusions) and no `.claude/` change.
- **Writes.** No write to the repository as ID-2 defines it.
- **Network.** No network: no `pip`, `git fetch` or installer; closed rails for every child (ID-9).
- **Dependencies.** No new dependency. `requirements*.txt` and `pyproject.toml` are outside the Plan's three deliverables (§6), and the replay reads `ci.yml` with the standard library (ID-8).
- **CI.** No new workflow, job, step or lane; the tool is not added to CI. Only its owner test runs, through the registration.
- **Classifier.** No classifier rule other than the new path's registration. The carried gaps stay (ID-11).
- **Release and evidence.** No release member, manifest, admission constant, evidence family, acceptance token or governed artifact change. The tool's output is not evidence (ID-1).
- **Documents and canon.** No `README.md`, `AGENTS.md` or `CHANGELOG.md` edit (WU-DOC-01 documents usage). No canon edit and no PF10 addendum.
- **Live and production.** No live vendor, production or database call; no deployment.
- **Tests.** No skipped, disabled, expected-failure or quarantined test. No write-mode run of any owner tool, frozen-family generator, the EPIC030 generator or the EPIC036/EPIC037 generators, in the repository or by the tool.

## 8. Interface contracts with other units

| Contract | Consumer | Content |
| :- | :- | :- |
| G-1 Usage | WU-DOC-01 ("pre-push check usage" in `README.md`); every later PR session | the command, report names, arguments, environment prerequisites (CI's install, `ruby`), exit rule and nonclaims, as the PR result record states them |
| G-2 Coverage definition | WU-PR-01's guard; any later change to coverage | the binding definition of ID-7 and the token-set pin. A pull request that changes how coverage is derived records the new definition and updates the tool in the same pull request |
| G-3 Replay inventory | any later pull request that adds, renames or removes a `ci.yml` step | the inventory pin of ID-8 fails until the tool knows the step; that pull request updates the tool |
| G-4 Classifier registration | later classifier changes | the new path's entry (ID-10) |
| G-5 Nonclaims | every user | the tool's green is not CI's green and not QA; its output is not evidence |

## 9. Disposition rules PR-20 must apply and record

1. **Choices left to PR-20,** each recorded with its reason (C5):
   - the argument syntax and output format (ID-1);
   - the copy mechanism and how it writes nothing to the repository (ID-2);
   - how `sweep` reproduces the 135-file set (ID-7);
   - the replay parser, whether full validation gets a named option, and how the interpreter and installed package are shown (ID-8);
   - the registration form (ID-10);
   - how the owner test stays fast and how it checks byte identity, ignored files and `.git` included (ID-10).
2. **Prototype** the tool and its test in a throwaway copy. Run every report there at least once. Record each report's output, exit status and duration, and the byte-identity check of the copy's repository before and after.
3. **Baseline re-check.** Re-measure §5.2 to §5.4 at the plan's head. Any difference in step names, token sets or the uncovered set is recorded and handled before planning edits.
4. **Carried items.** Record each item of §15 with its disposition.
5. **Stale documents.** Name any document the tool makes stale but this unit may not change, with its owner (WU-DOC-01 or the Product Owner).

## 10. Acceptance, tests and evidence

**Plan v1.1 §7 WU-PR-06 acceptance, verbatim**, with the binding readings in brackets:
1. "Each IF-9 report runs and the repository tree is byte-identical before and after (asserted by the tool and by its test)." [The tool asserts a clean tree and an unchanged `HEAD` before and after (ID-3). The test asserts the stronger rule of ID-2 for every report: files, ignored files included, and `.git` state.]
2. "`lanes` output equals the classifier's for the same inputs; `membership` matches `ADMITTED_RELEASE_ROSTER`; `build-notes` resolves exactly one `docs/pfcanon/PF10-HDE-Build-Notes-v*.md` and prints its SHA-256; `sweep` reproduces the Audit §3(b) set and runs it in a throwaway export; `replay` covers every lane step name in `ci.yml` (pinned by the test)."
   - `lanes`: both modes, refusals included (ID-4).
   - `membership`: ID-5.
   - `build-notes`: zero and several matches fail (ID-6).
   - `sweep`: the binding definition; 135 files at `a429c7c` and 0 at the head; non-empty fails (ID-7).
   - `replay`: every step of the `test` job executed or excluded with a reason; the pin (ID-8).
3. "No hook, no writes, no network." [§7; ID-2; ID-9.]
4. "Lanes green (full validation, classifier changed)." [Hosted CI on the exact head: all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.]

**Evidence obligations.** The Plan says "PR result record with one captured run". Read here as one captured run of every report at the candidate head, recorded in the PR result record. The record holds:
- `lanes` for the pull request's own base and head, and for a given path list that includes one refused path;
- `membership` for a list with a member and a non-member;
- `build-notes`;
- `sweep` (0 at the head) and the 135-file reproduction at `a429c7c`;
- `replay` of the pull request's base and head, and one full-validation replay;
- each report's exit status and duration;
- the byte-identity check of the repository before and after the captured runs;
- each check actually run, with counts;
- the registration;
- the carried items' dispositions (§15);
- the nonclaims (§12).

**Validation PR-20 plans** (minimum). Every item ran at the baseline in its read-only form (§5); the new test, the negative controls and the captured runs need the tool to exist:
- the full `tests/` sweep in a detached copy with `ruby`, `bash` and `curl` on `PATH`, under the closed-rails profile, with `XDG_STATE_HOME` pointed at an empty scratch directory, and with the editable install mapping to the copy under test (OBS-W5-5);
- the seven lanes as `ci.yml` writes them, which a full-validation `replay` by the new tool performs;
- the classifier dry run on the pull request's base and head, expecting all seven lanes;
- `tests/evidence/test_rails_ci_workflow_integration.py` (the coverage guard, the path-filter test and every pin) and `tests/evidence/test_http_reader_ci_ownership.py`;
- the new owner test, alone and in the changed-test step;
- the negative controls of ID-10.

Each run that can write tracked files runs in a detached copy and ends with `git diff --exit-code` and an empty untracked status.

| Requirement | Acceptance item | Proof | Stage |
| :- | :- | :- | :- |
| S20 "one read-only command" | (1), (3) | the owner test's byte-identity and hook checks; the captured runs' before/after check | PR-30; CI; PR-40 |
| S20 "CI lanes … for given paths" | (2) `lanes` | equality tests; captured runs | PR-30; CI |
| S20 "release membership for given paths" | (2) `membership` | roster test; captured run | PR-30; CI |
| S20 "the current Build Notes path and hash" | (2) `build-notes` | uniqueness tests; captured run | PR-30; CI |
| S20 "the uncovered-test sweep run in a throwaway copy" | (2) `sweep` | definition and token-set tests; the 135/0 reproduction | PR-30; PR-40 |
| S20 "a `ci.yml` replay in a throwaway worktree" | (2) `replay` | the inventory pin; the captured replays | PR-30; CI; PR-40 |
| Constraint "Duplication" | (2) pins | G-2, G-3 | PR-30; later units |
| Lanes and classifier | (4) | hosted CI on the exact head, all seven lanes | PR-35 |

## 11. Migration and security constraints

- **Migration:** none.
- **Rollback:** Nathan's revert of the squash commit. No member changes, so no refresh.
- **Security:**
  - Read-only by construction (ID-2) and closed rails for every child (ID-9). No secret, token, key value, birth input, location or user identifier appears in the tool's output, a test, a record or a commit.
  - Given paths are validated as the classifier validates them (`_normalized_path`: no empty, absolute, `..` or control-character path) before any use. Paths and SHAs go to subprocesses as argument vectors, never through a shell string.
  - The replay runs `ci.yml`'s own `run:` text in the throwaway copy. That is the same code CI runs on that head, and it runs nothing else.
  - The temporary directory is created owner-only and removed at exit.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, the classifier, `ci.yml`, the integration test and canon on `main`;
  - re-checks the baseline (§9.3);
  - prototypes in a throwaway copy;
  - writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`: the design choices of §9.1 with reasons, the requirement-to-change/test map, ordered steps, validation, risks and recovery;
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan):
  - recovers existing work first and implements only the planned files;
  - tests locally under §10 and captures the runs of §10;
  - commits coherently;
  - publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings (PF10 addendum 2.3: the Codex security review is not part of the chain);
  - retests, and pushes coherent corrections (ID-12 for a correction outside the change set);
  - verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
  - returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage and, on ACCEPT, selects the next unit (WU-PR-07).
- **Attributable lineage:** the PR result records, the PR reference and the squash commit.
- **Nonclaims** every record keeps:
  - the tool's green is not CI's green and not QA (Plan);
  - its output is not governed evidence;
  - no QA verdict, acceptance, Ops, deployment, PF09 movement or closure;
  - no canon edit.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- **A failed prototype or captured run** leaves the repository untouched by design (ID-2). Remove the temporary directory and run again.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version, never an edit of v1.0.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or budget, schedule or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions), and this IA reviews it through RS-20. The decision returns to the PR-20 planning context.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:**
  - a needed change in an "expected unchanged" path of §6, for example `ci.yml` or a new dependency;
  - a report that cannot meet ID-2 or ID-9 within the Plan's deliverables;
  - a reading of ID-1 to ID-12 that PR-20 believes conflicts with canon.
- **Not a trigger:** an in-scope correction recorded under ID-12, and a design choice §9.1 leaves to PR-20.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| The design choices of §9.1 | PR-20 session | In the plan |
| F-5: WU-PR-05's classifier registration `"scripts/ingest/run_vendor_ingest.py": ("tests/bodygraph/test_ingest.py",)` in `_PRODUCT_TEST_OWNER_PATHS` (IF-35-3) | this unit: `lanes` delegates, so it reports the registration as the classifier applies it (§5.3) | Carried; nothing to change |
| C-3 coverage definition and LR O-1 (the guard's wider token set) | this instruction (ID-7) | Settled here |
| C-4 lane names and step structure | this unit (ID-8 pin) | Carried |
| C-6 owner-registry shape | this unit (ID-10) | Carried |
| OBS-P4-1, OBS-P3-5 (classifier gaps) | this unit surfaces them (ID-11); Product Owner for the gaps as later classifier change candidates | Re-measured; carried |
| O-14 (S19 record) | none | Does not reproduce (ID-11; §5.3) |
| The `ruby` requirement (addendum 2.2); O-6 (hosted `ruby` version unprinted); `ruby` on hosted runners after `ubuntu-latest` moves to Ubuntu 26.04 (addendum 2.2 "Unresolved obligations and owners": unknown) | this unit (ID-9: missing `ruby` is a tooling failure); PR-35 records the hosted version and image if a job log shows them | Carried |
| OBS-W5-5: `hdctl` subprocess tests use the installed package | this unit (ID-8 interpreter report; §10 sweep environment) | A hazard here |
| OBS-W5-3 and S19-R04: owner tools that act on any invocation, `--help` included; the EPIC030 generator rewrites tracked files | this unit (ID-8 runs only `ci.yml` text; §7) | A hazard here |
| OBS-P4-2 and OBS-P4-7: route-policy tests that depend on an ambient `APP_ENV`; `tests/adapter/test_jsonschema.py`'s `ENGINE_ENV` leak | this unit (the replay and sweep set `APP_ENV=dev` from `ci.yml`); the leak's fix stays with a later owner through the IA | A hazard here |
| OBS-4 (WU-PR-01): `tests/evidence/test_bodygraph_policy_proofs.py` (nine paths) and `tests/reader_v1/test_release_pack.py` (`artifacts/release_id.txt`, `artifacts/release_pack_manifest.json`) rewrite tracked files with identical bytes; `git diff` and `git status` cannot see it | this unit (byte identity is content; the sweep and replay run tests only in a copy) | A hazard here |
| OBS-14 (WU-PR-01): `test_epic034_presenter_bypass_detects_imported_adapter_helper` in `tests/evidence/test_hdapi_v2_contract_inventory.py` writes `adapter/boundary_tmp_helper.py` and `adapter/boundary_tmp_route.py` under the repository root while it runs, then removes them (still so at `5e62a65`) | this unit (the sweep and replay run tests only in a copy, never in the session's checkout) | A hazard here |
| OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` | QA tool and test owner, through the IA; Product Owner to route | If the qa lane or a replay shows it, it is recorded as OBS-17, never "fixed" here |
| The current `release_id` `77204764…` and the 45-member roster | this unit (`membership`) | Carried |
| The current PF10 file | this unit (`build-notes`, by pattern, ID-6) | `v13.6.1` at the baseline |
| LR5-O2 lesson | this instruction (ID-12) | Applied |
| LR4-O3 lesson (run every check the instruction lists) | this instruction (§10 validation list ran at the baseline) | Applied |
| WU-PR-01 O-2, O-3, O-4, O-5 and the carried OBS items of WU-PR-01 | their owners as WU-PR-01 lineage review v1.0 §6 names | Not this unit |
| S19-R01 to S19-R07, X-01 to X-04, LR5-O1, LR5-O4's later-change candidates | Product Owner and the named owners (addendum 2.10) | Not this unit |
| AQ-1 | Product Owner | WU-PR-07 only |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- The Plan's "throwaway worktree" and "throwaway export" and the Specification's "writing nothing to the repository" are read together under ID-2. A copy outside the repository satisfies both; a registered `git worktree` would write to the repository. Glow QA Guide §2.2.11's non-mutation rule supports the reading.
- The Plan's "`sweep` reproduces the Audit §3(b) set" and the WU-PR-01 instruction's binding definition agree under ID-7. Both name the same computation, which gave 135 at `a429c7c`.
- Canon is silent on git hooks and pre-push tools. Silence is not a conflict; the Specification's Exclusions govern.

Coverage read for this instruction (in this invocation):
- Glow QA Guide §2 "Pre-commit QA (local/CI)" in full (§2.1 to §2.2.11);
- HDE Mechanics Guide §1.2 "CI default CLOSED & evidence";
- Change Process Guide §0.2 in full;
- Plan Templates "CI lane classification and automated budget-control discipline" in full, and "Repository loci and file minting" in full;
- HDE Governance §9.1.1 in full;
- whole-canon searches for pre-push, pre-plan, hooks (git, SessionStart, pre-commit), CI lane budget control, replay, throwaway copies and the Build Notes file.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S20 "One read-only command" | one tool a session runs on demand; it writes nothing | ID-1; ID-2; ID-3 | WU-PR-06 | (1), (3) | PR-30; CI; PR-40 |
| S20 "reports CI lanes … for given paths" | the classifier's answer, not a copy of it | ID-4 (both modes, refusals) | WU-PR-06 | (2) | PR-30; CI |
| S20 "release membership for given paths" | roster membership | ID-5 | WU-PR-06 | (2) | PR-30; CI |
| S20 "the current Build Notes path and hash" | the unique PF10 file and its SHA-256 | ID-6 | WU-PR-06 | (2) | PR-30; CI |
| S20 "the uncovered-test sweep run in a throwaway copy" | WU-PR-01's coverage definition, computed at the head and run outside the repository | ID-7 (C-3, O-1; 135/0) | WU-PR-06 | (2) | PR-30; PR-40 |
| S20 "a `ci.yml` replay in a throwaway worktree" | what CI would run, read from `ci.yml`'s text, in a copy | ID-8 (inventory, pin, conditions, full validation) | WU-PR-06 | (2) | PR-30; CI; PR-40 |
| S20 "writing nothing to the repository" | no file, ignored file or git metadata changes | ID-2 (three measured hazards, §5.7) | WU-PR-06 | (1), (3) | PR-30; CI |
| Constraint "Duplication" | the tool tracks `ci.yml` | pins G-2, G-3 | WU-PR-06 and later units | (2) | PR-30; later PRs |
| Exclusion "No SessionStart hook" | no hook of any kind | §7 "Hooks" | WU-PR-06 | (3) | PR-30; PR-40 |
| IF-9 "exit 0 only when every requested report succeeds" | a failed report fails the run | ID-1; ID-7 status rule | WU-PR-06 | (1), (2) | PR-30 |
| Plan (4) "full validation, classifier changed" | all seven lanes on the exact head | ID-10 | WU-PR-06 | (4) | PR-35 |
| Addendum 2.2 "sweep environment must provide ruby" | `ruby` present, or a tooling failure | ID-9; §10 | WU-PR-06 | (2) | PR-30 |
| Addendum 2.10 carried list | every carried item placed | §15 rows; ID-11 | WU-PR-06 | — | PR-10 (here) |

Checks against the full PR-20 contract:
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries everything PR-20 needs:
  - the Specification, Audit, Plan and review lineage;
  - the PF10 path and overlays;
  - the baseline, loci, exclusions, interfaces and dependencies;
  - acceptance, evidence, migration and security;
  - recovery, rescope, merge ownership and the return owner.
- PR-20's step 2 forbids mutating the repository while planning. Its prototype runs in a throwaway copy, and its only writes are its own artifacts.
- Numeric domains and sentinels:
  - exit codes: 0 only when every requested report succeeds (IF-9);
  - `sweep` set size: 0 is success, any positive count fails (ID-7);
  - no boolean is introduced into a numeric field.
- Closed schemas: the classifier's `--github-output` key set is fixed (§5.3), and `lanes` reproduces it exactly.
- No decisive comparison fails. Every fact in §5 was measured at `5e62a65` by this IA. Every check §10 lists ran at the baseline in its read-only form (lesson LR4-O3).

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-06 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:**
  - PR-40 lineage review after Nathan's merge;
  - rescope review through RS-20;
  - same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-06)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan, not yet reviewed, for one work unit of an approved change: a new read-only pre-push and pre-plan command-line tool of a few hundred lines with five independent sub-reports (CI lane classification delegated to the existing classifier for given paths or a base and head, release membership of given paths, the current build-notes file and its hash, an uncovered-test sweep run in a throwaway copy, and a replay of every CI workflow step read from the workflow text in a throwaway copy), one new owner test module that proves each report and that nothing in the repository is written, and one classifier registration. A ready instruction lists the files, contracts, baseline and test-environment hazards; the planner prototypes in a throwaway copy, no live provider call occurs, and a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.35 (confidence 0.71); rung probabilities low 0.01, medium 0.03, high 0.60, extra high 0.33, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.19, Opus 5.5 0.66, Sonnet 5.5 0.15, Haiku 5.5 0.00 (confidence 0.55). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.002, Fable 5.1 at medium 0.006, Fable 5.1 at high 0.114, Fable 5.1 at extra high 0.063, Fable 5.1 at max 0.006, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.007, Opus 5.5 at medium 0.020, Opus 5.5 at high 0.396, Opus 5.5 at extra high 0.218, Opus 5.5 at max 0.020, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.002, Sonnet 5.5 at medium 0.004, Sonnet 5.5 at high 0.090, Sonnet 5.5 at extra high 0.050, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-19T01:29:58Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-19T01:29:58Z; HTTP 200 in 0.65 s; 5528 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 (`request-v8.2.json`, sha256 `62486fcc4357e5917c3e9ba3e1ba9e2709364f0338dde70d4a88b116022b22ec`) and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records.** The Notion row was not written, as PR-10 directs. Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is WU-PR-05 lineage review v1.0 §11.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.**
  - The baseline re-check, the prototype and the sweep need Python 3.12 with CI's install (package-index access for `pip install -r requirements-dev.txt`), `ruby` on `PATH` for the contract-inventory test, `bash`, `curl` and git.
  - Run under closed rails with the vendor, database and GitHub keys unset; the container sets several of them.
  - Work in throwaway clones outside the session's checkout, and point the editable install at the copy under test before a sweep or replay (OBS-W5-5).
  - The 135-file reproduction needs history back to `a429c7c`. A shallow clone lacks it; `git fetch --deepen=400 origin main` reached older history earlier in this lineage.
- **Run times observed.**
  - A full `tests/` sweep: about 17 to 28 minutes in this lineage, depending on concurrency.
  - A full-validation replay: @@REPLAY_TIME@@.
  - Hosted CI on the same code: 21 minutes.
- **Access.** No live vendor, production or database access is needed.
- **Order.** This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-06 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-06 (S20) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z). Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | @@CREATED@@ |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | WU-PR-05 lineage review v1.0 §12 (PR-40) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `5e62a65` (`docs/pfcanon/` last changed by `5e62a65`, the PF10 rename; every other PF file unchanged since 2026-10-09).

| Topic | Sources and sections |
| :- | :- |
| Instruction authority, content and readiness | PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1 ("Inputs", "Working rules", "Authoritative PF10 and overlay input", "Execute", "Required result", "COMPLETE APPROVED-SCOPE PLAN → PR-30"; the receiver contract); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (read in full: PR Instructions are the IA's; Proceed per detailed PR plan; PR merges remain Product Owner actions) and §9.1.2 (canon precedence over in-flight documents; ID-1 to ID-12 rest on it) |
| Overlays and carried items | PF10-HDE-Build-Notes v13.6.1 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.1.md`): addendum 2.10 in full (the list carried into this instruction; LR5-O2 and LR5-O5); 2.2 in full ("Affected surfaces": the coverage definition contracted to WU-PR-06 and the `ruby` requirement); 2.3 in full (Rules 1–5); 2.4 in full (WU-PR-01 acceptance; C-1 to C-6; O-1 to O-6); 2.5 in full (OBS-17; record commits select lanes base to head); 2.9 (OBS-P4-1); 2.1 (§19); 2.6 to 2.8 for applicability (no member change, no refresh) |
| Non-mutation, rails and failure classes (C1–C3) | Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §2.2.5 "Tooling vs behavior failures (pytest and harnesses)", §2.2.6 "Rails posture in CI (default CLOSED)", §2.2.11 "Evidence-governed CI sequence (names-only)" ("A non-writing check MUST NOT mutate the repository or external state"), and §2 in full; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.2 "CI default CLOSED & evidence" |
| Classifier and CI scope (C4, C5) | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.2 (a validly reduced lane set with a passing final applicability audit is sufficient CI evidence); Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "CI lane classification and automated budget-control discipline" (repository-owned validation tooling as durable control; a plan or review does not invent a tool's mechanism) |
| Loci and tool output (C6) | Plan Templates "Repository loci and file minting" (file minting within established homes; `tools/` output is non-governed tooling output unless bound to an evidence family) |
| Coverage definition and lane structure | WU-PR-01 instruction v1.0 §5.1 and §8 (C-3, C-4, C-6); WU-PR-01 lineage review v1.0 §5 and §6 (O-1, O-4, O-6) and v2.0; WU-PR-01 plan v1.1 OBS rows (OBS-3, OBS-4, OBS-14) |
| In-flight documents | Specification v1.1: row S20, constraints "Duplication" and "Uncovered tests", Exclusions, the Live QA class table, the Distillation phase row; Plan v1.1 §3, §5 IF-9, §6, §7 (common paragraph; WU-PR-01, WU-PR-06 and WU-DOC-01 blocks), §9 item 4, §12, §14; review v1.1 (no note for this unit); Audit §3, §5.2, §5.3, §6 S03 and S20, §7.1 EC-9, §7.5; candidate item briefs v1.2 and kickoff, item 7 (origin only); WU-PR-03 plan v1.0 (OBS-P3-5); WU-PR-04 plan v1.0 §17 (OBS-P4-1, OBS-P4-2, OBS-P4-7); S19 record v1.0 §7 (O-14) and §4 (S19-R04); WU-PR-05 instruction v1.0 (structure; OBS-W5-3, OBS-W5-5) and lineage review v1.0 (§7, §8) |
| Operative documentation | `AGENTS.md`: canon-first rule; closed rails and redaction; pytest readiness; "Search tooling note" (`rg` absent); "Ordinary CI is the one `test` job … seven change-aware lanes … final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`"; "Release identity"; PR descriptions; "Code review guidelines" and "Code review scope" (Markdown and `docs/ephemeral/` outside the Codex code review); "Truncation/retrieval-failure guardrail" (exit codes captured from the producer) |

Silence: canon names no git-hook, pre-push or SessionStart rule (whole-canon search); the Specification's Exclusions govern.
