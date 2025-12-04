# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref

**Version:** v1.4.5

**Status:** Canon

**Effective date:** 2025-12-04

**Last Update Gate:** BN 8.0.7 Drain A8

**Invocation tag:** INV-f2ac55d77ce9aacc

---

## **0.2 Scope \[Required-Now\]**

* **Supersession (PF10 addenda).** PF10 is living; when multiple **numbered** addenda exist, the later number supersedes earlier guidance. PF05 integrates the latest addenda and routes **by title only** to single homes (no version numbers).

* **Ownership.** This document owns the **bytes** for CLI, Reader transport, and Vendor ingest (HDAPI): payload shapes, validators, headers & conditional delivery, typed error mapping, and exit-code/stream rules. It is authoritative for CLI and Reader wire bytes. **Appendix A** transport matrices are kept in lockstep with **HDE-Governance §10** (titles only). Writers/errors posture is policy-owned in Governance; PF05 references it by title.

* **Public resonance posture (v1).** Public surface is **bands-only** and **numeric-free**; resonance is **SR-only** (`alpha=1.0`). `hysteresis=1` is armed for future XR and not exposed. Any XR diagnostics, if used, are **CLI-admin-guarded** and never emitted on Reader 200\.

* **Canonical JSON and locale.** All public bytes are UTF-8 (no BOM), ASCII-sorted keys, compact, with exactly **one trailing LF**. Arrays used as sets are deduped and ASCII-sorted. All byte checks and comparisons run with `LC_ALL=C` and `TZ=UTC` (see **HDE-Schemas & Artifacts**).

* **Endpoint Catalog (JSON success): proof surface (A7).** The Catalog is **internal-only** and **env-gated** per entry; entries not gated for prod are **unreachable in production**. A7 transport proofs **must** run on a **§5.6 Endpoint Catalog (JSON success)** route (titles only; path-agnostic). Internal-ops `/internal/version` is **excluded** and governed by **HDE-Governance §10.5**. A7 **byte rules** are owned in **§5.3** of this document.

* **Single homes (routing by title only).**  
   • **Math/algorithms** (composite, scoring, banding, preimage, constants): **HDE-Math-Spec**.  
   • **Schemas and pack/manifest/canonical rules** (including `catalog/manifest.json` for `release_id`) and the **machine JSONL mirror** schema & parity rules: **HDE-Schemas & Artifacts**.  
   • **Governance & acceptance policy** (A-gates, evidence, SAFE rails, numeric-free covenant, internal-ops exception): **HDE-Governance**.  
   PF05 does not duplicate rules, token rosters, or evidence paths; it points to single homes.

* **Evidence discipline (PF12 single home).** Evidence indexing (titles/paths only), the human Evidence Index and its hash sentinel, and the machine JSONL mirror are governed in **PF12** and must update **in the same PR** as artifact changes. CI enforces: 1:1 join equality (human↔machine), unknown-key rejection, ASCII field order, sort-before-write, **single mirror file**, and required `proof_anchor` path-proofs, per PF12.

* **Process and PR workflow (titles only).** CodEx staging, PR-first merging, **evidence-only QA branches**, and diff-scoped validation live in **Epic-Process-Guide**. Follow the evidence-only PR template. **Build Notes** are WIP-only and not a single home; drained guidance must land in canon.

* **QA status note (informative).** The CLI is installable and `--help` / `--version` behave correctly. `hdctl showcompat` is wired through the single canonical presenter/emitter and is expected to **always** emit a non-empty, LF-terminated compat JSON document on success. AB↔BA parity, two-run identity, Reader↔CLI parity (via `--dump-reader`), and preimage recompute for the Reader v1 envelope are enforced via dedicated harnesses and indexed evidence (titles-only; see Appendix D and HDE-Schemas & Artifacts). Any empty stdout on a reported success, any deviation from the compat/Reader contracts in §§3–5, or any canonicalization/schema failure **must be treated as a regression** and must fail the associated CLI acceptance tokens (`CLI_SHOWCOMPAT_CANON_OK`, `CLI_STDOUT_LF_OK`, `PARITY_AB_BA_OK`, `TWO_RUN_IDENTITY_OK`, `CLI_READER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`). These tokens remain merge-gating for EPIC017; failures indicate bugs to be remediated, not acceptable behavior.

* **Narratives routing (titles only).** Reader remains **numeric-free and narrative-free**. Narrative bytes are carried via **Aux (text surface)** and **CLI admin preview** only. A7 transport and suppression policy lives in **HDE-Governance**. **Aux and CLI endpoint bytes live here** (see §5.7 and §4.5). No narrative text appears on Reader 200\.

**Non-goals.** App UX, SPA behavior, and narrative content are out of scope; this doc focuses on transport, CLI, and vendor.

## **0.3 Tagging convention**

* **\[Implemented\]** — Verified in the repository and exercised by surfaces/tests.  
* **\[Required-Now\]** — Required for current build goals; if missing in code, it is a gap to close.  
* **\[Speculative\]** — Accepted future design; preserved here but not yet wired.

  ## **0.4 Change policy**

* **Single homes; no duplication.** Do not restate Architecture/Math rules; keep CLI/Reader/Vendor **bytes here** and reference other documents **by title only**.

* **Governed paths only.** Evidence must live under governed repo paths (`artifacts/**`, `docs/**`). Transient generator paths (scratch/temp) are disallowed.

* **Determinism first.** Any change that could affect byte identity (serializer/emitter path, schema keys, conditional delivery) **must** include updated acceptance evidence (**AB↔BA**, **two-run**, **LF**, **idempotence recompute**). All byte checks run under `LC_ALL=C`, `TZ=UTC`.

* **Doc-Delta discipline.** Record normative deltas succinctly in the Change Log with: scope, targets (section anchors), acceptance impact, and whether a freeze-pack or evidence update is required.

* **Same-PR parity (human ↔ machine) lives in PF12.** When evidence indexes change, update **in the same PR** per PF12: human `docs/evidence/INDEX.json`, its hash sentinel, and the machine mirror at `artifacts/evidence_index.jsonl`. CI enforces: **1:1 join**, **records-only JSONL**, **ASCII field order**, **sort-before-write**, **unknown-key rejection**, **single mirror file**, and required **`proof_anchor` path-proofs**.

* **Sentinel gate.** The human Evidence Index **hash sentinel** is merge-gating and is governed in PF12. Note sentinel updates in the Change Log entry.

* **PR checklist tokens.** Include (at minimum) `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`. For full hygiene, also include `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`, `CI_CHECK_FINAL_LF_OK`. *(Token names live in Governance.)*

* **Process ownership.** Use the evidence-only PR template and follow the “update in same PR” workflow defined in **Epic-Process-Guide** (titles only). **Build Notes** are WIP only; drained guidance must land in canon.

* **Freeze-pack changes.** If a freeze-pack is affected, emit a new `release_id` and log it in the Change Log; snapshot/manifest schemas are owned by **HDE-Schemas & Artifacts** (titles only).

**Editorial vs. normative.** Pure editorial rearrangements need not be logged; any change to math, transport, or the public contract **must** be logged.

---

# **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**

## **CLI commands**

* **`hdctl showcompat` — Implemented; merge-blocking until compat determinism and Reader↔CLI parity are proven.** Canonical compat admin harness and Reader parity surface. See §4.1 for full CLI contract, canonical JSON rules, and acceptance tokens.

* **`read singlebg` — Speculative.** Planned single-chart read. Flags, validators, and payload shape will be owned in §4.2 when wired.

* **`list people` — Speculative.** Planned listing command for people. Sorting/filters and JSON/tabular payloads will be owned in §4.3 when wired.

* **Fetch commands (person/batch) — Speculative.** Explicitly disabled in Alpha. Enabling them requires transport acceptance and Governance tokens as defined in the CLI and Vendor sections (§4.4, §7).

* **`hdctl dev:sampler` — Implemented (dev/admin-only).** Dev/admin sampler harness; runs only when `APP_ENV ∈ {dev, test, local}` under closed rails, reads a JSON candidates file, calls the sampler core, and emits canonical JSON for deterministic QA replay. Full contract (inputs, seed semantics, determinism, and streams) lives in §4.10.

  ---

  ## **Reader transport**

* **Endpoint Catalog (JSON success) — Required-Now.** Internal-only, env-gated per entry, and the **single A7 proof surface** for Reader success routes (not `/internal/version`). A7 header matrix, conditional behavior, and proof artifacts are specified in §5.3, §5.6, and Appendix A; PF12 owns the Evidence Index and mirror schema.

* **Dev harness — Implemented (dev-only).** `/api/reader?v=1` dev Reader surface for schema/LF checks, AB↔BA and two-run identity, and Reader↔CLI parity. Rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); harness proofs are **supplemental** and do not replace Endpoint Catalog A7 proofs. See §5.4.

* **`/internal/version` (ops endpoint) — Required-Now.** Ops-only identity surface (JSON, no cache, no ETag) used for engine identity and rails snapshots. Header and refusal posture are governed by HDE-Governance §10.5; bytes live in the internal-ops section of Reader transport.

* **Production Reader surface — Speculative.** Future public endpoint for Glow App. When enabled, public header and conditional-delivery rules will be owned in §5.2/§5.3; until then, behavior is dev/ops-only.

  ---

  ## **Serializer and emitter**

* **Single canonical emitter shared by CLI and Reader — Required-Now.** All public JSON (success and typed errors) is emitted by a single presenter/emitter entrypoint with canonical JSON rules (UTF-8, sorted keys, compact, one LF). No ad-hoc `json.dumps` or alternate serializers on public paths. Full rules and grep-guards live in §6.

  ---

  ## **Vendor ingest (HDAPI)**

* **Request shaping — Implemented.** Canonical vendor endpoint, HTTP method, headers, and three-key BodyGraph JSON body, plus deterministic mapping from provider responses to typed CLI/Reader errors. See §7.2.

* **Base-URL resolution — Required-Now.** `HDAPI_BASE_URL` is required and must be non-empty. No literal default; missing/empty fails closed with a typed error and **no network I/O**, per §7.1.

* **Live HTTP gated by SAFE rails — Required-Now.** Vendor calls are permitted only when rails are explicitly open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); default posture for dev/CI is closed. Closed-rails refusal behavior, admin override, and rails evidence live in §7.1.

* **Adapter data-source policy — Required-Now.** In prod, the adapter reads from DB on the hot path, using vendor only on explicit triggers (birth-data change, scheduled refresh, operator). In dev, direct vendor calls are allowed but must upsert into DB for repeatability. See §7.4.

* **Production calls — Speculative.** Concrete timeout, retry, backoff, and observability profiles are defined in §7.3 and must be pinned (closed enums/integers) before enabling production vendor traffic.

  ---

  ## **Evidence discipline: indices and parity**

* **Evidence index & mirror — Required-Now.** Appendix D and HDE-Schemas & Artifacts govern the human Evidence Index (`docs/evidence/INDEX.json` \+ hash sentinel), the machine mirror (`artifacts/evidence_index.jsonl`), and all governed Reader/Vendor proof artifacts. PF05 relies on PF12 for schema and path details; every change to governed artifacts must update both human index and mirror in the same PR, with CI enforcing 1:1 parity and path-proofs.

  ---

  # **2\) Purpose & Scope \[Required-Now\]**

  ## **2.1 Purpose**

* **CLI \= test & debug tool.** The CLI exists to **exercise and verify** the HD Engine and transport behavior (schema/LF, AB↔BA, two-run, idempotence), not to serve end users.

* **Reader transport & vendor ingest.** This document **owns** the technical bytes for **Reader transport** (public payload, headers/conditional delivery, error mapping) and **Vendor ingest (HDAPI)** (request shaping, typed failures, rails).

* **Integration & acceptance.** The spec provides what’s needed to integrate the engine behind the Glow app and to pass acceptance (evidence, goldens, CI hygiene).

  ## **2.2 Out of scope**

* **Product UX / SPA.** Application UX, narrative copy, and public SPA behavior are **out of scope** here.

* **Routing by title only.** When needed, reference **Architecture** and **Math** **by title only** (no duplicated rules/bytes).

# 

  # **3\) CLI Overview & Conventions \[Required-Now\]**

**QA status note (informative).** The CLI is installable and \`--help\` / \`--version\` behave as expected. A known issue remains: in some runs \`hdctl showcompat\` emits empty stdout, which violates the non-empty compat JSON requirement and blocks the determinism/parity tokens (\`CLI\_SHOWCOMPAT\_CANON\_OK\`, \`CLI\_STDOUT\_LF\_OK\`, \`PARITY\_AB\_BA\_OK\`, \`TWO\_RUN\_IDENTITY\_OK\`, \`CLI\_READER\_PARITY\_OK\`, \`JSON\_CANONICAL\_CHECK\_OK\`). Until this is fixed and re-proven, those tokens remain pending. All success output must come from the single canonical emitter, use UTF‑8 with ASCII-sorted keys and exactly one trailing LF, and be validated under \`LC\_ALL=C\` and \`TZ=UTC\`.

.

## **3.1 Global flags & process contract**

* **Packaging & entrypoints (normative).** Single home in **pyproject**:  
   `[project.scripts]` defines `hdctl = "engine.cli.main:cli"`.  
   **Module-runner parity:** `python -m engine.cli --help` ≡ `hdctl --help` (exit 0).  
   **QA status:** expected PASS for `CLI_PYPROJECT_ENTRYPOINT_OK`, `CLI_INSTALL_OK`, `CLI_MODULE_RUN_OK`, `CLI_HELP_EXIT_0_OK`, `CLI_HELP_STDOUT_OK`.

* **`--help` / `-h`** — print usage synopsis and exit 0 (no payload; stdout).

* **`--version`** — print CLI version/build tag and exit 0 (no payload; stdout).

* **Environment gate** — the CLI must **not** alter SAFE rails or emit non-canonical bytes; all public outputs come from the **single presenter/emitter** (see §6).

* **Input normalization** — the CLI prepares normalized inputs (**order-neutral AB↔BA**) before invoking the engine.

  ## **3.2 Input forms (files vs inline) \[Required-Now\]**

Input methods for commands that compare or display charts. Titles-only pointers; no transport bytes restated here.

### **Files (Required-Now)**

* **File arguments.** Commands accept file paths to **canonical chart JSON** (e.g., `--a <path>`, `--b <path>`).  
* **Schema gate.** Each file must validate against its owning chart JSON Schema (titles-only pointer; schema lives in **HDE-Schemas & Artifacts**).  
* **Canonical JSON gate.** Files must be UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF; arrays-as-sets deduped & ASCII-sorted (see **HDE-Schemas & Artifacts** §4).  
* **Typed input error on failure.** Missing/unreadable file, non-JSON, schema failure, or canonicalization failure → **typed input error** (see §5.2) on **stderr**; **stdout empty**.  
* **Locale.** Parsing/validation and byte checks run under `LC_ALL=C`.

  ### **Time-zone overrides (when allowed)**

* **Flags.** Use `--a-tz`, `--b-tz` with **IANA** zone identifiers.  
* **Behavior \[OPEN\]:**  
  1. chart omits tz and no `--*-tz` provided → **\[OPEN\]** (typed error vs default policy).  
  2. both chart tz and `--*-tz` present → **\[OPEN\]** precedence rule.  
* **Invalid tz.** Invalid/unknown IANA tz **must** yield a typed input error (stderr); stdout empty.

  ### **Inline JSON (Speculative)**

* Not defined in this version. If added later, must use the **same schema/canonicalization gates** as file inputs and follow the same **typed-error** posture. Track as **\[OPEN\]**.

  ### **Aliases policy (inputs)**

* **\[OPEN\] decision.** If input-only aliases are accepted, they must normalize via declared alias ledgers (titles-only to **HDE-Schemas & Artifacts** A1/A4/A5) and outputs remain canonical.  
* **v1 default (current):** unknown IDs **hard-fail** with a typed input error; no implicit aliases unless an explicit allow-list is adopted.

  ### **Validation (binary)**

1. **Exists/reads OK:** file present and readable.  
2. **JSON/Schema OK:** parses as JSON and passes the owning chart schema.  
3. **Canonical JSON OK:** UTF-8, no BOM, sorted keys, compact, one LF; arrays-as-sets deduped & ASCII.  
4. **TZ overrides:** when used, tz flags validate as IANA zones; failure → typed input error (stderr); stdout empty.  
5. **Streams:** on any input error, stderr carries the typed error; stdout empty.

**Routing (titles-only).** Canonical JSON rules & chart schemas: **HDE-Schemas & Artifacts**. Governance tokens: **HDE-Governance** (§2.0).

## 3.3 Streams discipline (stdout / stderr) Required‑NowRequired‑NowRequired‑Now

**Rules for command output streams.** Transport acceptance (A7) lives in HDE‑Governance; do not restate it here. Serialization rules are in §6.1/§6.2.

### **Success → stdout**

* On **exit 0**, each command emits its **canonical success payload** to `stdout` and leaves `stderr` empty.

  * For commands whose success payload is the **Reader v1 envelope** (for example, Reader HTTP endpoints, any CLI commands explicitly defined as “Reader‑on‑stdout”), that payload is the six‑key, numeric‑free Reader v1 body defined in §5.1.

  * For commands whose success payload is **compat/admin JSON** (for example, `hdctl showcompat`), the payload is the compat JSON shape defined for that command (e.g. `{ "a": {…}, "b": {…}, "viewer_prefs": {…}, "compat": { "categories": [...], "meta": {...} } }`), not the Reader v1 envelope.

* **Canonical JSON.** All JSON success payloads on stdout must be:

  * UTF‑8 (no BOM),

  * ASCII‑sorted keys,

  * compact (no pretty printing),

  * terminated by exactly **one** `\n`,

  * with arrays‑as‑sets deduped and ASCII‑sorted.

* **Reader parity.**

  * When a command is defined to produce **Reader v1 envelope bytes** (either on stdout or via a dedicated reader‑dump path such as `--dump-reader`), those bytes **must equal** the Reader API body for the same inputs and environment.

  * For `hdctl showcompat`, Reader parity is defined between the Reader API success body and the `--dump-reader` sidecar file, not the compat JSON stdout payload.

### **Usage & typed errors → stderr**

* **Usage (exit 64).** Print a short human synopsis to `stderr`; `stdout` empty.

* **Typed errors (exit 2).** Print a numeric‑free error object (see §5.2) to `stderr`, LF‑terminated; `stdout` empty.

* Error JSON must use the same canonical JSON rules and single emitter as success payloads.

### **No mixed streams**

* Do **not** interleave diagnostics with public bytes.

* Logs/diagnostics go to `stderr` or files; **never** into stdout payloads.

* No secrets/PII in logs; redact if referenced.

### **Determinism pins**

* For the same inputs and flags, outputs (payload bytes, error bytes, and exit code) must be **stable** (**two‑run identity**).

* All JSON emitted must follow §6.1 canonicalization.

* Locale/encoding pins: run under `LC_ALL=C`; UTF‑8 only; single LF terminator; no BOM/ANSI.

### **Validation (binary)**

1. **Success (0):** `stdout ==` the command’s **canonical success payload** (byte‑for‑byte); `stderr` empty.

   * For Reader‑envelope commands, the canonical success payload is the six‑key Reader v1 body (§5.1).

   * For `hdctl showcompat`, the canonical success payload is compat JSON stdout (§4.1/§5.1).

2. **Error/usage:** `stderr` is LF‑terminated (JSON or synopsis); `stdout` empty.

3. **No ANSI / no extra lines:** grep‑guards block escape sequences; exactly one trailing LF.

4. **Canonical compare:** re‑serialize JSON payloads and byte‑compare (must match); checks run under `LC_ALL=C`, `TZ=UTC`.

5. **Reader parity:** for any surface that emits Reader v1 bytes (Reader HTTP \+ CLI reader‑dump surfaces), those bytes are **byte‑identical** across Reader and CLI for identical inputs/environment.

6. **Determinism:** two‑run identity holds for both success and error paths.

**Routing (titles‑only).** Canonical JSON rules and chart schemas live in **HDE‑Schemas & Artifacts**; governance tokens and A7 posture live in **HDE‑Governance**.

## **3.4 Exit codes taxonomy \[Required-Now\]**

Exit codes are exhaustive for the public surface. **Non‑zero** exits must **not** print partial payloads on stdout. All JSON emitted uses the **single presenter/emitter** (§6.2) and **canonical JSON** (§6.1).

#### **Codes**

* **0 — Success.** Print the command’s **canonical success payload** to `stdout`, LF‑terminated; `stderr` empty.

  * For Reader endpoints and CLI commands whose success payload is the Reader v1 envelope, this is the six‑key Reader v1 body (§5.1).

  * For `hdctl showcompat`, this is the compat JSON payload defined in §§4.1/4.7/5.1 (admin/test compat JSON), not the Reader v1 envelope.

* **64 — Usage/config error.** Print a short synopsis (human text) to `stderr`; `stdout` empty. Use 64 for: missing/unreadable input; invalid flags/combination; JSON parse failure; schema failure; canonicalization failure (e.g. non‑UTF‑8, BOM, unsorted keys, pretty/indented, missing final LF); invalid IANA tz in `--*-tz` (when allowed).

* **2 — Typed failure (runtime/transport/vendor).** Print a numeric‑free **typed error** JSON to `stderr`; `stdout` empty. Use 2 for: SAFE‑rails refusal (rails closed), DB connectivity failure in non‑dev, invalid env (e.g. missing `HD_API_KEY`) with no network I/O, and vendor/transport errors (HTTP 4xx/5xx, network failures). Deterministic 429 may include `retry_after_ms` (int ≥ 0); otherwise omit.

* **1 — Unhandled error (internal).** Reserve for unexpected failures; print typed error JSON to `stderr`; `stdout` empty. Treat as a bug until triaged.

  #### **Global rules**

* **No mixed streams.** Non‑zero exits print only to `stderr`; `stdout` empty.

* **No partial payloads.** Never print fragments of the success payload on stdout/stderr for non‑zero exits.

* **Hygiene.** No ANSI; one LF terminator; UTF‑8 only; no BOM.

* **Determinism.** For the same inputs/flags, exit code and emitted bytes are stable (two‑run identity); AB↔BA does not alter exit code or error bytes.

  #### **Validation (binary)**

1. **Success (0):** `stdout ==` the command’s canonical success payload (byte‑for‑byte); `stderr` empty.

2. **Usage (64):** `stderr` shows synopsis; `stdout` empty; grep‑guard confirms **no JSON payload**.

3. **Typed failure (2):** `stderr` is LF‑terminated canonical JSON error; `stdout` empty.

4. **Canonical checks:** re‑serialize any JSON and byte‑compare (must match); one LF; no BOM/ANSI.

5. **Error parity:** for equivalent error scenarios, Reader error body and CLI stderr are byte‑identical.

6. **Determinism:** two‑run identity and AB↔BA parity hold for error paths as well as success.

**Routing (titles‑only).** Canonical JSON rules: **HDE‑Schemas & Artifacts**. A7 transport rules and SAFE rails: **HDE‑Governance** and §5.3 of this document.

**Evidence (titles-only; indexed via PF12)**

* Exit-0 success stdout snapshot (one LF)  
* Exit-64 synopsis stderr snapshot; ANSI/JSON guards  
* Exit-2 typed error stderr snapshot; LF/encoding checks  
* Reader↔CLI error parity snapshot  
* Two-run identity logs for all code paths

**Routing (titles-only).** Canonical JSON rules: **HDE-Schemas & Artifacts (§4)**. A7 transport rules: **HDE-Governance (A7)** and **§5.3**. SAFE rails / vendor posture: **HDE-Governance (§3)**.

---

## **3.5 Single-emitter parity with Reader**

* **One entrypoint.** CLI must call the **same presenter/emitter** used by Reader (see §6.2). Output is UTF-8, ASCII-sorted keys, compact separators, exactly **one LF**.  
* **No ad-hoc serialization.** Forbid `json.dumps(`, `jsonify(`, templating, or any local “mini-emitters” on public paths.  
* **Symbol allow-list and CI guard.** Pin the presenter/emitter symbol as the only allowed public serializer. CI must fail if public paths reference other serializer symbols or contain disallowed patterns (grep-guard). Tests must assert that CLI and Reader import and call the **same emitter symbol**.  
* **Preimage recipe.** Build the preimage as defined in **PF01** (do not restate fields here), compute `idempotence_hash`, then re-emit the final six-key body.  
* **Determinism & parity.** A single emitter guarantees Reader↔CLI byte equality, **AB↔BA parity**, and **two-run identity** for identical inputs/environment.  
* **Evidence.** Provide (1) grep-guard report, (2) import graph/reflection proof of the shared symbol, and (3) byte-compare fixtures showing CLI stdout equals Reader body. **Evidence is indexed in PF12** (records-only; titles-only).

  ## **3.6 Determinism expectations for stdout**

* **AB↔BA parity.** For identical inputs differing only by pair order, stdout bytes are identical (including the single trailing LF).  
* **Two-run identity.** Running the same command twice with the same inputs/environment produces byte-identical stdout.  
* **Schema & shape gates.** The printed body must validate the six-key covenant and `{id,band}` policy (see §2.1–§2.2); any violation results in a typed error to stderr with exit 2\.  
* **Locale/TZ pins.** All CLI tests and byte comparisons run under `LC_ALL=C` and, where relevant, `TZ=UTC`.

  ## **3.7 Interim “no-user” QA mode (pre-Glow prod)**

**Status.** Informative for HDE-EPIC017 Live QA. CLI bytes and flag semantics in this document remain canonical; this subsection constrains **how** those commands are used in the current production environment until a Glow App user model exists.

**Environment premise.**

* No app-level user model is integrated with the HD Engine.

* No persistent user-bound BodyGraph records exist in production.

* We must not create app-like user records in prod ahead of Glow App integration.

**Compat & Reader (`hdctl showcompat`).**

* For pre-Glow prod QA, use `hdctl showcompat` with **birth arguments only** as the primary compat harness:

  * `--birthdate-a/-b`, `--birthtime-a/-b`, `--location-a/-b`.

* In this environment, **set `--source vendor` explicitly** for birth-based compat runs. The default source selection may follow DB/auto paths that are blocked or misconfigured when there is no user model.

* Do **not** use `--user-a` / `--user-b` or `--source=db` in prod QA until a user model is live and an epic explicitly re-opens DB-backed compat flows.

* AB↔BA identity, two-run identity, canonical JSON, and Reader↔CLI parity are still required and are exercised via birth-based compat plus `--dump-reader`.

**Aux narratives (`hdctl aux-preview`).**

* Drive `hdctl aux-preview` from compat JSON produced by the **birth-based** `showcompat` flow.

* Do not rely on DB users or user-bound BodyGraph rows for Aux tests in pre-Glow prod.

**BodyGraph resolver & vendor ingest (`hdctl bg:resolve`).**

* In pre-Glow prod QA, treat `--user` keys as **ephemeral QA identifiers**, not stable app user IDs.

* Allowed in prod:

  * `bg:resolve` with `--source=db` or `--source=auto` in **stub** mode when there is no real DB behind the adapter.

  * `bg:resolve --source=vendor` under **closed rails** as a typed refusal (no network I/O).

  * `bg:resolve --source=vendor --dry-run` under **open rails** for a single vendor call that returns ingest metadata and does **not** write DB rows that look like app user records.

* Disallowed in prod until a Glow App user model exists:

  * `bg:resolve --source=vendor --upsert` (no vendor-driven writes that appear to create user-bound BodyGraph records).

**Evidence skeleton (CLI QA).**

* Live QA runs that only execute the flows above are expected to be **behaviorally read-only** with respect to governed evidence.

* Snapshot the Evidence Index and machine mirror before and after CLI QA runs; treat any mutation as a defect or unexpected side effect and remediate before closing epic-level acceptance.

**Forward plan.**

* A future epic, once a Glow App user model and user IDs exist, will re-run EPIC017-style QA with **real app user IDs**, exercise DB-backed `showcompat` and `bg:resolve --source=vendor --upsert` semantics in prod or stage, and close any remaining tokens that require real user-bound DB coverage (see **HDE-Phased Epics** and **Glow QA Guide** by title).

  ---

# 4\. Commands (by status)

*This section keeps the existing requirements as canon and adds per‑command implementation status based on the Codex CLI audit (no code changes were made in the audit). The audit reports a single `hdctl showcompat` subcommand; this version reconciles all `showcompat` behaviour into §4.1, and §4.7 now routes to that single spec.*

---

## 4.1 hdctl showcompat Implemented;Required‑NowImplemented; Required‑NowImplemented;Required‑Now

### 4.1.1 Purpose and posture (normative)

`hdctl showcompat` is the canonical compat harness for:

* Computing the full Magic‑10 compat result (scores, bands, narrative keys) for a pair of BodyGraphs; and

* Producing both:

  * **Compat JSON** on stdout for admin/QA (full compat detail: all categories, bands, scores, narrative keys); and

  * An optional **Reader v1 success envelope** (six‑key, numeric‑free) via its **reader‑dump** path, byte‑identical to the Reader API.

It is an admin/QA tool, not a public API. It is **implemented** in the CLI but remains **merge‑blocking** until determinism and Reader↔CLI parity tokens are proven green.

*Single emitter.* All JSON surfaces (stdout compat JSON, reader‑dump envelope, admin sidecars) must use the single canonical presenter/emitter shared with Reader (§6).

### 4.1.2 Inputs — flags and normalization (normative)

`showcompat` supports three input families for the *pair* of BodyGraphs; flags below are as reported by the Codex CLI audit and are now normative.

**A. DB-backed users**

`hdctl showcompat --user-a <idA> --user-b <idB> [--source {db|vendor|auto}]`

`# or`

`hdctl showcompat --a-user <idA> --b-user <idB> [--source {db|vendor|auto}]`

* `--user-a` / `--a-user`, `--user-b` / `--b-user` are **engine user keys**. In the long run they are expected to align with Glow App user IDs; in pre-Glow prod QA (EPIC017) they are used as **ephemeral QA keys** and do not correspond to a real app user model.

* `--source {db|vendor|auto}` has the same semantics as `bg:resolve` (§4.6):

  * `db` — read both BodyGraphs from DB only (no vendor I/O).

  * `vendor` — resolve both from vendor only; vendor calls are allowed **only** when SAFE rails are open (see Rails interaction below). On success, the resolved BodyGraphs may be upserted according to the adapter policy in the **HDE-Mechanics Guide** (titles-only).

  * `auto` — DB-first, vendor-fallback per user key, following the adapter’s environment policy (**HDE-Mechanics Guide** / **HDE-Governance**; titles-only).

* **Pre-Glow prod QA constraint (informative).** Because there is currently no app-level user model or persistent user-bound BodyGraph table in production, DB-backed `showcompat` flows (`--user-*` with `--source=db` or `--source=auto`) and vendor-backed user upserts are **blocked by environment** in prod QA and are exercised only in closed-rails dev/QA harnesses. For EPIC017 Live QA, compat/Reader acceptance is proved via **birth-based** flows; see §3.7 for the interim “no-user” QA mode.


**B. File‑based BodyGraph fixtures**

`hdctl showcompat --pair-file <path>`

`# legacy spelling --file <path> is treated as an alias when present in code; the canonical flag is --pair-file.`

* `<path>` is a **compat input fixture** containing the two BodyGraphs and any required metadata.

* No DB or vendor access occurs in this mode; all data is taken from the fixture.

* The file **MUST** be UTF‑8, canonical JSON, and validate against the owning compat/BodyGraph fixture schema (titles‑only to HDE‑Schemas & Artifacts).

**C. STDIN**

`cat compat_input.json | hdctl showcompat --stdin`

* Reads BodyGraphs and metadata for the pair from STDIN.

* No DB or vendor access occurs in this mode.

**Normalization (AB↔BA).**

Before invoking compat math, `showcompat` **must normalize the pair** into a canonical order (AB↔BA neutral). The compat engine sees a canonical `(a,b)` regardless of flag order or input ordering.

**Rails interaction.**

* For `--source=db`, `showcompat` must **never** perform vendor I/O.

* For `--source=vendor` or `auto` paths that require a vendor call:

  * Vendor I/O is allowed **only** when `SAFE_MODE=0` and `ALLOW_NETWORK=1`.

  * With rails closed (default in dev/CI), a vendor‑required run must **fail closed** with a typed refusal (no network).

* Rails resolution uses the same `_resolver_env()` mechanism as `bg:resolve` (SAFE rails and env policy are titles‑only in Governance/Mechanics).

### 4.1.3 Output surfaces and shapes (normative)

### **4.1.3 Output surfaces and shapes (normative)**

`showcompat` has **two** primary byte surfaces and optional admin sidecars:

1. **Compat JSON to stdout (admin/test surface)** — **primary** CLI output.

2. **Reader v1 success envelope via reader-dump** — **secondary parity surface**.

3. **Admin sidecars** — optional, file-backed diagnostics.

All JSON surfaces:

* Use the single canonical emitter (§6).

* Are UTF-8 (no BOM), ASCII-sorted keys, compact, exactly **one trailing LF**.

* Treat arrays that represent sets as deduped and ASCII-sorted.

  ---

**1\) Compat JSON — stdout (primary)**

On success, and **in the absence of explicit reader-dump overrides**, `showcompat` **MUST** write a single LF-terminated compat JSON object to **stdout**, and **MUST NOT** print the Reader v1 envelope directly to stdout.

**Envelope (informative outline).**  
 Compat JSON is a single object, canonically emitted, whose high-level shape is:

* `{`  
*   `"a": { … },`  
*   `"b": { … },`  
*   `"viewer_prefs": { … },`  
*   `"compat": {`  
*     `"categories": [ … ],`  
*     `"meta": { … }`  
*   `}`  
* `}`


*The exact internal schema (fields for scores, bands, narrative keys per category, and identity fields) is owned by this document (later sections) and the HDE-Mechanics Guide (titles-only), and is **not** the Reader v1 envelope.*

**Semantics.**

* `a` / `b` describe the pair participants and resolved BodyGraphs for this compat run.

* `viewer_prefs` captures viewer-preference inputs where applicable (for example `top_category` and weights across the Magic-10 set). In pre-App QA contexts it is expected to be present but neutral (equal weights) unless the test explicitly varies it.

* `compat.categories[*]` carries per-category compat details (including scores, bands, and narrative selection keys) for the full Magic-10 set; the **public** Reader envelope continues to expose only `"harmony"` and bands (§5.1).

* `compat.meta` carries **CLI/local compat identity**, not the prod engine identity:

  * In CLI contexts (including dev Codespaces), `meta.engine_tag`, `meta.invocation_tag`, and `meta.release_id` describe the **engine instance and invocation used by the CLI** (for example `hdengine-dev`, `INV-LOCAL`, or an all-zero `release_id` in early QA).

  * These values **may differ** from the prod Reader identity reported by `/internal/version` on Railway (`engine_tag: "hdengine@prod"`, non-zero `release_id`, etc.). The authoritative source for prod engine identity remains the `/internal/version` ops endpoint and the Reader v1 envelope on Railway, as governed by **HDE-Governance** and **HDE-Mechanics Guide** (titles-only).

  * QA and tooling **must not** treat compat.meta as proving the identity of a remote prod engine; it is a local/CLI identity context used for debugging and evidence tagging.

**Streams.**

* On success: stdout \= single compat JSON document; stderr empty.

* Errors and usage go to **stderr** only (see §3.3/§3.4).

Compat JSON is an **admin/test surface only**; it is not a public Reader payload.

---

**2\) Reader v1 success envelope — reader-dump path**

When the `--dump-reader <path>` flag is present, `showcompat` **MUST**:

* Compute the Reader v1 success envelope (six keys; numeric-free) for the resolved pair, using the same `emit_reader_public_envelope` path as the Reader API.

* Serialize it with the single emitter as canonical JSON (UTF-8, sorted keys, compact, one LF).

* Write those bytes to the target file `<path>` (0600 permissions recommended; enforcement details in HDE-Mechanics Guide; titles-only).

* Ensure the resulting bytes are **byte-identical** to the Reader 200 success body for the same inputs/environment.

The Reader v1 envelope **MUST NOT** be extended with compat scores or narrative fields. It remains:

* `{`  
*   `"reader_version": "v1",`  
*   `"eligible": …,`  
*   `"categories": [ { "id": "harmony", "band": "Cool|Open|Warm|Glow" } or [] ],`  
*   `"meta": { "engine_tag": "...", "invocation_tag": "..." },`  
*   `"release_id": "<hex64>",`  
*   `"idempotence_hash": "<hex64>"`  
* `}`


(Full covenant and preimage rules live in §5.1 and HDE-Math-Spec / HDE-Governance by title.)

---

**3\) Admin sidecars and diagnostics**

When `--dump-admin-dir <dir>` (or equivalent) is set, `showcompat` MAY emit additional **admin/test files** under `<dir>`:

* Admin compat JSON snapshots (potentially richer than stdout, e.g., extra diagnostics), written via the canonical emitter.

* SHA-256 sidecars (`.sha256`) for each artifact.

* Additional logs needed for acceptance tokens (AB↔BA, two-run, preimage recompute), titles-only referenced in HDE-Schemas & Artifacts / HDE-Mechanics Guide.

Admin sidecars:

* Must never alter the public Reader v1 envelope shape.

* Must never be treated as public API bytes.

* Must remain numeric-free where they mirror public envelopes; compat-internal numerics remain admin-only.

### 4.1.4 Errors and exit codes (normative)

Exit codes follow §3.4. The mapping for `showcompat`:

* `0` — success: compat JSON on stdout; stderr empty. Reader‑dump/admin sidecars may be written when their flags are present.

* `64` — usage/config error: short synopsis to stderr; stdout empty.

* `2` — typed failure: numeric‑free error object on stderr (LF‑terminated); stdout empty.

* Other non‑zero codes are reserved; in all cases stdout remains empty.

Error envelopes and streams follow §5.2.

### **4.1.5 Determinism, parity, environment, and acceptance (normative)**

**Determinism (compat JSON and Reader envelope).**

For a fixed pair and environment:

* **AB↔BA parity.** Swapping the pair inputs (`a`,`b`) yields byte-identical compat JSON on stdout and a byte-identical Reader envelope (when produced).

* **Two-run identity.** Running the same command twice with the same inputs/flags/environment produces identical stdout bytes and identical reader-dump bytes (if enabled).

* **Canonical JSON.** Re-serializing outputs via the canonical emitter must yield identical bytes.

**Reader vs CLI parity.**

* When CLI produces Reader v1 bytes via `--dump-reader`, those bytes **MUST** be byte-identical to the Reader 200 body for the same inputs/environment.

**Environments for `showcompat` acceptance (dev harness vs vendor-backed).**

The behavior and tokens for `hdctl showcompat` are **environment-agnostic**: the same determinism, parity, and canonical JSON rules apply whether `showcompat` is exercised against:

* a **dev harness** Reader surface with rails closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`), or

* a **vendor-backed engine** with rails open (`SAFE_MODE=0`, `ALLOW_NETWORK=1`) that may resolve BodyGraphs via vendor HTTP subject to the Vendor Ingest rules in §7.

This section constrains the CLI and transport bytes; it does **not** pick a single canonical environment. Instead:

* In **dev/CI** contexts, `CLI_SHOWCOMPAT_CANON_OK` and related tokens may be satisfied via:

  * `hdctl showcompat` invoking the compat engine locally and/or via a **dev harness** Reader route that runs entirely with closed rails (no vendor I/O), and

  * evidence that AB↔BA parity, two-run identity, canonical JSON, and Reader↔CLI parity hold under those closed-rails conditions.

* In **vendor-backed QA** contexts (for example Live QA from Codespaces to Railway prod), the same tokens may be exercised via:

  * `hdctl showcompat` calling a vendor-backed engine with rails explicitly opened (`SAFE_MODE=0`, `ALLOW_NETWORK=1`), and

  * evidence that, even in this open-rails environment, the compat stdout payload is canonical and the Reader v1 envelope bytes produced by the engine still satisfy the determinism and parity requirements above.

The QA guide and epic records (by title only) **must declare** which environment is canonical for a given epic’s `CLI_SHOWCOMPAT_CANON_OK` and related tokens; PF05 provides the byte-level contract and rails constraints that must hold in whichever environment is chosen.

**Acceptance tokens (names-only).** At minimum:

* `CLI_SHOWCOMPAT_CANON_OK` — stdout compat JSON uses canonical emitter and canonical JSON rules in the chosen environment (dev harness or vendor-backed), with non-empty, LF-terminated bytes.

* `CLI_STDOUT_LF_OK` — exactly one trailing LF on stdout compat JSON.

* `PARITY_AB_BA_OK` — AB↔BA identity for stdout compat JSON and reader-dump envelope in the chosen environment.

* `TWO_RUN_IDENTITY_OK` — two-run identity for stdout compat JSON (and reader-dump when enabled).

* `CLI_READER_PARITY_OK` — reader-dump bytes equal the Reader 200 body for the same inputs/environment.

* `JSON_CANONICAL_CHECK_OK` — global canonicalization checks pass for compat JSON and Reader envelopes.

* `PREIMAGE_RECOMPUTE_OK` — idempotence preimage recompute for Reader envelope `idempotence_hash` passes.

* `CLI_IMPLEMENTED_SET_OK` — command present and wired as specified.

These token names are owned by Governance and the QA guide; this section constrains the underlying `showcompat` behavior so that the tokens can be evaluated consistently in either dev harness or vendor-backed environments.

**Evidence surfaces (titles-only; PF12 owns schema).**

Examples (names may be adjusted in PF12):

* `cli/showcompat/stdout` — exact stdout compat JSON bytes (non-empty; LF-terminated) plus sha256.

* `cli/showcompat/two_run` — two-run identity log.

* `cli/showcompat/abba` — AB vs BA stdout diff (expected empty).

* `cli/reader_vs_cli` — Reader vs CLI reader-dump envelope diff (expected empty).

* `cli/showcompat/preimage_recompute` — preimage recompute log for Reader envelope `idempotence_hash`.

Evidence must clearly indicate which environment (dev harness vs vendor-backed) each capture represents. All records must be indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` in the same PR, per PF12.

### 4.1.6 Implementation status (audit v1)

* **Implementation status:** Partially implemented.

* **Evidence (audit).** The Codex audit reports:

  * A `hdctl` console script wired to `engine.cli.main:cli`, with a `showcompat` subcommand supporting:

    * `--pair-file`, `--a-file/--a`, `--b-file/--b`,

    * DB/vendor options `--user-a/--user-b`, vendor birth tuple flags,

    * `--dump-reader`, `--dump-admin-dir`, `--viewer-prefs-file`,

    * and `--source {db,vendor,auto}`.

  * Legacy scripts `scripts/hd_cli.py` and `scripts/hdctl.clean.py` expose similar compat flows (file‑based charts, canonical JSON, optional admin output).

* **Gaps (audit).**

  * The audit does **not** inspect the exact compat JSON schema, does not confirm the six‑key Reader envelope is only produced via `--dump-reader`, and does not validate AB↔BA/two‑run identity, preimage recompute, or token evidence names above.

  * Numeric scores and narrative keys are known to exist in admin compat JSON; the audit does not verify that they are restricted to admin/test surfaces and omitted from the Reader envelope.

The canonical behaviour is now specified in §4.1/§5.1; any divergence in code is a defect until corrected or explicitly re‑canonized.

### **4.1.7 Stateless compat export mode (gap; no-DB JSON QA)**

**Purpose (normative, future-epic).**  
 Provide a **no-DB JSON QA mode** for compat that:

* Takes only **birth tuples** and/or **BodyGraph JSON files** as inputs,

* Calls the compat engine directly (no DB reads, no user-ID lookups), and

* Writes both **compat JSON** and the **Reader v1 envelope** to governed JSON artifacts, so QA can exercise compat, AB↔BA identity, two-run identity, narratives, and Reader parity **without** an app DB or user IDs.

This capability is a **Calcination gap** recorded in Build Notes (Addendum 11). It is required for future calcination/separation/conjunction epics that want to QA engine math independently of any app user model and persistence.

**Inputs (stateless compat harness).**

In addition to the existing input families in §4.1.2, `showcompat` **MUST**, in a future epic, support a stateless QA mode that:

* Accepts **either**:

  * two BodyGraph export JSON files (produced by `hdctl bg:export-json`; see §4.8), **or**

  * two birth tuples (equivalent to the vendor birth payload) that can be resolved via a **dry-run** vendor path, without DB writes; and

* Does **not** require `--user-a` / `--user-b` or any DB-backed `--source=db`/`auto` behaviour.

Exact flag names and wiring (`--export-dir`, `--from-bodygraph`, etc.) are **\[OPEN\]** and will be pinned in a future Doc-Delta; this section constrains behaviour, not the CLI UX.

**Outputs (files, not DB).**

In stateless compat export mode, `showcompat` **MUST**:

* Call the compat engine directly using the provided BodyGraph inputs (or the derived BodyGraph from vendor dry-run), without reading from or writing to DB; and

* Emit, under governed repo paths (for example `artifacts/hdctl/…` or `artifacts/qa/…` — exact locations and schemas are owned by **HDE-Schemas & Artifacts**):

  1. A **compat JSON** file containing the full admin/test compat structure (scores, bands, narrative selection keys per category) as defined in this document and **HDE-Mechanics Guide** (titles-only), and

  2. A **Reader v1 envelope** JSON file containing the six-key, numeric-free public body defined in §5.1 (and HDE-Math-Spec / HDE-Governance by title), such that:

     * both files are canonical JSON (UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets deduped and ASCII-sorted), per §6.1 and **HDE-Schemas & Artifacts**, and

     * the Reader v1 file is **byte-identical** to the Reader 200 success body for the same inputs/environment.

Compat stdout behaviour for the general case remains as in §4.1.3: compat JSON on stdout, and optional `--dump-reader` sidecars. The stateless export mode adds **file-backed** outputs for QA; it does **not** change the public Reader envelope.

**Rails and DB posture (informative).**

* In the stateless compat export mode, `showcompat` **must not**:

  * create or update DB rows that look like app users, or

  * depend on an app-level user model or user IDs.

* Vendor use (if any) **must** follow §7.1/§7.2/§7.3 SAFE rails and dry-run semantics (no writes) and be clearly separated from any future `--upsert`/DB-binding behaviour.

**QA and evidence hooks (titles-only).**

* QA harnesses (defined in **HDE-Mechanics Guide** and **Glow QA Guide**) will use the stateless compat export mode to run AB↔BA, two-run, Reader parity, and narrative tests entirely from files.

* Schemas and evidence records for compat export JSON and stateless Reader-envelope files are owned by **HDE-Schemas & Artifacts**; PF05 references them by title only.

**Implementation status.**

* **Not implemented.** This subsection records a **required capability and gap**. Current EPIC017 Live QA uses birth-based `showcompat` plus `--dump-reader` and cannot yet produce a full no-DB JSON run bundle. A future epic (for example “Stateless JSON Export & QA Harness”) must:

  * Wire this mode into the CLI,

  * Pin schemas and artifact paths in **HDE-Schemas & Artifacts**, and

  * Add the corresponding evidence entries and tokens in **HDE-Mechanics Guide**, **Glow QA Guide**, and **HDE-Phased Epics**.

---

## 4.2 hdctl read singlebg SpeculativeSpeculativeSpeculative

*(Unchanged in spirit; shown here only for completeness with minor wording aligned to Option B. No new semantics were invented.)*

**Purpose (normative, draft).**  
 Emit a single‑chart diagnostic to stdout using the same canonical emitter as Reader/CLI success bodies (UTF‑8, sorted keys, compact, exactly one LF). This command is for testing & debugging chart ingestion/normalization; it is not a product surface. It does **not** change the Reader v1 public envelope.

**Inputs, stdout schema, errors, and acceptance** remain as in the existing PF05 text (single‑chart file input, optional tz override, schema gate, canonical JSON, two‑run identity, stderr‑only errors). No dependency on compat JSON or narratives.

Implementation status (audit v1): **Not implemented**; see existing PF05 language for details.

---

## 4.3 hdctl list people SpeculativeSpeculativeSpeculative

*(Unchanged; still speculative developer convenience for local people store listing.)*

---

## 4.4 Fetch commands (person/batch) Speculative;disabledinAlphaSpeculative; disabled in AlphaSpeculative;disabledinAlpha

*(Unchanged; still disabled by design; rails, privacy, and determinism constraints remain as previously specified.)*

---

## 4.5 CLI Admin Preview (narrative) Required‑NowRequired‑NowRequired‑Now

*(Unchanged in substance.)* `hdctl aux-preview` remains the admin preview surface for Aux narrative text and IDs, reading compat JSON from `--pair-file` and calling the Aux emitter. It must **not** change Reader 200 bytes; it is admin‑only and LF‑only.

---

## 4.6 hdctl bg:resolve Required-NowRequired-NowRequired-Now

`hdctl bg:resolve` is the operator command for resolving a single BodyGraph for a given key and data source.

**Inputs and sources (normative).**

* `--user <id>` — engine user key. In the long run it is expected to align with a Glow App user ID; in pre-Glow prod QA it is used as an **ephemeral QA key** and not as a durable app user identifier.

* `--source {db|vendor|auto}` selects the data source:

  * `db` — resolve from DB only (no vendor I/O).

  * `vendor` — resolve from vendor only; vendor HTTP calls are allowed **only** when SAFE rails are open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`). Shaping and error mapping follow §7.1/§7.2/§7.3 and the policies in **HDE-Governance** and the **HDE-Mechanics Guide** (titles-only).

  * `auto` — DB-first, vendor-fallback according to the adapter’s environment policy (HDE-Mechanics Guide; titles-only).

* Implementations MAY expose `--dry-run` and `--upsert` switches; when present they must follow the vendor rails and adapter data-source policy in §7.1/§7.4 and the **HDE-Mechanics Guide** (titles-only).

**Outputs and streams.**

* On success, `bg:resolve` prints the resolved BodyGraph JSON to **stdout** using the single canonical emitter (UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets deduped and ASCII-sorted).

* Typed failures and usage errors follow the error and exit-code taxonomy in §3.3/§3.4/§5.2: errors go to **stderr** only; stdout is empty.

**Pre-Glow prod QA constraint (informative).**

* In the current pre-Glow production environment there is no app-level user model and no persistent user-bound BodyGraph table. For EPIC017 Live QA:

  * `--user` is treated as an **ephemeral QA key**.

  * Allowed flows in prod are:

    * `bg:resolve` with `--source=db` or `--source=auto` in **stub** mode when no real DB is configured behind the adapter.

    * `bg:resolve --source=vendor` under **closed rails** as a typed refusal (no network I/O).

    * `bg:resolve --source=vendor --dry-run` under **open rails** for a single vendor call that returns ingest metadata and does **not** write DB rows that look like app user records.

  * `bg:resolve --source=vendor --upsert` **must not** be used in prod until a Glow App user model exists and a future epic explicitly re-opens user-bound upsert flows.

These constraints do not change the CLI bytes or flags defined elsewhere in this document; they constrain how `bg:resolve` is used in pre-Glow prod QA. Once a user model exists and DB-backed flows are re-opened by a later epic, this subsection remains as historical context for how EPIC017 was exercised.

---

## 4.7 Implementation Matrix (audit v1)

Update rows that refer to `showcompat` to point to §4.1 and reflect Option B:

| Requirement / area | Spec location | Status from audit | Key CLI touchpoints | Gap / note |
| ----- | ----- | ----- | ----- | ----- |
| hdctl showcompat – compat harness & AB/BA | §4.1 | Partially implemented | `hdctl` subcommand `showcompat`; `scripts/hd_cli.py`, `scripts/hdctl.clean.py` | Command/flags exist; emits compat-related JSON; audit does not confirm final stdout compat JSON schema, AB↔BA harness, or two-run identity. |
| hdctl read singlebg – single-chart diagnostic | §4.2 | Not implemented | None reported | No `read singlebg` subcommand; single-BG diagnostic surface not exposed as such; `bg:resolve` is partial substitute. |
| hdctl list people | §4.3 | Not implemented | None reported | No people-listing command; table/JSON listing behaviour remains speculative. |
| Fetch commands (person/batch) | §4.4 | Not implemented | None reported | No `fetch` CLI commands; feature remains disabled/speculative as intended. |
| CLI Admin Preview (HTTP Aux emitter) | §4.5 | Partially implemented | `hdctl aux-preview` | `aux-preview` exists and calls Aux emitter; audit does not cover HTTP admin surface, LF discipline, or evidence/indexing. |
| hdctl bg:resolve – BodyGraph resolver | §4.6 | Partially implemented | `hdctl` subcommand `bg:resolve` | Flags and env handling implemented; audit does not inspect BG schema, rails-closed behaviour, or evidence. |
| Core: compat outputs (scores, bands, narratives) | §4.1, §4.5 | Unknown from audit | `hdctl showcompat`, `hdctl aux-preview`, `scripts/hdctl.clean.py` | Audit mentions compat bands and narrative preview flags, but does not inspect JSON payload to confirm scores/narrative keys per category or schema. |
| Core: BodyGraph data source selection | §4.1, §4.6 | Partially implemented | `hdctl bg:resolve --source`, `hdctl showcompat --source`, `_resolver_env()` | CLI exposes `--source {auto,db,vendor}` and uses env rails; internal resolver semantics and guardrails are not fully audited. |
|  |  |  |  |  |

## **4.8 hdctl bg:export-json Speculative; gap — stateless BodyGraph export**

**Purpose (normative, future-epic).**  
 `hdctl bg:export-json` is the **stateless BodyGraph export** command. It exists to:

* Drive engine **BodyGraph math directly** (no DB read/write),

* Emit a complete BodyGraph export JSON artifact suitable for compat/narratives QA, and

* Enable a fully **no-DB JSON QA mode** when combined with `hdctl showcompat` stateless compat export (§4.1.7).

This command is a **required capability and gap** recorded in Build Notes (Addendum 11). It is not implemented in the current CLI; status is **Speculative; gap** until a dedicated epic delivers it.

### **4.8.1 Inputs (stateless only)**

`hdctl bg:export-json` **MUST**, in a future epic, support:

* **Birth-tuple inputs** equivalent to the vendor BodyGraph payload and existing CLI birth flags, for example:

  * `--birthdate`, `--birthtime`, `--location`, and any existing options that map to the three-key vendor body (`birthdate`, `birthtime`, `location`) as defined in §7.2; and/or

* **Vendor BodyGraph JSON input** (optional):

  * a BodyGraph JSON file previously returned by the vendor in a **dry-run** ingest flow (schema single home in **HDE-Schemas & Artifacts**).

Exact flag names and combinations are **\[OPEN\]** and will be pinned in a later Doc-Delta; this section constrains semantics:

* The command **must not** require an app-level user ID or DB-backed `--source=db` / `--source=auto` modes.

* Any use of `bg:resolve` or vendor HTTP under the hood **must** respect §7.1/§7.2/§7.3 SAFE rails and **dry-run** semantics (no DB writes) unless an explicit, separately-documented `--upsert`\-style switch is provided and enabled in a non-QA context.

### **4.8.2 Behaviour and outputs (no DB, canonical JSON)**

In all success cases, `hdctl bg:export-json` **MUST**:

* Call the engine BodyGraph math directly (no DB reads, no DB writes). The engine remains pure; adapters may use vendor HTTP under SAFE rails but may not touch DB in stateless mode.

* Write a **single BodyGraph export JSON file** under a governed path (for example `artifacts/hdctl/bg_export/…` or `artifacts/qa/…`; exact path and schema are owned by **HDE-Schemas & Artifacts**), containing:

  * **Provenance:** raw birth details used to construct the chart (so audits can trace inputs), and, when applicable, a reference to any vendor response used (IDs only; no full vendor payload).

  * **Full BodyGraph topology:** centers, channels, gates, lines, profile, authority, definition, and type in the canonical forms defined by **HDE-Schemas & Artifacts** and **HDE-Math-Spec** (titles-only).

  * **Registry IDs:** any internal IDs required for downstream compat/narratives (for example IDs that compat uses to look up presets or narratives). Only IDs and structural metadata appear; no narrative text.

* Emit the file as **canonical JSON** using the single emitter (§6.1/§6.2):

  * UTF-8 (no BOM),

  * ASCII-sorted keys,

  * compact separators,

  * exactly **one trailing LF**,

  * arrays-as-sets deduped and ASCII-sorted where appropriate.

Stdout/stderr follow the general rules in §3.3/§3.4:

* On success: stdout may remain empty or print a short, numeric-free synopsis; the exported JSON lives on disk.

* On error: emit a typed error JSON to stderr (`ok:false, code, error`), LF-terminated, with `exit 2`; stdout empty.

### **4.8.3 QA usage and evidence (titles-only)**

**QA harness role.**

* `hdctl bg:export-json` is the **first leg** of the stateless QA pipeline:

  * birth (or vendor BodyGraph) → `bg:export-json` → BodyGraph export JSON → `showcompat` stateless compat export (§4.1.7) → compat JSON \+ Reader v1 envelope files.

* QA plans defined in **Glow QA Guide** and epic records in **HDE-Phased Epics** will use this pipeline to test BodyGraph, compat, and narratives **without DB**.

**Evidence & schemas.**

* Schemas for BodyGraph export JSON and any “run bundle” composite artifacts are owned by **HDE-Schemas & Artifacts**; PF05 **must not** define those schemas.

* Evidence index entries (for example “BodyGraph export JSON golden”, “stateless run bundle”) live in **PF12**; this section simply requires that the CLI surfaces exist and honour canonical JSON and no-DB semantics.

### **4.8.4 Implementation status (gap record)**

* **Current status:** Not implemented; no `bg:export-json` command exists, and no standard BodyGraph export JSON artifact is produced in the repository.

* **Gap:** EPIC017 Live QA is limited to compat/Reader behaviour and cannot fully validate internal BodyGraph derivations in a DB-independent way.

* **Future work:** A dedicated epic (for example “Stateless JSON Export & QA Harness”) must:

  * Implement `hdctl bg:export-json` as specified here,

  * Extend **HDE-Schemas & Artifacts** with BodyGraph export and optional composite “run bundle” schemas, and

  * Wire QA harnesses and evidence (PF14/PF19/PF20) to use these stateless artifacts.

## **4.9 hdctl admin-bundle Required-Now; admin-only**

### **4.9.1 Purpose and posture (normative)**

hdctl admin-bundle is the canonical CLI surface for producing a full admin bundle for a single match. It exists to:

* Compose, for a given pair, the full product payload that already exists in canon:

  * the per-person BodyGraph JSON for each party

  * the full compat JSON for the pair (all categories, scores, bands, narrative selection keys)

  * three narrative compositions for the match

  * a meta block with engine identity and rails context

* Emit that composition as a single canonical JSON object (the admin bundle) for admin, QA, and internal product use.

Posture:

* Admin-only surface. The admin bundle is explicitly not a public Reader response and is not subject to the public numeric-free covenant. It may contain numeric scores and narrative text.

* Pre-Glow product requirement. A build that cannot produce admin bundles via hdctl admin-bundle against Railway prod is considered unusable pre-Glow, regardless of any Admin GUI.

* Not an A7 surface. Admin bundle transport is not part of the A7 proof surface; A7 proofs remain on cataloged Reader JSON success routes only.

The mechanical implementation of the admin bundle builder (pure function or module inside the engine) is owned by the HDE-Mechanics Guide. This section defines the CLI contract that uses that builder.

### **4.9.2 Inputs and environment targeting (normative)**

hdctl admin-bundle takes inputs for a single pair and uses existing resolvers and compat logic; it does not introduce new math.

Pre-Glow, inputs are birth-based. The CLI command must support:

* Either a births-file option that points at a JSON file describing the two parties by birth tuples, or an equivalent structured set of flags for party A and party B birth details

* Future support for user-id based inputs is reserved; when a user model is live, flags for user keys may be added and pinned in this section

Exact flag names are pinned here:

* hdctl admin-bundle

  * Required pair inputs (pre-Glow): either

    * births-file PATH, or

    * a set of birth flags for party A and party B that map to the three-key vendor birth payload (birthdate, birthtime, location) as defined in Vendor Ingest

  * Optional output file flag for the bundle (see below)

  * Optional flags to select input source once a user model exists (user-a, user-b) are reserved for a later Doc-Delta

Environment targeting:

* hdctl admin-bundle must be able to run from any terminal that can reach the Railway production engine, not only from Codespaces.

* Base URL resolution for remote calls is handled via the same configuration rules used for other CLI commands:

  * read the prod engine base URL from Glow-Infrastructure governed configuration (for example a PROD\_ENDPOINTS file or environment variables such as HDE\_BASE\_URL)

  * do not hard-code Codespaces-specific hostnames or ports

  * any host with the same configuration and network reachability must be able to run hdctl admin-bundle

When hdctl admin-bundle needs remote data, it must:

* Use the existing engine resolvers and adapter policy described for showcompat and bg:resolve

* Honor SAFE rails for any vendor calls; rails logic and vendor shaping remain owned by Governance and Vendor Ingest sections

### **4.9.3 Admin bundle JSON shape (normative)**

On success, hdctl admin-bundle produces a single JSON object, the admin bundle, with at least the following top-level keys:

* a\_bodygraph: canonical BodyGraph JSON for person A

* b\_bodygraph: canonical BodyGraph JSON for person B

* compat: canonical compat JSON for the pair (full categories and meta as already defined for compat JSON in this document)

* narratives: array of three narrative compositions for the match, each including at least composition identifiers and text

* meta: meta information about the bundle and environment, including:

  * engine\_tag

  * release\_id

  * invocation\_tag or equivalent invocation marker

  * bundle source (CLI, GUI, or other)

  * any rails context needed for audit (for example whether the bundle was built using birth-based inputs or user IDs when available)

Semantics and constraints:

* a\_bodygraph and b\_bodygraph reuse the existing canonical BodyGraph JSON shape defined in the HDE-Math-Spec, HDE-Mechanics Guide, and HDE-Schemas and Artifacts. This section does not restate their internal schema.

* compat reuses the existing compat JSON shape already specified for hdctl showcompat:

  * categories covers the full Magic-10 set with scores, bands, and narrative selection keys for each category

  * compat meta continues to carry compat-level identity and viewer preference context

* narratives contains exactly three entries:

  * each entry includes at least:

    * the composition identifier used by the narrative engine

    * a pack identifier or SHA that identifies the narrative pack

    * the narrative text itself

  * the exact internal schema of each narrative entry is owned by the HDE-Narratives Guide and HDE-Narrative Deliverables; this section pins the requirement that three narrative compositions for the match are present

* meta is part of the admin-only surface. It may include identifiers used to correlate this bundle with other logs and evidence; it is not the public Reader identity.

The admin bundle must be:

* canonical JSON emitted by the single presenter/emitter:

  * UTF-8 without BOM

  * keys sorted in ASCII order

  * compact separators

  * exactly one trailing newline character

  * any arrays that represent sets deduplicated and ASCII-sorted

* admin-only:

  * may contain numeric scores and narrative text

  * not constrained by the numeric-free public covenant that applies to Reader v1 success envelopes

* used consistently across admin surfaces:

  * the CLI admin-bundle command and the admin HTTP route must produce byte-identical bundles for the same inputs and environment

### **4.9.4 Streams, exit codes, and destination (normative)**

hdctl admin-bundle follows the global streams and exit code rules:

* On success (exit 0):

  * either writes the admin bundle JSON to stdout and leaves stderr empty, or

  * writes the admin bundle JSON to a specified output file and prints a short, numeric-free synopsis to stdout, leaving stderr empty

* On usage errors (exit 64):

  * prints a short synopsis to stderr; stdout remains empty

* On typed failures (exit 2):

  * prints a typed error JSON object to stderr using the standard error shape and canonical JSON rules; stdout remains empty

* No mixed streams: public bytes for the admin bundle never interleave with diagnostics

When writing to a file:

* the file must be emitted with canonical JSON and exactly one trailing newline

* the file path must be accepted via an explicit flag and must not overlap with governed Evidence Index paths unless explicitly documented in HDE-Schemas and Artifacts

### **4.9.5 Authentication, authorization, and admin-only gating (normative)**

hdctl admin-bundle must always enforce authentication and authorization before an admin bundle can be obtained:

* A secret admin credential must be required for all admin bundle requests:

  * high-entropy value

  * not checked into the repository

  * stored as a secret in Railway or equivalent infrastructure

* The CLI must present this credential with every admin-bundle request to the engine:

  * for example, via an Authorization header or another explicit header pinned in the admin HTTP route section

* The admin credential must not be printed, logged, or echoed in errors. Keys-only logging posture still applies.

Admin-only gating:

* If the required credential is missing or invalid, the engine must:

  * reject the admin bundle request

  * return a typed, numeric-free error via the HTTP route

  * surface a typed error on stderr for the CLI

* An unauthenticated request must never receive the full admin bundle.

Post-Glow, authentication for admin surfaces must align with the wider identity and auth model for app admins and users; until that is pinned, this section requires that pre-Glow admin surfaces are not left open in production.

### **4.9.6 Logging, audit, and parity (normative)**

Every successful hdctl admin-bundle call must produce an audit trail:

* Logs must record:

  * the timestamp of the request

  * whether the caller used CLI or an Admin GUI

  * a high-level description of the input:

    * for birth-based runs: that it was a birth-based match for two anonymous parties

    * for future user-based runs: user identifiers used, without including raw birth or other PII

  * a correlation identifier that allows operators to trace the request across logs and systems

Logs must:

* follow keys-only posture (no secrets, no full payload bodies, no vendor responses)

* be governed by Glow QA Guide and HDE-Governance for retention and PII handling

Parity expectations:

* For the same inputs and environment, hdctl admin-bundle and the admin HTTP route must produce byte-identical admin bundle JSON.

* Future QA tokens that enforce:

  * CLI and HTTP admin bundle parity

  * bundle structural completeness (BodyGraphs, compat, narratives, meta present)

  * required authentication for admin surfaces  
     will be owned and named in HDE-Governance and Glow QA Guide. This section requires the underlying behavior and byte equality; token names are referenced there.

## **4.10 hdctl dev:sampler Implemented; dev/admin-only**

### **4.10.1 Purpose and posture (normative)**

`hdctl dev:sampler` is a **dev/admin-only** CLI subcommand that provides an internal harness for the sampler core introduced in HDE-EPIC019:

* It exercises the **sampler core** with a viewer and a set of candidates, using the current sampler rules to produce a ranked candidate list.

* It emits a **single canonical JSON payload** that includes:

  * the viewer identifier used for the run,

  * an optional seed echo, and

  * a list of candidates with ranking and key diagnostic fields.

Posture:

* **Dev/admin-only surface.** `dev:sampler` is a non-public tool for engine developers and admin operators. It is not a user-facing CLI command for Glow App users and is **not** part of the public Reader or Aux contracts.

* **No A7 or public covenant.** The sampler output is internal/admin JSON; it may contain numeric scores, weights, bands, and diagnostic flags. It is not governed by the Reader v1 numeric-free public covenant.

* **No schema ownership.** Any reusable schemas for sampler inputs/outputs live in **HDE-Schemas & Artifacts**; this section defines only the CLI contract and behavior and references schemas by title only.

  ### **4.10.2 Environment gating and rails (normative)**

`hdctl dev:sampler` is **strictly environment-gated** and runs under closed rails:

* **APP\_ENV gate.**

  * The command **MUST** only run when `APP_ENV ∈ {dev, test, local}`.

  * When `APP_ENV` is unset, empty, or set to any other value (including `prod`), `dev:sampler` **MUST** fail fast with a typed CLI error (for example a `DEV_ADMIN_ONLY` style code) on `stderr` and exit with a non-zero code; `stdout` remains empty.

* **Rails posture (closed by default).**

  * Runs under determinism rails pinned by the shared determinism helper:

    * `SAFE_MODE=1`, `ALLOW_NETWORK=0`

    * `LC_ALL=C`, `LANG=C`, `TZ=UTC`

  * `dev:sampler` **MUST NOT** perform network I/O or vendor calls. It operates purely on local JSON input and the in-process sampler core.

* **Determinism.**

  * Under a fixed `APP_ENV ∈ {dev, test, local}` and determinism env pins, `dev:sampler` runs are subject to the same **two-run identity** and canonical JSON requirements as other governed CLI JSON surfaces (§3.3, §6).

### **4.10.3 Inputs and candidates file (normative)**

`dev:sampler` accepts the following inputs:

* `--viewer <viewer_id>` (required)

  * Opaque viewer identifier used by the sampler core. Semantics are owned by the sampler mechanics; PF05 treats it as a string key.

* `--candidates-file <path>` (required)

  * Path to a JSON file describing the candidate pool.

  * The file is read using the existing CLI file helper (`_read_file` semantics; titles-only), and **MUST** obey the global file input rules (§3.2): readable file, valid JSON, canonical JSON (UTF-8, sorted keys, compact, one LF), and schema-conformant for the sampler candidates payload.

  * The payload MAY be either:

    * a top-level JSON array of candidate objects, or

    * a JSON object with a `candidates` array field containing the candidate objects.

  * Any other top-level shape (missing `candidates`, non-array, wrong types) MUST produce a typed input error on `stderr` with a clear error code (for example “INVALID\_CANDIDATES\_PAYLOAD”); `stdout` remains empty.

* `--seed <string>` (optional)

  * Arbitrary string used as a **metadata seed**. In the current implementation it is **echoed only**:

    * It appears in the `seed` field of the output JSON.

    * It does **not** influence candidate ranking or selection.

  * Future versions MAY extend the sampler core to use seed for tie-breaking; any such change MUST preserve determinism (same inputs/seed ⇒ same output) and MUST be accompanied by updated acceptance evidence.

Per-candidate payload (titles-only):

* Each candidate object MUST include an identifier and MAY include additional sampler fields:

  * identifier fields: `person_uid` (preferred) or `id` (legacy) as a string.

  * `weight`: numeric (int/float) weight used by the sampler core.

  * `compat_score`: numeric (int/float) score used by the sampler core.

  * `band`: optional string band label.

  * `diversity_key`: optional string used for diversity balancing.

  * `is_recent`: optional boolean flag.

* The CLI harness MUST:

  * Normalize identifier fields into a single internal candidate identifier (for example preferring `person_uid` over `id` when both are present).

  * Validate that required fields are of the expected type (non-empty string IDs, numeric weights/scores); type mismatches or missing required fields MUST yield a typed input error on `stderr` with a clear error code (for example `INVALID_CANDIDATE_ID`, `INVALID_CANDIDATE_WEIGHT`, `INVALID_COMPAT_SCORE`), and `stdout` remains empty.

All validation and error behavior follows the global CLI input and streams rules in §3.2 and §3.3: on any input error, `stderr` carries a numeric-free error object or synopsis; `stdout` remains empty, and exit code is non-zero.

### **4.10.4 Output JSON and determinism (normative)**

On success (exit code 0), `hdctl dev:sampler` emits a single JSON object on `stdout` with at least:

* `viewer_id` — the `viewer` input value.

* `seed` — the `--seed` argument value if present, otherwise `null`.

* `candidates` — an array of candidate result objects; for each candidate:

  * `person_uid` — the canonical candidate identifier.

  * `score` — numeric score from the sampler core.

  * `weight` — numeric weight used by the sampler.

  * `band` — string band label if available.

  * `rank` — 1-based rank assigned by the sampler core (1 \= highest priority).

  * `diversity_key` — string if present in input; omitted or null otherwise.

  * `is_recent` — boolean if present in input; omitted or null otherwise.

Serialization and determinism:

* The output MUST be produced by the **single canonical emitter** (§6):

  * UTF-8, no BOM.

  * ASCII-sorted keys in all objects.

  * Compact separators.

  * Exactly **one** trailing LF.

  * Arrays that conceptually represent sets (for example, if any set-valued sampler fields are added later) MUST be deduplicated and ASCII-sorted.

* Two-run identity:

  * For fixed inputs (`viewer`, `candidates-file` contents, `seed`), environment pins, and `APP_ENV`, two successive runs of `hdctl dev:sampler` **MUST** produce byte-identical stdout, including the trailing LF.

* Seed-only impact:

  * For fixed viewer and candidate inputs, changing `--seed` **MUST** affect only the `seed` field in the output JSON. The `candidates` array (including ordering, scores, weights, bands, diversity flags, and `is_recent`) **MUST** remain byte-identical across runs with different seeds.

* Streams:

  * On success, `stdout` carries only the sampler JSON payload; `stderr` is empty.

  * On usage errors (e.g., missing `--viewer` or `--candidates-file`), exit code is 64 and a short synopsis appears on `stderr`; `stdout` remains empty.

  * On typed errors (validation failures), exit code is 2 and a typed error JSON object appears on `stderr` per §5.2; `stdout` remains empty.

    ### **4.10.5 Relationship to other surfaces (informative)**

* `hdctl dev:sampler` is **orthogonal** to:

  * `hdctl showcompat` (compat harness and Reader parity),

  * `hdctl bg:resolve` (BodyGraph resolver and vendor ingest),

  * `hdctl bg:export-json` (stateless BodyGraph export), and

  * `hdctl admin-bundle` (full product admin bundle).

* It does **not**:

  * call Reader or Aux endpoints,

  * write governed evidence artifacts directly, or

  * alter the public Reader or Aux contracts.

* QA coverage (CLI harness):

  * CLI tests for `dev:sampler` are expected to prove:

    * two-run identity for a fixed seed,

    * seed-only impact (seed changes, candidates unchanged), and

    * help output clearly marking the command as “DEV/ADMIN ONLY”.

* Relationship to the HTTP dev sampler harness (§5.11):

  * For sampler behavior and determinism, `hdctl dev:sampler` is the **primary** sampler QA harness:

    * it runs entirely under closed rails, without HTTP or vendor dependencies,

    * it is the first place sampler/core determinism and seed-only semantics must be proven.

  * The dev sampler HTTP harness (`POST /internal/dev/sampler` in §5.11) is a **secondary**, infra-dependent harness:

    * it wraps the same sampler core for internal HTTP use,

    * it is used to layer HTTP-level determinism and seed-only checks on top of the CLI proofs when a Reader dev environment is available,

    * it remains dev/admin-only and is explicitly excluded from the Endpoint Catalog and A7 proof surface.

  * QA plans should treat CLI sampler proofs as required foundation, and HTTP sampler proofs as additional coverage when infra allows; behavior discrepancies between the two must be treated as defects.

    

---

# 5\. Reader Transport (public bytes) Required‑NowRequired‑NowRequired‑Now

## 5.1 Success envelope Required‑NowRequired‑NowRequired‑Now

**Body shape (six keys).**  
 The Reader v1 success body contains exactly these six top‑level keys — no extras:

* `reader_version` — fixed string `"v1"`.

* `eligible` — boolean.

* `categories` — array of items exactly `{ "id", "band" }`.

* `meta` — object exactly `{ "engine_tag", "invocation_tag" }`.

* `release_id` — lowercase 64‑hex string.

* `idempotence_hash` — lowercase 64‑hex string.

### 5.1.1 CLI and admin compatibility surfaces (normative)

* The Reader v1 success envelope above is the **only** public compat payload exposed by the Reader API. It remains six‑key and numeric‑free.

* The compat engine also produces a richer **compat JSON** structure (scores, bands, narrative keys, and per‑category metadata) used for admin/test workflows. This richer JSON is **not** the Reader v1 envelope.

**hdctl showcompat (CLI admin harness).**

In v1, `hdctl showcompat` behaves as follows (normative; see §4.1 for full details):

* Resolves the pair inputs and viewer preferences (via DB/vendor/file/STDIN as specified in §4.1).

* Computes full compat JSON, including:

  * per‑category `band` and numeric scores, and

  * narrative selection keys per category (for Aux/Narratives).

Emits that compat JSON to **stdout** as a single LF‑terminated canonical JSON document of the form:

 `{`

  `"a": {…},`

  `"b": {…},`

  `"viewer_prefs": {…},`

  `"compat": {`

    `"categories": [ … ],`

    `"meta": { … }`

  `}`

`}`

*  The exact schema (fields and enums) is owned by this document’s later compat sections and **HDE‑Mechanics Guide** (titles‑only). Compat JSON is an **admin/test surface only**; it is not a public Reader payload.

* When `--dump-reader <path>` is provided, `showcompat` also writes the Reader v1 success envelope bytes to `<path>` via the same `emit_reader_public_envelope` path as the Reader API. These bytes must obey the six‑key covenant above and the canonical JSON rules in §6.1.

### 5.1.2 Reader v1 envelope bytes (normative)

When the Reader v1 envelope is produced (either by the Reader API on a Catalog JSON success route, or by the CLI via its reader‑dump path), its bytes **MUST**:

* Match the six‑key shape defined at the top of this section, with no additional fields.

* Be canonical JSON per §6.1:

  * UTF‑8 (no BOM),

  * ASCII‑sorted keys,

  * compact separators,

  * exactly **one trailing LF**.

* Satisfy the categories policy:

  * Each item in `categories` is exactly `{ "id", "band" }`.

  * `band ∈ {"Cool","Open","Warm","Glow"}`.

  * `id` comes from the Magic‑10 closed set (HDE‑Schemas & Artifacts §2.6; HDE‑Math‑Spec §5.1).

  * In v1 Alpha:

    * if `eligible == true`: emit exactly one item `{"id": "harmony", "band": …}`;

    * if `eligible == false`: `categories` MAY be `[]`.

* Be byte‑identical across Reader and CLI for the same underlying compat result and environment (when CLI produces the envelope via `--dump-reader`).

Richer compat JSON (including numeric scores and narrative selection keys) is restricted to **admin/test artifacts** (for example, `hdctl showcompat` compat JSON on stdout, admin sidecars, and Aux preview inputs). These admin surfaces **must not** extend or change the Reader v1 public envelope; the six‑key envelope remains numeric‑free and field‑closed.

### 5.1.3 Emission algorithm (success case; titles‑only)

The emission algorithm for the Reader v1 envelope is unchanged and remains:

1. **Build preimage** as defined in HDE‑Math‑Spec §3 (fields owned there; do not restate here). The preimage excludes `idempotence_hash`.

2. **Canonicalize & hash.**

   * Serialize the preimage with the single shared emitter and canonical JSON rules (§6.1) to obtain `preimage_bytes`.

   * Compute `idempotence_hash = sha256(preimage_bytes)` (lowercase 64‑hex).

3. **Finalize.**

   * Add `idempotence_hash` to the envelope.

   * Re‑serialize with the same emitter to produce the final success body bytes (LF‑terminated).

All byte checks run under `LC_ALL=C` (and `TZ=UTC` where relevant), as described in PF01/PF12 (titles‑only).

### 5.1.4 Public covenant and determinism

**Public covenant.**

* The Reader v1 success body is **numeric‑free**.

* Fields such as `score`, `prompt`, `uncertainty`, or any narrative keys/diagnostics **MUST NOT** appear in the Reader v1 envelope.

* Numeric scores and narrative keys exist only in compat/admin JSON (e.g., `showcompat` stdout compat JSON and Aux preview inputs), never in the public Reader response.

**Determinism and parity.**

* **AB vs BA.** Normalization at the compat layer guarantees identical preimages and identical final Reader v1 envelope bytes for `{a,b}` and `{b,a}`.

* **Two‑run identity.** Two serializations with the same inputs produce byte‑identical Reader envelope bytes.

* **Reader vs CLI.**

  * When the CLI produces Reader v1 bytes via `--dump-reader`, those bytes **MUST** be identical to the Reader 200 success body for the same inputs and environment.

  * CLI compat JSON (admin/test) is canonical and deterministic, but it is a **distinct envelope** from the Reader v1 public envelope.

**Routing (titles‑only).**

* Canonical JSON & pack/manifest rules: **HDE‑Schemas & Artifacts**.

* Magic‑10 IDs, scoring, and band selection: **HDE‑Math‑Spec** and **HDE‑Mechanics Guide**.

* Transport status & headers (A7 matrices): **HDE‑Governance** §10 and this document’s §5.3.

* Preimage/idempotence details: **HDE‑Math‑Spec** §3.

* CLI compat JSON schema and admin/test evidence surfaces: this document (later CLI/compat sections) and **HDE‑Mechanics Guide** (titles‑only).

### **5.1.5 EPIC017 CLI reader-dump QA status (informative)**

EPIC017 Live QA captured a Reader v1 envelope produced by:

`hdctl showcompat --source vendor --dump-reader <path>`

for a synthetic birth pair in the CLI/Codespaces environment. The captured JSON:

* has exactly the six canonical top-level keys (`reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`), with no extras;

* is numeric-free and satisfies the v1 `categories` policy (`categories` either `[]` or a single `{ "id": "harmony", "band": … }` when `eligible == true`);

* uses `meta.engine_tag` / `meta.invocation_tag` values from the CLI/dev context (for example `hdengine-dev`, `INV-LOCAL`) and a lowercase 64-hex `release_id` (all zeros in this QA run), consistent with the pattern requirements in this section; and

* passes the canonical JSON gates in §6.1 (UTF-8, sorted keys, compact, exactly one LF).

This evidence confirms that the CLI `--dump-reader` path can produce a valid Reader v1 envelope in the Codespaces QA environment using a **CLI-local identity**. The authoritative production engine identity remains the `/internal/version` ops endpoint and the Reader v1 envelope on Railway, governed by **HDE-Governance** and **HDE-Mechanics Guide** (titles-only); compat and CLI meta fields are local/admin identity contexts and must not be treated as proof of a remote prod engine’s identity.

AB↔BA identity, two-run identity, and Reader↔CLI parity for Reader v1 envelope bytes remain required by this spec and are exercised via dedicated harnesses and evidence families (see §3.6, §5.1.2, and Appendix D). This QA step validates a single well-formed envelope instance in the CLI QA environment; it does not, by itself, satisfy the broader parity and determinism acceptance tokens.

---

## **5.2 Errors \[Required-Now\]**

* **Typed, numeric-free.** Error body is a typed JSON object, serialized by the same canonical emitter (§6.1/§6.2) and LF-terminated. **Shape:**  
   `{"ok": false, "code": "<string>", "error": "<string>"}`.  
   *(Optional)* `retry_after_ms` (**int ≥ 0**) appears **only** for deterministic **429** mappings; otherwise **omit**. No PII, no payload echoes, no SR/XR numerics.

* **Headers (normative).**  
   `Content-Type: application/json; charset=utf-8` · `Cache-Control: no-store` · **no `ETag`**. A7 conditional rules live in §5.3.

* **Streams.** Errors travel on **stderr** in the CLI; Reader uses **HTTP status** with the headers above. Public bytes are canonical JSON: UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; checks run under `LC_ALL=C`, `TZ=UTC`.

* **Determinism & parity.** Given the same inputs/environment, error bodies are **byte-identical**; **AB vs BA** has no effect. **CLI stderr** and **Reader body** are byte-equal for the same error condition.

* **Refusal vs 429 (policy note).** **Refusal** (rails closed) is an **ops surface**, **not** an A7 proof surface. Transport invariants on refusal: `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, **no `ETag`**, **no `Vary`**, **no `Content-Encoding`**. **429** is an **A7 transport outcome** and **may** include `retry_after_ms`. Keys-only log allow-lists and token names are owned in **HDE-Governance** (titles only).  
* **DB availability (non‑dev).** If no database connection can be established (and no dev fallback applies), respond with a **typed, deterministic JSON error** (numeric‑free envelope; headers per §5.2). CLI exit code is **2**. No raw driver exceptions or stack traces surface.

### **Validation (binary)**

1. **Schema gate:** object contains `ok:false`, `code`, `error` (strings); optional `retry_after_ms` is integer ≥ 0 (**429 only**); **no other keys**.  
2. **Canonicalization:** re-serialize canonically and **byte-compare** (must match); one LF; UTF-8; no BOM/ANSI.  
3. **Parity:** CLI **stderr** vs Reader **error body** byte-compare (must match).  
4. **A7 checks:** `Content-Type` present; `Cache-Control: no-store` present; **no `ETag`**.

**Routing (titles-only).** A7 policy and acceptance tokens live in **HDE-Governance** (§2.0 and A7). Canonical JSON rules live in **HDE-Schemas & Artifacts** (§4).

---

## **5.3 Conditional delivery (A7) \[Required-Now\]**

These transport bytes are owned here; PF05 owns **Reader bytes only** and keeps matrices in lockstep with HDE-Governance (writers live in Governance; titles only). Bodies use the canonical serializer (§6.1). **A7 proofs run only on a PF05 Endpoint Catalog (JSON success) route** (titles only). Internal-ops `/internal/version` is excluded.

* **ETag identity & conditional sequence.** On 200 success, emit a **strong, quoted ETag** over the **LF-terminated canonical body** (pre-compression). A **304 Not Modified** may be returned **only after** a prior 200-with-body for the same identity. **HEAD** mirrors 200 validators and never has a body.  
* **304 entity headers (tightened).** **Omit both** `Content-Type` **and** `Content-Length` on 304\. Body is empty.  
* **POST is non-conditional.** POST never carries validators and never returns 304\.  
* **Cache semantics.** **200 and HEAD:** `Cache-Control: private, max-age=0, must-revalidate`. **Writers and errors:** `Cache-Control: no-store`.  
* **Content-Type on 200\.** `Content-Type: application/json; charset=utf-8`.  
* **Vary (required).** `Vary: Authorization, Accept-Encoding` is required (additional members allowed).  
* **Error and writer ETags.** Do **not** emit `ETag` on writers or errors (error `Content-Type` lives in §5.2).  
* **Encoding invariance.** For the same canonical body, the identity `ETag` and the **HEAD identity length** (length of the LF-terminated body pre-compression) are unchanged across accepted `Accept-Encoding` selections (identity, gzip, br).  
* **HEAD parity.** For the same resource, HEAD returns status 200 with **no body**. `Content-Length` equals the identity 200 body length (LF-terminated, pre-compression). `Content-Type` on HEAD equals GET.

### **Validation (binary)**

1. **200:** strong, quoted `ETag` present; `Cache-Control: private, max-age=0, must-revalidate`; `Content-Type: application/json; charset=utf-8`; `Vary: Authorization, Accept-Encoding`.  
2. **304:** only after prior 200; no body; validators mirror 200 **except** `Content-Type` and `Content-Length`, which are omitted.  
3. **HEAD:** status 200; validators mirror 200; **no body**; `Content-Length == len(identity 200 body)`; `Cache-Control: private, max-age=0, must-revalidate`; `Content-Type == GET`.  
4. **Writers/errors:** `Cache-Control: no-store`; **no `ETag`**.  
5. **POST:** treated as non-conditional (ignore `If-*` conditionals).  
6. **Encoding invariance:** for the same canonical body, `ETag` and **HEAD identity length** are stable across accepted encodings.

### **Evidence hooks (titles-only)**

* Endpoint Catalog snapshot (titles only).  
* Headers-only **env-gate proof** (demonstrate non-prod entries are unreachable in prod).  
* A7 header snapshots (GET / HEAD / 304).  
* **Composite A7 proof JSON** (schema and validation live in PF12).

**Routing (titles-only).** Governance tokens for these checks live in **HDE-Governance §2.0 Acceptance Tokens**. Proofs run on a PF05 Endpoint Catalog (JSON success) route and are indexed in **PF12** (human Evidence Index \+ hash sentinel \+ machine mirror, same-PR rule).

---

## **5.4 Dev harness routing and guard (dev-only) \[Implemented\]**

**Purpose.** Dev-only Reader surface for acceptance evidence. Internal validation aid; not a public contract. Bytes and headers here exist solely to produce evidence (schema and LF checks, AB↔BA parity, two-run identity, Reader↔CLI parity). **Harness proofs do not replace** the §5.6 Endpoint Catalog (JSON success) requirement for A7; they are **supplemental**.

### **Route and gate (must)**

* **Route.** `GET|POST /api/reader?v=1` is the harness endpoint.  
* **Gate.** The route **must** be gated by `APP_ENV=dev` and bound only to a local interface (for example, `127.0.0.1`). It **must not** be mounted in production builds or non-dev deploys.  
* **Rails closed.** Harness runs with rails closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); it never opens vendor rails.

### **Emitter and parity (must)**

* **Single emitter.** All harness success and error bodies are emitted by the **same shared presenter/emitter** as Reader and CLI (§6.2).  
* **Reader↔CLI parity.** For identical inputs and environment, harness responses are **byte-identical** to `hdctl showcompat` stdout (six keys, LF).  
* **Determinism.** **AB↔BA** parity and **two-run identity** must hold at the byte level.

### **Serialization (canonical)**

* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF. Arrays used as sets are deduped & ASCII-sorted (§6.1). All comparisons run with `LC_ALL=C`, `TZ=UTC`.  
* **No ANSI or prompts.** No color codes, prompts, extra lines, or trailing spaces in bodies.

### **Headers (A7 posture applied to harness)**

* **Success (200).** `Content-Type: application/json; charset=utf-8`, **strong quoted ETag** over the LF-terminated body, `Cache-Control: private, max-age=0, must-revalidate`, and `Vary: Authorization, Accept-Encoding`.  
* **Errors.** `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, **no `ETag`**; body is LF-terminated canonical JSON.

### **Conditionals (dev stability)**

* **POST.** Non-conditional. No validators and never returns `304`.  
* **GET.** May implement the A7 conditional flow (§5.3 and Appendix A) **for local evidence**:  
  * **304:** only after a prior `200` with matching ETag; **no body**; **omit `Content-Type` and `Content-Length`**.  
  * **HEAD (optional evidence):** status `200`; **no body**; validators mirror `200`; **`Content-Length == len(identity 200 body)`**; `Content-Type == GET`.  
  * **Encoding invariance (optional evidence):** for the same canonical body, **ETag** and **HEAD identity length** are stable across accepted `Accept-Encoding` selections. These harness captures **supplement**—do **not** replace—the A7 proofs that must run on an Endpoint Catalog (JSON success) route.

### **Hygiene and logs (dev)**

* **No mixed streams.** Never interleave diagnostics with public bytes; keep logs and diagnostics out of payloads.  
* **No secrets or PII.** Logs contain no secrets or payloads; redact any secret mentions (keys-only logs posture lives in HDE-Governance; do not inline keys).

### **Evidence (records-only; titles-only; indexed via PF12)**

* `parity/harness_vs_cli` — harness `GET` or `POST` vs CLI stdout byte-compare (**expected empty diff**).  
* `determinism/abba`, `determinism/two_run` — AB/BA and two-run fixtures for harness outputs.  
* `transport/headers` — header snapshots for `200`, `HEAD`, `304` if implemented (captures normalized per **HDE-Schemas & Artifacts**).  
   **Indexing discipline:** update **PF12** human `docs/evidence/INDEX.json`, **hash sentinel** `docs/evidence/INDEX.sha256`, and machine `artifacts/evidence_index.jsonl` **in the same PR**. Each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor` (transcript anchor \+ on-disk stat).

**Routing (titles-only).** A7 transport rules: **HDE-Governance** §10 and this document §5.3 / Appendix A. Canonical JSON and capture normalization: **HDE-Schemas & Artifacts** §4. Token names live in **HDE-Governance** §2.0.

---

## **5.5 Compat v1 (dev-only) route & parity harness \[Implemented (dev-only)\]**

**Purpose (informative).** Provide a development-only endpoint for exercising the Compatibility Engine and producing acceptance evidence. This route exists solely for operator/testing workflows; it is **not** a public Reader contract and **may contain numerics** (internal surface). **A7 proofs do not run here**; the proof surface is the **Catalog JSON success route** (see §5.6).

### **Route**

* **Path.** `POST /api/compat/v1` (dev only).

* **Method posture.**

  * **POST** is normative and **MUST** be used for JSON bodies.  
  * **POST is non-conditional** (no validators; never returns `304`).  
  * An optional `GET /api/compat/v1` **MAY** exist for health/probing in the dev harness; if present, `GET` **MUST NOT** carry a request body. If this `GET` implements A7 behavior for local evidence, it **MUST** conform to §5.3 / Appendix A (A.1–A.6).

### **Payload shape & validators (titles-only)**

* **Request body (POST).** As defined in Mechanics → §7A “Compatibility Engine (pair) — contract” (titles-only):

  * `a`, `b` each either an `*_id` **or** a full person payload (**do not mix** id \+ payload for the same party; mixing ⇒ `invalid_json`).  
  * `viewer_prefs` with `top_category` and `weights` covering all 10 Magic-10 IDs as ints `0..100` (missing/non-integer ⇒ `invalid_prefs`).  
* **Success body (dev/internal).** Returns the §7A pair contract (`10 × {id, score:int 0..100, band ∈ {Cool,Open,Warm,Glow}, personal_key, shared_key}`) plus `meta.{engine_tag, release_id}`. This is an internal/admin testing surface — **not** the public Reader v1 payload.

* **Error body.** Typed, numeric-free `{"ok": false, "code": "…", "error": "…"}`; never echo request/vendor payload text; **no PII** (e.g., `invalid_json`, `invalid_prefs`, `missing_narrative_key`).

### **Headers & conditionals (normative)**

* **Success (200).** `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`. **POST is non-conditional**; do not return `304` for POST. **ETag optional** on this dev-only route in alpha; if emitted, it **MUST** cover the final LF-terminated body bytes.  
* **Errors.** `Content-Type: application/json; charset=utf-8`; `Cache-Control: no-store`; **no `ETag`**.  
* **HEAD/304 (optional GET only).** Not required for this dev-only route. If an optional `GET` is exposed and implements A7 for local evidence, it **MUST**: return `304` only after `200` with matching ETag; have **no body**; **omit `Content-Type` and `Content-Length`**; and honor **HEAD 200 parity** and validators as per A.1–A.4.

### **Serialization & determinism (dev)**

* **Single emitter.** Responses **MUST** be emitted by the same presenter/emitter the CLI uses (§6.2).  
* **Canonical JSON.** UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF; arrays-as-sets deduped & ASCII-sorted (§6.1).  
* **Determinism.** For a fixed request, **two runs** produce byte-identical LF-terminated bytes; **AB↔BA parity** holds when swapping `a/b`. Tests run under `LC_ALL=C`.

### **Parity (clarified)**

* **Public parity lives in §5.4** (`/api/reader?v=1` ↔ `hdctl showcompat` stdout).  
* **Compat v1 parity (optional/when enabled).** If a dev-only CLI admin sidecar or file-backed internal output is enabled, its bytes **MUST** match `POST /api/compat/v1` for identical inputs. (Admin sidecar is disabled by default; enabling it requires a Doc-Delta and refreshed evidence.)

### **Evidence (records-only; titles-only; indexed via PF12)**

* **CLI parity (public):** `artifacts/cli/parity/reader_cli_parity.bytes`, `artifacts/cli/parity/abba_identity.bytes`, `artifacts/cli/parity/tworun_identity.sha256`.  
* **Harness headers:** `artifacts/cli/transport/post_nonconditional_proof.log`, `artifacts/cli/transport/no_secrets_error_headers.log`.  
* **Serializer guards:** `artifacts/cli/guards/serializer_grep_guard.log`, `artifacts/cli/guards/emitter_symbol.txt`.  
* **(If sidecar enabled)** internal-contract parity bytes for compat v1 (file path per Doc-Delta).  
   **Indexing discipline:** update **PF12** human `docs/evidence/INDEX.json`, **hash sentinel**, and machine `artifacts/evidence_index.jsonl` **in the same PR**.

**Routing (titles-only).** §7A contract lives in **HDE-Mechanics Guide**. A7 transport policy lives in **HDE-Governance** (A7) and §5.3 / Appendix A here. Canonical JSON rules: **HDE-Schemas & Artifacts** §4. Tokens: **HDE-Governance** §2.0.

---

**5.6 Endpoint Catalog (JSON success)**

**Purpose.** Name the Reader JSON success routes that are eligible for A7 proofs. The catalog is titles-only; bytes and examples live elsewhere. The Catalog is **internal-only** and is not a client contract.

### **Scope and rules**

* **Single home.** This subsection is the only place that lists success endpoints eligible for A7 proofs.  
* **Internal-only.** FE or third-party clients must not couple to the Catalog.  
* **Env-gated.** Each entry declares an environment gate (`dev`, `staging`, `prod`). Entries not gated for `prod` must be unreachable in production.  
* **Titles-only.** List by route title; do not include URLs, payload bytes, or example bodies.  
* **Exclusions.** `/internal/version` is operator-only and excluded from A7 proofs.  
* **Empty allowed.** The catalog may be empty until a qualifying success route ships. In that case, catalog presence can pass while A7 proofing remains unmet.  
* **Maintenance.** When the catalog changes, update Appendix D: Evidence Index and the machine mirror in the same change (titles only).

### **Catalog (titles only)**

* (no entries yet)

### **Evidence artifacts (titles-only)**

* `artifacts/reader/endpoints_snapshot.json` — Endpoint-Catalog snapshot (records-only; route titles and envelope keys; single trailing LF).  
* `artifacts/proofs/endpoints_env_gate_proof.log` — Env-gating proof (headers-only; shows non-prod entries are unreachable in `prod`; single trailing LF).  
* *(Optional, informative)* `docs/ENDPOINTS_CATALOG.json` — Non-canonical helper list by title only; keep synchronized with Appendix D and the machine mirror.

### **Acceptance (binary)**

* **ENDPOINTS\_CATALOG\_INTERNAL\_OK.** Catalog posture is internal-only; not a client contract.  
* **ENDPOINTS\_CATALOG\_ENV\_GATE\_OK.** Each entry declares an env gate and non-prod entries are unreachable in `prod`.  
* **ENDPOINTS\_CATALOG\_OK.** Catalog subsection exists, is current, and lists success routes by title only. An empty list is permitted until a route ships.  
* **A7\_TRANSPORT\_PROOF\_OK.** At least one cataloged success route has a complete A7 proof set (see §5.3 and Appendix A). This remains unmet until a cataloged route is proven.

### **Routing (titles only)**

* Governance token names live in **HDE-Governance §2.0**.  
* Transport validators live in **§5.3** and **Appendix A** of this document.  
* Evidence artifacts and snapshots are listed in **Appendix D: Evidence Index**.

Here’s the updated section, aligned with the prior edits to §§0.2, 5.2, and 5.3 and the plan item to keep the catalog gated and status-noted until EPIC-012 ships.

## **5.6 Endpoint Catalog (JSON success) \[Required-Now\]**

**Purpose and scope.** Define the set of **JSON success** routes on which **A7 proofs must run**. PF05 owns **Reader bytes only**; writers/errors posture is governed in **HDE-Governance** (titles only). Internal-ops `/internal/version` is **excluded**.

**Status (current).** The Catalog is defined but not yet populated for production. Populate entries as **EPIC-012** ships success routes. Until then, any non-prod entries remain **env-gated** and **unreachable in production**.

**Catalog ownership.**

* The Catalog is **internal-only** and **env-gated per entry** (titles-only; path-agnostic).  
* The Catalog file **bytes** are defined in **Appendix B** (this spec).  
* Schemas and records-only artifacts (snapshot, Catalog file, proof captures) live in **HDE-Schemas & Artifacts** (PF12). PF05 specifies the **transport bytes and proof rules**.

**Transport invariants (apply to every cataloged route).**

* **GET 200:** strong, **quoted `ETag`** over the **LF-terminated canonical body** (pre-compression); `Content-Type: application/json; charset=utf-8`; `Cache-Control: private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding`.  
* **HEAD 200:** **no body**; validators mirror GET; `Content-Length == len(identity 200 body)` (LF-terminated, pre-compression); `Content-Type == GET`.  
* **304 Not Modified:** allowed **only after** a prior 200 for the same identity; **no body**; **omit both** `Content-Type` and `Content-Length`; validators mirror cached GET.  
* **No `ETag` on writers/errors.** Writers and error responses use `Cache-Control: no-store` and **omit `ETag`** (see §5.2 and §5.3).  
* **Encoding invariance:** for the same canonical body, `ETag` and **HEAD identity length** are stable across accepted encodings.

**Population and change policy.**

* Add or modify Catalog entries **by title only**; do **not** embed literal URLs.  
* When the Catalog changes, follow PF12’s **same-PR indexing discipline** (update the human index and hash sentinel and the machine mirror in the same PR) and record the Doc-Delta in the local **Change Log** (§0.4). Titles-only; PF12 is the **single home** for evidence/indexing.  
* Each non-prod entry **must** include an **env gate**; entries not gated for prod must be proven **unreachable** in production (headers-only env-gate proof).

**Evidence (titles-only pointers).**

* **Snapshot & Catalog file:** governed in PF12 (records-only artifacts; titles-only listing; `proof_anchor` path-proofs present).  
* **Env-gate proof and A7 proof artifacts:** governed in PF12; **A7 proofs run only on cataloged JSON success routes** (headers-only/env-gate; composite success proof JSON that validates against PF12’s composite proof schema — see §8.12). PF05 references these by title only.

### **Validation (binary)**

1. **Catalog posture:** snapshot present and env-gated; production excludes entries not explicitly opened.  
2. **GET 200 invariants:** strong quoted `ETag`; `Content-Type` and `Cache-Control` as specified; required `Vary`.  
3. **304 after 200:** returned only after a prior body-ful 200 for the same identity; **no body**; `Content-Type` and `Content-Length` **omitted**.  
4. **HEAD parity:** status 200; **no body**; validators mirror GET; `Content-Length == len(identity 200 body)`; `Content-Type == GET`.  
5. **Writers/errors posture:** `Cache-Control: no-store`; **no `ETag`**.  
6. **Encoding invariance:** for the same canonical body, `ETag` and **HEAD identity length** are unchanged across accepted encodings.

**Routing (titles-only).** Transport governance and acceptance tokens live in **HDE-Governance (§2.0)**. Snapshot/mirror schemas live in **HDE-Schemas & Artifacts**. Proof files and admin artifacts are indexed in **PF12**. **EPIC-012** owns delivery of concrete success routes that will populate this Catalog.

---

## **5.7 Aux Narrative (public bytes)**

**Route (canonical \+ alias; byte-identity required).**

* Canonical: `GET /api/aux/narrative?v=1`  
* Alias: `/aux/narrative?v=1`  
* **Alias parity (merge-blocking):** Canonical and alias **MUST** produce byte-identical status/headers/body for the same query tuple. **Acceptance:** `AUX_CANON_ALIAS_PARITY_OK`. (Policy/tokens: HDE-Governance.)  
  ---

**Query parameters (names-only; public).**

* `category` — Magic-10 id (closed set).  
* `band` — one of `{Cool, Open, Warm, Glow}`.  
* `perspective` — one of `{shared, a_to_b, b_to_a}`.  
* **Not public:** `slot` is **not** exposed on the public route (pack-internal only; QA override permitted).  
  ---

**Outcomes (deterministic).**

1. **Text** — `200 text/plain; charset=utf-8`

   * Body: LF-terminated **text** (no `\r`, no ANSI).  
   * Validators: **strong quoted `ETag`** over the LF-terminated identity body (pre-compression).  
   * `Vary: Authorization, Accept-Encoding` (**required**).  
2. **Suppressed** — `200` with **empty body**

   * **No `ETag`**.  
   * `Vary: Authorization, Accept-Encoding` (**required**).  
   * Optional generic policy echo: `X-Narrative-Policy: suppressed`.

   ---

**Provenance echoes (both outcomes; names-only).**

* `X-Narrative-Pack-Sha`  
* `X-Narrative-Composition`

These header values **MUST** be stable across two identical runs. **Acceptance:** `COMPOSE_IDS_DETERMINISM_OK`. (Schema/pack identity lives in HDE-Schemas & Artifacts; tokens in HDE-Governance.)

---

**A7 scope linkage (reminder).**

* A7 proofs (GET/HEAD/304, ETag/Vary/304 invariants) run **only** on a **§5.6 Endpoint Catalog (JSON success)** route.  
* Aux **HEAD/304 are out of scope** for EPIC-010. (Policy: HDE-Governance.)  
  ---

**Snapshot normalization (routing).**

* Stored header snapshots use **lower-case header names**; values verbatim.  
* Normalization is governed in HDE-Schemas & Artifacts; **acceptance:** `SNAPSHOT_HEADER_LOWERCASE_OK`.  
  ---

**Evidence (titles/paths only; PF12 single home).**

* Headers-only snapshots (exactly two):  
  * `tests/transport/headers/aux_text_200.snap`  
  * `tests/transport/headers/aux_suppression_200.snap`

Update the **human index**, its **hash sentinel**, and the **machine mirror** in the **same PR**. (PF12 governs mirror/index.)

---

## **5.8 SDK interfaces (PF14 pointer) \[Required-Now\]**

**Purpose.** Bind SDK contracts to the Reader transport so client libraries cannot drift. PF05 owns the **bytes**; SDK specifics (types/tests/examples) live elsewhere.

**Requirements (titles-only)**

* **Reader parity.** SDKs (TypeScript / Python) **MUST byte-match** the Reader v1 six-key public envelope using the **single presenter/emitter** (§6.2) and **canonical JSON** (§6.1: UTF-8, sorted keys, compact, exactly one LF; arrays-as-sets deduped & ASCII-sorted).  
* **Conditional-GET helper.** Provide a helper that **conforms to §5.3 A7 invariants** on cataloged success routes: strong quoted ETag on 200, HEAD parity (no body; identity length), 304 only after prior 200 **omitting both** `Content-Type` and `Content-Length`, required `Vary: Authorization, Accept-Encoding`, and **encoding-invariance** of identity ETag and effective length.  
* **Errors.** Surface **typed, numeric-free** errors that follow §5.2 (no `ETag`, `no-store`, `Content-Type: application/json; charset=utf-8`); **no public numerics**.  
* **No ad-hoc serializers.** SDKs must **not** implement alternate emitters; all public JSON comes from the shared presenter/emitter (§6.2).

**Validation (binary)**

1. **Byte equality:** SDK output **\==** Reader body (byte-for-byte, one LF).  
2. **A7 helper:** helper exchanges satisfy §5.3 (200/HEAD/304/Vary/encoding-invariance rules).  
3. **Determinism:** AB↔BA and two-run identity hold for identical inputs/env; outputs are stable under `LC_ALL=C`, `TZ=UTC`.

**Evidence (titles-only; indexed via PF12)**

* Parity and determinism fixtures (SDK↔Reader byte compare, AB↔BA, two-run) and conditional-GET transcripts.  
* **Indexing discipline:** update **PF12** human `docs/evidence/INDEX.json`, **hash sentinel**, and machine `artifacts/evidence_index.jsonl` **in the same PR** (records-only; mirror with `proof_anchor`, ASCII field order, sort-before-write).

**Routing (single homes; titles-only)**

* SDK types, helpers, and tests → **PF14 — SDKs & Admin UI**.  
* Evidence schema & indexing → **PF12 — HDE-Schemas & Artifacts**.  
* Transport/A7 policy & tokens → **PF04 — HDE-Governance**.  
* Preimage/idempotence recipe → **PF01 — HDE-Math-Spec**.

## **5.9 Ops: BodyGraph resolve (non‑public) \[Required-Now\]**

**Route (ops‑only; env‑gated).** `POST /_ops/bodygraph/resolve` with body:  
 `{"user_id":"<uuid>","source":"db|vendor","upsert":true}`

**Posture.** Internal operator surface; **not** a Catalog success route and not public. With **rails closed**, a `source:"vendor"` request returns a **typed refusal** without making any outbound call. Bytes follow the same typed‑error envelope rules as §5.2.

**Routing (titles‑only).** Selection semantics mirror `hdctl bg:resolve` (§4.6). Governance (rails/tokens) and PF14 (adapter mechanics) are single homes.

**Acceptance impact:** None; documents implemented ops path for auditability.

## **5.10 Admin bundle HTTP route (admin-only; non-public) Required-Now**

### **5.10.1 Purpose and posture**

The admin bundle HTTP route is the canonical HTTP surface for returning the full admin bundle JSON for a single match, for use by an Admin GUI and other internal tools.

Purpose:

* Provide a single HTTP route that composes:

  * per-person BodyGraph JSON for both parties

  * full compat JSON for the pair

  * three narrative compositions for the match

  * a meta block with engine identity and bundle provenance

* Allow an Admin GUI to query Railway prod and display the full product payload for a match using the same bundle as the CLI.

Posture:

* Admin-only route. This route is not a public Reader JSON success route and is not part of the A7 proof surface.

* Not cataloged for A7. It must not be listed as a JSON success endpoint in the Endpoint Catalog used for A7 proofs.

* Not numeric-free. The admin bundle may include numeric scores and narrative text; the public numeric-free covenant continues to apply only to the Reader v1 success envelope.

  ### **5.10.2 Route, method, and request body (normative)**

Route and method:

* Method: POST

* Path: an admin path pinned here, for example:

  * POST /admin/bundle

* The exact path string chosen here is the canonical bytes; any aliases must produce byte-identical responses and headers.

Request body:

* JSON request describing the two parties whose match should be bundled:

  * pre-Glow:

    * birth-based payload describing the two parties by birth tuples, sufficient for the engine to resolve BodyGraphs using existing resolvers and adapter policy

  * post user-model (future):

    * request body that can address two parties by canonical user identifiers

This section constrains behavior, not the internal schema of the request beyond requiring that:

* the request body is JSON

* it is emitted and processed as UTF-8 without BOM

* it is validated and rejected with a typed error if required fields are missing or malformed

The exact request shape for birth-based and user-based inputs is owned by the HDE-Mechanics Guide and Schemas and Artifacts. PF05 requires that the admin bundle route accepts a single JSON object describing the two parties and returns the admin bundle for that pair.

### **5.10.3 Response body and headers (normative)**

On success:

* Status: 200

* Headers:

  * Content-Type: application/json; charset=utf-8

  * Cache-Control: private, max-age=0, must-revalidate

  * No ETag requirement for admin bundle responses; this route is not an A7 proof surface

* Body:

  * the admin bundle JSON object defined in the CLI section, with top-level keys:

    * a\_bodygraph

    * b\_bodygraph

    * compat

    * narratives

    * meta

  * emitted as canonical JSON:

    * UTF-8 without BOM

    * keys sorted in ASCII order

    * compact separators

    * exactly one trailing newline character

    * arrays that represent sets deduplicated and ASCII-sorted

On error:

* Status:

  * usage or validation errors, authentication failures, or authorization failures:

    * use the existing error taxonomy (typed error body, numeric-free)

* Headers:

  * Content-Type: application/json; charset=utf-8

  * Cache-Control: no-store

  * No ETag

* Body:

  * typed, numeric-free error object as defined in the error model section

  * must not echo secrets, raw birth data, or full bundle content

This route must never return a body that follows the public Reader v1 six-key envelope shape. It always returns either an admin bundle or a typed error body.

### **5.10.4 Authentication, authorization, and admin-only gating (normative)**

The admin bundle HTTP route must be protected by authentication and authorization:

* Every successful admin bundle response must be the result of an authenticated, authorized admin request.

* Pre-Glow minimal requirement:

  * a secret admin credential must exist and be stored as a secret in Railway or equivalent infrastructure

  * the route must require this credential on every request, for example:

    * using an Authorization header that carries a bearer token, or

    * another explicit header pinned for admin use only

* When the credential is missing, invalid, or expired:

  * the route must return a typed error indicating that admin authorization is required

  * the body must be a typed, numeric-free error object

  * no part of the admin bundle may be returned

Post-Glow:

* the authentication and authorization model for admin surfaces must align with the wider app identity and auth model

* until that is pinned, the requirement that admin bundle routes are not left open in production remains in force

This route is not accessible to end users; only admin operators or admin GUI services with the correct credential may call it.

### **5.10.5 Logging and audit (normative)**

Every successful admin bundle HTTP request must be logged and auditable:

* Logs must capture:

  * timestamp

  * caller identity (for example which admin account or client application invoked the route)

  * a high-level description of inputs:

    * for birth-based requests: that the bundle was generated from two birth tuples

    * for user-based requests when available: identifiers for user A and user B without including raw birth details or other PII beyond what Governance permits

  * a correlation identifier usable across logs

Logs must follow keys-only posture:

* no secrets

* no complete request or response bodies

* no vendor payloads

These logs are operations logs and are governed by Glow QA Guide and HDE-Governance for retention, PII handling, and security.

### **5.10.6 Parity with CLI admin bundle (normative)**

For a given pair of parties and environment:

* The admin bundle HTTP route must produce an admin bundle that is byte-identical to the bundle produced by hdctl admin-bundle, once both are emitted as canonical JSON.

* Differences in where meta fields are populated (for example engine\_tag or invocation\_tag) must be controlled; for the same engine instance and configuration the CLI and HTTP bundles must match, including meta.

Future QA tokens that enforce:

* parity between CLI and HTTP bundle outputs

* structural completeness of the bundle

* enforcement of authentication for admin surfaces

will be owned and named in Governance and QA documents. PF05 requires the underlying parity behavior between the CLI and HTTP admin bundle surfaces.

## **5.11 Dev sampler HTTP harness (dev/admin-only) \[Implemented\]**

### **5.11.1 Purpose and posture**

The dev sampler HTTP harness is a **dev/admin-only** route that wraps the sampler core behind HTTP, mirroring the semantics of `hdctl dev:sampler` while returning a minimal, IDs-only payload for internal QA and debugging.

Purpose:

* Provide an HTTP entrypoint that:

  * accepts a viewer identifier and a set of candidate IDs,

  * calls the same sampler core used by the CLI dev sampler, and

  * returns the ranked candidate IDs plus a seed echo in canonical JSON for deterministic replay.

Posture:

* **Dev/admin-only.** The route is intended for engine developers and admin operators only. It is not a public Reader contract and is not exposed to end users.

* **Not cataloged; not A7.** This route **MUST NOT** appear in the Endpoint Catalog (§5.6) and is not an A7 proof surface. A7 transport proofs continue to run only on cataloged JSON success routes.

* **Writer-style errors.** The route uses the standard typed error envelope and headers from §5.2/§8; gating failures and validation errors are treated as writer-style/ops outcomes (`Cache-Control: no-store`, no `ETag`), not as public Reader errors.

  ### **5.11.2 Route, method, and APP\_ENV gate (normative)**

Route and method:

* Method: `POST`.

* Path: `/internal/dev/sampler`.

* Bound to the existing reader blueprint, but with **dev/admin-only** gating and HTTP posture as defined here.

APP\_ENV gate:

* The handler **MUST** enforce `APP_ENV ∈ {dev, test, local}`:

  * When `APP_ENV` is exactly one of `dev`, `test`, or `local`, the handler may proceed to validate input and call the sampler core.

  * When `APP_ENV` is unset, empty, or set to any other value (including `prod`), the handler **MUST** return a **403 Forbidden** response using the typed error envelope from §5.2 (for example with a `DEV_ADMIN_ONLY` style code), and **MUST NOT** call the sampler core. The body is a numeric-free error object; `Cache-Control: no-store`; no `ETag`.

Rails posture:

* The route runs under closed rails:

  * `SAFE_MODE=1`, `ALLOW_NETWORK=0`.

  * No vendor HTTP calls or other network I/O are performed.

* The harness operates purely on the provided candidate IDs and the in-process sampler core.

  ### **5.11.3 Request body and validation (normative)**

The handler accepts a JSON request body with the following fields:

* `viewer_id` — required; non-empty string.

* `candidate_ids` — required; non-empty array of non-empty strings.

* `seed` — optional; string; if absent, treated as `null`.

Validation rules:

* The handler **MUST** reject any request where:

  * `viewer_id` is missing, not a string, or an empty string; or

  * `candidate_ids` is missing, not an array, empty, or contains any element that is not a non-empty string.

* On validation failure, the handler returns:

  * `422` (or the existing invalid-input status used by writer-style routes),

  * a typed, numeric-free error object as defined in §5.2/§8 (for example with an `INVALID_INPUT` style code), and

  * `Cache-Control: no-store`, no `ETag`, `Content-Type: application/json; charset=utf-8`.

* The request body **MUST** be read and validated using the existing writer JSON helpers; it is processed as UTF-8 without BOM and rejected with a typed error if it is not valid JSON or does not match the expected shape.

  ### **5.11.4 Sampler invocation and response payload (normative)**

On a valid, gated request, the handler:

* Constructs internal sampler inputs from `viewer_id` and `candidate_ids` (details owned by the sampler mechanics; this spec treats them as opaque identifiers).

* Invokes the sampler core (same function used by `hdctl dev:sampler`) to obtain a ranked list of candidate IDs.

Response:

* Status: `200`.

* Headers:

  * `Content-Type: application/json; charset=utf-8`.

  * `Cache-Control: private, max-age=0, must-revalidate`.

  * No `ETag` requirement; this route is not an A7 surface.

* Body: a JSON object with at least:

  * `viewer_id` — the `viewer_id` from the request.

  * `meta` — an object with at least:

    * `seed` — the seed string from the request, or `null` if no seed was provided.

  * `candidate_ids` — an array of candidate IDs (strings) in the ranked order returned by the sampler core.

Serialization:

* The response body **MUST** be emitted via the single canonical emitter (§6):

  * UTF-8 (no BOM).

  * ASCII-sorted keys at each object level.

  * Compact separators.

  * Exactly one trailing newline (`\n`).

* Arrays that conceptually represent sets (notably `candidate_ids`) are not treated as sets; they preserve the sampler’s ranking order and are not resorted.

  ### **5.11.5 Determinism and seed semantics (normative)**

Determinism:

* For a fixed `viewer_id`, `candidate_ids` array, `seed` value (including `null`), environment pins, and `APP_ENV`, two successive `POST /internal/dev/sampler` calls **MUST** produce byte-identical responses (status, headers, and LF-terminated body).

Seed-only differences:

* For fixed `viewer_id` and `candidate_ids`, changing `seed` **MUST** affect only the `meta.seed` field in the response body:

  * The `candidate_ids` array **MUST** remain byte-identical across runs with different seeds.

  * No other fields in the response (including ordering of `candidate_ids`) may change as a function of `seed` in the current implementation.

These semantics mirror the CLI sampler (§4.10): seed is metadata-only at this stage and does not influence eligibility or ordering. Any future change that uses seed for tie-breaking must preserve determinism (same inputs/seed ⇒ same output) and be accompanied by updated acceptance evidence.

### **5.11.6 A7, Catalog, and evidence (informative)**

A7 and Catalog:

* `POST /internal/dev/sampler` is a **dev/admin-only internal harness** and is explicitly excluded from the Endpoint Catalog (§5.6). No A7 proofs run on this route.

* The A7 transport invariants in §5.3 apply only to cataloged JSON success routes; this harness follows the writer/error header posture in §5.2 for errors and the standard success headers above for 200 responses.

Evidence and tests (titles-only):

* Adapter-level tests (for example in the `tests/adapter` tree) are expected to:

  * verify determinism (two-run identity),

  * verify seed-only differences (same `candidate_ids` across seeds),

  * verify APP\_ENV gating for `dev`, `test`, `local` vs `prod`/unset/empty, and

  * verify canonical JSON (UTF-8, sorted keys, compact, one LF).

* Any governed evidence artifacts and test transcripts for this route are indexed in the Evidence Index and machine mirror per PF12 (titles/paths only); PF05 does not duplicate those paths.

  ---

# 6\. Serializer Canon & Single Emitter \[Required-Now\]

## 6.1 Canonical JSON (UTF-8, sorted keys, compact, one LF) \[Implemented\]

* **Encoding & termination.** Emit UTF-8 JSON, BOM/ANSI-free, with **exactly one** trailing LF (`\n`).  
* **Ordering & separators.** Serialize with **sorted keys (ASCII lexicographic)** and **compact separators** (`,` and `:`; no spaces).  
* **Arrays-as-sets.** Any array that functions as a set **MUST** be deduplicated and ASCII-sorted by its identity rule (see **HDE-Schemas & Artifacts §4**).  
* **Locale determinism.** All canonicalization and byte comparisons run under `LC_ALL=C`, `TZ=UTC`.

**No pretty-print; no alternates.** Pretty/indented output and alternate serializers are **not permitted** on public paths. Grep-guards **MUST** block ad-hoc `json.dumps(...)` or any non-presenter emitter.

**Validation (binary)**

* **Canonical compare:** re-serialize with the rules above and byte-compare against the produced bytes (**must match exactly**).  
* **LF/encoding check:** UTF-8 only, no BOM/ANSI, **exactly one LF** at end of file.

**Routing (titles-only).** Canonical JSON rules are owned by **HDE-Schemas & Artifacts (§4)**. Governance tokens for these checks live in **HDE-Governance (§2.0 Acceptance Tokens)**.

## 6.2 Unify entrypoint (single presenter/emitter) \[Required-Now\]

* **One entrypoint for public bytes.** Reader and CLI **MUST** call the **same presenter/emitter** entrypoint to produce the public body (both success and typed errors).  
* **Forbid ad-hoc serialization.** Disallow any direct `json.dumps(`, `jsonify(`, module-local “mini emitters,” templating, or string-built JSON on public paths.  
* **Symbol allow-list (single source).** The only permitted public serializer is the presenter’s **emitter entrypoint**. The exact symbol is pinned in code and CI allow-lists (owned in code/CI; titles-only here). **All other serializer symbols are denied** on public paths.  
* **CI grep-guard (fail fast).** CI **MUST** fail on disallowed patterns in CLI or HTTP handlers, including (not limited to): `json.dumps(`, `jsonify(`, string-built JSON, alternate emitters, or templating renderers that bypass the presenter.  
* **Test parity (symbol-level).** Tests **MUST** assert that CLI and Reader import and call the same emitter symbol (import-graph or reflection proof).  
* **Canonicalization coupling.** The shared emitter **MUST** use the canonical JSON rules in §6.1 (UTF-8 no BOM, sorted keys, compact, exactly one LF; arrays-as-sets deduped & ASCII-sorted). All byte checks run under `LC_ALL=C`, `TZ=UTC`.  
* **Determinism & parity.** A single emitter ensures Reader↔CLI **byte equality**, **AB↔BA parity**, and **two-run identity** for identical inputs and environment.

**Acceptance (titles-only).** `CLI_READER_PARITY_OK`, `SINGLE_EMITTER_PARITY_OK`, `JSON_CANONICAL_CHECK_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `PARITY_AB_BA_OK`.

**Evidence (records-only; titles-only; indexed via PF12)**

* **Serializer grep guard (CLI scope).**  
   `artifacts/cli/guards/serializer_grep_guard.log` — AST-based grep guard over the governed CLI scope (`engine/cli/**`) proving there are **no ad-hoc serializers** on public paths. The guard runs under determinism pins (`LC_ALL="C"`, `LANG="C"`, `TZ="UTC"`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`) and emits a stable PASS/FAIL summary and sorted violation list without timestamps or env-dependent content.

* **Shared emitter symbol proof (CLI handlers).**  
   `artifacts/cli/guards/emitter_symbol_proof.txt` — import-graph/AST proof that governed CLI handlers (at minimum `showcompat` and `bg:resolve`) call only the **allow-listed presenter/emitter symbols** (for example `emitter.emit_public`, `emit_reader_public_envelope`) for public bytes. Optional handlers such as `aux-preview` may be listed with an explicit `<none>` emitter entry when exempt; in that case the proof remains PASS for required handlers and still surfaces the exemption as governed evidence.

* **Parity fixtures (Reader↔CLI, AB↔BA, two-run).**  
   Reader/CLI parity and AB↔BA/two-run identity fixtures for compat and Reader v1 envelopes (for example `artifacts/cli/ab.json`, `artifacts/cli/ba.json`, `artifacts/cli/summary.json`, `artifacts/cli/reader_cli_parity.bytes`, and related harness outputs) remain listed and schema-governed in **HDE-Schemas & Artifacts** (titles-only) and are referenced here only as the parity evidence family for §6.2.

* **Indexing discipline (PF12 single home).**  
   All guard and parity artifacts **MUST**:

  * be listed in the human Evidence Index (`docs/evidence/INDEX.json` with `docs/evidence/INDEX.sha256` sentinel), and

  * have corresponding Machine Mirror records in `artifacts/evidence_index.jsonl`,

* updated in the **same PR** as any change to the artifacts. Each mirror record uses canonical JSONL (UTF-8; ASCII-sorted keys; compact; one LF) with **exactly** the field set and order defined in **HDE-Schemas & Artifacts** and includes a `proof_anchor` pointing to a co-located `*.path_proof.txt` transcript for the artifact’s `discovered_physical_path`, `sha256`, `size_bytes`, and `produced_at_utc`. PF05 does not define mirror schema; it relies on PF12 as the single home for Evidence Index and mirror rules.

## 6.3 Idempotence preimage recipe (Reader/CLI parity) \[Required-Now\]

* **Build preimage (exactly five keys).** Construct an object with **exactly** these keys (no others), with values normalized per this spec:

  * `reader_version`: `"v1"`  
  * `eligible`: `<boolean>`  
  * `categories`: `[ { "id","band" } … ]` — numeric-free and constrained by **§5.1** *(v1: when eligible: exactly one `{ "id":"harmony","band":… }`)*  
  * `meta`: `{ "engine_tag","invocation_tag" }` — non-empty strings; `invocation_tag` uses the **short form** defined in Governance/Invocation (titles-only)  
  * `release_id` — lowercase 64-hex (see **§5.1**)  
* **Canonicalize & hash (one emitter, one recipe).** Serialize the five-key object with the **single presenter/emitter** and **canonical JSON rules** (§6.1: UTF-8 no BOM, sorted keys, compact, exactly one LF; arrays-as-sets deduped & ASCII-sorted; run under `LC_ALL=C`, `TZ=UTC`) to obtain `preimage_bytes`. Compute `idempotence_hash = sha256(preimage_bytes)` as lowercase 64-hex.

* **Finalize.** Add the computed `idempotence_hash` to the object (becoming the **sixth top-level key**) and **re-serialize** with the same emitter to produce the public bytes (LF-terminated).

* **Parity & determinism.** The `preimage_bytes` and final public bytes produced by Reader and CLI **MUST** be **byte-identical** for identical inputs/environment. Preimage and final bytes **MUST** also be identical for **AB vs BA** normalized inputs, and across **two runs** with the same inputs.

**Validation gates (binary)**

1. **Recheck:** Remove `idempotence_hash`, re-serialize the five-key preimage canonically, and verify `sha256(preimage_bytes) == published idempotence_hash` for Reader and CLI.  
2. **Pattern checks:** `idempotence_hash` and `release_id` each match `^[0-9a-f]{64}$`.  
3. **AB↔BA:** Preimage and final bytes for `(A,B)` vs `(B,A)` are **byte-identical**.  
4. **Two-run identity:** Two serializations over the same inputs produce **byte-identical** preimage and final bytes.  
5. **Emitter proof:** Tests/reflection show both surfaces call the **same emitter** entrypoint (see §6.2).

**Evidence (titles/paths only)**

* **Parity harness outputs** for Reader vs CLI and AB vs BA (see **PF12 Appendix C**).  
* **Recompute logs/scripts** for `idempotence_hash`.  
* **Indexing in PF12:** update human `docs/evidence/INDEX.json` \+ hash sentinel and the machine `artifacts/evidence_index.jsonl` in the **same PR** as artifacts.

**Routing (titles-only).** Canonical JSON rules: **HDE-Schemas & Artifacts (§4)**. Governance tokens: **HDE-Governance (§2.0 Acceptance Tokens)**.

---

# **7\) Vendor Ingest (HDAPI) \[Required-Now\]**

## **7.1 Rails & Environment \[Required-Now\]**

### **7.1.1 Rails defaults (env inventory; titles-only)**

* **Dev / stage:** rails **OPEN** by default

  * `SAFE_MODE = 0`

  * `ALLOW_NETWORK = 1`

* **Prod / CI:** rails **CLOSED** by default

  * `SAFE_MODE = 1`

  * `ALLOW_NETWORK = 0`

* Opening rails is an **explicit job/session decision** (ops/config), not a runtime toggle.

* The authoritative environment inventory lives in **Glow-Infrastructure** (titles-only).

### **7.1.2 Two-gate rule (both required)**

* A live HDAPI call is permitted **only when both**:

  * `SAFE_MODE = 0`, and

  * `ALLOW_NETWORK = 1`.

### **7.1.3 Refusal semantics (closed rails)**

* When either gate is not satisfied, vendor paths **MUST NOT** perform any network I/O (no sockets, DNS, HTTP).

* In this case, return a **typed refusal**:

  * Numeric-free, LF-terminated canonical JSON.

  * No secrets; logs follow **keys-only** posture.

* Proof remains a **single-file capture**:

  * Headers → blank line → LF-terminated JSON body.

  * Path: `artifacts/proofs/ops_refusal_proof.txt` (see PF12).

### **7.1.4 Environment variables (must be present and non-empty; names-only)**

* `HDAPI_BASE_URL`

* `HD_API_KEY`

* `GEO_API_KEY` (when needed)

Missing or empty env values **MUST** produce a typed failure **without** I/O.

### **7.1.5 Determinism and shaping (closed rails)**

* With rails closed:

  * Providers **may shape** the request (URL, headers, body schema) **deterministically**:

    * Order-neutral.

    * No time/locale/random dependence.

  * Providers **must not send** the request; the output is the typed refusal.

* All checks run under:

  * `LC_ALL = C`

  * `TZ = UTC`.

### **7.1.6 CI / test posture**

* CI runs **CLOSED** by default (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).

* Any CI job that opens rails **must**:

  * Pin timeout/retry/backoff policy.

  * Attach **keys-only** evidence in the same PR.

### **7.1.7 Evidence (titles/paths only; PF12 single home)**

The following artifacts are governed and indexed in **PF12**:

* `artifacts/proofs/ops_refusal_proof.txt` — single-file refusal (headers → blank line → LF-terminated JSON).

* `artifacts/runtime/env_connectivity.snapshot.json` — dev jobs (env and connectivity snapshot).

* Grep-guard reports for keys-only logging.

### **7.1.8 Acceptance (titles-only; tokens live in Governance)**

The behavior above is covered by acceptance tokens owned in **HDE-Governance** (names-only):

* `NO_EXTERNAL_IO_ON_REFUSAL_OK`

* `ERROR_CTYPE_JSON_UTF8_OK`

* `NO_CONTENT_ENCODING_OK`

* `PF04_LOG_ALLOWLIST_009_OK`

* `REFUSAL_ROUTE_PINNED_OK`

* `OPS_REFUSAL_FILE_FORMAT_OK`

* `OPS_REFUSAL_HEADERS_OK`

* `OPS_REFUSAL_BODY_OK`

* `OPS_REFUSAL_MIRROR_LINK_OK`

### **7.1.9 Routing (titles-only)**

* Env inventory: **Glow-Infrastructure**.

* Transport matrices and refusal/error policy: **HDE-Governance**.

* Evidence index and mirror: **HDE-Schemas & Artifacts**.

---

### **7.1.10 Endpoint policy (BodyGraph vendor HTTP)**

**Full BodyGraph endpoint (only):**

The engine uses **only** the full BodyGraph endpoint:

 POST /bodygraphs

 with the three-key JSON body:

 {"birthdate": "...", "birthtime": "...", "location": "..."}

* 

**Unsupported endpoint (simple BodyGraph):**

The optional vendor endpoint:

 POST /bodygraphs/simple

*  is **unsupported** for HDE and **MUST NOT** appear in engine code, QA harnesses, or docs for this engine.

* Any such usage is out-of-policy and must be removed or migrated to `POST /bodygraphs`.

**Privacy / payload constraints:**

* Vendor HTTP **never** receives internal user ids or other internal identifiers.

* Only the birth payload and location are sent, along with the documented header set:

  * `Accept`

  * `Content-Type`

  * `HD-Api-Key`

  * Optional `HD-Geocode-Key`

  * `User-Agent`, etc.

---

### **7.1.11 SAFE rails and admin override (vendor ingest)**

Vendor HTTP for BodyGraph ingest is subject to the SAFE rails posture described in Governance:

* When rails are **closed** (`SAFE_MODE=1` or `ALLOW_NETWORK=0`):

  * **No vendor HTTP calls** are made.

* In **prod**, admin vendor calls are permitted **only** when:

  * Rails are explicitly **open** (`SAFE_MODE=0`, `ALLOW_NETWORK=1`), and

  * The documented **admin override environment guard** is set.

* Otherwise, vendor calls **MUST NOT** be attempted and `bg:resolve` / CLI commands **MUST** fail closed with a typed error.

This section owns the **on-wire HTTP contract** (endpoint, headers, body). Policy, rails, and override semantics are owned by **HDE-Governance** and referenced here by title only.

---

## **7.2 Request Shaping (owned here) \[Implemented\]**

Purpose (normative).  
 Define the exact HDAPI request construction used by CLI and Reader vendor calls: endpoint paths, method, base-URL resolution, canonical headers, content type, request-body schema, and deterministic error mapping from provider responses to typed CLI/Reader errors. Rails and enablement live in §7.1.

### **7.2.1 Endpoints, method, base URL**

* **Primary endpoint:** `POST /bodygraphs` (JSON).

  * This is the **only** vendor BodyGraph endpoint HDE uses. No alternate vendor endpoint is defined here; see §7.1.10 for the explicit statement that `POST /bodygraphs/simple` is unsupported for this engine.

* **Base-URL resolution (no fallback).**

  * Resolve **only** from `HDAPI_BASE_URL`.

  * If `HDAPI_BASE_URL` is missing or empty, fail closed with a typed error (see §7.1); do **not** default to any literal URL.

* **Method rules.**

  * `POST` is normative for JSON BodyGraph requests.

  * `GET` **MUST NOT** carry a request body; if ever used, it is only for dev-harness health probes and not for BodyGraph computation.

### **7.2.2 Canonical headers (dash-case, exact on wire)**

Send these verbatim on wire. Do not add other headers unless explicitly pinned.

* `Accept: application/json`

* `Content-Type: application/json; charset=utf-8`

* `HD-Api-Key: <secret>`

* `HD-Geocode-Key: <secret>`

* `User-Agent: GlowHDEngine/<release_id>` (lowercase 64-hex; contains no secrets)

Capture normalization.  
 Persisted header captures follow the normalization rules in HDE-Schemas & Artifacts (artifact header casing and formatting). On wire, use the exact forms above.

Redaction.  
 API keys are secrets. Never echo values in logs or errors. Keys-only logging posture is owned in HDE-Governance; reference by title only.

### **7.2.3 Request body schema (exact three keys)**

The JSON body must contain exactly these keys (no others), serialized canonically (UTF-8 no BOM, sorted keys, compact, one LF):

`{"birthdate":"DD-MMM-YYYY","birthtime":"HH:MM","location":"City, Country"}`

* `birthdate`: English month abbreviations `Jan..Dec`; day zero-padded `01..31`; year `YYYY`.

* `birthtime`: 24-hour `HH:MM` (`00..23:00..59`).

* `location`: ASCII English `"City, Country"` with a single comma and single space; trim outer whitespace; collapse internal runs to single spaces.

* **No tz.** Do not send timezone. Vendor derives timezone from `location` using `HD-Geocode-Key`.

### **7.2.4 Deterministic construction**

* **Order-neutral.** URL, headers, and body are constructed identically for AB and BA.

* **Locale-neutral.** No locale or formatting beyond the pinned rules. Strings are ASCII/UTF-8 as stated. Jobs run under `LC_ALL=C`, `TZ=UTC`.

* **No floats or wall-clock.** Shaping must not depend on time or non-deterministic sources.

* **Path joining.** Join base URL and endpoint with a single `/`; no duplicate slashes; no query string unless explicitly pinned.

### **7.2.5 Deterministic error mapping (provider → typed errors)**

Map provider HTTP outcomes to typed, numeric-free errors. Never include vendor payloads or secrets in errors or logs.

* `401` → `PROVIDER_UNAUTHORIZED`

* `403` → `PROVIDER_FORBIDDEN`

* `404` → `PROVIDER_NOT_FOUND`

* `429` → `PROVIDER_RATE_LIMITED`

  * If a valid `Retry-After` is present: delta-seconds → integer ms; HTTP-date → integer ms (UTC).

  * On invalid / unsupported / overflow: omit `retry_after_ms`.

* `5xx` → `PROVIDER_UNAVAILABLE`

* Malformed or invalid vendor JSON → `PROVIDER_BAD_RESPONSE` (schema or mapping failure; do not echo vendor body)

Acceptance (vendor mapping).  
 Tests and logs must prove the remap above and that no provider payloads or secrets are logged. Error objects are numeric-free and LF-terminated canonical JSON.

### **7.2.6 Logging and redaction (keys-only)**

* Never log request or response bodies, header values, tokens, or URIs containing keys.

* Keys-only allow-lists live in HDE-Governance. Do not inline key names in this spec. Tests assert conformance to the allow-list by title.

* Redaction examples and fixtures (for example showing a secret value replaced with `REDACTED`) belong in evidence only, not in live logs.

* For persisted captures, apply header capture normalization per HDE-Schemas & Artifacts.

### **7.2.7 Validation (binary)**

1. Method and endpoint. `POST` used for JSON. Any health `GET` (dev harness only) carries no body.

2. Headers. Exact dash-case set above. `Accept` and `Content-Type` as specified. Secrets present on wire but never logged. Captures normalized per HDE-Schemas & Artifacts.

3. Body shape. Exactly three keys. Values match `DD-MMM-YYYY` / `HH:MM` / `"City, Country"` rules. No timezone key present.

4. Determinism. Shaping output is identical for AB vs BA. No locale, time, or random dependence. Checks under `LC_ALL=C`, `TZ=UTC`.

5. Error mapping. Each provider outcome maps to the typed error above. `retry_after_ms` is integer, non-negative, and omitted on invalid formats.

6. Hygiene. All emitted JSON is canonical (UTF-8 no BOM, sorted keys, compact, one LF).

Evidence (records-only; titles-only; indexed via PF12).

* `vendor/shaping_example` — canonical headers, body, and URL (no secrets).

* `rails/closed_refusal` — typed refusal proof (no I/O).

* `rails/open_conformance` — header redaction and policy proof (if rails opened in an integration profile).

Indexing discipline: update PF12 human `docs/evidence/INDEX.json`, hash sentinel, and machine `artifacts/evidence_index.jsonl` in the same change; each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor`.

Routing (titles-only).  
 Rails and enablement: §7.1. Live HTTP policies: §7.3. Canonical JSON and capture normalization: HDE-Schemas & Artifacts §4. Governance tokens and keys-only allow-lists: HDE-Governance §2.0.

---

## **7.3 Live HTTP Call Behavior \[Required-Now\]**

Scope & prerequisites.  
 Rails open (`SAFE_MODE=0` and `ALLOW_NETWORK=1`); env ready (`HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` when needed); shaping fixed per §7.2.

### **7.3.2 Timeouts (closed integers)**

Domains (ms):

* `connect_timeout_ms ∈ {1000,2000,5000}`

* `read_timeout_ms ∈ {2000,5000,10000}`

* `total_timeout_ms ∈ {5000,10000,15000,30000}`

One `timeout_profile ∈ {small, default, long}` pins the triple.

### **7.3.3 Retries (deterministic classes)**

`max_attempts ∈ {0,1,2,3}` (includes the initial try).  
 Retryable classes: `{network_error, 5xx}`. Do not retry other 4xx; 429 handling is defined below (no auto-success in EPIC011).

### **7.3.4 Backoff policy (deterministic; no jitter)**

`backoff ∈ {none, fixed, exponential}` with closed integer params.  
 Schedule respects `total_timeout_ms`; no random jitter.

### **7.3.5 Rate limits & Retry-After (429)**

Map **429** to a typed `PROVIDER_RATE_LIMITED` error (numeric-free).  
 If `Retry-After` parses, surface `retry_after_ms` (int ≥ 0); otherwise omit.  
 EPIC011 does not auto-recover on 429; any success-path retry belongs to a later epic.

### **7.3.6 Observability (keys-only)**

Bounded labels; never log request/response bodies or secret header values; secrets redacted.

### **7.3.7 Failure posture (typed, numeric-free)**

Refusal on closed rails (no I/O); deterministic mapping per §7.2;

* timeouts/exhaustion → `PROVIDER_UNAVAILABLE`

* malformed vendor JSON → `PROVIDER_BAD_RESPONSE`

### **7.3.8 Acceptance to flip rails**

Pin a concrete policy (from the domains above); prove refusal on closed rails; prove conformance on open rails; maintain CLI↔Reader parity; update indices in the same PR.

Acceptance impact.  
 Moves 429 out of retryable set for EPIC011; no token additions (PF04 owns tokens).

---

## **7.4 Adapter data-source policy (PF10-AA) \[Required-Now\]**

**Purpose.** Pin where the adapter reads BodyGraph data in each environment without changing public transport bytes.

**Prod (cached DB on the hot path).**

* Adapter **reads from DB** for all hot-path reads.  
* Direct vendor calls run **only on explicit triggers** (birth-data change, scheduled refresh, operator action).  
* Public transport bytes and A7 surface **do not change**.

**Dev (vendor direct with DB upsert).**

* Direct vendor calls are permitted.  
* The adapter **MUST upsert** the vendor result into the DB to make subsequent reads repeatable.

**Rails & policy.**

* **SAFE rails apply** (see §7.1). Opening rails is an ops decision; this policy does **not** open rails by itself.  
* Transport/A7 posture is unchanged; proofs still run on a **Catalog JSON success** route (§5.6, §5.3).  
* **Persistence is canonical.** BodyGraph **write/read in DB** is part of the standard flow (EPIC011); using the persistent cache is not optional. (Schema and durability mechanics live in **HDE‑Mechanics** and **Glow‑Infrastructure**.)

**Evidence (titles-only; PF12 single home).**

* BodyGraph **source selection snapshot** — `artifacts/bodygraph/source_selection.snapshot.json`  
* Source-invariance **AB / BA / summary** — `artifacts/bodygraph/source_invariance/{ab.json,ba.json,summary.json}`  
* **Release bindings** — `artifacts/bodygraph/release_bindings.json`  
* **Refresh/TTL/SWR policy snapshot** — `artifacts/bodygraph/refresh_policy.snapshot.json`  
* **Metrics snapshot (keys-only)** — `artifacts/bodygraph/metrics.snapshot.json`  
* **Keys-only logs sample (sanitized)** — `artifacts/bodygraph/keys_only.logs.sample`  
* **Indexing discipline:** update PF12 human `docs/evidence/INDEX.json` \+ hash sentinel and machine `artifacts/evidence_index.jsonl` **in the same PR**; each mirror record includes a `proof_anchor`.

**Routing (titles-only).**

* Tokens & policy: **HDE-Governance** (vendor source policy, privacy, keys-only logs).  
* Evidence/indexing: **HDE-Schemas & Artifacts** (PF12).  
* DB names/ownership: **Glow Infrastructure** (names-only).  
* PF05 remains the bytes home for any adapter-emitted request/response examples.

  ---

If you want, I can also append the required **titles** for those BodyGraph artifacts into PF05’s **Appendix D — Evidence Index (titles/paths only)** so it’s easy to see they must appear in PF12’s index/mirror as well.

---

# 

# **8\. Error Model & Exit Codes \[Required-Now\]**

## **8.1 Typed public error object (numeric-free) \[Required-Now\]**

**Shape (minimum). The CLI/Reader typed error is a numeric-free JSON object serialized by the single emitter (UTF-8, sorted keys, compact, one LF):**

**{"ok": false, "code": "\<token\>", "error": "\<non-PII message\>"}**

* **`ok:false` (boolean)**

* **`code` (short machine token; closed vocabulary)**

* **`error` (human-readable, non-PII, non-secret)**

* **Optional: `retry_after_ms` (integer ≥ 0\) when the transport policy explicitly permits it (e.g., vendor 429).**

* **No other fields. Do not echo payloads, secrets, stack traces, or vendor bodies.**

* **LF termination: emitter must append exactly one trailing `\n`.**

## **8.2 Streams discipline \[Required-Now\]**

* **Success → `stdout`. Print the Reader v1 success body (six keys; LF-terminated).**

* **Errors & usage → `stderr`.**

  * **Usage prints a short synopsis; stdout is empty.**

  * **Typed failures print the error object above; stdout is empty.**

* **No mixed streams. Never interleave diagnostics with public bytes.**

## **8.3 Exit codes (taxonomy) \[Required-Now\]**

* **`0` — Success. Public body on stdout (LF-terminated).**

* **`64` — Usage error. Synopsis on stderr; stdout empty.**

* **`2` — Typed failure. Typed error object on stderr; stdout empty.**

**These codes are exhaustive for the public surface. OS/runtime failures must not print partial payloads to `stdout`.**

## **8.4 Determinism & hygiene gates \[Required-Now\]**

* **Canonical emitter. All error/usage outputs follow the same emitter rules as success (UTF-8, sorted keys, compact, one LF).**

* **No ad-hoc dumps. Forbid `json.dumps` and alternate serializers on public paths.**

* **Idempotence posture. Typed errors are not part of the success preimage; success preimage/idempotence checks remain unchanged.**

* **Parity expectations. CLI error serialization must be stable across runs (two-run identity) and deterministic across AB/BA inputs where applicable.**

# 9\. Acceptance & Evidence \[Required-Now\]

## 9.1 Parity (binary)

* **Reader↔CLI byte-equality.** For identical inputs/environment, Reader response bytes and CLI stdout **MUST** be byte-identical (including the single trailing LF).  
* **AB↔BA identity.** Swapping pair order produces **bit-for-bit identical** bytes (pair normalization in effect).  
* **Two-run identity.** Two serializations under identical inputs produce **byte-identical** output.  
  ---

  ## 9.2 Idempotence (binary)

* **Preimage re-check.** Remove `idempotence_hash`, canonicalize the five-key preimage with the single emitter, compute `sha256(preimage_bytes)`, and verify it equals the published `idempotence_hash`.  
* **Scope.** Check holds for **both** Reader **and** CLI outputs.  
  ---

  ## 9.3 Transport (A7) invariants (binary)

* **ETag / 304 / HEAD.** Emit **strong, quoted ETag** on `200`; return `304` **only after** a prior `200`\-with-body for that identity; `HEAD` **mirrors `200` validators** and has **no body**.  
* **304 entity headers (tightened).** **Omit both** `Content-Type` **and** `Content-Length` on `304`; body is empty.  
* **POST is non-conditional.** `POST` never carries validators and never returns `304`.  
* **Cache semantics.** `200`/`HEAD`: `Cache-Control: private, max-age=0, must-revalidate`. Writers/errors: `Cache-Control: no-store`.  
* **Content-Type on 200\.** `Content-Type: application/json; charset=utf-8`.  
* **Vary (required).** `Vary: Authorization, Accept-Encoding` present.  
* **Encoding invariance.** For the same canonical body, the **identity ETag** and **HEAD identity length** (LF-terminated, pre-compression) are stable across accepted `Accept-Encoding` selections (`identity`, `gzip`, `br`).  
  ---

  ## 9.4 Vendor rails acceptance (binary)

* **Refusal posture (rails closed).** With rails closed (any of `SAFE_MODE!=0` **or** `ALLOW_NETWORK!=1`), vendor calls **MUST NOT** perform network I/O and **MUST** return a typed refusal (numeric-free), with secrets redacted.  
* **Shaping correctness (closed).** Request shaping (endpoint, headers, body) remains **deterministic** and **order-neutral** without sending the request.  
* **Conformance when opened.** With rails open and env present, live calls obey pinned **timeouts/retries/backoff**; typed error mapping is deterministic; **no payload/secret logging**; parity/identity remain unaffected.  
  ---

  ## 9.5 Evidence posture (titles-only; PF12 single home)

* **Maintain proofs.** Keep evidence current for: parity (Reader↔CLI, AB↔BA, two-run), idempotence recompute, transport (ETag/304/HEAD, no-store on writers/errors, Vary, encoding-invariance), and vendor rails (refusal closed; conformance open).

* **Index (human).** **`docs/evidence/INDEX.json`** (PF12 §8.6) lists artifacts and scripts (**titles/paths only; no payload bytes**). A **hash sentinel** **`docs/evidence/INDEX.sha256`** gates merges and is **not mirrored**.

* **Machine mirror (single home).** The records-only JSONL mirror lives at **`artifacts/evidence_index.jsonl`** (PF12 §8.3). Human↔machine entries **must be 1:1**; a non one-to-one join is a failure. Each mirror record includes `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` (transcript reference plus on-disk stat). The mirror is **ASCII field-ordered** and **sort-before-write** with **unknown-key rejection**; a **single** mirror file is permitted.

* **Repo docs tokens (PR checklist).** Include `EVIDENCE_INDEX_UPDATED_OK`, **`EVIDENCE_INDEX_HASH_OK`**, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK`.

* **Update discipline (MUST).** When any golden, artifact, or script path changes, update **`docs/evidence/INDEX.json`**, **`docs/evidence/INDEX.sha256`**, and **`artifacts/evidence_index.jsonl`** in the **same commit/PR**, and add a matching entry in **§11 Change Management: Doc-Delta Hooks**.

* **Process routing.** The “update in same PR” workflow and merge gating for the sentinel live in **Epic-Process-Guide** (titles only).

  # **10\. Security & Privacy \[Required-Now\]**

  ## **10.1 Public covenant (numeric-free)**

* **Bands-only, no numerics.** Public Reader bodies are **numeric-free**; `categories[*]` are **exactly** `{id, band}`. No `score`, `score_pct`, or other numeric fields appear on the public surface.

* **Canonical emission only.** All public bytes (success and typed errors) are produced by the **single presenter emitter** (UTF-8, sorted keys, compact, **one LF**).

  ## **10.2 Logging hygiene (keys-only)**

* **No secrets/PII in logs.** Never log request/response bodies, header **values**, or vendor payloads. API keys and tokens **must** be redacted (keys-only posture).

* **Deterministic, bounded labels.** Observability uses bounded enums/labels (route, outcome class, rails state); no user identifiers or free-text payloads in logs.

  ## **10.3 Dev harness containment**

* **Fixtures only; no vendors.** The dev Reader harness uses **local fixtures** and **must not** perform vendor calls.

* **Environment gate.** The harness is enabled **only** when `APP_ENV=dev`; it **must not** be mounted in production.

* **Parity evidence, not a product surface.** The harness exists to prove schema/LF, AB↔BA, two-run, and Reader↔CLI byte parity; it does not relax any privacy rules. 

## **10.4 Admin surfaces: authentication, authorization, and audit**

Admin-only surfaces:

* hdctl admin-bundle

* the admin bundle HTTP route

* any future admin-only routes that expose full product payloads

must follow stricter authentication and audit rules than public Reader or dev harness endpoints.

Authentication and authorization:

* All admin bundle surfaces must require a valid admin credential for access in production.

* Pre-Glow:

  * a high-entropy secret or equivalent credential must be provisioned as a Railway or infrastructure secret

  * CLI and HTTP admin bundle calls must present this credential; unauthenticated calls must not receive an admin bundle

* Post-Glow:

  * admin surfaces must align with the app-level admin identity model once it is defined; until then, they must not be left open

Logging and audit:

* Every successful admin bundle operation must be logged in operations logs with:

  * timestamp

  * caller identity or account

  * a high-level description of the requested match

  * a correlation identifier for tracing

* Logs must:

  * remain keys-only (no secrets, no full bundle payloads, no vendor bodies)

  * be governed by the same retention and PII constraints as other operations logs

QA hooks (names-only; owned elsewhere):

* Governance and QA documents will define QA tokens that ensure:

  * parity between CLI and HTTP admin bundle outputs

  * that admin bundles contain the required structural elements (BodyGraphs, compat JSON, three narratives, meta)

  * that admin surfaces are not callable without the admin credential

* PF05 does not define token semantics; it requires that CLI and HTTP surfaces be designed so such QA checks can be implemented and tied to evidence in the Evidence Index.

Admin surfaces are never part of the Reader public covenant and must remain clearly separated from the A7 success surfaces defined for Reader.

# **11\. Change Log & Doc-Delta Hooks \[Required-Now\]**

## **11.1 Change Log (concise, normative)**

* **Policy.** Log normative deltas only—changes that affect math, the public contract/transport, or acceptance evidence. Pure editorial moves (reordering, wording without byte/evidence impact) need not be logged.  
* **Entry style.** One line per version, action-oriented, with verbs and the smallest set of affected sections/anchors.  
* **Examples (pattern only).**  
  * v0.3 — Remove prompt; retire uncertainty; unify to single presenter emitter; tag sections for status.  
  * v1.0 — Add §7.2 Request Shaping; pin typed error mapping; assert rails refusal posture.  
* **Where to put links.** Evidence artifacts and scripts are indexed in **Appendix D — Evidence Index** (titles/paths only); do not paste payloads or transport bytes here. If the human Index changed, note **“Sentinel updated: YES”** in the Change Log entry (the sentinel is derived from Appendix D and is not mirrored).

  ## **11.2 Doc-Delta Hooks (how we propose, review, and land changes)**

**Purpose.** Provide a uniform, auditable record for any normative change. Each Doc-Delta is self-contained and copy-paste-ready.

### **11.2.1 Doc-Delta template (fill all required fields)**

* **DOC-DELTA-ID:** `CLI-<YYYYMMDD>-<shortslug>`  
* **Date / Author:** `<YYYY-MM-DD> / <name>`  
* **Scope:** (pick one or more) `Math | Public Contract/Transport | Serializer/Emitter | Vendor Ingest | Schema | Acceptance/Evidence | Editorial`  
* **Targets (section anchors):** e.g., `§5.1`, `§7.2.5`, `Appendix D`  
* **Summary (≤5 bullets):**  
  * … (action verb; concrete change)  
  * …  
* **Acceptance impact (binary gates to update):**  
  * Parity (Reader↔CLI, AB↔BA, two-run)  
  * Idempotence (preimage recompute)  
  * Transport (ETag/304/HEAD; no-store on writers/errors)  
  * Vendor rails (refusal closed; conformance open)  
* **Evidence updates (titles/paths only):** goldens, scripts, schema, CI grep-guards to add/update.  
* **Sentinel impact:** `Yes/No`. If **Yes**, recompute the **human Evidence Index hash sentinel** (derived from Appendix D; **not mirrored**) and mark the Change Log entry with “Sentinel updated: YES”.  
* **Freeze-pack impact:** `Yes/No`. If **Yes**, include the new canonical manifest digest and `release_id`.  
* **Routing (titles-only):** confirm that **Architecture/Math** remain referenced by title only and that **this doc** continues to own transport/CLI/vendor bytes—no duplication.  
* **Rollout plan:** CI jobs to update (parity, LF one-trailing-LF check, idempotence, rails refusal), and any gated integration jobs.  
* **PR checklist tokens:** include `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATHS_VALIDATED_OK`.

  ### **11.2.2 Acceptance to land a Doc-Delta (binary outcome)**

A Doc-Delta is **Accepted** only when:

* All implicated binary gates pass (see **Acceptance impact**).  
* **Appendix D (human Index)** and the **machine mirror** at `artifacts/evidence_index.jsonl` are updated **in the same PR** (records-only, path-agnostic).  
* The **human↔machine join is exactly 1:1** (no extras/misses); CI enforces join parity and path proofs under `LC_ALL=C`, `TZ=UTC`.  
* **Sentinel** is recomputed when the human Index changed and is noted in the Change Log entry.  
* Freeze-pack changes (if any) produce a new `release_id` and are logged.

Otherwise, it is **Rejected** (no partial merges).

### **11.2.3 Guardrails (do not regress)**

* **Single emitter.** Reader and CLI must produce public bytes via the same presenter emitter; forbid ad-hoc `json.dumps`.  
* **Numeric-free public.** Reader v1 success remains `{id, band}` only; no numerics on the public surface.  
* **No duplicated bytes.** Architecture/Math are referenced by title only; transport and vendor bytes live here.  
* **Determinism first.** Never introduce jitter or locale/time dependencies; AB↔BA and two-run identity remain required. CI byte comparisons run with `LC_ALL=C`, `TZ=UTC`; JSON is UTF-8 (no BOM), ASCII-sorted keys, compact, exactly one trailing LF.  
* **Process ownership.** The **“update in same PR”** workflow lives in **Epic-Process-Guide** (titles only). **Build Notes are WIP-only and never a single home**; drained items must land in canon.  
  ---

# **Appendices \[Informative / Reference\]**

## **Appendix A — Transport Matrices (headers, conditional rules, examples) \[Required-Now\]**

**Purpose.** Pin the Reader transport behavior the CLI must emit or parity-check. These matrices are normative for CLI/Reader and are kept in lockstep with HDE-Governance §10 (titles only). They cover at minimum: 200 strong quoted ETag; 304-after-200 with no body and omitted Content-Type and Content-Length; HEAD parity (no body; Content-Length equals identity 200 body; Content-Type \== GET); writers/errors no-store with no ETag; and encoding-invariance of identity across Accept-Encoding. Architecture and Math are referenced by title only.

**Proof surface.** Proofs run on a cataloged JSON success route listed in §5.6 (not on `/internal/version`). Byte rules are owned here; examples live in tests and PF12 evidence artifacts (titles only).

### **A.1 Success (200) — required headers**

* Content-Type: `application/json; charset=utf-8`  
* ETag: `"<strong, quoted>"` (identity over the final LF-terminated body; MUST be present on 200; identity is computed over pre-compression bytes)  
* Vary: `Authorization, Accept-Encoding`  
* Cache-Control: `private, max-age=0, must-revalidate`

### **A.2 304 Not Modified (conditional GET)**

**Preconditions.** A prior 200 success with a strong, quoted ETag exists, and the request presents a matching `If-None-Match`.

**Body.** None.

**Headers.**

* ETag present (matches the cached 200\)  
* Mirror 200 validators (Cache-Control, Vary)  
* Omit Content-Type  
* Omit Content-Length

### **A.3 Writers and errors**

* Cache-Control: `no-store` (MUST)  
* No ETag (MUST)  
* Errors: `Content-Type: application/json; charset=utf-8` and LF-terminated body

### **A.4 HEAD parity**

* **Status.** 200  
* **Body.** None  
* **Validators.** Headers equal the 200 success validators for the same resource (including Content-Type)  
* **Length.** `Content-Length == len(identity 200 body)` (pre-compression)  
* **Type.** `Content-Type` on HEAD equals GET

### **A.5 POST semantics**

* **Non-conditional.** Requests do not send validators; responses never return 304\.  
* **Success endpoints.** Successful POST responses on success endpoints include a strong, quoted ETag and the success cache headers from A.1.  
* **Writer-style POSTs.** Remain no-store with no ETag.

### **A.6 Encoding invariance (accepted Accept-Encoding: identity, gzip, br)**

* **Identity stability.** For the same canonical body, the ETag identity is unchanged across accepted encodings.  
* **Length stability.** The effective Content-Length of the identity body is invariant across accepted encodings.  
* **Evidence.** Capture on a cataloged JSON success route; artifacts are listed and indexed in PF12 (human `INDEX.json` \+ hash sentinel \+ machine mirror, same-PR rule).

### **A.7 Aux Narrative (excerpt, Aux Narrative)**

**Aux — Text (200)**  
 *Status:* 200  
 *Content-Type:* `text/plain; charset=utf-8`  
 *ETag:* **present**, strong, quoted (over LF-terminated identity body)  
 *Vary:* `Authorization, Accept-Encoding` (**required**)  
 *Body:* LF-terminated text (no `\r`, no ANSI)

**Aux — Suppressed (200)**  
 *Status:* 200  
 *Content-Type:* (absent or policy-owned; optional `X-Narrative-Policy: suppressed`)  
 *ETag:* **absent**  
 *Vary:* `Authorization, Accept-Encoding` (**required**)  
 *Body:* **empty**

*(Matrices mirror §5.7; A7 proofs remain Catalog-only.)*

## **Appendix B — Vendor Request/Response Examples (typed mapping tables; redact secrets) \[Speculative\]**

**Purpose.** Provide **redacted** examples for HDAPI interactions to aid integration tests. These are **illustrative**, follow §7.2 request shaping, and obey §7.3 policies when rails are open. **Never** include real keys or payload bodies in logs.

### **B.1 Request (redacted example; rails open)**

The canonical vendor BodyGraph request for HDE is:

POST /bodygraphs

with JSON body:

{  
  "birthdate": "YYYY-MM-DD",  
  "birthtime": "HH:MM",  
  "location": "free-text or structured location (see vendor docs)"  
}

and headers:

* `Accept: application/json`

* `Content-Type: application/json; charset=utf-8`

* `HD-Api-Key: <redacted>`

* `HD-Geocode-Key: <optional, redacted>`

* `User-Agent: GlowHDEngine/<release_id>`

HDE does **not** use `POST /bodygraphs/simple`. That endpoint is treated as unsupported for this engine and MUST NOT appear in engine code, QA harnesses, or governed documentation.

**Acceptance impact**

* No new tokens; this redline encodes endpoint policy that is already implied by PF10 and PF01.

* Keeps PF05 as the single home for the on-wire vendor HTTP contract while deferring rails and override policy to PF04.

* **B.2 Response → typed error mapping (deterministic)**  
* `401` → `PROVIDER_UNAUTHORIZED`

* `403` → `PROVIDER_FORBIDDEN`

* `404` → `PROVIDER_NOT_FOUND`

* `429` → `PROVIDER_RATE_LIMITED` (+ `retry_after_ms` if header parses)

* `5xx` → `PROVIDER_UNAVAILABLE`  
   No vendor body echo; secrets redacted; numeric-free error object on stderr (CLI) per §8.

### **B.3 Profiles/placeholders**

* **Timeout profile:** `default|small|long` (see §7.3.2)

* **Backoff:** `none|fixed|exponential` with closed integer params (see §7.3.4)

* **Retries:** `max_attempts ∈ {0,1,2,3}` (see §7.3.3)  
   Pin a single set before enabling production calls; record via Doc-Delta.

---

## **Appendix C — CLI Parity Harness (usage recipes for AB↔BA, two-run) \[Required-Now\]**

**Purpose.** Repeatable recipes to prove **Reader↔CLI byte parity**, **AB↔BA identity**, and **two-run identity**, without exposing vendor calls. The harness is **dev-only** (`APP_ENV=dev`).

### **C.1 Reader↔CLI parity (success)**

1. **Run Reader (dev harness)** with fixture inputs; capture the **LF-terminated** body.

2. **Run CLI** `hdctl showcompat` for the same inputs; capture **stdout**.

3. **Hygiene pre-checks (both bodies):** assert **UTF-8**, **BOM/ANSI-free**, **exactly one LF**, and **six-key success** with `{id,band}` only.

4. **Byte-compare:** bodies **MUST** be identical (same `idempotence_hash`, same single LF).

5. **Preimage re-check:** remove `idempotence_hash`, re-serialize the five-key preimage canonically, and confirm `sha256(preimage_bytes)` equals the published digest.

   ### **C.2 AB↔BA identity**

* Repeat **C.1** for **(A,B)** and **(B,A)**; the two outputs **MUST** match **bit-for-bit** (pair normalization in effect).

  ### **C.3 Two-run identity**

* Repeat the **same** command twice with identical inputs/environment; outputs **MUST** be **byte-identical** (including the single LF).

  ### **C.4 Hygiene**

* Use the **single presenter emitter** on both surfaces; **forbid** ad-hoc `json.dumps` or local “mini-emitters”.

* Enforce schema & LF gates on every run; fail fast on any deviation. 

## **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**

Keep this index synchronized with repo changes. When any golden or artifact path changes, update this list and add a matching entry in §11 (Doc-Delta). Titles and paths only; no payload bytes here. Keep this list in lockstep with HDE-Governance: Appendix D (titles only).

**Mirror parity (MUST).** Every item below must also appear as a records-only line in the machine mirror at `artifacts/evidence_index.jsonl` with: `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` (transcript reference \+ on-disk stat). The mirror is records-only and path-agnostic, ASCII field-ordered, and sort-before-write. **HDE-Schemas & Artifacts** remains the single home for the mirror schema/field ordering.

**Sentinel note.** The human Evidence Index hash sentinel is derived from this appendix and is not mirrored; it gates merges when the human Index changes (see §11).

---

### **D.0 Close-pack & release manifests (admin)**

* `audit/EPIC-009_close_report.md`  
* `audit/EPIC-009_MANIFEST.json`

### **D.1 Parity (Reader↔CLI, AB↔BA, two-run)**

* Goldens: `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Parity harness and tests: `adapter/http_reader.py` (dev-only), `tests/reader_v1/test_emitter.py`, `tests/cli/test_cli_stdout_schema_and_lf.py`  
* Byte-compare scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Composite fingerprint: `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`  
* Integration parity set: `fixtures/composite/integration_abba/*.json`, `audit/gates/determinism/abba_compare_integration.log`

### **D.2 LF and encoding discipline (UTF-8; one LF; no BOM/ANSI)**

* Checks and tests: `tests/cli/test_cli_stdout_schema_and_lf.py`, `tests/reader_v1/test_emitter.py`  
* CI guards: `ci/jobs/lf_and_encoding_check.yml`, `ci/grep-guards/no_ansi_no_bom.regex`

### **D.3 Idempotence coupling (preimage → sha256 → final)**

* Identity marker and logs: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Recompute scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Schema (success, six keys): `schemas/reader.v1.schema.json`

### **D.4 Endpoint Catalog and A7 transport proofs (success endpoints)**

**Endpoint Catalog snapshot (titles only)**

* `artifacts/reader/endpoints_snapshot.json`

**Env-gating proof (headers-only; one LF)**

* `artifacts/proofs/endpoints_env_gate_proof.log` *(shows that non-prod entries are unreachable in prod)*

**A7 proofs (headers-only; one LF per file; proofs run on a cataloged JSON success route, not on `/internal/version`)**

* `artifacts/proofs/success_get.txt`  
* `artifacts/proofs/success_head.txt`  
* `artifacts/proofs/success_304.txt`  
* `artifacts/proofs/success_writers_errors.txt`

**Composite A7 proof (records-only JSON)**

* `artifacts/proofs/reader_success_get_head_304.json`

**Optional encoding-invariance proof**

* `artifacts/proofs/encoding_invariance.txt`

**Aux Narrative (text) snapshots (titles/paths only)**

* `tests/transport/headers/aux_text_200.snap`  
* `tests/transport/headers/aux_head.snap`  
* `tests/transport/headers/aux_304.snap`  
* `tests/transport/headers/aux_suppression.snap`

**Catalog example (informative; titles-only)**

* `docs/ENDPOINTS_CATALOG.json` — list of success routes by title; keep aligned with Appendix D and the machine mirror. *(Populate entries as EPIC-012 ships; until then, keep success proofs/capture files absent or marked pending.)*  
* `docs/ENDPOINTS_CATALOG.json.sha256`

### **D.5 Error headers and writer posture**

* Error response headers (UTF-8): `tests/transport/headers/error_headers_utf8.snap`  
* No-store and no-ETag posture (writers/errors): `tests/transport/headers/no_store_writers_errors.snap`

### **D.6 Single-emitter guard (serializer path)**

* Grep-guard: `ci/grep-guards/no_json_dumps_public.regex`  
* Allowlist for canonical emitter: `ci/grep-guards/canonical_emitter.allowlist`  
* Shared presenter/emitter symbol proof: `audit/gates/canonical_emitter/emitter_symbol_proof.txt`

### **D.7 Canonical JSON checks (public bytes)**

* Policy check: `audit/gates/canonical_json/json_canonical_check.log`  
* Canonical re-serialization compare: `audit/gates/canonical_json/json_canon_compare.log`

### **D.8 showcompat seam (non-empty canonical JSON \+ parity)**

* `artifacts/cli/showcompat/stdout.json` *(LF-terminated, non-empty)*  
* `artifacts/cli/showcompat/two_run_identity.log`  
* `artifacts/cli/showcompat/abba.diff` *(expected empty)*  
* `artifacts/cli/showcompat/reader_cli_parity.diff` *(expected empty)*

### **D.9 Vendor rails (closed refusal and open conformance)**

* Closed-rails refusal proof (single-file canonical; headers → blank line → body): `artifacts/proofs/ops_refusal_proof.txt`  
* Shaping correctness (closed rails): `ci/jobs/logs_keys_only_redaction.yml`  
* Open-rails conformance (timeouts/retries/backoff): `ci/jobs/rails_open_conformance.yml`

### **D.10 Runtime posture & env-resolver envelopes**

* Env snapshot (DB posture): `artifacts/runtime/env_matrix.snapshot.json`  
* Failure envelope (guarded selection-only bytes): `artifacts/runtime/env_matrix.failure.json`  
* **Dev resolver snapshot (rails evidence):** `artifacts/runtime/env_connectivity.snapshot.json`

### **D.11 QA artifacts namespace (transient captures)**

* **Namespace:** `artifacts/qa/` *(transient, test-only captures; titles/paths only — persistent rules live in canon)*

### **D.12 BodyGraph adapter data-source & invariance (PF10-AA)**

* Source selection snapshot: `artifacts/bodygraph/source_selection.snapshot.json`  
* Source invariance (A→B): `artifacts/bodygraph/source_invariance/ab.json`  
* Source invariance (B→A): `artifacts/bodygraph/source_invariance/ba.json`  
* Source invariance (summary): `artifacts/bodygraph/source_invariance/summary.json`  
* Release bindings: `artifacts/bodygraph/release_bindings.json`  
* Refresh/TTL/SWR policy snapshot: `artifacts/bodygraph/refresh_policy.snapshot.json`  
* Metrics snapshot (keys-only): `artifacts/bodygraph/metrics.snapshot.json`  
* Keys-only logs sample (sanitized): `artifacts/bodygraph/keys_only.logs.sample`

*(All BodyGraph artifacts are records-only; add titles-only entries to PF12’s human index and mirror them in `artifacts/evidence_index.jsonl` in the **same PR**, each with a `proof_anchor` path-proof.)*

---

## **Appendix E — Channel Label Glossary (informative; non-contract)**

**Purpose.** A copy/UX aid mapping the **36 canonical channel IDs** to conventional lineage **labels**. This appendix **does not** change payload bytes or schemas. **IDs are authoritative; labels are non-normative.** If channel identifiers ever appear publicly in a future version, they **must** be normalized per PF-Schemas §2.1 to **min→max, zero-padded `NN-NN`** before emission.

**Routing (titles-only):**  
 Public payload contract → PF-Canon-HDE-CLI-API-Vendor-Ref main text; machine catalogs & identity rules → PF-Canon-HDE-Schemas and Artifacts; math/semantics → PF-Canon-HDE-Math-Spec.

---

### **E.1 Canonical IDs → conventional labels**

*(Grouped by center pair for readability; IDs use min→max, zero-padded `NN-NN`.)*

**Head–Ajna (3):**  
 `04-63` — Logic; `24-61` — Awareness; `47-64` — Abstraction

**Ajna–Throat (3):**  
 `17-62` — Acceptance; `23-43` — Structuring; `11-56` — Curiosity

**G–Throat (4):**  
 `01-08` — Inspiration; `07-31` — The Alpha; `10-20` — Awakening; `13-33` — The Prodigal

**Spleen–Throat (2):**  
 `16-48` — The Wavelength; `20-57` — The Brainwave

**Sacral–Throat (1):**  
 `20-34` — Charisma

**Solar Plexus–Throat (2):**  
 `12-22` — Openness; `35-36` — Transitoriness

**G–Sacral (4):**  
 `02-14` — The Beat; `05-15` — Rhythm; `10-34` — Exploration; `29-46` — Discovery

**Spleen–G (1):**  
 `10-57` — Perfected Form

**Ego–G (1):**  
 `25-51` — Initiation

**Solar Plexus–Ego (1):**  
 `37-40` — Community

**Ego–Spleen (1):**  
 `26-44` — Surrender

**Ego–Throat (1):**  
 `21-45` — Money Line

**Sacral–Root (3):**  
 `03-60` — Mutation; `09-52` — Concentration; `42-53` — Maturation

**Sacral–Solar Plexus (1):**  
 `06-59` — Mating

**Sacral–Spleen (2):**  
 `27-50` — Preservation; `34-57` — Power

**Spleen–Root (3):**  
 `18-58` — Judgment; `28-38` — Struggle; `32-54` — Transformation

**Root–Solar Plexus (3):**  
 `19-49` — Synthesis; `30-41` — Recognition/Desire; `39-55` — Emoting

---

### **E.2 Usage notes (copy discipline)**

* Use labels for **UX copy only**; never substitute them for IDs in code, schemas, or evidence.  
* When referencing channels in QA or examples, include the **canonical ID** (e.g., “`10-20` Awakening”).  
* Circuit or tone references are **channel-scoped**, not gate-scoped (see PF-Math/PF-Mechanics).

### **E.3 Evidence hooks (titles/paths only)**

* `audit/gates/topology/orientation_demo.txt` — before/after normalization samples (`high-low` → `min-max` `NN-NN`).  
* (Optional) `fixtures/reference/channel_labels.snapshot.txt` — human-readable dump of the table above (non-contract).

---

