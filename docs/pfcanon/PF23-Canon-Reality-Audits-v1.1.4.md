# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.1.4

**Status:** Canon

**Effective date:** 2026-06-25

**Last Update Gate:** HDE-EPIC034

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

**Date:** 2026-06-25

**Last Epic:** HDE-EPIC034

# Audit Snapshot Metadata

* Repo root: /workspace/glow-hdengine-v2; confirmed by pwd and git rev-parse \--show-toplevel, both output /workspace/glow-hdengine-v2.  
* Commit: ac2d0a40ee98f8356ded6416f0053eb648444267 (git rev-parse HEAD).  
* Working tree cleanliness: clean; git status \--porcelain produced no path lines.  
* Branch: work (git rev-parse \--abbrev-ref HEAD).  
* Timestamp UTC: 2026-06-25T03:13:19Z (date \-u \+%Y-%m-%dT%H:%M:%SZ).  
* Execution environment:  
  * OS/kernel: Linux 8ff59f5e65f8 6.12.47 \#1 SMP Mon Oct 27 10:01:15 UTC 2025 x86\_64 ... (uname \-a).  
  * Python: Python 3.14.4 (python \--version).  
  * Node: v24.15.0 (node \--version).

Scope/posture used: read-only static inspection. No code execution, package install, tests, edits, commits, or PR creation were performed.  
---

# Top-level Repo Map

## Top-level paths observed

Repo listing output showed these notable roots/files at top level: .github, adapter, artifacts, audit, catalog, ci, config, docs, engine, fixtures, migrations, narratives, presenter, proofs, pyproject.toml, pytest.ini, requirements-dev.txt, requirements.txt, run\_flask.py, scripts, sql, tests, tools, plus many reports/backups such as \_archive, \_backup\_\*.tgz, and hde-epic023\_\_...step\_report.md.

## Expected HD Engine families

* engine/ — Present.  
  * Listing proof: engine present 90 files.  
  * Contains engine packages for compatibility, sampler, CLI, DB, bodygraph, runtime, serializer, presenter, narratives, provider/vendor seams.  
  * Anchors:  
    * engine/compat/compute.py  
    * engine/sampler/core.py  
    * engine/cli/main.py  
* adapter/ — Present.  
  * Listing proof: adapter present 17 files.  
  * Contains Flask app factories, reader HTTP surface, DB access helpers, WSGI entrypoint, env/no-IO guards.  
  * Anchors:  
    * adapter/wsgi.py  
    * adapter/http\_reader.py  
    * adapter/factory.py  
* presenter/ — Present at root, and also engine/presenter/.  
  * Listing proof: top-level presenter; directory summary: presenter present 4 files.  
  * Engine package also contains engine/presenter/emitter.py.  
  * Anchor: engine/presenter/emitter.py excerpt: def emit\_public(envelope: Dict\[str, Any\], \*, sort\_keys: bool \= True) \-\> bytes:.  
* CLI package location(s) — Present under engine/cli/; scripts also present under scripts/.  
  * Packaging proof: pyproject.toml declares hdctl \= "engine.cli.main:cli".  
  * Listing proof: engine/cli/main.py, engine/cli/\_\_main\_\_.py, scripts/hdctl.py, scripts/hd\_cli.py.  
  * Anchors:  
    * engine/cli/main.py  
    * scripts/hdctl.py  
    * scripts/hd\_cli.py  
* docs/ — Present.  
  * Listing proof: docs present 100 files.  
  * Contains endpoint catalog, evidence index, acceptance maps, run/docs files.  
  * Anchors:  
    * docs/ENDPOINTS\_CATALOG.json  
    * docs/evidence/INDEX.json  
    * docs/acceptance\_map\_epic034.json  
* artifacts/ — Present.  
  * Listing proof: artifacts present 439 files.  
  * Contains generated/proof-like outputs, evidence mirror, audit headers, CLI/showcompat artifacts, vendor contract artifacts.  
  * Anchors:  
    * artifacts/evidence\_index.jsonl  
    * artifacts/audit/http/reader\_get\_headers.txt  
    * artifacts/vendor/hdapi\_v2/endpoint\_reference.csv  
* audit/ — Present.  
  * Listing proof: audit present 122 files.  
  * Contains manifests, close reports, QA logs, token matrices, gates.  
  * Anchors:  
    * audit/EPIC-034\_READ\_ONLY\_REPO\_READINESS\_AUDIT.md  
    * audit/EPIC-030\_MANIFEST.json  
    * audit/qa/hde-epic034/...  
* tools/ — Present.  
  * Listing proof: tools present 69 files.  
  * Contains evidence, QA, CLI, config generators/checkers.  
  * Anchors:  
    * tools/evidence/update\_evidence\_index.py  
    * tools/evidence/run\_sanity\_pipeline.py  
    * tools/cli/generate\_showcompat\_artifacts.py  
* ci/ and .github/ — Present.  
  * Listing proof: ci present 10 files; .github present 1 files.  
  * .github/workflows/ci.yml defines CI jobs; ci/checks/\*\* contains shell/Python checks.  
  * Anchors:  
    * .github/workflows/ci.yml  
    * ci/checks/check\_env\_pins.sh  
    * ci/checks/check\_mirror\_schema.sh  
* tests/ — Present.  
  * Listing proof: tests present 231 files.  
  * Contains CLI, adapter, evidence, ops, transport, QA, bodygraph tests.  
  * Anchors:  
    * tests/cli/test\_cli\_canonical\_bytes.py  
    * tests/adapter/test\_compat\_http\_dev.py  
    * tests/evidence/test\_evidence\_skeleton.py  
* scripts/ — Present.  
  * Listing proof: scripts present 64 files.  
  * Contains alternate CLI wrappers, QA/ops scripts, DB scripts, release/evidence scripts.  
  * Anchors:  
    * scripts/hdctl.py  
    * scripts/ingest/run\_vendor\_ingest.py  
    * scripts/release\_id\_recompute.py

## Root discipline capture: observed truth/governed-output homes

Top-level roots that appear to hold governed, generated, audit, or source-of-truth material:

* audit/ — manifests, close reports, QA logs; proof: audit/EPIC-034\_READ\_ONLY\_REPO\_READINESS\_AUDIT.md, audit/EPIC-030\_MANIFEST.json.  
* artifacts/ — evidence mirror and generated outputs; proof: artifacts/evidence\_index.jsonl, artifacts/audit/http/reader\_get\_headers.txt.  
* docs/ — human evidence index, endpoint catalog, acceptance maps; proof: docs/evidence/INDEX.json, docs/ENDPOINTS\_CATALOG.json.  
* catalog/ — release/catalog JSON; proof: catalog/manifest.json, catalog/channels\_catalog\_v1.json.  
* tools/ — governed generators/checkers; proof: tools/evidence/update\_evidence\_index.py.  
* scripts/ — operational/evidence/release scripts; proof: scripts/release\_id\_recompute.py, scripts/ingest/run\_vendor\_ingest.py.  
* ci/ and .github/ — CI checks/workflows; proof: .github/workflows/ci.yml, ci/checks/check\_mirror\_schema.sh.  
* proofs/ — top-level proof-like root exists in listing.  
* reports/, scan\_reports/, validation/ — report/validation-like top-level roots exist in listing.

---

# Packaging and Entrypoints

## Packaging / build configuration

* pyproject.toml  
  * Excerpt:  
    * \[project\]  
    * name \= "glow-hdengine"  
    * version \= "0.0.0"  
    * dependencies \= \[\]  
    * \[project.scripts\]  
    * hdctl \= "engine.cli.main:cli"  
    * \[tool.setuptools.packages.find\]  
    * include \= \["engine\*", "adapter\*", "presenter\*"\]  
  * Declares a setuptools package named glow-hdengine, Python \>=3.10, no project dependencies in the \[project\] table, and a console script hdctl.  
* requirements.txt / requirements-dev.txt  
  * Present in top-level listing.  
  * CI uses them: .github/workflows/ci.yml excerpt:  
    * test \-f requirements.txt && python \-m pip install \-r requirements.txt || true  
    * test \-f requirements-dev.txt && python \-m pip install \-r requirements-dev.txt || true  
* pytest.ini  
  * Present in top-level listing.  
  * Categorized as test configuration by filename and location; exact contents were not expanded in this audit.

## Entrypoint inventory

### HTTP server/app startup

* adapter/wsgi.py:create\_app  
  * Excerpt:  
    * def create\_app():  
    * app \= Flask(\_\_name\_\_)  
    * app.register\_blueprint(reader\_bp)  
    * app.register\_blueprint(compat\_blueprint)  
    * app \= create\_app()  
  * Role: constructs the Flask app, installs logging/env guards, mounts reader and compat blueprints, and defines internal health/ready routes.  
* adapter/app.py  
  * Excerpt:  
    * from adapter.wsgi import create\_app  
    * app \= create\_app()  
  * Role: imports create\_app for flask \--app adapter.app run.  
* adapter/http\_reader.py:create\_app  
  * Excerpt:  
    * def create\_app():  
    * app \= Flask(\_\_name\_\_)  
    * app.register\_blueprint(bp, url\_prefix="")  
    * app.register\_blueprint(compat\_blueprint)  
  * Role: alternate app factory registering the reader blueprint at root and compat blueprint.  
* adapter/factory.py:create\_app  
  * Excerpt:  
    * from adapter.http\_reader import bp  
    * app.register\_blueprint(bp, url\_prefix="") \# mount at /  
  * Role: another factory mounting adapter.http\_reader.bp at /.

### CLI console scripts

* pyproject.toml → engine.cli.main:cli  
  * Excerpt: hdctl \= "engine.cli.main:cli".  
  * Role: installed hdctl command.  
* engine/cli/main.py:cli  
  * Excerpt:  
    * def cli(argv: list\[str\] | None \= None) \-\> int:  
    * parser \= \_build\_parser()  
    * args \= parser.parse\_args(argv)  
    * return int(handler(args) or 0\)  
  * Role: parses CLI args and dispatches to subcommand handlers.  
* engine/cli/main.py:\_build\_parser  
  * Excerpt:  
    * sub \= parser.add\_subparsers(dest="command", required=True)  
    * show \= sub.add\_parser("showcompat", ...)  
    * aux \= sub.add\_parser("aux-preview", ...)  
    * bg \= sub.add\_parser("bg:resolve", ...)  
    * dev\_sampler \= sub.add\_parser("dev:sampler", ...)  
  * Role: defines hdctl subcommands.  
* scripts/hdctl.py  
  * Excerpt from grep output:  
    * Use \\hdctl showcompat \--pair-file \<pair.json\> \--dump-reader \<out.json\> \--dump-admin-dir \<dir\>\`\`  
    * def main() \-\> int:  
    * if \_\_name\_\_ \== "\_\_main\_\_":  
  * Role: script wrapper around CLI behavior.

### Evidence/indexing background or scheduled-like jobs

* tools/evidence/update\_evidence\_index.py  
  * Excerpt:  
    * HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json"  
    * HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256"  
    * MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl"  
    * docstring: Harden the evidence index, hash sentinel, and machine mirror.  
  * Role: reads/writes/checks evidence index, hash sentinel, and JSONL mirror.  
* tools/evidence/run\_sanity\_pipeline.py  
  * Referenced by CI: .github/workflows/ci.yml excerpt:  
    * name: Run sanity pipeline  
    * run: python tools/evidence/run\_sanity\_pipeline.py  
  * Role: CI-invoked sanity pipeline.  
* scripts/db/run\_retention\_job.py  
  * Grep proof:  
    * scripts/db/run\_retention\_job.py:50:def main() \-\> None:  
    * scripts/db/run\_retention\_job.py:88:if \_\_name\_\_ \== "\_\_main\_\_":  
  * Role: script entrypoint for DB retention job; exact behavior not expanded beyond entrypoint evidence.

---

# Engine Modules

## Sampler

* engine/sampler/core.py  
  * Primary symbols:  
    * ViewerProfile — excerpt: @dataclass(frozen=True) class ViewerProfile:  
    * CandidateFeatures — excerpt: class CandidateFeatures:  
    * SamplerConfig — excerpt: class SamplerConfig:  
    * build\_candidate\_pool — excerpt: def build\_candidate\_pool(...):  
    * rank\_candidates — excerpt: def rank\_candidates(...):  
    * sample\_and\_rank — excerpt: def sample\_and\_rank(...):  
  * Role facts:  
    * File docstring states: Pure-compute sampler core (DISS003).  
    * Pool construction excerpt: if \_is\_zero\_weight(candidate): continue; \_is\_eligible(...).  
    * Ranking excerpt: ordered \= sorted(pool.candidates, key=cmp\_to\_key(lambda a, b: \_compare\_entries(a, b, cfg))).  
    * Deterministic claim in file itself: No randomness, clocks, or external state are consulted.

## Core compatibility compute

* engine/compat/compute.py  
  * Primary symbols:  
    * band\_for(score) — maps numeric score to Cool, Open, Warm, Glow; excerpt: if score \<= THRESHOLDS\_V1\["cool\_max"\]: return "Cool".  
    * \_score\_for(cat, pair\_k, weights) — excerpt: hashlib.sha256(f"{pair\_k}:{cat}".encode("utf-8")).digest().  
    * compat\_public(...) — excerpt: \# AB↔BA identity by normalization; a1,b1 \= normalize\_pair(a,b); pkey \= pair\_key(a1,b1).  
    * conjunction\_public(...) — excerpt: Build a deterministic conjunction contract payload for canonical emission.  
    * conjunction\_public\_resolved(...) — excerpt: Resolve unresolved conjunction inputs through local lookup first, then resolver acquisition when rails allow.  
  * Role facts:  
    * Compatibility output includes categories and meta: excerpt: return {"categories": cats, "meta":{"engine\_tag":engine\_tag,"release\_id":release\_id,"invocation\_tag":invocation\_tag}}.  
    * AB↔BA handling is explicit in compat\_public: a1,b1 \= normalize\_pair(a,b).  
* engine/compat/ordering.py  
  * Imported by compute.py: from engine.compat.ordering import normalize\_pair, pair\_key.  
  * Role: pair normalization and pair-key support for AB↔BA identity, as evidenced by imports and call sites in compat\_public.  
* engine/runtime/\_\_init\_\_.py / runtime public emitter  
  * Imported by CLI and adapter:  
    * from engine.runtime import emit\_reader\_public\_envelope  
    * from engine.runtime import emit\_reader\_public\_bytes  
  * Role: Reader envelope/public bytes path; exact file contents were not expanded in this audit, but import/call anchors show use.

## Determinism hazards inventory

Observed in audited engine/adapter paths:

* Process-time captured in adapter HTTP module  
  * Path: adapter/http\_reader.py  
  * Excerpt:  
    * \_PROCESS\_STARTED\_AT \= datetime.now(timezone.utc)  
    * \_PROCESS\_PID \= os.getpid()  
  * Fact: module import captures wall-clock time and process id.  
* Vendor client uses monotonic/wall time and sleep  
  * Path: engine/bodygraph/vendor\_client.py  
  * Excerpts:  
    * def \_now\_ms() \-\> float: return time.monotonic() \* 1000.0  
    * self.\_sleep \= sleep or time.sleep  
    * self.\_wall\_time \= wall\_time or time.time  
    * deadline \= self.\_monotonic() \+ self.\_timeouts.total\_timeout\_ms  
  * Fact: vendor fetch timing/retry logging uses clocks and sleep hooks.  
* BodyGraph ingest uses monotonic and UTC timestamp  
  * Path: engine/bodygraph/ingest.py  
  * Excerpts:  
    * start \= time.monotonic()  
    * return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) \+ "Z"  
    * duration\_ms \= (time.monotonic() \- start) \* 1000.0  
  * Fact: ingest outcome/log records include duration and timestamp logic.  
* File I/O in CLI and DB/evidence-related engine paths  
  * Path: engine/cli/main.py  
  * Excerpt: \_dump\_reader\_bytes: target.parent.mkdir(parents=True, exist\_ok=True) and target.write\_bytes(payload).  
  * Path: engine/db/adapter.py  
  * Excerpt: \_write\_snapshot: path.write\_text(text, encoding="utf-8").  
  * Fact: CLI dump and DB adapter snapshot paths write files.  
* Network calls in vendor seam  
  * Path: engine/bodygraph/vendor\_client.py  
  * Excerpt: req \= urlrequest.Request(request.url, data=request.body\_bytes, headers=request.headers, method="POST"); status\_code, body\_bytes, headers \= self.\_request(req, timeout).  
  * Fact: HTTP POST is performed through urllib request abstraction unless a test/request callable is injected.

Audited for sampler determinism:

* engine/sampler/core.py explicitly sorts candidates and states no clocks/randomness/external state; no direct random, time, network, or file I/O observed in the sampled sampler file.

---

# Adapter / HTTP Surfaces

## Route registration map

* adapter/wsgi.py:create\_app  
  * Excerpt:  
    * app.register\_blueprint(reader\_bp)  
    * app.register\_blueprint(compat\_blueprint)  
  * Mounted groups:  
    * Reader blueprint from adapter.http\_reader.bp; prefix not supplied in this factory.  
    * Compat blueprint from engine.http.compat\_handler.compat\_blueprint, whose own declaration includes url\_prefix="/api/compat/v1".  
* adapter/http\_reader.py:create\_app  
  * Excerpt:  
    * app.register\_blueprint(bp, url\_prefix="")  
    * app.register\_blueprint(compat\_blueprint)  
  * Mounted groups:  
    * bp at root prefix "".  
    * compat\_blueprint at its own prefix /api/compat/v1.  
* adapter/factory.py:create\_app  
  * Excerpt:  
    * app.register\_blueprint(bp, url\_prefix="") \# mount at /  
  * Mounted group:  
    * adapter.http\_reader.bp at /.  
* engine/http/compat\_handler.py  
  * Excerpt: compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
  * Routes:  
    * @compat\_blueprint.get("") → get\_ids\_only  
    * @compat\_blueprint.route("", methods=\["POST"\], provide\_automatic\_options=False) → post\_json  
    * @compat\_blueprint.route("", methods=\["HEAD"\], provide\_automatic\_options=False) → post\_json\_head  
    * @compat\_blueprint.route("", methods=\["OPTIONS"\], provide\_automatic\_options=False) → post\_json\_options  
* adapter/http\_reader.py reader/dev/ops/internal routes  
  * Grep proof:  
    * @bp.get("/reader")  
    * @bp.get("/api/aux/narrative")  
    * @bp.get("/aux/narrative")  
    * @bp.post("/reader")  
    * @bp.route("/ops/db/unavailable", methods=\["GET"\])  
    * @bp.route("/ops/rails/refusal", methods=\["GET", "POST"\])  
    * @bp.route("/ops/probe/env", methods=\["GET"\])  
    * @bp.route("/internal/dev/sampler", methods=\["POST"\], provide\_automatic\_options=False)  
    * @bp.get("/dev/sampler/conjunction")  
    * @bp.get("/dev/reader/conjunction")  
    * @bp.get("/dev/writer/conjunction")  
    * @bp.route("/internal/version", methods=\["GET", "HEAD"\])  
    * @bp.route("/ops/writer/diagnostic", methods=\["POST"\], provide\_automatic\_options=False)

## Surface classification

* Reader-like JSON success  
  * Path: adapter/http\_reader.py  
  * Handler: reader\_v1  
  * Excerpts:  
    * @bp.get("/reader")  
    * if request.args.get("v") \!= "1":  
    * body \= emit\_fn(a, b, engine\_tag=..., invocation\_tag=..., release\_id=...)  
    * resp \= Response(body, status=200)  
  * Role: dev-gated Reader response from chart file inputs.  
* Compat API  
  * Path: engine/http/compat\_handler.py  
  * Handlers: get\_ids\_only, post\_json, post\_json\_head, post\_json\_options  
  * Excerpt:  
    * compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1")  
    * body \= compat\_public(a, b, vp\["top\_category"\], vp\["weights"\], ...)  
  * Role: /api/compat/v1 GET/POST/HEAD/OPTIONS surface.  
* Aux/narrative  
  * Path: adapter/http\_reader.py  
  * Handler: aux\_narrative  
  * Excerpts:  
    * @bp.get("/api/aux/narrative")  
    * @bp.get("/aux/narrative")  
    * emission \= emit\_public\_aux(...)  
    * Content-Type": "text/plain; charset=utf-8"  
  * Role: narrative text emission route.  
* Admin/internal  
  * Paths:  
    * adapter/http\_reader.py:internal\_version  
    * adapter/wsgi.py:internal\_healthz, internal\_readyz  
  * Excerpts:  
    * @bp.route("/internal/version", methods=\["GET", "HEAD"\])  
    * @app.get("/internal/healthz")  
    * @app.get("/internal/readyz")  
  * Role: internal version/health/ready surfaces.  
* Dev/diagnostic harness  
  * Path: adapter/http\_reader.py  
  * Handlers from grep:  
    * /internal/dev/sampler  
    * /dev/sampler/conjunction  
    * /dev/reader/conjunction  
    * /dev/writer/conjunction  
    * /ops/writer/diagnostic  
  * Role: dev/ops harness and diagnostic writer surfaces.

## Transport semantics hooks

* HEAD vs GET parity for Reader  
  * Path: adapter/http\_reader.py  
  * Excerpt:  
    * \# HEAD parity  
    * if request.method.upper() \== "HEAD":  
    * resp \= Response(b"", status=200)  
    * resp.headers\["Content-Length"\] \= str(len(body))  
* Conditional 304 for Reader  
  * Path: adapter/http\_reader.py  
  * Excerpt:  
    * etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\""  
    * tokens \= \_parse\_if\_none\_match(request.headers.get("If-None-Match"))  
    * if etag in tokens and "\*" not in tokens:  
    * resp \= Response(b"", status=304)  
* ETag quoting  
  * Path: adapter/http\_reader.py  
  * Excerpt: etag \= "\\"" \+ \_sha256\_hex(body) \+ "\\"".  
  * Aux narrative also sets quoted ETag: resp.headers\["ETag"\] \= f'"{digest}"'.  
* Cache-Control  
  * Path: adapter/http\_reader.py  
  * Excerpt:  
    * \_set\_reader\_200\_headers: resp.headers\["Cache-Control"\] \= "private, max-age=0, must-revalidate".  
    * Writer response: resp.headers\["Cache-Control"\] \= "no-store".  
  * Path: engine/http/compat\_handler.py  
  * Excerpt: \_writer\_payload: resp.headers\["Cache-Control"\] \= "no-store".  
* Content-Type  
  * Path: adapter/http\_reader.py  
  * Excerpt: \_set\_reader\_200\_headers: resp.headers\["Content-Type"\] \= "application/json; charset=utf-8".  
  * Path: engine/http/compat\_handler.py  
  * Excerpt: Response(payload, status=status, mimetype="application/json; charset=utf-8").  
  * Path: adapter/http\_reader.py aux route excerpt: "Content-Type": "text/plain; charset=utf-8".

---

# Presenter / Emitter

* engine/presenter/emitter.py  
  * Primary functions:  
    * emit\_public(envelope, sort\_keys=True) — excerpt: return canon.sercanon(envelope, sort\_keys=sort\_keys).  
    * emit\_public\_with\_envelope(...) — excerpt: return emit\_public(envelope, sort\_keys=sort\_keys), envelope.  
    * emit\_compact\_json(...) — excerpt: Compatibility alias for the canonical emitter.  
  * Semantics:  
    * Docstring excerpt: Canonical emitter for governed public JSON bytes.  
    * Delegates to canonical serializer: Delegates to the canonical serializer (LF-terminated UTF-8).  
  * Callers:  
    * adapter/http\_reader.py imports: from engine.presenter.emitter import emit\_public.  
    * engine/http/compat\_handler.py imports: from engine.presenter import emit\_public.  
    * engine/cli/main.py imports: from engine.presenter import emitter.  
    * engine/bodygraph/ingest.py imports: from engine.presenter import emitter.  
* engine/serializer/canon.py  
  * Primary function: sercanon(obj, sort\_keys=True).  
  * Excerpt:  
    * Canonical JSON serializer for public envelopes.  
    * UTF-8 bytes  
    * ensure\_ascii=False  
    * keys sorted by default  
    * compact separators  
    * exactly one trailing newline  
    * return stable\_sercanon.serialize(obj, sort\_keys=sort\_keys)  
  * Role: canonical JSON byte formatting used by presenter.  
* engine/stable/sercanon.py  
  * Imported by engine/serializer/canon.py: from engine.stable import sercanon as stable\_sercanon.  
  * Role: underlying stable serializer.  
* Additional runtime/Reader emitter  
  * engine.runtime.emit\_reader\_public\_envelope and engine.runtime.emit\_reader\_public\_bytes are imported/called by CLI and HTTP:  
    * adapter/http\_reader.py: from engine.runtime import emit\_reader\_public\_bytes  
    * engine/cli/main.py: from engine.runtime import emit\_reader\_public\_envelope  
  * Usage excerpt in CLI:  
    * reader\_bytes, reader\_envelope \= emit\_reader\_public\_envelope(...)  
  * Distinction: this path emits Reader-specific public bytes/envelope, while engine.presenter.emitter.emit\_public emits generic canonical JSON envelopes.

---

# CLI Surfaces

## Console script

* Installed command: hdctl  
  * pyproject.toml excerpt: hdctl \= "engine.cli.main:cli".

## Parser/subcommands

* engine/cli/main.py:\_build\_parser  
  * Excerpts:  
    * parser \= argparse.ArgumentParser(prog="hdctl", ...)  
    * sub \= parser.add\_subparsers(dest="command", required=True)  
    * show \= sub.add\_parser("showcompat", ...)  
    * aux \= sub.add\_parser("aux-preview", ...)  
    * bg \= sub.add\_parser("bg:resolve", ...)  
    * dev\_sampler \= sub.add\_parser("dev:sampler", ...)

## hdctl showcompat

* Entrypoint symbol: engine/cli/main.py:showcompat  
* Arguments evidenced by parser:  
  * File inputs: \--pair-file, \--a-file, \--b-file, aliases \--a, \--b.  
  * Output dumps: \--dump-reader, \--dump-admin-dir.  
  * Source: \--source, choices ("db", "vendor", "auto").  
  * Conjunction: \--conjunction.  
  * Viewer prefs: \--viewer-prefs-file.  
  * DB/user inputs: \--user-a, \--user-b.  
  * Vendor birth inputs: \--birthdate-a, \--birthtime-a, \--location-a, same for b.  
* Call chain facts:  
  * Reads source/file/stdin via nested \_load\_from\_source and \_load\_from\_files\_or\_stdin.  
  * Computes compatibility with compat\_public(...); excerpt: compat\_full \= compat\_public(...).  
  * Emits CLI stdout with canonical emitter; excerpt: compat\_bytes \= emitter.emit\_public(compat\_payload) and \_emit\_stdout\_bytes(compat\_bytes).  
  * Generates Reader bytes with runtime emitter; excerpt: reader\_bytes, reader\_envelope \= emit\_reader\_public\_envelope(...).  
* Output behavior:  
  * Writes stdout: \_emit\_stdout\_bytes: sys.stdout.buffer.write(payload).  
  * Enforces LF/CRLF: \_emit\_stdout\_bytes: if not payload.endswith(b"\\n"): raise CliError("STDOUT\_MISSING\_LF"); if b"\\r\\n" in payload: raise CliError("STDOUT\_CRLF").  
  * Writes files when flags are supplied:  
    * \_dump\_reader\_bytes: target.write\_bytes(payload).  
    * \_emit\_admin\_dumps: canon\_dump(admin\_dir / f"{case\_name}.left.bodygraph.json", left) and related sidecars.  
  * Nonzero/missing arg behavior:  
    * cli(...) catches CliError and returns err.exit\_code.  
    * Example vendor source missing inputs: \_vendor\_inputs\_from\_args: if missing: raise CliError("MISSING\_VENDOR\_INPUT").  
    * Argparse errors map to 64: return 64 if code else 0\.

## hdctl bg:resolve

* Entrypoint symbol: engine/cli/main.py:bg\_resolve  
* Arguments evidenced:  
  * \--user required.  
  * \--source choices ("auto", "db", "vendor"), default auto.  
  * \--upsert, \--dry-run, \--birthdate, \--birthtime, \--location.  
* Call chain facts:  
  * Calls resolve\_bodygraph(...).  
  * Emits response: output \= emitter.emit\_public(result.payload).decode("utf-8"); sys.stdout.write(output).  
  * Vendor input guard: if args.source \== "vendor": ... raise CliError("MISSING\_VENDOR\_INPUT", exit\_code=64).

## hdctl aux-preview

* Entrypoint symbol: engine/cli/main.py:aux\_preview  
* Arguments evidenced:  
  * \--category, \--band, \--perspective, \--pair-file, \--show-narrative, \--admin-out.  
* Call chain facts:  
  * Calls get\_pack() and emit\_public\_aux(...).  
  * Writes narrative body to stdout if enabled: sys.stdout.buffer.write(emission.body).  
  * Writes admin sidecar if \--admin-out: canon\_dump(args.admin\_out, sidecar).

## hdctl dev:sampler

* Entrypoint symbol: engine/cli/main.py:dev\_sampler\_run  
* Arguments evidenced:  
  * \--viewer required.  
  * \--candidates-file required.  
  * \--seed optional.  
* Call chain facts:  
  * Dev guard: \_ensure\_dev\_admin\_env() requires APP\_ENV in ("dev", "test", "local").  
  * Calls sampler: ranked \= sample\_and\_rank(viewer, candidates).  
  * Emits canonical output: sys.stdout.buffer.write(sercanon(payload)).  
  * Seed is echoed, not used for ranking; excerpt: "Seed is echoed only for now; future phases may use this for tie-breaking hooks."

---

# Vendor Seam & BodyGraph Storage

## Vendor client

* engine/bodygraph/vendor\_client.py  
  * Primary symbols:  
    * HdApiClient  
    * VendorRequest  
    * VendorResult  
    * VendorRetryConfig  
    * VendorTimeouts  
    * VendorError  
    * join\_vendor\_resource\_url  
  * Env/config inputs:  
    * \_resolve\_hdapi\_base\_url reads HD\_API\_BASE\_URL and HDAPI\_BASE\_URL.  
    * from\_env reads HD\_API\_KEY, GEO\_API\_KEY, RELEASE\_ID.  
    * Rails state reads SAFE\_MODE, ALLOW\_NETWORK.  
  * Request shaping:  
    * \_ROUTE\_CONTRACTS includes "bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates".  
    * build\_contract\_route\_request(...) validates route fields and auth model.  
    * Body bytes: json.dumps(body, sort\_keys=True, separators=(",", ":")).encode("utf-8") \+ b"\\n".  
    * Headers include Accept, Content-Type, User-Agent; auth uses either Authorization: Bearer ... or HD-Api-Key.  
  * HTTP call:  
    * urlrequest.Request(..., method="POST")  
    * status\_code, body\_bytes, headers \= self.\_request(req, timeout)

## BodyGraph ingest and persistence/cache

* engine/bodygraph/ingest.py  
  * Primary symbols:  
    * resolve\_db\_user\_id  
    * VendorInputs  
    * IngestOutcome  
    * gather\_inputs\_from\_env  
    * ingest\_vendor\_bodygraph  
  * Env inputs:  
    * gather\_inputs\_from\_env requires INGEST\_TEST\_USER\_ID, INGEST\_TEST\_BIRTHDATE, INGEST\_TEST\_BIRTHTIME, INGEST\_TEST\_LOCATION.  
  * Cache/key formation:  
    * ID normalization uses UUID or UUID5:  
      * return str(uuid.uuid5(uuid.NAMESPACE\_URL, normalized))  
    * Ingest computes idempotency\_key \= \_idempotency\_key(inputs.user\_id, "hdapi", vendor\_version, request.input\_fingerprint); function body not expanded in the captured excerpt, but call anchor shows key ingredients.  
  * Persistence:  
    * Uses DBAccess: db \= db\_access or DBAccess.for\_current\_env().  
    * Counts/fetches/persists with helper calls: \_row\_count, \_persist\_bodygraph, \_fetch\_payload.  
    * Success log path constants:  
      * INGEST\_DIR \= Path("artifacts/ingest")  
      * SUCCESS\_LOG \= INGEST\_DIR / "ingest\_success.log"  
      * RETRY\_LOG \= INGEST\_DIR / "retry\_trace.log"  
* engine/db/adapter.py  
  * Primary symbol: DBAccess.  
  * Providers:  
    * Imports BridgeProvider and PsycopgProvider.  
    * Provider selection order excerpt: order \= \["psycopg", "bridge"\].  
  * Env/config:  
    * Reads DATABASE\_URL, DB\_BRIDGE\_URL, DB\_FORCE\_PG, DB\_FORCE\_BRIDGE, DB\_ALLOW\_BRIDGE\_IN\_PROD.  
  * Snapshot:  
    * Default snapshot\_path: "artifacts/db\_bridge/adapter\_selection.snapshot.json".  
    * Writes snapshot: \_write\_snapshot(snapshot, snapshot\_payload).  
* CLI BodyGraph DB read  
  * Path: engine/cli/main.py  
  * Function: \_fetch\_db\_bodygraph  
  * Excerpt:  
    * SELECT payload::text FROM hde.body\_graphs\_current WHERE user\_id \= %s ORDER BY vendor\_version DESC LIMIT 1  
    * db \= db\_access or DBAccess.for\_current\_env()  
  * Fact: CLI reads current BodyGraph payload from DB table hde.body\_graphs\_current.

## Offline/vendor gating posture

* Resolver gate  
  * Path: engine/bodygraph/resolver.py  
  * Excerpts:  
    * safe\_mode\_closed \= \_truthy(env.get("SAFE\_MODE"))  
    * allow\_network \= \_truthy(env.get("ALLOW\_NETWORK"))  
    * If safe: error code PROVIDER\_REFUSED, message Vendor source is refused under SAFE rails (SAFE\_MODE=1).  
    * If network blocked: error code PROVIDER\_NETWORK\_BLOCKED, message Network disabled under current rails.  
  * Fact: vendor resolution fails closed when SAFE\_MODE is truthy or ALLOW\_NETWORK is not truthy.  
* Ingest gate  
  * Path: engine/bodygraph/ingest.py  
  * Excerpts:  
    * safe\_mode \= \_truthy(env.get("SAFE\_MODE"))  
    * allow\_network \= \_truthy(env.get("ALLOW\_NETWORK"))  
    * if safe\_mode: raise VendorError("PROVIDER\_REFUSED", "Vendor source refused under SAFE rails", ...)  
    * if not allow\_network: raise VendorError("PROVIDER\_NETWORK\_BLOCKED", "Network blocked by rails")  
  * Fact: BodyGraph ingest refuses vendor network under closed rails.  
* Vendor log rails-state  
  * Path: engine/bodygraph/vendor\_client.py  
  * Excerpt: return "open\_exception" if safe\_mode \== "0" and allow\_network \== "1" else "closed\_default".  
  * Fact: vendor client labels rails state from SAFE\_MODE/ALLOW\_NETWORK.

---

# Evidence, Indices, Catalogs

## Evidence homes inventory

* docs/  
  * Contains human-facing evidence/index/catalog/acceptance docs.  
  * Proof anchors:  
    * docs/evidence/INDEX.json  
    * docs/evidence/INDEX.sha256  
    * docs/ENDPOINTS\_CATALOG.json  
    * docs/acceptance\_map\_epic034.json  
  * Generated/mixed posture: docs/acceptance\_map\_epic034.json is compact JSON with generated\_at\_utc; docs/evidence/INDEX.\* is managed by tools/evidence/update\_evidence\_index.py.  
* artifacts/  
  * Contains generated outputs, mirrors, hashes, HTTP header captures, vendor inventories.  
  * Proof anchors:  
    * artifacts/evidence\_index.jsonl  
    * artifacts/evidence\_index.jsonl.path\_proof.txt  
    * artifacts/audit/http/reader\_get\_headers.txt  
    * artifacts/vendor/hdapi\_v2/endpoint\_reference.csv  
  * Generated/mixed posture: many .sha256 and .path\_proof.txt siblings indicate generated/governed patterns.  
* audit/  
  * Contains manifests, close reports, QA roots, gates.  
  * Proof anchors:  
    * audit/EPIC-030\_MANIFEST.json  
    * audit/EPIC-030\_close\_report.md  
    * audit/qa/hde-epic034/...  
  * Generated/mixed posture: manifests and close reports have .path\_proof.txt siblings; QA logs appear generated.  
* catalog/  
  * Contains release/catalog JSON.  
  * Proof anchors:  
    * catalog/manifest.json  
    * catalog/channels\_catalog\_v1.json  
  * Generated/mixed posture not determined beyond file presence in this audit.  
* artifacts/vendor/hdapi\_v2/  
  * Endpoint catalog output listed: artifacts/vendor/hdapi\_v2/endpoint\_reference.csv.  
  * Source-cache input listed: artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt.  
  * Evidence-like vendor contract inventory home.

## Evidence index structures

* docs/evidence/INDEX.json  
  * Tool anchor: tools/evidence/update\_evidence\_index.py sets HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json".  
  * Test anchor: tests/evidence/test\_evidence\_skeleton.py reads it: entries \= update\_evidence\_index.\_load\_human\_index().  
* docs/evidence/INDEX.sha256  
  * Tool anchor: HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256".  
  * Test anchor: sentinel\_line \= Path("docs/evidence/INDEX.sha256").read\_text(...).  
* artifacts/evidence\_index.jsonl  
  * Tool anchor: MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl".  
  * Tool docstring excerpt: The machine mirror lived at artifacts/evidence\_index.jsonl with the required keys already.  
  * CI anchor: .github/workflows/ci.yml runs ci/checks/check\_mirror\_schema.sh.  
* artifacts/evidence\_index.jsonl.sha256  
  * Tool anchor: MIRROR\_SHA\_PATH \= ROOT / "artifacts/evidence\_index.jsonl.sha256".  
* Tooling  
  * tools/evidence/update\_evidence\_index.py  
    * Excerpt: Harden the evidence index, hash sentinel, and machine mirror.  
    * Imports determinism guard: from engine.runtime.determinism\_env import DETERMINISM\_ENV\_PINS, ensure\_determinism\_env.  
  * CI:  
    * python tools/evidence/update\_evidence\_index.py  
    * python tools/evidence/update\_evidence\_index.py \--check  
    * ci/checks/check\_evidence\_index\_hash.sh  
    * ci/checks/check\_mirror\_schema.sh

## Endpoint catalog

* docs/ENDPOINTS\_CATALOG.json  
  * First-line shape excerpt:  
    * {"endpoints":\[{"a7\_eligible":false,"blueprint\_module":"engine.http.compat\_handler","classification":"internal\_admin",...  
    * Includes method, path, classification, blueprint\_module, env\_gate, rails\_profile.  
  * Listed endpoints include:  
    * /api/compat/v1  
    * /dev/reader/conjunction  
    * /dev/writer/conjunction  
    * /dev/sampler/conjunction  
    * /internal/version  
    * /reader  
  * References:  
    * Grep/listing found artifacts/audit/ENDPOINTS\_CATALOG.json and multiple QA snapshots.  
    * CI/test references visible in grep include tests/evidence/test\_hdapi\_v2\_contract\_inventory.py route/catalog assertions, though exact docs catalog reader functions were not expanded.  
* artifacts/audit/ENDPOINTS\_CATALOG.json  
  * Listed by find output.  
  * Appears as audit mirror/catalog sibling to docs catalog by name.  
* Other endpoint-like artifacts  
  * artifacts/hdapi/endpoints.json  
  * artifacts/reader/endpoints\_snapshot.json  
  * docs/run/PROD\_ENDPOINTS.json  
  * artifacts/vendor/hdapi\_v2/endpoint\_reference.csv

## Proof artifacts / snapshot artifacts

Observed proof/header/snapshot artifacts include:

* Reader HTTP proofs  
  * Paths from listing:  
    * artifacts/audit/http/reader\_get\_headers.txt  
    * artifacts/audit/http/reader\_head.json  
    * artifacts/audit/http/reader\_head\_headers.txt  
    * artifacts/audit/http/reader\_304\_headers.txt  
    * artifacts/cards/a7/reader\_200\_headers.txt  
    * artifacts/cards/a7/reader\_304\_headers.txt  
    * artifacts/cards/a7/reader\_head\_headers.txt  
  * Producer not fully traced in captured snippets; filenames correspond to HTTP header/body proof outputs.  
* Internal version proofs  
  * Paths from listing:  
    * artifacts/audit/http/internal\_version\_get\_headers.txt  
    * artifacts/audit/http/internal\_version\_head\_headers.txt  
    * artifacts/audit/http/internal\_version\_conditional\_headers.txt  
    * artifacts/ops/internal\_version/headers\_get.txt  
    * artifacts/ops/internal\_version/headers\_head.txt  
    * artifacts/ops/internal\_version/headers\_cond\_if\_none\_match.txt  
* Evidence index snapshot  
  * Test anchor:  
    * tests/evidence/test\_d23\_evidence\_index\_snapshot\_contract.py uses snapshot\_path \= root / "audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json".  
  * Tool anchor:  
    * CI and tests reference tools.evidence.generate\_evidence\_index\_snapshot.  
* DB bridge/provider snapshot  
  * Path from DB adapter default:  
    * artifacts/db\_bridge/adapter\_selection.snapshot.json  
  * Producer:  
    * engine/db/adapter.py:DBAccess.for\_current\_env calls \_write\_snapshot(snapshot, snapshot\_payload).

---

# Tests, QA Harness, CI/Checks

## Tests map

Key test loci observed:

* CLI canonical bytes / showcompat  
  * Path: tests/cli/test\_cli\_canonical\_bytes.py  
  * Grep excerpts:  
    * def test\_showcompat\_stdout\_is\_canonical():  
    * \_run\_hdctl(\["showcompat"\], stdin=(PAIR \+ "\\n").encode())  
    * def test\_showcompat\_conjunction\_stdout\_is\_canonical():  
  * Role: CLI canonical stdout and conjunction canonical output.  
* CLI showcompat parity/identity  
  * Path: tests/cli/test\_showcompat\_parity\_and\_identity.py  
  * Grep excerpts:  
    * PRESENTER\_AB\_ARTIFACT \= Path("artifacts/presenter/showcompat\_ab.bytes")  
    * def \_run\_showcompat(...)  
    * pytest.skip("showcompat vendor calls require open rails")  
  * Role: AB/BA identity, two-run identity, presenter byte artifacts; includes vendor/open-rails skips.  
* Compat HTTP  
  * CI references:  
    * tests/adapter/test\_compat\_http\_dev.py  
    * tests/adapter/test\_compat\_http\_parity.py  
  * Role: dev \+ WSGI compat HTTP coverage, as named in CI job Run dev \+ wsgi compat HTTP tests.  
* Internal version transport  
  * CI references:  
    * tests/transport/test\_internal\_version\_contract.py  
  * Role: internal version GET/HEAD/contract coverage.  
* Evidence index/catalog  
  * Paths:  
    * tests/evidence/test\_evidence\_skeleton.py  
    * tests/ops/test\_evidence\_index.py  
    * tests/evidence/test\_sanity\_evidence\_index.py  
  * Grep excerpts:  
    * Path("docs/evidence/INDEX.sha256").read\_text(...)  
    * Path("artifacts/evidence\_index.jsonl").read\_text(...)  
    * assert index\_entries, "sanity log missing from INDEX.json"  
* Determinism gates  
  * Paths:  
    * tests/evidence/test\_evidence\_index\_env.py  
    * tests/evidence/test\_sanity\_pipeline.py  
  * Grep excerpts:  
    * def test\_update\_evidence\_index\_requires\_closed\_rails  
    * assert any(line.startswith("check update\_evidence\_index.post:") for line in log\_lines)  
* Vendor/bodygraph  
  * Path:  
    * tests/bodygraph/test\_vendor\_client.py referenced in docs/acceptance\_map\_epic034.json evidence titles.  
    * tests/evidence/test\_hdapi\_v2\_contract\_inventory.py includes many adapter/vendor boundary assertions.  
  * Vendor/network reliance:  
    * CLI test grep shows pytest.skip("showcompat vendor calls require open rails").

## CI workflows

* .github/workflows/ci.yml  
  * Workflow name: ci.  
  * Trigger: on: \[push, pull\_request\].  
  * Common closed rails env:  
    * LC\_ALL: C  
    * LANG: C  
    * TZ: UTC  
    * SAFE\_MODE: "1"  
    * ALLOW\_NETWORK: "0"

Jobs/checks observed:

* test  
  * Runs setup, dependency install, editable install, then:  
    * ci/checks/check\_env\_pins.sh  
    * ci/checks/check\_cli\_help.sh  
    * python tools/cli/serializer\_grep\_guard.py  
    * python tools/cli/emitter\_symbol\_proof.py  
    * python tools/evidence/run\_canonical\_json\_gate.py  
    * python tools/evidence/update\_evidence\_index.py  
    * python tools/evidence/update\_evidence\_index.py \--check  
    * python tools/evidence/orientation\_demo.py \--check  
    * ci/checks/check\_evidence\_index\_hash.sh  
    * ci/checks/check\_bridge\_consistency.py  
    * ci/checks/check\_mirror\_schema.sh  
    * ci/checks/check\_final\_lf.sh  
    * pytest suites for evidence/order/CLI serializer guards.  
* compat-conj-pr01-closure  
  * Runs:  
    * tests/http/test\_compat\_endpoint\_contract.py::test\_conjunction\_identity\_hash\_artifact\_matches\_canonical\_bytes  
    * tests/ops/test\_evidence\_index.py::test\_evidence\_index\_has\_required\_compat\_artifacts  
* epic020  
  * Job name: epic020 acceptance suites (closed rails).  
  * Runs tests:  
    * tests/adapter/test\_jsonschema.py  
    * tests/cli/test\_cli\_usage\_and\_errors.py  
    * tests/cli/test\_errors\_parity.py  
    * tests/cli/test\_cli\_canonical\_bytes.py  
    * tests/cli/test\_showcompat\_parity\_and\_identity.py  
    * tests/cli/test\_serializer\_guards.py  
    * tests/transport/test\_internal\_version\_contract.py  
    * tests/qa/test\_epic020\_qa\_docs.py  
* compat-http-epic020  
  * Job name: EPIC020 compat HTTP coverage (closed rails).  
  * Runs:  
    * tests/adapter/test\_compat\_http\_dev.py  
    * tests/adapter/test\_compat\_http\_parity.py  
* epic020-evidence-bundles  
  * Runs:  
    * python \-m tools.evidence.epic020\_bundle build \--epic-id HDE-EPIC020  
    * python tools/evidence/update\_evidence\_index.py \--epic-id HDE-EPIC020  
    * ci/checks/check\_mirror\_schema.sh  
    * python \-m pytest tests/evidence/test\_epic020\_bundle\_index\_integration.py  
* sanity-pipeline  
  * Runs: python tools/evidence/run\_sanity\_pipeline.py.

## Script/check inventory

Representative QA/check scripts anchored by CI or grep:

* ci/checks/check\_env\_pins.sh — CI runs it before tests/gates.  
* ci/checks/check\_cli\_help.sh — CI CLI help check.  
* ci/checks/check\_evidence\_index\_hash.sh — CI evidence index hash check.  
* ci/checks/check\_mirror\_schema.sh — CI mirror schema check.  
* ci/checks/check\_final\_lf.sh — CI final-LF check.  
* ci/checks/check\_bridge\_consistency.py — grep shows def main() \-\> None; CI runs it.  
* tools/cli/serializer\_grep\_guard.py — CI serializer guard.  
* tools/cli/emitter\_symbol\_proof.py — CI emitter proof.  
* tools/evidence/update\_evidence\_index.py — index/mirror/sentinel generator/checker.  
* tools/evidence/orientation\_demo.py — CI \--check orientation demo.  
* tools/evidence/run\_canonical\_json\_gate.py — CI canonical JSON gate.  
* tools/evidence/run\_sanity\_pipeline.py — sanity pipeline job.  
* tools/cli/generate\_showcompat\_artifacts.py — QA harness references it for showcompat artifacts.  
* tools/qa/run\_hde\_epic024\_harness.py — grep shows it invokes python tools/cli/generate\_showcompat\_artifacts.py.  
* scripts/release\_id\_recompute.py — release identity recompute entrypoint; grep shows argparse def main.  
* scripts/ingest/run\_vendor\_ingest.py — vendor ingest script; grep shows def main() \-\> int.

---

# Flows & Call Chains

## 1\. Reader success flow (HTTP)

adapter/wsgi.py:create\_app → adapter.http\_reader.bp → adapter/http\_reader.py:reader\_v1 → engine.runtime.emit\_reader\_public\_bytes → Flask Response

* Route anchor: @bp.get("/reader").  
* Dev gate: if os.environ.get("APP\_ENV", "dev") \!= "dev": return \_error("ERR\_READER\_FORBIDDEN", 403).  
* Inputs: a, b, a\_tz, b\_tz query parameters.  
* File loading: \_safe\_load\_chart(a\_path) and \_safe\_load\_chart(b\_path).  
* Output: Response(body, status=200) with ETag, JSON content type, cache headers, content length.  
* Conditional handling: If-None-Match checked against quoted SHA256 ETag.

## 2\. Compat API flow (HTTP)

adapter/wsgi.py:create\_app → engine.http.compat\_handler.compat\_blueprint → engine/http/compat\_handler.py:post\_json → engine.compat.compute.compat\_public → engine.presenter.emit\_public → Flask Response

* Blueprint anchor: Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
* Handler anchor: @compat\_blueprint.route("", methods=\["POST"\], provide\_automatic\_options=False).  
* Prod behavior: if (os.environ.get("APP\_ENV") or "").lower() \== "prod": ... status=404.  
* Input validation: rejects mixed a/a\_id style payloads and invalid UIDs.  
* Viewer prefs: validate\_viewer\_prefs, then normalize\_viewer\_prefs.  
* Output: \_writer\_payload sets canonical JSON body, Cache-Control: no-store, no ETag.

## 3\. CLI showcompat / compat preview flow

pyproject.toml hdctl → engine/cli/main.py:cli → \_build\_parser → showcompat → \_load\_from\_source / \_load\_from\_files\_or\_stdin → compat\_public \+ emit\_reader\_public\_envelope → engine.presenter.emitter.emit\_public → \_emit\_stdout\_bytes

* Console script anchor: hdctl \= "engine.cli.main:cli".  
* Parser anchor: show \= sub.add\_parser("showcompat", ...).  
* File/stdin path: \_load\_from\_files\_or\_stdin reads \--pair-file, \--a-file/--b-file, or sys.stdin.read().  
* Source path:  
  * DB: \_fetch\_db\_bodygraph.  
  * Vendor: ingest\_vendor\_bodygraph(..., dry\_run=True).  
* Compatibility: compat\_full \= compat\_public(...).  
* Reader bytes: reader\_bytes, reader\_envelope \= emit\_reader\_public\_envelope(...).  
* Stdout: \_emit\_stdout\_bytes(compat\_bytes); LF and CRLF guarded.

## 4\. Vendor acquisition flow (BodyGraph ingest)

engine/cli/main.py:bg\_resolve or showcompat \--source vendor → engine.bodygraph.resolver.resolve\_bodygraph / engine.bodygraph.ingest.ingest\_vendor\_bodygraph → engine.bodygraph.vendor\_client.HdApiClient.from\_env → build\_request / fetch → engine.db.DBAccess.for\_current\_env → DB persist/fetch

* Resolver gate: safe\_mode\_closed \= \_truthy(env.get("SAFE\_MODE")); allow\_network \= \_truthy(env.get("ALLOW\_NETWORK")).  
* Closed rails result: PROVIDER\_REFUSED or PROVIDER\_NETWORK\_BLOCKED.  
* Client config: HD\_API\_BASE\_URL, HDAPI\_BASE\_URL, HD\_API\_KEY, GEO\_API\_KEY, RELEASE\_ID.  
* Request shaping: build\_contract\_route\_request validates route contract and auth model.  
* HTTP: urlrequest.Request(... method="POST").  
* Persistence: ingest uses DBAccess.for\_current\_env(), \_persist\_bodygraph, \_fetch\_payload.  
* Evidence/log outputs: artifacts/ingest/ingest\_success.log, artifacts/ingest/retry\_trace.log, artifacts/presenter/json\_canon\_compare.log.

## 5\. Evidence index update/validation flow

.github/workflows/ci.yml → python tools/evidence/update\_evidence\_index.py → tools/evidence/update\_evidence\_index.py constants → writes/checks docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl, mirror sha → CI check scripts

* CI anchor: .github/workflows/ci.yml runs both update and \--check.  
* Tool constants:  
  * HUMAN\_INDEX \= ROOT / "docs/evidence/INDEX.json"  
  * HASH\_SENTINEL \= ROOT / "docs/evidence/INDEX.sha256"  
  * MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl"  
  * MIRROR\_SHA\_PATH \= ROOT / "artifacts/evidence\_index.jsonl.sha256"  
* Determinism env import: ensure\_determinism\_env.  
* CI follow-up:  
  * ci/checks/check\_evidence\_index\_hash.sh  
  * ci/checks/check\_mirror\_schema.sh  
  * python tools/evidence/orientation\_demo.py \--check.

## 6\. Dev sampler CLI flow

hdctl dev:sampler → engine/cli/main.py:dev\_sampler\_run → \_ensure\_dev\_admin\_env → \_load\_candidates\_from\_path → engine.sampler.core.sample\_and\_rank → \_emit\_sampler\_output → sercanon

* Parser anchor: dev\_sampler \= sub.add\_parser("dev:sampler", ...).  
* Required args: \--viewer, \--candidates-file.  
* Env gate: if app\_env not in ("dev", "test", "local"): raise CliError("DEV\_ADMIN\_ONLY").  
* Engine call: ranked \= sample\_and\_rank(viewer, candidates).  
* Output: sys.stdout.buffer.write(sercanon(payload)).

---

# Drift and Reality vs Expectations

Neutral factual drift/alignment observations only.

## Directory/architecture drift

* Observed: There is both a root presenter/ directory and an engine package engine/presenter/.  
  * Proof anchor: top-level listing includes presenter; engine file listing includes engine/presenter/emitter.py.  
  * Impact: This creates ambiguity about presenter location when reading by directory name alone; the packaging include list includes both engine\* and presenter\*.  
* Observed: CLI implementation exists in engine/cli/, while script wrappers/backups also exist under scripts/.  
  * Proof anchor: pyproject.toml declares hdctl \= "engine.cli.main:cli"; grep/listing shows scripts/hdctl.py, scripts/hdctl.clean.py, scripts/hdctl.backup.py.  
  * Impact: This creates multiple CLI-related paths to distinguish during audits.  
* Observed: Adapter and HTTP code are split between adapter/http\_reader.py, adapter/wsgi.py, adapter/factory.py, and engine/http/compat\_handler.py.  
  * Proof anchor: adapter/wsgi.py imports reader\_bp from adapter.http\_reader and compat\_blueprint from engine.http.compat\_handler; adapter/http\_reader.py:create\_app also registers both.  
  * Impact: This creates multiple app factory/registration locations to inspect for route reality.

## Surface drift

* Observed: /api/compat/v1 is implemented under engine/http/compat\_handler.py, not under top-level adapter/.  
  * Proof anchor: engine/http/compat\_handler.py: compat\_blueprint \= Blueprint("compat", \_\_name\_\_, url\_prefix="/api/compat/v1").  
  * Impact: HTTP adapter responsibilities are split across adapter/ and engine/http/.  
* Observed: Reader route is dev-gated in code.  
  * Proof anchor: adapter/http\_reader.py: if os.environ.get("APP\_ENV", "dev") \!= "dev": return \_error("ERR\_READER\_FORBIDDEN", 403).  
  * Impact: Reader success flow is environment-dependent.  
* Observed: Endpoint catalog marks /reader as classification":"dev\_harness" and env\_gate":"APP\_ENV=dev".  
  * Proof anchor: docs/ENDPOINTS\_CATALOG.json excerpt includes /reader with "classification":"dev\_harness" and "env\_gate":"APP\_ENV=dev".  
  * Impact: Catalog and code both indicate Reader is not represented as an unrestricted public route in this snapshot.

## Evidence drift

* Observed: Evidence-like outputs are spread across docs/, artifacts/, audit/, catalog/, and QA subtrees.  
  * Proof anchor: top-level listing and path examples: docs/evidence/INDEX.json, artifacts/evidence\_index.jsonl, audit/EPIC-030\_MANIFEST.json, catalog/manifest.json.  
  * Impact: Evidence lookup requires checking multiple roots.  
* Observed: Endpoint catalogs/snapshots exist in multiple homes.  
  * Proof anchor: find output lists docs/ENDPOINTS\_CATALOG.json, artifacts/audit/ENDPOINTS\_CATALOG.json, audit/qa/hde-epic025/checks/.../endpoints\_catalog.json, docs/run/PROD\_ENDPOINTS.json.  
  * Impact: Catalog identity requires distinguishing docs source, audit mirror, QA snapshots, and run outputs.

## Determinism drift

* Observed: Pure sampler core is explicitly deterministic, while vendor/ingest paths include time, sleep, network, and file I/O.  
  * Proof anchor sampler: engine/sampler/core.py docstring says No randomness, clocks, or external state are consulted.  
  * Proof anchor vendor: engine/bodygraph/vendor\_client.py uses time.monotonic, time.sleep, and urlrequest.Request.  
  * Impact: Determinism posture differs by engine subdomain: sampler/core compute vs vendor acquisition.  
* Observed: Adapter module captures process start time and pid at import.  
  * Proof anchor: adapter/http\_reader.py: \_PROCESS\_STARTED\_AT \= datetime.now(timezone.utc) and \_PROCESS\_PID \= os.getpid().  
  * Impact: Any payload using those values would be process/time-dependent.

## Vendor seam drift

* Observed: Vendor client code lives under engine/bodygraph/vendor\_client.py, while older provider-shaped modules also exist under engine/provider/ and engine/providers/.  
  * Proof anchor: engine file listing includes engine/bodygraph/vendor\_client.py, engine/provider/vendor\_http.py, engine/providers/vendor\_http.py, engine/providers/vendor\_http\_hdapi.py.  
  * Impact: Vendor seam discovery requires differentiating BodyGraph vendor client from provider/provider(s) modules.  
* Observed: DB provider façade lives under engine/db/adapter.py, not top-level adapter/db\_access.py alone.  
  * Proof anchor: engine/db/adapter.py defines class DBAccess; adapter/http\_reader.py imports from engine.db import DBAccess.  
  * Impact: DB/cache path crosses engine and adapter naming boundaries.

## Path-case drift

* Observed: Lowercase epic QA paths coexist with uppercase manifest filenames.  
  * Proof anchor: listing shows audit/qa/hde-epic034/... and audit/EPIC-030\_MANIFEST.json.  
  * Impact: Case conventions vary between QA directory names and top-level audit manifest/report filenames.

## Root proliferation

* Observed: At least 9 top-level roots act as source/evidence/tooling homes: audit/, artifacts/, docs/, catalog/, tools/, scripts/, ci/, .github/, proofs/.  
  * Proof anchor: top-level listing includes all named roots.  
  * Impact: Architecture/evidence audits must traverse several top-level homes rather than a single evidence root.

## Alignment summary table

| Expectation area | Classification | Anchor |
| :---- | :---- | :---- |
| Engine package exists | Aligned | engine present 90 files; engine/compat/compute.py, engine/sampler/core.py |
| Adapter/HTTP layer exists | Partial | adapter/wsgi.py registers reader; engine/http/compat\_handler.py owns compat blueprint |
| Presenter/emitter exists | Aligned | engine/presenter/emitter.py:def emit\_public delegates to canon.sercanon |
| Single emitter | Partial | Generic emitter in engine/presenter/emitter.py; Reader-specific runtime emitter imported as emit\_reader\_public\_envelope |
| CLI surface exists | Aligned | pyproject.toml: hdctl \= "engine.cli.main:cli" |
| Vendor seam outside core compute | Partial | Vendor client under engine/bodygraph/vendor\_client.py; core engine/compat/compute.py imports resolver/vendor error for conjunction resolution |
| DB/cache for BodyGraph storage | Aligned | engine/db/adapter.py:class DBAccess; CLI query against hde.body\_graphs\_current |
| Evidence layout | Partial | Canonical index paths exist, but evidence homes span docs/, artifacts/, audit/, catalog/ |

---

# Negative-Claim Proof Appendix

No “Not found” architectural family claim was used as a conclusion in this audit for the minimum expected families; all minimum families checked were present or represented by present paths.  
Negative searches executed:

* Top-level cli/ directory  
  * Search token: top-level directory named cli  
  * Method/scope: find . \-maxdepth 1 \-type d \-name cli \-print from repo root  
  * Result: 0 output lines  
  * Related positive path: CLI exists under engine/cli/ and scripts under scripts/.  
* Top-level vendor/ directory  
  * Search token: top-level directory named vendor  
  * Method/scope: find . \-maxdepth 1 \-type d \-name vendor \-print from repo root  
  * Result: 0 output lines  
  * Related positive path: vendor code exists under engine/bodygraph/vendor\_client.py, engine/provider/vendor\_http.py, engine/providers/vendor\_http.py, engine/providers/vendor\_http\_hdapi.py.  
* Top-level db/ directory  
  * Search token: top-level directory named db  
  * Method/scope: find . \-maxdepth 1 \-type d \-name db \-print from repo root  
  * Result: 0 output lines  
  * Related positive path: DB code exists under engine/db/ and adapter/db\_access.py.  
* Top-level presenter/ directory  
  * Search token: top-level directory named presenter  
  * Method/scope: find . \-maxdepth 1 \-type d \-name presenter \-print from repo root  
  * Result: ./presenter  
  * Related positive path: engine/presenter/emitter.py also exists.

