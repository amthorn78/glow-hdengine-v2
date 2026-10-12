---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-01-RESCOPE-1
proposed_pf10_number: "2.2 (next continuous number after addendum 2.1 of the current controlled PF10; allocation and publication are the Product Owner's)"
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (RS-20; selected version 100926.1, release GCFPE-20261009.1; https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c)
approval_decision: HDE-CRD-0002-WU-PR-01-RESCOPE-REVIEW v1.0, decision APPROVE, docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md
immutable_base: HDE-CRD-0002-SPECIFICATION v1.1 (SPECIFICATION_APPROVED, Thoth CF-C-30; docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md) → HDE-CRD-0002 Implementation Plan v1.1 (approved by IA-30 review v1.1, Isis; docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md and docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md) → HDE-CRD-0002 WU-PR-01 PR instruction v1.0 (IA, PR-10; docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md)
applicable_prior_addenda: NONE
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (v13.5.2; blob ec71eeecec8b0fcff1645d317211258bc708712c; read in full at creation; provenance, not a gate)
originating_request: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md (RESCOPE_REQUEST v1.0, items RP-1 and RP-2, from the dedicated WU-PR-01 PR engineering session at PR-20 pre-Proceed planning)
return_phase: PR-20 planning context of the dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (pre-Proceed; no Proceed, vehicle or pull request for code exists; PR_RETURN_PHASE not applicable)
capture_time_utc: 2026-10-12T23:07:18Z
normalized_approved_delta_digest: not computed (no governed normalization procedure exists; none is invented)
---

## 2.2 HDE-CRD-0002 WU-PR-01: two HDAPI v2 contract-inventory evidence tools join the CI-coverage work unit for bounded corrections; the legacy chart-loader test is retired with its defect routed to the Product Owner

Timestamp: 101226 23:07 (UTC) Details: Records the whole-change Implementation Agent's approval, through Review Bounded Work-Unit Rescope, of one bounded implementation rescope of work unit WU-PR-01 (CI coverage of every test file; requirements S03, S04, S05) of the approved HDE-CRD-0002 Implementation Plan v1.1. Origin: the WU-PR-01 rescope request v1.0 (items RP-1 and RP-2) from the dedicated PR engineering session during pre-Proceed planning. Evidence: the review's own reproduction of both findings at `main` `6c664dd9` and at `cf9198df`, and its reading of the tools, the adapter, the classifier and the loader.

### Decision and approval status

The continuing whole-change Implementation Agent for HDE-CRD-0002 decided `APPROVE` on the WU-PR-01 rescope request v1.0, as one state for the one request. The decision record is `docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md`. The approval is a bounded implementation rescope within the approved Specification's intent; it is not a change to the Epic-level commitment, to any acceptance criterion, protected boundary, other work unit, accepted dependency or Product Owner matter. The immutable base is not rewritten. This addendum is the one overlay the approval creates; the effective baseline for WU-PR-01 is the approved base plus this addendum.

### Base

HDE-CRD-0002 Specification v1.1, requirement S03 ("Bring every test file into a CI lane or retire it with a recorded reason"; criterion "No test file runs in no CI lane; each retirement has a recorded reason; recorded failures and collection errors are fixed or retired with their files"; constraint "S03 may expose real defects that enlarge the work"). Implementation Plan v1.1, work unit WU-PR-01 (deliverables, acceptance (1) to (5), risk R-1). WU-PR-01 PR instruction v1.0 §6 (bounded files: fixes stay inside test code and test-local fixtures), §7 (no change to any `tools/**` or `scripts/**` file), §9.2 (fix-versus-retire criterion), §9.8 (a real product defect is not fixed by changing a test's expectation; a needed non-test change is routed) and §14 (rescope behavior). None of these is changed.

### Approved delta (RP-1)

WU-PR-01's bounded files are extended by exactly two items, and the instruction's `tools/**` exclusion is relaxed for exactly the changes stated here:

1. `tools/evidence/generate_hdapi_v2_contract_inventory.py`: only the data of `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` changes. It is rebuilt from the public route records the three app factories register at the PR head and reviewed against HDE CLI/API/Vendor Reference §5.1.0 and §5.4 before commit. It must contain `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed` at `/api` and must not contain the removed `reader_v1_post`. The generator's outputs, schema, evidence family, refusal codes, flags and write paths do not change; it gains no `--check` mode or other feature; it is not run in write mode against the repository.
2. `tools/evidence/hdapi_v2_boundary_analyzer.py`: the change is confined to presenter-provenance resolution in `_adapter_routes_without_presenter` and any private helper it needs inside the analyzer. Provenance through a helper is accepted only when the view calls a module-level helper of its own module with an argument whose bound value, or whose parameter default, is a sanctioned presenter callable (the production Reader's `get_reader_api_bp` → `_production_reader_response(emit_fn)` shape, whose default is `emit_reader_public_bytes`). Bypass detection is not weakened: a parameter whose default is not a sanctioned presenter callable, a helper that emits through any other path, a parameter with neither a sanctioned default nor a sanctioned bound value, and every case reported today stay reported.

With them, inside files WU-PR-01 already owns:

- `ci/checks/classify_ci_changes.py`: `_EVIDENCE_GENERATOR_TEST_OWNERS["tools/evidence/generate_hdapi_v2_contract_inventory.py"] = ("tests/evidence/test_hdapi_v2_contract_inventory.py",)`; `tools/evidence/hdapi_v2_boundary_analyzer.py` leaves `_EVIDENCE_HELPERS_REQUIRING_OWNER` and enters `_EVIDENCE_HELPER_TEST_OWNERS` with owners `tests/evidence/test_hdapi_v2_contract_inventory.py` and `_EVIDENCE_HELPER_OWNERSHIP_TEST`. These two source keys are the only exception to the detailed plan's rule that no new source key is created.
- `tests/evidence/test_hdapi_v2_contract_inventory.py`: the 103 `tmp_boundary_test` fixture sites move to `tmp_path`; one positive analyzer case (the shape above is accepted) and one negative case (a helper with a non-presenter default is reported and fails the analyzer verdict) are added; the file is registered under the detailed plan's registration rule.
- `tests/evidence/test_rails_ci_workflow_integration.py`: every pin over the owner registries stays true.

### Binding requirements

- The file passes 298 of 298 plus the two new cases with `ruby` on `PATH`, in the detached-worktree full-validation run, with a clean tree and a clean mtime check. No test is skipped, deselected, `xfail`-marked or quarantined.
- `changed_test_targets` returns the test for each tool (plus the ownership test for the analyzer).
- The lane that runs the file has `ruby` available or the run fails; it never skips. The detailed plan records `ruby` as a visible dependency and names where the lane obtains it.
- No governed artifact changes: the diff from base to head over `artifacts/vendor/hdapi_v2/`, `docs/evidence/`, `artifacts/evidence_index.jsonl` and its checksum, and `artifacts/architecture/` is empty; the frozen HDE-EPIC033 to HDE-EPIC035 captures are unchanged; the architecture snapshot test stays green. Neither tool gains a new import symbol, because the architecture snapshot records both by import-symbol keys; a needed new import is a new finding to the Implementation Agent, never a regeneration.
- If the analyzer change cannot be made without weakening bypass detection, that is a new finding to the Implementation Agent through the rescope lane; it is not resolved by changing a test.
- The detailed plan states the mechanism by which a route change in `adapter/factory.py` or `adapter/http_reader.py` re-runs this test, so that the baseline stays current when WU-PR-03 changes those routes.
- WU-PR-01's acceptance (1) to (5), its interface contracts C-1 to C-6, its evidence obligations, its nonclaims and its PR-30/PR-35 split are unchanged.

### RP-2: in scope under the base; no delta

`tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` is retired under the base's own authority (S03; instruction §9.2; the detailed plan's retirement class for a legacy signature no current entrypoint reaches). Its ledger row records the reason: the file exposes a product defect in the legacy signature of `engine/charts/loader.py` (`_call_legacy` calls `get_chart` on a `FixturesProvider` that has none, since `6c6f4b2a`, 2025-09-28); only tests call it; the loader is not a release member and is not reached at runtime; the defect is routed to the Product Owner as the decision owner for Task HDE-SEPA006 (HDE Build Checklist — Separation; HDE Architecture §1.1 "Non-BodyGraph chart loader classification"); it is not fixed in HDE-CRD-0002. Replacing coverage for its passing case: `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`, both retained and passing at the PR head. `engine/charts/loader.py`, `engine/provider/fixtures.py` and every other non-test file stay unchanged; the tracked `artifacts/logs/loader_call.jsonl` is not edited, truncated or regenerated. Neither the ledger nor the PR result record represents the defect as fixed, deferred to a unit of HDE-CRD-0002, or resolved.

### Scope, exclusions and nonclaims

- No other `tools/**` or `scripts/**` file changes; `ci/jobs/*.yml` and `ci/checks/run_rails_job_definitions.py` are unchanged.
- No release member changes; `catalog/manifest.json`, `engine/config/registry_loader.py` and the admission constants are unchanged; no manifest refresh.
- No public route, public payload, public flag, transport or runtime behavior changes; the production Reader continues to emit only through the presenter.
- No live vendor, production or database call; closed rails throughout.
- No QA artifact, QA verdict, acceptance, PF09 or PF30 status movement, deployment, canon edit, Product Owner Proceed, merge authority or epic/CRD closure follows from this addendum.
- Retiring the contract-inventory test together with both tools as historical was not decided; it remains a separate product decision the Product Owner may raise.
- A repair of `engine/charts/loader.py` was not approved.

### Affected surfaces

- **Requirements.** S03 acceptance (1) and (2) become reachable; S04, S05 and acceptance (3) to (5) are unaffected; S03 remains classified as not production-affecting.
- **Dependencies.** None upstream. The coverage definition contracted to WU-PR-06 is unchanged; WU-PR-06's sweep environment must provide `ruby` for this file.
- **Tests.** Two cases added; one file retired. The detailed plan's dispositions become 42 retained, 27 retained-and-fixed and 66 retired, restated by plan v1.1 from its own table.
- **Ops.** None.
- **Documentation.** The undeclared `ruby` dependency of the generator (the detailed plan's observation OBS-12) is a documentation delta candidate for the Product Owner.
- **Downstream work.** WU-PR-03 later changes the adapter routes and must keep the generator's baseline current; the Implementation Agent carries that into the WU-PR-03 PR instruction. The WU-PR-06 instruction carries the `ruby` requirement of the sweep environment.

### Evidence

- At `main` `6c664dd9`, with Python 3.12, CI's install, closed rails and `ruby` on `PATH`: `tests/evidence/test_hdapi_v2_contract_inventory.py` gives 21 failed and 277 passed, every failure raising `ADAPTER_BOUNDARY_CHECK_FAILED:presenter_emitter_inspected,no_presenter_bypass,no_public_reader_change`; at `cf9198df`, the parent of HDE-EPIC040 PR06a (`d79cfc1c`), it gives 298 passed. The tree was clean after both runs.
- The production Reader view `reader_post` returns `_production_reader_response(emit_fn)`, whose default is the sanctioned emitter `emit_reader_public_bytes`; the analyzer does not follow the parameter-passed emitter; the generator's baseline predates the production Reader and still names `reader_v1_post`.
- At `6c664dd9`, `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` gives 1 failed (`AttributeError` at `engine/charts/loader.py:81`) and 1 passed, and the run appends to the tracked `artifacts/logs/loader_call.jsonl`.
- The detailed plan v1.0's integrated prototype leaves exactly these two files uncovered; the two findings are the whole remaining gap to acceptance (1).

### Conflicts

NONE. The `CANON_CONFLICT_REGISTER` entries CR-1 to CR-3 of HDE-CRD-0002 are carried unchanged (`APPROVED_AS_CHANGED`); no new entry.

### Unresolved obligations and owners

- The analyzer change design: not prototyped at approval; owner, the dedicated WU-PR-01 PR engineering session (plan v1.1, then PR-30), with the failure route above.
- `ruby` on hosted runners after the announced move of `ubuntu-latest` to Ubuntu 26.04: unknown; owner, PR-35 observation of hosted CI, with the documentation delta candidate to the Product Owner.
- The legacy chart-loader defect: returned to the Product Owner as the decision owner for HDE-SEPA006; nothing in HDE-CRD-0002 waits on it.
- PF10 numbering and publication: the Product Owner.

### Status and consequences

Completed: the review decision and this overlay. Not yet done: plan v1.1, the Product Owner's Proceed, implementation, reviews and merge of WU-PR-01; the WU-PR-03 and WU-PR-06 instructions that carry the downstream obligations. Unproven: that the analyzer change can be made without weakening bypass detection, pending the prototype. Consequence: when WU-PR-01 lands under this overlay, every tracked test file runs in a CI lane or is retired with a recorded reason, the two HDAPI v2 contract-inventory tools regain a registered owner test that runs on their change, and the loader defect remains recorded and owned rather than hidden.
