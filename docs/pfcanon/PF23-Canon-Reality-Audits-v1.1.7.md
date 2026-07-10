# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.7

**Status:** Canon

**Effective date:** 2026-07-07

**Last Update Gate:** HDE-EPIC037

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

**Date:** 2026-07-07

## Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2 confirmed by pwd output (/workspace/glow-hdengine-v2).  
* Commit: 78676daca5771b3d779850866689370e04ce59a5 (git rev-parse HEAD).  
* Working tree cleanliness: dirty. git status \--porcelain output showed changed path only:  
  * work  
* Branch: work (git rev-parse \--abbrev-ref HEAD).  
* Timestamp UTC: 2026-07-07T12:56:49Z (date \-u \+%Y-%m-%dT%H:%M:%SZ).  
* Execution environment:  
  * OS/kernel: Linux 06ec3756b321 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 x86\_64 x86\_64 GNU/Linux  
  * Python: Python 3.14.4  
  * Node: v24.15.0

Scope/posture for this audit: read-only static inspection; no code execution, tests, installs, edits, refactors, or design proposals.  
---

## Top-level Repo Map

Top-level listing proof came from find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort.

### Expected HD Engine families

* engine/ — Present.  
  * Listing proof: top-level output included engine.  
  * Contains engine packages for bodygraph, CLI, compat, DB, HTTP compat handler, narratives, presenter, runtime, sampler, serializer.  
  * Anchors: engine/compat/compute.py, engine/sampler/core.py, engine/bodygraph/vendor\_client.py.  
* adapter/ — Present.  
  * Listing proof: top-level output included adapter.  
  * Contains Flask app factories, WSGI app, reader HTTP blueprint, DB/env guards, ETag/cache helpers.  
  * Anchors: adapter/wsgi.py, adapter/http\_reader.py, adapter/factory.py.  
* presenter/ — Present as a top-level package, and engine/presenter/ also exists.  
  * Listing proof: top-level output included presenter; file listing showed engine/presenter/emitter.py.  
  * Top-level presenter/reader\_v1/emitter.py builds Reader v1 envelopes; engine/presenter/emitter.py delegates canonical public bytes to serializer.  
  * Anchors: presenter/reader\_v1/emitter.py, engine/presenter/emitter.py.  
* CLI package location — Present under engine/cli/; top-level cli/ not found.  
  * Proof: pyproject declares hdctl \= "engine.cli.main:cli".  
  * Anchors: engine/cli/main.py, engine/cli/\_\_main\_\_.py.  
  * Negative claim for top-level cli/: see Negative-Claim Proof Appendix.  
* docs/ — Present.  
  * Listing proof: top-level output included docs.  
  * Contains PF canon docs, acceptance maps, endpoint catalog, evidence index, schemas, ops docs.  
  * Anchors: docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, docs/ENDPOINTS\_CATALOG.json.  
* artifacts/ — Present.  
  * Listing proof: top-level output included artifacts.  
  * Contains generated-looking evidence families, proofs, logs, snapshots, CLI captures, vendor artifacts, DB bridge artifacts, sampler/core evidence.  
  * Anchors: artifacts/evidence\_index.jsonl, artifacts/vendor/hdapi\_v2/, artifacts/cli/showcompat/.  
* audit/ — Present.  
  * Listing proof: top-level output included audit.  
  * Contains QA, ops, gate, docdelta, manifest/close-pack evidence homes.  
  * Anchors: audit/qa/hde-epic037/, audit/gates/json\_gate/, audit/ops/hde-epic037/.  
* tools/ — Present.  
  * Listing proof: top-level output included tools.  
  * Contains evidence generators/validators and QA close-pack/harness scripts.  
  * Anchors: tools/evidence/update\_evidence\_index.py, tools/evidence/validate\_evidence\_paths.py, tools/qa/run\_hde\_epic024\_harness.py.  
* ci/ and .github/ — Present.  
  * Listing proof: top-level output included both ci and .github.  
  * ci/checks/ and ci/jobs/ contain shell/YAML checks; .github/workflows/ exists.  
  * Anchors: ci/checks/check\_mirror\_schema.sh, ci/checks/check\_evidence\_index\_hash.sh, .github/workflows/.  
* tests/ — Present.  
  * Listing proof: top-level output included tests.  
  * Contains audit/evidence/engine/HTTP/CLI-oriented tests; sampled listing showed tests/audit/, tests/evidence/.  
  * Anchors: tests/evidence/test\_evidence\_skeleton.py, tests/evidence/test\_sanity\_evidence\_index.py, tests/audit/test\_epic017\_manifest.py.  
* scripts/ — Present.  
  * Listing proof: top-level output included scripts.  
  * Contains release/config/dev helper scripts; pyproject search found root requirements plus scripts directory in top-level map.  
  * Anchors: scripts/release\_id\_recompute.py, scripts/dev\_start\_reader.sh if present in tree expectations from AGENTS text.

### Other notable top-level roots

* catalog/ — freeze-pack manifest home; AGENTS references catalog/manifest.json.  
* config/, schemas/, sql/, migrations/ — configuration/schema/database roots.  
* fixtures/, goldens/ — fixture/golden-data roots.  
* narratives/ — narrative content root.  
* parity/, proofs/, reports/, validation/, scan\_reports/ — evidence/report-like roots.  
* Root-level transient/report files observed: .body200.json, .code304.txt, .tmp\_refusal\_get.txt, .tmp\_refusal\_post.txt, big.json, patch.diff, multiple hde-epic023\_\_...step\_report.md.

Root discipline capture — truth/governed-output-looking homes observed at top level: audit/, artifacts/, docs/, catalog/, tools/, scripts/, ci/, .github/, proofs/, reports/, parity/, validation/, goldens/, fixtures/, schemas/, sql/, migrations/.  
---

## Packaging and Entrypoints

### Packaging / build configuration

* pyproject.toml  
  * Proof: \[project\] name \= "glow-hdengine" and \[project.scripts\] hdctl \= "engine.cli.main:cli".  
  * Declares package discovery for engine\*, adapter\*, presenter\* via \[tool.setuptools.packages.find\] include \= \["engine\*", "adapter\*", "presenter\*"\].  
  * Declares no runtime dependencies: dependencies \= \[\].  
* requirements.txt, requirements-dev.txt  
  * Present by packaging search output.  
* setup.py, setup.cfg  
  * Not found in packaging search output. See Negative-Claim Proof Appendix.  
* Workspace/monorepo manager config:  
  * No package.json found by find . \-maxdepth 2 ... \-name package.json; no workspace manager config observed in sampled packaging search.

### Entrypoint inventory

* HTTP server startup:  
  * adapter/wsgi.py:create\_app  
    * Proof: adapter/wsgi.py:11 def create\_app():; lines 12–19 create Flask app and register reader\_bp and compat\_blueprint.  
    * Role: primary WSGI Flask factory with common headers and health/readiness/internal errors.  
  * adapter/wsgi.py:app  
    * Proof: adapter/wsgi.py ends with app \= create\_app().  
    * Role: module-level WSGI app object.  
  * adapter/factory.py:create\_app  
    * Proof: lines 4–7 create Flask app and register bp.  
    * Role: smaller Flask factory mounting adapter.http\_reader.bp at root.  
  * adapter/http\_reader.py:create\_app  
    * Proof: symbol listing showed adapter/http\_reader.py:944:def create\_app() and adapter/http\_reader.py:994:if \_\_name\_\_ \== "\_\_main\_\_":.  
    * Role: reader module local app factory/main path.  
* CLI console script:  
  * engine.cli.main:cli  
    * Proof: pyproject.toml declares hdctl \= "engine.cli.main:cli"; engine/cli/main.py:239 def cli(argv: list\[str\] | None \= None) \-\> int.  
    * Role: argparse dispatcher for showcompat, aux-preview, bg:resolve, and dev:sampler.  
  * engine/cli/\_\_main\_\_.py:main  
    * Proof: symbol listing showed engine/cli/\_\_main\_\_.py:8:def main() and engine/cli/\_\_main\_\_.py:14:if \_\_name\_\_ \== "\_\_main\_\_":.  
    * Role: module execution wrapper for CLI.  
* Evidence/indexing jobs:  
  * tools/evidence/update\_evidence\_index.py  
    * Proof: lines 23–28 define ROOT, HUMAN\_INDEX, HASH\_SENTINEL, MIRROR\_PATH, MIRROR\_SHA\_PATH.  
    * Role: hardens/writes/checks human evidence index, hash sentinel, and machine mirror.  
  * ci/checks/check\_mirror\_schema.sh  
    * Proof from grep output: references artifacts/evidence\_index.jsonl and prints MISSING:artifacts/evidence\_index.jsonl.  
    * Role: CI schema/order check for mirror.  
  * ci/checks/check\_evidence\_index\_hash.sh  
    * Proof from grep output: checks docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
    * Role: CI hash sentinel check.

---

## Engine Modules

### Sampler

* engine/sampler/core.py  
  * Primary classes:  
    * ViewerProfile — proof: class at line 31; stores person\_uid and optional top category.  
    * CandidateFeatures — line 39; normalized candidate state.  
    * SamplerConfig — line 52; sampler thresholds/filters/priority.  
    * CandidatePoolEntry, CandidatePool, RankedCandidate, RankedCandidates — lines 63–90; pool/ranked result data structures.  
  * Primary functions:  
    * build\_candidate\_pool — line 126; comment says it constructs pool after eligibility and zero-weight filtering.  
    * rank\_candidates — line 170; docstring says it sorts by weight, compat score, band priority, ID tie-breaker.  
    * sample\_and\_rank — line 196; helper that builds pool then ranks.  
  * Determinism proof: rank\_candidates docstring says “No randomness, clocks, or external state are consulted.”

### Core compute / compatibility

* engine/compat/compute.py  
  * compat\_public  
    * Proof: function returns categories plus meta; code comment says \# AB↔BA identity by normalization; calls normalize\_pair(a,b) and pair\_key(a1,b1).  
    * Role: computes deterministic compatibility categories/scores/bands/keys from two people and viewer prefs.  
  * \_score\_for  
    * Proof: comment says “Base (0..100) from stable hash of (pair\_key, category)” and uses hashlib.sha256.  
    * Role: stable per-category scoring.  
  * conjunction\_public / conjunction\_public\_resolved  
    * Proof: conjunction\_public\_resolved docstring lists local lookup, closed rails refusal, open rails acquisition, local-cache behavior.  
    * Role: resolves conjunction parties and emits conjunction compatibility payload.  
* engine/compat/ordering.py  
  * Referenced by compute.py import: normalize\_pair, pair\_key.  
  * Role based on import/call: AB/BA pair normalization and pair-key creation.  
* engine/serializer/canon.py  
  * Proof: docstring says canonical serializer uses UTF-8 bytes, ensure\_ascii=False, sorted keys by default, compact separators, exactly one trailing newline.  
  * Role: canonicalization at public JSON boundary.  
* engine/presenter/emitter.py  
  * Proof: emit\_public delegates to canon.sercanon(envelope, sort\_keys=sort\_keys).  
  * Role: governed public JSON byte emitter.

### Determinism hazards inventory

Observed hazards in engine/bodygraph acquisition paths, not in sampler/compat pure compute paths:

* Current time / monotonic duration:  
  * engine/bodygraph/vendor\_client.py  
    * Proof: imports time; defines \_now\_ms() \-\> time.monotonic() \* 1000.0 and \_utc\_iso(...).  
    * Factual scope: vendor logging/timing support.  
  * engine/bodygraph/ingest.py  
    * Proof: lines 144 and 153 use start \= time.monotonic() and compute duration\_ms.  
    * Factual scope: ingest timing fields in logs/outcome.  
* Network calls:  
  * engine/bodygraph/ingest.py  
    * Proof: line 147 calls vendor\_result \= client.fetch(request).  
  * engine/bodygraph/vendor\_client.py  
    * Proof: imports urllib.request as urlrequest; class HdApiClient exists.  
* File I/O:  
  * engine/bodygraph/ingest.py  
    * Proof: INGEST\_DIR \= Path("artifacts/ingest"); \_append\_jsonl writes logs; lines 154–165 append success log in dry-run path.  
* DB I/O:  
  * engine/bodygraph/ingest.py  
    * Proof: lines 243–244 call db.tx(\[stmt\]); lines 252–259 call db.query(...).  
* Randomness:  
  * engine/providers/vendor\_http\_hdapi.py  
    * Proof: fallback ensure\_cid imports secrets and returns "CID-" \+ secrets.token\_hex(8) if no CID matches.  
    * Factual scope: provider HTTP request shaping fallback.

No randomness/clocks/network/file I/O observed in sampled engine/sampler/core.py or engine/compat/compute.py; reviewed paths: engine/sampler/core.py, engine/compat/compute.py, engine/serializer/canon.py, engine/presenter/emitter.py.  
---

## Adapter / HTTP Surfaces

### Route registration map

* App factory: adapter/wsgi.py:create\_app  
  * Proof: line 12 app \= Flask(\_\_name\_\_); lines 18–19 app.register\_blueprint(reader\_bp) and app.register\_blueprint(compat\_blueprint).  
  * Mounted groups:  
    * adapter.http\_reader.bp — no prefix in adapter/wsgi.py.  
    * engine.http.compat\_handler.compat\_blueprint — blueprint has url\_prefix="/api/compat/v1" in engine/http/compat\_handler.py:11.  
* Compat routes:  
  * Base path: /api/compat/v1  
  * Proof: compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
  * Handlers:  
    * get\_ids\_only — @compat\_blueprint.get("").  
    * post\_json — @compat\_blueprint.route("", methods=\["POST"\]).  
    * post\_json\_head — HEAD.  
    * post\_json\_options — OPTIONS.  
* Reader/internal/dev routes:  
  * adapter/http\_reader.py:get\_reader\_bp  
    * Proof: docstring says factory returns blueprint exposing /reader.  
    * Handler: reader\_v1 at @bp.get("/reader").  
  * adapter/http\_reader.py:bp module-level routes:  
    * /internal/version — proof: @bp.route("/internal/version", methods=\["GET", "HEAD"\]).  
    * /ops/writer/diagnostic — proof: POST/HEAD/OPTIONS decorators.  
    * /internal/dev/sampler — proof: @bp.route("/internal/dev/sampler", methods=\["POST"\]).

### Surface classification

* Reader-like JSON success:  
  * adapter/http\_reader.py:reader\_v1  
  * Proof: requires v=1, APP\_ENV=dev, loads a/b chart paths, emits emit\_fn(...), sets ETag and Reader headers.  
* Compat API/internal admin:  
  * engine/http/compat\_handler.py:post\_json, get\_ids\_only  
  * Proof: POST rejects prod with ERR\_NOT\_FOUND; GET returns {"ok": True, "schema": "v1"}.  
* Admin/internal:  
  * adapter/wsgi.py:internal\_healthz, internal\_readyz  
  * Proof: @app.get("/internal/healthz"), @app.get("/internal/readyz").  
  * adapter/http\_reader.py:internal\_version  
  * Proof: @bp.route("/internal/version", methods=\["GET", "HEAD"\]).  
* Dev/diagnostic harness:  
  * adapter/http\_reader.py:dev\_sampler\_internal  
  * Proof: route /internal/dev/sampler; docstring says “Dev-only sampler harness”.  
  * adapter/http\_reader.py:diagnostic\_writer  
  * Proof: /ops/writer/diagnostic POST/HEAD/OPTIONS.

### Transport semantics hooks

* HEAD vs GET parity:  
  * adapter/http\_reader.py:reader\_v1  
    * Proof: code block says \# HEAD parity; returns empty body with Content-Length equal to body length.  
  * adapter/http\_reader.py:internal\_version  
    * Proof: route methods include \["GET", "HEAD"\].  
  * engine/http/compat\_handler.py  
    * Proof: \_compat\_writer\_transport\_guard intercepts HEAD for /api/compat/v1; post\_json\_head returns \_writer\_head\_response().  
* Conditional 304:  
  * adapter/http\_reader.py:reader\_v1  
    * Proof: code block says \# 304: strong match, empty body, CL 0/absent; checks If-None-Match tokens.  
* ETag generation:  
  * adapter/http\_reader.py:reader\_v1  
    * Proof: etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"".  
* Cache-control:  
  * adapter/wsgi.py:\_apply\_common\_headers  
    * Proof: sets Cache-Control to no-store.  
  * engine/http/compat\_handler.py:\_writer\_payload  
    * Proof: sets resp.headers\["Cache-Control"\] \= "no-store".  
* Content-Type:  
  * adapter/wsgi.py:\_apply\_common\_headers  
    * Proof: sets Content-Type to application/json; charset=utf-8.  
  * engine/http/compat\_handler.py:\_writer\_payload  
    * Proof: creates Response(..., mimetype="application/json; charset=utf-8").

---

## Presenter / Emitter

* engine/presenter/emitter.py  
  * Functions: emit\_public, emit\_public\_with\_envelope, emit\_compact\_json.  
  * Proof: emit\_public docstring says “Canonical emitter for governed public JSON bytes”; delegates to canon.sercanon.  
  * Called by:  
    * HTTP compat: engine/http/compat\_handler.py imports from engine.presenter import emit\_public.  
    * WSGI app: adapter/wsgi.py imports from engine.presenter.emitter import emit\_public.  
    * CLI: engine/cli/main.py imports from engine.presenter import emitter.  
    * Bodygraph ingest: engine/bodygraph/ingest.py imports from engine.presenter import emitter.  
* engine/serializer/canon.py  
  * Function: sercanon.  
  * Proof: docstring lists canonical JSON rules: UTF-8 bytes, sorted keys by default, compact separators, exactly one trailing newline.  
  * Role: canonical serializer under engine presenter.  
* presenter/reader\_v1/emitter.py  
  * Function: emit\_reader\_v1.  
  * Proof: docstring says returns (public\_bytes, final\_envelope\_dict) and public bytes are LF-terminated.  
  * Role: Reader v1 envelope construction with category dedupe/sort and idempotence hash.  
  * Calls engine.presenter.emitter.emit\_public.  
* Multiple emitters exist:  
  * engine/presenter/emitter.py — general canonical public JSON bytes.  
  * presenter/reader\_v1/emitter.py — Reader v1 envelope-specific wrapper adding idempotence\_hash.  
  * engine/serializer/canon.py — canonical serializer layer used by the general emitter.

---

## CLI Surfaces

* Console script:  
  * hdctl  
  * Proof: pyproject.toml \[project.scripts\] hdctl \= "engine.cli.main:cli".  
* Parser:  
  * engine/cli/main.py:\_build\_parser  
  * Proof: lines 73–190 build argparse parser and subcommands.  
  * Subcommands:  
    * showcompat  
      * Proof: sub.add\_parser("showcompat", ...).  
      * Args include \--pair-file, \--a-file, \--b-file, aliases \--a, \--b, \--dump-reader, \--dump-admin-dir, \--source {db,vendor,auto}, \--conjunction, viewer prefs, user and birth fields.  
    * aux-preview  
      * Proof: parser adds aux-preview with \--category, \--band, \--perspective, \--pair-file, \--show-narrative, \--admin-out.  
    * bg:resolve  
      * Proof: parser adds bg:resolve; \--user is required; \--source choices are auto, db, vendor; includes \--upsert, \--dry-run, birth args.  
    * dev:sampler  
      * Proof: parser adds dev:sampler; \--viewer and \--candidates-file are required; optional \--seed.  
* Exit behavior:  
  * Missing/invalid args:  
    * Proof: cli() catches SystemExit from argparse and returns 64 if code else 0\.  
  * CLI typed errors:  
    * Proof: except CliError as err: sys.stderr.write(f"{err.code}\\n"); return err.exit\_code.  
* Output surfaces:  
  * Stdout:  
    * Proof: bg\_resolve writes sys.stdout.write(output).  
    * Proof: \_emit\_stdout\_bytes writes sys.stdout.buffer.write(payload).  
  * File writes:  
    * Proof: \_dump\_reader\_bytes creates parent dirs and writes bytes to target path.  
    * Proof: \_emit\_admin\_dumps writes admin proof JSON via canon\_dump(admin\_dir / ...).  
  * LF/CRLF guard:  
    * Proof: \_emit\_stdout\_bytes raises STDOUT\_MISSING\_LF if payload lacks LF and STDOUT\_CRLF if CRLF present.  
* High-level call chains:  
  * showcompat: engine/cli/main.py:cli → showcompat → compat\_public / conjunction\_public\_resolved → emitter/\_emit\_stdout\_bytes.  
  * bg:resolve: cli → bg\_resolve → engine.bodygraph.resolver.resolve\_bodygraph → engine.presenter.emitter.emit\_public → stdout.  
  * dev:sampler: cli → dev\_sampler\_run → sample\_and\_rank → \_emit\_sampler\_output.

---

## Vendor Seam & BodyGraph Storage

### Vendor client

* engine/bodygraph/vendor\_client.py  
  * Symbols: HdApiClient, VendorRequest, VendorResult, VendorRetryConfig, VendorTimeouts, VendorError, classify\_bg\_resolve\_route\_policy, route\_auth\_posture, join\_vendor\_resource\_url.  
  * Proof: \_\_all\_\_ exports these names.  
  * Inputs/config keys:  
    * HD\_API\_BASE\_URL, HDAPI\_BASE\_URL — proof: \_resolve\_hdapi\_base\_url reads both and errors if both differ.  
    * Route auth posture includes HD API key vs bearer posture; proof: \_ROUTE\_CONTRACTS maps bodygraphs to hd\_api\_key, charts to bearer.  
* engine/bodygraph/ingest.py  
  * Symbol: ingest\_vendor\_bodygraph.  
  * Proof: lines 125–147 gate SAFE/network, build client/request, fetch vendor result.  
  * Inputs/env:  
    * SAFE\_MODE, ALLOW\_NETWORK — proof: lines 137–143.  
    * INGEST\_TEST\_USER\_ID, INGEST\_TEST\_BIRTHDATE, INGEST\_TEST\_BIRTHTIME, INGEST\_TEST\_LOCATION — proof: gather\_inputs\_from\_env.  
* engine/bodygraph/resolver.py  
  * Symbol: resolve\_bodygraph.  
  * Proof: docstring says resolution control-flow primitives for CLI and ops surfaces.  
  * Inputs/env:  
    * SAFE\_MODE, ALLOW\_NETWORK, HD\_API\_BASE\_URL, HDAPI\_BASE\_URL — proof: CLI \_resolver\_env() returns these names; resolver classifies route policy from vendor env.  
* engine/providers/vendor\_http\_hdapi.py  
  * Symbol: prepare\_hdapi\_request.  
  * Proof: docstring says shapes HDAPI request without network I/O; reads HD\_API\_KEY, GEO\_API\_KEY, HDAPI\_BASE\_URL.  
  * Note: file contains multiple redefinitions of prepare\_hdapi\_request; final definition in Python file is authoritative by normal module execution order, but this audit records only that multiple same-name definitions exist.

### BodyGraph persistence/caching

* engine/bodygraph/ingest.py  
  * Persists to SQL table:  
    * Proof: \_persist\_bodygraph SQL inserts into hde.body\_graphs (user\_id, vendor, vendor\_version, input\_fingerprint, payload).  
  * Reads row count:  
    * Proof: \_row\_count queries SELECT COUNT(\*) FROM hde.body\_graphs WHERE user\_id \= %s AND vendor \= %s AND vendor\_version \= %s AND input\_fingerprint \= %s.  
  * Fetches stored payload:  
    * Proof: \_fetch\_payload queries SELECT payload::text FROM hde.body\_graphs.  
  * Cache/idempotency key:  
    * Proof: \_idempotency\_key returns f"{user\_id}:{vendor}:{vendor\_version}:{fingerprint}".  
* engine/cli/main.py:\_fetch\_db\_bodygraph  
  * Proof: SQL reads from hde.body\_graphs\_current WHERE user\_id \= %s ORDER BY vendor\_version DESC LIMIT 1\.  
  * Role: CLI DB-source bodygraph lookup.  
* engine/db/adapter.py:DBAccess  
  * Proof: class docstring says “High-level façade exposing DB operations across providers.”  
  * Provider selection:  
    * Reads DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD.  
    * Writes snapshot to artifacts/db\_bridge/adapter\_selection.snapshot.json by default.

### Offline / vendor-required posture

* engine/bodygraph/resolver.py  
  * Proof: \_resolve\_vendor returns PROVIDER\_REFUSED when safe mode is closed and PROVIDER\_NETWORK\_BLOCKED when network not allowed.  
* engine/bodygraph/ingest.py  
  * Proof: lines 140–143 raise VendorError("PROVIDER\_REFUSED", ...) and VendorError("PROVIDER\_NETWORK\_BLOCKED", ...).  
* engine/providers/vendor\_http.py  
  * Symbol listing showed \_safe\_mode\_enabled and VendorHttpProvider.  
  * Role: provider-level SAFE\_MODE posture exists in vendor provider package.

---

## Evidence, Indices, Catalogs

### Evidence homes inventory

* docs/evidence/  
  * Contains INDEX.json, INDEX.sha256, path proofs per AGENTS expectations.  
  * Appears generated/mixed: index content is machine-shaped JSON with artifact\_key, discovered\_physical\_path, sha256, tokens.  
* artifacts/  
  * Contains many generated-looking subfamilies: artifacts/evidence\_index.jsonl, artifacts/vendor/hdapi\_v2/, artifacts/cli/showcompat/, artifacts/sanity/, artifacts/proofs/, artifacts/db\_bridge/, artifacts/ops/internal\_version/.  
  * Appears generated/mixed: .jsonl, .sha256, .path\_proof.txt, .snapshot.json, logs.  
* audit/  
  * Contains audit/qa/hde-epic0xx/, audit/ops/, audit/gates/, manifests and close reports.  
  * Appears generated/mixed: close reports and token matrices are docs-like; per-check logs/gates are generated-looking.  
* catalog/  
  * AGENTS identifies catalog/manifest.json as freeze-pack source of truth.  
* reports/, proofs/, parity/, validation/, goldens/  
  * Evidence/report-like roots observed in top-level listing.

### Evidence index structures

* docs/evidence/INDEX.json  
  * Proof: exists, size 117238; first record includes keys artifact\_key, discovered\_physical\_path, epic\_id, notes, produced\_at\_utc, record\_type, schema\_version, sha256, size\_bytes, tokens.  
  * Tooling:  
    * tools/evidence/update\_evidence\_index.py defines HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json".  
    * Tests reference it extensively, e.g. tests/evidence/test\_evidence\_skeleton.py, tests/evidence/test\_sanity\_evidence\_index.py.  
* docs/evidence/INDEX.sha256  
  * Proof: tools/evidence/update\_evidence\_index.py defines HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".  
  * CI:  
    * ci/checks/check\_evidence\_index\_hash.sh checks docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
* artifacts/evidence\_index.jsonl  
  * Proof: exists; tools/evidence/update\_evidence\_index.py defines MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl".  
  * CI:  
    * ci/checks/check\_mirror\_schema.sh reads artifacts/evidence\_index.jsonl.  
* artifacts/evidence\_index.jsonl.sha256  
  * Proof: tools/evidence/update\_evidence\_index.py defines MIRROR\_SHA\_PATH.

### Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * Proof: exists, size 1749; JSON has top-level endpoints and success\_endpoints.  
  * Shape summary:  
    * Entries include path, method, classification, blueprint\_module, description, env\_gate, rails\_profile, a7\_eligible.  
    * Paths listed include /api/compat/v1, /dev/reader/conjunction, /dev/writer/conjunction, /dev/sampler/conjunction, /internal/version, /reader.  
  * Referenced by tooling/tests:  
    * tools/qa/generate\_epic028\_acceptance\_ledger.py references docs/ENDPOINTS\_CATALOG.json.  
    * tools/qa/generate\_epic027\_close\_pack.py references it.  
    * tools/evidence/generate\_hde\_epic037\_v2\_adapter.py references it.

### Proof / snapshot artifacts

Examples observed in index/catalog/tool references:

* artifacts/proofs/success\_get.txt, artifacts/proofs/success\_head.txt, artifacts/proofs/success\_304.txt  
  * Producer/reference proof: tools/qa/generate\_epic027\_close\_pack.py text references “D3 reader/endpoint family” with those paths.  
* artifacts/ops/internal\_version/body\_get.json, headers\_get.txt, headers\_head.txt, headers\_cond\_if\_none\_match.txt  
  * Proof: docs/evidence/INDEX.json records these under INTVER\_\*.  
* artifacts/vendor/hdapi\_v2/\*.snapshot.json  
  * Proof: top-level directory listing included artifacts/vendor/hdapi\_v2; AGENTS and grep references list snapshot artifacts.  
* audit/gates/json\_gate/canonical/  
  * Proof: directory listing included audit/gates/json\_gate; AGENTS names canonical JSON gate files.

---

## Tests, QA Harness, CI/Checks

### Tests map

Test roots observed by listing:

* tests/audit/  
  * Examples from grep output:  
    * tests/audit/test\_epic017\_manifest.py references artifacts/evidence\_index.jsonl.  
    * tests/audit/test\_epic020\_acceptance\_bundle\_wiring.py references docs/evidence/INDEX.json.  
* tests/evidence/  
  * Examples:  
    * tests/evidence/test\_evidence\_skeleton.py asserts docs/evidence/INDEX.json hash sentinel and artifacts/evidence\_index.jsonl.  
    * tests/evidence/test\_sanity\_evidence\_index.py checks sanity log presence in index/mirror.  
    * tests/evidence/test\_hdapi\_v2\_contract\_inventory.py, test\_hdapi\_v2\_live\_conformance.py, test\_hdapi\_v2\_response\_normalization.py reference HDAPI v2 evidence and index/mirror coverage.  
* Other tests exist under tests/ but were not fully enumerated in the final output; sampled command listed test paths and grep hits for evidence/index behavior.

Categories based on filenames/paths only:

* Evidence/contract: tests/evidence/\*.  
* Audit/manifest: tests/audit/\*.  
* Unit/integration labels: not consistently inferred unless encoded in file path/name; this audit does not relabel unlabeled tests.

### CI workflows/checks

* .github/workflows/  
  * Directory exists by find .github/workflows ci \-type f.  
* ci/checks/check\_mirror\_schema.sh  
  * Proof: grep output shows it reads artifacts/evidence\_index.jsonl and emits MISSING:artifacts/evidence\_index.jsonl.  
  * Role: mirror schema/order validation.  
* ci/checks/check\_evidence\_index\_hash.sh  
  * Proof: grep output shows it checks docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
  * Role: evidence index hash sentinel validation.  
* ci/checks/check\_final\_lf.sh  
  * Proof: grep output shows it checks docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl.  
  * Role: final-LF discipline check.  
* ci/checks/check\_env\_pins.sh  
  * Mentioned in AGENTS as determinism env pin gate; path family exists under ci/checks.

### QA-relevant scripts

* tools/evidence/update\_evidence\_index.py  
  * Proof: docstring says hardens evidence index, hash sentinel, and machine mirror.  
* tools/evidence/validate\_evidence\_paths.py  
  * AGENTS names it as evidence path validation entrypoint.  
* tools/evidence/orientation\_demo.py  
  * AGENTS names it as orientation demo/index proof entrypoint.  
* tools/evidence/run\_sanity\_pipeline.py  
  * AGENTS names it as deterministic sanity pipeline.  
* tools/evidence/run\_canonical\_json\_gate.py  
  * AGENTS names it as canonical JSON gate producer.  
* tools/qa/run\_hde\_epic024\_harness.py  
  * Grep output shows it references docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl and writes/validates EPIC024 evidence.  
* tools/qa/generate\_epic027\_close\_pack.py  
  * Grep output shows it references endpoint catalog, index, mirror, and proof artifacts.  
* scripts/release\_id\_recompute.py  
  * AGENTS identifies it as release identity recompute gate.

---

## Flows & Call Chains

### 1\. Reader success flow HTTP

adapter/wsgi.py:create\_app → adapter.http\_reader.bp / get\_reader\_bp → adapter/http\_reader.py:reader\_v1 → emit\_reader\_public\_bytes/emit\_fn → ETag/cache headers → Response

* Start proof: adapter/wsgi.py registers reader\_bp.  
* Handler proof: adapter/http\_reader.py:get\_reader\_bp docstring says exposes /reader.  
* Input proof: reader\_v1 requires v=1, a, b, optional a\_tz, b\_tz.  
* Transport proof: ETag is quoted SHA-256 of body; 304 and HEAD handling are explicitly coded.  
* Output proof: returns Response(body, status=200) and sets Content-Length.

### 2\. Compat API flow HTTP

adapter/wsgi.py:create\_app → engine.http.compat\_handler.compat\_blueprint → post\_json → normalize\_viewer\_prefs/validate\_viewer\_prefs → engine.compat.compute.compat\_public → engine.presenter.emit\_public → Response

* Start proof: adapter/wsgi.py registers compat\_blueprint.  
* Prefix proof: compat\_blueprint has url\_prefix="/api/compat/v1".  
* Handler proof: post\_json reads a, b, a\_id, b\_id.  
* Engine proof: post\_json calls compat\_public(...).  
* Presenter proof: \_writer\_payload calls emit\_public(env).  
* Output proof: JSON response with Cache-Control: no-store, no ETag, explicit content length.

### 3\. CLI showcompat / compat preview flow

pyproject.toml hdctl → engine/cli/main.py:cli → \_build\_parser/showcompat → \_load\_from\_source or files/stdin → compat\_public or conjunction\_public\_resolved → emitter.emit\_public / \_emit\_stdout\_bytes → stdout and optional dumps

* Entrypoint proof: hdctl \= "engine.cli.main:cli".  
* Parser proof: showcompat parser defines file/stdin/source/conjunction args.  
* Output proof: \_emit\_stdout\_bytes writes to sys.stdout.buffer.  
* File proof: \_dump\_reader\_bytes writes optional Reader bytes; \_emit\_admin\_dumps writes admin proofs.  
* Error proof: missing args become exit 64 via argparse catch or CliError.

### 4\. Vendor acquisition / BodyGraph ingest flow

engine/cli/main.py:bg\_resolve → engine.bodygraph.resolver.resolve\_bodygraph → \_resolve\_vendor → HdApiClient.from\_env/build\_request/fetch OR v2 chart adapter path → engine.bodygraph.ingest.ingest\_vendor\_bodygraph → DBAccess.tx/query → logs/artifacts

* Start proof: bg\_resolve calls resolve\_bodygraph(...).  
* Rails proof: resolver refuses vendor when SAFE\_MODE closed or network disabled.  
* Vendor proof: ingest\_vendor\_bodygraph calls client.fetch(request).  
* Persistence proof: \_persist\_bodygraph inserts into hde.body\_graphs.  
* Cache/idempotency proof: \_idempotency\_key uses user\_id:vendor:vendor\_version:fingerprint.

### 5\. Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py → HUMAN\_INDEX/docs/evidence/INDEX.json → HASH\_SENTINEL/docs/evidence/INDEX.sha256 → MIRROR\_PATH/artifacts/evidence\_index.jsonl → MIRROR\_SHA\_PATH/artifacts/evidence\_index.jsonl.sha256 → ci/checks/check\_mirror\_schema.sh / check\_evidence\_index\_hash.sh

* Start proof: script docstring says it hardens evidence index, hash sentinel, and machine mirror.  
* Path proof: lines 23–28 define all four canonical paths.  
* CI proof: grep output shows mirror schema check reads artifacts/evidence\_index.jsonl.  
* Hash proof: grep output shows evidence index hash check reads docs/evidence/INDEX.json and INDEX.sha256.

### 6\. Dev sampler flow

engine/cli/main.py:cli → dev\_sampler\_run → \_load\_candidates\_from\_path → engine.sampler.core.sample\_and\_rank → \_emit\_sampler\_output → stdout

* Parser proof: dev:sampler requires \--viewer and \--candidates-file.  
* Engine proof: dev\_sampler\_run calls sample\_and\_rank(viewer, candidates).  
* Sampler proof: sample\_and\_rank builds candidate pool then ranks.  
* Determinism proof: rank\_candidates docstring says no randomness, clocks, or external state.

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: presenter code exists in both engine/presenter/ and top-level presenter/.  
  * Proof anchor: file listing showed engine/presenter/emitter.py and presenter/reader\_v1/emitter.py.  
  * Impact: creates ambiguity about whether “presenter” means engine-internal emitter or top-level Reader-specific presenter.  
* Observed: CLI exists under engine/cli/, not top-level cli/.  
  * Proof anchor: pyproject.toml maps hdctl to engine.cli.main:cli; top-level cli directory not found.  
  * Impact: CLI architecture is engine-package-local rather than separate top-level package.

### Surface drift

* Observed: endpoint catalog lists /dev/reader/conjunction, /dev/writer/conjunction, /dev/sampler/conjunction, while sampled route grep did not show these route decorators in adapter/http\_reader.py; catalog references them as adapter.http\_reader.  
  * Proof anchor: docs/ENDPOINTS\_CATALOG.json first line includes those paths; route grep output showed /internal/dev/sampler, /internal/version, /ops/writer/diagnostic, /reader, /api/compat/v1.  
  * Impact: creates ambiguity between cataloged dev conjunction paths and sampled route decorators.  
* Observed: compat route is under engine/http/compat\_handler.py rather than adapter/.  
  * Proof anchor: compat\_blueprint \= Blueprint(... url\_prefix="/api/compat/v1") in engine/http/compat\_handler.py.  
  * Impact: adapter/HTTP responsibilities span both adapter/ and engine/http/.

### Evidence drift

* Observed: evidence-like homes exist across many top-level roots: audit/, artifacts/, docs/, proofs/, reports/, parity/, validation/, goldens/, root-level step reports.  
  * Proof anchor: top-level listing output includes all named roots/files.  
  * Impact: creates ambiguity about governed vs auxiliary output homes without consulting index/path-proof rules.

### Determinism drift

* Observed: pure sampler/compat sampled paths are deterministic by code comments and hash/sort usage, while bodygraph vendor/ingest paths use clocks, network, DB, and file logs.  
  * Proof anchor: engine/sampler/core.py docstring says no randomness/clocks/external state; engine/bodygraph/ingest.py uses time.monotonic, client.fetch, \_append\_jsonl, db.tx.  
  * Impact: determinism posture differs by layer: compute/sampler is pure; acquisition/ingest is side-effectful under rail gates.

### Vendor seam drift

* Observed: vendor-related code exists in multiple places: engine/bodygraph/vendor\_client.py, engine/bodygraph/ingest.py, engine/providers/vendor\_http\_hdapi.py, engine/providers/vendor\_http.py.  
  * Proof anchor: file listing and symbol grep show vendor client, ingest, and provider shapers.  
  * Impact: creates ambiguity about the single vendor seam unless call chain is followed per surface.

### Path-case drift

* Observed: audit QA paths sampled are lowercase epic homes like audit/qa/hde-epic031/, but root contains mixed-case report filenames such as HDE-EPIC023\_\_...md, EPIC023\_D12\_close\_pack\_manifest\_FINAL\_EVIDENCE.md.  
  * Proof anchor: top-level listing output includes mixed-case root reports and lowercase audit/qa/hde-epic0xx directories.  
  * Impact: path-case conventions differ between root reports and governed QA homes.

### Root proliferation

* Observed: at least 14 truth/evidence-looking roots: audit/, artifacts/, docs/, catalog/, tools/, scripts/, ci/, .github/, proofs/, reports/, parity/, validation/, goldens/, fixtures/.  
  * Proof anchor: top-level listing output.  
  * Impact: reviewers need index/mirror/path-proof context to distinguish governed evidence from supporting files.

### Alignment summary

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package | Aligned | engine/compat/compute.py, engine/sampler/core.py exist |
| Adapter / HTTP app | Partial | adapter/wsgi.py mounts reader and compat; compat handler lives in engine/http/compat\_handler.py |
| Presenter / emitter | Partial | engine/presenter/emitter.py plus presenter/reader\_v1/emitter.py |
| CLI | Partial | console script exists as hdctl; package is engine/cli, no top-level cli/ |
| Vendor seam outside compute | Partial | vendor code in engine/bodygraph/\* and engine/providers/\*; compute imports resolver for conjunction acquisition path |
| DB/cache | Aligned/partial | engine/db/adapter.py and SQL in engine/bodygraph/ingest.py; CLI also queries hde.body\_graphs\_current |
| Evidence layout | Drift/partial | canonical index/mirror exist, but many evidence-like top-level homes also exist |

---

## Negative-Claim Proof Appendix

* Top-level cli/ directory not found.  
  * Searched token/path: cli  
  * Method: find . \-maxdepth 1 \-type d \-name 'cli' \-print | wc \-l  
  * Scope: repo root top-level directories  
  * Result: 0  
* setup.py not found in packaging search.  
  * Searched token/path: setup.py  
  * Method: find . \-maxdepth 2 \\( \-name 'pyproject.toml' \-o \-name 'setup.cfg' \-o \-name 'setup.py' \-o \-name 'requirements\*.txt' \-o \-name 'package.json' \\) \-print | sort  
  * Scope: repo root, max depth 2  
  * Result: no setup.py line in output  
* setup.cfg not found in packaging search.  
  * Searched token/path: setup.cfg  
  * Method: same packaging find command above  
  * Scope: repo root, max depth 2  
  * Result: no setup.cfg line in output  
* package.json not found in packaging search.  
  * Searched token/path: package.json  
  * Method: same packaging find command above  
  * Scope: repo root, max depth 2  
  * Result: no package.json line in output  
* engine/adapter directory not found.  
  * Searched token/path: engine/adapter  
  * Method: \[ \-e "engine/adapter" \] check in combined negative proof command  
  * Scope: repo root  
  * Result: engine/adapter NOTFOUND  
* Cataloged /dev/reader/conjunction route decorator not found in sampled route grep.  
  * Searched token/path: route decorators and route-registration tokens via grep \-R "@app\\.route\\|add\_url\_rule\\|Blueprint\\|FastAPI\\|Flask\\|APIRouter\\|route(" \-n engine adapter presenter run\_flask.py  
  * Scope: engine, adapter, presenter, run\_flask.py  
  * Result: route grep output did not include /dev/reader/conjunction; catalog contains it in docs/ENDPOINTS\_CATALOG.json

---

Read-only checks/commands run:

* ✅ pwd; git rev-parse HEAD; git status \--porcelain; git rev-parse \--abbrev-ref HEAD; date \-u \+%Y-%m-%dT%H:%M:%SZ; uname \-a; python \--version 2\>&1 || true; node \--version 2\>&1 || true  
* ✅ find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort  
* ✅ find . \-maxdepth 2 \\( \-name 'pyproject.toml' \-o \-name 'setup.cfg' \-o \-name 'setup.py' \-o \-name 'requirements\*.txt' \-o \-name 'package.json' \\) \-print | sort  
* ✅ find engine app api docs artifacts audit tools ci tests scripts .github \-maxdepth 2 \-type d 2\>/dev/null | sort | head \-200  
* ✅ sed \-n '1,220p' pyproject.toml; find engine \-maxdepth 3 \-type f | sort | head \-200; find adapter presenter \-maxdepth 3 \-type f 2\>/dev/null | sort | head \-120  
* ✅ grep \-R "@app\\.route\\|add\_url\_rule\\|Blueprint\\|FastAPI\\|Flask\\|APIRouter\\|route(" \-n engine adapter presenter run\_flask.py 2\>/dev/null | head \-200  
* ✅ sed \-n / nl \-ba static source inspections of adapter/wsgi.py, adapter/factory.py, adapter/http\_reader.py, engine/http/compat\_handler.py, engine/cli/main.py, engine/compat/compute.py, engine/sampler/core.py, engine/presenter/emitter.py, presenter/reader\_v1/emitter.py, engine/serializer/canon.py, engine/bodygraph/resolver.py, engine/bodygraph/vendor\_client.py, engine/bodygraph/ingest.py, engine/db/adapter.py, tools/evidence/update\_evidence\_index.py  
* ✅ grep \-R "^def \\|^class \\|if \_\_name\_\_ \== .\_\_main\_\_." \-n adapter engine tools/evidence ci/checks scripts tests 2\>/dev/null | head \-300  
* ✅ find .github/workflows ci \-type f | sort | head \-200  
* ✅ find tests \-maxdepth 3 \-type f | sort | head \-200  
* ✅ grep \-R "INDEX.json\\|evidence\_index.jsonl\\|ENDPOINTS\_CATALOG" \-n tools ci tests docs adapter engine .github 2\>/dev/null | head \-200

