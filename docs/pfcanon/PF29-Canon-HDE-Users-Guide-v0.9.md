## **0\. Document Control**

### **0.1 Header**

**Title:** PF29-Canon-HDE-Users-Guide

**Version:** v0.9

**Status:** Canon

**Effective date:** 2026-08-08

**Last Update Gate:** BN 12.6.2 A28-44

**Invocation tag:** INV-f2ac55d77ce9aacc

### **0.2 Scope**

PF29 is the runnable operator and agent guide for using the HD Engine standalone app. It documents only the information needed by a human operator, QA session, implementation agent, or review agent to run the engine surfaces that currently exist, choose closed-rails versus authorized open-rails posture, generate valid JSON payloads, inspect engine outputs, and refresh evidence ledgers after generated evidence changes.

PF29 is a usage guide, not the authoritative source for architecture, transport contracts, infrastructure, schemas, evidence rules, math, QA governance, or build checklist status. It may summarize or duplicate operationally necessary information from PF02, PF05, PF07, PF12, PF14, PF19, PF09, and related PF documents, but those documents remain the authoritative homes for their respective subjects and must feed PF29 when they are updated.

PF29 must not contain information that is not directly relevant to using the HD Engine standalone app. It must not function as a Glow app product UX guide, and it must not describe swiping, daily sets, app onboarding, product copy, app-side HumanDesignAPI use, or any other Glow app behavior outside the HD Engine usage boundary.

PF29 must keep feature availability current. Any command, route, workflow, payload shape, evidence workflow, rails posture, or operational surface described in this guide must be checked against current repo reality before it is documented as available. Planned or intended features may be included only when they are clearly marked as not yet implemented.

### **0.3 Audience**

This guide is for:

* local developers running the HD Engine in a checkout;

* QA operators running deterministic closed-rails checks;

* PO-authorized operators running bounded open-rails vendor checks;

* AI agents preparing or reviewing engine usage workflows;

* implementation agents who need an exact command surface before drafting PR, QA, or OPS artifacts.

### **0.4 Single-home routing**

PF29 is a workflow guide only. It must not replace or redefine these single homes:

* HDE Architecture owns component boundaries and data/control flow.

* HDE CLI/API Vendor Ref owns CLI, HTTP, Reader, Aux, and vendor bytes.

* Glow Infrastructure owns provider, service, base URL, environment, and config-key inventory.

* HDE Schemas and Artifacts owns canonical JSON, manifests, evidence catalogs, Human Evidence Index, Machine Mirror, and path-proof discipline.

* HDE Mechanics Guide owns repo mechanics, harnesses, tools, and implementation responsibilities.

* Glow QA Guide owns QA planning and execution posture.

* HDE Build Checklist owns phase task inventory and PF09 status posture.

* HDE Governance owns acceptance tokens, rails, secret posture, and operational policy.

When this guide names a command, route, or file, it is documenting how to run the current engine. It is not creating a new contract, new token, new PF09 status, new public route, new evidence schema, or new infrastructure fact.

### **0.5 Feature availability legend**

**\[Implemented\]** means the current repository exposes the command, route, or workflow named here.

**\[Dev or QA only\]** means the workflow is intentionally gated to local, dev, test, or QA usage and must not be presented as a production-public surface.

**\[Operator-authorized only\]** means the workflow requires explicit PO or operator authorization, open rails, correct configuration, and secret-safe evidence handling.

**\[Current gap\]** means the workflow or claim is not truthfully implemented end-to-end in the current repository.

**\[Planned, not implemented\]** means the feature may be expected later but is not currently exposed by the implemented CLI or runtime surfaces.

## **1\. Feature availability map**

### 1.1 Implemented local and QA surfaces

| Surface | Current availability | Primary use |
| :---- | :---- | :---- |
| hdctl console entrypoint | \[Implemented\] | Primary CLI entrypoint. |
| python scripts/hdctl.py | \[Implemented\] | Source-tree fallback when console entrypoint is unavailable. |
| hdctl showcompat | \[Implemented\] | Deterministic compat from files, stdin, DB, or vendor-resolved inputs depending on flags and rails. |
| hdctl showcompat \--dump-reader | \[Implemented\] | Emit public Reader JSON to a file while stdout receives full compat JSON. |
| hdctl showcompat \--dump-admin-dir | \[Implemented\] | Emit left/right BodyGraph JSON, composite BodyGraph JSON, compat proof JSON, and .sha256 sidecars. |
| hdctl showcompat \--conjunction | \[Implemented\] | Emit conjunction compat JSON. |
| hdctl aux-preview | \[Implemented\] | Preview Aux narrative text and write IDs-only admin sidecar JSON. |
| hdctl bg:resolve | \[Implemented\] | Resolve BodyGraph control-flow envelope and vendor route-policy classification. Configured-v2 dry-run uses the version-neutral charts resource path and deterministic v2 ChartResult adapter mapping. Configured-v2 non-dry-run mapped-cache persistence is implemented only with explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target; failed gates refuse before the vendor request. Non-v2 configured bases preserve explicit legacy BodyGraph fallback |
| hdctl dev:sampler | \[Implemented\] \[Dev or QA only\] | Deterministic CLI sampler harness. |
| scripts/dev\_start\_reader.sh | \[Implemented\] \[Dev or QA only\] | Start local Reader/dev adapter harness. |
| POST /internal/dev/sampler | \[Implemented\] \[Dev or QA only\] | HTTP dev sampler harness. |
| GET /reader | \[Implemented\] \[Dev or QA only\] | Local Reader v1 public JSON from safe fixture chart files. |
| POST /api/compat/v1 | \[Implemented\] \[Dev or QA only\] | Local HTTP compat computation. Returns 404 in prod. |
| GET /api/aux/narrative and GET /aux/narrative | \[Implemented\] | Aux narrative HTTP preview routes on Reader harness. |
| GET /dev/sampler/conjunction, GET /dev/reader/conjunction, GET /dev/writer/conjunction | \[Implemented\] \[Dev or QA only\] | Dev HTTP conjunction routes. |
| GET /internal/version and HEAD /internal/version | \[Implemented\] | Service identity checks, including production service identity checks when the correct service URL is known. |

### **1.2 Planned or not currently implemented features**

| Feature | Current posture | Operator guidance |
| :---- | :---- | :---- |
| hdctl read singlebg | \[Planned, not implemented\] | Do not document as runnable until the CLI exposes it. |
| hdctl list people | \[Planned, not implemented\] | Do not document as runnable until the CLI exposes it. |
| Fetch person or batch commands | \[Planned, not implemented\] | Explicitly disabled for current alpha-style posture. |
| Production-public POST /api/compat/v1 | \[Current gap\] | Do not claim. Current code returns 404 when APP\_ENV=prod. |
| Direct Glow app HumanDesignAPI credential path | \[Current gap\] | Do not claim. Vendor acquisition belongs to the HD Engine boundary unless a future ADR changes that. |
| Configured-v2 ChartResult dry-run resolution  | \[Implemented, Operator−authorized only\]  | With a configured v2 base and authorized open rails, \--dry-run uses the version-neutral charts route and deterministic v2 ChartResult adapter, reports rows\_written=0, and performs no mapped-cache persistence. |
| Mapped v2 ChartResult adapter output feeding compat computation | \[Implemented, Dev or QA only\] | Closed-rails evidence proves mapped v2 ChartResult adapter output can enter the existing compatibility computation path and preserve public Reader boundary posture. This does not change public Reader bytes or prove broad platform conformance.  |
| ChartSimpleResult as full BodyGraph-detail source | \[Current gap\] | ChartSimpleResult may support bounded smoke, auth, geokey, provider availability, or route-family confirmation, but it is not presumed sufficient for full BodyGraph detail or durable cache use. |
| Durable mapped-cache persistence for configured-v2 chart-backed BodyGraph resolution | \[Implemented, Operator−authorized only\]  | Use only with explicit \--upsert, open rails, non-production-like requested and process environments, a configured v2 base, the required vendor keys, and an available sanctioned direct PostgreSQL target. The workflow persists adapter-mapped HDE data only, verifies canonical read-back, and is idempotent for repeated identity writes. OPS-02 smoke evidence remains separate and does not authorize production writes. |
| PF09 status movement, HDE-FERM008 parent Done, HDE-EPIC037 closeout, production deployment, or final acceptance | \[Current gap\] | HDE-EPIC037 evidence supports later-drain posture only. PF29 must not claim QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, production deployment, final acceptance, or broad HumanDesignAPI v2 platform conformance. |

Feature-availability rows are operator guidance only. They are not backlog items, future-work authorization, PF09 task creation, PF09 status movement, or closure recommendations. Any future work that changes implementation, QA, OPS, evidence, runtime, vendor, architecture, or product behavior must be accounted for in the owning phased PF09 task or subtask, or marked as a PF09 gap in planning artifacts.

## **2\. Rails and environment modes**

### **2.1 Closed-rails QA/default mode**

Use closed rails for deterministic local and QA operations that do not require live vendor network access.

Closed-rails command prefix:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0

Use this prefix for:

* local CLI compat;

* Reader harness startup;

* dev sampler checks;

* local HTTP compat;

* local Aux preview;

* conjunction payload tests;

* canonical JSON checks;

* evidence index and mirror checks;

* any generated evidence refresh that does not require external network access.

Closed rails mean vendor acquisition is refused. A vendor source under SAFE\_MODE=1 is expected to fail closed with provider refusal posture rather than attempting outbound network access.

### **2.2 Open-rails vendor/live mode**

Use open rails only when explicitly authorized and only for bounded vendor or production-relevant work.

Open-rails command prefix:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1

Open rails are required for real vendor acquisition. Open rails are not enough by themselves. The operator must also have:

* explicit authorization for the run;

* the correct HD Engine environment and service target;

* the required configuration keys present;

* secret-safe capture rules;

* a bounded proof scope.

For any QA session tied to an epic that affects user-facing behavior, production runtime behavior, CLI behavior, vendor ingestion, vendor transport, persistence, runtime routes, environment binding, or operational surfaces, closed-rails-only QA is not sufficient. At least one bounded open-rails QA step is required unless the owning QA plan records a valid exemption. PF29 supplies operator recipes only; the QA plan owns step scope, PASS/FAIL predicates, and evidence classification.

Never print secret values. Never capture raw bearer tokens, API keys, geocode keys, raw request bodies, raw response bodies, or raw vendor payload bodies in evidence.

### **2.3 Production mode separation**

Production use falls into three categories:

1. production service identity checks;

2. production or operator compat computation through internal CLI or server-side flows;

3. production/open-rails vendor BodyGraph acquisition.

Do not collapse those categories. In particular, a production /internal/version identity check does not prove production compat availability, and a bounded vendor dry-run does not prove full HumanDesignAPI v2 runtime conformance.

## **3\. Install and entrypoints**

### **3.1 Preferred setup from a clean checkout \[Implemented\]**

Install the engine package in editable mode:

python \-m pip install \-e . \--no-deps \--no-build-isolation

Verify the console entrypoint:

hdctl \--help  
hdctl \--version

### **3.2 Source-tree fallback \[Implemented\]**

If the hdctl console entrypoint is unavailable in a source-tree context, use the fallback launcher:

python scripts/hdctl.py \--help

For all hdctl recipes in this guide, the source-tree fallback is:

python scripts/hdctl.py \<same arguments\>

Example:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \> compat.json

When copying commands from rendered Markdown, chat, or docs, normalize presentation escapes before execution only when the route, environment variables, flags, output file identity, rails posture, and secret posture remain unchanged. Treat PF29 command examples as operator recipes. Exact command bytes matter only when a recipe explicitly says the command bytes are the proof target.

If an operator normalizes syntax in a governed evidence run, the final evidence should preserve the actually executed command when command bytes are material to trust.

## **4\. Local/dev QA Reader harness**

### **4.1 Start the local Reader/dev harness \[Implemented\] \[Dev or QA only\]**

Terminal 1:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev PORT=8000 scripts/dev\_start\_reader.sh

The harness runs the Flask dev adapter through:

python \-m adapter.http\_reader

The helper binds the process through python \-m adapter.http\_reader to host 0.0.0.0 on PORT, with default PORT=8000. Use [http://127.0.0.1:8000](http://127.0.0.1:8000) as the documented local client access address unless an operator context requires a proven exception.

Default local URL family:

http://127.0.0.1:8000

Dev sampler URL:

http://127.0.0.1:8000/internal/dev/sampler

### **4.2 Healthcheck the dev sampler route \[Implemented\] \[Dev or QA only\]**

Terminal 2:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev DEV\_SAMPLER\_URL=http://127.0.0.1:8000/internal/dev/sampler scripts/qa/dev\_sampler\_healthcheck.py

The healthcheck starts or targets the Reader harness, posts the sampler payload, records the dev response, and also records prod-gating diagnostics where applicable.

## **5\. Dev sampler workflows**

### **5.1 HTTP dev sampler \[Implemented\] \[Dev or QA only\]**

Route:

POST /internal/dev/sampler

Gate:

APP\_ENV must be dev, test, or local.

Allowed request keys:

* viewer\_id

* candidate\_ids

* seed

Example request body:

{"viewer\_id":"qa-viewer-001","candidate\_ids":\["qa-candidate-001","qa-candidate-002"\],"seed":"pf29-smoke-001"}

Example local command:

curl \-sS \-X POST http://127.0.0.1:8000/internal/dev/sampler \-H 'Content-Type: application/json; charset=utf-8' \--data-binary '{"viewer\_id":"qa-viewer-001","candidate\_ids":\["qa-candidate-001","qa-candidate-002"\],"seed":"pf29-smoke-001"}' \> dev\_sampler\_response.json

Expected successful response posture:

* canonical JSON;

* viewer\_id;

* meta.seed;

* ordered candidate\_ids;

* Cache-Control: no-store;

* no ETag.

### **5.2 CLI dev sampler \[Implemented\] \[Dev or QA only\]**

Create a candidate payload:

cat \> sampler\_candidates.json \<\<'EOF'  
{"candidates":\[{"person\_uid":"qa-candidate-001","weight":1.0,"compat\_score":50,"band":"Open"},{"person\_uid":"qa-candidate-002","weight":1.0,"compat\_score":75,"band":"Warm"}\]}  
EOF

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev hdctl dev:sampler \--viewer qa-viewer-001 \--candidates-file sampler\_candidates.json \--seed pf29-smoke-001 \> sampler\_cli\_response.json

The CLI sampler is dev/admin only. If APP\_ENV is not dev, test, or local, expect DEV\_ADMIN\_ONLY.

## **6\. Reader v1 local workflow**

### **6.1 Reader route \[Implemented\] \[Dev or QA only\]**

Route:

GET /reader?v=1\&a=\<fixture-chart-a\>\&b=\<fixture-chart-b\>\&a\_tz=\<iana-or-offset\>\&b\_tz=\<iana-or-offset\>

Rules:

* v=1 is required.

* APP\_ENV=dev is required.

* a and b must point to safe chart files under fixtures/charts.

* Missing timezone in a chart may be supplied through a\_tz or b\_tz.

* Success returns public Reader bytes with JSON content type, cache headers, ETag, and content length.

Reader v1 public output is a bands-only public posture. Numeric/admin details belong to CLI/admin dumps, not Reader public JSON.

### **6.2 Example local Reader request**

Start the Reader harness first.

Then run a request using fixture chart paths that exist in the checkout:

curl \-sS 'http://127.0.0.1:8000/reader?v=1\&a=fixtures/charts/\<left-chart\>.json\&b=fixtures/charts/\<right-chart\>.json\&a\_tz=UTC\&b\_tz=UTC' \> reader\_response.json

Replace \<left-chart\> and \<right-chart\> with real fixture filenames.

### **6.3 Reader JSON from CLI**

For local QA, the most reliable way to emit Reader JSON without HTTP fixture path concerns is hdctl showcompat \--dump-reader:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \> audit/tmp/pf29/compat.json

## **7\. Compat workflows**

### **7.1 Magic-10 category IDs**

Use these category IDs in viewer preferences:

1. heat

2. harmony

3. communication

4. alignment

5. comfort

6. consistency

7. expansion

8. creativity

9. drive

10. balance

### **7.2 Local HTTP compat \[Implemented\] \[Dev or QA only\]**

Route:

POST /api/compat/v1

Example request file:

cat \> compat\_request.json \<\<'EOF'  
{"a":{"person\_uid":"qa-left"},"b":{"person\_uid":"qa-right"},"viewer\_prefs":{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}  
EOF

Example local command:

curl \-sS \-X POST http://127.0.0.1:8000/api/compat/v1 \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

Production boundary:

POST /api/compat/v1 is not production-public in the current repository. It returns 404 when APP\_ENV=prod. Production compat computation, when needed, must be treated as internal/server-side or CLI/operator workflow, not a public HTTP claim.

### **7.3 CLI compat from payload files \[Implemented\]**

Use CLI payload mode for deterministic local or QA compat without DB or vendor I/O.

Create pair.json:

cat \> pair.json \<\<'EOF'  
{"left":{"person\_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person\_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}  
EOF

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \> compat.json

Fallback:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \> compat.json

Other supported file forms:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--a-file left.json \--b-file right.json \> compat.json  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \< pair.json \> compat.json

Success bytes are LF-terminated canonical JSON on stdout.

### **7.4 Optional viewer preferences file \[Implemented\]**

Create viewer\_prefs.json:

cat \> viewer\_prefs.json \<\<'EOF'  
{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}  
EOF

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--viewer-prefs-file viewer\_prefs.json \> compat.json

## **8\. BodyGraph/admin JSON export workflow**

### **8.1 Main local QA payload generation \[Implemented\]**

Use this as the main end-to-end local QA workflow because it uses current repository code and produces useful JSON payloads without vendor I/O.

Create pair.json as shown in §7.3.

Run:

mkdir \-p audit/tmp/pf29/compat\_admin  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Fallback:

mkdir \-p audit/tmp/pf29/compat\_admin  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Expected outputs when the pair file is named pair.json:

audit/tmp/pf29/compat.json  
audit/tmp/pf29/reader.json  
audit/tmp/pf29/compat\_admin/pair.left.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.right.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.composite.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.compat.proof.json

Expected sidecars for admin dumps:

audit/tmp/pf29/compat\_admin/pair.left.bodygraph.json.sha256  
audit/tmp/pf29/compat\_admin/pair.right.bodygraph.json.sha256  
audit/tmp/pf29/compat\_admin/pair.composite.bodygraph.json.sha256  
audit/tmp/pf29/compat\_admin/pair.compat.proof.json.sha256

The admin dump helper writes canonical JSON and .sha256 sidecars, and enforces local file mode 0600 on the dump files and sidecars. Admin dump files are local/admin artifacts and are not Reader public output.

### **8.2 What each generated file is for**

| File | Use |
| :---- | :---- |
| compat.json | Full CLI compat envelope for local/admin inspection and downstream Aux preview. |
| reader.json | Public Reader JSON envelope emitted by the same local run. |
| pair.left.bodygraph.json | Left person BodyGraph-shaped admin JSON. |
| pair.right.bodygraph.json | Right person BodyGraph-shaped admin JSON. |
| pair.composite.bodygraph.json | Pair/composite BodyGraph-shaped admin JSON. |
| pair.compat.proof.json | Admin proof JSON with category order, thresholds, signals, and per-category proof posture. |

## **9\. Conjunction workflows**

### **9.1 CLI conjunction from payload \[Implemented\]**

Create conjunction\_pair.json:

cat \> conjunction\_pair.json \<\<'EOF'  
{"left":{"person\_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person\_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}  
EOF

Run closed rails:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file conjunction\_pair.json \> conjunction.json

Other supported forms:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--a-file left.json \--b-file right.json \> conjunction.json  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \< conjunction\_pair.json \> conjunction.json

### **9.2 CLI conjunction from DB or vendor source \[Implemented with rails constraints\]**

DB mode:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--user-a \<user\_a\> \--user-b \<user\_b\> \--source db \> conjunction\_db.json

Vendor mode requires open rails and full birth tuples for both people:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl showcompat \--conjunction \--user-a \<user\_a\> \--user-b \<user\_b\> \--source vendor \--birthdate-a YYYY-MM-DD \--birthtime-a HH:MM \--location-a "Place" \--birthdate-b YYYY-MM-DD \--birthtime-b HH:MM \--location-b "Place" \> conjunction\_vendor.json

Closed rails may emit explicit refusal codes for unresolved vendor inputs. Do not treat a refusal as a successful vendor acquisition.

### **9.3 Dev HTTP conjunction routes \[Implemented\] \[Dev or QA only\]**

Routes:

GET /dev/sampler/conjunction  
GET /dev/reader/conjunction  
GET /dev/writer/conjunction

Required query parameters:

* a\_user\_id

* b\_user\_id

Optional query parameters:

* a\_birthdate

* a\_birthtime

* a\_location

* b\_birthdate

* b\_birthtime

* b\_location

Example:

curl \-sS 'http://127.0.0.1:8000/dev/reader/conjunction?a\_user\_id=qa-left\&b\_user\_id=qa-right\&a\_birthdate=1990-01-01\&a\_birthtime=12:00\&a\_location=Paris%2C%20FR\&b\_birthdate=1991-02-03\&b\_birthtime=08:30\&b\_location=Lisbon%2C%20PT' \> dev\_reader\_conjunction.json

These routes are APP\_ENV gated through the dev/admin gate and build canonical request fields from query parameters.

## **10\. Aux narrative preview workflow**

### **10.1 CLI Aux preview from compat output \[Implemented\]**

Use a compat JSON file produced by hdctl showcompat.

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file audit/tmp/pf29/compat.json \--category harmony \--band Cool \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

CLI options:

* \--pair-file \<compat.json\>

* \--category \<slug\>

* \--band \<Cool|Open|Warm|Glow\>

* \--perspective \<personal|shared\>

* \--show-narrative

* \--admin-out \<ids.json\>

The admin sidecar is IDs-only. It is not raw payload capture.

### **10.2 HTTP Aux narrative routes \[Implemented\]**

Routes on the Reader harness:

GET /api/aux/narrative  
GET /aux/narrative

Key query parameters:

* category

* band

* perspective

* optional viewer\_top

* optional flags or flag

* optional families\_fired

* optional release\_id

* optional pack\_sha

Example:

curl \-sS 'http://127.0.0.1:8000/api/aux/narrative?category=harmony\&band=Cool\&perspective=shared' \> aux\_narrative.txt

The route emits text/plain and includes narrative pack/composition headers. Suppressed output may be an empty 200 body with no ETag.

## **11\. BodyGraph resolve and vendor ingest workflow**

### **11.1 Closed-rails default dry path \[Implemented\]**

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl bg:resolve \--user qa-user \--source auto \--dry-run \> bg\_resolve\_auto.json

Current bg:resolve \--source auto or \--source db is a control-flow envelope path for this command. It must not be overclaimed as proof that DB rows were read unless the emitted payload says so.

### **11.2 Open-rails configured-v2 vendor dry-run \[Implemented\] \[Operator−authorized only\]**

Vendor source requires a full birth tuple.

Run only after confirming authorization and required environment keys are present without printing their values:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json

With a configured v2 base, current dry-run behavior uses the version-neutral charts route, route-metadata Bearer/geokey posture, and deterministic v2 ChartResult adapter mapping. Closed rails still refuse before outbound I/O. Dry-run output may include resolver route policy, redacted request posture, adapter status, resolved mapped BodyGraph/person posture, cache posture, and ingest rows\_written=0.

Success is determined by the emitted JSON payload. For dry-run, do not claim persistence.

### **11.3 Non-v2 legacy fallback \[Implemented with rails and config constraints\]**

When the configured base is non-v2, explicit legacy BodyGraph fallback is preserved. Treat this as legacy fallback only, not v2 runtime conformance.

For non-v2 legacy fallback, persistent success must be determined by fields emitted in the JSON payload, including rows\_written, db\_rows\_after, db\_emitted\_sha256, and parity\_match where present. Do not claim rows were written by assumption.

### **11.4 Configured-v2 mapped-cache persistence \[Implemented\] \[Operator−authorizedonly\]**

Configured-v2 chart-backed bg:resolve supports bounded mapped-cache persistence of adapter-mapped HDE data. Use it only after explicit authorization and only with open rails, non-production-like requested and process environments, a configured v2 base, the required vendor keys, DATABASE\_URL available to the sanctioned direct PostgreSQL provider, and explicit \--upsert. Missing \--upsert, a production-like environment, retired bridge configuration, or an unavailable sanctioned database target fails closed before the vendor request.

Run:

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--upsert \> vendor\_bodygraph\_mapped\_cache.json

Treat persistence as successful only when the emitted JSON has status=ok and the ingest object reports the observed rows\_written, rows\_after, read\_back\_match, and idempotent values. The path writes only the projected mapped payload and verifies canonical read-back. Do not infer persistence from exit code or vendor response alone.

This workflow does not authorize production writes or substitute for the separately governed OPS-02 evidence axis.

Generic BodyGraph ingest remains guarded from raw v2 ChartResult persistence. Do not use generic BodyGraph ingest as proof that configured-v2 mapped-cache persistence exists.

Do not treat charts/simple success or ChartSimpleResult as proof of full BodyGraph detail. ChartSimpleResult may remain useful for bounded live smoke, authentication proof, geokey proof, provider availability proof, and minimal route-family confirmation, but the mapped configured-v2 path uses ChartResult.

Dual-route policy is not implemented and requires a future ADR.

## **12\. HDAPI configuration and geokey/header syntax**

### **12.1 Environment keys**

Current canonical keys:

HD\_API\_BASE\_URL  
HD\_API\_KEY  
GEO\_API\_KEY

Compatibility alias:

HDAPI\_BASE\_URL

HDAPI\_BASE\_URL is compatibility-only and may be used only when HD\_API\_BASE\_URL is absent. If both are present and conflict, the vendor configuration is ambiguous and must fail closed.

For configured-v2 mapped-cache persistence, DATABASE\_URL is the sole canonical HDE database endpoint key and direct psycopg is the sole active database transport. DB\_BRIDGE\_URL, DB\_FORCE\_BRIDGE, and DB\_ALLOW\_BRIDGE\_IN\_PROD are retired. Their presence is configuration drift and fails closed before provider construction or external I/O. Record only key names or redacted presence posture, never values.

### **12.2 Header posture by route family**

Legacy v1 BodyGraph-style routes:

| Runtime resource path | Auth header posture |
| :---- | :---- |
| bodygraphs | HD-Api-Key: \<redacted\> |
| bodygraphs/simple | HD-Api-Key: \<redacted\> |

Current v2 chart-style routes:

| Runtime resource path | Auth header posture | Geocode posture |
| :---- | :---- | :---- |
| charts | Authorization: Bearer \<redacted\> | Requires HD-Geocode-Key: \<redacted\> |
| charts/simple | Authorization: Bearer \<redacted\> | Requires HD-Geocode-Key: \<redacted\> |
| charts/coordinates | Authorization: Bearer \<redacted\> | Uses coordinates; geocode key not required for that route. |

Use version-neutral runtime resource paths. Do not hardcode /v1 or /v2 as active runtime request-construction inputs. The configured HD\_API\_BASE\_URL owns any vendor API version prefix.

### **12.3 Secret handling**

Allowed in commands and evidence:

* key names;

* route-family labels;

* redacted header family names;

* high-level status code or error class;

* bounded result summaries;

* hashes of governed artifacts.

Disallowed in commands, logs, docs, and evidence:

* raw bearer token values;

* raw API key values;

* raw geocode key values;

* raw request bodies;

* raw response bodies;

* raw vendor payload bodies;

* uncontrolled production user PII.

## **13\. Production posture**

### **13.1 Production Reader/service identity checks \[Implemented\]**

Use the production service base URL from Glow Infrastructure. Do not guess production URLs.

Safe service identity checks:

curl \-i \<production-hde-base-url\>/internal/version  
curl \-I \<production-hde-base-url\>/internal/version

/internal/version emits no-store JSON identity bytes for GET and supports HEAD parity. It is an identity and runtime posture check. It is not an A7 success proof surface and not a compat proof.

### **13.2 Production compat posture \[Current gap for public HTTP\]**

Do not document POST /api/compat/v1 as production-public. Current code returns 404 when APP\_ENV=prod.

Production compat computation, if needed, must be handled as one of:

* internal/server-side workflow;

* CLI/operator workflow;

* future explicit production contract after canon and implementation change.

PF29 does not create that production public endpoint.

### **13.3 Production/open-rails vendor BodyGraph acquisition \[Operator-authorized only\]**

This section governs production and production-like posture. Configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter under authorized open rails. With a non-v2 configured base, explicit legacy fallback may proceed under its normal rails, configuration, and emitted-payload success rules.

Configured-v2 mapped-cache persistence is implemented only for the bounded non-production workflow in §11.4. Production or production-like non-dry-run attempts fail closed with PROVIDER\_WRITE\_UNSUPPORTED even when \--upsert is supplied. Do not treat the bounded non-production workflow or OPS-02 evidence as production write authorization or broad v2 conformance.

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json

Persistent success for any supported non-v2 legacy fallback must be determined by emitted JSON fields, not by assumption.

## **14\. Evidence and validation workflow**

### **14.1 When to run evidence refresh**

Run evidence refresh and checks when a workflow creates or changes governed evidence under governed roots such as audit/\*\*, artifacts/\*\*, or docs/\*\* and that evidence is intended to be promoted into the Human Evidence Index and Machine Mirror.

Do not index scratch output under audit/tmp/pf29/\*\* unless the output is intentionally promoted as governed evidence through the owning evidence process.

For PO-authorized OPS or open-rails evidence that is already retained under a nested evidence root, use a manifest to map approved deliverable names to retained evidence paths without moving or deleting evidence. A nested root such as audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/ is acceptable only when the manifest preserves the approved deliverable identity, retained path, status, and nonclaim posture.

Prefer machine-readable JSON only when the approved task requires JSON semantics. Text or markdown summaries may be used only when explicitly mapped by the manifest and not treated as schema-governed JSON.

When a QA PASS, operator review, or closeout recommendation relies on refreshed governed evidence outside the QA root, preserve a routing receipt or equivalent review trail that shows whether the refresh was routed through PR work, OPS work, QA plan update, or documentation update. A QA log alone must not be treated as sufficient proof that non-QA-root governed evidence refreshes were authorized, performed, and bound.

### **14.2 Write/update sequence**

Run from the repository root under closed rails:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/orientation\_demo.py

### **14.3 Check sequence**

Run from the repository root under closed rails:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py \--check  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/validate\_evidence\_paths.py  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python ci/checks/check\_mirror\_schema.sh  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 bash ci/checks/check\_evidence\_index\_hash.sh

ci/checks/check\_mirror\_schema.sh is a Python entrypoint despite the .sh filename. Use python ci/checks/check\_mirror\_schema.sh unless the executable bit and shebang invocation are intentionally being tested.

The checker always reads artifacts/evidence\_index.jsonl through fixed repository-relative paths and does not support caller-selected mirror arguments. Run it from the repository root and omit any appended mirror path; an appended operand is ignored.

Do not invoke the checker with bash or sh. Shell-parser output is an invocation or tooling defect, not a Machine Mirror schema finding. A MISSING:artifacts/evidence\_index.jsonl result obtained outside the repository root is a locus defect until the supported command is rerun from the repository root. Only the supported invocation's exit status and validator output may be used to claim the Mirror-schema result, and the actual command transcript must be preserved.

## **15\. Minimum runnable recipes**

### **Recipe A — local QA Reader plus dev sampler**

Terminal 1:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev PORT=8000 scripts/dev\_start\_reader.sh

Terminal 2:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev DEV\_SAMPLER\_URL=http://127.0.0.1:8000/internal/dev/sampler scripts/qa/dev\_sampler\_healthcheck.py

### **Recipe B — local CLI compat plus BodyGraph/admin JSON payloads**

cat \> pair.json \<\<'EOF'  
{"left":{"person\_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person\_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}  
EOF  
mkdir \-p audit/tmp/pf29/compat\_admin  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Fallback:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Expected files:

audit/tmp/pf29/compat.json  
audit/tmp/pf29/reader.json  
audit/tmp/pf29/compat\_admin/pair.left.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.right.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.composite.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.compat.proof.json

### **Recipe C — local HTTP compat**

Start Reader as in Recipe A.

cat \> compat\_request.json \<\<'EOF'  
{"a":{"person\_uid":"qa-left"},"b":{"person\_uid":"qa-right"},"viewer\_prefs":{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}  
EOF  
curl \-sS \-X POST http://127.0.0.1:8000/api/compat/v1 \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

### **Recipe D — local Aux narrative preview**

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file audit/tmp/pf29/compat.json \--category harmony \--band Cool \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

### **Recipe E — local conjunction compat from payload**

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file pair.json \> audit/tmp/pf29/conjunction.json

### **Recipe F — open-rails configured-v2 vendor dry-run**

Before running, confirm the operator environment has HD\_API\_BASE\_URL, HD\_API\_KEY, and, for geocode-required routes, GEO\_API\_KEY. Do not print their values.

With a configured v2 base, current expected dry-run behavior is charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0.

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json

### **Recipe G — operator-authorized configured-v2 mapped-cache persistence**

Use only for a separately authorized, bounded non-production run. Confirm that the required vendor keys and DATABASE\_URL are present without printing their values, the configured base is v2, the requested and process environments are non-production-like, and no retired bridge key is present.

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--upsert \> vendor\_bodygraph\_mapped\_cache.json

Expect status=ok, adapter status=mapped, mapped-only cache posture, and ingest fields that report rows\_written, rows\_after, read\_back\_match, and idempotent. A repeated same-identity run may report rows\_written=0 and idempotent=true; do not treat that as failure when canonical read-back still matches and the identity cardinality remains one.

This recipe is not production-write authorization, OPS authorization, QA PASS, PF09 status movement, deployment, migration, or closeout.

## **16\. Known limitations and nonclaims**

PF29 must preserve these nonclaims:

* POST /api/compat/v1 is not production-public because current code returns 404 when APP\_ENV=prod.

* /internal/dev/sampler and /dev/\*/conjunction are dev/test/local-only.

* GET /reader is a dev/local Reader v1 harness route and requires safe fixture chart paths.

* Current configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter. For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved.

* Current configured-v2 evidence supports scoped dry-run mapping, mapped v2 output feeding compatibility computation, bounded mapped-cache persistence of adapter-mapped HDE data, and a separate PO-authorized OPS-02 smoke proving one configured-v2 request, mapped-only persistence, canonical read-back, idempotence, and production-like refusal. It does not authorize production upsert, public Reader changes, new public routes, app-side vendor ownership, or broad HumanDesignAPI v2 platform conformance.

* Configured-v2 non-dry-run persistence requires explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target. Missing intent or direct access and every production-like attempt fail closed; runtime selection does not fall back to a bridge or alternate database transport.

* PF29 does not complete HDE-FERM008.7 through HDE-FERM008.12, does not move PF09 status, does not mark HDE-FERM008 parent Done, and does not perform HDE-EPIC037 closeout, production deployment, OPS completion, PO closeout, board update, PF-canon update, or final acceptance.

* No workflow may record raw vendor payload bodies, raw request bodies, raw response bodies, bearer token values, API key values, geocode key values, or production user PII.

* Evidence-generation workflows are not user-facing runtime workflows. Evidence outputs under audit/\*\* and artifacts/\*\* require Human Evidence Index, Machine Mirror, and path-proof discipline when promoted.

## **17\. Troubleshooting**

| Symptom | Likely cause | Operator action |
| :---- | :---- | :---- |
| hdctl: command not found | Console entrypoint is not installed in the current environment. | Run python \-m pip install \-e . \--no-deps \--no-build-isolation, or use python scripts/hdctl.py. |
| VERSION\_FLAG\_WITH\_COMMAND | \--version was passed with another command. | Run hdctl \--version by itself. |
| DEV\_ADMIN\_ONLY | A dev/admin CLI command was run without APP\_ENV=dev, test, or local. | Add APP\_ENV=dev for local QA. |
| HTTP 403 from /internal/dev/sampler | APP\_ENV is not dev, test, or local. | Restart the harness with APP\_ENV=dev. |
| HTTP 404 from POST /api/compat/v1 in prod | Expected current production block. | Use dev/QA HTTP compat locally or an internal CLI/server-side production workflow. |
| ERR\_READER\_FORBIDDEN | Reader v1 route was called outside APP\_ENV=dev. | Use local dev harness or the correct production identity route instead. |
| ERR\_READER\_MISSING\_TZ\_A or ERR\_READER\_MISSING\_TZ\_B | Fixture chart lacks timezone and no override was supplied. | Add a\_tz or b\_tz, or use fixture files that include timezone. |
| MISSING\_VENDOR\_INPUT | Vendor source was requested without full birth tuple. | Supply birthdate, birthtime, and location. |
| PROVIDER\_REFUSED | Vendor source was attempted under closed rails. | Confirm authorization, then run with SAFE\_MODE=0 ALLOW\_NETWORK=1. |
| PROVIDER\_NETWORK\_BLOCKED | Network access is disabled. | Confirm authorization and set ALLOW\_NETWORK=1 only for bounded open-rails runs. |
| PROVIDER\_CONFIG\_MISSING | Required vendor config is absent. | Confirm HD\_API\_BASE\_URL, HD\_API\_KEY, and when needed GEO\_API\_KEY, without printing values. |
| PROVIDER\_CONFIG\_INVALID | Vendor configuration is ambiguous or violates contract. | Check for conflicting HD\_API\_BASE\_URL and HDAPI\_BASE\_URL, invalid base URL, or unpinned vendor policy. |
| PROVIDER\_ROUTE\_REQUIRES\_ADAPTER | Generic BodyGraph ingest attempted to build a configured-v2 chart request outside the resolver adapter path. | Use bg:resolve \--source vendor through the configured-v2 resolver path. Add \--dry-run for mapping-only use; add \--upsert only for the authorized bounded persistence workflow in §11.4. Do not treat generic BodyGraph ingest as adapter-backed v2 resolution. |
| PROVIDER\_WRITE\_UNSUPPORTED | Explicit upsert intent is missing, the environment is production-like, or the mapped-cache input or projection violates the supported contract. | Use \--dry-run for mapping-only work. Use \--upsert only within the authorized non-production workflow in §11.4. Never bypass a production-like refusal.  |
| DB\_WRITER\_UNAVAILABLE  | DATABASE\_URL is absent or unavailable, a retired bridge key is present, or the sanctioned direct provider or write transaction could not be used. | Confirm authorization and names-only DATABASE\_URL presence, remove retired bridge keys from the execution environment, and retry only within the authorized workflow. Do not print values or fall back to another transport. |
| DB\_QUERY\_FAILED | A DB query, identity-cardinality check, mapped-cache read-back, or canonical-parity check failed. | Inspect the emitted typed error and direct database posture. Do not claim persistence or read-back success. |
| BODYGRAPH\_NOT\_FOUND | No BodyGraph row was found for the requested user. | Confirm the user ID and whether ingest/persistence has actually completed. |
| Evidence mirror or hash check fails | Generated evidence changed without refresh, or path-proof/index/mirror drift exists. | Run the write/update sequence, then the check sequence in §14. |

## **18\. Quick command reference**

Install and verify:

python \-m pip install \-e . \--no-deps \--no-build-isolation  
hdctl \--help  
hdctl \--version

Start local Reader harness:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev PORT=8000 scripts/dev\_start\_reader.sh

Run dev sampler healthcheck:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev DEV\_SAMPLER\_URL=http://127.0.0.1:8000/internal/dev/sampler scripts/qa/dev\_sampler\_healthcheck.py

Run CLI compat:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \> compat.json

Run CLI compat with Reader and admin dumps:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Run local HTTP compat:

curl \-sS \-X POST http://127.0.0.1:8000/api/compat/v1 \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

Run local conjunction:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file pair.json \> conjunction.json

Run Aux preview:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file compat.json \--category harmony \--band Cool \--perspective shared \--show-narrative \--admin-out aux\_sidecar.json

Run open-rails configured-v2 vendor dry-run. With a configured v2 base, expect charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json

Run operator-authorized non-production configured-v2 mapped-cache persistence only after confirming required vendor keys and DATABASE\_URL are present without printing values, no retired bridge key is present, and the environment is non-production-like:

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--upsert \> vendor\_bodygraph\_mapped\_cache.json

APP\_ENV=dev constrains only the local HD Engine process. It must not be used to classify the external vendor API base or environment target as nonproduction. External-target authority must come from the exact approved contract and explicit PO decision, not from URL substrings or the local APP\_ENV value.

Production-like writes remain refused. This command does not itself authorize OPS execution or production persistence.

Refresh evidence after governed generated evidence changes:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/orientation\_demo.py

Check evidence after refresh:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/update\_evidence\_index.py \--check  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/validate\_evidence\_paths.py  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python ci/checks/check\_mirror\_schema.sh  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 bash ci/checks/check\_evidence\_index\_hash.sh

