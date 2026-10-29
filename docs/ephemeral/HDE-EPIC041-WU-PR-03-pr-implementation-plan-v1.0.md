---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC041-WU-PR-03-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
approval_hold: "ASK OK? — PR IMPLEMENTATION PLAN"
predecessor: none (first plan for WU-PR-03)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-03
DOCUMENTATION_UNIT_ID: WU-PR-03
work_unit_title: "WU-PR-03 — Final repository documentation (GCF-19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; 38,337 bytes; git blob 88519d1658ec14c9d69e212ccf7774a7f5169f16; merged by amthorn78/glow-hdengine-v2#798 as 9ff76b53)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; 37,557 bytes; git blob 2ff65a377ae392396b32707313399fab3bf154e9)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; git blob 2ca19d33c1098fde7f606e2a09ee9e884f1ba7f3)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md, CF-E-30 INITIAL_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; git blob 9decb6085a64a9d0c2b7b8919e97ef3627a2846a; corrected for later stages by AUD-CORR-1 in the WU-PR-01 lineage review)
DEPENDENCY_REFS:
  - docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-01, amthorn78/glow-hdengine-v2#791; git blob 20e9d51c481db2485163a12d2cb3193d86348501)
  - docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-02, amthorn78/glow-hdengine-v2#796; git blob 2d93a6fd866e4daccedcb6d03c866f16fd3e9e35)
REMEDIATION_REVIEW_ID: none (no remediation lineage)
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
immutable_approved_base: Specification v1.1 (Thoth, CF-E-30 review v1.1) → Implementation Plan v1.1 (Isis, IA-30 review v1.1)
effective_baseline: "approved base + applicable PF10 overlays (HDE Build Notes addenda 2.2, 2.3 and 2.4 for their scope)"
pf10_path: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md (741 lines, 102,755 bytes, sha256 6fa054b1e51cf76fd795e460cec039a51caf99cec16fe1521f0a00febff15f3c; the only PF10 file on main at 9ff76b53; read in this session: front matter, addenda 2.2, 2.3 and 2.4 in full; provenance, not a gate)
pf10_addenda_applicable: "addendum 2.2 'Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close' (R-1 and R-2 bound what the documentation may cite; R-3 not engaged); addendum 2.3 (WU-PR-01 record); addendum 2.4 (WU-PR-02 record; its deferred-obligations table names DELTA-001, DELTA-002, SWEEP-1 and the 2.2 bearing for this unit). All three are sections of the one file above; no separate addendum file exists. Addendum 2.1 (S19) is not engaged"
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff (see §12)
repository_baseline: origin/main 9ff76b53662e00c7df5efecb056d3777d3fdae30 (#798). `git diff --stat 4fcb3c76 9ff76b53` is the one instruction file under docs/ephemeral/, so every byte outside docs/ephemeral/ and docs/pfcanon/ equals the WU-PR-02 squash 9843934f
working_branch: claude/hde-epic041-wu-pr-03-savt6d (this plan's documents only)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_01Q789tzy6y65nrdG8GrR5hb (the dedicated WU-PR-03 PR engineering session Nathan created; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9; page state 2026-10-27T13:18:23.839Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1 (carried from the instruction; the PR-20 page sits under "HDE IA — GCFPE-20261027.1 — 102726.1"; the GCFPE register was not re-read in this session)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; no new entry (§18)
created_at: 2026-10-29 (UTC)
GCFPE_PROMPT_USES: see §21
---

# HDE-EPIC041 WU-PR-03 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED for v1.0.** This is the complete plan for WU-PR-03 within the instruction's scope. The unit changes three Markdown files and no code:

* `CHANGELOG.md`: one new "Unreleased — HDE-EPIC041" section (+18 lines).
* `ARCHITECTURE.md`: two bullets that give the delivered chart modules their single homes (+2 lines). This is the instruction's candidate **C-A: change**.
* `AGENTS.md`: one short "HDE-EPIC041 current posture" section (+6 lines). This is candidate **C-C: add**.
* `docs/INDEX.md` (candidate **C-B**): **no change**.

The plan fixes the exact text. A prototype ran in a throwaway clone (§12):

* the three-file diff is 26 added lines and applies cleanly to `9ff76b53`; applying it to a clean checkout gives tree `0487f5c44c37…`, the prototype head's tree;
* the classifier, as `ci.yml` calls it, returns `reason=documentation_only` with no lanes and no changed-test target;
* `check_agents_md_citations.py` returns `AGENTS_MD_CITATIONS_OK`; `check_direct_db_contract.py` returns `DIRECT_DB_CONTRACT_OK`;
* the pre-push check reports every path `not-member` and the admitted release unchanged (`1.3.0`, 45 members, `release_id` 77204764…);
* the local replay of the `test` job passes, ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` and leaves the clone clean;
* every statement the new text makes was checked against the code at the baseline (§7).

PR-30 applies the companion diff, re-runs §11 and publishes one PR.

**One judgment call is Nathan's to see before the Proceed.** C-C adds text to `AGENTS.md`, a file every agent reads. §5 PD-3 gives the basis and the exact text. If Nathan does not want it, the plan is revised to a v1.1 without it; the Proceed for v1.0 approves it.

This plan authorizes nothing. Only the Product Owner's `PR Implementation Proceed` (PR-30) for exactly v1.0 authorizes implementation, and only the Product Owner merges.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Lineage and sources read in this session

* **Instruction v1.0**, read in full at `9ff76b53` (blob 88519d16…, the blob #798 landed).
* **PR-20 prompt** (Notion, page state 2026-10-27T13:18:23.839Z), read in full. The PR-30 page was located by search (`https://app.notion.com/p/4064590a05eb8157bcb9c79a43cefb08`) and **not read in this session**; PR-30's own contract is its session's to read.
* **Implementation Plan v1.1**: §6 WU-PR-03 (business case, scope, dependency, acceptance; file lines 272 to 292), §7 traceability and §8 DL-03 (file line 353), checked against the instruction's quotations. **IA-30 review v1.1**: the WU-PR-03 business-case row ("Passes"). **Implementation Audit v1.0**: O-20, FND-005 to FND-007, DELTA-001 and DELTA-002. **Specification v1.1**: TI-03 (the gap statement the sweep serves). Each was checked for the facts this plan relies on; the instruction holds the rest of their lineage.
* **WU-PR-02 plan v1.0**, read in full as the format and obligations pattern (PR-30/PR-35 split, CI economy, result record).
* **HDE Build Notes** (PF10): addenda 2.2, 2.3 and 2.4 in full (§2.4's deferred-obligations table is the source of DELTA-001, DELTA-002, SWEEP-1 and the 2.2 bearing).
* **Canon text re-read for the DELTA notes:** HDE Architecture §1.1 "Non-BodyGraph chart loader classification" (quoted sentence found verbatim: "The checked-in loader remains current repository reality until separately remediated"); HDE Mechanics Guide §1.1 "BodyGraph and loader seam posture" (quoted sentence found verbatim: "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift"). Change Process Guide §3.5.3 "Repo docs sweep (major epics)" and the line 3300 rule ("MUST prove non-obvious claims before documenting them").
* **Skills:** the TypeSafe scoring skill (request v8.2) for §20; `glow-write-boundary` and `glow-workspace-currency` for where this plan lands.
* **Code and documents read at `9ff76b53`:** `adapter/chart_orchestration.py` (113 lines), `engine/charts/pure.py` (101 lines), `git ls-tree origin/main engine/charts/`, `scripts/make_compat_determinism_artifacts.py`, `tests/retired_tests.md`, the four test files under `tests/charts/`, `tests/adapter/test_chart_orchestration.py` and `tests/scripts/test_make_compat_determinism_artifacts.py` (names and docstrings; run, §12.4), `engine/util/input_validators.py`, `ci/checks/classify_ci_changes.py` (`_HISTORICAL_PREFIXES`), `.github/workflows/ci.yml` (triggers, step conditions, final step), `ci/checks/check_agents_md_citations.py` (contract), `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/INDEX.md`, `CHANGELOG.md` (top), `.github/pull_request_template.md`.

## 3. Business case (as the PR Instruction states it; the Proceed is given against it)

* **Beneficiary:** the delivery team and the QA lane.
* **Evidence:**
  * HDE-EPIC040's QA Step-0B doc-delta record (`audit/docdeltas/hde-epic040_doc_deltas.md`, DD-05, DD-10, DD-11) found repository documentation that contradicted code, and QA had to carry it as caveats.
  * O-11 shows canon-named tooling that had silently stopped working for five weeks.
* **Benefit:** QA-10 and later sessions read a repository record that matches the delivered boundary, so they do not plan against a removed module.
* **Measure:**
  1. A `CHANGELOG.md` "Unreleased — HDE-EPIC041" section names WU-PR-01 and WU-PR-02 and their nonclaims (O-20 convention).
  2. A `git grep` sweep at the PR head finds no live repository document outside `docs/pfcanon/`, `docs/ephemeral/` and the historical prefixes describing `engine/charts/loader.py` as current.
* **Stop rule** (HDE Governance §9.7.7): "A work unit whose business case is met stops; further work on it needs a new business case."

Measure 2 already holds at the baseline. Measure 1 maps to §11 items 1 and 7, measure 2 to item 3.

## 4. Baseline re-check (instruction §3.1, at `9ff76b53`)

Each fact was re-read in the code, not taken from the instruction.

| ID | Re-verified at `9ff76b53` | Proof |
| :- | :- | :- |
| F-1 | **Holds.** Two call forms; any other shape raises `TypeError("Invalid arguments to load_chart")` | `adapter/chart_orchestration.py:70` (signature), `:72-75` (docstring), `:86`, `:90`, `:92` (the raises). Probe: `load_chart('U1')` and `load_chart(42)` both raise `TypeError: Invalid arguments to load_chart` |
| F-2 | **Holds.** `SAFE_MODE` read at `:79`; correlation id `:80`; clocks `:104` and `:109`; pinned lists anchored at `_ROOT` (`:24-25`); fixture chart `:47`; one line per call in the `finally` block with the eight keys (`:104-111`); `route` is `loader.load_chart` (`:105`), `provider` is `fixtures` (`:106`); sink or module logger (`:62`, `:64`) | The file; `tests/adapter/test_chart_orchestration.py::test_default_sink_is_the_module_logger_and_writes_no_file`, `::test_log_line_is_keys_only` (run, §12.4) |
| F-3 | **Holds.** `validate_birth_inputs` (`pure.py:61`), `normalize_chart` (`:91`), `ChartInputError` (`:16`) with code `READER_INVALID_INPUT` and `details.field` (`:32-33`); it also defines the `BirthInputs` return type (`:24`) | The file; `tests/charts/test_chart_pure_purity.py::test_fresh_import_and_calls_have_no_external_side_effects` (run) |
| F-4 | **Holds.** `git ls-tree origin/main engine/charts/` lists only `pure.py` (blob 6b7d10ca…) | The command |
| F-5 | **Holds.** The guard's docstring and tests (`test_no_tracked_python_file_imports_the_retired_loader`, `test_the_retired_module_path_does_not_exist`, two checker self-tests) | The file; 4 tests run |
| F-6 | **Holds.** Line 9 imports the entry; line 18-19 exits 2 with `compat_public not implemented`. From a new temporary directory under `env -i`: exit 2, stdout empty, directory empty | The script; the probe; `tests/scripts/test_make_compat_determinism_artifacts.py` (1 test, run) |
| F-7 | **Holds.** `git grep loader_call` over `*.py *.sh *.yml *.yaml` finds writers only under `.audit_src/` (a historical prefix). The tracked `artifacts/logs/loader_call.jsonl` has blob 92556952…, last changed by `c6fdc913` (2026-05-01), before this Epic (#791 landed 2026-10-28) | The commands |
| F-8 | **Holds.** `tests/retired_tests.md` line 8 names the characterization file and `tests/adapter/test_chart_orchestration.py` as replacing coverage | The file |
| F-9 | **Holds.** `prepush_check.py membership` for the three paths: `not-member`; admitted release `1.3.0`, roster 45, `release_id` 77204764c225…; `artifacts/compat/AB.json` and `identity_hash.txt` blobs 7fe71f99… and 7e6176a2…, as the WU-PR-02 review recorded | §12.2 |

| Other baseline fact | At `9ff76b53` |
| :- | :- |
| Code and documentation outside `docs/ephemeral/`, `docs/pfcanon/` | Equal to `4fcb3c76` and to the WU-PR-02 squash `9843934f` |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md`, the only PF10 file; `prepush_check.py build-notes` PASS with the sha256 in the front matter |
| SWEEP-1 (instruction §3.3 pattern, in scope) | **No match.** `git grep -n -I -E '<pattern>' HEAD -- README.md AGENTS.md ARCHITECTURE.md CHANGELOG.md docs ':(exclude)docs/pfcanon' ':(exclude)docs/ephemeral'` finds nothing. A wider search (`tests/loader`, `chart loader`, `chart_loader`, `loader.load_chart`, `compat_determinism`, `characterization`, `provider/decision.txt`, `FixturesProvider`, `resolve_provider`, the word `loader`) finds only two unrelated "registry report's loader" sentences (`AGENTS.md:154`, `docs/adr/hde/release_attestation_scaling_adr.md:22`) |
| README mentions of `artifacts/compat/identity_hash.txt` (`README.md:110`, `:230`) | Not made stale by this Epic: they describe a captured and test-verified artifact, not the generator. The generator broke earlier (FND-005, `cd6f9e6c`). **Left as is** |
| Hosted workflow | `.github/workflows/ci.yml` `on.pull_request.paths` excludes only the eight `docs/` prefixes; `CHANGELOG.md`, `ARCHITECTURE.md` and `AGENTS.md` are not excluded, so the `test` job **starts** on this PR (§11 note; OBS-9) |

## 5. Design decisions (the choices the instruction leaves to PR-20)

| ID | Decision | Basis |
| :- | :- | :- |
| PD-1 | **CHANGELOG section** in the file's convention, directly below `# CHANGELOG` and above the HDE-CRD-0002 section. Heading `Unreleased — HDE-EPIC041: chart-loader boundary separation, final repository documentation (WU-PR-03)`; `### Added` (3 bullets), `### Changed / Fixed` (9 bullets). No earlier section is edited. | Instruction §3.2; Audit O-20; the HDE-CRD-0002 and HDE-EPIC040 sections are the pattern |
| PD-2 | **C-A: change `ARCHITECTURE.md`**, two additive bullets: "Charts (pure)" under `engine/` and "Chart orchestration" under `adapter/`. The `adapter/` heading line ("dev runner & route registration (the only app home)") stays. "Architecture capture (every epic)" is not touched. | Decision rule (instruction §3.3): change it if a reader would otherwise place chart operational concerns in `engine/` or miss the entry. The file calls itself "the authoritative map of the HD Engine repo" and lists each Engine single home (compat, validation, emission, serialization, errors, HTTP handlers) with none for charts; the removed loader was an I/O-bearing module in `engine/`. A reader using the map to place chart code had no home to find. Only F-1 to F-4 facts are added. The change is incomplete-statement repair, not a restructuring. |
| PD-3 | **C-C: add one `AGENTS.md` section** "HDE-EPIC041 current posture (chart-loader separation)", inserted before the HDE-EPIC040 section (the file orders newest first). Four bullets: the chart path and what not to do; the rule for stale loader wording; the generator's state; nonclaims. | Decision rule: add only if an agent would otherwise act wrongly. The real case: HDE Architecture §1.1 says "The checked-in loader remains current repository reality until separately remediated", HDE Mechanics Guide §1.1 describes the module as drift to be remediated, and drainage waits until after QA. AGENTS.md's canon-first rule sends every agent to that text first. A QA-10, documentation or implementation agent can therefore report the missing module as a regression or recreate it. The guard tests fail such a return only after a push. Also real: the canon-named generator exits 2 (F-6), and the logged `route` string `loader.load_chart` (F-2) invites the same mistake. The text states repository facts and routes the drift to the canon owner. It edits and cites no canon. |
| PD-4 | **C-B: no change to `docs/INDEX.md`.** | Decision rule: change the heading only if it would mislead a reader about current state. "HDE-EPIC040 current" heads orientation for the Reader, the core and the configuration, which HDE-EPIC041 does not change (F-9). HDE-CRD-0002 landed after HDE-EPIC040 without changing it. The INDEX "Local map" line "ARCHITECTURE.md — entrypoints and providers" stays accurate. A pointer to the CHANGELOG section would add a second place to keep in sync for no new fact. |
| PD-5 | **README.md: no change.** No statement in it names the loader, the entry or the generator (§4). | Instruction §3.3: change only a statement the delivered boundary makes stale or incomplete. |
| PD-6 | **No command block is added** to any document. | Instruction §3.5. Item 8 of §11 therefore records "none added". |
| PD-7 | **The CHANGELOG cites merged PRs and repository paths, PF-Canon by no name, and no planning document by path.** Decision identifiers D-1 and FND-005 to FND-007 are not written; the text says "by Product Owner decision" and states each not-delivered item in words. | HDE Build Notes addendum 2.2, R-1 and R-2; instruction §3.5. A permanent record must stay valid when `docs/ephemeral/` is archived. |
| PD-8 | **The "Not delivered" bullet is limited to what the code shows**: the generator's compat computation, the `input_validators` working-directory reads and `TZ` read, and the architecture snapshot that still names the loader. | Instruction §3.2. Proof in §7. The snapshot is under `artifacts/architecture/`, a historical prefix, so it is named as not regenerated, not as a live document. |
| PD-9 | **DELTA-001 and DELTA-002 go in the PR description only** (§13.4). | Instruction §3.4; HDE Governance planning-artifact rules; no canon file, `audit/docdeltas/` or governed surface is written. |
| PD-10 | **The PR description carries a sweep record**: the search, the head SHA and a disposition per match. At the planned head every match is a sentence in `CHANGELOG.md`, `ARCHITECTURE.md` or `AGENTS.md` that states the module is removed or names the new entry (§12.3). | Instruction §3.3, §6 item 3, PR-40 re-run. |

## 6. Files and components, with each component's real inputs (PR-20 Execute step 3)

| Path | Change | Component | Real inputs | Outside the real set: the one refusal or stated limit |
| :- | :- | :- | :- | :- |
| `CHANGELOG.md` | +18 lines, one new section at the top | Release-history record | F-1 to F-9 at the PR head; merged PR numbers #791 and #796 | A planning document as a dependency (R-1) and a PF file name, version or digest (R-2) are refused: none is written. A fact the code does not show is left out (PD-8) |
| `ARCHITECTURE.md` | +2 lines | Single-homes map | The current text of the file; F-1 to F-4 | Claims about later units, QA, release or closure: none written. "Architecture capture (every epic)" is a close-time step and is not done here (§17 OBS-D1) |
| `AGENTS.md` | +6 lines (heading, four bullets, blank line) | Agent posture | The current text; F-1 to F-9; the citation checker's contract | No PF document other than HDE Build Notes is named, and HDE Build Notes is not named at all; the checker enforces this |
| `docs/INDEX.md`, `README.md` | none | — | — | — |
| PR description | not a repository file | Why / What changed / Checks run / Not in this PR / What merging does; sweep record; DELTA-001 and DELTA-002 | §6 (this table), §11, §12, §13.4 | No canon edit, no governed-surface write |

**Not changed** (instruction §5): any code, test, script, schema, workflow, CI check or classifier file; `pytest.ini`, `catalog/`, `engine/config/registry_loader.py`; `docs/pfcanon/`; `audit/`, `artifacts/`, `docs/evidence/`, `docs/ENDPOINTS_CATALOG.json` and every governed or frozen artifact; `tests/retired_tests.md`; earlier CHANGELOG sections; the `audit/HDE-CRD-0002_close_report.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md` records that name HDE-SEPA006.

## 7. Exact text and claim proof

The exact new text is the companion diff (§12.1), 60 lines. Every non-obvious claim in it has a proof here (instruction §3.5, Change Process Guide §3.5.3). "Run" means a run in this session (§12); "read" means code read at `9ff76b53`.

| Document and statement | Proof |
| :- | :- |
| CHANGELOG: `load_chart(birthdate, birthtime, place, *, tz=None, correlation_id=None, log_sink=None)` or the three birth arguments by keyword | F-1; `chart_orchestration.py:72-73` |
| CHANGELOG: owns the `SAFE_MODE` read for its log field, both clocks, the correlation id, the pinned-list reads anchored at the repository root, the fixture chart and one keys-only line per call | F-2; `:79-80`, `:24-25`, `:47`, `:104-113`; `test_log_line_is_keys_only`, `test_validation_does_not_depend_on_the_working_directory` (run) |
| CHANGELOG: eight keys; `route` is `loader.load_chart`; `provider` is `fixtures` | `:104-111` |
| CHANGELOG: line goes to `log_sink` when given, module logger otherwise; registers no route, writes no file | `:60-64`; `test_default_sink_is_the_module_logger_and_writes_no_file` (run) |
| CHANGELOG: `validate_birth_inputs(...)`, `normalize_chart(obj)`, `ChartInputError`, code, `details.field` values | `pure.py:16`, `:32-33`, `:61`, `:91`; the `field` values are `date`, `time`, `place`, `tz` (`pure.py` `_invalid` calls at `:74`, `:78`, `:80`, `:83`, `:85`, `:87`) |
| CHANGELOG: no time, randomness, environment, network, provider, logging or filesystem access, at import or in a call | The module docstring; `test_fresh_import_and_calls_have_no_external_side_effects` and `test_pure_module_has_no_forbidden_dependency_or_call` (run) |
| CHANGELOG: the five test files and what they do | Names and docstrings read; run (§12.4: 48 passed, tests/charts, tests/adapter/test_chart_orchestration.py, the generator test and tests/loader) |
| CHANGELOG: guard fails on an import, a `_call_legacy` reference or the module path | Guard docstring and tests; the WU-PR-02 lineage review recorded planted-importer probes at `9843934f` (not re-run here; the guard tests pass, §12.4) |
| CHANGELOG: `engine/charts/loader.py` removed; `engine/charts/` holds only `pure.py` | F-4; `git ls-tree` |
| CHANGELOG: legacy shapes such as `load_chart(user_id)` raise `TypeError("Invalid arguments to load_chart")` | F-1 probe; `test_other_argument_shapes_raise_type_error_and_log_one_error_line` (run) |
| CHANGELOG: the generator imports the entry; exit 2 with `compat_public not implemented`; writes nothing | F-6 probe and test |
| CHANGELOG: characterization test retired with a row naming `tests/adapter/test_chart_orchestration.py` | F-8 |
| CHANGELOG: no supported run writes `loader_call.jsonl`; tracked file unchanged | F-7 |
| CHANGELOG: nothing public changed; release `1.3.0`, 45 members, `release_id` 77204764c225…c51e | F-9; `prepush_check.py membership` (run) |
| CHANGELOG: `input_validators` reads its pinned lists relative to the working directory | `engine/util/input_validators.py:12-13` (`Path("artifacts/constants/...")`), `:46`, `:54` |
| CHANGELOG: its date parser still reads `TZ` | Probe: with `time.tzset` counted, the first `parse_date_yyyy_mm_dd("1990-05-04")` call makes 1 call (the function is outside the chart path's use; the claim is about the module) |
| CHANGELOG: the architecture snapshot is not regenerated and still names `engine/charts/loader.py` | `artifacts/architecture/architecture_snapshot.keys_only.json` contains the string once; last changed 2026-08-02 (`dbd7487d`) |
| ARCHITECTURE: pure module contents and purity; pinned lists arrive as arguments | F-3; `validate_birth_inputs(..., *, iso_codes, iana_zones)` |
| ARCHITECTURE: entry owns the listed concerns, registers no route, writes no file | F-2 |
| AGENTS: entry, pure module, removed loader and signature, no shim | F-1, F-3, F-4 |
| AGENTS: the logged route string is a label, not a module | `chart_orchestration.py:105`; no module of that name exists (F-4) |
| AGENTS: the guard fails if the module path or an import of it returns; the purity test fails on a forbidden dependency or side effect | Guard docstring and test names; purity test names (run) |
| AGENTS: generator imports the entry and still exits 2 before its chart call | F-6 |

**Not verified, therefore not written:** the post-merge `main` push run on `9843934f` (run 40777435776) is recorded by the instruction as `success`; this plan does not repeat it as a fact about the documentation.

## 8. Requirement-to-documentation map (PR-20 Execute step 4)

| Approved requirement / obligation | Change | Validation |
| :- | :- | :- |
| R-01 / AC-01: one Adapter-owned orchestration entry | CHANGELOG "Added" bullet 1; ARCHITECTURE adapter bullet | §7 rows for F-1, F-2; §11 item 7 |
| R-02 / AC-02: pure Engine chart interface | CHANGELOG "Added" bullet 2; ARCHITECTURE engine bullet | §7 rows for F-3 |
| R-03 / AC-03: callers migrated; legacy path removed | CHANGELOG "Changed / Fixed" bullets 1 to 4 | F-4, F-6, F-8 proofs |
| R-04 / AC-04: automated boundary checks | CHANGELOG "Added" bullet 3 | The test files exist at the head (§11 item 7) |
| AC-05: outputs preserved, no fallback, clean tree | CHANGELOG bullets 5 and 6 | `prepush_check.py membership`; compat blobs unchanged |
| Plan v1.1 WU-PR-03 measure 1 | CHANGELOG section | §11 items 1 and 7 |
| Plan v1.1 WU-PR-03 measure 2; Specification TI-03 | Sweep record (PD-10) | §11 item 3; PR-40 re-runs it |
| Plan v1.1 scope: AGENTS.md line only if a reader needs it | PD-3 | Citation check (§11 item 4); PD-3 basis |
| Addendum 2.4 deferred obligations (DELTA-001, DELTA-002, SWEEP-1, 2.2 bearing) | PD-7, PD-9, PD-10 | §13.4; citation rules |
| Instruction §3.5 (ground claims; no canon edit; no code change) | §7; §6 "Not changed" | §11 items 1, 7 |

## 9. Implementation sequence for PR-30

1. **Recover before creating.** Inspect the session's checkout, branches, worktrees, open PRs and `docs/ephemeral/` for WU-PR-03 work. Expected: the instruction, this plan, its diff and this plan's documents PR.
2. **Branch** from current `origin/main` on the session's designated branch, after `git fetch --unshallow` if the clone is shallow (OBS-5). Re-run §4 for the three target files and F-1 to F-9 if `main` moved past `9ff76b53` outside `docs/ephemeral/`; record any difference. A change to `CHANGELOG.md`, `ARCHITECTURE.md` or `AGENTS.md`, or to the code F-1 to F-9 cite, is reconciled before applying.
3. **Apply** `docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff` (`git apply --check`, then `git apply`). A hunk that fails (`CHANGELOG.md` and `AGENTS.md` are the files most likely to move) is applied by hand to the same effect and recorded under *In-flight decisions*.
4. **Local checks**, §11 items 1 to 9, under `env -i` closed rails.
5. **Commit once:** `docs: HDE-EPIC041 final repository documentation (WU-PR-03)`.
6. **Publish** one PR. Description: the `.github/pull_request_template.md` headings with the AGENTS.md content rules (§13.4 has the content).
7. **Result record** `docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-implementation-result-v1.0.md` (`PR_IMPLEMENTATION_RESULT`): `PR_CANDIDATE_PUBLISHED`, tested-source SHA, the checks record, *In-flight decisions*, `PR_REMOTE_ACTION_LEDGER`, nonclaims. Hand off to PR-35 in its own session.

**Integration seams:** none in code. The documents cite code paths; the sweep and the claim proof are the seam. **Order inside the commit:** one commit; no ordering constraint among the three files.

## 10. PR split and merge dependencies

* **One PR**, one coherent change; reversible by revert, which restores the three files.
* **Before it:** this plan's documents PR merged (it carries the companion diff PR-30 applies). WU-PR-01 (#791) and WU-PR-02 (#796) are merged and accepted (§4; the lineage reviews).
* **Before its merge:** PR-35's `MERGE_PENDING`; Nathan merges.
* **After it:** PR-40 lineage review; then DOC-20 completion verification; then QA-10 (instruction §10).
* **No release member changes** (§4), so no manifest refresh and no evidence regeneration. No merge-order dependency among HDE-EPIC041 PRs remains.

## 11. Validation PR-30 runs (PR-35 re-runs items 1 to 6 after any correction)

**Environment.** `env -i` with `HOME`, a `PATH` that includes `/usr/local/bin`, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and `PYTHONPATH=<checkout>`. The container exports database, vendor and GitHub credentials; without `env -i` they reach the tools (OBS-2). Record environment probes as SET/UNSET only. Items 2 to 6 and 9 need only `git` and a CPython (this plan's runs used 3.13.17; CI uses 3.12). The classifier needs full 40-character SHAs, so use `git rev-parse`. No pytest install is needed for this unit's required checks.

1. **Docs-only scope.** `git diff --name-status <base>..HEAD` lists only `CHANGELOG.md`, `ARCHITECTURE.md` and `AGENTS.md` (plus, for the PR as published, the `docs/ephemeral/` result records). Expected: `M` for each of the three.
2. **Classifier, as `ci.yml` calls it.** `python3 ci/checks/classify_ci_changes.py --base <base SHA> --head <head SHA> --event-name pull_request --github-output <tmp> --changed-tests-output <tmp>` → exit 0, `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=3;lanes=none`, every lane `false`, `needs_python=false`, `changed_tests=false`, the changed-tests file empty. Record the actual output. (With the `docs/ephemeral/` result records in the diff, `paths` reflects only paths the classifier counts; record what it prints.)
3. **Sweep at the head.** `git grep -n -I -E 'engine\.charts|engine/charts|charts\.loader|load_chart\b|loader_call|LoaderInputError|_call_legacy|chart_orchestration|make_compat_determinism_artifacts' <head> -- README.md AGENTS.md ARCHITECTURE.md CHANGELOG.md docs ':(exclude)docs/pfcanon' ':(exclude)docs/ephemeral'` with a disposition per match. Expected: matches only in the three changed files, each a sentence that says the module is removed or names the new entry (§12.3 lists them); no file describes `engine/charts/loader.py` as current.
4. **AGENTS.md citations.** `python3 ci/checks/check_agents_md_citations.py` → `AGENTS_MD_CITATIONS_OK`, exit 0.
5. **Direct-DB contract scan.** `python3 ci/checks/check_direct_db_contract.py` → `DIRECT_DB_CONTRACT_OK`, exit 0. It scans active repository prose; the `db` lane is not selected for a documentation-only change.
6. **Membership and HDE Build Notes.** `python3 tools/ci/prepush_check.py --base <base> --head <head> --path CHANGELOG.md --path ARCHITECTURE.md --path AGENTS.md lanes membership build-notes` → PASS; each path `not-member`; HDE Build Notes resolved to the one current file (its name is not pinned in any document, R-2).
7. **Claim grounding.** Re-check §7 against the head: every row, and that the five test files named in the CHANGELOG exist (`ls`), that `git ls-tree <head> engine/charts/` lists only `pure.py`, and that the generator exits 2 from a new temporary directory.
8. **Commands.** None is added to any document (PD-6); say so in the record.
9. **Local replay and clean tree.** `python3 tools/ci/prepush_check.py --base <base> --head <head> replay` → PASS, step 02 `reason=documentation_only`, step 03 `AGENTS_MD_CITATIONS_OK`, steps 04 to 15 skipped, step 16 `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; then `git status --porcelain --untracked-files=all` is empty.

**Hosted CI (note on OBS-9).** The workflow's path filter does not exclude these three files, so the `test` job runs on the PR. The replay models it: classification `documentation_only`, the AGENTS.md citation step, every Python and lane step skipped, and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The pre-push tool prints "reason=documentation_only means the workflow's path filter starts no hosted run"; for these paths that note is not true (the filter excludes only the eight `docs/` prefixes). The exact-head hosted run must be green. No CI waiver exists for HDE-EPIC041.

## 12. Prototype record

A throwaway clone under this session's scratchpad, at `9ff76b53`; the session checkout was not changed by it, and the clone ended clean after every run. CPython 3.13.17; git as installed. The prototype commit `8366b025c3e5461e18fa6f92ebe49549b44b9a4d` exists only in the clone and was never pushed.

### 12.1 Change set and companion diff

* `git diff 9ff76b53 8366b025`: 3 files, +26 −0.

  | Path | + | − |
  | :- | -: | -: |
  | `AGENTS.md` | 6 | 0 |
  | `ARCHITECTURE.md` | 2 | 0 |
  | `CHANGELOG.md` | 18 | 0 |

* Companion diff: `docs/ephemeral/HDE-EPIC041-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff`, 60 lines, 8,393 bytes, sha256 `4b5adc3d41d92bdfee1a32570686f4a6b73c9d1c5e956e6c374d3487e42c533d`. `git apply --check` is clean on `9ff76b53`; applying it to a clean checkout there and running `git add -A; git write-tree` gives tree `0487f5c44c376f26fc442eee26180e639aa3d954`, the prototype head's tree (the base tree is `e77c4c00606a…`).

### 12.2 Classifier, replay, membership (on `8366b025`, closed rails through `env -i`)

| Run | Result |
| :- | :- |
| `classify_ci_changes.py --base 9ff76b53… --head 8366b025… --event-name pull_request` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=3;lanes=none`; all seven lanes `false`; `needs_python=false`; `changed_tests=false`; changed-tests file 0 bytes. (A first call with abbreviated SHAs exited 2 with `Git comparison identity is not a full hexadecimal SHA`; noted in §11.) |
| `check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| `check_direct_db_contract.py` | `DIRECT_DB_CONTRACT_OK`, exit 0 |
| `prepush_check.py --path CHANGELOG.md --path ARCHITECTURE.md --path AGENTS.md lanes membership build-notes` | PASS; `not-member` ×3; admitted release `1.3.0`, roster 45, `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; HDE Build Notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.3.md`, 102,755 bytes, sha256 6fa054b1…; "repository unchanged" |
| `prepush_check.py replay` | PASS; steps 02 and 03 `SUCCESS [executed]`, 04 and 05 `SKIPPED [excluded]`, 06 to 15 `SKIPPED [executed]`, 16 `SUCCESS` with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; copy clean afterwards; replay step time 0.6 s |
| `git status --porcelain --untracked-files=all` | empty after every run |

This is a local replay, not hosted CI; exact-head hosted CI is PR-35's to verify.

### 12.3 Sweep at the prototype head

The instruction §3.3 search over the in-scope pathspec at `8366b025` finds 13 lines in exactly three files and no other:

| Match | Disposition |
| :- | :- |
| `AGENTS.md:130`, `:132` (new posture section) | State that the loader is removed and name the entry and the generator; none describes the loader as current |
| `ARCHITECTURE.md:13`, `:16` (new bullets) | Name `engine/charts/pure.py` and `adapter/chart_orchestration.py` as homes |
| `CHANGELOG.md:6`, `:7`, `:8`, `:11`, `:12`, `:13`, `:14`, `:15`, `:18` (new section) | Record the delivered state: the entry, the pure module, the tests, the removal, the `TypeError` behavior, the generator, the retired test, the log file, and the unfixed snapshot |

At the baseline the same search finds nothing in scope (§4), so SWEEP-1 holds at both ends. PR-30 re-runs it at its head and records any difference.

### 12.4 Behavior probes and tests (closed rails, `env -i`)

| Probe | Result |
| :- | :- |
| Generator from a new temporary directory | exit 2; stderr `compat_public not implemented`; directory empty |
| `load_chart('U1')`, `load_chart(42)` | both raise `TypeError: Invalid arguments to load_chart` |
| `parse_date_yyyy_mm_dd("1990-05-04")` with `time.tzset` counted | 1 call |
| `pytest -q -p no:cacheprovider tests/charts tests/adapter/test_chart_orchestration.py tests/scripts/test_make_compat_determinism_artifacts.py tests/loader` in a scratch venv with `requirements.txt` and `pytest` | **48 passed**; status empty. A first run in a venv with `pytest` alone showed 1 failed, 37 passed: the generator test saw `ModuleNotFoundError: jsonschema` (exit 1, not 2), an environment gap, not a defect (OBS-10) |

These are local observations to ground the documentation. They are not CI, QA or governed evidence.

## 13. Acceptance and evidence obligations

* **Business-case measures** (§3) hold at the PR head and are recorded.
* **§11 items 1 to 9 pass**, and exact-head hosted CI `test` is green (classification `documentation_only`, the AGENTS.md citation step, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`). No waiver exists for HDE-EPIC041.
* **Every statement written traces** to §7 (F-1 to F-9, the PR refs, or a cited canon title).
* **Acceptance of the unit** is PR-40's lineage review after Nathan's merge, then DOC-20. ACCEPT and COMPLETE are their decisions, not this plan's.

### 13.1 Checks record (PR description "Checks run" and the result record)

Commands and configuration (§11, closed rails through `env -i`), the tested-source SHA (distinct from any later record commit and from review-time HEAD), results with counts, the actor (the PR-30 session), the UTC window and the limitations. State which claims a run verified (the classifier, the citation and contract checks, membership, replay, the generator probe) and which were verified by diff and code reading (every other row of §7). Local runs are not CI, QA or governed evidence.

### 13.2 Governed evidence

None. No changed path is in the Human Evidence Index or the Machine Mirror, and none is a release member (§4, §12.2).

### 13.3 Reviews

The Codex code review runs on the PR. Under the repository instructions it excludes Markdown, so the PR may have no files in its scope; a result of "no files in code-review scope" is expected, not a failure. Findings, if any, go to PR-35 under the real-input rule.

### 13.4 PR description content (PR-30 writes it; AGENTS.md "PR descriptions")

* **Why:** the instruction (`HDE-EPIC041-WU-PR-03-pr-instruction-v1.0`, #798) and Plan v1.1 §6 WU-PR-03; the business case of §3.
* **What changed:** by path, as §6. State the decisions C-A (changed), C-B (not changed) and C-C (added), each with its basis from PD-2 to PD-4.
* **Checks run:** §13.1, with the sweep record of §12.3 re-run at the head.
* **Not in this PR:** DOC-20 and QA-10; canon drainage; the generator's compat repair, the `input_validators` reads and the architecture snapshot (CL-40 scan and the Product Owner); the close PR's sweep and architecture capture (CL-05, §17 OBS-D1).
* **What merging does:** the repository record names the delivered chart boundary; it establishes no QA verdict, acceptance, Ops, deployment, release change, PF09 or board movement, canon drainage or closure. No merge-order dependency. (The PR also carries records under `docs/ephemeral/`, so it states: "Merging preserves the record and approves nothing (D21-C)" for those.)
* **Doc-Delta candidates (non-mandatory; drift notes, not a gate; no canon file, `audit/docdeltas/` or governed surface is written):**
  * **DELTA-001.** HDE Architecture §1.1, "Non-BodyGraph chart loader classification": the sentence "The checked-in loader remains current repository reality until separately remediated" no longer holds. `engine/charts/loader.py` was removed by #796; the Adapter-owned entry is `adapter/chart_orchestration.py` (#791) and the pure module is `engine/charts/pure.py`.
  * **DELTA-002.** HDE Mechanics Guide §1.1, "BodyGraph and loader seam posture" and its remediation paragraph: "The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift" describes a module that is removed; the responsibility sits in `adapter/chart_orchestration.py` (F-1, F-2) and `engine/charts/pure.py` (F-3).
  * Drainage belongs to the canon owner after QA.

## 14. Security, privacy, migration, rollout, rollback

* **Security:** no code, route, credential, flag, network or environment gate changes. The new text names no secret, credential value, base URL, token or birth input. No security review is required by the instruction or the repository instructions.
* **Privacy:** the documents describe the keys-only log line by its key names only.
* **Migration, rollout:** none; no release cut, manifest or admission change.
* **Rollback:** revert the PR.

## 15. Risks and recovery

| Risk | Treatment |
| :- | :- |
| A written claim goes stale before merge (`main` moves) | §9 step 2 re-checks the three files and F-1 to F-9 before applying |
| The `AGENTS.md` citation step rejects the text | Checked on the prototype (`AGENTS_MD_CITATIONS_OK`); §11 item 4 re-runs it; PR-35 fixes any wording |
| `CHANGELOG.md` or `AGENTS.md` conflicts when the diff is applied | §9 step 3: apply by hand to the same effect and record it |
| C-C judged unneeded by Nathan or a reviewer | It is one section and removable; a revision is a v1.1 of this plan, not an in-flight change (§1) |
| A review finding on a constructed input | PR-35 answers it with the traced path and the stated limit (§6 last column); a P1 on a real input is fixed. Codex is expected to have no scope (§13.3) |
| Scope creep into code, the generator, `input_validators` or the snapshot | Excluded (§6 "Not changed"); a genuine boundary goes to one `RESCOPE_REQUEST` from the PR author through RS-10 to RS-20 with `PR_RETURN_PHASE` |
| An unrelated red CI result | PR-35's CI-red rules; the unit is not widened |
| Interruption | Resume in this session from the last saved artifact; prototypes only in throwaway clones |

## 16. Observations for owners (outside this unit's bound; nothing changed here)

* **OBS-9.** `tools/ci/prepush_check.py` line 905 prints "reason=documentation_only means the workflow's path filter starts no hosted run". That holds only when every changed path is under the workflow's eight excluded `docs/` prefixes. For `CHANGELOG.md`, `ARCHITECTURE.md` or `AGENTS.md` the filter does not exclude the path, so the hosted `test` job starts with `reason=documentation_only` (and the replay models it). Owner: the Product Owner / CI tooling owner. No change here; §11 records the correct expectation.
* **OBS-10 (environment).** The generator test (`tests/scripts/test_make_compat_determinism_artifacts.py`) needs the repository's `requirements.txt` installed (it imports `jsonschema` through the script). A minimal `pytest`-only environment fails it with exit 1. Owner: later sessions' surface advice. This unit's required checks need no pytest.
* **OBS-11.** `README.md` lines 110 and 230 describe `artifacts/compat/identity_hash.txt` as captured and test-verified. They are not made stale by this Epic; the generator that once wrote it broke earlier (FND-005). Owner: CL-40 scan and the Product Owner. No change here.

## 17. Carried items (instruction §12)

| Item | Owner |
| :- | :- |
| OBS-D1 (close-PR sweep and architecture capture timing; WU-PR-03 is the pre-QA pass and claims no close-PR sweep) | CL-05 at close |
| DELTA-001, DELTA-002 | Carried as PR-description notes (§13.4); canon owner after QA |
| SWEEP-1 | Recorded at the baseline (§4) and the prototype head (§12.3); PR-30 re-runs it |
| FND-005, FND-006, FND-007 | CL-40 scan and the Product Owner |
| OBS-6, OBS-7, OBS-8 (`scripts/scratch.py` holds Markdown; classifier error order; `ruby` path) | As the WU-PR-02 review records |
| OBS-2, OBS-5 (environment) | §11; §9 step 2 |
| Review v1.0 N-4 | QA-10 |
| TI-07 / CCR-1; TI-02; Candidate CRD Items 9 and 10 | Product Owner; CL-05 |
| Not produced | Proceed, code on a PR branch, PR, CI result, PR-35, PR-40 and DOC-20 records |
| Usage persistence | Pending (§21) |

## 18. CANON_CONFLICT_REGISTER (carried)

| ID | Classification | Status and reviewer | Treatment in WU-PR-03 |
| :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION (acceptance map for tokenless work) | APPROVED, Thoth, CF-E-30 review v1.1 (Ruling R-A); confirmed by Isis IA-30 v1.1 | None; a close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 | CANON_RECONCILIATION (Business Case content lists) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 | CANON_RECONCILIATION (S19 vendor decisions) | APPROVED as conditional, Thoth, review v1.1 | Not triggered: the unit changes three Markdown files and adds no vendor, route, evidence tool or gate row |
| CCR-4 | CANON_RECONCILIATION (cited Build Notes loader record) | APPROVED, Thoth, review v1.1 | None |

No new entry. The canon sections read for this unit (HDE Architecture §1.1, HDE Mechanics Guide §1.1) describe the loader as drift awaiting remediation and say "this classification does not claim that relocation, caller migration, or removal has occurred". The delivered boundary is the remediation they anticipate, so this is drift to drain (DELTA-001, DELTA-002), not a conflict between canon and an approved base. HDE Build Notes addenda 2.2 to 2.4 conflict with neither base.

## 19. PR-30 and PR-35 obligations

* **PR-30** (this session, after the Proceed for exactly v1.0):
  * recover existing work first;
  * implement only §6 from the companion diff;
  * run §11;
  * decide any obvious in-scope correction under the PR-30 rule and record it under *In-flight decisions*;
  * take a material boundary (as PR-30 defines it) to one `RESCOPE_REQUEST` for the IA through RS-20 with `PR_RETURN_PHASE`;
  * commit once; publish one PR; record the sweep and the replay; write the result record;
  * return `PR_CANDIDATE_PUBLISHED` with one handoff to PR-35 in its own session.

  It does not resolve reviews, wait for CI readiness or merge.
* **PR-35** (its own dedicated session):
  * subscribe to the PR; retrieve every review finding and thread;
  * fix each that shows a wrong result, a crash or a guarantee breach on a real input, and answer every other with the traced path and the stated limit; declining a P1 or a security finding goes to the Product Owner first; after two consecutive rounds of the same class, one design question to the Product Owner;
  * re-run §11 items 1 to 6 locally before each coherent corrective push; no `[skip ci]`; known findings before stale CI;
  * if a hosted failure appears, confirm whether it reproduces on the base before treating it as this PR's, and follow the CI-red rules;
  * verify current-head CI (`documentation_only`, the citation step, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability;
  * return `MERGE_PENDING — Ready to merge` without merging, with the conditional PR-40 block.
* **Nonclaims every record keeps:** no QA verdict, acceptance, Ops, deployment, PF09 movement, drainage or closure; no canon edit; no release cut.

## 20. TypeSafe reading and surface advice for the receiving session (PR-30, WU-PR-03, plan v1.0)

* **Method.** Installed TypeSafe scoring skill, request v8.2, `score_v8.py` run once before this plan was saved; session kind `implementation`; label "HDE-EPIC041 PR-30 WU-PR-03 implementation". The Notion row was not written (PR-20 handoff rule).
* **Action sent (v8.2).** "Implement, in a dedicated session, the third and last PR work unit of an approved Epic from a detailed PR plan that the Product Owner has proceeded; it is a documentation-only unit: apply an already prototyped, locally checked change of about 26 added lines across three existing Markdown files (a new CHANGELOG section naming the two delivered units, two added bullets in the architecture map, and one short posture section in the agent-rules file), with the exact text and a companion diff supplied; run a few read-only checks (the CI change classifier, an agent-rules citation check, a direct-database contract scan, a pre-push membership report and a documentation sweep), then commit once and open the pull request, which starts the hosted CI job with no test lanes; no code, tests or schemas change and no live run against a provider occurs; an automated code review that excludes Markdown, a separate merge-readiness session, a lineage review and a documentation-completion verification follow."
* **Reading, as printed.** **TypeSafe v8.2: Sonnet 5.5 at medium.** Effort score 0.76 (confidence 0.79); rung probabilities low 0.28, medium 0.69, high 0.03, extra high 0.00, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.42, Sonnet 5.5 0.56, Haiku 5.5 0.02 (confidence 0.41). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.118, Opus 5.5 at medium 0.290, Opus 5.5 at high 0.013, Opus 5.5 at extra high 0.000, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.157, Sonnet 5.5 at medium 0.386, Sonnet 5.5 at high 0.017, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.006, Haiku 5.5 at medium 0.014, Haiku 5.5 at high 0.001, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Sonnet 5.5 and Opus 5.5. Sent 2026-10-29T01:25:44Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.63 s; 5542 input and 69 output tokens; jev-1.13.0. Rung by rule: medium; model by rule: Sonnet 5.5.
* **Flags.** "model near tie between Sonnet 5.5 and Opus 5.5", as printed.
* **Picks.** Nathan has stated no pick for PR-30 (WU-PR-03) and none for this PR-20 session (its reading is the instruction's §14). None is recorded.
* **Surface advice (PR-30).**
  * PR-30 continues in this same top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, after this plan's documents PR merges, with GitHub access for one PR.
  * It needs `git`, `bash` and a CPython (3.12 matches CI), a non-shallow clone and `env -i` closed rails, because the container exports vendor, database and GitHub credentials. The required checks run in seconds (the classifier, citation, contract and pre-push checks, 0.1 s to 2.4 s each in this session); no package install or pytest run is required.
  * Keep any negative or extra probes in a throwaway copy, and make no tool call that touches the checkout during the replay.
  * Not needed: code or test changes, open rails, or vendor, Railway, database or Notion writes.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage_id | HDE-EPIC041-PR20-WU-PR-03-20261029 |
| change | HDE-EPIC041 (EPIC) |
| specification | `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` (v1.1) |
| work unit | WU-PR-03 (documentation of R-01 to R-04 as delivered; AC-01 to AC-05 recorded, not re-proved) |
| ecosystem release | GCFPE-20261027.1 / 102726.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 102726.1, https://app.notion.com/p/4064590a05eb8141a25be9a48df6c2a9, page state 2026-10-27T13:18:23.839Z |
| role/stage | dedicated WU-PR-03 PR engineering session / GCF-14 |
| capture time | 2026-10-29 |
| runtime identity | https://claude.ai/code/session_01Q789tzy6y65nrdG8GrR5hb |
| inherited usage | `HDE-EPIC041-DOC10-WU-PR-03-20261028` (instruction front matter), which itself inherits `HDE-EPIC041-PR40-WU-PR-02-20261028` |
| repository persistence | PENDING: no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` (`docs/changes/` holds `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md` only; checked at `9ff76b53`). Owner: GCFPE management. Non-gating |

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `9ff76b53`; this branch changes nothing there. Terms searched: final repository documentation, documentation unit, CHANGELOG, README, AGENTS.md, docs sweep, Doc-Delta, doc delta candidate, drift note, chart loader, `engine/charts`, HDE-SEPA006, planning document, PF version, copy/paste command, per-PR plan, business case.

| Title | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Notes | Front matter; addenda 2.2, 2.3 and 2.4 in full | R-1 and R-2 citation rules (PD-7); the deferred obligations DELTA-001, DELTA-002, SWEEP-1 and the 2.2 bearing (PD-9, PD-10); 2.1 not engaged |
| HDE Architecture | §1.1 "Non-BodyGraph chart loader classification" (paragraph read in full) | DELTA-001; the C-A basis (a Required-Now classification that places chart operational concerns in the Adapter and allows only pure validation in Engine) |
| HDE Mechanics Guide | §1.1 "BodyGraph and loader seam posture" and the remediation paragraph | DELTA-002 |
| Change Process Guide | §3.5.3 "Repo docs sweep (major epics)", including the claim-proof rule | §7; §11; OBS-D1 |
| HDE Governance | §9.7.7 "Plan approval gate" (hold label, Proceed as approval); the business case and stop rule as the instruction quotes them; §9.2 as the instruction applies it (no Doc-Delta required) | §1, §3, §13.4 |
| HDE Build Checklist — Separation | Task HDE-SEPA006 heading and Subtask .1 heading | Identity of the task the CHANGELOG cites |

The instruction's own canon table (Change Process Guide docs-only rules, HDE Governance §9.1.4, §9.1.5, §9.2, §9.3, Plan Templates, HDE CRD Records) was relied on as the instruction's record of what it read; this plan did not re-read those sections.

## Approval

* **Approval hold:** `ASK OK? — PR IMPLEMENTATION PLAN`
* **Approval state:** Pending.
* **Approval authority:** Nathan / Product Owner, by invoking `PR Implementation Proceed` (PR-30) for exactly this v1.0.
* **Approved scope or rejection basis:** not yet decided.

## Nonclaims

This plan is not implementation, a Proceed, a PR, CI, QA, Ops, acceptance, a PF09 or board movement, a canon change, a PF10 addendum or closure. The prototype results are local scratch observations, not CI, not QA and not governed evidence. It decides C-A, C-B and C-C as the instruction directs; it does not decide canon. Nothing outside `docs/ephemeral/` is changed by this plan's PR. Merging it preserves the record and approves nothing (D21-C).
