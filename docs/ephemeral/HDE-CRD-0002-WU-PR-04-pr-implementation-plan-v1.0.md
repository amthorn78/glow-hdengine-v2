---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-04-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 1 (first plan for this work unit)
predecessor: none
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff (the prototype's diff from 9c82b62 for the 11 hand-edited paths of §7.1; owner-produced paths excluded; §4.4)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-04
work_unit_title: "Provider gate and Aux preview (PR; Fermentation; S08, S14)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 51371eeae9d9; 73,805 bytes; landed by amthorn78/glow-hdengine-v2#649 at 9c82b62)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — lineage only
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10). None is rewritten
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review); 2.5 (LR-O1 to LR-O3, OBS-17, O-6, carried); 2.6 ("Affected surfaces", Dependencies and Downstream work: the 22-path roster; the updater-consumer, label-timing and stale-label rules; the step-3b order and restart point); 2.7 (AD-5 "Order" and "New base"; "Affected surfaces" Downstream: refresh from the new release_id); 2.8 (the WU-PR-03 acceptance and its "Carried into the WU-PR-04 instruction" list). 2.1 governs §21 only. 2.2 and 2.4 have no item for this unit
effective_baseline: approved base + applicable PF10 overlays = the base above + addenda 2.3, 2.5, 2.6, 2.7 (AD-5 and its downstream items) and 2.8, as instruction v1.0 applies them
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md (v13.5.9, effective 2026.10.18; blob a125fd4eefbf; 135,146 bytes; sha256 361274ddcb0e04e1d8986e2bfff4529912b5bba06a9c57820b8bc12a1adbff1e). Resolved afresh on main at 9c82b62: the unique controlled PF10; unchanged since b9edb0c (git diff b9edb0c 9c82b62 adds only the instruction)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md §2.3, §2.5, §2.6, §2.7, §2.8; §2.1 for §21
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the dedicated HDE-CRD-0002 WU-PR-04 PR engineering session, created by Nathan / Product Owner)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8
author: dedicated HDE-CRD-0002 WU-PR-04 PR engineering session (PR-20)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the merge; RS-20 for any rescope; PR-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T12:08:43Z
repository_baseline: origin/main 9c82b62de348471b00dd44af8db276a4d14f69f9 (tree 09be2edb541d; #649). git diff 39afdc6..9c82b62 changes only docs/pfcanon/ (b9edb0c, PF10 v13.5.8 → v13.5.9) and docs/ephemeral/ (#649), so every repository fact of instruction §5, measured at 39afdc6, holds here; re-verified (§4.1)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-04 — Detailed PR Implementation Plan v1.0

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.1.1).

This is the complete, executable plan for WU-PR-04:
- S14, the production vendor override of HDE-CLI-API-Vendor-Ref §7.1.11a to §7.1.11f, with IF-1, IF-2 and EC-7;
- S08, the `aux-preview --band` fix for pair-file input;
- the ID-8 adjustments, the ID-10 classifier registration and the documents line;
- the same-version release refresh at `1.3.0` with its governed-evidence convergence.

It applies instruction v1.0's ID-1 to ID-10 as written and records every choice instruction §9.1 leaves to PR-20 (§15). The design was prototyped in scratch clones, its refresh rehearsed in two byte-identical passes on the final bytes, and the result swept in full (§4.3). The prototype also found two defects the instruction could not see, both fixed inside its bounds (F-3 and F-13, §4.2).

Authority:
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` (v1.0) authorizes implementation. Only Nathan merges.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure, and no live use of `--allow-prod-vendor`. It changes no canon and creates no PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-04 (Plan v1.1 §7 "WU-PR-04 — Provider gate and Aux preview (PR; Fermentation)") |
| Requirements | S08, S14; EC-7; IF-1, IF-2; the same-version refresh |
| Binding IA decisions | instruction §4.2 ID-1 to ID-10 |
| Carried review note | review v1.0 N4 (override actor principal and sink key), carried by review v1.1 to this plan: §6.6 and §6.7 |
| Upstream units | WU-PR-01 (addendum 2.4), WU-PR-02 (addendum 2.5) and WU-PR-03 (lineage review v1.0, addendum 2.8): all accepted |
| Refresh base | `release_id` `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7` (addendum 2.7 AD-5 "New base"; manifest sha256 at 9c82b62) |
| Downstream | WU-PR-05 refreshes from this unit's `release_id` and reviews the override code under S19; WU-PR-06 reads the ID-10 registrations; WU-PR-08 cuts `1.4.0`; WU-DOC-01 owns the repository documents of §17; the QA Plan designs the live call on contract F-2 |
| Phase | Fermentation |
| Live QA class | S08 functional-feature; S14 functional-feature with the mandatory live vendor call (Specification table; Plan §6). The live call is QA's, not this unit's |

## 3. Sources read

Read completely by this session:
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion, page state 2026-10-12T02:29:47Z).
- PR instruction v1.0 (all 20 sections and "Canon relied on").
- HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`): §7.1.10 and §7.1.11 to §7.1.11f in full; §3.1, §3.1.1, §3.3, §3.4; §4.5; §4.6; the §7.2.0 posture paragraph.
- PF10 v13.5.9: addenda 2.1 and 2.3 in full; 2.5 "Retained decisions and requirements"; 2.6 "RP-2", "Binding requirements", "Scope, exclusions and nonclaims", "Affected surfaces" to "Status and consequences"; 2.7 AD-5 and "Affected surfaces"; 2.8 in full.
- Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1 (key names, the `HDE_` names in use).
- HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §10.1, Recipes F and G, §16.
- Specification v1.1 rows S08 and S14 and constraints "Release members", "Vendor override", "Override initiator", "Live QA", Exclusions; Plan v1.1 §3, §4, §5 (IF-1, IF-2), §7 (common paragraph; WU-PR-04 block), §10 to §14; review v1.0 N4 and review v1.1's carry line; Audit §6 S08 and S14 and §7.1 EC-7.
- WU-PR-03 plan v1.1 (structure precedent) and WU-PR-03 result v2.0 §8 (the converged refresh).
- Code: `engine/cli/main.py` (parser, `_resolver_env`, `bg_resolve`, `cli`, `aux_preview`); `engine/bodygraph/resolver.py` (`resolve_bodygraph`, `_resolve_vendor`, `_resolve_vendor_v2_chart`, `_vendor_config_env`, `_classify_env_route_policy`, `_vendor_error`, `_acquire_dry_run`); `engine/bodygraph/vendor_client.py` (`VendorError`, `HdApiClient.__init__`, `from_env`, `fetch`, `_default_request`, `classify_bg_resolve_route_policy`, status mapping); `engine/bodygraph/ingest.py` (in full); `engine/serializer/canon.py::sercanon` output form; `engine/runtime/determinism_env.py` pins; `tools/evidence/generate_v2_mapped_cache_evidence.py` (hermetic guard and resolver exercise); `tools/evidence/generate_hde_epic037_bg_resolve.py`; `tools/evidence/build_release_attestation.py` (`CLOSED_RAILS`, `_clean_child_env`, the isolated stages); `tools/cli/emitter_symbol_proof.py`; `ci/checks/check_cli_help.sh`; `ci/checks/classify_ci_changes.py` (registries); `ci/jobs/*.yml`; `.github/workflows/ci.yml` (setup, changed-tests step, all seven lanes); `scripts/ops/admin_vendor_qa.py`.
- Tests: `tests/cli/test_bg_resolve.py`, `tests/cli/test_aux_preview.py`, `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` (in full); `tests/bodygraph/test_bg_resolve_route_policy.py` (environment usage); `tests/evidence/test_rails_ci_workflow_integration.py` (registry pins).

## 4. Repository baseline (verified at `9c82b62`)

### 4.1 Instruction facts re-verified

`git diff --name-only 39afdc6 9c82b62` outside `docs/pfcanon/` and `docs/ephemeral/` is empty. Every instruction §5 fact this plan relies on was re-read at `9c82b62`; none differs:
- Parser, `_resolver_env`, `bg_resolve` and `cli()` as §5.1 states; no `--allow-prod-vendor` outside `docs/`.
- `_resolve_vendor`'s order and the only `APP_ENV`/`ENGINE_ENV` reading (the v2 write guard) as §5.2 states.
- The shared acquisition paths of §5.3: `_acquire_dry_run` calls `_resolve_vendor_v2_chart` directly and `ingest_vendor_bodygraph(dry_run=True)`.
- The write paths of §5.4; the codes of §5.5; the Aux pair-file path of §5.6; the tests of §5.7 (6, 2, 4 and 13 test functions; 28 collected cases in the mapped-cache file).
- Manifest: `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`, 45 members, sha256 `d84d99e1…`.
- Classifier at `9c82b62` (run): `engine/bodygraph/vendor_audit.py` → `CI_PRODUCT_OWNER_TEST_MISSING`; `tools/evidence/generate_v2_mapped_cache_evidence.py` → `CI_EVIDENCE_OWNER_TEST_MISSING`.
- Baseline full `tests/` sweep at `9c82b62` (this session): **4,761 passed, 3 skipped, 2 xfailed, 0 failed** (1,544.8 s), equal to the WU-PR-03 lineage review's count on `2f3db0a`.

### 4.2 Facts this session established (not in the instruction)

| ID | Fact | Effect on the plan |
| :- | :- | :- |
| F-1 | argparse prints `invalid choice: 'X'` and `unrecognized arguments: X` for options it does not own, so `hdctl showcompat --allow-prod-vendor X` and `hdctl --allow-prod-vendor X bg:resolve …` echo the value on stock argparse | The pre-scan runs over the whole `argv` before argparse and also refuses the option outside `bg:resolve` (PD-1) |
| F-2 | `ci/checks/check_mirror_schema.sh`, `check_evidence_index_hash.sh` and `check_final_lf.sh` are Python scripts with a `.sh` name; `bash <path>` fails with a syntax error. WU-PR-03 recorded the same (its F-25) | The refresh invokes them by path (§6.13) |
| F-3 | `tools/evidence/build_release_attestation.py` runs its isolated stages in `_clean_child_env()`: `PATH`, `TMPDIR` and `CLOSED_RAILS` only, **no `APP_ENV`**. Its `release_sanity` stage runs the sanity pipeline, whose stage 06 runs `ci/jobs/rails_closed_refusal.yml` and `ci/jobs/logs_keys_only_redaction.yml`, both `python -m pytest tests/bodygraph/test_resolver_vendor.py`. Two existing tests there (`test_vendor_resolver_maps_synthetic_user`, `test_vendor_resolver_wraps_unexpected_normalization_errors`) pass an open-rails mapping without `APP_ENV` and rely on the ambient value. With S14's step 4 they refuse `PROVIDER_CONFIG_INVALID` there. Observed: the attestation build exits 1 with `RELEASE_ATTESTATION_FAILED:isolated_stage_failed` (`stage: release_sanity`); every CI lane, which sets `APP_ENV=dev`, stays green | ID-8 "Test-environment setup": both mappings gain `"APP_ENV": "test"`; nothing else changes. The attestation then builds and verifies (§4.3). Not in instruction §5.7 or §5.8 |
| F-4 | With `APP_ENV` unset, six tests of `tests/bodygraph/test_bg_resolve_route_policy.py` fail on the prototype and pass on `main`: `test_v2_resolver_dry_run_maps_payload_through_adapter`, `test_v2_adapter_unsupported_becomes_typed_resolver_error`, `test_v2_non_dry_run_without_upsert_fails_closed_before_fetch`, `test_bg_resolve_cli_v2_dry_run_uses_adapter`, `test_resolver_uses_single_merged_config_source_for_policy_and_ingest`, `test_resolver_v2_override_uses_v2_even_when_process_env_is_v1`. Every lane and the changed-tests step set `APP_ENV=dev`; neither the sanity pipeline nor the attestation runs this file | Not changed: the file is outside instruction §6 and the work does not need it (§6.9). OBS-P4-2 |
| F-5 | `tools/evidence/generate_hde_epic037_bg_resolve.py --check` and `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py --check` exit 1 **on `main` at `9c82b62`** (`STALE_HDE_EPIC037_PR03_BG_RESOLVE:…v2_route_policy.snapshot.json,…request_shape.snapshot.json`; `STALE_HDE_EPIC036_BG_RESOLVE_ROUTE_POLICY:…`). Their captures bind source digests of release members (`inspected_internal_loci`), which earlier units changed. Comparing the EPIC037 generator's in-memory outputs on `main` and on the prototype: all four bodies are equal, the closed-rails envelope included; only the `inspected_internal_loci` digests of `engine/bodygraph/resolver.py` and `engine/cli/main.py` differ. The EPIC036 tool does not call the resolver | Instruction §10 lists the EPIC037 `--check` as a validation. It cannot pass at the baseline, so this plan replaces it with the equivalence check (§10 item 7) and records the instruction defect for the IA (OBS-P4-3). Neither tool runs in write mode; `artifacts/vendor/**` stays byte-unchanged |
| F-6 | The EPIC037 generator's open-rails dry run passes no `APP_ENV` and relies on the process `APP_ENV=dev` of the closed-rails profile | Equality in F-5 holds under that profile; recorded in §6.9 |
| F-7 | The changed set of the refresh is 54 paths (§6.13), not WU-PR-03's 61: this unit does not change the catalog validator, so step 3b rewrites the catalog family byte-identically | Expected set in §6.13 |
| F-8 | `aux-preview`'s tuple (`viewer_top=None`, `flags=None`) selects a `.1.` variant key for every band of `balance`, the only category with governed suppressions; both suppressed keys are `.2.` variants | ID-9's suppressed-key sentence is a property of the unchanged Aux emitter; no `--band` value reaches a suppressed key through `aux-preview`, so no test constructs one (§6.10) |
| F-9 | `HdApiClient._default_request` re-checks `SAFE_MODE` and `ALLOW_NETWORK` in the process environment inside `fetch`, before opening a socket | `outbound_attempted` is set when the governed fetch is entered (PD-12) |
| F-10 | `scripts/ops/admin_vendor_qa.py` runs `bg:resolve --source vendor … --dry-run --upsert` without the required `--user`, so it exits 64 today; under S14 a production run would also need the flag and is refused for `--upsert` | Not changed (outside §6); OBS-P4-4 |
| F-11 | `ingest_vendor_bodygraph` accepts a `client` argument and, with `dry_run=True`, constructs no database target | The allowed production legacy path passes an attempt-tracking client (PD-11); the non-production call is unchanged |
| F-12 | `sercanon` returns UTF-8, sorted-key, compact JSON with exactly one trailing LF | The audit line is `sercanon(event)` (§6.7) |
| F-13 | `tests/adapter/test_jsonschema.py::_call` writes `ENGINE_ENV` (finally `dev`) and `ENGINE_SERVICE_TOKEN` into `os.environ` with `os.environ.update` and never restores them. Any later test in the same pytest process inherits them. In the first prototype's full sweep, 31 tests failed with `PROVIDER_CONFIG_INVALID`: 27 in `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` and 4 new ones in `tests/bodygraph/test_resolver_vendor.py`. Their mappings set `APP_ENV=test` or `prod`, which conflicts with the leaked `ENGINE_ENV=dev` under §7.1.11b. Reproduced with `test_jsonschema.py` first and the mapped-cache file second: 27 failed. Each file passes alone, in the changed-tests step and in the lanes | ID-8 "Test-environment setup": both files gain an autouse fixture that removes the ambient `ENGINE_ENV` with `monkeypatch.delenv` (environment setup only). With `test_jsonschema.py` first in the same process: 195 passed, 2 xfailed. `tests/adapter/test_jsonschema.py` is outside §6 and is not changed (OBS-P4-7) |

### 4.3 Prototype (this session; scratch only, never pushed)

Two kinds of scratch copy were used:
- a detached worktree of `9c82b62` in the session scratchpad, for edits;
- independent clones (`git clone --no-local`, `origin` removed) for commits, rehearsals and sweeps.

Common environment: CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`), pytest 8.4.2, `ruby` at `/usr/local/bin/ruby` (3.3.6), `bash`, `curl`. Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Unset, by name: `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `ENGINE_ENV`. The container sets several of them.

Rehearsal record:

**First rehearsal** (the first design, before F-3 and F-13):
- The refresh, two passes: 37 and 34 runs, all exit 0; the two passes' `git diff` were byte-identical (SHA-256 `293d068a…`); 54 changed paths; rehearsal `release_id` `e0e21ba5…`.
- The attestation build exited 1 at `release_sanity`. That is F-3.
- After the F-3 fix:
  - the attestation build and verify exited 0;
  - the classifier selected all seven lanes for 65 paths and 166 targets;
  - the changed-tests step: 3,677 passed;
  - all seven lanes were green: product 77; compat 103 passed, 3 skipped, 2 xfailed; db 249; rails jobs 24, 113 and 59 with the pin file 138; evidence 130; qa 488; release 79.
- The full sweep, run on the state before the F-3 fix: 31 failed, 4,882 passed, 3 skipped, 2 xfailed (1,763 s). All 31 are F-13, fixed in the final design.

**Final rehearsal** (the bytes of the companion diff, from `9c82b62`):
- the member bytes in the diff produce the rehearsal `release_id` `89ddc78587619790170579abe33cd60fe3799cc017df62462424825c337b145d` (45 members, `1.3.0`; recompute and cutter `--check` exit 0; two manifest rows change). It is a rehearsal value only: PR-30's own bytes fix the real one (PD-18);
- the refresh, steps 2 to 10, two passes (§6.13): pass 1 (steps 2–10) 37 runs and pass 2 (steps 3–10) 34 runs, all exit 0; sanity `summary:PASS` twice; open-rails digest `c5701a853dc700166f13a55ca4f313395e860e5456425b54341e02303e7c70d9` both times; after each pass 54 paths differ from the source commit and no untracked file exists; the two `git diff HEAD` patches are byte-identical (SHA-256 `f39ee2661beb70cb5486d101a4e3f77043cc477527cabd3459182679108707f5`);
- the step-11 sweep and labels: `git grep -l -E 'd84d99e1|06611525'` outside the excluded prefixes: no hit (exit 1); `docs/` outside `docs/ephemeral/` and `docs/pfcanon/`: no hit. Mirror: 620 rows, 27 labelled rows, all carrying the rehearsal `release_id`; the purity-report row has no `notes`;
- the classifier on the candidate's 65 changed paths: reason `selected_lanes`, all seven lanes, 166 changed-test targets;
- the changed-tests step as CI runs it (detached copy, `git diff --exit-code`, empty status): 3,677 passed, exit 0 (673.9 s); clean tree;
- the seven lanes' commands as `ci.yml` writes them: product 77 passed; compat (`check_cli_help.sh`, serializer guard, emitter proof, tests) 103 passed, 3 skipped, 2 xfailed; db (direct-DB contract check, tests) 249 passed; rails (the three job definitions: 24, 113 and 59 passed; then the pin file: 138 passed); evidence (seven checks, tests) 130 passed; qa 488 passed; release (recompute, tests) 79 passed; every lane exit 0 and the tree clean afterwards;
- the attestation build and verify into an external empty directory with `--require-clean`: build exit 0 (`attestation.json`, its `.sha256`, `build.log`, `evidence/`), verify exit 0, tree clean;
- the full `tests/` sweep: **4,913 passed, 3 skipped, 2 xfailed, 0 failed** (1,648.3 s; 11:29:54Z to 11:57:24Z), exit 0, then `git diff --exit-code` and an empty status. The baseline's 4,761 plus the 152 new cases (96 + 29 + 7 + 20), with the same skips and xfails;
- the four changed test files and the mapped-cache file with `APP_ENV` unset: 192 passed; the same five with `tests/adapter/test_jsonschema.py` first in one process (F-13): 195 passed, 2 xfailed.

Negative controls, each on the final prototype source with one hunk disabled, run on `tests/bodygraph/test_vendor_prod_override.py`, `tests/bodygraph/test_resolver_vendor.py` and `tests/cli/test_bg_resolve.py` (155 cases) unless stated; every one fails as intended, and every file was restored:

| ID | Hunk disabled | Result |
| :- | :- | :- |
| NC-1 | step 5 (production-like goes straight to step 7) | 42 failed, 113 passed |
| NC-2 | the pre-I/O event write | 14 failed, 141 passed |
| NC-3 | ID-3's legacy write refusal | 6 failed, 149 passed |
| NC-4 | the S08 band override (`tests/cli/test_aux_preview.py`) | 3 failed, 6 passed |
| NC-5 | the CLI pre-scan (`test_bg_resolve.py` and the new file, 131 cases) | 20 failed, 111 passed |

Other runs on the prototype, all exit 0 unless stated:
- `generate_v2_mapped_cache_evidence.py --check`;
- `generate_bodygraph_policy_proofs.py --check`;
- `ci/checks/check_cli_help.sh`;
- `serializer_grep_guard.py`;
- `emitter_symbol_proof.py`, whose output is byte-identical to `artifacts/cli/guards/emitter_symbol_proof.txt`;
- `release_id_recompute.py --check-manifest-only`;
- the EPIC037 and EPIC036 `--check`s exit 1, as on `main` (F-5).

### 4.4 Prototype diff (companion file)

`docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff` is the final prototype's diff from `9c82b62` for the 11 hand-edited paths of §7.1. The manifest, the `FROZEN_OPEN_ABBA_SHA256` line and every regenerated governed artifact are excluded: PR-30 produces them with their owners. `git apply --check` succeeds on `9c82b62`.

PR-30 may apply it as its starting point, but owns the implementation:
- it re-reads every hunk against this plan;
- it re-runs §10 on the real branch;
- where the diff and this plan differ, this plan governs, and the difference is a defect PR-30 corrects.

## 5. Scope

In scope (instruction §6; Plan v1.1 §7 WU-PR-04 "Deliverables"; ID-8 and ID-10):
- **S14 (CLI):** the option, its pre-scan, validation, applicability and usage carrier; passing the reference to the resolver (ID-1, IF-1).
- **S14 (resolver):** steps 4 to 6 in `_resolve_vendor`, the keyword argument, step 7 as one function, the state event and ID-3's production write refusal (ID-1 to ID-4, ID-7).
- **S14 (audit):** `engine/bodygraph/vendor_audit.py`, new: record, sink, actor, clock and correlation seams (IF-2, ID-4 to ID-6, EC-7, N4).
- **S08:** the band override in `_resolve_from_pair_file` (ID-9).
- **Tests:** the matrix, order, usage, audit and band tests; the ID-8 environment and invocation changes.
- **ID-10:** two classifier registry entries.
- **Documents:** `docs/CLI_commands.md` — the synopsis, the production-gate sentence with the sink key, and the band sentence.
- **Release:** the same-version refresh and every family it regenerates, by owners only.
- **Record:** the PR result record under `docs/ephemeral/`.

Out of scope (instruction §7):
- no change to `hdctl showcompat`, the conjunction paths or any HTTP route, and no vendor path on Reader, Aux or any HTTP surface;
- no public contract, payload, flag or transport change, and no change to existing stdout or stderr bytes, retry or timeout pins, route selection, credential handling or non-production write behavior;
- no version bump or admission-constant change;
- no canon edit, PF10 addendum, `schemas/` file, evidence family or acceptance token;
- no live vendor, production or database call, no real credential, no production configuration change and no audit sink file in the repository;
- no `AGENTS.md`, `README.md`, `CHANGELOG.md` or `.env.example` edit;
- no skipped, disabled, `xfail` or quarantined test;
- OBS-W4-1 to OBS-W4-4 and OBS-P4-1 to OBS-P4-7 are recorded, not fixed.

## 6. Design

### 6.1 ID-1 — CLI steps 1 and 2 (`engine/cli/main.py`, member)

**Option.** `bg.add_argument("--allow-prod-vendor", dest="allow_prod_vendor", metavar="AUTHORIZATION_REF", help=…)` on the `bg:resolve` parser only:
- no short spelling, alias, negated form, environment-variable form or default (§7.1.11a);
- `hdctl bg:resolve --help` lists it;
- the top-level help is unchanged, so `artifacts/cli/help/hdctl_help.txt` and the CLI conformance family stay byte-unchanged.

**Pre-scan** (`_allow_prod_vendor_usage_error(argv)`):
- **Where.** Called in `cli()` after the existing `--version` handling and before argparse. It counts every occurrence in the whole `argv` of the exact token `--allow-prod-vendor`, whose value is the next token, and of `--allow-prod-vendor=VALUE`.
- **Order of checks:**
  1. **Command.** The command is the first token that does not start with `-`; the top-level parser takes no value options. The option must follow a `bg:resolve` command, otherwise `COMMAND` (F-1).
  2. **Duplicate.** Two or more occurrences, in either spelling, give `DUPLICATE`.
  3. **Value.** A missing, empty or pattern-invalid value gives `VALUE`. The test is `is_valid_authorization_ref`: `re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")`.
- **Output.** On any of them `cli()` writes the line and a LF to stderr and returns 64. Stdout stays empty and the resolver is never reached.

**Step 2** (`bg_resolve`):
- If `args.allow_prod_vendor` is set and `args.source != "vendor"` (`db`, `auto` or the default `auto`), the handler raises `CliError(SOURCE, exit_code=64)`, whose code `cli()` prints.
- `MISSING_VENDOR_INPUT` (exit 64) keeps its place. It applies only to `--source vendor`, so it and step 2 never both apply.
- **Fixed order:** pre-scan, then argparse's own errors on other options, then step 2, then `MISSING_VENDOR_INPUT`, then the resolver. All come before step 3.

**Usage lines** (PD-2; each ends with one LF, names the option and never contains the value):

| Key | Text |
| :- | :- |
| `COMMAND` | `hdctl: --allow-prod-vendor is accepted only by bg:resolve --source vendor` |
| `DUPLICATE` | `hdctl bg:resolve: --allow-prod-vendor may be given only once` |
| `VALUE` | `hdctl bg:resolve: --allow-prod-vendor requires one AUTHORIZATION_REF of 1 to 128 characters matching ^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$` |
| `SOURCE` | `hdctl bg:resolve: --allow-prod-vendor is accepted only with --source vendor` |

**Hand-over.** `resolve_bodygraph(..., authorization_ref=args.allow_prod_vendor)`. `bg_resolve` keeps emitting only through `emitter.emit_public` (ID-7).

### 6.2 ID-1 — the seven-step order (`engine/bodygraph/resolver.py`, member)

**`resolve_bodygraph`** gains `authorization_ref: str | None = None`; `None` means absent (PD-3). A non-`None` reference that fails `is_valid_authorization_ref`, or comes with a source other than `vendor`, is refused before the rails with `PROVIDER_PROD_OVERRIDE_INVALID`. It performs zero I/O and writes no event (PD-4). `_resolve_vendor` gains the same keyword with the same default; the existing tests that call it directly are unaffected.

**`_resolve_vendor`, in order:**
1. **Step 3.** The existing `PROVIDER_REFUSED` and `PROVIDER_NETWORK_BLOCKED` blocks, byte for byte unchanged.
2. **Unchanged in place.** `_vendor_config_env(env)` and the `database_env` construction (pure, no I/O).
3. **Step 4.** `classify_vendor_environment(vendor_env)` (§6.3).
4. **Step 5.** The matrix (§6.4).
5. **Step 6.** The actor, the sink and the durable `allowed` event (§6.6, §6.7).
6. **Step 7.** `_resolve_vendor_route(...)`: the former body from `_classify_env_route_policy` onward, moved into one function without change except the `gate` hooks below, followed by the state event (§6.4 (e)).

`_resolve_vendor_route` runs the route policy and base-URL classification, input resolution, identity, the write-intent and write guards, client construction and fetch, in today's order. With a gate (an allowed production override) it also:
- records `route_family` and `resource_path` once route classification succeeds;
- applies ID-3 (§6.5);
- marks the fetch as entered (PD-12).

Without a gate (every non-production path) it is the former body, unchanged.

| Step | Where | Refusal | Exit | Stdout | Stderr | Event | Zero-outbound proof |
| :- | :- | :- | :- | :- | :- | :- | :- |
| O-1 parse | `cli()` pre-scan; argparse | usage `COMMAND`, `DUPLICATE`, `VALUE` | 64 | empty | one line, no value | none (§7.1.11f second sentence) | resolver patched to fail; the I/O guards (§6.9); `test_o1_*`, CLI usage tests |
| O-2 source | `bg_resolve` | usage `SOURCE` | 64 | empty | one line | none | as O-1; `test_o2_*` |
| O-3 rails | `_resolve_vendor` | existing `PROVIDER_REFUSED`, `PROVIDER_NETWORK_BLOCKED` | 1 | existing envelope bytes | empty | none | classification patched to fail; `test_o3_*`, M-1, M-2 |
| O-4 environment | `classify_vendor_environment` | `PROVIDER_CONFIG_INVALID` | 1 | envelope, `error.details` `{"outbound_attempted": false}` | empty | none | route policy patched to fail; `test_o4_*` |
| O-5 matrix | `_resolve_vendor` | `PROVIDER_PROD_OVERRIDE_REQUIRED` (M-3), `PROVIDER_PROD_OVERRIDE_INVALID` (M-8) | 1 | envelope with `outbound_attempted` false | empty | M-3: one `refused` event when actor and sink are available; M-8: none | actor and event seams patched to fail for M-8; `test_o5_*` |
| O-6 actor and event | `_resolve_vendor` | `PROVIDER_AUDIT_UNAVAILABLE` | 1 | envelope with `outbound_attempted` false | empty | none on refusal; otherwise one durable `allowed` event before step 7 | the `allowed` line is observed from inside step 7's first call; `test_o6_*` |
| O-7 existing gates | `_resolve_vendor_route` | existing step-7 codes; ID-3 `PROVIDER_WRITE_UNSUPPORTED` | 1 or 0 | existing step-7 envelope bytes | empty | one state event: `refused`, `failed` or `completed` | the I/O guards on every pre-fetch refusal; exactly one fake fetch on success; `test_o7_*` |

**Why the steps are ordered as they are.**
- No client construction, credential read, DNS, socket or HTTP happens before step 7 on any path.
- On the CLI, every policy refusal prints its envelope on stdout with exit 1 and an empty stderr, as `bg:resolve` already does (OBS-W4-2).
- Matrix row 1 says "any" flag, but steps 1 and 2 come before step 3. So with closed rails, a malformed or duplicated flag is still a usage error (exit 64). This reading follows canon's own §7.1.11d order and ID-1 ("All of them come before step 3"); it is not a conflict.

### 6.3 ID-2 — environment classification (step 4)

`classify_vendor_environment(view, process=None) -> VendorEnvironment(label, production_like)` implements §7.1.11b in one function:
- **Normalize.** Trim ASCII whitespace (`" \t\n\r\x0b\x0c"`) and lowercase; blank counts as absent.
- **Conflict.** Nonblank `APP_ENV` and `ENGINE_ENV` must be equal.
- **Choose.** Use `APP_ENV`, else `ENGINE_ENV`.
- **Classify.** Production-like is `{prod, production, live}`; non-production is `{dev, test, local, stage, staging}`. Absent, unknown or conflicting gives `PROVIDER_CONFIG_INVALID` with the fixed message "vendor environment classification requires APP_ENV or ENGINE_ENV to name one recognized environment" and `details: {"outbound_attempted": false}`. The value is never echoed.

**The view rule (PD-5):**
1. *view* is the merged vendor configuration view `_vendor_config_env(env)`: the process environment overlaid by the caller's mapping. For the CLI it equals the process environment for both keys, because `_resolver_env()` passes the process `APP_ENV` and the merged view takes `ENGINE_ENV` from the process.
2. Classify *view* by the rule above. If it is production-like, the label is *view*'s.
3. If *view* classifies as non-production, look at the process environment: if its `APP_ENV`, and then its `ENGINE_ENV`, normalizes to a production-like value, the result is production-like with that label. A caller's mapping never downgrades a production-like process environment.
4. A process value that is unknown, blank or non-production changes nothing. This is the same fail-safe direction as the v2 write guard, which reads both views (`or` semantics).
5. A conflict inside *view* is `PROVIDER_CONFIG_INVALID`, whatever the process holds.

**Effects.**
- Every open-rails `--source vendor` invocation is classified. An unset or unknown environment now refuses where it proceeded before (F-3, F-4, F-6).
- The v2 write guard's own reading is unchanged as an additional check. The `ENGINE_ENV` alias applies to this gate only.

### 6.4 ID-4 — the matrix (step 5), events and outcomes

| Row | Environment | Rails | Flag | Code | Exit | Stdout | Events | Zero outbound |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| M-1 | any recognized | `SAFE_MODE` closed | absent or valid (malformed or duplicate: O-1 first) | existing `PROVIDER_REFUSED` | 1 | existing bytes | none | I/O guards; `test_m1_*` (5 environments × 2 flag states) |
| M-2 | any recognized | network closed | absent or valid | existing `PROVIDER_NETWORK_BLOCKED` | 1 | existing bytes | none | I/O guards; `test_m2_*` |
| M-3 | `prod`, `production`, `live` | open | absent | `PROVIDER_PROD_OVERRIDE_REQUIRED` | 1 | envelope, `outbound_attempted` false | one `refused` (`authorization_ref` null, `error_code` `PROVIDER_PROD_OVERRIDE_REQUIRED`, `outbound_attempted` false, route fields null) if actor and sink are available; else none, same result | I/O guards; `test_m3_*` (5 spellings × dry run and write; unwritable sink; unavailable actor) |
| M-4 | production-like | open | malformed or duplicated | CLI usage (O-1) | 64 | empty | none | resolver never reached; CLI usage tests |
| M-5 | production-like | open | valid; actor or sink unavailable | `PROVIDER_AUDIT_UNAVAILABLE` | 1 | envelope, `outbound_attempted` false | none | I/O guards; `test_m5_*` |
| M-6 | production-like | open | valid and auditable | step 7 decides | 0 or 1 | existing step-7 bytes | `allowed` (pre-I/O, durable), then the state event | exactly one fake fetch on success; `test_m6_*` (v2 and legacy) |
| M-7 | recognized non-production | open | absent | current behavior | as today | as today | none | one fake fetch; `test_m7_*` (6 spellings) |
| M-8 | recognized non-production | open | present | `PROVIDER_PROD_OVERRIDE_INVALID` | 1 | envelope, `outbound_attempted` false | none | I/O guards; `test_m8_*` |

**(a) Code precedence follows the row.**
- Flag absent: row 3, even when its event cannot persist.
- A valid flag with no actor or sink: row 5.
- A non-production environment with a flag: row 8.

**(b) Events** are written only for production-like invocations that reach step 5. None for:
- steps 1 and 2;
- closed rails;
- step 4;
- non-production invocations, `PROVIDER_PROD_OVERRIDE_INVALID` included.

**(c) The row-3 event** is written best-effort; it never changes the result.

**(d) The `allowed` event.** It is written, flushed and `fsync`ed before step 7 starts. It carries `route_family` and `resource_path` null, `error_code` null and `outbound_attempted` false. Its failure is `PROVIDER_AUDIT_UNAVAILABLE`, and the call stops.

**(e) The state event** is one event after step 7, with the same `correlation_id`:

| Outcome | When | `outbound_attempted` |
| :- | :- | :- |
| `completed` | success | true |
| `failed` | a typed error after the fetch was entered, with its code | true |
| `refused` | a step-7 refusal before the fetch, with its code | false |

- Route fields carry the labels route classification produced (`recommended_v2_chart`/`charts` or `legacy_bodygraph`/`bodygraphs`), or null if classification did not complete.
- An unexpected exception in step 7 appends `failed` or `refused` with `error_code` null, then propagates (PD-13).
- A failure to append the state event changes nothing and prints nothing.

**(f)** §7.1.11f's "invalid" has no separately reachable case: a syntactically invalid value stops at step 1.

### 6.5 ID-3 — the production override is read-only

With a gate (production-like, valid flag, auditable), every write path refuses `PROVIDER_WRITE_UNSUPPORTED` before database construction and before vendor I/O. `--upsert` is refused as well, with or without `--dry-run` (PD-10).

**v2 mapped-cache path** (`_resolve_vendor_v2_chart`, new keyword `override_gate=None`):
- The existing first guard (no `--dry-run` and no `--upsert` → "v2 chart-backed mapped-cache persistence requires explicit upsert intent") is unchanged and still comes first.
- The production guard becomes `if (not dry_run or (override_gate is not None and upsert)) and production_like`, where `production_like` is the existing two-view reading or `True` when a gate is present. It keeps its existing message, "mapped-cache persistence is refused in production-like environments".
- Without a gate (`_acquire_dry_run`, showcompat, conjunction and every non-production call) the condition reduces to today's.

**Legacy v1 path** (`_resolve_vendor_route`):
- With a gate and (`upsert` or not `dry_run`), the path refuses `PROVIDER_WRITE_UNSUPPORTED` "BodyGraph persistence is refused in production-like environments" before `ingest_vendor_bodygraph`. The message has no details, matching the v2 step-7 refusal.
- With a gate and a plain dry run, it constructs the client exactly as `ingest_vendor_bodygraph` would (`HdApiClient.from_env(log_path=RETRY_LOG, env=_client_config_env(database_env))`). It passes it wrapped in `_AttemptTrackingClient` (PD-11). With `dry_run=True`, ingest builds no database target, and its own rails check cannot fire after step 3 has passed on the same view, so the order of observable steps is unchanged.
- Without a gate the call is today's, byte for byte.

**Unchanged:** a production dry run that contacts the vendor still needs the flag (M-3); non-production write behavior; retry and timeout pins.

### 6.6 ID-5 — the actor principal (N4)

`vendor_audit.resolve_actor_principal()`:
- **Source.** `pwd.getpwuid(os.geteuid()).pw_name`: the process's own credentials resolved through the system user database. Never `USER`, `LOGNAME`, `LNAME`, `USERNAME` or any other caller-settable value, a CLI option or the reference.
- **Unavailable.** A failed lookup (`KeyError`, `ImportError`, `OSError`) raises `AuditUnavailable`. So does a name that sanitizes to the empty string.
- **UID without a name** (PD-6). A numeric UID with no account name is **not** a stable identity: any container can run under an arbitrary UID, so the number does not attribute the act to a person. It refuses with `PROVIDER_AUDIT_UNAVAILABLE`.
- **Sanitized** like every field (§6.7).

Whether the Live QA venue yields a stable authenticated human principal is the QA Plan's question (Plan R-3; review v1.0 N4).

### 6.7 ID-6 — the audit record and sink (`engine/bodygraph/vendor_audit.py`, new, not a member)

**Constants:**
- `VENDOR_PROD_OVERRIDE_AUDIT_SCHEMA_VERSION = "vendor_prod_override.v1"` (PD-8);
- `VENDOR_PROD_OVERRIDE_EVENT = "vendor_prod_override"`;
- `VENDOR_OVERRIDE_AUDIT_PATH_KEY = "HDE_VENDOR_OVERRIDE_AUDIT_PATH"` (PD-7);
- `DEFAULT_AUDIT_SUBPATH = glow-hdengine/vendor_prod_override.jsonl`;
- `AUDIT_FIELDS`: the 16 keys of IF-2.

No `schemas/` file.

**Seams** (module-level functions, replaced by tests with `monkeypatch`):

| Seam | Behavior |
| :- | :- |
| `utc_now()` | the clock (OBS-W4-4) |
| `new_correlation_id()` | `str(uuid.uuid4())`, never from input |
| `resolve_actor_principal()` | §6.6 |
| `resolve_sink_path(env)` | below |
| `build_event(...)` | builds one record |
| `append_event(sink, event)` | writes one record |

**Sink path** (PD-7), read from the merged vendor view:
1. A nonblank `HDE_VENDOR_OVERRIDE_AUDIT_PATH`.
2. Otherwise `$XDG_STATE_HOME/glow-hdengine/vendor_prod_override.jsonl`, when `XDG_STATE_HOME` is nonblank and absolute.
3. Otherwise `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`, with `~` from `os.path.expanduser` (`HOME`, else the user database). An unresolvable home is unavailable.

The result must be absolute; it is resolved with `os.path.realpath`. A path equal to or inside the repository checkout (`Path(vendor_audit.__file__).resolve().parents[2]`) is unavailable.

**Writing** (PD-9):
- `mkdir(mode=0o700, parents=True, exist_ok=True)` for the parent;
- `os.open(O_WRONLY | O_APPEND | O_CREAT | O_CLOEXEC, 0o600)`;
- the opened file must be a regular file (`fstat`);
- write `sercanon(event)` (UTF-8, sorted keys, compact, one LF), loop until every byte is written, then `os.fsync` and close.

Any `OSError`, or a non-regular file, raises `AuditUnavailable`. An existing file's permissions are not changed.

**Fields.**
- `schema_version`, `event`, `command` (`bg:resolve`) and `source` (`vendor`) are constants.
- `occurred_at` is `utc_now()` formatted as `%Y-%m-%dT%H:%M:%S.%fZ`.
- `correlation_id`, `actor_principal`, `authorization_ref` (or null) and `environment` (the normalized production label).
- `safe_mode_open` and `network_open` are true. Events exist only after step 3 has passed.
- `route_family` and `resource_path` (labels or null), `outcome` (one of the four; anything else is `ValueError`), `error_code` (or null) and `outbound_attempted` (boolean).

**Sanitization** (PD-14). Every string field keeps printable ASCII (`" "` to `"~"`) and replaces every other character with `?`, so no CR, LF, other control byte, Unicode line separator or delimiter survives. JSON escaping handles quotes and backslashes.

**Never written.** Nothing from §7.1.11f's exclusion list, or from any input: no subject, birth field, location, URL, header, key, database identifier or raw provider message.

Tests and every tool run by this unit use a temporary sink; the repository gains no sink file.

### 6.8 ID-7 — output bytes and redaction

- **Existing envelopes** stay byte-identical: closed-rails refusals, step-7 refusals and success envelopes, in every environment. The EPIC037 generator's embedded closed-rails envelope is equal on `main` and the prototype (F-5).
- **New refusals** use the existing shape (`status`, `error` with `code`, a fixed `message` and `details`, `resolver`), exit 1. They carry `outbound_attempted: false` at one place, `error.details.outbound_attempted` (PD-15): `PROVIDER_CONFIG_INVALID` from step 4, `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` and `PROVIDER_AUDIT_UNAVAILABLE`. Their `resolver` object is the existing snapshot plus `resolved_source` (no route policy, which is step 7's).
- **Step-7 refusals,** ID-3's included, keep the step-7 convention (no `details` for the write refusals). Their zero outbound attempt is recorded in the state event.
- **Never emitted:** the reference, actor, correlation ID, sink path, timestamp and override state never appear on stdout or stderr, in an exception message or in a log. Proof: `test_record_and_streams_carry_no_subject_url_or_secret` and the usage tests' searches.
- **Determinism:** two-run identity of the new refusal (`test_production_like_cli_without_flag_emits_the_override_refusal`).
- **Emitter:** `emitter.emit_public` only. `emitter_symbol_proof.py` output is byte-identical to the governed proof.

### 6.9 ID-8 — existing tests and evidence tools

The rule: a scenario that asserted a later guard keeps asserting it, by supplying a valid reference, a test actor and a temporary sink. A test that relied on an ambient `APP_ENV` may set it. By the same reading, a test whose explicit `APP_ENV` would conflict with a leaked ambient `ENGINE_ENV` may remove that `ENGINE_ENV` (F-13; PD-19): this is environment setup only. Nothing else changes, and no expected code is weakened or assertion removed.

| Path | Change |
| :- | :- |
| `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` | a helper `production_override(monkeypatch, tmp_path)` (patches `vendor_audit.resolve_actor_principal` to `"test-operator"`; returns the reference `HDE-CRD-0002-TEST-1` and the sink mapping `{"HDE_VENDOR_OVERRIDE_AUDIT_PATH": tmp_path/…}`); `test_production_like_refuses_before_vendor_and_db` (3 parameters) and `test_process_production_environment_cannot_be_overridden_for_database_write` use it; assertions unchanged (`PROVIDER_WRITE_UNSUPPORTED`, no vendor or DB construction) |
| `tools/evidence/generate_v2_mapped_cache_evidence.py` | only the `production` scenario's invocation: inside `tempfile.TemporaryDirectory()` and `patch("engine.bodygraph.vendor_audit.resolve_actor_principal", lambda: "fixture-operator")`, the mapping gains the sink key and the call gains `authorization_ref="HDE-CRD-0002-FIXTURE"`. `PREDICATE_KEYS`, every output byte and the hermetic guard are unchanged; `--check` exits 0 (observed) |
| `tests/bodygraph/test_resolver_vendor.py` | the two existing open-rails mappings gain `"APP_ENV": "test"` (F-3); an autouse fixture removes the ambient `ENGINE_ENV` (F-13) |
| `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` (also) | an autouse fixture removes the ambient `ENGINE_ENV` (F-13); no test body changes |

**Found and not changed:**
- The six route-policy tests of F-4. They pass wherever `APP_ENV=dev` is set, which is every lane and the changed-tests step, and neither the sanity pipeline nor the attestation runs them. A change would be outside §6 and is not needed (OBS-P4-2).
- `generate_hde_epic037_bg_resolve.py`, which relies on the ambient `APP_ENV=dev` (F-6).

The prototype sweep found no other affected test or tool (§4.3). No governed or frozen output changes.

### 6.10 ID-9 — Aux preview band (S08)

In `_resolve_from_pair_file`, after the category and its band are read from the file and validated (`INVALID_COMPAT_INPUT`, `MISSING_COMPAT_CATEGORY` unchanged), `if args.band: band = args.band`. `--band` is limited to `AUX_BANDS` by argparse.

Unchanged:
- category selection;
- perspective;
- the file's `release_id`;
- stdout emission only with `--show-narrative`;
- the `--admin-out` sidecar, which names the flagged band's key;
- the non-pair-file path.

The suppressed-key line of ID-9 holds through the unchanged emitter (F-8).

### 6.11 ID-10 — classifier registration

In `ci/checks/classify_ci_changes.py`, exactly two entries, each with a one-line comment naming HDE-CRD-0002 WU-PR-04:
- `_PRODUCT_TEST_OWNER_PATHS["engine/bodygraph/vendor_audit.py"] = ("tests/bodygraph/test_vendor_prod_override.py",)`
- `_EVIDENCE_GENERATOR_TEST_OWNERS["tools/evidence/generate_v2_mapped_cache_evidence.py"] = ("tests/evidence/test_v2_mapped_cache_evidence.py",)`

No function changes. Effects:
- The two paths classify. `vendor_audit.py` selects product and release and its owner; the generator selects evidence and release and its owner.
- The new test file is a registered owner, so it is a full-validation target and satisfies the WU-PR-01 coverage pin with no `ci.yml` change.
- The classifier is a full-validation path, so the PR selects all seven lanes.
- Every pin in `tests/evidence/test_rails_ci_workflow_integration.py` stays true (138 passed on the prototype), and none needs adding.

The classifier gap this leaves for later resolver-only or CLI-only changes is OBS-P4-1.

### 6.12 Documents (`docs/CLI_commands.md`)

- The `bg:resolve` synopsis gains `[--allow-prod-vendor <AUTHORIZATION_REF>]`.
- One sub-bullet, "Production gate (HDE-CLI-API-Vendor-Ref §7.1.11)", states:
  - the step-4 classification and `PROVIDER_CONFIG_INVALID`;
  - the flag in `prod`, `production` or `live` and `PROVIDER_PROD_OVERRIDE_REQUIRED`;
  - `PROVIDER_PROD_OVERRIDE_INVALID` in non-production;
  - the sink key, the default path and `PROVIDER_AUDIT_UNAVAILABLE`;
  - read-only (`--upsert` and every write refuse `PROVIDER_WRITE_UNSUPPORTED`);
  - the usage errors (exit 64).
- One `aux-preview` sub-bullet states that an explicit `--band` replaces the file's band for the selected category, and that the category must still be present in the file.

The exact text is in the companion diff. No other document changes (§17).

### 6.13 Release refresh and convergence (Plan v1.1 §10; addenda 2.6 RP-2 and 2.7 AD-5; instruction §5.9)

All steps run under closed rails, with vendor and database keys unset, in the working tree of the implementation branch after the member bytes are final and committed. Every check that can write tracked files then runs in a detached worktree. Steps 3 to 10 run twice; the second pass must reproduce the first byte for byte.

| Step | Commands (owner) | Notes |
| :- | :- | :- |
| 1 | member bytes final: `engine/cli/main.py`, `engine/bodygraph/resolver.py` (one final LF) | no updater run from here to the cut (LR-O3 (a)) |
| 2 | `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `python scripts/release_id_recompute.py --check-manifest-only`; the cutter again with `--check` | two manifest rows change; record the new `release_id` |
| 3 | admission one-liner (`load_active_mechanics_bundle()` → `release_id`, members, version); `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | expect `1.3.0`, 45, the new `release_id`; exit 0 |
| 3b | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; then `--check` | the step-3b order (addenda 2.6, 2.7); the catalog family is rewritten byte-identically (F-7) |
| 4 | `python tools/evidence/run_canonical_json_gate.py`; `--check-only` | |
| 5 | `python tools/evidence/update_evidence_index.py`; `--check` | first updater run after the cut |
| 6 | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | |
| 7 | A7 write and `--check` (byte-stable); `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, keys absent); set `FROZEN_OPEN_ABBA_SHA256` in that file to `sha256sum audit/gates/determinism/open_rails_abba.json` by one anchored replacement; `python tools/evidence/generate_conjunction_writer_evidence.py`; `python tools/evidence/generate_engine_core_evidence.py` | the open-rails digest supersedes `06611525…` |
| 8 | updater; `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check` | the `ci/checks/*.sh` are invoked by path (F-2); step-7 captures take the new label here (LR-O3 (b)) |
| 9 | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` (must end `summary:PASS`); the canonical run; `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check` | |
| 10 | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen families unchanged |
| 11 | `git grep -l -E 'd84d99e1|06611525'` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256` | expected: no hit; every hit is a defect to fix before publication. Also: the Mirror's labelled rows all carry the new label and the purity-report row has no `notes` (LR-O3 (c); addendum 2.6) |
| 12 | §10's tests and lanes; the attestation build and verify | |

**Restart rules.** A member byte change after step 2 restarts at step 2. An evidence-primary change restarts at step 3b (addenda 2.6 RP-2 and 2.7 AD-5).

**Expected changed set** (54 paths; observed in both rehearsals; PR-30 records its actual set):
- `catalog/manifest.json`;
- `tools/evidence/generate_open_rails_abba_proof.py` (`FROZEN_OPEN_ABBA_SHA256` only);
- 26 evidence primaries and their 26 path proofs:
  - **A7 success proofs:** `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`;
  - **config:** `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`;
  - **engine core:** `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`;
  - **F07 writer:** `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`;
  - **canonical JSON gate:** `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`;
  - **determinism and parity:** `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`;
  - **Index and Mirror:** `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.

**Rewritten byte-identically** (not in the diff):
- the catalog family: `artifacts/audit/ENDPOINTS_CATALOG.json`, both `.sha256` sidecars and their path proofs;
- `artifacts/proofs/endpoints_env_gate_proof.log`, `success_writers_errors.txt`;
- `artifacts/reader/endpoints_snapshot.json`;
- `artifacts/core/purity/purity_report.json`;
- the canonical sanity log.

## 7. Change set

### 7.1 Files edited by hand (the companion diff)

| Path | Change | Requirement |
| :- | :- | :- |
| `engine/cli/main.py` (member) | the option; the four usage lines; `_allow_prod_vendor_usage_error`; its call in `cli()`; step 2 and the hand-over in `bg_resolve`; the band override | S14 (ID-1), S08 (ID-9) |
| `engine/bodygraph/resolver.py` (member) | `AUTHORIZATION_REF_PATTERN`, `is_valid_authorization_ref`, `VendorEnvironment`, `classify_vendor_environment`, `_OverrideGate`, `_AttemptTrackingClient`, `_override_refusal`; the keyword on `resolve_bodygraph` and `_resolve_vendor`; steps 4 to 6; `_resolve_vendor_route` (the former step-7 body with the gate hooks); `_append_flag_absent_event`, `_append_state_event`; `override_gate` on `_resolve_vendor_v2_chart` | S14 (ID-1 to ID-4, ID-7) |
| `engine/bodygraph/vendor_audit.py` (new, 178 lines) | §6.7 | S14 (IF-2, ID-4 to ID-6, EC-7) |
| `tests/bodygraph/test_vendor_prod_override.py` (new, 488 lines, 96 cases) | M-1 to M-8, O-1 to O-7, the audit record and seams | S14 |
| `tests/cli/test_bg_resolve.py` (6 → 35 cases) | usage carrier (duplicate in three spelling pairs; 14 invalid values: empty in two forms, missing, space, tab, `\x01`, `\x7f`, `é`, `@`, `;`, leading `-`, leading `.`, LF, 129 characters; non-vendor sources; outside `bg:resolve`); valid values reach the resolver once; `MISSING_VENDOR_INPUT` kept; the CLI row-3 refusal with two-run identity | S14 |
| `tests/cli/test_aux_preview.py` (2 → 9 cases) | `--band` with `--pair-file` for all four bands, with the sidecar key; without `--band`; the unchanged refusals; no stdout without `--show-narrative` | S08 |
| `tests/bodygraph/test_resolver_vendor.py` (4 → 24 cases) | environment classification table (11 cases) and refusals (5); ID-3 on the legacy path (3); the unchanged non-production legacy write (1); `APP_ENV` in two existing mappings (F-3); the `ENGINE_ENV` fixture (F-13); imports at the top | S14, ID-8 |
| `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` (28 cases, unchanged count) | §6.9: the `production_override` helper, the two production-like tests, the `ENGINE_ENV` fixture | ID-8 |
| `tools/evidence/generate_v2_mapped_cache_evidence.py` | §6.9 | ID-8 |
| `ci/checks/classify_ci_changes.py` | two entries and comments (§6.11) | ID-10 |
| `docs/CLI_commands.md` | §6.12 | Plan "flag and band wording" |

### 7.2 Written only by owners

`catalog/manifest.json` (cutter); `FROZEN_OPEN_ABBA_SHA256` (step 7); every family of §6.13; the Index, Mirror, sentinels and path proofs (updater only).

### 7.3 Expected unchanged (a change is a finding, §14 RK-7)

- **Code:** `engine/bodygraph/vendor_client.py`, `engine/bodygraph/ingest.py`, `engine/compat/**`, `adapter/**`, `engine/http/**`, `engine/narratives/**`, `engine/presenter/**`, `engine/config/registry_loader.py`.
- **Tools and CI:** `tools/evidence/update_evidence_index.py`, `tools/evidence/generate_hde_epic037_bg_resolve.py`, `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`, `.github/workflows/ci.yml`, `ci/jobs/**`.
- **Other tests and scripts:** `tests/bodygraph/test_bg_resolve_route_policy.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `scripts/ops/admin_vendor_qa.py`.
- **Frozen and captured families:** `artifacts/vendor/**`, `artifacts/cli/**` (help, guards, install, showcompat), `artifacts/architecture/**`, `artifacts/identity/**`, `audit/ops/**`.
- **Documents:** `AGENTS.md`, `README.md`, `CHANGELOG.md`, `.env.example`.

## 8. Implementation sequence (PR-30)

1. **Recover.** Inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/HDE-CRD-0002-WU-PR-04-*` before creating anything (instruction §13).
2. **Branch** from current `main` (the session's designated branch). If `main` moved outside `docs/ephemeral/` and `docs/pfcanon/` since `9c82b62`, re-run §4.1's checks and `git apply --check` of the companion diff, and record any difference. A changed member or manifest on `main` is a new refresh base.
3. **Set up** Python 3.12 with CI's install, `ruby`, `bash` and `curl`; unset the vendor, database and GitHub keys; record versions.
4. **Apply §7.1** (the companion diff as a starting point) and re-read every hunk against §6.
5. **Pre-cut tests.** Run the changed-surface tests that do not need admission: `tests/bodygraph/test_vendor_prod_override.py`, `tests/bodygraph/test_resolver_vendor.py`, `tests/cli/test_bg_resolve.py`, `tests/cli/test_aux_preview.py`, `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`, `tests/evidence/test_v2_mapped_cache_evidence.py`. Run them once more with `APP_ENV` unset, and once with `tests/adapter/test_jsonschema.py` first in the same process (F-13). Run the negative controls NC-1 to NC-5 in a scratch copy.
6. **Source commit.** Freeze the member bytes and commit the source.
7. **Refresh.** Run §6.13 steps 2 to 11 and commit the convergence. Record each step's exit code, both passes, the byte-stability digest, the changed set and the sweep.
8. **Validate.** Run §10 in detached worktrees of the candidate commit.
9. **Record and publish.**
   - Write and read back the PR result record v1.0 (§12).
   - Commit coherently: source, convergence, record.
   - Push and open the PR with the template headings.
   - Record `PR_CANDIDATE_PUBLISHED` and hand off to PR-35.

## 9. Requirement → change → test map

| Requirement / acceptance item | Change | Proof |
| :- | :- | :- |
| S14 flag, order, matrix, carrier / (1) | §6.1–§6.4 | `test_vendor_prod_override.py` M-1 to M-8 and O-1 to O-7 under the I/O guards (`HdApiClient` construction, `DBAccess`, `urllib.request.Request` and `urlopen`, `socket.getaddrinfo`, `socket.socket` fail the test); `test_bg_resolve.py` usage tests (duplicate in both spellings, empty, missing, each invalid class, 129 characters, `db`, `auto`, default source); `ENGINE_ENV` alias and conflict (`test_o4_*`, `test_environment_classification*`); the production dry run without the flag (`test_production_dry_run_without_flag_refuses`, M-3 with `dry_run`); exactly one fake fetch on the allowed rows |
| S14 initiator and audit / (2) | §6.6, §6.7 | `test_record_has_exactly_the_if2_fields_and_canonical_lines`; `test_fields_are_sanitized_against_cr_lf_and_control_bytes`; `test_record_and_streams_carry_no_subject_url_or_secret` (reference, actor, sink path absent from stdout; user, birth inputs, base URL, keys, `Bearer` absent from the sink); unwritable sink and unavailable actor (M-5, `test_unwritable_sink_is_unavailable`); the row-3 event (M-3); the state events (`test_m6_*`, `test_o6_*`, `test_o7_*`); `test_actor_comes_from_the_effective_uid_not_the_environment`; `test_sink_path_rule`; `test_sink_is_created_owner_only_and_appended` |
| S14 rails first, no public path, read-only / (3) | §6.2, §6.5; §5.3 call sites unchanged | M-1 and M-2 with existing bytes; `test_o3_*`; `test_o7_production_override_is_read_only_on_both_write_paths` (6 cases); `test_production_override_refuses_legacy_writes_before_ingest`; the diff touches no `adapter/**`, `engine/http/**` or `engine/compat/**` path; `_acquire_dry_run` unchanged (`tests/bodygraph/test_resolve_compat_chart.py` passes) |
| S14 live behavior | — | the Live QA vendor call (QA Plan), not this unit |
| S08 / (4) | §6.10 | `test_aux_preview_pair_file_band_flag_selects_the_flagged_band` (4 bands, sidecar key); `…_without_band_flag_uses_the_file_band`; `…_keeps_category_refusals`; `…_without_show_narrative_emits_nothing` |
| Refresh / (5) | §6.13 | admission line; second-pass byte identity; recompute; seven lanes (ID-10); attestation |
| ID-8 | §6.9 | the two mapped-cache tests; `generate_v2_mapped_cache_evidence.py --check`; sanity `summary:PASS`; the attestation |
| ID-10 | §6.11 | classifier dry run on the PR's paths; `tests/evidence/test_rails_ci_workflow_integration.py` |
| ID-7 | §6.8 | M-1/M-2 byte assertions; `emitter_symbol_proof.py` byte equality; the EPIC037 equivalence (§10 item 7) |

## 10. Validation plan (PR-30, local)

Every run that can write tracked files runs in a detached worktree and ends with `git diff --exit-code` and an empty `git status --short --untracked-files=all`:
1. **Classifier.** Dry run on the PR's changed paths: all seven lanes; record the path and target counts.
2. **Changed-tests step** as CI runs it (the classifier's targets, in a detached worktree).
3. **Seven lanes.** The lanes' commands as `.github/workflows/ci.yml` writes them: product, compat, db, rails, evidence, qa and release. The release lane includes the attestation build and verify into an external empty directory with `--require-clean`. The attestation is mandatory before publication: it is the only local run that exercises the no-`APP_ENV` child environment (F-3).
4. **Full sweep.** The full `tests/` sweep with `ruby`, `bash` and `curl` on `PATH`. The refresh rewrites the Index and Mirror, so this covers every updater consumer (LR-O2). It is also the only run in which `tests/adapter/test_jsonschema.py`'s leaked `ENGINE_ENV` reaches the vendor-path tests (F-13). Record pass, skip and xfail counts.
5. **Generator checks** under the closed-rails profile: `generate_v2_mapped_cache_evidence.py --check` and `generate_bodygraph_policy_proofs.py --check`.
6. **CLI checks.** `ci/checks/check_cli_help.sh`; `tests/cli/test_serializer_guards.py`; `emitter_symbol_proof.py` output compared with `artifacts/cli/guards/emitter_symbol_proof.txt`.
7. **EPIC037 equivalence** (replaces instruction §10's `generate_hde_epic037_bg_resolve.py --check`, which fails on `main`, F-5). Compute `build_outputs()` on `main` and on the candidate. Assert that every body is equal with `inspected_internal_loci` and `input_references` set aside, and that only the two member digests differ. Record the pre-existing `--check` failure; do not run it in write mode.
8. **Convergence checks** of §6.13 steps 4 to 10 and the step-11 sweep.
9. **Negative controls** NC-1 to NC-5 (§4.3); each must fail.
10. **Hermeticity.** The four changed test files and the mapped-cache file pass with `APP_ENV` unset, and with `tests/adapter/test_jsonschema.py` first in one process. Record F-4's six route-policy tests as known ambient dependants (informative).

## 11. PR split, merge dependencies and pull request description

**No split: one PR for the whole unit** (Plan v1.1 §7). The member edits, the cut and the convergence must land together, so that admission and the updater hold at every commit of `main`.

**Merge dependency:** none open. WU-PR-01, WU-PR-02 and WU-PR-03 have landed. WU-PR-05 and WU-PR-08 depend on this PR's `release_id` (instruction §8, contract F-1).

**PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules:
- **Why:** instruction §4; the Specification rows.
- **What changed:** grouped by path.
- **Checks run:** each with its counts.
- **Not in this PR:** §17's stale documents and observations, with owners.
- **What merging does:** what becomes current on `main`, and that it establishes no QA, acceptance or closure.

## 12. Acceptance and evidence obligations (PR result record v1.0)

`docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.0.md` names:
- **Checks.** Each check actually run, with counts.
- **Release.** The refreshed `release_id`, every regenerated family with paths, both passes, the byte-stability digest and the step-11 sweep.
- **Tables.** The matrix and order tables of §6.2 and §6.4, with the test results.
- **Override contract** (instruction §8, contract F-2):
  - the sink key `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and its default rule;
  - the actor rule, including the UID-only refusal;
  - the event shapes and outcomes;
  - the refusal codes and the `error.details.outbound_attempted` placement;
  - the exact command form `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF> …`.
- **Bounded changes.** The ID-8 list (§6.9), the two ID-10 keys and the stale-document list (§17).
- **In-flight decisions.** PR-30's own, or `NONE`.
- **Nonclaims:**
  - the flag was not exercised live;
  - no QA verdict, acceptance, Ops, deployment, PF09 movement or closure;
  - no conformance claim beyond §7.1.11's implementation;
  - the DD-04 canon paragraph is not edited;
  - the EPIC036 and EPIC037 frozen captures stay stale as on `main` (F-5).

Plan v1.1's evidence obligations: the PR result record; no live call; no audit sink in the repository.

## 13. Security and migration constraints

**Migration and rollback.**
- Migration: none (no data or schema change).
- Rollback: Nathan's revert of the squash commit, followed by a same-version manifest refresh (Plan v1.1 §7, §14).

**Security.**
- **The gate only narrows.** No rail opens; the override is read-only (ID-3), `--upsert` included; no HTTP surface gains vendor access; showcompat and conjunction acquisition are unchanged (OBS-W4-1).
- **The reference** is validated, is not authentication and grants nothing by itself.
- **The actor** comes from the process's effective UID through the user database and is never caller-asserted. A UID without a name refuses.
- **The audit record** is keys-only, sanitized, owner-only (`0600`, parent `0700`) and outside the repository. The repository-path refusal enforces the last point.
- **Never emitted:** nothing in stdout, stderr, exceptions or logs carries the reference, actor, sink path or any secret. Tests and records hold no secret, token or key value; the fake keys in tests are fixed non-secret strings.
- **The refresh** opens no rail. The open-rails fixture proof runs in fixture mode with keys absent.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | A vendor-path test depends on the ambient environment: the attestation's no-`APP_ENV` child environment (F-3), or an `ENGINE_ENV` leaked by an earlier test in the same process (F-13) | the attestation build and verify and the full sweep are mandatory before publication (§10 items 3 and 4); a new dependant is fixed only under ID-8's rule inside §6, otherwise RK-7 |
| RK-2 | A member byte change after the cut | restart at step 2 |
| RK-3 | `argparse` keeps the last of repeated values silently, and echoes values in its own messages | the pre-scan over the whole `argv` (F-1); NC-5 |
| RK-4 | A frozen family changes | §10 items 6 to 8; any change is RK-7 |
| RK-5 | OBS-17: intermittent qa-lane failure of `tests/qa/test_generate_epic_close_pack.py` | recorded as OBS-17 on this PR, never "fixed" here |
| RK-6 | `ruby` absent on a runner | the contract-inventory test fails rather than skips; PR-35 records the hosted version if the log shows it (O-6) |
| RK-7 | A boundary trigger of instruction §14: a change outside §6, a governed output that cannot stay byte-identical, a need to gate showcompat or conjunction, a canon need for a registered audit schema, a frozen-family `--check` failure that `main` does not already have, or a reading of ID-1 to ID-9 that conflicts with canon | stop the affected work; `RESCOPE_REQUEST` through RS-20 (PR-30 records `PR_RETURN_PHASE`) |

**Recovery.**
- An interruption resumes in the same dedicated phase session from its last saved artifact.
- An ordinary defect in this plan returns to this PR-20 context as a new plan version.
- An instruction defect returns to the IA through PR-10.
- Abort is only Nathan's manual PR-50.

## 15. Decisions taken in this plan (within approved scope)

| ID | Decision (instruction §9.1 item) | Basis |
| :- | :- | :- |
| PD-1 | The pre-scan covers the whole `argv`, also refuses the option outside `bg:resolve`, and checks command, duplicate and value in that order | §7.1.11a ("accepted only by `hdctl bg:resolve --source vendor`"); ID-1 ("never echoes the value"); F-1 |
| PD-2 | **Usage-error text:** the four lines of §6.1 | §3.3 "Usage (exit 64). Print a short human synopsis"; §3.4 one LF; ID-1 |
| PD-3 | **Keyword name:** `authorization_ref`, default `None` (absent), on `resolve_bodygraph` and `_resolve_vendor` | §7.1.11a `AUTHORIZATION_REF`; IF-2 field name |
| PD-4 | **Malformed library reference:** `PROVIDER_PROD_OVERRIDE_INVALID`, also for a reference with a non-vendor source; before the rails; zero I/O; no event. No new code is invented | ID-1 "Library interface"; the step-1 analogue precedes step 3 (§7.1.11d); canon defines this code for an inapplicable override |
| PD-5 | **View rule:** classify the merged view per §7.1.11b; a production-like process `APP_ENV` or `ENGINE_ENV` wins over a non-production merged view; a conflict inside the merged view is `PROVIDER_CONFIG_INVALID` | ID-2 "No downgrade"; the v2 write guard's two-view reading; keeps the ID-8 test `test_process_production_environment_cannot_be_overridden_for_database_write` asserting its guard |
| PD-6 | **UID-only actor:** not a stable identity; refuses `PROVIDER_AUDIT_UNAVAILABLE` | §7.1.11e "If a stable authenticated actor identity is unavailable, refuse"; §7.1.11f "authenticated OS/control-plane principal" |
| PD-7 | **Key name and default path:** `HDE_VENDOR_OVERRIDE_AUDIT_PATH`; `$XDG_STATE_HOME/glow-hdengine/vendor_prod_override.jsonl`, else `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`; absolute; never inside the checkout | EC-7; ID-6; Glow Infrastructure §8.1 observation (`HDE_` names) |
| PD-8 | **Schema-version constant:** `VENDOR_PROD_OVERRIDE_AUDIT_SCHEMA_VERSION = "vendor_prod_override.v1"` | ID-6; no `schemas/` file |
| PD-9 | **Parent-directory rule:** create missing parents owner-only (`0700`); any failure, or a non-regular sink, is unavailable; existing permissions are not changed | ID-6 "Writing"; §7.1.11f "locally durable" |
| PD-10 | `--upsert` is refused in a production-like override, with or without `--dry-run` | §7.1.11d "does not authorize … production `--upsert`, any production database write"; HDE-CLI-API-Vendor-Ref §4.6 ("`--upsert` **must not** be used in prod"); ID-3 "read only" |
| PD-11 | The allowed production legacy path passes an attempt-tracking client constructed as ingest would construct it; the non-production call is unchanged | F-11; ID-4 (e) needs `refused` versus `failed`; `vendor_client.py` and `ingest.py` stay unchanged |
| PD-12 | `outbound_attempted` is true once the governed fetch is entered (conservative: it never under-reports an attempt) | F-9; §7.1.11f boolean field |
| PD-13 | An unexpected exception in step 7 appends a state event with `error_code` null, then propagates | §7.1.11f "A post-I/O completion event may … append a second state event"; the record should not go silent |
| PD-14 | Sanitization keeps printable ASCII only | §7.1.11f "Sanitize audit fields against CR/LF and delimiter injection"; ID-6 |
| PD-15 | **`outbound_attempted` placement:** `error.details.outbound_attempted` on the step-4 to step-6 refusals and the library refusal; step-7 refusals keep their existing bytes | IF-1; ID-7 ("one place"); `VendorError.as_payload` already carries `details` |
| PD-16 | Test placement: tables and audit in the new file (the `vendor_audit.py` owner); classification and the legacy write refusal also in `test_resolver_vendor.py`, which the resolver's owners and two rails jobs run | ID-10's smallest registration; OBS-P4-1 |
| PD-17 | The EPIC037 `--check` is replaced by the equivalence check of §10 item 7 | F-5 |
| PD-18 | The rehearsal `release_id` is not binding; PR-30 records its own | §4.3 |
| PD-19 | The two vendor-path test files that set `APP_ENV` in their mappings remove the ambient `ENGINE_ENV` with an autouse `monkeypatch.delenv` fixture. `tests/adapter/test_jsonschema.py`'s leak is recorded, not fixed | F-13; ID-8 "Test-environment setup" (environment setup only); the leaking file is outside instruction §6 |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | the IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- §6.1 to §6.8 apply HDE-CLI-API-Vendor-Ref §7.1.11 as written, within IF-1, IF-2 and EC-7.
- Matrix row 1's "any" and the step order are read together, as ID-1 binds (§6.2).
- PD-10 applies §7.1.11d's own words.
- PD-4 uses a code canon already defines.
- The view rule (PD-5) refines only what §7.1.11b leaves open: canon names one environment, and the repository has two views.

Coverage read for this plan: HDE-CLI-API-Vendor-Ref §3.1, §3.1.1, §3.3, §3.4, §4.5, §4.6, §7.1.10, §7.1.11 to §7.1.11f, §7.2.0; HDE Governance §9.1.1 and §9.1.2; Glow Infrastructure §8.1; HDE Users Guide §10.1, Recipes F and G, §16; PF10 addenda 2.1, 2.3, 2.5 to 2.8; a whole-canon search on `main` for `allow-prod-vendor`, `override flag`, `PROVIDER_PROD_OVERRIDE`, `PROVIDER_AUDIT_UNAVAILABLE` and `DD-04`.

## 17. Stale documents, observations and carried items (not in this PR)

**Stale documents** (this unit makes them stale and may not change them; instruction §9.5):

| Document | Statement | Owner |
| :- | :- | :- |
| HDE-CLI-API-Vendor-Ref §7.1.11 "Required-Now implementation gap (DD-04; held)" | the flag is not an available facility | Product Owner (canon doc-delta) |
| HDE-CLI-API-Vendor-Ref §7.2.0 "Contract and implementation posture" | lists "no production-vendor override flag or audit gate" among the material gaps | Product Owner (canon doc-delta; new in this plan) |
| HDE Users Guide §16 | "`--allow-prod-vendor` is absent from the inspected active CLI parser" | Product Owner (canon doc-delta) |
| HDE Users Guide §10.1 | "The band comes from that row; --band does not override it" (stale after S08) | Product Owner (canon doc-delta; new in this plan) |
| HDE Users Guide Recipe F | the open-rails dry-run command supplies no `APP_ENV`; after S14 an unset value refuses `PROVIDER_CONFIG_INVALID`, and a production-like one needs the flag | Product Owner (canon doc-delta; new in this plan) |
| Glow Infrastructure §8 config keys | the new key `HDE_VENDOR_OVERRIDE_AUDIT_PATH` | Product Owner (canon doc-delta) |
| §7.1.11f "governed clock boundary" | undefined (OBS-W4-4) | Product Owner (canon doc-delta) |
| `README.md`, `AGENTS.md` mentions of the override and the CLI | WU-DOC-01 to state the shipped flag, the sink key and the band behavior | WU-DOC-01 |
| repository runbooks with `bg:resolve --source vendor` commands (for example `docs/RUN.md` lines 65–66 at `9c82b62`) | to state an explicit recognized `APP_ENV` | WU-DOC-01 |

`audit/docdeltas/hde-epic040_doc_deltas.md` DD-04, `audit/qa/hde-epic040/00_meta/doc_deltas.md` DD-04 and HDE Phased Epics' DD-04 row stay as they are (historical).

**New observations** (owner: the IA, who routes them):

| ID | Observation | Suggested route |
| :- | :- | :- |
| OBS-P4-1 | A change to `engine/bodygraph/resolver.py` or `engine/cli/main.py` alone does not select `tests/bodygraph/test_vendor_prod_override.py`, and `engine/cli/main.py` does not select `tests/cli/test_bg_resolve.py` or `tests/cli/test_aux_preview.py`. The smallest registration (ID-10) leaves these targets to full validation. PD-16 keeps a classification and write-refusal subset in a resolver owner | WU-PR-06 (pre-push check) or a later classifier unit |
| OBS-P4-2 | Six route-policy tests depend on an ambient `APP_ENV` (F-4) | IA; a later unit that touches that file |
| OBS-P4-3 | Instruction v1.0 §10 lists `generate_hde_epic037_bg_resolve.py --check`, which fails on `main` (F-5). Its §5.8 effect row ("none if ID-2 and ID-7 hold") holds for the bodies, not for the source-digest fields. The EPIC036 tool's `--check` fails the same way | IA (instruction lesson, no correction needed for this unit); Product Owner (whether these frozen captures should be refreshed or retired) |
| OBS-P4-4 | `scripts/ops/admin_vendor_qa.py` is already non-functional (missing `--user`) and would also need the flag and drop `--upsert` in production (F-10) | Product Owner |
| OBS-P4-5 | The attestation's isolated child environment has no `APP_ENV` (F-3). Any later unit that adds an open-rails vendor-path test to a rails job, or to another sanity-run test, must set `APP_ENV` in that test | IA, for the WU-PR-05 and WU-PR-08 instructions |
| OBS-P4-6 | Through `aux-preview` no band reaches a governed suppressed key (F-8), so `aux_suppressed_empty` is not reachable from that command today | IA (observation only) |
| OBS-P4-7 | `tests/adapter/test_jsonschema.py` leaks `ENGINE_ENV` and a fixture `ENGINE_SERVICE_TOKEN` into `os.environ` for the rest of the pytest process (F-13). After S14, any later test that sets `APP_ENV` to anything but the leaked value and reaches the vendor gate without removing `ENGINE_ENV` refuses `PROVIDER_CONFIG_INVALID`. A two-line `monkeypatch` change would remove the leak | IA (route to the file's owner or a later unit; outside this unit's §6) |

**Carried** (instruction §15):
- OBS-W4-1 and OBS-W4-3 are named S19 inputs for WU-PR-05; OBS-W4-2 and OBS-W4-4 go to the Product Owner.
- LR-O1 and LR-O3 are applied here (§6.13).
- LR-O2 is not triggered (the updater does not change), but its consumers run in the full sweep.
- OBS-17 is RK-5; O-6 is RK-6.
- AD-4's gaps, OBS-P3-3, OBS-P3-14, OBS-P3-17 and LR3-O2's wording go to the WU-PR-05 instruction.
- LR3-O1, LR3-O4 and LR3-O5 stay with their owners.
- AQ-1 gates WU-PR-07 only.

## 18. Route-policy statement (instruction §9.6; Plan Templates "`bg:resolve --source vendor` route-policy posture")

The route policy is unchanged:
- configured `v2` bases are v2 chart-backed (`charts`, the deterministic `ChartResult` adapter);
- every other base takes the explicit legacy BodyGraph fallback (`bodygraphs`), including the unversioned and nonterminal bases of OBS-W4-3.

This unit claims no complete BodyGraph-resolution conformance beyond the existing evidence. It claims no broad HumanDesignAPI v2 platform conformance, no live route availability and no public Reader change.

## 19. PR-30 and PR-35 ownership

**PR-30** (after Nathan's Proceed for this exact plan), in the dedicated session:
- recovers existing work first (§8 step 1);
- implements only §7.1 and produces governed evidence only through owners (§6.13, §7.2);
- tests locally (§10), the attestation included;
- commits coherently: source, convergence, record;
- writes and reads back the PR result record v1.0;
- opens the one PR, returns `PR_CANDIDATE_PUBLISHED` and hands off to PR-35 in its own dedicated session;
- does not own review correction, current-head CI readiness or merge.

**PR-35** (its own dedicated session, from PR-30's handoff):
- retrieves and resolves the Codex code review findings (addendum 2.3: no Codex security review);
- retests and pushes coherent corrections. Any member change re-runs §6.13 from step 2, and any evidence-primary change from step 3b, with the attestation again;
- uses CI economically, and verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
- records OBS-17 and O-6 if they occur;
- returns `MERGE_PENDING` without merging. Nathan merges manually; PR-40 by the IA follows the merge.

## 20. Session identity and recovery envelope

```yaml
change: HDE-CRD-0002 / WU-PR-04
phase: PR-20 complete; AWAITING_PO_PROCEED
plan: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md (v1.0)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff
instruction: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (v1.0)
baseline: origin/main 9c82b62de348471b00dd44af8db276a4d14f69f9
refresh_base_release_id: d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner)
authoring_session: https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8
next: PR-30 on Nathan's Proceed for this exact plan
vehicle: none (no implementation branch, commit or PR exists for this unit's code)
resume_point: PR-30 §8 step 1
```

## 21. TypeSafe reading for the receiving session (PR-30, WU-PR-04, plan v1.0)

Action sent (v8.2): "Implement, in a new dedicated session after the Product Owner's Proceed, one work unit of an approved change from a new, not yet reviewed detailed plan whose design was already prototyped, rehearsed and fully tested by the planning session, following its ordered task list: about eleven hand-edited files (a production vendor-override flag with a pre-parse duplicate check on one CLI command, an eight-row environment matrix and seven-step pre-I/O order in the resolver, a new audit module of about 180 lines writing an append-only local record, a read-only production write refusal, a band-flag fix, one new test file of about 450 lines and four extended test files, one evidence generator call, a two-entry CI classifier registration and one document); two release members change, so a same-version release manifest re-cut and a fixed governed-evidence convergence of about twelve owner-tool steps regenerating about 54 paths run in order, each proven byte-stable on a second pass, followed by a full test sweep and an attestation build; then commit, open the pull request and hand off. No live vendor, production or database call; code review, review resolution and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 3.03 (confidence 0.74); rung probabilities low 0.00, medium 0.02, high 0.14, extra high 0.63, max 0.21, ultracode 0.00. Model probabilities Fable 5.1 0.05, Opus 5.5 0.94, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.92). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.032, Fable 5.1 at max 0.011, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.132, Opus 5.5 at extra high 0.592, Opus 5.5 at max 0.197, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.001, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-18T11:03:14Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T11:03:14Z; HTTP 200 in 0.6 s; 5591 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.

- **Notion row:** not written, as PR-20 directs. **Nathan's pick for PR-30:** not stated. **For this PR-20 session:** not stated; the instruction's v8.2 reading for PR-20 is in instruction §19.

**Surface advice:** run PR-30 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** Python 3.12 with CI's install (package-index access for `pip install`), plus `ruby`, `bash` and `curl` on `PATH`. All were present in this session's cloud container. Unset the vendor, database and GitHub keys the container sets.
- **Run times observed here.** A full `tests/` sweep about 26 minutes; one refresh pass about 4; the changed-tests step about 11; the evidence lane about 13; an attestation build about 2.
- **Discipline.** Run the refresh in the implementation branch's working tree only after the member bytes are final, and every check that can write tracked files in a detached worktree. Run the attestation before publishing (F-3).
- **Access.** No live vendor, production or database access is needed.
- **Order.** This plan's pull request should be merged first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-04 / PR-20 / plan 1, version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-04 (S08, S14) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-04 PR engineering session / PR-20 |
| capture time | 2026-10-18T12:08:43Z |
| execution identity | https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8 |
| inherited usage | PR-10 instruction 1 (instruction §20) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

## Canon precedence (Plan Templates, "Canon precedence for template use")

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Canon relied on

Read on `main` at `9c82b62` (`docs/pfcanon/` unchanged since `b9edb0c`).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, hold and Proceed | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (hold label; Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon precedence over in-flight documents) |
| S14 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §7.1.11 preamble and §7.1.11a to §7.1.11f (each clause mapped in §6); §7.1.10 (route selection; OBS-W4-3); §3.1.1 carriers; §3.3 "Usage & typed errors → stderr" and "Determinism pins"; §3.4 exit codes; §4.6 (`--upsert` must not be used in prod; PD-10); §7.2.0 (stale passage) |
| S08 | HDE-CLI-API-Vendor-Ref §4.5; §3.1.1 `aux_narrative_text`, `aux_suppressed_empty`; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §10.1 |
| Sink key | Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1 |
| Stale passages | HDE-CLI-API-Vendor-Ref §7.1.11, §7.2.0; HDE Users Guide §10.1, Recipe F, §16 |
| Overlays and carried items | PF10-HDE-Build-Notes v13.5.9 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md`): addendum 2.8 in full; 2.3 (Rules 1–5); 2.5 ("Retained decisions and requirements": LR-O1 to LR-O3, OBS-17, O-6); 2.6 ("RP-2", "Binding requirements", "Affected surfaces": Dependencies and Downstream work); 2.7 (AD-5 "Order" and "New base"; "Affected surfaces" Downstream); 2.1 (§21) |
| Route-policy statement | Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "`bg:resolve --source vendor` route-policy posture", "Canon precedence for template use" |
| Refresh | Implementation Plan v1.1 §10; WU-PR-03 result v2.0 §8; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| In-flight documents | Specification v1.1 rows S08 and S14, constraints "Release members", "Vendor override", "Override initiator", "Live QA", Exclusions; Plan v1.1 §3, §4, §5 (IF-1, IF-2), §7, §10–§14; review v1.0 N4 and review v1.1's carry line; Audit §6 S08 and S14, §7.1 EC-7; PR instruction v1.0 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; sole Index/Mirror writer; no hand edits; pytest readiness; PR descriptions; truncation guardrail) |

## Checks run by this session

All in the session scratchpad (worktrees and independent clones of `9c82b62`; never pushed), with the environment of §4.3:

| Check | Result |
| :- | :- |
| `git diff --name-only 39afdc6 9c82b62` outside `docs/` | empty |
| Classifier on the two new paths at `9c82b62` | `CI_PRODUCT_OWNER_TEST_MISSING`, `CI_EVIDENCE_OWNER_TEST_MISSING` (instruction §5.10 confirmed) |
| Full `tests/` sweep at `9c82b62` | 4,761 passed, 3 skipped, 2 xfailed, 0 failed (1,544.8 s) |
| First rehearsal: refresh, two passes | 37 and 34 runs exit 0; passes byte-identical; 54 paths |
| First rehearsal: attestation | exit 1, `isolated_stage_failed` at `release_sanity` (F-3) |
| Isolated-environment reproduction | stage 06 `CI rails` fails on the prototype through `tests/bodygraph/test_resolver_vendor.py` (`PROVIDER_CONFIG_INVALID`) and passes after F-3's fix |
| First rehearsal: full sweep | 31 failed, 4,882 passed, 3 skipped, 2 xfailed (F-13) |
| F-13 reproduction | `tests/adapter/test_jsonschema.py` then the mapped-cache file: 27 failed before the fix; with the fix, five files after it: 195 passed, 2 xfailed |
| `APP_ENV`-unset inventory (10 vendor-path test files) | `main`: 168 passed; prototype: 6 failed (F-4), 211 passed |
| EPIC037 and EPIC036 `--check` on `main` and the prototype | exit 1 on both (F-5); EPIC037 bodies equal |
| Negative controls NC-1 to NC-5 | each fails as intended (§4.3) |
| Final rehearsal | refresh 37 + 34 runs exit 0, byte-identical (`f39ee266…`), 54 paths, rehearsal `release_id` `89ddc785…`; sweep no hit; classifier 65 paths, seven lanes, 166 targets; changed-tests step 3,677 passed; seven lanes green; attestation build and verify exit 0; full sweep 4,913 passed, 3 skipped, 2 xfailed, 0 failed; generator, CLI and recompute checks exit 0; EPIC037 bodies equal; NC-1 to NC-5 fail as intended; hermeticity 192 and 195 passed |
| TypeSafe v8.2 | one send for PR-30, HTTP 200 (§21) |

Not executed: hosted CI, and the PR-30 and PR-35 runs on the real branch. No live vendor, production or database call was made.
