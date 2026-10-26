# Redlines — PF02-Canon-HDE-Architecture from v2.4.6

## Package identity

- Package: `redlines-PF02-from-v2.4.6.md`, with its proof log `redlines-PF02-from-v2.4.6.proof-log.md` in the same directory.
- Run identity: `gtwpe-20261026-pf10-v13-8-8/T-PF02/TW-DRAIN-10/r1`.
- Preparer: TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff), run in Claude Code session https://claude.ai/code/session_01M9PsXYe8yx3bTeqJUj1sTL, started by Nathan for T-PF02.
- Preparation outcome: `READY`. Save completeness is recorded in the proof log after read-back.
- Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF02, rows A06 (context), A07, A08 with X04, A10 with X06.

## Original baseline

- Path: `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`.
- In-document title: `PF02-Canon-HDE-Architecture`; version `v2.4.6`; status `Canon`; effective date `2026-10-09`.
- Read at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (the ledger baseline) and again at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`; the blob is the same at both: `b0bf3d66965d0de91044b519a29bc30b1cc2d040`.
- Raw bytes: 140,533 bytes; 1,617 lines; LF only; no BOM; no final LF; SHA-256 `4bfa53ad9775f6b69432b28ae11048b6458461249186c9bb9161e51e5ecb28db`.

## Change source

- `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, HDE Build Notes v13.8.8; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`.
- Selected units, each read in full: front matter lines 1–223; addendum 2.6 lines 531–687 (context only); 2.7 lines 688–889; 2.8 lines 890–1002; 2.10 lines 1102–1204.
- Supporting cross-references, read at their boundaries and not change sources in their own right: X04 `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` §18, lines 753–792 (blob `1d6a92a483e2`); X06 `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md` §10, lines 156–165 (blob `20b170490447`).

## Metadata inputs for TW-APPLY-10

This package carries no document-control redline. TW-APPLY-10 derives the header from these facts:

- Native header schema (lines 3–11 of the original): `**Title:**`, `**Version:**`, `**Status:**`, `**Effective date:**`, `**Last Update Gate:**`, `**Invocation tag:**`, in that order.
- Version scheme: `v` followed by three dot-separated integers; baseline `v2.4.6`.
- Date format: `YYYY-MM-DD`; baseline `2026-10-09`.
- Sources that justified the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, PF10 version 13.8.8. No other file is a change source.
- PF02 carries no change log or revision-history entry format, so no history redline is required. The target carries no draft-status language, placeholder, TODO, unresolved drafting note, editorial comment or instruction to a future writer; its placeholder mentions (lines 181, 1160 and 1218) are canon rules that require that exact language.

## Literal convention

Each OLD and NEW literal is the exact byte sequence between the line that opens its four-backtick `text` fence and the line that closes it, joined by LF, with no LF after its last line. Trailing spaces inside a literal are part of it. Every OLD literal is matched against the whole original document, case-sensitively and byte-exactly; line numbers are informative and never locate an edit.

## Redlines

### RL-01 — §3.3: the production-posture refusal replaces the stale mount discrepancy

- Operation: `REPLACE`.
- Change type: CANON_UPDATE.
- Target document: PF02-Canon-HDE-Architecture.
- Heading path: `# **3\. Runtime surfaces (by responsibility, not bytes)**` > `## **3.3 Sample (dev harness) (dev-only)**` > paragraph `**Current repository discrepancy.**`.
- Original location (informative): lines 896–897.
- Expected occurrence of the OLD block in the whole document: 1.
- Ledger rows: A10 with X06.
- Basis: HDE Build Notes 2.10 records S19-F03 delivered by #656 and routes HDE Architecture §3.3 to the Product Owner as a stale canon passage (X06 §10; WU-PR-05 plan v1.0 §19 names the stale statement "the selected factory registers the Reader blueprint without an environment-specific unmount"). Verified on `main` `0838ba0`: `get_reader_bp` calls `bp.record(_mount_for_production)`; `_production_posture` uses `adapter.env_guard._compute_env_mode`, the resolution the compat handler also uses; the hook refuses the dev `GET /reader` endpoint and the four dev/admin endpoints and reads no request-time environment value; no rule is added or removed.

OLD:

````text
**Current repository discrepancy.**  
The selected factory registers the Reader blueprint without an environment-specific unmount. The dev route handlers enforce a request-time gate, but static repository bytes do not establish that the routes are never mounted in production or that any route is runtime-reachable.
````

NEW:

````text
**Current repository behavior (production posture) \[Implemented\].**  
At repository commit `0838ba08254eaefc888019df49a06aa2ae99cc6c`, the dev/internal blueprint that defines these routes records one registration-time callback, so `adapter/factory.py`, `adapter/http_reader.py::create_app` and `adapter/wsgi.py` apply the same production posture when they register it. The callback resolves the posture once, at registration, as **HDE-CLI-API-Vendor-Ref** resolves the production-like posture for compat v1. In a production-like posture it installs one application-level hook that refuses the dev `GET /reader` route, `POST /internal/dev/sampler` and the three dev conjunction routes before any of their handlers runs, whatever `APP_ENV` holds at request time. In every other posture registration is unchanged, and each handler keeps its own request-time gate. No route is added or removed: the registered rules are the same in every posture.

**Static inspection cannot establish.**  
Static repository bytes do not establish the posture of any deployed process, production enablement, or that any route is runtime-reachable.
````

### RL-02 — §3.4: the liveness and readiness probes are required, not speculative

- Operation: `REPLACE`.
- Change type: CONSISTENCY.
- Target document: PF02-Canon-HDE-Architecture.
- Heading path: `# **3\. Runtime surfaces (by responsibility, not bytes)**` > `## **3.4 Internal ops signals**` > label `**Future concepts \[Speculative\].**`.
- Original location (informative): line 914.
- Expected occurrence of the OLD block in the whole document: 1.
- Ledger rows: A07; A08 with X04 (the same §3.4 item).
- Basis: HDE Build Notes 2.7 names as a canon doc-delta candidate "HDE Architecture §3.4, which labels the health probes speculative, while HDE Mechanics Guide §32.3 requires them"; 2.8 carries it and plan v2.0 §18 (X04, line 763) restates it. HDE Mechanics Guide §32 is `[Required-Now]`, states that Mechanics owns health/ready behavior, and §32.3 requires a liveness and a readiness probe. The bullets, the identity surface, the boundary and the current-behavior paragraph that follow are unchanged; the current-behavior paragraph was verified true on `main` `0838ba0`.

OLD:

````text
**Future concepts \[Speculative\].**
````

NEW:

````text
**Liveness and readiness probes \[Required-Now\].**  
**HDE-Mechanics Guide** requires a liveness probe and a readiness probe and owns their behavior and probe bytes; PF02 records their architectural roles only.
````

### RL-03 — §3.5: the retired routes answer as unknown paths in a production-like posture

- Operation: `REPLACE`.
- Change type: CANON_UPDATE.
- Target document: PF02-Canon-HDE-Architecture.
- Heading path: `# **3\. Runtime surfaces (by responsibility, not bytes)**` > `## **3.5 Internal-ops identity and refusal (route-only)**` > paragraph `**Current repository discrepancy.**`.
- Original location (informative): lines 955–956.
- Expected occurrence of the OLD block in the whole document: 1.
- Ledger rows: A10 with X06.
- Basis: HDE Build Notes 2.10 routes HDE Architecture §3.5 as a stale canon passage (X06 §10); WU-PR-05 plan v1.0 §19 names the stale statement: the retired routes' "continued presence in the selected blueprint", where "the code stays, a production-like application answers them as unknown paths". Verified on `main` `0838ba0`: the three routes remain defined in the blueprint that the three factories register; `_refuse_in_production` answers their endpoints, and a method no rule names on their paths, with the application's not-found answer before any handler runs; the Endpoint Catalog holds 18 records and none for these paths. The `RETIRED/NONCANONICAL` classification, the non-description sentence and the nonclaim sentence are retained.

OLD:

````text
**Current repository discrepancy.**  
The checked-in `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic` routes are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog. Their continued presence in the selected blueprint is repository drift; this document does not describe them as supported ops, admin, diagnostic, evidence, product, or public interfaces. No repository removal, test migration, deployment convergence, or catalog mutation is claimed.
````

NEW:

````text
**Current repository discrepancy.**  
The checked-in `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic` routes are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog. At repository commit `0838ba08254eaefc888019df49a06aa2ae99cc6c`, their handlers remain in the blueprint that `adapter/factory.py`, `adapter/http_reader.py::create_app` and `adapter/wsgi.py` register, and that continued presence is repository drift; this document does not describe them as supported ops, admin, diagnostic, evidence, product, or public interfaces. In a production-like posture the blueprint's registration-time hook (§3.3) answers every request routed to these paths as the application answers an unknown path, before any of their handlers runs; in any other posture their handlers still run. No repository removal, test migration, deployment convergence, or catalog mutation is claimed.
````

### RL-04 — §3.8.1: the dev server registers the production routes, and a production-like posture refuses the dev-only ones

- Operation: `REPLACE`.
- Change type: CANON_UPDATE.
- Target document: PF02-Canon-HDE-Architecture.
- Heading path: `# **3\. Runtime surfaces (by responsibility, not bytes)**` > `## **3.8 Reader dev/QA posture & services \[Required-Now\]**` > `### **3.8.1 Dev/QA Reader availability**` > bullet beginning `* In dev/QA, the adapter/Reader stack is hosted`.
- Original location (informative): line 1089.
- Expected occurrence of the OLD block in the whole document: 1.
- Ledger rows: A10 with X06.
- Basis: HDE Build Notes 2.10 routes HDE Architecture §3.8.1 as a stale canon passage (X06 §10); WU-PR-05 plan v1.0 §19 names the stale statement "exposes the same Reader and internal/dev sampler routes as the production adapter". Verified on `main` `0838ba0`: `adapter.http_reader.create_app` and `adapter.factory.create_app` register the same three blueprints, and the production-posture hook of RL-01 refuses the dev-only routes before their handlers run. The bullet's remaining text is unchanged.

OLD:

````text
* In dev/QA, the adapter/Reader stack is hosted by a concrete framework development HTTP server (currently a Flask dev server) that exposes the same Reader and internal/dev sampler routes as the production adapter. Architecture treats this dev server as part of the adapter and dev harness component: it is a real, required piece of the system in dev/QA, but the choice of framework and all start commands, ports, and environment wiring remain the responsibility of **Glow Infrastructure** and **HDE-Mechanics Guide**, not PF02.  
````

NEW:

````text
* In dev/QA, the adapter/Reader stack is hosted by a concrete framework development HTTP server (currently a Flask dev server) that registers the same Reader and internal/dev sampler routes as the production adapter. A production-like posture refuses the dev-only routes before any of their handlers runs (§3.3), so those handlers run only in a non-production posture, behind their own request-time gates. Architecture treats this dev server as part of the adapter and dev harness component: it is a real, required piece of the system in dev/QA, but the choice of framework and all start commands, ports, and environment wiring remain the responsibility of **Glow Infrastructure** and **HDE-Mechanics Guide**, not PF02.  
````

### RL-05 — §3.8.1: the retired harness and the root helpers, as they stand on `main`

- Operation: `REPLACE`.
- Change type: CANON_UPDATE.
- Target document: PF02-Canon-HDE-Architecture.
- Heading path: `# **3\. Runtime surfaces (by responsibility, not bytes)**` > `## **3.8 Reader dev/QA posture & services \[Required-Now\]**` > `### **3.8.1 Dev/QA Reader availability**` > paragraph `**Current repository discrepancy.**`.
- Original location (informative): lines 1093–1094.
- Expected occurrence of the OLD block in the whole document: 1.
- Ledger rows: A10 with X06 (§3.8.1 stale; the root helpers); A07 and A08 for the delivered harness retirement (S09); A06 as context (the start-helper posture stands).
- Basis: HDE Build Notes 2.10 routes HDE Architecture §3.8.1 as stale (X06 §10) and carries the root helpers as X-02 (OBS-P3-17), routed to the Product Owner and not decided; the S19 record states that under a production-like `APP_ENV` no harness handler is reachable through them. 2.7 and 2.8 record the dev harness retirement (S09) and the start helper's exact `APP_ENV` propagation (2.6 RP-1). HDE Mechanics Guide §34 names `scripts/dev_start_reader.sh` the canonical dev runner that invokes `python -m adapter.http_reader`. Verified on `main` `0838ba0`: no tracked path begins with `dev/reader_harness/`; the start helper exports `APP_ENV` only when the caller sets it and execs `python -m adapter.http_reader`; that module's `create_app` registers `bp`, `api_bp` under `/api` and `compat_blueprint`; `run_flask.py` imports `adapter.factory.create_app` and runs it with `use_reloader=True` and the debugger on unless its debug setting is changed; `run_flask_dev.sh` sets `FLASK_APP=adapter.factory:create_app` and `FLASK_DEBUG=1` and runs `run_flask.py`. The existing classification of the root helpers is retained; X-02 is not decided here.

OLD:

````text
**Current repository discrepancy.**  
At repository commit `cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, `dev/reader_harness/app.py` silently treats an absent `APP_ENV` as `dev`, registers only the Reader blueprint under `/api`, calls `app.getattr` instead of `app.register_blueprint`, and does not mount the compat blueprint. The root `run_flask_dev.sh` and `run_flask.py` helpers start `adapter.factory:create_app` rather than the dedicated harness. These checked-in facts do not satisfy the required dedicated-harness contract.
````

NEW:

````text
**Current repository behavior \[Implemented\].**  
At repository commit `0838ba08254eaefc888019df49a06aa2ae99cc6c`, no tracked path begins with `dev/reader_harness/`. `scripts/dev_start_reader.sh` propagates `APP_ENV` exactly as the calling environment supplies it and starts the `adapter.http_reader` module runner, whose application registers the dev/internal blueprint, the production Reader blueprint under `/api`, and the compat blueprint.

**Current repository discrepancy.**  
The root `run_flask_dev.sh` and `run_flask.py` helpers start `adapter.factory:create_app` rather than the module runner that `scripts/dev_start_reader.sh` starts, with the framework reloader on and the interactive debugger on by default. They are not the canonical start command, and these checked-in helpers do not satisfy the dev-harness contract above. In a production-like posture no dev-harness handler runs behind them either (§3.3).
````

## Batch summary

Five `REPLACE` operations, each with a unique OLD block, in original order RL-01, RL-02, RL-03, RL-04, RL-05. No two consume intersecting original bytes, no edit sits at another's boundary, and no NEW literal is used as another redline's locator. No `INSERT`, `DELETE` or repeated-replacement operation is used.

END OF REDLINES
