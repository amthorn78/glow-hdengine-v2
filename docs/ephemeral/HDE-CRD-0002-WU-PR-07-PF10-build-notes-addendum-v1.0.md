---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-07-RESCOPE-1
proposed_pf10_number: "2.13 (next continuous number after addendum 2.12 of the current controlled PF10; allocation and publication are the Product Owner's)"
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (RS-20; selected version 100926.1, release GCFPE-20261009.1; https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c)
approval_decision: HDE-CRD-0002-WU-PR-07-RESCOPE-REVIEW v1.0, decision APPROVE, docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md
immutable_base: HDE-CRD-0002-SPECIFICATION v1.1 (SPECIFICATION_APPROVED, Thoth CF-C-30; docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md) → HDE-CRD-0002 Implementation Plan v1.1 (approved by IA-30 review v1.1, Isis; docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md and docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md) → HDE-CRD-0002 WU-PR-07 PR instruction v1.0 (INSTRUCTION_READY; docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md)
applicable_prior_addenda: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md §2.11 (read with §2.12's numbering), §2.12, §2.5, §2.3. None is superseded
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (v13.6.3; blob 41d5cfd2da6d; SHA-256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35; addenda 2.5, 2.6, 2.11 and 2.12 read in full; provenance, not a gate)
originating_proposal: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0.md (RESCOPE_PROPOSAL v1.0, finding F-1, from the dedicated WU-PR-07 PR engineering session at PR-20 pre-Proceed planning, through RS-10), with docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0-prototype.diff (SHA-256 e786b30ba2719cebcf7a8808edb5423e0c21c4db17dbef37ba9ecb529cf70149)
return_phase: PR-20 planning context of the dedicated HDE-CRD-0002 WU-PR-07 PR engineering session (pre-Proceed; no Proceed, vehicle or pull request for code exists; PR_RETURN_PHASE not applicable)
capture_time_utc: 2026-10-20T15:50:00Z
normalized_approved_delta_digest: not computed (no governed normalization procedure exists; none is invented)
---

## 2.13 HDE-CRD-0002 WU-PR-07: the closeout-validation job installs the repository's runtime requirements, so its read-only evidence checks can pass

Timestamp: 102026 15:50 (UTC). Details: Records the whole-change Implementation Agent's approval, through Review Bounded Work-Unit Rescope, of one bounded implementation rescope of work unit WU-PR-07 (requirement S21: the close-pack writer for Epic and CRD identities, the close-run evidence home and the ADR draft) of the approved HDE-CRD-0002 Implementation Plan v1.1.
- Origin: the WU-PR-07 rescope proposal v1.0 (finding F-1, items D-1 and D-2) from the dedicated PR engineering session during pre-Proceed planning, written at the Product Owner's direction "Option A, write the rescope proposal".
- Evidence: the review's own reproduction at `main` `a9fd343`, in throwaway clones with two fresh interpreters, of the failing step and its correction; the plan v1.0 rehearsal of the close sequence; the GitHub Actions record of the workflow (0 runs).

### Decision and approval status

The continuing whole-change Implementation Agent for HDE-CRD-0002 decided `APPROVE` on the WU-PR-07 rescope proposal v1.0, as one state for the one proposal. The decision record is `docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md`.

The approval is a bounded implementation rescope within the approved Specification's intent. It does not change the Epic-level commitment, any Specification acceptance criterion, any protected boundary, any other work unit, any accepted dependency or any Product Owner matter. The immutable base is not rewritten.

This addendum is the one overlay the approval creates. The effective baseline for WU-PR-07 is the approved base, plus addenda 2.11 (read with 2.12's numbering), 2.12, 2.5 and 2.3, plus the Product Owner's business-case disposition of 2026-10-20, plus this addendum.

No canon-conflict register entry is created or changed.

### Base

The base is not changed. Its relevant clauses are:
- **Specification v1.1:** requirement S21 and its acceptance intent ("The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has a home …; the accompanying ADR is approved"); the constraint "Close-pack writer", which states that "S21 touches the release-sanity and close-validation lanes".
- **Implementation Plan v1.1, WU-PR-07:**
  - Deliverables, which name `.github/workflows/epic-closeout-validation.yml` "only where they read the schema version";
  - Terminal-state reachability (e): HDE-CRD-0002's close dispatches that workflow on the exact close head (T7) before the Product Owner merges.
- **WU-PR-07 PR instruction v1.0:**
  - §6 lists the workflow as expected unchanged;
  - §7: "No CI change. No new workflow, job, step or lane; the validation workflow and release-sanity stages stay as they are (ID-10)";
  - ID-10: "The job also runs the updater's `--check`, `orientation_demo.py --check`, the hash, path, Mirror-schema and final-LF checks. ID-9 keeps them passing before HDE-CRD-0002's close pack exists";
  - contract H-6;
  - §14 names a needed change to the validation workflow as an expected rescope trigger.

### Finding

The closeout-validation job cannot pass its step "Run retained read-only evidence checks" for any candidate.
- **The install.** The job installs only `jsonschema==4.23.0`.
- **The import.** `tools/evidence/update_evidence_index.py --check` runs `_validate_epic038_pr02_semantics`, which imports `tools/evidence/generate_a7_transport_proofs.py`. That reaches `adapter/http_reader.py`, which imports Flask at module level.
- **Measured at `main` `a9fd343`**, under the job's own environment with a `jsonschema`-only interpreter: the updater's `--check` exits 1 with `ModuleNotFoundError: No module named 'flask'`. The other five read-only checks exit 0.
- **On the plan's rehearsal of a real close state,** the writer's `--check` exits 0 and the updater's `--check` fails the same way.
- **History.** The import entered the updater on 2026-07-28 (#375), before the workflow was added on 2026-08-21 (#396, HDE-EPIC039 PR-05). The step has therefore never been passable. The workflow has never been dispatched.
- **Effect.** Without a change, T7 fails for HDE-CRD-0002's close and for every later close. The business-case measure for WU-PR-07 ("every check mode passes … on the first attempt") cannot be met.
- **Instruction premise.** Instruction v1.0 ID-10's statement that those checks pass was not measured under the job's install and is false.

### Approved delta

1. **D-1.** In `.github/workflows/epic-closeout-validation.yml`, the install step changes from `- name: Install bounded validation dependency` / `run: python -m pip install 'jsonschema==4.23.0'` to `- name: Install the read-only checks' runtime requirements` / `run: python -m pip install -r requirements.txt`. Nothing else in the workflow changes: the triggers, inputs, permissions (`contents: read`), checkout (`persist-credentials: false`, exact ref), environment, step count and order, the writer's `--check`, the six read-only checks and the clean-checkout assertions all stay as they are.
2. **D-2.** In `tests/evidence/test_rails_ci_workflow_integration.py`, the test `test_manual_closeout_validation_is_isolated_read_only_and_exact_head` gains four lines. They assert that the workflow has exactly one `python -m pip install`, and that it is `run: python -m pip install -r requirements.txt`.
3. **Bounded files.** WU-PR-07's bounded files gain exactly those two paths, each for exactly that change.
4. **Overlaid instruction clauses.** Instruction v1.0 is read as follows for WU-PR-07:
   - **§6:** the validation workflow leaves the expected-unchanged list for D-1 only. `.github/workflows/ci.yml`, every other workflow and `tools/evidence/run_sanity_pipeline.py` stay expected unchanged.
   - **§7:** "No new workflow, job, step or lane; the release-sanity stages stay as they are; the validation workflow changes only by D-1 (its install step installs `requirements.txt`)."
   - **ID-10:** the job installs `requirements.txt`, and its six read-only checks pass at the base and at the prototype head. ID-9 keeps them passing before HDE-CRD-0002's close pack exists. The writer and the v2 schema still keep standard-library plus `jsonschema` imports.
   - **Contract H-6:** "unchanged inputs; the job installs `requirements.txt` (D-1); the writer stays runnable with `jsonschema==4.23.0` alone".
   - **§14:** the rescope trigger for a needed change to the validation workflow no longer covers D-1. Any other change to that workflow remains a trigger.
5. **Validation.** The unit's validation adds three checks:
   - the job's seven checks, run with a fresh interpreter holding only `-r requirements.txt` on the rehearsal's terminal state, each exiting 0 with the checkout clean afterwards;
   - the writer's `--check`, run on that state with a `jsonschema`-only interpreter, exiting 0;
   - D-2's negative control: the new assertions fail against the unchanged workflow, and the test file passes with D-1 and D-2.
6. **Plan v1.1.** The unit's next planning artifact is plan v1.1, a complete successor of plan v1.0. It carries D-1 and D-2, F-1's disposition and the updated ceiling statement. Plan v1.0 and its prototype diff are preserved.

### Evidence

Each check below was run by the reviewer in throwaway clones under the job's environment: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0 GIT_NO_LAZY_FETCH=1`, with CPython 3.12.3.

| Check | Result |
| :- | :- |
| The six read-only checks at `a9fd343`, `jsonschema`-only interpreter | the updater's `--check` exits 1 (`No module named 'flask'`); the other five exit 0; checkout clean |
| The same six at `a9fd343`, interpreter with only `-r requirements.txt` and no editable install (Flask 2.3.3, gunicorn 21.2.0, jsonschema 4.23.0, psycopg 3.2.13) | all exit 0; checkout clean |
| The same six at the plan v1.0 prototype head (`a9fd343` plus the plan's companion diff), `requirements.txt`-only interpreter | all exit 0; checkout clean |
| The delta diff | applies to `a9fd343` and on top of the plan prototype |
| The workflow on the delta head, parsed with Ruby's YAML loader | 7 steps in the same order; `permissions: contents: read`; step 4 `python -m pip install -r requirements.txt` |
| D-2 against the unchanged workflow | the test fails (1 failed) |
| `tests/evidence/test_rails_ci_workflow_integration.py` with D-1 and D-2 | 138 passed (two runs; `main` unchanged also 138). One earlier run had 1 failure in an unrelated subprocess test that runs with a 120 s timeout; it passed on re-run and alone |
| GitHub Actions runs of `epic-closeout-validation.yml` | 0 |

From the proposal and plan v1.0, not re-run by the reviewer:
- on the rehearsal's terminal state C3, all seven of the job's checks exit 0 with a `requirements.txt`-only interpreter;
- the writer's `--check` exits 0 with a `jsonschema`-only interpreter.

### Scope, exclusions and nonclaims

- **Ceiling.** Within the adopted ceiling: one PR, at most 4 sessions or 3 days.
  - Either way the ceiling is counted, the projected total is 4 of 4 sessions, with no slack. Under the disposition's counting text, plan v1.1 is a repeat of the PR-20 stage; the proposal counts this review as session 3.
  - The Product Owner chose this option with that cost stated.
  - A projected pass of the ceiling is material and returns to the Product Owner before work continues.
- **Not changed:**
  - no Specification requirement, acceptance criterion or exclusion;
  - WU-PR-07 acceptance items (1) to (7);
  - instruction IDs other than ID-10, contracts H-1 to H-5, the other exclusions and the nonclaims;
  - AQ-1, the CI lanes and the PR-30/PR-35 split.
- **No other changes:**
  - no `ci.yml` change; the pre-push tool's `ci.yml` pin is unaffected;
  - no new workflow, job, step, lane, trigger, permission or secret;
  - no other unit's scope changes.
- **Not established:**
  - no hosted run of the job: its first run is HDE-CRD-0002's T7, because a dispatch needs a tracked candidate source on the exact head;
  - no live vendor, production or database call; closed rails throughout;
  - no QA artifact, QA verdict, acceptance, PF09 or PF30 status movement, deployment, canon edit, Product Owner Proceed, merge authority or closure follows from this addendum.

### Dependencies, conflicts and unresolved obligations

- **Dependency.** The delta lands in WU-PR-07's one implementation PR, after the Product Owner's Proceed against plan v1.1. AQ-1, the Product Owner's decision on the S21 ADR, still comes before that PR merges.
- **Conflicts.** None. Canon names no dependency rule for this job. The job keeps every property the operative workflow posture states: manual `workflow_dispatch`, read-only contents permission, exact-ref checkout, non-writing checks, clean-tree enforcement, no pull-request trigger, no credentials persistence, receipt, source writeback or hosted-result feedback.
- **Unresolved, with owners:**
  - plan v1.1: the WU-PR-07 PR engineering session;
  - the job's first hosted run at HDE-CRD-0002's T7: HDE-CRD-0002's close mutation set, with the Product Owner's dispatch;
  - the root cause of the one unrelated test failure observed in the reviewer's container, if it recurs on a hosted run: the WU-PR-07 PR-35 session.
