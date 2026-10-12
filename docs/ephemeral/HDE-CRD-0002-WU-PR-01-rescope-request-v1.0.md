---
artifact_type: RESCOPE_REQUEST
artifact_id: HDE-CRD-0002-WU-PR-01-RESCOPE-REQUEST
artifact_version: "1.0"
status: RESCOPE_REQUEST_PENDING_REVIEW
approval_sentinel: "ASK OK?"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
items: RP-1 (tool drift behind tests/evidence/test_hdapi_v2_contract_inventory.py), RP-2 (legacy loader defect behind tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py)
originating_stage: PR-20 — Create Detailed PR Implementation Plan — 100926.1, pre-Proceed planning (no PR_RETURN_PHASE: no Proceed, workspace vehicle or pull request for code exists)
author: originating PR implementation author, the dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20); authoring session https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002 through RS-20 (the IA issued instruction v1.0 under PR-10 and did not author this request)
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, PENDING)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0; blob 24597a31fbb910a4d36106a1aa2d5b861faec976)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, approved)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; lineage)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (v13.5.2; blob ec71eeecec8b0fcff1645d317211258bc708712c; read in full; addendum 2.1 only)
pf10_addendum_paths: none
prior_rescope_proposal_or_review: none
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_baseline: origin/main a8c99d11dccc0bdd844352515bd629efa8af5233
created_at: 2026-10-12T22:36:44Z
return_point: this PR-20 planning context for WU-PR-01, which writes plan v1.1 (complete successor) and presents it at AWAITING_PO_PROCEED
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry
---

# HDE-CRD-0002 WU-PR-01 — Rescope request v1.0

## 1. Request

The WU-PR-01 PR-20 author asks the whole-change IA for one RS-20 decision on two items. Each blocks the disposition of one test file, and so blocks WU-PR-01 acceptance (1): "The Audit §3(b) computation at the PR head returns zero files outside lane-or-target coverage."

| Item | File | Boundary | Requested decision |
| :- | :- | :- | :- |
| RP-1 | `tests/evidence/test_hdapi_v2_contract_inventory.py` | Fixing it needs changes to `tools/evidence/generate_hdapi_v2_contract_inventory.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py`. Instruction §7: "No change to any `tools/**` or `scripts/**` file"; §6: "Any other file the work needs is a finding: route it under §14 before changing it" | Approve adding the two tool files to WU-PR-01 for the bounded corrections of §3.3, or rule `IN_SCOPE_REPAIR` if Plan v1.1 WU-PR-01 ("the retained test files, fixed where they fail") already authorizes them |
| RP-2 | `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` | It exposes a real product defect in `engine/charts/loader.py`. Instruction §9.8: "If fixing it needs a non-test change, route it (§14); the file's disposition waits on that route" | Approve retiring the file with the defect recorded in its ledger row and routed to the Product Owner (§4.3) |

**Basis for a request rather than a proposal.** PR-20 owns the rescope request during pre-Proceed planning: "The originating PR implementation author owns the rescope request/proposal ... PR-20 during pre-Proceed planning". RS-10 is "optional proposal support". RS-20 accepts "exactly one complete read-back `RESCOPE_REQUEST` from PR-20/PR-30/PR-35 or `RESCOPE_PROPOSAL` from RS-10". This is that one request; RS-10 was not used.

**What this request does not do.** It approves nothing, authorizes no implementation, rewrites no approved base, requests no Proceed and creates no PF10 addendum.

**Materiality.** Neither item changes an approved acceptance criterion, a protected architecture, security, data-model or external-contract boundary, another unit's scope, an accepted dependency, or budget, schedule or risk needing Product Owner direction. The author therefore does not claim either is material under the Epic-level definition the RS prompts share. Each exceeds instruction v1.0 as the IA issued it (§6, §7, §9.8), so the IA decides. RS-20's matrix allows `APPROVE`, or `IN_SCOPE_REPAIR` where "the existing immutable base plus already active overlays authorizes the repair". The author recommends whichever the IA finds correct for each item; §3.4 and §4.4 give the evidence against each excluded outcome.

## 2. Stage, lineage and completed work

- **Originating stage:** PR-20 pre-Proceed planning. No Proceed, workspace vehicle or code PR exists, so there is no `PR_RETURN_PHASE`.
- **Lineage:** Specification v1.1 → Plan v1.1 + review v1.1 → instruction v1.0. PF10 v13.5.2 has no overlay. `docs/pfcanon/` is unchanged since `df23bbf` (#614).
- **Completed valid work** (preserved; nothing in it depends on the outcome except the two files): `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.0.md`, state `PENDING`. It contains:
  - the inventory re-verified at `a8c99d1` (135 uncovered);
  - a per-file sweep;
  - 133 decided dispositions: 42 retain, 26 retain and fix, 65 retire;
  - the S04 and S05 designs, each with pinned tests and negative controls;
  - an integrated prototype in a scratch clone. With every in-scope change applied, the coverage computation leaves exactly these 2 files uncovered. The pinned workflow suites give 313 passed and 1 failed (the new coverage guard, naming these 2 files). All 162 full-validation targets pass in one detached-worktree run: 2,962 passed with a clean tree.
- **Unchanged obligations:** WU-PR-01 acceptance (1)–(5), evidence obligations, exclusions other than the bounded RP-1 addition, contracts C-1 to C-6, nonclaims, and the PR-30/PR-35 split.

## 3. RP-1 — HDAPI v2 contract-inventory tools left stale by HDE-EPIC040 PR06a

### 3.1 Finding and evidence

`tests/evidence/test_hdapi_v2_contract_inventory.py` is one of the 135 files. It has 298 tests; at `a8c99d1`, 26 fail in the sweep environment.

**Group A: 5 failures, environment.** The generator's `parse_yaml_openapi` shells out to `ruby` (`tools/evidence/generate_hdapi_v2_contract_inventory.py`, line 2530). `ruby` lives in `/usr/local/bin`, which the sweep's `PATH` omitted. With it on `PATH` these 5 pass. Ruby is declared in no requirements file or workflow. GitHub's Ubuntu 24.04 runner image lists "Ruby 3.2.3" (actions/runner-images `Ubuntu2404-Readme.md`, image 20261004.327.1), and PF09.5 HDE-FERM006.2 records that "Ruby was installed before rerunning the check to PASS".

**Group B: 21 failures, tool drift.** This session re-verified the drift in a throwaway clone with full history, Python 3.12.3, closed rails and `ruby` on `PATH`. At `a8c99d1`: 21 failed, 277 passed, in 98 s. At `cf9198df`, the parent of `d79cfc1c` ("HDE-EPIC040-PR06a: Reader v2 full Magic-10 on POST /api/reader ..." #508): 298 passed, in 100 s. The tree was clean after both runs. A worker's bisection on the same interpreter places the first failing commit at `d79cfc1c` (21 failed). HDE-EPIC040 PR05's clean result was measured at `25b2c87b`, an ancestor. Two independent causes:

1. **The analyzer does not follow presenter provenance into the new Reader helper.**
   - Since `d79cfc1c`, the production Reader view `reader_post` returns `_production_reader_response(emit_fn)`, a module-level helper (`adapter/http_reader.py`, line 509) that calls its `emit_fn` parameter.
   - `get_reader_api_bp` defaults that parameter to `emit_reader_public_bytes` (line 553), imported from `engine.runtime` (line 11).
   - `_adapter_routes_without_presenter` in `tools/evidence/hdapi_v2_boundary_analyzer.py` (line 1791 onward) does not follow the parameter-passed emitter into the helper, so it reports `reader_post` as a route without presenter provenance.
   - **Not a product defect:** the Reader still emits only through the presenter (PF02 "Emitter rule", as the worker read it).
2. **The generator's public-route baseline predates the PF05 production Reader.**
   - The baseline is `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` (generator line 135; the records run to about line 2382; last changed in `dbc7e650`, 2026-06-23).
   - It has no record of `reader_post`, `reader_method_not_allowed` or `reader_post_not_allowed`, nor of `api_bp` / `reader_api_bp` registered at `/api` in `adapter/factory.py`, `adapter/http_reader.py` and `adapter/wsgi.py`. It still holds the removed `reader_v1_post`.
   - The generator therefore fails closed at HEAD (`ADAPTER_BOUNDARY_CHECK_FAILED:presenter_emitter_inspected,no_presenter_bypass,no_public_reader_change`; rc 1, nothing written). It has no `--check` mode, so no CI lane noticed.

**Sufficiency.** With both corrections applied as non-test diagnostic edits in a throwaway clone (then reverted), the file passed 298/298. The diagnostic edits were a baseline regenerated from the current public route records, and the presenter check cleared. The worker cleared it by inlining the helper in `adapter/http_reader.py`; that is not the proposed fix (§3.3).

**Why no test-only fix exists:**
- Building the baseline from discovery inside the test makes the drift check tautological.
- Pinning old adapter copies as fixtures stops the test proving the current repository.
- Stubbing the boundary proof hides that a governed generator cannot run at HEAD.
- Any of these would change "the test's expectation" to reach green, which instruction §9.8 and Plan R-1 forbid.

**Why the file cannot simply be retired.** Under the fix-versus-retire criterion (review v1.0 N2, instruction §9.2), a file of current, governed behaviour is not retired without a named replacing test.
- This is the only test of both tools.
- The tools implement current invariants and artifact families: PF02 single HTTP home and presenter-only emission; PF12 §8.6.3.10, the HDAPI v2 contract-inventory family (worker-read).
- Covered tests overlap only partially: `tests/evidence/test_architecture_snapshot.py`, `tests/cli/test_serializer_guards.py`, `tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py`.
- Canon citations of this test (PF09.5 lines 2108, 2114; PF09.6 line 1756; PF14 lines 6561, 6721) are historical records, not current requirements.

**Ownership state today.** Changes to either tool already fail CI classification:
- the analyzer is in `_EVIDENCE_HELPERS_REQUIRING_OWNER` (classifier line 653), so a change raises `CI_EVIDENCE_HELPER_OWNER_MISSING`;
- the generator has no `_EVIDENCE_GENERATOR_TEST_OWNERS` entry, so a change raises `CI_EVIDENCE_OWNER_TEST_MISSING`.

### 3.2 Alternatives considered

| Alternative | Assessment |
| :- | :- |
| A1. Add the two tool files to WU-PR-01 for the two bounded corrections, and register this test as their owner (recommended) | Smallest change that satisfies acceptance (1) without hiding a defect. No release member, governed artifact or acceptance criterion changes |
| A2. Leave the file uncovered and carve it out of WU-PR-01's acceptance (1); route the tool repair to a new or later unit | Changes approved acceptance (1) and adds a unit (material); S03's intent "No test file runs in no CI lane" would not hold when WU-PR-01 merges |
| A3. Retire the test with both tools as historical (paired generator and owner retirement) | A product decision for the Product Owner. The tools serve current PF02 and PF12 obligations; not recommended |
| A4. Retire the test only | Violates N2 (current behaviour, no replacement); leaves both tools untested |
| A5. Test-only change | Hides the defect (§3.1); forbidden |

### 3.3 Proposed bounded delta (A1)

Added to WU-PR-01's bounded files (instruction §6). Each change is limited as stated.

| Path | Bounded change |
| :- | :- |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | Replace `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` with the public route records the three app factories register at the PR head. Review them against the PF05 production and dev Reader route set (§5.1.0, §5.4) before committing: they must contain `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed` at `/api`, and no `reader_v1_post`. No other change to the generator: no change to its outputs, schema, evidence family or refusal codes. It is not run in write mode against the repository |
| `tools/evidence/hdapi_v2_boundary_analyzer.py` | In `_adapter_routes_without_presenter`, accept presenter provenance through a module-level helper that the view calls with a parameter whose bound value or default is a sanctioned presenter callable (the `get_reader_api_bp` → `_production_reader_response(emit_fn)` shape). Bypass detection must not weaken: a helper whose parameter default is not a sanctioned presenter callable, or that emits through any other path, must still be reported. The design of the AST change is not yet prototyped (§6) |
| `ci/checks/classify_ci_changes.py` (already in WU-PR-01) | `_EVIDENCE_GENERATOR_TEST_OWNERS["tools/evidence/generate_hdapi_v2_contract_inventory.py"] = ("tests/evidence/test_hdapi_v2_contract_inventory.py",)`; move `tools/evidence/hdapi_v2_boundary_analyzer.py` from `_EVIDENCE_HELPERS_REQUIRING_OWNER` to `_EVIDENCE_HELPER_TEST_OWNERS` with owners `tests/evidence/test_hdapi_v2_contract_inventory.py` and `_EVIDENCE_HELPER_OWNERSHIP_TEST`. These two new source keys are the plan's only exception to its no-new-key rule (plan §5.1); without them the tool edits fail classification |
| `tests/evidence/test_hdapi_v2_contract_inventory.py` (already in WU-PR-01) | Move the untracked `<ROOT>/tmp_boundary_test/` fixtures (about 103 call sites, removed in `finally` today and not git-ignored) to `tmp_path`. Add one positive analyzer case (the helper shape above is accepted) and one negative case (a helper with a non-presenter default is reported). Register it under the plan's §5.1 rule (`pytest.ini` + supplemental) |
| `tests/evidence/test_rails_ci_workflow_integration.py` (already in WU-PR-01) | Any pin over `_EVIDENCE_HELPERS_REQUIRING_OWNER` or the generator-owner set is kept true. `test_non_generator_evidence_helpers_have_exact_fail_closed_owners` iterates the set and needs no change |

**Verification (PR-30, local), in addition to the plan's §11:**
- the file passes 298 of 298 plus the two new cases, with `ruby` on `PATH`, in the detached-worktree full-validation run, with a clean tree and a clean mtime check;
- no test of the file is skipped or deselected;
- `changed_test_targets(ROOT, ("tools/evidence/generate_hdapi_v2_contract_inventory.py",))` and the same for the analyzer return the test (plus the ownership test for the analyzer);
- `git diff base..head -- artifacts/vendor/hdapi_v2/ docs/evidence/ artifacts/evidence_index.jsonl` is empty.

**Effects:**
- **Requirements:** S03 acceptance (1) and (2) become reachable. S04, S05 and acceptance (3)–(5) are unaffected.
- **Dependencies:** none upstream. WU-PR-06's `sweep` (C-3) is unaffected: the coverage definition does not change.
- **Ops:** none.
- **Documentation:** OBS-12 (the Ruby dependency) goes to the Product Owner as a Glow Infrastructure doc-delta candidate.
- **Downstream units:** none. WU-PR-03 later changes `adapter/factory.py` and `adapter/http_reader.py` routes (IF-11 handlers), so it must keep this baseline current. That becomes a visible dependency, where today it is silent drift.
- **Release:** no member changes (`tools/evidence/` holds no release member), so there is no manifest refresh.
- **CI:** the two tools are evidence-lane paths, and WU-PR-01 is already full validation.

**Exclusions that stay:**
- no other `tools/**` or `scripts/**` change;
- no regenerated governed artifact; the frozen HDE-EPIC033–035 captures stay unchanged;
- no live vendor call; no public route change.

### 3.4 Evidence against the excluded outcomes

- **REJECT:** the boundary is real and evidenced. Without the delta, the file has no lawful disposition (A2–A5).
- **REVISION_REQUIRED:** the evidence, alternatives, bounds and verification are stated. The one unprototyped item, the analyzer's AST change, is a design detail inside a bounded locus, with acceptance tests named.
- **SPECIFICATION_CHANGE_REQUIRED:** S03's intent ("recorded failures and collection errors are fixed or retired with their files") does not restrict fixes to test code. The delta stays within it and changes no product behaviour.
- **IN_SCOPE_REPAIR:** possible only if the IA reads Plan v1.1's deliverable "the retained test files, fixed where they fail" as authorizing tool fixes despite instruction §7's exclusion. The author does not presume that reading.

## 4. RP-2 — legacy chart-loader defect

### 4.1 Finding and evidence

`tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` has 2 tests. At `a8c99d1`, 1 passes and 1 fails.

**The failure.** `test_loader_uses_fixtures_by_default_in_safe_mode` calls the legacy signature `load_chart("user-abc", correlation_id=...)`. `engine/charts/loader.py` `_call_legacy` (lines 76–82) then calls `provider.get_chart(...)` on the provider that `engine.config.provider_loader.resolve_provider()` returns, an `engine.provider.fixtures.FixturesProvider`. That class has no `get_chart`: `AttributeError: 'FixturesProvider' object has no attribute 'get_chart'`. The behaviour broke at `6c6f4b2` (2025-09-28), which removed the `_ensure_provider_with_get_chart` fallback added in `4887012` (worker pickaxe).

**The passing case.** `test_loader_vendor_path_is_gated_in_safe_mode` monkeypatches the resolver to a `VendorHttpProvider` and asserts `ProviderUnavailable` with `safe_mode`.

**Reach.**
- No non-test code calls the legacy signature. The only non-test importer of `load_chart` is `scripts/make_compat_determinism_artifacts.py`, through the current signature.
- `engine/charts/loader.py` is not a release member.
- The loader is not reached at runtime: `adapter/http_reader.py` uses its own `_safe_load_chart`.

**Canon.** PF02 §1.1 "Non-BodyGraph chart loader classification" calls the loader "implementation drift ... current repository reality until separately remediated". PF09.3 Separation HDE-SEPA006.2 migrates "relevant loader/provider tests" and removes "the old operational Engine path". Both were read by a planning worker and reported. Neither HDE-SEPA006 nor this path is in HDE-CRD-0002's Specification.

**The file writes.** It appends to tracked `artifacts/logs/loader_call.jsonl` on every run. That file has already been committed with test-run appends (`39a5a33`, `f3e1f9a`, `c6fdc91`).

### 4.2 Alternatives considered

| Alternative | Assessment |
| :- | :- |
| B1. Retire the file. Its ledger row records the defect and the route; the defect evidence goes to the Product Owner as owner of HDE-SEPA006 (recommended) | No non-test change. The defect stays recorded and routed to its canon owner. The passing case has a retained replacement (§4.3) |
| B2. Add `engine/charts/loader.py` to WU-PR-01 for a minimal `_call_legacy` repair | Requires deciding the correct behaviour of a legacy path that canon assigns to HDE-SEPA006 for removal; an architecture decision outside HDE-CRD-0002's Specification |
| B3. Keep the file and leave it uncovered or failing | Violates acceptance (1) or (2) |
| B4. Delete only the failing test function | Hides the defect inside a retained file; the remaining function duplicates a retained test |

### 4.3 Proposed bounded delta (B1)

- **Retirement.** Delete `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` under the plan's §6 class (b) (not a governed surface: a legacy signature that no current entrypoint reaches).
  - **Ledger reason:** "Exposes a product defect in the legacy signature of `engine/charts/loader.py` (`_call_legacy` calls `get_chart` on a `FixturesProvider` that has none, since `6c6f4b2`). Only tests call it. The defect is routed to the Product Owner as owner of PF09 Separation HDE-SEPA006 (PF02 §1.1 'Non-BodyGraph chart loader classification'). Not fixed in HDE-CRD-0002."
  - **Replacing coverage** for the passing case: `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` (retained, fixed) and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` (retained).
- **Routed finding.** The defect evidence of §4.1 goes to the Product Owner, through the IA's RS-20 decision artifact or its next handoff, as an HDE-SEPA006 input. No Plan unit of HDE-CRD-0002 owns it.

**Effects:**
- **Requirements:** acceptance (1) becomes reachable.
- **Unchanged:** no other unit, no Ops, no documentation, no release member.
- **Totals:** the plan's retirement count becomes 66.

### 4.4 Evidence against the excluded outcomes

- **REJECT:** without a decision the file has no lawful disposition (B3).
- **REVISION_REQUIRED:** the defect, reach, canon owner and replacement are stated.
- **SPECIFICATION_CHANGE_REQUIRED:** retirement with a recorded reason is an S03 disposition; nothing in the Specification changes.
- **IN_SCOPE_REPAIR:** possible if the IA holds that S03 retirement with a routed finding is already authorized. Instruction §9.8 makes the disposition wait on the route, so the author asks.

## 5. Combined effect, if both items are approved as proposed

- **Dispositions:** 42 retain, 27 retain and fix (RP-1's file joins), 66 retire (RP-2's file joins). Zero files remain uncovered.
- **Classifier and configuration:** the supplemental tuple goes from 40 to 109 entries and `pytest.ini` gains 68 file entries. Two new owner keys are added (RP-1); no other.
- **Loci beyond instruction §6:** the two RP-1 tool files only.

## 6. Risks, conflicts and unresolved facts

| Item | Status | Owner |
| :- | :- | :- |
| The analyzer change of §3.3 is not prototyped | Unresolved design detail inside the bounded locus; acceptance tests named. If PR-20 v1.1 finds it cannot be done without weakening bypass detection, that is a new finding to this IA | PR-20 v1.1 (this author) |
| Ruby on `ubuntu-latest` after its announced move to Ubuntu 26.04 (November 2026) | Unknown; Ubuntu 24.04 provides Ruby 3.2.3 | PR-35 observes hosted CI; OBS-12 to the Product Owner |
| WU-PR-03 route changes must keep the RP-1 baseline current | A new visible dependency; WU-PR-03 already lists `adapter/factory.py` and `adapter/http_reader.py` | IA (WU-PR-03 instruction) |
| Canon conflict | None new. CR-1 to CR-3 carried unchanged | — |
| Specification or product-intent change | None requested | — |

## 7. TypeSafe reading for the receiving session (RS-20)

Identical to plan v1.0 §21 (one send, recorded in both artifacts):

Action sent (v6): "Review, as the whole-change Implementation Agent and first reviewer of this new request, a rescope request from the PR planning session of the first unit of an approved CRD Implementation Plan: two boundary findings, each with a proposed bounded delta — two governed evidence tools (a 4,800-line generator and a 3,200-line analyzer) left stale by an earlier Reader route change, whose repair the unit's instruction excluded from its file list (proposal: add the two tool files and their owner registrations to the unit), and a legacy chart-loader defect that canon assigns to a separate future build item (proposal: retire one test file and route the defect to the Product Owner) — then decide approve, reject, revision required, in-scope repair or specification change, and write the review and, only on approval, one build-notes addendum. It reads the request, the 135-file planning draft it suspends, the approved Plan, Specification and canon; no code is written and no live provider call occurs; a revised detailed PR plan, a Product Owner Proceed, implementation and independent reviews follow."

- **TypeSafe v6: Fable 5.1, extra high.** Effort score 3.29 (confidence 0.54); rung probabilities low 0.00, medium 0.00, high 0.16, extra high 0.37, max 0.47, ultracode 0.00. Model probabilities Fable 5.1 0.58, Opus 5.5 0.42 (confidence 0.16). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.00, Opus 5.5 at high 0.07, Opus 5.5 at extra high 0.16, Opus 5.5 at max 0.20, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.09, Fable 5.1 at extra high 0.21, Fable 5.1 at max 0.27, Fable 5.1 at ultracode 0.00. Flags: boundary between extra high and max; model near tie. Sent 2026-10-12T22:27:59Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T22:27:59Z; HTTP 200 in 0.8 s; 4338 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Fable 5.1 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between extra high and max; model near tie.
- No Notion row was written. **Nathan's pick for RS-20:** not stated.

**Surface advice:**
- Run RS-20 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the continuing whole-change IA role for HDE-CRD-0002.
- **What to re-check:**
  - RP-1, by running `tests/evidence/test_hdapi_v2_contract_inventory.py` at `a8c99d1` and at `cf9198df`. Use a throwaway clone with full history (the local checkout is shallow, 50 commits) and `ruby` on `PATH`; about two minutes each.
  - RP-2, by reading `engine/charts/loader.py` lines 50–100 and `engine/provider/fixtures.py`.
- **What to read:** `docs/pfcanon/` on `main`, including PF02 §1.1, PF09.3 HDE-SEPA006 and PF12 §8.6.3.10.
- **What it needs:** no live vendor, production or database access. It writes its review, and one addendum only on `APPROVE`.
- **Prerequisite:** merge the pull request carrying this request and plan v1.0 first.

## 8. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-20 / WU-PR-01 / rescope request 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 |
| work unit | WU-PR-01; S03 (acceptance (1), (2)) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; receiver contract read: RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; RS-10 read, not used |
| role/stage | originating PR implementation author / PR-20 pre-Proceed planning |
| capture time | 2026-10-12T22:36:44Z |
| execution identity | https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8 |
| repository persistence | PENDING / NON_GATING (no `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `a8c99d1`); recorded here only |

## Canon relied on

Read on `main` at `a8c99d1`. The full list, with sections and the split between canon this session read and canon the planning workers read and reported, is in plan v1.0 "Canon relied on". The sections that bear on this request's decision topics:

- **Rescope authority and outcomes:** RS-20, RS-10 and PR-20 — 100926.1 (rescope authorship, decision matrix, materiality definition, return routing); PF04-Canon-HDE-Governance v2.8.7 §9.1.1 (the PR session authors the detailed per-PR Plan; the IA issues PR instructions) and §9.7.7 (no scope laundering; no proof by intent).
- **Fix-versus-retire and the CI-lane rule:** PF27-Canon-Plan-Templates v2.0.5, "CI lane classification and automated budget-control discipline" (read in full); Plan review v1.0 N2 as carried by review v1.1 §4 and instruction §9.2.
- **RP-1 subject matter** (worker-read and reported): PF02-Canon-HDE-Architecture v2.4.6 §2.1 (single HTTP home, emitter rule); PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.6.3.10; PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.1.0 and §5.4 (Reader routes); PF09.5 HDE-FERM006.2. Read by this session: the PF09.5, PF09.6 and PF14 lines that cite the test (historical records).
- **RP-2 subject matter** (worker-read and reported): PF02 §1.1 "Non-BodyGraph chart loader classification"; PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.7 HDE-SEPA006, .1, .2, .3.
- **PF10-HDE-Build-Notes v13.5.2:** read in full; silent on both items.
- **External:** GitHub actions/runner-images `Ubuntu2404-Readme.md` (Ruby 3.2.3).

---

**Status:** `RESCOPE_REQUEST_PENDING_REVIEW` — one request, two items (RP-1, RP-2), from the WU-PR-01 PR-20 author to the whole-change IA through RS-20.

ASK OK?
