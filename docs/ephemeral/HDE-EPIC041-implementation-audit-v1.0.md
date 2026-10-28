---
artifact_type: IMPLEMENTATION_AUDIT
artifact_version: "1.0"
logical_id: HDE-EPIC041-IMPLEMENTATION-AUDIT
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
state: AUDIT_COMPLETE
author: whole-change Implementation Agent for HDE-EPIC041 (bound by this IA-10 FIRST_ENTRY invocation; session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
prompt: IA-10 — Create Whole-Change Implementation Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb813281cbc25f2f30db13; page state 2026-10-27T13:16:07.631Z, read in full)
entry_mode: FIRST_ENTRY
r1_rows: GCF-09 (this artifact); GCF-10 follows in the separate Plan
ecosystem_release: GCFPE-20261027.1 / 102726.1 (selected by the GCFPE Membership and Release Register, "Current selection", read 2026-10-28)
approved_specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; 51,861 bytes; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28)
thoth_decision: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md (CF-E-30, INITIAL_APPROVE, ASK OK; merged by amthorn78/glow-hdengine-v2#784 as b29ca84)
prior_decision_in_force: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md (INITIAL_DENY of v1.0; Rulings R-A to R-C kept in force)
canon_conflict_register: review v1.1 §5, CCR-1 to CCR-4 (dispositions in §7 below)
repository_head_audited: origin/main b29ca84a5c134fe7f54fd21cba955b0dab64c0ea (full clone; unshallowed for this audit)
audited_at: 2026-10-28 (UTC)
successor_artifact: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md (the separate initial pending Plan)
pf10_resolved: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md (501 lines, read in full; one addendum, 2.1, not applicable to this change; see §1.3)
pf10_addenda_applicable: NONE
---

# HDE-EPIC041 — Implementation Audit (GCF-09)

This audit is complete. Every requirement and acceptance criterion of the approved Specification v1.1 has a planning disposition (§4). It approves nothing and authorizes no PR, Proceed, Ops, QA, PF09 movement or closure. Merging this file preserves the record and approves nothing (D21-C).

## 1. Sources, selection and canon relied on

### 1.1 Inputs verified

| Input | Check | Result |
| :- | :- | :- |
| Approved Specification v1.1 | Read in full; identity matches review v1.1 front matter | Immutable approved base for this change |
| Thoth decision, review v1.1 | Read in full; `INITIAL_APPROVE`, `ASK OK`; next prompt IA-10; IA binding "not yet bound" | Authorizes Audit and Plan preparation only |
| Review v1.0 | Read in full; Rulings R-A, R-B, R-C | Kept in force by review v1.1 |
| CANON_CONFLICT_REGISTER | Review v1.1 §5, CCR-1 to CCR-4 | Each disposed in §7 |
| PR #784 merged | `origin/main` head is `b29ca84`, "HDE-EPIC041 Epic Specification review v1.1, INITIAL_APPROVE of v1.1 (CF-E-30) (#784)" | Precondition of the handoff met |
| Prompt selection | GCFPE Membership and Release Register, "Current selection — GCFPE-20261027.1 / 102726.1", exactly 56 members; IA-10 sits in "HDE IA — GCFPE-20261027.1 — 102726.1" | IA-10 102726.1 is selected. Only the register's current-selection section and its binding table were read; its historical sections (about 118 KB) were not needed and were not read |
| IA binding state | Review v1.1 §6: "no whole-change Implementation Agent is bound yet. IA-10 FIRST_ENTRY binds one" | This invocation binds the IA role for HDE-EPIC041 |
| Denied or unavailable access facts | Review v1.1 §6: none | None encountered |

### Canon relied on

Resolved from `docs/pfcanon/` on `main` `b29ca84`. This branch changes nothing under `docs/pfcanon/`. Terms searched: chart loader, `engine/charts`, `load_chart`, `get_chart`, `loader_call`, SEPA006, purity, Adapter-owned, orchestration, implementation audit, implementation plan, business case, work unit, doc delta, `make_compat_determinism`, open-rails, production-functional.

| Document (title; file) | Sections read in full | What it governs here |
| :- | :- | :- |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 (lines 1280 to 1379) | Scope, sequencing (.1 before .2; .3 reconciles), deliverables, Product Owner as decision owner |
| HDE Architecture (`PF02-…-v2.4.7.md`) | §1.1 "Single homes", whole section including "Purity rule", "BodyGraph seam carve-out", "Non-BodyGraph chart loader classification [Required-Now]", `adapter/` and Guards; §2.1 "Behavior-only boundary" and "Surfaces vs evidence" | Ownership split; purity predicate (no time, network, file I/O, randomness, environment reads; no import-time side effects) |
| HDE Mechanics Guide (`PF14-…-v3.5.9.md`) | §1.1 "Capabilities the repo must provide": "Audit classification for I/O-bearing engine seams", "BodyGraph and loader seam posture" and its remediation paragraph | "Remediation must migrate active callers, including compatibility/determinism and generator callers … preserve existing canonical outputs and public/vendor contracts; it does not authorize fallback behavior, an Engine Core I/O exception or a second resolver" |
| HDE Governance (`PF04-…-v2.8.8.md`) | §9.1.1; §9.7.7 "Business case for every requirement and work unit"; GATE:CORE-DET, D.1 and D.3 (lines 4205 to 4620, the three bullets naming `scripts/make_compat_determinism_artifacts.py`) | Work-unit business cases; the generator is a canon-named recompute script |
| Change Process Guide (`PF06-…-v2.5.5.md`) | §2.2 "Audit (the executing agent)" with "Findings → Doc Delta Map"; §3 "Implementation Plan" (3.1 to 3.4); §0 PR-route Doc-Delta rule (line 72) | Audit output fields (§9, §10 here); negative/no-hit proof rule (§5.2 here) |
| Plan Templates (`PF27-…-v2.0.6.md`) | §12 "General Implementation Plan (Template)"; "Canon precedence for template use"; "Repository loci and file minting" | Plan shape (used by the Plan); precedence rule |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`) | Whole file, 501 lines | §1.3 |
| Reality Audits (`PF23-…-v1.2.3.md`) | RA-20261026-08 and FND-022 rows (loader) | Context only: aligned observation of the loader's I/O; no authority over requirements |
| HDE State of the Repository (`PF31-Reference-…-v0.1.md`) | §2.2 | Reference context only |
| AGENTS.md | Canon-first rule; closed rails; pytest readiness; pre-push check; QA output placement; governed evidence rules; Doc agents | Audit method and Plan constraints |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

### 1.3 PF10 resolution

* Current controlled PF10: `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md`, unlettered, the only PF10 file in `docs/pfcanon/`. Read in full (501 lines).
* Addenda: one, 2.1, "Canon policy for the S19 routed security findings". Its scope is the production vendor override (D-1), vendor route selection (D-2), compat route gating (D-3), evidence-tool output roots (D-4) and gate-row content (D-5).
* Applicability: none to this change. The Audit found that no path in scope performs vendor acquisition, resolver-selected or otherwise (O-09, O-10), registers or changes an HTTP route, or writes governed gate rows or attestation outputs. CCR-3 is therefore not triggered (§7).
* The initial Specification approval produced no PF10 addendum (review v1.1 front matter, `pf10_addendum: NONE`).
* `approved base + applicable PF10 overlays` = Specification v1.1 + NONE.

## 2. Method and repository identity

* Repository `amthorn78/glow-hdengine-v2`, `origin/main` `b29ca84a5c134fe7f54fd21cba955b0dab64c0ea`. The clone was unshallowed (`git fetch --unshallow`) so the commits for TI-05 resolve.
* Static method: `git grep` over all tracked files (patterns in §5.2), `git log`, `git show`, `git diff`, and direct reads of each named file.
* Executed method, closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`):
  * Interpreter Python 3.13.17, in a scratch virtualenv installed as AGENTS.md's pytest-readiness rule directs (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), with `python -m pytest --version` reporting `pytest 8.4.2`.
  * All execution was run from the repository root or from a scratch working directory outside the repository.
  * After every run, `git status --porcelain` was empty, and `artifacts/logs/loader_call.jsonl` kept SHA-256 `24b6c8423e98f4ce3b0a010a47787f18102f2a6904788873b564bae4625cf236`.
* Actor and time: this IA, 2026-10-28 from 03:32:56Z UTC.
* Limitation: all execution is local and closed-rails. It is not CI, not QA and not governed evidence.

| Run | Command (summary) | Result |
| :- | :- | :- |
| X-1 | `python -m pytest -q -p no:cacheprovider tests/loader tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on tests/evidence/test_architecture_snapshot.py` from the repository root | 17 passed, exit 0; tracked tree unchanged |
| X-2 | `load_chart('user-abc', correlation_id=…)` from a scratch CWD | `AttributeError: 'FixturesProvider' object has no attribute 'get_chart'`; wrote `artifacts/logs/loader_call.jsonl` and `artifacts/provider/decision.txt` under that CWD |
| X-3 | `load_chart('1990-01-01','12:34','Amsterdam, NL', tz='Europe/Amsterdam')` from a scratch CWD | `LoaderInputError: invalid place`, caused by `FileNotFoundError: artifacts/constants/iso_3166_1_alpha2.json`; one `status:"error"` log line written under that CWD |
| X-4 | `python scripts/make_compat_determinism_artifacts.py` from a scratch CWD | stderr `compat_public not implemented`, exit 2, before any chart load; no file written by it |
| X-5 | `python tools/evidence/generate_architecture_snapshot.py --check` | `STALE:artifacts/architecture/architecture_snapshot.keys_only.json`, exit 1 (pre-existing on `main`; see O-14) |
| X-6 | Import `adapter.factory`, `adapter.wsgi`, `adapter.http_reader`, `engine.cli.main`, `engine.compat.compute`, `engine.bodygraph.resolver` with `APP_ENV=dev`; list loaded `engine.charts*`, `engine.util.input_validators`, `engine.config.provider_loader` modules | None loaded |

## 3. Observed facts

E-1 to E-5 are the Specification's. O-01 onward are this Audit's, and each restates or extends an E-item where it says so.

| ID | Fact | Basis |
| :- | :- | :- |
| O-01 | `engine/charts/loader.py`: 173 lines, 6,338 bytes, blob `8ea4dce2…`. Last changed by `6c6f4b2a` (2025-09-28). It is byte-identical to its state at `5ef911fe`, the commit HDE Architecture §1.1 classifies (`git diff --stat 5ef911fe HEAD -- engine/charts/loader.py` empty) | `git log`, `git diff` |
| O-02 | The loader's operational concerns, by line: `SAFE_MODE` read (54); wall clock `datetime.now` (49); `time.perf_counter` (95, 168); correlation id via `ensure_cid`, which synthesizes with `secrets.token_hex` (97; `engine/util/input_validators.py` 60 to 70); keys-only JSONL append to `artifacts/logs/loader_call.jsonl` relative to CWD, creating the directory (57 to 73); legacy provider selection through `engine.config.provider_loader.resolve_provider` (20 to 23, 76 to 82) | Direct read (confirms E-4) |
| O-03 | The new-signature path performs no acquisition. After validation it returns a fixed literal: `{"gates":[1,2,3],"channels_short":[],"centers":[],"type":"","authority":"","profile":"","meta":{"provider":"fixtures","source":"default"}}`. Its own comment reads "Minimal normalized fixtures result (no network here)" | Direct read, lines 139 to 150 |
| O-04 | The legacy path is broken for every provider `resolve_provider` can construct. `fixtures`, `internal_engine` and `vendor_http` (`engine/provider/*.py`) define only `get_pair_profile`. `get_chart` exists only on `engine/providers/fixtures_provider.py::FixturesProvider`, which `provider_loader.py` does not import. When the resolver import fails, the path returns fallback data `{"gates":[1,2,3]}` (78 to 79) | `grep` of the three classes; X-2 (confirms and extends E-1) |
| O-05 | A legacy call also writes `artifacts/provider/decision.txt` relative to CWD, through `resolve_provider` → `_write_decision`. With `ENGINE_SECRETS_DIR` set it can also run `git rev-parse` as a subprocess (`provider_loader.py` 46 to 57) | X-2; direct read |
| O-06 | New-signature validation reads the pinned lists `artifacts/constants/iso_3166_1_alpha2.json` and `artifacts/constants/iana_tz_list.json` from disk on every call, relative to CWD (`input_validators.py` 12 to 19, 46, 53). From any CWD other than the repository root, a valid place is misreported as `READER_INVALID_INPUT` / `invalid place` | X-3 |
| O-07 | The kwargs form of the new signature (lines 160 to 163) calls `load_chart` recursively, so one call writes two log lines with the same correlation id | Direct read; paired lines with equal `correlation_id` in `.audit_src/artifacts/logs/loader_call.jsonl` |
| O-08 | The tracked `artifacts/logs/loader_call.jsonl` (67 lines, blob `92556952…`) is not in `docs/evidence/INDEX.json` or `artifacts/evidence_index.jsonl` (0 matches in each). Committed runs appended to it three times: `39a5a33a` (2025-09-29, +25 lines), `f3e1f9a1` (2026-04-27, "HDE-EPIC030 QA PASS 1", +12) and `c6fdc913` (2026-05-01, "HDE-EPIC030 QA PASS 2", +4) | `grep -c`; `git show --numstat` (extends E-2: the mutation recurred and was committed) |
| O-09 | No production entry point loads the loader. Importing the selected factory, the WSGI factory, the Reader module, the CLI, the compat compute module and the BodyGraph resolver loads none of `engine.charts*`, `engine.util.input_validators` or `engine.config.provider_loader` | X-6 |
| O-10 | `engine/charts/loader.py`, `engine/util/input_validators.py`, `engine/config/provider_loader.py` and `scripts/make_compat_determinism_artifacts.py` are not release members. `catalog/manifest.json` lists 45 members, none of them these | Manifest read |
| O-11 | `scripts/make_compat_determinism_artifacts.py` exits 2 with `compat_public not implemented` before it calls `load_chart`, because `engine.compat.compute.compat_public` was removed by `cd6f9e6c` (2026-09-22, "HDE-EPIC040-PR04: bounded application, identity and consumer integration (#467)"). Its module-level `from engine.charts.loader import load_chart` (line 9) still executes on every run. HDE Governance GATE:CORE-DET, D.1 and D.3 still name it as a recompute and byte-compare script | X-4; `git log -S 'def compat_public'`; PF04 |
| O-12 | The compat proof bytes `artifacts/compat/AB.json`, `BA.json` (both blob `7fe71f99…`, 62 bytes) and `identity_hash.txt` (65 bytes) are tracked and indexed (`AB.json` 1 match in the Human Index). The script writes `identity_hash.txt` when it runs to completion. `tools/evidence/generate_epic030_pr03_compat_evidence.py` binds all three | Direct read; `grep` |
| O-13 | `ci/checks/classify_ci_changes.py` maps no owner test for `engine/charts/loader.py`, `engine/util/input_validators.py`, `engine/config/provider_loader.py`, `scripts/make_compat_determinism_artifacts.py`, or a new module under `engine/charts/` or `adapter/`. A change to any of them fails classification with `CI_PRODUCT_OWNER_TEST_MISSING:<path>`. `tests/loader/test_load_chart_fixture_only.py` and `test_loader_logs_keys_only.py` are listed in its product test roster (112, 114) and in `pytest.ini` `testpaths` (72, 74) | `_product_owner_targets` called per path; direct read |
| O-14 | `.audit_src/`, `_archive/` and `artifacts/architecture/` are in the classifier's `_HISTORICAL_PREFIXES` (lines 156 to 165). The architecture snapshot is already stale on `main`: it lacks 4 current paths, keeps 2 removed ones and differs on 28. Its `--check` is not a CI step, and its CI test checks only that analysis is read-only and passes | X-5; classifier read; `tests/evidence/test_architecture_snapshot.py` |
| O-15 | `.audit_src/engine/charts/loader.py` is byte-identical to the live loader. `.audit_src/` was added by `cfc48dc6` (2025-10-22, "HDE-EPIC004: close") and last touched on 2025-12-04 | `diff`; `git log` |
| O-16 | An existing purity-check pattern exists in `tests/core/test_engine_core_purity.py`: an AST import/call deny-list over named pure paths, plus a fresh-interpreter import-and-compute side-effect test. A request-scoped socket/DNS attempt counter exists at `adapter/no_io_guard.py` | Direct read |
| O-17 | `engine/util/input_validators.py` has one other caller, `engine/providers/vendor_http_hdapi.py` (and `tests/loader/test_validators_strict.py`) | `git grep` |
| O-18 | TI-05: `6c6f4b2a` resolves to 2025-09-28T15:00:32Z, "CORE-CHART-LOADER-READY-001: close 20250928T150032Z", the loader's last change, and matches the date canon states. `5ef911fe` resolves to 2026-08-09, "docs: replace PF01 v1.3.1 with v1.3.2", a docs-only commit at which the loader is unchanged (O-01). Canon's citations are accurate | `git show -s` on the unshallowed clone |
| O-19 | The retained-coverage tests named by PF09.3 pass on `main`, as do the five current `tests/loader` files and the architecture-snapshot test | X-1 |
| O-20 | No repository documentation outside `docs/pfcanon/` and `docs/ephemeral/` describes the loader. `tests/retired_tests.md` row 57 records the retired legacy test and the defect. `CHANGELOG.md` carries one "Unreleased — <change>" section per change's final documentation pass (HDE-CRD-0002 WU-DOC-01; HDE-EPIC040) | `git grep`; direct read |

## 4. Requirement coverage and planning dispositions

Every requirement and criterion below has a disposition. None is blocked.

### R-01 — Adapter-owned orchestration (HDE-SEPA006.1)

* **Source clause.** Specification §3 R-01; PF09.3 Task "Implementation / integration boundary" and Subtask .1; HDE Architecture §1.1; HDE Mechanics Guide §1.1.
* **Current behavior.** Every operational concern listed in R-01 sits in Engine code (O-02). Provider selection exists only on the broken legacy path (O-04, O-05). Acquisition on the supported path is a fixed in-process fixture literal (O-03). No vendor or database acquisition occurs on any path.
* **Required behavior.** One supported Adapter-owned entry owns rails and environment reads, provider or source choice, acquisition, both clocks, correlation context, keys-only operational logging and any filesystem access. Vendor/DB acquisition, if any, uses the sanctioned resolver/ingest boundary. No fallback data and no additional Engine I/O carve-out.
* **Affected components.** New Adapter-owned module under `adapter/`, path to be fixed by the per-PR plan; `engine/charts/loader.py` (removed by R-03); `engine/util/input_validators.py::ensure_cid` (called from the orchestration, unchanged).
* **Dependencies.** None upstream. R-02's pure interface is consumed by it.
* **Feasibility.** Feasible with no new provider contract, because the supported path acquires only the fixture literal and needs no resolver (O-03, O-09). The resolver/ingest clause is satisfied vacuously, and the Plan must not add vendor or DB acquisition.
* **Risks.** Adding acquisition would bring in CCR-3 and the live-proof binding condition. Changing the log line's keys or route value would break the keys-only log contract that `tests/loader/test_loader_logs_keys_only.py` pins. Writing the tracked log again would repeat E-2.
* **Tests/evidence needs.** Rails, correlation, keys-only logging and failure-behavior tests with controlled fixtures and an injected log sink; a zero-socket check (`adapter/no_io_guard.py`); a tracked-files-unchanged check.
* **Canon/documentation effects.** Drainage candidates once delivered: HDE Architecture §1.1 ("remains current repository reality until separately remediated") and HDE Mechanics Guide §1.1 loader posture (§9, FND-003).
* **Gaps.** None.
* **Disposition.** Plan WU-PR-01.

### R-02 — Pure Engine chart validation and normalization (HDE-SEPA006.1)

* **Source clause.** Specification §3 R-02; PF09.3 Subtask .1; HDE Architecture §1.1 purity rule.
* **Current behavior.** Validation is mixed with operational code. Its helpers read pinned lists from disk relative to CWD on every call (O-06). `_normalize_chart` is pure. The typed error `LoaderInputError` is pure.
* **Required behavior.** Explicit data-in/data-out validation and normalization with no time, randomness, environment, network, provider, logging or filesystem effect, and none at import. Explicit inputs, outputs, failure behavior and orchestration ownership defined.
* **Affected components.** New pure module under `engine/charts/`, path to be fixed by the per-PR plan, taking the ISO-3166 and IANA lists as explicit arguments. `engine/util/input_validators.py` stays unchanged for its other caller (O-17).
* **Dependencies.** None.
* **Feasibility.** Feasible. The validation logic is small and pure once the lists are passed in.
* **Risks.** Divergence from `input_validators` rules. Mitigation: the per-PR plan either reuses its pure parsing helpers (`parse_date_yyyy_mm_dd`, `parse_time_hh_mm` are pure) or proves equality with characterization tests.
* **Tests/evidence needs.** An AST deny-list test and a fresh-interpreter import/call side-effect test, following O-16. A negative self-test proving the checker flags a violating source.
* **Canon/documentation effects.** As R-01.
* **Gaps.** None.
* **Disposition.** Plan WU-PR-01.

### R-03 — Caller migration and retirement (HDE-SEPA006.2)

* **Source clause.** Specification §3 R-03; PF09.3 Subtask .2; HDE Mechanics Guide §1.1 remediation paragraph.
* **Current behavior.** Three supported callers (§5.1). The legacy signature has no supported caller (O-04, E-3).
* **Required behavior.** Every supported caller migrated to the correct interface. The old operational Engine path removed, or only a genuinely pure surface kept under an owning contract. Not merely an import-path rename. Historical captures unchanged. Governed caller output and failure behavior preserved.
* **Product Owner decision D-1 (TI-01), made 2026-10-28.** Nathan / Product Owner answered "Retire it" to IA-10 question Q-01 (§8). The legacy signature `load_chart(user_id)`, `_call_legacy`, its `resolve_provider` import and the `{"gates":[1,2,3]}` resolver-unavailable fallback are retired. No compatibility surface is retained, so TI-06 needs no owning contract.
* **Affected components.** `scripts/make_compat_determinism_artifacts.py`; `tests/loader/test_load_chart_fixture_only.py`; `tests/loader/test_loader_logs_keys_only.py`; `engine/charts/loader.py` (removed); `pytest.ini` `testpaths`; `ci/checks/classify_ci_changes.py` (owner mappings and test roster, O-13).
* **Dependencies.** R-01 and R-02 delivered (PF09.3 ".1 before .2").
* **Feasibility.** Feasible. The script's behavior on `main` is exit 2 before the chart load (O-11), so preserving its governed output and failure behavior means its stderr, exit status and no-write outcome stay identical, and the compat bytes of O-12 stay unchanged.
* **Risks.**
  * Removing the module while an importer remains would turn the script's exit 2 into an `ImportError`, a changed failure behavior. Mitigation: migrate the script in the same work unit as the removal.
  * Restoring the script's compat computation is not part of HDE-SEPA006 (FND-005).
* **Tests/evidence needs.**
  * A repository-wide guard: no tracked Python file outside the historical prefixes (O-14) imports `engine.charts.loader`.
  * Script behavior preserved: exit 2 and its stderr, run from a temporary CWD, with no file written.
  * Compat bytes unchanged.
  * Caller-regression results.
* **Canon/documentation effects.**
  * HDE Governance GATE:CORE-DET, D.1 and D.3 keep naming the script; that stays true.
  * `tests/retired_tests.md` row 57 stays as history.
  * CHANGELOG entry (WU-PR-03).
* **Gaps.** None.
* **Disposition.** Plan WU-PR-02.

### R-04 — Boundary and behavior verification (HDE-SEPA006.3)

* **Source clause.** Specification §3 R-04; PF09.3 Subtask .3.
* **Current behavior.**
  * The two loader tests redirect the log write by monkeypatching `_Path` (O-13 files).
  * No purity, import-side-effect or caller-completeness check exists for chart code.
* **Required behavior.**
  * Purity and no-import-side-effect checks.
  * Orchestration rails, correlation, keys-only logging and failure behavior exercised with controlled fixtures.
  * Complete caller migration verified.
  * R-01 to R-03 reconciled.
* **Affected components.**
  * New tests under `tests/`. The paths are fixed by the per-PR plans.
  * Owner mappings in `ci/checks/classify_ci_changes.py`.
* **Dependencies.** PF09.3: "Develop verification with both changes". The interface checks ship with WU-PR-01. The caller-completeness checks and the reconciliation ship with WU-PR-02.
* **Feasibility.** Feasible with existing patterns (O-16).
* **Risks.** A purity check that cannot fail. Mitigation: a negative self-test is required.
* **Tests/evidence needs.** AC-04's recorded fields: commands, configuration, tested-source identity, results, actor, time and limitations. The PR records carry them.
* **Canon/documentation effects.** None.
* **Gaps.** None.
* **Disposition.** Split by PF09.3's own sequencing: WU-PR-01 (interface-level) and WU-PR-02 (migration-level and reconciliation).

### Acceptance criteria

| AC | Disposition | Where satisfied | Evidence that will exist |
| :- | :- | :- | :- |
| AC-01 | Plan | WU-PR-01 (entry), WU-PR-02 (no operational concern left in `engine/charts/`) | Interface and side-effect account in the PR; orchestration tests; WU-PR-02 guard |
| AC-02 | Plan | WU-PR-01 | AST and fresh-import tests, with a negative self-test |
| AC-03 | Plan | WU-PR-02 | Supported-caller inventory (§5.1, re-verified at the WU-PR-02 head) with dispositions; module removed; repository-wide import guard |
| AC-04 | Plan | WU-PR-01, WU-PR-02 | Test results with the recorded fields |
| AC-05 | Plan | WU-PR-01, WU-PR-02 | Output preservation of the fixture chart; script exit 2 preserved; compat bytes unchanged; `git status --porcelain` empty after the covering tests; no fallback data in the changed boundary |

## 5. Supported-caller inventory (TI-03)

### 5.1 Inventory with dispositions

| # | Path | Kind | Supported? | Calls | Disposition |
| :- | :- | :- | :- | :- | :- |
| C-1 | `scripts/make_compat_determinism_artifacts.py` | Tooling | Yes. Canon names it the "active compatibility-determinism artifact generator" (PF09.3) and a recompute script (HDE Governance GATE:CORE-DET) | `load_chart(**kwargs)` new signature; module-level import | Migrate to the orchestration entry (WU-PR-02). Preserve exit 2, its stderr and the no-write outcome (O-11) |
| C-2 | `tests/loader/test_load_chart_fixture_only.py` | Test | Yes (`pytest.ini`, classifier roster) | New signature, positional; `LoaderInputError` | Migrate to the orchestration entry and the pure interface (WU-PR-02). Drop the `_Path` monkeypatch in favor of an injected sink |
| C-3 | `tests/loader/test_loader_logs_keys_only.py` | Test | Yes (same) | New signature; keys-only log line | Migrate to the orchestration's keys-only logging with an injected sink (WU-PR-02) |
| C-4 | Legacy signature `load_chart(user_id)` | Interface | No supported caller (retired test only) | — | Retired by D-1 (WU-PR-02) |
| H-1 | `.audit_src/engine/charts/loader.py`, `.audit_src/scripts/make_compat_determinism_artifacts.py`, `.audit_src/tests/loader/` (three files), `.audit_src/tests/compat/test_compat_public_ab_ba_identity.py`, `.audit_src/tests/compat/test_compat_public_lf_bom.py`, `.audit_src/tests/provider/test_provider_call_logging_keys_only.py`, `.audit_src/artifacts/logs/loader_call.jsonl` | Historical audit capture | No. CI historical prefix; HDE-EPIC004 close capture; not collected by `pytest.ini` | — | Unchanged (R-03; RL-7) |
| H-2 | `.audit_src/adapter/http_reader.py`, `.audit_src/_archive/EPIC003_CLEAN_20251017_211719/server/app.py` (review v1.1 N-3); `adapter/http_reader.py::_safe_load_chart` | Name collision only | Not callers: `_safe_load_chart` reads a fixture JSON by path and imports no loader | — | Unchanged |
| H-3 | Inventories and captures naming the loader as text: `artifacts/architecture/architecture_snapshot.keys_only.json`, `artifacts/epic004/guards/forbidden_serializers.txt`, `artifacts/math/_manifest_files.txt`, `artifacts/qa/a7_presence.rg.txt`, `artifacts/qa/evidence_presence.rg.txt`, `audit/inventory_epic007.json`, `codex/out/008.evidence_inventory.json`, `manifest_pre.sha256`, `manifest_post.sha256`, `_arch/**`, `handoff/epic004_live_evidence_20251022T202304Z/**`, `notes/dev-sampler/*.txt` | Historical capture or evidence text | Not callers | — | Unchanged |
| H-4 | `tests/retired_tests.md` row 57 | Retirement registry | Not a caller | — | Unchanged, as history |
| N-1 | `pytest.ini` (72, 74); `ci/checks/classify_ci_changes.py` (112, 114) | CI selection lists | Name C-2 and C-3 | — | Updated in WU-PR-02 if C-2 or C-3 is renamed or moved; owner mappings added for every new or changed product path (O-13) |
| N-2 | `engine/config/provider_loader.py`, `engine/providers/fixtures_provider.py`, `engine/util/input_validators.py` | Callees, each with other callers (`tests/provider/*`, `tests/provider/test_provider_interface_contract.py`, O-17) | — | — | Unchanged |

### 5.2 Negative and no-hit proof (Change Process Guide §2.2)

* **Scope.** All tracked files on `main` `b29ca84`, excluding `docs/pfcanon/` and `docs/ephemeral/`.
* **Patterns.** `engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy`. These also match dynamic-import strings such as `importlib.import_module("engine.charts.loader")`.
* **Result.**
  * Live importers of the loader: C-1, C-2 and C-3 only.
  * No match under `engine/` other than the module itself, and none under `adapter/`, `presenter/`, `tools/`, `ci/` or `.github/`.
  * Under `docs/`, only the two excluded trees match.
  * `pyproject.toml`'s only console script is `hdctl = engine.cli.main:cli`, which X-6 shows does not load the loader.
* **Runtime corroboration.** X-6.
* **Limitation.** The proof covers import paths and string references, not code generated at runtime from computed strings. None was found, and the per-PR plan re-runs this search at its own head.

## 6. Public, CLI and production reach; open-rails binding condition

* **Finding.**
  * No affected surface is used to produce a production feature.
  * No affected surface reaches vendor acquisition in a deployed or CLI path.
  * The changed boundary cannot affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior.
  * The basis is O-03, O-04, O-09, O-10 and §5.2.
* **Consequence for Specification §4.**
  * Item 3's binding condition is not met, so on this evidence the mandatory bounded live vendor test does not attach.
  * Item 4's condition is not met, so no open-rails step or exemption is required by it.
  * Both items are preserved verbatim in the Plan for the QA Plan owner (Ruling R-B).
  * If a per-PR plan or QA-10 finds new reach, the conditions re-attach.
* **Limitation.** The basis is static search plus import of the named entry points under `APP_ENV=dev`. It is not a deployed-environment observation.

## 7. Tracked issues, review observations and canon conflict register

| Item | Disposition at Audit | Owner going forward |
| :- | :- | :- |
| TI-01 / D-1 | Decided by the Product Owner, 2026-10-28: retire (§8 Q-01) | Closed for planning; delivered by WU-PR-02 |
| TI-02 | Candidate CRD Items List items 9 and 10 share no file with this change's planned paths. Item 9's paths (`adapter/http_reader.py`, `engine/providers/vendor_http.py`, the resolver) are not touched by the Plan. The S19 decisions do not apply (§1.3). The `main` CI failure: not re-verified by this Audit. The Plan requires each PR to read current-head CI | Product Owner (items 9 and 10); each PR session (CI state) |
| TI-03 | Resolved: §5 | Re-verified at each PR head |
| TI-04 | Resolved: the retained-coverage tests pass on `main` (X-1, O-19) | AC-05 regression in WU-PR-02 |
| TI-05 | Resolved: both commits resolve and match canon (O-18) | Closed |
| TI-06 | Moot under D-1: no compatibility surface is retained, so no owning contract is needed | Closed |
| TI-07 / CCR-1 | Unchanged: the acceptance map stays in the close baseline with no token roster (Ruling R-A). It is a close-pack matter, not implementation | Product Owner (possible canon change); CL-05 at close |
| N-1, N-2 | Nits in the approved base; not editable. No planning effect | None |
| N-3 | Inventoried: H-1 and H-2 | Closed |
| CCR-2 | No effect on implementation | None |
| CCR-3 | Not triggered: no resolver-selected vendor acquisition in scope (O-03, O-04, O-09). The Plan forbids adding any | Re-checked at each PR head |
| CCR-4 | No effect | None |

## 8. Questions, engineering choices and scope boundaries

### 8.1 Decisive question

**Q-01 (answered).**

* **Question.** What should happen to the legacy signature `load_chart(user_id)`?
* **Affected:** R-03, AC-03, TI-01, TI-06.
* **Inspected evidence:** O-04, O-05, E-3; the canon search for an owning contract (none in `docs/pfcanon/`).
* **Known facts.**
  * There is no supported caller.
  * The signature is broken for every resolvable provider.
  * A repair needs a `get_chart` provider contract or fixture/fallback data, both excluded by the Specification's non-goals.
  * Pure retention is impossible because the path selects a provider.
* **Alternatives:** retire; repair (a Specification change); retain as a pure surface (needs an owning contract).
* **Decision criteria:** consistency with the non-goals and with R-03.
* **Owner:** Nathan / Product Owner (PF09.3 Task owner line).
* **Stage deadline:** before the Plan.
* **Answer:** "Retire it", given in this IA-10 session on 2026-10-28 through the session's question tool.

### 8.2 Engineering choices within IA authority

Isis reviews each of these at IA-30.

| ID | Choice | Basis |
| :- | :- | :- |
| ED-01 | The orchestration entry lives in the `adapter/` package as a non-HTTP module. It registers no route and is not a release member | HDE Architecture §1.1: Adapter applies guards and rails; `adapter/` already holds non-HTTP infrastructure (`env_guard.py`, `no_io_guard.py`, `db_access.py`) |
| ED-02 | The pure module lives under `engine/charts/` and takes the pinned ISO-3166 and IANA lists as explicit arguments. It returns data, or raises a typed error carrying today's `code` (`READER_INVALID_INPUT`) and `details.field` values | R-02; failure behavior preserved |
| ED-03 | The orchestration reads the pinned lists from their existing files, resolved against the repository root rather than the CWD | O-06 is a misreport of valid input, not governed behavior. Every governed caller runs at the root, so its behavior is unchanged |
| ED-04 | The keys-only log line keeps today's keys and values (`ts, route="loader.load_chart", provider, source, status, duration_ms, safe_mode, correlation_id`). It is emitted to an injectable sink whose default is a Python `logging` logger, with no default file write. One line per call: the O-07 double line is not reproduced. The tracked `artifacts/logs/loader_call.jsonl` is left unchanged as a historical record | R-01 (filesystem writes owned by orchestration); E-2, O-08. The file is not governed evidence (O-08) |
| ED-05 | The log's `safe_mode` field keeps the loader's reading (`SAFE_MODE == "1"`, unset → `false`). It has no rail effect, because the supported path performs no acquisition | Preserve the pinned log semantics; no behavior change |
| ED-06 | `engine/charts/loader.py` is removed entirely in WU-PR-02, together with the migration of C-1 to C-3. No re-export shim is kept | D-1; AC-03; "An import-path rename alone is not migration" |
| ED-07 | Only the import and chart call of C-1 change. Its `compat_public` lookup, exit 2 and write logic stay as they are | R-03 "preserves governed caller output and failure behavior"; FND-005 |
| ED-08 | `engine/util/input_validators.py`, `engine/config/provider_loader.py` and `engine/providers/fixtures_provider.py` are unchanged | Other callers (N-2); not chart-loader scope |
| ED-09 | No historical capture is regenerated, including the stale architecture snapshot | R-03; O-14 |
| ED-10 | No vendor or DB acquisition, provider contract, fallback data, route, flag, CLI option or release-member change is added | Specification §2.1 non-goals, §4; PF14 §1.1 |

### 8.3 Specification ambiguity or scope change

None that needs the Specification's owners. FND-005 is outside this change, and FND-006 and FND-007 are observations. None changes an approved requirement.

## 9. Findings → Doc Delta Map (Change Process Guide §2.2)

* **Audit Summary.** The loader is a non-release, unreached module whose supported path needs no acquisition, so the boundary correction is three small work units with no Ops and no live proof attached.
* **Drift theme.** "operational code inside Engine chart validation".
* **Count of findings:** 7.
* **Count of Must-act-now findings:** 4 (FND-001 to FND-004, all within the approved scope).
* **PF homes consulted:** HDE Architecture, HDE Mechanics Guide, HDE Build Checklist — Separation, HDE Governance.
* **PF homes receiving proposals:** HDE Architecture, HDE Mechanics Guide, HDE Build Checklist — Separation (post-delivery drainage only).
* **PF09 task delta proposed:** none.
* **PF-canon doc delta proposed:** drainage after delivery (DELTA-001, DELTA-002).

**FND-001**

* Finding: Engine chart code reads the environment and the clocks, synthesizes a random correlation id and writes a log file.
* Audit anchor: `return str(_os.getenv("SAFE_MODE", "0")).strip() == "1"`.
* Audit evidence pointer: `engine/charts/loader.py` (O-02).
* Epic Specification linkage: R-01 and R-02.
* Epic Specification anchor: "Environment and SAFE_MODE/rails evaluation, provider selection, chart acquisition, wall and performance clocks, correlation context, operational logging and filesystem writes belong to one supported Adapter-owned orchestration entry."
* Must-act-now: YES.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: YES, post-delivery.
  * PF02 architecture delta: YES, post-delivery.
  * Other PF canon delta(s): None.
  * PF20 historical correction: NO.
* Why these are the correct homes: HDE Architecture §1.1 and HDE Mechanics Guide §1.1 hold the drift classification that delivery retires.

**FND-002**

* Finding: The legacy signature fails for every resolvable provider and carries fallback data.
* Audit anchor: `res = provider.get_chart(user_id, correlation_id=correlation_id)`.
* Audit evidence pointer: `engine/charts/loader.py:81` (O-04, X-2).
* Epic Specification linkage: R-03, D-1.
* Epic Specification anchor: "The old operational Engine path is removed, or only a genuinely pure compatibility surface is kept where its owning contract permits it."
* Must-act-now: YES.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): None.
  * PF20 historical correction: NO.
* Why these are the correct homes: PF09.3 already records the defect and its owner.

**FND-003**

* Finding: Committed runs mutated the tracked loader log three times.
* Audit anchor: `c6fdc913 2026-05-01 HDE-EPIC030 QA PASS 2` (+4 lines).
* Audit evidence pointer: `artifacts/logs/loader_call.jsonl` (O-08).
* Epic Specification linkage: AC-05.
* Epic Specification anchor: "running the covering tests leaves tracked files unchanged".
* Must-act-now: YES.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): None.
  * PF20 historical correction: NO.
* Why these are the correct homes: the outcome is already canon-required; this is implementation.

**FND-004**

* Finding: No CI owner mapping exists for the paths this change must touch.
* Audit anchor: `CI_PRODUCT_OWNER_TEST_MISSING:engine/charts/loader.py`.
* Audit evidence pointer: `ci/checks/classify_ci_changes.py` (O-13).
* Epic Specification linkage: R-04.
* Epic Specification anchor: "Meaningful automated checks …".
* Must-act-now: YES.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): None.
  * PF20 historical correction: NO.
* Why these are the correct homes: repository CI tooling, delivered in the PRs.

**FND-005**

* Finding: The canon-named compat-determinism generator cannot run on `main`: it exits 2 at `compat_public not implemented`, after `cd6f9e6c` removed `compat_public`.
* Audit anchor: `compat_public not implemented`.
* Audit evidence pointer: `scripts/make_compat_determinism_artifacts.py` (O-11, X-4).
* Epic Specification linkage: it does not create new planned runnable work. R-03 migrates the script and preserves its current behavior; restoring its function is outside HDE-SEPA006.
* Epic Specification anchor: N/A.
* Must-act-now: NO.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): HDE Governance (GATE:CORE-DET, D.1, D.3 name a script that cannot complete), as a candidate only.
  * PF20 historical correction: NO.
* Why these are the correct homes: HDE Governance names the script as a recompute and byte-compare gate.
* Routing: the CL-40 scan candidate list, and the Product Owner.

**FND-006**

* Finding: `engine/util/input_validators.py` reads pinned lists relative to CWD for its other caller as well.
* Audit anchor: `_ISO_PATH = Path("artifacts/constants/iso_3166_1_alpha2.json")`.
* Audit evidence pointer: O-06, O-17.
* Epic Specification linkage: not in scope (ED-08).
* Epic Specification anchor: N/A.
* Must-act-now: NO.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): None.
  * PF20 historical correction: NO.
* Why these are the correct homes: it is an implementation defect in a non-chart caller. CL-40 candidate.

**FND-007**

* Finding: The architecture snapshot is stale on `main`, and CI does not check it for currency.
* Audit anchor: `STALE:artifacts/architecture/architecture_snapshot.keys_only.json`.
* Audit evidence pointer: O-14, X-5.
* Epic Specification linkage: none (ED-09).
* Epic Specification anchor: N/A.
* Must-act-now: NO.
* Doc deltas required:
  * PF09 task delta: NO.
  * PF14 mechanics delta: NO.
  * PF02 architecture delta: NO.
  * Other PF canon delta(s): HDE Schemas and Artifacts (whether this snapshot is a frozen family or a current one), as a candidate only.
  * PF20 historical correction: NO.
* Why these are the correct homes: HDE Schemas and Artifacts owns evidence-family currency. CL-40 candidate.

**Doc Delta Proposals — PF09 (Tasks).** None.

**Doc Delta Proposals — PF canon.**

* **DELTA-001.**
  * Target doc: HDE Architecture.
  * Target section: §1.1 "Non-BodyGraph chart loader classification".
  * Delta: after delivery and acceptance, replace "remains current repository reality until separately remediated" with the delivered boundary.
  * Why: the classification describes a module this change removes.
  * Evidence pointers: WU-PR-02 merge; QA.
  * PF proof excerpt: "The checked-in loader remains current repository reality until separately remediated".
* **DELTA-002.**
  * Target doc: HDE Mechanics Guide.
  * Target section: §1.1 "BodyGraph and loader seam posture".
  * Delta: the same, after acceptance.
  * Why: the same.
  * Evidence pointers: the same.
  * PF proof excerpt: "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift".

Drainage is Product Owner canon work, not this change's implementation.

**Open Questions for PO.** None remaining (Q-01 answered).

## 10. Change Process Guide §2.2 audit output fields

```yaml
audit:
  serializer_path: "not_applicable"
  duplicates: []
  det_serializer_ok: "not_applicable"
  idempotence_ok: "not_applicable"
  a7_proof_surface_exists: "not_applicable"
  a7_vary_auth_ae_ok: "not_applicable"
  a7_head_parity_ok: "not_applicable"
  a7_304_omits_ct_cl_ok: "not_applicable"
  a7_encoding_invariance_ok: "not_applicable"
  endpoints_catalog_file_ready: "not_applicable"
  composite_proof_json_ready: "not_applicable"
  env_gate_proof_ready: "not_applicable"
  writers_errors_semantics_ok: "not_applicable"
  refusal_proof_ready: "not_applicable"
  logs_keys_only_ok: "true"
  governed_locations_ok: "true"
  dev_db_bridge_fallback_ready: "not_applicable"
  dev_connectivity_snapshot_ready: "not_applicable"
  human_index_wired: "true"
  human_index_hash_ready: "true"
  machine_mirror_wired: "true"
  mirror_schema_ok: "unassessed"
  path_proofs_ok: "unassessed"
  missing_components:
    - "Adapter-owned chart orchestration entry (R-01)"
    - "Pure Engine chart validation and normalization interface (R-02)"
    - "CI owner mappings for changed chart paths (FND-004)"
  proposed_fixes:
    - "WU-PR-01 and WU-PR-02 of the Implementation Plan"
  blockers: []
```

Grounds for `not_applicable`:

* The change touches no public serializer path, no public JSON or A7 transport, no Endpoint Catalog entry, no writer or error HTTP semantics, no rails-refusal HTTP proof and no database transport (§4, ED-10).
* `logs_keys_only_ok` is `true` because the current log line is keys-only (O-02; `tests/loader/test_loader_logs_keys_only.py` passes, X-1), and ED-04 keeps it.
* The three index fields are `true` because the Human Index, its hash sentinel and the Machine Mirror exist on `main`.
* `mirror_schema_ok` and `path_proofs_ok` were not run in this Audit. They bind only if a PR changes governed evidence.

## 11. TypeSafe reading, surface advice and recovery state

* **TypeSafe reading.** This Audit hands off to no session by itself. The reading for the receiving IA-30 session is in the Plan, §15.
* **RECOVERY_ENVELOPE.**
  * Paused prompt: none.
  * Phase 1: complete.
  * Phase 2: the Plan, `docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md`.
  * Question state: Q-01 answered.
  * Remaining work: none in this Audit.
  * Same-author return: this IA.
  * Prerequisites: none outstanding.

## 12. Nonclaims

This Audit claims no implementation, CI result, QA verdict, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum, deployment or closure. Local runs X-1 to X-6 are observations, not governed evidence. It edits no approved artifact and no file outside `docs/ephemeral/`.
