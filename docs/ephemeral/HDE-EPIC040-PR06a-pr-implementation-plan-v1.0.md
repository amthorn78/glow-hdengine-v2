---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06a
pr_instruction_id: HDE-EPIC040-PR06a-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
planning_inspection_capture_utc: 2026-09-26T03:11:48Z to 2026-09-26T04:02:51Z
next_stage: PR-30 (Product Owner Proceed required first)
---

# HDE-EPIC040-PR06a — PR Implementation Plan v1.0

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN` |
| version | `v1.0` — first issue; no predecessor plan exists for this unit |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the applicable PF10 overlays (§2.3); no boundary finding raised (§14.3); pending Nathan / Product Owner's exact PR-30 invocation against this version |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md` |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR06a` — Reader v2 full Magic-10 exposure, the deferred Reader contract work (F03, F05, F07) and the 45-member release re-cut |
| PR_INSTRUCTION_ID | `HDE-EPIC040-PR06a-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md`, SHA-256 `b6e1c663fe19a073e519ef57455701d1b437c0fb9c12d284b4b0d6fb83220fcb`, 12,599 bytes, blob `e6c129cc01fd010e677719b6715cf3563cc2ce43`. At planning time it is **not on `main`**: it is the single file of open PR [#506](https://github.com/amthorn78/glow-hdengine-v2/pull/506) (head `dd9b9a8e9549bb10b742a9123305f00f73b9a969`, created 2026-09-26T03:09:06Z). It was read completely from that head; its lineage is preserved as supplied |
| IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1, immutable approved base, `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| SPECIFICATION_ID | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| IMPLEMENTATION_AUDIT_ID | `HDE-EPIC040-IMPLEMENTATION-AUDIT` v2.0, `AUDIT_COMPLETE`, `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md`, SHA-256 `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` |
| PLAN_REVIEW_ID (original, preserved) | `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`, SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Applicable overlay decision | `HDE-EPIC040-PR07-F01-RESCOPE-DECISION` v1.0, `APPROVE` option 1, decided by Isis-50 on the Product Owner's delegation (route `GCF-17.RESCOPE`, 2026-09-26T02:55:39Z), `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md`, SHA-256 `0c3d4ad718cbed410f1d248fcea5f1772b140bd06bc2866bc0ecc4257a7e8a55`; with its one addendum `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`, SHA-256 `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9`, drained as PF10 §2.23. Also effective within their scopes: PF10 §2.12 (PR03-R02 admission boundary), §§2.16–2.18 (the F03/F05/F07 deferrals, return point reassigned to this unit), §2.21 (PR06-F01 frozen-capture identity). No `REMEDIATION_REVIEW` applies |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR06a |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` (this PR-20 run); PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `NOT_YET_ASSIGNED` — the handoff named no reference and the operator assigned none; no platform ID is invented. Known runtime identity from the harness: `https://claude.ai/code/session_01EBvvgYQTXQqvSpd2eHtK8V` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR06a` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| Authority boundary | This plan authorizes nothing. Implementation waits for the Product Owner's PR-30 Proceed for this exact version; merge is Nathan's alone; QA, Ops, acceptance, release activation, deployment, PF-Canon edits (including C040-07 drainage), PF09 movement and Epic closure are outside it (instruction §§4, 8, 10; overlay "Preserved exclusions and nonclaims") |

## 2. Exact controlling lineage and source record

### 2.1 Approved and accepted change lineage

| Role | Artifact | Identity used here |
| --- | --- | --- |
| Approved bases | Specification v1.1; Implementation Audit v2.0; immutable Plan v2.1; Plan Review v2.1 Isis-50 `APPROVE` | read; Plan §6.7 (PR07 boundary) and §6.8 (OPS01) are what the overlay amends by addition; §11 carries the register |
| Product Owner decision | Public Reader exposes the full Magic-10 set (2026-09-26), recorded in the decision §2 and the overlay | supersedes, for HDE-EPIC040, the Specification v1.1 exclusion "No public ten-category expansion"; the numeric-result exclusion stands (overlay "Requirements and acceptance effects") |
| Accepted predecessors | PR01 v1.1, PR02–PR05 v1.0 and PR06 v1.0 lineage reviews under `docs/ephemeral/` | all `ACCEPTED_FINAL`; the PR06 review (`docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md`, SHA-256 `27d49898f6a416332f5171a969a2ae2973b20097b8faf4ea58e31e470b51de98`) records the admitted 44-member release at `1.1.0`, `release_id 988ed2a7…`, F03/F05/F07 carried, CR-01/O-12 open, no Security Review of PR06 |
| This unit's instruction | `HDE-EPIC040-PR06a-pr-instruction-v1.0.md` (§1) | sole native input of this plan; §§3–13 mapped into §§3–14 below; where it and the overlay differ, the overlay governs (instruction §2) |
| Overlay and decision | §1 | the operative authority: objective, five deliveries, owned loci, proof, exclusions, completion, C040-07, dependency order `PR01 → … → PR06 → PR06a → PR07 → OPS01` |
| PR-10 handoff | `docs/ephemeral/HDE-EPIC040-PR06a-PR10-handoff-v1.0.md`, SHA-256 `46602a0398aa551dc5b40dd0f76dc9631ccf57848409427a1794dbc2823cc4c3` | context only; it named PF10 v13.3.3, which the instruction already corrects to v13.3.4 |
| Format precedent | `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.1.md`, SHA-256 `8df055a33bed5e4b1289b4e8791708e0cb9dc399d3f10fd35cc87c469e447e74` | structure and convergence procedure only; no content inherited |

Accepted-final PR01–PR06 are not reopened, rerun, revised or reaccepted by this plan. PR06's 44-member admission is valid history, superseded as the current release only by this unit's re-cut once it lands.

### 2.2 Controlled subject-matter sources used (all from `docs/pfcanon/`, read-only)

| Source | Sections used | Bearing |
| --- | --- | --- |
| `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`, SHA-256 `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a` | §§2.1–2.4, 3.2, 4.4–4.7, 5.1, 5.4.7 | Reader v1 six-key covenant, harmony-only v1 policy, "future, versioned change", five-key preimage recipe, closed ordered Magic-10 set; §2.1 records the checked-in v1 schema as non-conforming; §2.3 records the error-envelope `schema`/`details` gap (§13.1 candidate C040-08) |
| `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`, SHA-256 `e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696` | §8.1 (8.1.1–8.1.4), §15.2 `OI-001` | numeric-free covenant and v1 exposure rule; `OI-001` terms for `reader.v2` (ten items, canonical order, no omission/duplication/default fill/harmony substitution/viewer mutation; Reader v1 unchanged) |
| `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`, SHA-256 `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e` | §1 map ("Reader transport"), §§5.1–5.1.4, 5.2 (5.2.3 tokens/statuses/messages), 5.3, 5.4 (route, version selection, API-mount alias posture, gate), 5.6 (route table, `/api/reader POST` row, catalog record model), 6.2–6.3 | production route `POST /api/reader`, request contract, error contract, A7 rules, alias posture, catalog rows, single emitter and preimage recipe |
| `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`, SHA-256 `d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d` | §2.6 (frozen order and bands), §5.1 (frozen-input completeness, promoted paths, "Reader and governed errors" row, manifest form, `1.1.0` / `2026-08-24T18:04:49Z` for the v1 cut), §5.2 | member form, canonical bytes, sidecar posture; the 45-member roster and re-cut version are C040-07 drainage items for the PF12 maintainer, not repository writes |
| `PF03-Reference-Technical-Writing-Best-Practices` | source fidelity | applied to this document |

No PF source was resolved from anywhere but `docs/pfcanon/`. Nothing under `docs/pfcanon/` is changed by this plan or by the unit it plans.

### 2.3 Current controlled PF10 and every applicable active addendum

- Current controlled PF10 Markdown (resolved by its own §6 current-version rule; a single unlettered document): `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md`, SHA-256 `0029e2827904f6b798f6367f54a8d134bb55d170a412cc544b1555594c4e4f29`, 270,087 bytes, 2,485 lines, addenda §2.1 through §2.23, read completely. The four older base files (`v13.3`, `v13.3.1`, `v13.3.2`, `v13.3.3`) sit beside it and are not read (PF10 §6; instruction N-01; §13.2 O-P06a-01).
- Applicable active addenda, by repository path, in the order they bear on this unit:
  - §2.23 — `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (the operative overlay; its front matter lists the prior addenda it preserves or reassigns).
  - §2.16, §2.17, §2.18 — `docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md`, `…-F05-…`, `…-F07-…` (the deferred work; return point reassigned by §2.23 from PR07 to PR06a; their "What PR07 inherits" tables are the exact work items, mapped in §7).
  - §2.12 — `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` (admission binds executing mechanics to the admitted release; the boundary this unit must not change).
  - §2.21 — `docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md` (frozen-capture identity source for the canonical JSON gate; the reason a re-cut no longer breaks the frozen captures).
  - §2.22 — `docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md` (PR06 accepted final; the current admitted release this unit supersedes).
  - §2.15 (`docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`) — its interval ended with PR06; its `RELEASE_NOT_ADMITTED` branches are never taken on this candidate but remain in the tools and tests untouched.
- Effective baseline: **approved base + applicable PF10 overlays** (`AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`). The PF10 version actually read is recorded as provenance; it is not a gate on later work.

### 2.4 GCFPE execution sources

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, read completely at invocation (Notion read only; no Notion write is directed by this task, so none was made).
- Destination verified for §17: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (page title confirmed by fetch; read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members, per the release register named by the handoff. The register itself was not re-read for this run; the selection is carried as supplied.
- Repository instructions applied: `AGENTS.md` (closed rails, pytest readiness, governed-evidence rules, QA-output placement, PR-description contract, code-review scope) and the workspace skills governing write boundaries, artifact storage and reporting.

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline verified at planning time

| Fact | Value |
| --- | --- |
| `main` | `7f58ad613a0991bdc32accb179c30c11715209bc` (`docs: Update PF10 HDE Build Notes to v13.3.4 (#505)`), tree `d8fb2ae34df39f56dce046869471b7d2c48eaa75`; `origin/main` identical; equals the instruction's `baseline_main` |
| Remote branches | `main`; `claude/nice-mendel-foex54` (PR #506, the instruction, one commit ahead of `main`); this session's planning branch. No PR06a implementation branch, worktree or pull request exists |
| Admitted release | `catalog/manifest.json`: 44 rows, version `1.1.0`, `built_at_utc 2026-08-24T18:04:49Z`, 5,752 bytes; `load_active_mechanics_bundle()` returns `ADMITTED` with `release_id 988ed2a7c597631efc30662cfab1b16763d087434a64eb588985abed12d72f0e`; `engine.runtime.identity.identity_meta()["release_id"]` agrees; cutter `--check` and `release_id_recompute.py --check-manifest-only` exit 0 |
| Working tree | clean at inspection start; this plan is the only intended write of this session (`docs/ephemeral/` only) |

### 3.2 Verified baseline facts that shape this plan

Each fact was established by reading the file named or by executing the command named, at the baseline above (execution in the scratch clone of §3.3, never in the checkout).

| # | Fact | Consequence |
| --- | --- | --- |
| F-01 | `engine/config/registry_loader.py`: `ADMITTED_RELEASE_VERSION = "1.1.0"` (line 398), `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` (399), `ADMITTED_RELEASE_ROSTER` (400–445), import-time invariant `!= 44` (447). `_validate_admitted_manifest` checks the exact roster, the version **and** the timestamp (`RELEASE_TIMESTAMP_MISMATCH`, lines 1220–1240) | the instruction bounds this file to roster, invariant and version; therefore the re-cut keeps `built_at_utc` at the canon-fixed value (D-15) |
| F-02 | `_validate_admitted_schema_documents` validates six named schema members plus `schemas/reader.v1.schema.json` (draft 2020-12, `$id https://example.org/schemas/reader.v1.schema.json`) and `adapter/schemas/error_v1.schema.json`; any other `.json` member is validated only as canonical JSON by `_parse_release_member_bytes` | the new v2 schema is admitted as a canonical-JSON member; its draft and `$id` are proven by tests, not by admission (admission logic unchanged by bound; §13.2 O-P06a-07) |
| F-03 | Blueprint `reader_v1` (`adapter/http_reader.py`) is registered with `url_prefix=""` by all three app factories: `adapter/factory.py` (the `Procfile` entry point), `adapter/http_reader.py::create_app` (tests and evidence generators) and `adapter/wsgi.py`. It declares `GET /reader` (dev-gated, `v=1`), `POST /reader` (the production handler since PR04), `/aux/narrative` **and** `/api/aux/narrative` as two decorators on one view, the `/ops/*`, `/dev/*` and `/internal/*` surfaces. The compat blueprint is a separate `Blueprint` with `url_prefix="/api/compat/v1"` and scoped JSON 404/405 handling | the route mechanism of §5.2 |
| F-04 | Today `POST /api/reader` is 404; `GET /api/reader` on an `/api`-mounted rule would be Flask's HTML 405; a duplicated selector `?v=1&v=1` is served as `v=1` because `request.args.get("v")` takes the first value (`getlist` returns both) | governed 405 refusals and strict version selection (§5.1, §5.2) |
| F-05 | `schemas/reader.v1.schema.json` (1,563 canonical bytes) rejects a `harmony` success (`'harmony' is not one of ['open_leader', 'warm_leader', 'cool_leader', 'glow_leader']`) **and** rejects the route's real error bytes (`Additional properties are not allowed ('schema' was unexpected)`); it still declares `prompt`; its success branch is closed only by root-level `additionalProperties` | F05 correction of §5.4; the error-branch fact is carried, not fixed (D-06, §13.1) |
| F-06 | `presenter/reader_v1/emitter.py` sorts categories by `id` (set semantics), passes a `prompt` key through when present, builds the five-key preimage and emits through `engine.presenter.emitter.emit_public`; `engine/runtime/public.py` builds exactly one `harmony` item; `engine/stable/sercanon.py` sorts object keys and preserves array order | v2 needs an ordered path (§5.3); the single emitter is unchanged |
| F-07 | `engine/compat/compute.py::evaluate_pair` returns the validated `magic10_compat_result.v1` whose `categories` rows are checked against `bundle.registry.magic10_order` (harmony-first, loaded from `catalog/magic10.json`); `harmony_band()` is the first row's band; `engine/categories/registry.py::FROZEN_MAGIC10_ORDER` carries the same order as a pure tuple | the ten bands come from the already-validated result with no second calculator (§5.3) |
| F-08 | The endpoint catalog is **written** by `tools/evidence/generate_a7_transport_proofs.py::catalog_obj()`; `--check` compares the bytes of `docs/ENDPOINTS_CATALOG.json`, its `.sha256`, the audit mirror and its `.sha256`, `artifacts/reader/endpoints_snapshot.json` and seven `artifacts/proofs/*`; `validate_catalog` requires exactly one `success_endpoints` designation and it must be `GET`; `CLASS` already contains an unused `public_reader`; `capture()` posts to `/reader` expecting 422 (the PR04 F01 posture) and `PROOFS[4]` pins that text | catalog rows exist only through this owner (D-11) |
| F-09 | `tools/evidence/generate_open_rails_abba_proof.py` pins `FROZEN_OPEN_ABBA_SHA256` to the digest of `audit/gates/determinism/open_rails_abba.json`; that primary carries the release identity and is regenerated by a re-cut; PR06 landed exactly this two-line constant refresh (`f7484d0`) | D-12 |
| F-10 | F07 today: `generate_conjunction_writer_evidence.py` requires open rails, imports `dev_compat_identity` and compares `conjunction.compat.meta` to the dev stamp; `_emit_conjunction_response` hardcodes `local_lookup=None`; `resolver._resolve_stored` consults `local_lookup(canonical_id)` first and `_bind_lookup_hit` accepts a `MappedBodyGraphRow` whose `user_id` equals the canonical id; `resolve_db_user_id("left")` is `93f59310-804c-5c09-8ba6-e4a10d83bc7a`, `("right")` is `af2a86d3-cde1-511e-83cd-60c0deea1d90`; the compat result carries `release_id` and no `meta`; both writer artifacts are Index/Mirror rows with path proofs; `dev_compat_identity()` has no other consumer | §5.8 |
| F-11 | `engine/bodygraph/resolver.py::_vendor_config_env` merges `os.environ`, so a dev conjunction request under open rails with vendor credentials present reaches the vendor | the corrected generator requires closed rails and the corrected tests delete the vendor keys (§5.8, §8.7, R-13) |
| F-12 | Goldens: `scripts/make_reader_v1_goldens.py` is the owning writer of `goldens/reader/v1/*` and hardcodes the retired `*_leader` identities; `g02_*.jsonl` carry a pre-v1 legacy shape (`bands`, `flags`, `prompt`, `uncertainty`, `versions`); `g06` is a synthetic error golden; sidecars are hash-only lines. `scripts/make_release_pack.sh` names the goldens in its default list and writes the tracked `artifacts/release_pack_manifest.json` and `artifacts/release_id.txt`; `tests/reader_v1/test_release_pack.py` runs it and, at the baseline, **rewrites the tracked `artifacts/release_id.txt`** (`44136fa3…` tracked vs `f0eabbc3…` produced: stale since PR06 canonicalized the v1 schema); `tests/reader_v1/test_cli_proof.py` fails at the baseline (`scripts/hd_cli.py` exits 2 with `ADMIN_FLAG_REQUIRED`; a legacy EPIC004 script that emits an `open_leader` envelope) | §5.6, D-08, D-13, D-18, §13.2 |
| F-13 | `tools/cli/emitter_symbol_proof.py` allow-lists `emitter.emit_public` and `emit_reader_public_envelope` for `showcompat`; `tools/cli/serializer_grep_guard.py` scans `engine/cli` and `adapter/http_reader.py` for `json.dumps`; `engine/cli/main.py` calls `emit_reader_public_envelope(…, eligible=, harmony_band=)`; `engine/emit_public.py` forwards exactly the five keywords the dev harness `dev/reader_harness/app.py` injects | the CLI stays a v1 family with no symbol change; new keywords are optional (§5.3) |
| F-14 | Classifier (`ci/checks/classify_ci_changes.py`) verdicts at the baseline: `goldens/**` is `CI_CHANGE_SURFACE_UNCLASSIFIED`; `adapter/factory.py`, `adapter/wsgi.py`, `schemas/reader.v2.schema.json(.sha256)`, `scripts/make_reader_v1_goldens.py`, `scripts/make_release_pack.sh` have no product owner test (`CI_PRODUCT_OWNER_TEST_MISSING`); `tools/evidence/generate_conjunction_writer_evidence.py` has no generator owner; `docs/ENDPOINTS_CATALOG.json` selects `evidence`+`release`; `tests/http/*` and `tests/reader_v1/*` select `product`(+`compat`)+`release`; `tests/evidence/test_http_reader_ci_ownership.py` requires every test module importing `adapter.http_reader` to be registered in `_HTTP_READER_TEST_OWNERS`; any change to the classifier selects all seven lanes | §5.11 registrations |
| F-15 | Tests pinning the 44-member identity: 27 tests in six files fail on a 45-member tree (§8.8, executed in §3.3); `tests/config/helpers.py` derives the synthetic release from the constants and needs no change | §8.8 |
| F-16 | CI (`.github/workflows/ci.yml`): one `test` job; exact-head checkout; classifier; changed tests in a detached worktree with `git diff --exit-code` and a clean-tree assertion; seven lanes; release lane runs `release_id_recompute.py --check-manifest-only`, the release pytest set in a worktree and the strict attestation build + verify; final audit `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | §10 |
| F-17 | No repository artifact defines an ingress policy; the phrase exists only in the F03 deferral record | §5.12 |
| F-18 | The PR06 landed diff (`f7484d0`, 113 files) is the empirical map of what a re-cut touches: catalog logs, canonical-JSON gate outputs, determinism family, open-rails proof, A7 family, Index/Mirror, sanity log, path proofs | §6.3; reproduced in §3.3 |
| F-19 | `pyproject.toml` packages `catalog/*.json` only; no `schemas/` package data | CR-01 posture unchanged; the 45th member is also outside the wheel (§13.2 O-P06a-14) |
| F-20 | `errors/token_map/token_map.json` already carries `ERR_NOT_FOUND` ("not found") and `ERR_READER_INVALID_VERSION` ("unsupported reader version"); `MAGIC10_HTTP_STATUS` and `BOUNDARY_REASONS` cover every token the production route can emit | no new token, no token-map regeneration (§5.10) |

### 3.3 Planning rehearsal in scratch clones (inference support, not PR evidence)

To plan from execution rather than reading alone, this session rehearsed the unit in throwaway clones of `7f58ad6…` under the session scratchpad (`rehearsal`, `rehearsal2`, `rehearsal3`, one virtualenv: Python 3.11.15, pytest 8.4.2, Flask 2.3.3, jsonschema 4.23.0, setuptools 79.0.1), never in the repository checkout. What it established is recorded as **inference support**; it is not implementation, QA or CI, and none of its bytes enter the PR. PR-30 re-executes every step on the real branch (§§9–10). Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, except where stated.

**Incident, recorded plainly.** This container's environment carries `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` and `DATABASE_URL` (names only; values never read or logged). Before that was noticed, two rehearsal steps that follow the *existing* F07 posture — the generator's `--check` under `SAFE_MODE=0 ALLOW_NETWORK=1` and the first test of `tests/evidence/test_dev_conjunction_identity.py`, which sets those rails itself — returned 200s from `/dev/writer/conjunction`, which with credentials present means live vendor acquisitions occurred (F-11; confirmed by the same request refusing `PROVIDER_CONFIG_MISSING` once the keys were absent). No database write occurred: `--check` neutralizes `DATABASE_URL`, and every other executed test deletes it or fakes the DB. Every later command ran with the four keys unset. The corrected generator and tests (§5.8, §8.7) make this impossible by construction, and §10.1 requires PR-30 to run with the keys absent.

| Step rehearsed | Outcome |
| --- | --- |
| Baseline admission and identity | `ADMITTED`, 44 members, `988ed2a7…`; `identity_meta()` agrees; magic10 order harmony-first |
| Baseline focused suites (`tests/reader_v1`, `tests/http/{test_reader_post_v1,test_reader_a7_transport,test_endpoint_catalog,test_dev_conjunction_http}.py`, `tests/transport/test_a7_transport_proofs.py`, `tests/runtime/{test_identity,test_emit_public_legacy_helper}.py`, `tests/evidence/test_dev_conjunction_identity.py`) | 105 passed, 3 failed: `test_cli_proof` (pre-existing, F-12) and the two F07 tests (the deferred defect); `artifacts/release_id.txt` rewritten by `test_release_pack` (F-12); baseline A7 `--check` ok; cutter `--check` and recompute exit 0 |
| Current v1 schema against real bytes | rejects the harmony success and the real error envelope (F-05) |
| v2 projection | `evaluate_pair` on the synthetic complete release yields ten rows in registry order, AB == BA; `harmony_band()` equals the first row |
| v2 emission through the single emitter (prototype function in a script) | AB == BA bytes, two-run identity, exactly one LF, array order preserved, preimage recompute; 590-byte envelope for the synthetic pair; ineligible `[]` |
| `/api` mount feasibility (second URL rule on the same view) | `POST /api/reader?v=1` 200 with one `harmony` item; `?v=2` 400 `ERR_READER_INVALID_VERSION` today; `GET /api/reader` HTML 405 today; `?v=1&v=1` 200 today (F-04) |
| Reader v2 schema draft (§5.5), written canonically | 4,269 bytes, SHA-256 `7e4373869fd3810ec083e13cea0600aa4b9899443ee2db834b27fd4be2922fcf` (a draft; PR-30 authors the real bytes); `check_schema` ok; valid: ten-in-order eligible, ineligible `[]`, the real `ERR_READER_INVALID_VERSION` envelope; invalid: nine items, wrong order, duplicate `harmony`, `prompt` on an item, numeric `score`, `reader_version "v1"`, extra top-level key, eligible with `[]`, ineligible with ten, error with `details`, unknown token |
| F07 seam (clone `rehearsal2`, `adapter/http_reader.py` patched, constants bumped, manifest re-cut) | first attempt without a re-cut refused `ERR_M10_MANIFEST_MISMATCH` — PF10 §2.12 working as designed (any change to `adapter/http_reader.py` needs the cut); after the cut: seam absent → 503 `ERR_WRITER_RAILS_CLOSED` / `PROVIDER_REFUSED`; seam present under closed rails with `HdApiClient.from_env` patched to fail → writer 200 twice, reader 200, sampler 200, invalid 422; two-run bytes equal; writer result == reader payload; `compat.release_id == identity_meta()["release_id"]`; no `meta` (no dev stamp); `magic10_compat_result.v1`; `dev.writer.conjunction.success.v1`; prod gate still 403 with the seam set |
| 45-member cut (clone `rehearsal`: v2 schema draft added, roster + `!= 45` + `1.2.0`) | `cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission` exit 0; `--check` 0; `release_id_recompute.py --check-manifest-only` 0; 45 rows, 5,881 bytes; `ADMITTED`, `identity_meta()` agrees; scratch `release_id eb859d3b…` — **prototype bytes only; the real value is recomputed by PR-30 and is not predicted here** |
| Convergence, PR06 order | `--compare-goldens .` exit 0, eight `match`; gate `--check-only` 1 before the write (manifest target changed), write 0, `--check-only` 0; updater 0 / `--check` 0; `--publish-family` 0; A7 write / `--check` 0; determinism write / `--check` 0; open-rails fixture proof write / `--check` 0 (`SAFE_MODE=0 ALLOW_NETWORK=1`, vendor keys absent, fixture mode); updater; `orientation_demo --check`, `validate_evidence_paths`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `check_lf_endings`, `check_final_lf.sh` all 0; second run of gate/updater/A7/determinism byte-stable |
| Sanity pipeline | stage 06 failed twice for reasons that are now planned facts: (a) `run_rails_job_definitions.py` shells to `python -m pytest`, so `python` on `PATH` must be the interpreter that has pytest (§10.1); (b) `test_open_rails_abba_proof.py` refused `FROZEN_PRIMARY_DRIFT` until `FROZEN_OPEN_ABBA_SHA256` was refreshed to the regenerated primary (F-09, D-12). Then `RAILS_JOB_DEFINITIONS_OK`; the failed canonical run had bound the FAIL model, so the PR06 plan §5.8 pre-binding (non-canonical run `summary:PASS`; owner renderer writes the PASS model; updater; canonical run) restored a PASS log byte-identical to the tracked one; `run_sanity_pipeline_gate.py` 0; updater `--check` 0 |
| Frozen families | `generate_showcompat_artifacts.py --check`, `generate_cli_conformance_artifacts.py --check`, `generate_rails_gate_evidence.py --check`, `generate_env_matrix_snapshot.py --check` all 0 (unaffected by the re-cut) |
| Touched-file set of the converged scratch commit | 44 files: `catalog/manifest.json`, `engine/config/registry_loader.py`, `schemas/reader.v2.schema.json(+.sha256)`, `tools/evidence/generate_open_rails_abba_proof.py`, `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`, `artifacts/evidence_index.jsonl(+.sha256)`, `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`, `audit/gates/canonical_json/*.log`, `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/json_gate/canonical/*.ndjson`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`, and their path proofs |
| Pinned-identity tests on the converged 45-member tree | exactly the 27 tests of §8.8 fail; 564 others in the same files pass |
| Strict attestation on the committed scratch cut | `build_release_attestation.py --output <external empty dir> --require-clean` exit 0; `--verify` exit 0; `release_admission PR06R_B_FINAL_PASS`, `validation_result PASS`, `release_id` equals the scratch manifest digest, 174 files bound, 14 declared outputs under `omitted_files` (the builder's existing secret-safety rule, as on PR06); tree clean afterwards; 79 seconds |

Caveats: the rehearsal used a placeholder-free but incomplete candidate (no route change, no goldens, no F07 generator change), so its evidence bytes and `release_id` are not the real ones; the real candidate re-derives all of them. Nothing above is a QA result.

## 4. Exact objective, completion conditions and exclusions

### 4.1 Objective (overlay "Objective"; instruction §4)

Deliver the public Reader contract that current canon and the Product Owner decision define: full Magic-10 exposure through Reader v2, Reader v1 conformed to its unchanged covenant, the production Reader at its PF05 route, the dev conjunction evidence capture restored, and one release re-cut binding the result — through the existing runtime, the single emitter, the existing owners and the unchanged admission boundary.

### 4.2 Completion conditions

| # | Condition | Proof home |
| --- | --- | --- |
| CC-1 | `POST /api/reader?v=2` serves the Reader v2 success envelope: six keys, `reader_version "v2"`, ten `{id, band}` items in the canonical governed order when eligible, `[]` when ineligible, numeric-free, canonical bytes, AB↔BA and two-run identity, preimage recompute; validates against `schemas/reader.v2.schema.json`; goldens under `goldens/reader/v2/` pin eligible, ineligible, AB↔BA and error cases; pairs derived from the golden cases that carry Gate sets reproduce the canonical matrix bands | §§5.3, 5.5, 5.6, 8.1, 8.6 |
| CC-2 | `schemas/reader.v1.schema.json` admits `harmony` only, declares no `prompt`, closes the success branch to exactly six keys, and validates the route's v1 success bytes; `goldens/reader/v1/*` are regenerated by their owner without any `*_leader` identity; the dev `GET /reader` bytes and the CLI `--dump-reader` bytes are unchanged for the same inputs | §§5.4, 5.6, 8.2, 8.6 |
| CC-3 | `POST /api/reader` serves `v=1` and `v=2` from every app factory; `POST /reader` and every non-POST method on `/api/reader` are governed 405 refusals; version selection is strict; the catalog and its audit mirror carry the production row and regenerate through their owner with the A7 family | §§5.1, 5.2, 5.7, 8.1–8.5 |
| CC-4 | The dev conjunction routes carry the real admitted release identity and no dev stamp; the resolver seam is absent by default and never read by the production Reader; the generator runs under closed rails with no vendor client and no DB; its two artifacts are regenerated and its test is a CI changed-test target | §§5.8, 5.11, 8.7 |
| CC-5 | `catalog/manifest.json` lists exactly the 45 roster paths, version `1.2.0`, `built_at_utc 2026-08-24T18:04:49Z`; cutter `--check` and `release_id_recompute.py --check-manifest-only` exit 0; `load_active_mechanics_bundle()` admits the real root with the recomputed `release_id` and `identity_meta()` agrees; tampered, missing and extra members refuse | §§5.9, 8.8 |
| CC-6 | Config family, canonical JSON gate outputs, determinism family, open-rails fixture proof, A7 family, F07 writer artifacts, Index/Mirror/path proofs/orientation and the sanity log converge through their owners; every read-only check of §10.4 exits 0; the sanity log is the PASS model and the gate wrapper exits 0 | §§5.9, 10 |
| CC-7 | The 27 pinned tests express the 45-member `1.2.0` release; every rewritten and new test passes; no test is skipped, disabled or quarantined; all seven CI lanes and the supplemental roster pass on the exact candidate head; the final audit finds a clean tree | §§8, 10 |
| CC-8 | `build_release_attestation.py --output <external empty dir> --require-clean` and `--verify` succeed in the release lane on the exact candidate head; no change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS` | §10.6 |
| CC-9 | PR-session code review, security review of the new public route and the dev seam, and CI on the exact head; native findings resolved on the current substantive change; the PR description follows the template with the merge statement of §15 | §§11, 15 |

### 4.3 Hard exclusions

No change to Magic-10 mathematics, membership, order, weights, caps, bands or catalog data; no public numeric field; no narrative or prompt on any public surface; no new CLI flag (Reader↔CLI dump parity stays a Reader v1 family; `engine/cli/main.py` and `scripts/hd_cli.py` untouched); no Reader v1 contract change beyond the F05 conformance items named by the overlay; no change to `hde.release_attestation.v1` or `PR06R_B_FINAL_PASS`; no change to admission logic (`engine/config/registry_loader.py` changes only the roster, its count invariant and the admitted version); no change to the 26-target canonical JSON gate or its six set rules; no release activation, promotion or deployment; no live vendor or database operation; no PF-Canon edit (C040-07 drainage belongs to the PF01/PF04/PF05/PF12 maintainers); no re-identification of the frozen showcompat / CLI-conformance / identity-family captures; PR06 not rerun; PR07's documentation not absorbed; no change to `.github/workflows/ci.yml`, `tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/run_canonical_json_gate.py`, `engine/compat/**`, `engine/bodygraph/**`, `engine/emit_public.py`, `engine/compat/identity.py`.

## 5. Designed interfaces, invariants and contracts

### 5.1 Strict version selection — `adapter/http_reader.py` (owned locus)

- One helper `_select_reader_version(allowed)` reads `request.args.getlist("v")`. It returns `"v1"` for exactly `["1"]` and `"v2"` for exactly `["2"]` when that value is in `allowed`. Anything else — absent, empty, more than one value (`v=1&v=1`, `v=1&v=2`), an unsupported value (`v=3`), a malformed value (`v=01`, `v= 1`, `v=1.0`) — raises `_ReaderFailure("ERR_READER_INVALID_VERSION", 400)`.
- The production route allows `("1", "2")`; the dev `GET /reader` allows `("1",)` only, so `GET /reader?v=2` is refused exactly as `v=3` is. The refusal keeps today's token, status 400, `Cache-Control: no-store`, no ETag, canonical `error_v1` body, and happens before any body read or DB lookup.
- Existing behaviour preserved: the version check precedes the `APP_ENV` gate on the dev GET (the existing forbidden-in-production test relies on `v=1` reaching the gate).

### 5.2 Production route mechanism — `adapter/http_reader.py`, `adapter/factory.py`, `adapter/wsgi.py` (owned loci; D-01, D-02)

- A second, production-only blueprint is created by a new factory `get_reader_api_bp(emit_fn=None)` returning `Blueprint("reader_api", __name__)` and exported at module level as `api_bp = get_reader_api_bp()`. It declares:
  - `POST /reader` (`provide_automatic_options=False`) → the shared production handler `_reader_post(emit_fn)` (today's `reader_v1_post` body, extended by §5.3);
  - one method-catch rule for `GET, HEAD, OPTIONS, PUT, PATCH, DELETE` on `/reader` (`provide_automatic_options=False`) → governed 405: `error_envelope("ERR_NOT_FOUND")` through `emit_public`, `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, `Allow: POST`, no ETag, no `Content-Encoding`.
- Every app factory registers it under the `/api` prefix: `app.register_blueprint(api_bp, url_prefix="/api")` in `adapter/factory.py` (the `Procfile` entry point), in `adapter/http_reader.py::create_app` and in `adapter/wsgi.py::create_app`, each next to its existing `bp` registration. This is the PF05 §5.4 mechanism: the Reader (production) blueprint mounted under an `/api` prefix, so `/api/reader` is the mounted path, not a duplicate declaration. The dev `GET /reader` stays at its canonical PF05 path on the unprefixed blueprint and remains Reader v1 with unchanged bytes.
- The unprefixed `POST /reader` no longer reaches the production handler. It becomes a governed 405 stub on the dev blueprint (`ERR_NOT_FOUND`, `Allow: GET, HEAD`, `no-store`, no ETag), restoring the pre-PR04 posture with the canonical token so no production handler is served outside `/api` (the security half of F03, PF10 §2.16 §4).
- The dev harness `dev/reader_harness/app.py`, which injects `engine.emit_public.emit_public_envelope` into the dev blueprint and mounts it at `/api` locally, is untouched; its injected function is never called with the v2 keywords because the dev blueprint's routes pass only the existing five (§5.3).
- `adapter/wsgi.py`'s global JSON 404/405 handlers and `adapter/factory.py`'s compat-scoped handlers are unchanged. No other route moves. `/internal/*`, `/ops/*`, `/dev/*`, `/aux/narrative` keep their paths.

### 5.3 Reader v2 projection — `adapter/http_reader.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py` (owned loci; D-04, D-05)

- `_evaluate_reader_pair(left, right)` returns `(eligible, bands, release_id)` where `bands` is the tuple of `(category_id, band)` pairs of the validated compat result in its validated order (F-07), or `None` when ineligible. The v1 harmony band is `bands[0][1]` (the first row is `harmony` by the registry order; the handler asserts `bands[0][0] == "harmony"` and treats anything else as `CompatBoundaryError("result_schema")`). No second calculator: the ten bands are read from the result `validate_compat_result` already checked against `registry.magic10_order`.
- `_reader_post(emit_fn)` calls `emit_fn(None, None, engine_tag=…, invocation_tag=…, release_id=result_release_id or meta["release_id"], eligible=eligible, harmony_band=<v1 band or None>, reader_version=version, categories=bands if version == "v2" else None)`. Success headers are exactly today's (`Content-Type`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, `Content-Length`, no ETag; POST non-conditional). Errors are unchanged.
- `engine/runtime/public.py::emit_reader_public_envelope(a_chart=None, b_chart=None, *, engine_tag=None, invocation_tag=None, release_id=None, eligible, harmony_band=None, reader_version="v1", categories=None)`: the v1 path is byte-for-byte today's (`harmony` item, `emit_reader_v1`). The v2 path requires, when eligible, `categories` to be exactly ten `(id, band)` pairs whose ids equal `FROZEN_MAGIC10_ORDER` in order and whose bands are in `("Cool", "Open", "Warm", "Glow")`, else `ValueError("reader_v2_categories_required")`; when ineligible `categories` must be empty and the array is `[]`. It builds `{"eligible", "categories": [{"id", "band"}…], "meta", "release_id"}` and calls `emit_reader_v2`. `emit_reader_public_bytes` forwards the two new keywords. Both keywords default so every existing caller (`engine/cli/main.py`, `engine/emit_public.py`, `scripts/cli/canonical_harness.py`, tests) is unaffected; `engine/runtime/__init__.py` needs no change.
- `presenter/reader_v1/emitter.py` (the existing module; no new presenter module):
  - `emit_reader_v1(enriched)` keeps its preimage (`reader_version "v1"`, set-sorted categories) and now refuses any category key other than `id` and `band` (`prompt` included) with `ValueError` instead of passing it through (D-05; the covenant never allowed `prompt` and no route supplies it).
  - `emit_reader_v2(enriched)` builds the preimage `{"reader_version": "v2", "eligible", "categories", "meta", "release_id"}` where `categories` is the caller's ordered array validated to be exactly ten items, ids equal to `FROZEN_MAGIC10_ORDER` (imported from `engine.categories.registry`, a pure tuple), bands in the enum, keys exactly `{id, band}`, no duplicates — **not sorted** (C040-07: an ordered array in canonical governed order, not a set-sorted array); when `eligible` is false the array must be empty.
  - One private `_emit(preimage)` does what both do today: `pre_bytes = emitter.emit_public(preimage)`, `idempotence_hash = sha256(pre_bytes)`, final envelope, `emitter.emit_public(final)`. Serialization stays the single canonical serializer (`sort_keys=True` sorts object keys and preserves array order, F-06); the five-key preimage recipe and the six-key envelope apply to v2 exactly as to v1.
- No public field is added; `meta` stays `{engine_tag, invocation_tag}`; identity comes from `identity_meta()` and the admitted bundle as today.

### 5.4 Reader v1 schema conformance (F05) — `schemas/reader.v1.schema.json` and `.sha256` (owned loci; D-06)

The file is rewritten in canonical bytes (`engine.serializer.canon.sercanon`, the same form PR06 gave it), draft 2020-12, same `$id`, with exactly the three corrections the overlay names and a restructuring that makes the third one expressible:

- `$defs.category_id.enum` is `["harmony"]`.
- `$defs.category` declares exactly `id` and `band` (`prompt` removed), `additionalProperties: false`.
- The success branch is its own closed object `$defs.success`: `additionalProperties: false`, `required` and `properties` exactly the six keys (`reader_version` `const "v1"`, `eligible` boolean, `categories` array of `category`, `meta`, `release_id` and `idempotence_hash` hex64), with the eligibility coupling `oneOf: [{eligible const true, categories minItems 1 maxItems 1}, {eligible const false, categories maxItems 0}]`.
- The error branch keeps today's semantics unchanged (`ok` const false, `code`, `error`, optional integer `retry_after_ms ≥ 0`, `additionalProperties: false`) as `$defs.error`; the root becomes `oneOf: [success, error]`. It still does not admit the route's `schema` key: that disagreement between PF05 §5.2 and PF01 §2.3 / PF04 §8.1.2 is a Canon question carried in §13.1 (candidate C040-08), not decided here.
- `schemas/reader.v1.schema.json.sha256` is refreshed in its existing `sha256sum` line format.

### 5.5 Reader v2 schema — `schemas/reader.v2.schema.json` and `.sha256` (new owned loci; D-07)

Canonical bytes, draft 2020-12, `$id https://example.org/schemas/reader.v2.schema.json`, `title "Reader v2 — public envelope (success | error)"`, root `oneOf: [success, error]`:

- `$defs.success`: `additionalProperties: false`; required/properties exactly `reader_version` (`const "v2"`), `eligible`, `categories`, `meta` (exactly `engine_tag`, `invocation_tag`, non-empty strings), `release_id` and `idempotence_hash` (`^[0-9a-f]{64}$`); `oneOf` coupling: eligible true ⇒ `categories` is `$defs.categories_eligible` = `prefixItems` of ten closed items in the exact order `harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance` (each `{"id": const, "band": enum}` with `additionalProperties: false`), `minItems 10`, `maxItems 10`, `items: false`; eligible false ⇒ `categories` `maxItems 0`.
- `$defs.error`: the production Reader error envelope PF05 §5.2.3.1 specifies for the route whose error behaviour v2 shares (C040-07): exactly `schema` (`const "v1"`), `ok` (`const false`), `code`, `error`; `additionalProperties: false`; `oneOf` of the twelve exact token/message pairs the route can emit: `ERR_READER_INVALID_VERSION`/`unsupported reader version`, `ERR_READER_INVALID_INPUT`/`invalid Reader request`, `ERR_READER_INVALID_CHART`/`invalid Reader chart`, `ERR_M10_PERSON_UNRESOLVED`/`BodyGraph not found`, `ERR_M10_RESOLVER_UNAVAILABLE`/`BodyGraph resolver unavailable`, `ERR_M10_BODYGRAPH_INCOMPLETE`/`BodyGraph is incomplete`, `ERR_M10_LEGACY_INPUT_UNSUPPORTED`/`legacy scoring input is unsupported`, `ERR_M10_CONFIG_MISMATCH`/`Magic10 configuration mismatch`, `ERR_M10_MANIFEST_MISMATCH`/`Magic10 release manifest mismatch`, `ERR_M10_RESULT_SCHEMA_MISMATCH`/`Magic10 result schema mismatch`, `ERR_M10_STALE_RESULT`/`Magic10 cached result is stale`, `ERR_NOT_FOUND`/`not found` (the messages are the token map's; a test pins each pair to `ERROR_TOKEN_MAP`). No `details`, no `retry_after_ms`.
- Positive and adverse validation cases are the thirteen of §3.3 (rehearsed on the draft). The sidecar uses the `sha256sum` line format like v1's.
- The v2 schema becomes the 45th release member (§5.9). Admission validates it as canonical JSON; its draft and `$id` are pinned by `tests/reader_v1/test_schema.py` (§8.6).

### 5.6 Goldens through their owning writer — `scripts/make_reader_v1_goldens.py`, `goldens/reader/v1/*`, `goldens/reader/v2/*`, companions (D-08, D-09, D-13)

- The writer's v1 section drops the `*_leader` list and writes the covenant set with the same synthetic identity as today (`Isis5`, `INV-000000`, `release_id "a"×64`): `g01_minimal_ineligible.json` (bytes expected unchanged), `g02_ab_ba_parity_A.jsonl` / `_B.jsonl` (two identical LF-terminated v1 envelopes with one `harmony` item, replacing the pre-v1 legacy shape), `g03_harmony_open.json`, `g04_harmony_warm.json`, `g05_harmony_cool.json`, `g07_harmony_glow.json` (new, so every band is pinned), `g06_error_invalid_input.json` (unchanged: a synthetic error golden consistent with the unchanged error branch, D-06). Old `g03_open_leader.json`, `g04_warm_leader.json`, `g05_cool_leader.json` and their sidecars are removed. Hash-only `.sha256` sidecars as today.
- A v2 section in the same script writes `goldens/reader/v2/`: `g01_ineligible.json` (`[]`), `g02_ab_ba_parity_A.jsonl` / `_B.jsonl` (two identical ten-item envelopes emitted from AB- and BA-labelled but identical band inputs), `g03_eligible_ten_in_order.json` (a fixed synthetic band vector covering all four bands, in canonical order), `g04_error_invalid_version.json` (the real `error_envelope("ERR_READER_INVALID_VERSION")` bytes through `emit_public`), with hash-only sidecars. The script's name is kept (renaming is a candidate for its owner, §13.2 O-P06a-15).
- Companions: `scripts/make_release_pack.sh`'s default list names the new v1 files; `tests/reader_v1/test_release_pack.py` names the same list; the script is run once (its owner) so the tracked `artifacts/release_pack_manifest.json` and `artifacts/release_id.txt` are byte-idempotent under the test in CI's detached worktree (this also repairs the baseline staleness of F-12).

### 5.7 Endpoint catalog and the A7 family — `docs/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json` (owned loci) through `tools/evidence/generate_a7_transport_proofs.py` (owning writer; D-11)

- `catalog_obj()` gains one row, inserted after `/api/compat/v1` (row order is authored; keys are canonicalized by the writer):
  `{"a7_eligible": false, "blueprint_module": "adapter.http_reader", "classification": "public_reader", "description": "Production Reader (POST; v=1 Reader v1, v=2 Reader v2)", "env_gate": "not_applicable_public", "internal": false, "method": "POST", "path": "/api/reader", "rails_profile": "public-read-only; closed rails; current-row DB resolution; no vendor call; POST non-conditional no-ETag"}`.
  `success_endpoints` stays exactly `[{"method": "GET", "path": "/reader"}]` (the validator requires one GET designation; a POST is A7-ineligible by PF05 §5.3). `classification` uses the existing `public_reader`, `env_gate` the PF05 §5.6 public sentinel `not_applicable_public`, `internal: false`. This is the "POST success row" owed as PR04 observation O-03.
- `validate_catalog` gains one rule mirroring the sampler rule: exactly one `POST /api/reader` row, `public_reader`, `internal` false, `a7_eligible` false.
- `capture()` proves the PF05 §5.3 non-conditional POST fact on the production route: `POST /api/reader` with query-only input and `If-None-Match` → 422 `ERR_READER_INVALID_INPUT`, `no-store`, no ETag, canonical body; `PROOFS[4]` (`artifacts/proofs/success_writers_errors.txt`) records `POST /api/reader` instead of `POST /reader`. The env-gate proof (`APP_ENV=prod` ⇒ `GET /reader` not 200) and every other capture are unchanged.
- Regenerated by the owner (write mode `HDE_WRITE_A7_PROOFS=1`, then `--check`): both catalogs and `.sha256` companions, `artifacts/reader/endpoints_snapshot.json` (expected byte-identical: `generated_at_utc` is the unchanged manifest timestamp), the seven proofs (the success proofs change because the v1 body carries the new `release_id`). Index/Mirror rows and path proofs follow through the updater.

### 5.8 Dev conjunction evidence (F07) — `adapter/http_reader.py`, `tools/evidence/generate_conjunction_writer_evidence.py`, `artifacts/writer/*` (owned loci; D-14)

- Route identity: unchanged from PR04 — the routes go through real admission and the compat result carries the admitted `release_id`; no `dev_compat_identity()` stamp anywhere. This is the F07 identity answer the decision records.
- Resolver seam: `_emit_conjunction_response` passes `local_lookup=current_app.config.get("DEV_CONJUNCTION_LOCAL_LOOKUP")` (a callable or `None`). The key is absent from every app factory's default config, so the routes fabricate nothing by default; it is read only inside the three dev routes, all behind `_dev_admin_gate()` (`APP_ENV ∈ {dev, test, local}`), and never by the production Reader, which keeps its own `_reader_current_rows` lookup. Under closed rails a lookup miss still refuses `PROVIDER_REFUSED` before any vendor client is built.
- Generator: requires **closed** rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`; refuses otherwise, so it cannot reach a vendor even when credentials exist), `APP_ENV` `dev` as today, neutralizes `DATABASE_URL` in both modes (write and `--check`), builds two deterministic `MappedBodyGraphRow`s from `fixtures/charts/alice.json` ("left") and `fixtures/charts/bob.json` ("right") rebased to the canonical ids `resolve_db_user_id` yields (F-10), with `vendor "hdapi"`, `vendor_version 2`, `input_fingerprint` = SHA-256 of the fixture's canonical `bodygraph` bytes, `payload = project_bodygraph(chart)`; installs `app.config["DEV_CONJUNCTION_LOCAL_LOOKUP"] = rows.get` on the app it creates; first sends one control request **without** the seam and records the refusal. Checks (all must be true): `seam_absent_refuses_closed_rails`, `writer_status_200`, `reader_status_200`, `writer_bytes_two_run_equal`, `writer_payload_two_run_equal`, `writer_result_reader_readback_equal`, `writer_success_typed_envelope`, `writer_error_typed_envelope`, `writer_admitted_release_identity` (`compat.release_id == identity_meta()["release_id"]` and `compat.schema == "magic10_compat_result.v1"`), `reader_admitted_release_identity`, `no_dev_identity_stamp` (no `meta` under `compat`; `release_id != "dev"`). Summary `schema: conjunction_writer_summary.v2` adds `release_id` (the public admitted identity) and `rails: closed`; the log becomes `schema=conjunction_write_readback.log.v2` with one line per check plus the payload hashes. `dev_compat_identity` is no longer imported.
- Registration: `tools/evidence/generate_conjunction_writer_evidence.py` → `("tests/evidence/test_dev_conjunction_identity.py",)` in `_EVIDENCE_GENERATOR_TEST_OWNERS`, so the test is a changed-test target (§5.11).
- Artifacts `artifacts/writer/conjunction_write_readback.log` and `conjunction_writer_summary.json` are regenerated by the generator's write mode after the re-cut (they carry the admitted identity); their Index/Mirror rows and path proofs follow through the updater.

### 5.9 Release re-cut and convergence order (overlay item 5; instruction §5.5; D-15)

- `engine/config/registry_loader.py`: `"schemas/reader.v2.schema.json"` added to `ADMITTED_RELEASE_ROSTER` (the sorted union keeps ASCII order), the invariant becomes `!= 45`, `ADMITTED_RELEASE_VERSION = "1.2.0"`. `ADMITTED_RELEASE_BUILT_AT_UTC` stays `"2026-08-24T18:04:49Z"`: admission compares the manifest timestamp to it (F-01), the instruction bounds this file to the three items, and PF12 §5.1 fixes that timestamp for the adopted cut while C040-07's PF12 drainage records the re-cut version. Nothing else in the file changes; the PF10 §2.12 boundary and every admission check are untouched.
- Cut command (closed rails), after **every** member byte is final: `python scripts/cut_release_manifest.py --version 1.2.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; then `python scripts/release_id_recompute.py --check-manifest-only`; then the cutter with `--check`. `release_id` is `sha256(canonical manifest bytes)`, recomputed on the real branch and recorded in the result artifact; this plan predicts no value.
- Members whose bytes this unit changes and which therefore fix the cut order: `adapter/http_reader.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json` (new), `engine/config/registry_loader.py`. `.json` members must be canonical bytes; `.py` members one final LF (member-format rule).
- Convergence order (PR06's generation order, extended by this unit's owners; every step under closed rails unless stated; each producer re-run on unchanged inputs to prove a fixed point):

| Step | Owner command | Produces / proves |
| --- | --- | --- |
| 1 Source and fixtures | code and schema edits final; `python scripts/make_reader_v1_goldens.py`; `FILES=<test list> bash scripts/make_release_pack.sh`; the A7 generator, ABBA tool and F07 generator edits in place | members pass the member-format rule; goldens and their companions written by owners |
| 2 Cut | cutter, recompute check, cutter `--check` (above) | complete canonical 45-row manifest; `release_id` fixed; fixed point |
| 3 Admission and comparison | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; b=l(); print(b.release_id, len(b.source_identities))"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | real-root admission, 45; eight goldens equal; exit 0 |
| 4 Gate | `python tools/evidence/run_canonical_json_gate.py`; then `--check-only` | gate outputs for the 45-member manifest; 26 targets, six set rules unchanged |
| 5 Updater | `python tools/evidence/update_evidence_index.py`; `--check` | Index/Mirror/path proofs bind the gate outputs and the manifest before publication |
| 6 Config family | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | catalog logs, registry report, bundles, arrays report converge; gate byte-idempotent |
| 7 Live producers | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, vendor keys absent) then refresh `FROZEN_OPEN_ABBA_SHA256` to `sha256sum audit/gates/determinism/open_rails_abba.json`; `python tools/evidence/generate_conjunction_writer_evidence.py` (closed rails); then each owner's `--check` | A7 family with the production row, determinism family, fixture open-rails proof, F07 artifacts regenerated from the admitted root |
| 8 Updater and read-only checks | updater; `--check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `python ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh` | all companions current |
| 9 Sanity | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` must end `summary:PASS`; then the canonical run; `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check`. If a canonical run ever binds the FAIL model, apply the PR06 plan §5.8 pre-binding before the next canonical run | `audit/gates/sanity_pipeline/sanity_pipeline.log` in the PASS model, byte-identical to the tracked bytes, bound; wrapper exit 0 |
| 10 Frozen families | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen digests intact; no write |
| 11 Tests | §8 | every rewritten, new and pinned test passes |
| 12 Candidate-wide | §§10.3–10.6 | every lane green locally; clean tree; attestation rehearsal |

Any change to a member byte after step 2 restarts at step 2; any change to an evidence primary restarts at step 5. Steps 4–10 are re-runnable and must be byte-stable on the second run.

### 5.10 Failure tokens

None added. `ERR_NOT_FOUND` (405 refusals) and `ERR_READER_INVALID_VERSION` (400) are existing governed tokens; `engine/compat/error_tokens.py` and `errors/token_map/token_map.json` are unchanged, so no token-map regeneration runs.

### 5.11 CI classifier registrations — `ci/checks/classify_ci_changes.py` (registration only; D-16)

| Table | Entry |
| --- | --- |
| `_PRODUCT_TEST_OWNER_PATHS` | `adapter/factory.py` → (`tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py`, `tests/http/test_endpoint_catalog.py`); `adapter/wsgi.py` → the same three; `schemas/reader.v2.schema.json` → (`tests/reader_v1/test_schema.py`, `tests/reader_v1/test_goldens.py`, `tests/config/test_production_admission.py`); `schemas/reader.v2.schema.json.sha256` → (`tests/reader_v1/test_schema.py`); `scripts/make_reader_v1_goldens.py` → (`tests/reader_v1/test_goldens.py`); `scripts/make_release_pack.sh` → (`tests/reader_v1/test_release_pack.py`); `engine/runtime/public.py` gains `tests/http/test_reader_post_v2.py`; `presenter/reader_v1/emitter.py` gains `tests/reader_v1/test_emitter.py` |
| `_FIXTURE_LANE_PREFIXES` / `_FIXTURE_TEST_OWNER_PREFIXES` | `goldens/reader/` → lanes `{product, compat, release}`; owners (`tests/reader_v1/test_goldens.py`, `tests/reader_v1/test_release_pack.py`) |
| `_EVIDENCE_GENERATOR_TEST_OWNERS` | `tools/evidence/generate_conjunction_writer_evidence.py` → (`tests/evidence/test_dev_conjunction_identity.py`) |
| `_HTTP_READER_TEST_OWNERS` | `tests/http/test_reader_post_v2.py` (a direct importer; required by the ownership guard) |

No other table changes. `artifacts/release_pack_manifest.json` and `artifacts/release_id.txt` already classify to the evidence lane. The classifier coherence tests (`tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_http_reader_ci_ownership.py`) are run after registration (§10.2).

### 5.12 Ingress scope

No repository artifact defines an ingress policy (F-17). The production route falls inside `/api`-scoped policy by construction: it is mounted only under the `/api` prefix and the production handler is reachable at no other path (§5.2). The infrastructure-side policy is not a repository deliverable; it is recorded for OPS01 / the Product Owner (§13.2 O-P06a-09).

## 6. Exact file and component plan

### 6.1 Owned loci (instruction §6)

| Path | Change | Why |
| --- | --- | --- |
| `adapter/http_reader.py` | `_select_reader_version`; `get_reader_api_bp` / `api_bp` with `POST /reader` and the method-catch 405; `_reader_post(emit_fn)` shared handler with v1/v2 emission; `_evaluate_reader_pair` returns the ordered bands; unprefixed `POST /reader` becomes the governed 405 stub; `create_app` registers `api_bp` at `/api`; `_emit_conjunction_response` reads the dev seam | §§5.1–5.3, 5.8 |
| `adapter/factory.py` | registers `api_bp` at `url_prefix="/api"` next to `bp` | §5.2 |
| `adapter/wsgi.py` | registers `api_bp` at `url_prefix="/api"` next to `reader_bp` (the route mechanism requires it: this factory otherwise lacks the production route) | §5.2 |
| `engine/runtime/public.py` | `reader_version` and `categories` keywords; v2 validation and envelope; v1 path unchanged | §5.3 |
| `presenter/reader_v1/emitter.py` | `emit_reader_v2`; shared `_emit`; v1 refuses non-`{id, band}` keys | §5.3 |
| `engine/presenter/emitter.py` | no change (the existing emission path needs none) | §5.3 |
| `schemas/reader.v1.schema.json`, `.sha256` | F05 corrections in canonical bytes; sidecar refreshed | §5.4 |
| `schemas/reader.v2.schema.json`, `.sha256` | **new** release member and sidecar | §5.5 |
| `goldens/reader/v1/*` | regenerated by the owning writer; three files renamed, one added; legacy shapes replaced | §5.6 |
| `goldens/reader/v2/*` | **new** family and sidecars | §5.6 |
| `docs/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json` (+ `.sha256`) | production row, through the owner | §5.7 |
| `tools/evidence/generate_conjunction_writer_evidence.py`, `artifacts/writer/*` | closed-rails deterministic capture with the admitted identity; artifacts regenerated | §5.8 |
| `ci/checks/classify_ci_changes.py` | registrations of §5.11 only | §5.11 |
| `engine/config/registry_loader.py` | roster membership (+1), invariant 45, version `1.2.0` — nothing else | §5.9 |
| `catalog/manifest.json` | cut by the cutter only: 45 rows, `1.2.0`, `2026-08-24T18:04:49Z` | §5.9 |
| Test homes (instruction §6): `tests/http/` (`test_reader_post_v1.py`, **new** `test_reader_post_v2.py`, `test_reader_a7_transport.py`, `test_endpoint_catalog.py`, `test_dev_conjunction_http.py`), `tests/reader_v1/` (`test_schema.py`, `test_goldens.py`, `test_emitter.py`, `test_release_pack.py`), `tests/evidence/test_dev_conjunction_identity.py`, `tests/runtime/test_identity.py`, and the runtime-identity/release/manifest homes of §8.8 | §8 | |
| Index/Mirror rows, path proofs, config artifacts, registry report, bundles, gate outputs, determinism and A7 families, sanity log | only through their owning writers (§5.9) | |

### 6.2 Coherence dependents outside the §6 list (no gate semantics; §14.3)

| Path | Change | Class |
| --- | --- | --- |
| `tools/evidence/generate_a7_transport_proofs.py` | one catalog row, one validator rule, the production POST probe path, `PROOFS[4]` text | owning writer of the named catalog loci (D-11) |
| `tools/evidence/generate_open_rails_abba_proof.py` | `FROZEN_OPEN_ABBA_SHA256` refreshed to the regenerated primary | frozen-digest coherence, PR06 precedent (D-12) |
| `scripts/make_reader_v1_goldens.py` | v1 covenant set; v2 section | owning writer of the named goldens loci (D-09) |
| `scripts/make_release_pack.sh`, `artifacts/release_pack_manifest.json`, `artifacts/release_id.txt` | default list renamed; the two tracked outputs regenerated by running the script | companions of the goldens family consumed by an owned test home (D-13) |
| `tests/transport/test_a7_transport_proofs.py` | proof text and probe path; catalog-row assertions | the transport test home covering the changed seam (overlay: "existing … transport … endpoint-catalog … test homes") |
| `tests/evidence/test_rails_ci_workflow_integration.py` | only if a pinned classifier expectation breaks on registration (none identified by reading) | evidence test home covering the registration seam |

### 6.3 Governed evidence regenerated by owners (never hand-edited)

Config family (`artifacts/thresholds/*`, `artifacts/registry/registry_report.json`, `artifacts/config_bundles/{fe,be}_bundle.json`, `artifacts/catalog/*.log`, `artifacts/canonical/arrays_as_sets_report.log`), canonical JSON gate outputs (`audit/gates/canonical_json/*`, `audit/gates/json_gate/canonical/*`), determinism family (`audit/gates/parity/reader_cli/{ab,ba,summary}.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256`, `artifacts/cards/a3/IDENTITY_OK.txt`), open-rails fixture proof (`audit/gates/determinism/open_rails_abba.json`), A7 family (`docs/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/audit/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/*` of that family), F07 writer artifacts (`artifacts/writer/*`), the sanity log, and every Index/Mirror/path-proof/orientation companion through the sole updater. The rehearsal saw 44 files change for the cut alone (§3.3); the real candidate adds the A7 catalog bytes, the writer artifacts and whatever the owners decide.

### 6.4 Frozen families (stay frozen, with nonclaims)

`artifacts/cli/showcompat/*`, `artifacts/cli/{ab,ba,summary}.json`, help/install captures (EPIC022 D2 / CLI conformance); `artifacts/identity/*`, `artifacts/math/*`, `artifacts/parity/two_run_identity.log`, `artifacts/bodygraph/release_bindings.json`, `artifacts/runtime/env_matrix.snapshot.json` (capture-time identity evidence regenerated only by the isolated closure inside the attestation, per `AGENTS.md`; the attestation rehearsal passed with them frozen); `artifacts/vendor/*`, `audit/ops/*`, EPIC032 router captures. Their `--check` modes exit 0 on the re-cut (§3.3).

### 6.5 Consequence for CI lanes

The candidate changes `ci/checks/classify_ci_changes.py`, so full validation applies: all seven lanes plus `_FULL_VALIDATION_SUPPLEMENTAL_TESTS`. Independently: `catalog/manifest.json` selects `release`; `adapter/http_reader.py` selects `product`/`compat`/`db`/`release`; the schemas, presenter and factories select `product`/`compat`/`release`; the catalog and evidence select `evidence`/`release`; the F07 generator selects `evidence`. The `RELEASE_NOT_ADMITTED` branches of the rails and release lanes are never taken.

### 6.6 Explicitly unchanged paths

`engine/compat/**` (including `compute.py`, `error_tokens.py`, `errors.py`, `identity.py`), `engine/bodygraph/**`, `engine/cli/main.py`, `engine/emit_public.py`, `engine/presenter/emitter.py`, `engine/serializer/**`, `engine/stable/**`, `engine/categories/registry.py`, `scripts/hd_cli.py`, `scripts/cut_release_manifest.py`, `scripts/release_id_recompute.py`, `tools/evidence/run_canonical_json_gate.py` (its roster constant is already bound to `ADMITTED_RELEASE_ROSTER`), `tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/run_sanity_pipeline*.py`, `tools/evidence/update_evidence_index.py`, `tools/config/**`, `tools/errors/**`, `errors/token_map/token_map.json`, `catalog/*` data, `narratives/**`, `dev/reader_harness/app.py`, `.github/workflows/ci.yml`, `ci/jobs/*.yml`, `pyproject.toml`, `docs/pfcanon/**`, every historical evidence family, `tests/reader_v1/test_cli_proof.py` (D-18).

## 7. Requirement-to-change-and-test mapping

| Requirement | Source | Change | Proof |
| --- | --- | --- | --- |
| Reader v2: `v=2` on `POST /api/reader`; same request, resolution, eligibility, transport, conditional and error behaviour as v1 | C040-07 bullet 1; overlay item 1 | §§5.1–5.3 | §8.1 cases 1–3, 6–7, 9, 11 |
| Six-key numeric-free envelope, `reader_version "v2"` | C040-07 bullet 2 | §5.3 | §8.1 case 1, §8.6 v2 schema |
| Ten `{id, band}` items in canonical governed order, one per identifier, bands from the complete canonical matrix, no omission/duplication/default fill/harmony substitution/viewer mutation | C040-07 bullet 3; PF04 `OI-001` | §5.3 (validated result rows; emitter enforces order) | §8.1 cases 1, 5; §8.6 emitter and schema adverse cases |
| Ordered array, not set-sorted | C040-07 bullet 4 | `emit_reader_v2` | §8.6 (`order preserved`, wrong order refused) |
| Ineligible ⇒ `[]` | C040-07 bullet 5; PF01 §4.7 | §5.3 | §8.1 case 3, §8.6 |
| Canonical JSON, five-key preimage, AB↔BA, two-run identity for v2 | C040-07 bullet 6; PF05 §6.3 | `_emit` shared | §8.1 case 2, §8.6, §8.10 |
| Reader v1 unchanged; v1 schema conformed: `harmony` only, `prompt` removed, six-key closure | overlay item 2; PF01 §§2.1–2.2; PF04 §8.1.3; PF10 §2.17 "What PR07 inherits" rows 1–2 | §§5.3 (v1 path byte-identical), 5.4, 5.6 | §8.2 (dev GET bytes unchanged; CLI parity test unchanged), §8.6 |
| Retired `*_leader` identities leave the published contract; consumers | overlay item 2; PF10 §2.17 row 3 | §5.6; no repository consumer found (instruction §11) | `grep` in review §11.1 |
| Production route `POST /api/reader` for both versions, PF05 §5.6 mechanism and alias posture | overlay item 3; PF10 §2.16 rows 1, 3, 4 | §5.2 | §8.1 case 8, §8.2, §8.3 |
| Catalog rows incl. the O-03 POST row; audit mirror | overlay item 3; PF10 §2.16 row 2 | §5.7 | §8.4, §8.5 |
| Route inside `/api`-scoped ingress | overlay item 3; PF10 §2.16 row 3 | §5.12 | structural (url_map assertion, §8.1 case 8) |
| PR04 plan O-13 superseded | overlay item 3 | recorded in §13.2 O-P06a-05 | — |
| Dev conjunction: real admitted identity, no dev stamp; seam absent by default; generator assertions; registration; artifacts regenerated | overlay item 4; PF10 §2.18 "What PR07 inherits" items 1–4; §2.12 | §5.8, §5.11 | §8.7 |
| Release re-cut: 45 members, `1.2.0`, roster/invariant/version only, admission logic unchanged, cutter, recomputed `release_id`, owners converge, strict attestation | overlay item 5; instruction §5.5; PF12 §5.1 | §5.9 | §8.8, §10.4–10.6 |
| Version selection strict; missing/unsupported/duplicated/malformed refused | overlay proof; PF05 §5.2.4 token | §5.1 | §8.1 case 6, §8.2 |
| No public numeric, prompt, narrative key, score, UUID or Gate value | overlay proof; PF04 §8.1 | unchanged emitters; forbidden-substring scans | §8.1 case 1, §8.2 |
| `K040-REQ-010` / `AC040-06` (Reader v1 golden reconciliation, v2 goldens; G001–G008 unchanged) | overlay "Requirements and acceptance effects" | §5.6; `tests/fixtures/magic10/v1/goldens.json` untouched | §8.6; `--compare-goldens` in §10.4 |
| `K040-REQ-012` / `AC040-08` (evidence converges through owners) | same | §5.9 | §10.4 |
| Public full Magic-10 exposure (Product Owner requirement, no `K040-REQ` id) | overlay | §§5.3, 5.5 | §8.1 |
| Completion: code review, security review, ordinary CI incl. attestation on the exact head | overlay "Completion" | §§10–11 | CC-8, CC-9 |

Every other requirement, criterion, allocation and completion burden of Plan v2.1 is unchanged and untouched by this unit.

## 8. Detailed test design

No test is skipped, marked `xfail` or deselected. New test files are created only inside the instruction's homes (D-10). Every positive HTTP case injects the synthetic complete release through `tests/support/pr04_fixtures.inject_seams` unless it says "real admission owner".

### 8.1 `tests/http/test_reader_post_v2.py` (new, in `tests/http/`)

1. Eligible pair on `POST /api/reader?v=2`: 200; key order `["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]`; `reader_version "v2"`; exactly ten items; ids equal `FROZEN_MAGIC10_ORDER`; every band in the enum; bands equal, in order, to `compute.evaluate_pair` on the same parties (in-process oracle); `meta` and `release_id` as in v1; `sercanon(body) == bytes`; headers as v1; no ETag; the v1 FORBIDDEN substrings plus `score`, `prompt`, `shared_key`, `personal` absent.
2. AB↔BA and two-run byte identity for v2; preimage recompute equals `idempotence_hash`.
3. Valid self-pair on v2: 200, `eligible false`, `categories []`, core not reached (patched `compute_core`), one row lookup.
4. The v2 body validates against `schemas/reader.v2.schema.json` (Draft 2020-12, strict integer check as `compute` uses).
5. Golden-derived pairs: for every case of `tests/fixtures/magic10/v1/goldens.json` that carries Gate sets — `M10-G004` (`member_a_gates`/`member_b_gates`), `M10-G005` (both `pairs`), `M10-G008` (`a`/`b`) — build complete charts with those Gates and distinct canonical UUIDs, POST `v=2`, and assert the ten bands equal the case's expected category bands in order (`expected.categories` or `expected.intrinsic.categories`); `M10-G007` (valid self-pair) yields `eligible false`, `[]`. The four kernel-only cases carry no pair and are covered by `--compare-goldens` unchanged.
6. Version strictness on `/api/reader`: absent, `v=`, `v=3`, `v=01`, `v=1&v=1`, `v=1&v=2`, `v=2&v=2` → 400 `ERR_READER_INVALID_VERSION`, `no-store`, no ETag, no DB query.
7. Method refusals: `GET`, `HEAD`, `PUT`, `PATCH`, `DELETE`, `OPTIONS` on `/api/reader` → 405, JSON `ERR_NOT_FOUND`, `Allow: POST`, `no-store`, no ETag; `POST /reader` → 405 `ERR_NOT_FOUND`, `Allow: GET, HEAD`.
8. Mount assertions for `adapter.factory.create_app`, `adapter.http_reader.create_app` and `adapter.wsgi.create_app`: the url_map has `POST /api/reader`, `GET|HEAD /reader`, no `POST` handler at `/reader` other than the 405 rule, and `/api/aux/narrative`, `/internal/version`, `/dev/*` unmoved (the wsgi factory's env guard is satisfied with the closed-rails environment).
9. Real admission owner (no injected bundle): `v=2` on the repository root serves 200 with `release_id == identity_meta()["release_id"]` and ten items.
10. Errors on v2 are the v1 route's: unknown person 404, DB unavailable 503, stored-row defects 503, admission refusal 503 `ERR_M10_MANIFEST_MISMATCH` — a parametrized subset of the v1 matrix, asserting identical bytes for `v=1` and `v=2`.
11. `APP_ENV=production`: `POST /api/reader?v=2` 200; dev `GET /reader` 403.

### 8.2 `tests/http/test_reader_post_v1.py` (existing home; rewrites)

`_post` targets `/api/reader`; every existing v1 case is kept at the new path; the missing-version case stays 400; new: duplicated `v` refused; `POST /reader` is the governed 405; the dev `GET /reader` regression cases are unchanged; the real-admission-owner case asserts the recomputed identity; a new case asserts that the dev `GET /reader` bytes for `fixtures/charts/{alice,bob}.json` are identical to the bytes `emit_reader_public_envelope(eligible=…, harmony_band=…)` produced before the change (recorded as a fixed synthetic-identity golden in the test) — the "dev GET bytes unchanged" proof.

### 8.3 `tests/http/test_reader_a7_transport.py`

The Reader↔CLI parity test is unchanged (v1 family). The A7 invariants test asserts `POST /reader` → 405 `ERR_NOT_FOUND`, no ETag, `no-store`; and `POST /api/reader` with query-only input and `If-None-Match` → 422 `ERR_READER_INVALID_INPUT`, non-conditional.

### 8.4 `tests/http/test_endpoint_catalog.py`

Adds: exactly one `POST /api/reader` row with `public_reader`, `internal false`, `a7_eligible false`, `env_gate "not_applicable_public"`; `success_endpoints` still `[{"method": "GET", "path": "/reader"}]`; `validate_catalog` still returns the `/reader` GET target; `GET /api/reader` on `create_app()` is 405.

### 8.5 `tests/transport/test_a7_transport_proofs.py`

`test_post_reader_is_the_pf05_non_conditional_422_fact` becomes the `/api/reader` fact (proof text `POST /api/reader\nstatus=422\n…`); a live-matrix case asserts `POST /reader` is not the capture target; the invalid-catalog matrix gains "production row missing" and "two production rows"; `test_build_and_check_succeed_on_the_admitted_root` reproduces the tracked A7 family byte for byte on the real root.

### 8.6 `tests/reader_v1/*`

- `test_schema.py`: v1 — harmony success valid; `open_leader` invalid; `prompt` invalid; extra top-level key invalid; `retry_after_ms` on a success invalid; eligible with `[]` invalid; ineligible with an item invalid; two items invalid; the existing error-shape case unchanged; sidecar test unchanged. v2 — the thirteen cases of §3.3 plus: each of the twelve error pairs valid, a valid token with a wrong message invalid, `$id` and `$schema` constants, sidecar format, the file is canonical bytes (`sercanon(json.loads(raw)) == raw`) for both schemas.
- `test_goldens.py`: v1 — every `*.json` validates against the v1 schema, LF-terminated, sidecar equal; no filename or byte contains `_leader`; jsonl identity. v2 — every `*.json` validates against the v2 schema; the eligible golden's ids are the canonical order; the error golden equals `emit_public(error_envelope("ERR_READER_INVALID_VERSION"))`; jsonl identity; sidecars.
- `test_emitter.py`: v1 — `harmony` cases replace the `*_leader` cases; two-run identity; `prompt` refused (`ValueError`); duplicate refused; schema valid. v2 — ten-in-order bytes; order preserved (not sorted); wrong order, nine items, eleven items, duplicate, `prompt`, unknown band refused; ineligible `[]`; eligible with `[]` refused; preimage coupling; schema valid; exactly one LF.
- `test_release_pack.py`: the FILES list names the new v1 goldens; the script's outputs equal the tracked bytes (the test itself asserts the run leaves `git status` clean for those two paths).
- `test_cli_proof.py`: untouched (D-18).

### 8.7 F07 homes

- `tests/evidence/test_dev_conjunction_identity.py`: closed-rails environment; the subprocess environment deletes `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` and `DATABASE_URL`; `--check` exit 0 and artifacts unchanged; summary `schema` `conjunction_writer_summary.v2`; every check true; `summary["release_id"] == identity_meta()["release_id"]`; `no_dev_identity_stamp` true; the DATABASE_URL neutralization and restore-on-failure cases kept; new: the generator refuses open rails (`SystemExit`) and writes nothing; new: with `HdApiClient.from_env` patched to fail, `main(["--check"])` still returns 0.
- `tests/http/test_dev_conjunction_http.py`: existing cases kept (the closed-rails refusal proves the seam is absent by default); new: with `app.config["DEV_CONJUNCTION_LOCAL_LOOKUP"]` set to a `RowStore` of complete charts, the three dev routes return 200 under closed rails with the injected bundle's `release_id` and no `meta`, the vendor client is never constructed, and the writer is idempotent; new: the production `POST /api/reader` never consults the seam (seam set, DB rows absent → 404 `ERR_M10_PERSON_UNRESOLVED`); new: in `APP_ENV=prod` the seam is unreachable (403 before any lookup).

### 8.8 Pinned-identity rewrites (27 tests, six files; executed inventory of §3.3)

| File | Tests | Rewrite |
| --- | --- | --- |
| `tests/config/test_production_admission.py` | `test_mechanics_fresh_startup_and_optimization_semantics[0..2 × loader,core]` (6); `test_mechanics_timestamp_valid_stale_bytecode_refuses_and_fresh_source_admits[4 paths]` (4); `test_synthetic_complete_release_is_labeled_and_admits_exact_identities`; `test_actual_repository_root_admits`; `test_gate_schema_is_required_and_an_unlisted_43_member_release_is_incomplete` | `"members": 44` → `45`; `len(ADMITTED_RELEASE_ROSTER) == 44` → `45` plus `"schemas/reader.v2.schema.json" in ADMITTED_RELEASE_ROSTER`; `ADMITTED_RELEASE_VERSION == "1.1.0"` → `"1.2.0"`; `len(bundle.source_identities) == 44` → `45`; the 43-member case becomes the 44-member case (name and assertion) |
| `tests/config/test_manifest_schema.py` | `test_generic_manifest_shape_does_not_claim_full_release_admission` | `"1.1.0"` → `"1.2.0"`; `44` → `45` |
| `tests/config/test_execution_coherence.py` | `test_public_fresh_execution_admits_all_four_modules_under_matching_semantics[0..2]` (3); `test_timestamp_valid_stale_bytecode_refuses_but_fresh_b_admits[4 paths]` (4); `test_only_the_exact_44_member_roster_admits[42,43,45]` (3) | `members == 44` → `45`; the roster test is renamed to 45 and parametrized `[43, 44, 46]` with `count < 45` / `HELPERS[:45 - count]` |
| `tests/scripts/test_cut_release_manifest.py` | `test_roster_cut_constructs_exactly_the_admitted_roster` | `len(payload["files"]) == 44` → `45`; the comment "complete to 44 members" → 45 (`_PRE_PR06_MEMBERS` stays the historical 15) |
| `tests/evidence/test_sanity_pipeline.py` | `test_probe_classifies_exactly_the_incomplete_roster_refusal` | `44` → `45` |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` | `test_manifest_validator_binds_the_admitted_roster` | `44` → `45` (26 targets and 6 set rules unchanged) |
| `tests/config/test_config_artifacts.py`, `tests/config/helpers.py` | docstrings "44-member" | → "45-member" (cosmetic; no assertion) |

### 8.9 Classifier and ownership coherence

`tests/evidence/test_rails_ci_workflow_integration.py` and `tests/evidence/test_http_reader_ci_ownership.py` run after the registrations of §5.11; the dry-run of §10.3 must classify every changed path and select every changed test.

### 8.10 `tests/runtime/test_identity.py`

Adds one case: `emit_reader_public_envelope(eligible=True, reader_version="v2", categories=<ten pairs>)` carries `identity_meta()`'s `engine_tag`, `invocation_tag` and `release_id`, ten items, and `emit_reader_public_envelope(eligible=False, reader_version="v2")` carries `[]`.

## 9. Ordered implementation procedure (for PR-30, after the Product Owner's Proceed for this version)

One pull request, one coherent commit series in the order below (D-17). No split is planned: an intermediate state with a moved route but un-cut manifest, or a cut manifest with unconverged evidence, is red on every lane and is not a meaningful checkpoint. Each checkpoint ends with the listed proof; a failing proof stops the procedure at that checkpoint and never proceeds by hand-editing.

### C0 — Preconditions (not implementation)

- Product Owner PR-30 Proceed for exactly this plan version. PR-30 inspects existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06a before creating anything: at planning time none exist; the PR-20 planning branch holds only this document and is not an implementation vehicle; PR #506 holds the instruction only.
- Environment as §10.1, including the absent vendor/DB keys and the `python`-on-`PATH` rule; `origin/main` re-verified; any non-documentation change since `7f58ad6…` re-evaluated against §3.2 before starting.

### C1 — Reader code (§§5.1–5.3)

1. `adapter/http_reader.py`: `_select_reader_version`; `get_reader_api_bp` and `api_bp`; the shared `_reader_post(emit_fn)` with the ordered-bands evaluation and v1/v2 emission; the governed 405 stub on the unprefixed `POST /reader`; the method-catch on `/api/reader`; the dev seam read in `_emit_conjunction_response`; `create_app` registers `api_bp` at `/api`.
2. `adapter/factory.py` and `adapter/wsgi.py`: register `api_bp` at `/api`.
3. `engine/runtime/public.py` and `presenter/reader_v1/emitter.py` per §5.3.
4. Tests §8.1, §8.2, §8.3, §8.10 and the emitter cases of §8.6; run `python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/reader_v1/test_emitter.py tests/runtime/test_identity.py tests/runtime/test_emit_public_legacy_helper.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_cli_canonical_bytes.py`.
5. Proof: the suites above green; `python tools/cli/serializer_grep_guard.py --output <tmp>` and `python tools/cli/emitter_symbol_proof.py --output <tmp>` exit 0 (the CLI symbol set is unchanged); the dev `GET /reader` bytes for the fixtures equal the pre-change bytes.

### C2 — Schemas and goldens (§§5.4–5.6)

1. Write `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json` as canonical bytes (`sercanon(json.loads(raw)) == raw`); refresh/create the `.sha256` sidecars in `sha256sum` format.
2. Edit `scripts/make_reader_v1_goldens.py`; run it; verify `goldens/reader/v1/g01_minimal_ineligible.json` and `g06_error_invalid_input.json` are byte-identical to before and that no `_leader` filename or byte remains; verify the v2 family.
3. Edit the FILES lists in `scripts/make_release_pack.sh` and `tests/reader_v1/test_release_pack.py`; run `FILES=<that list> bash scripts/make_release_pack.sh`; commit the two regenerated artifacts.
4. Tests §8.6; run `python -m pytest -q -p no:cacheprovider tests/reader_v1`. Expect one pre-existing failure only: `tests/reader_v1/test_cli_proof.py` (D-18; recorded in the result artifact, not in the changed-test set).
5. Proof: both schemas canonical, sidecars equal, goldens validate, `git status` clean after the release-pack test.

### C3 — Catalog, A7 and F07 owners (§§5.7–5.8)

1. `tools/evidence/generate_a7_transport_proofs.py`: the catalog row, validator rule, `/api/reader` probe and `PROOFS[4]` text (write mode runs later, in C5).
2. `tools/evidence/generate_conjunction_writer_evidence.py`: closed-rails deterministic capture, seam installation, new checks, `.v2` schema strings (write mode runs later, in C5).
3. Tests §8.4, §8.5, §8.7; run `python -m pytest -q -p no:cacheprovider tests/http/test_endpoint_catalog.py tests/transport/test_a7_transport_proofs.py tests/http/test_dev_conjunction_http.py tests/evidence/test_dev_conjunction_identity.py`. Until C5 the real-root cases that read the tracked artifacts fail by design (`DRIFT`, admission of the not-yet-cut root); the injected-seam cases pass.
4. Proof: injected cases green; `HdApiClient.from_env` is never constructed in any F07 test; the generator refuses open rails.

### C4 — Classifier registrations and pinned tests (§§5.11, 8.8, 8.9)

1. Register the entries of §5.11; nothing else in the classifier changes.
2. Rewrite the 27 tests of §8.8 and the two docstrings.
3. Run `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_http_reader_ci_ownership.py` and the dry-run of §10.3.
4. Proof: every changed path classified; every changed test selected; no `skip`, `xfail` or deselect added.

### C5 — Cut and convergence (§5.9 steps 1–10)

1. Confirm every member byte is final (§5.9 list); cut; recompute check; cutter `--check`; record `release_id`.
2. Steps 3–10 in order; after step 7 refresh `FROZEN_OPEN_ABBA_SHA256` from the regenerated primary and re-run that owner's `--check`; run the F07 generator's write mode then `--check`; after step 8 every read-only check; step 9 sanity (non-canonical first); step 10 frozen families.
3. Proof: `git status --short --untracked-files=all` shows only intended paths; a second run of steps 4–10 changes no byte; `load_active_mechanics_bundle()` admits with the recorded `release_id`; `identity_meta()` agrees; the sanity log equals the tracked PASS model byte for byte.

### C6 — Candidate-wide validation and attestation rehearsal (§§10.3–10.6)

1. Lane-equivalent commands of §10.4 in CI order; supplemental roster of §10.5; the 27 rewritten tests and every home of §8.
2. Attestation rehearsal of §10.6 from a clean committed tree into an external empty directory, then `--verify`. A failure is a finding to record, never something to patch around.
3. Proof: every command exit 0; clean tree after every isolated run.

### C7 — Publication (PR-30's `PR_CANDIDATE_PUBLISHED`)

1. One meaningful commit series on the working branch in the order C1–C5 (code; schemas and goldens; owners and tests; registrations and pinned tests; cut and converged evidence), each commit locally tested; the PR description per `.github/pull_request_template.md` and `AGENTS.md` with the §15 merge statement; the `PR_IMPLEMENTATION_RESULT` under `docs/ephemeral/` naming every command run and its exit code, the before/after digests of every member, the `release_id`, the A7 and F07 artifact digests, the attestation outcome, the classifier outputs, the *In-flight decisions* section, and what was not executed.
2. Hand off to PR-35 in its own dedicated session. PR-35 owns review correction, current-head CI, coherent corrective pushes and `MERGE_PENDING`; Nathan merges.

Recovery at any checkpoint: revert the compatible set together (code, schemas, goldens, generated artifacts, manifest, tests) with `git restore` on the branch; re-run the owners on unchanged inputs; if a member byte changed, restart at C5 step 1. Nothing is hand-edited; nothing is claimed that an owner did not produce.

## 10. Local validation and evidence commands

### 10.1 Environment (as `.github/workflows/ci.yml` installs, plus what the rehearsal needed)

```
python --version                      # CI: 3.12 (actions/setup-python); local rehearsal used 3.11.15
python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version            # readiness proof (AGENTS.md)
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
unset HD_API_BASE_URL HDAPI_BASE_URL HD_API_KEY GEO_API_KEY DATABASE_URL   # for the whole session (R-13)
```

Three environment facts PR-30 must respect: (a) `python` on `PATH` must be the interpreter that carries pytest — `ci/checks/run_rails_job_definitions.py` (rails lane; sanity stage 06) shells out to `python -m pytest` and fails with `No module named pytest` otherwise (rehearsed; §3.3); (b) the editable install must point at the tree being attested, because the scripts the attestation runs inside its isolated copy import `engine` from the installed location (PR06 plan §10.1 (b)); (c) PR06's Debian system-`setuptools` caveat did not recur with `setuptools` 79.0.1 in a virtualenv; if `pip wheel --no-build-isolation` fails with `AttributeError: install_layout`, install a current `setuptools` first.

### 10.2 Focused behavioral and ownership suites

```
python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py tests/http/test_dev_conjunction_http.py tests/http/test_compat_endpoint_contract.py tests/reader_v1/test_schema.py tests/reader_v1/test_goldens.py tests/reader_v1/test_emitter.py tests/reader_v1/test_release_pack.py tests/runtime/test_identity.py tests/runtime/test_emit_public_legacy_helper.py tests/transport/test_a7_transport_proofs.py tests/evidence/test_dev_conjunction_identity.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_sanity_pipeline.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_release_attestation.py tests/config/test_production_admission.py tests/config/test_manifest_schema.py tests/config/test_execution_coherence.py tests/config/test_config_artifacts.py tests/scripts/test_cut_release_manifest.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_errors_parity.py tests/evidence/test_rails_ci_workflow_integration.py tests/evidence/test_http_reader_ci_ownership.py
```

### 10.3 Classifier dry-run and changed-test isolation (as `ci.yml` runs them)

```
python ci/checks/classify_ci_changes.py --base origin/main --head HEAD --event-name pull_request --github-output /tmp/gh_out.txt --changed-tests-output /tmp/changed_tests.txt
# expect every lane true (classifier change ⇒ full validation) and no CI_CHANGE_SURFACE_UNCLASSIFIED / CI_PRODUCT_OWNER_TEST_MISSING / CI_EVIDENCE_OWNER_TEST_MISSING
git worktree add --detach /tmp/pr06a-changed-tests HEAD && (cd /tmp/pr06a-changed-tests && PYTHONPATH=$PWD python -m pytest -q -p no:cacheprovider -- $(cat /tmp/changed_tests.txt) && git diff --exit-code && test -z "$(git status --short --untracked-files=all)")
```

### 10.4 Lane-equivalent validation (commands verbatim from `.github/workflows/ci.yml`, in lane order)

product: `python tools/order/generate_ordering_artifacts.py --check`; `python -m pytest -q tests/order tests/mech/test_order_properties.py tests/evidence/test_architecture_snapshot.py`.
compat: `ci/checks/check_cli_help.sh`; `python tools/cli/serializer_grep_guard.py --output <tmp>/serializer_grep_guard.log`; `python tools/cli/emitter_symbol_proof.py --output <tmp>/emitter_symbol_proof.txt`; `python -m pytest -q tests/adapter/test_jsonschema.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_errors_parity.py tests/cli/test_cli_canonical_bytes.py tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_serializer_guards.py tests/transport/test_internal_version_contract.py tests/http/test_compat_endpoint_contract.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py`.
db: `python ci/checks/check_direct_db_contract.py`; `python -m pytest -q tests/db tests/unit/test_check_direct_db_contract.py tests/bodygraph/test_bg_resolve_v2_mapped_cache.py tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py tests/bodygraph/test_ingest.py tests/ops/test_capture_rails_open_scope.py tests/ops/test_http_logging.py`.
rails: `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` (must exit 0, never 3); `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`.
evidence: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/refresh_step_logs_manifest.py --check`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh` (a Python script with a `.sh` name: execute it directly or via `python`, not `bash`); `ci/checks/check_final_lf.sh`; `python -m pytest -q tests/evidence/test_evidence_index_missing_state.py tests/evidence/test_evidence_skeleton.py tests/evidence/test_machine_mirror_self_proof.py tests/evidence/test_orientation_demo.py tests/ops/test_evidence_index.py tests/qa/test_epic020_qa_docs.py`.
qa: the qa pytest set of the workflow in a detached worktree with the clean-tree assertion.
release: `git diff --exit-code`; `python scripts/release_id_recompute.py --check-manifest-only`; `python -m pytest -q tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` in a detached worktree; then §10.6.

### 10.5 Candidate-wide roster

`_FULL_VALIDATION_SUPPLEMENTAL_TESTS` from `ci/checks/classify_ci_changes.py` (the 40-path list), plus `tests/evidence/test_canonical_json_gate_check_outputs.py tests/evidence/test_determinism_gate_proofs.py tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_release_bindings.py tests/scripts tests/core/test_engine_core_purity.py tests/unit/test_narratives_loader.py tests/unit/test_narratives_router.py tests/evidence/test_internal_version_manifest_captures.py tests/evidence/test_http_reader_ci_ownership.py`, plus every home of §8. Do not run bare `pytest tests`: it collects legacy modules that fail at import and proves nothing (PR06 plan §10.5).

### 10.6 Attestation rehearsal and the recorded planning outcome

```
python tools/evidence/build_release_attestation.py --output "$RUNNER_TEMP/hde-release-attestation" --require-clean
python tools/evidence/build_release_attestation.py --verify "$RUNNER_TEMP/hde-release-attestation" --require-clean
git diff --exit-code && test -z "$(git status --short --untracked-files=all)"
```

Planning rehearsal record (scratch clone at the converged 45-member cut, committed there; inference support only): build exit 0; `--verify` exit 0; `release_admission PR06R_B_FINAL_PASS`; `validation_result PASS`; `release_id` equal to the scratch manifest digest; 174 files bound; 14 declared outputs under `omitted_files` with the builder's existing secret-safety reason codes (the same set PR06 recorded); tree clean afterwards; 79 seconds. The attestation on the real candidate remains `NOT EXECUTED` until PR-30 runs it (C6) and CI runs it in the release lane.

### 10.7 Result record

PR-30 writes `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.0.md` with: every command of §§10.2–10.6 and its exit code; the before/after digests of the six changed members and the two schemas' sidecars; the manifest bytes and `release_id`; the golden report digest; the A7 and F07 artifact digests; the `FROZEN_OPEN_ABBA_SHA256` value; the sanity log model and its binding; the attestation bundle digest (or its failure receipt); the classifier outputs; the pre-existing `test_cli_proof` failure; not-executed items with reasons; the *In-flight decisions* section; and the same distinctions (verified / inferred / not produced / not executed) this plan uses.

## 11. Code review and security review checklist

### 11.1 Code review (PR-session, on the current substantive change)

- Version selection: `getlist` exact; absent, empty, duplicate, unsupported and malformed values refused before any body read or lookup; dev GET accepts `1` only; token, status and headers unchanged.
- Route: the production handler exists once (`_reader_post`) and is reachable only through `api_bp` at `/api/reader`; every factory registers `api_bp` at `/api`; the unprefixed `POST /reader` is the governed 405; the `/api/reader` method-catch carries `Allow: POST`; no other route moved; `/api/aux/narrative` still served by its own decorator.
- Projection: bands are read from the validated result rows in their validated order; `harmony` is asserted first; no second calculator; `emit_reader_v2` refuses everything but exactly ten `{id, band}` in `FROZEN_MAGIC10_ORDER`; the array is not sorted; v1 path byte-identical (dev GET golden in §8.2); `_emit` is the single hashing path; every byte still leaves through `engine.presenter.emitter.emit_public`.
- Schemas: canonical bytes; v1 changes are exactly the three overlay items plus the restructuring that expresses them; the v1 error branch is semantically unchanged; v2 `$id`, draft, ten `prefixItems` in order, `items: false`, twelve exact pairs; sidecars in `sha256sum` format.
- Goldens: produced by the writer, not by hand; no `_leader` remains; `g01`/`g06` bytes unchanged; the release-pack outputs equal a fresh script run.
- A7 owner: one row, one rule, one probe path, one proof text; `success_endpoints` untouched; regenerated bytes equal a fresh write; `endpoints_snapshot.json` unchanged.
- F07: the seam key is read only in the dev routes after the gate; absent from every factory's config; the generator refuses open rails, neutralizes `DATABASE_URL` in both modes, builds rows from repository fixtures only, records the control refusal; no `dev_compat_identity` import; artifacts equal a fresh write.
- Admission: `registry_loader.py` diff is exactly three lines (roster entry, `45`, `1.2.0`); timestamp constant untouched; the cut used `--roster-from-admission`; `release_id` in the result equals `sha256(catalog/manifest.json)`.
- Evidence: every changed governed artifact has an owner command in the result record (`git log -p` on evidence paths shows only owner-produced diffs); `FROZEN_OPEN_ABBA_SHA256` equals the digest of the regenerated primary; Index/Mirror/path proofs/orientation converge under `--check`.
- Tests: no skip/xfail/deselect; the 27 rewrites assert 45 / `1.2.0`; every new HTTP test that imports `adapter.http_reader` is registered; the F07 tests delete the vendor keys and patch the vendor client.
- Classifier: exactly the registrations of §5.11; coherence tests green; dry-run selects every changed test.
- Nothing under `docs/pfcanon/`, `engine/compat/`, `engine/bodygraph/`, `.github/workflows/` changed; no token-map, attestation schema or wire-value change.

### 11.2 Security review (new public route and dev seam)

- `POST /api/reader` keeps the bounded body read (`_READER_MAX_BODY_BYTES + 1` stream read before any parse), the exact two-UUID grammar, the read-only parameterized current-row lookup, value-free refusals, `no-store` on every error, no ETag on POST, no identifier leakage on 404.
- `v=2` adds no request field, no numeric, prompt, narrative key, score, UUID or Gate value to any public body (forbidden-substring scans in §8.1/§8.2).
- The 405 refusals emit governed `error_v1` bytes, never framework HTML; no path information in any error.
- The dev seam is unreachable outside `APP_ENV ∈ {dev, test, local}` (gate before the read), is never consulted by the production route, and defaults to absent; a configured callable can only supply rows that still pass `_bind_lookup_hit`'s identity binding and full admission — it cannot bypass §2.12.
- The F07 generator cannot reach a vendor (closed rails required) or a database (`DATABASE_URL` neutralized); its artifacts carry the public admitted identity and no secret, birth or Gate value (`validate_retained_text_safety` runs inside the attestation; the keys-only redaction job runs in the rails lane).
- The `/api`-scoped placement removes the production handler from the unprefixed path (PF10 §2.16 §4 item 2); the infrastructure-side policy is recorded for its owner (§13.2).
- Attestation output only to an external empty directory; nothing written inside the repository by the builder.

## 12. Risk register and recovery

| ID | Risk | Treatment |
| --- | --- | --- |
| R-01 | A member byte changes after the cut (a review correction to `adapter/http_reader.py`, a schema edit) | any member change ⇒ re-cut (C5 step 1) and restart convergence at §5.9 step 4; the cutter `--check` and `check_manifest_only` in the release lane catch a stale cut (rehearsed: an un-re-cut member refuses `ERR_M10_MANIFEST_MISMATCH`) |
| R-02 | The v1 error branch is left non-conforming to the route's bytes | recorded as candidate C040-08 (§13.1) with interim treatment; v1 success validation is the overlay's proof; no client is served by the v1 error schema today |
| R-03 | `getlist` strictness rejects a client that today sends `v=1&v=1` | PF05 requires refusal of a duplicated selector; no repository consumer sends it |
| R-04 | Moving the production handler breaks an unknown external consumer of `POST /reader` | PF05 §5.6 names `/api/reader` as the production route; `POST /reader` answers a governed 405; no repository consumer found; a consumer found later returns to change control (instruction §11) |
| R-05 | `FROZEN_OPEN_ABBA_SHA256` not refreshed ⇒ rails lane and sanity stage 06 red | §5.9 step 7; §8.9; rehearsed |
| R-06 | Sanity canonical run binds the FAIL model after a transient failure | PR06 plan §5.8 pre-binding; the non-canonical run first; never hand-edit the log |
| R-07 | `test_release_pack.py` rewrites tracked artifacts in CI's worktree | the script's outputs are committed after the final golden bytes (D-13); the test asserts byte-idempotence |
| R-08 | New `goldens/reader/v2/` or a renamed golden is `CI_CHANGE_SURFACE_UNCLASSIFIED` | registration of §5.11; dry-run of §10.3 |
| R-09 | `tests/http/test_reader_post_v2.py` unregistered ⇒ ownership guard red | `_HTTP_READER_TEST_OWNERS` registration (§5.11) |
| R-10 | Golden-derived proof depends on fixture identities | charts are built from the fixture Gate sets with test UUIDs; bands compared to the fixture's expected rows; kernel-only cases excluded by construction (§8.1 case 5) |
| R-11 | CI Python 3.12 vs local 3.11 | lane-equivalent runs are evidence of behaviour, not of CI; CI on the exact head remains the record |
| R-12 | Attestation rehearsal blocked by packaging environment | §10.1 (b)–(c); record the environment in the result |
| R-13 | Vendor or DB credentials present in the developer's environment turn an F07 or open-rails test into a live call or a write | §10.1 unsets them for the session; the corrected generator refuses open rails and neutralizes `DATABASE_URL`; the corrected tests delete the keys and patch the vendor client; the open-rails ABBA proof runs in fixture mode |
| R-14 | The v2 emitter is called with rows from a non-admitted source | it is called only from `_reader_post` after real admission and result validation; the runtime and the emitter both enforce ten-in-order |
| R-15 | PR07 (documentation) or OPS01 assume the 44-member release | the overlay reassigns OPS01 to the 45-member release; §15 states the merge-order dependency |
| R-16 | `tests/reader_v1/test_cli_proof.py` is mistaken for a PR06a regression | pre-existing baseline failure (F-12), untouched (D-18), recorded in the result; it is in no CI lane or roster |

Recovery: roll back the compatible set together on the branch; re-run owners on unchanged inputs; re-cut on member change; on convergence failure claim nothing and hand-edit nothing (instruction §11).

## 13. Carried `CANON_CONFLICT_REGISTER` and observations

### 13.1 `CANON_CONFLICT_REGISTER` (carried from Plan v2.1 §11, Plan Review v2.1 §6, PF10 §§2.2–2.5, 2.19, 2.20, 2.22, 2.23 and the instruction §12; no entry reopened, relabeled, omitted or newly decided)

| Entry | Classification / status | Decision lineage | PR06a note |
| --- | --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z (PF10 §2.2) | carried |
| C040-02 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | current controlled PF12 is repository v2.9.5; used as such (§2.2); the register's recorded v2.9.6 stays with the PF12 maintainer (overlay "Unresolved items") |
| C040-03 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-04 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-05 | `CANON_RECONCILIATION` / `APPROVED`, alternative A | Isis-49, 2026-09-09T03:57:16Z (PF10 §2.3) | carried; PF14 §6.7 correction pending, non-gating |
| C040-06 | `NEW_CANON` / `APPROVED`, alternative A | Isis-50, 2026-09-09T11:48:08Z (PF10 §2.5) | carried; PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |
| C040-07 | `NEW_CANON` / `APPROVED` by the Product Owner, 2026-09-26 (PF10 §2.23) | public full Magic-10 via Reader v2; Reader v1 unchanged | the contract this unit implements (§§5.3, 5.5); drainage into PF01, PF04, PF05, PF12 and the consequential PF14/PF29 statements belongs to their maintainers and is non-gating for PR06a |

**Candidate entry recorded by this plan (PROPOSED; not decided here; reviewer fields not yet reviewed):**

| Field | C040-08 (candidate) |
| --- | --- |
| Classification | `CANON_RECONCILIATION` (proposed) |
| Conflicting sources | PF05 v2.5.2 §5.2.1 and §5.2.3.1 (the Reader error envelope is exactly `schema`, `ok`, `code`, `error`; `schema` fixed `"v1"`) versus PF01 v1.3.7 §2.3 ("The pinned `error_envelope` also emits `schema` and can emit `details`; neither field is permitted by this Reader error contract") and PF04 v2.8.6 §8.1.2 ("only `{ ok:false, code, error }` are allowed") |
| Evidence | the route emits `{"schema":"v1","ok":false,"code":…,"error":…}` (tests pin it); `schemas/reader.v1.schema.json` rejects those bytes (F-05); PF01 §2.3's own routing clause assigns transport ownership to PF05 |
| Conflict statement | canon disagrees on whether the public Reader error envelope carries `schema` |
| Affected requirements | the v1 schema's error branch (left unchanged by this unit, D-06); the v2 schema's error branch (follows PF05 and the actual bytes, D-07); no `K040-REQ` |
| Alternatives | (A) PF05 governs transport bytes, PF01 §2.3 and PF04 §8.1.2 drain to admit `schema`; (B) PF01/PF04 govern and the route drops `schema` — a wire change touching every governed HTTP error surface |
| Recommended disposition | A |
| Interim treatment | v2 schema expresses the actual production error bytes; v1 error branch untouched; no route change |
| Unresolved risk | a client validating v1 errors against the published v1 schema rejects real errors (pre-existing, unchanged by this unit) |
| Permanent drainage target and owner | PF01 §2.3 and PF04 §8.1.2 maintainers via the register owner (the whole-change IA; Isis disposition) |
| Status | `PROPOSED` by this plan; reviewer / reviewed artifact / decision time / rationale: not yet reviewed |

Neither `HDE-EPIC040-PR07-F01` nor any PR06a planning decision is a register entry. The O-01 token-naming tension remains with the PF01/PF05 maintainers.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner |
| --- | --- | --- |
| O-P06a-01 | `docs/pfcanon/` holds five PF10 files (`v13.3` through `v13.3.4`); only v13.3.4 is read under PF10 §6 (instruction N-01) | Nathan |
| O-P06a-02 | The instruction (PR #506) is not on `main` at planning time; this plan reads it from that PR's head and carries its digest | Nathan (merge of #506) |
| O-P06a-03 | `tests/reader_v1/test_cli_proof.py` fails at the baseline: `scripts/hd_cli.py` (a legacy EPIC004 script that emits a synthetic `open_leader` envelope from `artifacts/release_id.txt`) exits 2 `ADMIN_FLAG_REQUIRED` for the test's `--admin-out` call; in no lane or roster; untouched by this unit | Product Owner / legacy script owner |
| O-P06a-04 | At the baseline `tests/reader_v1/test_release_pack.py` rewrites the tracked `artifacts/release_id.txt` (stale since PR06's canonicalization of the v1 schema); this unit regenerates both release-pack artifacts through the script (D-13), which also repairs the staleness | legacy release-pack owner |
| O-P06a-05 | PR04 plan v1.2 item 5 / R-18 / O-11 (the "same declared route" premise) and its correction note O-13 are superseded by this unit's route mechanism, as the overlay states; the note itself is history and is not edited | history |
| O-P06a-06 | `GET /api/reader` (and every non-POST method there) is an ungoverned framework HTML 405 on any `/api` mount today; this unit makes it governed | fixed here |
| O-P06a-07 | Admission validates schema members as schema documents only for a fixed list; `schemas/reader.v2.schema.json` is admitted as canonical JSON and its draft/`$id` are pinned by tests; extending `_validate_admitted_schema_documents` is admission logic and outside this unit's bound | admission owner (PF10 §2.12) |
| O-P06a-08 | The re-cut reuses `built_at_utc 2026-08-24T18:04:49Z` because admission compares it to a constant the instruction bounds this unit not to touch and PF12 §5.1 fixes it; a fresh timestamp would be a one-line constant change plus PF12 drainage — a Product Owner / PF12 decision, not made here | Product Owner; PF12 maintainer (C040-07 drainage) |
| O-P06a-09 | No repository artifact defines the `/api`-scoped ingress policy; the route is inside `/api` by construction; the infrastructure policy itself is OPS01's / the Product Owner's | OPS01 / Product Owner |
| O-P06a-10 | `engine/compat/identity.py::dev_compat_identity` has no consumer after this unit; removal is its owner's call (outside the loci) | engine owner |
| O-P06a-11 | Every re-cut must refresh `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` (a digest of a regenerated primary pinned in code); a structural coupling the proof owner may want to replace with a Mirror-bound digest | open-rails proof owner |
| O-P06a-12 | `ci/checks/run_rails_job_definitions.py` resolves `python` from `PATH`; a virtualenv not on `PATH` makes sanity stage 06 fail with `No module named pytest` | CI owner (cosmetic; CI installs into the runner interpreter) |
| O-P06a-13 | This planning container carried vendor and DB credentials; two rehearsal runs under the existing F07 open-rails posture reached the vendor before the keys were unset (§3.3). No repository byte or DB row was affected. The corrected generator/tests cannot repeat it; the environment posture of planning and development containers is the operator's | Nathan / operator |
| O-P06a-14 | CR-01 / O-12: the packaged wheel omits `schemas/**` (package-data is `catalog/*.json` only); the 45th member is omitted too; a packaged install still refuses `MISSING_FILE` | packaging owner / Product Owner |
| O-P06a-15 | `scripts/make_reader_v1_goldens.py` now writes both Reader families under its v1 name; a rename is its owner's call | goldens writer owner |
| O-P06a-16 | The endpoint catalog's `public_reader` classification and the `not_applicable_public` sentinel are used by the new row; PF05 §5.6 says PF12 must register `public_aux`, `aliases`, the public sentinel and the record model before Catalog conformance may be claimed — a C040-07 / PF12 drainage matter; this unit claims no Catalog conformance | PF12 maintainer |
| O-P06a-17 | `dev/reader_harness/app.py` mounts the dev blueprint at `/api` locally and injects the legacy emit helper; untouched; it is a local harness, not a runtime configuration | dev harness owner |
| O-P06a-18 | No Security Review was run against PR06 (its review §1); this unit's completion includes one for its own change (CC-9); PR06's remains the Product Owner's | Product Owner |

## 14. Boundary findings, planning decisions and boundary classification

### 14.1 Findings

No `FINDING_REF` is raised. No material boundary (PR-20's definition: outcome/objective, acceptance criteria, protected architectural/security/data-model/external-contract boundary, several units' scope, accepted dependency, budget/schedule/risk) was found beyond what the overlay already decides: the external-contract change (Reader v2, the v1 schema correction, the route move) **is** the approved delta of PF10 §2.23. `PR_RETURN_PHASE` does not apply; RS-40 is ineligible.

### 14.2 Planning decisions (D-xx) and their boundary classification

| ID | Decision | Classification |
| --- | --- | --- |
| D-01 | Route mechanism: a second, production-only blueprint mounted at `/api` by every factory; dev `GET /reader` stays unprefixed; the production handler is served nowhere else | in scope — the overlay's "open design choice inside the bound" (PF05 §5.4 alias posture, §5.6) |
| D-02 | Governed 405 refusals for `POST /reader` and non-POST methods on `/api/reader` | in scope (PF05 §5.2 governed error surfaces; pre-PR04 stub posture restored) |
| D-03 | Strict version selection through `getlist`; `ERR_READER_INVALID_VERSION` 400; dev GET accepts `1` only | in scope (overlay proof; existing token) |
| D-04 | v2 bands read from the validated compat result rows; runtime and emitter both enforce ten-in-order; v1 bytes unchanged | in scope |
| D-05 | The v1 emitter refuses a `prompt` key instead of passing it through | in scope (PF01 §2.2 covenant; dead passthrough; no route supplies it); severable |
| D-06 | The v1 schema's error branch is left semantically unchanged; only the overlay's three items and the restructuring that expresses them | in scope by omission; the canon disagreement is C040-08 (§13.1) |
| D-07 | The v2 schema's error branch expresses the production route's actual error envelope per PF05 §5.2.3.1 with the twelve exact pairs | in scope (C040-07: v2 error behaviour is the production v1 route's; PF05 owns transport bytes by PF01 §2.3's routing) |
| D-08 | v1 goldens renamed to their harmony identities, a Glow golden added, `g01`/`g06` unchanged; v2 goldens pin eligible/ineligible/AB↔BA/error | in scope (overlay item 1 and item 2, "through their owning writer") |
| D-09 | The existing goldens writer is extended with a v2 section rather than a new script | coherence; owning writer of named loci |
| D-10 | New v2 tests live in `tests/http/test_reader_post_v2.py` and as sections of the existing `tests/reader_v1/*` files | in scope (instruction §6: new test files only inside the named homes) |
| D-11 | `tools/evidence/generate_a7_transport_proofs.py` changes: catalog row, validator rule, `/api/reader` probe, proof text | coherence dependent — the owning writer of the named catalog loci; a hand edit would violate `AGENTS.md` and fail the owner's `--check`; not material (§14.3) |
| D-12 | `FROZEN_OPEN_ABBA_SHA256` refreshed | coherence dependent; PR06 precedent (`f7484d0`); not material |
| D-13 | `scripts/make_release_pack.sh` list and its two tracked outputs regenerated by the script | coherence dependent — companions of the goldens consumed by an owned test home; not material |
| D-14 | F07: Flask-config seam key, dev-gated, absent by default; generator requires closed rails, neutralizes `DATABASE_URL` in both modes, builds rows from repository fixtures, records the control refusal; `.v2` summary/log schema strings | in scope (overlay item 4; PF10 §2.18 items 1–4) |
| D-15 | `built_at_utc` kept at `2026-08-24T18:04:49Z` | in scope (instruction §5.5 bound; F-01); O-P06a-08 |
| D-16 | Classifier registrations exactly as §5.11 | registration only (instruction §6) |
| D-17 | One PR, ordered commits C1–C7, no split | in scope |
| D-18 | `tests/reader_v1/test_cli_proof.py` and `scripts/hd_cli.py` untouched despite the baseline failure | in scope by omission (outside the changed seams; O-P06a-03) |

No decision here rewrites the Plan, mints a Proceed, reruns an accepted unit, edits PF-Canon, decides a Canon conflict or merges.

### 14.3 Paths outside the instruction's §6 list, classified

The instruction's §6 says a file genuinely required outside its list is a finding for the rescope route (§9), not an implicit extension; its last row admits governed companions "only through their existing owning writers", and its test-home row covers "existing runtime-identity/release/manifest test homes covering changed seams". Four paths outside the literal list are needed, each an owner or companion of a listed locus and none a gate-semantics change; they are classified as coherence dependents, exactly as PR06 classified its classifier registration, error-artifact writer, ABBA tool constant and interval-test rewrites (accepted in PF10 §2.22 §4):

| Path | Why it is not an implicit extension |
| --- | --- |
| `tools/evidence/generate_a7_transport_proofs.py` | the only writer of the listed `docs/ENDPOINTS_CATALOG.json` and its audit mirror; the listed rows cannot exist otherwise (F-08) |
| `tools/evidence/generate_open_rails_abba_proof.py` | a pinned digest of a regenerated governed primary; the listed re-cut cannot converge otherwise (F-09; PR06 did the same) |
| `scripts/make_reader_v1_goldens.py` | the owning writer the overlay itself names for the listed goldens |
| `scripts/make_release_pack.sh` and its two tracked outputs | companions of the listed goldens consumed by the listed `tests/reader_v1/test_release_pack.py` |

This classification is the plan author's and is severable: if the retained whole-change IA reads §6 more strictly, each item can be removed or re-routed without changing any other part of this plan, and the plan would be re-issued as a same-owner correction (PR-20 "SAME-OWNER CORRECTION OR RECOVERY"). No finding is routed, and the state `AWAITING_PO_PROCEED` stands on this classification.

## 15. Manual merge and post-implementation boundary

- Merge is Nathan's alone. PR-30 ends at `PR_CANDIDATE_PUBLISHED`; PR-35 ends at `MERGE_PENDING — Ready to merge`; PR-40 runs after `MERGE_OBSERVED` (or Nathan's assertion where no such result exists) with the retained IA in its read-only role.
- **What merging does.** Merging PR06a makes Reader v2 (`POST /api/reader?v=2`), the production Reader at `/api/reader`, the corrected Reader v1 schema and goldens, the restored dev conjunction capture, and the 45-member `1.2.0` release with its converged evidence current on `main`. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-07 drainage, deployment, activation, Epic closure. The PR description states this under "What merging does", following `.github/pull_request_template.md` and `AGENTS.md` (Why / What changed / Checks run / Not in this PR / What merging does).
- Merge-order dependency: none upstream in code (PR06 landed); the instruction's PR #506 is a documentation record and is not a code dependency; PR07 must follow PR06a; OPS01 verifies the 45-member release (overlay "Work-unit, dependency and status effects").

## 16. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR06a-01`; prior entries carried by reference: `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR06a-01` (instruction §13), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06-01` (PR06 review §6).

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204` (body as read at invocation; Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR06a; Specification v1.1; instruction v1.0.
- Role / stage: dedicated PR06a PR-development session / PR-20.
- Captured: 2026-09-26T04:02:51Z (planning inspection began 2026-09-26T03:11:48Z).
- Execution identity: harness session `https://claude.ai/code/session_01EBvvgYQTXQqvSpd2eHtK8V`.
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent (only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md` exist there); `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

- Receiver: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`; the same dedicated PR06a session (`RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06a / PR-30`; `context_conflict: NONE`).
- Gate: Nathan / Product Owner's manual PR-30 Proceed for exactly `HDE-EPIC040-PR06a-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR06a-PR-INSTRUCTION` v1.0. `AWAITING_PO_PROCEED` is not implementation approval and authorizes no merge, publication, Ops or QA.
- Inputs by repository path: this plan (`docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md`); `docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md` (on `main` once PR #506 merges; until then on that PR's head); `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (the overlay); `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md`; `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md` (§§2.12, 2.16–2.18, 2.21, 2.23); the immutable bases of §2.1.
- PR-30 obligations carried: inspect authorized local roots, repository state, existing worktrees, branches, PRs and `docs/ephemeral/` records for PR06a before creating anything (none exist at planning time; the PR-20 planning branch holds only this document and is not a PR06a implementation vehicle); resume the most advanced consistent state; challenge assumptions and the boundary cases of §8; implement only §§5–6 in the order of §9; test locally per §10 with the keys of §10.1 absent, including the attestation rehearsal; form one coherent meaningful checkpoint series; deliberately publish the initial candidate; `PR_CANDIDATE_PUBLISHED`; hand off to PR-35 in its own dedicated session naming the `PR_IMPLEMENTATION_RESULT` and the PR reference.
- PR-35 obligations carried: review retrieval and correction, local retesting, coherent corrective pushes, CI economy, current-head identity, required checks or a valid waiver, mergeability, genuine merge readiness; no merge. Nathan merges; PR-40 follows `MERGE_OBSERVED`.

### 17.2 Routes not taken

No RS-10 package is emitted: no material boundary was found (§14.1). No `PR_RETURN_PHASE` or RS-40 applies. PR-50 is Nathan's alone and is not a destination.

### 17.3 State summary (truthful states)

| Item | State |
| --- | --- |
| This plan | `AWAITING_PO_PROCEED` — complete, executable within approved scope plus PF10 §§2.12, 2.16–2.18, 2.21, 2.23; pending the Product Owner's PR-30 invocation for v1.0 |
| Boundary finding | none raised; four coherence dependents classified in §14.3 for the IA's confirmation; C040-08 candidate recorded, not decided |
| PR06a implementation, PR, CI, merge | `NOT EXECUTED` |
| PR06a result artifact, PR07, OPS01, QA, Ops, activation, C040-07 drainage, closure | `NOT PRODUCED` / `NOT EXECUTED` |
| Real `release_id`, real evidence bytes, real attestation | `NOT PRODUCED` (rehearsed in scratch clones only, §3.3, §10.6) |
| Instruction PR #506 | open, unmerged at planning time (O-P06a-02) |
| Provenance persistence | `PENDING / NON_GATING` |
