# **0\. Document Control \[Required-Now\]**

## **0.1 Header**

**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref

**Version:** v1.3.1

**Status:** Canon

**Effective date:** 2025-11-21

**Last Update Gate:** BN 7.6.6 Drain

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

* **QA status note (informative).** The CLI is installable and `--help` / `--version` behave correctly. A known issue remains: in some runs `hdctl showcompat` emits **empty output**, violating non-empty canonical JSON and parity requirements (six-key success body, LF-terminated; Reader↔CLI byte equality; AB↔BA and two-run identity). Until that path is corrected, related CLI tokens remain pending (token names live in **HDE-Governance §2**).

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

## **1\) “Map at a Glance” — What’s live vs planned \[Required-Now\]**

### **CLI commands**

* **`hdctl showcompat` — Implemented; *merge-blocking* until Reader↔CLI parity passes.** Prints the public Reader body to **stdout** (six keys, **exactly one LF**, no ANSI). Output **must be non-empty canonical JSON**; **AB↔BA** and **two-run identity** required; **Reader↔CLI byte parity** required. QA: install/help OK; some runs emitted empty output, so related CLI tokens remain pending (tokens tracked in HDE-Governance §2.0).  
   *Notes:* single presenter/emitter (§6.2); stdout only on success, stderr only on errors (§3.3/§3.4); module-runner parity required (`python -m engine.cli`).

* **`read singlebg` — Speculative.** Single-chart read; flags/validators to be defined; not wired.

* **`list people` — Speculative.** Table/JSON listing; sorting/filters to be defined; not wired.

* **Fetch commands (person/batch) — Speculative.** Explicitly disabled in Alpha; activation requires transport acceptance.

  ---

  ### **Reader transport**

* **Endpoint Catalog (JSON success) — Required-Now.** Internal-only and **env-gated** per entry; non-prod entries are **unreachable in prod**. **Single A7 proof surface** (not `/internal/version`). Run 200/HEAD/304 proofs here: **quoted strong ETag** on 200; **Vary: Authorization, Accept-Encoding** required; **HEAD 200 mirrors 200** (no body; **Content-Length \= len(identity 200 body)**); **304 only after 200** and **omits both `Content-Type` and `Content-Length`** (body empty). **Encoding-invariance** holds (ETag and HEAD identity length stable across encodings). Keep Catalog **titles-only, path-agnostic**; file schema in **Appendix B**. Publish:  
   – records-only **Catalog snapshot** → `artifacts/reader/endpoints_snapshot.json`  
   – **env-gate proof (headers-only)** → `artifacts/proofs/endpoints_env_gate_proof.log`  
   – **composite A7 proof JSON** → `artifacts/proofs/reader_success_get_head_304.json` (PF12 schema)  
   – checksum sidecar for the example Catalog file → `docs/ENDPOINTS_CATALOG.json.sha256`

* **Dev harness — Implemented (dev-only).** `/api/reader?v=1` gated by `APP_ENV=dev`; used for schema/LF checks and Reader↔CLI parity. Rails remain closed in dev/CI (`SAFE_MODE=1`, `ALLOW_NETWORK=0`); **no vendor I/O**. Harness proofs are supplemental and **do not replace** Endpoint Catalog A7 proofs.

* **`/internal/version` (ops endpoint) — Required-Now.** Ops-only identity surface; not cacheable. JSON (UTF-8); `Cache-Control: no-store`; **no ETag**; **HEAD=200** with validator parity and `Content-Type == GET`; conditionals ignored (**never 304**); `Vary` optional. Acceptance lives in HDE-Governance §10.5 (titles only).

* **Production Reader surface — Speculative.** Future public endpoint; conditional delivery and headers owned here when enabled.

  ---

  ### **Serializer and emitter**

* **Single canonical emitter shared by CLI and Reader — Required-Now.** UTF-8, sorted keys, compact separators, **exactly one LF**; arrays-as-sets (dedupe \+ ASCII sort); **preimage → idempotence\_hash → final**. **No ad-hoc `json.dumps`**. Both surfaces call the **same entry point**. All byte checks run with `LC_ALL=C`, `TZ=UTC`.

  ---

  ### **Vendor ingest (HDAPI)**

* **Request shaping — Implemented.** Canonical endpoint/method, **dash-case headers**, and **three-key body** (`birthdate`, `birthtime`, `location`) defined; deterministic **typed error mapping** owned here (§7.2).

* **Base-URL resolution — Required-Now.** `HDAPI_BASE_URL` **required** (env); **no literal default**. Missing/empty ⇒ **typed failure (no network I/O)**.

* **Live HTTP gated or disabled by SAFE rails — Required-Now.** Vendor calls allowed **only** when `SAFE_MODE=0` **and** `ALLOW_NETWORK=1`; default **closed** for dev/CI (§7.1).

* **Adapter data-source policy (PF10-AA) — Required-Now.** **Prod:** adapter reads **from DB** on the hot path; vendor calls only on explicit triggers (birth-data change/scheduled refresh/operator). **Dev:** vendor direct allowed; **must upsert** into DB for repeatability (§7.4). Evidence family registered in **Appendix D → D.12**.

* **Production calls — Speculative.** Timeouts, retries, rate limits, observability to be **pinned** (closed enums/integers) prior to enabling (see §7.3).

  ---

  ### **Evidence discipline: indices and parity**

* **Appendix D (human) and machine mirror — Required-Now.** Update **both** in the **same PR**. CI enforces **1:1 parity** and **path-proofs** for all artifacts. Listings are **titles-only**. Machine mirror lives at `artifacts/evidence_index.jsonl` (records-only). Record:  
   – Endpoint-Catalog snapshot → `artifacts/reader/endpoints_snapshot.json`  
   – env-gate proof → `artifacts/proofs/endpoints_env_gate_proof.log`  
   – composite A7 proof JSON → `artifacts/proofs/reader_success_get_head_304.json`  
   – BodyGraph adapter evidence set → see **Appendix D → D.12** (source selection, AB/BA invariance set, release bindings, refresh policy, metrics, keys-only log sample)

  ---

  # **2\. Purpose & Scope \[Required-Now\]**

  ## **2.1 Purpose**

* **CLI \= test & debug tool.** The CLI exists to **exercise and verify** the HD Engine and transport behavior (schema/LF, AB↔BA, two-run, idempotence), not to serve end users.

* **Reader transport & vendor ingest.** This document **owns** the technical bytes for **Reader transport** (public payload, headers/conditional delivery, error mapping) and **Vendor ingest (HDAPI)** (request shaping, typed failures, rails).

* **Integration & acceptance.** The spec provides what’s needed to integrate the engine behind the Glow app and to pass acceptance (evidence, goldens, CI hygiene).

  ## **2.2 Out of scope**

* **Product UX / SPA.** Application UX, narrative copy, and public SPA behavior are **out of scope** here.

* **Routing by title only.** When needed, reference **Architecture** and **Math** **by title only** (no duplicated rules/bytes).

# 

  # **3\) CLI Overview & Conventions \[Required-Now\]**

**QA status note (informative).** The CLI is installable and `--help` / `--version` behave as expected. A known issue remains: in some runs `hdctl showcompat` emits **empty output**, which violates the non-empty canonical JSON and parity requirements (six-key success body, LF-terminated; Reader↔CLI byte equality; AB↔BA and two-run identity). Until that path is corrected, the related acceptance tokens remain **pending**: `CLI_READER_PARITY_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `JSON_CANONICAL_CHECK_OK` (see §2.0 and §4.1). All success output **must** be produced by the single canonical emitter, use UTF-8 with sorted keys and exactly one trailing LF, and be validated under `LC_ALL=C` and `TZ=UTC`.

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

## **3.3 Streams discipline (stdout / stderr) \[Required-Now\]**

**Rules for command output streams.** Transport acceptance (A7) lives in HDE-Governance; do not restate it here. Serialization rules are in §6.1/§6.2.

### **Success → stdout**

* Emit the public body (six keys) **LF-terminated**; **no ANSI**, no prompts, no extra lines, no trailing spaces.  
* **Canonical JSON:** UTF-8 (no BOM), sorted keys (ASCII), compact, exactly one LF; arrays-as-sets deduped & ASCII-sorted.  
* **Reader parity:** stdout bytes **must equal** the Reader body exactly for identical inputs/environment.

### **Usage & typed errors → stderr**

* **Usage:** print a short synopsis; **stdout empty**.  
* **Typed errors:** print a numeric-free error object (see §5.2 Errors) **LF-terminated**; **stdout empty**.  
* **Canonical JSON:** same serializer/emitter and rules as success.

### **No mixed streams**

* Do **not** interleave diagnostics with public bytes.  
* Logs/diagnostics go to **stderr** or files; **never** into stdout payloads. **No secrets/PII** in logs; redact if referenced.

### **Determinism pins**

* Outputs must be **stable** for the same inputs/flags (**two-run identity**).  
* Follow §6.1 canonicalization for **all** JSON emitted.  
* **Locale:** run under `LC_ALL=C`; single LF terminator; UTF-8 only; no BOM/ANSI.

### **Validation (binary)**

1. **Success (0):** `stdout ==` canonical public body (byte-for-byte); **stderr empty**.  
2. **Error/usage:** **stderr** is LF-terminated canonical JSON (or synopsis); **stdout empty**.  
3. **No ANSI / no extra lines:** grep-guard blocks escape sequences; **exactly one LF** at end.  
4. **Canonical compare:** re-serialize and byte-compare outputs (**must match**).  
5. **Reader parity:** CLI stdout **byte-equals** Reader body for identical inputs.  
6. **Determinism:** two-run identity holds for success and error paths.

**Evidence (titles-only; indexed via PF12)**

* CLI success stdout snapshot (six-key body; one LF)  
* CLI typed error stderr snapshot (numeric-free; one LF)  
* Reader↔CLI parity snapshot  
* Two-run identity logs  
* ANSI/extra-line grep-guard report

**Routing (titles-only).** Canonical JSON rules: **HDE-Schemas & Artifacts (§4)**. Governance tokens: **HDE-Governance (§2.0)**.

## **3.4 Exit codes taxonomy \[Required-Now\]**

Exit codes are exhaustive for the public surface. **Non-zero** exits must **not** print partial payloads on stdout. All JSON emitted uses the **single presenter/emitter** (§6.2) and **canonical JSON** (§6.1).

### **Codes**

* **0 — Success.** Print the Reader v1 public body (six keys) to **stdout**, LF-terminated; **stderr empty**.  
* **64 — Usage/config error.** Print a short synopsis (human text) to **stderr**; **stdout empty**. Use 64 for: missing/unreadable input; invalid flags/combination; JSON parse failure; **schema failure; canonicalization failure** (not UTF-8, has BOM/ANSI, unsorted keys, pretty/indented, missing final LF); invalid IANA tz in `--*-tz` (when allowed).  
* **2 — Typed failure (runtime/transport/vendor).** Print a numeric‑free **typed error** to **stderr**; **stdout empty**. Use 2 for: SAFE‑rails refusal (rails closed), **database connectivity failure in non‑dev** (engine unavailable), invalid env (e.g., missing `HD_API_KEY`) with no network I/O, and vendor/transport errors (HTTP 4xx/5xx, network failures). **Deterministic 429** may include `retry_after_ms` (int ≥ 0); otherwise omit.  
* **1 — Unhandled error (internal).** Reserve for unexpected failures; print typed error to **stderr**; **stdout empty**. Treat as a bug until triaged.

### **Global rules**

* **No mixed streams:** non-zero exits print only to **stderr**; **stdout empty**.  
* **No partial payloads:** never print fragments of the success body on stderr/stdout for non-zero exits.  
* **Hygiene:** no ANSI; one LF terminator; UTF-8 only; no BOM.  
* **Determinism:** for the same inputs/flags, exit code and bytes are stable (**two-run identity**); **AB↔BA** does not alter exit code or error bytes.

### **Validation (binary)**

1. **Success (0):** stdout \== canonical success body (byte-for-byte); **stderr empty**.  
2. **Usage (64):** **stderr** shows synopsis; **stdout empty**; grep-guard confirms **no JSON payload**.  
3. **Typed failure (2):** **stderr** is LF-terminated canonical JSON error; **stdout empty**.  
4. **Canonical checks:** re-serialize any JSON and byte-compare (**must match**); one LF; no BOM/ANSI.  
5. **Parity:** for the same scenario, **Reader error body** and **CLI stderr** are byte-identical.  
6. **Determinism:** two-run identity and AB↔BA parity hold for error paths.

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
  ---

  ## **4\. Commands (by status)**

*This section keeps the existing requirements as canon and adds per‑command implementation status based on the Codex CLI audit (no code changes were made in the audit). The audit reports a single `hdctl showcompat` subcommand; both §4.1 and §4.7 describe that same command and will need a later doc reconciliation.*

---

### **4.1 hdctl showcompat \[Implemented\]**

**Purpose (normative).**  
 Produce the Reader v1 public body for a pair of charts and print it to stdout using the single presenter/emitter (six keys, LF‑terminated). The CLI is a test/debug surface; bytes must match Reader for identical inputs and environment. Status: merge‑blocking until Reader↔CLI parity passes.

**Inputs — flags and normalization**

* `--a <path>` / `--b <path>`: paths to canonical chart JSON files (see §3.2 Files).

* `--a-tz <IANA>` / `--b-tz <IANA>`: optional time‑zone overrides only when the chart is missing `tz` (see §3.2). Invalid tz ⇒ typed input error (stderr; stdout empty).

* **Normalization.** The CLI must normalize the pair to canonical order before invoking the engine (AB↔BA neutral).

* **SAFE rails.** This command does not open vendor rails; it exercises in‑proc engine math and the presenter/emitter only.

**Output — public body to stdout**

* **Success payload.** Print the six‑key Reader v1 success object (numeric‑free; `categories[*]` exactly `{"id","band"}`; v1 exposure from §5.1) and terminate with exactly one LF. Output must be non‑empty canonical JSON.

* **Parity.** `stdout` must be byte‑identical to the Reader body for the same inputs and environment. AB↔BA and two‑run identity must hold.

**Serialization and emitter (canonical)**

* **Single emitter.** CLI must call the same presenter/emitter as Reader (§6.2).

* **Canonical JSON.** UTF‑8 (no BOM), sorted keys (ASCII), compact, exactly one trailing LF. Arrays that represent sets are deduped and ASCII‑sorted (§6.1). All byte checks run with `LC_ALL=C`, `TZ=UTC`.

* **No ANSI or prompts.** No color codes, prompts, extra lines, or trailing spaces in stdout.

**Optional flags (disabled by default) \[Speculative\]**

* `--score`: would add a top‑level `score_pct` in CLI‑only output (Reader remains numeric‑free).

* **Admin sidecar.** Opt‑in, file‑backed emission of internal numeric diagnostics with stdout unchanged. Status: disabled by default. Enabling either option requires an approved Doc‑Delta, CI grep‑guards, and refreshed parity/idempotence/LF evidence.

**Errors — typed object to stderr**

* **Usage (exit 64).** Print a short synopsis to stderr; stdout empty.

* **Typed failure (exit 2).** Print a numeric‑free error object to stderr (LF‑terminated; no PII); stdout empty.

* **No mixed streams.** Never interleave diagnostics with public bytes (see §3.3 Streams; §3.4 Exit codes).

**Determinism and acceptance**

* **Idempotence re‑check.** Removing `idempotence_hash`, canonicalize the preimage fields as defined in PF01 and verify `sha256(preimage_bytes)` reproduces the published digest (Reader and CLI).

* **Parity proofs.** AB↔BA and two‑run identity must hold at the byte level; Reader↔CLI bytes must be equal for identical inputs.

* **Acceptance (tokens).** `CLI_SHOWCOMPAT_CANON_OK`, `CLI_TWO_RUN_IDENTITY_OK`, `PARITY_AB_BA_OK`, `CLI_READER_PARITY_OK`, `CLI_STDOUT_LF_OK`, `JSON_CANONICAL_CHECK_OK`, `PREIMAGE_RECOMPUTE_OK`, `CLI_IMPLEMENTED_SET_OK`. (Token names tracked in HDE‑Governance §2.0.)

**Evidence (records‑only; titles‑only; indexed via PF12 machine mirror)**

* `showcompat/stdout` — exact stdout bytes (non‑empty; LF‑terminated) \+ sha256.

* `showcompat/two_run` — two‑run identity log (same bytes twice).

* `showcompat/abba` — AB vs BA byte‑diff (expected empty).

* `reader_vs_cli` — Reader body vs CLI stdout diff (expected empty).

* `preimage_recompute` — recompute log proving `sha256(preimage_bytes)` equals `idempotence_hash`.

Each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor` (transcript anchor \+ on‑disk stat). Update PF12 human `INDEX.json` \+ hash sentinel and the machine mirror in the same PR.

**Routing (titles‑only)**

* Reader payload covenant and preimage: PF01 — HDE‑Math‑Spec (§2.1/§3).

* Canonical JSON and pack/manifest rules: PF12 — HDE‑Schemas & Artifacts (§4).

* Transport behavior (headers/conditionals) and vendor rails: this document (§5.3, §7) and HDE‑Governance (A7).

**Implementation status (audit v1)**

* **Implementation status:** Partially implemented.

* **Evidence:** The audit reports a `hdctl` console script wired to `engine.cli.main:cli`, with a `showcompat` subcommand defined in `engine/cli/main.py`. The subcommand supports `--pair-file`, `--a-file/--a`, `--b-file/--b`, and additional DB/vendor‑related options (user ids and birth tuple fields). Legacy scripts `scripts/hd_cli.py` and `scripts/hdctl.clean.py` also expose `showcompat`‑like flows and compute compat bands with canonical JSON output and optional admin sidecar.

* **Gaps:** The audit does not inspect the JSON payload shape for `hdctl showcompat`, does not confirm that stdout matches the Reader v1 six‑key envelope, and does not validate AB↔BA/two‑run identity, preimage recompute, or the acceptance tokens above. Presence of an optional `--score` flag and diagnostics sidecar is not confirmed. Error envelopes and stream separation are described in canon but not checked in the audit.

  ---

  ### **4.2 hdctl read singlebg \[Speculative\]**

**Purpose (normative, draft).**  
 Emit a single‑chart diagnostic to stdout using the same canonical emitter as Reader/CLI success bodies (UTF‑8, sorted keys, compact, exactly one LF). This command is for testing & debugging chart ingestion/normalization; it is not a product surface.

**Inputs — intended flags & validators \[Speculative\]**

* **Chart path.** Accept one path to a chart JSON file (normalized or raw, per validator).

* **Time‑zone override (optional).** An IANA tz override is permitted only when the chart lacks `tz`.

* **Validation.**

  * Validate against the single‑chart schema (titles‑only reference; owned with the chart provider).

  * Require the minimal fields needed to deterministically construct a normalized chart (birth date, time, place or tz).

  * No best‑effort parsing: missing/invalid date/time/place/tz MUST yield typed failures; do not infer or coerce values.

  * Enforce locale‑neutral parsing and no floats for canonical fields.

* **Note.** Exact flag spellings follow the CLI’s global conventions; final names will be pinned when the command is enabled.

**Stdout schema (single‑chart) \[Speculative\]**

* **Schema ownership.** The single‑chart (BG) schema is referenced by title only (no bytes duplicated here).

* **Canonical emission.** Serialize with the single emitter (UTF‑8, sorted keys, compact, one LF).

* **Numeric‑free public posture.** Output is a diagnostic object for engine inputs; it does not alter the public Reader covenant (no narratives, no prompts).

* **Determinism.** Two identical inputs yield byte‑identical stdout (two‑run identity). AB↔BA does not apply (single input).

**Errors & exits \[Required‑Now\]**

* **Usage (exit 64).** Synopsis to stderr; stdout empty.

* **Typed failure (exit 2).** Numeric‑free error object (LF‑terminated) to stderr; stdout empty.

* **No mixed streams.** Never interleave diagnostics with stdout payloads.

**Status & acceptance gating (to enable later) \[Speculative\]**

* **Schema pinning.** Pin the single‑chart schema title/anchor and add schema tests.

* **Emitter parity.** Prove stdout uses the same emitter as Reader (§6), with one LF and canonical key order.

* **Two‑run identity.** Add byte‑compare fixtures for repeated runs on the same input.

* **CI hygiene.** Grep‑guard against ad‑hoc `json.dumps` and local canonicalizers on this path.

* **Security.** Confirm no PII is written to logs; only stdout/stderr per stream rules.

**Implementation status (audit v1)**

* **Implementation status:** Not implemented.

* **Evidence:** The audit enumerates `hdctl` subcommands `showcompat`, `aux-preview`, and `bg:resolve` in `engine/cli/main.py`. It does not report any `hdctl read singlebg` or equivalently named subcommand. Legacy scripts (`scripts/hd_cli.py`, `scripts/hdctl.clean.py`) implement compat flows but not a single‑chart diagnostic command.

* **Gaps:** The core requirement “CLI can emit a single BodyGraph/chart result via a dedicated command” is not satisfied under this name; single‑chart output likely flows through `bg:resolve` or lower‑level helpers, but the audit does not confirm stdout schema, flags, or determinism for a single‑BG diagnostic surface.

  ---

  ### **4.3 hdctl list people \[Speculative\]**

**Purpose (normative, draft).**  
 List the locally known people entries for test/debug workflows (e.g., feeding `showcompat` by slug/path). This is a developer convenience; it is not a product surface and must not leak PII beyond the stored display name/slug needed for local testing.

**Output modes & streams \[Speculative\]**

* `--format table` (default).

  * Columns: `slug`, `name`, `stored_at`.

  * Rendering: plain text table to stdout, no ANSI, one trailing LF.

* `--format json`.

  * Schema: a JSON array of objects, each exactly `{ "slug": <string>, "name": <string>, "stored_at": <RFC3339 string> }`.

  * Emission: canonical emitter (UTF‑8, sorted keys, compact separators, exactly one LF).

**Errors & usage.** As in §3.3/§3.4: usage → stderr exit 64; typed error → stderr exit 2; stdout empty.

**Sorting rules \[Speculative\]**

* Default: `stored_at` descending (most recent first).

* Alternates: `--sort slug` (ASCII ascending), `--sort name` (ASCII ascending), `--sort stored_at:asc|desc`.

* Determinism: when values tie, break with ASCII ascending `slug`, then `name`. All orders are order‑independent and stable.

**Filters \[Speculative\]**

* Name/slug filter: `--filter "<substring>"` matches case‑insensitive substring on name or slug.

* Time‑window: `--since <RFC3339>`, `--until <RFC3339>` filter by `stored_at` (inclusive).

* Limit: `--limit <N>` returns at most N rows after filtering/sorting (deterministic).

* Exact match (optional): `--slug <slug>` restricts to one entry (fail‑closed if missing).

**Determinism & hygiene \[Required‑Now\]**

* **Canonical JSON.** For `--format json`, use the single presenter emitter (UTF‑8, sorted keys, compact, one LF); no ad‑hoc `json.dumps`.

* **Two‑run identity.** Given the same underlying people store, the same flags produce byte‑identical stdout across runs.

* **No PII beyond schema.** Do not print secrets, internal IDs, or auxiliary metadata. Only `{slug, name, stored_at}`.

**Status & acceptance gating (to enable later) \[Speculative\]**

* Schema pinning; sorting/filter tests; emitter parity; CI hygiene; and security constraints as described in the original text.

**Implementation status (audit v1)**

* **Implementation status:** Not implemented.

* **Evidence:** The audit lists `showcompat`, `aux-preview`, and `bg:resolve` as `hdctl` subcommands; no `list people` or equivalent enumeration command is present. Legacy scripts are focused on compat calculations and admin output, not listing stored people.

* **Gaps:** All behaviour described here (tabular/JSON listing, filters, sorting, and schema) remains unimplemented. Any future implementation must ensure the PII and determinism constraints are enforced.

  ---

  ### **4.4 Fetch commands (person/batch) \[Speculative\]**

**Purpose (normative, draft).**  
 Provide CLI helpers to fetch person data (single/batch) from a vendor service for test/debug and fixture generation. These commands are not product surfaces.

**Status — Explicitly disabled in Alpha**

* **Default posture:** fetch person / fetch batch are disabled.

* **Observed behavior when called:** return a typed error to stderr (exit 2\) stating that fetch commands are disabled in Alpha; stdout empty.

* **No vendor I/O is attempted when disabled.**

**Preconditions to enable (all MUST be satisfied)**

* **SAFE rails & env**

  * Rails explicitly opened: `SAFE_MODE=0` and `ALLOW_NETWORK=1`.

  * Required env/keys present and non‑empty (e.g., `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`). Never print secrets.

* **Request shaping completeness (owned in this document)**

  * Canonical endpoint/method, headers, and body schema (birthdate, time, location) pinned.

  * Typed error mapping from vendor responses to CLI/Reader error tokens (numeric‑free).

* **Transport acceptance**

  * Timeouts, retries, rate‑limit/backoff policies pinned (closed enums/integers).

  * Observability: bounded counters/timers only (no PII, no payload logging).

  * Refusal posture proven when rails are closed (no outbound calls).

* **Determinism & hygiene**

  * CLI stdout (on success) still prints only the public Reader bytes or a pinned fetch result schema (if different), via the single presenter emitter (UTF‑8, sorted keys, compact, one LF).

  * No ad‑hoc `json.dumps` on public paths; no ANSI to stdout.

* **Security & privacy**

  * No PII beyond explicitly allowed fields in the fetch schema; secrets never echoed.

  * Redaction rules for logs firmly applied; stderr contains only typed tokens/messages.

* **Evidence & CI**

  * Goldens for idempotence, LF discipline, AB↔BA (if pair‑derived), two‑run identity; CI grep‑guards; network tests gated on rails.

**Command sketches (deferred/speculative)**

* `hdctl fetch person --name <str> --birthdate <YYYY-MM-DD> --birthtime <HH:MM> --place "<City, CC>" [--tz <IANA>]`

* `hdctl fetch batch --file <CSV|JSON>`

Exact flag names, stdout schemas, and mapping tables are pinned in this document when the feature is enabled; until then, these commands remain disabled by default.

**Routing (titles‑only)**  
 Reader payload covenant and serializer rules are referenced by title only in Architecture/Math; this document owns transport/vendor bytes (headers, validators, error mapping).

**Implementation status (audit v1)**

* **Implementation status:** Not implemented (and disabled by design).

* **Evidence:** The audit finds no `fetch`‑prefixed `hdctl` subcommands or equivalent person/batch fetch commands. It also notes no network‑calling CLI commands beyond those implied by `bg:resolve` using `resolve_bodygraph`, whose external behaviour is not inspected.

* **Gaps:** All fetch behaviour remains speculative; if these commands are added, they must satisfy the rails, privacy, and determinism constraints above.

  ---

  ### **4.5 CLI Admin Preview (narrative) \[Required‑Now\]**

**Purpose.**  
 Admin preview of Aux narrative text via the shared presenter/emitter used by Reader (no change to Reader public contract).

**Posture (EPIC‑010)**

* “CLI” for this epic refers to the admin preview surface exposed over HTTP that calls the same emitter as Reader. A local binary (for example, `hdctl`) is not normative for acceptance.

* Enabled by default (admin‑only) across dev, stage, and production; no environment gate.

**Outputs and hygiene**

* **stdout:** LF‑terminated text; no carriage returns, no ANSI, no extra lines.

* **Sidecar (ids‑only):** canonical JSON written by the single emitter; UTF‑8, sorted keys, compact, exactly one LF; no prose.

* **Fields (names‑only):** `pack_sha`, `composition_id`, `fragment_ids[]`, optional `release_id`. (Schema ownership lives in HDE‑Schemas and Artifacts.)

**Determinism and parity**

* Uses the same emitter as Aux; for identical inputs, preview bytes match Aux emitter bytes.

* **Acceptance (titles‑only):** `CLI_PREVIEW_ENABLED_OK`, `CLI_READER_EMITTER_PARITY_OK`, `CLI_PREVIEW_INDEXED_OK`.

**Evidence (titles/paths only; PF12 single home)**

* `artifacts/cli/narrative/stdout.txt` — LF‑terminated narrative text (no ANSI).

* `artifacts/cli/narrative/sidecar.json` — ids‑only canonical JSON.

Index both with the human Evidence Index and the machine JSONL mirror in the same PR. PF12 governs indexing and mirror behavior.

**Implementation status (audit v1)**

* **Implementation status:** Partially implemented (CLI entrypoint only).

* **Evidence:** The audit reports a `hdctl` subcommand `aux-preview` in `engine/cli/main.py` with flags `--category`, `--band` (using an `AUX_BANDS` enum), `--pair-file`, `--show-narrative` (boolean), and `--admin-out`. It further notes that `hdctl aux-preview` “reads compat pair file, optionally writes admin output via `get_pack/emit_public_aux`,” indicating a CLI wires into the Aux emitter for narrative preview.

* **Gaps:** The audit does not examine the HTTP admin preview surface described here, does not verify LF‑only text output and sidecar schema, and does not confirm indexing of `artifacts/cli/narrative/*`. It also does not validate acceptance tokens or access control (admin‑only behaviour). Narrative count and category coverage (3× narratives per category) are not checked.

  ---

  ### **4.6 hdctl bg:resolve \[Required‑Now\]**

**Purpose.**  
 Operator‑facing command to resolve a BodyGraph with explicit per‑call source selection. The Engine remains mode‑free; selection is externalized to the adapter via this command.

**Flags (normative).**

* `--user <uuid>` — target user identifier.

* `--source {db|vendor|auto}` — choose data source.

  * `db` — use persistent BodyGraph (if present); no vendor call.

  * `vendor` — perform a live fetch only if rails are open; on success, upsert to DB.

  * `auto` — adapter default (check DB, then follow environment policy).

* `--upsert` — when `--source=vendor`, upsert result to DB (idempotent per uniqueness/fingerprint; details live in PF14).

**Rails interaction.**  
 If rails are closed, `--source=vendor` yields a typed refusal (no network I/O).

**Streams & exit codes.**  
 Success prints canonical JSON via the single emitter; typed failures print to stderr and exit 2; usage exits 64 (see §3.3–§3.4).

**Evidence & routing (titles‑only).**  
 Source‑selection snapshots and invariance set under Appendix D → D.12; persistence/home and DB mechanics live in HDE‑Mechanics; governance tokens live in HDE‑Governance.

**Acceptance impact.**  
 None new; documents an implemented path from PF10 (per‑call source).

**Implementation status (audit v1)**

* **Implementation status:** Partially implemented.

* **Evidence:** The audit describes a `hdctl` subcommand `bg:resolve` in `engine/cli/main.py` with required `--user` and optional `--source {auto,db,vendor}` (default `auto`), plus `--upsert` and `--dry-run`, and vendor birth tuple fields. It notes that `hdctl` uses `_resolver_env()` reading `SAFE_MODE`, `ALLOW_NETWORK`, and `APP_ENV`; DB source modes use supplied user IDs, and vendor modes use birth tuple arguments. It further states that `hdctl bg:resolve` calls `resolve_bodygraph`, which may access DB or vendor, and “writes public payload to stdout only.”

* **Gaps:** The audit does not verify that `--source` semantics exactly match the policy above, does not inspect the BodyGraph JSON schema, and does not test rails‑closed behaviour, typed refusals, or evidence/indexing for source selection. It also does not confirm that this satisfies the “single BodyGraph output” diagnostic requirement from §4.2.

  ---

  ### **4.7 hdctl showcompat \[Required‑Now\]**

`hdctl showcompat` is the canonical compat harness for comparing two users and driving Aux narrative preview. It is an admin/QA tool; it is not a public API.

It binds three things together:

* The Reader v1 public envelope (compat result exposed to clients).

* The compat math over Magic‑10 categories and bands (owned by the HDE Math Spec).

* Aux narrative selection (owned by the Narratives Guide and Narrative Deliverables).

  #### **4.7.1 Inputs (normative)**

`showcompat` supports three input families:

**DB‑backed users**

* hdctl showcompat \--user-a \<idA\> \--user-b \<idB\> \[--source {db|vendor|auto}\]  
* or equivalent aliases:  
* hdctl showcompat \--a-user \<idA\> \--b-user \<idB\> \[--source {db|vendor|auto}\]  
    
* `--user-a` / `--a-user`, `--user-b` / `--b-user` are internal user ids.

* `--source` has the same semantics as in `bg:resolve`:

  * `db` — both BodyGraphs are fetched from DB only (no vendor).

  * `vendor` — both are resolved from vendor only.

  * `auto` — DB‑first, vendor‑fallback for each user independently.

**File inputs (fixtures)**

* hdctl showcompat \--file \<path\>  
    
* `<path>` is a compat fixture file containing the two BodyGraphs and any required metadata.

* No DB or vendor access occurs in this mode.

**STDIN**

* cat compat\_input.json | hdctl showcompat \--stdin  
    
* Reads BodyGraphs and metadata from STDIN.

* No DB or vendor access occurs in this mode.

In all modes, user ids and other internal identifiers never leave the engine; they are used only to locate BodyGraphs and inputs in internal storage.

#### **4.7.2 Output (normative)**

On success, `showcompat` MUST emit the Reader v1 public envelope on stdout.

**Shape:**

* Exactly the success envelope defined in §5.1 (six‑key, numeric‑free JSON).

* Canonical JSON: UTF‑8, sorted keys, compact separators, exactly one trailing LF.

* No compat‑internal or vendor‑specific fields are added to the public envelope.

**Semantics:**

* Represents the compat result for the input pair (bands and key indicators).

* Is byte‑identical to what the public Reader API would return for the same underlying BodyGraphs.

Compat “rich” JSON (scores, feature flags, internal diagnostics) is allowed only in admin/test artifacts, such as sidecar files or dedicated admin commands; it MUST NOT be added to the on‑wire Reader envelope or to `showcompat` stdout.

#### **4.7.3 Exit status and parity**

**Exit status:**

* 0 on success (Reader v1 envelope emitted on stdout).

* Non‑zero on any typed failure (error envelope as defined in the JSON error section).

**Reader/CLI parity:**

* For DB‑backed runs with `--source db`, `showcompat` stdout MUST be byte‑identical to the Reader v1 success body for the same pair.

* Appendix C.1 defines the parity harness that enforces this equality.

  #### **4.7.4 Usage with Aux preview**

`showcompat` can be used to generate compat inputs for `hdctl aux-preview`:

* Admin/test compat JSON (when produced) is written to a file (e.g., via separate admin flags or tools) and consumed by `aux-preview` via `--pair-file`.

* `aux-preview` uses that compat JSON to drive Aux narrative selection but does not reach DB or vendor; see §4.5 and §5.7 for details.

**Acceptance impact.**  
 Aligns CLI behaviour with existing Reader v1 envelope spec and the CLI/Reader parity harness in Appendix C. No new acceptance tokens are introduced; this section clarifies behaviour required for existing CLI/Reader parity and narrative preview tokens elsewhere.

**Implementation status (audit v1)**

* **Implementation status:** Partially implemented.

* **Evidence:** The audit confirms a `hdctl showcompat` subcommand in `engine/cli/main.py` with:

  * File/STDIN inputs (`--pair-file`, `--a-file/--a`, `--b-file/--b`) and

  * DB/vendor inputs via user‑id and birth‑tuple options (`--user-a/--user-b`, and vendor birthdate/time/location flags),  
     and notes that these modes are validated in code. It also summarizes behaviour as “hdctl showcompat: may read JSON from files or stdin; can write compat‑related output depending on source,” and references legacy CLIs (`scripts/hd_cli.py`, `scripts/hdctl.clean.py`) that read charts and compute compat bands.

* **Gaps:** The audit does **not** describe the exact JSON envelope emitted by `hdctl showcompat`, does not confirm that stdout matches the six‑key Reader v1 envelope, and does not verify inclusion or exclusion of scores, bands, or narrative keys. It does not validate parity with the Reader API, exit codes, or the Aux preview integration described here. As a result, the core requirement “compat run produces a Reader v1 envelope on stdout while rich compat JSON (scores, bands, narratives) lives only in sidecars/admin commands” remains unverified and may be in conflict with actual compat‑JSON behaviour in legacy CLIs.

  ---

  ### 4.8 mplementation Matrix (audit v1)

* | Requirement / area                                     | Spec location        | Status from audit       | Key CLI touchpoints                                    | Gap / note                                                                                                  |  
* |--------------------------------------------------------|----------------------|-------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|  
* | hdctl showcompat – file AB/BA harness                  | §4.1                 | Partially implemented   | \`hdctl\` subcommand \`showcompat\`; \`scripts/hd\_cli.py\`, \`scripts/hdctl.clean.py\` | Command and flags exist; audit does not confirm Reader v1 envelope, AB↔BA harness, or preimage/identity checks. |  
* | hdctl read singlebg – single-chart diagnostic          | §4.2                 | Not implemented         | None reported                                          | No \`read singlebg\` subcommand; single BG output likely via \`bg:resolve\` but not exposed as this command.     |  
* | hdctl list people                                      | §4.3                 | Not implemented         | None reported                                          | No listing command for people; all behaviour here remains speculative.                                       |  
* | Fetch commands (person/batch)                          | §4.4                 | Not implemented         | None reported                                          | No \`fetch\` CLI commands; feature remains disabled/speculative as intended.                                   |  
* | CLI Admin Preview (HTTP Aux emitter)                   | §4.5                 | Partially implemented   | \`hdctl aux-preview\` subcommand                         | CLI aux-preview exists and calls Aux emitter; audit does not cover HTTP admin surface or evidence/indexing.  |  
* | hdctl bg:resolve – BodyGraph resolver                  | §4.6                 | Partially implemented   | \`hdctl\` subcommand \`bg:resolve\`                        | Flags and env handling implemented; audit does not inspect BG schema, rails-closed behaviour, or evidence.   |  
* | hdctl showcompat – compat harness for Aux/Reader       | §4.7                 | Partially implemented   | \`hdctl\` subcommand \`showcompat\`; legacy compat scripts | Inputs match design (file/STDIN, DB/vendor); emitted JSON shape and Reader parity are unknown from audit.    |  
* | Core: single BodyGraph output capability               | §§4.2, 4.6           | Partially implemented   | \`hdctl bg:resolve\`; helper scripts                     | Resolver command exists and writes a public payload; dedicated \`read singlebg\` CLI and stdout schema unpinned.|  
* | Core: compat outputs (scores, bands, narratives)       | §§4.1, 4.5, 4.7      | Unknown from audit       | \`hdctl showcompat\`, \`hdctl aux-preview\`, \`scripts/hdctl.clean.py\` | Audit mentions compat bands and narrative preview flags, but does not inspect JSON payload to confirm scores or narrative keys per category. |  
* | Core: BodyGraph data source selection (DB vs vendor)   | §§4.6, 4.7           | Partially implemented   | \`hdctl bg:resolve \--source\`, \`hdctl showcompat \--source\`; \`\_resolver\_env()\` | CLI exposes \`--source {auto,db,vendor}\` and uses env rails; internal resolver semantics and guardrails are not fully audited. |  
* | Doc-level: two showcompat specs (4.1 vs 4.7)           | §§4.1, 4.7           | Conflict in docs; one CLI | Same \`hdctl showcompat\` subcommand                     | Audit sees a single \`showcompat\` command; the two doc sections describe overlapping but not clearly unified behaviour and must be reconciled separately. |


If you want, next step can be a much narrower follow-up prompt for Codex that turns the “Unknown from audit” cells (especially compat scores/bands/narratives and Reader envelope parity) into concrete tests or small probe scripts, still without changing any code.

* 

  # **5\. Reader Transport (public bytes) \[Required-Now\]**

\*\*Cross-doc alignment (titles-only).\*\* Transport matrices and acceptance checklists are mirrored in PF-Canon-HDE-Governance; this chapter owns the bytes; Appendix A remains aligned.

## 5.1 Success envelope \[Required-Now\]

Body shape (six keys). The Reader v1 success body contains exactly these six top‑level keys — no extras:

* `reader_version` — fixed string `"v1"`.

* `eligible` — boolean.

* `categories` — array of items exactly `{ "id", "band" }`.

* `meta` — object exactly `{ "engine_tag", "invocation_tag" }`.

* `release_id` — lowercase 64‑hex string.

* `idempotence_hash` — lowercase 64‑hex string.

CLI and admin compatibility surfaces.

* The Reader v1 success envelope above is the **only** public compat payload exposed by the Reader API. It remains six‑key and numeric‑free.

* The compat engine also produces a richer compat JSON structure (scores, bands, narrative keys, and per‑category metadata) used for admin/test workflows. This richer JSON is **not** the Reader v1 envelope.

* `hdctl showcompat` is an admin/QA tool. In its current implementation it:

  * Resolves the pair inputs and viewer preferences.

  * Computes full compat JSON (including `score`, `band`, and narrative key fields for each category).

  * Emits that compat JSON to `stdout` as a single LF‑terminated canonical JSON document of the form `{ "a": {…}, "b": {…}, "viewer_prefs": {…}, "compat": { "categories": [...], "meta": {...} } }` (shape owned by HDE‑CLI‑API‑Vendor‑Ref and HDE‑Mechanics; titles‑only).

  * Optionally writes the Reader v1 success envelope bytes to a file via its reader‑dump path; those bytes are generated through the same `emit_reader_public_envelope` path as the Reader API.

* When the Reader v1 envelope is produced (by the Reader API or by the CLI reader‑dump path), its bytes **MUST**:

  * Match the six‑key shape defined above, with no additional fields.

  * Be canonical JSON per §6.1 (UTF‑8, sorted keys, compact, exactly one trailing LF).

  * Be byte‑identical across Reader and CLI for the same underlying compat result and environment (used for parity tests and evidence).

Richer compat JSON (including numeric scores and narrative selection keys) is restricted to admin/test artifacts (for example, `hdctl showcompat` compat JSON, admin sidecars, and Aux preview inputs). These admin surfaces **must not** extend or change the Reader v1 public envelope; the six‑key envelope remains numeric‑free and field‑closed.

Categories (v1 Alpha).

* If `eligible == true`: emit exactly one item `{"id": "harmony", "band": …}` in `categories`.

* If `eligible == false`: `categories` MAY be `[]`.

* Each item in `categories` is exactly `{ "id", "band" }`.

  * `band ∈ {"Cool","Open","Warm","Glow"}`.

  * No numeric fields (scores) or narrative fields appear in `categories`.

* `id` MUST come from the Magic‑10 closed set (see HDE‑Schemas & Artifacts §2.6 and HDE‑Math‑Spec §5.1). The v1 envelope publicly exposes only the `"harmony"` category; the full Magic‑10 framework (scores, bands, narrative keys per category) remains internal to compat and admin/test JSON surfaces.

Emission algorithm (success case).

1. Build preimage (defer to HDE‑Math‑Spec). Construct the idempotence preimage exactly as defined in HDE‑Math‑Spec §3. The preimage contains all fields required there and **excludes** `idempotence_hash` itself.

2. Canonicalize & hash.

   * Serialize the preimage with the single shared emitter and canonical JSON rules (§6.1) to obtain `preimage_bytes`.

   * Compute `idempotence_hash = sha256(preimage_bytes)` (lowercase 64‑hex).

3. Finalize.

   * Add `idempotence_hash` to the envelope.

   * Re‑serialize with the same emitter to produce the final success body bytes (LF‑terminated).

Serialization. Canonical JSON (§6.1):

* UTF‑8 (no BOM).

* ASCII‑sorted keys.

* Compact separators.

* Exactly one trailing LF.

* Arrays used as sets are deduped and ASCII‑sorted.

* All byte checks run under `LC_ALL=C`.

Public covenant.

* The Reader v1 success body is numeric‑free.

* Fields such as `score`, `prompt`, `uncertainty`, narrative keys, or any other internal compat diagnostics MUST NOT appear in the Reader v1 envelope.

* Numeric scores and narrative keys exist only in internal compat/admin JSON (for example, compat JSON from `showcompat` and Aux preview inputs), never in the public Reader v1 response.

Determinism and parity.

* AB vs BA: normalization at the compat layer guarantees identical preimages and identical final Reader v1 envelope bytes for `{a,b}` and `{b,a}`.

* Two‑run identity: two serializations with the same inputs produce byte‑identical Reader v1 envelope bytes.

* Reader vs CLI:

  * When the CLI produces Reader v1 bytes (via the reader‑dump path), those bytes MUST be identical to the Reader API success body for the same inputs and environment.

  * CLI compat JSON (admin/test) is canonical JSON and deterministic, but it is a distinct envelope from the Reader v1 public envelope.

Routing (titles‑only).

* Canonical JSON & pack/manifest rules: HDE‑Schemas & Artifacts.

* Magic‑10 IDs, scoring, and band selection: HDE‑Math‑Spec and HDE‑Mechanics Guide.

* Transport status & headers: HDE‑Governance (A7) and this document’s §5.3.

* Preimage/idempotence details: HDE‑Math‑Spec §3.

* CLI compat JSON shape and admin/test evidence surfaces: HDE‑CLI‑API‑Vendor‑Ref and HDE‑Mechanics Guide.

Normalization note (informative). If future versions surface channel identifiers in public payloads, they MUST be normalized per HDE‑Schemas & Artifacts §2.1 to `NN-NN` (zero‑padded, min‑first) before emission. IDs remain authoritative; labels are non‑normative.

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

* `grep_guard/report` — proves no disallowed serializers on public paths.  
* `emitter_symbol/proof` — import-graph or reflection proof of the shared presenter symbol used by Reader and CLI.  
* `parity/fixtures` — byte-compare cases showing **CLI stdout equals Reader body** for the same inputs (see parity artifacts referenced in **PF12 Appendix C**).  
* **Indexing discipline:** update **PF12** human Evidence Index and hash sentinel and the machine mirror **in the same PR**; each mirror record includes `artifact_key`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and `proof_anchor` (transcript anchor \+ on-disk stat).

**Routing (titles-only).** Canonical JSON rules: **HDE-Schemas & Artifacts (§4)**. Governance tokens: **HDE-Governance (§2.0 Acceptance Tokens)**.

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

* **Alternate endpoint:** `POST /bodygraphs/simple` (CLI may expose `--vendor-mode full|simple`, default `full`).

* **Base-URL resolution (no fallback).** Resolve **only** from `HDAPI_BASE_URL`. If missing or empty, fail with typed error (see §7.1). Do **not** default to a literal.

* **Method rules.** `POST` is normative for JSON bodies. `GET` must not carry a request body (if ever used for a dev-harness health probe only).

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

