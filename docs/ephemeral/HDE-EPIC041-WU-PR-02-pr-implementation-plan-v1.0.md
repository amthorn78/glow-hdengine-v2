---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC041-WU-PR-02-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
approval_hold: "ASK OK? — PR IMPLEMENTATION PLAN"
predecessor: none (first plan for WU-PR-02)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-02
work_unit_title: "WU-PR-02 — Caller migration, legacy retirement and boundary reconciliation (HDE-SEPA006.2; reconciliation part of .3)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; 29,326 bytes; git blob 52faaba5d08857c2cdc391c95360a716260dc187; merged by amthorn78/glow-hdengine-v2#794 as d09de6ea)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; 37,557 bytes; git blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE, ASK OK.; git blob 2ca19d33c1098fde7f606e2a09ee9e884f1ba7f3)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; git blob 9decb6085a64a9d0c2b7b8919e97ef3627a2846a; corrected for later stages by AUD-CORR-1 in the WU-PR-01 lineage review §10)
DEPENDENCY_REF: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-01; git blob 20e9d51c481db2485163a12d2cb3193d86348501; merged by #793 as 3c2f7788)
REMEDIATION_REVIEW_ID: none (no remediation lineage)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
immutable_approved_base: Specification v1.1 (Thoth, CF-E-30 review v1.1) → Implementation Plan v1.1 (Isis, IA-30 review v1.1)
effective_baseline: "approved base + applicable PF10 overlays (HDE Build Notes addendum 2.2 for its scope, as I-7; addendum 2.3 as the WU-PR-01 lineage record)"
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md (661 lines, 73,639 bytes, sha256 2a43e518f13219569ee3de74f544af9c176a648c8f40c926673671fae164c213; the only PF10 file on main at d09de6ea; read in this session: front matter and precedence rules 1 to 9, addendum index, addendum 2.1's decision table, D-2 and scope sections, addenda 2.2 and 2.3 in full; provenance, not a gate)
pf10_addenda_applicable: "addendum 2.2 'Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close' (R-1, R-2 constrain this unit's code and tests); addendum 2.3 (the WU-PR-01 lineage record; its deferred-obligations table names this unit's carried items). Both are sections of docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md; no separate addendum file exists. Addendum 2.1 (S19) is not engaged"
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff (see §12)
repository_baseline: origin/main d09de6eaedf8ae779a857d4a154459a94be2f87a (#794). `git diff --stat e72c9bac d09de6ea -- . ':!docs/'` is empty, so every byte outside docs/ equals the WU-PR-01 squash; the instruction's baseline 9f681bdf differs from d09de6ea only by the instruction itself under docs/ephemeral/
working_branch: claude/kind-lovelace-30iyf2 (this plan's documents only)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01Q789u2FkMeZpy3U2W5XTh9 (the dedicated WU-PR-02 PR engineering session Nathan created; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9; page state 2026-10-27T13:18:23.839Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1 (carried from the instruction; the PR-20 and PR-30 pages read sit under "HDE IA — GCFPE-20261027.1 — 102726.1"; the register was not re-read in this session)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; CCR-3 re-checked at d09de6ea, not triggered; no new entry (§18)
created_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES: see §21
---

# HDE-EPIC041 WU-PR-02 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED for v1.0.** This is the complete plan for WU-PR-02 within the instruction's scope. It does four things:

* migrates C-1, C-2 and C-3 to WU-PR-01's interfaces;
* deletes `engine/charts/loader.py` and the characterization test, with no shim;
* adds a repository-wide import guard and a generator behavior test;
* updates three owner mappings and adds one retired-test row.

The plan fixes the names, paths and choices the instruction leaves to PR-20 (§5). A prototype ran in throwaway clones (§12):

* the 56 tests of the focused set pass;
* the guard flags exactly the five files of §4 on the unchanged base (the loader and its four importers) and fails on planted importers at the prototype head; the generator test fails if the loader is deleted without migrating C-1; the migrated C-3 passes with the clock pinned at 12:34 UTC, where today's C-3 fails (OBS-4);
* the classifier, as `ci.yml` calls it, selects all seven lanes and 170 changed-test targets;
* every changed path is a non-member; admission reports `1.3.0`, 45 members and `release_id` 77204764…, unchanged;
* the 170 targets: 3,660 passed on the prototype head, with the tree clean (§12.4);
* the full local `ci.yml` replay passes all 16 steps and ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (§12.5);
* `artifacts/compat/` is byte-unchanged and every run left the tree clean.

PR-30 applies the companion diff, re-runs §11 and publishes one PR.

This plan authorizes nothing. Only the Product Owner's `PR Implementation Proceed` (PR-30) for exactly v1.0 authorizes implementation, and only the Product Owner merges.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Lineage and sources read in this session

* **Instruction v1.0**, read in full at d09de6ea (blob 52faaba5…, the blob #794 landed).
* **Implementation Plan v1.1**, read in full. **IA-30 review v1.1** (INITIAL_APPROVE), read for this unit: its business-case check (WU-PR-02 "Passes"), the RL-3 (c) and RL-8 application rows (the deletion, retired row and registrations; the embedded search) and the N-5 nit, which has no effect here.
* **Implementation Audit v1.0**: §5 (caller inventory C-1 to C-4, H-1 to H-4, N-1), O-05, O-11 to O-13, O-20, ED-04 to ED-10, D-1 (§8.1), FND-005 to FND-007.
* **WU-PR-01 records:** the instruction v1.0's interface section (§3) as landed; the plan v1.0 in full; the PR-35 result v1.5 in full; the PR-40 lineage review v1.0 in full (ACCEPT; §10 OBS-1, OBS-4, AUD-CORR-1, the addendum bearing).
* **Prompts (Notion):** PR-20 102726.1 in full; PR-30 102726.1 in full (receiver contract; page state 2026-10-27T13:15:20.197Z).
* **Skills:** `glow-hde-pr-development` 1.5.0, "Execute the two-phase engineering lifecycle" through "Control remote-action cost", read as the PR-30 and PR-35 contract (it is not used for planning); the TypeSafe scoring skill (request v8.2), for §20.
* **Code read at d09de6ea:**
  * `engine/charts/loader.py` (173 lines, blob 8ea4dce2…);
  * `engine/charts/pure.py` and `adapter/chart_orchestration.py` (WU-PR-01's interfaces, unchanged by this unit);
  * `scripts/make_compat_determinism_artifacts.py`;
  * all five `tests/loader/*.py`; the four WU-PR-01 test files;
  * `tests/conftest.py`; `pytest.ini`; `tests/retired_tests.md`;
  * `ci/checks/classify_ci_changes.py`: `_HISTORICAL_PREFIXES`, `_DOCUMENTATION_PREFIXES`, `_PRODUCT_TEST_OWNER_PATHS`, `_product_owner_targets`, `changed_test_targets`;
  * the `test` job of `.github/workflows/ci.yml` (classification, isolated changed tests, lanes, final applicability);
  * `tests/evidence/test_architecture_snapshot.py`; existing subprocess idioms (`tests/compliance/test_release_id_precedence_and_grep_guard.py`, `tests/evidence/test_v2_mapped_cache_evidence.py`);
  * `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` (no row names `engine/charts`, `loader_call` or the generator).

## 3. Business case (as the PR Instruction states it; the Proceed is given against it)

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

Each measure maps to a §11 item: absence and guard, items 1, 3 and 8; C-1, item 1 (generator test) and item 2; compat bytes, item 2; retained coverage, item 1; clean tree, items 1, 4 and 6.

## 4. Baseline re-check (instruction §4, at d09de6ea)

| Fact | At d09de6ea |
| :- | :- |
| Code since WU-PR-01's squash `e72c9bac` | `git diff --stat e72c9bac d09de6ea -- . ':!docs/'` empty. Under `docs/pfcanon/` the only change is HDE Build Notes (now the v13.9.2 file) |
| `engine/charts/loader.py` | blob 8ea4dce2602d…, 173 lines, unchanged |
| `engine/charts/` | `loader.py` and `pure.py`; no `__init__.py` |
| C-1, C-2, C-3, `pytest.ini`, `tests/retired_tests.md` | blobs b3879105…, a97eadab…, 758b5edf…, 6c2833bd…, ea44b462…; the same as at the Audit's head, as the instruction records |
| C-1 run from a temporary CWD (closed rails, `env -i`) | exit 2, stderr `compat_public not implemented`, nothing created |
| `artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt` | blobs 7fe71f99…, 7fe71f99…, 7e6176a2… |
| `artifacts/logs/loader_call.jsonl` | blob 92556952… |
| Instruction §3.3 inventory pattern, outside `docs/pfcanon/` and `docs/ephemeral/` | 67 files: 23 live paths and 44 under the historical captures (§13.3 has the head's list) |
| Tracked `.py` files importing the loader, outside the classifier's historical prefixes | `engine/charts/loader.py` itself, C-1, C-2, C-3, the characterization file. No other |
| Owner mappings | `engine/charts/pure.py` and `adapter/chart_orchestration.py` list the characterization file; none for the loader or C-1 (O-13) |
| Release membership | admitted release `1.3.0`, 45 members, `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; every planned path "not-member" |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md`, the only PF10 file; `prepush_check.py build-notes` PASS with the sha256 in the front matter |
| CCR-3 | not triggered (§18) |

## 5. Design decisions (the names, paths and choices the instruction leaves to PR-20)

| ID | Decision | Basis |
| :- | :- | :- |
| PD-1 | **C-2 and C-3 are migrated in place**: same paths, same test function names, same `pytest.ini` `testpaths` (lines 72, 74) and classifier roster (lines 112, 114) entries. No retired row for either. | Instruction §3.1 permits either. In place keeps every registration, so `pytest.ini` and the roster do not change. `tests/retired_tests.md` names `tests/loader/test_loader_logs_keys_only.py` as the replacing coverage for a retired provider-logging test; that reference stays valid |
| PD-2 | **C-1 changes one line**: `from engine.charts.loader import load_chart` becomes `from adapter.chart_orchestration import load_chart`. The call `load_chart(**a)` is textually unchanged because the name is the same; it now resolves to the orchestration entry in the same keyword form. | Instruction §3.1 C-1; Audit ED-07. The keyword form with `tz` and the generator's two literal inputs are already pinned by WU-PR-01's `test_positional_and_keyword_forms_return_the_fixture_chart` |
| PD-3 | **C-2** calls the entry with `log_sink=lines.append`, catches `engine.charts.pure.ChartInputError`, and keeps its two assertions in substance: the normalized fixture result (now `meta.provider == "fixtures"`; the old set also allowed `legacy` and `internal_engine`, which the retired path produced and nothing now can) and the tz-absent typed error (`READER_INVALID_INPUT`, field `tz`). Each test also asserts one log line. No `_Path` patch. | Instruction §3.1 C-2 |
| PD-4 | **C-3** calls the entry with `log_sink=data.append` and `SAFE_MODE=1` by `monkeypatch`. It keeps its key, route, `duration_ms`, `safe_mode` and correlation-id assertions. `ts` is pinned to `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$` and removed from the raw line before the substring check, as WU-PR-01's `test_log_line_is_keys_only` does (ID-35-1). The forbidden list is unchanged. | Instruction §3.1 C-3; OBS-4. Prototype §12.3: passes with the clock pinned at 12:34:00Z, where today's C-3 fails |
| PD-5 | **Import guard:** `tests/charts/test_chart_loader_import_guard.py`, four tests (§7). The file walk is `git ls-files -z -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/'`, so those two trees are never listed or read; then the classifier's `_HISTORICAL_PREFIXES` and the guard's own path are skipped. Nothing else is excluded. | Instruction §5; I-7 (HDE Build Notes addendum 2.2, R-1, which lists path exclusions of those trees as a conforming use). The classifier's prefixes are imported (`from ci.checks import classify_ci_changes as classifier`, as seven existing tests do), so the guard cannot drift from them |
| PD-6 | **What the guard flags** (AST, per file): `import engine.charts.loader[.x]`; `from engine.charts.loader[.x] import …`; `from engine.charts import loader`; a relative `from` import that resolves to `engine.charts.loader` from the file's own package; a string constant that is exactly the module's dotted name, or that name followed by `.attr` or `:attr` (the `importlib.import_module`, `__import__`, `mock.patch` and `monkeypatch.setattr` target forms); and `_call_legacy` as a name, an attribute, a definition, an imported name or an exact string. **It does not flag** the module name inside a longer string, a path string, or a comment. | The purity test `tests/charts/test_chart_pure_purity.py` (must not change, instruction §4) holds the planted string `"from engine.charts.loader import load_chart\n"` as source text for its own AST checker, and the classifier must hold the key `"engine/charts/loader.py"` (instruction §3.3). Neither is an import. Restoring the module at its path is caught by the guard's path test, which also owns that path in the classifier (PD-8) |
| PD-7 | **A tracked `.py` file that does not parse is searched as text** for `engine.charts.loader` or `_call_legacy`. | A real input on `main`: `scripts/scratch.py` (469 bytes, from `b2e011f5`) holds Markdown notes and raises `SyntaxError`. Excluding it is not permitted (the guard "excludes only" the listed paths), so it is scanned the only way it can be |
| PD-8 | **CI registration**, all in `_PRODUCT_TEST_OWNER_PATHS` of `ci/checks/classify_ci_changes.py`: (a) remove the characterization file from the `engine/charts/pure.py` and `adapter/chart_orchestration.py` entries; (b) add `"engine/charts/loader.py": ("tests/charts/test_chart_loader_import_guard.py",)`; (c) add `"scripts/make_compat_determinism_artifacts.py": ("tests/scripts/test_make_compat_determinism_artifacts.py",)`. **`pytest.ini`, the roster and `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` do not change.** | Instruction §3.3. Probed (§12.2): without (b), `CI_PRODUCT_OWNER_TEST_MISSING:engine/charts/loader.py`; without (c), `CI_PRODUCT_OWNER_TEST_MISSING:scripts/make_compat_determinism_artifacts.py`; with the characterization file left in an entry, `CI_FULL_VALIDATION_TEST_INVALID:ci/checks/classify_ci_changes.py:tests/adapter/test_chart_orchestration_characterization.py`. Registered owners join full validation automatically, as WU-PR-01's PD-4 found, so both new test files reach CI without a `testpaths` entry |
| PD-9 | **Generator test:** `tests/scripts/test_make_compat_determinism_artifacts.py`, one test. It runs `[sys.executable, scripts/make_compat_determinism_artifacts.py]` with `cwd=tmp_path` and `PYTHONPATH` = the checkout root prepended to the inherited value, and asserts `(returncode, stdout, stderr) == (2, "", "compat_public not implemented\n")` and an empty `tmp_path`. | Instruction §5. The `PYTHONPATH` idiom is the repository's (`tests/compliance/test_release_id_precedence_and_grep_guard.py`); it makes the child import the checkout under test. Basename unique |
| PD-10 | **Retired row** for the characterization file, inserted in the table's path order (after `tests/adapter/test_cache_keys.py`): reason "Compared adapter/chart_orchestration.py with engine/charts/loader.py, which HDE-EPIC041 WU-PR-02 removes together with its legacy load_chart(user_id) signature (Product Owner decision D-1); it cannot run without the removed module."; date = the UTC date of PR-30's commit; replacing coverage `tests/adapter/test_chart_orchestration.py` (the fixture chart, its canonical bytes, and each error code, field and message, asserted as literal values). | Plan v1.1 §6 WU-PR-02 Scope. The row cites no planning document (R-1). The loader row stays byte-identical; inserting above it moves it from line 57 to line 58 (I-6 protects its content, "as history", Audit H-4). The QA-02 row-format check passes on 67 rows |
| PD-11 | **No new assertion that `engine/charts/` holds only `pure.py`.** I-2 is evidenced in the reconciliation record (`git ls-tree` of `engine/charts/` at the PR head) and by the guard's path test. | The instruction's guard specification does not include it, and a future module there must be registered (`CI_PRODUCT_OWNER_TEST_MISSING`) anyway |
| PD-12 | **Comments and docstrings** in the new and changed files cite HDE-EPIC041, the work unit and HDE-SEPA006 task IDs only. No PF file name, version, digest or addendum number appears in code. | HDE Build Notes addendum 2.2, R-2 and its note on addendum numbers in comments |

## 6. Files and components, with each component's real inputs (PR-20 Execute step 3)

| Path | Change | Component | Real inputs | Outside the real set: the one refusal or stated limit |
| :- | :- | :- | :- | :- |
| `scripts/make_compat_determinism_artifacts.py` | modified, 1 line | C-1, the compat-determinism generator | Its own literal birth data; the CWD of the operator's shell or of CI; the importable checkout | No new argument and no logic change (ED-07). Its exit 2 before the chart call is preserved; restoring its compat computation is FND-005, out of scope |
| `engine/charts/loader.py` | deleted (173 lines) | The mixed loader, its legacy signature, `_call_legacy`, the `resolve_provider` import and the `{"gates":[1,2,3]}` fallback | — | No shim (ED-06, D-1). An import of the old path raises `ModuleNotFoundError`; that is the intended refusal |
| `tests/adapter/test_chart_orchestration_characterization.py` | deleted (70 lines) | WU-PR-01's equality check against the loader | — | Its literal-value coverage remains in `tests/adapter/test_chart_orchestration.py` |
| `tests/loader/test_load_chart_fixture_only.py` | migrated in place, 2 tests | C-2 | The literal inputs `1990-01-01`, `12:34`, `Amsterdam, NL`, `Europe/Amsterdam`, `CID-deadbeefdeadbeef` | — |
| `tests/loader/test_loader_logs_keys_only.py` | migrated in place, 1 test | C-3 | The same literals; `SAFE_MODE` from `monkeypatch`; the runner's clock | The clock appears only in `ts`, which is pinned to its shape and excluded from the substring check (OBS-4) |
| `tests/charts/test_chart_loader_import_guard.py` | new, 143 lines, 4 tests | Repository-wide import guard | The tracked `.py` files of the checkout outside `docs/ephemeral/`, `docs/pfcanon/` and the classifier's historical prefixes; the checkout's `git` index; the classifier's prefix tuple | Untracked or generated files are not inputs (stated limit). A module name assembled at run time from parts, or code held in a string and executed, is not recognized (stated limit; the inventory, §13.3, finds none outside the listed members). A tracked `.py` that is not Python is searched as text (PD-7) |
| `tests/scripts/test_make_compat_determinism_artifacts.py` | new, 23 lines, 1 test | Generator behavior test | The script, run as a subprocess from a temporary CWD with the checkout on `PYTHONPATH` | — |
| `ci/checks/classify_ci_changes.py` | +7 −6 in `_PRODUCT_TEST_OWNER_PATHS` (PD-8) | Owner mappings | The changed-path list CI passes | Unchanged behavior for every other path |
| `tests/retired_tests.md` | +1 row (PD-10) | Retirement registry | — | Row 57's content unchanged |

**Not changed** (instruction §4): `engine/charts/pure.py`; `adapter/chart_orchestration.py`; `engine/util/input_validators.py`; `engine/config/provider_loader.py`; `engine/providers/*`; `engine/provider/*`; `catalog/manifest.json` and `engine/config/registry_loader.py`; `pytest.ini`; `artifacts/compat/*`; `artifacts/logs/loader_call.jsonl`; any governed evidence; `docs/pfcanon/`; the historical captures; `tests/loader/test_loader_hdapi_ignores_tz.py`, `test_pinned_lists_not_empty.py` and `test_validators_strict.py`; the other WU-PR-01 test files.

## 7. Behavior contracts (as prototyped)

**Import guard** (`tests/charts/test_chart_loader_import_guard.py`):

| Test | Asserts |
| :- | :- |
| `test_no_tracked_python_file_imports_the_retired_loader` | The scanned set contains C-1, C-2 and C-3 (the walk is not vacuous), and `scan` finds nothing in any scanned file |
| `test_the_retired_module_path_does_not_exist` | `engine/charts/loader.py` does not exist and is not tracked |
| `test_checker_flags_every_import_form` | 18 planted sources, one per form of PD-6 (plain, aliased, `from`, `from engine.charts import`, a mixed import list, three relative forms, `import_module`, `__import__`, `monkeypatch.setattr` target, `mock.patch` entry-point target, and five `_call_legacy` forms), plus an unparseable text source (PD-7): each is flagged |
| `test_checker_ignores_text_that_is_not_an_import` | The real non-import forms (the purity test's planted string, the classifier's path key, a comment, an import of `engine.charts.pure`, `from . import pure` inside `engine/charts/`, `from .loader import x` inside `engine/narratives/`, which resolves to the real `engine.narratives.loader`) and an unparseable text naming only the entry: none is flagged |

**Generator test:** as PD-9.

**Migrated C-2 and C-3:** as PD-3 and PD-4.

## 8. Requirement-to-change/test map (PR-20 Execute step 4)

| Obligation (source) | Change | Test or evidence |
| :- | :- | :- |
| R-03 / AC-03: every supported caller migrated; an import-path rename alone is not migration (instruction §3.1; Specification R-03; PF09.3 HDE-SEPA006.2) | C-1 to the orchestration entry; C-2 and C-3 to the entry with an injected sink and the pure error | Generator test; migrated C-2 and C-3; the guard. C-2 and C-3 drop the `_Path` patch and the file read, so they test the new contract (sink, typed error), not a renamed import |
| D-1 / C-4: retire the legacy signature | `engine/charts/loader.py` deleted, no shim | Guard path test; `TypeError` for legacy shapes stays pinned by WU-PR-01's `test_other_argument_shapes_raise_type_error_and_log_one_error_line` |
| R-01 / AC-01 residual, I-2: no R-01 concern under `engine/charts/` | The loader deleted | Reconciliation (§13.3): `git ls-tree` of `engine/charts/` = `pure.py`; every R-01 concern located in `adapter/chart_orchestration.py` |
| R-04 / AC-04: verify the complete migration; reconcile R-01 to R-03 | — | §11; the reconciliation and AC-04 record in the PR (§13) |
| AC-05 / I-4: outputs and failures preserved | — | Generator test and item 2 (exit 2, stderr, no write); `git diff --exit-code -- artifacts/compat/`; WU-PR-01's literal-value tests |
| AC-05 / I-3: no fallback, acquisition, provider contract, route, flag, CLI option or release-member change | Removing the loader removes its fallback and its `resolve_provider` path | `prepush_check.py membership` (all not-member); code review: the diff adds no import of a resolver, provider, vendor, HTTP or CLI module |
| AC-05 / I-5: clean tree | — | `git status --porcelain --untracked-files=all` empty after items 1, 4 and 6; CI's changed-tests and final steps enforce it too |
| I-1: `engine/charts/pure.py` unchanged; nothing imports `input_validators` into a pure path | — | The diff path list (§12.1) |
| I-6: historical captures, `loader_call.jsonl`, row 57, `input_validators`, `provider_loader`, `engine/provider*/` unchanged | — | The diff path list; PD-10 |
| I-7 (HDE Build Notes addendum 2.2, R-1, R-2) | Pathspec exclusions in the guard; no PF name or version in code (PD-12) | Code read of the diff; PR-40 |
| OBS-4 | C-3's clock-safe check (PD-4) | Pinned-clock run (§12.3) |
| Instruction §3.3 CI facts | PD-8 | Classifier run as `ci.yml` calls it; the three fail-closed probes (§12.2) |
| Plan v1.1 §6 WU-PR-02 Tests: retained coverage | — | The two PF09.3 tests and WU-PR-01's three remaining test files, in item 1 |
| HDE Mechanics Guide §1.1: migrate generator callers; preserve canonical outputs; no fallback, no Engine I/O exception, no second resolver | C-1; the loader deleted | Generator test; compat bytes; no new module under `engine/` |
| HDE Architecture §1.1 purity rule | — | WU-PR-01's purity tests in item 1 |
| Doc-Delta (Change Process Guide §0.2; HDE Governance §9.2) | none in this unit | HDE Architecture §1.1 and HDE Mechanics Guide §1.1 describe the loader as current reality "until separately remediated"; removing it makes that text the drainage target DELTA-001 and DELTA-002, which Plan v1.1 assigns to WU-PR-03 (carried in its PR description; no canon edit). No README, AGENTS.md or non-canon `docs/` file names the loader (§13.3) |

## 9. Implementation sequence for PR-30

1. **Recover before creating.** Inspect the session's checkout, branches, worktrees, open PRs and `docs/ephemeral/` for WU-PR-02 work. Expected: the instruction, this plan, its diff, and this plan's own documents PR.
2. **Branch** from current `origin/main` on the session's designated branch, after `git fetch --unshallow` if the clone is shallow (OBS-5). If `main` moved past d09de6ea outside `docs/`, re-run §4 first and record any difference. A change to any §6 file, to `engine/charts/pure.py`, `adapter/chart_orchestration.py`, the WU-PR-01 test files or `tests/charts/test_chart_pure_purity.py` is reconciled before applying.
3. **Apply** `docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff` (`git apply --check`, then `git apply`). A hunk that fails (the classifier and `tests/retired_tests.md` are the files most likely to move) is applied by hand to the same effect and recorded under *In-flight decisions*.
4. **Set the retired row's date** to the UTC date of the commit (PD-10). The prototype carries 2026-10-28.
5. **Local checks**, §11 items 1 to 8, under `env -i` closed rails.
6. **Commit once:** `refactor(charts): migrate chart-loader callers, remove engine/charts/loader.py and guard against its return (HDE-EPIC041 WU-PR-02, HDE-SEPA006.2)`.
7. **Replay** `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit (§11 item 9), with no other tool call touching the checkout while it runs.
8. **Publish** one PR. Description: the `.github/pull_request_template.md` headings with the AGENTS.md content rules.
   * "Why": the instruction, HDE-SEPA006.2 and D-1.
   * "What changed": by path, as §6.
   * "Checks run": the AC-04 record and the reconciliation (§13).
   * "Not in this PR": WU-PR-03 (CHANGELOG, documentation sweep, Doc-Delta notes DELTA-001 and DELTA-002); FND-005 to FND-007.
   * "What merging does": the callers use the Adapter entry, `engine/charts/loader.py` and the legacy signature are gone, and the guard runs in CI; it establishes no QA, acceptance or closure; no merge-order dependency.
   * State that the PR runs all seven lanes because it changes the classifier, and record the one intended behavior fact: the legacy-routed shapes have raised `TypeError` since WU-PR-01, and that is now the only behavior.
9. **Result record** `docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-result-v1.0.md` (`PR_IMPLEMENTATION_RESULT`): `PR_CANDIDATE_PUBLISHED`, tested-source SHA, the AC-04 fields, *In-flight decisions*, `PR_REMOTE_ACTION_LEDGER`, nonclaims. Hand off to PR-35 in its own session.

**Integration seams:** C-1 → `adapter.chart_orchestration.load_chart` (keyword form); C-2 and C-3 → the same entry with `log_sink`, and `engine.charts.pure.ChartInputError`; the guard → `ci.checks.classify_ci_changes._HISTORICAL_PREFIXES` and `git ls-files`; the classifier's `_PRODUCT_TEST_OWNER_PATHS` lookup in `_product_owner_targets` and `changed_test_targets` (no code change there). **Order inside the commit:** one commit; the migration and the removal must land together (Plan v1.1 RK-02: removal before migration turns C-1's exit 2 into an import error, which the prototype reproduced, §12.3).

## 10. PR split and merge dependencies

* **One PR**, one coherent change; reversible by revert, which restores the module, the characterization test and the callers.
* **Before it:** this plan's documents PR merged (it carries the companion diff PR-30 applies). WU-PR-01 is merged and accepted (§4; the lineage review).
* **Before its merge:** PR-35's `MERGE_PENDING`; Nathan merges.
* **After it:** PR-40 lineage review; ACCEPT returns to the whole-change IA, which issues WU-PR-03's instruction (Plan v1.1 §6).
* **No release member changes** (§4), so no manifest refresh and no evidence regeneration.

## 11. Validation PR-30 runs (PR-35 re-runs items 1 to 6 after any correction)

**Environment.** CPython 3.12 with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`, the editable install pointed at the checkout under test); `git`, `bash`; `env -i` with `HOME`, a `PATH` that includes the directory holding `ruby` (`/usr/local/bin` in this container, OBS-8), `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and `PYTHONPATH=<checkout>`. The container exports database, vendor and GitHub credentials; without `env -i` they reach the tests (OBS-2). Record environment probes as SET/UNSET only. `ruby` and `curl` are needed: eleven of the 170 targets and the sweep call `ruby` (OBS-8).

1. **Focused set:** `python -m pytest -q -p no:cacheprovider tests/charts tests/adapter/test_chart_orchestration.py tests/loader tests/scripts/test_make_compat_determinism_artifacts.py tests/core/test_engine_core_purity.py tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` → expected 56 passed (guard 4, generator 1, C-2 2, C-3 1, WU-PR-01's three files 33, the other three `tests/loader` files 7, core purity 6, retained 2); then `git status --porcelain --untracked-files=all` empty.
2. **Generator and compat bytes:** run C-1 from a new temporary directory under `env -i` (`python <checkout>/scripts/make_compat_determinism_artifacts.py`) → exit 2, stderr `compat_public not implemented`, directory empty; `git diff --exit-code -- artifacts/compat/` → exit 0.
3. **Negative proofs in a throwaway copy** (never in the PR checkout): (a) the guard on the unchanged base, with only the guard file added, fails `test_no_tracked_python_file_imports_the_retired_loader` and `test_the_retired_module_path_does_not_exist`, listing exactly the five files of §4; (b) on the candidate, appending `importlib.import_module("engine.charts.loader")` to one tracked test file, or `from engine.charts import loader` to `adapter/chart_orchestration.py`, fails the guard; (c) the migrated C-3 passes with `adapter.chart_orchestration._dt` replaced by a clock fixed at 12:34:00Z (§12.3 has the harness).
4. **Classifier as `ci.yml` calls it:** `python3 ci/checks/classify_ci_changes.py --base <base SHA> --head <head SHA> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>` → exit 0, `reason=selected_lanes`, all seven lanes, 170 targets including the guard, the generator test and the migrated C-2 and C-3. Then the targets run as CI's isolated changed-tests step runs them (a detached worktree of `HEAD`, `PYTHONPATH` = that worktree), followed by `git diff --exit-code` and an empty `git status --short --untracked-files=all` → expected 3,660 passed, diff and status clean. A failure that also fails on the base is not this unit's (compare with a base run of the same list minus the two new files, as §12.4 did); any other failure is.
5. **Pre-push:** `python tools/ci/prepush_check.py --base <base> --head HEAD --path <each of the 9 paths> lanes membership build-notes` → PASS; every path not-member; HDE Build Notes resolved to the one current file; and `python tools/ci/prepush_check.py sweep --no-run` → PASS, `uncovered=0`.
6. **Admission unchanged:** `load_active_mechanics_bundle()` succeeds with `1.3.0`, 45 members, `release_id` 77204764…; `python scripts/release_id_recompute.py --check-manifest-only` exit 0.
7. **Inventory re-run** at the commit (§13.3 pattern and scope), with a disposition per member, written into the PR record.
8. **Guard path facts:** `git ls-files engine/charts/` lists only `engine/charts/pure.py`; `test -e engine/charts/loader.py` fails.
9. **Replay:** `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit, nothing else touching the checkout while it runs → PASS, steps 01 to 16 SUCCESS, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, "repository unchanged" (§12.5).

## 12. Prototype record

Throwaway clones under this session's scratchpad, at d09de6ea; the session checkout was not changed and every clone ended clean. Environment: CPython 3.12.3 venv with CI's install, the prototype clone installed editable; git 2.43.0. The prototype was committed only in its clone. The companion diff is `git diff d09de6ea <prototype head>`.

### 12.1 Change set and companion diff

* Prototype head `3c8ab6278642be75106ebca7944e4b124cb811b9` (scratch clone only; never pushed).
* `git diff d09de6ea 3c8ab627`: 9 files, +196 −274.

  | Path | + | − |
  | :- | -: | -: |
  | `ci/checks/classify_ci_changes.py` | 7 | 6 |
  | `engine/charts/loader.py` (deleted) | 0 | 173 |
  | `scripts/make_compat_determinism_artifacts.py` | 1 | 1 |
  | `tests/adapter/test_chart_orchestration_characterization.py` (deleted) | 0 | 70 |
  | `tests/charts/test_chart_loader_import_guard.py` (new) | 143 | 0 |
  | `tests/loader/test_load_chart_fixture_only.py` | 10 | 11 |
  | `tests/loader/test_loader_logs_keys_only.py` | 11 | 13 |
  | `tests/retired_tests.md` | 1 | 0 |
  | `tests/scripts/test_make_compat_determinism_artifacts.py` (new) | 23 | 0 |

* Nothing under `engine/charts/pure.py`, `adapter/`, `engine/util/`, `engine/config/`, `engine/provider*/`, `catalog/`, `pytest.ini`, `.github/`, `docs/evidence/`, `artifacts/`, `audit/` or `docs/pfcanon/`.
* Companion diff: `docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff`, 572 lines, 26,082 bytes, sha256 `70ebf3a3d3b96debcc93e41512cf5798c4e39b8e111bdd4f797e211f7e49d565`; `git apply --check` clean on d09de6ea, and applying it there gives tree `6844997032c40e42e854b0584ff9259c45e99742`, the prototype head's tree.

### 12.2 Classifier, lanes, membership, admission (on 3c8ab627)

| Run | Result |
| :- | :- |
| `classify_ci_changes.py --base d09de6ea --head 3c8ab627 --event-name pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=9;lanes=product,compat,db,rails,evidence,qa,release`; `changed_tests=true`; 170 targets, including `tests/charts/test_chart_loader_import_guard.py`, `tests/scripts/test_make_compat_determinism_artifacts.py`, `tests/loader/test_load_chart_fixture_only.py` and `tests/loader/test_loader_logs_keys_only.py` |
| `changed_test_targets` with one mapping removed or kept (in-process probe) | as prototyped: accepted; without the loader mapping: `CI_PRODUCT_OWNER_TEST_MISSING:engine/charts/loader.py`; without the generator mapping: `CI_PRODUCT_OWNER_TEST_MISSING:scripts/make_compat_determinism_artifacts.py`; the characterization file left in an owner entry: `CI_FULL_VALIDATION_TEST_INVALID:ci/checks/classify_ci_changes.py:tests/adapter/test_chart_orchestration_characterization.py`. The instruction recorded `CI_REGISTERED_OWNER_TEST_DELETED` for the deletion alone; with the classifier also changed, the full-validation check reports it first. Both fail closed |
| `prepush_check.py --base d09de6ea --head HEAD` with the 9 paths, `lanes membership build-notes` | PASS; 170 targets; not-member ×9; admitted release `1.3.0`, roster 45, `release_id` 77204764c225…; HDE Build Notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md`, 73,639 bytes, 2a43e518…; "repository unchanged"; exit 0 |
| `prepush_check.py sweep --no-run` (in a separate clone at 3c8ab627) | PASS; `tracked_test_files=220`, `full_validation_targets=170`, `uncovered=0`; "repository unchanged" |
| `tests/retired_tests.md` row check (the QA-02 `awk` form) | 67 rows, none malformed; none of the 67 paths is tracked |

### 12.3 Behavior and negative probes (closed rails, `env -i`)

| Probe | Result |
| :- | :- |
| Base C-1 from a temporary CWD | exit 2; stderr `compat_public not implemented`; nothing created |
| Inventory search at the base and at the head | 67 files at d09de6ea; 66 at 3c8ab627. The only differences: `engine/charts/loader.py` and the characterization file leave, the guard file joins |
| Tracked `.py` files outside the excluded trees | 519 scanned at the head; one does not parse: `scripts/scratch.py` (Markdown notes) → PD-7 |
| N1: the guard on the base (only the guard file added) | 2 failed, 2 passed. Flagged: `engine/charts/loader.py` (`_call_legacy` definition and name), C-1 (`from engine.charts.loader import`), the characterization file, C-2 and C-3 (`import` and `from` forms). `tests/charts/test_chart_pure_purity.py` not flagged |
| N2: planted importers at the head | `importlib.import_module("engine.charts.loader")` appended to `tests/loader/test_validators_strict.py` → guard fails, naming that file and `string 'engine.charts.loader'`; `from engine.charts import loader` appended to `adapter/chart_orchestration.py` → guard fails. Both reverted |
| N3: the generator test | passes on the base (C-1 exits 2 before its chart call, so the test alone does not prove the migration); fails with the loader deleted and C-1 unmigrated (`ModuleNotFoundError`, exit 1); passes on the prototype. The guard is what proves the import changed |
| N4: the clock pinned at 12:34:00Z (`<module>._dt` replaced by a fixed clock, then pytest on C-3) | migrated C-3: 1 passed. Today's C-3 on the base: 1 failed, `assert '12:34' not in '{"ts":"2026...'` (OBS-4 reproduced) |

### 12.4 Tests (`env -i` closed rails)

| Run | Result |
| :- | :- |
| Focused set (§11 item 1), 18:45:47Z to 18:45:54Z | 56 passed; status empty |
| First run, the 170 targets on 3c8ab627 as CI's isolated step (a detached worktree), 18:43:30Z to 18:51:06Z, with a `PATH` that omitted `/usr/local/bin` | 3,649 passed, 11 failed; diff clean, status empty |
| The same list without the two new files (168) on d09de6ea, same `PATH`, 18:51:08Z to 18:58:47Z | 3,644 passed, 11 failed; diff clean, status empty |
| Failure sets compared | identical: the 11 tests that call `ruby` (OBS-8) |
| Those 11 re-run with `/usr/local/bin` on `PATH`, 18:59:32Z (head) and 19:00:09Z (base) | 11 passed on each; status empty |
| **The 170 targets on 3c8ab627, corrected `PATH`, 19:01:16Z to 19:09:42Z** | **3,660 passed** (the base's 3,655 plus the guard's 4 and the generator test's 1); diff clean, status empty |
| Compat bytes | `git diff --exit-code -- artifacts/compat/` exit 0 after every run |

### 12.5 Local `ci.yml` replay

`python tools/ci/prepush_check.py --base d09de6ea --head HEAD --full replay` on 3c8ab627, 19:09:43Z to 19:33:38Z, with nothing else touching the clone: **PASS**, exit 0, "repository unchanged (tree, ignored files, directories, HEAD and git metadata)".

| Step | Result |
| :- | :- |
| 01 checkout, 04 Python set-up, 05 install | SUCCESS (excluded, substituted, as the tool states) |
| 02 classification; 03 AGENTS.md citation check; 06 pytest readiness; 07 closed environment | SUCCESS |
| 08 affected behavioral tests in isolation | SUCCESS, 3,660 passed (490.9 s) |
| 09 product lane | SUCCESS, 77 passed |
| 10 CLI and compatibility lane | SUCCESS, 119 passed, 3 skipped, 2 xfailed |
| 11 database lane | SUCCESS, 269 passed |
| 12 rails lane | SUCCESS, 160 passed |
| 13 evidence lane | SUCCESS, 134 passed (722.6 s) |
| 14 QA lane | SUCCESS, 488 passed |
| 15 release attestation, built and verified | SUCCESS (113.5 s) |
| 16 applicability and clean tree | SUCCESS, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |

The clone's `git status --short --untracked-files=all` was empty afterwards.

This is a local replay, not hosted CI; exact-head hosted CI is PR-35's to verify.

## 13. Acceptance and evidence obligations

* **AC-01** (no R-01 concern left under `engine/charts/`), **AC-03** (inventory, dispositions, module removed, guard), **AC-04** (migration-level checks and the reconciliation), **AC-05** (preserved outputs and failures, no fallback, a clean tree).
* **Exact-head hosted CI `test` green** on the PR head, all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. No CI waiver exists for HDE-EPIC041. A red result caused outside this change is handled under Plan v1.1 RK-06 and the CI-red rules; it is not green.
* **Acceptance of the unit** is PR-40's lineage review after Nathan's merge.

### 13.1 AC-04 record (PR description "Checks run" and the result record)

* Commands and configuration: §11, closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev` through `env -i`.
* The tested-source SHA, distinct from any later record commit and from review-time HEAD.
* Results with counts, the actor (the PR-30 session), the UTC time window, and the limitations: local runs are not CI, QA or governed evidence.

### 13.2 Governed evidence

None planned (Plan v1.1 §10). No changed path is listed in the Human Evidence Index or the Machine Mirror, and none is a release member (§4). `artifacts/logs/loader_call.jsonl` and `artifacts/compat/*` are not changed. Review v1.0 N-4 stays with QA-10.

### 13.3 Reconciliation of R-01 to R-03 (the PR record)

* **Search.** Scope: all tracked files except `docs/pfcanon/` and `docs/ephemeral/`. Pattern: `engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy`. Command: `git grep -I -l -E '<pattern>' <head> -- . ':!docs/pfcanon/' ':!docs/ephemeral/'`.
* **Dispositions at the prototype head (66 files).** PR-30 re-runs it at its commit and records any difference.

  | Members | Disposition |
  | :- | :- |
  | `adapter/chart_orchestration.py` | The Adapter-owned entry: every R-01 concern for chart loading (`SAFE_MODE` read, both clocks, correlation id, pinned-list reads, fixture acquisition, keys-only log line) is here (AC-01, I-2) |
  | `engine/charts/pure.py` (not matched by the pattern; `git ls-tree` of `engine/charts/`) | The only module under `engine/charts/`; pure (WU-PR-01's tests) |
  | `scripts/make_compat_determinism_artifacts.py` | C-1, migrated (PD-2) |
  | `tests/loader/test_load_chart_fixture_only.py`, `tests/loader/test_loader_logs_keys_only.py` | C-2, C-3, migrated in place (PD-1, PD-3, PD-4) |
  | `tests/adapter/test_chart_orchestration.py`, `tests/charts/test_chart_pure_interface.py`, `tests/charts/test_chart_pure_purity.py` | WU-PR-01's tests of the new interfaces; unchanged |
  | `tests/charts/test_chart_loader_import_guard.py` | The guard (this unit) |
  | `ci/checks/classify_ci_changes.py` | Owner mappings, including the removed path's (PD-8) |
  | `tests/retired_tests.md` | Row 57 (H-4, history) and the new row (PD-10) |
  | `adapter/http_reader.py` | H-2 name collision: `_safe_load_chart` reads a fixture file and imports no loader |
  | `artifacts/logs/loader_call.jsonl` | The tracked historical log (I-6); unchanged; no supported run can now append to it |
  | `artifacts/epic004/guards/forbidden_serializers.txt`, `artifacts/math/_manifest_files.txt`, `artifacts/qa/a7_presence.rg.txt`, `artifacts/qa/evidence_presence.rg.txt`, `audit/inventory_epic007.json`, `codex/out/008.evidence_inventory.json`, `manifest_pre.sha256`, `manifest_post.sha256`, `notes/dev-sampler/grep_reader_start_gunicorn.txt`, `notes/dev-sampler/grep_reader_start_http_reader.txt` | H-3: historical captures and inventories naming the loader as text; unchanged |
  | 44 files under `.audit_src/`, `_archive/`, `_arch/`, `handoff/` and `artifacts/architecture/` | H-1 and H-3 historical captures; unchanged (I-6, ED-09) |
  | `engine/charts/loader.py`, `tests/adapter/test_chart_orchestration_characterization.py` | Removed (D-1, ED-06; PD-10) |

* **Compatibility surface:** none retained, so TI-06 is moot (Audit §8.1).

## 14. Security, privacy, migration, rollout, rollback

* **Security:** no route, credential, flag, network or environment gate. Removing the loader removes a provider-resolution path that wrote `artifacts/provider/decision.txt` relative to the CWD (O-05). The guard and the generator test run `git` and the script as subprocesses with fixed arguments; neither reads a secret. The Codex code review is in the chain; neither the instruction nor the repository instructions require a separate security review for this change.
* **Privacy:** C-3 keeps the keys-only assertion; the log line carries no birth input.
* **Migration:** in-repository callers only; no data migration.
* **Rollout:** no release cut, no manifest or admission change.
* **Rollback:** revert the PR.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| RK-01 CI classification | The three owner mappings in the same commit; §11 item 4; the fail-closed probes (§12.2) |
| RK-02 removal before migration | One commit (§9); N3 reproduced the failure mode |
| A guard that cannot fail (RK-04's concern) | 18 planted forms, an unparseable text form, N1 on the base and N2 at the head; non-vacuity assertion on the three live callers |
| A guard that flags a real non-import (the purity test, the classifier key) | PD-6; covered by `test_checker_ignores_text_that_is_not_an_import`, whose inputs are those real forms |
| `main` moves before PR-30 | §9 step 2 |
| RK-06 an unrelated red CI result | PR-35's CI-red rules; the unit is not widened |
| A review finding on a constructed input | PR-35 answers it with the traced path and the stated limit (§6, last column); a P1 on a real input is fixed |
| Scope creep into the generator's compat repair or `input_validators` (RK-05) | I-3; FND-005 and FND-006 stay with their owners; rescope to the IA through RS-20 |
| Interruption | Resume in this session from the last saved artifact; prototypes only in throwaway clones |

## 16. Observations for owners (outside this unit's bound; nothing changed here)

* **OBS-6.** `scripts/scratch.py` is a tracked `.py` file that holds Markdown notes (since `b2e011f5`). It is not Python, so any repository-wide AST tool must handle it (this plan does, PD-7). Owner: the Product Owner, as repository hygiene; no change here.
* **OBS-7.** The instruction §3.3 named `CI_REGISTERED_OWNER_TEST_DELETED` for deleting the characterization file while it is still registered. With the classifier changed in the same push, the classifier reports `CI_FULL_VALIDATION_TEST_INVALID` first (§12.2). Both fail closed; the plan's PD-8 avoids both. Owner: the IA, as a note for PR-40.
* **OBS-8 (environment).** In this container `ruby` is installed at `/usr/local/bin` (a link to `/opt/ruby-3.3.6`). An `env -i` `PATH` without `/usr/local/bin` fails eleven of the 170 targets (nine in `tests/evidence/test_hdapi_v2_contract_inventory.py`, two in `tests/tools/test_prepush_check.py`) with `FileNotFoundError: 'ruby'`, identically on the base and the head (§12.4). This session also installed the distribution `ruby` package at `/usr/bin/ruby` before finding the cause; it was not needed. Owner: later sessions' surface advice.

## 17. Carried items (instruction §11)

| Item | Owner |
| :- | :- |
| OBS-4 (clock-dependent C-3) | Resolved by PD-4 in this unit |
| AUD-CORR-1, OBS-1 | Applied as I-1; no `input_validators` change (FND-006) |
| HDE Build Notes addendum 2.2 bearing | Applied as I-7 (PD-5, PD-10, PD-12) |
| OBS-2, OBS-5 (environment) | §11 |
| OBS-6, OBS-7, OBS-8 | §16 |
| TI-07 / CCR-1 | Product Owner; CL-05 at close |
| TI-02, Candidate CRD Items List items 9 and 10 | Product Owner |
| FND-005 to FND-007 | CL-40 scan and the Product Owner |
| Review v1.0 N-4 | QA-10 |
| DELTA-001, DELTA-002 | WU-PR-03 |
| Not produced | Proceed, code on a PR branch, PR, CI results, PR-35 and PR-40 records |
| Usage persistence | Pending (§21) |

## 18. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Status and reviewer | Treatment in WU-PR-02 |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work; Plan Templates Preflight B; HDE Governance §2.0.19; HDE Schemas and Artifacts) | APPROVED, Thoth, CF-E-30 review v1.1, 2026-10-28 (Ruling R-A); confirmed by Isis IA-30 v1.1 | None; a close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists; HDE Governance §9.7.7; Plan Templates §2) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 | CANON_RECONCILIATION (HDE Build Notes S19 decisions on vendor route selection and the production vendor override) | APPROVED as conditional, Thoth, review v1.1; not triggered (Audit §7; IA-30 v1.1 §4.4; WU-PR-01 lineage review §9) | **Re-checked at d09de6ea: not triggered.** The S19 addendum governs resolver-selected vendor acquisition (`bg:resolve --source vendor`, showcompat and conjunction through `engine/bodygraph/resolver.py`), the compat route, evidence-tool output roots and gate rows. This unit removes an import of `engine/config/provider_loader.resolve_provider`, which none of those decisions names, and adds no acquisition, route, evidence tool or gate row (I-3) |
| CCR-4 | CANON_RECONCILIATION (PF09.3 Task notes vs HDE Build Notes on the loader defect record) | APPROVED, Thoth, review v1.1 | None |

No new entry. HDE Build Notes addenda 2.2 and 2.3 are current canon and conflict with neither approved base; 2.2 applies as I-7. OBS-6 and OBS-7 are repository facts, not canon conflicts.

## 19. PR-30 and PR-35 obligations

* **PR-30** (this session, after the Proceed for exactly v1.0):
  * recover existing work first;
  * implement only §6 from the companion diff;
  * run §11;
  * decide any obvious in-scope correction under the PR-30 rule and record it under *In-flight decisions*;
  * take a material boundary (as PR-30 defines it) to one `RESCOPE_REQUEST` for the IA through RS-20 with `PR_RETURN_PHASE`;
  * commit once; publish one PR; record the replay; write the result record;
  * return `PR_CANDIDATE_PUBLISHED` with one handoff to PR-35 in its own session.

  It does not resolve reviews, wait for CI readiness or merge.
* **PR-35** (its own dedicated session):
  * subscribe to the PR; retrieve every Codex review finding and thread;
  * fix each that shows a wrong result, a crash or a guarantee breach on a real input, and answer every other with the traced path and the stated limit; a P1 on a real input is fixed; declining a P1 or a security finding goes to the Product Owner first; after two consecutive rounds of the same class, one design question to the Product Owner;
  * re-run §11 items 1 to 6 locally before each coherent corrective push; no `[skip ci]`; known findings before stale CI;
  * if a hosted failure appears, confirm whether it reproduces on the base before treating it as this PR's, and follow the CI-red rules;
  * verify current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability;
  * return `MERGE_PENDING — Ready to merge` without merging, with the conditional PR-40 block.
* **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 movement, drainage or closure; no canon edit; no release cut.

## 20. TypeSafe reading and surface advice for the receiving session (PR-30, WU-PR-02, plan v1.0)

* **Method.** Installed TypeSafe scoring skill, request v8.2, `score_v8.py` run once before this plan was saved; session kind `implementation`; label "HDE-EPIC041 PR-30 WU-PR-02 implementation". The Notion row was not written (PR-20 handoff rule).
* **Action sent (v8.2).** "Implement, in a dedicated session, the second of three PR work units of an approved Epic from a detailed PR plan that the Product Owner has proceeded: apply an already prototyped, locally validated change that deletes one legacy Python module of about 170 lines and one 70-line characterization test, changes one import line in an existing script, migrates two small existing tests to an already merged interface, adds a repository-wide import guard test of about 140 lines and a 23-line script behavior test, adds one retired-test row and edits a 13-line owner-test registration in an existing 2,100-line CI change classifier; a task list and a prototype diff exist; run the new and migrated tests, the classifier-selected suite of about 170 test files and a full local CI replay, then commit once and open the pull request, which runs all seven CI lanes; no live run against a provider occurs; an automated code review, a separate merge-readiness session and a lineage review follow."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.08 (confidence 0.65); rung probabilities low 0.00, medium 0.22, high 0.50, extra high 0.26, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.98, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.216, Opus 5.5 at high 0.490, Opus 5.5 at extra high 0.255, Opus 5.5 at max 0.020, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.004, Sonnet 5.5 at high 0.010, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T18:44:05Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.64 s; 5551 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for PR-30 and none for this PR-20 session (whose reading is the instruction's §14), so none is recorded.
* **Surface advice (PR-30).** PR-30 continues in this same top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, after this plan's documents PR merges, with GitHub access for one PR. It needs CPython 3.12 with CI's install (package-index access), `git`, `bash`, `ruby` and `curl`, a non-shallow clone, and `env -i` closed rails because the container exports vendor, database and GitHub credentials. Observed times in this session: the focused set under 10 seconds; the 170-target set about 8.5 minutes; the full replay about 24 minutes, the evidence lane taking 12 of them. Keep the negative proofs (§11 item 3) in a throwaway copy, and make no tool call that touches the checkout during the replay. No open rails, vendor, Railway, database or Notion writes.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage_id | HDE-EPIC041-PR20-WU-PR-02-20261028 |
| change | HDE-EPIC041 (EPIC) |
| specification | `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` (v1.1) |
| work unit | WU-PR-02 (R-01 residual, R-03, R-04 reconciliation part; AC-01, AC-03, AC-04, AC-05) |
| ecosystem release | GCFPE-20261027.1 / 102726.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 102726.1, https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9, page state 2026-10-27T13:18:23.839Z |
| role/stage | dedicated WU-PR-02 PR engineering session / GCF-14 |
| capture time | 2026-10-28 |
| runtime identity | https://claude.ai/code/session_01Q789u2FkMeZpy3U2W5XTh9 |
| inherited usage | `HDE-EPIC041-PR10-WU-PR-02-20261028` (instruction front matter) |
| repository persistence | PENDING: `docs/changes/` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`; no installed `GCFPE_PROMPT_PROVENANCE.md`. Owner: GCFPE management. Non-gating |

## Canon relied on

Resolved from `docs/pfcanon/` on `main` d09de6ea; this branch changes nothing there. Terms searched: HDE-SEPA006, chart loader, `engine/charts`, `charts/loader`, `resolve_provider`, `provider_loader`, purity, per-PR plan, business case, PR review finding disposition, CI lane classification, Canon precedence.

| Title | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Checklist — Separation | Task HDE-SEPA006; Subtasks .1 to .3 | Scope; .2 migration (the generator and loader/provider tests included; no import-path rename as migration; historical captures unchanged); .3 reconciliation and evidence fields |
| HDE Architecture | §1.1 "Single homes" (Purity rule; BodyGraph seam carve-out; Non-BodyGraph chart loader classification) | What leaves `engine/`; §8 Doc-Delta row |
| HDE Mechanics Guide | §1.1 "Audit classification for I/O-bearing engine seams", "BodyGraph and loader seam posture" and the remediation paragraph | Migrate generator callers; preserve outputs; no fallback, no Engine I/O exception, no second resolver |
| HDE Governance | §9.7.7 "Plan approval gate" (hold label `ASK OK? — PR IMPLEMENTATION PLAN`; Proceed is the approval; per-PR plan follows the exact instruction; no proof by intent; negative proof); the business case and stop rule as the instruction quotes them | §1, §3, §12.3 |
| Change Process Guide | "PR review finding disposition (every pull request; real inputs only)" | §6 last column; §19 |
| Plan Templates | "Review guardrails"; "CI lane classification and automated budget-control discipline"; "Canon precedence for template use" | §19; one coherent push; the precedence quote; HDE Build Notes cited by title in prose |
| HDE Build Notes | Front matter and precedence rules 1 to 9; addendum index; addendum 2.1's decision table, D-2, scope and dependencies; addenda 2.2 and 2.3 in full | I-7 (R-1, R-2); the carried items of 2.3; CCR-3 re-check against 2.1 |

## Approval

* **Approval hold:** `ASK OK? — PR IMPLEMENTATION PLAN`
* **Approval state:** Pending.
* **Approval authority:** Nathan / Product Owner, by invoking `PR Implementation Proceed` (PR-30) for exactly this v1.0.
* **Approved scope or rejection basis:** not yet decided.

## Nonclaims

This plan is not implementation, a Proceed, a PR, CI, QA, Ops, acceptance, a PF09 or board movement, a canon change, a PF10 addendum or closure. The prototype results are local scratch observations, not CI, not QA and not governed evidence. Nothing outside `docs/ephemeral/` is changed by this plan's PR. Merging it preserves the record and approves nothing (D21-C).
