---
artifact_type: IMPLEMENTATION_AUDIT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-AUDIT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: AUDIT_COMPLETE
author: whole-change Implementation Agent (IA) for HDE-CRD-0002 (session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah)
ia_session_binding: this session, assigned by the Product Owner's launch of the IA-10 handoff on 2026-10-12 (handoff state NOT_YET_ASSIGNED; no earlier IA session exists for this change)
prompt: IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb813aa0ccd709ebd134d0)
entry_mode: FIRST_ENTRY
prompt_release: GCFPE-20261009.1 / 100926.1
release_selection_check: GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", exactly 55 members; register entry GCFPE-20261009.1 step X16 "this register's selection updated last" done; read 2026-10-12
created_at: 2026-10-12T20:31:21Z
repository_head_read: origin/main 982071b8203bfed961091811e24f57e99f92e593
specification_ref: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480; 43,151 bytes; sha256 fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df)
specification_reviewed_source: docs/ephemeral/HDE-CRD-0002-specification-v1.1.md (blob 8a3ef0a8930dcb6f610235ee84d68882bfaa80e1; 41,824 bytes; landed on main at fd47cab, amthorn78/glow-hdengine-v2#617)
thoth_decision_ref: docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md (INITIAL_APPROVE, 2026-10-12T19:39:51Z; blob c48f77a0c220d65455f50e3c550a283d0b332a0c; 14,195 bytes)
canon_conflict_register: CR-1, CR-2, CR-3 carried as APPROVED_AS_CHANGED (review v1.0 §6; confirmed in review v1.1 §4); interim treatments applied below, no canon changed
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (PF10-HDE-Build-Notes v13.5.2, effective 2026.10.11, invocation tag INV-f2ac55d77ce9aacc; blob ec71eeecec8b0fcff1645d317211258bc708712c; 13,583 bytes; read in full)
pf10_applicable_addenda: addendum 2.1 only, governing the TypeSafe reading recorded in this artifact; no addendum addresses S01 to S22, so permanent PF canon governs their subject matter (PF10 silence rule)
approved_base_plus_overlays: approved base = Specification v1.1 (approved representation above); applicable PF10 overlays = NONE
next_artifact: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md (IMPLEMENTATION_PLAN, PLAN_PENDING; authored after this Audit in the same invocation)
---

# HDE-CRD-0002 — Implementation Audit v1.0

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Result

**AUDIT_COMPLETE.** Every approved requirement S01 to S22 has a planning disposition (§6). No requirement is blocked. One disposition carries a pending owner decision that gates later reliance, not planning: the S21 ADR (AQ-1, §8). No Specification correction or product/scope decision is returned to its owner: the Audit found no insufficiency, contradiction or ambiguity in the approved Specification that engineering choices within IA authority cannot resolve (§7.1). The approved Specification is not expanded or reinterpreted; where this Audit chose between readings the Specification leaves open, §7.1 records the choice and its basis so that the Plan reviewer can see it.

| Disposition | Requirements |
| :---- | :---- |
| `PLAN_READY` | S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S22 |
| `PLAN_READY_PENDING_OWNER_DECISION` (plannable now; a named owner decision gates later reliance) | S21 (ADR approval by the Product Owner, AQ-1) |
| `BLOCKED` | none |

This Audit authorizes nothing. It is the first IA artifact, consumed by the Plan and its review (HDE Governance §9.1.1 role table). It establishes no implementation, PR Proceed, Ops, QA verdict, acceptance or closure, and it changes no canon.

## 2. Inputs verified (Phase 1, step 1)

| Check | Result |
| :---- | :---- |
| Approved Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, state `SPECIFICATION_APPROVED`, sentinel `ASK OK.`, read in full on `main` at `982071b`. Its line diff against the exact reviewed v1.1 shows only the publication delta its front matter declares (front-matter approval fields; Record control status and last material update; the Specification approval block; one Material-change history row; the Specification decisions line; the three CR status lines). The reviewed v1.1 itself was read in full. |
| Thoth decision | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`: `INITIAL_APPROVE` on exactly v1.1 (blob `8a3ef0a8…`), 2026-10-12T19:39:51Z, by the same CF-C-30 reviewer as review v1.0; `pf10_addendum: none`; routes FIRST_ENTRY to IA-10. Read in full. The predecessor review v1.0 (INITIAL_DENY) was not re-read beyond the passages v1.1 quotes; v1.1 is the approved baseline and its application record is referenced, not relied on. |
| Change class and identity | `CHANGE_CLASS: CRD`, `CHANGE_ID: HDE-CRD-0002` (class-selection record `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md`, CLASS_SELECTED by Nathan / Product Owner, read in full). |
| Source lineage | briefs v1.0 → v1.1 → v1.2 (`docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`, read in full) → kickoff v1.0 → Specification v1.0 (denied) → v1.1 (approved). The kickoff was not re-read; the Specification's "Kickoff open points resolved" table carries its open points U-1 to U-7. |
| Carried register | CR-1 to CR-3 present in the approved representation with status `APPROVED_AS_CHANGED`; interim treatments: no PF30 entry (CR-1); no planned work units in the Specification (CR-2); this Specification is the governing record and `HDE-CRD-0002` is the Product Owner-assigned ID (CR-3). This Audit applies them and uses `audit/qa/hde-crd-0002/` as the CRD QA root (Glow QA Guide "Change-lane QA applicability"; HDE Schemas & Artifacts §8.17). |
| IA session binding | Truthful state: the handoff carried `NOT_YET_ASSIGNED`; the Product Owner launched this top-level session with the IA-10 handoff, so this session (`session_012nUipT8gpdYtjzA5UQk5ah`) is the dedicated whole-change IA session for HDE-CRD-0002 from this invocation on. No earlier IA session, Audit, Plan, work unit, PR, QA artifact or Ops receipt exists for this change (`docs/ephemeral/` listing on `main`; the Notion board card `HDE-CRD-0002 — Candidate CRD Items 5–8` still reads `CRD_PENDING`, "Not started: Specification", which is stale for its owner and was not written to). |
| Isis reviewer binding | Established by review v1.1 §6: Isis authored the Specification in session `session_012tPq26JWVhCYZmcqTidpV2`; IA-30's reviewer session may be assigned at that boundary. Carried, not changed. |
| Release selection | The register selects GCFPE-20261009.1 / 100926.1 / 55; IA-10 at 100926.1 is a member (hub `HDE IA — GCFPE-20261009.1 — 100926.1`, candidate table row `IA-10`). |
| Controlled sources | PFCanon resolved only from `docs/pfcanon/` on `main` at `982071b` (`git diff --stat df23bbf 982071b -- docs/pfcanon` is empty, so canon is unchanged since the Specification's reads). No Google Doc, export or title-similar item was opened. |

## 3. Method, tested states and limits

- **Repository inspection.** Read on the working checkout at `982071b8203bfed961091811e24f57e99f92e593` (equal to `origin/main`), by exact-string and regex search and by reading the governing files. Line numbers below are as of that head.
- **Throwaway executions (no repository write).** (a) A clean export (`git archive HEAD`) of `982071b` was built into a wheel in the session scratchpad with a Python 3.13 virtual environment (`pip wheel --no-deps`, build isolation on) and its contents compared with `ADMITTED_RELEASE_ROSTER` (S01). (b) The set of test files reached by no CI lane, no registered owner target and no `pytest.ini` root was computed by importing `ci/checks/classify_ci_changes.py` read-only (S03). (c) That set was run once in a throwaway clone of `982071b` under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode and database keys unset) with a Python 3.12 virtual environment carrying CI's install (`setuptools>=68 wheel -r requirements.txt -r requirements-dev.txt -e .`), `pytest -q -p no:cacheprovider --continue-on-collection-errors` (S03). An earlier run of the same sweep in a clone that had checked out a stale head (`ad1615d`, 2026-10-06) under Python 3.13 is discarded and not relied on. No live vendor, production or database call was made. No file in the repository was written outside `docs/ephemeral/`.
- **Evidence labels.** Each asserted locus below is `Observed` (read at `982071b`, with path and line), `Canon-cited` (PF title and section) or `Unknown pending discovery` (Change Process Guide §0.5.1 "Plan locus validation labels"; Plan Templates "Repository loci and file minting"). Observed facts prove planning-time repository reality only; the executing PR session re-verifies before editing (Plan Templates, same section).
- **Intake records.** The HDE-EPIC040 records the Specification names were consulted for the original observation rows only (`O-10`, `O-11`, `O-12`, `O-22`, `O-P06a-22`, `O-P06a-23`, `O-P06b-17`, `O-OPS01-01`, `RA-08`, `RA-09`, `RA-12`, `RA-14`, `CC-1`, `CC-2`, `B-1`, `B-2`), read by search, not in full; they are planning context, never current repository truth (Change Process Guide, "Reality Audits MAY be read as historical context only"). PF23 Reality Audits (the canon document) was not read; the PF23 anchors in §5.8 come from those HDE-EPIC040 records and from current inspection.
- **Limits.** The deployed Railway service was not inspected (no Ops authority in IA-10); S01's deployment fact rests on checked-in declarations and Glow Infrastructure §10 (§6, S01). The sweep result (S03) is a one-run, one-environment measurement; it classifies files, it is not a QA result. The S19 security review itself is a work unit, not performed here; this Audit fixes its input set only.

## 4. Controlled sources: PF10 and canon

- **PF10.** The unique current controlled PF10 Markdown is `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md` (one unlettered document; "1.1 Addendum Index" lists `2.1` only). Read in full. Addendum 2.1 ("GCFPE model and reasoning-level guidance is the TypeSafe reading; no AI recommendation is given") governs the TypeSafe reading in §10 and nothing else here. Under PF10's silence rule, authority for S01 to S22 returns to permanent PF canon. Initial Specification approval produced no addendum (review v1.1 front matter), so `approved base + applicable PF10 overlays` = Specification v1.1 (approved) + NONE.
- **Canon applied** is listed with sections in "Canon relied on" at the end of this artifact. Where two canon passages conflict for this change, the carried register governs: CR-1 (no PF30 entry; HDE Governance §9.1.1 over Change Process Guide §1.0.3), CR-2 (no planned units in the Specification), CR-3 (this Specification is the governing record; the CRD ID is the Product Owner-assigned one). No new conflict was found.

## 5. Shared repository facts (current state at `982071b`)

### 5.1 Release identity and admission (Observed)

- `catalog/manifest.json`: version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`, root `catalog/`, 45 members (ASCII-sorted list identical to the roster below).
- `engine/config/registry_loader.py` lines 398–447: `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"`, `ADMITTED_RELEASE_ROSTER` of exactly 45 paths with an import-time `!= 45` invariant (line 448). Admission (`load_active_mechanics_bundle`, line 1506) derives the lexical root from the retained execution provenance of the covered admission modules (line 1341: "the fixed eight-owner set") and reads every member relative to that root; the manifest version and timestamp are compared with the constants (lines 1233–1237) and the member set with the roster (line 1221).
- The cutter `scripts/cut_release_manifest.py --version <semver> --built-at-utc <UTC> [--roster-from-admission] [--check]` changes only the manifest; `scripts/release_id_recompute.py --check-manifest-only` validates it (AGENTS.md "Release identity"; `docs/adr/hde/release_attestation_scaling_adr.md` decisions 1–7).
- Members among the observed loci of this change: `engine/cli/main.py` (S07, S08, S14), `engine/bodygraph/resolver.py` (S14), `adapter/http_reader.py` (S10; S15 only if a route is removed; S02 only if the handler is placed there), `engine/config/registry_loader.py` (every re-cut: the version constant lives in a member), `engine/http/compat_handler.py` and `engine/runtime/public.py` (S19 review inputs; changed only if a confirmed finding needs a fix). Non-members: `pyproject.toml` (S01), `adapter/factory.py` (S02), `ci/**`, `.github/workflows/ci.yml`, `tests/**`, `tools/**` except `tools/bodygraph/check_magic10_gate_readiness.py`, `docs/**`, `.env.example`, `VERIFY.sh`, `dev/**`.
- **Consequence.** Admission compares each member's bytes with the manifest's recorded hash (`_capture_admitted_members`, line 1244 onward; `MISSING_FILE` at line 478; `tests/evidence/test_release_manifest_content_binding.py::test_release_evaluation_rejects_manifest_entries_that_do_not_match_disk`), and PR06b's plan (line 381) records that an intermediate state with a changed member and an un-refreshed manifest refuses admission. So every unit that changes a member byte (S07, S08, S10, S14; S19 only if a fix touches a member) must refresh `catalog/manifest.json` in the same unit through the cutter at the current version and timestamp (`--version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`, as HDE-EPIC040-PR06a's PR-35 did) and converge the generated evidence that binds the release identity. The Specification's "one coherent re-cut" with new admission pins is the single version bump, which lands once, after the last member-changing unit. The convergence order is proven by `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §5.4 steps 1–13 (cut; admission and goldens; canonical JSON gate; updater; config family; live producers including the A7 owner before the updater; engine-core owner after every re-cut, O-P06a-23; read-only checks; sanity; frozen-family checks; stale-binding sweep; tests; candidate-wide lanes). That order is reused by the Plan for every refresh and for the version bump (an `Observed` precedent, not canon).

### 5.2 CI structure (Observed)

- `.github/workflows/ci.yml` (404 lines): one `test` job; `paths-ignore` on `push` and `pull_request` lists exactly four prefixes (`docs/pfcanon/**`, `docs/ephemeral/**`, `docs/graph/**`, `docs/prompt_ecosystem_management/**`, lines 5–17); `concurrency.cancel-in-progress` on pull requests (line 24); classification by `ci/checks/classify_ci_changes.py` (line 53); install `pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` on Python 3.12 (lines 64–80); changed-test isolation in a detached worktree (lines 91–117); seven lanes with explicit pytest lists (`product` lines 126–130, `compat` 141–151, `db` 160–167, `rails` 203, `evidence` 218–224, `qa` 243–250, `release` 277–281); the release lane builds and verifies the attestation and accepts a `release_not_admitted` receipt only with the independent `INCOMPLETE_RELEASE_ROSTER` probe (lines 257–330); final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (line 404).
- `ci/checks/classify_ci_changes.py` (1,958 lines): `_DOCUMENTATION_PREFIXES` lists eight prefixes (lines 106–115: `docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/`); `_FIXED_LANE_TEST_PROVIDERS` and `_FIXED_LANE_TEST_DIRECTORIES` (lines 820–863) mirror the lane lists in `ci.yml`; registered owner tests are collected by `_registered_owner_test_paths()` (lines 965–988) and the changed-test targets by `_full_validation_test_targets()` (lines 990–1000); `_UNKNOWN_SOURCE_SUFFIXES = {".py", ".sh", ".sql"}` (line 865); the unknown-source refusal applies only when `_lanes_for_path` returns `None` (lines 1578–1582); `tools/qa/` and `tests/qa/` receive `{"evidence", "qa"}` unconditionally (line 1657); `_qa_tool_owner_targets` fails closed only for `.py` under `tools/qa/` (lines 1174–1199); `_bodygraph_tool_owner_targets` fails closed for every `_UNKNOWN_SOURCE_SUFFIXES` file under `tools/bodygraph/` (lines 1209–1229). A governed primary under a documentation prefix still selects the evidence lane through `docs/evidence/INDEX.json` (lines 895–925).
- `pytest.ini` `testpaths`: twelve roots (`tests/bodygraph/test_gates.py`, `tests/mech`, `tests/categories`, `tests/config`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/invariance`, `tests/transport`, `tests/support`, `tests/cli`, `tests/db`, `tests/qa`, `tests/m10`). No `ci.yml` step runs bare `pytest`, so the `testpaths` roster is reached by CI only through lane lists and changed-test targets.

### 5.3 Test inventory (Observed; computed at `982071b`)

| Set | Count |
| :---- | ----: |
| `tests/**/test_*.py` files tracked | 278 |
| Reached by a fixed `ci.yml` lane command | 49 |
| Registered owner tests (`_registered_owner_test_paths()`) | 133 |
| Active full-validation changed-test targets (`_full_validation_test_targets()`) | 94 (all exist) |
| Under a `pytest.ini` root | 70 |
| Reached by neither a lane, nor a registered owner, nor a `pytest.ini` root (PR05's O-11 definition) | **130** |
| Reached by neither a lane nor a full-validation target (what CI can ever run) | 135 |
| Under a `pytest.ini` root but reached by no lane and no target | 5: `tests/cli/test_cli_env_pins_epic021.py`, `tests/config/test_config_acceptance_map.py`, `tests/qa/test_epic021_scaffolding.py`, `tests/qa/test_epic022_acceptance_scaffold.py`, `tests/qa/test_epic022_close_pack_ready.py` (the five `_FULL_VALIDATION_INACTIVE_TESTS`, deliberately fail-closed, classifier lines 83–90) |

The 130 files by directory: `tests/` root 5; `adapter` 13; `adapters` 1; `arch` 2; `artifacts` 1; `audit` 7; `bodygraph` 2; `canon` 6; `compat` 4; `compliance` 12; `em` 4; `epic003` 3; `evidence` 28; `hdctl` 5; `identity` 1; `infra` 4; `integration` 1; `loader` 6; `provider` 17; `reader_v1` 1; `scripts` 1; `unit` 6. The full list is reproducible from the method in §3 and is carried into the Plan's S03 unit as its inventory input (the Plan names the 130 paths).

### 5.4 Packaging and the deployed service (Observed; Canon-cited)

- `pyproject.toml`: setuptools build; `packages.find` include `engine*`, `adapter*`, `presenter*`, `catalog*`, `math*`; `package-data` only `catalog = ["*.json"]` and `math = ["*.json"]`; console script `hdctl = engine.cli.main:cli`; version `0.0.0`. No `setup.py`, `setup.cfg` or `MANIFEST.in`. `catalog/narratives/`, `errors/`, `schemas/`, `migrations/` and `tools/bodygraph/` have no `__init__.py`.
- A wheel built from `982071b` (129 entries; top-level `adapter`, `catalog`, `engine`, `math`, `presenter`, dist-info) omits **16 of the 45 members**: `adapter/schemas/error_v1.schema.json`; the five `catalog/narratives/*.json`; `errors/token_map/token_map.json`; `migrations/005_identity.sql`; the seven `schemas/*.schema.json`; `tools/bodygraph/check_magic10_gate_readiness.py`. PR06 (#501) recorded the same class: "a regular wheel built from `6252c5b` omits 15 of the 44 members; installed non-editable and run outside the checkout, admission refuses `MISSING_FILE`" (CR-01 / O-12); the 45th member `schemas/reader.v2.schema.json` (PR06a) is also omitted.
- Deployed service: `Procfile` `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …`; `validation/service_cmd.txt` installs `requirements.txt` only and runs the same factory; Glow Infrastructure §10.1 records exactly these declarations and states "The current Railway setting is not verified". Glow Infrastructure §4.1: provider Railway, project `ample-illumination`, service `glow-hdengine-v2`, base URL `https://glow-hdengine-v2-production.up.railway.app`, build artifact "container image (Railway) — TBD". Glow Infrastructure §2.4 Production — Railway: `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `HD_API_BASE_URL=https://api.humandesignapi.nl/v2`, `GEO_API_KEY={redacted}`, `HD_API_KEY={redacted}`, `DATABASE_URL={redacted}`, `TZ=UTC`, `LANG=C`, `LC_ALL=C`. No checked-in declaration installs the distribution (no `pip install .`, no wheel); no `railway.json`, `railway.toml`, `nixpacks.toml` or `Dockerfile` exists. Glow Infrastructure records no deployment trigger (search for auto-deploy / deploy trigger / on push: none).

### 5.5 HTTP homes (Observed)

- Production app (per `Procfile`): `adapter/factory.py::create_app` mounts `bp` (the dev/internal root blueprint from `adapter/http_reader.py::get_reader_bp`) at `/`, `api_bp` (production Reader) at `/api`, and `compat_blueprint`; its only error shaping is an `after_request` that rewrites HTML 404/405 **on compat paths only** into the governed envelope (lines 14–25). Unknown non-compat paths therefore get Flask's HTML 404 without `no-store` (S02; O-P06a-22 / PR06a CR-03). `adapter/wsgi.py::create_app` (a second app, used by `adapter/app.py`, `scripts/scratch.py` and `tests/compliance/*`) registers app-level `errorhandler(404)` and `errorhandler(405)` returning the `ERR_NOT_FOUND` envelope with `no-store` (lines 53–66) and serves `/internal/healthz` and `/internal/readyz` returning 200 unconditionally (lines 41–51). `adapter/http_reader.py::create_app` (line 1163, "EPIC-005 factory") is a third factory with the same compat-only shaping.
- Dev `GET /reader` gate: `adapter/http_reader.py` line 603 `if os.environ.get("APP_ENV", "dev") != "dev": return _error("ERR_READER_FORBIDDEN", 403)` — served when `APP_ENV` is unset or exactly `dev`; refused for `test`, `local` and every other value (S10). The sampler and conjunction dev routes already use the explicit pattern `_dev_admin_gate` (lines 817–823: served only for normalized `dev`, `test`, `local`; otherwise `ERR_WRITER_FORBIDDEN` 403).
- Routes registered in `adapter/` with no entry in `docs/ENDPOINTS_CATALOG.json` (10 entries; generator `tools/evidence/generate_a7_transport_proofs.py::catalog_obj`, lines 36–48): on `bp` (mounted at `/` by the production factory) `/api/aux/narrative` and `/aux/narrative` (lines 671–672), `/ops/db/unavailable` (747), `/ops/rails/refusal` (789), `/ops/probe/env` (797), `/ops/writer/diagnostic` (1114, 1135, 1147); on `adapter/wsgi.py` only, `/internal/healthz` (41) and `/internal/readyz` (47). That is the eight route strings RA-14 named (S15). The catalog and its audit mirror are both written by that generator's `build()` (line 144, `DOC`/`AUD` with `.sha256` sidecars) and validated by `validate_catalog` (lines 49–70) and by the updater (`tools/evidence/update_evidence_index.py` line 3447); `docs/ENDPOINTS_CATALOG.json` and `artifacts/audit/ENDPOINTS_CATALOG.json` are byte-identical today.

### 5.6 Evidence tooling (Observed)

- Canonical updater `tools/evidence/update_evidence_index.py`: CRD admission constants `CRD_QA_ID = "HDE-CRD-0001"`, `CRD_QA_ROOT_REL = "audit/qa/hde-crd-0001"`, `CRD_QA_KEY = "audit.qa.hde_crd_0001"` (lines 47–51, under "another CRD needs its own explicit admission"); `_crd_qa_entry` (3776), `_load_crd_qa_entries` (3791–3827, builds a `HarnessConfig(crd_id=CRD_QA_ID)`), `publish_crd_check_family` (4897–4945, "governed CRD publication admits only HDE-CRD-0001", line 4911). `tools/qa/qa_harness.py` line 23 `CRD_RE = r"HDE-CRD-[0-9]{4,}\Z"` and `HarnessConfig(crd_id=…)` (59–82) already accept any canonical CRD ID and derive `audit/qa/<crd-id lower-case>`. Tests: `tests/evidence/test_evidence_index_missing_state.py` (`crd_repo` fixture, seven `test_crd_*` cases, lines 363–560) and `tests/qa/test_generic_qa_harness.py` (`test_crd_*`, lines 1365–1500). Both files are in the evidence and qa lanes.
- Attestation builder `tools/evidence/build_release_attestation.py::_install_packaged_console_entrypoint` (lines 341–452): `sys.executable -m pip wheel --no-index --no-deps --no-build-isolation` of the tracked source copy, then a fresh `venv` and `pip install --no-index --no-deps <wheel>`; child environment keeps only `PATH` and `TMPDIR` plus closed rails (lines 328–340). O-10 (PR05 result): under Debian's patched setuptools 68.1.2 the `--no-build-isolation` build fails with `AttributeError: install_layout` before any admission stage; hosted CI (stock setuptools) is unaffected (S06).
- Isolated closure `tools/evidence/regenerate_identity_closure.py`: `release_not_admitted_observed()` (lines 384–393) imports `engine.config.registry_loader` from the ambient interpreter path, so inside the attestation's isolated copy the probe resolves `engine` from the editable install of the source clone, not from the copy (O-OPS01-01; S13); the closure's steps otherwise run `sys.executable` with `cwd=ROOT` (lines 330–350).
- Engine-core evidence: `tests/evidence/test_engine_core_evidence.py::test_current_proofs_bind_actual_sources_and_behavior` (lines 78–97) checks `fixture_kind`, `source_sha256` of `writer.SOURCE_PATHS`, run equality, signal/score vectors and the JSON-compare digests, and never reads the payloads' `release_id`; `tools/evidence/generate_engine_core_evidence.py` writes `release_id` into all four `artifacts/core/*` payloads (PR06b plan F-12). A re-cut without the engine-core owner therefore leaves stale release bindings no gate detects (O-P06a-23; S11).
- Mirror provenance labels: the updater registers current-release captures under their origin families, for example the endpoint catalog and its mirror as `epic038.pr02.endpoint_catalog*` with `"epic_id": "HDE-EPIC038"` (lines 2981–2984) and the CLI conformance captures as `cli.*` without release fields (3333–3342); PR06b carried this as O-P06b-17, "a per-regeneration provenance model is an evidence-model change for its owners" (S12).
- CLI conformance family: `tools/cli/generate_cli_conformance_artifacts.py` pins `FROZEN_SHA256` for `artifacts/cli/help/hdctl_help.txt`, `showcompat_help.txt`, `reject_nonjson.txt`, `ab.json`, `ba.json`, `summary.json` and the install captures (lines 46–57); `--check` validates bytes on disk by digest only (line 70) and never compares them with live `--help` output; generation requires an admitted release. PR06b plan §6.4 kept this family frozen with nonclaims at the `1.3.0` re-cut; AGENTS.md "Release identity" says EPIC022 release evidence stays frozen and is never refreshed. `artifacts/cli/help/hdctl_help.txt` line 8 carries the stale showcompat summary (S07).
- Close-pack writer `tools/qa/generate_epic_close_pack.py` with `schemas/epic_close_candidate_source.v1.json`: `epic_id` pattern `^HDE-EPIC[0-9]{3}$` (CD-1); four fixed `REPORT_SECTION_HEADINGS` (line 60) and ten fixed `REPORT_BODY_LINES` (66); five mandatory `nonclaims` (schema `minItems` 5), one of which renders "No QA PASS, acceptance, or token satisfaction is claimed."; the manifest carries `candidate_posture: candidate_only` and an `outputs` map, not `key_outputs`; feedback-dependency patterns refuse run/receipt/attestation/commit vocabulary in every causal field. Tests `tests/qa/test_generate_epic_close_pack.py` pin the closed sets (CLOSE01 result §1.1, B-1). The writer and schema are the HDE-EPIC039 generic closeout-candidate capability (AGENTS.md "HDE-EPIC039 current workflow posture"), designed to be feedback-free and neutral.

### 5.7 Sweep of the 130 uncovered test files (Observed; one run)

Run as §3(c) describes, at `982071b` with Python 3.12.3 and CI's install: **79 failed, 523 passed, 14 errors in 160 s**; exit 1. The run rewrote **27 tracked files** and created `tmp/` in the throwaway clone (`artifacts/epic020/bundles/*` (16 files), `artifacts/evidence_index.jsonl` and its `.sha256` and path proofs, `docs/evidence/INDEX.json`, `INDEX.sha256` and their path proofs, `artifacts/goldens/public_success.json` and `.sha256`, `artifacts/logs/loader_call.jsonl`, `artifacts/release_id.txt`), which confirms O-11: these files cannot be run in the repository tree. PR05 measured 57 failed / 546 passed / 13 errors over 129 files at `25b2c87b` and `96b54dd8` with Python 3.11.15; the main difference is 21 failures in `tests/evidence/test_hdapi_v2_contract_inventory.py` and one in `tests/evidence/test_hde_epic037_pr05_parent_binding.py`, which were not diagnosed here (environment or drift; the S03 unit triages them on the CI interpreter).

| Class | Files | Evidence |
| :---- | ----: | :---- |
| Collection errors: imports of removed legacy trees (`core.canon`, `core.pipeline`, `core.config`, `core.stable`, `core.catalog`, `adapters.hdapi`, `adapters._net`) | 14 | `tests/adapters/test_safe_mode.py`; `tests/canon/{test_center_order_and_counts,test_checksums,test_loader_integrity,test_overrides_prod,test_report_determinism}.py`; `tests/em/test_em_defaults_and_ladder.py`; `tests/test_catalog_canon.py`; `tests/test_pipeline_properties.py`; `tests/test_pipeline_public.py`; `tests/test_resolver_prod_rules.py`; `tests/test_sercanon.py`; `tests/unit/test_channel_derivation.py`; `tests/unit/test_enum_closure.py`. ARCHITECTURE.md "Deprecated/archived trees": `core/`, `server/`, `adapters/` removed; active code must not import them. |
| Files with at least one failure | 37 | 21 in `tests/evidence/test_hdapi_v2_contract_inventory.py`; 3 each in `tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py`, `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py`, `tests/compliance/test_cli_release_id_resolver_precedence.py`, `tests/arch/test_arch_guards.py`, `tests/adapter/test_readyz.py`, `tests/adapter/test_reader_parity.py`; 2 each in seven `tests/provider/*`, `tests/hdctl/test_cli_read_singlebg.py`, `tests/em/test_em_throat_and_adjacency.py`, `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py`, `tests/adapter/test_headers_and_determinism.py`; 1 each in sixteen further files including `tests/reader_v1/test_cli_proof.py` (the O-P06a-03 baseline failure) and `tests/compat/test_cli_public_bytes_identity.py`. |
| Files that passed completely | 79 | the remainder of the 130 |

### 5.8 PF23 anchors (historical context only; not deliverables)

Components and loci named by the HDE-EPIC040 QA-10 records consulted (`docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md` RA-08, RA-09, RA-12, RA-14; `docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md` RA-09): the CI lane classifier and workflow, the test inventory, the endpoint catalog and the adapter routes, the four HDE-EPIC040 PR deliveries. Each was re-inspected at `982071b` (§5.2, §5.3, §5.5, §6 S19). No PF23 update is assigned or scheduled (Change Process Guide, Reality Audits updates are PO-only).

## 6. Requirement-by-requirement audit

Each entry records: the Specification clause; current behavior (`Observed` at `982071b` unless labelled otherwise); required behavior (the acceptance intent, verbatim from the Specification where quoted); affected components and interfaces; dependencies; feasibility; risks; tests and evidence needs; canon and documentation effects; gaps; and the planning disposition with the phase block the Specification assigns.

### S01 — Package every release member with the distribution (Coagulation)

- **Source clause.** S01 (5(a), O-12): "A regular wheel install admits the complete release outside a source checkout." Constraint "Release members"; Live QA class 2 row for S01.
- **Current behavior.** §5.4: the wheel omits 16 of 45 members, so a non-editable install cannot admit (`MISSING_FILE`, PR06 CR-01). Every current consumer avoids the gap: CI installs `-e .`; the Procfile runs the factory from the checkout; the attestation builder installs its wheel only to exercise the `hdctl` console entrypoint. Admission resolves the root from the installed location of the covered modules (`engine/config/registry_loader.py` lines 1325–1341), so an installed wheel is admitted only if every roster path exists relative to the directory that contains `engine/`.
- **Required behavior.** The wheel carries all 45 roster paths at their roster-relative locations, and `load_active_mechanics_bundle()` admits from a non-editable installation in a fresh environment with no source checkout on `sys.path`.
- **Affected components.** `pyproject.toml` (package discovery for `catalog.narratives`, `adapter.schemas`, and the top-level data trees `schemas/`, `errors/token_map/`, `migrations/`, `tools/bodygraph/`; package-data per tree); a new packaging test; `tools/evidence/build_release_attestation.py` is the existing isolated-install consumer and must keep passing. `pyproject.toml` is a classifier full-validation path (classifier lines 32–39), so the PR runs every lane.
- **Dependencies.** Converges with the re-cut (§7.3): S01 must not change `engine/config/registry_loader.py` (a member), and the Audit found no reason to; the data trees are shipped at the locations the loader already expects.
- **Feasibility.** Yes. Setuptools can ship the data trees (namespace-style discovery plus package-data, or an equivalent the per-PR plan selects); the wheel already ships the top-level `math/` data directory, which proves the layout installs. `math` is a CPython built-in module, so the data directory does not shadow it.
- **Risks.** A wheel that installs top-level `schemas/`, `errors/`, `migrations/`, `tools/` and `catalog/` directories can collide with unrelated distributions in a shared site-packages; the repository's own consumers install into dedicated environments (CI, the attestation venv). Recorded as a documentation obligation (README install note), not a blocker. `hdctl --version` reads the distribution version `0.0.0` (`engine/cli/main.py` lines 58–62); S01 does not change it.
- **Tests and evidence.** A test that builds the wheel into `tmp_path`, installs it `--no-index --no-deps` into a venv there, and asserts admission (`release_id` equal to the manifest hash) and `hdctl --version` from that venv; the attestation rehearsal (`build_release_attestation.py --output <external> --require-clean`) in the release lane.
- **Canon and documentation effects.** None to canon. README install guidance (final documentation unit). Live QA: the checked-in deployment declarations install only `requirements.txt` and run the app from the checkout (§5.4), and Glow Infrastructure §10 does not verify the live Railway setting; the QA Plan may record the S01 exemption basis once the Ops placement task (Plan OPS-01) confirms the deployed build shape (`discoverable by OPS`).
- **Gaps.** None open.
- **Disposition.** `PLAN_READY`.

### S02 — Governed not-found envelope on the production app (Conjunction)

- **Source clause.** S02 (5(b), O-P06a-22): "Every 404 from the production app is the governed `ERR_NOT_FOUND` envelope with `no-store`, never Flask HTML."
- **Current behavior.** §5.5: `adapter/factory.py` (the Procfile app) rewrites only compat-path HTML 404/405; any other unknown path returns Flask's HTML 404 without `no-store`. `adapter/wsgi.py` lines 53–66 already register app-level 404 and 405 handlers that emit `error_envelope("ERR_NOT_FOUND")` through `emit_public` with `no-store` and no ETag. `docs/server/reader_v1.md` line 20 documents the limitation.
- **Required behavior.** App-level 404 (and the matching 405 on unknown paths) handlers on the production factory emitting the same governed envelope and headers as `adapter/wsgi.py`, with the existing compat shaping and the production Reader's governed 405 (`api_bp`) unchanged.
- **Affected components.** `adapter/factory.py` (non-member); `adapter/http_reader.py::create_app` line 1163 (the third factory, a member) is fixed in the same unit only because S10 changes that file anyway, so no extra re-cut is forced; tests under `tests/http/` (the per-factory method matrix in `tests/http/test_reader_post_v2.py` is the pattern) and `tests/adapter/`.
- **Dependencies.** None. Live QA class 1 (production app).
- **Feasibility.** Yes; the pattern exists in the repository.
- **Risks.** HEAD and OPTIONS on unknown paths; `/internal/` ETag stripping must keep working; the classifier's owner registration for `adapter/factory.py` is `Unknown pending discovery` (the PR verifies `_PRODUCT_TEST_OWNER_PATHS`).
- **Tests and evidence.** Per-factory tests for unknown paths (GET, HEAD, POST, OPTIONS): status 404, body is the canonical envelope, `Cache-Control: no-store`, no ETag, `Content-Type: application/json; charset=utf-8`.
- **Canon and documentation effects.** None to canon; `docs/server/reader_v1.md` line 20 becomes stale (final documentation unit).
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S03 — Bring every test file into a CI lane or retire it (Distillation)

- **Source clause.** S03 (5(c-1), O-11, RA-08, O-P06a-03): "No test file runs in no CI lane; each retirement has a recorded reason; recorded failures and collection errors are fixed or retired with their files." Constraint "Uncovered tests"; U-1.
- **Current behavior.** §5.3 and §5.7: 130 files (135 under the strict definition) are outside every lane and target; 14 cannot be collected; 37 files hold 79 failures; 27 tracked files are rewritten by the sweep. The five deliberately inactive files are fail-closed by the classifier and reachable by no lane.
- **Required behavior.** Each of the 135 files is either (a) registered to a fixed lane list in `ci.yml` and the classifier, or to a registered owner so that it is a changed-test target, or (b) retired (deleted) with a recorded reason; every retained file passes under closed rails in the lane's execution shape; retained files that write tracked artifacts are fixed to write under `tmp_path` or run only in the detached-worktree step with the clean-tree assertion.
- **Affected components.** `tests/**` (the 135 files, Appendix A); `ci/checks/classify_ci_changes.py` (owner registrations, `_FULL_VALIDATION_INACTIVE_TESTS`); `.github/workflows/ci.yml` lane lists; `pytest.ini`; the classifier's pinned expectations in `tests/evidence/test_rails_ci_workflow_integration.py`; a tracked retirement ledger (proposed `tests/retired_tests.md`, §7.1 EC-3) so that reasons are recorded in the repository and not only in PR records.
- **Dependencies.** S04 and S05 travel with S03 (Specification phase table); S20 follows S03–S05. Interplay: `tests/bodygraph/test_resolver_vendor.py` and `tests/adapter/test_gate_auth.py` are in the uncovered set and test surfaces S14 and S10 change, so S03's lane registration for them lands before, or together with, those units, or their retirement is recorded first.
- **Feasibility.** Yes, with the largest effort of the change. The 14 legacy-import files and the tests of removed behaviors (for example `tests/adapter/test_readyz.py`, which asserts the readiness rules S17 removes from the documentation) are retirement candidates with reasons; passing files need registration only; failing files need triage one by one.
- **Risks.** Real defects behind some failures may enlarge the work (Specification constraint); the per-PR plan may propose a bounded rescope if so. Lane runtime grows (CI budget: PF27 "CI lane classification and automated budget-control discipline" asks for the smallest correct lane, not a new required suite for administrative tests).
- **Tests and evidence.** The lanes themselves; the classifier tests; a `--check`-style assertion that no `tests/**/test_*.py` is outside lane-or-target coverage (the S20 tool's sweep component can share it).
- **Canon and documentation effects.** None to canon. AGENTS.md "Pytest readiness rule" unchanged; README test instructions (final documentation unit).
- **Gaps.** The 22 failures not explained by PR05's baseline (§5.7) are undiagnosed; the unit diagnoses them on the CI interpreter.
- **Disposition.** `PLAN_READY`, with the size risk recorded.

### S04 — Fail-closed treatment for unregistered `tools/qa/` sources (Distillation)

- **Source clause.** S04 (5(c-2), O-22): "An unregistered `tools/qa/` source, `.sh` and `.sql` included, cannot pass classification without an owner test."
- **Current behavior.** §5.2: `tools/qa/` paths get `{"evidence","qa"}` unconditionally (classifier line 1657); `_qa_tool_owner_targets` fails closed only for `.py` (lines 1174–1199); the unknown-source refusal is skipped because lanes are returned (lines 1578–1582); `tools/bodygraph/` already fails closed for `.py`, `.sh` and `.sql` (lines 1209–1229). No `.sh` or `.sql` file exists under `tools/qa/` today (O-22; `ls` finds none).
- **Required behavior.** `_qa_tool_owner_targets` (or the prefix rule) treats every `_UNKNOWN_SOURCE_SUFFIXES` file under `tools/qa/` as the bodygraph rule does: registered owner or `CI_QA_OWNER_TEST_MISSING`.
- **Affected components.** `ci/checks/classify_ci_changes.py`; `tests/evidence/test_rails_ci_workflow_integration.py` (rails lane) for the new refusal cases.
- **Dependencies.** Travels with S03.
- **Feasibility.** Yes (a few lines).
- **Risks.** None material; existing `tools/qa/*.py` registrations are unchanged.
- **Tests and evidence.** Classifier unit tests for an unregistered `.sh` and `.sql` under `tools/qa/`.
- **Canon and documentation effects.** None.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S05 — Align the CI workflow's documentation skip list with the classifier (Distillation)

- **Source clause.** S05 (5(c-3), RA-12): "A PR touching only classifier documentation prefixes starts no CI run."
- **Current behavior.** §5.2: `ci.yml` `paths-ignore` lists four prefixes; the classifier exempts eight; a PR touching only `docs/crd/`, `docs/plans/`, `docs/qa/` or `docs/run/` starts a run that selects no lanes. Two governed primaries live under a classifier-exempt prefix: `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json` are in `docs/evidence/INDEX.json`, and the classifier gives such paths the evidence lane through the Human Index (lines 895–925).
- **Required behavior.** The workflow's skip list equals the classifier's documentation prefixes **except** that a change to a governed primary under one of them still starts a run (otherwise aligning the lists would remove the evidence-lane protection the classifier gives those two files). GitHub path filters support negation, so the list can carry the eight prefixes with explicit exceptions for governed primaries, kept in step by a test that reads `docs/evidence/INDEX.json` (§7.1 EC-1). The Audit reads the acceptance intent's "classifier documentation prefixes" as paths the classifier returns no lanes for; a governed primary is not one.
- **Affected components.** `.github/workflows/ci.yml` (a full-validation path, classifier line 29–30); `tests/evidence/test_rails_ci_workflow_integration.py` (which pins the workflow text; the rails lane). The exact YAML arrangement is the PR's choice (Plan Templates, "CI lane classification and automated budget-control discipline": a plan must not invent the YAML).
- **Dependencies.** Travels with S03.
- **Feasibility.** Yes.
- **Risks.** A future governed primary under a doc prefix without a negation would silently lose CI: the pinning test prevents it. AGENTS.md "Code review scope — CI-exempt paths" describes the eight prefixes as the classifier's list; it stays accurate.
- **Tests and evidence.** The workflow-integration test cases; a dry run of the classifier on a docs-only path set.
- **Canon and documentation effects.** None to canon; AGENTS.md passage stays true (operative documentation, verify at the final documentation unit).
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S06 — Attestation builder's wheel stage under Debian-patched setuptools (Distillation)

- **Source clause.** S06 (5(d), O-10): "The release attestation builds under Debian-patched setuptools."
- **Current behavior.** §5.6: the wheel stage runs `sys.executable -m pip wheel --no-index --no-deps --no-build-isolation`, so it uses whatever setuptools the invoking interpreter has; Debian's patched setuptools 68.1.2 fails with `AttributeError: install_layout` (O-10, PR05 result). Not reproduced in this container (no Debian-patched setuptools present; both scratch environments carry upstream setuptools); hosted CI passes (stock setuptools).
- **Required behavior.** The isolated build no longer depends on the invoking interpreter's distribution-patched setuptools, or tolerates it, so that `build_release_attestation.py --output <external> --require-clean` completes its wheel stage on a Debian interpreter; the exact-source guarantees (`_require_exact_source_copy`, clean child environment, `--no-index`) stay.
- **Affected components.** `tools/evidence/build_release_attestation.py::_install_packaged_console_entrypoint` (lines 341–452) and `_clean_child_env` (328–340); `tests/evidence/test_release_attestation.py` (release lane); `docs/adr/hde/release_attestation_scaling_adr.md` is the design record (read; no decision in it is changed).
- **Dependencies.** Same tool as S13; same unit.
- **Feasibility.** Yes; the per-PR plan reproduces O-10 on a Debian interpreter first and then selects among: building inside the fresh venv after seeding it with upstream `setuptools`/`wheel` from a build-time wheelhouse the builder captures from the invoking environment (keeps `--no-index`); or assembling the pure-Python wheel without invoking the Debian `install` command path. The choice is engineering; the acceptance is the Debian build.
- **Risks.** The attestation's exact-source and fixed-point proofs must remain byte-identical to CI's; any change to the wheel stage is exercised by the release lane on every PR.
- **Tests and evidence.** `tests/evidence/test_release_attestation.py` additions for the stage; a recorded Debian reproduction before and after in the PR result.
- **Canon and documentation effects.** None.
- **Gaps.** Reproduction environment: `discoverable by PR` (a Debian interpreter with `python3-setuptools`); not a blocker.
- **Disposition.** `PLAN_READY`.

### S07 — Correct the showcompat help summary (Conjunction)

- **Source clause.** S07 (5(e), O-P07-01): "`hdctl --help` describes showcompat's actual `magic10_compat_result.v1` output."
- **Current behavior.** `engine/cli/main.py` line 79: `help="Emit canonical Reader v1 bytes from vendor JSON (stdin or files)"`; `docs/CLI_commands.md` line 25 records this as a known gap and states the current contract; `artifacts/cli/help/hdctl_help.txt` line 8 is a frozen capture of the stale text with a pinned digest (§5.6); the identity closure regenerates that family only when its `--check` drifts (`regenerate_identity_closure.py::_ensure_step`, lines 357–361), and the on-disk bytes stay unchanged, so the closure keeps skipping the write.
- **Required behavior.** The subparser help names the actual stdout contract (the canonical `magic10_compat_result.v1` document; Reader v1 bytes only through `--dump-reader`), consistent with `docs/CLI_commands.md`.
- **Affected components.** `engine/cli/main.py` (member, re-cut); `docs/CLI_commands.md` line 25 (remove the known-gap sentence); a test asserting the summary text (`tests/cli/test_cli_install_help.py` or `tests/cli/test_cli_usage_and_errors.py`, compat lane / supplemental targets). The frozen capture family stays frozen with a nonclaim (§7.1 EC-6): AGENTS.md "Release identity" forbids refreshing the EPIC022 capture-time records and PR06b §6.4 kept them frozen at the last re-cut; `--check` compares bytes to digests, not to live output, so it keeps passing.
- **Dependencies.** Re-cut (§7.3).
- **Feasibility.** Yes (one string).
- **Risks.** None material. `ci/checks/check_cli_help.sh` checks only exit status, empty stderr and the final LF.
- **Tests and evidence.** The help-text assertion; `hdctl --help` captured in the PR result.
- **Canon and documentation effects.** None to canon; `docs/CLI_commands.md` (in the unit).
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S08 — Apply `aux-preview --band` for pair-file input (Fermentation)

- **Source clause.** S08 (5(e), O-P07-02): "The band flag takes effect for pair-file input."
- **Current behavior.** `engine/cli/main.py` lines 538–567: with `--pair-file`, `_resolve_from_pair_file` takes the band from the pair file's category row and never reads `args.band`; `--category` and `--perspective` are honored. Without a pair file, `--band` is required.
- **Required behavior.** With `--pair-file`, an explicit `--band` (one of `AUX_BANDS`) overrides the band read from the file; absent the flag, the file's band is used as today.
- **Affected components.** `engine/cli/main.py` (member, re-cut); `tests/cli/test_aux_preview.py` (supplemental target; compat lane through `tests/cli` owners); `docs/CLI_commands.md` aux-preview wording (final documentation unit).
- **Dependencies.** Re-cut.
- **Feasibility.** Yes.
- **Risks.** None material (the Aux preview is an admin, ids-only or narrative preview surface; no public payload changes).
- **Tests and evidence.** A pair-file case with and without `--band`.
- **Canon and documentation effects.** None to canon.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S09 — Repair or retire the dev Reader harness and the references to it (Conjunction)

- **Source clause.** S09 (5(e), O-P07-03): "The harness imports and runs, or it is retired and `VERIFY.sh` and `docs/acceptance/reader_a7_crib.md` no longer reference it."
- **Current behavior.** `dev/reader_harness/app.py` line 12 `app.getattr(app,"register_"+"blueprint")(bp, url_prefix="/api")` raises `AttributeError` at import (`create_app()` runs at module import, line 17); its gate is the same `APP_ENV` default-`dev` pattern S10 removes. References: `VERIFY.sh` lines 42–44 (starts it on port 5000); `docs/acceptance/reader_a7_crib.md` line 4; `docs/server/reader_v1.md` lines 19 and 24 (legacy notice already stating it raises); `engine/emit_public.py` lines 20–22 and `tests/runtime/test_emit_public_legacy_helper.py` lines 4–6 (docstrings); `CHANGELOG.md` line 333 (history); `notes/dev-sampler/dev_sampler_http_discovery.md` line 13. Historical prefixes (`.audit_src/`, `_arch/`, `.backup_epic004/`, `handoff/`, `audit/docs_snapshot_r7/`) also name it and stay untouched.
- **Required behavior.** Retire (§7.1 EC-2): delete the harness; repoint `VERIFY.sh` to the canonical dev runner (`python -m adapter.http_reader`, `PORT` default 8000, `scripts/dev_start_reader.sh`), keeping its checks runnable; rewrite the crib's start line; correct the two docstrings and the legacy notice in `docs/server/reader_v1.md`.
- **Affected components.** `dev/reader_harness/app.py`; `VERIFY.sh`; `docs/acceptance/reader_a7_crib.md`; `docs/server/reader_v1.md`; `engine/emit_public.py` (docstring only; the legacy five-positional helper stays because `VERIFY.sh` calls it); `tests/runtime/test_emit_public_legacy_helper.py` (docstring). Classifier treatment of `dev/` and `VERIFY.sh` deletions or edits: `Unknown pending discovery` (the PR checks `_lanes_for_path`).
- **Dependencies.** Coordinates with S10 (same file family, same block).
- **Feasibility.** Yes.
- **Risks.** `VERIFY.sh` binds port 5000 and uses `emit_public_envelope`; repointing it must keep its predicates meaningful or the unit records which checks it no longer performs.
- **Tests and evidence.** `VERIFY.sh` executed once in the PR result; the docstring test unchanged in behavior.
- **Canon and documentation effects.** None to canon; README/CHANGELOG (final documentation unit).
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S10 — Gate dev `GET /reader` on an explicit environment (Conjunction)

- **Source clause.** S10 (5(e), O-P07-04): "The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses." Constraint "Dev route"; Exclusions bullet 5 (production `APP_ENV` is already `prod`).
- **Current behavior.** §5.5: `adapter/http_reader.py` line 603 serves when unset or exactly `dev`, refuses `test` and `local`; `_dev_admin_gate` (lines 817–823) already implements the required semantics for the sampler and conjunction routes; the catalog rows for `GET`/`HEAD /reader` say `env_gate: APP_ENV=dev` (`generate_a7_transport_proofs.py` lines 46–47); `scripts/dev_start_reader.sh` lines 13–18 exports `APP_ENV` only when it is already set, so an operator who starts the runner without it would, after S10, get a refusing `/reader`; `tests/http/test_reader_a7_transport.py` line 79 sets `APP_ENV=dev`; `tests/adapter/test_gate_auth.py` (uncovered set) deletes `APP_ENV` at lines 27 and 54 and would see the behavior change; production is `APP_ENV=prod` (Glow Infrastructure §2.4), so the route refuses there today with 403.
- **Required behavior.** The route uses the `_dev_admin_gate` semantics (normalize; served only for `dev`, `test`, `local`; otherwise `ERR_READER_FORBIDDEN` 403, the token `tests/reader_v1/test_schema.py` line 18 already pins); dev, test and local use keeps working: `scripts/dev_start_reader.sh` defaults `APP_ENV=dev` when unset (as `VERIFY.sh` line 4 already does) and `docs/server/reader_v1.md` says so (§7.1 EC-4).
- **Affected components.** `adapter/http_reader.py` (member, re-cut); `tools/evidence/generate_a7_transport_proofs.py` catalog rows (`env_gate` text for the two `/reader` rows) and therefore `docs/ENDPOINTS_CATALOG.json`, its mirror, sidecars and proofs, regenerated by that owner then the updater (same unit as S15); `scripts/dev_start_reader.sh`; `docs/server/reader_v1.md`; tests in `tests/http/` and the uncovered `tests/adapter/test_gate_auth.py` (S03 interplay).
- **Dependencies.** Re-cut; S15 (catalog regeneration in one owner run).
- **Feasibility.** Yes.
- **Risks.** None material beyond the dev-runner default; Live QA class 1 (production app: prove the refusal in the deployed target, headers-only, as the A7 env-gate proof already does for `APP_ENV=prod`).
- **Tests and evidence.** Parametrized tests for unset, `dev`, `test`, `local`, `prod`, `production`, `live`, arbitrary; the A7 env-gate proof regenerated.
- **Canon and documentation effects.** None to canon; the catalog is regenerated by its owner.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S11 — Engine-core evidence currency test checks release identity (Distillation)

- **Source clause.** S11 (5(e), O-P06a-23): "The test fails when `release_id` drifts."
- **Current behavior.** §5.6: `tests/evidence/test_engine_core_evidence.py::test_current_proofs_bind_actual_sources_and_behavior` (lines 78–97) checks fixture kind, source digests, run equality, vectors and JSON-compare digests; it never compares the payloads' `release_id` with the admitted identity. The writer records `release_id` in all four `artifacts/core/*` payloads.
- **Required behavior.** The test asserts each payload's `release_id` equals the admitted release identity (`identity_meta()["release_id"]` / the manifest's canonical hash) so a re-cut that skips the engine-core owner fails the evidence lane.
- **Affected components.** `tests/evidence/test_engine_core_evidence.py` (evidence lane); no writer change expected.
- **Dependencies.** None; the re-cut unit must run the engine-core owner (already in the convergence order).
- **Feasibility.** Yes.
- **Risks.** None.
- **Tests and evidence.** The assertion itself; a negative case by monkeypatching the admitted identity.
- **Canon and documentation effects.** None.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S12 — Provenance labels on current-release captures in the Machine Mirror (Distillation)

- **Source clause.** S12 (5(e), O-P06b-17): "Current-release captures carry current-release labels."
- **Current behavior.** §5.6: the sole updater registers the captures a re-cut regenerates under their origin families with origin labels (for example `epic038.pr02.endpoint_catalog*` with `"epic_id": "HDE-EPIC038"`, lines 2981–2984; `cli.*` rows without any release field, lines 3333–3342). PR06b's lineage review carried this as O-P06b-17 for the evidence/updater owner: "a per-regeneration provenance model is an evidence-model change for its owners". The families a re-cut regenerates are listed in `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §6.3; the frozen families in §6.4 keep capture-time identity by design.
- **Required behavior.** Reading adopted (§7.1 EC-5): every Index/Mirror row for a capture that the current release regenerates carries fields that identify the admitted release that produced it (release version and `release_id`, or an equivalent `release_binding` field the owner defines), while its origin artifact key stays stable for index continuity; frozen capture-time families keep their capture-time labels and are not relabelled. The exact field set is the updater owner's engineering choice; the invariant is that a reader of the Mirror can tell a current-release capture from a frozen one without opening the file.
- **Affected components.** `tools/evidence/update_evidence_index.py` (family registrations and the row writer); the Mirror schema checked by `ci/checks/check_mirror_schema.sh` and `tests/evidence/test_machine_mirror_self_proof.py` / `test_evidence_skeleton.py` (`Unknown pending discovery`: whether added fields need a schema change); `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl` and companions, regenerated only by the updater.
- **Dependencies.** Shares the updater with S22; the re-cut unit regenerates the rows afterwards, so the label model must land before the re-cut (§7.3 order).
- **Feasibility.** Yes.
- **Risks.** Mirror consumers (`tools/evidence/orientation_demo.py`, `validate_evidence_paths.py`, the classifier's Human Index reader) must accept the added fields; the PR runs every read-only validator.
- **Tests and evidence.** Updater unit tests for the label fields; `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`.
- **Canon and documentation effects.** None to canon (HDE Schemas & Artifacts owns the Mirror schema; if a schema field is added, that is a doc-delta candidate for its owner, not a plan-mandated canon edit); `docs/EVIDENCE_INDEX.md` (final documentation unit).
- **Gaps.** None blocking; the field set is decided in the unit.
- **Disposition.** `PLAN_READY`.

### S13 — Closure admission probe independent of the ambient installed package (Distillation)

- **Source clause.** S13 (5(e), O-OPS01-01): "The probe's result depends only on the isolated closure's own sources."
- **Current behavior.** §5.6: `release_not_admitted_observed()` imports `engine.config.registry_loader` in-process, so inside the attestation's isolated copy it resolves `engine` from the ambient installation (the editable source clone), and fails with an unrecorded traceback when no package is installed (OPS01 receipt v1.2 row O-OPS01-01). The `ci.yml` release lane's inline probe (lines 285–296) runs in the checkout and is correct there.
- **Required behavior.** The closure's probe evaluates admission against the isolated copy only (for example a child `sys.executable -I` with the copy as `cwd` and `PYTHONPATH`, or an explicit root-bound import), and an absent ambient package is not a failure.
- **Affected components.** `tools/evidence/regenerate_identity_closure.py` (lines 384–393 and the `_run`/`_is_current` helpers, 330–350); `tools/evidence/build_release_attestation.py` where it invokes the closure in the copy; `tests/evidence/test_release_attestation.py` (release lane).
- **Dependencies.** Same unit as S06.
- **Feasibility.** Yes.
- **Risks.** The probe must keep refusing truthfully (`INCOMPLETE_RELEASE_ROSTER` only) without widening acceptance (PF10's former §2.15 posture is retired from the current PF10; the `ci.yml` comment still cites it as history).
- **Tests and evidence.** A test that runs the closure probe from a copy with no ambient `engine` importable and from one with a deliberately different ambient package, proving the result follows the copy.
- **Canon and documentation effects.** None.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S14 — Implement the production vendor override as CLI/API/Vendor Ref §7.1.11a to §7.1.11f state it (Fermentation)

- **Source clause.** S14 (5(f), DD-04, QA50-B01): "`--allow-prod-vendor` behaves as §7.1.11 specifies, including environment classification, rails, evaluation order, error carrier, authorized initiator and audit; closed rails still refuse first, and public Reader or Aux traffic never reaches the vendor." Constraints "Vendor override", "Override initiator", "Live QA".
- **Current behavior.** No implementation: the only occurrences of `--allow-prod-vendor` outside `docs/pfcanon/` are the HDE-EPIC040 doc-delta rows (`audit/docdeltas/hde-epic040_doc_deltas.md` DD-04). `bg:resolve` parser (`engine/cli/main.py` lines 138–160): `--user`, `--source {auto,db,vendor}`, `--upsert`, `--dry-run`, `--birthdate/--birthtime/--location`; handler (lines 210–230) passes `_resolver_env()` = `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `HD_API_BASE_URL`, `HDAPI_BASE_URL` (lines 186–187) and raises `MISSING_VENDOR_INPUT` (exit 64) for a missing birth tuple. Resolver `_resolve_vendor` (`engine/bodygraph/resolver.py` lines 112–145) refuses `SAFE_MODE` first (`PROVIDER_REFUSED`), then network (`PROVIDER_NETWORK_BLOCKED`), before any client construction; environment classification exists only inside `_resolve_vendor_v2_chart` (lines 246–253: lowercased `APP_ENV`/`ENGINE_ENV`, production aliases checked only for the non-dry-run write path); `PROVIDER_CONFIG_INVALID` already exists as a `VendorError` code (`engine/bodygraph/vendor_client.py` lines 115–172). A vendor `--dry-run` reaches `_resolve_vendor_v2_chart` and may contact the vendor (lines 236–253 gate only the write path), which §7.1.11d addresses ("A production dry run that contacts the vendor still requires the flag").
- **Required behavior.** PF05 §7.1.11a–f in full (read): the single value-bearing flag with its regex and duplicate/empty refusal; `APP_ENV` canonical with `ENGINE_ENV` alias, normalization, the two allow-lists, conflict and unknown values → `PROVIDER_CONFIG_INVALID` before I/O; the eight-row rail/flag matrix (`PROVIDER_PROD_OVERRIDE_REQUIRED`, CLI usage error, `PROVIDER_AUDIT_UNAVAILABLE`, allowed, `PROVIDER_PROD_OVERRIDE_INVALID` in non-production); the seven-step evaluation order with the pre-I/O durable audit event at step 6; usage errors through the canonical CLI usage carrier exit 64 and policy refusals through the `status="error"` resolver envelope exit 1 with outbound-attempt count 0; the authorized initiator rule (authenticated human principal from the execution environment; refuse when unavailable; the reference is not authentication); the 15-field append-only keys-only audit record (`event: vendor_prod_override`, sanitized, no subject data), plus the optional post-I/O completion event.
- **Affected components.** `engine/cli/main.py` (member: parser, pre-parse duplicate detection, usage carrier); `engine/bodygraph/resolver.py` (member: classification, matrix, order, envelope codes); a new audit module (proposed `engine/bodygraph/vendor_audit.py`, non-member, imported by the resolver like `vendor_client.py`); actor-identity resolution from the OS principal; the audit sink (§7.1 EC-7: a local append-only JSONL file whose path comes from one new operator environment key with a default under the operator's state directory; PF05 names no location, so this is engineering, and the key is a PF07 doc-delta candidate); tests `tests/cli/test_bg_resolve.py` (supplemental target), `tests/bodygraph/test_resolver_vendor.py` (currently uncovered, Appendix A; S03 registers it), new matrix/audit tests; `docs/CLI_commands.md` and `README.md` (final documentation unit); `docs/ENDPOINTS_CATALOG.json` unaffected (CLI only).
- **Dependencies.** Re-cut (two members change); S03 for the vendor resolver test file; Live QA class 1 with the mandatory live vendor call (the QA Plan designs it; initiator per §7.1.11e; production shell facts are PF07-derived: `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, key presence for `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, Glow Infrastructure §2.4 and §2.6).
- **Feasibility.** Yes; the resolver already evaluates rails before I/O and has typed envelopes; the contract is fully specified. The audit sink's durability on a read-only filesystem yields `PROVIDER_AUDIT_UNAVAILABLE`, which is the specified behavior.
- **Risks.** Largest behavioral unit; argparse accepts repeated options silently, so duplicate detection needs an argv pre-scan; `ENGINE_ENV` is read elsewhere in the resolver with different leniency (lines 246–247) and must be unified for the vendor path without changing the v2 write guard's semantics; a vendor dry run must be classified as production vendor contact when it would contact the vendor.
- **Tests and evidence.** Table-driven tests over the eight matrix rows and the seven evaluation steps with a monkeypatched client proving zero outbound attempts on every refusal; audit record shape and sanitization; usage-carrier exit codes; `ENGINE_ENV` alias and conflict; dry-run classification. No live call in implementation (Exclusions bullet 5).
- **Canon and documentation effects.** Implements PF05 §7.1.11 unchanged. After landing, the "Required-Now implementation gap (DD-04; held)" paragraph in PF05 §7.1.11 and the `--allow-prod-vendor` bullet of HDE Users Guide §16 become stale: doc-delta candidates for their owners (non-mandatory, PO-owned). The new sink key is a Glow Infrastructure §8 config-key doc-delta candidate.
- **Gaps.** None blocking.
- **Disposition.** `PLAN_READY`.

### S15 — Reconcile the endpoint catalog with the routes the service registers (Conjunction)

- **Source clause.** S15 (5(g), RA-14): "Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner." Constraint "Governed artifacts".
- **Current behavior.** §5.5: eight registered route strings have no entry; the catalog object is hardcoded in `tools/evidence/generate_a7_transport_proofs.py::catalog_obj` with classification set `{'internal_admin','dev_harness','internal_identity','public_reader'}` (line 48) and validator rules including exactly one `public_reader` row and the sampler row's gate (lines 49–70); the generator writes `docs/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json` and both `.sha256` sidecars in one build (line 144); the updater re-validates the catalog (line 3447). HDE-CLI-API-Vendor-Ref §5.6 "Endpoint Catalog (JSON success)" owns the catalog's purpose and A7 proof-surface rules (internal-only, env-gated per entry), and Glow Infrastructure §4.1 lists `/aux/narrative` as an HD Engine external surface (names-only).
- **Required behavior.** Reading adopted (§7.1 EC-8): catalog, do not remove. Each of the eight routes gets a row with its real method set, blueprint module (`adapter.http_reader` for the six `bp` routes; `adapter.wsgi` for `/internal/healthz` and `/internal/readyz`), classification (existing classes or a new internal class the validator admits), observed env gate and rails profile; `success_endpoints` stays `GET /reader`; `a7_eligible` stays false for all new rows. Removal of a served route is a production-surface change no requirement asks for; if the S19 review recommends one, it is handled there with class-1 Live QA.
- **Affected components.** `tools/evidence/generate_a7_transport_proofs.py` (catalog rows, `CLASS` set, validator rules); regenerated `docs/ENDPOINTS_CATALOG.json`, mirror, sidecars and the proofs under `artifacts/proofs/` through the owner's write mode (`HDE_WRITE_A7_PROOFS=1`, PR06b §5.4 step 7), then the updater; `tests/http/test_endpoint_catalog.py`, `tests/transport/test_a7_transport_proofs.py`, `tests/evidence/test_rails_ci_workflow_integration.py` if it pins catalog shape (`Unknown pending discovery`); the updater's own catalog assertions (line 3447 onward).
- **Dependencies.** Same owner run as S10's `env_gate` text change (one regeneration); the re-cut regenerates the A7 family again afterwards (idempotent).
- **Feasibility.** Yes.
- **Risks.** The gating of the `/ops/*` routes and `/aux/narrative` must be read from the code before the rows are written (`Unknown pending discovery`: `/aux/narrative` currently answers `rails_closed` 503 unconditionally, lines 671–680; the ops probes carry their own guards). The canon catalog contract (HDE-CLI-API-Vendor-Ref §5.6) lists the required per-entry fields; the PR re-reads it before changing the validator.
- **Tests and evidence.** A test that enumerates every `url_map` rule of the three factories and asserts a catalog row exists for each `(method, path)`; the regenerated A7 family; updater `--check`.
- **Canon and documentation effects.** None to canon; AGENTS.md names the catalog as source of truth (unchanged).
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S16 — Add `GEO_API_KEY` to the environment template (Coagulation)

- **Source clause.** S16 (5(h)): "`.env.example` has a `GEO_API_KEY` entry."
- **Current behavior.** `.env.example` holds exactly `HD_API_BASE_URL`, `HD_API_KEY`, `HD_API_SECRET`; `GEO_API_KEY` is read by `engine/providers/vendor_http_hdapi.py` (lines 50–185) and named as an HD Engine boundary key in Glow Infrastructure §2.4 and §4.1.
- **Required behavior.** One `GEO_API_KEY=changeme` entry (placeholder value, no secret).
- **Affected components.** `.env.example` only (bounded by R3 to this one entry).
- **Dependencies.** None.
- **Feasibility.** Yes.
- **Risks.** None.
- **Tests and evidence.** The PR result shows the file; no test is proportionate.
- **Canon and documentation effects.** None.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S17 — Correct the readiness and port statements in `docs/ADAPTER_009.md` (Coagulation)

- **Source clause.** S17 (5(i), O-P07-05): "The readiness rules describe what `/internal/readyz` does, and the port statements are current."
- **Current behavior.** `docs/ADAPTER_009.md` lines 46–52 describe readiness as resolver, catalog/freeze and a `compute_pair` smoke with typed 503s; `adapter/wsgi.py` lines 47–51 return `{"ok": true, "schema": "v1"}` with 200 unconditionally, and the Procfile app (`adapter/factory.py`) registers no `/internal/readyz` at all; no `compute_pair` exists under `engine/` or `adapter/`. Port statements at lines 122 and 138 name `http://127.0.0.1:5000`, while the dev runner binds `0.0.0.0:$PORT` with default `8000` (`adapter/http_reader.py` line 1218; `scripts/dev_start_reader.sh`) and the Procfile binds `0.0.0.0:$PORT`. Line 55's `ENGINE_ENV=dev|staging|prod` is outside S17's bound and is noted as a doc-delta candidate only.
- **Required behavior.** The readiness section states what `/internal/readyz` does and on which app it exists; the port statements name the current bindings and defaults. The default documented dev access host stays `127.0.0.1` with the correct port (Change Process Guide, dev access address convention).
- **Affected components.** `docs/ADAPTER_009.md` (documentation; `.md` is a document suffix for the classifier, no lane).
- **Dependencies.** None; if S19 changes the readiness behavior, S17's text follows in the same unit or the final documentation unit.
- **Feasibility.** Yes.
- **Risks.** None.
- **Tests and evidence.** None proportionate; the PR result quotes the corrected lines.
- **Canon and documentation effects.** None to canon.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S18 — Correct `docs/ADAPTER_009.md`'s GET-with-body code and `ARCHITECTURE.md`'s stale statements (Conjunction)

- **Source clause.** S18 (5(i), DD-11, O-P07-06): "The documents say `invalid_json` for a compat GET with a body …, and state the current emitter return type and route mounts."
- **Current behavior.** `docs/ADAPTER_009.md` line 174 says a compat GET with a body yields `{"error":"body_not_allowed"}`; `engine/http/compat_handler.py` lines 124–125 emit `error_envelope("invalid_json")` (U-6 confirmed by the Lead Developer at `2aed56f1`; unchanged at `982071b`). `ARCHITECTURE.md` lines 9 and 24 state `emit_compact_json(payload) -> bytes`; `engine/presenter/emitter.py` line 23 declares `emit_compact_json(envelope, *, sort_keys=True) -> Tuple[bytes, Dict[str, Any]]` and names `emit_public_with_envelope` as the preferred entry; line 28 "Routing (dev only)" while `adapter/` carries the production mounts (`adapter/factory.py` per the Procfile; `api_bp` under `/api`).
- **Required behavior.** As the acceptance intent states.
- **Affected components.** `docs/ADAPTER_009.md`, `ARCHITECTURE.md` (documents).
- **Dependencies.** Lands with the Conjunction surfaces unit so the routing description matches S02's and S10's final shape.
- **Feasibility.** Yes.
- **Risks.** None.
- **Tests and evidence.** The PR result quotes the corrected statements; `tests/unit/test_check_agents_md_citations.py` is unaffected (AGENTS.md not touched here).
- **Canon and documentation effects.** None to canon.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S19 — One code security review of what #467, #492, #501 and #508 merged, read on `main` (Distillation)

- **Source clause.** S19 (6(b), RA-09): "The review is recorded; each confirmed finding is fixed within this CRD or routed to an owner with a reason." Constraint "Security review"; Live QA row "inherits the class of the surface its fix changes".
- **Current behavior.** No code security review of the merged implementation deltas exists (RA-09; PR bodies: #467 security review on the PR-open head only; #501 "A Codex security review of the implementation: none exists"; #508 security review on `402db72` only, not the corrective head). The four squash commits on `main` are `cd6f9e6` (#467, 2026-09-22), `4d7ab9d` (#492, 2026-09-25), `f7484d0` (#501, 2026-09-26) and `d79cfc1` (#508, 2026-09-26). Their union of non-document, non-test, non-evidence files that still exist on `main` is 48 paths (Appendix B). Since those merges only PR06b (`8999bd0`, #513) changed any of them (`engine/config/registry_loader.py`, `schemas/reader.v1.schema.json`, `scripts/make_reader_v1_goldens.py`, `tools/evidence/generate_open_rails_abba_proof.py`); the review reads current bytes.
- **Required behavior.** One recorded review of the 48 current files (plus the tests they rely on for proof), against a stated threat checklist (input bounds and body limits, path and file handling, environment gating and rails, secret and keys-only logging, error disclosure, injection into audit or log lines, concurrency and atomic publication for the evidence writers, dependency and subprocess use), with each finding classified confirmed / not confirmed and each confirmed finding either fixed in this CRD or routed with an owner and reason. The record is a change-process document under `docs/ephemeral/` (Change Process Guide: audits and reviews use exact repository paths there), proposed `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`.
- **Affected components.** The 48 files as review input; fixes only where confirmed; `tests/**` for regression proof of each fix.
- **Dependencies.** Ordered after the Conjunction surfaces unit so that fixes to `adapter/http_reader.py` or `engine/http/compat_handler.py` are judged against their final shape and, when they change a member, fall before the re-cut (§7.3). Fixes inherit the Live QA class of their surface.
- **Feasibility.** Yes; manual review with repository tooling only (no new scanner dependency; Exclusions bullet 6 forbids changing the review tooling, and adding a static analyzer is not needed to meet the acceptance intent).
- **Risks.** Findings may enlarge the work (Specification constraint); a finding on a member forces nothing new because the re-cut already follows.
- **Tests and evidence.** The review record; regression tests per fix.
- **Canon and documentation effects.** None to canon.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S20 — One read-only pre-push and pre-plan check with its own test (Distillation)

- **Source clause.** S20 (7): "One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository." Exclusions: no SessionStart hook. Constraint "Duplication".
- **Current behavior.** No such tool exists (`scripts/` and `tools/` listings; no `pre-push`/`prepush` reference). Every input it needs exists: `ci/checks/classify_ci_changes.py` (`classify_paths`; CLI `--base --head --event-name`), `ADMITTED_RELEASE_ROSTER`, the unique `docs/pfcanon/PF10-HDE-Build-Notes-v*.md`, the sweep method of §3 and §5.3, the `ci.yml` lane commands.
- **Required behavior.** One command (proposed `tools/ci/prepush_check.py`, §7.1 EC-9) with sub-reports: lanes and changed-test targets for given paths (delegating to the classifier, not re-implementing it); release membership of given paths; Build Notes path and SHA-256; the uncovered sweep (classifier-derived set) run in a throwaway export; a `ci.yml` replay in a throwaway worktree; every report read-only with respect to the repository (writes only under a temporary directory; asserts a clean tree before and after).
- **Affected components.** New `tools/ci/prepush_check.py` and `tests/tools/test_prepush_check.py`; `ci/checks/classify_ci_changes.py` registration (a `tools/ci/` path has no lane rule today, so an unregistered `.py` there fails classification: the unit registers lanes and the owner test); README/AGENTS usage note (final documentation unit).
- **Dependencies.** Follows S03–S05 (lane lists and the sweep definition must be final).
- **Feasibility.** Yes; duplication of CI logic is bounded by delegating to the classifier and by replaying `ci.yml` text rather than copying its commands (the unit decides the replay mechanism; a test pins that the replay covers every lane step name in `ci.yml`).
- **Risks.** Drift from `ci.yml` (the pinning test); runtime (minutes) acceptable for a pre-push tool.
- **Tests and evidence.** The owner test: read-only guarantee (tree unchanged), report shape, classifier delegation, Build Notes resolution uniqueness.
- **Canon and documentation effects.** None to canon.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

### S21 — Governed, feedback-free close-pack writer for Epic and CRD identities, and an admitted home for close-workflow run evidence (Distillation)

- **Source clause.** S21 (8, CC-1, CC-2): "The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has a home, inside an existing evidence family or in one S21's ADR admits, that does not reopen an approved QA manifest; the accompanying ADR is approved." CD-1 (resolved by S21); CD-2 / CR-3 (identity); constraints "Close-pack writer" and "Governed artifacts"; Exclusions bullets 3, 4 and 7.
- **Current behavior.** §5.6 and the CLOSE01 analysis (`docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` §1.1–1.2, B-1 and B-2): the generic writer's closed heading and sentence sets, mandatory nonclaims, Epic-only identity and `outputs` map cannot express the close report canon requires; and every admitted home for same-run close-workflow evidence is a check in the approved QA manifest. The canon requirements, read in full: Change Process Guide §3.5.2.1 (canonical filenames; exact-source acceptance section; verification statement; TI mapping; binary `SATISFIED` / `NOT SATISFIED`; follow-ups; superseded-artifact statement) and §3.5.1 "Feedback-free terminal lifecycle" (no source → CI → source back-edge); HDE Schemas & Artifacts §1.2 "Close-pack artifacts" and "Change-container compatibility" (CRD ID as the filename prefix; shipped deliverables; deferrals by ID; later-drain statements with the fixed vocabulary; `key_outputs` pointer; QA RCA embedded or referenced; supporting ledgers `audit/docdeltas/<change-id>_doc_deltas.md`, `_drain_targets.md`, `audit/qa/<change-id>/qa_step_logs_manifest.json`; no relocation of baseline artifacts); Glow QA Guide "Close report requirements" (verbatim heading `QA Rails — Open/Close (Final PR)`; "Acceptance and evidence pointers" list) and "Close-pack truthfulness and same-run execution" (same-run mechanical evidence under the QA root). The repository's ADR home is `docs/adr/hde/<name>_adr.md` (two precedents).
- **Required behavior.** (a) A new candidate-source schema version (proposed `schemas/close_candidate_source.v2.json`, the v1 file retained for history) that accepts `^HDE-(EPIC[0-9]{3}|CRD-[0-9]{4,})$`, maps the identity to the canonical filename prefix (`EPIC-NNN` / `CRD-NNNN`) and the lower-case directory form, carries the canon-required report content as structured source fields (acceptance criteria bound to tracked evidence paths and digests; deliverables; deferrals with drain targets; later-drain statements in the fixed vocabulary; the binary decision and its posture; follow-ups; the pointers list; the QA RCA reference or embedded summary) and validated free-text sections, while keeping the feedback-free invariant (no run IDs, receipts, attestations or commit identities in causal fields; candidate identity by tracked-path digest only). (b) The writer renders the heading `QA Rails — Open/Close (Final PR)` verbatim, the "Acceptance and evidence pointers" list and a manifest with a `key_outputs` map, and keeps check mode non-writing. (c) A home for close-workflow run evidence outside the approved QA manifest, inside an ADR-admitted family under the change's QA root (proposed `audit/qa/<change-id>/close/<check_id>/primary.log` with path proofs, published by the canonical updater as a post-verdict family), so that same-run mechanical evidence exists without adding a check to `qa_step_logs_manifest.json`. (d) The ADR (proposed `docs/adr/hde/close_pack_writer_adr.md`) records the decision, the affected canon (Change Process Guide §3.5.2, HDE Schemas & Artifacts §1.2, Glow QA Guide close-pack sections) and the drainage consequences; agents draft it, the Product Owner approves it (HDE Governance §9.7.3; Change Process Guide §1.0.5); S21's changed behavior is relied on only after approval.
- **Affected components.** `tools/qa/generate_epic_close_pack.py` (kept at its registered path; AGENTS.md and the classifier name it), the new schema, `tests/qa/test_generate_epic_close_pack.py`, `tools/evidence/update_evidence_index.py` (admission of the close-run family), `ci/checks/classify_ci_changes.py` registrations, `.github/workflows/epic-closeout-validation.yml` and `tools/evidence/run_sanity_pipeline.py` where they validate close packs (`Unknown pending discovery`: which release-sanity stage reads the candidate pair), the ADR, AGENTS.md and README passages (final documentation unit).
- **Dependencies.** The ADR approval (AQ-1) gates reliance, not implementation; S22 (updater) lands first so the close-run family and the CRD admission share one updater model; S21 completes before HDE-CRD-0002's ordinary Close Gate.
- **Feasibility.** Yes. The HDE-EPIC039 rationale (neutral, feedback-free) is weighed: the invariant worth keeping is the absence of a back-edge, which structured tracked-input fields preserve; the restriction worth lifting is the closed vocabulary, which made every canon-required element inexpressible (B-1).
- **Risks.** Canon drift between the three close-pack homes (the ADR names all three and the drain targets); over-wide free text (validated sections with required headings); the `QA Rails` heading's em dash versus the current heading regex (the v2 schema admits it explicitly).
- **Tests and evidence.** Writer tests for Epic and CRD identities, feedback-dependency refusal retained, required headings and pointers, manifest `key_outputs`, check-mode non-writing; updater tests for the close-run family; a dry run producing a CRD close pack for a synthetic candidate into `tmp_path`.
- **Canon and documentation effects.** ADR-covered canon change: Change Process Guide §3.5.2 (which writer), HDE Schemas & Artifacts §1.2 "Close-pack artifacts" (writer and evidence home), Glow QA Guide "Close-pack truthfulness and same-run execution" and "Close report requirements" (the post-verdict home). Operative documentation: AGENTS.md "HDE-EPIC039 current workflow posture" and README line 25 (final documentation unit). Drainage remains Product Owner-owned.
- **Gaps.** The ADR's approval is pending (AQ-1). No architecture or feasibility unknown remains.
- **Disposition.** `PLAN_READY_PENDING_OWNER_DECISION` (plannable; reliance gated by AQ-1).

### S22 — Extend the canonical evidence-index updater's CRD admission to HDE-CRD-0002's QA root (Distillation)

- **Source clause.** S22 (CD-3; review v1.0 R2; HDE Schemas & Artifacts §8.17 "Change-container identity"): "Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`, and existing Epic and HDE-CRD-0001 inputs still publish and validate." Constraint "QA evidence admission".
- **Current behavior.** §5.6: single-ID admission (`CRD_QA_ID`, `CRD_QA_ROOT_REL`, `CRD_QA_KEY`), `publish_crd_check_family` refuses any other `crd_id` (line 4911), `_load_crd_qa_entries` reconciles only the one root; `qa_harness.HarnessConfig` already accepts any canonical CRD ID and derives the lower-case root; tests cover the HDE-CRD-0001 posture through a fixture repository.
- **Required behavior.** An explicit admitted-CRD table (`HDE-CRD-0001` and `HDE-CRD-0002`, each with its root and key prefix; "source-owned admission", no directory discovery), the entry builders, reconciler and publisher parameterized by admitted ID, the refusal message naming the admitted set, and the root-absent case preserved (`audit/qa/hde-crd-0002/` is QA-created later; its absence publishes nothing).
- **Affected components.** `tools/evidence/update_evidence_index.py`; `tests/evidence/test_evidence_index_missing_state.py` (parametrize the `crd_repo` cases over both IDs; foreign-scope and forgery cases for the new ID); `docs/EVIDENCE_INDEX.md` (final documentation unit). The Index and Mirror are regenerated by the updater only (no row changes expected until QA creates the root).
- **Dependencies.** Lands before QA-10 readiness (Specification phase table); shares the unit with S12.
- **Feasibility.** Yes.
- **Risks.** None material; the generic harness tests already prove multi-ID acceptance (`test_crd_ordinary_recording_accepts_expanding_canonical_ids`).
- **Tests and evidence.** The parametrized evidence tests; `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`.
- **Canon and documentation effects.** Implements the compatibility duty of HDE Schemas & Artifacts §8.17 without changing it; AGENTS.md "sole active writer" statement unchanged.
- **Gaps.** None.
- **Disposition.** `PLAN_READY`.

## 7. Cross-cutting findings

### 7.1 Engineering choices resolved within IA authority

Each choice stays inside the approved scope and acceptance intent; none rewrites the Specification. The Plan carries them; Isis can reverse any of them by redline.

| ID | Requirement | Choice | Basis |
| :---- | :---- | :---- | :---- |
| EC-1 | S05 | Align the workflow skip list to the classifier's eight prefixes with explicit negations for governed primaries under them (today `docs/run/EPIC011_TEST_IDENTITIES.md`, `docs/run/PROD_ENDPOINTS.json`), pinned by a test that reads `docs/evidence/INDEX.json`. | The classifier itself gives those two files the evidence lane; skipping CI for them would lose protection the acceptance intent does not ask to remove. |
| EC-2 | S09 | Retire the dev harness; repoint `VERIFY.sh` and the crib to the canonical dev runner. | The Specification allows either; the canonical runner exists and the harness duplicates it with a stale gate. |
| EC-3 | S03 | Record retirement reasons in a tracked ledger `tests/retired_tests.md` in addition to the PR record. | "Each retirement has a recorded reason" is durable only if the reason is in the repository. |
| EC-4 | S10 | `scripts/dev_start_reader.sh` defaults `APP_ENV=dev` when unset; `docs/server/reader_v1.md` states it. | Constraint "Dev route": S10 must not break dev use; the runner would otherwise start a refusing `/reader`. |
| EC-5 | S12 | Current-release capture rows carry release-identifying fields (version and `release_id`, or an equivalent `release_binding` field); origin keys stay; frozen families keep capture-time labels. | The acceptance intent names the label, not the field; the owner defines the field set. |
| EC-6 | S07 | The frozen `artifacts/cli/help/*` family stays frozen with a nonclaim that it captures the earlier help text; `docs/CLI_commands.md` loses its known-gap sentence. | AGENTS.md "Release identity" (never refresh EPIC022 capture-time records); PR06b §6.4 precedent; `--check` validates bytes, not live output. |
| EC-7 | S14 | Audit sink: one local append-only JSONL file; path from one new operator environment key with a default under the operator's state directory; actor principal from the OS user of the executing shell; absence of either refuses with `PROVIDER_AUDIT_UNAVAILABLE`. | PF05 §7.1.11f fixes the record, not the location; no production configuration change (Exclusions bullet 5); the CLI runs in the operator's shell (Glow Infrastructure §2.6). The key name is a Glow Infrastructure doc-delta candidate. |
| EC-8 | S15 | Catalog every registered route; remove none. `/aux/narrative` follows the HDE-CLI-API-Vendor-Ref §5.6 projected record (`public_aux`, alias `/api/aux/narrative`); the ops probes and the two `adapter.wsgi` health routes get internal rows with their observed gates. | Removal is a production-surface change no requirement asks for; §5.6 already projects the Aux record. |
| EC-9 | S20 | Tool path `tools/ci/prepush_check.py` with owner test `tests/tools/test_prepush_check.py`; delegates to the classifier; replays `ci.yml` text. | Concrete deliverable paths are required for a planned unit (HDE Governance §9.7, mechanical blockers); no existing `tools/` prefix fits a CI helper. |
| EC-10 | S21 | New schema version `schemas/close_candidate_source.v2.json` (v1 retained), writer kept at `tools/qa/generate_epic_close_pack.py`, close-run evidence under `audit/qa/<change-id>/close/<check_id>/primary.log` as an ADR-admitted post-verdict family, ADR at `docs/adr/hde/close_pack_writer_adr.md`. | Keeps the feedback-free invariant, lifts the closed vocabulary (B-1), gives same-run evidence a home that leaves the approved manifest closed (B-2); the ADR is the Product Owner's to approve (AQ-1). |
| EC-11 | S01 | Ship the sixteen missing members as package data at their roster-relative locations; do not change the loader. | The loader's root rule is fixed in a member; shipping data at the expected locations needs no member change. |
| EC-12 | re-cut | Each member-changing unit refreshes the manifest at the current version and timestamp and converges evidence (§5.1); the single new release `1.4.0`, with `ADMITTED_RELEASE_VERSION` and `ADMITTED_RELEASE_BUILT_AT_UTC` set at cut time and the roster unchanged (45), is cut once, after the last member-changing unit, following PR06b §5.4's convergence order. | Admission's byte binding (§5.1); AGENTS.md "Release identity" and "HDE-EPIC040 admission addition"; Specification constraint "Release members" (one re-cut with new admission pins). |

### 7.2 Items returned to owners (none require a Specification change)

| ID | Item | Owner | Effect on planning |
| :---- | :---- | :---- | :---- |
| AQ-1 | Approval of the S21 ADR (content proposed by the Plan and drafted in the S21 unit). | Product Owner (HDE Governance §9.7.3; Change Process Guide §1.0.5). | None on planning; gates reliance on the new writer for any Close Gate, including HDE-CRD-0002's. |
| DD-C1 | Doc-delta candidates (non-mandatory, PO-owned): HDE-CLI-API-Vendor-Ref §7.1.11 "Required-Now implementation gap (DD-04; held)" paragraph and HDE Users Guide §16 `--allow-prod-vendor` bullet (stale after S14); Glow Infrastructure §8 config keys (the S14 audit-sink key) and §4.1/§10 (deployment trigger and build command, once OPS-01 discovers them); HDE Schemas & Artifacts endpoint-catalog registration of `public_aux` and `aliases` if not yet registered (S15); HDE Schemas & Artifacts Mirror schema if S12 adds fields; the three close-pack homes through the S21 ADR; `docs/ADAPTER_009.md` line 55 `ENGINE_ENV` wording (outside S17's bound). | Product Owner and the owning PF maintainers. | None; recorded for drainage, never as a plan deliverable (HDE Governance §9.7 "Documentation drainage is never a planning or approval gate"). |
| N-1 | The Notion board card for HDE-CRD-0002 is stale (`CRD_PENDING`, "Not started: Specification"). | Its owner. | None; this session is read-only on Notion. |

### 7.3 Release re-cut: forced set and order

- Member-changing requirements: S07, S08, S14 (`engine/cli/main.py`; S14 also `engine/bodygraph/resolver.py`), S10 (`adapter/http_reader.py`); possibly S19 fixes (members among the 48 inputs: `adapter/http_reader.py`, `engine/bodygraph/{mapped_cache,projection,resolver,v2_adapter}.py`, `engine/cli/main.py`, `engine/compat/{compute,error_tokens}.py`, `engine/config/registry_loader.py`, `engine/http/compat_handler.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, `adapter/schemas/error_v1.schema.json`, `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`, `errors/token_map/token_map.json`, `tools/bodygraph/check_magic10_gate_readiness.py`). Non-member units (S01–S06, S09, S11–S13, S15–S18, S20–S22) force nothing.
- Each member-changing unit refreshes `catalog/manifest.json` at the current version through the cutter and converges the generated evidence in PR06b §5.4's order (admission would otherwise refuse the intermediate state, §5.1). The version-bump unit changes `engine/config/registry_loader.py` (version and timestamp constants) and cuts `1.4.0`, then converges again; it lands after every member-changing unit and before QA-10 readiness. One new release only (Exclusions bullet 2).

### 7.4 Live QA surface confirmation (Specification table, re-read against current state)

| Class | Finding |
| :---- | :---- |
| Functional-feature class (S14, S02, S10, S07, S08, S15 route removal) | Unchanged. S15 removes no route under EC-8, so S15 stays "catalog entries only". |
| Production-affecting outside functional scope (S01) | The checked-in deployment declarations do not install the distribution (§5.4); the live Railway build setting is unverified and `discoverable by OPS` (Plan OPS-01). The QA Plan may record the S01 exemption basis on that discovery. |
| Inherits (S19) | Each fix takes its surface's class; the Plan names fixes when they exist (S19 unit result). |
| Not production-affecting | Unchanged for S03–S06, S09, S11–S13, S16–S18, S20–S22. |

### 7.5 CI lane consequences by unit (Observed classifier rules)

Full validation (every lane) is triggered by `pyproject.toml`, `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`, `pytest.ini`, `requirements*.txt` and `tests/evidence/test_rails_ci_workflow_integration.py` (classifier lines 29–39): the CI unit (S03–S05), the S20 unit (classifier registration) and the Coagulation unit (`pyproject.toml`) run all seven lanes. `adapter/http_reader.py` has its own owner-guard tuple (`_HTTP_READER_TEST_OWNERS`, lines 283–323) that must include any new consumer test. New `.py` files under unregistered `tools/` prefixes fail classification until registered (S14's audit module under `engine/` needs an owner test; S20's tool under `tools/ci/` needs lanes and an owner).

### 7.6 Risk register

| ID | Risk | Affects | Treatment |
| :---- | :---- | :---- | :---- |
| R-1 | S03 exposes real defects or needs more retirements than expected; the unit grows beyond one PR. | S03 unit | The per-PR plan bounds the work by class (§5.7); a bounded rescope (RS lane) if needed; the 135-file inventory is fixed here. |
| R-2 | The re-cut invalidates generated evidence if run out of order or twice with member changes in between. | re-cut unit | PR06b §5.4 order; restart rules (member byte change restarts at the cut; primary change restarts at the updater). |
| R-3 | S14 audit durability or actor identity unavailable in the operator shell during Live QA. | QA | Specified refusal (`PROVIDER_AUDIT_UNAVAILABLE`); the QA Plan verifies the sink before the live call. |
| R-4 | S21 ADR not approved by the time HDE-CRD-0002 closes. | closeout | S21's writer is not relied on; the ordinary Close Gate waits or an exceptional closure is the Product Owner's decision (Change Process Guide §3.5.1). |
| R-5 | S19 findings enlarge the work after the surfaces units merged. | S19 unit | Fixes land in the S19 unit before the re-cut; larger findings route with reasons. |
| R-6 | Top-level wheel data directories collide in a shared environment. | S01 | Documented dedicated-environment install; no shared-site-packages claim. |
| R-7 | Catalog validator changes (`public_aux`, `aliases`) run ahead of HDE Schemas & Artifacts registration: a search of that document for `public_aux` and `aliases` finds no registration, and HDE-CLI-API-Vendor-Ref §5.6 says PF12 must register them before catalog conformance may be claimed. | S15 | Follow the §5.6 projected record; record the PF12 registration as a doc-delta candidate; claim no "catalog conformance". |

## 8. Decisive questions register

| ID | Question | Affected | Inspected evidence | Known facts | Exact unknown | Alternatives | Decision criteria | Owner | Stage deadline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ-1 | Does the Product Owner approve the S21 ADR as the Plan proposes it (new candidate-source schema version admitting Epic and CRD identities with the canon-required close-report content; close-run evidence under an ADR-admitted post-verdict family in the change's QA root; writer kept at its registered path)? | S21; CD-1; Close Gate availability for HDE-CRD-0002 and later changes | §5.6, §6 S21, CLOSE01 §1.1–1.2, Change Process Guide §3.5.1–§3.5.2.1, HDE Schemas & Artifacts §1.2, Glow QA Guide close-pack sections | The current writer cannot express the required report (B-1); every admitted evidence home is a manifest check (B-2); ADRs are PO-owned | Whether the PO prefers a different evidence home or a separate close-report writer | (a) extend the generic writer and admit a post-verdict family (proposed); (b) a separate governed close-report writer beside the neutral one; (c) allow the close PR to add a manifest check after the verdict (rejected by CC-2) | Feedback-freedom preserved; no reopening of an approved QA manifest; one writer per artifact family; least canon drift | Product Owner | Before any Close Gate relies on S21's output; drafting proceeds in the S21 unit regardless |

No question blocks the Plan; no research package (IA-60) and no answer seed (IA-50) is needed.

## 9. RECOVERY_ENVELOPE (checkpoint)

```yaml
paused_prompt: none — IA-10 (100926.1) Phase 1 complete; Phase 2 (Plan) authored in the same invocation
phase: AUDIT_COMPLETE
base_identity: Specification v1.1 approved (docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md, blob c4802a5a7fa33db38d42d8a7f64679cd18b50480); Thoth INITIAL_APPROVE (docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md); PF10 v13.5.2 (blob ec71eeecec8b0fcff1645d317211258bc708712c), overlays NONE
checkpoint_identity: this artifact, docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md, repository head 982071b8203bfed961091811e24f57e99f92e593
completed_work: inputs verified; PF10 and canon resolved; S01–S22 audited with dispositions; shared facts, sweep, wheel comparison, S19 input set, re-cut set, Live QA confirmation
open_question: AQ-1 (Product Owner; non-blocking for the Plan)
evidence: §3 method; §5 facts; Appendices A and B
answer_state: not required for continuation
remaining_work: Phase 2 initial Implementation Plan (same author, same session), then IA-30 review
same_author_return: whole-change IA for HDE-CRD-0002, session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah
prerequisites: none beyond the inputs above
```

## 10. TypeSafe reading for the receiving session (IA-30 review)

Action sent (v6): "Review, as the independent whole-change Implementation Plan reviewer, a new 120 KB Implementation Audit and a new 60 KB initial Implementation Plan for an approved 22-requirement CRD Specification (CI coverage of 135 uncovered test files, release-evidence tooling, production HTTP error shaping and a dev-route gate, a canon production vendor-override contract with audit, a code security review of four merged PRs, a pre-push check tool, a close-pack writer with an ADR, packaging and one release re-cut), checking every requirement's disposition and the ten ordered PR, Ops and documentation work units against canon and the repository, then approving or returning itemized redlines. No code is written and no live run occurs; a Product Owner Proceed per PR and independent QA follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 3.36 (confidence 0.57); rung probabilities low 0.00, medium 0.01, high 0.18, extra high 0.25, max 0.55, ultracode 0.01. Model probabilities Fable 5.1 0.29, Opus 5.5 0.71 (confidence 0.42). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.13, Opus 5.5 at extra high 0.18, Opus 5.5 at max 0.39, Opus 5.5 at ultracode 0.01, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.07, Fable 5.1 at max 0.16, Fable 5.1 at ultracode 0.00. Sent 2026-10-12T20:30:55Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T20:30:55Z; HTTP 200 in 0.63 s; 4276 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: none; the rule's cell (Opus 5.5 at extra high) differs from the single most probable cell (Opus 5.5 at max 0.39), as the skill allows.
- **One send:** this reading was taken once, before the Audit and the Plan were saved, and is recorded identically in both artifacts.
- **Nathan's pick for IA-30:** not stated.
- **Nathan's pick for this IA-10 session:** not stated (the reading for IA-10 is recorded in review v1.1 §7).

**Surface advice:** run IA-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the continuing Isis reviewer lineage. It reads the approved Specification, review v1.1, the Audit and the Plan from `main`, `docs/pfcanon/` on `main`, and the repository files the Audit cites (the classifier, `ci.yml`, the updater, the resolver and CLI parser, the attestation builder, the close-pack writer and schema, `pyproject.toml`); it needs no live vendor, production or database access and writes only its review artifact under `docs/ephemeral/`. The pull request carrying the Audit and the Plan should be merged to `main` first.

## Canon relied on

Read on `main` at `982071b8203bfed961091811e24f57e99f92e593` (`docs/pfcanon/` unchanged since `df23bbf`, the last canon commit, #614). Sections read in full unless marked (grep) for a targeted passage.

- PF04-Canon-HDE-Governance v2.8.7: §9.1.1 "Change authority and exact-artifact lineage" (two authorities; Audit first; role table; approval map; historical drainage); §9.1.2 "Canon precedence and persistent sources"; §9.7.1 scope and stages; §9.7.3 identifier fidelity and PO-owned ADR stubs; §9.7.7 plan approval gate (artifact-level detail; identifier proportionality; QA planning post-implementation; implementation planning must not require QA evidence; no hidden acceptance; retrieval-first review); the planning-posture rules at lines 3118–3150 (Reality Audits consult; PF23 anchors; no PF update mandates; documentation drainage never a gate; infrastructure source rule); the mechanical-blocker list at lines 3175–3190.
- PF06-Canon-Change-Process-Guide v2.5.4: §0.1A "Specification format authority" and the Build Notes addendum rule; §0.5.1 "Plan path provenance" and locus validation labels; §1.0.5 "Canon changes" (ADR for canon-changing CRDs); §1.0.6; the canon-first and Live QA planning rules at lines 1035–1085 (PF07 postures; dev access address; Post-Audit ADRs); §1.1.5A "Production-affecting open-rails Live QA requirement"; the whole-change audit paragraph at lines 1501–1503; §2.x "Implementation Plans must be concrete enough" and the plan-execution boundary (lines 2295–2312); §3 "IMPLEMENTATION PLAN" machine header, tasks, blockers, approval and §3.5.1 Close Gate (PR route, up to 10 PRs; feedback-free terminal lifecycle; exceptional closure record); §3.5.2.1 "Close-pack files".
- PF27-Canon-Plan-Templates v2.0.5: "Artifact execution boundary"; "Repository loci and file minting"; "Unknowns, discovery, deferral, and open rails"; "Canon precedence for template use"; the IP evidence limits, ADR discipline and KISS evidence posture (lines 1098–1140); "Materiality-based blocker discipline for planning and review artifacts"; "CI lane classification and automated budget-control discipline"; §2A "Alchemical phase separation", "Existing-template reuse and substitution", "Canon, QA, and closeout boundaries", "PF30-owned Specification format and record contract"; §3 "Ops Task Record (Template)" in full.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §7.1.11 and §7.1.11a–f in full (production vendor override contract); §5.6 "Endpoint Catalog (JSON success)" in full.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6: §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)" (lines 583–660); §8.17 "Live QA evidence layout" opening and "Change-container identity (normative)" (lines 5258–5285); §8.12 "Reader A7 composite proof" (artifact write gating `HDE_WRITE_A7_PROOFS=1`; indexing); the "Endpoint Catalog and A7 proofs" evidence list (lines 2980–2989); searched for `public_aux` and `aliases` (no registration found).
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability (normative)" (lines 18–26); §3.1.1 "Integrated implementation audit and readiness"; "QA evidence and work-product path grammar (normative)" (lines 724–760); "Close-pack truthfulness and same-run execution" and "Close report requirements" (lines 1115–1140); §3.5.5 "Production-affecting Live QA minimum" (lines 1352–1375).
- PF07-Canon-Glow-Infrastructure v2.3.3: §2.4 "Env Deployment Inventory", Production — Railway; §2.6 "Prod on Railway, QA via Codespaces" (grep: Codespaces is a client to prod); §3.1 "Railway"; §4.1 "HD Engine" component map; §10 "Service start declarations", §10.1.
- PF03-Reference-Technical-Writing-Best-Practices v1.8.8: lines 495–506 (exact source-established identifiers; Implementation Plans may use the producing prompt's format).
- PF10-HDE-Build-Notes v13.5.2: read in full; addendum 2.1 applies to §10 only; silent on S01–S22.
- `AGENTS.md`: canon-first rule; PF canon read-only; release identity and the HDE-EPIC040 admission addition; sole Index/Mirror writer; HDE-EPIC039 workflow posture (generic close-pack capability); code-review scope prefixes; QA output placement.
- Not read (not relied on): PF23-Canon-Reality-Audits; PF29-Canon-HDE-Users-Guide §16 (cited through the Specification only); PF09 volumes (phase names taken from the Specification's phase table); PF30.1 (format of the Specification, not of this Audit).

**In-flight documents read in full:** `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`; `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md` (diffed against the approved representation); `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`; `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md`; `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`. Consulted by search: the HDE-EPIC040 records named in §3; `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md` §5.4 and §6.2–6.4; `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md` §1.1–1.2; PR bodies of amthorn78/glow-hdengine-v2#467, #501, #508 and #618 (GitHub); `docs/adr/hde/release_attestation_scaling_adr.md` (decisions 1–10).

**Prompts read:** IA-10 — Create Whole-Change Implementation Audit and Plan — 100926.1 (this invocation); IA-30 — Review Whole-Change Implementation Plan — 100926.1 (receiver contract for the handoff); the hub `HDE IA — GCFPE-20261009.1 — 100926.1` and the register entry `GCFPE Membership and Release Register Entry — GCFPE-20261009.1` (selection check). Prompt release: GCFPE-20261009.1 / 100926.1.

## Appendix A — The 130 test files outside every lane, owner target and `pytest.ini` root (at `982071b`)

Computed as §3(b) describes. The five `pytest.ini`-root files reached by no lane and no target (§5.3) are listed separately there; together they make the 135-file strict set the S03 unit treats.

- `tests/adapter/test_cache_keys.py`
- `tests/adapter/test_compat_writer_transport.py`
- `tests/adapter/test_env_guard_forbidden_matrix.py`
- `tests/adapter/test_env_guard_import.py`
- `tests/adapter/test_env_guard_import_purity.py`
- `tests/adapter/test_env_guard_prod_variants.py`
- `tests/adapter/test_env_guard_silence_and_idempotence.py`
- `tests/adapter/test_etag_core.py`
- `tests/adapter/test_gate_auth.py`
- `tests/adapter/test_headers_and_determinism.py`
- `tests/adapter/test_no_etag_on_writers_and_errors.py`
- `tests/adapter/test_reader_parity.py`
- `tests/adapter/test_readyz.py`
- `tests/adapters/test_safe_mode.py`
- `tests/arch/test_arch_capture_exists.py`
- `tests/arch/test_arch_guards.py`
- `tests/artifacts/test_cli_text_artifacts_bom_lf.py`
- `tests/audit/test_acceptance_map_epic017.py`
- `tests/audit/test_acceptance_map_epic019.py`
- `tests/audit/test_acceptance_maps_index.py`
- `tests/audit/test_epic017_close_report.py`
- `tests/audit/test_epic017_docdeltas.py`
- `tests/audit/test_epic017_manifest.py`
- `tests/audit/test_epic020_acceptance_bundle_wiring.py`
- `tests/bodygraph/test_bg_resolve_route_policy.py`
- `tests/bodygraph/test_resolver_vendor.py`
- `tests/canon/test_center_order_and_counts.py`
- `tests/canon/test_checksums.py`
- `tests/canon/test_error_envelope.py`
- `tests/canon/test_loader_integrity.py`
- `tests/canon/test_overrides_prod.py`
- `tests/canon/test_report_determinism.py`
- `tests/compat/test_cli_public_bytes_identity.py`
- `tests/compat/test_thresholds_constants_pack.py`
- `tests/compat/test_ts_import_no_io.py`
- `tests/compat/test_ts_sidecar_checks_manual.py`
- `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py`
- `tests/compliance/test_cli_admin_gate_sidecar_perms_and_stdout_hash_invariance.py`
- `tests/compliance/test_cli_release_id_resolver_precedence.py`
- `tests/compliance/test_invocation_tag_accept_reject_and_roundtrip.py`
- `tests/compliance/test_log_shape_snapshot.py`
- `tests/compliance/test_meta_abba_parity.py`
- `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py`
- `tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py`
- `tests/compliance/test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py`
- `tests/compliance/test_reader_etag_and_conditional.py`
- `tests/compliance/test_reader_etag_compression_invariance.py`
- `tests/compliance/test_release_id_precedence_and_grep_guard.py`
- `tests/em/test_em_defaults_and_ladder.py`
- `tests/em/test_em_off_toggle.py`
- `tests/em/test_em_throat_and_adjacency.py`
- `tests/em/test_goldens_public_shape_and_identity.py`
- `tests/epic003/test_error_message_map.py`
- `tests/epic003/test_http_home_single_path.py`
- `tests/epic003/test_legacy_imports_denied.py`
- `tests/evidence/test_aux_preview_identity_parity.py`
- `tests/evidence/test_cli_conformance_artifacts.py`
- `tests/evidence/test_db_runtime_posture.py`
- `tests/evidence/test_env_matrix_snapshot_v3.py`
- `tests/evidence/test_epic018_manifest.py`
- `tests/evidence/test_epic020_bundle_index_integration.py`
- `tests/evidence/test_epic030_pr01_pr03_fail_closed_evidence.py`
- `tests/evidence/test_epic030_pr04_band_thresholds_evidence.py`
- `tests/evidence/test_evidence_index_env.py`
- `tests/evidence/test_evidence_index_snapshot.py`
- `tests/evidence/test_evidence_index_token_sets.py`
- `tests/evidence/test_hdapi_v2_contract_inventory.py`
- `tests/evidence/test_hdapi_v2_live_conformance.py`
- `tests/evidence/test_hdapi_v2_response_normalization.py`
- `tests/evidence/test_hde_epic035_pr03_evidence_loop.py`
- `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`
- `tests/evidence/test_hde_epic037_bg_resolve.py`
- `tests/evidence/test_hde_epic037_field_sufficiency.py`
- `tests/evidence/test_hde_epic037_pr05_parent_binding.py`
- `tests/evidence/test_hde_epic037_v2_to_compat.py`
- `tests/evidence/test_identity_provenance.py`
- `tests/evidence/test_internal_version_manifest_captures.py`
- `tests/evidence/test_presenter_evidence_ownership.py`
- `tests/evidence/test_refresh_policy_snapshot.py`
- `tests/evidence/test_release_bindings.py`
- `tests/evidence/test_sampler_evidence.py`
- `tests/evidence/test_sanity_evidence_index.py`
- `tests/evidence/test_v2_mapped_cache_evidence.py`
- `tests/hdctl/test_cli_admin_sidecar_invariance.py`
- `tests/hdctl/test_cli_read_singlebg.py`
- `tests/hdctl/test_cli_showcompat_parity.py`
- `tests/hdctl/test_cli_streams_and_exits.py`
- `tests/hdctl/test_cli_two_run_identity.py`
- `tests/identity/test_service_identity_canonical.py`
- `tests/infra/test_hash_coupling.py`
- `tests/infra/test_resolver_serializer_discipline.py`
- `tests/infra/test_sercanon_bytes.py`
- `tests/infra/test_serializer_guard.py`
- `tests/integration/test_normalized_fixture.py`
- `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py`
- `tests/loader/test_load_chart_fixture_only.py`
- `tests/loader/test_loader_hdapi_ignores_tz.py`
- `tests/loader/test_loader_logs_keys_only.py`
- `tests/loader/test_pinned_lists_not_empty.py`
- `tests/loader/test_validators_strict.py`
- `tests/provider/test_factory_and_safemode.py`
- `tests/provider/test_hdapi_error_mapping.py`
- `tests/provider/test_hdapi_json_headers.py`
- `tests/provider/test_hdapi_request_shape.py`
- `tests/provider/test_provider_call_logging_keys_only.py`
- `tests/provider/test_provider_interface_contract.py`
- `tests/provider/test_prtest_precedence_and_artifact.py`
- `tests/provider/test_resolve_log_correlation_id.py`
- `tests/provider/test_secrets_dir_invalid.py`
- `tests/provider/test_secrets_errors_typed.py`
- `tests/provider/test_secrets_unknown_provider_is_misconfigured.py`
- `tests/provider/test_startup_logging.py`
- `tests/provider/test_vendor_and_prod_guard.py`
- `tests/provider/test_vendor_and_prod_guard_min.py`
- `tests/provider/test_vendor_call_rails_and_config.py`
- `tests/provider/test_vendor_guard_min.py`
- `tests/provider/tests/provider/test_decisions_perms_and_newline.py`
- `tests/reader_v1/test_cli_proof.py`
- `tests/scripts/test_dev_sampler_healthcheck.py`
- `tests/test_catalog_canon.py`
- `tests/test_pipeline_properties.py`
- `tests/test_pipeline_public.py`
- `tests/test_resolver_prod_rules.py`
- `tests/test_sercanon.py`
- `tests/unit/test_channel_derivation.py`
- `tests/unit/test_enum_closure.py`
- `tests/unit/test_narratives_composer.py`
- `tests/unit/test_no_io_guard.py`
- `tests/unit/test_sampler_core.py`
- `tests/unit/test_viewer_prefs_normalization.py`

## Appendix B — S19 review input: code and configuration files merged by #467, #492, #501 and #508 that still exist on `main`

Union of the four squash commits' non-document, non-test, non-evidence paths (`docs/`, `tests/`, `audit/`, `artifacts/`, `goldens/`, `narratives/`, `fixtures/` excluded), 48 paths; sidecars included where the PR changed them. Attribution: `cd6f9e6` (#467, PR04), `4d7ab9d` (#492, PR05), `f7484d0` (#501, PR06), `d79cfc1` (#508, PR06a).

`.github/workflows/ci.yml` (#467); `adapter/factory.py` (#508); `adapter/http_reader.py` (#467, #508); `adapter/schemas/error_v1.schema.json` (#501); `adapter/wsgi.py` (#508); `catalog/manifest.json` (#467, #501, #508); `ci/checks/classify_ci_changes.py` (all four); `ci/checks/run_rails_job_definitions.py` (#467); `ci/jobs/rails_open_conformance.yml` (#467); `engine/bodygraph/ingest.py`, `engine/bodygraph/mapped_cache.py`, `engine/bodygraph/projection.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/v2_adapter.py`, `engine/cli/main.py`, `engine/compat/compute.py`, `engine/compat/error_tokens.py`, `engine/config/__init__.py`, `engine/emit_public.py`, `engine/http/compat_handler.py` (#467); `engine/config/registry_loader.py` (#508); `engine/runtime/public.py` (#467, #508); `errors/token_map/token_map.json` and its `.path_proof.txt` (#467, #501); `presenter/reader_v1/emitter.py` (#508); `schemas/reader.v1.schema.json` and `.sha256` (#501, #508); `schemas/reader.v2.schema.json` and `.sha256` (#508); `scripts/cut_release_manifest.py` (#501); `scripts/make_reader_v1_goldens.py`, `scripts/make_release_pack.sh` (#508); `tools/bodygraph/check_magic10_gate_readiness.py`, `tools/config/artifacts.py`, `tools/config/generate_config_artifacts.py` (#492, #501 for the latter two); `tools/cli/generate_cli_conformance_artifacts.py`, `tools/cli/generate_showcompat_artifacts.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/generate_determinism_gate_proofs.py`, `tools/evidence/generate_epic030_pr05_category_framework_evidence.py`, `tools/evidence/generate_hde_epic037_v2_to_compat.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/run_sanity_pipeline.py`, `tools/evidence/run_sanity_pipeline_gate.py` (#467); `tools/evidence/generate_a7_transport_proofs.py` (#467, #508); `tools/evidence/generate_open_rails_abba_proof.py` (#467, #501, #508); `tools/evidence/run_canonical_json_gate.py` (#467, #501); `tools/errors/generate_error_artifacts.py` (#501); `tools/evidence/generate_conjunction_writer_evidence.py` (#508).
