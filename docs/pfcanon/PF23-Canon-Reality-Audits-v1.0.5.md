# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.0.5

**Status:** Canon

**Effective date:** 2026-03-14

**Last Update Gate:** HDE-EPIC027

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

**Date:** 2026-03-14

**Last Epic:** HDE-EPIC027

## Audit Snapshot Metadata

* Repo root confirmation: pwd returned /workspace/glow-hdengine-v2.  
* Commit: git rev-parse HEAD → 0e3375dfdbba21a54f8a525716b7c4ccf90b11dc  
* Branch: git rev-parse \--abbrev-ref HEAD → work  
* Working tree cleanliness: git status \--porcelain returned no paths (clean).  
* Timestamp (UTC): 2026-03-14T05:12:49Z  
* Execution environment:  
  * OS/kernel: Linux 6.12.47  
  * Python: Python 3.10.19  
  * Node: v22.21.1

---

## Top-level Repo Map

### Expected HD Engine families (explicit classification)

* engine/ — Present  
  * Contains core runtime, compute, sampler, CLI, provider, DB code.  
  * Anchors: engine/compat/compute.py, engine/sampler/core.py, engine/cli/main.py  
* adapter/ — Present  
  * HTTP-layer wiring, cache/etag helpers, env guards.  
  * Anchors: adapter/http\_reader.py, adapter/factory.py, adapter/cache\_keys.py  
* presenter/ — Present  
  * Presenter package including reader emitter variant.  
  * Anchors: presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py  
* CLI package location(s) — Present  
  * Package script entry in pyproject.toml (hdctl \= "engine.cli.main:cli"), plus launcher at scripts/hdctl.py.  
  * Anchors: pyproject.toml, engine/cli/main.py, scripts/hdctl.py  
* docs/ — Present  
  * Architecture, acceptance maps, evidence docs, PF canon docs.  
  * Anchors: docs/architecture/emitters.md, docs/evidence/INDEX.json, docs/ENDPOINTS\_CATALOG.json  
* artifacts/ — Present  
  * Generated evidence, proofs, snapshots, CLI/compat outputs.  
  * Anchors: artifacts/evidence\_index.jsonl, artifacts/cli/showcompat/stdout.json, artifacts/proofs/reader\_\_get.txt  
* audit/ — Present  
  * Close reports, manifests, QA runs, gates, doc deltas.  
  * Anchors: audit/EPIC-024\_close\_report.md, audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json, audit/qa/hde-epic026/  
* tools/ — Present  
  * Evidence/index generators, QA harnesses, config and CLI artifact tools.  
  * Anchors: tools/evidence/update\_evidence\_index.py, tools/qa/run\_hde\_epic024\_harness.py, tools/cli/generate\_showcompat\_artifacts.py  
* ci/ — Present  
  * Shell/Python checks for env pins, mirror schema, LF and release identity.  
  * Anchors: ci/checks/check\_env\_pins.sh, ci/checks/check\_mirror\_schema.sh, ci/checks/check\_release\_identity.sh  
* .github/workflows/ — Present  
  * CI workflow executes determinism/evidence/test gates.  
  * Anchor: .github/workflows/ci.yml  
* tests/ — Present  
  * HTTP/CLI/evidence/order/QA tests.  
  * Anchors: tests/http/test\_compat\_endpoint\_contract.py, tests/cli/test\_serializer\_guards.py, tests/ops/test\_evidence\_index.py  
* scripts/ — Present  
  * Operational CLIs and support scripts (including fallback CLI launchers).  
  * Anchors: scripts/hdctl.py, scripts/release\_id\_recompute.py, scripts/db/run\_retention\_job.py  
* vendor/ — Not found (top-level directory)  
  * Negative proof in appendix.

### Root discipline capture (truth-home-like roots observed)

* audit/  
* artifacts/  
* docs/  
* tools/  
* scripts/  
* catalog/  
* proofs/  
* parity/

(These paths exist in top-level listing output and contain governance/evidence-like content.)  
---

## Packaging and Entrypoints

### 3.1 Packaging/build configuration

* pyproject.toml  
  * Declares project metadata (\[project\] name \= "glow-hdengine"), package discovery includes engine\*, adapter\*, presenter\*, and console script.  
  * Excerpt: \[project.scripts\] hdctl \= "engine.cli.main:cli".  
* requirements.txt  
  * Runtime dependencies listed (psycopg\[binary\], Flask, gunicorn).  
* requirements-dev.txt  
  * Test dependencies listed (pytest, pytest-cov, pytest-mock, jsonschema).  
* No setup.py / setup.cfg found  
  * Negative proof in appendix.

### 3.2 Entrypoint inventory

* HTTP app startup  
  * adapter/factory.py:create\_app creates Flask app and registers bp.  
  * Excerpt: app \= Flask(\_\_name\_\_) and app.register\_blueprint(bp, url\_prefix="").  
  * Procfile runs gunicorn against adapter.factory:create\_app().  
* Alternate HTTP app assembly  
  * adapter/http\_reader.py:create\_app registers bp plus compat\_blueprint.  
  * Excerpt: app.register\_blueprint(compat\_blueprint).  
* CLI console script  
  * engine/cli/main.py:cli invoked by hdctl via pyproject entrypoint.  
* Module CLI entrypoint  
  * engine/cli/\_\_main\_\_.py:main delegates to cli() and exits with returned code.  
* Evidence/background-like batch entrypoints  
  * tools/evidence/update\_evidence\_index.py:main  
  * tools/evidence/orientation\_demo.py:main  
  * tools/evidence/run\_sanity\_pipeline.py:main  
  * tools/qa/run\_hde\_epic024\_harness.py (script-style harness entrypoint)

---

## Engine Modules

### 4.1 Sampler

* engine/sampler/core.py  
  * build\_candidate\_pool(...): filters zero-weight/ineligible candidates into pool.  
  * rank\_candidates(...): deterministic ordering of pool entries.  
  * sample\_and\_rank(...): top-level wrapper for pool \+ rank flow.  
  * Excerpt evidence: comments/state include “No randomness, clocks, or external state are consulted.”

### 4.2 Core compute

* engine/compat/compute.py  
  * band\_for(score): maps score to Cool/Open/Warm/Glow.  
  * compat\_public(a,b,...): computes categories list \+ meta envelope.  
  * conjunction\_public(...): wraps normalized compat under conjunction.left/right/compat.  
  * conjunction\_public\_resolved(...): resolves unresolved parties (local lookup \+ resolver flow) then emits conjunction payload.  
  * Symmetry anchor: a1,b1 \= normalize\_pair(a,b) then pkey \= pair\_key(a1,b1) inside compat\_public.  
* Normalization/canonicalization boundary (engine)  
  * Compute normalizes party ordering via normalize\_pair.  
  * Canonical byte serialization delegated to emitter/serializer (engine.presenter.emitter.emit\_public → engine.serializer.canon.sercanon).

### 4.3 Determinism hazards inventory (engine modules)

Observed in sampled engine modules:

* Network calls  
  * engine/bodygraph/vendor\_client.py: urlrequest.urlopen(req, timeout=timeout).  
* Clock/time usage  
  * engine/bodygraph/vendor\_client.py: time.monotonic(), time.strftime(...).  
  * engine/bodygraph/ingest.py: start \= time.monotonic() and duration calculations.  
* File I/O  
  * engine/bodygraph/vendor\_client.py: with path.open("a", encoding="utf-8") as handle:  
  * engine/bodygraph/ingest.py: same append-log pattern.  
* No randomness observed in sampled engine compute/sampler paths  
  * engine/sampler/core.py uses deterministic sorting/tie-breakers and no RNG calls in inspected code.

---

## Adapter / HTTP Surfaces

### 5.1 Route registration map

* App/router creation  
  * adapter/http\_reader.py:create\_app  
  * adapter/factory.py:create\_app  
* Blueprint mounting  
  * adapter/http\_reader.py: app.register\_blueprint(bp, url\_prefix="")  
  * adapter/http\_reader.py: app.register\_blueprint(compat\_blueprint)  
  * adapter/factory.py: app.register\_blueprint(bp, url\_prefix="")  
* Route groups and prefixes  
  * compat\_blueprint defined in engine/http/compat\_handler.py with url\_prefix="/api/compat/v1".  
  * Reader/aux/internal/dev routes are on bp in adapter/http\_reader.py with empty app prefix.

### 5.2 Surface classification

* Reader-like JSON success  
  * adapter/http\_reader.py handler reader\_v1 at @bp.get("/reader").  
* Aux/narrative  
  * adapter/http\_reader.py handler aux\_narrative at /api/aux/narrative and /aux/narrative.  
* Admin/internal  
  * adapter/http\_reader.py /internal/version, /ops/writer/diagnostic, /ops/probe/env, /ops/db/unavailable.  
  * engine/http/compat\_handler.py POST /api/compat/v1.  
* Dev/diagnostic harness  
  * adapter/http\_reader.py /internal/dev/sampler, /dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction.

### 5.3 Transport semantics hooks

* HEAD vs GET parity  
  * Reader route checks if request.method.upper() \== "HEAD" and sets Content-Length from GET body length.  
  * Internal version route has explicit GET/HEAD branch with identical payload length contract.  
* Conditional responses / 304  
  * Reader route computes ETag and returns 304 when If-None-Match token matches.  
* ETag generation/quoting  
  * Reader route: etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"".  
  * Aux narrative sets and explicitly quotes ETag.  
* Cache-control rules  
  * Reader success: "private, max-age=0, must-revalidate".  
  * Writer/internal paths set "no-store" in multiple handlers.  
* Content-Type rules  
  * Reader/writer/internal set application/json; charset=utf-8; aux sets text/plain; charset=utf-8.

---

## Presenter / Emitter

* Primary canonical emitter  
  * engine/presenter/emitter.py  
  * emit\_public(envelope, sort\_keys=True) delegates to canonical serializer.  
  * Excerpt: “Canonical emitter… Delegates to canonical serializer… Sorts keys by default”.  
* Serializer implementation  
  * engine/serializer/canon.py:sercanon calls engine.stable.sercanon.serialize.  
  * Excerpt notes UTF-8, sorted keys, compact separators, trailing newline.  
* Reader-specific presenter  
  * presenter/reader\_v1/emitter.py:emit\_reader\_v1  
  * Builds preimage, computes idempotence\_hash, emits final canonical bytes.  
* Callers  
  * HTTP/CLI call engine.presenter.emit\_public / engine.presenter.emitter.emit\_public (e.g., engine/http/compat\_handler.py, adapter/http\_reader.py, engine/cli/main.py).

---

## CLI Surfaces

* Command entrypoint  
  * hdctl console script → engine.cli.main:cli (pyproject.toml).  
* Subcommands and parser  
  * In engine/cli/main.py:  
    * showcompat  
    * aux-preview  
    * bg:resolve  
    * dev:sampler-run  
  * Parser uses argparse with subparsers(dest="command", required=True).  
* Relevant command: showcompat  
  * Required structure evidenced by args definitions for \--pair-file or \--a-file/--b-file and conjunction args (--conjunction, \--user-a, \--user-b etc.).  
  * Call chain includes:  
    * parsing/input loading  
    * compat/conjunction compute (compat\_public / conjunction\_public\_resolved)  
    * canonical emit via emitter.emit\_public  
    * stdout via \_emit\_stdout\_bytes.  
* Output surfaces  
  * Stdout: \_emit\_stdout\_bytes writes sys.stdout.buffer.write(payload).  
  * File writes:  
    * \_dump\_reader\_bytes for \--dump-reader  
    * admin dump writers under \--dump-admin-dir.  
  * Nonzero on arg/error paths:  
    * cli() returns 64 on parser/system usage issues and maps CliError to code \+ stderr token line.

---

## Vendor Seam & BodyGraph Storage

### 8.1 Vendor client

* Vendor HTTP seam  
  * engine/bodygraph/vendor\_client.py uses stdlib urllib.  
  * Excerpt: with urlrequest.urlopen(req, timeout=timeout) as resp.  
* Ingest orchestration  
  * engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph(...)  
  * Builds request, fetches vendor payload, emits canonical bytes, persists DB row, logs evidence.  
* Resolver control-flow  
  * engine/bodygraph/resolver.py:resolve\_bodygraph(...) enforces source and rails behavior.  
* Inputs/env keys observed  
  * Determinism/offline gating keys: SAFE\_MODE, ALLOW\_NETWORK (resolver logic).  
  * DB/env keys: in DB adapter DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD.

### 8.2 BodyGraph persistence/caching

* DB layer  
  * engine/db/adapter.py:DBAccess.for\_current\_env(...) chooses psycopg vs bridge provider.  
* Persistence  
  * engine/bodygraph/ingest.py:\_persist\_bodygraph inserts into hde.body\_graphs.  
* Read-after-write/checks  
  * \_row\_count and \_fetch\_payload query same table to validate persistence/parity.  
* Cache key formation (adapter)  
  * adapter/cache\_keys.py:build\_cache\_key(...) creates orientation-safe tuple (min\_user,max\_user,release\_id,fp\_min,fp\_max).

### 8.3 Offline / vendor-required posture

* Explicit gating exists  
  * engine/bodygraph/resolver.py:\_resolve\_vendor:  
    * If SAFE rails closed → returns PROVIDER\_REFUSED.  
    * If network not allowed → returns PROVIDER\_NETWORK\_BLOCKED.  
  * conjunction\_public\_resolved defaults env to {"SAFE\_MODE": "1", "ALLOW\_NETWORK": "0"} when env not provided.

---

## Evidence, Indices, Catalogs

### 9.1 Evidence homes inventory

* docs/  
  * Contains acceptance maps, architecture docs, endpoint catalog, evidence index.  
  * Generated/hand-authored appears mixed (JSON maps \+ markdown narrative docs).  
* artifacts/  
  * Contains machine artifacts, proofs, CLI captures, parity outputs, DB snapshots.  
  * Mostly generated by naming patterns (\*.sha256, \*.path\_proof.txt, showcompat/stdout.json).  
* audit/  
  * Contains close reports, manifests, gate outputs, QA logs/manifests.  
  * Mixed: generated logs plus authored reports.  
* Other evidence-like homes  
  * parity/, proofs/, catalog/ present as additional artifact homes.

### 9.2 Evidence index structures

* docs/evidence/INDEX.json  
  * JSON array of artifact records (artifact\_key, discovered\_physical\_path, sha/size/token metadata).  
* docs/evidence/INDEX.sha256  
  * Hash sentinel for INDEX file.  
* artifacts/evidence\_index.jsonl  
  * Line-delimited mirror records with proof anchors.  
* Tooling  
  * tools/evidence/update\_evidence\_index.py defines:  
    * HUMAN\_INDEX \= ...docs/evidence/INDEX.json  
    * HASH\_SENTINEL \= ...docs/evidence/INDEX.sha256  
    * MIRROR\_PATH \= ...artifacts/evidence\_index.jsonl  
    * path-proof write/refresh functions (\_write\_path\_proof, \_refresh\_path\_proof, main).

### 9.3 Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json (and mirrored artifacts/audit/ENDPOINTS\_CATALOG.json)  
  * Shape includes endpoints array entries with keys such as:  
    * path, method, classification, blueprint\_module, env\_gate, rails\_profile, a7\_eligible.  
  * Referenced by tests:  
    * tests/http/test\_compat\_endpoint\_contract.py reads it and asserts compat entry presence/classification.

### 9.4 Proof/snapshot artifacts

* Examples observed:  
  * artifacts/proofs/reader\_\_get.txt  
  * artifacts/proofs/writers\_no\_304.txt  
  * artifacts/proofs/success\_writers\_errors.txt (+ .path\_proof.txt)  
  * artifacts/cli/showcompat/stdout.json and stdout.json.sha256  
* Producer anchors:  
  * tools/cli/generate\_showcompat\_artifacts.py writes showcompat stdout and sha files.  
  * tools/evidence/update\_evidence\_index.py writes proof-anchor files (\*.path\_proof.txt).

---

## Tests, QA Harness, CI/Checks

### 10.1 Tests map (key loci)

* HTTP compat/contract  
  * tests/http/test\_compat\_endpoint\_contract.py  
  * Asserts compat endpoint contract, conjunction canonical stability, and endpoint catalog inclusion.  
* CLI canonical/guards  
  * tests/cli/test\_serializer\_guards.py  
  * Exercises serializer/CLI guard behavior (as named and run in CI).  
* Evidence index/cross-check  
  * tests/ops/test\_evidence\_index.py  
  * Asserts required artifacts exist in INDEX.json and evidence\_index.jsonl with proof anchors/sha.  
* Evidence bundle integration  
  * tests/evidence/test\_epic020\_bundle\_index\_integration.py  
  * Verifies generated bundle/manifest records are indexed and mirrored consistently.  
* Vendor/network fixture implications  
  * In tests/http/test\_compat\_endpoint\_contract.py, tests include VendorError and resolver behavior paths, indicating vendor seam behavior is exercised/mocked in tests.

### 10.2 CI workflows

* Workflow file: .github/workflows/ci.yml  
* Job test  
  * Runs env pin check, CLI guards, canonical JSON gate, evidence index update/checks, mirror schema/LF checks, and pytest suites.  
* Job compat-conj-pr01-closure  
  * Runs targeted conjunction hash/evidence tests.  
* Job epic020  
  * Runs EPIC020 acceptance test set.  
* Job compat-http-epic020  
  * Runs compat HTTP tests.  
* Job epic020-evidence-bundles  
  * Builds evidence bundles, updates index, validates schema, runs bundle-index integration test.  
* Job sanity-pipeline  
  * Runs python tools/evidence/run\_sanity\_pipeline.py.

### 10.3 Script/check inventory (QA-relevant)

* ci/checks/check\_env\_pins.sh  
  * Invokes python \-m engine.runtime.determinism\_env ... \--check-log.  
* ci/checks/check\_mirror\_schema.sh  
  * Mirror schema validation gate.  
* ci/checks/check\_release\_identity.sh  
  * Release identity gate script.  
* tools/evidence/run\_sanity\_pipeline.py  
  * Orchestrates deterministic pipeline steps and writes artifacts/sanity/sanity.log.  
* tools/evidence/update\_evidence\_index.py  
  * Regenerates INDEX \+ mirror \+ proof anchors.  
* tools/evidence/validate\_evidence\_paths.py  
  * Validates each mirror discovered\_physical\_path exists and is safe/relative.  
* tools/evidence/check\_lf\_endings.py  
  * Final LF discipline gate.  
* tools/qa/run\_hde\_epic024\_harness.py  
  * EPIC024 QA harness orchestration.

---

## Flows & Call Chains

### 1\) Reader success flow (HTTP)

adapter/http\_reader.py:reader\_v1 → engine.runtime.emit\_reader\_public\_bytes → (presenter/serializer path) → flask.Response

* Starts at @bp.get("/reader").  
* Validates query args and APP\_ENV gate.  
* Emits bytes with engine/invocation/release identity args.  
* Computes quoted ETag from body sha256.  
* Handles conditional 304 and HEAD parity in-handler.

### 2\) Compat API flow (HTTP)

engine/http/compat\_handler.py:post\_json → engine.compat.compute.compat\_public → engine.presenter.emit\_public → flask.Response

* POST /api/compat/v1 validates payload shape and viewer prefs.  
* Supports ID-mode resolution fallback (\_resolve\_person\_by\_id minimal resolver in module).  
* Builds compat categories and appends flattened keys.  
* Writer-style transport headers: Cache-Control: no-store, no ETag.

### 3\) CLI showcompat / compat preview flow

engine/cli/main.py:cli → showcompat → engine.compat.compute.compat\_public / conjunction\_public\_resolved → engine.presenter.emitter.emit\_public → \_emit\_stdout\_bytes

* Parser defines subcommand and required/optional input modes.  
* Branches by source (db|vendor|auto) and conjunction mode.  
* Emits canonical bytes to stdout; validates trailing LF/CRLF guard in \_emit\_stdout\_bytes.  
* Optional artifact writes with \--dump-reader and \--dump-admin-dir.

### 4\) Vendor acquisition / BodyGraph ingest flow

engine/compat/compute.py:conjunction\_public\_resolved → engine.bodygraph.resolver.resolve\_bodygraph → engine.bodygraph.ingest.ingest\_vendor\_bodygraph → engine.bodygraph.vendor\_client.HDAPIClient.fetch → engine.db.DBAccess

* Conjunction resolver attempts local lookup first, then resolver.  
* Resolver enforces SAFE/network gates before vendor path.  
* Ingest fetches vendor payload, canonical-emits, writes DB row (hde.body\_graphs), computes parity/hash evidence.  
* Vendor client issues HTTP request via urllib.

### 5\) Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py:main → writes docs/evidence/INDEX.json \+ INDEX.sha256 \+ artifacts/evidence\_index.jsonl \+ \*.path\_proof.txt → tools/evidence/orientation\_demo.py:main(--check) / ci/checks/check\_mirror\_schema.sh

* Update tool defines canonical homes (HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH).  
* Generates/refreshes path proofs and mirror self-record handling.  
* Orientation demo checks coherence between index/mirror/proofs.  
* CI workflow runs these checks in closed-rails jobs.

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Both adapter/factory.py:create\_app and adapter/http\_reader.py:create\_app construct Flask apps.  
  * Proof: each file contains def create\_app() \+ app \= Flask(\_\_name\_\_).  
  * Impact: introduces two app-factory loci for runtime wiring.

### Surface drift

* Observed: Dev conjunction HTTP surfaces exist (/dev/sampler/conjunction, /dev/reader/conjunction, /dev/writer/conjunction) alongside reader/internal/compat.  
  * Proof: route decorators in adapter/http\_reader.py for all three paths.  
  * Impact: runtime surface includes explicit dev-harness endpoints in addition to core reader/compat endpoints.

### Evidence drift

* Observed: Governed/evidence-like artifacts are distributed across multiple roots (audit/, artifacts/, docs/, plus proofs/ and parity/).  
  * Proof: top-level listing shows all roots; docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl coexist; parity/errors\_reader\_cli... records appear in index.  
  * Impact: evidence location is multi-home by repository layout.

### Determinism drift

* Observed: Determinism gates are explicit, but vendor/ingest modules include time/network/file I/O operations.  
  * Proof: engine/runtime/determinism\_env.py pins env rails; engine/bodygraph/vendor\_client.py uses urlopen, time.\*, append-log file writes.  
  * Impact: deterministic posture depends on rail enforcement around non-pure modules.

### Vendor seam drift

* Observed: Vendor seam is inside engine package under engine/bodygraph/\* rather than a top-level vendor/ directory.  
  * Proof: vendor HTTP code in engine/bodygraph/vendor\_client.py; top-level vendor/ directory absent.  
  * Impact: vendor integration is package-internal rather than root-separated.

### Path-case drift

* Observed: Mixed naming/case style in audit/report artifact filenames (e.g., EPIC-024\_close\_report.md, EPIC017\_close\_report.md.path\_proof.txt).  
  * Proof: audit/ file listing examples from top-level and sampled output.  
  * Impact: naming conventions vary across audit artifacts.

### Root proliferation

* Observed: 8 truth-home-like roots identified: audit/, artifacts/, docs/, tools/, scripts/, catalog/, proofs/, parity/.  
  * Proof: top-level listing output includes each root.  
  * Impact: multiple roots hold governance/evidence/runtime-check materials.

---

## Negative-Claim Proof Appendix

1. Claim: Top-level vendor/ directory not found.  
   * Search token: directory name vendor  
   * Method: find . \-maxdepth 1 \-type d \-name 'vendor' \-print  
   * Scope: repo root  
   * Result: 0 hits (command produced no path output)  
2. Claim: setup.py / setup.cfg not found.  
   * Search token: filenames setup.py, setup.cfg  
   * Method: find . \-maxdepth 2 \-type f \\( \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'pyproject.toml' \-o \-name 'package.json' \\) | sort  
   * Scope: repo root through depth 2  
   * Result: only ./pyproject.toml found (0 hits for setup.py and setup.cfg)

---

## Checks executed

✅ pwd; git rev-parse HEAD; git rev-parse \--abbrev-ref HEAD; git status \--porcelain; date \-u \+"%Y-%m-%dT%H:%M:%SZ"; uname \-sr; python3 \--version 2\>/dev/null || true; node \--version 2\>/dev/null || true  
✅ find . \-maxdepth 1 \-mindepth 1 \-printf "%f\\n" | sort  
✅ rg \-n "\\\[project\\\]|\\\[project\\.scripts\\\]|entry\_points|console\_scripts|if \_\_name\_\_ \== \['\\"\]\_\_main\_\_\['\\"\]|Flask\\(|FastAPI\\(|APIRouter\\(|Blueprint\\(|add\_url\_rule|@app\\.route|@router\\.|argparse|click\\.group|typer\\.Typer" pyproject.toml run\_flask.py engine adapter presenter tools scripts tests ci docs \-g '\!docs/pfcanon/\*\*'  
✅ for d in engine adapter presenter docs artifacts audit tools ci tests scripts vendor; do if \[ \-e "$d" \]; then echo "== $d \=="; find "$d" \-maxdepth 2 \-type f | head \-n 8; else echo "== $d (missing) \=="; fi; done  
✅ sed \-n '1,220p' run\_flask.py; sed \-n '1,260p' adapter/http\_reader.py; sed \-n '1,220p' engine/http/compat\_handler.py  
✅ rg \-n "def create\_app|register\_blueprint|add\_url\_rule|@bp\\.|Blueprint\\(" adapter/http\_reader.py adapter/factory.py engine/http/compat\_handler.py adapter/http\_writer.py  
✅ sed \-n '1,140p' adapter/factory.py; sed \-n '300,980p' adapter/http\_reader.py  
✅ sed \-n '1,260p' engine/sampler/core.py; sed \-n '1,260p' engine/compat/compute.py; sed \-n '1,260p' engine/bodygraph/ingest.py; sed \-n '1,260p' engine/bodygraph/vendor\_client.py; sed \-n '1,220p' adapter/cache\_keys.py; sed \-n '1,220p' engine/runtime/determinism\_env.py  
✅ rg \-n "def compat\_public|def conjunction\_public\_resolved|def band\_for|random|datetime\\.now|time\\.|requests\\.|urllib|open\\(|os\\.urandom|set\\(|dict\\(" engine/compat/compute.py engine/sampler/core.py engine/bodygraph/\*.py engine/provider/\*.py adapter/http\_reader.py  
✅ sed \-n '1,260p' engine/compat/compute.py  
✅ sed \-n '1,260p' engine/bodygraph/resolver.py; sed \-n '1,320p' engine/bodygraph/vendor\_client.py; sed \-n '1,280p' engine/bodygraph/ingest.py; sed \-n '1,240p' engine/db/\_\_init\_\_.py; sed \-n '1,260p' engine/db/access.py  
✅ sed \-n '1,320p' engine/db/adapter.py  
✅ sed \-n '1,260p' engine/presenter/emitter.py; sed \-n '1,220p' presenter/reader\_v1/emitter.py; sed \-n '1,220p' engine/runtime/\_\_init\_\_.py; sed \-n '1,260p' engine/serializer/canon.py  
✅ sed \-n '1,220p' pyproject.toml; sed \-n '1,260p' engine/cli/main.py; sed \-n '260,520p' engine/cli/main.py; sed \-n '520,860p' engine/cli/main.py; sed \-n '860,1080p' engine/cli/main.py; sed \-n '1,120p' scripts/hdctl.py  
✅ rg \-n "def cli\\(|sys\\.exit|raise SystemExit|stdout|stderr|dump\_reader|dump\_admin|add\_parser\\(|set\_defaults\\(|subparsers|return 64|CliError|STDOUT\_MISSING\_LF|STDOUT\_CRLF" engine/cli/main.py  
✅ find .github/workflows \-maxdepth 2 \-type f 2\>/dev/null | sort; rg \-n "run:|name:|check\_env\_pins|run\_sanity\_pipeline|update\_evidence\_index|orientation\_demo|check\_mirror\_schema|check\_release\_identity|pytest|hdctl|generate\_showcompat\_artifacts" .github/workflows ci/checks tools/evidence tools/qa tests \-g '\!docs/pfcanon/\*\*'  
✅ sed \-n '1,120p' docs/evidence/INDEX.json; sed \-n '1,80p' docs/evidence/INDEX.sha256; sed \-n '1,80p' artifacts/evidence\_index.jsonl; sed \-n '1,160p' docs/ENDPOINTS\_CATALOG.json; sed \-n '1,120p' artifacts/audit/ENDPOINTS\_CATALOG.json  
✅ rg \-n "def main|def update|INDEX.json|INDEX.sha256|evidence\_index.jsonl|ENDPOINTS\_CATALOG|path\_proof|write\_text|jsonl" tools/evidence/update\_evidence\_index.py tools/evidence/orientation\_demo.py tools/evidence/run\_sanity\_pipeline.py tools/cli/generate\_showcompat\_artifacts.py tools/evidence/validate\_evidence\_paths.py tools/evidence/check\_lf\_endings.py  
✅ sed \-n '1,240p' tests/http/test\_compat\_endpoint\_contract.py; sed \-n '1,220p' tests/cli/test\_serializer\_guards.py; sed \-n '1,220p' tests/evidence/test\_epic020\_bundle\_index\_integration.py; sed \-n '1,220p' tests/ops/test\_evidence\_index.py; sed \-n '1,200p' tests/test\_reader\_contract.py  
✅ sed \-n '1,260p' .github/workflows/ci.yml  
✅ sed \-n '1,120p' requirements.txt; sed \-n '1,120p' requirements-dev.txt; find . \-maxdepth 2 \-type f \\( \-name 'setup.py' \-o \-name 'setup.cfg' \-o \-name 'pyproject.toml' \-o \-name 'package.json' \\) | sort  
✅ find docs \-maxdepth 2 \-type d | sort | head \-n 40; find artifacts \-maxdepth 2 \-type d | sort | head \-n 60; find audit \-maxdepth 3 \-type d | sort | head \-n 80  
✅ find . \-maxdepth 1 \-type d \-name 'vendor' \-print; rg \-n "def create\_app\\(|app \= Flask\\(\_\_name\_\_\\)|register\_blueprint\\(|@bp\\.route\\(" adapter/http\_reader.py adapter/factory.py; rg \-n "@compat\_blueprint|compat\_blueprint \= Blueprint|before\_app\_request" engine/http/compat\_handler.py; rg \-n "DETERMINISM\_ENV\_PINS|ensure\_determinism\_env" engine/runtime/determinism\_env.py ci/checks/check\_env\_pins.sh  
✅ sed \-n '1,220p' ci/checks/check\_env\_pins.sh; sed \-n '1,220p' tools/evidence/run\_sanity\_pipeline.py; sed \-n '1,220p' tools/cli/generate\_showcompat\_artifacts.py; sed \-n '1,220p' tools/evidence/validate\_evidence\_paths.py  
✅ sed \-n '1,120p' Procfile; sed \-n '1,120p' engine/cli/\_\_main\_\_.py; sed \-n '1,220p' tools/evidence/orientation\_demo.py; sed \-n '1,220p' tools/evidence/update\_evidence\_index.py

* 

