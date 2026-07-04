# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.6

**Status:** Canon

**Effective date:** 2026-07-02

**Last Update Gate:** HDE-EPIC036

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

**Date:** 2026-07-02

## Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2 confirmed by pwd output: /workspace/glow-hdengine-v2.  
* Commit: 369e7b5e3fee05ef012a756241e160c691bb8a6b from git rev-parse HEAD.  
* Working tree cleanliness: git status \--porcelain produced no changed-path output before branch output; working tree observed clean.  
* Branch: work from git rev-parse \--abbrev-ref HEAD.  
* Timestamp UTC: 2026-07-02T13:54:25Z from date \-u \+%Y-%m-%dT%H:%M:%SZ.  
* OS/kernel: Linux eaeac00a6a0b 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 x86\_64 x86\_64 GNU/Linux.  
* Python: Python 3.14.4.  
* Node: v24.15.0.  
* Scope/posture: Read-only architecture audit by static inspection. No code execution, tests, installs, commits, PR, edits, or refactors were performed.

---

## Top-level Repo Map

Top-level listing proof came from find . \-maxdepth 1 \-mindepth 1 \-printf '%f\\n' | sort, which showed these relevant roots/files.

### Expected HD Engine families

* engine/ — Present.  
  * Listing proof: engine appeared in top-level output.  
  * Contains core engine packages, CLI, compatibility compute, sampler, BodyGraph resolver/vendor client, DB adapter, presenter, serializer, runtime, narratives.  
  * Anchors:  
    * engine/compat/compute.py  
    * engine/sampler/core.py  
    * engine/bodygraph/vendor\_client.py  
  * Excerpt proof: find engine ... showed engine/compat/compute.py, engine/sampler/core.py, engine/bodygraph/vendor\_client.py.  
* adapter/ — Present.  
  * Listing proof: adapter appeared in top-level output.  
  * Contains Flask/Wsgi HTTP app assembly, reader blueprint, env guard, cache/ETag helpers, DB access shim files.  
  * Anchors:  
    * adapter/wsgi.py  
    * adapter/http\_reader.py  
    * adapter/app.py  
  * Excerpt proof: find adapter ... showed adapter/wsgi.py, adapter/http\_reader.py, adapter/app.py.  
* presenter/ — Present.  
  * Listing proof: presenter appeared in top-level output.  
  * Contains a root-level reader presenter package and JSON canonical comparison tool, alongside an engine/presenter/ package.  
  * Anchors:  
    * presenter/reader\_v1/emitter.py  
    * presenter/json\_canon\_compare.py  
    * engine/presenter/emitter.py  
  * Excerpt proof: file listing showed presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py, and engine/presenter/emitter.py.  
* CLI package location — Present under engine/cli/.  
  * pyproject.toml:14 declares hdctl \= "engine.cli.main:cli".  
  * File listing showed engine/cli/main.py and engine/cli/\_\_main\_\_.py.  
* docs/ — Present.  
  * Listing proof: docs appeared in top-level output.  
  * Contains evidence index, PF canon, endpoint catalog, acceptance maps, contracts, schemas, ops docs.  
  * Anchors:  
    * docs/evidence/INDEX.json  
    * docs/evidence/INDEX.sha256  
    * docs/ENDPOINTS\_CATALOG.json  
  * Excerpt proof: search output showed tools/evidence/update\_evidence\_index.py:24:HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json" and tests/http/test\_endpoint\_catalog.py:6: catalog \= json.loads(Path("docs/ENDPOINTS\_CATALOG.json")...).  
* artifacts/ — Present.  
  * Listing proof: artifacts appeared in top-level output.  
  * Contains generated/proof-like outputs: CLI captures, BodyGraph proofs, DB bridge snapshots, headers, math/release identity, vendor snapshots, evidence mirror.  
  * Anchors:  
    * artifacts/evidence\_index.jsonl  
    * artifacts/cli/showcompat/  
    * artifacts/vendor/hdapi\_v2/  
  * Excerpt proof: file listing showed artifacts/evidence\_index.jsonl, artifacts/cli/showcompat, and artifacts/vendor/hdapi\_v2.  
* audit/ — Present.  
  * Listing proof: audit appeared in top-level output.  
  * Contains QA/gate/ops/docdelta evidence roots and epic-specific evidence families.  
  * Anchors:  
    * audit/qa/hde-epic036/  
    * audit/gates/json\_gate/  
    * audit/docdeltas/  
  * Excerpt proof: directory listing showed audit/qa/hde-epic036, audit/gates/json\_gate, audit/docdeltas.  
* tools/ — Present.  
  * Listing proof: tools appeared in top-level output.  
  * Contains evidence generators/checkers, CLI guards, ordering, QA harnesses, config tooling.  
  * Anchors:  
    * tools/evidence/update\_evidence\_index.py  
    * tools/evidence/validate\_evidence\_paths.py  
    * tools/cli/serializer\_grep\_guard.py  
  * Excerpt proof: search output showed tools/evidence/update\_evidence\_index.py:24:HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json" and tools/evidence/validate\_evidence\_paths.py:31:def main() \-\> int:.  
* ci/ and .github/ — Present.  
  * Listing proof: both ci and .github appeared in top-level output.  
  * .github/workflows/ci.yml defines GitHub Actions jobs; ci/checks/ contains shell/Python checks.  
  * Anchors:  
    * .github/workflows/ci.yml  
    * ci/checks/check\_env\_pins.sh  
    * ci/checks/check\_mirror\_schema.sh  
  * Excerpt proof: CI output showed .github/workflows/ci.yml with name: ci and steps invoking ci/checks/check\_env\_pins.sh.  
* tests/ — Present.  
  * Listing proof: tests appeared in top-level output.  
  * Contains HTTP, adapter, CLI, QA, evidence, config, transport, compat, ops tests.  
  * Anchors:  
    * tests/http/test\_compat\_endpoint\_contract.py  
    * tests/cli/test\_cli\_canonical\_bytes.py  
    * tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
  * Excerpt proof: search output included those paths and assertions involving endpoint catalogs, SAFE rails, CLI canonical bytes.  
* scripts/ — Present.  
  * Listing proof: scripts appeared in top-level output.  
  * Contains older/auxiliary CLIs, release identity scripts, QA scripts, DB/ops scripts.  
  * Anchors:  
    * scripts/release\_id\_recompute.py  
    * scripts/hd\_cli.py  
    * scripts/bodygraph/run\_refresh\_worker.py  
  * Excerpt proof: search output showed scripts/release\_id\_recompute.py:275: parser \= argparse.ArgumentParser(...), scripts/hd\_cli.py:4:import sys, argparse..., and scripts/bodygraph/run\_refresh\_worker.py:290:if \_\_name\_\_ \== "\_\_main\_\_":.

### Root discipline capture: truth-home-like roots observed

Observed roots that hold governed, generated, canonical, audit, validation, or evidence-like material:

* audit/  
* artifacts/  
* docs/  
* tools/  
* scripts/  
* ci/  
* .github/  
* catalog/  
* schemas/  
* goldens/  
* fixtures/  
* proofs/  
* reports/  
* validation/  
* math/  
* config/  
* narratives/  
* migrations/  
* sql/

Proof: top-level listing included all names above, including audit, artifacts, docs, tools, scripts, ci, .github, catalog, schemas, goldens, fixtures, proofs, reports, validation, math, config, narratives, migrations, and sql.  
---

## Packaging and Entrypoints

### Packaging / build configuration

* pyproject.toml — Present.  
  * Declares setuptools build backend: pyproject.toml excerpt: \[build-system\], requires \= \["setuptools\>=68", "wheel"\], build-backend \= "setuptools.build\_meta".  
  * Declares project package: name \= "glow-hdengine", version \= "0.0.0", requires-python \= "\>=3.10".  
  * Declares console script: pyproject.toml:13:\[project.scripts\]; pyproject.toml:14:hdctl \= "engine.cli.main:cli".  
  * Declares package discovery: pyproject.toml:18:include \= \["engine\*", "adapter\*", "presenter\*"\].  
* requirements.txt and requirements-dev.txt — Present.  
  * Top-level listing showed both requirements.txt and requirements-dev.txt.  
  * CI installs both when present: .github/workflows/ci.yml excerpt: test \-f requirements.txt && python \-m pip install \-r requirements.txt || true and test \-f requirements-dev.txt && python \-m pip install \-r requirements-dev.txt || true.  
* setup.cfg, setup.py, package.json, pnpm-workspace.yaml — Not found.  
  * Negative proof in appendix.

### Entrypoint inventory

* HTTP server startup: adapter/wsgi.py:create\_app.  
  * adapter/wsgi.py:11:def create\_app():  
  * Mounts blueprints: adapter/wsgi.py:23: app.register\_blueprint(reader\_bp) and adapter/wsgi.py:24: app.register\_blueprint(compat\_blueprint).  
  * Role: constructs Flask app, installs logging/env guard, registers reader and compat blueprints, and defines internal health/ready/error handlers.  
* Flask app object: adapter/app.py:app.  
  * Excerpt: from adapter.wsgi import create\_app and app \= create\_app().  
  * Role: exposes app for flask \--app adapter.app run.  
* HTTP reader local factory: adapter/http\_reader.py:create\_app.  
  * adapter/http\_reader.py:944:def create\_app():  
  * adapter/http\_reader.py:948: app.register\_blueprint(bp, url\_prefix="")  
  * adapter/http\_reader.py:954: app.register\_blueprint(compat\_blueprint)  
  * Role: local factory for reader blueprint and compat blueprint.  
* CLI console script: engine.cli.main:cli.  
  * pyproject.toml:14:hdctl \= "engine.cli.main:cli".  
  * engine/cli/main.py:239:def cli(argv: list\[str\] | None \= None) \-\> int:  
  * Role: main hdctl argparse dispatcher.  
* Evidence/index scheduled/background-style entrypoints.  
  * tools/evidence/update\_evidence\_index.py:2408:def main(argv: list\[str\] | None \= None) \-\> None:  
  * tools/evidence/validate\_evidence\_paths.py:31:def main() \-\> int:  
  * CI invokes them: .github/workflows/ci.yml excerpt: python tools/evidence/update\_evidence\_index.py, python tools/evidence/update\_evidence\_index.py \--check, python tools/evidence/orientation\_demo.py \--check, ci/checks/check\_mirror\_schema.sh.

---

## Engine Modules

### Sampler

* engine/sampler/core.py  
  * Classes/functions:  
    * ViewerProfile, CandidateFeatures, SamplerConfig, CandidatePoolEntry, CandidatePool, RankedCandidate, RankedCandidates — dataclasses representing sampler inputs/config/output.  
    * build\_candidate\_pool — engine/sampler/core.py:126:def build\_candidate\_pool(...); filters zero-weight and ineligible candidates into a pool.  
    * rank\_candidates — engine/sampler/core.py:170:def rank\_candidates(...); sorts pool entries deterministically by weight, compatibility score, band priority, and ID.  
    * sample\_and\_rank — helper that builds then ranks.  
  * Determinism excerpt: engine/sampler/core.py:175: \- No randomness, clocks, or external state are consulted.

### Core compute

* engine/compat/compute.py  
  * compat\_public — engine/compat/compute.py:36:def compat\_public(...); builds category compatibility scores and metadata.  
  * AB↔BA normalization: engine/compat/compute.py:40: a1,b1 \= normalize\_pair(a,b).  
  * Pair key use: engine/compat/compute.py:9:from engine.compat.ordering import normalize\_pair, pair\_key.  
  * conjunction\_public — normalizes resolved left/right persons; excerpt: engine/compat/compute.py:82: left, right \= normalize\_pair(left, right).  
  * conjunction\_public\_resolved — engine/compat/compute.py:141:def conjunction\_public\_resolved(...); resolves unresolved users through local lookup and BodyGraph resolver before producing conjunction payload.  
* engine/compat/ordering.py  
  * Referenced by compute and CLI: engine/cli/main.py:23:from engine.compat.ordering import normalize\_pair, pair\_key.  
  * Role evidenced by imports: supplies normalized pair/order helpers used by compatibility and CLI output paths.

### Determinism hazards inventory

Observed hazards in audited engine/adapter paths:

* Current time in adapter process metadata.  
  * adapter/http\_reader.py excerpt from opened file: \_PROCESS\_STARTED\_AT \= datetime.now(timezone.utc).  
  * This value is later emitted by ops probe: payload \= {"pid": \_PROCESS\_PID, "started\_at\_utc": \_PROCESS\_STARTED\_AT...} in adapter/http\_reader.py.  
* Current time / monotonic time in BodyGraph ingest.  
  * engine/bodygraph/ingest.py:125:def ingest\_vendor\_bodygraph(...)  
  * Excerpt: start \= time.monotonic() and \_utc\_iso() uses time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) \+ "Z" in opened file.  
  * Used for duration\_ms and log at fields.  
* Network I/O in vendor client and DB bridge.  
  * engine/bodygraph/vendor\_client.py:491:def fetch(self, request: VendorRequest) \-\> VendorResult:  
  * engine/db/providers/bridge\_provider.py:39: with urllib.request.urlopen(req, timeout=10) as resp.  
  * These are not in sampler/core compute, but are inside engine BodyGraph/DB provider paths.  
* File I/O in BodyGraph ingest and evidence/presenter comparison paths.  
  * engine/bodygraph/ingest.py opened excerpt: \_append\_jsonl(path: Path, record: Mapping\[str, Any\]) writes JSONL logs.  
  * presenter/json\_canon\_compare.py search output showed with path.open("a", encoding="utf-8") as handle.  
* No randomness observed in sampled sampler/core paths.  
  * Reviewed: engine/sampler/core.py, engine/compat/compute.py.  
  * Positive proof: engine/sampler/core.py:175: \- No randomness, clocks, or external state are consulted.  
  * Search output for random in audited engine paths only surfaced the sampler doc statement and historical/test/tool contexts, not random calls in engine/sampler/core.py or engine/compat/compute.py.

---

## Adapter / HTTP Surfaces

### Route registration map

* App creation and mounting: adapter/wsgi.py:create\_app.  
  * adapter/wsgi.py:11:def create\_app():  
  * adapter/wsgi.py:23: app.register\_blueprint(reader\_bp)  
  * adapter/wsgi.py:24: app.register\_blueprint(compat\_blueprint)  
* Reader blueprint: adapter/http\_reader.py.  
  * Route: adapter/http\_reader.py:330:@bp.get("/reader")  
  * POST posture: adapter/http\_reader.py:441:@bp.post("/reader")  
  * Aux narrative routes:  
    * adapter/http\_reader.py:392:@bp.get("/api/aux/narrative")  
    * opened excerpt also showed @bp.get("/aux/narrative").  
  * Ops routes:  
    * adapter/http\_reader.py:469:@bp.route("/ops/db/unavailable", methods=\["GET"\])  
    * adapter/http\_reader.py:514:@bp.route("/ops/rails/refusal", methods=\["GET", "POST"\])  
    * adapter/http\_reader.py:522:@bp.route("/ops/probe/env", methods=\["GET"\])  
    * adapter/http\_reader.py:898:@bp.route("/ops/writer/diagnostic", methods=\["POST"\], provide\_automatic\_options=False)  
* Compat blueprint: engine/http/compat\_handler.py.  
  * Base prefix: engine/http/compat\_handler.py:11:compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1")  
  * Methods:  
    * engine/http/compat\_handler.py:82:@compat\_blueprint.get("")  
    * engine/http/compat\_handler.py:90:@compat\_blueprint.route("", methods=\["POST"\], provide\_automatic\_options=False)  
    * engine/http/compat\_handler.py:130:@compat\_blueprint.route("", methods=\["HEAD"\], provide\_automatic\_options=False)  
    * engine/http/compat\_handler.py:135:@compat\_blueprint.route("", methods=\["OPTIONS"\], provide\_automatic\_options=False)

### Surface classification

* Reader-like JSON success  
  * adapter/http\_reader.py:330:@bp.get("/reader")  
  * Calls emitter function selected by get\_reader\_bp(emit\_fn=None); opened excerpt: if emit\_fn is None: emit\_fn \= emit\_reader\_public\_bytes.  
* Compat API  
  * engine/http/compat\_handler.py:90:def post\_json():  
  * Calls compat\_public(...); opened excerpt: body \= compat\_public(a, b, vp\["top\_category"\], vp\["weights"\], engine\_tag="dev", release\_id="dev", invocation\_tag="INV-DEV").  
* Aux/narrative  
  * adapter/http\_reader.py:392:@bp.get("/api/aux/narrative")  
  * Opened excerpt: route calls get\_pack() and emit\_public\_aux(...), returns text/plain.  
* Admin/internal  
  * adapter/wsgi.py defines:  
    * @app.get("/internal/healthz")  
    * @app.get("/internal/readyz")  
  * Opened excerpt: both emit {"ok": True, "schema": "v1"} through emit\_public.  
* Dev/diagnostic harness  
  * adapter/http\_reader.py:469:@bp.route("/ops/db/unavailable", methods=\["GET"\])  
  * adapter/http\_reader.py:514:@bp.route("/ops/rails/refusal", methods=\["GET", "POST"\])  
  * adapter/http\_reader.py:898:@bp.route("/ops/writer/diagnostic", methods=\["POST"\], provide\_automatic\_options=False)

### Transport semantics hooks

* HEAD vs GET parity: reader.  
  * Opened adapter/http\_reader.py excerpt:  
    * if request.method.upper() \== "HEAD":  
    * resp.headers\["Content-Length"\] \= str(len(body))  
  * Same handler sets empty body with reader headers.  
* Conditional responses / 304: reader.  
  * Opened adapter/http\_reader.py excerpt:  
    * tokens \= \_parse\_if\_none\_match(request.headers.get("If-None-Match"))  
    * if etag in tokens and "\*" not in tokens: resp \= Response(b"", status=304)  
* ETag generation / quoting: reader.  
  * Opened adapter/http\_reader.py excerpt:  
    * etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\""  
    * resp.headers\["ETag"\] \= etag.  
* Cache-control rules.  
  * Reader 200 helper: opened adapter/http\_reader.py excerpt: \_set\_reader\_200\_headers sets Cache-Control to private, max-age=0, must-revalidate.  
  * Writer helper: opened excerpt \_emit\_writer\_response sets resp.headers\["Cache-Control"\] \= "no-store".  
  * WSGI common header: adapter/wsgi.py opened excerpt \_apply\_common\_headers sets default Cache-Control to no-store.  
* Content-Type rules.  
  * Reader helper: opened adapter/http\_reader.py excerpt: resp.headers\["Content-Type"\] \= "application/json; charset=utf-8".  
  * Writer response: opened excerpt \_emit\_writer\_response sets Content-Type to application/json; charset=utf-8.  
  * Aux route uses text: opened excerpt Response(emission.body, status=200, mimetype="text/plain; charset=utf-8").

---

## Presenter / Emitter

* Canonical public JSON emitter: engine/presenter/emitter.py.  
  * engine/presenter/emitter.py:6:def emit\_public(envelope: Dict\[str, Any\], \*, sort\_keys: bool \= True) \-\> bytes:  
  * Excerpt: docstring says Canonical emitter for governed public JSON bytes and Delegates to the canonical serializer (LF-terminated UTF-8).  
  * Also exposes:  
    * engine/presenter/emitter.py:16:def emit\_public\_with\_envelope(...)  
    * emit\_compact\_json(...) in opened file.  
  * Called by:  
    * adapter/http\_reader.py import excerpt: from engine.presenter.emitter import emit\_public  
    * adapter/wsgi.py import excerpt: from engine.presenter.emitter import emit\_public  
    * engine/http/compat\_handler.py import excerpt: from engine.presenter import emit\_public  
    * engine/bodygraph/ingest.py opened excerpt: payload\_bytes, \_ \= emitter.emit\_public\_with\_envelope(vendor\_result.payload).  
* Reader v1 presenter: presenter/reader\_v1/emitter.py.  
  * presenter/reader\_v1/emitter.py:54:def emit\_reader\_v1(enriched: Dict\[str, Any\]) \-\> Tuple\[bytes, Dict\[str, Any\]\]:  
  * Excerpt: public\_bytes are LF-terminated, produced by sercanon.serialize.  
  * It builds idempotence hash: opened excerpt digest \= hashlib.sha256(pre\_bytes).hexdigest() and final\["idempotence\_hash"\] \= digest.  
* Runtime reader emitter path: engine.runtime.emit\_reader\_public\_bytes.  
  * adapter/http\_reader.py opened excerpt imports from engine.runtime import emit\_reader\_public\_bytes.  
  * get\_reader\_bp uses it when no emit\_fn is supplied: opened excerpt if emit\_fn is None: emit\_fn \= emit\_reader\_public\_bytes.  
* Canonical serializer: engine/serializer/canon.py.  
  * Called by engine/presenter/emitter.py: opened excerpt return canon.sercanon(envelope, sort\_keys=sort\_keys).  
  * Output semantics are surfaced through emitter docstring as sorted-key, LF-terminated UTF-8 canonical bytes.

Multiple emitters exist and are distinguishable by usage:

* engine/presenter/emitter.py emits governed public JSON bytes for HTTP/CLI/vendor payloads.  
* presenter/reader\_v1/emitter.py emits reader-v1 envelopes and idempotence hash.  
* presenter/json\_canon\_compare.py is a CLI/tooling comparison emitter/checker; search output showed argparse and append-log behavior.

---

## CLI Surfaces

### Console script

* pyproject.toml:14:hdctl \= "engine.cli.main:cli".  
* Entrypoint: engine/cli/main.py:239:def cli(argv: list\[str\] | None \= None) \-\> int:.

### Parser/subcommands

Search output from engine/cli/main.py:

* engine/cli/main.py:75: prog="hdctl",  
* engine/cli/main.py:85: show \= sub.add\_parser(  
* engine/cli/main.py:133: aux \= sub.add\_parser(  
* engine/cli/main.py:145: bg \= sub.add\_parser(  
* engine/cli/main.py:173: dev\_sampler \= sub.add\_parser(

Relevant command symbols:

* hdctl showcompat  
  * Entrypoint: engine/cli/main.py:674:def showcompat(\_: argparse.Namespace) \-\> int:  
  * Uses canonical stdout: search output engine/cli/main.py:969: sys.stdout.buffer.write(sercanon(payload)).  
  * Pair normalization appears in CLI path: engine/cli/main.py:665: ordered\_people \= list(normalize\_pair(left\_person, right\_person)).  
* hdctl bg:resolve  
  * Entrypoint: engine/cli/main.py:218:def bg\_resolve(args: argparse.Namespace) \-\> int:  
  * Prints output: engine/cli/main.py:235: sys.stdout.write(output).  
  * Calls BodyGraph resolver based on opened imports and symbol name; resolver entrypoint is engine/bodygraph/resolver.py:resolve\_bodygraph.  
* hdctl aux:preview  
  * Entrypoint: engine/cli/main.py:592:def aux\_preview(args: argparse.Namespace) \-\> int:  
  * Output path: engine/cli/main.py:638: sys.stdout.buffer.write(emission.body).  
* hdctl dev:sampler / dev sampler command  
  * Entrypoint: engine/cli/main.py:972:def dev\_sampler\_run(args: argparse.Namespace) \-\> int:  
  * Command parser anchor: engine/cli/main.py:173: dev\_sampler \= sub.add\_parser(.

### CLI output/error behavior

* Writes stdout.  
  * engine/cli/main.py:235: sys.stdout.write(output)  
  * engine/cli/main.py:564: sys.stdout.buffer.write(payload)  
  * engine/cli/main.py:638: sys.stdout.buffer.write(emission.body)  
  * engine/cli/main.py:969: sys.stdout.buffer.write(sercanon(payload))  
* Writes stderr and returns nonzero on usage/error paths.  
  * engine/cli/main.py:245: sys.stderr.write("VERSION\_FLAG\_WITH\_COMMAND\\n")  
  * engine/cli/main.py:246: return 64  
  * engine/cli/main.py:256: parser.print\_usage(sys.stderr)  
  * engine/cli/main.py:257: return 64  
  * engine/cli/main.py:261: sys.stderr.write(f"{err.code}\\n")  
* File-writing CLI/tooling surfaces exist outside hdctl.  
  * Evidence tools write index/proofs: tools/evidence/update\_evidence\_index.py:2456: \_write\_if\_changed(HUMAN\_INDEX, index\_bytes, check=check) and tools/evidence/update\_evidence\_index.py:2459: \_refresh\_path\_proof(HUMAN\_INDEX, default\_produced\_at=produced\_default, check=check).

---

## Vendor Seam & BodyGraph Storage

### Vendor client

* engine/bodygraph/vendor\_client.py  
  * engine/bodygraph/vendor\_client.py:273:class HdApiClient:  
  * engine/bodygraph/vendor\_client.py:359:def build\_request(self, \*, birthdate: str, birthtime: str, location: str) \-\> VendorRequest:  
  * engine/bodygraph/vendor\_client.py:491:def fetch(self, request: VendorRequest) \-\> VendorResult:  
  * Opened file showed vendor dataclasses: VendorRequest, VendorResult, VendorRetryConfig, VendorTimeouts.  
  * Environment rails: engine/bodygraph/vendor\_client.py:153: safe\_mode \= (source.get("SAFE\_MODE") or "").strip() and engine/bodygraph/vendor\_client.py:154: allow\_network \= (source.get("ALLOW\_NETWORK") or "").strip().  
  * Explicit open-rails requirement: engine/bodygraph/vendor\_client.py:749: if safe\_mode \!= "0" or allow\_network \!= "1": and engine/bodygraph/vendor\_client.py:750: raise VendorError("PROVIDER\_REFUSED", ...).  
* Inputs / env names visible  
  * Ingest env inputs: opened engine/bodygraph/ingest.py excerpt missing \= \[name for name in ("INGEST\_TEST\_USER\_ID", "INGEST\_TEST\_BIRTHDATE", "INGEST\_TEST\_BIRTHTIME", "INGEST\_TEST\_LOCATION") ...\].  
  * Base/auth env names are referenced by AGENTS instructions and code search; vendor client config lines in sampled output specifically showed SAFE\_MODE and ALLOW\_NETWORK.

### BodyGraph persistence/caching

* Ingest path: engine/bodygraph/ingest.py.  
  * engine/bodygraph/ingest.py:125:def ingest\_vendor\_bodygraph(...)  
  * Rails gating:  
    * engine/bodygraph/ingest.py:138: safe\_mode \= \_truthy(env.get("SAFE\_MODE"))  
    * engine/bodygraph/ingest.py:139: allow\_network \= \_truthy(env.get("ALLOW\_NETWORK"))  
    * engine/bodygraph/ingest.py:140: if safe\_mode:  
    * engine/bodygraph/ingest.py:142: if not allow\_network:  
  * DB persistence: opened excerpt db \= db\_access or DBAccess.for\_current\_env(), \_persist\_bodygraph(...), \_fetch\_payload(...).  
  * Idempotency key is formed after request fingerprint: opened excerpt idempotency\_key \= \_idempotency\_key(inputs.user\_id, "hdapi", vendor\_version, request.input\_fingerprint).  
* Resolver path: engine/bodygraph/resolver.py.  
  * engine/bodygraph/resolver.py:59: safe\_mode\_closed \= \_truthy(env.get("SAFE\_MODE"))  
  * engine/bodygraph/resolver.py:60: allow\_network \= \_truthy(env.get("ALLOW\_NETWORK"))  
  * engine/bodygraph/resolver.py:108: if safe\_mode\_closed:  
  * engine/bodygraph/resolver.py:118: if not allow\_network:  
  * Role: gates vendor source and returns resolver envelopes.  
* DB access facade: engine/db/adapter.py.  
  * engine/db/adapter.py:112:class DBAccess:  
  * engine/db/adapter.py:128:def for\_current\_env(  
  * Opened excerpt shows provider choice based on DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD.  
* DB bridge provider: engine/db/providers/bridge\_provider.py.  
  * engine/db/providers/bridge\_provider.py:56:class BridgeProvider:  
  * Network call: engine/db/providers/bridge\_provider.py:39: with urllib.request.urlopen(req, timeout=10) as resp  
  * HTTPS requirement opened excerpt: if parsed.scheme \!= "https": raise BridgeUnsupported("bridge\_requires\_https", ...).

### Offline / vendor-required posture

* Explicit closed/open rails posture exists in multiple locations:  
  * engine/bodygraph/ingest.py:140: if safe\_mode: raises provider refusal in opened file.  
  * engine/bodygraph/ingest.py:142: if not allow\_network: raises network blocked in opened file.  
  * engine/bodygraph/vendor\_client.py:749-750 refuses unless SAFE\_MODE=0 and ALLOW\_NETWORK=1.  
  * adapter/http\_reader.py:447-449 derives rails state from SAFE\_MODE and ALLOW\_NETWORK.  
  * .github/workflows/ci.yml sets closed rails: SAFE\_MODE: "1" and ALLOW\_NETWORK: "0".

---

## Evidence, Indices, Catalogs

### Evidence homes inventory

* docs/evidence/  
  * Contains human evidence index and hash sentinel.  
  * Anchors:  
    * docs/evidence/INDEX.json  
    * docs/evidence/INDEX.sha256  
  * Tool proof: tools/evidence/update\_evidence\_index.py:24:HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json" and tools/evidence/update\_evidence\_index.py:25:HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".  
* artifacts/  
  * Contains generated snapshots/logs/proofs across many families.  
  * Directory proof included:  
    * artifacts/cli/showcompat  
    * artifacts/db\_bridge  
    * artifacts/vendor/hdapi\_v2  
    * artifacts/evidence\_index.jsonl  
  * The .path\_proof.txt pattern appears in listing, e.g. artifacts/evidence\_index.jsonl.path\_proof.txt.  
* audit/  
  * Contains QA/gate/ops/doc-delta outputs.  
  * Directory proof included:  
    * audit/gates/json\_gate  
    * audit/gates/evidence\_index\_snapshot  
    * audit/qa/hde-epic027  
    * audit/qa/hde-epic036  
    * audit/ops/hde-epic035  
* catalog/  
  * Present in top-level listing.  
  * AGENTS says catalog/manifest.json is freeze-pack SoT; top-level listing showed catalog.  
* schemas/, docs/schemas/, adapter/schemas/  
  * Present by top-level/file listing.  
  * Examples: adapter/schemas/error\_v1.schema.json, docs/schemas/core, schemas.

### Evidence index structures

* docs/evidence/INDEX.json  
  * Tool constants: tools/evidence/update\_evidence\_index.py:24:HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json".  
  * Read path: tools/evidence/update\_evidence\_index.py:2131: payload \= json.loads(HUMAN\_INDEX.read\_text(encoding="utf-8")).  
  * Write path: tools/evidence/update\_evidence\_index.py:2456: \_write\_if\_changed(HUMAN\_INDEX, index\_bytes, check=check).  
* docs/evidence/INDEX.sha256  
  * Tool constant: tools/evidence/update\_evidence\_index.py:25:HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".  
  * CI check: ci/checks/check\_evidence\_index\_hash.sh output showed it checks docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
* artifacts/evidence\_index.jsonl  
  * Listing proof: artifacts/evidence\_index.jsonl, artifacts/evidence\_index.jsonl.path\_proof.txt, artifacts/evidence\_index.jsonl.sha256.  
  * AGENTS and CI both treat this as mirror; CI invokes ci/checks/check\_mirror\_schema.sh.  
* Regeneration/validation tooling  
  * tools/evidence/update\_evidence\_index.py  
  * tools/evidence/orientation\_demo.py  
  * tools/evidence/validate\_evidence\_paths.py  
  * ci/checks/check\_mirror\_schema.sh  
  * ci/checks/check\_evidence\_index\_hash.sh  
  * CI excerpt invokes all of the above.

### Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * Referenced by tests: tests/http/test\_endpoint\_catalog.py:6: catalog \= json.loads(Path("docs/ENDPOINTS\_CATALOG.json").read\_text(encoding="utf-8")).  
  * Also referenced by compat endpoint tests: tests/http/test\_compat\_endpoint\_contract.py:32: catalog \= json.loads(Path("docs/ENDPOINTS\_CATALOG.json").read\_text(encoding="utf-8")).  
* artifacts/audit/ENDPOINTS\_CATALOG.json  
  * Listing proof: artifacts/audit/ENDPOINTS\_CATALOG.json and .sha256.  
  * Role from filename/path: audit mirror/snapshot of endpoint catalog.

### Proof / snapshot artifacts

Observed proof/snapshot families from listings:

* Reader/header transport snapshots:  
  * artifacts/headers/reader\_200.json  
  * artifacts/headers/reader\_304.json  
  * artifacts/headers/reader\_head\_304.json  
  * artifacts/headers/headers\_HEAD.json  
* Reader A7 success proofs:  
  * Test producer proof: tests/http/test\_reader\_a7\_transport.py:131: proof\_dir / "success\_get.txt" and tests/http/test\_reader\_a7\_transport.py:136: proof\_dir / "success\_head.txt".  
* Showcompat/CLI:  
  * artifacts/cli/showcompat/  
  * artifacts/showcompat/epic024/  
* Vendor HDAPI v2:  
  * artifacts/vendor/hdapi\_v2/  
* DB/BodyGraph:  
  * artifacts/bodygraph/  
  * artifacts/db\_bridge/  
  * artifacts/db/

---

## Tests, QA Harness, CI/Checks

### Tests map

* HTTP/compat endpoint tests  
  * tests/http/test\_compat\_endpoint\_contract.py  
  * Excerpts:  
    * Reads catalog: tests/http/test\_compat\_endpoint\_contract.py:32: catalog \= json.loads(Path("docs/ENDPOINTS\_CATALOG.json")...).  
    * SAFE rails expectations: tests/http/test\_compat\_endpoint\_contract.py:216: env={"SAFE\_MODE": "1", "ALLOW\_NETWORK": "0"}.  
  * Role: exercises compat/conjunction HTTP contract, catalog references, rails behavior.  
* Reader transport tests  
  * tests/http/test\_reader\_a7\_transport.py  
  * Producer anchors: success\_get.txt and success\_head.txt lines from search output.  
  * Role: records/validates reader GET/HEAD transport proofs.  
* CLI canonical/output tests  
  * tests/cli/test\_cli\_canonical\_bytes.py  
  * Search output showed closed rails env setup: SAFE\_MODE: "1", ALLOW\_NETWORK: "0".  
  * Role: CLI canonical byte behavior.  
* Showcompat tests  
  * tests/cli/test\_showcompat\_sources.py  
  * Search output includes open/closed rails env setup at lines with SAFE\_MODE and ALLOW\_NETWORK.  
  * Role: showcompat source behavior.  
* Evidence/index/catalog tests  
  * tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
  * tests/ops/test\_evidence\_index.py  
  * tests/config/test\_registry\_report\_indexing.py  
  * Excerpts:  
    * tests/config/test\_registry\_report\_indexing.py:12: index \= json.loads(Path("docs/evidence/INDEX.json")...)  
    * tests/evidence/test\_hdapi\_v2\_contract\_inventory.py contains boundary checks for adapter/presenter/vendor source patterns.  
* QA harness tests  
  * tests/qa/test\_epic021\_harness\_entrypoint.py  
  * CI excerpt runs it: python \-m pytest tests/qa/test\_epic021\_harness\_entrypoint.py.

### CI workflows

* .github/workflows/ci.yml  
  * Workflow: name: ci.  
  * Main job env:  
    * LC\_ALL: C  
    * LANG: C  
    * TZ: UTC  
    * SAFE\_MODE: "1"  
    * ALLOW\_NETWORK: "0"  
  * Main job commands include:  
    * ci/checks/check\_env\_pins.sh  
    * ci/checks/check\_cli\_help.sh  
    * python tools/cli/serializer\_grep\_guard.py  
    * python tools/cli/emitter\_symbol\_proof.py  
    * python tools/evidence/run\_canonical\_json\_gate.py  
    * python tools/evidence/update\_evidence\_index.py  
    * python tools/evidence/update\_evidence\_index.py \--check  
    * python tools/evidence/orientation\_demo.py \--check  
    * ci/checks/check\_evidence\_index\_hash.sh  
    * ci/checks/check\_mirror\_schema.sh  
    * ci/checks/check\_final\_lf.sh  
    * multiple python \-m pytest ... invocations.  
* Other named jobs observed:  
  * compat-conj-pr01-closure  
  * epic020  
  * compat-http-epic020  
  * epic020-evidence-bundles  
  * sanity-pipeline  
  * Proof: CI output showed these job keys/names and commands.

### Script/check inventory

QA-relevant scripts/checks observed:

* ci/checks/check\_env\_pins.sh — CI invokes it before test/check lanes; role: determinism env pins gate.  
* ci/checks/check\_evidence\_index\_hash.sh — excerpt checks docs/evidence/INDEX.json and docs/evidence/INDEX.sha256.  
* ci/checks/check\_mirror\_schema.sh — CI invokes after evidence index updates.  
* ci/checks/check\_final\_lf.sh — CI invokes final LF check.  
* tools/evidence/update\_evidence\_index.py — constants/read/write paths for human index and hash sentinel.  
* tools/evidence/validate\_evidence\_paths.py — def main() \-\> int; role: evidence path validation.  
* tools/evidence/orientation\_demo.py — comments mention INDEX/mirror/proofs coherence.  
* tools/evidence/run\_sanity\_pipeline.py — CI sanity-pipeline job runs it.  
* tools/cli/serializer\_grep\_guard.py and tools/cli/emitter\_symbol\_proof.py — CI invokes as CLI serializer/emitter guards.  
* scripts/release\_id\_recompute.py — argparse release-id recompute script; search output showed parser definition.  
* scripts/bodygraph/run\_refresh\_worker.py — background/worker-like BodyGraph script; search output showed time.time() and if \_\_name\_\_ \== "\_\_main\_\_".

---

## Flows & Call Chains

### 1\. Reader success flow HTTP

adapter/wsgi.py:create\_app → adapter/http\_reader.py:reader\_v1 → engine.runtime.emit\_reader\_public\_bytes → engine.presenter.emitter.emit\_public / reader emitter → Flask Response

* Mount proof: adapter/wsgi.py:23: app.register\_blueprint(reader\_bp).  
* Route proof: adapter/http\_reader.py:330:@bp.get("/reader").  
* Runtime emitter proof: opened excerpt if emit\_fn is None: emit\_fn \= emit\_reader\_public\_bytes.  
* ETag proof: opened excerpt etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"".  
* Output proof: opened excerpt resp \= Response(body, status=200) plus Content-Type, Cache-Control, Content-Length.

### 2\. Compat API flow HTTP

adapter/wsgi.py:create\_app → engine/http/compat\_handler.py:post\_json → engine.compat.compute.compat\_public → engine.presenter.emit\_public → Flask Response

* Mount proof: adapter/wsgi.py:24: app.register\_blueprint(compat\_blueprint).  
* Prefix proof: engine/http/compat\_handler.py:11:compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
* POST proof: engine/http/compat\_handler.py:90:@compat\_blueprint.route("", methods=\["POST"\], provide\_automatic\_options=False).  
* Engine proof: opened excerpt body \= compat\_public(...).  
* Presenter proof: opened excerpt \_writer\_payload calls payload \= emit\_public(env).

### 3\. CLI showcompat / compat preview flow

pyproject.toml:hdctl → engine/cli/main.py:cli → engine/cli/main.py:showcompat → engine.compat.ordering.normalize\_pair / compat payload construction → sercanon(payload) → sys.stdout.buffer.write(...)

* Entrypoint proof: pyproject.toml:14:hdctl \= "engine.cli.main:cli".  
* CLI proof: engine/cli/main.py:239:def cli(argv: list\[str\] | None \= None) \-\> int:.  
* Command proof: engine/cli/main.py:674:def showcompat(\_: argparse.Namespace) \-\> int:.  
* Ordering proof: engine/cli/main.py:665: ordered\_people \= list(normalize\_pair(left\_person, right\_person)).  
* Output proof: engine/cli/main.py:969: sys.stdout.buffer.write(sercanon(payload)).

### 4\. Vendor acquisition / BodyGraph ingest flow

engine/bodygraph/resolver.py:resolve\_bodygraph → engine/bodygraph/ingest.py:ingest\_vendor\_bodygraph → engine/bodygraph/vendor\_client.py:HdApiClient.build\_request → HdApiClient.fetch → engine/db/adapter.py:DBAccess.for\_current\_env → DB provider persist/fetch → logs/artifacts

* Resolver rails proof: engine/bodygraph/resolver.py:59-60 reads SAFE\_MODE and ALLOW\_NETWORK.  
* Ingest proof: engine/bodygraph/ingest.py:125:def ingest\_vendor\_bodygraph(...).  
* Ingest rails proof: engine/bodygraph/ingest.py:138-142 reads and gates SAFE\_MODE / ALLOW\_NETWORK.  
* Vendor request proof: engine/bodygraph/vendor\_client.py:359:def build\_request(...).  
* Vendor fetch proof: engine/bodygraph/vendor\_client.py:491:def fetch(...).  
* DB proof: engine/db/adapter.py:128:def for\_current\_env(.  
* Output/log proof: opened ingest excerpt writes SUCCESS\_LOG \= INGEST\_DIR / "ingest\_success.log" and RETRY\_LOG \= INGEST\_DIR / "retry\_trace.log".

### 5\. Evidence index update/validation flow

tools/evidence/update\_evidence\_index.py:main → read docs/evidence/INDEX.json → write docs/evidence/INDEX.json / INDEX.sha256 / path proofs → CI check\_evidence\_index\_hash.sh / check\_mirror\_schema.sh / validate\_evidence\_paths.py

* Tool constants: tools/evidence/update\_evidence\_index.py:24:HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json".  
* Hash sentinel: tools/evidence/update\_evidence\_index.py:25:HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".  
* Read proof: tools/evidence/update\_evidence\_index.py:2131: payload \= json.loads(HUMAN\_INDEX.read\_text(encoding="utf-8")).  
* Write proof: tools/evidence/update\_evidence\_index.py:2456: \_write\_if\_changed(HUMAN\_INDEX, index\_bytes, check=check).  
* Path proof refresh: tools/evidence/update\_evidence\_index.py:2459: \_refresh\_path\_proof(HUMAN\_INDEX, default\_produced\_at=produced\_default, check=check).  
* CI proof: .github/workflows/ci.yml runs update, check, orientation, mirror schema, hash check.

### 6\. Aux/narrative HTTP flow

adapter/wsgi.py:create\_app → adapter/http\_reader.py:aux\_narrative → engine.narratives.get\_pack / emit\_public\_aux → text Flask Response

* Route proof: adapter/http\_reader.py:392:@bp.get("/api/aux/narrative").  
* Opened excerpt also shows @bp.get("/aux/narrative").  
* Narrative calls: opened excerpt pack \= get\_pack() and emission \= emit\_public\_aux(...).  
* Output proof: opened excerpt Response(emission.body, status=200, mimetype="text/plain; charset=utf-8").  
* Headers proof: opened excerpt sets X-Narrative-Pack-Sha, X-Narrative-Composition, X-Narrative-Key.

---

## Drift and Reality vs Expectations

### Directory/architecture drift

* Observed: Presenter code exists both as root presenter/ and as engine/presenter/.  
  * Proof anchor: file listing showed presenter/reader\_v1/emitter.py, presenter/json\_canon\_compare.py, and engine/presenter/emitter.py.  
  * Impact: This creates factual ambiguity about whether “presenter” means the root package, the engine subpackage, or both in call-chain discussions.  
* Observed: CLI implementation lives under engine/cli/, while additional CLI-like scripts exist under scripts/.  
  * Proof anchor: pyproject.toml:14:hdctl \= "engine.cli.main:cli" and search output showed scripts/hd\_cli.py:4:import sys, argparse....  
  * Impact: This creates ambiguity about canonical versus legacy/auxiliary CLI surfaces unless the packaging entrypoint is used as the anchor.

### Surface drift

* Observed: HTTP compat route is implemented under engine/http/compat\_handler.py, while app mounting lives in adapter/wsgi.py.  
  * Proof anchor: engine/http/compat\_handler.py:11:compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1"); adapter/wsgi.py:24: app.register\_blueprint(compat\_blueprint).  
  * Impact: The adapter/HTTP surface spans both adapter/ and engine/http/.  
* Observed: Reader blueprint includes reader, aux narrative, ops, and writer/diagnostic routes in the same file.  
  * Proof anchor: adapter/http\_reader.py:330:@bp.get("/reader"), adapter/http\_reader.py:392:@bp.get("/api/aux/narrative"), adapter/http\_reader.py:469:@bp.route("/ops/db/unavailable", methods=\["GET"\]), adapter/http\_reader.py:898:@bp.route("/ops/writer/diagnostic", methods=\["POST"\], provide\_automatic\_options=False).  
  * Impact: This creates ambiguity about route-family separation by file.

### Evidence drift

* Observed: Evidence/proof outputs are spread across docs/, artifacts/, audit/, and additional roots such as catalog/, proofs/, reports/, goldens/, and validation/.  
  * Proof anchor: top-level listing and evidence directory listing showed docs/evidence, artifacts/evidence\_index.jsonl, audit/gates, catalog, proofs, reports, goldens, validation.  
  * Impact: This creates ambiguity about evidence-home boundaries without consulting the governing index/tooling.

### Determinism drift

* Observed: Deterministic sampler/core paths coexist with time/network/file I/O paths in adjacent engine/adapter areas.  
  * Proof anchor: engine/sampler/core.py:175: \- No randomness, clocks, or external state are consulted. versus engine/db/providers/bridge\_provider.py:39: with urllib.request.urlopen(req, timeout=10) as resp and engine/bodygraph/ingest.py:138-142 rails-gated ingest.  
  * Impact: This creates ambiguity if “engine” is discussed as one uniform purity boundary rather than by subpackage.

### Vendor seam drift

* Observed: Vendor seam lives under engine/bodygraph/vendor\_client.py, and DB bridge network provider also lives under engine/db/providers/bridge\_provider.py.  
  * Proof anchor: engine/bodygraph/vendor\_client.py:273:class HdApiClient: and engine/db/providers/bridge\_provider.py:56:class BridgeProvider:.  
  * Impact: Vendor/network seams are inside engine/ subpackages rather than outside engine/ as a fully separate top-level vendor adapter root.

### Path-case drift

* Observed: Most epic QA roots sampled are lowercase hyphenated paths such as audit/qa/hde-epic036; root/top-level includes mixed/uppercase files such as AGENTS.md, README.md, AcceptanceMap.md, CANON\_CHECKSUMS.json, and Run.  
  * Proof anchor: top-level listing showed AGENTS.md, AcceptanceMap.md, CANON\_CHECKSUMS.json, Run; audit listing showed audit/qa/hde-epic036.  
  * Impact: Case conventions differ between documentation/root files and QA/evidence roots.

### Root proliferation

* Observed: At least 16 truth-home-like roots were observed: audit/, artifacts/, docs/, tools/, scripts/, ci/, .github/, catalog/, schemas/, goldens/, fixtures/, proofs/, reports/, validation/, math/, config/.  
  * Proof anchor: top-level listing included all listed roots.  
  * Impact: This creates ambiguity about where a reviewer should start when tracing governed outputs unless anchored to index/tooling.

### Alignment summary table

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package exists | Aligned | top-level engine; engine/compat/compute.py, engine/sampler/core.py |
| Adapter package exists | Aligned | top-level adapter; adapter/wsgi.py:11:def create\_app() |
| Presenter split exists | Partial | root presenter/reader\_v1/emitter.py and engine/presenter/emitter.py:6:def emit\_public |
| CLI package location | Aligned | pyproject.toml:14:hdctl \= "engine.cli.main:cli" |
| Vendor seam outside core compute | Partial | vendor seam in engine/bodygraph/vendor\_client.py; compute in engine/compat/compute.py |
| Evidence layout | Partial | docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, audit/qa/... |
| Determinism gates | Aligned for CI/rails | .github/workflows/ci.yml sets SAFE\_MODE: "1" and ALLOW\_NETWORK: "0"; ingest/vendor refuse closed rails |

---

## Negative-Claim Proof Appendix

* setup.cfg not found  
  * Search method/scope: shell existence check at repo root: \[ \-e setup.cfg \].  
  * Result: setup.cfg NOT\_FOUND.  
* setup.py not found  
  * Search method/scope: shell existence check at repo root: \[ \-e setup.py \].  
  * Result: setup.py NOT\_FOUND.  
* package.json not found  
  * Search method/scope: shell existence check at repo root: \[ \-e package.json \].  
  * Result: package.json NOT\_FOUND.  
* pnpm-workspace.yaml not found  
  * Search method/scope: shell existence check at repo root: \[ \-e pnpm-workspace.yaml \].  
  * Result: pnpm-workspace.yaml NOT\_FOUND.

