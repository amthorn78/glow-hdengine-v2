---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md
artifact_version: "1.1"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.0.md (v1.0, PENDING, suspended at RS-20; blob 1279c0f6047ead0a00fb938b75c3fd5e1f9c1a74; 103,859 bytes; landed on main at 6c664dd, amthorn78/glow-hdengine-v2#624). This v1.1 is its complete successor; v1.0 is preserved unchanged
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 24597a31fbb910a4d36106a1aa2d5b861faec976; 54,620 bytes; landed on main at a8c99d1, amthorn78/glow-hdengine-v2#623)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c) — lineage only
RESCOPE_REQUEST_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md (v1.0, items RP-1 and RP-2; blob 1a8d95b55aaa811ad687831955696cf268c78d8c) — decided
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md (RS-20, whole-change IA, decision APPROVE; blob eccab2187769262ecb4c99374cc9e73674dd37e6; landed on main at 7936b4b, amthorn78/glow-hdengine-v2#625)
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10)
applicable_pf10_overlays: PF10 addendum 2.2 (HDE-CRD-0002 WU-PR-01 rescope), approved by RESCOPE_REVIEW_ID
effective_baseline: approved base + applicable PF10 overlays = the base above + PF10 addendum 2.2
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3, effective 2026.10.12; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; 26,372 bytes; sha256 bcb0b438585c99a3a7333f2766a3c960cd381571f449a38eca6c75464c100c7d; read in full; one unlettered document; active addenda 2.1 and 2.2)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md § "2.2 HDE-CRD-0002 WU-PR-01: two HDAPI v2 contract-inventory evidence tools join the CI-coverage work unit for bounded corrections; the legacy chart-loader test is retired with its defect routed to the Product Owner" (controlled PF10); its record as approved: docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md (PF10_BUILD_NOTES_ADDENDUM, addendum_id HDE-CRD-0002-WU-PR-01-RESCOPE-1, proposed number 2.2; blob 7a14f0cad47e6f80cb58d3c77269e954f631a824). The two texts are identical apart from Markdown formatting (§3)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (unchanged; the same dedicated session resumed its PR-20 planning context after RS-20)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); last known and authoring session https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
author: dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
prompt_release: GCFPE-20261009.1 / 100926.1 / 55 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", read 2026-10-12)
created_at: 2026-10-13T00:12:19Z
repository_baseline: origin/main 9c767d24761c61fb764c04004eac769ab25e2e88 ("PF10 update"). git diff a8c99d1..9c767d2 outside docs/ephemeral/ and docs/pfcanon/ is empty; under docs/pfcanon/ the only change is PF10 v13.5.2 → v13.5.3 (addendum 2.2 added)
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry (§18)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), same dedicated session, on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-01 — Detailed PR Implementation Plan v1.1

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.7.7).

This is the complete, executable plan for WU-PR-01 within approved scope: the approved base plus PF10 addendum 2.2. It plans all 135 uncovered test files, S04 and S05. Every in-scope change was applied together in a scratch prototype on the current `main` and verified (§4.3).

The two boundary findings of v1.0 are decided. The whole-change IA approved the rescope request v1.0 through RS-20 (`APPROVE`, one state):
- **RP-1** is an approved bounded delta. Two `tools/evidence/` files join the unit for exactly the corrections addendum 2.2 states (§5.8).
- **RP-2** is in scope under the base. The loader test is retired under class (b), and its defect is routed to the Product Owner (§7 row 97).

What v1.1 changes from v1.0:
- §1–§4, the front matter and the identity: the decision, PF10 v13.5.3 and the new baseline `9c767d2`;
- §5.1 and §5.8: the RP-1 design, verified;
- §6 and §7: the two routed rows are decided, giving 42 retained, 27 retained and fixed, and 66 retired;
- §8–§17 and §19–§22: the results of the decision;
- the TypeSafe reading, which is now for PR-30.

Everything else is carried from v1.0 unchanged.

What this artifact does not do:
- It authorizes no implementation, merge, publication, Ops, QA, acceptance or closure.
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md` (v1.1) authorizes implementation, and only Nathan merges.
- It changes no canon. It creates no PF10 addendum: addendum 2.2 is the IA's overlay, published by the Product Owner.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| `CHANGE_CLASS` / `CHANGE_ID` | `CRD` / `HDE-CRD-0002` |
| `WORK_UNIT_ID` | `WU-PR-01`: CI coverage of every test file; Distillation; S03, S04, S05 |
| `PR_INSTRUCTION_ID` | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md` (v1.0, `INSTRUCTION_READY`), unchanged. Addendum 2.2 extends its §6 and relaxes its §7 exactly as stated there |
| `IMPLEMENTATION_PLAN_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (v1.1; the approved representation is the unchanged body plus `PLAN_REVIEW_ID`) |
| `PLAN_REVIEW_ID` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md` (Isis, IA-30 `INITIAL_APPROVE`, `ASK OK.`) |
| `SPECIFICATION_ID` | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (Thoth, CF-C-30 `INITIAL_APPROVE`) |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md` (lineage only) |
| Rescope | request v1.0 (this session, at PR-20) → `RESCOPE_REVIEW_ID` `docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md` (RS-20, `APPROVE`; binding conditions B-1 to B-14 in its §6) |
| `REMEDIATION_REVIEW_ID` | none |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md`, the unique current controlled PF10 (one unlettered document). Addenda: 2.1 governs the TypeSafe reading (§21); 2.2 governs WU-PR-01's RP-1 files and the RP-2 retirement. For the rest of S03–S05, PF10 is silent ("Silence rule"), so permanent canon governs |
| Active addenda | 2.2 (applicable to this unit); 2.1 (applicable to §21 only) |
| Effective baseline | approved base + applicable PF10 overlays = Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0, + PF10 addendum 2.2 |
| Dependency state | Ready (instruction §3: "First. No upstream dependency"). No HDE-CRD-0002 code unit has landed |
| Predecessor attempts | plan v1.0 (`PENDING`, suspended at RS-20; preserved). No Proceed, vehicle, branch or PR for code exists (the open-PR list at authoring holds none for this unit) |

## 3. Sources

**Inputs read in full for v1.1:**
- the rescope review v1.0, the addendum v1.0, and the RS-20 checkpoint and handoff;
- PF10 v13.5.3, resolved afresh. Its addendum 2.2 was compared with the addendum v1.0: after removing Markdown emphasis, backslash escapes, list markers and whitespace, the two texts are identical (12,228 characters each);
- this session's own request v1.0 and plan v1.0.

The instruction v1.0, Plan v1.1, review v1.1 and Specification v1.1 are unchanged since v1.0 (same blobs) and were read then as recorded in v1.0 §3.

**Canon read for v1.1 on `main` at `9c767d2`:** PF05 §5.1.0 and §5.4 in full, for the B-2 baseline review (§5.8.1). PF10 v13.5.3 in full. The list is under "Canon relied on".

**Repository read for RP-1 at `9c767d2`:**
- `tools/evidence/hdapi_v2_boundary_analyzer.py`: lines 20–100, 480–560, 904–945, 1097–1215, 1466–1530, 1791–2295 (`_adapter_routes_without_presenter` in full) and 2868–3130;
- `tools/evidence/generate_hdapi_v2_contract_inventory.py`: lines 1–31, 130–140, 2375–2390, 3650–3665 and 4117–4301, plus every `boundary_analyzer.` use;
- `adapter/http_reader.py`: lines 495–585, 700–730, 1074 and 1163–1175; `adapter/factory.py` lines 9–13; `adapter/wsgi.py` lines 11–25;
- `ci/checks/classify_ci_changes.py`: the owner registries (lines 345–390, 478–494, 603–735 and 1038–1078);
- `tests/evidence/test_hdapi_v2_contract_inventory.py`: all 103 `tmp_boundary_test` sites, checked with `ast`, plus lines 1–80, 940–950, 1130–1300, 2385–2430, 2862–2890 and 3450–3660;
- `tests/evidence/test_http_reader_ci_ownership.py` (lines 1–150) and `tests/evidence/test_evidence_tool_ownership.py` (lines 1–45);
- `tests/evidence/test_rails_ci_workflow_integration.py`: lines 440–470, 642–682, 1020–1040 and 1076–1150.

**External:** carried from v1.0 (GitHub path-filter syntax; `actions/runner-images` `Ubuntu2404-Readme.md`, image 20261004.327.1, "Ruby 3.2.3").

## 4. Repository baseline (re-verified at `9c767d2`)

### 4.1 Inventory

**Baseline drift.** `git diff a8c99d1 9c767d2` outside `docs/ephemeral/` and `docs/pfcanon/` is empty. Every non-documentation path is therefore byte-identical to v1.0's tested state.

The v1.0 inventory stands, recomputed by the instruction's §5.1 definition:

| Set | Count at `a8c99d1` = `9c767d2` |
| :- | -: |
| Tracked `tests/**/test_*.py` | 278 |
| Reached by a `ci.yml` lane `python -m pytest` token | 49 |
| `_registered_owner_test_paths()` | 135 |
| `_full_validation_test_targets()` | 94 |
| Under a `pytest.ini` `testpaths` root | 70 |
| **Strict uncovered set** (no lane token, no full-validation target) | **135** |
| Of which O-11 (no lane, owner or `pytest.ini` root) | 130 |
| Of which the five `_FULL_VALIDATION_INACTIVE_TESTS` | 5 |

### 4.2 Per-file sweep

v1.0 §4.2 stands unchanged. Its tested state was `a8c99d1`, which is content-identical to `9c767d2` outside documentation:
- 135 files run alone; 638 tests: 548 passed, 76 failed, 14 collection errors;
- 87 files passed completely, 32 had failures, 14 could not be collected and 2 collected no test;
- 12 files wrote visibly and 9 more wrote invisibly (same-byte rewrites caught by the mtime check).

### 4.3 Integrated prototype v1.1 (this session)

Every in-scope change of §8 was applied together in a scratch clone and committed there as `180a376` on `9c767d2`. It was never pushed. It consists of v1.0's integrated prototype (`b1a67f1`, re-applied cleanly), the RP-1 prototype (§5.8) and the RP-2 retirement. The diff is 100 files: 33 modified, 66 deleted, 1 added; 1,953 insertions and 6,387 deletions.

Checks on `180a376`, all under the closed rails of §9 step 2, with Python 3.12.3, CI's install and `ruby` 3.3.6 on `PATH`:
- **Coverage.** The §4.1 computation leaves **0** files uncovered. Counts: 212 tracked test files, 49 lane-reached, 163 full-validation targets and 204 registered owners. No inactive entry remains.
- **Pinned suites.** `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/qa/test_qa_tool_ownership.py`, `tests/evidence/test_http_reader_ci_ownership.py` and `tests/evidence/test_evidence_tool_ownership.py`: 314 passed, 0 failed. The new coverage guard passes.
- **Classifier dry run** (`--base 9c767d24… --head 180a376b… --event-name pull_request`): exit 0; seven lanes; `changed_tests=true`; 100 paths. The 163 changed-test targets equal `_full_validation_test_targets()`.
- **Documentation-only dry run** (`docs/run/RUN_PROD_QA.md` plus new files under `docs/crd/`, `docs/qa/` and `docs/plans/`): exit 0; `reason=documentation_only`; no lane; `needs_python=false`; `changed_tests=false`.
- **Full-validation shape** (all 163 targets in one pytest process, in a detached worktree): 3,262 passed in 430.0 s; exit 0; `git diff --exit-code` 0; `git status --short --untracked-files=all` empty. The mtime check finds the same 11 tracked files rewritten with identical bytes as in v1.0. All come from the two covered tests of OBS-4: `tests/evidence/test_bodygraph_policy_proofs.py` (9 paths under `artifacts/bodygraph/` and `schemas/bodygraph_source_invariance.*.v2.json`) and `tests/reader_v1/test_release_pack.py` (`artifacts/release_id.txt`, `artifacts/release_pack_manifest.json`). A first pass of the check used a malformed `find` call and listed nothing. It was recomputed correctly on the same post-run worktree, where `README.md` also appeared; that came from this session's own `touch` used to test the check, not from a test.
- **The 69 retained files alone:** 489 passed in 140.8 s; exit 0; `git diff --exit-code` 0; empty `git status --short --untracked-files=all`; no tracked file newer than the marker (fresh detached worktree, correct mtime check). The `ruby`-dependent file is included. v1.0's equivalent run (68 files) gave 189 passed.
- **The contract-inventory file alone:** 300 passed in 106.2 s; exit 0 (fresh detached worktree of `180a376`, correct mtime check). Afterwards: `git diff --exit-code` 0; empty `git status --short --untracked-files=all`; no `tmp_boundary_test/`; no tracked file newer than the marker. The only path whose mtime moved is the `adapter/` directory itself, from F-10's transient module writes. An earlier single-file run (103.4 s, also 300 passed) used the malformed mtime call noted under the full-validation shape, so it is not relied on for the mtime result. Without `ruby` on `PATH`: in a fresh detached worktree with `ruby` absent (`command -v ruby` finds nothing): 9 failed, 291 passed, 0 skipped; exit 1. Every failure raises `FileNotFoundError: [Errno 2] No such file or directory: 'ruby'`. The tree is clean afterwards and no tracked file was touched.
- **B-5 checks** (§5.8.7): the governed-path diff is empty, the import lines of both tools are unchanged, and `tests/evidence/test_architecture_snapshot.py` gives 5 passed.
- **Ledger.** The table's 66 retire rows, the ledger's 66 rows and the 66 deleted paths are the same set.

### 4.4 Facts that correct or extend the instruction

F-1 to F-4, F-7 and F-8 are carried from v1.0 §4.4 unchanged:
- **F-1:** path proofs under the documentation prefixes carry the evidence lane, so the S05 filter re-includes them.
- **F-2:** `tests/adapter/test_gate_auth.py` exercises only `GET /internal/version`.
- **F-3:** the "S14 environment classification" files exercise `env_guard` and `provider_loader`, not the CLI gate.
- **F-4:** additional consumers of uncovered files and the two pins.
- **F-7:** `test_resolver_vendor.py` already runs in the rails lane through `ci/jobs/*.yml`.
- **F-8:** `test_vendor_and_prod_guard.py` leaks a session-wide environment change.

F-5 and F-6 are now decided, and F-9 to F-11 are new:

| ID | Fact (at `9c767d2`) | Effect on this plan |
| :- | :- | :- |
| F-5 (decided) | `tests/evidence/test_hdapi_v2_contract_inventory.py`: of its 26 sweep failures, 5 need only `ruby` (the generator calls it at line 2530) and 21 are tool drift since `d79cfc1c`. With the drift corrected, 9 tests depend on `ruby` (§5.8.5) | RP-1 approved (addendum 2.2): retain and fix, with §5.8's two tool corrections |
| F-6 (decided) | `engine/charts/loader.py:76–82` `_call_legacy` calls `get_chart` on a `FixturesProvider` that has none (since `6c6f4b2a`) | RP-2 in scope under the base: the file is retired under (b), and the defect goes to the Product Owner (HDE-SEPA006). `engine/charts/loader.py`, `engine/provider/fixtures.py` and `artifacts/logs/loader_call.jsonl` are unchanged |
| F-9 | The analyzer ties a blueprint route to its mount through the variable name passed to `register_blueprint`. In `adapter/http_reader.py`, both `get_reader_bp` and `get_reader_api_bp` name their local blueprint `bp`. The module `bp` is registered with `url_prefix=""`, and the production blueprint is registered as `api_bp` at `/api`. So the discovered records of `reader_post` and `reader_method_not_allowed` carry `route_path=/reader`, and the `/api` mount appears in the three `register_blueprint` records (`factory.py` `api_bp`, `http_reader.py` `api_bp`, `wsgi.py` `reader_api_bp`) | B-2's "at `/api`" is met the way the analyzer represents routes (§5.8.1). Changing discovery is outside B-3's confinement. Routed as OBS-13 |
| F-10 | `test_epic034_presenter_bypass_detects_imported_adapter_helper` writes `adapter/boundary_tmp_helper.py` and `adapter/boundary_tmp_route.py` into the tree and removes them in `finally`. It is not among the 103 `tmp_boundary_test` sites | Not moved: B-7 names the 103 sites. The clean-tree and mtime checks pass after the run. Routed as OBS-14 |
| F-11 | The frozen `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log` names both tools as inspected loci, but records no tool hash. No check binds the tools' bytes to a governed artifact other than the architecture snapshot, which records import symbols only | The tool corrections leave every governed artifact valid without regeneration (B-5) |

## 5. Design

### 5.1 Registration model

**Rule (one for every retained file).** Each retained file that no `ci.yml` lane list reaches joins the **configured suite**:
- an explicit file entry is appended to `pytest.ini` `testpaths`, unless the file already lies under a root;
- the path is added to `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` in `ci/checks/classify_ci_changes.py`, sorted.

That is the classifier's existing mechanism for owner tests with no single source owner. `tests/evidence/test_rails_ci_workflow_integration.py::test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned` pins it: `configured == fixed | supplemental | inactive`.

An owner-registered file is also in supplemental. That is the existing convention: 43 supplemental entries in the prototype are also owner targets, among them `tests/adapter/test_gate_auth.py`.

Effects:
- the file becomes a full-validation target, run by the changed-test step in the detached worktree on every full-validation change and whenever the file itself changes;
- `pytest.ini` gains **68** file entries (`tests/qa/test_epic021_scaffolding.py` is already under the `tests/qa` root);
- the supplemental tuple grows from 40 to **109**.

**Owner additions** (only to owner tuples that already exist, or where a contract or an executing consumer requires them; the two new keys are addendum 2.2's exception):

| Source key (registry) | Added owner targets | Basis |
| :- | :- | :- |
| `adapter/http_reader.py` (`_HTTP_READER_TEST_OWNERS`, and `_HTTP_READER_INDIRECT_TEST_OWNERS`) | `tests/adapter/test_gate_auth.py` | C-2; indirect consumer (F-2). Both sets are required: `test_http_reader_owner_registry_matches_current_consumers` asserts `direct_consumers == registered_direct` |
| `adapter/http_reader.py` (both sets, as above) | `tests/evidence/test_hdapi_v2_contract_inventory.py` | B-9 (§5.8.6). The file reads `adapter/http_reader.py` as an analyzer locus and does not import it, so it is indirect |
| `adapter/factory.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/evidence/test_hdapi_v2_contract_inventory.py` | B-9 |
| `adapter/wsgi.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/adapter/test_compat_writer_transport.py`, `tests/adapter/test_headers_and_determinism.py`, `tests/evidence/test_hdapi_v2_contract_inventory.py` | The first two test the wsgi app. The third is B-9: `wsgi.py` is the third app factory whose public records the baseline encodes (D-6) |
| `engine/bodygraph/resolver.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_bg_resolve_route_policy.py` | C-1 (WU-PR-04 extends the first); both exercise `_resolve_vendor` and the route policy |
| `engine/bodygraph/vendor_client.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/bodygraph/test_bg_resolve_route_policy.py` | Exercises `classify_bg_resolve_route_policy` |
| `engine/http/compat_handler.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/adapter/test_compat_writer_transport.py` | Writer transport of `/api/compat/v1` |
| `engine/stable/sercanon.py` (`_PRODUCT_TEST_OWNER_PATHS`) | `tests/infra/test_sercanon_bytes.py` | Release member under test |
| `tools/evidence/regenerate_identity_closure.py` (`_EVIDENCE_HELPER_TEST_OWNERS`) | `tests/evidence/test_internal_version_manifest_captures.py`, `tests/evidence/test_aux_preview_identity_parity.py` | Executed by the closure (lines 278–283, 372–381); consumers-first rule §9.5 |
| `tools/evidence/generate_bodygraph_policy_proofs.py` (`_EVIDENCE_GENERATOR_TEST_OWNERS`) | `tests/evidence/test_refresh_policy_snapshot.py` | PF14 §19.2 requires the guard to stay green; it asserts the ADR values |
| **new key** `tools/evidence/generate_hdapi_v2_contract_inventory.py` (`_EVIDENCE_GENERATOR_TEST_OWNERS`) | `("tests/evidence/test_hdapi_v2_contract_inventory.py",)` | B-6, addendum 2.2 |
| **new key** `tools/evidence/hdapi_v2_boundary_analyzer.py` (moves from `_EVIDENCE_HELPERS_REQUIRING_OWNER` to `_EVIDENCE_HELPER_TEST_OWNERS`) | `("tests/evidence/test_hdapi_v2_contract_inventory.py", _EVIDENCE_HELPER_OWNERSHIP_TEST)` | B-6, addendum 2.2. `test_evidence_helper_owner_registry_is_exhaustive_and_exact` (mapped ∪ blocked = tracked; disjoint; the ownership test in every tuple) stays true |

**No other new source key is created.** A new key changes the classifier's verdict on an edit to that source, from refusal (`CI_PRODUCT_OWNER_TEST_MISSING`, `CI_EVIDENCE_OWNER_TEST_MISSING`) to owner-tested. S03–S05 do not require that decision, and the units that edit those sources make it.
- The candidates are listed for their owners in §17 (OBS-10).
- One prototype proposed an `adapter/env_guard.py` key; it is excluded under this rule (D-1).
- The two keys above are the only exception, by addendum 2.2.

**No new fixed-lane entry.** Every retained file is a full-validation target, the smallest correct lane (Plan Templates, "CI lane classification and automated budget-control discipline"). The `ci.yml` lane lists are unchanged (C-4).

### 5.2 S04: `tools/qa/` fail-closed for `.py`, `.sh` and `.sql`

Unchanged from v1.0 §5.2.

In `_qa_tool_owner_targets`, replace the suffix test `rel.suffix.lower() != ".py"` with `rel.suffix.lower() not in _UNKNOWN_SOURCE_SUFFIXES`. That is the same set `_bodygraph_tool_owner_targets` uses.
- An unregistered `tools/qa/*.sh` or `*.sql` (any case) then raises `CI_QA_OWNER_TEST_MISSING`, as a `.py` does today.
- Registered `.py` behaviour is unchanged, and so are the lanes (`{"evidence", "qa"}`).
- `tools/qa/` holds no `.sh` or `.sql` file, so no current path changes verdict.

Pinned tests, in `test_qa_tool_owner_policy_is_exhaustive_and_deduplicated`:
- the `tracked` set over `_UNKNOWN_SOURCE_SUFFIXES`;
- `.sh`, `.sql`, `.SH` and `.SQL` each raise `CI_QA_OWNER_TEST_MISSING`;
- a `.md` file yields no owner target.

A negative control (the classifier line reverted) fails.

### 5.3 S05: workflow path filter

Unchanged from v1.0 §5.3. Both `on.pull_request` and `on.push` (branch `main`) replace `paths-ignore` with this ordered `paths` list:

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

The reasons, the new pinned test `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths` (four checks), its negative control and the matcher limits (R-3) are as in v1.0 §5.3.

### 5.4 Inactive set

Unchanged from v1.0 §5.4:
- `tests/qa/test_epic021_scaffolding.py` is retained and joins supplemental;
- the other four inactive files are retired;
- `_FULL_VALIDATION_INACTIVE_TESTS` becomes an empty `set[str]` with a comment;
- the `CI_INACTIVE_TEST_REQUIRES_DISPOSITION` mechanism stays, with a monkeypatched synthetic case so its pinned loop is not vacuous.

### 5.5 Other pinned-test edits (all in `tests/evidence/test_rails_ci_workflow_integration.py`)

- **New `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target`** (acceptance (1); the instruction §5.1 / C-3 set). In the v1.1 prototype it passes: 0 unreached.
- **`test_change_classifier_executes_against_exact_git_refs`** (lines 1323, 1339): the "unlisted test" example is renamed to the unregistered `tests/adapter/test_unlisted_adapter_regression.py`.
- **`test_http_reader_owner_guard_is_selected_without_fixed_lane_duplication`** (pinned tuple at lines 664–679 at `9c767d2`): gains `"tests/adapter/test_gate_auth.py"` after `tests/adapter/test_diagnostic_writer.py`, and `"tests/evidence/test_hdapi_v2_contract_inventory.py"` before `guard` (B-9; sorted position).
- **S04 and S05 tests:** §5.2 and §5.3.
- **Inactive refusal case:** §5.4.

No other pin over the owner registries changes. In the prototype, every pin over the registries stays true (addendum 2.2: "every pin over the owner registries stays true"):
- `_EVIDENCE_GENERATOR_TEST_OWNERS` loop, lines 452–455;
- `_EVIDENCE_HELPERS_REQUIRING_OWNER` loop, line 1027, now over four helpers;
- the roster test;
- the two ownership guard files.

### 5.6 Retirement mechanics and ledger

As v1.0 §5.6, with 66 rows:
- **Retirement is deletion** (`git rm`), never a skip marker, `xfail` or exclusion list (instruction §7 bullet 4).
- **Registrations leave with the file.** A retired file stays in no registry and not in `pytest.ini`. None of the 66 is registered today except the four inactive entries, which leave with §5.4.
- **`tests/retired_tests.md`** is new.
  - Absence check: `test ! -e tests/retired_tests.md` passes at `9c767d2`. PR-30 repeats it at its base, and if it fails, stops and records what exists.
  - Format: one Markdown table, one row per retired file, with the columns path, reason, retirement date (the PR-30 implementation date) and replacing coverage.
  - Rows are sorted by path and taken verbatim from §7's retire rows. The classifier gives `tests/*.md` no lane.
- **The loader row (B-11, B-13, B-14).** Its reason:
  - states the `_call_legacy` defect and its origin (`6c6f4b2a`);
  - states that only tests call the legacy signature, and that the loader is neither a release member nor reached at runtime;
  - names RS-20 review v1.0 (PF10 addendum 2.2) as the route by which the defect goes to the Product Owner for HDE-SEPA006;
  - records that the file was the only test writer of the tracked `artifacts/logs/loader_call.jsonl`, which is unchanged.

  Its replacing coverage is the two `tests/provider` cases of B-11. It does not say the defect is fixed, deferred to a unit of HDE-CRD-0002 or resolved. PR-30 writes §7 row 97's reason verbatim. The prototype's ledger row carried the same content in slightly earlier wording.
- **Orphaned fixtures are not deleted** (OBS-8).
- **Historical governed records stay unchanged.**

### 5.7 Fix patterns (test code only)

Unchanged from v1.0 §5.7:
- `monkeypatch.chdir(tmp_path)` for product code that writes relative to the working directory;
- a `_Path` monkeypatch for the loader log;
- `ROOT` or output redirection for generator tests that run write mode;
- `monkeypatch` for environment and `sys.modules` state;
- current-contract assertions for stale expectations;
- anchored patterns for the two false-positive guards;
- `pytest.raises` for the vacuous assertion.

The RP-1 file adds one pattern of the same kind: untracked fixture writes under the repository root move to `tmp_path` (§5.8.4).

### 5.8 RP-1: the two tool corrections and the contract-inventory file (PF10 addendum 2.2)

This section is the verified design that review §13 asked for: prototyped in a throwaway clone with `ruby` on `PATH`, then integrated (§4.3). It maps to binding conditions B-1 to B-9. B-10 to B-14 are mapped in §16.

**B-1, the loci.** Exactly two tool files join the unit's bounded files: `tools/evidence/generate_hdapi_v2_contract_inventory.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py`. No other `tools/**` or `scripts/**` file changes. `ci/jobs/*.yml` and `ci/checks/run_rails_job_definitions.py` are unchanged.

#### 5.8.1 Generator: rebuild the baseline data (B-2)

- **What changes.** Only the value of `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS`.
- **Proof that it is data-only.** An `ast` comparison of the module at base and head, with that one value replaced by a constant, is identical. Records go from 23 to 21. Diff: 374 insertions, 584 deletions.
- **What does not change.** No output, schema, evidence family, refusal code, flag, write path or `--check` mode. The generator is never run in write mode against the repository.
- **Rule.** The records are rebuilt from the public route records that the app factories register at the PR head, selected the way the analyzer compares them (`analyze_adapter_boundary`): `asdict(r)` for each record of `discover_route_registrations(ADAPTER_BOUNDARY_ADAPTER_LOCI)` with `parser_status == "supported"`, `public_internal_classification == "public"` and `registration_kind != "blueprint_constructor"`.
  - The records stay in discovery order and are rendered with `pprint.pformat` (default width), the existing layout.
  - At `cf9198df`, where the file last passed, the same rule yields 16 records, each equal to one of the 16 baseline entries the comparison used.
- **What the rebuild changes, exactly.** Of the 23 old entries, 15 are kept unchanged and 8 are removed:
  - `reader_v1_post`;
  - 7 `compat_blueprint` records labelled public in the old value, which the current analyzer classifies internal. These are 5 `/api/compat/v1` route and hook records in `engine/http/compat_handler.py`, and the `compat_blueprint` registrations in `adapter/http_reader.py` and `adapter/wsgi.py`. The comparison already ignored these 7 (D-10).

  6 records are new: the three `/api` registrations, and `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed`.
- **Procedure for PR-30.** Run this scratch script from outside the repository, with the checkout as its argument, under closed rails. It writes only the generator's source file. Then check the diff with the `ast` comparison above.

```python
"""Rebuild ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS (data only) from the
public route records the app factories register in the checkout argv[1].
Scratch helper for HDE-CRD-0002 WU-PR-01 (PF10 addendum 2.2, B-2); not committed."""
import ast, pprint, sys
from dataclasses import asdict
from pathlib import Path
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
from tools.evidence import generate_hdapi_v2_contract_inventory as g
from tools.evidence import hdapi_v2_boundary_analyzer as a
a.ROOT = g.ROOT
records = a.discover_route_registrations(g.ADAPTER_BOUNDARY_ADAPTER_LOCI)
public = tuple(
    asdict(r) for r in records
    if r.parser_status == a.BOUNDARY_ROUTE_SUPPORTED
    and r.public_internal_classification == "public"
    and r.registration_kind != "blueprint_constructor"
)
path = root / "tools/evidence/generate_hdapi_v2_contract_inventory.py"
src = path.read_text(encoding="utf-8")
tree = ast.parse(src)
node = next(n for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS")
lines = src.splitlines(keepends=True)
start = sum(len(l) for l in lines[: node.value.lineno - 1]) + node.value.col_offset
end = sum(len(l) for l in lines[: node.value.end_lineno - 1]) + node.value.end_col_offset
new = src[:start] + pprint.pformat(public) + src[end:]
assert ast.literal_eval(pprint.pformat(public)) == public
path.write_text(new, encoding="utf-8")
print("records:", len(public))
for d in public:
    print(" ", d["source_locus"], d["registration_kind"], d["decorator_path"], d["endpoint"], d.get("route_path"), d.get("register_blueprint_prefix"), d.get("http_methods"))
```

**The 21 rebuilt records, reviewed against PF05 §5.1.0 and §5.4:**

| Source | Kind | Endpoint / prefix | Route, methods | Canon check |
| :- | :- | :- | :- | :- |
| `adapter/factory.py` | hook | `_strip_etag_on_internal` (after_request) | — | not a route |
| `adapter/factory.py` | register | `api_bp` at `/api` | — | §5.4 "production Reader blueprint is mounted under `/api`" |
| `adapter/factory.py` | register | `bp` unprefixed | — | dev/internal blueprint stays unprefixed (§5.4 "Do not move the dev/internal blueprint") |
| `adapter/http_reader.py` | errorhandler | `_compat_scoped_not_found` 404, `_compat_scoped_method_not_allowed` 405 | — | not routes |
| `adapter/http_reader.py` | hook | `_strip_etag_on_internal` | — | not a route |
| `adapter/http_reader.py` | register | `api_bp` at `/api`; `bp` unprefixed | — | as for `factory.py` |
| `adapter/http_reader.py` | route | `aux_narrative` | `/aux/narrative` GET; `/api/aux/narrative` GET | §5.4 "auxiliary narrative surface is served at `/aux/narrative`". The `/api` alias was already in the old baseline |
| `adapter/http_reader.py` | route | `reader_v1` | `/reader` GET | §5.4 dev `GET /reader`, `v=1` only |
| `adapter/http_reader.py` | route | `reader_post` | `/reader` POST; production blueprint, mounted at `/api` (F-9) | §5.1.0 "The production route is `POST /api/reader`" |
| `adapter/http_reader.py` | route | `reader_method_not_allowed` | `/reader` DELETE, GET, HEAD, OPTIONS, PATCH, PUT; production blueprint at `/api` | §5.1.0 "Every method other than `POST` at `/api/reader` … returns the governed `405`". Extension methods are refused by the blueprint's app hook, which is not a route record |
| `adapter/http_reader.py` | route | `reader_post_not_allowed` | `/reader` POST; dev blueprint, unprefixed | §5.4 "unprefixed `POST /reader` is a `405` stub" |
| `adapter/logging_filter.py` | hooks | `_keys_only_after`, `_start_timer_and_cid` | — | not routes |
| `adapter/wsgi.py` | errorhandler | `_not_found` 404, `_method_not_allowed` 405 | — | not routes |
| `adapter/wsgi.py` | hook | `_ensure_common_headers` | — | not a route |
| `adapter/wsgi.py` | register | `reader_api_bp` at `/api`; `reader_bp` unprefixed | — | as for `factory.py` |

The table accounts for all 21 records; the rows that list two endpoints or two registrations count two each. `reader_v1_post` is absent. §5.4 "There is no `/api/reader-proof/v1` route": none is present.

**Reading of B-2's "at `/api`".** `reader_post` and `reader_method_not_allowed` are mounted at `/api` through the production blueprint. In the analyzer's record model, that mount is carried by the `register_blueprint` records, and the route records show `/reader` (F-9). `reader_post_not_allowed` is, by PF05 §5.4 and the code, the unprefixed stub, so placing it at `/api` would contradict both. The baseline holds all three records as the factories register them, plus the three `/api` mounts. This is how plan v1.1 meets B-2. If the IA reads B-2 as requiring different records, that needs a discovery change, which is outside B-3's confinement and would be a new finding.

#### 5.8.2 Analyzer: presenter provenance through a module-level helper (B-3)

The change is confined to `_adapter_routes_without_presenter`. An `ast` comparison of every other top-level node and of every import line gives no difference. The diff is 69 added lines and no removed line.
- **Bookkeeping.** A map from proof key to the presenter-bound parameters seeds `presenter_callable_names_for`.
- **Two private nested helpers:**
  - `name_is_bound_in` detects any binding of a name: assignments, `for`, `with`, `except`, walrus, `del`, `def`, `class`, `import`, `global` and `nonlocal`.
  - `presenter_bound_helper_key` decides the new shape.
- **One added branch** in `value_has_presenter`, tried only after every existing proof of the callee has failed.

The new shape is accepted only when all of these hold:
1. the view calls, by a bare name, a module-level function of its own module that is the only definition of that name;
2. the name is not an import alias and is not rebound anywhere at module level, in the view or in its enclosing functions;
3. the call has no `*args` or `**kwargs`, and the helper has none;
4. at least one helper parameter is presenter-bound. The bound argument is a name the caller already proves to be a presenter callable (for example the factory's `emit_fn=None` → `emit_reader_public_bytes`), or a sanctioned presenter reference. When the argument is omitted, the parameter's default is a sanctioned presenter reference;
5. no bound parameter is rebound anywhere in the helper body.

The helper's returns are then proved by the existing `function_returns_presenter`, under a separate proof key in which only the bound parameters count as presenter callables. Everything else the helper returns must already be proved as today.

What stays reported (addendum 2.2):
- a parameter whose default is not a sanctioned presenter callable;
- a parameter whose bound value is not one, which overrides a sanctioned default;
- a parameter with neither a sanctioned default nor a sanctioned bound value;
- a helper that emits through any other path;
- a helper that rebinds the parameter;
- every case reported today. The file's 298 existing tests pass, with their assertions unchanged by the fixture move, including every bypass fixture.

At `9c767d2` with this change, `_adapter_routes_without_presenter(ADAPTER_BOUNDARY_ADAPTER_LOCI)` returns `[]` (before: `['adapter/http_reader.py:reader_post']`), and `_adapter_presenter_bypass_routes` returns `[]`.

The exact prototype diff, which PR-30 applies or reproduces:

```diff
--- a/tools/evidence/hdapi_v2_boundary_analyzer.py
+++ b/tools/evidence/hdapi_v2_boundary_analyzer.py
@@ -1866,6 +1866,8 @@ def _adapter_routes_without_presenter(loci: tuple[str, ...]) -> list[str]:
             for node in fn.body:
                 yield node
 
+        presenter_bound_params_by_key: dict[str, frozenset[str]] = {}
+
         def presenter_callable_names_for(owner: str) -> set[str]:
             def is_none_constant(value: ast.AST) -> bool:
                 return isinstance(value, ast.Constant) and value.value is None
@@ -1930,6 +1932,7 @@ def _adapter_routes_without_presenter(loci: tuple[str, ...]) -> list[str]:
             names = set(imported_presenter_callable_names)
             for key in reversed(chain):
                 fn = function_defs[key]
+                names.update(presenter_bound_params_by_key.get(key, frozenset()))
                 for node in direct_body_nodes(fn):
                     if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
                         names.remove(node.name)
@@ -2016,6 +2019,69 @@ def _adapter_routes_without_presenter(loci: tuple[str, ...]) -> list[str]:
                 candidates.update(simple_names.get(name, []))
             return candidates
 
+        def name_is_bound_in(node: ast.AST, name: str) -> bool:
+            for child in ast.walk(node):
+                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and child.name == name:
+                    return True
+                if isinstance(child, (ast.Global, ast.Nonlocal)) and name in child.names:
+                    return True
+                if _effect_binds_or_unbinds_name(child, name) or _import_binds_name(child, name):
+                    return True
+            return False
+
+        def presenter_bound_helper_key(call: ast.Call, owner: str, candidate: str) -> str | None:
+            """Prove a call to a module-level helper of this module that receives a
+            sanctioned presenter callable: the argument's bound value in the caller, or,
+            when the argument is omitted, the helper parameter's default.  Returns the
+            key under which the helper is proven with exactly those parameters treated
+            as presenter callables, or ``None`` when the shape does not apply."""
+
+            fn = function_defs.get(candidate)
+            if fn is None or ast_parents.get(fn) is not tree or not isinstance(call.func, ast.Name) or call.func.id in aliases:
+                return None
+            helper_name = call.func.id
+            if any(name_is_bound_in(stmt, helper_name) for stmt in tree.body if stmt is not fn):
+                return None
+            scope: str | None = owner
+            while scope is not None:
+                scope_fn = function_defs[scope]
+                scope_params = scope_fn.args.posonlyargs + scope_fn.args.args + scope_fn.args.kwonlyargs
+                if any(param.arg == helper_name for param in scope_params) or any(name_is_bound_in(stmt, helper_name) for stmt in scope_fn.body):
+                    return None
+                scope = parent_function_by_key.get(scope)
+            if fn.args.vararg is not None or fn.args.kwarg is not None or _has_expanded_kwargs(call) or any(isinstance(arg, ast.Starred) for arg in call.args):
+                return None
+            positional = list(fn.args.posonlyargs) + list(fn.args.args)
+            if len(call.args) > len(positional):
+                return None
+            bound_args: dict[str, ast.AST] = {param.arg: arg for param, arg in zip(positional, call.args)}
+            keyword_params = {param.arg for param in fn.args.args + fn.args.kwonlyargs}
+            for keyword in call.keywords:
+                if keyword.arg not in keyword_params or keyword.arg in bound_args:
+                    return None
+                bound_args[keyword.arg] = keyword.value
+            defaults: dict[str, ast.AST] = dict(zip([param.arg for param in positional][len(positional) - len(fn.args.defaults) :], fn.args.defaults))
+            defaults.update({param.arg: default for param, default in zip(fn.args.kwonlyargs, fn.args.kw_defaults) if default is not None})
+            caller_presenter_names = presenter_callable_names_for(owner)
+            bound: set[str] = set()
+            for param in positional + list(fn.args.kwonlyargs):
+                if param.arg in bound_args:
+                    value = bound_args[param.arg]
+                    if (isinstance(value, ast.Name) and value.id in caller_presenter_names) or (
+                        isinstance(value, (ast.Name, ast.Attribute)) and _is_sanctioned_presenter_call(_attribute_chain(value), aliases)
+                    ):
+                        bound.add(param.arg)
+                elif param.arg in defaults:
+                    default = defaults[param.arg]
+                    if isinstance(default, (ast.Name, ast.Attribute)) and _is_sanctioned_presenter_call(_attribute_chain(default), aliases):
+                        bound.add(param.arg)
+            if not bound or any(name_is_bound_in(stmt, name) for stmt in fn.body for name in bound):
+                return None
+            key = f"{candidate}#presenter_bound:{','.join(sorted(bound))}"
+            function_defs[key] = fn
+            presenter_bound_params_by_key[key] = frozenset(bound)
+            return key
+
         def helper_passthrough_params(name: str) -> set[str]:
             fn = function_defs.get(name)
             if fn is None:
@@ -2171,6 +2237,9 @@ def _adapter_routes_without_presenter(loci: tuple[str, ...]) -> list[str]:
                                 return True
                     if function_returns_presenter(candidate, seen):
                         return True
+                    bound_key = presenter_bound_helper_key(value, owner, candidate)
+                    if bound_key is not None and function_returns_presenter(bound_key, seen):
+                        return True
             return False
 
         def assigned_presenter_vars(fn: ast.FunctionDef | ast.AsyncFunctionDef, owner: str, seen: set[str]) -> set[str]:
```

#### 5.8.3 The two new cases (B-4)

There are exactly two new test functions, so the file collects 298 + 2 = 300 items.
- **Positive case.** It covers the production shape (a presenter bound through the factory's `emit_fn` and passed to the helper) and the sanctioned-default shape, and asserts that `_adapter_routes_without_presenter` returns nothing and the verdict passes.
- **Negative case.** It is one test that checks five shapes. Each must be reported for the route and must make `build_adapter_boundary_proof` raise `ADAPTER_BOUNDARY_CHECK_FAILED:…no_presenter_bypass`. It includes addendum 2.2's named case, "a helper with a non-presenter default" (D-7).
- **Baseline used.** The cases pass typed route records (`discover_route_registrations`) as the baseline, so presenter provenance is the only check in play (D-8).
- **Negative control.** With the unmodified analyzer, the positive case fails and the negative case passes. The positive case therefore tests the change.

Inserted before `test_epic034_adapter_boundary_fails_closed_on_after_request_replacement`:

```python
_PRESENTER_HELPER_MODULE = """
from flask import Blueprint, Flask, Response
from engine.presenter.emitter import emit_public, emit_reader_public_bytes
SAFE_MODE='1'
def _plain(payload):
    return 'plain'
{helper}
def get_bp(emit_fn=None, payload_fn=None):
    if emit_fn is None:
        emit_fn = emit_reader_public_bytes
    bp = Blueprint('helper_bp', __name__)
    @bp.route('/good')
    def good():
        return emit_public({{'ok': True}})
    @bp.route('/reader', methods=['POST'], provide_automatic_options=False)
    def reader_post():
        return {call}
    return bp
bp = get_bp()
def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix='/api')
    return app
"""


def test_epic034_adapter_boundary_accepts_presenter_passed_to_module_helper(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """The production Reader shape: the view passes the factory's presenter-bound
    ``emit_fn`` to a module-level helper, or relies on the helper's sanctioned default."""

    shapes = {
        "bound_value": ("def _respond(emit_fn):\n    body = emit_fn({'ok': True})\n    resp = Response(body, status=200)\n    return resp, 200", "_respond(emit_fn)"),
        "sanctioned_default": ("def _respond(emit_fn=emit_reader_public_bytes):\n    return Response(emit_fn({'ok': True}), status=200)", "_respond()"),
    }
    for name, (helper, call) in shapes.items():
        adapter = _write_boundary_temp(tmp_path, f"presenter_helper_{name}.py", _PRESENTER_HELPER_MODULE.format(helper=helper, call=call))
        assert boundary_analyzer._adapter_routes_without_presenter((adapter,)) == [], name
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer.discover_route_registrations((adapter,))))
        proof, checks = generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
        assert checks["no_presenter_bypass"] is True, name
        assert "[no_presenter_bypass] status=PASS" in proof, name


def test_epic034_adapter_boundary_rejects_module_helper_without_presenter_provenance(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """A helper whose emitter is not a sanctioned presenter callable stays reported:
    a non-presenter default, a non-presenter bound value, a parameter with neither,
    a helper that emits through another path, and a helper that rebinds the parameter."""

    shapes = {
        "non_presenter_default": ("def _respond(emit_fn=_plain):\n    return Response(emit_fn({'ok': False}), status=200)", "_respond()"),
        "non_presenter_bound_value": ("def _respond(emit_fn=emit_reader_public_bytes):\n    return Response(emit_fn({'ok': False}), status=200)", "_respond(_plain)"),
        "no_sanctioned_default_or_value": ("def _respond(emit_fn):\n    return Response(emit_fn({'ok': False}), status=200)", "_respond(payload_fn)"),
        "emits_through_other_path": ("def _respond(emit_fn):\n    return Response(_plain({'ok': False}), status=200)", "_respond(emit_fn)"),
        "rebinds_parameter": ("def _respond(emit_fn):\n    emit_fn = _plain\n    return Response(emit_fn({'ok': False}), status=200)", "_respond(emit_fn)"),
    }
    for name, (helper, call) in shapes.items():
        adapter = _write_boundary_temp(tmp_path, f"presenter_helper_{name}.py", _PRESENTER_HELPER_MODULE.format(helper=helper, call=call))
        assert boundary_analyzer._adapter_routes_without_presenter((adapter,)) == [f"{adapter}:reader_post"], name
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_ADAPTER_LOCI", (adapter,))
        monkeypatch.setattr(generator, "ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE", tuple(boundary_analyzer.discover_route_registrations((adapter,))))
        with pytest.raises(ValueError, match="ADAPTER_BOUNDARY_CHECK_FAILED:.*no_presenter_bypass"):
            generator.build_adapter_boundary_proof("2026-06-18T00:00:00Z", *_epic034_boundary_inputs())
```

#### 5.8.4 Fixture move to `tmp_path` (B-7)

All 103 sites move. Each has the same shape: one `import shutil`, one `rel_dir = "tmp_boundary_test"`, and a `try:` body with a `finally: shutil.rmtree(ROOT / rel_dir, ignore_errors=True)` as the function's last statement. The edit for each site:
- add `tmp_path: Path` to the signature. For the helper `_w003_result_for_row`, add it as a parameter, and pass it from `test_epic034_w003_taxonomy_rows_are_analyzer_owned`, which gains `tmp_path`;
- delete `import shutil` (and the blank line after it), the `rel_dir` assignment, the `try:` line, and the `finally:` and `rmtree` lines;
- dedent the try body by four spaces. Continuation lines of multi-line string literals are never re-indented, so fixture source bytes are unchanged;
- replace `rel_dir` by `tmp_path` in the body;
- change `_write_boundary_temp(directory: Path, name, body)` to write `directory / name` and return `path.as_posix()`, an absolute locus. The analyzer's `ROOT / rel` resolves an absolute locus to itself.

The prototype made the edit with a tokenize-aware script and checked it with `ast`:
- the multiset of string constants is unchanged, except the 103 `"tmp_boundary_test"` literals removed;
- the set of 187 test functions is unchanged (before §5.8.3 adds two).

PR-30 may use a script or hand edits, but must repeat both checks. The diff is large (849 insertions, 1,403 deletions, including §5.8.3) but mechanical. Run alone in the prototype: 300 passed in 106.2 s; exit 0; diff and status clean; no `tmp_boundary_test/`; no tracked file newer than the marker.

#### 5.8.5 `ruby` (B-8)

`ruby` is a visible dependency of this file: the generator's YAML parsing shells out to it (`generate_hdapi_v2_contract_inventory.py:2525–2541`).
- **Without `ruby`** the affected tests fail; they never skip. The file has no skip marker and no fallback for a missing `ruby`. Measured in the prototype: 9 failed (each `FileNotFoundError` for `ruby`), 291 passed, 0 skipped; exit 1; clean tree.
- **In CI.** The file runs as a full-validation target, and as an owner target of the two tools and the three app factories, in the changed-test step of the `test` job (`runs-on: ubuntu-latest`).
- **Where the lane obtains `ruby`.** The job installs no Ruby (`ci.yml` has only `actions/setup-python@v5`), so `ruby` comes from the GitHub-hosted runner image. The Ubuntu 24.04 image `20261004.327.1` lists "Ruby 3.2.3".
- **What is unknown.** Whether the announced move of `ubuntu-latest` to Ubuntu 26.04 keeps Ruby. Owner: PR-35, which observes the hosted run; the documentation delta goes to the Product Owner as OBS-12.
- **What is not done.** No workflow step is added to install Ruby. That would change `ci.yml` beyond S05 (C-4), and it is not needed while the image provides Ruby.
- **Locally.** PR-30 puts `ruby` on `PATH` (§9 step 2; here `/usr/local/bin/ruby` 3.3.6).

#### 5.8.6 Re-run on route changes (B-9)

**Mechanism.** The test is registered as an owner of the three app-factory sources whose routes the baseline encodes:
- `_PRODUCT_TEST_OWNER_PATHS["adapter/factory.py"]` and `["adapter/wsgi.py"]` (existing tuples, appended);
- `_HTTP_READER_TEST_OWNERS` and `_HTTP_READER_INDIRECT_TEST_OWNERS` for `adapter/http_reader.py` (an indirect consumer: it reads the file as a locus and never imports it);
- the pinned `adapter/http_reader.py` tuple in `test_http_reader_owner_guard_is_selected_without_fixed_lane_duplication` (§5.5).

**Result in the prototype.** `changed_test_targets(ROOT, (src,))` includes the test for `adapter/factory.py` (4 targets), `adapter/http_reader.py` (17) and `adapter/wsgi.py` (6). A route change in any of them in WU-PR-03, or later, runs the test, which fails until the baseline is rebuilt.

**Not registered.**
- `adapter/logging_filter.py` has no owner tuple, and a new key is outside addendum 2.2.
- `engine/http/compat_handler.py` routes are classified internal and are not in the public baseline.

Both are analyzer loci. A change to either still runs the test whenever full validation runs. Otherwise it runs that source's own owners (`compat_handler.py`) or fails classification (`logging_filter.py`, `CI_PRODUCT_OWNER_TEST_MISSING`, as today).

The B-6 requirement holds: `changed_test_targets` returns the test for the generator, and the test plus `tests/evidence/test_evidence_tool_ownership.py` for the analyzer.

#### 5.8.7 Governed artifacts and import symbols (B-5)

In the prototype:
- the base-to-head diff over `artifacts/vendor/hdapi_v2/`, `docs/evidence/`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `artifacts/architecture/` and `audit/` is empty;
- the frozen HDE-EPIC033 to HDE-EPIC035 captures are unchanged;
- no import line of either tool changes, so the architecture snapshot's import-symbol keys stay true. `tests/evidence/test_architecture_snapshot.py` gives 5 passed.

A needed new import would be a new finding to the IA, never a regeneration.

## 6. Fix-versus-retire criterion (review v1.0 N2)

The criterion is unchanged from v1.0 §6. A file is **retained (and fixed if needed)** when it exercises code that exists and is reached from a current entrypoint, or a canon-governed current contract, and when it can pass with a test-only change that asserts the current governed behaviour. Addendum 2.2 extends this, for the RP-1 file only, to the two tool corrections of §5.8.

A file is **retired** only for one of these reasons, recorded in the ledger:
- **(a) Removed surface.** It imports or runs a removed tree, script, route, flag or API (ARCHITECTURE.md "Deprecated/archived trees"; the removal commit cited).
- **(b) Not a governed surface.** It asserts a rule canon classes as Speculative, a rule that was never implemented, or behaviour of a legacy stub or dead module, or of a legacy signature, that no current entrypoint reaches. The governed replacement is named where one exists.
- **(c) Frozen record only.** It validates only a frozen administrative or historical record, whose bytes the evidence lane's `update_evidence_index.py --check` already protects, or which is unindexed and frozen (Plan Templates, "CI lane classification and automated budget-control discipline").
- **(d) Vacuous or empty.** It cannot fail, or collects no test.
- **(e) Redundant.** It duplicates a retained test that is named.

Rules:
- A file of current, governed behaviour is never retired except under (e), with the replacing test named.
- A **real product defect** is never hidden by changing an expectation; it is routed (as RS-20 routed the loader defect).
- A file with a live consumer (instruction §9.5) is retained unless the consumer is shown to keep working.

The application to the files instruction §9.2 names is unchanged from v1.0 §6.

Retirements total **66** (the class appears in §7's Disposition column):
- (a) 24;
- (b) 11, including the loader file (B-11);
- (c) 24;
- (d) 4;
- (e) 3.

None retires a test of current, governed behaviour without a named replacement. Security-relevant retirements name their replacing test, or state why the behaviour no longer exists. The loader file's passing rails case is replaced by the two named provider cases. Canon citations of retired files are listed in §17.

## 7. Per-file disposition (135 files)

"Sweep" is the per-file result of §4.2; "writes" includes the hidden writes of §4.2. A retirement's letter is its §6 class. "`pytest.ini` + supplemental" is the §5.1 rule; "owner add" entries are the §5.1 table. Rows 69 and 97 are decided by RS-20 (addendum 2.2); every other row is carried from v1.0 unchanged.

Totals:
- retain as is: 42;
- retain and fix: 27;
- retire: 66;
- route: 0.

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
| 69 | `tests/evidence/test_hdapi_v2_contract_inventory.py` | fail 26/298 | retain + fix | `pytest.ini` + supplemental; new owner keys (B-6): tools/evidence/generate_hdapi_v2_contract_inventory.py (generator), tools/evidence/hdapi_v2_boundary_analyzer.py (helper, with the ownership test); owner add (B-9): adapter/factory.py, adapter/wsgi.py, adapter/http_reader.py (direct and indirect sets) | Of the 26 sweep failures, 5 need only ruby (9 tests depend on it; B-8) and 21 are tool drift since d79cfc1c (HDE-EPIC040 PR06a): the route baseline and the analyzer's presenter provenance are corrected in the two tools under PF10 addendum 2.2 (§5.8). The 103 tmp_boundary_test sites move to tmp_path; one positive and one negative case are added; 300/300 in the integrated prototype with ruby on PATH. |
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
| 97 | `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` | fail 1/2; writes | retire (b) | replaced by: tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode; tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on | Exposes a product defect in the legacy signature of engine/charts/loader.py: _call_legacy calls get_chart on a FixturesProvider that has none (since 6c6f4b2a, 2025-09-28). Only tests call that signature; the loader is not a release member and is not reached at runtime. The defect is not fixed in HDE-CRD-0002: RS-20 review v1.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md; PF10 addendum 2.2) routes it to the Product Owner as decision owner for Task HDE-SEPA006 (HDE Build Checklist — Separation; HDE Architecture §1.1 "Non-BodyGraph chart loader classification"). The file was the only test writer of the tracked artifacts/logs/loader_call.jsonl, which is unchanged. |
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

Counts are from the integrated prototype (§4.3). All paths are inside instruction §6 as addendum 2.2 extends it.

| Path | Change |
| :- | :- |
| `.github/workflows/ci.yml` | `paths-ignore` → ordered `paths` for `pull_request` and `push` (§5.3). No other line changes (36 lines changed) |
| `ci/checks/classify_ci_changes.py` | S04 suffix rule (§5.2); supplemental tuple 40 → 109 (§5.1); owner additions and the two B-6 keys (§5.1); the analyzer leaves `_EVIDENCE_HELPERS_REQUIRING_OWNER`; inactive set emptied, with a comment (§5.4) |
| `pytest.ini` | 68 `testpaths` file entries appended, sorted (§5.1). Markers unchanged |
| `tests/evidence/test_rails_ci_workflow_integration.py` | §5.5 edits, and the new S04, S05, coverage and inactive-refusal tests |
| `tests/evidence/test_hdapi_v2_contract_inventory.py` | §5.8.3 and §5.8.4 |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | baseline data only (§5.8.1) |
| `tools/evidence/hdapi_v2_boundary_analyzer.py` | `_adapter_routes_without_presenter` only (§5.8.2) |
| 26 other retained test files | the other §7 "retain + fix" rows |
| 66 retired test files | deleted (§7 "retire" rows) |
| `tests/retired_tests.md` | new ledger (§5.6) |
| `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md` | the PR-30 result record (§13), written by PR-30 |

Unchanged:
- every release member, so `catalog/manifest.json`, `engine/config/registry_loader.py`, the admission constants and `release_id` stay put (C-5);
- every other `tools/**`, every `scripts/**`, `ci/jobs/*.yml` and `ci/checks/run_rails_job_definitions.py`;
- `engine/charts/loader.py`, `engine/provider/fixtures.py` and every other non-test file outside this table (B-12);
- every governed artifact, including `artifacts/logs/loader_call.jsonl` (B-13), `AGENTS.md`, `README.md` and `docs/pfcanon/`.

## 9. Implementation sequence (PR-30)

PR-30 executes this after Nathan's Proceed for exactly this plan (v1.1).

1. **Recover before creating anything.**
   - Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/` for HDE-CRD-0002 WU-PR-01 work, and resume the most advanced consistent state (PR-30 Execute 1).
   - Fetch `main` and record the base SHA. If `main` has moved past `9c767d2` outside `docs/ephemeral/`, re-run the §4.1 inventory, the §5.8.1 rebuild and the per-file runs of any changed file. Treat any changed fact as an in-flight decision or a rescope finding.
   - Run the ledger absence check (§5.6).
2. **Environment.**
   - Python 3.12 with CI's install. Check pytest readiness with `python -m pip install -r requirements-dev.txt` then `python -m pytest --version` (AGENTS.md).
   - Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `DATABASE_URL`, `HD_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `GEO_API_KEY` and `GH_TOKEN` unset (`env -i` is the proven method).
   - `ruby` on `PATH`, verified with `ruby --version` (B-8).
3. **S04 and S05** (§5.2, §5.3), with their pinned tests and negative controls.
4. **RP-1** (§5.8), in this order:
   1. the analyzer change (§5.8.2);
   2. the two new cases (§5.8.3), with the negative control on the unmodified analyzer;
   3. the fixture move (§5.8.4), with its two `ast` checks;
   4. the baseline rebuild (§5.8.1), with its data-only check and a review of the rebuilt records against the §5.8.1 table. A record that differs from the table is a finding to resolve before continuing;
   5. the file alone with `ruby` on `PATH` (expect 300 passed, clean tree, clean mtime);
   6. the B-5 checks (§5.8.7).
5. **Fixes:** the other 26 "retain + fix" rows, in directory order. After each directory, run its files alone and together in a throwaway copy, with `git status` and the mtime check.
6. **Retirements:** the 66 "retire" rows, including the loader file (RP-2), plus the four inactive entries leaving the classifier (§5.4).
7. **Registrations:** `pytest.ini`, the supplemental tuple, the owner additions, the two B-6 keys and the B-9 registrations (§5.1, §5.8.6).
8. **Pinned-test edits** (§5.5).
9. **Ledger:** `tests/retired_tests.md`, 66 rows with the PR-30 date.
10. **Local validation** (§11), all in a detached worktree of the commit candidate.
11. **One coherent commit** (PR-30 "Mandatory PR-development execution contract"). Push it to the work branch and open the PR with the `.github/pull_request_template.md` headings and the AGENTS.md content rules (instruction §12).
    - The PR body cites RS-20 review v1.0 and PF10 addendum 2.2 for the two tool files and the loader retirement.
    - It never says the loader defect is fixed (B-14).
12. **PR result record** (§13): write it, commit and push it, then return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

Checkpoint and restart rules:
- **Step order.** Steps 3–9 can be reordered, except within step 4. Step 10 runs on the final candidate tree only.
- **Rework after validation.** Any change after step 10 repeats step 10.
- **Base drift.** A base change that touches `ci.yml`, the classifier, `pytest.ini`, any of the 135 files, the two tools or the adapter route files repeats steps 1 and 10. If it touches the adapter route files, it also repeats step 4.4.

## 10. Requirement → change → test map

| Requirement / acceptance | Change | Proof (local, PR-30) | Proof (CI, PR-35) |
| :- | :- | :- | :- |
| S03 (1): zero files outside lane-or-target coverage; the ledger explains every retirement | §5.1 registrations; §5.6 retirements and ledger | new coverage guard test; the §4.1 computation script returns 0; the deleted paths (`git diff --diff-filter=D --name-only base..head`) equal the ledger's path column (prototype: 66 = 66 = 66) | rails lane runs the integration file (full validation) |
| S03 (2): every retained file passes in its lane shape in a detached worktree, with a clean tree | §5.7 and §5.8 fixes; environment isolation; `ruby` on `PATH` | all full-validation targets in one pytest process in a detached worktree; `git diff --exit-code`; empty `git status --short --untracked-files=all`; no tracked file newer than a pre-run marker, apart from OBS-4's 11 paths | changed-test step (full validation) with its clean-tree assertion; final audit |
| S03: recorded failures and collection errors fixed or retired | §7 | per-file runs of the 27 fixed files; collection of the configured suite (`test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`) | as above |
| S04 (3): an unregistered `.sh`/`.sql` under `tools/qa/` fails classification in a unit test | §5.2 | `test_qa_tool_owner_policy_is_exhaustive_and_deduplicated` (new cases); negative control | rails lane |
| S05 (4): a docs-only dry run selects no lane; the filter ignores exactly the classifier's no-lane documentation paths | §5.3 | new path-filter test; negative control; classifier CLI dry run on a docs-only commit in a throwaway clone | rails lane; observed on the PR: a run starts |
| (5): all seven lanes green on the exact head, `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | `ci.yml` and the classifier are full-validation paths | classifier CLI dry run on `base..head`: seven lanes, and changed-test targets equal to `_full_validation_test_targets()` | PR-35: exact-head CI |
| C-1 | resolver owner add | `changed_test_targets(ROOT, ("engine/bodygraph/resolver.py",))` includes `tests/bodygraph/test_resolver_vendor.py` | — |
| C-2 | http_reader owner add | `tests/evidence/test_http_reader_ci_ownership.py` passes; the pinned tuple includes the file | — |
| C-3, C-4 | coverage definition and lane lists unchanged | the coverage guard test uses the §5.1 definition; the `ci.yml` diff touches only the `on:` block | — |
| C-5 | no member change | `python scripts/release_id_recompute.py --check-manifest-only` exits 0; `git diff base..head -- catalog/manifest.json engine/config/registry_loader.py` is empty | release lane |
| C-6 | the S04 rule mirrors `_bodygraph_tool_owner_targets` | §5.2 tests | rails lane |
| B-1, B-2, B-3, B-5 | §5.8.1, §5.8.2, §5.8.7 | the generator `ast` data-only check; the analyzer `ast` confinement and import-line check; the empty governed-path diff; `test_architecture_snapshot.py` | evidence and release lanes (full validation) |
| B-4, B-7 | §5.8.3, §5.8.4 | file alone: 300 passed with `ruby`; the analyzer negative control; the two fixture-move `ast` checks; clean tree and mtime | changed-test step |
| B-6, B-9 | §5.1, §5.8.6 | `changed_test_targets` for the two tools and the three adapter files includes the test; `tests/evidence/test_evidence_tool_ownership.py` and the http_reader guard pass | rails lane |
| B-8 | §5.8.5 | `ruby --version` recorded; the no-`ruby` run fails and does not skip | PR-35 records `ruby` on the hosted runner from the job log |
| B-11 to B-14 | §5.6; §7 row 97 | the ledger row text; `git diff base..head -- engine/charts/loader.py engine/provider/fixtures.py artifacts/logs/loader_call.jsonl` is empty; the two replacement cases pass in the full-validation run | — |

## 11. Validation plan (PR-30, local)

All of the following run in a detached worktree of the commit candidate, under step 2's environment. A failure is a finding to fix, never to skip or quarantine.

1. `ci/checks/check_env_pins.sh` and `python3 ci/checks/check_agents_md_citations.py`: exit 0.
2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py tests/qa/test_qa_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py tests/evidence/test_evidence_tool_ownership.py`: all pass (prototype: 314 passed).
3. **Full-validation shape.**
   - List the targets with `_full_validation_test_targets()` (163 in the prototype) and run them in one `python -m pytest -q -p no:cacheprovider -- <targets>` process, with `ruby` on `PATH`.
   - Afterwards: `git diff --exit-code`; an empty `git status --short --untracked-files=all`; and no tracked file newer than a marker touched before the run, apart from the 11 paths that OBS-4's two covered tests rewrite today.
   - A separate run of the 69 retained files alone must touch nothing.
   - Prototype counts: §4.3.
4. **The RP-1 file alone** (300 passed), and the B-5 checks (§5.8.7).
5. **Fixed lane lists, as `ci.yml` runs them.**
   - Product, compat, db, rails and evidence run in the worktree root, with their pre-steps:
     - `tools/order/generate_ordering_artifacts.py --check`;
     - `ci/checks/check_cli_help.sh`;
     - the two compat guards, writing under a temporary directory;
     - `python ci/checks/check_direct_db_contract.py`;
     - `ci/checks/run_rails_job_definitions.py` with the three job files;
     - the seven evidence read-only checks.
   - The qa and release lane test lists run in their own detached worktrees.
   - The tree is clean after each.
6. **Classifier dry runs:**
   - `base..head`: expect all seven lanes, `changed_tests=true`, and targets equal to the full-validation set;
   - a docs-only commit in a throwaway clone: expect `documentation_only`;
   - `changed_test_targets` for the two tools and the three adapter files (B-6, B-9).
7. **Inventory:** the §4.1 computation script returns 0 uncovered, and the deleted-path set equals the ledger's path column.
8. **Members:** `python scripts/release_id_recompute.py --check-manifest-only` exits 0, and the `catalog/manifest.json` / `engine/config/registry_loader.py` diff is empty.

Not run locally (PR-35, or hosted CI): the release attestation build and verify (`tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean`). PR-30 may run it in an external directory if time allows. Hosted CI runs it in the release lane on full validation.

## 12. PR split, merge dependencies and downstream contracts

- **One PR**, carrying the whole unit, with one coherent commit at initial publication. A split would leave `main` with a coverage guard that fails, or with coverage that does not hold, between PRs. The RP-1 corrections belong with the file they make pass.
- **Upstream merge dependencies:** none. The instruction (#623), plan v1.0 and the request (#624), and the review and addendum (#625) are merged. This plan's own PR must be merged before PR-30 runs, so that PR-30 reads it from `main`.
- **Downstream:**
  - WU-PR-03 and WU-PR-04 (C-1, C-2) and WU-PR-06 (C-3, C-4) build on this unit's merged state.
  - WU-PR-03 changes the adapter routes and must rebuild the generator baseline by §5.8.1. B-9 makes the test run on that change. The IA carries this into the WU-PR-03 instruction (addendum 2.2, "Downstream work").
  - WU-PR-06's sweep environment must provide `ruby` (addendum 2.2).
  - WU-PR-02, WU-PR-06 and WU-PR-07 may be prepared in parallel and merge in Plan order.
- **CI cost:**
  - This PR is a full-validation change (all seven lanes and 163 changed-test targets).
  - The contract-inventory file adds about 100 s to full validation, and to every change of the two tools or the three adapter files.
  - Edits to `ci.yml`, the classifier, `pytest.ini` or `requirements*` run the full-validation set (§4.3).

## 13. Acceptance and evidence obligations (PR result record)

PR-30 writes `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md`. It contains:
- the before/after inventory (135/130 → 0);
- the per-file disposition table, as applied;
- the sweep transcript summary (§4.2 and PR-30's own rerun);
- the lane counts and the full-validation run counts;
- every §11 check actually run, with its result and counts;
- the `ruby` version used;
- the ledger path;
- the RP-1 evidence of §5.8: the data-only check, the confinement check, the negative control, the governed-path diff and the rebuilt-record review;
- the RP-2 statement, which names RS-20 review v1.0 as the route and does not represent the defect as fixed (B-14);
- the in-flight decisions;
- the nonclaims: CI green is not QA; no PF09 mapping; no QA artifact.

QA evidence and `audit/qa/hde-crd-0002/` are out of scope (instruction §7).

## 14. Security and migration constraints

- **Migration:** none. No data, schema, catalog or stored BodyGraph changes, and no member changes. Rollback is Nathan's revert of the squash commit; no manifest refresh is needed.
- **Workflow:** `permissions: contents: read`, the exact-head checkout, closed rails in every lane and the isolation steps are unchanged. The filter never skips CI for a governed primary or a path proof (§5.3).
- **Classifier:** S04 only narrows what passes. Beyond the two B-6 keys, no source owner key is added (§5.1). The analyzer's move out of `_EVIDENCE_HELPERS_REQUIRING_OWNER` turns an edit to it from a refusal into an owner-tested change, as addendum 2.2 decides.
- **Boundary analyzer:** the change widens what the analyzer accepts by one shape, under five conditions (§5.8.2). Every existing bypass fixture still fails, and the negative case pins the shapes that must stay reported. The production Reader still emits only through the presenter; the change is in the tool, not in the route.
- **Fixes:** test-only, apart from §5.8's two tool corrections. They remove tracked writes, the planting of `secrets/provider.json`, untracked writes under the repository root, and session-wide environment mutation (F-8).
- **Retirements:** each security-relevant retirement names a replacing retained test, or the reason the behaviour no longer exists (§6, §7).
- **Secrets:** no secret, token or key value appears in tests, logs, the ledger or the PR record. Runs strip credentials from the environment.

## 15. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| R-1 | Size (Plan R-1): 66 deletions, 27 fixed files and two tool corrections | Bounded by §6's criterion and addendum 2.2; nothing is skipped or quarantined; the integrated prototype passed (§4.3) |
| R-2 | Hidden same-byte rewrites pass `git status` | mtime check (§11) plus the fixes of §5.7 |
| R-3 | The filter model in the S05 test differs from GitHub's matcher | The model is limited to `*` and `**`, and the test asserts no other metacharacter; PR-35 observes the run start |
| R-4 | A future governed primary under a documentation prefix | The S05 test fails at the next rails or full-validation run |
| R-5 | The four fixed hdctl subprocess tests depend on the tree's release being admitted | True on `main`; a unit that leaves the release unadmitted fails them visibly |
| R-6 | Full-validation runtime grows | Measured (§4.3); full validation runs only on full-validation paths |
| R-7 | `ubuntu-latest` moves to Ubuntu 26.04 in November 2026, and Ruby availability there is unverified | B-8: the file fails rather than skips; PR-35 records the hosted `ruby`; OBS-12 goes to the Product Owner |
| R-8 | `main` moves before PR-30 | §9 step 1 re-verification and restart rules |
| R-9 | The analyzer change accepts a bypass it should report | Five conditions (§5.8.2); the negative case covers the shapes addendum 2.2 lists; the 298 existing cases pass with their assertions unchanged. If PR-30 cannot keep these true, it routes a new finding to the IA through the rescope lane (B-4) and never changes a test to pass |
| R-10 | The rebuilt baseline goes stale when routes change | B-9 runs the test on any change to the three app factories; WU-PR-03's instruction carries the rebuild |
| R-11 | The fixture move is a large diff to review | It is mechanical; the two `ast` checks of §5.8.4 prove that it changes no fixture string and leaves the set of test functions unchanged |

Recovery:
- an interruption resumes in the same phase session from its last saved artifact;
- an ordinary defect in this plan returns to this PR-20 context, and a correction is a complete successor version;
- a boundary found in PR-30 before publication goes through RS-20 with `PR_RETURN_PHASE` recorded;
- abort is only Nathan's manual PR-50 instruction.

## 16. RS-20 decision, binding conditions and in-flight planning decisions

**Decision.** RS-20 review v1.0 `APPROVE` (one state) on request v1.0:
- RP-1 is an approved bounded delta with one overlay, PF10 addendum 2.2;
- RP-2 is in scope under the base, with the loader defect routed to the Product Owner.

The IA's routed findings (review §9) and return (review §10) are reflected here and in §17.

**Binding conditions, and where this plan meets them:**

| Condition | Met by |
| :- | :- |
| B-1: exactly the two tool files join the loci | §5.8 B-1; §8 |
| B-2: generator data only; rebuilt from the factories' public records; reviewed against PF05 §5.1.0/§5.4; contains `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed`, and not `reader_v1_post`; no output, flag or `--check` change; no write-mode run | §5.8.1 (with the reading of "at `/api`" and F-9) |
| B-3: analyzer change confined to `_adapter_routes_without_presenter` and private helpers; accepted only for the stated helper shape; everything else stays reported | §5.8.2 |
| B-4: one positive and one negative case; weakening detection would be a new finding | §5.8.3; R-9 |
| B-5: empty governed diff; architecture snapshot green; no new import symbol | §5.8.7 |
| B-6: exactly two owner keys, as stated | §5.1 |
| B-7: 103 sites to `tmp_path`; 298 + 2 pass with `ruby`; clean tree and mtime; the lane shape stated | §5.8.4; §4.3; §11 step 3 (one pytest process over the full-validation targets in the changed-test step's detached worktree) |
| B-8: `ruby` available or the run fails, never skips; its source named | §5.8.5 |
| B-9: the re-run mechanism for route changes in `adapter/factory.py` and `adapter/http_reader.py` | §5.8.6 (registration in existing owner tuples, extended to `adapter/wsgi.py`, D-6) |
| B-10: acceptance (1)–(5), C-1 to C-6 and the PR-30/PR-35 split unchanged | §10; §19 |
| B-11: the loader test retired under (b), with the two named replacements | §7 row 97; §6 |
| B-12: no non-test change for RP-2 | §8 "Unchanged" |
| B-13: `artifacts/logs/loader_call.jsonl` not edited; the retirement removes its only test writer, recorded as a fact | §5.6; §7 row 97 |
| B-14: the ledger row and the PR record cite the review as the route, and never claim the defect is fixed | §5.6; §9 step 11; §13 |

**In-flight planning decisions** (taken here, within approved scope):

| ID | Decision | Why | Tested |
| :- | :- | :- | :- |
| D-1 | No new source owner key beyond B-6 (rejects a prototype's `adapter/env_guard.py` key) | §5.1 rule; S03–S05 do not need the verdict change | integrated prototype pinned suites |
| D-2 | The `test_release_id_precedence_and_grep_guard.py` fix adds no new fallback-value test | The legacy stub's fallback value is not governed behaviour | integrated prototype |
| D-3 | Path proofs under documentation prefixes stay under CI (F-1) | EC-1's definition and reason | S05 test |
| D-4 | `paths` with ordered negations, not `paths-ignore` with `!` | Only the former is documented | S05 test model; hosted observation at PR-35 |
| D-5 | Retain orphan-module tests that pass | They test code that still exists; removing modules is outside §6 | per-file runs |
| D-6 | B-9 registration also covers `adapter/wsgi.py` | It is the third app factory whose public records the baseline encodes; its tuple exists | B-9 dry runs (§5.8.6) |
| D-7 | The negative case checks five shapes inside one test | B-4 and the "298 + 2" count allow two new items; the extra shapes test addendum 2.2's non-weakening list | §5.8.3 |
| D-8 | The new cases use typed route records as their baseline | The legacy-signature baseline used by older cases does not carry routing keywords, which would fail `no_public_reader_change` for the wrong reason | §5.8.3 |
| D-9 | The in-tree adapter helper test (F-10) is not moved | Outside the 103 sites B-7 names; it is clean after the run | §4.3 |
| D-10 | The baseline is regenerated by rule, not patched by hand | B-2 says "rebuilt from the public route records"; a hand patch would keep 7 stale entries | §5.8.1 |

## 17. Observations routed to other owners, and doc-delta candidates

No observation below is fixed in WU-PR-01. Each goes to the named owner, through the IA where the IA owns the unit routing, with its evidence. Nothing here is a finding against this unit's acceptance.

OBS-1 to OBS-11 are carried from v1.0 §17 unchanged:
- **OBS-1:** inert wsgi startup guard;
- **OBS-2:** `provider_loader` environment order;
- **OBS-3:** `test_jsonschema.py` xfails;
- **OBS-4:** same-byte rewrites by two covered tests;
- **OBS-5:** dead adapter modules;
- **OBS-6:** `_compute_env_mode` semantics;
- **OBS-7:** always-skipped showcompat tests;
- **OBS-8:** orphaned fixtures;
- **OBS-9:** `invocation_tag.py`;
- **OBS-10:** owner-key candidates;
- **OBS-11:** documents naming retired files.

Updated and new observations:

| ID | Observation | Evidence | Owner / route |
| :- | :- | :- | :- |
| OBS-12 (updated) | `tools/evidence/generate_hdapi_v2_contract_inventory.py` depends on `ruby`, which is declared nowhere. CI obtains it from the runner image (§5.8.5) | line 2530; `ci.yml` has no Ruby setup; runner image readme | Product Owner (documentation delta candidate, as addendum 2.2 records); PR-35 for the hosted observation |
| OBS-13 (new) | The analyzer ties blueprint routes to mounts through the registered variable name (F-9), so production Reader route records show `/reader` and not `/api/reader` | `_blueprint_registration_prefixes`; discovered records at `9c767d2` | IA (outside B-3's confinement; WU-PR-03 instruction context) |
| OBS-14 (new) | `test_epic034_presenter_bypass_detects_imported_adapter_helper` writes two modules under `adapter/` during the test (F-10) | test lines 2392–2423 at `9c767d2` | IA (a later test-hygiene item) |
| OBS-15 (new; RS-20) | The legacy chart-loader defect (F-6) | review §9 | Product Owner, as decision owner for HDE-SEPA006. Nothing in HDE-CRD-0002 waits on it |

**Doc-delta candidates (Product Owner drainage; no canon edit).** Carried from v1.0 §17:
- PF09.2 Dissolution line 677;
- PF05 §4.1.6 line 837 and PF09.4 Conjunction line 2139;
- PF09.1 Calcination lines 1146, 1166 and 2053;
- PF14 line 7653;
- the PF20 references to the retired HDE-EPIC035–037 evidence tests.

Added: the undeclared `ruby` dependency (OBS-12).

## 18. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried unchanged from the Specification, Plan, instruction and addendum 2.2 ("Conflicts: NONE"):
- **CR-1** (CANON_RECONCILIATION; the PF30 record and "CRD Plan" wording versus HDE Governance §9.1.1): `APPROVED_AS_CHANGED`. Affects no requirement of this unit.
- **CR-2** (CANON_RECONCILIATION; planned units in a Specification): `APPROVED_AS_CHANGED`. Affects no requirement of this unit.
- **CR-3** (CANON_RECONCILIATION; "stable CRD ID recorded in PF30"): `APPROVED_AS_CHANGED`. Not touched.

**No new conflict.** For v1.1, PF10 v13.5.3 was searched in full; addendum 2.2 governs this unit's RP-1 and RP-2 scope. PF05 §5.1.0 and §5.4 were read for the baseline and agree with the rebuilt records (§5.8.1). v1.0's searches stand, because canon is otherwise unchanged since `a8c99d1`.

## 19. PR-30 and PR-35 ownership

- **PR-30** (after Nathan's Proceed for this v1.1, in this same dedicated PR session):
  - recovers before creating any vehicle;
  - implements only v1.1's scope (the approved base plus addendum 2.2), with tests run locally under §11;
  - forms one coherent commit;
  - publishes the initial candidate and records `PR_IMPLEMENTATION_RESULT`;
  - returns `PR_CANDIDATE_PUBLISHED` with a handoff to PR-35 in PR-35's own dedicated session.

  PR-30 owns neither review correction nor CI readiness. A boundary found in PR-30 goes through RS-20 with `PR_RETURN_PHASE` recorded (PR-30 before or after publication), never into the PR unapproved.
- **PR-35** (its own dedicated session):
  - retrieves and resolves review findings (Codex code review and security review), retests locally and pushes coherent corrections;
  - uses CI economically: known findings first, no `[skip ci]` without Nathan's direct authorization;
  - verifies current-head CI (all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability, and observes that the workflow started on the PR (§5.3);
  - records the hosted runner's `ruby` (B-8);
  - returns `MERGE_PENDING — Ready to merge` without merging.

  No CI waiver exists for HDE-CRD-0002.
- **Merge:** Nathan merges, manually. Afterwards, PR-40 lineage review by the IA.

## 20. Session identity and recovery envelope

```yaml
paused_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (planning complete; held for Proceed)
phase: PR-20 pre-Proceed planning; no PR_RETURN_PHASE (no Proceed, workspace vehicle or PR exists for code)
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner); authoring and last known session https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
base_identity: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0; PF10 v13.5.3; overlay PF10 addendum 2.2 (RS-20 review v1.0, APPROVE)
checkpoint_identity: this artifact (v1.1, AWAITING_PO_PROCEED); predecessor v1.0 (PENDING) preserved
completed_work: inventory, per-file sweep, 135 dispositions (all decided), S04/S05 design, RP-1 design, integrated prototype v1.1 (scratch only, never pushed)
pending_decision: Nathan's PR Implementation Proceed for exactly this plan (v1.1)
resume: on Proceed, PR-30 in this same dedicated session (§9)
scratch_state: TRANSIENT_SCRATCH only (prototype clones and diffs in the session scratchpad); this plan is self-sufficient without them
```

## 21. TypeSafe reading for the receiving session (PR-30, this dedicated session)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation is given beside it.

Action sent (v6): "Implement, as the dedicated PR session after the Product Owner's Proceed, the first unit of an approved CRD Implementation Plan from a detailed plan that is written, prototyped end to end, and whose two boundary changes a rescope review approved, with a complete task list: bring 135 test files that no CI lane runs into CI or retire them (69 kept, 27 of them fixed in test code only; 66 deleted with a ledger), replace the CI workflow's path filter, tighten one classifier rule and register owner tests in the classifier, and make two approved bounded corrections to governed evidence tools (rebuild the route-baseline data of a 4,800-line generator and add helper-provenance resolution to a 3,200-line analyzer), then run the full local validation (about 3,300 tests in one detached-worktree run) and publish one pull request of about 100 files. No live provider call occurs; an independent review-and-CI phase and the Product Owner's manual merge follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.62 (confidence 0.70); rung probabilities low 0.00, medium 0.03, high 0.36, extra high 0.58, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.09, Opus 5.5 0.91 (confidence 0.82). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.33, Opus 5.5 at extra high 0.53, Opus 5.5 at max 0.03, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.03, Fable 5.1 at extra high 0.05, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-12T23:57:26Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T23:57:26Z; HTTP 200 in 0.71 s; 4331 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).

- **One send**, taken before this artifact was saved. The Notion row was not written (this session writes nothing to Notion); the printed row object is kept with this session's records only.
- **Nathan's pick for PR-30:** not stated.

**Surface notes (facts, not a model recommendation):**
- PR-30 runs in this same dedicated session, on `amthorn78/glow-hdengine-v2`, branch `claude/elegant-mayer-y6ppap` unless Nathan names another.
- It needs Python 3.12, CI's install and `ruby` on `PATH`. It needs no live vendor, production or database access, and the closed rails strip every credential.
- The full-validation run took 430 s for the 163 targets in one pytest process (§4.3); the other §11 steps add a few minutes.
- Prerequisite: the pull request carrying this plan is merged to `main` first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-20 / WU-PR-01 / plan 2 (v1.1) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by review v1.1) |
| instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md`, v1.0 |
| overlay | PF10 addendum 2.2 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md`; record `docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md`), approved by RS-20 review v1.0 |
| work unit / requirements | WU-PR-01; S03, S04, S05 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (retrieved 2026-10-12 and re-fetched 2026-10-13; page state as of 2026-10-12T02:29:47Z, unchanged) |
| role/stage | dedicated WU-PR-01 PR engineering session / PR-20 (resumed after RS-20) |
| capture time | 2026-10-13T00:12:19Z |
| execution identity | https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8 |
| inherited prompt uses | IA-10 (Audit v1.0), IA-40 (Plan v1.1), IA-30 (review v1.1 §7), PR-10 (instruction v1.0 §20), PR-20 (plan v1.0 §22), RS-20 (review v1.0 §14) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `9c767d2`. Recorded here only; owner of any later installation: GCFPE-MGMT-10 and the Product Owner |

## Canon relied on

Read on `main` at `9c767d2`. `docs/pfcanon/` differs from v1.0's `a8c99d1` only by PF10 v13.5.2 → v13.5.3.

**Read by this session for v1.1:**
- **PF10-HDE-Build-Notes v13.5.3:** read in full.
  - Addendum 2.2 governs §5.1 (the two keys), §5.6 (the loader row), §5.8 (B-1 to B-9), §6, §7 rows 69 and 97, §8 to §16 where they implement it, and §19.
  - Addendum 2.1 governs §21.
  - The precedence rules ("PF10 authority", "Scope within an individual PF10 document", "Silence rule") decide that 2.2 applies only to this unit's RP-1 and RP-2 scope, and that permanent canon governs the rest of S03–S05.
- **PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3:** §5.1.0 "Production POST request and resolution (normative)" and §5.4 "Dev harness routing and guard (dev-only)", in full (§5.8.1 review).

**Relied on through the RS-20 decision** (the review's "Canon relied on", not re-read in full here):
- PF04-Canon-HDE-Governance v2.8.7 §9.1.1 and §9.7.7;
- PF06-Canon-Change-Process-Guide v2.5.4 §0.1A;
- PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use";
- PF02-Canon-HDE-Architecture v2.4.6 §1.1 and the emitter rule;
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.6.3.10;
- PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.7 HDE-SEPA006;
- PF09.5-Canon-HDE-Build-Checklist-Fermentation v1.6.1, HDE-FERM006.2.

**Carried from v1.0** (read then on `a8c99d1`; unchanged on `9c767d2`):
- PF04 v2.8.7: §9.1.1 role table and approval map; §9.7.7 "Plan approval gate"; the review-boundary bullets; §9.7 path validation, "Planning audit posture", file minting with absence proof, and "No fabricated required paths";
- PF27 v2.0.5: "CI lane classification and automated budget-control discipline", "Repository loci and file minting" and "Artifact execution boundary";
- PF06 v2.5.4: §1.0.6 and §3.5.1;
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability (normative)";
- the canon lines citing the 135 files (v1.0 "Canon relied on");
- the sections read by v1.0's planning workers for the per-file reasons (v1.0 "Canon relied on", second list).

**Operative documentation:** `AGENTS.md` (canon-first; closed rails; pytest readiness; QA output placement; CI-exempt paths; PR description rules; no hand-edited governed artifacts; evidence attribution).

**In-flight documents:**
- RS-20 review v1.0, addendum v1.0, checkpoint and handoff: in full;
- request v1.0 and plan v1.0 (own);
- instruction v1.0, Plan v1.1, review v1.1, Specification v1.1 and Audit v1.0: as recorded in v1.0.

**Prompts:** PR-20 (100926.1). This session's copy was retrieved on 2026-10-12 for v1.0 and re-read for its overlay, Execute and output rules. It was re-fetched on 2026-10-13; the page state is as of 2026-10-12T02:29:47Z, unchanged. PR-30's receiver contract is as carried in PR-20's "Next step".

## Checks run by this session

v1.0's checks stand (v1.0 "Checks run by this session"). Added for v1.1:

| Check | Result |
| :- | :- |
| `git diff --stat a8c99d1 9c767d2 -- . ':!docs/ephemeral' ':!docs/pfcanon'` | empty |
| PF10 2.2 against addendum v1.0 (normalized) | identical (12,228 characters) |
| Analyzer at `9c767d2` before the change | `_adapter_routes_without_presenter` → `['adapter/http_reader.py:reader_post']`; route drift: 6 discovered-only records, 1 baseline-only (`reader_v1_post`) |
| Baseline rule at `cf9198df` | yields 16 records, each equal to one of the 16 baseline entries the comparison used |
| RP-1 prototype: the file alone, `ruby` on `PATH` | 300 passed in 106.2 s; exit 0; diff and status clean; no `tmp_boundary_test/`; no tracked file newer than the marker |
| RP-1 negative control (unmodified analyzer) | positive case fails; negative case passes |
| Generator `ast` data-only check | identical outside the baseline value; 23 → 21 records; no `reader_v1_post` |
| Analyzer `ast` confinement and import lines | only `_adapter_routes_without_presenter` differs; import lines identical |
| Fixture move `ast` checks | string constants unchanged except 103 `tmp_boundary_test`; 187 test functions unchanged |
| B-5 governed diff; `test_architecture_snapshot.py` | empty; 5 passed |
| Integrated prototype v1.1: coverage | 0 uncovered; 212 / 49 / 163 / 204 |
| Integrated prototype v1.1: pinned suites | 314 passed |
| Classifier dry run `9c767d2..180a376` | exit 0; seven lanes; 100 paths; 163 targets = full-validation set |
| Docs-only classifier dry run | `documentation_only`; no lane; `changed_tests=false` |
| B-6/B-9 `changed_test_targets` | generator → the test; analyzer → the test + ownership test; `factory.py` 4, `http_reader.py` 17, `wsgi.py` 6 targets, each including the test |
| Table / ledger / deleted paths | 66 = 66 = 66, the same set |
| Integrated prototype v1.1: 163 full-validation targets in a detached worktree | 3,262 passed in 430.0 s; exit 0; diff and status clean; mtime: only the 11 OBS-4 same-byte rewrites |
| The 69 retained files alone | 489 passed in 140.8 s; exit 0; diff and status clean; no tracked file newer than the marker |
| The contract-inventory file without `ruby` | 9 failed (each `FileNotFoundError` for `ruby`), 291 passed, 0 skipped; exit 1; clean tree |
| TypeSafe reading (§21) | HTTP 200; Opus 5.5 at extra high |

Not executed by this session:
- the fixed-lane pre-steps and lane lists on the prototype;
- the release attestation build;
- hosted CI;
- Codex code review and security review.

Those belong to PR-30 and PR-35.

---

**State:** `AWAITING_PO_PROCEED`, held at `ASK OK? — PR IMPLEMENTATION PLAN`. This is the WU-PR-01 detailed PR implementation plan v1.1, complete and executable within the approved base plus PF10 addendum 2.2. Nathan's `PR Implementation Proceed` for exactly this plan path and version authorizes PR-30. Nothing else does.
