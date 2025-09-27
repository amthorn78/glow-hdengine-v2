## **Human Design API**

Absolutely—no need for the URL. I’ve drafted a repo-ready, standalone guide based on our findings and decisions.

# **Human Design API Integration Guide (Glow) — v1.0**

**Owner:** Isis (Engine Lead)  
 **Scope:** Vendor ingest → Normalization → Replay fixtures → Safety & rate limits → CLI notes  
 **Applies to:** HumanDesignAPI.nl (HD API) \+ optional Google Places/Time Zone  
 **Last updated:** *today*

---

## **1\) Purpose & posture**

* We use the external HD API only to fetch **chart anatomy** (gates, channels, centers, type, authority, definition).  
* All vendor responses are transformed into a **closed, deterministic Glow schema** for replay and testing.  
* **SAFE\_MODE=1** by default in CI/tests: any network call must fail **immediately** with a typed error.  
* Artifacts (fixtures, normalized JSON) are **UTF-8, sorted keys, compact**, with **exactly one trailing `\n`**.

---

## **2\) Endpoints & auth (vendor)**

* **HD API endpoint used:** `POST /v1/bodygraphs`  
* **Required headers:** `HD-Api-Key`, `HD-Geocode-Key` (names only; secrets never stored in repo).  
* **Inputs (typical):** birth date, birth time, location fields (see §5 for how we normalize).  
* **Observed outputs:** gates, channels (sometimes omitted by vendor), centers, type, authority, definition.

We capture **RAW** payloads selectively for fixtures; we never commit secrets, full queries, PII, or URIs.

---

## **3\) SAFE\_MODE & network guards**

* **Module:** `adapters/_net.py`  
  * `NetworkDisabledError`, `safe_mode_enabled()`, `require_network(service_name)`  
* **Rule:** All live callers (`adapters/hdapi/*`, `adapters/geo/*`) must call `require_network()` first.  
* **Default:** `SAFE_MODE=1` in CI/tests → network calls **raise immediately** (no sleep/retry).  
* **Manual smoke:** set `SAFE_MODE=0` locally for controlled captures.

---

## **4\) Normalized Glow schema (closed)**

**File:** `schemas/hdapi.normalized.v1.schema.json` (all objects `additionalProperties:false`)

{  
  "schema": "chart.normalized.v1",  
  "source": "hdapi",  
  "birth": {  
    "date": "YYYY-MM-DD",  
    "time": "HH:MM",  
    "timezone": "America/Los\_Angeles"   // IANA tzId  
  },  
  "location": {  
    "name": "City, CC",  
    "lat": "37.774900",                 // strings, fixed 6+ dp  
    "lng": "-122.419400"  
  },  
  "mechanics": {  
    "gates": \["05","06","10", "..."\],   // %02d strings, sorted, unique  
    "channels": \["01-08","10-20", "..."\], // %02d-%02d min-first, sorted, unique  
    "centers": \[  
      {"id": "head", "state": "defined|undefined"},  
      {"id": "ajna", "state": "defined|undefined"}  
      // …  
    \]  
  },  
  "type": "manifestor|generator|manifesting\_generator|projector|reflector",  
  "authority": "emotional|sacral|splenic|ego|self\_projected|environment|lunar|none",  
  "definition": "single|split|triple\_split|quadruple\_split|none"  
}

### **Canon rules**

* **Gates:** strings, `%02d`, **sorted/unique**.  
* **Channels:** derive `%02d-%02d` as **min-first**, **sorted/unique**. If vendor omits channels, we **derive** from gates using our canon channel map.  
* **Centers:** ids (lowercase): `head, ajna, throat, g, ego, sacral, spleen, solar_plexus, root`. Vendor aliases normalized (`heart|will → ego`).  
* **Type/Authority/Definition:** **enum-closed**, with vendor→Glow mapping tables (see §7).

Unknown/unsupported enum → **NormalizationEnumError** (typed).

---

## **5\) Location & time handling (DST-safe)**

* **lat/lng** in normalized output are **strings** with fixed precision (no binary floats).  
* **timezone** is IANA tzId (e.g., `Europe/Amsterdam`), not a numeric offset.  
* **Time zone lookup (optional, via Google Time Zone):**  
  * Always query with the **birth UTC timestamp**, not “now”.  
  * On DST ambiguity, pick the **earlier legal instant** deterministically (documented tie-break).  
* **Google Places (optional):** If used for geocoding, store **only** place display name and lat/lng strings; never store raw queries.

---

## **6\) Rate limits & retries**

* Backoff: `min(2**retries, 2)` seconds, **max 3 attempts**.  
* If `Retry-After` (or similar) header present, parse to `retry_after_ms` on error and raise **UpstreamRateLimited** (typed).  
* In tests, inject a `sleep_fn` so we **never actually sleep**.

---

## **7\) Vendor → Glow normalization tables (excerpt)**

**Centers (aliases → id):**

* `heart, will, ego` → `ego`  
* `identity, g` → `g`  
* `solar plexus, emotional` → `solar_plexus`

**Types:**

* `Manifestor` → `manifestor`  
* `Generator` → `generator`  
* `Manifesting Generator` → `manifesting_generator`  
* `Projector` → `projector`  
* `Reflector` → `reflector`

**Authorities:**

* `Emotional (Solar Plexus)` → `emotional`  
* `Sacral` → `sacral`  
* `Splenic` → `splenic`  
* `Ego (Heart)` → `ego`  
* `Self Projected (G)` → `self_projected`  
* `Mental/Environment` → `environment`  
* `Lunar` → `lunar`  
* None/Unknown → `none` (only if vendor explicitly expresses none)

**Definition:**  
 `Single`, `Split`, `Triple Split`, `Quadruple Split`, or `None` → lowercased with underscores as shown in schema.

Mapping tables live in `docs/hdapi_go_nogo.md` with full enumerations.

---

## **8\) Fixtures, provenance, and checksums**

**Folders:**

* RAW: `fixtures/hdapi/raw/*.json` (+ `.sha256`)  
* Provenance (per RAW): `*_provenance.json`  
* Normalized: `fixtures/hdapi/normalized/*_normalized.json` (+ `.sha256`)

**Provenance shape (names only):**

{  
  "source": "HumanDesignAPI.nl",  
  "endpoint": "POST /v1/bodygraphs",  
  "query\_shape": \["birthdate","birthtime","location"\],  
  "captured\_at": "YYYY-MM-DDTHH:MM:SSZ",  
  "http\_status": 200,  
  "rate\_limit\_headers": \[\]  
}

**Discipline:** All JSON via canonical serializer; **exactly one trailing `\n`**. No secrets/PII ever stored.

---

## **9\) Normalization contract (implementation notes)**

* **File:** `adapters/hdapi/normalize.py`  
  * Validates and maps centers, type, authority, definition via enum tables.  
  * Gates/Channels: formats as strings; channels fallback from gates using canon map.  
  * Sorts/dedupes arrays; emits consistent key order; returns normalized dict.  
* **Schema validation:** `schemas/hdapi.normalized.v1.schema.json` enforced in tests.

---

## **10\) Testing & replay (offline by default)**

* **Integration (fixtures):** Validate normalized docs against schema; assert two-run identity; verify `.sha256` matches literal bytes (newline included).  
* **Unit:** Channel derivation from gates (min-first `%02d-%02d`, sorted); enum closure (unknowns raise).  
* **SAFE\_MODE:** All network functions raise `NetworkDisabledError` when `SAFE_MODE=1`.

---

## **11\) CLI (admin-only) — current stance**

* **Planned card:** `CORE-CLI-BODYGRAPH-007`  
  * `fetch-chart` prints **normalized JSON** to stdout (canonical serializer; single LF).  
  * `--admin-out <path>` writes a sidecar (0600 perms) with raw & provenance refs; stdout bytes **unchanged**.  
  * Optional `--place-id` to bypass Places when known.  
* A small fixture-backed helper already proved **stdout invariance**; live-key mode will be implemented in the card above.

---

## **12\) Security & privacy**

* Secrets only in env; `.env*` ignored by git.  
* Logs are **keys-only**: route, status, correlation\_id, endpoint\_name, fixture\_tag/hash. **No payloads, no queries, no keys**.  
* Fixtures never include emails/names/addresses or raw URIs.

---

## **13\) Go / No-Go criteria**

**Go** when all true:

1. Normalized schema validates; enum tables complete; channel derivation proven.  
2. Fixtures present (≥3) with RAW \+ normalized \+ `.sha256` \+ provenance.  
3. Replay tests pass offline (SAFE\_MODE on).  
4. Rate-limit handling is deterministic; no sleeps in tests.  
5. DST tie-break documented and tested on boundary dates.

**No-Go** if any:

* Floats emitted in normalized JSON; missing newline discipline; unknown enums silently pass; network calls in SAFE\_MODE.

---

## **14\) Known limitations & future work**

* Vendor may omit `channels`; our derivation is canon-correct but depends on full gate list quality.  
* Localization not in scope for this ingest; location display stays vendor/Places text.  
* CLI live capture and admin UX ship under `CORE-CLI-BODYGRAPH-007`.

---

## **15\) Quick appendix**

### **15.1 Example normalized (truncated)**

{  
  "schema":"chart.normalized.v1",  
  "source":"hdapi",  
  "birth":{"date":"1990-05-21","time":"14:30","timezone":"Europe/Amsterdam"},  
  "location":{"name":"Amsterdam, NL","lat":"52.367600","lng":"4.904100"},  
  "mechanics":{  
    "gates":\["01","08","10","20","57"\],  
    "channels":\["01-08","10-20","20-57"\],  
    "centers":\[  
      {"id":"throat","state":"defined"},  
      {"id":"g","state":"defined"},  
      {"id":"spleen","state":"defined"}  
    \]  
  },  
  "type":"projector",  
  "authority":"splenic",  
  "definition":"single"  
}

### **15.2 Example provenance**

{  
  "source":"HumanDesignAPI.nl",  
  "endpoint":"POST /v1/bodygraphs",  
  "query\_shape":\["birthdate","birthtime","location"\],  
  "captured\_at":"2025-09-27T01:24:14Z",  
  "http\_status":200,  
  "rate\_limit\_headers":\[\]  
}

---

## **16\) File index (expected in repo)**

* `schemas/hdapi.normalized.v1.schema.json`  
* `adapters/_net.py`, `adapters/hdapi/normalize.py`  
* `fixtures/hdapi/raw/*.json` (+ `.sha256`, `_provenance.json`)  
* `fixtures/hdapi/normalized/*_normalized.json` (+ `.sha256`)  
* `tests/integration/test_normalized_fixture.py`  
* `tests/unit/test_channel_derivation.py`  
* `tests/adapters/test_safe_mode.py`  
* `artifacts/hdapi/endpoints.json`, `artifacts/hdapi/rate_limits.md`  
* `docs/hdapi_go_nogo.md` (enum maps & rules)

---

If you want this saved as a file now, say the filename (e.g., `docs/HumanDesignAPI_Integration_Guide_v1.md`) and I’ll output it exactly in that format.

https://api.humandesignapi.nl/api-docs/

  import requests  
  import json  
  import os  
    
  url \= 'https://api.humandesignapi.nl/v1/bodygraphs/simple';  
  headers \= {  
      'Content-Type': 'application/json',  
      'HD-Api-Key': os.environ.get('HD\_API\_KEY'),  
      'HD-Geocode-Key': os.environ.get('GEO\_API\_KEY'),  
  }  
  data \= {  
      'birthdate': "05-Sep-90",  
      'birthtime': "21:17",  
      'location': "Haarlem, The Netherlands",  
  }  
    
  response \= requests.post(url, headers=headers, data=json.dumps(data))  
  bodygraph \= response.json()  
  \# Process the bodygraph data as needed  
    

## **1.1.204**

## **OAS 3.0**

Welcome to the Human Design API documentation. This API provides endpoints for calculating and analyzing Human Design charts.

## **Authentication**

All endpoints require an API key to be passed in the header as `HD-Api-Key`.

## **Google Places API**

All endpoints require a Geocode key to be passed in the header as `HD-Geocode-Key`.

[API Support \- Website](https://humandesignapi.nl/)

Send email to API Support

[Proprietary](https://humandesignapi.nl/)

**Servers**

**https://api.humandesignapi.nl/v1/ \- Production server**

**Authorize**

### [**Bodygraph**](https://api.humandesignapi.nl/api-docs/#/Bodygraph)

**POST**

[/bodygraphs](https://api.humandesignapi.nl/api-docs/#/Bodygraph/post_bodygraphs)

Generate a complete bodygraph

#### **Parameters**

**Try it out**

No parameters

#### **Request body**

**application/json**

* **Example Value**  
* Schema

{  
  "birthdate": "01-Jan-1990",  
  "birthtime": "14:30",  
  "location": "Haarlem, The Netherlands"

}

#### **Responses**

| Code | Description | Links |
| :---- | :---- | :---- |
| 200 | Successful bodygraph generation Media type **application/json** Controls Accept header. **Example Value** Schema {   "type": "Generator",   "profile": "6/2",   "channels\_short": \[     "20-34",     "10-57"   \],   "centers": \[     "Head",     "Ajna",     "G",     "Sacral"   \],   "strategy": "To Respond",   "authority": "Sacral",   "incarnation\_cross": "Cross of Tension (20/34 | 10/57)",   "definition": "Split Definition",   "signature": "Satisfaction",   "not\_self\_theme": "Frustration",   "cognition": "Strategic",   "determination": "Focused Determination",   "variables": "PLL DRL",   "motivation": "Hope/Pain",   "transference": "Dominance",   "perspective": "Observation",   "distraction": "Attachment",   "circuitries": "Individual, Tribal",   "channels\_long": \[     "Integration (20/34)",     "Awareness (10/57)"   \],   "gates": \[     "20",     "34",     "10",     "57"   \],   "activations": {     "design": {       "sun": "20.1",       "earth": "34.6"     },     "personality": {       "sun": "10.3",       "earth": "57.3"     }   } } | *No links* |
| 401 | API Key missing Media type **application/json Example Value** Schema {   "status": "error",   "code": 401,   "message": "API Key missing" } | *No links* |
| 403 | User does not have access to this feature Media type **application/json Example Value** Schema {   "status": "error",   "code": 403,   "message": "User does not have access to this feature" } | *No links* |
| 404 | Not found Media type **application/json Example Value** Schema {   "status": "error",   "code": 404,   "message": "Not found" } | *No links* |
| 500 | Server error Media type **application/json Example Value** Schema {   "status": "error",   "code": 500,   "message": "Internal server error" } | *No links* |

**POST**

[/bodygraphs/simple](https://api.humandesignapi.nl/api-docs/#/Bodygraph/post_bodygraphs_simple)

Generate a simplified bodygraph

#### **Parameters**

**Try it out**

No parameters

#### **Request body**

**application/json**

* **Example Value**  
* Schema

{  
  "birthdate": "01-Jan-1990",  
  "birthtime": "14:30",  
  "location": "Haarlem, The Netherlands"

}

#### **Responses**

| Code | Description | Links |
| :---- | :---- | :---- |
| 200 | Successful simplified bodygraph generation Media type **application/json** Controls Accept header. **Example Value** Schema {   "type": "Generator",   "profile": "6/2",   "gates": \[     "20",     "34",     "10",     "57"   \],   "channels\_short": \[     "20-34",     "10-57"   \],   "centers": \[     "Head",     "Ajna",     "G",     "Sacral"   \] } | *No links* |
| 400 | Invalid input Media type **application/json Example Value** Schema {   "status": "error",   "code": 400,   "message": "Invalid input" } | *No links* |
| 401 | API Key missing Media type **application/json Example Value** Schema {   "status": "error",   "code": 401,   "message": "API Key missing" } | *No links* |
| 403 | User does not have access to this feature Media type **application/json Example Value** Schema {   "status": "error",   "code": 403,   "message": "User does not have access to this feature" } | *No links* |
| 404 | Not found Media type **application/json Example Value** Schema {   "status": "error",   "code": 404,   "message": "Not found" } | *No links* |
| 500 | Server error Media type **application/json Example Value** Schema {   "status": "error",   "code": 500,   "message": "Internal server error" } |  |

