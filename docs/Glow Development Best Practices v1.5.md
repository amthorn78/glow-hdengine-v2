# Glow Development Best Practices v1.1

Agent: Full Stack Guru 5 

Date: 09/27/25

# **Chapter 1 — FIRE: Delivery Process & Execution Rituals**

*Truth above all else. FIRE is how we purify intent into clean, verifiable shipments without CI, with PO-only review, and with uncompromising integrity.*

---

## **0\) Purpose & Operating Mode (read me first)**

* **Purpose:** Make every change *true*: reproducible, reviewable, reversible.  
* **Operating Mode:** **No GitHub CI/PR.** Actions may store **secrets only**. All checks run **locally**.  
* **Review Model:**  
  * **Before any coding session:** request a **pre-session audit** (latest **repo dump** \+ **HEAD SHA**).  
  * **Per card close:** PO produces a **full repo dump** (authoritative evidence).  
  * **Mid-card review:** *only if the PO requests it* (share a code snapshot).  
* **Agency:** Agents are **not autonomous**. Act **only** in response to PO prompts. No background work, no inter-agent directions.

---

## **1\) Doctrine of FIRE (what never changes)**

* **Truth \> speed.** If it isn’t reproducible, it isn’t done.  
* **Proposal before code.** Every change starts with a **CRD** and explicit **ASK OK**.  
* **One owner, one intent.** **WIP ≤ 1** per lane; deliver strictly in dependency order.  
* **Small, reversible moves.** Keep diffs surgical; rollback is a **single revert**.  
* **Determinism as a gate.** Byte-stable artifacts; one canonical serializer (UTF-8, sorted keys, compact, **exactly one trailing `\n`**).  
* **Programmatic config only.** Runtime env \= **secrets/coords/SAFE\_MODE** (SAFE\_MODE default **OFF**, owner \+ sunset).  
* **Local gates, not cloud CI.** Evidence is captured **in-repo** and visible in the **repo dump**.

**Current sizing pins (by PO):** Core ≤ **700 LOC** per card; total (incl. tests/docs/tools) ≤ **2,000 LOC** when justified. Smaller is better.

---

## **2\) Roles & Decision Rights (AI-friendly RACI)**

* **Owner (implementer):** Writes CRD → awaits ASK OK → codes exactly the plan → runs gates → prepares closeout notes (paths \+ commands).  
* **Lead/Reviewer (FSG/Dev Lead):** Redlines/approves CRDs; enforces standards and reversibility.  
* **PO:** Only human reviewer; runs end-of-card **repo dump**; may request mid-card audit. Updates docs **after acceptance** (Doc-Delta rule).

---

## **3\) Lifecycle: TBCACT+3 (every card)**

**T — Task**

* One-sentence **Cup** (goal), exact scope, non-goals, binary acceptance, LOC cap, dependencies, named artifacts.

**B — Build Plan (in the CRD)**

* Diff summary (\~LOC, paths), risk & rollback, validation plan (tests/schemas/determinism), smoke plan, evidence list.

**C — CRD (Ask to proceed)**

* Owner requests **ASK OK**. Reviewer replies **ASK OK** or **redlines** (line-items only).

**A — Apply (code)**

* Implement **only** the approved plan; stay within cap; no new runtime flags.

**C — Commit**

* One revert-friendly commit (squash ok). Message: `feat(scope): <CARD-ID> <subject>`.

**T — Test (local gates)**

* One command runs lint/type/tests, schema checks, determinism probes, **smoke tests**. Artifacts land under `artifacts/` with byte-stable output and **LF** termination.

**\+3 — Close Evidence, Sync, Optional SE**

1. Evidence pack (in repo): gate logs, hashes, header snapshots, golden results.  
2. SYNC line (in notes): `YYYY-MM-DDThh:mm:ssZ card=<ID> commit=<sha> result=SANITY: OK note="<short>"`.  
3. If surface changed: PO-run **smoke/SE** captured in repo (see §6).

---

## **4\) Pre-Session & End-of-Card Audits (truth windows)**

* **Pre-Session Audit (mandatory):**  
  * Ask PO for **latest repo dump** and **HEAD SHA**.  
  * Read structure; list **assumptions/risks** in CRD.  
  * If dump is stale, **pause** until refreshed or PO grants exception.  
* **End-of-Card Audit (mandatory):**  
  * PO runs the **repo dump**. This is the **single evidence channel**.  
  * Implementer references artifacts by **path** \+ **command**; do **not** paste code that already exists in repo.

---

## **5\) Determinism & Integrity (make the fire steady)**

* **Serializer:** One canonical path for public bytes & artifacts (UTF-8, sorted keys, compact, **one trailing `\n`**).  
* **Two-run identity:** Relevant artifacts hashed twice → **identical** (`sha256`).  
* **Hash coupling (when applicable):** `idempotence_hash == sha256(public_success_bytes_without_hash)`; admin/debug excluded.  
* **No nondeterministic sources** in outputs: no wall clock, hostnames, random seeds in visible bytes.  
* **File integrity:** Include `.sha256` sidecars for key artifacts; list tool versions in `artifacts/sanity.txt`.

---

## **6\) Smoke Tests (must exist in-repo; no CI required)**

Minimal, fast checks captured as artifacts and run locally:

* **Write→Read reflection:** one safe writer returns **204** (or 200+no-store) then one reader shows the change. Save headers & small JSON tails.  
* **Conditional GET:** 200 with expected headers → repeat GET with `If-None-Match` → **304 empty body**; header snapshot only.  
* **DB hygiene (when writers present):** JSONB mutation persists (prefer Postgres test).  
* **Serializer newline:** Representative artifact ends with **exactly one LF**.

Smoke outputs live in `artifacts/smoke/…` (byte-stable, small, redacted).

---

## **7\) Evidence & Gate Script Conventions**

* **Sanity gate:** `scripts/make_sanity.sh` → writes `artifacts/sanity.txt` ending `SANITY: OK`.  
* **Determinism gate:** emits `artifacts/determinism.txt` with pass/fail and hashes.  
* **Header snapshots:** `artifacts/headers/{reader_200.txt, reader_304.txt}` (no bodies for 304).

**Failure format (stderr):**  
 {"error":{"code":"GATE\_FAIL","message":"\<what failed\>","details":{"hint":"\<how to fix\>"}}}

* 

---

## **8\) Communication Rules (token-honest)**

* Do **not** reference CI, PRs, bots, or peer approvals.  
* Do **not** promise background work or direct other agents.  
* In chat: provide **paths \+ commands \+ expected tails**. The **repo dump** holds code and full outputs.

---

## **9\) Incident & Hotfix Protocol (smallest flame possible)**

1. **Freeze** affected surface.  
2. Open **HF--** with a *single, reversible* change.  
3. Reproduce with a test (Postgres if persistence).  
4. Fix → run gates → smoke.  
5. Post a 5-bullet note: cause, blast radius, detection gap, fix, prevention.  
    **Golden rule:** the fix is **no larger** than the diff that broke it.

---

## **10\) Anti-Patterns (extinguish on sight)**

* Coding without a CRD/ASK OK.  
* Runtime feature flags for product behavior.  
* Multi-intent “mega-cards”.  
* Unstable artifacts (no LF, unsorted keys, timestamps).  
* Writers that hydrate the UI or emit cacheable bodies.  
* Depending on SQLite semantics when prod uses Postgres.  
* Pretending team workflows exist (PRs/CI/review queues).

---

## **11\) Checklists (clip-and-run)**

**ASK-OK readiness**

* \[ \] Single intent, LOC cap, non-goals clear  
* \[ \] Rollback \= single revert  
* \[ \] Gates & smoke defined (paths/commands)  
* \[ \] Pre-session audit received (repo dump \+ HEAD SHA)

**Before commit**

* \[ \] Matches CRD exactly (no “bonus” edits)  
* \[ \] Gates green; artifacts byte-stable (LF)  
* \[ \] Error envelopes & rate limits consistent

**Close**

* \[ \] Commands & artifact paths documented  
* \[ \] SYNC line prepared  
* \[ \] PO repo dump produced; SHA noted

---

## **12\) Templates (paste-ready)**

### **A) CRD**

\# CRD — \<CARD-ID\> · \<Short Title\>

Owner: \<name\> · Lane: FE|BE|Engine · LOC cap: ≤\<N\> · WIP: 1

Cup (one line): \<what changes, why it matters\>

Scope (in/out):

\- In: \<files, behaviors, data\>

\- Out: \<explicitly not included\>

Diff summary:

\- \<path\> (new|mod, \~LOC)

Risk & rollback:

\- Risk: LOW|MED|HIGH (\<why\>)

\- Rollback: single revert of this commit

Validation plan (local gates):

\- Lint/type/tests: \<cmd\>

\- Schema/contract: \<cmd\>

\- Determinism: \<cmd\> (expect: two hashes equal)

\- Smoke: \<cmds\> (expect: 204 then visible change; 200→304 headers)

Artifacts to produce:

\- artifacts/sanity.txt (tail: SANITY: OK)

\- artifacts/determinism.txt

\- artifacts/headers/reader\_{200,304}.txt

\- artifacts/smoke/\<name\>.txt

Pre-session audit:

\- Repo dump date: \<UTC\> · HEAD: \<sha7\>

\- Assumptions/risks: \<bullets\>

ASK: May I implement \<CARD-ID\> as proposed?

### **B) Session Report (close)**

Card: \<CARD-ID\> · Commit: \<sha7\> \<subject\>

Changed: \<1–3 bullets\>

Why: \<spec/canon reference\>

Gates: ruff/mypy/pytest: PASS · SANITY: OK · determinism: PASS

Artifacts: 

\- artifacts/…

SYNC: YYYY-MM-DDThh:mm:ssZ card=\<ID\> commit=\<sha7\> result=SANITY: OK note="\<short\>"

### **C) Hotfix Card**

\# HF-\<date\>-\<slug\> — Hotfix: \<one-liner\>

Symptom: \<evidence\>

Hypothesis: \<root cause\>

Fix (narrow): \<file/line\>; \+ regression test

Acceptance: repro→fixed; gates green; smoke clean

Rollback: single revert

---

## **13\) Why FIRE works**

FIRE burns away ambiguity and vanity. What remains is **truth**: a proposal everyone can read, a small reversible diff, byte-stable evidence, and a single human audit via repo dump. No ceremony for its own sake—only artifacts that prove reality.

# **Chapter 2 — LAKE: The Single, Calm Surface**

*Water is love. After FIRE has purified, LAKE dissolves everything that isn’t essential and presents one serene truth for the product, the team, and the user.*

---

## **0\) Promise & Posture**

* **Promise:** A single, peaceful source of truth the app can dip into—predictable, private, and stable.  
* **Posture:** One canonical reader, very few writers, strict caching, and byte-stable outputs. No GitHub CI/PR assumptions; proofs live in the repo and PO’s end-of-card dump.

---

## **1\) The Lake Covenant (non-negotiables)**

* **One reader only:** `GET /api/auth/me` is the canonical surface for SPA state.  
* **Few, gentle writers:** Minimal, idempotent, narrowly scoped; never return state for UI hydration.  
* **Refetch discipline:** After any successful write, the SPA **refetches** the reader and renders from it. No optimistic UI.  
* **Determinism:** Public bytes come from a single serializer (UTF-8, sorted keys, compact, exactly one trailing `\n`).  
* **Programmatic config:** Behavior is generated at build time from versioned JSON (registries, cutpoints). Runtime env \= secrets/coords/SAFE\_MODE (OFF by default, with owner \+ sunset).  
* **Privacy first:** Public payloads are **numeric-free** and human-safe; uncertainty stays internal.

---

## **2\) Reader (the lake itself)**

**Contract:** A small, stable JSON with everything the SPA needs to render and nothing more.

**Required properties (public “matching” slice):**

* `reader_version: "v1"` (stable contract label)  
* `eligible: <bool>`  
* `categories: [{id, band, (optional) prompt}]` — a **set** with a **stable order** (sort by `id`)  
* `release_id: <sha256>` — identity of the frozen engine pack (proof label)  
* `idempotence_hash: <sha256>` — identity of the public bytes (see §5)  
* `meta: { engine_tag, invocation_tag }` — human tag \+ request token (no secrets)

**Must not include:** raw scores, internal gates/channels, WHY traces, PII, or debug numerics.

**Versioning:** Only bump `reader_version` when SPA-observable behavior changes. `engine_tag` is human-readable; SPA must not branch on it.

---

## **3\) Caching & Transport (so the water stays still)**

* **Reader-only ETag:**  
  * `ETag: <idempotence_hash>` on **200 OK** reader responses.  
  * Include `Vary: Authorization, Accept-Encoding`.  
  * Include `Cache-Control: private, no-cache, must-revalidate`.  
* **Conditional GET:** Client sends `If-None-Match`. If it matches the current ETag → **304 Not Modified** with **empty body**; SPA reuses cached JSON.  
* **No ETag anywhere else:** Writers and error responses never emit ETag.  
* **Server cache key:** Where server caching exists, the key includes `(user_id, fpA, fpB, release_id)`—never share on hash alone.

---

## **4\) Writers (the gentle inlets)**

* **Shape:** Strict validation; reject unknowns or ignore by contract (be explicit).  
* **Responses:** Prefer **204 No Content** (or minimal **200 {"ok":true}**) with `Cache-Control: no-store`.  
* **Refetch rule:** SPA **never** hydrates from write bodies; it **always** refetches the reader.  
* **Error envelope:** `{ "ok": false, "code": "<code>", "error": "<human>" }` and for 429 include `retry_after_ms`.  
* **Guards:** Per-user/IP rate limits; CSRF rotate-and-retry once on 403; duplicate-route guard at boot in non-prod.

---

## **5\) Determinism & Identity (the clarity test)**

* **Serializer discipline:** UTF-8, sorted keys, compact separators, **exactly one trailing newline**.  
* **AB↔BA parity:** Public bytes (and `idempotence_hash`) are identical regardless of pair order.  
* **Hash coupling:**  
  * Compute `idempotence_hash = sha256(public_success_bytes_without_hash)`.  
  * Insert the hash, emit the bytes.  
  * Never include admin/debug fields in the hash input.  
* **Release identity:** `release_id = sha256(frozen pack)` (explicit allow-list in a stable order). Public exposes the label; proofs live in artifacts.

---

## **6\) Privacy & Language (human safety)**

* Public text is **neutral and supportive**; no internal jargon or numeric magnitudes.  
* **Prompt** (if present) is short, single-line, and human-safe; suppression rules apply when uncertainty is high.  
* Logs are **keys-only** (no PII, no bodies, no secrets). Correlation IDs on every request.

---

## **7\) Frontend Responsibilities (rest into the lake)**

* Use **only** the reader for page state.  
* After any successful writer, **await** the reader refetch before rendering.  
* Send `If-None-Match` on reader GETs; on **304**, reuse cached JSON.  
* Do not introduce public runtime flags (`VITE_*`, `NEXT_PUBLIC_*`).  
* Treat unknown reader fields as ignorable; UI remains numeric-free.

---

## **8\) Backend Responsibilities (hold the shoreline)**

* Enforce the reader contract and serializer discipline; compute and attach ETag on **200** only; implement **304** path with empty body.  
* Ensure writers and error responses **never** emit ETag.  
* Keep error envelopes canonical; validate inputs against programmatic constants.  
* Persistence hygiene: Postgres JSONB with `MutableDict` or `flag_modified`; include at least one Postgres test when writers exist.

---

## **9\) Observability (quiet confidence)**

* **Counters:** reader\_success\_total, reader\_error\_total{code}, reader\_latency\_ms (p50/p95).  
* **Header snapshots:** store reader 200/304 headers as small artifacts; never store 304 bodies.  
* **Smoke (staging/prod):** one safe writer → reader refetch expectation; fail noisy if not reflected.

---

## **10\) Change Control (safe evolution)**

* Any change to reader shape/behavior or writer semantics requires:  
  1. **CRD** with binary acceptance,  
  2. Updated tests/goldens and determinism checks,  
  3. Doc-Delta applied **after** acceptance, based on what shipped.

---

## **11\) Checklists (gold standard)**

**Reader readiness**

* \[ \] Numeric-free; stable schema; `reader_version` pinned  
* \[ \] ETag on 200; `Vary` \+ `Cache-Control` set; 304 empty body  
* \[ \] `idempotence_hash` equals sha256(public bytes) (LF terminator)  
* \[ \] AB↔BA parity proven; header snapshots stored

**Writer readiness**

* \[ \] 204 (or minimal 200\) \+ `no-store`; strict validation  
* \[ \] No ETag; canonical error envelopes; rate limits & CSRF posture  
* \[ \] Postgres JSONB mutation persists in test; duplicate-route guard on

**FE discipline**

* \[ \] Uses only the reader for state  
* \[ \] Sends `If-None-Match`; reuses cached JSON on 304  
* \[ \] Refetches reader after writes; no public runtime flags

---

## **12\) Anti-patterns (turn a swamp back into a lake)**

* Multiple readers or diverging “partial state” endpoints  
* Hydrating UI from writer bodies  
* Emitting ETag on writers or error responses  
* Public numerics, gates/channels, or internal jargon in the reader  
* Runtime feature flags driving product behavior  
* Unstable serialization (no sort, missing LF, timestamps in bodies)

---

## **13\) Why LAKE works**

LAKE dissolves noise and leaves only essence: one calm surface, few disciplined inlets, stable bytes, and gentle caching. The result is a product that feels safe and clear—peaceful to use, easy to reason about, and simple to evolve. Water is love, and the lake keeps that love unclouded.

# Chapter 3 — AIR: Architecture & Modularity (Redraft)

How we shape and evolve systems: clear layers, crisp contracts, deterministic cores, and change‑safe extensions. AIR is project‑agnostic and encodes our policies from LAKE (surface discipline) and FIRE (delivery ritual). Lift these patterns into any stack.

---

## 1\) Core doctrine (why AIR exists)

* Layer by responsibility, not tech. Separate the Surface (readers/writers), Application (orchestration), and Deterministic Engines (pure rules/math).  
* Contracts‑first. Every cross‑layer boundary is a documented contract (schema \+ invariants) with tests. Implementation is an internal detail.  
* Determinism at the core. Engines are pure, time‑independent, byte‑stable. Sorting/rounding are explicit; public surfaces never leak debug numerics.  
* Programmatic config \> runtime flags. Generate typed constants at build time from versioned JSON. Runtime env is secrets/coordinates and an optional global kill‑switch only.  
* Versioned namespaces. Breaking changes get a new namespace (`/v2`), not a silent remodel of `v1`.  
* Small, reversible increments. Modules ship independently with a rollback plan.  
* Minimize coupling; prefer composition. Data flows forward; side‑effects are localized and observable.

---

## 2\) Layering model (three‑tier anatomy)

### A) Surface Layer (LAKE)

What it does: Exposes stable reads; accepts minimal writes.

Rules

* One canonical reader (e.g., `GET /api/auth/me`); versioned shape; numeric‑free if policy requires.  
* Writers: minimal, idempotent; `204 No Content` (or `200 {"ok":true}`) with `Cache-Control: no-store`; SPA never hydrates UI from mutation bodies—always refetch the reader.  
* Caching: Reader `200` includes `ETag: <idempotence_hash>` and `Vary: Authorization`; honor `If-None-Match` → `304` (empty body). No ETag on writers/errors.  
* Observability: typed errors, correlation IDs, rate limits, CSRF rotate+retry.

### B) Application Layer

What it does: Orchestrates flows, validation, caching, and authZ; composes results for the surface.

Rules

* Import engines through a stable façade (e.g., `engine/<domain>/v1`), not concretes.  
* Enforce schema validation on inbound/outbound contracts; reject unknown/rogue fields.  
* Use programmatic config: generate enums/cutpoints/thresholds from JSON \+ schema at build time.  
* Provide in‑proc cache wrappers with deterministic keys (include user identity, pair fingerprints, release identity), never share across users.

### C) Deterministic Engines

What they do: Pure functions transforming normalized inputs into decisions/bands.

Rules

* Pure: no network, filesystem, or wall clocks; no global mutable state.  
* Stable serialization for public bytes and artifacts (UTF‑8, sorted keys, compact separators, exactly one trailing `\n`).  
* Versioned modules (e.g., `core/ops/v1`, `core/scoring/v1`); deprecate via new namespaces.  
* Release identity (see §6) embedded in proof artifacts; exposed publicly only as a human tag where appropriate.

---

## 3\) Contracts & schemas (how we prevent drift)

* JSON Schema per contract under `/schemas`; validate in tests and sanity.  
* Registry as source of truth for fields/enums under `/docs/registry`; build fails if references drift.  
* Programmatic generation (build‑time)  
  * FE: generate `src/types/*` from registry JSON.  
  * BE: generate constants/enums modules from registry JSON.  
  * Engine: load freeze packs (catalogs, weights) from checked‑in JSON; hard‑fail on unknown IDs.

Template: contract descriptor

{  
  "schema": "public\_payload\_v1",  
  "version": "1.0.0",  
  "fields": \["eligible","categories","prompt","meta.engine\_tag"\],  
  "invariants": \[  
    "categories\[\].band ∈ {Cool,Open,Warm,Glow}",  
    "no numerics in public payload",  
    "stable sort order for arrays explicitly defined"  
  \]  
}

---

## 4\) Namespacing & versioning (how we change safely)

* Versioned directories: `app/engine/<domain>/v1/*`; façade re‑exports the active version.  
* No breaking changes in place. Bump to `v2` when contracts break; keep `v1` shim until migration completes.  
* Human tag vs identity fuse: public includes `engine_tag` (human alias). Deterministic identity (fuse, checksums) is internal proofing and ops only.

---

## 5\) Configuration posture (no flag sprawl)

* Programmatic config (default): registries, catalogs, thresholds, bands, penalty maps as JSON \+ schema; small build scripts generate typed constants for FE/BE/engine.  
* Runtime env (minimal): secrets/keys; deployment coordinates; an optional global `SAFE_MODE` kill‑switch with removal plan.  
* Guards: boot‑time env sanity fails closed on disallowed keys (e.g., `VITE_*`, `NEXT_PUBLIC_*`).  
* Temporary flags (exceptional): default OFF, have owner \+ sunset, removed next sprint.

---

## 6\) Determinism & release identity (proofs, not inputs)

Why: anyone should re‑run and get the same bytes.

* Serializer: one canonical implementation for public bytes and artifacts (UTF‑8, sorted keys, compact, single trailing `\n`).  
* Hash coupling (when applicable): `idempotence_hash = sha256(public_success_envelope_bytes_without_hash)`; `_admin_debug` is excluded.  
* AB↔BA parity: public bytes identical regardless of pair order; normalize ordering (e.g., sort categories by `id`).  
* Two‑run identity: gate scripts emit the same bytes (and sha256) twice in a row.  
* Checksums as evidence: compute checksums over allow‑listed canon files; publish proof artifacts (e.g., `CANON_CHECKSUMS.json`) but never feed proofs back into release identity.

---

## 7\) Data & persistence patterns

* JSONB: prefer `MutableDict.as_mutable(JSONB)` and non‑null defaults; call `flag_modified` if mutating in place without `MutableDict`.  
* Idempotent writers: setting a value to the existing value returns 204; avoid noisy writes; add uniqueness where identity applies.  
* Migrations: small, reversible, testable; zero downtime.  
* Normalization: canonicalize IDs at the edge (zero‑pad, ASCII separators); reject on schema mismatch.

---

## 8\) API design patterns (lake‑true)

* Readers: one canonical reader; stable, versioned, and minimal; neutral copy; numeric‑free if policy requires.  
* Writers: strict validation; reject unknown keys or ignore by contract (be explicit); respond `204` or minimal `200` and always `no-store`.  
* Caching: Reader `200` has `ETag` (= `idempotence_hash`); `If-None-Match` → `304` empty body; no ETag on writers/errors/ops.  
* Errors: `{ "error": "bad_request|unauthorized|...", "message": "..." }` consistently.

---

## 9\) Observability & internal adapters

* Logs: keys‑only (no PII/secrets); include `reader_version`, `release_id`, `meta.engine_tag`, `correlation_id`, `duration_ms`.  
* Metrics: `reader_success_total`, `reader_error_total{code}`, `reader_latency_ms` (histogram).  
* Internal adapters (ops‑only):  
  * `/internal/healthz` — liveness (no body logging).  
  * `/internal/readyz` — dependencies ready.  
  * `/internal/version` — keys: `release_id`, `engine_tag`, checksums, `invocation_tag`/sha; `Cache-Control: no-store`.  
* Guards: duplicate‑route detection at boot (non‑prod); required env sanity (set/unset only); rate limits on writers; CSRF rotate \+ single retry.  
* Prod overrides: presence of `config/overrides/*.json` or env keys matching `/(?:^|_)(OVERRIDE|TOGGLES)(?:$)/` with `APP_ENV=prod` → typed fail.

---

## 10\) Performance envelopes & budgets

* Reader p95 ≤ 200 ms; write→read p95 ≤ 400 ms (including SPA refetch discipline).  
* Engine p95 ≤ 80 ms per call; pure CPU; no I/O.  
* Payloads: public responses ≤ \~10 KB typical; gzip/brotli friendly.  
* Backpressure: 429 under load; short DB transactions; circuit breakers for downstreams.

---

## 11\) Change management & deprecation

* ADR‑lite: one paragraph per decision under `docs/ADR/` (context → decision → alternatives → impact).  
* SYNC\_LOG: each card appends one line (timestamp, card, commit, result).  
* Deprecation: announce → dual‑read/serve → cutover → remove; time‑boxed; shims carry explicit end dates.

---

## 12\) Security posture (steady‑state minimum)

* Auth boundary: clear split between browser sessions and S2S tokens; CSRF on browser writers only.  
* Input validation: schema‑based; fail closed; reject unknown fields on security‑sensitive routes.  
* Secrets: env or vault; never logged; reported as set/unset.  
* Supply chain: pin tool versions; minimal dependencies; signed artifacts when possible.

---

## 13\) Reference module layout (adaptable)

/docs/  
  ADR/…  
  registry/fields\_v1.json  
/schemas/  
  public\_payload\_v1.schema.json  
  fields\_v1.schema.json  
  freeze\_pack\_v1.schema.json  
/config/  
  policy\_v1.json  
  bands\_v1.json  
  weights\_v1.json  
  freeze\_pack\_v1.json  
/app/  
  api/                 \# surface (LAKE)  
    readers.py         \# GET /api/auth/me  
    writers.py         \# PUT /api/profile/preferences  
  services/            \# orchestration  
    engine\_facade.py   \# calls engine/\<domain\>/v1  
  generated/  
    enums.py           \# build-time from registry  
/engine/  
  \<domain\>/v1/         \# deterministic engine  
    \_\_init\_\_.py  
    ops.py  
    scoring.py  
  present/v1/presenter.py  
  why/v1/trace.py  
/scripts/  
  make\_sanity.sh  
  generate\_enums.py  
  run\_gate\_\*          \# gate scripts (canon/det/hash/etc.)  
/artifacts/  
  sanity.txt  
  determinism.txt  
  registry\_report.txt  
/audit/gates/  
  \<gate\>/\<UTC-stamp\>/ { artifacts \+ .sha256 \+ gate\_log.txt }

---

## 14\) Checklists (architect’s pocket cards)

Boundary design

* Reader payload numeric‑free (per policy); stable schema \+ tests.  
* Writers minimal; `204`/minimal `200`; `no-store` headers set; SPA refetches reader.

Engine contract

* Inputs normalized; IDs canonicalized; enums validated.  
* Outputs deterministic (sorted keys; explicit rounding; single `\n`).  
* Release fuse/tag emitted in proofs (tag only in public where appropriate).

Config discipline

* Enums/caps/thresholds generated at build time from JSON+schema.  
* No new runtime flags unless secret/coord/emergency; flags have owner/sunset.

Security & ops

* Duplicate‑route guard; env sanity prints; rate limits \+ CSRF rotate‑retry.  
* Post‑deploy smoke (writer→reader) scripted.

Testing

* Unit \+ schema; property tests for parity where applicable.  
* At least one persistence test against real DB engine (e.g., Postgres for JSONB).  
* Determinism harness for engines and public bytes.

---

## 15\) Anti‑patterns (smoke alarms)

* Runtime toggles for product behavior where programmatic config suffices.  
* Multiple handlers for the same (method, path) or unreachable code blocks.  
* Engine code branching on clocks/locales/env.  
* Public readers exposing internal jargon or raw numerics.  
* Build scripts that emit non‑stable bytes (unsorted JSON, timestamps).  
* SQLite‑only tests when production uses a different DB.

---

## 16\) AIR scorecard (0–2 each; ship ≥ 16/20)

1. Contracts‑first: schemas \+ tests in place.  
2. Deterministic core: pure functions; sorted outputs; explicit rounding; single `\n`.  
3. Programmatic config: no new runtime flags; generators in place.  
4. Boundary hygiene: lake discipline; no UI hydration from write bodies.  
5. Observability: errors, IDs, rate limits, internal adapters.  
6. Versioning: v1/v2 discipline; tag/fuse separation.  
7. Security: CSRF/rate limits; PII‑free logs.  
8. Rollback: small diff; single‑commit revert.  
9. Performance: latency/payload budgets respected.  
10. Evidence: determinism \+ sanity \+ gate artifacts ready.

---

### Why this chapter works

AIR limits surprise. It codifies how we segment responsibilities, freeze contracts, and evolve safely—without flag sprawl or ambiguity about ownership. Combined with LAKE and FIRE, it keeps teams fast and precise, even with single‑threaded staffing.

# **Chapter 3 — AIR: The Blue-Sky Protocol (Architecture, Data, Modularity)**

*Air is knowledge made gentle. After FIRE proves truth and LAKE presents a single calm surface, AIR holds the sky clear: data that is safe, available, precise, and scalable—without clutter, drift, or surprise.*

---

## **0\) Promise & Posture**

* **Promise:** A serene, trustworthy information system: easy to reason about, hard to break, and ready to grow.  
* **Posture:** Contracts-first, deterministic cores, programmatic config, and **No-CI / PO-only review** with **repo-dump evidence**.

---

## **1\) The Blue-Sky Doctrine (non-negotiables)**

* **Contracts above code:** Every boundary (API, queue, store, file) has a schema \+ invariants \+ tests.  
* **Deterministic cores:** Engines are pure (no I/O/time); public bytes use one serializer (UTF-8, sorted keys, compact, **exactly one trailing `\n`**).  
* **Programmatic config:** Behavior is generated at build time from versioned JSON packs (registries, cutpoints). Runtime env \= **secrets/coords** (+ optional **SAFE\_MODE OFF** with owner \+ sunset).  
* **Versioned namespaces:** Breaking changes get `/v2`—never silent remodels.  
* **Small, reversible deltas:** Rollback is a **single revert**.  
* **Privacy first:** Classify data; keep public payloads **numeric-free**; logs are **keys-only**.  
* **No GitHub CI / PR flows:** All gates run locally; **evidence is the PO’s repo dump** at card close.

---

## **2\) The AIR Model (layers & flow)**

### **A) Surface (LAKE)**

Stable reads (`GET /api/auth/me`) and minimal writers. Reader 200 emits `ETag:<idempotence_hash>`, `Vary: Authorization`, and `Cache-Control: private, no-cache, must-revalidate`. Writers/errors emit **no ETag**. SPA always refetches after writes.

### **B) Application (Orchestration)**

Validation, authZ, composition, caching. Import engines through a façade (`engine/<domain>/v1`), not concretes. Enforce schemas on ingress/egress. Deterministic cache keys include `(user_id, fpA, fpB, release_id)`; never share across users.

### **C) Deterministic Engines**

Pure functions (no network/files/clocks). AB↔BA parity; hash coupling: `idempotence_hash = sha256(public_success_bytes_without_hash)`. `release_id = sha256(frozen pack)`; `engine_tag` is human-readable only.

### **D) Data Plane (Storage & Movement)**

OLTP: Postgres (JSONB with `MutableDict` or `flag_modified`).  
 Files/artifacts: append-only, byte-stable, checksummed.  
 Eventing (optional): idempotent, schema’d messages; at-least-once consumers.

---

## **3\) Contracts & Schemas (drift prevention)**

* **Where:** `/schemas/*` (JSON Schema) and `/docs/registry/*` (fields/enums).  
* **Rules:** Closed enums; reject unknown fields where security-sensitive; explicit array ordering; neutral copy for public text.  
* **Generators:** FE types, BE constants, and engine enums are **build-time** artifacts from packs. Builds fail on schema/registry drift.

---

## **4\) Data Safety & Privacy (human protection)**

* **Classification:** `public`, `internal`, `admin`, `secret`, `PII`.  
* **Access:** Least-privilege roles; no cross-lane raw PII access by default.  
* **Encryption:** TLS in transit; disk-level at rest; secrets in env/manager (never in logs).  
* **Logging:** Keys-only; correlation ID on every request; redact tokens/bodies.  
* **Public posture:** Reader is numeric-free; prompts (when present) are short, single-line, and human-safe; suppress when uncertainty is high.

---

## **5\) Availability & Integrity (blue-sky SLOs)**

* **Budgets:** Reader p95 ≤ **200 ms**; write→read p95 ≤ **400 ms** (incl. SPA refetch).  
* **Integrity:** End-to-end checksum where practical (artifact `.sha256`, header snapshots).  
* **Backups:** Daily snapshot \+ point-in-time where supported; **monthly restore drill**; document RPO/RTO targets in `/docs/ADR/`.  
* **Smoke:** Scripted writer→reader smoke on staging/prod; fail noisy if reflection missing.

---

## **6\) Scalability & Performance (when clouds gather)**

* **Shape first:** Keep payloads ≤ \~10 KB typical; compress (gzip/brotli).  
* **Indices:** Add only with proof (EXPLAIN plans); name by contract.  
* **Hot paths:** Cache by composite key (never by hash alone); bound lifetimes; evict on `release_id` change.  
* **Load:** Rate-limit writers; short DB transactions; backpressure with 429; circuit breakers for downstreams.  
* **Growth:** Partition by tenant/user where necessary; prefer horizontal scaling over global locks.

---

## **7\) Lifecycle & Governance**

* **Retention:** Define per-table/file retention and purge schedules; automate with safe windows.  
* **Deletion:** Implement id-based erase jobs for internal/admin data; never expose destructive ops in public APIs.  
* **Lineage:** Record “who wrote what and why” via SYNC\_LOG and minimal audit tables (keys-only).  
* **Docs:** ADR-lite (one paragraph) for each consequential decision.

---

## **8\) Observability & Audit**

* **Metrics:** `reader_success_total`, `reader_error_total{code}`, `reader_latency_ms`.  
* **Traces:** Correlation ID propagated; no payloads in spans.  
* **Evidence:** Header snapshots for reader 200/304; determinism/registry reports; all inside the **repo dump**.  
* **Alerts (minimal):** Error rate spike, p95 breach, smoke failure.

---

## **9\) Change Management & Migrations**

* **CRD → ASK OK → implement → sanity → evidence → repo dump.**  
* **Migrations:** Small, reversible; defaults/backfills; zero downtime; run in maintenance lanes; tested on Postgres (not SQLite only).  
* **Version bumps:** New `/v2` for breaking public contracts; keep `/v1` shim until cutover complete.

---

## **10\) Checklists (gold standard)**

**New/changed contract**

* \[ \] Schema \+ invariants under `/schemas/`  
* \[ \] Generators updated; builds fail on drift  
* \[ \] Tests for accept/reject; stable ordering asserted

**Engine change**

* \[ \] Pure functions; no I/O/time  
* \[ \] AB↔BA parity; two-run identity  
* \[ \] `idempotence_hash` \= sha256(public bytes without hash)  
* \[ \] `release_id` recomputed from frozen pack

**Storage/migration**

* \[ \] Reversible migration; defaults set; backfill plan  
* \[ \] Postgres test covers JSONB mutation (no SQLite masking)  
* \[ \] Index proof (EXPLAIN) \+ rollback

**Privacy & logs**

* \[ \] Data classified; PII guarded  
* \[ \] Keys-only logs; secrets redacted  
* \[ \] Public text neutral; suppression rules enforced

**Availability**

* \[ \] Reader p95 & write→read p95 within budget  
* \[ \] Header snapshots (200/304) captured  
* \[ \] Smoke script passes on staging/prod

**Process**

* \[ \] SYNC\_LOG appended; ADR-lite added  
* \[ \] Repo dump produced (authoritative evidence)

---

## **11\) Anti-patterns (wind shear)**

* Runtime flags for product behavior (use programmatic config instead)  
* Multiple handlers for the same `(method, path)`; unreachable code after returns  
* Engines branching on clocks/locales/env  
* Public readers exposing numerics, gates, or internal jargon  
* Non-stable serializers (unsorted keys, timestamps), missing LF  
* SQLite-only tests when prod is Postgres  
* CI/PR references (“wait for bot/reviewer”)—**not used in this phase**

---

## **12\) AIR Scorecard (0–2 each; ship ≥ 16/20)**

1. Contracts-first (+ tests)  
2. Deterministic cores (sorted, pure, LF)  
3. Programmatic config (no new runtime flags)  
4. Boundary hygiene (lake discipline held)  
5. Privacy posture (numeric-free public, keys-only logs)  
6. Versioning (v1/v2 discipline; tag/fuse separation)  
7. Availability (p95s met; smoke green)  
8. Migration safety (reversible, Postgres-tested)  
9. Rollback (single revert)  
10. Evidence (repo dump with headers, hashes, reports)

---

## **13\) Templates (paste-ready)**

**ADR-lite (one paragraph)**  
 *Context → Decision → Alternatives → Impact.* File under `/docs/ADR/<YYYY-MM-DD>-<slug>.md`.

**Migration plan**

* Change: \<table/column/index\>  
* Risk: \<LOW/MED/HIGH\> (why)  
* Steps: create default → backfill → flip reads → drop old  
* Reversible:  
* Tests: module::test (Postgres)

**Data-access request (internal)**

* Purpose:  
* Scope: \<tables/fields\> (no PII unless justified)  
* Retention:  
* Owner: \<person/role\>  
* Sunset:

---

### **Why AIR works**

AIR is the mind of the system: knowledge with boundaries. By insisting on contracts, determinism, privacy, and reversible change—proved locally and recorded in the repo dump—we keep the sky clear. Users experience calm; engineers move fast without breaking trust.

# **Chapter 4 — EARTH: The Green Foundation**

*Infrastructure · Ethics · Proof · Governance*

*Earth is the conjunction: FIRE’s truth and LAKE’s calm made durable; AIR’s knowledge kept safe. It’s the garden we can tend—secure, reproducible, auditable, and kind to people. This chapter defines the pins, processes, and proofs that make the system self-sustaining without GitHub CI, using PO-only review and repo-dump evidence.*

---

## **0\) Promise & Responsibility**

* **Promise:** Users entrust us with their time, attention, and data. We answer with rigor: least privilege, transparent boundaries, deterministic builds, and reversible change.  
* **Operating mode:** **No GitHub CI/PR flows.** All checks run locally; the **PO’s repo dump at card close** is the **only** code-review channel. Mid-card audit happens **only** when the PO requests it.

---

## **1\) Ethics Charter (non-negotiables)**

1. **Truth first:** no dark patterns; no hidden numerics in public payloads.  
2. **Do no harm:** minimize data; collect only what the feature needs; document retention.  
3. **Respect & consent:** clear user intent drives writes; destructive operations require explicit confirmation.  
4. **Least privilege:** every key, role, and query is scoped; PII guarded; logs are **keys-only**.  
5. **Transparency:** boundaries, versions, and contracts are documented; evidence is published in-repo.  
6. **Reversibility:** every change is roll-backable via **single revert**.

---

## **2\) Ground Covenant (cross-team invariants)**

* **Single reader (LAKE):** `GET /api/auth/me` is the canonical surface.  
* **Writers:** `204` (preferred) or `200` **with** `Cache-Control: no-store`; SPA **always refetches** the reader; **no ETag** on writers/errors.  
* **Reader caching:** 200 → `ETag: <idempotence_hash>`, `Vary: Authorization`; `If-None-Match` match → `304` **empty body**.  
* **Public payload:** numeric-free (bands, eligibility, optional short prompt) \+ `meta{engine_tag,invocation_tag}` \+ `release_id`.  
* **Determinism:** one serializer (UTF-8, sorted keys, compact, **exactly one trailing `\n`**); two-run identity; AB↔BA parity.  
* **Identity:** `idempotence_hash = sha256(public_success_bytes_without_hash)`; `release_id = sha256(frozen pack)`.  
* **Config posture:** programmatic config (generated from JSON packs). Runtime env \= **secrets/coords** \+ optional **SAFE\_MODE (OFF; owner+sunset)**.  
* **Persistence:** Postgres as DB of record; JSONB hygiene (`MutableDict` or `flag_modified`). SQLite is dev/test only.  
* **Process:** TBCACT+3; one owner; **WIP ≤ 1** per lane; **Doc-Delta after acceptance**.

---

## **3\) Environments & Topology**

* **Locales:** `local` → `staging` → `prod`. No shadow/hidden envs.  
* **Boundaries:** browser sessions vs S2S tokens; CSRF on browser writers only.  
* **Network posture:** default-deny ingress; explicit allowlists; TLS everywhere.  
* **Secrets:** injected at runtime (env/manager), never in code or logs; rotation playbook maintained.  
* **SAFE\_MODE:** optional global kill-switch (OFF by default) with owner \+ sunset; presence is logged.

---

## **4\) Reproducible Builds (no-CI discipline)**

* **Lock & pin:** language/toolchain versions and lockfiles committed.  
* **Hermetic builds:** no network at import; no clock/hostnames in build outputs.  
* **Single serializer:** used by engines, readers, and artifacts.  
* **Release fuse:** deterministic `release_id` from an **allow-listed frozen pack** (paths \+ order documented).  
* **Evidence:** hashes for artifacts, header snapshots for reader 200/304, registry reports—**all inside the repo dump**.

---

## **5\) Data Governance**

* **Classification:** `public` / `internal` / `admin` / `secret` / `PII`.  
* **Access:** role-scoped connections; read/write separation where feasible.  
* **Retention:** table/file retention matrix with owners and purge cadence; automated, logged deletes.  
* **Backups:** daily snapshot \+ PITR where supported; **monthly restore drill**; RPO/RTO pinned in `/docs/ADR/`.  
* **Deletion requests:** id-based erasure jobs for internal/admin data; public APIs never expose destructive wipes.

---

## **6\) Security Posture**

* **Inputs:** schema-validated; reject unknown fields for security-sensitive routes; canonicalize IDs (ASCII, zero-pad).  
* **Logging:** keys-only; tokens and bodies redacted; correlation ID on every request.  
* **Rates & abuse:** per-route/user/IP limits on writers; short DB transactions; 429 backpressure.  
* **Supply chain:** minimal dependencies; license scan; vendoring/pinning where prudent.

---

## **7\) Observability & Audit**

* **Metrics:** `reader_success_total`, `reader_error_total{code}`, `reader_latency_ms` (histogram).  
* **Traces:** correlation ID propagation; no payloads.  
* **Audit trails:**  
  * `artifacts/` (sanity, determinism, registry reports, header snapshots)  
  * `audit/gates/<name>/<UTC>/` (byte-stable artifacts \+ `.sha256` \+ `gate_log.txt`)  
  * `SYNC_LOG` (timestamp, card, commit, result note)  
* **Alerts (minimal, meaningful):** reader p95 breach; error-rate spike; smoke failure.

---

## **8\) Local Gates & Scripts (interfaces, not bots)**

* **Sanity runner:** lints, types, tests, schema/registry validation, determinism probes; writes `artifacts/sanity.txt` ending `SANITY: OK`.  
* **Registry validator:** rejects drift; emits deterministic `registry_report.txt`.  
* **Determinism triplet (engine):** three identical hashes in a row or fail.  
* **Route collision guard:** non-prod boot fails on (method, path) duplicates.  
* **Post-deploy smoke:** writer → reader refetch proof (staging/prod).

These scripts are part of the repo; they do **not** require CI and are executed locally. Their results are captured in the **repo dump**.

---

## **9\) Change Management (No-CI, PO-only)**

* **Lifecycle:** CRD → **ASK OK** → implement (within LOC cap) → sanity → **repo dump** → PO review → Doc-Delta.  
* **Mid-card audit:** PO may share a snapshot for targeted review; otherwise **no intermediate review** is implied.  
* **Rollback:** single revert; hotfix cards follow the **minimal diff** rule (fix no larger than the break).

---

## **10\) Availability & Performance**

* **Budgets:** Reader p95 ≤ **200 ms**; write→read p95 ≤ **400 ms** (incl. SPA refetch).  
* **Caching:** composite keys include `(user_id, fpA, fpB, release_id)`; never share on hash alone.  
* **Payloads:** public ≤ \~10 KB typical; compression enabled.  
* **Scaling:** horizontal where feasible; add indices with EXPLAIN proof; evict cache on `release_id` change.

---

## **11\) Runbooks & Drills (living muscle memory)**

* **Backup restore drill:** monthly; time to restore recorded.  
* **Secret rotation:** quarterly; verify zero downtime.  
* **Smoke on deploy:** mandatory; failure blocks promotion.  
* **Incident flow:** severity triage → repro test → narrow fix → sanity → smoke → post-incident note (cause, blast, gap, fix, prevention).

---

## **12\) Access & Autonomy Rules (agents)**

* **Act only on PO prompts.** No background tasks; no inter-agent pings; no promises of future action.  
* **Never reference CI/PR bots or peer reviews.** They do not exist here.  
* **When unsure, ask.** If context is low: post a **CONTEXT-ALERT** with a mini snapshot (role, active card, next step, gates, risks).

---

## **13\) Earth Scorecard (0–2 each; ship ≥ 16/20)**

1. Ethics & least-privilege enforced  
2. Repo-dump evidence complete & legible  
3. Deterministic builds (same bytes twice)  
4. Lake discipline honored (ETag/304; no ETag on writers)  
5. Programmatic config; no public runtime flags  
6. Postgres JSONB hygiene; SQLite not relied on  
7. Backups \+ restore drill recorded  
8. Logs keys-only; correlation IDs present  
9. Performance budgets met; smoke green  
10. Single-revert rollback plan documented

---

## **14\) Quick Checklists**

**Before starting a card**

* \[ \] CRD cites canon & versions; ethics/privacy touched if relevant  
* \[ \] LOC cap, rollback plan, acceptance gates listed

**Before calling it done**

* \[ \] Sanity runner `SANITY: OK`; determinism proofs (if engine)  
* \[ \] Header snapshots (reader 200/304) captured when applicable  
* \[ \] SYNC\_LOG appended; ADR-lite added if decisions made  
* \[ \] **Repo dump** produced and shared with PO

**Monthly maintenance**

* \[ \] Restore drill done; RPO/RTO confirmed  
* \[ \] Secret rotation status  
* \[ \] Registry/report determinism re-run

---

### **Why EARTH matters**

Earth is how we honor users: we don’t just build; we **care** for what we’ve built. With ethics as guardrails, deterministic tooling, and human-auditable proofs—delivered without external CI—we get a system that stays alive, legible, and kind. A garden, not a gadget.

Awesome—here’s a clean, copy-ready **Appendix** you can drop into the repo (e.g., `/docs/appendix/`). It’s faithful to the pins we’ve already set (Lake discipline, Reader-only ETag, numeric-free public surface, programmatic config, Postgres JSONB, no GitHub CI/PR). It’s organized so each section stands alone.

---

# **Appendix — Canonical Schemas, Patterns & Gate Scripts**

**Operating mode:** No CI/PR. All checks run locally. Evidence lives in the **repo dump** at card close. Mid-card review only if the PO requests it.

---

## **A) Reader v1 — Public JSON Schema (numeric-free)**

**Path:** `schemas/reader_public_v1.schema.json`

{  
  "$schema": "https://json-schema.org/draft/2020-12/schema",  
  "$id": "schemas/reader\_public\_v1.schema.json",  
  "title": "Reader Public Payload v1",  
  "type": "object",  
  "required": \["user", "matching"\],  
  "additionalProperties": false,  
  "properties": {  
    "user": {  
      "type": "object",  
      "required": \["id", "profile", "preferences"\],  
      "additionalProperties": true  
    },  
    "matching": {  
      "type": "object",  
      "required": \[  
        "reader\_version", "eligible", "release\_id",  
        "idempotence\_hash", "meta"  
      \],  
      "additionalProperties": false,  
      "properties": {  
        "reader\_version": { "enum": \["v1"\] },  
        "eligible": { "type": "boolean" },  
        "categories": {  
          "type": "array",  
          "items": {  
            "type": "object",  
            "required": \["id", "band"\],  
            "additionalProperties": false,  
            "properties": {  
              "id": { "type": "string", "pattern": "^\[a-z0-9\_\]+$" },  
              "band": { "enum": \["Cool","Open","Warm","Glow"\] },  
              "prompt": {  
                "type": "string",  
                "maxLength": 160,  
                "pattern": "^\[^\\n\\r\]\*$"  
              }  
            }  
          }  
        },  
        "prompt": { "type": "string", "maxLength": 160, "pattern": "^\[^\\n\\r\]\*$" },  
        "release\_id": { "type": "string", "pattern": "^\[a-f0-9\]{64}$" },  
        "idempotence\_hash": { "type": "string", "pattern": "^\[a-f0-9\]{64}$" },  
        "meta": {  
          "type": "object",  
          "required": \["engine\_tag", "invocation\_tag"\],  
          "additionalProperties": false,  
          "properties": {  
            "engine\_tag": { "type": "string", "minLength": 1 },  
            "invocation\_tag": { "type": "string", "pattern": "^INV-\[a-f0-9\]{16}$" }  
          }  
        }  
      }  
    }  
  }  
}

---

## **B) Canonical Serializer & Hash Coupling (Python)**

**Paths:**

* `app/lib/sercanon.py` — single source of truth  
* `tests/lib/test_sercanon.py` — determinism tests

\# app/lib/sercanon.py  
import json, hashlib  
from typing import Any, Dict

\# Stable JSON: UTF-8, sorted keys, compact, exactly ONE trailing LF.  
def dumps\_public(obj: Any) \-\> bytes:  
    s \= json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",", ":"))  
    return (s \+ "\\n").encode("utf-8")

\# Hash over PUBLIC BYTES \*\*EXCLUDING\*\* the 'idempotence\_hash' field to avoid recursion.  
\# Caller constructs the envelope without the hash, computes it, then inserts it.  
def idempotence\_hash(public\_without\_hash: Dict\[str, Any\]) \-\> str:  
    b \= dumps\_public(public\_without\_hash)  
    return hashlib.sha256(b).hexdigest()

\# tests/lib/test\_sercanon.py  
from app.lib.sercanon import dumps\_public, idempotence\_hash

def test\_dumps\_public\_trailing\_lf():  
    b \= dumps\_public({"a": 1})  
    assert b.endswith(b"\\n")  
    assert b.count(b"\\n") \== 1

def test\_idempotence\_hash\_stable():  
    obj \= {"x": 1, "y": {"a": 2}}  
    h1 \= idempotence\_hash(obj)  
    h2 \= idempotence\_hash({"y": {"a": 2}, "x": 1})  \# key reorder  
    assert h1 \== h2  
    assert len(h1) \== 64 and all(c in "0123456789abcdef" for c in h1)

---

## **C) Reader Adapter — ETag & 304 (Flask)**

**Paths:**

* `app/api/readers.py`  
* `tests/api/test_reader_etag.py`

\# app/api/readers.py  
from flask import Blueprint, g, make\_response, request  
from app.present.reader\_v1 import emit\_public \# returns dict WITHOUT idempotence\_hash  
from app.lib.sercanon import dumps\_public, idempotence\_hash

bp \= Blueprint("readers", \_\_name\_\_, url\_prefix="/api")

@bp.get("/auth/me")  
def reader\_v1():  
    \# Domain build (internal)  
    public\_wo \= emit\_public(g.user\_id)      \# dict without the 'idempotence\_hash' key  
    etag \= idempotence\_hash(public\_wo)  
    inm \= request.headers.get("If-None-Match")  
    if inm \== etag:  
        \# Conditional GET: 304, empty body  
        resp \= make\_response("", 304\)  
        resp.headers\["ETag"\] \= etag  
        resp.headers\["Vary"\] \= "Authorization"  
        resp.headers\["Cache-Control"\] \= "private, no-cache, must-revalidate"  
        return resp

    public \= dict(public\_wo, idempotence\_hash=etag)  
    body \= dumps\_public({"user": build\_user(g.user\_id), "matching": public})  
    resp \= make\_response(body, 200\)  
    resp.mimetype \= "application/json"  
    resp.headers\["ETag"\] \= etag  
    resp.headers\["Vary"\] \= "Authorization"  
    resp.headers\["Cache-Control"\] \= "private, no-cache, must-revalidate"  
    return resp

def build\_user(user\_id):  \# minimal placeholder (kept small & boring)  
    return {"id": f"u\_{user\_id}", "profile": {}, "preferences": {}}

\# tests/api/test\_reader\_etag.py  
def test\_reader\_200\_has\_etag\_and\_headers(client, authed):  
    r \= client.get("/api/auth/me")  
    assert r.status\_code \== 200  
    assert "ETag" in r.headers  
    assert "Authorization" in r.headers.get("Vary", "")  
    assert "private" in r.headers.get("Cache-Control", "")

def test\_reader\_304\_empty\_body(client, authed):  
    r1 \= client.get("/api/auth/me")  
    etag \= r1.headers\["ETag"\]  
    r2 \= client.get("/api/auth/me", headers={"If-None-Match": etag})  
    assert r2.status\_code \== 304  
    assert r2.data \== b""  
    assert r2.headers\["ETag"\] \== etag

def test\_writers\_no\_etag(client, authed):  
    w \= client.put("/api/profile/preferences", json={"preferred\_pace":"fast"})  
    assert w.status\_code in (200,204)  
    assert "ETag" not in w.headers

---

## **D) Writers — JSONB Hygiene (SQLAlchemy \+ Postgres)**

**Paths:**

* `app/models/preferences.py`  
* `app/api/writers.py`  
* `tests/api/test_writer_preferences.py`

\# app/models/preferences.py  
from sqlalchemy.dialects.postgresql import JSONB  
from sqlalchemy.ext.mutable import MutableDict  
from app.db import db

class UserPreferences(db.Model):  
    \_\_tablename\_\_ \= "user\_preferences"  
    user\_id \= db.Column(db.Integer, primary\_key=True)  
    prefs   \= db.Column(MutableDict.as\_mutable(JSONB), nullable=False, server\_default="{}")

\# app/api/writers.py  
from flask import Blueprint, g, request, make\_response  
from app.models.preferences import UserPreferences  
from app.db import db  
from app.middleware.errors import error\_response  
from app.generated.enums import PREFERRED\_PACE

bp \= Blueprint("writers", \_\_name\_\_, url\_prefix="/api")

@bp.put("/profile/preferences")  
def update\_preferences():  
    if not getattr(g, "user\_id", None):  
        return error\_response(401, "unauthorized", "auth required")  
    payload \= request.get\_json(silent=True) or {}  
    pace \= payload.get("preferred\_pace")  
    if pace not in set(PREFERRED\_PACE):  
        return error\_response(400, "bad\_request", "preferred\_pace invalid")  
    with db.session.begin():  
        prefs \= db.session.get(UserPreferences, g.user\_id) or UserPreferences(user\_id=g.user\_id, prefs={})  
        prefs.prefs\["preferred\_pace"\] \= pace  
        db.session.add(prefs)  
    resp \= make\_response("", 204\)  
    resp.headers\["Cache-Control"\] \= "no-store"  
    return resp

\# tests/api/test\_writer\_preferences.py  
from sqlalchemy import select  
from app.models.preferences import UserPreferences

def test\_writer\_204\_and\_persists(client, authed, session):  
    r \= client.put("/api/profile/preferences", json={"preferred\_pace":"fast"})  
    assert r.status\_code \== 204  
    assert r.headers.get("Cache-Control") \== "no-store"  
    row \= session.execute(select(UserPreferences).where(UserPreferences.user\_id==authed.id)).scalar\_one()  
    assert row.prefs.get("preferred\_pace") \== "fast"

---

## **E) Error Envelope & Correlation ID**

**Paths:**

* `app/middleware/errors.py`  
* `app/middleware/correlation.py`

\# app/middleware/errors.py  
from flask import jsonify

def error\_response(code: int, err: str, msg: str, \*\*extra):  
    body \= {"ok": False, "code": err, "error": msg}  
    body.update(extra)  
    resp \= jsonify(body)  
    resp.status\_code \= code  
    return resp

\# app/middleware/correlation.py  
import uuid  
from flask import g, request

def install\_correlation(app):  
    @app.before\_request  
    def \_inject():  
        g.correlation\_id \= request.headers.get("X-Correlation-ID") or str(uuid.uuid4())

---

## **F) FE (React) Reader Wrapper — Conditional GET**

**Path:** `src/lib/reader.ts`

// src/lib/reader.ts  
type Matching \= {  
  reader\_version: "v1";  
  eligible: boolean;  
  categories?: { id: string; band: "Cool"|"Open"|"Warm"|"Glow"; prompt?: string }\[\];  
  prompt?: string;  
  release\_id: string;  
  idempotence\_hash: string;  
  meta: { engine\_tag: string; invocation\_tag: string };  
};

type Reader \= { user: any; matching: Matching };

const etagCache \= new Map\<string, { etag: string; json: Reader }\>();

export async function fetchReader(authToken: string): Promise\<Reader\> {  
  const key \= "auth\_me"; // SPA has a single reader  
  const cached \= etagCache.get(key);  
  const headers: Record\<string,string\> \= { "Authorization": \`Bearer ${authToken}\` };  
  if (cached?.etag) headers\["If-None-Match"\] \= cached.etag;

  const r \= await fetch("/api/auth/me", { method: "GET", headers, credentials: "include" });  
  if (r.status \=== 304 && cached) return cached.json;

  if (\!r.ok) throw new Error(\`Reader failed: ${r.status}\`);  
  const etag \= r.headers.get("ETag") || "";  
  const json: Reader \= await r.json();  
  etagCache.set(key, { etag, json });  
  return json;  
}

**FE rules:** never render from writer bodies; after a successful write, call `fetchReader()` and re-render. No `VITE_*`/`NEXT_PUBLIC_*` product flags.

---

## **G) Programmatic Config (Generator)**

**Paths:**

* `docs/registry/fields_v1.json` (authoritative)  
* `scripts/generate_enums.py`  
* `app/generated/enums.py` (generated)

\# scripts/generate\_enums.py  
import json, pathlib, sys  
REG \= pathlib.Path("docs/registry/fields\_v1.json")  
OUT \= pathlib.Path("app/generated/enums.py")

def main():  
    reg \= json.loads(REG.read\_text("utf-8"))  
    pace \= next(x for x in reg if x\["id"\] \== "preferred\_pace")  
    allowed \= sorted(pace.get("enum", \[\]))  
    body \= (  
        "\# generated; DO NOT EDIT\\n"  
        "PREFERRED\_PACE \= (" \+ ", ".join(repr(x) for x in allowed) \+ ",)\\n"  
    )  
    OUT.write\_text(body, "utf-8")

if \_\_name\_\_ \== "\_\_main\_\_":  
    sys.exit(main())

---

## **H) Sanity Runner & Gate Stubs (No-CI)**

**Paths:**

* `scripts/make_sanity.sh`  
* `scripts/run_gate_reader.sh`  
* `artifacts/` (outputs)

\#\!/usr/bin/env bash  
\# scripts/make\_sanity.sh  
set \-euo pipefail  
mkdir \-p artifacts  
echo "== Ruff \==" && ruff .          | tee artifacts/ruff.txt  
echo "== Mypy \==" && mypy .          | tee artifacts/mypy.txt  
echo "== Pytest \==" && pytest \-q     | tee artifacts/pytest.txt  
python3 scripts/generate\_enums.py  
echo "SANITY: OK" | tee artifacts/sanity.txt

\#\!/usr/bin/env bash  
\# scripts/run\_gate\_reader.sh  
set \-euo pipefail  
STAMP=$(date \-u \+"%Y%m%dT%H%M%SZ")  
OUT="audit/gates/reader/$STAMP"  
mkdir \-p "$OUT"  
\# Snapshot reader headers (200)  
curl \-sS \-D "$OUT/reader\_200.headers.txt" \-o /dev/null \\  
  \-H "Authorization: Bearer $TOKEN" https://\<host\>/api/auth/me  
\# Conditional GET to prove 304  
ETAG=$(grep \-i '^ETag:' "$OUT/reader\_200.headers.txt" | awk '{print $2}' | tr \-d '\\r')  
curl \-sS \-D "$OUT/reader\_304.headers.txt" \-o /dev/null \\  
  \-H "Authorization: Bearer $TOKEN" \-H "If-None-Match: $ETAG" https://\<host\>/api/auth/me  
echo "READER\_GATE: OK" | tee "$OUT/gate\_log.txt"

---

## **I) Optional Server Cache (e.g., Redis) — Composite Keys**

**Use only if explicitly required.** Keys MUST include `(user_id, fpA, fpB, release_id)`. Never share by hash alone.

**Path:** `app/cache/reader_cache.py`

def reader\_cache\_key(user\_id: int, fpA: str, fpB: str, release\_id: str) \-\> str:  
    return f"reader:v1:u:{user\_id}:a:{fpA}:b:{fpB}:r:{release\_id}"

---

## **J) Post-Deploy Smoke (PUT → GET)**

**Path:** `scripts/post_deploy_smoke.sh`

\#\!/usr/bin/env bash  
set \-euo pipefail  
curl \-fsS \-X PUT \-H "Content-Type: application/json" \\  
  \-H "Authorization: Bearer $TOKEN" \\  
  \-d '{"preferred\_pace":"fast"}' https://\<host\>/api/profile/preferences \\  
  \-D /tmp/smoke\_put.h \-o /dev/null  
curl \-fsS \-H "Authorization: Bearer $TOKEN" \\  
  https://\<host\>/api/auth/me | jq '.user.preferences.preferred\_pace' | grep \-q '"fast"'  
echo "SMOKE: OK"

---

## **K) Repo Dump Manifest (evidence index)**

**Path:** `artifacts/repo_dump_manifest.json` (generated by your dump script)

{  
  "card\_id": "CORE-XXXX-YYY",  
  "commit": "\<sha7\>",  
  "generated\_at": "2025-09-27T12:34:56Z",  
  "files": \[  
    {"path":"app/api/readers.py","bytes":1234,"sha256":"..."},  
    {"path":"schemas/reader\_public\_v1.schema.json","bytes":2048,"sha256":"..."}  
  \],  
  "gates": {  
    "sanity": "SANITY: OK",  
    "reader": "READER\_GATE: OK"  
  },  
  "notes": "Evidence is authoritative in this dump."  
}

---

## **L) Rate Limits & CSRF (BE)**

**Path:** `app/middleware/rate_limit.py` (illustrative stub)

\# Keep simple & explicit; tune per route.  
WINDOW\_S \= 60  
MAX\_PER\_WINDOW \= 30  
\# Implement with Redis or in-DB counters only if required; otherwise document limits and audit manually.

Browser writers: on **403 CSRF**, refresh token once and retry exactly once; else show a clear error to the user. (FE implements; BE returns typed errors.)

---

## **M) Minimal FE/BE Naming & Canon**

* IDs are `snake_case`; arrays sorted before emission where the order is a SET.  
* No raw numerics to the public surface; keep WHY/debug private.  
* Avoid public runtime flags in SPA; **fail boot in prod** on `VITE_*`/`NEXT_PUBLIC_*`.

---

### **Notes for Agents**

* **Self-QA** every step: run sanity, unit tests, schema validation, and (if engine touched) determinism probes **locally** before asking for acceptance.  
* **Do not** reference CI, PR reviewers, or background tasks. You act **only** on PO prompts.  
* When unsure, ask. When memory is tight, post a **CONTEXT-ALERT** and summarize your next step.

---

Awesome—here’s a clean, copy-ready **Appendix** you can drop into the repo (e.g., `/docs/appendix/`). It’s faithful to the pins we’ve already set (Lake discipline, Reader-only ETag, numeric-free public surface, programmatic config, Postgres JSONB, no GitHub CI/PR). It’s organized so each section stands alone.

---

# **Appendix — Canonical Schemas, Patterns & Gate Scripts**

**Operating mode:** No CI/PR. All checks run locally. Evidence lives in the **repo dump** at card close. Mid-card review only if the PO requests it.

---

## **A) Reader v1 — Public JSON Schema (numeric-free)**

**Path:** `schemas/reader_public_v1.schema.json`

{

  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "$id": "schemas/reader\_public\_v1.schema.json",

  "title": "Reader Public Payload v1",

  "type": "object",

  "required": \["user", "matching"\],

  "additionalProperties": false,

  "properties": {

    "user": {

      "type": "object",

      "required": \["id", "profile", "preferences"\],

      "additionalProperties": true

    },

    "matching": {

      "type": "object",

      "required": \[

        "reader\_version", "eligible", "release\_id",

        "idempotence\_hash", "meta"

      \],

      "additionalProperties": false,

      "properties": {

        "reader\_version": { "enum": \["v1"\] },

        "eligible": { "type": "boolean" },

        "categories": {

          "type": "array",

          "items": {

            "type": "object",

            "required": \["id", "band"\],

            "additionalProperties": false,

            "properties": {

              "id": { "type": "string", "pattern": "^\[a-z0-9\_\]+$" },

              "band": { "enum": \["Cool","Open","Warm","Glow"\] },

              "prompt": {

                "type": "string",

                "maxLength": 160,

                "pattern": "^\[^\\n\\r\]\*$"

              }

            }

          }

        },

        "prompt": { "type": "string", "maxLength": 160, "pattern": "^\[^\\n\\r\]\*$" },

        "release\_id": { "type": "string", "pattern": "^\[a-f0-9\]{64}$" },

        "idempotence\_hash": { "type": "string", "pattern": "^\[a-f0-9\]{64}$" },

        "meta": {

          "type": "object",

          "required": \["engine\_tag", "invocation\_tag"\],

          "additionalProperties": false,

          "properties": {

            "engine\_tag": { "type": "string", "minLength": 1 },

            "invocation\_tag": { "type": "string", "pattern": "^INV-\[a-f0-9\]{16}$" }

          }

        }

      }

    }

  }

}

---

## **B) Canonical Serializer & Hash Coupling (Python)**

**Paths:**

* `app/lib/sercanon.py` — single source of truth  
* `tests/lib/test_sercanon.py` — determinism tests

\# app/lib/sercanon.py

import json, hashlib

from typing import Any, Dict

\# Stable JSON: UTF-8, sorted keys, compact, exactly ONE trailing LF.

def dumps\_public(obj: Any) \-\> bytes:

    s \= json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",", ":"))

    return (s \+ "\\n").encode("utf-8")

\# Hash over PUBLIC BYTES \*\*EXCLUDING\*\* the 'idempotence\_hash' field to avoid recursion.

\# Caller constructs the envelope without the hash, computes it, then inserts it.

def idempotence\_hash(public\_without\_hash: Dict\[str, Any\]) \-\> str:

    b \= dumps\_public(public\_without\_hash)

    return hashlib.sha256(b).hexdigest()

\# tests/lib/test\_sercanon.py

from app.lib.sercanon import dumps\_public, idempotence\_hash

def test\_dumps\_public\_trailing\_lf():

    b \= dumps\_public({"a": 1})

    assert b.endswith(b"\\n")

    assert b.count(b"\\n") \== 1

def test\_idempotence\_hash\_stable():

    obj \= {"x": 1, "y": {"a": 2}}

    h1 \= idempotence\_hash(obj)

    h2 \= idempotence\_hash({"y": {"a": 2}, "x": 1})  \# key reorder

    assert h1 \== h2

    assert len(h1) \== 64 and all(c in "0123456789abcdef" for c in h1)

---

## **C) Reader Adapter — ETag & 304 (Flask)**

**Paths:**

* `app/api/readers.py`  
* `tests/api/test_reader_etag.py`

\# app/api/readers.py

from flask import Blueprint, g, make\_response, request

from app.present.reader\_v1 import emit\_public \# returns dict WITHOUT idempotence\_hash

from app.lib.sercanon import dumps\_public, idempotence\_hash

bp \= Blueprint("readers", \_\_name\_\_, url\_prefix="/api")

@bp.get("/auth/me")

def reader\_v1():

    \# Domain build (internal)

    public\_wo \= emit\_public(g.user\_id)      \# dict without the 'idempotence\_hash' key

    etag \= idempotence\_hash(public\_wo)

    inm \= request.headers.get("If-None-Match")

    if inm \== etag:

        \# Conditional GET: 304, empty body

        resp \= make\_response("", 304\)

        resp.headers\["ETag"\] \= etag

        resp.headers\["Vary"\] \= "Authorization"

        resp.headers\["Cache-Control"\] \= "private, no-cache, must-revalidate"

        return resp

    public \= dict(public\_wo, idempotence\_hash=etag)

    body \= dumps\_public({"user": build\_user(g.user\_id), "matching": public})

    resp \= make\_response(body, 200\)

    resp.mimetype \= "application/json"

    resp.headers\["ETag"\] \= etag

    resp.headers\["Vary"\] \= "Authorization"

    resp.headers\["Cache-Control"\] \= "private, no-cache, must-revalidate"

    return resp

def build\_user(user\_id):  \# minimal placeholder (kept small & boring)

    return {"id": f"u\_{user\_id}", "profile": {}, "preferences": {}}

\# tests/api/test\_reader\_etag.py

def test\_reader\_200\_has\_etag\_and\_headers(client, authed):

    r \= client.get("/api/auth/me")

    assert r.status\_code \== 200

    assert "ETag" in r.headers

    assert "Authorization" in r.headers.get("Vary", "")

    assert "private" in r.headers.get("Cache-Control", "")

def test\_reader\_304\_empty\_body(client, authed):

    r1 \= client.get("/api/auth/me")

    etag \= r1.headers\["ETag"\]

    r2 \= client.get("/api/auth/me", headers={"If-None-Match": etag})

    assert r2.status\_code \== 304

    assert r2.data \== b""

    assert r2.headers\["ETag"\] \== etag

def test\_writers\_no\_etag(client, authed):

    w \= client.put("/api/profile/preferences", json={"preferred\_pace":"fast"})

    assert w.status\_code in (200,204)

    assert "ETag" not in w.headers

---

## **D) Writers — JSONB Hygiene (SQLAlchemy \+ Postgres)**

**Paths:**

* `app/models/preferences.py`  
* `app/api/writers.py`  
* `tests/api/test_writer_preferences.py`

\# app/models/preferences.py

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.ext.mutable import MutableDict

from app.db import db

class UserPreferences(db.Model):

    \_\_tablename\_\_ \= "user\_preferences"

    user\_id \= db.Column(db.Integer, primary\_key=True)

    prefs   \= db.Column(MutableDict.as\_mutable(JSONB), nullable=False, server\_default="{}")

\# app/api/writers.py

from flask import Blueprint, g, request, make\_response

from app.models.preferences import UserPreferences

from app.db import db

from app.middleware.errors import error\_response

from app.generated.enums import PREFERRED\_PACE

bp \= Blueprint("writers", \_\_name\_\_, url\_prefix="/api")

@bp.put("/profile/preferences")

def update\_preferences():

    if not getattr(g, "user\_id", None):

        return error\_response(401, "unauthorized", "auth required")

    payload \= request.get\_json(silent=True) or {}

    pace \= payload.get("preferred\_pace")

    if pace not in set(PREFERRED\_PACE):

        return error\_response(400, "bad\_request", "preferred\_pace invalid")

    with db.session.begin():

        prefs \= db.session.get(UserPreferences, g.user\_id) or UserPreferences(user\_id=g.user\_id, prefs={})

        prefs.prefs\["preferred\_pace"\] \= pace

        db.session.add(prefs)

    resp \= make\_response("", 204\)

    resp.headers\["Cache-Control"\] \= "no-store"

    return resp

\# tests/api/test\_writer\_preferences.py

from sqlalchemy import select

from app.models.preferences import UserPreferences

def test\_writer\_204\_and\_persists(client, authed, session):

    r \= client.put("/api/profile/preferences", json={"preferred\_pace":"fast"})

    assert r.status\_code \== 204

    assert r.headers.get("Cache-Control") \== "no-store"

    row \= session.execute(select(UserPreferences).where(UserPreferences.user\_id==authed.id)).scalar\_one()

    assert row.prefs.get("preferred\_pace") \== "fast"

---

## **E) Error Envelope & Correlation ID**

**Paths:**

* `app/middleware/errors.py`  
* `app/middleware/correlation.py`

\# app/middleware/errors.py

from flask import jsonify

def error\_response(code: int, err: str, msg: str, \*\*extra):

    body \= {"ok": False, "code": err, "error": msg}

    body.update(extra)

    resp \= jsonify(body)

    resp.status\_code \= code

    return resp

\# app/middleware/correlation.py

import uuid

from flask import g, request

def install\_correlation(app):

    @app.before\_request

    def \_inject():

        g.correlation\_id \= request.headers.get("X-Correlation-ID") or str(uuid.uuid4())

---

## **F) FE (React) Reader Wrapper — Conditional GET**

**Path:** `src/lib/reader.ts`

// src/lib/reader.ts

type Matching \= {

  reader\_version: "v1";

  eligible: boolean;

  categories?: { id: string; band: "Cool"|"Open"|"Warm"|"Glow"; prompt?: string }\[\];

  prompt?: string;

  release\_id: string;

  idempotence\_hash: string;

  meta: { engine\_tag: string; invocation\_tag: string };

};

type Reader \= { user: any; matching: Matching };

const etagCache \= new Map\<string, { etag: string; json: Reader }\>();

export async function fetchReader(authToken: string): Promise\<Reader\> {

  const key \= "auth\_me"; // SPA has a single reader

  const cached \= etagCache.get(key);

  const headers: Record\<string,string\> \= { "Authorization": \`Bearer ${authToken}\` };

  if (cached?.etag) headers\["If-None-Match"\] \= cached.etag;

  const r \= await fetch("/api/auth/me", { method: "GET", headers, credentials: "include" });

  if (r.status \=== 304 && cached) return cached.json;

  if (\!r.ok) throw new Error(\`Reader failed: ${r.status}\`);

  const etag \= r.headers.get("ETag") || "";

  const json: Reader \= await r.json();

  etagCache.set(key, { etag, json });

  return json;

}

**FE rules:** never render from writer bodies; after a successful write, call `fetchReader()` and re-render. No `VITE_*`/`NEXT_PUBLIC_*` product flags.

---

## **G) Programmatic Config (Generator)**

**Paths:**

* `docs/registry/fields_v1.json` (authoritative)  
* `scripts/generate_enums.py`  
* `app/generated/enums.py` (generated)

\# scripts/generate\_enums.py

import json, pathlib, sys

REG \= pathlib.Path("docs/registry/fields\_v1.json")

OUT \= pathlib.Path("app/generated/enums.py")

def main():

    reg \= json.loads(REG.read\_text("utf-8"))

    pace \= next(x for x in reg if x\["id"\] \== "preferred\_pace")

    allowed \= sorted(pace.get("enum", \[\]))

    body \= (

        "\# generated; DO NOT EDIT\\n"

        "PREFERRED\_PACE \= (" \+ ", ".join(repr(x) for x in allowed) \+ ",)\\n"

    )

    OUT.write\_text(body, "utf-8")

if \_\_name\_\_ \== "\_\_main\_\_":

    sys.exit(main())

---

## **H) Sanity Runner & Gate Stubs (No-CI)**

**Paths:**

* `scripts/make_sanity.sh`  
* `scripts/run_gate_reader.sh`  
* `artifacts/` (outputs)

\#\!/usr/bin/env bash

\# scripts/make\_sanity.sh

set \-euo pipefail

mkdir \-p artifacts

echo "== Ruff \==" && ruff .          | tee artifacts/ruff.txt

echo "== Mypy \==" && mypy .          | tee artifacts/mypy.txt

echo "== Pytest \==" && pytest \-q     | tee artifacts/pytest.txt

python3 scripts/generate\_enums.py

echo "SANITY: OK" | tee artifacts/sanity.txt

\#\!/usr/bin/env bash

\# scripts/run\_gate\_reader.sh

set \-euo pipefail

STAMP=$(date \-u \+"%Y%m%dT%H%M%SZ")

OUT="audit/gates/reader/$STAMP"

mkdir \-p "$OUT"

\# Snapshot reader headers (200)

curl \-sS \-D "$OUT/reader\_200.headers.txt" \-o /dev/null \\

  \-H "Authorization: Bearer $TOKEN" https://\<host\>/api/auth/me

\# Conditional GET to prove 304

ETAG=$(grep \-i '^ETag:' "$OUT/reader\_200.headers.txt" | awk '{print $2}' | tr \-d '\\r')

curl \-sS \-D "$OUT/reader\_304.headers.txt" \-o /dev/null \\

  \-H "Authorization: Bearer $TOKEN" \-H "If-None-Match: $ETAG" https://\<host\>/api/auth/me

echo "READER\_GATE: OK" | tee "$OUT/gate\_log.txt"

---

## **I) Optional Server Cache (e.g., Redis) — Composite Keys**

**Use only if explicitly required.** Keys MUST include `(user_id, fpA, fpB, release_id)`. Never share by hash alone.

**Path:** `app/cache/reader_cache.py`

def reader\_cache\_key(user\_id: int, fpA: str, fpB: str, release\_id: str) \-\> str:

    return f"reader:v1:u:{user\_id}:a:{fpA}:b:{fpB}:r:{release\_id}"

---

## **J) Post-Deploy Smoke (PUT → GET)**

**Path:** `scripts/post_deploy_smoke.sh`

\#\!/usr/bin/env bash

set \-euo pipefail

curl \-fsS \-X PUT \-H "Content-Type: application/json" \\

  \-H "Authorization: Bearer $TOKEN" \\

  \-d '{"preferred\_pace":"fast"}' https://\<host\>/api/profile/preferences \\

  \-D /tmp/smoke\_put.h \-o /dev/null

curl \-fsS \-H "Authorization: Bearer $TOKEN" \\

  https://\<host\>/api/auth/me | jq '.user.preferences.preferred\_pace' | grep \-q '"fast"'

echo "SMOKE: OK"

---

## **K) Repo Dump Manifest (evidence index)**

**Path:** `artifacts/repo_dump_manifest.json` (generated by your dump script)

{

  "card\_id": "CORE-XXXX-YYY",

  "commit": "\<sha7\>",

  "generated\_at": "2025-09-27T12:34:56Z",

  "files": \[

    {"path":"app/api/readers.py","bytes":1234,"sha256":"..."},

    {"path":"schemas/reader\_public\_v1.schema.json","bytes":2048,"sha256":"..."}

  \],

  "gates": {

    "sanity": "SANITY: OK",

    "reader": "READER\_GATE: OK"

  },

  "notes": "Evidence is authoritative in this dump."

}

---

## **L) Rate Limits & CSRF (BE)**

**Path:** `app/middleware/rate_limit.py` (illustrative stub)

\# Keep simple & explicit; tune per route.

WINDOW\_S \= 60

MAX\_PER\_WINDOW \= 30

\# Implement with Redis or in-DB counters only if required; otherwise document limits and audit manually.

Browser writers: on **403 CSRF**, refresh token once and retry exactly once; else show a clear error to the user. (FE implements; BE returns typed errors.)

---

## **M) Minimal FE/BE Naming & Canon**

* IDs are `snake_case`; arrays sorted before emission where the order is a SET.  
* No raw numerics to the public surface; keep WHY/debug private.  
* Avoid public runtime flags in SPA; **fail boot in prod** on `VITE_*`/`NEXT_PUBLIC_*`.

---

### **Notes for Agents**

* **Self-QA** every step: run sanity, unit tests, schema validation, and (if engine touched) determinism probes **locally** before asking for acceptance.  
* **Do not** reference CI, PR reviewers, or background tasks. You act **only** on PO prompts.  
* When unsure, ask. When memory is tight, post a **CONTEXT-ALERT** and summarize your next step.

---

If you want this split into multiple files in `/docs/appendix/` with a tiny index, say the word and I’ll output them pre-named and ready to paste.

Absolutely. Here’s a paste-ready standard you can drop into the docs as a new section:

\# Appendix C — Agent↔Agent Communication Protocol (AICP)

\> \*\*Stance\*\*  

\> Agents are not autonomous. All cross-agent messages are authored \*\*for relay by the PO\*\*. Messages contain no time references, no promises of future action, and no CI/PR chatter. Evidence beats opinion; hashes beat adjectives.

\---

\#\# C.0 Principles (pins)

\- \*\*No autonomy\*\*: never address another agent as if you can trigger them. Address the PO with a relay note: \`TO:\<agent/role\>\`.

\- \*\*No time talk\*\*: no dates, no waiting, no estimates. Identity is by \*\*paths, SHAs, hashes\*\*.

\- \*\*Dense, readable, deterministic\*\*: minimal prose; exact schemas/paths; stable terminology.

\- \*\*Repo-dump truth\*\*: if code exists in the repo, \*\*cite paths and SHAs\*\*, do not inline the whole file.

\- \*\*Ask-first\*\*: if an input is missing, list it under \`NEEDED\_INPUTS\` and stop.

\---

\#\# C.1 Message Format (AGENT-MSG v1)

Use this fenced block for \*\*all\*\* inter-agent messages (cards, CRDs, reviews, requests). The PO relays it verbatim.

AGENT-MSG v1 TO: \<role|agent\> \# e.g., Engine Lead | FE Lead FROM: \<role|agent\> \# e.g., Full-Stack Guru SUBJECT:

CONTEXT\_CAPSULE: ROLE= CARD= WIP\_OK=YES CANON=\[ , , ... \] HEAD\_SHA=

INTENT:

ASSUMPTIONS:

* \<explicit assumption 1\>  
* \<explicit assumption 2\>

NEEDED\_INPUTS:

* \<missing fact 1\> \# stop here if critical  
* \<missing fact 2\>

CONTRACTS\_REFERENCED:

* /schemas/.json §  
* /docs/registry/.json §

EVIDENCE\_ANCHORS:

* PATH: SHA: HASH:  
* GATE: audit/gates//\[/SEQ-n\]/gate\_log.txt → \*\_GATE: OK

PROPOSAL|REVIEW:

* \<delta summary; bullet list of files and \~LOC or behaviors\>  
* \<risk, rollback \= single revert of \>

ACCEPTANCE (binary):

1.   
2.   
3. 

PATCH\_CAPSULE (optional): \<\<\<PATCH

# **unified diff or JSON patch; minimal, self-contained; no timestamps**

\--- a/app/... \+++ b/app/... @@ ... PATCH

VALIDATION\_CAPSULE: CMD: \- ruff/mypy/pytest/schema \- scripts/run\_gate\_.sh → \*\_GATE: OK \- reader 200/304 header capture → artifacts/headers/.txt EXPECT: \- SANITY: OK in artifacts/sanity.txt \- Writers: 204 \+ no-store; no ETag on errors \- Reader: 200 ETag=\<idempotence\_hash\>; 304 empty body

ATTEST: I assert this message contains only reproducible claims anchored by paths/SHAs/hashes. END

\*\*Rules\*\*

\- Keep each section present; use \`N/A\` rather than omit.

\- Prefer bullets and capsules to paragraphs.

\- Never include secrets; log them as \*\*present/absent\*\* only.

\---

\#\# C.2 Card-to-Agent Skeleton (implementer-facing)

AGENT-MSG v1 TO: FROM: SUBJECT: CRD —

INTENT: Ship with ≤ LOC, reversible by single revert.

PROPOSAL: FILES: \- (\~LOC) \- (\~LOC) BEHAVIOR: \- \- NON-GOALS: \-

ACCEPTANCE:

1. scripts/make\_sanity.sh → SANITY: OK  
2. Reader headers: 200 ETag present; 304 empty; writers/errors no ETag  
3. Determinism harness PASS (if engine)

RISK & ROLLBACK: Risk=\<LOW|MED\>; rollback=single revert of this change.

VALIDATION\_CAPSULE: CMD: \- pytest \-q tests/:: \- python scripts/registry\_validate.py \- bash scripts/run\_gate\_reader.sh EXPECT: \- \*\_GATE: OK lines present; artifacts have single trailing \\n END

\---

\#\# C.3 Review-to-Agent Skeleton (redline format)

AGENT-MSG v1 TO: FROM: SUBJECT: REDLINE —

FINDINGS:

* \[BLOCKER\] Writers emit ETag on 400; must be absent. PROOF: artifacts/headers/writer\_400.txt → "ETag": "..." FIX: guard header emission in error path.  
* \[MAJOR\] Missing AB↔BA parity test. PROOF: no goldens under goldens/reader/v1/g06\_ab\_ba\_\*.jsonl FIX: add jsonl pair; assert byte equality and hash.

ACCEPTANCE\_DIFF:

* tests/reader\_v1/test\_parity.py::test\_ab\_ba\_identity  
* server/adapter/reader.py guard: no ETag on non-200

RE-VALIDATE WITH:

* bash scripts/run\_gate\_reader.sh → READER\_GATE: OK  
* pytest \-q tests/reader\_v1/test\_parity.py::test\_ab\_ba\_identity

ATTEST: Redlines reference only repo paths and artifacts; no stylistic or speculative items. END

\---

\#\# C.4 Relay-Safe Phrases (do use / don’t use)

\*\*Do\*\*

\- “NEEDED\_INPUT: confirm FE wrapper sends \`If-None-Match\` and reuses cached JSON on 304.”

\- “EVIDENCE: audit/gates/reader/\<sha\>/gate\_log.txt ends READER\_GATE: OK.”

\- “RISK: single revert restores prior behavior.”

\*\*Don’t\*\*

\- “Ping me later / I’ll do this tomorrow / waiting for CI.”

\- “We’ll sync offline / I’ll coordinate with X.”

\- “Time-boxed / ETA / delay.”

\---

\#\# C.5 Memory & Context Anchors

Agents should emit compact anchors the next agent can absorb without backscroll:

CONTEXT\_ANCHOR CARD= HEAD\_SHA= SURFACE\_UNCHANGED=\<true|false\> READER\_ETAG\_POLICY=ENFORCED WRITERS\_NO\_STORE=ENFORCED DETERMINISM\_HARNESS=\<PASS|N/A\> SCHEMA\_DRIFT=\<none|paths\>

\---

\#\# C.6 Evidence Grammar (hash-anchored claims)

\- \*\*Header Snapshot\*\*: \`artifacts/headers/\<case\>.txt\` → key:value lines; no body for 304\.

\- \*\*Golden\*\*: \`goldens/\<domain\>/\<v\>/gNN\_\*.json\[.sha256\]\` → exact bytes; single trailing \`\\n\`.

\- \*\*Gate Log\*\*: \`audit/gates/\<name\>/\<sha\>/gate\_log.txt\` → ends with \`\<NAME\>\_GATE: OK\`.

\- \*\*SBOM\*\*: \`artifacts/sbom.json\[.sha256\]\` → lists dependencies and licenses.

\*\*Claim form\*\*:  

\`CLAIM: \<assertion\>  PROOF: \<path\> \[HASH:\<sha256\>\]\`

\---

\#\# C.7 Prohibited Constructs

\- Any mention of dates, durations, “soon,” “waiting,” “later.”

\- Any implication of background activity or external comms between agents.

\- CI/PR language (“open a PR,” “wait for checks,” “assign a reviewer”).

\- Pasting secrets or PII in messages or artifacts.

\---

\#\# C.8 Minimal Examples

\*\*Short request to Engine Lead\*\*

AGENT-MSG v1 TO: Engine Lead FROM: BE Lead SUBJECT: Confirm frozen pack membership for release\_id

NEEDED\_INPUTS:

* List of files and canonical order used in sha256(release\_id)

EVIDENCE\_ANCHORS:

* Current script path: scripts/release\_fuse.py (lines 18–52)

ACCEPTANCE:

1. Path list confirmed  
2. Order confirmed  
3. Hash matches artifacts/release\_id.txt END

\*\*Short ACK from Engine Lead\*\*

AGENT-MSG v1 TO: BE Lead FROM: Engine Lead SUBJECT: ACK — frozen pack membership

INTENT: Confirm allow-list and order.

FACTS:

* /config/freeze\_pack\_v1.json  
* /engine//v1/present/\*  
* /engine//v1/ops.py  
* /goldens/engine/v1/\*

ORDER: freeze\_pack\_v1.json → present/\* (sorted) → ops.py → goldens/\* (sorted)

ATTEST: This mirrors the hashing function in scripts/release\_fuse.py. END

\---

\#\# C.9 Final Attestation (drop at end of every inter-agent note)

I acknowledge: no autonomy, no time references, no CI/PR requests. All claims are hash-anchored and reproducible from the repo dump.

# 

---

---

