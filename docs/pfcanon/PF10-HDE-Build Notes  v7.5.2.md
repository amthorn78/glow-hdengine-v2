# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** 7.5.2  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

**Purpose.** Working scratchpad for new, not-yet-merged documentation. When an entry is merged into canon, delete that entry here in the next cut. This file temporarily supersedes canon for the covered items. Higher numbers supersede. Titles-only cross-refs (no version numbers in body). 

TEMPLATE — Addendum Entry (do not edit/remove)  
ADDENDUM \<number\> — \<short, action-oriented title\>  
Timestamp: \<mmddyy hh:mm\>  
owner: \<role/person\>  
Details: \<specific information to drain to canon, it’s origin, and any evidence available\>

---

(Numbered Addenda Begin)  
---

## Addendum 1 — Token governance for PF09 / PF12 / Governance

### 1\. Intent and scope

This addenda defines how **acceptance tokens** are governed across:

* **HDE-Governance** (semantics and gating rules)

* **PF12-Canon-HDE-Schemas and Artifacts** (artifact schemas and acceptance hints)

* **PF09-Canon-HDE-Build Checklist** (phase-by-phase status view and acceptance lists)

Goal: prevent token drift by making PF09 a **consumer** of tokens, never a source of new ones, and by enforcing a single, explicit **Token Registry** owned upstream.

This addenda is **normative** and supersedes any prior informal practice about where tokens may be introduced or modified.

## Addendum 2 — A7 Catalog merge-gate & ops / SAFE audit integration

Timestamp: 111825 00:00  
 owner: PF10 / Governance \+ Engine QA

Details: PF09/PF12/PF04 need synchronized updates based on the PF09 rails-closed / rails-open audits and the new A7 / SAFE harness work. This addenda captures (1) the PF12 Catalog merge-gate rule, (2) PF04 ops-surface clarifications and SAFE rails-open token names, (3) the minimal PF05 editorial note, and (4) a dependency-ordered “what to do next” list and delta summary.

---

### 2.1 PF12 addendum (Addenda-PF12-A01)

**Purpose.** Tighten the coupling between PF12’s single-home **Endpoint Catalog artifacts** and A7 claims by making Catalog presence **merge-gating** for any A7 proofs.

**Insert under PF12 §8.6 “Endpoint Catalog artifacts” — Addendum A01 (names-only):**

**Merge gate.** Any PR that claims or updates A7 proofs **MUST** include a present `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) and its `.sha256` sidecar, plus a refreshed `artifacts/reader/endpoints_snapshot.json` and `artifacts/proofs/endpoints_env_gate_proof.log`. If the Catalog file is absent, CI **MUST** fail A7 token claims and classify all A7 tests as `skip (catalog_missing)`.

**Rationale.** The PF09 rails-closed and rails-open audits show that A7 proofing was blocked solely by the missing Catalog; PF12 already owns the endpoints snapshot and permits an **empty** `endpoints` array. This addenda makes **presence** of those artifacts mandatory to prevent drift between PF09 “Reader success surface & transport A7” and the actual repo state.

---

### 2.2 PF04 addendum (Addenda-PF04-A02)

**Purpose.** Confirm `/internal/version` ops-surface rules and centralize SAFE **rails-open** acceptance token names in Governance (PF04 §2.0).

**Insert in PF04 §10.5 “/internal/version ops surface” — Addendum A02:**

**Conditionals ignored.** `GET /internal/version` and `HEAD /internal/version` always return `200`; conditional headers are ignored (`304` is never returned).  
 **Headers.** `Cache-Control: no-store`; **no** `ETag`. `HEAD` echoes `Content-Type` and **may** carry `Content-Length == len(identity GET body)`. Evidence is stored as headers-only snapshots and body JSON (LF-terminated).

(This matches the PF09 audit captures and locks the ops-only posture so it cannot accidentally drift into A7 semantics.)

**Insert in PF04 §2.0 “Acceptance Tokens” — Addendum A02-b (names-only):**

Add/confirm the following tokens for rails-open SAFE policy and observability, with semantics owned by PF04 and artifact wiring in PF12/PF09:  
 `VENDOR_RETRY_BACKOFF_OK · PROVIDER_429_TYPED_OK · RETRY_AFTER_PARSE_OK · LOGS_KEYS_ONLY_OK`  
 (Bytes/paths live in PF12; harness wiring, CI jobs, and PF09 acceptance lists own where these must be proven.)

**Rationale.** The PF09 rails-open audit shows these behaviors cannot be claimed without explicit vendor/bridge harness jobs (`ci/jobs/rails_open_conformance.yml`, DB bridge captures, keys-only logs/metrics). PF04 must list the rails-open tokens centrally so PF09 and PF12 can reference them titles-only.

---

### 2.3 PF05 note (editorial alignment only)

**Note (no redline).** PF05 §5.6 already states that:

* A7 proofs run **only** on Catalog JSON success routes, and

* `/internal/version` is explicitly **non-A7** (ops-only) and must follow the no-store/no-ETag posture.

PF05 remains the single home for **Reader public bytes**. No structural change is required; PF05 should simply **reference PF12 Addendum A01** as the Catalog merge-gate when the Catalog artifacts are populated.

---

### 2.4 What to do next (dependency-ordered tasks)

1. **Create & index the Endpoint Catalog artifacts.**

   * Add `docs/ENDPOINTS_CATALOG.json` (canonical JSON; LF-terminated) with an **empty** `endpoints` list if necessary.

   * Add `docs/ENDPOINTS_CATALOG.json.sha256`.

   * Refresh `artifacts/reader/endpoints_snapshot.json` and `artifacts/proofs/endpoints_env_gate_proof.log`.

   * Update `docs/evidence/INDEX.json` \+ `INDEX.sha256` and `artifacts/evidence_index.jsonl` in the same PR to register the Catalog artifacts and proof files. (PF12 §8.6 \+ Addenda-PF12-A01 govern listing & schema.)

2. **Unify Reader↔CLI emitter inputs / identity and re-prove parity.**

   * Align `emit_reader_public_envelope` usage in CLI (`showcompat`) and Reader HTTP so the same Alice/Bob tuple emits identical `band`, `engine_tag`, `release_id`, and `idempotence_hash` under rails-closed.

   * Capture `artifacts/audit/http/reader_cli_diff.json` as passing parity evidence, and update the Evidence Index & Machine Mirror accordingly.

   * Only then may PF09 claim `CLI_READER_EMITTER_PARITY_OK`, `CLI_SHOWCOMPAT_CANON_OK`, and `READER_200_CTYPE_JSON_UTF8_OK` as **Done** for parity-dependent items.

3. **Add rails-open vendor/DB harness jobs and SAFE policy captures.**

   * Introduce `ci/jobs/rails_open_conformance.yml` for SAFE.2 (open-rails conformance) and jobs/scripts that exercise DB bridge fallback.

   * Capture and index:

     * Vendor policy pins: `artifacts/vendor/policies_pinned.md`.

     * 429 parsing: `artifacts/vendor/retry_after_parse.log`.

     * DB bridge fallback & parity: `artifacts/runtime/env_connectivity.snapshot.json`, `artifacts/db/provider_parity/*.json`, `artifacts/audit/db_bridge/rails_open.log`.

   * Ensure logs & metrics samples (`artifacts/bodygraph/keys_only.logs.sample`, `artifacts/bodygraph/metrics.snapshot.json`) are keys-only and registered in Evidence Index \+ Machine Mirror.

4. **Re-run A7 suite on the Catalog JSON success route.**

   * With Catalog present, capture GET/HEAD/304/encoding-invariance proofs on a Catalog-declared JSON success endpoint:  
      `artifacts/proofs/success_get.txt`, `success_head.txt`, `success_304.txt`, `success_encoding_invariance.txt`.

   * Index all A7 proofs in the Evidence Index & Machine Mirror in the same PR, and assert `A7_*` and `ENDPOINTS_CATALOG_*` tokens only once these artifacts are present.

---

### 2.5 Delta report (vs current PF09/PF12/PF04)

**PF09 (Build Checklist).**

* PF09’s A7, Reader↔CLI parity, SAFE-open, DB posture, Gate scripts, and Observability/Bench rows must **remain Not done** until:

  * Catalog artifacts (`docs/ENDPOINTS_CATALOG.json` \+ `.sha256`, snapshot, env-gate proof) exist and are indexed;

  * Reader↔CLI parity bytes are proven and show identical `band` and identity;

  * Rails-open SAFE and DB harnesses are in place with vendor/bridge evidence;

  * Keys-only logs, metrics, and bench harness captures are present and indexed.

* PF09 may still refer to acceptance tokens titles-only, but Addenda 1 (Token Governance) now enforces that PF09’s token lists are **subset-only** of the Token Registry and cannot introduce new token names.

**PF12 (Schemas & Artifacts).**

* **Addenda-PF12-A01** elevates Catalog presence from “nice-to-have” to **merge-gating** for any A7 token claims.

* PF12 continues to own artifact shapes, Evidence Index/Mirror schema, and “Acceptance hints (names-only)” lists; PF09 and PF04 reference these titles-only.

**PF04 (Governance).**

* **Addenda-PF04-A02** formally pins `/internal/version` behavior (conditionals ignored, no ETag, no A7 participation) and centralizes rails-open SAFE policy token names (`VENDOR_RETRY_BACKOFF_OK`, `PROVIDER_429_TYPED_OK`, `RETRY_AFTER_PARSE_OK`, `LOGS_KEYS_ONLY_OK`).

* PF04 remains the single home for transport and rails semantics; PF09/PF12 now consume these tokens, with addenda clarifying where evidence must live.

Below are the **new PF10 Build Notes addenda** to append to **PF10 v7.4** (living). Each addendum cites canon and will be **drained into the named homes** after EPIC‑011 closure.

---

## **Addendum 3 — Ops Refusal Proof Path (PF12/PF06 lock)**

**Intent.** Canonicalize the refusal proof artifact path and layout across all repos and QA runs.

**Normative effect (now):**

* The refusal proof MUST be written to **`artifacts/proofs/ops_refusal_proof.txt`**.

* File layout: **lower‑case headers** → **one blank line** → **single‑line canonical JSON** (numeric‑free, LF‑terminated).

* Evidence indexing: add a record to the **single** mirror `artifacts/evidence_index.jsonl` with a `proof_anchor` pointing to this file; update the Human Index and `INDEX.sha256` **in the same PR**.

**Why here:** PF12 owns artifacts/indexing; PF06 governs QA PR discipline. This addendum enforces the fixed path immediately for EPIC‑011 work and prevents drift from older paths.

**Drain to:** PF12 (Artifact catalog); PF06 (QA PR template).

---

## **Addendum 4 — DB Connectivity & Selection Posture (Token: `DB_CONN_ENV_OK`)**

**Intent.** Make the **presence‑order selection** and **typed failure** posture explicit in EPIC‑011 acceptance.

**Normative effect (now):**

* Acceptance roster for EPIC‑011 MUST include **`DB_CONN_ENV_OK`**.

* Evidence MUST include:

  * `artifacts/runtime/env_connectivity.snapshot.json` (selection order, e.g., `DATABASE_URL` → bridge).

  * A typed‑failure capture in non‑dev (numeric‑free JSON envelope per PF05/PF04).

* Index both artifacts in the Human Index \+ single Mirror **in the same PR**.

**Drain to:** PF04 (Token registry example set), PF05 (typed error envelope examples), PF12 (evidence examples).

---

## **Addendum 5 — EPIC‑011 Partition Plan: Non‑Deferred, Standard Paths**

**Intent.** Lock EPIC‑011 to a non‑deferred partition deliverable using standardized artifact paths.

**Normative effect (now):**

* EPIC‑011 MUST deliver `PARTITION_PLAN_OK` (no “plan‑or‑defer”).

* Required artifacts (standardized):

  * **`artifacts/db/partition_plan.txt`**, **`artifacts/db/partition_verify.log`** (adjacent).

* Index both in Human Index \+ Mirror (same PR).

**Drain to:** PF16 (Epic notes for 011), PF14 (explicit path examples).

---

## **Addendum 6 — BodyGraph Observability Tokens (NEW CANON)**

**Intent.** Name BodyGraph‑specific observability gates that extend PF04’s logging posture beyond `LOGS_KEYS_ONLY_OK`.

**Tokens (NEW CANON — to PF04 §2.0 on next edit):**

* **`BG_PRIVACY_REDACTION_OK`** — BodyGraph logs are keys‑only, redact PII/payload fragments; no secrets.

* **`BG_METRICS_EXPOSED_OK`** — BodyGraph metrics limited to counters/histograms; no payload or PII in labels.

**Required artifacts (paths pinned):**

* **`artifacts/bodygraph/keys_only.logs.sample`**

* **`artifacts/bodygraph/metrics.snapshot.json`**  
   Index in Human \+ Mirror in the same PR.

**Drain to:** PF04 (Token registry); PF19 (QA playbook examples).

---

## **Addendum 7 — Codespaces→PROD QA Window (EPIC‑011 execution frame)**

**Intent.** Capture production‑grade evidence from Codespaces under a guarded window, without expanding EPIC‑011 scope.

**Normative effect (now):**

* A PO‑approved, time‑boxed rails‑open window (names‑only env; **`SAFE_MODE=0, ALLOW_NETWORK=1`**) may be used to produce EPIC‑011 evidence: DB posture, pg‑bridge parity, ingest upsert \+ DB parity, TTL/SWR.

* A7/Catalog proofs remain out of scope (EPIC‑012).

* Every prod capture MUST run under env pins (`LC_ALL=C, LANG=C, TZ=UTC`) and land in Human Index \+ Mirror **in the same PR**.

**Drain to:** PF06 (execution checklist), PF19 (prod QA playbook).

---

## **Addendum 8 — Vendor 429 SAFE Posture (names‑only pins, EPIC‑011)**

**Intent.** Re‑affirm the rails‑open SAFE pins for vendor behavior asserted by name in EPIC‑011, with success‑path handling deferred to EPIC‑012.

**Normative effect (now):**

* EPIC‑011 asserts (names‑only): **`PROVIDER_429_TYPED_OK`**, **`RETRY_AFTER_PARSE_OK`**, alongside `VENDOR_RETRY_BACKOFF_OK` and `VENDOR_NO_PAYLOAD_LOGGING_OK`.

* No success‑path logic for 429 is introduced in EPIC‑011; A7/Catalog and 429 success behaviors are EPIC‑012.

**Drain to:** PF04 (token roster examples), PF05 (typed error mapping reference).

---

## **Addendum 9 — Evidence System Tightening (mirror cardinality & unknown‑key reject)**

**Intent.** Re‑assert single‑file mirror and unknown‑key rejection as merge‑gating for EPIC‑011 evidence PRs.

**Normative effect (now):**

* **Exactly one** machine mirror file: `artifacts/evidence_index.jsonl`.

* Each record is canonical JSON (ASCII key order), one line per record, LF‑terminated, and includes `proof_anchor`.

* Mirror ingest MUST **reject unknown keys**; CI MUST gate on: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`.

**Drain to:** PF12 (explicit schema/validator notes), PF19 (CI gate list).

---

### **Notes**

* These addenda extend **PF10 v7.4** (living) with session‑approved pins from the **r6 QA Guide** and IA plan; they do **not** change A7/Catalog or `/internal/version` scope (EPIC‑012 / EPIC‑013 respectively).

* Where **NEW CANON** is marked, Governance (PF04) will absorb the token names on its next cut; until then, treat this addendum as the operative source.

If you want these compiled into a paste‑ready `PF10-HDE-Build Notes v7.5.md` block, I can output the file‑formatted text exactly as above.

## ADDENDUM 10 — DB posture evidence & application role hardening (EPIC-011)

Timestamp: 111825 05:00  
owner: HDE-EPIC011-3 / Engine QA

Details: EPIC-011’s DB posture harness now captures grants and boundary-view policy for the engine schema via the DBAccess façade and standard artifact paths (artifacts/db/check\_schema.txt, artifacts/db/ddl\_fingerprint.json, artifacts/db/grants.txt, artifacts/db/partition\_plan.txt, artifacts/db/partition\_verify.log, artifacts/db/boundary\_view.readonly.proof.txt). In the current dev environment, all privileges on the EPIC-011 objects (hde.body\_graphs, hde.body\_graphs\_current, public.hde\_body\_graphs\_current and related) are held by the built-in postgres role; no dedicated non-superuser “application roles” (for example hde\_engine, hde\_reader, hde\_writer) exist or are used by the engine yet. The boundary view public.hde\_body\_graphs\_current is confirmed not updatable via information\_schema.views (is\_updatable \= NO, is\_insertable\_into \= NO), and the partition plan for hde.pair\_evaluation and hde.public\_results is present and verified. For EPIC-011, DB\_ROLE\_OK is interpreted as “posture is captured and indexed” rather than “app roles are already hardened”: it is sufficient that the harness truthfully records that postgres currently owns the EPIC-011 objects and that the boundary view and partition plan match expectations. Application role hardening (creating a dedicated runtime role such as hde\_engine and granting it only the privileges required by EPIC-005/EPIC-009/EPIC-011, then rotating DATABASE\_URL/DB\_BRIDGE\_URL to that role) is recommended as future infra work, but is not a blocker for EPIC-011 closure and is not implied by any existing EPIC-011 tokens. When such a role is introduced, the same DB posture harness and artifacts will serve as before/after evidence by showing the shift from postgres to the dedicated app role in grants.txt and the associated EPIC-011 objects.

Below are **paste‑ready** PF10 Build Notes addenda to append to the current file. They consolidate all EPIC‑011 QA changes, acceptance tokens, configuration updates, NEW CANON, and the synthetic‑identity decision, and they reference the existing PF10 living notes for continuity.

---

## **ADDENDUM 11 — PROD endpoints SoT (NEW CANON) \+ bootstrap acceptance (PR‑1)**

**Timestamp:** 111825 06:40  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **NEW CANON SoT:** add `docs/run/PROD_ENDPOINTS.json` (canonical JSON; one LF; names‑only base URLs). All runbooks/scripts **read** from this SoT; **no hard‑coded** prod URLs.  
* **Validator & evidence:** `scripts/runtime/validate_prod_endpoints.py` emits `artifacts/runtime/prod_endpoints_check.txt`. Index both SoT \+ check in Human Index & single Machine Mirror with `*.path_proof.txt`.  
* **Codespaces bootstrap:** `.devcontainer/devcontainer.json` installs package in editable mode and prepends `~/.local/bin` to `PATH`. Canonical CLI invocation is **module‑run** (`python -m engine.cli`).  
* **Acceptance tokens (merge‑gating for PR‑1):**  
   `CLI_MODULE_RUN_OK · CLI_PYPROJECT_ENTRYPOINT_OK · CLI_HELP_EXIT_0_OK · CLI_STDOUT_LF_OK · EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · EVIDENCE_INDEX_MIRROR_OK · MACHINE_MIRROR_UPDATED_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK · EVIDENCE_PATHS_VALIDATED_OK`.

---

## **ADDENDUM 12 — Evidence hash integrity incident & fix (PR‑1)**

**Timestamp:** 111825 06:42  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details (RCA & fix):**

* **Incident:** `artifacts/runtime/prod_endpoints_check.txt` changed, but its `*.path_proof.txt` and the mirror record retained a **stale sha256**, producing a tamper signal during verification.  
* **Root cause:** artifact was regenerated without synchronizing its **path\_proof** and the **Machine Mirror** entry.  
* **Remediation:** recomputed sha256; updated both `…prod_endpoints_check.txt.path_proof.txt` and the mirror’s `runtime.prod_endpoints_check` record.  
* **Preventive:** keep PR‑1 evidence tokens (above) **merge‑gating**; do not merge when any path\_proof ↔ mirror hash mismatch exists.

---

## **ADDENDUM 13 — DB posture & bridge parity (PR‑2 results)**

**Timestamp:** 111825 06:45  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **Façade‑only posture:** All captures via **DBAccess** (no `psql` / raw driver).  
* **Delivered artifacts:**  
   `artifacts/db/check_schema.txt` (`hde, public\n`) · `artifacts/db/ddl_fingerprint.json` (`"schema":"hde"`) · `artifacts/db/grants.txt` (EPIC‑011 objects only) · `artifacts/db/partition_plan.txt` · `artifacts/db/partition_verify.log` · `artifacts/db/boundary_view.readonly.proof.txt` (metadata shows not updatable).  
* **Bridge parity & fallback:**  
   `artifacts/db/provider_parity/{direct.json,bridge.json,summary.json}` · `artifacts/db_bridge/caps.snapshot.json` · `artifacts/db_bridge/adapter_selection.snapshot.json` (dev shows **bridge selected**, direct failed; parity \= `skip` with reason when direct unavailable).  
* **Dev‑only connectivity snapshot:** `artifacts/runtime/env_connectivity.snapshot.json` (selection order, attempts, typed failure envelope). **Forbidden in prod.**  
* **Acceptance tokens (PR‑2):**  
   `DB_SCHEMA_FINGERPRINT_OK · DB_RUNTIME_SEARCH_PATH_OK · DB_ROLE_OK · DB_BOUNDARY_VIEW_OK · PARTITION_PLAN_OK · DB_BRIDGE_CAPS_OK · DB_PROVIDER_PARITY_OK · DB_BRIDGE_FALLBACK_OK · DEV_DB_BRIDGE_FALLBACK_OK · DB_CONN_ENV_OK`  
   (+ standard evidence tokens for index/mirror).

---

## **ADDENDUM 14 — Grants artifact contract regression & fix (PR‑2 RCA)**

**Timestamp:** 111825 06:47  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **Bug:** Python posture harness initially emitted only explicit grant lines and **omitted** the **`ALTER DEFAULT PRIVILEGES:`** section required by legacy contract and QA checks.

**Fix:** restore contract:  
 \<explicit grants\>

ALTER DEFAULT PRIVILEGES:  
\<defaults ...\> | (none)

*   
* **Why it matters:** `DB_ROLE_OK` depends on the **full** grants posture (explicit \+ defaults). The corrected artifact is now merge‑gated by the evidence tokens.

---

## **ADDENDUM 15 — Prod rails‑window runbook & presenter parity helper (PR‑3)**

**Timestamp:** 111825 06:50  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **Runbook:** `docs/run/RUN_PROD_QA.md` defines **open rails → vendor upsert → DB resolve → byte parity → close rails → refusal proof**. Evidence paths fixed:  
   `artifacts/proofs/ops_refusal_proof.txt` · `artifacts/bodygraph/vendor_upsert.<id>.json` · `artifacts/bodygraph/db_resolve.<id>.json` · `artifacts/presenter/json_canon_compare.log`.  
* **Refusal proof format (canonical):** lower‑case headers; **one blank line**; LF‑terminated **numeric‑free JSON**; includes `cache-control: no-store` and excludes `etag`, `vary`, compression.  
* **Parity helper:** added `presenter/json_canon_compare.py` (module‑run) to compute canonical bytes \+ SHA‑256 and log parity.  
* **CLI corrections (docs):** removed non‑existent `--emit-json`; corrected `--upsert true` → `--upsert`.  
* **Acceptance tokens targeted by live run (captured in a subsequent evidence PR):**  
   `SNAPSHOT_HEADER_LOWERCASE_OK · INGEST_OK · INGEST_IDEMPOTENT_OK · BG_SOURCE_SELECTION_OK · BG_SOURCE_INVARIANCE_OK · BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`.

---

## **ADDENDUM 16 — EPIC‑011 synthetic test identity (NEW CANON) & QA alignment**

**Timestamp:** 111825 06:55  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **Canonical identity:** EPIC‑011 QA uses a **synthetic** test identity (alias) as the “person under test” for ingest/resolve/parity.  
* **Documentation:** add `docs/run/EPIC011_TEST_IDENTITIES.md` naming the synthetic alias and describing its properties and **pinned mapping** used by the engine; `RUN_PROD_QA.md` and all QA examples must reference **`<EPIC011_TEST_USER>`** (the alias), not a random/real UUID.  
* **Why:** earlier QA text implied “consented prod UUID.” The engine has been wired to a **synthetic** identity; this closes the docs/QA gap.  
* **Acceptance impact:** using a single pinned identity stabilizes `INGEST_IDEMPOTENT_OK`, `BG_SOURCE_INVARIANCE_OK`, and parity checks across vendor‑upsert vs DB‑resolve.  
* **Indexing:** treat `EPIC011_TEST_IDENTITIES.md` as governed (add to Human Index \+ Mirror with path‑proof).

---

## **ADDENDUM 17 — EPIC‑011 acceptance roster (merge‑blocking summary)**

**Timestamp:** 111825 06:58  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details (grouped tokens):**

* **CLI & bootstrap:**  
   `CLI_MODULE_RUN_OK · CLI_PYPROJECT_ENTRYPOINT_OK · CLI_HELP_EXIT_0_OK · CLI_STDOUT_LF_OK`.  
* **Evidence discipline:**  
   `EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · EVIDENCE_INDEX_MIRROR_OK · MACHINE_MIRROR_UPDATED_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK · EVIDENCE_PATHS_VALIDATED_OK`.  
* **DB posture & bridge:**  
   `DB_SCHEMA_FINGERPRINT_OK · DB_RUNTIME_SEARCH_PATH_OK · DB_ROLE_OK · DB_BOUNDARY_VIEW_OK · PARTITION_PLAN_OK · DB_BRIDGE_CAPS_OK · DB_PROVIDER_PARITY_OK · DB_BRIDGE_FALLBACK_OK · DEV_DB_BRIDGE_FALLBACK_OK · DB_CONN_ENV_OK`.  
* **Prod rails window & ingest/parity:**  
   `SNAPSHOT_HEADER_LOWERCASE_OK · INGEST_OK · INGEST_IDEMPOTENT_OK · BG_SOURCE_SELECTION_OK · BG_SOURCE_INVARIANCE_OK · BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`.  
* **Observability (NEW CANON):**  
   `LOGS_KEYS_ONLY_OK · BG_PRIVACY_REDACTION_OK · BG_METRICS_EXPOSED_OK`.  
* **Vendor SAFE (names‑only pins for EPIC‑011):**  
   `VENDOR_RETRY_BACKOFF_OK · PROVIDER_429_TYPED_OK · RETRY_AFTER_PARSE_OK`.

---

## **ADDENDUM 18 — Execution phases for EPIC‑011 (what must precede prod QA)**

**Timestamp:** 111825 07:00  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* **Before opening prod rails:** complete **PR‑1 (bootstrap \+ PROD SoT)** and **PR‑2 (DB posture \+ bridge parity)**; merge **PR‑3 (runbook)**.  
* **Prod QA window:** run the choreography in `RUN_PROD_QA.md`; collect real artifacts under the fixed paths.  
* **After window:** submit an **evidence ingest PR** (index \+ mirror \+ path‑proofs) to claim the ingest/rails tokens.  
* **Then finish:** **PR‑4** (observability logs/metrics \+ privacy) and **PR‑5** (backup/restore/retention \+ CI gates). **PR‑6** (vendor 429/backoff) is optional but recommended.

---

## **ADDENDUM 19 — CLI posture reaffirmation (no destructive changes in PR‑3)**

**Timestamp:** 111825 07:02  
 **owner:** HDE‑EPIC011‑3 / Engine QA

**Details:**

* PR‑3 added a **new** helper `presenter/json_canon_compare.py` but made **no changes** to `engine.cli` parser or behavior.  
* Canonical invocation remains **module‑run**; runbook examples are aligned to actual CLI flags (no `--emit-json`; `--upsert` is boolean).  
* This addendum prevents misinterpretation that PR‑3 “changed the CLI.”

---

**Note:** Once these addenda are merged into PF10, drain the normative parts to their permanent homes on next cuts: token names to **PF04** (Governance), artifact shapes & index rules to **PF12**, runbook & synthetic identity docs to **`docs/run`**, and phase sequencing to **PF06/PF19**.

If you want, I can output these as an updated `PF10-HDE-Build Notes v7.5.2.md` file blob ready to commit.

