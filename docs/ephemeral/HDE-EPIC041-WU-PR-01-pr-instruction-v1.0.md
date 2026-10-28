---
artifact_type: PR_INSTRUCTION
artifact_version: "1.0"
logical_id: HDE-EPIC041-WU-PR-01-PR-INSTRUCTION
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
work_unit_title: "WU-PR-01 — Adapter orchestration entry and pure Engine chart interface (HDE-SEPA006.1; interface part of .3)"
state: INSTRUCTION_READY
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
producer: the whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
prompt: PR-10 — Create PR Work-Unit Instructions — 102726.1 (https://app.notion.com/p/4064590a05eb81de9686f14e4693b315; page state 2026-10-27T13:19:04.774Z, read in full)
r1_rows: GCF-13, GCF-13.PR
ecosystem_release: GCFPE-20261027.1 / 102726.1
SPECIFICATION_REF: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; 37,557 bytes; git blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE, ASK OK.; merged by amthorn78/glow-hdengine-v2#788 as 23324960)
immutable_approved_bases: Specification v1.1 (Thoth); Implementation Plan v1.1 (Isis)
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md (blob cb61644d4380fa5aa32ba0332fd532b5c29279a7; read in full; unchanged since the Audit)
pf10_addenda_applicable: NONE
effective_baseline: "approved base + applicable PF10 overlays (NONE)"
repository_baseline: origin/main 23324960d90447dcbde40f13cc601affd8f2e5ae (only docs/ephemeral/ changed since b29ca84, the Audit's head)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner assigns the dedicated WU-PR-01 PR session at launch)
return_owner: the whole-change IA for HDE-EPIC041, through PR-40 lineage review and the Plan's next stage; rescope through RS-20
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9)
authored_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-PR10-WU-PR-01-20261028
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: WU-PR-01 (requirements R-01, R-02, R-04 interface part; AC-01, AC-02, AC-04, AC-05)
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: PR-10 — 102726.1 (https://app.notion.com/p/4064590a05eb81de9686f14e4693b315), revision as of 2026-10-27T13:19:04.774Z
    role_stage: whole-change IA / GCF-13.PR
    captured_at: 2026-10-28
    runtime_identity: https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj
    repository_persistence: PENDING (no installed GCFPE provenance procedure found under docs/changes/; it holds only AUDIT_RESULTS.json and AUDIT_SUMMARY.md, last changed 2025-11-18; owner: GCFPE management)
---

# HDE-EPIC041 — PR Instruction: WU-PR-01 (PR-10)

This instruction is self-contained for the dedicated WU-PR-01 PR session's PR-20 planning. It does not authorize implementation. Only Nathan / Product Owner's invocation of PR-30 against the exact PR-20 plan does that. Merging this file preserves the record and approves nothing (D21-C).

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `23324960`. `git diff --stat b29ca84 23324960 -- docs/pfcanon/` is empty. This branch changes nothing under `docs/pfcanon/`.

| Title | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Checklist — Separation | Task HDE-SEPA006; Subtasks .1 and .3 | Scope, sequencing (.1 before .2; verification with both), evidence |
| HDE Architecture | §1.1 "Single homes" (Purity rule; Non-BodyGraph chart loader classification; `adapter/`) | The ownership split and the purity predicate |
| HDE Mechanics Guide | §1.1 "BodyGraph and loader seam posture" and the paragraph that follows it | No fallback, no Engine I/O exception, no second resolver; preserve canonical outputs |
| HDE Governance | §9.7.7 "Business case for every requirement and work unit"; §9.1.1 | The business case and its stop rule; the change authority |
| Plan Templates | §12 "General Implementation Plan (Template)"; "Canon precedence for template use" | Instruction fields; precedence |
| HDE Build Notes | Whole file (read for the Audit; unchanged blob) | Silent on this unit. Its one addendum does not apply (Audit §1.3) |
| PR-20 — Create Detailed PR Implementation Plan — 102726.1 (Notion, page state 2026-10-27T13:18:23.839Z) | Role and task; Inputs; Authoritative PF10 and overlay input; Execute; Required result; Next step and recovery (PR-30, PR-35, PR-40, RS-10/20/30, same-owner, terminal) | The receiver contract this instruction is checked against (§12) |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Selection and dependency evidence

* **Selection.** WU-PR-01 is the first of three ordered PR work units in Plan v1.1 §6.
* **Dependency.** "None. It is first" (Plan v1.1 §6). IA-30 review v1.1 §4 names it the first dependency-ready unit.
* **Lane.** WU-PR-01 is a PR unit, not Ops or documentation.

## 2. Business case (as Plan v1.1 states it)

* **Beneficiary:** the delivery team.
* **Evidence:**
  * Audit O-08: committed runs appended to the tracked `artifacts/logs/loader_call.jsonl` three times (`39a5a33a`; `f3e1f9a1` "HDE-EPIC030 QA PASS 1"; `c6fdc913` "HDE-EPIC030 QA PASS 2").
  * Audit O-06 / X-3: chart validation misreports a valid place as invalid when run outside the repository root.
  * E-4 / O-02 locate the concerns.
* **Benefit:** chart validation exists as deterministic data-in/data-out code that tests can run from any CWD without touching the repository, and logging and file reads have one Adapter owner that writes no file by default. This work unit adds the interfaces and changes no caller, so on its own it does not stop a run of today's loader from writing the tracked file. That benefit is realized when WU-PR-02 migrates the callers and removes the loader.
* **Measure:**
  * The AC-02 purity and import-side-effect tests pass, and their negative self-test fails a planted violation.
  * The orchestration tests pass with an injected sink, from a temporary CWD, with zero socket attempts.
  * `git status --porcelain` is empty after the run.
* **Stop rule** (HDE Governance §9.7.7): "A work unit whose business case is met stops; further work on it needs a new business case."

## 3. Required behavior

Plan v1.1 §5, restated so the instruction stands alone.

### 3.1 Target boundary

* **Caller → Adapter chart orchestration entry.** A new non-HTTP module under `adapter/`. It is not a release member and registers no route.
  * It reads `SAFE_MODE`, for the log field only, and the wall clock and the performance clock.
  * It owns the correlation id (`engine.util.input_validators.ensure_cid`), the reads of the pinned-list files (anchored to the repository root, not the CWD), the fixture-chart acquisition and the keys-only log line to an injectable sink.
  * It calls the Engine pure chart interface.
* **Engine pure chart interface.** A new module under `engine/charts/`.
  * It validates the birth inputs against explicit `iso_codes` and `iana_zones` collections, returning the validated values or raising the typed error.
  * It provides `normalize_chart(dict) -> dict`.

### 3.2 Invariants

These are Plan v1.1 §5.2, verbatim in substance.

* **I-1.** The Engine chart module reads no time, randomness, environment, network, provider, logging or filesystem state, and writes none, at import or in any call. Importing it has no side effect (R-02, AC-02).
  * It may reuse the pure helpers `parse_date_yyyy_mm_dd` and `parse_time_hh_mm` of `engine.util.input_validators`. It calls no other function of that module.
  * `_load_list`, `parse_place_city_cc`, `parse_tz_iana` and `ensure_cid` read files or randomness.
  * The AST deny-list checks the module's own imports and calls.
  * The fresh-interpreter test patches the time, randomness, environment, filesystem and socket entry points, and proves that none is reached at import or during validation and normalization.
* **I-2.** The orchestration entry is the only place where the R-01 concerns occur for chart loading (AC-01).
* **I-3.** No vendor or DB acquisition, provider contract, fallback data, route, flag, CLI option or release-member change is introduced. Adding any of them stops the unit and returns it to the IA through rescope.
* **I-4.** Governed output and failure behavior are preserved:
  * the fixture chart dict is byte-identical in canonical serialization;
  * error `code`, `details.field` and message keep today's values for every shape today's supported path accepts;
  * the legacy-routed shapes of §3.3 raise `TypeError`, the one intended change.
* **I-5.** Running any covering test leaves `git status --porcelain` empty.
* **I-6.** Historical captures (`.audit_src/`, `_archive/`, `_arch/`, `handoff/`, `artifacts/architecture/`), `artifacts/logs/loader_call.jsonl` and `tests/retired_tests.md` row 57 are unchanged.

### 3.3 Interface contracts

**Orchestration entry.**

* Signature: `load_chart(*args, **kwargs) -> dict`. `tz`, `correlation_id` and `log_sink` are read from the keyword arguments only, as today. A positional argument after the third is ignored, as today.
* It accepts exactly the two call forms today's supported path accepts, with today's routing:
  * positional: at least three positional strings, the first matching `^\d{4}-\d{2}-\d{2}$` and the second matching `^\d{2}:\d{2}$`;
  * keyword: `birthdate`, `birthtime` and `place` keywords, with optional `tz`, routed as the positional form. This is the form C-1 uses.
* Every other argument shape raises `TypeError("Invalid arguments to load_chart")`. That includes the shapes today's code routes to the legacy signature: a first positional string not shaped `YYYY-MM-DD`, and a keyword-form `birthdate` not so shaped. D-1 retires that path, so this is the one intended change of failure behavior.
* Exactly one keys-only log line is emitted per call, on success and on error.
  * Keys and values: `ts`, `route="loader.load_chart"`, `provider="fixtures"`, `source="default"`, `status` (`ok` or `error`), `duration_ms` (an integer), `safe_mode` and `correlation_id`.
  * `safe_mode` is `true` only when `SAFE_MODE == "1"`, as the loader reads it today (Audit ED-05).
* `log_sink` is a callable that takes the line. When it is `None`, the line goes to a module `logging` logger, and no file is written by default. A raising sink never breaks the call.

**Pure interface.**

* The typed error keeps `code`, `message` and `details`. It is raised with `code="READER_INVALID_INPUT"` and `details={"field": <field>}`, with these messages:

  | Field | Message |
  | :- | :- |
  | `date` | `invalid date` |
  | `time` | `invalid time` |
  | `place` | `invalid place` |
  | `tz`, when absent | `tz required on internal path` |
  | `tz`, when invalid | `invalid tz` |

* The checks run in today's order: date, time, place, then tz presence, then tz validity.
* `normalize_chart(obj)` keeps today's `_normalize_chart`: integer gates are kept, digit strings become integers, and other entries are dropped.

**Data shape.** The fixture chart is today's literal (Audit O-03):

```json
{"gates":[1,2,3],"channels_short":[],"centers":[],"type":"","authority":"","profile":"","meta":{"provider":"fixtures","source":"default"}}
```

### 3.4 Real inputs of each component (PR-20 Execute step 3)

| Component | Real inputs | Outside the real set |
| :- | :- | :- |
| Pure module | Four birth strings, from the orchestration entry only. The entry's callers are WU-PR-02's three migrated callers (Audit §5.1: C-1 fixed literals; C-2, C-3 test literals) and this unit's tests. Pinned ISO and IANA lists, read from the tracked `artifacts/constants/iso_3166_1_alpha2.json` and `iana_tz_list.json` | Non-string or other values get today's typed error or `TypeError`. No further modelling |
| Orchestration entry | Call arguments from those callers. `SAFE_MODE` from the CI runner or the operator's shell. The CWD (repository root in CI and in C-1's runs; a temporary directory in tests). `log_sink` from tests. The two pinned-list files | Arguments outside §3.3 → `TypeError`. A missing pinned-list file is a stated limit (it is tracked), with no fallback |

## 4. Repository baseline, bounded files and exclusions

* **Baseline.** `main` `23324960`. Repository facts are the Audit's (`b29ca84`); no code path has changed since. The per-PR plan re-verifies them at its own base.
* **May add:**
  * one module under `adapter/` (the orchestration entry);
  * one module under `engine/charts/` (pure interface);
  * new test files under `tests/` for both modules and for the characterization;
  * owner-test mappings in `ci/checks/classify_ci_changes.py`;
  * registration of the new tests in `pytest.ini` `testpaths` and the classifier roster, as the classifier's fail-closed rules require.

  Names and paths are fixed by PR-20. `engine/charts/` holds only `loader.py`, with no `__init__.py`; it is imported today as a namespace package, and PR-20 decides whether the new module needs one.
* **Must not change:**
  * `engine/charts/loader.py` and every caller (`scripts/make_compat_determinism_artifacts.py`, `tests/loader/*`);
  * `engine/util/input_validators.py`, `engine/config/provider_loader.py`, `engine/providers/*`, `engine/provider/*`;
  * `catalog/manifest.json` and `engine/config/registry_loader.py` admission constants;
  * any governed evidence;
  * `docs/pfcanon/`.
* **Exclusions:**
  * Plan v1.1 §2;
  * WU-PR-02's migration and removal;
  * WU-PR-03's documentation;
  * Audit FND-005 (the generator's compat repair), FND-006 (`input_validators` CWD reads) and FND-007 (the stale architecture snapshot).

## 5. Tests and evidence (Plan v1.1 §6 WU-PR-01)

* **Purity.**
  * An AST deny-list test for the pure module, after `tests/core/test_engine_core_purity.py`.
  * A fresh-interpreter test that patches time, randomness, environment, filesystem and socket entry points and asserts none is reached at import or in a call.
  * A negative self-test showing the checker flags a planted violation.
* **Orchestration tests:**
  * `SAFE_MODE` set to `1`, to `0` and unset → the `safe_mode` field;
  * a valid correlation id passed through; an absent or invalid one synthesized, matching `^CID-[a-f0-9]{16}$`;
  * keys-only content, with no input value in the line;
  * each invalid field → `READER_INVALID_INPUT` and that field;
  * `tz` absent → field `tz`;
  * a bad argument shape, including each legacy-routed shape of §3.3 and a call with no arguments → `TypeError`;
  * one line per call, on success and on error;
  * a raising sink does not break the call;
  * `adapter.no_io_guard.NoIoGuard` attempts equal 0;
  * a run from a temporary CWD validates the same as a run from the root;
  * the O-03 fixture chart dict, and each `code`, `details.field` and message of §3.3, asserted as literal values.
* **Characterization test** (its own test file).
  * It proves the new entry and today's `engine/charts/loader.load_chart` return equal results, and equal error `code`, `details.field` and message values, on the same inputs, for every call shape today's supported path accepts, valid and invalid.
  * It runs from the repository root, which today's validators need, with today's loader's log write redirected to a temporary directory by patching `engine.charts.loader._Path`, as C-2 and C-3 do today. That keeps `git status --porcelain` empty.
  * WU-PR-02 deletes this file together with the loader (Plan v1.1 §6 WU-PR-02 Scope).
* **AC-04 record.** The PR records:
  * the commands and configuration (closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`);
  * the tested-source SHA;
  * the results with counts;
  * the actor, the time and the limitations.

  Tested-source identity stays distinct from any later commit and from review-time HEAD.
* **Clean tree.** `git status --porcelain` is empty after the covering tests.
* **Governed evidence.** None is planned (Plan v1.1 §10). If a changed path triggers a governed family, it is published only through `tools/evidence/update_evidence_index.py` and the canonical generators, and then the read-only checks run. This question stays with QA-10 (review v1.0 N-4).

## 6. Acceptance

* AC-01: the entry exists and owns the R-01 concerns for chart loading.
* AC-02.
* AC-04: the interface-level checks.
* AC-05: output equality and a clean tree.
* Exact-head hosted CI `test` is green. No CI waiver exists for HDE-EPIC041. A red result caused outside this change is handled under the CI-red rules (Plan v1.1 RK-06) and is not green.
* Acceptance of the work unit is the PR-40 lineage review after Nathan's merge.

## 7. Environment, CI and access facts

* **Local.** AGENTS.md pytest readiness: `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, then `python -m pytest --version`.
* **Pre-push.** `python tools/ci/prepush_check.py lanes build-notes`, and `python tools/ci/prepush_check.py --path <path> membership` for each changed path. Every changed path must report "not a release member".
* **CI classification.**
  * A new product path with no owner mapping fails with `CI_PRODUCT_OWNER_TEST_MISSING:<path>` (Audit O-13).
  * `ci/checks/classify_ci_changes.py` and `pytest.ini` are full-validation paths (classifier lines 32 to 40). A change to either selects the full validation target set, so plan CI runs economically: one coherent push, not iterative pushes.
* **Not needed.** No open rails, vendor, Railway, database or production access. No Notion writes.

## 8. Migration, security and recovery

* **Migration.** None. Nothing imports the new modules in this unit.
* **Security.**
  * No route, credential or network.
  * The log line carries no birth input.
  * `NoIoGuard` proves zero sockets.
* **Rollback.** Revert the PR. The change is additive.
* **Recovery.**
  * Interrupted work resumes in the same work unit: PR-30 recovery before publication, RS-40 after publication.
  * A genuine boundary finding becomes one `RESCOPE_REQUEST` by the PR author (PR-20, PR-30 or PR-35) to this IA through RS-20, with the exact `PR_RETURN_PHASE`. Isis has no role in that lane.
  * An ordinary in-scope defect is repaired in place.

## 9. Ownership, code review and merge

* **Sessions.**
  * PR-20 plans in the dedicated WU-PR-01 session.
  * Nathan's PR Implementation Proceed (PR-30), against the exact PR-20 plan, is the only implementation authorization.
  * PR-30 implements, tests locally, makes a coherent commit and publishes the initial candidate (`PR_CANDIDATE_PUBLISHED`).
  * PR-35, in its own dedicated session, retrieves and resolves reviews, retests, pushes coherent corrections, verifies current-head CI and mergeability, and returns `MERGE_PENDING` without merging.
* **Code review.** Every finding that shows a wrong result, a crash or a guarantee breach on a real input is fixed. Every other finding is answered on its thread with the traced path and the stated limit. Declining a security finding or a P1 goes to the Product Owner first.
* **Merge.** Nathan merges. No agent merges, enables auto-merge or schedules a merge.
* **Lineage.** PR-40 reviews the landed lineage against this instruction, the PR-20 plan and the Proceed, and its ACCEPT returns to this IA for the Plan's next stage (WU-PR-02).

## 10. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Sources | Statement | Affected | Disposition and status | Interim treatment for WU-PR-01 | Drainage target / owner |
| :- | :- | :- | :- | :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION | Plan Templates Preflight B; HDE Governance §2.0.19; HDE Schemas and Artifacts token-shape clarification | Acceptance map for tokenless work | Close pack (§10 of the Specification) | APPROVED by Thoth, CF-E-30 review v1.1, 2026-10-28: no operative conflict; keep the map with no token roster (Ruling R-A); confirmed by Isis IA-30 v1.1 | None. A close-pack matter for CL-05 | Product Owner (possible canon change) |
| CCR-2 | CANON_RECONCILIATION | HDE Governance §9.7.7; Plan Templates §2 | Business Case content lists differ | Specification | APPROVED by Thoth, review v1.1: no conflict for this Epic | None | None |
| CCR-3 | CANON_RECONCILIATION | HDE Build Notes (S19 decisions on vendor route selection and production vendor override) | Possible reach into the orchestration path | R-01 | APPROVED by Thoth, review v1.1, as conditional. The Audit (§7) and Isis (IA-30 v1.1 §4.4) find it not triggered | I-3 forbids resolver-selected vendor acquisition; PR-20 re-checks at its head | Implementation Audit; each PR |
| CCR-4 | CANON_RECONCILIATION | PF09.3 Task notes; HDE Build Notes | Cited Build Notes record of the loader defect is no longer present | None | APPROVED by Thoth, review v1.1: no conflict | None | None |

## 11. Unresolved items, not-produced artifacts and owners

* **Not produced:** the PR-20 plan, Proceed, code, tests, PR and CI results. All are the dedicated PR session's, after this instruction.
* **Open and not blocking:**
  * TI-07 / CCR-1: Product Owner.
  * TI-02, items 9 and 10: Product Owner.
  * FND-005 to FND-007: CL-40 and the Product Owner.
  * Review v1.0 N-4: QA-10.
  * Review v1.1 N-5: a nit in the approved Plan, with no effect here.
* **Usage persistence:** pending (front matter).

## 12. Semantic readiness comparison (PR-10)

| Source clause | Intended meaning | Instruction meaning | Owned unit | Acceptance / evidence stage |
| :- | :- | :- | :- | :- |
| Specification R-01 / AC-01 | Operational concerns in one Adapter-owned entry | §3.1, I-2 | WU-PR-01 (entry); WU-PR-02 (none left in Engine) | PR evidence; PR-40 |
| Specification R-02 / AC-02 | Pure, explicit data-in/data-out, no import side effect | §3.2 I-1, §5 purity tests | WU-PR-01 | PR evidence |
| Specification R-04 / AC-04 | Meaningful checks with recorded fields | §5 | WU-PR-01 (interface part) | PR record |
| Specification AC-05 | Outputs and failures preserved; no fallback; clean tree | I-4, I-5, characterization and literal tests | WU-PR-01 and WU-PR-02 | PR evidence |
| Plan v1.1 §5.3 | Argument contract; one intended failure change | §3.3, verbatim in substance | WU-PR-01 | Orchestration `TypeError` tests |
| Plan v1.1 §6 dependency | First unit | §1 | WU-PR-01 | — |
| Plan v1.1 I-3 / Specification non-goals | No acquisition, contract, fallback or release change | §3.2 I-3, §4 must-not-change | WU-PR-01 | Pre-push membership check |
| PR-20 "real inputs" | Each component's real inputs | §3.4 | WU-PR-01 | PR-20 plan |
| PR-20 PR-30/PR-35 ownership | Distinct phases; no agent merge | §9 | WU-PR-01 | — |

Each comparison passes. There are no numeric domains, sentinel values or nested closed schemas beyond those stated. `duration_ms` is an integer, as today. The unit does not depend on an external system, so no pin or precondition is needed.

## 13. TypeSafe reading and surface advice for PR-20

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `authoring`, label "HDE-EPIC041 PR-20 WU-PR-01 per-PR plan".
  * No Notion row written: this is an executing-flow session, and PR-10 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Create a new detailed per-PR implementation plan for the first of three PR work units of an approved Epic, from one new PR instruction of about 24 KB: one new pure Engine chart validation module, one new Adapter-owned orchestration module, about four groups of new tests and CI owner mappings, alongside one legacy Python module of about 170 lines that this unit does not change. A written prompt with steps exists; the planning session reads code but changes none, and no live run against a provider occurs. The Product Owner's Proceed, implementation and independent PR reviews follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.28 (confidence 0.77); rung probabilities low 0.00, medium 0.03, high 0.69, extra high 0.25, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.13, Opus 5.5 0.69, Sonnet 5.5 0.17, Haiku 5.5 0.01 (confidence 0.59). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.004, Fable 5.1 at high 0.090, Fable 5.1 at extra high 0.033, Fable 5.1 at max 0.004, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.021, Opus 5.5 at high 0.476, Opus 5.5 at extra high 0.172, Opus 5.5 at max 0.021, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.005, Sonnet 5.5 at high 0.117, Sonnet 5.5 at extra high 0.043, Sonnet 5.5 at max 0.005, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.007, Haiku 5.5 at extra high 0.003, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T04:28:02Z. Nathan picks the cell.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for PR-20 and none for this PR-10 session, so none is recorded.
* **Surface advice (PR-20).**
  * Run it in a new dedicated top-level Claude Code cloud session for the WU-PR-01 PR role on `amthorn78/glow-hdengine-v2`, started after this instruction's pull request merges. The same session then receives PR-30 after Nathan's Proceed. PR-35 later runs in its own session.
  * Read access is needed to `main`: this instruction; Plan v1.1, its review v1.1 and the Audit; Specification v1.1; `docs/pfcanon/`; and the code it names (`engine/charts/loader.py`, `engine/util/input_validators.py`, `adapter/no_io_guard.py`, `tests/core/test_engine_core_purity.py`, `tests/loader/`, `pytest.ini`, `ci/checks/classify_ci_changes.py`, `tools/ci/prepush_check.py`).
  * Planning needs no code change. A local closed-rails virtualenv for read-only checks (pre-push `lanes`, `membership`, classifier probes) is useful.
  * Write access is needed to one branch and one pull request under `docs/ephemeral/` for the plan.
  * Not needed: open rails, or vendor, Railway, database or Notion writes.

## 14. Nonclaims

This instruction is not Product Owner implementation approval. It is not a PR-20 plan, Proceed, implementation, CI result, QA, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum or closure. Nothing outside `docs/ephemeral/` is changed.
