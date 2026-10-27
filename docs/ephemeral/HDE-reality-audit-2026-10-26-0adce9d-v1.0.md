---
artifact_type: REALITY_AUDIT
artifact_version: v1.0
title: "HDE Repository Reality Audit at 0adce9d"
repository: amthorn78/glow-hdengine-v2
audited_commit: 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b
observation_time_utc: "2026-10-26T18:15:45Z"
form: "PF23 HDE Reality Audits §1 (13 sections)"
producer: "Claude Code, session https://claude.ai/code/session_01RGjGWVEZreG9yshKfXifNJ"
prompt: "HDE Repository Reality Audit — 102626.1"
prompt_url: "https://app.notion.com/p/4054590a05eb818d8986c702bb309350"
status: COMPLETE
nonclaims: "Not Live QA evidence and not an acceptance token. Decides no QA verdict, acceptance, readiness, triage, closure or PF23 text."
---

# HDE Repository Reality Audit — `amthorn78/glow-hdengine-v2` at `0adce9d`

**Status: COMPLETE.** This is a factual record of the repository at one pinned commit, in the 13-section form of PF23 §1. It records facts and their evidence. Where two sources disagree it records both sides and the source compared; whether a difference is a defect is not decided here.

How to read it:

- §§2–11 give the current value of each fact that PF23's audit at `39b9cdf` recorded, plus this audit's new findings.
- §12 holds the comparisons: this audit's observations, canon claims, `AGENTS.md` and `README.md`, the PF23 history and the PF23 item table.
- An `E-xx-nnn` id is evidence and an `N-xx-nnn` id a negative claim. §13 gives every N- id with its pattern, tool, scope and result; the Evidence list at the end gives every E- id with its file and line, or its command, and the excerpt or result.

## 1. Audit Snapshot Metadata

| Field | Value |
| :--- | :--- |
| Repository and commit | `amthorn78/glow-hdengine-v2` at `0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b`, the head of `main` when pinned (subject "PF10", committed 2026-10-26T17:49:24Z) |
| Observation | Pinned 2026-10-26T18:15:45Z. Inspection continued in the same session into 2026-10-27 |
| Method | Static, read-only inspection by the producer and read-only workers in this session: `git show`, `git grep`, `grep` and standard-library Python parsing. The executable checks (validators, a wheel build, `hdctl` help runs and two test-suite runs) ran only in disposable clones of the pinned commit, outside the checkout. Every id was re-checked against the pinned commit before this file was written (Provenance) |
| Tools | `git` 2.43.0; host Python 3.13.17 for parsing; Python 3.12.3 with pytest 8.4.2 in the clones, after the CI install command |
| Environment | Recorded by name and SET/UNSET only. Every command set `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`. The session environment also holds `APP_ENV`, `DATABASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY` and `GEO_API_KEY` (SET), and leaves `HD_API_BASE_URL` and `ENGINE_ENV` UNSET (checked by name at 2026-10-27T00:10Z). The clone runs did not unset them, so they ran with them. Whether any clone run reached the database or the vendor was not established |
| Earlier audits | PF23 v1.2.2 (the audit at `39b9cdf`, 2026-09-27) and three session audits under `docs/ephemeral/` were used as comparison evidence only. No section, table or count was copied from them |

**Canon relied on:** PF23 Canon Reality Audits v1.2.2, read in full; PF04 HDE Governance §2.0.18 (drift stub); PF06 Change Process Guide §0.6.1; PF19 Glow QA Guide §3.1.1 and §10.6; HDE Build Notes (PF10) v13.8.6, read in full by a worker and its §0 and §1.1 by the producer; PF02 Architecture v2.4.6, PF05 CLI/API/Vendor Reference v2.5.3, PF12 Schemas and Artifacts v2.9.6, PF14 Mechanics Guide v3.5.8 and PF31 State of the Repository v0.1, as comparison sources; `AGENTS.md`. In-flight documents: none, because this audit belongs to no change.

**Coverage.** A section is COMPLETE only when every unit of its population was read in full.

| § | Population | Status |
| :- | :- | :- |
| 1 | Pin, tool versions, environment names, canon identities | COMPLETE |
| 2 | All 8,374 tracked index entries | COMPLETE |
| 3 | `pyproject.toml`, requirements, deployment and launcher files, backup-named files; wheel build | COMPLETE |
| 4 | All 97 `engine/` modules; release admission (`registry_loader.py`, 1,542 lines); `catalog/` (25 files), `schemas/` (47 files), mechanics configuration | COMPLETE |
| 5 | 888 tracked `.py` files searched: 12 Flask apps, 33 route decorators, 23 hooks; endpoint catalog against written routes | COMPLETE |
| 6 | Emitter and serializer modules and their call sites | COMPLETE |
| 7 | `engine/cli/main.py` (961 lines), 72 argparse CLIs, `hdctl` help runs | COMPLETE |
| 8 | Vendor client, `engine/db/`, mapped cache, readiness tool, `migrations/`, `sql/` | COMPLETE |
| 9 | 13 validators named by the prompt plus 8 named by `AGENTS.md`; Index, Mirror, orientation, manifest, roster, QA roots, close packs, acceptance maps, goldens | COMPLETE |
| 10 | 215 test files, pytest configuration, 2 workflows, the CI classifier (2,092 lines), the QA harness; two test-suite runs; hosted CI read | COMPLETE |
| 11 | 14 flow families, with every inner hop read in full (gap reads G1–G6) | COMPLETE |
| 12 | 2,316 canon claims of PF02, PF05, PF10, PF12 and PF14; all 228 `AGENTS.md` lines and 255 `README.md` lines; PF23's 43 RA and FND ids and 120 E- and N- ids | COMPLETE |
| 13 | Every N- id cited in this file | COMPLETE |

**Limitations.**

- The audit made no route, database or vendor probe of its own. Runtime, deployed and production state are Unknown. Whether a clone run reached the database or the vendor through the inherited variables was not established (Environment, above).
- Hosted CI was read, not re-run, and no hosted run exists for the pinned commit (§10). A test result here describes a disposable clone under the stated conditions; it is not CI's result.
- At 2026-10-26T19:32:35Z a `pytest --version` run with the checkout as its working directory wrote 10 ignored `.pyc` files. They were removed at 19:46:17Z, and no tracked file changed.
- At 2026-10-27T00:33Z the producer's check of this file imported the repository's hook script `.claude/hooks/check_canon_relied_on.py`, which wrote one ignored `.pyc` under `.claude/hooks/__pycache__/`. It was removed at 00:34:05Z, and no tracked file changed.
- `main` moved after the pin. At 2026-10-26T23:58:58Z `origin/main` was `9d9fcca0`, 4 commits later (E-02-932). Those commits add 56 files under `docs/ephemeral/` and rename PF10 HDE Build Notes from v13.8.6 to v13.8.8 (E-02-933, E-02-934). They are not audited, and the PF10 comparisons here are against v13.8.6.
- Drift stubs give the claims and the surface, as PF04 §2.0.18 asks. Each stub's bucket is "not assigned", because the prompt's stub names only claims and surface. The Product Owner chooses the bucket.
- This is the short form. The complete working record (every claim row and evidence register, 7 MB) is not published.

## 2. Top-level Repo Map

- E-02-001 8,374 tracked index entries: 8,235 with mode `100644`, 137 with `100755`, 2 symlinks (`120000`), no gitlinks.
- E-03-002 The tree is clean at the pinned commit.
- E-02-002 40 root directories, with tracked files each: `.audit_src/` 485, `.backup_epic004/` 6, `.claude/` 9, `.devcontainer/` 3, `.github/` 3, `.vscode/` 1, `_arch/` 147, `_archive/` 29, `adapter/` 17, `artifacts/` 1026, `audit/` 3196, `catalog/` 25, `ci/` 14, `codex/` 37, `config/` 2, `dev/` 2, `docs/` 2567, `engine/` 102, `errors/` 10, `fixtures/` 17, `freeze/` 1, `goldens/` 26, `handoff/` 49, `internal/` 5, `math/` 1, `migrations/` 3, `narratives/` 10, `notes/` 21, `parity/` 17, `presenter/` 4, `proofs/` 6, `release/` 1, `reports/` 2, `scan_reports/` 2, `schemas/` 47, `scripts/` 66, `sql/` 1, `tests/` 255, `tools/` 100, `validation/` 2.
- E-02-003 57 root files: project documents (`README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md` and others), build and run files, 14 `*step_report*.md` files, and scratch files (`.body200.json`, `.code304.txt`, `.tmp_refusal_get.txt`, `.tmp_refusal_post.txt`, `big.json`, `patch.diff`, `temp_run.*`, `changes_report.txt`, `code304_new.txt`, `manifest_pre.sha256`, `manifest_post.sha256`).
- E-02-006 344 zero-byte tracked files, among them the root files `Run`, `assert`, `import`, `temp_run.err` and `temp_run.out`.
- E-02-007 50 paths contain spaces. One also contains an em dash: `docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md` (E-02-011).
- E-02-005 The two symlinks: `docs/ENDPOINTS_CATALOG.json` → `../artifacts/audit/ENDPOINTS_CATALOG.json`, and `artifacts/ops/internal_version/body_get.json.sha256` → `body_get.sha256`.
- E-02-004 `docs/` holds 18 directories and 53 files. By directory: `ephemeral` 2319, `graph` 58, `pfcanon` 34, `prompt_ecosystem_management` 32, `schemas` 20, `evidence` 9, `design` 8, `plans` 8, `run` 6, `adr` 5, `crd` 3, `acceptance` 2, `architecture` 2, `changes` 2, `contracts` 2, `qa` 2, `ops` 1, `server` 1.
- E-02-008 Evidence homes:
  - the Human Index (653 rows, 639 distinct paths) binds artifacts under nine top-level directories;
  - 928 `.path_proof.txt` companions are tracked;
  - `goldens/` (26 files) and `proofs/` (6 files) hold evidence-like files that no Index row names.
- E-02-009 Prefix lists in `ci/checks/classify_ci_changes.py`:
  - `_HISTORICAL_PREFIXES` (:156–165) has 8 entries;
  - `_DOCUMENTATION_PREFIXES` (:171–180) has 8 entries: `docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/` and `docs/run/`.
- E-02-010 20 file names directly under `docs/ephemeral/` match PF23's prior-readiness pattern N-00, where PF23 recorded none.

## 3. Packaging and Entrypoints

- `pyproject.toml`:
  - name `glow-hdengine`, version `0.0.0`, `dependencies = []`;
  - one console script, `hdctl = "engine.cli.main:cli"` (N-12-907);
  - packages `engine*`, `adapter*`, `presenter*`, `catalog*` and `math*`, with package data `*.json` for `catalog` and `math` (E-03-014, E-03-015, E-03-019, E-03-021, E-03-024, E-03-026, E-03-027). Unchanged since PF23.
- `requirements.txt` lists `psycopg[binary]`, `Flask<3.0`, `gunicorn<22` and `jsonschema==4.23.0` (E-03-040–E-03-043). `requirements-dev.txt` adds `pytest`, `pytest-cov` and `pytest-mock` (E-03-045, E-03-047–E-03-049).
- `Procfile:1` is `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …` (E-03-054, E-03-055). Three server configurations differ (RA-20261026-11).
- Other launchers: `run_flask.py:22`, `run_flask_dev.sh:21`, `scripts/start_web.sh:4`, `scripts/scratch.py:4`, `adapter/app.py` (a `wsgi` alias) and `scripts/dev_start_reader.sh:26` (`python -m adapter.http_reader`) (E-03-114, E-03-122, E-03-111, E-11-1383, E-03-096, E-03-135). `dev/reader_harness/app.py` is no longer tracked; a copy is at `.audit_src/dev/reader_harness/app.py:7` (E-03-216, N-03-019). The two dev runners differ in bind address, port and reloader (RA-20261026-12), and `scripts/demo_mvp.sh` runs a module that has no `__main__` block (RA-20261026-13).
- `hdctl` copies outside the package: `scripts/hdctl.py`, `scripts/hdctl.clean.py`, `scripts/hdctl.backup.py` and `scripts/hdctl.py.bak` (E-03-363).
- No `Dockerfile*`, `setup.py` or `setup.cfg` is tracked (N-12-901, N-03-008, N-03-010, N-03-011).
- A wheel built in a disposable clone has 130 entries and lacks 16 of the 45 release members, as `README.md:138` also states (E-03-901, E-03-902, E-03-903). PF23 recorded 15 of 44.

## 4. Engine Modules

- `engine/core/` holds `__init__.py` and `core.py` (E-04-903). `engine/core/__init__.py` was first added in `c57d5b4b` on 2025-11-30 (E-04-901), before PF23's audit commit (E-04-914), and no commit deletes it (N-04-901). The thirteen subpackages PF23 names are among the 28 first-level directories of `engine/` (E-04-902).
- Release admission (`engine/config/registry_loader.py`), unchanged since PF23:
  - `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` and `ADMITTED_RELEASE_ROSTER = tuple(sorted({…}))` at :398–400 (E-04-576–E-04-578);
  - an import-time check that the roster has 45 entries, else `RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")` (:448–449) (E-04-055, E-04-056, E-04-579);
  - `_validate_admitted_manifest` (1219–1241) raises `INCOMPLETE_RELEASE_ROSTER`, `RELEASE_ROSTER_MISMATCH`, `RELEASE_VERSION_MISMATCH` or `RELEASE_TIMESTAMP_MISMATCH` (E-04-105, E-04-106, E-04-169, E-04-173–E-04-175);
  - `MISSING_FILE` at :478, in `_safe_source_path` (E-04-904, E-04-093);
  - `load_active_mechanics_bundle()` (1506–1511): "Admit the exact installed complete mechanics release, or fail closed" (E-04-081–E-04-084).
- `_deep_freeze` maps a Mapping to `MappingProxyType` and a list or tuple to a tuple, and returns other types unchanged (E-04-137, E-04-905, E-04-149–E-04-151).
- `engine/core/core.py`:
  - `CoreResult` is a frozen, slotted dataclass, and `compute_core(member_a, member_b, mechanics_bundle, release_id)` is at :209;
  - errors collapse to `ValueError("invalid pure core contract")` (E-04-907, E-04-183, E-04-185–E-04-188, E-04-204);
  - there are no I/O imports in `engine/core` or `engine/magic10` (N-12-903);
  - its callers outside tests are `engine/compat/compute.py:346`, `tools/config/artifacts.py:645–647` and `tools/evidence/generate_engine_core_evidence.py:120–123` (E-04-308, E-04-911).
- `engine/compat/compute.py`:
  - it requires `type(bundle) is AdmittedMechanicsBundle`, else `CompatBoundaryError("admission_config")`;
  - its intrinsic cache is keyed `INTRINSIC_CACHE_PREFIX` + `pair_key`, and a hit is revalidated (E-04-908, E-04-264, E-04-265, E-04-912, E-04-913);
  - its module state is `_BUNDLE_PROVIDER` (:50) and `_SCHEMA_VALIDATORS` (:52) (E-04-245, E-04-247);
  - there is no `lru_cache` or `functools.cache` in the paths PF23 named (N-12-904).
- Catalog and configuration:
  - `catalog/channels_v1.json` has 36 Channels, gates in ascending order, 36 unique pairs and no null field (E-04-835, N-04-547);
  - `catalog/magic10_mechanics_v1.json` (`config_id` `m10-channel-state-v1.0.0`) has three schemas (E-04-776, E-04-652–E-04-654), 20 signals, 10 category weights and 3 profiles (E-04-779, E-04-781, E-04-787, E-04-790);
  - the Balance operations are `twice_min_owner_mass_v1` and `companionship_em_mass_v1`, refused with `SIGNAL_OPERATION_MISMATCH` (`registry_loader.py:1168`) and "invalid Balance operation" (`signals.py:107`) (E-04-800, E-04-801, E-04-798, E-04-823);
  - `catalog/channels_catalog_v1.json` holds one placeholder row, is not a roster member, and is referenced by no `engine/` or `tools/` module (E-04-511, N-04-501, N-04-502).
- `engine/charts/loader.py` reads `SAFE_MODE` (:54), writes `loader_call.jsonl` (:71) and times calls with `perf_counter` (:95, :168) (E-04-369, E-04-909, E-04-910).
- New findings, both sides recorded in §12.1:
  - `engine/core`'s import closure reaches non-pure modules (RA-20261026-17);
  - `engine/magic10/thresholds.py` reads a file at import (RA-20261026-18);
  - `compute.py` reads its schema from disk on each validation (RA-20261026-19);
  - the band thresholds have two sources, which agree (RA-20261026-21).

## 5. Adapter / HTTP Surfaces

- Three app factories mount the same three blueprints: the dev blueprint at "", the API blueprint at `/api`, and the compat blueprint. They are:
  - `adapter/factory.py:13–15` (`create_app` at :11);
  - `adapter/http_reader.py` `create_app` (:1249; registrations at :1252, :1257 and :1260);
  - `adapter/wsgi.py:23–25`.

  (E-03-078, E-03-080, E-11-009, E-11-010, E-05-038–E-05-041, E-11-012, E-11-013.)
- All three factories return JSON for unknown paths and methods:
  - `adapter/factory.py` has `errorhandler(404)` (:30) and `errorhandler(405)` (:35), which return `ERR_NOT_FOUND` for every path. Its `after_request` (:43) converts compat-path HTML 404s and 405s (E-05-208–E-05-216).
  - The `http_reader` handlers at :1287 and :1293 do the same, and the 405 handler sets `Allow` (E-05-217–E-05-220).
  - `wsgi` has global 404 and 405 handlers that return `ERR_NOT_FOUND` (E-05-224, E-05-225).

  PF23 recorded HTML 404s on two factories (RA-05, now Resolved).
- `adapter/wsgi.py`:
  - it serves `/internal/healthz` and `/internal/readyz`;
  - it sets `no-store` by `setdefault` (:28);
  - it adds HSTS (:38) when `APP_ENV` or `ENGINE_ENV` is `prod`, `production` or `live` (:36) (E-05-069, E-05-070, E-05-356, E-05-364, E-05-429, E-05-393).
- Production Reader:
  - `POST /api/reader` is at `http_reader.py:640` and calls `_production_reader_response` (:525) (E-11-027–E-11-030). It serves `v=1` and `v=2` (RA-20261026-04).
  - GET, HEAD, OPTIONS, PUT, PATCH and DELETE get a governed 405 (:644) (E-11-227–E-11-229).
  - Other methods are refused by the before-request hook `_refuse_unrouted_methods` (:648–665) (E-11-024–E-11-026, E-11-233).
  - The 405 is `ERR_NOT_FOUND` with status 405 and `Cache-Control: no-store` (E-11-230–E-11-232, E-05-288, E-05-289).
- Dev routes:
  - `GET /reader` requires `APP_ENV` exactly `dev`, and refuses an unset value with 403 (E-05-129–E-05-131);
  - `_dev_admin_gate` (:901–907) allows `APP_ENV` in {dev, test, local} and answers anything else with `ERR_WRITER_FORBIDDEN` 403 (E-11-563–E-11-565).
- The compat blueprint (`engine/http/compat_handler.py`) has prefix `/api/compat/v1` (:19), GET at :122, POST at :130, HEAD at :180 and OPTIONS at :185 (E-11-266, E-11-314, E-11-281, E-11-317, E-11-319).
- The endpoint catalog (`docs/ENDPOINTS_CATALOG.json`, a symlink) has 18 rows; PF23 recorded 10.
  - 17 rows match a written route; `HEAD /reader` matches none.
  - 12 of the 30 written live route pairs have no row: the six non-POST `/api/reader` methods, `POST /reader`, and five pairs on three retired `/ops/*` paths (E-05-450, E-05-457, E-05-465, N-05-029, E-05-477–E-05-486, E-09-033).
  - Its `env_gate` strings differ from the code conditions (RA-20261026-28).
- Other differences between two repository sources:
  - the Reader's `Cache-Control` differs from `adapter/etag_core.py` (RA-20261026-29);
  - the `/internal/version` body differs from `adapter/schemas/version_v1.schema.json` (RA-20261026-30);
  - `adapter.wsgi` defaults `RELEASE_ID` to `rel_dev` (RA-20261026-27).

## 6. Presenter / Emitter

- The emitters are `presenter/reader_v1/emitter.py`, `presenter/json_canon_compare.py` and `engine/presenter/emitter.py` (`emit_public`, `emit_public_with_envelope`, `emit_compact_json`) (E-06-016, E-06-018, E-06-020, E-06-023, E-06-024, E-06-138).
- Category items:
  - each item is exactly `{id, band}`, with the band checked against `_CATEGORY_BANDS` (E-06-055–E-06-059);
  - a duplicate id raises `ValueError` (`emitter.py:41`; E-06-060);
  - `_ordered_categories_v2` requires `FROZEN_MAGIC10_ORDER` when eligible and `[]` when not (E-06-902, E-06-062, E-06-063).
- `engine/runtime/public.py`:
  - Reader v1 emits only `harmony` (or `[]`);
  - it dispatches v1 and v2, and raises `ValueError("reader_version_unsupported")` otherwise;
  - `_emit` hashes the five-key preimage into `idempotence_hash` (E-06-070–E-06-072, E-04-289, E-06-067, E-06-068, E-06-025–E-06-029, E-06-065, E-06-066).
- `engine/stable/sercanon.py:21–28` serializes with `json.dumps(…, ensure_ascii=False, compact separators, sort_keys=…)` plus exactly one LF (E-11-206–E-11-208). There is no `allow_nan` in `engine/stable` or `engine/serializer` (N-12-905).
- The CLI reaches the emitters through `main.py:812` → `engine.runtime.public.emit_reader_public_envelope` → `emit_reader_v1`/`emit_reader_v2` → `emit_public`. `tools/config/artifacts.py:738` calls `emit_reader_v1` (E-11-470, E-11-186, E-11-192–E-11-194, E-11-199, E-11-941).

## 7. CLI Surfaces

- The only console script is `hdctl`, which calls `cli` in `engine/cli/main.py` (:284) (E-03-021, E-03-029, N-12-907). `add_subparsers(required=True)` is at :91 (E-07-030).
- The subcommands are `showcompat`, `aux-preview`, `bg:resolve` and `dev:sampler`; their help was run in a clone (E-07-901, E-07-902a–E-07-902d). `hdctl --version` prints `hdctl 0.0.0 (hdengine@prod;77204764…)` (E-07-903).
- `showcompat`:
  - its help reads "Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader" (E-07-032, E-07-901);
  - its stdout is the canonical `magic10_compat_result.v1` document plus one LF (`main.py:829`; the conjunction wrap is at `compute.py:423`) (E-07-147, E-11-486, E-04-277);
  - `_emit_stdout_bytes` (:570–575) raises `STDOUT_MISSING_LF` and `STDOUT_CRLF` (E-07-141, E-07-143, E-07-145).

## 8. Vendor Seam & BodyGraph Storage

- `engine/bodygraph/vendor_client.py`:
  - the base URL comes from `HD_API_BASE_URL` or `HDAPI_BASE_URL` (:197–200), and differing values give `PROVIDER_CONFIG_INVALID`;
  - https is required (:297–298), and `HD_API_KEY` is named at :333 (E-08-183–E-08-186, E-08-225, E-08-226);
  - the transport refuses with `PROVIDER_REFUSED` unless `SAFE_MODE=0` and `ALLOW_NETWORK=1`, and its opener follows no redirects (:762–765) (E-08-192, E-08-193, E-08-207, E-08-208, E-08-237, E-08-239);
  - the logged `rails_state` and the refusal read different sources (RA-20261026-23).
- The database is direct-only:
  - the retired bridge keys (`engine/db/adapter.py:16–18`) are refused in `DBAccess.for_current_env` before any provider is built (E-08-286, E-11-048, E-11-049);
  - `DATABASE_URL` is the only configuration, and the provider is `PsycopgProvider` (E-08-285, E-08-293).
- Mapped cache (`engine/bodygraph/mapped_cache.py`): posture `adapter_mapped_no_raw_vendor_payload` (:19); `persist_mapped_bodygraph` (:60; `PROVIDER_WRITE_UNSUPPORTED` at :89); `read_current_mapped_bodygraph` (:165) (E-08-428, E-11-741, E-08-1901, E-08-442).
- Gate readiness (`tools/bodygraph/check_magic10_gate_readiness.py`):
  - it declares itself read-only, with `"read_only": True` (:82), and uses `DBAccess.for_current_env()` (:217);
  - its refusals are `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID` and `READINESS_UNAVAILABLE`;
  - a selection is at most 1 MiB, and it requires closed rails (E-08-455–E-08-457, E-08-460, E-08-465, E-08-466, E-08-468, E-11-967);
  - its body has no `INSERT`, `UPDATE`, `DELETE`, `persist_mapped` or `commit(` (N-12-906).
- There is no top-level `vendor/` directory (N-12-908).
- Differences between two repository sources: `ingest.py:306` passes `details` positionally to a keyword-only parameter (RA-20261026-22), and the route policy's `error_code` is read where no branch sets it (RA-20261026-26).

## 9. Evidence, Indices, Catalogs

**Validators**, run in a disposable clone at the pin, under closed rails. A fingerprint of `git status` taken before and after each command was unchanged, so no command wrote into the clone.

| Id | Command | Exit |
| :- | :- | -: |
| E-09-001 | `python tools/evidence/update_evidence_index.py --check` | 0 |
| E-09-002 | `python tools/evidence/orientation_demo.py --check` | 0 |
| E-09-003 | `python tools/evidence/validate_evidence_paths.py` | 0 |
| E-09-004 | `ci/checks/check_mirror_schema.sh`, run directly; it exits 2 when run through `bash` (E-10-914) | 0 |
| E-09-005 | `ci/checks/check_evidence_index_hash.sh` | 0 |
| E-09-006 | `ci/checks/check_final_lf.sh` | 0 |
| E-09-007 | `python tools/evidence/check_lf_endings.py` | 0 |
| E-09-008 | `ci/checks/check_env_pins.sh` | 0 |
| E-09-009 | `python scripts/release_id_recompute.py --check-manifest-only` | 0 |
| E-09-010 | `python tools/evidence/run_canonical_json_gate.py --check-only` | 0 |
| E-09-011 | `python tools/config/generate_config_artifacts.py --compare-goldens .` (8 of 8 cases match) | 0 |
| E-09-012 | `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check`. It exits 1 with `DIRTY_TREE` in the clone holding the CI install's ignored `egg-info` directory, and 0 in a clean clone (E-09-012b) | 1 / 0 |
| E-09-013 | `python tools/ci/prepush_check.py lanes build-notes`; also 0 with the clone's `origin/main` set to the pin (E-09-013b) | 0 |
| E-09-040–E-09-047 | the 8 read-only checks that `AGENTS.md` names: the HDE-EPIC037 parent binding, DB runtime posture, BodyGraph policy proofs, v2 mapped cache, direct-DB contract, HDE-EPIC038 direct-DB selection, and EPIC031 PR02 and PR03 | 0 each |

- Indices:
  - the Human Index `docs/evidence/INDEX.json` has 653 rows (PF23: 606), and its sentinel matches (E-09-020);
  - the Machine Mirror has 653 lines, and its sentinel matches (E-09-021);
  - the orientation file reads `total_artifacts: 653` and `status: ok` (E-09-022);
  - the Index was last changed in `09e443f4` (E-09-035), and 16 rows are tagged HDE-EPIC040 (E-09-036).
- Release manifest:
  - `catalog/manifest.json` has version `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`, 45 files and canonical bytes (E-09-023);
  - its paths equal `ADMITTED_RELEASE_ROSTER` exactly (E-09-024), and it was last changed in `822ce15c` (E-09-037);
  - its path proof records a different size and SHA-256 from the file's (RA-20261026-10).
- The endpoint catalog is a symlink with 18 rows, last changed in `2f3db0a0` (E-02-005, E-09-033, E-09-038).
- Other evidence:
  - `goldens/` holds 26 files, and the frozen EPIC022 records are present (E-09-029, E-09-039, E-09-030);
  - `audit/qa/hde-crd-0001/` has 23 files (E-09-026);
  - the OPS01 evidence under `audit/ops/hde-epic040/ops01/` passes its `SHA256SUMS` 7 of 7 and is not in the Index or the Mirror (E-09-050, N-09-004, N-09-005).
- The canonical JSON gate declares 26 target paths and 6 set rules (E-09-031). `artifacts/registry/registry_report.json` carries no release identity (E-09-032, N-09-002).
- The tracked PF10 is v13.8.6. Its §1.1 index lists 2.1–2.33, which matches its body, and it ends with the authored marker `\<eof\>` (E-02-012–E-02-014, E-02-018).
- Two further differences: sanity stage 11's name does not match its `--check` step (RA-20261026-25), and the `orientation_demo.py` comment differs from its body (RA-20261026-31).

## 10. Tests, QA Harness, CI/Checks

- `tests/` has 255 tracked files, 215 of them `test_*.py`; PF23 recorded 316 and 277 (E-10-012). `tests/conftest.py` only adjusts `sys.path`, and `tests/provider/conftest.py:270` reads `SAFE_MODE` (E-10-915, E-10-053, N-12-902).
- `pytest.ini` `testpaths` has 80 entries, which reach 134 of the 215 test files. It has no `tests/order` or `tests/http` entry (E-10-032, E-10-913, N-12-914).
- `.github/workflows/ci.yml` (420 lines):
  - it runs on `pull_request` and on `push` to `main`, with a `paths` filter of `'**'`, the 8 documentation-prefix negations and 3 re-includes (E-10-009, E-10-174, E-10-175, E-10-188, E-10-191, E-10-193, N-10-021);
  - it has one `test` job (:43), with exact-head checkout (:59), Python 3.12 (:85), seven lanes and the final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (:420) (N-10-023, E-10-213, E-10-228, E-10-336, E-10-438).
- `epic-closeout-validation.yml` runs on `pull_request` (path-filtered) and `workflow_dispatch`; PF23 recorded dispatch only (E-11-1119–E-11-1121).
- The CI classifier:
  - it has 7 lanes (E-10-438, E-10-011) and 8 documentation prefixes (E-10-446);
  - `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` has 109 entries, all tracked (E-10-442, E-10-571);
  - its owner registry covers 205 of the 215 test files (E-10-612, E-10-616, E-10-617, E-10-619–E-10-622, E-10-626).
- `tools/qa/qa_harness.py`:
  - its statuses are `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED` and `PARKED` (E-10-630–E-10-635);
  - for an empty input its two roll-ups differ: `summarize_checks` gives `TOOLING_BLOCKED` and `_status_rollup` gives `PASS` (RA-20261026-32).
- Test runs, in a disposable clone under the conditions of §1:
  - the `testpaths` run exits 0 with `3240 passed, 3 skipped` (E-10-901);
  - the whole `tests/` directory exits 1 with `1 failed, 5855 passed, 3 skipped, 2 xfailed` (E-10-902);
  - the failure is `tests/bodygraph/test_vendor_prod_override.py::test_record_and_streams_carry_no_subject_url_or_secret`, and its cause was not established (E-10-903).
- Hosted CI (read, not re-run):
  - no run exists for the pinned commit (E-10-910);
  - the latest `ci` run on `main` (head `1fb4731`) failed on `tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest` (E-10-911);
  - that test passed 3 of 3 times when run alone in the clone (E-10-904);
  - the 19 `main` push runs before it succeeded (E-10-912).
- The retired-tests ledger `tests/retired_tests.md` lists `tests/reader_v1/test_cli_proof.py` (E-10-165).

## 11. Flows & Call Chains

Every flow below was traced hop by hop to its writes. Each inner hop that the first trace left unread was then read in full, in gap reads G1 to G6.

| # | Flow | Entry | Evidence |
| :- | :- | :- | :- |
| 1 | Reader HTTP v1/v2 and dev `GET /reader` | `get_reader_bp` (`adapter/http_reader.py:669`, registered at :1158); production `POST /api/reader` (:640) | E-11-001–E-11-004, E-11-027 |
| 2 | Compat HTTP `/api/compat/v1` | the transport guard, `engine/http/compat_handler.py:108–109` | E-11-270, E-11-271 |
| 3 | `hdctl showcompat` | the console script (`pyproject.toml:14`) → `cli` (`engine/cli/main.py:284`) | E-11-327–E-11-329 |
| 4 | Aux preview | parser `main.py:140`, handler :151 → `aux_preview` (:594) | E-11-487–E-11-489, E-11-339 |
| 5 | Dev sampler | parser `main.py:186`, handler :203 → `dev_sampler_run` (:928) | E-11-533–E-11-535 |
| 6 | `hdctl bg:resolve` | parser `main.py:152` (`--source` default `auto`, :161) → `bg_resolve` (:259) | E-11-619–E-11-624 |
| 7 | Configured-v2 mapped cache | `persist_mapped_bodygraph` (`engine/bodygraph/mapped_cache.py:60`; exactly six keys, :65) | E-11-741, E-11-745, E-11-746 |
| 8 | Evidence update | `tools/evidence/update_evidence_index.py` `main` (:5294; `--check`, `--rebind-sanity-log`, `--epic-id`) | E-11-782–E-11-784 |
| 9 | Golden comparison | `tools/config/generate_config_artifacts.py` `_main` (:386), `--compare-goldens` | E-11-901–E-11-903 |
| 10 | Gate readiness | `tools/bodygraph/check_magic10_gate_readiness.py` `main` (:211) | E-11-954–E-11-956, N-11-013 |
| 11 | QA harness recording | `tools/qa/epic021_qa.py` `main` (:1725), with the library `tools/qa/qa_harness.py` | E-11-978–E-11-982 |
| 12 | Close pack `--write` / `--check` | `tools/qa/generate_epic_close_pack.py` `main` (:4914; exactly one `--source` and one mode) | E-11-1044–E-11-1048, N-11-016 |
| 13 | Release cut and runtime identity | `scripts/cut_release_manifest.py` `main` (:184) | E-11-1138–E-11-1140 |
| 14 | Every other route, hook, subcommand and launcher | 23 route registrations, 16 hook lines, 4 subcommands, 13 launcher rows | — |

Release identity closure (`tools/evidence/regenerate_identity_closure.py`):

- `CLOSURE_STEPS` has 18 steps (E-11-5203, E-11-5204). The program runs only with `HDE_ISOLATED_RELEASE_BUILD=1` and `--in-place-isolated` (E-11-5223, E-11-5224).
- Steps 14 (`bodygraph_policy`) and 15 (`mapped_cache`) each also write two files under `schemas/` that are not among their declared outputs (E-11-5331–E-11-5333, E-11-5341–E-11-5343).
- Step 8 (`canonical_json`) also writes a `.path_proof.txt` for each of its six outputs, and these are not declared outputs (E-11-5284, E-11-5285, E-11-3765–E-11-3768).
- Step 16 also writes `artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt`, which is not declared (E-11-3325, E-11-3569).
- The canonical-JSON gate runs its validators in both write mode and `--check-only` mode (E-11-3663–E-11-3666). Three of them copy their inputs into standard-library temporary directories (E-11-3177, E-11-3194, E-11-3209), and one changes the process working directory and restores it (E-11-3202).
- `ensure_request_chain_manifest` creates its directory before any check, whatever `allow_create` is (E-11-3319).

## 12. Drift and Reality vs Expectations

### 12.1 Observations

#### 12.1.A This audit's observations

Every observation is a fact with both sides. "Two repository sources" means two places in the repository disagree. A PF31 row compares a repository fact with PF31, which is reference canon; a `K-31-nnn` id names the PF31 line compared. Status: Aligned, Partial or Drift. The drift stub follows PF04 §2.0.18: the two claims and the surface, with the bucket "not assigned".

| Id | Observation | Compared with | Status | Evidence | Drift stub |
| :- | :- | :- | :- | :- | :- |
| RA-20261026-01 | `engine/compat/compute.py` `evaluate_pair` takes category scores from `compute_core(lo.gates, hi.gates, bundle, release_id)` (`:346`), which reduces ten categories from twenty Gate/Channel signals with integer arithmetic. The viewer-preference parameters of `conjunction_public` are not used in its body. | PF31 §1.2 table, `engine/compat/compute.py` row (K-31-002) | Drift | E-04-911, E-04-266, E-04-185, E-04-210, E-04-211, E-04-212, N-04-009 | Source claim: "Category scores are derived from a stable hash of pair identity and category, then modified by viewer weights." (K-31-002) · Conflicting repository fact: Scores come from `compute_core` (E-04-911); `viewer_weights` is unused in `conjunction_public` (N-04-009) · Surface: `engine/compat/compute.py` · bucket: not assigned |
| RA-20261026-02 | `engine/runtime/public.py` does not name `ts_v0` or `band_v0`. `emit_reader_public_envelope` emits caller-supplied bands: Reader v1 `[{"id": "harmony", "band": …}]` (or `[]` when ineligible), Reader v2 the ten categories in `FROZEN_MAGIC10_ORDER`. | PF31 §1.2 table, `engine/runtime/public.py` row (K-31-003) | Drift | N-04-902, E-04-288, E-04-290, E-04-292 | Source claim: "Calls `ts_v0` and builds a Harmony-only projection." (K-31-003) · Conflicting repository fact: No `ts_v0` reference (N-04-902); v1 Harmony-only, v2 ten categories (E-04-290, E-04-292) · Surface: `engine/runtime/public.py` · bucket: not assigned |
| RA-20261026-03 | `band_v0` still returns `Warm` when `sacral_pair` is true and `Open` otherwise. It is defined twice in `engine/compat/ts_v0.py`. Outside `docs/`, `audit/` and `.audit_src/`, only `scripts/hdctl.backup.py` and `scripts/hdctl.clean.py` import `ts_v0`. | PF31 §1.2 table, `ts_v0.band_v0` row (K-31-011) | Aligned | E-04-918, E-04-919 | — |
| RA-20261026-04 | Production `POST /api/reader` is registered and serves `v=1` and `v=2` (exactly one `v` value from `{"1","2"}`, else `ERR_READER_INVALID_VERSION` 400). Other methods on `/api/reader` get a governed 405. Dev `GET /reader` remains and requires `APP_ENV` exactly `dev` (otherwise 403 `ERR_READER_FORBIDDEN`). | PF31 §1.2 table, HTTP Reader row (K-31-004) | Drift | E-11-027, E-11-029, E-11-031, E-11-032, E-11-034, E-11-035, E-11-227, E-11-229, E-11-230, E-11-234, E-11-237, E-11-239, E-11-240 | Source claim: "GET is development-only and fixture-backed; POST returns 405" (K-31-004) · Conflicting repository fact: `POST /api/reader?v=1\|2` is served (E-11-027, E-11-031); 405 is for the other methods (E-11-227) · Surface: Reader HTTP (`adapter/http_reader.py`) · bucket: not assigned |
| RA-20261026-05 | In production posture the compat guard answers every compat path with `compat_error_response(404)`. | PF31 §1.2 qualification (K-31-005) | Aligned | E-11-274, E-11-275, E-11-276 | — |
| RA-20261026-06 | No hosted workflow run exists for the audited commit. The latest hosted `ci` run on `main` (head `1fb4731`) concluded failure; the 19 `main` push runs before it succeeded. The five commits after `1fb4731` change only `docs/ephemeral/` and `docs/pfcanon/` paths, which the `ci.yml` path filters exclude. | PF31 §1.3 (K-31-006) | Drift | E-10-910, E-10-911, E-10-912, E-10-916, E-10-917, E-10-178, E-10-180, E-10-191 | Source claim: "The exact reviewed `main` commit has a successful hosted `test` check." (K-31-006, about `9cda1b49`) · Conflicting repository fact: No hosted run for `0adce9d`; latest `main` run failed (E-10-910, E-10-911) · Surface: Hosted CI (`.github/workflows/ci.yml`) · bucket: not assigned |
| RA-20261026-07 | `catalog/manifest.json` lists 45 members at version `1.3.0`, and its paths equal `ADMITTED_RELEASE_ROSTER`. | PF31 §1.4 (K-31-007) | Drift | E-09-023, E-09-024 | Source claim: "The current `catalog/manifest.json` contains fifteen members." (K-31-007) · Conflicting repository fact: 45 members (E-09-023) · Surface: `catalog/manifest.json` · bucket: not assigned |
| RA-20261026-08 | `engine/charts/loader.py` reads `SAFE_MODE` from the environment, times calls with `time.perf_counter`, imports the legacy `resolve_provider` inside `try/except` (set to `None` on failure), appends JSON lines to `loader_call.jsonl` after creating its directory, and returns `{"gates": [1, 2, 3]}` on the legacy path when no resolver is available (also at line 141). | PF31 §2.2 (K-31-008, K-31-009) | Aligned | E-04-369, E-04-910, E-04-915, E-04-909, E-04-916, E-04-917 | — |
| RA-20261026-09 | `pyproject.toml` declares version `0.0.0` and `dependencies = []`; `requirements.txt` lists four runtime requirements. | PF31 §2.4 (K-31-010) | Aligned | E-03-015, E-03-019, E-03-040, E-03-041, E-03-042, E-03-043 | — |
| RA-20261026-10 | `catalog/manifest.json.path_proof.txt` records `size_bytes: 1981` and `sha256: dbf89997…`; `catalog/manifest.json` is 5,881 bytes with SHA-256 `77204764…`. Of the six path proofs under `catalog/`, this is the one that does not match. Neither the Human Index nor the Machine Mirror names this path proof. | `catalog/manifest.json.path_proof.txt` vs `catalog/manifest.json` | Drift | E-04-533, E-04-534, E-04-581, E-04-580, N-09-006 | — |
| RA-20261026-11 | Three server configurations differ: `Procfile:1` binds `0.0.0.0:$PORT` with 2 workers, 4 threads and a 30 s timeout; `scripts/start_web.sh:4` uses the same values with a `${PORT:-8000}` default; `adapter/gunicorn.conf.py:1-4` sets `0.0.0.0:8080`, 1 worker, timeout 10, keepalive 2, and no code-type file references it. | `Procfile` vs `scripts/start_web.sh` vs `adapter/gunicorn.conf.py` | Drift | E-03-055, E-03-111, E-03-061, E-03-062, E-03-063, E-03-064, N-03-015 | — |
| RA-20261026-12 | The two dev runners differ: the `adapter/http_reader.py` `__main__` block binds `127.0.0.1`, uses `PORT` (default 8000) and turns the debugger and reloader off; `run_flask.py` binds `127.0.0.1`, port 5000, with `use_reloader=True` and `FLASK_DEBUG` defaulting to `1`. | `adapter/http_reader.py:1319-1324` vs `run_flask.py` | Drift | E-03-090, E-03-091, E-03-092, E-03-094, E-03-095, E-03-116, E-03-117, E-03-119, E-03-121 | — |
| RA-20261026-13 | `scripts/demo_mvp.sh:15` runs `python adapter/app.py`; `adapter/app.py` has no `__main__` guard and no `.run(` call. | `scripts/demo_mvp.sh` vs `adapter/app.py` | Drift | E-03-201, N-03-025 | — |
| RA-20261026-14 | `ci/checks/classify_ci_changes.py:266` maps `dev/reader_harness/app.py` to the `product` lane; nothing is tracked under `dev/reader_harness/`. The tracked file with that path tail is `.audit_src/dev/reader_harness/app.py`. | CI change classifier vs tracked tree | Drift | E-03-147, N-03-019, E-11-1397, N-11-028, E-11-1398 | — |
| RA-20261026-15 | `_HISTORICAL_BACKUP_PATHS` in the CI classifier names six backup files, including `scripts/hdctl.backup.py` and `scripts/hdctl.py.bak`; the tracked backup-named script `scripts/hdctl.clean.py` is not named anywhere in that file. | CI classifier backup list vs tracked backup-named files | Partial | E-03-393, E-03-394, E-03-395, E-03-396, E-03-397, E-03-398, E-03-399, N-03-033 | — |
| RA-20261026-16 | The `_admission_execution_provenance` docstring says "eight actual consumers" and its owners tuple has 8 entries; the comment in `load_active_mechanics_bundle` says "corroborate all four live origins". | `engine/config/registry_loader.py` docstring vs comment | Drift | E-04-143, E-04-089, E-04-144 | — |
| RA-20261026-17 | `engine/core` is documented as "Pure Gate kernel" and `engine/core/core.py` is in the purity test's `PURE_PATHS`. Its own imports contain no forbidden item. Its static top-level import closure (31 modules) reaches `engine/bodygraph/__init__.py` → `resolver.py` → `vendor_client.py` (`socket`, `urllib.request`) and `engine/db`. | Package docstring and purity test vs static import closure | Partial | E-04-019, E-04-414, N-04-023, E-04-431, E-04-437, E-04-438, E-04-439, E-04-440, E-04-441 | — |
| RA-20261026-18 | The `engine/magic10` package docstring says "Private pure mechanics used by engine.core". `engine/magic10/thresholds.py` reads `math/thresholds.json` at import; `engine/core/core.py` imports only `calculators`, `composite` and `signals` from the package. | Package docstring vs `thresholds.py` | Partial | E-04-024, E-04-232, E-04-181 | — |
| RA-20261026-19 | `tools/evidence/generate_hdapi_v2_contract_inventory.py` names `engine/compat/compute.py` the adapter-boundary pure-compute locus. `compute.py` reads the compat-result schema bytes from disk on each validation and imports `engine.bodygraph.resolver` at top level. | Tool constant vs `engine/compat/compute.py` | Drift | E-04-428, E-04-272, E-04-240 | — |
| RA-20261026-20 | `engine/sampler/core.py` describes itself as "Pure-compute sampler core"; its own imports contain no forbidden item, and its static closure (47 modules) includes `engine/compat/compute.py` and the bodygraph and db modules. | Module docstring vs static import closure | Partial | E-04-427, N-04-024, E-04-434 | — |
| RA-20261026-21 | Band thresholds have two sources whose values agree: 24/49/74 hard-coded in `calculators.py`, `core.py` and `compute._band_for_score`; `compute.band_for` uses edges from `math/thresholds.json` (`[24,49,74,100]`), which admission pins. | Hard-coded thresholds vs `math/thresholds.json` | Aligned | E-04-213, E-04-206, E-04-249, E-04-248, E-04-236, E-04-129 | — |
| RA-20261026-22 | `engine/bodygraph/ingest.py:306` constructs `VendorError("DB_PAYLOAD_MISSING", "stored payload missing", {})` with three positional arguments; `engine/bodygraph/vendor_client.py:216` declares `details` keyword-only. | Call site vs constructor signature | Drift | E-08-641, E-08-642 | — |
| RA-20261026-23 | `HdApiClient.from_env` derives the logged `rails_state` from the mapping it is given (`vendor_client.py:359`); the transport refusal reads `SAFE_MODE`/`ALLOW_NETWORK` from `os.environ` (`vendor_client.py:762-764`). | Two reads of the same rails values | Partial | E-08-643, E-08-644 | — |
| RA-20261026-24 | The dev sampler healthcheck comment says the Reader runner "binds to 0.0.0.0" (`scripts/qa/dev_sampler_healthcheck.py:129`); the Reader `__main__` block passes `host="127.0.0.1"` (`adapter/http_reader.py:1320`). | Script comment vs Reader runner | Drift | E-11-1393, E-11-1394, E-11-1371 | — |
| RA-20261026-25 | Sanity stage 11 is named "Human Index and Machine Mirror refresh"; the step bound to it runs `update_evidence_index.py --check`. | Stage name vs stage command (`tools/evidence/run_sanity_pipeline.py`) | Drift | E-11-1399, E-11-1400, E-11-1220 | — |
| RA-20261026-26 | The resolver and the vendor client read `route_policy["error_code"]` when a policy is not supported; both return branches of `classify_bg_resolve_route_policy` carry `supported: True` and no `error_code` key. | Route guards vs route-policy function | Drift | E-11-678, E-11-679, E-11-1401, E-11-440, E-11-1402, E-11-677, N-11-008 | — |
| RA-20261026-27 | `adapter.wsgi.create_app` defaults `RELEASE_ID` to `rel_dev` and sends it as `X-Release-Id`; `/internal/version` reports the release id computed from the packaged manifest (`77204764…`). | `adapter/wsgi.py` vs `engine/runtime/identity.py` | Drift | E-11-1258, E-11-1257, E-11-1403, E-11-1238 | — |
| RA-20261026-28 | Endpoint-catalog `env_gate` strings compared with the code conditions: the `/api/compat/v1` rows say `APP_ENV!=prod`, while the code refuses with 404 when `_compute_env_mode(os.environ) == "prod"`, a mode that also falls back to `ENGINE_ENV` and folds `production`/`live` to `prod`. The dev-route rows (`APP_ENV in {dev,test,local}`) and `/reader` rows (`APP_ENV=dev`) state the code conditions. The `operator-network-only` rows have no environment read in their handlers; the `not_applicable_public` rows have no environment gate. | `artifacts/audit/ENDPOINTS_CATALOG.json` `env_gate` vs handler code | Partial | E-05-487, E-05-172, E-05-442, E-05-443, E-05-488, E-05-147, E-05-246, E-05-489, E-05-130, E-05-490, N-05-013, N-05-030, N-05-031, E-05-160, E-05-491, N-05-012 | — |
| RA-20261026-29 | Reader success responses set `Cache-Control: private, max-age=0, must-revalidate` (`adapter/http_reader.py:42`); `adapter/etag_core.py:6` defines `READER_CACHE = "private, no-cache, must-revalidate"`, and no live module imports `adapter/etag_core.py`. | `adapter/http_reader.py` vs `adapter/etag_core.py` | Drift | E-05-501, E-05-389, N-05-020 | — |
| RA-20261026-30 | `adapter/schemas/version_v1.schema.json` requires `ok, schema, engine_tag, release_id, checksums, toggles_sha, build` with `additionalProperties: false`; `/internal/version` emits `identity_admin()`, whose keys are `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`. The test that validates the route against that schema is marked `xfail(strict=False)`. | `version_v1` schema vs `/internal/version` payload | Drift | E-05-502, E-05-503, E-06-001, E-06-002, E-05-504, E-05-505 | — |
| RA-20261026-31 | The `tools/evidence/orientation_demo.py` module comment says the updater must run first in write mode and that `generate_orientation(check=False)` writes the orientation report; the body of `generate_orientation` with `check=False` calls the updater's `main([])` and returns, with the comment "Compatibility write mode has no independent write authority." | Module comment vs function body (`tools/evidence/orientation_demo.py`) | Drift | E-11-9293, E-11-9294, E-11-9295, E-11-9296 | — |
| RA-20261026-32 | In `tools/qa/qa_harness.py`, `summarize_checks` returns `TOOLING_BLOCKED` for an empty input (lines 1469–1470), and `_status_rollup` returns `PASS` for an empty input (line 3441); both use the same four-member precedence order. `_status_rollup` computes the viability `final_status` from the issue statuses and non-PASS diagnostic statuses. | `AGENTS.md:48` ("no absent or unevaluated condition becomes a PASS", row P-A-033) vs the two roll-up functions | Partial | E-11-6937, E-11-6742, E-11-6938, E-11-6738, E-11-6813 | — |

RA-20261026-33 to -39 are the per-document counts in §12.1.B.

#### 12.1.B Canon claims compared with the repository

Each current-state or status claim of the documents below was compared with the repository at the pinned commit. The labels are Aligned, Partial, Drift, Unknown and Not a claim. Unknown means the claim names hosted, runtime, person-held or historical state, or a record that is not in the repository, so it cannot be checked statically.

| Document | Claims | Aligned | Partial | Drift | Unknown | Not a claim |
| :- | -: | -: | -: | -: | -: | -: |
| PF02 HDE Architecture v2.4.6 | 97 | 74 | 4 | 4 | 14 | 1 |
| PF05 HDE CLI/API/Vendor Reference v2.5.3 | 255 | 171 | 29 | 29 | 25 | 1 |
| PF10 HDE Build Notes v13.8.6, lines 1–1799 | 456 | 370 | 20 | 0 | 66 | 0 |
| PF10 HDE Build Notes v13.8.6, lines 1800–3641 | 525 | 457 | 13 | 1 | 54 | 0 |
| PF12 HDE Schemas and Artifacts v2.9.6 | 327 | 280 | 14 | 5 | 9 | 19 |
| PF14 HDE Mechanics Guide v3.5.8, lines 1–5999 | 331 | 242 | 29 | 16 | 42 | 2 |
| PF14 HDE Mechanics Guide v3.5.8, lines 6000–7723 | 325 | 215 | 30 | 12 | 58 | 10 |
| **All** | **2316** | **1809** | **139** | **67** | **268** | **33** |

The rows labelled Drift, with their drift stubs (PF04 §2.0.18: the source claim, the conflicting repository fact and the surface; bucket "not assigned"):

| Claim | Document | Line | Drift stub |
| :- | :- | :- | :- |
| K-02-063 (B) | PF02 | L173 | Source claim: 'Canonical documents and plans MUST NOT contain ... the Unicode ellipsis character (U+2026) ... three consecutive U+002E' (L173-177). Conflicting repository fact: U+2026 on 131 lines/12 files and '...' on 50 lines/11 files of docs/pfcanon (E-02-2816, E-02-2818). Surface: docs/pfcanon/*.md. bucket: not assigned |
| K-02-333 (A) | PF02 | L1094 | Source claim: 'dev/reader_harness/app.py silently treats an absent APP_ENV as dev' (L1094). Conflicting repository fact: No dev/reader_harness/ path at PINNED (N-12-2807); the behavior exists only in the .audit_src/ copy (E-02-2801). Surface: dev/reader_harness/app.py. bucket: not assigned |
| K-02-334 (A) | PF02 | L1094 | Source claim: 'registers only the Reader blueprint under /api, calls app.getattr instead of app.register_blueprint, and does not mount the compat blueprint' (L1094). Conflicting repository fact: No dev/reader_harness/ path at PINNED (N-12-2807). Surface: dev/reader_harness/app.py. bucket: not assigned |
| K-02-365 (A) | PF02 | L1172 | Source claim: 'Current limitation: showcompat requires vendor-sourced BodyGraph data to compute compatibility.' (L1172). Conflicting repository fact: Local file/stdin and DB sources need no vendor (E-07-2810, E-08-2881, E-07-2809). Surface: hdctl showcompat input sources. bucket: not assigned |
| K-05-076 (A) | PF05 | L125 | Source claim: 'the unimplemented production override requirement' (L125). Conflicting repository fact: The override flag and its environment/audit gate are implemented (E-07-2836, E-08-2862, E-08-2863). Surface: hdctl bg:resolve --allow-prod-vendor; engine/bodygraph/resolver.py. bucket: not assigned |
| K-05-133 (B) | PF05 | L279 | Source claim: 'the payload is the compat JSON shape ... { "a": ..., "b": ..., "viewer_prefs": ..., "compat": {...} }' (L279). Conflicting repository fact: stdout is the unwrapped magic10_compat_result.v1 (E-07-2806, E-04-2807). Surface: hdctl showcompat stdout. bucket: not assigned |
| K-05-165 (A) | PF05 | L416 | Source claim: 'the bg:export-json wording in §4.8 still permits empty stdout or a human synopsis ... the admin-bundle wording in §4.9 still permits a human file-success synopsis' (L416). Conflicting repository fact: PF05 L1066 and L1182 require a canonical JSON receipt (E-02-2812, E-02-2813). Surface: docs/pfcanon/PF05 sections 4.8.2 and 4.9. bucket: not assigned |
| K-05-221 (B) | PF05 | L614 | Source claim: 'When --conjunction is used, --compat-format is ignored.' (L614). Conflicting repository fact: --compat-format is not an option (N-12-2815). Surface: hdctl showcompat --conjunction. bucket: not assigned |
| K-05-278 (A) | PF05 | L778 | Source claim: 'hdctl showcompat currently depends on vendor-backed computation ... requires either a local compute path or a cached or seeded deterministic vendor stub' (L778). Conflicting repository fact: A local compute path and offline file/stdin inputs exist (E-07-2807, E-04-2804, E-07-2810). Surface: hdctl showcompat. bucket: not assigned |
| K-05-382 (B) | PF05 | L1196 | Source claim: 'schemas/admin_bundle.births.v1.json' (schema home). Conflicting repository fact: No schemas/admin_bundle* file at PINNED (N-12-2805). Surface: schemas/. bucket: not assigned |
| K-05-383 (B) | PF05 | L1197 | Source claim: 'schemas/admin_bundle.request.v1.json' (schema home). Conflicting repository fact: No schemas/admin_bundle* file at PINNED (N-12-2805). Surface: schemas/. bucket: not assigned |
| K-05-384 (B) | PF05 | L1198 | Source claim: 'schemas/admin_bundle.response.v1.json' (schema home). Conflicting repository fact: No schemas/admin_bundle* file at PINNED (N-12-2805). Surface: schemas/. bucket: not assigned |
| K-05-385 (B) | PF05 | L1199 | Source claim: 'schemas/admin_bundle.receipt.v1.json' (schema home). Conflicting repository fact: No schemas/admin_bundle* file at PINNED (N-12-2805). Surface: schemas/. bucket: not assigned |
| K-05-386 (B) | PF05 | L1200 | Source claim: 'schemas/admin_bundle.audit.v1.json' (schema home). Conflicting repository fact: No schemas/admin_bundle* file at PINNED (N-12-2805). Surface: schemas/. bucket: not assigned |
| K-05-559 (A) | PF05 | L2071 | Source claim: 'the factory-specific HTML 404 limitation is retained in §5.1.7' (L2071). Conflicting repository fact: Both factories return JSON ERR_NOT_FOUND for unknown paths (E-05-2804, E-05-2877). Surface: adapter/factory.py; adapter/http_reader.py 404 handling. bucket: not assigned |
| K-05-600 (A) | PF05 | L2253 | Source claim: 'unknown non-compat paths, including Reader descendant paths, receive framework HTML 404 from adapter/factory.py and adapter/http_reader.py' (L2253). Conflicting repository fact: Both factories register JSON 404 handlers (E-05-2804, E-05-2877). Surface: adapter/factory.py; adapter/http_reader.py. bucket: not assigned |
| K-05-691 (B) | PF05 | L2527 | Source claim: 'artifacts/cli/transport/post_nonconditional_proof.log, artifacts/cli/transport/no_secrets_error_headers.log' (L2527). Conflicting repository fact: Neither file is tracked (N-12-2829). Surface: artifacts/cli/transport/. bucket: not assigned |
| K-05-700 (B) | PF05 | L2548 | Source claim: '\| /internal/admin/bundle/v1 \| POST \| internal admin; authenticated and scope-gated ...' (L2548). Conflicting repository fact: No catalog record or route (N-12-2810, N-12-2804). Surface: docs/ENDPOINTS_CATALOG.json; admin bundle route. bucket: not assigned |
| K-05-716 (B) | PF05 | L2596 | Source claim: 'v - required exactly once; after ordinary URL decoding its value MUST be exactly ... 1' (L2596). Conflicting repository fact: No v handling in the Aux handler (N-12-2811). Surface: GET /aux/narrative, /api/aux/narrative. bucket: not assigned |
| K-05-718 (B) | PF05 | L2601 | Source claim: 'Missing v, empty v=, unsupported values ... and every duplicate occurrence return the version refusal' (L2601). Conflicting repository fact: No v validation (N-12-2811). Surface: Aux query grammar. bucket: not assigned |
| K-05-719 (B) | PF05 | L2603 | Source claim: 'slot, viewer_top, flags, flag, families_fired, release_id, pack_sha ... are not public ... refused before composition' (L2603). Conflicting repository fact: Hidden names are read and forwarded (E-05-2849, E-05-2854). Surface: Aux handler query parsing. bucket: not assigned |
| K-05-720 (B) | PF05 | L2605 | Source claim: 'The server obtains families_fired, release_id, pack_sha ... from governed internal mechanics and identity state' (L2605). Conflicting repository fact: Values are taken from the query (E-05-2852, E-05-2853, E-05-2851). Surface: Aux handler. bucket: not assigned |
| K-05-721 (B) | PF05 | L2616 | Source claim: 'An unsupported query name wins over an invalid v.' (L2616). Conflicting repository fact: No refusals exist (N-12-2803). Surface: Aux handler. bucket: not assigned |
| K-05-722 (B) | PF05 | L2622 | Source claim: '400 ERR_AUX_UNSUPPORTED_QUERY_PARAMETER' (L2622). Conflicting repository fact: Token absent (N-12-2803). Surface: Aux refusals; errors/token_map. bucket: not assigned |
| K-05-723 (B) | PF05 | L2623 | Source claim: '400 ERR_AUX_INVALID_VERSION' (L2623). Conflicting repository fact: Token absent (N-12-2803). Surface: Aux refusals; errors/token_map. bucket: not assigned |
| K-05-724 (B) | PF05 | L2637 | Source claim: 'Both refusals use Content-Type: application/json; charset=utf-8 and Cache-Control: no-store ...' (L2637). Conflicting repository fact: No Aux refusal exists (N-12-2803). Surface: Aux handler. bucket: not assigned |
| K-05-725 (B) | PF05 | L2637 | Source claim: 'The version gate runs before identity preflight, narrative routing, suppression, or prose composition.' (L2637). Conflicting repository fact: No version gate (N-12-2811). Surface: Aux handler. bucket: not assigned |
| K-05-740 (B) | PF05 | L2727 | Source claim: 'POST /_ops/bodygraph/resolve with body ...' (L2727). Conflicting repository fact: Route absent (N-12-2806). Surface: /_ops/bodygraph/resolve. bucket: not assigned |
| K-05-741 (B) | PF05 | L2730 | Source claim: 'With rails closed, a source:"vendor" request returns a typed refusal without making any outbound call.' (L2730). Conflicting repository fact: Route absent (N-12-2806). Surface: /_ops/bodygraph/resolve. bucket: not assigned |
| K-05-828 (A) | PF05 | L3380 | Source claim: '.env.example omitting GEO_API_KEY remains an implementation-lane documentation gap' (L3380). Conflicting repository fact: .env.example line 4 names GEO_API_KEY (E-02-2823). Surface: .env.example. bucket: not assigned |
| K-05-839 (B) | PF05 | L3473 | Source claim: 'An unversioned base ... fails with PROVIDER_ROUTE_UNSUPPORTED before credential projection or any external I/O.' (L3473). Conflicting repository fact: Unversioned bases go to legacy bodygraphs; no such code (E-08-2826, N-12-2812). Surface: engine/bodygraph/vendor_client.py route policy. bucket: not assigned |
| K-05-847 (A) | PF05 | L3500 | Source claim: 'The following production override contract is a requirement, not an available CLI facility.' (L3500). Conflicting repository fact: --allow-prod-vendor and its gate are implemented (E-07-2836, E-08-2862). Surface: hdctl bg:resolve --allow-prod-vendor. bucket: not assigned |
| K-05-848 (A) | PF05 | L3500 | Source claim: 'finds no --allow-prod-vendor implementation or corresponding authenticated override/audit gate' (L3500). Conflicting repository fact: Implementation and audit gate present (E-07-2836, E-08-2864). Surface: engine/cli/main.py; engine/bodygraph/resolver.py; engine/bodygraph/vendor_audit.py. bucket: not assigned |
| K-10-975 | PF10 | 2055 | Source claim: Line 2055: "This record follows addendum 2.18, which is pending publication." Conflicting repository fact: PF10 at PINNED contains addendum 2.18 (E-02-4865) and addendum 2.20, the record self-numbered 2.18 (E-02-4864, E-02-4866). CL-C-10 records the publication numbering (E-02-4868). Surface: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md (line 2055). bucket: not assigned |
| K-12-685 | PF12 | L1941 | Source claim: "The exact manifest digest and current release_id are 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96." (L1941). Conflicting repository fact: PINNED digest/release_id 77204764...c51e E-09-3202 (E-09-023); 52be4558 = manifest at 8999bd05 E-09-3204; 4 manifest commits after 2026-10-09 E-09-3205. Surface: catalog/manifest.json; release_id. bucket: not assigned |
| K-12-1380 | PF12 | L5945 | Source claim: prior_release_id: "52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96" (L5945). Conflicting repository fact: PINNED release_id 77204764... E-09-3202 (E-09-023); 4 manifest commits after 2026-10-09 E-09-3205. Surface: catalog/manifest.json; release_id. bucket: not assigned |
| K-12-1381 | PF12 | L5946 | Source claim: computed_release_id: "52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96" (L5946). Conflicting repository fact: Recomputed at PINNED: 77204764... E-09-3202 (E-09-023). Surface: catalog/manifest.json; release_id. bucket: not assigned |
| K-12-1382 | PF12 | L5947 | Source claim: "prior release_id remains valid; verified by static hashing of unchanged manifest bytes" (L5947). Conflicting repository fact: Manifest changed after 2026-10-09 (c98d41f3, 2f3db0a0, 58925380, 822ce15c) E-09-3205; digest 77204764... E-09-3202. Surface: catalog/manifest.json. bucket: not assigned |
| K-12-1385 | PF12 | L5961 | Source claim: evidence_path: "docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md" (L5961). Conflicting repository fact: Not tracked; PF10 at PINNED is v13.8.6 E-02-3203; deleted in 632f1cdf E-02-3204. Surface: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md. bucket: not assigned |
| K-14-210 | PF14 | PF14:684 | Source claim: 'call the sampler evidence generator and tools/evidence/generate_engine_core_evidence.py ..., then refresh the Evidence Index and Machine Mirror' (PF14:684-687) · Conflicting repository fact: the 15-stage pipeline has no sampler/Engine Core step (N-12-3604) and its Index stage is check-only (E-09-3628) · Surface: tools/evidence/run_sanity_pipeline.py · bucket: not assigned |
| K-14-213 | PF14 | PF14:695 | Source claim: 'audit/qa/hde-epic024/checks/D01_env_pins_gate/primary.log' (PF14:695) · Conflicting repository fact: the tracked path is .../d01_env_pins_gate/primary.log (lowercase directory) (E-02-3625, N-12-3606) · Surface: EPIC024 D01 env-pins evidence path · bucket: not assigned |
| K-14-237 | PF14 | PF14:898 | Source claim: 'HDE-Build Notes records the bounded header-helper correction, the generic harness and composed publication contract' (PF14:898) · Conflicting repository fact: PF10 v13.8.6 has 0 lines with those terms (N-12-3608) · Surface: PF10 HDE-CRD-0001 records · bucket: not assigned |
| K-14-1217 | PF14 | PF14:4947 | Source claim: 'adapter/http_reader.py binds 0.0.0.0, not the required ordinary-local 127.0.0.1' (PF14:4947) · Conflicting repository fact: create_app().run(host="127.0.0.1", ...) (E-03-3602); no 0.0.0.0 in the file (N-12-3629) · Surface: adapter/http_reader.py runner · bucket: not assigned |
| K-14-1218 | PF14 | PF14:4948 | Source claim: 'The module invocation does not explicitly bind debug=False, use_debugger=False, or use_reloader=False' (PF14:4948) · Conflicting repository fact: the runner passes all three explicitly (E-03-3605, E-03-3613, E-03-3614) · Surface: adapter/http_reader.py runner · bucket: not assigned |
| K-14-1220 | PF14 | PF14:4950 | Source claim: 'The Reader handler treats missing APP_ENV as dev' (PF14:4950) · Conflicting repository fact: the dev gate requires APP_ENV exactly dev; unset is refused with 403 (E-11-239, E-11-240) (E-05-3605) · Surface: adapter/http_reader.py dev GET /reader gate · bucket: not assigned |
| K-14-1428 | PF14 | PF14:5605 | Source claim: 'The recorded root cause class is proof-class and evidence-discipline separation across a Dissolution closeout' (PF14:5605) · Conflicting repository fact: audit/EPIC-030_QA_RCA.md has no root-cause or proof-class text (N-12-3635) · Surface: audit/EPIC-030_QA_RCA.md · bucket: not assigned |
| K-14-1433 | PF14 | PF14:5614 | Source claim: 'The recorded QA verdict is READY WITH CAVEATS' (PF14:5614) · Conflicting repository fact: the tracked QA RCA records 'NOT FINAL until ...' (E-09-3776); no EPIC030 record contains READY WITH CAVEATS (N-12-3636) · Surface: audit/EPIC-030_QA_RCA.md · bucket: not assigned |
| K-14-1435 | PF14 | PF14:5620 | Source claim: 'PF10 is the primary record for epic-specific implementation events, remediation loops, ADRs, QA outcomes, evidence pointers, and review-close trace' (PF14:5620) · Conflicting repository fact: PF10 v13.8.6 has no HDE-EPIC030 content (N-12-3639, E-02-3680) · Surface: PF10 / EPIC030 records · bucket: not assigned |
| K-14-1457 | PF14 | PF14:5706 | Source claim: 'No closure-trace evidence gap remains visible in PF10' (PF14:5706) · Conflicting repository fact: PF10 v13.8.6 has no HDE-EPIC030 content (N-12-3639) · Surface: PF10 / EPIC030 closure trace · bucket: not assigned |
| K-14-1458 | PF14 | PF14:5707 | Source claim: 'PF09.2 actual drain is not proven and is intentionally non-claimed' (PF14:5707) · Conflicting repository fact: PF09.2 records the EPIC030-scoped rows Done (E-02-3684, E-02-3685) · Surface: PF09.2 Dissolution rows · bucket: not assigned |
| K-14-1506 | PF14 | PF14:5877 | Source claim: '/reader as public Reader route context' (PF14:5877) · Conflicting repository fact: GET/HEAD /reader is cataloged dev_harness; POST /api/reader is public_reader (E-09-3654) · Surface: Endpoint Catalog / Reader routes · bucket: not assigned |
| K-14-1527 | PF14 | PF14:5918 | Source claim: 'Parent HDE-FERM001 status posture remains a later close or drain judgment' (PF14:5918) · Conflicting repository fact: PF09.5 records HDE-FERM001 Task status Done (E-02-3699) · Surface: PF09.5 HDE-FERM001 · bucket: not assigned |
| K-14-1558 | PF14 | PF14:5992 | Source claim: 'ci/checks/check_bridge_consistency.py' (PF14:5992) · Conflicting repository fact: not tracked (E-02-3703); deleted in a618ba7b (E-02-3704) · Surface: ci/checks/ · bucket: not assigned |
| K-14-1561 | PF14 | PF14:5995 | Source claim: 'tests/unit/test_check_bridge_consistency.py' (PF14:5995) · Conflicting repository fact: not tracked (E-02-3703); deleted in a618ba7b (E-02-3705) · Surface: tests/unit/ · bucket: not assigned |
| K-14-1563 | PF14 | PF14:5997 | Source claim: 'tools/evidence/generate_db_bridge_parity.py' (PF14:5997) · Conflicting repository fact: not tracked (E-02-3703); deleted in a618ba7b (E-09-030) · Surface: tools/evidence/ · bucket: not assigned |
| K-14-1568 | PF14 | 6018 | Source claim: L6018: PR-03 'treats APP_ENV=live as production-like by aligning live with prod and production for bridge fallback guarding'. Conflicting repository fact: No bridge fallback guard exists at PINNED and live is not handled (E-08-4004, E-08-4005, N-12-4010). Surface: engine/db/adapter.py (APP_ENV handling); tests/db/. bucket: not assigned |
| K-14-1580 | PF14 | 6061 | Source claim: L6061: PR-04 path tests/evidence/test_generate_db_bridge_parity_nondev.py. Conflicting repository fact: The file does not exist at PINNED (N-12-4002). Surface: tests/evidence/test_generate_db_bridge_parity_nondev.py. bucket: not assigned |
| K-14-1622 | PF14 | 6172 | Source claim: L6172: 'APP_ENV=live remains recorded as production-like bridge-guard hardening for the DB bridge mechanics family'. Conflicting repository fact: engine/db/adapter.py has no bridge guard and labels live as unknown (E-08-4004, E-08-4005, N-12-4010). Surface: engine/db/adapter.py. bucket: not assigned |
| K-14-1729 | PF14 | 6553 | Source claim: L6553: 'PF10 2.1, PF10 2.16, and the HDE-FERM004.2 combined-evidence decision are recorded as candidates for permanent PF-Canon memorialization'. Conflicting repository fact: PF10 2.1 and 2.16 at PINNED have unrelated content (E-09-4154, E-09-4156, N-12-4014). Surface: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md. bucket: not assigned |
| K-14-1763 | PF14 | 6681 | Source claim: L6681: 'PF09.5 still showed HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4 as Not done'. Conflicting repository fact: PF09.5 v1.6.1 shows all five rows Done (E-09-4165, E-09-4166). Surface: docs/pfcanon/PF09.5 HDE-FERM006 rows. bucket: not assigned |
| K-14-1764 | PF14 | 6682 | Source claim: L6682: 'HDE-FERM007 implementation proof was not present.' Conflicting repository fact: HDE-FERM007 proof artifacts exist and PF09.5 shows HDE-FERM007 Done (E-09-4280, E-02-4040, E-09-4168). Surface: artifacts/vendor/hdapi_v2/; docs/pfcanon/PF09.5 HDE-FERM007. bucket: not assigned |
| K-14-1765 | PF14 | 6683 | Source claim: L6683: 'HDE-FERM008 live conformance and open-rails proof were not present.' Conflicting repository fact: Later acceptance maps bind HDE-FERM008 subtasks and PF09.5 shows HDE-FERM008 Done (E-09-4282, E-09-4283, E-09-4170). Surface: docs/acceptance_map_epic034.json; docs/acceptance_map_epic037.json; PF09.5 HDE-FERM008. bucket: not assigned |
| K-14-1811 | PF14 | 6888 | Source claim: L6888: 'IMP-01 records HDE-FERM007 implementation proof as not present.' Conflicting repository fact: HDE-FERM007 proof artifacts exist and PF09.5 shows it Done (E-09-4280, E-09-4168). Surface: artifacts/vendor/hdapi_v2/; PF09.5 HDE-FERM007. bucket: not assigned |
| K-14-1812 | PF14 | 6889 | Source claim: L6889: 'IMP-02 records HDE-FERM008 live conformance and open-rails proof as not present.' Conflicting repository fact: Later acceptance maps bind HDE-FERM008 subtasks; PF09.5 shows HDE-FERM008 Done (E-09-4282, E-09-4283, E-09-4170). Surface: docs/acceptance_map_epic034.json; docs/acceptance_map_epic037.json; PF09.5 HDE-FERM008. bucket: not assigned |
| K-14-1936 | PF14 | 7144 | Source claim: L7144: 'audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log'. Conflicting repository fact: Only the lower-case directory d03_showcompat_artifacts exists (N-12-4005, E-02-4020). Surface: audit/qa/hde-epic024/checks/. bucket: not assigned |
| K-14-1956 | PF14 | 7199 | Source claim: L7199: 'audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log'. Conflicting repository fact: Only the lower-case directory d05_arrays_as_sets exists (N-12-4005, E-02-4020). Surface: audit/qa/hde-epic024/checks/. bucket: not assigned |
| K-14-2090 | PF14 | 7653 | Source claim: L7653: 'python -m pytest -q tests/qa/test_epic022_close_pack_ready.py'. Conflicting repository fact: The test file is absent and retired (N-12-4007, E-10-4003). Surface: tests/qa/test_epic022_close_pack_ready.py. bucket: not assigned |
| P-A-013 | AGENTS.md | 31 | Source claim: "PF documents other than PF10 never cite PF10 by section, addendum number, heading, paragraph or version" (AGENTS.md:31). Conflicting repository fact: Non-PF10 PF documents carry PF10 addendum, section, version and file-name citations (E-02-2052, E-02-2053, E-02-2058, E-02-2059, E-02-2060, E-02-2061, E-02-2062). Surface: `docs/pfcanon/` documents other than PF10. bucket: not assigned. |
| P-A-094 | AGENTS.md | 111 | Source claim: "For HDE-CRD-0001, PF10 records the existing plan-wide hosted-CI override, including PR-01, PR-02 and PR-03" (AGENTS.md:111). Conflicting repository fact: PF10 v13.8.6 has no such record (E-02-2012, E-02-2013, N-12-2006, N-12-2007). Surface: PF10 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md`). bucket: not assigned. |
| P-A-196 | AGENTS.md | 179 | Source claim: "classifies configured v2 bases as `unsupported_runtime_nonclaim` before legacy `bodygraphs` request construction" (AGENTS.md:179). Conflicting repository fact: Configured v2 bases are classified adapter_backed_v2_chart and routed to the charts route (E-08-2002, E-11-688, E-11-689); the named classification is absent from runtime code (N-12-2005). Surface: `engine/bodygraph/vendor_client.py` route policy; `engine/bodygraph/resolver.py`. bucket: not assigned. |

### 12.2 `AGENTS.md` and `README.md` posture

- `AGENTS.md`, all 228 lines: Aligned 166, Partial 13, Drift 3, Unknown 27, Not a claim 37 (246 claims). Its three Drift rows, P-A-013, P-A-094 and P-A-196, are in the drift table of §12.1.B.
- `README.md`, all 255 lines: Aligned 273, Partial 18, Unknown 29, Not a claim 36 (356 claims). No row is Drift.

### 12.3 Historical comparison with PF23

The comparison list is every RA id in PF23 v1.2.2 §12 (the audit at `39b9cdf`) and every FND id in PF23 v1.2 (the audit at `71307d9`), as carried in the v1.2.2 §12 table: 18 RA ids and 25 FND ids. The statuses mean:

- **Persistent:** the observation still holds.
- **Resolved:** it no longer holds.
- **Changed:** it holds in a different form.
- **Unverifiable:** this audit cannot establish it.

| PF23 id | PF23 observation (short) | PF23 status | Now | Evidence | Note |
| :- | :- | :- | :- | :- | :- |
| RA-01 | Catalog, config, schemas, loader, roster 1.3.0/45 and core exist and agree | Aligned | Persistent | E-09-023, E-09-024, E-04-049, E-04-050, E-04-051, E-04-055, E-04-081, E-04-185, E-09-011 | Manifest 1.3.0 with 45 members equals the admitted roster; compare-goldens 8/8 match. |
| RA-02 | Reader v1 harmony-only, Reader v2 ten ordered items, POST /api/reader, governed 405 | Aligned | Persistent | E-04-290, E-04-292, E-06-063, E-05-125, E-05-122, E-05-127, E-05-126, E-11-230 | — |
| RA-03 | Evidence Index, Mirror, orientation, paths, canonical gate and manifest validators pass | Aligned | Persistent | E-09-001, E-09-002, E-09-003, E-09-004, E-09-005, E-09-006 | All rc 0 in a disposable clone (§9). |
| RA-04 | Wheel packaging omits release members (O-12) | Drift, carried | Persistent | E-03-901, E-03-902, E-03-903 | The built wheel lacks 16 of the 45 manifest members. |
| RA-05 | HTML 404 for unknown non-compat paths on two of three factories (O-P06a-22) | Drift, carried | Resolved | E-05-208, E-05-211, E-05-217, E-05-218, E-05-219, E-05-224, E-05-225 | All three live factories register 404 and 405 handlers that return JSON envelopes for every path. |
| RA-06 | Dev GET /reader treats unset APP_ENV as dev and refuses test; conjunction routes allow dev/test/local and refuse unset (O-P07-04) | Partial | Changed | E-05-129, E-05-130, E-05-131, E-11-239, E-11-240, E-05-147, E-05-148, E-11-564 | Dev GET /reader now requires APP_ENV exactly `dev` (unset is refused with 403); the conjunction and dev routes still allow dev/test/local. |
| RA-07 | showcompat help text says Reader v1 (O-P07-01); --band ignored with --pair-file (O-P07-02); dev harness calls app.getattr (O-P07-03) | Drift, carried | Resolved | E-07-901, E-07-032, E-11-499, N-03-019, E-05-031 | Help text now names `magic10_compat_result.v1`; `--band` replaces the file band (main.py:616-618); `dev/reader_harness/` is not tracked (the `app.getattr` copy exists only under `.audit_src/`). |
| RA-08 | 189 test files not named by a fixed lane or the roster; recorded pre-existing failures | Informational; not established as never run | Changed | E-10-012, E-10-612, E-10-626, E-10-901, E-10-902, E-10-903 | 215 test files now; the static union of CI tokens, roster and owner registry names all 215; whole-suite run has 1 failure (§10.11). |
| RA-09 | Security review did not cover implementation deltas in four units | Evidence limit | Unverifiable | N-12-916, N-12-917, E-02-016 | The PF10 records PF23 cited are not in PF10 v13.8.6; PF10 §2.3 deprecates the Codex security review; PR review history was not re-read. |
| RA-10 | Live Gate readiness against production rows never observed; open-rails QA step owed | Reserved for QA | Unverifiable | E-08-455 | No database probe is allowed in this audit; the tool's static facts are in §8.10. |
| RA-11 | bg:resolve output bypasses the LF/CRLF guard | Not established as a requirement | Persistent | E-11-639, E-11-640, E-11-388, E-11-389, E-11-390, N-06-004, N-06-005 | — |
| RA-12 | ci.yml paths-ignore (4) differs from _DOCUMENTATION_PREFIXES (8) | Drift (informational) | Resolved | E-10-174, E-10-175, E-10-177, E-10-184, E-10-191, E-10-193 | ci.yml now uses `paths` filters with the same eight documentation negations and three re-includes. |
| RA-13 | check_mirror_schema.sh is Python; AGENTS.md documents bash-style invocation | Drift (docs) | Resolved | E-10-686, E-10-2480, E-10-294, E-09-004, E-02-022, N-12-920 | The script is still Python (python3 shebang, mode 100755) and CI runs it by path; AGENTS.md names it by path on six lines and has no bash or sh invocation of it. |
| RA-14 | Registered routes absent from the endpoint catalog (aux, ops, healthz/readyz) | Persistent | Changed | E-05-457, E-05-485, E-05-486, E-05-465, N-05-029, E-09-033 | Catalog now 18 rows including aux narrative, /ops/rails/refusal and healthz/readyz; 12 written pairs have no row (non-POST /api/reader ×6, POST /reader, five retired /ops/* pairs); row HEAD /reader has no written pair. |
| RA-15 | Serializer relies on upstream validation for NaN; rebindable module globals; admission per call | Informational hazard | Persistent | N-06-001, N-12-905, E-04-245, E-04-351, N-04-013, N-12-904, E-04-250 | — |
| RA-16 | Root hygiene: zero-byte files, scratch files, placeholder channels_catalog_v1.json, duplicate hdctl scripts, pytest.ini scope differs from CI | Persistent / informational | Persistent | E-02-003, E-02-006, E-04-511, E-03-363, E-10-913, N-12-914 | — |
| RA-17 | PF10 v13.3.8 stored text truncated at line 1374; §2.27 missing from the Addendum Index | Defect (canon storage) | Resolved | E-02-018, E-02-012, E-02-013, E-02-014, N-02-002 | PF10 is now v13.8.6; its Addendum Index equals its 33 body headings and it ends with the authored marker `\<eof\>`. |
| RA-18 | Canon drainage of C040-05, -06, -07, -08 pending | Pending, non-gating | Changed | E-02-015, E-02-020 | PF10 v13.8.6 names C040-06/07/08 once (line 2952): PF04, PF05 and PF12 carry that content, and drainage into PF01 §§6.1–6.2 is listed as an open question. |
| FND-001 | Presenter component mapping: engine emitter and root Reader envelope builder split by namespace | Persistent | Persistent | E-06-016, E-06-023, E-06-025, E-06-026 | — |
| FND-002 | Compat blueprint under engine/http, mounted through adapter factories | Persistent | Persistent | E-05-118, E-05-037, E-05-041, E-05-045, E-11-266 | — |
| FND-003 | One hdctl registration dispatches the four engine.cli subcommands | Persistent | Persistent | E-03-021, N-12-907, E-07-030, E-07-031, E-07-053, E-07-063, E-07-075 | — |
| FND-004 | Human Index and Machine Mirror bind artifacts across several roots | Persistent | Persistent | E-02-008, E-09-020, E-09-021 | — |
| FND-005 | Compute and sanctioned I/O boundaries (bounded) | Persistent (bounded) | Persistent | N-04-023, N-04-024, N-04-025, E-04-431 | Own imports of the pure modules contain no forbidden item; their static closure is recorded in §4.9.4. |
| FND-006 | Top-level vendor/ Not found; transport is engine/bodygraph/vendor_client.py | Persistent | Persistent | N-12-908, E-08-183 | — |
| FND-007 | Direct DBAccess in engine/db with adapter facade | Persistent | Persistent | E-08-285, E-08-286, E-08-293 | — |
| FND-008 | Exact lowercase root names | Persistent | Persistent | E-02-002 | — |
| FND-009 | Producer/evidence root counts | Changed (docs 155→1508, audit 3049→3080, tests 302→316, engine 98→101) | Changed | E-02-002 | docs 2,567, audit 3,196, tests 255, engine 102 at this commit. |
| FND-010 | docs/ENDPOINTS_CATALOG.json is a symlink to the artifact catalog | Persistent | Persistent | E-02-005, E-05-450, E-05-451 | — |
| FND-011 | Procfile selects adapter.factory; adapter.wsgi.create_app is used by adapter/app.py | Persistent | Persistent | E-03-054, E-03-096, E-05-077, E-05-086 | — |
| FND-012 | assert and import are zero-byte tracked files | Persistent | Persistent | E-02-006 | — |
| FND-013 | Duplicate Reader category ids raise ValueError | Persistent | Persistent | E-06-060, E-06-061 | — |
| FND-014 | Truthful compatibility claims helper present | Persistent (presence only) | Persistent | E-10-918 | Presence only. |
| FND-015 | Ordinary CRD recording and governed publication present | Persistent (presence only) | Persistent | E-10-918, E-10-919 | Presence only. |
| FND-016 | Final operative documentation present | Persistent (presence only) | Persistent | E-02-021 | Presence only. |
| FND-017 | docs/ADAPTER_009.md retains body_not_allowed while code emits invalid_json | Persistent | Resolved | N-12-915, E-11-315 | `docs/ADAPTER_009.md` no longer names `body_not_allowed`. |
| FND-018 | Hosted CI outcomes | Unverifiable (hosted CI) | Changed | E-10-910, E-10-911, E-10-912, E-10-916 | Hosted CI was read: no run exists for the audited commit; the latest `main` run (head 1fb4731) failed; the 19 `main` push runs before it succeeded. |
| FND-019 | Permanent PF19 current-source wording | Resolved in PF19 v3.0.5 | Resolved | E-02-017 | PF19 v3.0.6 line 4253 keeps the SHA-alone wording. |
| FND-020 | docs/changes/GCFPE_PROMPT_PROVENANCE.md Not found | Persistent | Persistent | N-12-909 | — |
| FND-021 | Public paths reach compute_core only through compat/compute.py:346 | Changed | Persistent | N-12-911, E-04-911, E-11-131 | Same as recorded at 39b9cdf. |
| FND-022 | engine/charts/loader.py environment reads, timing, provider resolution and file logging | Persistent | Persistent | E-04-369, E-04-910, E-04-915, E-04-909, E-04-916 | — |
| FND-023 | audit/qa/hde-crd-0001 present (presence only) | Resolved | Resolved | E-09-026 | 23 files. |
| FND-024 | showcompat stdout is the magic10_compat_result.v1 document plus LF | Resolved at source level | Resolved | E-11-486, E-06-166, E-06-170 | — |
| FND-025 | Endpoint catalog lacks Aux and admin-bundle records | Persistent | Changed | E-09-033, E-05-480, N-12-912 | The aux record is now present (with `/api/aux/narrative` as alias); no row has `/internal/admin/bundle/v1`. |

PF23 ids compared: 43 of 43 (18 RA ids of PF23 v1.2.2 §12 and 25 FND ids of PF23 v1.2). Statuses: New 32, Persistent 25, Resolved 9, Changed 7, Unverifiable 2. This audit's RA observations with a PF23 predecessor are carried in that predecessor's row: RA-20261026-04 → RA-02, RA-20261026-06 → FND-018, RA-20261026-07 → RA-01, RA-20261026-08 → FND-022, RA-20261026-17 → FND-005, RA-20261026-20 → FND-005, RA-20261026-14 → RA-07. The 32 New rows of that count are this audit's observations that have no PF23 predecessor: the RA-20261026 rows of §12.1.A and the canon counts of §12.1.B.

### 12.4 PF23 item table

One row for every E- and N- id of PF23 v1.2.2 §§1–13. The results mean:

- **Same:** the statement still holds.
- **Changed:** it holds with different values.
- **Not found:** its subject is absent.
- **Unknown:** it cannot be established.

PF23's own ids (`E-A01` and so on) are PF23's; the last column gives this audit's evidence.

| PF23 id | PF23 statement (short) | Result | Old → new | Evidence |
| :- | :- | :- | :- | :- |
| N-00 | §1 prior-readiness proof: ls docs/ephemeral \| grep -iE 'EPIC040.*(reality\|triage\|readiness\|QA-10\|qa10)' → 0 files | Changed | 0 → 20 matching file names directly under docs/ephemeral (the four HDE-EPIC040-QA10-* records, eight QA100 checkpoint/handoff records, four QA100 results records, four QA90 handoff records) | E-02-010 |
| E-A01 | Tree clean at the audited commit (git status --porcelain → 0) | Same | — | E-03-002 |
| E-A02 | Tracked roots and file counts (39 directories) | Changed | 39 → 40 directories; `.claude/` added (9); `audit/` 3080 → 3196; `ci/` 13 → 14; `dev/` 4 → 2; `docs/` 1508 → 2567; `engine/` 101 → 102; `schemas/` 46 → 47; `tests/` 316 → 255; `tools/` 99 → 100; the other 30 directories have the same counts | E-02-002 |
| E-A02b | Root files include project docs, build/run files, EPIC023 step reports and the scratch files big.json, patch.diff, temp_run.*, .tmp_refusal_*.txt, changes_report.txt, manifest_pre.sha256, manifest_post.sha256 | Same | — | E-02-003 |
| E-A04 | assert, import and Run are zero-byte files | Same | — | E-02-006 |
| E-A03 | One tracked path contains an em dash (docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md) | Same | — | E-02-007, E-02-011 |
| E-A06 | docs/ second level: ephemeral 1268, graph 58, pfcanon 34, prompt_ecosystem_management 25, schemas 20, evidence 9, plans 8, design 8, run 6, adr 4, crd 3, qa 2 | Changed | ephemeral 1268 → 2319; prompt_ecosystem_management 25 → 32; adr 4 → 5; the other nine listed counts are the same. The audited commit has 18 second-level directories; the six not in PF23's list are acceptance 2, architecture 2, changes 2, contracts 2, ops 1, server 1 (PF23 does not say whether they existed at 39b9cdf) | E-02-004 |
| E-A07 | Evidence homes artifacts/ (1026), audit/ (3080), docs/evidence/, goldens/ (26); historical prefixes declared at classify_ci_changes.py:92 | Changed | audit/ 3080 → 3196; `_HISTORICAL_PREFIXES` now at classify_ci_changes.py:156–165; artifacts/ 1026 and goldens/ 26 unchanged; docs/evidence/ still holds the Index and sentinel | E-02-002, E-02-008, E-02-009 |
| E-A08 | pyproject.toml name, version 0.0.0, dependencies [], hdctl script, packages engine*/adapter*/presenter*/catalog*/math*, package-data catalog and math *.json | Same | — | E-03-014, E-03-015, E-03-019, E-03-021, E-03-024, E-03-026, E-03-027 |
| E-A12 | requirements.txt: psycopg[binary], Flask<3.0, gunicorn<22, jsonschema==4.23.0 | Same | — | E-03-040, E-03-041, E-03-042, E-03-043 |
| E-A13 | requirements-dev.txt adds pytest, pytest-cov, pytest-mock | Same | — | E-03-045, E-03-047, E-03-048, E-03-049 |
| E-A10 | Procfile:1 web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' … | Same | — | E-03-054, E-03-055 |
| E-A11 | Other create_app callers: run_flask.py:22, run_flask_dev.sh:21, scripts/start_web.sh:4, scripts/scratch.py:4, adapter/app.py (wsgi alias), dev/reader_harness/app.py:7 (own factory); scripts/dev_start_reader.sh:26 runs python -m adapter.http_reader | Changed | `dev/reader_harness/app.py` is no longer tracked (a copy remains at `.audit_src/dev/reader_harness/app.py:7`); every other listed caller is at the same line | E-03-114, E-03-122, E-03-111, E-11-1383, E-03-096, E-03-216, N-03-019, E-03-135 |
| E-A14 | Additional hdctl scripts: scripts/hdctl.py, scripts/hdctl.clean.py, scripts/hdctl.backup.py, scripts/hdctl.py.bak | Same | — | E-03-363 |
| N-A01 | No root Dockerfile*, setup.py or setup.cfg | Same | — (0; no tracked Dockerfile* anywhere) | N-12-901, N-03-008, N-03-010, N-03-011 |
| E-B-wheel | PF10 §2.22 records that a non-editable wheel omits 15 of the then-44 release members | Changed | A wheel built at the audited commit omits 16 of the 45 members (README.md:138 states the same 16 of 45) | E-03-901, E-03-902, E-03-903 |
| E-B01 | engine/ subpackages include bodygraph cli compat config core db magic10 mech presenter runtime serializer stable; engine/core/ holds only core.py | Changed | "engine/core/ holds only core.py" → `engine/core/` holds `__init__.py` and `core.py` (E-04-903). History at the pin: `engine/core/__init__.py` was first added in `c57d5b4b` on 2025-11-30 (E-04-901), before the PF23 audit commit `39b9cdf6` of 2026-09-27 (E-04-914), and no commit deletes it (N-04-901). The thirteen named subpackages are all among the 28 first-level directories of `engine/` (E-04-902) | E-04-901, E-04-902, E-04-903, E-04-914, E-04-019, E-04-177, N-04-901 |
| E-B02 | registry_loader.py:398-400 ADMITTED_RELEASE_VERSION "1.3.0", ADMITTED_RELEASE_BUILT_AT_UTC "2026-08-24T18:04:49Z", ADMITTED_RELEASE_ROSTER tuple(sorted({...})) | Same | — | E-04-576, E-04-577, E-04-578, E-09-024 |
| E-B03 | registry_loader.py:448-449 import-time invariant len(ADMITTED_RELEASE_ROSTER) != 45 → RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID") | Same | — | E-04-055, E-04-056, E-04-579 |
| E-B04 | _validate_admitted_manifest (1219–1242): strict subset → INCOMPLETE_RELEASE_ROSTER; other → RELEASE_ROSTER_MISMATCH; version/timestamp → RELEASE_VERSION_MISMATCH / RELEASE_TIMESTAMP_MISMATCH | Same | — (the function's last non-blank line is 1241; line 1242 is blank, E-04-906) | E-04-105, E-04-106, E-04-169, E-04-173, E-04-175, E-04-174, E-04-906, E-11-112 |
| E-B05 | registry_loader.py:478 SchemaValidationError('MISSING_FILE', …) | Same | — (inside `_safe_source_path`, defined at line 465) | E-04-904, E-04-093 |
| E-B06 | load_active_mechanics_bundle() (1506–1511): "Admit the exact installed complete mechanics release, or fail closed" | Same | — | E-04-081, E-04-082, E-04-083, E-04-084, E-11-105 |
| E-B07 | _deep_freeze maps Mapping → MappingProxyType, list/tuple → tuple; other types unchanged | Same | — | E-04-137, E-04-905, E-04-149, E-04-150, E-04-151 |
| E-B08 | CoreResult frozen/slots dataclass; compute_core at core.py:209 validates, classifies, computes signals, reduces categories, derives pair_key; errors collapse to ValueError("invalid pure core contract") | Same | — | E-04-907, E-04-183, E-04-185, E-04-186, E-04-204, E-04-187, E-04-188, E-11-132, E-11-151 |
| N-B01 | No I/O imports in engine/core engine/magic10 | Same | — (0) | N-12-903 |
| E-B09 | compute_core callers: engine/compat/compute.py:346; tools/config/artifacts.py:645-647, tools/evidence/generate_engine_core_evidence.py:120-123 | Same | — (the three non-test callers are unchanged; the caller scan also lists six test files and the `engine/core/__init__.py` re-export, E-04-308) | E-04-308, E-04-911, E-11-131, E-11-935 |
| E-B10 | Compat compute requires type(bundle) is AdmittedMechanicsBundle else CompatBoundaryError("admission_config"); intrinsic cache key INTRINSIC_CACHE_PREFIX + pair_key, hits revalidated | Same | — | E-04-908, E-04-264, E-04-265, E-04-912, E-04-913 |
| E-B11 | Module state: compute.py:50 _BUNDLE_PROVIDER (rebindable), compute.py:52 _SCHEMA_VALIDATORS dict (process cache keyed by schema SHA-256) | Same | — (no rebinding of `_BUNDLE_PROVIDER` inside `engine/`, N-04-017; 13 test files rebind it with `monkeypatch.setattr`, E-04-351) | E-04-245, E-04-247, E-04-274, E-04-351, N-04-017 |
| N-B02 | No lru_cache\|functools.cache in the named paths; admission runs on each provider call | Same | — (0) | N-12-904, N-11-001 |
| E-B25 | catalog/channels_v1.json: 36 Channels, gates ascending, 36 unique pairs, no null field | Same | — | E-04-835, N-04-547 |
| E-B26 | Config catalog/magic10_mechanics_v1.json (config_id m10-channel-state-v1.0.0) and its three schemas | Same | — | E-04-776, E-04-653, E-04-654, E-04-652 |
| E-B28 | 20 signals (schema pins min/max 20), 10 category weights, 3 profiles | Same | — | E-04-779, E-04-781, E-04-787, E-04-790 |
| E-B29 | Balance: equilibrium_score twice_min_owner_mass_v1, counterweight_ratio companionship_em_mass_v1; registry_loader.py:1168 SIGNAL_OPERATION_MISMATCH; signals.py:107 "invalid Balance operation" | Same | — | E-04-800, E-04-801, E-04-798, E-04-823 |
| E-B-cat | catalog/channels_catalog_v1.json holds one placeholder row; not a roster member; no .py under engine/tools references it | Same | — | E-04-511, N-04-501, N-04-502 |
| E-D26 | engine/charts/loader.py:54 reads SAFE_MODE; :71 writes loader_call.jsonl; :95/:168 perf_counter | Same | — | E-04-369, E-04-909, E-04-910 |
| E-C01 | adapter/factory.py:11-13 registers the dev blueprint at "", the API blueprint at /api and compat_blueprint | Changed | the three registrations moved from :11–13 to :13–15 (`create_app` stays at :11) | E-03-078, E-03-080, E-11-009, E-11-010, E-11-267 |
| E-C02 | adapter/factory.py after_request converts HTML 404/405 to JSON only for compat paths; no errorhandler | Changed | "no errorhandler" → `adapter/factory.py` registers `errorhandler(404)` (`:30`) and `errorhandler(405)` (`:35`), both returning the `ERR_NOT_FOUND` envelope for every path; its `after_request` (`:43`) still converts compat-path HTML 404/405 into the compat envelope and pops `ETag` on `/internal/` | E-05-208, E-05-209, E-05-210, E-05-211, E-05-212, E-05-213, E-05-214, E-05-215, E-05-216, E-11-1272, E-11-1275, E-11-1277 |
| E-C03 | adapter/http_reader.py:1163-1175 create_app mounts the same three | Changed | `adapter/http_reader.py:1163-1175` → `create_app` at `:1249` registers `bp` (`:1252`), `api_bp` at `/api` (`:1257`) and `compat_blueprint` (`:1260`); the three blueprints are the same | E-05-038, E-05-039, E-05-040, E-05-041, E-11-269 |
| E-C04 | http_reader.create_app 404/405 handlers return JSON only for /api/compat/v1, otherwise Werkzeug HTML | Changed | "JSON only for /api/compat/v1, otherwise Werkzeug HTML" → the 404 handler (`:1287`) returns the compat envelope for `/api/compat/v1` paths and the governed `ERR_NOT_FOUND` envelope for every other path; the 405 handler (`:1293`) splits the same way and sets `Allow` to the sorted valid methods | E-05-217, E-05-218, E-05-219, E-05-220, E-11-1280, E-11-1281 |
| E-C05 | adapter/wsgi.py:23-25 mounts the same three | Same | — | E-11-012, E-11-013, E-11-268 |
| E-C06 | wsgi global 404/405 → JSON ERR_NOT_FOUND | Same | — | E-05-224, E-05-225, E-11-1295, E-11-1296 |
| E-C07 | wsgi /internal/healthz, /internal/readyz; no-store default and HSTS for prod-like env (:28, :36-38) | Same | — (`no-store` by `setdefault` at `:28`; HSTS at `:38` when `APP_ENV`/`ENGINE_ENV` is `prod`, `production` or `live`, `:36`) | E-05-069, E-05-070, E-05-356, E-05-364, E-05-429, E-05-393, E-11-1298, E-11-1300 |
| E-C10 | http_reader.py:556 POST /api/reader → _production_reader_response | Changed | route :556 → :640 (handler :641 → `_production_reader_response` :525) | E-11-027, E-11-028, E-11-029, E-11-030 |
| E-C11 | :560 GET/HEAD/OPTIONS/PUT/PATCH/DELETE → governed 405 | Changed | :560 → :644 | E-11-227, E-11-228, E-11-229 |
| E-C12 | :574-584 before_request gives unrouted methods the same 405 | Changed | :574-584 → :648-665 (`_refuse_unrouted_methods`, installed at :665; hook :663) | E-11-024, E-11-025, E-11-026, E-11-233 |
| E-C13 | The 405 is ERR_NOT_FOUND, status 405, Cache-Control: no-store | Same | — | E-11-230, E-11-231, E-11-232, E-05-288, E-05-289 |
| E-C14 | _dev_admin_gate (:818-823) allows APP_ENV in {dev,test,local}; unset or other → ERR_WRITER_FORBIDDEN 403 | Changed | :818-823 → :901-907; behaviour the same | E-11-563, E-11-564, E-11-565 |
| E-C15 | Compat blueprint compat_handler.py:19 prefix /api/compat/v1; GET :122, POST :130, HEAD :176, OPTIONS :181 | Changed | prefix :19, GET :122 and POST :130 unchanged; HEAD :176 → :180; OPTIONS :181 → :185 | E-11-266, E-11-314, E-11-281, E-11-317, E-11-319 |
| E-C17 | docs/ENDPOINTS_CATALOG.json (symlink, byte-identical) has 10 rows, all matched by registered routes; registered but not catalogued: aux narrative ×2, four /ops/* routes, healthz/readyz, compat GET/HEAD/OPTIONS, 405-only refusals | Changed | 10 rows → 18 rows (symlink unchanged). 17 of 18 rows match a written route pair; row `HEAD /reader` matches none. Of the 30 written live pairs, 12 have no row: the six non-POST `/api/reader` methods, `POST /reader`, and five pairs on the three retired `/ops/*` paths. Aux narrative (with `/api/aux/narrative` as alias), `/ops/rails/refusal` GET/POST, `/internal/healthz`, `/internal/readyz` and compat GET/HEAD/OPTIONS now have rows | E-05-450, E-05-457, E-05-465, N-05-029, E-05-485, E-05-486, E-05-477, E-05-478, E-05-479, E-05-480, E-05-481, E-05-482, E-05-483, E-05-484, E-09-033 |
| E-B12 | presenter/reader_v1/emitter.py, presenter/json_canon_compare.py; engine/presenter/emitter.py (emit_public, emit_public_with_envelope, emit_compact_json) | Same | — | E-06-016, E-06-018, E-06-020, E-06-023, E-06-024, E-06-138 |
| E-B13 | Category items are exactly {id, band}; band checked against _CATEGORY_BANDS | Same | — | E-06-055, E-06-056, E-06-057, E-06-058, E-06-059 |
| E-D22 | Duplicate category id raises ValueError (emitter.py:41) | Same | — | E-06-060 |
| E-B14 | _ordered_categories_v2 (:48-62) requires ids equal FROZEN_MAGIC10_ORDER when eligible, [] when ineligible | Same | — | E-06-902, E-06-062, E-06-063 |
| E-B15 | engine/runtime/public.py:30-36 Reader v1 emits only harmony (or []); :94-100 dispatches v1/v2, else ValueError("reader_version_unsupported") | Same | — | E-06-902, E-06-070, E-06-071, E-06-072, E-04-289, E-06-067, E-06-068 |
| E-B16 | _emit (:105-112) hashes the five-key preimage into idempotence_hash | Same | — | E-06-902, E-06-025, E-06-026, E-06-027, E-06-028, E-06-029, E-06-065, E-06-066 |
| E-B17 | engine/stable/sercanon.py:21-28 json.dumps(…, ensure_ascii=False, compact separators, sort_keys=…) plus exactly one \n | Same | — | E-11-206, E-11-207, E-11-208 |
| N-B03 | allow_nan absent in engine/stable engine/serializer | Same | — (0) | N-12-905 |
| E-B18 | Call path: engine/cli/main.py → engine.runtime → emit_reader_v{1,2} → emit_public; also tools/config/artifacts.py:729-738 | Same | — (CLI: main.py:812 → engine.runtime.public.emit_reader_public_envelope → emit_reader_v1/v2 → emit_public; tools/config/artifacts.py:738 still calls emit_reader_v1) | E-11-470, E-11-186, E-11-192, E-11-193, E-11-194, E-11-199, E-11-941 |
| E-C18 | Sole console script hdctl → engine/cli/main.py:cli (:231) | Changed | sole script unchanged; `cli` :231 → :284 | E-03-021, E-03-029, N-12-907 |
| E-C19 | add_subparsers(required=True) (:76) | Changed | :76 → :91 | E-07-030 |
| E-C20 | showcompat help text: "Emit canonical Reader v1 bytes from vendor JSON (stdin or files)" | Changed | → "Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader" | E-07-032, E-07-901 |
| E-C22 | _emit_stdout_bytes (:511-516) raises STDOUT_MISSING_LF / STDOUT_CRLF | Changed | :511-516 → :570-575 | E-07-141, E-07-143, E-07-145 |
| E-D28 | showcompat stdout is the canonical magic10_compat_result.v1 document plus one LF (:765-767); the conjunction path wraps its result (compute.py:426) | Changed | main.py:765-767 → :829; compute.py:426 → :423 | E-07-147, E-11-486, E-04-277 |
| E-B19 | vendor_client.py:196-202 reads HD_API_BASE_URL / HDAPI_BASE_URL (conflict → PROVIDER_CONFIG_INVALID); :298 https required; :335 names HD_API_KEY | Changed | base-URL reads :197–200 (inside 196–202); https rule :297–298; HD_API_KEY named at :333 (was :335) | E-08-183, E-08-184, E-08-185, E-08-225, E-08-226, E-08-186 |
| E-B20 | :762-765 refuses unless SAFE_MODE=0 and ALLOW_NETWORK=1 (PROVIDER_REFUSED); no-redirect opener | Same | — | E-08-192, E-08-193, E-08-207, E-08-208, E-08-237, E-08-239 |
| E-B21 | engine/db/adapter.py:16-18 retired bridge keys; DBAccess.for_current_env (105–118) refuses them before provider construction | Same | — | E-08-286, E-11-048, E-11-049 |
| E-B22 | DATABASE_URL only (:119-142); provider PsycopgProvider | Same | — | E-08-285, E-08-293 |
| E-B23 | mapped_cache.py:19 posture adapter_mapped_no_raw_vendor_payload; persist_mapped_bodygraph (:60, PROVIDER_WRITE_UNSUPPORTED :89); read_current_mapped_bodygraph (:165) | Same | — | E-08-428, E-11-741, E-08-1901, E-08-442 |
| E-B24 | Readiness tool: docstring read-only declaration; "read_only": True (:82); DBAccess.for_current_env() (:217); refusals READINESS_EMPTY_SELECTION, READINESS_SELECTION_INVALID, READINESS_UNAVAILABLE; selection ≤ 1 MiB; require_closed_rails | Same | — | E-08-455, E-08-456, E-11-967, E-08-465, E-08-466, E-08-468, E-08-460, E-08-457 |
| N-B04 | No INSERT\|UPDATE\|DELETE\|persist_mapped\|commit\( in the readiness tool body below its docstring | Same | — (0) | N-12-906 |
| N-D01 | No top-level vendor/ | Same | — (0) | N-12-908 |
| E-D01 | update_evidence_index.py --check → rc 0 (env pins line) | Same | — | E-09-001 |
| E-D02 | orientation_demo.py --check → rc 0 | Same | — | E-09-002 |
| E-D03 | validate_evidence_paths.py → rc 0 | Same | — | E-09-003 |
| E-D04 | ./ci/checks/check_mirror_schema.sh → rc 0; via bash it fails rc 2; CI runs it directly (ci.yml:211) | Changed | rc 0 direct and rc 2 via bash unchanged; ci.yml line :211 → :232 | E-09-004, E-10-914 |
| E-D05 | release_id_recompute.py --check-manifest-only → rc 0 | Same | — | E-09-009 |
| E-D06 | run_canonical_json_gate.py --check-only → rc 0 | Same | — | E-09-010 |
| E-D07 | Human Index 606 rows, SHA-256 matches INDEX.sha256 | Changed | 606 → 653 rows; sentinel still matches | E-09-020 |
| E-D08 | Mirror 606 lines, matches its sentinel | Changed | 606 → 653 lines; sentinel still matches | E-09-021 |
| E-D09 | orientation total_artifacts: 606, status: ok | Changed | 606 → 653; status ok | E-09-022 |
| E-D10 | Last commit touching docs/evidence/INDEX.json: 3828d4b (PR01) | Changed | 3828d4b → 09e443f4 (2026-10-26) | E-09-035 |
| E-D11 | EPIC040-tagged rows: catalog.catalog_schema_validation, catalog.domain_closure_report | Changed | 2 → 16 rows with epic_id HDE-EPIC040 (the two named rows are still among them) | E-09-036 |
| E-D14 | catalog/manifest.json: version 1.3.0, built_at_utc 2026-08-24T18:04:49Z, 45 files, last changed 8999bd0 | Changed | version, timestamp and 45 files unchanged; last changed 8999bd0 → 822ce15c (2026-10-18) | E-09-023, E-09-037 |
| E-B27 | Manifest paths equal the roster literal exactly (45 45 True set()) | Same | — | E-09-024 |
| E-D15 | Endpoint catalog symlink, 10 rows, last changed d79cfc1 | Changed | still a symlink; 10 → 18 rows; last changed d79cfc1 → 2f3db0a0 (2026-10-18) | E-02-005, E-09-033, E-09-038 |
| E-D13 | goldens/ 26 files; artifacts/cards/a3/IDENTITY_OK.txt family present; artifacts/release_id.txt and artifacts/release_pack_manifest.json are frozen EPIC022 records per AGENTS.md | Same | — | E-09-029, E-09-039, E-09-030 |
| E-OPS | OPS01 evidence under audit/ops/hde-epic040/ops01/ with SHA256SUMS (7 of 7 OK); not promoted into the Index/Mirror | Same | — (re-verified: 7 of 7 OK; no Index row or Mirror line names the directory) | E-09-050, N-09-004, N-09-005 |
| E-DOC | DOC-20 §4 R6 records --compare-goldens . exit 0, 8 of 8 cases match (not re-executed by PF23) | Same | — (re-executed at the audited commit: exit 0, 8 of 8 match) | E-09-011 |
| E-PF10 | PF10 v13.3.8 line 1374 ends mid-word; the §1.1 Addendum Index lists 2.1–2.26 and omits §2.27 | Changed | PF10 v13.3.8 is no longer tracked; the tracked PF10 is v13.8.6, whose §1.1 index lists 2.1–2.33, equal to its body headings, and which ends with the authored marker `\<eof\>` | E-02-018, E-02-012, E-02-013, E-02-014 |
| E-A15 | tests/: 316 tracked files, 277 test_*.py | Changed | 316 → 255 files; 277 → 215 test_*.py | E-10-012 |
| E-A16 | pytest.ini testpaths lists 12 entries; it omits e.g. tests/order, tests/http | Changed | 12 → 80 entries (reaching 134 of 215 test files); still no tests/order or tests/http entry (2 and 6 test files there) | E-10-032, E-10-913, N-12-914 |
| E-A17 | tests/conftest.py only adjusts sys.path (no rails/network fixture); tests/provider/conftest.py:270 reads SAFE_MODE | Same | — | N-12-902, E-10-915, E-10-053 |
| N-A02 | ALLOW_NETWORK\|SAFE_MODE\|socket\|def pytest_\|ensure_determinism in tests/conftest.py → 0 | Same | — (0) | N-12-902 |
| E-A18 | ci.yml (399 lines): pull_request and push to main, paths-ignore of 4 documentation prefixes | Changed | 399 → 420 lines; `paths-ignore` (4 prefixes) → a `paths` filter on both triggers with `'**'`, the 8 documentation-prefix negations and 3 re-includes | E-10-009, E-10-174, E-10-175, E-10-188, E-10-191, E-10-193, N-10-021 |
| E-A19 | One test job: exact-head checkout (:43), lane classification, Python 3.12, changed tests in an isolated worktree under closed rails, lanes product/compat/db/rails/evidence/qa/release, final CI_APPLICABILITY_AND_EXACT_HEAD_OK (:399) | Changed | one `test` job (defined at :43) with exact-head checkout ref at :59; Python 3.12 (:85); final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK` :399 → :420; seven lanes unchanged | N-10-023, E-10-213, E-10-228, E-10-336, E-10-438 |
| E-A20 | epic-closeout-validation.yml is workflow_dispatch (only) | Changed | triggers are now `pull_request` (path-filtered) and `workflow_dispatch` | E-11-1119, E-11-1120, E-11-1121 |
| E-A22 | Classifier LANES (7) | Same | — (7 lanes: product, compat, db, rails, evidence, qa, release) | E-10-438, E-10-011 |
| E-A23 | _DOCUMENTATION_PREFIXES 8 entries (docs/crd/ … docs/run/) | Same | — | E-10-446, E-02-009 |
| E-A24 | _FULL_VALIDATION_SUPPLEMENTAL_TESTS 40 (all exist) | Changed | 40 → 109 entries, all tracked | E-10-442, E-10-571 |
| E-A26 | Of 277 test_*.py: 48 named by ci.yml tokens, 40 by the roster, 189 by neither; 145 outside the owner registry (134 paths) | Changed | 215 files; ci.yml tokens 37 exact / 49 with directories expanded; roster 109; owner registry 205 of 215; named by none 10 exact / 0 with directories expanded | E-10-612, E-10-616, E-10-617, E-10-619, E-10-620, E-10-621, E-10-622, E-10-626 |
| E-A25 | tools/qa/qa_harness.py governed statuses PASS, FAIL_BEHAVIOR, FAIL_TOOLING, TOOLING_BLOCKED, PARKED | Same | — | E-10-630, E-10-631, E-10-632, E-10-633, E-10-634, E-10-635 |
| E-REC | Recorded known failures (not re-executed): tests/reader_v1/test_cli_proof.py baseline failure (PF10 §2.24, §2.26 "476 passed, 1 failed"); PR05 sweep 57 failed, 546 passed, 13 errors | Changed | test_cli_proof.py is retired (tests/retired_tests.md); at the audited commit the testpaths run gives 3240 passed, 3 skipped, 0 failed, and the whole tests/ run gives 1 failed (tests/bodygraph/test_vendor_prod_override.py::test_record_and_streams_carry_no_subject_url_or_secret), 5855 passed; the latest hosted main run failed on one other test | E-10-165, E-10-901, E-10-902, E-10-903, E-10-911 |
| E-SEC | Security-review coverage recorded in PF10 §§2.19, 2.20, 2.22, 2.24, 2.26 (PR04/PR06 opened before code; PR05/PR06a at open only; PR06b on acae4c6, no finding) | Not found | The cited PF10 records are not in PF10 v13.8.6 (no `acae4c6`, no `PR06b`); PF10 v13.8.6 §2.3 deprecates the Codex security review | N-12-916, N-12-917, E-02-016 |
| E-D17 | (cited at PF23 L223 within the range "E-D17–E-D22"; no definition in PF23 v1.2.2) | Unknown | PF23 defines no claim for this id, so there is nothing to compare | N-12-918 |
| E-D18 | (cited at PF23 L223 within the range "E-D17–E-D22"; no definition in PF23 v1.2.2) | Unknown | PF23 defines no claim for this id, so there is nothing to compare | N-12-918 |
| E-D19 | (cited at PF23 L223 within the range "E-D17–E-D22"; no definition in PF23 v1.2.2) | Unknown | PF23 defines no claim for this id, so there is nothing to compare | N-12-918 |
| E-D20 | (cited at PF23 L223 within the range "E-D17–E-D22"; no definition in PF23 v1.2.2) | Unknown | PF23 defines no claim for this id, so there is nothing to compare | N-12-918 |
| E-D21 | FND-009 counts: docs 1508, audit 3080, tests 316, engine 101 | Changed | docs 1508 → 2567; audit 3080 → 3196; tests 316 → 255; engine 101 → 102 | E-02-002 |
| E-D12 | (cited at PF23 L223 within the range "E-D07–E-D12"; no definition in PF23 v1.2.2) | Unknown | PF23 defines no claim for this id, so there is nothing to compare | N-12-918 |
| N-D04 | server, adapters at the repository root → no such file | Same | — (0) | N-12-910 |
| E-D23 | docs/ADAPTER_009.md:174 says body_not_allowed; code emits invalid_json | Changed | `body_not_allowed` no longer occurs in docs/ADAPTER_009.md | N-12-915 |
| E-D24 | FND-019 resolved in PF19 v3.0.5 (SHA-alone wording) | Same | — (PF19 v3.0.6 line 4253 carries the wording) | E-02-017 |
| N-D02 | docs/changes/GCFPE_PROMPT_PROVENANCE.md → no such file | Same | — (0) | N-12-909 |
| N-D05 | \bcompute_core\b in engine/runtime/public.py, engine/http/compat_handler.py, engine/cli/main.py → 0 each | Same | — (0 each) | N-12-911 |
| E-D25 | Public paths reach compute_core through compat/compute.py:346 | Same | — | E-11-131, E-04-266 |
| E-D27 | audit/qa/hde-crd-0001 has 23 files | Same | — | E-09-026 |
| N-D06 | Catalog rows with path ∈ {/aux/narrative, /internal/admin/bundle/v1} → 0 (all 10 rows) | Changed | 0 → 1 of 18 rows: `/aux/narrative` is now a catalog path; `/internal/admin/bundle/v1` is still absent | E-09-033, N-12-912 |
| N-C01 | Extra entries under [project.scripts] → only hdctl | Same | — (only hdctl) | N-12-907 |
| N-D03 | aux\|admin, grep -ci, artifacts/audit/ENDPOINTS_CATALOG.json → 0 lines | Same | — as recorded (basic-regex `grep -ci 'aux\|admin'` treats `\|` literally and still finds 0 lines); with ERE alternation (`grep -ciE`) the catalog's single line matches | N-12-919, E-09-034 |
| N-PF10 | 7\.3\.9, open.rails QA, production rows in PF10 v13.3.8 → 0 | Not found | PF10 v13.3.8 is no longer tracked; the same pattern has 0 hits in PF10 v13.8.6 | N-12-913 |

Rows: 120, one for each PF23 E- and N- id. Results: Same 70, Changed 43, Not found 2, Unknown 5.

## 13. Negative-Claim Proof Appendix

Every N- id cited in this file. Each command runs from the repository root of a clean checkout of the pinned commit under closed rails. A `{W:<name>}` path is a helper script in the producer's session scratchpad. "Zero-hit reading" states exactly what returned zero.

| Id | Claim | Pattern | Tool | Case | Scope | Command | Result | Zero-hit reading |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| N-02-002 | No line of PF10 v13.8.6 ends with the fragment PF23 recorded as the v13.3.8 truncation (persistence remains p) | persistence remains p$ | grep -c -E | sensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `grep -c -E 'persistence remains p$' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` | `0` | 0 hits |
| N-03-008 | No tracked `Dockerfile*` | `(^\|/)dockerfile[^/]*$` | git ls-files \| grep -i -c -E | insensitive | all tracked paths | `git ls-files \| grep -i -c -E '(^\|/)dockerfile[^/]*$'` | `0` | 0 hits |
| N-03-010 | No tracked `setup.py` | `(^\|/)setup\.py$` | git ls-files \| grep -i -c -E | insensitive | all tracked paths | `git ls-files \| grep -i -c -E '(^\|/)setup\.py$'` | `0` | 0 hits |
| N-03-011 | No tracked `setup.cfg` | `(^\|/)setup\.cfg$` | git ls-files \| grep -i -c -E | insensitive | all tracked paths | `git ls-files \| grep -i -c -E '(^\|/)setup\.cfg$'` | `0` | 0 hits |
| N-03-015 | No code-type tracked file names `gunicorn.conf` (no `-c`/config reference) | `gunicorn.conf` | git grep -c -F | sensitive | tracked `*.py *.sh *.yml *.yaml *.toml *.cfg *.ini Procfile` | `git grep -c -F 'gunicorn.conf' -- '*.py' '*.sh' '*.yml' '*.yaml' '*.toml' '*.cfg' '*.ini' 'Procfile' \| LC_ALL=C awk -F: '{n++; s+=$NF} END{print n+0" files "s+0" lines"}'` | `0 files 0 lines` | 0 for every count shown |
| N-03-019 | No tracked path under `dev/reader_harness/` in the live tree | `dev/reader_harness` | git ls-files -- &lt;dir> \| wc -l | sensitive | pathspec `dev/reader_harness` | `git ls-files -- dev/reader_harness \| wc -l` | `0` | 0 hits |
| N-03-025 | `adapter/app.py` (the file `scripts/demo_mvp.sh:15` executes) contains no `__main__` guard and no `.run(` call | `__main__\|\.run\(` | grep -c -E | sensitive | `adapter/app.py` | `grep -c -E '__main__\|\.run\(' adapter/app.py` | `0` | 0 hits |
| N-03-033 | `scripts/hdctl.clean.py` is not named in `ci/checks/classify_ci_changes.py` | `hdctl.clean` | grep -c -F | sensitive | `ci/checks/classify_ci_changes.py` | `grep -c -F hdctl.clean ci/checks/classify_ci_changes.py` | `0` | 0 hits |
| N-04-009 | (stated where cited) | `Load-context Name references to each parameter inside the function body` | AST (unused_params.py) | exact identifier | engine/compat/compute.py conjunction_public (L396-428) | `python3 -I {W:w2-engine}/unused_params.py engine/compat/compute.py conjunction_public \| cut -f3` | `unused_params=viewer_top,viewer_weights,engine_tag,release_id,invocation_tag` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-013 | (stated where cited) | `lru_cache\|functools\.cache\|cached_property\|@cache` | git grep -E | case-sensitive | engine/ (all tracked files) | `git grep -n -E "lru_cache\|functools\.cache\|cached_property\|@cache" -- engine/ \| wc -l` | `0` | 0 hits |
| N-04-017 | (stated where cited) | `_BUNDLE_PROVIDER (word)` | git grep -w | case-sensitive | engine/ | `git grep -n -w _BUNDLE_PROVIDER -- engine/ \| cut -d: -f2 \| paste -sd, -` | `50,65,328` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-023 | (stated where cited) | `imports of engine.db, psycopg(2), urllib*, http/http.client, requests, socket, subprocess, flask, logging, any *.vendor_client; calls named open/fdopen, getenv, Path write APIs (write_text, write_bytes, mkdir, touch, unlink, rename, replace, rmdir, symlink_to, hardlink_to, chmod), logging file handlers/basicConfig; attribute .environ, names environ/getenv` | AST (purity_scan.py directsum) | exact identifiers | scope A: engine/core/__init__.py engine/core/core.py engine/magic10/__init__.py engine/magic10/calculators.py engine/magic10/composite.py engine/magic10/signals.py engine/magic10/thresholds.py | `python3 -I {W:w2-engine}/purity_scan.py directsum engine/core/__init__.py engine/core/core.py engine/magic10/__init__.py engine/magic10/calculators.py engine/magic10/composite.py engine/magic10/signals.py engine/magic10/thresholds.py` | `files=7 forbidden_hits=0 read_api_hits=1` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-024 | (stated where cited) | `same as scope A` | AST (purity_scan.py directsum) | exact identifiers | scope B: engine/bodygraph/gates.py engine/bodygraph/projection.py engine/bodygraph/v2_adapter.py engine/mech/compare.py engine/sampler/core.py engine/stable/sercanon.py | `python3 -I {W:w2-engine}/purity_scan.py directsum engine/bodygraph/gates.py engine/bodygraph/projection.py engine/bodygraph/v2_adapter.py engine/mech/compare.py engine/sampler/core.py engine/stable/sercanon.py` | `files=6 forbidden_hits=0 read_api_hits=0` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-025 | (stated where cited) | `same as scope A` | AST (purity_scan.py directsum) | exact identifiers | scope C: engine/compat/compute.py | `python3 -I {W:w2-engine}/purity_scan.py directsum engine/compat/compute.py` | `files=1 forbidden_hits=0 read_api_hits=1` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-501 | The 14 `catalog/` files not listed in `catalog/manifest.json` `files` (exact list printed) | `tracked catalog path not in manifest files[].path` | facts.py catalog_non_members (json parse + git ls-files) | sensitive | tracked files under `catalog/` vs `catalog/manifest.json` | `python3 -I {W:w1-pack-catalog}/facts.py catalog_non_members` | `members=11 non_members=14 catalog/__init__.py catalog/channels_catalog_v1.json catalog/manifest.json catalog/manifest.json.path_proof.txt catalog/narratives/keys.json.path_proof.txt catalog/narratives/keys.json.sha256 catalog/narratives/manifest.json.path_proof.txt catalog/narratives/manifest.json.sha256 catalog/narratives/palettes.json.path_proof.txt catalog/narratives/palettes.json.sha256 catalog/narratives/suppression_map.json.path_proof.txt catalog/narratives/suppression_map.json.sha256 catalog/narratives/templates.json.path_proof.txt catalog/narratives/templates.json.sha256` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-04-502 | No in-scope code-type file names `channels_catalog_v1` (neither the data file nor its schema is loaded by code) | `channels_catalog_v1` | git grep -c -F | sensitive | tracked `*.py *.sh *.yml *.yaml *.toml *.cfg *.ini Procfile` outside docs/, audit/, artifacts/ | `git grep -c -F channels_catalog_v1 -- '*.py' '*.sh' '*.yml' '*.yaml' '*.toml' '*.cfg' '*.ini' 'Procfile' ':(exclude)docs/' ':(exclude)audit/' ':(exclude)artifacts/' \| LC_ALL=C awk -F: '{n++; s+=$NF} END{print n+0" files "s+0" lines"}'` | `0 files 0 lines` | 0 for every count shown |
| N-04-547 | No Channel row field value is JSON `null` | `value is None` | python3 -I json parse | n/a | `catalog/channels_v1.json` `channels[*]` values | `python3 -I -c 'import json;print(sum(1 for r in json.load(open("catalog/channels_v1.json"))["channels"] for v in r.values() if v is None))'` | `0` | 0 hits |
| N-04-901 | No commit reachable from the pin deletes engine/core/__init__.py | --diff-filter=D | git log | n/a | history of engine/core/__init__.py reachable from the pin | `git log --diff-filter=D --format='%h' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- engine/core/__init__.py \| wc -l` | `0` | 0 hits |
| N-04-902 | Neither engine/runtime/public.py nor engine/compat/compute.py names ts_v0 or band_v0 (whole word) | ts_v0\|band_v0 | git grep -n -w -E | sensitive | engine/runtime/public.py engine/compat/compute.py | `git grep -n -w -E 'ts_v0\|band_v0' -- engine/runtime/public.py engine/compat/compute.py \| wc -l` | `0` | 0 hits |
| N-05-012 | The production Reader code path (lines 392-557) and `aux_narrative` (755-802) contain no `environ`/`getenv` text (DB selection inside `DBAccess.for_current_env()` lies outside the HTTP layer). | `environ\|getenv` | sed -n + grep -c -E | sensitive | adapter/http_reader.py:392-557,755-802 | `sed -n '392,557p;755,802p' adapter/http_reader.py \| grep -c -E 'environ\|getenv'` | `0` | 0 hits |
| N-05-013 | The `/internal/version` handler block (lines 1175-1196) reads no environment. | `environ\|getenv` | sed -n + grep -c -E | sensitive | adapter/http_reader.py:1175-1196 | `sed -n '1175,1196p' adapter/http_reader.py \| grep -c -E 'environ\|getenv'` | `0` | 0 hits |
| N-05-020 | No tracked .py outside .audit_src/ and _archive/ contains `etag_core`. | `etag_core` | git grep -n | sensitive | tracked *.py excluding .audit_src/, _archive/ | `git grep -n 'etag_core' -- '*.py' ':(exclude).audit_src/*' ':(exclude)_archive/*' \| wc -l` | `0` | 0 hits |
| N-05-029 | Only catalog row `HEAD /reader` lacks a written route pair. | `catalog rows vs written live pairs` | audit_http.py catalog | exact strings | artifacts/audit/ENDPOINTS_CATALOG.json vs live factories | `python3 -I {W:w3-http-presenter}/audit_http.py key catalog catalog_rows_without_written_pair` | `["HEAD /reader"]` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-05-030 | The `/ops/rails/refusal` handler block (lines 873-879) reads no environment. | `environ\|getenv` | sed -n + grep -c -E | sensitive | adapter/http_reader.py:873-879 | `sed -n '873,879p' adapter/http_reader.py \| grep -c -E 'environ\|getenv'` | `0` | 0 hits |
| N-05-031 | The `/internal/healthz` and `/internal/readyz` handler blocks (adapter/wsgi.py lines 41-51) read no environment. | `environ\|getenv` | sed -n + grep -c -E | sensitive | adapter/wsgi.py:41-51 | `sed -n '41,51p' adapter/wsgi.py \| grep -c -E 'environ\|getenv'` | `0` | 0 hits |
| N-06-001 | No tracked .py file contains the text `allow_nan`; hence no json.dumps/json.dump call or canonical function passes it. | `allow_nan` | git grep -n | sensitive | all tracked *.py files (888) | `git grep -n allow_nan -- '*.py' \| wc -l` | `0` | 0 hits |
| N-06-004 | `_emit_stdout_bytes(` occurs 3 times in engine/ (def :570, calls :801 and :829). | `_emit_stdout_bytes\(` | git grep -n -E | sensitive | engine/ | `git grep -n -E '_emit_stdout_bytes\(' -- engine/ \| cut -d: -f1,2 \| paste -sd ' ' -` | `engine/cli/main.py:570 engine/cli/main.py:801 engine/cli/main.py:829` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-06-005 | engine/cli/ has exactly five `sys.stdout.write(` / `sys.stdout.buffer.write(` calls. | `sys\.stdout\.(buffer\.)?write\(` | git grep -n -E | sensitive | engine/cli/ | `git grep -n -E 'sys\.stdout\.(buffer\.)?write\(' -- engine/cli/ \| cut -d: -f1,2 \| paste -sd ' ' -` | `engine/cli/main.py:280 engine/cli/main.py:288 engine/cli/main.py:575 engine/cli/main.py:645 engine/cli/main.py:925` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-09-002 | registry_report.json contains none of release_id, manifest.json, 77204764, built_at_utc, "version" | release_id\|manifest\.json\|77204764\|built_at_utc\|"version" | grep -c -E | sensitive | artifacts/registry/registry_report.json | `grep -c -E 'release_id\|manifest\.json\|77204764\|built_at_utc\|"version"' artifacts/registry/registry_report.json` | `0` | 0 hits |
| N-09-004 | No Human Index row binds a path under audit/ops/hde-epic040/ | audit/ops/hde-epic040/ | python3 -I json parse | sensitive | docs/evidence/INDEX.json (all 653 rows, every string value) | `python3 -I -c 'import json;d=json.load(open("docs/evidence/INDEX.json"));print(sum(1 for r in d if any(isinstance(v,str) and "audit/ops/hde-epic040/" in v for v in r.values())))'` | `0` | 0 hits |
| N-09-005 | No Machine Mirror line names a path under audit/ops/hde-epic040/ | audit/ops/hde-epic040/ | grep -c -F | sensitive | artifacts/evidence_index.jsonl | `grep -c -F 'audit/ops/hde-epic040/' artifacts/evidence_index.jsonl` | `0` | 0 hits |
| N-09-006 | catalog/manifest.json.path_proof.txt is named in neither the Human Index nor the Machine Mirror | catalog/manifest.json.path_proof.txt | grep -c -F | sensitive | docs/evidence/INDEX.json artifacts/evidence_index.jsonl | `grep -c -F 'catalog/manifest.json.path_proof.txt' docs/evidence/INDEX.json artifacts/evidence_index.jsonl \| cut -d: -f2 \| paste -sd'\|' -` | `0\|0` | 0 for every count shown |
| N-10-021 | (stated where cited) | `paths-ignore` | grep -c | case-sensitive | .github/workflows/ci.yml, .github/workflows/epic-closeout-validation.yml | `grep -c 'paths-ignore' .github/workflows/ci.yml .github/workflows/epic-closeout-validation.yml \| paste -sd' ' -` | `.github/workflows/ci.yml:0 .github/workflows/epic-closeout-validation.yml:0` | 0 for every count shown |
| N-10-023 | (stated where cited) | `` two-space-indented keys after `jobs:` (every job id) `` | awk | case-sensitive | .github/workflows/ci.yml | `awk '/^jobs:/{j=1;next} j && /^  [A-Za-z0-9_-]+:/{sub(/^  /,""); print NR":"$0}' .github/workflows/ci.yml \| paste -sd' ' -` | `43:test:` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-11-001 | engine/config/registry_loader.py uses no lru_cache / functools memoization | lru_cache\|functools | grep -n -E | sensitive | engine/config/registry_loader.py | `grep -n -E 'lru_cache\|functools' engine/config/registry_loader.py \| wc -l` | `0` | 0 hits |
| N-11-008 | classify_bg_resolve_route_policy returns no error_code key | error_code | sed + grep -c | sensitive | engine/bodygraph/vendor_client.py lines 124-153 | `sed -n '124,153p' engine/bodygraph/vendor_client.py \| grep -c error_code` | `0` | 0 hits |
| N-11-013 | check_magic10_gate_readiness.py defines no --report option | --report | grep -c | sensitive | tools/bodygraph/check_magic10_gate_readiness.py | `grep -c -- '--report' tools/bodygraph/check_magic10_gate_readiness.py` | `0` | 0 hits |
| N-11-016 | generate_epic_close_pack.py declares exactly two mode flags (--write, --check) in one required mutually exclusive group | mode.add_argument( | grep -c | sensitive | tools/qa/generate_epic_close_pack.py | `grep -c 'mode.add_argument(' tools/qa/generate_epic_close_pack.py` | `2` | Exact count: 0 beyond the 2 counted |
| N-11-028 | No tracked file exists under dev/reader_harness | dev/reader_harness | git ls-files | sensitive | dev/reader_harness | `git ls-files -- dev/reader_harness \| wc -l` | `0` | 0 hits |
| N-12-901 | No tracked Dockerfile*, setup.py or setup.cfg at the root, and no tracked Dockerfile* anywhere (PF23 N-A01) | Dockerfile*, setup.py, setup.cfg | git ls-files; grep -c -E | sensitive | repository root; whole index for Dockerfile* | `git ls-files -- Dockerfile 'Dockerfile*' setup.py setup.cfg \| wc -l; git ls-files \| grep -cE '(^\|/)Dockerfile[^/]*$'` | `0\|0` | 0 for every count shown |
| N-12-902 | tests/conftest.py names none of ALLOW_NETWORK, SAFE_MODE, socket, def pytest_, ensure_determinism (PF23 N-A02) | ALLOW_NETWORK\|SAFE_MODE\|socket\|def pytest_\|ensure_determinism | grep -c -E | sensitive | tests/conftest.py | `grep -cE 'ALLOW_NETWORK\|SAFE_MODE\|socket\|def pytest_\|ensure_determinism' tests/conftest.py` | `0` | 0 hits |
| N-12-903 | No I/O import names in engine/core and engine/magic10 (PF23 N-B01) | import engine.db\|from engine.db\|vendor_client\|urllib\|psycopg | grep -rn -E \| wc -l | sensitive | engine/core engine/magic10 | `grep -rnE 'import engine.db\|from engine.db\|vendor_client\|urllib\|psycopg' engine/core engine/magic10 \| wc -l` | `0` | 0 hits |
| N-12-904 | No lru_cache or functools.cache in the PF23 N-B02 scope (PF23 N-B02) | lru_cache\|functools.cache | grep -rn -E \| wc -l | sensitive | engine/config engine/core engine/magic10 presenter engine/presenter engine/runtime/public.py | `grep -rnE 'lru_cache\|functools.cache' engine/config engine/core engine/magic10 presenter engine/presenter engine/runtime/public.py \| wc -l` | `0` | 0 hits |
| N-12-905 | allow_nan does not occur in engine/stable or engine/serializer (PF23 N-B03) | allow_nan | grep -rn \| wc -l | sensitive | engine/stable engine/serializer | `grep -rn 'allow_nan' engine/stable engine/serializer \| wc -l` | `0` | 0 hits |
| N-12-906 | The readiness tool body below its docstring (line 23 on) has no INSERT, UPDATE, DELETE, persist_mapped or commit( (PF23 N-B04) | INSERT\|UPDATE\|DELETE\|persist_mapped\|commit\( | sed -n + grep -c -E | sensitive | tools/bodygraph/check_magic10_gate_readiness.py lines 23–end | `sed -n '23,$p' tools/bodygraph/check_magic10_gate_readiness.py \| grep -cE 'INSERT\|UPDATE\|DELETE\|persist_mapped\|commit\('` | `0` | 0 hits |
| N-12-907 | pyproject.toml [project.scripts] holds only hdctl (PF23 N-C01) | non-empty lines in [project.scripts] | awk | sensitive | pyproject.toml | `awk '/^\[project.scripts\]/{f=1;next} /^\[/{f=0} f&&NF' pyproject.toml` | `hdctl = "engine.cli.main:cli"` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-12-908 | No tracked top-level vendor/ (PF23 N-D01) | vendor | git ls-files | sensitive | vendor | `git ls-files -- vendor \| wc -l` | `0` | 0 hits |
| N-12-909 | docs/changes/GCFPE_PROMPT_PROVENANCE.md is not tracked (PF23 N-D02) | exact path | git ls-files | sensitive | exact path | `git ls-files -- docs/changes/GCFPE_PROMPT_PROVENANCE.md \| wc -l` | `0` | 0 hits |
| N-12-910 | No tracked top-level server/ or adapters/ (PF23 N-D04) | server, adapters | git ls-files | sensitive | server adapters | `git ls-files -- server adapters \| wc -l` | `0` | 0 hits |
| N-12-911 | compute_core (whole word) does not occur in the three public-path files (PF23 N-D05) | compute_core | grep -cw | sensitive | engine/runtime/public.py engine/http/compat_handler.py engine/cli/main.py | `for f in engine/runtime/public.py engine/http/compat_handler.py engine/cli/main.py; do printf '%s=%s\n' $f $(grep -cw compute_core $f); done \| paste -sd ' ' -` | `engine/runtime/public.py=0 engine/http/compat_handler.py=0 engine/cli/main.py=0` | 0 for every count shown |
| N-12-912 | No endpoint-catalog row has path /internal/admin/bundle/v1 (PF23 N-D06, admin-bundle half) | path == /internal/admin/bundle/v1 | python3 -I json parse | sensitive | artifacts/audit/ENDPOINTS_CATALOG.json, all 18 "endpoints" rows | `python3 -I -c 'import json;e=json.load(open("artifacts/audit/ENDPOINTS_CATALOG.json"))["endpoints"];print(len(e), sum(1 for r in e if r.get("path")=="/internal/admin/bundle/v1"))'` | `18 0` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-12-913 | PF10 v13.3.8 is not tracked, and the PF23 N-PF10 pattern has no hit in PF10 v13.8.6 (PF23 N-PF10) | 7\.3\.9\|open.rails QA\|production rows | git ls-files; grep -c -i -E | insensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.3.8.md; docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `git ls-files -- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.8.md \| wc -l; grep -ciE '7\.3\.9\|open.rails QA\|production rows' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` | `0\|0` | 0 for every count shown |
| N-12-914 | pytest.ini names no path under tests/order or tests/http (PF23 E-A16) | tests/(order\|http) | grep -c -E | sensitive | pytest.ini | `grep -c -E 'tests/(order\|http)' pytest.ini` | `0` | 0 hits |
| N-12-915 | docs/ADAPTER_009.md no longer names body_not_allowed (PF23 FND-017 / E-D23) | body_not_allowed | grep -c | sensitive | docs/ADAPTER_009.md | `grep -c body_not_allowed docs/ADAPTER_009.md` | `0` | 0 hits |
| N-12-916 | PF10 v13.8.6 does not contain the commit prefix acae4c6 (PF23 E-SEC source) | acae4c6 | grep -c -F | sensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `grep -c -F acae4c6 docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` | `0` | 0 hits |
| N-12-917 | PF10 v13.8.6 does not contain the string PR06b (PF23 E-SEC source) | PR06b | grep -c -F | sensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `grep -c -F PR06b docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` | `0` | 0 hits |
| N-12-918 | PF23 v1.2.2 has no definition bullet for E-D12, E-D17, E-D18, E-D19 or E-D20 | ^\* E-D(12\|17\|18\|19\|20)\b | grep -c -E | sensitive | docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.2.md | `grep -c -E '^\* E-D(12\|17\|18\|19\|20)\b' docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.2.md` | `0` | 0 hits |
| N-12-919 | PF23 N-D03 re-run exactly as recorded (basic-regex grep -ci with the literal pattern aux\|admin) finds no line | aux\|admin (basic regex: literal bar) | grep -ci | insensitive | artifacts/audit/ENDPOINTS_CATALOG.json | `grep -ci 'aux\|admin' artifacts/audit/ENDPOINTS_CATALOG.json` | `0` | 0 hits |
| N-12-920 | AGENTS.md at PINNED names ci/checks/check_mirror_schema.sh by path only: no line runs it through bash or sh | (bash\|sh) +ci/checks/check_mirror_schema | git show + grep -c -E | sensitive | AGENTS.md at 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b (228 lines) | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:AGENTS.md \| grep -c -E '(bash\|sh) +ci/checks/check_mirror_schema'` | `0` | 0 hits |
| N-12-2005 | The runtime code has no unsupported_runtime_nonclaim classification | `unsupported_runtime_nonclaim` | git grep -l -F | sensitive | engine/ adapter/ presenter/ at PINNED | `git grep -l -F 'unsupported_runtime_nonclaim' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- engine adapter presenter \| wc -l` | `0` | 0 hits |
| N-12-2006 | No PF10 line that names HDE-CRD-0001 mentions hosted CI, an override, a waiver, unavailability or non-blocking status | `HDE-CRD-0001 then hosted\|override\|waiver\|unavailab\|non-blocking` | git show + grep -F + grep -c -i -E | sensitive then insensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md at PINNED | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -F 'HDE-CRD-0001' \| grep -c -i -E 'hosted\|override\|waiver\|unavailab\|non-blocking'` | `0` | 0 hits |
| N-12-2007 | PF10 contains no "plan-wide" text | `plan-wide` | git show + grep -c -i -F | insensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md at PINNED | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -c -i -F 'plan-wide'` | `0` | 0 hits |
| N-12-2803 | No ERR_AUX token in code, schemas or token map | `ERR_AUX` | git grep -n | sensitive | engine adapter presenter schemas errors | `git grep -n 'ERR_AUX' -- engine adapter presenter schemas errors \| wc -l` | `0` | 0 hits |
| N-12-2804 | No admin-bundle command or route in code | `admin-bundle\|admin_bundle\|/internal/admin/bundle` | git grep -n -E | sensitive | engine adapter presenter | `git grep -n -E 'admin-bundle\|admin_bundle\|/internal/admin/bundle' -- engine adapter presenter \| wc -l` | `0` | 0 hits |
| N-12-2805 | No schemas/admin_bundle* file | `schemas/admin_bundle*` | git ls-files | sensitive | schemas/ | `git ls-files 'schemas/admin_bundle*' \| wc -l` | `0` | 0 hits |
| N-12-2806 | No /_ops/bodygraph/resolve route in code or in the Endpoint Catalog | `_ops/bodygraph` | git grep -n | sensitive | engine adapter presenter docs/ENDPOINTS_CATALOG.json | `git grep -n '_ops/bodygraph' -- engine adapter presenter docs/ENDPOINTS_CATALOG.json \| wc -l` | `0` | 0 hits |
| N-12-2807 | dev/reader_harness/ is absent at PINNED | `dev/reader_harness` | git ls-tree -r --name-only | sensitive | tree of PINNED under dev/reader_harness | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- dev/reader_harness \| wc -l` | `0` | 0 hits |
| N-12-2810 | Catalog has no /internal/admin/bundle/v1 record | `/internal/admin/bundle` | grep -c | sensitive | docs/ENDPOINTS_CATALOG.json (one line) | `grep -c '/internal/admin/bundle' docs/ENDPOINTS_CATALOG.json` | `0` | 0 hits |
| N-12-2811 | The Aux handler reads no v query value | `args.(get\|getlist)("v"` | awk + grep -c -E | sensitive | adapter/http_reader.py lines 755-802 | `awk 'NR>=755 && NR<=802' adapter/http_reader.py \| grep -c -E 'args\.(get\|getlist)\("v"'` | `0` | 0 hits |
| N-12-2812 | No PROVIDER_ROUTE_UNSUPPORTED code in code | `PROVIDER_ROUTE_UNSUPPORTED` | git grep -n | sensitive | engine adapter | `git grep -n 'PROVIDER_ROUTE_UNSUPPORTED' -- engine adapter \| wc -l` | `0` | 0 hits |
| N-12-2815 | None of 13 named options exists in the packaged parser | `--stdin --a-user --b-user --file --viewer-prefs --compat-format --admin-sidecar --export-dir --from-bodygraph --lat --lng --a-tz --b-tz` | python3 -I ast inventory (own script) | sensitive (exact strings) | engine/cli/main.py add_argument calls | `python3 -I {W:c1-pf02-pf05}/cli_inventory.py absent --stdin --a-user --b-user --file --viewer-prefs --compat-format --admin-sidecar --export-dir --from-bodygraph --lat --lng --a-tz --b-tz` | `absent=13/13` | Exhaustive result: 0 hits outside those listed; any count shown as 0 is zero |
| N-12-2829 | artifacts/cli/transport/ (both harness-header logs) is absent | `artifacts/cli/transport` | git ls-files | sensitive | artifacts/cli/transport/ | `git ls-files artifacts/cli/transport \| wc -l` | `0` | 0 hits |
| N-12-3604 | run_sanity_pipeline.py mentions neither the sampler nor the Engine Core generator | `sampler\|engine_core` | git grep -i -E \| wc -l | insensitive | tools/evidence/run_sanity_pipeline.py | `git grep -i -E 'sampler\|engine_core' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- tools/evidence/run_sanity_pipeline.py \| wc -l` | `0` | 0 hits |
| N-12-3606 | No tracked file under the mixed-case directory D01_env_pins_gate/ | `D01_env_pins_gate/` | git ls-tree -r \| wc -l | sensitive (Git paths) | audit/qa/hde-epic024/checks/D01_env_pins_gate/ | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- audit/qa/hde-epic024/checks/D01_env_pins_gate/ \| wc -l` | `0` | 0 hits |
| N-12-3608 | PF10 v13.8.6 has no line with the CRD-0001 header-helper / harness-publication terms | `header-helper\|header helper\|step_log_header\|write_header\|publish_crd_check_family\|composed publication` | git show \| grep -c -i -E | insensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -c -i -E 'header-helper\|header helper\|step_log_header\|write_header\|publish_crd_check_family\|composed publication'` | `0` | 0 hits |
| N-12-3629 | adapter/http_reader.py contains no 0.0.0.0 | `0.0.0.0` | git show \| grep -c -F | sensitive | adapter/http_reader.py | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:adapter/http_reader.py \| grep -c -F '0.0.0.0'` | `0` | 0 hits |
| N-12-3635 | audit/EPIC-030_QA_RCA.md contains no root-cause, proof-class or timeline text | `root cause\|proof-class\|timeline` | git show \| grep -c -i -E | insensitive | audit/EPIC-030_QA_RCA.md | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:audit/EPIC-030_QA_RCA.md \| grep -c -i -E 'root cause\|proof-class\|timeline'` | `0` | 0 hits |
| N-12-3636 | No EPIC030 QA/OPS record, RCA or close report contains READY WITH CAVEATS | `READY WITH CAVEATS` | git grep -l -F \| wc -l | sensitive | audit/qa/hde-epic030/ audit/ops/hde-epic030/ audit/EPIC-030_QA_RCA.md audit/EPIC-030_close_report.md | `git grep -l -F 'READY WITH CAVEATS' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- audit/qa/hde-epic030 audit/ops/hde-epic030 audit/EPIC-030_QA_RCA.md audit/EPIC-030_close_report.md \| wc -l` | `0` | 0 hits |
| N-12-3639 | PF10 v13.8.6 does not mention HDE-EPIC030 | `HDE-EPIC030` | git show \| grep -c -F | sensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -c -F 'HDE-EPIC030'` | `0` | 0 hits |
| N-12-4002 | tools/evidence/generate_db_bridge_parity.py and tests/evidence/test_generate_db_bridge_parity_nondev.py are absent at PINNED | `the two exact paths` | git ls-tree -r --name-only | exact path (case-sensitive) | commit tree at PINNED | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- tools/evidence/generate_db_bridge_parity.py tests/evidence/test_generate_db_bridge_parity_nondev.py \| wc -l` | `0` | 0 hits |
| N-12-4005 | The mixed-case paths audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log and .../D05_arrays_as_sets/primary.log are absent at PINNED | `the two exact mixed-case paths` | git ls-tree -r --name-only | exact path (case-sensitive) | commit tree at PINNED | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- audit/qa/hde-epic024/checks/D03_showcompat_artifacts/primary.log audit/qa/hde-epic024/checks/D05_arrays_as_sets/primary.log \| wc -l` | `0` | 0 hits |
| N-12-4007 | tests/qa/test_epic022_close_pack_ready.py is absent at PINNED | `the exact path` | git ls-tree -r --name-only | exact path (case-sensitive) | commit tree at PINNED | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- tests/qa/test_epic022_close_pack_ready.py \| wc -l` | `0` | 0 hits |
| N-12-4010 | No file under engine/db/ or tests/db/ contains the word live at PINNED | `live (whole word)` | git grep -l -w | case-sensitive | engine/db/ tests/db/ at PINNED | `git grep -l -w live 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- engine/db tests/db \| wc -l` | `0` | 0 hits |
| N-12-4014 | PF10 at PINNED contains none of EPIC032, DB_PROVIDER_PARITY_OK, HDE-FERM004.2, selection_order, NARR_REGISTRY_CLOSURE_OK | `EPIC032 \| DB_PROVIDER_PARITY_OK \| HDE-FERM004.2 \| selection_order \| NARR_REGISTRY_CLOSURE_OK` | grep -c -e | case-sensitive | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md at PINNED | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -c -e EPIC032 -e DB_PROVIDER_PARITY_OK -e HDE-FERM004.2 -e selection_order -e NARR_REGISTRY_CLOSURE_OK` | `0` | 0 hits |

## Evidence list

Every E- id cited in this file, with its file and line at the pinned commit and a verbatim excerpt, or its command and result. `{SCRATCH}` is the producer's session scratchpad and `{W:<name>}` a worker's directory in it. The helper scripts those commands call are in the working record, not in this file. Cells longer than 200 characters are cut, and the cut is marked `…`.

| Id | Citation | Excerpt or result |
| :- | :- | :- |
| E-02-001 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^(TRACKED_TOTAL\|MODES) ' \| paste -sd';' -` | `TRACKED_TOTAL 8374;MODES {'100644': 8235, '100755': 137, '120000': 2}` |
| E-02-002 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^ROOT_DIRS ' ` | `ROOT_DIRS 40` |
| E-02-003 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^ROOT_FILES '` | `ROOT_FILES 57` |
| E-02-004 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^DOCS_(SECOND_LEVEL_DIRS\|ROOT_FILES) ' \| paste -sd';' -` | `DOCS_SECOND_LEVEL_DIRS 18;DOCS_ROOT_FILES 53` |
| E-02-005 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^(SYMLINKS\|LINK)' \| paste -sd';' -` | `SYMLINKS 2;LINK	artifacts/ops/internal_version/body_get.json.sha256	->	body_get.sha256;LINK	docs/ENDPOINTS_CATALOG.json	->	../artifacts/audit/ENDPOINTS_CATALOG.json` |
| E-02-006 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^ZERO_BYTE '` | `ZERO_BYTE 344` |
| E-02-007 | `python3 -I {SCRATCH}/scripts/s2_map.py /home/user/glow-hdengine-v2 \| grep -E '^NONASCII_OR_SPACE '` | `NONASCII_OR_SPACE 50 nonascii 1 space 50` |
| E-02-008 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^HUMAN_INDEX (rows with\|top-level)' \| paste -sd';' -; git ls-files \| grep -E '\.path_proof\.txt$' \| cut -d/ -f1 \| sort \| …` | `HUMAN_INDEX rows with discovered_physical_path 653 distinct 639;HUMAN_INDEX top-level dirs of paths {'artifacts': 248, 'audit': 338, 'catalog': 5, 'docs': 31, 'errors': 5, 'notes': 1, 'parity': 8, 's…` |
| E-02-009 | `grep -n -E '^_(HISTORICAL_PREFIXES\|HISTORICAL_PATHS\|DOCUMENTATION_PREFIXES\|DOCUMENT_SUFFIXES\|DOCUMENT_PATHS)' ci/checks/classify_ci_changes.py \| cut -d'=' -f1 \| paste -sd';' -` | `156:_HISTORICAL_PREFIXES ;166:_HISTORICAL_PATHS ;171:_DOCUMENTATION_PREFIXES ;181:_DOCUMENT_SUFFIXES ;182:_DOCUMENT_PATHS` |
| E-02-010 | `git ls-files -- docs/ephemeral \| sed 's#^docs/ephemeral/##' \| grep -v / \| grep -ciE 'EPIC040.*(reality\|triage\|readiness\|QA-10\|qa10)'` | `20` |
| E-02-011 | `git ls-files -z -- 'docs/ephemeral/GCFPE Direct-Handoff*' \| tr '\0' '\n'` | `docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md` |
| E-02-012 | `printf '%s %s\n' "$(wc -c < docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md)" "$(sha256sum docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| cut -c1-64)"` | `692581 e521bf2ea8705862260f4d84100e01dddd78b07b8437751aa419a51b41c1b985` |
| E-02-013 | `a=$(sed -n '1,221p' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -oE '^\* 2\.[0-9]+ ' \| sed 's/^\* //;s/ $//' \| sort -t. -k2,2n \| paste -sd ' ' -); b=$(grep -oE '^## (\*\*)?2\.[0-9]+ ' docs/pf…` | `equal 33 first=2.1 last=2.33` |
| E-02-014 | `tail -c 7 docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` | `\<eof\>` |
| E-02-015 | `grep -n 'C040-0[5-8]' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| cut -d: -f1 \| paste -sd ' ' -` | `2952` |
| E-02-016 | `grep -n '^## 2.3 Codex security review is deprecated' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| cut -d: -f1` | `336` |
| E-02-017 | `sed -n '4253p' docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md \| grep -c -F 'A changed, different or unavailable SHA alone must never block progression'` | `1` |
| E-02-018 | `git ls-files -- 'docs/pfcanon/PF10*' \| paste -sd ' ' -` | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` |
| E-02-020 | `sed -n '2952p' docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -c -F 'whether C040 drainage into PF01 §§6.1–6.2 is complete (open question; PF04, PF05 and PF12 carry the C040-06/07/08 content)'` | `1` |
| E-02-021 | `git ls-files -- AGENTS.md docs/qa_harness_pattern.md docs/ADAPTER_009.md docs/acceptance/http_transport_evidence.md \| paste -sd' ' -` | `AGENTS.md docs/ADAPTER_009.md docs/acceptance/http_transport_evidence.md docs/qa_harness_pattern.md` |
| E-02-022 | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:AGENTS.md \| grep -n -F 'ci/checks/check_mirror_schema.sh' \| cut -d: -f1 \| paste -sd' ' -` | `46 93 94 162 168 175` |
| E-02-932 | `git rev-list --count 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b..9d9fcca0f2141b23a6200dcafcfb40d401c523f3` | `4` |
| E-02-933 | `git diff --name-status 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b 9d9fcca0f2141b23a6200dcafcfb40d401c523f3 \| cut -f1 \| sort \| uniq -c \| sed 's/^ *//' \| paste -sd' ' -; git diff --name-only 0adce9d9c7c8…` | `56 A 1 R094\|56 docs/ephemeral 1 docs/pfcanon` |
| E-02-934 | `git diff --name-status 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b 9d9fcca0f2141b23a6200dcafcfb40d401c523f3 -- docs/pfcanon/ \| tr '\t' ' '` | `R094 docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` |
| E-02-2012 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:4` | `**Version: v13.8.6**` |
| E-02-2013 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:186` | `* 2.1 GCFPE model and reasoning-level guidance is the TypeSafe reading` |
| E-02-2052 | `git grep -l -E 'PF10[ ,]+[Aa]ddend(um\|a) [0-9]\|PF10[^0-9]{0,3}§\|PF10[- ]v?1[0-9]\.[0-9]\|PF10-HDE-Build-Notes-v' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- docs/pfcanon/ ':!docs/pfcanon/PF10-HDE-Buil…` | `7` |
| E-02-2053 | `git grep -h -E 'PF10[ ,]+[Aa]ddend(um\|a) [0-9]' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md \| wc -l` | `914` |
| E-02-2058 | `docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md:246` | `PF10 Addendum 1 marks HDE-EPIC011 as failed` |
| E-02-2059 | `docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md:4551` | `(PF10 §2.32)` |
| E-02-2060 | `docs/pfcanon/PF16-Canon-HD Engine Epics Map v2.3.8.md:132` | `PF10 Addendum 4` |
| E-02-2061 | `docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md:13` | `**Last Update Gate:** PF10 13.0.9` |
| E-02-2062 | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md:5961` | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` |
| E-02-2801 | `.audit_src/dev/reader_harness/app.py:8` | `if os.environ.get("APP_ENV","dev") != "dev":` |
| E-02-2812 | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md:1066` | `MUST contain one canonical JSON receipt with exactly one trailing LF` |
| E-02-2813 | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md:1182` | `the bundle goes only to that file and stdout is only the receipt` |
| E-02-2816 | `git grep -c -F "$(printf '\342\200\246')" -- docs/pfcanon \| awk -F: '{s+=$NF} END {print s}'` | `131` |
| E-02-2818 | `git grep -c -F '...' -- docs/pfcanon \| awk -F: '{s+=$NF} END {print s}'` | `50` |
| E-02-2823 | `.env.example:4` | `GEO_API_KEY` |
| E-02-3203 | `git ls-tree --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- docs/pfcanon/ \| grep PF10` | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` |
| E-02-3204 | `git log --format='%H %cs' --diff-filter=D 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` | `632f1cdf4839d1bb0d1cdfb3e48c28391d03cfdf 2026-10-09` |
| E-02-3625 | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- audit/qa/hde-epic024/checks/d01_env_pins_gate/ \| wc -l` | `2` |
| E-02-3680 | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md \| grep -n -o -E 'the EPIC030 generator' \| cut -d: -f1 \| paste -sd' '` | `1148 1171` |
| E-02-3684 | `docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md:1372` | `HDE-DISS005.2 through HDE-DISS005.4 are now Done after HDE-EPIC030 PR-04. The ta` |
| E-02-3685 | `docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md:1576` | `HDE-DISS006.3 through HDE-DISS006.5 are now Done after HDE-EPIC030 PR-05. The ta` |
| E-02-3699 | `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md:262` | `**Task status:** Done` |
| E-02-3703 | `sed 's\|^\|0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:\|' {W:c4-pf14a}/lists/K-14-1556.txt \| git cat-file --batch-check \| grep ' missing$' \| sed -e 's\|^[0-9a-f]*:\|\|' -e 's\| missing$\|\|' \| paste -sd' '` | `ci/checks/check_bridge_consistency.py tests/unit/test_check_bridge_consistency.py tools/evidence/generate_db_bridge_parity.py` |
| E-02-3704 | `git log --diff-filter=D --format='%h %cs' -1 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- ci/checks/check_bridge_consistency.py` | `a618ba7b 2026-07-21` |
| E-02-3705 | `git log --diff-filter=D --format='%h %cs' -1 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- tests/unit/test_check_bridge_consistency.py` | `a618ba7b 2026-07-21` |
| E-02-4020 | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- audit/qa/hde-epic024/checks/d03_showcompat_artifacts/primary.log audit/qa/hde-epic024/checks/d05_arrays_as_sets/primary.log \| wc…` | `2` |
| E-02-4040 | `git ls-tree -r --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- artifacts/vendor/hdapi_v2/source_selection.snapshot.json artifacts/vendor/hdapi_v2/request_shaping.snapshot.json artifacts/vendo…` | `6` |
| E-02-4864 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:2320` | `## 2.20 HDE-CRD-0002: Specification delta 01 is approved` |
| E-02-4865 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:1954` | `## 2.18 Requirements and work units carry no cost ceiling` |
| E-02-4866 | `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md:1` | `## 2.18 HDE-CRD-0002: Specification delta 01 is approved` |
| E-02-4868 | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md:232` | `the no-cost-ceiling record as 2.18, the Specification delta 01 record as 2.20` |
| E-03-002 | `git --no-optional-locks status --porcelain \| wc -l` | `0` |
| E-03-014 | `pyproject.toml:6` | `name = "glow-hdengine"` |
| E-03-015 | `pyproject.toml:7` | `version = "0.0.0"` |
| E-03-019 | `pyproject.toml:11` | `dependencies = []` |
| E-03-021 | `pyproject.toml:14` | `hdctl = "engine.cli.main:cli"` |
| E-03-024 | `pyproject.toml:18` | `include = ["engine*", "adapter*", "presenter*", "catalog*", "math*"]` |
| E-03-026 | `pyproject.toml:21` | `catalog = ["*.json"]` |
| E-03-027 | `pyproject.toml:22` | `math = ["*.json"]` |
| E-03-029 | `engine/cli/main.py:284` | `def cli(argv: list[str] \| None = None) -> int:` |
| E-03-040 | `requirements.txt:1` | `psycopg[binary]>=3.1,<3.3` |
| E-03-041 | `requirements.txt:2` | `Flask>=2.3,<3.0` |
| E-03-042 | `requirements.txt:3` | `gunicorn>=21,<22` |
| E-03-043 | `requirements.txt:4` | `jsonschema==4.23.0` |
| E-03-045 | `requirements-dev.txt:2` | `jsonschema==4.23.0` |
| E-03-047 | `requirements-dev.txt:5` | `pytest>=7.4,<9.0` |
| E-03-048 | `requirements-dev.txt:6` | `pytest-cov>=4.1,<5.0` |
| E-03-049 | `requirements-dev.txt:7` | `pytest-mock>=3.12,<4.0` |
| E-03-054 | `Procfile:1` | `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()'` |
| E-03-055 | `Procfile:1` | `--bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30` |
| E-03-061 | `adapter/gunicorn.conf.py:1` | `bind = "0.0.0.0:8080"` |
| E-03-062 | `adapter/gunicorn.conf.py:2` | `workers = 1` |
| E-03-063 | `adapter/gunicorn.conf.py:3` | `timeout = 10` |
| E-03-064 | `adapter/gunicorn.conf.py:4` | `keepalive = 2` |
| E-03-078 | `adapter/factory.py:11` | `def create_app():` |
| E-03-080 | `adapter/factory.py:14` | `app.register_blueprint(api_bp, url_prefix="/api")` |
| E-03-090 | `adapter/http_reader.py:1319` | `create_app().run(` |
| E-03-091 | `adapter/http_reader.py:1320` | `host="127.0.0.1",` |
| E-03-092 | `adapter/http_reader.py:1321` | `port=int(os.environ.get("PORT", "8000")),` |
| E-03-094 | `adapter/http_reader.py:1323` | `use_debugger=False,` |
| E-03-095 | `adapter/http_reader.py:1324` | `use_reloader=False,` |
| E-03-096 | `adapter/app.py:2` | `from adapter.wsgi import create_app` |
| E-03-111 | `scripts/start_web.sh:4` | `CMD_ARGS="'adapter.factory:create_app()' --bind 0.0.0.0:${PORT:-8000}` |
| E-03-114 | `run_flask.py:22` | `from adapter.factory import create_app` |
| E-03-116 | `run_flask.py:30` | `host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")` |
| E-03-117 | `run_flask.py:31` | `port = int(os.environ.get("FLASK_RUN_PORT", 5000))` |
| E-03-119 | `run_flask.py:51` | `use_reloader=True,` |
| E-03-121 | `run_flask.py:27` | `os.environ.setdefault("FLASK_DEBUG", "1")` |
| E-03-122 | `run_flask_dev.sh:21` | `export FLASK_APP=adapter.factory:create_app` |
| E-03-135 | `.audit_src/dev/reader_harness/app.py:7` | `def create_app() -> Flask:` |
| E-03-147 | `ci/checks/classify_ci_changes.py:266` | `"dev/reader_harness/app.py": {"product"},` |
| E-03-201 | `scripts/demo_mvp.sh:15` | `python adapter/app.py >/dev/null 2>&1 & PID=$!` |
| E-03-216 | `scripts/dev_start_reader.sh:26` | `exec python -m adapter.http_reader` |
| E-03-363 | `git ls-files 'scripts/hdctl*' \| paste -sd' ' -` | `scripts/hdctl.backup.py scripts/hdctl.clean.py scripts/hdctl.py scripts/hdctl.py.bak` |
| E-03-393 | `ci/checks/classify_ci_changes.py:320` | `_HISTORICAL_BACKUP_PATHS = {` |
| E-03-394 | `ci/checks/classify_ci_changes.py:321` | `"engine/config/provider_loader.bak2",` |
| E-03-395 | `ci/checks/classify_ci_changes.py:322` | `"engine/config/provider_loader.py.bak.1758996879",` |
| E-03-396 | `ci/checks/classify_ci_changes.py:323` | `"engine/serializer/canon.py.bak.20251022212047",` |
| E-03-397 | `ci/checks/classify_ci_changes.py:324` | `"scripts/card_close.sh.bak",` |
| E-03-398 | `ci/checks/classify_ci_changes.py:325` | `"scripts/hdctl.backup.py",` |
| E-03-399 | `ci/checks/classify_ci_changes.py:326` | `"scripts/hdctl.py.bak",` |
| E-03-901 | python -m pip wheel --no-deps --no-build-isolation -w {SCRATCH}/wheel .  (disposable clone {SCRATCH}/clone-wheel) | exit 0; Created wheel for glow-hdengine: filename=glow_hdengine-0.0.0-py3-none-any.whl size=212242 sha256=a6a822e81c32771e24d96de7e9ac7607048a0bc7095b11ed620dee749f17f4e5 |
| E-03-902 | `python3 -I {SCRATCH}/scripts/s3_wheel_cmp.py {SCRATCH}/wheel/glow_hdengine-0.0.0-py3-none-any.whl catalog/manifest.json \| grep -E '^WHEEL ' \| paste -sd';' -` | `WHEEL entries 130;WHEEL top-level {'adapter': 13, 'catalog': 9, 'engine': 97, 'glow_hdengine-0.0.0.dist-info': 6, 'math': 1, 'presenter': 4}` |
| E-03-903 | `python3 -I {SCRATCH}/scripts/s3_wheel_cmp.py {SCRATCH}/wheel/glow_hdengine-0.0.0-py3-none-any.whl catalog/manifest.json \| grep -E '^MANIFEST '` | `MANIFEST members 45 present in wheel 29 missing 16` |
| E-03-3602 | `adapter/http_reader.py:1320` | `host="127.0.0.1",` |
| E-03-3605 | `adapter/http_reader.py:1322` | `debug=False,` |
| E-03-3613 | `adapter/http_reader.py:1323` | `use_debugger=False,` |
| E-03-3614 | `adapter/http_reader.py:1324` | `use_reloader=False,` |
| E-04-019 | `engine/core/__init__.py:1` | `Pure Gate kernel and immutable result.` |
| E-04-024 | `engine/magic10/__init__.py:1` | `Private pure mechanics used by engine.core` |
| E-04-049 | `engine/config/registry_loader.py:398` | `ADMITTED_RELEASE_VERSION = "1.3.0"` |
| E-04-050 | `engine/config/registry_loader.py:399` | `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` |
| E-04-051 | `engine/config/registry_loader.py:400` | `ADMITTED_RELEASE_ROSTER = tuple(sorted({` |
| E-04-055 | `engine/config/registry_loader.py:448` | `if len(ADMITTED_RELEASE_ROSTER) != 45:` |
| E-04-056 | `engine/config/registry_loader.py:449` | `raise RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")` |
| E-04-081 | `engine/config/registry_loader.py:1506` | `def load_active_mechanics_bundle() -> AdmittedMechanicsBundle:` |
| E-04-082 | `engine/config/registry_loader.py:1507` | `Admit the exact installed complete mechanics release, or fail closed.` |
| E-04-083 | `engine/config/registry_loader.py:1510` | `repository_root, _ = _admission_execution_provenance()` |
| E-04-084 | `engine/config/registry_loader.py:1511` | `return _load_active_mechanics_bundle_from_root(repository_root)` |
| E-04-089 | `engine/config/registry_loader.py:1283` | `owners = (` |
| E-04-093 | `engine/config/registry_loader.py:465` | `def _safe_source_path(root: Path, relative_path: str) -> Path:` |
| E-04-105 | `engine/config/registry_loader.py:1219` | `def _validate_admitted_manifest(manifest: Manifest) -> None:` |
| E-04-106 | `engine/config/registry_loader.py:1224` | `if actual < expected:` |
| E-04-129 | `engine/config/registry_loader.py:1204` | `if capture.read('math/thresholds.json').data['edges'] != [24, 49, 74, 100]:` |
| E-04-137 | `engine/config/registry_loader.py:1401` | `def _deep_freeze(value: object) -> object:` |
| E-04-143 | `engine/config/registry_loader.py:1267` | `Validate the eight actual consumers` |
| E-04-144 | `engine/config/registry_loader.py:1509` | `corroborate all four live origins` |
| E-04-149 | `engine/config/registry_loader.py:1403` | `return MappingProxyType({key: _deep_freeze(item)` |
| E-04-150 | `engine/config/registry_loader.py:1405` | `return tuple(_deep_freeze(item) for item in value)` |
| E-04-151 | `engine/config/registry_loader.py:1406` | `return value` |
| E-04-169 | `engine/config/registry_loader.py:1226` | `'INCOMPLETE_RELEASE_ROSTER'` |
| E-04-173 | `engine/config/registry_loader.py:1230` | `'RELEASE_ROSTER_MISMATCH'` |
| E-04-174 | `engine/config/registry_loader.py:1239` | `'RELEASE_TIMESTAMP_MISMATCH'` |
| E-04-175 | `engine/config/registry_loader.py:1235` | `'RELEASE_VERSION_MISMATCH'` |
| E-04-177 | `engine/core/__init__.py:3` | `from .core import CoreResult, compute_core` |
| E-04-181 | `engine/core/core.py:16` | `from engine.magic10.calculators import CategoryValue, _reduce_category` |
| E-04-183 | `engine/core/core.py:23` | `class CoreResult:` |
| E-04-185 | `engine/core/core.py:209` | `def compute_core(member_a, member_b, mechanics_bundle, release_id)` |
| E-04-186 | `engine/core/core.py:210` | `eligibility belongs to the caller` |
| E-04-187 | `engine/core/core.py:237` | `except (KeyError, TypeError, AttributeError, ValueError, RecursionError):` |
| E-04-188 | `engine/core/core.py:238` | `raise ValueError("invalid pure core contract") from None` |
| E-04-204 | `engine/core/core.py:228` | `"schema": "magic10_pair_preimage.v1",` |
| E-04-206 | `engine/core/core.py:203` | `band = ("Cool" if row.score <= 24 else "Open" if row.score <= 49` |
| E-04-210 | `engine/magic10/calculators.py:15` | `def _reduce_category(category_id, q_values, bounds, weights) -> CategoryValue:` |
| E-04-211 | `engine/magic10/calculators.py:31` | `capped = tuple(min(2 * upper, max(2 * lower, q)) for q in q_values)` |
| E-04-212 | `engine/magic10/calculators.py:34` | `score = min(100, max(0, (weighted + total) // (2 * total)))` |
| E-04-213 | `engine/magic10/calculators.py:35` | `band = ("Cool" if score <= 24 else "Open" if score <= 49` |
| E-04-232 | `engine/magic10/thresholds.py:10` | `_DATA = json.loads((_ROOT / "math" / "thresholds.json").read_text(` |
| E-04-236 | `cat math/thresholds.json` | `{"clamp":[0,100],"edges":[24,49,74,100],"rounding":"ROUND_HALF_UP","version":"1"}` |
| E-04-240 | `engine/compat/compute.py:13` | `from engine.bodygraph.resolver import (` |
| E-04-245 | `engine/compat/compute.py:50` | `_BUNDLE_PROVIDER: Callable[[], AdmittedMechanicsBundle]` |
| E-04-247 | `engine/compat/compute.py:52` | `_SCHEMA_VALIDATORS: dict[str, Any] = {}` |
| E-04-248 | `engine/compat/compute.py:27` | `if score <= THRESHOLDS_V1["cool_max"]: return "Cool"` |
| E-04-249 | `engine/compat/compute.py:166` | `return "Cool" if score <= 24 else "Open" if score <= 49` |
| E-04-250 | `engine/compat/compute.py:65` | `return _BUNDLE_PROVIDER()` |
| E-04-264 | `engine/compat/compute.py:331` | `raise CompatBoundaryError("admission_config", detail="provider")` |
| E-04-265 | `engine/compat/compute.py:336` | `cache_key = f"{INTRINSIC_CACHE_PREFIX}{pair_key}"` |
| E-04-266 | `engine/compat/compute.py:346` | `core = compute_core(lo.gates, hi.gates, bundle, release_id)` |
| E-04-272 | `engine/compat/compute.py:267` | `raw = (_ROOT / _COMPAT_RESULT_SCHEMA_PATH).read_bytes()` |
| E-04-274 | `engine/compat/compute.py:282` | `_SCHEMA_VALIDATORS[identity.sha256] = cached` |
| E-04-277 | `engine/compat/compute.py:423` | `"conjunction": {` |
| E-04-288 | `engine/runtime/public.py:68` | `def emit_reader_public_envelope(` |
| E-04-289 | `engine/runtime/public.py:94` | `raise ValueError("reader_version_unsupported")` |
| E-04-290 | `engine/runtime/public.py:36` | `return [{"id": _HARMONY_ID, "band": harmony_band}]` |
| E-04-292 | `engine/runtime/public.py:63` | `if [cid for cid, _ in items] != list(FROZEN_MAGIC10_ORDER):` |
| E-04-308 | `python3 -I {W:w2-engine}/callers.py entrysum compute_core` | `compute_core files=10 call=32 import=9 reference=2 parse_errors=2 sha256=c110e234b9a6f11b` |
| E-04-351 | `git grep -l -E 'setattr\(compute, "_BUNDLE_PROVIDER"\|^[[:space:]]+compute, "_BUNDLE_PROVIDER"' -- tests/ \| wc -l` | `13` |
| E-04-369 | `engine/charts/loader.py:54` | `return str(_os.getenv("SAFE_MODE", "0")).strip() == "1"` |
| E-04-414 | `tests/core/test_engine_core_purity.py:16` | `PURE_PATHS = (` |
| E-04-427 | `engine/sampler/core.py:4` | `Pure-compute sampler core (DISS003).` |
| E-04-428 | `tools/evidence/generate_hdapi_v2_contract_inventory.py:134` | `ADAPTER_BOUNDARY_PURE_COMPUTE_LOCI = ("engine/compat/compute.py",)` |
| E-04-431 | `python3 -I {W:w2-engine}/purity_scan.py closuresum engine/core/core.py` | `engine/core/core.py toplevel_closure=31 modules_with_forbidden_hits=9 has_vendor_client=True has_db_adapter=True urllib_root=True socket_root=True psycopg_root=False` |
| E-04-434 | `python3 -I {W:w2-engine}/purity_scan.py closuresum engine/sampler/core.py` | `engine/sampler/core.py toplevel_closure=47 modules_with_forbidden_hits=10 has_vendor_client=True has_db_adapter=True urllib_root=True socket_root=True psycopg_root=False` |
| E-04-437 | `engine/bodygraph/__init__.py:3` | `from .resolver import ResolveBodygraphResult, resolve_bodygraph` |
| E-04-438 | `engine/bodygraph/resolver.py:35` | `from .vendor_client import HdApiClient, VendorError` |
| E-04-439 | `engine/bodygraph/resolver.py:13` | `from engine.db import DBAccess` |
| E-04-440 | `engine/bodygraph/vendor_client.py:6` | `import socket` |
| E-04-441 | `engine/bodygraph/vendor_client.py:15` | `from urllib import request` |
| E-04-511 | `catalog/channels_catalog_v1.json:1` | `{"channels":[{"id":"alpha","band":"4B60","status":"active"}]}` |
| E-04-533 | `catalog/manifest.json.path_proof.txt:2` | `size_bytes: 1981` |
| E-04-534 | `catalog/manifest.json.path_proof.txt:3` | `sha256: dbf89997d358cdd524e787f8dc08a9b9b5d8ceea0a2f2db97559d3f5001513bf` |
| E-04-576 | `engine/config/registry_loader.py:398` | `ADMITTED_RELEASE_VERSION = "1.3.0"` |
| E-04-577 | `engine/config/registry_loader.py:399` | `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"` |
| E-04-578 | `engine/config/registry_loader.py:400` | `ADMITTED_RELEASE_ROSTER = tuple(sorted({` |
| E-04-579 | `engine/config/registry_loader.py:448` | `if len(ADMITTED_RELEASE_ROSTER) != 45:` |
| E-04-580 | `python3 -I {W:w1-pack-catalog}/facts.py proofs catalog` | `proofs=6 MATCH=5 MISMATCH=1 mismatched=catalog/manifest.json.path_proof.txt` |
| E-04-581 | `printf '%s %s\n' "$(wc -c < catalog/manifest.json)" "$(sha256sum catalog/manifest.json \| cut -c1-64)"` | `5881 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` |
| E-04-652 | `python3 -I {W:w1-pack-catalog}/facts.py schema_meta schemas/magic10_compat_result_v1.schema.json` | `$schema=https://json-schema.org/draft/2020-12/schema \| $id=schemas/magic10_compat_result_v1.schema.json \| title=magic10_compat_result_v1 \| type=object \| required(6)=schema,config_id,release_id,pair_k…` |
| E-04-653 | `python3 -I {W:w1-pack-catalog}/facts.py schema_meta schemas/magic10_mechanics_v1.schema.json` | `$schema=https://json-schema.org/draft/2020-12/schema \| $id=schemas/magic10_mechanics_v1.schema.json \| title=magic10_mechanics_v1 \| type=object \| required(10)=category_weights,config_id,profiles,respo…` |
| E-04-654 | `python3 -I {W:w1-pack-catalog}/facts.py schema_meta schemas/magic10_result_v1.schema.json` | `$schema=https://json-schema.org/draft/2020-12/schema \| $id=schemas/magic10_result_v1.schema.json \| title=magic10_result_v1 \| type=object \| required(6)=schema,config_id,release_id,pair_key,signals,cat…` |
| E-04-776 | `catalog/magic10_mechanics_v1.json:1` | `"config_id":"m10-channel-state-v1.0.0"` |
| E-04-779 | `python3 -I {W:w1-pack-catalog}/facts.py mech_ops` | `ops=companionship_em_mass_v1:1,twice_min_owner_mass_v1:1,weighted_state_sum_v1:18 profiles=-:2,activation_bp_v1:7,coherence_bp_v1:8,expression_bp_v1:3 memberships=90 weights=[1] distinct_channels_use…` |
| E-04-781 | `schemas/magic10_mechanics_v1.schema.json:1` | `"maxItems":20,"minItems":20,"type":"array","uniqueItems":true` |
| E-04-787 | `python3 -I {W:w1-pack-catalog}/facts.py mech_categories` | `count=10 harmony=[1,1] heat=[1,1] communication=[1,1] alignment=[1,1] comfort=[1,1] consistency=[1,1] expansion=[1,1] creativity=[1,1] drive=[1,1] balance=[1,1] reducers=weighted_mean_half_unit_v1 to…` |
| E-04-790 | `python3 -I {W:w1-pack-catalog}/facts.py mech_profiles` | `activation_bp_v1={"companionship":5000,"compromise":2500,"dominance":7500,"electromagnetic":10000,"none":0} coherence_bp_v1={"companionship":10000,"compromise":2500,"dominance":5000,"electromagnetic"…` |
| E-04-798 | `engine/config/registry_loader.py:1168` | `raise SchemaValidationError('SIGNAL_OPERATION_MISMATCH', 'Balance operation/prof` |
| E-04-800 | `engine/config/registry_loader.py:372` | `'equilibrium_score': ('twice_min_owner_mass_v1',` |
| E-04-801 | `engine/config/registry_loader.py:374` | `'counterweight_ratio': ('companionship_em_mass_v1',` |
| E-04-823 | `engine/magic10/signals.py:107` | `raise ValueError("invalid Balance operation")` |
| E-04-835 | `python3 -I {W:w1-pack-catalog}/facts.py channels_invariants` | `count=36 ids_unique=True ids_sorted=True gates_len2_int=True gates_ascending=True gates_1_64=True pairs_unique=True unordered_pairs_unique=True id_eq_gates=True nulls=0 centers_len2=True centers_sort…` |
| E-04-901 | `git log --diff-filter=A --format='%h %cI' 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- engine/core/__init__.py` | `c57d5b4b 2025-11-30T05:34:50+01:00` |
| E-04-902 | `git ls-tree -d --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b engine/ \| sed 's#^engine/##' \| paste -sd' ' -` | `bodygraph canon categories charts cli compat compliance config core db errors http magic10 mech narratives ops order presenter presets provider providers runtime sampler serializer stable testsupport…` |
| E-04-903 | `git ls-tree --name-only 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b engine/core/ \| paste -sd' ' -` | `engine/core/__init__.py engine/core/core.py` |
| E-04-904 | `sed -n '478p' engine/config/registry_loader.py \| grep -c -F "raise SchemaValidationError('MISSING_FILE', f'missing source: {relative_path}') from exc"` | `1` |
| E-04-905 | `sed -n '1402p;1404p' engine/config/registry_loader.py \| sed 's/^ *//' \| paste -sd'\|' -` | `if isinstance(value, Mapping):\|if isinstance(value, (list, tuple)):` |
| E-04-906 | `sed -n '1240,1243p' engine/config/registry_loader.py \| sed 's/^ *//' \| paste -sd'\|' -` | `'release manifest timestamp is not the adopted timestamp',\|)\|\|` |
| E-04-907 | `sed -n '22p' engine/core/core.py` | `@dataclass(frozen=True, slots=True)` |
| E-04-908 | `sed -n '330p' engine/compat/compute.py \| sed 's/^ *//'` | `if type(bundle) is not AdmittedMechanicsBundle:` |
| E-04-909 | `sed -n '70,73p' engine/charts/loader.py \| sed 's/^ *//' \| paste -sd'\|' -` | `d.mkdir(parents=True, exist_ok=True)\|f = d / "loader_call.jsonl"\|with f.open("ab") as fh:\|fh.write(_json.dumps(line, separators=(",", ":"), ensure_ascii=False).encode("utf-8") + b"\n")` |
| E-04-910 | `grep -n -F 'perf_counter' engine/charts/loader.py \| cut -d: -f1 \| paste -sd, -` | `95,168` |
| E-04-911 | `sed -n '346p' engine/compat/compute.py \| sed 's/^ *//'` | `core = compute_core(lo.gates, hi.gates, bundle, release_id)` |
| E-04-912 | `sed -n '342,343p' engine/compat/compute.py \| sed 's/^ *//' \| paste -sd'\|' -` | `pure = _cached_pure_result(hit, bundle=bundle, pair_key=pair_key, config_id=config_id, release_id=release_id, fingerprints=fingerprints)\|stale_hit = pure is None` |
| E-04-913 | `sed -n '205,207p;210p' engine/compat/compute.py \| sed 's/^ *//' \| paste -sd'\|' -` | `if (hit.get("pair_key") != pair_key or hit.get("config_id") != config_id\|or hit.get("release_id") != release_id or hit.get("result_schema") != PURE_RESULT_SCHEMA\|or list(hit.get("fingerprints") or []…` |
| E-04-914 | `git log -1 --format='%h %cI' 39b9cdf6 && git merge-base --is-ancestor 39b9cdf6 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b && echo ancestor` | `39b9cdf6 2026-09-27T07:56:33+00:00\|ancestor` |
| E-04-915 | `sed -n '19,23p' engine/charts/loader.py \| sed 's/^ *//' \| paste -sd'\|' -` | `# Legacy provider resolve (kept for backward compatibility with old tests)\|try:\|from engine.config.provider_loader import resolve_provider  # type: ignore\|except Exception:  # pragma: no cover\|resolv…` |
| E-04-916 | `sed -n '78,79p' engine/charts/loader.py \| sed 's/^ *//' \| paste -sd'\|' -` | `if resolve_provider is None:\|return {"gates": [1, 2, 3]}` |
| E-04-917 | `sed -n '141p' engine/charts/loader.py \| sed 's/^ *//'` | `"gates": [1, 2, 3],` |
| E-04-918 | `grep -n -F 'def band_v0' engine/compat/ts_v0.py \| cut -d: -f1 \| paste -sd, - && sed -n '63p;89p' engine/compat/ts_v0.py \| sed 's/^ *//' \| sort -u` | `61,87\|return "Warm" if features.get("sacral_pair") else "Open"` |
| E-04-919 | `git grep -l -E 'from engine\.compat import ts_v0\|from engine\.compat\.ts_v0\|import ts_v0' -- . ':!docs/' ':!audit/' ':!.audit_src/' \| paste -sd' ' -` | `scripts/hdctl.backup.py scripts/hdctl.clean.py` |
| E-04-2804 | `engine/compat/compute.py:346` | `core = compute_core(lo.gates, hi.gates, bundle, release_id)` |
| E-04-2807 | `engine/compat/compute.py:42` | `COMPAT_RESULT_SCHEMA = "magic10_compat_result.v1"` |
| E-05-031 | `.audit_src/dev/reader_harness/app.py:12` | `app.getattr(app,"register_"+"blueprint")(bp, url_prefix="/api")` |
| E-05-037 | `adapter/factory.py:15` | `app.register_blueprint(compat_blueprint)` |
| E-05-038 | `adapter/http_reader.py:1249` | `app = Flask(__name__)` |
| E-05-039 | `adapter/http_reader.py:1252` | `app.register_blueprint(bp, url_prefix="")` |
| E-05-040 | `adapter/http_reader.py:1257` | `app.register_blueprint(api_bp, url_prefix="/api")` |
| E-05-041 | `adapter/http_reader.py:1260` | `app.register_blueprint(compat_blueprint)` |
| E-05-045 | `adapter/wsgi.py:25` | `app.register_blueprint(compat_blueprint)` |
| E-05-069 | `adapter/wsgi.py:41` | `@app.get("/internal/healthz")` |
| E-05-070 | `adapter/wsgi.py:47` | `@app.get("/internal/readyz")` |
| E-05-077 | `Procfile:1` | `gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2` |
| E-05-086 | `adapter/app.py:2` | `from adapter.wsgi import create_app` |
| E-05-118 | `engine/http/compat_handler.py:19` | `compat_blueprint = Blueprint("compat", __name__, url_prefix="/api/compat/v1")` |
| E-05-122 | `adapter/http_reader.py:532` | `version = _select_reader_version(("1", "2"))` |
| E-05-125 | `adapter/http_reader.py:640` | `@bp.route("/reader", methods=["POST"], provide_automatic_options=False)` |
| E-05-126 | `adapter/http_reader.py:646` | `return _reader_method_not_allowed("POST")` |
| E-05-127 | `adapter/http_reader.py:644` | `@bp.route("/reader", methods=["GET", "HEAD", "OPTIONS", "PUT", "PATCH", "DELETE"` |
| E-05-129 | `adapter/http_reader.py:687` | `if not _reader_dev_env_explicit():` |
| E-05-130 | `adapter/http_reader.py:389` | `return os.environ.get("APP_ENV") == "dev"` |
| E-05-131 | `adapter/http_reader.py:688` | `return _error("ERR_READER_FORBIDDEN", 403)` |
| E-05-147 | `adapter/http_reader.py:904` | `if os.environ.get("APP_ENV") in {"dev", "test", "local"}:` |
| E-05-148 | `adapter/http_reader.py:907` | `return _writer_error("ERR_WRITER_FORBIDDEN", status=403)` |
| E-05-160 | `adapter/http_reader.py:1178` | `if request.headers.get("X-Identity-Override"):` |
| E-05-172 | `engine/http/compat_handler.py:112` | `if _compute_env_mode(os.environ) == "prod":` |
| E-05-208 | `adapter/factory.py:30` | `@app.errorhandler(404)` |
| E-05-209 | `adapter/factory.py:33` | `return _not_found_envelope_response(404, None)` |
| E-05-210 | `adapter/factory.py:20` | `payload = emit_public(error_envelope("ERR_NOT_FOUND"))` |
| E-05-211 | `adapter/factory.py:35` | `@app.errorhandler(405)` |
| E-05-212 | `adapter/factory.py:39` | `return _not_found_envelope_response(405, err.get_response().headers.get("Allow")` |
| E-05-213 | `adapter/factory.py:41` | `return _not_found_envelope_response(405, ", ".join(sorted(err.valid_methods or (` |
| E-05-214 | `adapter/factory.py:43` | `@app.after_request` |
| E-05-215 | `adapter/factory.py:48` | `and resp.mimetype == "text/html"` |
| E-05-216 | `adapter/factory.py:54` | `if resp.headers.get("ETag") and _req.path.startswith("/internal/"):` |
| E-05-217 | `adapter/http_reader.py:1287` | `@app.errorhandler(404)` |
| E-05-218 | `adapter/http_reader.py:1289` | `if request.path.rstrip("/").startswith("/api/compat/v1"):` |
| E-05-219 | `adapter/http_reader.py:1293` | `@app.errorhandler(405)` |
| E-05-220 | `adapter/http_reader.py:1281` | `resp.headers["Allow"] = ", ".join(sorted(err.valid_methods))` |
| E-05-224 | `adapter/wsgi.py:53` | `@app.errorhandler(404)` |
| E-05-225 | `adapter/wsgi.py:60` | `@app.errorhandler(405)` |
| E-05-246 | `adapter/http_reader.py:618` | `if request.endpoint in writers:` |
| E-05-288 | `adapter/http_reader.py:414` | `resp.headers["Cache-Control"] = "no-store"` |
| E-05-289 | `adapter/http_reader.py:415` | `resp.headers["Allow"] = allow` |
| E-05-356 | `adapter/wsgi.py:28` | `resp.headers.setdefault("Cache-Control", "no-store")` |
| E-05-364 | `adapter/wsgi.py:38` | `resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeS` |
| E-05-389 | `adapter/etag_core.py:6` | `READER_CACHE = "private, no-cache, must-revalidate"` |
| E-05-393 | `adapter/wsgi.py:36` | `env_mode = (os.environ.get("APP_ENV") or os.environ.get("ENGINE_ENV") or "dev").` |
| E-05-429 | `adapter/wsgi.py:36` | `env_mode = (os.environ.get("APP_ENV") or os.environ.get("ENGINE_ENV") or "dev").` |
| E-05-442 | `adapter/env_guard.py:42` | `if app is not None and app.strip() != "":` |
| E-05-443 | `adapter/env_guard.py:17` | `_PROD_ALIASES = {"prod", "production", "live"}` |
| E-05-450 | `git ls-files -s docs/ENDPOINTS_CATALOG.json \| awk '{print $1, $2, $4}'` | `120000 5d041e91a8c01957975e16c715aa7bdd7d3b06b3 docs/ENDPOINTS_CATALOG.json` |
| E-05-451 | `git cat-file -p 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/ENDPOINTS_CATALOG.json` | `../artifacts/audit/ENDPOINTS_CATALOG.json` |
| E-05-457 | `python3 -I {W:w3-http-presenter}/audit_http.py catparse` | `{"bytes": 5618, "endpoints": 18, "generated_at_utc": "2026-08-24T18:04:49Z", "lines": 1, "row_keys": ["a7_eligible", "aliases", "blueprint_module", "classification", "description", "env_gate", "inter…` |
| E-05-465 | `python3 -I {W:w3-http-presenter}/audit_http.py key catalog catalog_rows_matching_written_pair` | `17` |
| E-05-477 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"GET","path":"/api/compat/v1"` |
| E-05-478 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"HEAD","path":"/api/compat/v1"` |
| E-05-479 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"OPTIONS","path":"/api/compat/v1"` |
| E-05-480 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"GET","path":"/aux/narrative"` |
| E-05-481 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"GET","path":"/ops/rails/refusal"` |
| E-05-482 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"POST","path":"/ops/rails/refusal"` |
| E-05-483 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"GET","path":"/internal/healthz"` |
| E-05-484 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"method":"GET","path":"/internal/readyz"` |
| E-05-485 | `python3 -I {W:w3-http-presenter}/audit_http.py key catalog pairs_without_catalog_row_count` | `12` |
| E-05-486 | `adapter/http_reader.py:574` | `_PRODUCTION_RETIRED = {` |
| E-05-487 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"env_gate":"APP_ENV!=prod"` |
| E-05-488 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"env_gate":"APP_ENV in {dev,test,local}"` |
| E-05-489 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"env_gate":"APP_ENV=dev"` |
| E-05-490 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"env_gate":"operator-network-only"` |
| E-05-491 | `artifacts/audit/ENDPOINTS_CATALOG.json:1` | `"env_gate":"not_applicable_public"` |
| E-05-501 | `adapter/http_reader.py:42` | `resp.headers["Cache-Control"] = "private, max-age=0, must-revalidate"` |
| E-05-502 | `adapter/schemas/version_v1.schema.json:6` | `"required": ["ok", "schema", "engine_tag", "release_id", "checksums", "toggles_s` |
| E-05-503 | `adapter/schemas/version_v1.schema.json:5` | `"additionalProperties": false,` |
| E-05-504 | `adapter/http_reader.py:1184` | `payload = _build_internal_version_payload()` |
| E-05-505 | `tests/adapter/test_jsonschema.py:75` | `@pytest.mark.xfail(reason="/internal/version untouched in PR scope", strict=Fals` |
| E-05-2804 | `adapter/factory.py:32` | `An unknown path, compat or not, answers the governed envelope.` |
| E-05-2849 | `adapter/http_reader.py:763` | `viewer_top = request.args.get("viewer_top") or None` |
| E-05-2851 | `adapter/http_reader.py:765` | `families = tuple(_collect_query_values("families_fired"))` |
| E-05-2852 | `adapter/http_reader.py:766` | `release_id = request.args.get("release_id") or identity_meta()["release_id"]` |
| E-05-2853 | `adapter/http_reader.py:767` | `requested_pack_sha = request.args.get("pack_sha") or pack.pack_sha` |
| E-05-2854 | `adapter/http_reader.py:769` | `emission = emit_public_aux(` |
| E-05-2877 | `adapter/http_reader.py:1275` | `never framework HTML` |
| E-05-3605 | `adapter/http_reader.py:386` | ``` empty, ``test``, ``local`` and every other value refuse; an unset ``` |
| E-06-001 | `engine/runtime/identity.py:26` | `_FIELDS = (` |
| E-06-002 | `engine/runtime/identity.py:151` | `return {field: getattr(_IDENTITY, field) for field in _FIELDS}` |
| E-06-016 | `engine/presenter/emitter.py:6` | `def emit_public(envelope: Dict[str, Any], *, sort_keys: bool = True) -> bytes:` |
| E-06-018 | `engine/presenter/emitter.py:16` | `def emit_public_with_envelope(` |
| E-06-020 | `engine/presenter/emitter.py:23` | `def emit_compact_json(envelope: Dict[str, Any], *, sort_keys: bool = True) -> Tu` |
| E-06-023 | `presenter/reader_v1/emitter.py:115` | `def emit_reader_v1(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:` |
| E-06-024 | `presenter/reader_v1/emitter.py:123` | `def emit_reader_v2(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:` |
| E-06-025 | `presenter/reader_v1/emitter.py:105` | `def _emit(preimage: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:` |
| E-06-026 | `presenter/reader_v1/emitter.py:107` | `pre_bytes = emitter.emit_public(preimage)` |
| E-06-027 | `presenter/reader_v1/emitter.py:108` | `digest = hashlib.sha256(pre_bytes).hexdigest()` |
| E-06-028 | `presenter/reader_v1/emitter.py:110` | `final["idempotence_hash"] = digest` |
| E-06-029 | `presenter/reader_v1/emitter.py:111` | `public_bytes = emitter.emit_public(final)` |
| E-06-055 | `presenter/reader_v1/emitter.py:8` | `_CATEGORY_BANDS = {"Cool","Open","Warm","Glow"}` |
| E-06-056 | `presenter/reader_v1/emitter.py:9` | `_CATEGORY_KEYS = {"id", "band"}` |
| E-06-057 | `presenter/reader_v1/emitter.py:19` | `if not isinstance(c, dict) or set(c) != _CATEGORY_KEYS:` |
| E-06-058 | `presenter/reader_v1/emitter.py:23` | `if not isinstance(cid, str) or not cid:` |
| E-06-059 | `presenter/reader_v1/emitter.py:25` | `if band not in _CATEGORY_BANDS:` |
| E-06-060 | `presenter/reader_v1/emitter.py:41` | `raise ValueError(f"Duplicate category id: {item['id']}")` |
| E-06-061 | `presenter/reader_v1/emitter.py:44` | `cleaned.sort(key=lambda x: x["id"])` |
| E-06-062 | `presenter/reader_v1/emitter.py:58` | `raise ValueError("Reader v2 ineligible envelope must carry no categories")` |
| E-06-063 | `presenter/reader_v1/emitter.py:60` | `if [item["id"] for item in items] != list(FROZEN_MAGIC10_ORDER):` |
| E-06-065 | `presenter/reader_v1/emitter.py:74` | `"reader_version": "v1",` |
| E-06-066 | `presenter/reader_v1/emitter.py:94` | `"reader_version": "v2",` |
| E-06-067 | `engine/runtime/public.py:11` | `_READER_VERSIONS = ("v1", "v2")` |
| E-06-068 | `engine/runtime/public.py:93` | `if reader_version not in _READER_VERSIONS:` |
| E-06-070 | `engine/runtime/public.py:32` | `    if not eligible:` |
| E-06-071 | `engine/runtime/public.py:34` | `if harmony_band not in _BANDS:` |
| E-06-072 | `engine/runtime/public.py:36` | `return [{"id": _HARMONY_ID, "band": harmony_band}]` |
| E-06-138 | `presenter/json_canon_compare.py:31` | `def _canonical_bytes(payload: Any) -> bytes:` |
| E-06-166 | `engine/cli/main.py:823` | `_dump_reader_bytes(_.dump_reader, reader_bytes)` |
| E-06-170 | `engine/cli/main.py:801` | `_emit_stdout_bytes(emitter.emit_public(conjunction_payload))` |
| E-06-902 | `grep -n -E '^def (_ordered_categories_v2\|_emit)\b' presenter/reader_v1/emitter.py \| cut -d: -f1 \| paste -sd, - && sed -n '62p;112p' presenter/reader_v1/emitter.py \| sed 's/^ *//' && grep -n -E '^def …` | `48,105\|return items\|return public_bytes, final\|30\|return [{"id": _HARMONY_ID, "band": harmony_band}]` |
| E-07-030 | `engine/cli/main.py:91` | `sub = parser.add_subparsers(dest="command", required=True)` |
| E-07-031 | `engine/cli/main.py:93` | `"showcompat",` |
| E-07-032 | `engine/cli/main.py:94` | `Emit the canonical magic10_compat_result.v1 document for a pair` |
| E-07-053 | `engine/cli/main.py:141` | `"aux-preview",` |
| E-07-063 | `engine/cli/main.py:153` | `"bg:resolve",` |
| E-07-075 | `engine/cli/main.py:187` | `"dev:sampler",` |
| E-07-141 | `engine/cli/main.py:570` | `def _emit_stdout_bytes(payload: bytes) -> None:` |
| E-07-143 | `engine/cli/main.py:572` | `raise CliError("STDOUT_MISSING_LF")` |
| E-07-145 | `engine/cli/main.py:574` | `raise CliError("STDOUT_CRLF")` |
| E-07-147 | `engine/cli/main.py:829` | `_emit_stdout_bytes(emitter.emit_public(result))` |
| E-07-901 | hdctl --help  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: usage: hdctl [-h] [--version] |
| E-07-902a | hdctl showcompat --help  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: usage: hdctl showcompat [-h] [--pair-file PAIR_FILE] [--a-file A_FILE] |
| E-07-902b | hdctl aux-preview --help  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: usage: hdctl aux-preview [-h] [--category CATEGORY] |
| E-07-902c | hdctl bg:resolve --help  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: usage: hdctl bg:resolve [-h] --user USER [--source {auto,db,vendor}] |
| E-07-902d | hdctl dev:sampler --help  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: usage: hdctl dev:sampler [-h] --viewer VIEWER --candidates-file |
| E-07-903 | hdctl --version  (disposable clone {SCRATCH}/clone, closed rails, APP_ENV inherited from the session) | exit 0; first stdout line: hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e) |
| E-07-2806 | `engine/cli/main.py:829` | `_emit_stdout_bytes(emitter.emit_public(result))` |
| E-07-2807 | `engine/cli/main.py:807` | `result = evaluate_pair(a_party, b_party)` |
| E-07-2809 | `engine/cli/main.py:757` | `auto is DB-only; the birth-based vendor fallback is prohibited.` |
| E-07-2810 | `engine/cli/main.py:783` | `File and stdin modes perform no DB or vendor access` |
| E-07-2836 | `engine/cli/main.py:52` | `_ALLOW_PROD_VENDOR = "--allow-prod-vendor"` |
| E-08-183 | `engine/bodygraph/vendor_client.py:197` | `env.get("HD_API_BASE_URL")` |
| E-08-184 | `engine/bodygraph/vendor_client.py:198` | `env.get("HDAPI_BASE_URL")` |
| E-08-185 | `engine/bodygraph/vendor_client.py:199` | `if canonical and legacy and canonical != legacy:` |
| E-08-186 | `engine/bodygraph/vendor_client.py:333` | `source.get("HD_API_KEY")` |
| E-08-192 | `engine/bodygraph/vendor_client.py:762` | `safe_mode = (os.environ.get("SAFE_MODE") or "").strip()` |
| E-08-193 | `engine/bodygraph/vendor_client.py:763` | `allow_network = (os.environ.get("ALLOW_NETWORK") or "").strip()` |
| E-08-207 | `engine/bodygraph/vendor_client.py:764` | `if safe_mode != "0" or allow_network != "1":` |
| E-08-208 | `engine/bodygraph/vendor_client.py:765` | `raise VendorError("PROVIDER_REFUSED", "Vendor source refused unless SAFE_MODE=0` |
| E-08-225 | `engine/bodygraph/vendor_client.py:297` | `if parsed.scheme != "https":` |
| E-08-226 | `engine/bodygraph/vendor_client.py:298` | `raise VendorError("PROVIDER_CONFIG_MISSING", "HD_API_BASE_URL must be https")` |
| E-08-237 | `engine/bodygraph/vendor_client.py:272` | `class _NoRedirectHandler(urlrequest.HTTPRedirectHandler):` |
| E-08-239 | `engine/bodygraph/vendor_client.py:766` | `opener = urlrequest.build_opener(_NoRedirectHandler())` |
| E-08-285 | `engine/db/adapter.py:119` | `dsn = (env.get("DATABASE_URL") or "").strip()` |
| E-08-286 | `engine/db/adapter.py:16` | `"DB_ALLOW_BRIDGE_IN_PROD",` |
| E-08-293 | `engine/db/adapter.py:127` | `ctor = psycopg_factory or (lambda value: PsycopgProvider(value))` |
| E-08-428 | `engine/bodygraph/mapped_cache.py:19` | `_EXPECTED_POSTURE = "adapter_mapped_no_raw_vendor_payload"` |
| E-08-442 | `engine/bodygraph/mapped_cache.py:165` | `def read_current_mapped_bodygraph(db: DBAccess, canonical_user_id: str) -> Mappe` |
| E-08-455 | `tools/bodygraph/check_magic10_gate_readiness.py:8` | ``` It issues no ``UPDATE``, ``` |
| E-08-456 | `tools/bodygraph/check_magic10_gate_readiness.py:82` | `"read_only": True,` |
| E-08-457 | `tools/bodygraph/check_magic10_gate_readiness.py:89` | `def require_closed_rails() -> None:` |
| E-08-460 | `tools/bodygraph/check_magic10_gate_readiness.py:54` | `SELECTION_FILE_MAX_BYTES = 1_048_576` |
| E-08-465 | `tools/bodygraph/check_magic10_gate_readiness.py:142` | `raise ReadinessRefusal(READINESS_EMPTY_SELECTION)` |
| E-08-466 | `tools/bodygraph/check_magic10_gate_readiness.py:143` | `if any(strict_canonical_uuid(value) is None for value in raw):` |
| E-08-468 | `tools/bodygraph/check_magic10_gate_readiness.py:219` | `raise ReadinessRefusal(READINESS_UNAVAILABLE) from exc` |
| E-08-641 | `engine/bodygraph/ingest.py:306` | `raise VendorError("DB_PAYLOAD_MISSING", "stored payload missing", {})` |
| E-08-642 | `engine/bodygraph/vendor_client.py:216` | `def __init__(self, code: str, message: str, *, details: Mapping[str, Any] \| None` |
| E-08-643 | `engine/bodygraph/vendor_client.py:359` | `rails_state=_rails_state_from_env({key: str(value) for key, value in source.item` |
| E-08-644 | `engine/bodygraph/vendor_client.py:762` | `safe_mode = (os.environ.get("SAFE_MODE") or "").strip()` |
| E-08-1901 | `sed -n '89p' engine/bodygraph/mapped_cache.py \| grep -c -F 'MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache projection was refused")'` | `1` |
| E-08-2002 | `engine/bodygraph/vendor_client.py:137` | `"classification": "adapter_backed_v2_chart",` |
| E-08-2826 | `engine/bodygraph/vendor_client.py:150` | `"classification": "explicit_legacy_fallback",` |
| E-08-2862 | `engine/bodygraph/resolver.py:296` | `"PROVIDER_PROD_OVERRIDE_REQUIRED",` |
| E-08-2863 | `engine/bodygraph/resolver.py:319` | `"PROVIDER_AUDIT_UNAVAILABLE",` |
| E-08-2864 | `engine/bodygraph/resolver.py:302` | `actor = vendor_audit.resolve_actor_principal()` |
| E-08-2881 | `engine/bodygraph/resolver.py:1126` | `if has_chart:` |
| E-08-4004 | `engine/db/adapter.py:22` | `{"ci", "dev", "local", "prod", "production", "staging", "test"}` |
| E-08-4005 | `engine/db/adapter.py:41` | `return name if name in _SAFE_APP_ENV_NAMES else "unknown"` |
| E-09-001 | python tools/evidence/update_evidence_index.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; first output line: [evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC |
| E-09-002 | python tools/evidence/orientation_demo.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-003 | python tools/evidence/validate_evidence_paths.py  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-004 | ci/checks/check_mirror_schema.sh  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-005 | ci/checks/check_evidence_index_hash.sh  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-006 | ci/checks/check_final_lf.sh  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-007 | python tools/evidence/check_lf_endings.py  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-008 | ci/checks/check_env_pins.sh  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; first output line: [env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC |
| E-09-009 | python scripts/release_id_recompute.py --check-manifest-only  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-010 | python tools/evidence/run_canonical_json_gate.py --check-only  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-011 | python tools/config/generate_config_artifacts.py --compare-goldens .  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; first output line: {"candidate_release_id":"77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e", |
| E-09-012 | python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 1; first output line: EPIC_CLOSE_PACK_ERROR:DIRTY_TREE |
| E-09-012b | the E-09-012 command in a second clean clone {SCRATCH}/clone-close (nothing installed) | exit 0; EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json |
| E-09-013 | python tools/ci/prepush_check.py lanes build-notes  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; first output line: PREPUSH_CHECK: repo= |
| E-09-013b | the E-09-013 command after setting the clone refs/remotes/origin/main to the pinned commit | exit 0; PREPUSH_CHECK_RESULT: PASS lanes=PASS build-notes=PASS |
| E-09-020 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^HUMAN_INDEX (type\|sentinel\|distinct key-sets\|rows with\|paths missing)' \| paste -sd';' -` | `HUMAN_INDEX type list rows 653 bytes 172372 sha256 2cb32a6819aa7335891754e6ac04b59663dcb3b7affd7ff88025e66446f42cb4;HUMAN_INDEX sentinel 2cb32a6819aa7335891754e6ac04b59663dcb3b7affd7ff88025e66446f42c…` |
| E-09-021 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^MIRROR (bytes\|sentinel\|distinct paths)' \| paste -sd';' -; git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:artifacts/ev…` | `MIRROR bytes 312779 newline-count 653 nonempty lines 653 sha256 cae6df84a17fd5325b7157b02dd177f4e4c90e62ae5b86aeca85895eafd32c71;MIRROR sentinel cae6df84a17fd5325b7157b02dd177f4e4c90e62ae5b86aeca8589…` |
| E-09-022 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^ORIENTATION' \| paste -sd';' -` | `ORIENTATION bytes 115 lines 4;ORIENTATION total_artifacts: 653;ORIENTATION status: ok` |
| E-09-023 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^(MANIFEST\|RELEASE_ID)' \| paste -sd';' -` | `MANIFEST keys ['built_at_utc', 'files', 'root', 'version'] version 1.3.0 built_at_utc 2026-08-24T18:04:49Z root catalog/ files 45;MANIFEST file is canonical bytes? True ascii-variant equal? True file…` |
| E-09-024 | `python3 -I {SCRATCH}/scripts/s9_inv.py /home/user/glow-hdengine-v2 \| grep -E '^(LOADER ADMITTED_RELEASE_(VERSION\|BUILT_AT_UTC)\|ROSTER)' \| paste -sd';' -` | `LOADER ADMITTED_RELEASE_VERSION line 398 '1.3.0';LOADER ADMITTED_RELEASE_BUILT_AT_UTC line 399 '2026-08-24T18:04:49Z';ROSTER literal count 45 manifest paths 45 equal True roster-only [] manifest-only…` |
| E-09-026 | `git ls-files -- audit/qa \| awk -F/ 'NF>3{print $3}' \| sort \| uniq -c \| awk '{print $2"="$1}' \| paste -sd' ' -; git ls-files -- audit/qa \| awk -F/ 'NF==3' \| wc -l; git ls-files -- audit/qa/hde-crd-000…` | `archived_from_root=17 compat=44 hde-crd-0001=23 hde-crd-0002=62 hde-epic017=14 hde-epic018=45 hde-epic019=67 hde-epic020=48 hde-epic021=76 hde-epic022=317 hde-epic023=72 hde-epic024=171 hde-epic025=8…` |
| E-09-029 | `git ls-files -- goldens \| wc -l; for f in $(git ls-files -- 'goldens/*.sha256'); do t=${f%.sha256}; a=$(git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:$t \| sha256sum \| cut -d' ' -f1); b=$(git show…` | `26;match=13` |
| E-09-030 | `for f in artifacts/release_id.txt artifacts/release_pack_manifest.json artifacts/db_bridge/provider_parity.proof.json artifacts/runtime/env_connectivity.nondev_failure.json audit/ops/hde-epic032/db-p…` | `artifacts/release_id.txt 65 8999bd05 2026-09-26;artifacts/release_pack_manifest.json 451 d79cfc1c 2026-09-26;artifacts/db_bridge/provider_parity.proof.json 3313 79e47867 2026-07-16;artifacts/runtime/…` |
| E-09-031 | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:tools/evidence/run_canonical_json_gate.py \| python3 -I -c 'import ast,sys; t=ast.parse(sys.stdin.read()); [print(getattr((n.targets[0] if isinstance(…` | `EXPECTED_TARGET_PATHS 236 26;EXPECTED_SET_RULES 294 6;9` |
| E-09-032 | `git cat-file -s 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:artifacts/registry/registry_report.json; git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:artifacts/registry/registry_report.json \| python3 -…` | `3832;artifacts generated_at_utc inputs notes schema;0 0 0 0 0` |
| E-09-033 | `python3 -I -c 'import json,re;e=json.load(open("artifacts/audit/ENDPOINTS_CATALOG.json"))["endpoints"];print(len(e), sorted(r["path"] for r in e if re.search("aux\|admin", r.get("path",""), re.I)))'` | `18 ['/aux/narrative']` |
| E-09-034 | `printf '%s %s\n' "$(grep -ciE 'aux\|admin' artifacts/audit/ENDPOINTS_CATALOG.json)" "$(wc -l < artifacts/audit/ENDPOINTS_CATALOG.json)"` | `1 1` |
| E-09-035 | `git log -1 --format='%h %cs' -- docs/evidence/INDEX.json` | `09e443f4 2026-10-26` |
| E-09-036 | `python3 -I -c 'import json;print(sum(1 for r in json.load(open("docs/evidence/INDEX.json")) if r.get("epic_id")=="HDE-EPIC040"))'` | `16` |
| E-09-037 | `git log -1 --format='%h %cs' -- catalog/manifest.json` | `822ce15c 2026-10-18` |
| E-09-038 | `git log -1 --format='%h %cs' -- artifacts/audit/ENDPOINTS_CATALOG.json` | `2f3db0a0 2026-10-18` |
| E-09-039 | `git ls-files -- 'artifacts/cards/a3/IDENTITY_OK.txt*' \| paste -sd ' ' -` | `artifacts/cards/a3/IDENTITY_OK.txt artifacts/cards/a3/IDENTITY_OK.txt.path_proof.txt` |
| E-09-040 | python tools/evidence/generate_hde_epic037_parent_binding.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; output: checked HDE-EPIC037 PR-05 parent-binding artifacts |
| E-09-041 | python tools/evidence/generate_db_runtime_posture.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-042 | python tools/evidence/generate_bodygraph_policy_proofs.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-043 | python tools/evidence/generate_v2_mapped_cache_evidence.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; output: V2_MAPPED_CACHE_EVIDENCE_OK |
| E-09-044 | python ci/checks/check_direct_db_contract.py  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; output: DIRECT_DB_CONTRACT_OK |
| E-09-045 | python tools/evidence/generate_hde_epic038_direct_db_selection.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; (no output) |
| E-09-046 | python tools/evidence/generate_epic031_pr02_log_posture.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; output: EPIC031_PR02_LOG_POSTURE_OK |
| E-09-047 | python tools/evidence/generate_epic031_pr03_evidence_coherence.py --check  (disposable clone {SCRATCH}/clone, closed rails) | exit 0; output: EPIC031_PR03_EVIDENCE_COHERENCE_OK |
| E-09-050 | `printf '%s %s\n' "$(wc -l < audit/ops/hde-epic040/ops01/SHA256SUMS)" "$(cd audit/ops/hde-epic040/ops01 && sha256sum -c SHA256SUMS \| grep -c ': OK$')"` | `7 7` |
| E-09-3202 | `python3 -I -B {W:c3-pf12}/q.py manifest_facts` | `keys=built_at_utc,files,root,version root=catalog/ version=1.3.0 built_at_utc=2026-08-24T18:04:49Z files=45 unique=True ascii_sorted=True self_listed=False canonical=True release_id=77204764c225b6458…` |
| E-09-3204 | `python3 -I -B {W:c3-pf12}/q.py manifest_history_find 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` | `hits=1 8999bd0599e0230ec41b2e06675c35f326ceb111 2026-09-26 version=1.3.0 files=45 built_at_utc=2026-08-24T18:04:49Z` |
| E-09-3205 | `python3 -I -B {W:c3-pf12}/q.py manifest_history_count 2026-10-09` | `commits_after_2026-10-09=4 822ce15cb157e8d598859e8480debaf893aaae66 589253800bd8e9c3c68431c640c8c265f6761b83 2f3db0a0090069022f7043484e99306d45b3e279 c98d41f3966d824c0fbc5cf2af0a141c1be5e247` |
| E-09-3628 | `tools/evidence/run_sanity_pipeline.py:138` | `_py("tools/evidence/update_evidence_index.py", "--check"),),` |
| E-09-3654 | `python3 -I -B {W:c4-pf14a}/catrow.py 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b POST:/api/reader GET:/reader HEAD:/reader` | `POST /api/reader public_reader a7=False; GET /reader dev_harness a7=True; HEAD /reader dev_harness a7=True` |
| E-09-3776 | `audit/EPIC-030_QA_RCA.md:40` | `NOT FINAL until all required primary logs, discovery artifact, QA RCA, step-log` |
| E-09-4154 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:222` | `2.1 GCFPE model and reasoning-level guidance is the TypeSafe reading` |
| E-09-4156 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md:1689` | `2.16 HDE-CRD-0002 WU-PR-07: PR work-unit lineage review v1.0` |
| E-09-4165 | `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md:1956` | `Task status: Done` |
| E-09-4166 | `git show 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md \| grep -A8 -E 'Subtask HDE-FERM006\.[1-4] ' \| grep -c 'Subtask status: Done'` | `4` |
| E-09-4168 | `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md:2250` | `Task status: Done` |
| E-09-4170 | `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md:2438` | `Task status: Done` |
| E-09-4280 | `artifacts/vendor/hdapi_v2/source_selection.snapshot.json:1` | `HDE-EPIC034 PR-01 HDE-FERM007.1 route-family source selection only` |
| E-09-4282 | `docs/acceptance_map_epic034.json:1` | `scope_supported_by_this_pr":["HDE-FERM008.2"]` |
| E-09-4283 | `docs/acceptance_map_epic037.json:1` | `"pf09_subtask_id":"HDE-FERM008.12"` |
| E-10-009 | `wc -l .github/workflows/ci.yml .github/workflows/epic-closeout-validation.yml .audit_src/.github/workflows/ci.yml \| awk '{print $1}' \| paste -sd' ' -` | `420 217 18 655` |
| E-10-011 | `python3 -I -B {W:w5-tests-ci}/scripts/classifier_tables.py tables \| wc -l` | `62` |
| E-10-012 | `echo "$(git ls-files tests \| wc -l) $(git ls-files tests \| grep -cE '(^\|/)test_[^/]*\.py$') $(git ls-files tests \| grep -cE '(^\|/)conftest\.py$') $(git ls-files tests \| grep -c '\.py$') $(git ls-file…` | `255 215 2 223 32` |
| E-10-032 | `python3 -I -B {W:w5-tests-ci}/scripts/testpaths_check.py summary` | `entries=80 dir=10 file=70 absent=0 tests_test_files=215 covered=134 uncovered=81` |
| E-10-053 | `echo "$(wc -l < tests/conftest.py) $(wc -l < tests/provider/conftest.py)"` | `6 348` |
| E-10-165 | `tests/retired_tests.md:65` | `` `tests/reader_v1/test_cli_proof.py` `` |
| E-10-174 | `.github/workflows/ci.yml:4` | `  pull_request:` |
| E-10-175 | `.github/workflows/ci.yml:5` | `    paths:` |
| E-10-177 | `.github/workflows/ci.yml:7` | `- '!docs/crd/**'` |
| E-10-178 | `.github/workflows/ci.yml:8` | `- '!docs/ephemeral/**'` |
| E-10-180 | `.github/workflows/ci.yml:10` | `- '!docs/pfcanon/**'` |
| E-10-184 | `.github/workflows/ci.yml:14` | `- '!docs/run/**'` |
| E-10-188 | `sed -n '18p' .github/workflows/ci.yml \| tr -d ' '` | `push:` |
| E-10-191 | `.github/workflows/ci.yml:21` | `    paths:` |
| E-10-193 | `diff <(sed -n '6,17p' .github/workflows/ci.yml) <(sed -n '22,33p' .github/workflows/ci.yml) >/dev/null && echo identical` | `identical` |
| E-10-213 | `.github/workflows/ci.yml:59` | `ref: ${{ github.event.pull_request.head.sha \|\| github.sha }}` |
| E-10-228 | `.github/workflows/ci.yml:85` | `python-version: '3.12'` |
| E-10-294 | `.github/workflows/ci.yml:232` | `ci/checks/check_mirror_schema.sh` |
| E-10-336 | `.github/workflows/ci.yml:420` | `echo "CI_APPLICABILITY_AND_EXACT_HEAD_OK"` |
| E-10-438 | `ci/checks/classify_ci_changes.py:25` | `LANES = ("product", "compat", "db", "rails", "evidence", "qa", "release")` |
| E-10-442 | `ci/checks/classify_ci_changes.py:41` | `_FULL_VALIDATION_SUPPLEMENTAL_TESTS = (` |
| E-10-446 | `ci/checks/classify_ci_changes.py:171` | `_DOCUMENTATION_PREFIXES = (` |
| E-10-571 | `python3 -I -B {W:w5-tests-ci}/scripts/classifier_tables.py supplemental_count` | `entries=109 distinct=109 tracked=109 sorted=True` |
| E-10-612 | `grep -o -E 'tests/[A-Za-z0-9_./-]+' .github/workflows/ci.yml \| sort -u \| wc -l` | `39` |
| E-10-616 | `python3 -I -B {W:w5-tests-ci}/scripts/naming_counts.py summary \| paste -sd' ' -` | `T=215 ci_tokens=39 ci_file_tokens=37 ci_dir_tokens=2 A_exact=37 A_with_dirs=49 B=109 C_exact=205 C_with_dirs=215 A_or_B_or_C=215 D=0 D_strict=10 B_subset_C=True A_subset_C=True A_and_B=0` |
| E-10-617 | `for f in $(git ls-files tests \| grep -E '(^\|/)test_[^/]*\.py$'); do grep -q -F "\"$f\"" ci/checks/classify_ci_changes.py && echo y \|\| echo n; done \| sort \| uniq -c \| awk '{print $2"="$1}' \| paste -sd…` | `n=10 y=205` |
| E-10-619 | `python3 -I -B {W:w5-tests-ci}/scripts/venn.py \| tr '\t' ':' \| paste -sd' ' -` | `---:10 --M:59 -B-:64 -BM:45 A--:10 A-M:27 A=37 B=109 M=131 none=10` |
| E-10-620 | `.github/workflows/ci.yml:177` | `            tests/db` |
| E-10-621 | `.github/workflows/ci.yml:143` | `            tests/order` |
| E-10-622 | `cmp <(PYTHONDONTWRITEBYTECODE=1 python3 -I -B {W:w5-tests-ci}/scripts/naming_counts.py unnamed_strict_extra) {W:w5-tests-ci}/unnamed_tests.txt && echo same` | `same` |
| E-10-626 | `python3 -I -B {W:w5-tests-ci}/scripts/fullval_union.py \| head -n 1` | `fullval_files=166 ci_yml_reach=49 ci_jobs_tests=3 union=215 of 215` |
| E-10-630 | `tools/qa/qa_harness.py:49` | `class Status(str, Enum):` |
| E-10-631 | `tools/qa/qa_harness.py:50` | `    PASS = "PASS"` |
| E-10-632 | `tools/qa/qa_harness.py:51` | `FAIL_BEHAVIOR = "FAIL_BEHAVIOR"` |
| E-10-633 | `tools/qa/qa_harness.py:52` | `FAIL_TOOLING = "FAIL_TOOLING"` |
| E-10-634 | `tools/qa/qa_harness.py:53` | `TOOLING_BLOCKED = "TOOLING_BLOCKED"` |
| E-10-635 | `tools/qa/qa_harness.py:54` | `PARKED = "PARKED"` |
| E-10-686 | `ci/checks/check_mirror_schema.sh:1` | `#!/usr/bin/env python3` |
| E-10-901 | python -m pytest -q -p no:cacheprovider  (disposable clone {SCRATCH}/clone-tests, venv {SCRATCH}/venv-tests) | exit 0; 3240 passed, 3 skipped in 635.58s (0:10:35) |
| E-10-902 | python -m pytest -q -p no:cacheprovider -rfEs tests  (same clone) | exit 1; 1 failed, 5855 passed, 3 skipped, 2 xfailed, 5 warnings in 2713.54s (0:45:13) |
| E-10-903 | the failing test rerun alone (same clone), with and without APP_ENV=dev PYTHONDONTWRITEBYTECODE=1; its file alone | exit 1 (1 failed in 0.35s); exit 1 (1 failed in 0.27s); 1 failed, 98 passed in 0.80s |
| E-10-904 | tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest run alone three times (same clone, APP_ENV=dev PYTHONDONTWRITEBYTECODE=1) | exit 0 three times (1 passed in 1.19s, 1.24s, 1.27s) |
| E-10-910 | GitHub Actions run list (30 most recent runs, repository-wide), read through the GitHub connector about 2026-10-26T18:33Z | no run with head SHA 0adce9d…; newest run 40359063642 created 2026-10-26T16:26:00Z |
| E-10-911 | GitHub Actions run 40359063642, job 121699262919 (log tail), read through the GitHub connector | push on head 1fb4731ba23a; conclusion failure; step 9 1 failed, 4528 passed, 2 skipped; step 17 failed without CI_APPLICABILITY_AND_EXACT_HEAD_OK |
| E-10-912 | GitHub Actions run list (main push runs before 40359063642), read through the GitHub connector | 19 runs back to 2026-10-18T08:34:37Z all success; pull_request runs 40353776329 and 40353776342 success on a90029c3b733 |
| E-10-913 | `for d in tests/order tests/http; do printf '%s=%s\n' $d $(git ls-files -- $d \| grep -c '/test_[^/]*\.py$'); done \| paste -sd ' ' -` | `tests/order=2 tests/http=6` |
| E-10-914 | `grep -n -F 'ci/checks/check_mirror_schema.sh' .github/workflows/ci.yml \| cut -d: -f1 \| paste -sd ' ' -` | `232` |
| E-10-915 | `sed -n '270p' tests/provider/conftest.py \| grep -c -F 'os.environ.get("SAFE_MODE", "1")'` | `1` |
| E-10-916 | `git merge-base --is-ancestor 1fb4731 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b && git log --format=%h 1fb4731..0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b \| wc -l && git diff --name-only 1fb4731 0adce9d9…` | `5\|docs/ephemeral/=6 docs/pfcanon/=1` |
| E-10-917 | `git show --name-status --format= 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b \| tr '\t' ' '` | `R097 docs/pfcanon/PF10-HDE-Build-Notes-v13.8.5.md docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md` |
| E-10-918 | `git ls-files -- tools/qa/step_log_header.py tests/qa/test_qa_tool_ownership.py tools/qa/qa_harness.py tests/qa/test_generic_qa_harness.py tests/evidence/test_evidence_index_missing_state.py \| paste -…` | `tests/evidence/test_evidence_index_missing_state.py tests/qa/test_generic_qa_harness.py tests/qa/test_qa_tool_ownership.py tools/qa/qa_harness.py tools/qa/step_log_header.py` |
| E-10-919 | `git grep -n -E 'def (validate_crd_check_family\|_publish_with_rollback\|publish_crd_check_family)\b' -- tools/qa/qa_harness.py tools/evidence/update_evidence_index.py \| cut -d'(' -f1 \| paste -sd'\|' -` | `tools/evidence/update_evidence_index.py:5166:def publish_crd_check_family\|tools/qa/qa_harness.py:1763:def validate_crd_check_family\|tools/qa/qa_harness.py:2321:def _publish_with_rollback` |
| E-10-2480 | `git ls-tree 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b ci/checks/check_mirror_schema.sh \| cut -c1-6` | `100755` |
| E-10-4003 | `tests/retired_tests.md:64` | `` `tests/qa/test_epic022_close_pack_ready.py` \| Inactive set. `` |
| E-11-001 | `adapter/http_reader.py:1158` | `bp = get_reader_bp()` |
| E-11-002 | `adapter/http_reader.py:669` | `def get_reader_bp(emit_fn=None):` |
| E-11-003 | `adapter/http_reader.py:678` | `emit_fn = emit_reader_public_bytes` |
| E-11-004 | `adapter/http_reader.py:679` | `bp = Blueprint("reader_v1", __name__)` |
| E-11-009 | `adapter/factory.py:13` | `app.register_blueprint(bp, url_prefix="")` |
| E-11-010 | `adapter/factory.py:14` | `app.register_blueprint(api_bp, url_prefix="/api")` |
| E-11-012 | `adapter/wsgi.py:23` | `app.register_blueprint(reader_bp)` |
| E-11-013 | `adapter/wsgi.py:24` | `app.register_blueprint(reader_api_bp, url_prefix="/api")` |
| E-11-024 | `adapter/http_reader.py:665` | `bp.record(_refuse_unrouted_methods)` |
| E-11-025 | `adapter/http_reader.py:648` | `def _refuse_unrouted_methods(state):` |
| E-11-026 | `adapter/http_reader.py:663` | `state.app.before_request(_governed_405_for_unrouted_methods)` |
| E-11-027 | `adapter/http_reader.py:640` | `@bp.route("/reader", methods=["POST"], provide_automatic_options=False)` |
| E-11-028 | `adapter/http_reader.py:641` | `def reader_post():` |
| E-11-029 | `adapter/http_reader.py:642` | `return _production_reader_response(emit_fn)` |
| E-11-030 | `adapter/http_reader.py:525` | `def _production_reader_response(emit_fn):` |
| E-11-031 | `adapter/http_reader.py:532` | `version = _select_reader_version(("1", "2"))` |
| E-11-032 | `adapter/http_reader.py:392` | `def _select_reader_version(allowed: tuple[str, ...]) -> str:` |
| E-11-034 | `adapter/http_reader.py:380` | `_READER_VERSIONS = {"1": "v1", "2": "v2"}` |
| E-11-035 | `adapter/http_reader.py:403` | `raise _ReaderFailure("ERR_READER_INVALID_VERSION", 400)` |
| E-11-048 | `engine/db/adapter.py:106` | `def for_current_env(` |
| E-11-049 | `engine/db/adapter.py:113` | `retired = retired_db_transport_keys_present(env)` |
| E-11-105 | `engine/config/registry_loader.py:1506` | `def load_active_mechanics_bundle() -> AdmittedMechanicsBundle:` |
| E-11-112 | `engine/config/registry_loader.py:1219` | `def _validate_admitted_manifest(manifest: Manifest) -> None:` |
| E-11-131 | `engine/compat/compute.py:346` | `core = compute_core(lo.gates, hi.gates, bundle, release_id)` |
| E-11-132 | `engine/core/core.py:209` | `def compute_core(member_a, member_b, mechanics_bundle, release_id)` |
| E-11-151 | `engine/core/core.py:238` | `raise ValueError("invalid pure core contract") from None` |
| E-11-186 | `engine/runtime/public.py:68` | `def emit_reader_public_envelope(` |
| E-11-192 | `engine/runtime/public.py:109` | `return emit(enriched)` |
| E-11-193 | `presenter/reader_v1/emitter.py:115` | `def emit_reader_v1(enriched: Dict[str, Any])` |
| E-11-194 | `presenter/reader_v1/emitter.py:123` | `def emit_reader_v2(enriched: Dict[str, Any])` |
| E-11-199 | `presenter/reader_v1/emitter.py:107` | `pre_bytes = emitter.emit_public(preimage)` |
| E-11-206 | `engine/stable/sercanon.py:25` | `def serialize(obj: dict[str, Any], *, sort_keys: bool = True) -> bytes:` |
| E-11-207 | `engine/stable/sercanon.py:22` | `return json.dumps(obj, ensure_ascii=False, separators=_COMPACT_SEPS` |
| E-11-208 | `engine/stable/sercanon.py:29` | `return (s + "\n").encode("utf-8")` |
| E-11-227 | `adapter/http_reader.py:644` | `methods=["GET", "HEAD", "OPTIONS", "PUT", "PATCH", "DELETE"` |
| E-11-228 | `adapter/http_reader.py:645` | `def reader_method_not_allowed():` |
| E-11-229 | `adapter/http_reader.py:646` | `return _reader_method_not_allowed("POST")` |
| E-11-230 | `adapter/http_reader.py:407` | `def _reader_method_not_allowed(allow: str) -> Response:` |
| E-11-231 | `adapter/http_reader.py:411` | `body = emit_public(error_envelope("ERR_NOT_FOUND"))` |
| E-11-232 | `adapter/http_reader.py:415` | `resp.headers["Allow"] = allow` |
| E-11-233 | `adapter/http_reader.py:659` | `MethodNotAllowed) and request.path == route:` |
| E-11-234 | `adapter/http_reader.py:681` | `@bp.get("/reader")` |
| E-11-237 | `adapter/http_reader.py:687` | `if not _reader_dev_env_explicit():` |
| E-11-239 | `adapter/http_reader.py:389` | `return os.environ.get("APP_ENV") == "dev"` |
| E-11-240 | `adapter/http_reader.py:688` | `return _error("ERR_READER_FORBIDDEN", 403)` |
| E-11-266 | `engine/http/compat_handler.py:19` | `compat_blueprint = Blueprint("compat", __name__, url_prefix="/api/compat/v1")` |
| E-11-267 | `adapter/factory.py:15` | `app.register_blueprint(compat_blueprint)` |
| E-11-268 | `adapter/wsgi.py:25` | `app.register_blueprint(compat_blueprint)` |
| E-11-269 | `adapter/http_reader.py:1260` | `app.register_blueprint(compat_blueprint)` |
| E-11-270 | `engine/http/compat_handler.py:108` | `@compat_blueprint.before_app_request` |
| E-11-271 | `engine/http/compat_handler.py:109` | `def _compat_writer_transport_guard():` |
| E-11-274 | `engine/http/compat_handler.py:112` | `if _compute_env_mode(os.environ) == "prod":` |
| E-11-275 | `engine/http/compat_handler.py:113` | `return compat_error_response(404)` |
| E-11-276 | `engine/http/compat_handler.py:42` | `def compat_error_response(status: int, *, allow: str \| None = None) -> Response:` |
| E-11-281 | `engine/http/compat_handler.py:130` | `@compat_blueprint.route("", methods=["POST"], provide_automatic_options=False)` |
| E-11-314 | `engine/http/compat_handler.py:122` | `@compat_blueprint.get("")` |
| E-11-315 | `engine/http/compat_handler.py:123` | `def get_ids_only():` |
| E-11-317 | `engine/http/compat_handler.py:180` | `@compat_blueprint.route("", methods=["HEAD"], provide_automatic_options=False)` |
| E-11-319 | `engine/http/compat_handler.py:185` | `methods=["OPTIONS"], provide_automatic_options=False)` |
| E-11-327 | `pyproject.toml:14` | `hdctl = "engine.cli.main:cli"` |
| E-11-328 | `engine/cli/main.py:284` | `def cli(argv: list[str] \| None = None) -> int:` |
| E-11-329 | `engine/cli/main.py:285` | `argv = list(sys.argv[1:] if argv is None else argv)` |
| E-11-339 | `engine/cli/main.py:309` | `return int(handler(args) or 0)` |
| E-11-388 | `engine/cli/main.py:570` | `def _emit_stdout_bytes(payload: bytes) -> None:` |
| E-11-389 | `engine/cli/main.py:572` | `raise CliError("STDOUT_MISSING_LF")` |
| E-11-390 | `engine/cli/main.py:574` | `raise CliError("STDOUT_CRLF")` |
| E-11-440 | `engine/bodygraph/resolver.py:704` | `return classify_bg_resolve_route_policy(base_url)` |
| E-11-470 | `engine/cli/main.py:812` | `reader_bytes, _reader_envelope = emit_reader_public_envelope(` |
| E-11-486 | `engine/cli/main.py:829` | `_emit_stdout_bytes(emitter.emit_public(result))` |
| E-11-487 | `engine/cli/main.py:140` | `aux = sub.add_parser(` |
| E-11-488 | `engine/cli/main.py:151` | `aux.set_defaults(handler=aux_preview)` |
| E-11-489 | `engine/cli/main.py:594` | `def aux_preview(args: argparse.Namespace) -> int:` |
| E-11-499 | `engine/cli/main.py:618` | `band = args.band` |
| E-11-533 | `engine/cli/main.py:186` | `dev_sampler = sub.add_parser(` |
| E-11-534 | `engine/cli/main.py:203` | `dev_sampler.set_defaults(handler=dev_sampler_run)` |
| E-11-535 | `engine/cli/main.py:928` | `def dev_sampler_run(args: argparse.Namespace) -> int:` |
| E-11-563 | `adapter/http_reader.py:901` | `def _dev_admin_gate() -> Response \| None:` |
| E-11-564 | `adapter/http_reader.py:904` | `if os.environ.get("APP_ENV") in {"dev", "test", "local"}:` |
| E-11-565 | `adapter/http_reader.py:907` | `return _writer_error("ERR_WRITER_FORBIDDEN", status=403)` |
| E-11-619 | `engine/cli/main.py:152` | `bg = sub.add_parser(` |
| E-11-620 | `engine/cli/main.py:157` | `bg.add_argument("--user", required=True, help="BodyGraph user identifier")` |
| E-11-621 | `engine/cli/main.py:161` | `default="auto",` |
| E-11-622 | `engine/cli/main.py:179` | `_ALLOW_PROD_VENDOR,` |
| E-11-623 | `engine/cli/main.py:184` | `bg.set_defaults(handler=bg_resolve)` |
| E-11-624 | `engine/cli/main.py:259` | `def bg_resolve(args: argparse.Namespace) -> int:` |
| E-11-639 | `engine/cli/main.py:279` | `output = emitter.emit_public(result.payload).decode("utf-8")` |
| E-11-640 | `engine/cli/main.py:280` | `sys.stdout.write(output)` |
| E-11-677 | `sed -n '124,153p' engine/bodygraph/vendor_client.py \| grep -c '"supported": True'` | `2` |
| E-11-678 | `engine/bodygraph/resolver.py:416` | `if not route_policy["supported"]:` |
| E-11-679 | `engine/bodygraph/resolver.py:418` | `str(route_policy["error_code"]),` |
| E-11-688 | `engine/bodygraph/resolver.py:444` | `if route_policy["route_family"] == "recommended_v2_chart":` |
| E-11-689 | `engine/bodygraph/resolver.py:445` | `return _resolve_vendor_v2_chart(` |
| E-11-741 | `engine/bodygraph/mapped_cache.py:60` | `def persist_mapped_bodygraph(db: DBAccess, cache: Mapping` |
| E-11-745 | `engine/bodygraph/mapped_cache.py:65` | `required = {"user_id", "vendor", "vendor_version", "input_fingerprint"` |
| E-11-746 | `engine/bodygraph/mapped_cache.py:19` | `_EXPECTED_POSTURE = "adapter_mapped_no_raw_vendor_payload"` |
| E-11-782 | `tools/evidence/update_evidence_index.py:5329` | `    main()` |
| E-11-783 | `tools/evidence/update_evidence_index.py:5294` | `def main(argv: list[str] \| None = None) -> None:` |
| E-11-784 | `tools/evidence/update_evidence_index.py:5296` | `parser.add_argument("--check", action="store_true"` |
| E-11-901 | `tools/config/generate_config_artifacts.py:416` | `raise SystemExit(_main())` |
| E-11-902 | `tools/config/generate_config_artifacts.py:386` | `def _main(argv: list[str] \| None = None) -> int:` |
| E-11-903 | `tools/config/generate_config_artifacts.py:392` | `modes.add_argument("--compare-goldens", metavar="CANDIDATE_ROOT"` |
| E-11-935 | `tools/config/artifacts.py:645` | `first = compute_core(member_a, member_b, bundle, bundle.release_id).to_payload()` |
| E-11-941 | `tools/config/artifacts.py:738` | `return emit_reader_v1(enriched)` |
| E-11-954 | `tools/bodygraph/check_magic10_gate_readiness.py:230` | `raise SystemExit(main())` |
| E-11-955 | `tools/bodygraph/check_magic10_gate_readiness.py:211` | `def main(argv: Sequence[str] \| None = None) -> int:` |
| E-11-956 | `tools/bodygraph/check_magic10_gate_readiness.py:206` | `parser.add_argument("--selection-file", type=Path, metavar="PATH",` |
| E-11-967 | `tools/bodygraph/check_magic10_gate_readiness.py:217` | `db = DBAccess.for_current_env()` |
| E-11-978 | `tools/qa/epic021_qa.py:1744` | `raise SystemExit(main())` |
| E-11-979 | `tools/qa/epic021_qa.py:1725` | `def main() -> int:` |
| E-11-980 | `tools/qa/epic021_qa.py:1727` | `ensure_determinism_env()` |
| E-11-981 | `tools/qa/epic021_qa.py:1729` | `with _WrapperWriteTransaction():` |
| E-11-982 | `tools/qa/epic021_qa.py:1429` | `class _WrapperWriteTransaction:` |
| E-11-1044 | `tools/qa/generate_epic_close_pack.py:4960` | `raise SystemExit(main())` |
| E-11-1045 | `tools/qa/generate_epic_close_pack.py:4914` | `def main(argv: Sequence[str] \| None = None) -> int:` |
| E-11-1046 | `tools/qa/generate_epic_close_pack.py:4915` | `args = _parse_args(argv)` |
| E-11-1047 | `tools/qa/generate_epic_close_pack.py:4883` | `def _parse_args(argv: Sequence[str] \| None) -> argparse.Namespace:` |
| E-11-1048 | `tools/qa/generate_epic_close_pack.py:4908` | `parser.error("exactly one --source is required")` |
| E-11-1119 | `.github/workflows/epic-closeout-validation.yml:10` | `pull_request:` |
| E-11-1120 | `.github/workflows/epic-closeout-validation.yml:13` | `- "tools/qa/generate_epic_close_pack.py"` |
| E-11-1121 | `.github/workflows/epic-closeout-validation.yml:19` | `workflow_dispatch:` |
| E-11-1138 | `scripts/cut_release_manifest.py:211` | `raise SystemExit(main())` |
| E-11-1139 | `scripts/cut_release_manifest.py:184` | `def main(argv: Sequence[str] \| None = None) -> int:` |
| E-11-1140 | `scripts/cut_release_manifest.py:186` | `parser.add_argument("--manifest", type=Path, default=ROOT` |
| E-11-1220 | `tools/evidence/run_sanity_pipeline.py:138` | `(_py("tools/evidence/update_evidence_index.py", "--check"),),` |
| E-11-1238 | `sha256sum catalog/manifest.json` | `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e  catalog/manifest.json` |
| E-11-1257 | `adapter/wsgi.py:32` | `resp.headers.setdefault("X-Release-Id", app.config.get("RELEASE_ID", ""))` |
| E-11-1258 | `adapter/wsgi.py:15` | `app.config.setdefault("RELEASE_ID", "rel_dev")` |
| E-11-1272 | `adapter/factory.py:30` | `@app.errorhandler(404)` |
| E-11-1275 | `adapter/factory.py:35` | `@app.errorhandler(405)` |
| E-11-1277 | `adapter/factory.py:43` | `@app.after_request` |
| E-11-1280 | `adapter/http_reader.py:1287` | `@app.errorhandler(404)` |
| E-11-1281 | `adapter/http_reader.py:1293` | `@app.errorhandler(405)` |
| E-11-1295 | `adapter/wsgi.py:53` | `@app.errorhandler(404)` |
| E-11-1296 | `adapter/wsgi.py:60` | `@app.errorhandler(405)` |
| E-11-1298 | `adapter/wsgi.py:27` | `def _apply_common_headers(resp: Response) -> Response:` |
| E-11-1300 | `adapter/wsgi.py:38` | `resp.headers.setdefault("Strict-Transport-Security"` |
| E-11-1371 | `adapter/http_reader.py:1320` | `host="127.0.0.1",` |
| E-11-1383 | `scripts/scratch.py:4` | `from adapter.wsgi import create_app` |
| E-11-1393 | `scripts/qa/dev_sampler_healthcheck.py:133` | `"-m", "adapter.http_reader"` |
| E-11-1394 | `scripts/qa/dev_sampler_healthcheck.py:129` | `# Reader runner binds to 0.0.0.0; host is used for readiness checks only.` |
| E-11-1397 | `ci/checks/classify_ci_changes.py:266` | `"dev/reader_harness/app.py": {"product"},` |
| E-11-1398 | `.audit_src/dev/reader_harness/app.py:17` | `app = create_app()` |
| E-11-1399 | `tools/evidence/run_sanity_pipeline.py:105` | `"11 Human Index and Machine Mirror refresh", "12 Evidence-path validation",` |
| E-11-1400 | `tools/evidence/run_sanity_pipeline.py:137` | `STAGE_NAMES[10],` |
| E-11-1401 | `engine/bodygraph/vendor_client.py:378` | `str(policy["error_code"]),` |
| E-11-1402 | `engine/bodygraph/vendor_client.py:364` | `policy = classify_bg_resolve_route_policy(self._base_url)` |
| E-11-1403 | `engine/runtime/identity.py:138` | `{**_STATIC_IDENTITY, "release_id": _manifest_release_id()}` |
| E-11-3177 | `tools/evidence/run_canonical_json_gate.py:803` | `tempfile.TemporaryDirectory(prefix="canonical-manifest-")` |
| E-11-3194 | `tools/evidence/run_canonical_json_gate.py:847` | `tempfile.TemporaryDirectory(prefix="canonical-registry-")` |
| E-11-3202 | `tools/evidence/run_canonical_json_gate.py:866` | `os.chdir(path)` |
| E-11-3209 | `tools/evidence/run_canonical_json_gate.py:874` | `tempfile.TemporaryDirectory(prefix="canonical-narratives-")` |
| E-11-3319 | `tools/ops/internal_version_artifacts.py:81` | `base_dir.mkdir(parents=True, exist_ok=True)` |
| E-11-3325 | `tools/ops/internal_version_artifacts.py:135` | `update_evidence_index._write_path_proof(check=False, **proof_kwargs)` |
| E-11-3569 | `tools/evidence/update_evidence_index.py:3598` | `proof_rel = f"{rel}.path_proof.txt"` |
| E-11-3663 | `tools/evidence/run_canonical_json_gate.py:1168` | `for target in sorted(targets, key=lambda t: t.rel_path):` |
| E-11-3664 | `tools/evidence/run_canonical_json_gate.py:1203` | `_validate_target(target, obj)` |
| E-11-3665 | `tools/evidence/run_canonical_json_gate.py:1204` | `except Exception as exc:  # validators deliberately fail closed` |
| E-11-3666 | `tools/evidence/run_canonical_json_gate.py:1408` | `if check_only:` |
| E-11-3765 | `tools/evidence/run_canonical_json_gate.py:1110` | `def _write_path_proof(rel_path: str, *, produced_at: str) -> None:` |
| E-11-3766 | `tools/evidence/run_canonical_json_gate.py:1113` | `update_evidence_index._write_path_proof(` |
| E-11-3767 | `tools/evidence/run_canonical_json_gate.py:1114` | `rel=rel_path,` |
| E-11-3768 | `tools/evidence/run_canonical_json_gate.py:1120` | `check=False,` |
| E-11-5203 | `tools/evidence/regenerate_identity_closure.py:180` | `CLOSURE_STEPS = (` |
| E-11-5204 | `git grep -c "ClosureStep(" 0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b -- tools/evidence/regenerate_identity_closure.py` | `0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b:tools/evidence/regenerate_identity_closure.py:18` |
| E-11-5223 | `tools/evidence/regenerate_identity_closure.py:426` | `if os.environ.get("HDE_ISOLATED_RELEASE_BUILD") != "1":` |
| E-11-5224 | `tools/evidence/regenerate_identity_closure.py:431` | `if not args.in_place_isolated:` |
| E-11-5284 | `tools/evidence/run_canonical_json_gate.py:1416` | `for path in outputs:` |
| E-11-5285 | `tools/evidence/run_canonical_json_gate.py:1113` | `update_evidence_index._write_path_proof(` |
| E-11-5331 | `tools/evidence/generate_bodygraph_policy_proofs.py:33` | `"sel": ROOT / "artifacts/bodygraph/source_selection.snapshot.json",` |
| E-11-5332 | `tools/evidence/generate_bodygraph_policy_proofs.py:37` | `"run_schema": ROOT / "schemas/bodygraph_source_invariance.run.v2.json",` |
| E-11-5333 | `tools/evidence/generate_bodygraph_policy_proofs.py:38` | `"summary_schema": ROOT / "schemas/bodygraph_source_invariance.summary.v2.json",` |
| E-11-5341 | `tools/evidence/generate_v2_mapped_cache_evidence.py:36` | `OUT = ROOT / "artifacts/bodygraph/v2_mapped_cache"` |
| E-11-5342 | `tools/evidence/generate_v2_mapped_cache_evidence.py:37` | `TRANSCRIPT_SCHEMA = ROOT / "schemas/bodygraph_v2_mapped_cache_transcript` |
| E-11-5343 | `tools/evidence/generate_v2_mapped_cache_evidence.py:38` | `MANIFEST_SCHEMA = ROOT / "schemas/bodygraph_v2_mapped_cache_manifest.v1.json"` |
| E-11-6738 | `tools/qa/qa_harness.py:3434` | `Status.FAIL_TOOLING,` |
| E-11-6742 | `tools/qa/qa_harness.py:3441` | `return Status.PASS` |
| E-11-6813 | `tools/qa/qa_harness.py:3806` | `all_statuses = [status for status, _ in issues] + [` |
| E-11-6937 | `tools/qa/qa_harness.py:1469` | `if not statuses:` |
| E-11-6938 | `tools/qa/qa_harness.py:1472` | `Status.FAIL_TOOLING,` |
| E-11-9293 | `tools/evidence/orientation_demo.py:26` | `# Evidence refresh order: update_evidence_index.py must run first (write mode)` |
| E-11-9294 | `tools/evidence/orientation_demo.py:27` | `then generate_orientation(check=False) should` |
| E-11-9295 | `tools/evidence/orientation_demo.py:152` | `# Compatibility write mode has no independent write authority.  The` |
| E-11-9296 | `tools/evidence/orientation_demo.py:154` | `update_evidence_index([])` |

## Provenance

- **How it was made.** The producer and read-only workers drafted every section under written rules: read-only, closed rails, evidence for every fact, complete populations, no judgement. The workers were W1–W9 (inspection and canon claim catalogues), G1–G6 (gap reads of function bodies), P1 and P2 (the `AGENTS.md` and `README.md` posture checks) and C1–C5 (the canon comparisons). The producer read every draft in full and re-checked its evidence when it was handed back.
- **Final re-verification.** Started 2026-10-27T00:03:55Z at `0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b` with a clean checkout. 23,308 of 23,308 file-line citations matched their excerpts, and 3,494 of 3,494 recorded commands gave their recorded results. Failures: 0. The ids in this file are a subset of those checked.
- **Corrections made by the producer.**
  - Six claim rows of the comparison drafts cited the wrong evidence id. Each was corrected to the id that holds the fact: K-10-919, K-10-930, K-10-992, K-10-1022, K-10-1045 and P-A-005.
  - The environment statement in §1 was corrected. It had said the database and vendor variables were unset.
- **Not in this file.** The complete working record (7 MB): every canon claim row with its comparison, the full evidence registers, all 1,033 N- proofs, the worker drafts and the helper scripts. It stays in the producer's session scratchpad and is not published.
- **Repository writes.** This file is the only path the audit adds to the repository. No PF canon file, generated evidence, index or path proof was written, and no generator ran in write mode.
