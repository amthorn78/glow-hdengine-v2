---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: PENDING
pending_on: RS-20 decision on docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md (RESCOPE_REQUEST v1.0, items RP-1 and RP-2)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 24597a31fbb910a4d36106a1aa2d5b861faec976; 54,620 bytes; landed on main at a8c99d1, amthorn78/glow-hdengine-v2#623)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c) — lineage only
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10)
effective_baseline: approved base + applicable PF10 overlays = the base above + NONE
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (v13.5.2; blob ec71eeecec8b0fcff1645d317211258bc708712c; sha256 c53dac75b7a6e7b7ed303c5b032e6d9a05a7285b89819104abd793bb1767222d; read in full; addendum 2.1 only, governing §21 only)
pf10_addendum_paths: none
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); this authoring ran in https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
author: dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
prompt_release: GCFPE-20261009.1 / 100926.1 / 55 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", read 2026-10-12)
created_at: 2026-10-12T22:36:44Z
repository_baseline: origin/main a8c99d11dccc0bdd844352515bd629efa8af5233 (git diff a429c7c..a8c99d1 outside docs/ephemeral/ is empty)
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry (§18)
companion_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md
next_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c), continuing whole-change IA session
---

# HDE-CRD-0002 WU-PR-01 — Detailed PR Implementation Plan v1.0

## 1. State and authority

**PENDING.** This is the complete planning draft for WU-PR-01. It plans 133 of the 135 uncovered test files, S04 and S05 in full, and it is executable for that part.

Two files cannot be given a disposition inside the approved bounds:
- `tests/evidence/test_hdapi_v2_contract_inventory.py` needs a change to two `tools/evidence/` files, which instruction §7 excludes (RP-1).
- `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` exposes a product defect in `engine/charts/loader.py`. Instruction §9.8 says its disposition waits on a route (RP-2).

Both go to the whole-change IA as one `RESCOPE_REQUEST` (`docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md`, RS-20). Acceptance (1) requires zero uncovered files, so the plan is not presented for Proceed until RS-20 decides: PR-20 §8 allows `AWAITING_PO_PROCEED` only for a complete, executable, approved-scope plan, and PR-20 "Same-owner correction" forbids a runnable PR-30 package while a decisive prerequisite is missing.

What this artifact does not do:
- It authorizes no implementation, commit outside its own artifacts, pull request for code, merge, Ops, QA, acceptance or closure.
- It is not held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.7.7). That hold, and Nathan's `PR Implementation Proceed`, apply to the successor v1.1 this session writes after RS-20 returns.
- It changes no canon and creates no PF10 addendum.

Resume point: on RS-20's decision, this same PR-20 planning context writes `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md`, a complete successor that applies the decision to RP-1 and RP-2 and leaves everything else as here. It then presents v1.1 at `AWAITING_PO_PROCEED`.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| `CHANGE_CLASS` / `CHANGE_ID` | `CRD` / `HDE-CRD-0002` |
| `WORK_UNIT_ID` | `WU-PR-01` — CI coverage of every test file; Distillation; S03, S04, S05 |
| `PR_INSTRUCTION_ID` | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md` (v1.0, `INSTRUCTION_READY`) |
| `IMPLEMENTATION_PLAN_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (v1.1; approved representation = the unchanged body plus `PLAN_REVIEW_ID`) |
| `PLAN_REVIEW_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (Isis, IA-30 `INITIAL_APPROVE`, `ASK OK.`, no addendum) |
| `SPECIFICATION_ID` | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (Thoth, CF-C-30 `INITIAL_APPROVE`) |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md` (lineage only) |
| `REMEDIATION_REVIEW_ID` | none |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md`, the unique current controlled PF10 (one unlettered document; addendum index `2.1` only, which governs TypeSafe readings). Silent on S03–S05, so permanent canon governs them (PF10 "Silence rule") |
| Active addenda | none |
| Effective baseline | approved base + applicable PF10 overlays = Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0, + NONE |
| Dependency state | Ready (instruction §3: "First. No upstream dependency"; no HDE-CRD-0002 unit has landed) |
| Predecessor attempts | none for this work unit (no earlier PR-20 artifact, branch, PR or Proceed exists; searched `docs/ephemeral/` and the open PR list) |

## 3. Sources

- **Inputs read in full:** the PR instruction v1.0. Plan v1.1 was read in full for §1–§7, §11–§17 and "Canon relied on", review v1.1 in full, and Specification v1.1 for the S03–S05 rows, the Exclusions, the Constraints and the Distillation phase row. The Audit was read for §3, §5.2, §5.3, §5.7, S03–S05 and §7.5.
- **Canon read on `main` at `a8c99d1`** (`docs/pfcanon/` unchanged since `df23bbf`, #614): listed with sections under "Canon relied on". PF10 was read in full.
- **Prompts read:** PR-20 (in full), PR-30 (in full, receiver contract), RS-10 (in full), RS-20 (in full), the hub `HDE IA — GCFPE-20261009.1 — 100926.1`, and the release register's current-selection section.
- **Repository read at `a8c99d1`:** `.github/workflows/ci.yml` (full), `ci/checks/classify_ci_changes.py` (full, 1,958 lines), `pytest.ini`, `tests/conftest.py`, `ci/jobs/*.yml`, `ci/checks/run_rails_job_definitions.py` lines 40–75, and `tests/evidence/test_rails_ci_workflow_integration.py` (lines 1–460, 800–920, 1051–1200 and every test name). `tests/evidence/test_http_reader_ci_ownership.py` was read in full; `adapter/app.py`, `adapter/wsgi.py` lines 1–60, `adapter/http_reader.py` route lines, `engine/charts/loader.py` lines 50–100 and `tools/evidence/hdapi_v2_boundary_analyzer.py` lines 1791–1861 were read in part.
- **Planning workers.** Eight read-only workers diagnosed the 135 files in throwaway clones. Each worked under the same closed rails with credentials stripped and restored its clone after every prototype; none wrote to the repository. Their per-file evidence is carried in §7 and §16. The two decisive facts behind RP-1 were re-verified by this session (§4.4).
- **External:** GitHub, "Workflow syntax for GitHub Actions" (path filters: "`**`: Matches zero or more of any character"; `!` patterns in `paths`; ordered evaluation; "When all the path names match patterns in `paths-ignore`, the workflow will not run") and `actions/runner-images` `Ubuntu2404-Readme.md` (image 20261004.327.1: "Ruby 3.2.3").

## 4. Repository baseline (re-verified at `a8c99d1`)

### 4.1 Inventory

Recomputed read-only at `a8c99d1` by the §5.1 definition of the instruction. The script imports the classifier from a throwaway clone with `PYTHONDONTWRITEBYTECODE=1`.

| Set | Count |
| :- | -: |
| Tracked `tests/**/test_*.py` | 278 |
| Reached by a `ci.yml` lane `python -m pytest` token | 49 |
| `_registered_owner_test_paths()` | 135 |
| `_full_validation_test_targets()` | 94 |
| Under a `pytest.ini` `testpaths` root | 70 |
| **Strict uncovered set** (no lane token, no full-validation target) | **135** |
| Of which O-11 (no lane, owner or `pytest.ini` root) | 130 |
| Of which the five `_FULL_VALIDATION_INACTIVE_TESTS` | 5 |

The 135 paths are identical to instruction §5.1. A duplicate-basename check found one duplicate, `test_arrays_as_sets.py`; both of its directories are packages, so there is no collection collision.

### 4.2 Per-file sweep (this session; tested state `a8c99d1`)

Each of the 135 files was run alone in a throwaway clone. The environment was:
- `env -i`, with only `PATH`, `HOME`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `PYTHONDONTWRITEBYTECODE=1` and `PYTHONPATH` set. The session environment carries `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY` and `HDAPI_BASE_URL`; all were removed.
- Python 3.12.3, with CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; pytest 8.4.2).
- `pytest -q -p no:cacheprovider` per file, with `git status --porcelain --untracked-files=all` after each run and `git checkout -- . && git clean -fd` between runs.

Results:
- **Tests:** 638 collected; 548 passed, 76 failed, 14 collection errors. Summed run time 216.5 s.
- **Files:** 87 passed completely, 32 had failures, 14 could not be collected and 2 collected no test (exit 5). All five inactive files pass alone.
- **Visible writes:** 12 files changed tracked files or left untracked files.
- **Hidden writes.** The planning workers' mtime checks (`find -newer <marker>`) found 9 more files. They rewrite tracked files with identical bytes, or rewrite and then restore them, so `git status` and `git diff --exit-code` cannot see it. These are `test_db_runtime_posture`, `test_presenter_evidence_ownership`, `test_v2_mapped_cache_evidence`, `test_release_id_precedence_and_grep_guard`, `test_resolve_log_correlation_id`, `test_startup_logging`, `test_vendor_and_prod_guard`, `test_cli_env_pins_epic021` and `test_evidence_index_snapshot`. §11 therefore adds an mtime check to the clean-tree check.
- **Comparison with the Audit's batch run** (130 files at `982071b`: 79 failed, 523 passed, 14 errors):
  - The batch total is not comparable file by file, because batch order and shared state change outcomes. Run together, `tests/provider` and `tests/loader` give 9 failures; run per file, 5.
  - The 26 failures of `tests/evidence/test_hdapi_v2_contract_inventory.py` (21 in the Audit) are diagnosed in §4.4.

### 4.3 Lane-shape measurements (this session)

- **Existing full-validation shape.** The 94 current targets in one pytest process took 2,773 passed in 291 s, with a clean tree.
- **Adding the uncovered files.** The same 94 targets plus the 80 uncovered files that pass alone without visible writes gave 3,024 passed in 322 s. There were no cross-file failures and the tree was clean.
- **Conditions.** Both runs were taken while eight worker processes shared the CPU; the timings are upper bounds, not CI times.
- **Integrated prototype.** Every in-scope change of §8 was applied together in a scratch clone, committed there as `b1a67f1` on `a8c99d1` (never pushed). It was then checked:
  - **Coverage.** The §5.1 computation leaves exactly 2 files uncovered, the RP-1 and RP-2 files. Counts: 213 tracked test files, 49 lane-reached, 162 full-validation targets, 203 registered owners.
  - **Pinned suites.** `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/qa/test_qa_tool_ownership.py`, `tests/evidence/test_http_reader_ci_ownership.py` and `tests/evidence/test_evidence_tool_ownership.py` gave 313 passed and 1 failed. The one failure is the new coverage guard, which names exactly those 2 files.
  - **Classifier dry run on the prototype change.** `--base a8c99d1 --head b1a67f1 --event-name pull_request` exited 0 and selected all seven lanes and `changed_tests=true`. Its 162 changed-test targets equal `_full_validation_test_targets()`.
  - **Classifier dry run on a documentation-only commit** (`docs/run/RUN_PROD_QA.md`, plus new files under `docs/crd/`, `docs/qa/` and `docs/plans/`): exit 0, `reason=documentation_only`, no lane, `needs_python=false`, `changed_tests=false`.
  - **Full-validation shape** (all 162 targets, one pytest process, detached worktree, closed rails): 2,962 passed in 327.6 s; exit 0; `git diff --exit-code` 0; `git status --short --untracked-files=all` empty. The mtime check found 11 tracked files rewritten with identical bytes. All come from two already-covered tests outside the 135: `tests/evidence/test_bodygraph_policy_proofs.py` (9 `artifacts/bodygraph/*` and `schemas/bodygraph_source_invariance.*.v2.json` paths) and `tests/reader_v1/test_release_pack.py` (`artifacts/release_id.txt`, `artifacts/release_pack_manifest.json`). This was proven by running those two alone (3 passed; the same 11 paths) and the 68 retained files alone (189 passed in 32 s; no status change; no tracked file newer than the marker). Pre-existing behaviour: OBS-4

### 4.4 Facts that correct or extend the instruction

| ID | Instruction text | Measured fact at `a8c99d1` | Effect on this plan |
| :- | :- | :- | :- |
| F-1 | §5.4 / EC-1: governed primaries under the eight prefixes are "exactly `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json`" | The classifier gives lanes to **four** tracked paths under the prefixes: those two plus `docs/run/EPIC011_TEST_IDENTITIES.md.path_proof.txt` and `docs/run/PROD_ENDPOINTS.json.path_proof.txt`. In `_lanes_for_path`, the `.path_proof.txt` rule (evidence lane) runs before the documentation-prefix rule | The S05 filter re-includes path proofs as well as governed primaries. This applies EC-1's own definition ("'Classifier documentation prefixes' therefore means paths the classifier returns no lanes for") and its stated reason. Not a scope change (§5.3) |
| F-2 | §8 C-2: `tests/adapter/test_gate_auth.py` passes "against current `GET /reader` behavior. WU-PR-03 changes the behavior and the test with S10" | The file calls only `GET /internal/version`, through `adapter.app` → `adapter.wsgi.create_app()` → the `adapter/http_reader.py` blueprint (the `/internal/version` block at `http_reader.py:1076–1111`; `bp` created at line 1073). It never exercises `GET /reader`, and S10's gate (`http_reader.py:603`) does not affect it | C-2 is still met: retained and registered, it joins `_HTTP_READER_TEST_OWNERS` and `_HTTP_READER_INDIRECT_TEST_OWNERS`. For WU-PR-03's owner: S10 needs its own `GET /reader` tests |
| F-3 | §9.2 lists `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py` and `tests/provider/test_vendor_and_prod_guard*.py` as "S14 environment classification" | They exercise `adapter/env_guard.py` and `engine/config/provider_loader.py::resolve_provider`, not `engine/bodygraph/resolver.py` or `engine/cli/main.py`. PF05 §7.1.11b scopes its classification rule to "this CLI gate only" | The N2 criterion is still applied to them (§6). For WU-PR-04's owner: S14 needs its own tests and should not reuse `env_guard._compute_env_mode` (OBS-6) |
| F-4 | §5.5 consumers list | Also: `tools/qa/epic021_qa.py` (lines 30, 64, 72, 74) requires `tests/qa/test_epic021_scaffolding.py`, `tests/evidence/test_evidence_index_env.py` and `tests/evidence/test_sanity_evidence_index.py`; deleting any one fails the covered qa-lane test `tests/qa/test_epic021_acceptance_alignment.py`. `tests/evidence/test_epic018_manifest.py` asserts `tests/config/test_config_acceptance_map.py` exists. `tests/evidence/test_rails_ci_workflow_integration.py` pins `tests/adapter/test_env_guard_prod_variants.py` as an *unregistered* example (lines 1323, 1339) and pins the `adapter/http_reader.py` changed-test tuple (lines 664–679) | Those three are retained; the two EPIC-018 files are retired together; the two pins are updated (§5.5) |
| F-5 | §5.2: 22 failures "not diagnosed" | `test_hdapi_v2_contract_inventory.py` has 26 sweep failures at `a8c99d1`. **5** need `ruby`, which the generator calls (`generate_hdapi_v2_contract_inventory.py:2530`) and which the sweep's PATH omitted; with `/usr/local/bin` on PATH they pass. **21** are tool drift since `d79cfc1c` (HDE-EPIC040 PR06a, #508). This session re-verified: 21 failed / 277 passed at `a8c99d1`, and 298 passed at `cf9198df` (the parent of `d79cfc1c`), both with ruby on PATH and a clean tree. The `test_hde_epic037_pr05_parent_binding.py` failure diffs `docs/pfcanon/` against a moving base and fails whenever canon later changes | RP-1; the parent-binding file is retired (§7) |
| F-6 | §5.2: 37 failing files, 14 collection errors | One more real product defect: `engine/charts/loader.py:76–82` (`_call_legacy`) calls `get_chart` on the `engine.provider.fixtures.FixturesProvider` that `resolve_provider()` returns, which has no such method (broken since `6c6f4b2`). Only tests use the legacy signature. `engine/charts/loader.py` is not a release member | RP-2 |
| F-7 | — | `tests/bodygraph/test_resolver_vendor.py` already runs in the rails lane through `ci/checks/run_rails_job_definitions.py` and `ci/jobs/*.yml`. It counts as uncovered only because the §5.1 definition reads `ci.yml` pytest commands | Registered as a resolver owner, so the definition counts it. C-3 unchanged |
| F-8 | — | `tests/provider/test_vendor_and_prod_guard.py:6–8` uses `os.environ.pop`, which strips `SAFE_MODE` and `APP_ENV` for the rest of a pytest session. Unfixed, it would silently weaken closed rails for every later test in the full-validation run | Its fix (an autouse `monkeypatch` fixture) is mandatory (§7, row 92) |

## 5. Design

### 5.1 Registration model

**Rule (one for every retained file).** Each retained file that no `ci.yml` lane list reaches joins the **configured suite**:
- an explicit file entry is appended to `pytest.ini` `testpaths`, unless the file already lies under a root;
- the path is added to `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` in `ci/checks/classify_ci_changes.py`, sorted.

That is the classifier's existing mechanism for owner tests with no single source owner. `tests/evidence/test_rails_ci_workflow_integration.py::test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned` pins it: `configured == fixed | supplemental | inactive`. Effects:
- the file becomes a full-validation target, run by the changed-test step in the detached worktree on every full-validation change and whenever the file itself changes;
- `pytest.ini` gains 67 file entries (`tests/qa/test_epic021_scaffolding.py` is already under the `tests/qa` root);
- the supplemental tuple grows from 40 to 108.

**Owner additions (only to owner tuples that already exist, or where a contract or an executing consumer requires them):**

| Source key (registry) | Added owner targets | Basis |
| :- | :- | :- |
| `adapter/http_reader.py` (`_HTTP_READER_TEST_OWNERS`, and `_HTTP_READER_INDIRECT_TEST_OWNERS`) | `tests/adapter/test_gate_auth.py` | C-2; indirect consumer (F-2). Both sets are required: `test_http_reader_owner_registry_matches_current_consumers` asserts `direct_consumers == registered_direct` |
| `engine/bodygraph/resolver.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_bg_resolve_route_policy.py` | C-1 (WU-PR-04 extends the first); both exercise `_resolve_vendor` and the route policy |
| `engine/bodygraph/vendor_client.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/bodygraph/test_bg_resolve_route_policy.py` | Exercises `classify_bg_resolve_route_policy` |
| `adapter/wsgi.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/adapter/test_compat_writer_transport.py`, `tests/adapter/test_headers_and_determinism.py` | Both test the wsgi app |
| `engine/http/compat_handler.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/adapter/test_compat_writer_transport.py` | Writer transport of `/api/compat/v1` |
| `engine/stable/sercanon.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/infra/test_sercanon_bytes.py` | Release member under test |
| `tools/evidence/regenerate_identity_closure.py` (`_EVIDENCE_HELPER_TEST_OWNERS`) | `tests/evidence/test_internal_version_manifest_captures.py`, `tests/evidence/test_aux_preview_identity_parity.py` | Executed by the closure (lines 278–283, 372–381); consumers-first rule §9.5 |
| `tools/evidence/generate_bodygraph_policy_proofs.py` (`_EVIDENCE_GENERATOR_TEST_OWNERS`) | `tests/evidence/test_refresh_policy_snapshot.py` | PF14 §19.2 requires the guard to stay green; it asserts the ADR values |

**No new source key is created.** A new key changes the classifier's verdict on an edit to that source from refusal (`CI_PRODUCT_OWNER_TEST_MISSING`, `CI_EVIDENCE_OWNER_TEST_MISSING`) to owner-tested. S03–S05 do not require that decision, and the units that edit those sources make it. The candidates are listed for their owners in §17 (OBS-10). One prototype proposed a new `adapter/env_guard.py` key; it is excluded under this rule (in-flight planning decision D-1, §16).

**No new fixed-lane entry.** Every retained file is a full-validation target, the smallest correct lane (Plan Templates, "CI lane classification and automated budget-control discipline"). The `ci.yml` lane lists are unchanged (C-4).

### 5.2 S04: `tools/qa/` fail-closed for `.py`, `.sh` and `.sql`

In `_qa_tool_owner_targets` (`ci/checks/classify_ci_changes.py`, lines 1174–1199 at `a8c99d1`), replace the suffix test `rel.suffix.lower() != ".py"` with `rel.suffix.lower() not in _UNKNOWN_SOURCE_SUFFIXES`. That is the same set `_bodygraph_tool_owner_targets` uses. An unregistered `tools/qa/*.sh` or `*.sql` (any case) then raises `CI_QA_OWNER_TEST_MISSING`, as a `.py` does today. Registered `.py` behaviour is unchanged, and so are the lanes (`{"evidence", "qa"}`). `tools/qa/` holds no `.sh` or `.sql` file, so no current path changes verdict. The rule only narrows what passes (instruction §11).

Pinned tests (in `tests/evidence/test_rails_ci_workflow_integration.py::test_qa_tool_owner_policy_is_exhaustive_and_deduplicated`):
- the `tracked` set is computed over `classifier._UNKNOWN_SOURCE_SUFFIXES` instead of `.py`;
- an unowned `tools/qa/new_harness` with each of `.sh`, `.sql`, `.SH` and `.SQL` selects the qa lane but raises `CI_QA_OWNER_TEST_MISSING` from `changed_test_targets`;
- a non-source file under `tools/qa/` (`.md`) yields no owner target.

Prototype: all pass. With the classifier line reverted, the policy test fails (negative control).

### 5.3 S05: workflow path filter

Both `on.pull_request` and `on.push` (branch `main`) replace `paths-ignore` with this ordered `paths` list:

```yaml
    paths:
      - '**'
      - '!docs/crd/**'
      - '!docs/ephemeral/**'
      - '!docs/graph/**'
      - '!docs/pfcanon/**'
      - '!docs/plans/**'
      - '!docs/prompt_ecosystem_management/**'
      - '!docs/qa/**'
      - '!docs/run/**'
      - '**.path_proof.txt'
      - 'docs/run/EPIC011_TEST_IDENTITIES.md'
      - 'docs/run/PROD_ENDPOINTS.json'
```

Why this arrangement:
- **`paths`, not `paths-ignore`.** GitHub documents `!` exceptions only for `paths` ("use the `paths` filter prefixed with the `!` character to indicate which paths should be excluded"). Patterns are evaluated in order, and "A pattern that negates a previous pattern will re-include file paths".
- **The catch-all.** `'**'` "Matches zero or more of any character", so dot-prefixed paths (`.github/`, `.claude/`, `.gitignore`) stay included. They are full-validation paths in the classifier.
- **The negations.** They are the eight `_DOCUMENTATION_PREFIXES`, in the classifier's order.
- **Re-included paths.** `'**.path_proof.txt'` mirrors the classifier rule that gives every path proof the evidence lane (F-1). The governed primaries come from `docs/evidence/INDEX.json`.
- **Coverage of all changed files.** The filter skips a run only when every changed file is a classifier no-lane path under the eight prefixes, which is S05's intent as EC-1 defines it. A PR touching only those paths starts no run; any other changed file starts one.
- **What is unchanged.** `permissions: contents: read`, the exact-head checkout, concurrency, install, isolation and the final marker.

Pinned test (new, in `tests/evidence/test_rails_ci_workflow_integration.py`): `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths`. It reads both `paths` lists from the workflow text; no YAML library is installed, and adding one would change `requirements*`, which is outside §6. It checks that:
1. `paths-ignore:` is absent;
2. both lists equal the expected list built from `classifier._DOCUMENTATION_PREFIXES` and the governed primaries under them (`classifier._load_governed_primary_paths(ROOT)`);
3. for every tracked path, an ordered-match model of the filter selects the path exactly when the path lies outside the eight prefixes or the classifier gives it at least one lane;
4. the classifier dry run on all no-lane documentation paths returns `documentation_only` with no lane and `needs_python` false.

Prototype: passes. With the old workflow restored it fails (negative control).

Limits, recorded as risk R-3: the model covers only `*` and `**`, and the test asserts the patterns use no other metacharacter. A future governed primary under a documentation prefix fails this test, but only when the rails lane or full validation runs.

### 5.4 Inactive set

All five `_FULL_VALIDATION_INACTIVE_TESTS` are resolved:
- `tests/qa/test_epic021_scaffolding.py` is retained and joins supplemental (consumer F-4);
- the other four are retired (§7).

The constant becomes an empty `set[str]`, with a comment recording the resolution. The `CI_INACTIVE_TEST_REQUIRES_DISPOSITION` mechanism in `changed_test_targets` stays. Its pinned loop in `test_full_validation_inputs_run_the_supplemental_behavioral_gap` would otherwise become vacuous, so it gains one case that monkeypatches a synthetic inactive path and asserts the refusal. `tests/evidence/test_release_attestation.py` lines 617–618 (both EPIC022 files absent from the closure source) stay true.

### 5.5 Other pinned-test edits (all in `tests/evidence/test_rails_ci_workflow_integration.py`)

- **New `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target`** (acceptance (1)). It computes the instruction §5.1 set: every tracked `tests/**/test_*.py` against the `ci.yml` lane tokens plus `classifier._full_validation_test_targets()`, and asserts none is unreached. This is the same function as C-3, so WU-PR-06's `sweep` can reproduce it. It fails today (135), and in the prototype it reports exactly the 2 routed files.
- **`test_change_classifier_executes_against_exact_git_refs`** (lines 1323, 1339): its "unlisted test" example `tests/adapter/test_env_guard_prod_variants.py` becomes registered, so the example is renamed to the unregistered `tests/adapter/test_unlisted_adapter_regression.py`.
- **`test_http_reader_owner_guard_is_selected_without_fixed_lane_duplication`** (pinned tuple at lines 664–679): gains `"tests/adapter/test_gate_auth.py"` after `tests/adapter/test_diagnostic_writer.py`.
- **S04 and S05 tests:** §5.2 and §5.3.
- **Inactive refusal case:** §5.4.

### 5.6 Retirement mechanics and ledger

- **Retirement is deletion** (`git rm`), never a skip marker, `xfail` or exclusion list (instruction §7 bullet 4).
- **Registrations removed with the file.** A retired file must not stay in any registry or in `pytest.ini`. None of the 65 is registered today except the four inactive entries, which leave with §5.4.
- **`tests/retired_tests.md`** is new. Absence check at `a8c99d1`: `test ! -e tests/retired_tests.md` passed. PR-30 repeats the check at its base, and if it fails stops and records what exists.
  - Format: one Markdown table, one row per retired file, with the columns path, reason, retirement date (the PR-30 implementation date) and replacing coverage (named `path::test`, or `none` with the reason).
  - Introduction: a sentence stating that historical governed records naming a retired file are unchanged.
  - The rows are the §7 table's retire rows, verbatim. The classifier gives `tests/*.md` no lane (`_DOCUMENT_SUFFIXES`), and `changed_test_targets` skips it.
- **Orphaned fixtures are not deleted.** Examples are `tests/fixtures/g05_*`, `g08_*`, `*__admin.json` and `tests/goldens/*`. They are outside §6, and a `tests/fixtures/` change would itself need an owner (`CI_TEST_SUPPORT_OWNER_MISSING`). Listed as OBS-8.
- **Historical governed records stay unchanged.** These are acceptance maps, audit logs, QA harness copies and inventories that name a retired file (instruction §7 bullet 3).

### 5.7 Fix patterns (test code only)

| Pattern | Files | Change |
| :- | :- | :- |
| Product code writes a tracked file relative to the working directory | provider tests writing `artifacts/provider/decision.txt` (`engine/config/provider_loader.py:142–152`) | `monkeypatch.chdir(tmp_path)` per test or an autouse fixture |
| Product code writes through a module path helper | loader tests writing `artifacts/logs/loader_call.jsonl` (`engine/charts/loader.py:57–73`) | `monkeypatch.setattr(engine.charts.loader, "_Path", lambda p: tmp_path / p)`, then read the log from `tmp_path` |
| A generator test runs write mode against the real tree | `test_db_runtime_posture`, `test_presenter_evidence_ownership`, `test_v2_mapped_cache_evidence`, `test_evidence_index_snapshot`, the two EPIC030 tests | Redirect the tool's output root or `ROOT` to `tmp_path`; keep the read-only real-tree `--check` |
| Environment leak or unrestored import state | `test_vendor_and_prod_guard`, `test_env_guard_import_purity`, `test_headers_and_determinism` | `monkeypatch.setenv/delenv` and `monkeypatch.delitem`; remove the `pytest.skip` fallback |
| Stale expectation of current, governed behaviour | hdctl ×4, the two compliance ETag tests, the admin gate, streams/exits usage literal, the access-log line | Assert today's governed contract (PF05 §3.4, §4.1.3, §5.3, §5.4); the property under test is kept |
| False-positive guard | `tests/arch/test_arch_guards.py`, `tests/epic003/test_legacy_imports_denied.py` | Anchor import patterns to statement starts, scope the emitter check to `engine/http/` and `engine/cli/`, and match registration calls only. The prototype proves both still fail on synthetic real violations (PF02 §2.1) |
| Vacuous assertion | `test_env_guard_forbidden_matrix::test_sorted_keys_in_details` | `try/except` replaced by `pytest.raises` |

Every fix of §7 was prototyped by a worker in a throwaway clone. Each passed with a clean tree, and with a clean mtime check where §4.2 lists the file as a hidden writer. Everything passed together in the integrated prototype (§4.3). Exact per-file changes are stated in the §7 reason column. PR-30 re-verifies each against its own base.

## 6. Fix-versus-retire criterion (review v1.0 N2)

A file is **retained (and fixed if needed)** when:
- it exercises code that exists and is reached from a current entrypoint, or a canon-governed current contract;
- it can be made to pass with a test-only change that asserts the current governed behaviour.

A file is **retired** only for one of these reasons, recorded in the ledger:
- **(a) Removed surface.** It imports or runs a removed tree, script, route, flag or API (ARCHITECTURE.md "Deprecated/archived trees"; the removal commit cited).
- **(b) Not a governed surface.** It asserts a rule canon classes as Speculative, a rule that was never implemented, or behaviour of a legacy stub or dead module that no current entrypoint reaches; the governed replacement is named where one exists.
- **(c) Frozen record only.** It validates only a frozen administrative or historical record, whose bytes the evidence lane's `update_evidence_index.py --check` already protects, or which is unindexed and frozen. Plan Templates, "CI lane classification and automated budget-control discipline": "Administrative closeout work MUST NOT become ordinary required PR CI solely to … validate an epic close report, token matrix, … close pack, historical receipt, … acceptance package, or other administrative proof".
- **(d) Vacuous or empty.** It cannot fail, or collects no test.
- **(e) Redundant.** It duplicates a retained test that is named.

A file of current, governed behaviour is never retired except under (e), with the replacing test named.

A **real product defect** is never hidden by changing an expectation: the file goes to RP-2, or to RP-1 for a tool defect. A file with a live consumer (instruction §9.5) is retained unless the consumer is shown to keep working.

Applied to the files instruction §9.2 names:
- **`tests/compliance/test_override_guard_engine_env_and_app_env_alias.py`: retire, (a) and (e).**
  - Its expectations encode removed detection rules: the `HD_TOGGLES` key and `config/overrides` file detection, from `ebb95f5f`, `00234322` and `1520c65f`.
  - `adapter.wsgi.create_app()` cannot raise, because `adapter/wsgi.py:20` passes the Flask app and `env_guard._as_mapping` reads `app.config` (OBS-1).
  - Its current content (APP_ENV over ENGINE_ENV; production aliases) is replaced by the retained `tests/adapter/test_env_guard_prod_variants.py::test_empty_app_env_falls_back_to_engine_env`, `::test_app_env_overrides_engine_env` and `::test_prod_aliases_still_reject_forbidden_overrides`, plus `tests/adapter/test_env_guard_forbidden_matrix.py::test_each_forbidden_key_raises`.
  - It is not an S14 surface (F-3).
- **`tests/provider/test_vendor_and_prod_guard.py` and `test_vendor_and_prod_guard_min.py`: retain and fix.** Both pass and test current `provider_loader.resolve_provider` guards; the fixes remove the tracked writes and the environment leak (F-8). `tests/provider/test_vendor_guard_min.py`: retain as is.
- **`tests/adapter/test_gate_auth.py`: retain** (C-2, F-2).

Retirements total 65 (the class appears in §7's Disposition column):
- (a) 24;
- (b) 10;
- (c) 24;
- (d) 4;
- (e) 3.

None retires a test of current, governed behaviour without a named replacement. Security-relevant retirements (rails, keys-only logging, secrets and environment guards) each name the retained test that replaces them, or state why the behaviour no longer exists (instruction §11). Five retired files are cited by permanent canon as historical evidence or descriptive examples, and seven more by the reference-only PF20; §17 lists them as doc-delta candidates.

## 7. Per-file disposition (135 files)

"Sweep" is the per-file result of §4.2; "writes" includes the hidden writes of §4.2. A retirement's letter is its §6 class. "`pytest.ini` + supplemental" is the §5.1 rule; "owner add" entries are the §5.1 table. Totals:
- retain as is: 42;
- retain and fix: 26;
- retire: 65;
- route: 2.

| # | Path | Sweep at `a8c99d1` | Disposition | Registration, owner or replacing coverage | Reason |
| -: | :- | :- | :- | :- | :- |
| 1 | `tests/adapter/test_cache_keys.py` | pass 1/1 | retire (b) | replaced by: tests/compat/test_evaluate_pair_eligibility.py (test_cache_hit_* cases) | Tests adapter/cache_keys.py, which no code imports; the governed compat cache key lives in engine/compat/compute.py (PF01 §5.2). |
| 2 | `tests/adapter/test_compat_writer_transport.py` | pass 3/3 | retain | `pytest.ini` + supplemental; owner add: engine/http/compat_handler.py, adapter/wsgi.py | Current PF04 writer behaviour on the wsgi app (no-store, HEAD 405 Content-Length 0, OPTIONS 204); no covered equivalent. |
| 3 | `tests/adapter/test_env_guard_forbidden_matrix.py` | pass 5/5 | retain + fix | `pytest.ini` + supplemental | Vacuous try/except in test_sorted_keys_in_details replaced by pytest.raises. |
| 4 | `tests/adapter/test_env_guard_import.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Current adapter/env_guard.py import behaviour. |
| 5 | `tests/adapter/test_env_guard_import_purity.py` | pass 2/2 | retain + fix | `pytest.ini` + supplemental | Unrestored sys.modules.pop leaks a second EnvGuardError class into the session; restore with monkeypatch.delitem and the package attribute; remove the pytest.skip fallback. |
| 6 | `tests/adapter/test_env_guard_prod_variants.py` | pass 5/5 | retain | `pytest.ini` + supplemental; pinned example in test_rails_ci_workflow_integration.py renamed | Current APP_ENV/ENGINE_ENV precedence and production aliases of adapter/env_guard.py. |
| 7 | `tests/adapter/test_env_guard_silence_and_idempotence.py` | pass 2/2 | retain | `pytest.ini` + supplemental | Current adapter/env_guard.py behaviour. |
| 8 | `tests/adapter/test_etag_core.py` | pass 6/6 | retire (b) | replaced by: tests/http/test_reader_a7_transport.py::test_reader_a7_transport_invariants | Tests adapter/etag_core.py, a dead module whose rules contradict PF05 §5.3 (no-cache; HEAD and 304 Content-Length 0). |
| 9 | `tests/adapter/test_gate_auth.py` | pass 5/5 | retain | `pytest.ini` + supplemental; owner add: adapter/http_reader.py (_HTTP_READER_TEST_OWNERS and _HTTP_READER_INDIRECT_TEST_OWNERS) (C-2) | GET /internal/version on adapter.wsgi (blueprint defined in adapter/http_reader.py); PF04 §10.5. It does not exercise GET /reader. |
| 10 | `tests/adapter/test_headers_and_determinism.py` | fail 2/3 | retain + fix | `pytest.ini` + supplemental; owner add: adapter/wsgi.py | HSTS test: isolate APP_ENV/ENGINE_ENV with monkeypatch (adapter/wsgi.py lets APP_ENV override ENGINE_ENV); access-log test: assert the one keys-only LOG_SINK line adapter/logging_filter.py emits today. |
| 11 | `tests/adapter/test_no_etag_on_writers_and_errors.py` | pass 2/2 | retire (b) | replaced by: tests/transport/test_writers_errors_headers.py::test_writers_errors_headers | Builds its own Flask app around the dead adapter/etag_core.writer_headers. |
| 12 | `tests/adapter/test_reader_parity.py` | fail 3/3 | retire (e) | replaced by: tests/http/test_reader_a7_transport.py::test_reader_a7_transport_invariants; tests/compliance/test_reader_etag_and_conditional.py (fixed, wsgi factory) | Stale and redundant: omits v=1 (400 ERR_READER_INVALID_VERSION, PF05 §5.4), expects no-cache and HEAD Content-Length 0 against PF05 §5.3. |
| 13 | `tests/adapter/test_readyz.py` | fail 3/3 | retire (b) | replaced by: tests/adapter/test_jsonschema.py::test_readyz_schema_ok_and_deterministic | Tests readiness rules that are not implemented (adapter/wsgi.py /internal/readyz always 200; rule logic lived in the removed core/ tree); PF02 §3.4 classes readyz Speculative; S17 removes the documented rules. |
| 14 | `tests/adapters/test_safe_mode.py` | collection error | retire (a) | replaced by: tests/bodygraph/test_vendor_client.py::test_default_request_refuses_unless_both_open_rails_flags_are_set; ::test_closed_rails_default_request_refuses_before_url_opener | Imports the removed adapters/ tree (ARCHITECTURE.md "Deprecated/archived trees"). |
| 15 | `tests/arch/test_arch_capture_exists.py` | pass 2/2 | retire (c) | replaced by: tests/evidence/test_architecture_snapshot.py (product lane) | Checks only that a frozen closeout _arch/HDE-EPIC005_* snapshot exists (PF27 CI-lane rule). |
| 16 | `tests/arch/test_arch_guards.py` | fail 3/3 | retain + fix | `pytest.ini` + supplemental | Three false positives: anchor legacy-import patterns to statement starts, limit the emitter check to engine/http/ and engine/cli/, match registration calls only. Still fails on synthetic violations (PF02 §2.1). |
| 17 | `tests/artifacts/test_cli_text_artifacts_bom_lf.py` | pass 1/1 | retire (b) | replaced by: tests/compat/test_compat_public_lf_bom.py; tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical | Checks LF/BOM of the legacy stub, which is not a Reader surface; governed LF/BOM is covered. |
| 18 | `tests/audit/test_acceptance_map_epic017.py` | pass 1/1 | retire (c) | replaced by: update_evidence_index.py --check | Validates only a frozen administrative closeout record (PF27 CI-lane rule); the record is Index-bound. |
| 19 | `tests/audit/test_acceptance_map_epic019.py` | fail 1/2 | retire (c) | replaced by: none (frozen record) | Validates only a frozen administrative closeout record (PF27 CI-lane rule); stale since D6 was added (953e2684); the record is not indexed and is frozen. |
| 20 | `tests/audit/test_acceptance_maps_index.py` | fail 1/1 | retire (c) | replaced by: none (no consumer) | Validates only a frozen administrative closeout record (PF27 CI-lane rule); stale roster (index grew in 5f2b3683, 46610efc); no consumer. |
| 21 | `tests/audit/test_epic017_close_report.py` | pass 1/1 | retire (c) | replaced by: update_evidence_index.py --check | Validates only a frozen administrative closeout record (PF27 CI-lane rule); Index-bound. |
| 22 | `tests/audit/test_epic017_docdeltas.py` | pass 1/1 | retire (c) | replaced by: update_evidence_index.py --check | Validates only a frozen administrative closeout record (PF27 CI-lane rule); all 7 doc deltas Index-bound. |
| 23 | `tests/audit/test_epic017_manifest.py` | fail 1/2 | retire (c) | replaced by: update_evidence_index.py --check | Validates only a frozen administrative closeout record (PF27 CI-lane rule); the manifest binds capture-time hashes of artifacts later regenerated legitimately; cannot pass without hand-editing governed evidence. |
| 24 | `tests/audit/test_epic020_acceptance_bundle_wiring.py` | pass 1/1 | retire (c) | replaced by: tests/qa/test_epic020_qa_docs.py (evidence lane); tests/evidence/test_evidence_skeleton.py | Validates only a frozen administrative closeout record (PF27 CI-lane rule). |
| 25 | `tests/bodygraph/test_bg_resolve_route_policy.py` | pass 12/12 | retain | `pytest.ini` + supplemental; owner add: engine/bodygraph/resolver.py, engine/bodygraph/vendor_client.py | Passes; route policy of engine/bodygraph/resolver.py and vendor_client.py. Not edited (a frozen HDE-EPIC036 record hashes it). |
| 26 | `tests/bodygraph/test_resolver_vendor.py` | pass 4/4 | retain | `pytest.ini` + supplemental; owner add: engine/bodygraph/resolver.py (C-1) | Passes; run by the rails lane through ci/jobs definitions; WU-PR-04 extends it (C-1). |
| 27 | `tests/canon/test_center_order_and_counts.py` | collection error | retire (a) | replaced by: tests/config/test_registry_catalog_contract.py::test_all_source_facts_and_product_metadata_are_exact | Imports the removed core/ tree (core.canon, 1520c65f); assertions describe the removed code. |
| 28 | `tests/canon/test_checksums.py` | collection error | retire (a) | replaced by: none (artifacts/CANON_CHECKSUMS.json frozen; no producer) | Imports the removed core/ tree (core.canon, 1520c65f); assertions describe the removed code. |
| 29 | `tests/canon/test_error_envelope.py` | fail 1/1 | retire (a) | replaced by: none (removed script) | Runs scripts/validate_canon.sh, archived in 1520c65f (rc 127); CANON_SERIALIZER_MISMATCH no longer exists in code. |
| 30 | `tests/canon/test_loader_integrity.py` | collection error | retire (a) | replaced by: tests/config/test_registry_catalog_contract.py::test_all_source_facts_and_product_metadata_are_exact, ::test_gate_ids_are_exact_ascii_and_bound_to_pair | Imports the removed core/ tree (core.canon, 1520c65f); assertions describe the removed code. |
| 31 | `tests/canon/test_overrides_prod.py` | collection error | retire (a) | replaced by: none (rule removed; PF02 §6.2 forbids prod/dev toggles) | Imports the removed core/ tree (core.canon, 1520c65f); assertions describe the removed code. |
| 32 | `tests/canon/test_report_determinism.py` | collection error | retire (a) | replaced by: tests/invariance/test_bytes_identity.py | Imports the removed core/ tree (core.canon, 1520c65f); assertions describe the removed code. |
| 33 | `tests/cli/test_cli_env_pins_epic021.py` | pass 1/1; writes | retire (c) | replaced by: ci/checks/check_env_pins.sh (CI step); tests/invariance/test_determinism_env_helper.py::test_helper_writes_and_checks_log | Inactive set. EPIC021 administrative log writer: rewrites tracked artifacts/cli/env_pins_epic021.log (unindexed); PF27 CI-lane rule. |
| 34 | `tests/compat/test_cli_public_bytes_identity.py` | fail 1/1 | retire (a) | replaced by: tests/hdctl/test_cli_two_run_identity.py (fixed) | Flags removed (c4a73ae0), stale band key; duplicates the fixed hdctl two-run test. |
| 35 | `tests/compat/test_thresholds_constants_pack.py` | pass 1/1 | retain | `pytest.ini` + supplemental | engine/compat/thresholds.py current; no covered equivalent. |
| 36 | `tests/compat/test_ts_import_no_io.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Import-purity guard on engine/compat/type_strategy_v0.py (PF01 Appendix E). |
| 37 | `tests/compat/test_ts_sidecar_checks_manual.py` | no tests (exit 5) | retire (d) | replaced by: none (no tests) | Comments only; collects no test (pytest exit 5); refers to removed flags. |
| 38 | `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py` | fail 2/2 | retire (a) | replaced by: tests/bodygraph/test_vendor_client.py::test_fetch_does_not_retry_429_and_parses_retry_after_delta, ::test_retry_after_parses_http_date_and_omits_invalid_or_overflow; tests/reader_v1/test_schema.py::test_v1_error_adverse_cases_invalid | Its /_test/429_* routes were removed (9dafefe6); Reader errors may not carry retry_after_ms (PF05 §5.2, §8.1; PF04 §10.3). |
| 39 | `tests/compliance/test_cli_admin_gate_sidecar_perms_and_stdout_hash_invariance.py` | fail 1/3 | retain + fix | `pytest.ini` + supplemental | Stale expectation: the stub's admin gate now refuses before any stdout (scripts/hd_cli.py:83-89); assert exit 2 and empty stdout. |
| 40 | `tests/compliance/test_cli_release_id_resolver_precedence.py` | fail 3/3; writes | retire (a) | replaced by: tests/compliance/test_release_id_precedence_and_grep_guard.py (fixed); tests/runtime/test_identity.py::test_runtime_identity_paths_do_not_read_artifacts_or_identity_env | Expects non-hex values and a rel_dev_ fallback removed in f83ffc48; deletes tracked artifacts/release_id.txt read by covered tests/reader_v1/test_release_pack.py. |
| 41 | `tests/compliance/test_invocation_tag_accept_reject_and_roundtrip.py` | pass 2/2 | retain | `pytest.ini` + supplemental | Passes; engine/compliance/invocation_tag.py exists (no importer; observation OBS-9). |
| 42 | `tests/compliance/test_log_shape_snapshot.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Keys-only logging and header redaction on dev /reader; writes only to tmp_path. |
| 43 | `tests/compliance/test_meta_abba_parity.py` | pass 1/1 | retire (d) | replaced by: tests/compat/test_compat_public_ab_ba_identity.py::test_ab_ba_public_bytes_identical | Vacuous: the scripts/hd_cli.py stub ignores its inputs (lines 61-62), so its AB/BA assertion cannot fail. |
| 44 | `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py` | fail 3/3 | retire (a) | replaced by: tests/adapter/test_env_guard_prod_variants.py::test_empty_app_env_falls_back_to_engine_env, ::test_app_env_overrides_engine_env, ::test_prod_aliases_still_reject_forbidden_overrides; tests/adapter/test_env_guard_forbidden_matrix.py::test_each_forbidden_key_raises | Encodes removed detection rules (HD_TOGGLES, config/overrides files); create_app() cannot raise because adapter/wsgi.py:20 passes the Flask app (observation OBS-1). Not an S14 surface (PF05 §7.1.11 governs the CLI vendor gate). |
| 45 | `tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py` | fail 3/3 | retire (b) | replaced by: none (nothing executes the gate) | The preset gate is called by no app factory and its loader cannot import (engine/presets/loader.py:11); presets are Speculative (PF01 §1). |
| 46 | `tests/compliance/test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py` | fail 1/1; writes | retire (a) | replaced by: tests/reader_v1/test_goldens.py::test_json_goldens_schema_and_hashes_and_lf; the 429 replacements above | Depends on the removed 429 route and an error shape canon forbids; rewrites tracked artifacts/goldens/public_success.json and .sha256 (frozen, unindexed). |
| 47 | `tests/compliance/test_reader_etag_and_conditional.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | Governed A7 behaviour (PF05 §5.3, §5.4, Appendix A); setup predates v=1 and release admission: set APP_ENV=dev, inject seams, call with v=1 and absolute fixture charts. |
| 48 | `tests/compliance/test_reader_etag_compression_invariance.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | Same setup fix as the conditional test. |
| 49 | `tests/compliance/test_release_id_precedence_and_grep_guard.py` | pass 3/3; writes | retain + fix | `pytest.ini` + supplemental | Rewrites and restores tracked artifacts/release_id.txt mid-run; run the stub with cwd=tmp_path and absolute paths. |
| 50 | `tests/config/test_config_acceptance_map.py` | pass 2/2 | retire (c) | replaced by: update_evidence_index.py --check | Inactive set. Validates the frozen HDE-EPIC018 acceptance map (PF27); retired with tests/evidence/test_epic018_manifest.py, which asserts it exists. |
| 51 | `tests/em/test_em_defaults_and_ladder.py` | collection error | retire (a) | replaced by: none (removed tree) | Imports the removed core.config (1520c65f). |
| 52 | `tests/em/test_em_off_toggle.py` | pass 1/1 | retire (d) | replaced by: none | HD_FORCE_EM_OFF was never implemented; passes vacuously on the stub. |
| 53 | `tests/em/test_em_throat_and_adjacency.py` | fail 2/2 | retire (a) | replaced by: none (Speculative) | Throat/adjacency logic removed (eb7bfb2f); PF01 §6.4 Speculative; would overwrite tracked tests/fixtures/*__admin.json. |
| 54 | `tests/em/test_goldens_public_shape_and_identity.py` | pass 1/1 | retire (c) | replaced by: none | Validates only frozen pre-v1 goldens under tests/goldens/ that nothing produces or reads (PF27 CI-lane rule). |
| 55 | `tests/epic003/test_error_message_map.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Current alias-to-message map in engine/compat/errors.py; only assertion of it. |
| 56 | `tests/epic003/test_http_home_single_path.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Enforces the PF02 deny-list. |
| 57 | `tests/epic003/test_legacy_imports_denied.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | False positive on 'from engine.core import core' (engine/config/registry_loader.py:1277); anchor patterns to statement starts with re.MULTILINE (PF02 §2.1). |
| 58 | `tests/evidence/test_aux_preview_identity_parity.py` | pass 5/5 | retain | `pytest.ini` + supplemental; owner add: tools/evidence/regenerate_identity_closure.py | Executed by tools/evidence/regenerate_identity_closure.py inside the release attestation copy. |
| 59 | `tests/evidence/test_cli_conformance_artifacts.py` | pass 5/5 | retain | `pytest.ini` + supplemental | Release-closure --check of tools/cli/generate_cli_conformance_artifacts.py. |
| 60 | `tests/evidence/test_db_runtime_posture.py` | pass 4/4; writes | retain + fix | `pytest.ini` + supplemental | Rewrites 7 tracked artifacts/db/* files with identical bytes (invisible to git status); write mode to tmp_path, keep the real-tree --check. |
| 61 | `tests/evidence/test_env_matrix_snapshot_v3.py` | pass 6/6 | retain | `pytest.ini` + supplemental | Release-closure and sanity input; presence booleans only. |
| 62 | `tests/evidence/test_epic018_manifest.py` | pass 2/2 | retire (c) | replaced by: update_evidence_index.py --check | Validates only a frozen administrative closeout record (PF27 CI-lane rule) (HDE-EPIC018 manifest, Index-bound); retired with test_config_acceptance_map.py. |
| 63 | `tests/evidence/test_epic020_bundle_index_integration.py` | pass 1/1; writes | retire (c) | replaced by: tests/tools/test_epic020_bundle_tool.py (registered owner); update_evidence_index.py --check; ci/checks/check_mirror_schema.sh | Removed from active CI in 347ad40f ("self-referential EPIC020 bundle/index build"); running it rewrites 24 tracked files including the Index and Mirror. |
| 64 | `tests/evidence/test_epic030_pr01_pr03_fail_closed_evidence.py` | pass 3/3; writes | retain + fix | `pytest.ini` + supplemental | Writes under the repository's tmp/; use tmp_path and patch the tool ROOT where it computes relative paths. |
| 65 | `tests/evidence/test_epic030_pr04_band_thresholds_evidence.py` | pass 1/1; writes | retain + fix | `pytest.ini` + supplemental | Same tmp/ write; tmp_path and ROOT patch. |
| 66 | `tests/evidence/test_evidence_index_env.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Closed-rails guard for the evidence writer (PF09.1 HDE-CALC003.7); required by tools/qa/epic021_qa.py. |
| 67 | `tests/evidence/test_evidence_index_snapshot.py` | pass 3/3; writes | retain + fix | `pytest.ini` + supplemental | Writes into the repository's tmp/ and leaves a directory; use tmp_path and patch both snapshot.ROOT and snapshot.update_evidence_index.ROOT. |
| 68 | `tests/evidence/test_evidence_index_token_sets.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Only coverage of the updater's token-set normalization. |
| 69 | `tests/evidence/test_hdapi_v2_contract_inventory.py` | fail 26/298 | route | pending RS-20 (RP-1) | 21 failures since d79cfc1c (HDE-EPIC040 PR06a): stale route baseline in tools/evidence/generate_hdapi_v2_contract_inventory.py and presenter-provenance gap in tools/evidence/hdapi_v2_boundary_analyzer.py; 298/298 at its parent. RP-1. |
| 70 | `tests/evidence/test_hdapi_v2_live_conformance.py` | pass 9/9 | retire (c) | replaced by: tests/bodygraph/test_vendor_client.py::test_fetch_maps_status_to_typed_error, ::test_fetch_does_not_retry_429_and_parses_retry_after_delta, ::test_retry_after_parses_http_date_and_omits_invalid_or_overflow; update_evidence_index.py --check | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 71 | `tests/evidence/test_hdapi_v2_response_normalization.py` | pass 9/9 | retire (c) | replaced by: tests/bodygraph/test_v2_adapter.py::test_incomplete_standard_response_envelope_fails_closed, ::test_route_payload_family_mismatch_fails_closed | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 72 | `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` | pass 7/7 | retire (c) | replaced by: update_evidence_index.py --check; tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 73 | `tests/evidence/test_hde_epic036_pr02_evidence_loop.py` | pass 6/6 | retire (c) | replaced by: update_evidence_index.py --check; tests/evidence/test_evidence_skeleton.py::test_index_entries_have_mirrors_and_path_proofs | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 74 | `tests/evidence/test_hde_epic037_bg_resolve.py` | pass 3/3 | retire (c) | replaced by: tests/bodygraph/test_bg_resolve_v2_mapped_cache.py::test_closed_rails_refuse_before_all_io, ::test_explicit_legacy_fallback_remains_legacy | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 75 | `tests/evidence/test_hde_epic037_field_sufficiency.py` | pass 7/7 | retire (c) | replaced by: tests/bodygraph/test_v2_adapter.py::test_missing_internal_identity_context_fails_closed, ::test_unsupported_payload_family_fails_closed | Validates only a frozen HDE-EPIC035-037 evidence or closeout record (PF27 CI-lane rule); the record's bytes are hash-bound by update_evidence_index.py --check. |
| 76 | `tests/evidence/test_hde_epic037_pr05_parent_binding.py` | fail 1/6 | retire (c) | replaced by: none (the nonclaim is recorded in the hash-bound acceptance map) | Closeout administration only; test_pr05_did_not_edit_pfcanon diffs against a moving base and fails whenever canon later changes (stale by construction). |
| 77 | `tests/evidence/test_hde_epic037_v2_to_compat.py` | pass 4/4 | retire (e) | replaced by: tests/compat/test_hde_epic037_v2_adapter_to_compat.py::test_mapped_v2_adapter_outputs_feed_evaluate_pair, ::test_v2_to_compat_two_run_and_pair_order_identity, ::test_v2_to_compat_public_reader_boundary_fixture | Redundant with the registered owner tests/compat/test_hde_epic037_v2_adapter_to_compat.py. |
| 78 | `tests/evidence/test_identity_provenance.py` | pass 3/3 | retain | `pytest.ini` + supplemental | Release-closure input; fail-closed identity checks. |
| 79 | `tests/evidence/test_internal_version_manifest_captures.py` | pass 1/1 | retain | `pytest.ini` + supplemental; owner add: tools/evidence/regenerate_identity_closure.py | Executed by tools/evidence/regenerate_identity_closure.py; in classifier _RELEASE_IMPLEMENTATION_PATHS. |
| 80 | `tests/evidence/test_presenter_evidence_ownership.py` | pass 9/9; writes | retain + fix | `pytest.ini` + supplemental | Atomically replaces tracked artifacts/presenter/json_canon_compare.log; write mode to tmp_path (PF12 §8.6.3.5). |
| 81 | `tests/evidence/test_refresh_policy_snapshot.py` | pass 1/1 | retain | `pytest.ini` + supplemental; owner add: tools/evidence/generate_bodygraph_policy_proofs.py | PF14 §19.2 requires it to stay green; only test of the ADR values. |
| 82 | `tests/evidence/test_release_bindings.py` | pass 3/3 | retain | `pytest.ini` + supplemental | Release-closure input; drift cases in tmp_path. |
| 83 | `tests/evidence/test_sampler_evidence.py` | pass 2/2 | retire (c) | replaced by: update_evidence_index.py --check; tests/adapter/test_dev_sampler_http.py::test_dev_sampler_determinism; tests/cli/test_dev_sampler_cli.py::test_dev_sampler_two_run_identity | Schema and index checks of frozen, hash-bound HDE-EPIC019 sampler bytes (PF27 CI-lane rule). |
| 84 | `tests/evidence/test_sanity_evidence_index.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Current sanity-log Index/Mirror/proof binding; required by tools/qa/epic021_qa.py. |
| 85 | `tests/evidence/test_v2_mapped_cache_evidence.py` | pass 18/18; writes | retain + fix | `pytest.ini` + supplemental | Rewrites 8 artifacts/bodygraph/v2_mapped_cache/* and 2 schemas/bodygraph_v2_mapped_cache_*.v1.json with identical bytes; isolate write mode to tmp_path (security-relevant: rails, redaction, no raw payload). |
| 86 | `tests/hdctl/test_cli_admin_sidecar_invariance.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | Property current; rewrite to --pair-file and --dump-admin-dir (flags removed: ef140410). |
| 87 | `tests/hdctl/test_cli_read_singlebg.py` | fail 2/2 | retire (a) | replaced by: none (Speculative surface) | read singlebg was removed (c4a73ae0); PF05 §4.2 classes it Speculative ("absence is not a current defect"). |
| 88 | `tests/hdctl/test_cli_showcompat_parity.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | AB/BA property current; rewrite to --pair-file; drop stale numeric-free and band asserts (PF05 §4.1.3). |
| 89 | `tests/hdctl/test_cli_streams_and_exits.py` | fail 1/2 | retain + fix | `pytest.ini` + supplemental | Only the pinned usage literal is stale; assert the usage: hdctl prefix and one LF (PF05 §3.4). |
| 90 | `tests/hdctl/test_cli_two_run_identity.py` | fail 1/1 | retain + fix | `pytest.ini` + supplemental | Two-run property current; rewrite to a --pair-file in tmp_path built from tests.support.pr04_fixtures.complete_chart. |
| 91 | `tests/identity/test_service_identity_canonical.py` | pass 1/1 | retire (c) | replaced by: update_evidence_index.py --check (ci.yml evidence lane) | Validates only a frozen HDE-EPIC038 capture (release_id 12523fec..., current 52be4558...); its bytes are hash-bound by tools/evidence/update_evidence_index.py --check (evidence lane); PF27 CI-lane rule. |
| 92 | `tests/infra/test_hash_coupling.py` | pass 1/1 | retain | `pytest.ini` + supplemental | engine/stable/hashcouple.py exists. |
| 93 | `tests/infra/test_resolver_serializer_discipline.py` | fail 1/1 | retire (a) | replaced by: none (removed script) | Runs scripts/hd_resolve.py, deleted in 1520c65f. |
| 94 | `tests/infra/test_sercanon_bytes.py` | pass 1/1 | retain | `pytest.ini` + supplemental; owner add: engine/stable/sercanon.py | engine/stable/sercanon.py is a release member. |
| 95 | `tests/infra/test_serializer_guard.py` | pass 1/1 | retire (b) | replaced by: tests/cli/test_serializer_guards.py (compat lane) | Exercises only the legacy scripts/validate_det.sh over the stub; writes /tmp/HDS_A.json and /tmp/HDS_B.json. |
| 96 | `tests/integration/test_normalized_fixture.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; legacy chart.normalized.v1 schema and fixtures still tracked. |
| 97 | `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` | fail 1/2; writes | route | pending RS-20 (RP-2) | Product defect: engine/charts/loader.py:76-82 _call_legacy calls get_chart on a FixturesProvider that has none (since 6c6f4b2). RP-2. |
| 98 | `tests/loader/test_load_chart_fixture_only.py` | pass 2/2; writes | retain + fix | `pytest.ini` + supplemental | engine/charts/loader.py appends to tracked artifacts/logs/loader_call.jsonl; monkeypatch loader._Path to tmp_path. |
| 99 | `tests/loader/test_loader_hdapi_ignores_tz.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 100 | `tests/loader/test_loader_logs_keys_only.py` | pass 1/1; writes | retain + fix | `pytest.ini` + supplemental | Same loader log write; monkeypatch loader._Path and read the log from tmp_path (keys-only logging). |
| 101 | `tests/loader/test_pinned_lists_not_empty.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 102 | `tests/loader/test_validators_strict.py` | pass 5/5 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 103 | `tests/provider/test_factory_and_safemode.py` | fail 2/3; writes | retire (b) | replaced by: tests/provider/test_vendor_and_prod_guard.py (fixed); tests/bodygraph/test_vendor_client.py rails tests | Calls provider_loader APIs that never existed (get_provider, install_socket_trap_if_enabled); one vacuous pass; plants secrets/provider.json in the tree. |
| 104 | `tests/provider/test_hdapi_error_mapping.py` | pass 2/2 | retain | `pytest.ini` + supplemental | Passes; PF05 §7.2.5 mapping on engine/providers/vendor_http_hdapi.py. |
| 105 | `tests/provider/test_hdapi_json_headers.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; PF05 §7.2.2 headers. |
| 106 | `tests/provider/test_hdapi_request_shape.py` | fail 2/2 | retire (b) | replaced by: tests/bodygraph/test_vendor_client.py::test_from_env_normalizes_base_and_headers, ::test_build_contract_route_request_supports_legacy_simple_bodygraphs, ::test_join_vendor_resource_url_preserves_configured_base_path | Has never passed (unpacks a dict subclass); a fix would pin the orphan module's default-base fallback that PF05 §7.2.1 rejects. |
| 107 | `tests/provider/test_provider_call_logging_keys_only.py` | fail 2/2; writes | retire (a) | replaced by: tests/loader/test_loader_logs_keys_only.py (fixed) | The provider.call log it expects was removed (6c6f4b2); also rewrites tracked artifacts/logs/loader_call.jsonl. |
| 108 | `tests/provider/test_provider_interface_contract.py` | pass 3/3 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 109 | `tests/provider/test_prtest_precedence_and_artifact.py` | pass 2/2; writes | retain + fix | `pytest.ini` + supplemental | engine/config/provider_loader.py writes artifacts/provider/decision.txt relative to the working directory; chdir to tmp_path. |
| 110 | `tests/provider/test_resolve_log_correlation_id.py` | pass 1/1; writes | retain + fix | `pytest.ini` + supplemental | Same hidden decision.txt rewrite; chdir to tmp_path. |
| 111 | `tests/provider/test_secrets_dir_invalid.py` | pass 2/2 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 112 | `tests/provider/test_secrets_errors_typed.py` | no tests (exit 5) | retire (d) | replaced by: tests/provider/test_secrets_dir_invalid.py; tests/provider/test_secrets_unknown_provider_is_misconfigured.py | No tests (a copy of provider_loader.py); pytest exit 5. |
| 113 | `tests/provider/test_secrets_unknown_provider_is_misconfigured.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 114 | `tests/provider/test_startup_logging.py` | pass 1/1; writes | retain + fix | `pytest.ini` + supplemental | Unlinks and rewrites tracked decision.txt; chdir to tmp_path. |
| 115 | `tests/provider/test_vendor_and_prod_guard.py` | pass 6/6; writes | retain + fix | `pytest.ini` + supplemental | os.environ.pop strips SAFE_MODE and APP_ENV for the rest of the session and it writes/unlinks repo-root secrets/provider.json; autouse fixture with chdir and monkeypatch.delenv. |
| 116 | `tests/provider/test_vendor_and_prod_guard_min.py` | pass 2/2; writes | retain + fix | `pytest.ini` + supplemental | Writes tracked decision.txt; chdir to tmp_path. |
| 117 | `tests/provider/test_vendor_call_rails_and_config.py` | pass 4/4 | retain | `pytest.ini` + supplemental | Passes; rails configuration. |
| 118 | `tests/provider/test_vendor_guard_min.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Passes; no writes. |
| 119 | `tests/provider/tests/provider/test_decisions_perms_and_newline.py` | pass 1/1 | retire (e) | replaced by: tests/provider/test_prtest_precedence_and_artifact.py::test_decision_perms_and_exactly_one_newline | Accidental nested duplicate of test_prtest_precedence_and_artifact.py::test_decision_perms_and_exactly_one_newline; rewrites tracked decision.txt. |
| 120 | `tests/qa/test_epic021_scaffolding.py` | pass 3/3 | retain | supplemental (moves out of the inactive set; already under the `tests/qa` root) | Inactive set. Live consumer: tools/qa/epic021_qa.py runs it as the bootstrap test; deleting it fails the covered qa-lane test tests/qa/test_epic021_acceptance_alignment.py. |
| 121 | `tests/qa/test_epic022_acceptance_scaffold.py` | pass 11/11 | retire (c) | replaced by: ci/checks/check_env_pins.sh; tests/cli/test_errors_parity.py::test_http_and_cli_parity | Inactive set. Epic closeout assertion, removed from the release closure in 347ad40f (PF27 CI-lane rule); tests/evidence/test_release_attestation.py's absence assertion stays true. |
| 122 | `tests/qa/test_epic022_close_pack_ready.py` | pass 5/5 | retire (c) | replaced by: update_evidence_index.py --check | Inactive set. Close-pack readiness of a closed Epic (PF27 CI-lane rule); PF14's citation is records-only. |
| 123 | `tests/reader_v1/test_cli_proof.py` | fail 1/1 | retire (b) | replaced by: tests/reader_v1/test_emitter.py; tests/cli/test_cli_canonical_bytes.py::test_reader_dump_and_admin_sidecars_are_canonical | O-P06a-03: the legacy scripts/hd_cli.py stub refuses --admin-out without --admin (exit 2); the stub is not a Reader surface (PF05 §5.1.6) and not proof (PF29 §16). |
| 124 | `tests/scripts/test_dev_sampler_healthcheck.py` | pass 3/3 | retain | `pytest.ini` + supplemental | Current dev Reader healthcheck (PF19 §1.4); logs to tmp_path. |
| 125 | `tests/test_catalog_canon.py` | collection error | retire (a) | replaced by: tests/config/test_registry_catalog_contract.py | Imports removed core.catalog / core.stable; its emit test would rewrite tracked artifacts/CANON_CHECKSUMS.json. |
| 126 | `tests/test_pipeline_properties.py` | collection error | retire (a) | replaced by: tests/compat/test_compat_public_ab_ba_identity.py::test_ab_ba_public_bytes_identical; tests/reader_v1/test_schema.py::test_additional_properties_closed_everywhere | Imports the removed placeholder core.pipeline compute_pair. |
| 127 | `tests/test_pipeline_public.py` | collection error | retire (a) | replaced by: tests/http/test_reader_post_v1.py::test_success_envelope_headers_and_ab_ba_identity; tests/compat/test_compat_public_ab_ba_identity.py::test_ab_ba_public_bytes_identical | Imports the removed placeholder core.pipeline. |
| 128 | `tests/test_resolver_prod_rules.py` | collection error | retire (a) | replaced by: none (removed rule) | Imports the removed core.config toggles resolver (PF02 §6.2 forbids toggles); would create config/runtime_overrides.json. |
| 129 | `tests/test_sercanon.py` | collection error | retire (a) | replaced by: tests/infra/test_sercanon_bytes.py (retained) | Imports the removed core.stable API; its NFC assertion contradicts PF14 §5.1 (no Unicode normalization). |
| 130 | `tests/unit/test_channel_derivation.py` | collection error | retire (a) | replaced by: tests/core/test_engine_core_determinism.py | Imports the removed adapters.hdapi; the v2 adapter fails closed instead of deriving. |
| 131 | `tests/unit/test_enum_closure.py` | collection error | retire (a) | replaced by: none (removed behaviour) | Imports the removed adapters.hdapi v1 enum closure. |
| 132 | `tests/unit/test_narratives_composer.py` | pass 3/3 | retain | `pytest.ini` + supplemental | Current compose_text branches; not edited (audit/qa/hde-epic039/00_meta/qa_runner.py hashes it). |
| 133 | `tests/unit/test_no_io_guard.py` | pass 1/1 | retain | `pytest.ini` + supplemental | Current adapter/no_io_guard.py (rails-relevant; only test). |
| 134 | `tests/unit/test_sampler_core.py` | pass 4/4 | retain | `pytest.ini` + supplemental | Current engine/sampler/core.py; PF09.2 HDE-DISS003 names its test functions. |
| 135 | `tests/unit/test_viewer_prefs_normalization.py` | pass 5/5 | retain | `pytest.ini` + supplemental | Current engine/validation/viewer_prefs.py; its node ID is pinned by tests/qa/test_viability_generator_wrappers.py and tools/qa/generate_epic028_acceptance_ledger.py. |

## 8. Change set

All paths are inside instruction §6 for the in-scope part. RP-1 would add two `tools/evidence/` files if approved (§16). Counts are from the integrated prototype.

| Path | Change |
| :- | :- |
| `.github/workflows/ci.yml` | `paths-ignore` → ordered `paths` for `pull_request` and `push` (§5.3). No other line changes |
| `ci/checks/classify_ci_changes.py` | S04 suffix rule (§5.2); supplemental tuple 40 → 108 (§5.1); owner additions (§5.1 table); inactive set emptied, with a comment (§5.4) |
| `pytest.ini` | 67 `testpaths` file entries appended (§5.1). Markers unchanged |
| `tests/evidence/test_rails_ci_workflow_integration.py` | §5.5 edits and the new S04, S05, coverage and inactive-refusal tests |
| 26 retained test files | the §7 "retain + fix" rows |
| 65 retired test files | deleted (§7 "retire" rows) |
| `tests/retired_tests.md` | new ledger (§5.6) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md` | the PR-30 result record (§13), written by PR-30 |

Unchanged:
- every release member, so `catalog/manifest.json` and `release_id` stay put (C-5);
- every `tools/**`, `scripts/**` and `ci/jobs/*.yml` file, and `ci/checks/run_rails_job_definitions.py`;
- every governed artifact, `AGENTS.md`, `README.md` and `docs/pfcanon/`.

## 9. Implementation sequence (PR-30)

PR-30 executes this after Nathan's Proceed for the successor v1.1. It executes nothing on v1.0.

1. **Recover before creating anything.** Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/` for HDE-CRD-0002 WU-PR-01 work, and resume the most advanced consistent state (PR-30 Execute 1). Fetch `main` and record the base SHA. If `main` has moved past `a8c99d1` outside `docs/ephemeral/`, re-run the §4.1 inventory and the §4.2 sweep, and treat any changed fact as an in-flight decision or a rescope finding. Run the ledger absence check (§5.6).
2. **Environment.** Use Python 3.12 with CI's install; check pytest readiness with `python -m pip install -r requirements-dev.txt` then `python -m pytest --version` (AGENTS.md). Use closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `DATABASE_URL`, `HD_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `GEO_API_KEY` and `GH_TOKEN` unset (`env -i` is the proven method). Put `ruby` on `PATH` for the RP-1 file if RP-1 is approved.
3. **S04 and S05** (§5.2, §5.3) with their pinned tests. Run the rails integration file; also run the two negative controls.
4. **Fixes:** the 26 "retain + fix" rows, in directory order. After each directory, run its files alone and together in a throwaway copy, with `git status` and the mtime check.
5. **Retirements:** the 65 "retire" rows, plus the four inactive entries leaving the classifier (§5.4).
6. **Registrations:** `pytest.ini`, the supplemental tuple and the owner additions (§5.1).
7. **Pinned-test edits** (§5.5), and the RS-20-approved RP-1/RP-2 changes as v1.1 states them.
8. **Ledger:** `tests/retired_tests.md`, with the PR-30 date.
9. **Local validation** (§11), all in a detached worktree of the commit candidate.
10. **One coherent commit** (PR-30 "Mandatory PR-development execution contract"), push to the work branch, and open the PR with the `.github/pull_request_template.md` headings and the AGENTS.md content rules (instruction §12).
11. **PR result record** (§13): write it, commit and push it, then return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

Checkpoint and restart rules:
- **Step order.** Steps 3–8 can be reordered. Step 9 runs on the final candidate tree only.
- **Rework after validation.** Any change after step 9 repeats step 9.
- **Base drift.** A base change that touches `ci.yml`, the classifier, `pytest.ini` or any of the 135 files repeats steps 1 and 9.

## 10. Requirement → change → test map

| Requirement / acceptance | Change | Proof (local, PR-30) | Proof (CI, PR-35) |
| :- | :- | :- | :- |
| S03 (1): zero files outside lane-or-target coverage; ledger explains every retirement | §5.1 registrations; §5.6 retirements and ledger | new coverage guard test; §4.1 computation script → 0; every deleted path (`git diff --diff-filter=D --name-only base..head`) equals the ledger's path column | rails lane runs the integration file (full validation) |
| S03 (2): every retained file passes in its lane shape in a detached worktree, clean tree | §5.7 fixes; env isolation | all full-validation targets in one pytest process in a detached worktree; `git diff --exit-code`; empty `git status --short --untracked-files=all`; no tracked file newer than a pre-run marker | changed-test step (full validation) with its clean-tree assertion; final audit |
| S03: recorded failures and collection errors fixed or retired | §7 | per-file runs of the 26 fixed files; collection of the configured suite (`pytest --collect-only`, exercised by `test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`) | as above |
| S04 (3): unregistered `.sh`/`.sql` under `tools/qa/` fails classification in a unit test | §5.2 | `test_qa_tool_owner_policy_is_exhaustive_and_deduplicated` (new cases); negative control | rails lane |
| S05 (4): docs-only dry run selects no lane; the filter ignores exactly the classifier's no-lane documentation paths | §5.3 | new path-filter test; negative control; classifier CLI dry run on a docs-only commit in a throwaway clone (reason `documentation_only`, no lane, `changed_tests=false`) | rails lane; observed on the PR: a run starts (the PR changes non-doc paths) |
| (5): all seven lanes green on the exact head, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | `ci.yml` and the classifier are full-validation paths | classifier CLI dry run on `base..head` selects all seven lanes and changed-test targets equal to `_full_validation_test_targets()` | PR-35: exact-head CI |
| C-1 | resolver owner add | `changed_test_targets(ROOT, ("engine/bodygraph/resolver.py",))` includes `tests/bodygraph/test_resolver_vendor.py` | — |
| C-2 | http_reader owner add | `tests/evidence/test_http_reader_ci_ownership.py` passes; the pinned tuple includes the file | — |
| C-3, C-4 | the coverage definition and lane lists are unchanged | the coverage guard test uses the §5.1 definition; the `ci.yml` lane step names and lists are unchanged (`git diff` shows only the `on:` block) | — |
| C-5 | no member change | `python scripts/release_id_recompute.py --check-manifest-only` exits 0; `git diff base..head -- catalog/manifest.json engine/config/registry_loader.py` is empty | release lane |
| C-6 | S04 rule mirrors `_bodygraph_tool_owner_targets` | §5.2 tests | rails lane |

## 11. Validation plan (PR-30, local)

All of the following run in a detached worktree of the commit candidate, under step 2's environment. A failure is a finding to fix, never to skip or quarantine.

1. `ci/checks/check_env_pins.sh` and `python3 ci/checks/check_agents_md_citations.py`: exit 0.
2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py tests/qa/test_qa_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py tests/evidence/test_evidence_tool_ownership.py`: all pass. On the prototype: 314 collected, 313 passed; the one failure is the coverage guard naming the two files RS-20 decides.
3. **Full-validation shape.** List the targets with `_full_validation_test_targets()` (162 in the prototype, plus any that RS-20 adds), then run them in one `python -m pytest -q -p no:cacheprovider -- <targets>` process.
   - Afterwards: `git diff --exit-code`, an empty `git status --short --untracked-files=all`, and no tracked file newer than a marker touched before the run, apart from the 11 paths the two covered tests of OBS-4 rewrite today. A separate run of the retained files alone must touch nothing (prototype: 189 passed, nothing touched).
   - Prototype counts: §4.3.
4. **Fixed lane lists** as `ci.yml` runs them. Product, compat, db, rails and evidence run in the worktree root, with their pre-steps (`tools/order/generate_ordering_artifacts.py --check`, `ci/checks/check_cli_help.sh`, the two compat guards writing under a temporary directory, `python ci/checks/check_direct_db_contract.py`, `ci/checks/run_rails_job_definitions.py` with the three job files, and the seven evidence read-only checks). The qa and release lane test lists run in their own detached worktrees. Clean tree after each.
5. **Classifier dry runs:** `base..head` (expect all seven lanes, `changed_tests=true`, targets equal to the full-validation set), and a docs-only commit in a throwaway clone (expect `documentation_only`).
6. **Inventory:** the §4.1 computation script returns 0 uncovered, and the deleted-path set equals the ledger's path column.
7. **Members:** `python scripts/release_id_recompute.py --check-manifest-only` exits 0, and the `catalog/manifest.json` / `engine/config/registry_loader.py` diff is empty.

Not run locally (PR-35, or hosted CI): the release attestation build and verify (`tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean`). PR-30 may run it in an external directory if time allows. Hosted CI runs it in the release lane on full validation.

## 12. PR split, merge dependencies and downstream contracts

- **One PR**, carrying the whole unit, with one coherent commit at initial publication. A split would leave `main` with a coverage guard that fails, or with coverage that does not hold, between PRs.
- **Upstream merge dependencies:** none. The instruction's PR #623 is merged.
- **Downstream:** WU-PR-03 and WU-PR-04 (C-1, C-2) and WU-PR-06 (C-3, C-4) build on this unit's merged state. WU-PR-02, WU-PR-06 and WU-PR-07 may be prepared in parallel and merge in Plan order.
- **CI cost:** this PR is a full-validation change (all seven lanes and 162+ changed-test targets). Later PRs touching only one source run that source's owners plus their lanes. Edits to `ci.yml`, the classifier, `pytest.ini` or `requirements*` run the larger full-validation set, measured in §4.3 at about +31 s for 80 files under shared CPU.

## 13. Acceptance and evidence obligations (PR result record)

PR-30 writes `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md`. It contains:
- the before/after inventory (135/130 → 0);
- the per-file disposition table, as applied;
- the sweep transcript summary (§4.2 and PR-30's own rerun);
- the lane counts and the full-validation run counts;
- every §11 check actually run, with its result and counts;
- the ledger path;
- the in-flight decisions, with the RP-1/RP-2 outcomes as approved;
- the nonclaims: CI green is not QA; no PF09 mapping; no QA artifact.

QA evidence and `audit/qa/hde-crd-0002/` are out of scope (instruction §7).

## 14. Security and migration constraints

- **Migration:** none. No data, schema, catalog or stored BodyGraph changes, and no member changes. Rollback is Nathan's revert of the squash commit; no manifest refresh is needed.
- **Workflow:** `permissions: contents: read`, the exact-head checkout, closed rails in every lane and the isolation steps are unchanged. The filter never skips CI for a governed primary or a path proof (§5.3).
- **Classifier:** S04 only narrows what passes. No new source owner key is added (§5.1).
- **Fixes:** test-only. They remove tracked writes, `secrets/provider.json` planting, and session-wide environment mutation (F-8).
- **Retirements:** each security-relevant retirement names a replacing retained test, or the reason the behaviour no longer exists (§6, §7).
- **Secrets:** no secret, token or key value appears in tests, logs, the ledger or the PR record. Runs strip credentials from the environment.

## 15. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| R-1 | Size (Plan R-1): 65 deletions and 26 fixed files | Bounded by §6's criterion; two boundary findings are routed through RS-20, not absorbed; nothing is skipped or quarantined |
| R-2 | Hidden same-byte rewrites pass `git status` | mtime check (§11) plus the fixes of §5.7 |
| R-3 | The filter model in the S05 test differs from GitHub's matcher | The model is limited to `*` and `**` and the test asserts no other metacharacter; documented GitHub semantics are cited; PR-35 observes the run start |
| R-4 | A future governed primary under a documentation prefix | The S05 test fails at the next rails or full-validation run; until then the classifier still selects evidence if a run starts |
| R-5 | The four fixed hdctl subprocess tests depend on the tree's release being admitted | True on `main`; a unit that leaves the release unadmitted fails them visibly (as it fails the covered `test_admission_refusal_is_a_single_stderr_token`) |
| R-6 | Full-validation runtime grows | Measured (§4.3); full validation runs only on full-validation paths |
| R-7 | `ubuntu-latest` moves to Ubuntu 26.04 in November 2026 (runner-images announcement); Ruby availability there is unverified | Only RP-1's file needs Ruby; PR-35 observes the hosted result |
| R-8 | `main` moves before PR-30 | §9 step 1 re-verification and restart rules |

Recovery:
- an interruption resumes in the same phase session from its last saved artifact;
- an ordinary defect in this plan returns to this PR-20 context, and a correction is a complete successor version;
- abort is only Nathan's manual PR-50 instruction.

## 16. Boundary findings, rescope route and in-flight planning decisions

**RP-1 and RP-2** are stated with evidence, alternatives and the proposed bounded delta in `docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md`. In summary:
- **RP-1 (tool drift).**
  - Finding: `tests/evidence/test_hdapi_v2_contract_inventory.py` fails 21 tests because HDE-EPIC040 PR06a changed the Reader routes. That left the route baseline in `tools/evidence/generate_hdapi_v2_contract_inventory.py` stale, and `tools/evidence/hdapi_v2_boundary_analyzer.py` unable to follow a parameter-passed presenter emitter into a module-level helper.
  - Proposed delta: add those two tool files to WU-PR-01's loci for those two corrections only. Register this test as the owner of both (the analyzer leaves `_EVIDENCE_HELPERS_REQUIRING_OWNER`), move its untracked fixtures to `tmp_path`, and register it like the other retained files.
  - No governed artifact is regenerated, and no release member changes.
- **RP-2 (loader defect).**
  - Finding: the legacy-signature defect of F-6.
  - Proposed delta: retire `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py`. Its ledger row records the defect and the route. The defect is routed to the Product Owner as owner of PF09 Separation HDE-SEPA006, which canon assigns to the old loader/provider path (PF02 §1.1 "Non-BodyGraph chart loader classification"; PF09.3 HDE-SEPA006.2).

Neither changes an approved acceptance intent, Specification boundary or another unit's scope. Each exceeds instruction §6/§7 or §9.8 as issued, so the IA decides.

**In-flight planning decisions** (taken here, within approved scope):

| ID | Decision | Why | Tested |
| :- | :- | :- | :- |
| D-1 | No new source owner key (rejects a prototype's `adapter/env_guard.py` key) | §5.1 rule; S03–S05 do not need the verdict change | integrated prototype pinned suites pass without it |
| D-2 | `test_release_id_precedence_and_grep_guard.py` fix does not add a new fallback-value test | the legacy stub's fallback value is not governed behaviour | integrated prototype |
| D-3 | Path proofs under documentation prefixes stay under CI (F-1) | EC-1's definition and reason | S05 test |
| D-4 | `paths` with ordered negations, not `paths-ignore` with `!` | only the former is documented | S05 test model; hosted observation at PR-35 |
| D-5 | Retain orphan-module tests that pass (`engine/providers/*`, `engine/compliance/invocation_tag.py`, `chart.normalized.v1`) | they test code that still exists; removing modules is outside §6 | per-file runs |

## 17. Observations routed to other owners, and doc-delta candidates

No observation below is fixed in WU-PR-01. Each goes to the named owner through the IA, which owns the Plan's unit routing, with its evidence. Nothing here is a finding against this unit's acceptance.

| ID | Observation | Evidence | Owner / route |
| :- | :- | :- | :- |
| OBS-1 | The `adapter.wsgi` pre-serve environment guard is inert: `validate_or_fail(app)` reads Flask config, not the process environment; the production factory `adapter/factory.py` has no startup guard | `adapter/wsgi.py:20`; `adapter/env_guard.py:82–104`; probe with `APP_ENV=prod HD_ADMIN=1` | IA for routing; WU-PR-05 (security review) or the Product Owner |
| OBS-2 | `engine/config/provider_loader.py:50–52` checks `ENGINE_ENV` before `APP_ENV`, unlike `adapter/env_guard.py` | read at `a8c99d1` | WU-PR-04 owner (S14) for awareness |
| OBS-3 | Covered `tests/adapter/test_jsonschema.py` carries two `@pytest.mark.xfail` markers (lines 75, 82) and leaks `ENGINE_ENV` | read at `a8c99d1` | IA (outside WU-PR-01's 135 files) |
| OBS-4 | Covered `tests/evidence/test_bodygraph_policy_proofs.py` (9 paths) and `tests/reader_v1/test_release_pack.py` (`artifacts/release_id.txt`, `artifacts/release_pack_manifest.json`) rewrite tracked files with identical bytes on every run; `git diff` and `git status` cannot see it | mtime check (§4.3) | IA (outside the 135) |
| OBS-5 | `adapter/etag_core.py` and `adapter/cache_keys.py` are dead modules | no importer | IA / Product Owner (non-test follow-up) |
| OBS-6 | `env_guard._compute_env_mode` treats unset as dev and unknown as non-production; reusing it for S14 would contradict PF05 §7.1.11b | `adapter/env_guard.py`; `engine/http/compat_handler.py:5,112` | WU-PR-04 owner |
| OBS-7 | Covered `tests/cli/test_showcompat_parity_and_identity.py` subprocess tests skip unless rails are open, so they always skip in CI | lines 107, 127, 149 | IA |
| OBS-8 | Fixtures orphaned by retirements (`tests/fixtures/g05_*`, `g08_*`, `*__admin.json`, `tests/goldens/*`) | §5.6 | WU-DOC-01 or a later cleanup |
| OBS-9 | `engine/compliance/invocation_tag.py` has no importer, and its 16-hex rule conflicts with canon examples (`INV-000000`) | PF01 §3.3; PF05 golden | IA |
| OBS-10 | Sources whose retained tests could become owner keys: `adapter/env_guard.py`, `adapter/no_io_guard.py`, the EPIC030 PR-01–PR-04 generators, `tools/evidence/generate_evidence_index_snapshot.py`, `generate_db_runtime_posture.py`, `generate_presenter_history.py`, `generate_v2_mapped_cache_evidence.py` | §5.1 rule | the unit that next edits each source |
| OBS-11 | Documents name retired files: `docs/RUN.md:9` and `docs/ADAPTER_009.md:115` (`tests/test_sercanon.py`); `README.md:218` (`tests/qa/test_epic022_acceptance_scaffold.py`) | grep at `a8c99d1` | WU-DOC-01 |
| OBS-12 | `tools/evidence/generate_hdapi_v2_contract_inventory.py` depends on `ruby`, declared nowhere | line 2530; PF09.5 HDE-FERM006.2 notes Ruby was installed | Product Owner (Glow Infrastructure doc-delta candidate) |

**Doc-delta candidates (Product Owner drainage; no canon edit).** Canon passages that cite a file this plan retires, all historical records or descriptive examples:
- PF09.2 Dissolution line 677 (`tests/evidence/test_sampler_evidence.py`);
- PF05 §4.1.6 line 837 and PF09.4 Conjunction line 2139 (`tests/reader_v1/test_cli_proof.py`; the recorded failure no longer exists);
- PF09.1 Calcination lines 1146, 1166 (`tests/evidence/test_epic020_bundle_index_integration.py` and the removed `epic020-evidence-bundles` job, already stale since `347ad40f`) and line 2053 (`tests/config/test_config_acceptance_map.py`);
- PF14 line 7653 (`tests/qa/test_epic022_close_pack_ready.py`, records-only);
- PF20 references to the retired HDE-EPIC035–037 evidence tests (reference-only document).

## 18. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried unchanged from the Specification, Plan and instruction:
- **CR-1** (CANON_RECONCILIATION; PF30 record and "CRD Plan" wording versus HDE Governance §9.1.1): `APPROVED_AS_CHANGED`. Interim: no PF30 entry. Affects no requirement of this unit.
- **CR-2** (CANON_RECONCILIATION; planned units in a Specification): `APPROVED_AS_CHANGED`. Affects no requirement of this unit.
- **CR-3** (CANON_RECONCILIATION; "stable CRD ID recorded in PF30"): `APPROVED_AS_CHANGED`. Interim: `HDE-CRD-0002` is the Product Owner-assigned ID. Not touched.

**No new conflict.** Coverage for this unit was searched: `git grep` of `docs/pfcanon/` on `main` for every one of the 135 paths, and for `paths-ignore`, quarantine, test retirement, xfail, skip, `pytest.ini`, `testpaths`, changed-test, detached worktree and lane list. Canon that cites a retired file does so as a historical record or a descriptive example (§17), which is drift to drain, not a conflict with a current requirement. PF14 §19.2's "MUST remain green" guard is retained.

## 19. PR-30 and PR-35 ownership

- **PR-30** (after Nathan's Proceed for v1.1, in this same dedicated PR session):
  - recovers before creating any vehicle;
  - implements only v1.1's scope, with tests run locally under §11;
  - forms one coherent commit;
  - publishes the initial candidate and records `PR_IMPLEMENTATION_RESULT`;
  - returns `PR_CANDIDATE_PUBLISHED` with a handoff to PR-35 in PR-35's own dedicated session.

  PR-30 owns neither review correction nor CI readiness.
- **PR-35** (its own dedicated session):
  - retrieves and resolves review findings (Codex code review and security review), retests locally and pushes coherent corrections;
  - uses CI economically: known findings first, no `[skip ci]` without Nathan's direct authorization;
  - verifies current-head CI (all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability, and observes that the workflow started on the PR (§5.3);
  - returns `MERGE_PENDING — Ready to merge` without merging.

  No CI waiver exists for HDE-CRD-0002.
- **Merge:** Nathan merges, manually. Afterwards, PR-40 lineage review by the IA.

## 20. Session identity and recovery envelope

```yaml
paused_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (planning context suspended at a boundary finding)
phase: PR-20 pre-Proceed planning; no PR_RETURN_PHASE (no Proceed, workspace vehicle or PR exists for code)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner); authoring session https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
base_identity: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0; PF10 v13.5.2, overlays NONE
checkpoint_identity: this artifact (v1.0, PENDING) and docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md
completed_work: inventory, per-file sweep, 135 dispositions (133 decided), S04/S05 design, integrated prototype (scratch only, never pushed)
pending_decision: RS-20 on RP-1 and RP-2 (whole-change IA)
resume: on the RS-20 decision, this PR-20 context writes plan v1.1 (complete successor) and presents it at AWAITING_PO_PROCEED
scratch_state: TRANSIENT_SCRATCH only (prototype diffs and clones in the session scratchpad); this plan is self-sufficient without them
```

## 21. TypeSafe reading for the receiving session (RS-20, continuing whole-change IA)

Action sent (v6): "Review, as the whole-change Implementation Agent and first reviewer of this new request, a rescope request from the PR planning session of the first unit of an approved CRD Implementation Plan: two boundary findings, each with a proposed bounded delta — two governed evidence tools (a 4,800-line generator and a 3,200-line analyzer) left stale by an earlier Reader route change, whose repair the unit's instruction excluded from its file list (proposal: add the two tool files and their owner registrations to the unit), and a legacy chart-loader defect that canon assigns to a separate future build item (proposal: retire one test file and route the defect to the Product Owner) — then decide approve, reject, revision required, in-scope repair or specification change, and write the review and, only on approval, one build-notes addendum. It reads the request, the 135-file planning draft it suspends, the approved Plan, Specification and canon; no code is written and no live provider call occurs; a revised detailed PR plan, a Product Owner Proceed, implementation and independent reviews follow."

- **TypeSafe v6: Fable 5.1, extra high.** Effort score 3.29 (confidence 0.54); rung probabilities low 0.00, medium 0.00, high 0.16, extra high 0.37, max 0.47, ultracode 0.00. Model probabilities Fable 5.1 0.58, Opus 5.5 0.42 (confidence 0.16). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.00, Opus 5.5 at high 0.07, Opus 5.5 at extra high 0.16, Opus 5.5 at max 0.20, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.09, Fable 5.1 at extra high 0.21, Fable 5.1 at max 0.27, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and max; model near tie. Sent 2026-10-12T22:27:59Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T22:27:59Z; HTTP 200 in 0.8 s; 4338 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Fable 5.1 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between extra high and max; model near tie.
- **One send**, taken before this artifact and the rescope request were saved; recorded identically in both. No Notion row was written (PR-20 directs that it is not).
- **Nathan's pick for RS-20:** not stated.
- **Nathan's pick for this PR-20 session:** not stated (the reading for PR-20 is in instruction v1.0 §19).

**Surface advice:**
- Run RS-20 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the continuing whole-change IA role for HDE-CRD-0002 (the role that issued instruction v1.0 under PR-10). The proposal's author is this PR session, so author/reviewer independence holds.
- **What it reads:** the rescope request and this plan. It re-checks the two findings against `main` by running `tests/evidence/test_hdapi_v2_contract_inventory.py` at `a8c99d1` and at `cf9198df` in a throwaway clone with full history and `ruby` on `PATH` (about two minutes each), and by reading `engine/charts/loader.py` lines 50–100. It also reads `docs/pfcanon/` on `main`, including PF02 §1.1, PF09.3 HDE-SEPA006 and PF12 §8.6.3.10.
- **What it needs:** no live vendor, production or database access. It writes only its review artifact, plus one addendum only on `APPROVE`.
- **Prerequisite:** the pull request carrying this plan and the request should be merged to `main` first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-20 / WU-PR-01 / plan 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by review v1.1) |
| instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md`, v1.0 |
| work unit / requirements | WU-PR-01; S03, S04, S05 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (retrieved 2026-10-12; page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-01 PR engineering session / PR-20 |
| capture time | 2026-10-12T22:36:44Z |
| execution identity | https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8 |
| inherited prompt uses | IA-10 (Audit v1.0), IA-40 (Plan v1.1), IA-30 (review v1.1 §7), PR-10 (instruction v1.0 §20) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `a8c99d1` (`docs/changes/` holds `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`); recorded here only; owner of any later installation: GCFPE-MGMT-10 and the Product Owner |

## Canon relied on

Read on `main` at `a8c99d1`; `docs/pfcanon/` is unchanged since `df23bbf` (#614).

**Read by this session:**
- **PF10-HDE-Build-Notes v13.5.2:** read in full. Addendum 2.1 governs §21 only, and it is silent on S03–S05.
- **PF04-Canon-HDE-Governance v2.8.7:**
  - §9.1.1, the role table (the dedicated PR session authors the detailed per-PR Plan; Nathan's Proceed is its approval) and the approval-map paragraphs;
  - §9.7.7 "Plan approval gate" (the `ASK OK? — PR IMPLEMENTATION PLAN` hold; artifact-level detail; no proof by intent; retrieval-first review; negative proof);
  - the review-boundary bullets (Implementation Plan review boundary; plans are approval artifacts, not execution artifacts);
  - §9.7 path validation, "Planning audit posture", file minting with absence proof, and "No fabricated required paths".
- **PF27-Canon-Plan-Templates v2.0.5:** "CI lane classification and automated budget-control discipline" (full: smallest correct lane; administrative closeout never ordinary required PR CI; no hidden failed or unexecuted work), "Repository loci and file minting" (full) and "Artifact execution boundary" (full).
- **PF06-Canon-Change-Process-Guide v2.5.4:** §1.0.6 (CI success alone is not QA acceptance), and §3.5.1 "Requirement", opening paragraphs (PR route; each PR self-contained; the Product Owner is the sole merger).
- **PF19-Canon-Glow-QA-Guide v3.0.6:** "Change-lane QA applicability (normative)" (no QA artifact in a PR unit; the CRD QA root).
- **Canon lines citing the 135 files:** read at each citation: PF09.5 lines 322, 2108; PF09.1 lines 1042, 1146, 1166, 2053; PF09.6 line 1756; PF14 lines 5557, 6561, 6721, 7653; PF09.2 lines 299, 301, 677; PF05 line 837; PF09.4 lines 429, 2139.

**Read by the planning workers and reported with their evidence** (relied on for the per-file reasons in §7; not re-read in full by this session):
- PF02 Architecture §1.1, §2.1, §3.4, §6.2;
- PF05 CLI/API/Vendor Ref §3.3, §3.4, §4.1.3, §4.1.6, §4.2, §5.1.6, §5.2, §5.3, §5.4, §7.1.11a–f, §7.2, §8.1, Appendix A;
- PF01 Math Spec §1, §3.3, §5.2, §6.1, §6.4, §10.2, §12, Appendix E;
- PF04 §2.3, §10.3, §10.5, §11.2.4, Appendix OI-005;
- PF12 §8.6.3.5, §8.6.3.10;
- PF14 §3.1.1, §4.2, §5.1, §19.2;
- PF09.1 HDE-CALC003.7, 003.10, 004.7; PF09.2 HDE-DISS001.3, .6, DISS003; PF09.3 HDE-SEPA006 and .1/.2/.3;
- PF29 §1.2, §16; PF07 production rails.

**Operative documentation:** `AGENTS.md` (canon-first; closed rails; pytest readiness; QA output placement; CI-exempt paths; PR description rules; no hand-edited governed artifacts; Evidence attribution).

**In-flight documents:** the instruction v1.0 (in full); Plan v1.1 and review v1.1; Specification v1.1 (S03–S05 rows, Exclusions, Constraints, Distillation row); Audit v1.0 (§3, §5.2, §5.3, §5.7, S03–S05, §7.5).

**Prompts:** PR-20, PR-30, RS-10 and RS-20 (100926.1, in full); the hub; the register's current selection.

## Checks run by this session

| Check | Result |
| :- | :- |
| Inventory at `a8c99d1` (§4.1) | 278 / 49 / 135 owners / 94 targets / 70 roots / 135 uncovered / 130 O-11; equals instruction §5.1 |
| Absence: `test ! -e tests/retired_tests.md` | PASS |
| `git diff --stat a429c7c a8c99d1 -- . ':!docs/ephemeral'` | empty |
| Per-file sweep (§4.2) | 135 files; 638 tests: 548 passed, 76 failed, 14 errors; 87 / 32 / 14 / 2 files; 12 visible writers |
| Lane shape, existing 94 targets | 2,773 passed in 291 s; clean |
| Lane shape, 94 targets + 80 clean uncovered files | 3,024 passed in 322 s; clean |
| S04/S05 prototype pinned suites | 286 passed; both negative controls fail as intended |
| RP-1 re-verification (ruby on PATH) | `a8c99d1`: 21 failed, 277 passed; `cf9198df`: 298 passed; clean |
| Integrated prototype: coverage | 2 uncovered (the RP-1 and RP-2 files) |
| Integrated prototype: pinned suites | 313 passed, 1 failed (coverage guard, the same 2 files) |
| Integrated prototype: classifier dry run `a8c99d1..b1a67f1` | exit 0; seven lanes; 162 targets = full-validation set |
| Docs-only classifier dry run | `documentation_only`; no lane; `changed_tests=false` |
| Integrated prototype: 162 full-validation targets in a detached worktree | 2,962 passed in 327.6 s; diff and status clean; mtime: 11 same-byte rewrites, all from two covered tests outside the unit (OBS-4); the 68 retained files alone: 189 passed, nothing touched |
| TypeSafe reading (§21) | HTTP 200; Fable 5.1 at extra high |

Not executed by this session: the fixed-lane pre-steps and lane lists on the prototype; the release attestation build; hosted CI; Codex code review; security review. Those belong to PR-30 and PR-35.

---

**State:** `PENDING`. This is the WU-PR-01 detailed PR implementation plan v1.0: a complete planning draft, suspended for the RS-20 decision on `docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md`. On that decision, this PR-20 context writes v1.1 for Nathan's Proceed.
