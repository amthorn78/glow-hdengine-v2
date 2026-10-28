---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC041-WU-PR-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
approval_hold: "ASK OK? — PR IMPLEMENTATION PLAN"
predecessor: none (first plan for WU-PR-01)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
work_unit_title: "WU-PR-01 — Adapter orchestration entry and pure Engine chart interface (HDE-SEPA006.1; interface part of .3)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; 27,072 bytes; git blob 455874034a8a627b1b2706c8193bb4c35dc010f7; merged by amthorn78/glow-hdengine-v2#789 as 7100d6f9)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; 37,557 bytes; git blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE, ASK OK.; git blob 2ca19d33c1098fde7f606e2a09ee9e884f1ba7f3; merged by #788 as 23324960)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; git blob 9decb6085a64a9d0c2b7b8919e97ef3627a2846a)
REMEDIATION_REVIEW_ID: none (no remediation lineage)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
immutable_approved_base: Specification v1.1 (Thoth, CF-E-30 review v1.1) → Implementation Plan v1.1 (Isis, IA-30 review v1.1)
effective_baseline: "approved base + applicable PF10 overlays (NONE)"
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md (git blob cb61644d4380fa5aa32ba0332fd532b5c29279a7; 37,581 bytes; sha256 cf23eda0b8cd6dcca1c33ffccdc1fc2de2a1ded28c149f62de947a5f492dd3a3; the only PF10 file on main at 7100d6f9; unchanged since the Audit)
pf10_addenda_applicable: NONE
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0-prototype.diff (see §12)
repository_baseline: origin/main 7100d6f95f8d663399afc6605ae75656713aa6b3 (#789). `git diff --stat b29ca84 7100d6f9 -- . ':!docs/ephemeral/'` is empty, so every byte outside docs/ephemeral/ equals the Audit's head
working_branch: claude/wu-pr-01-implementation-plan-js521f (this plan's documents only)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01Q789tyc3umMjXiHB1aoXAR (the dedicated WU-PR-01 PR engineering session Nathan created; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9; page state 2026-10-27T13:18:23.839Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1 (GCFPE Membership and Release Register, "Current selection", read 2026-10-28)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; CCR-3 re-checked at 7100d6f9, not triggered; no new entry (§18)
created_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES: see §21
---

# HDE-EPIC041 WU-PR-01 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED for v1.0.** This is the complete plan for WU-PR-01 within the instruction's scope: one pure Engine chart module, one Adapter-owned orchestration entry, their tests and two owner-test mappings. No existing caller and no existing module changes. The plan fixes the names and paths the instruction leaves to PR-20 (§5) and records a prototype that ran in throwaway clones (§12):

* the 46 new tests pass, and the purity checker and harness each fail their planted violation;
* the classifier, as `ci.yml` calls it, selects all seven lanes and 170 changed-test targets, including the four new files;
* every changed path is a non-member; admission reports `1.3.0`, 45 members and `release_id` 77204764…, unchanged;
* of the 170 targets, 4,427 tests pass and 150 fail; **the same 150 fail on the unchanged base**, all in `tests/qa/test_generate_epic_close_pack.py` (§16 OBS-3);
* lanes 09 to 15 of `ci.yml`, run directly, pass (§12.5);
* every run left the tree clean.

**One known blocker outside this unit (OBS-3).** `main` is red for `tests/qa/test_generate_epic_close_pack.py`: it reads `docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.1.md` (replaced by v0.9.2 in `2d99bffc`) and `docs/ephemeral/` records archived by `de27c356`. Those were documentation-only pushes, which select no CI lane, so their own runs did not run that file. This unit must change the classifier (the owner mappings), which selects full validation, so its hosted `test` job will be red on that file until `main` carries a fix. The Plan's acceptance requires green exact-head CI (RK-06; no waiver). The fix is not in this unit's bounded files; it goes to the Product Owner (TI-02 owner) now, and PR-35 ports it when it exists (§19).

PR-30 applies the companion diff, re-runs §11 and publishes one PR.

This plan authorizes nothing. Only the Product Owner's `PR Implementation Proceed` (PR-30) for exactly v1.0 authorizes implementation, and only the Product Owner merges.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Lineage and sources read in this session

* **Instruction v1.0**, read in full at 7100d6f9 (blob 455874034a8a…, the blob #789 landed).
* **Implementation Plan v1.1** and its **IA-30 review v1.1**, read in full. The review's N-5 nit has no effect here.
* **Implementation Audit v1.0**, read in full (facts O-01 to O-20, X-1 to X-6; ED-01 to ED-10; §5 inventory).
* **Specification v1.1**, read in full (R-01 to R-04, AC-01 to AC-05, §4 items 3 and 4).
* **Prompts (Notion):** PR-20 102726.1 in full; PR-30 102726.1 in full (receiver contract; page state 2026-10-27T13:15:20.197Z); the HDE IA hub; the register's "Current selection" section only (its historical sections were not needed and were not read).
* **Skill:** `glow-hde-pr-development` SKILL.md 1.5.0, read as the PR-30 and PR-35 contract (it is not used for planning).
* **Precedent:** `docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0.md` at 977a9c7f (#686), for structure and the companion-diff convention.
* **Code read at 7100d6f9:** `engine/charts/loader.py` (173 lines, blob 8ea4dce2…, unchanged); `engine/util/input_validators.py`; `adapter/no_io_guard.py`; `adapter/__init__.py`; `adapter/logging_filter.py` (the keys-only sink idiom); `tests/core/test_engine_core_purity.py`; all five `tests/loader/*.py`; `tests/conftest.py`; `pytest.ini`; `pyproject.toml`; `ci/checks/classify_ci_changes.py` (sets, `_product_owner_targets`, `changed_test_targets`, `_lanes_for_path`, `_full_validation_test_targets`); the `test` job of `.github/workflows/ci.yml` (classify, changed-tests isolation, lanes); `tests/evidence/test_rails_ci_workflow_integration.py` (the roster invariants); `tools/cli/serializer_grep_guard.py` (its scope); `scripts/make_compat_determinism_artifacts.py`; `artifacts/constants/iso_3166_1_alpha2.json` and `iana_tz_list.json`; `engine/serializer/canon.py`; `README.md` "Pre-push check (HDE-CRD-0002)"; `.github/pull_request_template.md`.

## 3. Business case (as the PR Instruction states it; the Proceed is given against it)

* **Beneficiary:** the delivery team.
* **Evidence:** Audit O-08 (committed runs appended to the tracked `artifacts/logs/loader_call.jsonl` three times: `39a5a33a`; `f3e1f9a1` "HDE-EPIC030 QA PASS 1"; `c6fdc913` "HDE-EPIC030 QA PASS 2"); O-06 / X-3 (chart validation misreports a valid place as invalid outside the repository root); E-4 / O-02 locate the concerns.
* **Benefit:** chart validation exists as deterministic data-in/data-out code that tests can run from any CWD without touching the repository, and logging and file reads have one Adapter owner that writes no file by default. This unit adds the interfaces and changes no caller, so on its own it does not stop a run of today's loader from writing the tracked file. That benefit is realized when WU-PR-02 migrates the callers and removes the loader.
* **Measure:** the AC-02 purity and import-side-effect tests pass, and their negative self-test fails a planted violation; the orchestration tests pass with an injected sink, from a temporary CWD, with zero socket attempts; `git status --porcelain` is empty after the run.
* **Stop rule** (HDE Governance §9.7.7): a work unit whose business case is met stops; further work on it needs a new business case.

## 4. Baseline re-check (instruction §4: "the per-PR plan re-verifies them at its own base")

| Fact | At 7100d6f9 |
| :- | :- |
| Code since the Audit's head b29ca84 | `git diff --stat b29ca84 7100d6f9 -- . ':!docs/ephemeral/'` empty |
| `engine/charts/loader.py` | blob 8ea4dce2602d…, 173 lines, unchanged (O-01) |
| `artifacts/logs/loader_call.jsonl` | sha256 24b6c8423e98…cf236, as the Audit recorded |
| Audit §5.2 pattern outside `docs/pfcanon/`, `docs/ephemeral/` and the historical captures | `adapter/http_reader.py` (H-2 name collision), `engine/charts/loader.py`, `manifest_pre.sha256` and `manifest_post.sha256` (H-3), C-1 `scripts/make_compat_determinism_artifacts.py`, C-2 and C-3 `tests/loader/…`, `tests/retired_tests.md` (H-4). Same set as Audit §5 |
| `engine/charts/` | holds only `loader.py`; no `__init__.py` (namespace package) |
| Planned paths | none of `adapter/chart_orchestration.py`, `engine/charts/pure.py`, `tests/charts/` exists |
| Owner mapping | `prepush_check.py --path adapter/chart_orchestration.py … lanes` fails with `CI_PRODUCT_OWNER_TEST_MISSING:adapter/chart_orchestration.py` (O-13 confirmed) |
| Release membership | admitted release `1.3.0`, 45 members, `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; every planned path "not-member" |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md`, the only PF10 file; `prepush_check.py build-notes` PASS with the sha256 in the front matter |
| CCR-3 | not triggered: the planned code imports no resolver, provider or vendor module (§18) |

## 5. Design decisions (the names, paths and choices the instruction leaves to PR-20)

| ID | Decision | Basis |
| :- | :- | :- |
| PD-1 | **Pure module:** `engine/charts/pure.py`. **Orchestration entry:** `adapter/chart_orchestration.py`, function `load_chart`. | Plan v1.1 §5.1 names "Engine pure chart interface" under `engine/charts/` and a non-HTTP `adapter/` module (ED-01). Neither name collides with the WU-PR-02 guard, which targets `engine.charts.loader` |
| PD-2 | **No `engine/charts/__init__.py`.** The new module joins the existing namespace package, as `loader.py` is imported today. | Adding one would be a new product path that needs its own owner mapping and changes the package type for no benefit |
| PD-3 | **Tests:** `tests/charts/test_chart_pure_purity.py` (AST deny-list, fresh-interpreter test, two negative self-tests); `tests/charts/test_chart_pure_interface.py` (direct calls: values, the five typed errors, order, `normalize_chart` on the fixture); `tests/adapter/test_chart_orchestration.py` (every orchestration test of instruction §5); `tests/adapter/test_chart_orchestration_characterization.py` (its own file, deleted by WU-PR-02). Basenames are unique in the repository, which matters because no test directory has an `__init__.py`. | Instruction §5 |
| PD-4 | **CI registration:** two entries in `_PRODUCT_TEST_OWNER_PATHS` of `ci/checks/classify_ci_changes.py` (`engine/charts/pure.py` → the four test files; `adapter/chart_orchestration.py` → the orchestration and characterization files). **`pytest.ini` is not changed and `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` is not changed.** | The fail-closed rules need only the owner mapping: an unmapped product path fails with `CI_PRODUCT_OWNER_TEST_MISSING`. Registered owners join the full-validation targets automatically (`_full_validation_test_targets`). `tests/evidence/test_rails_ci_workflow_integration.py` requires the `testpaths` collection to equal fixed ∪ supplemental ∪ inactive, so adding to `testpaths` would also force a roster entry. `tests/core/test_engine_core_purity.py` is registered the same way (owner only, not in `testpaths`). WU-PR-02 therefore removes the characterization file from the two owner entries only |
| PD-5 | **Date check is local integer arithmetic, not `parse_date_yyyy_mm_dd`.** The pure module reuses only `parse_time_hh_mm`. | Probe (§12.3): `datetime.strptime`, which `parse_date_yyyy_mm_dd` calls, imports `_strptime` on its first call in a process, and that import calls `time.strftime` and `time.tzset()` (a read of the `TZ` environment). Under the fresh-interpreter test's patches the first validation call trips them. I-1 permits ("may"), it does not require, reusing the date helper. The local check accepts exactly what `strptime(s, "%Y-%m-%d")` accepts behind the `\d{4}-\d{2}-\d{2}` shape: equal on all 203,200 shaped strings probed (years 0 to 39, 1890 to 2100, 2400, 2500, 9999; months 00 to 19; days 00 to 39), and the characterization test pins it against today's loader |
| PD-6 | **Pinned lists:** read on every call, as today, from `Path(__file__).resolve().parents[1] / "artifacts/constants/…"`; the same non-empty-list check as today's `_load_list`; passed to the pure module as `frozenset`s. | ED-03; instruction §3.1. No cache, so no stale state |
| PD-7 | **Log sink:** the line is the JSON text today's `_log_call` writes, without the newline (same key order, `separators=(",", ":")`, `ensure_ascii=False`). With `log_sink` given it is called with that string; otherwise `logging.getLogger("adapter.chart_orchestration").info(line)`. Any exception from either is swallowed. | Instruction §3.3; ED-04; the `adapter/logging_filter.py` sink-then-logger idiom |
| PD-8 | **Routing order is today's branch order:** (1) the positional predicate on `args`; (2) today's legacy predicate (first positional a string not shaped `YYYY-MM-DD`) → `TypeError`; (3) all three birth keywords → the positional predicate applied to them, else `TypeError`; (4) otherwise `TypeError`. | Reproduces today's routing for every shape, so the one changed outcome is the D-1 retirement. One log line per call (O-07 not reproduced) |
| PD-9 | **The orchestration normalizes the acquired fixture with `normalize_chart`.** | Gives `normalize_chart` its caller; the result equals the O-03 literal (asserted) |
| PD-10 | **The typed error is `engine.charts.pure.ChartInputError`** (`code`, `message`, `details`), raised by the pure module and propagated unchanged by the entry. `validate_birth_inputs` returns `BirthInputs(date=(y, m, d), time=(h, m), city, country, tz)`. | Instruction §3.3. The pure module cannot import `datetime` under the deny-list, so the date is a tuple |

## 6. Files and components, with each component's real inputs (PR-20 Execute step 3)

| Path | Change | Component | Real inputs | Outside the real set: the one refusal or stated limit |
| :- | :- | :- | :- | :- |
| `engine/charts/pure.py` | new, 92 lines | Pure interface: `ChartInputError`, `BirthInputs`, `validate_birth_inputs`, `normalize_chart` | Four birth values from the entry (C-1's literals `1990-05-04`/`14:22`/`Austin, US` and `1992-07-19`/`08:05`/`New York, US` with `Europe/Amsterdam`; C-2 and C-3's `1990-01-01`/`12:34`/`Amsterdam, NL`; the invalid literals of `tests/loader/test_validators_strict.py`); the two pinned lists (10 ISO codes, 5 IANA zones on `main`); the fixture chart dict | Any other value gets the typed error for its field (or, for a non-dict to `normalize_chart`, Python's own error). `normalize_chart`'s digit-string branch is kept verbatim from today but no real input reaches it: stated limit, not tested |
| `adapter/chart_orchestration.py` | new, 113 lines | Orchestration entry `load_chart(*args, **kwargs)` | Call arguments from this unit's tests and, after WU-PR-02, C-1 to C-3; `SAFE_MODE` from the CI runner (`1`) or the operator's shell; the CWD (repository root in CI and in C-1's runs, a temporary directory in tests); `log_sink` from tests; the two tracked pinned-list files | Any other argument shape → `TypeError("Invalid arguments to load_chart")`. A missing or malformed pinned-list file is a stated limit (both are tracked): the read error propagates, one `status:"error"` line is logged, no fallback. A non-callable `log_sink` loses the line (swallowed), as a raising sink does |
| `ci/checks/classify_ci_changes.py` | +13 lines in `_PRODUCT_TEST_OWNER_PATHS` | Owner mappings | The changed-path list CI passes | Unchanged behavior for every other path |
| `tests/charts/test_chart_pure_purity.py` | new, 137 lines | AC-02 checks | The module source; a fresh interpreter | — |
| `tests/charts/test_chart_pure_interface.py` | new, 56 lines | Direct interface checks | Real literals only (column 4) | — |
| `tests/adapter/test_chart_orchestration.py` | new, 160 lines | AC-01, AC-04, AC-05 interface-level checks | Real literals; `SAFE_MODE` 1, 0, unset; the retired legacy literals `"user-abc"` and `"CID-deadbeef"` (`.audit_src/tests/loader/…` on `main`) for the legacy-routed shapes and the invalid correlation id | — |
| `tests/adapter/test_chart_orchestration_characterization.py` | new, 70 lines | I-4 equality with today's loader | 13 shapes: every supported-path shape the callers use, valid and invalid, plus the two non-legacy `TypeError` shapes | Legacy-routed shapes are not called on today's loader: it would run `resolve_provider`, which writes `artifacts/provider/decision.txt` (O-05). They are covered by the orchestration `TypeError` test |

Not changed (instruction §4): `engine/charts/loader.py` and every caller; `engine/util/input_validators.py`; `engine/config/provider_loader.py`; `engine/providers/*`; `engine/provider/*`; `catalog/manifest.json`; `engine/config/registry_loader.py`; `pytest.ini`; any governed evidence; `docs/pfcanon/`; `tests/retired_tests.md`; `artifacts/logs/loader_call.jsonl`; the historical captures.

## 7. Interface contracts (as implemented; instruction §3.3)

**`adapter.chart_orchestration.load_chart(*args, **kwargs) -> dict`**

* Accepted forms: positional `(birthdate, birthtime, place, …)` where the first three are strings, the first matches `^\d{4}-\d{2}-\d{2}$` and the second `^\d{2}:\d{2}$` (extra positionals ignored); keyword `birthdate=`, `birthtime=`, `place=`, routed through the same predicate. `tz`, `correlation_id`, `log_sink` are keyword-only reads.
* Every other shape: `TypeError("Invalid arguments to load_chart")`, including both legacy-routed shapes (D-1).
* Validation: `engine.charts.pure.validate_birth_inputs` with the pinned lists; errors propagate as `ChartInputError`.
* Success: a fresh dict equal to `{"gates":[1,2,3],"channels_short":[],"centers":[],"type":"","authority":"","profile":"","meta":{"provider":"fixtures","source":"default"}}`; `sercanon` bytes `{"authority":"","centers":[],"channels_short":[],"gates":[1,2,3],"meta":{"provider":"fixtures","source":"default"},"profile":"","type":""}` plus LF.
* Log: exactly one line per call, success or error, keys in order `ts, route, provider, source, status, duration_ms, safe_mode, correlation_id`; `route="loader.load_chart"`, `provider="fixtures"`, `source="default"`, `status` `ok`/`error`, `duration_ms` int, `safe_mode` = `str(os.getenv("SAFE_MODE", "0")).strip() == "1"`, `correlation_id` = `ensure_cid(kwargs.get("correlation_id"))`. No birth input in the line.

**`engine.charts.pure`**

| Check, in order | `details.field` | `message` |
| :- | :- | :- |
| date (`\d{4}-\d{2}-\d{2}` full match, year ≥ 1, month 1 to 12, day within the Gregorian month) | `date` | `invalid date` |
| time (`parse_time_hh_mm`) | `time` | `invalid time` |
| place (string; NFC; strip; exactly two non-empty comma parts; upper-cased country in `iso_codes`) | `place` | `invalid place` |
| tz is `None` | `tz` | `tz required on internal path` |
| tz not a non-blank string in `iana_zones` | `tz` | `invalid tz` |

`code` is always `READER_INVALID_INPUT`. `normalize_chart(obj)` returns a shallow copy with `gates` rebuilt: integers kept, digit strings converted, the rest dropped (today's `_normalize_chart`, verbatim).

## 8. Requirement-to-change/test map (PR-20 Execute step 4)

| Obligation (source) | Change | Test or evidence |
| :- | :- | :- |
| R-01 / AC-01: one Adapter-owned entry owns rails read, clocks, correlation id, file reads, acquisition, logging (instruction §3.1, I-2) | `adapter/chart_orchestration.py` | orchestration tests: SAFE_MODE, correlation id, keys-only line, one line per call, default logger with no file, temporary-CWD equality, `NoIoGuard` 0 |
| R-02 / AC-02, I-1 | `engine/charts/pure.py` (PD-5) | AST deny-list (own imports and calls; only `parse_time_hh_mm` from `input_validators`); fresh-interpreter test with 31 patched entry points at import and during validation and normalization; two negative self-tests |
| R-04 / AC-04 interface part | the four test files | AC-04 record in the PR (§13) |
| AC-05 / I-4: fixture byte-identical; errors identical on supported shapes; legacy shapes `TypeError` | entry + pure module | literal-value tests (orchestration and interface files); characterization file (13 shapes, results, errors and log fields); `TypeError` test (4 shapes, including both legacy-routed ones and no arguments) |
| AC-05 / I-5: clean tree | — | `git status --porcelain --untracked-files=all` empty after the covering tests (§11 item 3); CI's changed-tests step enforces it too |
| I-3: no acquisition, contract, fallback, route, flag, CLI option, release member | — | prepush `membership` (all not-member); code review: the two modules import no resolver, provider, HTTP or CLI module |
| I-6: historical captures, `loader_call.jsonl`, `retired_tests.md` row 57 unchanged | — | the diff touches none of them (§12.1) |
| Instruction §7 CI classification | classifier owner mappings (PD-4) | classifier run as `ci.yml` calls it (§12.1) |
| Plan v1.1 §6 WU-PR-01 Scope: "Do not change `engine/charts/loader.py` or any caller" | — | diff path list (§12.1) |
| HDE Mechanics Guide §1.1: no fallback, no Engine I/O exception, no second resolver | — | the entry has no fallback branch; the pure module does no I/O; no resolver is imported |
| HDE Architecture §1.1 purity rule | PD-5 | as R-02 |
| Doc-Delta (Change Process Guide §0.2; HDE Governance §9.2) | none triggered | The unit is additive: no public contract, serializer, schema, transport, rails or existing logging guarantee changes, and HDE Architecture §1.1 and HDE Mechanics Guide §1.1 stay true while the loader exists. DELTA-001 and DELTA-002 drain after WU-PR-02, carried by WU-PR-03 |

## 9. Implementation sequence for PR-30

1. **Recover before creating.** Inspect this session's checkout, branches, worktrees, open PRs and `docs/ephemeral/` for WU-PR-01 work. Expected: this plan, its diff, and this plan's own merged documents PR.
2. **Branch** from current `origin/main` on the session's designated branch. If `main` moved past 7100d6f9 outside `docs/ephemeral/`, re-run §4 first and record any difference. A change to any file in §6 or to `tests/core/test_engine_core_purity.py`, `adapter/no_io_guard.py` or `engine/util/input_validators.py` is reconciled before applying.
3. **Apply** `docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0-prototype.diff` (`git apply --check`, then `git apply`). A hunk that fails (the classifier is the only file that can move) is applied by hand to the same effect and recorded.
4. **Local checks**, §11 items 1 to 5, under `env -i` closed rails.
5. **Commit once:** `feat(charts): pure Engine chart interface and Adapter-owned orchestration entry (HDE-EPIC041 WU-PR-01, HDE-SEPA006.1)`.
6. **Replay** `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit (§11 item 6).
7. **Publish** one PR. Description: the `.github/pull_request_template.md` headings with the AGENTS.md content rules. "Why" cites the instruction and HDE-SEPA006.1; "Checks run" carries the AC-04 record (§13); "Not in this PR" names WU-PR-02 (migration, loader removal, characterization deletion) and WU-PR-03; "What merging does" says the two modules and their tests become current on `main` with no caller and establishes no QA, acceptance or closure. State that the PR runs all seven lanes because it changes the classifier.
8. **Result record** `docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.0.md` (`PR_IMPLEMENTATION_RESULT`): `PR_CANDIDATE_PUBLISHED`, tested-source SHA, the AC-04 fields, an *In-flight decisions* section, the `PR_REMOTE_ACTION_LEDGER`, nonclaims. Hand off to PR-35 in its own session.

**Integration seams:** `adapter.chart_orchestration` → `engine.charts.pure.validate_birth_inputs` and `normalize_chart`; → `engine.util.input_validators.ensure_cid`; `engine.charts.pure` → `engine.util.input_validators.parse_time_hh_mm`; the classifier's `_PRODUCT_TEST_OWNER_PATHS` lookup in `_product_owner_targets` (no code change there). **Order inside the commit:** none needed; one commit.

## 10. PR split and merge dependencies

* **One PR**, one coherent additive change; reversible by revert.
* **Before it:** this plan's documents PR merged (it carries the companion diff PR-30 applies).
* **Before its merge:** PR-35's `MERGE_PENDING`; Nathan merges.
* **After it:** PR-40 lineage review; ACCEPT returns to the whole-change IA, which issues WU-PR-02's instruction (Plan v1.1 §6: WU-PR-02 depends on WU-PR-01 merged and accepted).
* **No release member changes** (§4), so no manifest refresh and no evidence regeneration.

## 11. Validation PR-30 runs (PR-35 re-runs items 1 to 5 after any correction)

Environment: CPython 3.12 with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`, editable install pointed at the checkout under test); `ruby`, `bash`, `curl`, git; `env -i` with `HOME`, `PATH`, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and `PYTHONPATH=<checkout>`. **The cloud container sets `DATABASE_URL`, `GEO_API_KEY`, `HDAPI_BASE_URL`, `HD_API_KEY` and GitHub tokens; without `env -i` they reach the tests and make unrelated suites fail** (observed in this session, §12.4). Record env probes as SET/UNSET only.

1. The four new test files: `python -m pytest -q -p no:cacheprovider tests/charts tests/adapter/test_chart_orchestration.py tests/adapter/test_chart_orchestration_characterization.py` → expected 46 passed (4 + 8 + 20 + 14).
2. Classifier as `ci.yml` calls it: `python3 ci/checks/classify_ci_changes.py --base <base SHA> --head <head SHA> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>` → exit 0, `reason=selected_lanes`, all seven lanes, 170 changed-test targets including the four new files.
3. The classifier-selected targets from item 2, run as CI's isolated changed-tests step runs them, then `git diff --exit-code` and an empty `git status --short --untracked-files=all` → expected, while OBS-3 holds: 4,427 passed and 150 failed, the 150 being exactly the base's failures in `tests/qa/test_generate_epic_close_pack.py` (compare the failure list with a run on the base); clean tree. Any other failure is this unit's to fix. Once `main` carries a fix for OBS-3: all pass.
4. `python tools/ci/prepush_check.py --base <base> --head HEAD --path <each of the 7 paths> lanes membership build-notes` → PASS; every path not-member; PF10 v13.9.
5. Admission unchanged: `load_active_mechanics_bundle()` succeeds with `1.3.0`, 45 members, `release_id` 77204764…; `python scripts/release_id_recompute.py --check-manifest-only` exit 0.
6. `python tools/ci/prepush_check.py --base <base> --head HEAD --full replay` on the commit, with nothing else touching the checkout while it runs → while OBS-3 holds: steps 01 to 07 SUCCESS, step 08 FAILURE on the base-red file only, steps 09 to 15 SKIPPED by the replay; then run lanes 09 to 15 directly as §12.5 did. Once `main` carries a fix: every step SUCCESS and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

## 12. Prototype record

Throwaway clones under this session's scratchpad, at 7100d6f9; the session checkout was not changed and every clone ended with an empty `git status --short`. Environment: CPython 3.12.3 venv with CI's install, the prototype clone installed editable; git 2.43.0. The prototype was committed only in its clone. The companion diff is `git diff 7100d6f9 <prototype head>`.

### 12.1 Change set and companion diff

* Prototype head `1cca0c552f680231fee3ceb94767aea04093ecec` (scratch clone only; never pushed).
* `git diff 7100d6f9 1cca0c55`: 7 files, +641, −0 — `adapter/chart_orchestration.py` (113 lines), `engine/charts/pure.py` (92), `ci/checks/classify_ci_changes.py` (+13), `tests/charts/test_chart_pure_purity.py` (137), `tests/charts/test_chart_pure_interface.py` (56), `tests/adapter/test_chart_orchestration.py` (160), `tests/adapter/test_chart_orchestration_characterization.py` (70). Nothing under `engine/charts/loader.py`, `scripts/`, `tests/loader/`, `engine/util/`, `engine/config/`, `engine/provider*/`, `catalog/`, `pytest.ini`, `.github/`, `docs/evidence/`, `artifacts/`, `audit/` or `docs/pfcanon/`.
* Companion diff: `docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0-prototype.diff`, 688 lines, 28,287 bytes, sha256 `4a2e61381e34bdf71a7dc9a108e326d049adac9bc685557a73ce1167e3070524`; `git apply --check` clean on 7100d6f9.

### 12.2 Classifier, lanes, membership, admission (on 1cca0c55)

| Run | Result |
| :- | :- |
| `classify_ci_changes.py --base 7100d6f9 --head 1cca0c55 --event-name pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=7;lanes=product,compat,db,rails,evidence,qa,release`; `changed_tests=true`; 170 targets (the base's 166 plus the four new files) |
| `prepush_check.py --base 7100d6f9 --head HEAD` with the 7 paths, `lanes membership build-notes` | PASS; 170 targets; not-member ×7; PF10 v13.9 cf23eda0…; "repository unchanged"; exit 0 |
| Admission | `load_active_mechanics_bundle()` ok; `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (= base) |
| `scripts/release_id_recompute.py --check-manifest-only` | exit 0 |
| `tools/cli/serializer_grep_guard.py` | PASS (its scope is `engine/cli` and `adapter/http_reader.py`) |

### 12.3 Design probes

* `datetime.strptime` under the purity patches: importing `engine.util.input_validators` is clean; the first `parse_date_yyyy_mm_dd` call trips `time.strftime`, and with that patch lifted, `time.tzset`. `_strptime`'s source calls exactly `time.strftime`, `time.struct_time` and `time.tzset`. Basis of PD-5.
* Local date check against `parse_date_yyyy_mm_dd`: 203,200 shaped strings, 0 differences.
* An earlier sketch used `re.compile` in the pure module; the AST deny-list flagged it (`compile` is a forbidden call name, as in `tests/core/test_engine_core_purity.py`). The final module calls `re.fullmatch` instead.

### 12.4 Tests (`env -i` closed rails; window 04:52:51Z to 05:01:08Z)

| Run | Result |
| :- | :- |
| The four new files | 46 passed (4 + 8 + 20 + 14), 0.4 s |
| The 170 targets on 1cca0c55 | 4,427 passed, 150 failed, 495.8 s; `git diff` clean, status empty |
| The 166 base targets on 7100d6f9 (same run shape) | 4,381 passed, 150 failed, 494.3 s; clean |
| Failure sets compared | identical: all 150 in `tests/qa/test_generate_epic_close_pack.py` (137 `PF30.1-…-v0.9.1.md` not found; 13 archived `docs/ephemeral/` records not found) — OBS-3 |
| Classifier-owned set: `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/tools/test_prepush_check.py`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_http_reader_ci_ownership.py`, `tests/qa/test_qa_tool_ownership.py` | 477 passed, 117.5 s (04:57:02Z to 04:59:00Z) |
| A first run without `env -i` | many unrelated failures from the container's credentials (OBS-2); discarded, not counted |

### 12.5 Local `ci.yml` replay and lanes

* `prepush_check.py --base 7100d6f9 --head HEAD --full replay` on 1cca0c55 (05:02:46Z to 05:10:52Z): steps 01 to 07 SUCCESS (01, 04, 05 substituted, as the tool states); step 08 FAILURE, 150 failed / 4,427 passed, every failure in the OBS-3 file; steps 09 to 15 SKIPPED by the replay; step 16 FAILURE (follows step 08). The tool's exit was 4 ("repository changed") because a test-collection command of this session wrote `__pycache__` into the clone during the replay; the clone was cleaned afterwards. This is session interference, not a candidate effect; §11 item 6 tells PR-30 to leave the checkout alone during a replay.
* Lanes 09 to 15, each `run:` block of `ci.yml` executed in the clone under `env -i` with its own `RUNNER_TEMP` (05:11:52Z to 05:24:09Z):

  | Lane | Result |
  | :- | :- |
  | product | rc 0; ordering check; 77 passed |
  | compat | rc 0; CLI help, serializer guard, emitter proof; 119 passed, 3 skipped, 2 xfailed |
  | db | rc 0; direct-DB contract; 269 passed |
  | rails | rc 0; rail job definitions; 159 passed |
  | evidence | rc 0; updater, orientation, step-logs, hash, paths, mirror and final-LF checks; 134 passed |
  | qa | rc 0; isolated worktree; 488 passed; clean |
  | release | rc 0; manifest recompute; 79 passed; attestation built and verified with `--require-clean`; clean |

* The clone's `git status --short --untracked-files=all` was empty at the end.
* This is a local replay, not hosted CI; exact-head hosted CI is PR-35's to verify.

## 13. Acceptance and evidence obligations

* **AC-01** (entry exists and owns the R-01 concerns for chart loading), **AC-02**, **AC-04** (interface-level checks), **AC-05** (output equality; clean tree).
* **Exact-head hosted CI `test` green** on the PR head. No CI waiver exists for HDE-EPIC041. A red result caused outside this change is handled under Plan v1.1 RK-06 and the CI-red rules; it is not green.
* **AC-04 record**, in the PR description's "Checks run" and in the result record: commands and configuration (closed rails as §11), tested-source SHA, results with counts, actor (the PR-30 session), UTC time window, limitations (local runs are not CI, QA or governed evidence). Tested-source identity stays distinct from any later commit and from review-time HEAD.
* **Governed evidence:** none planned (Plan v1.1 §10). No changed path is listed in the Human Evidence Index, and none is a release member. Review v1.0 N-4 (whether implementation evidence must be governed) stays with QA-10.
* **Acceptance of the unit** is PR-40's lineage review after Nathan's merge.

## 14. Security, privacy, migration, rollout, rollback

* **Security:** no route, credential, flag, network or environment gate. `NoIoGuard` attempts 0 is asserted. The only environment read is `SAFE_MODE`, for a log field. The Codex code review is in the chain; a security review applies only if the repository instructions require one for this change.
* **Privacy:** the log line carries no birth input (asserted against today's C-3 forbidden list plus the country and tz).
* **Migration:** none; nothing imports the new modules in this unit.
* **Rollout:** no release cut, no manifest or admission change.
* **Rollback:** revert the PR; the change is additive.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| A purity test that cannot fail (RK-04) | Two negative self-tests: the AST checker on ten planted sources; the fresh-interpreter harness on a planted module that reads the environment at import |
| Log contract drift (RK-03) | Keys, order and values asserted literally; the characterization test compares every field but `ts` and `duration_ms` with today's last line |
| Hidden I/O inside a reused helper | PD-5 removes the one found; the fresh-interpreter test patches `time.strftime` and `time.tzset` |
| CI classification (RK-01) | Owner mappings in the same commit; §11 item 2 |
| The seven-lane run exposes failures that are not this unit's (RK-06, TI-02) | Known: OBS-3. PR-35's base-red rule; the unit is not widened. The prototype's base run is the comparison (§12.4): any failure outside OBS-3's 150 is this unit's |
| Scope creep into acquisition or the generator (RK-05) | I-3; rescope to the IA through RS-20 |
| A review finding on a constructed input | PR-35 answers it with the traced path and the stated limit (§6 last column); a P1 on a real input is fixed |
| Interruption | Resume in this session from the last saved artifact; prototypes only in throwaway clones |

## 16. Observations for owners (outside this unit's bound; nothing changed here)

* **OBS-1.** `engine.util.input_validators.parse_date_yyyy_mm_dd` is not side-effect-free on its first call in a process: `datetime.strptime` imports `_strptime`, which calls `time.strftime` and `time.tzset()`. Audit §4 R-02 and Plan v1.1 I-1 describe it as pure. This plan avoids it (PD-5) and does not change the helper (excluded, FND-006 neighbourhood). Owner: the whole-change IA, through PR-40, as context for FND-006.
* **OBS-2.** This cloud container exports vendor, database and GitHub credentials into every shell; unguarded local runs fail unrelated suites (§12.4). Recorded for later sessions' surface advice.
* **OBS-3 (blocks this unit's green CI; not this unit's to fix).** `tests/qa/test_generate_epic_close_pack.py` fails 150 of its tests on `main` 7100d6f9, identically with and without this unit's change (§12.4):
  * 137 read `docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.1.md` (its `CRD_REGISTER_REL`, line 4370), which `2d99bffc` (2026-10-27, #762) replaced with v0.9.2;
  * 13 read `docs/ephemeral/` records (the HDE-EPIC040 and HDE-CRD-0002 Specifications, Plans, QA Plan, QA Report and one PR instruction) that `de27c356` (2026-10-28, "Archived /docs/ephemeral to Google Drive") deleted.
  * Both pushes were documentation-only, which selects no CI lane, so their own runs did not run the file. The earlier red `main` push run at 1fb4731b (TI-02) predates both; its cause was not re-verified here.
  * Effect here: the owner mappings make this PR a full-validation change, and full validation runs that file, so the hosted `test` job is red until `main` carries a fix. Plan v1.1 RK-06 says such a result is not green, and no waiver exists.
  * Fix: outside this unit's bounded files (instruction §4) and not within HDE-SEPA006. Options for its owner, not chosen here: point the register pin at the current PF30.1 file, and bind the archived records to bytes the test can read (tracked fixtures, or `git show` of a pinned commit: CI checks out with `fetch-depth: 0`). The test is the close-pack writer's owner test (HDE-CRD-0002 WU-PR-07 lineage).
  * Owner: Nathan / Product Owner (TI-02 covers the unresolved `main` CI failure). Not a blocker for the Proceed or for PR-30's publication; it is a blocker for PR-35's `MERGE_PENDING`.

## 17. Carried items (instruction §11)

| Item | Owner |
| :- | :- |
| TI-07 / CCR-1 | Product Owner (possible canon change); CL-05 at close |
| TI-02, Candidate CRD Items List items 9 and 10 | Product Owner |
| FND-005 to FND-007 | CL-40 scan and the Product Owner |
| Review v1.0 N-4 | QA-10 |
| Review v1.1 N-5 | none (nit in the approved Plan) |
| OBS-1, OBS-2 | the IA through PR-40 |
| OBS-3 (base-red close-pack writer test) | Nathan / Product Owner, now; PR-35 ports the fix once it exists |
| Usage persistence | pending (§21) |

## 18. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Status and reviewer | Treatment in WU-PR-01 |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work; Plan Templates Preflight B; HDE Governance §2.0.19; HDE Schemas and Artifacts) | APPROVED, Thoth, CF-E-30 review v1.1, 2026-10-28 (Ruling R-A); confirmed by Isis IA-30 v1.1 | None; close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists; HDE Governance §9.7.7; Plan Templates §2) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 | CANON_RECONCILIATION (HDE Build Notes S19 decisions on vendor route selection and the production vendor override) | APPROVED as conditional, Thoth, review v1.1; not triggered per Audit §7 and IA-30 v1.1 §4.4 | **Re-checked at 7100d6f9: not triggered.** Neither module imports or calls a resolver, provider, vendor or HTTP module; I-3 holds |
| CCR-4 | CANON_RECONCILIATION (PF09.3 Task notes vs HDE Build Notes on the loader defect record) | APPROVED, Thoth, review v1.1 | None |

No new entry. OBS-1 is a repository fact about a helper, not a canon conflict: HDE Architecture §1.1's purity rule is applied, not contested.

## 19. PR-30 and PR-35 obligations

* **PR-30** (this session, after the Proceed for exactly v1.0): recover existing work first; implement only §6 from the companion diff; run §11; decide any obvious in-scope correction under the PR-30 rule and record it under *In-flight decisions*; take a material boundary (as PR-30 defines it) to one `RESCOPE_REQUEST` for the IA through RS-20 with `PR_RETURN_PHASE`; commit once; publish one PR; record the replay; write the result record; return `PR_CANDIDATE_PUBLISHED` with one handoff to PR-35 in its own session. It does not resolve reviews, wait for CI readiness or merge.
* **PR-35** (its own dedicated session): subscribe to the PR; retrieve every Codex review finding and thread; fix each that shows a wrong result, a crash or a guarantee breach on a real input, answer every other with the traced path and the stated limit; a P1 on a real input is fixed; declining a P1 or a security finding goes to the Product Owner first; after two consecutive rounds of the same class, one design question to the Product Owner. Re-run §11 items 1 to 5 locally before each coherent corrective push; no `[skip ci]`; known findings before stale CI. **OBS-3:** while `main` is red for `tests/qa/test_generate_epic_close_pack.py`, confirm the hosted failures are exactly that file's base failures; when a fix exists (a merged or open change whose diff you have read and expect to make it pass), port the same change into this PR and push; until one exists, post one PR comment naming the failing check, why it is not this PR's (OBS-3), and that no fix exists yet, and report it to Nathan; do not widen the PR with a fix of your own and never skip or disable the test. Verify current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability; return `MERGE_PENDING — Ready to merge` without merging, with the conditional PR-40 block.
* **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 movement, drainage or closure; no canon edit; no release cut.

## 20. TypeSafe reading and surface advice for the receiving session (PR-30, WU-PR-01, plan v1.0)

* **Method.** Installed TypeSafe scoring skill, request v8.2, `score_v8.py` run once before this plan was saved; session kind `implementation`; label "HDE-EPIC041 PR-30 WU-PR-01 implementation". The Notion row was not written (PR-20 handoff rule).
* **Action sent (v8.2).** "Implement, in a dedicated session, the first of three PR work units of an approved Epic from a detailed PR plan that the Product Owner has proceeded: apply an already prototyped, locally validated change that adds two new Python modules of about 90 and 110 lines (a pure Engine chart validation module and an Adapter-owned orchestration entry), four new test files of about 420 lines, and a 13-line owner-test registration in an existing 2,100-line CI change classifier, changing no existing caller; a task list and a prototype diff exist; run the new tests, the classifier-selected suite of about 170 test files and a full local CI replay, then commit once and open the pull request, which runs all seven CI lanes; no live run against a provider occurs; an automated code review, a separate merge-readiness session and a lineage review follow."
* **Reading, as printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.17 (confidence 0.66); rung probabilities low 0.00, medium 0.17, high 0.52, extra high 0.28, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.93, Sonnet 5.5 0.06, Haiku 5.5 0.00 (confidence 0.91). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.003, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.158, Opus 5.5 at high 0.484, Opus 5.5 at extra high 0.260, Opus 5.5 at max 0.028, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.010, Sonnet 5.5 at high 0.031, Sonnet 5.5 at extra high 0.017, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T04:53:09Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.54 s; 5526 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for PR-30 and none for this PR-20 session (whose reading is the instruction's §13), so none is recorded.
* **Surface advice (PR-30).** PR-30 continues in this same top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, after this plan's documents PR merges, with GitHub access for one PR. It needs CPython 3.12 with CI's install (package-index access), `ruby`, `bash`, `curl` and git, and `env -i` closed rails because the container exports vendor, database and GitHub credentials. Observed times in this session: the new tests under a second; the 170-target set about 8 minutes; the replay about 8 minutes while OBS-3 stops it at step 08; lanes 09 to 15 run directly about 12 minutes (evidence 9). Nathan may want OBS-3 fixed on `main` before PR-35 starts, since PR-35 cannot reach `MERGE_PENDING` while it holds. No open rails, vendor, Railway, database or Notion writes.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage_id | HDE-EPIC041-PR20-WU-PR-01-20261028 |
| change | HDE-EPIC041 (EPIC) |
| specification | `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` (v1.1) |
| work unit | WU-PR-01 (R-01, R-02, R-04 interface part; AC-01, AC-02, AC-04, AC-05) |
| ecosystem release | GCFPE-20261027.1 / 102726.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 102726.1, https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9, page state 2026-10-27T13:18:23.839Z |
| role/stage | dedicated WU-PR-01 PR engineering session / GCF-14 |
| capture time | 2026-10-28 |
| runtime identity | https://claude.ai/code/session_01Q789tyc3umMjXiHB1aoXAR |
| inherited usage | `HDE-EPIC041-PR10-WU-PR-01-20261028` (instruction front matter) |
| repository persistence | PENDING: `docs/changes/` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`; no installed `GCFPE_PROMPT_PROVENANCE.md`. Owner: GCFPE management. Non-gating |

## Canon relied on

Resolved from `docs/pfcanon/` on `main` 7100d6f9; this branch changes nothing there. Terms searched: per-PR, PR implementation plan, Proceed, chart loader, `engine/charts`, purity, Adapter-owned, orchestration, business case, work unit, Doc-Delta, CI cost, lane classification.

| Title | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Checklist — Separation | Task HDE-SEPA006; Subtasks .1 to .3 | Scope; .1 before .2; evidence |
| HDE Architecture | §1.1 "Single homes" (Purity rule; BodyGraph seam carve-out; Non-BodyGraph chart loader classification; `adapter/`; Guards) | Ownership split; purity; no ad-hoc serialization on public paths (the log line is not a public path) |
| HDE Mechanics Guide | §1.1 "Audit classification for I/O-bearing engine seams", "BodyGraph and loader seam posture" and the remediation paragraph | No fallback, no Engine I/O exception, no second resolver; preserve outputs |
| HDE Governance | §9.1.1; §9.1.2; §9.1.3 (storage; GCFPE model guidance); §9.1.4; §9.2; §9.7.7 (holds, business cases, severity, plans not blocked on syntax); §4.3.9 | Hold label `ASK OK? — PR IMPLEMENTATION PLAN`; Proceed is the approval; business case and stop rule; Doc-Delta triggers; CI economy |
| Plan Templates | §12 "General Implementation Plan (Template)"; "Canon precedence for template use"; "CI lane classification and automated budget-control discipline" | Shape; precedence quote; CI lane posture |
| Change Process Guide | §0.2 "Policy and principles" (PR route contents; no PF-canon edits) | PR carries code, Doc-Delta updates and evidence companions where required |
| HDE Build Notes | Whole file, 501 lines, read in this session (blob cb61644d…, unchanged since the Audit): precedence rules 1 to 9 and its one addendum, 2.1 (D-1 to D-5) | Silent on this unit. Addendum 2.1 governs production vendor gating, vendor route selection, compat route gating, evidence-tool output roots and gate-row content; this unit touches none of them (no vendor acquisition, no route, no evidence tool, no gate row) |

## Approval

* **Approval hold:** `ASK OK? — PR IMPLEMENTATION PLAN`
* **Approval state:** Pending.
* **Approval authority:** Nathan / Product Owner, by invoking `PR Implementation Proceed` (PR-30) for exactly this v1.0.
* **Approved scope or rejection basis:** not yet decided.

## Nonclaims

This plan is not implementation, a Proceed, a PR, CI, QA, Ops, acceptance, a PF09 or board movement, a canon change, a PF10 addendum or closure. The prototype results are local scratch observations, not CI, not QA and not governed evidence. Nothing outside `docs/ephemeral/` is changed by this plan's PR. Merging it preserves the record and approves nothing (D21-C).
