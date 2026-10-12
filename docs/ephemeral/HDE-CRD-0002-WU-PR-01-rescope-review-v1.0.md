---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-01-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: APPROVE
approval_sentinel: "ASK OK."
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
items_decided: RP-1 (approved bounded implementation delta; one PF10 addendum overlay), RP-2 (in scope under the immutable base; no overlay; the loader defect is routed to the Product Owner)
request_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-request-v1.0.md (v1.0, RESCOPE_REQUEST, RESCOPE_REQUEST_PENDING_REVIEW; blob 1a8d95b55aaa811ad687831955696cf268c78d8c; SHA-256 6e298614cc91649173058cdd400bea1dd283f06d5eec03aeb8d3237b2490b94b; 29,091 bytes; read in full)
request_author: the dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20 pre-Proceed planning), session https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, this session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah (IA-10 lineage: Audit v1.0, Plan v1.0); the PR instruction v1.0 was issued at PR-10 in session https://claude.ai/code/session_01WiUd7gGCtJvGgBixQNUjg1
author_reviewer_independence: VERIFIED (distinct sessions and roles; this IA did not author the request)
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; retrieved revision last edited 2026-10-12T02:29:57.795Z); release GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
originating_stage: PR-20 pre-Proceed planning. No Proceed, workspace vehicle or code pull request exists. PR_RETURN_PHASE: not applicable
vehicle_state_relied_on: no open pull request on amthorn78/glow-hdengine-v2 at review time (GitHub pull-request listing, state open, zero results); origin/main 6c664dd9 (#624 merged, carrying the request and plan v1.0); docs/pfcanon/ unchanged since df23bbf; working tree clean
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, PENDING; blob 1279c0f6047ead0a00fb938b75c3fd5e1f9c1a74; preserved; its successor is plan v1.1)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0; blob 24597a31fbb910a4d36106a1aa2d5b861faec976; unchanged by this decision)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE by Isis; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; lineage)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0. None is rewritten by this decision
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (blob ec71eeecec8b0fcff1645d317211258bc708712c; SHA-256 c53dac75b7a6e7b7ed303c5b032e6d9a05a7285b89819104abd793bb1767222d; read in full; holds addendum 2.1 only; silent on both items; next continuous addendum number 2.2)
applicable_prior_addenda: NONE
addendum_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md (the one PF10_BUILD_NOTES_ADDENDUM this APPROVE creates; proposed number 2.2)
checkpoint_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0-checkpoint.md
handoff_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0-handoff.md
capture_time_utc: 2026-10-12T23:07:18Z
return_to: the PR-20 planning context of the dedicated WU-PR-01 PR engineering session (the request's author), which writes plan v1.1 as a complete successor under approved base + this overlay and presents it at AWAITING_PO_PROCEED
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry (§11)
---

# HDE-CRD-0002 WU-PR-01 — Rescope Review v1.0

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Decision and authority

**decision: APPROVE — one state for the one request.** RP-1 is approved as a bounded implementation delta, with the binding conditions in §6.1, and is represented by exactly one PF10 addendum overlay (§8). RP-2 needs no overlay: retiring the file with a recorded reason is authorized by the immutable base once the defect it exposes is routed, and this decision routes that defect to the Product Owner (§9). Nothing else changes.

**Authority.** RS-20 — Review Bounded Work-Unit Rescope — 100926.1: the continuing whole-change IA reviews the originating PR author's request independently and returns the decision to that author's phase. This authority is limited to the native `RESCOPE_REVIEW` classification within approved Specification intent. It decides no Product Owner product intent, approves no replacement whole-change Plan, authorizes no implementation or merge, edits no PF10, restarts no accepted work and invokes no PR-50. Isis has no role in this lane.

**Author and reviewer independence — verified.** The request's front matter and its merged pull request (#624) record its author as the dedicated WU-PR-01 PR engineering session at PR-20 (session `session_011q4bUbzJCYk2KAF7eAceF8`). This IA's lineage is IA-10 in this session (Audit v1.0, Plan v1.0) and PR-10 in session `session_01WiUd7gGCtJvGgBixQNUjg1` (instruction v1.0). This IA did not author the request or the suspended plan v1.0 and reviewed both from their merged copies on `main`.

**Reading of "material".** RS-20 defines **Material** as a change to the Epic-level commitment (outcome or objective, approved acceptance criteria, a protected architecture, security, data-model or external-contract boundary, several units' scope, an accepted dependency, or budget, schedule or risk needing Product Owner direction) and says a planned approach found incomplete, impractical or inferior is not by itself material. `APPROVE` requires "a material bounded implementation delta within approved Specification intent". These are two different thresholds. This review reads the second as a substantive, evidenced change to the unit's bounded loci that the immutable base does not authorize, and the first as the line beyond which the matter leaves this IA's authority (`SPECIFICATION_CHANGE_REQUIRED` or the Product Owner). RP-1 is the former and not the latter (§3.3). The earlier RS-20 decision on `main`, `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md` §2, applied the same reading; it is cited as precedent, not as authority.

**Bases, unchanged:** Specification v1.1 (approved); Implementation Plan v1.1 and its review v1.1 (approved); PR instruction v1.0. The suspended plan v1.0 is preserved as the predecessor of plan v1.1.

**PF10 read:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md` in full (front matter §§1–9, the template, index §1.1, addendum 2.1). It is silent on HDAPI v2 contract-inventory tooling, on the legacy chart loader and on WU-PR-01. The next continuous addendum number is 2.2. No prior addendum applies.

## 2. Vehicle state and request completeness — verified

**Stage and vehicle.** Pre-Proceed planning. No Product Owner Proceed, no workspace vehicle and no code pull request exist for WU-PR-01; the GitHub pull-request listing for `amthorn78/glow-hdengine-v2` with state `open` returned zero results at review time. `PR_RETURN_PHASE` is therefore not applicable, and RS-40 does not apply. `origin/main` is `6c664dd9` (#624). `docs/pfcanon/` is unchanged since `df23bbf`. The working tree used for this review was clean.

**Baseline difference.** The request measured at `a8c99d11`; this review re-verified at `6c664dd9`. The only difference is #624 itself (files under `docs/ephemeral/`). Every code, classifier, workflow and history fact below was re-read at `6c664dd9`.

**Completeness against RS-20's required inputs.** Exactly one `RESCOPE_REQUEST` from PR-20, by repository path and artifact type, carrying: the exact findings (§3, §4); the approved Specification, immutable base Plan and review, and PF10 with active addenda (front matter, §2); explicit proposed deltas (§3.3, §4.3); originating stage, owner and session (front matter, §2); author and reviewer lineage (front matter, §1); completed valid work (§2); affected requirements, dependencies, tests, Ops, documentation and downstream work (§3.3 "Effects", §4.3 "Effects", §5); evidence (§3.1, §4.1); risks and unresolved facts (§6); exclusions (§3.3); conflicts (§6, canon register line); no prior decision or application report (none exists). The request is complete. Three details differ from this review's own measurements and none affects the decision: the request dates the baseline's last change to `dbc7e650` (2026-06-23), which is the generator file's last commit, while a line-range history of the constant itself ends at `c9c7122b` (2026-06-22); the request's run times (98 s and 100 s) differ from this review's (74 s and 69 s); and the request's "26 fail in the sweep environment" is the 21 tool-drift failures plus the 5 that need `ruby` on `PATH`, which this review confirms by running with `ruby` available.

## 3. RP-1 — HDAPI v2 contract-inventory tools left stale by HDE-EPIC040 PR06a

### 3.1 Reproduction by this reviewer

Throwaway clone with full history, Python 3.12 virtual environment with CI's install, closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), `ruby 3.3.6` on `PATH`:

| Commit | `tests/evidence/test_hdapi_v2_contract_inventory.py` | Time | Tree after |
| :- | :- | :- | :- |
| `6c664dd9` (`main`) | 21 failed, 277 passed | 74 s | clean |
| `cf9198df` (parent of `d79cfc1c`, HDE-EPIC040 PR06a #508) | 298 passed | 69 s | clean |

Every one of the 21 failures raises `ValueError: ADAPTER_BOUNDARY_CHECK_FAILED:presenter_emitter_inspected,no_presenter_bypass,no_public_reader_change` from the generator; one of them (`test_epic034_pr05_refusal_builder_exercises_each_v2_route`) then also fails a downstream assertion that depends on that result. The request's Group B count, commit attribution and refusal code are confirmed.

### 3.2 Code facts verified at `6c664dd9`

- `adapter/http_reader.py`: `_production_reader_response(emit_fn)` is a module-level helper (line 509); `get_reader_api_bp(emit_fn=None)` (line 544) defaults the parameter to `emit_reader_public_bytes` (line 553), imported from `engine.runtime`; the view `reader_post` (line 557) returns `_production_reader_response(emit_fn)`; `reader_method_not_allowed` (line 561) and `reader_post_not_allowed` (line 721) are the other production Reader views.
- `tools/evidence/hdapi_v2_boundary_analyzer.py` (3,157 lines): `_adapter_routes_without_presenter` (line 1791 onward) walks the view's AST for sanctioned presenter calls and resolves presenter callables for the owner module; it does not follow a parameter-passed emitter into a helper the view calls. Extending that resolution to a parameter whose default or bound value is a sanctioned presenter callable is a bounded change inside this function's existing model; no design was prototyped by the request or by this review.
- `tools/evidence/generate_hdapi_v2_contract_inventory.py` (4,789 lines): `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` starts at line 135 and still names `reader_v1_post` (lines 1105–1201); it holds no `reader_post`, `reader_method_not_allowed` or `reader_post_not_allowed`; the fail-closed raises are at lines 4139 and 4357; `main` (line 4769) has no `--check` mode; `parse_yaml_openapi` shells out to `ruby` at line 2530. `ruby` is declared in no requirements file or workflow; `.github/workflows/ci.yml` names no `hdapi_v2` step.
- Ownership: the analyzer is in `_EVIDENCE_HELPERS_REQUIRING_OWNER` (`ci/checks/classify_ci_changes.py` line 653); the generator has no `_EVIDENCE_GENERATOR_TEST_OWNERS` entry (line 532); `_EVIDENCE_HELPER_OWNERSHIP_TEST` (line 569) and `_EVIDENCE_HELPER_TEST_OWNERS` (line 572) exist as the request names them; `tests/evidence/test_rails_ci_workflow_integration.py::test_non_generator_evidence_helpers_have_exact_fail_closed_owners` (line 1003) iterates the requiring-owner set.
- Consumers: outside tests, the two tools are named only by the classifier and by `artifacts/architecture/architecture_snapshot.keys_only.json`, which records each by its import-symbol keys, not by content. The governed HDAPI v2 evidence family is frozen: one `docs/evidence/INDEX.json` row and 35 Machine Mirror rows under `artifacts/vendor/hdapi_v2/`.
- The test file (4,876 lines) has 103 `tmp_boundary_test` call sites that write fixtures under the repository root.
- The production Reader still emits only through the presenter: the view calls the helper, the helper calls the sanctioned emitter. This is a tooling defect, not a product defect (HDE Architecture, "Emitter rule (normative)" and the `adapter/` single-HTTP-home paragraph).

### 3.3 Boundary and classification

- **Boundary is real.** Instruction v1.0 §6 bounds fixes to "test code and test-local fixtures" and says "Any other file the work needs is a finding: route it under §14 before changing it"; §7 says "No change to any `tools/**` or `scripts/**` file". Plan v1.1 §7 WU-PR-01 "Deliverables" names no `tools/` path. The base does not authorize the delta.
- **No lawful test-only disposition exists.** A baseline rebuilt inside the test is tautological; pinned adapter copies stop the test proving the current repository; a stubbed boundary proof hides that a governed generator cannot run at `HEAD`; each changes the test's expectation to reach green, which instruction §9.8 and Plan R-1 forbid. Retirement fails the fix-versus-retire criterion (review v1.0 N2 carried by review v1.1 §4; instruction §9.2): the file is the only test of two tools that implement current obligations (HDE Architecture single HTTP home and presenter-only emission; HDE Schemas and Artifacts §8.6.3.10), and no retained test replaces it.
- **Classification: a bounded implementation delta that is not Material.** It changes no Specification outcome, acceptance criterion, protected architecture, security, data-model or external-contract boundary, other unit's scope, accepted dependency, budget, schedule or risk needing Product Owner direction. It touches no release member (`tools/evidence/` holds none; C-5 holds), no public route, no runtime behavior and no governed artifact. The Specification anticipates it: S03's criterion is "recorded failures and collection errors are fixed or retired with their files" and its constraint says "S03 may expose real defects that enlarge the work"; its classification of S03 as "Not production-affecting" (CI lanes and classifier, evidence tests and labels, read-only repository tooling) is preserved. Plan R-1 names "a real defect" enlarging WU-PR-01 as the rescope trigger.

### 3.4 Alternatives

| Alternative | Disposition |
| :- | :- |
| A1. Add the two tool files for the two bounded corrections and register the test as their owner | **Approved**, with §6.1. Smallest change that satisfies acceptance (1) and (2) without hiding a defect |
| A2. Carve the file out of acceptance (1) and route the repair to another unit | Rejected. Changes an approved acceptance criterion and adds a unit, which is Material; S03's intent would not hold when WU-PR-01 merges |
| A3. Retire the test and both tools as historical | Rejected. The tools serve current canon obligations; retiring them is a product decision outside this IA's authority, and nothing here forecloses the Product Owner raising it separately |
| A4. Retire the test only | Rejected. Fails N2 and leaves both tools untested |
| A5. Test-only change | Rejected. Forbidden by instruction §9.8 and Plan R-1 |

## 4. RP-2 — legacy chart-loader defect

### 4.1 Reproduction by this reviewer

Same clone and environment, `6c664dd9`: `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` gives 1 failed, 1 passed. The failure is `AttributeError` at `engine/charts/loader.py:81` in `test_loader_uses_fixtures_by_default_in_safe_mode`. After the run the clone's tracked `artifacts/logs/loader_call.jsonl` was modified, confirming the tracked write.

### 4.2 Code and history verified

- `engine/charts/loader.py` `_call_legacy` (lines 76–82) calls `provider.get_chart(user_id, correlation_id=correlation_id)` on whatever `resolve_provider()` returns; `engine/provider/fixtures.py` `FixturesProvider` defines only `__init__` and `get_pair_profile`. The loader's `_log_call` appends to `artifacts/logs/loader_call.jsonl`, which is tracked and has been committed with test-run appends (`39a5a33a` 2025-09-29, `f3e1f9a1` 2026-04-27, `c6fdc913` 2026-05-01).
- History: `48870125` (2025-09-27) added the provider calls; `6c6f4b2a` (2025-09-28, "CORE-CHART-LOADER-READY-001: close") removed the fallback that made the legacy signature work. The defect is a year old.
- Reach: the only non-test importer of `load_chart` is `scripts/make_compat_determinism_artifacts.py` (line 25), through the current signature; `engine/charts/loader.py` is not a `catalog/manifest.json` member; `adapter/http_reader.py` uses its own chart loading and does not reach `_call_legacy`.
- The passing case, `test_loader_vendor_path_is_gated_in_safe_mode`, is covered by retained tests `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` (line 9) and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` (line 5), both present at `6c664dd9`.

### 4.3 Canon

HDE Architecture §1.1 "Non-BodyGraph chart loader classification [Required-Now]" classifies `engine/charts/loader.py` as implementation drift that "remains current repository reality until separately remediated". HDE Build Checklist — Separation records that remediation as Task HDE-SEPA006 with subtasks .1 to .3, all **Not done**, owned by "Task HDE-SEPA006's IA and dedicated PR implementation lane", and states that HDE-SEPA006 is separate planned Separation work outside HDE-EPIC040. Neither HDE-SEPA006 nor the loader is in HDE-CRD-0002's Specification.

### 4.4 Classification: in scope under the base; the defect has no lawful PR author here

- S03 authorizes retirement with a recorded reason; instruction §9.2 permits retiring a file of current behavior when the plan records why its coverage is redundant and which retained test replaces it (plan v1.0 §6 class (b); replacements named in §4.2); instruction §9.8 makes the disposition wait only on the route of the defect. The route is the one thing the base reserved to §14, and this decision supplies it. No overlay is needed, so no addendum content is created for RP-2 beyond recording this.
- The loader defect is a non-PR finding of HDE-CRD-0002: no Plan unit owns the loader, and a fix would decide the behavior of a path canon assigns to HDE-SEPA006 for correction and removal. RS-20 directs that, without a lawful PR author, the finding and its actual owner are preserved and the unresolved assignment returns to the Product Owner. This review does that in §9; it invents no PR, Proceed or phase.

### 4.5 Alternatives

| Alternative | Disposition |
| :- | :- |
| B1. Retire the file; ledger row records the defect and the route; defect evidence to the Product Owner as owner of HDE-SEPA006 scheduling | **In scope under the base**, with §6.2 |
| B2. Add `engine/charts/loader.py` for a minimal `_call_legacy` repair | Rejected. An architecture decision on a path canon assigns elsewhere; outside the Specification; would be `SPECIFICATION_CHANGE_REQUIRED` if pursued |
| B3. Keep the file uncovered or failing | Rejected. Violates acceptance (1) or (2) |
| B4. Delete only the failing function | Rejected. Hides the defect inside a retained file whose remaining case duplicates retained coverage |

## 5. Evidence against each excluded decision

| Excluded decision | RP-1 | RP-2 | Request as a whole |
| :- | :- | :- | :- |
| `REJECT` | The boundary is real (§3.3), reproduced (§3.1), necessary (A2–A5 each violate an acceptance item, N2 or §9.8), safe (no member, governed artifact, public route or runtime change) and within this IA's authority (not Material) | Retirement is lawful and necessary (B3, B4 fail); the route is the only open item | Not rejected |
| `REVISION_REQUIRED` | Evidence, alternatives, bounds, verification and effects are stated with precision sufficient for an executable plan v1.1. The unprototyped analyzer change is a design detail inside one bounded locus with named acceptance tests and a stated failure route (§6.1 B-4). The three measurement differences in §2 are immaterial | Defect, reach, canon owner and replacing coverage are stated and verified | Not required |
| `SPECIFICATION_CHANGE_REQUIRED` | Within S03's criterion and its "real defects that enlarge the work" constraint; S03 stays "Not production-affecting"; no Exclusion, outcome or acceptance criterion changes | An S03 disposition; nothing in the Specification changes; B2, which would need one, is rejected | Not required |
| `IN_SCOPE_REPAIR` | The base does not authorize `tools/**` changes (instruction §6, §7; Plan deliverables). "The retained test files, fixed where they fail" is about test files and does not reach the tools | The base does authorize the retirement; only the route was reserved. This is recorded inside the single `APPROVE` state, not as a second state | Not the whole request's state: RP-1 needs an overlay |

## 6. Binding conditions

These bind PR-20 plan v1.1, PR-30 and PR-35 for WU-PR-01. Instruction v1.0 stays as issued; the overlay extends §6 by exactly the two files in B-1 and relaxes §7's `tools/**` exclusion for exactly the changes in B-2 and B-3. Everything else in the instruction holds.

### 6.1 RP-1

- **B-1 Loci.** Exactly `tools/evidence/generate_hdapi_v2_contract_inventory.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py` join the bounded files, each limited as below. No other `tools/**` or `scripts/**` file changes.
- **B-2 Generator.** Only the `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` data changes, rebuilt from the public route records the three app factories register at the PR head and reviewed against HDE CLI/API/Vendor Reference §5.1.0 and §5.4 before commit. It must contain `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed` at `/api` and must not contain `reader_v1_post`. No change to the generator's outputs, schema, evidence family, refusal codes, flags or write paths; no `--check` mode or other new feature; it is not run in write mode against the repository.
- **B-3 Analyzer.** The change is confined to presenter-provenance resolution in `_adapter_routes_without_presenter` and any private helper it needs inside the analyzer. Provenance through a helper is accepted only when the view calls a module-level helper of its own module with an argument whose bound value, or whose parameter default, is a sanctioned presenter callable. Everything else stays reported: a parameter whose default is not a sanctioned presenter callable, a helper that emits through any other path, a parameter with neither a sanctioned default nor a sanctioned bound value, and every case the analyzer reports today.
- **B-4 Bypass proof and failure route.** The test file gains one positive case (the `get_reader_api_bp` → `_production_reader_response(emit_fn)` shape is accepted) and one negative case (a helper with a non-presenter default is reported and fails the analyzer verdict). If plan v1.1 or PR-30 finds the change cannot be made without weakening bypass detection, that is a new finding to this IA through the rescope lane; it is not resolved by changing a test (instruction §9.8).
- **B-5 No governed artifact.** `git diff <base>..<head> --` over `artifacts/vendor/hdapi_v2/`, `docs/evidence/`, `artifacts/evidence_index.jsonl` and its `.sha256`, and `artifacts/architecture/` is empty; the frozen HDE-EPIC033 to HDE-EPIC035 captures stay unchanged; `tests/evidence/test_architecture_snapshot.py` stays green. Consequence: neither tool gains a new import symbol, because the architecture snapshot records both by import-symbol keys. A needed new import is a finding to this IA, never a regeneration.
- **B-6 Classifier.** Exactly the two owner keys the request proposes: `_EVIDENCE_GENERATOR_TEST_OWNERS["tools/evidence/generate_hdapi_v2_contract_inventory.py"] = ("tests/evidence/test_hdapi_v2_contract_inventory.py",)`; the analyzer leaves `_EVIDENCE_HELPERS_REQUIRING_OWNER` and enters `_EVIDENCE_HELPER_TEST_OWNERS` with owners `tests/evidence/test_hdapi_v2_contract_inventory.py` and `_EVIDENCE_HELPER_OWNERSHIP_TEST`. `changed_test_targets(ROOT, (<tool>,))` returns the test for each tool (plus the ownership test for the analyzer). The plan's no-new-source-key rule holds everywhere else, and every pin in `tests/evidence/test_rails_ci_workflow_integration.py` stays true.
- **B-7 Test file.** The 103 `tmp_boundary_test` fixture sites move to `tmp_path`. The file passes 298 of 298 plus the two new cases with `ruby` on `PATH` in the detached-worktree full-validation run with a clean tree and a clean mtime check. No test is skipped, deselected, `xfail`-marked or quarantined. Plan v1.1 states the file's lane shape.
- **B-8 Ruby.** The lane that runs the file has `ruby` available or the run fails; it never skips. Plan v1.1 records `ruby` as a visible dependency of this test and names where the lane obtains it. OBS-12 goes to the Product Owner as a documentation delta candidate (§9).
- **B-9 Baseline currency at WU-PR-03.** Plan v1.1 states the mechanism by which a route change in `adapter/factory.py` or `adapter/http_reader.py` re-runs this test (registration of the test in an existing owner tuple for those paths, or the lane the file joins). Independently, this IA carries the obligation to keep the baseline current into the WU-PR-03 PR instruction at PR-10 (§9).
- **B-10 Unchanged obligations.** Acceptance (1) to (5), contracts C-1 to C-6, nonclaims, evidence obligations and the PR-30/PR-35 split are unchanged. The request's §3.3 verification items bind PR-30, and the PR result record names each check actually run with its counts.

### 6.2 RP-2

- **B-11 Retirement under the base.** `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` is deleted under plan class (b). Its `tests/retired_tests.md` row carries the reason the request states in §4.3 and names the replacing coverage: `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on`, both retained and passing at the PR head (the first is retained-and-fixed; its fix stays in test code).
- **B-12 No non-test change.** `engine/charts/loader.py`, `engine/provider/fixtures.py` and every other non-test file stay unchanged for RP-2. B2 is not approved.
- **B-13 The tracked log.** `artifacts/logs/loader_call.jsonl` is not edited, truncated or regenerated by WU-PR-01. The retirement removes the only test writer; plan v1.1 records that as a fact, not as a cleanup.
- **B-14 Honest record.** The ledger row and the PR result record cite this review as the route of the defect. Neither represents the defect as fixed, as deferred to a unit of HDE-CRD-0002, or as resolved.

## 7. Effects and preserved work

- **Requirements.** S03 acceptance (1) and (2) become reachable; S04, S05 and acceptance (3) to (5) are unaffected; S03 remains "Not production-affecting".
- **Dependencies.** None upstream. C-3's coverage definition is unchanged. WU-PR-06's sweep runner must provide `ruby` for this file; this IA carries that into the WU-PR-06 instruction (§9).
- **Tests.** Two cases added; one file retired. Plan v1.0's totals (42 retain, 26 retain-and-fix, 65 retire; supplemental tuple 40 → 109; `pytest.ini` +68) become 42, 27 and 66 as the request states; plan v1.1 restates them from its own table.
- **Ops.** None. **Documentation.** OBS-12 to the Product Owner. **Downstream.** WU-PR-03 baseline currency (B-9).
- **Release.** No member change; no manifest refresh; C-5 holds. **CI.** The two tools are evidence-lane paths and WU-PR-01 already runs full validation; lane runtime adds the two new cases only.
- **Preserved work.** Plan v1.0's inventory re-verification, per-file sweep, 133 dispositions, S04 and S05 designs with pinned tests and negative controls, integrated prototype and check results stand; plan v1.1 is a complete successor that carries them and changes only what this decision requires.

## 8. PF10 overlay

One addendum, `docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md`, proposed as PF10 addendum 2.2 (the next continuous number after 2.1 in v13.5.2), with `applicable_prior_addenda: NONE`. Its `approved_delta` is RP-1 (§6.1); it records RP-2 as in scope under the base with the defect routed. Lineage: Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0 → this review → the addendum. PF10 is not edited; numbering and publication are the Product Owner's. The effective baseline for WU-PR-01 from this decision onward is `approved base + this addendum`.

## 9. Findings returned to the Product Owner, and obligations this IA carries

- **To the Product Owner — legacy chart-loader defect (RP-2).** `engine/charts/loader.py` `_call_legacy` calls `get_chart` on a `FixturesProvider` that has none, since `6c6f4b2a` (2025-09-28). Only tests reach it; it is not a release member; no HDE-CRD-0002 unit owns it. Canon owner: Task HDE-SEPA006 (HDE Build Checklist — Separation), per HDE Architecture §1.1. This review preserves the finding and returns the assignment: whether and when HDE-SEPA006 takes it is the Product Owner's decision. Nothing in HDE-CRD-0002 waits on it.
- **To the Product Owner — OBS-12, the `ruby` dependency.** The contract-inventory generator shells out to `ruby`, which no requirements file or workflow declares; the request records that the hosted Ubuntu 24.04 runner image provides Ruby 3.2.3 and that HDE Build Checklist — Fermentation HDE-FERM006.2 recorded installing Ruby to reach PASS. Documentation delta candidate for Glow Infrastructure or the environment template; not decided here.
- **IA-carried.** At PR-10 for WU-PR-03: keep `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` current with the IF-11 route changes and run `tests/evidence/test_hdapi_v2_contract_inventory.py`. At PR-10 for WU-PR-06: the sweep environment provides `ruby`.

## 10. Return

The decision returns to the PR-20 planning context of the dedicated WU-PR-01 PR engineering session, the request's author. That session writes plan v1.1 as the complete successor of the suspended plan v1.0 under `approved base + this addendum`, carrying the addendum's repository path as the one applicable active addendum, `AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`, the `CANON_CONFLICT_REGISTER`, and §6's conditions mapped into its per-file table, implementation sequence and verification, and presents it at `AWAITING_PO_PROCEED` when complete and executable. This decision creates no Proceed, vehicle, branch or pull request for code and grants no implementation or merge authority. The pull request carrying this review and the addendum is merged to `main` by the Product Owner before PR-20 resumes.

## 11. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried from the approved Specification, Plan and instruction, unchanged; no new entry:

- **CR-1** (CANON_RECONCILIATION; HDE CRD Records and "CRD Plan" wording versus HDE Governance §9.1.1) — `APPROVED_AS_CHANGED` (Thoth, Specification review v1.0 §6; confirmed review v1.1 §4). Interim: no HDE CRD Records entry. Not affected by this decision.
- **CR-2** (CANON_RECONCILIATION; planned units in a Specification) — `APPROVED_AS_CHANGED`. Interim: the Plan, not the Specification, carries units. Not affected.
- **CR-3** (CANON_RECONCILIATION; "stable CRD ID recorded in HDE CRD Records") — `APPROVED_AS_CHANGED`. Interim: `HDE-CRD-0002` is the Product Owner-assigned ID; QA root `audit/qa/hde-crd-0002/`. Not affected.

The canon searched for this decision ("Canon relied on") is consistent with the request and the bases. Drainage stays with the Product Owner. Full field sets and decision history are in Specification v1.1 §CR and Plan v1.1 §15.

## 12. Working-state note and recovery

- **Attempt:** 1 of this RS-20 invocation; no prior RS-20 result for this request.
- **State:** review, addendum, checkpoint and handoff written under `docs/ephemeral/` on the working branch of this session, committed, pushed and read back; one pull request opened for the Product Owner to merge. No Notion write; no repository write outside `docs/ephemeral/`.
- **Reproducibility:** §3.1 and §4.1 runs use a throwaway clone with full history, CI's Python 3.12 install, closed rails and `ruby` on `PATH`; `python -m pytest tests/evidence/test_hdapi_v2_contract_inventory.py -q` at `6c664dd9` and at `cf9198df`; `python -m pytest tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py -q` at `6c664dd9`. Never run these in a working tree that must stay clean.
- **Interruption:** if the carrying pull request is not merged, the Product Owner merges it; nothing is re-run. If re-entry is needed, the four artifacts on `main` are the complete state.

## 13. TypeSafe reading and surface advice for the receiving session (PR-20, WU-PR-01 plan v1.1)

Action sent (v6): "Revise, as the dedicated PR engineering session that authored it, an existing 104 KB detailed PR implementation plan, not yet reviewed, for the first unit of an approved CRD Implementation Plan (CI coverage of 135 uncovered test files, about 3,000 tests under full validation) into a complete successor that applies one approved bounded rescope: two governed evidence tools (a 4,800-line generator and a 3,200-line analyzer) join the unit for bounded corrections, including a not-yet-prototyped change to the analyzer's AST walk with one positive and one negative test, two classifier owner registrations, and one test-file retirement whose product defect is routed to the Product Owner; a per-file disposition table and the review's binding conditions exist as the task list, and each of the 135 files must be checked. No code is merged and no live provider call occurs; a Product Owner Proceed, implementation, and independent code, security and lineage reviews follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.52 (confidence 0.61); rung probabilities low 0.00, medium 0.03, high 0.52, extra high 0.37, max 0.06, ultracode 0.02. Model probabilities Fable 5.1 0.10, Opus 5.5 0.90 (confidence 0.80). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.47, Opus 5.5 at extra high 0.33, Opus 5.5 at max 0.05, Opus 5.5 at ultracode 0.02, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.01, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and high. Sent 2026-10-12T22:58:25Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T22:58:25Z; HTTP 200 in 0.6 s; 4318 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between extra high and high.
- No Notion row was written. **Nathan's pick for PR-20 (plan v1.1):** not stated. **Nathan's pick for this RS-20 session:** not stated (the request's §7 reading for RS-20 stands as recorded there).

**Surface advice:**
- Resume PR-20 in the dedicated WU-PR-01 PR engineering session's planning context, as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with Notion read access. It writes plan v1.1 as a complete successor file; it does not edit plan v1.0.
- **What to prototype before presenting `AWAITING_PO_PROCEED`:** the B-3 analyzer change and the B-4 positive and negative cases, in a throwaway clone with `ruby` on `PATH`, so that plan v1.1 carries a verified design rather than the request's unprototyped one; then the 298 + 2 run with a clean tree.
- **What it needs:** no live vendor, production or database access; closed rails throughout; the carrying pull request merged first.

## 14. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / RS-20 / WU-PR-01 / rescope review 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 |
| work unit | WU-PR-01; S03 (acceptance (1), (2)); items RP-1, RP-2 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; retrieved revision last edited 2026-10-12T02:29:57.795Z. Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (retrieved revision last edited 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA / RS-20 review of a PR-20 pre-Proceed request |
| capture time | 2026-10-12T23:07:18Z |
| execution identity | https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah |
| earlier entries | Audit v1.0 and Plan v1.0 (IA-10, this session); instruction v1.0 (PR-10); plan v1.0 and request v1.0 (PR-20); each holds its own entry |
| repository persistence | PENDING / NON_GATING (no `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `6c664dd9`; `docs/changes/` holds `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md` only); recorded here only; authorized owner: a repository writer under an installed procedure, when one exists |

## Canon relied on

Read on `main` at `6c664dd9` (`docs/pfcanon/` unchanged since `df23bbf`). Decision topics are mapped to the sections read.

- **Rescope authority, decision matrix, materiality, addendum contract, routing (§1, §5, §8, §10):** RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (Notion, read in full; the governing procedure); PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion, read in full as the receiver contract); PF04-Canon-HDE-Governance v2.8.7 §9.1.1 "Change authority and exact-artifact lineage" (the dedicated PR session authors the detailed plan; the IA issues instructions; the Specification and Plan are the two authorities) and §9.7.7 "Plan approval gate" (`ASK OK? — PR IMPLEMENTATION PLAN` hold; no scope laundering; no plan-local token); PF06-Canon-Change-Process-Guide v2.5.4 §0.1A "Governing lanes, common lifecycle, and authority routing" (CRD lane; Build Notes recording; authority routing by title); PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" (precedence rule; addendum form: next continuous H2, H3-or-deeper children, page-ready, no role-addressed instructions; Build Notes cited by title only in PF prose).
- **PF10 and addendum numbering (§1, §8):** PF10-HDE-Build-Notes v13.5.2, read in full: front matter §§1–9 (authority, scope, continuous sequence, supersession, current-version, live-content, silence and operational rules), the template, §1.1 index and addendum 2.1. Silent on both items; the next number is 2.2; the file's own rule that PF references inside it are titles-only governs the addendum body.
- **RP-1 subject matter (§3):** PF02-Canon-HDE-Architecture v2.4.6, the `adapter/` single-HTTP-home paragraphs (including the mounted-handler posture) and "Emitter rule (normative)"; PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.1.0 "Production POST request and resolution (normative)" and §5.4 "Dev harness routing and guard (dev-only)" (the route set the rebuilt baseline is reviewed against); PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.6.3.10 "HDAPI v2 vendor contract and adapter-conformance evidence" (the governed family the tools produce; frozen captures); PF09.5-Canon-HDE-Build-Checklist-Fermentation v1.6.1, the HDE-FERM006.2 PO-003 line recording that Ruby was installed before the check passed.
- **RP-2 subject matter (§4, §9):** PF02-Canon-HDE-Architecture v2.4.6 §1.1 "Non-BodyGraph chart loader classification [Required-Now]"; PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.7, Task HDE-SEPA006 and subtasks HDE-SEPA006.1 to .3 (Not done; owner lane), and the HDE-EPIC040 scope statement that HDE-SEPA006 is separate planned work.
- **In-flight documents (all sections cited above):** Specification v1.1 approved (S03 row; "Uncovered tests" constraint; the classification table; Exclusions; CR-1 to CR-3); Implementation Plan v1.1 (§7 WU-PR-01 in full; R-1; §15 register); Plan review v1.1 (N2 carry, §4); PR instruction v1.0 (§§5–7, §9, §10, §14, §16, §18); PR implementation plan v1.0 (§4.4, §5.1, §6, §16, §17, §20 and its checks table); rescope request v1.0 (in full); `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md` and its addendum (precedent form only).
- **Silence and searches:** `grep -n -i -E 'rescope' docs/pfcanon/*.md` finds, beyond Plan Templates above, only HDE Governance §9.4-area QA-10 integration coverage (rescope among the contracts QA-10 review must cover), Change Process Guide's statement that HDE Phased Epics is never the rescope owner, a historical "Completed bounded rescope" record in HDE Build Checklist — Distillation, and historical HDE Phased Epics entries. None governs the RS-20 decision procedure, which lives in the GCFPE prompts. `grep -n -i -E 'hdapi_v2_boundary_analyzer|generate_hdapi_v2_contract_inventory|charts/loader' docs/pfcanon/PF10-*.md` finds nothing. The PF09.5, PF09.6 and PF14 lines that cite the contract-inventory test, which the request calls historical, were not re-read here and are not relied on.
- **Not canon, recorded as data:** the GitHub runner-images README (Ruby 3.2.3) as cited by the request; this review did not fetch it.

---

**Status:** `RESCOPE_REVIEW` v1.0, decision `APPROVE`, one request, two items (RP-1 approved delta with addendum 2.2; RP-2 in scope under the base, defect routed to the Product Owner). Returns to the PR-20 planning context of the dedicated WU-PR-01 PR engineering session.

ASK OK.
