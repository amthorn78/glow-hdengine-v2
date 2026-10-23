---
artifact_type: REALITY_AUDIT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-QA10-REALITY-AUDIT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
predecessor: none (first QA-10 for HDE-CRD-0002)
producer: Isis, continuing Lead Developer and whole-change readiness decision owner (Isis-53; this session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok; earlier Isis work for this change https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
prompt: QA-10 — Audit Implementation and Establish QA Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb8134af92e7c85a48e67c; page state of 2026-10-12T02:30:12Z, read in full: 93,929 characters)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_head_inspected: origin/main 39122b77b7f8e548e005e8bc82fabc2c6e33708b ("pf10", 2026-10-23T13:58:19Z)
companions: docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.0.md; docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.0.md
created_at: 2026-10-23T14:30:00Z
---

# HDE-CRD-0002 — Reality Audit v1.0 (QA-10)

This is a factual record of what the repository contains at `39122b7`. Compliance judgements belong to the triage; the readiness decision belongs to the readiness record.
- **No test or route was run here.** Read-only validator commands are recorded with their results.
- **CI evidence** is the hosted push runs, read from GitHub, and is attributed to the commit each run tested.

## 1. Audit Snapshot Metadata

| Field | Value |
| :- | :- |
| Class / change | CRD / HDE-CRD-0002 (Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer) |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (v1.1, approved by `…-specification-review-v1.1.md`, INITIAL_APPROVE) with Specification delta 01 `…-specification-delta-v1.0.md` (DELTA_APPROVE, `…-specification-delta-review-v1.0.md`; HDE Build Notes addendum 2.20) |
| Plan / review | `…-implementation-plan-v1.1.md` / `…-implementation-plan-review-v1.1.md` (INITIAL_APPROVE), with Plan delta 01 v1.1 `…-implementation-plan-delta-01-v1.1.md` (DELTA_APPROVE, `…-implementation-plan-delta-01-review-v1.1.md`; addendum 2.19) |
| Implementation Audit | `…-implementation-audit-v1.0.md` (AUDIT_COMPLETE) |
| Delivered units | Each PR-40 lineage review is ACCEPT (E-002). The PRs and squashes: WU-PR-01 #627 `7136040`, #630 `bf7ad8c`; WU-PR-02 #634 `1d2c834`, #637 `b26f44f`; WU-PR-03 #643 `c98d41f`, #646 `2f3db0a`; WU-PR-04 #651 `5892538`; WU-PR-05 #656 `822ce15`; WU-PR-06 #660 `b963ed4`; WU-PR-07 #668 `8b73b57` (companion #670 `102e97e`); WU-PR-08 #687 `1a4c8ab`; WU-DOC-01 #692 `4c9bbfc`, #695 `cf8b759`, #700 `f508dcf` |
| Ops | WU-OPS-01 task v1.0 (#703), execution result v1.0 attempt 1 PASS (#704), receipt v1.0 ACCEPT (#705; addendum 2.22) |
| Documentation | WU-DOC-01 completion v1.1, COMPLETE (#702) |
| Prior readiness history | None. Proof N-001 |
| Repository | `amthorn78/glow-hdengine-v2`. Local checkout detached at `39122b7`, plus a throwaway clone `--no-hardlinks` at the same commit. `git status --porcelain` was empty in both, before and after. Both are shallow (80 commits, boundary `142e56f`), so `39b9cdf` (PF23's baseline) is not an object here |
| Method | Direct read-only inspection by this session and four read-only workers inside this invocation (grep/find/git/python parsing with `-I`, `PYTHONDONTWRITEBYTECODE=1`, closed rails); six read-only validator commands (§9); hosted CI job logs read through GitHub (E-003). No install, generator, test, route probe, vendor, database or production call |
| Limitations | The container has no Flask or pytest. QA-10 forbids installing them, so no test was executed here; two validators that import Flask could not run (E-141, E-146). Routes were enumerated from decorators, not from `url_map`. Deployed state is known only from the WU-OPS-01 evidence (one read at 2026-10-23T13:30:06Z). History before the shallow boundary is unavailable |
| Canon read | Listed in "Canon relied on" at the end |

**Evidence pointers kept from the workers:** E-1xx (repository map, packaging, tests, CI), E-2xx (engine, adapter, presenter, CLI, vendor, flows), E-3xx (evidence, indices, catalogs) and E-4xx (documentation and historical comparison). E-0xx are this session's own checks.

- **E-001 | `ls docs/ephemeral`** | 222 HDE-CRD-0002 files; none named `QA10` or `readiness` before this audit (N-001).
- **E-002 | the decision line of each accepting record:**
  - lineage reviews: WU-PR-01 v2.0, WU-PR-02 v2.0, WU-PR-03 to WU-PR-08 v1.0, WU-DOC-01 v2.0 and v3.0 all `decision: ACCEPT`;
  - `…-WU-DOC-01-documentation-completion-v1.1.md` `result: COMPLETE`;
  - `…-WU-OPS-01-ops-task-receipt-v1.0.md` `decision: ACCEPT`;
  - AQ-1 "Approve with changes" (`…-PF10-build-notes-addendum-aq1-adr-v1.0.md:5`).
- **E-003 | GitHub Actions, workflow `ci.yml`, push runs on `main`:**
  - Every push run from `7136040` (#627) to `04645f4` (#704) concluded `success`.
  - Run 39699657729 on `1a4c8ab` (job 119565525679; full log, 919 lines) read: `CI_CHANGE_CLASSIFICATION:event=push;reason=selected_lanes;paths=6;lanes=product,compat,db,rails,evidence,qa,release`.
  - Its counts: changed tests "4521 passed, 2 skipped"; product 77; compat "119 passed, 3 skipped, 2 xfailed"; db 269; rails 120, 113, 155, 138; evidence 134; qa 488; release 79; every outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **E-004 | `git diff --stat 1a4c8ab 39122b7` outside `docs/ephemeral/` and `docs/pfcanon/`:**
  - Only Markdown documentation changed (AGENTS.md, CHANGELOG.md, README.md, docs/ADAPTER_009.md, docs/CLI_commands.md, docs/EVIDENCE_INDEX.md, docs/RUN.md, docs/acceptance/reader_a7_crib.md, docs/contracts/reader_v2_public_bytes.md, docs/qa_harness_pattern.md), plus the six `audit/ops/hde-crd-0002/wu-ops-01/` files.
  - So the code at `39122b7` is the code run 39699657729 tested.
  - Push run 39962751831 on `04645f4` ran only the evidence lane: `success`.

## 2. Top-level Repo Map

- **E-101 | file count** | 8194 tracked files.
- **E-102 | 40 tracked roots, with file counts:**
  - .audit_src/ 485, .backup_epic004/ 6, .claude/ 9, .devcontainer/ 3, .github/ 3, .vscode/ 1;
  - _arch/ 147, _archive/ 29, adapter/ 17, artifacts/ 1026, audit/ 3127, catalog/ 25, ci/ 14, codex/ 37, config/ 2, dev/ 2;
  - docs/ 2456, engine/ 102, errors/ 10, fixtures/ 17, freeze/ 1, goldens/ 26, handoff/ 49, internal/ 5, math/ 1, migrations/ 3;
  - narratives/ 10, notes/ 21, parity/ 17, presenter/ 4, proofs/ 6, release/ 1, reports/ 2, scan_reports/ 2, schemas/ 47, scripts/ 66, sql/ 1;
  - tests/ 255, tools/ 100, validation/ 2.
- **E-103 | new root `.claude/`** | 9 files: `hooks/check_canon_relied_on.py`, `settings.json` and 7 `*.skill` files, four of them named with " (1)". The classifier's `_FULL_VALIDATION_PREFIXES` includes `.claude/` (`ci/checks/classify_ci_changes.py:28`).
- **E-104 | `dev/`** | holds `dev/.env.codex` and `dev/__init__.py` only; `dev/reader_harness` was deleted in `c98d41f` (#643).
- **E-105 | 57 root files:**
  - project docs;
  - 14 HDE-EPIC023 step reports;
  - build and run files: pyproject.toml, Procfile, requirements*.txt, pytest.ini, run_flask*.{py,sh}, run_d3_2_*.sh, VERIFY.sh, card_close.sh, .env.example, CANON_CHECKSUMS.json;
  - scratch files: big.json, patch.diff, changes_report.txt, manifest_pre.sha256, manifest_post.sha256, .tmp_refusal_{get,post}.txt, temp_run.{ec,err,out}, .body200.json, .code304.txt, code304_new.txt.
- **E-106 | zero-byte root files** | Run, assert, import, temp_run.err, temp_run.out.
- **E-107 | em-dash path** | one tracked path contains an em-dash: `docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md`.
- **E-108 | `docs/` second level:**
  - ephemeral 2208, graph 58, pfcanon 34, prompt_ecosystem_management 32, schemas 20, evidence 9, plans 8, design 8, run 6, adr 5, crd 3, qa 2, contracts 2, changes 2, architecture 2, acceptance 2, server 1, ops 1;
  - plus 53 files directly under `docs/`.
- **E-109 | evidence homes** | artifacts/ 1026, audit/ 3127, docs/evidence/ 9, goldens/ 26; `_HISTORICAL_PREFIXES` at `classify_ci_changes.py:156`.

## 3. Packaging and Entrypoints

- **E-110 | `pyproject.toml:6-22`:**
  - name "glow-hdengine", version "0.0.0", requires-python ">=3.10", `dependencies = []`;
  - `[project.scripts] hdctl = "engine.cli.main:cli"` only;
  - packages engine*, adapter*, presenter*, catalog*, math*; package-data catalog and math `*.json`;
  - build-system setuptools>=68, wheel.
- **E-111 | requirements:**
  - `requirements.txt`: psycopg[binary]>=3.1,<3.3; Flask>=2.3,<3.0; gunicorn>=21,<22; jsonschema==4.23.0.
  - `requirements-dev.txt`: jsonschema, pytest>=7.4,<9.0, pytest-cov, pytest-mock.
- **E-112 | `Procfile:1`** | `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30`.
- **E-113 | three factories and their callers:**
  - Factories: `adapter/factory.py:11`, `adapter/wsgi.py:11` (module app :73), `adapter/http_reader.py:1248` (module app :1313; `__main__` loopback run :1315-1325).
  - Callers: run_flask.py:22/35, run_flask_dev.sh:21, scripts/start_web.sh:4, scripts/scratch.py:4-5, adapter/app.py:2,5 (the wsgi alias), tools/evidence/generate_a7_transport_proofs.py:24.
  - `python -m adapter.http_reader` is run by scripts/dev_start_reader.sh:26 and scripts/qa/dev_sampler_healthcheck.py:133.
- **E-114 | extra hdctl copies** | scripts/hdctl.py, hdctl.clean.py, hdctl.backup.py, hdctl.py.bak, plus copies under .audit_src/scripts/.
- **E-435, E-436 | packaging covers 29 of 45 release members:**
  - packages.find and package-data cover 29 of the 45 release members by a static estimate; no wheel was built.
  - Not covered: `adapter/schemas/error_v1.schema.json`, `catalog/narratives/*.json` (5), `errors/token_map/token_map.json`, `migrations/005_identity.sql`, `schemas/*.json` (7), `tools/bodygraph/check_magic10_gate_readiness.py`.
  - README.md:138 states this limit ("omits 16 of the 45").
- **N-101 | no build file at the root** | no Dockerfile*, setup.py or setup.cfg at the root, and no Dockerfile anywhere in the working tree.

## 4. Engine Modules

Fully inspected:
- the admission block of `engine/config/registry_loader.py`;
- `engine/core/core.py` `compute_core`;
- `engine/compat/compute.py` `evaluate_pair`;
- `engine/runtime/identity.py`.

The rest is sampled.

- **E-201 | `engine/` subpackages** | bodygraph canon categories charts cli compat compliance config core db errors http magic10 mech narratives ops order presenter presets provider providers runtime sampler serializer stable testsupport util validation. `engine/core/` holds `__init__.py` and `core.py`.
- **E-202 to E-205 | admission (`registry_loader.py`):**
  - :398-400 `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"`, `ADMITTED_RELEASE_ROSTER`;
  - :448-449 import-time `len != 45` → `ADMITTED_RELEASE_ROSTER_INVALID`;
  - :1219-1241 `_validate_admitted_manifest` (INCOMPLETE_RELEASE_ROSTER, RELEASE_ROSTER_MISMATCH, RELEASE_VERSION_MISMATCH, RELEASE_TIMESTAMP_MISMATCH);
  - :1506-1511 `load_active_mechanics_bundle()` "Admit the exact installed complete mechanics release, or fail closed".
- **E-206, E-308 | manifest matches roster** | manifest paths equal the roster literal (45, symmetric difference empty); all 45 member sha256/size values match the tree.
- **E-209 to E-211 | `compute_core`:**
  - `core.py:209-238` `compute_core(member_a, member_b, mechanics_bundle, release_id) -> CoreResult` imports types and constants only.
  - Callers: `engine/compat/compute.py:346`, `tools/config/artifacts.py:645-647`, `tools/evidence/generate_engine_core_evidence.py:120-123`.
- **E-212 | process state in `engine/compat/compute.py`** | `_BUNDLE_PROVIDER` is a rebindable module global (:50); `_SCHEMA_VALIDATORS` is a process dict (:52); evaluate_pair requires `type(bundle) is AdmittedMechanicsBundle` (:331); intrinsic cache key prefix `magic10:v1:` (:44, :336).
- **E-213 | identity** | `engine/runtime/identity.py:130-139` computes the identity once at import, with `release_id` = sha256 of the packaged manifest.
- **N-201 to N-203 | no I/O, environment or cache in the pure core:**
  - no I/O import in `engine/core` or `engine/magic10`;
  - no `os.environ`/`getenv` there;
  - no `lru_cache`/`functools.cache` in the admission and presenter paths.

## 5. Adapter / HTTP Surfaces

- **E-214, E-215 | production app** | Procfile runs `adapter.factory`, which mounts `bp` at "", `api_bp` at `/api` and the compat blueprint.
- **E-216 to E-219 | `adapter.factory` error handling:**
  - app-level `errorhandler(404)` returns the governed `ERR_NOT_FOUND` envelope with `no-store` and no ETag, for every path ("An unknown path, compat or not, answers the governed envelope", :30-33);
  - `errorhandler(405)` gives the same envelope; compat keeps Flask's Allow, other paths a sorted Allow (:35-41);
  - after_request converts a compat HTML 404/405 and strips ETag on `/internal/` (:43-56).
- **E-220, E-221 | `adapter.http_reader.create_app`:**
  - mounts the same three blueprints; its 404 and 405 handlers return the compat envelope on `/api/compat/v1`, otherwise `_governed_error_response` (`ERR_NOT_FOUND`, no-store).
  - Its after_request reads `getattr(resp, "request", None)` and so never fires (unchanged since HDE Build Notes 2.7 AD-4 item 4).
- **E-222 | `adapter.wsgi`** | the same mounts; `no-store` default; HSTS for prod-like `APP_ENV`/`ENGINE_ENV`; `GET /internal/healthz` and `GET /internal/readyz` (always 200 `{"ok":true,"schema":"v1"}`); global 404/405 JSON `ERR_NOT_FOUND`, and the 405 has no Allow.
- **E-223 to E-225 | production Reader routes:**
  - `api_bp` `POST /reader` → `_production_reader_response`;
  - GET/HEAD/OPTIONS/PUT/PATCH/DELETE → governed 405 with `Allow: POST`;
  - unrouted methods get the same 405 through `bp.record(_refuse_unrouted_methods)`.
- **E-226, E-227 | dev `GET /reader` gate:**
  - `_reader_dev_env_explicit()` returns `os.environ.get("APP_ENV") == "dev"` (`http_reader.py:383-389`): exact, no trim or case-fold.
  - Version validation runs first; refusal is `ERR_READER_FORBIDDEN` 403, no-store.
- **E-232, E-233 | dev writers** | `_dev_admin_gate` is `APP_ENV in {"dev","test","local"}`, exact (`:901-907`); it applies to `POST /internal/dev/sampler` and the three `/dev/*/conjunction` routes.
- **E-238 | production posture (S19):**
  - Under `_compute_env_mode(os.environ) == "prod"`, `_mount_for_production` (`:560-625`, registered at :1155) answers the canon-retired `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` as unknown paths (`ERR_NOT_FOUND` 404).
  - It refuses dev `/reader` (403) and the dev writers (403) before their handlers run.
- **E-236, E-237 | internal routes:**
  - `/internal/version` GET/HEAD: `X-Identity-Override` → 400; otherwise `identity_admin()`, no-store, no ETag.
  - `/ops/writer/diagnostic` needs a bearer admin scope.
- **E-229, N-210 | Aux narrative** | `/api/aux/narrative` and `/aux/narrative` share a view that reaches no vendor and no resolver.
- **E-240 to E-244 | compat blueprint:**
  - `/api/compat/v1`; in a prod posture every compat path returns 404 (:108-120).
  - GET with a non-empty body → `error_envelope("invalid_json")` → `ERR_COMPAT_INVALID_JSON` 400 (:122-128; `engine/compat/error_tokens.py:9-11`).
  - POST, HEAD and OPTIONS are also registered.
- **E-245 | unknown person** | the production Reader's unknown person is `ERR_M10_PERSON_UNRESOLVED` 404 (`http_reader.py:521`; `error_tokens.py:134`).
- **E-246, E-457, E-310 | endpoint catalog:**
  - `docs/ENDPOINTS_CATALOG.json` is a symlink to `../artifacts/audit/ENDPOINTS_CATALOG.json` (byte-identical; sha256 85453d93…2885, matching both sidecars).
  - It has 18 rows. Since `142e56f` it changed in `c98d41f` and `2f3db0a`.
- **Route enumeration (static, from decorators)** | 53 served (method, path) pairs across the three factories, split into 18 catalog rows and 35 reasoned exclusions (7 governed refusals, 1 alias, 18 framework-implicit, 9 canon-retired). The production factory serves 47; it lacks healthz/readyz. The exclusion table is `tests/http/test_endpoint_catalog.py:103-139`.
- **E-235 | dead fallback** | the module-level `except NameError` fallback for `bp` (:1168-1172) can never execute, because `bp` is bound at :1158.
- **N-207 | no aborts** | no `abort(` in adapter, engine/http, presenter or engine/runtime.

## 6. Presenter / Emitter

- **E-248 | shared emitter** | `engine/presenter/emitter.py:6-28`: `emit_public(envelope, *, sort_keys=True) -> bytes`; `emit_public_with_envelope(...) -> Tuple[bytes, Dict]`; `emit_compact_json` is its alias.
- **E-249, E-250 | serializer** | `engine/serializer/canon.py` `sercanon` → `engine/stable/sercanon.py:21-29`: `json.dumps(ensure_ascii=False, separators=compact, sort_keys=…)`, exactly one LF, UTF-8. `dumps = sercanon` is an alias.
- **E-251, E-252 | Reader v1 presenter** | `presenter/reader_v1/emitter.py`:
  - category items are exactly {id, band} with band in {Cool, Open, Warm, Glow};
  - a duplicate id raises ValueError (:41);
  - v2 ids equal `FROZEN_MAGIC10_ORDER` when eligible, `[]` otherwise;
  - `_emit` hashes the five-key preimage into `idempotence_hash`.
- **E-253 | runtime dispatch** | `engine/runtime/public.py`: v1 is harmony-only; v1/v2 dispatch; `reader_version_unsupported` otherwise.
- **N-204 | no `allow_nan`** in engine/stable or engine/serializer.

## 7. CLI Surfaces

- **E-254, E-255 | entry point** | the sole console script `hdctl` → `engine.cli.main:cli`; `add_subparsers(required=True)` (:91).
- **E-256, E-463 | showcompat** | help: "Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader" (:92-96). Stdout is that document plus one LF (:827-829).
- **E-257 to E-260 | subcommands and their options:**
  - showcompat (:97-138);
  - aux-preview (:140-151);
  - bg:resolve (:152-184, including `--allow-prod-vendor` AUTHORIZATION_REF);
  - dev:sampler (:186-203; `APP_ENV not in ("dev","test","local")` → DEV_ADMIN_ONLY, :833-837).
- **E-261, E-262 | exit codes** (:284-327):
  - `--version` → 0; usage → 64; CliError → its code (default 64);
  - typed boundary, vendor and registry errors → 1; anything else → `CLI_UNEXPECTED` 1.
  - An `--allow-prod-vendor` pre-scan runs before argparse.
- **E-263 to E-265 | stdout writes:**
  - bg:resolve writes with `sys.stdout.write` (:279-280);
  - showcompat and conjunction go through `_emit_stdout_bytes`, which raises STDOUT_MISSING_LF/STDOUT_CRLF (:570-575).
- **E-266 | aux-preview `--band`** | with `--pair-file`, the band read from the file row is replaced by an explicit `--band` (:616-618). A missing category still refuses first.
- **E-268 to E-270 | tool CLIs:**
  - `tools/config/generate_config_artifacts.py --compare-goldens` (0/1/5);
  - `tools/bodygraph/check_magic10_gate_readiness.py`;
  - `tools/evidence/update_evidence_index.py` (`--check` → `_run_once(check=True)`).
- **E-135, E-136 | pre-push check** | `tools/ci/prepush_check.py`:
  - reports `lanes`, `membership`, `build-notes`, `sweep`, `replay` and `all`;
  - `--path docs/ADAPTER_009.md lanes membership build-notes` gave rc 0, `documentation_only`, release 1.3.0 roster 45 `release_id` 77204764…, build-notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.5.md` sha256 2759c4da…e167;
  - it ended "repository unchanged", and the tree was clean afterwards.
- **E-138, E-139 | pre-push check internals** | its replay pin `REPLAY_WORKFLOW_SHA256` equals the sha256 of `ci.yml`. Its throwaway copy is a `git clone --shared` (`:365-382`).

## 8. Vendor Seam & BodyGraph Storage

Configuration names only; no values were inspected.

- **E-271, E-272 | vendor client** | `engine/bodygraph/vendor_client.py`:
  - reads `HD_API_BASE_URL`/`HDAPI_BASE_URL` (a conflict → PROVIDER_CONFIG_INVALID), requires https, and names `HD_API_KEY` and `GEO_API_KEY`;
  - refuses unless `SAFE_MODE=0` and `ALLOW_NETWORK=1`; no-redirect opener.
- **E-273 | database** | `engine/db/adapter.py`: the retired bridge keys are refused before provider construction; the DSN comes from `DATABASE_URL` only; `PsycopgProvider`.
- **E-274 | mapped cache** | `engine/bodygraph/mapped_cache.py`: posture `adapter_mapped_no_raw_vendor_payload`; persist and read-current functions.
- **E-275 to E-277 | production-override audit** | `engine/bodygraph/vendor_audit.py`:
  - `vendor_prod_override.v1`, a 16-key event;
  - sink: `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, else `$XDG_STATE_HOME`, else `~/.local/state`; a sink in the repository or a relative sink is refused;
  - actor = effective-UID account name;
  - O_APPEND 0600 with fsync of the file and its directories; any failure → AuditUnavailable.
- **E-278 to E-286 | resolver production override** | `engine/bodygraph/resolver.py`:
  - environment classification (:65-103), with production {prod, production, live} and non-production {dev, test, local, stage, staging}; unknown, conflicting or absent → PROVIDER_CONFIG_INVALID; never downgraded;
  - closed rails refuse first (:242-261);
  - the matrix (:268-299); the allowed event before any outbound call (:300-322); the state event after it (:324-331, :354-390);
  - production write refusal on both paths (:466-470, :529-533);
  - refusal envelope `outbound_attempted: false`, exit 1.
- **E-287, E-288 | public paths stay local** | the production Reader, dev `/reader` and compat call `resolve_compat_chart(source_policy="local", env=None)` (closed-rails env), which never acquires.
- **E-289, N-208, E-290 | showcompat and conjunction vendor path** | showcompat `--source vendor` and conjunction vendor acquisition (`_acquire_dry_run`, :915-1031) apply generic rails only, with no environment classification or override gate. The dev conjunction routes call it behind `_dev_admin_gate` and the production-posture refusal.

## 9. Evidence, Indices, Catalogs

**Read-only validators** were run in the throwaway clone under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`, with exit codes captured as `out=$(cmd); rc=$?`. The tree was clean after each.

| ID | Command | Result |
| :- | :- | :- |
| E-141 | `python3 tools/evidence/update_evidence_index.py --check` | rc 1: env-pins line, then `ModuleNotFoundError: No module named 'flask'` via `_validate_epic038_pr02_semantics` → `generate_a7_transport_proofs.py:24` → `adapter/http_reader.py:6`. An environment limit; result Unknown here |
| E-142 | `python3 tools/evidence/orientation_demo.py --check` | rc 0 |
| E-143 | `python3 tools/evidence/validate_evidence_paths.py` | rc 0 |
| E-144 | `./ci/checks/check_mirror_schema.sh` | rc 0 (a Python script with a `.sh` name) |
| E-145 | `python3 scripts/release_id_recompute.py --check-manifest-only` | rc 0 |
| E-146 | `python3 tools/evidence/run_canonical_json_gate.py --check-only` | rc 1, the same Flask import (`run_canonical_json_gate.py:31`). An environment limit; result Unknown here |

Hosted CI ran the full evidence lane, including `update_evidence_index.py --check`, with `success`:
- on `1a4c8ab` (E-003);
- on `04645f4` (run 39962751831, evidence lane only).

**Index, Mirror and orientation:**
- **E-301 to E-304 | sizes and sentinels:**
  - Human Index `docs/evidence/INDEX.json` has 620 rows; its sha256 matches `INDEX.sha256`.
  - Mirror `artifacts/evidence_index.jsonl` has 620 lines; it matches its sentinel and has the same key set.
  - `audit/gates/topology/orientation_demo.txt` reads `total_artifacts: 620`, `status: ok`.
  - Every Mirror path exists; the only sha mismatch is the expected self-record.
- **E-305 | last Index change** | `docs/evidence/INDEX.json` last changed in `822ce15` (#656).

**Release identity:**
- **E-306, E-434 | manifest** | `catalog/manifest.json`: version 1.3.0, built 2026-08-24T18:04:49Z, 45 files, canonical bytes; sha256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` = `release_id`.
- **E-307 | same-version refreshes** | in `2f3db0a`, `5892538` and `822ce15`; each changed only member digests.

**Index rows by change:**
- **E-311 | rows by tag** | no Index row carries `crd_id`; 16 rows are tagged HDE-EPIC040; 11 are HDE-CRD-0001 rows.
- **E-312, N-302 | no HDE-CRD-0002 QA root** | `audit/qa/hde-crd-0002/` does not exist.
- **N-301 | no HDE-CRD-0002 rows** | no Index or Mirror row mentions `crd-0002`.

**Current-release labels (S12):**
- **E-321 | label logic** | `tools/evidence/update_evidence_index.py:56-88, 3817-3930`: `CURRENT_RELEASE_CAPTURE_PATHS` (22 paths); labels are derived from the manifest.
- **E-322, N-305 | labelled rows** | all 27 labelled Mirror rows over those 22 paths read `current-release capture: release 1.3.0, release_id 77204764…`. No other row carries the label.

**CRD admission (S22):**
- **E-326 | admission table** | `update_evidence_index.py:48-54` `ADMITTED_CRD_QA` = {HDE-CRD-0001: (`audit/qa/hde-crd-0001`, `audit.qa.hde_crd_0001`), HDE-CRD-0002: (`audit/qa/hde-crd-0002`, `audit.qa.hde_crd_0002`)}.
- **E-326 | loading and refusal** | `_load_crd_qa_entries` (3947-4005) skips an absent root. `publish_crd_check_family` refuses an unadmitted ID.
- **E-328 | the absent-root test** | `tests/evidence/test_evidence_index_missing_state.py:977-983` `test_absent_admitted_crd_root_publishes_nothing` asserts, with no condition:
  - `not (ROOT / "audit/qa/hde-crd-0002").exists()`;
  - no `_load_crd_qa_entries` current row for `hde-crd-0002`;
  - no Index row under `audit/qa/hde-crd-0002`.
- **E-005 | the test runs in the evidence lane** | `.github/workflows/ci.yml:221-240`, step "Run governed evidence integrity lane", runs `python -m pytest -q tests/evidence/test_evidence_index_missing_state.py …`.
- **E-005 | QA evidence selects that lane** | `classify_paths(['audit/qa/hde-crd-0002/checks/x/primary.log', 'audit/qa/hde-crd-0002/qa_step_logs_manifest.json', 'docs/evidence/INDEX.json'])` returns `reason='selected_lanes'` with `evidence: True` and `release: True`. Run by this session in the checkout; the transient `__pycache__` was removed and the tree verified clean.
- **E-006 | where the test came from:**
  - WU-PR-02 PR plan v1.0 §8.4 specifies it: "on the real checkout, `audit/qa/hde-crd-0002/` is absent, `_load_crd_qa_entries([])` yields no HDE-CRD-0002 row and the Index has none".
  - Plan v1.1 §7 WU-PR-02 acceptance (5) reads "the absent real root publishes nothing".
  - Lineage review v1.0 `…-WU-PR-02-pr-work-unit-lineage-review-v1.0.md:134` marks it MET.
  - A search of `docs/ephemeral/` and `docs/pfcanon/` for the test name, "absent real root" and `absent_admitted` finds only these WU-PR-02 and Plan records (N-002). None of them says how the test behaves once QA creates the root.

**Close pack and close-run family (S21):**
- **E-329 to E-336 | the v2 writer** | `tools/qa/generate_epic_close_pack.py`:
  - `CHANGE_RE` accepts `HDE-EPIC[0-9]{3}` or `HDE-CRD-[0-9]{4,}`;
  - CRD outputs are `audit/HDE-CRD-NNNN_close_report.md` and `_MANIFEST.json`;
  - exactly one `--source` and one of `--write`/`--check`, with closed rails first;
  - the manifest is installed last, then read back;
  - its source schema is `schemas/close_candidate_source.v2.json`;
  - typed refusals: REQUIREMENTS_SOURCE_NOT_CURRENT, CLOSURE_OVERRIDE_INVALID, QA_LEDGER_INVALID and others.
- **E-334, E-335 | the close-run family:**
  - `publish_crd_close_run_family` covers `audit/qa/<crd>/close/<check_id>/primary.log` only;
  - it writes neither the QA manifest nor `checks/` (test at :1317-1385).
- **E-337 to E-339 | the ADR:**
  - `docs/adr/hde/close_pack_writer_adr.md:3` reads "Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15 …)".
  - Its "Stated limits" still carry "and `SATISFIED` needs every recorded status to be `PASS`", the clause addendum 2.17 Resolution A supersedes.
- **N-303 | nothing produced yet** | no CRD close pack, v2 candidate source or close-run directory exists.

**Ops evidence:**
- **E-313, E-314 | WU-OPS-01** | `audit/ops/hde-crd-0002/wu-ops-01/` holds six files; SHA256SUMS.attempt1 5 of 5 OK (recomputed); result PASS, exit 0; identity read HTTP 200 MATCH, `release_id` 77204764…; seven variables SET (presence only). The files are not in the Index or Mirror (N-301).
- **E-343, N-307 | HDE-EPIC040 OPS01** | `audit/ops/hde-epic040/ops01/SHA256SUMS` 7 of 7 OK; still not in the Mirror.

**Other governed files:**
- **E-344 | goldens and frozen records** | goldens/ 26; the `artifacts/cards/a3/IDENTITY_OK.txt` family is present; `artifacts/release_id.txt` is the frozen EPIC022 record.

**PF10 itself:**
- **E-451, E-452, E-345 | PF10 v13.7.5 (454,052 bytes, sha256 2759c4da…e167):**
  - the Addendum Index lists 2.1 to 2.22, exactly the body's headings;
  - no mid-word truncation;
  - the file ends with the authored `\<eof\>` marker and has no final LF.

## 10. Tests, QA Harness, CI/Checks

**Test files:**
- **E-116, E-117 | tests and pytest.ini** | `tests/` has 255 tracked files, 215 `test_*.py`. `pytest.ini` testpaths has 80 entries and still omits `tests/order` and `tests/http` (N-110).
- **E-118, N-103 | conftest** | `tests/conftest.py` only adjusts `sys.path`.

**Workflows:**
- **E-119, E-120 | `.github/workflows/ci.yml` (420 lines):**
  - `pull_request` and `push` to `main` use a `paths:` filter: `**`, each of the 8 `_DOCUMENTATION_PREFIXES` negated, then `**.path_proof.txt`, `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json` re-included.
  - One `test` job: exact-head checkout, classification, Python 3.12, changed tests in an isolated worktree, seven lanes, and the final `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (:420).
  - N-105: there is no `paths-ignore`.
- **E-121 | `epic-closeout-validation.yml`** | `workflow_dispatch` only, `contents: read`.

**Classifier** (`ci/checks/classify_ci_changes.py`, 2092 lines):
- **E-122 | constants:**
  - LANES: product, compat, db, rails, evidence, qa, release;
  - `_FULL_VALIDATION_PATHS` has 7 entries, including the classifier itself;
  - `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` has 109;
  - `_FULL_VALIDATION_INACTIVE_TESTS` is empty;
  - `_DOCUMENTATION_PREFIXES` has 8 entries;
  - `_DOCUMENT_PATHS` has 7, including `.env.example`.
- **E-123 | owner registries** | `_registered_owner_test_paths()` holds 207 paths, all on disk; `_full_validation_test_targets()` 166; `_UNKNOWN_SOURCE_SUFFIXES` {.py, .sh, .sql}.
- **E-124 | unregistered sources** | an unregistered `tools/qa` source raises `CI_QA_OWNER_TEST_MISSING`, and an unknown source raises `CI_SOURCE_OWNER_TEST_MISSING`. In CI either one becomes `CI_CHANGE_CLASSIFIER_ERROR`, exit 2.
- **E-131 | hypothetical new `tools/qa` sources** | new `tools/qa/new_unregistered_tool.{py,sh,sql}` and a nested `.sh`: `changed_test_targets` raises `CI_QA_OWNER_TEST_MISSING` (pure path logic, run in the clone).

**Coverage of every test file (S03):**
- **E-126, N-106, N-107 | coverage computed in the clone:**
  - of 215 tracked `test_*.py`, 49 are reached by `ci.yml` tokens and 166 by full-validation targets;
  - none is uncovered, and every file selects at least one lane.
- **E-127, E-128, N-108 | retirement ledger:**
  - `tests/retired_tests.md` has 66 rows, each with a reason and the date 2026-10-13, and none of the 66 paths is still tracked;
  - the recorded baseline failure O-P06a-03 (`tests/reader_v1/test_cli_proof.py`) is retired with its reason.
- **E-129 | the guard tests:**
  - `tests/evidence/test_rails_ci_workflow_integration.py:2127-2141` asserts the uncovered list is `[]`;
  - `tests/tools/test_prepush_check.py:596-610` asserts the same.
- **E-130 | recorded sweep (not re-executed)** | WU-PR-06 result v1.9:84 records a full sweep "5,231 passed, 3 skipped, 2 xfailed, 0 failed".

**Other guard tests:**
- **E-132 (S04)** | `tests/evidence/test_rails_ci_workflow_integration.py:852-891` pins the `tools/qa` owner refusal for .py, .sh and .sql in both cases.
- **E-133, E-134, N-109 (S05)** | `test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths` (:2076-2112) pins filter equality. Replayed over all 8194 tracked paths: 0 disagreements between the filter and the classifier.
- **E-140 (S20)** | `tests/tools/test_prepush_check.py` (1070 lines, 36 tests) covers read-only behaviour, lane equality, classifier-in-copy, a single build-notes file, dirty-tree refusal, the closed-rails child environment, and the synthetic sweep and replay.

**QA harness:**
- **E-125 | statuses and CRD IDs** | `tools/qa/qa_harness.py`: statuses PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, PARKED; `CRD_RE` `HDE-CRD-[0-9]{4,}`.
- **E-467 | identity rule** | "exactly one of epic_id or crd_id is required".

**Recorded hosted failures (not re-executed):**
- **E-007 | WU-PR-08 run 39695867041 on `e1cb6d1`** | lineage review v1.0:128 records a failure: 1 failed, 4,520 passed, 2 skipped, at `tests/tools/test_prepush_check.py::test_build_notes_requires_exactly_one_file[names2-False]`, attributed to a git auto-maintenance race (PR35-C1). The same code passed on `bf32d20` and `d37090e`.

### 10.1 Documentation evidence (E-4xx)

**Environment template (S16):**
- **E-401, E-402 | `.env.example:1-4`** | `HD_API_BASE_URL=https://api.example.invalid`, `HD_API_KEY=changeme`, `HD_API_SECRET=changeme`, `GEO_API_KEY=changeme`; registered in `_DOCUMENT_PATHS` (`classify_ci_changes.py:185`).

**Readiness and ports (S17):**
- **E-403 to E-406 | which app serves readyz:**
  - `/internal/readyz` is registered only by `adapter/wsgi.py:47-51` (200 `{"ok":true,"schema":"v1"}`, unconditional);
  - `adapter/app.py` aliases wsgi;
  - `adapter.factory` and `adapter.http_reader` do not register it.
- **E-410 to E-413 | bindings in the code** | Procfile binds `0.0.0.0:$PORT`; `scripts/start_web.sh` `${PORT:-8000}`; `scripts/dev_start_reader.sh` `PORT:=8000`, host 127.0.0.1; the `http_reader` `__main__` runs on 127.0.0.1 at `PORT` (default 8000).
- **E-414 to E-417 | what `docs/ADAPTER_009.md` says:**
  - :6 and :43-44 describe readyz as implemented, unconditional, and served only by `adapter.wsgi`;
  - :115 and :135 give loopback `127.0.0.1:8000` on `$PORT`;
  - :141-147 quote the Procfile line byte for byte.

**Compat GET error code and architecture (S18):**
- **E-418, E-419 | `invalid_json`** | `docs/ADAPTER_009.md:171` "Compat GET with body ⇒ 400 … built from the `invalid_json` alias (emitted `code`: `ERR_COMPAT_INVALID_JSON`)". This matches `compat_handler.py:122-126` and `error_tokens.py:9-11`.
- **E-420 to E-423 | ARCHITECTURE.md:**
  - :9 and :24 give `emit_public(...) -> bytes`, matching `engine/presenter/emitter.py:6`;
  - :29-32 describe the three factories' mounts, matching `factory.py:13-15`, `wsgi.py:23-25`, `http_reader.py:1252-1261` and `compat_handler.py:19`.

**`/internal/version` (the stale text in RA2-23):**
- **E-427 | auth and override** | `http_reader.py:1175-1196`: `/internal/version` reads no Authorization; `X-Identity-Override` → 400 in every environment.
- **E-428 | six keys** | `engine/runtime/identity.py:26-33`: `_FIELDS` are engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id. This matches `docs/ADAPTER_009.md:15`.
- **E-429 to E-431 | stale lines in `docs/ADAPTER_009.md`:**
  - :189-193 and :223 list a five-key body;
  - :49 is the single word "New";
  - :209 reads "**Override (prod):**".

**WU-DOC-01 statements:**
- **E-432 to E-445 | 17 statements checked** | Each statement WU-DOC-01 delivered and the worker checked matches the code: README.md:13, :18, :137, :138, :254; AGENTS.md:143; CHANGELOG.md:7, :8, :10, :14, :19; docs/EVIDENCE_INDEX.md:62, :64; docs/CLI_commands.md:3, :19, :23, :29; docs/server/reader_v1.md:17, :20; docs/ADAPTER_009.md:47, :48; docs/qa_harness_pattern.md:14, :97.
- **E-453 to E-456 | LR8-F2 and LR8-O1** | Every item addendum 2.21 routed to WU-DOC-01 is resolved in the documents:
  - `/internal/version` listed once;
  - no "localhost";
  - the ENGINE_ENV line corrected;
  - the Procfile start line;
  - `APP_ENV=dev` in the capture environment;
  - no X-Toggles-SHA;
  - the `rel_dev` default explained;
  - no Bearer on `/internal/version`;
  - the documentation side of `artifacts/release_id.txt` stated at README.md:137.

**Other documents and canon:**
- **E-447, E-448 | `check_mirror_schema.sh`** | `ci/checks/check_mirror_schema.sh` is `#!/usr/bin/env python3` (mode 100755) and CI runs it directly. AGENTS.md has no bash or sh invocation of it.
- **E-449, E-450 | root hygiene** | the zero-byte and scratch root files are listed in E-105 and E-106; `catalog/channels_catalog_v1.json` is a placeholder no `.py` references; `pytest.ini` testpaths has 80 entries.
- **E-458, E-459 | counts** | Index 620 rows, Mirror 620 lines, `INDEX.sha256` match; root counts as E-102.
- **E-460 | `compute_core` call site** | `engine/compat/compute.py:20, 346` is the only caller in the request paths.
- **E-461 | non-BodyGraph loader** | `engine/charts/loader.py:54, 71, 95, 168` reads `SAFE_MODE`, writes `loader_call.jsonl` and uses `perf_counter`.
- **E-462 | CRD QA roots** | `audit/qa/hde-crd-0001` has 23 tracked files; `audit/qa/hde-crd-0002` does not exist.
- **E-464 to E-467 | earlier-finding comparison points:**
  - `presenter/reader_v1/emitter.py:5, 41`;
  - `[project.scripts]` lists hdctl only;
  - `engine/db/adapter.py:83` `DBAccess`;
  - `tools/qa/step_log_header.py`;
  - `qa_harness.py:64-68`.
- **E-468 | HDE-EPIC040 deferrals** | `docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-v1.1.md:222`: live Gate readiness and live DB Reader success were "not run".
- **E-469, E-470 | C040 drainage:**
  - PF04 v2.8.7, PF05 v2.5.3, PF12 v2.9.6 and PF09.3 now carry C040-06/07/08 content;
  - PF10 v13.7.5 has no C040 entry;
  - `docs/contracts/reader_v2_public_bytes.md:8` still says C040-07 is not drained into PF04 or PF12.
- **E-471, E-472 | canon presence:**
  - PF10 2.3 deprecates the Codex security review;
  - `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` exists;
  - the PF19 v3.0.6 §10.8 heading is present.
- **E-473 | ARCHITECTURE.md:36** | "any JSON body → 400" is narrower wording than the code's `if request.data`; there is no contradiction.

**Engine-core and S19 code security review:**
- **E-315 to E-325, E-340, E-341 | per-requirement detail** | recorded in the triage's coverage map with the same IDs:
  - the S06 compat shim and its tests;
  - the S11 drift test;
  - the S12 label logic;
  - the S13 root-bound probe;
  - the S19 record and the presence on `main` of fixes F01 to F09.

## 11. Flows & Call Chains

| Family | Status | Chain |
| :- | :- | :- |
| Reader HTTP v1/v2 | Found | factory.py:14 `/api` → http_reader.py:641 `reader_post` → `_production_reader_response` :525 → `_select_reader_version(("1","2"))` :392 → `_parse_reader_post_body` :477 (32 KiB) → `_reader_current_rows` :508 → `DBAccess.for_current_env` → `read_current_mapped_bodygraph` → `resolve_compat_chart(source_policy="local")` → `_evaluate_reader_pair` :457 → `evaluate_pair` compute.py:307 → `compute_core` :346 → `emit_reader_public_bytes` (public.py:112) → `emit_reader_v1/v2` → `emit_public`; failures `_reader_failure` :437 → `_error` :370 |
| Compat HTTP | Found | compat_handler.py:108 guard (prod → 404) → POST :130 → stored party or `resolve_compat_chart` :168 → `evaluate_pair` → `_writer_payload` :28; GET with body → `invalid_json` 400 |
| CLI showcompat | Found | `cli` main.py:284 → `showcompat` :666 → source or files :738/:763 → `_resolve_party` :390 → `evaluate_pair` :807 → `_emit_stdout_bytes(emit_public(result))` :829; conjunction :707 → `conjunction_public_resolved` compute.py:430 → `resolve_compat_chart` ×2 → `_emit_stdout_bytes` :801 |
| CLI aux-preview | Found | `aux_preview` :594 → `_resolve_from_pair_file` :597 (band override :616-618) or flags :626 → `emit_public_aux` :632 → `sys.stdout.buffer.write` :645 |
| Vendor ingestion bg:resolve (with production override) | Found | `cli` → pre-scan :293 → `bg_resolve` :259 → `resolve_bodygraph` resolver.py:161 → reference check :195 → `_resolve_vendor` :227 → rails :242/:252 → `classify_vendor_environment` :270 → matrix :285-299 → `append_event(allowed)` :301-316 → `_resolve_vendor_route` :326/:393 → v2 `HdApiClient.from_env` :543 → `fetch` :554 (or the legacy write guard :466 → ingest) → `_append_state_event` :330 → `emit_public` → `sys.stdout.write` |
| Evidence update | Found | `update_evidence_index.py:main` :5294 → `ensure_determinism_env` :5310 → `--check` `_run_once(check=True)` :5322, or `_WriteTransaction` → `_converge_and_publish` :5324-5325; inner writers not traced |
| CRD QA publication | Found (fixture only) | `publish_crd_check_family` :5166/:5183 → `_load_crd_qa_entries` :3947 → Index/Mirror publication; exercised by `test_crd_0002_fixture_root_publishes_beside_crd_0001` in a fixture repository; the real root is absent |
| Close pack (v2) | Found (no run) | `generate_epic_close_pack.py` main :4851 → `_require_closed_rails` → `--write` `_publish_pair` :4200-4290 (report, then manifest, then read-back) or `--check` |
| Golden comparison | Found | `generate_config_artifacts.py:392` → `_compare_goldens_main` :351 → `compare_goldens` (artifacts.py:969) |
| Gate readiness | Found | `check_magic10_gate_readiness.py:main` :211 → `require_closed_rails` :214 → `parse_selection` :215 → `DBAccess.for_current_env` :217 → `observe` :220 |
| Pre-push check | Found | `prepush_check.py` → `make_copy` (shared clone) → classifier in the copy → reports; before/after repository state compared |
| Dev sampler and conjunction HTTP | Found by name | `_dev_admin_gate` → sampler/conjunction handlers; not re-traced beyond the gate |

## 12. Drift and Reality vs Expectations

**Observations** (RA2-##), in source order, each with its comparison source. The triage assigns each a finding ID.

| ID | Observation | Comparison source | Alignment | Evidence |
| :- | :- | :- | :- | :- |
| RA2-01 | The release is 1.3.0 with 45 members; the roster equals the manifest; `release_id` 77204764… is the one production reported | Specification delta 01 C-5, C-7; Plan delta 01 P-3, P-4; addendum 2.22 | Aligned | E-202, E-206, E-306, E-313 |
| RA2-02 | Every 404 and 405 from `adapter.factory` is the governed `ERR_NOT_FOUND` envelope with no-store; the production Reader's unknown person is `ERR_M10_PERSON_UNRESOLVED` 404 | Spec S02 | Aligned on unknown paths; the person 404 is a canon-defined envelope | E-216 to E-219, E-245 |
| RA2-03 | Every test file is reached by a lane or a full-validation target; 66 retirements are recorded with reasons; O-P06a-03 is retired | Spec S03 | Aligned | E-126 to E-130 |
| RA2-04 | Unregistered `tools/qa` .py/.sh/.sql sources fail classification | Spec S04 | Aligned | E-124, E-131, E-132 |
| RA2-05 | The workflow path filter excludes exactly the classifier's 8 documentation prefixes | Spec S05 | Aligned | E-119, E-133, E-134 |
| RA2-06 | The attestation wheel stage detects a distribution-patched setuptools and injects a scoped compatibility shim; the Debian proof is the WU-PR-02 local rehearsal (E-318); hosted CI uses setup-python | Spec S06 | Aligned in code and tests; the hosted run does not exercise the Debian path | E-315 to E-318 |
| RA2-07 | showcompat help names `magic10_compat_result.v1` | Spec S07 | Aligned | E-256, E-463 |
| RA2-08 | aux-preview `--band` overrides the pair-file band | Spec S08 | Aligned | E-266 |
| RA2-09 | The dev Reader harness is retired; VERIFY.sh and the A7 crib have no harness reference | Spec S09 | Aligned | E-104, E-294, E-295, N-205, N-206 |
| RA2-10 | Dev `GET /reader` is served only for `APP_ENV` exactly `dev`; test and local refuse | Spec S10 ("dev, test or local"); Plan v1.1 §15; addenda 2.6 and 2.7 (CR-6, CR-8 APPROVED (a)) | Aligned with the approved Plan and canon; narrower than the Specification's text | E-226, E-227 |
| RA2-11 | The engine-core evidence test fails when `release_id` drifts | Spec S11 | Aligned | E-319, E-320 |
| RA2-12 | Current-release captures carry manifest-derived labels; no stray label | Spec S12 | Aligned | E-321 to E-323 |
| RA2-13 | The closure probe is root-bound and fails closed when `engine` comes from elsewhere | Spec S13 | Aligned | E-324, E-325 |
| RA2-14 | `--allow-prod-vendor` follows §7.1.11a to f in code and tests; the actor is the effective-UID account, so a human initiator is not enforceable by code | Spec S14; HDE CLI/API/Vendor Ref §7.1.11e; addendum 2.9 LR4-O2 | Aligned except the initiator, which is reserved for QA | E-261 to E-263, E-275 to E-288 |
| RA2-15 | The endpoint catalog has 18 rows; 53 served pairs = 18 rows + 35 reasoned exclusions; the retired `/ops/*` routes stay registered and answer as unknown paths in a prod posture | Spec S15; addendum 2.7 AD-1 | Aligned under AD-1 | E-246, E-238, E-247 |
| RA2-16 | `.env.example` has `GEO_API_KEY=changeme` and is a classified surface | Spec S16 | Aligned | E-401, E-402 |
| RA2-17 | `docs/ADAPTER_009.md` readiness and port statements match the code | Spec S17 | Aligned | E-403 to E-417 |
| RA2-18 | `docs/ADAPTER_009.md` says `invalid_json`; `ARCHITECTURE.md` states the `-> bytes` emitter and the mounts | Spec S18 | Aligned | E-418 to E-423 |
| RA2-19 | The S19 review recorded 9 findings fixed (fixes present on `main`) and 7 routed to the Product Owner with reasons | Spec S19 | Aligned as a record | E-340, E-341 |
| RA2-20 | The pre-push check reports lanes, membership, Build Notes path and hash, sweep and replay, read-only, with its own tests | Spec S20 | Aligned (the copy is a shared clone, not a `git worktree`) | E-135 to E-140 |
| RA2-21 | The v2 close-pack writer accepts Epic and CRD IDs; the close-run family is CRD-only and leaves the QA manifest alone; the ADR is approved with changes; no close pack or close run exists yet | Spec S21; addenda 2.15, 2.17 | Aligned; the ADR still carries the clause 2.17 supersedes | E-329 to E-339, N-303 |
| RA2-22 | The updater admits HDE-CRD-0002 alongside HDE-CRD-0001 and Epic inputs (fixture-tested). An evidence-lane test asserts that the real `audit/qa/hde-crd-0002/` does not exist and has no Index rows, so the first publication of HDE-CRD-0002 QA evidence fails that lane | Spec S22 ("Before HDE-CRD-0002 enters QA, the canonical updater publishes and validates Index and Mirror entries for artifacts under `audit/qa/hde-crd-0002/`"); Constraints "QA evidence admission"; QA requirement ("published by the canonical updater once S22 holds") | Drift: the delivered test contradicts the objective's real-root state | E-326 to E-328, E-005, E-006 |
| RA2-23 | `docs/ADAPTER_009.md` keeps stale text WU-DOC-01 did not touch: a stray "New" (:49); 5-key `/internal/version` bodies (:189-193, :223) against the six keys at :15 and in the code; "Override (prod)" (:209) although the code refuses in every environment | Code (E-428, E-427) | Drift (docs) | E-429 to E-431 |
| RA2-24 | `ARCHITECTURE.md` cites `canon.py::dumps` (an alias, :10, :25), describes compat GET as "ids-only" (:35; the code returns `{"ok":true,"schema":"v1"}`), and does not mention the S19 production posture | Code | Drift (docs) | E-249, E-242, E-238 |
| RA2-25 | `docs/contracts/reader_v2_public_bytes.md:8` says C040-07 is not drained into PF04/PF12; AGENTS.md's HDE-EPIC040 posture says "PF10 records them"; PF10 v13.7.5 has no C040 entries, and PF04, PF05 and PF12 now carry the content | Current canon | Drift (docs) | E-469, E-470, N-414 |
| RA2-26 | `adapter.http_reader.create_app`'s after_request never fires | Addendum 2.7 AD-4 item 4 | Persistent | E-221 |
| RA2-27 | showcompat/conjunction vendor acquisition has no production-override gate | S19-R01 (routed to the Product Owner); HDE CLI/API/Vendor Ref §7.1.11 scopes the flag to bg:resolve | Persistent, routed | E-289, N-208, E-340 |
| RA2-28 | The production env guard (`adapter/env_guard.py`) sees `app.config`, not the process environment; `adapter.factory` does not call it | Addendum 2.21 LR8-F1 | Persistent, routed | addendum 2.21 |
| RA2-29 | `tests/tools/test_prepush_check.py` raced git auto-maintenance once on hosted CI | Addendum 2.21 PR35-C1 | Persistent, routed | E-007 |
| RA2-30 | Two read-only validators (`update_evidence_index.py --check`, `run_canonical_json_gate.py --check-only`) import Flask, so they need the runtime install | AGENTS.md read-only validation list | Informational | E-141, E-146 |
| RA2-31 | The WU-OPS-01 evidence carries a SHA-256 ledger and no path proof or Index row (CR-9's interim treatment) | Plan delta 01 P-9; Glow QA Guide §11.1; CR-9 PROPOSED | As designed pending CR-9 | E-313, N-301 |
| RA2-32 | The packaging covers 29 of 45 release members (a stated limit) | Specification delta 01 C-6 | Stated limit | E-435, E-436 |
| RA2-33 | Root hygiene: zero-byte files, scratch files, duplicate hdctl scripts, `catalog/channels_catalog_v1.json` placeholder, " (1)" skill file names, the em-dash path, pytest.ini scope differs from CI | AGENTS.md "no QA artifacts in the repo root" | Informational | E-103, E-105 to E-107, E-114, E-117, E-449 |

**Historical comparison** with PF23 v1.2.2 (HDE-EPIC040 audit at `39b9cdf`, 2026-09-27):

| PF23 ID | Status at `39122b7` | Evidence |
| :- | :- | :- |
| RA-01 | Changed: same version, build time and roster; bytes and `release_id` moved by three same-version refreshes | E-306, E-307 |
| RA-02 | Persistent (aligned) | E-223 to E-225, E-253 |
| RA-03 | Changed: Index/Mirror 606 → 620, sentinels match; four of six validators rc 0 here, two need Flask; hosted evidence lane success | E-141 to E-146, E-301 to E-303, E-003 |
| RA-04 | Persistent as a stated limit (16 of 45; S01 removed) | E-436 |
| RA-05 | Resolved | E-217, E-220 |
| RA-06 | Changed, aligned with canon (exact `dev`; exact `{dev,test,local}` writers; production posture added) | E-226, E-232, E-238 |
| RA-07 | Resolved | E-256, E-266, E-104 |
| RA-08 | Resolved at source level (0 uncovered; 66 retired) | E-126, E-127 |
| RA-09 | Changed: the S19 review covered #467, #492, #501, #508 | E-340 |
| RA-10 | Persistent; not reopened (Spec exclusion "live Gate readiness and live Reader success") | E-468 |
| RA-11 | Persistent; not reopened (Spec exclusions) | E-263 |
| RA-12 | Resolved | E-119, E-133 |
| RA-13 | Changed: the file is still Python with a `.sh` name; AGENTS.md has no bash or sh invocation | E-447, E-448 |
| RA-14 | Resolved under AD-1 (10 → 18 rows; every pair accounted for) | E-246 |
| RA-15 | Persistent; not reopened | E-212, N-203, N-204 |
| RA-16 | Persistent; pytest.ini changed (12 → 80 entries) | E-449, E-450 |
| RA-17 | Resolved in PF10 v13.7.5 | E-451, E-452 |
| RA-18 | Changed: C040-06/07/08 content now in PF04, PF05, PF12; PF10 carries no C040 entry; completeness not established | E-469 |
| Duplicate `reader_v1` blueprint note | Resolved by static reading (the fallback is dead code) | E-235 |
| FND-001 to FND-004, FND-006 to FND-008, FND-010 to FND-014, FND-020, FND-022 | Persistent | E-464, E-423, E-465, E-458, E-466, E-457, E-410, E-449, E-467, N-415, E-461 |
| FND-005 | Persistent (core purity; I/O grep 0) | N-201, N-202 |
| FND-009 | Changed (counts) | E-102, E-459 |
| FND-015 | Persistent and extended (HDE-CRD-0002 admitted) | E-438 |
| FND-016 | Not re-checked: an HDE-CRD-0001 historical record with no current comparison point | — |
| FND-017 | Resolved | E-418, N-402 |
| FND-018 | Changed: hosted CI is now read through GitHub (E-003) | E-003 |
| FND-019 | Resolved as recorded (PF19 v3.0.6 §10.8 present) | E-472 |
| FND-021 | Persistent (public paths reach `compute_core` only through compat) | E-460, N-417 |
| FND-023 | Changed: HDE-CRD-0001's root has 23 files; HDE-CRD-0002's root does not exist yet | E-462 |
| FND-024 | Resolved at source level | E-463 |
| FND-025 | Resolved under AD-1 | E-246 |

## 13. Negative-Claim Proof Appendix

| ID | Pattern / target | Method | Case | Scope | Result |
| :- | :- | :- | :- | :- | :- |
| N-001 | `QA10`, `readiness`, `reality`, `triage` in HDE-CRD-0002 file names | `ls docs/ephemeral \| grep -i HDE-CRD-0002 \| grep -iE 'qa10\|readiness\|reality\|triage'` | insensitive | `docs/ephemeral` file names before this audit | 0 |
| N-002 | `absent real root`, `test_absent_admitted_crd_root`, `absent_admitted` | `grep -rln` | sensitive | `docs/ephemeral`, `docs/pfcanon` | only the WU-PR-02 instruction, plan, prototype diff, result and lineage review v1.0, and Plan v1.0/v1.1; none states the post-QA behaviour |
| N-101 | Dockerfile*, setup.py, setup.cfg | `ls` root; `find -iname 'Dockerfile*'` | insensitive | root; whole tree for Dockerfile | 0 |
| N-103 | `ALLOW_NETWORK\|SAFE_MODE\|socket\|def pytest_\|ensure_determinism` | `grep -nE` | sensitive | `tests/conftest.py` | 0 |
| N-104 | `dev/reader_harness` | `git ls-files` | sensitive | index | 0 |
| N-105 | `paths-ignore` | `git grep -c` | sensitive | `.github/` | 0 |
| N-106 | tracked `test_*.py` reached by no `ci.yml` token and no full-validation target | stdlib import of the classifier | sensitive | 215 files | 0 |
| N-107 | tracked `test_*.py` with no lane | `classify_paths` | — | 215 files | 0 |
| N-108 | ledger rows without a reason or date, or still tracked | python parse | — | 66 rows | 0 |
| N-109 | paths where the filter and the classifier disagree | stdlib replay | sensitive | 8194 tracked paths | 0 |
| N-110 | `tests/order`, `tests/http` | `grep -E` | sensitive | `pytest.ini` | 0 |
| N-111 | step "Run canonical JSON gate" | `grep -c` | sensitive | `ci.yml` | 0 |
| N-112 | `_FULL_VALIDATION_INACTIVE_TESTS` members | import | — | classifier | 0 |
| N-113 | registered owner paths missing on disk | import | — | 207 paths | 0 |
| N-114 | PF10 files other than v13.7.5 | `ls docs/pfcanon \| grep -c PF10` | sensitive | `docs/pfcanon` | 1 file |
| N-201 | `import engine\.db\|from engine\.db\|vendor_client\|urllib\|psycopg\|import socket\|requests\|http\.client\|open\(` | `grep -rnE` | sensitive | `engine/core`, `engine/magic10` | 0 |
| N-202 | `os\.environ\|getenv` | `grep -rnE` | sensitive | `engine/core/*.py`, `engine/magic10/*.py` | 0 |
| N-203 | `lru_cache\|functools\.cache\|@cache\b` | `grep -rnE` | sensitive | engine/config, engine/core, engine/magic10, presenter, engine/presenter, engine/runtime/public.py | 0 |
| N-204 | `allow_nan` | `grep -rn` | sensitive | engine/stable, engine/serializer | 0 |
| N-205 | `reader_harness`, `harness` | `grep -ni` | insensitive | VERIFY.sh, docs/acceptance/reader_a7_crib.md | 0 |
| N-206 | `reader_harness` in active scripts and tests | `git ls-files \| xargs grep -li`, archive and snapshot trees excluded | insensitive | tracked files | only CHANGELOG.md history and the classifier's lane map for the deleted paths |
| N-207 | `abort\(` | `grep -rn` | sensitive | adapter, engine/http, presenter, engine/runtime | 0 |
| N-208 | environment classification or override gate in `_acquire_dry_run` | read | — | resolver.py:915-1031 | absent |
| N-209 | `/ops/db/unavailable`, `/ops/probe/env`, `/ops/writer/diagnostic` as a catalog path or alias | JSON scan | sensitive | 18 rows | 0 |
| N-210 | vendor or resolver call in the Aux route | read | — | http_reader.py:755-802 | none |
| N-301 | `crd-0002` | `grep -ci`; python scan | insensitive | Index and Mirror | 0 |
| N-302 | `audit/qa/hde-crd-0002` | `ls`; `git ls-files \| grep -i crd-0002` outside docs/ephemeral | — | whole tree | absent; only the six wu-ops-01 files are tracked |
| N-303 | `audit/**/close/**`, `audit/HDE-CRD*` | `git ls-files 'audit/*' \| grep -E`; find | — | `audit/` | none |
| N-305 | current-release label outside `CURRENT_RELEASE_CAPTURE_PATHS` | regex over Mirror notes | exact | 620 rows | 0 |
| N-306 | manifest member digest or size mismatch | hashlib | — | 45 members | 0 |
| N-307 | `audit/ops/hde-epic040` | `grep -c` | exact | Mirror | 0 |
| N-401 | `localhost` | `grep -ci` | insensitive | docs/ADAPTER_009.md | 0 |
| N-402 | `body_not_allowed` | `grep -c` | sensitive | docs/ADAPTER_009.md | 0 |
| N-403 | `pip install` | `grep -cE` | sensitive | docs/ADAPTER_009.md | 0 |
| N-404, N-405 | `X-Toggles-SHA`; `TOGGLES_SHA`, `BUILD_COMMIT_SHORT`, `BUILD_TIMESTAMP_UTC` | `grep -rn --include=*.py`, tests excluded | sensitive | adapter; whole tree | 0 each |
| N-406 | `ensure_determinism_env` | `grep -rn` | sensitive | engine/cli | 0 |
| N-409 to N-411 | `persistence remains p`; mid-word line endings; Addendum Index vs body headings | grep; python | — | PF10 v13.7.5 | 0; 0; equal |
| N-412 | `bash` or `sh` invocation of `check_mirror_schema.sh` | grep | sensitive | AGENTS.md | 0 |
| N-414 | `C040-0[5-8]` | `grep -cE` | sensitive | PF10 v13.7.5 | 0 |
| N-415 | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` | `ls` | sensitive | exact path | absent |
| N-416 | `Bearer` | `grep -rli` | insensitive | artifacts/headers/ | 0 |
| N-417 | `compute_core` | `grep -cw` | sensitive | public.py, compat_handler.py, main.py, http_reader.py | 0 each |

## Canon relied on

Read on `main` at `39122b7`.

| Topic | Source and sections |
| :- | :- |
| Audit method, structure and historical comparison | PF23-Canon-Reality-Audits v1.2.2, read in full (front matter; §§1–13 of the HDE-EPIC040 audit at `39b9cdf`) |
| QA-10 placement, outputs and assessment states | PF19-Canon-Glow-QA-Guide v3.0.6 §3.1, §3.1.1, §3.1.2, §3.1.3, read in full; QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, read in full |
| Build Notes | PF10-HDE-Build-Notes v13.7.5 (sha256 2759c4da…e167): Addendum Index; addenda 2.21 and 2.22 read in full; every addendum's "Deferred obligations" or "Unresolved" section (2.2 to 2.22) read in full; 2.12 "Epic, task, and status effects"; 2.16 LR7-O4 and the option A line; 2.6, 2.7 (AD-1 to AD-5), 2.9, 2.15, 2.17 as read by the workers |
| S14 clause map | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11 and §§7.1.11a–f (read in full by the engine worker) |
| Infrastructure facts | PF07-Canon-Glow-Infrastructure v2.3.3 §0, §2.4, §3.1, §3.3, §4.1, §10 (read for Plan delta review v1.0 in this session) |
| Approved scope | Specification v1.1-approved §"Intake, analysis & bounded scope" through §"Canon, QA & Build Notes posture" (read in full); Specification delta 01 (read in full); Plan v1.1 §3, §6, §7 (WU-PR-02, WU-PR-08, WU-DOC-01, WU-OPS-01), §9 to §15; Plan delta 01 v1.1 (read in full) |
| Evidence writer rules | AGENTS.md "Governed evidence rules", "HDE-EPIC039 current workflow posture", "Release identity" |

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-10-20261023-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1 with delta 01) |
| unit | whole change |
| prompt | QA-10 — Audit Implementation and Establish QA Readiness — 100926.1, page state of 2026-10-12T02:30:12Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | continuing Isis, QA-10 |
| capture time | 2026-10-23T14:30:00Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, with four read-only worker subagents inside it |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; N-415) |

CANON_CONFLICT_REGISTER: CR-1 to CR-9 are carried unchanged; their statuses are in the readiness record §6.
