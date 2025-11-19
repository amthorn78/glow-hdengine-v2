# **PF09-Canon-HDE-Build Checklist**

**Version:** v1.4.9  
 **Status:** Canon  
**Effective date:** 2025-11-17

**Last Update Gate:** PF14 v1.8

### **Scope (canon)**

Build‑only, dependency‑ordered checklist of HD Engine components and concrete implementation tasks required to reach a stable production run. This list excludes documentation and process chores and focuses on shipping code, wiring transport, enforcing determinism, and proving behavior with runnable evidence. Organized by seven alchemical phases.

### **Conventions**

* **Statuses:** Done / Partial / Not done / Consolidation pending / Optional.

* **“SoT: canon” in Notes only.** Use to mark behavior locked by spec while code evidence is pending (never as a Status).

* **Sequencing pattern:** determinism first → transport parity → evidence.

---

## **Evidence Index and mirror (paths pinned)**

**Human Index (authoritative).** `docs/evidence/INDEX.json` — titles and paths only; no payload bytes. *Single home for the listing:* see **PF12 §8.6 “Evidence Index entries (titles/paths only)”**. PF09 does not duplicate that list.  
 **Human Index hash sentinel.** `docs/evidence/INDEX.sha256` — sha256 over the exact bytes of `INDEX.json`. Update in the same PR as the Human Index. **Gate:** `EVIDENCE_INDEX_HASH_OK`.

**Machine Mirror (records‑only).** `artifacts/evidence_index.jsonl` — one JSON object per line; canonical JSON (UTF‑8, no BOM; ASCII‑sorted keys; compact; exactly one trailing `\n`). **Unknown keys are rejected.** Keep **1:1 parity** with the Human Index; provide path‑proofs.

**Mirror discipline (normative).**  
 The machine mirror is **one and only one** file at `artifacts/evidence_index.jsonl`; **records‑only canonical JSONL** (UTF‑8; ASCII‑sorted keys; compact; exactly one LF per record); **unknown keys rejected**; **sort‑before‑write** by `(artifact_key, discovered_physical_path)`.  
 **Exact field order (per PF12/PF10):** `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.  
 **Acceptance & CI (titles‑only):** `EVIDENCE_INDEX_UPDATED_OK` · `EVIDENCE_INDEX_HASH_OK` · `EVIDENCE_INDEX_MIRROR_OK` · `MACHINE_MIRROR_UPDATED_OK` · `CI_CHECK_MIRROR_SCHEMA_OK` · `CI_CHECK_FINAL_LF_OK` · `EVIDENCE_PATHS_VALIDATED_OK` · `ENV_LC_ALL_C_OK`. *(Schema & tokens are routed by title to PF12/PF09; this checklist does not restate the mirror schema.)*

**Minimum mirror record fields (reject unknown keys)**

`{`

  `"artifact_key": "",`

  `"role": "<proof|golden|snapshot|script|log>",`

  `"sha256": "<lowercase 64-hex>",`

  `"size_bytes": 0,`

  `"produced_at_utc": "",`

  `"discovered_physical_path": "",`

  `"proof_anchor": ""`

`}`

**Field order and write discipline (merge‑blocking).**  
 • **ASCII field order (exact):** `artifact_key, discovered_physical_path, produced_at_utc, proof_anchor, role, sha256, size_bytes`.  
 • **Sort‑before‑write** by the tuple `(artifact_key, discovered_physical_path)`.  
 • **Single mirror file:** exactly one `artifacts/evidence_index.jsonl` in the repo.  
 • **Uniqueness:** the pair `(artifact_key, discovered_physical_path)` is unique; duplicates fail CI.  
 • **CI gate:** fail the PR on missing human↔machine parity, non‑canonical JSONL, unknown keys, missing path‑proofs, wrong field order, or unsorted records.

**Parity and path‑proofs.**  
 • **Same‑PR parity:** Human Index ↔ Machine Mirror must be **1:1** in the **same PR** or commit that adds, moves, or renames artifacts.  
 • **Path‑proofs:** store a `path_proof.txt` alongside each artifact and reference it via `proof_anchor`. The `proof_anchor` must exactly match the discovered path‑proof for that artifact.  
 • **Governed locations only:** index artifacts only from governed paths (`artifacts/**`, `audit/**`, `docs/evidence/**`); **transient generator paths** (e.g. `codex/out/**`) are not authoritative and **MUST NOT** be indexed — relocate proofs under `artifacts/**` before gating.

**Registry report (names‑only).**  
 `artifacts/registry/registry_report.json` (canonical JSON; kept in sync and mirrored).

**Governed record types.**  
 Single home: **PF12 Appendix C “Governed artifact record types.”** PF09 does not define or duplicate these.

**Locale pins for all byte checks.**  
 `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

---

## **A7 proof surface (titles‑only pointers)**

**Single home (location & scope).**  
 • **Catalog file:** `docs/ENDPOINTS_CATALOG.json` (canonical JSON; one LF) with `docs/ENDPOINTS_CATALOG.json.sha256`.  
 • **Scope:** list **JSON success routes only**, each with an env‑gate; **exclude all `/internal/*`**.  
 • **Proof surface:** **A7 proofs run only on a route listed in the Catalog.**

**Env‑gating proof (headers‑only).**  
 • `artifacts/proofs/endpoints_env_gate_proof.log` shows non‑prod entries are unreachable in prod.  
 • Index in human \+ machine evidence in the same PR.

**A7 invariants to prove (headers‑only).**  
 • **200:** strong **quoted** `ETag`; `Vary: Authorization, Accept-Encoding`; success cache headers.  
 • **HEAD:** 200; no body; validators mirror 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.  
 • **304:** only after prior 200; **omit `Content-Type` and omit `Content-Length`**; validators mirror cached 200\.  
 • **Encoding invariance:** for the same canonical LF‑terminated body, ETag identity and the effective Content‑Length are stable across accepted encodings (identity/gzip/br).  
 • **Writers/errors posture:** writers & error routes carry `Cache-Control: no-store`.

**Artifacts (headers‑only; one LF each).**  
 • `artifacts/proofs/success_get.txt`  
 • `artifacts/proofs/success_head.txt`  
 • `artifacts/proofs/success_304.txt`  
 • `artifacts/proofs/success_encoding_invariance.txt`  
 • `artifacts/proofs/success_writers_errors.txt`  
 *(Capture on a Catalog route; index human+machine in the same PR; machine mirror is records‑only canonical JSONL; unknown‑key reject; each record has a `proof_anchor`.)*

**Transport guidance — A7 rows & Catalog tie‑in.**  
 • A7 rows apply **only** to routes declared in `docs/ENDPOINTS_CATALOG.json`.  
 • `/internal/*` (including `/internal/version`) is **never Catalog‑eligible** and is verified under ops posture: **no‑store**, **no `ETag`**, **HEAD 200 parity**, **conditionals ignored**.  
 • When capturing A7 proofs, always cite the Catalog entry used and include the env‑gate proof in the same PR.

**A7/Catalog acceptance (titles‑only).**  
 `ENDPOINTS_CATALOG_OK` · `ENDPOINTS_CATALOG_ENV_GATE_OK` · `A7_GET_QUOTED_ETAG_OK` · `A7_HEAD_PARITY_OK` · `A7_304_OMITS_CT_CL_OK` · `A7_VARY_AUTH_AE_OK` · `A7_ENCODING_INVARIANCE_OK`.

---

## **Index & mirror discipline**

Update the **Human Evidence Index** (`docs/evidence/INDEX.json`) and the **Machine Mirror** (`artifacts/evidence_index.jsonl`) in the **same PR**. Mirror rules: **records‑only canonical JSONL** (UTF‑8; ASCII‑sorted keys; compact; one LF); unknown keys rejected; include `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor`. **Locale pins** apply to all byte checks: `LC_ALL=C`, `LANG=C`, `TZ=UTC`. 

---

## **Phase I — Calcination (Foundations first)**

### **Completed**

#### **Canonical Enumerations Registry — Done**

Notes (SoT). Enumerations are frozen in canon (HDE-Math-Spec, HDE-Schemas & Artifacts; titles only). Registry structure and generation scripts are in place.

---

### **Not done**

#### **Canonical Serialization Package — Not done**

Status (Audit v1 — 2025-11-17): Missing tokens: `CLI_NO_ALT_JSON_OK`, `CLI_READER_EMITTER_PARITY_OK`, `CLI_SHOWCOMPAT_CANON_OK`, `CLI_STDOUT_LF_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`. Evidence: —.

Notes (SoT). Single presenter/emitter; UTF-8 (no BOM), ASCII-sorted keys, compact separators, exactly one trailing LF; arrays-as-sets deduped & ASCII-sorted; all dumps/compares under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Evidence (titles/paths only)**

* `tests/test_emitter_determinism.py`

* `audit/gates/canonical_json/json_canonical_check.log`

* `audit/gates/canonical_json/json_canon_compare.log`

* `artifacts/cli/guards/serializer_grep_guard.log`

* `artifacts/cli/guards/emitter_symbol_proof.txt`

---

#### **Repository & Tooling Skeleton — Not done**

Status (Audit v1 — 2025-11-17): Missing tokens: `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`. Human Index \+ sentinel and Machine Mirror absent.

**Tasks to finish**

* **Human Evidence Index (titles/paths only).**  
   Path: `docs/evidence/INDEX.json`.  
   Single home for the listing: see PF-Canon-HDE-Schemas & Artifacts §8.6 “Evidence Index entries (titles/paths only)”. PF09 does not duplicate that list.

* **Human Evidence Index hash sentinel.**  
   Path: `docs/evidence/INDEX.sha256`. Compute sha256 over the exact bytes of `INDEX.json`. Update in the same PR as the Human Index. Gate: `EVIDENCE_INDEX_HASH_OK`.

* **Machine Evidence Index — JSONL (records-only).**  
   Path: `artifacts/evidence_index.jsonl`; one JSON object per line; canonical JSONL (UTF-8, no BOM; ASCII-sorted keys; compact; ends with exactly one LF); unknown keys rejected; maintain 1:1 parity with the Human Index; provide path-proofs.

* **Mirror discipline.**  
   Enforce ASCII field order (exact):  
   `artifact_key`, `discovered_physical_path`, `produced_at_utc`, `proof_anchor`, `role`, `sha256`, `size_bytes`.  
   Sort-before-write by the tuple `(artifact_key, discovered_physical_path)`. Ensure uniqueness of the pair `(artifact_key, discovered_physical_path)`.

* **Registry report (names-only).**  
   Produce on every run. Path: `artifacts/registry/registry_report.json` (canonical JSON).

* **Locale pins.**  
   Export `LC_ALL=C`, `LANG=C`, `TZ=UTC` in all lint/test/artifact jobs.

* **Topology orientation demo.**  
   Add `audit/gates/topology/orientation_demo.txt` showing high→low normalized to min→max `NN–NN` (before/after).

* **Wire local run targets.**  
   Keep `scripts/make_sanity.sh` current.

**Acceptance (titles only)**  
 `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `JSON_CANONICAL_CHECK_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `EVIDENCE_INDEX_HASH_OK`.

**Indexing & parity**  
 Update the Human Index (`docs/evidence/INDEX.json`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR (records-only; with path-proofs). Governed locations only. Transient generator paths (for example `codex/out/**`) are not authoritative and MUST NOT be indexed; relocate proofs under `artifacts/**` before gating. (Mirror remains records-only canonical JSONL with path-proofs.)

**Mirror record — minimum fields (reject unknown keys)**

`{`

  `"artifact_key": "<title from human Index>",`

  `"role": "<proof|golden|snapshot|script|log>",`

  `"sha256": "<lowercase 64-hex>",`

  `"size_bytes": <non-negative integer>,`

  `"produced_at_utc": "<UTC ISO-8601 with Z>",`

  `"discovered_physical_path": "<repo-relative POSIX path>",`

  `"proof_anchor": "<transcript ref or on-disk path_proof.txt>"`

`}`

**Path-proof**  
 Store a stat transcript next to each artifact (for example `path_proof.txt` or `<artifact>.stat.txt`) and reference it via `proof_anchor`.

**CI gate**  
 CI must fail the PR if the Human Index or the Machine Mirror lacks an entry for any new/renamed artifact in this change, or if JSONL is non-canonical / has unknown keys / missing path-proofs / wrong field order / not sorted.

---

#### **Programmatic Configuration System — Not done**

Status (Audit v1 — 2025-11-17): Not done. Unknown-ID failure capture and registry report missing; indices not updated.

**Tasks to finish**

* **Unknown-ID hard-fail** required.

* **Input-alias policy.**  
   Default OFF (titles-only to HDE-Schemas & Artifacts / HDE-Math-Spec for ownership). If ON, normalize via declared alias ledgers; outputs remain canonical; reject unknowns.

* **Emit registry report** each run (names-only, canonical JSON).  
   Path: `artifacts/registry/registry_report.json`.

**Acceptance (titles only)**  
 `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`.

**Indexing & parity**  
 Update the Human Index and the Machine Mirror in the same PR (records-only; with path-proofs; do not list entries here — see PF-Canon-HDE-Schemas & Artifacts §8.6).

---

#### **Deterministic Tie-Break & Total-Order Module — Not done**

Status (Audit v1 — 2025-11-17): Not done. Missing tokens: `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`. No comparator proofs or sorted snapshots are indexed.

**Tasks**

* Implement ASCII comparators for ids, centers, channels (`NN–NN` min-first, zero-padded), and categories (frozen Magic-10 rank → ASCII).

* Provide helpers: `dedupe_sort`, `ensure_total_order`, `canonicalize_array`, `sort_pairs`; require their use at all ordered emission sites (composites, categories, evidence).

* Property tests: antisymmetry, transitivity, totality; prove channel order (min-first `NN–NN`) and category loop equals the frozen order.

* AB↔BA and two-run identity checks; canonical re-serialization byte-compare under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Evidence (titles/paths only)**

* `artifacts/engine/order/props_total_order.log`

* `artifacts/engine/order/channels_sorted.snapshot.json`

* `artifacts/engine/order/categories_iter.snapshot.json`

* `artifacts/engine/order/abba_identity.bytes`

**Acceptance (titles only)**  
 `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`.

---

###### **ChatGPT said:**

## **Phase II — Dissolution (Normalize and make it pure)**

### **Completed**

#### **Deterministic Engine Core — Not done**

Status (Audit v1 — 2025-11-17): Missing tokens: `TWO_RUN_IDENTITY_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `NO_IO_NO_CLOCKS_OK`. Evidence: —.

Notes (SoT). Core is pure compute (ops, scoring, aggregation). No I/O, no clocks, no globals/env. Executions are AB↔BA neutral and satisfy two-run identity. All reductions stabilize order via ASCII sorting; any core-emitted JSON for evidence is UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one LF; arrays treated as sets are deduped and ASCII-sorted; checks run under `LC_ALL=C`.

**Evidence (titles/paths only)**

* `artifacts/engine/tworun_identity.log` — two-run identity proof

* `artifacts/engine/abba_identity.bytes` — AB↔BA compare

* `artifacts/engine/guards/no_io_no_clock.report` — static proof (no I/O, clocks, globals)

**Acceptance (titles-only)**  
 `TWO_RUN_IDENTITY_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `NO_IO_NO_CLOCKS_OK`.

---

#### **Input Normalization & Validation Layer — Done**

Notes. IDs normalize via declared alias ledgers when enabled (otherwise reject). `viewer_prefs` requires `top_category ∈ Magic-10` and `weights` contains all ten Magic-10 keys with integer `0..100` (no floats). Zero-weight rule is enforced downstream by the sampler/ranker (HDE-Mechanics Guide §11, titles-only). Normalized forms are re-serialized to canonical JSON (UTF-8/no BOM, ASCII-sorted keys, compact, one LF; arrays-as-sets deduped & ASCII-sorted) and are byte-identical for `(A,B)` vs `(B,A)`.

**Evidence (titles/paths only)**

* Success parity (CLI vs service): `tests/test_emitter/test_emitter_determinism.py`

* Invalid shapes/ids: service-side typed error tests (invalid\_prefs, invalid\_json)

* Normalization snapshots & canonical-compare logs

**Acceptance (titles-only)**  
 `UNKNOWN_IDS_FAIL_CLOSED_OK`, `ALIAS_NORMALIZATION_OK` (when enabled), `PREFS_KEYSET_10_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`.

---

#### **Compatibility Engine (pair) — Done**

Scope. Compute per-category score (0..100) → map to band (inclusive-high, e.g., 24/49/74/100) via `round_half_up`; select `personal_key`/`shared_key`; emit ten categories in frozen Magic-10 order (HDE-Schemas & Artifacts §2.6; HDE-Math-Spec §5.1, titles-only). Per-channel semantics: treat each channel as a canonical `NN-NN` edge (min-first, zero-padded) and record compromise direction \+ gate; Integration `{10, 20, 34, 57}` channels are independent and must be validated for AB↔BA parity (HDE-Mechanics Guide §7.2, titles-only). Inputs: `a`, `b` each ID or full person payload (HDE-CLI-API-Vendor-Ref Reader schema); do not mix for the same party (`invalid_json`).

**Evidence (titles/paths only)**

* `artifacts/narratives/key_table_10x2.snapshot.json` — 10×2 narrative key table

* `artifacts/compat/identity_hash.txt` — sha256 of LF-terminated compat body

* AB↔BA parity logs, including 20-34 vs 20-57 (Integration) pairs

**Acceptance (titles-only)**  
 `JSON_CANONICAL_CHECK_OK`, `AB_BA_PARITY_OK` (including Integration cases), `TWO_RUN_IDENTITY_OK`.

---

### **Not done**

#### **Band Thresholds & Tuning (admin) — Not done**

Status (Audit v1 — 2025-11-17): Not done. Missing tokens: `BAND_EDGE_GOLDENS_OK`, `M10_MAPS_OK`, `RELEASE_ID_RECOMPUTE_OK`. No edge fixtures/diffs/identity hash artifacts indexed.

**Tasks**

* Pin inclusive-high policy; add edge-case fixtures at 24/49/74/100 per preset (with \+1 transitions).

* Route numeric thresholds to the constants pack (HDE-Math-Spec / HDE-Schemas & Artifacts) and keep public output numeric-free.

* Capture compact diffs per change and compute `identity_hash` over the LF-terminated compat body for each tuning run.

**Acceptance (titles-only)**  
 `BAND_EDGE_GOLDENS_OK`, `M10_MAPS_OK`, `RELEASE_ID_RECOMPUTE_OK`.

**Evidence (titles/paths only)**

* `artifacts/thresholds/*.json`

* `audit/gates/bands/edges.snapshot.json`

* `audit/gates/bands/edges.diff.json`

* `artifacts/thresholds/identity_hash.txt`

**Indexing**  
 Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs).

---

#### **Category Framework (internal) — Not done (Notes: SoT: canon)**

Status (Audit v1 — 2025-11-17): Not done. Missing tokens: `CATEGORY_FRAMEWORK_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`; Magic-10 key table & compat parity evidence absent.

**Tasks**

* Implement per-category calculators and precedence hooks; use total-order utilities (§5) for any ordered emission.

* Enforce frozen Magic-10 order at all emission points; enforce AB↔BA and two-run identity.

* Integrate per-channel mechanics (treat channels as canonical `NN-NN`; compromise direction \+ gate; circuit is channel-scoped; optional bridge/timing analytics for internal use).

**Acceptance (titles-only)**  
 `CATEGORY_FRAMEWORK_OK`, `JSON_CANONICAL_CHECK_OK`, `AB_BA_PARITY_OK` (category layer), `TWO_RUN_IDENTITY_OK`.

**Evidence (titles/paths only)**

* `artifacts/category/calculators.snapshot.json`

* `artifacts/category/abba_identity.bytes`

* canonical-compare logs

**Indexing**  
 Update `docs/evidence/INDEX.json` and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; path-proofs).

## **Phase III — Separation (Public shape, identity, guardrails)**

### **Completed**

#### **Persistence Layer — Done**

**Notes (SoT)**  
 Persist public results and provenance with **canonical bytes** and a stable link to `release_id` (no partial payload writes). Writer surfaces are `Cache-Control: no-store`; DDL/grants are kept current. Integrity checks verify the **stored public body equals emitter output** (byte-for-byte).

**Acceptance (titles-only)**  
 Idempotent write path; canonical byte-compare vs emitter output; grants/DDL artifacts current; no secrets/PII in logs.

**Evidence (titles/paths only)**

* `artifacts/db/ddl_applied.sql`

* `artifacts/db/grants.txt`

* `artifacts/identity/service_identity.json`

* `artifacts/presenter/json_canon_compare.log`

**Indexing**  
 Update **Appendix D: Evidence Index** (`docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`) and the machine mirror `artifacts/evidence_index.jsonl` in the **same PR** (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; each record includes a `proof_anchor` to a co-located path\_proof).

---

### **Not done**

#### **Error Envelope & Token Set — Not done**

**Status (Audit v1 — 2025-11-17)**  
 Missing tokens: `CLI_STDERR_ONLY_ON_ERROR_OK`, `CLI_STDOUT_LF_OK`, `JSON_CANONICAL_CHECK_OK`; writers/errors header posture has not yet been proven on a Catalog success route. Evidence: —.

**Notes (SoT)**  
 Error body is typed, numeric-free JSON  
 `{"ok": false, "code": "…", "error": "…"}` — LF-terminated, serialized by the single presenter/emitter. No PII, no payload echoes, no SR/XR numerics.  
 **Transport.** `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, no `ETag`. Writers/errors are not Catalog-eligible; A7 success proofs stay bound to Catalog routes.

**Acceptance (titles-only)**  
 Typed schema gate; canonical re-serialization compare (UTF-8, no BOM, ASCII-sorted keys, compact, one LF); **CLI streams discipline** (`CLI_STDERR_ONLY_ON_ERROR_OK`, `CLI_STDOUT_LF_OK`); writers/errors headers match Governance (no-store, no `ETag`). Tokens live in HDE-Governance §2.0 (titles-only).

**Evidence (titles/paths only)**

* `tests/reader_v1/test_errors.py`

* `artifacts/cli/canonical/json_canon_compare.log`

* `tests/transport/headers/no_store_writers_errors.snap`

**Indexing**  
 Update Appendix D and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs). Writers/errors remain `Cache-Control: no-store` and emit typed, numeric-free JSON; not Catalog-eligible.

---

#### **Public Presenter / Emitter — Not done**

**Status (Audit — 2025-11-18)**  
 Reader↔CLI parity fails under rails-closed; for the same pair, Reader emitted Warm/alpha while CLI emitted Open/dev. Do **not** claim `CLI_READER_EMITTER_PARITY_OK`, `CLI_SHOWCOMPAT_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK` until the shared emitter and identity pins are aligned.

**Reason**  
 CLI parity gap: `showcompat` produced empty or non-matching output in some runs; Reader↔CLI byte identity is not universally satisfied; shared emitter path is specified but not fully proven.

**Tasks**

* Ensure Reader and CLI call the **same presenter/emitter symbol** (single allow-listed entrypoint).

* Prove **non-empty, LF-terminated canonical JSON** on `showcompat`.

* Enforce streams: success → stdout (one LF); errors → stderr.

* Re-prove AB↔BA and two-run identity for CLI parity flows.

* Add grep-guard on public paths and an import-graph symbol proof of the shared emitter.

**Acceptance (titles-only)**  
 Reader↔CLI byte identity; non-empty canonical JSON; AB↔BA parity; two-run identity; canonical JSON checks; stdout LF; preimage recompute:  
 `CLI_READER_EMITTER_PARITY_OK`, `CLI_SHOWCOMPAT_CANON_OK`, `CLI_STDOUT_LF_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`.

**Evidence (titles/paths only)**

* `artifacts/presenter/preimage_recompute.log`

* `artifacts/presenter/reader_cli_parity.bytes`

* `artifacts/cli/guards/serializer_grep_guard.log`

* `artifacts/cli/guards/emitter_symbol_proof.txt`

**Routing (titles-only)**  
 HDE-CLI-API-Vendor-Ref (public bytes, preimage flow); HDE-Schemas & Artifacts §4 (canonical JSON); HDE-Governance §2.0 (tokens).

**Indexing**  
 Update Appendix D and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs).

---

#### **Internal Ops Surface `/internal/version` — Not done**

*(Covers the Identity & Provenance Module \+ Internal Meta Surface for `/internal/version`.)*

**Status (Audit v1 — 2025-11-17)**  
 Missing tokens: `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK`; headers/body proofs incomplete. Evidence: —.

**Reason**  
 Earlier builds lacked stable captured evidence for HEAD=200 parity (including `Content-Type`), conditional-ignore behavior (never 304), and no-store/no-ETag posture, even though Mechanics and Governance define the required ops surface.

**Tasks**

* Implement HEAD parity and conditional-ignore for `/internal/version`.

* Capture GET/HEAD/conditional transcripts.

* Keep `Cache-Control: no-store`, no `ETag`.

* Re-index proofs with human↔machine parity in the same PR.

**Acceptance (tokens)**  
 `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, `INTVER_CONDITIONALS_IGNORED_OK`, `INTVER_200_NO_ETAG_OK` (see HDE-Governance §2.0).

**Evidence (titles/paths only)**

* `artifacts/ops/internal_version/headers_get.txt`

* `artifacts/ops/internal_version/headers_head.txt`

* `artifacts/ops/internal_version/body_get.json`

* `artifacts/ops/internal_version/body_get.sha256`

* `artifacts/ops/internal_version/cond_if_none_match_headers.txt`

* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

* `artifacts/ops/internal_version/two_run_identity.log`

**Related artifacts**

* `artifacts/math/freeze_pack_manifest.json`

* `artifacts/math/release_id.txt`

* `artifacts/math/release_id_recompute.log`

* `artifacts/identity/emitter_sha256.txt`

**Routing (titles-only)**  
 HDE-Schemas & Artifacts §6 (manifest/`release_id`); HDE-Governance (Doc-Delta/Index); HDE-CLI-API-Vendor-Ref (identity exposure).

**Indexing**  
 Update Appendix D and mirror `artifacts/evidence_index.jsonl` in the same PR (records-only; with path-proofs).

---

#### **Cross-phase coupling (titles-only)**

* **Canonical JSON & pack/manifest:** HDE-Schemas & Artifacts.

* **Public Reader/CLI bytes & preimage:** HDE-CLI-API-Vendor-Ref.

* **A7 transport policy & Evidence Index discipline:** HDE-Governance.

---

## **Phase IV — Conjunction (Surfaces and tools meet the core)**

### **Completed**

#### **Dev HTTP Harness (single home) — Done**

**Notes**  
 Single home for local/QA validation; `Cache-Control: no-store` by default; never exposes SR/XR numerics; runs under `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Supplemental only: authoritative A7 proofs live on the Catalog JSON success route.

**Acceptance (titles only)**  
 Harness parity with CLI; AB↔BA on compat; canonicalization checks; evidence in `audit/gates/*`.

**Evidence (titles/paths only)**

* `tests/harness/test_end_to_end.py`

* `audit/gates/parity/*.bytes`

* `audit/gates/canonical_json/*.log`

**Indexing**  
 Update the Human Index (`docs/evidence/INDEX.json`) and the machine mirror (`artifacts/evidence_index.jsonl`) in the same PR (records-only; with path-proofs). PF-Canon-HDE-Schemas & Artifacts §8.6 is the single home for the entry list.

---

### **Not done**

#### **Compat Surface (internal) — Not done**

**Status (Audit v1 — 2025-11-17)**  
 Not done. Missing tokens: `CATEGORY_FRAMEWORK_OK`, `AB_BA_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`; no Magic-10 key table or compat parity logs.

**Notes**  
 Internal endpoint for pair-compat emission and QA; uses the same presenter/emitter; never exposes SR/XR numerics on Reader; any CLI-only diagnostic sidecar is flag-guarded.

**Acceptance (titles only)**  
 Canonical LF-terminated output; AB↔BA parity on full body (include Integration channel cases such as `20–34` vs `20–57`); `identity_hash` capture.

**Evidence (titles/paths only)**

* `artifacts/compat/identity_hash.txt`

* `tests/compat/test_abba_parity.py`

**Routing (titles only)**  
 HDE-CLI-API-Vendor-Ref; HDE-Math-Spec (resonance posture); HDE-Governance (no diagnostics on Reader 200).

---

#### **CLI Serializer Coupling — Not done**

**Status (Audit v1 — 2025-11-17)**  
 Not done. Missing tokens: `CLI_READER_EMITTER_PARITY_OK`, `CLI_NO_ALT_JSON_OK`, `CLI_SHOWCOMPAT_CANON_OK`, `TWO_RUN_IDENTITY_OK`; grep/symbol proofs not recorded.

**Notes**  
 Reader and CLI are specified to share one emitter; CLI stdout must be byte-identical to the Reader body; no ad-hoc serializers on public paths (guarded by grep).

**Acceptance (titles only)**  
 `PREIMAGE_RECOMPUTE_OK`, `CLI_READER_EMITTER_PARITY_OK`, `CLI_SHOWCOMPAT_CANON_OK`, `CLI_NO_ALT_JSON_OK`, `TWO_RUN_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK`.

**Evidence (titles/paths only)**

* `tests/test_emitter_determinism.py`

* `artifacts/cli/guards/serializer_grep_guard.log`

* `artifacts/cli/guards/emitter_symbol_proof.txt`

* `artifacts/cli/reader_cli_parity.bytes`

**Indexing**  
 Update the Human Index and the machine mirror in the same PR (records-only; with path-proofs). PF-Canon-HDE-Schemas & Artifacts §8.6 lists entries.

---

#### **CLI Conformance — Not done**

**Status (Audit v1 — 2025-11-17)**  
 Not done. No CLI conformance artifacts recorded for `ab.json` / `ba.json` / `summary.json`.

**Goal**  
 `showcompat` present and wired; CLI outputs LF-terminated canonical JSON; Reader↔CLI parity; AB↔BA & two-run identity; installation and help flows exit cleanly.

**Acceptance (titles only)**

* `CLI_PYPROJECT_ENTRYPOINT_OK`

* `CLI_MODULE_RUN_OK`

* `CLI_INSTALL_OK`

* `CLI_HELP_EXIT_0_OK`

* `CLI_HELP_STDOUT_OK`

* `CLI_SHOWCOMPAT_PRESENT`

* `CLI_READER_EMITTER_PARITY_OK`

* `CLI_SHOWCOMPAT_CANON_OK`

* `CLI_AB_BA_PARITY_OK`

* `CLI_TWO_RUN_IDENTITY_OK`

**Evidence (titles/paths only)**

* `artifacts/cli/ab.json`

* `artifacts/cli/ba.json` (byte-identical to `ab.json`)

* `artifacts/cli/summary.json`

**Indexing**  
 Index the three artifacts in both Human Index and machine mirror (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present) in the same PR.

---

#### **Reader Surface (API) — Not done (was Partial)**

**Status (Audit v1 — 2025-11-17)**  
 Not done. Missing tokens: `ENDPOINTS_CATALOG_OK`, `ENDPOINTS_CATALOG_ENV_GATE_OK`, `A7_GET_QUOTED_ETAG_OK`, `A7_HEAD_PARITY_OK`, `A7_304_OMITS_CT_CL_OK`, `A7_VARY_AUTH_AE_OK`, `A7_ENCODING_INVARIANCE_OK`, `READER_200_CTYPE_JSON_UTF8_OK`. Catalog \+ GET/HEAD/304/encoding proofs are absent.

**Notes (SoT)**  
 Public success body \= six keys  
 `{reader_version, eligible, categories, meta, release_id, idempotence_hash}`  
 via the single presenter/emitter as canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; one LF; arrays-as-sets deduped). All checks run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Transport (A7)**  
 Must prove on a Catalog JSON success route:

* Strong quoted ETag.

* `Vary: Authorization, Accept-Encoding`.

* HEAD 200 parity with `Content-Type == GET` and `Content-Length == len(identity 200 body)`.

* 304 only after a prior 200; omit both `Content-Type` and `Content-Length`.

* POST non-conditional.

* Writers/errors `Cache-Control: no-store`, no `ETag`.

* Encoding invariance: ETag and effective `Content-Length` stable across accepted encodings.

**Acceptance (titles only)**  
 Schema gate; Reader↔CLI parity; AB↔BA parity; two-run identity; A7 matrix; canonical re-serialization; plus:

* `ENDPOINTS_CATALOG_OK`

* `ENDPOINTS_CATALOG_ENV_GATE_OK`

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

* `READER_200_CTYPE_JSON_UTF8_OK`

**Evidence (titles/paths only)**

* `docs/ENDPOINTS_CATALOG.json`

* `docs/ENDPOINTS_CATALOG.json.sha256`

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_encoding_invariance.txt`

* `artifacts/proofs/endpoints_env_gate_proof.log`

* `artifacts/proofs/success_writers_errors.txt`

*(Capture on a Catalog route only; `/internal/version` is excluded.)*

**Tasks (add)**

* Expose one JSON success route (six-key envelope via shared presenter/emitter).

* Add Endpoint Catalog entry (internal-only; env-gated; non-prod unreachable in prod).

* Capture full A7 proofs on that Catalog route: GET/HEAD/304; encoding invariance; env-gate proof.

**Indexing**  
 Index Catalog \+ A7 artifacts in both Human Index and mirror in the same PR.

---

#### **Caching & Transport Wiring (Reader) — Not done (was Partial)**

**Status (Audit v1 — 2025-11-17)**  
 Not done. A7 matrix not proven on a cataloged JSON success route; encoding invariance and env-gate evidence missing.

**Notes**  
 Enforce the A7 matrix on the same Catalog JSON success route:

* ETag on 200\.

* 304 omits `Content-Type` and `Content-Length`; no body.

* HEAD 200 parity.

* POST non-conditional.

* Writers/errors `Cache-Control: no-store`.

* ETag over canonical LF-terminated body.

* Encoding invariance across accepted `Accept-Encoding` values.

**Tasks (add)**

* Tie A7 proofs explicitly to the Catalog JSON success route.

* Re-run and capture `success_get`, `success_head`, `success_304`.

* Prove encoding invariance.

* Add env-gate proof if missing.

**Acceptance (titles only)**

* `A7_GET_QUOTED_ETAG_OK`

* `A7_HEAD_PARITY_OK`

* `A7_304_OMITS_CT_CL_OK`

* `A7_VARY_AUTH_AE_OK`

* `A7_ENCODING_INVARIANCE_OK`

* `A7_TRANSPORT_PROOF_OK`

**Evidence (titles/paths only)**

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_writers_errors.txt`

* `artifacts/proofs/success_encoding_invariance.txt`

* `artifacts/proofs/endpoints_env_gate_proof.log`

**Indexing**  
 Update Human Index and mirror in the same PR (records-only, with path-proofs).

---

#### **CLI Tooling (showcompat, sample) — Not done (was In progress)**

**Status (Audit v1 — 2025-11-17)**  
 Not done. CLI parity/determinism harness exists as a plan; acceptance tokens not yet proven or indexed.

**Notes**

* `showcompat`: six-key LF-terminated body via shared emitter; v1 when eligible: exactly one `{id: "harmony", band}`. Merge-blocking until parity/determinism tokens pass.

* `sample` (dev-only): IDs only with deterministic order (echo seed in `meta` when provided); enforces diversity window/bounds/recent constraints; one LF.

**Acceptance (extend with CLI conformance; titles only)**

* **showcompat:** `CLI_READER_EMITTER_PARITY_OK`, `PREIMAGE_RECOMPUTE_OK`, `JSON_CANONICAL_CHECK_OK`, `CLI_STDOUT_LF_OK`, `CLI_AB_BA_PARITY_OK`, `CLI_TWO_RUN_IDENTITY_OK`.

* **sample:** deterministic IDs order; `COMPOSITE_ABBA_IDENTITY_OK`, `TWO_RUN_IDENTITY_OK`; diversity constraints satisfied.

* **CLI conformance:** `CLI_PYPROJECT_ENTRYPOINT_OK`, `CLI_MODULE_RUN_OK`, `CLI_INSTALL_OK`, `CLI_HELP_EXIT_0_OK`, `CLI_HELP_STDOUT_OK`, `CLI_STDERR_ONLY_ON_ERROR_OK`, plus parity harness tokens `CLI_SHOWCOMPAT_PRESENT`, `CLI_SHOWCOMPAT_CANON_OK`.

**Evidence (titles/paths only)**

* `artifacts/cli/ab.json` — canonical output for AB inputs (LF-terminated)

* `artifacts/cli/ba.json` — canonical output for BA inputs (byte-identical to AB)

* `artifacts/cli/summary.json` — canonical JSON with attempted commands, sha256 of ab/ba, and `ab_ba_equal: true`

**Indexing**  
 Index these artifacts in Human Index and mirror (records-only canonical JSONL; one LF; unknown-key reject; `proof_anchor` present) in the same PR.

---

#### **Writer Surfaces (API) — Not done**

**Tasks**

* Define typed success and error envelopes (numeric-free) and A7 posture (writers `Cache-Control: no-store`, never 304).

* Ensure idempotent write path; canonicalize body before persist; record `release_id`; run byte-equality checks against emitter output.

* Gate with admin capability; include rate limiting, authZ, and audit per Governance.

**Evidence (titles/paths only)**  
 Write/readback byte parity; DDL updates; ops logs; Evidence Index entries.

**Acceptance (titles only)**  
 All A7 rows pass; canonical byte identity; Evidence Index updated in the same PR.

**Routing (titles-only)**  
 HDE-Governance (writers, A7), HDE-CLI-API-Vendor-Ref (request/validation), HDE-Schemas & Artifacts §4 (canonical JSON).

---

### **Global discipline**

All surfaces honor the single-emitter, canonical JSON rules (UTF-8, no BOM; ASCII-sorted keys; compact; one LF; arrays-as-sets deduped) and run under `LC_ALL=C`, `LANG=C`, `TZ=UTC`. Index updates are mandatory: update the Human Index (`docs/evidence/INDEX.json` and `docs/evidence/INDEX.sha256`) and the machine mirror (`artifacts/evidence_index.jsonl`) in the same PR that adds or changes artifacts. PF-Canon-HDE-Schemas & Artifacts §8.6 is the single home for the entries list.

## **Phase V — Fermentation (Narratives & external bridges)**

Overall status: **Partial** (semantics and routes are specified in canon, but none of the items in this phase are yet fully accepted as Done; all remain **Not done** until tokens pass and evidence is indexed in Human Index and Machine Mirror).

---

### **SAFE rails & provider gate — Not done**

**Status (Audit v1 — 2025-11-17).** Not done. Missing tokens: `SAFE_RAILS_CLOSED_OK`, `SAFE_RAILS_OPEN_OK`, `SAFE_LOG_REDACTION_OK`, `SAFE_RETRY_BACKOFF_OK`, `SAFE_429_TYPED_REFUSAL_OK`. No SAFE-rails evidence captured.

**Notes (SoT)**  
 Rails are closed by default; vendor HTTP is allowed only when both gates are open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`).

Under closed rails:

* Refusal path is a typed, numeric-free JSON body, LF-terminated.

* No secrets in logs.

* No `ETag`.

* No `Vary` on error/ops routes.

* No response compression on refusal.

Request shapes may be computed for diagnostics under closed rails, but **no outbound I/O** is permitted.

**Routing (titles-only)**  
 HDE-Governance (rails policy & tokens) · HDE-CLI-API-Vendor-Ref (vendor bytes) · HDE-Mechanics Guide (§7.1/§7.3).

**Tasks to finish**

* **Refusal posture (closed rails)**

  * Prove: no sockets, DNS lookups, or HTTP calls when rails are closed.

  * Verify a typed refusal envelope (for example `PROVIDER_DISABLED`) with numeric-free JSON and LF termination.

  * Verify keys-only logging (header names, route, status, duration, `idempotence_hash`, `release_id`) and that all secret values are redacted (for example `HD-Api-Key: REDACTED`).

* **Open posture (integration) — pin policy before live tests**

  * Timeouts: `timeout_profile ∈ {small, default, long}` → `(connect_timeout_ms, read_timeout_ms, total_timeout_ms)` from closed integer sets.

  * Retries: `max_attempts ∈ {0,1,2,3}` (includes initial attempt); `retryable = {network_error, 5xx}`; do **not** retry 429 or any other 4xx.

  * Backoff: `{none, fixed, exponential}` with closed integer parameters; no jitter; accumulated delay must not exceed `total_timeout_ms`.

  * 429 handling: on HTTP 429, produce typed `PROVIDER_RATE_LIMITED`; if `Retry-After` is valid (delta-seconds or HTTP-date), compute `retry_after_ms ≥ 0`; on invalid/unsupported/overflow, omit `retry_after_ms`. Do not treat 429 as a success path in this epic.

* **Observability**

  * Ensure counters/timers for success vs failure classes (`network_error`, 4xx, 5xx, 429).

  * Ensure labels are bounded (for example route, outcome, rails\_state, timeout\_profile).

  * Verify logs never include payload bodies or secret header values.

**Acceptance (titles-only)**

* Closed rails: refusal proof present (`ci/jobs/rails_closed_refusal.yml`), request-shaping snapshot, and keys-only redaction verified.

* Open rails: success path emits canonical JSON envelopes; retry behavior follows the pinned policy; 429 handling is deterministic (`PROVIDER_RATE_LIMITED` with optional `retry_after_ms` when valid); total time budget is enforced; AB↔BA coherence and two-run identity remain satisfied.

**Evidence (titles/paths only)**

* `ci/jobs/rails_closed_refusal.yml` — closed-rails refusal proof harness

* `ci/jobs/rails_open_conformance.yml` — success / retry / 429 exercise

* `ci/jobs/logs_keys_only_redaction.yml` — log redaction check

* `artifacts/vendor/policies_pinned.md` — selected timeout/retry/backoff/429 parameters

* `artifacts/vendor/retry_after_parse.log` — Retry-After parse/normalization traces

**Indexing**

Update, in the same PR:

* `docs/evidence/INDEX.json` (Human Index)

* `docs/evidence/INDEX.sha256` (hash sentinel)

* `artifacts/evidence_index.jsonl` (Machine Mirror)

Mirror must be records-only canonical JSONL (UTF-8; sorted keys; compact; exactly one LF), reject unknown keys, use fixed field order, and include a `proof_anchor` to a co-located `path_proof.txt`. PF12 §8.6 is the single home for the evidence listing; PF12 Appendix C defines record types.

---

### **Narrative Selection Router (keys only) — Not done**

**Notes**

* The router selects narrative keys only; it does **not** generate text.

* Inputs: `(category, band, perspective ∈ {personal, shared}, viewer_top, flags)`.

* Output: `{personal_key, shared_key}`.

* Deterministic: no randomization, no time-based behavior.

* No fallbacks: missing mapping ⇒ `missing_narrative_key`.

* CLI and Reader must remain in parity via the shared presenter.

**Routing (titles-only)**  
 HDE-Mechanics Guide (§7 — Category Framework) · HDE-Math-Spec (banding & category semantics).

**Tasks**

* Implement a deterministic router:

  * Freeze argument schema.

  * Use explicit total-order utilities (§5) for any “top N” or tie-break logic.

  * Eliminate clocks, randomness, or external I/O from routing.

* Add unit tests:

  * For each `(category, band, perspective)` case, verify:

    * Same inputs → same keys (two-run identity).

    * AB/BA coherence where applicable (for example A–B vs B–A).

**Acceptance (titles-only)**

* Resolver returns keys or `missing_narrative_key`.

* Outputs are canonical JSON (UTF-8, sorted keys, compact, one LF).

* Reader’s public surface remains bands-only; keys map to content by title.

* CLI and Reader use the same keys for the same inputs (parity via shared presenter).

**Evidence (titles/paths only)**

* `audit/gates/narratives/keys_10x2.table.json` — router output table (canonical JSON; one LF)

* `tests/narratives/test_router.py` — unit tests and edge cases

**Indexing**

Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR; include `proof_anchor` path-proofs for router artifacts. PF12 §8.6 and Appendix C govern the listing and record types.

---

### **Narrative Key Registry & Manifests — Not done**

**Notes**

* Versioned, diffable manifests are the single source of truth for narrative keys.

* Exactly one key per `(category, band, perspective)`.

* Registry supports closure checks (no missing or duplicate keys).

* Pack identity is `pack_sha = sha256(canonical manifest bytes)`; packs are stored under `/narratives/<pack_sha>/…`.

* Exporter and loader behavior is owned by HDE-Mechanics and the Narratives Guide (titles-only).

**Tasks**

* Define the manifest shape:

  * Canonical JSON (UTF-8, sorted keys, compact, one LF).

  * Fields sufficient to capture category, band, perspective, language/variant, and key.

* Implement a closure validator:

  * Fail if any required `(category, band, perspective)` is missing or duplicated.

* Build diff tooling:

  * Produce a concise diff artifact for manifest changes.

* Wire Doc-Delta policy:

  * Any registry change must be accompanied by a Doc-Delta entry and evidence updates in the same PR.

**Acceptance (titles-only)**

* Manifests pass closure (no gaps/dupes).

* Diffs for manifest changes are present and readable.

* Doc-Delta entries exist for each registry change.

* ABBA / two-run identity remains unaffected.

* Pack identity is computed as `pack_sha` and matches the manifest bytes used to build `/narratives/<pack_sha>/…`.

**Evidence (titles/paths only)**

* `artifacts/narratives/registry/*.json` — manifests (canonical JSON; one LF)

* `audit/gates/narratives/registry.diff.json` — compact diff of manifest changes

* `docs/changes/DOC-DELTA-*.md` — change records (titles-only; no payload duplication)

**Indexing**

Update Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR; ensure `proof_anchor` path-proofs exist for each artifact directory. PF12 §8.6 and Appendix C remain the single homes for listing and record types.

---

### **Database Runtime Posture — Not done**

**Status (Audit v1 — 2025-11-17).** Not done. Missing tokens: `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`, `DB_CONN_ENV_OK`, `DB_BRIDGE_FALLBACK_OK`, `DEV_DB_BRIDGE_FALLBACK_OK`, `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`. Evidence: —.

**Tasks to implement (normative)**

* **Adapter façade only**  
   All DB posture/evidence scripts MUST call the DBAccess façade (provider-agnostic), never raw driver clients, to guarantee parity across TCP and HTTPS providers.

* **Runtime `search_path`**  
   Prove `hde, public` (unquoted, in that order) at runtime; capture a `check_schema` artifact.

* **Least-privilege grants**  
   Capture a grants snapshot for the runtime role; verify no extraneous DML/DDL privileges.

* **DDL fingerprint**  
   Capture normalized DDL and compute a SHA-256 fingerprint.

* **Dev fallback (adapter)**  
   In `APP_ENV=dev`, when `DATABASE_URL` is present but unusable, fallback to `DB_BRIDGE_URL` (HTTPS); record attempts and the selected source.

* **Bridge capability & provider parity**  
   Snapshot bridge capabilities (endpoints and grants) and demonstrate that queries against the bridge produce results identical to direct DB access on a canonical corpus.

* **Total failure (non-dev)**  
   In non-dev, use presence-order selection: `DATABASE_URL → DB_BRIDGE_URL → typed error`.  
   Never run proactive probes; on total failure, emit a deterministic, numeric-free error.

**Evidence (titles/paths only; governed paths; index human+machine in same PR)**

* `artifacts/db/ddl_fingerprint.json`

* `artifacts/db/grants.txt`

* `artifacts/db/check_schema.txt`

* `artifacts/runtime/env_connectivity.snapshot.json` (dev resolver snapshot — attempts/result/selected)

* `artifacts/db_bridge/adapter_selection.snapshot.json`

* `artifacts/db_bridge/caps.snapshot.json`

* `artifacts/db/provider_parity/*.json` (normalized parity results)

**Acceptance (titles-only)**

* DB posture & durability: `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`.

* Connectivity & errors: `DB_CONN_ENV_OK` (presence-order behavior; typed error on total failure).

* Bridge & fallback: `DB_BRIDGE_FALLBACK_OK`, `DEV_DB_BRIDGE_FALLBACK_OK`, `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`.

* Index/mirror/path-proofs: `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

**Indexing discipline (must)**

Update the Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and the Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR. Mirror must be records-only canonical JSONL (sorted keys; one LF; unknown-key reject; single mirror file) and each record must include a `proof_anchor` to a co-located `path_proof.txt`.

---

## **Phase VI — Distillation (Evidence & performance)**

Overall status: **Not done.** The harness and gates are specified in canon and in PF09, but pack/manifest, environment snapshot, and the integrated evidence harness are all still pending; PF09 Audit marked Pack/manifest and Environment snapshot tracks as **Not done**.

---

### **Gate scripts & evidence harness — Not done**

**Purpose**  
 One-button runners that exercise all critical mechanics and produce the full set of binary evidence artifacts in a deterministic, repeatable way.

**Determinism gates (must)**

* **Preimage recompute.** Strip `idempotence_hash`; re-serialize the five-key preimage as canonical JSON (UTF-8, no BOM; ASCII-sorted keys; compact; exactly one LF; arrays-as-sets deduped and ASCII-sorted; `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and compute `sha256(preimage_bytes)`. Result must equal the published `idempotence_hash`.

* **Reader↔CLI parity.** For a fixed corpus of pairs, run both Reader and CLI on the same inputs; byte-compare the emitted JSON envelopes. Outputs must be identical (single emitter, same canonical JSON).

* **AB↔BA & two-run identity.** For each Integration pair (for example `20–34` vs `34–20`, `20–57` vs `57–20`) run the harness twice: A↔B and B↔A produce expected mirrored narratives and banding (AB/BA coherence); a second full run produces byte-identical outputs (two-run determinism).

* **Canonical JSON compare.** Re-emit a sample of envelopes and verify that on-disk artifacts and over-the-wire responses are canonical JSON.

**CI rails posture (must)**

* CI pipelines run with rails CLOSED by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).

* If any job opens rails (for example to call a live vendor or bridge), that job must:

  * Use closed-domain timeouts/retries/backoff parameters, and

  * Produce governed evidence and update both the Human Index and Machine Mirror in the same PR.

**Transport (A7) gates (must) — run on a Catalog success route**

* Success (200): `Content-Type: application/json; charset=utf-8`; strong, quoted `ETag` over LF-terminated body; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.

* HEAD: status 200; no body; validators match 200; `Content-Type == GET`; `Content-Length == len(identity 200 body)`.

* 304 (not modified): only after a successful 200 on the same route; no body; omit `Content-Type` and `Content-Length`; validators match cached 200\.

* POST: non-conditional; never returns 304\.

* Writers/errors: all writer and error routes send `Cache-Control: no-store`; no `ETag` on error responses; errors use `Content-Type: application/json; charset=utf-8`.

* Encoding invariance: for a fixed canonical LF-terminated body, `ETag` and effective `Content-Length` are stable across accepted encodings (`identity`, `gzip`, `br`).

* Env-gating proof: capture headers-only proof that non-prod Catalog entries are unreachable when running with `APP_ENV=prod`.

**Rails gates (must)**

* **Closed rails.** Prove no outbound network I/O under closed rails; refusal envelopes are typed, numeric-free JSON; logs are keys-only.

* **Open rails (pinned).** With policy pins in place (timeouts, retries from closed domains; no jitter), show:

  * Retry/backoff behavior matches the pinned profile.

  * 429 responses produce typed `PROVIDER_RATE_LIMITED` with `retry_after_ms` only when `Retry-After` is valid.

  * Determinism and AB/BA parity remain intact.

**Acceptance (titles-only)**

* **Determinism & parity**:  
   `PREIMAGE_RECOMPUTE_OK · CLI_READER_EMITTER_PARITY_OK · CLI_AB_BA_PARITY_OK · TWO_RUN_IDENTITY_OK · JSON_CANONICAL_CHECK_OK`

* **A7 & Catalog**:  
   `A7_GET_REQUEST_HEADERS_OK · A7_HEAD_PARITY_OK · A7_304_HEADERS_OK · A7_VARY_HEADERS_OK · A7_ENCODING_INVARIANCE_OK · A7_TRANSPORT_PROOF_OK · ENDPOINTS_CATALOG_INTERNAL_OK · ENDPOINTS_CATALOG_ENV_GATE_PROOF_OK`

* **Env / rails / evidence**:  
   `ENV_RAILS_POLICY_OK · ENV_LC_ALL_C_OK · EVIDENCE_INDEX_UPDATED_OK · MACHINE_MIRROR_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · CI_CHECK_MIRROR_SCHEMA_OK · CI_CHECK_FINAL_LF_OK · EVIDENCE_PATHS_VALIDATED_OK`

* **DB posture & bodygraph mechanics (if verified here)**:  
   `DB_RUNTIME_SEARCH_PATH_OK · DB_ROLE_OK · DB_SCHEMA_FINGERPRINT_OK · DB_CONN_ENV_OK · BG_SOURCE_SELECTION_OK · BG_DEV_DB_BRIDGE_FALLBACK_OK · BG_VENDOR_DISABLED_OK · BG_SOURCE_INVARIANCE_OK · BG_TTL_SWR_OK · BG_RATE_LIMIT_POLICY_OK · BG_CIRCUIT_BREAKER_OK`

**Evidence (titles/paths only)**

* Determinism / parity: `audit/gates/parity/reader_cli/ab.json`, `.../ba.json`, `.../summary.json`, `audit/gates/determinism/abba.bytes`, `.../tworun_identity.sha256`, `audit/gates/canonical_json/json_canon_compare.log`

* Transport (Catalog success route): `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/success_get.txt`, `.../success_head.txt`, `.../success_304.txt`, `.../success_writers_errors.txt`, `.../encoding_invariance.txt`, `.../endpoints_env_gate_proof.log`

* Aux (EPIC-010 — headers-only): `tests/transport/headers/aux_text_200.snap`, `.../aux_suppression_200.snap`

* Rails: `ci/jobs/rails_closed_refusal.yml`, `.../rails_open_conformance.yml`, `.../logs_keys_only_redaction.yml`

* Database posture: `artifacts/db/check_schema.txt`, `.../grants.txt`, `.../ddl_fingerprint.json`, `artifacts/runtime/env_matrix.snapshot.json`, `.../env_connectivity.snapshot.json`, optional `artifacts/prod/latency_sample.jsonl`

* BodyGraph proofs: `artifacts/bodygraph/source_selection.snapshot.json`, `.../source_invariance/ab.json`, `.../ba.json`, `.../summary.json`, `.../refresh_policy.snapshot.json`, `.../metrics.snapshot.json`, `.../keys_only.logs.sample`

* Sanity pipeline transcript: `artifacts/proofs/sanity_pipeline.transcript.log`

**Indexing**

Every artifact above must be indexed in the Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and in the Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR. Mirror is records-only canonical JSONL (UTF-8; ASCII-sorted keys; compact; exactly one LF), rejects unknown keys, uses fixed field order, and each record includes a `proof_anchor` to a co-located `path_proof.txt`. PF12 §8.6 remains the single home for the evidence listing and schema.

---

### **Pack/manifest & release identity — Not done**

**Status (Audit v1 — 2025-11-17).** Not done. Manifest freeze and `release_id` recompute not run; no pack identity artifacts indexed.

**Goal**  
 `release_id = sha256(canonical_bytes("catalog/manifest.json"))`; manifest canonical; no self-listing; checksums audit passes.

**Rules**

* `catalog/manifest.json` is canonical JSON (UTF-8, no BOM, ASCII-sorted keys, compact, exactly one LF).

* Manifest contains no self-reference and no duplicate paths; paths are ASCII-sorted.

**Acceptance (titles-only)**

* `RELEASE_ID_RECOMPUTE_OK`

* `MANIFEST_SHA256_HEX64_OK`

* `PACK_MANIFEST_NO_SELF_LISTING_OK`

* `MANIFEST_PATH_ASCII_SORT_OK`

* `MANIFEST_NO_DUP_PATHS_OK`

* `JSON_CANONICAL_CHECK_OK`

**Evidence (titles/paths only)**

* `artifacts/math/freeze_pack_manifest.json`

* `artifacts/math/release_id.txt`

* `artifacts/math/release_id_recompute.log`

* `artifacts/math/checksums_audit.log`

**Indexing**

Index manifest and release identity artifacts in Human Index and Machine Mirror in the same PR; each mirror record includes a `proof_anchor` path-proof. PF12 §8.6 remains the single home for the listing and record types.

---

### **Environment snapshot (singleton) & observability — Not done**

**Status (Audit v1 — 2025-11-17).** Not done. Env matrix, metrics, and keys-only log samples missing.

#### **Environment snapshot (singleton, v3)**

**Artifact & path**  
 `artifacts/runtime/env_matrix.snapshot.json` — one file per repo (singleton).

**Schema (v3; unknown-key rejection)**

Canonical JSON per PF12 §4 (UTF-8; sorted keys; compact; exactly one LF). Minimum shape:

`{`

  `"schema_version": 3,`

  `"default_rails": {`

    `"dev":   {"SAFE_MODE": 0, "ALLOW_NETWORK": 1},`

    `"stage": {"SAFE_MODE": 0, "ALLOW_NETWORK": 1},`

    `"prod":  {"SAFE_MODE": 1, "ALLOW_NETWORK": 0},`

    `"CI":    {"SAFE_MODE": 1, "ALLOW_NETWORK": 0}`

  `},`

  `"determinism_pins": {"LC_ALL": "C", "LANG": "C", "TZ": "UTC"},`

  `"presence": {`

    `"DATABASE_URL": {"present": true},`

    `"DB_BRIDGE_URL": {"present": false},`

    `"db_allow_bridge_in_prod": {"present": false}`

  `},`

  `"notes": []`

`}`

**Rules**

* Open in write mode (overwrite, never append).

* Exactly one JSON object; final LF; no auxiliary content.

* Reject unknown keys; `schema_version` must be 3\.

  #### **Observability — logs & metrics**

**Logs**

* Keys-only; no raw birth data.

* No vendor payloads.

* No secrets; redact any key-like values.

* Provide a sanitized sample at `artifacts/bodygraph/keys_only.logs.sample`.

**Metrics**

* Counters: refresh successes/failures; rate-limit hits; circuit-breaker openings.

* Histograms: `engine.latency_ms`, `presenter.latency_ms`.

* Gauges: for example staleness %.

* Capture metrics at `artifacts/bodygraph/metrics.snapshot.json` (canonical JSON; single LF).

**Acceptance (titles-only)**

* `ENV_SNAPSHOT_SINGLETON_OK`

* `ENV_SNAPSHOT_SCHEMA_V3_OK`

* `ENV_PINS_PRESENT_OK`

* `LOGS_KEYS_ONLY_SAMPLE_OK`

* `OBS_KEYS_ONLY_OK`

* `BG_PRIVACY_OK`

* `BG_METRICS_OK`

**Evidence (titles/paths only)**

* `artifacts/runtime/env_matrix.snapshot.json`

* `artifacts/bodygraph/keys_only.logs.sample`

* `artifacts/bodygraph/metrics.snapshot.json`

**Indexing**

Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` in the same PR; include `proof_anchor` path-proofs for env snapshot, logs, and metrics artifacts.

---

### **Performance & Load Harness — Not done**

**Purpose**  
 Non-PII, deterministic performance suite with stable labels and reproducible scenarios.

**Tasks**

* Profiles: small / default / long; warm vs cold; bounded concurrency; rails closed by default.

* Metrics: percentiles and histograms (for example `engine.latency_ms`, `presenter.latency_ms`); counters by outcome; bounded labels (`route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`).

* SLO probes: steady-state latency (p95/p99 bands); budget for canonicalization and preimage cost; prove parity under realistic load.

**Acceptance**

* Runs are repeatable (two-run identity for metrics).

* No payloads/secrets in logs.

* Parity is maintained with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

**Evidence (titles/paths only)**

* `artifacts/bench/bench_report_{release_id}.json`

* `artifacts/bench/parity_identity_{release_id}.log`

* `artifacts/bench/transport_headers_{release_id}/…`

* `ci/jobs/bench_math_transport.yml`

* `ci/jobs/bench_vendor_open.yml`

* `ci/jobs/slo_verify.yml`

**Indexing**

Update the Human Index and Machine Mirror in the same PR (records-only canonical JSONL, one LF, `proof_anchor` present). PF12 §8.6 remains the single home for evidence listing and schema.

---

### **Global discipline (Phase VI)**

* All artifacts under evidence are canonical JSON (or headers-only text) and LF-terminated.

* All harnesses and checks that reason about bytes run with `LC_ALL=C`, `LANG=C`, `TZ=UTC`.

* Index updates are mandatory in the same PR that adds/moves/removes an artifact:

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `artifacts/evidence_index.jsonl`

PF12 §8.6 is the single home for the evidence listing; PF12 Appendix C is the single home for governed record type schemas. 

---

## **Phase VII — Coagulation (SDKs & runtime packaging)**

**Scope.** Ship a hardened runtime and minimal client SDKs that emit the six-key public envelope and typed errors, and lock evidence/ops practices to Governance. Titles-only routing; no contract bytes are defined here. Overall phase status: **Not done**.

---

### **Packaging & Runtime — Not done**

**Status (Audit v1 — 2025-11-17):** Missing tokens: `SERVICE_START_CMD_CAPTURED_OK`, `GUNICORN_APP_FACTORY_OK`, `ENV_PORT_REQUIRED_OK`. SBOM/start-command/env pins proofs not gathered.

**Purpose**  
 Produce a deterministic, hardened runtime artifact and align ops posture with Governance.

**Tasks**

* **Image hygiene**

  * Build reproducible container images.

  * Run as non-root; prefer read-only filesystem where practical.

  * Generate a CycloneDX SBOM for the runtime image.

* **Env & secrets**

  * Enforce an env allow-list; ignore or fail on unexpected env keys.

  * Ensure rails defaults match infra inventory (dev/stage open; prod/CI closed) per Glow-Infrastructure.

  * Never log secrets or PII; enforce redaction for any key-like header or token.

  * Export and verify `LC_ALL=C`, `LANG=C`, `TZ=UTC` in the runtime environment to preserve determinism.

* **Start command & service factory**

  * Capture the exact production start command as `artifacts/proofs/start_command_capture.txt` (UTF-8; one LF; no secrets).

  * Prove the runtime starts via the configured app factory (for example `adapter.factory:create_app`) and binds `$PORT`, not a hard-coded port.

* **Health & ops surface (`/internal/version`)**

  * `GET /internal/version` is operator-only; always `Cache-Control: no-store`; no `ETag`.

  * `HEAD /internal/version` returns 200 with no body and `Content-Length: 0`.

  * Conditional headers (`If-Modified-Since`, `If-None-Match`) are ignored; `/internal/version` never returns 304 and never participates in A7.

  * Body includes emitter SHA, `release_id`, build commit, and minimal deployment metadata required by Governance (titles-only).

* **Caching (production, optional)**

  * If used, provide a private cache keyed by `{viewer_id|person_id(s), design_fingerprint, thresholds_identity, release_id}`.

  * Include `viewer_id` only when output is viewer-dependent (for example perspective).

  * Ensure cache hits preserve A7 semantics (headers, `ETag`, encoding behavior) and never alter typed errors.

  * Invalidate on new `release_id`, threshold/config changes, input shape changes, and manifest/design changes.

* **Security posture (writers & inputs)**

  * Per-route rate-limits on writer endpoints; no unbounded fan-out.

  * Writers and error routes always send `Cache-Control: no-store`; never send `ETag`.

  * Inputs validated against schemas (titles-only to HDE-Schemas & Artifacts).

  * Never log secrets or PII; redaction enforced at the logger boundary.

  * For browser-facing writers, rotate CSRF token on login and allow exactly one safe retry on CSRF failure.

**Acceptance (titles-only)**

* **A7 on success routes**  
   `READER_200_CTYPE_JSON_UTF8_OK · A7_GET_QUOTED_ETAG_OK · A7_HEAD_PARITY_OK · A7_304_OMITS_CT_CL_OK · A7_VARY_AUTH_AE_OK · A7_ENCODING_INVARIANCE_OK`

* **Body parity**  
   Stored vs emitted body byte-parity; encoding-invariance for `ETag` across accepted `Accept-Encoding` values.

* **Pack identity**  
   `MANIFEST_SHA256_HEX64_OK · RELEASE_ID_RECOMPUTE_OK · PACK_MANIFEST_NO_SELF_LISTING_OK`

* **Packaging & ops**  
   `SERVICE_START_CMD_CAPTURED_OK · GUNICORN_APP_FACTORY_OK · ENV_PORT_REQUIRED_OK`

(Token definitions and semantics live in HDE-Governance.)

**Evidence (titles/paths only)**

* **SBOM (CycloneDX) \+ hash**

  * `sbom/cyclonedx.json`

  * `sbom/cyclonedx.json.sha256`

* **Start command & env pins**

  * `artifacts/proofs/start_command_capture.txt`

  * `artifacts/proofs/env_pins.txt` (captures `LC_ALL`, `LANG`, `TZ`, rails posture, port binding, in effect)

* **Ops surface proofs**

  * `artifacts/ops/internal_version/headers_get.txt`

  * `artifacts/ops/internal_version/headers_head.txt`

  * `artifacts/ops/internal_version/body.json`

  * `artifacts/ops/internal_version/conditional_headers.snap` (showing 304 never returned)

* **Reader A7 success proofs** (may be shared with Phase VI artifacts)

  * `artifacts/reader/endpoints_snapshot.json`

  * `artifacts/proofs/success_get.txt`

  * `artifacts/proofs/success_head.txt`

  * `artifacts/proofs/success_304.txt`

  * `artifacts/proofs/success_writers_errors.txt`

**Indexing**

Update, in the same PR:

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `artifacts/evidence_index.jsonl`

Mirror is records-only canonical JSONL; one LF per record; unknown-key reject; fixed field order; each record includes a `proof_anchor` to a co-located `path_proof.txt`. Single home for entry listings: PF12 §8.6. Governed record types: PF12 Appendix C.

---

### **SDKs (TypeScript / Python) — Not done**

**Purpose**  
 Provide minimal SDKs that mirror the six-key public envelope and typed error contracts, with no public numerics and no hidden behavior.

**Tasks**

* **Models & serialization**

  * Define strongly-typed models for the six-key envelope and typed error shapes (titles-only to HDE-CLI-API-Vendor-Ref).

  * Implement canonical JSON serialization:

    * UTF-8, no BOM

    * Sorted keys

    * Compact (no extra whitespace)

    * Exactly one trailing LF

* **Round-trip and parity**

  * `serialize → parse → serialize` must be byte-exact for valid payloads.

  * For a shared test corpus, SDK responses must match Reader’s public envelope and typed error shapes exactly (no extra fields, no missing fields, no renaming).

* **Retries & conditional GET (optional)**

  * Default: no automatic retries; SDK must not introduce its own retry policy.

  * Where provided, a conditional GET helper for Reader must construct headers according to the same rules as core (titles-only) and must not change `ETag` semantics.

**Acceptance (titles-only)**

* Round-trip: `SDK_ROUND_TRIP_CANONICAL_JSON_OK`

* Reader parity: `SDK_READER_PARITY_OK`, `SDK_ERROR_CONTRACT_PARITY_OK`

(Definitions/semantics live in PF04/PF09; PF14 defines behavior, PF05 defines wire contracts.)

**Evidence (titles/paths only)**

* **Type and schema fixtures**

  * `sdks/typescript/schemas/*.json`

  * `sdks/python/schemas/*.json`

* **Test outputs**

  * `sdks/typescript/tests/*`

  * `sdks/python/tests/*`

* **Artifacts per SDK**

  * `sdks/<lang>/artifacts/schema_hashes.json`

  * `sdks/<lang>/artifacts/reader_roundtrip.bytes`

  * `sdks/<lang>/artifacts/conditional_get_headers.snap` (if implemented)

  * `sdks/<lang>/artifacts/error_contract_snapshot.json`

**Indexing**

Update Human Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR. Mirror records must follow PF12 §8.3/§8.6 (canonical JSONL, single file, `proof_anchor`, governed paths).

---

### **Runbooks & Deployment Guards — Not done**

**Purpose**  
 Codify a repeatable go-live and rollback process that enforces Doc-Delta discipline, release identity, index parity, and parity/rails/ops gates.

**Tasks**

* **Runbooks**  
   Write concise runbooks for **Build → Verify → Release → Rollback**. Each must cover:

  * Regenerating `release_id` (via manifest SHA-256).

  * Rebuilding and verifying evidence (A7, determinism, DB posture, bodygraph invariance).

  * Updating Human Index, hash sentinel, and Machine Mirror.

  * Performing a safe rollback and verifying no stale cache or A7 breakage.

* **Pre-flight CI jobs**  
   Add pre-flight jobs that fail fast on:

  * Parity drift (CLI↔Reader / SDK↔Reader).

  * Canonical bytes mismatch (JSON canonicalization).

  * Stale `docs/evidence/INDEX.json` vs `artifacts/evidence_index.jsonl`.

  * `ETag` invariance / A7 regressions.

  * Rails posture violations and missing env pins.

  * 429 handling regressions.

* **Metrics & alerts**

  * Configure bounded labels for ops metrics (`route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`).

  * Define alerts for:

    * Unexpected spike in 5xx/429.

    * Circuit-breaker activations.

    * A7 invariant failures.

    * Evidence indexing failures (missing mirror records, `proof_anchor` mismatches).

**Evidence (titles/paths only)**

* Runbooks: `docs/runbooks/*.md`

* Dry runs: `audit/gates/ops/release_dryrun.log`

* Alert configuration: `artifacts/ops/alerts/*.json`

**Indexing**

Update Human Index (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) in the same PR. Mirror follows PF12 §8.3/§8.6 (canonical JSONL, one file, unknown-key reject, `proof_anchor` path-proofs).

