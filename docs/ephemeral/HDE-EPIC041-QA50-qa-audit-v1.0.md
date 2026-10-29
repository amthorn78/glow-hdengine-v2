---
artifact_type: QA_AUDIT
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA50-QA-AUDIT
QA_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md
state: AUDIT_COMPLETE
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
companion_plan: docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING, authored in the same invocation after this Audit)
predecessor: none (first QA Audit for HDE-EPIC041; no earlier QA-50 or QA-60 result, QA-70 review or QA-80 revision exists on main)
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-EPIC041-QA20-live-qa-guide-v1.0.md (LIVE_QA_GUIDE v1.0, GUIDE_READY)
QA_READINESS_ID: docs/ephemeral/HDE-EPIC041-QA10-qa-readiness-v1.0.md (QA_READINESS v1.0, READY_FOR_QA)
REALITY_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA10-reality-audit-v1.0.md (REALITY_AUDIT v1.0, COMPLETE, of main 6a0f55f0)
CHANGE_AUDIT_TRIAGE_ID: docs/ephemeral/HDE-EPIC041-QA10-change-audit-triage-v1.0.md (CHANGE_AUDIT_TRIAGE v1.0, COMPLETE, 28 rows)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; CF-E-30 review v1.1 INITIAL_APPROVE, Thoth)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1; IA-30 review v1.1 INITIAL_APPROVE, Isis)
delivery_lineage: "WU-PR-01 #791 squash e72c9bac (lineage review v1.0 ACCEPT); WU-PR-02 #796 squash 9843934f (lineage review v1.0 ACCEPT); WU-PR-03 #800 squash 634be154 (lineage review v1.0 ACCEPT); DOC-20 v1.0 COMPLETE"
ops_lineage: none (Plan v1.1 §6 declares no Ops unit)
approved_amendments: none
remediation_lineage: none
repository: amthorn78/glow-hdengine-v2
repository_head_read: 1e2ac50e88dd30253e3c96315fad0836d62ad79d (origin/main; "HDE-EPIC041-QA20-live-qa-guide-v1.0.md", direct commit by amthorn78 2026-10-29T05:23:43Z; parent b67056ef "PF10")
producer: Kronos, the continuing QA authority for HDE-EPIC041 (role continuity per D27; this session's platform identity is not directly known and is not invented)
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81dbb28ed028d68b8816; page state 2026-10-27T13:08:15.848Z, read in full)
r1_row: GCF-21
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261027.1 / 102726.1", exactly 56 members; QA-50, QA-60, QA-70, QA-80 and QA-90 at 102726.1 are members)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.4.md (871 lines, 123,623 bytes, sha256 b2142317093e9e89c69ee774aec61c518be3e9a8e0d7c71e2fbb21752f2ca091; read in full; provenance, not a gate)
pf10_addenda: "2.1 (S19 decisions): not engaged. 2.2 (planning documents and PF-Canon versions are never inputs; close-pack writer only at close): binds every QA evidence artifact, Index or Mirror row, path proof and the close pack. 2.3 and 2.4 (WU-PR-01 and WU-PR-02 lineage records): deferred obligations reconciled in section 15. 2.5 (QA-10 triage record, new since the Guide): records DELTA-001 to DELTA-003 and CCR-5 as PROPOSED; no decision"
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
canon_conflict_register: held in the companion QA Plan section 21 (CCR-1 to CCR-4 carried unchanged; CCR-5 carried, PROPOSED; CCR-6 proposed by this Audit, finding QA50-F03)
next_stage: QA-70 — Review Whole-Change QA Plan — 102726.1 (https://app.notion.com/p/4064590a05eb819ca94af85f1561b596), continuing Isis, after the companion QA Plan
authored_at: 2026-10-29 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-QA50-20261029
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    requirements: R-01 to R-04; AC-01 to AC-05; work units WU-PR-01, WU-PR-02, WU-PR-03
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: QA-50 — 102726.1 (https://app.notion.com/p/4064590a05eb81dbb28ed028d68b8816), revision as of 2026-10-27T13:08:15.848Z
    role_stage: continuing Kronos / GCF-21 (QA-50), QA_AUDIT phase
    captured_at: 2026-10-29
    runtime_identity: not directly known (D27)
    inherited_usage: HDE-EPIC041-QA20-20261029
    outcome: AUDIT_COMPLETE for this artifact; the same usage produced the companion QA Plan (PLAN_PENDING)
    result_references: this Audit and the companion QA Plan at the paths above; their pull request and merge commit do not exist at writing and are recorded by the stage that reads them
    repository_persistence: PENDING (docs/changes/ has no GCFPE_PROMPT_PROVENANCE.md at 1e2ac50e; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — QA Audit v1.0 (QA-50): AUDIT_COMPLETE

## 0. What this Audit is

**AUDIT_COMPLETE.** This is Kronos's independent whole-change QA Audit of HDE-EPIC041. It audits testability, requirement and acceptance coverage, integration seams, actual repository and environment behavior, evidence sufficiency, dependencies, risks, data and permissions, and deviations between planned and delivered work, and it records every repository locus the companion QA Plan relies on (section 5). The companion QA Plan, authored next in the same invocation, is the separate `QA_PLAN` artifact.

* **It is** the "initial QA Audit for the epic" that Plan Templates names as an allowed provenance source for repository loci ("Path provenance and locus provenance lock"). Every repository-resident string the QA Plan cites as Audit-proven is copied verbatim from section 5 or section 4 of this Audit.
* **It is not** QA execution, a QA verdict, a QA Plan, an approval, acceptance, a readiness decision, a remediation, PF10 text, a canon change or closure. The local runs reported in section 4 are read-only audit observations in a throwaway clone; they are not QA evidence, not CI and not governed evidence, and they prove no PASS.

## 1. Canon and sources relied on

Resolved from `docs/pfcanon/` on `main` at `1e2ac50e`; each stable identity resolves to exactly one controlled Markdown file. No Google Doc, export or archive was opened. Terms searched (exact-string first, then `grep -n -i`): Live QA Plan, step log, qa_step_logs_manifest, path_proof, update_evidence_index, EPIC041, admission, evidence-only, open rails, production-functional, Step-0B, doc delta, D0, QA RCA, functional proof, entrypoint regression, Moon Loop, non-QA-root, rerun, venue, close pack.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §0 "Document Control" (all subsections, including "Repository loci and file minting", "Template-safe placeholders and omission syntax", "Canon precedence for template use"); §1 "Live QA Plan" (whole); "Review guardrails" (whole, including "Hard blockers for plan approval/execution", "PF09 phased-routing boundary", "QA planning QoS guardrails") | Plan structure; locus provenance lock; Step-0B; rerun posture; non-QA-root route; check matrix rules; functional proof; hard blockers; PF09 routing |
| Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.7.md`) | §2.2.5; §2.3; §3.1 to §3.3; §3.4.1 to §3.4.14; §3.5.6; §4.1 to §4.4.7; §9.2.13 "D0 discovery gate (non-token)"; §9.2.15.5 | Tooling discipline and preflight; evidence grammar; execution-critical helper readiness; VCS boundary; plan validity lint; D0 gate |
| Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.5.md`) | §0.4.1 to §0.4.1.3; §0.5.1; §0.7 "QA branches posture"; §3.5.1; §3.5.2.8 "Live QA via harness (required for epic closeout)"; §4.5 | D0 and QA RCA & Doc Delta summary; functional proof producing governed evidence; evidence landing routes; entrypoint regression tests in CI; evidence-only QA PR scope |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §3.4 "Open rails (controlled)", including "Production-functional epic live-proof requirement" and "Other production-affecting scope"; §9.1.3 to §9.1.5 | Open-rails determination; QA escalation (ESC-10, ESC-30) |
| HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`) | §8.17 "Scope / root", "Current-state evidence", "Close-run family exception"; §8.17.1 to §8.17.4 | QA root; the QA Plan decides which artifacts are indexed; no Epic close-run family |
| HDE Build Checklist — Separation (`PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks HDE-SEPA006.1 to .3 | Deliverables and required evidence, including "required indexing through the existing governed writer" |
| HDE Architecture (`PF02-Canon-HDE-Architecture-v2.4.7.md`) | §1.1 "Non-BodyGraph chart loader classification" paragraph | DELTA-001 text |
| HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md`) | §1.1 "BodyGraph and loader seam posture" paragraph | DELTA-002 text |
| HDE State of the Repository (`PF31-Reference-HDE-State-of-the-Repository-v0.1.md`) | §2.2 loader paragraph | DELTA-003 candidate text |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.4.md`, the current controlled PF10) | Whole file | Planning documents and PF versions are never inputs; close pack only at close; WU-PR-01 and WU-PR-02 lineage records; QA-10 triage record |
| Technical Writing Best Practices (`PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`) | §3; §12 "Task, plan, and execution-document writing" | Source fidelity; observed versus required versus unknown |
| AGENTS.md | "Closed rails default"; "Pytest readiness rule"; "Redaction rule"; "Evidence harness"; "Governed evidence rules"; "Evidence attribution, currentness and distinct decisions"; "Operating routes and authority"; "HDE-EPIC041 current posture" | Environment, redaction, writer, attribution and route facts |
| In-flight records (current versions, whole) | The Guide; the three QA-10 records; Specification v1.1 and review v1.1; Plan v1.1 and review v1.1; the three lineage reviews; DOC-20 v1.0 | Every obligation audited below |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

No formally approved bounded Product Owner rescope applies. Scoped override in force: HDE Build Notes (planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close) over Change Process Guide, Glow QA Guide and Plan Templates text that would bind a planning document or a PF file name or version, for that scope only.

## 2. Intake verification

| Check | Result | Evidence |
| :- | :- | :- |
| The Guide is `GUIDE_READY`, complete and on `main` | Yes. Landed by direct commit `1e2ac50e` (amthorn78, 2026-10-29T05:23:43Z), which adds only the Guide under `docs/ephemeral/` | `git log -1 1e2ac50e`; `git show --stat 1e2ac50e` |
| The readiness record is `READY_FOR_QA` with its two companions | Yes; the three QA-10 records landed by direct commit `ad537323` | The three records, read end to end |
| Later material evidence since the Guide was written at `ad537323` | `b67056ef` ("PF10", amthorn78, 2026-10-29T05:10:09Z) deletes the nine `cline_skills/*.skill` files and renames HDE Build Notes v13.9.3 to v13.9.4, adding the QA-10 triage record (134 lines). Code, tests, CI, tools and governed evidence are byte-identical: `git diff --name-status 6a0f55f0 1e2ac50e` lists only 4 added `docs/ephemeral/` files, 9 deleted `cline_skills/` files and the PF10 rename | Kronos observation at `1e2ac50e` |
| Effect on readiness | None. The new PF10 record restates what QA-10 found and decides nothing (CCR-5 stays PROPOSED); the deleted `cline_skills/` files were the cause QA-10 gave for the red `main` push classification (QA50-F09) | HDE Build Notes, QA-10 triage record |
| Approved bases, amendments, remediation, Ops | Unchanged: Specification v1.1, Plan v1.1; no amendment, remediation or Ops | Readiness §2 |
| Product Owner dispositions | D-1 "Retire it" (2026-10-28), delivered; the 2026-10-28 direction recorded in HDE Build Notes (planning documents never inputs; close pack only at close). CCR-5 has no ruling. No disposition is pending for QA-50 itself | Readiness §2.4; HDE Build Notes |
| Selected release and prompt identity | GCFPE-20261027.1 / 102726.1, 56 members; QA-50 page read in full at its 2026-10-27T13:08:15.848Z state | Register; QA-50 page |
| Repeated invocation | No prior QA-50, QA-60, QA-70 or QA-80 artifact for HDE-EPIC041 exists on `main` or in an open pull request (no open pull requests at 1e2ac50e) | `ls docs/ephemeral`; GitHub pull request list |

**Readiness is not invalidated**; the `BLOCKED` route is not taken.

## 3. Change identity and delivery lineage

| Unit | Pull request | Reviewed head | Exact-head CI (verified at audit time through the authenticated GitHub API) | Squash on `main` | Lineage review |
| :- | :- | :- | :- | :- | :- |
| WU-PR-01 (HDE-SEPA006.1) | #791 | `815fd5b2` | run 40723983402, job 122942172254 `test`, `success`, 2026-10-28T16:14:27Z to 16:33:34Z | `e72c9bac` | ACCEPT |
| WU-PR-02 (HDE-SEPA006.2) | #796 | `8200d1fb` | run 40774524113, job 123120191675 `test`, `success`, 2026-10-28T21:45:13Z to 22:04:52Z | `9843934f` | ACCEPT |
| WU-PR-03 (documentation) | #800 | `88d4a311` | run 40801978516, job 123211959044 `test`, `success`, classification `documentation_only`, lanes none (per its lineage review; not re-read) | `634be154` | ACCEPT |

* **Whole delivered change set.** `git diff --name-status e121e354 1e2ac50e`, excluding `docs/` and `cline_skills/` (`e121e354` is the first parent of `e72c9bac`), lists exactly 16 paths: `A adapter/chart_orchestration.py`, `A engine/charts/pure.py`, `D engine/charts/loader.py`, `M ci/checks/classify_ci_changes.py`, `M scripts/make_compat_determinism_artifacts.py`, `A tests/adapter/test_chart_orchestration.py`, `A tests/charts/test_chart_loader_import_guard.py`, `A tests/charts/test_chart_pure_interface.py`, `A tests/charts/test_chart_pure_purity.py`, `A tests/scripts/test_make_compat_determinism_artifacts.py`, `M tests/loader/test_load_chart_fixture_only.py`, `M tests/loader/test_loader_logs_keys_only.py`, `M tests/retired_tests.md`, `M AGENTS.md`, `M ARCHITECTURE.md`, `M CHANGELOG.md`. Nothing under `docs/` outside `docs/ephemeral/` and `docs/pfcanon/` changed.
* **Unchanged by the change** (same diff, empty): `artifacts/compat/`, `artifacts/logs/loader_call.jsonl`, `catalog/manifest.json`, `.audit_src/` (no commit in `e121e354..1e2ac50e` touches `.audit_src/`).
* **Code identity since delivery.** `git diff --name-only 9843934f 1e2ac50e` outside `docs/` and `cline_skills/` lists only `AGENTS.md`, `ARCHITECTURE.md` and `CHANGELOG.md` (WU-PR-03). The code #796's exact-head CI tested equals the code at `1e2ac50e`, and the WU-PR-01 files (`adapter/chart_orchestration.py`, `engine/charts/pure.py` and their three test files) have not changed since `e72c9bac`.
* **Planned versus delivered.** No material deviation. The one intended failure-behavior change (legacy shapes raise `TypeError`) is D-1's. The generator's compat computation is not restored (excluded scope, FND-005). The post-merge `main` push runs (40735776026 on `e72c9bac`, 40777435776 on `9843934f`) were in progress when their lineage reviews were committed; this Audit does not rely on them.

## 4. Repository and environment facts (audit observations at `1e2ac50e`; not QA)

All runs below were made by Kronos's audit workers in throwaway full-history clones under `/tmp`, under `env -i PATH=<venv>/bin:/usr/local/bin:/usr/bin:/bin HOME=<scratch> LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` unless stated. Nothing was committed or pushed, and `/workspace/glow-hdengine-v2` was not written. They are observations for planning, not QA, CI or governed evidence.

### 4.1 Environment

* Python: `/usr/bin/python3.12` (3.12.3). CI uses Python 3.12: `.github/workflows/ci.yml` L80 to L85 (`actions/setup-python@v5`, `python-version: '3.12'`).
* Install: the CI command (ci.yml L87 to L95) `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` exited 0; readiness `python -m pytest --version` printed `pytest 8.4.2` (ci.yml L97 to L100). The install needs package-index network access; that is environment setup, not a QA step.
* The editable install maps only `adapter`, `catalog`, `engine`, `math` and `presenter` to the clone it was run from; `scripts`, `tools`, `ci` and `tests` are imported from the working directory. **Consequence for the Plan:** the virtual environment must be installed from the same clone that executes QA.
* `-e .` creates `glow_hdengine.egg-info/` at the repository root; `.gitignore` L34 `*.egg-info/` ignores it, so `git status --porcelain --untracked-files=all` stays empty.
* `git check-ignore -v --no-index` on `audit/qa/hde-epic041/qa_step_logs_manifest.json`, `audit/qa/hde-epic041/checks/d0-discovery/primary.log`, `audit/qa/hde-epic041/00_meta/doc_deltas.md` and `audit/docdeltas/hde-epic041_doc_deltas.md` exited 1: none of the planned QA evidence paths is git-ignored.
* CI's job-level environment (ci.yml L45 to L52): `LC_ALL: C`, `LANG: C`, `TZ: UTC`, `SAFE_MODE: "1"`, `ALLOW_NETWORK: "0"`, `APP_ENV: dev`, `PYTHONDONTWRITEBYTECODE: "1"`.
* `bash`, `git`, `cmp`, `grep`, `cut`, `sort`, `date` and `sha256sum` resolve under `PATH=<venv>/bin:/usr/bin:/bin`; no check needs `ruby`.

### 4.2 The change's tests and the retained coverage

* One run of `python -m pytest -p no:cacheprovider -q -rA` over the seven change files and the two PF09.3 retained-coverage nodes exited 0 with **43 passed** (per selector: L-05 20, L-06 5, L-07 8, L-08 4, L-09 1, L-10 2, L-11 1, L-12 1, L-13 1; section 5). No skip or xfail marker exists in any selected file (`grep -n -i 'skip\|xfail\|importorskip'` over the nine files: no hit).
* The same run with `SAFE_MODE` unset, and again with `APP_ENV` unset, gave identical sorted PASSED id lists (43 each); the tests that depend on `SAFE_MODE` set it themselves with `monkeypatch`.
* `pytest.ini` `testpaths` lists the two loader tests and both provider files but not `tests/charts/*`, `tests/adapter/test_chart_orchestration.py` or `tests/scripts/test_make_compat_determinism_artifacts.py`; those five files run only when named. CI runs the change's files only through the changed-tests lane (ci.yml L128). QA names them explicitly (QA50-F04).
* `python -m pytest --collect-only -q -p no:cacheprovider` over the same nine selectors prints `43 tests collected` as its last line.
* `git status --porcelain --untracked-files=all` was empty after every run.

### 4.3 C-1, the compat-determinism generator

* From an empty temporary working directory and from the repository root, `python scripts/make_compat_determinism_artifacts.py` exited **2** with empty stdout and stderr exactly `compat_public not implemented` plus LF; the temporary directory stayed empty; the 11 files of `artifacts/compat/` kept name, size and mtime; a wrapper counting calls of `adapter.chart_orchestration.load_chart` recorded **0** calls. The delivered test `tests/scripts/test_make_compat_determinism_artifacts.py::test_generator_exits_2_and_writes_nothing_from_any_working_directory` asserts exactly `(2, "", "compat_public not implemented\n")` and an empty temporary working directory.

### 4.4 The entry's `safe_mode` field

* `load_chart("1990-01-01", "12:34", "Amsterdam, NL", tz="Europe/Amsterdam", log_sink=<list>.append)` emitted one log line per call with `safe_mode` `true`, `false` and `false` for `SAFE_MODE` `1`, `0` and unset (`adapter/chart_orchestration.py` L79 reads `SAFE_MODE` with default `"0"`), under `ALLOW_NETWORK=0`. The delivered test `test_safe_mode_field` covers the same three values by `monkeypatch` inside a closed-rails process, so QA needs no process-level rails change for it.

### 4.5 Evidence tooling, read-only

| Command | Exit | Output |
| :- | :- | :- |
| `python tools/evidence/update_evidence_index.py --check` | 0 | `[evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` |
| `python tools/evidence/orientation_demo.py --check` | 0 | none |
| `ci/checks/check_mirror_schema.sh` (a Python script; `#!/usr/bin/env python3`) | 0 | none |
| `python tools/evidence/validate_evidence_paths.py` | 0 | none |
| `ci/checks/check_evidence_index_hash.sh` (bash) | 0 | none |
| `python tools/evidence/check_lf_endings.py` (runs `ci/checks/check_final_lf.sh`) | 0 | none |
| `python scripts/release_id_recompute.py --check-manifest-only` | 0 | none |

The first two need the CI install (`jsonschema`); without it they exit 1 with `ModuleNotFoundError: No module named 'jsonschema'`. `python tools/evidence/orientation_demo.py` without `--check` is not read-only (it runs the updater in write mode).

### 4.6 The import guard

* `tests/charts/test_chart_loader_import_guard.py` enumerates tracked files with `git ls-files -z -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/'`, skips `classify_ci_changes._HISTORICAL_PREFIXES`, asserts that the three live callers are among the scanned files (`assert set(LIVE_CALLERS) <= set(scanned)`, so a scan that saw nothing would fail) and that no scanned file has a finding.
* Negative probes in throwaway worktrees: a `git add`ed `scripts/zz_planted_import.py` containing `import engine.charts.loader` made `test_no_tracked_python_file_imports_the_retired_loader` fail and name the file; a `git add`ed empty `engine/charts/loader.py` made `test_the_retired_module_path_does_not_exist` fail; an untracked planted importer is not seen (the guard scans tracked files only, consistent with IR-02; QA50-F05).

### 4.7 Purity of `engine.charts.pure` at import

* `python -X importtime -c 'import engine.charts.pure'` and a `sys.modules` delta both show only standard-library modules (`typing`, `_typing`, `collections.abc`, `contextlib`, `unicodedata`, `typing.io`, `typing.re`) plus `engine`, `engine.charts` and `engine.charts.pure`. Under `python -S` the standard library loads `os` transitively through `contextlib`; `pure.py` itself imports only `re`, `unicodedata` and `typing`. The delivered purity test forbids direct imports by an AST deny-list and checks a fresh import against an operational-module deny-list (`random`, `secrets`, `socket`, `logging`, `json`, `pathlib` and others); both pass. IR-01's residual is that both lists are deny-lists (QA50-F06).

### 4.8 Hosted CI workflow facts (`.github/workflows/ci.yml` at `1e2ac50e`)

* Changed-tests lane L107 to L133: in a detached worktree, `python -m pytest -q -p no:cacheprovider -- "${changed_test_targets[@]}"` (L128), then `git diff --exit-code` and an empty `git status --short --untracked-files=all` (L129 to L130). It is the only lane that ran the change's own test files.
* Evidence lane L221 to L240: `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check` (an EPIC024 refresher; an HDE-EPIC041 root does not affect it), `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`, then six named evidence test files.
* QA lane L242 to L271 runs seven `tests/qa/` files, including `tests/qa/test_generic_qa_harness.py`; it is selected only by `tools/qa/` or `tests/qa/` paths.

## 5. Audit-proven loci (verbatim; for the QA Plan's locus provenance lock)

Each locus below exists at `1e2ac50e`, proven by the command in its row (all run by Kronos or its audit workers at that commit; output as observed). The QA Plan copies these strings verbatim.

| ID | Locus (verbatim) | Kind | Proof at `1e2ac50e` |
| :- | :- | :- | :- |
| L-01 | `adapter/chart_orchestration.py` | Adapter-owned chart entry (`load_chart`) | `git ls-files`; imports `from engine.charts.pure import normalize_chart, validate_birth_inputs` (L20) |
| L-02 | `engine/charts/pure.py` | Pure Engine chart module | `git ls-files`; `engine/charts/` holds only this file |
| L-03 | `engine/charts/loader.py` | Removed module (negative existence) | absent from `git ls-files`; `test ! -e` true |
| L-04 | `scripts/make_compat_determinism_artifacts.py` | C-1 generator | `git ls-files`; L9 `from adapter.chart_orchestration import load_chart` |
| L-05 | `tests/adapter/test_chart_orchestration.py` | Entry tests, 20 cases | `--collect-only`; blob `06c1ed555ed8` |
| L-06 | `tests/charts/test_chart_pure_purity.py` | Purity tests, 5 | blob `bba716089d39` |
| L-07 | `tests/charts/test_chart_pure_interface.py` | Interface tests, 8 cases | blob `c996cf4d9c61` |
| L-08 | `tests/charts/test_chart_loader_import_guard.py` | Import guard, 4 | blob `9a57943c17cc` |
| L-09 | `tests/scripts/test_make_compat_determinism_artifacts.py` | Generator test, 1 | blob `bfc054cef32d` |
| L-10 | `tests/loader/test_load_chart_fixture_only.py` | C-2, 2 | blob `21d36bc6fc55` |
| L-11 | `tests/loader/test_loader_logs_keys_only.py` | C-3, 1 | blob `27bd3d61c50d` |
| L-12 | `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` | PF09.3 retained coverage | node collected |
| L-13 | `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` | PF09.3 retained coverage | node collected |
| L-14 | `tests/provider/test_vendor_and_prod_guard_min.py`, `tests/provider/test_vendor_call_rails_and_config.py` | Files holding L-12 and L-13 | `git ls-files` |
| L-15 | `tools/qa/qa_harness.py` | Tracked QA harness library (no CLI): `HarnessConfig` (L58), `CheckResult` (L109), `validate_check_id` (L1363), `run_pytest_check` (L2185), `record_check` (L2401), `Status` values `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED` | `grep -n`; demonstrated in section 10.4 |
| L-16 | `tools/evidence/update_evidence_index.py` | Sole authorized Index/Mirror writer; CLI `[--check] [--rebind-sanity-log] [--epic-id ID]` (`main` L5294); `_refresh_path_proof(path, *, default_produced_at, check)` (L4510); `EPIC040_QA_PRIMARY_ARTIFACTS` (L3296) spliced at L4232 (`*EPIC040_QA_PRIMARY_ARTIFACTS,`) | `--help`; `grep -n` |
| L-17 | `tools/evidence/orientation_demo.py` | Read-only with `--check` | exit 0 |
| L-18 | `tools/evidence/validate_evidence_paths.py` | Path validation | exit 0 |
| L-19 | `tools/evidence/check_lf_endings.py` | Final-LF check | exit 0 |
| L-20 | `ci/checks/check_mirror_schema.sh` | Mirror schema check (Python script) | exit 0 |
| L-21 | `ci/checks/check_evidence_index_hash.sh` | Index hash sentinel check | exit 0 |
| L-22 | `ci/checks/classify_ci_changes.py` | CI classifier; `_HISTORICAL_PREFIXES` (L164) `('.audit_src/', '_archive/', '_backup_', 'artifacts/architecture/', 'artifacts/epic020/', 'audit/history/', 'audit/historical/', 'audit/ops/')`; `_DOCUMENTATION_PREFIXES` (L179); owner map for `engine/charts/pure.py`, `adapter/chart_orchestration.py`, `engine/charts/loader.py` (L612 to L620); writer owners (L768 to L772) | `grep -n`; import |
| L-23 | `docs/evidence/INDEX.json` (653 rows), `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt` | Writer-owned governed files | `git ls-files`; row count |
| L-24 | `.github/workflows/ci.yml` | Workflow lines cited in section 4 | read |
| L-25 | `pytest.ini`, `.gitignore` (L34 `*.egg-info/`), `requirements.txt`, `requirements-dev.txt`, `pyproject.toml` (`[project.scripts]` `hdctl = "engine.cli.main:cli"`), `Procfile` (`web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()'` with its bind, worker, thread and timeout options) | Configuration and production entry declarations | read |
| L-26 | `tests/qa/test_generic_qa_harness.py::test_pf27_header_and_manifest_replace_by_check_id` (L337), `tests/qa/test_generic_qa_harness.py::test_same_interpreter_and_classification` (L368), `tests/evidence/test_evidence_skeleton.py::test_refresh_path_proof_supports_staged_missing_artifact` (L14) | CI entrypoint regression tests for `record_check`, `run_pytest_check` and `_refresh_path_proof` (QA lane L259; evidence lane L234 to L240) | `grep -n` |
| L-27 | `tests/ops/test_evidence_index.py` (`EPIC040_CHECK_IDS` L86, `EPIC040_TARGETS` L101, `test_evidence_index_has_required_epic040_artifacts` L333, `test_epic040_qa_roster_matches_canonical_bindings` L337) | Precedent owner tests for an Epic QA registration | `grep -n` |
| L-28 | `tools/qa/generate_epic_close_pack.py` (one `--source` and exactly one of `--write` or `--check`) and `schemas/close_candidate_source.v2.json` | Close-pack writer and source schema (CL-05; not run) | read |
| L-29 | `docs/pfcanon/PF02-Canon-HDE-Architecture-v*.md`, `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v*.md`, `docs/pfcanon/PF31-Reference-HDE-State-of-the-Repository-v*.md` | Versionless resolution patterns; each matches exactly one file today | `ls` count 1 each |
| L-30 | `The checked-in loader remains current repository reality until separately remediated`; `The non-BodyGraph loader responsibility represented by`; `still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging` | Exact canon text keys for DELTA-001, -002 and -003 | `grep -n -F` hits: HDE Architecture §1.1 (line 198), HDE Mechanics Guide §1.1 (line 179), HDE State of the Repository §2.2 (line 153) |

**L-31, the caller set (verbatim).** The command `git grep -l -E 'chart_orchestration|engine\.charts' -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/' ':(exclude).audit_src/'`, run at `1e2ac50e`, prints exactly these 11 paths, one per line, in this order:

1. `adapter/chart_orchestration.py`
2. `ci/checks/classify_ci_changes.py`
3. `engine/charts/pure.py`
4. `scripts/make_compat_determinism_artifacts.py`
5. `tests/adapter/test_chart_orchestration.py`
6. `tests/charts/test_chart_loader_import_guard.py`
7. `tests/charts/test_chart_pure_interface.py`
8. `tests/charts/test_chart_pure_purity.py`
9. `tests/loader/test_load_chart_fixture_only.py`
10. `tests/loader/test_loader_logs_keys_only.py`
11. `tests/scripts/test_make_compat_determinism_artifacts.py`

Without the `.audit_src/` exclusion the same search adds seven `.audit_src/` files, the historical captures R-03 keeps unchanged. In the 11 paths, `ci/checks/classify_ci_changes.py` holds owner-map strings only and `engine/charts/pure.py` names the entry in its docstring only; the importers are `adapter/chart_orchestration.py` (of `engine.charts.pure`), `scripts/make_compat_determinism_artifacts.py` (of the entry) and tests.

**Absences relied on (negative proofs, bounded to the search shown):** no `EPIC041` text in `tools/evidence/update_evidence_index.py` (`grep -n -i epic041`: no hit); no `hde-epic041` path and no `HDE-EPIC041` `epic_id` among the 653 rows of `docs/evidence/INDEX.json`; no `audit/qa/hde-epic041/`, `audit/docdeltas/hde-epic041_doc_deltas.md` or `audit/EPIC-041_*` file; no `docs/changes/GCFPE_PROMPT_PROVENANCE.md`; no tracked file outside `docs/` and the historical prefixes names `chart_orchestration` other than L-31 and `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `tests/retired_tests.md`; `Procfile` and `pyproject.toml` do not name it.

## 6. Requirement and acceptance coverage audit

| Objective | Delivered (observed) | Existing evidence QA binds | What QA must still establish | Gap class |
| :- | :- | :- | :- | :- |
| R-01 / AC-01 | L-01 owns SAFE_MODE read (log field only), clocks, correlation id, pinned-list reads and the keys-only log line; no acquisition exists, so the resolver clause is vacuous (Reality Audit E-018, N-004) | Exact-head CI of #791 and #796 ran L-05, L-10, L-11 | Governed functional proof of the adapter-to-engine seam at the QA execution source; a supported path for each supported use (C-1 to C-3) | Evidence gap |
| R-02 / AC-02 | L-02 imports only `re`, `unicodedata`, `typing`; typed `ChartInputError` refusals in the loader's order | Same CI; section 4.7 | Governed purity and interface proof at the QA source | Evidence gap |
| R-03 / AC-03 | L-03 absent; guard passes; C-1 to C-3 migrated; inventory 69 files with dispositions (Reality Audit §12.4); historical captures unchanged (section 3) | #796 CI; PR diffs (GitHub); section 3 | Governed guard, generator and caller results; a governed record of the current caller set at the QA source (L-31) | Evidence gap |
| R-04 / AC-04 | Positive and negative tests exist and are CI-owner-registered (L-22) | Exact-head CI runs | The checks pass "with actual commands, configuration, tested-source identity, results, responsible actor, time and limitations recorded" in governed evidence, and the governed evidence is indexed by the authorized writer | Evidence and indexing gap (G-OBS-01) |
| AC-05 | Compat bytes, `artifacts/logs/loader_call.jsonl`, release membership and historical captures unchanged (section 3); C-1 writes nothing; entry writes no file | PR diffs; CI clean-tree gates (ci.yml L129 to L130) at the PR heads | Governed proof that running the covering tests at the QA source leaves tracked files unchanged; retained coverage passes | Evidence gap |
| Specification §4 items 3 to 5 | Not met (section 9) | Implementation Audit §6; QA10-OBS-07 | Confirmation at the QA source that no new reach exists | Plan-validity precondition |
| Specification §8 and §6 D4 | No governed evidence exists (L-23 absences) | None | Governed evidence by canonical tools, indexed by L-16, tested source distinct from evidence-storage commit | Evidence and indexing gap |
| Specification §9 | Live QA required for eventual close | None | The executed Live QA stage with D0 and a QA RCA & Doc Delta summary | QA stage |
| Specification §10 | Doc-delta surfaces absent | None | Step-0B pair; the close pack is CL-05's | QA Step-0B; CL-05 |
| TI-01 to TI-07 | TI-01, TI-03 to TI-06 closed; TI-02 open advisory (Product Owner); TI-07/CCR-1 open for CL-05 | Readiness §4.4 | Final QA Report carries each state; QA adds no work for TI-02 or TI-07 | Carried |

No objective is shown unmet and no product defect was found.

## 7. Testability and integration seams

| Id | Seam or risk | Audit assessment | Effect on the Plan |
| :- | :- | :- | :- |
| IR-01 | Purity proof covers only patched entry points | Bounded by deny-lists; observed import closure is standard library only (section 4.7). An allow-list check would be a newly written decisive evaluator, which Glow QA Guide §3.4.8 forbids in a plan | Limitation carried to the Final QA Report; no QA-created evaluator (QA50-F06) |
| IR-02 | Guard misses run-time-assembled names and untracked files | Confirmed by probe (section 4.6); a missing module fails at import anyway; untracked files are not supported callers | Limitation carried; the real-tree negative probe is not planned (section 8.3) |
| IR-03 | C-1 exit 2 depends on `compat_public` absence | Confirmed: 0 chart calls | L-09 covers it; restoring compat is out of scope |
| IR-04 | `ensure_cid` lives in `engine/util/input_validators.py` | Entry-only use; L-05's `test_validation_does_not_depend_on_the_working_directory` and `test_default_sink_is_the_module_logger_and_writes_no_file` cover a foreign working directory | Covered by the entry check |
| IR-05 | Clock-derived `ts` in the log line | L-05's `test_log_line_is_keys_only` removes `ts` before the substring check | No QA string check on log text |
| IR-06 | Canon still describes the removed loader | Confirmed (L-30) | Step-0B DELTA-001 to -003; QA tests the delivered boundary |
| IR-07 | Indexing needs a writer change outside the QA root | Confirmed (section 10) | Routed work item and dependency in the Plan |
| IR-08 | `main` push CI red | Cause path deleted (QA50-F09); a QA pull request classifies only its own paths | Read the landing pull request's exact-head CI |
| IR-09 | Local Python differs from CI | Python 3.12 with CI's install proven (section 4.1) | Environment contract in the Plan |
| IR-10 | A run that writes a tracked file | None observed | A dedicated tracked-file predicate after the covering runs |
| IR-11 (new) | Editable install binds `adapter` and `engine` to the clone it was installed from (section 4.1) | A virtual environment installed from another clone would test that clone's code | The Plan requires installing from the execution clone and D0 records `pip list` |
| IR-12 (new) | `orientation_demo.py` without `--check` writes | Observed (section 4.5) | The Plan uses only `--check` in validation |

## 8. Evidence sufficiency against CI and PR evidence

### 8.1 What bound evidence proves

| Id | Evidence | Proves | Does not prove |
| :- | :- | :- | :- |
| BE-01 | #791 exact-head CI run 40723983402 (`success`) on `815fd5b2` | All seven lanes and the changed tests passed on WU-PR-01's head | WU-PR-02 code; anything at a later source; governed evidence |
| BE-02 | #796 exact-head CI run 40774524113 (`success`) on `8200d1fb`, the code tree of `9843934f` and of `1e2ac50e` | All seven lanes, including the changed-tests lane for WU-PR-02's diff (the guard, the generator test and the migrated callers), passed on the delivered code under closed rails, with a clean tree | A governed, indexed record with tested-source identity, actor and limitations; the QA execution source |
| BE-03 | GitHub diffs of #791, #796 and #800 | Compat artifacts, `artifacts/logs/loader_call.jsonl`, `catalog/manifest.json` and `.audit_src/` untouched; the 16-path change set | Behavior |
| BE-04 | WU-PR-02 lineage review focused run (56 passed at `9843934f`, both retained-coverage tests included) and Reality Audit E-036 (13 of 13 call shapes equal against the removed loader) | Preservation against the removed loader, which can no longer run | Governed evidence; current-source behavior |
| BE-05 | Owner registration in L-22 (L612 to L620) | CI reruns the change's tests when their owners change | That they pass now |

### 8.2 The gap QA closes

Change Process Guide §3.5.2.8 requires every Epic to complete Live QA through a QA harness that "produces governed evidence", including a functional proof step for changed adapter-to-engine behavior, and states that "CI tests MUST NOT be treated as a source of governed evidence". PF09.3 HDE-SEPA006.3 and Specification §8 require "actual commands, configuration, tested-source identity, results, responsible actor, time, and limitations; and required indexing through the existing governed writer". No bound record supplies that: CI results are hosted logs tied to PR heads, not governed repository evidence, and none is indexed. Each QA check therefore re-executes CI-registered tests through the tracked harness at the QA execution source **only** to produce that governed, indexed receipt, and binds BE-01 to BE-05 for everything else. Each Plan check states its specific addition.

### 8.3 Checks considered and excluded (not "for good measure")

| Candidate | Why excluded |
| :- | :- |
| Real-tree guard negative probe (planted tracked importer) | The guard already proves a non-empty scan (`LIVE_CALLERS` subset) and every import form (`test_checker_flags_every_import_form`); the probe would need a VCS mutation (`git add` in a worktree), which Plan Templates forbids in QA execution |
| Import-closure allow-list for `engine.charts.pure` | A newly written decisive evaluator; the delivered fresh-import harness already decides purity at import |
| Direct C-1 run with an asserting wrapper | L-09 runs the same script as a subprocess from a temporary directory and asserts exit, streams and no write; a second run adds no proof |
| Output equality against the removed loader | Cannot run without restoring removed code; bound as BE-04 |
| Historical-capture and compat-byte diff | GitHub records it reliably (BE-03) |
| Full repository suite or other CI lanes | Not tied to this change's surfaces; CI's applicability classification already selected the lanes for each PR |
| Acceptance-map viability check | No acceptance map exists before CL-05; CCR-1 places it in the close pack; the v2 close-pack source has no acceptance-map field (QA50-F10) |

## 9. Open-rails determination (QR-03)

**Carried verbatim** (Specification v1.1 §4; Plan v1.1 §11):

* **Item 3.** "*Binding condition.* If the Implementation Audit finds that any affected surface, including the new orchestration entry, is used to produce such a feature, or reaches vendor acquisition in a deployed or CLI path, the mandatory bounded live vendor test (synthetic data only, `SAFE_MODE=0`, `ALLOW_NETWORK=1`) applies to this Epic's QA Plan. No exemption or non-vendor substitute then applies. Closed-rails proof, static validation, repository inspection, generated evidence, an OPS observation or exemption language does not replace it."
* **Item 4.** "*Broader scope.* This Specification records no exemption from the broader production-affecting open-rails requirement. If the Implementation Audit finds the changed boundary can affect runtime compute, vendor ingest, database retrieval or production-used CLI/API behavior, the QA Plan must carry a bounded open-rails step or an exemption authorized and recorded under the Product Owner. Silence is not an exemption."
* **Item 5.** "*Authorization.* The row authorizes no live vendor or production database activity. Any live step needs separate, task-specific Product Owner authorization (§9)."

**Evidence at `1e2ac50e`.** The production entry points are `Procfile` `web` (`adapter.factory:create_app()`) and the console script `hdctl = "engine.cli.main:cli"` (L-25). The only modules importing L-01 are L-04 and tests; the only module importing L-02 is L-01 (L-31; `git grep` over all tracked files, including string forms). Neither production entry names, imports or dynamically loads either module, and L-01 acquires nothing from a vendor or database (Reality Audit E-018).

**Determination: neither item 3 nor item 4 is met.** HDE Governance §3.4 "Production-functional epic live-proof requirement" and "Other production-affecting scope" do not attach; no open-rails step is required and no exemption is needed, because the scope is affirmatively determined, not left silent. CCR-3 stays not triggered. **Re-attachment:** if the QA execution source shows any change to L-31, the determination no longer holds for it; the Plan's D0 check blocks execution in that case and Kronos re-determines, and a live step would then need separate, task-specific Product Owner authorization. This Audit authorizes no live step.

## 10. Evidence publication and indexing audit (QR-04, G-OBS-01)

### 10.1 G-OBS-01 confirmed

L-16 builds Human Index rows only from rows already in L-23, the CRD-only `ADMITTED_CRD_QA` table, source-owned per-change lists (the QA lists are `EPIC039_QA_PRIMARY_ARTIFACTS` and `EPIC040_QA_PRIMARY_ARTIFACTS`), conditional loaders and `--epic-id HDE-EPIC020`. It never enumerates a QA root (HDE Schemas and Artifacts §8.17: tools "MUST NOT infer run state by enumerating subdirectories"). `--epic-id HDE-EPIC041` is accepted and does nothing (`--check --epic-id HDE-EPIC041` exits 0). Unlisted QA files are invisible to `--check`. Indexing HDE-EPIC041 QA evidence therefore needs a source change to L-16 that lists it.

### 10.2 Ordering constraint

A static list cannot merge before its files exist: with the list and no files, `--check` exits 1 `STALE:<root>/docs/evidence/INDEX.json` and write mode fails `FileNotFoundError` and rolls back (observed in a throwaway worktree). CI's evidence lane runs `--check` first (ci.yml L227).

### 10.3 Landing routes against canon

| Route | Shape | Canon fit | Precedent |
| :- | :- | :- | :- |
| A | One pull request carries the QA evidence, the L-16 list with an owner test, and the writer's regenerated Index, Mirror, sentinels, orientation and proofs | Satisfies the same-mutation-set parity rule (Change Process Guide §3.5.2.8). Carries tooling code, which Change Process Guide §0.7 does not list for an evidence-only QA PR, so it needs a recorded Product Owner route decision | HDE-EPIC040 #559 under Lead Dev decision D-3, which logged the same gap as CC-3 |
| B | Evidence lands unindexed; a later pull request adds the list and regenerates the Index | Breaks the parity rule ("the index and mirror trio updates in the same authorized mutation set") | HDE-EPIC039 (direct commits) |
| C | A writer pull request first adds a presence-gated, fail-closed registration and its test; then an evidence-only QA PR carries the evidence and the regenerated Index | Canon-conformant: tooling lands by the normal PR route, and the evidence PR keeps parity | None |

Route B is not planned. The canon gap behind A is CCR-6 (QA50-F03).

### 10.4 Feasibility proof (throwaway; not QA)

In a throwaway clone at `1e2ac50e`, Kronos ran the companion Plan's exact command snippets and scripts, extracted mechanically from the final Plan file, end to end (QA Plan section 9.4): all seven checks recorded `PASS`; every primary, sidecar, doc-delta file and the manifest received a capture-time path proof that verified; after the Plan's worked rerun example, `qa-closeout-deliverables` verified 16 proofs. Adding an `EPIC041_QA_PRIMARY_ARTIFACTS` list built by the Plan's registration rule (16 entries, including the two rerun files) spliced after `*EPIC040_QA_PRIMARY_ARTIFACTS,` and running the writer in write mode took the Index from 653 to 669 rows (16 with `epic_id` `HDE-EPIC041`); `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh` and `check_lf_endings.py` all exited 0, and an earlier rehearsal with the same writer showed it keeps the QA-written proofs (their `produced_at_utc` stays the capture time). Negative rehearsals with the final scripts classified as designed: a tracked modification before D0 gave `TOOLING_BLOCKED` ("tracked files are modified before QA"); a tracked modification before the tracked-file check gave `FAIL_BEHAVIOR`. Everything was discarded and the clone returned to a clean `1e2ac50e`.

### 10.5 Harness, proofs and close-pack facts

* `HarnessConfig("HDE-EPIC041")` needs no registration; `run_pytest_check` admits only selectors, `-q`, `--quiet`, `--collect-only`, `-p no:cacheprovider`, `-k EXPR` and `-m EXPR` (other options give `TOOLING_BLOCKED` unexecuted) and maps exit 0 to `PASS`, 1 to `FAIL_BEHAVIOR`, 5 to `TOOLING_BLOCKED` and 2, 3, 4 or negative to `FAIL_TOOLING`; `record_check` writes `checks/<check_id>/primary.log` with a `pf27.step_log_header.v2` header and the flat manifest `{check_id: {check_id, log_path, status}}`, and writes no path proof; `PASS` requires exit 0.
* The harness's fixed `pf_refs` (`PF14-Canon-HDE-Mechanics-Guide`, `PF19-Canon-Glow-QA-Guide`, `PF27-Canon-Plan-Templates`) are the exact in-document **Title** values of those documents, with no file name, version or digest, so they conform to HDE Build Notes' rule that canon is cited by title.
* A new proof written by the writer itself takes `produced_at_utc` from the Mirror proof's prior value (`2026-09-22T14:25:29Z` today), earlier than the capture; writing proofs at capture time with `_refresh_path_proof` (the HDE-EPIC039 and HDE-EPIC040 practice; HDE-EPIC040 QA-70 decision C040-09) avoids that, and the writer keeps a matching proof.
* The v2 close-pack writer (L-28) derives the close-pack paths `audit/EPIC-041_close_report.md` and `audit/EPIC-041_MANIFEST.json` and the supporting paths `audit/docdeltas/hde-epic041_doc_deltas.md`, `audit/docdeltas/hde-epic041_drain_targets.md` and `audit/qa/hde-epic041/qa_step_logs_manifest.json` from the change id. It consumes the harness manifest and primaries as tracked bytes, requires the doc-delta file to state `Doc Deltas: None` or list items (never both) and the `00_meta` copy to be the same git blob, takes the QA RCA as summary lines or `audit/EPIC-041_QA_RCA.md`, takes the check-to-requirement mapping as source text, and refuses Index, Mirror, proofs and anything under `docs/ephemeral/` or `docs/pfcanon/` as inputs. It runs only at close.

## 11. Dependencies, risks, data and permissions

| Id | Risk | Likelihood and effect | Treatment in the Plan |
| :- | :- | :- | :- |
| RK-QA-01 | Writer registration (IDX-01) not authored or not approved | Evidence lands unindexed; HDE-SEPA006.3 indexing stays unmet | Explicit dependency and Product Owner inputs; QA-110 treats missing indexing as incomplete, never PASS |
| RK-QA-02 | `main` moves between approval and execution | Audit facts may not hold | D0 records the source and re-checks L-31; no SHA-equality predicate |
| RK-QA-03 | Wrong-clone editable install (IR-11) | Tests another clone's code | Environment contract; D0 records `pip list` |
| RK-QA-04 | Evidence left in a working tree | Violates persistence | Landing route named; evidence stays unchanged until the landing PR carries it |
| RK-QA-05 | A rerun overwrites the first receipt | Lost attempt lineage | Preservation snippet copies attempt-1 files before any rerun |
| RK-QA-06 | Doc-delta text binding a planning path | HDE Build Notes nonconformance | Step-0B and closeout predicates reject `docs/ephemeral` and `docs/pfcanon` strings in the pair |

**Data.** Synthetic inputs only (the fixture chart and synthetic birth tuples in the delivered tests); no person, user, production, database, cache or vendor data. **Secrets.** None needed; no vendor key, base URL or credential is read; probes record environment names only. **Permissions.** QA execution writes only under `audit/qa/hde-epic041/` and `audit/docdeltas/hde-epic041_doc_deltas.md` plus `/tmp` scratch; the writer run, branch, commit, push and pull request belong to the separately authorized landing lane; Nathan alone merges.

## 12. Findings (classified, with owners)

| Id | Finding | Class | Evidence | Owner and route |
| :- | :- | :- | :- | :- |
| QA50-F01 | No governed HDE-EPIC041 evidence exists; Live QA must produce it through the harness | Test/evidence gap (expected before QA) | Section 5 absences; section 8.2 | Kronos plans (companion Plan); QA execution under the Product Owner's arrangement; QA-110 |
| QA50-F02 | The authorized writer cannot index HDE-EPIC041 QA evidence without a source change (G-OBS-01 confirmed) | Tooling gap outside the QA root (not Moon Loop) | Section 10.1 to 10.2 | No lawful PR implementation author exists for it (WU-PR-01 to -03 are merged and accepted); the assignment and route return to the Product Owner. The Plan specifies the registration set and dependency (IDX-01) |
| QA50-F03 | No canon landing route covers QA evidence plus the writer registration it needs; Change Process Guide §0.7's allowed-change list omits QA-root artifacts and evidence tooling | Canon reconciliation gap | Section 10.3; HDE-EPIC040 D-3 (CC-3) | CCR-6, PROPOSED; Isis for the QA Plan route at QA-70; Product Owner for the route decision and any canon change |
| QA50-F04 | `pytest.ini` `testpaths` omits five change test files | Observation (CI selects them through owner registration; QA names them) | Section 4.2 | No work proposed; Product Owner may note it |
| QA50-F05 | The guard scans tracked files only and does not resolve run-time-assembled names | Bounded proof limit (IR-02) | Section 4.6 | Carried to the Final QA Report as a limitation |
| QA50-F06 | Purity proof is deny-list based; `os` loads transitively through the standard library | Bounded proof limit (IR-01) | Section 4.7 | Carried as a limitation |
| QA50-F07 | HDE Build Notes v13.9.4's Addendum Index lists four addenda while the body holds five | Canon hygiene observation | `PF10-HDE-Build-Notes-v13.9.4.md` lines 184 to 191 against 742 | Product Owner; non-gating; not a QA deliverable |
| QA50-F08 | The Guide and the QA-10 records cite the superseded PF10 file v13.9.3 | Provenance only | Section 2 | No effect |
| QA50-F09 | The `cline_skills/` paths that stopped `main` push classification (E-035) were deleted by `b67056ef`; later hosted push results were not read | Observation (QR-07) | Section 2 | Product Owner |
| QA50-F10 | The v2 close-pack source has no acceptance-map field, while Specification §10 lists an acceptance map (CCR-1, TI-07) | Close-stage observation | Section 10.5 | CL-05; Product Owner |

No product defect, Plan defect, Specification ambiguity that blocks planning, or authority conflict that blocks planning was found.

## 13. Carried obligations and where they land

| Id | Obligation | Lands in |
| :- | :- | :- |
| QR-01 | Independent verification of R-01 to R-04, AC-01 to AC-05 under closed rails | Plan checks `ac01-orchestration-entry`, `ac02-pure-module`, `ac03-caller-migration`, `ac05-tracked-files-unchanged` |
| QR-02 | C-1 exit 2, no file, temporary working directory, CI's install | `ac03-caller-migration` (L-09), environment contract |
| QR-03 | Items 3 to 5 verbatim; determination; re-attachment | Section 9; Plan section 3 and D0 |
| QR-04, G-OBS-01 | Governed evidence through the authorized writer; parity; read-only validation; HDE Build Notes R-1 and R-2 | Plan sections 8, 12 and 13 (IDX-01, IDX-RUN, EL-01) |
| QR-05 | Step-0B DELTA-001 to -003; drainage after QA | `step-0b-doc-delta-capture` |
| QR-06 | Canon drift is not the contract | Plan scope statement |
| QR-07 | `main` push CI | Product Owner (QA50-F09) |
| QR-08 | FND-005 to FND-007 out of scope | Plan exclusions |
| QR-09 | Close mutation set at CL-05; CCR-5 ruling first | Plan section 18; not QA |
| QR-10 | Environment facts | Plan section 6 |
| QR-11 | PF09.3 rows stay Not done until the post-closure update | Plan section 20 |
| QR-12 | TI-02; OBS-9; PR35-LINK; QA10-OBS-14; prompt-use persistence PENDING | Carried; Product Owner, CI tooling owner, GCFPE management |
| HDE Build Notes WU-PR-01 and WU-PR-02 deferred obligations | OBS-4, AUD-CORR-1 met; OBS-1 and FND-005 to -007 persist out of scope; DELTA-001 and -002 carried | Step-0B; Final QA Report |

## 14. Result

**State: `AUDIT_COMPLETE`.** The Audit supports planning; the companion QA Plan is authored in this invocation (QA-60 is not inserted). Unresolved items and owners: IDX-01 authorship and route (Product Owner), CCR-5 and CCR-6 (Product Owner; Isis for the Plan's route at QA-70), QR-07 (Product Owner), prompt-use persistence (GCFPE management).

## Nonclaims

This Audit is authored process material. It is not QA, QA execution, a QA verdict, a QA Plan, readiness, acceptance of HDE-EPIC041, Ops, deployment, release, a canon change, a PF10 addendum, PF23 publication, PF09 or board movement, or closure. Its local runs were throwaway observations. It edits no file outside `docs/ephemeral/`. Merging it preserves the record and approves nothing (D21-C).
