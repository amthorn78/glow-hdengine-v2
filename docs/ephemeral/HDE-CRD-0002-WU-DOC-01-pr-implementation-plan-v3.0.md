---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v3.0.md
artifact_version: "3.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 3, the bounded corrective pass for DOC-20 findings DC-1 and DC-2 (instruction v1.1)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0.md (cycle 2; Proceeded once and spent; landed as amthorn78/glow-hdengine-v2#695, squash cf8b759) and plan v1.0 (cycle 1; #692, squash 4c9bbfc), with their companion diffs. All preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
DOCUMENTATION_UNIT_ID: WU-DOC-01
work_unit_title: "Final repository documentation (DOC; after WU-PR-08)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.1.md (v1.1, INSTRUCTION_READY; landed by #698 as 892feeb)
originating_finding: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.0.md (DOC-20, INCOMPLETE; DC-1, DC-2)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-doc20-correction-v1.0.md §2
accepted_lineage: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT across #692 and #695). Accepted-final; not reopened
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-8)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db) — lineage only
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (unchanged; no ceiling, addendum 2.18)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved) → PR instruction v1.1 (issued by the IA under DOC-10)
effective_baseline: approved base + PF10 overlays — addendum 2.19 (P-8, the unit's scope), 2.21 (routed items, LR8-F2), 2.17 (the writer's nonclaims), 2.18 (business case without ceiling; the measure), 2.11 rules 4 to 8 and 2.14 (real inputs; finding disposition; P1), 2.3 (reviewer chain)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; unchanged on main at 892feeb)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.17, §2.18, §2.19, §2.21 (read in full in this session); §2.3, §2.11, §2.14 (as plan v2.0 records them)
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v3.0-prototype.diff (git diff 892feeb → prototype head 0a843cc; 4 files, +4/−4; 52 lines; 10,918 bytes; sha256 9fb7d91ea40efd527fa35946ec82cd224dd88ad2469900319a82cdd2bfb7c3a3; `git apply --check` clean on 892feeb)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: PRODUCT_OWNER_SELECTED_CONTINUING_CONTEXT. Nathan directed PR-20 to run in this session ("just do it here", 2026-10-22), instead of the new dedicated session instruction v1.1 §16 names
role_session_ref: https://claude.ai/code/session_017Tz88x3eecWgXvRf3dudTQ (PR-20 now; PR-30 after the Proceed)
context_conflict: this session is also the whole-change IA that issued instruction v1.1 (DOC-10) and that the instruction names as the PR-40 reviewer and DOC-20 verifier. Under the Product Owner's choice it now authors this plan, so PR-40 for cycle 3 would no longer be independent of the author if run here. Recorded, not resolved: who runs PR-40 for cycle 3 is the Product Owner's choice (§17)
author: this session, in the PR-20 role for WU-DOC-01 plan cycle 3
return_owner: the whole-change HDE-CRD-0002 IA (PR-40 after the merge, then DOC-20; RS-20 for a rescope; DOC-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state of 2026-10-12T02:29:47.327Z; Inputs, Execute, Required result and Next step read in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-22T04:05:00Z
repository_baseline: origin/main 892feeb4ec53c7c718b1ea1c2840fa7bc4755fb0 (#698). Outside docs/ephemeral/ the tree equals f3cc29e's, where instruction v1.1 measured
working_branch: claude/jolly-lovelace-89fdzx, restarted from 892feeb (its earlier commit landed as #698); this plan's records only
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for exactly this v3.0
---

# HDE-CRD-0002 WU-DOC-01 — PR Implementation Plan v3.0 (corrective, plan cycle 3)

## 1. Result

**AWAITING_PO_PROCEED for v3.0.** This is the complete plan for WU-DOC-01's third cycle: the four sentences of DOC-20 findings DC-1 and DC-2, as instruction v1.1 bounds them.

- **The work:** four sentence corrections in four files (§6), drafted to exact text. The companion diff carries them byte for byte; PR-30 applies it with `git apply`.
- **The prototype** passed every check in a throwaway clone of `892feeb` (§10):
  - the six document-reading test files: **1,248 passed** (CPython 3.12.3, CI's full install);
  - `AGENTS_MD_CITATIONS_OK` and `DIRECT_DB_CONTRACT_OK`;
  - `lanes`: `documentation_only`, 4 paths, no lanes; `membership`: all four not members;
  - only the four planned paths changed.
- **Probes** confirm both corrected facts (§10.3): the vendor client takes `RELEASE_ID` from the environment; the HTTP adapter ignores both names in the environment.
- **What stands:** everything #692 and #695 landed, apart from these four sentences.
- **Landed history:** #692 and #695. Their Proceeds are spent. PR-30 opens a new PR on a new branch and never pushes to either.
- **Not done here:** implementation, publication of the correction, merge, Ops, QA, acceptance or closure.

## 2. Lineage and sources read in this session

- Instruction v1.1 in full (this session issued it under DOC-10); the DOC-20 record in full; the decision record in full; instruction v1.0 in full; lineage review v2.0 in full; the business case in full.
- Plan v2.0, read for structure and its validation set (§1 to §18).
- PF10 addenda 2.17, 2.18, 2.19 and 2.21, read in full in this session.
- PR-20 — Create Detailed PR Implementation Plan — 100926.1: "Inputs", "Execute", "Required result" and "Next step and recovery", read in this session.
- The four documents at the target lines and their paragraphs; the code at §5's lines.

## 3. Business case and real inputs

- **Business case:** unchanged (business case record §2). The measure, "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20", is what §6 serves.
- **Real inputs** (addendum 2.11 rule 4): the four documents on `main`, which agents and operators read; an operator shell or service with `RELEASE_ID` set (DOC-20 §6, DC-2 "Real input").

## 4. Baseline (verified at `892feeb`)

- `origin/main` is `892feeb` (#698). `git diff --stat f3cc29e 892feeb -- . ':(exclude)docs/ephemeral'` is empty, so instruction v1.1's measurements at `f3cc29e` hold.
- **Recovery check:** no branch or open PR for cycle 3 exists. The local and remote branches are `main` and `claude/jolly-lovelace-89fdzx`, whose one commit landed as #698. No `…-pr-implementation-plan-v3.0*` or `…-pr-implementation-result-v3.*` existed under `docs/ephemeral/`.
- **The four target lines** read exactly as instruction v1.1 §6 quotes them: `README.md:13`, `AGENTS.md:143`, `CHANGELOG.md:7`, `docs/ADAPTER_009.md:48`.
- **No consumer** asserts any of the four sentences (instruction v1.1 §5.3; re-checked).

## 5. Facts re-measured (instruction v1.1 §5)

| Fact | Evidence at `892feeb` |
| :- | :- |
| 16 Epic close packs exist; none carries a writer manifest schema | `audit/*_MANIFEST.json`: 16 files, none has a top-level `schema_version`; writer schemas at `tools/qa/generate_epic_close_pack.py:43` and `:2190` |
| No candidate source; no close-run family | `git grep` for the four schema values as `"schema_version"` outside `tests/` and `docs/ephemeral/`: no hit; no `close/` directory under `audit/qa/` |
| Adapter ignores the environment for both names | `adapter/wsgi.py:14-15,31-32`; `adapter/logging_filter.py:46,65`; probe §10.3 |
| Vendor client reads `RELEASE_ID` from the environment | `engine/bodygraph/vendor_client.py:331,344-348,482`; callers `resolver.py:471,543`, `ingest.py:172`; both config helpers start from `dict(os.environ)` (`ingest.py:118-128`, `resolver.py:670-683`); probe §10.3 |

## 6. Exact changes (the statement-to-proof list DOC-20 verifies for this cycle)

The exact bytes are in the companion diff. Each change replaces one clause; the rest of each line is unchanged.

### C-3 (DC-1a), `README.md` line 13

- **Old:** "no close pack, candidate source or close-run family of any change exists."
- **New:** "no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists."
- **Proof:** §5 rows 1 and 2. "Under either schema" covers v1 and v2; neither appears in any manifest. The close-run family is named separately because the updater writes it, not the writer (`publish_crd_close_run_family`); none exists. Legacy Epic packs stay unmentioned.

### C-4 (DC-1b), `AGENTS.md` line 143

- **Old:** "no close pack, candidate source or close-run family of any change exists, and a close pack establishes …"
- **New:** "no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists; a close pack establishes …"
- **Proof:** as C-3. The semicolon keeps the following clause ("a close pack establishes no QA verdict, …") unchanged.

### C-5 (DC-1c), `CHANGELOG.md` line 7

- **Old:** "Capability only: no close pack of any change exists."
- **New:** "Capability only: no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists."
- **Proof:** as C-3. The same wording as C-3 and C-4, so the three documents agree.

### C-6 (DC-2), `docs/ADAPTER_009.md` line 48, second sentence

- **Old:** "`ENGINE_TAG` and `RELEASE_ID` are not read from the environment: `adapter/wsgi.py` sets them as app configuration defaults (`Isis6` and `rel_dev`) for its `X-Engine-Tag` and `X-Release-Id` headers and its log lines."
- **New:** "The HTTP adapter reads neither `ENGINE_TAG` nor `RELEASE_ID` from the environment (`adapter/wsgi.py` sets them as app configuration defaults, `Isis6` and `rel_dev`, for its `X-Engine-Tag` and `X-Release-Id` headers and its log lines), but the vendor client (`engine/bodygraph/vendor_client.py`) reads `RELEASE_ID` from the environment for its `User-Agent: GlowHDEngine/<release_id>` header when no release identity is passed."
- **Proof:** §5 rows 3 and 4; probes §10.3. One sentence, as the instruction requires. The normalization detail is not stated (PD-2). The line's first sentence is unchanged.

## 7. Files and requirement-to-change/test map

| Item | File | Requirement / obligation | Test or check |
| :- | :- | :- | :- |
| C-3, C-4, C-5 | `README.md`, `AGENTS.md`, `CHANGELOG.md` | S21; H-4; instruction v1.1 DC-1a to DC-1c | no test asserts the sentence; citation check on `AGENTS.md`; the six-file set; DOC-20 |
| C-6 | `docs/ADAPTER_009.md` | S16/S17 operator variables; LR8-F2; instruction v1.1 DC-2 | probes §10.3; the six-file set; DOC-20 |

- **Files changed:** four (`M`). **Not changed:** everything else (instruction v1.1 §7).
- **`AGENTS.md`:** C-4 is the only edit. The Proceed on this plan is the Product Owner's instruction for that exact edit (instruction v1.1 §9).

## 8. Implementation sequence for PR-30

1. **Recover first.** Inspect worktrees, branches, open PRs and `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-*`. Resume the most advanced consistent cycle-3 state. #692, #695 and their branches are not recovery targets.
2. **Check the base.** `git fetch origin main`; `git diff --stat 892feeb origin/main -- README.md AGENTS.md CHANGELOG.md docs/ADAPTER_009.md` must be empty. If not, run `git apply --check` of the companion on `origin/main`. If it fails or a change touches a target line, stop and return to PR-20 through same-owner recovery. No hand merge.
3. **Branch** from `origin/main`: a new branch for cycle 3.
4. **Apply** `git apply docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v3.0-prototype.diff`, read from `main`. `git diff --name-status origin/main` must list exactly the four files.
5. **Validate** as §9 items 1 to 5.
6. **Commit once:** `docs: scope the close-pack nonclaim to the writer and correct RELEASE_ID's environment read (HDE-CRD-0002 WU-DOC-01, DC-1, DC-2)`, with the session's attribution lines.
7. **Write result v3.0** under `docs/ephemeral/`: the applied-diff sha256, test counts, `lanes` and `membership` output, and the CI state known at writing.
8. **Push and open a new PR**, with the `.github/pull_request_template.md` headings under the `AGENTS.md` "PR descriptions" rules. "Why" cites DC-1 and DC-2. "What merging does" states what becomes current on `main` and that merging establishes no QA, acceptance or closure.
9. **Return** `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

**PR split:** one PR (PD-1). **Merge dependency:** this plan's record PR merges first, so PR-30 reads the companion from `main`. **Downstream:** PR-40, then DOC-20, then WU-OPS-01's business case before OPS-10.

## 9. Validation PR-30 runs (PR-35 re-runs items 2 and 3 on the final head)

Closed rails throughout (`env -i … SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`), with no vendor, database or GitHub key passed to a child.

1. **Install:** CPython 3.12, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, in a throwaway copy; then `python -m pytest --version`.
2. **Citations:** `python ci/checks/check_agents_md_citations.py` → `AGENTS_MD_CITATIONS_OK`; `tests/unit/test_check_agents_md_citations.py` passes.
3. **The six document-reading test files** (instruction v1.0 §5.5), zero failures. Prototype: 1,248 passed.
4. **Pre-push reports** on the committed head: `lanes build-notes` → `reason=documentation_only;paths=4;lanes=none`, PF10 path and sha256; `membership` with the four `--path`s → each `not-member`, `release_id` unchanged.
5. **Changed paths:** exactly the four files before the result record; the applied diff's sha256 equals the companion's.
6. **Hosted CI (PR-35):** the `test` job succeeds on the final head, `documentation_only`, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

Codex excludes Markdown, so no Codex finding is expected. Any other review comment is dispositioned under addendum 2.11 rule 7 and addendum 2.14.

## 10. Prototype record

### 10.1 Construction

- A throwaway clone of `892feeb` in the session scratchpad, branch `proto`.
- A scratch script of four exact old→new replacements, each required to match exactly once. Not committed; the diff is the deliverable.
- Prototype head `0a843cc4435a0dbe6f2bb915e6662cedceab3eaa`; diff = the companion (sha256 `9fb7d91e…7c3a3`); `git apply --check` clean on `892feeb` in the working checkout.

### 10.2 Results (2026-10-22 UTC)

Venv: CPython 3.12.3, CI's full install, exit 0; pytest 8.4.2. `env -i` closed rails with `APP_ENV=dev` and `PYTHONDONTWRITEBYTECODE=1`.

| Check | Result |
| :- | :- |
| The six document-reading test files | **1,248 passed** in 118.12 s; exit 0 (04:00:22Z to 04:02:21Z) |
| `check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| `check_direct_db_contract.py` | `DIRECT_DB_CONTRACT_OK` |
| `prepush_check.py --base 892feeb… --head HEAD lanes build-notes` | `reason=documentation_only;paths=4;lanes=none`; `changed_test_targets=0`; PF10 433,368 bytes, sha256 `8ac97232…6d37ff`; `PREPUSH_CHECK_RESULT: PASS`; repository unchanged |
| `prepush_check.py --head HEAD --path …(4) membership` | four `not-member`; `1.3.0`, roster 45, `release_id` `77204764…c51e`; PASS |
| `git diff --name-status 892feeb HEAD` | `M` for the four files |
| Clone clean after the runs | yes |

### 10.3 Probes (closed rails; no network; dummy values)

- **Vendor client:** with `RELEASE_ID` set to 64 `a`s in the environment and a dummy base URL and key, `HdApiClient.from_env()._release_id` is the env value. With `release_id='b'*64` passed, the passed value wins. With `RELEASE_ID` unset, 64 zeros. No request was sent.
- **HTTP adapter:** with `RELEASE_ID=envvalue` and `ENGINE_TAG=envtag` in the environment, `adapter.wsgi:create_app()`'s test client answers `GET /internal/readyz` 200 with `X-Release-Id: rel_dev` and `X-Engine-Tag: Isis6`.

## 11. Interface contracts (instruction v1.1 §8)

| Contract | Met by |
| :- | :- |
| H-4 (the writer's nonclaims) | C-3 to C-5 state "has been produced", as WU-PR-07 result v1.0 lines 172-173 and addendum 2.17 put it |
| D-4 / LR8-F2 | C-6 states what is read and by which code |
| DOC-20 | §6 adds C-3 to C-6 to the statement lists of plans v1.0 and v2.0 |

## 12. Security and migration

- No secret, value or base URL in the change; `RELEASE_ID` appears by name only. The probes used dummy values and sent nothing.
- Migration: none. Rollback: a revert of the new PR.

## 13. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | `main` changes a target file before PR-30 | §8 step 2 |
| RK-2 | PR-30 pushes to #692's or #695's branch | §8 steps 1 and 3 |
| RK-3 | A close pack is produced with the writer later, and C-3 to C-5 go stale | expected: the first v2 close pack is HDE-CRD-0002's own close work, which owns updating these lines. Recorded for the Product Owner (RF-12) |
| RK-4 | A caller starts passing `release_id`, and C-6 goes stale | C-6 says "when no release identity is passed", so it stays true |

- **Recovery:** resume from the last saved artifact. **Instruction defect:** to the IA through DOC-10. **Abort:** only Nathan's manual PR-50.

## 14. Decisions taken in this plan (within approved scope)

| ID | Decision | Reason |
| :- | :- | :- |
| PD-1 | One PR, one commit | four sentences, one subject per finding |
| PD-2 | C-6 omits the normalization detail | optional in instruction v1.1 §6; one sentence stays readable |
| PD-3 | C-3 to C-5 name the close-run family separately, as "no close-run family exists" | the updater writes the family, not the writer; "produced with this writer" would be wrong for it |
| PD-4 | Same clause in all three documents | one fact, one wording |
| PD-5 | Plan and result version 3.0 | the cycle convention of plans v1.0 and v2.0 |

No Product Owner question arises under instruction v1.1 §9: C-4 is the only `AGENTS.md` edit, and it is named here.

## 15. Findings outside this unit's bound (recorded and routed, not changed here)

| ID | Finding | Proposed owner |
| :- | :- | :- |
| RF-12 | When HDE-CRD-0002's close work produces the first v2 close pack, the three nonclaim clauses (C-3 to C-5) and `docs/EVIDENCE_INDEX.md:64` become stale | the owner of that close work; the Product Owner |
| RF-11; RF-1 to RF-10 | as plan v2.0 §16 and plan v1.0 §16 | unchanged |

## 16. Carried items and canon-conflict register

- **Carried unchanged:** plan v1.0 §17 (DOC10-O1; O-19 code; OBS-8; OBS-P3-13; PR35-C1; LR8-F1; the canon doc-deltas; the S21 ADR revision); WU-OPS-01's business case (Product Owner); DOC-20's DC-O1 and DC-O2.
- **`CANON_CONFLICT_REGISTER`:** CR-1 to CR-3 APPROVED_AS_CHANGED by Thoth; CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED by the Product Owner; CR-6 APPROVED (a) by the IA through RS-20; CR-7 and CR-8 APPROVED (a) each by the Product Owner. **No new conflict.** C-6 matches HDE-CLI-API-Vendor-Ref §7.2.2's `User-Agent` and adds nothing to Glow Infrastructure §8.1's OPEN/TBD entry for `RELEASE_ID`.

## 17. PR-30 and PR-35 obligations, and the context conflict

- **PR-30** (this session, under the Product Owner's selection, after Nathan's Proceed for exactly v3.0): §8; returns `PR_CANDIDATE_PUBLISHED` with a PR-35 handoff. PR-30 does not own review correction, current-head CI readiness or merge.
- **PR-35** (its own dedicated session): retrieves every review thread and dispositions any finding; corrects in-scope defects; re-runs §9 items 2 and 3 on the final head; verifies item 6, the remote head and mergeability; returns `MERGE_PENDING` without merging. No `[skip ci]` without Nathan's direct instruction.
- **Merge:** Nathan, manually.
- **PR-40 and DOC-20:** the instruction names this IA. Because this session also authored this plan, a PR-40 run here would review its own plan. The Product Owner decides whether PR-40 for cycle 3 runs here or in another session; this plan does not decide it.
- **Nonclaims:** no QA, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.

## 18. TypeSafe reading for the receiving session (PR-30, WU-DOC-01, plan v3.0)

Action sent (v8.2): "Implement, in the same session that wrote the plan, an approved and not yet implemented correction of four sentences in four Markdown documents (README, CHANGELOG, the agent-instructions file and an operator document) after a completion verification found them inaccurate: apply a ready prototype diff byte for byte on a new branch, run the local tests that read these documents and a read-only pre-push check, commit once, write a result record, push and open the initial pull request. A detailed plan with the exact text and a passing prototype exists; no code changes and no live run occur; an independent review phase, CI, a lineage review and a repeated completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at medium.** Effort score 1.30 (confidence 0.78); rung probabilities low 0.02, medium 0.68, high 0.29, extra high 0.01, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.93, Sonnet 5.5 0.07, Haiku 5.5 0.00 (confidence 0.91). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.019, Opus 5.5 at medium 0.632, Opus 5.5 at high 0.270, Opus 5.5 at extra high 0.009, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.001, Sonnet 5.5 at medium 0.048, Sonnet 5.5 at high 0.020, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-22T04:03:18Z. Nathan picks the cell.
- **Flags:** none printed in the header line.
- **Detail:** the script's detail and Notion-row output (latency, token counts) were not captured: this session displayed only the header lines. The reading was not re-run (one text, one reading).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for PR-30 is not stated; his pick for this PR-20 session is not stated (its reading is instruction v1.1 §17).

**Surface advice:** PR-30 runs in this Claude Code cloud session (the Product Owner's selection) on `amthorn78/glow-hdengine-v2`.
- **Environment:** CPython 3.12 at `/usr/bin/python3.12` with CI's full install in a throwaway clone (about 2 minutes for the six test files); `ruby` at `/usr/local/bin` on `PATH` for the pre-push check; closed rails through `env -i`.
- **Access:** GitHub write for the new branch and PR; no live vendor, production or database access.
- **Order:** this plan's pull request should be merged first.

## 19. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-20 / plan 3 (v3.0) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 (DC-1, DC-2) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state of 2026-10-12T02:29:47.327Z) |
| role/stage | PR-20 author for plan cycle 3 (in the session that also ran DOC-10, by the Product Owner's selection) |
| capture time | 2026-10-22T04:05:00Z |
| execution identity | https://claude.ai/code/session_017Tz88x3eecWgXvRf3dudTQ |
| inherited usage | instruction v1.1 §18 |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; pending and non-gating |

## Canon relied on

Read on `main` at `892feeb`; `docs/pfcanon/` unchanged since DOC-20's head; PF10 v13.7.4.

| Topic | Sources and sections |
| :- | :- |
| Plan contents, state and handoff | PR-20 — Create Detailed PR Implementation Plan — 100926.1: "Inputs", "Execute" 1 to 10, "Required result", "Next step and recovery" |
| Selected context; author/reviewer independence | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, "Role and artifact continuity" ("Honor an explicitly Product Owner-selected continuing context … Preserve author/reviewer independence") |
| Unit scope; deploy facts excluded | PF10 addendum 2.19 (P-8) |
| Routed item LR8-F2 | PF10 addendum 2.21 |
| Writer nonclaims | PF10 addendum 2.17 ("Scope boundaries and nonclaims"; "Deferred obligations") |
| Measure; no ceiling | PF10 addendum 2.18, rules 1, 2 and 5 |
| `User-Agent`; `RELEASE_ID` key | HDE-CLI-API-Vendor-Ref §7.2.2 "Canonical headers"; Glow Infrastructure §8.1 "Shared keys" |
| Repository rules | `AGENTS.md`: "Code review guidelines"; "Operating workflow" (closed rails; pytest readiness; pre-push check; PR descriptions; redaction) |
