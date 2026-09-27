---
artifact_type: QA_AUDIT
artifact_id: HDE-EPIC040-QA50-QA-AUDIT
artifact_version: "1.0"
predecessor: none (first QA Audit for this change)
state: AUDIT_COMPLETE
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-50 / whole change
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1 (Notion 3db4590a05eb81a3ac91f602bad8cfa2; page as of 2026-09-24T15:54:17.481Z; read in full)
ecosystem_release: GCFPE-20260914.1 (091426.1)
live_qa_guide: docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md (LIVE_QA_GUIDE v1.0, GUIDE_READY)
qa_readiness: docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md (QA_READINESS v1.0, READY_FOR_QA)
reality_audit: docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md
change_audit_triage: docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md
po_disposition: docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md (Q-1 yes, Q-2 yes)
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md (SHA-256 54e660e364c29b9f0d91b6de28ca15efee4ae346f8ecd032833f2e47d8cebf0d; 299,321 bytes; read in full)
observed_revision: a6002d27cd955c814e90661ae2309dc74b190733 (origin/main after #534)
observation_time_utc: 2026-09-27T09:26:32Z
companion: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-50
---

# HDE-EPIC040 — Whole-Change QA Audit v1.0 (QA-50)

This is Kronos's independent QA Audit of the delivered HDE-EPIC040 change. It records what the repository and planning environment actually contain, what QA can and cannot test, and which gaps belong to which owner. It is the planning-time D0 introspection record required by PF19-Canon-Glow-QA-Guide §3.6 and the "initial QA Audit" provenance source for every repository-resident locus the companion QA Plan uses (PF27-Canon-Plan-Templates, "Path provenance and locus provenance lock").

It executes no QA, selects no task, approves nothing and declares no PASS. Every locus below was read or listed directly; nothing here is a test result unless a row says so.

## 1. Method and limits

| Item | Record |
| --- | --- |
| Checkout | `amthorn78/glow-hdengine-v2`, branch `claude/hde-epic040-separation-pass-3-qa-u24ee0` at `a6002d2` (identical to `origin/main`). Working tree clean before and after (`git status --porcelain` empty) |
| History | The clone was shallow (depth 51). It was deepened read-only (`git fetch --deepen=400 origin main`) to resolve lineage commits; no ref was rewritten |
| Read-only commands | `grep`, `sed`, `find`, `ls`, `git log`, `git diff`, `git check-ignore`, `sha256sum`, `sha256sum -c` (OPS01 ledger), Python JSON parsing, CLI `--help` and `pytest --collect-only` |
| Isolated execution | CLI help and pytest collection ran in a scratch copy (`git archive a6002d2`) outside the repository, with a fresh Python 3.12.3 venv (`requirements.txt`, `requirements-dev.txt`, `-e .`), closed rails, `APP_ENV=test`, and `DATABASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HDAPI_BASE_URL` unset. No test body ran. No generator, server, network, vendor or database call was made |
| Not done | No QA check, no route probe, no DB or vendor contact, no evidence write, no PF edit |
| Limits | Hosted CI history, deployed service state and live DB contents are Unknown. Collection counts are audit-time facts at `a6002d2`, not predicates |

## 2. Controlled sources resolved

Only the unique controlled Markdown under `docs/pfcanon/` was read as PF authority. No Drive, Google Doc, `.doc` or `.docx` variant was opened.

| Identity (in-document title) | Repository path | Use |
| --- | --- | --- |
| PF10-HDE-Build-Notes | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` | Read in full. Addenda §§2.2–2.28 apply to HDE-EPIC040 |
| PF19-Canon-Glow-QA-Guide | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md` | §§3.1.2, 3.3, 3.4.3, 3.4.9, 3.4.10, 3.5.7, 3.5.10, 3.6, 4.4.3–4.4.6, 10.6–10.8 |
| PF27-Canon-Plan-Templates | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md` | §A.1 Live QA Plan template and Review guardrails |
| PF05-Canon-HDE-CLI-API-Vendor-Ref | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` | §7.1.11, §7.3.9, §7.4 |
| PF07-Canon-Glow-Infrastructure | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md` | §§2.2, 2.4, 2.6–2.8, 7.0, 7.1, 7.2.1, 8.1, 10.1–10.3, 10.5 |
| PF09.3-Canon-HDE-Build-Checklist-Separation | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md` | Task HDE-SEPA005 and subtasks .1–.5 (L1148–L1210); status summary L171 |
| PF06-Canon-Change-Process-Guide | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md` | §0.4.1 (D0 Discovery artifact; QA RCA and Doc Delta summary) |
| PF04-Canon-HDE-Governance | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md` | §2.0 token roster (this change is tokenless) |
| PF12-Canon-HDE-Schemas-and-Artifacts | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md` | §8.3 Machine Mirror, §8.6 Index entries (follow-up publication only) |
| PF01-Canon-HDE-Math-Spec | `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md` | §9.5 goldens, as transcribed in `tests/fixtures/magic10/v1/goldens.json` |

Immutable approved bases: `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` (Specification v1.1), `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` (Plan v2.1) and `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` (Isis-50 APPROVE). Overlays on those bases are PF10 v13.3.9 §§2.7, 2.9, 2.10, 2.12, 2.15–2.18, 2.21, 2.23 and 2.25, as the QA-10 readiness record §2 lists. The Specification's line-265 ten-category exclusion is superseded for this change by PF10 §2.23 (C040-07).

PF10 addendum numbers differ between PF10 versions. This audit cites v13.3.9 numbers with the addendum heading. AGENTS.md's "PF10 §2.8" bounded-execution-source reference does not match v13.3.9, where §2.8 is "PF10-FORM-001"; the current home of that rule is PF19 §10.8 (see QA50-F12).

## 3. Change identity and accepted delivery lineage

| Unit | Pull request | Landed commit | Acceptance |
| --- | --- | --- | --- |
| PR01 catalog and contract data | #403 | `3828d4b` | ACCEPT (lineage review v1.1) |
| PR02 strict immutable admission | #404 | `5b2fb8d` | ACCEPT (lineage review v1.0) |
| PR03 pure Gate mechanics | #405 | `9cda1b4` | ACCEPTED_FINAL |
| PR04 application, identity, consumers | #467 | `cd6f9e6` | ACCEPTED_FINAL |
| PR05 golden comparison and readiness | #492 | `4d7ab9d` | ACCEPTED_FINAL (PF10 §2.20) |
| PR06 release admission and evidence | #501 | `f7484d0` | ACCEPTED_FINAL (PF10 §2.22) |
| PR06a Reader v2 (C040-07) | #508 | `d79cfc1` | ACCEPTED_FINAL (PF10 §2.24) |
| PR06b Reader v1 error envelope (C040-08), release 1.3.0 | #513 | `8999bd0` | ACCEPTED_FINAL (PF10 §2.26) |
| PR07 repository documentation | #518 | `edbd414` | ACCEPTED_FINAL |
| OPS01 external verification | #520 (task v1.0, attestation candidate), #526 (task v1.3) | `6f53d82`, `6e4b3a1` | Result v1.4 PASS; receipt v1.2 ACCEPT (PF10 §2.27) |
| DOC-20 documentation completion | #531 | `39b9cdf` | COMPLETE |
| QA-10 audit, triage, readiness | #532 | `fcb02f1` | READY_FOR_QA |
| PF10 v13.3.9, PF23 v1.2.1 | #533 | `78351a8` | Canon publication |
| QA-20 Guide and PO disposition | #534 | `a6002d2` | GUIDE_READY; Q-1 and Q-2 yes |

Landed commits were confirmed with `git log origin/main --grep "(#NNN)"`.

Since the QA-10 audited state `39b9cdf`, `git diff --name-only 39b9cdf a6002d2` changes 5 files under `docs/ephemeral/` and 3 under `docs/pfcanon/` only. No product, test, schema, catalog, CI or evidence byte changed. QA-10 readiness therefore still describes the code under test.

Release identity at `a6002d2`:

| Fact | Value | Proof |
| --- | --- | --- |
| Manifest | `catalog/manifest.json`: version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`, 45 `files` entries, each with `path`, `sha256`, `size` | JSON parse |
| Admission pins | `engine/config/registry_loader.py` L398 `ADMITTED_RELEASE_VERSION = "1.3.0"`, L399 `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` | read |
| `release_id` | `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` = SHA-256 of the canonical manifest bytes | `sha256sum catalog/manifest.json` |
| OPS01 attestation | `audit/ops/hde-epic040/ops01/attestation.json`: `release_id` and `manifest_sha256` equal the value above; `source_commit` `6f53d828a30101bb7cd6638f3695eb82c2b10979`; `validation_result` PASS; `release_admission` `PR06R_B_FINAL_PASS` | JSON parse |
| OPS01 ledger | `sha256sum -c SHA256SUMS` in `audit/ops/hde-epic040/ops01/`: 7 of 7 OK, rc 0 | executed read-only |
| Members since attestation | `git diff --name-only 6f53d82 a6002d2` over the 45 member paths and the manifest: 0 files. Whole diff: 8 files under `audit/ops/`, 19 under `docs/ephemeral/`, 3 under `docs/pfcanon/` | git |

The attested release bytes are the bytes under test. OPS01's supplemental adverse checks A-5 to A-7 ran at candidate `6e4b3a1` (#526); the attestation itself binds `6f53d82` (#520). The Guide §8 phrase "attestation proves release integrity at candidate `6e4b3a1`" conflates the two (QA50-F11, informational).

## 4. Audit-proven loci inventory

The companion Plan copies every repository-resident string it uses from this section (Audit-proven), from PF10 or PF-Canon (Canon-defined), or declares it QA-created.

### 4.1 Entrypoints and tools

| ID | Locus (verbatim) | Observed fact |
| --- | --- | --- |
| L-01 | `hdctl` | Sole console script, `[project.scripts] hdctl = "engine.cli.main:cli"` in `pyproject.toml`; subcommands `showcompat`, `aux-preview`, `bg:resolve`, `dev:sampler` (help rc 0) |
| L-02 | `engine/cli/__main__.py` | Present; `python -m engine.cli` is available |
| L-03 | `hdctl showcompat` flags | `--pair-file`, `--a-file`, `--b-file`, `--a`, `--b`, `--dump-reader`, `--dump-admin-dir`, `--source {db,vendor,auto}`, `--conjunction`, `--viewer-prefs-file`, `--user-a`, `--user-b`, `--birthdate-a`, `--birthtime-a`, `--location-a`, `--birthdate-b`, `--birthtime-b`, `--location-b` (help). Help summary still reads "Emit canonical Reader v1 bytes from vendor JSON (stdin or files)" (O-P07-01) |
| L-04 | `hdctl bg:resolve` flags | `--user` (required), `--source {auto,db,vendor}`, `--upsert`, `--dry-run`, `--birthdate`, `--birthtime`, `--location`. No `--allow-prod-vendor` (help; `grep -rn allow-prod-vendor` outside `docs/` returns 0) |
| L-05 | `showcompat --source vendor` path | `engine/cli/main.py` L686–692 resolves both birth tuples with `source_policy="vendor"`; `engine/bodygraph/resolver.py` sends a vendor policy without a local lookup to `_acquire_dry_run` (L789), which never persists (`_resolve_vendor_v2_chart` opens `DBAccess` only when not dry-run, L253). Missing birth input exits 64 `MISSING_VENDOR_INPUT` (`engine/cli/main.py` L215) |
| L-06 | `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root>` | Read-only comparison: exit 0 match (canonical report on stdout), 1 mismatch (stderr `GOLDEN_COMPARISON_MISMATCH:<n>`, no stdout), 5 refusal. `--goldens PATH` defaults to `tests/fixtures/magic10/v1/goldens.json`. `--report PATH` must lie outside the candidate root and the repository (`REPORT_PATH_INVALID` otherwise). Requires closed rails |
| L-07 | Comparator hazard | With no mode flag the same script runs the generator write path; `--check` validates committed primaries without writing; `--publish-family` writes. Only `--compare-goldens` and `--check` are read-only |
| L-08 | Goldens mismatch mechanics | `tools/config/artifacts.py` L258 pins annotations (`GOLDEN_ANNOTATION_SHA256`); an annotation change refuses `GOLDENS_INVALID` (exit 5). A changed `inputs` or `expected` value still runs and reports its own mismatch plus `transcription.expected` or `transcription.inputs` (L259–262, L407–414). Case `M10-G001` `expected.signals[0]` is `{"q": 0, "signal_id": "rapport_delta"}` |
| L-09 | `python tools/bodygraph/check_magic10_gate_readiness.py` | `--user-id UUID` (repeatable) or `--selection-file PATH` (canonical UUIDs, one per line, `#` comments, at most 1,048,576 bytes). Requires the five closed pins. Exit 0 prints canonical report: `schema` `magic10_gate_readiness.v1`, `readiness` `READY` or `NOT_READY`, `provider`, `read_only` true, `selection` {`requested`, `sha256`}, `counts` {`ready`, `missing`, `duplicate`, `row_invalid`, `payload_invalid`, `gates_invalid`}, `diagnostics`. Exit 5 with one stderr token: `RAILS_CLOSED_REQUIRED:<pins>`, `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`. Reads rows only through `read_current_mapped_bodygraph` |
| L-10 | `engine/bodygraph/mapped_cache.py` | `CURRENT_ROW_VIEW = "public.hde_body_graphs_current"`; `CURRENT_ROW_SQL` selects `user_id, vendor, vendor_version, input_fingerprint, payload` for one `user_id` and vendor `hdapi`; `read_current_mapped_bodygraph(db, canonical_user_id)` is one parameterized `SELECT` |
| L-11 | `engine.config.registry_loader.load_active_mechanics_bundle()` | Returns `AdmittedMechanicsBundle` with fields `registry`, `mechanics`, `manifest` (`Manifest`: `root`, `version`, `built_at_utc`, `files`), `config_sha256`, `source_identities`, `manifest_sha256`, `release_id`; fails closed otherwise |
| L-12 | `python scripts/release_id_recompute.py --check-manifest-only` | Read-only: validates canonical manifest bytes and audits the bytes and size of all 45 members (`manifest_only_problems`, L322–345); prints `MANIFEST_ERROR:<problem>` and exits 1 on any problem. Hazard: without `--check-manifest-only` or `--check` the script writes derived artifacts under `artifacts/math/` |
| L-13 | Read-only evidence validators | `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `python tools/evidence/validate_evidence_paths.py`, `./ci/checks/check_mirror_schema.sh` (a Python script; direct invocation, RA-13), `python tools/evidence/run_canonical_json_gate.py --check-only`, `python tools/evidence/check_lf_endings.py`, `ci/checks/check_evidence_index_hash.sh`, `ci/checks/check_env_pins.sh`, `python tools/config/generate_config_artifacts.py --check` (all present) |
| L-14 | HTTP server declaration | PF07 §10.1 (Canon-defined): `python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30`. `gunicorn` is in `requirements.txt`. `adapter/factory.py` has no `APP_ENV` start guard |
| L-15 | Comparator report | Canonical JSON (sorted keys, one LF) with keys `schema`, `candidate_root`, `goldens_path`, `goldens_sha256`, `candidate_release_id`, `config_id`, `ok`, `cases` (`case_id`, `case_type`, `kind`, `outcome` `match` or `mismatch`), `mismatches` (`case_id`, `path`, `expected`, `actual`) (`tools/config/artifacts.py` L1018–1033) |

### 4.2 HTTP surfaces on `adapter.factory:create_app()`

| ID | Route (verbatim) | Observed fact |
| --- | --- | --- |
| L-20 | `POST /api/reader` | `adapter/http_reader.py` `_production_reader_response`: exactly one `v` in `1`/`2` else 400 `ERR_READER_INVALID_VERSION` before the body is read; body at most 32,768 bytes (`_READER_MAX_BODY_BYTES`), bounded read also for chunked bodies; UTF-8 without BOM, JSON object with exactly `a_id` and `b_id`, lowercase canonical UUIDs, else 422 `ERR_READER_INVALID_INPUT`; DB unavailable 503 `ERR_M10_RESOLVER_UNAVAILABLE`; row missing 404 `ERR_M10_PERSON_UNRESOLVED`; admission refusal 503 `ERR_M10_MANIFEST_MISMATCH` or `ERR_M10_CONFIG_MISMATCH`. Reads rows through `read_current_mapped_bodygraph`; calls `evaluate_pair` without a cache; no DB write |
| L-21 | Reader error body | Exactly four keys `code`, `error`, `ok` (false), `schema` (`"v1"`); `Cache-Control: no-store`; no `ETag` (`docs/contracts/reader_v1_public_bytes.md` L21; `docs/contracts/reader_v2_public_bytes.md`, "Error body") |
| L-22 | Reader success body | Six keys `categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version`, `release_id`; v1 carries one `harmony` item or `[]`; v2 carries ten `{"band","id"}` items in the order `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`, or `[]`; no numeric field; headers `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, no `ETag` (`docs/contracts/reader_v2_public_bytes.md`) |
| L-23 | Non-POST on `/api/reader` | GET, HEAD, OPTIONS, PUT, PATCH, DELETE route to `reader_api.reader_method_not_allowed`; unrouted methods (TRACE, CONNECT, extension methods) get the same response from `before_request`. Body `{"code":"ERR_NOT_FOUND","error":"not found","ok":false,"schema":"v1"}` plus LF, `Allow: POST`, `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, no `ETag` (tests/http/test_reader_post_v2.py L232–259) |
| L-24 | Unknown path under `/api/` | HTML 404 from `adapter/factory.py` (O-P06a-22, PF10 §2.24; documented known limitation in `docs/contracts/reader_v2_public_bytes.md`) |
| L-25 | Dev routes | `GET /reader` (Reader v1): 403 `ERR_READER_FORBIDDEN` unless `os.environ.get("APP_ENV", "dev") == "dev"` (L603). `/dev/sampler/conjunction`, `/dev/reader/conjunction`, `/dev/writer/conjunction` (GET): `_dev_admin_gate` allows `APP_ENV` in {`dev`, `test`, `local`}, otherwise 403 `ERR_WRITER_FORBIDDEN` (O-P07-04 asymmetry for unset and `test`) |
| L-26 | Writing routes | `/dev/writer/conjunction` (GET) and `/ops/writer/diagnostic` (POST) call `_persist_idempotence_record`, which inserts into `hde.idempotent_writes` when `DBAccess.for_current_env()` can reach a database through `DATABASE_URL` and falls back to a process-local cache otherwise (`adapter/http_reader.py` L252–320, L873, L1128) |
| L-27 | Full route list | `/api/aux/narrative`, `/api/compat/v1`, `/api/reader`, `/aux/narrative`, `/dev/reader/conjunction`, `/dev/sampler/conjunction`, `/dev/writer/conjunction`, `/internal/dev/sampler`, `/internal/version`, `/ops/db/unavailable`, `/ops/probe/env`, `/ops/rails/refusal`, `/ops/writer/diagnostic`, `/reader`, `/static/<path:filename>` (Flask `url_map` of the factory) |
| L-28 | `GET /internal/version` | 200 JSON with `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`; `Cache-Control: no-store`; no ETag. `release_id` derives from the packaged manifest; `build_commit` is a static literal (`engine/runtime/identity.py` L26–40) and is not tested-source identity |

### 4.3 Environment names and infrastructure facts (PF07-derived)

| ID | Fact | Source |
| --- | --- | --- |
| L-30 | `DATABASE_URL` is the sole HDE DB key; direct psycopg only; `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD` are retired drift, reported names-only | PF07 §7.0 |
| L-31 | All environments share instance `ample-illumination/production/postgres`, schema `hde`; `public.hde_body_graphs_current` is the read-only boundary view the Reader uses | PF07 §2.2, §7.1, §7.2.1 |
| L-32 | QA console: GitHub Codespaces for `amthorn78/glow-hdengine-v2`; QA root pattern `audit/qa/<epic-id>/` | PF07 §2.6, §2.8 |
| L-33 | CLI-local vendor smoke target: `hdctl showcompat`, `--source vendor`, `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when geocoding is needed, pins `LC_ALL=C LANG=C TZ=UTC`, `SAFE_MODE=0` and `ALLOW_NETWORK=1` for the vendor step only, `APP_ENV=dev`; presence-only capture names listed | PF07 §2.7 |
| L-34 | QA Codespaces inventory: `ALLOW_NETWORK=0`, `APP_ENV=dev`, redacted `DATABASE_URL`, `DB_BRIDGE_URL` (retired key still listed), `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`, `HD_API_BASE_URL=https://api.humandesignapi.nl/v2`, `HDAPI_BASE_URL` deprecated alias only, `LANG=C`, `LC_ALL=C`, `TZ=UTC` | PF07 §2.4 |
| L-35 | Local-style client access uses `127.0.0.1`; production targets keep the real hosted URL `https://glow-hdengine-v2-production.up.railway.app` | PF07 §2.2 |
| L-36 | `PORT`: referenced by the start declarations; Development inventory `PORT=8000`; QA `DEV_SAMPLER_URL` uses port 8000 | PF07 §2.4, §10.3 |
| L-37 | PF05 §7.1.11b: `prod`, `production`, `live` are production-like; `dev`, `test`, `local`, `stage`, `staging` are recognized non-production; the production flag applies only to `bg:resolve --source vendor` | PF05 |

### 4.4 Test surface

`git diff --name-status 9065e6f a6002d2 -- tests/` lists 73 added or modified paths: 70 test files, `tests/fixtures/magic10/v1/goldens.json`, `tests/config/helpers.py` and `tests/support/pr04_fixtures.py`. Collection of the 70 files at `a6002d2` (Python 3.12.3, closed rails): 2,090 tests, rc 0. The counts are audit-time references, not predicates.

| Group | Test files (collected count) | Total |
| --- | --- | --- |
| A catalog, config, schemas | `tests/config/test_registry_catalog_contract.py` (67), `tests/config/test_magic10_contracts.py` (104), `tests/config/test_manifest_schema.py` (31), `tests/config/test_typed_bundles.py` (21), `tests/config/test_alias_policy_enforcement.py` (10), `tests/config/test_config_loader_unknown_ids_fail_closed.py` (2), `tests/config/test_registry_report.py` (2), `tests/config/test_registry_report_determinism.py` (6), `tests/config/test_registry_report_indexing.py` (2), `tests/compare/test_arrays_as_sets.py` (24), `tests/m10/test_defs_order.py` (2), `tests/m10/test_thresholds_rounding.py` (33) | 12 files, 304 |
| B admission, core, identity | `tests/config/test_production_admission.py` (136), `tests/config/test_execution_coherence.py` (67), `tests/core/test_engine_core_purity.py` (6), `tests/core/test_engine_core_determinism.py` (105), `tests/core/test_engine_core_abba.py` (8), `tests/m10/test_m10_symmetry_identity.py` (1), `tests/runtime/test_identity.py` (7), `tests/scripts/test_cut_release_manifest.py` (40), `tests/reader_v1/test_release_pack.py` (1) | 9 files, 371 |
| C comparison | `tests/config/test_config_artifacts.py` (153) | 1 file, 153 |
| D Gate ingress and readiness | `tests/bodygraph/test_gates.py` (55), `tests/bodygraph/test_projection_gate_ingress.py` (35), `tests/bodygraph/test_resolve_compat_chart.py` (38), `tests/bodygraph/test_check_magic10_gate_readiness.py` (63) | 4 files, 191 |
| E compat and CLI | `tests/compat/test_evaluate_pair_eligibility.py` (29), `tests/compat/test_conjunction_no_user_boundary.py` (21), `tests/compat/test_compat_public_ab_ba_identity.py` (2), `tests/compat/test_compat_public_lf_bom.py` (1), `tests/compat/test_abba_parity.py` (1), `tests/compat/test_hde_epic037_v2_adapter_to_compat.py` (5), `tests/cli/test_showcompat_sources.py` (17), `tests/cli/test_errors_parity.py` (39), `tests/cli/test_cli_usage_and_errors.py` (6), `tests/cli/test_cli_canonical_bytes.py` (6), `tests/cli/test_cli_file_inputs.py` (3), `tests/cli/test_showcompat_parity_and_identity.py` (7), `tests/artifacts/test_cli_text_artifacts_bom_lf.py` (1), `tests/qa/test_cli_admin_dumps.py` (2), `tests/qa/test_cli_admin_parity.py` (1), `tests/runtime/test_emit_public_legacy_helper.py` (5), `tests/epic003/test_meta_invocation_ok.py` (1) | 17 files, 147 |
| F Reader, HTTP, transport | `tests/http/test_reader_post_v1.py` (65), `tests/http/test_reader_post_v2.py` (66), `tests/http/test_reader_a7_transport.py` (2), `tests/http/test_endpoint_catalog.py` (8), `tests/http/test_compat_endpoint_contract.py` (34), `tests/http/test_dev_conjunction_http.py` (17), `tests/adapter/test_compat_http_dev.py` (2), `tests/adapter/test_compat_http_parity.py` (4), `tests/adapter/test_compat_writer_transport.py` (3), `tests/reader_v1/test_emitter.py` (29), `tests/reader_v1/test_goldens.py` (7), `tests/reader_v1/test_schema.py` (74), `tests/transport/test_a7_transport_proofs.py` (26), `tests/compliance/test_log_shape_snapshot.py` (1), `tests/compliance/test_logging_filter_keys_only_and_redactions.py` (1) | 15 files, 339 |
| G evidence and QA tooling | `tests/evidence/test_canonical_json_gate_check_outputs.py` (94), `tests/evidence/test_cli_conformance_artifacts.py` (5), `tests/evidence/test_determinism_gate_proofs.py` (15), `tests/evidence/test_dev_conjunction_identity.py` (10), `tests/evidence/test_engine_core_evidence.py` (10), `tests/evidence/test_epic030_pr05_category_framework_evidence.py` (4), `tests/evidence/test_evidence_index_missing_state.py` (45), `tests/evidence/test_evidence_tool_ownership.py` (27), `tests/evidence/test_open_rails_abba_proof.py` (78), `tests/evidence/test_rails_ci_workflow_integration.py` (133), `tests/evidence/test_sanity_pipeline.py` (18), `tests/qa/test_qa_tool_ownership.py` (146) | 12 files, 585 |

The seven groups partition all 70 files and all 2,090 collected tests without overlap. 36 of the 70 files are named by neither a `ci.yml` lane token nor the classifier's supplemental roster, so a full QA run of the EPIC040 surface is not otherwise guaranteed (RA-08).

Relevant in-process coverage already present: `tests/http/test_reader_post_v2.py` L247 exercises GET, HEAD, PUT, PATCH, DELETE, OPTIONS, TRACE, CONNECT, PROPFIND and QUERY on all three factories; `tests/http/test_reader_post_v1.py` L255 and `tests/http/test_reader_post_v2.py` L352 exercise admission refusal as 503 `ERR_M10_MANIFEST_MISMATCH` with injected rows.

CI pytest posture: `.github/workflows/ci.yml` L33–35 sets `SAFE_MODE: "1"`, `ALLOW_NETWORK: "0"`, `APP_ENV: dev`; L65 Python `3.12`; L106 exports `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and runs `python -m pytest -q -p no:cacheprovider`.

### 4.5 QA evidence and harness

| ID | Locus | Observed fact |
| --- | --- | --- |
| L-40 | `audit/qa/hde-epic040/`, `audit/docdeltas/hde-epic040_doc_deltas.md` | Absent at `a6002d2` (`ls` and `grep`, no match). Not matched by any ignore rule (`git check-ignore` rc 1 for the planned paths) |
| L-41 | `tools/qa/qa_harness.py` | `HarnessConfig("HDE-EPIC040", repo_root)` derives `audit/qa/hde-epic040`. `CheckResult(check_id, status, status_reason, check_name, command, command_provenance, exit_code, output, evidence_artifacts, intended_tokens, pf_refs, captured_env)`. `record_check` and `record_check_family` write `checks/<check_id>/primary.log` with a `pf27.step_log_header.v2` header and the flat manifest `qa_step_logs_manifest.json` (entries `check_id`, `log_path`, `status`). `run_pytest_check` runs `sys.executable -m pytest --version` then the tests, and maps rc 0 PASS, 5 TOOLING_BLOCKED, 2/3/4 or negative FAIL_TOOLING, other FAIL_BEHAVIOR |
| L-42 | Harness constraints | `pf_refs` must fully match the `PF_TITLE_RE` pattern (a `PF` number, then `-Canon-` or `-Reference-`, then a title), so `PF10-HDE-Build-Notes` cannot be a `pf_refs` value; `captured_env` admits only `LC_ALL`, `LANG`, `TZ`, `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`; `claimed_tokens` is always `[]`; the harness writes no path proofs and no Index or Mirror rows. Epic mode needs no acceptance map to record checks |
| L-43 | `tools/evidence/update_evidence_index.py` `_refresh_path_proof(path, *, default_produced_at, check)` (L4170) | The canonical updater's path-proof writer (fields `path`, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`). The HDE-EPIC039 QA runner `audit/qa/hde-epic039/00_meta/qa_runner.py` imports it (L17) to write QA path proofs |
| L-44 | Index and Mirror admission | The updater registers QA artifacts by explicit lists; HDE-EPIC039's QA manifest and RCA were registered by `932e6ab` ("evidence: register HDE-EPIC039 QA closeout artifacts": updater, test, regenerated Index and Mirror) after QA evidence landed in `16a7a62`. No HDE-EPIC040 QA registration exists. `validate_evidence_paths.py` reads only `artifacts/evidence_index.jsonl`; `ci/checks/check_final_lf.sh` checks a fixed file list |
| L-45 | CI effect of evidence commits | `ci/checks/classify_ci_changes.py` maps `audit/` paths to the `evidence` lane; `docs/ephemeral/` selects no lane |

### 4.6 Fixtures and inputs

| ID | Locus | Observed fact |
| --- | --- | --- |
| L-50 | `tests/fixtures/magic10/v1/goldens.json` | `schema` `magic10_goldens.v1`; eight cases `M10-G001` to `M10-G008`; constants `uuid_1` `00000000-0000-0000-0000-000000000001`, `uuid_2` `00000000-0000-0000-0000-000000000002` (synthetic PF01 §9.5 family) |
| L-51 | `audit/ops/hde-epic030/ops-02/vendor_command.txt` | Prior governed vendor command with birth tuples A (`1999-10-16`, `04:37`, `Santiago, Chile`) and B (`1978-06-17`, `02:35`, `Tallinn, Estonia`) |
| L-52 | `schemas/magic10_compat_result_v1.schema.json` | Top-level keys `schema`, `config_id`, `release_id`, `pair_key`, `signals`, `categories`; no Gate arrays |
| L-53 | `catalog/channels_v1.json` | Object with key `channels`: 36 rows, each with keys `centers`, `circuit_primary`, `domains`, `flags`, `gates`, `id`, `primary_domain`, `substream`; every `gates` pair ascending; 36 unique pairs; no null value |
| L-54 | `catalog/magic10_mechanics_v1.json` | Keys `category_weights` (10 items: `category_id`, `reducer`, `weights`), `config_id` `m10-channel-state-v1.0.0`, `profiles` (3: `activation_bp_v1`, `coherence_bp_v1`, `expression_bp_v1`), `response_scale`, `result_schema` `magic10_result.v1`, `rounding`, `schema` `magic10_mechanics_config.v1`, `signal_scale`, `signals` (20: `signal_id`, `profile_id`, `operation`, `channels`), `sources`. Operations: `equilibrium_score` `twice_min_owner_mass_v1`, `counterweight_ratio` `companionship_em_mass_v1`, the other 18 `weighted_state_sum_v1` |

## 5. Acceptance coverage and testability

| Criterion | Delivered proof so far | Runtime QA still needed | Testability | Planned check IDs |
| --- | --- | --- | --- | --- |
| AC040-01 scope and ownership | Lineage reviews; readiness §3; register §11 | Coverage record over the executed QA | Documentary; assessed in the QA-120 Report from lineage and closeout accounting | `qa-closeout-deliverables` |
| AC040-02 catalog and compatibility | PR01/PR02 tests and evidence | Execute catalog and bundle tests; read the actual catalog | Closed rails, repository-local | `ac040-02-03-catalog-config` |
| AC040-03 default and schemas | PR01/PR02 tests | Execute schema mutation tests; read the actual config | Closed rails | `ac040-02-03-catalog-config` |
| AC040-04 fail-closed consumption | PR02/PR03 tests | Execute admission and refusal tests; admit the actual checkout | Closed rails | `d0-discovery`, `ac040-04-05-admission-identity`, `ac040-04-09-compat-cli-offline` |
| AC040-05 identity | OPS01 A-5 to A-7; recompute rc 0 | Re-run manifest-and-member audit; bind the manifest to OPS01 | Closed rails | `ac040-04-05-admission-identity` |
| AC040-06 comparison | DOC-20 R6 (8 of 8) | Match twice, deliberate mismatch, before/after non-mutation | Closed rails | `ac040-06-golden-comparison` |
| AC040-07 ingress and readiness | Offline only (PF10 §2.20) | Ingress corpus; readiness refusals; live read-only observation of current rows | Offline: closed rails. Live: PO-only, real `DATABASE_URL`, PO-supplied selection; rows may not exist (PF19 §3.3) | `ac040-07-gate-ingress-offline`, `live-db-gate-readiness` |
| AC040-08 integrated evidence | E-D01 to E-D06 | Re-run read-only validators and evidence tests | Closed rails | `ac040-08-evidence-validators`, `qa-closeout-deliverables` |
| AC040-09 boundary | Code inspection; in-process tests | Public-surface probing over live HTTP; security step (Q-1); dev-route gating in production posture; numeric-free proof | Closed rails with a loopback server; live-DB refusal path with a real DSN; live-DB success path is conditional on current rows | `ac040-09-reader-http-in-process`, `sec-reader-http-live`, `live-db-reader-refusal`, `live-db-reader-success` |
| PF05 §7.3.9 open rails (Q-2) | None | Bounded vendor-backed CLI run | PO-only, open rails for the step | `open-rails-showcompat-vendor` |

## 6. Integration seams and functional proof

PF27 requires at least one functional proof per touched seam.

| Seam | Functional proof available to QA |
| --- | --- |
| Catalog and config to loader and admission | Admission of the actual checkout in `d0-discovery`; groups A and B |
| Admission to compat compute and pure core | Groups B and E; golden comparison through canonical entrypoints |
| Core to presenter and Reader v1/v2 emitters | Group F (in-process routes); `sec-reader-http-live` (live transport and refusal classes); `live-db-reader-success` (live success path, conditional) |
| CLI `showcompat` to resolver, vendor client, v2 adapter | Group E (offline); `open-rails-showcompat-vendor` (vendor-backed, end to end) |
| Resolver and mapped cache to DB (read) | Group D (fake DB); `live-db-gate-readiness`, `live-db-reader-refusal` and `live-db-reader-success` (live, read-only) |
| Readiness tool to DB | Group D; readiness refusal probes; live observation |
| Comparator to candidate root | `ac040-06-golden-comparison` |
| Release manifest to identity and attestation | `ac040-04-05-admission-identity` |

## 7. Environment, data, permissions and executors

Planning container (presence only): `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`; `DATABASE_URL` SET, `HD_API_KEY` SET, `GEO_API_KEY` SET, `HD_API_BASE_URL` UNSET, `HDAPI_BASE_URL` SET (deprecated alias), retired bridge keys UNSET, `ENGINE_ENV` UNSET, `PORT` SET. Default interpreter Python 3.11.15; Python 3.12.3 available. CI uses 3.12.

Consequences for planning:

1. Closed rails do not gate database access. `engine/db` has no `SAFE_MODE` or `ALLOW_NETWORK` check, and the readiness tool is designed to read the DB under closed rails. A closed-rails step that must not touch the live DB has to run with `DATABASE_URL` unset.
2. With `HDAPI_BASE_URL` set and `HD_API_BASE_URL` unset, a vendor step would read the deprecated alias. PF07 §2.4 and PF19 §3.5.7 make `HD_API_BASE_URL` canonical; the vendor step needs `HD_API_BASE_URL` set and `HDAPI_BASE_URL` unset.
3. Any `DB_BRIDGE_URL` presence (PF07 §2.4 still lists it for QA Codespaces) makes `DBAccess.for_current_env` refuse. Steps unset the retired keys and record their names only.
4. The live Reader success path and the live readiness observation need current rows. PF19 §3.3 states that no app users or persistent user-bound BodyGraphs are available in production pre-App; whether any `hdapi` current rows exist is Unknown (no mapped-cache write was found in `audit/ops/` or `audit/qa/`). QA must not create rows (`bg:resolve --upsert` is forbidden, PF19 §3.3).
5. `/dev/writer/conjunction` and `/ops/writer/diagnostic` write `hde.idempotent_writes` rows when a DB is reachable (L-26). Closed-rails local HTTP probes run without a reachable DB; live-DB checks never call those routes.
6. Vendor calls, secret handling and live DB access are PO-only (PF19 §3.3, §3.5.7). Closed-rails, repository-local checks may be delegated by the PO to a named repository-capable execution agent in the same checkout (PF19 §3.3, last bullets).

Permissions: QA writes only under `audit/qa/hde-epic040/` and `audit/docdeltas/hde-epic040_doc_deltas.md` (PF27: QA-created writes stay under `audit/**` or `artifacts/**`). Evidence storage is a separately authorized lane (PF19 §3.4.9); the Plan states its bounded commit permission.

## 8. Evidence posture

- QA root `audit/qa/hde-epic040/` is canon-defined (PF19 §3.4.3, §4.4.3–4.4.4; PF27 check-centric layout) and absent now. The Plan's first check records that absence before creating it.
- The generic harness (L-41) writes conforming primary logs and the manifest. It cannot record `PF10-HDE-Build-Notes` in `pf_refs` or secret presence in `captured_env`; those go in the log body (QA50-F07).
- PF19 §3.4.3 requires the manifest path proof whenever the manifest is created and the primary-log path proof whenever a primary log is governed evidence. The harness writes none. The canonical updater's `_refresh_path_proof` (L-43) produces the canonical format, as the HDE-EPIC039 QA did (QA50-F02).
- Index and Mirror publication of HDE-EPIC040 QA evidence has no admitted writer registration (L-44). Until the evidence owner adds it, the QA manifest cannot be claimed ledger-bound (PF19 §4.4.3, "Manifest ledger-coverage proof"). This limits that claim only; check verdicts do not depend on it (PF27 Step-0B: Evidence Index additions are follow-ups unless plan-required) (QA50-F01).
- Committing `audit/qa/hde-epic040/` triggers the CI `evidence` lane (L-45). HDE-EPIC039's unregistered QA evidence landed before its registration (`16a7a62`, then `932e6ab`); whether unregistered QA path proofs disturb `update_evidence_index.py --check` is not proven here, so the Plan re-runs that check after writing them.
- No acceptance map, token matrix or viability ledger exists for HDE-EPIC040. The change is tokenless; the PF19 §3.6 acceptance-map viability gate does not apply.

## 9. Planned versus delivered

| Item | Planned (Plan v2.1) | Delivered | Effect on QA |
| --- | --- | --- | --- |
| Reader v2 | Excluded by Specification line 265 | Delivered by PR06a under C040-07 (PF10 §2.23) | QA tests `?v=2` as a governed surface |
| Reader v1 error envelope | PR04 | Four-key `error_v1` per C040-08 (PR06b, PF10 §2.25) | QA asserts four keys |
| Release | Complete manifest in PR06 | Release 1.3.0 with 45 members in PR06b | Admission pins and OPS01 bind 1.3.0 |
| Live readiness | "Current production rows are unobserved in this Plan" (§5.9) | Offline tests only (PF10 §2.20) | Live observation owed; PO-only and data-dependent |
| Security review | Per-PR | No current-head security review for PR04, PR05, PR06, PR06a (PF10 §§2.19–2.24) | Bounded security step (Q-1) |
| Open-rails step | Plan Review v2.1 §5.4 citing PF05 §7.3.9 | None run | Required (Q-2) |
| Wheel packaging | Not planned | Non-editable wheel refuses admission (O-12, PF10 §2.22) | QA installs editable from the source tree |

## 10. Findings

Status vocabulary: a finding is not a failure unless it states an objective shortfall with evidence. No objective failure was found.

### 10.1 Test, evidence and setup gaps (owned by QA unless stated)

| ID | Finding | Evidence | Treatment and owner | PF09 accountability |
| --- | --- | --- | --- | --- |
| QA50-F01 | HDE-EPIC040 QA evidence has no Index or Mirror writer registration | L-44 | Evidence owner adds it through the whole-change IA PR route after QA evidence exists. Not a check prerequisite; blocks only a ledger-bound manifest claim | PF09.3 HDE-SEPA005.5 ("indexed evidence") |
| QA50-F02 | The harness writes no path proofs | L-41, L-43 | Plan uses `_refresh_path_proof` from the canonical updater, verified in check mode | None (no task created) |
| QA50-F03 | Closed rails do not block DB access | §7 item 1 | Every closed-rails step unsets `DATABASE_URL` and vendor keys | None |
| QA50-F04 | Comparator and release-recompute scripts write when run without their read-only mode | L-07, L-12 | Plan fixes the mode flags and forbids other modes | None |
| QA50-F05 | Live readiness and live Reader success need PO-supplied canonical UUIDs of existing current rows; existence Unknown | §7 item 4 | PO input. With no usable rows the live claim is `TOOLING_BLOCKED` (environment), never PASS (AC040-07: "unavailable live facts remain unavailable") | None (input availability) |
| QA50-F06 | 36 of 70 EPIC040 test files are outside fixed CI lanes | §4.4 | Plan runs all 70 files in seven groups | None |
| QA50-F07 | Harness `pf_refs` and `captured_env` limits | L-42 | PF10 citations and SET/UNSET secret presence go in the log body | None |
| QA50-F08 | Default interpreter 3.11 differs from CI 3.12 | §7 | D0 requires a Python 3.12 venv | None |
| QA50-F09 | Local HTTP routes can write `hde.idempotent_writes` | L-26 | Closed-rails local servers run with `DATABASE_URL` unset; live-DB checks probe only `POST /api/reader` and `GET /internal/version`, which do not write | None |
| QA50-F10 | `HDAPI_BASE_URL` set, `HD_API_BASE_URL` unset in the planning container | §7 item 2 | Vendor step requires `HD_API_BASE_URL` SET and `HDAPI_BASE_URL` UNSET | None |

### 10.2 Product defects

None evidenced. Carried items keep their recorded owners and remain non-gating: O-12, O-P06a-22, O-P07-01 to O-P07-04, O-P06a-03, O-P06a-23, O-P06b-17, O-OPS01-01 and O-OPS01-02 (QA-10 triage §2). QA observes O-P06a-22 and O-P07-04 without reclassifying them.

### 10.3 Plan defects

None evidenced in the approved Plan v2.1 or its overlays for QA purposes.

### 10.4 Specification ambiguity

| ID | Ambiguity | Safe reading used by the QA Plan | Owner |
| --- | --- | --- | --- |
| QA50-S01 | Plan v2.1 §7.4 says "never persist secrets, birth records or full Gate payloads in evidence"; PF19 §3.3 requires the vendor-smoke evidence to include the substituted birth-input record | Use PO-designated synthetic QA tuples, not a real person's data. Record them verbatim as PF19 requires. Default: the tuples in L-51 unless the PO names others | Isis confirms at QA-70; Thoth if a Specification clarification is needed |
| QA50-S02 | AC040-07 "current rows" does not name a population | The PO-supplied selection defines it; the report is aggregate and identity-safe | Product Owner |

### 10.5 Scope and authority boundaries

| ID | Boundary | Evidence | Treatment | PF09 accountability |
| --- | --- | --- | --- | --- |
| QA50-B01 | PF05 §7.1.11 `--allow-prod-vendor` is documented but not implemented | L-04 | Not needed: the vendor step uses `showcompat` with `APP_ENV=dev` (recognized non-production; PF07 §2.7). No production vendor call | PF09 gap (mapping not proven). Owner: PF05 and CLI owners through change control; outside HDE-EPIC040 |
| QA50-B02 | Deployed service identity is Unknown | No deployment record in scope | QA targets a local server from the tested source; no deployment claim | Out of scope |
| QA50-B03 | Vendor calls, secrets and live DB access | PF19 §3.3, §3.5.7 | PO-only execution | None |

### 10.6 Informational canon and source observations

| ID | Observation | Owner | Doc delta |
| --- | --- | --- | --- |
| QA50-F11 | Guide §8 says OPS01's attestation proves integrity at `6e4b3a1`; the attestation binds `6f53d82`, and `6e4b3a1` is the supplemental A-5 to A-7 run's candidate. No effect: members unchanged since `6f53d82` | Isis (Guide author), informational | Recorded in Step-0B |
| QA50-F12 | AGENTS.md cites "PF10 §2.8" for the bounded QA/OPS PF-copy rule; in v13.3.9 that rule lives in PF19 §10.8 | Repository docs owner | Proposed |
| QA50-F13 | PF19 §§3.4.3, 3.6 and 10.8 and AGENTS.md name ChatGPT Library or Google Drive for authored plans and canon reading; the PO storage decision D7 (`docs/prompt_ecosystem_management/gcfpe.decision-record.md`) and this prompt use `docs/ephemeral/` and `docs/pfcanon/` | PF19 maintainer; repository docs owner | Proposed, documentation drainage only |
| QA50-F14 | PF07 §2.4 still lists retired `DB_BRIDGE_URL` for QA Codespaces | PF07 maintainer | Proposed, documentation drainage only |
| QA50-F15 | PF07 §2.8 forbids git operations and QA-time scripts in Live QA runbooks; PF19 §3.4.9 permits read-only repository observation and PF27/PF19 permit embedded harness invocation and QA-created evidence harnesses | Isis for this Plan; PF07 maintainer for drainage | Register entry C040-09 (PROPOSED) |

## 11. CANON_CONFLICT_REGISTER

One register, carried unchanged for C040-01 to C040-08 from `docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md` §5, with the full original proposals and decision histories retrievable at the exact references below. C040-09 is new and PROPOSED. A proposal here is not approval.

| ID | Classification | Sources and clauses | Decision and status | Reviewer, artifact, time | Interim treatment | Drainage target and owner | Full history |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION | Pinned source/scope predicate | APPROVED exactly as proposed | Thoth-17, Specification v1.0 (represented by approved v1.1), 2026-09-08T13:23:24Z | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 v13.3.9 §2.2, §2.4 |
| C040-02 | CANON_RECONCILIATION | PF12 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-03 | CANON_RECONCILIATION | PF14 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-04 | CANON_RECONCILIATION | PF19 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-05 | CANON_RECONCILIATION | PF14 §6.7 superseded precomputed-score test instructions | APPROVED, alternative A | Isis-49, Plan v1.0 review, 2026-09-09T03:57:16Z | PF10 §2.3 governs | PF14 §6.7; PF14 maintainer; pending, non-gating | Plan v2.1 §11.2; PF10 §2.3 |
| C040-06 | NEW_CANON | 36-row Channel taxonomy and 16-case existing-state conformance | APPROVED, alternative A | Isis-50, Implementation Plan Review v2.0, 2026-09-09T11:48:08Z | PF10 §2.5 governs | PF12 §2.1, PF01 §§6.1–6.2; their maintainers; pending | Plan v2.1 §11.3; `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`; PF10 §2.5 |
| C040-07 | NEW_CANON | Full Magic-10 exposure via Reader v2 versus Specification line 265 and PF01, PF04, PF05, PF12 statements | PO decision 2026-09-26; delivered by PR06a | Product Owner; PF10 §2.23 | PF10 §2.23 governs; QA tests `?v=2` | PF01, PF04, PF05, PF12, with PF14 and PF29 consequences; their maintainers; pending | PF10 §2.23, §2.24 |
| C040-08 | CANON_RECONCILIATION | Reader v1 error envelope versus schema | Alternative A; delivered by PR06b | PF10 §2.25 decision record | PF10 §2.25 governs; QA asserts the four-key envelope | PF01 §2.3, PF04 §8.1.2; their maintainers; pending | PF10 §2.25, §2.26 |
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks"; QA-only harness scaffolding permitted) | PROPOSED. Recommended disposition: PF19 and PF27 govern the execution rail and plan shape, as PF07 §2.8 itself routes the execution rail to PF19. Alternatives: (a) recommended; (b) forbid all git reads and embedded helpers, losing tested-source attribution that PF19 §10.8 requires | Unreviewed. Native decision owner: Isis at QA-70 for this QA Plan | Interim: the Plan uses read-only git observations for attribution only, never as a PASS gate, and creates no script file; it invokes existing harness APIs through embedded `python -c` calls. Unresolved risk: a reviewer applying PF07 §2.8 literally | PF07 §2.8 wording; PF07 maintainer; documentation drainage only | This entry (original proposal, 2026-09-27) |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013).

## 12. Unresolved items and owners

| Item | Owner | Blocking |
| --- | --- | --- |
| QA50-F01 Index/Mirror registration of QA evidence | Evidence owner via whole-change IA PR route | Blocks only a ledger-bound manifest claim |
| QA50-F05 selection of existing current rows | Product Owner | Live readiness and live Reader checks are `TOOLING_BLOCKED` without it |
| QA50-S01 birth-tuple reading | Isis (QA-70) | No, safe default stated |
| C040-09 | Isis (QA-70) | No, interim treatment stated |
| QA50-B01 `--allow-prod-vendor` gap | PF05 and CLI owners | No |
| QA50-F12 to QA50-F14 doc deltas | Named maintainers | No |
| Carried items in QA-10 triage §2 and §4 | As recorded there | No |

## 13. Negative-claim proofs

| ID | Pattern or target | Method | Scope | Result |
| --- | --- | --- | --- | --- |
| N50-01 | `audit/qa/hde-epic040`, `audit/docdeltas/hde-epic040_doc_deltas.md` | `ls` with `grep -i epic04` | `audit/qa/`, `audit/docdeltas/` | 0 matches |
| N50-02 | Ignore rules for planned QA paths | `git check-ignore -v` | five planned paths | none ignored (rc 1) |
| N50-03 | `allow-prod-vendor` | `grep -rn` | repository outside `docs/` | 0 |
| N50-04 | Release members changed since `6f53d82` | `git diff --name-only` | 45 members and manifest | 0 |
| N50-05 | Non-documentation changes since `39b9cdf` | `git diff --name-only` | whole tree | 0 (8 files, all under `docs/ephemeral/` or `docs/pfcanon/`) |
| N50-06 | HDE-EPIC040 QA registration in the updater | `grep -n audit/qa/hde-epic040` | `tools/evidence/update_evidence_index.py` | 0 |
| N50-07 | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` | `ls` | exact path | absent |
| N50-08 | `SAFE_MODE\|ALLOW_NETWORK` | `grep -rln` | `engine/db/` | 0 files |

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-50-20260927-01
  change: EPIC / HDE-EPIC040 (Specification v1.1, docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md)
  components: HDE-SEPA005, HDE-SEPA005.1 to HDE-SEPA005.5; K040-REQ-001 to K040-REQ-013; AC040-01 to AC040-09
  prompt: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1; Notion 3db4590a05eb81a3ac91f602bad8cfa2; page as of 2026-09-24T15:54:17.481Z; release GCFPE-20260914.1
  role_stage: continuing Kronos, QA-50
  capture_time: 2026-09-27T09:26:32Z
  execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  result: QA_AUDIT v1.0 (AUDIT_COMPLETE) and QA_PLAN v1.0 (PLAN_PENDING)
  repository_persistence: PENDING / NON_GATING (no installed docs/changes/GCFPE_PROMPT_PROVENANCE.md; authorized owner: the GCFPE-MGMT-10 maintenance owner)
- earlier entries: GCFPE-USE-HDE-EPIC040-QA-10-20260927-01 (QA-10) and GCFPE-USE-HDE-EPIC040-QA-20-20260927-01 (QA-20), recorded in their artifacts
```
