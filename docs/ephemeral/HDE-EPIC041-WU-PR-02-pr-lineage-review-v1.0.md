---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_version: "1.0"
logical_id: HDE-EPIC041-WU-PR-02-PR-WORK-UNIT-LINEAGE-REVIEW
decision: ACCEPT
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-02
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-instruction-v1.0.md (v1.0; blob 52faaba5d08857c2cdc391c95360a716260dc187)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0.md (v1.0; blob 9883d7ae5c27cf76594d935d38e762c21d5c9458; with its companion docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff, blob e55a745427ef14c397c0700d4ea24f136ae96227, sha256 70ebf3a3d3b96debcc93e41512cf5798c4e39b8e111bdd4f797e211f7e49d565)
PR30_RESULT_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED)
PR35_RESULT_ID: docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-result-v1.1.md (MERGE_PENDING on 3dee9885; historical pre-merge evidence)
PR_REFS: [amthorn78/glow-hdengine-v2#796]
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1, approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0; corrected for later stages by AUD-CORR-1 in docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md §10)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
DEPENDENCY_REF: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-lineage-review-v1.0.md (PR-40 ACCEPT of WU-PR-01)
entry: Nathan's manual-merge assertion for #796, through the conditional PR-40 block of PR-35 result v1.1 ("Use only after Nathan has manually merged amthorn78/glow-hdengine-v2#796, and only if no MERGE_OBSERVED result was returned for that merge"). No MERGE_OBSERVED result was supplied. The merged state is verified independently (§2)
reviewer: the designated PR reviewer for WU-PR-02, run in the whole-change IA context for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj). This context authored the Audit, Plan and PR instruction. It authored none of the PR-20 plan, the code, the tests or the PR-30/PR-35 results
pr_sessions: PR-20/PR-30 https://claude.ai/code/session_01Q789u2FkMeZpy3U2W5XTh9; PR-35 https://claude.ai/code/session_01Q789u2MpERK4PwJNcd7ex1
prompt: PR-40 — Review PR Work-Unit Lineage — 102726.1 (https://app.notion.com/p/4064590a05eb81479a74fa542b90cadb; page state 2026-10-27T13:18:21.343Z, read in full)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head_reviewed: origin/main 9843934f276f5c17be499a6a565bf82fa7a84e26 (the squash merge of #796; nothing after it)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.2.md (661 lines, sha256 2a43e518f13219569ee3de74f544af9c176a648c8f40c926673671fae164c213; read in full during PR-10 for this unit; unchanged on main since 9f681bdf; addenda 2.2 and 2.3 re-read for this review; provenance)
pf10_addendum_created: none (PR-40 is not an addendum producer)
return_owner: the whole-change IA for HDE-EPIC041 (Plan progress)
next_stage: DOC-10 — Create Final Repository Documentation PR Instructions — 102726.1, for WU-PR-03 (§11)
reviewed_at: 2026-10-28 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-PR40-WU-PR-02-20261028
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: WU-PR-02
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: PR-40 — 102726.1 (https://app.notion.com/p/4064590a05eb81479a74fa542b90cadb), revision as of 2026-10-27T13:18:21.343Z
    role_stage: designated PR reviewer / GCF-17.LINEAGE
    captured_at: 2026-10-28
    runtime_identity: https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj
    inherited_usage: HDE-EPIC041-PR10-WU-PR-02-20261028; HDE-EPIC041-PR20-WU-PR-02-20261028; the PR-30 and PR-35 entries of results v1.0 §9 and v1.1 §12
    result_references: "#796; squash 9843934f; final reviewed head 8200d1fb"
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md; owner GCFPE management; non-gating)
---

# HDE-EPIC041 WU-PR-02 — PR work-unit lineage review v1.0 (PR-40): ACCEPT

## 1. Decision

**ACCEPT.** WU-PR-02 is delivered completely, and the delivery is attributable to its ordered lineage, which is the one PR, amthorn78/glow-hdengine-v2#796.

* #796 is merged. Its squash commit `9843934f` has the same tree as the final reviewed and CI-verified head `8200d1fb` (§2, §3).
* The landed code and tests are byte-identical to the plan's companion diff. No change was made after the plan (§6).
* Every obligation of the PR instruction is met by the landed code and tests (§4).
* Codex found nothing on any head. There is no finding, open thread or P1 (§5).
* The business-case measure is met (§7). Under HDE Governance §9.7.7 the work unit stops.

ACCEPT is not QA, Ops, release, acceptance of the Epic or closure. It returns WU-PR-02 to the whole-change IA for Plan progress. The next stage is WU-PR-03 through DOC-10 (§11).

## 2. Merge state and PR evidence

| Item | Evidence |
| :- | :- |
| PR | #796, `state: closed`, `merged: true`, `merged_at` 2026-10-28T22:06:58Z, `merged_by` amthorn78 (GitHub) |
| Base | `main` `abcc13f33e5cf56128bd27c6d1229373f1ec6b31` (#795, the plan's documents PR) |
| Final reviewed head | `8200d1fbbad65d65a021e94f52bc73b2784069bf` (the v1.1 record's commit) |
| Landing | squash commit `9843934f276f5c17be499a6a565bf82fa7a84e26`, sole parent `abcc13f3` |
| Trees | `9843934f^{tree}` = `8200d1fb^{tree}` = `1c30cc4b257942bd184e5fd12e98c79fe6f4a0b5` |
| Later divergence on `main` | none: `origin/main` = `9843934f` at review time |
| PR commits, in order | `cc287d8d` (implementation, PR-30; the tested source); `3dee9885` (result v1.0); `8200d1fb` (result v1.1, PR-35) |
| Code since the instruction's baseline | `git diff --stat d09de6ea abcc13f3 -- . ':!docs/ephemeral/'` is empty, so the plan's prototype base and the PR's base are the same outside `docs/ephemeral/` |
| Merge-order dependency | none. #795 merged first, as the plan required (§10 of the plan) |

## 3. Reviews and CI

* **Codex code review.** It ran on each head carrying new commits. The summary comment (6480113837) reads `code_review {commit_sha: 8200d1fb…, has_any_findings: false, has_unresolved_findings: false, status: completed}`, completed 2026-10-28T21:46:07Z. On `3dee9885` it also completed with no findings (20:39:36Z, result v1.1 §4). Formal reviews: none. Inline threads: none (`totalCount: 0`).
* **Security review.** Not run. Neither the instruction nor the repository instructions require one for this change. It adds no route, credential, flag, network or environment gate, and it removes a provider-resolution path (plan §14). No security finding exists.
* **Exact-head CI on `8200d1fb`.** Check run 123120191675 (run 40774524113), `test`, `success`, 21:45:13Z to 22:04:52Z. All seven lanes ran and succeeded (`PRODUCT`, `COMPAT`, `DB`, `RAILS`, `EVIDENCE`, `QA`, `RELEASE`, each `true` with outcome `success`), and the log ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The earlier head `3dee9885` also passed (run 40765095607, check run 123087714366). The run on `cc287d8d` was cancelled when `3dee9885` superseded it, by the workflow's pull-request cancellation. No waiver was used, and none exists for HDE-EPIC041.
* **Post-merge `main` push run on `9843934f`.** Run 40777435776 is recorded in §12 as it stood when this record was committed. It is not an acceptance predicate, because the pre-merge exact-head run on the identical tree passed.
* **Local corroboration by this reviewer.** All runs used closed rails through `env -i` (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), a CPython 3.13.17 scratch venv with CI's install, and `9843934f`.
  * Focused set, 22:11:21Z to 22:11:28Z: `tests/charts`, `tests/adapter/test_chart_orchestration.py`, `tests/loader`, `tests/scripts/test_make_compat_determinism_artifacts.py`, `tests/core/test_engine_core_purity.py` and the two PF09.3 retained-coverage tests. **56 passed.** `git status --porcelain --untracked-files=all` was empty afterwards.
  * C-1 from a new temporary directory: exit 2, stderr `compat_public not implemented`, stdout empty, directory empty.
  * Guard negative probes, in a throwaway clone at `9843934f` that was deleted afterwards. The clean guard passes 4 of 4. Each planted case fails 1 of 4:
    * `importlib.import_module("engine.charts.loader")` appended to a tracked test fails `test_no_tracked_python_file_imports_the_retired_loader`;
    * `from engine.charts import loader` appended to `adapter/chart_orchestration.py` fails the same test;
    * a tracked `engine/charts/loader.py` fails `test_the_retired_module_path_does_not_exist`.

  These local runs are not CI, QA or governed evidence.

## 4. Requirement coverage across the complete work unit

| Instruction obligation | Landed evidence | Result |
| :- | :- | :- |
| §3.1 C-1: change only the import and the chart call; exit 2, stderr and write logic unchanged | One line: `from adapter.chart_orchestration import load_chart`. `load_chart(**a)` is textually unchanged and resolves to the entry in the keyword form. The generator test and the local run (§3) show exit 2, the stderr, no stdout and no file | Met (ED-07; FND-005 untouched) |
| §3.1 C-2: the entry with an injected sink and `ChartInputError`; no `_Path` patch; both assertions kept in substance | `tests/loader/test_load_chart_fixture_only.py` calls the entry with `log_sink=lines.append`. It asserts the normalized fixture result, now `meta.provider == "fixtures"` (plan PD-3), and the tz-absent `READER_INVALID_INPUT` with field `tz`. Each test asserts one log line | Met; migrated in place (plan PD-1) |
| §3.1 C-3: the entry with an injected sink; must not carry OBS-4 | `tests/loader/test_loader_logs_keys_only.py` uses `log_sink=data.append`. `ts` is matched to `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$` and removed from the raw line before the substring check. Key, route, `safe_mode`, correlation-id and forbidden-list assertions are kept. PR-30's pinned-clock probe at 12:34:00Z passed (result v1.0) | Met; OBS-4 resolved |
| §3.1 C-4 and D-1: legacy signature retired with the module, no shim | `engine/charts/loader.py` deleted (173 lines); `git ls-tree -r 9843934f engine/charts/` lists only `engine/charts/pure.py` | Met |
| §3.1 characterization file deleted in the same commit | Deleted in `cc287d8d`; a `tests/retired_tests.md` row names `tests/adapter/test_chart_orchestration.py` as the replacing literal-value coverage | Met |
| I-1: `engine/charts/pure.py` unchanged; no `input_validators` import into a pure path | Not in the landed name-status. No changed file imports `engine.util.input_validators` | Met |
| I-2 and AC-01: no R-01 concern under `engine/charts/` | Only `pure.py` remains. The inventory (below) locates every R-01 concern for chart loading in `adapter/chart_orchestration.py` | Met |
| I-3: no acquisition, provider contract, fallback, route, flag, CLI option or release-member change | The landed name-status names no such path. No new import of a resolver, provider, vendor, HTTP or CLI module. Removing the loader removes its `{"gates":[1,2,3]}` fallback and its `resolve_provider` import. All nine code paths are not release members (result v1.0); admission stays `1.3.0`, 45 members | Met; CCR-3 not triggered |
| I-4: outputs and failures preserved | `artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt` at `9843934f`: blobs `7fe71f99…`, `7fe71f99…`, `7e6176a2…`, unchanged. C-1's behavior is unchanged (above). WU-PR-01's literal-value tests pass in the focused set. `TypeError` for legacy shapes is the only behavior, pinned by WU-PR-01's test | Met |
| I-5 and AC-05: clean tree | CI's clean-tree step passed on `8200d1fb`; the local runs left the tree clean (§3) | Met |
| I-6: historical captures, `loader_call.jsonl`, row 57, `input_validators`, `provider_loader`, `engine/provider*/` unchanged | None is in the landed name-status. `artifacts/logs/loader_call.jsonl` is blob `92556952…`. The old row 57 is byte-identical and now line 58, because the new row was inserted above it in path order (plan PD-10) | Met |
| I-7 (HDE Build Notes addendum 2.2, R-1 and R-2) | The guard lists files with `git ls-files -z -- '*.py' ':(exclude)docs/ephemeral/' ':(exclude)docs/pfcanon/'`, so it never lists or reads either tree. No landed code or test reads, binds or resolves a path under them, or names a PF file, version, digest or addendum number. Comments cite only HDE-EPIC041, the unit and HDE-SEPA006 (code read) | Conforms |
| §3.3 CI registration | `_PRODUCT_TEST_OWNER_PATHS`: the characterization file removed from both entries; `engine/charts/loader.py` → the guard; `scripts/make_compat_determinism_artifacts.py` → the generator test. `pytest.ini` and the roster are unchanged; C-2 and C-3 keep their registrations. Hosted classification selected all seven lanes and passed | Met |
| §4 bounded files and must-not-change list | The landed code paths are exactly the plan's nine. None of `engine/charts/pure.py`, `adapter/`, `engine/util/`, `engine/config/`, `engine/provider*/`, `catalog/`, `pytest.ini`, `.github/`, governed evidence, `artifacts/`, `audit/` or `docs/pfcanon/` changed. The other three `tests/loader/` files are unchanged | Met |
| §5 import guard: every import form, dynamic-string forms, `_call_legacy`, the path, a negative self-test, exclusions limited to self, synthetic sources and the named trees | `tests/charts/test_chart_loader_import_guard.py`, 4 tests. 18 planted forms plus an unparseable text are flagged; the real non-import forms are not. It skips only its own file, the classifier's `_HISTORICAL_PREFIXES` (imported from the classifier, so they cannot drift) and the two pathspec-excluded trees. A tracked `.py` that does not parse (`scripts/scratch.py`) is searched as text rather than excluded. The planted importers fail it (§3) | Met |
| §5 generator behavior test | `tests/scripts/test_make_compat_determinism_artifacts.py`: from `tmp_path`, `(returncode, stdout, stderr) == (2, "", "compat_public not implemented\n")` and an empty directory | Met |
| §5 compat bytes; retained coverage; clean tree | §3 and the I-4 row | Met |
| §5 reconciliation of R-01 to R-03 in the PR record | The PR description records the search, 66 files and their dispositions (plan §13.3), and "TI-06 is moot". This reviewer re-ran the search at `9843934f` and found 66 files: 22 live and 44 under the historical prefixes. Its member list matches plan §13.3, less the two removed files. The only Python matches outside the historical prefixes are the guard's own self-test strings and the purity test's planted source text | Met (AC-03, AC-04) |
| §5 AC-04 record | PR description "Checks run" and result v1.0 §4: commands, closed-rails configuration, tested-source `cc287d8d`, counts, actor, window 20:03Z to 20:36Z, and limitations | Met |
| §6 acceptance: exact-head CI green, no waiver | §3 | Met |
| §7 CI economy: one coherent push | One implementation push and two record pushes under `docs/ephemeral/`. No corrective push was needed | Met |
| §8 recovery and rescope | No `RESCOPE_REQUEST` and no in-flight decision (results v1.0 §5 and v1.1 §7) | Met |
| §9 ownership: PR-30 publication, then PR-35 in its own session; no agent merge | Two sessions as recorded; Nathan merged | Met |
| §10 CANON_CONFLICT_REGISTER carried | Carried unchanged through the plan and both results | Met (§9 here) |
| Plan v1.1 RK-02: migration and removal land together | One implementation commit, `cc287d8d` | Met |

Documentation: none was due in this unit (plan §8 Doc-Delta row). With the loader removed, HDE Architecture §1.1 and HDE Mechanics Guide §1.1 now describe a module that no longer exists. Those are the drainage targets DELTA-001 and DELTA-002, which Plan v1.1 assigns to WU-PR-03, carried in its PR description with no canon edit. The inventory at `9843934f` finds no `README.md`, `AGENTS.md`, `CHANGELOG.md` or non-canon `docs/` file naming the loader.

## 5. Findings and their dispositions

None. Codex raised no finding on `3dee9885` or `8200d1fb`, there are no review threads, and no P1 at any priority exists. No finding was declined.

**Coverage limitation (a stated limit, not a finding).** The guard recognizes the static and string forms listed in plan PD-6. It does not recognize a module name assembled at run time, code executed from a string, or an attribute chain through an imported parent package (for example `from engine import charts` then `charts.loader`). The plan §6 states this limit. At `9843934f` no tracked file outside the historical prefixes contains any of these forms (the inventory above). Any such form would also fail at import, because the module no longer exists.

## 6. Delivered code against the plan's companion diff

`git diff abcc13f3 9843934f -- . ':!docs/ephemeral/'` is **byte-identical** to `docs/ephemeral/HDE-EPIC041-WU-PR-02-pr-implementation-plan-v1.0-prototype.diff`: 572 lines, the same 9 files, +196 −274. The retired row's date is the prototype's 2026-10-28, which is the UTC date of `cc287d8d` (plan PD-10). PR-35 made no correction. The only other landed paths are the two result records under `docs/ephemeral/`.

## 7. Business-case measure (instruction §2)

**Met.**

* `engine/charts/loader.py` is absent: the guard's path test, and `git ls-tree`.
* The repository-wide import guard passes, and it fails on a planted importer: §3, and PR-30's probes on the base (result v1.0).
* C-1 still exits 2 with its stderr from a temporary CWD and writes nothing: the generator test, and the local run (§3).
* `artifacts/compat/*` bytes are unchanged: the blobs in §4.
* The retained-coverage tests named in PF09.3 pass: both are in the 56 of the focused set.
* `git status --porcelain` is empty after the covering tests: CI's clean-tree step, and the local runs.

The benefit WU-PR-01 deferred is realized. `engine/charts/` holds only `pure.py`, and the entry writes no file by default, so no supported run of the chart path can write the tracked `artifacts/logs/loader_call.jsonl`. WU-PR-02 stops.

## 8. Merged-change attribution

This section uses the `glow-merged-change-attribution-lock` skill (1.2.0, interface `GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3`, `SHADOW_VALIDATION`), in local Git mode.

* **Comparison.** The comparison ref is `origin/main`, pinned to `9843934f276f5c17be499a6a565bf82fa7a84e26`. The attributed change is `amthorn78/glow-hdengine-v2#796`, squash `9843934f` with pre-stage `abcc13f3`. The direct delta (base `abcc13f3` to head `8200d1fb`) and the landed delta (`abcc13f3` to `9843934f`) have the same SHA-256, `ffa0e971305edbf49d48df304033fa8dc170010e70e3ecbf104b8da1aeac400a`. Reconciliation: **EXACT**. Run key `auto-4df5fafb93c4f323829474dc`; stage-delta bundle SHA-256 `adeaad2ad1a3b988579c9d6d6b4d205a1089ba86927f9feb76aa9a7f89e0746f`.
* **Landed paths (11).**
  * `ci/checks/classify_ci_changes.py` (M);
  * `engine/charts/loader.py` (D);
  * `scripts/make_compat_determinism_artifacts.py` (M);
  * `tests/adapter/test_chart_orchestration_characterization.py` (D);
  * `tests/charts/test_chart_loader_import_guard.py` (A);
  * `tests/loader/test_load_chart_fixture_only.py` and `tests/loader/test_loader_logs_keys_only.py` (M);
  * `tests/retired_tests.md` (M);
  * `tests/scripts/test_make_compat_determinism_artifacts.py` (A);
  * the result records v1.0 and v1.1 under `docs/ephemeral/` (A).
* **Divergence.**
  * Later committed divergence: none (an empty delta from `9843934f` to the comparison SHA).
  * Worktree-only divergence: none (empty staged, unstaged and untracked deltas).
  * Interstage divergence: none.
* **Validator.** The attribution artifact validated (`status: PASS`, `eligible_as_validated_evidence: true`, no errors). Evidence-manifest SHA-256: `556187fc998c2da18666d027e6aaba1afe17c6f9889d983994c5705da171ed28`.
* **Unproven items.** None.
* **Shadow comparison.** The native review agrees with the skill's result: tree identity, parent topology, PR metadata and the byte-identical companion diff (§2, §6). There is no discrepancy.
* **Retention.** The artifact was task-scoped and is discarded after this review. It is not kept as a separate record.

## 9. CANON_CONFLICT_REGISTER (carried unchanged)

| ID | Status | Treatment at this review |
| :- | :- | :- |
| CCR-1 (acceptance map for tokenless work) | APPROVED, Thoth, CF-E-30 review v1.1 (Ruling R-A); confirmed by Isis IA-30 v1.1 | A close-pack matter for CL-05. Drainage: Product Owner |
| CCR-2 (Business Case content lists) | APPROVED, Thoth, review v1.1 | None |
| CCR-3 (S19 vendor decisions) | APPROVED as conditional, Thoth, review v1.1 | Not triggered. The landed change removes an import of `engine/config/provider_loader.resolve_provider`, which no S19 decision names, and adds no acquisition, route, evidence tool or gate row (§4, I-3) |
| CCR-4 (cited Build Notes loader record) | APPROVED, Thoth, review v1.1 | None |

No new entry. HDE Build Notes addenda 2.2 and 2.3 are current canon and conflict with neither approved base. The landed code conforms to 2.2 (§4, I-7). It meets every deferred obligation 2.3 assigns to WU-PR-02: OBS-4 (§4, C-3), AUD-CORR-1 (I-1) and the 2.2 bearing on the guard (I-7).

## 10. Observations carried to the IA for the next stage

None of these is a defect in WU-PR-02.

| ID | Observation | Owner and use |
| :- | :- | :- |
| DELTA-001, DELTA-002 | HDE Architecture §1.1 ("Non-BodyGraph chart loader classification") and HDE Mechanics Guide §1.1 (the loader seam posture and remediation paragraph) describe `engine/charts/loader.py` as current reality "until separately remediated". It is now removed (§4) | WU-PR-03: Doc-Delta notes in its PR description, with no canon edit (Plan v1.1 §6). Permanent drainage stays with its canon owner |
| SWEEP-1 | At `9843934f` the inventory finds no live `README.md`, `AGENTS.md`, `CHANGELOG.md` or non-canon `docs/` file naming the loader. The live non-code members are `artifacts/logs/loader_call.jsonl` (I-6) and historical captures and inventories (H-3) | DOC-10: input to WU-PR-03's sweep and measure. The sweep excludes `docs/pfcanon/`, `docs/ephemeral/` and the historical prefixes (Plan v1.1 §6) |
| PF10-2.2 | R-1 to R-3 apply to WU-PR-03: its CHANGELOG and docs may cite canon by title, but no code, test, tool, CI step or governed evidence may read, bind or resolve a planning document or a versioned PF file | DOC-10 and CL-05, as addendum 2.3 records |
| OBS-6 | `scripts/scratch.py` is a tracked `.py` file holding Markdown notes. The guard handles it (plan PD-7) | Product Owner, as repository hygiene; no change in this Epic |
| OBS-7 | With the classifier changed in the same push, deleting a still-registered owner test reports `CI_FULL_VALIDATION_TEST_INVALID` before `CI_REGISTERED_OWNER_TEST_DELETED`. Both fail closed | Record only |
| OBS-8, OBS-2, OBS-5 | Local-environment facts: `ruby` is at `/usr/local/bin` and must be on an `env -i` `PATH`; the container exports credentials, so use `env -i`; the clone may be shallow | Later sessions' surface advice |
| FND-005, FND-006, FND-007 | Unchanged: the generator's compat repair, the `input_validators` CWD and `TZ` reads, the stale architecture snapshot | CL-40 scan and the Product Owner |

## 11. Next approved Plan stage

* **Selected unit.** `WU-PR-03`, "Final repository documentation (GCF-19)", Plan v1.1 §6. The Plan orders the units WU-PR-01 → WU-PR-02 → WU-PR-03 and declares no Ops unit.
* **Dependency.** "WU-PR-02 merged and accepted." Merged: §2. Accepted: this record. WU-PR-01 was accepted by its own lineage review.
* **Lane.** WU-PR-03 is the final documentation unit, and no instruction exists for it. PR-40 routes "a final documentation unit without instructions" to DOC-10. It therefore goes to DOC-10 — Create Final Repository Documentation PR Instructions — 102726.1, run by the whole-change IA. DOC-10 records the normal lane: PR-20, Proceed, PR-30, PR-35, Nathan's merge, PR-40, then DOC-20 completion verification.
* **Per-PR base.** WU-PR-03's work is formed against a `main` that contains WU-PR-02, here `9843934f` or later.
* **Not reached.** QA-10 follows WU-PR-03's delivery and DOC-20 verification ("Initial delivery of WU-PR-03 completes before QA readiness", GCF-19).

## 12. Post-merge `main` run (as recorded at commit time)

* Run 40777435776 (`ci`, push, job 123130252296), on `9843934f`.
* Read at about 22:17Z, before this record was committed: **in progress**.
  * Steps 1 to 13 had concluded `success`: checkout of `9843934f`, classification, the AGENTS.md citation check, install, pytest readiness, the closed-environment check, isolated changed tests (22:07:18Z to 22:11:58Z), and the product, compatibility, database and rails lanes.
  * Step 14, the evidence lane, was running. Steps 15 to 17 (QA lane, release attestation, final applicability check) were pending.
* Its final conclusion is not recorded here and is not claimed. It does not bear on ACCEPT: the exact-head run on `8200d1fb`, whose tree is the same, passed every step (§3).
* If it ends red, the cause is a fact for its owner under the CI-red rules. It does not reopen this review unless it shows a defect in WU-PR-02's code.

## 13. TypeSafe reading and surface advice for DOC-10 (WU-PR-03)

* **Method.**
  * Installed TypeSafe scoring skill, request v8.2.
  * Script run once, session kind `authoring`, label "HDE-EPIC041 DOC-10 WU-PR-03 documentation PR instruction".
  * No Notion row written: this is an executing-flow session, and PR-40 writes only under `docs/ephemeral/`.
* **Action sent (v8.2).** "Create a final repository-documentation PR work-unit instruction for the third and last planned PR work unit of an approved whole-change Implementation Plan, after the first two units were merged and accepted: the unit adds one CHANGELOG section naming the two delivered units and their nonclaims, sweeps README, AGENTS.md and non-canon docs for any statement still describing one removed Python module as current, and carries two Doc-Delta drainage notes in its PR description without editing canon. Inputs are the approved Plan's unit scope and measure, the two accepted units' landed code and lineage reviews, and a repository rule that planning documents and versioned canon files are never code inputs. A written prompt with steps exists; no code is changed, no tests run and no live run against a provider occurs. A per-PR plan, the Product Owner's Proceed, implementation, independent PR review, a lineage review and a documentation-completion verification follow later in separate sessions."
* **Reading, as printed.** **TypeSafe v8.2: Sonnet 5.5 at medium.** Effort score 1.21 (confidence 0.79); rung probabilities low 0.05, medium 0.71, high 0.22, extra high 0.02, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.16, Sonnet 5.5 0.83, Haiku 5.5 0.01 (confidence 0.77). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.008, Opus 5.5 at medium 0.114, Opus 5.5 at high 0.035, Opus 5.5 at extra high 0.003, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.042, Sonnet 5.5 at medium 0.589, Sonnet 5.5 at high 0.183, Sonnet 5.5 at extra high 0.017, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.007, Haiku 5.5 at high 0.002, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T22:14:25Z. Nathan picks the cell.
* **Detail.** HTTP 200 in 0.64 s; 5534 input and 69 output tokens; jev-1.13.0. Rung by rule: medium; model by rule: Sonnet 5.5.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for DOC-10 (WU-PR-03) and none for this PR-40 session, so none is recorded.
* **Surface advice (DOC-10, WU-PR-03).**
  * Run it in the whole-change IA role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this review's pull request merges.
  * Read access is needed to `main`:
    * this review and the WU-PR-01 lineage review;
    * Plan v1.1 and its review, the Audit and Specification v1.1;
    * the WU-PR-01 and WU-PR-02 instructions, plans and results;
    * `docs/pfcanon/`, including HDE Build Notes, HDE Architecture §1.1 and HDE Mechanics Guide §1.1;
    * the delivered code (`adapter/chart_orchestration.py`, `engine/charts/pure.py`, `tests/charts/`, `tests/loader/`, `scripts/make_compat_determinism_artifacts.py`);
    * the documentation homes (`CHANGELOG.md`, `README.md`, `AGENTS.md`, non-canon `docs/`).
  * Write access is needed to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: code changes, test runs, open rails, or vendor, Railway, database or Notion writes.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` `9843934f`. The last `docs/pfcanon/` change is `9f681bdf` (HDE Build Notes v13.9.2); #795 and #796 change nothing there, and neither does this branch. Terms searched: HDE-SEPA006, chart loader, `engine/charts`, `charts/loader`, `resolve_provider`, purity, business case, PR review finding disposition, CI lane classification, final repository documentation, GCF-19, canon precedence.

| Title (file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.2.md`, the current controlled PF10) | Whole file, 661 lines, read in full during PR-10 for this unit and unchanged since. Addenda 2.2 ("Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close") and 2.3 (the WU-PR-01 lineage record, including "Deferred obligations and unresolved work") re-read in full for this review | §4 I-7 (R-1, R-2); §9 (2.3's deferred obligations met); §10 PF10-2.2. Addendum 2.1 (S19) not engaged (CCR-3) |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006; Subtasks .1 to .3 | Scope delivered (.2 migration, no import-path rename as migration, historical captures unchanged; .3 reconciliation); the two retained-coverage tests (§7) |
| HDE Architecture (`PF02-…-v2.4.7.md`) | §1.1 "Single homes" (Purity rule; Non-BodyGraph chart loader classification) | §4 I-1, I-2, AC-01; §10 DELTA-001 |
| HDE Mechanics Guide (`PF14-…-v3.5.9.md`) | §1.1 "BodyGraph and loader seam posture" and the remediation paragraph | §4 C-1 and I-3 (migrate generator callers; preserve outputs; no fallback, no Engine I/O exception, no second resolver); §10 DELTA-002 |
| HDE Governance (`PF04-…-v2.8.8.md`) | §9.7.7 "Business case for every requirement and work unit" (measure and stop rule); §9.1.1 | §7; author and reviewer lineage (front matter) |
| Change Process Guide (`PF06-…-v2.5.5.md`) | "PR review finding disposition (every pull request; real inputs only)" | §5: no finding; the coverage limitation rests on inputs not present on `main` |
| Plan Templates (`PF27-…-v2.0.6.md`) | "Review guardrails" (finding disposition, P1, repeated class); "Canon precedence for template use" | §5; precedence rule below |
| HDE CRD Records (`PF30.1-…-v0.9.2.md`) | The HDE-CRD-0002 record's "Phase blocks" section, including its closing paragraph on WU-DOC-01, "the final repository documentation unit" (lineage reviews `ACCEPT`; documentation completion `COMPLETE`) | §11: precedent that a final documentation unit has its own lineage review and completion verification |
| Specification v1.1, Implementation Audit v1.0, Plan v1.1 and review v1.1 (in-flight) | R-01, R-03, R-04, AC-01, AC-03 to AC-05; Audit §5, §8.1, §9; Plan §5, §6 (WU-PR-02 and WU-PR-03), §10; review v1.1 business-case rows | §4 coverage; §11 next unit and its lane |
| WU-PR-02 instruction v1.0, plan v1.0 with its companion diff, results v1.0 and v1.1 (in-flight) | Whole documents | §2 to §8 |
| WU-PR-01 lineage review v1.0 (in-flight) | Whole document | Dependency; OBS-4, AUD-CORR-1 and PF10-2.2 carried into this unit |
| PR-40 — Review PR Work-Unit Lineage — 102726.1 (Notion) | Whole page | Procedure, decision vocabulary, next-stage resolution ("a final documentation unit without instructions goes to DOC-10") |
| DOC-10 — Create Final Repository Documentation PR Instructions — 102726.1 (Notion) | Whole page (state 2026-10-27T13:19:44.974Z) | §11: the receiver's required inputs and lane |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Nonclaims

This review accepts WU-PR-02's delivery only. It is not a merge or merge request. It is not QA, Ops, deployment or release, and it does not accept HDE-EPIC041. It is not PF09 or board movement, a canon change, a PF10 addendum, or closure. It does not authorize WU-PR-03's implementation, which needs its own instruction, plan and Proceed. It does not edit any reviewed artifact. Merging this file preserves the record and approves nothing (D21-C).
