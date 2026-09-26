---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC040-PR06b-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06b
pr_instruction_id: HDE-EPIC040-PR06b-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
baseline_main: 870fe5d49600b4f5395fc573fba63aa7d7681cd1
planning_inspection_capture_utc: 2026-09-26T13:36Z (first repository read, approximate) to 2026-09-26T14:10:12Z
next_stage: PR-30 (Product Owner Proceed required first)
---

# HDE-EPIC040-PR06b — PR Implementation Plan v1.0

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-PLAN` |
| version | `v1.0` — first issue; no predecessor plan exists for this unit |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the applicable PF10 overlays (§2.3); no boundary finding raised (§14.1); pending Nathan / Product Owner's exact PR-30 invocation against this version |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR06b` — Reader v1 error-envelope schema conformance (C040-08, alternative A) with a release re-cut to `1.3.0` |
| PR_INSTRUCTION_ID | `HDE-EPIC040-PR06b-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR06b-pr-instruction-v1.0.md`, SHA-256 `d3d750cb51bd02c6fbbc38a5bfc8dd24d6b0f51398b450976a7629b643fb2696`, 9,611 bytes, blob `6db263b44d4896a1a56d6b0f91b33ea1ae5449c9`. On `main` since PR [#511](https://github.com/amthorn78/glow-hdengine-v2/pull/511) merged as `870fe5d` (2026-09-26T13:34:55Z); read completely from `main` |
| IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1, immutable approved base, `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| SPECIFICATION_ID | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| IMPLEMENTATION_AUDIT_ID | `HDE-EPIC040-IMPLEMENTATION-AUDIT` v2.0, `AUDIT_COMPLETE`, `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md`, SHA-256 `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` |
| PLAN_REVIEW_ID (original, preserved) | `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`, SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Applicable overlay decision | `HDE-EPIC040-PR06b-RESCOPE-DECISION` v1.0, `APPROVE` alternative A, decided by the retained whole-change HDE-EPIC040 Implementation Architect by Product Owner direction ("Decide on this", 2026-09-26), `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md`, SHA-256 `cebbe8ec34a91a39d9eec4692fcc8e1832b28d37cfada523638e25ee1a62140c`; with its one addendum `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md`, SHA-256 `63d0bdcee8d4295738bb6a05a5a93c72951a871532e12d53b7e3a449fcca14a3`, drained as **PF10 §2.24** in v13.3.5. Also effective within their scopes: PF10 §2.12 (admission boundary), §2.21 (frozen-capture identity), §2.23 (PR06a; Reader v1 unchanged covenant; the current release this unit re-cuts). No `REMEDIATION_REVIEW` applies |
| Predecessor unit | `HDE-EPIC040-PR06a` is `ACCEPTED_FINAL` (`docs/ephemeral/HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md`, SHA-256 `19ac13b7900cd94fc7d07ccf5991e6fb32e9f47c8cce2832e824f412a34fe12b`); its result v1.1 (`docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.1.md`, SHA-256 `2d0a38bb1c774c17879723c41dc160b31c6c91ee6235d9447745573af4ebdc57`) carries CR-02 (this unit's defect), the re-cut convergence log this plan reuses, and O-P06a-23 (the engine-core owner) |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR06b |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` (this PR-20 run); PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `NOT_YET_ASSIGNED` — the handoff named no reference and the operator assigned none; no platform ID is invented. Known runtime identity from the harness: `https://claude.ai/code/session_018Zth7shEF7GFWMU8jgFUjZ` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR06b` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| Authority boundary | This plan authorizes nothing. Implementation waits for the Product Owner's PR-30 Proceed for this exact version; merge is Nathan's alone; QA, Ops, acceptance, release activation, deployment, PF-Canon edits (including the PF01 §2.3 / PF04 §8.1.2 drainage of C040-08), PF09 movement and Epic closure are outside it (instruction §§4, 8, 10; PF10 §2.24 "Exclusions", "Completion") |

## 2. Exact controlling lineage and source record

### 2.1 Approved and accepted change lineage

| Role | Artifact | Identity used here |
| --- | --- | --- |
| Approved bases | Specification v1.1; Implementation Audit v2.0; immutable Plan v2.1; Plan Review v2.1 Isis-50 `APPROVE` | read; none is rewritten; Plan v2.1 §6.7 (PR07) and §6.8 (OPS01) are what §2.24 amends by addition ("Work-unit effects") |
| Accepted predecessors | PR01 v1.1, PR02–PR05 v1.0, PR06 v1.0 and PR06a v1.0 lineage reviews under `docs/ephemeral/` | all `ACCEPTED_FINAL`; the PR06a review records the admitted 45-member release at `1.2.0`, `release_id 9f962ce3…`, C040-08 reproduced, CR-03 / O-P06a-22, O-P06a-23, O-P06a-03 and O-12 carried |
| This unit's instruction | `HDE-EPIC040-PR06b-pr-instruction-v1.0.md` (§1) | sole native input of this plan; its §§3–13 are mapped into §§3–14 below; where it and §2.24 differ, §2.24 governs (instruction §2) — no difference was found |
| Overlay and decision | §1 | the operative authority: objective, three deliveries, owned loci, proof, exclusions, completion, C040-08 decided A, order `PR01 → … → PR06 → PR06a → PR06b → PR07 → OPS01` |
| Format precedent | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md`, SHA-256 `48cf4120e4613b4fde38ebe26c99186ead627808593540155eb79e576aaa9d68` | structure and the re-cut convergence procedure (its §5.9), as the instruction §5.3 directs ("PR06/PR06a's generation order"); no content inherited |

Accepted-final PR01–PR06a are not reopened, rerun, revised or reaccepted by this plan. PR06a's 45-member `1.2.0` admission is valid history, superseded as the current release only by this unit's re-cut once it lands.

### 2.2 Controlled subject-matter sources used (all from `docs/pfcanon/`, read-only)

| Source | Sections used | Bearing |
| --- | --- | --- |
| `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`, SHA-256 `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e` | §5.2.1 (error_v1 minimum shape `{"schema":"v1","ok":false,"code","error"}`), §5.2.2 (optional `retry_after_ms` and `details` only where transport policy permits), §5.2.3.1 (Reader v1 error envelope has **exactly** `schema`, `ok`, `code`, `error`; `error_envelope()` without `details`; token/status table), §5.2.3.2 (exact messages), §5.2.3.3 (the v1 schema's error branch MUST enforce the closed topology and the governed pairs; `adapter/schemas/error_v1.schema.json` unchanged), §5.2.4.1 (canonical tokens incl. `ERR_READER_INVALID_VERSION`, `ERR_READER_FORBIDDEN`, `ERR_READER_MISSING_PARAM`, `ERR_READER_INVALID_CHART`, `ERR_READER_INVALID_PATH`, `ERR_READER_MISSING_TZ_A/B`, and `ERR_NOT_FOUND` for 404/405), §5.2.5 headers, §5.3 (POST non-conditional) | the envelope this unit's schema must describe; the token inventory (§5.1); the `retry_after_ms` decision (§5.2); one message discrepancy recorded as O-P06b-01 |
| `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`, SHA-256 `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a` | §2.3 (public error object `ok/code/error`, optional `retry_after_ms`, "no additional public fields"; its "static implementation posture" names `schema`/`details` as not permitted; its pointer routes transport ownership to PF05) | the PF01 side of C040-08, decided A; drainage belongs to the PF01 maintainer (§13.1) |
| `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`, SHA-256 `e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696` | §8.1.2 "Typed errors" (`{ ok:false, code, error }` only; `retry_after_ms` the sole integer, only under vendor retry policies), §8.1.3 | the PF04 side of C040-08, decided A; drainage belongs to the PF04 maintainer |
| `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`, SHA-256 `d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d` | §5.1 (manifest shape; the "Reader and governed errors" row: `schemas/reader.v1.schema.json`, `adapter/schemas/error_v1.schema.json`, `engine/compat/error_tokens.py`, `errors/token_map/token_map.json`; version `1.1.0` / `built_at_utc 2026-08-24T18:04:49Z` for the adopted cut) | member form and canonical bytes; the re-cut version is a PF12 drainage item for its maintainer, as `1.2.0` already is under C040-07 (O-P06b-05) |
| `PF03-Reference-Technical-Writing-Best-Practices` | source fidelity | applied to this document |

No PF source was resolved from anywhere but `docs/pfcanon/`. Nothing under `docs/pfcanon/` is changed by this plan or by the unit it plans.

### 2.3 Current controlled PF10 and every applicable active addendum

- Current controlled PF10 Markdown: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md`, SHA-256 `7010511cf61d1e6e84ce1e528f03027058df64eb0be2a6163cd89c7bf27efbae`, 274,422 bytes, 2,557 lines, addenda §2.1 through §2.24, read: the precedence front matter, the complete addendum inventory (the §2.1–§2.24 headings) and, completely, the addenda that bear on this unit — §§2.12, 2.17, 2.21, 2.23 and 2.24 (§2.17 is the F05 deferral whose success-branch items PR06a closed; it says nothing about the error branch). It is newer than the v13.3.4 the PR06a lineage named and carries §2.24, as the instruction §2 states. The five older base files (`v13.3`, `v13.3.1`, `v13.3.2`, `v13.3.3`, `v13.3.4`) sit beside it and are not read (instruction N-01; §13.2 O-P06b-07).
- Applicable active addenda, by repository path, in the order they bear on this unit:
  - §2.24 — `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` (the operative overlay: objective, three deliveries, owned loci, proof, exclusions, completion, work-unit effects, C040-08).
  - §2.23 — `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`, SHA-256 `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9` (Reader v1 remains the unchanged covenant; PR06a delivered the corrected v1 success branch, the v2 schema whose error branch is the pattern here, and the 45-member `1.2.0` release this unit re-cuts).
  - §2.21 — `docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md` (frozen-capture identity source for the canonical JSON gate; the reason a re-cut does not re-identify the frozen captures — instruction §8 "§2.21 frozen captures are not re-identified").
  - §2.12 — `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` (admission binds executing mechanics to the admitted release; the boundary this unit must not change — instruction §8 "no admission-logic change").
  - §2.22 — `docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md` (PR06 accepted final; the convergence and coherence-dependent precedent §2.24 and the instruction §6 invoke).
- Effective baseline: **approved base + applicable PF10 overlays** (`AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`). The PF10 version actually read is recorded as provenance; it is not a gate on later work.

### 2.4 GCFPE execution sources

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, read completely at invocation (page as of 2026-09-24T15:46:52.719Z; Notion read only — no Notion write is directed by this task, so none was made).
- Destination verified for §17: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (page title confirmed by fetch, as of 2026-09-24T15:47:45.499Z; read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members, per the release register named by the handoff; carried as supplied.
- Repository instructions applied: `AGENTS.md` (closed rails, pytest readiness, governed-evidence rules and sole writers, QA-output placement, PR-description contract, code-review scope) and the workspace skills governing write boundaries, artifact storage and reporting. This session wrote only this document, under `docs/ephemeral/`.

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline verified at planning time

| Fact | Value |
| --- | --- |
| `main` | `870fe5d49600b4f5395fc573fba63aa7d7681cd1` (`HDE-EPIC040-PR06b: issue PR instruction v1.0 (INSTRUCTION_READY) (#511)`, 2026-09-26T13:34:55Z); `origin/main` identical. It differs from the instruction's `baseline_main` `679c64b` by exactly one file, the instruction itself (`git diff --stat 679c64b 870fe5d`: 1 file, +165). Every commit since the PR06a landing `d79cfc1` is documentation-only (`git diff --name-only d79cfc1 870fe5d -- . ':!docs/'` is empty; the five changed paths are the PR06a lineage review, the PR06b decision, addendum and instruction, and PF10 v13.3.5), so the runtime tree equals the one the PR06a lineage review executed |
| Remote branches and PRs | `main` and this session's planning branch only. No PR06b implementation branch, worktree or pull request exists; no pull request is open |
| Admitted release | `catalog/manifest.json`: 45 rows, version `1.2.0`, `built_at_utc 2026-08-24T18:04:49Z`, 5,881 bytes, canonical (`sercanon(json.loads(raw)) == raw`); `release_id 9f962ce338c448c7a2312f05695d5fdab12b01fbc1a67d490465d9fc87edab3f`; `load_active_mechanics_bundle()` returns `ADMITTED` (executed in a detached worktree of `870fe5d` with `PYTHONPATH` on that tree: `AdmittedMechanicsBundle`, `1.2.0`, 45 identities, `release_id` equal to the manifest digest and to `identity_meta()`; `release_id_recompute.py --check-manifest-only` and the cutter `--check` exit 0; worktree clean) |
| Working tree | clean at inspection start and end; this plan is the only intended write of this session (`docs/ephemeral/` only) |
| Environment readiness | `python -m pip install -r requirements-dev.txt` then `python -m pytest --version` → `pytest 8.4.2` (container Python 3.11.15); the rehearsal used a virtualenv with CI's install set (§3.3) |

### 3.2 Verified baseline facts that shape this plan

Each fact was established by reading the file named or by executing the command named at the baseline above (execution in the scratch clone of §3.3, never in the checkout).

| # | Fact | Consequence |
| --- | --- | --- |
| F-01 | `engine/config/registry_loader.py`: `ADMITTED_RELEASE_VERSION = "1.2.0"` (line 398), `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` (399), `ADMITTED_RELEASE_ROSTER` (400–446), invariant `!= 45` (448); admission compares the manifest version to the constant (line 1233) and the timestamp to its constant. The file is itself a roster member, so the one-line version edit changes a member's bytes (same size, 73,226; digest `fa1e6315…` → `be8507f4…` in the rehearsal) | the cut must follow the edit (§5.4); the instruction bounds this file to the version constant; `built_at_utc` stays (D-05) |
| F-02 | `schemas/reader.v1.schema.json` (1,690 canonical bytes; sidecar in `sha256sum` format): `$defs.error` has keys `ok` (const false), `code`, `error`, optional integer `retry_after_ms ≥ 0`, `additionalProperties: false`, **no `schema`**; the success branch is the PR06a-conformed six-key closure; `$id https://example.org/schemas/reader.v1.schema.json`, draft 2020-12 | only `$defs.error` changes (§5.1); success branch, `$id`, `$schema`, root `oneOf` and title are untouched (CC-3) |
| F-03 | `schemas/reader.v2.schema.json` `$defs.error`: `oneOf` of twelve exact `code`/`error` const pairs; `properties` `code`/`error` (`type: string`), `ok` (`const: false`), `schema` (`const: "v1"`); `required ["schema","ok","code","error"]`; `additionalProperties: false`; no `retry_after_ms`. Every pair's message equals `ERROR_TOKEN_MAP[code]["message"]` (executed) | the pattern the v1 branch mirrors (D-03) |
| F-04 | Defect reproduced at the baseline: `POST /api/reader?v=1` with body `{}` → 422 `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}` (94 bytes); dev `GET /reader?v=1` without `a`/`b` → 400 `ERR_READER_MISSING_PARAM`; `GET /api/reader?v=1` → 405 `ERR_NOT_FOUND`. All three bodies fail the current v1 schema (`'schema' was unexpected`); the 422 body validates against the v2 schema | CC-1; the goldens' target bytes (§5.3) |
| F-05 | Token inventory by code reading (`adapter/http_reader.py`, `engine/compat/error_tokens.py`, `engine/bodygraph/resolver.py::projection_refusal`), confirmed by execution. Production `POST /api/reader?v=1` can emit exactly the twelve tokens of the v2 branch: `ERR_READER_INVALID_VERSION` (`_select_reader_version`), `ERR_READER_INVALID_INPUT` (`_parse_reader_post_body`), `ERR_M10_RESOLVER_UNAVAILABLE` and `ERR_M10_PERSON_UNRESOLVED` (`_reader_current_rows`, `MappedCacheError`, `AdapterError`), the ten distinct Reader-transport tokens of `BOUNDARY_REASONS` (`ERR_READER_INVALID_INPUT`, `ERR_READER_INVALID_CHART`, `ERR_M10_BODYGRAPH_INCOMPLETE`, `ERR_M10_RESOLVER_UNAVAILABLE`, `ERR_M10_PERSON_UNRESOLVED`, `ERR_M10_LEGACY_INPUT_UNSUPPORTED`, `ERR_M10_CONFIG_MISMATCH`, `ERR_M10_MANIFEST_MISMATCH`, `ERR_M10_RESULT_SCHEMA_MISMATCH`, `ERR_M10_STALE_RESULT`) reached through `_reader_failure` (`CompatBoundaryError`, `projection_refusal`, `admission_token_for`), and `ERR_NOT_FOUND` (the governed 405 on `/api/reader` and on the unprefixed `POST /reader`). Dev `GET /reader` (`reader_v1`) additionally emits `ERR_READER_FORBIDDEN` (non-dev `APP_ENV`), `ERR_READER_MISSING_PARAM`, `ERR_READER_INVALID_PATH` (also via the alias `invalid_path`, canonicalized by `canonical_token_for`), `ERR_READER_INVALID_CHART` and `ERR_READER_MISSING_TZ_A` / `ERR_READER_MISSING_TZ_B` (`_safe_load_chart`, `_require_tz_or_raise`). `ERR_M10_GATES_MISSING` / `ERR_M10_GATES_INVALID` are in `MAGIC10_HTTP_STATUS` but unreachable from either route (`BOUNDARY_REASONS` maps `gates_*` to `ERR_M10_BODYGRAPH_INCOMPLETE` on the Reader transport; PF05 §5.2.3.1 assigns them to the internal/CLI rows). Total: **17 distinct governed pairs** | the exact `oneOf` of §5.1 (D-01) |
| F-06 | No governed Reader v1 emitter produces `retry_after_ms`: `engine.compat.errors.error_envelope` emits `schema`, `ok`, `code`, `error` and adds `details` only when passed; the Reader helpers `_error` and `_reader_method_not_allowed` never pass it; `adapter/retry_after.py::parse_retry_after_ms` has **no importer** anywhere under `adapter/`, `engine/`, `presenter/`, `scripts/`, `ci/`, `dev/`; `engine/bodygraph/vendor_client.py::_retry_after_ms` feeds a vendor keys-only log field, not an envelope; `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py` and `test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py` call routes that do not exist (`/_test/429_seconds`, `/_test/429_date`) and are in no CI lane; PF05 §5.2.3.1 fixes the Reader v1 envelope at exactly four keys | `retry_after_ms` is dropped from the v1 error branch (D-02); the two legacy tests are an observation (O-P06b-02) |
| F-07 | `goldens/reader/v1/g06_error_invalid_input.json` is synthetic (`{"code":"InvalidInput","error":"bad gates","ok":false}`, 55 bytes, `bf802311…`), written by `scripts/make_reader_v1_goldens.py` through `json.dumps`, not through the emitter. The script already imports `emit_public` and `error_envelope` (the v2 `g04` golden uses them). `emit_public(error_envelope("ERR_READER_INVALID_INPUT"))` equals the route's 422 bytes byte for byte (F-04; executed) | the g06 change is three lines in the writer (§5.3, D-04) |
| F-08 | `scripts/make_release_pack.sh` lists the v1 schema and the eight v1 goldens; `tests/reader_v1/test_release_pack.py` asserts that list and that running the script leaves the two tracked outputs byte-identical. Changing the schema and g06 bytes changes `artifacts/release_id.txt` (65 bytes) and leaves `artifacts/release_pack_manifest.json` unchanged. Neither output is an Index/Mirror row (no `evidence_index.jsonl` row names them); both classify to the evidence lane | the pack is regenerated by the script after the final golden bytes (§5.3, D-07) |
| F-09 | Consumers of the v1 schema's error branch in tests: `tests/reader_v1/test_schema.py` (`test_error_shape_valid_with_retry_after_optional` with the synthetic envelope and `retry_after_ms`; the error case of `test_additional_properties_closed_everywhere`) and `tests/reader_v1/test_goldens.py` (`test_v1_goldens_are_the_harmony_covenant` asserts the synthetic g06 dict). `tests/reader_v1/test_emitter.py`, `tests/config/test_production_admission.py` and `tests/config/helpers.py` touch the success branch or the member bytes only. `.audit_src/` is a frozen legacy snapshot and `scripts/make_cli_smoke_audit.sh` only copies the file; neither is a lane input | the exact rewrites of §8.1–§8.2 |
| F-10 | Literal version pins: exactly three — `tests/config/test_production_admission.py:375` (`== "1.2.0"`), `tests/config/test_manifest_schema.py:141`, `tests/config/test_registry_catalog_contract.py:322`. Every other version/timestamp assertion (`tests/config/helpers.py`, `tests/scripts/test_cut_release_manifest.py`, the rest of `test_production_admission.py`) reads the constants. No test pins `release_id 9f962ce3…`; the 45-count pins stay true | §8.5 (D-11) |
| F-11 | Bindings of the current `release_id` outside `docs/` and tests: `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`, `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`, `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`, `audit/gates/parity/reader_cli/{ab,ba}.json`; the A7 success proofs, the determinism family, the gate outputs and the F07 artifacts report `DRIFT` on the re-cut (§3.3). All are owner-written | §5.4 convergence order; §6.3 |
| F-12 | `tools/evidence/generate_engine_core_evidence.py` builds its synthetic root from the real roster and records `release_id` in the run payloads **and** the source digests of its inputs in `artifacts/core/purity/purity_report.json` (`source_sha256` includes `engine/config/registry_loader.py`). The version edit therefore changes all four engine-core artifacts, including the purity report that PR06a's PR-35 re-cut left unchanged (that re-cut did not touch `registry_loader.py`) | the engine-core owner is a mandatory convergence step (§2.24 item 3; O-P06a-23; D-08) |
| F-13 | `tools/evidence/generate_open_rails_abba_proof.py` pins `FROZEN_OPEN_ABBA_SHA256` (`29223e6f…`) to the digest of `audit/gates/determinism/open_rails_abba.json`; that primary carries the release identity and is regenerated by the re-cut; `tests/evidence/test_open_rails_abba_proof.py:338` asserts the constant equals the file digest; the rails lane's `--check-current` reads it. PR06 (`f7484d0`) and PR06a (`dc958ec`) each landed exactly this constant refresh | the one coherence dependent outside the literal §6 list, named as the instruction requires (§6.2, D-06) |
| F-14 | Classifier (`ci/checks/classify_ci_changes.py`) at the baseline already registers every path this unit touches: `schemas/reader.v1.schema.json` → (`tests/reader_v1/test_schema.py`, `test_goldens.py`, `tests/config/test_production_admission.py`) and its `.sha256` → `test_schema.py`; `scripts/make_reader_v1_goldens.py` → `test_goldens.py`; `goldens/reader/` → lanes `{product, compat, release}`, owners (`test_goldens.py`, `test_release_pack.py`); `engine/config/registry_loader.py` → eight `tests/config/*` owners; `catalog/manifest.json` → (`tests/runtime/test_identity.py`, `tests/evidence/test_release_manifest_content_binding.py`); `tools/evidence/generate_open_rails_abba_proof.py` → its evidence owner test; `artifacts/**` → evidence (+ release where applicable); `tests/http/test_reader_post_v1.py` is in `_HTTP_READER_TEST_OWNERS`. Dry run on the rehearsed stage-1 change: `lanes=product,compat,evidence,release`, `changed_tests=true`, 11 changed-test targets, no `CI_CHANGE_SURFACE_UNCLASSIFIED` / `CI_PRODUCT_OWNER_TEST_MISSING` / `CI_EVIDENCE_OWNER_TEST_MISSING` | no classifier change (D-09); §6.5 |
| F-15 | CI (`.github/workflows/ci.yml`): one `test` job; exact-head checkout; classifier; changed tests in a detached worktree with `git diff --exit-code` and a clean-tree assertion; seven lanes; the release lane runs `git diff --exit-code`, `release_id_recompute.py --check-manifest-only`, the four release tests in a worktree, then `build_release_attestation.py --output … --require-clean` and `--verify`; final `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | §10 |
| F-16 | `errors/token_map/token_map.json` (30 entries) carries exactly the `ERROR_TOKEN_MAP` code set (executed); every one of the 17 tokens is registered with the message the routes emit | no new token, no token-map regeneration (§5.5) |
| F-17 | PF05 §5.2.3.2 lists the exact message of `ERR_READER_INVALID_CHART` as `invalid Reader chart`; `ERROR_TOKEN_MAP`, `token_map.json`, the v2 schema and the emitted bytes all carry `invalid reader payload` | the v1 branch binds to the emitted bytes and the token map, as the v2 branch does (PR06a IF-01); the discrepancy is carried as O-P06b-01, not corrected here (a message change would change response bytes, which §2.24 excludes) |
| F-18 | `adapter/schemas/error_v1.schema.json` (a roster member, draft-07) requires `ok`, `schema`, `code`, `error` and allows `details`; PF05 §5.2.3.3 keeps it unchanged | unchanged; after this unit the Reader v1 branch agrees with it on the four required keys and is stricter (no `details`), as PF05 §5.2.3.1 requires |
| F-19 | `tests/reader_v1/test_cli_proof.py` fails at the baseline (`scripts/hd_cli.py` exits 2 `ADMIN_FLAG_REQUIRED`; PR06a plan D-18, review O-P06a-03); it is in no lane or roster. `scripts/hd_cli.py` reads the legacy `artifacts/release_id.txt`, whose bytes this unit regenerates; the failure's cause is unaffected | untouched (D-13); recorded in the result |
| F-20 | Two environment facts from PR06a stand: `ci/checks/run_rails_job_definitions.py` shells to `python -m pytest`, so `python` on `PATH` must be the interpreter carrying pytest; the editable install must point at the tree being attested | §10.1 |

### 3.3 Planning rehearsal in a scratch clone (inference support, not PR evidence)

To plan from execution rather than reading alone, this session rehearsed the complete unit in a throwaway clone of `870fe5d` under the session scratchpad (`pr06b-rehearsal`; one virtualenv with CI's install set `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`: Python 3.11.15, pytest 8.4.2, `engine` resolving from the clone), never in the repository checkout. Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` removed from the process environment for every command. No vendor call and no database connection occurred; the only open-rails command was the fixture-mode open-rails ABBA proof, as PR06a's plan prescribes. What follows is **inference support**; it is not implementation, QA or CI, and none of its bytes enter the PR. PR-30 re-executes every step on the real branch (§§9–10).

| Step rehearsed (stage 1, 13:46Z) | Outcome |
| --- | --- |
| Baseline defect and token inventory | F-04, F-05, F-06 as recorded; predicted g06 bytes equal the route's 422 bytes |
| `$defs.error` rewritten as §5.1 (17 pairs, v2 structure, title kept), canonical bytes, sidecar | 3,466 bytes, SHA-256 `42bd46c41e6ddf00d647c4a81ee3e797e07d50c4c8d18b58d07565e7301b6370`; `sercanon(json.loads(raw)) == raw` |
| Goldens writer edited (three lines, §5.3); `python scripts/make_reader_v1_goldens.py`; `bash scripts/make_release_pack.sh` | g06 = the route bytes, 94 bytes, SHA-256 `c5eb83aec246444fe5d207f14e089b28d2cafc35c5d84ff49bc719b01c37b27a`; every other golden byte-identical; `artifacts/release_id.txt` → `8ca9ba71c8d8ba3a4a775f20741d6d22cd31fde8c8f8793fdc5e3ab8b5324806`; `release_pack_manifest.json` unchanged |
| `ADMITTED_RELEASE_VERSION = "1.3.0"`; `cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `release_id_recompute.py --check-manifest-only`; cutter `--check` | exit 0 / 0 / 0; 45 rows, 5,881 bytes; only the `engine/config/registry_loader.py` and `schemas/reader.v1.schema.json` rows changed; `load_active_mechanics_bundle()` → `AdmittedMechanicsBundle`, version `1.3.0`, 45 identities, `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` = `sha256(manifest)` = `identity_meta()["release_id"]` — **rehearsal value**: the real value is what the cutter computes on the real branch; it equals this one only if the member bytes of §5.1 and §5.4 are reproduced exactly, and a different value must be explained by a member-byte difference |
| Classifier dry run on the eight stage-1 paths | `lanes=product,compat,evidence,release`; 11 changed-test targets (the eight `registry_loader.py` owners plus `tests/reader_v1/{test_goldens,test_release_pack,test_schema}.py`); no unclassified path, no missing owner |

| Step rehearsed (stage 2, convergence in PR06's order, 13:47–13:52Z) | Outcome |
| --- | --- |
| 3 Admission; `generate_config_artifacts.py --compare-goldens . --report <scratch>` | `52be4558… 45 1.3.0`; `ok: true`, `mismatches: []`, `candidate_release_id` = the cut |
| 4 Gate | `--check-only` 1 before the write (manifest target changed); write 0; `--check-only` 0 |
| 5 Updater | write 0; `--check` 0 |
| 6 Config family | `--publish-family` 0 (the two catalog logs); updater `--check` 0 |
| 7 Live producers | A7 `--check` 1 (`DRIFT` on the five success proofs), `HDE_WRITE_A7_PROOFS=1` write 0, `--check` 0; determinism `--check` 1 (`DRIFT` on `ab.json`, `ba.json`, `summary.json`, `abba.bytes`, `tworun_identity.sha256`), write 0, `--check` 0; open-rails fixture proof with `SAFE_MODE=0 ALLOW_NETWORK=1` and the keys absent: write 0, `FROZEN_OPEN_ABBA_SHA256` refreshed to `c78740b3f9d45472e67c3bdeef4ade9e4a9c74fc3e6b11bc2f29d1a90a323348`, `--check` 0; F07 generator `--check` 1 (`DRIFT` on both writer artifacts), write 0, `--check` 0 |
| Engine-core owner (O-P06a-23) | `generate_engine_core_evidence.py` 0 (it runs the updater, its `--check` and `orientation_demo.py --check` itself); all four payloads changed, the purity report through its `source_sha256` of `registry_loader.py` (F-12) |
| 5–8 restart | updater 0 / `--check` 0; `--publish-family` 0 / `--check` 0; A7, determinism, open-rails and F07 `--check` 0 each; `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `check_lf_endings.py`, `check_final_lf.sh`, `refresh_step_logs_manifest.py --check` all 0 |
| 9 Sanity | non-canonical run to a scratch log 0, `summary:PASS`, `first_failed_stage:NONE`; canonical run 0, tracked log byte-identical to the PASS model (`88d787c1…`); `run_sanity_pipeline_gate.py` 0; updater `--check` 0 |
| 10 Frozen families | showcompat, CLI conformance, rails gate evidence and env matrix `--check` 0 each |
| Touched-file set after convergence | 51 paths over the stage-1 eight: `tools/evidence/generate_open_rails_abba_proof.py` (constant) and 50 owner-written files — `artifacts/catalog/*.log` (2), `artifacts/core/**` (4), `artifacts/evidence_index.jsonl` and `.sha256` (2), `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}` (5), `artifacts/writer/*` (2), `audit/gates/canonical_json/*.log` (2), `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}` (3), `audit/gates/json_gate/canonical/*.ndjson` (2), `audit/gates/parity/reader_cli/{ab,ba,summary}.json` (3), and their 25 path proofs. Unchanged by measurement: `docs/evidence/INDEX.json` (`163fbc21…`), the sanity log, `artifacts/audit/ENDPOINTS_CATALOG.json` (`acb78306…`, also reached through the `docs/ENDPOINTS_CATALOG.json` symlink), `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/success_writers_errors.txt`, `artifacts/release_pack_manifest.json`, `schemas/reader.v2.schema.json`, `errors/token_map/token_map.json`, every other golden and every frozen family |
| Second run of steps 2–9 | cutter `--check`, gate, updater, `--publish-family`, A7, determinism, open-rails, F07 and engine-core writers, updater, canonical sanity, gate wrapper, updater `--check`: all 0; the digest of the complete working-tree diff was identical before and after (`dbffe2ee…`); no untracked file |
| Stale-binding sweep | `git grep` outside `docs/`, `.audit_src/`, `handoff/` and the two legacy `manifest_*.sha256` for the superseded `release_id 9f962ce3…`, the superseded v1 schema digest `5af89652…`, the superseded g06 digest `bf802311…` and the superseded open-rails digest `29223e6f…`: none remain |

| Step rehearsed (stage 3, tests and candidate-wide validation, from 13:54Z) | Outcome |
| --- | --- |
| The test rewrites of §8 applied (six files; committed in the clone) | 65 files changed against `870fe5d` in total: the eight of stage 1, the 51 of stage 2 and the six test homes |
| Focused suites (§10.2 roster, 32 files) | `1285 passed, 3 skipped in 115.64s`, exit 0; the three skips are the pre-existing open-rails vendor cases of `tests/cli/test_showcompat_parity_and_identity.py` (lines 108, 128, 150, `showcompat vendor calls require open rails`), unchanged by this unit |
| `tests/reader_v1/test_cli_proof.py` alone | 1 failed, exit 1 — the pre-existing baseline failure (`scripts/hd_cli.py` exits non-zero for the test's `--admin-out` call; `CalledProcessError`; O-P06a-03, F-19); in no lane or roster |
| Classifier on the committed candidate (`--base 870fe5d… --head <clone head> --event-name pull_request`) | exit 0; `lanes=product,compat,evidence,release`; `db=false`, `rails=false`, `qa=false`; `needs_python=true`; `changed_tests=true`; `reason=selected_lanes`; `path_count=65`; no `CI_CHANGE_SURFACE_UNCLASSIFIED`, `CI_PRODUCT_OWNER_TEST_MISSING` or `CI_EVIDENCE_OWNER_TEST_MISSING`; 14 changed-test targets: the eight `registry_loader.py` owners (`tests/config/{test_alias_policy_enforcement,test_config_loader_unknown_ids_fail_closed,test_execution_coherence,test_magic10_contracts,test_manifest_schema,test_production_admission,test_registry_catalog_contract,test_typed_bundles}.py`), `tests/evidence/test_http_reader_ci_ownership.py`, `tests/evidence/test_open_rails_abba_proof.py`, `tests/http/test_reader_post_v1.py`, `tests/reader_v1/{test_goldens,test_release_pack,test_schema}.py` |
| Changed-test isolation (detached worktree, `git diff --exit-code`, clean status) | `667 passed in 60.07s`; `git diff --exit-code` 0; no untracked file |
| Lane-equivalent commands (verbatim from `ci.yml`), all seven lanes | product: ordering `--check` 0, `20 passed`. compat: `check_cli_help.sh` 0, serializer grep guard `summary: PASS`, emitter symbol proof `summary:PASS`, `102 passed, 3 skipped, 2 xfailed` (pre-existing markers). db (prudence): `DIRECT_DB_CONTRACT_OK`, `249 passed`. rails (prudence): runner exit 0 — `rails_closed_refusal` 4 passed, `rails_open_conformance` 113 passed with `--check-current` → `{"result": "pass", "status": "OK", "top_level_pass": true}`, `logs_keys_only_redaction` `RAILS_GATE_EVIDENCE_OK` 39 passed, `RAILS_JOB_DEFINITIONS_OK`; workflow integration `133 passed`. evidence: updater, orientation, step-log, index-hash, path, mirror-schema and final-LF checks 0 each; `111 passed in 289.67s`. qa (prudence, detached worktree): `488 passed`, worktree clean. release: `git diff --exit-code` 0; `--check-manifest-only` 0; `64 passed` in a detached worktree, clean. `RELEASE_NOT_ADMITTED` appears in no log |
| Strict attestation from the committed clean clone into an external empty directory, then `--verify` | build exit 0 and `--verify` exit 0, 89 seconds; `attestation.json` 28,163 bytes, SHA-256 `530c551880231c344190420f646315ae19b79ecce236991df3ac5935f01292c2`: `schema hde.release_attestation.v1`, `source_commit` = the clone head with `source_commit_exact: true`, `release_id` = `manifest_sha256` = `52be4558…`, `validation_result PASS`, `release_admission PR06R_B_FINAL_PASS`, `pipeline_stop null`, 174 files bound, 14 `omitted_files` (the builder's existing secret-safety omissions, the same count PR06 and PR06a recorded), five `nonclaims`; the bundle stayed in the scratchpad |
| Tree after everything | `git diff --exit-code` 0 and empty `git status --short --untracked-files=all` after every isolated run and at the end (14:04:38Z) |

Caveats: the rehearsal ran on Python 3.11.15 (CI: 3.12); its bytes and `release_id` are not the real ones until PR-30 reproduces them on the real branch; nothing above is a QA result.

## 4. Exact objective, completion conditions and exclusions

### 4.1 Objective (§2.24 "Objective"; instruction §4)

Make the published Reader v1 schema accept the Reader v1 error envelope the routes actually emit (PF05 §5.2), and bind the result with one release re-cut to `1.3.0`.

### 4.2 Completion conditions

| ID | Condition | Proven by |
| --- | --- | --- |
| CC-1 | Every governed Reader v1 error response from `POST /api/reader?v=1` and dev `GET /reader` validates against the corrected v1 schema — tested for each of the 17 tokens the v1 routes can emit (F-05) | §8.1 (17 pairs), §8.4 (`_assert_error` validates every route-level error; the 17-token helper case; the dev-route cases) |
| CC-2 | Refused by the schema: a v1 error with no `schema`; a wrong `schema` const; an ungoverned `code`; a governed `code` with the wrong message; an extra key (`details`, `retry_after_ms`); `ok: true`; the retired synthetic golden | §8.1 adverse cases |
| CC-3 | Every existing v1 success golden still validates; Reader v1 and v2 response bytes are unchanged; dev `GET /reader` bytes are unchanged | §8.2 (goldens), the existing `test_dev_get_bytes_for_the_fixture_pair_are_unchanged`, the unchanged `tests/http/test_reader_post_v2.py` (66 cases), `git diff --exit-code` on `goldens/reader/v1/g0[1-5]*`, `g07*` and `goldens/reader/v2/*` (C1 proof), and the untouched emitters and routes (§6.6) |
| CC-4 | Admission returns `ADMITTED` on `1.3.0` with a recomputed `release_id`; a tampered, missing or extra member is refused | `tests/config/test_production_admission.py`, `test_execution_coherence.py`, `test_manifest_schema.py`, `tests/scripts/test_cut_release_manifest.py` (existing adverse cases, unchanged), the real-root cases (§8.5) |
| CC-5 | Config artifacts, registry report, bundles and evidence — including the engine-core owner — converge through their owners in PR06/PR06a's generation order; a second run is byte-stable; no stale binding to the superseded identities remains outside `docs/` | §5.4, §10.4 evidence lane, the sweep of C4 |
| CC-6 | The strict attestation builds and verifies in the ordinary-CI release lane on the exact candidate head | §10.6 rehearsal (`NOT EXECUTED` on the real candidate until PR-30 and CI run it) |
| CC-7 | Real code review and security review pass on the exact candidate head (PR-35) | §11 |
| CC-8 | Ordinary CI is green on the exact candidate head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | §10.3–10.4 |
| CC-9 | PR06b claims no QA verdict, acceptance, PF09 movement or closure | §15 |

### 4.3 Hard exclusions (§2.24 "Exclusions"; instruction §8)

No change to Reader v1 or v2 response bytes, routes, the success branches, Magic-10, or the v2 schema; no roster membership change; no admission-logic change; no change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS`; no PF-Canon edit; no deployment or activation. Inherited, not resolved here: CR-03 / O-P06a-22 (HTTP transport owner), O-12 (packaging owner / Product Owner), O-P06a-03 (`scripts/hd_cli.py` / `test_cli_proof.py`, its owner), the §2.21 frozen captures (not re-identified).

## 5. Designed interfaces, invariants and contracts

### 5.1 Reader v1 error branch — `schemas/reader.v1.schema.json` and `.sha256` (owned locus; D-01, D-03, D-14)

Only `$defs.error` changes. It mirrors the v2 branch's structure (F-03) and keeps its own `title`:

- `additionalProperties: false`;
- `properties`: `code` (`type: string`), `error` (`type: string`), `ok` (`const: false`), `schema` (`const: "v1"`);
- `required`: `["schema", "ok", "code", "error"]`, in that order;
- `oneOf`: exactly the 17 governed `code`/`error` const pairs of F-05, in this fixed order — the twelve of the v2 branch in the v2 branch's order, then the five dev-route tokens in route order:

| # | `code` | `error` |
| --- | --- | --- |
| 1 | `ERR_READER_INVALID_VERSION` | `unsupported reader version` |
| 2 | `ERR_READER_INVALID_INPUT` | `invalid Reader request` |
| 3 | `ERR_READER_INVALID_CHART` | `invalid reader payload` |
| 4 | `ERR_M10_PERSON_UNRESOLVED` | `BodyGraph not found` |
| 5 | `ERR_M10_RESOLVER_UNAVAILABLE` | `BodyGraph resolver unavailable` |
| 6 | `ERR_M10_BODYGRAPH_INCOMPLETE` | `BodyGraph is incomplete` |
| 7 | `ERR_M10_LEGACY_INPUT_UNSUPPORTED` | `legacy scoring input is unsupported` |
| 8 | `ERR_M10_CONFIG_MISMATCH` | `Magic10 configuration mismatch` |
| 9 | `ERR_M10_MANIFEST_MISMATCH` | `Magic10 release manifest mismatch` |
| 10 | `ERR_M10_RESULT_SCHEMA_MISMATCH` | `Magic10 result schema mismatch` |
| 11 | `ERR_M10_STALE_RESULT` | `Magic10 cached result is stale` |
| 12 | `ERR_NOT_FOUND` | `not found` |
| 13 | `ERR_READER_FORBIDDEN` | `reader endpoint disabled` |
| 14 | `ERR_READER_MISSING_PARAM` | `missing required reader parameters` |
| 15 | `ERR_READER_INVALID_PATH` | `invalid chart path` |
| 16 | `ERR_READER_MISSING_TZ_A` | `missing tz for party A` |
| 17 | `ERR_READER_MISSING_TZ_B` | `missing tz for party B` |

Every message is `ERROR_TOKEN_MAP[code]["message"]` (F-16). `retry_after_ms` is removed (§5.2). The resulting `$defs.error`, in canonical form, is exactly:

```json
{"additionalProperties":false,"oneOf":[{"properties":{"code":{"const":"ERR_READER_INVALID_VERSION"},"error":{"const":"unsupported reader version"}}},{"properties":{"code":{"const":"ERR_READER_INVALID_INPUT"},"error":{"const":"invalid Reader request"}}},{"properties":{"code":{"const":"ERR_READER_INVALID_CHART"},"error":{"const":"invalid reader payload"}}},{"properties":{"code":{"const":"ERR_M10_PERSON_UNRESOLVED"},"error":{"const":"BodyGraph not found"}}},{"properties":{"code":{"const":"ERR_M10_RESOLVER_UNAVAILABLE"},"error":{"const":"BodyGraph resolver unavailable"}}},{"properties":{"code":{"const":"ERR_M10_BODYGRAPH_INCOMPLETE"},"error":{"const":"BodyGraph is incomplete"}}},{"properties":{"code":{"const":"ERR_M10_LEGACY_INPUT_UNSUPPORTED"},"error":{"const":"legacy scoring input is unsupported"}}},{"properties":{"code":{"const":"ERR_M10_CONFIG_MISMATCH"},"error":{"const":"Magic10 configuration mismatch"}}},{"properties":{"code":{"const":"ERR_M10_MANIFEST_MISMATCH"},"error":{"const":"Magic10 release manifest mismatch"}}},{"properties":{"code":{"const":"ERR_M10_RESULT_SCHEMA_MISMATCH"},"error":{"const":"Magic10 result schema mismatch"}}},{"properties":{"code":{"const":"ERR_M10_STALE_RESULT"},"error":{"const":"Magic10 cached result is stale"}}},{"properties":{"code":{"const":"ERR_NOT_FOUND"},"error":{"const":"not found"}}},{"properties":{"code":{"const":"ERR_READER_FORBIDDEN"},"error":{"const":"reader endpoint disabled"}}},{"properties":{"code":{"const":"ERR_READER_MISSING_PARAM"},"error":{"const":"missing required reader parameters"}}},{"properties":{"code":{"const":"ERR_READER_INVALID_PATH"},"error":{"const":"invalid chart path"}}},{"properties":{"code":{"const":"ERR_READER_MISSING_TZ_A"},"error":{"const":"missing tz for party A"}}},{"properties":{"code":{"const":"ERR_READER_MISSING_TZ_B"},"error":{"const":"missing tz for party B"}}}],"properties":{"code":{"type":"string"},"error":{"type":"string"},"ok":{"const":false},"schema":{"const":"v1"}},"required":["schema","ok","code","error"],"title":"error","type":"object"}
```

The whole file is written as canonical bytes (`engine.serializer.canon.sercanon(doc, sort_keys=True)`; UTF-8, ASCII-sorted keys, compact separators, one trailing LF) — 3,466 bytes, SHA-256 `42bd46c4…` when reproduced exactly — and the sidecar is regenerated in `sha256sum` format (`<hex64>  schemas/reader.v1.schema.json\n`). The pair order is fixed so that PR-30 reproduces the same bytes; an equivalent order would still be correct but would yield a different digest and a different `release_id`. `$id`, `$schema`, the root `oneOf`, the title `Reader v1 — public envelope (success | error)` and `$defs.success`, `category`, `category_id`, `band`, `hex64`, `meta` are byte-for-byte unchanged (CC-3).

### 5.2 `retry_after_ms` — dropped (D-02)

§2.24 item 1 keeps `retry_after_ms` "only if a governed emitter produces it", and the instruction §5.1 requires the plan to establish this by reading the code. F-06 establishes that none does: the single error emitter path (`error_envelope` → `emit_public`) never sets it, the only parser of `Retry-After` in the adapter has no importer, and the vendor client's value is a keys-only log field. PF05 §5.2.3.1 independently fixes the Reader v1 envelope at exactly four keys. The corrected branch therefore refuses `retry_after_ms` as an extra key (CC-2). PF05 §5.2.2's general allowance for the field on transports whose policy permits it is untouched; no such Reader v1 transport policy exists in the repository.

### 5.3 Goldens through their owning writer — `scripts/make_reader_v1_goldens.py`, `goldens/reader/v1/g06_error_invalid_input.json` and `.sha256`, the release-pack outputs (D-04, D-07)

- The g06 block of the writer becomes one call through the canonical emitter: `_write(OUT / "g06_error_invalid_input.json", emit_public(error_envelope("ERR_READER_INVALID_INPUT")))`, replacing the three-line `json.dumps` synthetic (F-07). The comment names PF05 §5.2 and PF10 §2.24. No other line of the writer changes; both imports already exist. The filename is unchanged: the release-pack list and the test homes reference it.
- Running the writer regenerates the v1 and v2 families; every file but g06 and its sidecar must be byte-identical (C1 proof). g06 becomes the exact production 422 bytes: `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}\n` (94 bytes; sidecar hash-only, `c5eb83ae…`).
- `bash scripts/make_release_pack.sh` (default `FILES`) regenerates `artifacts/release_id.txt` (the pack digest, changed) and rewrites `artifacts/release_pack_manifest.json` with identical bytes. Both are committed after the final golden and schema bytes, so `tests/reader_v1/test_release_pack.py`'s byte-idempotence assertion holds in CI's worktree (F-08).

### 5.4 Release re-cut and convergence order (§2.24 item 3; instruction §5.3; D-05, D-06, D-08)

- `engine/config/registry_loader.py`: `ADMITTED_RELEASE_VERSION = "1.3.0"`. Nothing else in the file changes: `ADMITTED_RELEASE_BUILT_AT_UTC` stays `"2026-08-24T18:04:49Z"` (the instruction §5.3 keeps PR06a's timestamp; admission compares the manifest timestamp to this constant, which the instruction bounds this unit not to touch — D-05, O-P06b-05), the roster and the `!= 45` invariant stay, and the PF10 §2.12 boundary and every admission check are untouched.
- Members whose bytes this unit changes, and which therefore fix the cut order: `schemas/reader.v1.schema.json` (§5.1) and `engine/config/registry_loader.py` (this item). `.json` members must be canonical bytes; `.py` members one final LF (member-format rule of the cutter).
- Cut command (closed rails), after every member byte is final: `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; then `python scripts/release_id_recompute.py --check-manifest-only`; then the cutter with `--check`. `release_id = sha256(canonical manifest bytes)`, recomputed on the real branch and recorded in the result artifact (rehearsal value in §3.3).
- Convergence order — PR06's generation order as PR06a executed it (result v1.1 §6.3), plus the engine-core owner (O-P06a-23; §2.24 item 3). Every step under closed rails unless stated; each producer re-run on unchanged inputs to prove a fixed point:

| Step | Owner command | Produces / proves |
| --- | --- | --- |
| 1 Source and fixtures | schema bytes and sidecar final (§5.1); `python scripts/make_reader_v1_goldens.py`; `bash scripts/make_release_pack.sh`; the version edit | members pass the member-format rule; goldens, their sidecars and the pack outputs written by their owners |
| 2 Cut | cutter, recompute check, cutter `--check` (above) | complete canonical 45-row manifest at `1.3.0`; `release_id` fixed; fixed point |
| 3 Admission and comparison | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; b=l(); print(b.release_id, len(b.source_identities), b.manifest.version)"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | real-root admission, 45, `1.3.0`; eight goldens `match`, `ok: true`; exit 0 |
| 4 Gate | `python tools/evidence/run_canonical_json_gate.py`; then `--check-only` | gate outputs for the re-cut manifest; 26 targets, six set rules unchanged |
| 5 Updater | `python tools/evidence/update_evidence_index.py`; `--check` | Index/Mirror/path proofs bind the gate outputs and the manifest before publication |
| 6 Config family | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | the two catalog logs converge (they carry `release_id`); registry report and bundles byte-idempotent |
| 7 Live producers | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, vendor and DB keys absent) then refresh `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` to `sha256sum audit/gates/determinism/open_rails_abba.json`; `python tools/evidence/generate_conjunction_writer_evidence.py` (closed rails); then each owner's `--check` | the five A7 success proofs, the determinism family, the fixture open-rails proof and the two F07 writer artifacts regenerated from the admitted root |
| 7b Engine-core owner | `python tools/evidence/generate_engine_core_evidence.py` (runs the updater, its `--check` and `orientation_demo.py --check` itself) | `artifacts/core/{two_run/identity,abba/ab_ba_parity,json_compare/core_result_json_compare,purity/purity_report}.json` regenerated with the new `release_id` and the new `registry_loader.py` digest (F-12) |
| 8 Updater and read-only checks | updater; `--check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `python tools/evidence/refresh_step_logs_manifest.py --check` | all companions current |
| 9 Sanity | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` must end `summary:PASS`; then the canonical run; `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check`. If a canonical run ever binds the FAIL model, apply the PR06 plan §5.8 pre-binding before the next canonical run | `audit/gates/sanity_pipeline/sanity_pipeline.log` in the PASS model, byte-identical to the tracked bytes; wrapper exit 0 |
| 10 Frozen families | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen digests intact; no write |
| 11 Stale-binding sweep | `git grep` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256` for the superseded `release_id` `9f962ce3…`, the superseded schema digest `5af89652…`, the superseded g06 digest `bf802311…` and the superseded open-rails digest `29223e6f…` | none remain |
| 12 Tests | §8 | every rewritten, new and pinned test passes |
| 13 Candidate-wide | §§10.3–10.6 | every selected lane green locally; clean tree; attestation rehearsal |

Any change to a member byte after step 2 restarts at step 2; any change to an evidence primary restarts at step 5. Steps 4–10 are re-runnable and must be byte-stable on the second run (rehearsed).

### 5.5 Failure tokens

None added. All 17 tokens are existing governed tokens of `ERROR_TOKEN_MAP`, already regenerated into `errors/token_map/token_map.json` (F-16); `engine/compat/error_tokens.py`, `engine/compat/errors.py` and `errors/token_map/token_map.json` are unchanged, so no token-map regeneration runs.

### 5.6 CI classifier

No registration change (D-09): every touched path is already classified and owned (F-14), and the new tests live in existing homes that are already registered owners or importers. `tests/http/test_reader_post_v1.py` is a direct importer registered in `_HTTP_READER_TEST_OWNERS`, so the ownership guard (`tests/evidence/test_http_reader_ci_ownership.py`) is unaffected.

## 6. Exact file and component plan

### 6.1 Owned loci (instruction §6)

| Path | Change | Why |
| --- | --- | --- |
| `schemas/reader.v1.schema.json`, `.sha256` | `$defs.error` as §5.1, canonical bytes; sidecar refreshed | §2.24 item 1 |
| `goldens/reader/v1/g06_error_invalid_input.json`, `.sha256` | regenerated by the writer as the real 422 bytes | §2.24 item 2 |
| `scripts/make_reader_v1_goldens.py` | the g06 block (three lines) emits through `emit_public(error_envelope(…))` | §2.24 item 2 ("only where needed to emit the governed envelope") |
| `scripts/make_release_pack.sh` outputs: `artifacts/release_id.txt` (changed), `artifacts/release_pack_manifest.json` (rewritten, identical) | regenerated by running the script; the script itself is unchanged | instruction §6 |
| `engine/config/registry_loader.py` | `ADMITTED_RELEASE_VERSION` → `"1.3.0"` — nothing else | §2.24 item 3 |
| `catalog/manifest.json` | cut by the cutter only: 45 rows, `1.3.0`, `2026-08-24T18:04:49Z`; two rows change | §2.24 item 3 |
| `tests/reader_v1/test_schema.py`, `test_goldens.py`, `test_release_pack.py`; `tests/http/test_reader_post_v1.py` | §8.1–§8.4 (`test_release_pack.py` needs no edit) | instruction §6 "covering the changed seams" |
| `tests/config/test_production_admission.py`, `tests/config/test_manifest_schema.py`, `tests/config/test_registry_catalog_contract.py` | the three literal version pins (§8.5) | instruction §6 "the release, manifest and config test homes that pin the version" |
| Governed evidence companions (Index/Mirror, path proofs, config artifacts, registry report, bundles, A7, open-rails ABBA, engine-core) | only through their owning writers (§5.4) | instruction §6 |

### 6.2 Coherence dependents the re-cut forces, named as the instruction §6 requires

| Path | Change | Class |
| --- | --- | --- |
| `tools/evidence/generate_open_rails_abba_proof.py` | `FROZEN_OPEN_ABBA_SHA256` refreshed to the regenerated primary's digest (one line) | frozen-digest constant in a proof tool; PR06 (`f7484d0`) and PR06a (`dc958ec`) precedent; the instruction §6 names this class explicitly, so it is not a finding (§14.3; D-06) |

No other path outside §6.1 is needed. In particular `ci/checks/classify_ci_changes.py` (F-14), `tools/evidence/generate_a7_transport_proofs.py` (no catalog change; the proofs regenerate through its write mode), `tools/evidence/run_canonical_json_gate.py` (its roster constant is bound to `ADMITTED_RELEASE_ROSTER`) and every emitter and route are unchanged.

### 6.3 Governed evidence regenerated by owners (never hand-edited; the rehearsed set of §3.3)

Config family: `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log` (the registry report, bundles, thresholds and arrays report are byte-idempotent). Canonical JSON gate: `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`. Determinism family: `audit/gates/parity/reader_cli/{ab,ba,summary}.json`, `audit/gates/determinism/{abba.bytes,tworun_identity.sha256}`. Open-rails fixture proof: `audit/gates/determinism/open_rails_abba.json`. A7 family: `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}` (the catalog, its mirror and `.sha256`, `endpoints_snapshot.json` and `success_writers_errors.txt` are unchanged). F07 writer artifacts: `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`. Engine-core: `artifacts/core/{two_run/identity,abba/ab_ba_parity,json_compare/core_result_json_compare,purity/purity_report}.json`. Machine Mirror `artifacts/evidence_index.jsonl` and `.sha256`; the 25 path-proof siblings of the above through the sole updater. The Human Index `docs/evidence/INDEX.json` and the sanity log keep their bytes (rehearsed); if the real candidate moves either, it moves only through the updater or the sanity owner.

### 6.4 Frozen families (stay frozen, with nonclaims)

`artifacts/cli/showcompat/*`, `artifacts/cli/{ab,ba,summary}.json`, help/install captures (EPIC022 D2 / CLI conformance); `artifacts/identity/*`, `artifacts/math/*`, `artifacts/parity/two_run_identity.log`, `artifacts/bodygraph/release_bindings.json`, `artifacts/runtime/env_matrix.snapshot.json` (capture-time identity evidence regenerated only by the isolated closure inside the attestation, per `AGENTS.md`); `artifacts/vendor/*`, `audit/ops/*`, EPIC032 router captures; the §2.21 frozen captures. Their `--check` modes exit 0 on the re-cut (§3.3).

### 6.5 Consequence for CI lanes

The candidate does not change the classifier, so no full-validation trigger applies. By path: `schemas/reader.v1.schema.json`, `scripts/make_reader_v1_goldens.py`, `goldens/reader/*` and the test homes select `product`/`compat`/`release`; `engine/config/registry_loader.py` selects `product`/`compat`/`release`; `catalog/manifest.json` selects `release`; `artifacts/**`, `audit/gates/**` and the proof tool select `evidence` (+ `release` where applicable). Expected classification: `lanes=product,compat,evidence,release` with `changed_tests=true` (rehearsed, §3.3); the `db`, `rails` and `qa` lanes are not selected. The `RELEASE_NOT_ADMITTED` branches of the rails and release lanes are never taken on this candidate. The rails lane's `--check-current` of the open-rails proof is exercised locally (§10.4) even though CI does not select that lane.

### 6.6 Explicitly unchanged paths

`adapter/**` (routes, factories, `adapter/schemas/error_v1.schema.json`, `adapter/retry_after.py`), `engine/compat/**` (including `compute.py`, `error_tokens.py`, `errors.py`), `engine/presenter/emitter.py`, `presenter/reader_v1/emitter.py`, `engine/runtime/**`, `engine/bodygraph/**`, `engine/cli/main.py`, `engine/serializer/**`, `engine/stable/**`, `schemas/reader.v2.schema.json` and its sidecar, `goldens/reader/v1/g01*`, `g02*`, `g03*`, `g04*`, `g05*`, `g07*`, `goldens/reader/v2/**`, `errors/token_map/token_map.json`, `scripts/cut_release_manifest.py`, `scripts/release_id_recompute.py`, `scripts/make_release_pack.sh`, `scripts/hd_cli.py`, `ci/checks/**`, `.github/workflows/ci.yml`, `ci/jobs/*.yml`, `tools/evidence/run_canonical_json_gate.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/generate_a7_transport_proofs.py`, `tools/config/**`, `tools/errors/**`, `docs/ENDPOINTS_CATALOG.json` and its mirror, `catalog/*` data, `pyproject.toml`, `README.md`, `CHANGELOG.md` (PR07 documents the delivered schema and release), `docs/pfcanon/**`, every historical evidence family, `tests/reader_v1/test_cli_proof.py` (D-13), `tests/http/test_reader_post_v2.py`, `.audit_src/**`.

## 7. Requirement-to-change-and-test mapping

| Requirement | Source | Change | Proof |
| --- | --- | --- | --- |
| The v1 error branch requires `schema` (const `"v1"`) | §2.24 item 1; PF05 §5.2.1, §5.2.3.1 | §5.1 | §8.1 (`no_schema`, `wrong_schema_const`, `schema_case` refused; 17 pairs valid); §8.4 |
| `code`/`error` restricted to the governed pairs the v1 routes can emit, as the v2 branch does | §2.24 item 1 and proof ("every token in `ERROR_TOKEN_MAP` that the v1 routes can emit"); PF05 §5.2.3.3 | §5.1 (17 pairs, F-05) | §8.1 (`ungoverned_writer_code`, `internal_only_code`, `wrong_message` refused; pairs bound to the token map); §8.4 (17-token helper case; route-level validation) |
| `additionalProperties: false` kept; extra key refused | §2.24 item 1 and proof | §5.1 | §8.1 (`details`, `retry_after_ms`); §8.4 (`set(body) == {schema, ok, code, error}` plus schema validation) |
| `retry_after_ms` kept only if a governed emitter produces it | §2.24 item 1; instruction §5.1 | §5.2 (dropped, F-06) | §8.1 (`retry_after_ms` refused); code reading recorded in F-06 |
| Success branch unchanged; all v1 success goldens validate | §2.24 item 1 and proof | §5.1 (untouched `$defs.success`) | §8.2 (`_check_json_goldens` and `_check_jsonl_goldens` against the corrected schema); `tests/reader_v1/test_emitter.py` unchanged and passing; C1 byte proof |
| g06 regenerated through `scripts/make_reader_v1_goldens.py` as a real governed v1 error envelope; companion and release-pack outputs regenerated | §2.24 item 2 | §5.3 | §8.2 (`g06 == emit_public(error_envelope("ERR_READER_INVALID_INPUT"))`); `test_release_pack.py` byte-idempotence |
| Membership 45, admission logic unchanged; only `ADMITTED_RELEASE_VERSION` changes, to `1.3.0`; manifest cut by the cutter; `release_id` recomputed | §2.24 item 3; instruction §5.3 | §5.4 | §8.5; `tests/config/test_production_admission.py::test_actual_repository_root_admits`; cutter `--check`; `release_id_recompute.py --check-manifest-only`; the existing tampered/missing/extra-member refusals (CC-4) |
| Evidence converges through owners in PR06's order, including the engine-core owner | §2.24 item 3; O-P06a-23 | §5.4 steps 3–11 | §10.4 evidence lane; `tests/evidence/test_engine_core_evidence.py`, `test_open_rails_abba_proof.py`, `test_determinism_gate_proofs.py`, `test_canonical_json_gate_check_outputs.py`, `test_dev_conjunction_identity.py`, `tests/transport/test_a7_transport_proofs.py`; the sweep of §5.4 step 11 |
| Strict attestation builds and verifies in the release lane | §2.24 item 3 and proof | — | §10.6 |
| Reader v1 and v2 response bytes unchanged; dev `GET /reader` bytes unchanged | §2.24 proof; exclusions | §6.6 (no emitter or route change) | `test_dev_get_bytes_for_the_fixture_pair_are_unchanged`; `tests/http/test_reader_post_v2.py` unchanged and green; A7 `--check` after the write; `success_writers_errors.txt` unchanged bytes |
| Completion: code review, security review, ordinary CI on the exact head; no QA/acceptance/PF09/closure claim | §2.24 "Completion" | §§10–11 | CC-7, CC-8, CC-9 |
| `K040-REQ-012` / `AC040-08` (evidence converges through owners) | Plan v2.1; §2.23 "Requirements and acceptance effects" (unchanged by §2.24) | §5.4 | §10.4 |

Every other requirement, criterion, allocation and completion burden of Plan v2.1 and §2.23 is unchanged and untouched by this unit. No `K040-REQ` identifier is introduced or altered.

## 8. Detailed test design

No test is skipped, marked `xfail` or deselected. No new test file is created; every new case lives in an existing home the instruction names. The rehearsal applied exactly these rewrites (§3.3).

### 8.1 `tests/reader_v1/test_schema.py`

- Add `V1_DEV_ROUTE_ERROR_PAIRS` (the five dev-route pairs, rows 13–17 of §5.1) and `V1_ERROR_PAIRS = V2_ERROR_PAIRS + V1_DEV_ROUTE_ERROR_PAIRS`; add `_error_v1(code, message)` returning the four-key envelope.
- Replace `test_error_shape_valid_with_retry_after_optional` (the synthetic envelope with `retry_after_ms`, now a refusal case) with:
  - `test_v1_error_pairs_valid_and_bound_to_the_token_map[code, message]` — parametrized over the 17 pairs; each validates and `ERROR_TOKEN_MAP[code]["message"] == message`.
  - `test_v1_error_branch_is_exactly_the_reader_route_pairs` — the schema's `oneOf` pairs equal `V1_ERROR_PAIRS` (17); `required == ["schema", "ok", "code", "error"]`; `additionalProperties is False`; `properties` keys are exactly the four; `schema` is `{"const": "v1"}`; the first twelve pairs equal the v2 branch's pairs in order.
  - `test_v1_error_adverse_cases_invalid[…]` — parametrized: no `schema`; `schema: "v2"`; `schema: "V1"`; ungoverned code (`ERR_WRITER_INVALID_INPUT` with its own message); internal-only code (`ERR_M10_GATES_INVALID`); governed code with the wrong message; the retired synthetic `{"ok":false,"code":"InvalidInput","error":"bad gates"}`; `retry_after_ms`; `details`; `ok: true`; missing `error`.
- `test_additional_properties_closed_everywhere`: the error case becomes a governed envelope plus `details`.
- Every other v1 and v2 case is unchanged, including the sidecar and canonical-bytes tests, which now bind the new bytes.

### 8.2 `tests/reader_v1/test_goldens.py`

`test_v1_goldens_are_the_harmony_covenant`: the g06 assertion becomes `read_bytes() == emit_public(error_envelope("ERR_READER_INVALID_INPUT"))` plus the decoded dict `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":False,"schema":"v1"}`. `_check_json_goldens` already validates every `*.json` golden against the v1 schema, which now admits g06 (CC-1, CC-3). Everything else is unchanged.

### 8.3 `tests/reader_v1/test_release_pack.py`

No edit. The `FILES` list is unchanged; the byte-idempotence assertion holds once the regenerated pack outputs are committed (D-07).

### 8.4 `tests/http/test_reader_post_v1.py`

- Load `SCHEMA_V1` from `schemas/reader.v1.schema.json`; add `_validates_v1(raw)` (Draft 2020-12 validation) and the `V1_ERROR_TOKENS` map of the 17 tokens to their route statuses (F-05).
- `_assert_error` validates every route-level error body against the v1 schema, so every existing route-level v1 error case (version grammar, invalid input, unknown person, DB unavailable, row-contract violations, stored-row defects, admission refusal) each prove CC-1 for their token.
- `test_unprefixed_post_reader_is_the_governed_405` validates the 405 body (`ERR_NOT_FOUND`).
- New `test_every_governed_reader_v1_error_token_validates_against_the_v1_schema[token, status]`: in `create_app().test_request_context("/api/reader?v=1")`, `http_reader._error(token, status)` returns the canonical `emit_public(error_envelope(token))` bytes with exactly the four keys, `no-store`, no ETag, and the bytes validate — this covers the tokens no route-level fixture reaches (`ERR_M10_CONFIG_MISMATCH`, `ERR_M10_RESULT_SCHEMA_MISMATCH`, `ERR_M10_STALE_RESULT`, `ERR_READER_INVALID_CHART` on the production path) through the single Reader error helper both routes use.
- Dev-route cases: `test_dev_get_route_resolves_complete_fixtures_and_keeps_tz_and_conditional_contract` validates the `ERR_READER_MISSING_TZ_A` body and adds `ERR_READER_MISSING_PARAM` (no `a`/`b`) and `ERR_READER_INVALID_PATH` (a missing fixture path) with validation; `test_dev_get_route_refuses_legacy_or_incomplete_fixtures` validates the `ERR_M10_LEGACY_INPUT_UNSUPPORTED` and `ERR_M10_BODYGRAPH_INCOMPLETE` bodies; `test_production_app_env_serves_post_and_forbids_dev_get` asserts and validates the `ERR_READER_FORBIDDEN` body.
- Everything else, including `test_dev_get_bytes_for_the_fixture_pair_are_unchanged` and the real-admission-owner case (which asserts `release_id == identity_meta()["release_id"] == sha256(manifest)` and therefore the new cut), is unchanged.

### 8.5 Pinned rewrites (three tests, three files; F-10)

| File | Test | Rewrite |
| --- | --- | --- |
| `tests/config/test_production_admission.py` | `test_actual_repository_root_admits` | `ADMITTED_RELEASE_VERSION == "1.2.0"` → `"1.3.0"` |
| `tests/config/test_manifest_schema.py` | `test_generic_manifest_shape_does_not_claim_full_release_admission` | `"1.2.0"` → `"1.3.0"` |
| `tests/config/test_registry_catalog_contract.py` | `test_source_capture_detects_later_change_and_base_needs_no_mechanics_release` | `'1.2.0'` → `'1.3.0'` |

No count, roster or timestamp pin changes (45 and `2026-08-24T18:04:49Z` stay true).

### 8.6 Owner and coherence tests run unchanged

`tests/evidence/test_engine_core_evidence.py` (after the engine-core owner), `tests/evidence/test_open_rails_abba_proof.py` (after the constant refresh), `tests/evidence/test_determinism_gate_proofs.py`, `tests/evidence/test_canonical_json_gate_check_outputs.py`, `tests/evidence/test_dev_conjunction_identity.py`, `tests/transport/test_a7_transport_proofs.py`, `tests/scripts/test_cut_release_manifest.py`, `tests/config/test_execution_coherence.py`, `tests/runtime/test_identity.py`, `tests/evidence/test_release_manifest_content_binding.py`, `tests/evidence/test_sanity_pipeline.py`, `tests/evidence/test_release_attestation.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_http_reader_ci_ownership.py`, `tests/http/test_reader_post_v2.py`, `tests/reader_v1/test_emitter.py`, `tests/cli/test_errors_parity.py`.

## 9. Ordered implementation procedure (for PR-30, after the Product Owner's Proceed for this version)

One pull request and one implementation commit (D-12): an intermediate state with the schema changed but the manifest not re-cut refuses admission (`ERR_M10_MANIFEST_MISMATCH` / `RELEASE_ROSTER_MISMATCH`) on every lane, and a cut manifest with unconverged evidence is red on the evidence lane, so neither is a meaningful checkpoint. The result artifact follows in a records commit, as PR06a did. Each checkpoint ends with the listed proof; a failing proof stops the procedure at that checkpoint and never proceeds by hand-editing.

### C0 — Preconditions (not implementation)

- Product Owner PR-30 Proceed for exactly this plan version. PR-30 inspects existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06b before creating anything: at planning time none exist; the PR-20 planning branch holds only this document and is not an implementation vehicle.
- Environment as §10.1, including the absent vendor/DB keys and the `python`-on-`PATH` rule; `origin/main` re-verified against `870fe5d`; any non-documentation change since then re-evaluated against §3.2 before starting.

### C1 — Source edits (§§5.1–5.4, step 1)

1. Write `schemas/reader.v1.schema.json` with `$defs.error` exactly as §5.1 (build it programmatically from the 17 pairs and serialize the whole document with `sercanon(doc, sort_keys=True)`); refresh the sidecar in `sha256sum` format.
2. Edit the g06 block of `scripts/make_reader_v1_goldens.py`; run `python scripts/make_reader_v1_goldens.py`; run `bash scripts/make_release_pack.sh`.
3. `engine/config/registry_loader.py`: `ADMITTED_RELEASE_VERSION = "1.3.0"`.
4. Proof: `sercanon(json.loads(raw)) == raw` for the schema and the sidecar digest equals the file; `git diff --exit-code -- goldens/reader/v1/g01_minimal_ineligible.json goldens/reader/v1/g02_ab_ba_parity_A.jsonl goldens/reader/v1/g02_ab_ba_parity_B.jsonl goldens/reader/v1/g03_harmony_open.json goldens/reader/v1/g04_harmony_warm.json goldens/reader/v1/g05_harmony_cool.json goldens/reader/v1/g07_harmony_glow.json goldens/reader/v2 artifacts/release_pack_manifest.json` exits 0; g06 bytes equal `emit_public(error_envelope("ERR_READER_INVALID_INPUT"))`; `artifacts/release_id.txt` changed; `git diff -- engine/config/registry_loader.py` is exactly one changed line. From this point the tracked manifest no longer matches two members, so admission refuses until C2 — run no admission-bound test before C2.

### C2 — Cut (§5.4, steps 2–3)

1. Confirm every member byte is final; cut; recompute check; cutter `--check`; record `release_id`.
2. `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; b=l(); print(b.release_id, len(b.source_identities), b.manifest.version)"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json`.
3. Proof: `AdmittedMechanicsBundle`, `1.3.0`, 45; `identity_meta()["release_id"]` equals the recorded value and the manifest digest; the golden report is `ok: true` with no mismatch.

### C3 — Tests of the changed seams (§8)

1. Apply §8.1, §8.2, §8.4 and §8.5.
2. Run `python -m pytest -q -p no:cacheprovider tests/reader_v1/test_schema.py tests/reader_v1/test_goldens.py tests/reader_v1/test_emitter.py tests/reader_v1/test_release_pack.py tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/config/test_production_admission.py tests/config/test_manifest_schema.py tests/config/test_registry_catalog_contract.py tests/config/test_execution_coherence.py tests/scripts/test_cut_release_manifest.py tests/runtime/test_identity.py`.
3. Proof: every case green; `git status` clean after `test_release_pack.py` (it reruns the pack script); no `skip`, `xfail` or deselect added. `tests/reader_v1/test_cli_proof.py` is not in this roster (D-13) and fails for its own pre-existing reason if run.

### C4 — Convergence (§5.4 steps 4–11)

1. Steps 4–10 in order; after step 7 refresh `FROZEN_OPEN_ABBA_SHA256` from the regenerated primary and re-run that owner's `--check`; run the engine-core owner (7b); after step 8 every read-only check; step 9 sanity (non-canonical first); step 10 frozen families; step 11 sweep.
2. Run `python -m pytest -q -p no:cacheprovider tests/evidence/test_engine_core_evidence.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_dev_conjunction_identity.py tests/transport/test_a7_transport_proofs.py tests/evidence/test_sanity_pipeline.py tests/evidence/test_release_manifest_content_binding.py`.
3. Proof: `git status --short --untracked-files=all` shows only intended paths (the 65-path footprint of §3.3 is the expectation; any other path is a finding to record, never to hand-edit); a second run of steps 4–10 changes no byte; the sanity log equals the tracked PASS model byte for byte; the sweep finds nothing.

### C5 — Candidate-wide validation and attestation rehearsal (§§10.3–10.6)

1. Classifier dry run; changed-test isolation; the lane-equivalent commands of §10.4 for the selected lanes (and the three unselected lanes as a prudence check); the supplemental roster of §10.5.
2. Attestation rehearsal of §10.6 from a clean committed tree into an external empty directory, then `--verify`. A failure is a finding to record, never something to patch around.
3. Proof: every command exit 0; clean tree after every isolated run.

### C6 — Publication (PR-30's `PR_CANDIDATE_PUBLISHED`)

1. One implementation commit on the working branch (schema and sidecar; writer, goldens and pack outputs; version constant and manifest; converged evidence and the constant refresh; tests), locally tested; the PR description per `.github/pull_request_template.md` and `AGENTS.md` (Why / What changed / Checks run / Not in this PR / What merging does) with the §15 merge statement; then the records commit with the `PR_IMPLEMENTATION_RESULT` under `docs/ephemeral/` naming every command run and its exit code, the before/after digests of both changed members, the schema and g06 bytes, the `release_id`, the `FROZEN_OPEN_ABBA_SHA256` value, the engine-core and A7 artifact digests, the attestation outcome, the classifier outputs, the *In-flight decisions* section, and what was not executed.
2. Hand off to PR-35 in its own dedicated session. PR-35 owns review correction, current-head CI, coherent corrective pushes and `MERGE_PENDING`; Nathan merges.

Recovery at any checkpoint: revert the compatible set together (schema, writer, goldens, pack outputs, constant, manifest, evidence, tests) with `git restore` on the branch; re-run the owners on unchanged inputs; if a member byte changed, restart at C2. Nothing is hand-edited; nothing is claimed that an owner did not produce.

## 10. Local validation and evidence commands

### 10.1 Environment (as `.github/workflows/ci.yml` installs, plus what the rehearsal needed)

```
python --version                      # CI: 3.12 (actions/setup-python); the rehearsal used 3.11.15
python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version            # readiness proof (AGENTS.md)
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
unset HD_API_BASE_URL HDAPI_BASE_URL HD_API_KEY GEO_API_KEY DATABASE_URL DEV_SAMPLER_URL GH_TOKEN   # for the whole session
```

Two facts PR-30 must respect (F-20): `python` on `PATH` must be the interpreter that carries pytest (`ci/checks/run_rails_job_definitions.py` shells out to `python -m pytest`); the editable install must point at the tree being attested (the scripts the attestation runs inside its isolated copy import `engine` from the installed location). A virtualenv created inside the working tree's parent with `-e <working tree>` satisfies both (rehearsed).

### 10.2 Focused behavioral and ownership suites

```
python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_dev_conjunction_http.py tests/http/test_compat_endpoint_contract.py tests/reader_v1/test_schema.py tests/reader_v1/test_goldens.py tests/reader_v1/test_emitter.py tests/reader_v1/test_release_pack.py tests/runtime/test_identity.py tests/runtime/test_emit_public_legacy_helper.py tests/transport/test_a7_transport_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_sanity_pipeline.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_release_attestation.py tests/config/test_production_admission.py tests/config/test_manifest_schema.py tests/config/test_execution_coherence.py tests/config/test_config_artifacts.py tests/scripts/test_cut_release_manifest.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_errors_parity.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_http_reader_ci_ownership.py tests/evidence/test_engine_core_evidence.py tests/config/test_registry_catalog_contract.py
```

### 10.3 Classifier dry-run and changed-test isolation (as `ci.yml` runs them)

```
python ci/checks/classify_ci_changes.py --base <full SHA of origin/main> --head <full SHA of HEAD> --event-name pull_request --github-output /tmp/gh_out.txt --changed-tests-output /tmp/changed_tests.txt
# expect product=true compat=true evidence=true release=true, db/rails/qa=false, changed_tests=true, reason=selected_lanes,
# and no CI_CHANGE_SURFACE_UNCLASSIFIED / CI_PRODUCT_OWNER_TEST_MISSING / CI_EVIDENCE_OWNER_TEST_MISSING. Full 40-hex SHAs are required.
git worktree add --detach /tmp/pr06b-changed-tests HEAD && (cd /tmp/pr06b-changed-tests && PYTHONPATH=$PWD python -m pytest -q -p no:cacheprovider -- $(cat /tmp/changed_tests.txt) && git diff --exit-code && test -z "$(git status --short --untracked-files=all)")
```

### 10.4 Lane-equivalent validation (commands verbatim from `.github/workflows/ci.yml`, in lane order)

product: `python tools/order/generate_ordering_artifacts.py --check`; `python -m pytest -q tests/order tests/mech/test_order_properties.py tests/evidence/test_architecture_snapshot.py`.
compat: `ci/checks/check_cli_help.sh`; `python tools/cli/serializer_grep_guard.py --output <tmp>/serializer_grep_guard.log`; `python tools/cli/emitter_symbol_proof.py --output <tmp>/emitter_symbol_proof.txt`; `python -m pytest -q tests/adapter/test_jsonschema.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_errors_parity.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_serializer_guards.py tests/transport/test_internal_version_contract.py tests/http/test_compat_endpoint_contract.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py`.
evidence: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/refresh_step_logs_manifest.py --check`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_final_lf.sh`; `python -m pytest -q tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_skeleton.py tests/evidence/test_machine_mirror_self_proof.py tests/evidence/test_orientation_demo.py tests/ops/test_evidence_index.py tests/qa/test_epic020_qa_docs.py`.
release: `git diff --exit-code`; `python scripts/release_id_recompute.py --check-manifest-only`; `python -m pytest -q tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` in a detached worktree with the clean-tree assertion; then §10.6.
Prudence (not selected by the classification for this candidate, run locally anyway): db — `python ci/checks/check_direct_db_contract.py` and its pytest set; rails — `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` (must exit 0, never 3) and `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`; qa — the workflow's qa pytest set in a detached worktree with the clean-tree assertion.

### 10.5 Candidate-wide roster

`_FULL_VALIDATION_SUPPLEMENTAL_TESTS` from `ci/checks/classify_ci_changes.py` (the 40-path list), plus every home of §8 and §10.2. Do not run bare `pytest tests`: it collects legacy modules that fail at import and proves nothing (PR06 plan §10.5; F-06 names two of them).

### 10.6 Attestation rehearsal and the recorded planning outcome

```
python tools/evidence/build_release_attestation.py --output "$RUNNER_TEMP/hde-release-attestation" --require-clean
python tools/evidence/build_release_attestation.py --verify "$RUNNER_TEMP/hde-release-attestation" --require-clean
git diff --exit-code && test -z "$(git status --short --untracked-files=all)"
```

Planning rehearsal record (scratch clone at the converged `1.3.0` cut, committed there; inference support only): build exit 0; `--verify` exit 0; `release_admission PR06R_B_FINAL_PASS`; `validation_result PASS`; `release_id` equal to the scratch manifest digest (`52be4558…`); 174 files bound; 14 declared outputs under `omitted_files` with the builder's existing secret-safety reason codes (the same count PR06 and PR06a recorded); tree clean afterwards; 89 seconds. The attestation on the real candidate remains `NOT EXECUTED` until PR-30 runs it (C5) and CI runs it in the release lane.

### 10.7 Result record

PR-30 writes `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.0.md` with: every command of §§10.2–10.6 and its exit code; the before/after digests of the two changed members and the two sidecars; the manifest bytes and `release_id`; the g06 bytes; the golden report digest; the A7, F07 and engine-core artifact digests; the `FROZEN_OPEN_ABBA_SHA256` value; the sanity log model and its binding; the attestation bundle digest (or its failure receipt); the classifier outputs; the pre-existing `test_cli_proof` failure; not-executed items with reasons; the *In-flight decisions* section; and the same distinctions (verified / inferred / not produced / not executed) this plan uses.

## 11. Code review and security review checklist

### 11.1 Code review (PR-session, on the current substantive change)

- Schema: the file is canonical bytes; only `$defs.error` differs from `main` (diff the parsed documents key by key: `$defs.success`, `category`, `category_id`, `band`, `hex64`, `meta`, root `oneOf`, `$id`, `$schema`, `title` identical); the 17 pairs are exactly F-05's, in §5.1's order, each equal to the token map; `required`, `additionalProperties`, `schema` const as §5.1; no `retry_after_ms`, no `details`, no `minLength`; sidecar in `sha256sum` format and equal to the file.
- Goldens: g06 produced by the writer, not by hand, and equal to the route's 422 bytes; every other golden byte-identical to `main`; the pack outputs equal a fresh script run; no `_leader`, no synthetic `InvalidInput` remains anywhere but the frozen `.audit_src/` snapshot.
- Re-cut: `registry_loader.py` diff is exactly one line; manifest diff is exactly two rows plus `version`; `built_at_utc` unchanged; roster 45; `release_id_recompute.py --check-manifest-only` and the cutter `--check` exit 0; `identity_meta()["release_id"]` equals the manifest digest; no other member's bytes changed.
- Evidence: every changed artifact under `artifacts/` and `audit/` is on the owner-written list of §6.3 or its path proof; each owner's `--check` exits 0 on the committed head; a second run changes no byte; the Human Index and the sanity log are unchanged or moved only by their owners; `FROZEN_OPEN_ABBA_SHA256` equals `sha256sum audit/gates/determinism/open_rails_abba.json`; the sweep of §5.4 step 11 finds nothing.
- Tests: the rewrites are exactly §8; no `skip`, `xfail` or deselect added; `V1_ERROR_PAIRS` is derived from `V2_ERROR_PAIRS` plus the five dev-route pairs, not a second hand-copied list of the twelve; the 17-token helper case reaches every token through `_error`; the three literal pins read `1.3.0`.
- Unchanged surfaces: `adapter/http_reader.py`, `engine/compat/*`, the emitters, `schemas/reader.v2.schema.json`, `token_map.json`, `ci/checks/classify_ci_changes.py`, `ci.yml` are byte-identical to `main`.
- PR description follows the template and states §15's "What merging does".

### 11.2 Security review (a public contract and the unchanged route surface; instruction §11)

- The schema is a public contract. The change **narrows** what the v1 error branch accepts (governed pairs only, `schema` required, no `retry_after_ms`) and admits exactly the bytes the routes already emit; no new field, no numeric, no free-text `error` outside the governed messages, no PII, path, UUID, Gate, configuration or database detail in any envelope (PF05 §5.2.3.1). A client validating v1 errors against the published schema starts accepting real errors; a client that depended on rejecting them is not expected and returns to change control if found (instruction §11).
- Route surface unchanged: the bounded body read, the two-UUID grammar, the read-only parameterized lookup, value-free refusals, `no-store` on every error, no ETag on POST or errors, the governed 405s and the dev gate are byte-identical to `main` (§6.6); the review confirms this by diff, and the unchanged `tests/http/test_reader_post_v2.py` (66 cases including the 30 method-refusal cases) and the A7 `--check` prove it by execution.
- Goldens and evidence carry the public admitted identity and governed messages only; no secret, birth, Gate or credential value (the attestation's retained-text safety check and the keys-only redaction job run unchanged).
- The re-cut changes no admission logic; the PF10 §2.12 executable-equivalence and roster checks are untouched and are proven by the unchanged adverse tests (CC-4).
- No live vendor or database action anywhere in the procedure; the only open-rails command is the fixture-mode ABBA proof with the keys absent (§10.1).
- Attestation output only to an external empty directory; nothing written inside the repository by the builder.

## 12. Risk register and recovery

| ID | Risk | Treatment |
| --- | --- | --- |
| R-01 | A member byte changes after the cut (a review correction to the schema, or any edit to `registry_loader.py`) | any member change ⇒ re-cut (C2) and restart convergence at §5.4 step 4; the cutter `--check` and `--check-manifest-only` in the release lane catch a stale cut; admission refuses it on every lane |
| R-02 | PR-30 reproduces an equivalent but differently ordered `oneOf`, so the schema digest and `release_id` differ from the rehearsal | not a defect; §5.1 fixes the order so the rehearsal digests reproduce; the result records the real values either way |
| R-03 | `FROZEN_OPEN_ABBA_SHA256` not refreshed ⇒ `test_open_rails_abba_proof.py`, sanity stage 06 and the rails lane red | §5.4 step 7; §8.6; rehearsed |
| R-04 | Engine-core owner omitted ⇒ stale `release_id` and stale `registry_loader.py` digest in `artifacts/core/**`, undetected by the currency test (O-P06a-23) | §5.4 step 7b is mandatory; the sweep of step 11 catches the stale `release_id` |
| R-05 | Sanity canonical run binds the FAIL model after a transient failure | PR06 plan §5.8 pre-binding; the non-canonical run first; never hand-edit the log |
| R-06 | `test_release_pack.py` rewrites tracked artifacts in CI's worktree | the pack outputs are committed after the final golden and schema bytes (D-07); the test asserts byte-idempotence |
| R-07 | A test elsewhere pins the synthetic g06 or the old error shape | F-09 found exactly two homes, both rewritten (§8.1, §8.2); the focused suites and the changed-test isolation would surface any other |
| R-08 | CI Python 3.12 vs local 3.11 | lane-equivalent runs are evidence of behaviour, not of CI; CI on the exact head remains the record |
| R-09 | Vendor or DB credentials present in the developer's environment turn the open-rails proof or an F07 test into a live call or a write | §10.1 unsets them for the session; the F07 generator refuses open rails and neutralizes `DATABASE_URL`; the open-rails ABBA proof runs in fixture mode |
| R-10 | PF05 §5.2.3.2's `invalid Reader chart` is read as the required message and the branch or the token map is "corrected" to it | the branch binds to the emitted bytes and the token map (F-17, PR06a IF-01); a message change would change response bytes, which §2.24 excludes; O-P06b-01 carries the discrepancy |
| R-11 | `tests/reader_v1/test_cli_proof.py` is mistaken for a PR06b regression | pre-existing baseline failure (F-19), untouched (D-13), recorded in the result; in no lane or roster |
| R-12 | Attestation rehearsal blocked by the packaging environment | §10.1 (F-20); record the environment in the result |
| R-13 | PR07 or OPS01 assume the `1.2.0` release | §2.24 "Work-unit effects": PR07 documents the v1 schema as PR06b delivers it; OPS01 verifies `1.3.0`; §15 states the merge-order dependency |

Recovery: roll back the compatible set together on the branch; re-run owners on unchanged inputs; re-cut on member change; on convergence failure claim nothing and hand-edit nothing. The unit's own recovery after landing is a revert of the squash commit, which restores `1.2.0` (instruction §11); there is no data migration.

## 13. Carried `CANON_CONFLICT_REGISTER` and observations

### 13.1 `CANON_CONFLICT_REGISTER` (carried from Plan v2.1 §11, Plan Review v2.1 §6, PF10 §§2.2–2.5, 2.19, 2.20, 2.22, 2.23, 2.24, the PR06b decision §5 and the instruction §12; no entry reopened, relabeled, omitted or newly decided here)

| Entry | Classification / status | Decision lineage | PR06b note |
| --- | --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z (PF10 §2.2) | carried |
| C040-02 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried; current controlled PF12 is repository v2.9.5 (§2.2) |
| C040-03 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-04 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-05 | `CANON_RECONCILIATION` / `APPROVED`, alternative A | Isis-49, 2026-09-09T03:57:16Z (PF10 §2.3) | carried; PF14 §6.7 correction pending, non-gating |
| C040-06 | `NEW_CANON` / `APPROVED`, alternative A | Isis-50, 2026-09-09T11:48:08Z (PF10 §2.5) | carried; PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |
| C040-07 | `NEW_CANON` / `APPROVED` by the Product Owner, 2026-09-26 (PF10 §2.23) | public full Magic-10 via Reader v2; Reader v1 unchanged | delivered by PR06a; drainage into PF01, PF04, PF05, PF12 (and PF14/PF29 statements) pending with their maintainers, non-gating |
| C040-08 | `CANON_RECONCILIATION` / **`APPROVED`, alternative A** | the retained whole-change IA by Product Owner direction, 2026-09-26 (`docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md`; PF10 §2.24) | **the conflict this unit implements**: PF05 §5.2 (the four-key envelope with `schema`) governs the Reader v1 error branch; PF01 §2.3 and PF04 §8.1.2 drainage to admit `schema` belongs to their maintainers and is pending and non-gating for PR06b (decision §5) |

No new register entry is proposed by this plan. O-P06b-01 (below) is carried to the register owner as a candidate for its own disposition; it is not entered here.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner |
| --- | --- | --- |
| O-P06b-01 | PF05 §5.2.3.2 lists the exact message of `ERR_READER_INVALID_CHART` as `invalid Reader chart`; the governed token map, `token_map.json`, the v2 schema (PR06a IF-01) and the emitted bytes carry `invalid reader payload`. This unit binds the v1 branch to the emitted bytes and the token map, as §2.24 item 1 directs ("as the v2 branch does"), and changes no message. Whether PF05's table or the token map is corrected is a PF05-maintainer / register-owner disposition | the whole-change IA (register owner); PF05 maintainer |
| O-P06b-02 | `adapter/retry_after.py::parse_retry_after_ms` has no importer, and `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py` / `test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py` call routes that do not exist (`/_test/429_*`); they are in no CI lane. Legacy remnants of the retired `retry_after_ms` transport; untouched by this unit | Product Owner / legacy adapter owner (PR07 or the IA backlog) |
| O-P06b-03 | `ERR_M10_GATES_MISSING` and `ERR_M10_GATES_INVALID` carry Reader statuses in `MAGIC10_HTTP_STATUS` but are unreachable from either Reader route (`BOUNDARY_REASONS` maps `gates_*` to `ERR_M10_BODYGRAPH_INCOMPLETE` on the Reader transport, as PF05 §5.2.3.1 assigns them to internal/CLI rows). They are correctly excluded from the v1 branch; the unused statuses are cosmetic | error-token owner |
| O-P06b-04 | Dev `GET /reader`'s `_safe_load_chart` catches `FileNotFoundError` only; another `OSError` (permission, symlink loop) would surface as a framework 500, not a governed envelope. Pre-existing, dev-only, outside §6 | HTTP transport / PF05 owner (adjacent to O-P06a-22) |
| O-P06b-05 | PF12 §5.1 records `1.1.0` / `2026-08-24T18:04:49Z` for the adopted cut; `1.2.0` is a C040-07 drainage item and `1.3.0` follows it. The re-cut reuses `built_at_utc` because admission compares it to a constant the instruction bounds this unit not to touch (D-05, as PR06a O-P06a-08); a fresh timestamp would be a Product Owner / PF12 decision | PF12 maintainer; Product Owner |
| O-P06b-06 | `artifacts/core/purity/purity_report.json` changes on this re-cut (its `source_sha256` includes `registry_loader.py`, F-12) although PR06a's PR-35 re-cut left it unchanged; a future re-cut that touches no engine-core source will again leave it unchanged. The currency test still does not check `release_id` (O-P06a-23 stands) | evidence owners / plan authors |
| O-P06b-07 | `docs/pfcanon/` holds six PF10 files (`v13.3` through `v13.3.5`); only v13.3.5 is read (instruction N-01) | Nathan |
| O-P06b-08 | `scripts/hd_cli.py` reads the legacy release-pack `artifacts/release_id.txt`, whose bytes this unit regenerates; `tests/reader_v1/test_cli_proof.py` keeps failing for its own reason (`ADMIN_FLAG_REQUIRED`; O-P06a-03) | Product Owner / legacy script owner |
| O-P06b-09 | `adapter/schemas/error_v1.schema.json` (draft-07, allows `details`) and the Reader v1 branch (2020-12, no `details`) now agree on the four required keys; PF05 §5.2.3.3 keeps the adapter schema unchanged unless its parity check proves a mismatch — none is claimed | PF05 / PF12 maintainers |
| O-P06b-10 | Inherited and carried unchanged: CR-03 / O-P06a-22 (framework HTML 404 for unknown paths on two factories), O-12 / CR-01 (packaged wheel omits `schemas/**`), O-P06a-03 (`hd_cli.py`), O-P06a-11 (the frozen open-rails digest coupling refreshed again here), O-P06a-12 (`python` on `PATH`) | their recorded owners |
| O-P06b-11 | `.audit_src/` holds a frozen copy of the pre-PR06 v1 schema and synthetic g06 (with `retry_after_ms`); it is a legacy audit snapshot, not a consumer, and is untouched | Product Owner |
| O-P06b-12 | The rehearsal ran on Python 3.11.15; CI runs 3.12 (R-08) | — |

## 14. Boundary findings, planning decisions and boundary classification

### 14.1 Findings

No `FINDING_REF` is raised. No material boundary (PR-20's definition: outcome/objective, acceptance criteria, protected architectural/security/data-model/external-contract boundary, several units' scope, accepted dependency, budget/schedule/risk) was found beyond what §2.24 already decides: the public-contract change to the v1 error branch **is** the approved delta of C040-08 / PF10 §2.24. No required change falls outside the owned loci (§14.3). `PR_RETURN_PHASE` does not apply; RS-40 is ineligible. O-P06b-01 is carried to the whole-change IA as a non-gating candidate register item, not as a finding, because it requires no change in this unit.

### 14.2 Planning decisions (D-xx) and their boundary classification

| ID | Decision | Classification |
| --- | --- | --- |
| D-01 | The v1 error branch admits exactly the 17 governed pairs the two v1 routes can emit: the production route's twelve (the v2 branch) plus the dev route's five | in scope — §2.24 proof: "every token in `ERROR_TOKEN_MAP` that the v1 routes can emit"; PF05 §5.2.4.1 names the five |
| D-02 | `retry_after_ms` removed | in scope — §2.24 item 1's condition is established false by F-06; PF05 §5.2.3.1 |
| D-03 | The branch mirrors the v2 branch's structure (`properties`, `required`, `additionalProperties`, `oneOf`) and keeps its `title` | in scope — "as `schemas/reader.v2.schema.json`'s error branch does" |
| D-04 | g06 emitted through `emit_public(error_envelope("ERR_READER_INVALID_INPUT"))`; filename unchanged | in scope — §2.24 item 2 ("through `scripts/make_reader_v1_goldens.py` as a real governed v1 error envelope") |
| D-05 | `built_at_utc` kept at `2026-08-24T18:04:49Z` | in scope — instruction §5.3 ("keeps PR06a's timestamp unless the plan justifies otherwise"; F-01 shows a change would need the bounded constant); O-P06b-05 |
| D-06 | `FROZEN_OPEN_ABBA_SHA256` refreshed | coherence dependent named as the instruction §6 requires; PR06/PR06a precedent; not material |
| D-07 | `scripts/make_release_pack.sh` run after the final bytes; its two outputs committed | in scope — instruction §6 "outputs regenerated by the script" |
| D-08 | The engine-core owner runs in the convergence order | in scope — §2.24 item 3 ("including the engine-core owner, per O-P06a-23") |
| D-09 | No classifier change | in scope by omission — every path already classified and owned (F-14); the classifier is not an owned locus and needs no change |
| D-10 | Route-level validation through `_assert_error` plus a 17-token helper case through `_error`, all in `tests/http/test_reader_post_v1.py`; no new test file | in scope — instruction §6 test homes; covers tokens no fixture reaches |
| D-11 | The three literal version pins rewritten to `1.3.0` | in scope — "the release, manifest and config test homes that pin the version" |
| D-12 | One PR, one implementation commit plus a records commit | in scope |
| D-13 | `tests/reader_v1/test_cli_proof.py` and `scripts/hd_cli.py` untouched despite the baseline failure | in scope by omission (O-P06a-03; inherited, instruction §8) |
| D-14 | The pair order is fixed (§5.1) so PR-30 reproduces the rehearsal bytes | in scope; reproducibility, no semantic effect |

No decision here rewrites the Plan, mints a Proceed, reruns an accepted unit, edits PF-Canon, decides a Canon conflict or merges.

### 14.3 Paths outside the instruction's §6 list, classified

The instruction §6 lists the owned loci, admits governed companions "only through their owning writers", and states that coherence dependents the re-cut forces, "such as frozen-digest constants in proof tools, follow the PR06a precedent and must be named in the plan"; any other required file is a finding (§9). Exactly one path outside the literal list is needed, and it is of the named class:

| Path | Why it is not an implicit extension |
| --- | --- |
| `tools/evidence/generate_open_rails_abba_proof.py` | the frozen-digest constant of a regenerated governed primary; the re-cut cannot converge without it (F-13); PR06 and PR06a landed the same one-line refresh; the instruction names this class and requires it to be named here |

Every other changed path is a listed locus, a listed test home, a script output the instruction lists, or a governed companion written by its owner (§6.3). No finding is routed, and the state `AWAITING_PO_PROCEED` stands on this classification.

## 15. Manual merge and post-implementation boundary

- Merge is Nathan's alone. PR-30 ends at `PR_CANDIDATE_PUBLISHED`; PR-35 ends at `MERGE_PENDING — Ready to merge`; PR-40 runs after `MERGE_OBSERVED` (or Nathan's assertion where no such result exists) with the retained IA in its read-only role.
- **What merging does.** Merging PR06b makes the corrected Reader v1 schema (its error branch admitting exactly the 17 governed envelopes the v1 routes emit, `schema` required, `retry_after_ms` removed), the real g06 error golden and regenerated release-pack outputs, and the 45-member `1.3.0` release with its recomputed `release_id` and converged evidence current on `main`. Reader v1 and v2 response bytes do not change. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-08 drainage into PF01 §2.3 / PF04 §8.1.2, C040-07 drainage, deployment, activation, Epic closure. The PR description states this under "What merging does", following `.github/pull_request_template.md` and `AGENTS.md` (Why / What changed / Checks run / Not in this PR / What merging does).
- Merge-order dependency: none upstream in code (PR06a landed as `d79cfc1`; the instruction landed as `870fe5d`); PR07 must follow PR06b and documents the v1 schema as PR06b delivers it; OPS01 requires all nine PR units and verifies the `1.3.0` release (§2.24 "Work-unit effects").

## 16. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR06b-01`; prior entries carried by reference: `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR06b-01` (instruction §13), `GCFPE-USE-HDE-EPIC040-RS-20-20260926-PR06b-01` (decision §7), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06a-01` (PR06a review §6).

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204` (body as read at invocation, page as of 2026-09-24T15:46:52.719Z; Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06b; Specification v1.1; instruction v1.0.
- Role / stage: dedicated PR06b PR-development session / PR-20.
- Captured: 2026-09-26T14:10:12Z (planning inspection began at approximately 2026-09-26T13:36Z; rehearsal 13:46–14:04:38Z).
- Execution identity: harness session `https://claude.ai/code/session_018Zth7shEF7GFWMU8jgFUjZ`.
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent (only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md` exist there); `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

- Receiver: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`; the same dedicated PR06b session (`RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06b / PR-30`; `context_conflict: NONE`).
- Gate: Nathan / Product Owner's manual PR-30 Proceed for exactly `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR06b-PR-INSTRUCTION` v1.0. `AWAITING_PO_PROCEED` is not implementation approval and authorizes no merge, publication, Ops or QA.
- Inputs by repository path: this plan (`docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md`); `docs/ephemeral/HDE-EPIC040-PR06b-pr-instruction-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` (the overlay, PF10 §2.24); `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.1.md` (the convergence precedent); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` (§§2.12, 2.21, 2.23, 2.24); the immutable bases of §2.1.
- PR-30 obligations carried: inspect authorized local roots, repository state, existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06b before creating anything (none exist at planning time; the PR-20 planning branch holds only this document and is not a PR06b implementation vehicle); resume the most advanced consistent state; challenge assumptions and the boundary cases of §8; implement only §§5–6 in the order of §9; test locally per §10 with the keys of §10.1 absent, including the attestation rehearsal; form one coherent locally tested implementation commit and a records commit; deliberately publish the initial candidate; `PR_CANDIDATE_PUBLISHED`; hand off to PR-35 in its own dedicated session naming the `PR_IMPLEMENTATION_RESULT` and the PR reference.
- PR-35 obligations carried: review retrieval and correction, local retesting, coherent corrective pushes, CI economy, current-head identity, required checks or a valid waiver, mergeability, genuine merge readiness, a Security Review on the corrected head where a correction lands; no merge. Nathan merges; PR-40 follows `MERGE_OBSERVED`.

### 17.2 Routes not taken

No RS-10 package is emitted: no material boundary was found (§14.1). No `PR_RETURN_PHASE` or RS-40 applies. PR-50 is Nathan's alone and is not a destination.

### 17.3 State summary (truthful states)

| Item | State |
| --- | --- |
| This plan | `AWAITING_PO_PROCEED` — complete, executable within approved scope plus PF10 §§2.12, 2.21, 2.23, 2.24; pending the Product Owner's PR-30 invocation for v1.0 |
| Boundary finding | none raised; one coherence dependent classified in §14.3; O-P06b-01 carried to the IA as a non-gating candidate |
| PR06b implementation, PR, CI, reviews, merge | `NOT EXECUTED` |
| PR06b result artifact, PR07, OPS01, QA, Ops, activation, C040-08 drainage, closure | `NOT PRODUCED` / `NOT EXECUTED` |
| Real `release_id`, real evidence bytes, real attestation | `NOT PRODUCED` (rehearsed in a scratch clone only, §3.3, §10.6) |
| Provenance persistence | `PENDING / NON_GATING` |
