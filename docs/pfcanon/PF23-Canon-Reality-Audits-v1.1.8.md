# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.8

**Status:** Canon

**Effective date:** 2026-07-24

**Last Update Gate:** HDE-EPIC038

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

**Date:** 2026-07-24

# Audit Snapshot Metadata

* Repository root: /workspace/glow-hdengine-v2; the current directory and Git top level resolved to the same path. E-001  
* Commit: e9422f0a16d3cb689e18e993e809a96dd14899e8. E-001  
* Branch: work. E-001  
* Working tree: clean; git status \--porcelain returned no changed paths. E-001  
* Audit timestamp: 2026-07-24T21:43:53Z. E-001  
* Kernel/OS: Linux 6.12.13 x86\_64 GNU/Linux. E-001  
* Python: Python 3.14.4. E-001  
* Node: v24.15.0. E-001  
* This was a static, read-only inspection. No application code, tests, generators, setup scripts, or package installers were executed.

Evidence anchors

* E-001 | Repo state | pwd; git rev-parse \--show-toplevel; git rev-parse HEAD; git status \--porcelain; git rev-parse \--abbrev-ref HEAD; date \-u; uname \-srmo; python \--version; node \--version | "/workspace/glow-hdengine-v2 … e9422f0a16d3cb689e18e993e809a96dd14899e8 … work … 2026-07-24T21:43:53Z … Linux 6.12.13 x86\_64 GNU/Linux … Python 3.14.4 … v24.15.0"

# Top-level Repo Map

## Complete root listing

The complete one-level listing contained the following directories and files. E-002

### Top-level directories

| Exact root | State | Observed contents or role | Representative anchors |
| :---- | :---- | :---- | :---- |
| .audit\_src/ | Present | A 485-file retained source/audit tree with its own tests and requirements; separate from the active tests/ tree. | .audit\_src/tests/, .audit\_src/requirements-dev.txt |
| .backup\_epic004/ | Present | EPIC004-named backup material. No runtime import or registration was established in the sampled runtime paths. | .backup\_epic004/ |
| .devcontainer/ | Present | Development-container configuration. | .devcontainer/ |
| .git/ | Present | Git metadata tying the working directory to the audited repository. | .git/ |
| .github/ | Present | GitHub CI workflow home. | .github/workflows/ci.yml |
| .vscode/ | Present | Editor/workspace configuration. | .vscode/ |
| \_arch/, \_archive/ | Present | Archive-named roots. No active runtime wiring was established in the sampled entrypoints. | \_arch/, \_archive/ |
| adapter/ | Present | Flask application factories, Reader blueprint, HTTP guards, headers, DB access compatibility modules, and HTTP schemas. | adapter/http\_reader.py, adapter/wsgi.py, adapter/schemas/ |
| artifacts/ | Present | 1,020 checked-in evidence, proof, snapshot, capture, bundle, and mirror files distributed across many subfamilies. | artifacts/evidence\_index.jsonl, artifacts/vendor/hdapi\_v2/, artifacts/cli/showcompat/ |
| assert/ | Present | Assertion-named root; its contents were not used for a runtime claim. | assert/ |
| audit/ | Present | 2,927 checked-in QA, OPS, gate, manifest, close-report, and documentation-capture files. | audit/qa/, audit/gates/, audit/ops/ |
| catalog/ | Present | Packaged JSON catalog and release manifest material. | catalog/manifest.json |
| ci/ | Present | Shell/Python checks plus declarative rail-job definitions. | ci/checks/, ci/jobs/ |
| codex/ | Present | Codex-named repository material; not used as an active runtime source in this audit. | codex/ |
| config/ | Present | Configuration-root material alongside engine/config/. | config/ |
| dev/ | Present | Development-only material. Active dev HTTP handlers themselves are registered from adapter/http\_reader.py. | dev/, adapter/http\_reader.py |
| docs/ | Present | 143 documentation, schema, acceptance, endpoint-catalog, PF-canon, and evidence-index files. | docs/evidence/INDEX.json, docs/ENDPOINTS\_CATALOG.json, docs/pfcanon/ |
| engine/ | Present | Main Python engine package: compatibility, sampler, BodyGraph, DB, CLI, provider, presenter, serializer, runtime, and narratives. | engine/compat/, engine/sampler/, engine/bodygraph/ |
| errors/ | Present | Error-related root material distinct from engine/errors/ and engine/compat/errors.py. | errors/ |
| fixtures/ | Present | Test/runtime fixture data. | fixtures/ |
| freeze/ | Present | One-file freeze-related root. | freeze/ |
| goldens/ | Present | Fourteen golden-reference files. | goldens/ |
| handoff/ | Present | Handoff documentation/material. | handoff/ |
| import/ | Present | Import-named root; no active package wiring was established. | import/ |
| internal/ | Present | Checked-in internal endpoint response examples, particularly readiness captures. | internal/readyz/ |
| math/ | Present | Packaged JSON-bearing Python/package family included by setuptools. | math/, pyproject.toml |
| migrations/ | Present | Database migration material. | migrations/ |
| narratives/ | Present | Hash-addressed narrative-pack JSON and SHA-256 sidecars. | narratives/64e17c9c…/manifest.json, templates.json |
| notes/ | Present | Notes material. | notes/ |
| parity/ | Present | Parity-related checked-in material. | parity/ |
| presenter/ | Present | Top-level Reader presenter and canonical-JSON comparison CLI. | presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py |
| proofs/ | Present | Six proof files outside artifacts/. | proofs/ |
| release/ | Present | Release-related material. | release/ |
| reports/, scan\_reports/ | Present | Two files in each report home. | reports/, scan\_reports/ |
| schemas/ | Present | Root-level schemas, in addition to docs/schemas/ and adapter/schemas/. | schemas/ |
| scripts/ | Present | Release, BodyGraph worker, DB retention, schema, and ingest entrypoints. | scripts/bodygraph/run\_refresh\_worker.py, scripts/ingest/run\_vendor\_ingest.py |
| sql/ | Present | SQL source material used alongside migrations and engine/db/. | sql/ |
| tests/ | Present | Active pytest tree spanning HTTP, CLI, compatibility, DB, BodyGraph, determinism, evidence, and QA. | tests/reader\_v1/, tests/evidence/, tests/db/ |
| tools/ | Present | Evidence producers/checkers, QA harnesses, CLI guards, config generators, and report generators. | tools/evidence/, tools/qa/, tools/cli/ |
| validation/ | Present | Validation-related root material. | validation/ |

### Material root files

| Root file(s) | State and observed role |
| :---- | :---- |
| AGENTS.md | Present; repository operating and evidence rules. |
| pyproject.toml | Present; setuptools build metadata, package discovery, and hdctl console script. |
| requirements.txt, requirements-dev.txt | Present; runtime and test dependency declarations. |
| pytest.ini | Present; pytest configuration anchor. |
| Procfile, run\_flask.py, run\_flask\_dev.sh, Run | Present; server/process or development startup material. |
| README.md, ARCHITECTURE.md, CHANGELOG.md, AcceptanceMap.md, FLASK\_AUTO\_RUN\_GUIDE.md | Present; repository-facing documentation. |
| .env.example | Present; environment configuration example. |
| .github/workflows/ci.yml | Present under .github/; active CI configuration. |
| VERIFY.sh, card\_close.sh, run\_d3\_2\_complete.sh, run\_d3\_2\_validation\_complete.sh | Present; verification/close or QA shell entrypoints. |
| CANON\_CHECKSUMS.json, manifest\_pre.sha256, manifest\_post.sha256 | Present; checksum-bearing root artifacts. |
| LICENSE, .gitignore, .gitattributes | Present; repository/legal configuration. |
| Root EPIC reports and \*\_step\_report.md files | Present; point-in-time report/evidence material at repository root. |
| .body200.json, .code304.txt, .tmp\_refusal\_get.txt, .tmp\_refusal\_post.txt, big.json, code304\_new.txt, temp\_run.\*, changes\_report.txt, patch.diff | Present; root-level captures or working artifacts. |
| \_backup\_1761350008.tgz, \_backup\_corrupted\_1761349750.tgz, \_backup\_corrupted\_1761349780.tgz | Present; backup archives. |

Expected-family classification

| Comparison family | Classification | Direct evidence |
| :---- | :---- | :---- |
| engine/ | Present | Main package includes compat, sampler, bodygraph, db, cli, presenter, and runtime modules. E-003 |
| adapter/ | Present | Flask app and Reader wiring reside here. E-003, E-005 |
| presenter/ | Present | Top-level Reader presenter exists; an additional engine/presenter/ package also exists. E-003, E-010 |
| CLI package | Present | engine/cli/; packaged as hdctl. E-004, E-008 |
| docs/ | Present | Documentation, schemas, catalog, PF-canon, and index. E-013 |
| artifacts/ | Present | Evidence mirror and broad artifact families. E-012, E-013 |
| audit/ | Present | QA/OPS/gate evidence families. E-013 |
| tools/ | Present | Evidence and QA producers/checkers. E-014 |
| ci/ or workflows | Present | Both ci/ and .github/workflows/ci.yml. E-014, E-015 |
| tests/ | Present | Active pytest tree. E-014 |
| scripts/ | Present | Worker, retention, ingest, release scripts. E-014 |

Truth-bearing or governed-output roots observed: 12 — .audit\_src/, artifacts/, audit/, catalog/, docs/, freeze/, goldens/, narratives/, proofs/, reports/, scan\_reports/, and root-level checksum/report/capture files. This is a path/count observation, not an authority judgment. E-002, E-012, E-013  
Evidence anchors

* E-002 | Repo listing | find . \-mindepth 1 \-maxdepth 1 \-printf '%f\\t%y\\n' \\| sort | "adapter d; artifacts d; audit d; catalog d; ci d; docs d; engine d; presenter d; scripts d; tests d; tools d; pyproject.toml f; requirements.txt f; requirements-dev.txt f; …"  
* E-003 | Repo listing | find engine adapter presenter internal narratives \-type f \\| sort | "adapter/http\_reader.py; engine/bodygraph/vendor\_client.py; engine/cli/main.py; engine/compat/compute.py; engine/db/adapter.py; engine/presenter/emitter.py; engine/sampler/core.py; presenter/reader\_v1/emitter.py; …"

# Packaging and Entrypoints

## Packaging and build configuration

* pyproject.toml declares project glow-hdengine, version 0.0.0, Python \>=3.10, and setuptools package discovery for engine\*, adapter\*, presenter\*, catalog\*, and math\*. It declares hdctl \= "engine.cli.main:cli". Its PEP 621 dependencies array is empty. E-004  
* requirements.txt separately declares psycopg\[binary\]\>=3.1,\<3.3, Flask\>=2.3,\<3.0, and gunicorn\>=21,\<22. E-004  
* requirements-dev.txt declares jsonschema, pytest, pytest-cov, and pytest-mock. E-004  
* pytest.ini is present as the root pytest configuration anchor. E-002  
* No setup.py, setup.cfg, package.json, or workspace manifest was observed in the complete depth-two packaging-file listing. NCP-001

## HTTP entrypoints

* adapter/wsgi.py:create\_app constructs the principal WSGI Flask application, installs logging and environment validation, mounts reader\_bp without an added prefix and mounts compat\_blueprint, and defines /internal/healthz and /internal/readyz. Module-level app \= create\_app() exposes the WSGI object. E-005  
* adapter/http\_reader.py:create\_app is another app factory mounting the same Reader blueprint and compatibility blueprint; its module-level app and \_\_main\_\_ runner provide an additional startup path. E-006  
* adapter/factory.py:create\_app is a narrower development factory mounting only the Reader blueprint and stripping ETags from /internal/ responses. run\_flask.py imports this factory and invokes app.run(...). E-005  
* Procfile is present as process-launch configuration, while the inspected WSGI module exposes adapter.wsgi:app. E-002, E-005

## CLI and scheduled/background entrypoints

* The installed CLI entrypoint is hdctl → engine.cli.main:cli; engine/cli/\_\_main\_\_.py also supplies module execution. E-004, E-008  
* Relevant subcommands registered by \_build\_parser are showcompat, aux-preview, bg:resolve, and dev:sampler. E-008  
* scripts/bodygraph/run\_refresh\_worker.py is the discovered BodyGraph refresh-worker entrypoint; scripts/db/run\_retention\_job.py is a retention-job entrypoint; scripts/ingest/run\_vendor\_ingest.py is a vendor-ingest entrypoint. E-014  
* Evidence/index jobs are directly invokable Python CLIs rather than an observed in-process scheduler: tools/evidence/update\_evidence\_index.py, orientation\_demo.py, run\_sanity\_pipeline.py, and related generators. CI invokes index and orientation checks. E-012, E-015

Evidence anchors

* E-004 | Repo file | pyproject.toml and requirements files | project/build tables | "name \= \\"glow-hdengine\\" … hdctl \= \\"engine.cli.main:cli\\" … include \= \[\\"engine\*\\", \\"adapter\*\\", \\"presenter\*\\", \\"catalog\*\\", \\"math\*\\"\]"; "psycopg\[binary\]… Flask… gunicorn…"; "pytest… jsonschema…"  
* E-005 | Repo file | adapter/wsgi.py, adapter/factory.py, run\_flask.py | create\_app, module app, \_\_main\_\_ | "app.register\_blueprint(reader\_bp)"; "app.register\_blueprint(compat\_blueprint)"; "app \= create\_app()"; "app.run(host=host, port=port, debug=debug, …)"  
* E-006 | Repo file | adapter/http\_reader.py | create\_app, module app, \_\_main\_\_ | "app.register\_blueprint(bp, url\_prefix=\\"\\")"; "app.register\_blueprint(compat\_blueprint)"; "app \= create\_app()"; "create\_app().run(host=\\"0.0.0.0\\", …)"

# Engine Modules

## Engine-role packages

The primary engine role is implemented beneath engine/, with compatibility computation under engine/compat/, sampling under engine/sampler/, BodyGraph acquisition/storage under engine/bodygraph/, and DB access under engine/db/. E-003

## Sampler

* engine/sampler/core.py:build\_candidate\_pool forms a candidate pool by excluding non-positive weights, resolving bands, and applying compatibility-score, allowed/excluded-band, and diversity-key eligibility rules. E-007  
* engine/sampler/core.py:rank\_candidates establishes a total order using descending weight, descending compatibility score, configured band priority, and canonical ID comparison. E-007  
* engine/sampler/core.py:sample\_and\_rank composes pool formation and ranking. E-007  
* No random-selection operation is present in this sampled module: the observed “sample” operation is deterministic ranking, and its docstring states that no randomness, clocks, or external state are consulted. This is a sampled conclusion for engine/sampler/core.py, not a repository-wide absence claim. E-007

## Core compatibility compute

* engine/compat/compute.py:compat\_public normalizes the pair, hashes pair\_key:category, calculates scores and bands in CATEGORIES\_ORDER\_V1, and returns categories plus engine/release/invocation metadata. E-007  
* engine/compat/ordering.py:normalize\_pair orders parties by validated person\_uid and uses a stable payload-hash tie-break when IDs match; pair\_key applies that normalization. This is the direct AB↔BA symmetry mechanism. E-007  
* engine/compat/compute.py:conjunction\_public and conjunction\_public\_resolved wrap compatibility output in a conjunction result and, for unresolved users, attempt local lookup before resolver acquisition. E-007  
* Boundary canonicalization is split: pair canonicalization is in engine/compat/ordering.py; JSON byte canonicalization is in engine/serializer/canon.py and engine/stable/sercanon.py. E-007, E-010

## Determinism hazards in sampled engine paths

* engine/bodygraph/vendor\_client.py contains network I/O, retry sleeping, monotonic/wall-clock measurements, UTC timestamp generation, and optional append-only retry-log file I/O. E-011  
* engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph uses time.monotonic(), writes success/canonical logs through \_append\_jsonl, calls the vendor client, and reads/writes PostgreSQL unless dry\_run changes DB behavior. E-011  
* engine/cli/main.py reads stdin and local files and can write Reader/admin outputs; those are explicit CLI boundary effects rather than pure compute. E-008, E-009  
* No unseeded randomness was observed in the sampled sampler and compatibility modules. Sampled paths: engine/sampler/core.py, engine/compat/compute.py, and engine/compat/ordering.py; inspection method was complete-file static reading of those modules. E-007

Evidence anchors

* E-007 | Repo file | engine/sampler/core.py, engine/compat/compute.py, engine/compat/ordering.py | build\_candidate\_pool, \_is\_eligible, rank\_candidates, compat\_public, normalize\_pair | "if \_is\_zero\_weight(candidate): continue"; "ordered \= sorted(… \_compare\_entries …)"; "\# AB↔BA identity by normalization"; "a1,b1 \= normalize\_pair(a,b)"  
* E-011 | Repo file | engine/bodygraph/vendor\_client.py, engine/bodygraph/ingest.py | \_now\_ms, \_utc\_iso, \_append\_retry\_log, ingest\_vendor\_bodygraph | "return time.monotonic() \* 1000.0"; "time.gmtime"; "with path.open(\\"a\\"…"; "vendor\_result \= client.fetch(request)"; "DBAccess.for\_current\_env(…)"

# Adapter / HTTP Surfaces

## App creation and mounting

* adapter/wsgi.py:create\_app mounts adapter.http\_reader:bp at its declared paths with no added prefix and mounts engine.http.compat\_handler:compat\_blueprint, whose blueprint prefix is /api/compat/v1. E-005, E-017  
* adapter/http\_reader.py:create\_app performs the same two registrations. adapter/factory.py mounts only the Reader blueprint. E-005, E-006

## Mounted route groups

| Exact path/group | Definition and mounting | Handler(s) | Classification |
| :---- | :---- | :---- | :---- |
| /reader | adapter/http\_reader.py; Reader blueprint mounted at "" | reader\_v1, reader\_v1\_post | Reader-like JSON success |
| /api/aux/narrative, /aux/narrative | Same blueprint and mount | aux\_narrative | Aux/narrative |
| /api/compat/v1 | engine/http/compat\_handler.py, blueprint prefix /api/compat/v1; mounted by adapter/wsgi.py and adapter/http\_reader.py | get\_ids\_only, post\_json, post\_json\_head, post\_json\_options, request guard | Admin/internal |
| /internal/version | Reader blueprint | internal\_version | Admin/internal |
| /internal/healthz, /internal/readyz | Direct app routes in adapter/wsgi.py | internal\_healthz, internal\_readyz | Admin/internal |
| /internal/dev/sampler | Reader blueprint | dev\_sampler\_internal | Dev/diagnostic harness |
| /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction | Reader blueprint | corresponding conjunction handlers | Dev/diagnostic harness |
| /ops/db/unavailable, /ops/rails/refusal, /ops/probe/env | Reader blueprint | corresponding OPS handlers | Dev/diagnostic harness |
| /ops/writer/diagnostic | Reader blueprint | diagnostic\_writer, HEAD and OPTIONS handlers | Dev/diagnostic harness |

All path, handler, and classification facts above are grounded in decorators, blueprint mounting, and handler behavior rather than catalog names alone. E-005, E-006, E-016, E-017

## HTTP behavior hooks

* Reader GET generates a quoted SHA-256 ETag as "${sha256(body)}". E-016  
* If-None-Match strong matching can return 304 with an empty body while preserving ETag and Reader headers. E-016  
* Reader HEAD returns no body but sets Content-Length to the corresponding GET body length. E-016  
* \_set\_reader\_200\_headers supplies Reader response headers; Reader errors, internal, compatibility, dev, and writer surfaces generally set Cache-Control: no-store. The narrative success route instead uses private, max-age=0, must-revalidate; suppressed narrative responses use no-store. E-016, E-017  
* Reader and JSON routes emit application/json; charset=utf-8; narrative routes emit text/plain; charset=utf-8. E-016, E-017  
* Compatibility HEAD is explicitly a 405 empty-body response with Allow: POST, OPTIONS; OPTIONS returns 204\. It is not a success-body parity implementation. E-017  
* /internal/version implements GET/HEAD length parity but deliberately removes ETag and uses no-store. E-006

Evidence anchors

* E-016 | Repo file | adapter/http\_reader.py | get\_reader\_bp, reader\_v1, aux\_narrative, dev and OPS decorators | "@bp.get(\\"/reader\\")"; "etag \= \\"\\\\\\"\\" \+ \_sha256\_hex(body) \+ \\"\\\\\\"\\""; "if etag in tokens … Response(b\\"\\", status=304)"; "resp.headers\[\\"Content-Length\\"\] \= str(len(body))"; "@bp.get("/api/aux/narrative")"\`\*\*  
* E-017 | Repo file | engine/http/compat\_handler.py | compat\_blueprint, \_compat\_writer\_transport\_guard, post\_json | "url\_prefix=\\"/api/compat/v1\\""; "if request.method \== \\"HEAD\\": return \_writer\_head\_response()"; "body \= compat\_public(…)"; "return \_writer\_payload(body, status=200)"

# Presenter / Emitter

* engine/presenter/emitter.py:emit\_public is the shared governed JSON-byte emitter. It delegates to engine.serializer.canon.sercanon, sorts keys by default, and returns LF-terminated UTF-8 bytes. It is called by HTTP compatibility, Reader/internal/dev handlers, CLI, and BodyGraph ingest paths. E-010, E-017  
* engine/serializer/canon.py:sercanon delegates to engine.stable.sercanon.serialize; the documented semantics are UTF-8, ensure\_ascii=False, compact separators, sorted keys by default, and exactly one trailing newline. E-010  
* presenter/reader\_v1/emitter.py:emit\_reader\_v1 normalizes Reader categories, constructs the public preimage, hashes its canonical bytes for idempotence\_hash, then emits the final Reader envelope through engine.presenter.emitter. E-010  
* engine/runtime:emit\_reader\_public\_envelope and the Reader HTTP adapter provide the proven Reader caller chain into the presenter; CLI imports engine.presenter.emitter and writes returned bytes to stdout. E-008, E-016  
* presenter/json\_canon\_compare.py is a separate argparse utility for canonical-JSON comparison, distinct from runtime response emission. E-003  
* Multiple emitters therefore exist with distinct observed roles: shared canonical bytes (engine/presenter/emitter.py), Reader-envelope shaping (presenter/reader\_v1/emitter.py), and comparison tooling (presenter/json\_canon\_compare.py). E-003, E-010

Evidence anchors

* E-010 | Repo file | engine/presenter/emitter.py, engine/serializer/canon.py, engine/stable/sercanon.py, presenter/reader\_v1/emitter.py | emitter functions | "return canon.sercanon(envelope, sort\_keys=sort\_keys)"; "UTF-8 bytes … compact separators … exactly one trailing newline"; "digest \= hashlib.sha256(pre\_bytes).hexdigest()"; "public\_bytes \= emitter.emit\_public(final)"

# CLI Surfaces

## Discovery

Packaging, \_\_main\_\_, and argparse inspection found the installed hdctl entrypoint, module execution in engine/cli/\_\_main\_\_.py, argparse in engine/cli/main.py, and a separate argparse comparison utility in presenter/json\_canon\_compare.py. E-003, E-004, E-008

## Relevant commands

### hdctl showcompat

* Entrypoint: engine.cli.main:cli; handler: showcompat. E-004, E-008  
* Input modes include \--pair-file, paired \--a-file/--b-file (plus \--a/--b aliases), stdin, DB/vendor/auto source selection, user IDs, and birth tuples. \--conjunction selects conjunction output. E-008  
* Argparse does not mark the file arguments globally required; handler-level validation raises typed CliError values for conflicts, incomplete file pairs, unresolved source/user combinations, and malformed input. E-008, E-009  
* The call chain reaches pair normalization, compatibility computation or conjunction resolution, then engine.presenter.emitter. E-008, E-009  
* It writes canonical output to stdout. Optional \--dump-reader writes Reader bytes to a path; \--dump-admin-dir writes mode-0600 JSON and SHA-256 sidecars through the admin dump helper. E-008  
* Missing subcommands and argparse failures are normalized by cli to exit 64; handler-raised CliError carries its configured exit code. E-009

### hdctl aux-preview

* Handler: aux\_preview; accepts category/band/perspective or a pair file, optionally emits narrative text to stdout, and optionally writes an IDs-only preview via \--admin-out. E-008, E-009  
* Its call chain uses engine.narratives:emit\_public\_aux/get\_pack; canonical admin writing goes through canon\_dump. E-008, E-009

### hdctl bg:resolve

* Handler: bg\_resolve; \--user is parser-required, \--source defaults to auto, and \--upsert, \--dry-run, and vendor birth fields control resolver behavior. E-008  
* Vendor selection requires all three birth fields at handler level; omission raises MISSING\_VENDOR\_INPUT with exit 64\. E-009  
* It calls engine.bodygraph.resolve\_bodygraph, emits result.payload through the presenter, writes it to stdout, and returns the resolver’s exit code. E-009

### hdctl dev:sampler

* Handler: dev\_sampler\_run; parser-required inputs are \--viewer and \--candidates-file; \--seed is optional. E-008  
* It reads the candidates file, calls sample\_and\_rank, and writes canonical sampler output to stdout. The seed is echoed but not used for selection. E-009

Evidence anchors

* E-008 | Repo file | engine/cli/main.py | \_build\_parser | "sub.add\_parser(\\"showcompat\\"…)"; "sub.add\_parser(\\"aux-preview\\"…)"; "sub.add\_parser(\\"bg:resolve\\"…)"; "bg.add\_argument(\\"--user\\", required=True…)"; "sub.add\_parser(\\"dev:sampler\\"…)"  
* E-009 | Repo file | engine/cli/main.py | cli, bg\_resolve, showcompat, dev\_sampler\_run | "return 64 if code else 0"; "raise CliError("MISSING\_VENDOR\_INPUT", exit\_code=64)"; "sys.stdout.write(output)"; "ranked \= sample\_and\_rank(viewer, candidates)"; "sys.stdout.buffer.write(sercanon(payload))"\`\*\*

# Vendor Seam & BodyGraph Storage

## Vendor client

* engine/bodygraph/vendor\_client.py:HdApiClient is the primary observed external-vendor HTTP client. It uses urllib.request, validates HTTPS configuration, builds route-specific request bodies and auth headers, applies pinned retry/timeout profiles, fetches responses, parses JSON, and maps failures to VendorError. E-018  
* Governed resource paths are bodygraphs, bodygraphs/simple, charts, charts/simple, and charts/coordinates. Chart routes use Bearer auth posture; legacy BodyGraph routes use HD-Api-Key. E-018  
* Configuration names observed include HD\_API\_BASE\_URL, compatibility key HDAPI\_BASE\_URL, API/geocode keys consumed by from\_env, release identity, retry settings, SAFE\_MODE, and ALLOW\_NETWORK. No values were inspected or reported. E-018  
* classify\_bg\_resolve\_route\_policy selects charts for a configured v2 base and bodygraphs for non-v2/legacy bases. E-018  
* engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph gathers a request through HdApiClient, fetches and canonically serializes the response, optionally writes it to PostgreSQL, then reads it back and compares canonical hashes. E-011, E-019

## BodyGraph persistence and caching

* Persistence is direct PostgreSQL via engine.db.adapter.DBAccess and engine.db.providers.psycopg\_provider; runtime requirements declare psycopg. E-004, E-019  
* engine/bodygraph/ingest.py writes to hde.body\_graphs with identity columns (user\_id, vendor, vendor\_version, input\_fingerprint) and ON CONFLICT DO NOTHING, then reads payload::text back. E-019  
* engine/bodygraph/mapped\_cache.py:persist\_mapped\_bodygraph accepts only a strict adapter-mapped cache envelope, projects its payload, writes the same identity family, counts and reads the row, and verifies canonical read-back parity. E-019  
* The visible cache identity is (normalized\_user\_id, "hdapi", vendor\_version, input\_fingerprint). The ingest idempotency string is user\_id:vendor:vendor\_version:fingerprint. E-019  
* engine/compat/compute.py:conjunction\_public\_resolved attempts local\_lookup first; after a miss it calls resolve\_bodygraph(... source="vendor", upsert=True ...), then looks locally again. E-007

## Offline/vendor gating

* Vendor ingest explicitly refuses when SAFE\_MODE is truthy with PROVIDER\_REFUSED; it refuses when ALLOW\_NETWORK is false with PROVIDER\_NETWORK\_BLOCKED. E-019  
* Rails are considered open only when SAFE\_MODE=0 and ALLOW\_NETWORK=1; otherwise vendor client logging classifies them as closed\_default. E-018  
* The HTTP conjunction path supplies closed defaults and maps VendorError to a 503 writer envelope. E-016

Evidence anchors

* E-018 | Repo file | engine/bodygraph/vendor\_client.py | route contracts, HdApiClient, rails helpers | "\_ROUTE\_CONTRACTS \= {\\"bodygraphs\\": … \\"charts\\": …}"; "if parsed.scheme \!= \\"https\\": raise VendorError"; "open\_exception if safe\_mode \== \\"0\\" and allow\_network \== \\"1\\" else \\"closed\_default\\""  
* E-019 | Repo file | engine/bodygraph/ingest.py, engine/bodygraph/mapped\_cache.py | ingest\_vendor\_bodygraph, persist\_mapped\_bodygraph | "if safe\_mode: raise VendorError(\\"PROVIDER\_REFUSED\\"…)"; "if not allow\_network: raise VendorError(\\"PROVIDER\_NETWORK\_BLOCKED\\"…)"; "INSERT INTO hde.body\_graphs"; "ON CONFLICT … DO NOTHING"; "read\_back \!= canonical"\`\*\*

# Evidence, Indices, Catalogs

## Evidence homes

A complete static traversal counted the following principal homes. E-012, E-013

| Home | File count | Observed kinds and supported classification |
| :---- | :---- | :---- |
| docs/ | 143 | Markdown documentation, PF-canon documents, acceptance JSON, schemas, endpoint catalog, evidence index and hash. Mixed: prose is present alongside outputs managed by named tools and path-proof companions. |
| artifacts/ | 1,020 | JSON/JSONL, logs, text captures, snapshots, proof files, SHA-256 sidecars, path proofs, bundles, CLI/HTTP captures, DB/vendor evidence. Generated/governed classification is supported for indexed families by producer tools and path proofs; the root is mixed overall. |
| audit/ | 2,927 | QA step logs, token matrices, viability logs, OPS captures, gate outputs, manifests, close reports, doc deltas, snapshots, path proofs. Mixed producer-managed and hand-authored report material. |
| .audit\_src/ | 485 | Retained source/test snapshot with its own requirements and tests. Snapshot-like classification follows its distinct retained tree structure, not runtime imports. |
| proofs/ | 6 | Proof artifacts outside the main artifact root. |
| goldens/ | 14 | Golden-reference artifacts. |
| reports/ | 2 | Report files. |
| scan\_reports/ | 2 | Scan-report files. |
| catalog/ | 23 | Packaged catalog/release JSON and related material. |
| freeze/ | 1 | Freeze-related record. |
| narratives/ | 10 observed pack files | Hash-addressed manifest, palettes, templates, suppression map, keys, and SHA-256 companions. |
| Repository root | Multiple | EPIC step reports, checksums, HTTP/body captures, patches, temporary outputs, and backup archives. |

Representative exhaustive subfamilies observed beneath artifacts/ include audit/, bodygraph/, cli/, compat/, core/, db/, epic020/bundles/, identity/, ingest/, narratives/, presenter/, proofs/, runtime/, sampler/, and vendor/hdapi\_v2/. Beneath audit/, the traversal found gates/, ops/, qa/, docdeltas/, and retained documentation snapshots; audit/qa/ contains EPIC-specific families through at least HDE-EPIC038. E-013

## Evidence indices

* docs/evidence/INDEX.json is a JSON array of 548 records. Observed fields include artifact\_key, discovered\_physical\_path, epic\_id, notes, produced\_at\_utc, record\_type, schema\_version, sha256, size\_bytes, and tokens. E-020  
* docs/evidence/INDEX.sha256 is the human-index hash sentinel. E-012  
* artifacts/evidence\_index.jsonl contains 548 JSONL records. Its rows add mirror-specific fields such as proof\_anchor and role. E-020  
* tools/evidence/update\_evidence\_index.py:main loads and normalizes the human index, constructs and writes/checks the mirror and hash companions, refreshes path proofs, validates convergence, and supports \--check. E-020  
* tools/evidence/orientation\_demo.py reads the mirror, validates index/mirror/hash/size/path-proof relationships, and can generate or check orientation output. E-020  
* tools/evidence/validate\_evidence\_paths.py loads the index and validates referenced paths. ci/checks/check\_mirror\_schema.sh validates mirror schema, hashes, proof records, and self-record behavior. E-020  
* The CI workflow invokes index update in check mode, orientation in check mode, evidence-index hash checking, mirror-schema checking, and other evidence gates. E-015

## Endpoint catalogs

* docs/ENDPOINTS\_CATALOG.json is a JSON object with endpoints, generated\_at\_utc, and success\_endpoints. Endpoint rows include path, method, classification, blueprint module, internal/A7 flags, environment gate, and rails profile. E-020  
* artifacts/audit/ENDPOINTS\_CATALOG.json is the observed audit mirror with SHA-256 and path-proof companions. E-012  
* tests/http/test\_endpoint\_catalog.py validates catalog schema/types and checks /internal/version, the dev writer route ID, and the internal dev sampler classification. E-020  
* tools/evidence/update\_evidence\_index.py explicitly indexes and semantically validates both catalog copies and their SHA-256 companions. E-020

## Proof and snapshot artifacts

The complete evidence traversal found proof/snapshot families in:

* artifacts/proofs/, artifacts/sampler/pool\_snapshots/, artifacts/vendor/hdapi\_v2/\*.snapshot.json, artifacts/core/, artifacts/bodygraph/, artifacts/db/, and artifacts/audit/;  
* audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json;  
* numerous audit/qa/hde-epic\*/checks/\*\*/snapshots/ and OPS-discovery copies;  
* docs/schemas/\*\* definitions for core and sampler snapshot/log families;  
* path-proof companions named \*.path\_proof.txt throughout indexed homes. E-012, E-013

Producer wiring is directly established for major families by scripts such as generate\_evidence\_index\_snapshot.py, generate\_sampler\_evidence.py, generate\_engine\_core\_evidence.py, generate\_bodygraph\_policy\_proofs.py, generate\_v2\_mapped\_cache\_evidence.py, generate\_hde\_epic037\_\*, and generate\_hde\_epic038\_direct\_db\_selection.py. E-014  
No semantic claim is made solely from filenames; the producer-script and index wiring establish that these paths participate in evidence generation or validation.  
Evidence anchors

* E-012 | Repo listing | complete find traversal of evidence homes plus index/catalog lookup | "docs 143; artifacts 1020; audit 2927; proofs 6; goldens 14; reports 2; scan\_reports 2; .audit\_src 485; catalog 23; freeze 1"; "docs/evidence/INDEX.json"; "artifacts/evidence\_index.jsonl"; "docs/ENDPOINTS\_CATALOG.json"  
* E-013 | Repo listing | per-directory file-count traversal of docs artifacts audit .audit\_src proofs goldens reports scan\_reports | "artifacts/vendor/hdapi\_v2 70"; "audit/gates/json\_gate/canonical 6"; "audit/qa/hde-epic037 …"; "docs/pfcanon 31"; "docs/evidence 9"  
* E-020 | Repo file | indices, endpoint catalog, and index tooling | shape and symbols | "docs/evidence/INDEX.json list 548"; "mirror lines 548"; "\['endpoints', 'generated\_at\_utc', 'success\_endpoints'\]"; "def \_render\_mirror"; "def \_write\_path\_proof"; "def generate\_orientation"\`\*\*

# Tests, QA Harness, CI/Checks

## Test roots

* Active test root: tests/, with directories explicitly named unit/ and integration/; those two are classified according to repository labels. Other paths below are Uncategorized because their directory names indicate subject rather than test level. E-014  
* Retained secondary tree: .audit\_src/tests/, also containing unit/ and integration/ labels. It is separate from the active root. E-014  
* Active subject loci include:  
  * tests/reader\_v1/ and tests/http/: Reader and endpoint-catalog behavior;  
  * tests/compat/: compatibility API and computation;  
  * tests/cli/ and tests/hdctl/: CLI parsing, outputs, and exit behavior;  
  * tests/canon/, tests/compare/, tests/invariance/, tests/core/: canonical bytes, comparisons, parity, and determinism;  
  * tests/bodygraph/, tests/provider/, tests/db/, tests/ops/: vendor, resolver, persistence, and rails behavior;  
  * tests/evidence/, tests/audit/, tests/qa/, tests/artifacts/: indices, catalogs, evidence generators, and QA contracts. E-014, E-021

Examples of high-level assertions directly visible from test symbols include strict endpoint-catalog schema/type checks, internal-version GET/HEAD catalog records, canonical generator output, evidence chronology/path-proof binding, refusal of evidence generation under non-closed rails, and detection of presenter/vendor boundary violations. E-020, E-021  
Tests commonly use pytest monkeypatch and fixture injection for vendor/network behavior; the vendor client itself accepts injected request, sleep, monotonic, and wall-time callables. E-018, E-021

## CI

* .github/workflows/ci.yml defines workflow name ci, triggered on push and pull request, with job test. The job pins LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, and ALLOW\_NETWORK=0. E-015  
* Relevant exact step names include:  
  * Verify immutable release input without derived-tree writes;  
  * Run PO-006 token registry validity check \+ report (gated);  
  * Run direct PostgreSQL contract suites. E-015  
* Direct commands include ci/checks/check\_env\_pins.sh, check\_cli\_help.sh, release-manifest checking, runtime identity pytest, serializer/emitter guards, ordering-artifact check, evidence-index check, orientation check, token-registry validation, step-log manifest check, evidence-index hash check, direct-DB contract check, and focused DB/BodyGraph/OPS pytest suites. E-015

## QA-relevant scripts

Observed relevant check/generator families include:

* ci/checks/check\_env\_pins.sh — verifies deterministic environment pins.  
* ci/checks/check\_direct\_db\_contract.py — statically validates the direct-DB contract.  
* ci/checks/check\_evidence\_index\_hash.sh — checks the evidence-index hash sentinel.  
* ci/checks/check\_mirror\_schema.sh — validates machine-mirror records and proofs.  
* ci/checks/check\_final\_lf.sh — checks final-line-feed discipline.  
* tools/evidence/update\_evidence\_index.py — maintains/checks the human index and mirror.  
* tools/evidence/orientation\_demo.py — validates/generates topology orientation.  
* tools/evidence/run\_canonical\_json\_gate.py — canonical JSON gate.  
* tools/evidence/run\_sanity\_pipeline.py — evidence sanity chain.  
* tools/evidence/validate\_evidence\_paths.py — index path validation.  
* tools/evidence/check\_lf\_endings.py — evidence LF validation.  
* tools/cli/generate\_showcompat\_artifacts.py and generate\_showcompat\_parity\_artifacts.py — showcompat captures/parity artifacts.  
* tools/evidence/generate\_sampler\_evidence.py, generate\_engine\_core\_evidence.py, and generate\_bodygraph\_policy\_proofs.py — deterministic engine evidence.  
* tools/evidence/generate\_v2\_mapped\_cache\_evidence.py — configured-v2 mapped-cache evidence.  
* tools/qa/run\_hde\_epic024\_harness.py and EPIC close-pack generators — QA harness/close artifact entrypoints.  
* scripts/bodygraph/run\_refresh\_worker.py, scripts/db/run\_retention\_job.py, scripts/ingest/run\_vendor\_ingest.py — operational worker/retention/ingest scripts. E-014

Evidence anchors

* E-014 | Repo listing | test-root counts, CI tree, and relevant tool-family traversal | "tests/evidence 51; tests/adapter 18; tests/cli 12; tests/compat 9; tests/db 10; tests/bodygraph 9; tests/unit 9; tests/integration 1"; "ci/checks/check\_env\_pins.sh"; "tools/evidence/run\_sanity\_pipeline.py"; "scripts/ingest/run\_vendor\_ingest.py"  
* E-015 | Repo file | .github/workflows/ci.yml | workflow ci, job test | "LC\_ALL: C"; "SAFE\_MODE: \\"1\\""; "ALLOW\_NETWORK: \\"0\\""; "python tools/evidence/update\_evidence\_index.py \--check"; "python tools/evidence/orientation\_demo.py \--check"; "python ci/checks/check\_direct\_db\_contract.py"  
* E-021 | Repo listing | bounded test-symbol search in Reader/HTTP/CLI/compat/canon/evidence/invariance/core loci | "test\_endpoint\_catalog\_schema\_is\_strict\_and\_valid"; "test\_generator\_rendered\_outputs\_are\_canonical\_and\_scoped"; "test\_generator\_refuses\_non\_closed\_rails\_without\_writing"; "test\_epic034\_adapter\_boundary\_requires\_low\_level\_vendor\_io\_guard"\*\*

# Flows & Call Chains

## Reader success flow over HTTP — Found

Chain:  
adapter/wsgi.py:create\_app → adapter/http\_reader.py:reader\_v1 → engine.runtime:emit\_reader\_public\_envelope → presenter/reader\_v1/emitter.py:emit\_reader\_v1 → engine/presenter/emitter.py:emit\_public → Flask Response

* The Reader blueprint is mounted without an additional prefix. E-005  
* /reader requires v=1, a dev environment, a and b chart paths, and timezone validation. E-016  
* The handler loads both chart files, obtains runtime identity, and calls the injected/default Reader emitter. E-016  
* Reader-envelope shaping sorts/deduplicates categories and adds an idempotence hash derived from canonical preimage bytes. E-010  
* Canonical bytes are returned with quoted ETag, content length, and Reader headers; HEAD and conditional 304 branches are explicit. E-010, E-016

## Compat API flow over HTTP — Found

Chain:  
adapter/wsgi.py:create\_app → engine/http/compat\_handler.py:post\_json → engine.validation.viewer\_prefs:validate\_viewer\_prefs/normalize\_viewer\_prefs → engine.compat.compute:compat\_public → engine.presenter.emitter:emit\_public → engine.http.compat\_handler:\_writer\_payload

* The mounted base path is /api/compat/v1. E-005, E-017  
* POST is hidden with ERR\_NOT\_FOUND when APP\_ENV=prod. E-017  
* Input may contain party payloads or paired IDs, but mixed ID/payload modes are rejected. E-017  
* Validated viewer preferences feed compatibility computation. E-017  
* Compatibility categories and keys are emitted as canonical JSON with no-store, no ETag, and explicit content length. E-017

## CLI showcompat or compat-preview flow — Found

Chain:  
pyproject.toml:hdctl → engine/cli/main.py:cli → engine/cli/main.py:showcompat → engine.compat.ordering:normalize\_pair → engine.compat.compute:compat\_public → engine.runtime:emit\_reader\_public\_envelope / engine.presenter.emitter:emit\_public → stdout or optional dump paths

* hdctl is the installed console script. E-004  
* \_build\_parser registers showcompat and its file/stdin/source/conjunction inputs. E-008  
* Handler-level validation rejects conflicting or incomplete modes with typed CliError. E-009  
* Pair normalization supplies AB↔BA stability before computation. E-007  
* Canonical bytes are written to stdout; optional Reader/admin dump arguments create explicitly requested files. E-008, E-009

## Vendor acquisition or BodyGraph-ingest flow — Found

Chain:  
scripts/ingest/run\_vendor\_ingest.py:main → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.build\_request → HdApiClient.fetch → engine.presenter.emitter:emit\_public\_with\_envelope → engine.db.adapter:DBAccess.tx/query → hde.body\_graphs

* The operational script family contains a dedicated vendor-ingest entrypoint. E-014  
* Ingest refuses closed SAFE rails or disabled network before vendor acquisition. E-019  
* The vendor client shapes route/auth/body and performs the external HTTPS request with pinned retry and timeout settings. E-018  
* Vendor payload is canonically serialized and hashed. E-011, E-019  
* Non-dry-run ingestion writes the PostgreSQL row, reads it back, re-emits it, and compares hashes. E-019  
* Success and retry logs are optional append-only file outputs under configured/default artifact paths. E-011

## Evidence-index update or validation flow — Found

Chain:  
.github/workflows/ci.yml:test → tools/evidence/update\_evidence\_index.py:main \--check → \_load\_human\_index/\_render\_human\_index/\_render\_mirror → \_write\_if\_changed(check=True) → tools/evidence/orientation\_demo.py:generate\_orientation(check=True) → ci/checks/check\_evidence\_index\_hash.sh / check\_mirror\_schema.sh

* CI invokes the index updater and orientation utility in check mode. E-015  
* The updater loads, normalizes, deduplicates, and renders human-index and mirror records. E-020  
* In check mode, \_write\_if\_changed validates expected bytes rather than serving as a runtime producer. E-020  
* Mirror rendering includes proof anchors, roles, hashes, sizes, and a self-record. E-020  
* Subsequent checks validate index hash and mirror schema/path-proof relationships. E-015, E-020

# Drift and Reality vs Expectations

| Finding | Observed fact | Expected comparison point | Classification | Evidence | Direct impact |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DA-01 — Directory/architecture drift | Dedicated top-level engine/, adapter/, and presenter/ roots all exist, but presenter functionality also exists under engine/presenter/, and HTTP compatibility handlers live under engine/http/. | Separate engine, adapter, and presenter families. | Partial | E-003, E-010, E-017 | Presenter and HTTP-adapter responsibilities are resolved through more than one package root. |
| DA-02 — Directory/architecture drift | DB and vendor functions are nested under engine/db/ and engine/bodygraph/; no separate top-level vendor/ or db/ package is used by the observed runtime chain. | Vendor and DB as comparison families, without requiring top-level directories. | Aligned | E-003, E-018, E-019 | Runtime imports resolve these roles through the engine package. |
| SD-01 — Surface drift | /reader is Reader-like and file-path driven; /api/compat/v1 is a separate internal/admin compatibility surface with GET, POST, HEAD, and OPTIONS handling. | Reader and compat HTTP surfaces. | Partial | E-016, E-017 | Reader and compatibility calls enter different handlers and return different envelope/header semantics. |
| SD-02 — Surface drift | The repository exposes multiple app factories: adapter/wsgi.py, adapter/http\_reader.py, and adapter/factory.py; the narrow factory does not mount the compatibility blueprint. | One observable HTTP startup/mounting family. | Drift | E-005, E-006 | Route availability depends on which factory is selected. |
| ED-01 — Evidence drift | Evidence is distributed across docs/, artifacts/, audit/, .audit\_src/, proofs/, goldens/, reports, catalog/freeze/narrative roots, and root-level captures. | Evidence family as a comparison frame. | Partial | E-002, E-012, E-013 | Evidence discovery requires traversing multiple roots, although the 548-row human index and mirror bind many governed artifacts. |
| ED-02 — Evidence drift | docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl both contain 548 records and are maintained/validated by explicit tools and CI. | Indexed evidence posture. | Aligned | E-015, E-020 | Human-index and machine-mirror coherence is directly checked. |
| DD-01 — Determinism drift | Compatibility and sampler compute paths use stable hashing, normalization, explicit sorting, and no observed clocks/randomness; vendor/ingest paths use clocks, network, DB, and append-only logs. | Deterministic engine core with isolated effects. | Aligned | E-007, E-011, E-018, E-019 | Pure compute and effectful acquisition/storage have observably different dependencies. |
| VS-01 — Vendor seam drift | Vendor I/O is concentrated in engine/bodygraph/vendor\_client.py; ingest and resolver call it under explicit SAFE/network gates. | Identifiable vendor seam. | Aligned | E-018, E-019 | Closed rails produce typed refusal before normal vendor acquisition. |
| PC-01 — Path-case drift | Active package roots and imports consistently use lowercase engine, adapter, and presenter; evidence paths preserve mixed tokens such as ENDPOINTS\_CATALOG.json, EPIC IDs, and case-bearing report names. | Stable expected family path case. | Partial | E-002, E-003, E-012 | Code imports use lowercase package identities while evidence consumers must preserve exact artifact case. |
| RP-01 — Root proliferation | 12 truth-bearing/governed-output roots were observed: .audit\_src/, artifacts/, audit/, catalog/, docs/, freeze/, goldens/, narratives/, proofs/, reports/, scan\_reports/, and root-level checksum/report/capture files. | Root proliferation category requires count and paths only. | Partial | E-002, E-012, E-013 | Impact: Not established from Repo evidence. |
| EP-01 — Emitter posture | Shared canonical emission is in engine/presenter/emitter.py; Reader shaping is in presenter/reader\_v1/emitter.py; comparison tooling is in presenter/json\_canon\_compare.py. | Presenter/emitter family. | Partial | E-003, E-010 | Callers select different layers depending on whether they need generic canonical bytes, Reader shaping, or comparison output. |

# Negative-Claim Proof Appendix

## NCP-001

* What was searched: exact packaging/build filenames setup.py, setup.cfg, package.json, pnpm-workspace.yaml, and workspace/build equivalents included in the depth-two packaging listing  
* Search method: find  
* Scope: Repo root, maximum depth 2  
* Case: sensitive  
* Result: 0 hits

