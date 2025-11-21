# PF16‑Canon — HD Engine Epics Map

**Status:** Canon  
 **Version:** v2.3.8  
 **Date:** 2025‑11‑21  
 **Last Update Gate:** BN 7.6.6 Drain  
 **Invocation tag:** INV-f2ac55d77ce9aacc

## **Deprecation note**

**Deprecation note.** This epics map is **deprecated** and maintained for historical purposes only. EPIC‑011 is recorded here as a **failed** epic (its acceptance roster was not fully satisfied at the time this document was frozen). EPIC‑012 and later epics in this map are **won’t do** and are preserved only as design history. Current and future epic planning is owned by **PF20 — Canon‑HDE‑Phased Epics**; PF16 must not be used as the source of truth for new work.

## **Epic principle (North Star)**

An epic is a gate: it ships working capability with code, tests, runnable evidence, and change-aware execution. Bug fixes and remediation roll into the epic they support. **Green-freeze**: once a suite is certified under an epic, it freezes and re-runs only when a qualifying change touches its dependency tree; if new validation is needed, run it once, then freeze again. Each epic observes **same-PR evidence parity** (Doc-Delta \+ `docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256` \+ `artifacts/evidence_index.jsonl`) and routes bytes and tokens by **title only** to their single homes.

## **Scope**

**What this document includes**

* The **dependency‑ordered map** of engine epics and what each must own to ship.

* The **status locks** for closed epics (history‑only).

* The **active epic briefs** (scope statements), kept **contract‑free** and titles‑only.

* A **PF09→PF16 coverage box** that maps every PF09 task to a PF16 epic (**must be complete**).

* **Global guards** that apply to all epics: PF10 **later‑letter supersession**, **same‑PR evidence parity**, **single‑emitter** and **canonical‑JSON** posture, and the **Reader A7 proof‑surface rule** (Catalog JSON success route only). The Aux scope is limited to **two headers‑only snapshots** in EPIC‑010; Aux **HEAD/304** are excluded (A7 proofs remain Catalog‑only and live under EPIC‑012).

**What this document does not include**

* No byte‑level contracts, header snapshots, payload shapes, or token rosters. Those live by title in:  
   **PF05** (CLI/API/Vendor Ref, Endpoint Catalog and public wire bytes),  
   **PF04** (Governance, token semantics and rails policy),  
   **PF12** (Schemas & Artifacts, Evidence Index and mirror hygiene),  
   **PF06** (Epic Process, PR‑first and close‑pack rules).

* No environment secrets, concrete values, or ops runbooks.

**Rails affirmed here for consistency**

* **Merged SHAs** are recorded under **EPIC‑009** in the close‑pack.

* **All 429 activity** is owned by **EPIC‑012** (none remains in EPIC‑009).

* **Narratives coverage artifact is locked** to **`audit/gates/narratives/keys_10x4.table.json`** (10 categories × 4 bands). Scope and path are referenced by title only here; acceptance and indexing live in PF09/PF12.

**Success criteria for this document**

* Every active epic has a clear, minimal scope that can be tested and evidenced **without restating contracts**.

* The **PF09 coverage box** has **no gaps**; adding a PF09 task requires adding a PF16 mapping.

* Cross‑doc references are **titles‑only** and point to single homes.

---

## **Historical (retained verbatim, history‑only)**

### **EPIC 1.0 — Deterministic Public Reader (Core \+ Transport \+ Minimal Logic)**  \[CLOSED\]

Depends on: — (root). Purpose: Make the public surface correct, byte‑stable, and ready for use. No re‑testing: evidence is frozen; any deferrals are reassigned below.

### **EPIC 2.0 — Internal Mechanics & Enumerations (Person \+ Pair foundations)**  \[CLOSED\]

Depends on: 1.0. Purpose: Deterministic feature layer the rest of the engine relies on. No re‑testing: evidence is frozen; any deferrals are reassigned below. Reassignments from 1.0/2.0 (deferrals/unconfirmed): • Input normalization & canonical error tokens → EPIC‑003. • Deterministic tie‑break/total‑order → EPIC‑006. • Category framework scaffolds → EPIC‑006. • Compat pair engine & surface (internal) → EPIC‑003.

### **HDE‑EPIC003 — Alpha Unlock I: Compat Core & Inputs**  \[CLOSED\]

Depends on: 2.0. Resolves: compat engine & surface, input normalization, error envelope/tokens, with AB↔BA and fixed Magic‑10 order; alpha transport posture; single‑emitter proofing. *(Historical scope unchanged.)*

### **HDE‑EPIC004 — Alpha Unlock II: Single HTTP Home & Transport Consolidation**  \[CLOSED\]

Depends on: 003\. Resolves: single HTTP home, Reader A7 post‑consolidation proofs, edge posture. *(Historical scope unchanged.)*

### **HDE‑EPIC005 — Alpha Unlock III: Identity, Meta & Required Persistence**  \[CLOSED\]

Depends on: 004\. Resolves: identity/provenance, base DDL, **/internal/version** alpha posture and headers. *(Historical scope unchanged.)*

### **HDE‑EPIC006 — Mechanics Foundations**  \[CLOSED\]

**Status lock: CLOSED** (tie‑break/total‑order, comparators, invariance, **/internal/version** head/conditionals remediation). PF09 Phase‑I “Deterministic tie‑break & total‑order module — Implement” is satisfied by this closed epic; it is not carried to remaining epics.

### **HDE‑EPIC007 — Magic‑10 Category Engine (Signals)**  \[CLOSED\]

**Status lock: CLOSED** (Magic‑10 defs, caps, mappings, thresholds, determinism proofs). PF09 Phase‑II “Category framework” and “Band thresholds & tuning (admin)” are satisfied here; they are not carried forward.

**Status lock (history‑only; append‑only notes for clarity)**  
 **EPIC‑006 — CLOSED.**  
 **EPIC‑007 — CLOSED.**  
 **EPIC‑008 — CLOSED.**  
 **EPIC‑010 — CLOSED.** Exit set (by title only) includes: **Aux narrative posture** (200 text present, 200 suppressed no ETag with **Vary** on both outcomes), **provenance determinism and env pins**, **narratives coverage 10×4 present**, **mirror/index discipline**, and **CLI preview parity & indexing**; token names and CI gates live in PF09/PF04/PF12. The A7 proof surface remains the **Catalog JSON success route**; **Aux HEAD/304** are out‑of‑scope for EPIC‑010 and live under EPIC‑012.

**A7 routing reminder.** Reader A7 proofs apply **only** to **JSON success routes** cataloged in the Endpoint Catalog; **/internal/version** is ops‑only and excluded from A7. Aux HEAD/304 are **explicitly out of scope for EPIC‑010** and are owned by EPIC‑012.

---

### HDE-EPIC008 — Writers & Auth  \[CLOSED\]

**Status lock:** **CLOSED** (validated against PF10 \+ PF09 carry-ins)  
 **Depends on:** HDE-EPIC005

**Delivered scope (validated):**

1. Minimal idempotent writer surfaces — strict schemas; **no-store**; never echo payload/PII.  
2. AuthN/AuthZ boundary — browser vs S2S; scopes; route ownership.  
3. Secrets posture — env provisioning; redact in logs.  
4. Logging redaction & PII guards — keys-only diagnostics; redaction filters \+ tests.  
5. Typed envelopes & **A7 posture (writers)** — numeric-free success and error envelopes; writers **no-store** and **never 304**; errors carry `Content-Type: application/json; charset=utf-8`; **no ETag**.  
6. Idempotent write path — canonicalize body, recompute/verify `idempotence_hash`, record `release_id`; **byte-compare stored vs unified emitter bytes**.  
7. Admin gate \+ rate limits — admin capability required; rate limits; vendor gate respected.  
8. Evidence & indexing (**same PR**) — human Index and machine JSONL mirror with **path-proofs**. *(PF09 Phase-IV “Writer Surfaces: Not done” → **closed here**.)*

**Exit markers (met):** WRITERS\_SCHEMA\_OK, AUTHZ\_BOUNDARY\_OK, SECRETS\_READY\_OK, PII\_REDACTION\_OK, WRITERS\_ERRORS\_NOSTORE\_NOETAG\_OK, WRITERS\_NO\_304\_OK, IDEMPOTENT\_WRITE\_OK, RELEASE\_ID\_RECORDED\_OK, EVIDENCE\_INDEX\_UPDATED\_OK, EPIC\_IS\_GATE\_OK.

**Deferrals (history-only):** *None — all PF09 writer-surface carry-ins resolved in EPIC-008.*  
 **Routing (titles-only):** HDE-CLI-API-Vendor-Ref, HDE-Governance §2.0, HDE-Schemas & Artifacts §4.

### HDE-EPIC009 — Ops Safety & DB Runtime Posture \[CLOSED\]

**Depends on:** HDE-EPIC004

**Resolves (including PF09 carry-ins):**

1. **SAFE rails & provider gate.** Rails closed by default; typed refusal; keys-only logs (no payload/headers; secrets redacted); no `ETag`, no `Vary`, no compression on refusal.  
2. **429 scope.** **No 429 success-path activity lives here** (all 429 is owned by EPIC-012).  
3. **Observability.** Bounded labels (e.g., `route`, `outcome`, `rails_state`, `timeout_profile`, `attempt_idx`); counters/histograms only; no payload/secret logging.  
4. **Security posture.** Per-route limits; validation guards.  
5. **Open-rails policy pins.** Timeouts/retries/backoff with **closed integer domains**, **no jitter**, and total-time budget respected.

6.  6\. **DB runtime posture (production \+ dev bridge fallback).** `search_path = hde, public` (order enforced); least‑privilege runtime grants; **canonical DDL fingerprint**; **connection selection** — **Non‑dev**: presence‑only `DATABASE_URL → DB_BRIDGE_URL → typed error` (**no connectivity probe**). **Dev**: when `APP_ENV=dev` and `DATABASE_URL` is present **but unusable**, **fall back to `DB_BRIDGE_URL`** and proceed (**keys‑only diagnostics; no secrets/payloads in logs**). *(PF09 Phase V DB Runtime; PF10 Addendum 4 carry‑forward).*

7. **Evidence & indexing (same PR).** Refusal runs (**no success/429 here**), DB posture snapshots; update the **human Evidence Index** and its **hash sentinel** plus the **machine mirror** in the **same PR** (records-only, canonical JSONL, one LF, unknown-keys rejected, each record has a `proof_anchor`). **Close-pack includes merged commit SHA(s)** alongside the report and manifest. **artifacts/runtime/env\_connectivity.snapshot.json** — **dev fallback decision proof** (attempted, result, selected). *(Index human+machine in the same PR.)*

**Exit markers (titles-only):**  
 `SAFE_RAILS_OK`, `ENV_RAILS_POLICY_OK`, `OBS_KEYS_ONLY_OK`, `SECURITY_POSTURE_OK`,  
 `DB_RUNTIME_SEARCH_PATH_OK`, `DB_ROLE_OK`, `DB_SCHEMA_FINGERPRINT_OK`, `DB_CONN_ENV_OK`,  
 `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EPIC_IS_GATE_OK`, `CLOSE_PACK_FILES_PRESENT_OK`.

**Routing (titles-only):** HDE-Governance (rails/tokens), HDE-CLI-API-Vendor-Ref (provider bytes), HDE-Mechanics Guide §7.1/§7.3 (mechanics), HDE-Schemas & Artifacts (index/mirror), **Epic-Process-Guide** (PR-first/close-pack).

---

### HDE-EPIC010 — Aux Narrative Surface \[CLOSED\]

Depends on: **HDE-EPIC003, HDE-EPIC007**

**Resolves (including PF09 carry-ins):**

* **Aux text surface (not A7).** Deterministic, LF-terminated text surface for narrative output. Suppression carve-out: 200 with no body and no ETag (policy header optional). Transport bytes and header posture are owned by Governance/Vendor Ref (titles-only). Reader remains bands-only; Aux is the narrative surface.

* **Fragment packs & manifests.** Pack loader \+ validator; manifest SHA discipline; Doc-Delta on change.

* **Deterministic composer (keys-only).** Seeded selection, no clocks/RNG, AB↔BA parity; composer operates on keys only (no prose in this epic).

* **Narrative Selection Router (keys-only).** Deterministic mapping `(category, band, perspective, viewer_top, flags) → {personal_key, shared_key}`; no RNG; no fallbacks (missing mapping ⇒ `missing_narrative_key`). CLI \= HTTP parity via the shared emitter.

* **Narrative Key Registry & Manifests.** Exactly one key per `(category, band, perspective)`; manifest-driven identity `pack_sha = sha256(canonical manifest bytes)`; uploads at `/narratives/<pack_sha>/…`; diffable manifests; closure check enforced.

* **Two-plane architecture (authoring vs runtime).** DB-backed authoring (intake, lints, preview, publish pointer, audit) and file-backed runtime (sealed pack; no DB reads on hot path); loader `fetch → verify → atomic swap → load`; fail-closed on verify mismatch; keys-only logs.

* **Suppression posture.** Reader stays narrative-free; Aux suppression returns 200 empty body, no ETag (policy header optional).

**Evidence & indexing (same PR).**

* **Narratives coverage (router).** `audit/gates/narratives/keys_10x4.table.json` (10 categories × 4 bands).

* **Aux header snapshots (EPIC-010 scope; headers-only).**

  * `tests/transport/headers/aux_text_200.snap`

  * `tests/transport/headers/aux_suppression_200.snap`  
     *(No Aux HEAD/304 captures in EPIC-010; A7 remains Catalog-only.)*

* **Narrative manifests & registry.** `artifacts/narratives/registry/*.json` (manifests).

Index human \+ machine in the same PR (canonical JSONL; one LF; unknown-key reject; `proof_anchor` present). Keep prior captures (manifests diff, router snapshot/tests, suppression snapshot).

**Exit markers (titles-only).**

`AUX_SURFACE_OK, AUX_SUPPRESSION_NO_BODY_NO_ETAG_OK, PACKS_MANIFEST_OK, AUX_IDENTITY_OK, NARR_ROUTER_KEYS_ONLY_OK, NARR_REGISTRY_CLOSURE_OK, NARR_PACK_IDENTITY_OK, AUX_SUPPRESSION_200_EMPTY_NOETAG_OK, EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_HASH_OK, MACHINE_MIRROR_UPDATED_OK, EPIC_IS_GATE_OK.`

**Routing (titles-only).** HDE-Narratives Guide (PF17) for narrative rules; HDE-CLI-API-Vendor-Ref (PF05) for transport exposure points; HDE-Governance (PF04) for posture/tokens; HDE-Schemas & Artifacts (PF12) for Evidence Index/mirror.

# Carry‑forward summary from PF09 (titles‑only)

**Purpose.** Resolve all PF09 items not already closed under EPIC‑006/007 by assigning clear epic ownership, with status notes and dependency cues. No contracts or bytes are restated here; all routing is by title to PF05/PF04/PF12/PF10.

**Status context.**

* **Closed (history‑locked):** EPIC‑006, EPIC‑007, EPIC‑008, EPIC‑010. No PF09 work remains in these epics.

* **EPIC‑011:** *Implemented and merged* per PO note, but **no production QA evidence landed**; treat as **Open — developer review required** until governed proofs are captured and indexed (same‑PR Index \+ Mirror parity).

* **Reader A7 surface rule:** A7 proofs run **only** on a Catalog **JSON success** route; `/internal/*` is ops‑only. Ownership and proofing live under **EPIC‑012**.

---

#### **Allocation (PF09 → PF16 owner)**

**Phase I / II foundations (remaining items)**

* Canonical serialization package; deterministic tie‑break/total‑order **(residuals only)** → **EPIC‑012** (prove via parity harness \+ A7 captures on Catalog route).

* Programmatic configuration system (registry report; unknown‑ID hard‑fail) **carry‑in tests** → **EPIC‑012** (exercise under determinism & Reader parity).

**Phase III (public shape, identity, guardrails)**

* **Public Presenter/Emitter** (Reader↔CLI identity, LF, AB↔BA, two‑run, preimage) → **EPIC‑012** (shared‑emitter proof \+ CLI parity artifacts `artifacts/cli/ab.json|ba.json|summary.json`).

* **Reader Surface (API)** — Catalog \+ A7 matrix (GET/HEAD/304/encoding invariance; env‑gate) → **EPIC‑012** (creates and owns `docs/ENDPOINTS_CATALOG.json` \+ `.sha256`, env‑gate proof, success headers).

* **CLI tooling & conformance** (“showcompat”, install/help) → **EPIC‑012** (**All PF05‑documented CLI commands must be implemented here**).

* **Internal ops `/internal/version`** (HEAD 200 parity; conditionals ignored; no‑store; no ETag) → **EPIC‑013** (ship proofs with release provenance).

**Phase IV (surfaces meet the core)**

* **Compat surface (internal)** parity & identity\_hash capture (Catalog‑excluded) → **EPIC‑012** (prove via public parity harness; keep internal scope per PF09).

**Phase V (narratives & bridges)**

* **SAFE rails posture** (closed refusal; keys‑only logs; open pins) and **DB runtime posture** (search\_path, grants, DDL fingerprint, conn env order) → **EPIC‑009** (ops safety \+ posture).

* **429/Retry‑After success‑path semantics** (typed PROVIDER\_RATE\_LIMITED; deterministic parse) → **EPIC‑012** (A7/transport owner; none remains in 009).

* **Narrative selection router (keys‑only)**, **Key registry & manifests** → **EPIC‑010** *(closed; history‑only)*; any new gaps reopen as Doc‑Delta \+ evidence under **EPIC‑012**.

**Phase VI (evidence & performance)**

* **Gate scripts & integrated evidence harness** (preimage recompute; two‑run; AB↔BA; canonical compare), **A7 suite on Catalog**, **Observability samples**, **Bench/load** → **EPIC‑012** (harness & proofs) and **EPIC‑013** (release‑time reruns as needed).

**Phase VII (packaging, SDKs, runbooks)**

* **Packaging & runtime** (SBOM; start command; env pins; `/internal/version` ops proofs) → **EPIC‑013** (release & provenance).

* **SDKs (TS/Python) & Admin UI** (schemas hashed; Reader/error parity; optional conditional‑GET helper) → **EPIC‑014**.

* **Runbooks & deployment guards** (Doc‑Delta discipline; pre‑flight CI; alerts) → **EPIC‑013** (author) with **EPIC‑014** consuming checklists for SDK parity.

---

#### **Coverage box (PF09 rows → Epic owner)**

| PF09 area (titles‑only) | Epic owner | Notes |
| ----- | ----- | ----- |
| Endpoint Catalog (JSON success routes only) & A7 invariants | **EPIC‑012** | Owns `docs/ENDPOINTS_CATALOG.json` \+ `.sha256` and all success‑route proofs; `/internal/*` excluded. |
| Reader six‑key envelope; Reader↔CLI byte parity; preimage recompute | **EPIC‑012** | Shared‑emitter parity \+ CLI artifacts (`ab.json`, `ba.json`, `summary.json`). |
| CLI commands documented in PF05 | **EPIC‑012** | Must be implemented and evidenced here (install/help/run/parity). |
| SAFE rails closed/open (refusal; pins; log redaction) | **EPIC‑009** | 429 success‑path moved to EPIC‑012. |
| DB runtime posture (search\_path, grants, DDL fingerprint, conn env selection) | **EPIC‑009** | Evidence captured with same‑PR Index/Mirror parity. |
| Vendor ingest & durability (migrations, backups, retention, partition plan) | **EPIC‑011** | **Open — dev review required**; not closed until prod QA proofs are indexed. |
| Performance & load harness; observability samples | **EPIC‑012** | Deterministic, non‑PII; bounded labels. |
| Packaging/runtime; release provenance; `/internal/version` ops proofs | **EPIC‑013** | Includes SBOM; start command capture; env pins; ops headers. |
| SDKs & Admin UI; schema hashes; SDK parity | **EPIC‑014** | Tokens live in Governance; artifacts in PF12. |

**Allocation rule (PO).** All PF09 tasks **not** marked **Done** (and **not** already earmarked for EPIC‑011) are allocated to **EPIC‑012/013/014** as above. All PF05 CLI commands are implemented under **EPIC‑012**.

**Indexing rule.** For every epic: same‑PR parity for **Human Index** (`docs/evidence/INDEX.json` \+ `.sha256`) and **Machine Mirror** (`artifacts/evidence_index.jsonl`), records‑only canonical JSONL, unknown‑key reject, `proof_anchor` present. (Tokens and schemas live by title in PF12/PF04.) 

---

### **HDE-EPIC011 — Vendor Ingest & Data Durability *(failed)***

**Depends on.** HDE-EPIC005 (consumes rails/DB posture delivered by EPIC-009).

**Resolves (including PF09 carry-ins).** Vendor ingest (SAFE-default), idempotent persistence, deterministic retry/backoff conformance, migrations with rollback drills, backups & restore, data retention, partition plan, BodyGraph ingest policy, out-of-band refresh posture, source invariance concept. PF09 items routed here remain titles-only and are evidenced in this epic.

#### **Scope (titles-only)**

* **Vendor ingest (SAFE-default).** Integrations are refusal-first unless rails are open (per EPIC-009 / Governance). When open, requests follow pinned timeouts/retries/backoff; responses map to typed errors; no payload/header logging; secrets redacted (keys-only diagnostics).

* **Idempotent persistence.** Ingest writes are idempotent (idempotency key or content hash); transactional boundary proven; stored public body byte-compares to unified emitter bytes.

* **Retry/backoff conformance.** Profiles `{none, fixed, exponential}` with closed integer params, no jitter, total time respected; `retryable = {network_error, 5xx}`; do not retry other 4xx. `429` success-path activity is owned by EPIC-012; this epic only records the typed outcome.

* **Migrations with rollback drills.** Dry-run plan → forward apply → rollback verified → post-migration consistency checks.

* **Backups & restore.** Point-in-time backup plan \+ restore rehearsal; integrity/hash verification; operational runbook artifacts.

* **Data retention jobs.** Policy-driven deletes/archives; proof of effect with bounded labels (no payloads).

* **Partition plan *(non-deferred for EPIC-011*.** Provide and maintain a concrete partition plan for the governed tables (for example `hde.body_graphs`, `hde.body_graphs_current`, `hde.pair_evaluation`, `hde.public_results`). Where a plan exists, verify partition predicates and maintenance jobs via governed artifacts under `artifacts/db/partition/partition_plan.txt` and `artifacts/db/partition/partition_verify.log` (schemas and evidence rules live in **HDE-Schemas & Artifacts**). For this epic, the partition plan is **non-deferred**: EPIC-011 is gated by `PARTITION_PLAN_OK` only; there is no `PARTITION_PLAN_DEFERRED_NOTED` path under this epic (the “defer” pattern remains available in PF09 for other scopes).

* **BodyGraph ingest policy (adapter; env-aware).**

  * **Prod:** BodyGraph from DB; vendor calls only by explicit trigger or scheduled refresh (never inline).

  * **Dev:** Direct vendor allowed; on success, upsert to DB for repeatability. SAFE rails apply (rails CLOSED by default; rails-open guard and tokens live in Governance / PF04, PF07).

* **Refresh posture (out-of-band).** Enforce TTL and SWR; refreshes run out-of-band; apply vendor rate-limits and a circuit breaker `{fail_threshold, window_s, cooldown_s}`; no inline vendor calls in prod.

* **Source invariance (concept).** For identical normalized inputs, DB-sourced and vendor-sourced bodies render to byte-identical canonical JSON under the single shared presenter/emitter.

* **Preservation: CLI, vendor ingest, compat math, Aux.** Under EPIC-011, the following surfaces are **preservation surfaces** (EPIC-011 may add durability and evidence but MUST NOT change their contracts):

  * CLI (`hdctl` commands, flags, streams, exit codes) and on-wire vendor request/response bytes — owned by **HDE-CLI-API-Vendor-Ref**.

  * Compat math (Magic-10 category definitions, scoring, band thresholds, AB↔BA identity, Reader v1 envelope) — owned by **HDE Math & Technical Spec**.

  * Aux narratives (packs, IDs, suppression rules, text surfaces) — owned by **HDE Narratives Guide**.

  * Single-emitter, Reader↔CLI parity, two-run identity, canonical-JSON posture — owned by **HDE-Mechanics Guide**.

* Any functional change to these surfaces MUST be owned by a separate epic with its own scope and acceptance (per Governance); EPIC-011 only proves that these surfaces behave as defined in their canonical homes.

#### **Evidence (titles/paths only)**

**BodyGraph proofs**

* `artifacts/bodygraph/source_selection.snapshot.json` — `{app_env, attempted, selected, reason, upserted}` (canonical JSON; one LF).

* `artifacts/bodygraph/source_invariance/ab.json` · `.../ba.json` · `.../summary.json` — DB vs vendor bytes equality via shared emitter.

* `artifacts/bodygraph/refresh_policy.snapshot.json` — `{ttl_s, swr_s, rate_limit, cb{fail,window_s,cooldown_s}, sample_counts}`.

* *(Observability)* `artifacts/bodygraph/metrics.snapshot.json`, `artifacts/bodygraph/keys_only.logs.sample`.

**Ingest**

* `artifacts/ingest/ingest_success.log`

* `artifacts/ingest/retry_trace.log`

* `artifacts/ingest/idempotency_proof.log`

**Migrations**

* `artifacts/db/migrations/plan.json`

* `artifacts/db/migrations/dryrun.log`

* `artifacts/db/migrations/apply.log`

* `artifacts/db/migrations/rollback_verify.log`

**Backups / restore**

* `artifacts/db/backup/backup_manifest.json`

* `artifacts/db/backup/restore_verify.log`

**Retention**

* `artifacts/db/retention/retention_run.log`

**Partition plan**

* `artifacts/db/partition/partition_plan.txt`

* `artifacts/db/partition/partition_verify.log`

**Parity proof**

* `artifacts/presenter/json_canon_compare.log` — stored vs emitted bytes, via canonical presenter.

#### **Interfaces & constraints (titles-only)**

* Rails posture & open/closed policy pins → **EPIC-009** / **HDE-Governance**.

* `429` success-path A7 behavior → **EPIC-012** / **HDE-Governance** (this epic only asserts typed refusal and logging posture).

* DB runtime posture (search\_path / grants / fingerprint / connection order) → **EPIC-009** / **HDE-Schemas & Artifacts** evidence rules.

* Public bytes parity (emitters) → **HDE-CLI-API-Vendor-Ref**; canonical JSON rules → **HDE-Schemas & Artifacts** §4.

#### **Acceptance (titles-only; tokens live in HDE-Governance / PF09)**

**Ingest**

* `INGEST_OK`

* `INGEST_IDEMPOTENT_OK`

* `VENDOR_RETRY_BACKOFF_OK`

* `VENDOR_NO_PAYLOAD_LOGGING_OK`

**Migrations**

* `MIGRATE_ROLLBACK_OK`

**Backups / restore**

* `BACKUP_RESTORE_OK`

**Retention**

* `RETENTION_JOBS_OK`

**Partitioning**

* `PARTITION_PLAN_OK` — EPIC-011 is **non-deferred** on partitioning; there is no `PARTITION_PLAN_DEFERRED_NOTED` success path under this epic.

**Indexing & epic gate**

* `EVIDENCE_INDEX_UPDATED_OK`

* `EVIDENCE_INDEX_HASH_OK`

* `MACHINE_MIRROR_UPDATED_OK` *(see PF12 / PF09 for canonical naming and semantics)*

* `EPIC_IS_GATE_OK`

**BodyGraph ingress / durability**

* `BG_SOURCE_SELECTION_OK`

* `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`

* `BG_DEV_DIRECT_CALLS_UPSERT_OK`

* `BG_SOURCE_INVARIANCE_OK`

* `BG_TTL_SWR_POLICY_OK`

* `BG_RATE_LIMIT_POLICY_OK`

* `BG_CIRCUIT_BREAKER_OK`

#### **Indexing**

Update `docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256` \+ `artifacts/evidence_index.jsonl` in the same PR (records-only canonical JSONL; one LF; unknown-key reject; fixed field order; each record includes a `proof_anchor`). Single home for listings/schemas: **HDE-Schemas & Artifacts** §8.6 / Appendix C.

---

## **HDE‑EPIC012 — Distillation: Reader A7 proofs & Performance (won’t do)**

**Depends on:** HDE‑EPIC004 *(shared presenter/emitter)*; consumes rails/DB posture from **EPIC‑009**; interfaces with **EPIC‑011** as needed.

**Resolves** *(including PF09 carry‑ins)*: Reader JSON success route \+ Endpoint Catalog; env‑gate proof; A7 proofs on the Catalog route (GET/HEAD/304/Vary/encoding invariance; writers/errors no‑store); gate scripts & evidence harness; 429 success‑path ownership (deterministic Retry‑After parse → `retry_after_ms`); public CLI parity harness for Reader; performance & load harness; edge/server cache posture (optional).

### **Scope (titles‑only)**

* **Reader JSON success route** (six‑key envelope via shared presenter/emitter).

* **Endpoint Catalog posture** (internal‑only; env‑gated; env‑gate proof).

* **A7 on the Catalog route**:  
   strong quoted `ETag`; `Vary: Authorization, Accept‑Encoding`; **HEAD 200 parity**; **304 omission** (`Content‑Type`/`Content‑Length` absent); writers/errors **no‑store**; **encoding invariance**.

* **Gate scripts & evidence harness** for determinism/transport.

* **429 success‑path** ownership (deterministic `Retry‑After` parse → `retry_after_ms`).

* **Public CLI parity harness** (AB/BA, two‑run identity, canonical compare via shared emitter).

* **Performance/load harness**; optional server cache posture; edge/CDN posture.

* **Ops exclusion**: `/internal/version` is ops‑only and **not** A7‑eligible; proofs run **only** on a Catalog JSON success route.

### **Evidence (titles/paths only)**

**Catalog file (single home)**

* `docs/ENDPOINTS_CATALOG.json` *(canonical JSON; one LF)*

* `docs/ENDPOINTS_CATALOG.json.sha256`  
   *(List JSON success routes only; env‑gated; `/internal/*` excluded. Index human+machine in the same PR.)*

**Env‑gate proof (headers‑only)**

* `artifacts/proofs/endpoints_env_gate_proof.log` *(non‑prod entries unreachable in prod)*

**A7 invariants (headers‑only; Catalog route)**

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_encoding_invariance.txt`

* `artifacts/proofs/success_writers_errors.txt`  
   *(LF‑terminated; mirror is records‑only canonical JSONL; one LF; unknown‑key reject; each record has a `proof_anchor`.)*

**Performance / Load**

* `artifacts/bench/bench_report_{release_id}.json`

* `artifacts/bench/parity_identity_{release_id}.log`

* `artifacts/bench/transport_headers_{release_id}/…`

* CI jobs: `ci/jobs/bench_math_transport.yml`, `ci/jobs/bench_vendor_open.yml`, `ci/jobs/slo_verify.yml`

**CLI parity harness (public CLI)**

* `artifacts/cli/ab.json`

* `artifacts/cli/ba.json`

* `artifacts/cli/summary.json` *(attempted commands; sha256 of ab/ba; `ab_ba_equal: true`)*

### **Acceptance (titles‑only)**

`LOAD_HARNESS_OK, HEALTH_READY_CACHE_OK, EDGE_POSTURE_OK, SERVER_CACHE_OPTIONAL_OK, ENDPOINTS_CATALOG_OK, ENDPOINTS_CATALOG_INTERNAL_OK, ENDPOINTS_CATALOG_ENV_GATE_OK, A7_GET_QUOTED_ETAG_OK, A7_HEAD_PARITY_OK, A7_304_OMITS_CT_CL_OK, A7_VARY_AUTH_AE_OK, A7_ENCODING_INVARIANCE_OK, A7_TRANSPORT_PROOF_OK, RL_429_OK, RETRY_AFTER_PARSE_OK, EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_HASH_OK, MACHINE_MIRROR_UPDATED_OK, EPIC_IS_GATE_OK, CLI_INSTALL_OK, CLI_HELP_OK, CLI_SHOWCOMPAT_PRESENT, CLI_SHOWCOMPAT_CANON_OK, CLI_AB_BA_PARITY_OK, CLI_TWO_RUN_IDENTITY_OK, CLI_READER_EMITTER_PARITY_OK`

### **Indexing**

Update **docs/evidence/INDEX.json** \+ **docs/evidence/INDEX.sha256** \+ **artifacts/evidence\_index.jsonl** **in the same PR** (records‑only; canonical JSONL; one LF; unknown keys rejected; each record includes a `proof_anchor`). Single home for listings/schemas: **PF12 §8.6 / Appendix C**. 

---

## **HDE‑EPIC013 — Release & Provenance (won’t do)**

**Depends on:** HDE‑EPIC005, HDE‑EPIC012 (success route \+ A7 complete before release work lands). This epic packages the runtime, freezes provenance, and ships governed identity artifacts with same‑PR evidence parity.

### **Resolves (including PF09 carry‑ins)**

* **Packaging & runtime** (Docker/process launch; typed config; health/ready); **ops posture wired for `/internal/version`** — `Cache-Control: no-store`, **no ETag**, HEAD 200 parity, conditionals ignored.

* **Release & provenance packaging** — freeze pack; Evidence Index single‑home discipline with CI staleness block; repo‑dump manifest/checksums as governed artifacts.

* **SBOM & dependency pinning** — CycloneDX; dependency pins; vuln‑scan wiring (names‑only).

* **Post‑deploy smoke** — Writer→Reader verification, cache‑posture checks, bounded‑label metrics/log probes, no payloads/secrets.

* **Manifest & release identity discipline** — `release_id = sha256(canonical_bytes("catalog/manifest.json"))`; canonical JSON; one LF; no self‑listing; recompute \+ record on change.

* **DB posture artifacts with each release** — search\_path, grants, DDL fingerprint, and connection env selection included beside identity artifacts in every release PR.

* **Start‑command capture & env pins** — governed artifacts (exact start command bytes \+ sha256 and `LC_ALL/LANG/TZ` pins); **update human index \+ hash sentinel \+ machine mirror in the same PR**.

  ### **Exit markers (titles‑only)**

`RUNTIME_PACKAGING_OK, RELEASE_PROVENANCE_OK, SBOM_PINNED_OK, POSTDEPLOY_SMOKE_OK, MANIFEST_SHA256_HEX64_OK, PACK_MANIFEST_NO_SELF_LISTING_OK, RELEASE_ID_RECOMPUTE_OK, START_COMMAND_CAPTURE_OK, ENV_LC_ALL_C_OK, EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_HASH_OK, MACHINE_MIRROR_UPDATED_OK, EPIC_IS_GATE_OK.`

### **Evidence (titles/paths only)**

**Pack & identity**

* `artifacts/math/freeze_pack_manifest.json`

* `artifacts/math/release_id.txt`

* `artifacts/math/release_id_recompute.log`

**Start‑command & pins**

* `artifacts/proofs/start_command_capture.txt`

* `artifacts/proofs/env_pins.txt`

**Ops identity (`/internal/version`)**

* `artifacts/ops/internal_version/body_get.json`

* `artifacts/ops/internal_version/body_get.sha256`

* `artifacts/ops/internal_version/headers_get.txt`

* `artifacts/ops/internal_version/headers_head.txt`

* `artifacts/ops/internal_version/cond_if_none_match_headers.txt`

* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

**DB posture with release**

* `artifacts/db/check_schema.txt`

* `artifacts/db/grants.txt`

* `artifacts/db/ddl_fingerprint.json`

* `artifacts/db/conn_env_selection.log`

* `artifacts/runtime/env_matrix.snapshot.json`

* *(optional)* `artifacts/runtime/env_matrix.failure.json`

* `artifacts/runtime/env_connectivity.snapshot.json`

**SBOM (optional)**

* `sbom/cyclonedx.json`

* `sbom/cyclonedx.json.sha256`

**BodyGraph bindings**

* `artifacts/bodygraph/release_bindings.json` — release‑time bindings snapshot (records‑only; canonical JSON; one LF).

  ### **Indexing (same PR)**

Update `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` **together**, with records‑only canonical JSONL (UTF‑8; ASCII‑sorted keys; compact; one LF), unknown‑keys rejected, fixed field order, and a `proof_anchor` to a co‑located path proof for **each** record.

### **Routing (titles‑only)**

Public bytes & Endpoint Catalog → **HDE‑CLI‑API‑Vendor‑Ref** · A7/transport semantics & ops posture → **HDE‑Governance** · Index/mirror & canonical JSON rules → **HDE‑Schemas & Artifacts** · PR‑first/close discipline → **Epic‑Process‑Guide**.

---

## **HDE‑EPIC014 — SDKs & Admin UI (won’t do)**

**Depends on:** HDE‑EPIC007, HDE‑EPIC010, HDE‑EPIC013  
 **Interfaces:** consumes the six‑key Reader envelope and transport posture delivered under EPIC‑012 (titles‑only).

### **Resolves (including PF09 considerations)**

* **Schemas (Reader / internal / Aux) \+ schema hashes** — publish canonical JSON schemas (UTF‑8/no BOM; ASCII‑sorted keys; compact; one LF) and a governed `schema_hashes.json` (sha256 map); Doc‑Delta on change.

* **SDKs (TypeScript & Python)** — minimal helpers that reproduce service bytes using the single emitter (no ad‑hoc serializers); conditional GET helper for Reader; writer wrappers emit typed errors; **no public numerics**.

* **Parity tests** — SDK↔service byte/order parity for the six‑key envelope; AB↔BA identity where applicable; exactly one trailing LF.

* **Admin UI (Local Verification)** — local checks for AB↔BA identity scenarios and 304 reuse (conditional cache validation) without touching public caches.

  ### **Evidence & indexing (same PR)**

Update Human Evidence Index (`docs/evidence/INDEX.json` \+ `docs/evidence/INDEX.sha256`) and Machine Mirror (`artifacts/evidence_index.jsonl`) **in the same PR**. Mirror is records‑only canonical JSONL (one LF; unknown‑keys rejected; each record includes a `proof_anchor`). **PF12 §8.6 is the single home for entry listings; Appendix C defines record types** (titles‑only reference).

### **Exit markers (titles‑only)**

`SCHEMAS_HASHED_OK, SDK_TS_PY_OK, SDK_PARITY_OK, ADMIN_UI_OK, EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_HASH_OK, MACHINE_MIRROR_UPDATED_OK, EPIC_IS_GATE_OK.`

### **Evidence (titles/paths only)**

* **Schemas & hashes:** `sdks/*/schemas/*.json`, `sdks/*/artifacts/schema_hashes.json`

* **Parity & round‑trip:** `sdks/*/artifacts/reader_roundtrip.bytes`, `sdks/*/tests/parity.test.*`

* **Conditional GET helper:** `sdks/*/artifacts/conditional_get_headers.snap`

* **Admin UI local checks:** `sdks/admin/artifacts/local_304_reuse.snap`, `sdks/admin/tests/admin_verification.test.*`

  ### **Routing (titles‑only)**

Public wire bytes & Endpoint Catalog → **HDE‑CLI‑API‑Vendor‑Ref** · A7/transport semantics & policy → **HDE‑Governance** · Evidence Index/mirror & canonical JSON rules → **HDE‑Schemas & Artifacts** · Narrative keys/text policy → **HDE‑Narratives Guide** (PF17).

---

## **Dependency order (v2 Canon)**

`2.0 → 003 → 004 → 005 → 006 → 007 → 008 → 009 → 010 → 011 → 012 → 013 → 014`  
 (Clarifications: 012 follows 009 and precedes 013; 008 may progress in parallel after 005; 010 can stub after 003 with suppression‑only posture.)

---

## **Crosswalk (titles only)**

* **Mechanics Guide to the HD Engine (Build Guide)** — components & tasks referenced across all EPICs.

* **HD Engine Build Checklist (Components & Tasks)** — binding requirement: each epic line item references at least one checklist row (titles‑only; no versions). If a checklist item is *Consolidation pending*, it closes in **012** (Reader success route & A7) or **013** (packaging/runtime), not both.

  ---

  ## **Final guardrails**

* No duplicate closures across epics; resolve overlaps before execution.

* Alpha scope locked: Compat uses 200‑only posture behind the app; full A7 for Compat is production hardening (012/013); Reader A7 recapture is only in 012; POST is non‑conditional.

* Evidence once, then freeze (**green‑freeze**); re‑run suites only on qualifying changes.

* Merged SHAs are recorded under 009 (in the close‑pack).

* **All 429 activity is owned by 012 (none in 009).**

