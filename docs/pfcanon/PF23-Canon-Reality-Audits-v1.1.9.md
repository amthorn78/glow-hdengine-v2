# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.9

**Status:** Canon

**Effective date:** 2026-08-21

**Last Update Gate:** HDE-EPIC039

---

**Intent & scope \[Required-Now\]**

These audits are **Codex review passes run by the Product Owner at the closure of each epic** to compare what actually shipped (code, evidence, repo layout) with what PF-Canon and the epic plan said should exist. Their purpose is to:

* Highlight any **gaps between reality and expectation** (missing evidence, drift from PF docs, unrecorded behavior, or unclosed issues).

* Produce a **historical record** of what was found at close (including any “unknowns” that become future work, PF10 addenda, PF20 issues, or PF09 updates).

* Feed back into canon and planning **after** the epic is closed, without blocking day-to-day execution.

These audits:

* Are **PO-only responsibilities**; they are **not** part of any agent plan, CRD, or implementation workflow.

* Do **not** introduce new acceptance gates for agents and must **not** be treated as tasks or subtasks in PF09 or PF20.

* Are **archived for history** as standalone artifacts (for example, under `audit/codex/...`) so future epics and doc updates can refer to them when reconciling drift.

Agents may **read** these audits as context when planning future work, but they do **not** schedule, trigger, or satisfy them.

# 1\) \- HD Engine Current Audit 

**Date:** 2026-08-21

# Audit Snapshot Metadata

* Repository root: /workspace/glow-hdengine-v2; confirmed because pwd and git rev-parse \--show-toplevel returned the same path. E-001  
* Commit: 273889f1a09d609ffbf77f0c77711c6294484b8f. E-002  
* Branch: work. E-003  
* Working tree: clean; git status \--porcelain produced no changed paths. E-004  
* Snapshot time: 2026-08-21T21:15:35Z. E-005  
* Kernel/OS: Linux 6.18.35 x86\_64 GNU/Linux. E-006  
* Python: Python 3.14.4. E-007  
* Node: v24.15.0. E-008  
* This audit used static inspection only; no tests, package installation, application execution, generators, or write-producing commands were run.

Evidence anchors

* E-001 | Repo state | pwd; git rev-parse \--show-toplevel | "/workspace/glow-hdengine-v2" returned by both commands  
* E-002 | Repo state | git rev-parse HEAD | "273889f1a09d609ffbf77f0c77711c6294484b8f"  
* E-003 | Repo state | git rev-parse \--abbrev-ref HEAD | "work"  
* E-004 | Repo state | git status \--porcelain | ""  
* E-005 | Repo state | date \-u \+'%Y-%m-%dT%H:%M:%SZ' | "2026-08-21T21:15:35Z"  
* E-006 | Repo state | uname \-srmo | "Linux 6.18.35 x86\_64 GNU/Linux"  
* E-007 | Repo state | python \--version | "Python 3.14.4"  
* E-008 | Repo state | node \--version | "v24.15.0"

# Top-level Repo Map

## Complete root listing

The complete root inspection found the following entries. E-009

* Source/runtime directories — Present: adapter/, catalog/, config/, engine/, errors/, internal/, math/, migrations/, narratives/, presenter/, schemas/, sql/.  
* Tests, fixtures, and expected-output directories — Present: assert/, fixtures/, freeze/, goldens/, parity/, proofs/, tests/, validation/.  
* Automation and delivery directories — Present: .devcontainer/, .github/, .vscode/, ci/, dev/, scripts/, tools/.  
* Documentation, evidence, reports, and retained-material directories — Present: .audit\_src/, .backup\_epic004/, \_arch/, \_archive/, artifacts/, audit/, codex/, docs/, handoff/, import/, notes/, release/, reports/, scan\_reports/.  
* Key root configuration/runtime files — Present: .env.example, .gitattributes, .gitignore, AGENTS.md, ARCHITECTURE.md, AcceptanceMap.md, CANON\_CHECKSUMS.json, CHANGELOG.md, LICENSE, Procfile, README.md, Run, VERIFY.sh, pyproject.toml, pytest.ini, requirements.txt, requirements-dev.txt, run\_flask.py, run\_flask\_dev.sh.  
* Observed root reports/plans — Present: Approved Remediation Plan EPIC029.md, EPIC023\_D12\_close\_pack\_manifest\_FINAL\_EVIDENCE.md, FLASK\_AUTO\_RUN\_GUIDE.md, HDE-EPIC023\_\_d07-codespaces-snapshot-d08-qa-doc-deltas-capture\_\_step\_report.md, IMPLEMENTATION\_REPORT\_r7\_header\_template.md, adapters.DEPRECATED.md, changes\_report.txt, dev\_sampler\_http\_consolidated.md, and the hde-epic023\_\_\*.md step-report family.  
* Observed root captures, temporary-looking files, archives, and helper scripts — Present: .body200.json, .code304.txt, .tmp\_refusal\_get.txt, .tmp\_refusal\_post.txt, \_backup\_1761350008.tgz, \_backup\_corrupted\_1761349750.tgz, \_backup\_corrupted\_1761349780.tgz, big.json, card\_close.sh, code304\_new.txt, manifest\_post.sha256, manifest\_pre.sha256, patch.diff, run\_d3\_2\_complete.sh, run\_d3\_2\_validation\_complete.sh, temp\_run.ec, temp\_run.err, temp\_run.out.

Representative anchors include engine/cli/main.py, adapter/http\_reader.py, presenter/reader\_v1/emitter.py, docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, audit/qa/, tools/evidence/, and .github/workflows/ci.yml. E-010

## Expected-family check

| Expected family | Classification | Observed location and role | Evidence |
| :---- | :---- | :---- | :---- |
| engine/ | Present | Main compute, sampler, compatibility, BodyGraph, DB, provider, runtime, CLI, serialization, and internal presenter packages. | E-010 |
| adapter/ | Present | Flask app factories, Reader blueprint, environment guards, headers, ETag helpers, and WSGI app. | E-010, E-020 |
| presenter/ | Present | Reader-v1 emitter and canonical comparison utility; an additional presenter implementation exists under engine/presenter/. | E-010, E-017 |
| CLI package | Present | engine/cli/, with engine.cli.main:cli registered as hdctl. | E-011, E-018 |
| docs/ | Present | Documentation, schemas, endpoint catalog, acceptance material, PF-canon files, and evidence index. | E-038 |
| artifacts/ | Present | Generated/captured JSON, text, logs, hashes, proof files, snapshots, bundles, and mirror index. | E-038 |
| audit/ | Present | QA, OPS, gate, doc-delta, preflight, and historical capture families. | E-038 |
| tools/ | Present | Evidence, QA, config, CLI, order, presenter, registry, and artifact generators/checkers. | E-043 |
| ci/ or workflows | Present | ci/checks/, reusable job definitions, and two GitHub workflows. | E-042 |
| tests/ | Present | Numerous labeled and unlabeled test subtrees covering HTTP, CLI, engine, BodyGraph, DB, evidence, and determinism. | E-041 |
| scripts/ | Present | Runtime/startup helpers, ingestion, DB jobs, release tools, QA/OPS probes, and evidence-oriented commands. | E-043 |

## Truth-bearing or governed-output roots

Seven top-level roots visibly contain documentation, catalogs, schemas, captures, proofs, snapshots, reports, or their producers: docs/, artifacts/, audit/, catalog/, proofs/, tools/, and scripts/. This is a path/count observation only. E-009, E-038, E-043  
Evidence anchors

* E-009 | Repo listing | find . \-mindepth 1 \-maxdepth 1 \-printf '%f\\t%y\\n' | LC\_ALL=C sort | "adapter d … artifacts d … audit d … docs d … engine d … presenter d … tests d … tools d"  
* E-010 | Repo listing | find engine adapter presenter internal narratives \-type f … | sort | "adapter/http\_reader.py; engine/compat/compute.py; engine/sampler/core.py; engine/bodygraph/vendor\_client.py; engine/db/adapter.py; presenter/reader\_v1/emitter.py"  
* E-038 | Repo listing | tracked-file counts and first-two-level grouping for docs, artifacts, and audit | "docs 151; artifacts 1022; audit 3015"  
* E-043 | Repo listing | find ci/checks tools scripts \-type f (...) | sort | "ci/checks/check\_env\_pins.sh … tools/evidence/update\_evidence\_index.py … scripts/ingest/run\_vendor\_ingest.py"

# Packaging and Entrypoints

## Packaging and build configuration

* pyproject.toml declares project glow-hdengine, version 0.0.0, Python \>=3.10, setuptools/wheel build requirements, and the console script hdctl \= engine.cli.main:cli. Package discovery includes engine\*, adapter\*, presenter\*, catalog\*, and math\*; package data includes JSON files for catalog and math. E-011  
* requirements.txt declares Flask, Gunicorn, psycopg binary, and jsonschema runtime dependencies. requirements-dev.txt declares jsonschema, pytest, pytest-cov, and pytest-mock. E-012  
* pytest.ini supplies the configured test paths and epic markers. Its test paths are selective rather than all subdirectories visible under tests/. E-013  
* No packaging conclusion is made here about uninspected external workspace metadata; the observed Python packaging authority is pyproject.toml.

## Runtime and command entrypoints

| Entrypoint | Symbol | Observed role and invocation |
| :---- | :---- | :---- |
| adapter/wsgi.py | create\_app, module-level app | Creates the Flask application, installs logging/environment guards, registers Reader and compat blueprints, and defines /internal/healthz and /internal/readyz. E-020 |
| adapter/factory.py | create\_app | Creates an alternate Flask app factory and mounts the Reader blueprint at "" and the compat blueprint at its own prefix. E-019 |
| run\_flask.py | module main block | Root HTTP startup entrypoint discovered by the \_\_main\_\_ scan. E-014 |
| engine/cli/main.py | cli | hdctl parser and dispatcher for showcompat, aux-preview, bg:resolve, and dev:sampler. E-011, E-018 |
| engine/cli/\_\_main\_\_.py | module main block | Enables package-module CLI execution. E-014 |
| scripts/bodygraph/run\_refresh\_worker.py | module main block | Background BodyGraph refresh worker entrypoint. E-043 |
| scripts/db/run\_retention\_job.py | module main block | DB retention-job entrypoint. E-043 |
| tools/evidence/update\_evidence\_index.py | main | Maintains the human evidence index, hash sentinel, machine mirror, and related proofs; supports check behavior through its parser. E-040 |
| tools/evidence/orientation\_demo.py | main | Reads the mirror and calls the evidence-index updater in write mode when not checking. E-040 |

Evidence anchors

* E-011 | Repo file | pyproject.toml | \[project\] and \[project.scripts\] | "name \= \\"glow-hdengine\\" … hdctl \= \\"engine.cli.main:cli\\""  
* E-012 | Repo file | requirements.txt, requirements-dev.txt | complete files | "psycopg\[binary\]\>=3.1,\<3.3 … Flask\>=2.3,\<3.0 … pytest\>=7.4,\<9.0"  
* E-013 | Repo file | pytest.ini | \[pytest\] | "testpaths \= tests/mech … tests/cli … tests/db … tests/qa"  
* E-014 | Repo listing | git grep for if \_\_name\_\_ \== "\_\_main\_\_" and parser/app definitions | "run\_flask.py:24 … engine/cli/\_\_main\_\_.py:14 … scripts/bodygraph/run\_refresh\_worker.py:290"  
* E-018 | Repo file | engine/cli/main.py | \_build\_parser, cli | "sub \= parser.add\_subparsers(dest=\\"command\\", required=True)"  
* E-019 | Repo file | adapter/factory.py | create\_app | "app.register\_blueprint(bp, url\_prefix=\\"\\"); app.register\_blueprint(compat\_blueprint)"  
* E-020 | Repo file | adapter/wsgi.py | create\_app | "app.register\_blueprint(reader\_bp); app.register\_blueprint(compat\_blueprint)"  
* E-040 | Repo file | tools/evidence/update\_evidence\_index.py, tools/evidence/orientation\_demo.py | constants and main | "HUMAN\_INDEX \= ROOT / \\"docs/evidence/INDEX.json\\" … MIRROR\_PATH \= ROOT / \\"artifacts/evidence\_index.jsonl\\""

# Engine Modules

## Sampler

* engine/sampler/core.py defines immutable ViewerProfile, CandidateFeatures, SamplerConfig, pool, and ranked-result structures. build\_candidate\_pool removes nonpositive weights and applies score, band, and diversity eligibility. E-015  
* \_compare\_entries and rank\_candidates order by descending weight, descending compatibility score, configured band priority, and canonical person-ID comparison. E-015  
* sample\_and\_rank performs pool formation followed by deterministic ranking. No random-selection function is present in this sampled module; the observed sampler selects by filtering and total ordering rather than a random draw. E-015  
* The dev CLI and internal HTTP harness both import sample\_and\_rank, proving direct callers. E-018, E-021

## Core compute

* engine/compat/compute.py:compat\_public normalizes the pair, derives a stable pair key, computes SHA-256-based category scores in CATEGORIES\_ORDER\_V1, assigns bands, and returns category records plus engine/release/invocation metadata. E-016  
* engine/compat/compute.py:conjunction\_public normalizes the left/right persons and embeds compat\_public in a conjunction envelope. conjunction\_public\_resolved additionally performs local lookup and resolver-mediated acquisition. E-016  
* engine/core/core.py:compute\_core returns a CoreResult with canonical pair and band ordering, symmetric neutral score, shared traits, alignment, and explicit directional perspective values. E-015  
* AB↔BA-neutral mechanics are explicit in normalize\_pair usage in compat and \_ordered\_pair in core. E-015, E-016  
* Canonicalization at the output boundary is handled by engine/serializer/canon.py:sercanon, delegating to engine.stable.sercanon.serialize for UTF-8, compact, sorted-key, one-final-LF bytes. E-017

## Determinism hazards in sampled engine paths

* engine/compat/compute.py:conjunction\_public\_resolved can invoke resolve\_bodygraph, which crosses local DB/vendor boundaries when the supplied local lookup misses. E-016  
* engine/bodygraph/vendor\_client.py imports socket, time, filesystem, and urllib.request; its HdApiClient is the observed network seam. E-028  
* engine/cli/main.py performs file reads and optional file writes; these are CLI boundary effects, not pure compute. E-018, E-026  
* No clock, unseeded randomness, network, or file-I/O hazard was observed in the sampled pure-compute modules engine/sampler/core.py and engine/core/core.py. Inspection method: complete-file static read. This is a sampled conclusion. E-015

Evidence anchors

* E-015 | Repo file | engine/sampler/core.py, engine/core/core.py | build\_candidate\_pool, rank\_candidates, compute\_core | "No randomness, clocks, or external state are consulted."  
* E-016 | Repo file | engine/compat/compute.py | compat\_public, conjunction\_public\_resolved | "a1,b1 \= normalize\_pair(a,b) … h \= hashlib.sha256(...)"  
* E-017 | Repo file | engine/serializer/canon.py, engine/presenter/emitter.py | sercanon, emit\_public | "UTF-8 bytes … keys sorted by default … exactly one trailing newline"  
* E-021 | Repo file | adapter/http\_reader.py | imports and dev\_sampler\_internal | "from engine.sampler.core import … sample\_and\_rank"  
* E-028 | Repo file | engine/bodygraph/vendor\_client.py | imports, HdApiClient | "from urllib import request as urlrequest"

# Adapter / HTTP Surfaces

adapter/wsgi.py:create\_app is the primary observed WSGI composition root; adapter/factory.py:create\_app is an alternate factory. Both mount the Reader blueprint without an added prefix and mount engine.http.compat\_handler:compat\_blueprint, whose constructor owns /api/compat/v1. E-019, E-020, E-023

| Mounted surface | Classification | Definition / handler |
| :---- | :---- | :---- |
| /reader GET/HEAD | Reader-like JSON success; dev-gated | adapter/http\_reader.py:get\_reader\_bp.reader\_v1 E-022 |
| /reader POST | Other observed surface; typed method error | reader\_v1\_post E-022 |
| /api/aux/narrative, /aux/narrative GET | Aux/narrative | aux\_narrative E-022 |
| /api/compat/v1 GET/POST/HEAD/OPTIONS | Admin/internal | engine/http/compat\_handler.py:get\_ids\_only, post\_json, transport handlers E-023 |
| /internal/healthz, /internal/readyz GET | Admin/internal | adapter/wsgi.py:internal\_healthz, internal\_readyz E-020 |
| /internal/version GET/HEAD | Admin/internal | module blueprint handlers in adapter/http\_reader.py E-024 |
| /ops/db/unavailable, /ops/rails/refusal, /ops/probe/env | Dev/diagnostic harness | corresponding ops\_\* handlers E-022 |
| /ops/writer/diagnostic POST/HEAD/OPTIONS | Dev/diagnostic harness | diagnostic writer handlers E-024 |
| /internal/dev/sampler POST | Dev/diagnostic harness | dev\_sampler\_internal E-021 |
| /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction GET | Dev/diagnostic harness | conjunction preview handlers E-024 |

## HTTP response hooks

* Reader GET computes an SHA-256 ETag and explicitly quotes it. Matching If-None-Match yields an empty 304; HEAD returns an empty body with GET-equivalent ETag and computed content length. E-022  
* Reader success sets Content-Type: application/json; charset=utf-8, Cache-Control: private, max-age=0, must-revalidate, and Vary: Authorization, Accept-Encoding. E-022  
* Aux narrative success emits text/plain; charset=utf-8, a quoted ETag, and private revalidation caching; suppressed output has no ETag and uses no-store. E-022  
* Compat writer responses use canonical JSON, no-store, explicit content length, and remove ETag and content encoding. HEAD returns 405 with Allow: POST, OPTIONS; OPTIONS returns 204\. E-023  
* WSGI common headers default JSON UTF-8, no-store, identity headers, and security headers. E-020

Evidence anchors

* E-022 | Repo file | adapter/http\_reader.py | reader\_v1, aux\_narrative, ops handlers | "etag \= \\"\\\\\\"\\" \+ \_sha256\_hex(body) \+ \\"\\\\\\"\\" … if etag in tokens … status=304"  
* E-023 | Repo file | engine/http/compat\_handler.py | blueprint and writer handlers | "Blueprint(\\"compat\\", \_\_name\_\_, url\_prefix=\\"/api/compat/v1\\")"  
* E-024 | Repo listing | exact route-decorator scan in adapter/http\_reader.py | "/internal/version … /ops/writer/diagnostic … /dev/reader/conjunction"

# Presenter / Emitter

* engine/presenter/emitter.py:emit\_public is the shared canonical public JSON emitter. It calls engine.serializer.canon.sercanon and returns LF-terminated canonical bytes; callers include HTTP Reader/compat code and CLI showcompat. E-017, E-018, E-022, E-023  
* presenter/reader\_v1/emitter.py:emit\_reader\_v1 constructs the Reader-v1 preimage, deduplicates and sorts categories by ID, hashes the preimage, inserts idempotence\_hash, and emits the final envelope through engine.presenter.emitter. E-025  
* engine/runtime exports emit\_reader\_public\_bytes and emit\_reader\_public\_envelope, used respectively by HTTP Reader and CLI showcompat. E-018, E-022  
* engine/cli/main.py:\_emit\_stdout\_bytes enforces exactly one LF posture by rejecting missing LF and CRLF before writing to sys.stdout.buffer. E-026  
* presenter/json\_canon\_compare.py is an argparse comparison utility rather than an HTTP/CLI response presenter. E-014

Evidence anchors

* E-025 | Repo file | presenter/reader\_v1/emitter.py | emit\_reader\_v1 | "digest \= hashlib.sha256(pre\_bytes).hexdigest() … final\[\\"idempotence\_hash\\"\] \= digest"  
* E-026 | Repo file | engine/cli/main.py | \_emit\_stdout\_bytes | "if not payload.endswith(b\\"\\\\n\\"): raise CliError(\\"STDOUT\_MISSING\_LF\\")"

# CLI Surfaces

* Packaging registers hdctl to engine.cli.main:cli. The parser requires a subcommand. E-011, E-018  
* hdctl showcompat accepts pair-file, A/B files, stdin, DB/vendor/auto source selection, conjunction mode, viewer preferences, user IDs, and birth arguments. The parser does not mark these individual showcompat inputs required=True; handler-level validation emits typed errors such as MISSING\_PARTY\_FILE, MISSING\_DB\_USER, or AUTO\_SOURCE\_UNRESOLVED. E-018, E-027  
* Normal showcompat flows through input normalization, canonical pair ordering, chart feature computation, compat\_public, emitter.emit\_public, and \_emit\_stdout\_bytes. E-027  
* \--dump-reader writes canonical Reader bytes to the requested path. \--dump-admin-dir creates parent directories and writes admin JSON plus sidecars through canon\_dump. Normal output is written to stdout. E-026, E-027  
* Conjunction showcompat calls conjunction\_public\_resolved, emits canonical JSON to stdout, and rejects Reader/admin dumps for that mode. E-027  
* hdctl aux-preview accepts direct category/band/perspective inputs or a pair file, writes narrative text to stdout when selected, and can write an IDs-only admin sidecar. E-018  
* hdctl bg:resolve requires \--user at parser level and supports auto, db, and vendor, plus upsert/dry-run and birth inputs. E-018  
* hdctl dev:sampler requires \--viewer and \--candidates-file; it reads candidates from that file, calls sample\_and\_rank, and writes canonical JSON to stdout. E-018  
* cli prints typed CliError.code values to stderr and returns the error’s nonzero exit code; argparse itself supplies nonzero usage behavior for parser-required omissions. E-027

Evidence anchors

* E-027 | Repo file | engine/cli/main.py | showcompat, cli | "except CliError as err: sys.stderr.write(f\\"{err.code}\\\\n\\")"

# Vendor Seam & BodyGraph Storage

## Vendor client

* engine/bodygraph/vendor\_client.py contains HdApiClient, VendorRequest, VendorResult, retry/timeout profiles, governed route contracts, request shaping, authentication posture, response handling, and urllib-based HTTP transport. E-028  
* Governed resource paths observed are bodygraphs, bodygraphs/simple, charts, charts/simple, and charts/coordinates. Legacy BodyGraph routes use HD-Api-Key; chart routes use bearer authentication. E-028  
* The vendor configuration surface inspected in the client/resolver includes SAFE\_MODE, ALLOW\_NETWORK, HD\_API\_BASE\_URL, compatibility HDAPI\_BASE\_URL, HD\_API\_KEY, and geocode-related configuration. Only names are reported; no environment values were inspected. E-028, E-029  
* classify\_bg\_resolve\_route\_policy maps configured v2 bases to charts/ChartResult and other bases to legacy bodygraphs/BodyGraph. E-028

## Persistence and cache

* engine/db/adapter.py:DBAccess is a direct PostgreSQL façade. for\_current\_env uses DATABASE\_URL, constructs PsycopgProvider, performs health selection, and rejects the presence of retired bridge keys before reading a DSN. E-030  
* The explicitly rejected keys are DB\_ALLOW\_BRIDGE\_IN\_PROD, DB\_BRIDGE\_URL, and DB\_FORCE\_BRIDGE. E-030  
* engine/bodygraph/ingest.py persists to hde.body\_graphs with identity fields (user\_id, vendor, vendor\_version, input\_fingerprint) and ON CONFLICT DO NOTHING; it also reads/counts the same identity. E-031  
* engine/bodygraph/mapped\_cache.py:persist\_mapped\_bodygraph accepts only an exact mapped-cache metadata shape, projects the BodyGraph, canonicalizes it, inserts with the same four-column identity, reads it back, and checks canonical parity and idempotence. E-032  
* The visible cache key is therefore the SQL identity tuple (normalized\_user\_id, "hdapi", vendor\_version, fingerprint). E-032  
* conjunction\_public\_resolved tries a caller-provided local lookup first, calls resolve\_bodygraph after a miss, and attempts local lookup again after successful acquisition. E-016

## Offline/vendor-required posture

* Vendor acquisition is closed by default unless both SAFE\_MODE=0 and ALLOW\_NETWORK=1; the vendor client classifies all other combinations as closed\_default. E-028  
* The HTTP conjunction surfaces and CLI pass the rail environment into resolver-mediated acquisition; resolver failure is converted to typed vendor/CLI or writer errors. E-016, E-022, E-027  
* CI defines both closed-rail refusal and fixture-backed, non-live open-rail conformance jobs. E-042

Evidence anchors

* E-029 | Repo file | engine/bodygraph/resolver.py and engine/bodygraph/ingest.py | resolver/ingest configuration paths | "source=\\"vendor\\" … env=resolver\_env"  
* E-030 | Repo file | engine/db/adapter.py | RETIRED\_DB\_TRANSPORT\_KEYS, DBAccess.for\_current\_env | "dsn \= (env.get(\\"DATABASE\_URL\\") or \\"\\").strip()"  
* E-031 | Repo file | engine/bodygraph/ingest.py | \_persist\_bodygraph, \_row\_count, \_fetch\_payload | "INSERT INTO hde.body\_graphs … ON CONFLICT DO NOTHING"  
* E-032 | Repo file | engine/bodygraph/mapped\_cache.py | persist\_mapped\_bodygraph | "identity \= (normalized\_user\_id, \_EXPECTED\_VENDOR, vendor\_version, fingerprint)"

# Evidence, Indices, Catalogs

## Evidence homes

The tracked evidence-like homes were exhaustively counted and grouped by their first two path components. E-038

* docs/ — 151 tracked files. Observed subhomes include acceptance, adr, architecture, changes, contracts, crd, design, evidence, ops, pfcanon, plans, qa, run, schemas, and server. File patterns include Markdown, JSON, text, SHA-256 sentinels, and schemas. Classification: mixed, because prose/configuration coexist with generated index/hash artifacts and generator wiring. E-038, E-039, E-040  
* artifacts/ — 1,022 tracked files. Observed subhomes include admin, architecture, audit, BodyGraph, canonical, CLI, compat, config bundles, core, DB, engine, environment, errors, headers, identity, ingest, narratives, ops, presenter, proofs, QA, Reader, registry, runtime, sampler, sanity, serializer, showcompat, thresholds, vendor, and writer. Dominant formats are .txt, .json, .log, .sha256, bodies, JSONL, bytes, diffs, SQL, CSV, and YAML. Classification: generated/captured, supported by path proofs, hashes, generator names, and index records. E-038  
* audit/ — 3,015 tracked files. Subhomes include bootstrap, codex, db\_plan, docdeltas, documentation snapshots, gates, ops, pf09\_recheck, preflight, and qa; audit/qa alone accounts for 2,383 tracked files. Formats include text, logs, Markdown, JSON, hashes, stderr/stdout captures, scripts, headers, bodies, diffs, and NDJSON. Classification: mixed captured/governed, supported by QA harnesses, gate producers, reports, and retained scripts. E-038  
* Other observed evidence-like homes are proofs/, goldens/, freeze/, reports/, scan\_reports/, catalog/, schemas/, and selected tests/transport/headers/ snapshots. Their names alone are not used to assign authority; their role is supported where tests, packaging, or index records reference them. E-009, E-039, E-041

## Evidence indices

* docs/evidence/INDEX.json is a JSON array of artifact records containing at least artifact\_key and discovered\_physical\_path, with some records carrying epic IDs, notes, schemas, tokens, and other metadata. E-039  
* docs/evidence/INDEX.sha256 contains the SHA-256 binding for docs/evidence/INDEX.json. E-039  
* artifacts/evidence\_index.jsonl is the machine mirror: one JSON record per line, including artifact path, role/schema metadata, hashes, byte size, proof anchor, and tokens where applicable. E-039  
* tools/evidence/update\_evidence\_index.py owns the human index, sentinel, mirror, mirror hash, and proof refresh/check logic. orientation\_demo.py reads the mirror and compares paths, hashes, and sizes. ci/checks/check\_mirror\_schema.sh validates mirror structure and self-proof fields. E-040

## Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json has top-level endpoints, generated\_at\_utc, and success\_endpoints. Endpoint entries include method, path, blueprint module, classification, environment gate, internal/A7 flags, description, and rail profile. E-039  
* Its observed entries cover /reader, /api/compat/v1, internal version, internal sampler, and conjunction dev routes. A mirror exists at artifacts/audit/ENDPOINTS\_CATALOG.json with path-proof siblings. E-039  
* tests/http/test\_endpoint\_catalog.py is the directly observed test locus for this catalog. E-041

## Proof and snapshot artifacts

Observed indexed or proof-bearing families include:

* artifacts/proofs/success\_get.txt, success\_head.txt, success\_304.txt, reader\_success\_get\_head\_304.json, and their path proofs.  
* artifacts/audit/a7/get\_headers.txt, head\_headers.txt, get\_304\_headers.txt, Reader bodies, and CLI parity captures.  
* artifacts/cli/showcompat/stdout.json, SHA-256 and path-proof siblings.  
* artifacts/bodygraph/source\_selection.snapshot.json, refresh/metrics snapshots, and configured-v2 mapped-cache transcripts.  
* artifacts/core/abba/ab\_ba\_parity.json, sampler ABBA/two-run/pool snapshots, runtime DB-selection snapshots, and vendor HDAPI-v2 proof families.  
* Producers are visible in tools/evidence/generate\_a7\_transport\_proofs.py, tools/cli/generate\_showcompat\_artifacts.py, tools/evidence/generate\_bodygraph\_policy\_proofs.py, generate\_engine\_core\_evidence.py, generate\_sampler\_evidence.py, and related generator files. E-043

Evidence anchors

* E-039 | Repo file/listing | index/catalog reads and proof-path listing | "docs/evidence/INDEX.json … artifacts/evidence\_index.jsonl … docs/ENDPOINTS\_CATALOG.json"  
* E-041 | Repo listing | complete tests/ directory list and relevant tracked test selection | "tests/http/test\_endpoint\_catalog.py … tests/compliance/test\_reader\_etag\_and\_conditional.py"

# Tests, QA Harness, CI/Checks

## Tests

The complete directory listing under tests/ contains root-level suites and subtrees including \_helpers, adapter/adapters, arch, artifacts, audit, BodyGraph, canon, categories, CLI, compare, compat, compliance, config, core, DB, evidence, fixtures, goldens, hdctl, HTTP, identity, infra, integration, invariance, ops, order, provider, QA, Reader-v1, runtime, scripts, support, tools, transport, and unit. E-041  
Classification follows repository labels only:

* tests/unit/ — unit, by directory label.  
* tests/integration/ — integration, by directory label.  
* Contract-oriented files such as tests/http/test\_compat\_endpoint\_contract.py and tests/db/test\_adapter\_contract.py — contract, by filename.  
* Other suites — Uncategorized where configuration does not label them unit/integration/contract.

Key loci:

* Reader and HTTP: tests/http/test\_reader\_a7\_transport.py, tests/compliance/test\_reader\_etag\_and\_conditional.py, tests/adapter/test\_reader\_parity.py, tests/reader\_v1/test\_emitter.py. They cover transport parity, conditional responses, shared bytes, and Reader emission. E-041  
* Compat: tests/http/test\_compat\_endpoint\_contract.py, tests/adapter/test\_compat\_http\_dev.py, tests/compat/test\_compat\_public\_ab\_ba\_identity.py. They cover endpoint behavior and AB/BA identity. E-041  
* CLI: tests/cli/test\_cli\_canonical\_bytes.py, test\_cli\_usage\_and\_errors.py, test\_showcompat\_parity\_and\_identity.py, and tests/hdctl/test\_cli\_streams\_and\_exits.py. They cover canonical bytes, argument/error behavior, streams, exits, and parity. E-041  
* Determinism/canonical JSON: tests/core/test\_engine\_core\_determinism.py, tests/canon/test\_report\_determinism.py, tests/infra/test\_sercanon\_bytes.py, tests/invariance/test\_determinism\_env\_helper.py. E-041  
* Vendor/BodyGraph/DB: tests/bodygraph/test\_vendor\_client.py, test\_resolver\_vendor.py, test\_ingest.py, test\_v2\_mapped\_cache.py, and tests/db/test\_adapter\_selection.py. These include fixture/mocked vendor paths as evidenced by the reusable CI job labels. E-041, E-042  
* Evidence/index/catalog: tests/evidence/test\_evidence\_index\_\*, test\_machine\_mirror\_self\_proof.py, test\_orientation\_demo.py, test\_sanity\_pipeline.py, and tests/http/test\_endpoint\_catalog.py. E-041

## CI

* .github/workflows/ci.yml, workflow name ci, pins LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, and ALLOW\_NETWORK=0. It performs pytest readiness, environment-pin checks, selected pytest suites, ordering/CLI/DB/rails checks, evidence-index checks, mirror/hash/final-LF validation, and release-manifest/attestation checks. E-042  
* .github/workflows/epic-closeout-validation.yml, workflow name epic-closeout-validation, has job validate-closeout-candidate and invokes close-pack generation followed by evidence index, orientation, hash, path, mirror, and final-LF checks. E-042  
* Reusable job definitions are:  
  * ci/jobs/rails\_closed\_refusal.yml — rails\_closed\_refusal, closed rails, live vendor calls forbidden.  
  * ci/jobs/rails\_open\_conformance.yml — rails\_open\_conformance, open-rail variables but fixture-backed/mocked and live calls forbidden.  
  * ci/jobs/logs\_keys\_only\_redaction.yml — logs\_keys\_only\_redaction, closed rails and keys-only redaction evidence. E-042

## QA-relevant scripts

Observed families include:

* Environment, evidence integrity, and release checks under ci/checks/: check\_env\_pins.sh, check\_evidence\_index\_hash.sh, check\_mirror\_schema.sh, check\_final\_lf.sh, check\_direct\_db\_contract.py, check\_release\_identity.sh.  
* Canonical/evidence producers and validators under tools/evidence/: index update, orientation, sanity, canonical JSON, A7 transport, BodyGraph policy, DB posture, deterministic core/sampler, HDAPI-v2, mapped-cache, and release-binding families.  
* CLI producers under tools/cli/: CLI conformance and showcompat artifact/parity generators.  
* QA close-pack/harness code under tools/qa/.  
* Runtime/job scripts under scripts/bodygraph/, scripts/db/, and scripts/ingest/. E-043

Evidence anchors

* E-042 | Repo file/listing | .github/workflows/\*.yml, ci/jobs/\*.yml | "name: ci … SAFE\_MODE: \\"1\\" … ALLOW\_NETWORK: \\"0\\""  
* E-043 | Repo listing | QA-relevant check\_\*, run\_\*, and generate\_\* families | "tools/evidence/run\_sanity\_pipeline.py … tools/evidence/update\_evidence\_index.py"

# Flows & Call Chains

## Reader success flow over HTTP — Found

Chain: adapter/wsgi.py:create\_app → adapter/http\_reader.py:get\_reader\_bp.reader\_v1 → engine.runtime:emit\_reader\_public\_bytes → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine/presenter/emitter.py:emit\_public → Flask Response. E-020, E-022, E-025, E-017

* The blueprint is mounted without an additional prefix.  
* GET requires v=1, dev environment, A/B chart paths, and timezone information.  
* Charts are loaded at the adapter boundary.  
* Runtime emission returns canonical Reader bytes.  
* The handler creates a quoted SHA-256 ETag.  
* GET returns the bytes; HEAD returns no body with computed content length; a matching conditional request returns 304\. E-022

## Compat API flow over HTTP — Found

Chain: adapter/wsgi.py:create\_app → engine/http/compat\_handler.py:post\_json → engine.validation.viewer\_prefs:validate\_viewer\_prefs/normalize\_viewer\_prefs → engine.compat.compute:compat\_public → engine.presenter:emit\_public → \_writer\_payload → Flask Response. E-020, E-023, E-016, E-017

* Blueprint prefix is /api/compat/v1.  
* The route accepts complete A/B payloads or paired IDs, but rejects mixed modes.  
* Viewer preferences are validated and normalized.  
* compat\_public normalizes A/B before scoring.  
* \_writer\_payload emits canonical JSON, sets no-store, and removes ETag.  
* Production mode is guarded before the handler. E-023

## CLI showcompat or compat-preview flow — Found

Chain: pyproject.toml:hdctl → engine/cli/main.py:cli → showcompat → engine.compat.ordering:normalize\_pair → engine.compat.compute:compat\_public → engine.presenter.emitter:emit\_public → \_emit\_stdout\_bytes → stdout. E-011, E-018, E-027, E-016, E-026

* The parser requires the showcompat subcommand but permits several mutually interpreted input modes.  
* Source modes can read files/stdin, DB, vendor, or auto.  
* Input people and charts are placed in canonical order.  
* Compatibility categories are computed from the normalized pair.  
* Canonical bytes are checked for LF/CRLF posture before stdout.  
* Optional Reader and admin dumps write only when their flags are supplied. E-026, E-027

## Vendor acquisition or BodyGraph-ingest flow — Found

Chain: engine/cli/main.py:bg\_resolve/showcompat or engine.compat.compute:conjunction\_public\_resolved → engine/bodygraph/resolver.py:resolve\_bodygraph → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient → engine/db/adapter.py:DBAccess / engine/bodygraph/mapped\_cache.py:persist\_mapped\_bodygraph → hde.body\_graphs. E-027, E-016, E-028, E-030, E-031, E-032

* Local lookup precedes resolver acquisition in conjunction processing.  
* Network acquisition requires both rail variables to be open.  
* Request route/auth posture is selected from governed route contracts.  
* The vendor response is parsed into a vendor result.  
* Legacy ingest and configured-v2 mapped cache both use PostgreSQL storage paths, with mapped cache projecting before persistence.  
* DB access is direct psycopg and rejects retired bridge-key presence. E-028, E-030, E-032

## Evidence-index update or validation flow — Found

Chain: .github/workflows/ci.yml → tools/evidence/update\_evidence\_index.py:main \--check → docs/evidence/INDEX.json / docs/evidence/INDEX.sha256 / artifacts/evidence\_index.jsonl → tools/evidence/orientation\_demo.py:main \--check → ci/checks/check\_evidence\_index\_hash.sh → tools/evidence/validate\_evidence\_paths.py → ci/checks/check\_mirror\_schema.sh. E-042, E-040

* CI invokes the index updater in check mode.  
* The updater binds the human index, sentinel, mirror, mirror SHA, and proofs.  
* Orientation reads mirror records and compares path/hash/size information.  
* Dedicated checks validate the index hash, evidence paths, mirror schema, and final LF.  
* The closeout workflow invokes the same validation family after its close-pack generator. E-040, E-042

# Drift and Reality vs Expectations

| ID | Category | Observed fact | Expected comparison point | Classification | Impact |
| :---- | :---- | :---- | :---- | :---- | :---- |
| F-001 | Directory/architecture drift | engine/, adapter/, and root presenter/ all exist, but presenter code also exists under engine/presenter/. | Separate engine, adapter, and presenter families. | Partial | Callers use engine.presenter.emitter as the shared canonical emitter, while root presenter/reader\_v1 builds the Reader envelope. E-017, E-025 |
| F-002 | Surface drift | HTTP Reader mounting and request handling live in adapter/http\_reader.py, while compat route registration lives in engine/http/compat\_handler.py. | HTTP adapter separated from engine compute. | Partial | The engine package contains a Flask blueprint and imports Flask request/response types. E-023 |
| F-003 | Surface drift | CLI is packaged inside engine/cli/ and calls engine compute, BodyGraph, DB, runtime, narrative, and presenter modules. | Distinct CLI family. | Aligned | hdctl has one registered package entrypoint and typed subcommand dispatch. E-011, E-018 |
| F-004 | Evidence drift | Evidence is distributed across docs/, artifacts/, audit/, and additional proof/golden/catalog/schema homes, with a human index and machine mirror binding many paths. | Evidence family. | Partial | Consumers must traverse both index files and multiple physical roots; the updater and mirror checks encode those paths. E-038, E-040 |
| F-005 | Determinism drift | Pure sampler/core modules use explicit sorting and no clocks/randomness, while resolver/vendor/CLI boundaries perform DB, network, and file operations behind explicit controls. | Deterministic engine behavior with effects at seams. | Aligned | Pure compute is input-derived; acquisition and persistence occur in separate observed boundary modules. E-015, E-028, E-030 |
| F-006 | Vendor seam drift | Vendor transport is under engine/bodygraph/vendor\_client.py; additional provider packages also exist under engine/provider/ and engine/providers/. | Vendor family. | Partial | The audited BodyGraph flow resolves through the BodyGraph-specific client rather than a top-level vendor/ directory. E-010, E-028 |
| F-007 | Directory/architecture drift | DB access is under engine/db/, with a compatibility façade at adapter/db\_access.py and SQL persistence in BodyGraph modules. | DB family. | Partial | Direct callers import engine.db.DBAccess; persistence identity and SQL remain in BodyGraph modules. E-010, E-030, E-032 |
| F-008 | Path-case drift | Observed expected-family paths use lowercase exact names: engine/, adapter/, presenter/, docs/, artifacts/, audit/, tools/, ci/, tests/, scripts/. | Prompt path spellings. | Aligned | No case translation is needed for these observed roots. E-009 |
| F-009 | Root proliferation | Seven observed truth-bearing/producer roots: docs/, artifacts/, audit/, catalog/, proofs/, tools/, scripts/. | Root-count comparison only. | Partial | Impact: Not established from Repo evidence. E-009, E-038, E-043 |
| F-010 | Evidence drift | Canonical endpoint catalog exists in docs/ with an audit mirror under artifacts/audit/; evidence index likewise has human and machine forms. | Cataloged evidence layout. | Aligned | Tests and CI have explicit catalog/index validation loci. E-039, E-041, E-042 |

# Negative-Claim Proof Appendix

No negative claims made.

