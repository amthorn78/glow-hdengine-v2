---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-03-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
work_unit_title: "Public, dev and CLI surfaces (PR; Conjunction; S02, S07, S09, S10, S15, S18)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.2, its "Downstream work" item for WU-PR-03 (keep the contract-inventory generator's public-route baseline current; ID-4) with the binding requirements it sets for that generator; addendum 2.3 (reviewer chain without the Codex security review). Addendum 2.1 governs §19 only. Addenda 2.4 and 2.5 record the WU-PR-01 and WU-PR-02 acceptances; their carried items are in §15
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — lineage; §5 re-verifies its facts at the current baseline and corrects three of them
predecessor_unit_acceptance: WU-PR-01 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT; PF10 addendum 2.4); WU-PR-02 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v2.0.md (ACCEPT; landed at 142e56f, #638; PF10 addendum 2.5), with its predecessor docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v1.0.md (observations LR-O1 to LR-O3)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md (v13.5.6, effective 2026.10.14; blob 9c5468fb69e4; 69,689 bytes; sha256 8663ab94289adae036dbb07af8b302d1b7f3b1d2a1b57dfb7bbd664a5b98bec0). Read: v13.5.5 in full earlier in this IA lineage, plus the complete v13.5.5→v13.5.6 diff, which changes only the version and date lines, adds one index line and appends addendum 2.5 (read in full); addendum 2.2 re-read in full for this unit
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md §2.2 ("Downstream work"; "Binding requirements"), §2.3, §2.5; §2.1 for §19
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state as of 2026-10-12T02:29:33Z; read in full, unchanged since the WU-PR-02 instruction)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-14T00:31:02Z
repository_baseline: origin/main ad118212bbae0df2eb1aec336788bd2532b56569 (Product Owner direct-main commit "PF10 Update", adding PF10 v13.5.6 over #638 at 142e56f); every repository fact in §5 measured there
receiver: dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); no new entry (§16)
---

# HDE-CRD-0002 WU-PR-03 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-03 of HDE-CRD-0002, issued by the whole-change IA from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- author the detailed per-file plan (PR-20's output);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-03 (Plan v1.1 §7 heading "WU-PR-03 — Public, dev and CLI surfaces (PR; Conjunction)") |
| Requirements | S02, S07, S09, S10, S15, S18; engineering choices EC-2, EC-4, EC-6, EC-8; interfaces IF-6, IF-10, IF-11; the same-version manifest refresh and convergence its member changes force |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above); review v1.1 redlines R1.1 (IF-10 explicit-`dev`), R1.2 (IF-6 `/reader` `env_gate` stays `APP_ENV=dev`) and R1.3 (acceptance (2)) are in Plan v1.1 |
| Overlays | PF10 addendum 2.2 "Downstream work" (ID-4); addendum 2.3 (reviewer chain) |
| Upstream units | WU-PR-01 and WU-PR-02, both accepted |
| Phase | Conjunction |
| Live QA class (Specification table; Plan §6) | S02, S07, S10: functional-feature; S15: catalog entries only (no route removed); S09, S18: not production-affecting |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1, INITIAL_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.** Plan v1.1 §7: "Third; after WU-PR-01 (registered owners for `tests/adapter/test_gate_auth.py` and the http_reader owner guard) and WU-PR-02 (label model before rows are regenerated)." WU-PR-01 is accepted (addendum 2.4) and WU-PR-02 is accepted (lineage review v2.0; addendum 2.5). AQ-1 gates only WU-PR-07's merge. No QA Guide, QA Plan or Ops receipt is a prerequisite.
- **Order.** WU-PR-01 → WU-PR-02 → **WU-PR-03** → WU-PR-04 → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7).
- **Downstream dependents** (contracts in §8):
  - WU-PR-04 and WU-PR-05 take the release identity this unit's refresh sets as their own refresh base.
  - WU-PR-05 (S19 security review) reads the surfaces this unit lands.
  - WU-PR-06 reads the classifier registrations this unit adds.
  - WU-PR-08 and WU-DOC-01 own the documents this unit leaves stale (§15).
  - QA-10 needs S02 and S10 for the production-app Live QA steps (Plan v1.1 §7 WU-OPS-01).

## 4. Required behavior

**Acceptance intents**, verbatim from the approved Specification (Requirements table):

| ID | Requirement | Acceptance intent |
| :- | :- | :- |
| S02 | Unknown non-compat paths on the production app return the governed not-found envelope | "Every 404 from the production app is the governed `ERR_NOT_FOUND` envelope with `no-store`, never Flask HTML" |
| S07 | Correct the showcompat help summary | "`hdctl --help` describes showcompat's actual `magic10_compat_result.v1` output" |
| S09 | Repair or retire the dev Reader harness and the references to it | "The harness imports and runs, or it is retired and `VERIFY.sh` and `docs/acceptance/reader_a7_crib.md` no longer reference it" |
| S10 | Gate dev `GET /reader` on an explicit environment | "The dev route is served only when `APP_ENV` is explicitly `dev`, `test` or `local`; unset or any other value refuses" |
| S15 | Reconcile the endpoint catalog with the routes the service registers | "Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner" |
| S18 | Correct `docs/ADAPTER_009.md`'s GET-with-body code and `ARCHITECTURE.md`'s stale statements | "The documents say `invalid_json` for a compat GET with a body … and state the current emitter return type and route mounts" |

**S10 reading (approved; binding).** Plan v1.1 §15 records it and IA-30 applied it as redline R1.1: "S10 is implemented as an explicit-`dev` gate: the Specification's acceptance intent states a necessary condition that this gate satisfies, and HDE-CLI-API-Vendor-Ref §5.6 and HDE Schemas & Artifacts 'Reader surface routes and distinct contracts (normative)' require explicit `APP_ENV=dev` for this route (HDE Governance §9.1.2); serving `test` or `local` would need a canon change this CRD excludes, so no canon conflict is opened."
- The same requirement is in HDE-CLI-API-Vendor-Ref §5.4 "Gate" and in HDE Math Spec's dev-harness bullet ("A default that treats an unset environment as development is not fail-closed").
- The Audit's S10 "Required behavior" (`_dev_admin_gate` semantics: `dev`, `test`, `local`) is superseded by the approved Plan and must not be implemented.

**Interfaces**, verbatim from Plan v1.1 §5:
- **IF-6 (S15).** "Per-method records in the existing field set (`a7_eligible`, `blueprint_module`, `classification`, `description`, `env_gate`, `internal`, `method`, `path`, `rails_profile`, optional `route_id`), extended by the HDE-CLI-API-Vendor-Ref §5.6 projection for `/aux/narrative` (`classification: public_aux`, `internal: false`, `env_gate: not_applicable_public`, `aliases: ["/api/aux/narrative"]`); internal rows for `/ops/db/unavailable`, `/ops/rails/refusal`, `/ops/probe/env`, `/ops/writer/diagnostic` (`adapter.http_reader`) and `/internal/healthz`, `/internal/readyz` (`adapter.wsgi`); `/reader` rows' `env_gate` stays `APP_ENV=dev`; `success_endpoints` stays `[GET /reader]`."
- **IF-10 (S10).** "`GET /reader` (and its defined HEAD behavior) served only when `APP_ENV` is explicitly `dev`; unset, empty and every other value, including `test` and `local`, refuse with `ERR_READER_FORBIDDEN` 403 (HDE-CLI-API-Vendor-Ref §5.6; HDE Schemas & Artifacts 'Reader surface routes and distinct contracts (normative)'); `scripts/dev_start_reader.sh` defaults `APP_ENV=dev`."
- **IF-11 (S02).** "App-level 404 and 405 handlers on `adapter.factory` (and the `adapter/http_reader.py` factory) emitting `error_envelope("ERR_NOT_FOUND")` through `emit_public`, `Cache-Control: no-store`, no ETag, `application/json; charset=utf-8`, as `adapter/wsgi.py` does; existing compat shaping and the production Reader's governed 405 unchanged."

**Engineering choices**, verbatim from Audit §7.1 as carried by the Plan:
- **EC-2 (S09):** "Retire the dev harness; repoint `VERIFY.sh` and the crib to the canonical dev runner."
- **EC-4 (S10):** "`scripts/dev_start_reader.sh` defaults `APP_ENV=dev` when unset; `docs/server/reader_v1.md` states it."
- **EC-6 (S07):** "The frozen `artifacts/cli/help/*` family stays frozen with a nonclaim that it captures the earlier help text; `docs/CLI_commands.md` loses its known-gap sentence."
- **EC-8 (S15):** "Catalog every registered route; remove none. `/aux/narrative` follows the HDE-CLI-API-Vendor-Ref §5.6 projected record (`public_aux`, alias `/api/aux/narrative`); the ops probes and the two `adapter.wsgi` health routes get internal rows with their observed gates."

**Binding IA decisions** (canon-conforming readings; HDE Governance §9.1.2):

**ID-1. Catalog population: what "every (method, path) rule" means for acceptance (5).**
- **The problem.** Measured literally, the three factories register 28 uncatalogued `(method, path)` pairs, excluding OPTIONS (§5.2). The Audit counted eight route strings. The literal pairs include:
  - Flask's automatic HEAD and OPTIONS;
  - the governed-refusal methods of `/api/reader` and the unprefixed `POST /reader`;
  - the `/api/aux/narrative` alias.
- **Canon on these pairs.**
  - HDE Schemas & Artifacts §8.8 makes the Catalog "a machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints)" and says "The production route's other methods are refused by the adopted transport contract" (they are part of that record, not separate records).
  - HDE-CLI-API-Vendor-Ref §5.6 says "`aliases` contains reachable spellings of the same contract, not independent surfaces", and its table gives the methods each route defines.
  - HDE-CLI-API-Vendor-Ref §5.6 also says the population policy is single-homed in HDE Schemas & Artifacts.
- **Binding reading.** Every `(method, path)` that a factory serves as endpoint behavior has exactly one catalog row. Three kinds of pair are excluded, each named in an explicit, reasoned exclusion table that the enumeration test applies:
  - **(a) Governed refusal of a catalogued record:** every non-`POST` method on `/api/reader`, and the unprefixed `POST /reader` (HDE-CLI-API-Vendor-Ref §5.4 "Production mount").
  - **(b) Alias spelling of a canonical record:** `/api/aux/narrative`, represented by the Aux record's `aliases`.
  - **(c) Framework-implicit method:** a method Flask adds automatically (HEAD for a GET view; OPTIONS with `provide_automatic_options`) whose behavior neither HDE-CLI-API-Vendor-Ref §5.6 nor the route's own view defines. The catalogued `HEAD /reader` and `HEAD /internal/version` stay, because §5.6 defines them.
- **What the test must do.** A served pair that is neither catalogued nor excluded fails the test. An exclusion whose pair no longer exists also fails it.
- **Consequences.**
  - `GET`, `HEAD` and `OPTIONS /api/compat/v1` need rows: HDE-CLI-API-Vendor-Ref §5.6 lists those methods, the views exist, and only `POST` is catalogued today.
  - The HDE-CLI-API-Vendor-Ref §5.6 row `/internal/admin/bundle/v1` gets no row: no factory mounts it, and HDE Schemas & Artifacts §8.8 says to select only entries that "correspond to real mounted routes".
- **Classes.** The closed class set comes from HDE Schemas & Artifacts §8.8 (`public_reader`, `public_compat`, `internal_identity`, `internal_admin`, `ops`, `dev_harness`). The generator's `CLASS` lacks `ops`, which canon registers. `public_aux` and the `aliases` key follow the HDE-CLI-API-Vendor-Ref §5.6 projection, which HDE Schemas & Artifacts has not registered (Plan risk R-7): use them, claim no catalog conformance, and record the registration as a doc-delta candidate.
- **No conflict.** This opens no canon conflict, because it reads the Plan's own wording ("rule", "row", IF-6's "per-method records") within canon. If PR-20 finds a served pair that fits none of (a) to (c) and has no defensible row, that is a boundary finding for RS-10/RS-20 (§14), never an uncatalogued route.

**ID-2. The dev Reader harness after retirement (S09; EC-2).**
- **Canon.** HDE Architecture §3.8.1 requires that "the dev Reader harness used in dev/QA consoles" expose "the canonically required dev/internal HTTP surfaces for QA, using the same Presenter emitter … including mounting the compat HTTP surface (`/api/compat/v1`)".
- **The runner meets it.** The canonical dev runner (`python -m adapter.http_reader`, started by `scripts/dev_start_reader.sh`) mounts the root dev blueprint, the production blueprint under `/api` and the compat blueprint, and emits through the shared presenter (§5.1). After S10 it also meets the strict `APP_ENV=dev` gate.
- **Effect of retirement.** Retiring `dev/reader_harness/` leaves two descriptive canon passages stale:
  - HDE Architecture §3.8.1 "Current repository discrepancy";
  - HDE Math Spec's "Dev Reader harness: `dev/reader_harness/app.py`" bullet.

  Both are doc-delta candidates for the Product Owner. No canon edit, no conflict.

**ID-3. Classifier registration (S09, S10; Audit S09 "Unknown pending discovery"; Plan §7.5).**
- **The refusals.** At the baseline the classifier refuses three paths this unit must change (§5.8):
  - `VERIFY.sh`: `CI_CHANGE_SURFACE_UNCLASSIFIED`;
  - `dev/reader_harness/app.py` and `__init__.py`, including their deletion: no lane, `CI_SOURCE_OWNER_TEST_MISSING`;
  - `scripts/dev_start_reader.sh`: `CI_PRODUCT_OWNER_TEST_MISSING`.
- **The permitted change.** `ci/checks/classify_ci_changes.py` may change by exactly the smallest registration that classifies those paths with a real owner test.
- **The finding.** PR-20 states it as a finding with its reason (instruction §6 rule).
- **Consequences.**
  - The classifier is a full-validation path, so this unit's PR runs all seven lanes (consistent with acceptance (7)).
  - Every registry pin in `tests/evidence/test_rails_ci_workflow_integration.py` stays true. A pin the registration requires is added there, inside the same bound.
  - No other classifier behavior changes.

**ID-4. Contract-inventory baseline (PF10 addendum 2.2 "Downstream work").**
- **Why it changes.** `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` in `tools/evidence/generate_hdapi_v2_contract_inventory.py` records the factories' routes and their app-level `errorhandler`, `before_request` and `after_request` registrations (21 records; §5.9). S02's handlers change that set.
- **The permitted change.** Exactly the change addendum 2.2 allows: only that data changes, "rebuilt from the public route records the three app factories register at the PR head and reviewed against HDE CLI/API/Vendor Reference §5.1.0 and §5.4 before commit".
- **What must not change.** The generator's outputs, schema, evidence family, refusal codes, flags and write paths. It is not run in write mode against the repository. Neither tool gains a new import symbol. `artifacts/vendor/hdapi_v2/` stays byte-unchanged.
- **Verification.** `tests/evidence/test_hdapi_v2_contract_inventory.py` passes with `ruby` on `PATH`. The boundary analyzer accepts the new handlers, which must emit through the presenter.

## 5. Current repository and reference baseline (verified at `ad11821`)

The Audit measured these facts at `982071b`. Three of them are corrected here:
- (a) `adapter/http_reader.py::create_app` now has compat-scoped app-level 404/405 `errorhandler`s that return Flask's response on other paths, not an `after_request` rewrite.
- (b) The catalog gap is 13 rows under ID-1, not eight route strings.
- (c) `/aux/narrative` emits through `emit_public_aux`; it no longer answers 503 unconditionally.

### 5.1 HTTP homes

- **`adapter/factory.py` (28 lines; the Procfile app; non-member).**
  - Mounts `bp` at `/`, `api_bp` at `/api` and `compat_blueprint` (lines 9–13).
  - Its only shaping is `after_request` `_strip_etag_on_internal` (lines 14–27): it rewrites HTML 404/405 on compat paths through `compat_error_response`, with `Allow` kept on 405, and strips `ETag` under `/internal/`.
  - Other unknown paths get Flask's HTML 404.
- **`adapter/wsgi.py` (73 lines; non-member).**
  - `_apply_common_headers` sets `Cache-Control: no-store` and `Content-Type: application/json; charset=utf-8`.
  - `/internal/healthz` (line 41) and `/internal/readyz` (line 47) return 200.
  - `errorhandler(404)` (line 53) and `errorhandler(405)` (line 60) return `error_envelope("ERR_NOT_FOUND")` through `emit_public` with those headers. The 405 does not set `Allow`.
- **`adapter/http_reader.py` (1,218 lines; release member).**
  - `get_reader_api_bp` (line 544): `POST /reader` (556); the governed 405 for other methods (560).
  - `get_reader_bp` (585):
    - `GET /reader` (597), gate at line 603: `if os.environ.get("APP_ENV", "dev") != "dev": return _error("ERR_READER_FORBIDDEN", 403)`, so unset means served;
    - `/api/aux/narrative` and `/aux/narrative` (671–672, `emit_public_aux`);
    - the unprefixed `POST /reader` governed 405 (720);
    - `/ops/db/unavailable` (747), `/ops/rails/refusal` (789), `/ops/probe/env` (797);
    - `_dev_admin_gate` (817–823: `dev`, `test`, `local`; `ERR_WRITER_FORBIDDEN`);
    - the dev conjunction routes (1047, 1055, 1063);
    - `/internal/version` (1090);
    - `/ops/writer/diagnostic` POST, HEAD, OPTIONS (1114, 1135, 1147).
  - `create_app` (1163):
    - mounts `bp`, `api_bp` and `compat_blueprint`;
    - compat-scoped `errorhandler(404)`/`(405)` (1187, 1193) return `err` (Flask HTML) outside `/api/compat/v1`;
    - `after_request` (1199) strips `/internal/` ETags.
  - The `__main__` runner (1215–1218) binds `0.0.0.0` on `PORT` (default 8000).
- **`engine/http/compat_handler.py` (member; not changed by this unit).** `GET ""` (line 122) returns 200 `{"ok": true, "schema": "v1"}`, or 400 `invalid_json` for a GET with a body (124–126). `POST` (130). Explicit `HEAD` (176) and `OPTIONS` (181). A production environment answers the compat 404 before any view (108–113).

### 5.2 Endpoint catalog (S15) and the measured served set

- **Catalog.** `docs/ENDPOINTS_CATALOG.json` has 10 rows:
  - `POST /api/compat/v1` (`internal_admin`, `APP_ENV!=prod`);
  - `POST /api/reader` (`public_reader`);
  - `GET` of the three dev conjunction routes and `POST /internal/dev/sampler` (`dev_harness`, `APP_ENV in {dev,test,local}`);
  - `GET`/`HEAD /internal/version` (`internal_identity`);
  - `GET`/`HEAD /reader` (`dev_harness`, `APP_ENV=dev`, `a7_eligible: true`).

  `success_endpoints` is `[GET /reader]`. The audit mirror `artifacts/audit/ENDPOINTS_CATALOG.json` is byte-identical.
- **Owner.** `tools/evidence/generate_a7_transport_proofs.py` (160 lines; non-member):
  - `CLASS` (line 33) is `{internal_admin, dev_harness, internal_identity, public_reader}`;
  - `catalog_obj` (36–48);
  - `validate_catalog` (49 onward) closes the key set at the ten IF-6 fields plus `route_id` (line 57), and pins the sampler row (68) and the success designation;
  - `build()` (139) writes the catalog, its mirror, both `.sha256` sidecars, `artifacts/reader/endpoints_snapshot.json` and the seven A7 proofs (lines 30–31);
  - `main` refuses unless `HDE_WRITE_A7_PROOFS=1` (157);
  - `capture` sets `APP_ENV=dev` for the success proofs and probes `APP_ENV=prod` for the env-gate proof (lines 90–113).
- **Updater.** The canonical updater registers the catalog family under `epic038.pr02.endpoint_catalog*` (lines 3019–3022, 3429–3432).
- **Served set by factory, measured at `ad11821`** (`create_app().url_map`; the same blueprint set in all three factories, plus the two health routes in `adapter.wsgi`):

| Path | Methods served by a view (explicit route or catalogued) | Framework-implicit | Catalogued today | ID-1 outcome |
| :- | :- | :- | :- | :- |
| `/reader` | GET (HEAD defined by HDE-CLI-API-Vendor-Ref §5.6); POST = governed 405 | OPTIONS | GET, HEAD | POST excluded (a); OPTIONS excluded (c) |
| `/api/reader` | POST; DELETE, GET, HEAD, OPTIONS, PATCH, PUT = governed 405 | — | POST | non-POST excluded (a) |
| `/api/compat/v1` | GET, POST, HEAD, OPTIONS (explicit views) | — | POST | **add GET, HEAD, OPTIONS** |
| `/aux/narrative`, `/api/aux/narrative` | GET | HEAD, OPTIONS | — | **add one `GET /aux/narrative` record with `aliases`**; alias excluded (b); HEAD/OPTIONS excluded (c) |
| `/ops/db/unavailable` | GET | HEAD, OPTIONS | — | **add GET** |
| `/ops/rails/refusal` | GET, POST | HEAD, OPTIONS | — | **add GET, POST** |
| `/ops/probe/env` | GET | HEAD, OPTIONS | — | **add GET** |
| `/ops/writer/diagnostic` | POST, HEAD, OPTIONS (explicit views) | — | — | **add POST, HEAD, OPTIONS** |
| `/internal/healthz`, `/internal/readyz` (`adapter.wsgi` only) | GET | HEAD, OPTIONS | — | **add GET each** |
| `/dev/*/conjunction` (3) | GET | HEAD, OPTIONS | GET | implicit excluded (c) |
| `/internal/dev/sampler` | POST | — | POST | — |
| `/internal/version` | GET, HEAD | OPTIONS | GET, HEAD | OPTIONS excluded (c) |

The result is 13 rows to add (10 → 23). PR-20 confirms each row's methods, `env_gate` and `rails_profile` by reading the view and its guard, and records any difference from this table with its reason.

### 5.3 CLI help (S07)

- `engine/cli/main.py` (release member), lines 78–79: `"showcompat", help="Emit canonical Reader v1 bytes from vendor JSON (stdin or files)"`.
- `docs/CLI_commands.md` line 25 states the current stdout contract and carries the sentence "Known gap: the one-line `hdctl --help` summary for `showcompat` still reads …".
- The frozen CLI-conformance family (`artifacts/cli/help/*`, `tools/cli/generate_cli_conformance_artifacts.py` `FROZEN_SHA256`; `--check` validates digests, not live output) stays frozen under EC-6. Its consumers are `tests/evidence/test_cli_conformance_artifacts.py`, `tests/ops/test_evidence_index.py`, the updater, the identity closure and the canonical JSON gate.
- The same stale text appears in historical QA, Ops and proof captures (for example `artifacts/proofs/cli_help.txt`, `cli_install.txt`; `audit/qa/hde-epic026/…`). No producer or Index record binds those two `artifacts/proofs` files. All of them stay untouched.
- `ci/checks/check_cli_help.sh` exists and checks exit status, empty stderr and the final LF only (Audit S07).

### 5.4 Dev harness and its references (S09)

- **The harness.** `dev/reader_harness/__init__.py` and `app.py` (20 lines; non-members).
  - `app.py` line 12, `app.getattr(app, "register_"+"blueprint")(bp, url_prefix="/api")`, raises at import (line 17, `app = create_app()`).
  - Its gate (line 8) treats an unset `APP_ENV` as `dev`.
- **Active references.**
  - `VERIFY.sh` (non-member):
    - line 4 `export APP_ENV=${APP_ENV:-dev}`;
    - lines 39–45 free port 5000 and start `from dev.reader_harness.app import app` on `127.0.0.1:5000`;
    - line 53 probes `GET http://127.0.0.1:5000/api/reader?v=1&a=…&b=…`.

    The harness mounted the dev blueprint under `/api`, while the canonical runner serves the dev GET at `/reader`, and `GET /api/reader` there is the production route's governed 405. Repointing therefore changes the probed path to `/reader` and the port to the runner's.
  - `docs/acceptance/reader_a7_crib.md` line 4;
  - `docs/server/reader_v1.md` lines 19 and 24 (the legacy notice);
  - `engine/emit_public.py` line 21 (docstring; non-member; the five-positional `emit_public_envelope` helper stays because `VERIFY.sh` uses it at lines 12–29);
  - `tests/runtime/test_emit_public_legacy_helper.py` line 5 (docstring);
  - `CHANGELOG.md` line 333 (history; WU-DOC-01).
- **Historical references** stay untouched: `.audit_src/`, `_arch/`, `.backup_epic004/`, `handoff/`, `audit/docs_snapshot*`, `codex/out/`, `notes/`, `artifacts/epic004/…`, `artifacts/math/_manifest_files.txt`, `audit/inventory_epic007.json`, `manifest_*.sha256`.
- **Canon references** (read-only; ID-2): HDE Math Spec §12 "Implementation Notes (non-normative; repo pointers)", "Dev Reader harness" bullet (line 2257); HDE Architecture §3.8.1 (line 1094).

### 5.5 Dev runner (S10; EC-4)

`scripts/dev_start_reader.sh` (26 lines; non-member):
- sets `SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, `TZ` and `PORT` (default 8000) if unset;
- exports `APP_ENV` only when it is already set (lines 13–18);
- runs `exec python -m adapter.http_reader` (line 26).

After S10, an unset `APP_ENV` would start a runner whose `/reader` refuses, so EC-4's default is required.

### 5.6 Documents (S18)

- `docs/ADAPTER_009.md` line 174: "`COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 typed `{"error":"body_not_allowed"}`". The code emits `error_envelope("invalid_json")` with 400 (compat_handler lines 124–126).
- `ARCHITECTURE.md`:
  - lines 9 and 24 state `emit_compact_json(payload) -> bytes`, but `engine/presenter/emitter.py` line 23 is `emit_compact_json(envelope, *, sort_keys=True) -> Tuple[bytes, Dict[str, Any]]` ("Compatibility alias … Prefer `emit_public_with_envelope`");
  - line 28 is the heading "Routing (dev only)", while production mounts live in `adapter/factory.py` (Procfile; `api_bp` under `/api`).
- `docs/ADAPTER_009.md`'s S17 lines belong to WU-PR-08 (Plan §7).

### 5.7 Release identity and the refresh

- **Manifest.** `catalog/manifest.json`: version `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`, 45 members, `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.
- **Admission constants.** `engine/config/registry_loader.py` lines 398–399: `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"`. They are unchanged by a same-version refresh.
- **Members this unit changes:** `adapter/http_reader.py` (S10; S02's third factory) and `engine/cli/main.py` (S07).
- **Non-members:** `adapter/factory.py`, `adapter/wsgi.py`, `engine/emit_public.py`, `tools/**`, `scripts/**`, `VERIFY.sh`, `dev/**`, `ci/**`, `tests/**`, `docs/**`, `ARCHITECTURE.md`.
- **Required refresh.** Admission refuses a member whose bytes differ from the manifest (Audit §5.1), so the unit refreshes `catalog/manifest.json` at `1.3.0` / `2026-08-24T18:04:49Z` through the cutter and converges evidence in Plan v1.1 §10 order. The new `release_id` is the base for WU-PR-04.
- **Rules landed by WU-PR-02 that govern this run** (lineage review v1.0 §7 LR-O3; addendum 2.5):
  - **(a) Updater before the cut.** `tools/evidence/update_evidence_index.py` refuses `CURRENT_RELEASE_LABEL_MANIFEST_INVALID`, in write and `--check` modes, whenever a member's bytes differ from the manifest. The updater and the evidence lane's `--check` therefore fail between §10 step 1 (member bytes final) and step 2 (cut). Do not run them there.
  - **(b) Label timing.** A roster capture takes the new release's label at the first updater run after its owner regenerates it:
    - the canonical JSON gate's captures, after step 4 (relabelled at step 5);
    - the config family, during step 6;
    - the step-7 producers (A7: `artifacts/proofs/reader_success_get_head_304.json`, `success_304.txt`, `success_encoding_invariance.txt`, `success_get.txt`, `success_head.txt`; determinism; open-rails fixture proof; F07 writer; engine-core), at step 8.
  - **(c) Stale labels.** A roster capture left byte-stable across the `release_id` change keeps its earlier label. That is a finding to the IA (WU-PR-02 instruction §8 D-1), not a roster edit.
  - **(d) The label is not proof that an owner ran** (LR-O1). The owners' `--check` modes and the step-11 stale-binding sweep remain the protection.
- **Non-roster files the step-7 run rewrites.** The A7 run also rewrites `artifacts/proofs/endpoints_env_gate_proof.log`, `success_writers_errors.txt`, `artifacts/reader/endpoints_snapshot.json` and the catalog family. None of them is on the label roster.

### 5.8 CI classification at the baseline

`ci/checks/classify_ci_changes.py`: `_lanes_for_path` and `changed_test_targets`, read at `ad11821`.

| Path | Lanes | Owner targets |
| :- | :- | :- |
| `adapter/factory.py` | compat, product, release | 4: `tests/evidence/test_hdapi_v2_contract_inventory.py`, `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py` |
| `adapter/http_reader.py` | compat, db, product, release | 17 (the `_HTTP_READER_TEST_OWNERS` guard; it includes `tests/adapter/test_gate_auth.py`, `tests/http/test_reader_a7_transport.py`, `tests/http/test_endpoint_catalog.py`, the contract-inventory test) |
| `adapter/wsgi.py` | compat, product, release | 6 |
| `engine/cli/main.py` | compat, product, release | 4 |
| `tools/evidence/generate_a7_transport_proofs.py` | evidence, release | `tests/transport/test_a7_transport_proofs.py` |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | evidence | `tests/evidence/test_hdapi_v2_contract_inventory.py` |
| `engine/emit_public.py` | product, release | `tests/runtime/test_emit_public_legacy_helper.py` |
| `catalog/manifest.json`; the catalog family; A7 proofs | release / evidence, release | — |
| `scripts/dev_start_reader.sh` | product, release | **refused: `CI_PRODUCT_OWNER_TEST_MISSING`** |
| `VERIFY.sh` | none | **refused: `CI_CHANGE_SURFACE_UNCLASSIFIED`** |
| `dev/reader_harness/app.py`, `__init__.py` (edits and deletions; `git diff --diff-filter` includes D) | none | **refused: `CI_SOURCE_OWNER_TEST_MISSING`** |
| documents (`docs/**/*.md`, `ARCHITECTURE.md`) | none | — |

`tests/evidence/test_hdapi_v2_contract_inventory.py` needs `ruby` on `PATH` (addendum 2.2; present on the hosted `ubuntu-24.04` runner per addendum 2.5 O-6, version unprinted).

### 5.9 Contract-inventory baseline (ID-4)

`ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` (line 135; aliased at line 2173) holds 21 records:
- 4 `app.errorhandler`: `adapter/http_reader.py` `_compat_scoped_not_found`/`_compat_scoped_method_not_allowed`, and `adapter/wsgi.py` `_not_found`/`_method_not_allowed`;
- 4 `app.after_request`;
- 1 `app.before_request`;
- 3 `bp.get` and 3 `bp.route`;
- 6 registration records.

The test pins the analyzer's discovered signatures against it, which the test file monkeypatches in its fixtures (lines 2102 onward).

### 5.10 Tests that pin current behavior

- `tests/http/test_endpoint_catalog.py`: 8 tests.
  - line 43 asserts the sampler row's `env_gate`;
  - lines 73 and 77 assert the production Reader row in the authored and tracked catalog;
  - line 84 asserts the governed 405.
- `tests/transport/test_a7_transport_proofs.py` line 91 builds the A7 family and asserts it restores `APP_ENV`.
- `tests/http/test_reader_a7_transport.py` line 79 sets `APP_ENV=dev`.
- `tests/adapter/test_gate_auth.py` deletes `APP_ENV` at lines 27 and 54. Under IF-10 an unset environment refuses `/reader`, so PR-20 reads which routes these tests exercise and records whether any expectation changes.
- `tests/reader_v1/test_schema.py` line 18 pins `ERR_READER_FORBIDDEN`.

`artifacts/architecture/architecture_snapshot.keys_only.json` is a capture dated 2026-07-14. Its route line numbers already differ from the code, and `tests/evidence/test_architecture_snapshot.py` passes at the baseline, so this unit does not regenerate it. If PR-20 finds that a change here makes that test fail, it is a finding (§14), not a hand edit.

## 6. Bounded files and components

Plan v1.1 §7 WU-PR-03 "Deliverables" approves each locus, except those marked ID-3 or ID-4, which this instruction binds.

| Path | Bound |
| :- | :- |
| `adapter/factory.py` | S02 / IF-11: app-level 404 and 405 handlers. Compat shaping and the production Reader's governed 405 unchanged |
| `adapter/http_reader.py` (member) | S10 / IF-10: the `/reader` gate. S02 / IF-11: the `create_app` factory's handlers. No route added or removed; `__main__` unchanged |
| `engine/cli/main.py` (member) | S07: the `showcompat` help string only |
| `tools/evidence/generate_a7_transport_proofs.py` | S15 / IF-6 / ID-1: catalog rows, `CLASS`, validator (the `aliases` key; the class set; existing pins kept) |
| Regenerated by that owner, then the updater | `docs/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/audit/ENDPOINTS_CATALOG.json` and `.sha256`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/*` (the A7 family) and their path proofs; Index and Mirror companions |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | ID-4: `ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` data only |
| `ci/checks/classify_ci_changes.py`; `tests/evidence/test_rails_ci_workflow_integration.py` | ID-3: the smallest registration for `VERIFY.sh`, `dev/reader_harness/*` and an owner test for `scripts/dev_start_reader.sh`; pins kept true |
| `scripts/dev_start_reader.sh` | EC-4: default `APP_ENV=dev` when unset |
| `VERIFY.sh` | S09 / EC-2: run against the canonical runner; its checks stay meaningful, or the unit records which it no longer performs |
| `dev/reader_harness/app.py`, `dev/reader_harness/__init__.py` | S09 / EC-2: removed |
| `docs/acceptance/reader_a7_crib.md`; `docs/server/reader_v1.md` | S09 start line and legacy notice; S10 gate and runner default; S02 the line-20 known limitation |
| `engine/emit_public.py`; `tests/runtime/test_emit_public_legacy_helper.py` | docstrings only (S09) |
| `docs/ADAPTER_009.md` | S18: the `COMPAT_GET_BODY_400_OK` line only |
| `ARCHITECTURE.md` | S18: emitter return type and the routing/mounts statements |
| `docs/CLI_commands.md` | S07 / EC-6: remove the known-gap sentence |
| Tests under `tests/http/`, `tests/cli/`, `tests/transport/`, `tests/adapter/` | S02 per-factory matrix; S10 environment matrix; S07 help assertion; S15 route enumeration (ID-1); the runner-default test (ID-3 owner) |
| `catalog/manifest.json` | the refresh at `1.3.0` / `2026-08-24T18:04:49Z`, by the cutter only |
| Every evidence family the refresh regenerates, by its owner (Plan §10 steps 3–11), and the Index/Mirror by the updater | as the convergence requires |
| `docs/ephemeral/` PR result records | evidence obligations (§10) |

Any other file the work needs is a finding: route it under §14 before changing it. In particular:
- `engine/http/compat_handler.py`, `engine/presenter/**`, `engine/config/registry_loader.py`, `tools/evidence/update_evidence_index.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py` are expected to stay unchanged;
- `artifacts/vendor/hdapi_v2/**`, `artifacts/architecture/**` and every frozen family stay byte-unchanged.

## 7. Exclusions

- No route added or removed. No public contract, payload, flag or transport change. No change to the production Reader's governed 405 or to compat shaping (Specification Exclusions; Plan §4 invariant 1).
- No version bump and no admission-constant change: the refresh stays at `1.3.0` (WU-PR-08 owns `1.4.0`).
- No canon edit. No PF12 registration of `public_aux` or `aliases` (doc-delta candidate). No PF10 addendum.
- No hand edit of any governed artifact. Frozen families (`artifacts/cli/**`, `artifacts/identity/**`, `artifacts/math/**`, `artifacts/vendor/**`, `audit/ops/**` and the PR06b §6.4 list) keep their bytes, which their `--check` modes verify.
- No `AGENTS.md`, `README.md` or `CHANGELOG.md` edit (WU-DOC-01). No `.env.example` and no S17 line of `docs/ADAPTER_009.md` (WU-PR-08).
- No skipped, disabled, `xfail`-marked or quarantined test.
- No change to the `0.0.0.0` bind or to the production mount of the gated dev blueprint (observation OBS-W3-1, §15).
- No live vendor, production or database call; closed rails throughout.

## 8. Interface contracts with other units

| Contract | Consumer | Content |
| :- | :- | :- |
| E-1 Catalog model | WU-PR-05 (S19), WU-DOC-01, QA | The catalog lists every served `(method, path)` under ID-1, with the exclusion table in the enumeration test. A later route change adds or removes rows through the A7 owner. The Aux record carries `public_aux` and `aliases` without a conformance claim |
| E-2 Not-found envelope | QA (S02 Live QA step), WU-PR-05 | All three factories answer unknown paths with the governed `ERR_NOT_FOUND` envelope (`no-store`, no ETag, JSON). PR-20 decides whether the 405 handler keeps `Allow`; the decision stays fixed for later units |
| E-3 Release base | WU-PR-04, WU-PR-05 | This unit's refreshed `release_id` and converged evidence are the next refresh's base. The result record names the `release_id` |
| E-4 Classifier registrations | WU-PR-06 (the pre-push check delegates to the classifier) | The ID-3 registrations are part of the classifier's rules |
| E-5 Contract-inventory baseline | WU-PR-05, any later adapter change | The baseline equals the factories' records at this unit's head |
| E-6 Dev route and runner | QA (S10 Live QA refusal), WU-DOC-01 | `/reader` served only for `APP_ENV=dev`. The runner defaults `APP_ENV=dev`. `VERIFY.sh` uses the canonical runner |

## 9. Disposition rules PR-20 must apply and record

1. **S02 design (IF-11).**
   - Reuse the `adapter/wsgi.py` pattern. In `adapter/http_reader.py::create_app`, replace the compat-scoped `return err` branches; keep the compat responses byte-identical.
   - Decide and record whether the 405 handlers keep the framework's `Allow` header.
   - Cover HEAD (no body) and OPTIONS on unknown paths.
   - Keep the `/internal/` ETag stripping and the `/ops/writer/diagnostic` Content-Length rule.
2. **S10 gate (IF-10).** Normalize the value as `_dev_admin_gate` does (strip, lower), but serve only `dev`. Unset, empty, `test`, `local`, `prod`, `production`, `live` and arbitrary values return `ERR_READER_FORBIDDEN` 403. The `v` validation order (400 `ERR_READER_INVALID_VERSION`) stays as it is or changes only with the reason recorded.
3. **S15 rows (ID-1).** For each new row, read the view and its guard for:
   - `env_gate` (a string or object, per HDE Schemas & Artifacts §8.8);
   - `rails_profile` (names-only);
   - `classification` (from the §8.8 set, plus `public_aux`);
   - `internal`, `a7_eligible: false`, `blueprint_module` (`adapter.http_reader`, `engine.http.compat_handler` or `adapter.wsgi`).

   Write the exclusion table with one reason per pair. Keep `success_endpoints` exactly `[GET /reader]`, the `/reader` rows' `env_gate` `APP_ENV=dev`, and the existing pins.
4. **S07 text.** Name the `magic10_compat_result.v1` stdout contract, consistent with `docs/CLI_commands.md` line 25. Reader v1 bytes only through `--dump-reader`.
5. **S09 `VERIFY.sh`.** Start the canonical runner, defaulting `APP_ENV=dev` and binding a port. Probe `/reader?v=1` on `127.0.0.1` (HDE-CLI-API-Vendor-Ref §5.4 documented host). Keep each check, or record which one no longer applies and why. Run it once and record the result.
6. **ID-3 registration.** Choose the smallest lane assignment for `VERIFY.sh` and the deleted harness paths, and a real owner test for `scripts/dev_start_reader.sh` (for example, one that runs the script with `APP_ENV` unset and observes the default). Name the registry keys.
7. **ID-4 baseline.** Rebuild the records from the PR head with the analyzer's own signature function, as the test fixtures do. Review them against HDE-CLI-API-Vendor-Ref §5.1.0 and §5.4. Record the diff in the plan.
8. **Refresh order.** Follow Plan v1.1 §10 steps 1–12 with §5.7's rules (a)–(d). The member edits and the cut come before any updater run. The A7 owner run (catalog plus proofs) is part of step 7. Record every step, each second-run byte-stability result and the stale-binding sweep.
9. **Record every stale document.** Name each document or canon passage this unit makes stale but may not change (§15), with its owner.

## 10. Acceptance, tests and evidence

**Plan v1.1 §7 WU-PR-03 acceptance, verbatim**, with the binding readings in brackets:
1. "Unknown paths on the production factory and the `adapter/http_reader.py` factory return the IF-11 envelope for GET, HEAD, POST and OPTIONS; the compat and `api_bp` behaviors are unchanged." [HEAD carries no body; ID-1 does not affect this item.]
2. "`GET /reader` is served for `APP_ENV=dev` and refused (403, `ERR_READER_FORBIDDEN`) for unset, empty, `test`, `local`, `prod`, `production`, `live` and arbitrary values; `scripts/dev_start_reader.sh` without `APP_ENV` starts a serving runner."
3. "`hdctl --help` names the `magic10_compat_result.v1` stdout contract; `ci/checks/check_cli_help.sh` exits 0; `generate_cli_conformance_artifacts.py --check` exits 0 (frozen family untouched, nonclaim recorded)."
4. "`dev/reader_harness/app.py` no longer exists; `VERIFY.sh` runs against the canonical runner; no active file references the harness." [Active means outside the historical prefixes and canon listed in §5.4. Canon references are doc-delta candidates (ID-2).]
5. "Every `(method, path)` rule of the three factories has a catalog row; the catalog validator accepts the IF-6 model; `docs/ENDPOINTS_CATALOG.json` equals its mirror byte for byte; `success_endpoints` unchanged." [Read under ID-1: the enumeration test applies the reasoned exclusion table.]
6. "The documents state `invalid_json`, the emitter's real return type, and the production mounts."
7. "Admission at the PR head reports `1.3.0`, 45 members and the refreshed `release_id`; every convergence step byte-stable on a second run; `release_id_recompute.py --check-manifest-only` exits 0; all lanes green." [All seven lanes run because of ID-3.]

**Evidence obligations**, verbatim from the Plan: "PR result record naming the refreshed `release_id` and every regenerated family; the catalog diff; nonclaim for the frozen CLI help capture." The record also names:
- each check actually run, with counts;
- the S10 environment matrix result;
- the `VERIFY.sh` run;
- the ID-1 exclusion table;
- the ID-3 registry keys;
- the ID-4 baseline diff;
- the stale-document list (§9.9).

**Validation PR-20 plans** (minimum):
- The four lanes the touched members select. The full-validation lanes follow from ID-3.
- Every test file that imports or runs `tools/evidence/update_evidence_index.py` (lineage review v1.0 LR-O2), because the refresh rewrites the Index and Mirror. A full `tests/` sweep in a detached worktree also satisfies this. `ruby` must be on `PATH` (§5.8).
- The A7 owner's checks; the canonical JSON gate `--check-only`; the updater `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `check_mirror_schema.sh`; `check_evidence_index_hash.sh`; `check_lf_endings.py`; `check_final_lf.sh`; `refresh_step_logs_manifest.py --check`.
- The frozen families' `--check` modes (Plan §10 step 10).
- The attestation build and verify into an external empty directory with `--require-clean` (Plan §10 step 12). This needs a CI-like Python 3.12 environment.
- Each run that can write tracked files runs in a detached worktree and ends with `git diff --exit-code` and an empty untracked status.

| Requirement | Acceptance item | Proof | Stage |
| :- | :- | :- | :- |
| S02 | (1) | per-factory unknown-path matrix (status, body bytes, `Cache-Control: no-store`, no ETag, `Content-Type`), compat and `api_bp` regressions | PR-30; CI |
| S10 | (2) | environment matrix test; the runner-default test; the A7 env-gate proof regenerated | PR-30; CI |
| S07 | (3) | help assertion; `check_cli_help.sh`; frozen `--check` | PR-30; CI |
| S09 | (4) | absence; `VERIFY.sh` run; reference search | PR-30 |
| S15 | (5) | the enumeration test (ID-1); validator; mirror equality; updater `--check` | PR-30; CI |
| S18 | (6) | the corrected statements quoted in the result | PR-30 |
| Refresh | (7) | admission; second-run byte stability; recompute; seven lanes | PR-30; PR-35 (CI) |

## 11. Migration and security constraints

- **Migration:** none (no data or schema change).
- **Rollback:** Nathan's revert of the squash commit, followed by a same-version manifest refresh, because this unit changes members (Plan §7 common paragraph).
- **Security:**
  - S02 and S10 narrow exposure only: no route opens.
  - The `/reader` gate never serves an unset, empty or non-`dev` environment.
  - Catalog fields are names-only, with no secrets, URLs or payload bytes (HDE Schemas & Artifacts §8.8).
  - `VERIFY.sh` binds `127.0.0.1` for its probe target.
  - The refresh opens no rail.
  - No secret, token or key value appears in tests, logs or records.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, the §5 and §6 repository files, and canon on `main`;
  - writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/` (design per §9, requirement-to-change/test map, ordered steps including the full Plan §10 convergence, risks, recovery);
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan):
  - recovers existing work first;
  - implements only the authorized scope;
  - converges the evidence by owners only;
  - tests locally under §10;
  - makes one coherent commit, or a coherent sequence when the convergence needs it;
  - publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings (PF10 addendum 2.3: the Codex security review is not part of the chain);
  - retests, and pushes coherent corrections. Any member change re-runs the refresh from §10 step 2;
  - uses CI economically;
  - verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
  - returns `MERGE_PENDING` without merging.
- **PR description:** `.github/pull_request_template.md` headings with the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage and, on ACCEPT, issues WU-PR-04's instruction.
- **Attributable lineage:** the PR result records, the PR reference and the squash commit.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- **A failed or interrupted refresh** restarts per Plan §10:
  - a member change after step 2 restarts at step 2;
  - an evidence-primary change restarts at step 5.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version, never an edit of v1.0.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or budget, schedule or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions), and this IA reviews it through RS-20. The decision returns to the PR-20 planning context.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:**
  - a served `(method, path)` that fits no ID-1 class and has no defensible row;
  - a route that must be removed;
  - a change needed outside §6 (in particular to `compat_handler.py`, the presenter, the updater, the boundary analyzer or a frozen family);
  - a classifier change beyond ID-3;
  - a contract-inventory change beyond ID-4's data;
  - an architecture-snapshot test failure;
  - a frozen-family `--check` failure after the refresh.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| S02 405 `Allow` header; S15 row details; `VERIFY.sh` predicates; ID-3 registry keys; ID-4 baseline diff | PR-20 session | In the plan |
| LR-O1 (the label is not proof that an owner ran; CX-2 residual) and LR-O3 (updater before the cut; label timing; stale labels), lineage review v1.0 §7 | this unit applies them (§5.7); IA carries them to WU-PR-04, WU-PR-05 and WU-PR-08 | Applied here |
| LR-O2 (run every updater consumer on an updater change) | IA | Not triggered: the updater does not change here. Its consumers still run because the refresh rewrites the Index and Mirror (§10) |
| PF10 addendum 2.2 downstream item (generator baseline) | this unit (ID-4) | In scope |
| OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` | QA tool and test owner, through the IA; Product Owner to route | A qa-lane failure of that test on this PR is recorded as OBS-17, never "fixed" here. ID-3 runs the qa lane |
| O-6: hosted `ruby` version unprinted | IA | PR-35 records it if the job log shows it |
| **OBS-W3-1** (new): HDE-CLI-API-Vendor-Ref §5.4 "Gate" says the dev route "must be gated by `APP_ENV=dev` and bound only to a local interface … or disabled entirely. It must not be mounted in production builds or non-dev deploys." The runner binds `0.0.0.0` (`adapter/http_reader.py` line 1218), and `adapter/factory.py` mounts the gated dev blueprint in production (403 there today). No HDE-CRD-0002 requirement asks for a change, so it is outside this unit (§7) | IA reports it; Product Owner decides any route | Recorded |
| Doc-delta candidates (not edited here) | Product Owner (canon); WU-DOC-01 (repository docs) | Recorded |

The doc-delta candidates are:
- HDE-CLI-API-Vendor-Ref §5.1.7 "Known limits remain: unknown non-compat paths … receive framework HTML 404" (stale after S02), and §5.1 line 2071's reference to it;
- HDE Architecture §3.8.1 "Current repository discrepancy" and HDE Math Spec's "Dev Reader harness: `dev/reader_harness/app.py`" bullet (stale after S09; ID-2);
- HDE Schemas & Artifacts §8.8 registration of `public_aux`, `aliases` and the ID-1 population rule (R-7);
- `README.md` and `CHANGELOG.md` references (WU-DOC-01).

AQ-1 gates WU-PR-07 only.

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |

No new conflict:
- The S10 reading is the approved Plan's (§4).
- ID-1 and ID-2 apply HDE Schemas & Artifacts §8.8, HDE-CLI-API-Vendor-Ref §5.4 and §5.6, and HDE Architecture §3.8.1 as written, within the Plan's own wording.
- OBS-W3-1 is a pre-existing gap between canon and the repository, outside every HDE-CRD-0002 requirement. It is recorded for its owner and not resolved here.

Coverage read for this unit: HDE-CLI-API-Vendor-Ref §5.1.7, §5.2 item 1, §5.4, §5.6, §5.7 (route lines); HDE Schemas & Artifacts §8.8 in full; HDE Architecture §3.8.1; HDE Math Spec dev-harness bullet; Glow Infrastructure "Production rails" (production `APP_ENV` aliases).

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S02 "every 404 … governed `ERR_NOT_FOUND` … never Flask HTML" | no HTML error page from the production app | IF-11 handlers on two factories; 405 included | WU-PR-03 | (1) | PR-30; CI; Live QA |
| S07 "describes … `magic10_compat_result.v1` output" | help text matches the stdout contract | string change; frozen capture kept with a nonclaim | WU-PR-03 | (3) | PR-30; CI |
| S09 "imports and runs, or it is retired …" | no broken harness referenced | retire; repoint `VERIFY.sh` and the crib; the canonical runner is the harness (ID-2) | WU-PR-03 | (4) | PR-30 |
| S10 "served only when … explicitly …" | explicit-environment gate | explicit `dev` only (approved Plan; canon) | WU-PR-03 | (2) | PR-30; CI; Live QA |
| S15 "every registered route has a catalog entry … mirror by its owner" | inventory matches served routes | per-method rows under ID-1; owner regenerates catalog and mirror | WU-PR-03 | (5) | PR-30; CI |
| S18 statements | documents match code | three statements corrected | WU-PR-03 | (6) | PR-30 |
| Plan "same-version manifest refresh and convergence" | admission and evidence current after member changes | Plan §10 order with §5.7 (a)–(d) | WU-PR-03 | (7) | PR-30; PR-35 |
| Addendum 2.2 "keep the generator's baseline current" | analyzer baseline equals factories | ID-4 data refresh | WU-PR-03 | (7) lanes; contract-inventory test | PR-30; CI |

Checks against the full PR-20 contract:
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries the Specification, Audit, Plan and review lineage, the PF10 path and overlays, the baseline, loci, exclusions, interfaces, dependencies, acceptance, evidence, migration, security, recovery, rescope, merge ownership and the return owner.
- No decisive comparison fails. The facts in §5 were measured at `ad11821` by this IA, not carried unverified.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-03 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:**
  - PR-40 lineage review after Nathan's merge;
  - rescope review through RS-20;
  - same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-03)

Action sent (v6): "Write, in a new dedicated session, the detailed PR implementation plan for one work unit of an approved change, a first plan for this unit: correct public, dev and CLI surfaces across about fifteen files (a governed not-found envelope on two of three web app factories, an explicit-dev gate on a dev route, a CLI help string, retirement of a broken dev harness with its verify script, runner script and documents, an endpoint catalog grown from 10 rows to every served route method with its generator and validator, two operator documents), plus a CI classifier registration for three paths it refuses today and a data-only refresh of a contract-inventory route baseline; two release members change, so a same-version release manifest refresh and a twelve-step governed-evidence convergence run in a fixed order under a newly landed release-label model. Planning only, with a prototype in a throwaway copy; no live vendor, production or database run; a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.36 (confidence 0.73); rung probabilities low 0.00, medium 0.03, high 0.60, extra high 0.36, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.20, Opus 5.5 0.80 (confidence 0.60). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.48, Opus 5.5 at extra high 0.29, Opus 5.5 at max 0.01, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.12, Fable 5.1 at extra high 0.07, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-14T00:31:01Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T00:31:01Z; HTTP 200 in 0.52 s; 4312 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- **Notion row:** not written, as PR-10 directs. **Nathan's pick for PR-20:** not stated. **For this PR-10 session:** not stated (reading in WU-PR-02 lineage review v2.0 §11).

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** The prototype and the convergence rehearsal need a Python 3.12 environment with CI's install (package-index access for `pip install`) and `ruby` on `PATH` for the contract-inventory test (present at `/usr/local/bin/ruby` in the cloud container used for this instruction).
- **Run times observed in this lineage.** A full `tests/` sweep takes about 20–25 minutes; the evidence lane about 13; an attestation build about 3.
- **Access.** No live vendor, production or database access is needed.
- **Order.** This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33Z) |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | 2026-10-14T00:31:02Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating) |

## Canon relied on

Read on `main` at `ad11821`.

| Topic | Sources and sections |
| :- | :- |
| Instruction authority, content and readiness | PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (PR Instructions are the IA's; Proceed per detailed PR plan; PR merges remain Product Owner actions) and §9.1.2 (canon precedence over in-flight documents; ID-1 and ID-2 rest on it) |
| Overlays and carried items | PF10-HDE-Build-Notes v13.5.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`) addenda 2.2 ("Approved delta", "Binding requirements", "Affected surfaces / Downstream work"), 2.3 (Rules 1–5), 2.5 (carried items for WU-PR-03; next-stage basis), 2.1 (§19) |
| S02 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.2 item 1 (governed not-found responses emit error_v1); §5.1.0 line 2071 and §5.1.7 "Known limits" (the gap S02 closes) |
| S10, S09, OBS-W3-1 | HDE-CLI-API-Vendor-Ref §5.4 "Route and gate (must)" and "Emitter and parity (must)"; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8 "Reader surface routes and distinct contracts (normative)"; HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.8.1 "Dev/QA Reader availability" (ID-2); HDE Math Spec (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.8.md`) §12 "Implementation Notes (non-normative; repo pointers)", dev-harness bullet (line 2257); Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) "Production rails and CI-lane boundary" (production `APP_ENV` aliases) |
| S15, ID-1 | HDE-CLI-API-Vendor-Ref §5.6 "Endpoint Catalog (JSON success)" (read in full: ownership, the method table, the Aux record, aliases, R-7 registration rule) and §5.7 route lines; HDE Schemas & Artifacts §8.8 (read in full: authoritative file, sidecars, inventory scope, normative Reader surfaces, success-proof designation, minimum fields, classes, indexing, env-gate pairing) |
| Release refresh | Implementation Plan v1.1 §10; Audit §5.1 and §7.3; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; WU-PR-02 lineage review v1.0 §7 (LR-O1 to LR-O3) |
| In-flight documents | Specification v1.1 rows S02, S07, S09, S10, S15, S18 (and S03 for the test-coverage outcome); Plan v1.1 §4, §5 (IF-6, IF-10, IF-11), §6, §7 (common paragraph; WU-PR-03 block), §10, §11 (R-2, R-7, R-8), §12, §13, §15; review v1.1 R1.1–R1.3; Audit §5.1, §5.5, §5.6, §6 S02/S07/S09/S10/S15/S18, §7.1, §7.3, §7.5, §7.6; WU-PR-02 instruction v1.0 §8 (D-1); WU-PR-02 lineage reviews v1.0 and v2.0 |
| Operative documentation | `AGENTS.md` (canon-first rule; dev-only conjunction routes and `docs/ENDPOINTS_CATALOG.json` as source of truth with its audit mirror; sole Index/Mirror writer; no hand edits; closed rails; pytest readiness; PR descriptions) |
