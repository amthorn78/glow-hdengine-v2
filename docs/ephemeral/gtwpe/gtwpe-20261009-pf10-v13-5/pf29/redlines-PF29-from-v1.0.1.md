# PF29 v1.0.1 exact redlines — T-PF29

Run: gtwpe-20261009-pf10-v13-5 / T-PF29, preparation revision 1, 2026-10-09.
Originating preparer: this Nathan-started T-PF29 document session, running TW-DRAIN-10 100926.1. No separate session identifier is exposed; the task, original fingerprint and repository output namespace identify the session's package.
Target: docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.1.md at e7265a090ad0cc8de5f36de2f19481216aa3d073.
Original: v1.0.1, UTF-8 native repository content, 60103 bytes; SHA-256 e03cb9ec8005d1a7f18acb03b96623c608e896da1baf7d5121e5e5a1a14a4aaf; Git blob 2f1c6fb1d722ace3c2285c6bb77bb323b4c9cec0.
Ledger: docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md, pinned f057d124176143b3e02ba7ad599880fd7e9991b1, row T-PF29.
Companion: docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/pf29/redlines-PF29-from-v1.0.1.proof-log.md.

All operations resolve independently against the unchanged original. Locations use exact original heading paths and literal blocks, not line numbers alone. The four-backtick text fences contain literal payloads. Precisely one LF immediately before each closing fence is a delimiter and is excluded from the payload; any additional trailing LF belongs to the payload. Preserve every backslash and all whitespace literally. Line/character offsets are supplementary, zero-based half-open character spans, not byte locators. The document-control header is reserved for TW-APPLY-10's derived metadata plan. Preparation validation: all 23 REPLACE blocks are unique and mutually disjoint; full selected-source coverage is recorded in the companion report. Repository save readiness is established by that report's verified receipt, not this sentence.

## RL-002

Operation: REPLACE
Original heading path:

# **0\. Document Control** > ## **0.4 Single-home routing**

Location: original lines 45–45; original character span [2532, 2610).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
* PF02-Canon-HDE-Architecture owns component boundaries and data/control flow.
````

New text:

````text
* PF01-Canon-HDE-Math-Spec owns Gate mechanics, intrinsic identities, category order, scores and bands.  
    
* PF02-Canon-HDE-Architecture owns component boundaries and data/control flow.
````

## RL-001

Operation: REPLACE
Original heading path:

# **0\. Document Control** > ## **0.5 Feature availability legend**

Location: original lines 65–65; original character span [3658, 3758).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
**\[Implemented\]** means the current repository exposes the command, route, or workflow named here.
````

New text:

````text
**\[Implemented\]** means the checked-in repository exposes the command, route, or workflow named here. It does not establish a successful run, deployment, available database rows, or valid external configuration.
````

## RL-003

Operation: REPLACE
Original heading path:

# **1\. Feature availability map** > ## **1.1 Implemented local and QA surfaces**

Location: original lines 77–77; original character span [4388, 4433).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **1.1 Implemented local and QA surfaces**

````

New text:

````text
## **1.1 Implemented local and QA surfaces**

Availability below is based on bounded read-only inspection of repository snapshot `e7265a090ad0cc8de5f36de2f19481216aa3d073`. Commands are examples to run from the repository root with their stated prerequisites; no recipe was executed for this revision.

````

## RL-004

Operation: REPLACE
Original heading path:

# **1\. Feature availability map** > ## **1.1 Implemented local and QA surfaces**

Location: original lines 92–92; original character span [6191, 6304).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
| GET /reader | \[Implemented\] \[Dev or QA only\] | Local Reader v1 public JSON from safe fixture chart files. |
````

New text:

````text
| GET /reader | \[Implemented\] \[Dev or QA only\] | Local Reader v1 projection from complete mapped fixture charts with Gates and verified identities; timezone overrides remain required when absent. |
| POST /api/reader?v=1 and POST /api/reader?v=2 | \[Implemented\] | Versioned production Reader route with read-only current-row resolution. A declared route does not prove live database success or deployment. |
| python tools/config/generate_config_artifacts.py --compare-goldens . | \[Implemented\] | Read-only complete golden comparison against the explicitly selected candidate root; see §7.6. |
| python tools/bodygraph/check_magic10_gate_readiness.py | \[Implemented\] | Read-only readiness for an explicit UUID selection and an available database; see §7.7. |
````

## RL-005

Operation: REPLACE
Original heading path:

# **2\. Rails and environment modes** > ## **2.2 Open-rails vendor/live mode**

Location: original lines 175–175; original character span [11578, 11765).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
PF29 supplies operator recipes only. The owning QA plan determines whether a bounded open-rails QA step is required and owns step scope, PASS/FAIL predicates, and evidence classification.
````

New text:

````text
PF29 supplies operator recipes only. For an epic touching a surface used to produce a production feature described as functional in canon, consult PF19-Canon-Glow-QA-Guide and PF10-HDE-Build-Notes for the mandatory live vendor-backed synthetic open-rails test. Closed fixtures, database reads and deployed-service identity checks do not substitute for it. The owning QA plan defines the bounded step, request limit, stop checks, predicates and evidence classification.

A Product Owner direction for an identified vendor task permits the directed agent to execute that task under the same controls as a human executor. It provides no standing vendor-call permission. Pass environment-held vendor configuration to the product process; do not ask the Product Owner to type or paste values or put values in command arguments. Check HD_API_KEY and GEO_API_KEY, and the approved HD_API_BASE_URL (or compatibility-only HDAPI_BASE_URL), as SET or UNSET; never expose the values. Missing configuration prevents the call; an already-started step remains tooling-blocked under its owning QA contract. Preserve the compatibility base-URL alias when it is the only configured base.
````

## RL-006

Operation: REPLACE
Original heading path:

# **3\. Install and entrypoints** > ## **3.1 Preferred setup from a clean checkout \[Implemented\]**

Location: original lines 193–203; original character span [12667, 13058).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **3.1 Preferred setup from a clean checkout \[Implemented\]**

A clean checkout requires Python 3.10 or newer and an environment that already provides setuptools\>=68 and wheel for the no-build-isolation command. Install the engine package in editable mode:

python \-m pip install \-e . \--no-deps \--no-build-isolation

Verify the console entrypoint:

hdctl \--help  
hdctl \--version


````

New text:

````text
## **3.1 Preferred setup from a clean checkout \[Implemented\]**

A clean checkout requires Python 3.10 or newer and an environment that already provides setuptools\>=68 and wheel for the no-build-isolation command. Install the engine package in editable mode:

python \-m pip install \-e . \--no-deps \--no-build-isolation

Verify the console entrypoint:

hdctl \--help  
hdctl \--version

This editable/source-tree setup does not establish packaged-wheel admission. HDE Build Notes records the non-editable wheel omission and fail-closed refusal; distribution remains with the packaging owner and Product Owner. Install the runtime dependencies required by the workflow from `requirements.txt` in the selected environment; `--no-deps` does not install them. Do not infer readiness from the console entrypoint alone.


````

## RL-007

Operation: REPLACE
Original heading path:

# **6\. Reader v1 local workflow** > ## **6.1 Reader route \[Implemented\] \[Dev or QA only\]**

Location: original lines 322–322; original character span [17452, 17515).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
* a and b must point to safe chart files under fixtures/charts.
````

New text:

````text
* a and b must point to safe, complete mapped chart files under fixtures/charts with Gates and identity fields; a birth tuple alone is insufficient.
````

## RL-008

Operation: REPLACE
Original heading path:

# **6\. Reader v1 local workflow** > ## **6.2 Example local Reader request**

Location: original lines 332–341; original character span [18105, 18561).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **6.2 Example local Reader request**

Start the Reader harness first.

Then run a request using fixture chart paths that exist in the checkout:

curl \-sS '[http://127.0.0.1:8000/reader?v=1\\\&a=fixtures/charts/\\](http://127.0.0.1:8000/reader?v=1\\&a=fixtures/charts/\\)\<left-chart\>.json\&b=fixtures/charts/\<right-chart\>.json\&a\_tz=UTC\&b\_tz=UTC' \> reader\_response.json

Replace \<left-chart\> and \<right-chart\> with real fixture filenames.


````

New text:

````text
## **6.2 Example local Reader request**

Start the Reader harness first. The checked-in `fixtures/charts/alice.json` and `fixtures/charts/bob.json` contain complete synthetic mapped charts. Supply the missing timezone through the existing override parameters.

Example:

```sh
curl -sS 'http://127.0.0.1:8000/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=UTC&b_tz=UTC' > reader_response.json
```

Fixture behavior does not establish live current-row readiness or production Reader success.


````

## RL-009

Operation: REPLACE
Original heading path:

# **6\. Reader v1 local workflow** > ## **6.3 Reader JSON from CLI**

Location: original lines 342–347; original character span [18561, 18914).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **6.3 Reader JSON from CLI**

For local QA, the most reliable way to emit Reader JSON without HTTP fixture path concerns is hdctl showcompat \--dump-reader:

mkdir \-p audit/tmp/pf29 LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \> audit/tmp/pf29/compat.json


````

New text:

````text
## **6.3 Reader JSON from CLI**

Use the complete mapped `pair.json` prepared in §7.3. `--dump-reader` writes Reader v1 only; it is not a Reader v2 selector. Ordinary stdout contains the separate full internal/admin compat result.

Example:

```sh
mkdir -p audit/tmp/pf29
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json > audit/tmp/pf29/compat.json
```

## **6.4 Production Reader v1 and v2 usage [Implemented]**

Use `POST /api/reader?v=1` for the unchanged numeric-free harmony projection, or `POST /api/reader?v=2` for the full ordered ten-category bands-only projection. Both use the same read-only current-row input path. Select exactly one version value; a missing, repeated, malformed or unsupported value refuses. Unprefixed `POST /reader` remains a 405 stub; it is not the production route.

Use exactly `a_id` and `b_id` with canonical lowercase hyphenated UUIDs. Inline charts, Gates and viewer preferences do not belong in this request. The IDs must resolve to existing complete mapped current rows in the chosen authorized database; these example UUIDs do not create rows.

Example after those prerequisites are independently established:

```sh
curl -sS -X POST 'http://127.0.0.1:8000/api/reader?v=2' -H 'Content-Type: application/json; charset=utf-8' --data-binary '{"a_id":"11111111-1111-4111-8111-111111111111","b_id":"22222222-2222-4222-8222-222222222222"}' > reader_v2_response.json
```

An eligible v1 result contains one harmony band. An eligible v2 result contains all ten bands in the governed order; an ineligible valid self-pair has an empty categories array. Missing or invalid Gate data refuses rather than becoming successful ineligibility. Both public projections are numeric-free and omit scores, Gates, prompts and narrative keys. Consult PF05-Canon-HDE-CLI-API-Vendor-Ref and PF10-HDE-Build-Notes for versioned request, success/error and transport contracts, and PF12-Canon-HDE-Schemas-and-Artifacts for governed schema ownership. Production POST is non-conditional and has no ETag; the dev GET behavior in §6.1 is separate.

The corrected v1 error schema admits the existing four-key emitted envelope; it did not change response bytes or add a retry field. Historical in-process and loopback proofs do not establish deployed-service or live DB Reader v1/v2 success. That success remains environment-blocked in the supplied change record.


````

## RL-010

Operation: REPLACE
Original heading path:

# **7\. Compat workflows** > ## **7.1 Magic-10 category IDs**

Location: original lines 350–377; original character span [18942, 20057).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **7.1 Magic-10 category IDs**

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
     
10. Balance

**Current scoring limitation \[Currentgap\]:** The implemented compat scorer derives each category score from a SHA-256 hash of the normalized pair key and category, then applies viewer-weight adjustment. The HDAPI v2 adapter checks `gates` only as a list of strings; it does not enforce canonical integers `1..64`, uniqueness, or a nonempty complete Gate field. Current CLI and HTTP compat paths reduce the pair to identifiers before scoring, so the scorer receives no validated Gate set or Gate-derived Magic10 signals. A separate transitional Reader computation derives only a `harmony` band from Type/Strategy features.

Until the authorized Gate- and Channel-state-based Magic10 v1 mechanic is shipped and verified, treat these current scores and bands as placeholder or transitional development behavior rather than that mechanic.


````

New text:

````text
## **7.1 Magic-10 category IDs**

Use the governed category order:

1. harmony
2. heat
3. communication
4. alignment
5. comfort
6. consistency
7. expansion
8. creativity
9. drive
10. balance

The supported compat path validates complete mapped chart inputs and Gates, then evaluates eligible pairs through the pure Gate-based core using the immutable admitted mechanics bundle. It no longer computes the intrinsic categories from a hash of person identifiers or a Type/Strategy-only harmony substitute. Viewer preferences do not rescore the intrinsic result.

An eligible internal/admin result exposes the complete signals and category scores/bands; the public Reader projects bands only. A valid self-pair follows the separate ineligible path. Missing or malformed chart/Gate data is a refusal, not an ineligible success. PF01-Canon-HDE-Math-Spec owns the mechanics, identities, eligibility and category semantics; PF12-Canon-HDE-Schemas-and-Artifacts owns the result and configuration schemas. PF29 supplies no formula or alternate calculator.


````

## RL-011

Operation: REPLACE
Original heading path:

# **7\. Compat workflows** > ## **7.2 Local HTTP compat \[Implemented\] \[Dev or QA only\]**

Location: original lines 378–411; original character span [20057, 22449).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **7.2 Local HTTP compat \[Implemented\] \[Dev or QA only\]**

Route:

POST /api/compat/v1

Supported method posture:

* POST performs the dev/internal compatibility evaluation.  
    
* GET is a probe only. It does not compute compatibility, accepts no request body, and returns the fixed canonical body `{"schema":"v1","ok":true}`. A GET body receives `ERR_COMPAT_INVALID_JSON`.  
    
* In non-production posture, HEAD returns 405 with an empty body and `Allow: POST, OPTIONS`; OPTIONS returns 204 with an empty body and the same Allow value.  
    
* The route and its descendants return 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.

Example request file:

cat \> compat\_request.json \<\<'EOF'  
{"a":{"person\_uid":"qa-left"},"b":{"person\_uid":"qa-right"},"viewer\_prefs":{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}  
EOF

Example local command:

curl \-sS \-X POST [http://127.0.0.1:8000/api/compat/v1](http://127.0.0.1:8000/api/compat/v1) \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

Production boundary:

POST /api/compat/v1 is not production-public in the current repository. It returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values. Production compat computation, when needed, must be treated as internal/server-side or CLI/operator workflow, not a public HTTP claim.

**Current repository discrepancy \[Current gap\]:** `adapter/http_reader.py` treats a missing APP\_ENV as dev at the Reader guard. This does not weaken the explicit APP\_ENV=dev requirement above; it records checked-in behavior only and does not prove runtime exposure.

**Additional current repository discrepancy \[Current gap\]:** `POST /reader` is not supported by the mounted Reader v1 route; current code returns HTTP 405 with `method_not_allowed`. The mounted public computation derives only the `harmony` band from Type/Strategy features, while the checked-in Reader schema enumerates different category IDs. The schema and transitional runtime output therefore do not describe one settled full Magic10 contract.


````

New text:

````text
## **7.2 Local HTTP compat \[Implemented\] \[Dev or QA only\]**

Route:

POST /api/compat/v1

Supported method posture:

* POST performs the dev/internal compatibility evaluation.  
    
* GET is a probe only. It does not compute compatibility, accepts no request body, and returns the fixed canonical body `{"schema":"v1","ok":true}`. A GET body receives `ERR_COMPAT_INVALID_JSON`.  
    
* In non-production posture, HEAD returns 405 with an empty body and `Allow: POST, OPTIONS`; OPTIONS returns 204 with an empty body and the same Allow value.  
    
* The route and its descendants return 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.

Inline `a` and `b` must be complete mapped charts. Alternatively, use the supported stored-identity input family with both `a_id` and `b_id` and available current rows; do not mix the families. Identifier-only `a`/`b` objects and birth-tuple-only inline charts do not demonstrate successful Gate-based compat.

Example using the actual synthetic fixture charts:

```sh
python - <<'PY'
import json
from pathlib import Path
request = {"a": json.loads(Path("fixtures/charts/alice.json").read_text()), "b": json.loads(Path("fixtures/charts/bob.json").read_text())}
Path("compat_request.json").write_text(json.dumps(request, sort_keys=True, separators=(",", ":")) + "\n")
PY
curl -sS -X POST http://127.0.0.1:8000/api/compat/v1 -H 'Content-Type: application/json; charset=utf-8' --data-binary @compat_request.json > http_compat_response.json
```

The successful response is the internal/admin compat result, not Reader bytes. This route remains blocked in production as stated above. Reader v1/v2 production usage is §6.4; the old production prefix and Reader success/error-schema gaps are resolved in the selected change record, without making this compat route production-public.


````

## RL-012

Operation: REPLACE
Original heading path:

# **7\. Compat workflows** > ## **7.3 CLI compat from payload files \[Implemented\]**

Location: original lines 412–436; original character span [22449, 23426).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **7.3 CLI compat from payload files \[Implemented\]**

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


````

New text:

````text
## **7.3 CLI compat from payload files \[Implemented\]**

File and stdin modes use complete mapped charts locally, with no DB or vendor acquisition. A person label and birth tuple alone are not a complete mapped input.

Example: create `pair.json` from the existing synthetic fixture charts, preserving their Gate and identity fields:

```sh
python - <<'PY'
import json
from pathlib import Path
pair = {"left": json.loads(Path("fixtures/charts/alice.json").read_text()), "right": json.loads(Path("fixtures/charts/bob.json").read_text())}
Path("pair.json").write_text(json.dumps(pair, sort_keys=True, separators=(",", ":")) + "\n")
PY
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json > compat.json
```

Source-tree fallback and other supported file/stdin forms:

```sh
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python scripts/hdctl.py showcompat --pair-file pair.json > compat.json
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json > compat.json
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat < pair.json > compat.json
```

For an eligible pair, stdout is the complete LF-terminated canonical internal/admin compat result, with no `a`/`b`/viewer-preference wrapper. Success requires complete release admission (§7.6). The recipe is a fixture workflow, not proof of DB readiness, vendor capability or deployed Reader success.


````

## RL-013

Operation: REPLACE
Original heading path:

# **7\. Compat workflows** > ## **7.4 Optional viewer preferences file \[Implemented\]**

Location: original lines 437–450; original character span [23426, 24019).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **7.4 Optional viewer preferences file \[Implemented\]**

Create viewer\_prefs.json:

cat \> viewer\_prefs.json \<\<'EOF'  
{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}  
EOF

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--viewer-prefs-file viewer\_prefs.json \> compat.json

If \--viewer-prefs-file is omitted, the current CLI defaults top\_category to heat and all ten category weights to 50\.


````

New text:

````text
## **7.4 Optional viewer preferences file \[Implemented\]**

Create viewer\_prefs.json:

cat \> viewer\_prefs.json \<\<'EOF'  
{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}  
EOF

Run:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--viewer-prefs-file viewer\_prefs.json \> compat.json

The CLI still accepts and validates this compatibility input, and its defaults are top\_category heat and ten weights of 50. Neither supplied nor default preferences enter intrinsic scoring or Reader category projection, and the complete compat result does not carry a viewer\_prefs wrapper. Do not use this flag to tune the admitted mechanics or select a Reader v2 category.


````

## RL-014

Operation: REPLACE
Original heading path:

# **7\. Compat workflows** > ## **7.5 CLI compat from DB, vendor, or auto source \[Implemented\]**

Location: original lines 451–466; original character span [24019, 25593).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **7.5 CLI compat from DB, vendor, or auto source \[Implemented\]**

DB mode requires available database access and resolvable BodyGraph rows for both user IDs. It performs reads for the selected rows and does not invoke vendor I/O:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--source db \--user-a \<user\_a\> \--user-b \<user\_b\> \> compat\_db.json

Vendor mode is an operator-authorized open-rails workflow and requires complete birth tuples for both people:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl showcompat \--source vendor \--birthdate-a YYYY-MM-DD \--birthtime-a HH:MM \--location-a "Place" \--birthdate-b YYYY-MM-DD \--birthtime-b HH:MM \--location-b "Place" \> compat\_vendor.json

The current vendor path requests dry-run acquisition and does not perform mapped-cache database persistence. It does attempt to append a success record under `artifacts/ingest/ingest_success.log`; treat that file as generated output and do not promote it into governed evidence without the owning evidence process.

With \--source auto, a complete \--user-a/--user-b pair takes DB precedence. Otherwise, the presence of birthdate input selects vendor mode, which then requires both complete birth tuples. If neither source input family resolves, expect AUTO\_SOURCE\_UNRESOLVED.

Relevant typed failures include MISSING\_DB\_USER, BODYGRAPH\_NOT\_FOUND, DB\_QUERY\_FAILED, MISSING\_VENDOR\_INPUT, and the provider refusal, network, or configuration errors listed in §17. Failure output is not a successful compatibility result.


````

New text:

````text
## **7.5 CLI compat from DB, vendor, or auto source \[Implemented\]**

DB mode requires available database access and resolvable BodyGraph rows for both user IDs. It performs reads for the selected rows and does not invoke vendor I/O:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--source db \--user-a \<user\_a\> \--user-b \<user\_b\> \> compat\_db.json

Vendor mode is an operator-authorized open-rails workflow and requires complete birth tuples for both people:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl showcompat \--source vendor \--birthdate-a YYYY-MM-DD \--birthtime-a HH:MM \--location-a "Place" \--birthdate-b YYYY-MM-DD \--birthtime-b HH:MM \--location-b "Place" \> compat\_vendor.json

The current resolved-compat vendor path uses read-only dry-run acquisition: no mapped-cache database persistence, and success/retry logging is disabled at that acquisition boundary. Do not confuse it with the separately authorized persistence recipe in §12.

With \--source auto, both user IDs are required and resolution is DB-only. Birth-based vendor fallback is prohibited; use explicit \--source vendor for the two complete synthetic birth tuples. Without both IDs, auto refuses AUTO\_SOURCE\_UNRESOLVED. No database or vendor success is implied by the command declaration.

Relevant typed failures include MISSING\_DB\_USER, BODYGRAPH\_NOT\_FOUND, DB\_QUERY\_FAILED, MISSING\_VENDOR\_INPUT, and the provider refusal, network, or configuration errors listed in §17. Failure output is not a successful compatibility result.

## **7.6 Complete release admission and read-only golden comparison [Implemented]**

Eligible Gate computation consumes the complete pinned release through the admission owner; a partial roster, missing member, incoherent hash or executing-source mismatch refuses. The inspected source tree declares release version `1.3.0` and a 45-member roster. The earlier incomplete-release refusal interval ended with complete admission; it is not the current success predicate. File presence and a manifest version do not by themselves establish admission in an installation.

Example read-only comparison against the repository root:

```sh
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/config/generate_config_artifacts.py --compare-goldens .
```

The comparator uses all eight governed goldens and canonical application entrypoints. Exit 0 denotes a completed match, exit 1 a completed mismatch, and exit 5 a refusal; inspect the actual report or stderr. Use `--compare-goldens` explicitly: the generator's ordinary mode writes artifacts. Optional `--goldens PATH` chooses the expected collection; optional `--report PATH` writes its report only outside both candidate and repository roots and never over the goldens file. Do not turn comparison into activation, configuration selection, repair or evidence generation. An arbitrary candidate root is not proof that its application modules were executed: the comparator uses the executing installation's canonical application modules. The supplied proof compared the actual repository candidate; it provides no broader candidate-root runtime guarantee.

Consult PF12-Canon-HDE-Schemas-and-Artifacts for release/configuration/golden ownership and PF14-Canon-HDE-Mechanics-Guide for admission and tool responsibilities. Source-tree or editable availability does not resolve the recorded non-editable wheel gap.

## **7.7 Read-only current-row Gate readiness [Implemented]**

Use an explicit selection of canonical UUIDs and authorized read access to existing current rows. Example with IDs already established for that dataset:

```sh
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python tools/bodygraph/check_magic10_gate_readiness.py --user-id 11111111-1111-4111-8111-111111111111 --user-id 22222222-2222-4222-8222-222222222222
```

Alternatively, `--selection-file PATH` reads one canonical UUID per line; blank lines and `#` comments are ignored. Empty, duplicate, malformed or unavailable selections refuse. Exit 0 means a report was emitted; read its `readiness` value, which can be `READY` or `NOT_READY`. Exit 5 means refusal with a value-free stderr token and no readiness report. An unavailable database is never a ready dataset.

The command reads selected rows only. It performs no vendor acquisition, SQL write, backfill or automatic Gate repair. Offline/fake-DB proof establishes the tool's behavior, not current production row readiness. The selected change record leaves the live observation environment-blocked and requiring separate future ownership; exceptional closure did not perform it. Route input and report contracts to PF05-Canon-HDE-CLI-API-Vendor-Ref and PF12-Canon-HDE-Schemas-and-Artifacts, and proof classification to PF19-Canon-Glow-QA-Guide.


````

## RL-022

Operation: REPLACE
Original heading path:

# **9\. Conjunction workflows** > ## **9.1 CLI conjunction from payload \[Implemented\]**

Location: original lines 516–542; original character span [27903, 29538).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **9.1 CLI conjunction from payload \[Implemented\]**

Create conjunction\_pair.json:

cat \> conjunction\_pair.json \<\<'EOF'  
{"left":{"person\_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person\_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}  
EOF

Run closed rails:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file conjunction\_pair.json \> conjunction.json

Other supported forms:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--a-file left.json \--b-file right.json \> conjunction.json  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \< conjunction\_pair.json \> conjunction.json

## **9.2 CLI conjunction from DB source \[Implemented\]; vendor source \[Current gap\]**

DB mode requires available database access and resolvable rows for both user IDs:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--user-a \<user\_a\> \--user-b \<user\_b\> \--source db \> conjunction\_db.json

Vendor-source conjunction is not a safe compute-only operator workflow in the current repository. The implemented CLI exposes no \--upsert flag for showcompat, but an unresolved vendor-source conjunction calls BodyGraph resolution with non-dry-run persistence enabled. Do not run this mode until implementation requires explicit write intent and its database and authorization preconditions are documented.

A vendor-source refusal is not a successful acquisition or computation.


````

New text:

````text
## **9.1 CLI conjunction from payload \[Implemented\]**

Prepare the two complete mapped charts in `pair.json` using §7.3, then run closed rails:

```sh
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction --pair-file pair.json > conjunction.json
```

Other supported forms use the same complete mapped charts:

```sh
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json > conjunction.json
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction < pair.json > conjunction.json
```

A birth tuple alone is not a complete Gate input. The conjunction wrapper carries normalized identities and the same complete intrinsic compat result; it does not introduce viewer-weighted scoring.

## **9.2 CLI conjunction from DB source \[Implemented\]; vendor source \[Operator-authorized only\]**

DB mode requires available database access and resolvable rows for both canonical user IDs:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--user-a \<user\_a\> \--user-b \<user\_b\> \--source db \> conjunction\_db.json

The current conjunction resolver tries local rows first. After a local miss, explicit vendor source requires both user-ID arguments and may acquire read-only complete charts only with authorized open rails and the required complete birth inputs; closed rails refuse that acquisition. This resolver uses dry-run acquisition and does not perform mapped-cache database persistence. The CLI exposes no \--upsert option for showcompat; explicit persistence belongs to the separate BodyGraph workflow in §12.

No live DB or vendor success is established by this static availability check. A vendor-source refusal is not a successful acquisition or computation.


````

## RL-015

Operation: REPLACE
Original heading path:

# **10\. Aux narrative preview workflow** > ## **10.1 CLI Aux preview from compat output \[Implemented\]**

Location: original lines 583–604; original character span [31238, 32296).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **10.1 CLI Aux preview from compat output \[Implemented\]**

Use one of two input modes.

Pair-file mode derives category from viewer\_prefs.top\_category and band from the matching category in the compat JSON. In this mode, \--category and \--band do not override the pair file.

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file audit/tmp/pf29/compat.json \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

Explicit-tuple mode omits \--pair-file and supplies \--category and \--band:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--category harmony \--band Cool \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

Common options:

* \--perspective \<personal|shared\>  
    
* \--show-narrative  
    
* \--admin-out \<ids.json\>

The admin sidecar is IDs-only. It is not raw payload capture. When \--admin-out is supplied, the helper also writes a sibling .sha256 sidecar and sets local file mode 0600 on both files.


````

New text:

````text
## **10.1 CLI Aux preview from compat output \[Implemented\]**

Use one of two input modes.

Pair-file mode reads the complete compat result's categories, or conjunction.compat for a conjunction result. Optional \--category selects an existing category; without it, the first category row is used, which is harmony in the governed result order. The band comes from that row; \--band does not override it. viewer\_prefs does not select the category. This preview does not rescore the intrinsic result.

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file audit/tmp/pf29/compat.json \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

Explicit-tuple mode omits \--pair-file and supplies \--category and \--band:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--category harmony \--band Cool \--perspective shared \--show-narrative \--admin-out audit/tmp/pf29/aux\_sidecar.json

Common options:

* \--perspective \<personal|shared\>  
    
* \--show-narrative  
    
* \--admin-out \<ids.json\>

The admin sidecar is IDs-only. It is not raw payload capture. When \--admin-out is supplied, the helper also writes a sibling .sha256 sidecar and sets local file mode 0600 on both files.


````

## RL-016

Operation: REPLACE
Original heading path:

# **13\. Production posture** > ## **13.2 Production compat posture \[Current gap\]**

Location: original lines 768–781; original character span [40366, 40908).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **13.2 Production compat posture \[Current gap\]**

Do not document POST /api/compat/v1 as production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.

Production compat computation, if needed, must be handled as one of:

* internal/server-side workflow;  
    
* CLI/operator workflow;  
    
* future explicit production contract after canon and implementation change.

PF29 does not create that production public endpoint.


````

New text:

````text
## **13.2 Production compat posture \[Current gap\]**

Do not document POST /api/compat/v1 as production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.

Production compat computation, if needed, must be handled as one of:

* internal/server-side workflow;  
    
* CLI/operator workflow;  
    
* future explicit production contract after canon and implementation change.

PF29 does not create that production public endpoint.

The production-contract Reader route is `POST /api/reader?v=1` or `?v=2`, with usage and current-row prerequisites in §6.4. It is distinct from the blocked compat route. Checked-in routing does not establish reachability at a deployed base URL, live DB success, activation or deployment.


````

## RL-017

Operation: REPLACE
Original heading path:

# **15\. Minimum runnable recipes** > ## **Recipe B — local CLI compat plus BodyGraph/admin JSON payloads**

Location: original lines 844–864; original character span [46168, 47349).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **Recipe B — local CLI compat plus BodyGraph/admin JSON payloads**

cat \> pair.json \<\<'EOF'  
{"left":{"person\_uid":"qa-left","birthdate":"1990-01-01","birthtime":"12:00","location":"Paris, FR"},"right":{"person\_uid":"qa-right","birthdate":"1991-02-03","birthtime":"08:30","location":"Lisbon, PT"}}  
EOF  
mkdir \-p audit/tmp/pf29/compat\_admin  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Fallback:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Expected JSON files; the required admin-dump .sha256 sidecars are listed in §8.1:

audit/tmp/pf29/compat.json  
audit/tmp/pf29/reader.json  
audit/tmp/pf29/compat\_admin/pair.left.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.right.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.composite.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.compat.proof.json


````

New text:

````text
## **Recipe B — local CLI compat plus BodyGraph/admin JSON payloads**

Prepare the complete mapped synthetic `pair.json` using §7.3. Do not substitute the former birth-tuple-only example.

```sh
mkdir -p audit/tmp/pf29/compat_admin
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --pair-file pair.json --dump-reader audit/tmp/pf29/reader.json --dump-admin-dir audit/tmp/pf29/compat_admin > audit/tmp/pf29/compat.json
```

The Reader dump is v1; stdout is the complete internal/admin compat result. Fallback:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python scripts/hdctl.py showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Expected JSON files; the required admin-dump .sha256 sidecars are listed in §8.1:

audit/tmp/pf29/compat.json  
audit/tmp/pf29/reader.json  
audit/tmp/pf29/compat\_admin/pair.left.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.right.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.composite.bodygraph.json  
audit/tmp/pf29/compat\_admin/pair.compat.proof.json


````

## RL-018

Operation: REPLACE
Original heading path:

# **15\. Minimum runnable recipes** > ## **Recipe C — local HTTP compat**

Location: original lines 865–873; original character span [47349, 47957).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **Recipe C — local HTTP compat**

Start the persistent Reader mode in Recipe A.

cat \> compat\_request.json \<\<'EOF'  
{"a":{"person\_uid":"qa-left"},"b":{"person\_uid":"qa-right"},"viewer\_prefs":{"top\_category":"harmony","weights":{"heat":50,"harmony":50,"communication":50,"alignment":50,"comfort":50,"consistency":50,"expansion":50,"creativity":50,"drive":50,"balance":50}}}  
EOF  
curl \-sS \-X POST [http://127.0.0.1:8000/api/compat/v1](http://127.0.0.1:8000/api/compat/v1) \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json


````

New text:

````text
## **Recipe C — local HTTP compat**

Start the persistent Reader mode in Recipe A. Generate `compat_request.json` from the complete synthetic fixture charts and run the POST command in §7.2. The old identifier-only inline payload is insufficient for Gate-based computation. This is dev/QA compat output, not production-public Reader output. For the versioned Reader, use §6.4 with established current-row inputs.


````

## RL-023

Operation: REPLACE
Original heading path:

# **15\. Minimum runnable recipes** > ## **Recipe E — local conjunction compat from payload**

Location: original lines 878–881; original character span [48203, 48430).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
## **Recipe E — local conjunction compat from payload**

mkdir \-p audit/tmp/pf29 LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file pair.json \> audit/tmp/pf29/conjunction.json


````

New text:

````text
## **Recipe E — local conjunction compat from payload**

Prepare the complete mapped `pair.json` in §7.3 first.

```sh
mkdir -p audit/tmp/pf29
LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --conjunction --pair-file pair.json > audit/tmp/pf29/conjunction.json
```


````

## RL-019

Operation: REPLACE
Original heading path:

# **16\. Known limitations and nonclaims**

Location: original lines 900–919; original character span [50176, 52278).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
# **16\. Known limitations and nonclaims**

PF29 must preserve these nonclaims:

* POST /api/compat/v1 is not production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.  
    
* /internal/dev/sampler and /dev/\*/conjunction are dev/test/local-only.  
    
* GET /reader is a dev/local Reader v1 harness route and requires safe fixture chart paths.  
    
* Current configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter. For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved.  
    
* Current configured-v2 repository surfaces support scoped dry-run mapping, mapped v2 output feeding compatibility computation, and bounded mapped-cache persistence of adapter-mapped HDE data. This guide does not establish execution or acceptance of any separate OPS smoke. These surfaces do not authorize production upsert, public Reader changes, new public routes, app-side vendor ownership, or broad HumanDesignAPI v2 platform conformance.  
    
* Configured-v2 non-dry-run persistence requires explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target. Missing intent or direct access and every production-like attempt fail closed; runtime selection does not fall back to a bridge or alternate database transport.  
    
* No workflow may record raw vendor payload bodies, raw vendor request or response bodies, bearer token values, API key values, geocode key values, or any body containing secrets or production user PII in governed evidence. Synthetic local dev/QA request and response files used by this guide's bounded recipes are scratch operator inputs and outputs, not governed evidence.  
    
* Evidence-generation workflows are not user-facing runtime workflows. Evidence outputs under audit/\*\* and artifacts/\*\* require Human Evidence Index, Machine Mirror, and path-proof discipline when promoted.


````

New text:

````text
# **16\. Known limitations and nonclaims**

PF29 must preserve these nonclaims:

* POST /api/compat/v1 is not production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.  
    
* /internal/dev/sampler and /dev/\*/conjunction are dev/test/local-only.  
    
* GET /reader is a dev/local Reader v1 harness route and requires safe fixture chart paths.  
    
* Current configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter. For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved.  
    
* Current configured-v2 repository surfaces support scoped dry-run mapping, mapped v2 output feeding compatibility computation, and bounded mapped-cache persistence of adapter-mapped HDE data. This guide does not establish execution or acceptance of any separate OPS smoke. These surfaces do not authorize production upsert, public Reader changes, new public routes, app-side vendor ownership, or broad HumanDesignAPI v2 platform conformance.  
    
* Configured-v2 non-dry-run persistence requires explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target. Missing intent or direct access and every production-like attempt fail closed; runtime selection does not fall back to a bridge or alternate database transport.  
    
* No workflow may record raw vendor payload bodies, raw vendor request or response bodies, bearer token values, API key values, geocode key values, or any body containing secrets or production user PII in governed evidence. Synthetic local dev/QA request and response files used by this guide's bounded recipes are scratch operator inputs and outputs, not governed evidence.  
    
* Evidence-generation workflows are not user-facing runtime workflows. Evidence outputs under audit/\*\* and artifacts/\*\* require Human Evidence Index, Machine Mirror, and path-proof discipline when promoted.

Additional Gate/Reader limits:

* Missing or invalid Gates, incomplete charts and incoherent releases refuse. A valid ineligible self-pair is a separate outcome.
* The current admitted release declaration is 1.3.0 with 45 members. Source-tree inspection is not an admission run; packaged wheel admission remains a recorded gap with the packaging owner and Product Owner.
* Unknown non-compat paths may still return Flask HTML 404 responses in the affected factories. Do not claim that every unknown path has the Reader JSON error envelope; the HTTP transport owner retains this limitation.
* `--dump-reader` remains v1-only. The CLI help still describes ordinary `showcompat` stdout as Reader v1 although its actual handler emits the full internal/admin compat result. `scripts/hd_cli.py` is a separate legacy stub that emits `open_leader`; do not use it as proof of the supported Reader contract. The historical `test_cli_proof.py` failure and the recorded unselected test baseline remain out-of-lane, not fresh results of this revision.
* `--allow-prod-vendor` is absent from the inspected active CLI parser. Do not prescribe it as a runnable flag or infer production override support. Its requirement remains with the CLI and PF05 owners through change control.
* Dev GET `/reader` still defaults a missing APP_ENV to dev; conjunction dev routes require explicit dev/test/local values. The discrepancy does not waive the explicit environment requirement in this guide.
* The supplied QA record proves bounded offline/in-process Reader v1/v2 behavior and a synthetic live vendor-backed CLI AB/BA run with Reader v1 dumps. It does not prove exact vendor resource/auth family, mapped-cache persistence, rate-limit/error handling, Reader v2 live HTTP success or deployment. The live current-row readiness and live DB Reader v1/v2 success observations remain environment-blocked.
* HDE-EPIC040 was exceptionally closed by its recorded owner. That decision resolved the historical evidence landing/indexing gap; it did not establish an ordinary close pack, PF09 movement, canon publication, activation, deployment or the deferred live facts.


````

## RL-020

Operation: REPLACE
Original heading path:

# **17\. Troubleshooting**

Location: original lines 920–943; original character span [52278, 56223).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
# **17\. Troubleshooting**

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
| PROVIDER\_CONFIG\_MISSING | Required vendor config is absent or the configured base is not HTTPS. | Confirm HD\_API\_BASE\_URL, HD\_API\_KEY, and when needed GEO\_API\_KEY, without printing values, and confirm the configured base uses HTTPS. |
| PROVIDER\_CONFIG\_INVALID | Vendor configuration is ambiguous or violates contract. | Check for conflicting HD\_API\_BASE\_URL and HDAPI\_BASE\_URL or unpinned vendor policy. |
| PROVIDER\_ROUTE\_REQUIRES\_ADAPTER | Generic BodyGraph ingest attempted to build a configured-v2 chart request outside the resolver adapter path. | Use bg:resolve \--source vendor through the configured-v2 resolver path. Add \--dry-run for mapping-only use; add \--upsert only for the authorized bounded persistence workflow in §11.4. Do not treat generic BodyGraph ingest as adapter-backed v2 resolution. |
| PROVIDER\_WRITE\_UNSUPPORTED | Explicit upsert intent is missing, the environment is production-like, or the mapped-cache input or projection violates the supported contract. | Use \--dry-run for mapping-only work. Use \--upsert only within the authorized non-production workflow in §11.4. Never bypass a production-like refusal. |
| DB\_WRITER\_UNAVAILABLE | DATABASE\_URL is absent or unavailable, a retired bridge key is present, or the sanctioned direct provider or write transaction could not be used. | Confirm authorization and names-only DATABASE\_URL presence, remove retired bridge keys from the execution environment, and retry only within the authorized workflow. Do not print values or fall back to another transport. |
| DB\_QUERY\_FAILED | A DB query, identity-cardinality check, mapped-cache read-back, or canonical-parity check failed. | Inspect the emitted typed error and direct database posture. Do not claim persistence or read-back success. |
| DB\_PAYLOAD\_MISSING | Canonical mapped-cache read-back did not return exactly one row. | Inspect the emitted typed error and direct database posture. Do not claim persistence, read-back, or idempotence success. |
| BODYGRAPH\_NOT\_FOUND | No BodyGraph row was found for the requested user. | Confirm the user ID and whether ingest/persistence has actually completed. |
| Evidence mirror or hash check fails | Generated evidence changed without refresh, or path-proof/index/mirror drift exists. | Run the write/update sequence, then the check sequence in §14. |


````

New text:

````text
# **17\. Troubleshooting**

| Symptom | Likely cause | Operator action |
| :---- | :---- | :---- |
| hdctl: command not found | Console entrypoint is not installed in the current environment. | Run python \-m pip install \-e . \--no-deps \--no-build-isolation, or use python scripts/hdctl.py. |
| VERSION\_FLAG\_WITH\_COMMAND | \--version was passed with another command. | Run hdctl \--version by itself. |
| DEV\_ADMIN\_ONLY | A dev/admin CLI command was run without APP\_ENV=dev, test, or local. | Add APP\_ENV=dev for local QA. |
| HTTP 403 from /internal/dev/sampler | APP\_ENV is not dev, test, or local. | Restart the harness with APP\_ENV=dev. |
| HTTP 404 from POST /api/compat/v1 in prod | Expected current production block. | Use dev/QA HTTP compat locally or an internal CLI/server-side production workflow. |
| ERR\_READER\_FORBIDDEN | Reader v1 route was called outside APP\_ENV=dev. | Use the local dev harness for GET /reader, or the production POST /api/reader versioned route with existing current-row IDs (§6.4). |
| ERR\_READER\_MISSING\_TZ\_A or ERR\_READER\_MISSING\_TZ\_B | Fixture chart lacks timezone and no override was supplied. | Add a\_tz or b\_tz, or use fixture files that include timezone. |
| MISSING\_VENDOR\_INPUT | Vendor source was requested without full birth tuple. | Supply birthdate, birthtime, and location. |
| PROVIDER\_REFUSED | Vendor source was attempted under closed rails. | Confirm authorization, then run with SAFE\_MODE=0 ALLOW\_NETWORK=1. |
| PROVIDER\_NETWORK\_BLOCKED | Network access is disabled. | Confirm authorization and set ALLOW\_NETWORK=1 only for bounded open-rails runs. |
| PROVIDER\_CONFIG\_MISSING | Required vendor config is absent or the configured base is not HTTPS. | Confirm HD\_API\_BASE\_URL, HD\_API\_KEY, and when needed GEO\_API\_KEY, without printing values, and confirm the configured base uses HTTPS. |
| PROVIDER\_CONFIG\_INVALID | Vendor configuration is ambiguous or violates contract. | Check for conflicting HD\_API\_BASE\_URL and HDAPI\_BASE\_URL or unpinned vendor policy. |
| PROVIDER\_ROUTE\_REQUIRES\_ADAPTER | Generic BodyGraph ingest attempted to build a configured-v2 chart request outside the resolver adapter path. | Use bg:resolve \--source vendor through the configured-v2 resolver path. Add \--dry-run for mapping-only use; add \--upsert only for the authorized bounded persistence workflow in §11.4. Do not treat generic BodyGraph ingest as adapter-backed v2 resolution. |
| PROVIDER\_WRITE\_UNSUPPORTED | Explicit upsert intent is missing, the environment is production-like, or the mapped-cache input or projection violates the supported contract. | Use \--dry-run for mapping-only work. Use \--upsert only within the authorized non-production workflow in §11.4. Never bypass a production-like refusal. |
| DB\_WRITER\_UNAVAILABLE | DATABASE\_URL is absent or unavailable, a retired bridge key is present, or the sanctioned direct provider or write transaction could not be used. | Confirm authorization and names-only DATABASE\_URL presence, remove retired bridge keys from the execution environment, and retry only within the authorized workflow. Do not print values or fall back to another transport. |
| DB\_QUERY\_FAILED | A DB query, identity-cardinality check, mapped-cache read-back, or canonical-parity check failed. | Inspect the emitted typed error and direct database posture. Do not claim persistence or read-back success. |
| DB\_PAYLOAD\_MISSING | Canonical mapped-cache read-back did not return exactly one row. | Inspect the emitted typed error and direct database posture. Do not claim persistence, read-back, or idempotence success. |
| BODYGRAPH\_NOT\_FOUND | No BodyGraph row was found for the requested user. | Confirm the user ID and whether ingest/persistence has actually completed. |
| Evidence mirror or hash check fails | Generated evidence changed without refresh, or path-proof/index/mirror drift exists. | Run the write/update sequence, then the check sequence in §14. |

For Gate-based usage, a refused chart or release is not a successful ineligible response. Use the owning PF05 error contract to interpret the actual stderr or HTTP result; do not fabricate or repair Gates to force success. For the comparator, exit 1 is mismatch and exit 5 is refusal. For readiness, exit 0 can still report NOT_READY; exit 5 supplies no report. These observations do not authorize data correction, vendor acquisition or evidence regeneration.


````

## RL-021

Operation: REPLACE
Original heading path:

# **18\. Quick command reference**

Location: original lines 944–1003; original character span [56223, 60081).
Expected old-block occurrence: 1 within this heading-path location and the complete original; observed: 1.

Old text:

````text
# **18\. Quick command reference**

Install and verify:

python \-m pip install \-e . \--no-deps \--no-build-isolation  
hdctl \--help  
hdctl \--version

Start a persistent local Reader harness for subsequent HTTP recipes:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev PORT=8000 scripts/dev\_start\_reader.sh

Alternatively, run the self-contained dev sampler healthcheck only when no Reader is already bound to DEV\_SAMPLER\_URL:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev DEV\_SAMPLER\_URL=[http://127.0.0.1:8000/internal/dev/sampler](http://127.0.0.1:8000/internal/dev/sampler) scripts/qa/dev\_sampler\_healthcheck.py

Run CLI compat:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \> compat.json

Run CLI compat with Reader and admin dumps:

mkdir \-p audit/tmp/pf29/compat\_admin LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Run local HTTP compat:

curl \-sS \-X POST [http://127.0.0.1:8000/api/compat/v1](http://127.0.0.1:8000/api/compat/v1) \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

Run local conjunction:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file pair.json \> conjunction.json

Run Aux preview:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file compat.json \--perspective shared \--show-narrative \--admin-out aux\_sidecar.json

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
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 bash ci/checks/check\_evidence\_index\_hash.sh LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/orientation\_demo.py \--check


````

New text:

````text
# **18\. Quick command reference**

Install and verify:

python \-m pip install \-e . \--no-deps \--no-build-isolation  
hdctl \--help  
hdctl \--version

Start a persistent local Reader harness for subsequent HTTP recipes:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev PORT=8000 scripts/dev\_start\_reader.sh

Alternatively, run the self-contained dev sampler healthcheck only when no Reader is already bound to DEV\_SAMPLER\_URL:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev DEV\_SAMPLER\_URL=[http://127.0.0.1:8000/internal/dev/sampler](http://127.0.0.1:8000/internal/dev/sampler) scripts/qa/dev\_sampler\_healthcheck.py

Prepare the complete mapped `pair.json` in §7.3 before running CLI compat:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \> compat.json

Run CLI compat with Reader and admin dumps:

mkdir \-p audit/tmp/pf29/compat\_admin  
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--pair-file pair.json \--dump-reader audit/tmp/pf29/reader.json \--dump-admin-dir audit/tmp/pf29/compat\_admin \> audit/tmp/pf29/compat.json

Prepare the complete inline `compat_request.json` in §7.2 before running local HTTP compat:

curl \-sS \-X POST [http://127.0.0.1:8000/api/compat/v1](http://127.0.0.1:8000/api/compat/v1) \-H 'Content-Type: application/json; charset=utf-8' \--data-binary @compat\_request.json \> http\_compat\_response.json

Run local conjunction:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--pair-file pair.json \> conjunction.json

Run Aux preview:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl aux-preview \--pair-file compat.json \--perspective shared \--show-narrative \--admin-out aux\_sidecar.json

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
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 bash ci/checks/check\_evidence\_index\_hash.sh LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 python tools/evidence/orientation\_demo.py \--check


Reader v1/v2 POST and read-only tooling examples are in §6.4, §7.6 and §7.7. Current-row examples require established dataset access; no row is created by a UUID example. The wheel, unsupported flag, legacy CLI and deferred live proof limitations in §16 apply to this reference.

````

END OF REDLINES
