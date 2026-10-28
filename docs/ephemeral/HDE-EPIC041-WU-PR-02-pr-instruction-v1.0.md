---
artifact_type: PR_INSTRUCTION
artifact_version: "1.0"
logical_id: HDE-EPIC041-WU-PR-02-PR-INSTRUCTION
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-instruction-v1.0.md
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-02
work_unit_title: "WU-PR-02 — Caller migration, legacy retirement and boundary reconciliation (HDE-SEPA006.2; reconciliation part of .3)"
state: INSTRUCTION_READY
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
producer: the whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
prompt: PR-10 — Create PR Work-Unit Instructions — 102726.1 (https://app.notion.com/p/4064590a05eb81de9686f14e4693b315; page state 2026-10-27T13:19:04.774Z, read in full)
r1_rows: GCF-13, GCF-13.PR
ecosystem_release: GCFPE-20261027.1 / 102726.1
SPECIFICATION_REF: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; corrected by AUD-CORR-1 in the WU-PR-01 lineage review §10)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; git blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_REF: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE, ASK OK.)
DEPENDENCY_REF: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-01; merged by amthorn78/glow-hdengine-v2#793 as 3c2f7788)
DELIVERED_INTERFACE_REF: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (§3, as landed by amthorn78/glow-hdengine-v2#791 at e72c9bac)
immutable_approved_bases: Specification v1.1 (Thoth); Implementation Plan v1.1 (Isis)
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md (661 lines, 73,639 bytes, sha256 2a43e518f13219569ee3de74f544af9c176a648c8f40c926673671fae164c213; read in full; provenance)
pf10_addenda_applicable: "HDE Build Notes addendum 2.2 'Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close' (R-1, R-2: constraints on what WU-PR-02's code and tests may read or pin); addendum 2.3 (the WU-PR-01 lineage review record; its deferred-obligations table names WU-PR-02's carried items). Addendum 2.1 (S19) does not apply"
effective_baseline: "approved base + applicable PF10 overlays (addenda 2.2 and 2.3 for their scope)"
repository_baseline: origin/main 9f681bdf83686574d145508b825272eed8d27267 (outside docs/ identical to e72c9bac, the WU-PR-01 squash)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner assigns the dedicated WU-PR-02 PR session at launch)
return_owner: the whole-change IA for HDE-EPIC041, through PR-40 lineage review and the Plan's next stage; rescope through RS-20
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9)
authored_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-PR10-WU-PR-02-20261028
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: WU-PR-02 (requirements R-01 residual, R-03, R-04 reconciliation part; AC-01, AC-03, AC-04, AC-05)
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: PR-10 — 102726.1 (https://app.notion.com/p/4064590a05eb81de9686f14e4693b315), revision as of 2026-10-27T13:19:04.774Z
    role_stage: whole-change IA / GCF-13.PR
    captured_at: 2026-10-28
    runtime_identity: https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj
    inherited_usage: HDE-EPIC041-PR40-WU-PR-01-20261028
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — PR Instruction: WU-PR-02 (PR-10)

This instruction is self-contained for the dedicated WU-PR-02 PR session's PR-20 planning. It does not authorize implementation. Only Nathan / Product Owner's invocation of PR-30 against the exact PR-20 plan does that. Merging this file preserves the record and approves nothing (D21-C).

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `9f681bdf`. Since WU-PR-01's instruction the only `docs/pfcanon/` changes are HDE Build Notes, replaced by v13.9.1 (#792) and then v13.9.2. This branch changes nothing under `docs/pfcanon/`.

| Title | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Checklist — Separation | Task HDE-SEPA006; Subtasks .2 and .3 | Supported-caller migration; remove the old operational path or keep a pure surface under an owning contract; reconcile .1 and .2 |
| HDE Architecture | §1.1 "Single homes" (Purity rule; Non-BodyGraph chart loader classification) | What must leave `engine/` |
| HDE Mechanics Guide | §1.1 "BodyGraph and loader seam posture" and the remediation paragraph | Migrate active callers, including the compatibility/determinism generator; preserve canonical outputs; no fallback, no Engine I/O exception, no second resolver |
| HDE Governance | §9.7.7 "Business case for every requirement and work unit"; §9.1.1 | Business case and stop rule; change authority |
| HDE Build Notes | Whole file (v13.9.2, 661 lines). Addendum 2.2 R-1 to R-3; addendum 2.3 (the WU-PR-01 lineage record, including its deferred-obligations table); addendum 2.1 (S19, not engaged) | §3.2 I-7; §11 carried items |
| PR-20 — Create Detailed PR Implementation Plan — 102726.1 (Notion, read in full for WU-PR-01's instruction; unchanged page state 2026-10-27T13:18:23.839Z) | Inputs; Execute; Required result; Next step and recovery | The receiver contract (§12) |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Selection and dependency evidence

* **Selection.** WU-PR-02 is the second of three ordered PR work units in Plan v1.1 §6.
* **Dependency.** The Plan requires "WU-PR-01 merged to `main` and accepted by its PR-40 lineage review".
  * Merged: #791 as `e72c9bac`, 2026-10-28T17:26:38Z.
  * Accepted: the lineage review v1.0, ACCEPT, merged by #793.
  * The post-merge `main` push run 40735776026 on `e72c9bac` concluded `success`.
  * The per-PR plan is formed against a `main` that contains WU-PR-01, which `9f681bdf` does.
* **Lane.** A PR unit.

## 2. Business case (as Plan v1.1 states it)

* **Beneficiary:** the delivery team.
* **Evidence:**
  * E-1 / O-04 / X-2: the legacy signature fails for every resolvable provider and carries fallback data.
  * E-3: its only caller was retired to hide the defect, not fix it.
  * O-05: a legacy call writes `artifacts/provider/decision.txt`.
  * O-11: the canon-named generator still imports the mixed module on every run.
* **Benefit:** the broken path is closed rather than hidden, and no supported caller depends on Engine code with operational side effects. A regression that reintroduces an importer fails CI rather than surfacing later the way E-2 did. With WU-PR-01's interfaces, this also realizes WU-PR-01's deferred benefit: no supported run of the chart path can write the tracked `artifacts/logs/loader_call.jsonl`.
* **Measure:**
  * `engine/charts/loader.py` is absent.
  * The repository-wide import guard passes, and it fails on a planted importer.
  * C-1 still exits 2 with its stderr from a temporary CWD and writes nothing.
  * `artifacts/compat/*` bytes are unchanged.
  * The retained-coverage tests named in PF09.3 pass.
  * `git status --porcelain` is empty after the covering tests.
* **Stop rule** (HDE Governance §9.7.7): "A work unit whose business case is met stops; further work on it needs a new business case."

## 3. Required behavior

### 3.1 Caller dispositions (Audit §5.1, re-verified at `9f681bdf`)

| # | Caller | Today | Required disposition |
| :- | :- | :- | :- |
| C-1 | `scripts/make_compat_determinism_artifacts.py` | `from engine.charts.loader import load_chart` at module level (line 9); calls `load_chart(**a)` with the keyword form; exits 2 with `compat_public not implemented` before that call (Audit O-11) | Change **only** the import and the chart call, to `adapter.chart_orchestration.load_chart` (same keyword form). Its `compat_public` lookup, exit 2, stderr text and write logic stay unchanged (Audit ED-07). Restoring its compat computation is out of scope (FND-005) |
| C-2 | `tests/loader/test_load_chart_fixture_only.py` | Imports `engine.charts.loader`; redirects the loader's log by patching `_Path` | Migrate to the WU-PR-01 interfaces: the orchestration entry with an injected sink, and the pure module's `ChartInputError`. No `_Path` patch. Keep its two assertions in substance (normalized fixture result; tz-absent typed error) |
| C-3 | `tests/loader/test_loader_logs_keys_only.py` | Imports `engine.charts.loader`; reads the redirected `loader_call.jsonl`; asserts that `"12:34"` is absent from the whole raw line | Migrate to the orchestration entry with an injected sink. **It must not carry OBS-4:** the clock-derived `ts` is pinned to its shape and excluded from the birth-input substring check, as WU-PR-01's `test_log_line_is_keys_only` does (ID-35-1) |
| C-4 | Legacy signature `load_chart(user_id)` | No supported caller | Retired by D-1 with the module (below) |
| WU-PR-01 characterization file | `tests/adapter/test_chart_orchestration_characterization.py` | Imports `engine.charts.loader` to compare | Deleted in the same commit as the loader (Plan v1.1 §6 WU-PR-02 Scope, RL-3 (c)); see §3.3 for its registrations |

C-2 and C-3 may be migrated in place, keeping their paths and their CI registrations, or replaced. If the PR-20 plan replaces either, each removed test file gets a `tests/retired_tests.md` row and its CI registrations are updated (§3.3). The plan states which, with the basis.

### 3.2 Invariants

These are Plan v1.1 §5.2, and WU-PR-01's as delivered.

* **I-1.** The Engine chart module stays pure, at import and in any call. WU-PR-02 does not change `engine/charts/pure.py`. No caller is told to import `engine.util.input_validators` into a pure path. That module imports `secrets`, which seeds `random` at import, and its date helper reads `TZ` (AUD-CORR-1, OBS-1).
* **I-2.** After this unit, no R-01 concern remains under `engine/charts/`. The only module there is `pure.py`.
* **I-3.** No vendor or DB acquisition, provider contract, fallback data, route, flag, CLI option or release-member change is introduced. Removing the loader removes its `{"gates":[1,2,3]}` resolver-unavailable fallback.
* **I-4.** Governed caller output and failure behavior are preserved.
  * C-1's exit status, stderr and no-write outcome are unchanged.
  * `artifacts/compat/AB.json`, `BA.json` and `identity_hash.txt` are byte-unchanged (blobs `7fe71f99…`, `7fe71f99…`, `7e6176a2…`).
  * The supported chart path's results and typed errors are those WU-PR-01 pinned as literal values in `tests/adapter/test_chart_orchestration.py`.
  * The one intended change of failure behavior, legacy-routed shapes raising `TypeError`, was delivered by WU-PR-01 and is now the only behavior.
* **I-5.** Running any covering test leaves `git status --porcelain` empty.
* **I-6.** Unchanged:
  * the historical captures (`.audit_src/`, `_archive/`, `_arch/`, `handoff/`, `artifacts/architecture/`);
  * `artifacts/logs/loader_call.jsonl` (blob `92556952…`);
  * `tests/retired_tests.md` row 57;
  * `engine/util/input_validators.py`, `engine/config/provider_loader.py`, `engine/providers/*` and `engine/provider/*`.
* **I-7** (HDE Build Notes addendum 2.2, R-1 and R-2). No code, test, tool or CI step added or changed by this unit:
  * reads, binds, hashes or resolves a path under `docs/ephemeral/` or `docs/pfcanon/`;
  * pins a PF document's file name, version or digest.

  The import guard's file walk excludes those two trees. No test depends on a planning document.

### 3.3 CI registration facts (probed at `9f681bdf`, in a throwaway clone)

* **Deleting `engine/charts/loader.py`** without an owner mapping fails classification with `CI_CHANGE_CLASSIFIER_ERROR:CI_PRODUCT_OWNER_TEST_MISSING:engine/charts/loader.py`. The classifier resolves owners for deleted product paths too. WU-PR-02 therefore adds an owner mapping for the deleted path, for example to the import-guard test.
* **Deleting the characterization file** while it is still in WU-PR-01's two owner entries (`engine/charts/pure.py` and `adapter/chart_orchestration.py` in `_PRODUCT_TEST_OWNER_PATHS`) fails with `CI_REGISTERED_OWNER_TEST_DELETED:tests/adapter/test_chart_orchestration_characterization.py`. It is removed from both entries in the same commit. It is in no `pytest.ini` list (WU-PR-01 plan PD-4).
* **Changing `scripts/make_compat_determinism_artifacts.py`** needs an owner mapping (Audit O-13), for example to the generator-behavior test.
* **C-2 and C-3** are in `pytest.ini` `testpaths` (lines 72, 74) and the classifier roster (lines 112, 114). Migration in place keeps them. Replacement updates both lists. `tests/evidence/test_rails_ci_workflow_integration.py` requires the `testpaths` collection to equal fixed ∪ supplemental ∪ inactive (WU-PR-01 plan PD-4).
* **Full validation.** `ci/checks/classify_ci_changes.py` and `pytest.ini` are full-validation paths, so a change to either selects the full validation set. Plan one coherent push.
* **The PR-20 plan** confirms every registration with `python tools/ci/prepush_check.py --base <base> --head HEAD lanes membership build-notes` on a prototype, and with the `sweep` report.

## 4. Repository baseline, bounded files and exclusions

* **Baseline.** `main` `9f681bdf`. Outside `docs/` it is identical to `e72c9bac`. `engine/charts/loader.py` has blob `8ea4dce2…`, unchanged since `6c6f4b2a`. C-1, C-2, C-3, `pytest.ini` and `tests/retired_tests.md` have the same blobs as at the Audit's head `b29ca84`.
* **May change:**
  * `scripts/make_compat_determinism_artifacts.py` (import and call only);
  * `tests/loader/test_load_chart_fixture_only.py` and `tests/loader/test_loader_logs_keys_only.py`;
  * `ci/checks/classify_ci_changes.py` (owner mappings; roster if a test is replaced);
  * `pytest.ini` (only if a test is replaced);
  * `tests/retired_tests.md` (new rows only).
* **May delete:** `engine/charts/loader.py`; `tests/adapter/test_chart_orchestration_characterization.py`.
* **May add:** new test files for the import guard and the generator behavior. Names and paths are fixed by PR-20.
* **Must not change:**
  * `engine/charts/pure.py` and `adapter/chart_orchestration.py`. If a defect is found in either, it is an in-scope repair only if it is needed for this unit's acceptance; record it.
  * the I-6 files;
  * `catalog/manifest.json` and the admission constants;
  * `artifacts/compat/*`;
  * any governed evidence;
  * `docs/pfcanon/`;
  * the other `tests/loader/*` files (`test_loader_hdapi_ignores_tz.py`, `test_pinned_lists_not_empty.py`, `test_validators_strict.py`, which test `input_validators` and the HDAPI helper, not the loader).
* **Exclusions:**
  * Plan v1.1 §2;
  * WU-PR-03's documentation;
  * FND-005 (the generator's compat repair), FND-006 (`input_validators` CWD and `TZ` reads) and FND-007 (the stale architecture snapshot).

## 5. Tests and evidence (Plan v1.1 §6 WU-PR-02)

* **Repository-wide import guard** (a new test).
  * No tracked Python file outside the classifier's historical prefixes, `docs/ephemeral/` and `docs/pfcanon/` imports `engine.charts.loader` (`import` or `from … import`, including dynamic-import string forms) or references `_call_legacy`.
  * The path `engine/charts/loader.py` does not exist.
  * A negative self-test on a synthetic source proves the checker flags each import form.
  * The guard excludes only its own source file, the synthetic source of its self-test, and the trees named above.
* **Generator behavior test** (a new test). It runs C-1 as a subprocess from a temporary CWD and asserts:
  * exit status 2;
  * stderr `compat_public not implemented`;
  * no file created in the CWD.
* **Compat bytes.** `git diff --exit-code -- artifacts/compat/` holds, recorded in the PR.
* **Migrated C-2 and C-3** pass, and C-3 carries no clock dependency (OBS-4).
* **Retained coverage:**
  * `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode`;
  * `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`;
  * WU-PR-01's four test files minus the deleted characterization file.
* **Reconciliation of R-01 to R-03, in the PR record:**
  * the inventory search re-run at the PR head;
  * a disposition per member;
  * every R-01 concern located in the Adapter module;
  * no compatibility surface retained, so TI-06 is moot.

  The search has two parts:
  * Scope: all tracked files except `docs/pfcanon/` and `docs/ephemeral/`.
  * Pattern: `engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy`.
* **AC-04 record.**
  * Commands and configuration: closed rails, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, through `env -i`.
  * The tested-source SHA.
  * The results with counts.
  * The actor, the time and the limitations.
* **Clean tree.** `git status --porcelain --untracked-files=all` is empty after the covering tests.
* **Governed evidence.** None is planned (Plan v1.1 §10). If a changed path triggers a governed family, it is published only through `tools/evidence/update_evidence_index.py` and the canonical generators, and then the read-only checks run. Review v1.0 N-4 stays with QA-10.

## 6. Acceptance

* AC-01: no R-01 concern left under `engine/charts/`.
* AC-03: inventory, dispositions, module removed, guard.
* AC-04: the migration-level checks and the reconciliation.
* AC-05: preserved outputs and failures, no fallback, a clean tree.
* Exact-head hosted CI `test` is green. No CI waiver exists for HDE-EPIC041. A red result caused outside this change is handled under the CI-red rules (Plan v1.1 RK-06) and is not green.
* Acceptance of the unit is the PR-40 lineage review after Nathan's merge.

## 7. Environment, CI and access facts

* **Local.** AGENTS.md pytest readiness: `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, then `python -m pytest --version`.
  * Run tests under `env -i`: the container exports database, vendor and GitHub credentials (OBS-2).
  * Run `git fetch --unshallow` first (OBS-5).
  * Make no tool calls during `prepush_check.py replay`. The repository's canon hook writes `.git/` state, and the replay reports that as a read-only violation.
* **Pre-push.**
  * `python tools/ci/prepush_check.py lanes build-notes`.
  * `python tools/ci/prepush_check.py --path <path> membership` for each changed path; every path must be "not a release member".
  * `sweep` for test reachability.
* **Not needed.** No open rails, vendor, Railway, database or production access. No Notion writes.

## 8. Migration, security and recovery

* **Migration.** In-repository callers move to WU-PR-01's interfaces. No data migration.
* **Security.**
  * No route, credential or network.
  * Removing the loader removes a provider-resolution path that wrote `artifacts/provider/decision.txt` relative to the CWD (O-05).
* **Rollback.** Revert the PR. The module and the callers return. No data or release state is involved.
* **Recovery.**
  * Interrupted work resumes in the same work unit: PR-30 recovery before publication, RS-40 after publication.
  * A genuine boundary finding becomes one `RESCOPE_REQUEST` by the PR author (PR-20, PR-30 or PR-35) to this IA through RS-20, with the exact `PR_RETURN_PHASE`. Isis has no role in that lane.
  * An ordinary in-scope defect is repaired in place and recorded.

## 9. Ownership, code review and merge

* **Sessions.**
  * PR-20 plans in the dedicated WU-PR-02 session.
  * Nathan's PR Implementation Proceed (PR-30), against the exact PR-20 plan, is the only implementation authorization.
  * PR-30 implements, tests locally, makes a coherent commit and publishes (`PR_CANDIDATE_PUBLISHED`).
  * PR-35, in its own dedicated session, resolves reviews, retests, pushes coherent corrections, verifies current-head CI and mergeability, and returns `MERGE_PENDING` without merging.
* **Code review.** Every finding that shows a wrong result, a crash or a guarantee breach on a real input is fixed. Every other finding is answered on its thread with the traced path and the stated limit. Declining a security finding or a P1 goes to the Product Owner first. Two consecutive rounds raising the same finding class trigger one design question to the Product Owner.
* **Merge.** Nathan merges. No agent merges, enables auto-merge or schedules a merge.
* **Lineage.** PR-40 reviews the landed lineage against this instruction, the PR-20 plan and the Proceed, and its ACCEPT returns to this IA for the Plan's next stage (WU-PR-03, final documentation).

## 10. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Status and reviewer | Treatment in WU-PR-02 |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work; Plan Templates Preflight B; HDE Governance §2.0.19; HDE Schemas and Artifacts) | APPROVED, Thoth, CF-E-30 review v1.1, 2026-10-28 (Ruling R-A); confirmed by Isis IA-30 v1.1 | None; a close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists; HDE Governance §9.7.7; Plan Templates §2) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 | CANON_RECONCILIATION (HDE Build Notes S19 decisions on vendor route selection and the production vendor override) | APPROVED as conditional, Thoth, review v1.1; not triggered (Audit §7; IA-30 v1.1 §4.4; WU-PR-01 lineage review §9) | Not triggered: removing the loader removes a provider-resolution path and adds no acquisition (I-3). PR-20 re-checks it at its head |
| CCR-4 | CANON_RECONCILIATION (PF09.3 Task notes vs HDE Build Notes on the loader defect record) | APPROVED, Thoth, review v1.1 | None |

No new entry. HDE Build Notes addenda 2.2 and 2.3 are current canon and conflict with neither approved base. 2.2 applies as I-7.

## 11. Carried items, not-produced artifacts and owners

| Item | Owner and treatment here |
| :- | :- |
| OBS-4 (clock-dependent C-3) | Resolved by C-3's migration (§3.1) |
| AUD-CORR-1, OBS-1 (`input_validators` is not import-pure; date helper reads `TZ`) | Applied as I-1; no change to `input_validators` (FND-006) |
| Addendum 2.2 bearing | Applied as I-7 |
| OBS-2, OBS-5 (environment) | §7 |
| TI-07 / CCR-1 | Product Owner; CL-05 at close |
| TI-02, Candidate CRD Items List items 9 and 10 | Product Owner |
| FND-005 to FND-007 | CL-40 scan and the Product Owner |
| Review v1.0 N-4 | QA-10 |
| Not produced | The PR-20 plan, Proceed, code, tests, PR and CI results: the dedicated PR session's, after this instruction |
| Usage persistence | Pending (front matter) |

## 12. Semantic readiness comparison (PR-10)

| Source clause | Intended meaning | Instruction meaning | Owned unit | Acceptance / evidence stage |
| :- | :- | :- | :- | :- |
| Specification R-03 / AC-03 | Every supported caller migrated; the old operational path removed or only a pure surface under an owning contract; an import-path rename alone is not migration; historical captures unchanged; outputs and failures preserved | §3.1 dispositions; module deleted with no shim (D-1, ED-06); I-4, I-6 | WU-PR-02 | Guard test; generator test; PR-40 |
| Specification R-01 / AC-01 (residual) | No operational concern left in Engine chart code | I-2 | WU-PR-02 | Guard test; PR-40 |
| Specification R-04 / AC-04 (reconciliation) | Verify the complete migration; reconcile R-01 to R-03 | §5 reconciliation and guard | WU-PR-02 | PR record |
| Specification AC-05 | Preserved outputs and failures; no fallback; clean tree | I-3, I-4, I-5; compat-bytes check | WU-PR-02 | PR evidence |
| Plan v1.1 §6 WU-PR-02 Scope and Tests | Migrate C-1 to C-3; remove the module; delete the characterization test with a retired row; inventory re-run; guard with exclusions | §3.1, §3.3, §5 | WU-PR-02 | — |
| Plan v1.1 §6 dependency | WU-PR-01 merged and accepted | §1 | WU-PR-02 | — |
| D-1 (Product Owner, Audit §8.1) | Retire the legacy signature | §3.1 C-4 | WU-PR-02 | Guard; module absent |
| HDE Mechanics Guide §1.1 | Migrate generator callers; preserve canonical outputs; no fallback | C-1 disposition; I-3; I-4 | WU-PR-02 | Generator test; compat bytes |
| HDE Build Notes 2.2 R-1, R-2 | No code or test reads planning documents or pins PF versions | I-7 | WU-PR-02 | Code review; PR-40 |
| PR-20 "real inputs" | Each component's real inputs | §13 | WU-PR-02 | PR-20 plan |

Each comparison passes. There are no numeric domains or closed schemas beyond those stated. The unit depends on no external system, so no pin or precondition is needed.

## 13. Real inputs of each component (PR-20 Execute step 3)

| Component | Real inputs | Outside the real set |
| :- | :- | :- |
| Migrated C-1 | Its own literal birth data; the CWD of the operator's shell or CI | Unchanged script logic; no new argument |
| Migrated C-2, C-3 | Their literal inputs; `SAFE_MODE` from CI (`1`) or a test's `monkeypatch`; the runner's clock | The clock is excluded from the substring check (OBS-4) |
| Import guard | The tracked Python files of the checkout, outside the excluded trees | Generated or untracked files are not inputs; a stated limit |
| Generator behavior test | The script, run as a subprocess in a temporary CWD | — |

## 14. TypeSafe reading and surface advice for PR-20

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `authoring`, label "HDE-EPIC041 PR-20 WU-PR-02 per-PR plan".
  * No Notion row written: this is an executing-flow session, and PR-10 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Create a new detailed per-PR implementation plan for the second of three PR work units of an approved Epic, from one new PR instruction of about 25 KB: migrate three existing callers (one script and two tests) of one legacy Python module of about 170 lines to already merged interfaces, delete that module and one characterization test, add a repository-wide import guard test and a script behavior test, and update CI owner mappings and the retired-test record, with a throwaway prototype to confirm the CI classifier accepts the deletions. A written prompt with steps exists; the planning session changes no repository code, and no live run against a provider occurs. The Product Owner's Proceed, implementation and independent PR reviews follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.05 (confidence 0.87); rung probabilities low 0.00, medium 0.07, high 0.82, extra high 0.10, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.73, Sonnet 5.5 0.25, Haiku 5.5 0.01 (confidence 0.64). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.008, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.051, Opus 5.5 at high 0.599, Opus 5.5 at extra high 0.073, Opus 5.5 at max 0.007, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.018, Sonnet 5.5 at high 0.205, Sonnet 5.5 at extra high 0.025, Sonnet 5.5 at max 0.003, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.001, Haiku 5.5 at high 0.008, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T18:23:10Z. Nathan picks the cell.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for PR-20 (WU-PR-02) and none for this PR-10 session (its reading is the WU-PR-01 lineage review §13). None is recorded.
* **Surface advice (PR-20, WU-PR-02).**
  * Run it in a new dedicated top-level Claude Code cloud session for the WU-PR-02 PR role on `amthorn78/glow-hdengine-v2`, started after this instruction's pull request merges. The same session then receives PR-30 after Nathan's Proceed. PR-35 runs in its own session.
  * Read access is needed to `main`: this instruction and its referenced artifacts; `docs/pfcanon/`; and the code §4 names.
  * A local closed-rails virtualenv with CI's install, run through `env -i` after `git fetch --unshallow`, is needed for the throwaway-clone prototype and the classifier and pre-push probes.
  * Write access is needed to one branch and one pull request under `docs/ephemeral/` for the plan.
  * Not needed: open rails, or vendor, Railway, database or Notion writes.

## 15. Nonclaims

This instruction is not Product Owner implementation approval. It is not a PR-20 plan, Proceed, implementation, CI result, QA, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum or closure. Nothing outside `docs/ephemeral/` is changed.
