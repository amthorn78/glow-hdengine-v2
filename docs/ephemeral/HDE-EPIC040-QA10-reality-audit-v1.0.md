---
artifact_type: REALITY_AUDIT
artifact_id: HDE-EPIC040-QA10-REALITY-AUDIT
artifact_version: "1.0"
predecessor: none (first QA-10 audit for this change)
state: COMPLETE
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
producer: Isis — continuing Lead Developer and whole-change readiness decision owner (the Isis-50 session that reviewed Plan v2.1 and decided PR04-F01 and PR06a)
session_disposition: RETAIN_EXISTING
role_session_ref: Isis-50 (Product Owner-assigned continuing session)
invocation_binding: EPIC / HDE-EPIC040 / QA-10 / whole change
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-10 — Audit Implementation and Establish QA Readiness — 091426.1 (Notion 3db4590a05eb818bad2fcb4bc2610b29; page as of 2026-09-24T15:51:30Z; 84,484 chars read in full)
observed_revision: 39b9cdf (origin/main, "HDE-EPIC040: DOC-20 documentation completion v1.0 (COMPLETE) (#531)")
observation_time_utc: 2026-09-27T08:00:00Z–08:40:00Z
companions:
  - docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md
  - docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-10
---

# HDE-EPIC040 — Reality Audit v1.0 (QA-10)

This is a factual record of what the repository contains at `39b9cdf`. Compliance judgements belong to the triage; the readiness decision belongs to the readiness record. Inspection is not a claim that any test or route ran, except where a read-only validator command is recorded with its result.

## 1. Audit Snapshot Metadata

| Field | Value |
| --- | --- |
| Class / change | EPIC / HDE-EPIC040 (Separation Pass 3) |
| Specification | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` (approved v1.1) |
| Plan / review | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`; `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` (Isis-50 APPROVE) |
| Delivered units | PR01 #403 `3828d4b`, PR02 #404 `5b2fb8d`, PR03 #405 `9cda1b4`, PR04 #467 `cd6f9e6`, PR05 #492 `4d7ab9d`, PR06 #501 `f7484d0`, PR06a #508 `d79cfc1`, PR06b #513 `8999bd0`, PR07 #518 `edbd414`. Each lineage review's decision is ACCEPT (PR03–PR07 state `ACCEPTED_FINAL`); inputs listed in the readiness record §2 |
| Ops | OPS01 result v1.4 PASS; receipt v1.2 ACCEPT |
| Documentation | DOC-20 completion v1.0 COMPLETE (#531) |
| Prior readiness history | None. Proof N-00: `ls docs/ephemeral \| grep -iE 'EPIC040.*(reality\|triage\|readiness\|QA-10\|qa10)'` returned no file before this audit |
| Repository | `amthorn78/glow-hdengine-v2`, local checkout, branch `claude/nice-mayer-tf9l4c` reset to `origin/main` `39b9cdf`; `git status --porcelain` empty before and after inspection |
| Method | Direct read-only inspection of the checkout by this session and five read-only workers inside this invocation (grep/find/git/python parsing), plus six read-only validator commands (§9). No install, generator, test, route probe, network, vendor or DB call |
| Limitations | One worker import created an ignored `ci/checks/__pycache__/` file; it was removed and the tree verified clean. Runtime, deployed and hosted-CI state are Unknown. Samples are labelled where a unit was not read in full |
| Canon read | PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.8.md` (SHA-256 `980c4b05…`, 288,869 chars, read in full); PF23 `docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.md` (99,607 chars, read in full); targeted sections of PF05 v2.5.2 as cited by the Plan Review |

## 2. Top-level Repo Map

- **E-A01** Tree clean at `39b9cdf` (`git status --porcelain | wc -l` → 0).
- **E-A02** Tracked roots and file counts: `.audit_src/` 485, `.backup_epic004/` 6, `.devcontainer/` 3, `.github/` 3, `.vscode/` 1, `_arch/` 147, `_archive/` 29, `adapter/` 17, `artifacts/` 1026, `audit/` 3080, `catalog/` 25, `ci/` 13, `codex/` 37, `config/` 2, `dev/` 4, `docs/` 1508, `engine/` 101, `errors/` 10, `fixtures/` 17, `freeze/` 1, `goldens/` 26, `handoff/` 49, `internal/` 5, `math/` 1, `migrations/` 3, `narratives/` 10, `notes/` 21, `parity/` 17, `presenter/` 4, `proofs/` 6, `release/` 1, `reports/` 2, `scan_reports/` 2, `schemas/` 46, `scripts/` 66, `sql/` 1, `tests/` 316, `tools/` 99, `validation/` 2.
- **E-A02b** Root files include project docs (`README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, …), build/run files (`pyproject.toml`, `Procfile`, `requirements*.txt`, `pytest.ini`, `run_flask.py`, …), EPIC023 step reports, and scratch files (`big.json`, `patch.diff`, `temp_run.*`, `.tmp_refusal_*.txt`, `changes_report.txt`, `manifest_pre.sha256`, `manifest_post.sha256`).
- **E-A04** `assert`, `import` and `Run` are zero-byte files (`wc -c` → 0).
- **E-A03** One tracked path contains an em-dash (`docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md`).
- **E-A06** `docs/` second level: `ephemeral` 1268, `graph` 58, `pfcanon` 34, `prompt_ecosystem_management` 25, `schemas` 20, `evidence` 9, `plans` 8, `design` 8, `run` 6, `adr` 4, `crd` 3, `qa` 2.
- **E-A07** Evidence homes: `artifacts/` (1026), `audit/` (3080), `docs/evidence/` (Index, sentinel, proofs), `goldens/` (26). Historical prefixes are declared in `ci/checks/classify_ci_changes.py:92` (`_HISTORICAL_PREFIXES`).

## 3. Packaging and Entrypoints

- **E-A08** `pyproject.toml`: `name = "glow-hdengine"`, `version = "0.0.0"`, `dependencies = []`, `[project.scripts] hdctl = "engine.cli.main:cli"`, packages `engine*, adapter*, presenter*, catalog*, math*`, package-data `catalog = ["*.json"]`, `math = ["*.json"]`.
- **E-A12/E-A13** `requirements.txt`: psycopg[binary], Flask<3.0, gunicorn<22, jsonschema==4.23.0; `requirements-dev.txt` adds pytest, pytest-cov, pytest-mock.
- **E-A10** `Procfile:1` `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …`.
- **E-A11** Other `create_app` callers: `run_flask.py:22` (factory), `run_flask_dev.sh:21`, `scripts/start_web.sh:4`, `scripts/scratch.py:4` (wsgi), `adapter/app.py` (alias of `adapter.wsgi`), `dev/reader_harness/app.py:7` (own factory). `scripts/dev_start_reader.sh:26` runs `python -m adapter.http_reader`.
- **E-A14** Additional `hdctl` scripts outside the package: `scripts/hdctl.py`, `scripts/hdctl.clean.py`, `scripts/hdctl.backup.py`, `scripts/hdctl.py.bak`.
- **N-A01** No root `Dockerfile*`, `setup.py` or `setup.cfg` (`ls` at root → "No such file"; nested Dockerfiles not searched).
- **E-B-wheel** PF10 §2.22 (L2324) records that a non-editable wheel omits 15 of the then-44 release members and refuses `MISSING_FILE` (O-12); the packaging declarations above are unchanged since.

## 4. Engine Modules

Fully inspected: `engine/config/registry_loader.py` roster/admission block (395–449, 1219–1242) and `_deep_freeze` (1401–1406); `engine/core/core.py` from `compute_core` to end; `engine/runtime/public.py` 30–110. Sampled: the rest of the loader, `engine/compat/compute.py`, `engine/magic10/*`.

- **E-B01** `engine/` subpackages include `bodygraph cli compat config core db magic10 mech presenter runtime serializer stable`; `engine/core/` holds only `core.py`.
- **E-B02** `registry_loader.py:398-400` `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"`, `ADMITTED_RELEASE_ROSTER = tuple(sorted({...}))`.
- **E-B03** `registry_loader.py:448-449` import-time invariant `len(ADMITTED_RELEASE_ROSTER) != 45` → `RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")`.
- **E-B04** `_validate_admitted_manifest` (1219–1242): strict subset → `INCOMPLETE_RELEASE_ROSTER`; other difference → `RELEASE_ROSTER_MISMATCH`; version/timestamp → `RELEASE_VERSION_MISMATCH` / `RELEASE_TIMESTAMP_MISMATCH`.
- **E-B05** `registry_loader.py:478` `SchemaValidationError('MISSING_FILE', …)`.
- **E-B06** `load_active_mechanics_bundle()` (1506–1511): "Admit the exact installed complete mechanics release, or fail closed".
- **E-B07** `_deep_freeze` maps Mapping → `MappingProxyType`, list/tuple → tuple; other types returned unchanged (sets/bytearrays not handled).
- **E-B08** `CoreResult` is `@dataclass(frozen=True, slots=True)`; `compute_core(member_a, member_b, mechanics_bundle, release_id)` at `core.py:209` validates inputs, classifies Channels, computes signals, reduces categories and derives `pair_key` from the `magic10_pair_preimage.v1` digest; errors collapse to `ValueError("invalid pure core contract")`.
- **N-B01** No I/O imports in `engine/core engine/magic10` (pattern `import engine.db|from engine.db|vendor_client|urllib|psycopg`, grep -rn, case-sensitive → 0).
- **E-B09** `compute_core` callers: `engine/compat/compute.py:346`; tools `tools/config/artifacts.py:645-647`, `tools/evidence/generate_engine_core_evidence.py:120-123`.
- **E-B10** Compat compute requires `type(bundle) is AdmittedMechanicsBundle` else `CompatBoundaryError("admission_config")`; intrinsic cache key `INTRINSIC_CACHE_PREFIX + pair_key`, hits revalidated.
- **E-B11** Module state: `compute.py:50` `_BUNDLE_PROVIDER` (rebindable), `compute.py:52` `_SCHEMA_VALIDATORS: dict` (process cache keyed by schema SHA-256).
- **N-B02** No `lru_cache|functools.cache` in `engine/config engine/core engine/magic10 presenter engine/presenter engine/runtime/public.py` → 0; admission runs on each provider call.
- **E-B25** `catalog/channels_v1.json`: 36 Channels, every `gates[0] < gates[1]`, 36 unique pairs, no null field in any row.
- **E-B26** Config `catalog/magic10_mechanics_v1.json` (`config_id` `m10-channel-state-v1.0.0`); schemas `schemas/magic10_mechanics_v1.schema.json`, `schemas/magic10_result_v1.schema.json`, `schemas/magic10_compat_result_v1.schema.json`.
- **E-B28** 20 signals (schema pins min/max 20), 10 category weights, 3 profiles.
- **E-B29** Balance: `equilibrium_score` `twice_min_owner_mass_v1`, `counterweight_ratio` `companionship_em_mass_v1`; `registry_loader.py:1168` `SIGNAL_OPERATION_MISMATCH`; `engine/magic10/signals.py:107` "invalid Balance operation".
- **E-B-cat** `catalog/channels_catalog_v1.json` holds one placeholder row (`{'id':'alpha',…}`); it is not a roster member and no `.py` under `engine`/`tools` references it.
- **E-D26** `engine/charts/loader.py:54` reads `SAFE_MODE` from the environment; `:71` writes `loader_call.jsonl`; `:95/:168` `perf_counter`.

## 5. Adapter / HTTP Surfaces

- **E-C01/E-C02** `adapter/factory.py:11-13` registers the dev blueprint at `""`, the API blueprint at `/api`, and `compat_blueprint`; its `after_request` converts HTML 404/405 to JSON only for compat paths; no `errorhandler`.
- **E-C03/E-C04** `adapter/http_reader.py:1163-1175` `create_app` mounts the same three; its 404/405 handlers return JSON only for `/api/compat/v1`, otherwise Werkzeug HTML.
- **E-C05/E-C06/E-C07** `adapter/wsgi.py:23-25` mounts the same three; global 404/405 → JSON `ERR_NOT_FOUND`; `/internal/healthz`, `/internal/readyz`; `no-store` default and HSTS for prod-like env (`:28`, `:36-38`).
- **E-C10–E-C13** Production Reader: `http_reader.py:556` `POST /api/reader` → `_production_reader_response`; `:560` GET/HEAD/OPTIONS/PUT/PATCH/DELETE → governed 405; `:574-584` `before_request` gives unruled methods the same 405; the 405 is `ERR_NOT_FOUND`, status 405, `Cache-Control: no-store`.
- **Dev/internal routes** (`get_reader_bp`): `GET /reader` (`:597`, 403 unless `os.environ.get("APP_ENV","dev") == "dev"`, `:603`); `/api/aux/narrative`, `/aux/narrative` (`:671/672`); `POST /reader` always 405 (`:720`); `/ops/db/unavailable` (`:747`); `/ops/rails/refusal` (`:789`); `/ops/probe/env` (`:797`); `POST /internal/dev/sampler` (`:978`); `/dev/{sampler,reader,writer}/conjunction` (`:1047/1055/1063`, `_dev_admin_gate`); `/internal/version` (`:1090`, no-store, no ETag); `/ops/writer/diagnostic` (`:1114/1135/1147`).
- **E-C14** `_dev_admin_gate` (`:818-823`) allows `APP_ENV` in `{dev,test,local}`; unset or other → `ERR_WRITER_FORBIDDEN` 403.
- **E-C15** Compat blueprint `engine/http/compat_handler.py:19` prefix `/api/compat/v1`; GET `:122`, POST `:130`, HEAD `:176`, OPTIONS `:181`.
- **E-C17** `docs/ENDPOINTS_CATALOG.json` (symlink to `artifacts/audit/ENDPOINTS_CATALOG.json`, byte-identical) has 10 rows, all matched by registered routes. Registered but not catalogued: aux narrative ×2, four `/ops/*` routes, `/internal/healthz|readyz`, compat GET/HEAD/OPTIONS, and the 405-only refusals. Inclusion policy not established (Unknown).
- **Duplicate blueprint name**: `"reader_v1"` is defined in `get_reader_bp` (`:595`) and again at module level (`:1087`) as a `NameError` fallback; which object module-level routes bind to was not established (Unknown).

## 6. Presenter / Emitter

- **E-B12** `presenter/reader_v1/emitter.py`, `presenter/json_canon_compare.py`; `engine/presenter/emitter.py` (`emit_public`, `emit_public_with_envelope`, `emit_compact_json`).
- **E-B13** Category items are exactly `{id, band}`; band checked against `_CATEGORY_BANDS`.
- **E-D22** Duplicate category id raises `ValueError` (`emitter.py:41`).
- **E-B14** `_ordered_categories_v2` (`:48-62`) requires ids equal `FROZEN_MAGIC10_ORDER` when eligible, `[]` when ineligible.
- **E-B15** `engine/runtime/public.py:30-36` Reader v1 emits only `harmony` (or `[]`); `:94-100` dispatches v1/v2, else `ValueError("reader_version_unsupported")`.
- **E-B16** `_emit` (`:105-112`) hashes the five-key preimage into `idempotence_hash`.
- **E-B17** `engine/stable/sercanon.py:21-28` `json.dumps(…, ensure_ascii=False, separators=compact, sort_keys=…)` plus exactly one `\n`.
- **N-B03** `allow_nan` absent in `engine/stable engine/serializer` (grep -rn → 0).
- **E-B18** Call path: `engine/cli/main.py` → `engine.runtime` → `emit_reader_v{1,2}` → `emit_public`; also `tools/config/artifacts.py:729-738`.

## 7. CLI Surfaces

- **E-C18/E-C19** Sole console script `hdctl` → `engine/cli/main.py:cli` (`:231`); `add_subparsers(required=True)` (`:76`).
- Subcommands: `showcompat` (`:77`; `--pair-file`, `--a/--b[-file]`, `--dump-reader`, `--dump-admin-dir`, `--source db|vendor|auto`, `--conjunction` `:102`, `--viewer-prefs`, `--user-a/-b`, birth arguments); `aux-preview` (`:125`; `--band` etc.); `bg:resolve` (`:137`; `--user`, `--source`, `--upsert`, `--dry-run`, birth args); `dev:sampler` (`:165`; `_ensure_dev_admin_env` `:771-775`).
- **E-C20** showcompat help text: "Emit canonical Reader v1 bytes from vendor JSON (stdin or files)".
- Exit codes (`:231-268`): usage/argparse 64, help 0, `CliError` → its code, typed boundary/vendor/registry errors → 1, unexpected → `CLI_UNEXPECTED:` and 1; `MISSING_VENDOR_INPUT` 64 (`:210-215`).
- **E-C22** `_emit_stdout_bytes` (`:511-516`) raises `STDOUT_MISSING_LF` / `STDOUT_CRLF`.
- **E-D28** showcompat stdout is the canonical `magic10_compat_result.v1` document plus one LF (`:765-767`); the conjunction path wraps its result (`engine/compat/compute.py:426`).
- `bg:resolve` writes with `sys.stdout.write`, not `_emit_stdout_bytes`.
- `--band` with `--pair-file`: band taken from rows (`:549-554`); `args.band` used only without a pair file (`:564-567`).
- Tool CLIs: `tools/config/generate_config_artifacts.py:386` `--compare-goldens` (0 match / 1 mismatch / 5 refusal), `--goldens`, `--report`; `tools/bodygraph/check_magic10_gate_readiness.py:204-226`; `tools/evidence/update_evidence_index.py:4872-4886`.

## 8. Vendor Seam & BodyGraph Storage

- **E-B19** `engine/bodygraph/vendor_client.py:196-202` reads `HD_API_BASE_URL` / `HDAPI_BASE_URL` (conflict → `PROVIDER_CONFIG_INVALID`); `:298` https required; `:335` names `HD_API_KEY`. Values not inspected.
- **E-B20** `:762-765` refuses unless `SAFE_MODE=0` and `ALLOW_NETWORK=1` (`PROVIDER_REFUSED`); no-redirect opener.
- **E-B21/E-B22** `engine/db/adapter.py:16-18` retired bridge keys; `DBAccess.for_current_env` (105–118) refuses them before provider construction; `DATABASE_URL` only (`:119-142`); provider `PsycopgProvider`.
- **E-B23** `engine/bodygraph/mapped_cache.py:19` posture `adapter_mapped_no_raw_vendor_payload`; `persist_mapped_bodygraph` (`:60`, `PROVIDER_WRITE_UNSUPPORTED` `:89`); `read_current_mapped_bodygraph` (`:165`).
- **E-B24** Readiness tool: docstring (5–9) "issues no UPDATE, INSERT or DELETE…"; `"read_only": True` (`:82`); `DBAccess.for_current_env()` (`:217`); refusals `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`; selection ≤ 1 MiB; `require_closed_rails`.
- **N-B04** No `INSERT|UPDATE|DELETE|persist_mapped|commit\(` in the tool body below its docstring (case-sensitive → 0). DB-session read-only enforcement: Unknown.
- **N-D01** No top-level `vendor/` (`ls vendor` → no such file).

## 9. Evidence, Indices, Catalogs

Read-only validators under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`; exit codes captured with `out=$(cmd); rc=$?`; tree clean before and after.

| ID | Command | Result |
| --- | --- | --- |
| E-D01 | `python tools/evidence/update_evidence_index.py --check` | rc 0 (env pins line) |
| E-D02 | `python tools/evidence/orientation_demo.py --check` | rc 0 |
| E-D03 | `python tools/evidence/validate_evidence_paths.py` | rc 0 |
| E-D04 | `./ci/checks/check_mirror_schema.sh` | rc 0. Via `bash …` it fails rc 2 (the file is a Python script with a `.sh` name; CI runs it directly, `ci.yml:211`) |
| E-D05 | `python scripts/release_id_recompute.py --check-manifest-only` | rc 0 |
| E-D06 | `python tools/evidence/run_canonical_json_gate.py --check-only` | rc 0 |

- **E-D07/E-D08/E-D09** Human Index 606 rows, SHA-256 matches `INDEX.sha256`; Mirror 606 lines, matches its sentinel; orientation `total_artifacts: 606`, `status: ok`.
- **E-D10** Last commit touching `docs/evidence/INDEX.json`: `3828d4b` (PR01). **E-D11** EPIC040-tagged rows: `catalog.catalog_schema_validation`, `catalog.domain_closure_report`.
- **E-D14 / E-B27** `catalog/manifest.json`: version 1.3.0, `built_at_utc` 2026-08-24T18:04:49Z, 45 files, last changed `8999bd0`; manifest paths equal the roster literal exactly (python set comparison → `45 45 True set()`).
- **E-D15** Endpoint catalog symlink, 10 rows, last changed `d79cfc1`.
- **E-D13** `goldens/` 26 files; `artifacts/cards/a3/IDENTITY_OK.txt` family present; `artifacts/release_id.txt` and `artifacts/release_pack_manifest.json` are frozen EPIC022 records per AGENTS.md.
- **E-OPS** OPS01 evidence under `audit/ops/hde-epic040/ops01/` with `SHA256SUMS` (7 of 7 OK per receipt v1.2 §2); not promoted into the Index/Mirror (receipt §6).
- **E-DOC** DOC-20 §4 R6 records `--compare-goldens .` exit 0, 8 of 8 cases `match`, and an admission probe `AdmittedMechanicsBundle 1.3.0 45`, executed by the IA under closed rails at `47e2b976` (not re-executed here).
- **E-PF10** PF10 v13.3.8 line 1374 ends mid-word ("…persistence remains p"), confirmed from the Git blob `608003fe` at `39b9cdf` and present in every PF10 version in Git since v13.2.8 (`210250c`); previously recorded as O-P06-21; the §1.1 Addendum Index lists 2.1–2.26 and omits the body's §2.27.

## 10. Tests, QA Harness, CI/Checks

- **E-A15** `tests/`: 316 tracked files, 277 `test_*.py`.
- **E-A16** `pytest.ini` `testpaths` lists 12 entries; it omits e.g. `tests/order`, `tests/http`.
- **E-A17 / N-A02** `tests/conftest.py` only adjusts `sys.path` (no rails/network fixture; grep → 0); `tests/provider/conftest.py:270` reads `SAFE_MODE`.
- **E-A18–E-A20** `.github/workflows/ci.yml` (399 lines): `pull_request` and `push` to `main`, `paths-ignore` of 4 documentation prefixes; one `test` job: exact-head checkout (`:43`), lane classification, Python 3.12, changed tests in an isolated worktree under closed rails, lanes product/compat/db/rails/evidence/qa/release, final `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (`:399`). `epic-closeout-validation.yml` is `workflow_dispatch`, read-only.
- **E-A22–E-A24** Classifier `LANES` (7); `_DOCUMENTATION_PREFIXES` 8 entries (`docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/`); `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` 40 (all exist).
- **E-A26** Static count: of 277 `test_*.py`, 48 are named by `ci.yml` tokens, 40 by the roster; **189** by neither; 145 are outside the classifier owner registry (134 paths). They may still run as changed tests; "never run by CI" is Unknown.
- **E-A25** `tools/qa/qa_harness.py` governed statuses `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED`.
- **E-REC** Recorded known failures (not re-executed): `tests/reader_v1/test_cli_proof.py` baseline failure O-P06a-03 (PF10 §2.24, §2.26 "476 passed, 1 failed"); PR05 sweep of files outside the lanes: 57 failed, 546 passed, 13 errors (PR05 result v1.3).
- **E-SEC** Security-review coverage recorded by the units: PR04 and PR06 opened before code (no code review); PR05 and PR06a reviewed at PR open only; PR06b reviewed on `acae4c6` with no finding (PF10 §§2.19, 2.20, 2.22, 2.24, 2.26).

## 11. Flows & Call Chains

| Family | Status | Chain |
| --- | --- | --- |
| Reader HTTP v1/v2 | Found | `http_reader.py:556 reader_post` → `_production_reader_response` (`:509`) → `_select_reader_version(("1","2"))` → `_parse_reader_post_body` → `resolve_compat_chart(source_policy="local")` → `_evaluate_reader_pair` → `evaluate_pair` → `compute_core` (via `compat/compute.py:346`) → `engine.runtime.public.emit_reader_public_bytes` → `emit_reader_v1/v2` → response. Admission appears as the `RegistryConfigError` path |
| Compat HTTP | Found | `compat_handler.py:130` POST → stored party or `resolve_compat_chart` → `evaluate_pair` → `_writer_payload`; `RegistryConfigError` → 503 |
| CLI showcompat | Found | `cli` → `showcompat` (`:604`) → resolve party → `evaluate_pair` (`:745`) → `_emit_stdout_bytes`; `--conjunction` inner hops Unknown |
| Vendor ingestion `bg:resolve` | Found | `bg_resolve` (`:210`) → `resolver.resolve_bodygraph` (`:59`) → closed rails → `PROVIDER_REFUSED`, exit 1 → `emit_public` → `sys.stdout.write` |
| Evidence update | Found | `update_evidence_index.py:main` → `ensure_determinism_env()` → `_run_once(check=…)`; inner writers not traced |
| Golden comparison | Found | `generate_config_artifacts.py --compare-goldens` → `_compare_goldens_main` (`:345`) → `compare_goldens` (`:360`) |
| Gate readiness | Found | `check_magic10_gate_readiness.py:main` (`:211`) → `require_closed_rails` → `parse_selection` → `DBAccess.for_current_env` → `observe` → `sercanon` |
| PF23 families not in HDE-EPIC040 scope (sampler, aux preview, mapped-cache v2, CRD recording/publication, claims helper) | Present by name; not re-traced | Outside this change's scope; carried as PF23 comparison only |

## 12. Drift and Reality vs Expectations

Observations (RA-##), in source order, each with its comparison source:

| ID | Observation | Comparison source | Alignment | Evidence |
| --- | --- | --- | --- | --- |
| RA-01 | Catalog, config, schemas, loader, roster 1.3.0/45 and core exist and agree | Spec §5.2–5.5; Plan §§5–6 | Aligned | E-B02–E-B29, E-D05, E-D14 |
| RA-02 | Reader v1 harmony-only, Reader v2 ten ordered items, `POST /api/reader`, governed 405 | PF10 §§2.23, 2.25; Plan overlay | Aligned | E-B14, E-B15, E-C10–E-C13 |
| RA-03 | Evidence Index/Mirror/orientation/paths/canonical gate/manifest validators pass | Spec K040-REQ-012 | Aligned | E-D01–E-D06 |
| RA-04 | Wheel packaging omits release members (O-12) | PF10 §2.22 | Drift, carried | E-A08, E-B-wheel |
| RA-05 | HTML 404 for unknown non-compat paths on two of three factories (O-P06a-22) | PF10 §2.24; PF05 §5.2 per the PR06a disposition | Drift, carried | E-C02, E-C04, E-C06 |
| RA-06 | Dev `GET /reader` treats unset `APP_ENV` as dev and refuses `test`; conjunction routes allow dev/test/local and refuse unset (O-P07-04) | AGENTS.md dev-route gating | Partial | `:603`, E-C14 |
| RA-07 | showcompat help text says Reader v1 (O-P07-01); `--band` ignored with `--pair-file` (O-P07-02); dev harness calls `app.getattr` (O-P07-03) | DOC-20 §6 carried items | Drift, carried | E-C20; `main.py:549-567`; `dev/reader_harness/app.py:12` |
| RA-08 | 189 test files not named by a fixed lane or the roster; recorded pre-existing failures | Spec K040-REQ-011 coverage; PF10 §2.19 | Informational; not established as never run | E-A26, E-REC |
| RA-09 | Security review did not cover implementation deltas in four units | PF10 §§2.19–2.24 | Evidence limit | E-SEC |
| RA-10 | Live Gate readiness against production rows never observed; open-rails QA step owed | PF10 §2.20; Plan Review §5.4 (PF05 §7.3.9) | Reserved for QA | E-B24 |
| RA-11 | `bg:resolve` output bypasses the LF/CRLF guard | AGENTS.md showcompat stdout discipline (showcompat only) | Not established as a requirement | Flow table |
| RA-12 | `ci.yml` `paths-ignore` (4) differs from `_DOCUMENTATION_PREFIXES` (8) | AGENTS.md code-review-scope note | Drift (informational) | E-A19, E-A23 |
| RA-13 | `check_mirror_schema.sh` is Python; AGENTS.md documents `bash`-style invocation | AGENTS.md evidence rules | Drift (docs) | E-D04 |
| RA-14 | Registered routes absent from the endpoint catalog (aux, ops, healthz/readyz) | PF23 FND-025 | Persistent | E-C17, N-D06 |
| RA-15 | Serializer relies on upstream validation for NaN; rebindable module globals; admission per call | Plan §4.4 determinism (no explicit NaN rule found) | Informational hazard | N-B03, E-B11, N-B02 |
| RA-16 | Root hygiene: zero-byte files, scratch files, placeholder `channels_catalog_v1.json`, duplicate `hdctl` scripts, `pytest.ini` scope differs from CI | PF23 FND-012; AGENTS.md "no QA artifacts in repo root" | Persistent / informational | E-A02b, E-A04, E-A14, E-A16, E-B-cat |
| RA-17 | PF10 v13.3.8 stored text truncated at line 1374; §2.27 missing from the Addendum Index | PF10 §0/§1.1 | Defect (canon storage) | E-PF10 |
| RA-18 | Canon drainage of C040-05, -06, -07, -08 pending | PF10 §§2.3, 2.5, 2.23, 2.25 | Pending, non-gating | PF10 register |

**Historical comparison** (PF23 v1.2 §12, 2026-09-06 at `71307d9`):

| PF23 finding | Status at `39b9cdf` | Evidence |
| --- | --- | --- |
| FND-001–004, 006–013 | Persistent | E-D17–E-D22, E-D07–E-D12, N-D01, N-D04, Procfile, E-A04 |
| FND-005 | Persistent (bounded; not re-read in full) | E-B08, N-B01 |
| FND-009 counts | Changed (docs 155→1508, audit 3049→3080, tests 302→316, engine 98→101) | E-D21 |
| FND-014–016 | Persistent (presence only) | `tools/qa/step_log_header.py`; `qa_harness.py:2172`; docs present |
| FND-017 | Persistent: `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` | E-D23 |
| FND-018 | Unverifiable (hosted CI) | — |
| FND-019 | Resolved in PF19 v3.0.5 | E-D24 |
| FND-020 | Persistent (no provenance procedure) | N-D02 |
| FND-021 | Changed: public paths still call no `compute_core` directly (N-D05) but reach it through `compat/compute.py:346` | E-D25 |
| FND-022 | Persistent | E-D26 |
| FND-023 | Resolved (`audit/qa/hde-crd-0001` has 23 files; presence only) | E-D27 |
| FND-024 | Resolved at source level (showcompat stdout `magic10_compat_result.v1`) | E-D28 |
| FND-025 | Persistent (catalog now 10 rows, still no aux/admin-bundle) | N-D06 |

## 13. Negative-Claim Proof Appendix

| ID | Pattern / target | Method | Case | Scope | Result |
| --- | --- | --- | --- | --- | --- |
| N-00 | `EPIC040.*(reality\|triage\|readiness\|QA-10\|qa10)` | `ls docs/ephemeral \| grep -iE` | insensitive | `docs/ephemeral` file names | 0 |
| N-A01 | `Dockerfile*`, `setup.py`, `setup.cfg` | `ls` | sensitive | repo root | none |
| N-A02 | `ALLOW_NETWORK\|SAFE_MODE\|socket\|def pytest_\|ensure_determinism` | `grep -nE` | sensitive | `tests/conftest.py` | 0 |
| N-B01 | `import engine.db\|from engine.db\|vendor_client\|urllib\|psycopg` | `grep -rn` | sensitive | `engine/core`, `engine/magic10` | 0 |
| N-B02 | `lru_cache\|functools.cache` | `grep -rn` | sensitive | `engine/config engine/core engine/magic10 presenter engine/presenter engine/runtime/public.py` | 0 |
| N-B03 | `allow_nan` | `grep -rn` | sensitive | `engine/stable`, `engine/serializer` | 0 |
| N-B04 | `INSERT\|UPDATE\|DELETE\|persist_mapped\|commit\(` | `sed -n '23,$p' \| grep -cE` | sensitive | readiness tool body | 0 |
| N-C01 | extra entries under `[project.scripts]` | read | — | `pyproject.toml` | only `hdctl` |
| N-D01 | `vendor/` | `ls` | sensitive | repo root | no such file |
| N-D02 | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` | `ls` | sensitive | exact path | no such file |
| N-D03 | `aux\|admin` | `grep -ci` | insensitive | `artifacts/audit/ENDPOINTS_CATALOG.json` | 0 lines |
| N-D04 | `server`, `adapters` | `ls` | sensitive | repo root | no such file |
| N-D05 | `\bcompute_core\b` | `grep -cw` | sensitive | `engine/runtime/public.py`, `engine/http/compat_handler.py`, `engine/cli/main.py` | 0 each |
| N-D06 | path ∈ {`/aux/narrative`, `/internal/admin/bundle/v1`} | python JSON equality | sensitive | all 10 catalog rows | 0 |
| N-PF10 | `7\.3\.9`, `open.rails QA`, `production rows` | `grep -n -i` | insensitive | PF10 v13.3.8 | 0 |

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-10-20260927-01
  change: EPIC / HDE-EPIC040 (Specification v1.1)
  unit: whole change
  prompt: QA-10 — Audit Implementation and Establish QA Readiness — 091426.1; Notion 3db4590a05eb818bad2fcb4bc2610b29; page as of 2026-09-24T15:51:30Z; release GCFPE-20260914.1
  role_stage: continuing Isis, QA-10
  capture_time: 2026-09-27T08:40:00Z
  execution_identity: https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
  repository_persistence: PENDING / NON_GATING (no installed docs/changes/GCFPE_PROMPT_PROVENANCE.md; N-D02)
```

`CANON_CONFLICT_REGISTER` C040-01 to C040-08 is carried unchanged; its status is stated in the readiness record §5.
